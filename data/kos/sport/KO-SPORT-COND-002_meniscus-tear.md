---
schema_version: okds-ko-1.0
ko_id: KO-SPORT-COND-002
title: Meniscus Tear
preferred_term: Meniscus Tear
alternate_terms:
- meniscal tear
- torn meniscus
- meniscus injury
- meniscus lesion (degenerative)
ko_type: Condition
specialty: SPORT
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: A meniscus tear is a tear in one of the menisci, the cushion-like structures in the knee that share
  weight, absorb shock, and help keep the joint steady [S1]. Tears can come from a sudden knee injury
  (traumatic tear) or from slow wear over time (degenerative tear), and the two are treated differently
  [S2]. Treatment ranges from care without surgery to surgery that repairs or trims the meniscus [S1][S2].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- knee injury
- sports injury
- knee cartilage
- meniscus repair
- partial meniscectomy
- knee osteoarthritis
- MRI
relationships:
- predicate: COMPLICATION_OF
  target_id: KO-SPORT-COND-001
  target_label: Anterior Cruciate Ligament Tear
  source_ids:
  - S2
- predicate: PREREQUISITE_FOR
  target_id: KO-JOINT-COND-001
  target_label: Knee Osteoarthritis
  source_ids:
  - S1
  - S2
  - S3
proposed_concepts:
- term: Meniscus (knee)
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S1 describes the meniscus's role in load sharing, shock absorption, and stability; an anatomy
    KO is needed for an AFFECTS link.
- term: Knee MRI
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S1 says MRI is most likely used to confirm a tear; S2 discusses when MRI is advised.
- term: Arthroscopic partial meniscectomy
  suggested_type: Procedure
  predicate: PREREQUISITE_FOR
  reason: S1, S2, and S3 describe this common surgery and its long-term results.
- term: Meniscus repair
  suggested_type: Procedure
  predicate: PREREQUISITE_FOR
  reason: S1 and S2 recommend repair and preservation of the meniscus when possible.
- term: Lysholm knee score
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: S3 uses the Lysholm score (with WOMET) to measure knee symptoms and function.
sources:
- id: S1
  title: 'Meniscus Tear: Pathology, Incidence, and Management'
  publisher: Cureus
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9205760/
  source_type: journal_article
  audience: clinician
  publication_date: '2022'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC9205760). Licence: CC BY'
- id: S2
  title: 'Management of traumatic meniscus tears: the 2019 ESSKA meniscus consensus'
  publisher: Knee Surgery, Sports Traumatology, Arthroscopy
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7148286/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC7148286). Licence: CC BY'
- id: S3
  title: 'Arthroscopic partial meniscectomy for a degenerative meniscus tear: a 5 year follow-up of the
    placebo-surgery controlled FIDELITY (Finnish Degenerative Meniscus Lesion Study) trial'
  publisher: British journal of sports medicine
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7606577/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: trial. Text kept: abstract only.'
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
  - 'Source gap: no patient-level page (MedlinePlus or NIAMS) on meniscus tears was found in the dataset
    (the NIAMS Sports Injuries page mentions meniscal tears, but that part is cut from the pack). All three
    sources are clinician-level.'
  - 'Source gap: symptoms are thin in this pack (pain, knee dysfunction, mechanical symptoms). Classic
    symptoms such as locking, catching, or swelling are not described in plain terms. No "when to seek
    care" guidance is given; the section says to ask a clinician.'
  - 'Link check: COMPLICATION_OF ACL tear is based on S2 (meniscus tears found in 57-80% of people with
    a torn ACL). This is co-occurrence, not strictly a complication; confirm the predicate.'
  - 'Clinician check: S1 says repair is "recommended for all tears"; S2 and S3 add nuance (degenerative
    vs traumatic). Confirm the wording of the Treatment section.'
  - MeSH ID and ICD-10-CM code are unknown and left as <verify>.
  - S3 is abstract-only in this pack.
  - Plain-language definitions (meniscus, arthroscopy, osteoarthritis) were written by the drafter; check
    them.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- Any cited page shows a new 'last reviewed' date.
- ESSKA or another society updates its meniscus consensus (traumatic or degenerative tears).
- MedlinePlus or NIAMS publishes a patient page specific to meniscus tears.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
A meniscus tear is a tear in one of the menisci, the cushion-like structures in the knee that share weight, absorb shock, and help keep the joint steady [S1]. Tears can come from a sudden knee injury (traumatic tear) or from slow wear over time (degenerative tear), and the two are treated differently [S2]. Treatment ranges from care without surgery to surgery that repairs or trims the meniscus [S1][S2].

## Key Facts (claim → source)
- A meniscus tear is one of the most common sports-related injuries [S1].
- The menisci help share weight, keep the knee stable, absorb shock, and keep the joint moving smoothly [S1].
- A traumatic tear comes from a real knee injury with sudden pain, while a degenerative tear builds slowly without a clear injury [S2].
- Meniscus tears often happen together with ligament injuries, and are found in 57% to 80% of people with a torn ACL [S2].
- Diagnosis uses a health history, physical exam, special tests, and often an MRI scan [S1].
- Expert groups now say saving the meniscus (repair or leaving it in place) should come first when possible, because long-term results are worse after removing part of it [S1][S2].
- In a trial of people with degenerative tears, trimming the meniscus gave no better symptom relief than a placebo (fake) surgery after 5 years [S3].
- Losing the meniscus or having it injured raises the chance of knee osteoarthritis later [S1][S2].

