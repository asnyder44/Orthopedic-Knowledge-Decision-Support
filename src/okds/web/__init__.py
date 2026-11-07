"""KO Portal pages, served by the hub's Flask app under /ko (replaces the old Streamlit portal).

  /ko/                   What is a Knowledge Object (at a glance + full article)
  /ko/generator          Knowledge Object Generator (5-step wizard, generator prompt, 2-minute guide)
  /ko/library            Browse and read KOs;  /ko/manage  check, edit, import, export, delete
  /ko/topics             KO Topics (concept registry);  /ko/sources  data-source catalog and inventory
  /ko/orthobot           OrthoBot over the KOs only (quick answer, or AI answer when allowed)
  /ko/api/...            JSON endpoints used by the pages' scripts

Who can change things: reading is open to everyone. Saving, importing, deleting, adding topics,
fetching pages and AI drafts ("editing") are allowed for requests from this computer (127.0.0.1),
or after signing in with OKDS_EDIT_PASSWORD. Set OKDS_EDIT_LOCAL=0 to require the password locally too.
"""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import hmac
import io
import json
import os
import re
import secrets
import threading
import time
import zipfile
from collections import defaultdict, deque
from collections.abc import Iterator
from functools import wraps
from pathlib import Path

from flask import (
    Blueprint,
    Response,
    abort,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    send_file,
    session,
    stream_with_context,
    url_for,
)
from markdown_it import MarkdownIt
from markupsafe import Markup, escape
from werkzeug.exceptions import HTTPException

from .. import chatbot, generator, kindex, llm, vocab
from .. import registry as reg
from ..config import PACKAGE_DIR, SEARCH_METHODS, get_settings
from ..fetch import FetchError, fetch_page
from ..ko import (
    KODocument,
    KOFormatError,
    as_dict,
    as_list,
    iter_sections,
    normalize_heading,
    parse_ko,
    render_ko,
    to_json_record,
)
from ..storage import StorageError, get_store
from ..validator import ValidationResult, validate_doc, validate_text
from . import texts

CONTENT_DIR = PACKAGE_DIR / "content"
STATIC_DIR = Path(__file__).parent / "static"
LOCAL_ADDRESSES = {"127.0.0.1", "::1"}
MAX_QUESTION_CHARS = 500
SOURCE_FIELDS = ["title", "publisher", "url", "source_type", "audience", "publication_date",
                 "retrieved_date", "permitted_use", "evidence_strength", "notes", "text"]
MARKER_RE = re.compile(r"\s*\[S\d+\]")
QUESTION_RE = re.compile(r"^\s*\d+[.)]\s*(.+?\?)", re.M)
CITE_RE = re.compile(r"\[(\d{1,2})\]")
METHOD_LABELS = {"hybrid": "Hybrid (words + meaning)", "keyword": "Keyword (same words)",
                 "semantic": "Semantic (same meaning)"}
TEMPLATE_NOTE = "Template ready. Open the Edit tab and replace every TODO with facts from your sources."

bp = Blueprint("ko", __name__, url_prefix="/ko", template_folder="templates",
               static_folder="static", static_url_path="/static")

_md = MarkdownIt("commonmark", {"html": False}).enable("table")


# ---------------------------------------------------------------- small helpers

def md(text: str) -> Markup:
    """Markdown to HTML. Raw HTML in the text is shown as text, never run (html=False)."""
    return Markup(_md.render(str(text or "")))


def md_inline(text: str) -> Markup:
    return Markup(_md.renderInline(str(text or "")))


def cite_badges(html: Markup | str) -> Markup:
    """[1], [2] ... in already-escaped HTML become small badges that match the citation cards."""
    return Markup(CITE_RE.sub(r'<span class="cite">\1</span>', str(html)))


def smaller_headings(body: str) -> str:
    """KO '##'/'###' headings shown two levels smaller, so they don't look like page titles."""
    out = []
    for line in body.split("\n"):
        if line.startswith("### "):
            line = "##### " + line[4:]
        elif line.startswith("## "):
            line = "#### " + line[3:]
        out.append(line)
    return "\n".join(out)


def without_title(text: str) -> str:
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return "\n".join(lines[:i] + lines[i + 1:]).lstrip("\n")
        if line.strip():
            break
    return text


def demote(text: str, levels: int) -> str:
    out, in_code = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_code = not in_code
        elif not in_code and line.startswith("#"):
            hashes = len(line) - len(line.lstrip("#"))
            if line[hashes:hashes + 1] == " ":
                line = "#" * min(6, hashes + levels) + line[hashes:]
        out.append(line)
    return "\n".join(out)


