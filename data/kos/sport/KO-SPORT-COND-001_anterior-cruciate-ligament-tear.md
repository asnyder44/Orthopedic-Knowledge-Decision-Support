---
schema_version: okds-ko-1.0
ko_id: KO-SPORT-COND-001
title: Anterior Cruciate Ligament Tear
preferred_term: Anterior Cruciate Ligament Tear
alternate_terms:
- ACL tear
- ACL injury
- ACL rupture
ko_type: Condition
specialty: SPORT
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: An anterior cruciate ligament (ACL) tear is an injury to a strong band of tissue inside the
  knee that keeps the shinbone from sliding too far forward or twisting [S1][S2]. It usually happens
  during a sudden twist, a quick change of direction, or a jump landing in sports [S1][S2]. Treatment
  can be structured rehab exercise alone or surgery called ACL reconstruction, chosen together by the
  patient and the care team [S2].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- knee injury
- sports injury
- ligament tear
- knee instability
- giving way
- ACL reconstruction
- injury prevention
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-SPORT-PROC-001
  target_label: ACL Reconstruction
  source_ids:
  - S2
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-SPORT-COND-002
  target_label: Meniscus Tear
  source_ids:
  - S2
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-JOINT-COND-001
  target_label: Knee Osteoarthritis
  source_ids:
  - S1
  - S3
proposed_concepts:
- term: Anterior cruciate ligament (ACL)
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S2 and S3 describe the ACL as the main knee stabilizer; an anatomy KO is needed for an AFFECTS
    link.
- term: Lachman test
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S4 reports the accuracy of the Lachman test for ACL tears.
- term: Pivot shift test
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S4 names the pivot shift as one of the best exam tests for ruling in an ACL tear.
- term: Anterior drawer test and Lever sign test
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S4 reports the accuracy of both exam tests for ACL tears.
- term: Rehabilitation after ACL injury (non-operative and post-operative)
  suggested_type: RehabProtocol
  predicate: PREREQUISITE_FOR
  reason: S2 describes staged, progressive rehabilitation as needed after both non-surgical and surgical
    treatment.
- term: Neuromuscular injury prevention training
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S5 found neuromuscular and balance training lowered ACL injury rates.
sources:
- id: S1
  title: Knee Injuries and Disorders
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/kneeinjuriesanddisorders.html
  source_type: government_health_page
  audience: patient
  publication_date: '2025-06-23'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:kneeinjuriesanddisorders). Licence: Public domain (NLM-authored
    MedlinePlus summary); credit MedlinePlus'
- id: S2
  title: 'Treatment after anterior cruciate ligament injury: Panther Symposium ACL Treatment Consensus
    Group'
  publisher: Knee Surgery, Sports Traumatology, Arthroscopy
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7524809/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC7524809). Licence: CC BY'
- id: S3
  title: The Relationship between Anterior Cruciate Ligament Injury and Osteoarthritis of the Knee
  publisher: Advances in Orthopedics
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4410751/
  source_type: journal_article
  audience: clinician
  publication_date: '2015'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC4410751). Licence: CC BY'
- id: S4
  title: 'The diagnostic accuracy of clinical tests for anterior cruciate ligament tears are comparable
    but the Lachman test has been previously overestimated: a systematic review and meta-analysis'
  publisher: 'Knee surgery, sports traumatology, arthroscopy : official journal of the ESSKA'
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9464183/
  source_type: systematic_review
  audience: clinician
  publication_date: '2022'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: systematic review. Text kept: abstract only.'
- id: S5
  title: 'Effectiveness of Knee Injury and Anterior Cruciate Ligament Tear Prevention Programs: A Meta-Analysis'
  publisher: PloS one
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4670212/
  source_type: systematic_review
  audience: clinician
  publication_date: '2015'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc, plos. Licence: cc by. Type: systematic review. Text kept: abstract only.'
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
  - 'Source gap: no source in this pack lists the classic first symptoms of an ACL tear (for example a
    pop or fast swelling) or gives clear "when to seek care" advice. Symptoms are limited to pain, swelling,
    instability, and giving way from S1/S2. Add a patient page (for example NIAMS or MedlinePlus on ACL
    injuries) if one becomes available.'
  - 'Source gap: MRI is not described in this pack as a test for ACL tears; only exam tests (S4) are covered.'
  - MeSH ID and ICD-10-CM code are unknown and left as <verify>.
  - 'Clinician check: S3 figures (up to 80% of injured knees with X-ray signs of osteoarthritis at 5-15
    years) come from a 2015 review; confirm wording.'
  - 'Clinician check: incidence figure (about 85 per 100,000 people aged 16-39) is from S2; confirm.'
  - S4 and S5 are abstract-only in this pack.
  - Plain-language definitions of terms (for example "ligament", "shinbone") were written by the drafter;
    check they match the sources.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- Any cited page shows a new 'last reviewed' date.
