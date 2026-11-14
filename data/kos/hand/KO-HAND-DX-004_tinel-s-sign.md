---
schema_version: okds-ko-1.0
ko_id: KO-HAND-DX-004
title: Tinel's Sign
preferred_term: Tinel's Sign
alternate_terms:
- Tinel sign
- Tinel's test
- Hoffmann-Tinel sign
- nerve percussion test
ko_type: DiagnosticTest
specialty: HAND
cluster: 3
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Tinel's sign is a quick office test in which the doctor taps over a nerve; if this causes tingling
  or a small electric-shock feeling along the nerve, the sign is positive [S1][S2]. It is used to look
  for a squeezed or healing nerve, such as the median nerve in carpal tunnel syndrome, but it is not accurate
  enough to diagnose the condition alone [S2][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- physical exam
- provocative test
- tapping test
- carpal tunnel
- numbness
- tingling
- nerve damage
relationships:
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-DX-002
  target_label: Phalen's Test
  source_ids:
  - S1
  - S4
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-DX-006
  target_label: Durkan's Test
  source_ids:
  - S1
  - S4
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-DX-001
  target_label: Nerve Conduction Study
  source_ids:
  - S2
  - S3
proposed_concepts:
- term: CTS-6 (Carpal Tunnel Syndrome-6 diagnostic tool)
  suggested_type: DiagnosticTest
  predicate: CONTRASTS_WITH
  reason: Checklist of history and exam items, including Tinel's sign, used together to diagnose carpal
    tunnel syndrome [S4].
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
  title: 'Tinel''s sign – significance, mechanism, and diagnostic application: A Literature Review'
  publisher: Zenodo
  url: https://zenodo.org/records/17129324
  source_type: journal_article
  audience: clinician
  publication_date: '2025'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via zenodo. Licence: cc-by-4.0. Type: review. Text kept: abstract only.'
- id: S3
  title: 'Diagnostic accuracy of the Hoffmann-Tinel sign for carpal tunnel syndrome: A systematic review
    and meta-analysis with comparison of techniques'
  publisher: Journal of Clinical Orthopaedics and Trauma
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13242039/
  source_type: journal_article
  audience: clinician
  publication_date: '2026'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC13242039). Licence: CC BY'
