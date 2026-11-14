---
schema_version: okds-ko-1.0
ko_id: KO-SPORT-COND-003
title: Rotator Cuff Tear
preferred_term: Rotator Cuff Tear
alternate_terms:
- torn rotator cuff
- rotator cuff injury
- RCT (rotator cuff tear)
- partial-thickness rotator cuff tear
- full-thickness rotator cuff tear
ko_type: Condition
specialty: SPORT
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: A rotator cuff tear is a tear in one of the tendons of the rotator cuff, the group of four muscles
  and tendons that holds the upper arm bone in the shoulder socket and keeps the shoulder stable [S1][S2].
  Tears may come from wear and tear with age and repeated overhead use, or suddenly from an injury such
  as a fall [S1][S2]. Treatment may include rest, physical therapy, a steroid shot, or surgery, depending
  on the tear and the person [S1][S2].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- shoulder pain
- shoulder injury
- tendon tear
- overhead activity
- night pain
- physical therapy
- shoulder surgery
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-TRT-002
  target_label: Corticosteroid Injection
  source_ids:
  - S1
  - S2
  - S5
proposed_concepts:
- term: Rotator cuff
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S1 and S2 describe the rotator cuff muscles and tendons; an anatomy KO is needed for an AFFECTS
    link.
- term: Supraspinatus test
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S3 found it had the best diagnostic odds for full-thickness rotator cuff tears among shoulder
    exam tests.
- term: Shoulder MRI or ultrasound
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S1 lists x-rays, ultrasound, and MRI as imaging tests for rotator cuff injuries.
- term: Rotator cuff repair
  suggested_type: Procedure
  predicate: PREREQUISITE_FOR
  reason: S1 and S2 describe surgery as an option for large, recent, or long-lasting tears.
- term: Physical therapy for rotator cuff tears
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S1, S2, and S5 describe physical therapy as a main non-surgical treatment.
- term: DASH questionnaire (Disabilities of the Arm, Shoulder and Hand)
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: S5 used DASH scores to measure function in rotator cuff tears.
- term: Shoulder impingement / rotator cuff tendinitis and bursitis
  suggested_type: Condition
  predicate: CONTRASTS_WITH
  reason: S1 lists tendinitis and bursitis as other rotator cuff injuries that differ from tears.
sources:
- id: S1
  title: Rotator Cuff Injuries
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/rotatorcuffinjuries.html
  source_type: government_health_page
  audience: patient
  publication_date: '2024-01-08'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:rotatorcuffinjuries). Licence: Public domain (NLM-authored
    MedlinePlus summary); credit MedlinePlus'
- id: S2
  title: 'A Narrative Review of Rotator Cuff Tear Management: Surgery Versus Conservative Treatment'
  publisher: Cureus
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11692865/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC11692865). Licence: CC BY'
- id: S3
  title: 'Physical examination tests of the shoulder: a systematic review and meta-analysis of diagnostic
    test performance'
  publisher: BMC musculoskeletal disorders
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5267375/
  source_type: systematic_review
  audience: clinician
  publication_date: '2017'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: systematic review. Text kept: abstract only.'
- id: S4
  title: Association of rotator cuff injuries with night pain and sleep quality. A systematic review
  publisher: Zenodo
  url: https://zenodo.org/records/10652622
  source_type: systematic_review
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via zenodo. Licence: cc-by-4.0. Type: systematic review. Text kept: abstract only.'
- id: S5
  title: 'Comparison of the Separate and Combined Effects of Physiotherapy Treatment and Corticosteroid
    Injection on the Range of Motion and Pain in Nontraumatic Rotator Cuff Tear: A Randomized Controlled
    Trial'
  publisher: Advances in Orthopedics
  url: https://zenodo.org/records/6048821
  source_type: journal_article
  audience: clinician
  publication_date: '2021'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via zenodo. Licence: cc-by-4.0. Type: trial. Text kept: abstract only.'
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
  - 'Link check: the only registry link is PREREQUISITE_FOR Corticosteroid Injection (KO-HAND-TRT-002),
    a HAND-specialty KO. Confirm it is written generally enough to cover shoulder injections; otherwise
    remove the link. No shoulder anatomy, test, or procedure KOs exist in the registry yet (see proposed_concepts).'
  - 'Source quality: S4 is a systematic review posted on Zenodo with no named journal; S5 (Advances in
    Orthopedics) is a single small RCT. Both are abstract-only. Consider replacing S4 with a peer-reviewed
    journal source.'
  - 'Clinician check: prevalence figures (about 30% in their 60s, over 60% over age 80) are from S2; S1
    says most adults have tears by age 80. Confirm wording.'
  - MeSH ID and ICD-10-CM code are unknown and left as <verify>.
  - S5 names specific medicines and doses; these were deliberately left out of the KO.
  - Plain-language definitions (tendon, bursa) were written partly by the drafter from S1; check them.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- Any cited page shows a new 'last reviewed' date.
