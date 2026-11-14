---
schema_version: okds-ko-1.0
ko_id: KO-SPINE-COND-002
title: Lumbar Disc Herniation
preferred_term: Lumbar Disc Herniation
alternate_terms:
- herniated disc
- slipped disc
- sciatica from a disc
- herniated disk
- ruptured disc
- lumbar disc herniation (LDH)
- herniated nucleus pulposus
ko_type: Condition
specialty: SPINE
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: A lumbar disc herniation is when one of the soft disks between the bones of the lower back ruptures,
  letting its jelly-like center leak out and irritate nearby nerves [S1][S3]. It can cause back pain or
  sciatica, which is pain, numbness, tingling, or weakness that runs from the lower back down one leg
  [S1][S2]. With treatment, most people recover [S1].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- lower back
- spine
- disc
- sciatica
- leg pain
- nerve irritation
- back pain
relationships:
- predicate: CONTRASTS_WITH
  target_id: KO-SPINE-COND-001
  target_label: Lumbar Spinal Stenosis
  source_ids:
  - S2
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-SPINE-TRT-001
  target_label: Physical Therapy for Low Back Pain
  source_ids:
  - S1
  - S2
proposed_concepts:
- term: Intervertebral disc
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S1 and S3 describe the cushion-like disks between the vertebrae that herniate; no spine anatomy
    KO is in the registry.
- term: Sciatic nerve
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S2 describes the sciatic nerve and the leg symptoms when it is irritated, for example by a ruptured
    disk.
- term: Sciatica
  suggested_type: Concept
  predicate: HAS_SYMPTOM
  reason: S1 and S2 name sciatica as a main symptom of a herniated disk; needs a Concept KO.
- term: Spinal MRI
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S4 says MRI is the imaging test of choice for suspected lumbar disc herniation.
- term: Lumbar discectomy
  suggested_type: Procedure
  predicate: PREREQUISITE_FOR
  reason: S1, S2, and S4 say surgery is sometimes used and that disc herniation is the most common spine
    problem needing surgery; the pack does not describe the operation, so a source on discectomy is needed.
sources:
- id: S1
  title: Herniated Disk
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/herniateddisk.html
  source_type: government_health_page
  audience: patient
  publication_date: '2025-12-17'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:herniateddisk). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
- id: S2
  title: Sciatica
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/sciatica.html
  source_type: government_health_page
  audience: patient
  publication_date: '2024-09-16'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:sciatica). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
- id: S3
  title: Back Pain
  publisher: National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH)
  url: https://www.niams.nih.gov/health-topics/back-pain
  source_type: government_health_page
  audience: patient
  publication_date: '2023-02-01'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (niams:back-pain). Licence: Public domain (U.S. federal government
    work, NIH/NIAMS); credit NIAMS'
- id: S4
  title: Diagnostic accuracy of diagnostic imaging for lumbar disc herniation in adults with low back
    pain or sciatica is unknown; a systematic review
  publisher: Chiropractic & Manual Therapies
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6102824/
  source_type: journal_article
  audience: clinician
  publication_date: '2018'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC6102824). Licence: CC BY'
- id: S5
  title: Characteristics and mechanisms of resorption in lumbar disc herniation
  publisher: Arthritis research & therapy
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9396855/
  source_type: journal_article
  audience: clinician
  publication_date: '2022'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: review. Text kept: abstract only.'