- id: S4
  title: 'Sensitivity and Specificity of Examination Maneuvers for Carpal Tunnel Syndrome: A Meta-Analysis'
  publisher: Cureus
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10446104/
  source_type: journal_article
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC10446104). Licence: CC BY'
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
  - S2 (Zenodo literature review) is an abstract only from a repository; check that it is peer reviewed
    and that the CC BY 4.0 licence is correct.
  - The NICE statement (clinical tests such as Tinel's sign for first assessment) and the AAOS guideline
    change are reported second-hand through S3 and S4; check them against the current guidelines.
  - S4 pack text includes only the abstract and introduction, so its pooled numbers for Tinel's sign are
    not in the pack; accuracy numbers here come from S3.
  - The sources do not say how long tingling must last or exactly where to tap; a clinician should check
    the 'How it is done' wording.
  - MeSH ID is unknown ('<verify>'); ICD-10-CM does not usually apply to a test.
  - The vocab has no DiagnosticTest -> Condition predicate. DIAGNOSED_BY links should be added from the
    Carpal Tunnel Syndrome (KO-HAND-COND-001) and Cubital Tunnel Syndrome (KO-HAND-COND-002) KOs.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- NICE or AAOS updates its carpal tunnel syndrome guidance on clinical tests.
- A new meta-analysis reports the accuracy of Tinel's sign by tapping method.
- Any cited page shows a new 'last reviewed' date.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Tinel's sign is a simple test a doctor does in the office by tapping over a nerve [S1][S3]. If the tapping causes tingling or a feeling like a small electric shock along the nerve, the sign is called positive [S2]. Doctors use it to look for a nerve that is squeezed or healing, for example the median nerve at the wrist in carpal tunnel syndrome (CTS) [S1][S2]. It is quick and low-cost, but it can miss the problem or point to it when it is not there, so doctors use it together with other tests [S2][S3][S4].

## Key Facts (claim → source)
- Tinel's sign was first described in 1915 [S2].
- It was first developed to find nerve damage after wartime injuries and was later used for CTS [S3].
- Tapping on a damaged or healing nerve can cause tingling or shock-like feelings along the nerve's path [S2].
- Doctors tap with either a fingertip or a small tool called a tendon hammer [S3].
- In a 2026 review, tapping with a tendon hammer found CTS more often than tapping with a fingertip [S3].
- UK guidelines (NICE) support clinical tests such as Tinel's sign for the first check for CTS [S3].
- No single exam test is enough by itself to diagnose CTS [S4].

## Explanation
### What it checks
Tinel's sign is a test that does not break the skin and is used to check how well a nerve in the arms or legs is working [S2]. A nerve that is damaged or growing back can send false signals when it is tapped, and the person feels this as tingling or a small shock in the area that nerve supplies [S2]. Doctors use it for nerve compression problems, such as carpal tunnel syndrome and cubital tunnel syndrome (a squeezed nerve at the elbow), and after nerve injuries [S2]. It can also be used to follow a nerve as it heals [S2].

In CTS, the median nerve, which gives feeling to the thumb and the first fingers, is squeezed at the wrist [S1]. During the exam, the doctor checks whether tapping on this nerve causes numbness or tingling [S1].

### How it is done
- The doctor taps over the nerve, for CTS over the median nerve at the wrist [S1].
- The tapping can be done with a fingertip or with a tendon hammer [S3].
- You tell the doctor if you feel tingling or a shock-like feeling in your fingers [S1][S2].
- It is often done along with other exam tests, such as Phalen's test (bending the wrist) and Durkan's test (pressing on the wrist) [S1][S4].

### What results can mean
- A positive sign (tingling or a shock-like feeling) suggests the tapped nerve may be damaged, squeezed, or healing [S2].
- A positive sign at the wrist fits with CTS, but it does not prove it [S3][S4].
- Doctors combine the result with your history and other exam findings; the CTS-6 checklist, for example, includes Tinel's sign as one item among several [S4].
- Together with nerve tests and imaging, the sign can help find where a nerve problem is and track recovery [S2].

### Limits
- Studies report very different accuracy for this test [S2][S3][S4].
- Results depend on the person's own report and on how the examiner does the test, and there is no single standard method [S2][S3].
- In a review of 16 studies, tapping with a tendon hammer found about 62 of 100 people who had CTS, while fingertip tapping found only about 40 of 100 [S3].
- Because it misses many cases, a negative test does not rule out CTS [S3].
- Nerve conduction studies are often used for a firmer diagnosis [S3].

## Common Misunderstandings
- **Myth:** A positive Tinel's sign means you definitely have carpal tunnel syndrome. **Fact:** No single exam test is enough to diagnose CTS; doctors use a combination of tests and your history [S4].
- **Myth:** If tapping causes no tingling, the nerve is fine. **Fact:** The test misses many people who do have CTS, especially when done with a fingertip [S3].
- **Myth:** Tinel's sign is only for the wrist. **Fact:** It is also used for cubital tunnel syndrome at the elbow, thoracic outlet syndrome, and nerve injuries [S2].
- **Myth:** Every doctor does the test the same way. **Fact:** Some tap with a fingertip and some with a tendon hammer, and the method changes how accurate it is [S3].

## Questions to Ask Your Doctor
1. What did the tapping test show about my nerve?
2. Which other exam tests are you using along with it?
3. Do I need a nerve test or an ultrasound to confirm the result?
4. Could my symptoms come from a different nerve or place?
5. Will you repeat this test later to check how my nerve is healing?

## Test Questions
1. What does the doctor do during the Tinel's sign test? - Taps over a nerve, such as the median nerve at the wrist [S1].
2. What feeling makes the sign positive? - Tingling or an electric-shock feeling along the nerve [S2].
3. In what year was Tinel's sign first described? - 1915 [S2].
4. Which tapping method was more accurate in a 2026 review? - Tapping with a tendon hammer [S3].
5. Can Tinel's sign alone diagnose CTS? - No; no single exam test is enough on its own [S4].
6. Besides diagnosis, what else can the sign be used for? - To follow a nerve as it heals [S2].

## Related Topics
- Compared with: Phalen's Test (KO-HAND-DX-002), a wrist-bending exam test for carpal tunnel syndrome
- Compared with: Durkan's Test (KO-HAND-DX-006), a wrist-pressing exam test for carpal tunnel syndrome
- Compared with: Nerve Conduction Study (KO-HAND-DX-001), the nerve test used to confirm the diagnosis
- Used to diagnose (link to be added from the condition KOs): Carpal Tunnel Syndrome (KO-HAND-COND-001); Cubital Tunnel Syndrome (KO-HAND-COND-002)
- Proposed topic (not in the registry yet): CTS-6 diagnostic tool

## References
1. [S1] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Carpal Tunnel Syndrome.* https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome (retrieved 2026-10-26)
2. [S2] Zenodo. *Tinel's sign – significance, mechanism, and diagnostic application: A Literature Review.* https://zenodo.org/records/17129324 (retrieved 2026-11-14)
3. [S3] Journal of Clinical Orthopaedics and Trauma. *Diagnostic accuracy of the Hoffmann-Tinel sign for carpal tunnel syndrome: A systematic review and meta-analysis with comparison of techniques.* https://pmc.ncbi.nlm.nih.gov/articles/PMC13242039/ (retrieved 2026-10-26)
4. [S4] Cureus. *Sensitivity and Specificity of Examination Maneuvers for Carpal Tunnel Syndrome: A Meta-Analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10446104/ (retrieved 2026-10-26)
