"""Open-access research articles from Europe PMC (mirrors the PMC Open Access subset).

Only articles whose licence is in `licenses` (default: CC BY, CC BY-SA, CC0 —
licences that allow reuse with attribution) are collected. The licence is read
from each article. Search: https://europepmc.org/RestfulWebService

Raw layout: articles.jsonl (search metadata, one line per article) and
fulltext/<PMCID>.xml (JATS XML). Re-running resumes where it stopped.
"""

from __future__ import annotations

import json
import re
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
import xml.etree.ElementTree as ET
from pathlib import Path

API = "https://www.ebi.ac.uk/europepmc/webservices/rest"
SKIP_SECTIONS = re.compile(
    r"(?i)^(acknowledg|funding|conflicts? of interest|competing interest|declaration|author contribution|"
    r"data availability|ethics|consent|abbreviations|supplementary|disclosure|financial support)"
)


def build_query(term: str, cfg: dict) -> str:
    licenses = " OR ".join(f'LICENSE:"{lic}"' for lic in cfg["licenses"])
    # Plain terms are matched as a phrase in the title or abstract: unquoted words match
    # anywhere in the full text, which pulls in highly cited but unrelated papers.
    # A term containing ":" is used as written (Europe PMC query syntax).
    topic = term if ":" in term else f'TITLE_ABS:"{term}"'
    query = f'({topic}) AND OPEN_ACCESS:y AND HAS_FT:y AND LANG:"eng" AND ({licenses})'
    return f"{query} AND ({cfg['filter']})" if cfg.get("filter") else query


def collect(out: Path, cfg: dict, http) -> None:
    from . import write_manifest

    meta_path = out / "articles.jsonl"
    known = {}
    if meta_path.exists():
        known = {a["pmcid"]: a for a in map(json.loads, meta_path.read_text(encoding="utf-8").splitlines())}
    per_query = cfg.get("max_per_query", 50)

    with meta_path.open("a", encoding="utf-8") as fh:
        for term in cfg["queries"]:
            cursor, seen = "*", 0
            while seen < per_query:
                page = http.json(f"{API}/search", {
                    "query": build_query(term, cfg), "resultType": "core", "format": "json",
                    "pageSize": min(1000, per_query - seen), "cursorMark": cursor,
                    "sort": cfg.get("sort", "CITED desc"),
                }, delay=cfg.get("delay", 0.3))
                results = page.get("resultList", {}).get("result", [])
                for r in results:
                    pmcid = r.get("pmcid")
                    if not pmcid or pmcid in known:
                        continue
                    known[pmcid] = {
                        "pmcid": pmcid, "query": term, "title": r.get("title"),
                        "license": r.get("license"), "pub_year": r.get("pubYear"),
                        "pub_types": r.get("pubTypeList", {}).get("pubType", []),
                        "cited_by": r.get("citedByCount"), "doi": r.get("doi"),
                    }
                    fh.write(json.dumps(known[pmcid]) + "\n")
                seen += len(results)
                nxt = page.get("nextCursorMark")
                if not results or not nxt or nxt == cursor:
                    break
                cursor = nxt
            print(f"  {term!r}: {page.get('hitCount', 0)} matching, {len(known)} articles so far")

    full = out / "fulltext"
    full.mkdir(exist_ok=True)
    todo = [p for p in known if not (full / f"{p}.xml").exists()]

    def fetch(pmcid: str, client) -> str | None:
        try:
            data = client.get(f"{API}/{pmcid}/fullTextXML", delay=cfg.get("delay", 0.3))
        except urllib.error.HTTPError:
            return pmcid
        tmp = full / f"{pmcid}.xml.part"
        tmp.write_bytes(data)
        tmp.replace(full / f"{pmcid}.xml")  # atomic: never a half-written file
        return None

    # A few parallel downloads (each with its own polite delay) keep large pulls practical.
    workers = max(1, cfg.get("workers", 4))
    clients = [type(http)() for _ in range(workers)]
    missing = []
    with ThreadPoolExecutor(workers) as pool:
        futures = [pool.submit(fetch, p, clients[i % workers]) for i, p in enumerate(todo)]
        for i, fut in enumerate(as_completed(futures), 1):
            if fut.result():
                missing.append(fut.result())
            if i % 100 == 0:
                print(f"  downloaded {i}/{len(todo)} full texts", flush=True)
    write_manifest(out, queries=cfg["queries"], licenses=cfg["licenses"], articles=len(known),
                   missing_fulltext=missing)


