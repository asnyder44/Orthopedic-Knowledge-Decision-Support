---
schema_version: okds-ko-1.0
ko_id: KO-HAND-CONC-001
title: Hand Numbness and Tingling
preferred_term: Hand Numbness and Tingling
alternate_terms:
- paresthesia
- hand paresthesia
- pins and needles
ko_type: Concept
specialty: HAND
cluster: 7
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Numbness (loss of feeling) and tingling (a "pins and needles" feeling) in the hand are signs that
  a nerve is not sending messages normally [S1][S3]. They can come from a nerve squeezed at the wrist or
  elbow, from narrowing in the neck, or from diseases that affect nerves, such as diabetes or multiple sclerosis
  [S1][S2][S3][S4][S5]. Which fingers are affected can give clues about the cause, so a health care provider
  checks the pattern and may order tests [S1][S4].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- numbness
- tingling
- pins and needles
- nerve compression
- carpal tunnel syndrome
- cubital tunnel syndrome
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-COND-001
  target_label: Carpal Tunnel Syndrome
  source_ids:
  - S1
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-COND-002
  target_label: Cubital Tunnel Syndrome
  source_ids:
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-ANAT-001
  target_label: Median Nerve
  source_ids:
  - S1
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-ANAT-003
  target_label: Ulnar Nerve
  source_ids:
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-DX-001
  target_label: Nerve Conduction Study
  source_ids:
  - S1
proposed_concepts:
- term: Cervical spinal stenosis
  suggested_type: Condition
  predicate: PREREQUISITE_FOR
  reason: S2 says narrowing in the neck can cause numbness or tingling that spreads down the arms into the
    hands; only Lumbar Spinal Stenosis is in the registry.
- term: Diabetic peripheral neuropathy
  suggested_type: Condition
  predicate: PREREQUISITE_FOR
  reason: S5 lists numbness and paresthesia as the most common signs of diabetic nerve damage; not in the
    registry.
- term: Multiple sclerosis
  suggested_type: Condition
  predicate: PREREQUISITE_FOR
  reason: S3 lists numbness, tingling, and 'pins and needles' as common MS symptoms; not in the registry
    (outside orthopedics, may stay as an external link).
sources:
- id: S1
  title: Carpal Tunnel Syndrome
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/carpaltunnelsyndrome.html
  source_type: government_health_page
  audience: patient
  publication_date: '2024-01-10'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:carpaltunnelsyndrome). Licence: Public domain (NLM-authored
    MedlinePlus summary); credit MedlinePlus'
- id: S2
  title: Spinal Stenosis
  publisher: National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH)
  url: https://www.niams.nih.gov/health-topics/spinal-stenosis
  source_type: government_health_page
  audience: patient
  publication_date: '2023-11-01'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (niams:spinal-stenosis). Licence: Public domain (U.S. federal government
    work, NIH/NIAMS); credit NIAMS'
- id: S3
  title: Multiple Sclerosis
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/multiplesclerosis.html
  source_type: government_health_page
  audience: patient
  publication_date: '2026-09-17'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:multiplesclerosis). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
