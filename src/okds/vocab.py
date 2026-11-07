"""Load the controlled vocabulary (schema/vocab.yaml) and answer simple questions about it."""

from __future__ import annotations

import json
from functools import lru_cache
from typing import Any

import yaml

from .config import SCHEMA_DIR


@lru_cache(maxsize=1)
def load_vocab() -> dict[str, Any]:
    return yaml.safe_load((SCHEMA_DIR / "vocab.yaml").read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def load_ko_schema() -> dict[str, Any]:
    return json.loads((SCHEMA_DIR / "ko.schema.json").read_text(encoding="utf-8"))


def ko_types() -> list[str]:
    return list(load_vocab()["ko_types"])


def type_code(ko_type: str) -> str:
    return load_vocab()["ko_types"][ko_type]["code"]


def cluster_for(ko_type: str) -> int:
    return int(load_vocab()["ko_types"][ko_type]["cluster"])


def specialties() -> dict[str, str]:
    return dict(load_vocab()["enums"]["specialty"])


def enum(name: str) -> list[str]:
    values = load_vocab()["enums"][name]
    return list(values) if not isinstance(values, dict) else list(values.keys())


def predicates() -> dict[str, dict[str, Any]]:
    return load_vocab()["predicates"]


def required_headings(ko_type: str, audience: list[str]) -> tuple[list[str], list[str]]:
    """Return (core `##` headings in order, `###` subsections required under Explanation)."""
    h = load_vocab()["headings"]
    core = list(h["core"])
    if not set(audience or []) & set(h["patient_audiences"]):
        core.remove(h["patient_only_heading"])
    return core, list(h["explanation_subsections"].get(ko_type, []))


def predicate_allows(predicate: str, subject_type: str, object_type: str | None) -> bool | None:
    """True/False if the vocab says the link is allowed; None if the object type is unknown."""
    spec = predicates().get(predicate)
    if spec is None:
        return False
    subj = spec["subject"]
    if subj != "any" and subject_type not in subj:
        return False
    if object_type is None:
        return None
    obj = spec["object"]
    if obj == "any":
        return True
    if obj == "same":
        return object_type == subject_type
    return object_type in obj


def object_is_entity_record(predicate: str) -> bool:
    """True if the predicate points at API entity records (Guideline, Organization...), not KOs."""
    spec = predicates().get(predicate) or {}
    obj = spec.get("object")
    entity_types = set(load_vocab()["entity_record_types"])
    return isinstance(obj, list) and bool(obj) and set(obj) <= entity_types


def vocab_for_prompt() -> str:
    """A compact text version of the vocab for the generator prompt (stable, so it caches well)."""
    v = load_vocab()
    lines = ["KO TYPES (ko_type: id code, cluster):"]
    lines += [f"- {t}: {d['code']}, cluster {d['cluster']} ({d['description']})" for t, d in v["ko_types"].items()]
    lines.append("\nALLOWED PREDICATES (subject -> object):")
    for p, d in v["predicates"].items():
        subj = d["subject"] if isinstance(d["subject"], str) else "/".join(d["subject"])
        obj = d["object"] if isinstance(d["object"], str) else "/".join(d["object"])
        lines.append(f"- {p}: {subj} -> {obj} ({d['meaning']})")
    lines.append(f"\nFORBIDDEN PREDICATES: {', '.join(v['forbidden_predicates'])}")
    e = v["enums"]
    lines.append("\nENUMS:")
    lines.append(f"- specialty: {', '.join(e['specialty'])}")
    for name in ("audience", "difficulty", "source_type", "permitted_use"):
        lines.append(f"- {name}: {', '.join(map(str, e[name]))}")
    lines.append("- review.status: the generator may only use: draft")
    return "\n".join(lines)
