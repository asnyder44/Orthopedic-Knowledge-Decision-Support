"""MedlinePlus health topics (NLM), from the bulk XML file.

https://medlineplus.gov/xml.html publishes every health topic daily. We keep the
topics in the configured groups (e.g. "Bones, Joints and Muscles"). Each topic's
curated external links are kept as `related_links` (links only, not content).
Summaries written by NLM are public domain; see
https://medlineplus.gov/about/using/usingcontent/
"""

from __future__ import annotations

import datetime as dt
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from ..text import html_to_lines, split_sections

INDEX = "https://medlineplus.gov/xml.html"
LICENSE = "Public domain (NLM-authored MedlinePlus summary); credit MedlinePlus"
_LAST_UPDATED = re.compile(r'id="lastupdate"[^>]*>\s*Last updated\s+([A-Za-z]+ \d{1,2}, \d{4})')


def doc_id(url: str) -> str:
    return "mplus:" + url.rstrip("/").rsplit("/", 1)[-1].removesuffix(".html")


def selected_topics(root: ET.Element, cfg: dict) -> list[ET.Element]:
    groups, extra = set(cfg.get("groups", [])), set(cfg.get("extra_titles", []))
    return [
        t for t in root.findall("health-topic")
        if t.get("language") == "English"
        and (groups & {g.text for g in t.findall("group")} or t.get("title") in extra)
    ]


def collect(out: Path, cfg: dict, http) -> None:
    from . import write_manifest

    index = http.text(INDEX)
    files = sorted(set(re.findall(r"https://medlineplus\.gov/xml/mplus_topics_\d{4}-\d\d-\d\d\.xml", index)))
    if not files:
        raise RuntimeError("Could not find the MedlinePlus bulk XML link on " + INDEX)
    xml_path = out / "topics.xml"
    if not xml_path.exists():
        xml_path.write_bytes(http.get(files[-1]))
    topics = selected_topics(ET.parse(xml_path).getroot(), cfg)
    print(f"  {len(topics)} topics in {sorted(cfg.get('groups', []))}")

    dates_path = out / "last_updated.json"
    dates = json.loads(dates_path.read_text()) if dates_path.exists() else {}
    if cfg.get("fetch_page_dates", True):
        for t in topics:
            url = t.get("url")
            if url in dates:
                continue
            match = _LAST_UPDATED.search(http.text(url, robots=True))
            dates[url] = dt.datetime.strptime(match.group(1), "%B %d, %Y").date().isoformat() if match else None
            dates_path.write_text(json.dumps(dates, indent=1))
    write_manifest(out, bulk_file=files[-1], topics=len(topics))


def parse(raw: Path, cfg: dict):
    from . import make_document, read_manifest

    manifest = read_manifest(raw)
    dates_path = raw / "last_updated.json"
    dates = json.loads(dates_path.read_text()) if dates_path.exists() else {}
    for t in selected_topics(ET.parse(raw / "topics.xml").getroot(), cfg):
        url, title = t.get("url"), t.get("title")
        summary = "".join(t.find("full-summary").itertext()) if t.find("full-summary") is not None else ""
        created = t.get("date-created")
        yield make_document(
            doc_id=doc_id(url),
            source="medlineplus",
            source_type="patient_education",
            title=title,
            url=url,
            sections=split_sections(html_to_lines(summary), f"About {title}"),
            audience="patients and caregivers",
            publisher="MedlinePlus, U.S. National Library of Medicine",
            license=LICENSE,
            retrieved=manifest["retrieved"],
            alt_titles=[a.text for a in t.findall("also-called") if a.text],
            container="MedlinePlus",
            published=dt.datetime.strptime(created, "%m/%d/%Y").date().isoformat() if created else None,
            last_updated=dates.get(url),
            mesh_terms=[d.text for d in t.findall("mesh-heading/descriptor") if d.text],
            groups=[g.text for g in t.findall("group") if g.text],
            related_links=[
                {"title": s.get("title"), "url": s.get("url"),
                 "organization": ", ".join(o.text for o in s.findall("organization") if o.text)}
                for s in t.findall("site")
            ][: cfg.get("max_related_links", 15)],
        )
