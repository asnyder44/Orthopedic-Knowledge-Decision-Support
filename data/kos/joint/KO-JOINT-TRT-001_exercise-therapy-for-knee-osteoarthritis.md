---
schema_version: okds-ko-1.0
ko_id: KO-JOINT-TRT-001
title: Exercise Therapy for Knee Osteoarthritis
preferred_term: Exercise Therapy for Knee Osteoarthritis
alternate_terms:
- physical therapy for knee arthritis
- exercise training for knee osteoarthritis
- therapeutic exercise for knee OA
- physiotherapy exercise for knee OA
ko_type: Treatment
specialty: JOINT
cluster: 4
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Exercise therapy for knee osteoarthritis (OA) uses planned physical activity, such as strength, aerobic,
  balance, and mind-body exercise, to ease symptoms [S1][S3][S5]. Guidelines recommend exercise as a core treatment
  for OA, and reviews of many trials show it can reduce pain and improve function and quality of life [S4][S5].
  The benefits are strongest in the first couple of months and may fade over time [S4].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- knee osteoarthritis treatment
- exercise
- physical therapy
- strength training
- aerobic exercise
- tai chi
- non-surgical treatment
relationships:
- predicate: TREATS
  target_id: KO-JOINT-COND-001
  target_label: Knee Osteoarthritis
  source_ids:
  - S1
  - S3
  - S4
  - S5
- predicate: ALTERNATIVE_TO
  target_id: KO-JOINT-PROC-001
  target_label: Total Knee Arthroplasty
  source_ids:
  - S1
  - S3
proposed_concepts:
- term: Aerobic exercise
  suggested_type: Treatment
  predicate: ALTERNATIVE_TO
  reason: S5 found aerobic exercise most helpful for pain and performance in knee and hip OA.
- term: Mind-body exercise (tai chi, yoga)
  suggested_type: Treatment
  predicate: ALTERNATIVE_TO
  reason: S5 found mind-body exercise best for function and equal to aerobic exercise for pain.
- term: Weight loss for osteoarthritis
  suggested_type: Treatment
  predicate: ALTERNATIVE_TO
  reason: S1 lists weight loss with exercise as a first treatment for knee and hip OA.
- term: Exercise therapy for hip osteoarthritis
  suggested_type: Treatment
  predicate: TREATS
  reason: S4 and S5 pool knee and hip OA; a separate hip KO could link to Hip Osteoarthritis.
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
  title: Benefits and Mechanisms of Exercise Training for Knee Osteoarthritis
  publisher: Frontiers in Physiology
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8716769/
  source_type: journal_article
  audience: clinician
  publication_date: '2021'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC8716769). Licence: CC BY'
- id: S4
  title: 'Efficacy and potential determinants of exercise therapy in knee and hip osteoarthritis: A systematic
    review and meta-analysis'
  publisher: Annals of Physical and Rehabilitation Medicine
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6880792/
  source_type: journal_article
  audience: clinician
  publication_date: '2019'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC6880792). Licence: CC BY'
- id: S5
  title: 'Relative Efficacy of Different Exercises for Pain, Function, Performance and Quality of Life in Knee
    and Hip Osteoarthritis: Systematic Review and Network Meta-Analysis'
  publisher: Sports Medicine (Auckland, N.z.)
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6459784/
  source_type: journal_article
  audience: clinician
  publication_date: '2019'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC6459784). Licence: CC BY'
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
  - 'Risks and side effects: the pack says exercise is relatively safe compared with medicines (S4) but gives
    no specific side effects or safety precautions; clinician should add content from a new source.'
  - 'Who it may suit: S4''s finding that younger people, people with knee OA, and those not awaiting joint
    replacement benefit more is a study-level analysis the authors say needs confirmation; KO states this caveat.'
  - S4 and S5 pool knee and hip OA trials; results are not knee-only. S3 includes animal-study mechanisms;
    the KO avoids animal findings except as clearly labeled.
  - 'ALTERNATIVE_TO Total Knee Arthroplasty: sources present exercise as first-line before surgery and surgery
    as suited to end-stage disease (S1, S3), not as a direct head-to-head alternative; confirm the predicate.'
  - No guideline is in the pack; 'guidelines recommend exercise' is reported second-hand by S4 and S5. Consider
    adding a knee OA guideline.
  - MeSH ID and ICD-10-CM code are not applicable/unknown and set to <verify>.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- A new Cochrane review or guideline on exercise for knee osteoarthritis is published.
- MedlinePlus or NIAMS shows a new 'last updated' or 'last reviewed' date on a cited osteoarthritis page.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Exercise therapy for knee osteoarthritis (OA) uses planned physical activity to ease knee pain and help the knee work better [S1][S3]. Treatment for OA usually begins with exercises to improve strength, flexibility, and balance [S1]. Guidelines recommend exercise as a core treatment for OA, and reviews of many studies show it can reduce pain and improve function and quality of life [S4][S5]. The benefits seem largest after about 2 months and then slowly fade [S4].

## Key Facts (claim → source)
- Treatment of OA usually starts with exercise to improve strength, flexibility, and balance [S1].
- International guidelines recommend exercise as a core non-drug treatment for OA [S4][S5].
- A review of 77 trials found exercise reduced pain and improved function, performance, and quality of life compared with usual care at about 8 weeks [S4].
- In that review, the benefits peaked around 2 months and were no better than usual care after about 9 months [S4].
- Exercise types include aerobic, strengthening, balance, aquatic, and mind-body exercise like tai chi and yoga [S3][S5].
- One large review found aerobic and mind-body exercise worked best for pain, and mind-body exercise worked best for function [S5].
- Exercise is relatively safe compared with medicines [S4].

