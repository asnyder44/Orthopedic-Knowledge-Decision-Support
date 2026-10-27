"""NIAMS health topics (National Institute of Arthritis and Musculoskeletal and
Skin Diseases, NIH). U.S. federal government text is public domain; some images
are not, and we do not collect images. Each topic has an overview page plus
tabbed sub-pages (e.g. diagnosis and treatment), which become one document.
"""

from __future__ import annotations

import html
import re
import urllib.error
from pathlib import Path

from ..text import html_sections, strip_html

BASE = "https://www.niams.nih.gov"
LICENSE = "Public domain (U.S. federal government work, NIH/NIAMS); credit NIAMS"
_TOPIC_LINK = re.compile(r'href="(?:https://www\.niams\.nih\.gov)?/health-topics/([a-z0-9-]+)"')


def collect(out: Path, cfg: dict, http) -> None:
    from . import write_manifest

    skip = set(cfg.get("index_pages", [])) | set(cfg.get("exclude", []))
    slugs: set[str] = set()
    for index in cfg.get("index_pages", []):
        slugs |= set(_TOPIC_LINK.findall(http.text(f"{BASE}/health-topics/{index}", robots=True)))
    slugs -= skip
    print(f"  {len(slugs)} topics")

    for slug in sorted(slugs):
        overview = out / f"{slug}.html"
        if not overview.exists():
            overview.write_bytes(http.get(f"{BASE}/health-topics/{slug}", robots=True))
        page = overview.read_text(encoding="utf-8", errors="replace")
        for sub in sorted(set(re.findall(rf"/health-topics/{slug}/([a-z0-9-]+)", page))):
            if sub in cfg.get("skip_subpages", []):
                continue
            path = out / f"{slug}__{sub}.html"
            if path.exists():
                continue
            try:
                path.write_bytes(http.get(f"{BASE}/health-topics/{slug}/{sub}", robots=True))
            except urllib.error.HTTPError as exc:
                print(f"  skipped {slug}/{sub}: HTTP {exc.code}")
    write_manifest(out, topics=sorted(slugs))


def _content(page: str) -> str:
    marker = page.find('class="col-md-12 syndicate"')
    if marker == -1:
        return ""
    start = page.find(">", marker) + 1
    # The article ends where the link cards ("View all Diseases", "Related Information")
    # or the review date begin, whichever comes first.
    ends = [i for i in (page.find("view-all__btn-wrap", start), page.find("Last Reviewed", start)) if i != -1]
    body = page[start:min(ends)] if ends else page[start:]
    return re.sub(r'<ul class="nav navigation-tabs".*?</ul>', " ", body, flags=re.S)


def parse(raw: Path, cfg: dict):
    from . import make_document, read_manifest

    manifest = read_manifest(raw)
    for slug in manifest["topics"]:
        pages = [raw / f"{slug}.html", *sorted(raw.glob(f"{slug}__*.html"))]
        pages = [p.read_text(encoding="utf-8", errors="replace") for p in pages if p.exists()]
        if not pages:
            continue
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", pages[0], re.S)
        title = strip_html(h1.group(1)) if h1 else slug.replace("-", " ").title()
        sections = [s for p in pages for s in html_sections(_content(p), title)]
        if not sections:
            continue
        reviewed = re.search(r'Last Reviewed:.*?<time datetime="(\d{4}-\d\d-\d\d)', pages[0], re.S)
        yield make_document(
            doc_id=f"niams:{slug}",
            source="niams",
            source_type="patient_education",
            title=html.unescape(title),
            url=f"{BASE}/health-topics/{slug}",
            sections=sections,
            audience="patients and caregivers",
            publisher="National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH)",
            license=LICENSE,
            retrieved=manifest["retrieved"],
            container="NIAMS Health Topics",
            last_updated=reviewed.group(1) if reviewed else None,
        )
