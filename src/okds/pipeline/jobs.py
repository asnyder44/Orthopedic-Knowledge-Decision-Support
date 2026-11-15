"""The two scheduled jobs of the KO pipeline, plus review actions and topic suggestions.

Job 1 fetch_job:    topics without a KO -> search -> automatic checks -> article inbox (new / skipped)
Job 2 generate_job: topic with >= N new articles -> KO Generator (same prompt + rules) -> review queue
Review:             accept_ko (-> KO Library, team_checked) or store.reject (-> rejected/)

Runs on this computer now (CLI `okds pipeline ...` or the "Run now" buttons). Later each job becomes an
AWS Lambda function on an EventBridge Scheduler timer, with S3 for storage and Secrets Manager for the key.
"""

from __future__ import annotations

import datetime as dt
import re
import time
import uuid
from dataclasses import dataclass, field
from typing import Any

from .. import generator, llm, vocab
from .. import registry as reg
from ..config import Settings
from ..fetch import FetchError
from ..ko import as_dict, as_list, parse_ko, render_ko
from ..storage import LocalKOStore
from ..validator import validate_doc
from . import sources
from .store import Article, PipelineStore, mark_accepted, now_iso

PIPELINE_AUTHOR = "KO Pipeline"
# $ per million tokens (input, output), for the cost estimate in the run log.
PRICES = {"claude-sonnet-5-5": (2.0, 10.0), "claude-opus-5-5": (4.0, 20.0), "claude-haiku-5-5": (0.10, 0.50),
          "gpt-6.1-sol": (2.0, 10.0)}


@dataclass
class RunReport:
    job: str
    run_id: str = field(default_factory=lambda: uuid.uuid4().hex[:8])
    started: str = field(default_factory=now_iso)
    finished: str = ""
    status: str = "ok"  # ok | nothing to do | error
    counts: dict[str, int] = field(default_factory=dict)
    messages: list[str] = field(default_factory=list)
    usage: dict[str, Any] = field(default_factory=dict)
    est_cost_usd: float | None = None

    def add(self, key: str, n: int = 1) -> None:
        self.counts[key] = self.counts.get(key, 0) + n

    def to_dict(self) -> dict[str, Any]:
        return dict(self.__dict__)


def _library_ids(settings: Settings) -> set[str]:
    return {e.ko_id for e in LocalKOStore(settings).list_entries()}


# ---------------------------------------------------------------- Job 1: fetch

def fetchable_topics(settings: Settings, store: PipelineStore) -> list[reg.Concept]:
    """Topics Job 1 can work on: not retired, no KO in the library, and no KO waiting in the review queue."""
    library = _library_ids(settings)
    return [c for c in reg.load_registry(settings.registry_path).values()
            if c.status != "retired" and c.ko_id not in library and not store.in_queue(c.ko_id)]


def fetch_targets(settings: Settings, store: PipelineStore, topic_ids: list[str] | None = None) -> list[reg.Concept]:
    """Without topic_ids: topics with no KO yet that still need articles (up to OKDS_PIPELINE_TOPICS_PER_FETCH).
    With topic_ids (the operator chose them): those topics, if Job 1 can work on them."""
    topics = fetchable_topics(settings, store)
    if topic_ids:
        return [c for c in topics if c.ko_id in topic_ids]
    need = [c for c in topics if len(store.articles(c.ko_id, "new")) < settings.pipeline_min_articles]
    return need[: settings.pipeline_topics_per_fetch]


def fetch_job(settings: Settings, topic_ids: list[str] | None = None) -> RunReport:
    rep = RunReport("fetch")
    store = PipelineStore(settings)
    try:
        with store.lock():
            targets = fetch_targets(settings, store, topic_ids)
            if not targets:
                rep.status = "nothing to do"
                rep.messages.append("The chosen topics already have a KO or a KO in review." if topic_ids else
                                    "Every topic already has a KO, a KO in review, or enough new articles.")
            seen = store.seen_ids()
            for c in targets:
                _fetch_topic(settings, store, c, seen, rep)
    except Exception as e:  # report every failure in the run log
        rep.status = "error"
        rep.messages.append(f"{type(e).__name__}: {e}")
    rep.finished = now_iso()
    store.log_run(rep.to_dict())
    return rep


