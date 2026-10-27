import math

from orthoinfo import metrics as M
from orthoinfo.questions import validate
from orthoinfo.safety import needs_scope_notice
from orthoinfo.search import BM25Retriever


def chunk(doc_id, i, title, text, heading="About"):
    return {"chunk_id": f"{doc_id}#{i}", "doc_id": doc_id, "title": title, "alt_titles": [],
            "heading": heading, "text": text}


CHUNKS = [
    chunk("cts", 0, "Carpal Tunnel Syndrome", "Numbness and tingling in the fingers at night."),
    chunk("cts", 1, "Carpal Tunnel Syndrome", "Treatments include wrist splints.", "Treatments"),
    chunk("elbow", 0, "Elbow Injuries", "Tennis elbow is tendinitis of the elbow."),
    chunk("fx", 0, "Fractures", "A fracture is a broken bone. Casts help bones heal."),
]


def test_bm25_ranks_matching_document_first():
    result = BM25Retriever(CHUNKS).search("numb tingling fingers at night")
    assert result.ranked_doc_ids()[0] == "cts"
    assert result.confidence > 0


def test_bm25_returns_nothing_for_unrelated_query():
    result = BM25Retriever(CHUNKS).search("vaccines for travel")
    assert result.hits == [] and result.confidence == 0.0


def test_ranked_doc_ids_deduplicates_chunks():
    result = BM25Retriever(CHUNKS).search("carpal tunnel splints")
    ids = result.ranked_doc_ids()
    assert ids[0] == "cts" and len(ids) == len(set(ids))


def test_metrics():
    ranked, rel = ["a", "b", "c"], {"b", "z"}
    assert M.hit_at_k(ranked, rel, 1) == 0.0
    assert M.recall_at_k(ranked, rel, 3) == 0.5
    assert M.reciprocal_rank(ranked, rel) == 0.5
    expected = (1 / math.log2(3)) / (1 + 1 / math.log2(3))
    assert math.isclose(M.ndcg_at_k(ranked, rel, 3), expected)


def test_best_threshold_separates_scores():
    threshold, acc = M.best_threshold([5.0, 7.0, 9.0], [1.0, 2.0])
    assert 2.0 < threshold <= 5.0 and acc == 1.0


def test_scope_guard():
    assert needs_scope_notice("Should I stop taking ibuprofen?")
    assert needs_scope_notice("Do I have carpal tunnel?")
    assert not needs_scope_notice("What is carpal tunnel syndrome?")


def test_validate_flags_problems():
    good = {"id": "q1", "question": "x", "category": "lay", "relevant_doc_ids": ["cts"],
            "must_include": [], "split": "dev", "source": "interview", "status": "draft"}
    bad = good | {"id": "q2", "relevant_doc_ids": ["missing"], "split": "train"}
    problems, summary = validate([good, bad], {"cts"})
    assert summary["total"] == 2
    assert any("q2" in p and "split" in p for p in problems)
    assert any("q2" in p and "missing" in p for p in problems)
    assert not any(p.startswith("q1") for p in problems)
