"""Step 7: the search methods being compared.

  bm25      keyword search (classic BM25 ranking, pure Python, no dependencies)
  semantic  meaning-based search with a sentence-embedding model (optional extra)
  hybrid    reciprocal-rank fusion of the two

Each retriever ranks *chunks* (sections of a source) and reports a `confidence`
used to decide when the collection cannot support an answer.
"""

from __future__ import annotations

import hashlib
import math
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

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
        seen: list[str] = []
        for hit in self.hits:
            if hit.chunk["doc_id"] not in seen:
                seen.append(hit.chunk["doc_id"])
        return seen

    def by_document(self) -> list[tuple[str, list[Hit]]]:
        groups: dict[str, list[Hit]] = {}
        for hit in self.hits:
            groups.setdefault(hit.chunk["doc_id"], []).append(hit)
        return list(groups.items())


def index_text(chunk: dict) -> str:
    return " ".join([chunk["title"], *chunk.get("alt_titles", []), chunk["heading"], chunk["text"]])


class BM25Retriever:
    name = "bm25"

    def __init__(self, chunks: list[dict], k1: float = 1.5, b: float = 0.75):
        self.chunks, self.k1, self.b = chunks, k1, b
        docs = [tokenize(index_text(c)) for c in chunks]
        self.tfs = [Counter(d) for d in docs]
        self.lengths = [len(d) for d in docs]
        self.avgdl = sum(self.lengths) / max(len(docs), 1)
        df = Counter(t for d in docs for t in set(d))
        n = len(docs)
        self.idf = {t: math.log(1 + (n - f + 0.5) / (f + 0.5)) for t, f in df.items()}

    def score(self, query: str) -> list[float]:
        terms = tokenize(query)
        scores = []
        for tf, dl in zip(self.tfs, self.lengths):
            norm = self.k1 * (1 - self.b + self.b * dl / self.avgdl)
            scores.append(
                sum(self.idf[t] * tf[t] * (self.k1 + 1) / (tf[t] + norm) for t in terms if t in tf)
            )
        return scores

    def search(self, query: str, k: int = 10) -> SearchResult:
        scores = self.score(query)
        order = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        hits = [Hit(self.chunks[i], scores[i]) for i in order[:k] if scores[i] > 0]
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
            self.embeddings = self.model.encode(texts, normalize_embeddings=True, batch_size=32)
            if cache:
                np.save(cache, self.embeddings)

    def search(self, query: str, k: int = 10) -> SearchResult:
        qv = self.model.encode([query], normalize_embeddings=True)[0]
        scores = self.embeddings @ qv
        order = self.np.argsort(-scores)[:k]
        hits = [Hit(self.chunks[i], float(scores[i])) for i in order]
        return SearchResult(hits, hits[0].score if hits else 0.0)


class HybridRetriever:
    """Reciprocal-rank fusion: score = sum over methods of 1 / (rrf_k + rank)."""

    name = "hybrid"

    def __init__(self, keyword: BM25Retriever, semantic: SemanticRetriever, rrf_k: int = 60):
        self.keyword, self.semantic, self.rrf_k = keyword, semantic, rrf_k

    def search(self, query: str, k: int = 10, depth: int = 50) -> SearchResult:
        fused: dict[str, float] = {}
        chunk_by_id: dict[str, dict] = {}
        sem = self.semantic.search(query, depth)
        for result in (self.keyword.search(query, depth), sem):
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
