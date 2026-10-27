"""Steps 6-7: run every search method on the same questions and dataset.

Reports, per method:
  * ranking quality  — hit@1, recall@5, MRR@10, nDCG@10 over answerable questions
  * by question type — the same metrics split by category (lay, technical, ...)
  * robustness       — do paraphrases of one question reach the same top source?
  * abstention       — does confidence separate answerable from unanswerable?
  * cost             — index build time, query latency
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import statistics
import time
from collections import defaultdict
from pathlib import Path

from . import metrics as M
from .config import PROCESSED_DIR, RESULTS_DIR, load_search_config
from .dataset import load_dataset
from .questions import ABSTAIN_CATEGORIES, is_answerable, load_questions
from .safety import needs_scope_notice
from .search import build_retriever

K = 10


def evaluate_method(method: str, chunks: list[dict], questions: list[dict], cfg: dict, cache_dir: Path,
                    source_types: list[str] | None = None) -> dict:
    t0 = time.perf_counter()
    retriever = build_retriever(method, chunks, cfg["semantic_model"], cache_dir)
    index_seconds = time.perf_counter() - t0
    threshold = cfg["abstain_threshold"][method]

    rows, latencies = [], []
    for q in questions:
        t = time.perf_counter()
        # Several chunks can come from one document; fetch enough to rank K documents.
        result = retriever.search(q["question"], k=K * 5, source_types=source_types)
        latencies.append((time.perf_counter() - t) * 1000)
        ranked = result.ranked_doc_ids()
        rel = set(q["relevant_doc_ids"])
        rows.append(
            {
                "method": method,
                "id": q["id"],
                "category": q["category"],
                "paraphrase_group": q.get("paraphrase_group") or "",
                "question": q["question"],
                "relevant": ";".join(sorted(rel)),
                "top_docs": ";".join(ranked[:5]),
                "hit@1": M.hit_at_k(ranked, rel, 1),
                "recall@5": M.recall_at_k(ranked, rel, 5),
                "rr@10": M.reciprocal_rank(ranked, rel, K),
                "ndcg@10": M.ndcg_at_k(ranked, rel, K),
                "confidence": round(result.confidence, 4),
                "abstained": result.confidence < threshold,
                "scope_notice": needs_scope_notice(q["question"]),
            }
        )

    answerable = [r for r, q in zip(rows, questions) if is_answerable(q)]
    unanswerable = [r for r in rows if r["category"] in ABSTAIN_CATEGORIES]
    out_of_scope = [r for r in rows if r["category"] == "out_of_scope"]
    in_scope = [r for r in rows if r["category"] != "out_of_scope"]

    def agg(subset):
        return {m: round(M.mean([r[m] for r in subset]), 3) for m in ("hit@1", "recall@5", "rr@10", "ndcg@10")} | {"n": len(subset)}

    by_category = defaultdict(list)
    for r in answerable:
        by_category[r["category"]].append(r)

    groups = defaultdict(list)
    for r in answerable:
        if r["paraphrase_group"]:
            groups[r["paraphrase_group"]].append(r)
    groups = {g: rs for g, rs in groups.items() if len(rs) > 1}
    same_top = [len({r["top_docs"].split(";")[0] for r in rs}) == 1 for rs in groups.values()]
    rr_spread = [statistics.pstdev([r["rr@10"] for r in rs]) for rs in groups.values()]

    suggested, bal_acc = M.best_threshold(
        [r["confidence"] for r in answerable], [r["confidence"] for r in unanswerable]
    )
    return {
        "method": method,
        "ranking": agg(answerable),
        "by_category": {c: agg(rs) for c, rs in sorted(by_category.items())},
        "robustness": {
            "paraphrase_groups": len(groups),
            "same_top_source_rate": round(M.mean([float(x) for x in same_top]), 3),
            "mean_rr_stdev": round(M.mean(rr_spread), 3),
        },
        "abstention": {
            "threshold": threshold,
            "answerable_wrongly_abstained": sum(r["abstained"] for r in answerable),
            "unanswerable_correctly_abstained": sum(r["abstained"] for r in unanswerable),
            "n_answerable": len(answerable),
            "n_unanswerable": len(unanswerable),
            "suggested_threshold": round(suggested, 4),
            "suggested_balanced_accuracy": round(bal_acc, 3),
        },
        "scope_guard": {
            "out_of_scope_flagged": sum(r["scope_notice"] for r in out_of_scope),
            "n_out_of_scope": len(out_of_scope),
            "false_flags_in_scope": sum(r["scope_notice"] for r in in_scope),
        },
        "cost": {
            "index_seconds": round(index_seconds, 3),
            "mean_query_ms": round(M.mean(latencies), 2),
            "p95_query_ms": round(M.percentile(latencies, 95), 2),
            "external_api_cost": "none (runs locally)",
        },
        "rows": rows,
    }


def run(methods: list[str], split: str, version: str | None = None,
        source_types: list[str] | None = None) -> Path:
    cfg = load_search_config()
    if source_types is None:
        source_types = cfg.get("default_source_types")
    version, _, chunks = load_dataset(version)
    questions = load_questions(split=split)
    if not questions:
        raise SystemExit(f"No questions in split {split!r}")

    results = []
    for method in methods:
        print(f"Evaluating {method} on {len(questions)} {split} questions ({', '.join(source_types or ['all sources'])})...")
        try:
            results.append(evaluate_method(method, chunks, questions, cfg, PROCESSED_DIR / version, source_types))
        except (RuntimeError, OSError) as exc:
            print(f"  skipped {method}: {exc}")

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out = RESULTS_DIR / f"{stamp}_{split}"
    out.mkdir(parents=True, exist_ok=True)
    rows = [r for res in results for r in res.pop("rows")]
    if rows:
        with (out / "per_question.csv").open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    meta = {"dataset_version": version, "split": split, "n_questions": len(questions), "k": K,
            "source_types": source_types or "all"}
    (out / "summary.json").write_text(json.dumps(meta | {"methods": results}, indent=2), encoding="utf-8")
    (out / "summary.md").write_text(render_markdown(meta, results), encoding="utf-8")
    print((out / "summary.md").read_text(encoding="utf-8"))
    if split == "test":
        print("NOTE: test split — report these numbers; do not tune on them.")
    return out


def render_markdown(meta: dict, results: list[dict]) -> str:
    lines = [
        f"# Search experiment — {meta['split']} split",
        "",
        f"Dataset version `{meta['dataset_version']}`, {meta['n_questions']} questions, "
        f"source types: {meta['source_types']}. Metrics over source documents.",
        "",
        "## Ranking quality (answerable questions)",
        "",
        "| Method | n | hit@1 | recall@5 | MRR@10 | nDCG@10 |",
        "|---|---|---|---|---|---|",
    ]
    for r in results:
        g = r["ranking"]
        lines.append(f"| {r['method']} | {g['n']} | {g['hit@1']} | {g['recall@5']} | {g['rr@10']} | {g['ndcg@10']} |")

    lines += ["", "## By question type (MRR@10)", "", "| Method | " + " | ".join(
        sorted({c for r in results for c in r["by_category"]})) + " |"]
    cats = sorted({c for r in results for c in r["by_category"]})
    lines.append("|---" * (len(cats) + 1) + "|")
    for r in results:
        cells = [f"{r['by_category'][c]['rr@10']} (n={r['by_category'][c]['n']})" if c in r["by_category"] else "–" for c in cats]
        lines.append(f"| {r['method']} | " + " | ".join(cells) + " |")

    lines += ["", "## Robustness, abstention, scope guard, cost", "",
              "| Method | same top source across paraphrases | wrongly abstained | correctly abstained | suggested threshold | out-of-scope flagged | index s | query ms (mean / p95) |",
              "|---|---|---|---|---|---|---|---|"]
    for r in results:
        rb, ab, sg, c = r["robustness"], r["abstention"], r["scope_guard"], r["cost"]
        lines.append(
            f"| {r['method']} | {rb['same_top_source_rate']} ({rb['paraphrase_groups']} groups) "
            f"| {ab['answerable_wrongly_abstained']}/{ab['n_answerable']} "
            f"| {ab['unanswerable_correctly_abstained']}/{ab['n_unanswerable']} "
            f"| {ab['suggested_threshold']} (bal. acc {ab['suggested_balanced_accuracy']}) "
            f"| {sg['out_of_scope_flagged']}/{sg['n_out_of_scope']} "
            f"| {c['index_seconds']} | {c['mean_query_ms']} / {c['p95_query_ms']} |"
        )
    lines += ["", "Small question sets give noisy numbers: report counts alongside rates and "
              "read failures in per_question.csv before drawing conclusions.", ""]
    return "\n".join(lines)


def pool(methods: list[str], depth: int = 5, version: str | None = None,
         source_types: list[str] | None = None) -> Path:
    """Write the unlabelled top results of every method for relevance judging.

    A larger collection means questions have relevant documents nobody has
    labelled yet, which makes every method look worse. Standard fix ("pooling"):
    judge the union of each method's top `depth` documents, then add the relevant
    ones to `relevant_doc_ids` in questions.jsonl.
    """
    cfg = load_search_config()
    if source_types is None:
        source_types = cfg.get("default_source_types")
    version, documents, chunks = load_dataset(version)
    titles = {d["doc_id"]: (d["title"], d["url"]) for d in documents}
    questions = [q for q in load_questions() if q["category"] not in ABSTAIN_CATEGORIES]

    found: dict[tuple[str, str], list[str]] = defaultdict(list)
    for method in methods:
        try:
            retriever = build_retriever(method, chunks, cfg["semantic_model"], PROCESSED_DIR / version)
        except (RuntimeError, OSError) as exc:
            print(f"  skipped {method}: {exc}")
            continue
        for q in questions:
            ranked = retriever.search(q["question"], k=depth * 5, source_types=source_types).ranked_doc_ids()
            for doc_id in ranked[:depth]:
                if doc_id not in q["relevant_doc_ids"]:
                    found[(q["id"], doc_id)].append(method)

    out = RESULTS_DIR / f"pool_{dt.datetime.now():%Y%m%d-%H%M%S}.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    by_id = {q["id"]: q for q in questions}
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["question_id", "question", "doc_id", "title", "url", "found_by", "relevant (y/n)"])
        for (qid, doc_id), found_by in sorted(found.items()):
            writer.writerow([qid, by_id[qid]["question"], doc_id, *titles[doc_id], "+".join(found_by), ""])
    print(f"{len(found)} unjudged (question, document) pairs written to {out}")
    return out