def load_content(name: str) -> str:
    return (CONTENT_DIR / name).read_text(encoding="utf-8")


def store():
    return get_store(get_settings())


def load_registry() -> dict[str, reg.Concept]:
    return reg.load_registry(get_settings().registry_path)


def read_catalog() -> list[dict[str, str]]:
    path = get_settings().catalog_path
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return [row for row in csv.DictReader(f) if row.get("name")]


def to_csv(rows: list[dict]) -> str:
    if not rows:
        return ""
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()


def cluster(doc: KODocument) -> int:
    try:
        return int(doc.front.get("cluster") or 0)
    except (TypeError, ValueError):
        return 0


def topic_name(n: int) -> str:
    return str(vocab.load_vocab().get("clusters", {}).get(n, f"Topic {n}" if n else "Other"))


def short_title(title: str) -> str:
    """'Carpal Tunnel Syndrome (CTS)' -> 'Carpal Tunnel Syndrome' (for the 'What is ...?' question)."""
    return re.split(r" \(| — | – |: ", title, maxsplit=1)[0]


def test_questions(doc: KODocument) -> list[str]:
    for h2, _h3, text in iter_sections(doc.body):
        if normalize_heading(h2) == "test questions":
            return [m.group(1).strip() for m in QUESTION_RE.finditer(text)]
    return []


def sorted_docs(entries) -> list[KODocument]:
    return sorted((e.doc for e in entries if e.doc is not None),
                  key=lambda d: (cluster(d) or 99, str(d.front.get("title", d.ko_id)).lower()))


def issues_json(result: ValidationResult) -> dict:
    return {"ok": result.ok, "errors": [i.message for i in result.errors],
            "warnings": [i.message for i in result.warnings]}


# ---------------------------------------------------------------- who may edit

def edit_password() -> str:
    return os.environ.get("OKDS_EDIT_PASSWORD", "")


def _password_tag(password: str) -> str:
    return hashlib.sha256(("okds-editor\x00" + password).encode()).hexdigest()[:24]


def is_local_request() -> bool:
    if os.environ.get("OKDS_EDIT_LOCAL", "1").strip() == "0":
        return False
    if request.headers.get("X-Forwarded-For") or request.headers.get("Forwarded"):
        return False  # came through a proxy: the real visitor is somewhere else
    return request.remote_addr in LOCAL_ADDRESSES


def can_edit() -> bool:
    password = edit_password()
    if password and hmac.compare_digest(session.get("ko_editor", ""), _password_tag(password)):
        return True
    return is_local_request()


def public_ai_enabled() -> bool:
    return os.environ.get("ORTHOBOT_AI", "").strip() == "1"


def ai_allowed() -> bool:
    """AI answers in the KO OrthoBot: for editors, or for everyone when ORTHOBOT_AI=1. Needs a key."""
    return get_settings().ai_ready and (can_edit() or public_ai_enabled())


def is_api() -> bool:
    return request.path.startswith(f"{bp.url_prefix}/api/")


def jerr(status: int, message: str):
    resp = jsonify({"error": message})
    resp.status_code = status
    return resp


def editor_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not can_edit():
            msg = ("Editing is off for this visitor. Sign in as an editor (KO Portal → Sign in) "
                   "or run the app on your own computer.")
            if is_api():
                return jerr(403, msg)
            flash(msg, "error")
            return redirect(url_for("ko.login", next=request.full_path))
        return view(*args, **kwargs)
    return wrapped


class RateLimiter:
    """Per-process sliding window: at most `per_minute` calls per client address (0 = no limit)."""

    def __init__(self, per_minute: int):
        self.per_minute, self._hits, self._lock = per_minute, defaultdict(deque), threading.Lock()

    def allow(self, key: str) -> bool:
        if self.per_minute <= 0:
            return True
        now = time.monotonic()
        with self._lock:
            q = self._hits[key]
            while q and now - q[0] > 60:
                q.popleft()
            if len(self._hits) > 10_000:
                for k in [k for k, v in self._hits.items() if not v or now - v[-1] > 60]:
                    del self._hits[k]
            if len(q) >= self.per_minute:
                return False
            q.append(now)
            return True


ai_limiter = RateLimiter(int(os.environ.get("OKDS_AI_RATE_LIMIT", "10")))
fetch_limiter = RateLimiter(int(os.environ.get("OKDS_FETCH_RATE_LIMIT", "20")))


# ---------------------------------------------------------------- request hooks

