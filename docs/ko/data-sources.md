# Reliable Data Sources for OKDS

The full catalog (72 sources) is in [`data/sources/source_catalog.csv`](../data/sources/source_catalog.csv)
and in the portal's **Data Sources** tab. It was checked on 2026-10-24.
- **verified = yes:** the official page was opened.
- **partial:** the page loaded, but some details could not be read.
- **unverified:** the site blocked automated checks. Check it in a browser.

## Best sources by view

| View | Use first | Why |
|---|---|---|
| **Patient** (plain language) | MedlinePlus (NLM), NIAMS (NIH), NINDS (NIH) | Trusted US government pages. Most text is public domain (cite it) |
| | AAOS OrthoInfo, NASS Know Your Back, AOSSM STOP | Expert society pages. **Copyrighted: link and paraphrase only** |
| **Clinical** (guidelines) | AAOS Clinical Practice Guidelines + OrthoGuidelines, ACR Appropriateness Criteria (imaging), APTA Orthopedics CPGs (rehab) | Evidence-graded recommendations. Cite the recommendation and its strength |
| **Research** | PubMed E-utilities, PMC Open Access (license per article), Europe PMC, OpenAlex (CC0) | Free APIs. Use them to find and cite studies |
| **Trials** | ClinicalTrials.gov API v2 | Public trial records (entity records, not KOs) |
| **Industry / devices** | openFDA device APIs (510(k), PMA, recalls, UDI), AccessGUDID, eCFR 21 CFR Part 888 | Public-domain device and regulatory data |
| **Outcomes / registries** | AJRR (US), UK NJR, Australian AOANJRR annual reports, PROMIS | Implant and outcome trends. Summarize and cite |
| **Policy / burden** | BMUS, CDC (arthritis, WISQARS), NEISS, HCUPnet, IHME GBD | How common and costly MSK problems are |
| **Codes** (for tagging KOs) | MeSH, ICD-10-CM, NLM Clinical Tables API | Free. UMLS, SNOMED CT, and LOINC need a free license or account |
| **Indiana ecosystem** | IU Ortho Surgery, Indiana Center for Musculoskeletal Health, mskimpact.org, Regenstrief, Indiana CTSI, BioCrossroads, Zimmer Biomet, DePuy Synthes, OrthoPediatrics | Local experts, partners, and companies (Warsaw, IN) |

## Rules before using a source

1. **US government text** (MedlinePlus summaries, NIAMS, openFDA, eCFR) is usually public domain. Still cite it.
   MedlinePlus's A.D.A.M. encyclopedia and drug pages are copyrighted.
2. **Society, hospital, and company pages are copyrighted.** Paraphrase and link. Never copy text.
   Cleveland Clinic even asks for permission before linking, so use it only as background reading.
3. **Patient-level data needs approvals:** Regenstrief/INPC, IHIE, Indiana Biobank, HCUP files, OAI, MOST,
   and fastMRI need IRB approval, a data use agreement, or an application. They are marked `restricted` and are **never** used in KOs or OrthoBot.
4. **Watch for non-commercial licenses:** Radiopaedia (CC BY-NC-SA; no commercial AI training), IHME GBD (non-commercial),
   Semantic Scholar (attribution required, no redistribution).
5. **openFDA adverse-event (MAUDE) reports** are unverified reports. Do not present them as complication rates.

## Dead or moved links found (2026-10-24)

- boneandjointburden.org now goes to an unrelated site. Use `bmus.latticegroup.com`.
- PatentsView moved to the USPTO Open Data Portal (`data.uspto.gov`).
- stopsportsinjuries.org redirects elsewhere. The tip sheets are on sportsmed.org.
- The PMC OA Web Service was retired in 2026. Use the PMC Cloud Service, OAI-PMH, or the BioC API.
- **OrthoWorx has no working website** (orthoworx.org does not resolve). Ask the sponsor for the current link.
