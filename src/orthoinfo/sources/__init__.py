"""Source collectors. Each module provides:

    collect(out: Path, cfg: dict, http: Http) -> None
        download raw material into `out` (data/raw/<version>/<source>/), skipping
        files already present so an interrupted run can simply be restarted, and
        write out/manifest.json with at least {"retrieved": ISO datetime}.

    parse(raw: Path, cfg: dict) -> Iterator[dict]
        turn raw files into document records built with `make_document`.

Only sources whose terms allow reuse are collected; the licence of every
document is recorded so the app can show it and the team can check it.
"""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

from . import europepmc, medlineplus, niams, openstax, wikipedia

# Order matters: wikipedia searches for the topic titles found by earlier sources.
SOURCES = {
    "medlineplus": medlineplus,
    "niams": niams,
    "openstax": openstax,
    "europepmc": europepmc,
    "wikipedia": wikipedia,
}

SOURCE_TYPES = ("patient_education", "encyclopedia", "textbook", "research_article")


def make_document(
    *,
    doc_id: str,
    source: str,
    source_type: str,
    title: str,
    url: str,
    sections: list[dict],
    audience: str,
    publisher: str,
    license: str,
    retrieved: str,
    **extra,
) -> dict:
    assert source_type in SOURCE_TYPES, source_type
    doc = {
        "doc_id": doc_id,
        "source": source,
        "source_type": source_type,
        "title": title,
        "alt_titles": [],
        "authors": "",
        "container": "",  # journal, book or website the item belongs to
        "publisher": publisher,
        "audience": audience,
        "url": url,
        "license": license,
        "published": None,
        "last_updated": None,
        "retrieved": retrieved,
        "language": "en",
        "mesh_terms": [],
        "groups": [],
        "related_links": [],
        "sections": sections,
    }
    doc.update(extra)
    return doc


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def write_manifest(out: Path, **fields) -> None:
    path = out / "manifest.json"
    old = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    (out / "manifest.json").write_text(json.dumps(old | {"retrieved": now_iso()} | fields, indent=2), encoding="utf-8")


def read_manifest(raw: Path) -> dict:
    return json.loads((raw / "manifest.json").read_text(encoding="utf-8"))
