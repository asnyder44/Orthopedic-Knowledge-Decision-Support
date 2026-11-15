"""Collect open-access sources for a KO topic from public scholarly APIs, and build source packs.

Only sources that can be used legally and without logging in are queried:

  europepmc        Europe PMC: PubMed, PubMed Central open access, and preprints (bioRxiv, medRxiv)
  semanticscholar  Semantic Scholar Graph API (open-access papers only)
  doaj             Directory of Open Access Journals (covers SpringerOpen, MDPI, Hindawi, SciELO, Redalyc,
                   Wiley and Nature open-access journals)
  openaire         OpenAIRE research graph (open-access publications)
  zenodo           Zenodo publications
  hal              HAL open archive
  plos             PLOS journals
  core             CORE (only when CORE_API_KEY is set)
  medlineplus      MedlinePlus health topics (patient-level, public domain), for patient-audience KOs

Not used, on purpose: Sci-Hub and PaperPanda (copyright infringement); Google Scholar, ResearchGate and
Academia.edu (their terms forbid automated collection); DeepDyve, JSTOR, EBSCO, Research4Life (logins).

Each candidate keeps its licence. CC BY / CC0 / CC BY-SA -> permitted_use "open_license"; MedlinePlus ->
"public_domain"; anything else -> "link_and_paraphrase" (the KO may paraphrase the abstract and link it).
The text kept for a source is its abstract (or the MedlinePlus summary), not the full paper.
"""

from __future__ import annotations

import datetime as dt
import html
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from .tls import tls_context

USER_AGENT = "OKDS-portal/0.2 (student research project; open-access source collection)"
TIMEOUT = 30
OPEN_LICENCES = ("cc0", "cc by", "cc-by", "cc_by", "creative commons attribution", "public domain", "pd")
NC_ND = ("nc", "nd")  # open but restricted: still only paraphrase and link


@dataclass
class Candidate:
    provider: str
    title: str
    url: str
    publisher: str = ""
    year: str = ""
    doi: str = ""
    abstract: str = ""
    licence: str = ""
    kind: str = ""              # review / guideline / trial / article / preprint / patient page
    source_type: str = "journal_article"
    audience: str = "clinician"
    permitted_use: str = "link_and_paraphrase"
    score: float = 0.0
    providers: list[str] = field(default_factory=list)


# ---------------------------------------------------------------- HTTP

_TLS = tls_context()


def _get(url: str, headers: dict[str, str] | None = None, retries: int = 3) -> str:
    h = {"User-Agent": USER_AGENT, "Accept": "application/json, text/xml;q=0.9, */*;q=0.5", **(headers or {})}
    delay = 2.0
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=TIMEOUT, context=_TLS) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(delay)
                delay *= 2.5
                continue
            raise
    raise RuntimeError("unreachable")


def _json(url: str, **kw) -> Any:
    return json.loads(_get(url, **kw))


def _q(s: str) -> str:
    return urllib.parse.quote(s)


def _clean(text: Any) -> str:
    if isinstance(text, list):
        text = " ".join(str(t) for t in text)
    text = html.unescape(re.sub(r"<[^>]+>", " ", str(text or "")))
    return " ".join(text.split())


def classify_licence(licence: str) -> str:
    lic = (licence or "").lower()
    if any(o in lic for o in OPEN_LICENCES) and not any(re.search(rf"\b{x}\b", lic.replace("-", " ")) for x in NC_ND):
        return "open_license"
    return "link_and_paraphrase"


def _kind(title: str, types: list[str] | str = "") -> tuple[str, str]:
    """(kind, KO source_type) from publication types and the title."""
    types_text = (" ".join(types) if isinstance(types, list) else str(types)).lower()
    t, ti = types_text + " " + title.lower(), title.lower()
    if re.search(r"\bcase (report|series)\b|\ba (novel|rare|unusual) case\b|case-report", t):
        return "case report", "journal_article"
    if "guideline" in t or "consensus" in t:
        return "guideline", "guideline"
    if "systematic review" in t or "meta-analys" in t or "systematic-review" in t:
        return "systematic review", "systematic_review"
    if "review" in ti or "review-article" in types_text:  # many indexes tag ordinary papers "Review"
        return "review", "journal_article"
    if "trial" in t or "randomi" in t:
        return "trial", "journal_article"
    if "preprint" in t:
        return "preprint", "journal_article"
    return "article", "journal_article"