def csrf_token() -> str:
    token = session.get("csrf")
    if not token:
        token = session["csrf"] = secrets.token_urlsafe(32)
    return token


@bp.before_request
def _check_csrf():
    if request.method == "POST":
        sent = request.headers.get("X-CSRF-Token") or request.form.get("csrf_token", "")
        if not sent or not hmac.compare_digest(sent, session.get("csrf", "")):
            msg = "This page is out of date. Reload it and try again."
            if is_api():
                return jerr(400, msg)
            flash(msg, "error")
            return redirect(request.referrer or url_for("ko.home"))
    return None


@bp.errorhandler(HTTPException)
def _http_error(exc: HTTPException):
    if is_api():
        return jerr(exc.code or 500, exc.description or exc.name)
    return exc


@bp.context_processor
def _context():
    s = get_settings()
    return {"can_edit": can_edit(), "login_available": bool(edit_password()), "settings": s,
            "csrf": csrf_token(), "md": md, "md_inline": md_inline, "topic_name": topic_name, "cluster": cluster}


# ---------------------------------------------------------------- sign in

@bp.route("/login", methods=["GET", "POST"])
def login():
    nxt = request.values.get("next", "")
    if not nxt.startswith("/ko") or nxt.startswith("//"):
        nxt = url_for("ko.home")
    if request.method == "POST":
        password = edit_password()
        if password and hmac.compare_digest(request.form.get("password", ""), password):
            session["ko_editor"] = _password_tag(password)
            session.permanent = False
            flash("Signed in. You can now save and change KOs.", "success")
            return redirect(nxt)
        time.sleep(1)  # slow down guessing
        flash("That password is not right." if password else "Sign-in is off: OKDS_EDIT_PASSWORD is not set.", "error")
    return render_template("ko/login.html", active="", next=nxt)


@bp.post("/logout")
def logout():
    session.pop("ko_editor", None)
    flash("Signed out.", "success")
    return redirect(url_for("ko.home"))


# ---------------------------------------------------------------- What is a Knowledge Object

@bp.get("/")
def home():
    subsections = vocab.load_vocab()["headings"]["explanation_subsections"]
    return render_template("ko/home.html", active="home", t=texts, subsections=subsections,
                           article=md(load_content("knowledge-objects.md")))


@bp.get("/article.md")
def article_md():
    return Response(load_content("knowledge-objects.md"), mimetype="text/markdown",
                    headers={"Content-Disposition": "attachment; filename=knowledge-objects.md"})


# ---------------------------------------------------------------- Generator

@bp.get("/generator")
def generator_page():
    s = get_settings()
    registry = load_registry()
    specs = vocab.specialties()
    topics = [{"ko_id": c.ko_id, "term": c.preferred_term, "ko_type": c.ko_type,
               "specialty": specs.get(c.specialty, c.specialty), "alternate_terms": c.alternate_terms}
              for c in sorted(registry.values(), key=lambda c: c.preferred_term.lower())]
    catalog = []
    for row in read_catalog():
        catalog.append({
            "name": row.get("name", ""), "publisher": row.get("publisher", ""), "url": row.get("url", ""),
            "source_type": row.get("okds_source_type") if row.get("okds_source_type") in vocab.enum("source_type") else "",
            "permitted_use": (row.get("okds_permitted_use")
                              if row.get("okds_permitted_use") in vocab.enum("permitted_use") else ""),
            "notes": f"Catalog: {row.get('name', '')}. Terms: {row.get('license_terms', '')}"[:300],
        })
    data = {
        "topics": topics, "ko_types": vocab.ko_types(), "specialties": specs, "catalog": catalog,
        "enums": {name: vocab.enum(name) for name in ("audience", "difficulty", "source_type", "permitted_use")},
        "ai_ready": s.ai_ready, "ai_label": s.ai_label, "can_edit": can_edit(), "today": dt.date.today().isoformat(),
        "help": texts.FIELD_HELP, "steps": texts.STEPS,
        "urls": {"draft": url_for("ko.api_draft"), "check": url_for("ko.api_check"), "save": url_for("ko.api_save"),
                 "fetch": url_for("ko.api_fetch"), "topic": url_for("ko.api_topic"),
                 "library": url_for("ko.library"), "prompts": url_for("ko.api_prompts")},
    }
    prompt = load_content("ko-generator-prompt.md")
    return render_template("ko/generator.html", active="generator", data=data,
                           prompt_html=md(demote(without_title(prompt), 2)), system_prompt=generator.system_prompt(),
                           field_table=texts.FIELD_TABLE)


