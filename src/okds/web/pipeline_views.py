"""KO Portal pages for the KO data pipeline (ported from the okds repo's Streamlit pages):

  /ko/pipeline        Pipeline status: run Job 1 (fetch) / Job 2 (generate), upload a document, article inbox,
                      run history, suggested topics, settings & schedule, and the "how it works" diagram
  /ko/review          Review queue: pipeline drafts, drafts already in the library, and uploaded data batches.
                      A person accepts (-> team_checked) or rejects (with a reason) each one.
"""

from __future__ import annotations

import html
import json
import re

from flask import abort, flash, redirect, render_template, request, send_file, session, url_for

from .. import registry as reg
from .. import vocab
from ..config import get_settings
from ..kindex import STATUS_RANK
from ..ko import KOFormatError, as_dict, as_list, parse_ko
from ..pipeline import jobs
from ..pipeline.store import PipelineStore
from ..storage import LocalKOStore
from ..validator import validate_doc, validate_text
from . import STATIC_DIR, bp, can_edit, editor_required, md, smaller_headings

MAX_UPLOAD_BYTES = 2_000_000
TEXT_TYPES = (".txt", ".md", ".markdown", ".html", ".htm")
INBOX_SECTIONS = [
    ("new", "New", "Passed every automatic check and was saved with its text. Waiting for Job 2."),
    ("used", "Used", "Job 2 used it as a source for a KO draft (in the Review queue or the KO Library)."),
    ("skipped", "Skipped", "Failed an automatic check, so it is not used. Only the reason is kept."),
]


def reviewer_name() -> str:
    return str(session.get("reviewer_name", ""))


def remember_name(name: str) -> str:
    name = " ".join(str(name or "").split())[:80]
    if name:
        session["reviewer_name"] = name
    return name


# ---------------------------------------------------------------- diagrams (static, framed)

def _framed(name: str):
    resp = send_file(STATIC_DIR / name, mimetype="text/html")
    resp.headers["X-Frame-Options"] = "SAMEORIGIN"
    resp.headers["Content-Security-Policy"] = ("default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; "
                                               "script-src 'self' 'unsafe-inline'; frame-ancestors 'self'")
    return resp


@bp.get("/pipeline/diagram")
def pipeline_diagram():
    return _framed("pipeline_diagram.html")


@bp.get("/pipeline/guide")
def pipeline_guide():
    return _framed("pipeline_guide.html")


# ---------------------------------------------------------------- pipeline status

@bp.get("/pipeline")
def pipeline_page():
    s = get_settings()
    store = PipelineStore(s)
    arts = store.articles()
    decisions = store.decisions()
    registry = reg.load_registry(s.registry_path)
    fetchable = jobs.fetchable_topics(s, store)
    inbox = {status: [a for a in arts if a.status == status] for status, _h, _i in INBOX_SECTIONS}
    metrics = [("New articles", len(inbox["new"])), ("Used articles", len(inbox["used"])),
               ("Skipped articles", len(inbox["skipped"])), ("KOs to review", len(store.queue_items())),
               ("Accepted / rejected", f"{sum(d['decision'].startswith('accepted') for d in decisions)} / "
                                       f"{sum(d['decision'] == 'rejected' for d in decisions)}")]
    settings_rows = [
        ("OKDS_PIPELINE_KOS_PER_RUN", s.pipeline_kos_per_run, "KOs Job 2 makes per run (1 per day)"),
        ("OKDS_PIPELINE_TOPICS_PER_FETCH", s.pipeline_topics_per_fetch, "topics Job 1 searches per run"),
        ("OKDS_PIPELINE_ARTICLES_PER_TOPIC", s.pipeline_articles_per_topic, "most articles kept per topic"),
        ("OKDS_PIPELINE_MIN_ARTICLES", s.pipeline_min_articles, "articles needed before a KO is made"),
        ("OKDS_PIPELINE_MAX_CHARS", s.pipeline_max_chars, "longest article text kept"),
        ("OKDS_CONTACT_EMAIL", "(set)" if s.contact_email else "(not set)", "your email, sent to NCBI with API calls"),
        ("OKDS_ORTHOBOT_MIN_STATUS", s.orthobot_min_status, "which KOs OrthoBot answers from"),
    ]
    return render_template(
        "ko/pipeline.html", active="pipeline", s=s, metrics=metrics, inbox=inbox, sections=INBOX_SECTIONS,
        runs=store.runs(30), suggested=jobs.suggested_topics(s)[:30], fetchable=fetchable,
        new_counts={c.ko_id: len(store.articles(c.ko_id, "new")) for c in fetchable},
        topics=sorted(registry.values(), key=lambda c: c.preferred_term.lower()), settings_rows=settings_rows,
        permitted=vocab.enum("permitted_use"), tab=request.args.get("tab", "inbox"),
        reports=session.pop("pipe_reports", None))


