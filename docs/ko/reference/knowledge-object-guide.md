> Reference copy for the okds repo (copied 2026-11-01). Appendix A was shortened because it pointed to files outside this repo.

# Knowledge Object (KO) Guide for OKDS

**What a KO is, how to format one, and how to build a KO Generator and Reviewer for Orthopedic Knowledge & Decision Support**

**Audience:** the AI agent (and team) working on the Orthopedic Knowledge & Decision Support (OKDS) project.
**Written:** 2026-10-24. It is based on the Spring 2026 PQC project, which has the same sponsor, Kyle Stirling, and used KOs as its core unit.
**Status:** recommended design. Confirm the choices marked *(decide)* with the user or Kyle before building at scale.

---

## 0. How to use this guide

| If you need to… | Read |
|---|---|
| Understand what a KO is and why Kyle wants it | §1 |
| Avoid the mistakes the PQC team made | §2 |
| Learn the rules every KO must follow | §3 |
| Set up the orthopedic vocabulary (types, links, IDs, clusters) | §4 |
| See the exact KO file format | §5 |
| Copy a complete example KO | §6 |
| Build the KO Generator (prompt + pipeline) | §7 |
| Build the KO Reviewer | §8 |
| Validate KOs automatically | §9 |
| Load KOs into MongoDB, Neo4j, or Postgres | §10 |
| Start work immediately | §11 |

**One-paragraph summary:**
- A KO is a short, structured file about **one orthopedic concept**, such as a condition, procedure, test, or device. It has fixed metadata, plain-language content, a source for every claim, and typed links to other KOs.
- KOs are written in **Markdown with a YAML header**. The Markdown is the source of truth; it is converted to JSON for the database and to nodes and edges for the graph.
- A **KO Generator** (an LLM prompt plus a small script) drafts KOs **only from a provided source pack**.
- A **KO Reviewer** (an LLM rubric plus human checks) scores them.
- A **validator script** enforces the format before anything is loaded.

---

## 1. What a Knowledge Object is

### 1.1 Definition

Kyle defines it in his paper draft *Knowledge Objects in the Age of LLMs*:

> A Knowledge Object is a discrete, self-contained unit of semantically annotated knowledge designed to be **interpretable by humans, navigable by machines, linked to precursor knowledge, and composable across contexts.**

Every KO has four parts:

| Part | What it holds | Orthopedic example |
|---|---|---|
| **Core content** | The explanation of the concept | What carpal tunnel syndrome is, its symptoms, how it is diagnosed |
| **Metadata & tags** | ID, type, specialty, audience, difficulty, version, dates | `KO-HAND-COND-001`, Condition, Hand & Upper Extremity, Patient |
| **Provenance** | Sources, author, reviewer, review status, history | MedlinePlus, NINDS, AAOS OrthoInfo; reviewed by a clinician on a given date |
| **Interfaces / links** | Typed links to other KOs, plus a machine-readable form (YAML/JSON) | Carpal Tunnel Syndrome → DIAGNOSED_BY → Nerve Conduction Study |

### 1.2 What a KO is not

- **Not an article or web page.** An article mixes many concepts. A KO covers **one**, so it can be reused on many pages, in many learning paths, and in many chatbot answers.
- **Not a random text chunk.** RAG chunks are arbitrary slices of text. A KO is curated, versioned, and has a stable ID, so an answer can cite "KO-HAND-COND-001 v1.2," and that citation means something.
- **Not a rigid database row.** The metadata is the same for every KO, but the body adapts to the concept type. A procedure KO has "recovery timeline"; a condition KO has "symptoms."

### 1.3 Why KOs matter for OKDS

KOs are the base layer that everything else is built on:

```
Trusted sources (MedlinePlus, NIH, AAOS, PubMed, FDA...)
        │  source pack → KO Generator → validator → reviewer
        ▼
  Knowledge Objects (Markdown + YAML)   ← source of truth
        │
        ├─► Database (MongoDB or Postgres): full KO documents, used for search and pages
        └─► Graph (Neo4j): concepts + typed links, used for paths and connected answers
                  │
     ┌────────────┼─────────────────────┬──────────────────────┐
     ▼            ▼                     ▼                      ▼
 Website pages  Learning/“patient    OrthoBot (RAG):        Evaluation set
 (one per KO)   journey” paths       answers cite KO IDs    (test questions
                                     and sources            inside KOs)
```

**This directly fixes the gaps Kyle found in the OKDS prototype** (2026-10-12 review):

| Kyle's gap | KO fix |
|---|---|
| Citations are broad pages, not tied to claims | Each claim carries a source marker like `[S1]` |
| No named reviewers or review dates | `review` metadata block |
| Content is general and unconnected | Typed links between conditions, tests, treatments, and procedures |
| The audience is unclear | `audience` and `reading_level` fields |

### 1.4 Kyle's knowledge-engineering principles (follow these)

These come from his learning note *Knowledge Graphs and Knowledge Engineering*:
1. **Schema first.** Define types and links *before* generating content. "Humans first, AI in the loop."
2. **Nodes are real concepts.** Test: can you define it in one sentence? If not, it isn't a node.
3. **Relationships are verbs with meaning.** They must change understanding, not just connect things. **Avoid `related_to` and `associated_with`.**
4. **Controlled vocabulary.** One concept = one name, and one relationship = one verb. "Vocabulary drift breaks your graph."
5. **Properties describe nodes; tags are only for search.** A tag is not a concept.
6. **Entity linking.** Map every mention ("CTS," "carpal tunnel") to one canonical node.
7. **Governance.** Use Contributor → Reviewer → Approver roles. Every KO records its source, author, and version.
8. **"LLMs assist — but do not define truth."**

---

## 2. Lessons from the PQC project (do not repeat these)

The PQC team (Spring 2026) produced 85 KOs, but ran into these problems. Each one has a rule in this guide that prevents it.

