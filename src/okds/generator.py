"""KO Generator: builds a draft KO from one registry concept plus a source pack.

Two modes:
- template: a correct skeleton (no AI); a person writes the content.
- ai: the AI model (Claude or OpenAI) drafts the content ONLY from the source pack. The script then
  re-applies every field it owns (ID, cluster, sources, review status...).
"""

from __future__ import annotations

import datetime as dt
import re
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any

import yaml

from . import llm, vocab
from .config import PROMPTS_DIR
from .fetch import looks_like_bot_check
from .ko import (
    GENERATOR_PROMPT_VERSION,
    KODocument,
    KOFormatError,
    as_dict,
    as_list,
    build_body_skeleton,
    build_front_matter,
    parse_ko,
    refresh_references,
    render_ko,
)
from .registry import Concept, registry_summary

SOURCE_PACK_NEEDED = "SOURCE PACK NEEDED"
# Front matter fields the model may fill in; everything else comes from the skeleton.
MODEL_FIELDS = ["summary", "codes", "tags", "relationships", "proposed_concepts", "update_triggers"]


@dataclass
class KORequest:
    concept: Concept
    audience: list[str]
    reading_level: str
    difficulty: str
    sources: list[dict[str, Any]]  # source pack entries; each may carry a "text" field
    author: str
    license_name: str = "CC-BY-4.0"
    registry: dict[str, Concept] | None = None  # for link checks in finalize(); loaded from disk when None


