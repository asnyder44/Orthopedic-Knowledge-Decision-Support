"""Step 4a: collect raw source material from the MedlinePlus web service.

Raw responses are saved unmodified under data/raw/<version>/ so that cleaning
(`orthoinfo build`) can be re-run and audited without hitting the network again.

MedlinePlus web service: https://medlineplus.gov/about/developers/webservices/
It asks clients to stay under 85 requests per minute; we pause between calls.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

from .config import RAW_DIR, load_scope

API_URL = "https://wsearch.nlm.nih.gov/ws/query"
USER_AGENT = "orthoinfo-student-project/0.1 (educational; Data Science in Practice)"
_LAST_UPDATED = re.compile(r'id="lastupdate"[^>]*>\s*Last updated\s+([A-Za-z]+ \d{1,2}, \d{4})')


def _get(url: str, timeout: float = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8")


def search_health_topics(term: str, retmax: int = 10) -> str:
    """Return the raw XML search result for an English health-topic query."""
    query = urllib.parse.urlencode({"db": "healthTopics", "term": term, "retmax": retmax})
    return _get(f"{API_URL}?{query}")


def parse_search_xml(xml_text: str) -> list[dict]:
    """Parse a MedlinePlus search response into a list of documents.

    Content fields keep their HTML (summaries use <p>/<ul>); repeated fields such
    as groupName and altTitle become lists.
    """
    root = ET.fromstring(xml_text)
    docs = []
    for node in root.iter("document"):
        doc: dict = {"url": node.get("url"), "rank": int(node.get("rank", 0))}
        for content in node.findall("content"):
            name = content.get("name")
            value = "".join(content.itertext())
            doc.setdefault(name, []).append(value)
        docs.append(doc)
    return docs


def fetch_last_updated(url: str) -> str | None:
    """Scrape the 'Last updated <date>' line from a MedlinePlus page as ISO date."""
    try:
        match = _LAST_UPDATED.search(_get(url))
    except OSError:
        return None
    if not match:
        return None
    return dt.datetime.strptime(match.group(1), "%B %d, %Y").date().isoformat()


def collect(version: str | None = None, fetch_pages: bool = True, delay: float = 1.0) -> Path:
    """Download every topic in config/scope.toml into data/raw/<version>/."""
    scope = load_scope()
    version = version or dt.date.today().isoformat()
    out = RAW_DIR / version
    out.mkdir(parents=True, exist_ok=True)
    retrieved = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")

    manifest = {"version": version, "retrieved": retrieved, "api": API_URL, "topics": []}
    for topic in scope["topics"]:
        term = topic["term"]
        xml_text = search_health_topics(term)
        slug = re.sub(r"[^a-z0-9]+", "_", term.lower()).strip("_")
        (out / f"{slug}.xml").write_text(xml_text, encoding="utf-8")
        time.sleep(delay)

        docs = parse_search_xml(xml_text)
        urls = [d["url"] for d in docs]
        expected = topic.get("url")
        chosen = expected if expected in urls else (urls[0] if urls else None)
        if expected and expected not in urls:
            print(f"WARNING: {expected} not returned for '{term}'; using {chosen}")

        last_updated = None
        if fetch_pages and chosen:
            last_updated = fetch_last_updated(chosen)
            time.sleep(delay)

        manifest["topics"].append(
            {
                "term": term,
                "role": topic.get("role", "core"),
                "raw_file": f"{slug}.xml",
                "url": chosen,
                "last_updated": last_updated,
            }
        )
        print(f"  {term:35s} -> {chosen}  (last updated {last_updated})")

    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return out