def _fetch_topic(settings: Settings, store: PipelineStore, c: reg.Concept, seen: set[str], rep: RunReport) -> None:
    terms = sources.topic_terms(c.preferred_term, c.alternate_terms)
    try:
        candidates = sources.search_europe_pmc(terms)
    except FetchError as e:
        rep.messages.append(f"{c.ko_id}: search failed ({e}).")
        rep.add("search errors")
        return
    rep.add("articles found", len(candidates))
    kept = len(store.articles(c.ko_id, "new"))
    # Reviews first, newest first (two stable sorts).
    ordered = sorted(candidates, key=lambda x: x.publication_date, reverse=True)
    ordered.sort(key=lambda x: not x.is_review)
    for cand in ordered:
        if kept >= settings.pipeline_articles_per_topic:
            break
        result = sources.check_candidate(cand, seen)
        meta = _article_meta(cand, c.ko_id, result)
        if not result.ok:
            if cand.pmcid not in seen:  # record the skip once, so people can see why
                store.save_article(Article({**meta, "status": "skipped", "skip_reason": result.reason}, ""))
                seen.add(cand.pmcid)
                rep.add("articles skipped")
            continue
        try:
            text, origin = sources.fetch_full_text(cand.pmcid, settings.pipeline_max_chars, settings.contact_email)
        except FetchError as e:
            meta["checks"]["has full text"] = "no full text available"
            store.save_article(Article({**meta, "status": "skipped", "skip_reason": "no full text available"}, ""))
            seen.add(cand.pmcid)
            rep.add("articles skipped")
            rep.messages.append(f"{cand.pmcid}: {e}")
            continue
        meta["checks"]["has full text"] = "pass"
        meta["full_text_from"] = origin
        store.save_article(Article({**meta, "status": "new"}, text))
        seen.add(cand.pmcid)
        kept += 1
        rep.add("articles saved")
        time.sleep(sources.NCBI_PAUSE)
    rep.messages.append(f"{c.ko_id} {c.preferred_term}: {kept} new article(s) in the inbox.")


def _article_meta(cand: sources.Candidate, topic_id: str, result: sources.CheckResult) -> dict[str, Any]:
    return {
        "article_id": cand.pmcid, "topic_id": topic_id, "title": cand.title, "journal": cand.journal,
        "doi": cand.doi, "url": cand.url, "publication_date": cand.publication_date, "license": cand.license,
        "permitted_use": sources.permitted_use(cand.license), "pub_types": cand.pub_types,
        "source_type": "systematic_review" if cand.is_review and any("systematic" in t.lower() for t in cand.pub_types)
        else "journal_article",
        "found_in": cand.source, "fetched_at": now_iso(), "checks": dict(result.checks),
    }


# ---------------------------------------------------------------- Job 2: generate

def generate_targets(settings: Settings, store: PipelineStore) -> list[tuple[reg.Concept, list[Article]]]:
    concepts = reg.load_registry(settings.registry_path)
    library = _library_ids(settings)
    out = []
    for c in concepts.values():
        if c.ko_id in library or store.in_queue(c.ko_id):
            continue
        new = store.articles(c.ko_id, "new")
        if len(new) >= max(2, settings.pipeline_min_articles):
            out.append((c, new[: settings.pipeline_articles_per_topic]))
    return out


