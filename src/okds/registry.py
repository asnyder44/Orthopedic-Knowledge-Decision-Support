"""Concept registry (data/registry.csv). IDs are assigned here by code, never by the LLM."""

from __future__ import annotations

import csv
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

from . import vocab

FIELDS = ["ko_id", "preferred_term", "alternate_terms", "ko_type", "specialty", "mesh_id", "icd10cm", "status"]
STATUSES = ["planned", "drafted", "retired"]


@dataclass
class Concept:
    ko_id: str
    preferred_term: str
    ko_type: str
    specialty: str
    alternate_terms: list[str] = field(default_factory=list)
    mesh_id: str = ""
    icd10cm: str = ""
    status: str = "planned"

    def to_row(self) -> dict[str, str]:
        row = asdict(self)
        row["alternate_terms"] = "; ".join(self.alternate_terms)
        return row


def _split_terms(text: str) -> list[str]:
    return [t.strip() for t in (text or "").split(";") if t.strip()]


def load_registry(path: Path) -> dict[str, Concept]:
    if not path.is_file():
        return {}
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    concepts: dict[str, Concept] = {}
    for r in rows:
        if not (r.get("ko_id") or "").strip():
            continue
        c = Concept(
            ko_id=r["ko_id"].strip(),
            preferred_term=(r.get("preferred_term") or "").strip(),
            ko_type=(r.get("ko_type") or "").strip(),
            specialty=(r.get("specialty") or "").strip(),
            alternate_terms=_split_terms(r.get("alternate_terms", "")),
            mesh_id=(r.get("mesh_id") or "").strip(),
            icd10cm=(r.get("icd10cm") or "").strip(),
            status=(r.get("status") or "planned").strip(),
        )
        concepts[c.ko_id] = c
    return concepts


def save_registry(path: Path, concepts: dict[str, Concept]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for c in sorted(concepts.values(), key=lambda c: c.ko_id):
            writer.writerow(c.to_row())


def next_id(concepts: dict[str, Concept], specialty: str, ko_type: str) -> str:
    """Next free ID like KO-HAND-COND-003. Retired IDs are never reused."""
    prefix = f"KO-{specialty}-{vocab.type_code(ko_type)}-"
    pattern = re.compile(re.escape(prefix) + r"(\d{3})$")
    used = [int(m.group(1)) for cid in concepts if (m := pattern.match(cid))]
    n = max(used, default=0) + 1
    if n > 999:
        raise ValueError(f"No IDs left for {prefix}NNN")
    return f"{prefix}{n:03d}"


def find_duplicate(concepts: dict[str, Concept], term: str, alternate_terms: list[str]) -> Concept | None:
    """One concept = one name. Return an existing concept that already uses one of these names."""
    wanted = {t.strip().lower() for t in [term, *alternate_terms] if t.strip()}
    for c in concepts.values():
        names = {c.preferred_term.lower(), *(a.lower() for a in c.alternate_terms)}
        if wanted & names:
            return c
    return None


def add_concept(
    path: Path,
    preferred_term: str,
    ko_type: str,
    specialty: str,
    alternate_terms: list[str] | None = None,
    mesh_id: str = "",
    icd10cm: str = "",
) -> Concept:
    preferred_term = preferred_term.strip()
    if not preferred_term:
        raise ValueError("Preferred term is required.")
    if ko_type not in vocab.ko_types():
        raise ValueError(f"Unknown KO type: {ko_type}")
    if specialty not in vocab.specialties():
        raise ValueError(f"Unknown specialty: {specialty}")
    concepts = load_registry(path)
    alternate_terms = [t.strip() for t in (alternate_terms or []) if t.strip()]
    dup = find_duplicate(concepts, preferred_term, alternate_terms)
    if dup:
        raise ValueError(f"'{preferred_term}' overlaps with existing concept {dup.ko_id} ({dup.preferred_term}).")
    concept = Concept(
        ko_id=next_id(concepts, specialty, ko_type),
        preferred_term=preferred_term,
        ko_type=ko_type,
        specialty=specialty,
        alternate_terms=alternate_terms,
        mesh_id=mesh_id.strip(),
        icd10cm=icd10cm.strip(),
    )
    concepts[concept.ko_id] = concept
    save_registry(path, concepts)
    return concept


def set_status(path: Path, ko_id: str, status: str) -> None:
    if status not in STATUSES:
        raise ValueError(f"Unknown registry status: {status}")
    concepts = load_registry(path)
    if ko_id in concepts and concepts[ko_id].status != status:
        concepts[ko_id].status = status
        save_registry(path, concepts)


def registry_summary(concepts: dict[str, Concept]) -> str:
    """Compact list of valid link targets for the generator prompt."""
    return "\n".join(f"{c.ko_id} | {c.preferred_term} | {c.ko_type}" for c in sorted(concepts.values(), key=lambda c: c.ko_id))