| PQC problem | What went wrong | Prevention in this guide |
|---|---|---|
| **Three KO formats** | The format changed mid-project, and old KOs were never migrated | One schema with a `schema_version`; the validator rejects anything else (§5, §9) |
| **Duplicate IDs; filenames used as IDs** | IDs were typed by hand or by the LLM | IDs come from a registry and are assigned by the script, never by the LLM (§4.4) |
| **Same concept in two places** (for example, Shor's algorithm in 2 clusters) | No concept list existed before writing | Build the **concept registry first**; one concept = one KO (§4.4) |
| **9 cluster labels for 8 clusters; 16 categories** | Labels were free text | Enumerated values only (§4) |
| **192 free-text link targets for 85 KOs** | Links pointed to names, not IDs | Links must target **registry IDs**; new concepts are flagged, not invented (§4.2) |
| **Three different relationship vocabularies** | The prompt, the slides, and the code each used their own | One `vocab.yaml` is used by the generator, validator, and loader (§4) |
| **"Source-grounded" was self-declared by the LLM** | The LLM searched the web itself and certified its own output | Generate **only from a provided source pack**; only humans set reviewed statuses (§7, §8) |
| **No author or reviewer fields** | They weren't in the schema | A required `review` block (§5) |
| **Only 8 of 85 KOs made it into the database** | Content came before the pipeline | Build the pipeline on 3–5 KOs first, then scale (§11) |
| **The LLM-extracted graph was noisy** | They used automatic entity extraction (Neo4j LLM Graph Builder) | Build the graph **from KO links only**, with schema-first loading (§10) |
| **Loader notebook bug** (a `#` comment inside a Cypher string) | No tests | The validator plus a small load test (§9, §10) |

**What worked well and should be reused:**
- the KO body sections (overview, evidence snapshot, misunderstandings, test questions)
- the reviewer rubric
- "Markdown is the source of truth; JSON is a build artifact"
- a "SOURCE PACK NEEDED" fallback
- an "Update triggers" section
- a short canonical definition for grounding the LLM

---

## 3. Rules every KO must follow

1. **One KO = one primary concept.** "Knee problems" is too broad. "Meniscus tear" is right.
2. **Every factual claim has a source marker** (`[S1]`, `[S2]`) that points to an entry in `sources`.
3. **Never invent** a source, URL, date, code, statistic, or quote. If something is unknown, write `"<verify>"` and add a note in `review.open_issues`.
4. **Links point to registry IDs**, never to free text. Use only the predicates allowed in `vocab.yaml`.
5. **Medical safety:**
   - Give education only, never personal advice.
   - No dosing instructions.
   - Point the reader to a clinician.
   - Include "When to seek care" for conditions, using sourced content.
   - Set `safety.not_medical_advice: true`.
6. **Respect source terms.** Paraphrase. Never copy long passages. Record each source's `permitted_use`. (AAOS OrthoInfo is copyrighted: link to it and paraphrase.)
7. **Use plain language** for patient-audience KOs (target grade 6–8 reading level). Define every medical term on first use.
8. **Status rules:** LLMs may only set `draft` or `ai_checked`. Only people set `team_checked`, `clinician_reviewed`, or `published` (§8.3).
9. **Versioning:** any content change raises the `version` number and adds a `change_log` entry. IDs never change.
10. **Markdown is the source of truth.** Database and graph copies are always regenerated from it, never edited by hand.

---

## 4. OKDS vocabulary (set this up before generating anything)

Store everything in this section in one file, `schema/vocab.yaml`, read by the generator prompt, the validator, and the loaders. The values below are a **recommended starting point** *(decide)*.

### 4.1 KO types (ontology classes)

**Concept KOs** are written explanations, one per concept:

| `ko_type` | ID code | What it is | Example |
|---|---|---|---|
| `Condition` | COND | A disease, injury, or disorder | Carpal tunnel syndrome, ACL tear, hip osteoarthritis |
| `AnatomicalStructure` | ANAT | A body part relevant to orthopedics | Median nerve, carpal tunnel, meniscus |
| `DiagnosticTest` | DX | An exam maneuver, imaging test, or lab/electrodiagnostic test | Phalen's test, MRI of the knee, nerve conduction study |
| `Treatment` | TRT | A non-surgical treatment | Wrist splinting, corticosteroid injection, physical therapy |
| `Procedure` | PROC | A surgical procedure | Carpal tunnel release, total knee arthroplasty |
| `Device` | DEV | An implant, instrument, or brace category | Knee implant, wrist splint |
| `RehabProtocol` | REHAB | A recovery or rehabilitation plan | Rehab after ACL reconstruction |
| `OutcomeMeasure` | OUT | A way of measuring results | Boston Carpal Tunnel Questionnaire, KOOS |
| `Concept` | CONC | A general idea or clarification | "What is an orthopedic surgeon?", "Arthroscopy vs open surgery" |

**Entity records** are data rows, **not** hand-written KOs. They come from APIs and are linked to KOs:

| Record type | Source | Linked by |
|---|---|---|
| `Organization` (company, hospital, lab) | Company and university sites, OrthoWorx | `MANUFACTURED_BY`, `LOCATED_IN` |
| `ClinicalTrial` | ClinicalTrials.gov API | `STUDIED_IN` |
| `RegulatoryClearance` | openFDA (510(k), PMA, GUDID) | `CLEARED_AS` |
| `Patent` | PatentsView | `PATENTED_AS` |
| `Guideline` | AAOS clinical practice guidelines | `RECOMMENDED_BY` |
| `Researcher` / `Grant` | NIH RePORTER | `STUDIES` |

> **Why separate them:** a trial or patent doesn't need a written explanation. It needs accurate fields from its source. Writing KOs for thousands of records would be slow and error-prone.

### 4.2 Relationship vocabulary (closed list)

Rules:
- Use UPPER_SNAKE_CASE.
- Each predicate has **one direction** and allowed subject and object types.
- Don't add new predicates without updating `vocab.yaml`.

| Predicate | Subject → Object | Meaning |
|---|---|---|
| `AFFECTS` | Condition → AnatomicalStructure | The condition involves this body part |
| `PART_OF` | AnatomicalStructure → AnatomicalStructure | Anatomy hierarchy |
| `HAS_SYMPTOM` | Condition → Concept (symptom) | A typical symptom *(decide: separate Symptom type?)* |
| `HAS_RISK_FACTOR` | Condition → Concept (risk factor) | Raises the chance of the condition |
| `DIAGNOSED_BY` | Condition → DiagnosticTest | The test is used to diagnose the condition |
| `TREATS` | Treatment/Procedure → Condition | Used to treat the condition |
| `ALTERNATIVE_TO` | Treatment/Procedure → Treatment/Procedure | A reasonable alternative option (store both directions) |
| `USES_DEVICE` | Procedure/Treatment → Device | The procedure uses this device |
| `FOLLOWED_BY` | Procedure → RehabProtocol | Standard recovery after the procedure |
| `MEASURED_BY` | Condition/Procedure → OutcomeMeasure | How results are measured |
| `COMPLICATION_OF` | Condition → Procedure/Condition | A known complication |
| `CONTRASTS_WITH` | any → same type | Often confused but different (for example, carpal tunnel vs cubital tunnel) |
| `PREREQUISITE_FOR` | any KO → any KO | Read this first (builds learning paths) |
| `BELONGS_TO_SPECIALTY` | any KO → Specialty | Specialty grouping |
| `RECOMMENDED_BY` | Treatment/Procedure/DiagnosticTest → Guideline record | A guideline addresses it (store strength as an edge property) |
| `MANUFACTURED_BY` | Device → Organization | Maker |
| `STUDIED_IN` | Treatment/Procedure/Device → ClinicalTrial | A trial studies it |
| `CLEARED_AS` | Device → RegulatoryClearance | FDA clearance or approval |
| `PATENTED_AS` | Device → Patent | Related patent |
| `LOCATED_IN` | Organization → Location | For the Indiana ecosystem map |

**Edge properties (optional):**
- `source_ids`: which `[S#]` sources support the link
- `strength`: the guideline's own scale, for example "Strong" or "Moderate"
- `note`

**Forbidden:** `RELATED_TO`, `ASSOCIATED_WITH`, and lowercase or variant spellings.

### 4.3 Fixed value lists (enums)

| Field | Allowed values |
|---|---|
| `specialty` | `SPORT` Sports Medicine, `SPINE` Spine, `TRAUMA` Trauma, `HAND` Hand & Upper Extremity, `JOINT` Joint Reconstruction, `FOOT` Foot & Ankle, `GEN` General. (These match the 6 prototype areas plus General.) |
| `audience` | `patient`, `caregiver`, `student`, `clinician`, `researcher`, `industry` |
| `difficulty` | `beginner`, `intermediate`, `advanced` |
| `review.status` | `draft`, `ai_checked`, `team_checked`, `clinician_reviewed`, `published`, `retired` |
| `source_type` | `guideline`, `government_health_page`, `patient_education`, `journal_article`, `systematic_review`, `textbook`, `regulatory`, `trial_registry`, `patent`, `organization_site`, `other` |
| `permitted_use` | `public_domain`, `open_license` (state which), `link_and_paraphrase`, `restricted` (do not use), `<verify>` |

### 4.4 IDs and the concept registry

- **KO ID format:** `KO-<SPECIALTY>-<TYPE>-<NNN>`, for example `KO-HAND-COND-001`, `KO-HAND-DX-003`, `KO-JOINT-PROC-002`.
- IDs are **assigned by a script** from `schema/registry.csv`. They are **never reused or changed**.
- **Make the concept registry first.** Before generating KOs, list every planned concept: ID, preferred term, alternate terms, type, specialty, and external codes. This prevents duplicates and gives the generator a fixed set of link targets.

`schema/registry.csv` example:
```csv
ko_id,preferred_term,alternate_terms,ko_type,specialty,mesh_id,icd10cm,status
KO-HAND-COND-001,Carpal Tunnel Syndrome,"CTS; median nerve compression at the wrist",Condition,HAND,<verify>,G56.0-,planned
KO-HAND-ANAT-001,Median Nerve,,AnatomicalStructure,HAND,<verify>,,planned
KO-HAND-ANAT-002,Carpal Tunnel,,AnatomicalStructure,HAND,<verify>,,planned
KO-HAND-DX-001,Nerve Conduction Study,"NCS; electrodiagnostic testing",DiagnosticTest,HAND,<verify>,,planned
KO-HAND-TRT-001,Wrist Splinting,"wrist brace; night splint",Treatment,HAND,,,planned
KO-HAND-TRT-002,Corticosteroid Injection,"steroid shot",Treatment,HAND,,,planned
KO-HAND-PROC-001,Carpal Tunnel Release,"CTR; open release; endoscopic release",Procedure,HAND,<verify>,,planned
KO-HAND-COND-002,Cubital Tunnel Syndrome,"ulnar nerve entrapment at the elbow",Condition,HAND,<verify>,,planned
```

**External codes** (for entity linking and future data joins):
- **MeSH** and **ICD-10-CM** are free to use.
- **SNOMED CT** needs a UMLS license.
- **CPT** procedure codes are licensed by the AMA, so don't store them without permission.

### 4.5 Clusters (grouping KOs for learning)

PQC used 8 topic clusters chosen by Kyle, but had **no written rule** for which KO went where. For OKDS, use **patient-journey stages** and **assign clusters by rule from `ko_type`**, so no judgment calls are needed *(decide)*:

| Cluster | Name | Assigned automatically from `ko_type` |
|---|---|---|
| 1 | Body basics | AnatomicalStructure |
| 2 | Understand the condition | Condition |
| 3 | Getting diagnosed | DiagnosticTest |
| 4 | Treatment without surgery | Treatment |
| 5 | Surgery and devices | Procedure, Device |
| 6 | Recovery and results | RehabProtocol, OutcomeMeasure |
| 7 | Good to know | Concept |

The cluster is a "chapter" for navigation. The **graph links** drive the actual learning paths (`PREREQUISITE_FOR`).

---

## 5. KO file format (OKDS v1.0)

### 5.1 File layout

- One file per KO: `kos/<specialty>/<ko_id>_<slug>.md`, for example `kos/hand/KO-HAND-COND-001_carpal-tunnel-syndrome.md`.
- Each file is a **YAML front matter block** (machine-readable) followed by a **Markdown body** (human-readable, with fixed headings).

### 5.2 YAML front matter fields

| Field | Type | Req. | Notes |
|---|---|:-:|---|
| `schema_version` | string | ✓ | `"okds-ko-1.0"` |
| `ko_id` | string | ✓ | From the registry (§4.4) |
| `title` | string | ✓ | Human title |
| `preferred_term` | string | ✓ | Canonical name, matching the registry |
| `alternate_terms` | string[] | | Synonyms and abbreviations, used for search and entity linking |
| `ko_type` | enum | ✓ | §4.1 |
| `specialty` | enum | ✓ | §4.3 |
| `cluster` | int | ✓ | Set by rule from `ko_type` (§4.5) |
| `audience` | enum[] | ✓ | Primary audience first |
| `reading_level` | string | ✓ | For example "grade 6–8" for patients |
| `difficulty` | enum | ✓ | §4.3 |
| `summary` | string | ✓ | **1–3 sentence canonical definition**. It is used as the grounding text for the chatbot (Kyle's "LLM guardrail snippet") and must be sourced. |
| `codes` | object | | `mesh`, `icd10cm`, `snomed` (if licensed). Use `"<verify>"` if unsure. |
| `tags` | string[] | | Search keywords only; tags are not concepts |
| `relationships` | object[] | ✓ | Each has `predicate`, `target_id`, `target_label`, `source_ids[]`, and optional `strength`/`note` |
| `proposed_concepts` | object[] | | Link targets that aren't in the registry yet: `term`, `suggested_type`, `predicate`, `reason` |
| `sources` | object[] | ✓ | At least 2. Fields in §5.3. |
| `review` | object | ✓ | `status`, `author`, `generated_by` (model + prompt version), `ai_check` (score/date), `team_checker`, `clinician_reviewer`, `clinician_role`, `review_date`, `open_issues[]` |
| `safety` | object | ✓ | `not_medical_advice: true`, plus a `scope_note` |
| `version` | string | ✓ | Semantic version, for example `"1.0.0"` |
| `created` / `last_updated` | date | ✓ | ISO `YYYY-MM-DD` |
| `update_triggers` | string[] | ✓ | Events that should reopen the KO, for example "AAOS updates its guideline" |
| `license` | string | ✓ | For our own text, for example `"CC-BY-4.0"` *(decide)* |
| `change_log` | object[] | ✓ | Each has `version`, `date`, `by`, `change` |

### 5.3 Source entry fields

These match Kyle's dataset fields from his 2026-10-12 plan: topic, audience, publisher, URL, publication or review date, retrieval date, and permitted use.

```yaml
- id: S1                        # used as [S1] in the body
  title: "Carpal Tunnel Syndrome"
  publisher: "National Library of Medicine (MedlinePlus)"
  url: "https://medlineplus.gov/carpaltunnelsyndrome.html"
  source_type: government_health_page
  audience: patient
  publication_date: "<verify>"  # or the page's "last reviewed" date
  retrieved_date: 2026-10-24
  permitted_use: link_and_paraphrase
  evidence_strength: null       # for guidelines: the source's own scale
  notes: ""
```

### 5.4 Markdown body: required headings

**Core headings (every KO, in this order):**

| Heading | Content |
|---|---|
| `## Summary` | 2–4 plain sentences. Expands on the front-matter `summary`. |
| `## Key Facts (claim → source)` | 4–10 bullets. Each is **one claim followed by a source marker**, for example "...at the wrist [S1]." This is the trust layer. |
| `## Explanation` | The main content. Subsections depend on the type (§5.5). |
| `## Common Misunderstandings` | 2–5 "**Myth:** … **Fact:** … [S#]" pairs |
| `## Questions to Ask Your Doctor` | 3–6 questions (required for patient or caregiver audiences, optional otherwise) |
| `## Test Questions` | 3–6 questions with short answers and source markers, used for chatbot evaluation |
| `## Related Topics` | A human-readable list of the links, mirroring `relationships` |
| `## References` | Numbered list matching `sources` |

**Optional:** `## Suggested Visuals`, `## Terminology`, `## Open Questions`.

### 5.5 Type-specific `## Explanation` subsections

| `ko_type` | Required `###` subsections |
|---|---|
| Condition | What it is · Causes and risk factors · Symptoms · How it is diagnosed · Treatment options (overview; link to Treatment/Procedure KOs) · **When to seek care** |
| AnatomicalStructure | Where it is · What it does · Conditions that affect it |
| DiagnosticTest | What it checks · How it is done · What results can mean · Limits |
| Treatment | What it is · How it helps · Who it may suit (general, not personal) · Risks and side effects · Evidence summary |
| Procedure | What it is · Why it is done · How it is done (types) · Devices used · Risks · Recovery timeline (typical ranges) · Alternatives |
| Device | What it is · Where it is used · Types · Regulatory status (link to FDA records) · Makers (link to Organization records) |
| RehabProtocol | Goals · Phases and typical timing · Warning signs |
| OutcomeMeasure | What it measures · How it is scored · Where it is used |
| Concept | Explanation · Examples |

### 5.6 How the format maps to storage

| KO part | JSON / MongoDB | Neo4j |
|---|---|---|
| Front matter | Top-level fields | Node properties (`ko_id`, `title`, `ko_type`, `specialty`, `audience`, `version`, `review_status`) |
| `ko_type` | `ko_type` field | Node label, for example `(:KO:Condition)` |
| Body headings | `sections.<snake_case_heading>` plus `raw_markdown` | Not stored (or only `summary`) |
| `relationships` | `relationships[]` array | Edges `(:KO)-[:PREDICATE {source_ids}]->(:KO)` |
| `sources` | `sources[]` array | `(:Source)` nodes plus `(:KO)-[:CITES]->(:Source)` |
| `proposed_concepts` | Array (for review) | **Not loaded** until approved |

---

## 6. Complete example KO

> **Illustrative only.** It shows the format. All facts, codes, URLs, and dates must be checked against the actual sources before use. Fields marked `<verify>` are deliberately left open to show the "never invent" rule.

````markdown
---
schema_version: "okds-ko-1.0"
ko_id: KO-HAND-COND-001
title: "Carpal Tunnel Syndrome"
preferred_term: "Carpal Tunnel Syndrome"
alternate_terms: ["CTS", "median nerve compression at the wrist"]
ko_type: Condition
specialty: HAND
cluster: 2
audience: [patient, caregiver, student]
reading_level: "grade 6–8"
difficulty: beginner
summary: >
  Carpal tunnel syndrome is a condition where the median nerve is squeezed
  as it passes through a narrow space in the wrist called the carpal tunnel.
  This can cause numbness, tingling, and weakness in the hand [S1][S2].
codes:
  mesh: "<verify>"
  icd10cm: "G56.0-"   # verify exact code and laterality
tags: ["hand numbness", "wrist", "nerve", "tingling fingers"]
relationships:
  - {predicate: AFFECTS, target_id: KO-HAND-ANAT-001, target_label: "Median Nerve", source_ids: [S1, S2]}
  - {predicate: AFFECTS, target_id: KO-HAND-ANAT-002, target_label: "Carpal Tunnel", source_ids: [S2]}
  - {predicate: DIAGNOSED_BY, target_id: KO-HAND-DX-001, target_label: "Nerve Conduction Study", source_ids: [S2, S3]}
  - {predicate: CONTRASTS_WITH, target_id: KO-HAND-COND-002, target_label: "Cubital Tunnel Syndrome", source_ids: [S3]}
  - {predicate: PREREQUISITE_FOR, target_id: KO-HAND-PROC-001, target_label: "Carpal Tunnel Release", source_ids: []}
proposed_concepts:
  - {term: "Phalen's Test", suggested_type: DiagnosticTest, predicate: DIAGNOSED_BY, reason: "Common exam maneuver; not yet in registry"}
sources:
  - id: S1
    title: "Carpal Tunnel Syndrome"
    publisher: "National Library of Medicine (MedlinePlus)"
    url: "https://medlineplus.gov/carpaltunnelsyndrome.html"
    source_type: government_health_page
    audience: patient
    publication_date: "<verify>"
    retrieved_date: 2026-10-24
    permitted_use: link_and_paraphrase
  - id: S2
    title: "Carpal Tunnel Syndrome"
    publisher: "National Institute of Neurological Disorders and Stroke (NIH)"
    url: "https://www.ninds.nih.gov/health-information/disorders/carpal-tunnel-syndrome"
    source_type: government_health_page
    audience: patient
    publication_date: "<verify>"
    retrieved_date: 2026-10-24
    permitted_use: "<verify>"
  - id: S3
    title: "Carpal Tunnel Syndrome"
    publisher: "American Academy of Orthopaedic Surgeons (OrthoInfo)"
    url: "https://orthoinfo.aaos.org/en/diseases--conditions/carpal-tunnel-syndrome/"
    source_type: patient_education
    audience: patient
    publication_date: "<verify>"
    retrieved_date: 2026-10-24
    permitted_use: link_and_paraphrase   # copyrighted: never copy text
review:
  status: draft
  author: "KO Generator"
  generated_by: {model: "<model name>", prompt_version: "okds-gen-1.0"}
  ai_check: null
  team_checker: null
  clinician_reviewer: null
  clinician_role: null
  review_date: null
  open_issues:
    - "Verify MeSH ID and ICD-10-CM code."
    - "Add AAOS clinical practice guideline as a source (URL and date unknown)."
safety:
  not_medical_advice: true
  scope_note: "General education only. Not a diagnosis or treatment plan."
version: "0.1.0"
created: 2026-10-24
last_updated: 2026-10-24
update_triggers:
  - "AAOS publishes or updates its carpal tunnel syndrome guideline."
  - "Any cited page shows a new 'last reviewed' date."
license: "CC-BY-4.0"
change_log:
  - {version: "0.1.0", date: 2026-10-24, by: "KO Generator", change: "Initial draft from source pack SP-HAND-COND-001."}
---

## Summary
Carpal tunnel syndrome (CTS) happens when the median nerve, a nerve that runs
from the forearm into the hand, is squeezed inside the wrist [S1][S2]. People
often feel numbness or tingling in the thumb and first fingers [S2][S3].

## Key Facts (claim → source)
- The median nerve passes through the carpal tunnel, a narrow passage in the wrist [S2].
- Common symptoms are numbness, tingling, and pain in the thumb, index, middle, and part of the ring finger [S2][S3].
- Symptoms are often worse at night [S3].
- Diagnosis usually uses a medical history, a physical exam, and sometimes a nerve conduction study [S2][S3].
- Non-surgical treatments include wrist splinting and corticosteroid injections [S2][S3].
- Surgery (carpal tunnel release) may be an option when symptoms are severe or do not improve [S2][S3].

## Explanation
### What it is
...
### Causes and risk factors
...
### Symptoms
...
### How it is diagnosed
...
### Treatment options
See: Wrist Splinting (KO-HAND-TRT-001), Corticosteroid Injection (KO-HAND-TRT-002),
Carpal Tunnel Release (KO-HAND-PROC-001).
### When to seek care
...  (sourced)

## Common Misunderstandings
- **Myth:** Only people who type a lot get CTS. **Fact:** Many factors can play a role [S2].
- **Myth:** CTS and cubital tunnel syndrome are the same. **Fact:** They affect different nerves at different places [S3].

## Questions to Ask Your Doctor
1. What tests do I need to confirm carpal tunnel syndrome?
2. Which non-surgical treatments should I try first?
3. When would surgery make sense for me?

## Test Questions
1. Which nerve is affected in CTS? — The median nerve [S1][S2].
2. Name one non-surgical treatment for CTS. — Wrist splinting or corticosteroid injection [S2].
3. What test measures how well the nerve carries signals? — A nerve conduction study [S2].

## Related Topics
- Affects: Median Nerve, Carpal Tunnel
- Diagnosed by: Nerve Conduction Study
- Often confused with: Cubital Tunnel Syndrome
- Read next: Carpal Tunnel Release

## References
1. [S1] MedlinePlus. *Carpal Tunnel Syndrome.* https://medlineplus.gov/carpaltunnelsyndrome.html (retrieved 2026-10-24)
2. [S2] NINDS. *Carpal Tunnel Syndrome.* https://www.ninds.nih.gov/health-information/disorders/carpal-tunnel-syndrome (retrieved 2026-10-24)
3. [S3] AAOS OrthoInfo. *Carpal Tunnel Syndrome.* https://orthoinfo.aaos.org/en/diseases--conditions/carpal-tunnel-syndrome/ (retrieved 2026-10-24)
````

---

## 7. The KO Generator

### 7.1 What it is

The KO Generator is **an LLM prompt plus a small script**. Given one concept from the registry and a **source pack** (the source texts for that concept), it writes one KO draft in the exact format of §5.

### 7.2 Key design choice: grounded in a source pack, not web search

- The PQC generator told the LLM to "retrieve credible sources independently." The citations it produced could not be audited.
- **For OKDS, the generator may only use the provided source pack.** This makes every `[S#]` claim checkable, keeps license tracking accurate, and matches Kyle's request for a documented dataset.

### 7.3 Workflow

```
1. Registry        pick a planned concept (ko_id, type, specialty, audience)
2. Source pack     collect 2–5 sources from the source inventory; save text + metadata
                   (sources/packs/SP-<ko_id>.md)
3. Generate        LLM + generator prompt (§7.4) → kos/<specialty>/<ko_id>_<slug>.md
                   (status: draft)
4. Validate        scripts/validate.py (§9) → fix or regenerate until it passes
5. AI review       LLM + reviewer prompt (§8) → reviews/<ko_id>_<date>.json
                   (status: ai_checked if it passes)
6. Human check     a team member checks each [S#] claim against the source (team_checked)
7. Clinician       an expert reviews the content when available (clinician_reviewed)
8. Publish         convert to JSON → load into the DB and graph → status: published
```

Run steps 1–8 on **3–5 KOs end to end** before generating more.

### 7.4 Generator prompt (copy into `prompts/ko_generator.md`, version `okds-gen-1.0`)

```text
ROLE
You write Knowledge Objects (KOs) for an orthopedic education resource.
A KO is a short, structured Markdown file about ONE concept, with YAML
front matter, plain-language content, a source marker on every claim,
and typed links to other KOs. Your output is a DRAFT for human review.

INPUTS (provided below)
- CONCEPT: ko_id, preferred_term, alternate_terms, ko_type, specialty, audience
- SOURCE PACK: sources S1..Sn, each with metadata and text
- REGISTRY: list of existing ko_id + preferred_term + ko_type (valid link targets)
- VOCAB: allowed predicates with subject→object types; enum values
- TEMPLATE: the required front matter fields and body headings for this ko_type

HARD RULES
1. Use ONLY information in the SOURCE PACK. Do not use outside knowledge
   for facts. Do not browse.
2. Every factual sentence ends with one or more markers like [S1].
   A marker may only cite a source that supports that sentence.
3. Never invent sources, URLs, dates, codes, statistics, or quotes.
   If a required value is unknown, write "<verify>" and add a line to
   review.open_issues.
4. If the SOURCE PACK has fewer than 2 relevant sources, or cannot
   support the required sections, output ONLY:
     SOURCE PACK NEEDED
     Missing: <what is missing>
     Suggested sources: <2–3 types of sources to add>
5. Links: use only predicates from VOCAB, with valid subject/object types,
   and target_ids from REGISTRY. If a needed concept is not in REGISTRY,
   put it in proposed_concepts instead. Never use RELATED_TO.
6. Medical safety: general education only. No personal advice, no dosing,
   no promises of outcomes. For Conditions include "When to seek care"
   using source content. Set safety.not_medical_advice: true.
7. Language: for patient/caregiver audiences write at grade 6–8 level,
   short sentences, define each medical term on first use.
   Paraphrase; never copy more than a short phrase from any source.
8. Set review.status: draft, version: "0.1.0", generated_by with your
   model name and prompt_version "okds-gen-1.0". Do not set any other
   review status.
9. Do not set ko_id, cluster, or specialty yourself; copy them from CONCEPT.

STEPS
1. Read CONCEPT and confirm ko_type. Use the TEMPLATE for that type.
2. Extract 5–10 key facts from the SOURCE PACK, each tied to [S#].
3. Write the summary (1–3 sentences, sourced).
4. Write the body using the required headings in order, including the
   type-specific "### " subsections.
5. Ask: "What other concepts must exist for this to make sense?" Add links
   (aim for 3–8) using VOCAB and REGISTRY; add proposed_concepts if needed.
6. Write 2–5 common misunderstandings (Myth/Fact, sourced).
7. Write 3–6 "Questions to Ask Your Doctor" (patient audiences) and
   3–6 Test Questions with short sourced answers.
8. Fill sources[] by copying metadata from the SOURCE PACK exactly.
9. Add 1–3 update_triggers.

SELF-CHECK BEFORE OUTPUT
[ ] Front matter has every required field; values match enums
[ ] Every [S#] used in the body exists in sources[]; every source is used
[ ] No unsourced factual sentence
[ ] All link targets are in REGISTRY or listed in proposed_concepts
[ ] No RELATED_TO; predicates match subject/object types
[ ] All required headings present for this ko_type
[ ] Safety fields set; no personal advice or dosing
[ ] Unknown values written as "<verify>" and listed in open_issues

OUTPUT
Return only the complete Markdown file (front matter + body). No commentary.
```

**IMPROVE mode** (reuse the PQC idea): add an input `MODE: IMPROVE` plus the existing KO and the reviewer findings. The model must keep `ko_id` and the structure, fix only the listed issues, increase `version` (patch or minor), and add a `change_log` entry.

### 7.5 Generator script outline (`scripts/generate.py`)

```python
# Pseudocode — model-agnostic. Run with: python3 -I scripts/generate.py KO-HAND-COND-001
import sys, yaml, pathlib
from llm_client import complete   # wrapper for whichever LLM API the team uses

ko_id    = sys.argv[1]
registry = load_csv("schema/registry.csv")
vocab    = yaml.safe_load(open("schema/vocab.yaml"))
concept  = registry[ko_id]
pack     = open(f"sources/packs/SP-{ko_id}.md").read()
template = open(f"schema/templates/{concept['ko_type']}.md").read()
prompt   = open("prompts/ko_generator.md").read()

user_msg = render(prompt, CONCEPT=concept, SOURCE_PACK=pack,
                  REGISTRY=registry_summary(registry), VOCAB=vocab, TEMPLATE=template)
draft = complete(user_msg, temperature=0.2)

if draft.strip().startswith("SOURCE PACK NEEDED"):
    log_needed(ko_id, draft); sys.exit(2)

out = pathlib.Path(f"kos/{concept['specialty'].lower()}/{ko_id}_{slug(concept['preferred_term'])}.md")
out.write_text(draft)
run("python3 -I scripts/validate.py " + str(out))   # fail fast
```

**Notes:**
- Keep `temperature` low.
- Store the prompt version in every KO.
- If the API supports citations or document grounding (for example, citations on provided documents), pass the source pack as documents, so the API can check that the `[S#]` markers match.

### 7.6 Source packs (`sources/packs/SP-<ko_id>.md`)

```markdown
# Source pack SP-KO-HAND-COND-001 (Carpal Tunnel Syndrome)
## S1
id: S1
title: Carpal Tunnel Syndrome
publisher: National Library of Medicine (MedlinePlus)
url: https://medlineplus.gov/carpaltunnelsyndrome.html
source_type: government_health_page
audience: patient
publication_date: <from page>
retrieved_date: 2026-10-24
permitted_use: link_and_paraphrase
text: |
  <cleaned page text or relevant excerpt>
## S2
...
```

**Good sources for OKDS:**
- MedlinePlus (NLM; there is an API)
- NIH institute pages (NINDS, NIAMS)
- AAOS OrthoInfo (link and paraphrase only) and AAOS clinical practice guidelines
- PubMed abstracts and the PMC Open Access Subset (check each article's license)
- openFDA for devices
- ClinicalTrials.gov for trials

Record each source once in `sources/source_inventory.csv` (Kyle's dataset fields) and reuse its `id` across packs *(decide: global source IDs vs per-KO S1..Sn; per-KO is simpler for the LLM)*.

---

## 8. The KO Reviewer

### 8.1 What it is

An LLM prompt that scores a KO against a rubric and lists fixes. **It is not a substitute for human review.** It catches format, sourcing, and clarity problems before a person spends time on the KO. The PQC version was a custom ChatGPT GPT. Here, use a versioned prompt (`prompts/ko_reviewer.md`, `okds-rev-1.0`) so results can be reproduced.

### 8.2 Rubric (score each item 1–5)

| # | Criterion | What to check |
|---|---|---|
| 1 | Format compliance | Required fields and headings, enums, ID copied correctly |
| 2 | Claim support | **Each `[S#]` claim is actually supported by that source's text** (the reviewer gets the source pack) |
| 3 | Source quality & metadata | At least 2 credible sources, complete metadata, `permitted_use` respected, dates present |
| 4 | Medical safety & scope | No personal advice or dosing, "When to seek care" present for conditions, disclaimer set |
| 5 | Audience fit & readability | Reading level matches the audience, terms defined, short sentences |
| 6 | Terminology consistency | The preferred term is used consistently and matches the registry |
| 7 | Graph quality | Allowed predicates, valid types, targets exist, 3–8 meaningful links, no `RELATED_TO` |
| 8 | Completeness for type | All type-specific subsections are meaningful, not filler |
| 9 | Currency | Source dates are recent enough, and update triggers are present |
| 10 | Duplication | No large overlap with existing KOs, based on the registry and the summaries given |

**Pass rule** *(decide)*: every criterion ≥ 3, with criteria 2 and 4 at **5**. A failing KO goes back to the generator in IMPROVE mode with the findings.

### 8.3 Review statuses (who can set what)

```
draft ──(AI review passes)──► ai_checked ──(person checks every [S#] against source)──► team_checked
      ──(clinician reviews)──► clinician_reviewed ──(approved for site)──► published
Any status ──► retired (replaced or withdrawn; keep file, never reuse ID)
```

- LLMs can set only `draft` and `ai_checked`.
- If no clinician is available, publish at `team_checked` and label it on the site as "Checked against sources by the project team, not clinically reviewed."

### 8.4 Reviewer prompt (copy into `prompts/ko_reviewer.md`)

```text
ROLE
You review orthopedic Knowledge Objects (KOs) for an education resource.
You check format, sourcing, safety, clarity, and graph links. You do not
add new facts.

INPUTS
- KO: the full Markdown file
- SOURCE PACK: the sources the KO was generated from
- REGISTRY, VOCAB, TEMPLATE (same as the generator)

TASK
1. Score each rubric criterion 1–5 with a one-line reason:
   format, claim_support, source_quality, safety, readability,
   terminology, graph_quality, completeness, currency, duplication.
2. For claim_support, check EVERY sentence with a [S#] marker against
   that source's text. List each unsupported or overstated claim.
3. List unsourced factual sentences.
4. List safety problems (personal advice, dosing, missing "When to seek care").
5. List graph problems (bad predicate, wrong types, unknown target, RELATED_TO).
6. Give a prioritized fix list. Do not rewrite the KO.

OUTPUT (JSON only)
{
  "ko_id": "...", "version": "...", "reviewer_prompt": "okds-rev-1.0",
  "scores": {"format":n, "claim_support":n, "source_quality":n, "safety":n,
             "readability":n, "terminology":n, "graph_quality":n,
             "completeness":n, "currency":n, "duplication":n},
  "unsupported_claims": [{"text":"...", "marker":"S2", "problem":"..."}],
  "unsourced_sentences": ["..."],
  "safety_issues": ["..."],
  "graph_issues": ["..."],
  "fixes": ["1. ...", "2. ..."],
  "pass": true|false
}
```

---

## 9. Validation (automatic checks before review and before loading)

### 9.1 What `scripts/validate.py` must check

1. The YAML front matter parses, and `schema_version` = `okds-ko-1.0`.
2. The front matter passes the JSON Schema (§9.2): required fields, types, and enums.
3. `ko_id` exists in the registry, and `preferred_term`, `ko_type`, and `specialty` match it.
4. `ko_id` is unique across all KO files.
5. `cluster` equals the rule-based value for `ko_type` (§4.5).
6. Each predicate is in `vocab.yaml`, the subject and object types are allowed, and each `target_id` exists in the registry.
7. `RELATED_TO` or `ASSOCIATED_WITH` doesn't appear anywhere.
8. Every `[S#]` in the body exists in `sources`, and every source is used at least once.
9. There are at least 2 sources, and each has a `url`, `publisher`, `retrieved_date`, and `permitted_use`.
10. No source has `permitted_use: restricted`.
11. All required body headings for the `ko_type` are present and in order.
12. Dates use the ISO format, and `last_updated` ≥ `created`.
13. `review.status` is allowed, and LLM-generated files don't claim human statuses.
14. `"<verify>"` values are reported as warnings, which block `published` status.

The output is a pass/fail per file plus a summary table. Use it in CI or as a pre-commit check if the team uses Git.

### 9.2 JSON Schema starter (`schema/ko.schema.json`, front matter only)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "OKDS Knowledge Object front matter",
  "type": "object",
  "required": ["schema_version","ko_id","title","preferred_term","ko_type","specialty",
               "cluster","audience","reading_level","difficulty","summary",
               "relationships","sources","review","safety","version","created",
               "last_updated","update_triggers","license","change_log"],
  "properties": {
    "schema_version": {"const": "okds-ko-1.0"},
    "ko_id": {"type": "string", "pattern": "^KO-(SPORT|SPINE|TRAUMA|HAND|JOINT|FOOT|GEN)-(COND|ANAT|DX|TRT|PROC|DEV|REHAB|OUT|CONC)-[0-9]{3}$"},
    "ko_type": {"enum": ["Condition","AnatomicalStructure","DiagnosticTest","Treatment",
                         "Procedure","Device","RehabProtocol","OutcomeMeasure","Concept"]},
    "specialty": {"enum": ["SPORT","SPINE","TRAUMA","HAND","JOINT","FOOT","GEN"]},
    "cluster": {"type": "integer", "minimum": 1, "maximum": 7},
    "audience": {"type": "array", "minItems": 1,
                 "items": {"enum": ["patient","caregiver","student","clinician","researcher","industry"]}},
    "difficulty": {"enum": ["beginner","intermediate","advanced"]},
    "summary": {"type": "string", "minLength": 40},
    "relationships": {"type": "array", "items": {
        "type": "object", "required": ["predicate","target_id","target_label","source_ids"],
        "properties": {"predicate": {"type": "string", "pattern": "^[A-Z_]+$"},
                       "target_id": {"type": "string"},
                       "source_ids": {"type": "array", "items": {"type": "string"}}}}},
    "sources": {"type": "array", "minItems": 2, "items": {
        "type": "object",
        "required": ["id","title","publisher","url","source_type","retrieved_date","permitted_use"],
        "properties": {"id": {"type": "string", "pattern": "^S[0-9]+$"},
                       "permitted_use": {"type": "string"}}}},
    "review": {"type": "object", "required": ["status","author","generated_by"],
               "properties": {"status": {"enum": ["draft","ai_checked","team_checked",
                                                   "clinician_reviewed","published","retired"]}}},
    "safety": {"type": "object", "required": ["not_medical_advice"],
               "properties": {"not_medical_advice": {"const": true}}},
    "version": {"type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"}
  }
}
```

---

## 10. Storing and loading KOs

### 10.1 Markdown → JSON (`scripts/to_json.py`)
- Parse the front matter. Split the body by `##` and `###` headings into `sections.<snake_case>`. Keep `raw_markdown`. Add `source_file` and `built_at`.
- Write the result to `build/json/<ko_id>.json`. **Never hand-edit the JSON.**

### 10.2 Document store
- **MongoDB:** database `okds`, collection `knowledge_objects`.
  - Create a unique index on `ko_id`, plus indexes on `ko_type`, `specialty`, `audience`, and `review.status`.
  - Add a text index on `title`, `alternate_terms`, `summary`, and `tags`.
  - Load with upsert on `ko_id`.
- **Postgres alternative** (the OKDS technical guide suggests starting with Postgres + pgvector, which is still undecided):
  - Tables: `kos(ko_id PK, ... jsonb)`, `sources`, `ko_sources(ko_id, source_id)`, `relationships(subject_id, predicate, object_id, source_ids)`.
  - The same KO format works for both.

### 10.3 Graph (Neo4j)
Build the graph **only from validated KO `relationships`** and from API entity records. Don't use automatic LLM entity extraction.

```cypher
// one-time constraints
CREATE CONSTRAINT ko_id IF NOT EXISTS FOR (k:KO) REQUIRE k.ko_id IS UNIQUE;
CREATE CONSTRAINT src_url IF NOT EXISTS FOR (s:Source) REQUIRE s.url IS UNIQUE;

// node (label from ko_type is added in code, e.g. :Condition)
MERGE (k:KO {ko_id: $ko_id})
SET k.title = $title, k.ko_type = $ko_type, k.specialty = $specialty,
    k.audience = $audience, k.summary = $summary, k.version = $version,
    k.review_status = $review_status;

// edge (predicate already validated against vocab.yaml, so it is safe to insert)
MATCH (a:KO {ko_id: $subject}), (b:KO {ko_id: $target})
MERGE (a)-[r:DIAGNOSED_BY]->(b)
SET r.source_ids = $source_ids;
```

> Cypher comments use `//`, not `#`. A `#` inside a query string broke the PQC loader.

**Demo queries to prove the graph works:**
- "What tests diagnose carpal tunnel syndrome?" → `MATCH (c:KO {ko_id:'KO-HAND-COND-001'})-[:DIAGNOSED_BY]->(t) RETURN t.title`
- "Which treatments are alternatives to carpal tunnel release?"
- "What should I read before Carpal Tunnel Release?" (follow `PREREQUISITE_FOR`)
- "Which Indiana companies make devices used in this procedure?" (KO → `USES_DEVICE` → Device → `MANUFACTURED_BY` → Organization → `LOCATED_IN`)

### 10.4 Using KOs in OrthoBot (RAG)
- **Retrieve:** search KO `summary` plus sections (keyword, semantic, or hybrid; that comparison is Kyle's step 7). Then add the KO's graph neighbors.
- **Answer:** use only the retrieved KO text. Cite the **KO ID plus the original `[S#]` source**.
- **Refuse:** say "I don't know" when the retrieved KOs don't cover the question.
- **Evaluate:** the `## Test Questions` in each KO are the first draft of the 40–60 question evaluation set.

---

## 11. Quick start for the OKDS agent

1. **Confirm decisions** with the user: primary audience, first specialty, 3–4 conditions, Neo4j vs Postgres, and whether a clinician reviewer exists. Then write them down in the project notes.
2. **Create the folders:**
   ```
   schema/   vocab.yaml, ko.schema.json, registry.csv, templates/<ko_type>.md
   prompts/  ko_generator.md (okds-gen-1.0), ko_reviewer.md (okds-rev-1.0)
   sources/  source_inventory.csv, packs/SP-<ko_id>.md
   kos/      <specialty>/<ko_id>_<slug>.md      ← source of truth
   reviews/  <ko_id>_<date>.json
   scripts/  generate.py, validate.py, review.py, to_json.py, load_db.py, load_graph.py
   build/    json/ (generated)
   releases/ CHANGELOG.md, dataset version tags (v0.1, v0.2...)
   ```
3. **Write `vocab.yaml`** from §4 (types, predicates with subject and object types, enums, the cluster rule).
4. **Build the registry:** about 15–25 concepts for the first specialty, covering condition, anatomy, tests, treatments, procedure, and rehab, with IDs assigned by a script.
5. **Build the source inventory and 3–5 source packs.**
6. **Run the full loop on 3–5 KOs:** generate → validate → AI review → human check → JSON → load → demo queries.
7. Fix the prompts, schema, and scripts based on what broke. **Only then scale up.**
8. **Release dataset v0.1** with a change log. Update the project notes.

**Definition of done for one KO:**
- validator passes
- AI review passes
- every `[S#]` was checked by a person
- status is `team_checked` or higher
- it is loaded in both stores
- it appears correctly on the site and in at least one demo query

---

## Appendix A. Where the PQC originals are (optional reading)

The PQC project's original files are not part of this repo. The one this design builds on, the
PQC team's KO Generator Prompt (3-13-26), is copied here: [`pqc-ko-generator-prompt-3-13-26.md`](pqc-ko-generator-prompt-3-13-26.md).

## Appendix B. Mapping from the PQC KO format to OKDS v1.0

| PQC field or section | OKDS v1.0 equivalent | Change |
|---|---|---|
| `ko_id: KO-C1-TR-001` | `ko_id: KO-HAND-COND-001` | Specialty + type, not cluster, so the ID survives regrouping |
| `cluster`, `category` (free text) | `ko_type` (enum) + `cluster` (rule) | Enums only |
| `dependencies` (free text) | `relationships[]` with `target_id` | Linked by ID |
| `knowledge_graph.depends_on/related_to/...` | `relationships[].predicate` (closed list) | No `related_to` |
| `validation_status` (LLM-written) | `review.status` (human-controlled) | Statuses gated to people |
| Evidence Snapshot (claim → source) | `## Key Facts` + inline `[S#]` everywhere | Claim-level provenance |
| References (free citations) | `sources[]` with Kyle's dataset fields | Adds audience, retrieved date, permitted use |
| Performance test questions | `## Test Questions` (with sourced answers) | Feeds the evaluation set |
| Update Triggers (some KOs) | `update_triggers` (required) | Required |
| Kyle's "LLM guardrail snippet" | `summary` | Required and sourced |
| — | `safety`, `audience`, `reading_level`, `codes`, `proposed_concepts` | New for medical content |
