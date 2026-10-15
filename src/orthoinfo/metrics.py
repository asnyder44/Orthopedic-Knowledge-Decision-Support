"""Ranking metrics computed over source documents (binary relevance)."""

from __future__ import annotations

import math
import statistics


def hit_at_k(ranked: list[str], relevant: set[str], k: int) -> float:
    return float(any(d in relevant for d in ranked[:k]))


def recall_at_k(ranked: list[str], relevant: set[str], k: int) -> float:
    if not relevant:
        return 0.0
    return len(relevant.intersection(ranked[:k])) / len(relevant)


def reciprocal_rank(ranked: list[str], relevant: set[str], k: int = 10) -> float:
    for i, d in enumerate(ranked[:k], start=1):
        if d in relevant:
            return 1.0 / i
    return 0.0


def ndcg_at_k(ranked: list[str], relevant: set[str], k: int) -> float:
    dcg = sum(1 / math.log2(i + 1) for i, d in enumerate(ranked[:k], start=1) if d in relevant)
    ideal = sum(1 / math.log2(i + 1) for i in range(1, min(len(relevant), k) + 1))
    return dcg / ideal if ideal else 0.0


def mean(values: list[float]) -> float:
    return statistics.fmean(values) if values else float("nan")


def percentile(values: list[float], pct: float) -> float:
    if not values:
        return float("nan")
    ordered = sorted(values)
    return ordered[min(len(ordered) - 1, round(pct / 100 * (len(ordered) - 1)))]


def best_threshold(answerable: list[float], unanswerable: list[float]) -> tuple[float, float]:
    """Confidence threshold maximising balanced accuracy of the abstain decision.

    Returns (threshold, balanced_accuracy). Below threshold => abstain.
    """
    if not answerable or not unanswerable:
        return float("nan"), float("nan")
    candidates = sorted(set(answerable + unanswerable))
    best = (candidates[0], 0.0)
    for t in candidates:
        tpr = sum(c >= t for c in answerable) / len(answerable)
        tnr = sum(c < t for c in unanswerable) / len(unanswerable)
        if (tpr + tnr) / 2 > best[1]:
            best = (t, (tpr + tnr) / 2)
    return best
