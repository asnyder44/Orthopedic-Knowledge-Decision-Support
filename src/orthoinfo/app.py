"""Step 8: the end-to-end workflow as a small web app.

ask a question -> see understandable sections from reviewed sources -> check the
source (link, publisher, date) -> collect questions to take to an appointment.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import uuid

from flask import Flask, abort, render_template, request

from .config import LOG_DIR, PROCESSED_DIR, load_appointment_questions, load_scope, load_search_config
from .dataset import load_dataset
from .safety import EMERGENCY_NOTICE, SCOPE_NOTICE, needs_scope_notice
from .search import build_retriever
from .text import html_to_lines


def create_app(method: str | None = None, version: str | None = None) -> Flask:
    app = Flask(__name__)
    cfg = load_search_config()
    scope = load_scope()
    appt = load_appointment_questions()
    method = method or os.environ.get("ORTHOINFO_METHOD") or cfg["default_method"]
    version, documents, chunks = load_dataset(version)
    docs = {d["doc_id"]: d for d in documents}
    retriever = build_retriever(method, chunks, cfg["semantic_model"], PROCESSED_DIR / version)
    threshold = cfg["abstain_threshold"][method]
    log_queries = os.environ.get("ORTHOINFO_LOG_QUERIES") == "1"

    common = {"scope": scope, "version": version, "method": method,
              "emergency_notice": EMERGENCY_NOTICE, "appt_reviewed": bool(appt.get("reviewed_by"))}

    @app.get("/")
    def home():
        return render_template("index.html", **common, topics=documents)

    @app.get("/search")
    def search():
        query = request.args.get("q", "").strip()
        if not query:
            return home()
        result = retriever.search(query, k=10)
        abstain = result.confidence < threshold
        groups = [] if abstain else [
            {"doc": docs[doc_id], "hits": hits[:2]} for doc_id, hits in result.by_document()[:4]
        ]
        top_doc = groups[0]["doc"]["doc_id"] if groups else None
        questions = list(appt.get("general", []))
        if top_doc:
            questions = appt.get("topics", {}).get(top_doc, {}).get("questions", []) + questions

        if log_queries:
            _log(query, method, result, abstain)
        return render_template(
            "results.html", **common, query=query, groups=groups, abstain=abstain,
            scope_notice=SCOPE_NOTICE if needs_scope_notice(query) else None,
            appointment_questions=questions,
        )

    @app.get("/topic/<doc_id>")
    def topic(doc_id: str):
        doc = docs.get(doc_id) or abort(404)
        return render_template("topic.html", **common, doc=doc, lines=html_to_lines(doc["summary_html"]))

    @app.get("/about")
    def about():
        return render_template("about.html", **common, topics=documents)

    return app


def _log(query: str, method: str, result, abstain: bool) -> None:
    """Append an anonymous query record for pilot analysis (enable with ORTHOINFO_LOG_QUERIES=1)."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    record = {
        "id": uuid.uuid4().hex,
        "time": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "method": method,
        "query": query,
        "confidence": round(result.confidence, 4),
        "abstained": abstain,
        "top_docs": result.ranked_doc_ids()[:3],
    }
    with (LOG_DIR / "queries.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record) + "\n")