@bp.get("/generator-prompt.md")
def generator_prompt_md():
    return Response(load_content("ko-generator-prompt.md"), mimetype="text/markdown",
                    headers={"Content-Disposition": "attachment; filename=ko-generator-prompt.md"})


@bp.get("/guide")
def guide():
    """The animated 2-minute guide (our own static file), shown in a frame on the Generator page."""
    resp = send_file(STATIC_DIR / "generator_guide.html", mimetype="text/html")
    resp.headers["X-Frame-Options"] = "SAMEORIGIN"
    resp.headers["Content-Security-Policy"] = ("default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; "
                                               "script-src 'self' 'unsafe-inline'; frame-ancestors 'self'")
    return resp


def ko_request(body: dict, registry: dict[str, reg.Concept]) -> generator.KORequest:
    """The wizard's fields as a generator request. ValueError with a plain message when something is missing."""
    concept = registry.get(str(body.get("ko_id", "")))
    if concept is None:
        raise ValueError("Choose a topic (step 1).")
    allowed = vocab.enum("audience")
    audience = [a for a in as_list(body.get("audience")) if a in allowed]
    if not audience:
        raise ValueError("Choose at least 1 reader (step 2).")
    raw_sources = [s for s in as_list(body.get("sources")) if isinstance(s, dict)]
    if len(raw_sources) > 20:
        raise ValueError("Use at most 20 sources.")
    sources = []
    for i, src in enumerate(raw_sources, 1):
        s: dict = {"id": f"S{i}"}
        for field in SOURCE_FIELDS:
            value = src.get(field, "")
            s[field] = value.strip() if isinstance(value, str) else ("" if value is None else str(value))
        s["evidence_strength"] = s.get("evidence_strength") or None
        sources.append(s)
    if len([s for s in sources if s["url"] and s["title"] and s["publisher"]]) < 2:
        raise ValueError("Fill in the page link, title, and publisher for 2 sources (step 3).")
    difficulty = body.get("difficulty") if body.get("difficulty") in vocab.enum("difficulty") else "beginner"
    return generator.KORequest(
        concept=concept, audience=audience, reading_level=str(body.get("reading_level") or "")[:40],
        difficulty=difficulty, sources=sources, author=str(body.get("author") or "")[:80],
        license_name=str(body.get("license") or "CC-BY-4.0")[:40])


def ndjson(items: Iterator[dict]) -> Response:
    lines = (json.dumps(item, ensure_ascii=False) + "\n" for item in items)
    return Response(stream_with_context(lines), mimetype="application/x-ndjson",
                    headers={"Cache-Control": "no-store", "X-Accel-Buffering": "no"})


@bp.post("/api/prompts")
@editor_required
def api_prompts():
    """For experts: the exact instructions the AI would get for these wizard fields."""
    try:
        req = ko_request(request.get_json(silent=True) or {}, load_registry())
    except ValueError as e:
        return jerr(400, str(e))
    return jsonify({"system": generator.system_prompt(), "user": generator.user_prompt(req, load_registry())})


@bp.post("/api/draft")
@editor_required
def api_draft():
    body = request.get_json(silent=True) or {}
    registry = load_registry()
    try:
        req = ko_request(body, registry)
    except ValueError as e:
        return jerr(400, str(e))
    pack = generator.render_source_pack(req)
    if body.get("mode") != "ai":
        return jsonify({"markdown": generator.template_draft(req), "pack": pack, "notes": [TEMPLATE_NOTE]})
    s = get_settings()
    if not s.ai_ready:
        return jerr(400, "AI is off (no API key). Use the empty template, or add a Claude or OpenAI key to .env.")
    problems = generator.check_pack(req)
    if problems:
        return jerr(400, " ".join(problems))
    if not ai_limiter.allow(request.remote_addr or "?"):
        return jerr(429, "Too many AI requests in a short time. Wait a minute and try again.")

    def run() -> Iterator[dict]:
        result = llm.StreamResult()
        try:
            for text in generator.ai_draft_stream(req, registry, s.ai_model, s.generator_effort, result,
                                                  provider=s.ai_provider):
                yield {"t": text}
            markdown, notes = generator.finalize(result.text, req, s.ai_model)
            if result.stop_reason == "max_tokens":
                notes.append("The draft hit the length limit and may be cut off.")
            yield {"done": True, "markdown": markdown, "pack": pack, "notes": notes}
        except llm.LLMError as e:
            yield {"error": str(e)}

    return ndjson(run())


