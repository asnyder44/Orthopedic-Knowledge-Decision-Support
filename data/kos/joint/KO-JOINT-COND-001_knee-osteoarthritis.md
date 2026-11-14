---
schema_version: okds-ko-1.0
ko_id: KO-JOINT-COND-001
title: Knee Osteoarthritis
preferred_term: Knee Osteoarthritis
alternate_terms:
- knee arthritis
- osteoarthritis of the knee
- knee OA
- degenerative joint disease of the knee
ko_type: Condition
specialty: JOINT
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Knee osteoarthritis (OA) is a long-lasting joint disease in which the cartilage and other tissues
  of the knee slowly break down [S1][S2][S3]. It is the most common type of arthritis, and the knee is the
  joint it affects most often [S1][S4]. There is no cure, but exercise, weight loss, braces, medicines, and
  sometimes surgery can help manage it [S1].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- knee pain
- arthritis
- cartilage
- joint stiffness
- bone spurs
- weight-bearing joint
- exercise
- knee replacement
relationships:
- predicate: COMPLICATION_OF
  target_id: KO-SPORT-COND-001
  target_label: Anterior Cruciate Ligament Tear
  source_ids:
  - S3
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-JOINT-TRT-001
  target_label: Exercise Therapy for Knee Osteoarthritis
  source_ids:
  - S1
- predicate: PREREQUISITE_FOR
  target_id: KO-JOINT-PROC-001
  target_label: Total Knee Arthroplasty
  source_ids:
  - S1
  - S3
- predicate: CONTRASTS_WITH
  target_id: KO-JOINT-COND-002
  target_label: Hip Osteoarthritis
  source_ids:
  - S2
  - S4
proposed_concepts:
- term: Knee joint
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: All sources describe OA damaging the knee joint; no knee anatomy KO is in the registry.
- term: Articular cartilage
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S1, S2, and S4 describe cartilage breakdown as the core change in OA.
- term: Knee X-ray (radiograph)
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S1 and S2 say X-rays can show joint space loss and bone spurs; S4 notes X-ray changes do not match
    symptoms.
- term: Knee MRI
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S2 says MRI can show soft tissue damage, such as in a knee that locks or gives way.
- term: Obesity / excess body weight
  suggested_type: Concept
  predicate: HAS_RISK_FACTOR
  reason: S1, S2, S3, and S4 list being overweight as a risk factor.
- term: Intra-articular injection (knee)
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S1 and S3 mention joint injections (corticosteroid, hyaluronic acid, PRP) as treatment options.
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
  title: 'Knee Osteoarthritis: A Review of Pathogenesis and State-Of-The-Art Non-Operative Therapeutic Considerations'
  publisher: Genes
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7464436/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC7464436). Licence: CC BY'
- id: S4
  title: A Review on the Management of Hip and Knee Osteoarthritis
  publisher: International Journal of Chronic Diseases
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4590943/
  source_type: journal_article
  audience: clinician
  publication_date: '2013'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC4590943). Licence: CC BY'
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
  - No guideline is in this pack, so no evidence strength is given for any treatment; consider adding a knee
    OA guideline (e.g., AAOS) as a source.
  - 'When to seek care: the sources only say to talk with a provider about pain relievers and treatment; they
    give no red-flag symptoms. Clinician should confirm or add content from a new source.'
  - MeSH ID and ICD-10-CM code are unknown and set to <verify>; no source in the pack states them.
  - CONTRASTS_WITH Hip Osteoarthritis is based on S2/S4 describing different symptom locations and risk factors
    for knee vs hip OA; confirm this link is useful.
  - 'COMPLICATION_OF ACL Tear: S3/S4 present past ACL injury as a strong risk factor for later knee OA; confirm
    the predicate fits.'
  - S4 (2013) and S3 (2020) are clinician reviews; the prevalence figures (10% of men and 13% of women age
    60+, 41% of limb OA in the knee) come from them; confirm.
  - Short plain-language definitions (e.g., 'cartilage', 'bone spurs') were written by the drafter from S1/S2
    wording; check they match.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus or NIAMS shows a new 'last updated' or 'last reviewed' date on a cited osteoarthritis page.