## Explanation
### What it is
Knee OA is a long-lasting disease in which the cartilage, the bone under it, and the joint lining are damaged [S1][S2][S3]. Exercise therapy, or exercise training, aims to improve how the body works using a person's own strength, help from a therapist, or equipment [S3]. Common types include [S3][S5]:
- **Strengthening:** exercises that make muscles stronger, such as squats or lifting weights [S5].
- **Aerobic:** exercises that build heart and lung fitness, such as swimming [S5].
- **Flexibility and skill:** stretches to improve range of motion, and balance and coordination training [S5].
- **Mind-body:** movement combined with relaxation or mindfulness, such as tai chi and yoga [S5].
- **Aquatic and neuromuscular exercise:** water-based exercise and training that improves muscle control [S3].

### How it helps
Joint pain can make a person less active, and that can lead to weak muscles that put more stress on the joint [S2]. Reviews show that exercise can improve pain, stiffness, joint function, and muscle weakness in knee OA [S3][S4]. Exercise may also improve heart and lung fitness, muscle strength, posture, and mood [S3]. Studies in animals suggest exercise may lower inflammation and slow damage to cartilage and bone, but this has not been shown the same way in people [S3]. MedlinePlus notes that OA has no cure, so the goals are to ease pain, help a person move better, and keep the disease from getting worse [S1].

### Who it may suit
Exercise is a first treatment for most people with OA, along with weight loss if needed and braces or shoe inserts [S1]. Surgery is meant for end-stage knee OA, so a non-surgical option like exercise is especially important for people with earlier disease [S3]. One review found that people who were younger than about 60, had knee OA (rather than hip OA), and were not waiting for joint replacement got more pain relief from exercise [S4]. The authors say these findings need to be confirmed [S4]. Exercise done before and after knee surgery can also help restore thigh muscle strength [S3].

### Risks and side effects
Exercise is considered relatively safe compared with OA medicines [S4]. By contrast, some OA medicines can have side effects such as heart, blood pressure, and kidney problems [S3]. The sources in this pack do not describe specific side effects of exercise or safety precautions, so ask a clinician or physical therapist which exercises are safe for you.

### Evidence summary
- A review of 77 trials with about 6,500 people found exercise helped pain, function, performance, and quality of life compared with usual care at about 8 weeks [S4].
- The effects were largest around 2 months, then slowly faded, and were no better than usual care at 9 to 18 months [S4].
- A network review of 103 trials with about 9,100 people found aerobic exercise best for pain and performance, and mind-body exercise best for function [S5].
- In the same review, strengthening and flexibility or skill exercises helped several outcomes at a moderate level, while mixed programs were the least effective [S5].
- Many of these trials included both knee and hip OA, so results are not for the knee alone [S4][S5].

## Common Misunderstandings
- **Myth:** People with knee arthritis should avoid exercise. **Fact:** Exercise is a core treatment for OA and can reduce pain and improve function [S1][S4][S5].
- **Myth:** All kinds of exercise work the same. **Fact:** The effect varies by type; aerobic and mind-body exercise did best for pain in one large review, and mixed programs did least well [S5].
- **Myth:** Once you finish an exercise program, the benefit lasts forever. **Fact:** In one review, benefits peaked around 2 months and faded to no better than usual care by about 9 months [S4].
- **Myth:** Exercise cures knee OA. **Fact:** OA has no cure; treatment aims to ease pain and help a person move better [S1].

## Questions to Ask Your Doctor
1. What type of exercise is best for my knee: strengthening, aerobic, balance, or something like tai chi?
2. Should I work with a physical therapist to start?
3. Are there any exercises I should avoid?
4. How will we know if the exercise program is helping?
5. How can I keep the benefits going over time?

## Test Questions
1. What three things do OA exercises usually aim to improve? - Strength, flexibility, and balance [S1].
2. When did the benefits of exercise peak in a review of 77 trials? - Around 2 months [S4].
3. Which exercise types worked best for pain in a large network review? - Aerobic and mind-body exercise [S5].
4. Give an example of mind-body exercise. - Tai chi or yoga [S5].
5. Is exercise considered safe compared with OA medicines? - Yes, it is considered relatively safe compared with medicines [S4].

## Related Topics
- Treats: Knee Osteoarthritis (KO-JOINT-COND-001)
- Alternative to: Total Knee Arthroplasty (KO-JOINT-PROC-001)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Osteoarthritis.* https://medlineplus.gov/osteoarthritis.html (retrieved 2026-10-26)
2. [S2] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Osteoarthritis.* https://www.niams.nih.gov/health-topics/osteoarthritis (retrieved 2026-10-26)
3. [S3] Frontiers in Physiology. *Benefits and Mechanisms of Exercise Training for Knee Osteoarthritis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC8716769/ (retrieved 2026-10-26)
4. [S4] Annals of Physical and Rehabilitation Medicine. *Efficacy and potential determinants of exercise therapy in knee and hip osteoarthritis: A systematic review and meta-analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC6880792/ (retrieved 2026-10-26)
5. [S5] Sports Medicine (Auckland, N.z.). *Relative Efficacy of Different Exercises for Pain, Function, Performance and Quality of Life in Knee and Hip Osteoarthritis: Systematic Review and Network Meta-Analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC6459784/ (retrieved 2026-10-26)
