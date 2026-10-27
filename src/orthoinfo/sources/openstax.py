"""OpenStax open textbooks (CC BY 4.0), e.g. Anatomy and Physiology 2e.

Pages are listed from the book's sitemap and filtered to the configured
chapters (6-11 cover bone, skeleton, joints and muscles). Only numbered
sections and chapter introductions are kept, not end-of-chapter quizzes.
"""

from __future__ import annotations

import re
from pathlib import Path

from ..text import html_sections, strip_html

LICENSE = "CC BY 4.0 (OpenStax); attribute OpenStax and link to the book"


def _wanted(slug: str, chapters: set[int]) -> bool:
    m = re.match(r"(\d+)-(\d+-|introduction$)", slug)
    return bool(m) and int(m.group(1)) in chapters


def collect(out: Path, cfg: dict, http) -> None:
    from . import write_manifest

    book, chapters = cfg["book"], set(cfg["chapters"])
    sitemap = http.text(f"https://openstax.org/rex/sitemaps/{book}.xml", robots=True)
    urls = [u for u in re.findall(r"<loc>([^<]+)</loc>", sitemap) if _wanted(u.rsplit("/", 1)[-1], chapters)]
    print(f"  {len(urls)} pages from chapters {sorted(chapters)}")
    for url in urls:
        path = out / f"{url.rsplit('/', 1)[-1]}.html"
        if not path.exists():
            path.write_bytes(http.get(url, robots=True))
    write_manifest(out, book=book, pages=[u.rsplit("/", 1)[-1] for u in urls])


def parse(raw: Path, cfg: dict):
    from . import make_document, read_manifest

    manifest = read_manifest(raw)
    book = manifest["book"]
    book_title = cfg.get("book_title", book)
    for slug in manifest["pages"]:
        path = raw / f"{slug}.html"
        if not path.exists():
            continue
        page = path.read_text(encoding="utf-8", errors="replace")
        start = page.find('data-type="page"')
        end = page.find("</main>", start)
        body = page[page.find(">", start) + 1:end] if start != -1 else ""
        h2 = re.search(r'<h2 data-type="document-title"[^>]*>(.*?)</h2>', body, re.S)
        title = strip_html(h2.group(1)) if h2 else slug
        body = body[h2.end():] if h2 else body
        sections = html_sections(body, title)
        if not sections:
            continue
        yield make_document(
            doc_id=f"openstax:{book}:{slug}",
            source="openstax",
            source_type="textbook",
            title=f"{title} ({book_title})",
            url=f"https://openstax.org/books/{book}/pages/{slug}",
            sections=sections,
            audience="students",
            publisher="OpenStax, Rice University",
            license=LICENSE,
            retrieved=manifest["retrieved"],
            authors=cfg.get("authors", ""),
            container=book_title,
            published=str(cfg.get("year", "")) or None,
        )
