---
schema_version: okds-ko-1.0
ko_id: KO-JOINT-COND-002
title: Hip Osteoarthritis
preferred_term: Hip Osteoarthritis
alternate_terms:
- hip arthritis
- osteoarthritis of the hip
- hip OA
- HOA
ko_type: Condition
specialty: JOINT
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Hip osteoarthritis (OA) is a long-lasting joint disease in which the cartilage and other tissues of
  the hip joint slowly break down [S1][S2][S4]. It is the second most common form of OA after knee OA, and
  it becomes more common with age [S4]. It can cause pain and stiffness in the hip or groin, and treatment
  ranges from exercise to hip replacement surgery [S1][S2][S5].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- hip pain
- groin pain
- arthritis
- cartilage
- joint stiffness
- bone spurs
- exercise therapy
- hip replacement
relationships:
- predicate: CONTRASTS_WITH
  target_id: KO-JOINT-COND-001
  target_label: Knee Osteoarthritis
  source_ids:
  - S2
  - S3
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-JOINT-PROC-002
  target_label: Total Hip Arthroplasty
  source_ids:
  - S1
  - S3
proposed_concepts:
- term: Hip joint
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: All sources describe OA damaging the hip joint; no hip anatomy KO is in the registry.
- term: Articular cartilage
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S1, S2, S3, and S4 describe cartilage breakdown as the core change in OA.
- term: Hip X-ray (radiograph)
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S2 and S4 say X-rays show joint space narrowing and bone spurs; S4 says it is the most used way to
    grade hip OA.
- term: Exercise therapy for hip osteoarthritis
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S5 is a meta-analysis showing exercise therapy helps pain and function in hip OA; the registry only
    has a knee-specific exercise KO.
- term: Hip shape variants (abnormal hip morphology)
  suggested_type: Concept
  predicate: HAS_RISK_FACTOR
  reason: S3 links hip shape measurements to later need for hip replacement.
sources:
- id: S1
  title: Osteoarthritis
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/osteoarthritis.html
  source_type: government_health_page
  audience: patient
  publication_date: '2024-01-08'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:osteoarthritis). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
- id: S2
  title: Osteoarthritis
  publisher: National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH)
  url: https://www.niams.nih.gov/health-topics/osteoarthritis
  source_type: government_health_page
  audience: patient
  publication_date: '2023-09-01'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (niams:osteoarthritis). Licence: Public domain (U.S. federal government
    work, NIH/NIAMS); credit NIAMS'
- id: S3
  title: A Review on the Management of Hip and Knee Osteoarthritis
  publisher: International Journal of Chronic Diseases
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4590943/
  source_type: journal_article
  audience: clinician
  publication_date: '2013'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC4590943). Licence: CC BY'
- id: S4
  title: 'The prevalence of hip osteoarthritis: a systematic review and meta-analysis'
  publisher: Arthritis Research & Therapy
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10053484/
  source_type: journal_article
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC10053484). Licence: CC BY'
- id: S5
  title: 'Effect of exercise therapy in patients with hip osteoarthritis: A systematic review and cumulative
    meta-analysis'
  publisher: Osteoarthritis and Cartilage Open
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9932106/
  source_type: journal_article
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC9932106). Licence: CC BY'
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
  - Only 2 relationships could be supported by registry targets and pack text; consider a hip anatomy KO and
    an exercise-for-hip-OA KO (see proposed_concepts).
  - No guideline is in this pack, so no evidence strength is given for treatments other than exercise (S5).
  - 'When to seek care: the sources give no red-flag symptoms for hip OA; the section only repeats general
    advice to talk with a provider. Clinician should confirm or add a source.'
  - S4 found no significant difference in hip OA prevalence between men and women, while S1/S2 say OA in general
    is more common in women after 50. The KO states both; clinician should confirm the wording.
  - Prevalence figures (8.55% worldwide by X-ray; about 3% of adults over 30 with symptoms) come from S4 and
    S3; confirm.
  - MeSH ID and ICD-10-CM code are unknown and set to <verify>; no source in the pack states them.
  - CONTRASTS_WITH Knee Osteoarthritis is based on different symptom locations and risk factors in S2/S3; confirm
    this link is useful.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus or NIAMS shows a new 'last updated' or 'last reviewed' date on a cited osteoarthritis page.
