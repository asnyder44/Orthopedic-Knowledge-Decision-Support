---
schema_version: okds-ko-1.0
ko_id: KO-HAND-DX-002
title: Phalen's Test
preferred_term: Phalen's Test
alternate_terms:
- wrist flexion test
- Phalen maneuver
- Phalen sign
- Phalen test
ko_type: DiagnosticTest
specialty: HAND
cluster: 3
audience:
- patient
- caregiver
- student
reading_level: grade 6-8
difficulty: beginner
summary: 'Phalen''s test is a quick exam test for carpal tunnel syndrome: the wrists are bent down as
  far as they go and held for about 30 to 60 seconds, and the test is positive if this brings on tingling,
  numbness, or pain in the fingers served by the median nerve [S1][S2][S3]. It is easy to do, but it cannot
  confirm carpal tunnel syndrome on its own [S1][S2].'
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- carpal tunnel
- wrist
- physical exam
- provocative test
- numbness
- tingling
- median nerve
- hand exam
relationships:
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-DX-001
  target_label: Nerve Conduction Study
  source_ids:
  - S1
  - S2
proposed_concepts:
- term: Tinel's Sign
  suggested_type: DiagnosticTest
  predicate: CONTRASTS_WITH
  reason: The other common carpal tunnel exam test, often done together with Phalen's test and easy to
    confuse with it [S1][S2][S3].
- term: Durkan's Test (carpal compression test)
  suggested_type: DiagnosticTest
  predicate: CONTRASTS_WITH
  reason: Another exam test for carpal tunnel syndrome that presses on the nerve instead of bending the
    wrist [S2].
- term: Boston Carpal Tunnel Questionnaire
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: Questionnaire used with Phalen's test to follow recovery after surgery [S3]; link would go from
    Carpal Tunnel Syndrome.
sources:
- id: S1
  title: Correlations of Tinel and Phalen Signs with Nerve Conduction Study Test Results in a Randomly
    Chosen Population of Patients with Carpal Tunnel Syndrome
  publisher: NeuroSci, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12550957/
  source_type: journal_article
  audience: clinician
  publication_date: '2025-09-28'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: Kaczmarek K, et al. CC BY 4.0. Pack keeps the abstract, introduction, test methods, discussion,
    and conclusions (tables, figures, and statistics sections removed). Accepted 2025-09-25.
- id: S2
  title: 'Carpal Tunnel Syndrome: Pathophysiology and Comprehensive Guidelines for Clinical Evaluation
    and Treatment'
  publisher: Cureus, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9389835/
  source_type: journal_article
  audience: clinician
  publication_date: '2022-07-20'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: Joshi A, et al. CC BY. Pack keeps only the 'Ways to test for carpal tunnel syndrome' passage
    and the start of treatment options. One figure is CC BY-NC; no figures copied.
- id: S3
  title: Usefulness of the Phalen Test and the Tinel Sign in the Prognosis and the Impact on Quality of
    Life of Patients with Carpal Tunnel Syndrome Undergoing Classical Open Carpal Tunnel Release
  publisher: Revista Brasileira de Ortopedia, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10957282/
  source_type: journal_article
  audience: clinician
  publication_date: '2024-03-21'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: Pimentel BFR, et al. CC BY 4.0. Pack keeps the English abstract, introduction, methods, discussion,
    and conclusions (Portuguese abstract and results tables removed). Accepted 2023-06-26.