# ---------------------------------------------------------------- providers

def europepmc(term: str, n: int) -> list[Candidate]:
    q = f'(TITLE:"{term}" OR ABSTRACT:"{term}") AND (OPEN_ACCESS:y OR SRC:PPR) AND HAS_ABSTRACT:y'
    url = (f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={_q(q)}&format=json&resultType=core"
           f"&pageSize={n}&sort={_q('CITED desc')}")
    out = []
    for r in _json(url).get("resultList", {}).get("result", []):
        title = _clean(r.get("title")).rstrip(".")
        types = (r.get("pubTypeList") or {}).get("pubType", [])
        preprint = r.get("source") == "PPR"
        kind, stype = _kind(title, types + (["preprint"] if preprint else []))
        link = (f"https://europepmc.org/article/{r.get('source')}/{r.get('id')}" if not r.get("pmcid")
                else f"https://www.ncbi.nlm.nih.gov/pmc/articles/{r['pmcid']}/")
        journal = (((r.get("journalInfo") or {}).get("journal") or {}).get("title")
                   or (r.get("bookOrReportDetails") or {}).get("publisher", ""))
        if preprint:
            journal = journal or (r.get("publisher") or "Preprint server")
        out.append(Candidate("europepmc", title, link, publisher=journal or "Europe PMC", year=str(r.get("pubYear") or ""),
                             doi=r.get("doi") or "", abstract=_clean(r.get("abstractText")), licence=r.get("license") or "",
                             kind=kind, source_type=stype))
    return out


def semanticscholar(term: str, n: int) -> list[Candidate]:
    fields = "title,abstract,year,venue,externalIds,openAccessPdf,url,publicationTypes,citationCount"
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={_q(term)}&limit={n}&openAccessPdf&fields={fields}"
    headers = {"x-api-key": os.environ["S2_API_KEY"]} if os.environ.get("S2_API_KEY") else None
    out = []
    for r in _json(url, headers=headers, retries=5).get("data", []) or []:
        if not r.get("abstract"):
            continue
        pdf = (r.get("openAccessPdf") or {})
        kind, stype = _kind(r.get("title") or "", r.get("publicationTypes") or [])
        out.append(Candidate("semanticscholar", _clean(r.get("title")), r.get("url") or pdf.get("url") or "",
                             publisher=r.get("venue") or "Semantic Scholar", year=str(r.get("year") or ""),
                             doi=(r.get("externalIds") or {}).get("DOI", ""), abstract=_clean(r.get("abstract")),
                             licence=pdf.get("license") or "", kind=kind, source_type=stype,
                             score=min(float(r.get("citationCount") or 0), 500) / 500))
    return out


def doaj(term: str, n: int) -> list[Candidate]:
    url = f"https://doaj.org/api/search/articles/{_q(chr(34) + term + chr(34))}?pageSize={n}"
    out = []
    for r in _json(url).get("results", []):
        b = r.get("bibjson", {})
        abstract = _clean(b.get("abstract"))
        if not abstract:
            continue
        doi = next((i.get("id") for i in b.get("identifier", []) if i.get("type") == "doi"), "")
        link = next((li.get("url") for li in b.get("link", []) if li.get("url")), "") or (f"https://doi.org/{doi}" if doi else "")
        kind, stype = _kind(b.get("title") or "")
        journal = (b.get("journal") or {})
        out.append(Candidate("doaj", _clean(b.get("title")), link, publisher=journal.get("title") or journal.get("publisher", ""),
                             year=str(b.get("year") or ""), doi=doi, abstract=abstract,
                             licence="open access journal (licence per article: <verify>)", kind=kind, source_type=stype))
    return out


