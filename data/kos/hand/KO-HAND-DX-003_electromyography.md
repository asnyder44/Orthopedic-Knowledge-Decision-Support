---
schema_version: okds-ko-1.0
ko_id: KO-HAND-DX-003
title: Electromyography
preferred_term: Electromyography
alternate_terms:
- EMG
- needle electromyography
- needle EMG
- electrodiagnostic testing
- EDX
ko_type: DiagnosticTest
specialty: HAND
cluster: 3
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Electromyography (EMG) is a test that records the electrical activity inside muscles, using a
  thin needle placed in the muscle [S2]. In carpal tunnel syndrome it can show how much the muscles have
  been harmed and help rule out other nerve problems [S1][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- muscle test
- electrodiagnostic test
- EMG
- nerve damage
- carpal tunnel
- weakness
relationships:
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-DX-001
  target_label: Nerve Conduction Study
  source_ids:
  - S1
  - S3
  - S4
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-DX-005
  target_label: Nerve Ultrasound
  source_ids:
  - S1
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-PROC-001
  target_label: Carpal Tunnel Release
  source_ids:
  - S3
  - S4
proposed_concepts: []
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
  title: The basics of electromyography
  publisher: BMJ
  url: https://doi.org/10.1136/jnnp.2005.069211
  source_type: journal_article
  audience: clinician
  publication_date: '2005'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via openaire. Licence: Open Access. Type: article. Text kept: abstract only.'
- id: S3
  title: 'A Comparative Analysis Between Ultrasound and Electromyographic and Nerve Conduction Studies
    in Diagnosing Carpal Tunnel Syndrome (CTS): A Systematic Review and Meta-Analysis'
  publisher: Cureus
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9674040/
  source_type: journal_article
  audience: clinician
  publication_date: '2022'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC9674040). Licence: CC BY'
- id: S4
  title: 'Clinical and electrophysiological evaluation of carpal tunnel syndrome: approach and pitfalls'
  publisher: Neurosciences
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5946360/
  source_type: journal_article
  audience: clinician
  publication_date: '2017'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC5946360). Licence: CC BY'
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
  - No patient-level page about EMG itself was available in the candidates or local dataset (the MedlinePlus
    EMG and nerve conduction test page is not in the dataset). S1 (NIAMS) mentions EMG in one line only.
    Consider adding the MedlinePlus EMG test page to give a plain-language description of what the test
    feels like and how to prepare.
  - S2 (BMJ, 'The basics of electromyography') is link_and_paraphrase and only its abstract is in the
    pack. Check that no sentence is copied from it.
  - S4 is listed as open_license (CC BY), but the dataset licence text says the journal uses CC BY-NC
    (non-commercial). Check the licence before any commercial reuse.
  - S4 pack text is cut off before the article's detailed EMG section, so EMG findings in carpal tunnel
    syndrome are only covered in general terms. A clinician should check the plain-language wording.
  - The numbers for accuracy (S3) are for EMG and nerve conduction studies combined, not EMG alone.
  - MeSH ID is unknown ('<verify>'); ICD-10-CM does not usually apply to a test.
  - The vocab has no DiagnosticTest -> Condition predicate. A DIAGNOSED_BY link to this KO should be added
    from the Carpal Tunnel Syndrome (KO-HAND-COND-001) KO.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- NIAMS updates its carpal tunnel syndrome page (diagnosis section).
- A new systematic review compares EMG, nerve conduction studies, and ultrasound for carpal tunnel syndrome.
- Any cited page shows a new 'last reviewed' date.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Electromyography (EMG) is a test that records the electrical activity in your muscles [S2]. Doctors think of it as an extension of the physical exam [S2]. In carpal tunnel syndrome (CTS), a condition where a nerve at the wrist called the median nerve is squeezed, EMG can show how badly the muscles have been harmed [S1]. It is often done together with a nerve conduction study, a test of how fast signals move along a nerve [S1][S3][S4].

## Key Facts (claim → source)
- EMG records electrical activity in muscle [S2].
- The recording is made with a thin, throw-away needle electrode (a small sensor) placed into the muscle [S2].
- A muscle at rest is normally silent on EMG [S2].
- In carpal tunnel syndrome, EMG can show how severe the muscle damage is [S1].
- EMG and nerve conduction studies together are called electrodiagnostic (EDX) studies [S3][S4].
- In CTS, EMG is mainly used to rule out other problems, such as nerve root or nerve network problems higher up the arm [S3].
- Doctors may order these tests when a physical exam alone cannot confirm CTS [S1].
- Correct reading of the results takes training and experience [S4].

## Explanation
### What it checks
EMG looks at the electrical signals inside muscles [S2]. It can help tell whether weakness or muscle wasting (shrinking) comes from a muscle problem or from a nerve problem [S2]. It can find nerve damage in a muscle that still seems normal on the exam [S2][S4]. By checking which muscles are affected, it can help show whether the problem is in one nerve, in the network of nerves near the shoulder (plexus), or in a nerve root near the spine [S2].