def build_request(c: reg.Concept, articles: list[Article]) -> generator.KORequest:
    today = dt.date.today().isoformat()
    srcs = []
    for i, a in enumerate(articles, 1):
        m = a.meta
        uploaded = str(m.get("found_in", "")) == "upload"
        srcs.append({
            "id": f"S{i}", "title": m.get("title", ""),
            "publisher": (m.get("journal") or "Uploaded document") if uploaded
            else f"{m.get('journal') or 'Journal'} (via PubMed Central)",
            "url": m.get("url", ""), "source_type": m.get("source_type", "journal_article"), "audience": "clinician",
            "publication_date": m.get("publication_date") or "<verify>", "retrieved_date": today,
            "permitted_use": m.get("permitted_use", "open_license"),
            "notes": (f"Uploaded by {m.get('uploaded_by') or 'a team member'} ({m.get('article_id')}). "
                      f"License: {m.get('license') or 'not stated'}." if uploaded else
                      f"License: {str(m.get('license', '')).upper()}. DOI: {m.get('doi') or 'none'}. "
                      f"{m.get('article_id')}. Fetched by the KO pipeline."),
            "text": a.text,
        })
    return generator.KORequest(concept=c, audience=["patient", "caregiver", "student"], reading_level="grade 6-8",
                               difficulty="beginner", sources=srcs, author=PIPELINE_AUTHOR)


def _cost(model: str, usage: dict[str, Any]) -> float | None:
    """Estimate in USD. Cache writes cost 1.25x the input price, cache reads 0.1x (Claude prompt caching)."""
    price = PRICES.get(model)
    if not price or not (usage.get("input_tokens") or usage.get("output_tokens")):
        return None
    tokens_in = ((usage.get("input_tokens") or 0) + 1.25 * (usage.get("cache_creation_input_tokens") or 0)
                 + 0.1 * (usage.get("cache_read_input_tokens") or 0))
    return round(tokens_in / 1e6 * price[0] + (usage.get("output_tokens") or 0) / 1e6 * price[1], 4)


def generate_job(settings: Settings, max_kos: int | None = None, template: bool = False) -> RunReport:
    """template=True (or no AI key with template allowed): put an empty-template draft with the article
    sources in the review queue, for a person to write. No AI cost."""
    rep = RunReport("generate")
    store = PipelineStore(settings)
    limit = settings.pipeline_kos_per_run if max_kos is None else max_kos
    try:
        with store.lock():
            targets = generate_targets(settings, store)[:limit]
            if template and targets:
                registry = reg.load_registry(settings.registry_path)
                for c, articles in targets:
                    _template_one(settings, store, registry, c, articles, rep)
            elif not settings.ai_ready and not template:
                rep.status = "error"
                rep.messages.append("AI is off. Add a Claude or OpenAI API key to .env, or make template drafts "
                                    "(a person writes them), then run again.")
            elif not targets:
                rep.status = "nothing to do"
                rep.messages.append(f"No topic has {settings.pipeline_min_articles}+ new articles yet. Run Job 1 first.")
            else:
                registry = reg.load_registry(settings.registry_path)
                for c, articles in targets:
                    _generate_one(settings, store, registry, c, articles, rep)
    except Exception as e:
        rep.status = "error"
        rep.messages.append(f"{type(e).__name__}: {e}")
    rep.finished = now_iso()
    if template:
        rep.job = "generate (template)"
    rep.est_cost_usd = _cost(settings.ai_model, rep.usage)
    store.log_run(rep.to_dict())
    return rep