- AAOS or another society publishes or updates a rotator cuff tear clinical practice guideline.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
A rotator cuff tear is a tear in one of the tendons of the rotator cuff, the group of four muscles and tendons that holds the upper arm bone in the shoulder socket and keeps the shoulder stable [S1][S2]. Tears may come from wear and tear with age and repeated overhead use, or suddenly from an injury such as a fall [S1][S2]. Treatment may include rest, physical therapy, a steroid shot, or surgery, depending on the tear and the person [S1][S2].

## Key Facts (claim → source)
- The rotator cuff is a group of four muscles and their tendons that keeps the shoulder stable and helps the arm move [S1][S2].
- A tear can go partway through a tendon (partial tear) or all the way through (full tear) [S1].
- Most rotator cuff injuries come from wear and tear, and tears become more common with age [S1][S2].
- Many tears cause no symptoms, especially in older adults [S1][S2].
- When there is pain, it is often in the upper arm or shoulder and can be worse when lying on that side or lifting the arm [S1].
- Night pain is very common, and in one review it affected about 9 in 10 people with rotator cuff injuries [S4].
- Diagnosis uses a shoulder exam, strength tests, and sometimes x-rays, ultrasound, or MRI [S1].
- Non-surgical care can work well, especially for small and medium tears, while surgery may be an option for large, recent, or long-lasting tears [S1][S2].

## Explanation
### What it is
The rotator cuff is part of the shoulder joint [S1]. It is a group of muscles and tendons that holds the top of the upper arm bone firmly in the shoulder socket and keeps the shoulder stable when the arm moves [S1]. Tendons are the cords that connect muscles to bones [S1]. A rotator cuff tear is a tear in one of these tendons [S1]. A partial tear goes partway through the tendon, and a full tear goes all the way through [S1]. Rotator cuff injuries range from tendon irritation to partial and full tears, and in some cases to a form of shoulder arthritis called cuff tear arthropathy [S2].

### Causes and risk factors
Tears can happen slowly over time or suddenly from an injury, such as falling on an outstretched arm or lifting something heavy [S1][S2]. Most rotator cuff injuries come from wear and tear from doing the same arm movements again and again, especially reaching overhead [S1]. People who are more likely to have a rotator cuff injury include [S1]:
- People over age 40, since most of these injuries come from aging [S1].
- Athletes in sports with repeated shoulder movements, such as tennis, swimming, and baseball pitching [S1].
- Workers who reach overhead or lift heavy things a lot, such as carpenters, construction workers, and painters [S1].

Tears become more common with age, affecting about 30% of people in their 60s and more than 60% of people over 80 [S2].

### Symptoms
Rotator cuff injuries do not always cause pain [S1]. When they do, the pain is often in the top of the arm or the shoulder [S1]. Pain may be worse when [S1]:
- Lying down, especially on the hurt shoulder.
- Lifting the arm or lowering it to the front or side.
- Reaching behind the back.

A torn rotator cuff may also cause loss of arm strength and clicking or popping sounds when the arm moves [S1]. Tears can limit how far the shoulder moves [S2]. Night pain and poor sleep are very common with rotator cuff injuries, and sleep problems are linked to both pain and how well the shoulder works [S4].

### How it is diagnosed
A health care provider examines the shoulder, checks how far it moves and where it hurts, and tests arm and shoulder strength [S1]. The provider may order imaging tests such as x-rays, ultrasound, or an MRI scan [S1]. Many hands-on shoulder tests exist, but a large review found that no single test works very well on its own [S3]. Among the tests studied, the supraspinatus test did best for finding full-thickness tears [S3].

