---
schema_version: okds-ko-1.0
ko_id: KO-HAND-DX-006
title: Durkan's Test
preferred_term: Durkan's Test
alternate_terms:
- carpal compression test
- CCT
- Durkan test
- median nerve compression test
ko_type: DiagnosticTest
specialty: HAND
cluster: 3
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Durkan's test, also called the carpal compression test, is an office exam in which the doctor
  presses over the median nerve at the wrist to see if this brings on numbness or tingling [S1][S2]. It
  is used to check for carpal tunnel syndrome, but studies report very different accuracy, so it is used
  along with other tests and the patient's history [S2][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- physical exam
- provocative test
- carpal tunnel
- numbness
- tingling
- median nerve
relationships:
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-DX-002
  target_label: Phalen's Test
  source_ids:
  - S2
  - S3
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-DX-004
  target_label: Tinel's Sign
  source_ids:
  - S2
  - S3
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-DX-001
  target_label: Nerve Conduction Study
  source_ids:
  - S3
  - S4
proposed_concepts:
- term: Phdurkan test
  suggested_type: DiagnosticTest
  predicate: CONTRASTS_WITH
  reason: Combines wrist bending (Phalen's test) with pressure on the carpal tunnel (Durkan's test); more
    sensitive but less specific than Durkan's test alone [S3].
sources:
- id: S1
  title: Carpal Tunnel Syndrome
  publisher: National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH)
  url: https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome
  source_type: government_health_page
  audience: patient
  publication_date: '2023-12-22'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (niams:carpal-tunnel-syndrome). Licence: Public domain (U.S. federal
    government work, NIH/NIAMS); credit NIAMS'
- id: S2
  title: 'Sensitivity and Specificity of Examination Maneuvers for Carpal Tunnel Syndrome: A Meta-Analysis'
  publisher: Cureus
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10446104/
  source_type: journal_article
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC10446104). Licence: CC BY'
- id: S3
  title: Accuracy of Provocative Tests for Carpal Tunnel Syndrome
  publisher: Journal of hand surgery global online
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8991863/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via europepmc. Licence: cc by-nc-nd. Type: article. Text kept: abstract only.'
- id: S4
  title: 'Durkan Gauge and Carpal Compression Test: Accuracy and Diagnostic Test Properties'
  publisher: Journal of Orthopaedic & Sports Physical Therapy (JOSPT)
  url: https://doi.org/10.2519/jospt.2000.30.11.676
  source_type: journal_article
  audience: clinician
  publication_date: '2000'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via openaire. Licence: Open Access. Type: article. Text kept: abstract only.'
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
  - The pack does not say how long the pressure is held or how hard to press with the thumb; a clinician
    should check the 'How it is done' wording and consider a source that describes the method.
  - S3 is licensed CC BY-NC-ND and S4 is link_and_paraphrase; only abstracts are in the pack. Check that
    no sentence is copied.
  - S2 pack text includes only the abstract and introduction; the original 1991 Durkan figures and the
    AAOS guideline change are reported second-hand through S2.
  - Studies disagree widely on accuracy (S2-S4); the numbers given are from single studies or pooled medians
    and should be checked by a clinician.
  - MeSH ID is unknown ('<verify>'); ICD-10-CM does not usually apply to a test.
  - The vocab has no DiagnosticTest -> Condition predicate. A DIAGNOSED_BY link should be added from the
    Carpal Tunnel Syndrome (KO-HAND-COND-001) KO.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- AAOS updates its carpal tunnel syndrome guideline on physical exam tests or nerve testing.
- A new meta-analysis reports the accuracy of the carpal compression test.
- Any cited page shows a new 'last reviewed' date.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Durkan's test, also called the carpal compression test, is a quick exam a doctor can do in the office [S2][S4]. The doctor presses on the median nerve at the wrist to see if this causes numbness or tingling in the fingers [S1][S4]. A positive result can point to carpal tunnel syndrome (CTS), a condition where the median nerve is squeezed at the wrist [S1]. Studies report very different accuracy for this test, so doctors use it together with other exam tests and your history [S2][S3].

## Key Facts (claim → source)
- The test was described by Durkan in 1991 [S2].
- During the exam, the doctor checks whether pressing on the median nerve at the wrist causes numbness or tingling [S1].
- The first report found the test very accurate, but later studies found wide differences between examiners and methods [S2].
- In a 2023 review of 67 studies, Durkan's test had the second-highest typical sensitivity (ability to find true cases) of the exam tests, after Phalen's test [S2].
- In one study of 85 hands, Durkan's test found many true cases but often flagged CTS in people who did not have it [S3].
- When pressure was applied with a measuring tool called the Durkan gauge, the test was neither sensitive nor specific in one study [S4].
- A combination of exam tests plus the person's history should guide the diagnosis of CTS [S2].