def _summary(rep) -> dict:
    return {"job": rep.job, "status": rep.status, "counts": rep.counts, "messages": rep.messages[:12],
            "cost": rep.est_cost_usd}


@bp.post("/pipeline/run")
@editor_required
def pipeline_run():
    s = get_settings()
    job = request.form.get("job", "")
    topic_ids = request.form.getlist("topic") if request.form.get("mode") == "chosen" else None
    if topic_ids == []:
        flash("Pick at least one topic for Job 1, or choose 'Topics with no KO yet'.", "error")
        return redirect(url_for("ko.pipeline_page"))
    reports = []
    if job in ("fetch", "both"):
        reports.append(_summary(jobs.fetch_job(s, topic_ids)))
    if job in ("generate", "both"):
        reports.append(_summary(jobs.generate_job(s)))
    if job == "template":
        reports.append(_summary(jobs.generate_job(s, template=True)))
    if not reports:
        abort(400)
    session["pipe_reports"] = reports
    return redirect(url_for("ko.pipeline_page"))


def _upload_text() -> str:
    up = request.files.get("file")
    if up is None or not up.filename:
        return request.form.get("text", "")
    name = up.filename.lower()
    if not name.endswith(TEXT_TYPES):
        raise ValueError("Upload a text file (.txt, .md or .html). For a PDF, copy its text into the box instead.")
    raw = up.read(MAX_UPLOAD_BYTES + 1)
    if len(raw) > MAX_UPLOAD_BYTES:
        raise ValueError("That file is too large (2 MB at most).")
    text = raw.decode("utf-8", errors="replace")
    if name.endswith((".html", ".htm")):
        from ..fetch import _TextExtractor

        parser = _TextExtractor()
        parser.feed(text)
        text = parser.text()
    return text


@bp.post("/pipeline/upload")
@editor_required
def pipeline_upload():
    f = request.form
    try:
        a = jobs.upload_document(
            get_settings(), topic_id=f.get("topic", ""), title=f.get("title", ""), text=_upload_text(),
            publisher=f.get("publisher", ""), url=f.get("url", ""), license_name=f.get("license", ""),
            permitted_use=f.get("permitted_use", "<verify>"), publication_date=f.get("date", ""),
            uploaded_by=remember_name(f.get("name", "")))
    except ValueError as e:
        flash(str(e), "error")
    else:
        flash(f"Added '{a.meta['title']}' to the article inbox for {a.topic_id} ({a.pmcid}). Job 2 uses it when the "
              f"topic has enough new articles.", "success")
    return redirect(url_for("ko.pipeline_page", tab="upload"))


@bp.post("/pipeline/add-topic")
@editor_required
def pipeline_add_topic():
    s = get_settings()
    item = next((i for i in jobs.suggested_topics(s) if i["term"] == request.form.get("term")), None)
    if item is None:
        flash("That suggestion is no longer there.", "error")
    else:
        try:
            c = reg.add_concept(s.registry_path, item["term"], item["ko_type"], item["specialty"], [])
            flash(f"Added {c.ko_id} {c.preferred_term}. Job 1 will look for articles about it.", "success")
        except ValueError as e:
            flash(str(e), "error")
    return redirect(url_for("ko.pipeline_page", tab="suggested"))


# ---------------------------------------------------------------- review queue

def _library_drafts(s) -> list:
    floor = STATUS_RANK.index("team_checked")
    out = []
    for e in LocalKOStore(s).list_entries():
        if e.doc is None:
            continue
        status = str(as_dict(e.doc.front.get("review")).get("status", "draft"))
        if status in STATUS_RANK and STATUS_RANK.index(status) < floor:
            out.append(e)
    return sorted(out, key=lambda e: e.ko_id)