- A new international consensus or guideline on operative vs. non-operative ACL treatment is published.
- MedlinePlus or NIAMS publishes a patient page specific to ACL injuries.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
An anterior cruciate ligament (ACL) tear is an injury to a strong band of tissue inside the knee that keeps the shinbone from sliding too far forward or twisting [S1][S2]. It usually happens during a sudden twist, a quick change of direction, or a jump landing in sports [S1][S2]. Treatment can be structured rehab exercise alone or surgery called ACL reconstruction, chosen together by the patient and the care team [S2].

## Key Facts (claim → source)
- The ACL is the main ligament that keeps the knee steady, and an ACL injury is a common sports injury [S1][S2].
- Most ACL tears happen without contact, during pivoting, cutting (sharp side-steps), or jumping [S2].
- A torn ACL rarely heals back into its normal place on its own [S3].
- ACL tears often come with damage to the menisci (the knee's cartilage cushions), other ligaments, or cartilage [S3].
- People who have had an ACL injury have a higher chance of knee osteoarthritis later, even after surgery [S3].
- Doctors use hands-on knee tests to check for an ACL tear, but no single test is perfect [S4].
- Very active people in jumping, cutting, and pivoting sports are often advised to have early ACL reconstruction, while people who return to straight-line activities may do well with rehab alone [S2].
- Training programs that work on muscle control and balance lowered the rate of ACL injuries in studies [S5].

## Explanation
### What it is
The knee joint is made of bone, cartilage, ligaments, and fluid, with muscles and tendons that help it move [S1]. The ACL is a ligament (a tough band of tissue) and is the main structure that stops the shinbone (tibia) from sliding forward and twisting inward under the thighbone [S2][S3]. When the ACL is torn, the knee can become unstable, meaning it may shift or "give way" [S2][S3]. A tear can be partial or complete [S4].

### Causes and risk factors
- A sudden twisting motion is the usual way the ACL gets hurt [S1].
- The most common way is a non-contact injury while pivoting, cutting, or jumping, with the knee slightly bent and turned inward [S2].
- People who often jump, pivot, or cut in sports have a higher chance of knee injuries, including ACL tears [S5].
- ACL tears are common in athletes and young people [S3]. One source puts the rate at about 85 per 100,000 people aged 16 to 39 each year [S2].

### Symptoms
Knee injuries like this can cause pain and trouble walking [S1]. After an ACL injury, swelling in the joint (effusion) and pain are common early problems [S2]. Some people feel the knee is unstable and have episodes of the knee "giving way," which can keep them from returning to their usual activities [S2]. Over time, a knee without a working ACL can wear down more and get hurt again more easily [S3].

### How it is diagnosed
A health care provider checks the knee with hands-on tests [S4]. Common ones are the anterior drawer test, the Lachman test, the pivot shift test, and the Lever sign test [S4]. A large review found these tests are similarly accurate overall [S4]. The pivot shift test was best for confirming a tear, and the Lever sign was best for ruling one out [S4]. The Lachman test was less accurate than once thought, especially for complete tears and for injuries that are not new [S4]. The sources in this pack do not describe imaging tests for ACL tears, so ask a clinician which tests are needed.

### Treatment options
Treatment is decided through shared decision-making, where the provider explains the options and the patient's goals and expectations are taken into account [S2].
- **Rehab without surgery:** Structured, step-by-step physical therapy is an acceptable option for people who want to return to straight-line activities [S2]. Rehab first works on swelling, pain, motion, and thigh muscle strength, then on balance and knee control, and finally on strength and sport skills [S2].
- **ACL reconstruction surgery:** For very active people in jumping, cutting, and pivoting sports, early reconstruction is advised because delaying surgery raises the risk of more meniscus and cartilage damage [S2]. A period of rehab before surgery is still recommended [S2]. If the knee keeps feeling unstable or gives way after rehab, reconstruction is advised [S2].
- **Bracing:** Functional braces have not been clearly shown to lower ACL strain or injury risk [S2].

Surgery has not been shown to bring the risk of later knee osteoarthritis back down to normal [S3]. Keeping a healthy weight, avoiding too much load on the knee, and strength training are ways to help lower osteoarthritis risk, with or without surgery [S3].

### When to seek care
The sources in this pack do not give specific warning signs for when to see a clinician after a knee injury, so ask a health care provider for advice. They do show why a check-up matters: an ACL tear rarely heals in place on its own, and a knee that keeps giving way can lead to more damage to the menisci and cartilage [S2][S3].

## Common Misunderstandings
- **Myth:** A torn ACL will heal back to normal by itself. **Fact:** A torn ACL rarely heals back into its normal position [S3].
- **Myth:** Everyone with an ACL tear needs surgery. **Fact:** For people returning to straight-line activities, structured rehab without surgery is an acceptable option [S2].
- **Myth:** ACL surgery prevents arthritis later. **Fact:** Reconstruction has not been shown to lower the risk of knee osteoarthritis back to normal [S3].
- **Myth:** Wearing a knee brace will stop an ACL injury. **Fact:** Evidence that functional braces lower ACL injury risk is still limited [S2].
- **Myth:** Nothing can be done to prevent ACL tears. **Fact:** Muscle control and balance training programs lowered ACL injury rates in studies [S5].

## Questions to Ask Your Doctor
1. Which tests do I need to check whether my ACL is torn, and is anything else in my knee hurt?
2. Is rehab without surgery a good fit for my activities, or would reconstruction suit my goals better?
3. What would rehab involve, and how long might it take?
4. If my knee keeps giving way, what should I do?
5. What can I do to protect my knee from arthritis in the future?
6. Are there training programs that can lower my chance of another knee injury?

## Test Questions
1. What does the ACL do? - It keeps the shinbone from sliding forward and twisting under the thighbone, which keeps the knee stable [S2][S3].
2. How do most ACL tears happen? - Without contact, during pivoting, cutting, or jumping, often with a sudden twist [S1][S2].
3. Which exam test was best for ruling in an ACL tear in one large review? - The pivot shift test [S4].
4. Who may do well with rehab instead of surgery? - People who want to return to straight-line activities [S2].
5. What long-term knee problem is more likely after an ACL injury? - Knee osteoarthritis [S3].
6. What kind of training lowered ACL injury rates in studies? - Neuromuscular and balance (proprioceptive) training [S5].

## Related Topics
- Read next: ACL Reconstruction (KO-SPORT-PROC-001)
- Read next: Meniscus Tear (KO-SPORT-COND-002)
- Read next: Knee Osteoarthritis (KO-JOINT-COND-001)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Knee Injuries and Disorders.* https://medlineplus.gov/kneeinjuriesanddisorders.html (retrieved 2026-10-26)
2. [S2] Knee Surgery, Sports Traumatology, Arthroscopy. *Treatment after anterior cruciate ligament injury: Panther Symposium ACL Treatment Consensus Group.* https://pmc.ncbi.nlm.nih.gov/articles/PMC7524809/ (retrieved 2026-10-26)
3. [S3] Advances in Orthopedics. *The Relationship between Anterior Cruciate Ligament Injury and Osteoarthritis of the Knee.* https://pmc.ncbi.nlm.nih.gov/articles/PMC4410751/ (retrieved 2026-10-26)
4. [S4] Knee surgery, sports traumatology, arthroscopy : official journal of the ESSKA. *The diagnostic accuracy of clinical tests for anterior cruciate ligament tears are comparable but the Lachman test has been previously overestimated: a systematic review and meta-analysis.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9464183/ (retrieved 2026-11-14)
5. [S5] PloS one. *Effectiveness of Knee Injury and Anterior Cruciate Ligament Tear Prevention Programs: A Meta-Analysis.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4670212/ (retrieved 2026-11-14)