@bp.post("/api/fetch")
@editor_required
def api_fetch():
    url = str((request.get_json(silent=True) or {}).get("url") or "").strip()
    if not url:
        return jerr(400, "Paste the page link first.")
    if not fetch_limiter.allow(request.remote_addr or "?"):
        return jerr(429, "Too many page fetches in a short time. Wait a minute and try again.")
    try:
        page = fetch_page(url)
    except FetchError as e:
        return jerr(400, str(e))
    return jsonify({"url": page.url, "title": page.title, "text": page.text, "retrieved": dt.date.today().isoformat(),
                    "message": "Got the page text. Now delete the parts that are not about your topic."})


@bp.post("/api/topic")
@editor_required
def api_topic():
    body = request.get_json(silent=True) or {}
    try:
        c = add_topic(body)
    except ValueError as e:
        return jerr(400, str(e))
    specs = vocab.specialties()
    return jsonify({"message": f"Added {c.preferred_term} ({c.ko_id}).",
                    "topic": {"ko_id": c.ko_id, "term": c.preferred_term, "ko_type": c.ko_type,
                              "specialty": specs.get(c.specialty, c.specialty), "alternate_terms": c.alternate_terms}})


def add_topic(fields) -> reg.Concept:
    return reg.add_concept(
        get_settings().registry_path,
        preferred_term=str(fields.get("term") or ""),
        ko_type=str(fields.get("ko_type") or ""),
        specialty=str(fields.get("specialty") or ""),
        alternate_terms=str(fields.get("alternate_terms") or "").split(";"),
        mesh_id=str(fields.get("mesh") or ""),
        icd10cm=str(fields.get("icd10cm") or ""),
    )


# ---------------------------------------------------------------- editor API (check + save)

@bp.post("/api/check")
def api_check():
    text = str((request.get_json(silent=True) or {}).get("text") or "")
    result = validate_text(text, load_registry())
    out = issues_json(result)
    try:
        doc = parse_ko(text)
    except KOFormatError as e:
        out.update(preview=None, parse_error=str(e), ko_id=None, exists=False)
        return jsonify(out)
    try:
        preview = render_template("ko/_preview.html", doc=doc, front=doc.front, review=as_dict(doc.front.get("review")),
                                  specialty=vocab.specialties().get(doc.front.get("specialty"), doc.front.get("specialty")),
                                  body=md(smaller_headings(doc.body)),
                                  data=json.dumps(doc.front, indent=2, ensure_ascii=False, default=str))
    except Exception as e:  # an odd file: say so instead of failing
        preview = f'<p class="notice">Cannot show a preview ({escape(type(e).__name__)}).</p>'
    exists = any(e.ko_id == doc.ko_id and e.doc is not None for e in store().list_entries())
    out.update(preview=preview, ko_id=doc.ko_id, exists=exists)
    return jsonify(out)


@bp.post("/api/save")
@editor_required
def api_save():
    body = request.get_json(silent=True) or {}
    text = str(body.get("text") or "")
    result = validate_text(text, load_registry())
    if not result.ok and body.get("force") is not True:
        return jerr(400, f"{len(result.errors)} problem(s) to fix first, or tick 'Save anyway as a draft'.")
    try:
        doc = parse_ko(text)
        pack = body.get("pack")
        saved = store().save(doc, source_pack=pack if isinstance(pack, str) and pack.strip() else None)
    except (KOFormatError, StorageError) as e:
        return jerr(400, f"Not saved: {e}")
    reg.set_status(get_settings().registry_path, doc.ko_id, "drafted")
    return jsonify({"saved": saved.ko_id, "message": f"Saved {saved.ko_id}. Find it in the KO Library.",
                    "library_url": url_for("ko.library", ko=saved.ko_id)})


# ---------------------------------------------------------------- Library (browse)

@bp.get("/library")
def library():
    entries = store().list_entries()
    docs = sorted_docs(entries)
    by_id = {d.ko_id: d for d in docs}
    q = request.args.get("q", "").strip()[:100]
    topic = request.args.get("topic", 0, type=int)
    topics = sorted({cluster(d) for d in docs})
    counts = {n: sum(cluster(d) == n for d in docs) for n in topics}
    if topic not in topics:
        topic = 0

    def matches(d: KODocument) -> bool:
        f = d.front
        haystack = " ".join(map(str, [f.get("title", ""), d.ko_id, f.get("summary", ""), *as_list(f.get("tags")),
                                      *as_list(f.get("alternate_terms"))])).lower()
        return (not topic or cluster(d) == topic) and (not q or q.lower() in haystack)

    shown = [d for d in docs if matches(d)]
    selected = by_id.get(request.args.get("ko", ""))
    detail = None
    if selected is not None:
        try:
            detail = _detail(selected, by_id)
        except Exception as e:  # an odd file: say so instead of breaking the page
            detail = {"error": f"This KO file has an unexpected format ({e}). Fix it in Manage."}
    return render_template("ko/library.html", active="library", docs=docs, shown=shown, q=q, topic=topic,
                           topics=topics, counts=counts, selected=selected, detail=detail, n_entries=len(entries))


