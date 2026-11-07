"""Where KOs are saved. Local files now; S3 and a database are planned (same interface)."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from . import vocab
from .config import Settings
from .ko import KODocument, ko_relpath, parse_ko, render_ko, to_json_record


class StorageError(ValueError):
    """A KO that cannot be saved safely (bad ID or specialty). The message is shown to the user."""


def _id_pattern() -> re.Pattern[str]:
    return re.compile(vocab.load_ko_schema()["properties"]["ko_id"]["pattern"])


def check_ko_id(ko_id: object) -> str:
    """The ID is used in file names, so only IDs like KO-HAND-COND-001 are allowed."""
    if not isinstance(ko_id, str) or not _id_pattern().match(ko_id):
        raise StorageError(f"'{ko_id}' is not a valid KO ID. It must look like KO-HAND-COND-001.")
    return ko_id


def _inside(path: Path, folder: Path) -> Path:
    path, folder = path.resolve(), folder.resolve()
    if not path.is_relative_to(folder):
        raise StorageError("This KO would be saved outside the data folder, so it was blocked.")
    return path


@dataclass
class SavedKO:
    ko_id: str
    markdown_path: str
    json_path: str
    pack_path: str | None


@dataclass
class KOEntry:
    ko_id: str
    path: Path
    doc: KODocument | None
    error: str | None = None


class KOStore(Protocol):
    def save(self, doc: KODocument, source_pack: str | None = None) -> SavedKO: ...
    def list_entries(self) -> list[KOEntry]: ...
    def delete(self, ko_id: str) -> None: ...


class LocalKOStore:
    """Markdown in data/kos/<specialty>/, JSON in data/build/json/, source packs in data/sources/packs/."""

    def __init__(self, settings: Settings):
        self.settings = settings
        settings.ensure_dirs()

    def _rel(self, path: Path) -> str:
        try:
            return path.relative_to(self.settings.data_dir).as_posix()
        except ValueError:
            return path.as_posix()

    def exists(self, ko_id: str) -> bool:
        return any(e.ko_id == ko_id for e in self.list_entries())

    def save(self, doc: KODocument, source_pack: str | None = None) -> SavedKO:
        """Save the Markdown, its JSON copy, and the source pack. An older file with the same ID is
        replaced (e.g. the title changed); the new file is written first, so nothing is lost if it fails."""
        s = self.settings
        ko_id = check_ko_id(doc.front.get("ko_id"))
        specialty = str(doc.front.get("specialty", ""))
        if specialty not in vocab.specialties():
            raise StorageError(f"Unknown specialty '{specialty}'. Use one of: {', '.join(vocab.specialties())}.")
        md_path = _inside(s.kos_dir / ko_relpath(doc.front), s.kos_dir)
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(render_ko(doc), encoding="utf-8", newline="\n")
        for entry in self.list_entries():
            if entry.ko_id == ko_id and entry.path.resolve() != md_path:
                entry.path.unlink()
        record = to_json_record(doc, source_file=self._rel(md_path))
        json_path = s.json_dir / f"{ko_id}.json"
        json_path.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")
        pack_path = None
        if source_pack:
            pack_path = s.packs_dir / f"SP-{ko_id}.md"
            pack_path.write_text(source_pack, encoding="utf-8", newline="\n")
        return SavedKO(ko_id, self._rel(md_path), self._rel(json_path), self._rel(pack_path) if pack_path else None)

    def list_entries(self) -> list[KOEntry]:
        entries = []
        for path in sorted(self.settings.kos_dir.rglob("*.md")):
            try:
                doc = parse_ko(path.read_text(encoding="utf-8"))
                entries.append(KOEntry(doc.ko_id or path.stem, path, doc))
            except Exception as e:  # show broken files in the library instead of failing
                entries.append(KOEntry(path.stem.split("_")[0], path, None, str(e)))
        return entries

    def rebuild_json(self) -> int:
        count = 0
        for entry in self.list_entries():
            if entry.doc is not None and _id_pattern().match(entry.ko_id or ""):
                record = to_json_record(entry.doc, source_file=self._rel(entry.path))
                out = self.settings.json_dir / f"{entry.ko_id}.json"
                out.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")
                count += 1
        return count

    def delete(self, ko_id: str) -> None:
        check_ko_id(ko_id)
        for entry in self.list_entries():
            if entry.ko_id == ko_id:
                entry.path.unlink()
        (self.settings.json_dir / f"{ko_id}.json").unlink(missing_ok=True)


class S3KOStore:
    """Planned. Keep the bucket private: S3 Block Public Access on, no public bucket policy,
    server-side encryption, and IAM credentials from the environment (never in code)."""

    def __init__(self, settings: Settings):
        raise NotImplementedError(
            "S3 storage is planned but not built yet. Set OKDS_STORAGE=local for now."
        )


def get_store(settings: Settings) -> LocalKOStore:
    if settings.storage_backend == "local":
        return LocalKOStore(settings)
    if settings.storage_backend == "s3":
        S3KOStore(settings)
    raise ValueError(f"Unknown OKDS_STORAGE '{settings.storage_backend}'. Use 'local'.")
