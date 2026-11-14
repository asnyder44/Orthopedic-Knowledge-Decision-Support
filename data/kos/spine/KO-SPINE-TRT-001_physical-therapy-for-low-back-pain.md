---
schema_version: okds-ko-1.0
ko_id: KO-SPINE-TRT-001
title: Physical Therapy for Low Back Pain
preferred_term: Physical Therapy for Low Back Pain
alternate_terms:
- exercise therapy for low back pain
- physiotherapy for low back pain
- exercise for back pain
ko_type: Treatment
specialty: SPINE
cluster: 4
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Physical therapy for low back pain uses exercise to build strength, flexibility, and fitness
  so the back is better supported [S3][S5]. Staying active and doing a general exercise program can help
  people with long-lasting low back pain [S3]. European back pain guidelines mostly recommend non-drug
  treatments such as these [S4].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- lower back
- back pain
- exercise
- physical therapy
- physiotherapy
- core strength
- treatment without surgery
relationships:
- predicate: TREATS
  target_id: KO-SPINE-COND-001
  target_label: Lumbar Spinal Stenosis
  source_ids:
  - S5
- predicate: TREATS
  target_id: KO-SPINE-COND-002
  target_label: Lumbar Disc Herniation
  source_ids:
  - S2
proposed_concepts:
- term: Low back pain (non-specific)
  suggested_type: Condition
  predicate: TREATS
  reason: S1, S3, and S4 describe low back pain, mostly without a known cause; there is no general low
    back pain Condition KO in the registry.
- term: Core stabilization exercise
  suggested_type: Treatment
  predicate: ALTERNATIVE_TO
  reason: S3 discusses core and muscle-strength exercise as one type of exercise for chronic low back
    pain.
- term: Decompression surgery (laminectomy)
  suggested_type: Procedure
  predicate: ALTERNATIVE_TO
  reason: S5 compares land-based exercise with decompression surgery for lumbar spinal stenosis.
- term: Oswestry Disability Index (ODI)
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: S3 and S5 use the ODI to measure back-related disability; MEASURED_BY would be set from the
    Condition or Procedure side.
sources:
- id: S1
  title: Back Pain
  publisher: National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH)
  url: https://www.niams.nih.gov/health-topics/back-pain
  source_type: government_health_page
  audience: patient
  publication_date: '2023-02-01'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (niams:back-pain). Licence: Public domain (U.S. federal government
    work, NIH/NIAMS); credit NIAMS'
- id: S2
  title: Herniated Disk
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/herniateddisk.html
  source_type: government_health_page
  audience: patient
  publication_date: '2025-12-17'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:herniateddisk). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
- id: S3
  title: A Systematic Review of the Effects of Exercise and Physical Activity on Non-Specific Chronic
    Low Back Pain
  publisher: Healthcare
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4934575/
  source_type: journal_article
  audience: clinician
  publication_date: '2016'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC4934575). Licence: CC BY'
- id: S4
  title: 'Evidence‐based treatment recommendations for neck and low back pain across Europe: A systematic
    review of guidelines'
  publisher: European Journal of Pain (London, England)
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7839780/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC7839780). Licence: CC BY'
- id: S5
  title: 'The effectiveness of land based exercise compared to decompressive surgery in the management
    of lumbar spinal-canal stenosis: a systematic review'
  publisher: BMC Musculoskeletal Disorders
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3305601/
  source_type: journal_article
  audience: clinician
  publication_date: '2012'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC3305601). Licence: CC BY'
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
  - The NIAMS text in this pack (S1) stops before its treatment section, so no patient-level source here
    describes what a physical therapy visit involves. Consider adding a NIAMS or MedlinePlus page on physical
    therapy or back pain treatment.
  - No source in this pack reports side effects of physical therapy or exercise; the Risks section uses
    S1 (overdoing exercise after being inactive) and S3 (too much or too little activity linked to back
    pain) and says side effects are not well covered. Clinician check.
  - S3 is a narrative-style systematic review by a single reviewer; its 52.5% pain reduction figure comes
    from one small study (37 patients) and is not used in the KO.
  - S4 (European guidelines review) text here is mostly abstract and methods; the specific strength of
    exercise recommendations for low back pain is not shown. Check the full paper.
  - S5 (2012) rests on one head-to-head trial and covers lumbar spinal stenosis, not general low back
    pain.
  - MeSH ID and ICD-10-CM code are not stated in any source and remain <verify>.
  - The candidate study on early guideline-adherent physical therapy (BMC Health Services Research 2015)
    was dropped to make room for S5; consider it for a later update.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- NIAMS or MedlinePlus shows a new 'last reviewed' date on a cited back pain or herniated disk page.
- A new low back pain clinical practice guideline (or update of the guidelines reviewed in S4) is published.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Physical therapy for low back pain uses exercise to make the muscles that support the spine stronger and more flexible [S3][S5]. A general exercise program that combines strength, flexibility, and aerobic fitness can help people with long-lasting low back pain [S3]. European back pain guidelines mostly recommend non-drug treatments, including referral to exercise therapy [S4]. Physical therapy is also one of the treatments for a herniated disk and for lumbar spinal stenosis [S2][S5].

## Key Facts (claim → source)
- Back pain is one of the most common medical problems, and almost everyone has it at some point [S1].
- Weak back and stomach muscles that do not support the spine well can raise the chance of back pain [S1].
- People with long-lasting, non-specific low back pain are advised to stay physically active, because long periods of inactivity can slow recovery [S3].
- A general exercise program that combines muscle strength, flexibility, and aerobic fitness is helpful for long-lasting non-specific low back pain [S3].
- The best single type of exercise for long-lasting low back pain is still not known [S3].
- A review of European guidelines found mainly non-drug treatment options recommended for low back pain [S4].
- Physical therapy is one of the treatments for a herniated disk [S2].

