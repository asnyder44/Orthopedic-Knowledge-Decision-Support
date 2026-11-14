---
schema_version: okds-ko-1.0
ko_id: KO-SPINE-COND-003
title: Adolescent Idiopathic Scoliosis
preferred_term: Adolescent Idiopathic Scoliosis
alternate_terms:
- scoliosis
- AIS
- idiopathic scoliosis
ko_type: Condition
specialty: SPINE
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Adolescent idiopathic scoliosis (AIS) is a sideways, S- or C-shaped curve of the spine that shows
  up in children and teens, usually from about age 10 until they stop growing, and has no known cause
  [S2][S3]. It is the most common type of scoliosis and is found more often in girls [S2][S3]. Depending
  on the curve, treatment may be regular check-ups, a brace, or surgery [S1][S2].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- spine
- spinal curve
- children and teens
- posture
- back brace
- spinal fusion
- x-ray
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-SPINE-PROC-001
  target_label: Spinal Fusion
  source_ids:
  - S2
  - S3
proposed_concepts:
- term: Spine (vertebral column)
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S1 and S2 describe the sideways curve of the spine; no spine anatomy KO is in the registry.
- term: Spine x-ray and Cobb angle measurement
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S2 calls x-rays the most common test for scoliosis, and S3 says AIS is confirmed by a Cobb angle
    of 10 degrees or more.
- term: Forward bending exam (trunk asymmetry check)
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S2 says doctors check whether one side of the rib cage is higher when the child bends forward.
- term: Scoliosis bracing
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S1, S2, and S4 describe bracing to slow or stop curve growth in children who are still growing.
- term: Physiotherapeutic scoliosis-specific exercises (PSSE)
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S4 (SOSORT guidelines) gives recommendations on PSSE; S2 mentions physical therapy.
sources:
- id: S1
  title: Scoliosis
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/scoliosis.html
  source_type: government_health_page
  audience: patient
  publication_date: '2025-12-31'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:scoliosis). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
- id: S2
  title: Scoliosis in Children and Teens
  publisher: National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH)
  url: https://www.niams.nih.gov/health-topics/scoliosis
  source_type: government_health_page
  audience: patient
  publication_date: '2023-07-01'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (niams:scoliosis). Licence: Public domain (U.S. federal government
    work, NIH/NIAMS); credit NIAMS'
- id: S3
  title: Current concepts in the diagnosis and management of adolescent idiopathic scoliosis
  publisher: Child's Nervous System
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7250959/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC7250959). Licence: CC BY'
- id: S4
  title: '2016 SOSORT guidelines: orthopaedic and rehabilitation treatment of idiopathic scoliosis during
    growth'
  publisher: Scoliosis and Spinal Disorders
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5795289/
  source_type: journal_article
  audience: clinician
  publication_date: '2018'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC5795289). Licence: CC BY'
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
  - S4 (SOSORT 2016 guidelines) text in this pack is mainly the abstract and methods; specific bracing
    or exercise recommendations are not included, so only general statements are cited. SOSORT planned
    later updates (2019-2025); check for newer versions.
  - Sources S1 and S2 describe scoliosis in general (all types); facts are applied to AIS only where they
    speak of idiopathic scoliosis or children and teens. Clinician check.
  - The pack does not give clear advice on when to seek care; the KO uses the signs listed in S2 and tells
    readers to ask a clinician.
  - MeSH ID and ICD-10-CM code are not stated in any source and remain <verify>.
  - Only 1 registry link is supported by this pack (Spinal Fusion); brace, x-ray, and exercise KOs are
    proposed.
  - Plain-language definitions (e.g., idiopathic, Cobb angle, vertebrae) were written by the drafter;
    check they match the sources.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus or NIAMS shows a new 'last updated' or 'last reviewed' date on a cited scoliosis page.
- SOSORT or the Scoliosis Research Society publishes updated guidelines on scoliosis assessment, bracing,
  or exercise.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Adolescent idiopathic scoliosis (AIS) is a sideways curve of the spine that develops in children and teens, from about age 10 until they finish growing [S2][S3]. "Idiopathic" means doctors do not know the cause [S2]. It is the most common type of scoliosis, and girls are more likely to have it than boys [S2][S3]. Depending on the curve, treatment may be regular check-ups, a brace, or surgery [S1][S2].

## Key Facts (claim → source)
- Scoliosis is a sideways curve of the spine, often shaped like an S or a C [S1][S2].
- AIS is seen in children from about age 10 until their skeleton is fully grown [S3].
- AIS affects about 2 to 4 out of 100 adolescents [S3].
- Girls are more likely to have it, and severe curves are more common in girls [S2][S3].
- It is more likely if a parent, brother, or sister has scoliosis [S2][S3].
- Most children and teens with mild scoliosis have no symptoms or pain [S2].
- X-rays are the most common test used to diagnose and measure the curve [S2].
- With treatment, check-ups, and follow-up, most children and teens with scoliosis lead normal, active lives [S2].

## Explanation
### What it is
Everyone's spine has normal curves, but when viewed from behind it should look straight [S2]. In scoliosis, the spine curves sideways in an S- or C-shape [S1][S2]. AIS is a three-dimensional problem of the spine, which means the bones also twist (rotate), not just bend sideways [S3]. Doctors confirm AIS when the curve measures 10 degrees or more on a measure called the Cobb angle, together with twisting of the spine bones [S3]. It is the most common type of scoliosis [S2][S3].