review:
  status: draft
  author: OKDS agent (Claude)
  generated_by:
    model: claude-opus-5-5
    prompt_version: okds-gen-1.0
  ai_check: null
  team_checker: null
  clinician_reviewer: null
  clinician_role: null
  review_date: null
  open_issues:
  - All three sources are clinician-level research papers; there is no public-domain patient page for
    this test. A clinician should check the plain-language rewrites, especially the accuracy numbers.
  - 'Accuracy numbers differ between sources: S2 gives sensitivity 0.5 and specificity 0.33 (the specificity
    seems low and is from one cited study); S1 reports 47% positive among nerve-test-confirmed cases.
    A clinician should confirm these numbers and whether to keep them.'
  - Sources describe the test slightly differently (backs of hands pressed together vs. wrists bent and
    held, 30-60 s vs. about 60 s, active vs. passive bending). The KO lists the variations; a clinician
    should confirm the standard method.
  - S3 studied only women aged 40-80 having open carpal tunnel release; the follow-up finding may not
    apply to everyone.
  - MeSH ID is unknown ('<verify>'); ICD-10-CM does not usually apply to an exam test.
  - The vocab has no DiagnosticTest -> Condition predicate. Add 'KO-HAND-COND-001 DIAGNOSED_BY KO-HAND-DX-002'
    in the Carpal Tunnel Syndrome KO.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-01'
last_updated: '2026-11-01'
update_triggers:
- A new systematic review or guideline reports the accuracy of Phalen's test for carpal tunnel syndrome.
- AAOS updates its carpal tunnel syndrome guideline on physical exam tests.
- Any cited page shows a new 'last reviewed' date.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-01'
  by: OKDS agent (Claude)
  change: Initial AI draft written by the agent from source pack SP-KO-HAND-DX-002 (claude-opus-5-5, okds-gen-1.0).
---

## Summary
Phalen's test is a simple hand exam used to look for carpal tunnel syndrome (CTS), a condition where the median nerve is squeezed at the wrist [S1][S3]. The wrists are bent down as far as they go and held there for about 30 to 60 seconds [S1][S2][S3]. If this brings on tingling, numbness, or pain in the fingers served by the median nerve, the test is called positive [S1][S2]. It is quick and easy, but it cannot prove CTS by itself [S1][S2].

## Key Facts (claim → source)
- Phalen's test and Tinel's test are the most common exam tests doctors use for CTS [S1][S3].
- Bending the wrist increases the pressure on the median nerve [S2].
- A positive test brings back the person's usual symptoms, mainly tingling [S2].
- The fingers that matter are the thumb, index finger, middle finger, and half of the ring finger [S1].
- In one 2025 study, only 47% of people whose nerve tests showed CTS had a positive Phalen's test [S1].
- Doctors add other tests, such as a nerve conduction study, to confirm CTS [S1][S2].
- After carpal tunnel surgery, Phalen's test often turns negative, and in one study it did so sooner than Tinel's sign [S3].

## Explanation
### What it checks
When the wrist is bent, the median nerve is pressed between a tough band of tissue across the wrist (the flexor retinaculum) and the end of a forearm bone (the radius) [S2]. Phalen's test is a "provocative" test, which means it tries to bring on symptoms on purpose [S1]. If bending the wrist brings on the person's usual CTS symptoms, this points to a squeezed median nerve [S2]. CTS symptoms include pain, numbness, and tingling in the fingers served by the median nerve, often at night [S1].

### How it is done
Sources describe a few slightly different ways:
- The person presses the backs of both hands together, which bends both wrists, for 30 to 60 seconds [S2].
- The person bends both wrists down as far as they can and holds them for about 60 seconds [S1].
- The person rests the elbow, bent at a right angle, on the exam table while the wrist is placed fully bent [S3].

The test is positive if tingling or pain starts in the thumb, index finger, middle finger, half of the ring finger, or the forearm [S1]. In one study, tingling that began within 30 to 60 seconds counted as positive [S3]. The test is quick and easy to do [S1].

### What results can mean
- **Positive:** Bending the wrist brought on the usual symptoms, which supports a diagnosis of CTS [S2]. One study found Phalen's test most useful for spotting mild CTS [S1].
- **Negative:** No symptoms came on. This does not rule out CTS, because many people with CTS shown on nerve tests have a negative Phalen's test [S1].
- **Over time:** Doctors can repeat the test after treatment [S3]. In a study of women who had open carpal tunnel surgery, Phalen's test turned negative sooner than Tinel's sign [S3]. When both tests turned negative from the second week after surgery, patients tended to recover well [S3].