def _generate_one(settings: Settings, store: PipelineStore, registry: dict[str, reg.Concept], c: reg.Concept,
                  articles: list[Article], rep: RunReport) -> None:
    req = build_request(c, articles)
    result = llm.StreamResult()
    try:
        for _ in generator.ai_draft_stream(req, registry, settings.ai_model, settings.generator_effort, result,
                                           provider=settings.ai_provider):
            pass
    except llm.LLMError as e:
        rep.status = "error"
        rep.messages.append(f"{c.ko_id}: the AI failed ({e}).")
        return
    for k in ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"):
        rep.usage[k] = (rep.usage.get(k) or 0) + (result.usage.get(k) or 0)
    md, notes = generator.finalize(result.text, req, settings.ai_model)
    if md.startswith(generator.SOURCE_PACK_NEEDED):
        store.mark_articles(articles, "skipped", skip_reason="the AI said these articles are not enough for a KO")
        rep.add("KOs not made")
        rep.messages.append(f"{c.ko_id}: the AI said the articles are not enough ({md.splitlines()[1:2]}).")
        return
    try:
        doc = parse_ko(md)
    except Exception as e:
        rep.add("KOs not made")
        rep.messages.append(f"{c.ko_id}: the draft could not be read ({e}); articles kept as new.")
        return
    front = dict(doc.front)
    review = dict(as_dict(front.get("review")))
    review["author"] = PIPELINE_AUTHOR
    front["review"] = review
    for entry in as_list(front.get("change_log")):
        if isinstance(entry, dict):
            entry["by"] = PIPELINE_AUTHOR
            entry["change"] = f"Drafted by the KO pipeline from {', '.join(a.pmcid for a in articles)} ({settings.ai_model})."
    doc = type(doc)(front=front, body=doc.body)
    check = validate_doc(doc, registry)
    store.add_to_queue(c.ko_id, render_ko(doc), generator.render_source_pack(req), {
        "created": now_iso(), "run_id": rep.run_id, "model": settings.ai_model, "articles": [a.pmcid for a in articles],
        "generator_notes": notes, "problems": [i.message for i in check.errors],
        "to_double_check": [i.message for i in check.warnings], "usage": result.usage,
    })
    store.mark_articles(articles, "used", used_in=c.ko_id)
    rep.add("KOs in review queue")
    rep.messages.append(f"{c.ko_id} {c.preferred_term}: draft is in the review queue "
                        f"({len(check.errors)} problem(s), {len(check.warnings)} to double-check).")


def _template_one(settings: Settings, store: PipelineStore, registry: dict[str, reg.Concept], c: reg.Concept,
                  articles: list[Article], rep: RunReport) -> None:
    req = build_request(c, articles)
    md = generator.template_draft(req)
    check = validate_doc(parse_ko(md), registry)
    store.add_to_queue(c.ko_id, md, generator.render_source_pack(req), {
        "created": now_iso(), "run_id": rep.run_id, "model": "template (no AI)", "articles": [a.pmcid for a in articles],
        "generator_notes": ["Empty template with the article sources. A person writes it in the Review queue."],
        "problems": [i.message for i in check.errors], "to_double_check": [i.message for i in check.warnings],
    })
    store.mark_articles(articles, "used", used_in=c.ko_id)
    rep.add("KOs in review queue")
    rep.messages.append(f"{c.ko_id} {c.preferred_term}: a template draft is in the review queue (no AI).")


# ---------------------------------------------------------------- uploaded documents

MIN_UPLOAD_CHARS = 500


def upload_document(settings: Settings, *, topic_id: str, title: str, text: str, publisher: str = "", url: str = "",
                    license_name: str = "", permitted_use: str = "<verify>", publication_date: str = "",
                    uploaded_by: str = "") -> Article:
    """A document a person adds (partner report, guideline, article): it joins the article inbox after the
    same kind of automatic checks Job 1 runs. Raises ValueError with a plain reason when a check fails."""
    import hashlib

    store = PipelineStore(settings)
    concept = reg.load_registry(settings.registry_path).get(topic_id)
    text = (text or "").replace("\r\n", "\n").strip()[: settings.pipeline_max_chars]
    checks = {
        "topic exists": "pass" if concept else f"{topic_id} is not in KO Topics",
        "has a title": "pass" if title.strip() else "add a title",
        "has text": "pass" if len(text) >= MIN_UPLOAD_CHARS else f"only {len(text)} characters (need {MIN_UPLOAD_CHARS}+)",
        "reuse allowed": ("pass" if permitted_use in vocab.enum("permitted_use") and permitted_use != "restricted"
                          else "the reuse rules say it can't be used (restricted)"),
    }
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
    doc_id = f"UP-{digest}"
    checks["not added before"] = "pass" if doc_id not in store.seen_ids() else "this text is already in the inbox"
    failed = [f"{k}: {v}" for k, v in checks.items() if v != "pass"]
    if failed:
        raise ValueError("Not added. " + "; ".join(failed))
    meta = {"article_id": doc_id, "topic_id": topic_id, "title": title.strip(), "journal": publisher.strip(),
            "doi": "", "url": url.strip(), "publication_date": publication_date.strip() or "<verify>",
            "license": license_name.strip(), "permitted_use": permitted_use, "pub_types": ["uploaded document"],
            "source_type": "other", "found_in": "upload", "uploaded_by": uploaded_by.strip(), "fetched_at": now_iso(),
            "checks": checks, "status": "new"}
    article = Article(meta, text)
    store.save_article(article)
    store.log_decision({"ko_id": topic_id, "decision": "document uploaded", "reviewer": uploaded_by.strip(),
                        "file": f"articles/{topic_id}/{doc_id}.md"})
    return article