- A new clinical practice guideline for hip osteoarthritis is published and could be added to the pack.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Hip osteoarthritis (OA) is a long-lasting joint disease in which the cartilage and other tissues of the hip joint slowly break down [S1][S2][S4]. It is the second most common form of OA, after knee OA, and it becomes more common with age [S4]. It can cause pain and stiffness in the hip or groin and make walking harder [S2][S3][S4]. There is no cure, but treatments like exercise, weight loss, medicines, and hip replacement surgery can help [S1][S5].

## Key Facts (claim → source)
- In OA, cartilage, the smooth tissue that covers the ends of the bones, breaks down and becomes rough [S1][S4].
- Hip OA is the second most common form of OA, after knee OA [S4].
- About 8.5% of people worldwide have hip OA on X-ray, and it becomes more common with age [S4].
- Hip OA often causes pain in the groin, and pain and stiffness can limit how far the hip moves [S2][S4].
- Risk factors include older age, extra body weight, a past hip injury, family history, and hip shape [S1][S2][S3].
- Diagnosis uses a health history, a physical exam, and often X-rays [S1][S2][S4].
- Exercise therapy has been shown to ease pain and improve function in hip OA [S5].
- If other treatments do not help enough, surgery such as hip replacement may be an option [S1][S3].

## Explanation
### What it is
The hip is one of the main weight-bearing joints that OA affects [S2][S3]. In a healthy joint, the ends of the bones are covered with cartilage, a smooth, slippery tissue that lets the bones glide [S1]. In hip OA, this cartilage breaks down, and the bone under it changes as well [S1][S4]. Small bumps of extra bone, called bone spurs (osteophytes), can form at the edges of the joint [S2][S4]. OA can damage the whole joint, including bone, ligaments, and the joint lining (synovium) [S2][S3]. The damage usually builds slowly over years [S2].

Hip OA is common [S4]. A large review found that about 8.5% of people worldwide had hip OA on X-ray, with rates highest in Europe and lowest in Africa [S4]. Another review estimates that about 3% of adults over age 30 have hip arthritis symptoms [S3].

### Causes and risk factors
Researchers do not know exactly what starts the breakdown of the joint [S1][S2]. NIAMS says OA is not caused by simple "wear and tear," but by changes in the tissue that lead to damage over time [S2]. Factors that raise the chance of hip OA include:
- **Age:** hip OA becomes more common as people get older [S2][S4].
- **Body weight:** obesity is a risk factor for hip OA [S1][S3].
- **Past injury:** hip injuries from sports, falls, or car crashes are linked to a much higher risk of hip OA [S3].
- **Hip shape:** some differences in the shape of the hip bones are linked to OA and to later needing hip replacement [S3].
- **Family history and genes:** OA can run in families, and some genes have been linked to hip OA [S1][S3].
- **Joint overuse** from repeated movements [S1][S2].

OA in general is more common in women after age 50 [S1][S2]. However, a large review of hip OA found no clear difference in how often men and women had it [S4].

### Symptoms
OA symptoms often start slowly, and not everyone has pain [S1][S2]. With hip OA, a person may feel pain and stiffness in the hip, groin, inner thigh, or buttocks [S2]. Sometimes the pain spreads to the knee [S2]. Over time, the hip may not move as far as it used to [S2]. Other common OA symptoms include [S1][S2]:
- Pain when using the joint, which often eases with rest [S1][S2].
- Stiffness for less than 30 minutes after waking up or resting [S1][S2].
- Swelling after a lot of activity [S1][S2].
- A feeling that the joint is loose or unstable [S1][S2].

OA of the hip and knee is the most common cause of trouble walking [S3]. As it gets worse, tasks like getting in and out of a chair or walking across a parking lot can become hard [S2].