## Explanation
### What it checks
The median nerve runs from the forearm through the wrist into the hand and gives feeling to the thumb, index finger, middle finger, and part of the ring finger [S1]. In CTS, this nerve is pressed or squeezed inside the carpal tunnel, a narrow tube of ligament and bones at the base of the hand [S1]. Durkan's test adds pressure over the carpal tunnel to see if this brings on the person's symptoms [S1][S3]. It is one of several "provocative" tests, meaning tests that try to bring on symptoms, along with Tinel's sign and Phalen's test [S3].

### How it is done
- The doctor presses directly over the carpal tunnel at the wrist, often using thumb pressure [S1][S4].
- Some examiners have used a pressure gauge (the Durkan gauge) instead of thumb pressure [S4].
- The test checks whether the pressure causes numbness or tingling in the fingers [S1].
- Pressure can also be combined with wrist bending; this mix is sometimes called the Phdurkan test [S3].

### What results can mean
- Numbness or tingling during the test suggests the median nerve may be squeezed at the wrist [S1].
- A positive test fits with CTS, but no single exam test proves the diagnosis [S2].
- Doctors weigh the result with your history and other exam findings, and sometimes with nerve tests [S2][S3].
- Tests that push harder to bring on symptoms tend to find more true cases but also give more false alarms [S3].

### Limits
- Reported accuracy varies a lot between studies, examiners, and methods [S2].
- In one study, the test found 71 of 100 true cases but correctly cleared only 22 of 100 people without CTS [S3].
- When done with a pressure gauge, the test missed most cases in one study, even though the gauge itself measured pressure correctly [S4].
- There is no single, generally accepted gold-standard test for CTS, which makes it hard to judge exam tests [S2].

## Common Misunderstandings
- **Myth:** A positive Durkan's test proves you have carpal tunnel syndrome. **Fact:** No single exam test is enough; a mix of tests and history should guide the diagnosis [S2].
- **Myth:** The test gives the same result no matter who does it. **Fact:** Accuracy has varied widely between examiners and methods [S2].
- **Myth:** Using a pressure gauge makes the test more accurate. **Fact:** In one study, the gauge measured pressure well, but the test itself was not accurate when done this way [S4].
- **Myth:** Durkan's test and Phalen's test are the same thing. **Fact:** Durkan's test presses on the wrist, while Phalen's test bends the wrist; they can be combined [S1][S3].

## Questions to Ask Your Doctor
1. What did the wrist-pressure test show?
2. Which other exam tests are you using to check for carpal tunnel syndrome?
3. Do I need a nerve conduction study to confirm the result?
4. Could something else be causing my numbness or tingling?
5. How will this result affect my treatment options?

## Test Questions
1. What is another name for Durkan's test? - The carpal compression test [S4].
2. What does the doctor do during the test? - Presses over the median nerve at the wrist to see if it causes numbness or tingling [S1].
3. In what year did Durkan describe the test? - 1991 [S2].
4. Which exam test had a higher typical sensitivity than Durkan's test in a 2023 review? - Phalen's test [S2].
5. What happens to a test's accuracy as it becomes more provocative? - It finds more true cases but gives more false positives [S3].
6. Was the test accurate when done with the Durkan gauge in one study? - No; it was neither sensitive nor specific [S4].

## Related Topics
- Compared with: Phalen's Test (KO-HAND-DX-002), a wrist-bending exam test
- Compared with: Tinel's Sign (KO-HAND-DX-004), a tapping exam test
- Compared with: Nerve Conduction Study (KO-HAND-DX-001), the nerve test used as a reference in studies
- Used to diagnose (link to be added from the condition KO): Carpal Tunnel Syndrome (KO-HAND-COND-001)
- Proposed topic (not in the registry yet): Phdurkan test

## References
1. [S1] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Carpal Tunnel Syndrome.* https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome (retrieved 2026-10-26)
2. [S2] Cureus. *Sensitivity and Specificity of Examination Maneuvers for Carpal Tunnel Syndrome: A Meta-Analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10446104/ (retrieved 2026-10-26)
3. [S3] Journal of hand surgery global online. *Accuracy of Provocative Tests for Carpal Tunnel Syndrome.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8991863/ (retrieved 2026-11-14)
4. [S4] Journal of Orthopaedic & Sports Physical Therapy (JOSPT). *Durkan Gauge and Carpal Compression Test: Accuracy and Diagnostic Test Properties.* https://doi.org/10.2519/jospt.2000.30.11.676 (retrieved 2026-11-14)
