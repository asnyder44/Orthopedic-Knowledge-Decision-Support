---
schema_version: okds-ko-1.0
ko_id: KO-FOOT-COND-004
title: Achilles Tendinopathy
preferred_term: Achilles Tendinopathy
alternate_terms:
- Achilles tendinitis
- Achilles tendinosis
- AT
- insertional Achilles tendinopathy
- midportion (noninsertional) Achilles tendinopathy
ko_type: Condition
specialty: FOOT
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Achilles tendinopathy is a common overuse problem of the Achilles tendon, the large tendon at
  the back of the ankle, that causes pain, swelling, and trouble with activities that load the tendon
  [S2][S3][S5]. It is common in runners and jumping athletes but also affects people who are not active
  [S4][S5]. Treatment usually starts without surgery, such as with exercise programs, and surgery is
  considered if that fails [S2].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- Achilles tendon
- heel pain
- overuse injury
- running injury
- tendon pain
- eccentric exercise
relationships:
- predicate: CONTRASTS_WITH
  target_id: KO-FOOT-COND-003
  target_label: Achilles Tendon Rupture
  source_ids:
  - S3
proposed_concepts:
- term: Achilles tendon
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S2, S4 and S5 describe the tendon as the site of the condition; no foot/ankle anatomy KO is in
    the registry.
- term: VISA-A questionnaire
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: S3 says VISA-A is the most commonly used outcome measure for Achilles tendinopathy.
- term: Royal London Hospital test / painful arc sign
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S2 and S3 describe these exam tests for Achilles tendinopathy.
- term: Achilles tendon ultrasound
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S2 says ultrasound, MRI and X-ray can support the clinical diagnosis.
- term: Eccentric calf exercise
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S2 lists eccentric exercise among the main conservative treatments.
- term: Fluoroquinolone (quinolone) antibiotic use
  suggested_type: Concept
  predicate: HAS_RISK_FACTOR
  reason: S2, S4 and S5 name quinolone antibiotics as a risk factor; needs a Concept KO.
sources:
- id: S1
  title: Tendinitis
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/tendinitis.html
  source_type: government_health_page
  audience: patient
  publication_date: '2026-09-01'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:tendinitis). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
- id: S2
  title: 'Achilles Tendinopathy Pathogenesis and Management: A Narrative Review †'
  publisher: International Journal of Environmental Research and Public Health
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10487940/
  source_type: journal_article
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC10487940). Licence: CC BY'
- id: S3
  title: 'The clinical diagnosis of Achilles tendinopathy: a scoping review'
  publisher: PeerJ
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8485842/
  source_type: journal_article
  audience: clinician
  publication_date: '2021'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC8485842). Licence: CC BY'
- id: S4
  title: 'Clinical risk factors for Achilles tendinopathy: a systematic review'
  publisher: British Journal of Sports Medicine
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6837257/
  source_type: journal_article
  audience: clinician
  publication_date: '2019'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC6837257). Licence: CC BY'
- id: S5
  title: 'Achilles Tendinopathy: Current Concepts about the Basic Science and Clinical Treatments'
  publisher: BioMed Research International
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5112330/
  source_type: journal_article
  audience: clinician
  publication_date: '2016'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC5112330). Licence: CC BY'
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
  - S1 (MedlinePlus Tendinitis) is a general page about tendinitis, not specific to the Achilles tendon;
    it is used only for general tendon facts. Consider adding a patient page specific to Achilles tendon
    problems.
  - 'Terminology conflict: S1 describes tendinitis as tendon swelling (inflammation); S3 and S5 prefer ''tendinopathy''
    and say inflammation is not found in the failed-healing stages. The KO explains both; clinician check.'
  - 'Risk factors: S4 (systematic review, all studies high risk of bias) found being overweight was NOT linked,
    while S2 and S5 (narrative reviews) list obesity as a risk factor. The KO notes the conflict.'
  - 'Treatment options: the pack lacks a full-text treatment section, so evidence for each treatment (eccentric
    exercise, shockwave, injections, surgery) is not graded. Consider adding a treatment review or guideline.'
  - 'When to seek care: no source gives explicit warning signs; the section uses S1/S3 general statements.
    Clinician check needed.'
  - S2 lists NSAIDs among treatments; the KO names no medicines or doses on purpose.
  - MeSH and ICD-10-CM codes are unknown and set to verify.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- Any cited page shows a new 'last reviewed' date.