### How it is diagnosed
There is no single test for OA [S1][S2]. A health care provider asks about symptoms and health history and examines the joint [S1][S2]. X-rays are often used [S2][S4]. They can show a narrower joint space, bone spurs, and other bone changes [S2][S4]. Early damage may not show up on X-rays [S2]. MRI can show damage to soft tissues, and blood tests or a joint fluid sample can rule out other causes like infection or gout [S2].

X-ray results and symptoms do not always match; many people with OA changes on X-ray have no symptoms [S3].

### Treatment options
The goals of treatment are to ease pain, help the person move better, and keep OA from getting worse [S1]. Treatment usually starts with exercise to build strength, flexibility, and balance, weight loss if needed, and braces or shoe inserts fitted by a provider [S1]. Weight loss can ease pain in the hips and knees [S1].

A review of 18 studies found that exercise therapy led by a therapist helped pain and function in hip OA, both right after treatment and 6 to 9 months later [S5]. The benefits were mostly small [S5].

Over-the-counter pain relievers and creams can help, and it is best to check with a provider before using them [S1]. If they are not enough, a provider may suggest shots into the joint or prescription pain medicines [S1]. Heat, ice, massage, and acupuncture may help some people [S1]. If none of these help enough, surgery may be an option [S1]. More than 1 million total hip replacements are done around the world each year [S3].

### When to seek care
The sources in this pack do not list specific warning signs for hip OA [S1][S2]. They do advise talking with a health care provider about pain relievers and about whether surgery is right for you [S1]. Hip pain or stiffness that makes walking or daily tasks harder is worth discussing with a provider, since OA can slowly limit these activities [S2][S3]. Ask a clinician which symptoms need prompt attention.

## Common Misunderstandings
- **Myth:** Hip OA always causes pain right in the hip. **Fact:** Pain can be felt in the groin, inner thigh, or buttocks, and sometimes it spreads to the knee [S2].
- **Myth:** OA is just normal "wear and tear." **Fact:** NIAMS says OA is not caused by simple wear and tear; changes in the joint tissue trigger the breakdown [S2].
- **Myth:** Exercise will make hip OA worse. **Fact:** A review of 18 studies found that exercise therapy helped pain and function in hip OA [S5].
- **Myth:** Hip OA is mostly a women's disease. **Fact:** A large review found no clear difference in hip OA rates between men and women [S4].

## Questions to Ask Your Doctor
1. Could my hip, groin, or knee pain be coming from hip osteoarthritis?
2. Do I need an X-ray of my hip?
3. Would working with a physical therapist on an exercise program help me?
4. Would weight loss, a brace, or shoe inserts help in my case?
5. Which pain relievers or creams are safe for me?
6. When would hip replacement surgery be worth considering?

## Test Questions
1. What happens to the cartilage in hip OA? - It breaks down and becomes rough, and the bone under it changes [S1][S4].
2. Where can hip OA pain be felt besides the hip? - In the groin, inner thigh, or buttocks, and sometimes the knee [S2].
3. Name two risk factors for hip OA. - Examples: older age, obesity, a past hip injury, hip shape, or family history [S1][S2][S3].
4. What can an X-ray show in hip OA? - A narrower joint space and bone spurs [S2][S4].
5. Does exercise therapy help hip OA? - Yes; a review found it helped pain and function, though the effects were mostly small [S5].

## Related Topics
- Contrasts with: Knee Osteoarthritis (KO-JOINT-COND-001)
- Read next: Total Hip Arthroplasty (KO-JOINT-PROC-002)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Osteoarthritis.* https://medlineplus.gov/osteoarthritis.html (retrieved 2026-10-26)
2. [S2] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Osteoarthritis.* https://www.niams.nih.gov/health-topics/osteoarthritis (retrieved 2026-10-26)
3. [S3] International Journal of Chronic Diseases. *A Review on the Management of Hip and Knee Osteoarthritis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC4590943/ (retrieved 2026-10-26)
4. [S4] Arthritis Research & Therapy. *The prevalence of hip osteoarthritis: a systematic review and meta-analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10053484/ (retrieved 2026-10-26)
5. [S5] Osteoarthritis and Cartilage Open. *Effect of exercise therapy in patients with hip osteoarthritis: A systematic review and cumulative meta-analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC9932106/ (retrieved 2026-10-26)
