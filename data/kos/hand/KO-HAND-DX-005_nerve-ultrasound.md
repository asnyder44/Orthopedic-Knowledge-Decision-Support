---
schema_version: okds-ko-1.0
ko_id: KO-HAND-DX-005
title: Nerve Ultrasound
preferred_term: Nerve Ultrasound
alternate_terms:
- peripheral nerve ultrasound
- wrist ultrasound
- nerve ultrasonography
- high-resolution ultrasonography
- neuromuscular ultrasound
ko_type: DiagnosticTest
specialty: HAND
cluster: 3
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Nerve ultrasound uses sound waves to make live pictures of a nerve and the tissues around it
  [S2][S4]. In carpal tunnel syndrome it can show whether the median nerve is swollen at the wrist, and
  in studies it was about as accurate as nerve tests, though it does not yet replace them [S1][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- imaging test
- ultrasound
- median nerve
- carpal tunnel
- nerve injury
- nerve damage
relationships:
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-DX-001
  target_label: Nerve Conduction Study
  source_ids:
  - S1
  - S2
  - S3
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-DX-003
  target_label: Electromyography
  source_ids:
  - S1
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-PROC-001
  target_label: Carpal Tunnel Release
  source_ids:
  - S2
  - S3
proposed_concepts:
- term: Ultrasound elastography
  suggested_type: DiagnosticTest
  predicate: CONTRASTS_WITH
  reason: Newer ultrasound method that measures how stiff the nerve and nearby tissues are; mentioned
    as a recent advance for carpal tunnel syndrome [S2].
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
  title: Recent Advances in Ultrasound Diagnosis of Carpal Tunnel Syndrome
  publisher: Diagnostics
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7460039/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC7460039). Licence: CC BY'
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
  title: Nerve Ultrasound in Traumatic and Iatrogenic Peripheral Nerve Injury
  publisher: Diagnostics (Basel, Switzerland)
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7823340/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc, openaire. Licence: cc by. Type: review. Text kept: abstract only.'
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
  - S2 and S3 pack text holds only the abstract and introduction; the size cut-offs used to call a median
    nerve 'enlarged' are not in the pack, so no cut-off value is given here. Consider adding a source
    that states them.
  - Accuracy numbers (S3) are pooled from 12 non-randomized studies; a clinician should check the plain-language
    wording.
  - The PREREQUISITE_FOR link to Carpal Tunnel Release is a learning-path link (tests come before surgery);
    the sources do not say ultrasound is needed before surgery.
  - No patient-level page about nerve ultrasound itself was found; S1 (NIAMS) covers it in one line.
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
- A new systematic review compares ultrasound with nerve conduction studies for carpal tunnel syndrome.
- NIAMS updates the diagnosis section of its carpal tunnel syndrome page.
- Any cited page shows a new 'last reviewed' date.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Nerve ultrasound is an imaging test that uses sound waves to make live pictures of a nerve and the tissues around it [S2][S4]. In carpal tunnel syndrome (CTS), a condition where the median nerve is squeezed at the wrist, ultrasound can show whether the nerve is swollen [S1]. It is simple, quick, does not break the skin, and is low in cost [S2]. Studies found it about as accurate as nerve tests for CTS, but experts say it cannot fully replace them yet [S2][S3].

## Key Facts (claim → source)
- Ultrasound can show if the median nerve is swollen at the carpal tunnel [S1].
- The test only needs a small handheld probe (transducer) placed on the skin of the hand, so it is comfortable [S3].
- It shows the nerve and nearby tissues directly, which nerve tests cannot do [S3].
- In CTS, ultrasound may show a larger median nerve, a thicker ligament over the tunnel, and swelling around the finger tendons [S2].
- In one review, ultrasound found about 80 of 100 true CTS cases and correctly ruled it out in about 90 of 100 people without it [S3].
- Ultrasound can be an alternative test for CTS, but it cannot replace nerve conduction studies and electromyography yet [S3].
- After nerve injuries, ultrasound can show whether a nerve is still in one piece [S4].

## Explanation
### What it checks
Ultrasound looks at the shape and structure of a nerve [S4]. For CTS, it checks the median nerve inside the carpal tunnel, the narrow passage of bone and ligament at the base of the hand [S1]. Doctors look for a swollen median nerve near the start of the tunnel, thickening of the flexor retinaculum (the ligament that forms part of the tunnel), and swelling around the finger tendons [S1][S2]. Because the pictures are live, the doctor can also watch how the nerve and tendons move [S2].

