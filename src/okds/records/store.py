"""Uploaded record batches, by data model. Same flow as KO drafts: upload -> automatic checks -> review -> used.

data/records/<model>/batches/<batch-id>/
  batch.json        status (pending | accepted | rejected), who, when, counts, check issues, attestation
  <Entity>.csv      the rows, one file per entity (only the model's columns)

Only accepted batches are counted in summaries and linked into the Discovery Network. Real uploads are
ignored by git (see .gitignore); only the synthetic sample batch is kept in the repository.
"""

from __future__ import annotations

import csv
import datetime as dt
import io
import json
import re
import uuid
import zipfile
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..config import Settings
from .checks import CheckResult, check_batch
from .model import DataModel

MAX_UPLOAD_BYTES = 20_000_000
MIN_CELL = 5  # summaries show "<5" for smaller counts
BATCH_ID_RE = re.compile(r"[A-Za-z0-9-]{3,60}")


class UploadError(ValueError):
    pass


@dataclass
class Batch:
    id: str
    model: str
    meta: dict[str, Any]
    path: Path

    @property
    def status(self) -> str:
        return str(self.meta.get("status", "pending"))

    def tables(self) -> dict[str, list[dict[str, str]]]:
        out = {}
        for p in sorted(self.path.glob("*.csv")):
            with p.open(encoding="utf-8", newline="") as f:
                out[p.stem] = list(csv.DictReader(f))
        return out


# ---------------------------------------------------------------- reading uploads

def _rows_from_csv(text: str) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(text.lstrip("﻿")))
    return [{(k or "").strip(): (v or "").strip() for k, v in row.items() if k is not None} for row in reader]


def read_upload(files: list[tuple[str, bytes]]) -> dict[str, list[dict[str, Any]]]:
    """files: (file name, bytes). <Entity>.csv files, a .zip of them, or a .json object {"Entity": [rows]}."""
    tables: dict[str, list[dict[str, Any]]] = {}
    total = 0
    for name, data in files:
        total += len(data)
        if total > MAX_UPLOAD_BYTES:
            raise UploadError("The upload is too large (20 MB at most).")
        lower = name.lower()
        if lower.endswith(".zip"):
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                inner = [(Path(n).name, z.read(n)) for n in z.namelist()
                         if n.lower().endswith((".csv", ".json")) and not n.startswith("__MACOSX")]
            tables.update(read_upload(inner))
        elif lower.endswith(".csv"):
            tables.setdefault(Path(name).stem, []).extend(_rows_from_csv(data.decode("utf-8-sig", errors="replace")))
        elif lower.endswith(".json"):
            try:
                obj = json.loads(data.decode("utf-8-sig"))
            except (UnicodeDecodeError, json.JSONDecodeError) as e:
                raise UploadError(f"{name} is not valid JSON ({e}).") from e
            if not isinstance(obj, dict) or not all(isinstance(v, list) for v in obj.values()):
                raise UploadError(f'{name}: JSON must look like {{"Patient": [{{...}}, ...], "Rehabilitation": [...]}}.')
            for k, rows in obj.items():
                tables.setdefault(k, []).extend({str(c): ("" if v is None else v) for c, v in r.items()}
                                                for r in rows if isinstance(r, dict))
        else:
            raise UploadError(f"{name}: upload CSV files (one per entity, named like Patient.csv), a .zip of them, "
                              f"or a .json file.")
    return tables


# ---------------------------------------------------------------- store

