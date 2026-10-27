"""Step 5: the evaluation question set (data/eval/questions.jsonl)."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from .config import EVAL_DIR
from .dataset import read_jsonl

QUESTIONS_FILE = EVAL_DIR / "questions.jsonl"
CATEGORIES = {"lay", "technical", "ambiguous", "unanswerable", "out_of_scope"}
SPLITS = {"dev", "test"}
SOURCES = {"interview", "source_material", "reviewer", "team_draft"}
STATUSES = {"draft", "reviewed"}
REQUIRED = ("id", "question", "category", "relevant_doc_ids", "must_include", "split", "source", "status")

# Categories where the right behaviour is "the collection cannot answer this".
ABSTAIN_CATEGORIES = {"unanswerable"}


def load_questions(path: Path = QUESTIONS_FILE, split: str | None = None) -> list[dict]:
    rows = read_jsonl(path)
    return [q for q in rows if split in (None, "all") or q["split"] == split]


def is_answerable(q: dict) -> bool:
    return q["category"] not in ABSTAIN_CATEGORIES and q["category"] != "out_of_scope"


def validate(questions: list[dict], known_doc_ids: set[str]) -> tuple[list[str], dict]:
    """Return (problems, summary counts) for a question set."""
    problems: list[str] = []
    ids = Counter(q.get("id") for q in questions)
    problems += [f"duplicate id {i}" for i, n in ids.items() if n > 1]
    for q in questions:
        qid = q.get("id", "?")
        missing = [f for f in REQUIRED if f not in q]
        if missing:
            problems.append(f"{qid}: missing fields {missing}")
            continue
        for field, allowed in (("category", CATEGORIES), ("split", SPLITS),
                               ("source", SOURCES), ("status", STATUSES)):
            if q[field] not in allowed:
                problems.append(f"{qid}: {field}={q[field]!r} not in {sorted(allowed)}")
        unknown = set(q["relevant_doc_ids"]) - known_doc_ids
        if unknown:
            problems.append(f"{qid}: relevant_doc_ids not in dataset: {sorted(unknown)}")
        if is_answerable(q) and not q["relevant_doc_ids"]:
            problems.append(f"{qid}: answerable question has no relevant_doc_ids")
        if q["category"] in ABSTAIN_CATEGORIES and q["relevant_doc_ids"]:
            problems.append(f"{qid}: unanswerable question lists relevant_doc_ids")

    summary = {
        "total": len(questions),
        "by_split": dict(Counter(q.get("split") for q in questions)),
        "by_category": dict(Counter(q.get("category") for q in questions)),
        "by_status": dict(Counter(q.get("status") for q in questions)),
        "by_source": dict(Counter(q.get("source") for q in questions)),
    }
    return problems, summary