After an injury, ultrasound can check whether a nerve is whole, whether a neuroma (a lump of scar and nerve tissue) has formed, and whether bone or a foreign object is pressing on the nerve [S4].

### How it is done
- A small handheld probe called a transducer is placed on the skin of the hand and wrist [S3].
- The probe sends sound waves and shows pictures on a screen in real time [S2].
- No needles or electric pulses are used, which makes it more comfortable than nerve tests [S2][S3].
- Before some procedures, ultrasound can be used to mark where a nerve runs, to help avoid injuring it [S4].

### What results can mean
- A swollen median nerve at the carpal tunnel fits with CTS [S1][S2].
- Results can be read together with your symptoms, exam, and nerve tests [S2][S3].
- In nerve injuries, ultrasound is very good at finding a problem at one spot along a nerve [S4].
- Ultrasound shows where the problem is and what the area looks like, while nerve tests show how well the nerve works [S3].

### Limits
- Ultrasound did a bit worse than nerve tests at finding every true case of CTS in one review [S3].
- Experts say more research is needed on unclear cases and CTS caused by another condition before ultrasound can replace nerve tests [S3].
- Nerve conduction studies and electromyography are still useful when the diagnosis is unclear or when another nerve problem may also be present [S2].
- Older studies did not all agree on whether ultrasound or nerve tests were more accurate [S3].

## Common Misunderstandings
- **Myth:** Ultrasound is only for pregnancy or the belly. **Fact:** High-resolution ultrasound can show nerves, tendons, and ligaments in the wrist [S2].
- **Myth:** Ultrasound has fully replaced nerve tests for carpal tunnel syndrome. **Fact:** It can be an alternative, but it cannot replace nerve conduction studies and electromyography yet [S3].
- **Myth:** A nerve ultrasound uses needles or shocks. **Fact:** It only uses a probe placed on the skin [S3].
- **Myth:** Ultrasound only helps with carpal tunnel syndrome. **Fact:** It is also used to check nerves after injuries and to mark nerves before procedures [S4].

## Questions to Ask Your Doctor
1. What are you hoping to see on my ultrasound?
2. Will I also need a nerve conduction study or EMG?
3. Who will do the ultrasound, and who will explain the pictures?
4. What does it mean if my nerve looks swollen?
5. How will the results change my treatment options?

## Test Questions
1. What does nerve ultrasound use to make pictures? - Sound waves, shown as live images [S2].
2. In CTS, what change in the median nerve can ultrasound show? - Swelling (enlargement) of the nerve at the carpal tunnel [S1][S2].
3. Why is ultrasound more comfortable than nerve tests? - Only a probe touches the skin of the hand [S3].
4. Can ultrasound replace nerve conduction studies for CTS today? - No; it can be an alternative but cannot replace them yet [S3].
5. After a nerve injury, what can ultrasound check? - Whether the nerve is still whole and if anything is pressing on it [S4].

## Related Topics
- Compared with: Nerve Conduction Study (KO-HAND-DX-001), a test of how well the nerve carries signals
- Compared with: Electromyography (KO-HAND-DX-003), a needle test of muscle activity
- Read next: Carpal Tunnel Release (KO-HAND-PROC-001)
- Used to diagnose (link to be added from the condition KO): Carpal Tunnel Syndrome (KO-HAND-COND-001)
- Proposed topic (not in the registry yet): Ultrasound elastography

## References
1. [S1] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Carpal Tunnel Syndrome.* https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome (retrieved 2026-10-26)
2. [S2] Diagnostics. *Recent Advances in Ultrasound Diagnosis of Carpal Tunnel Syndrome.* https://pmc.ncbi.nlm.nih.gov/articles/PMC7460039/ (retrieved 2026-10-26)
3. [S3] Cureus. *A Comparative Analysis Between Ultrasound and Electromyographic and Nerve Conduction Studies in Diagnosing Carpal Tunnel Syndrome (CTS): A Systematic Review and Meta-Analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC9674040/ (retrieved 2026-10-26)
4. [S4] Diagnostics (Basel, Switzerland). *Nerve Ultrasound in Traumatic and Iatrogenic Peripheral Nerve Injury.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7823340/ (retrieved 2026-11-14)
