/* Data Skeleton: draws a data model as a top-down diagram (like the team's flow chart) from the model JSON.
   Layers come from the distance to the model's root entity; arrows carry the relationship labels. */
"use strict";
(() => {
  const { $, el } = KO;
  const M = JSON.parse($("#dm-data").textContent);
  const svg = $("#dm-svg"), panel = $("#dm-panel"), NS = "http://www.w3.org/2000/svg";
  const BW = 136, BH = 40, GX = 26, GY = 86, PAD = 24;
  const names = Object.keys(M.entities);

  // layer = steps from the root, following links in either direction
  const nbr = new Map(names.map(n => [n, new Set()]));
  M.edges.forEach(e => { nbr.get(e.from).add(e.to); nbr.get(e.to).add(e.from); });
  const layer = new Map([[M.root, 0]]), queue = [M.root];
  while (queue.length) { const n = queue.shift(); nbr.get(n).forEach(m => { if (!layer.has(m)) { layer.set(m, layer.get(n) + 1); queue.push(m); } }); }
  names.forEach(n => { if (!layer.has(n)) layer.set(n, Math.max(0, ...layer.values()) + 1); });
  const rows = [];
  layer.forEach((l, n) => { (rows[l] = rows[l] || []).push(n); });

  // order each row by the average x of its neighbours in the row above (fewer crossings)
  const pos = new Map();
  rows.forEach((row, l) => {
    if (l > 0) {
      const xOf = n => { const up = [...nbr.get(n)].filter(m => layer.get(m) === l - 1 && pos.has(m)); return up.length ? up.reduce((s, m) => s + pos.get(m).x, 0) / up.length : 1e9; };
      row.sort((a, b) => xOf(a) - xOf(b));
    }
    row.forEach((n, i) => pos.set(n, { x: i, y: l }));
  });
  const widest = Math.max(...rows.map(r => r.length));
  const W = PAD * 2 + widest * (BW + GX), H = PAD * 2 + rows.length * (BH + GY) - GY;
  rows.forEach(row => { const off = (widest - row.length) / 2; row.forEach(n => { const p = pos.get(n); p.px = PAD + (p.x + off) * (BW + GX); p.py = PAD + p.y * (BH + GY); }); });
  svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
  svg.style.width = `${W}px`;  // real size: the card scrolls sideways rather than shrinking the text
  svg.style.maxWidth = "none";

  const mk = (tag, a) => { const e = document.createElementNS(NS, tag); Object.entries(a || {}).forEach(([k, v]) => e.setAttribute(k, v)); return e; };
  const defs = mk("defs"), mark = mk("marker", { id: "dm-arrow", viewBox: "0 0 10 10", refX: "10", refY: "5", markerWidth: "7", markerHeight: "7", orient: "auto-start-reverse" });
  mark.appendChild(mk("path", { d: "M0,0 L10,5 L0,10 z", class: "arrowhead" })); defs.appendChild(mark); svg.appendChild(defs);
  const gE = mk("g"), gN = mk("g"); svg.appendChild(gE); svg.appendChild(gN);
  let selected = null;

  function draw() {
    gE.textContent = ""; gN.textContent = "";
    M.edges.forEach(e => {
      const a = pos.get(e.from), b = pos.get(e.to);
      const down = b.py >= a.py;
      const x1 = a.px + BW / 2, y1 = down ? a.py + BH : a.py, x2 = b.px + BW / 2, y2 = down ? b.py : b.py + BH;
      const midY = (y1 + y2) / 2, hot = selected && (e.from === selected || e.to === selected);
      const path = mk("path", { d: a.py === b.py ? `M${a.px + BW},${a.py + BH / 2} L${b.px},${b.py + BH / 2}` : `M${x1},${y1} V${midY} H${x2} V${y2}`,
        class: "dm-edge" + (hot ? " hot" : selected ? " dim" : ""), "marker-end": "url(#dm-arrow)" });
      const t = mk("title"); t.textContent = `${e.from} ${e.predicate} ${e.to}`; path.appendChild(t); gE.appendChild(path);
      const lab = mk("text", { x: (x1 + x2) / 2, y: a.py === b.py ? a.py + BH / 2 - 4 : midY - 4, class: "dm-label" + (hot ? " hot" : "") });
      lab.textContent = e.predicate; gE.appendChild(lab);
    });
    names.forEach(n => {
      const p = pos.get(n), g = mk("g", { class: "dm-node" + (n === selected ? " sel" : "") + (n === M.root ? " root" : ""), tabindex: "0", role: "button", transform: `translate(${p.px},${p.py})` });
      g.setAttribute("aria-label", `${n}: ${Object.keys(M.entities[n].fields).length} fields`);
      g.appendChild(mk("rect", { width: BW, height: BH, rx: 7 }));
      const words = n.replace(/([a-z])([A-Z])/g, "$1 $2"), lines = words.length > 18 ? [words.slice(0, words.lastIndexOf(" ", 18) > 0 ? words.lastIndexOf(" ", 18) : 18), words.slice(words.lastIndexOf(" ", 18) > 0 ? words.lastIndexOf(" ", 18) + 1 : 18)] : [words];
      lines.forEach((ln, i) => { const t = mk("text", { x: BW / 2, y: BH / 2 + (i - (lines.length - 1) / 2) * 13 + 4 }); t.textContent = ln; g.appendChild(t); });
      g.addEventListener("click", () => select(n));
      g.addEventListener("keydown", ev => { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); select(n); } });
      gN.appendChild(g);
    });
  }

  function select(n) {
    selected = n; draw();
    const e = M.entities[n]; panel.textContent = "";
    panel.appendChild(el("div", "eyebrow", n === M.root ? "Root entity" : "Entity"));
    panel.appendChild(el("h3", null, n));
    if (e.description) panel.appendChild(el("p", "small", e.description));
    const tbl = el("table", "small"), head = el("tr");
    ["Field", "Type", "Notes"].forEach(h => head.appendChild(el("th", null, h))); tbl.appendChild(head);
    Object.entries(e.fields).forEach(([fname, f]) => {
      const tr = el("tr"); tr.appendChild(el("td", null, fname + (f.required || f.type === "id" ? " *" : "")));
      tr.appendChild(el("td", null, f.type));
      const note = f.type === "ref" ? `→ ${f.ref} (${f.predicate})` : f.type === "ko" ? `KO: ${(f.ko_types || []).join(" / ")}`
        : f.values ? f.values.join(", ") : f.description || "";
      tr.appendChild(el("td", null, note)); tbl.appendChild(tr);
    });
    panel.appendChild(tbl);
    const links = M.edges.filter(x => x.from === n || x.to === n);
    if (links.length) {
      panel.appendChild(el("h4", null, "Links"));
      links.forEach(x => { const p = el("p", "small"); const b = el("button", "link", x.from === n ? x.to : x.from); b.type = "button";
        b.addEventListener("click", () => select(x.from === n ? x.to : x.from));
        p.appendChild(document.createTextNode(x.from === n ? `${n} ${x.predicate} → ` : `← ${x.predicate} from `)); p.appendChild(b); panel.appendChild(p); });
    }
    panel.appendChild(el("p", "muted small", "* required"));
  }

  draw();
  select(M.root);
  // show the real-data questions only when "real records" is chosen
  const real = document.getElementById("real-fields");
  if (real) document.querySelectorAll('input[name=kind]').forEach(r => r.addEventListener("change", () => {
    real.hidden = document.querySelector('input[name=kind]:checked').value !== "real"; }));
})();
