"""KO file format (okds-ko-1.0): Markdown with a YAML front matter block.

Markdown is the source of truth. JSON is a build artifact made from it (never edit the JSON).
"""

from __future__ import annotations

import datetime as dt
import re
from dataclasses import dataclass
from typing import Any

import yaml

from . import vocab

SCHEMA_VERSION = "okds-ko-1.0"
GENERATOR_PROMPT_VERSION = "okds-gen-1.1"  # 1.1: source text is data, not instructions
TEMPLATE_VERSION = "okds-template-1.0"

FIELD_ORDER = [
    "schema_version", "ko_id", "title", "preferred_term", "alternate_terms", "ko_type", "specialty",
    "cluster", "audience", "reading_level", "difficulty", "summary", "codes", "tags", "relationships",
    "proposed_concepts", "sources", "review", "safety", "version", "created", "last_updated",
    "update_triggers", "license", "change_log",
]
SOURCE_FIELD_ORDER = [
    "id", "title", "publisher", "url", "source_type", "audience", "publication_date",
    "retrieved_date", "permitted_use", "evidence_strength", "notes",
]
TODO = "TODO"
MARKER_RE = re.compile(r"\[(S\d+)\]")
_FRONT_RE = re.compile(r"\A\s*---\s*\n(.*?)\n---\s*(?:\n|\Z)(.*)\Z", re.S)


class KOFormatError(ValueError):
    pass


@dataclass
class KODocument:
    front: dict[str, Any]
    body: str

    @property
    def ko_id(self) -> str:
        return str(self.front.get("ko_id", ""))


def _normalize(value: Any) -> Any:
    """Turn YAML dates into ISO strings so the data is JSON-safe on every machine."""
    if isinstance(value, dt.datetime | dt.date):
        return value.isoformat()[:10]
    if isinstance(value, dict):
        return {str(k): _normalize(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_normalize(v) for v in value]
    return value


def as_dict(value: Any) -> dict[str, Any]:
    """A front matter field that should be a mapping (e.g. review, codes). Anything else -> {}."""
    return value if isinstance(value, dict) else {}


def as_list(value: Any) -> list[Any]:
    """A field that should be a list (sources, tags, ...). A single value becomes a one-item list."""
    if isinstance(value, list):
        return value
    return [] if value in (None, "") else [value]


def parse_ko(text: str) -> KODocument:
    text = text.replace("\r\n", "\n").lstrip("﻿")
    m = _FRONT_RE.match(text)
    if not m:
        raise KOFormatError("The file must start with a YAML front matter block between two '---' lines.")
    try:
        front = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        raise KOFormatError(f"The YAML front matter does not parse: {e}") from e
    if not isinstance(front, dict):
        raise KOFormatError("The YAML front matter must be a mapping of fields.")
    return KODocument(front=_normalize(front), body=m.group(2).strip("\n"))


def _ordered(front: dict[str, Any]) -> dict[str, Any]:
    out = {k: front[k] for k in FIELD_ORDER if k in front}
    out.update({k: v for k, v in front.items() if k not in out})
    if isinstance(out.get("sources"), list):
        out["sources"] = [
            {**{k: s[k] for k in SOURCE_FIELD_ORDER if k in s}, **{k: v for k, v in s.items() if k not in SOURCE_FIELD_ORDER}}
            for s in out["sources"]
            if isinstance(s, dict)
        ]
    return out


def render_ko(doc: KODocument) -> str:
    front_yaml = yaml.safe_dump(_ordered(doc.front), sort_keys=False, allow_unicode=True, width=100)
    return f"---\n{front_yaml}---\n\n{doc.body.strip()}\n"


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:60] or "ko"


def ko_relpath(front: dict[str, Any]) -> str:
    """kos/<specialty>/<ko_id>_<slug>.md, always with forward slashes."""
    specialty = str(front.get("specialty", "gen")).lower()
    slug = slugify(str(front.get("preferred_term") or front.get("title") or ""))
    return f"{specialty}/{front.get('ko_id', 'KO-UNKNOWN')}_{slug}.md"


def iter_sections(body: str) -> list[tuple[str, str | None, str]]:
    """Split the body into (## heading, ### heading or None, text) chunks, skipping fenced code."""
    chunks: list[tuple[str, str | None, str]] = []
    h2: str | None = None
    h3: str | None = None
    buf: list[str] = []
    in_code = False

    def flush() -> None:
        if h2 is not None:
            chunks.append((h2, h3, "\n".join(buf).strip()))

    for line in body.replace("\r\n", "\n").split("\n"):
        if line.strip().startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith("## "):
            flush()
            h2, h3, buf = line[3:].strip(), None, []
        elif not in_code and line.startswith("### ") and h2 is not None:
            flush()
            h3, buf = line[4:].strip(), []
        else:
            buf.append(line)
    flush()
    return chunks


