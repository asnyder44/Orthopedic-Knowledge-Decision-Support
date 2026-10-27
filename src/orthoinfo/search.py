"""Step 7: the search methods being compared.

  bm25      keyword search (classic BM25 ranking, pure Python, no dependencies)
  semantic  meaning-based search with a sentence-embedding model (optional extra)
  hybrid    reciprocal-rank fusion of the two

Each retriever ranks *chunks* (pieces of a source) and reports a `confidence`
used to decide when the collection cannot support an answer. `source_types`
restricts a search to e.g. patient-education material.
"""

from __future__ import annotations

import hashlib
import heapq
import math
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from .text import tokenize

METHODS = ("bm25", "semantic", "hybrid")


@dataclass
class Hit:
    chunk: dict
    score: float


@dataclass
class SearchResult:
    hits: list[Hit]
    confidence: float
    timings: dict = field(default_factory=dict)

    def ranked_doc_ids(self) -> list[str]:
        """Source documents in rank order (each counted at its best chunk)."""
        return list(dict.fromkeys(hit.chunk["doc_id"] for hit in self.hits))

    def by_document(self) -> list[tuple[str, list[Hit]]]:
        groups: dict[str, list[Hit]] = {}
        for hit in self.hits:
            groups.setdefault(hit.chunk["doc_id"], []).append(hit)
        return list(groups.items())


def index_text(chunk: dict) -> str:
    return " ".join([chunk["title"], *(chunk.get("alt_titles") or []), chunk["heading"], chunk["text"]])


def _allowed(chunk: dict, source_types: Iterable[str] | None) -> bool:
    return not source_types or chunk.get("source_type") in source_types


class BM25Retriever:
    name = "bm25"

    def __init__(self, chunks: list[dict], k1: float = 1.5, b: float = 0.75):
        self.chunks, self.k1 = chunks, k1
        self.postings: dict[str, list[tuple[int, int]]] = defaultdict(list)
        lengths = []
        for i, chunk in enumerate(chunks):
            tokens = tokenize(index_text(chunk))
            lengths.append(len(tokens))
            for term, tf in Counter(tokens).items():
                self.postings[term].append((i, tf))
        avgdl = sum(lengths) / max(len(lengths), 1)
        # Per-chunk length normalisation, precomputed.
        self.norm = [k1 * (1 - b + b * n / avgdl) for n in lengths]
        n = len(chunks)
        self.idf = {t: math.log(1 + (n - len(p) + 0.5) / (len(p) + 0.5)) for t, p in self.postings.items()}

    def search(self, query: str, k: int = 10, source_types: Iterable[str] | None = None) -> SearchResult:
        scores: dict[int, float] = defaultdict(float)
        for term in tokenize(query):
            idf = self.idf.get(term)
            if idf is None:
                continue
            for i, tf in self.postings[term]:
                scores[i] += idf * tf * (self.k1 + 1) / (tf + self.norm[i])
        allowed = ((i, s) for i, s in scores.items() if _allowed(self.chunks[i], source_types))
        top = heapq.nlargest(k, allowed, key=lambda item: item[1])
        hits = [Hit(self.chunks[i], s) for i, s in top]
        return SearchResult(hits, hits[0].score if hits else 0.0)


class SemanticRetriever:
    name = "semantic"

    def __init__(self, chunks: list[dict], model_name: str, cache_dir: Path | None = None):
        try:
            import numpy as np
            from sentence_transformers import SentenceTransformer
        except ImportError as exc:  # pragma: no cover - depends on optional extra
            raise RuntimeError(
                "Semantic search needs the optional extra: pip install -e \".[semantic]\""
            ) from exc
        try:
            import truststore

            truststore.inject_into_ssl()
        except ImportError:  # pragma: no cover
            pass
        self.np = np
        self.chunks = chunks
        self.model = SentenceTransformer(model_name)
        texts = [index_text(c) for c in chunks]
        key = hashlib.sha256("\x1f".join([model_name, *texts]).encode()).hexdigest()[:16]
        cache = cache_dir / f"embeddings_{key}.npy" if cache_dir else None
        if cache and cache.exists():
            self.embeddings = np.load(cache)
        else:
            self.embeddings = self.model.encode(texts, normalize_embeddings=True, batch_size=64,
                                                show_progress_bar=len(texts) > 2000)
            if cache:
                np.save(cache, self.embeddings)
        self._types = np.array([c.get("source_type") or "" for c in chunks])

    def search(self, query: str, k: int = 10, source_types: Iterable[str] | None = None) -> SearchResult:
        qv = self.model.encode([query], normalize_embeddings=True)[0]
        scores = self.embeddings @ qv
        if source_types:
            scores = self.np.where(self.np.isin(self._types, list(source_types)), scores, -self.np.inf)
        order = self.np.argsort(-scores)[:k]
        hits = [Hit(self.chunks[i], float(scores[i])) for i in order if self.np.isfinite(scores[i])]
        return SearchResult(hits, hits[0].score if hits else 0.0)


class HybridRetriever:
    """Reciprocal-rank fusion: score = sum over methods of 1 / (rrf_k + rank)."""

    name = "hybrid"

    def __init__(self, keyword: BM25Retriever, semantic: SemanticRetriever, rrf_k: int = 60):
        self.keyword, self.semantic, self.rrf_k = keyword, semantic, rrf_k

    def search(self, query: str, k: int = 10, source_types: Iterable[str] | None = None,
               depth: int = 50) -> SearchResult:
        fused: dict[str, float] = {}
        chunk_by_id: dict[str, dict] = {}
        sem = self.semantic.search(query, depth, source_types)
        for result in (self.keyword.search(query, depth, source_types), sem):
            for rank, hit in enumerate(result.hits, start=1):
                cid = hit.chunk["chunk_id"]
                chunk_by_id[cid] = hit.chunk
                fused[cid] = fused.get(cid, 0.0) + 1 / (self.rrf_k + rank)
        order = sorted(fused, key=fused.get, reverse=True)[:k]
        # RRF scores are rank-based, so use semantic similarity to judge answerability.
        return SearchResult([Hit(chunk_by_id[c], fused[c]) for c in order], sem.confidence)


def build_retriever(method: str, chunks: list[dict], model_name: str, cache_dir: Path | None = None):
    if method == "bm25":
        return BM25Retriever(chunks)
    if method == "semantic":
        return SemanticRetriever(chunks, model_name, cache_dir)
    if method == "hybrid":
        return HybridRetriever(BM25Retriever(chunks), SemanticRetriever(chunks, model_name, cache_dir))
    raise ValueError(f"Unknown method {method!r}; choose from {METHODS}")