- A new clinical practice guideline or systematic review on Achilles tendinopathy treatment is published.
- Achilles tendon anatomy, VISA-A or exercise-therapy KOs are added to the registry (add links).
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Achilles tendinopathy is a common overuse problem of the Achilles tendon, the large tendon at the back of the ankle, that causes pain, swelling, and trouble with activities that load the tendon [S2][S3][S5]. It is common in runners and jumping athletes but also affects people who are not active [S4][S5]. Treatment usually starts without surgery, such as with exercise programs, and surgery is considered if that fails [S2].

## Key Facts (claim → source)
- Tendons are flexible bands of tissue that connect muscles to bones [S1].
- The Achilles tendon is the largest and strongest tendon in the body, and it is the tendon most often affected by tendinopathy [S2][S4].
- The main signs are pain, swelling, and reduced ability to do activities that load the tendon, such as running or hopping [S3][S5].
- There are two main types: insertional, where the tendon attaches to the heel bone, and midportion, about 2 to 6 cm above the heel [S2][S5].
- It is common in runners, but about one-third of patients do not play sports [S4][S5].
- Diagnosis is mainly based on the person's history and a physical exam, and imaging can help confirm it [S2][S3].
- Non-surgical treatment comes first, and surgery is considered when it does not work [S2].

## Explanation
### What it is
The Achilles tendon joins the calf muscles to the heel bone [S5]. Tendinopathy means a tendon problem with pain, swelling, and reduced function [S2][S5]. Experts now prefer the word "tendinopathy" over older terms like "tendinitis" (which suggests swelling or inflammation) and "tendinosis," because studies show a failed healing process in the tendon rather than simple inflammation [S3][S5]. In this failed healing, the tendon tissue becomes disorganized and new blood vessels grow into it [S5].

There are two main types [S2][S5]:
- **Insertional:** at the spot where the tendon attaches to the heel bone [S5].
- **Midportion (noninsertional):** about 2 to 6 cm above the heel, where the tendon has the poorest blood supply [S5].

### Causes and risk factors
Tendinitis often happens after repeated injury to an area such as the ankle [S1]. Achilles tendinopathy mostly comes from overuse, and it is common in sports with running and jumping [S2][S5]. Reviews list these possible risk factors [S2][S5]:
- **Training errors:** too much load, sudden changes in training, more distance, lots of hill training, or hard or sloping surfaces [S2][S5].
- **Foot and leg shape:** such as a high arch, uneven leg length, or a stiff foot joint [S2][S5].
- **Health conditions:** older age, diabetes, high cholesterol, gout, and inflammatory arthritis [S2][S5].
- **Some medicines:** quinolone antibiotics and corticosteroids [S2][S4][S5].

A systematic review found only limited evidence for nine risk factors, including a past lower-leg tendon problem or fracture, weak calf muscles, moderate alcohol use, and training in cold weather [S4]. That review did not find a link with being overweight, even though other reviews list obesity as a risk factor [S2][S4].

### Symptoms
- Pain in the Achilles tendon, often 2 to 6 cm above the heel [S2][S3].
- Pain at the start of and after exercise at first, and later during exercise and daily activities [S2].
- Morning stiffness, which tends to be worse when the condition is more severe [S2].
- Swelling or thickening of the tendon [S2][S5].
- Pain and trouble with activities that load the tendon, such as heel raises or hopping [S3].

### How it is diagnosed
Doctors diagnose tendon problems with the medical history, a physical exam, and sometimes imaging tests [S1]. For Achilles tendinopathy, the key parts are where the pain is, pain when the tendon is pressed, and the person's history [S2][S3]. The clinician looks at both legs while standing and lying face down, and feels the tendon for tenderness, heat, thickening, or lumps [S2]. Exam tests such as the Royal London Hospital test and the painful arc sign may help confirm the diagnosis [S2][S3]. Ultrasound, MRI, or X-rays can be used to confirm or rule out the diagnosis [S2]. The clinician also needs to rule out other problems, such as a partial or complete Achilles tendon tear [S3]. There is no single agreed "gold standard" test for this condition [S3].

