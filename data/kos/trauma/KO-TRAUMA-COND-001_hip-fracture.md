---
schema_version: okds-ko-1.0
ko_id: KO-TRAUMA-COND-001
title: Hip Fracture
preferred_term: Hip Fracture
alternate_terms:
- femoral neck fracture
- broken hip
ko_type: Condition
specialty: TRAUMA
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: A hip fracture is a break in the upper part of the thigh bone (femur), near where it fits into
  the hip socket [S1][S2][S5]. It happens most often in older people, usually after a fall, and weak bones
  from osteoporosis make it more likely [S1][S3]. Nearly everyone with a hip fracture goes to the hospital
  for surgery [S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- broken hip
- femur
- thigh bone
- falls
- older adults
- osteoporosis
- hip surgery
- hip replacement
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-TRAUMA-COND-003
  target_label: Osteoporotic Fracture
  source_ids:
  - S1
  - S2
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-TRAUMA-PROC-001
  target_label: Open Reduction and Internal Fixation
  source_ids:
  - S2
  - S5
- predicate: PREREQUISITE_FOR
  target_id: KO-JOINT-PROC-002
  target_label: Total Hip Arthroplasty
  source_ids:
  - S1
  - S5
proposed_concepts:
- term: Femur (thigh bone)
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S1 and S5 describe the break in the upper femur (femoral neck); no femur KO exists in the registry.
- term: Hip joint
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S1 explains the hip as a ball-and-socket joint between the femur and pelvis; needed for an AFFECTS
    link.
- term: Hemiarthroplasty
  suggested_type: Procedure
  predicate: PREREQUISITE_FOR
  reason: S5 names unipolar and bipolar hemiarthroplasty as a main surgery for femoral neck fractures
    in older people.
- term: X-ray (radiograph)
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S2 says an x-ray or other imaging test is used to see whether a bone is broken.
- term: Falls in older adults
  suggested_type: Concept
  predicate: HAS_RISK_FACTOR
  reason: S1 and S3 name falls (and more falls with age) as a main cause of hip fractures.
- term: Pressure sores
  suggested_type: Condition
  predicate: COMPLICATION_OF
  reason: S4 links delayed hip fracture surgery to more pressure sores; a Condition KO would hold the
    COMPLICATION_OF link.
sources:
- id: S1
  title: Hip Injuries and Disorders
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/hipinjuriesanddisorders.html
  source_type: government_health_page
  audience: patient
  publication_date: '2025-06-25'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:hipinjuriesanddisorders). Licence: Public domain (NLM-authored
    MedlinePlus summary); credit MedlinePlus'
- id: S2
  title: Fractures
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/fractures.html
  source_type: government_health_page
  audience: patient
  publication_date: '2024-05-14'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:fractures). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
- id: S3
  title: Epidemiology of hip fractures
  publisher: Zeitschrift Fur Gerontologie Und Geriatrie
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6353815/
  source_type: journal_article
  audience: clinician
  publication_date: '2018'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC6353815). Licence: CC BY'
- id: S4
  title: 'Timing Matters in Hip Fracture Surgery: Patients Operated within 48 Hours Have Better Outcomes.
    A Meta-Analysis and Meta-Regression of over 190,000 Patients'
  publisher: PLoS ONE
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3463569/
  source_type: journal_article
  audience: clinician
  publication_date: '2012'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC3463569). Licence: CC BY'
- id: S5
  title: Treatment of femoral neck fractures in elderly patients over 60 years of age - which is the ideal
    modality of primary joint replacement?
  publisher: Patient Safety in Surgery
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2972258/
  source_type: journal_article
  audience: clinician
  publication_date: '2010'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC2972258). Licence: CC BY'
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
  - MeSH ID and ICD-10-CM code are unknown and set to verify; no source in this pack states them.
  - No source in this pack is a patient page written only about hip fracture (MedlinePlus has no stand-alone
    hip fracture page in the dataset). Symptoms and diagnosis use the general MedlinePlus Fractures page
    (S2); a clinician should confirm they fit hip fractures (for example, being unable to stand or walk
    is not stated in the pack).
  - S5 describes closed reduction and internal fixation with screws for younger adults, not open reduction.
    The PREREQUISITE_FOR link to Open Reduction and Internal Fixation rests on S2 (plates, pins, or screws)
    and S5; confirm this link is appropriate.
  - S5 (2010) is one review that favors total hip arthroplasty over hemiarthroplasty for people over 60;
    the KO presents this as one review's view. A newer guideline would help.
  - S3 and S4 are not patient-level sources and give death-rate figures; the KO uses general wording.
    Check the tone is right for patients and caregivers.
  - The plain-language definition of 'femoral neck' as the upper part of the thigh bone near the hip socket
    was written by the drafter from S1 and S5; check the wording.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus shows a new 'last updated' date on the Hip Injuries and Disorders or Fractures page.