- id: S4
  title: 'From Conservative Measures to Surgical Interventions, Treatment Approaches for Cubital Tunnel
    Syndrome: A Comprehensive Review'
  publisher: Cureus
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10823195/
  source_type: journal_article
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC10823195). Licence: CC BY'
- id: S5
  title: 'Diabetic peripheral neuropathy: pathogenetic mechanisms and treatment'
  publisher: Frontiers in endocrinology
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10803883/
  source_type: journal_article
  audience: clinician
  publication_date: '2023'
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
  - No source in the pack is a general overview of hand numbness and tingling; the KO is built from pages
    about specific causes (CTS, spinal stenosis, MS, cubital tunnel syndrome, diabetic neuropathy). Consider
    adding a MedlinePlus 'Numbness' or 'Peripheral Nerve Disorders' page.
  - The sources use 'paresthesia' (S5) but do not define it; the KO treats it as tingling or 'pins and needles'
    (the registry's alternate terms). Clinician should confirm.
  - S5 (diabetic neuropathy review) is abstract-only and describes limb symptoms in general, mainly feet;
    it does not say the hands specifically.
  - 'The list of causes is not complete and does not rank how common each cause is; the sources here do
    not give urgent warning signs (for example, sudden numbness), so the KO points readers to a clinician.'
  - MeSH ID and ICD-10-CM code are not stated in any source; left as verify.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus or NIAMS shows a new 'last updated' or 'last reviewed' date on a cited page.
- A general patient page on numbness and tingling is added to the dataset.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Numbness (loss of feeling) and tingling (a "pins and needles" feeling) in the hand are signs that a nerve is not sending messages normally [S1][S3]. They can come from a nerve squeezed at the wrist or elbow, from narrowing in the neck, or from diseases that affect nerves, such as diabetes or multiple sclerosis [S1][S2][S3][S4][S5]. Which fingers are affected can give clues about the cause, so a health care provider checks the pattern and may order tests [S1][S4].

## Key Facts (claim → source)
- Nerves carry feeling from the hand, and when a nerve is squeezed or damaged it may not work well, which can cause numbness, tingling, and weakness [S1][S3].
- Numbness or tingling in the thumb, index, and middle fingers is typical of carpal tunnel syndrome, a squeezed median nerve at the wrist [S1].
- Numbness and tingling in the ring and little fingers is typical of cubital tunnel syndrome, a squeezed ulnar nerve at the elbow [S4].
- Narrowing of the spine in the neck can cause numbness or tingling that spreads down the arms into the hands [S2].
- Numbness, tingling, or a "pins and needles" feeling is a common symptom of multiple sclerosis, a disease of the brain and spinal cord [S3].
- Numbness and tingling are among the most common signs of nerve damage from diabetes [S5].
- Without treatment, a squeezed nerve can lead to lasting loss of feeling and weakness, so early diagnosis matters [S1][S4].

## Explanation
### Explanation
Nerves carry messages between the body and the brain, including the sense of touch [S1][S3]. In the hand, the median nerve gives feeling to the thumb and the first three fingers, and the ulnar nerve gives feeling to the ring and little fingers [S1][S4]. When a nerve is squeezed, irritated, or damaged, its messages can slow down or get blocked [S1][S3]. This can cause numbness (less or no feeling), tingling or burning, a "pins and needles" feeling, pain, or weakness [S1][S3][S4]. Doctors may use the word paresthesia for these abnormal feelings, alongside numbness [S5].

The problem can start at different places along the nerve's path [S1][S2][S4]:
- At the wrist, as in carpal tunnel syndrome [S1].
- At the elbow, as in cubital tunnel syndrome [S4].
- In the neck, where narrowing of the spine presses on nerve roots [S2].
- In the brain and spinal cord, as in multiple sclerosis [S3].
- In many nerves at once, as in nerve damage from diabetes [S5].

To find the cause, a health care provider asks about symptoms and health history and does a physical exam that checks feeling, strength, and reflexes [S1][S2][S3]. Tests may include lab tests, X-rays, tests of the electrical activity in nerves and muscles, ultrasound of a nerve, or an MRI scan [S1][S3]. Early diagnosis and treatment can help prevent lasting nerve damage, so numbness or tingling that keeps coming back is worth checking with a provider [S1][S4]. The sources here do not list urgent warning signs, so ask a clinician which symptoms need prompt care.

### Examples
- **Carpal tunnel syndrome:** numbness, tingling, or burning in the thumb, index, and middle fingers, often at night if the wrists are bent during sleep, and often in both hands [S1].
- **Cubital tunnel syndrome:** numbness and tingling in the ring and little fingers, with hand weakness and pain along the inner elbow [S4].
- **Spinal stenosis in the neck:** neck pain, with numbness or tingling that spreads down the arms into the hands, and weakness in a hand, arm, or fingers [S2].
- **Multiple sclerosis:** numbness, tingling, or "pins and needles," along with other symptoms such as vision problems, weakness, or trouble with balance [S3].
- **Diabetic peripheral neuropathy:** numbness, tingling, and pain on both sides of the body, which become more common the longer a person has diabetes [S5].

## Common Misunderstandings
- **Myth:** Hand numbness always means carpal tunnel syndrome. **Fact:** It can also come from a squeezed ulnar nerve at the elbow, narrowing in the neck, multiple sclerosis, or diabetes [S2][S3][S4][S5].
- **Myth:** It does not matter which fingers are numb. **Fact:** Carpal tunnel syndrome mainly affects the thumb, index, and middle fingers, while ulnar nerve problems affect the ring and little fingers [S1][S4].
- **Myth:** Tingling that comes and goes is never worth checking. **Fact:** Without treatment, a squeezed nerve can cause lasting loss of feeling and weakness [S1][S4].

## Questions to Ask Your Doctor
1. Which nerve could be causing my numbness, based on the fingers that are affected?
2. Could the problem be in my wrist, my elbow, or my neck?
3. Do I need nerve tests, an ultrasound, or other tests?
4. Could a health condition such as diabetes be playing a part?
5. Which symptoms should make me seek care right away?

## Test Questions
1. Which fingers are usually numb in carpal tunnel syndrome? - The thumb, index, and middle fingers [S1].
2. Which fingers are usually numb when the ulnar nerve is squeezed at the elbow? - The ring and little fingers [S4].
3. How can a problem in the neck cause hand numbness? - Narrowing of the spine in the neck can cause numbness or tingling that spreads down the arms into the hands [S2].
4. Name a disease of the brain and spinal cord that can cause "pins and needles." - Multiple sclerosis [S3].
5. Why should ongoing hand numbness be checked? - Early diagnosis and treatment can help prevent lasting nerve damage [S1][S4].

## Related Topics
- Read next: Carpal Tunnel Syndrome (KO-HAND-COND-001), Cubital Tunnel Syndrome (KO-HAND-COND-002)
- Nerves: Median Nerve (KO-HAND-ANAT-001), Ulnar Nerve (KO-HAND-ANAT-003)
- Tests: Nerve Conduction Study (KO-HAND-DX-001)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Carpal Tunnel Syndrome.* https://medlineplus.gov/carpaltunnelsyndrome.html (retrieved 2026-10-26)
2. [S2] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Spinal Stenosis.* https://www.niams.nih.gov/health-topics/spinal-stenosis (retrieved 2026-10-26)
3. [S3] MedlinePlus, U.S. National Library of Medicine. *Multiple Sclerosis.* https://medlineplus.gov/multiplesclerosis.html (retrieved 2026-10-26)
4. [S4] Cureus. *From Conservative Measures to Surgical Interventions, Treatment Approaches for Cubital Tunnel Syndrome: A Comprehensive Review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10823195/ (retrieved 2026-10-26)
5. [S5] Frontiers in endocrinology. *Diabetic peripheral neuropathy: pathogenetic mechanisms and treatment.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10803883/ (retrieved 2026-11-14)