review:
  status: draft
  author: KO Collector + Claude (Claude Code session)
  generated_by:
    model: claude-opus-5-5 (Claude Code session)
    prompt_version: okds-gen-1.1
  ai_check: null
  team_checker: null
  clinician_reviewer: null
  clinician_role: null
  review_date: null
  open_issues:
  - No source in this pack describes the surgery used for disc herniation (for example discectomy), so
    the KO only says surgery is sometimes used. Add a source and a Procedure KO.
  - No source gives risk factors specific to disc herniation beyond disk aging (S1); the risk factors
    listed are for back pain in general (S3). Clinician check.
  - The When to seek care section uses the NIAMS back pain list (S3), which is about back pain in general,
    not disc herniation alone. Clinician check.
  - S4 is mostly based on studies done before 1995, so its imaging accuracy figures may not apply to modern
    MRI (the authors say this themselves).
  - S5 is an abstract only (CC BY review); it says spontaneous shrinking happens but not how often.
  - MeSH ID and ICD-10-CM code are not stated in any source and remain <verify>.
  - Only 2 registry links are supported; no spine anatomy, imaging, or discectomy KOs exist yet (see proposed_concepts).
  - Plain-language definitions (e.g., macrophages as immune cells, ionizing radiation) were written by
    the drafter; check they match the sources.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus or NIAMS shows a new 'last updated' or 'last reviewed' date on a cited herniated disk, sciatica,
  or back pain page.
- A new systematic review on imaging accuracy or on non-surgical versus surgical care for lumbar disc
  herniation is published.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
A lumbar disc herniation is when one of the soft disks between the bones of the lower back ruptures, letting its jelly-like center leak out and irritate nearby nerves [S1][S3]. It can cause back pain or sciatica, which is pain, numbness, tingling, or weakness that runs from the lower back down the leg [S1][S2]. Doctors diagnose it with a physical exam and sometimes imaging tests [S1]. With treatment, most people recover [S1].

## Key Facts (claim → source)
- Disks are soft, cushion-like pads with a jelly-like center that sit between the bones of the spine [S1][S3].
- A herniated disk ruptures and its center leaks out, which can irritate nearby nerves [S1].
- Herniated disks often happen in the lower (lumbar) back, but they can also happen in the neck [S3].
- About 5 to 15 out of 100 people with low back pain have a lumbar disc herniation [S4].
- A herniated disk can cause sciatica: pain, numbness, tingling, or weakness down one leg [S1][S2].
- Treatment includes rest, pain and anti-inflammatory medicines, physical therapy, and sometimes surgery [S1].
- A herniated disc can shrink and be absorbed by the body on its own, without surgery [S5].

## Explanation
### What it is
Your spine is made of 26 bones called vertebrae [S1]. Between them are soft disks filled with a jelly-like substance that cushion the bones and keep them in place [S1]. A herniated disk is a disk that ruptures, so the jelly-like center leaks out and irritates nearby nerves [S1]. When this squeezes a nerve root (a nerve where it branches off the spinal cord), doctors call it a lumbar disc herniation if it is in the lower back [S3][S4]. It is the most common spine problem that leads to surgery [S4].

### Causes and risk factors
As you age, the disks break down and lose their ability to cushion, which can lead to pain if the back is stressed [S1]. NIAMS describes a herniated or ruptured disc as an event in which a disc presses on and irritates nearby nerves [S3]. For back pain in general, NIAMS lists these risk factors [S3]:
- Low fitness, such as weak back and stomach muscles, or exercising too hard after being inactive.
- Weight gain that puts stress on the back.
- Jobs with heavy lifting, pushing, pulling, or twisting.
- Getting older, especially after age 45.
- Genes, for some disorders that cause back pain.

### Symptoms
A herniated disk can cause back pain or sciatica [S1]. Sciatica is a symptom of a problem with the sciatic nerve, the largest nerve in the body [S2]. It can cause pain, weakness, numbness, or tingling that starts in the lower back and runs down the leg to the calf, foot, or toes, usually on one side [S2]. Back pain may also spread into the buttocks, leg, or hip, or cause numbness or weakness in the legs or feet [S3].

### How it is diagnosed
A doctor diagnoses a herniated disk with a physical exam and, sometimes, imaging tests [S1]. The doctor asks about the pain and may ask you to bend or lift your legs and test your reflexes, strength, and feeling [S3]. One review notes that a history and exam alone are not always accurate enough to confirm a disc herniation [S4]. MRI is the imaging test of choice because it shows soft tissue well and does not use ionizing radiation (the kind of radiation in X-rays) [S4]. CT scans and myelography (X-ray or scan images taken after dye is injected in the lower spine) are also used [S4]. Older studies found these tests have only moderate accuracy, so they can miss a herniation or show one that is not there [S4].