- A new clinical practice guideline for knee osteoarthritis is published (for example by AAOS or OARSI) and
  could be added to the pack.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Knee osteoarthritis (OA) is a long-lasting joint disease in which the cartilage and other tissues of the knee slowly break down [S1][S2][S3]. It is the most common type of arthritis, and the knee is the joint it affects most often [S1][S4]. It can cause pain, stiffness, and swelling that make walking and daily tasks harder [S2][S4]. There is no cure, but exercise, weight loss, braces, medicines, and sometimes surgery can help manage it [S1].

## Key Facts (claim → source)
- In OA, cartilage, the smooth tissue that covers the ends of bones, breaks down and becomes rough, and bones may start to rub together [S1].
- OA is now seen as a disease of the whole joint, including bone, the joint lining, ligaments, and the meniscus in the knee [S2][S3].
- The knee is the joint most often affected, holding up to 41% of arthritis in the limbs [S4].
- About 10% of men and 13% of women age 60 or older are thought to have knee OA [S3].
- Risk factors include older age, extra body weight, a past knee injury or surgery, joint overuse, a joint that does not line up well, and family history [S1][S2][S3].
- There is no single test for OA; diagnosis uses a health history, a physical exam, and sometimes X-rays, MRI, or lab tests [S1][S2].
- Treatment usually starts with exercise, weight loss if needed, and braces or shoe inserts [S1].
- Joint replacement may be an option in late-stage disease when other treatments have not helped enough [S1][S3].

## Explanation
### What it is
A joint is where two bones meet [S2]. In a healthy knee, the ends of the bones are covered with cartilage, a smooth, slippery tissue that cushions the bones and helps them glide [S1]. In OA, this cartilage breaks down and gets rough, and sometimes it wears away so the bones rub together [S1]. Small bumps of extra bone, called bone spurs (osteophytes), may grow at the edges of the joint [S1][S2].

Experts now see knee OA as a disease of the whole joint, not just the cartilage [S3][S4]. It can also harm the bone under the cartilage, the joint lining (synovium), ligaments, tendons, and the meniscus, a pad of cartilage inside the knee [S2][S3]. The damage usually builds slowly over years, but it can get worse quickly in some people [S2].

### Causes and risk factors
Researchers do not know exactly what starts the breakdown of the joint [S1][S2]. NIAMS says it is not caused by simple "wear and tear," but by changes in the joint tissue that trigger damage over time [S2]. Things that raise the chance of knee OA include [S1][S2][S3][S4]:
- Getting older; OA becomes more common in middle age and later [S1][S2].
- Being a woman, especially after age 50 [S1][S2][S3].
- Being overweight, because extra weight puts more stress on the joints [S1][S3].
- A past knee injury or surgery, such as a torn ACL (a knee ligament) or a torn meniscus [S1][S3][S4].
- Work or sports with a lot of kneeling, squatting, heavy lifting, jumping, or twisting [S1][S3][S4].
- A knee that does not line up correctly or is unstable [S1][S3].
- A family history of OA [S1][S2].

In younger people, OA is often caused by an earlier joint injury [S1][S2]. Not moving enough can also play a role, because it leads to weaker, less stable joints [S3].

### Symptoms
OA symptoms often start slowly, and not everyone has pain [S1][S2]. Common symptoms are [S1][S2]:
- Pain when using the knee, which often gets better with rest [S1][S2].
- Stiffness, usually lasting less than 30 minutes, after waking up or resting [S1][S2].
- Swelling, especially after a lot of activity [S1][S2].
- Less movement in the knee than normal [S1][S2].
- A feeling that the knee is loose or unstable [S1][S2].

In the knee, a person may hear a grinding or scraping sound when moving, and over time weak muscles and ligaments can make the knee buckle (give way) [S2]. As OA gets worse, tasks like climbing a step, getting out of a chair, or walking across a parking lot can become hard [S2]. Pain may also lead to tiredness, poor sleep, and feeling depressed [S2][S3].

### How it is diagnosed
There is no single test for OA [S1][S2]. A health care provider will ask about symptoms and health history and do a physical exam [S1][S2]. Other tests may include [S1][S2]:
- X-rays, which can show narrowing of the joint space, bone damage, and bone spurs [S2]. Early damage often does not show on X-rays [S2].
- MRI (magnetic resonance imaging), which can show damage to soft tissues and helps check a knee that locks or gives out [S2].
- Blood tests or a sample of joint fluid, to rule out other causes like infection or gout [S1][S2].

