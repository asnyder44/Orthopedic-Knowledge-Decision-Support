"""Data models for the data skeleton: which entities a dataset has, their fields, and how they connect.

Models are YAML files: the built-in ones in src/okds/datamodels/, plus any a team adds in
data/models/<name>.yaml (same format; see src/okds/datamodels/rehab.yaml).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from ..config import PACKAGE_DIR, get_settings

BUILTIN_DIR = PACKAGE_DIR / "datamodels"
FIELD_TYPES = {"id", "ref", "ko", "text", "category", "integer", "number", "boolean", "day", "year"}


class ModelError(ValueError):
    """The model file itself is wrong (shown to whoever wrote it)."""


@dataclass
class Field:
    name: str
    type: str
    required: bool = False
    description: str = ""
    ref: str = ""             # ref: the entity it points to
    predicate: str = ""       # ref / ko: the arrow label in the flow diagram
    edge: str = "in"          # ref: "in" = referenced -> this entity, "out" = this entity -> referenced
    values: list[str] = field(default_factory=list)   # category
    ko_types: list[str] = field(default_factory=list)  # ko
    min: float | None = None
    max: float | None = None
    max_length: int | None = None
    unit: str = ""
    free_text: bool = False


@dataclass
class Entity:
    name: str
    fields: dict[str, Field]
    description: str = ""

    @property
    def id_field(self) -> str:
        return next(f.name for f in self.fields.values() if f.type == "id")

    @property
    def refs(self) -> list[Field]:
        return [f for f in self.fields.values() if f.type == "ref"]


@dataclass
class DataModel:
    name: str
    title: str
    version: str
    description: str
    root: str
    entities: dict[str, Entity]
    source: str = ""

    def edges(self) -> list[dict[str, str]]:
        """Diagram arrows: {from, to, predicate, field}. `in` refs point from the referenced entity to this one."""
        out = []
        for e in self.entities.values():
            for f in e.refs:
                a, b = (f.ref, e.name) if f.edge == "in" else (e.name, f.ref)
                out.append({"from": a, "to": b, "predicate": f.predicate or f.name.upper(), "field": f"{e.name}.{f.name}"})
        return out

    def ko_fields(self) -> list[tuple[str, Field]]:
        return [(e.name, f) for e in self.entities.values() for f in e.fields.values() if f.type == "ko"]

    def to_json(self) -> dict[str, Any]:
        return {"name": self.name, "title": self.title, "version": self.version, "description": self.description,
                "root": self.root, "edges": self.edges(),
                "entities": {n: {"description": e.description, "id_field": e.id_field,
                                 "fields": {k: {kk: vv for kk, vv in f.__dict__.items() if vv not in (None, "", [], False)}
                                            for k, f in e.fields.items()}} for n, e in self.entities.items()}}


def _parse(raw: dict[str, Any], source: str) -> DataModel:
    if not isinstance(raw, dict) or not raw.get("model") or not isinstance(raw.get("entities"), dict):
        raise ModelError(f"{source}: a model needs 'model' (its name) and 'entities'.")
    entities: dict[str, Entity] = {}
    for ename, spec in raw["entities"].items():
        fields = {}
        for fname, f in (spec or {}).get("fields", {}).items():
            f = dict(f or {})
            ftype = f.pop("type", None)
            if ftype not in FIELD_TYPES:
                raise ModelError(f"{source}: {ename}.{fname} has unknown type '{ftype}'. Use one of {sorted(FIELD_TYPES)}.")
            unknown = set(f) - set(Field.__dataclass_fields__)
            if unknown:
                raise ModelError(f"{source}: {ename}.{fname} has unknown settings {sorted(unknown)}.")
            fields[fname] = Field(name=fname, type=ftype, **f)
        if sum(f.type == "id" for f in fields.values()) != 1:
            raise ModelError(f"{source}: entity {ename} needs exactly one field of type id.")
        entities[ename] = Entity(ename, fields, str((spec or {}).get("description", "")).strip())
    for e in entities.values():
        for f in e.refs:
            if f.ref not in entities:
                raise ModelError(f"{source}: {e.name}.{f.name} points to '{f.ref}', which is not an entity.")
            if f.edge not in ("in", "out"):
                raise ModelError(f"{source}: {e.name}.{f.name} edge must be 'in' or 'out'.")
    root = str(raw.get("root") or next(iter(entities)))
    if root not in entities:
        raise ModelError(f"{source}: root '{root}' is not an entity.")
    return DataModel(name=str(raw["model"]), title=str(raw.get("title") or raw["model"]), version=str(raw.get("version", "")),
                     description=" ".join(str(raw.get("description", "")).split()), root=root, entities=entities,
                     source=source)


def _model_files() -> list[Path]:
    files = sorted(BUILTIN_DIR.glob("*.yaml"))
    team_dir = get_settings().data_dir / "models"
    if team_dir.is_dir():
        files += sorted(team_dir.glob("*.yaml"))
    return files


@lru_cache(maxsize=16)
def _load(path: str, mtime: float) -> DataModel:
    p = Path(path)
    return _parse(yaml.safe_load(p.read_text(encoding="utf-8")), p.name)


def models() -> dict[str, DataModel]:
    """Every model that loads. A broken team model is skipped here; `model_errors()` says why."""
    out = {}
    for p in _model_files():
        try:
            m = _load(str(p), p.stat().st_mtime)
        except (ModelError, yaml.YAMLError):
            continue
        out.setdefault(m.name, m)
    return out


def model_errors() -> list[str]:
    errors = []
    for p in _model_files():
        try:
            _load(str(p), p.stat().st_mtime)
        except (ModelError, yaml.YAMLError) as e:
            errors.append(str(e))
    return errors


def get_model(name: str) -> DataModel:
    m = models().get(name)
    if m is None:
        raise ModelError(f"No data model '{name}'. Models: {', '.join(models()) or 'none'}.")
    return m
