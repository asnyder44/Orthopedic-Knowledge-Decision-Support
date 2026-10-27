"""Step 4b: build a documented, versioned dataset from raw downloads.

Outputs in data/processed/<version>/:
  documents.jsonl.gz  one record per source document — see docs/data_dictionary.md
  chunks.jsonl.gz     ~220-word pieces of each section; the unit search ranks
  inventory.csv       source inventory (no text) for the sponsor and reviewer
  manifest.json       counts by source and licence, SHA-256 checksums
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path

from .config import PROCESSED_DIR, RAW_DIR, latest_version, load_scope, load_sources_config
from .sources import SOURCES
from .text import chunk_text

CHUNK_WORDS = 220
CHUNK_FIELDS = ("doc_id", "source", "source_type", "audience", "title", "alt_titles", "url",
                "container", "published", "last_updated", "role")
INVENTORY_FIELDS = ("doc_id", "source", "source_type", "title", "role", "audience", "authors",
                    "container", "publisher", "published", "last_updated", "retrieved", "url", "license")


def build(version: str | None = None) -> Path:
    version = version or latest_version(RAW_DIR)
    raw = RAW_DIR / version
    cfg, scope = load_sources_config(), load_scope()
    core = set(scope.get("core_doc_ids", []))

    documents: dict[str, dict] = {}
    for name, module in SOURCES.items():
        if not (raw / name / "manifest.json").exists():
            continue
        before = len(documents)
        for doc in module.parse(raw / name, cfg.get(name, {})):
            doc["role"] = "core" if doc["doc_id"] in core else "context"
            doc["specialty"] = scope["specialty"]
            doc["dataset_version"] = version
            documents.setdefault(doc["doc_id"], doc)
        print(f"  {name:12s} {len(documents) - before:6d} documents")
    if not documents:
        raise SystemExit(f"No raw data in {raw}. Run `orthoinfo collect` first.")

    chunks = []
    for doc in documents.values():
        n = 0
        for section in doc["sections"]:
            for text in chunk_text(section["text"], CHUNK_WORDS):
                chunks.append({"chunk_id": f"{doc['doc_id']}#{n}", **{f: doc.get(f) for f in CHUNK_FIELDS},
                               "heading": section["heading"], "text": text})
                n += 1

    out = PROCESSED_DIR / version
    out.mkdir(parents=True, exist_ok=True)
    write_jsonl(out / "documents.jsonl.gz", documents.values())
    write_jsonl(out / "chunks.jsonl.gz", chunks)
    with (out / "inventory.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=INVENTORY_FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(documents.values())

    docs = list(documents.values())
    manifest = {
        "version": version,
        "documents": len(docs),
        "chunks": len(chunks),
        "words": sum(len(c["text"].split()) for c in chunks),
        "by_source": dict(Counter(d["source"] for d in docs)),
        "by_source_type": dict(Counter(d["source_type"] for d in docs)),
        "by_license": dict(Counter(d["license"].split(" — ")[0] for d in docs)),
        "sha256": {name: hashlib.sha256((out / name).read_bytes()).hexdigest()
                   for name in ("documents.jsonl.gz", "chunks.jsonl.gz", "inventory.csv")},
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return out


def write_jsonl(path: Path, rows) -> None:
    # mtime=0 keeps the gzip bytes (and checksum) identical for identical content.
    with path.open("wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as gz:
        for row in rows:
            gz.write((json.dumps(row, ensure_ascii=False) + "\n").encode("utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def load_dataset(version: str | None = None) -> tuple[str, list[dict], list[dict]]:
    """Return (version, documents, chunks) for a processed dataset version."""
    version = version or latest_version(PROCESSED_DIR)
    base = PROCESSED_DIR / version
    return version, read_jsonl(base / "documents.jsonl.gz"), read_jsonl(base / "chunks.jsonl.gz")
