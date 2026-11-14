/* Knowledge Object Generator: the 5-step wizard. Typed values are kept in sessionStorage while you move between steps. */
"use strict";
(() => {
  const { $, $$, el } = KO;
  const D = JSON.parse($("#gen-data").textContent);
  const KEY = "ko-gen-state", DRAFT_KEY = "ko-gen-draft", N = 5;
  const newSource = () => ({
    uid: Math.random().toString(36).slice(2, 10), catalog: "", url: "", title: "", publisher: "", text: "",
    source_type: "government_health_page", audience: "patient", permitted_use: "<verify>",
    publication_date: "<verify>", retrieved_date: D.today, evidence_strength: "", notes: "",
  });
  const defaults = () => ({
    step: 1, conceptMode: "pick", ko_id: D.topics.length ? D.topics[0].ko_id : "", audience: ["patient", "caregiver"],
    author: "", reading_level: "grade 6-8", difficulty: "beginner", license: "CC-BY-4.0",
    mode: D.ai_ready ? "ai" : "template", sources: [newSource(), newSource()], pack: "", notes: [],
  });
  const S = Object.assign(defaults(), KO.store.get(KEY, {}));
  if (!D.topics.some(t => t.ko_id === S.ko_id) && D.topics.length) S.ko_id = D.topics[0].ko_id;
  const keep = () => KO.store.set(KEY, S);

  const editor = KOEditor($("#gen-editor"), {
    text: KO.store.get(DRAFT_KEY, ""), storageKey: DRAFT_KEY, urls: { check: D.urls.check, save: D.urls.save },
    canEdit: D.can_edit, getPack: () => S.pack,
  });
  const hasDraft = () => editor.text.trim().length > 0;

  // ---------------------------------------------------------------- progress
  function missing() {
    const m = {};
    m[1] = S.conceptMode === "add" ? "Add the topic, or go back to the list."
      : D.topics.some(t => t.ko_id === S.ko_id) ? null : "Choose a topic.";
    m[2] = S.audience.length ? null : "Choose at least 1 reader.";
    const complete = S.sources.filter(s => s.url.trim() && s.title.trim() && s.publisher.trim());
    m[3] = complete.length >= 2 ? null : "Fill in the page link, title, and publisher for 2 sources.";
    m[4] = hasDraft() ? null : "Click 'Generate draft'.";
    m[5] = null;
    return m;
  }

  function render() {
    keep();
    const m = missing(), step = S.step, info = D.steps[step];
    let blocked = null;
    for (let n = 1; n < step; n++) if (m[n]) { blocked = n; break; }
    // step pills
    const pills = $("#gen-steps"); pills.textContent = "";
    for (let n = 1; n <= N; n++) {
      const b = el("button", "steppill" + (n === step ? " on" : ""), `${!m[n] && n < N ? "✓" : n} · ${D.steps[n].short}`);
      b.type = "button"; b.setAttribute("role", "tab"); b.setAttribute("aria-selected", String(n === step));
      b.addEventListener("click", () => go(n)); pills.appendChild(b);
    }
    $("#gen-h").textContent = `${step} · ${info.title}`;
    $("#gen-sub").textContent = info.sub;
    const bl = $("#gen-blocked");
    bl.hidden = !blocked;
    bl.textContent = "";
    if (blocked) {
      bl.appendChild(document.createTextNode(`First finish step ${blocked} (${D.steps[blocked].title}): ${m[blocked]} `));
      const b = el("button", "link", `Go to step ${blocked}`); b.type = "button"; b.addEventListener("click", () => go(blocked)); bl.appendChild(b);
    }
    $$("[data-step]").forEach(s => { s.hidden = blocked || Number(s.dataset.step) !== step; });
    // side panel
    $("#p-badge").textContent = `Step ${step} · ${info.title}`;
    $("#p-title").textContent = info.title;
    $("#p-intro").innerHTML = info.intro;  // fixed text from the server (texts.STEPS)
    const fields = $("#p-fields"); fields.textContent = "";
    info.help.forEach(([f, msg]) => { const d = el("div", "g-f"); d.appendChild(el("b", null, f)); d.appendChild(el("span", null, msg)); fields.appendChild(d); });
    $("#p-example").textContent = info.example ? `Example: ${info.example}` : "";
    $("#p-track").style.width = `${(step / N) * 100}%`;
    $("#p-hint").textContent = step < N && m[step] && !blocked ? `To continue: ${m[step]}` : "";
    $("#p-back").disabled = step === 1;
    $("#p-next").hidden = step === N; $("#p-new").hidden = step !== N;
    $("#p-next").disabled = Boolean(m[step] || blocked);
    $("#p-count").textContent = `${step} / ${N}`;
    if (step === 1) renderTopic();
    if (step === 2) renderReaders();
    if (step === 3 && !$("#gen-sources").children.length) renderSources();
    if (step === 4) renderDraft();
    if (step === 5) renderSave();
  }
  function go(n) { S.step = Math.min(Math.max(n, 1), N); render(); window.scrollTo({ top: $("#gen-steps").offsetTop - 80 }); }
  $("#p-back").addEventListener("click", () => go(S.step - 1));
  $("#p-next").addEventListener("click", () => go(S.step + 1));
  $("#p-new").addEventListener("click", () => {
    if (!confirm("Start a new KO? The current draft and sources on this page are cleared (saved KOs stay in the library).")) return;
    KO.store.del(KEY); KO.store.del(DRAFT_KEY); location.reload();
  });

  // ---------------------------------------------------------------- step 1: topic
  function renderTopic() {
    $$('input[name="concept_mode"]').forEach(r => { r.checked = r.value === S.conceptMode; });
    $("#gen-pick").hidden = S.conceptMode !== "pick"; $("#gen-add").hidden = S.conceptMode !== "add";
    const sel = $("#gen-topic"); sel.textContent = "";
    D.topics.forEach(t => { const o = el("option", null, `${t.term}  ·  ${t.ko_id}`); o.value = t.ko_id; sel.appendChild(o); });
    sel.value = S.ko_id;
    const t = D.topics.find(x => x.ko_id === S.ko_id);
    $("#gen-topic-info").textContent = t ? `Type: ${t.ko_type} · ${t.specialty}` + (t.alternate_terms.length ? ` · Other names: ${t.alternate_terms.join(", ")}` : "")
      : "The topic list is empty. Choose 'Add a new one'.";
  }
  $$('input[name="concept_mode"]').forEach(r => r.addEventListener("change", () => { S.conceptMode = r.value; render(); }));
  $("#gen-topic").addEventListener("change", e => { S.ko_id = e.target.value; render(); });
  $("#nc-add").addEventListener("click", async () => {
    const msg = $("#nc-msg"); msg.className = ""; msg.textContent = "Adding…";
    try {
      const j = await KO.post(D.urls.topic, { term: $("#nc-term").value, alternate_terms: $("#nc-alts").value, ko_type: $("#nc-type").value,
        specialty: $("#nc-spec").value, mesh: $("#nc-mesh").value, icd10cm: $("#nc-icd").value });
      D.topics.push(j.topic); D.topics.sort((a, b) => a.term.toLowerCase().localeCompare(b.term.toLowerCase()));
      S.ko_id = j.topic.ko_id; S.conceptMode = "pick";
      ["#nc-term", "#nc-alts", "#nc-mesh", "#nc-icd"].forEach(s => { $(s).value = ""; });
      msg.className = "status ok"; msg.textContent = j.message; render();
    } catch (e) { msg.className = "status bad"; msg.textContent = e.message; }
  });

  // ---------------------------------------------------------------- step 2: readers
  function renderReaders() {
    const box = $("#gen-audience"); box.textContent = "";
    D.enums.audience.forEach(a => {
      const l = el("label"), c = el("input"); c.type = "checkbox"; c.checked = S.audience.includes(a);
      c.addEventListener("change", () => { S.audience = c.checked ? [...S.audience, a] : S.audience.filter(x => x !== a); render(); });
      l.appendChild(c); l.appendChild(document.createTextNode(" " + a)); box.appendChild(l);
    });
    $("#gen-audience-order").textContent = S.audience.join(" → ") || "none";
    $("#gen-author").value = S.author; $("#gen-reading").value = S.reading_level;
    $("#gen-difficulty").value = S.difficulty; $("#gen-license").value = S.license;
  }
  [["#gen-author", "author"], ["#gen-reading", "reading_level"], ["#gen-difficulty", "difficulty"], ["#gen-license", "license"]]
    .forEach(([sel, key]) => $(sel).addEventListener("input", e => { S[key] = e.target.value; keep(); }));

  // ---------------------------------------------------------------- step 3: sources
  const help = k => D.help[k] || "";
  function field(src, key, label, kind = "input", options = null) {
    const l = el("label", "field"); l.appendChild(document.createTextNode(label + " "));
    const h = el("span", "help", "?"); h.title = help({ text: "text", url: "url", title: "title", publisher: "publisher", source_type: "source_type",
      audience: "source_audience", permitted_use: "permitted_use", publication_date: "publication_date", retrieved_date: "retrieved_date",
      evidence_strength: "evidence_strength", notes: "notes", catalog: "known_source" }[key]); l.appendChild(h);
    let input;
    if (options) { input = el("select"); options.forEach(([v, t]) => { const o = el("option", null, t); o.value = v; input.appendChild(o); }); }
    else { input = el(kind); if (kind === "textarea") input.rows = 6; }
    if (key === "retrieved_date") input.type = "date";
    if (key === "url") input.placeholder = "https://...";
    if (key === "text") input.placeholder = "Paste the text from the page, or click 'Fetch'.";
    input.value = src[key] || ""; input.dataset.key = key;
    input.addEventListener(options ? "change" : "input", () => { src[key] = input.value; keep(); updateProgress(); });
    l.appendChild(input); return l;
  }
  function updateProgress() {  // refresh the panel without re-drawing the source cards (keeps the cursor in place)
    const m = missing(), step = S.step;
    $("#p-hint").textContent = step < N && m[step] ? `To continue: ${m[step]}` : "";
    $("#p-next").disabled = Boolean(m[step]);
  }
  function renderSources() {
    const box = $("#gen-sources"); box.textContent = "";
    S.sources.forEach((src, i) => {
      const card = el("div", "card srccard"); card.appendChild(el("h3", null, `Source S${i + 1}`));
      if (D.catalog.length) {
        const cat = field(src, "catalog", "Known source (optional)", "input", [["", "Pick from our list"], ...D.catalog.map(c => [c.name, c.name])]);
        cat.querySelector("select").addEventListener("change", e => {
          const c = D.catalog.find(x => x.name === e.target.value); if (!c) return;
          src.publisher = c.publisher; if (!src.url.trim()) src.url = c.url;
          if (c.source_type) src.source_type = c.source_type; if (c.permitted_use) src.permitted_use = c.permitted_use;
          src.notes = c.notes; keep(); renderSources(); updateProgress();
        });
        card.appendChild(cat);
      }
      const urlRow = el("div", "row-url"); urlRow.appendChild(field(src, "url", "Page link *"));
      const fetchBtn = el("button", "secondary", "Fetch"); fetchBtn.type = "button"; fetchBtn.title = help("fetch"); fetchBtn.disabled = !D.can_edit;
      urlRow.appendChild(fetchBtn); card.appendChild(urlRow);
      const msg = el("div"); msg.setAttribute("role", "status"); card.appendChild(msg);
      fetchBtn.addEventListener("click", async () => {
        if (!src.url.trim()) { msg.className = "status bad"; msg.textContent = "Paste the page link first."; return; }
        fetchBtn.disabled = true; msg.className = "muted"; msg.textContent = "Fetching the page…";
        try {
          const j = await KO.post(D.urls.fetch, { url: src.url });
          src.text = j.text; if (!src.title.trim() && j.title) src.title = j.title; src.retrieved_date = j.retrieved; keep();
          renderSources(); updateProgress();
          const again = $$(".srccard")[i].querySelector('[role="status"]'); again.className = "status ok"; again.textContent = j.message;
        } catch (e) { msg.className = "status bad"; msg.textContent = e.message; fetchBtn.disabled = false; }
      });
      const r2 = el("div", "row2"); r2.appendChild(field(src, "title", "Page title *")); r2.appendChild(field(src, "publisher", "Publisher *")); card.appendChild(r2);
      card.appendChild(field(src, "text", "Source text *", "textarea"));
      const more = el("details"); more.appendChild(el("summary", null, "More details (type, reuse rules, dates)"));
      const r3 = el("div", "row3");
      r3.appendChild(field(src, "source_type", "Source type", "input", D.enums.source_type.map(v => [v, v])));
      r3.appendChild(field(src, "audience", "Written for", "input", D.enums.audience.map(v => [v, v])));
      r3.appendChild(field(src, "permitted_use", "Reuse rules", "input", D.enums.permitted_use.map(v => [v, v])));
      const r4 = el("div", "row3");
      r4.appendChild(field(src, "publication_date", "Page date")); r4.appendChild(field(src, "retrieved_date", "Date you copied it"));
      r4.appendChild(field(src, "evidence_strength", "Evidence strength"));
      more.appendChild(r3); more.appendChild(r4); more.appendChild(field(src, "notes", "Notes")); card.appendChild(more);
      if (S.sources.length > 1) {
        const rm = el("button", "link", "Remove this source"); rm.type = "button";
        rm.addEventListener("click", () => { S.sources.splice(i, 1); renderSources(); render(); }); card.appendChild(rm);
      }
      box.appendChild(card);
    });
  }
  $("#src-collected").addEventListener("click", async () => {
    const msg = $("#src-collected-msg"); msg.className = "muted small"; msg.textContent = "Loading…";
    try {
      const r = await fetch(D.urls.collected.replace("__ID__", encodeURIComponent(S.ko_id)));
      const j = await r.json();
      if (!r.ok) throw new Error(j.error || "Could not load the collected sources.");
      if (S.sources.some(s => s.url.trim() || s.text.trim()) && !confirm("Replace the sources you already entered?")) { msg.textContent = ""; return; }
      S.sources = j.sources.map(s => ({ ...newSource(), ...Object.fromEntries(Object.entries(s).filter(([k]) => k !== "id").map(([k, v]) => [k, v == null ? "" : String(v)])) }));
      renderSources(); render();
      msg.className = "status ok"; msg.textContent = `Loaded ${j.sources.length} of ${j.count} collected sources. Read each one and delete what isn't about this topic.`;
    } catch (e) { msg.className = "status bad"; msg.textContent = e.message; }
  });
  $("#src-add").addEventListener("click", () => { S.sources.push(newSource()); renderSources(); render(); });
  $("#src-reset").addEventListener("click", () => {
    if (!confirm("Clear all sources on this step and start with 2 empty ones?")) return;
    S.sources = [newSource(), newSource()]; renderSources(); render();
  });

  // ---------------------------------------------------------------- step 4: draft
  const request = () => ({ ko_id: S.ko_id, audience: S.audience, author: S.author, reading_level: S.reading_level,
    difficulty: S.difficulty, license: S.license, sources: S.sources.map(({ uid, catalog, ...rest }) => rest), mode: S.mode });
  function packProblems() {
    const p = [];
    if (S.sources.filter(s => s.text.trim()).length < 2) p.push("Add at least 2 sources with text (paste or fetch the source text).");
    S.sources.forEach((s, i) => { if (s.permitted_use === "restricted") p.push(`Source S${i + 1} is 'restricted' and cannot be used.`); });
    return p;
  }
  function renderDraft() {
    $$('input[name="draft_mode"]').forEach(r => { r.checked = r.value === S.mode; });
    const warn = $("#gen-draft-warn"); warn.textContent = "";
    const notes = [];
    if (!D.can_edit) notes.push("Read only: sign in as an editor to make a draft.");
    if (S.mode === "ai" && !D.ai_ready) notes.push("AI is off (no API key). Use the empty template, or add a Claude or OpenAI key to .env.");
    const problems = S.mode === "ai" ? packProblems() : [];
    [...notes, ...problems].forEach(t => warn.appendChild(el("div", "notice", t)));
    $("#gen-generate").disabled = !D.can_edit || problems.length > 0 || (S.mode === "ai" && !D.ai_ready);
    $("#gen-has-draft").hidden = !hasDraft();
    $("#gen-prompts").hidden = S.mode !== "ai" || !D.can_edit;
  }
  $$('input[name="draft_mode"]').forEach(r => r.addEventListener("change", () => { S.mode = r.value; render(); }));
  $("#gen-prompts").addEventListener("toggle", async e => {
    if (!e.target.open) return;
    try { const j = await KO.post(D.urls.prompts, request()); $("#gen-prompts-system").textContent = j.system; $("#gen-prompts-user").textContent = j.user; }
    catch (err) { $("#gen-prompts-system").textContent = err.message; }
  });
  $("#gen-generate").addEventListener("click", async () => {
    const btn = $("#gen-generate"), box = $("#gen-stream"), out = $("#gen-stream-text"), warn = $("#gen-draft-warn");
    btn.disabled = true; warn.textContent = "";
    const done = (markdown, pack, notes) => { editor.setText(markdown); S.pack = pack; S.notes = notes || []; box.hidden = true; go(5); };
    try {
      if (S.mode !== "ai") {
        const j = await KO.post(D.urls.draft, request());
        done(j.markdown, j.pack, j.notes);
      } else {
        box.hidden = false; out.textContent = ""; $("#gen-stream-label").textContent = `${D.ai_label} is writing the draft…`;
        let failed = null;
        await KO.stream(D.urls.draft, request(), item => {
          if (item.t) { out.textContent += item.t; out.scrollTop = out.scrollHeight; }
          if (item.error) failed = item.error;
          if (item.done) done(item.markdown, item.pack, item.notes);
        });
        if (failed) throw new Error(failed);
      }
    } catch (e) { warn.appendChild(el("div", "flash error", e.message)); box.hidden = true; }
    finally { btn.disabled = false; renderDraft(); }
  });

  // ---------------------------------------------------------------- step 5: check and save
  function renderSave() {
    const notes = $("#gen-notes"); notes.textContent = "";
    (S.notes || []).forEach(n => notes.appendChild(el("div", "notice", n)));
    $("#gen-no-draft").hidden = hasDraft();
    $("#gen-editor").hidden = !hasDraft();
  }

  render();
})();
