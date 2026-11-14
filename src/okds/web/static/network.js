/* Discovery Network (prototype): interactive graph of the Knowledge Objects, plus the research-discovery concept.
   No libraries: a small force layout drawn in SVG. All KO text is inserted with textContent. */
"use strict";
(() => {
  const { $, el, safeUrl } = KO;
  const D = JSON.parse($("#net-data").textContent);
  const NET = D.net, SVGNS = "http://www.w3.org/2000/svg";
  const W = 900, H = 560;
  const COLORS = { Condition: "#d1495b", AnatomicalStructure: "#8d6cc4", DiagnosticTest: "#2a9d8f", Treatment: "#3b82c4",
    Procedure: "#e07b39", Device: "#6b7a8f", RehabProtocol: "#5aa469", OutcomeMeasure: "#c9a227", Concept: "#8f9aa6" };
  const color = t => COLORS[t] || "#8f9aa6";
  const words = p => (p || "").replace(/_/g, " ").toLowerCase();
  const byId = new Map(NET.nodes.map(n => [n.id, n]));
  const edges = NET.edges.filter(e => byId.has(e.source) && byId.has(e.target));
  const degree = new Map();
  edges.forEach(e => { if (!e.proposed) { degree.set(e.source, (degree.get(e.source) || 0) + 1); degree.set(e.target, (degree.get(e.target) || 0) + 1); } });
  const radius = n => (n.kind === "ko" ? 10 : 7) + 2.2 * Math.sqrt(degree.get(n.id) || 0);

  // ---------------------------------------------------------------- layout (deterministic force simulation)
  let seed = 7; const rand = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const P = new Map();
  // Lay out the written KOs on their own when proposed topics start hidden, so they spread over the frame.
  const layoutAll = NET.nodes.filter(n => n.kind === "proposed").length <= 60;
  NET.nodes.forEach(n => {
    const a = ((n.cluster || 7) / 7) * Math.PI * 2 + rand() * 0.9, r = n.kind === "ko" ? 120 : 230;
    P.set(n.id, { x: W / 2 + Math.cos(a) * r * (0.6 + rand() * 0.5), y: H / 2 + Math.sin(a) * r * 0.75 * (0.6 + rand() * 0.5), vx: 0, vy: 0, fixed: false });
  });
  function simulate(ticks, ids = [...P.keys()], frozen = new Set()) {
    const inSet = new Set(ids), simEdges = edges.filter(e => inSet.has(e.source) && inSet.has(e.target));
    for (let t = 0; t < ticks; t++) {
      const alpha = 1 - t / ticks;
      for (let i = 0; i < ids.length; i++) for (let j = i + 1; j < ids.length; j++) {
        const a = P.get(ids[i]), b = P.get(ids[j]);
        let dx = a.x - b.x, dy = a.y - b.y, d2 = dx * dx + dy * dy || 0.01;
        const f = 2600 / d2, d = Math.sqrt(d2); dx /= d; dy /= d;
        a.vx += dx * f; a.vy += dy * f; b.vx -= dx * f; b.vy -= dy * f;
      }
      simEdges.forEach(e => {
        const a = P.get(e.source), b = P.get(e.target), dx = b.x - a.x, dy = b.y - a.y, d = Math.hypot(dx, dy) || 1;
        const k = (d - (e.proposed ? 90 : 130)) * 0.06;
        a.vx += dx / d * k; a.vy += dy / d * k; b.vx -= dx / d * k; b.vy -= dy / d * k;
      });
      ids.forEach(id => {
        const p = P.get(id);
        p.vx += (W / 2 - p.x) * 0.002; p.vy += (H / 2 - p.y) * 0.004;
        if (!p.fixed && !frozen.has(id)) { p.x += Math.max(-12, Math.min(12, p.vx * alpha)); p.y += Math.max(-12, Math.min(12, p.vy * alpha)); }
        p.vx *= 0.5; p.vy *= 0.5;
        p.x = Math.max(30, Math.min(W - 30, p.x)); p.y = Math.max(24, Math.min(H - 30, p.y));
      });
    }
  }
  function stretch(ids) {  // use the whole wide frame: map these topics' bounds onto it
    const ps = ids.map(id => P.get(id)), xs = ps.map(p => p.x), ys = ps.map(p => p.y);
    const [x0, x1, y0, y1] = [Math.min(...xs), Math.max(...xs), Math.min(...ys), Math.max(...ys)];
    ps.forEach(p => { p.x = 70 + (p.x - x0) / ((x1 - x0) || 1) * (W - 140); p.y = 40 + (p.y - y0) / ((y1 - y0) || 1) * (H - 90); });
  }
  const core = NET.nodes.filter(n => layoutAll || n.kind !== "proposed").map(n => n.id);
  simulate(420, core);
  stretch(core);
  if (!layoutAll) {  // then hang each proposed topic next to the KO that proposed it, and let them settle
    NET.nodes.filter(n => n.kind === "proposed").forEach(n => {
      const host = P.get(n.proposed_by[0]) || { x: W / 2, y: H / 2 }, a = rand() * Math.PI * 2;
      Object.assign(P.get(n.id), { x: host.x + Math.cos(a) * 60, y: host.y + Math.sin(a) * 45 });
    });
    simulate(120, [...P.keys()], new Set(core));
  }

  // ---------------------------------------------------------------- state and filters
  const preds = [...new Set(edges.map(e => e.predicate))].sort();
  // With many proposed topics the full view is too busy: start with written KOs only (the checkbox adds the rest).
  const S = { selected: null, depth: 0, proposed: NET.nodes.filter(n => n.kind === "proposed").length <= 60, preds: new Set(preds) };
  $("#net-proposed").checked = S.proposed;
  const predBox = $("#net-preds");
  preds.forEach(p => {
    const l = el("label"), c = el("input"); c.type = "checkbox"; c.checked = true;
    c.addEventListener("change", () => { c.checked ? S.preds.add(p) : S.preds.delete(p); draw(); });
    l.appendChild(c); l.appendChild(document.createTextNode(" " + words(p))); l.title = NET.predicates[p] || ""; predBox.appendChild(l);
  });
  const legend = $("#net-legend");
  [...new Set(NET.nodes.map(n => n.ko_type))].filter(Boolean).sort().forEach(t => {
    const s = el("span", "lg"); const dot = el("i"); dot.style.background = color(t); s.appendChild(dot); s.appendChild(document.createTextNode(t)); legend.appendChild(s);
  });

  function visibleEdges() { return edges.filter(e => S.preds.has(e.predicate) && (S.proposed || !e.proposed)); }
  function visibleNodes(vEdges) {
    let keep = new Set(NET.nodes.filter(n => S.proposed || n.kind !== "proposed").map(n => n.id));
    if (S.selected && S.depth > 0) {
      const near = new Set([S.selected]); let frontier = [S.selected];
      for (let d = 0; d < S.depth; d++) {
        const next = [];
        vEdges.forEach(e => {
          if (frontier.includes(e.source) && !near.has(e.target)) { near.add(e.target); next.push(e.target); }
          if (frontier.includes(e.target) && !near.has(e.source)) { near.add(e.source); next.push(e.source); }
        });
        frontier = next;
      }
      keep = new Set([...keep].filter(id => near.has(id)));
    }
    return keep;
  }

  // ---------------------------------------------------------------- drawing
  const svg = $("#net-svg");
  const mk = (tag, attrs) => { const e = document.createElementNS(SVGNS, tag); Object.entries(attrs || {}).forEach(([k, v]) => e.setAttribute(k, v)); return e; };
  function draw() {
    svg.textContent = "";
    const defs = mk("defs"), marker = mk("marker", { id: "arrow", viewBox: "0 0 10 10", refX: "10", refY: "5", markerWidth: "6", markerHeight: "6", orient: "auto-start-reverse" });
    marker.appendChild(mk("path", { d: "M0,0 L10,5 L0,10 z", class: "arrowhead" })); defs.appendChild(marker); svg.appendChild(defs);
    const vEdges = visibleEdges(), keep = visibleNodes(vEdges);
    fit(keep);
    const near = new Set(S.selected ? [S.selected] : []);
    vEdges.forEach(e => { if (e.source === S.selected) near.add(e.target); if (e.target === S.selected) near.add(e.source); });
    const gE = mk("g"), gL = mk("g"), gN = mk("g"); svg.appendChild(gE); svg.appendChild(gL); svg.appendChild(gN);
    vEdges.forEach(e => {
      if (!keep.has(e.source) || !keep.has(e.target)) return;
      const a = P.get(e.source), b = P.get(e.target), rb = radius(byId.get(e.target)) + 3;
      const dx = b.x - a.x, dy = b.y - a.y, d = Math.hypot(dx, dy) || 1;
      const touches = S.selected && (e.source === S.selected || e.target === S.selected);
      const line = mk("line", { x1: a.x, y1: a.y, x2: b.x - dx / d * rb, y2: b.y - dy / d * rb, "marker-end": "url(#arrow)",
        class: "edge" + (e.proposed ? " proposed" : "") + (S.selected ? (touches ? " hot" : " dim") : "") });
      const t = mk("title"); t.textContent = `${byId.get(e.source).label} ${words(e.predicate)} ${byId.get(e.target).label}` + (e.proposed ? " (proposed)" : ""); line.appendChild(t);
      gE.appendChild(line);
      if (touches) {
        const lab = mk("text", { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 - 3, class: "elabel" }); lab.textContent = words(e.predicate); gL.appendChild(lab);
      }
    });
    NET.nodes.forEach(n => {
      if (!keep.has(n.id)) return;
      const p = P.get(n.id), g = mk("g", { class: "node " + n.kind + (S.selected ? (near.has(n.id) ? (n.id === S.selected ? " sel" : " hot") : " dim") : ""), transform: `translate(${p.x},${p.y})`, tabindex: "0", role: "button" });
      g.setAttribute("aria-label", `${n.label}, ${n.ko_type}${n.kind !== "ko" ? ", not written yet" : ""}`);
      g.appendChild(mk("circle", { r: radius(n), fill: n.kind === "ko" ? color(n.ko_type) : "var(--card)", stroke: color(n.ko_type) }));
      const label = mk("text", { y: radius(n) + 13, class: "nlabel" }); label.textContent = n.label.length > 26 ? n.label.slice(0, 24) + "…" : n.label; g.appendChild(label);
      const t = mk("title"); t.textContent = n.label; g.appendChild(t);
      g.addEventListener("keydown", ev => { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); select(n.id); } });
      dragAndClick(g, n.id);
      gN.appendChild(g);
    });
  }
  /* Zoom the view to the visible topics (keeps the 900 x 560 shape; never zooms in so far that labels get huge). */
  let dragging = false;
  function fit(keep) {
    if (dragging) return;  // don't move the view under the pointer
    const pts = [...keep].map(id => P.get(id));
    if (!pts.length) return;
    let x0 = Math.min(...pts.map(p => p.x)) - 60, x1 = Math.max(...pts.map(p => p.x)) + 60;
    let y0 = Math.min(...pts.map(p => p.y)) - 40, y1 = Math.max(...pts.map(p => p.y)) + 50;
    let w = Math.max(x1 - x0, 420), h = Math.max(y1 - y0, 260);
    if (w / h > W / H) h = w * H / W; else w = h * W / H;
    const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
    svg.setAttribute("viewBox", `${cx - w / 2} ${cy - h / 2} ${w} ${h}`);
  }
  function point(ev) { const pt = svg.createSVGPoint(); pt.x = ev.clientX; pt.y = ev.clientY; return pt.matrixTransform(svg.getScreenCTM().inverse()); }
  function dragAndClick(g, id) {
    let start = null, moved = false;
    g.addEventListener("pointerdown", ev => { start = point(ev); moved = false; g.setPointerCapture(ev.pointerId); });
    g.addEventListener("pointermove", ev => {
      if (!start) return; const q = point(ev);
      if (!moved && Math.hypot(q.x - start.x, q.y - start.y) < 4) return;
      moved = true; dragging = true; const p = P.get(id); p.x = q.x; p.y = q.y; p.fixed = true; draw();
    });
    g.addEventListener("pointerup", () => { dragging = false; if (start && !moved) select(id); start = null; });
  }

  // ---------------------------------------------------------------- side panel
  const panel = $("#net-panel");
  function select(id) { S.selected = id; draw(); showPanel(id); }
  function button(text, onClick, cls = "secondary") { const b = el("button", cls, text); b.type = "button"; b.addEventListener("click", onClick); return b; }
  function link(text, href, cls) { const a = el("a", cls, text); a.href = href; return a; }
  function showPanel(id) {
    const n = byId.get(id); panel.textContent = "";
    panel.appendChild(el("div", "eyebrow", n.kind === "ko" ? "Knowledge Object" : n.kind === "planned" ? "Planned topic" : "Proposed topic"));
    panel.appendChild(el("h3", null, n.label));
    const chips = el("p"); const chip = el("span", "chip", n.ko_type || "type unknown"); chip.style.borderColor = color(n.ko_type); chips.appendChild(chip);
    chips.appendChild(el("span", "chip", n.kind === "ko" ? "Review: " + n.status : n.kind === "planned" ? "No KO yet (" + n.status + ")" : "Not written yet"));
    panel.appendChild(chips);
    if (n.summary) panel.appendChild(el("p", "small", n.summary));
    if (n.kind === "proposed") panel.appendChild(el("p", "muted small", "Proposed by " + n.proposed_by.join(", ") + ". Add it on the KO Topics page to start a KO."));
    const row = el("div", "btnrow");
    if (n.kind === "ko") {
      row.appendChild(link("Open KO", `${D.urls.library}?ko=${encodeURIComponent(n.id)}`, "btn"));
      row.appendChild(link("Ask OrthoBot", `${D.urls.orthobot}?q=${encodeURIComponent("What is " + n.label + "?")}`, "btn secondary"));
    }
    row.appendChild(button(S.depth ? "Show everything" : "Focus here", () => { S.depth = S.depth ? 0 : 1; $("#net-depth").value = String(S.depth); select(id); }));
    panel.appendChild(row);

    const links = edges.filter(e => (e.source === id || e.target === id) && S.preds.has(e.predicate) && (S.proposed || !e.proposed));
    panel.appendChild(el("h4", null, `Connections (${links.length})`));
    if (!links.length) panel.appendChild(el("p", "muted small", "No connections yet."));
    const groups = new Map();
    links.forEach(e => { const key = (e.source === id ? "→ " : "← ") + words(e.predicate); if (!groups.has(key)) groups.set(key, []); groups.get(key).push(e); });
    groups.forEach((list, key) => {
      const box = el("div", "conn"); box.appendChild(el("div", "connhead", key));
      list.forEach(e => {
        const other = byId.get(e.source === id ? e.target : e.source), item = el("div", "connitem");
        const b = button(other.label, () => select(other.id), "link"); item.appendChild(b);
        if (e.proposed) item.appendChild(el("span", "chip", "proposed"));
        if (e.evidence && e.evidence.length) {
          const ev = el("div", "muted small"); ev.appendChild(document.createTextNode(`Sources (in ${e.stated_in}): `));
          e.evidence.forEach((s, i) => {
            const href = safeUrl(s.url), label = `[${s.id}] ${s.publisher || s.title || ""}`;
            if (href) { const a = el("a", null, label); a.href = href; a.target = "_blank"; a.rel = "noopener"; ev.appendChild(a); } else ev.appendChild(document.createTextNode(label));
            if (i < e.evidence.length - 1) ev.appendChild(document.createTextNode(" · "));
          });
          item.appendChild(ev);
        } else if (e.reason) item.appendChild(el("div", "muted small", e.reason));
        else if (!e.proposed) item.appendChild(el("div", "muted small warn", "No source listed for this connection."));
        box.appendChild(item);
      });
      panel.appendChild(box);
    });
  }

  // ---------------------------------------------------------------- controls
  $("#net-proposed").addEventListener("change", e => { S.proposed = e.target.checked; draw(); if (S.selected) showPanel(S.selected); });
  $("#net-depth").addEventListener("change", e => { S.depth = Number(e.target.value); draw(); });
  $("#net-reset").addEventListener("click", () => {
    S.selected = null; S.depth = 0; $("#net-depth").value = "0"; P.forEach(p => { p.fixed = false; }); simulate(120); draw();
    panel.textContent = ""; panel.appendChild(el("div", "eyebrow", "Selected topic")); panel.appendChild(el("p", "muted", "Pick a topic in the network to see what it connects to."));
  });
  $("#net-search").addEventListener("change", e => {
    const q = e.target.value.trim().toLowerCase(); if (!q) return;
    const hit = NET.nodes.find(n => n.label.toLowerCase() === q) || NET.nodes.find(n => n.label.toLowerCase().includes(q));
    if (hit) { if (hit.kind === "proposed" && !S.proposed) { S.proposed = true; $("#net-proposed").checked = true; } select(hit.id); }
  });
  draw();
  if (D.focus && byId.has(D.focus)) { S.depth = 1; $("#net-depth").value = "1"; select(D.focus); }

  // ---------------------------------------------------------------- research discovery (concept)
  const form = $("#rd-form");
  if (form) form.addEventListener("submit", ev => {
    ev.preventDefault();
    const topic = byId.get($("#rd-topic").value), focus = $("#rd-focus").value.trim();
    const kinds = new Set([...document.querySelectorAll('input[name="rd-kind"]:checked')].map(c => c.value));
    const near = new Map(); let frontier = [topic.id];
    for (let d = 1; d <= 2; d++) {
      const next = [];
      edges.forEach(e => [[e.source, e.target], [e.target, e.source]].forEach(([a, b]) => {
        if (frontier.includes(a) && b !== topic.id && !near.has(b)) { near.set(b, d); next.push(b); }
      }));
      frontier = next;
    }
    const nodes = [...near.keys()].map(id => byId.get(id));
    const out = $("#rd-results"); out.textContent = "";
    out.appendChild(el("h3", null, `Related knowledge: ${topic.label}${focus ? " · " + focus : ""}`));
    const grid = el("div", "grid cols-3"); out.appendChild(grid);
    function section(title, items, note) {
      const c = el("div", "card"); c.appendChild(el("h4", null, title));
      if (!items.length) c.appendChild(el("p", "muted small", note || "Nothing in the network yet."));
      items.forEach(n => {
        const p = el("p", "small");
        if (n.kind === "ko") p.appendChild(link(n.label, `${D.urls.library}?ko=${encodeURIComponent(n.id)}`));
        else { p.appendChild(document.createTextNode(n.label + " ")); p.appendChild(el("span", "chip", "not written yet")); }
        c.appendChild(p);
      });
      grid.appendChild(c);
    }
    const ofType = types => nodes.filter(n => types.includes(n.ko_type));
    if (kinds.has("Related KOs")) section("Related KOs", nodes.filter(n => n.kind === "ko"));
    if (kinds.has("Devices")) section("Devices and technology", ofType(["Device"]));
    if (kinds.has("Outcomes")) section("Outcomes and recovery", ofType(["OutcomeMeasure", "RehabProtocol"]));
    const q = encodeURIComponent([topic.label, focus].filter(Boolean).join(" "));
    [["Clinical trials", "ClinicalTrials.gov", `https://clinicaltrials.gov/search?term=${q}`],
     ["Publications", "PubMed", `https://pubmed.ncbi.nlm.nih.gov/?term=${q}`],
     ["Guidelines", "AAOS guidelines", "https://www.aaos.org/quality/quality-programs/"]].forEach(([kind, where, url]) => {
      if (!kinds.has(kind)) return;
      const c = el("div", "card ghostcard"); c.appendChild(el("h4", null, kind));
      c.appendChild(el("p", "muted small", `Not in the network yet. Planned: ${where} records turned into research objects, connected to “${topic.label}”, with each connection reviewed.`));
      const a = el("a", "small", `Search ${where} now ↗`); a.href = url; a.target = "_blank"; a.rel = "noopener"; c.appendChild(a);
      grid.appendChild(c);
    });
    const ask = el("p"); ask.appendChild(link(`Ask OrthoBot about ${topic.label}`, `${D.urls.orthobot}?q=${encodeURIComponent(`What is ${topic.label}?`)}`, "btn secondary"));
    out.appendChild(ask);
  });
})();
