---
schema_version: okds-ko-1.0
ko_id: KO-FOOT-COND-003
title: Achilles Tendon Rupture
preferred_term: Achilles Tendon Rupture
alternate_terms:
- ruptured Achilles tendon
- ATR
- acute Achilles tendon rupture
- torn Achilles tendon
ko_type: Condition
specialty: FOOT
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: An Achilles tendon rupture is a tear through the Achilles tendon, the large cord at the back
  of the ankle that joins the calf muscles to the heel bone [S2][S5]. It usually happens suddenly during
  sports, often with a "pop" and pain at the back of the ankle [S1][S3]. It can be treated without surgery
  or with surgical repair, and surgery lowers the chance of the tendon tearing again [S4][S5].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- Achilles tendon
- heel cord
- calf
- sports injury
- Thompson test
- tendon tear
relationships:
- predicate: CONTRASTS_WITH
  target_id: KO-FOOT-COND-004
  target_label: Achilles Tendinopathy
  source_ids:
  - S3
  - S5
proposed_concepts:
- term: Achilles tendon
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S2 and S5 describe the tendon (from the gastrocnemius and soleus muscles to the heel bone); no
    foot/ankle anatomy KO is in the registry.
- term: Thompson test (Simmonds-Thompson calf squeeze test)
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S1 and S2 describe the calf squeeze test as a key exam test for a complete rupture.
- term: Achilles tendon ultrasound
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S1 says point-of-care ultrasound can show the torn and pulled-apart tendon ends.
- term: Achilles tendon repair (open or minimally invasive)
  suggested_type: Procedure
  predicate: PREREQUISITE_FOR
  reason: S4 compares open and minimally invasive repair with non-surgical treatment.
- term: Functional rehabilitation with early mobilization after Achilles rupture
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S5 says functional rehab with early mobilization had outcomes comparable to surgery.
sources:
- id: S1
  title: Achilles Tendon Rupture
  publisher: Western Journal of Emergency Medicine
  url: https://doi.org/10.5811/westjem.2014.10.24127
  source_type: journal_article
  audience: clinician
  publication_date: '2015'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via openaire. Licence: Open Access. Type: article. Text kept: abstract only.'
- id: S2
  title: Thompson Test in Achilles Tendon Rupture
  publisher: Journal of Education and Teaching in Emergency Medicine
  url: http://jetem.org/thompson-test-achilles-tendon-rupture/
  source_type: journal_article
  audience: clinician
  publication_date: '2016'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via doaj. Licence: open access journal (licence per article: <verify>). Type: article.
    Text kept: abstract only.'
- id: S3
  title: 'Incidence, demographics, characteristics and management of acute Achilles tendon rupture: An
    epidemiological study'
  publisher: PLOS ONE
  url: https://doi.org/10.1371/journal.pone.0304197
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via plos. Licence: CC BY 4.0 (PLOS). Type: article. Text kept: abstract only.'
- id: S4
  title: 'Rerupture outcome of conservative versus open repair versus minimally invasive repair of acute
    Achilles tendon ruptures: A systematic review and meta-analysis'
  publisher: PLOS ONE
  url: https://doi.org/10.1371/journal.pone.0285046
  source_type: systematic_review
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via plos. Licence: CC BY 4.0 (PLOS). Type: systematic review. Text kept: abstract only.'
- id: S5
  title: 'Current Concepts in the Nonoperative Management of Achilles Tendon Pathologies: A Scoping Review'
  publisher: Journal of Clinical Medicine
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12250464/
  source_type: journal_article
  audience: clinician
  publication_date: '2025'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC12250464). Licence: CC BY'
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
  - No patient-level page (MedlinePlus/NIAMS) covering Achilles rupture was found in the dataset or candidates;
    all sources are clinician-level. Consider adding a MedlinePlus or NIAMS page on Achilles tendon injuries.
  - 'Source quality: S1 (WestJEM) and S2 (JETem) are short emergency-medicine case/image reports (abstract
    text only, permitted_use link_and_paraphrase; S2 licence per article is <verify>). They are used for
    symptoms, mechanism and exam findings; a review or guideline would be stronger.'
  - 'Causes and risk factors: the pack does not cover risk factors such as age or medicines; only sex, sport
    and prior Achilles problems (S3, one UK emergency department) are stated. Clinician check needed.'
  - 'When to seek care: no source gives explicit advice; the section is based on the emergency-department
    cases in S1/S2. Clinician check needed.'
  - 'Incidence figures differ: S3 reports 8 per 100,000 per year (UK); S5 cites up to 40 per 100,000. The
    KO states both.'
  - 'CONTRASTS_WITH Achilles Tendinopathy: S5 describes them as separate conditions and S3 reports prior
    tendinopathy in many patients; no source in this pack directly explains how to tell them apart.'
  - MeSH and ICD-10-CM codes are unknown and set to verify.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- Any cited page shows a new 'last reviewed' date.
