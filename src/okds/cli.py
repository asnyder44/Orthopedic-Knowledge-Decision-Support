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


def _collect(args: argparse.Namespace) -> int:
    """Search the open-access providers for one term and save every candidate."""
    from . import collect
    from .ko import slugify

    s = get_settings()
    providers = [p.strip() for p in args.providers.split(",")] if args.providers else None
    cands = collect.collect(args.term, args.alt, per_provider=args.per_provider, providers=providers)
    out = s.data_dir / "sources" / "candidates" / f"{slugify(args.term)}.json"
    collect.save_candidates(out, args.term, cands)
    for c in cands[: args.show]:
        print(f"{c.score:5.2f}  {c.kind:17} {c.permitted_use:20} {c.year:4}  {c.title[:80]}  [{','.join(c.providers)}]")
    print(f"\n{len(cands)} candidate(s) saved to {out}")
    return 0


def _collect_topics(args: argparse.Namespace) -> int:
    """Collect sources for registry topics; save candidates and a source pack (SP-<ko_id>.md) for each."""
    from . import collect

    s = get_settings()
    s.ensure_dirs()
    registry = load_registry(s.registry_path)
    have_ko = {e.ko_id for e in LocalKOStore(s).list_entries()}
    ids = args.ids or [c.ko_id for c in registry.values() if args.all or c.ko_id not in have_ko]
    providers = [p.strip() for p in args.providers.split(",")] if args.providers else None
    for ko_id in ids:
        c = registry.get(ko_id)
        if c is None:
            print(f"{ko_id}: not in the registry, skipped")
            continue
        pack_path = s.packs_dir / f"SP-{ko_id}.md"
        cand_path = s.data_dir / "sources" / "candidates" / f"{ko_id}.json"
        if pack_path.is_file() and not args.overwrite:
            print(f"{ko_id}: source pack exists (use --overwrite), skipped")
            continue
        print(f"{ko_id}: {c.preferred_term}")
        cands = collect.collect(c.preferred_term, c.alternate_terms, per_provider=args.per_provider, providers=providers)
        collect.save_candidates(cand_path, c.preferred_term, cands)
        pack = collect.pick_pack(cands, patient=True, size=args.pack_size)
        if len(pack) < 2:
            print(f"  only {len(pack)} usable source(s); no pack written")
            continue
        sources = [collect.as_source(x, f"S{i}") for i, x in enumerate(pack, 1)]
        pack_path.write_text(collect.render_pack(ko_id, c.preferred_term, sources), encoding="utf-8", newline="\n")
        print(f"  {len(cands)} candidates; pack of {len(pack)} -> {pack_path.name}")
    return 0


def _sources(args: argparse.Namespace) -> int:
    from . import collect, packs

    s = get_settings()
    if args.action == "show":
        path = packs.candidates_path(s, args.target)
        if not path.is_file():
            print(f"No candidates for {args.target}. Run: okds collect-topics {args.target}")
            return 1
        for i, c in enumerate(collect.load_candidates(path), 1):
            print(f"c{i:<3} {c.score:5.2f} {c.kind:17} {c.permitted_use:20} {c.year:4} {c.title[:90]}")
            if args.verbose:
                print(f"       {c.publisher[:60]} | {c.url}\n       {c.abstract[:300]}\n")
    elif args.action == "local":
        for _score, d in packs.search_local(" ".join([args.target, *args.picks])):
            print(f"local:{d['doc_id']:42} {d['source']:12} {d['title'][:80]}")
    else:  # set
        try:
            pack, ko = packs.set_sources(s, args.target, args.picks)
        except ValueError as e:
            print(f"Not changed: {e}")
            return 1
        print(f"Wrote {pack}" + (f" and updated sources in {ko}" if ko else ""))
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
    c = sub.add_parser("collect", help="Search open-access sources (Europe PMC, DOAJ, PLOS, ...) for one term")
    c.add_argument("term")
    c.add_argument("--alt", nargs="*", default=[], help="Other names that also count as a match")
    c.add_argument("--per-provider", type=int, default=10)
    c.add_argument("--providers", help="Comma-separated subset, e.g. europepmc,doaj,plos")
    c.add_argument("--show", type=int, default=15)
    c.set_defaults(func=_collect)
    ct = sub.add_parser("collect-topics", help="Collect sources and write a source pack for registry topics")
    ct.add_argument("ids", nargs="*", help="KO IDs (default: every topic without a KO)")
    ct.add_argument("--all", action="store_true", help="Include topics that already have a KO")
    ct.add_argument("--overwrite", action="store_true", help="Replace existing source packs")
    ct.add_argument("--per-provider", type=int, default=10)
    ct.add_argument("--pack-size", type=int, default=4)
    ct.add_argument("--providers")
    ct.set_defaults(func=_collect_topics)
    so = sub.add_parser("sources", help="Browse candidates, search the OrthoInfo dataset, set a KO's sources")
    so.add_argument("action", choices=["show", "local", "set"])
    so.add_argument("target", help="KO ID (show, set) or search words (local)")
    so.add_argument("picks", nargs="*", help="set: c<number> or local:<doc_id>, in order (S1, S2, ...)")
    so.add_argument("-v", "--verbose", action="store_true", help="show: also print publisher, link, abstract")
    so.set_defaults(func=_sources)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
