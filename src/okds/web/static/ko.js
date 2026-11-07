/* KO Portal shared script: tabs, API helpers, and the KO editor (Preview / Edit / Checks / Save). */
"use strict";
const KO = (() => {
  const csrf = (document.querySelector('meta[name="csrf-token"]') || {}).content || "";
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
  const safeUrl = u => /^https?:\/\//i.test(u || "") ? u : null;
  const store = {
    get(k, d) { try { const v = sessionStorage.getItem(k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { sessionStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* private mode */ } },
    del(k) { try { sessionStorage.removeItem(k); } catch (e) { /* ignore */ } },
  };

  async function post(url, body) {
    const r = await fetch(url, { method: "POST", headers: { "Content-Type": "application/json", "X-CSRF-Token": csrf }, body: JSON.stringify(body) });
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.error || `Request failed (${r.status}).`);
    return j;
  }

  /* POST, then read newline-delimited JSON objects as they arrive. */
  async function stream(url, body, onItem) {
    const r = await fetch(url, { method: "POST", headers: { "Content-Type": "application/json", "X-CSRF-Token": csrf }, body: JSON.stringify(body) });
    if (!r.ok) { const j = await r.json().catch(() => ({})); throw new Error(j.error || `Request failed (${r.status}).`); }
    const reader = r.body.getReader(), dec = new TextDecoder();
    let buf = "";
    for (;;) {
      const { value, done } = await reader.read();
      if (value) buf += dec.decode(value, { stream: true });
      let i;
      while ((i = buf.indexOf("\n")) >= 0) { const line = buf.slice(0, i).trim(); buf = buf.slice(i + 1); if (line) onItem(JSON.parse(line)); }
      if (done) break;
    }
    if (buf.trim()) onItem(JSON.parse(buf));
  }

  function tabs(root) {
    const buttons = $$(":scope > .tablist [data-tab]", root), panels = $$(":scope > [data-panel]", root);
    const show = name => {
      buttons.forEach(b => b.setAttribute("aria-selected", String(b.dataset.tab === name)));
      panels.forEach(p => { p.hidden = p.dataset.panel !== name; });
    };
    buttons.forEach(b => b.addEventListener("click", () => show(b.dataset.tab)));
    const first = buttons.find(b => b.getAttribute("aria-selected") === "true") || buttons[0];
    if (first) show(first.dataset.tab);
    return show;
  }

  function download(name, text, type = "text/markdown") {
    const a = el("a"); a.href = URL.createObjectURL(new Blob([text], { type })); a.download = name;
    document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }

  return { $, $$, el, safeUrl, store, post, stream, tabs, download, csrf };
})();

document.querySelectorAll("[data-tabs]").forEach(t => { t._show = KO.tabs(t); });

/* The KO editor. opts: {text, savedText?, storageKey?, urls:{check,save,library}, canEdit, getPack?(), onSaved?()} */
function KOEditor(root, opts) {
  const { $, el } = KO;
  const ta = $(".ed-text", root), status = $(".ed-status", root), preview = $(".ed-preview", root), checks = $(".ed-checks", root);
  const force = $(".ed-force", root), forceBox = $(".ed-force-box", root), save = $(".ed-save", root), result = $(".ed-result", root);
  const unsaved = $(".ed-unsaved", root), replace = $(".ed-replace", root);
  let last = null, timer = null, seq = 0;
  ta.value = (opts.storageKey && KO.store.get(opts.storageKey)) || opts.text || "";

  function setStatus(kind, text) { status.className = "ed-status status " + kind; status.textContent = text; }
  function list(title, items, cls) {
    if (!items.length) return;
    checks.appendChild(el("p", null, "")).appendChild(el("b", null, `${title} (${items.length})`));
    const ul = el("ul", cls); items.forEach(i => ul.appendChild(el("li", null, i))); checks.appendChild(ul);
  }
  async function check() {
    const my = ++seq;
    let j;
    try { j = await KO.post(opts.urls.check, { text: ta.value }); } catch (e) { setStatus("bad", e.message); return; }
    if (my !== seq) return;  // a newer check is on its way
    last = j;
    if (j.ok && !j.warnings.length) setStatus("ok", "Ready to save.");
    else if (j.ok) setStatus("info", `You can save it. ${j.warnings.length} thing(s) to double-check before publishing (see Checks).`);
    else setStatus("bad", `${j.errors.length} problem(s) to fix. Open the Checks tab.`);
    preview.innerHTML = j.preview || "";  // server-rendered; KO text is escaped there
    if (!j.preview) preview.appendChild(el("p", "notice", j.parse_error || "Nothing to show."));
    checks.textContent = "";
    if (!j.errors.length && !j.warnings.length) checks.appendChild(el("p", "status ok", "No problems found."));
    list("Problems to fix", j.errors, "bad");
    list("Double-check before publishing", j.warnings, "warn");
    force.hidden = j.ok;
    replace.hidden = !j.exists;
    replace.textContent = j.exists ? `This replaces the saved copy of ${j.ko_id}. If you changed the content, raise the version number.` : "";
    refreshSave();
  }
  function refreshSave() {
    save.disabled = !opts.canEdit || !last || (!last.ok && !forceBox.checked);
    if (opts.savedText != null) unsaved.hidden = ta.value === opts.savedText;
  }
  ta.addEventListener("input", () => {
    if (opts.storageKey) { if (opts.savedText != null && ta.value === opts.savedText) KO.store.del(opts.storageKey); else KO.store.set(opts.storageKey, ta.value); }
    refreshSave(); clearTimeout(timer); timer = setTimeout(check, 400);
  });
  forceBox.addEventListener("change", refreshSave);
  $(".ed-revert", root).addEventListener("click", () => { ta.value = opts.savedText; if (opts.storageKey) KO.store.del(opts.storageKey); check(); refreshSave(); });
  $(".ed-download", root).addEventListener("click", () => KO.download(`${(last && last.ko_id) || "ko"}.md`, ta.value));
  save.addEventListener("click", async () => {
    save.disabled = true; result.textContent = "Saving…"; result.className = "ed-result";
    try {
      const j = await KO.post(opts.urls.save, { text: ta.value, force: forceBox.checked, pack: opts.getPack ? opts.getPack() : null });
      result.className = "ed-result status ok"; result.textContent = j.message + " ";
      const a = el("a", null, "Open it in the library"); a.href = j.library_url; result.appendChild(a);
      opts.savedText = ta.value; if (opts.storageKey) KO.store.del(opts.storageKey);
      if (opts.onSaved) opts.onSaved(j);
      check();
    } catch (e) { result.className = "ed-result status bad"; result.textContent = e.message; refreshSave(); }
  });
  check();
  return { setText(t) { ta.value = t; if (opts.storageKey) KO.store.set(opts.storageKey, t); check(); }, get text() { return ta.value; } };
}
