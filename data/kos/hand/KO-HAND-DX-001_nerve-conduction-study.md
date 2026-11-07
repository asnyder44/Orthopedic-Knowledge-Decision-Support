---
schema_version: okds-ko-1.0
ko_id: KO-HAND-DX-001
title: Nerve Conduction Study
preferred_term: Nerve Conduction Study
alternate_terms:
- NCS
- electrodiagnostic testing
- nerve conduction velocity
- NCV
- electrodiagnostic study
- EDX
ko_type: DiagnosticTest
specialty: HAND
cluster: 3
audience:
- patient
- caregiver
- student
reading_level: grade 6-8
difficulty: beginner
summary: A nerve conduction study (NCS) is a test that measures how fast and how well electrical signals
  travel along a nerve; a damaged nerve sends a slower, weaker signal [S1]. Doctors use it to look for
  nerve damage and to find where a nerve is being squeezed, such as at the wrist or elbow [S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- nerve test
- electrodiagnostic test
- EMG
- nerve damage
- numbness
- tingling
- carpal tunnel
- pinched nerve
relationships:
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-DX-002
  target_label: Phalen's Test
  source_ids:
  - S2
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-PROC-001
  target_label: Carpal Tunnel Release
  source_ids:
  - S2
  - S3
proposed_concepts:
- term: Electromyography (EMG)
  suggested_type: DiagnosticTest
  predicate: CONTRASTS_WITH
  reason: Muscle test usually done at the same visit as an NCS; often confused with it [S1][S3].
- term: Nerve Ultrasound
  suggested_type: DiagnosticTest
  predicate: CONTRASTS_WITH
  reason: Painless imaging test used with or instead of nerve tests in some cases [S2][S3].
sources:
- id: S1
  title: Electromyography (EMG) and Nerve Conduction Studies
  publisher: MedlinePlus Medical Tests (National Library of Medicine)
  url: https://medlineplus.gov/lab-tests/electromyography-emg-and-nerve-conduction-studies/
  source_type: government_health_page
  audience: patient
  publication_date: '2024-04-10'
  retrieved_date: '2026-11-01'
  permitted_use: public_domain
  notes: US government text. Date is the 'last updated' date listed in docs/ko-starter-sources.md (the
    fetched text did not include it). Reference list removed from the pack.
- id: S2
  title: 'Electrodiagnostic Studies in the Surgical Treatment of Carpal Tunnel Syndrome: A Systematic
    Review'
  publisher: Journal of Clinical Medicine, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8235020/
  source_type: systematic_review
  audience: clinician
  publication_date: '2021-06-18'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: Osiak K, et al. CC BY 4.0. Pack keeps the abstract, introduction (incl. testing technique), discussion,
    and conclusions. Accepted 2021-06-17.
- id: S3
  title: Electrodiagnostic Testing
  publisher: AAOS OrthoInfo
  url: https://www.orthoinfo.org/en/treatment/electrodiagnostic-testing/
  source_type: patient_education
  audience: patient
  publication_date: <verify>
  retrieved_date: '2026-11-01'
  permitted_use: link_and_paraphrase
  notes: Copyrighted. Paraphrased only. No review date shown on the page. Pack text is for internal review
    only; do not publish the pack.
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
  - S2 is a clinician-level systematic review. A clinician should check the plain-language rewrites of
    its findings (test accuracy, link between test severity and surgery outcome, AAOS guideline statement
    as reported by S2).
  - The AAOS guideline statement ('helpful but not required') is reported second-hand through S2; check
    it against the current AAOS carpal tunnel guideline before publishing.
  - S3 (AAOS OrthoInfo) is copyrighted (link_and_paraphrase). Its trimmed text is stored in the source
    pack for review only; do not publish the pack. Check that no sentence is copied from S3.
  - S3 shows no review date, so publication_date is '<verify>'. S1 date (2024-04-10) comes from the sources
    doc, not the fetched text.
  - MeSH ID is unknown ('<verify>'); ICD-10-CM does not usually apply to a test (consider a CPT/LOINC
    field later).
  - The vocab has no DiagnosticTest -> Condition predicate. The DIAGNOSED_BY links should be added from
    the Carpal Tunnel Syndrome (KO-HAND-COND-001) and Cubital Tunnel Syndrome (KO-HAND-COND-002) KOs.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-01'
last_updated: '2026-11-01'
update_triggers:
- MedlinePlus updates its EMG and nerve conduction studies test page.
- AAOS updates its carpal tunnel syndrome guideline advice on whether nerve testing is needed.
- Any cited page shows a new 'last reviewed' date.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-01'
  by: OKDS agent (Claude)
  change: Initial AI draft written by the agent from source pack SP-KO-HAND-DX-001 (claude-opus-5-5, okds-gen-1.0).
---

## Summary
A nerve conduction study (NCS) checks how fast and how well electrical signals move along your nerves [S1]. Nerves carry messages between the brain and the body, and a damaged nerve sends a slower and weaker signal [S1][S3]. Doctors use the test to look for nerve damage and to find the exact spot where a nerve is being squeezed, such as at the wrist or elbow [S3]. It is usually done at the same visit as electromyography (EMG), a test of the muscles [S1].

## Key Facts (claim → source)
- An NCS measures the speed and strength of signals along a nerve; a damaged nerve gives a slower, weaker signal [S1].
- Other names include electrodiagnostic study and nerve conduction velocity (NCV) [S1].
- Patches called electrodes are stuck on the skin; some give a mild electric pulse and others record the response [S1].
- The pulse may feel like a mild tingle or a small static shock [S1][S3].
- The test takes from 15 minutes to over an hour, depending on how many nerves are checked [S1].
- Testing the nerve at several places helps the doctor find the exact spot of the problem [S3].
- In carpal tunnel syndrome, the test shows slowed signals in the median nerve across the wrist, with normal signals elsewhere [S2].
- The test supports a diagnosis but cannot make it alone, and it cannot measure pain [S2][S3].

## Explanation
### What it checks
Sensory nerves carry information about touch and your surroundings to the brain, and motor nerves carry signals from the brain to the muscles [S3]. Injuries or diseases can slow or stop these signals [S3]. An NCS measures how quickly and how well the signals travel [S1]. You may need it if you have muscle weakness, cramps, or twitching, or numbness or tingling in your arms, legs, hands, feet, or face [S1].

Orthopedic doctors often order the test for compressive neuropathies, which are nerve problems caused by pressure on a nerve, especially in the arm, elbow, or wrist [S3]. Examples are carpal tunnel syndrome (pressure on the median nerve at the wrist) and ulnar nerve entrapment (pressure on the ulnar nerve behind the elbow) [S3]. The test can also show how badly a nerve was hurt in an accident, study the effects of diseases such as diabetes, and show whether an injured nerve is healing [S3].

### How it is done
- You sit or lie on a table or bed [S1].
- The provider sticks "stimulating" electrodes on the skin over the nerve; they give a mild electrical pulse [S1].
- "Recording" electrodes go on the muscles that nerve controls, to record how the muscle responds [S1].
- The provider notes how long the muscle takes to respond; this speed is called the conduction velocity [S1].
- A neurologist (nerve doctor) or a physiatrist (rehabilitation doctor) usually does the test [S3].
- If you are also having an EMG, the NCS is done first [S1]. For the EMG, a thin needle electrode is placed in a muscle to record its electrical activity [S1].

Before the test, tell your provider if you have a pacemaker or heart defibrillator, or if you take blood thinners [S1]. Wear loose clothes, keep your skin clean, and skip lotions, creams, and perfume for a day or two before, because they can change the results [S1].

### What results can mean
Results that are not normal can be a sign of many conditions, depending on which nerves or muscles are affected [S1]. Examples include carpal tunnel syndrome, a herniated (bulging) disk in the spine, and some rare nerve and muscle diseases [S1]. Your provider reads the results together with your symptoms, health history, and other tests [S1].

For carpal tunnel syndrome, comparing the median nerve with a nearby nerve that does not pass through the carpal tunnel is one of the most accurate ways to do the test [S2]. The results can also grade how severe the nerve damage is [S2]. In research, people with the most severe results tended to do worst after carpal tunnel surgery, and people with moderate results did best, though not all studies agree [S2]. A test before surgery also gives a starting point to compare with if symptoms do not get better, and it can uncover another cause, such as a pinched nerve in the neck [S2].

### Limits
- The test cannot measure pain, and a person can still have symptoms when the nerves test normal [S3].
- In some conditions, changes may take several weeks to show up [S3].
- Accuracy depends on the skill of the tester and the quality of the equipment [S3].
- Age, sex, finger size, body weight, other diseases, and temperature can affect results and cause false results (showing a problem that is not there, or missing one) [S2].
- An abnormal result in a person with no symptoms does not mean they have carpal tunnel syndrome [S2].
- Doctors do not all agree that the test is needed before every carpal tunnel surgery; an AAOS guideline says it may help but is not required for diagnosis [S2].
- After successful surgery, results often improve but may not return fully to normal [S2].
- Risks are small: a tingly feeling during the NCS, and sore muscles or bruises for a few days after an EMG [S1].
- Ultrasound is a painless imaging test that can be used along with these tests [S3], but a review found it cannot replace them for confirming carpal tunnel syndrome [S2].

## Common Misunderstandings
- **Myth:** A nerve conduction study uses needles. **Fact:** The NCS uses patches on the skin; the needle belongs to the EMG, which is often done at the same visit [S1].
- **Myth:** The electric pulse is dangerous or very painful. **Fact:** Most people are quite comfortable; it feels like the small shock from touching a doorknob [S3].
- **Myth:** A normal result means nothing is wrong. **Fact:** People can still have pain or symptoms when the nerves test normal [S3].
- **Myth:** The test alone decides whether you have carpal tunnel syndrome. **Fact:** It supports the diagnosis, but doctors also use your symptoms and exam [S1][S2].

## Questions to Ask Your Doctor
1. Why do I need this test, and what are you looking for?
2. Will I have an EMG at the same visit?
3. What should I tell you about my medicines or devices before the test?
4. When will I get the results, and who will explain them?
5. How could the results change my treatment plan?
6. What happens if my results are normal but I still have symptoms?

## Test Questions
1. What does a nerve conduction study measure? - How fast and how well electrical signals travel along a nerve [S1].
2. What happens to the signal in a damaged nerve? - It becomes slower and weaker [S1].
3. If you have both an NCS and an EMG, which is done first? - The nerve conduction study [S1].
4. Why should you avoid lotions and creams before the test? - They can change the test results [S1].
5. Can a nerve conduction study measure pain? - No; a person can have pain even when the test is normal [S3].
6. In carpal tunnel syndrome, where does the test show slowed signals? - In the median nerve across the wrist [S2].

## Related Topics
- Compared with: Phalen's Test (KO-HAND-DX-002), a quick exam test for carpal tunnel syndrome
- Read next: Carpal Tunnel Release (KO-HAND-PROC-001)
- Used to diagnose: Carpal Tunnel Syndrome (KO-HAND-COND-001) and Cubital Tunnel Syndrome (KO-HAND-COND-002)
- Proposed topics (not in the registry yet): Electromyography (EMG); Nerve Ultrasound

## References
1. [S1] MedlinePlus Medical Tests (National Library of Medicine). *Electromyography (EMG) and Nerve Conduction Studies.* https://medlineplus.gov/lab-tests/electromyography-emg-and-nerve-conduction-studies/ (retrieved 2026-11-01)
2. [S2] Journal of Clinical Medicine, via PubMed Central. *Electrodiagnostic Studies in the Surgical Treatment of Carpal Tunnel Syndrome: A Systematic Review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC8235020/ (retrieved 2026-11-01)
3. [S3] AAOS OrthoInfo. *Electrodiagnostic Testing.* https://www.orthoinfo.org/en/treatment/electrodiagnostic-testing/ (retrieved 2026-11-01)