def _detail(doc: KODocument, by_id: dict[str, KODocument]) -> dict:
    f = doc.front
    title = str(f.get("title", doc.ko_id))
    review = as_dict(f.get("review"))
    links = []
    for r in as_list(f.get("relationships")):
        if isinstance(r, dict) and r.get("target_id") in by_id:
            target = by_id[r["target_id"]]
            links.append({"words": str(r.get("predicate", "")).replace("_", " ").lower(), "ko_id": target.ko_id,
                          "title": target.front.get("title", target.ko_id)})
    result = validate_doc(doc, load_registry())
    return {
        "title": title, "review": review, "status": review.get("status", "draft"),
        "summary": MARKER_RE.sub("", str(f.get("summary") or "")).strip(),
        "difficulty": str(f.get("difficulty") or "").capitalize(), "topic": topic_name(cluster(doc)),
        "ask": f"What is {short_title(title)}?", "body": md(smaller_headings(doc.body)),
        "sources": [s for s in as_list(f.get("sources")) if isinstance(s, dict)], "links": links,
        "questions": test_questions(doc), "errors": len(result.errors), "warnings": len(result.warnings),
        "open_issues": [str(i) for i in as_list(review.get("open_issues"))],
    }


def _find(ko_id: str) -> KODocument:
    for e in store().list_entries():
        if e.ko_id == ko_id and e.doc is not None:
            return e.doc
    abort(404)


@bp.get("/library/<ko_id>.md")
def ko_markdown(ko_id: str):
    doc = _find(ko_id)
    return Response(render_ko(doc), mimetype="text/markdown",
                    headers={"Content-Disposition": f"attachment; filename={doc.ko_id}.md"})


@bp.get("/library/<ko_id>.json")
def ko_json(ko_id: str):
    doc = _find(ko_id)
    body = json.dumps(to_json_record(doc, f"{doc.ko_id}.md"), indent=2, ensure_ascii=False)
    return Response(body, mimetype="application/json",
                    headers={"Content-Disposition": f"attachment; filename={doc.ko_id}.json"})


# ---------------------------------------------------------------- Library (manage)

@bp.get("/manage")
def manage():
    entries = store().list_entries()
    registry = load_registry()
    rows = []
    for e in entries:
        if e.doc is None:
            rows.append({"ko_id": e.ko_id, "title": f"(cannot read this file: {e.error})", "problems": 1, "readable": False})
            continue
        f = e.doc.front
        try:
            result = validate_doc(e.doc, registry)
        except Exception as exc:  # one odd file must not break the page
            rows.append({"ko_id": e.ko_id, "title": f"(cannot check this file: {exc})", "problems": 1, "readable": True})
            continue
        rows.append({"ko_id": e.ko_id, "title": f.get("title"), "type": f.get("ko_type"),
                     "status": as_dict(f.get("review")).get("status"), "version": f.get("version"),
                     "problems": len(result.errors), "warnings": len(result.warnings), "readable": True})
    return render_template("ko/manage.html", active="library", rows=rows)


@bp.get("/manage/<ko_id>")
def manage_edit(ko_id: str):
    entries = store().list_entries()
    doc = next((e.doc for e in entries if e.ko_id == ko_id and e.doc is not None), None)
    if doc is None:
        abort(404)
    others = [(e.ko_id, e.doc.front.get("title")) for e in entries if e.doc is not None]
    return render_template("ko/manage_edit.html", active="library", doc=doc, text=render_ko(doc), others=others,
                           urls={"check": url_for("ko.api_check"), "save": url_for("ko.api_save"),
                                 "library": url_for("ko.library")})


