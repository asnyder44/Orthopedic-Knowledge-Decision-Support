"""English Wikipedia articles (CC BY-SA 4.0) matched to the collected topics.

For every topic title found by the patient-education sources (plus any
`extra_titles`), the best Wikipedia search hit is fetched as plain text through
the MediaWiki API. Quality varies: treat as background, not as reviewed content.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

API = "https://en.wikipedia.org/w/api.php"
LICENSE = "CC BY-SA 4.0 (Wikipedia contributors); attribute and link to the article"
DROP_SECTIONS = re.compile(r"(?i)^(see also|references|external links|further reading|notes|bibliography|sources|citations)$")


def _topic_titles(version_dir: Path, from_sources: list[str]) -> list[str]:
    from . import SOURCES

    titles = []
    for name in from_sources:
        raw = version_dir / name
        if (raw / "manifest.json").exists():
            titles += [d["title"] for d in SOURCES[name].parse(raw, _source_cfg(name))]
    return titles


def _source_cfg(name: str) -> dict:
    from ..config import load_sources_config

    return load_sources_config()[name]


def _filename(title: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "_", title)[:120] + ".json"


def collect(out: Path, cfg: dict, http) -> None:
    from . import write_manifest

    wanted = _topic_titles(out.parent, cfg.get("titles_from", [])) + cfg.get("extra_titles", [])
    matches_path = out / "matches.json"
    matches = json.loads(matches_path.read_text(encoding="utf-8")) if matches_path.exists() else {}
    for term in dict.fromkeys(wanted):
        if term in matches:
            continue
        found = http.json(API, {"action": "query", "list": "search", "srsearch": term, "srlimit": 1,
                                "format": "json"}, delay=cfg.get("delay", 0.5))
        hits = found.get("query", {}).get("search", [])
        matches[term] = hits[0]["title"] if hits else None
        matches_path.write_text(json.dumps(matches, indent=1), encoding="utf-8")

    pages = sorted({t for t in matches.values() if t})
    print(f"  {len(pages)} articles for {len(matches)} topic titles")
    for title in pages:
        path = out / _filename(title)
        if path.exists():
            continue
        data = http.json(API, {
            "action": "query", "prop": "extracts|info|revisions", "titles": title, "explaintext": 1,
            "exsectionformat": "wiki", "inprop": "url", "rvprop": "timestamp", "redirects": 1,
            "format": "json", "formatversion": 2,
        }, delay=cfg.get("delay", 0.5))
        path.write_text(json.dumps(data), encoding="utf-8")
    write_manifest(out, pages=pages)


def _sections(extract: str, title: str) -> list[dict]:
    sections, heading, buf, dropping = [], title, [], False
    for line in extract.splitlines():
        m = re.match(r"^(=+)\s*(.*?)\s*\1$", line.strip())
        if m:
            if buf and not dropping:
                sections.append({"heading": heading, "text": "\n".join(buf)})
            level, name = len(m.group(1)), m.group(2)
            if level == 2:
                dropping = bool(DROP_SECTIONS.match(name))
            heading, buf = name, []
        elif line.strip():
            buf.append(line.strip())
    if buf and not dropping:
        sections.append({"heading": heading, "text": "\n".join(buf)})
    return sections


def parse(raw: Path, cfg: dict):
    from . import make_document, read_manifest

    manifest = read_manifest(raw)
    for title in manifest["pages"]:
        path = raw / _filename(title)
        if not path.exists():
            continue
        pages = json.loads(path.read_text(encoding="utf-8")).get("query", {}).get("pages", [])
        if not pages or "missing" in pages[0]:
            continue
        page = pages[0]
        sections = _sections(page.get("extract", ""), page["title"])
        if not sections:
            continue
        revisions = page.get("revisions") or [{}]
        yield make_document(
            doc_id="wiki:" + page["title"].replace(" ", "_"),
            source="wikipedia",
            source_type="encyclopedia",
            title=page["title"],
            url=page.get("fullurl", "https://en.wikipedia.org/wiki/" + page["title"].replace(" ", "_")),
            sections=sections,
            audience="general public",
            publisher="Wikipedia",
            license=LICENSE,
            retrieved=manifest["retrieved"],
            authors="Wikipedia contributors",
            container="Wikipedia",
            last_updated=(revisions[0].get("timestamp") or "")[:10] or None,
        )