### Limits
- A positive Phalen's test alone is not enough to confirm CTS [S1][S2]. Doctors often add a nerve conduction study, which measures how well signals travel along the median nerve, or imaging such as ultrasound or MRI [S1][S2].
- Studies report very different accuracy for this test [S1]. One review gives its sensitivity (how often it is positive in people who have CTS) as 0.5, which means it may miss about half of cases [S2].
- Phalen's test results match nerve test results only weakly [S1].
- Other nerve problems, including problems with nerve roots in the neck, can make results harder to read [S1].
- Researchers say nerve conduction studies are still needed to confirm CTS, judge how severe it is, and help plan treatment, including surgery [S1].

### Similar exam tests
- **Tinel's test:** the examiner taps over the median nerve at the wrist; it is positive if this causes tingling or pain along the path of the nerve into the fingers [S1][S2]. In one study, it was even less likely than Phalen's test to be positive in people with CTS [S1].
- **Durkan's test:** the examiner presses both thumbs over the carpal tunnel for 15 to 30 seconds and checks whether symptoms appear [S2].

## Common Misunderstandings
- **Myth:** A positive Phalen's test means you definitely have CTS. **Fact:** A positive result alone cannot confirm CTS, so other tests are usually needed [S1][S2].
- **Myth:** A negative Phalen's test means you do not have CTS. **Fact:** Many people with CTS shown on nerve tests have a negative Phalen's test [S1].
- **Myth:** Phalen's test and Tinel's test are the same thing. **Fact:** Phalen's test bends the wrist, while Tinel's test taps over the nerve [S1][S2].
- **Myth:** The test is only useful once, at diagnosis. **Fact:** Doctors can repeat it after surgery to help follow recovery [S3].

## Questions to Ask Your Doctor
1. What did my Phalen's test show, and what does that mean?
2. Do I need a nerve conduction study or an ultrasound to confirm the diagnosis?
3. Which other exam tests did you do, and what did they show?
4. Could another problem, such as one in my neck, be causing my symptoms?
5. Will you repeat this test to check how I am doing after treatment?

## Test Questions
1. How is Phalen's test done? - The wrists are bent down as far as they go (for example, by pressing the backs of the hands together) and held for about 30 to 60 seconds [S1][S2].
2. What makes Phalen's test positive? - It brings on tingling, numbness, or pain in the fingers served by the median nerve [S1][S2].
3. Why does bending the wrist bring on symptoms? - It increases pressure on the median nerve at the wrist [S2].
4. Can a positive Phalen's test alone confirm carpal tunnel syndrome? - No; other tests, such as a nerve conduction study, are usually needed [S1][S2].
5. In the 2025 study, what share of people with nerve-test-confirmed CTS had a positive Phalen's test? - Only 47% [S1].
6. After open carpal tunnel surgery, which turned negative sooner: Phalen's test or Tinel's sign? - Phalen's test [S3].

## Related Topics
- Compared with: Nerve Conduction Study (KO-HAND-DX-001), the nerve test used to confirm CTS
- Used to check for: Carpal Tunnel Syndrome (KO-HAND-COND-001)
- Proposed topics (not in the registry yet): Tinel's Sign; Durkan's Test; Boston Carpal Tunnel Questionnaire

## References
1. [S1] NeuroSci, via PubMed Central. *Correlations of Tinel and Phalen Signs with Nerve Conduction Study Test Results in a Randomly Chosen Population of Patients with Carpal Tunnel Syndrome.* https://pmc.ncbi.nlm.nih.gov/articles/PMC12550957/ (retrieved 2026-11-01)
2. [S2] Cureus, via PubMed Central. *Carpal Tunnel Syndrome: Pathophysiology and Comprehensive Guidelines for Clinical Evaluation and Treatment.* https://pmc.ncbi.nlm.nih.gov/articles/PMC9389835/ (retrieved 2026-11-01)
3. [S3] Revista Brasileira de Ortopedia, via PubMed Central. *Usefulness of the Phalen Test and the Tinel Sign in the Prognosis and the Impact on Quality of Life of Patients with Carpal Tunnel Syndrome Undergoing Classical Open Carpal Tunnel Release.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10957282/ (retrieved 2026-11-01)