def _detail(text: str, notes: dict, pack: str | None, registry) -> dict:
    result = validate_text(text, registry)
    try:
        doc = parse_ko(text)
    except KOFormatError as e:
        return {"error": str(e), "errors": [i.message for i in result.errors], "warnings": []}
    f = doc.front
    return {"doc": doc, "title": f.get("title", doc.ko_id), "summary": re.sub(r"\s*\[S\d+\]", "", str(f.get("summary") or "")),
            "body": md(smaller_headings(doc.body)), "sources": [x for x in as_list(f.get("sources")) if isinstance(x, dict)],
            "open_issues": [str(i) for i in as_list(as_dict(f.get("review")).get("open_issues"))],
            "errors": [i.message for i in result.errors], "warnings": [i.message for i in result.warnings],
            "notes": notes, "pack": pack}


@bp.get("/review")
def review_page():
    s = get_settings()
    store = PipelineStore(s)
    registry = reg.load_registry(s.registry_path)
    items = store.queue_items()
    drafts = _library_drafts(s)
    from . import data_views

    batches = data_views.pending_batches(s)
    tab = request.args.get("tab") or ("queue" if items or not (drafts or batches) else "library" if drafts else "data")
    selected = request.args.get("ko", "")
    detail = None
    if tab == "queue" and items:
        item = next((i for i in items if i.ko_id == selected), items[0])
        selected = item.ko_id
        detail = _detail(item.text, item.notes, store.source_pack(item.ko_id), registry) | {"ko_id": item.ko_id,
                                                                                            "mode": "queue",
                                                                                            "text": item.text}
    elif tab == "library" and drafts:
        entry = next((e for e in drafts if e.ko_id == selected), drafts[0])
        selected = entry.ko_id
        pack_path = s.packs_dir / f"SP-{entry.ko_id}.md"
        text = entry.path.read_text(encoding="utf-8")
        detail = _detail(text, {}, pack_path.read_text(encoding="utf-8") if pack_path.is_file() else None,
                         registry) | {"ko_id": entry.ko_id, "mode": "library", "text": text}
    return render_template("ko/review.html", active="review", tab=tab, items=items, drafts=drafts, batches=batches,
                           selected=selected, detail=detail, decisions=store.decisions(25), name=reviewer_name(),
                           data_detail=data_views.batch_detail(s, request.args.get("batch")) if tab == "data" else None)


@bp.post("/review/<ko_id>/save")
@editor_required
def review_save(ko_id: str):
    store = PipelineStore(get_settings())
    if not store.in_queue(ko_id):
        abort(404)
    store.update_queue_text(ko_id, request.form.get("text", ""))
    flash(f"Saved your changes to {ko_id}. It is still waiting for a decision.", "success")
    return redirect(url_for("ko.review_page", ko=ko_id))


@bp.post("/review/<ko_id>/accept")
@editor_required
def review_accept(ko_id: str):
    s = get_settings()
    name = remember_name(request.form.get("name", ""))
    mode = request.form.get("mode", "queue")
    try:
        if mode == "library":
            path = jobs.accept_library_ko(s, ko_id, name)
        else:
            if not PipelineStore(s).in_queue(ko_id):
                abort(404)
            path = jobs.accept_ko(s, ko_id, name, markdown=request.form.get("text") or None)
    except (ValueError, KOFormatError) as e:
        flash(f"Not accepted: {e}", "error")
        return redirect(url_for("ko.review_page", tab=mode if mode == "library" else "queue", ko=ko_id))
    flash(f"Accepted {ko_id} as team checked by {name}. It is in the KO Library ({path}).", "success")
    return redirect(url_for("ko.review_page", tab=mode if mode == "library" else "queue"))


@bp.post("/review/<ko_id>/reject")
@editor_required
def review_reject(ko_id: str):
    s = get_settings()
    store = PipelineStore(s)
    reason = " ".join(request.form.get("reason", "").split())
    if not store.in_queue(ko_id):
        abort(404)
    if not reason:
        flash("Say why you reject it (it helps improve the pipeline).", "error")
        return redirect(url_for("ko.review_page", ko=ko_id))
    store.reject(ko_id, remember_name(request.form.get("name", "")) or "unknown", reason)
    flash(f"Rejected {ko_id}. A copy and your reason are kept in data/pipeline/rejected/.", "success")
    return redirect(url_for("ko.review_page"))


def queue_count() -> int:
    try:
        s = get_settings()
        from . import data_views

        return len(PipelineStore(s).queue_items()) + len(data_views.pending_batches(s))
    except Exception:
        return 0


__all__ = ["queue_count", "can_edit", "html", "json", "validate_doc"]