### Causes and risk factors
For most children and teens, the cause is unknown, which is what "idiopathic" means [S2]. Researchers think a mix of factors plays a role, such as genes, hormones, and changes in cell structure [S2]. Studies of families and twins suggest genes are involved [S3]. Risk factors include:
- **Age and growth:** curves start and grow fastest during the growth spurt of puberty [S3]. Idiopathic scoliosis usually shows up at age 11 or older [S2].
- **Sex:** girls are more likely to have it [S1][S2]. Small curves are about equally common in girls and boys, but severe curves are more common in girls [S3].
- **Family history:** the chance is higher if a parent, brother, or sister has scoliosis [S2][S3].

Other types of scoliosis have a known cause, such as a problem with spine growth before birth, nerve and muscle diseases, injury, or a tumor [S2].

### Symptoms
Most children and teens with mild scoliosis have no symptoms or pain [S2]. A child, teen, or family member may notice changes in posture [S2]. Signs can include [S1][S2]:
- Uneven shoulders.
- One shoulder blade that sticks out more than the other.
- One hip that looks higher than the other.
- One side of the rib cage that is higher when bending forward.
- Leaning to one side.

If the curve gets worse and becomes severe, it can cause back pain [S2]. Rarely, a severe curve can make breathing difficult [S2]. Scoliosis is sometimes easy to notice, but not always [S1].

### How it is diagnosed
Because most children have no symptoms, scoliosis is often found during a routine check-up or school screening [S1][S2]. The doctor asks about medical and family history [S2]. The exam looks at posture, for uneven shoulders or trunk, and whether one side of the rib cage is higher when the child bends forward [S2]. X-rays are the most common test; they show and measure the curve, which helps the doctor judge how severe it is and plan treatment [S2]. Expert groups have also written recommendations on how to assess scoliosis in growing children [S4].

### Treatment options
Treatment depends on where the curve is, how large it is, whether it causes symptoms, and whether the child is still growing [S1][S2]. Goals include stopping or slowing the curve, easing pain, preventing breathing problems, and improving posture and quality of life [S2].
- **Observation:** a mild curve in a growing child may only need check-ups every few months [S2].
- **Bracing:** for a moderate curve in a child who is still growing, a fitted brace is worn every day for the hours the doctor sets, to keep the curve from getting worse [S2]. Research shows braces work well when the child is still growing and wears the brace as directed [S2]. The 2016 SOSORT guidelines note new high-quality evidence on bracing from one large trial [S4].
- **Exercise and physical therapy:** physical therapy may be used to strengthen muscles [S2]. The same guidelines give recommendations on scoliosis-specific exercises and note three newer randomized trials on them [S4].
- **Surgery:** if the curve keeps getting worse while the child is growing, surgery may be recommended [S2]. Spinal fusion joins two or more spine bones and can help straighten the curve, often with metal rods and screws [S2]. Another option for a child who is still growing is an expandable rod that the surgeon lengthens over time [S2]. All surgeries carry risks [S2].

### When to seek care
The sources here do not give a specific list of warning signs that need urgent care. NIAMS notes that posture changes, such as uneven shoulders or hips, may be a sign of scoliosis [S2]. A curve that gets worse can cause back pain, and rarely a severe curve can cause trouble breathing [S2]. Ask a health care provider which changes should prompt a visit.

## Common Misunderstandings
- **Myth:** Scoliosis always hurts. **Fact:** Most children and teens with mild scoliosis have no symptoms or pain [S2].
- **Myth:** Every child with scoliosis needs surgery. **Fact:** Many need only check-ups or a brace; surgery is for curves that keep getting worse [S1][S2].
- **Myth:** A brace works no matter how it is worn. **Fact:** Braces work well when the child is still growing and wears the brace as directed [S2].
- **Myth:** Scoliosis is caused by poor posture or something the child did. **Fact:** In most cases the cause is unknown, and genes, hormones, and growth may play a role [S2][S3].

## Questions to Ask Your Doctor
1. How large is my child's curve, and is it likely to get worse?
2. How often will my child need check-ups and x-rays?
3. Would a brace help, and how many hours a day would it need to be worn?
4. Are there exercises or physical therapy that could help?
5. At what point would surgery be considered, and what are the risks?
6. Can my child keep playing sports and staying active?

## Test Questions
1. What does "idiopathic" mean in adolescent idiopathic scoliosis? - That the cause is unknown [S2].
2. What shape does a scoliosis curve usually make? - An S-shape or a C-shape [S1][S2].
3. What is the most common test used to diagnose and measure scoliosis? - An x-ray [S2].
4. When does a brace work best? - When the child is still growing and wears the brace as directed [S2].
5. What does spinal fusion surgery do for scoliosis? - It joins two or more spine bones and can help straighten the curve [S2].

## Related Topics
- Read next: Spinal Fusion (KO-SPINE-PROC-001)
- Proposed topics (not yet in the library): spine anatomy, spine x-ray and Cobb angle, forward bending exam, scoliosis bracing, scoliosis-specific exercises

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Scoliosis.* https://medlineplus.gov/scoliosis.html (retrieved 2026-10-26)
2. [S2] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Scoliosis in Children and Teens.* https://www.niams.nih.gov/health-topics/scoliosis (retrieved 2026-10-26)
3. [S3] Child's Nervous System. *Current concepts in the diagnosis and management of adolescent idiopathic scoliosis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC7250959/ (retrieved 2026-10-26)
4. [S4] Scoliosis and Spinal Disorders. *2016 SOSORT guidelines: orthopaedic and rehabilitation treatment of idiopathic scoliosis during growth.* https://pmc.ncbi.nlm.nih.gov/articles/PMC5795289/ (retrieved 2026-10-26)
