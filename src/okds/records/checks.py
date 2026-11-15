"""Automatic checks for an uploaded batch of records: the data model's rules, and a privacy screen.

Errors stop the batch from being saved. Warnings are shown to the reviewer.
The privacy screen is a safety net, not a guarantee: whoever uploads must de-identify the data first
(see the "Before you upload" checklist on the Data skeleton page).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from .model import DataModel, Entity, Field

# Values that must never appear in de-identified records.
IDENTIFIER_PATTERNS = [
    ("an email address", re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")),
    ("a phone number", re.compile(r"(?<!\d)(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}(?!\d)")),
    ("a Social Security number", re.compile(r"(?<!\d)\d{3}-\d{2}-\d{4}(?!\d)")),
    ("a full date", re.compile(r"(?<!\d)(?:\d{4}[-/.]\d{1,2}[-/.]\d{1,2}|\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4})(?!\d)")),
    ("a record number", re.compile(r"\b(?:MRN|medical record|chart|acct|account)\b\s*#?:?\s*\w*\d", re.I)),
    ("a web address", re.compile(r"https?://|www\.", re.I)),
    ("a street address",
     re.compile(r"\b\d{1,5}\s+(?:[A-Z][a-z]+\s){1,3}(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Lane|Ln|Dr|Drive)\b")),
    ("an age (use an age band)", re.compile(r"\b(?:age[ds]?|aged)\s*:?\s*\d{1,3}\b|\b\d{1,3}[- ](?:year|yr)s?[- ]old\b", re.I)),
]
ID_RE = re.compile(r"[A-Za-z][A-Za-z0-9]{0,9}(?:[-_][A-Za-z0-9]{1,12}){0,3}")
LONG_NUMBER_RE = re.compile(r"\d{7,}")
KO_ID_RE = re.compile(r"KO-[A-Z]+-[A-Z]+-\d{3}")
TRUE, FALSE = {"true", "yes", "y", "1"}, {"false", "no", "n", "0"}


@dataclass
class Issue:
    level: str  # error | warning
    entity: str
    row: int | None
    field: str
    message: str

    def __str__(self) -> str:
        where = self.entity + (f" row {self.row}" if self.row is not None else "")
        where += f", {self.field}" if self.field else ""
        return f"{where}: {self.message}"


@dataclass
class CheckResult:
    issues: list[Issue] = field(default_factory=list)
    counts: dict[str, int] = field(default_factory=dict)
    clean: dict[str, list[dict[str, Any]]] = field(default_factory=dict)  # rows with typed values

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.level == "error"]

    @property
    def warnings(self) -> list[Issue]:
        return [i for i in self.issues if i.level == "warning"]

    @property
    def ok(self) -> bool:
        return not self.errors


def find_identifiers(text: str) -> list[str]:
    return [label for label, rx in IDENTIFIER_PATTERNS if rx.search(text or "")]


def _convert(f: Field, raw: Any) -> tuple[Any, str | None]:
    """(value, problem). Empty -> None."""
    if raw is None or (isinstance(raw, str) and not raw.strip()):
        return None, None
    s = str(raw).strip()
    if f.type in ("integer", "day", "year"):
        try:
            v = int(float(s))
            if float(s) != v:
                raise ValueError
        except ValueError:
            return None, f"'{s}' is not a whole number"
        if f.type == "year" and not 1900 <= v <= 2100:
            return None, f"{v} is not a year (only the year is kept, never a full date)"
        if f.type == "day" and not 0 <= v <= 3650:
            return None, f"day {v} is out of range (days since the rehabilitation started, 0-3650)"
    elif f.type == "number":
        try:
            v = float(s)
        except ValueError:
            return None, f"'{s}' is not a number"
    elif f.type == "boolean":
        if s.lower() not in TRUE | FALSE:
            return None, f"'{s}' is not yes/no"
        v = s.lower() in TRUE
    elif f.type == "category":
        match = next((x for x in f.values if x.lower() == s.lower()), None)
        if match is None:
            return None, f"'{s}' is not one of: {', '.join(f.values)}"
        v = match
    elif f.type == "ko":
        if not KO_ID_RE.fullmatch(s):
            return None, f"'{s}' is not a KO ID like KO-HAND-COND-001"
        v = s
    elif f.type in ("id", "ref"):
        if not ID_RE.fullmatch(s):
            return None, f"'{s}' is not a study code (letters, digits and dashes, e.g. P-0001)"
        v = s
    else:  # text
        v = s
        if f.max_length and len(s) > f.max_length:
            return None, f"text is longer than {f.max_length} characters"
    if f.type in ("integer", "number", "day") and isinstance(v, int | float):
        if f.min is not None and v < f.min:
            return None, f"{v} is below the minimum {f.min:g}"
        if f.max is not None and v > f.max:
            return None, f"{v} is above the maximum {f.max:g}"
    return v, None


def check_batch(model: DataModel, tables: dict[str, list[dict[str, Any]]], known_ids: dict[str, set[str]] | None = None,
                ko_types: dict[str, str] | None = None) -> CheckResult:
    """tables: entity name -> rows (dicts of column -> raw value).
    known_ids: ids already accepted in earlier batches (refs may point to them).
    ko_types: KO ID -> ko_type for every topic in the registry (ko fields must point to a real topic)."""
    res = CheckResult()
    known_ids = known_ids or {}
    err = lambda e, r, f, m: res.issues.append(Issue("error", e, r, f, m))  # noqa: E731
    warn = lambda e, r, f, m: res.issues.append(Issue("warning", e, r, f, m))  # noqa: E731

    for name in tables:
        if name not in model.entities:
            err(name, None, "", f"'{name}' is not part of the {model.name} model. Entities: {', '.join(model.entities)}.")
    ids: dict[str, set[str]] = {n: set(known_ids.get(n, set())) for n in model.entities}
    for name, rows in tables.items():
        ent = model.entities.get(name)
        if ent is None:
            continue
        _check_columns(ent, rows, err)
        clean_rows = []
        for i, row in enumerate(rows, 1):
            clean: dict[str, Any] = {}
            for fname, f in ent.fields.items():
                value, problem = _convert(f, row.get(fname))
                if problem:
                    err(name, i, fname, problem)
                elif value is None and (f.required or f.type == "id"):
                    err(name, i, fname, "is required")
                clean[fname] = value
            for col, raw in row.items():  # privacy screen on every cell, including ids and categories
                found = find_identifiers(str(raw or ""))
                if found:
                    err(name, i, col, f"looks like {found[0]}. Remove it: records must be de-identified.")
                elif col in ent.fields and ent.fields[col].type in ("id", "ref") and LONG_NUMBER_RE.search(str(raw or "")):
                    err(name, i, col, "a long number in a code may be a record number. Use a study code like P-0001.")
            rid = clean.get(ent.id_field)
            if rid is not None:
                if rid in {r.get(ent.id_field) for r in clean_rows}:
                    err(name, i, ent.id_field, f"'{rid}' is used twice in this upload")
                elif rid in known_ids.get(name, set()):
                    err(name, i, ent.id_field, f"'{rid}' was already accepted in an earlier batch")
                ids[name].add(rid)
            clean_rows.append(clean)
        res.clean[name] = clean_rows
        res.counts[name] = len(clean_rows)

    for name, rows in res.clean.items():  # references and KO links, now that every id is known
        ent = model.entities[name]
        for i, row in enumerate(rows, 1):
            for f in ent.fields.values():
                v = row.get(f.name)
                if v is None:
                    continue
                if f.type == "ref" and v not in ids.get(f.ref, set()):
                    err(name, i, f.name, f"points to {f.ref} '{v}', which is not in this upload or earlier ones")
                if f.type == "ko" and ko_types is not None:
                    if v not in ko_types:
                        warn(name, i, f.name, f"{v} is not in KO Topics yet (the link will show once the topic exists)")
                    elif f.ko_types and ko_types[v] not in f.ko_types:
                        err(name, i, f.name, f"{v} is a {ko_types[v]} KO; this field needs {' or '.join(f.ko_types)}")
    if not any(res.counts.values()):
        err("upload", None, "", "No rows found.")
    if res.counts.get(model.root, 0) and res.counts[model.root] < 5:
        warn(model.root, None, "", "Fewer than 5 people: summaries will show '<5' instead of numbers (small groups "
                                   "can identify people).")
    return res


def _check_columns(ent: Entity, rows: list[dict[str, Any]], err) -> None:
    cols = {c for r in rows for c in r}
    extra = sorted(c for c in cols if c not in ent.fields)
    if extra:
        err(ent.name, None, ", ".join(extra), f"unknown column(s). Only the model's columns are allowed "
                                              f"({', '.join(ent.fields)}), so nothing identifying slips in.")