def source_metadata(sources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Source entries as stored in the KO (the pack text is kept in the source pack file instead)."""
    return [{k: v for k, v in s.items() if k != "text" and v not in (None, "")} for s in sources]


def skeleton(req: KORequest, generated_by: dict[str, Any] | None = None) -> dict[str, Any]:
    return build_front_matter(
        req.concept,
        audience=req.audience,
        reading_level=req.reading_level,
        difficulty=req.difficulty,
        sources=source_metadata(req.sources),
        author=req.author,
        generated_by=generated_by,
        license_name=req.license_name,
    )


def template_draft(req: KORequest) -> str:
    front = skeleton(req)
    body = build_body_skeleton(req.concept.ko_type, req.audience, front["sources"])
    return render_ko(KODocument(front=front, body=body))


def render_source_pack(req: KORequest) -> str:
    """Source pack file (sources/packs/SP-<ko_id>.md): metadata plus the text the KO is built from."""
    lines = [f"# Source pack SP-{req.concept.ko_id} ({req.concept.preferred_term})", ""]
    for s in req.sources:
        lines.append(f"## {s.get('id')}")
        meta = {k: v for k, v in s.items() if k != "text"}
        lines.append(yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100).strip())
        lines.append("text: |")
        text = (s.get("text") or "").strip() or "<no text provided>"
        lines.extend("  " + line for line in text.split("\n"))
        lines.append("")
    return "\n".join(lines)


def system_prompt() -> str:
    prompt = (PROMPTS_DIR / "ko_generator.md").read_text(encoding="utf-8")
    return f"{prompt}\n\nVOCAB\n{vocab.vocab_for_prompt()}"


def user_prompt(req: KORequest, registry: dict[str, Concept]) -> str:
    gen_by = {"model": "<filled by script>", "prompt_version": GENERATOR_PROMPT_VERSION}
    front = skeleton(req, gen_by)
    core, subs = vocab.required_headings(req.concept.ko_type, req.audience)
    concept = {
        "ko_id": req.concept.ko_id,
        "preferred_term": req.concept.preferred_term,
        "alternate_terms": req.concept.alternate_terms,
        "ko_type": req.concept.ko_type,
        "specialty": req.concept.specialty,
        "audience": req.audience,
    }
    headings = "\n".join(f"## {h}" for h in core) + "\nUnder ## Explanation:\n" + "\n".join(f"### {s}" for s in subs)
    pack = []
    for s in req.sources:
        meta = yaml.safe_dump({k: v for k, v in s.items() if k != "text"}, sort_keys=False, allow_unicode=True)
        text = _defang_tags((s.get("text") or "").strip(), "source")
        pack.append(f'<source id="{s.get("id")}">\n{meta}text:\n{text}\n</source>')
    return (
        f"<concept>\n{yaml.safe_dump(concept, sort_keys=False, allow_unicode=True)}</concept>\n\n"
        f"<front_matter_skeleton>\n{yaml.safe_dump(front, sort_keys=False, allow_unicode=True)}</front_matter_skeleton>\n\n"
        f"<required_body_headings>\n{headings}\n</required_body_headings>\n\n"
        f"<registry>\n{registry_summary(registry)}\n</registry>\n\n"
        f"<source_pack>\n{chr(10).join(pack)}\n</source_pack>\n\n"
        f"Write the KO for {req.concept.ko_id} ({req.concept.preferred_term}) now."
    )


def check_pack(req: KORequest) -> list[str]:
    """Problems that make AI generation pointless (the guide requires at least 2 sources with text)."""
    problems = []
    with_text = [s for s in req.sources if (s.get("text") or "").strip()]
    if len(with_text) < 2:
        problems.append("Add at least 2 sources with text (paste or fetch the source text).")
    for s in req.sources:
        if not s.get("url") or not s.get("publisher") or not s.get("title"):
            problems.append(f"Source {s.get('id')} needs a title, publisher, and URL.")
        if s.get("permitted_use") == "restricted":
            problems.append(f"Source {s.get('id')} is 'restricted' and cannot be used.")
        if looks_like_bot_check(s.get("text") or ""):
            problems.append(f"Source {s.get('id')} text looks like a robot-check page, not the article. "
                            "Paste the real page text.")
    return problems


def _strip_fences(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        t = t.split("\n", 1)[1] if "\n" in t else ""
        if t.rstrip().endswith("```"):
            t = t.rstrip()[:-3]
    return t.strip()


def _defang_tags(text: str, tag: str) -> str:
    """Web text must not close (or open) our own <tag> blocks in the prompt."""
    return re.sub(rf"<(/?)\s*{tag}\b", r"‹\1" + tag, text, flags=re.I)


def finalize(raw: str, req: KORequest, model: str) -> tuple[str, list[str]]:
    """Re-apply script-owned fields to the model's draft. Returns (markdown, notes for the user)."""
    raw = _strip_fences(raw)
    if raw.startswith(SOURCE_PACK_NEEDED):
        return raw, ["The model says the source pack is not enough. Add more or better sources, then try again."]
    try:
        doc = parse_ko(raw)
    except KOFormatError as e:
        return raw, [f"The draft could not be parsed ({e}). Fix it by hand in the editor."]

    try:
        return _finalize_doc(doc, req, model)
    except Exception as e:  # never lose a paid draft: hand back the raw text to fix by hand
        return raw, [f"The draft has an unexpected format ({type(e).__name__}: {e}). Fix it by hand in the editor."]


def registry_of(req: KORequest) -> dict[str, Concept]:
    """The registry the request was made with (set by the caller), else the one on disk."""
    if req.registry is not None:
        return req.registry
    from .config import get_settings
    from .registry import load_registry
    return load_registry(get_settings().registry_path)


def _clean_links(raw, req: KORequest, registry: dict[str, Concept]) -> tuple[list[dict], list[str]]:
    """Keep links that follow the rules (from this KO, known target, allowed types); fill in missing labels.
    Other links are moved to review.open_issues with the reason, so a person can decide."""
    kept, moved = [], []
    me = req.concept
    for rel in as_list(raw):
        if not isinstance(rel, dict):
            continue
        pred, target = str(rel.get("predicate", "")), str(rel.get("target_id", ""))
        subject = str(rel.get("subject_id") or me.ko_id)
        sources = [str(x) for x in as_list(rel.get("source_ids"))]
        where = f"{pred} -> {target} ({', '.join(sources) or 'no sources'})"
        concept = registry.get(target)
        if subject != me.ko_id:
            moved.append(f"Link to add in {subject}'s KO: {subject} {pred} {me.ko_id} ({', '.join(sources)}).")
            continue
        if target == me.ko_id:
            moved.append(f"Removed a link from this KO to itself: {where}.")
            continue
        if concept is None and not vocab.object_is_entity_record(pred):
            moved.append(f"Link target {target} is not in KO Topics: {where}. Add the topic, or use proposed_concepts.")
            continue
        if concept is not None and vocab.predicate_allows(pred, me.ko_type, concept.ko_type) is False:
            moved.append(f"{pred} does not allow {me.ko_type} -> {concept.ko_type}: {where}.")
            continue
        clean = {"predicate": pred, "target_id": target,
                 "target_label": str(rel.get("target_label") or (concept.preferred_term if concept else target)),
                 "source_ids": sources}
        kept.append(clean)
    return kept, moved


def _finalize_doc(doc: KODocument, req: KORequest, model: str) -> tuple[str, list[str]]:
    notes: list[str] = []
    front = skeleton(req, {"model": model, "prompt_version": GENERATOR_PROMPT_VERSION})
    for key in MODEL_FIELDS:
        if key in doc.front and doc.front[key] not in (None, ""):
            front[key] = doc.front[key]
    # Keep registry codes when the registry has them.
    codes = dict(as_dict(front.get("codes")))
    if req.concept.mesh_id:
        codes["mesh"] = req.concept.mesh_id
    if req.concept.icd10cm:
        codes["icd10cm"] = req.concept.icd10cm
    front["codes"] = codes
    model_alt = as_list(doc.front.get("alternate_terms"))  # a single string stays one term
    front["alternate_terms"] = list(dict.fromkeys([*req.concept.alternate_terms, *map(str, model_alt)]))
    model_review = as_dict(doc.front.get("review"))
    front["review"]["author"] = "KO Generator"
    front["review"]["open_issues"] = [str(i) for i in as_list(model_review.get("open_issues"))]
    front["relationships"], moved = _clean_links(front.get("relationships"), req, registry_of(req))
    if moved:
        front["review"]["open_issues"].extend(moved)
        notes.append(f"{len(moved)} link(s) did not follow the link rules; they are listed in review.open_issues.")
    front["change_log"] = [{
        "version": "0.1.0",
        "date": dt.date.today().isoformat(),
        "by": "KO Generator",
        "change": f"Initial AI draft from source pack SP-{req.concept.ko_id} ({model}, {GENERATOR_PROMPT_VERSION}).",
    }]
    if doc.front.get("ko_id") not in (None, req.concept.ko_id):
        notes.append(f"The model changed ko_id to {doc.front.get('ko_id')}; it was reset to {req.concept.ko_id}.")
    if model_review.get("status") not in (None, "draft"):
        notes.append("The model tried to set a review status; it was reset to 'draft'.")
    final = refresh_references(KODocument(front=front, body=doc.body))
    return render_ko(final), notes


def ai_draft_stream(req: KORequest, registry: dict[str, Concept], model: str, effort: str,
                    result: llm.StreamResult, provider: str = "claude") -> Iterator[str]:
    """Stream the raw model text. After it finishes, call finalize(result.text, ...)."""
    req.registry = registry  # finalize() checks the links against the same registry
    yield from llm.stream_text(
        model=model, system=system_prompt(), user=user_prompt(req, registry), effort=effort, result=result,
        provider=provider,
    )