- A newer review or guideline on hip fracture surgery timing or surgery type (fixation versus hip replacement)
  is added to the source pack.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
A hip fracture is a break in the upper part of the thigh bone (femur), near where it fits into the hip socket [S1][S2][S5]. It happens most often in older people, usually after a fall, and weak bones from osteoporosis make it more likely [S1][S3]. Nearly everyone with a hip fracture goes to the hospital for surgery [S3]. Surgery is usually done soon, because waiting longer has been linked to more problems [S4].

## Key Facts (claim → source)
- The hip is a ball-and-socket joint where the ball at the top of the thigh bone (femur) fits into a socket in the pelvis [S1].
- A fracture is a break in a bone; a hip fracture is a break near the top of the femur, such as the femoral neck [S2][S5].
- The chance of a hip fracture rises very quickly with age, because bones get thinner and falls become more common [S3].
- In Western countries, about three out of four hip fractures happen in women [S3].
- In the year 2000 there were an estimated 1.6 million hip fractures around the world [S3].
- Surgery is the main treatment, and nearly everyone with a hip fracture is admitted to the hospital for it [S3][S5].
- A large review found that surgery within about one to two days was linked to a lower risk of death and of pressure sores [S4].
- Hip fractures often lead to disability, moving into a care home, or death [S3].

## Explanation
### What it is
Your hip is the joint where the thigh bone (femur) meets the hip bone (pelvis) [S1]. The ball at the top of the femur fits into a socket in the pelvis [S1]. A fracture means a broken bone [S2]. In a hip fracture, the femur breaks near the hip; one common type is a break in the femoral neck, the narrow part just below the ball [S5]. A healthy hip takes great force to injure, but a fall can break it, especially if the bone is weak [S1]. Hip fractures are seen as a major public health problem around the world [S3].

### Causes and risk factors
- **Older age:** the risk climbs very fast as people get older, because bone mass drops and falls happen more often [S3]. Most patients are older than 75 [S4].
- **Being a woman:** about three of every four hip fractures in Western countries happen in women, partly because women live longer [S3].
- **Weak bones:** osteoporosis of the hip makes bones weak so they break easily [S1]. Low bone density and osteoporosis make any broken bone much more likely [S2].
- **Falls:** falls are a common cause of fractures [S2]. Falling can cause hip injuries such as fractures [S1].
- **Living in a care setting or with a disability:** about half of all hip fractures happen in people who have a disability and need care [S3]. In nursing homes, about 4 of every 100 women break a hip each year [S3].
- **Other factors:** many illnesses and medicines have been linked to hip fractures [S3]. Hip fractures are 20 to 60 percent more common in cities than in the countryside [S3].

### Symptoms
Hip fractures always cause pain and trouble getting around in the short term [S4]. In general, a broken bone can cause [S2]:
- Strong pain [S2].
- A limb that looks out of place (deformity) [S2].
- Swelling, bruising, or tenderness near the injury [S2].
- Trouble moving the injured part [S2].

Symptoms can be different depending on which bone is broken [S2].

### How it is diagnosed
To find out if a bone is broken, a health care provider asks about the injury and does a physical exam [S2]. The provider will likely order an x-ray or another imaging test to see the break [S2]. The sources here do not describe hip-specific tests, so ask a clinician which tests are needed.

