"""Choose a KO's sources by hand: browse what `okds collect-topics` found, search the OrthoInfo dataset
(MedlinePlus, NIAMS, OpenStax and CC BY Europe PMC full text already in data/processed), and set the
KO's sources. Setting rewrites both the source pack (with the text) and the KO's `sources` + References.

  okds sources show KO-HAND-COND-003            numbered candidates for the topic
  okds sources local "trigger finger"           matching documents in the OrthoInfo dataset
  okds sources set KO-HAND-COND-003 local:mplus:triggerfinger c2 c5
"""

from __future__ import annotations

import datetime as dt
import gzip
import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

from . import collect
from .config import REPO_ROOT, Settings
from .ko import parse_ko, refresh_references, render_ko
from .registry import load_registry
from .storage import LocalKOStore

MAX_TEXT = 9000  # characters of a local document kept in a pack (long articles: the first sections; use #heading)
MAX_PATIENT_TEXT = 30000  # MedlinePlus / NIAMS pages are kept whole
LOCAL_KIND = {"medlineplus": ("government_health_page", "patient", "public_domain"),
              "niams": ("government_health_page", "patient", "public_domain"),
              "openstax": ("textbook", "student", "open_license"),
              "europepmc": ("journal_article", "clinician", "open_license"),
              "wikipedia": ("other", "patient", "open_license")}


def _dataset_file() -> Path | None:
    files = sorted((REPO_ROOT / "data" / "processed").glob("v*/documents.jsonl*"))
    return files[-1] if files else None