### Treatment options
Treatment includes rest, pain and anti-inflammatory medicines, physical therapy, and sometimes surgery [S1]. For sciatica, treatment depends on the cause and may include exercises, medicines, and surgery [S2]. Sometimes sciatica goes away on its own [S2]. A herniated disc can be absorbed by the body without surgery, a process linked to immune cells called macrophages and inflammation [S5]. Doctors cannot yet predict well which herniations will shrink this way [S5].

### When to seek care
NIAMS advises seeing a doctor if back pain does not improve after a few weeks [S3]. It also advises seeing a doctor if back pain comes with any of these [S3]:
- Numbness and tingling.
- Severe pain that does not improve with medicine.
- Pain after a fall or injury.
- Trouble urinating, weakness, pain, or numbness in the legs, fever, or weight loss you did not intend.

## Common Misunderstandings
- **Myth:** A herniated disk always needs surgery. **Fact:** Most people recover with treatment, and a herniated disc can even be absorbed by the body without surgery [S1][S5].
- **Myth:** Sciatica is its own disease. **Fact:** Sciatica is a symptom of a problem with the sciatic nerve, and a ruptured disk is only one possible cause [S2].
- **Myth:** An MRI or CT scan always gives a clear yes or no. **Fact:** Studies found these scans have moderate accuracy and can give false results [S4].
- **Myth:** Sciatica always means a herniated disk. **Fact:** Sciatica can also come from spinal stenosis (a narrowed spinal canal) or an injury, and often no cause is found [S2].

## Questions to Ask Your Doctor
1. Is my back or leg pain caused by a herniated disk, or could it be something else, like spinal stenosis?
2. Do I need an imaging test, and what can it show or miss?
3. Could physical therapy or exercises help me?
4. How long might it take for my symptoms to improve?
5. When would surgery be worth talking about?
6. Which symptoms mean I should call you right away?

## Test Questions
1. What happens in a herniated disk? - The disk ruptures and its jelly-like center leaks out and irritates nearby nerves [S1].
2. What is sciatica? - Pain, numbness, tingling, or weakness from the sciatic nerve that runs from the lower back down the leg [S2].
3. Which imaging test is the test of choice for a suspected lumbar disc herniation? - MRI [S4].
4. Name two treatments for a herniated disk. - Rest, pain or anti-inflammatory medicines, physical therapy, or sometimes surgery [S1].
5. Can a herniated disc get better without surgery? - Yes, it can be absorbed by the body on its own [S5].

## Related Topics
- Often confused with: Lumbar Spinal Stenosis (KO-SPINE-COND-001)
- Read next: Physical Therapy for Low Back Pain (KO-SPINE-TRT-001)
- Proposed topics (not yet in the library): intervertebral disc, sciatic nerve, sciatica, spinal MRI, lumbar discectomy

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Herniated Disk.* https://medlineplus.gov/herniateddisk.html (retrieved 2026-10-26)
2. [S2] MedlinePlus, U.S. National Library of Medicine. *Sciatica.* https://medlineplus.gov/sciatica.html (retrieved 2026-10-26)
3. [S3] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Back Pain.* https://www.niams.nih.gov/health-topics/back-pain (retrieved 2026-10-26)
4. [S4] Chiropractic & Manual Therapies. *Diagnostic accuracy of diagnostic imaging for lumbar disc herniation in adults with low back pain or sciatica is unknown; a systematic review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC6102824/ (retrieved 2026-10-26)
5. [S5] Arthritis research & therapy. *Characteristics and mechanisms of resorption in lumbar disc herniation.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9396855/ (retrieved 2026-11-14)