### Treatment options
Surgery is the main treatment for femoral neck fractures today [S5]. The type of surgery depends on the person and the break, and experts still debate which is best for older adults [S5].
- **Fixing the bone in place:** in younger adults (about 20 to 50 years old), surgeons usually line up the bone and hold it with screws [S5]. Some surgeons also use screws or a sliding hip screw in older people [S5]. In general, some fractures need surgery to put in plates, pins, or screws [S2].
- **Hip replacement:** older adults may have the broken part replaced with a hip implant, either a hemiarthroplasty or a total hip arthroplasty (total hip replacement) [S5]. One review found that total hip replacement gave the best function for people over 60 with a displaced (shifted) femoral neck fracture [S5].
- **Timing:** guidelines advise surgery within 24 to 48 hours of arriving at the hospital [S4]. Some doctors may wait a short time to make a patient with other health problems more stable first [S4].
- **Recovery:** recovery can be hard, and many people have lasting pain or disability afterward [S3][S4].

To lower the chance of a broken bone, people can get enough calcium and vitamin D, stay active with weight-bearing exercise like walking, treat osteoporosis, and remove tripping hazards at home [S2].

### When to seek care
If you think someone may have broken a bone, get medical care right away [S2]. Fractures can be serious [S2]. With a hip fracture, waiting a long time for surgery has been linked to a higher risk of death and pressure sores (skin wounds from lying in one position) [S4].

## Common Misunderstandings
- **Myth:** A hip fracture is a minor injury that heals on its own with rest. **Fact:** Nearly everyone with a hip fracture is treated in the hospital with surgery, and hip fractures often lead to disability or death [S3][S5].
- **Myth:** It does not matter how soon hip fracture surgery happens. **Fact:** A large review linked surgery within one to two days to a lower risk of death and pressure sores [S4].
- **Myth:** Only women break their hips. **Fact:** About three of four hip fractures happen in women, but men break hips too, and in German nursing homes the rates for men and women were nearly the same [S3].
- **Myth:** Healthy hips break easily. **Fact:** A healthy hip takes great force to injure; weak bones from osteoporosis are what make breaks easy [S1].

## Questions to Ask Your Doctor
1. What kind of hip fracture is this, and where is the break?
2. Will the bone be fixed with screws, or will part of the hip be replaced, and why?
3. How soon can surgery be done, and is there any reason to wait?
4. What will recovery and getting back to walking look like?
5. Should I be checked for osteoporosis, and what can lower the chance of another fall or fracture?

## Test Questions
1. What two bones meet at the hip joint? - The femur (thigh bone) and the pelvis (hip bone) [S1].
2. Why does the risk of a hip fracture rise with age? - Bone mass goes down and falls become more common [S3].
3. About how many hip fractures happen in women in Western countries? - About three out of four [S3].
4. What test is usually used to see if a bone is broken? - An x-ray or another imaging test [S2].
5. What did a large review find about the timing of hip fracture surgery? - Surgery within one to two days was linked to a lower risk of death and pressure sores [S4].
6. Name two kinds of surgery used for femoral neck fractures. - Fixing the bone with screws, or hip replacement (hemiarthroplasty or total hip arthroplasty) [S5].

## Related Topics
- Read next: Osteoporotic Fracture (KO-TRAUMA-COND-003), Open Reduction and Internal Fixation (KO-TRAUMA-PROC-001), Total Hip Arthroplasty (KO-JOINT-PROC-002)
- Proposed new topics: Femur (anatomy), Hip joint (anatomy), Hemiarthroplasty (procedure), X-ray (diagnostic test), Falls in older adults (concept), Pressure sores (condition)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Hip Injuries and Disorders.* https://medlineplus.gov/hipinjuriesanddisorders.html (retrieved 2026-10-26)
2. [S2] MedlinePlus, U.S. National Library of Medicine. *Fractures.* https://medlineplus.gov/fractures.html (retrieved 2026-10-26)
3. [S3] Zeitschrift Fur Gerontologie Und Geriatrie. *Epidemiology of hip fractures.* https://pmc.ncbi.nlm.nih.gov/articles/PMC6353815/ (retrieved 2026-10-26)
4. [S4] PLoS ONE. *Timing Matters in Hip Fracture Surgery: Patients Operated within 48 Hours Have Better Outcomes. A Meta-Analysis and Meta-Regression of over 190,000 Patients.* https://pmc.ncbi.nlm.nih.gov/articles/PMC3463569/ (retrieved 2026-10-26)
5. [S5] Patient Safety in Surgery. *Treatment of femoral neck fractures in elderly patients over 60 years of age - which is the ideal modality of primary joint replacement?.* https://pmc.ncbi.nlm.nih.gov/articles/PMC2972258/ (retrieved 2026-10-26)
