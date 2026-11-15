"""Job 1 helpers: find open-access articles about a topic, check them, and get their text.

- Search: Europe PMC REST API (open-access articles, reviews first).
- Full text: NCBI PubMed Central efetch (JATS XML), with Europe PMC as a fallback.
- Automatic checks (no person needed): open license, peer reviewed, not retracted, not a
  case report or editorial, has full text, not fetched before.
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urlencode

from defusedxml import ElementTree as SafeET

from ..fetch import FetchError, http_get

EPMC_SEARCH = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
EPMC_FULLTEXT = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
NCBI_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
PMC_ARTICLE_URL = "https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
TOOL_NAME = "okds-portal"
NCBI_PAUSE = 0.4  # NCBI allows 3 requests a second without an API key

# License -> OKDS reuse label. "No derivatives" licenses are not used: our KOs rewrite the text.
# Non-commercial (NC) articles may be used in this educational project, but only paraphrased and linked.
ALLOWED_LICENSES = {"cc0": "public_domain", "cc by": "open_license", "cc by-sa": "open_license",
                    "cc by-nc": "link_and_paraphrase", "cc by-nc-sa": "link_and_paraphrase"}
REVIEW_TYPES = {"review", "review-article", "systematic review", "systematic-review", "meta-analysis",
                "practice guideline", "guideline", "scoping review"}
SKIP_TYPES = {"case reports", "case-report", "editorial", "letter", "comment", "news", "erratum", "published erratum",
              "retracted publication", "retraction of publication", "preprint", "in-brief"}
SKIP_SECTIONS = re.compile(r"reference|acknowledg|funding|conflict|competing|author.*contribution|data availab|"
                           r"supplementary|abbreviation|ethic|consent|disclosure|declaration", re.I)


@dataclass
class Candidate:
    """One search result, before the full text is fetched."""
    pmcid: str
    title: str
    journal: str
    doi: str
    publication_date: str
    license: str
    pub_types: list[str]
    source: str = "Europe PMC"

    @property
    def url(self) -> str:
        return PMC_ARTICLE_URL.format(pmcid=self.pmcid)

    @property
    def is_review(self) -> bool:
        return bool({t.lower() for t in self.pub_types} & REVIEW_TYPES)


@dataclass
class CheckResult:
    ok: bool
    checks: dict[str, str] = field(default_factory=dict)  # name -> "pass" or the reason it failed
    reason: str = ""


def topic_terms(preferred_term: str, alternate_terms: list[str]) -> list[str]:
    """Search words for a topic: its name plus longer other names (short ones like "CTS" match too much)."""
    terms = [preferred_term] + [t for t in alternate_terms if len(t) >= 6 or " " in t]
    return list(dict.fromkeys(t.strip() for t in terms if t.strip()))


def build_query(terms: list[str], reviews_only: bool) -> str:
    def quote(t: str) -> str:
        return '"' + t.replace('"', "") + '"'
    title = " OR ".join(f"TITLE:{quote(t)}" for t in terms)
    q = f"({title}) AND OPEN_ACCESS:y AND NOT SRC:PPR"
    if reviews_only:
        q += ' AND (PUB_TYPE:"review" OR PUB_TYPE:"systematic-review" OR PUB_TYPE:"practice guideline")'
    return q


TEMPORARY_ERRORS = ("429", "500", "502", "503", "504", "timed out")


def _get_json(url: str, retries: int = 3) -> dict[str, Any]:
    """Europe PMC is sometimes briefly unavailable (503) or slow: wait and try again before giving up."""
    delay = 3.0
    for attempt in range(retries):
        try:
            data, _ctype, charset, _ = http_get(url, "application/json", ("json",))
            return json.loads(data.decode(charset, errors="replace"))
        except FetchError as e:
            if attempt == retries - 1 or not any(code in str(e) for code in TEMPORARY_ERRORS):
                raise
            time.sleep(delay)
            delay *= 2
    raise FetchError("unreachable")


def search_europe_pmc(terms: list[str], page_size: int = 10) -> list[Candidate]:
    """Reviews first, then other articles, without duplicates."""
    out: dict[str, Candidate] = {}
    for reviews_only in (True, False):
        params = {"query": build_query(terms, reviews_only), "format": "json", "resultType": "core", "pageSize": page_size}
        data = _get_json(f"{EPMC_SEARCH}?{urlencode(params)}")
        for r in (data.get("resultList") or {}).get("result") or []:
            pmcid = str(r.get("pmcid") or "")
            if not pmcid or pmcid in out:
                continue
            out[pmcid] = Candidate(
                pmcid=pmcid, title=str(r.get("title") or "").strip().rstrip("."),
                journal=str(((r.get("journalInfo") or {}).get("journal") or {}).get("title") or ""),
                doi=str(r.get("doi") or ""), publication_date=str(r.get("firstPublicationDate") or ""),
                license=str(r.get("license") or "").lower(),
                pub_types=[str(t) for t in ((r.get("pubTypeList") or {}).get("pubType") or [])],
            )
    return list(out.values())


def check_candidate(c: Candidate, seen: set[str]) -> CheckResult:
    """The automatic checks. Every failed check gives a plain reason."""
    checks: dict[str, str] = {}
    types = {t.lower() for t in c.pub_types}
    checks["not fetched before"] = "pass" if c.pmcid not in seen else "already in the inbox"
    checks["open license"] = ("pass" if c.license in ALLOWED_LICENSES else
                              f"license is {c.license.upper() or 'not stated'} (we need CC BY, CC BY-SA, CC BY-NC, or CC0)")
    checks["peer reviewed"] = "pass" if "preprint" not in types else "a preprint (not peer reviewed)"
    checks["not retracted"] = "pass" if not types & {"retracted publication", "retraction of publication"} else "retracted"
    bad = sorted(types & (SKIP_TYPES - {"preprint", "retracted publication", "retraction of publication"}))
    checks["article type"] = "pass" if not bad else f"a {bad[0]} (we use research and review articles)"
    failed = [v for v in checks.values() if v != "pass"]
    return CheckResult(ok=not failed, checks=checks, reason=failed[0] if failed else "")


def permitted_use(license_name: str) -> str:
    return ALLOWED_LICENSES.get(license_name.lower(), "restricted")


# ---------------------------------------------------------------- full text

def _text(el) -> str:
    return " ".join("".join(el.itertext()).split())


def jats_to_text(xml: bytes, max_chars: int) -> str:
    """Abstract + main sections as plain text with '## ' headings. References, tables, and figures are dropped."""
    root = SafeET.fromstring(xml)
    article = root.find(".//article") if root.tag != "article" else root
    if article is None:
        return ""
    parts: list[str] = []
    abstract = article.find(".//front//abstract")
    if abstract is not None:
        parts.append("## Abstract\n" + _text(abstract))
    body = article.find(".//body")
    if body is not None:
        for sec in body.findall("sec"):
            title = _text(sec.find("title")) if sec.find("title") is not None else ""
            if title and SKIP_SECTIONS.search(title):
                continue
            paras = [_text(p) for p in sec.iter("p") if not _inside_table_or_figure(sec, p)]
            text = "\n".join(p for p in paras if p)
            if text:
                parts.append(f"## {title or 'Section'}\n{text}")
        if not body.findall("sec"):  # some articles have paragraphs only
            parts.append("\n".join(_text(p) for p in body.findall("p")))
    text = "\n\n".join(p for p in parts if p.strip())
    if len(text) > max_chars:
        text = text[:max_chars].rsplit(" ", 1)[0] + " [...]"
    return text


def _inside_table_or_figure(sec, p) -> bool:
    for holder in list(sec.iter("table-wrap")) + list(sec.iter("fig")):
        if any(x is p for x in holder.iter("p")):
            return True
    return False


def fetch_full_text(pmcid: str, max_chars: int, email: str = "") -> tuple[str, str]:
    """Returns (text, where it came from). NCBI first, Europe PMC if NCBI fails."""
    params = {"db": "pmc", "id": pmcid.removeprefix("PMC"), "retmode": "xml", "tool": TOOL_NAME}
    if email:
        params["email"] = email
    errors = []
    for name, url in (("PubMed Central", f"{NCBI_EFETCH}?{urlencode(params)}"),
                      ("Europe PMC", EPMC_FULLTEXT.format(pmcid=pmcid))):
        try:
            data, *_ = http_get(url, "application/xml,text/xml", ("xml",))
            text = jats_to_text(data, max_chars)
            if len(text) >= 500:
                return text, name
            errors.append(f"{name}: almost no text")
        except (FetchError, SafeET.ParseError, ValueError) as e:
            errors.append(f"{name}: {e}")
        time.sleep(NCBI_PAUSE)
    raise FetchError("No full text: " + "; ".join(errors))