def openaire(term: str, n: int) -> list[Candidate]:
    url = f"https://api.openaire.eu/search/publications?title={_q(term)}&format=json&size={n}&OA=true"
    res = (_json(url).get("response", {}).get("results") or {}).get("result", []) or []
    out = []
    for r in res if isinstance(res, list) else [res]:
        m = r["metadata"]["oaf:entity"]["oaf:result"]
        titles = m.get("title")
        titles = titles if isinstance(titles, list) else [titles]
        title = _clean(next((t.get("$") for t in titles if isinstance(t, dict) and t.get("$")), ""))
        desc = m.get("description")
        desc = desc if isinstance(desc, list) else [desc]
        abstract = _clean(" ".join(d.get("$", "") if isinstance(d, dict) else str(d or "") for d in desc))
        if not title or not abstract:
            continue
        pids = m.get("pid")
        pids = pids if isinstance(pids, list) else [pids]
        doi = next((p.get("$") for p in pids if isinstance(p, dict) and p.get("@classid") == "doi"), "")
        lic = (m.get("bestaccessright") or {}).get("@classname", "")
        pub = m.get("publisher")
        out.append(Candidate("openaire", title, f"https://doi.org/{doi}" if doi else "",
                             publisher=(pub.get("$") if isinstance(pub, dict) else str(pub or "")) or "OpenAIRE",
                             year=(str(m["dateofacceptance"].get("$", ""))[:4]
                                   if isinstance(m.get("dateofacceptance"), dict) else ""),
                             doi=doi, abstract=abstract, licence=lic, kind=_kind(title)[0], source_type=_kind(title)[1]))
    return [c for c in out if c.url]


def zenodo(term: str, n: int) -> list[Candidate]:
    url = f"https://zenodo.org/api/records?q={_q(chr(34) + term + chr(34))}&size={n}&type=publication&sort=mostviewed"
    out = []
    for h in _json(url).get("hits", {}).get("hits", []):
        m = h.get("metadata", {})
        abstract = _clean(m.get("description"))
        if not abstract or len(abstract) < 200:
            continue
        lic = (m.get("license") or {}).get("id", "") if isinstance(m.get("license"), dict) else str(m.get("license") or "")
        kind, stype = _kind(m.get("title") or "")
        out.append(Candidate("zenodo", _clean(m.get("title")), (h.get("links") or {}).get("self_html", ""),
                             publisher=((m.get("journal") or {}).get("title") or "Zenodo"),
                             year=str(m.get("publication_date", ""))[:4],
                             doi=h.get("doi") or "", abstract=abstract, licence=lic, kind=kind, source_type=stype))
    return out


def hal(term: str, n: int) -> list[Candidate]:
    fl = "title_s,abstract_s,uri_s,producedDateY_i,journalTitle_s,licence_s,docType_s,doiId_s"
    url = f"https://api.archives-ouvertes.fr/search/?q={_q(chr(34) + term + chr(34))}&rows={n}&fl={fl}&fq=language_s:en"
    out = []
    for d in _json(url).get("response", {}).get("docs", []):
        abstract = _clean(d.get("abstract_s"))
        if not abstract:
            continue
        title = _clean(d.get("title_s"))
        kind, stype = _kind(title, d.get("docType_s") or "")
        out.append(Candidate("hal", title, d.get("uri_s", ""), publisher=d.get("journalTitle_s") or "HAL open archive",
                             year=str(d.get("producedDateY_i") or ""), doi=d.get("doiId_s") or "", abstract=abstract,
                             licence=d.get("licence_s") or "", kind=kind, source_type=stype))
    return out


def plos(term: str, n: int) -> list[Candidate]:
    q = f'title:"{term}" OR abstract:"{term}"'
    url = (f"https://api.plos.org/search?q={_q(q)}&rows={n}&fl=id,title_display,abstract,journal,publication_date,article_type"
           f"&fq={_q('doc_type:full')}")
    out = []
    for d in _json(url).get("response", {}).get("docs", []):
        abstract = _clean(d.get("abstract"))
        if not abstract:
            continue
        title = _clean(d.get("title_display"))
        kind, stype = _kind(title, d.get("article_type") or "")
        out.append(Candidate("plos", title, f"https://doi.org/{d['id']}", publisher=d.get("journal") or "PLOS",
                             year=str(d.get("publication_date", ""))[:4], doi=d["id"], abstract=abstract,
                             licence="CC BY 4.0 (PLOS)", kind=kind, source_type=stype))
    return out


