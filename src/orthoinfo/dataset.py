"""Step 4b: build a documented, versioned dataset from raw downloads.

Outputs in data/processed/<version>/:
  documents.jsonl  one record per source (health topic) — see docs/data_dictionary.md
  chunks.jsonl     one record per section of a document; the unit that search ranks
  inventory.csv    human-readable source inventory for the sponsor and reviewer
  manifest.json    counts and SHA-256 checksums so a version can be verified later
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

from .collect import parse_search_xml
from .config import PROCESSED_DIR, RAW_DIR, ROOT, latest_version, load_scope
from .text import html_to_lines, split_sections, strip_html

PUBLISHER = "MedlinePlus, U.S. National Library of Medicine"
AUDIENCE = "patients and caregivers"
# Verify with the reviewer/sponsor before publishing anything: see
# https://medlineplus.gov/about/using/usingcontent/
PERMITTED_USE = (
    "NLM-written MedlinePlus health topic summaries are public domain; credit MedlinePlus "
    "and link to the source. Confirm against MedlinePlus 'Using our content' before reuse."
)


def _doc_id(url: str) -> str:
    return url.rstrip("/").rsplit("/", 1)[-1].removesuffix(".html")


def _first(doc: dict, key: str, default: str = "") -> str:
    values = doc.get(key) or [default]
    return values[0]


def build(version: str | None = None) -> Path:
    version = version or latest_version(RAW_DIR)
    raw = RAW_DIR / version
    raw_manifest = json.loads((raw / "manifest.json").read_text(encoding="utf-8"))
    scope = load_scope()

    documents, chunks = [], []
    for topic in raw_manifest["topics"]:
        parsed = parse_search_xml((raw / topic["raw_file"]).read_text(encoding="utf-8"))
        match = next((d for d in parsed if d["url"] == topic["url"]), None)
        if match is None:
            print(f"WARNING: no document for '{topic['term']}', skipped")
            continue

        doc_id = _doc_id(match["url"])
        title = strip_html(_first(match, "title"))
        summary_html = _first(match, "FullSummary")
        documents.append(
            {
                "doc_id": doc_id,
                "title": title,
                "alt_titles": [strip_html(t) for t in match.get("altTitle", [])],
                "mesh_terms": [strip_html(t) for t in match.get("mesh", [])],
                "groups": match.get("groupName", []),
                "specialty": scope["specialty"],
                "role": topic["role"],
                "audience": AUDIENCE,
                "publisher": PUBLISHER,
                "organization": _first(match, "organizationName"),
                "url": match["url"],
                "last_updated": topic.get("last_updated"),
                "retrieved": raw_manifest["retrieved"],
                "permitted_use": PERMITTED_USE,
                "language": scope.get("language", "en"),
                "summary_html": summary_html,
                "search_term": topic["term"],
                "dataset_version": version,
            }
        )
        for i, section in enumerate(split_sections(html_to_lines(summary_html), f"About {title}")):
            chunks.append(
                {
                    "chunk_id": f"{doc_id}#{i}",
                    "doc_id": doc_id,
                    "title": title,
                    "alt_titles": documents[-1]["alt_titles"],
                    "heading": section["heading"],
                    "text": section["text"],
                    "url": match["url"],
                    "last_updated": topic.get("last_updated"),
                    "role": topic["role"],
                }
            )

    out = PROCESSED_DIR / version
    out.mkdir(parents=True, exist_ok=True)
    _write_jsonl(out / "documents.jsonl", documents)
    _write_jsonl(out / "chunks.jsonl", chunks)
    with (out / "inventory.csv").open("w", newline="", encoding="utf-8") as fh:
        fields = ["doc_id", "title", "role", "audience", "publisher", "url",
                  "last_updated", "retrieved", "permitted_use"]
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(documents)

    manifest = {
        "version": version,
        "source_manifest": (raw / "manifest.json").relative_to(ROOT).as_posix(),
        "documents": len(documents),
        "chunks": len(chunks),
        "sha256": {
            name: hashlib.sha256((out / name).read_bytes()).hexdigest()
            for name in ("documents.jsonl", "chunks.jsonl", "inventory.csv")
        },
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return out


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def load_dataset(version: str | None = None) -> tuple[str, list[dict], list[dict]]:
    """Return (version, documents, chunks) for a processed dataset version."""
    version = version or latest_version(PROCESSED_DIR)
    base = PROCESSED_DIR / version
    return version, read_jsonl(base / "documents.jsonl"), read_jsonl(base / "chunks.jsonl")
