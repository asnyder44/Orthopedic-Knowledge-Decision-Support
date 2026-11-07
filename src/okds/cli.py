"""Command line: `okds validate`, `okds build-json`, `okds list`, `okds ask`. Used by CI too."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .config import get_settings
from .ko import as_dict
from .registry import load_registry
from .storage import LocalKOStore
from .validator import validate_file


def _validate(args: argparse.Namespace) -> int:
    s = get_settings()
    registry = load_registry(s.registry_path)
    paths = [Path(p).resolve() for p in args.paths] or sorted(s.kos_dir.rglob("*.md"))
    if not paths:
        print(f"No KO files found in {s.kos_dir}")
        return 0
    store = LocalKOStore(s)
    ids = {e.ko_id: str(e.path.resolve()) for e in store.list_entries()}
    failed = 0
    for path in paths:
        result = validate_file(path, registry, ids)
        status = "PASS" if result.ok else "FAIL"
        print(f"{status}  {path}  ({len(result.errors)} errors, {len(result.warnings)} warnings)")
        for issue in result.issues:
            if issue.level == "error" or args.warnings:
                print(f"    {issue.level.upper():7} [{issue.check}] {issue.message}")
        failed += not result.ok
    print(f"\n{len(paths) - failed} passed, {failed} failed")
    return 1 if failed else 0


def _build_json(args: argparse.Namespace) -> int:
    n = LocalKOStore(get_settings()).rebuild_json()
    print(f"Built {n} JSON file(s).")
    return 0


def _list(args: argparse.Namespace) -> int:
    for e in LocalKOStore(get_settings()).list_entries():
        if e.doc is None:
            print(f"{e.ko_id:20} BROKEN  {e.path}  ({e.error})")
        else:
            f = e.doc.front
            print(f"{e.ko_id:20} {str(as_dict(f.get('review')).get('status')):12} v{f.get('version')}  {f.get('title')}")
    return 0


def _ask(args: argparse.Namespace) -> int:
    """Ask OrthoBot from the terminal. Also a quick live check that the AI key works."""
    from . import chatbot, llm
    from .semantic import SemanticIndex

    s = get_settings()
    docs = [e.doc for e in LocalKOStore(s).list_entries() if e.doc is not None]
    if not docs:
        print(f"No KOs in {s.kos_dir}. Save one first.")
        return 1
    index = chatbot.KOIndex(docs, semantic=SemanticIndex(s.embedding_model, s.cache_dir,
                                                         enabled=s.semantic_enabled and args.method != "keyword"))
    use_ai = not args.search_only
    if use_ai and not s.ai_ready:
        print("AI is off (no API key in .env). Showing search results.\n")
        use_ai = False
    try:
        ans = (chatbot.answer_with_ai(args.question, index, s, args.method) if use_ai
               else chatbot.answer_retrieval_only(args.question, index, args.method))
    except llm.LLMError as e:
        print(f"AI error: {e}")
        return 1
    print(ans.text)
    for c in ans.citations:
        print(f"  [{c['n']}] {c['title']} - {c['section']} ({c['ko_id']})")
    for w in ans.warnings:
        print(f"  note: {w}")
    if use_ai:
        print(f"\n({s.ai_label}: {s.ai_model})")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="okds", description="OKDS Knowledge Object tools")
    sub = parser.add_subparsers(dest="command", required=True)
    v = sub.add_parser("validate", help="Validate KO files (default: all files in data/kos)")
    v.add_argument("paths", nargs="*")
    v.add_argument("--warnings", action="store_true", help="Also print warnings")
    v.set_defaults(func=_validate)
    sub.add_parser("build-json", help="Rebuild data/build/json from the Markdown KOs").set_defaults(func=_build_json)
    sub.add_parser("list", help="List KOs in the local library").set_defaults(func=_list)
    a = sub.add_parser("ask", help="Ask OrthoBot a question (uses the AI from .env if set)")
    a.add_argument("question")
    a.add_argument("--method", choices=["keyword", "semantic", "hybrid"], default=get_settings().search_method)
    a.add_argument("--search-only", action="store_true", help="No AI; show the matching KO parts")
    a.set_defaults(func=_ask)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