def heading_key(heading: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", heading.lower().replace("→", " to ")).strip("_")


def normalize_heading(heading: str) -> str:
    return re.sub(r"\s+", " ", heading.replace("->", "→").strip().lower())


def body_without_references(body: str) -> str:
    """Body text excluding the References section (which lists every source by design)."""
    parts = []
    for h2, h3, text in iter_sections(body):
        if normalize_heading(h2) == "references":
            continue
        parts.append(f"{h3 or h2}\n{text}")
    return "\n".join(parts)


def used_markers(doc: KODocument) -> set[str]:
    text = body_without_references(doc.body) + "\n" + str(doc.front.get("summary", ""))
    return set(MARKER_RE.findall(text))


def to_json_record(doc: KODocument, source_file: str) -> dict[str, Any]:
    sections: dict[str, Any] = {}
    for h2, h3, text in iter_sections(doc.body):
        entry = sections.setdefault(heading_key(h2), {"heading": h2, "text": "", "subsections": {}})
        if h3 is None:
            entry["text"] = text
        else:
            entry["subsections"][heading_key(h3)] = {"heading": h3, "text": text}
    return {
        **_ordered(doc.front),
        "sections": sections,
        "raw_markdown": render_ko(doc),
        "source_file": source_file,
        "built_at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
    }


# ---------- building new KOs ----------


def reference_lines(sources: list[dict[str, Any]]) -> str:
    lines = []
    for i, s in enumerate(sources, 1):
        lines.append(
            f"{i}. [{s.get('id')}] {s.get('publisher', '')}. *{s.get('title', '')}.* {s.get('url', '')} "
            f"(retrieved {s.get('retrieved_date', '')})"
        )
    return "\n".join(lines)


def build_front_matter(
    concept: Any,
    *,
    audience: list[str],
    reading_level: str,
    difficulty: str,
    sources: list[dict[str, Any]],
    author: str,
    generated_by: dict[str, Any] | None,
    license_name: str = "CC-BY-4.0",
    today: str | None = None,
) -> dict[str, Any]:
    """Front matter with every field the script owns (ID, cluster, sources, review status...) filled in."""
    today = today or dt.date.today().isoformat()
    codes = {"mesh": concept.mesh_id or "<verify>", "icd10cm": concept.icd10cm or "<verify>"}
    return {
        "schema_version": SCHEMA_VERSION,
        "ko_id": concept.ko_id,
        "title": concept.preferred_term,
        "preferred_term": concept.preferred_term,
        "alternate_terms": list(concept.alternate_terms),
        "ko_type": concept.ko_type,
        "specialty": concept.specialty,
        "cluster": vocab.cluster_for(concept.ko_type),
        "audience": list(audience),
        "reading_level": reading_level,
        "difficulty": difficulty,
        "summary": f"{TODO}: write a 1-3 sentence definition of {concept.preferred_term}, with source markers like [S1].",
        "codes": codes,
        "tags": [],
        "relationships": [],
        "proposed_concepts": [],
        "sources": [dict(s) for s in sources],
        "review": {
            "status": "draft",
            "author": author or "<verify>",
            "generated_by": generated_by or {"model": None, "prompt_version": TEMPLATE_VERSION},
            "ai_check": None,
            "team_checker": None,
            "clinician_reviewer": None,
            "clinician_role": None,
            "review_date": None,
            "open_issues": [],
        },
        "safety": {"not_medical_advice": True, "scope_note": "General education only. Not a diagnosis or treatment plan."},
        "version": "0.1.0",
        "created": today,
        "last_updated": today,
        "update_triggers": ["Any cited page shows a new 'last reviewed' date."],
        "license": license_name,
        "change_log": [{"version": "0.1.0", "date": today, "by": author or "KO Generator", "change": "Initial draft."}],
    }


def build_body_skeleton(ko_type: str, audience: list[str], sources: list[dict[str, Any]]) -> str:
    """Body with every required heading and TODO notes. References are filled from the sources."""
    core, subsections = vocab.required_headings(ko_type, audience)
    hints = {
        "Summary": "write 2-4 plain sentences. End every factual sentence with a source marker like [S1].",
        "Key Facts (claim → source)": "4-10 bullets. Each bullet is one claim followed by its marker, e.g. '... [S1].'",
        "Common Misunderstandings": "2-5 pairs: **Myth:** ... **Fact:** ... [S1]",
        "Questions to Ask Your Doctor": "3-6 questions a patient could ask.",
        "Test Questions": "3-6 questions with short answers and markers, e.g. '1. Question? - Answer [S1].'",
        "Related Topics": "a readable list that mirrors `relationships` in the front matter.",
    }
    parts = []
    for heading in core:
        parts.append(f"## {heading}")
        if heading == "Explanation":
            for sub in subsections:
                parts.append(f"### {sub}\n{TODO}: write this part from the sources, with markers like [S1].\n")
        elif heading == "References":
            parts.append(reference_lines(sources) + "\n")
        elif heading == "Key Facts (claim → source)":
            parts.append(f"- {TODO}: {hints[heading]}\n")
        else:
            parts.append(f"{TODO}: {hints.get(heading, 'write this section.')}\n")
    return "\n".join(parts).strip()


def refresh_references(doc: KODocument) -> KODocument:
    """Rewrite the References section from `sources`, so the two always match."""
    sources = [s for s in as_list(doc.front.get("sources")) if isinstance(s, dict)]
    out, skipping = [], False
    for line in doc.body.split("\n"):
        if line.startswith("## "):
            skipping = normalize_heading(line[3:]) == "references"
            out.append(line)
            if skipping:
                out.append(reference_lines(sources))
            continue
        if not skipping:
            out.append(line)
    return KODocument(front=doc.front, body="\n".join(out))