- A new systematic review or guideline compares surgical and non-surgical treatment of Achilles tendon
  rupture.
- Achilles tendon anatomy, Thompson test or Achilles repair KOs are added to the registry (add links).
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
An Achilles tendon rupture is a tear through the Achilles tendon, the large cord at the back of the ankle that joins the calf muscles to the heel bone [S2][S5]. It usually happens suddenly during sports, often with a "pop" and pain at the back of the ankle [S1][S3]. It can be treated without surgery or with surgical repair, and surgery lowers the chance of the tendon tearing again [S4][S5].

## Key Facts (claim → source)
- The Achilles tendon is the largest and strongest tendon in the body, and it lets you point your foot down [S5].
- Most ruptures happen during sports, and in one UK study about 4 out of 5 patients were men [S3].
- People often feel a sudden "pop" and sharp pain at the back of the ankle, then have trouble walking [S1][S2].
- In the Thompson test, squeezing the calf of the hurt leg does not make the foot move, which points to a complete tear [S1][S2].
- Ultrasound can show the torn tendon ends pulled apart [S1].
- Both open and minimally invasive surgery lowered the chance of a re-tear compared with non-surgical care [S4].
- Non-surgical care with early, controlled movement has had results comparable to surgery in some studies [S5].

## Explanation
### What it is
The Achilles tendon, also called the heel cord, is formed by the two calf muscles, the gastrocnemius and the soleus, and attaches to the heel bone [S2][S5]. It is the largest and strongest tendon in the body and helps you push off and steady the ankle when you walk [S5]. Even so, high, repeated loads make it prone to both sudden injuries and overuse injuries [S5]. A rupture is a tear through the tendon, and it most often happens about 2 to 6 cm above the heel, where the tendon has a poor blood supply [S2]. Achilles tendon ruptures make up about 11% of all tendon and ligament injuries [S3].

### Causes and risk factors
A rupture typically happens when a person pushes off on the foot with the knee straight, or when the ankle is suddenly forced to bend upward [S1]. In a study from a UK emergency department, about 65% of ruptures happened during sports, and about 79% of patients were men [S3]. In that study, almost half had had an earlier rupture or Achilles tendinopathy (long-term tendon pain), and about 1 in 4 had Achilles pain before the tear [S3]. Reported rates range from about 8 to as many as 40 cases per 100,000 people per year [S3][S5].

### Symptoms
- A sudden "pop" felt at the back of the ankle, often during sports [S1][S2].
- Sharp pain at the back of the ankle that gets worse with movement [S1].
- Trouble putting weight on the foot and walking [S1][S2].
- A gap that can be felt in the tendon [S1][S2].

### How it is diagnosed
A clinician asks how the injury happened and examines both ankles [S1][S2]. Exam findings can include a gap in the tendon, weakness when pointing the foot down, and the ankle bending upward more than normal [S1].
- **Thompson test (calf squeeze):** the person lies face down with the feet over the edge of the table, or kneels on a chair, and the clinician squeezes the calf [S2]. In a healthy leg the foot points down; with a complete rupture the foot does not move [S1][S2]. Studies report the test is very accurate for complete tears, but the data are limited [S2].
- **Ultrasound:** an ultrasound scan done at the bedside can show a break in the tendon with the two ends pulled apart and a pocket of blood between them [S1].