class RecordStore:
    def __init__(self, settings: Settings, model: DataModel):
        self.s = settings
        self.model = model
        self.root = settings.records_dir / model.name / "batches"

    def batches(self, status: str | None = None) -> list[Batch]:
        out = []
        if not self.root.is_dir():
            return out
        for d in sorted(self.root.iterdir()):
            meta_path = d / "batch.json"
            if not meta_path.is_file():
                continue
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            b = Batch(d.name, self.model.name, meta, d)
            if status is None or b.status == status:
                out.append(b)
        return sorted(out, key=lambda b: str(b.meta.get("created", "")), reverse=True)

    def get(self, batch_id: str) -> Batch | None:
        if not BATCH_ID_RE.fullmatch(batch_id or ""):
            return None
        return next((b for b in self.batches() if b.id == batch_id), None)

    def accepted_ids(self) -> dict[str, set[str]]:
        ids: dict[str, set[str]] = {}
        for b in self.batches("accepted"):
            for ent, rows in b.tables().items():
                e = self.model.entities.get(ent)
                if e is not None:
                    ids.setdefault(ent, set()).update(r.get(e.id_field, "") for r in rows)
        return ids

    def check(self, tables: dict[str, list[dict[str, Any]]], ko_types: dict[str, str] | None) -> CheckResult:
        return check_batch(self.model, tables, self.accepted_ids(), ko_types)

    def save(self, tables: dict[str, list[dict[str, Any]]], result: CheckResult, *, uploaded_by: str, synthetic: bool,
             agreement: str, note: str = "", batch_id: str | None = None, status: str = "pending") -> Batch:
        if not result.ok:
            raise UploadError(f"{len(result.errors)} problem(s) to fix first.")
        bid = batch_id or f"{dt.date.today():%Y%m%d}-{uuid.uuid4().hex[:6]}"
        d = self.root / bid
        d.mkdir(parents=True, exist_ok=False)
        for ent_name, rows in result.clean.items():
            ent = self.model.entities[ent_name]
            with (d / f"{ent_name}.csv").open("w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(ent.fields))
                w.writeheader()
                for r in rows:
                    w.writerow({k: _cell(r.get(k)) for k in ent.fields})
        meta = {"id": bid, "model": self.model.name, "model_version": self.model.version, "status": status,
                "created": dt.datetime.now().replace(microsecond=0).isoformat(), "uploaded_by": uploaded_by,
                "synthetic": synthetic, "agreement": agreement, "note": note, "counts": result.counts,
                "warnings": [str(i) for i in result.warnings][:200]}
        (d / "batch.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")
        return Batch(bid, self.model.name, meta, d)

    def decide(self, batch_id: str, decision: str, reviewer: str, reason: str = "") -> Batch:
        b = self.get(batch_id)
        if b is None:
            raise UploadError("No such batch.")
        if b.status != "pending":
            raise UploadError(f"This batch is already {b.status}.")
        if not reviewer.strip():
            raise UploadError("Type your name first.")
        if decision == "rejected" and not reason.strip():
            raise UploadError("Say why you reject it.")
        if decision == "accepted":  # ids may have been taken by a batch accepted in the meantime
            taken = self.accepted_ids()
            clash = [f"{e} {r[self.model.entities[e].id_field]}" for e, rows in b.tables().items()
                     for r in rows if r.get(self.model.entities[e].id_field) in taken.get(e, set())]
            if clash:
                raise UploadError(f"Some ids were accepted in another batch meanwhile: {', '.join(clash[:5])}.")
        b.meta.update(status=decision, reviewer=reviewer.strip(), reason=reason.strip(),
                      decided=dt.datetime.now().replace(microsecond=0).isoformat())
        (b.path / "batch.json").write_text(json.dumps(b.meta, indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")
        return b

    # ------------------------------------------------------------ summaries (accepted data only)
    def accepted_tables(self) -> dict[str, list[dict[str, str]]]:
        out: dict[str, list[dict[str, str]]] = {}
        for b in self.batches("accepted"):
            for ent, rows in b.tables().items():
                out.setdefault(ent, []).extend(rows)
        return out

    def ko_usage(self) -> dict[str, dict[str, int]]:
        """KO ID -> {"Entity.field": rows that link to it}, over accepted batches."""
        usage: dict[str, Counter] = {}
        tables = self.accepted_tables()
        for ent_name, f in self.model.ko_fields():
            for r in tables.get(ent_name, []):
                v = r.get(f.name)
                if v:
                    usage.setdefault(v, Counter())[f"{ent_name}.{f.name}"] += 1
        return {k: dict(v) for k, v in usage.items()}


def _cell(v: Any) -> str:
    if v is None:
        return ""
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, float) and v.is_integer():
        return str(int(v))
    return str(v)


def small(n: int) -> str:
    """Counts below MIN_CELL are shown as '<5' (small groups can identify people)."""
    return f"<{MIN_CELL}" if 0 < n < MIN_CELL else str(n)
