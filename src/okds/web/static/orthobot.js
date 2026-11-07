/* KO OrthoBot: chat on the left, citations on the right. Answers stream in as newline-delimited JSON. */
"use strict";
(() => {
  const { $, $$, el, safeUrl } = KO;
  const dataEl = $("#bot-data");
  if (!dataEl) return;
  const D = JSON.parse(dataEl.textContent);
  const HIST = "ko-bot-history", QUOTE_CHARS = 360;
  const log = $("#bot-log"), cites = $("#bot-cites");
  let history = KO.store.get(HIST, []), busy = false;

  function quote(text) {
    let q = (text || "").split("\n").map(l => l.replace(/^\s*(?:[-*•]|\d+[.)])\s+/, "").trim()).filter(Boolean).join(" ");
    if (q.length > QUOTE_CHARS) q = q.slice(0, QUOTE_CHARS).replace(/\s+\S*$/, "") + "…";
    return `“${q}”`;
  }
  function renderCites(ans) {
    cites.textContent = "";
    const list = (ans && ans.citations) || [];
    if (!list.length) { cites.appendChild(el("p", "muted small", "After you ask a question, the KO parts used in the answer show here.")); return; }
    list.forEach(c => {
      const card = el("div", "card citecard"), h = el("div", "citehead");
      h.appendChild(el("span", "cite", String(c.n))); h.appendChild(el("b", null, " " + c.title));
      const read = el("a", "small", "Read"); read.href = `${D.urls.library}?ko=${encodeURIComponent(c.ko_id)}`; read.target = "_blank"; read.rel = "noopener";
      h.appendChild(read); card.appendChild(h);
      card.appendChild(el("p", "muted small", `Section: ${c.section} · ${c.ko_id} · ${c.review_status}`));
      card.appendChild(el("p", null, quote(c.quote)));
      const det = el("details"); det.appendChild(el("summary", null, "Original sources"));
      (c.sources || []).forEach(s => {
        const p = el("p", "small"); p.appendChild(document.createTextNode(`[${s.id}] ${s.publisher || ""}: `));
        const href = safeUrl(s.url);
        if (href) { const a = el("a", null, s.title || s.url); a.href = href; a.target = "_blank"; a.rel = "noopener"; p.appendChild(a); }
        else p.appendChild(document.createTextNode(s.title || ""));
        det.appendChild(p);
      });
      card.appendChild(det); cites.appendChild(card);
    });
    const extra = (ans.read || 0) - list.length;
    if (extra > 0) cites.appendChild(el("p", "muted small", `${extra} more passage(s) were read but not quoted.`));
  }
  function chips(options) {
    const box = el("div", "chips");
    options.forEach(q => { const b = el("button", "chipbtn", q); b.type = "button"; b.dataset.ask = q; box.appendChild(b); });
    return box;
  }
  function bubble(msg) {
    const b = el("div", "bubble " + msg.role);
    if (msg.role === "user") b.textContent = msg.content;
    else {
      const body = el("div", "prose"); body.innerHTML = msg.html;  // server-rendered Markdown, raw HTML escaped
      b.appendChild(body);
      if (msg.meta) b.appendChild(el("p", "muted small", msg.meta));
      (msg.warnings || []).forEach(w => b.appendChild(el("p", "muted small", w)));
      if (msg.suggestions && msg.suggestions.length) { b.appendChild(el("p", "muted small", "Keep exploring:")); b.appendChild(chips(msg.suggestions)); }
    }
    log.appendChild(b); return b;
  }
  function redraw() {
    log.textContent = ""; history.forEach(bubble);
    const last = [...history].reverse().find(m => m.role === "assistant"); renderCites(last);
  }
  const mode = () => ($('input[name="bot-mode"]:checked') || {}).value || "quick";
  const method = () => ($('input[name="bot-method"]:checked') || {}).value || "keyword";

  async function ask(q) {
    q = (q || "").trim(); if (!q || busy) return;
    busy = true; $("#bot-send").disabled = true;
    history.push({ role: "user", content: q }); bubble(history[history.length - 1]);
    const wait = el("div", "bubble assistant"); const live = el("div", "live", "Searching the Knowledge Objects…"); wait.appendChild(live); log.appendChild(wait);
    wait.scrollIntoView({ block: "nearest" });
    let text = "";
    try {
      await KO.stream(D.urls.ask, { question: q, mode: mode(), method: method() }, item => {
        if (item.t) { text += item.t; live.textContent = text; }
        if (item.reset) { text = ""; live.textContent = "Searching the Knowledge Objects…"; }
        if (item.done) {
          wait.remove();
          const a = item.answer; const msg = { role: "assistant", html: a.html, meta: a.meta, warnings: a.warnings, suggestions: a.suggestions, citations: a.citations, read: a.read };
          history.push(msg); bubble(msg); renderCites(msg);
        }
      });
    } catch (e) { wait.remove(); const err = el("div", "bubble assistant err", e.message); log.appendChild(err); }
    finally { busy = false; $("#bot-send").disabled = false; KO.store.set(HIST, history.slice(-40)); }
  }

  $("#bot-form").addEventListener("submit", e => { e.preventDefault(); const q = $("#bot-q").value; $("#bot-q").value = ""; ask(q); });
  document.addEventListener("click", e => { const b = e.target.closest("[data-ask]"); if (b) ask(b.dataset.ask); });
  $("#bot-clear").addEventListener("click", () => { history = []; KO.store.del(HIST); redraw(); });
  redraw();
  if (D.ask) { ask(D.ask); window.history.replaceState(null, "", location.pathname); }  // don't ask again on reload
})();
