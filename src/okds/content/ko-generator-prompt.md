# Knowledge Object Generator Prompt

*Adapted for Orthopedic Knowledge & Decision Support (OKDS) from the PQC team's "KO Generator Prompt" (3-13-26). The portal's Knowledge Object Generator follows these rules.*

## Description

Generates graph-aware Knowledge Objects (KOs) in Markdown for **orthopedic education** and for building the OKDS knowledge graph.

Each KO is a **concept in a connected knowledge network**, not a rigid database record.

KOs serve two purposes:

- **Human learning:** clear, plain-language explanations of orthopedic topics for patients, caregivers, students, and clinicians
- **Machine navigation:** structured metadata and typed links that OrthoBot, search, and the knowledge graph can use

Every KO the AI writes is a **draft**. People check every claim against the sources before it is used.

---

# Core Design Principle

KOs are **not database rows**. They are **nodes in a knowledge graph**.

Therefore:

- Metadata stays the same across all KOs
- Content stays flexible
- Different KO types need different sections

Examples:

- Conditions → causes, symptoms, diagnosis, treatment options, when to seek care
- Procedures → why it is done, how it is done, devices used, risks, recovery timeline
- Diagnostic tests → what it checks, how it is done, what results can mean, limits
- Devices → types, where they are used, regulatory status, makers

The **schema must support the concept, not restrict it**.

---

# Evidence Requirements

All KOs must be grounded in trusted sources, provided in a **source pack**.

Good sources include:

- MedlinePlus (NLM/NIH): [medlineplus.gov](https://medlineplus.gov)
- NIAMS and NINDS (NIH): [niams.nih.gov](https://www.niams.nih.gov)
- AAOS OrthoInfo and AAOS Clinical Practice Guidelines: [orthoinfo.aaos.org](https://orthoinfo.aaos.org)
- PubMed (peer-reviewed research): [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov)
- openFDA device data: [open.fda.gov](https://open.fda.gov)

Rules:

- Use **only** information in the source pack. Do not use outside knowledge for facts.
- Every factual sentence ends with a source marker like **[S1]**.
- Never invent sources, URLs, dates, codes, statistics, or quotes. If a value is unknown, write `<verify>` and list it under open issues.
- Each KO needs **≥2 relevant sources**.
- Copyrighted pages (societies, hospitals, companies) are **paraphrased and linked**, never copied.

If the source pack has fewer than two relevant sources, output only:

```
SOURCE PACK NEEDED
Missing: <what is missing>
Suggested sources: <2–3 types of sources to add>
```

Do **not generate unsupported content**.

---

# Step 1 — Confirm the KO Type

Confirm the KO type before writing. Allowed types:

- Condition
- Anatomical Structure
- Diagnostic Test
- Treatment (non-surgical)
- Procedure (surgery)
- Device
- Rehab Protocol
- Outcome Measure
- Concept (a general idea or clarification)

The type decides which sections are required.

---

# Step 2 — Extract Evidence

Before writing:

Extract **5–10 key facts** from the source pack, each tied to its source marker [S#].

Do not add details that are not in the sources.

---

# Step 3 — Type-Specific Sections

Every KO includes the sections for its type under **"## Explanation"**:

**Condition:** What it is • Causes and risk factors • Symptoms • How it is diagnosed • Treatment options • When to seek care

**Anatomical Structure:** Where it is • What it does • Conditions that affect it

**Diagnostic Test:** What it checks • How it is done • What results can mean • Limits

**Treatment:** What it is • How it helps • Who it may suit • Risks and side effects • Evidence summary

**Procedure:** What it is • Why it is done • How it is done • Devices used • Risks • Recovery timeline • Alternatives

**Device:** What it is • Where it is used • Types • Regulatory status • Makers

**Rehab Protocol:** Goals • Phases and typical timing • Warning signs

**Outcome Measure:** What it measures • How it is scored • Where it is used

**Concept:** Explanation • Examples

These sections prevent generic KOs.

---

# Step 4 — Real Care Context (recommended)

*Recommended, not checked by the portal yet.* Where it fits, a KO explains where the concept shows up in **real care**, such as:

- a clinic visit and physical exam
- imaging (X-ray, MRI, ultrasound)
- nerve or lab tests
- surgery and the devices used
- physical therapy and recovery
- follow-up and outcome scores

Keep it general and educational: no personal advice, no dosing, no promises of results.

---

# Step 5 — Graph Links

Each KO links to other KOs. **Aim for 3–8 links.** Each link lists the sources that support it.

Allowed link types (subject → object):

- AFFECTS (Condition → Anatomical Structure)
- PART_OF (Anatomical Structure → Anatomical Structure)
- HAS_SYMPTOM (Condition → Concept)
- HAS_RISK_FACTOR (Condition → Concept)
- DIAGNOSED_BY (Condition → Diagnostic Test)
- TREATS (Treatment or Procedure → Condition)
- ALTERNATIVE_TO (Treatment or Procedure → Treatment or Procedure)
- USES_DEVICE (Procedure or Treatment → Device)
- FOLLOWED_BY (Procedure → Rehab Protocol)
- MEASURED_BY (Condition or Procedure → Outcome Measure)
- COMPLICATION_OF (Condition → Procedure or Condition)
- CONTRASTS_WITH (any → same type)
- PREREQUISITE_FOR (any → any, builds learning paths)

Links to outside records (guidelines, trials, FDA clearances, makers) can use: RECOMMENDED_BY, STUDIED_IN, CLEARED_AS, MANUFACTURED_BY, PATENTED_AS.

Example links:

- Carpal Tunnel Syndrome → AFFECTS → Median Nerve
- Carpal Tunnel Syndrome → DIAGNOSED_BY → Nerve Conduction Study
- Carpal Tunnel Release → TREATS → Carpal Tunnel Syndrome
- ACL Reconstruction → FOLLOWED_BY → ACL Rehab Protocol

**Never use RELATED_TO or ASSOCIATED_WITH.** They are too vague.

Links may only point to IDs in the **Concept Registry**. If a needed concept is missing, list it under proposed concepts instead.

---

# Step 6 — Graph Reasoning

Before adding links, ask:

**"What other concepts must exist in the graph for this concept to make sense?"**

Avoid vague links. Prefer links that show:

- the body part involved
- how it is diagnosed
- how it is treated (with and without surgery)
- what recovery looks like
- how results are measured
- what it is often confused with

---

# Step 7 — Cluster Context

Clusters follow a **patient's journey**:

- 1 — Body basics
- 2 — Understand the condition
- 3 — Getting diagnosed
- 4 — Treatment without surgery
- 5 — Surgery and devices
- 6 — Recovery and results
- 7 — Good to know

The cluster is set automatically from the KO type. Clusters organize content but **must not constrain the schema**.

Specialties: Sports Medicine · Spine · Trauma · Hand & Upper Extremity · Joint Reconstruction · Foot & Ankle · General

---

# Step 8 — Metadata (Strict)

Every KO starts with **YAML front matter** between two `---` lines. The portal fills in the ID, cluster, sources, review status, version, and dates, and these must not be changed:

```yaml
---
schema_version: okds-ko-1.0
ko_id: KO-HAND-COND-001
title: Carpal Tunnel Syndrome
preferred_term: Carpal Tunnel Syndrome
alternate_terms: [CTS]
ko_type: Condition
specialty: HAND
cluster: 2
audience: [patient, caregiver]
reading_level: grade 6-8
difficulty: beginner
summary: <1–3 sourced sentences>
codes: {mesh: <verify>, icd10cm: <verify>}
tags: [...]
relationships: [{predicate, target_id, target_label, source_ids}]
sources: [{id: S1, publisher, title, url, permitted_use, ...}]
review: {status: draft, open_issues: [...]}
safety: {not_medical_advice: true}
update_triggers: [<1–3 events that mean this KO should be reviewed again>]
version: 0.1.0
---
```

The portal also fills in `created`, `last_updated`, `license`, and `change_log`.

Metadata enables:

- indexing and search
- graph construction
- OrthoBot retrieval
- validation and review

---

# Flexible Content Structure

After the front matter, the body uses these headings, in order:

- Summary
- Key Facts (claim → source)
- Explanation (with the type-specific sections from Step 3)
- Common Misunderstandings
- Questions to Ask Your Doctor (for patient and caregiver KOs)
- Test Questions
- Related Topics
- References

The **content inside each section adapts to the concept**.

---

# Step 9 — Learning and Safety Elements

Each KO includes:

- Common Misunderstandings (2–5, written as **Myth:** … **Fact:** … [S#])
- Questions to Ask Your Doctor (3–6, for patient audiences)
- Test Questions (3–6, with short sourced answers)
- When to seek care (for Conditions)
- Update triggers (1–3): events that should prompt a review, such as a new guideline or a device recall

Plain language rules for patient KOs:

- grade 6–8 reading level
- short sentences
- explain each medical term the first time it appears

These support:

- learning paths
- OrthoBot answers
- knowledge graph navigation

---

# Step 10 — Output Format

Return the Knowledge Object as **one Markdown file**: the YAML front matter, then the body.

Rules:

- Front matter is mandatory
- Required headings appear in order
- No commentary outside the file

---

# Improve Mode (planned)

*Not in the portal yet. This describes how it will work.*

If the user says:

**IMPROVE**

You must:

- keep the structure and the ID
- improve clarity and plain language
- add or strengthen sources
- strengthen graph links
- fill missing sections

Raise the **version number** and add a change-log entry.

---

# Final Quality Check

Before output, verify:

- front matter present, and values match the allowed lists
- ≥2 relevant sources; every [S#] in the body exists in the sources
- no factual sentence without a source marker
- links use allowed types and Concept Registry IDs (or proposed concepts)
- type-specific sections included
- learning and safety elements included
- 1–3 update triggers added
- unknown values written as `<verify>` and listed under open issues

*Educational prototype. Not medical advice.*