## Explanation
### What it is
Physical therapy (also called physiotherapy) for low back pain is care that uses exercise and activity to improve how the back works [S3][S5]. Exercise is a core part of physical therapy, and it helps people manage their own condition [S5]. Programs can include aerobic exercise (activity that raises the heart rate), core and muscle-strength exercises, and stretching or flexibility work [S3]. Exercise programs can be low cost and continued at home [S5]. In Europe, neck and low back pain are among the most common reasons people visit a family doctor or physiotherapist [S4].

### How it helps
- **Strength:** building core muscle strength can help support the lower spine [S3].
- **Flexibility:** stretching muscles, tendons, and ligaments in the back increases range of motion and helps with everyday movement [S3].
- **Aerobic fitness:** aerobic exercise increases blood flow to the soft tissues in the back, which may help healing and reduce stiffness [S3].
- **Staying active:** long periods of inactivity can hurt recovery from long-lasting low back pain [S3].
- **Coping:** exercise aims to counter both the physical and the emotional effects of losing fitness because of pain [S5].

### Who it may suit
- Adults with non-specific low back pain, meaning back pain with no clear cause, which is most back pain [S3].
- People with a herniated disk, where physical therapy is one of the standard treatments [S2].
- People with lumbar spinal stenosis, where one review suggests trying exercise before thinking about surgery [S5].

Doctors first look for the cause of back pain with a health history and a physical exam, because the best treatment depends on the cause [S1]. NIAMS advises seeing a doctor if back pain does not improve after a few weeks, or if it comes after a fall or injury or with trouble urinating, fever, weight loss you did not intend, or leg weakness or numbness [S1].

### Risks and side effects
The sources in this pack do not report specific side effects of physical therapy. One review noted that details of side effects were missing from exercise studies for spinal stenosis [S5]. Back pain is more likely if a person exercises too hard after being inactive for a while [S1]. Both too much and too little physical activity have been linked to low back pain [S3]. Ask a physical therapist or doctor how to start and progress exercise safely.

### Evidence summary
- For long-lasting non-specific low back pain, a review found that general exercise combining strength, flexibility, and aerobic fitness is helpful, but which type works best is still unknown [S3].
- A review of 17 European guidelines for neck and low back pain found broad agreement on mainly non-drug treatments for neck and low back pain, with generally moderate or strong recommendations for back pain [S4].
- For lumbar spinal stenosis, exercise programs showed early gains in function of about 16 to 29 percent [S5]. Surgery gave larger gains over two years, but the review still advised a trial of exercise first because of surgery's risks [S5].
- Experts note that back pain care often does not follow guidelines, for example by overusing imaging and opioids (strong prescription pain medicines) [S4].

## Common Misunderstandings
- **Myth:** Rest is the best treatment for long-lasting back pain. **Fact:** People with long-lasting non-specific low back pain are advised to stay active, because long inactivity can slow recovery [S3].
- **Myth:** There is one best exercise for back pain. **Fact:** The most effective type of exercise is still unknown, and a general program combining strength, flexibility, and aerobic fitness is helpful [S3].
- **Myth:** Physical therapy cannot help if you have spinal stenosis. **Fact:** Exercise programs showed early gains, and one review suggests trying exercise before surgery [S5].
- **Myth:** More exercise is always better. **Fact:** Both too much and too little physical activity have been linked to low back pain [S3].

## Questions to Ask Your Doctor
1. Could physical therapy help my back pain, and what would it involve?
2. Do we know what is causing my back pain, and does that change which exercises I should do?
3. Which exercises can I safely do at home?
4. How will we know if physical therapy is working?
5. What should I do if my pain gets worse during exercise?

## Test Questions
1. Name the three parts of a general exercise program that helps long-lasting low back pain. - Muscle strength, flexibility, and aerobic fitness [S3].
2. How can stronger core muscles help the back? - They help support the lower spine [S3].
3. Why are people with long-lasting low back pain advised to stay active? - Long periods of inactivity can slow recovery [S3].
4. What kinds of treatments do European back pain guidelines mostly recommend? - Mainly non-drug treatments [S4].
5. Is physical therapy one of the treatments for a herniated disk? - Yes [S2].

## Related Topics
- Treats: Lumbar Spinal Stenosis (KO-SPINE-COND-001), Lumbar Disc Herniation (KO-SPINE-COND-002)
- Proposed topics (not yet in the library): non-specific low back pain, core stabilization exercise, decompression surgery (laminectomy), Oswestry Disability Index

## References
1. [S1] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Back Pain.* https://www.niams.nih.gov/health-topics/back-pain (retrieved 2026-10-26)
2. [S2] MedlinePlus, U.S. National Library of Medicine. *Herniated Disk.* https://medlineplus.gov/herniateddisk.html (retrieved 2026-10-26)
3. [S3] Healthcare. *A Systematic Review of the Effects of Exercise and Physical Activity on Non-Specific Chronic Low Back Pain.* https://pmc.ncbi.nlm.nih.gov/articles/PMC4934575/ (retrieved 2026-10-26)
4. [S4] European Journal of Pain (London, England). *Evidence‐based treatment recommendations for neck and low back pain across Europe: A systematic review of guidelines.* https://pmc.ncbi.nlm.nih.gov/articles/PMC7839780/ (retrieved 2026-10-26)
5. [S5] BMC Musculoskeletal Disorders. *The effectiveness of land based exercise compared to decompressive surgery in the management of lumbar spinal-canal stenosis: a systematic review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC3305601/ (retrieved 2026-10-26)