### Treatment options
There is no agreed best treatment, and many studies disagree [S2][S5].
- **First steps:** the first goal is to reduce pain and swelling, for example with rest, wrapping or raising the area, and medicines [S1].
- **Non-surgical treatment:** this is usually tried first and includes anti-inflammatory medicines, eccentric exercises (slowly lowering the heel while the calf muscle works), and low-energy shockwave therapy [S2]. Other options for tendon problems include physical therapy, ultrasound treatment, and steroid injections [S1].
- **Surgery:** open or minimally invasive surgery may be considered when non-surgical treatment does not work [S2]. Choices should be based on the person's needs and activity level [S2].

### When to seek care
The sources here do not list specific warning signs, so ask a health care provider about Achilles pain that does not go away [S1][S2]. A clinician can check whether the pain comes from tendinopathy or from another problem, such as a partial or complete tendon tear or an inflamed fluid sac (bursitis) near the heel [S3]. Over time, the pain can start to interfere with daily activities [S2].

## Common Misunderstandings
- **Myth:** Achilles tendinopathy is just inflammation, so it is the same as "tendinitis." **Fact:** Experts now prefer "tendinopathy" because studies show a failed healing process in the tendon, not simple inflammation [S3][S5].
- **Myth:** Only athletes get it. **Fact:** About one-third of people with Achilles tendinopathy are not active, though it is most common in runners [S4].
- **Myth:** Surgery is the main treatment. **Fact:** Non-surgical treatment is tried first, and surgery is considered only if it fails [S2].
- **Myth:** There is one proven best treatment. **Fact:** Reviews say there is still no agreed best treatment [S2][S5].

## Questions to Ask Your Doctor
1. Is my pain from Achilles tendinopathy, and is it insertional or midportion?
2. Do I need an ultrasound or MRI?
3. Which exercises should I do, and how should I change my training?
4. Could any medicines I take affect my tendons?
5. What would we try if exercise does not help?

## Test Questions
1. What are the main signs of Achilles tendinopathy? - Pain, swelling, and trouble with activities that load the tendon [S3][S5].
2. Name the two main types. - Insertional (at the heel bone) and midportion (2 to 6 cm above the heel) [S2][S5].
3. Name one possible risk factor. - Examples: training errors, quinolone antibiotics, or weak calf muscles [S4][S5].
4. What is the main way it is diagnosed? - The person's history and a physical exam, with imaging as support [S2][S3].
5. What questionnaire is most often used to track Achilles tendinopathy? - The VISA-A questionnaire [S3].

## Related Topics
- Often confused with / contrasts with: Achilles Tendon Rupture (KO-FOOT-COND-003)
- Proposed topics: Achilles tendon, VISA-A questionnaire, Royal London Hospital test / painful arc sign, Achilles tendon ultrasound, Eccentric calf exercise, Fluoroquinolone antibiotic use.

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Tendinitis.* https://medlineplus.gov/tendinitis.html (retrieved 2026-10-26)
2. [S2] International Journal of Environmental Research and Public Health. *Achilles Tendinopathy Pathogenesis and Management: A Narrative Review †.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10487940/ (retrieved 2026-10-26)
3. [S3] PeerJ. *The clinical diagnosis of Achilles tendinopathy: a scoping review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC8485842/ (retrieved 2026-10-26)
4. [S4] British Journal of Sports Medicine. *Clinical risk factors for Achilles tendinopathy: a systematic review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC6837257/ (retrieved 2026-10-26)
5. [S5] BioMed Research International. *Achilles Tendinopathy: Current Concepts about the Basic Science and Clinical Treatments.* https://pmc.ncbi.nlm.nih.gov/articles/PMC5112330/ (retrieved 2026-10-26)
