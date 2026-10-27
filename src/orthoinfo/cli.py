"""Command-line entry point: `orthoinfo <command>` (or `python -m orthoinfo`)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


TYPES_HELP = ("comma-separated source types (patient_education, encyclopedia, textbook, "
              "research_article) or 'all'; default from config/search.toml")


def _types(value: str | None) -> list[str] | None:
    """None means 'use the configured default'; [] means all types."""
    if not value:
        return None
    return [] if value == "all" else [t.strip() for t in value.split(",")]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="orthoinfo", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("collect", help="download raw source material (resumable)")
    p.add_argument("--version", help="dataset version label (default: v<today>)")
    p.add_argument("--sources", help="comma-separated subset, e.g. medlineplus,niams")

    p = sub.add_parser("build", help="clean raw downloads into a processed dataset version")
    p.add_argument("--version")

    p = sub.add_parser("search", help="run one query from the terminal")
    p.add_argument("query")
    p.add_argument("--method", default=None)
    p.add_argument("-k", type=int, default=5)
    p.add_argument("--types", help=TYPES_HELP)

    p = sub.add_parser("validate-questions", help="check data/eval/questions.jsonl")

    p = sub.add_parser("evaluate", help="compare search methods on the question set")
    p.add_argument("--methods", default="bm25,semantic,hybrid")
    p.add_argument("--split", default="dev", choices=["dev", "test", "all"])
    p.add_argument("--version")
    p.add_argument("--types", help=TYPES_HELP)

    p = sub.add_parser("pool", help="list unlabelled top results for relevance judging")
    p.add_argument("--methods", default="bm25,semantic,hybrid")
    p.add_argument("--depth", type=int, default=5)
    p.add_argument("--types", help=TYPES_HELP)

    p = sub.add_parser("pilot-summary", help="summarise usability session CSVs in data/pilot/")
    p.add_argument("files", nargs="*", type=Path)

    p = sub.add_parser("serve", help="run the web app")
    p.add_argument("--method")
    p.add_argument("--port", type=int, default=5000)
    p.add_argument("--debug", action="store_true")

    args = parser.parse_args(argv)

    if args.command == "collect":
        from .collect import collect
        only = [s.strip() for s in args.sources.split(",")] if args.sources else None
        print(f"Raw data saved to {collect(args.version, only)}")

    elif args.command == "build":
        from .dataset import build
        out = build(args.version)
        print(json.dumps(json.loads((out / "manifest.json").read_text()), indent=2))

    elif args.command == "search":
        from .config import PROCESSED_DIR, load_search_config
        from .dataset import load_dataset
        from .search import build_retriever
        cfg = load_search_config()
        method = args.method or cfg["default_method"]
        version, _, chunks = load_dataset()
        types = _types(args.types)
        if types is None:
            types = cfg.get("default_source_types")
        retriever = build_retriever(method, chunks, cfg["semantic_model"], PROCESSED_DIR / version)
        result = retriever.search(args.query, args.k, source_types=types)
        threshold = cfg["abstain_threshold"][method]
        print(f"[{method}] confidence={result.confidence:.3f} (abstain below {threshold}); types={types or 'all'}")
        for hit in result.hits:
            print(f"  {hit.score:7.3f}  [{hit.chunk['source']}] {hit.chunk['title']} — {hit.chunk['heading']}")

    elif args.command == "validate-questions":
        from .dataset import load_dataset
        from .questions import load_questions, validate
        _, documents, _ = load_dataset()
        problems, summary = validate(load_questions(), {d["doc_id"] for d in documents})
        print(json.dumps(summary, indent=2))
        for problem in problems:
            print("PROBLEM:", problem)
        return 1 if problems else 0

    elif args.command == "evaluate":
        from .experiment import run
        run([m.strip() for m in args.methods.split(",")], args.split, args.version, _types(args.types))

    elif args.command == "pool":
        from .experiment import pool
        pool([m.strip() for m in args.methods.split(",")], args.depth, source_types=_types(args.types))

    elif args.command == "pilot-summary":
        from .pilot import load_sessions, summarise
        rows = load_sessions(args.files or None)
        if not rows:
            print("No session files found in data/pilot/ (copy sessions_template.csv to start).")
            return 1
        print(summarise(rows))

    elif args.command == "serve":
        from .app import create_app
        create_app(args.method).run(port=args.port, debug=args.debug)

    return 0


if __name__ == "__main__":
    sys.exit(main())