@bp.post("/manage/import")
@editor_required
def manage_import():
    up = request.files.get("file")
    if up is None or not up.filename:
        flash("Choose a KO Markdown file (.md) to import.", "error")
        return redirect(url_for("ko.manage"))
    try:
        doc = parse_ko(up.read().decode("utf-8"))
    except (KOFormatError, UnicodeDecodeError) as e:
        flash(f"Cannot import: {e}", "error")
        return redirect(url_for("ko.manage"))
    if store().exists(str(doc.ko_id)) and request.form.get("replace") != "1":
        flash(f"{doc.ko_id} is already in the library. Tick 'Replace a KO with the same ID' to import it anyway.",
              "error")
        return redirect(url_for("ko.manage"))
    try:
        saved = store().save(doc)
    except StorageError as e:
        flash(f"Cannot import: {e}", "error")
        return redirect(url_for("ko.manage"))
    flash(f"Imported {saved.ko_id}. Check it in the list.", "success")
    return redirect(url_for("ko.manage"))


@bp.get("/export.zip")
@editor_required
def export_zip():
    s = get_settings()
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for folder in (s.kos_dir, s.json_dir, s.packs_dir):
            for path in folder.rglob("*"):
                if path.is_file():
                    z.write(path, path.relative_to(s.data_dir).as_posix())
        if s.registry_path.is_file():
            z.write(s.registry_path, "registry.csv")
    buf.seek(0)
    return send_file(buf, mimetype="application/zip", as_attachment=True, download_name="okds_library.zip")


@bp.post("/manage/rebuild")
@editor_required
def manage_rebuild():
    flash(f"Rebuilt {store().rebuild_json()} data file(s).", "success")
    return redirect(url_for("ko.manage"))


@bp.post("/manage/<ko_id>/delete")
@editor_required
def manage_delete(ko_id: str):
    if request.form.get("confirm") != ko_id:
        flash(f"Tick 'Yes, delete {ko_id}' first.", "error")
        return redirect(url_for("ko.manage_edit", ko_id=ko_id))
    try:
        store().delete(ko_id)
    except StorageError as e:
        flash(f"Not deleted: {e}", "error")
        return redirect(url_for("ko.manage"))
    flash(f"Deleted {ko_id}. Its ID is never reused.", "success")
    return redirect(url_for("ko.manage"))


# ---------------------------------------------------------------- Topics

@bp.route("/topics", methods=["GET", "POST"])
def topics():
    form = {}
    if request.method == "POST":
        if not can_edit():
            return editor_required(lambda: None)()
        form = request.form.to_dict()
        try:
            c = add_topic(form)
        except ValueError as e:
            flash(str(e), "error")
        else:
            flash(f"Added {c.preferred_term} ({c.ko_id}).", "success")
            return redirect(url_for("ko.topics"))
    registry = load_registry()
    specs = vocab.specialties()
    rows = [{"term": c.preferred_term, "ko_id": c.ko_id, "type": c.ko_type, "specialty": specs.get(c.specialty, c.specialty),
             "alts": "; ".join(c.alternate_terms), "status": c.status}
            for c in sorted(registry.values(), key=lambda c: c.preferred_term.lower())]
    v = vocab.load_vocab()
    return render_template("ko/topics.html", active="topics", rows=rows, v=v, specs=specs, ko_types=vocab.ko_types(),
                           form=form, help=texts.FIELD_HELP)


# ---------------------------------------------------------------- Sources

def _filtered_catalog() -> tuple[list[dict], list[dict]]:
    catalog = read_catalog()
    views, cats = request.args.getlist("view"), request.args.getlist("cat")
    q = request.args.get("q", "").strip().lower()[:100]
    rows = [r for r in catalog
            if (not views or r.get("view") in views) and (not cats or r.get("category") in cats)
            and (not q or q in " ".join(v or "" for v in r.values()).lower())]
    return catalog, rows


def _inventory() -> list[dict]:
    out = []
    for e in store().list_entries():
        if e.doc is None:
            continue
        for src in as_list(e.doc.front.get("sources")):
            if isinstance(src, dict):
                out.append({"ko_id": e.ko_id, "topic": e.doc.front.get("title"), "source_id": src.get("id"),
                            "title": src.get("title"), "publisher": src.get("publisher"), "url": src.get("url"),
                            "source_type": src.get("source_type"), "audience": src.get("audience"),
                            "publication_date": src.get("publication_date"),
                            "retrieved_date": src.get("retrieved_date"), "permitted_use": src.get("permitted_use")})
    return out


@bp.get("/sources")
def sources():
    catalog, rows = _filtered_catalog()
    return render_template(
        "ko/sources.html", active="sources", catalog=catalog, rows=rows, inventory=_inventory(),
        views=sorted({r.get("view", "") for r in catalog} - {""}), cats=sorted({r.get("category", "") for r in catalog} - {""}),
        picked_views=request.args.getlist("view"), picked_cats=request.args.getlist("cat"),
        q=request.args.get("q", ""), tab=request.args.get("tab", "catalog"))


