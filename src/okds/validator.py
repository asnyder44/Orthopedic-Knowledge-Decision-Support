"""Automatic checks before review and before loading (docs/reference/knowledge-object-guide.md §9)."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from jsonschema import Draft202012Validator

from . import vocab
from .ko import TODO, KODocument, KOFormatError, as_dict, as_list, iter_sections, normalize_heading, parse_ko, used_markers
from .registry import Concept

ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
VERIFY = "<verify>"


@dataclass
class Issue:
    level: str  # "error" blocks saving as valid; "warning" blocks publishing
    check: str
    message: str


@dataclass
class ValidationResult:
    issues: list[Issue]

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.level == "error"]

    @property
    def warnings(self) -> list[Issue]:
        return [i for i in self.issues if i.level == "warning"]

    @property
    def ok(self) -> bool:
        return not self.errors


def validate_text(
    text: str,
    registry: dict[str, Concept],
    other_files: dict[str, str] | None = None,
    this_file: str | None = None,
) -> ValidationResult:
    try:
        doc = parse_ko(text)
    except KOFormatError as e:
        return ValidationResult([Issue("error", "1 front matter", str(e))])
    return validate_doc(doc, registry, other_files, this_file)


def validate_doc(
    doc: KODocument,
    registry: dict[str, Concept],
    other_files: dict[str, str] | None = None,
    this_file: str | None = None,
) -> ValidationResult:
    """other_files maps ko_id -> file path for the rest of the library (for the uniqueness check)."""
    issues: list[Issue] = []
    err = lambda check, msg: issues.append(Issue("error", check, msg))  # noqa: E731
    warn = lambda check, msg: issues.append(Issue("warning", check, msg))  # noqa: E731
    f = doc.front

    # 1. schema version
    if f.get("schema_version") != "okds-ko-1.0":
        err("1 schema version", "schema_version must be 'okds-ko-1.0'.")

    # 2. JSON Schema (required fields, types, enums)
    for e in sorted(Draft202012Validator(vocab.load_ko_schema()).iter_errors(f), key=lambda e: list(e.path)):
        where = ".".join(str(p) for p in e.absolute_path) or "(front matter)"
        err("2 field format", f"{where}: {e.message}")

    ko_id = str(f.get("ko_id", ""))
    ko_type = f.get("ko_type")

    # 3. registry match
    concept = registry.get(ko_id)
    if concept is None:
        err("3 registry", f"{ko_id or '(no ko_id)'} is not in the concept registry. Add the concept first.")
    else:
        for field in ("preferred_term", "ko_type", "specialty"):
            if str(f.get(field, "")) != str(getattr(concept, field)):
                err("3 registry", f"{field} is '{f.get(field)}' but the registry says '{getattr(concept, field)}'.")

    # 4. unique ID across the library
    if other_files and ko_id in other_files and other_files[ko_id] != this_file:
        err("4 unique ID", f"{ko_id} is already used by {other_files[ko_id]}.")

    # 5. cluster from rule
    if ko_type in vocab.ko_types() and f.get("cluster") != vocab.cluster_for(ko_type):
        err("5 cluster", f"cluster must be {vocab.cluster_for(ko_type)} for {ko_type}.")

    # 6 + 7. relationships
    forbidden = {p.upper() for p in vocab.load_vocab()["forbidden_predicates"]}
    source_ids = {str(s.get("id")) for s in as_list(f.get("sources")) if isinstance(s, dict)}
    for rel in as_list(f.get("relationships")):
        if not isinstance(rel, dict):
            continue
        pred, target = str(rel.get("predicate", "")), str(rel.get("target_id", ""))
        if pred.upper() in forbidden:
            err("7 forbidden link", f"{pred} is not allowed. Use a meaningful predicate from vocab.yaml.")
            continue
        if pred not in vocab.predicates():
            err("6 links", f"Unknown predicate '{pred}'.")
            continue
        for sid in as_list(rel.get("source_ids")):
            if str(sid) not in source_ids:
                err("6 links", f"{pred} -> {target} cites {sid}, which is not in sources.")
        if vocab.object_is_entity_record(pred):
            warn("6 links", f"{pred} -> {target} points to an entity record; entity records are not checked yet.")
            continue
        target_concept = registry.get(target)
        if target_concept is None:
            err("6 links", f"{pred} target {target} is not in the registry. Put new concepts in proposed_concepts.")
            continue
        if ko_type and vocab.predicate_allows(pred, ko_type, target_concept.ko_type) is False:
            err("6 links", f"{pred} does not allow {ko_type} -> {target_concept.ko_type} ({target}).")
    for pc in as_list(f.get("proposed_concepts")):
        pred = str(pc.get("predicate", "")) if isinstance(pc, dict) else ""
        if pred.upper() in forbidden:
            err("7 forbidden link", f"proposed_concepts uses {pred}. Use a meaningful predicate from vocab.yaml.")
        elif pred and pred not in vocab.predicates():
            err("6 links", f"proposed_concepts uses unknown predicate '{pred}'.")
    raw_text = str(f) + doc.body

    # 8. source markers
    markers = used_markers(doc)
    for m in sorted(markers - source_ids):
        err("8 source markers", f"[{m}] is used in the text but there is no source {m}.")
    for s in sorted(source_ids - markers):
        err("8 source markers", f"Source {s} is never cited in the text. Cite it or remove it.")
    for h2, h3, text in iter_sections(doc.body):
        if normalize_heading(h2).startswith("key facts") and h3 is None:
            for line in text.split("\n"):
                if line.strip().startswith(("- ", "* ")) and TODO not in line and not re.search(r"\[S\d+\]", line):
                    err("8 source markers", f"Key fact has no source marker: {line.strip()[:80]}")

    # 9 + 10. sources
    for s in as_list(f.get("sources")):
        if not isinstance(s, dict):
            continue
        sid = s.get("id", "?")
        for field in ("url", "publisher", "retrieved_date", "permitted_use"):
            if not s.get(field):
                err("9 sources", f"Source {sid} is missing {field}.")
        if s.get("permitted_use") == "restricted":
            err("10 permitted use", f"Source {sid} is 'restricted' and cannot be used.")
        if s.get("retrieved_date") and not ISO_DATE.match(str(s["retrieved_date"])):
            err("12 dates", f"Source {sid} retrieved_date must be YYYY-MM-DD.")

    # 11. required headings in order
    core, subs = vocab.required_headings(str(ko_type), [str(a) for a in as_list(f.get("audience"))])
    sections = iter_sections(doc.body)
    h2_seen = [normalize_heading(h2) for h2, h3, _ in sections if h3 is None]
    positions = []
    for heading in core:
        key = normalize_heading(heading)
        if key not in h2_seen:
            err("11 headings", f"Missing heading '## {heading}'.")
        else:
            positions.append(h2_seen.index(key))
    if positions != sorted(positions):
        err("11 headings", "Required headings are not in the standard order.")
    h3_seen = {normalize_heading(h3) for h2, h3, _ in sections if h3 and normalize_heading(h2) == "explanation"}
    for sub in subs:
        if normalize_heading(sub) not in h3_seen:
            err("11 headings", f"Missing '### {sub}' under Explanation (required for {ko_type}).")

    # 12. dates
    created, updated = str(f.get("created", "")), str(f.get("last_updated", ""))
    if ISO_DATE.match(created) and ISO_DATE.match(updated) and updated < created:
        err("12 dates", "last_updated is earlier than created.")

    # 13. review status rules (only people set human statuses)
    review = as_dict(f.get("review"))
    status = review.get("status")
    if status in ("team_checked", "clinician_reviewed", "published") and not review.get("team_checker"):
        err("13 review status", f"Status '{status}' needs review.team_checker (a person).")
    if status == "clinician_reviewed" and not review.get("clinician_reviewer"):
        err("13 review status", "Status 'clinician_reviewed' needs review.clinician_reviewer.")

    # 14. open values and placeholders
    open_values = raw_text.count(VERIFY)
    if open_values:
        warn("14 open values", f"{open_values} value(s) are still '{VERIFY}'. Check them before publishing.")
    if TODO in raw_text:
        warn("14 placeholders", "Placeholder text (TODO) is still in the KO.")
    if status == "published" and (open_values or TODO in raw_text):
        err("14 open values", "A published KO cannot have '<verify>' values or TODO placeholders.")

    return ValidationResult(issues)


def validate_file(path: Path, registry: dict[str, Concept], other_files: dict[str, str] | None = None) -> ValidationResult:
    return validate_text(path.read_text(encoding="utf-8"), registry, other_files, str(path))
