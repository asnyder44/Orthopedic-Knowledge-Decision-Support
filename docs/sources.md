# Sources and permitted use

"Publicly available" is not the same as "free to reuse". This project collects only
material whose owner permits reuse, records the licence on every document, and
shows it beside every result. **Have the sponsor confirm this table before anything
is published outside the class.**

## Collected (`config/sources.toml`)

| Source | Type | Audience | Licence / terms | How collected |
|---|---|---|---|---|
| [MedlinePlus](https://medlineplus.gov/xml.html) health topics, group "Bones, Joints and Muscles" | patient_education | patients | NLM-written summaries are public domain; credit MedlinePlus ([terms](https://medlineplus.gov/about/using/usingcontent/)) | Official daily bulk XML |
| [NIAMS](https://www.niams.nih.gov/health-topics) health topics (NIH) | patient_education | patients | U.S. federal government work: public domain. Images excluded | Web pages; robots.txt honoured |
| [OpenStax *Anatomy and Physiology 2e*](https://openstax.org/details/books/anatomy-and-physiology-2e), ch. 6–11 | textbook | students | CC BY 4.0 — attribute OpenStax | Web pages listed in the book sitemap; robots.txt honoured |
| [Europe PMC](https://europepmc.org/) open-access full text (the PMC Open Access subset) | research_article | clinicians, researchers | Per article; only CC BY, CC BY-SA, CC0 collected | Europe PMC REST API |
| [Wikipedia](https://en.wikipedia.org/) articles matched to each topic | encyclopedia | general | CC BY-SA 4.0 — attribute, share alike | MediaWiki API |

MedlinePlus also lists curated links for each topic (AAOS OrthoInfo, Mayo Clinic,
NIH institutes…). These are stored as **links only** (`related_links`) and shown on
topic pages; their content is not collected.

## Considered and not collected

| Source | Why not | What would be needed |
|---|---|---|
| Commercial textbooks and most books | Copyrighted; no reuse permission | Licence from the publisher, or the library's licensed access (not redistribution) |
| [AAOS OrthoInfo](https://orthoinfo.aaos.org/) | Copyrighted; terms restrict copying | Written permission from AAOS; until then, link to it |
| Paywalled journal articles; abstracts of non-OA articles | Publisher copyright | Use only the citation and link |
| StatPearls / [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/) | Bookshelf pages answer scripts with a CAPTCHA (we do not work around it); licence is CC BY-NC-ND | NCBI's open-access bulk download (`ftp.ncbi.nlm.nih.gov/pub/litarch/`) and a decision on the NC-ND terms |
| MedlinePlus Medical Encyclopedia (A.D.A.M.) | Licensed to NLM; not reusable | Link only |
| Europe PMC articles under CC BY-NC / NC-ND | Non-commercial / no-derivatives terms | Add `"cc by-nc"` etc. to `licenses` if the sponsor accepts those terms |

## Getting more

- **More research:** raise `max_per_query`, add `queries`, or remove `filter` (which keeps
  reviews, systematic reviews, meta-analyses and guidelines). The search reports how many
  matching articles exist for each query.
- **More patient information:** add MedlinePlus `groups` (e.g. "Injuries and Wounds") or
  NIAMS `index_pages`.
- **A new source:** add a module to `src/orthoinfo/sources/` with `collect()` and `parse()`
  (see `sources/__init__.py`), add it to `SOURCES`, and add a row to this table first.

## Quality caveat

More text is not better answers by itself. Research articles are written for clinicians
and report single findings; Wikipedia is not clinically reviewed. The app therefore
searches patient-education sources by default and labels every other type. Evaluate
whether adding a source type improves results for the target users before turning it on
by default (`orthoinfo evaluate --types ...`).