@lru_cache(maxsize=1)
def local_docs() -> dict[str, dict[str, Any]]:
    path = _dataset_file()
    if path is None:
        return {}
    opener = gzip.open if path.suffix == ".gz" else open
    out = {}
    with opener(path, "rt", encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            out[d["doc_id"]] = d
    return out


def _sections(d: dict[str, Any]) -> list[dict[str, str]]:
    s = d.get("sections")
    if isinstance(s, str):
        try:
            import ast
            s = ast.literal_eval(s)
        except (ValueError, SyntaxError):
            s = [{"heading": "", "text": s}]
    return s or []


def search_local(query: str, n: int = 15) -> list[tuple[float, dict[str, Any]]]:
    words = [w for w in re.findall(r"[a-z0-9]+", query.lower()) if len(w) > 2]
    if not words:
        return []
    scored = []
    for d in local_docs().values():
        title = f"{d.get('title', '')} {d.get('alt_titles', '')}".lower()
        first = " ".join(sec.get("text", "") for sec in _sections(d)[:3]).lower()
        s = sum(3 for w in words if w in title) + sum(1 for w in words if w in first)
        if all(w in title + " " + first for w in words):
            s += 4
        if d.get("source") in ("medlineplus", "niams"):
            s += 1  # patient-level first
        if s >= max(3, len(words) * 2):
            scored.append((s, d))
    scored.sort(key=lambda x: -x[0])
    return scored[:n]


def local_source(doc_id: str, sid: str, max_chars: int | None = None) -> dict[str, Any]:
    """doc_id may end in '#words' to keep only the sections whose heading contains those words
    (e.g. 'pmc:PMC8160369#splint'), plus the abstract/first section for context."""
    doc_id, _, want = doc_id.partition("#")
    d = local_docs().get(doc_id)
    if d is None:
        raise ValueError(f"No document '{doc_id}' in the OrthoInfo dataset. Use: okds sources local \"words\"")
    stype, audience, use = LOCAL_KIND.get(d.get("source", ""), ("other", "patient", "<verify>"))
    if max_chars is None:  # whole patient pages (they are the plain-language source); long articles: the start
        max_chars = MAX_PATIENT_TEXT if d.get("source") in ("medlineplus", "niams") else MAX_TEXT
    sections = _sections(d)
    if want:
        words = want.lower().replace("+", " ").split()
        picked = [s for s in sections if all(w in str(s.get("heading", "")).lower() for w in words)]
        if not picked:
            heads = "; ".join(str(s.get("heading", ""))[:40] for s in sections if s.get("heading"))
            raise ValueError(f"No section of {doc_id} has '{want}' in its heading. Headings: {heads[:600]}")
        sections = ([sections[0]] if sections[0] not in picked else []) + picked
    parts, size = [], 0
    for sec in sections:
        chunk = (f"{sec.get('heading')}\n" if sec.get("heading") else "") + str(sec.get("text", "")).strip()
        room = max_chars - size
        if room < 500:
            break
        if len(chunk) > room:  # keep the start of a long section rather than dropping it
            chunk = chunk[:room].rsplit(" ", 1)[0] + " […]"
        parts.append(chunk)
        size += len(chunk)
    licence = str(d.get("license", ""))
    if use == "open_license":  # CC BY-NC / -ND articles may be paraphrased and linked, not reused
        use = collect.classify_licence(licence.split(" — ")[0].split(" � ")[0])
    return {"id": sid, "title": d.get("title", ""), "publisher": d.get("publisher") or d.get("container") or d.get("source"),
            "url": d.get("url", ""), "source_type": stype, "audience": audience,
            "publication_date": str(d.get("last_updated") or d.get("published") or "<verify>")[:10],
            "retrieved_date": str(d.get("retrieved") or dt.date.today().isoformat())[:10], "permitted_use": use,
            "evidence_strength": None,
            "notes": (f"From the OrthoInfo dataset ({doc_id}{' sections: ' + want if want else ''}). "
                      f"Licence: {licence.split(' — ')[0][:120]}")[:300],
            "text": "\n\n".join(parts)[:max_chars]}


def candidates_path(settings: Settings, ko_id: str) -> Path:
    return settings.data_dir / "sources" / "candidates" / f"{ko_id}.json"


def build_sources(settings: Settings, ko_id: str, picks: list[str]) -> list[dict[str, Any]]:
    """picks: 'c3' (candidate 3 from `show`) or 'local:<doc_id>' (OrthoInfo dataset)."""
    cands = collect.load_candidates(candidates_path(settings, ko_id)) if candidates_path(settings, ko_id).is_file() else []
    sources = []
    for i, pick in enumerate(picks, 1):
        sid = f"S{i}"
        if pick.startswith("local:"):
            sources.append(local_source(pick[6:], sid))
        elif re.fullmatch(r"c\d+", pick):
            n = int(pick[1:])
            if not 1 <= n <= len(cands):
                raise ValueError(f"{pick}: there are {len(cands)} candidates for {ko_id}")
            sources.append(collect.as_source(cands[n - 1], sid))
        else:
            raise ValueError(f"Unknown pick '{pick}'. Use c<number> or local:<doc_id>.")
    return sources


def set_sources(settings: Settings, ko_id: str, picks: list[str]) -> tuple[Path, Path | None]:
    """Write the source pack and, if the KO file exists, its `sources` and References."""
    registry = load_registry(settings.registry_path)
    concept = registry.get(ko_id)
    if concept is None:
        raise ValueError(f"{ko_id} is not in the registry")
    sources = build_sources(settings, ko_id, picks)
    settings.ensure_dirs()
    pack = settings.packs_dir / f"SP-{ko_id}.md"
    pack.write_text(collect.render_pack(ko_id, concept.preferred_term, sources), encoding="utf-8", newline="\n")
    entry = next((e for e in LocalKOStore(settings).list_entries() if e.ko_id == ko_id), None)
    if entry is None:
        return pack, None
    doc = parse_ko(entry.path.read_text(encoding="utf-8"))
    doc.front["sources"] = [{k: v for k, v in s.items() if k != "text" and v not in (None, "")} for s in sources]
    entry.path.write_text(render_ko(refresh_references(doc)), encoding="utf-8", newline="\n")
    return pack, entry.path
