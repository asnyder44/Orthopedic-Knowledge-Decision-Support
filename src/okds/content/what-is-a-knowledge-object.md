# What is a Knowledge Object?

### Knowledge Objects for Orthopedic Knowledge & Decision Support (OKDS)

*Adapted for orthopedics from "Knowledge Objects in the Age of LLMs: A Framework for Navigating Collective Intelligence and Knowledge Graphs."*

#### Summary

Orthopedic knowledge grows faster than anyone can read it: new studies, new guidelines, new devices, and new patient-education pages appear every year. We use **Knowledge Objects (KOs)** to keep it manageable. A KO is a small, structured, sourced note about **one** orthopedic topic. People can read it, machines can use it, and it links to other KOs. Together, KOs form a **knowledge graph** that powers OrthoBot (our AI assistant), search, and learning paths. Every KO is drafted with help from AI and checked by people before anyone relies on it.

#### 1. Why we need structure

Patients, students, and clinicians all face the same problem: the information exists, but it is scattered. A single topic such as carpal tunnel syndrome shows up in patient pages, clinical guidelines, research papers, device records, and rehab plans, each written for a different reader.

Nobody can keep all of it in their head, so good knowledge gets lost, repeated, or used out of context. We need a way to **break orthopedic knowledge into reusable pieces**, keep the source of every fact, and connect the pieces so people and software can find their way.

That piece is the **Knowledge Object**.

#### 2. What a Knowledge Object is

A **Knowledge Object** is a self-contained unit of knowledge about one concept. It is **easy for people to read, easy for machines to navigate, and reusable in many places**.

Every KO has four parts:

- **Core content:** a plain-language explanation of one concept (for example, what it is, its symptoms, how it is diagnosed, and when to seek care).
- **Metadata and tags:** a stable ID (like `KO-HAND-COND-001`), the KO type, specialty, audience, reading level, and version.
- **Provenance:** the sources behind every fact (each claim carries a marker like [S1]), plus who wrote it, who checked it, and when.
- **Links:** typed connections to other KOs, such as *Carpal Tunnel Syndrome → DIAGNOSED_BY → Nerve Conduction Study*.

In OKDS, a KO can be one of these types:

| KO type | Example |
|---|---|
| Condition | Carpal tunnel syndrome, ACL tear, knee osteoarthritis |
| Anatomical structure | Median nerve, meniscus, rotator cuff |
| Diagnostic test | Nerve conduction study, Lachman test, knee MRI |
| Treatment (non-surgical) | Wrist splinting, physical therapy, steroid injection |
| Procedure (surgery) | Carpal tunnel release, total knee arthroplasty |
| Device | Knee implant, wrist brace |
| Rehab protocol | Recovery plan after ACL reconstruction |
| Outcome measure | A questionnaire that scores knee function |
| Concept | A general idea, such as "evidence levels" |

#### 3. How KOs work with AI and knowledge graphs

AI chatbots are good at writing fluent answers, but on their own they can be wrong, out of date, and hard to check. KOs give the AI a **trusted layer to stand on**:

- **OrthoBot uses RAG (Retrieval-Augmented Generation):** it looks up the right KOs first, then answers only from them, and shows the sources.
- **The knowledge graph is built from KO links:** conditions connect to the body parts they affect, the tests that diagnose them, the treatments and surgeries that treat them, and the rehab that follows.
- **Learning paths follow the links:** for example, Median Nerve → Carpal Tunnel Syndrome → Nerve Conduction Study → Carpal Tunnel Release → Recovery.

Because every answer points back to a KO, and every KO points back to its sources, the system stays **transparent, checkable, and trustworthy**.

#### 4. AI drafts, people decide

Writing and checking KOs by hand takes time. OKDS shares the work between AI and people:

**4.1 Shared drafting and review**

- The KO Generator uses AI to write a **first draft** from 2 or more trusted sources.
- An automatic validator checks the format, the source markers, and the links.
- **Only people** can mark a KO as team-checked, clinician-reviewed, or published. The steps are: draft → AI checked → team checked → clinician reviewed → published.

**4.2 Tags that fit the reader**

- Tags and audience fields make the right KO easy to find, whether it is for a patient, a caregiver, a student, or a clinician.
- Reading level matters: patient KOs are written at about a grade 6–8 level, with each medical term explained.

**4.3 Navigating by connection**

- People move through **connected topics**, not a static list. For example, they can go from a condition to its tests, its treatment choices, and what recovery looks like.
- Over time, the most useful paths show how patients and clinicians actually think about a problem.

#### 5. How the OKDS system is built

**5.1 Collecting knowledge**

- We start from a catalog of trusted sources: government health pages (MedlinePlus, NIH), professional societies (AAOS), research (PubMed), trial registries, and device records (FDA).
- Copyrighted pages are linked and paraphrased, never copied. Patient-level data is never used.

**5.2 Versions and history**

- Each KO has a version number and a change log, so edits can be tracked and undone.
- A citation like `KO-HAND-COND-001 v1.2` always means one exact version.

**5.3 Answering questions**

- **RAG:** OrthoBot finds the most relevant KOs for each question and answers only from them.
- If no KO covers a question, OrthoBot says "I don't know" instead of guessing.

**5.4 Ways to explore**

- **Graph view:** see how one topic connects to others.
- **Filters by reader and specialty:** for example, "patient" + "Hand & Upper Extremity".
- **Search** across titles, alternate names, and tags.

#### 6. Open questions

**6.1 Who writes and checks KOs?**

- Clinician review takes time. We need a clear, fair review process and credit for the reviewers.

**6.2 How strict should the format be?**

- Too strict, and KOs can't fit different topics (a surgery needs a recovery timeline; a condition needs symptoms). Too loose, and the system can't use them.
- OKDS uses fixed metadata, plus required sections that change with the KO type.

**6.3 Safety and fairness**

- KOs are for education, not personal medical advice. They tell readers when to seek care, and they avoid dosing or promises.
- We must watch for bias in sources and for AI mistakes, and keep humans in charge of what gets published.

#### 7. Conclusion

The hard part is no longer *finding* orthopedic information. It is understanding it, trusting it, and connecting it. **Knowledge Objects turn scattered information into small, sourced, linked pieces** that people and AI can use together, safely and openly. They are the foundation of everything OKDS builds: the library, the knowledge graph, and OrthoBot.

*Educational prototype. Not medical advice.*