### Treatment options
The best treatment depends on age, how much the injury bothers the person, the size of the tear, activity level, overall health, and whether the injury was sudden or from wear and tear [S1][S2].
- **First steps:** Rest, ice or a cold pack, and pain relievers to ease pain and swelling are often used [S1].
- **Physical therapy:** Exercises to strengthen the shoulder and improve movement are a common treatment [S1][S2].
- **Steroid shot:** A corticosteroid injection into the shoulder may be used if other treatments do not ease the pain [S1]. In one small trial, people who had both physical therapy and a steroid shot had less pain and better function than those who had only one of them [S5].
- **Other treatments:** Heat or electrical nerve and muscle stimulation (TENS) may also be used for a torn rotator cuff [S1].
- **Surgery:** Surgery may be suggested if the tear is large, comes from a recent injury, or if symptoms last 6 to 12 months [S1]. Surgery often gives better function and pain relief, while non-surgical care can also work, especially for smaller tears [S2]. After surgical repair, studies found night pain eased and sleep got better [S4].

### When to seek care
If certain activities bother the shoulder, it is best to stop doing them and check with a health care provider, because early treatment can keep mild injuries from getting worse [S1]. If the arm feels weak right after a sudden shoulder injury, see a provider as soon as possible [S1].

## Common Misunderstandings
- **Myth:** A rotator cuff tear always hurts. **Fact:** Many tears cause no pain, especially in older adults [S1][S2].
- **Myth:** Only athletes tear their rotator cuff. **Fact:** Most rotator cuff injuries come from wear and tear with age, and workers who reach overhead are also at risk [S1].
- **Myth:** Every rotator cuff tear needs surgery. **Fact:** Non-surgical care such as physical therapy and steroid shots can work, especially for small and medium tears [S2].
- **Myth:** One quick shoulder test can confirm a tear. **Fact:** No single shoulder exam test performed very well on its own in a large review [S3].

## Questions to Ask Your Doctor
1. Is my shoulder problem a tear, or could it be tendinitis or bursitis?
2. Do I need an x-ray, ultrasound, or MRI?
3. Is my tear partial or full, and how big is it?
4. What exercises or physical therapy would help me?
5. When would surgery make sense for me?
6. What can I do about shoulder pain that wakes me up at night?

## Test Questions
1. What does the rotator cuff do? - It holds the upper arm bone in the shoulder socket and keeps the shoulder stable when the arm moves [S1].
2. What is the difference between a partial and a full tear? - A partial tear goes partway through the tendon; a full tear goes all the way through [S1].
3. Name two groups of people more likely to have a rotator cuff injury. - Examples: people over 40, athletes in overhead sports, or workers who reach overhead or lift heavy things [S1].
4. Which exam test did best for full-thickness tears in one review? - The supraspinatus test [S3].
5. How common is night pain with rotator cuff injuries? - Very common; about 9 in 10 people in one review [S4].
6. When might surgery be suggested? - When the tear is large, from a recent injury, or symptoms last 6 to 12 months [S1].

## Related Topics
- Read next: Corticosteroid Injection (KO-HAND-TRT-002)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Rotator Cuff Injuries.* https://medlineplus.gov/rotatorcuffinjuries.html (retrieved 2026-10-26)
2. [S2] Cureus. *A Narrative Review of Rotator Cuff Tear Management: Surgery Versus Conservative Treatment.* https://pmc.ncbi.nlm.nih.gov/articles/PMC11692865/ (retrieved 2026-10-26)
3. [S3] BMC musculoskeletal disorders. *Physical examination tests of the shoulder: a systematic review and meta-analysis of diagnostic test performance.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5267375/ (retrieved 2026-11-14)
4. [S4] Zenodo. *Association of rotator cuff injuries with night pain and sleep quality. A systematic review.* https://zenodo.org/records/10652622 (retrieved 2026-11-14)
5. [S5] Advances in Orthopedics. *Comparison of the Separate and Combined Effects of Physiotherapy Treatment and Corticosteroid Injection on the Range of Motion and Pain in Nontraumatic Rotator Cuff Tear: A Randomized Controlled Trial.* https://zenodo.org/records/6048821 (retrieved 2026-11-14)