### Treatment options
Treatment can be non-surgical (conservative) or surgical repair, and experts do not agree on which is best for everyone [S4][S5]. Treatment plans should fit each person's goals [S5].
- **Non-surgical care:** the ankle is kept still (immobilized) for a time, and non-surgical plans include rehabilitation [S3][S5]. In one UK study, 97% of patients were treated without surgery, and the leg was kept still for about 63 days on average [S3]. Rehabilitation programs that start careful movement early have had results comparable to surgical repair [S5].
- **Surgery:** a surgeon repairs the tendon, either through an open cut or with a minimally invasive method that uses smaller cuts [S4]. A review of 13 trials found both types lowered the chance of a re-tear compared with non-surgical care, with no clear difference between the two [S4].

Recovery takes a long time, and some people have lasting calf weakness that affects daily life [S3].

### When to seek care
The sources here do not give specific advice on when to seek care, so ask a health care provider [S1][S2]. In the cases these sources describe, people with a sudden pop, pain at the back of the ankle, and trouble walking were checked in an emergency department [S1][S2].

## Common Misunderstandings
- **Myth:** A tendon this strong cannot tear. **Fact:** The Achilles is the strongest tendon in the body, but it still often gets hurt because it carries very high loads [S5].
- **Myth:** Every Achilles rupture needs surgery. **Fact:** Many ruptures are treated without surgery, and early-movement rehab programs have had results comparable to surgery [S3][S5].
- **Myth:** Surgery and non-surgical care have the same risk of re-tear. **Fact:** A review of trials found surgery lowered the chance of a re-tear compared with non-surgical care [S4].
- **Myth:** An Achilles rupture always comes out of nowhere. **Fact:** In one study, about 1 in 4 people had Achilles pain before the tear, and many had had an earlier Achilles problem [S3].

## Questions to Ask Your Doctor
1. Is my Achilles tendon fully torn, and do I need an ultrasound?
2. What are the pros and cons of surgery versus non-surgical treatment for me?
3. How long will my ankle need to be kept still?
4. When can I start rehab, and what will it involve?
5. What is my chance of tearing the tendon again?

## Test Questions
1. Which muscles form the Achilles tendon? - The calf muscles, the gastrocnemius and the soleus [S2][S5].
2. What do people often feel when the Achilles tendon ruptures? - A sudden pop and sharp pain at the back of the ankle [S1][S2].
3. What happens in the Thompson test when the tendon is fully torn? - Squeezing the calf does not make the foot point down [S1][S2].
4. What can an ultrasound show in a rupture? - The torn tendon ends pulled apart, with blood between them [S1].
5. What did a review of 13 trials find about surgery? - Open and minimally invasive surgery both lowered the chance of a re-tear compared with non-surgical care [S4].

## Related Topics
- Often confused with / contrasts with: Achilles Tendinopathy (KO-FOOT-COND-004)
- Proposed topics: Achilles tendon, Thompson test, Achilles tendon ultrasound, Achilles tendon repair, Functional rehabilitation with early mobilization.

## References
1. [S1] Western Journal of Emergency Medicine. *Achilles Tendon Rupture.* https://doi.org/10.5811/westjem.2014.10.24127 (retrieved 2026-11-14)
2. [S2] Journal of Education and Teaching in Emergency Medicine. *Thompson Test in Achilles Tendon Rupture.* http://jetem.org/thompson-test-achilles-tendon-rupture/ (retrieved 2026-11-14)
3. [S3] PLOS ONE. *Incidence, demographics, characteristics and management of acute Achilles tendon rupture: An epidemiological study.* https://doi.org/10.1371/journal.pone.0304197 (retrieved 2026-11-14)
4. [S4] PLOS ONE. *Rerupture outcome of conservative versus open repair versus minimally invasive repair of acute Achilles tendon ruptures: A systematic review and meta-analysis.* https://doi.org/10.1371/journal.pone.0285046 (retrieved 2026-11-14)
5. [S5] Journal of Clinical Medicine. *Current Concepts in the Nonoperative Management of Achilles Tendon Pathologies: A Scoping Review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC12250464/ (retrieved 2026-10-26)