def _text(el) -> str:
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip() if el is not None else ""


def _paragraphs(sec) -> list[str]:
    out = []
    for child in sec:
        if child.tag == "p":
            out.append(_text(child))
        elif child.tag == "list":
            out.extend("- " + _text(item) for item in child.iter("list-item"))
    return [p for p in out if p]


def _walk(sec, path: list[str], sections: list[dict]) -> None:
    title = _text(sec.find("title"))
    if title and SKIP_SECTIONS.match(title):
        return
    here = [*path, title] if title else path
    paras = _paragraphs(sec)
    if paras:
        sections.append({"heading": " — ".join(here) or "Main text", "text": "\n".join(paras)})
    for child in sec.findall("sec"):
        _walk(child, here, sections)


def parse_jats(xml_bytes: bytes) -> dict:
    root = ET.fromstring(xml_bytes)
    meta = root.find(".//article-meta")
    sections: list[dict] = []
    for abstract in (meta.findall("abstract") if meta is not None else []):
        if abstract.get("abstract-type") in (None, "summary", "structured"):
            paras = [_text(p) for p in abstract.iter("p")]
            if paras:
                sections.append({"heading": "Abstract", "text": "\n".join(paras)})
            break
    body = root.find(".//body")
    if body is not None:
        loose = _paragraphs(body)
        if loose:
            sections.append({"heading": "Main text", "text": "\n".join(loose)})
        for sec in body.findall("sec"):
            _walk(sec, [], sections)

    authors = []
    for name in root.findall(".//contrib-group/contrib[@contrib-type='author']/name"):
        authors.append(" ".join(filter(None, [_text(name.find("given-names")), _text(name.find("surname"))])))
    lic = root.find(".//permissions/license")
    href = lic.get("{http://www.w3.org/1999/xlink}href") if lic is not None else None
    return {
        "title": _text(root.find(".//title-group/article-title")),
        "journal": _text(root.find(".//journal-title")),
        "year": _text(root.find(".//pub-date/year")) or None,
        "doi": _text(root.find(".//article-id[@pub-id-type='doi']")) or None,
        "authors": authors,
        "license_text": " ".join(filter(None, [href, _text(lic)]))[:300],
        "sections": sections,
    }


def parse(raw: Path, cfg: dict):
    from . import make_document, read_manifest

    manifest = read_manifest(raw)
    for line in (raw / "articles.jsonl").read_text(encoding="utf-8").splitlines():
        meta = json.loads(line)
        path = raw / "fulltext" / f"{meta['pmcid']}.xml"
        if not path.exists():
            continue
        try:
            art = parse_jats(path.read_bytes())
        except ET.ParseError:
            continue
        if not art["sections"]:
            continue
        authors = art["authors"]
        yield make_document(
            doc_id=f"pmc:{meta['pmcid']}",
            source="europepmc",
            source_type="research_article",
            title=art["title"] or meta["title"],
            url=f"https://pmc.ncbi.nlm.nih.gov/articles/{meta['pmcid']}/",
            sections=art["sections"],
            audience="clinicians, researchers and students",
            publisher=art["journal"],
            license=f"{(meta.get('license') or '').upper()} — {art['license_text']}".strip(" —"),
            retrieved=manifest["retrieved"],
            authors=", ".join(authors[:3]) + (" et al." if len(authors) > 3 else ""),
            container=art["journal"],
            published=art["year"] or meta.get("pub_year"),
            doi=art["doi"],
            pub_types=meta.get("pub_types", []),
            cited_by=meta.get("cited_by"),
            collected_for=meta.get("query"),
        )