def core(term: str, n: int) -> list[Candidate]:
    key = os.environ.get("CORE_API_KEY")
    if not key:
        return []
    url = f"https://api.core.ac.uk/v3/search/works?q={_q(chr(34) + term + chr(34))}&limit={n}"
    out = []
    for r in _json(url, headers={"Authorization": f"Bearer {key}"}).get("results", []):
        abstract = _clean(r.get("abstract"))
        if not abstract:
            continue
        title = _clean(r.get("title"))
        kind, stype = _kind(title)
        link = r.get("doi") and f"https://doi.org/{r['doi']}" or (r.get("links") or [{}])[0].get("url", "")
        out.append(Candidate("core", title, link, publisher=r.get("publisher") or "CORE", year=str(r.get("yearPublished") or ""),
                             doi=r.get("doi") or "", abstract=abstract, licence="<verify>", kind=kind, source_type=stype))
    return out


def medlineplus(term: str, n: int) -> list[Candidate]:
    url = f"https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term={_q(term)}&retmax={n}"
    root = ET.fromstring(_get(url))
    out = []
    for doc in root.iter("document"):
        fields: dict[str, list[str]] = {}
        for c in doc.findall("content"):
            fields.setdefault(c.get("name", ""), []).append(_clean(c.text))
        title = (fields.get("title") or [""])[0]
        summary = (fields.get("FullSummary") or [""])[0]
        if not summary:
            continue
        out.append(Candidate("medlineplus", title, doc.get("url", ""), publisher="MedlinePlus (National Library of Medicine)",
                             abstract=summary, licence="U.S. government work (public domain)", kind="patient page",
                             source_type="government_health_page", audience="patient", permitted_use="public_domain",
                             score=1.0))
    return out


PROVIDERS = {"medlineplus": medlineplus, "europepmc": europepmc, "semanticscholar": semanticscholar, "doaj": doaj,
             "openaire": openaire, "plos": plos, "hal": hal, "zenodo": zenodo, "core": core}


# ---------------------------------------------------------------- collect, rank, pack

def _keys(c: Candidate) -> list[str]:
    """A paper is the same if its DOI or its title matches (repositories give one paper several DOIs)."""
    keys = ["t:" + re.sub(r"[^a-z0-9]+", "", c.title.lower())[:80]]
    if c.doi:
        keys.append("d:" + c.doi.lower().removeprefix("https://doi.org/"))
    return keys


def relevant(c: Candidate, terms: list[str]) -> bool:
    hay = f"{c.title} {c.abstract}".lower()
    return any(t.lower() in hay for t in terms if t)


KIND_SCORE = {"guideline": 3.0, "systematic review": 2.5, "patient page": 2.4, "review": 2.0, "trial": 1.4,
              "article": 1.0, "preprint": 0.6, "case report": 0.3}


def rank(c: Candidate, terms: list[str]) -> float:
    s = KIND_SCORE.get(c.kind, 1.0) + c.score
    if c.permitted_use in ("open_license", "public_domain"):
        s += 1.0
    if any(t.lower() in c.title.lower() for t in terms):
        s += 1.0
    try:
        s += max(0, int(c.year) - 2010) * 0.04
    except ValueError:
        pass
    if len(c.abstract) < 300:
        s -= 1.0
    return round(s, 3)


