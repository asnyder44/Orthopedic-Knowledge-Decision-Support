"""The integrated web app.

  /                 the Exclusive Orthopedics Hub website (index.html at the project root)
  /library          Anna's search UI (topic browser, search results, source pages)
  /search /doc/... /about    library pages (unchanged behaviour)
  POST /api/ask     OrthoBot endpoint used by the website's "Ask an OrthoBot" section
  GET  /api/health  liveness + dataset info (use for deploy health checks)
  GET  /api/info    dataset info for the front end (which source types exist)

Environment variables (all optional): see .env.example.
"""

from __future__ import annotations

import datetime as dt
import json
import logging
import os
import threading
import time
import uuid
from collections import Counter, defaultdict, deque

from flask import Flask, abort, jsonify, make_response, render_template, request, send_file
from werkzeug.exceptions import HTTPException

from .config import LOG_DIR, ROOT
from .safety import EMERGENCY_NOTICE
from .service import TYPE_LABELS, OrthoService

log = logging.getLogger("orthoinfo")

MAX_QUESTION_CHARS = 500
CSP = ("default-src 'self'; img-src 'self' https: data:; style-src 'self' 'unsafe-inline'; "
       "script-src 'self' 'unsafe-inline'; connect-src 'self'; base-uri 'self'; "
       "form-action 'self'; frame-ancestors 'none'")


class RateLimiter:
    """Per-process sliding-window limiter (requests per minute per client IP)."""

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
            if len(self._hits) > 10_000:  # bound memory under address-spraying
                for k in [k for k, v in self._hits.items() if not v or now - v[-1] > 60]:
                    del self._hits[k]
            if len(q) >= self.per_minute:
                return False
            q.append(now)
            return True


def create_app(method: str | None = None, version: str | None = None) -> Flask:
    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024
    if os.environ.get("ORTHOINFO_TRUST_PROXY") == "1":  # behind nginx / a PaaS router
        from werkzeug.middleware.proxy_fix import ProxyFix

        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

    svc = OrthoService(method, version)
    limiter = RateLimiter(int(os.environ.get("ORTHOINFO_RATE_LIMIT", "30")))
    log_queries = os.environ.get("ORTHOINFO_LOG_QUERIES") == "1"
    cors = [o.strip() for o in os.environ.get("ORTHOINFO_CORS_ORIGINS", "").split(",") if o.strip()]
    site_file = ROOT / "index.html"

    common = {"scope": svc.scope, "version": svc.version, "method": svc.method,
              "type_labels": TYPE_LABELS, "emergency_notice": EMERGENCY_NOTICE,
              "appt_reviewed": svc.appt_reviewed,
              "extra_types": svc.extra_types_phrase}

    # ---------------------------------------------------------------- website
    @app.get("/")
    def site():
        if not site_file.exists():
            return home()
        resp = make_response(send_file(site_file, mimetype="text/html"))
        resp.headers["Cache-Control"] = "no-cache"
        return resp

    # ---------------------------------------------------------------- library (Anna's UI)
    @app.get("/library")
    def home():
        patient = sorted((d for d in svc.documents if d["source_type"] == "patient_education"),
                         key=lambda d: (d["role"] != "core", d["title"]))
        return render_template("index.html", **common, topics=patient, counts=svc.type_counts)

    @app.get("/search")
    def search():
        query = request.args.get("q", "").strip()[:MAX_QUESTION_CHARS]
        if not query:
            return home()
        widen = request.args.get("all") == "1"
        ans = svc.ask(query, widen=widen, max_docs=6)
        if log_queries:
            _log(query, svc.method, widen, ans.result, ans.abstain, "web")
        return render_template("results.html", **common, query=query, groups=ans.groups,
                               abstain=ans.abstain, widen=widen, scope_notice=ans.scope_notice,
                               appointment_questions=ans.appointment_questions)

    @app.get("/doc/<path:doc_id>")
    def document(doc_id: str):
        doc = svc.docs.get(doc_id) or abort(404)
        return render_template("topic.html", **common, doc=doc)

    @app.get("/about")
    def about():
        by_source = Counter((d["source"], d["source_type"], d["publisher"] if d["source"] != "europepmc"
                             else "Various journals (Europe PMC)", d["license"].split(" — ")[0])
                            for d in svc.documents)
        return render_template("about.html", **common, by_source=sorted(by_source.items()),
                               total=len(svc.documents), chunks=svc.n_chunks)

    # ---------------------------------------------------------------- OrthoBot API
    @app.route("/api/ask", methods=["POST", "OPTIONS"])
    def api_ask():
        if request.method == "OPTIONS":
            return "", 204
        if not limiter.allow(request.remote_addr or "unknown"):
            return _error(429, "Too many questions in a short time. Please wait a minute and try again.")
        body = request.get_json(silent=True)
        if not isinstance(body, dict):
            return _error(400, "Send a JSON object like {\"question\": \"...\"}.")
        question = body.get("question")
        if not isinstance(question, str) or not question.strip():
            return _error(400, "Please type a question.")
        question = " ".join(question.split())
        if len(question) > MAX_QUESTION_CHARS:
            return _error(400, f"Please keep your question under {MAX_QUESTION_CHARS} characters.")
        widen = body.get("all_sources") is True
        ans = svc.ask(question, widen=widen, max_docs=3)
        if log_queries:
            _log(question, svc.method, widen, ans.result, ans.abstain, "api")
        return jsonify(svc.to_api(ans))

    @app.get("/api/health")
    def api_health():
        return jsonify({"status": "ok", **svc.info()})

    @app.get("/api/info")
    def api_info():
        return jsonify(svc.info())

    # ---------------------------------------------------------------- cross-cutting
    def _error(status: int, message: str):
        resp = jsonify({"error": message})
        resp.status_code = status
        return resp

    @app.errorhandler(HTTPException)
    def http_error(exc: HTTPException):
        if request.path.startswith("/api/"):
            return _error(exc.code or 500, exc.description or exc.name)
        return exc

    @app.errorhandler(Exception)
    def unexpected(exc: Exception):
        log.exception("unhandled error on %s", request.path)
        if request.path.startswith("/api/"):
            return _error(500, "Something went wrong on our side. Please try again.")
        return make_response("Something went wrong. Please try again.", 500)

    @app.after_request
    def headers(resp):
        resp.headers.setdefault("X-Content-Type-Options", "nosniff")
        resp.headers.setdefault("X-Frame-Options", "DENY")
        resp.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        resp.headers.setdefault("Content-Security-Policy", CSP)
        if request.path.startswith("/api/"):
            resp.headers["Cache-Control"] = "no-store"
            origin = request.headers.get("Origin")
            if origin and ("*" in cors or origin in cors):
                resp.headers["Access-Control-Allow-Origin"] = "*" if "*" in cors else origin
                resp.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
                resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
                resp.headers["Vary"] = "Origin"
        return resp

    return app


def _log(query: str, method: str, widen: bool, result, abstain: bool, channel: str) -> None:
    """Append an anonymous query record for pilot analysis (enable with ORTHOINFO_LOG_QUERIES=1)."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    record = {
        "id": uuid.uuid4().hex,
        "time": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "channel": channel,
        "method": method,
        "all_sources": widen,
        "query": query,
        "confidence": round(result.confidence, 4),
        "abstained": abstain,
        "top_docs": result.ranked_doc_ids()[:3],
    }
    with (LOG_DIR / "queries.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record) + "\n")