## Explanation
### What it is
The menisci are structures in the knee that help carry body weight [S1]. They share load, keep the knee stable, absorb shock, and help lubricate the joint [S1]. A traumatic meniscus tear is linked to a real knee injury and sudden knee pain [S2]. A degenerative tear (also called a meniscus lesion) is wear of the tissue that gets worse slowly, without a recent injury [S2]. Tears come in different shapes, such as long vertical tears (including "bucket handle" tears), radial tears, and tears at the root where the meniscus attaches to bone [S2].

### Causes and risk factors
- **Sports:** Meniscus tears are among the most common sports injuries, and the number is rising as more people play sports [S1].
- **Other knee injuries:** Traumatic tears are commonly found together with ligament injuries, including ACL tears [S2].
- **Wear over time:** Degenerative tears come from repeated small injuries and tissue breakdown, sometimes with osteoarthritis [S2].

### Symptoms
A meniscus tear can cause knee pain and problems using the knee [S1]. A traumatic tear starts with sudden knee pain after an injury [S2]. Some people have what doctors call mechanical symptoms, meaning problems with how the knee moves [S3]. The sources here give only limited detail on symptoms, so ask a clinician about other signs.

### How it is diagnosed
A health care provider asks about the history of the problem, examines the knee, and does special tests [S1]. An MRI scan is most likely used to confirm the tear [S1]. Experts did not agree that every person needs an MRI, but they advised it when arthroscopy (keyhole knee surgery) is being considered, to look for other injuries [S2].

### Treatment options
The choice depends on age, other health problems, the type of tear, and symptoms [S1].
- **Care without surgery:** This may be preferred for some people with small tears, advanced osteoarthritis, or who cannot have surgery [S1]. Trials found surgery was not better than non-surgical care for degenerative tears [S1].
- **Meniscus repair:** Repair aims to let the torn meniscus heal instead of removing it [S1]. It has better long-term results than removing part of the meniscus and is recommended especially for young people with new injury tears [S1]. When repair is needed, experts say it should be done as early as possible [S2]. Recovery takes longer than after trimming, and repairs fail and need another surgery more often [S2].
- **Partial meniscectomy:** This surgery trims away the torn part of the meniscus [S1]. People usually return to daily activities within 2 to 4 weeks [S2]. It is still the most common meniscus surgery, but it is no longer the first choice because of long-term side effects [S1]. People who had it later needed a knee replacement about three times more often [S1].
- **Healing boosters:** Experts found no evidence that add-ons like needling or platelet-rich plasma improve healing [S2].

### When to seek care
The sources in this pack do not give specific advice on when to see a clinician, so ask a health care provider. They do show that treatment decisions need a careful check of the knee, and that when repair is needed, early surgery is preferred [S1][S2].

## Common Misunderstandings
- **Myth:** The meniscus is not important, so removing it is harmless. **Fact:** The meniscus carries weight and keeps the knee stable, and removing it can lead to knee instability and osteoarthritis [S1].
- **Myth:** All meniscus tears are the same. **Fact:** Traumatic and degenerative tears have different causes and need different treatment approaches [S2].
- **Myth:** Trimming a worn meniscus always helps the pain. **Fact:** In a trial, trimming a degenerative tear gave no better symptom relief than placebo surgery at 5 years and slightly raised the chance of arthritis on X-rays [S3].
- **Myth:** Older tears can never be repaired. **Fact:** Experts say many tears once thought unrepairable, such as older or long tears, should be repaired [S2].

## Questions to Ask Your Doctor
1. Is my tear from an injury or from wear over time?
2. Do I need an MRI, and what would it show?
3. Can my meniscus be repaired, or would part of it need to be removed?
4. Could care without surgery work for my type of tear?
5. How long might recovery take with each option?
6. What can I do to lower my chance of knee arthritis later?

## Test Questions
1. Name two jobs the meniscus does in the knee. - Examples: sharing weight, absorbing shock, keeping the knee stable, or helping the joint move smoothly [S1].
2. What is the difference between a traumatic and a degenerative tear? - A traumatic tear comes from an injury with sudden pain; a degenerative tear develops slowly from wear [S2].
3. Which imaging test is most likely used to confirm a meniscus tear? - MRI [S1].
4. Why do experts prefer saving the meniscus when possible? - Long-term results are worse after partial meniscectomy than after repair [S1][S2].
5. What did a 5-year trial find about trimming degenerative tears? - It gave no better symptom relief than placebo surgery [S3].
6. Which knee ligament injury often comes with a meniscus tear? - An ACL tear [S2].

## Related Topics
- Complication of: Anterior Cruciate Ligament Tear (KO-SPORT-COND-001)
- Read next: Knee Osteoarthritis (KO-JOINT-COND-001)

## References
1. [S1] Cureus. *Meniscus Tear: Pathology, Incidence, and Management.* https://pmc.ncbi.nlm.nih.gov/articles/PMC9205760/ (retrieved 2026-10-26)
2. [S2] Knee Surgery, Sports Traumatology, Arthroscopy. *Management of traumatic meniscus tears: the 2019 ESSKA meniscus consensus.* https://pmc.ncbi.nlm.nih.gov/articles/PMC7148286/ (retrieved 2026-10-26)
3. [S3] British journal of sports medicine. *Arthroscopic partial meniscectomy for a degenerative meniscus tear: a 5 year follow-up of the placebo-surgery controlled FIDELITY (Finnish Degenerative Meniscus Lesion Study) trial.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7606577/ (retrieved 2026-11-14)