For carpal tunnel syndrome, EMG can show how much the muscles have been damaged [S1]. EDX studies help find the problem at the wrist, grade how severe it is, and rule out other conditions that look like CTS or happen at the same time [S4]. The diagnosis of CTS mostly depends on the nerve conduction study, and EMG is mainly used to exclude other conditions [S3].

### How it is done
- A thin needle electrode is placed into the muscle being checked [S2].
- The needle picks up signals from a very small area of muscle around its tip [S2].
- The doctor watches the signals on a screen and also listens to them through a loudspeaker [S2].
- The muscle is checked while it is relaxed, because a relaxed muscle should be silent [S2].
- Many people find it hard to relax a muscle fully, and the doctor can tell this apart from abnormal signals [S2].
- EMG is usually done as part of electrodiagnostic testing, together with a nerve conduction study [S3][S4].

### What results can mean
- Signals in a resting muscle that should be quiet can point to a problem [S2].
- EMG can give clues about whether a nerve's inner core (axon) or its outer coating is damaged [S2].
- In CTS, results help show how severe the condition is [S1][S4].
- Results can point to a different cause of hand symptoms, such as a pinched nerve root in the neck or a wider nerve disease [S3][S4].
- The doctor reads the results together with your symptoms and exam, because CTS is diagnosed from the history and symptoms and then confirmed by testing [S3].

### Limits
- EMG is not usually the main test for CTS; the nerve conduction study is [S3].
- Mistakes in how the test is done or read can lead to a wrong diagnosis [S4].
- In a review of studies, EMG and nerve conduction studies together found about 89 of 100 true cases of CTS, but they also sometimes flagged CTS in people who did not have it [S3].
- Ultrasound, an imaging test, is more comfortable and did about as well in that review, but it is not yet ready to replace EMG and nerve conduction studies [S3].
- Weakness in the hand without any change in feeling is not typical of CTS, so other causes should be checked [S4].

## Common Misunderstandings
- **Myth:** EMG and a nerve conduction study are the same test. **Fact:** EMG records signals inside the muscle with a needle, while a nerve conduction study measures how fast signals travel along a nerve [S1][S2].
- **Myth:** EMG is the main test for carpal tunnel syndrome. **Fact:** The diagnosis mostly depends on the nerve conduction study; EMG is mainly used to rule out other problems [S3].
- **Myth:** A muscle that looks and feels normal cannot be damaged. **Fact:** EMG can find nerve damage in muscles that seem normal on the exam [S2].
- **Myth:** Test results alone decide the diagnosis. **Fact:** CTS is diagnosed from your history and symptoms, and EDX tests help confirm it [S3][S4].

## Questions to Ask Your Doctor
1. Why do I need an EMG, and what are you looking for?
2. Will I have a nerve conduction study at the same visit?
3. Which muscles will be tested?
4. What should I tell you before the test about my health or medicines?
5. Who will explain my results, and when?
6. How could the results change my treatment plan?

## Test Questions
1. What does EMG record? - The electrical activity in muscle [S2].
2. What is used to make the recording? - A thin needle electrode placed in the muscle [S2].
3. How should a healthy muscle at rest look on EMG? - It should be silent [S2].
4. In carpal tunnel syndrome, what can EMG show? - How severe the muscle damage is [S1].
5. What is EMG mainly used for in CTS? - To rule out other conditions, such as nerve root problems [S3].
6. What are EMG and nerve conduction studies called together? - Electrodiagnostic (EDX) studies [S4].

## Related Topics
- Compared with: Nerve Conduction Study (KO-HAND-DX-001), the nerve test usually done with EMG
- Compared with: Nerve Ultrasound (KO-HAND-DX-005), an imaging test for the median nerve
- Read next: Carpal Tunnel Release (KO-HAND-PROC-001)
- Used to diagnose (link to be added from the condition KO): Carpal Tunnel Syndrome (KO-HAND-COND-001)

## References
1. [S1] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Carpal Tunnel Syndrome.* https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome (retrieved 2026-10-26)
2. [S2] BMJ. *The basics of electromyography.* https://doi.org/10.1136/jnnp.2005.069211 (retrieved 2026-11-14)
3. [S3] Cureus. *A Comparative Analysis Between Ultrasound and Electromyographic and Nerve Conduction Studies in Diagnosing Carpal Tunnel Syndrome (CTS): A Systematic Review and Meta-Analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC9674040/ (retrieved 2026-10-26)
4. [S4] Neurosciences. *Clinical and electrophysiological evaluation of carpal tunnel syndrome: approach and pitfalls.* https://pmc.ncbi.nlm.nih.gov/articles/PMC5946360/ (retrieved 2026-10-26)