X-ray changes do not always match how a person feels; many people with OA on X-ray have no symptoms [S4].

### Treatment options
The goals of treatment are to ease pain, help the person move better, and keep OA from getting worse [S1]. Treatment usually begins with [S1]:
- **Exercise** to build strength, flexibility, and balance [S1].
- **Weight loss**, if needed, which can ease knee pain [S1].
- **Braces or shoe inserts** (orthotics) fitted by a health care provider [S1].

Over-the-counter pain relievers and arthritis creams can help, and it is best to talk with a provider before using them [S1]. If they are not enough, a provider may suggest shots into the joint or prescription pain medicines [S1]. Shots used in knee OA include corticosteroids, hyaluronic acid, and platelet-rich plasma (PRP), which is made from a person's own blood [S3]. Heat, ice, massage, and acupuncture may help some people [S1].

If these treatments do not help enough, surgery may be an option [S1]. In late-stage knee OA, total knee replacement may be the main choice left to improve quality of life [S3].

### When to seek care
The sources in this pack do not list specific warning signs for knee OA [S1][S2]. They do advise talking with a health care provider about pain relievers and about treatment choices, including whether surgery is right for you [S1]. Because OA can slowly limit daily tasks like walking and climbing stairs, knee pain or stiffness that gets in the way of daily life is worth discussing with a provider [S2]. Ask a clinician which symptoms need prompt attention.

## Common Misunderstandings
- **Myth:** Knee OA is just normal "wear and tear." **Fact:** NIAMS says OA is not caused by simple wear and tear; changes in the joint tissue trigger the breakdown over time [S2].
- **Myth:** OA only damages cartilage. **Fact:** OA affects the whole joint, including bone, the joint lining, ligaments, and the meniscus [S2][S3].
- **Myth:** If the X-ray looks bad, the knee must hurt a lot. **Fact:** X-ray changes do not reflect symptoms well, and many people with OA on X-ray have no symptoms [S4].
- **Myth:** Only older adults get knee OA. **Fact:** It is more common with age, but younger people can get it, often after a knee injury [S1][S2].

## Questions to Ask Your Doctor
1. Is my knee pain caused by osteoarthritis, or could it be something else?
2. Do I need an X-ray or an MRI?
3. What kinds of exercise are safe and helpful for my knee?
4. Would a brace, shoe inserts, or weight loss help in my case?
5. Which pain relievers or creams are safe for me to use?
6. At what point would knee replacement surgery be worth talking about?

## Test Questions
1. What happens to cartilage in osteoarthritis? - It breaks down and becomes rough, and sometimes wears away so the bones rub together [S1].
2. Name three risk factors for knee OA. - Examples: older age, being overweight, a past knee injury, joint overuse, poor joint alignment, or family history [S1][S2][S3].
3. Is there a single test that diagnoses OA? - No; providers use a health history, a physical exam, and sometimes X-rays, MRI, or lab tests [S1][S2].
4. What knee sound can happen with OA? - A grinding or scraping noise when walking or moving [S2].
5. What treatments usually come first for OA? - Exercise, weight loss if needed, and braces or shoe inserts [S1].
6. When is knee replacement usually considered? - In late-stage OA when other treatments have not helped enough [S1][S3].

## Related Topics
- Complication of: Anterior Cruciate Ligament Tear (KO-SPORT-COND-001)
- Contrasts with: Hip Osteoarthritis (KO-JOINT-COND-002)
- Read next: Exercise Therapy for Knee Osteoarthritis (KO-JOINT-TRT-001), Total Knee Arthroplasty (KO-JOINT-PROC-001)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Osteoarthritis.* https://medlineplus.gov/osteoarthritis.html (retrieved 2026-10-26)
2. [S2] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Osteoarthritis.* https://www.niams.nih.gov/health-topics/osteoarthritis (retrieved 2026-10-26)
3. [S3] Genes. *Knee Osteoarthritis: A Review of Pathogenesis and State-Of-The-Art Non-Operative Therapeutic Considerations.* https://pmc.ncbi.nlm.nih.gov/articles/PMC7464436/ (retrieved 2026-10-26)
4. [S4] International Journal of Chronic Diseases. *A Review on the Management of Hip and Knee Osteoarthritis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC4590943/ (retrieved 2026-10-26)