@bp.get("/sources/catalog.csv")
def catalog_csv():
    _catalog, rows = _filtered_catalog()
    return Response(to_csv(rows), mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=okds_source_catalog.csv"})


@bp.get("/sources/inventory.csv")
def inventory_csv():
    return Response(to_csv(_inventory()), mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=okds_source_inventory.csv"})


# ---------------------------------------------------------------- Discovery Network (prototype)

@bp.get("/network")
def network_page():
    from .. import network

    net = network.build_network(get_settings())
    conds = network.conditions(net)
    pick = request.args.get("condition") or (conds[0]["id"] if conds else "")
    focus = request.args.get("focus", "")
    return render_template(
        "ko/network.html", active="network", net=net, insights=network.insights(net), conditions=conds,
        condition=pick, journey=network.journey(net, pick) if pick else [], focus=focus,
        tab=request.args.get("tab", "explore"), planned_types=network.PLANNED_OBJECT_TYPES)


@bp.get("/api/network")
def api_network():
    """The whole network as JSON (nodes, edges, vocabulary), for the graph view and for the team's experiments."""
    from .. import network

    return jsonify(network.build_network(get_settings()))


# ---------------------------------------------------------------- OrthoBot (KOs only)

@bp.get("/orthobot")
def orthobot():
    s = get_settings()
    index = kindex.get_index(s)
    docs = kindex.load_docs(s)
    return render_template(
        "ko/orthobot.html", active="orthobot", n_docs=len(docs), n_chunks=len(index.chunks),
        starters=chatbot.starter_questions(docs), semantic=index.semantic, ai_allowed=ai_allowed(),
        methods=[(m, METHOD_LABELS[m]) for m in SEARCH_METHODS],
        default_method=s.search_method if s.search_method in SEARCH_METHODS else "hybrid",
        ask=request.args.get("q", "")[:MAX_QUESTION_CHARS],
        urls={"ask": url_for("ko.api_ask"), "library": url_for("ko.library")})


def answer_payload(ans: chatbot.Answer, label: str) -> dict:
    meta = ""
    if ans.mode != "chat" and ans.citations:
        n = len({c["ko_id"] for c in ans.citations})
        meta = f"{label} · from {len(ans.citations)} passage(s) in {n} KO(s)"
    return {"html": str(cite_badges(md(ans.text))), "text": ans.text, "citations": ans.citations,
            "suggestions": ans.suggestions, "warnings": ans.warnings, "read": ans.passages_read, "meta": meta}


@bp.post("/api/ask")
def api_ask():
    body = request.get_json(silent=True) or {}
    question = " ".join(str(body.get("question") or "").split())
    if not question:
        return jerr(400, "Please type a question.")
    if len(question) > MAX_QUESTION_CHARS:
        return jerr(400, f"Please keep your question under {MAX_QUESTION_CHARS} characters.")
    s = get_settings()
    method = body.get("method") if body.get("method") in SEARCH_METHODS else s.search_method
    if method not in SEARCH_METHODS:
        method = "keyword"
    use_ai = body.get("mode") == "ai"
    if use_ai and not ai_allowed():
        return jerr(403, "AI answers are not available here. Use Quick answer.")
    index = kindex.get_index(s)
    if not index.chunks:
        return jerr(400, "No KOs yet. Save one in the Knowledge Object Generator first.")
    if use_ai and not ai_limiter.allow(request.remote_addr or "?"):
        return jerr(429, "Too many AI questions in a short time. Wait a minute, or use Quick answer.")

    def run() -> Iterator[dict]:
        label = "Quick answer"
        ans = chatbot.small_talk(question, index)
        if ans is None and not use_ai:
            ans = chatbot.answer_retrieval_only(question, index, method)
        elif ans is None:
            r = chatbot.retrieve(question, index, method)
            if not r.confident:
                ans = chatbot.no_answer(index, "ai", r.warnings)
            else:
                result = llm.StreamResult()
                try:
                    for text in chatbot.stream_ai_answer(r, s, result):
                        yield {"t": text}
                    ans = chatbot.finish_ai_answer(result.text, r, index)
                    label = f"AI answer ({s.ai_label} · {s.ai_model})"
                except llm.LLMError as e:
                    yield {"reset": True}  # remove any half-written AI text
                    ans = chatbot.answer_retrieval_only(question, index, method)
                    ans.warnings.insert(0, f"The AI is not available ({e}) This is a quick answer instead.")
        yield {"done": True, "answer": answer_payload(ans, label)}

    return ndjson(run())