# ---------------------------------------------------------------- review actions

def accept_ko(settings: Settings, ko_id: str, reviewer: str, markdown: str | None = None) -> str:
    """Move a reviewed KO into the library. Returns the library path. Raises ValueError with a reason."""
    if not reviewer.strip():
        raise ValueError("Type your name first.")
    store = PipelineStore(settings)
    text = markdown if markdown is not None else (store.queue_dir / f"{ko_id}.md").read_text(encoding="utf-8")
    doc = mark_accepted(parse_ko(text), reviewer.strip())
    result = validate_doc(doc, reg.load_registry(settings.registry_path))
    if result.errors:
        raise ValueError(f"Fix {len(result.errors)} problem(s) first: {result.errors[0].message}")
    saved = LocalKOStore(settings).save(doc, source_pack=store.source_pack(ko_id))
    reg.set_status(settings.registry_path, ko_id, "drafted")
    store.log_decision({"ko_id": ko_id, "decision": "accepted", "reviewer": reviewer.strip(), "file": saved.markdown_path})
    store.remove_from_queue(ko_id)
    return saved.markdown_path


def accept_library_ko(settings: Settings, ko_id: str, reviewer: str) -> str:
    """A draft that is already in the KO Library (made outside the pipeline) gets the same people check."""
    if not reviewer.strip():
        raise ValueError("Type your name first.")
    entry = next((e for e in LocalKOStore(settings).list_entries() if e.ko_id == ko_id and e.doc is not None), None)
    if entry is None:
        raise ValueError(f"{ko_id} is not in the KO Library.")
    doc = mark_accepted(entry.doc, reviewer.strip())
    result = validate_doc(doc, reg.load_registry(settings.registry_path))
    if result.errors:
        raise ValueError(f"Fix {len(result.errors)} problem(s) first: {result.errors[0].message}")
    saved = LocalKOStore(settings).save(doc)
    PipelineStore(settings).log_decision({"ko_id": ko_id, "decision": "accepted (library draft)",
                                          "reviewer": reviewer.strip(), "file": saved.markdown_path})
    return saved.markdown_path


# ---------------------------------------------------------------- suggested topics

def suggested_topics(settings: Settings) -> list[dict[str, Any]]:
    """New topics that KOs point to (their proposed_concepts) and that are not in KO Topics yet."""
    concepts = reg.load_registry(settings.registry_path)
    known = {c.preferred_term.lower() for c in concepts.values()}
    known |= {t.lower() for c in concepts.values() for t in c.alternate_terms}
    docs = [e.doc for e in LocalKOStore(settings).list_entries() if e.doc is not None]
    docs += [i.doc for i in PipelineStore(settings).queue_items() if i.doc is not None]
    found: dict[str, dict[str, Any]] = {}
    for d in docs:
        for pc in as_list(d.front.get("proposed_concepts")):
            if not isinstance(pc, dict) or not pc.get("term"):
                continue
            term = str(pc["term"]).strip()
            key = re.sub(r"\s*\(.*?\)\s*", " ", term).strip().lower()  # "BCTQ (Boston ...)" ~ "BCTQ"
            if key in known or term.lower() in known or str(pc.get("suggested_type")) not in vocab.ko_types():
                continue
            item = found.setdefault(key, {"term": term, "ko_type": pc.get("suggested_type"),
                                          "specialty": d.front.get("specialty", "HAND"), "from": [],
                                          "reason": pc.get("reason", "")})
            if d.ko_id not in item["from"]:
                item["from"].append(d.ko_id)
    return sorted(found.values(), key=lambda x: (-len(x["from"]), x["term"].lower()))
