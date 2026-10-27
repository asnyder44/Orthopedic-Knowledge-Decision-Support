"""Shared question-answering service used by both the HTML library and the JSON API.

One place owns: dataset loading, the retriever, the abstain threshold, the scope guard
and the appointment questions, so the web pages and the OrthoBot API cannot drift apart.

Answers are *extractive*: passages from the collection with their sources. Nothing is
generated, so nothing can be said that is not in a cited source.
"""

from __future__ import annotations

import os
from collections import Counter
from dataclasses import dataclass, field

from .config import PROCESSED_DIR, load_appointment_questions, load_scope, load_search_config
from .dataset import load_dataset
from .safety import EMERGENCY_NOTICE, SCOPE_NOTICE, needs_scope_notice
from .search import SearchResult, build_retriever
from .sources import SOURCE_TYPES

TYPE_LABELS = {
    "patient_education": "Patient information",
    "encyclopedia": "Encyclopedia",
    "textbook": "Textbook",
    "research_article": "Research article",
}


@dataclass
class Answer:
    query: str
    widen: bool
    abstain: bool
    result: SearchResult
    groups: list[dict] = field(default_factory=list)  # [{"doc": dict, "hits": [Hit]}]
    scope_notice: str | None = None
    appointment_questions: list[str] = field(default_factory=list)


class OrthoService:
    def __init__(self, method: str | None = None, version: str | None = None):
        self.cfg = load_search_config()
        self.scope = load_scope()
        self.appt = load_appointment_questions()
        self.method = method or os.environ.get("ORTHOINFO_METHOD") or self.cfg["default_method"]
        version = version or os.environ.get("ORTHOINFO_DATASET_VERSION") or None
        self.version, self.documents, chunks = load_dataset(version)
        self.docs = {d["doc_id"]: d for d in self.documents}
        self.retriever = build_retriever(self.method, chunks, self.cfg["semantic_model"],
                                         PROCESSED_DIR / self.version)
        self.n_chunks = len(chunks)
        self.threshold = self.cfg["abstain_threshold"][self.method]
        self.default_types = self.cfg.get("default_source_types") or list(SOURCE_TYPES)
        self.type_counts = Counter(d["source_type"] for d in self.documents)
        self.exclude_headings = {h.strip().lower() for h in self.cfg.get("exclude_headings", [])}
        self.appt_reviewed = bool(self.appt.get("reviewed_by"))

    @property
    def extra_types_phrase(self) -> str:
        """e.g. 'textbooks' or 'textbooks and research articles': what 'search all' really adds."""
        names = [TYPE_LABELS[t].lower() + "s" for t in SOURCE_TYPES
                 if t not in self.default_types and self.type_counts.get(t)]
        return " and ".join([", ".join(names[:-1]), names[-1]] if len(names) > 1 else names)

    def ask(self, query: str, widen: bool = False, max_docs: int = 6, hits_per_doc: int = 2) -> Answer:
        result = self.retriever.search(query, k=20, source_types=None if widen else self.default_types)
        kept = [h for h in result.hits if h.chunk["heading"].strip().lower() not in self.exclude_headings]
        if len(kept) != len(result.hits):
            # Keep confidence meaningful: for BM25 it *is* the top hit's score, so recompute it
            # without the filtered-out chrome; other methods keep their own confidence.
            confidence = (kept[0].score if kept else 0.0) if self.method == "bm25" else result.confidence
            result = SearchResult(kept, confidence, result.timings)
        abstain = result.confidence < self.threshold
        groups = [] if abstain else [
            {"doc": self.docs[doc_id], "hits": hits[:hits_per_doc]}
            for doc_id, hits in result.by_document()[:max_docs]
        ]
        questions = list(self.appt.get("general", []))
        if groups:
            topic_qs = self.appt.get("topics", {}).get(groups[0]["doc"]["doc_id"], {}).get("questions", [])
            questions = topic_qs + questions
        return Answer(query, widen, abstain, result, groups,
                      SCOPE_NOTICE if needs_scope_notice(query) else None, questions)

    # ----- serialisation for the JSON API -------------------------------------------------
    def source_info(self, doc: dict) -> dict:
        return {
            "doc_id": doc["doc_id"],
            "title": doc["title"],
            "url": doc["url"],
            "publisher": doc["publisher"],
            "container": doc.get("container") or doc["publisher"],
            "authors": doc.get("authors") or "",
            "source_type": doc["source_type"],
            "source_type_label": TYPE_LABELS.get(doc["source_type"], doc["source_type"]),
            "license": doc["license"].split(" — ")[0],
            "published": (doc.get("published") or "")[:4] or None,
            "last_updated": doc.get("last_updated"),
            "retrieved": (doc.get("retrieved") or "")[:10],
        }

    def to_api(self, ans: Answer) -> dict:
        return {
            "question": ans.query,
            "found": not ans.abstain,
            "passages": [
                {
                    "source": self.source_info(g["doc"]),
                    "sections": [
                        {"heading": h.chunk["heading"], "lines": h.chunk["text"].split("\n")}
                        for h in g["hits"]
                    ],
                }
                for g in ans.groups
            ],
            "scope_notice": ans.scope_notice,
            "emergency_notice": EMERGENCY_NOTICE,
            "appointment_questions": {"items": ans.appointment_questions, "reviewed": self.appt_reviewed},
            "meta": {
                "dataset_version": self.version,
                "method": self.method,
                "confidence": round(ans.result.confidence, 3),
                "all_sources": ans.widen,
            },
        }

    def info(self) -> dict:
        return {
            "dataset_version": self.version,
            "documents": len(self.documents),
            "chunks": self.n_chunks,
            "method": self.method,
            "default_source_types": self.default_types,
            "source_types_available": {
                t: {"label": TYPE_LABELS[t], "documents": n} for t, n in sorted(self.type_counts.items())
            },
        }