def collect(term: str, alternate_terms: list[str] | None = None, per_provider: int = 8,
            providers: list[str] | None = None, log=print, search_alternates: bool = True,
            min_found: int = 15) -> list[Candidate]:
    """Query every provider for the topic and return relevant, de-duplicated candidates, best first.
    When fewer than `min_found` turn up, the alternate names are searched too."""
    terms = [term, *(alternate_terms or [])]
    found: dict[str, Candidate] = {}
    for name in providers or list(PROVIDERS):
        fn = PROVIDERS[name]
        try:
            got = fn(term, per_provider)
        except Exception as e:  # one provider being down must not stop the others
            log(f"  {name}: skipped ({type(e).__name__}: {str(e)[:80]})")
            continue
        kept = 0
        for c in got:
            if not c.title or not c.url or not relevant(c, terms):
                continue
            if c.permitted_use != "public_domain":
                c.permitted_use = classify_licence(c.licence)
            c.score = rank(c, terms)
            keys = _keys(c)
            old = next((found[k] for k in keys if k in found), None)
            if old is not None:  # same paper from several providers: keep the richer record, remember both
                old.providers = sorted({*old.providers, old.provider, name})
                if len(c.abstract) > len(old.abstract):
                    old.abstract = c.abstract
                for k in keys:
                    found.setdefault(k, old)
                continue
            c.providers = [name]
            for k in keys:
                found[k] = c
            kept += 1
        log(f"  {name}: {kept} new of {len(got)}")
        if name == "semanticscholar":
            time.sleep(1.2)  # its shared anonymous rate limit
    unique = list({id(c): c for c in found.values()}.values())
    if len(unique) < min_found and search_alternates:  # thin results: papers often use another name
        for alt in alternate_terms or []:
            log(f"  few results; also searching '{alt}'")
            more = collect(alt, [term, *terms], per_provider, providers, log, search_alternates=False)
            have = {k for c in unique for k in _keys(c)}
            unique += [c for c in more if not set(_keys(c)) & have]
    return sorted(unique, key=lambda c: c.score, reverse=True)


def pick_pack(candidates: list[Candidate], patient: bool = True, size: int = 4) -> list[Candidate]:
    """A balanced source pack: a patient page first (for patient KOs), then the best research sources,
    preferring different kinds (guideline / review / trial)."""
    pack: list[Candidate] = []
    if patient:
        pack += [c for c in candidates if c.provider == "medlineplus"][:1]
    seen_kinds: set[str] = set()
    for c in candidates:
        if len(pack) >= size:
            break
        if c in pack or c.provider == "medlineplus":
            continue
        others = [x for x in candidates if x not in pack and x.provider != "medlineplus"]
        if c.kind in seen_kinds and any(x.kind not in seen_kinds for x in others):
            continue
        pack.append(c)
        seen_kinds.add(c.kind)
    for c in candidates:  # top up if kinds ran out
        if len(pack) >= size:
            break
        if c not in pack:
            pack.append(c)
    return pack


def as_source(c: Candidate, sid: str, today: str | None = None) -> dict[str, Any]:
    """A KO `sources` entry (plus its text, for the source pack)."""
    note = f"Found via {', '.join(c.providers or [c.provider])}. Licence: {c.licence or 'not stated'}."
    if c.kind not in ("patient page",):
        note += f" Type: {c.kind}. Text kept: abstract only."
    return {"id": sid, "title": c.title, "publisher": c.publisher or c.provider, "url": c.url,
            "source_type": c.source_type, "audience": c.audience, "publication_date": c.year or "<verify>",
            "retrieved_date": today or dt.date.today().isoformat(), "permitted_use": c.permitted_use,
            "evidence_strength": None, "notes": note[:300], "text": c.abstract}


def render_pack(ko_id: str, term: str, sources: list[dict[str, Any]]) -> str:
    """Source pack file (same format as the Generator's): metadata plus the text each source contributes."""
    import yaml

    lines = [f"# Source pack SP-{ko_id} ({term})", ""]
    for s in sources:
        lines.append(f"## {s.get('id')}")
        meta = {k: v for k, v in s.items() if k != "text"}
        lines.append(yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100).strip())
        lines.append("text: |")
        text = (s.get("text") or "").strip() or "<no text provided>"
        lines.extend("  " + line for line in text.split("\n"))
        lines.append("")
    return "\n".join(lines)


def save_candidates(path: Path, term: str, candidates: list[Candidate]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"term": term, "collected": dt.date.today().isoformat(), "count": len(candidates),
               "candidates": [asdict(c) for c in candidates]}
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")


def load_candidates(path: Path) -> list[Candidate]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [Candidate(**c) for c in data["candidates"]]
