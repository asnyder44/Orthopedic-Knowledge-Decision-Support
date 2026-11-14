---
schema_version: okds-ko-1.0
ko_id: KO-SPINE-COND-001
title: Lumbar Spinal Stenosis
preferred_term: Lumbar Spinal Stenosis
alternate_terms:
- spinal stenosis
- neurogenic claudication
- lumbar spinal canal stenosis
- LSS
- degenerative lumbar spinal stenosis
ko_type: Condition
specialty: SPINE
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Lumbar spinal stenosis is a narrowing of the spaces inside the lower spine that puts pressure
  on the spinal cord and nerve roots [S2][S3]. It most often affects people older than 50 and can cause
  low back pain and pain, numbness, or weakness in the legs that gets worse with standing or walking [S1][S2].
  Treatment options include medicines, physical therapy, braces, and surgery [S1].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- lower back
- spine
- leg pain
- nerve compression
- pain with walking
- older adults
- decompression surgery
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-SPINE-TRT-001
  target_label: Physical Therapy for Low Back Pain
  source_ids:
  - S1
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-SPINE-PROC-001
  target_label: Spinal Fusion
  source_ids:
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-SPINE-COND-002
  target_label: Lumbar Disc Herniation
  source_ids:
  - S2
proposed_concepts:
- term: Lumbar spine (spinal canal and nerve roots)
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S2 describes the spinal canal, nerve roots, and lumbar region narrowed in stenosis; no spine
    anatomy KO is in the registry.
- term: Decompression surgery (laminectomy)
  suggested_type: Procedure
  predicate: PREREQUISITE_FOR
  reason: S3 calls bony decompression by laminectomy the gold-standard surgery for lumbar spinal stenosis,
    and S4 compares it with exercise.
- term: Spinal MRI
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S1 says imaging tests are used to diagnose stenosis, and S4 describes diagnosis by MRI/CT plus
    symptoms.
- term: Neurogenic claudication
  suggested_type: Concept
  predicate: HAS_SYMPTOM
  reason: S3 defines it as leg pain during walking or standing that eases when bending forward; needs
    a Concept KO.
- term: Oswestry Disability Index (ODI)
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: S3 and S4 use the ODI to measure disability in people with lumbar spinal stenosis.
- term: Spondylolisthesis
  suggested_type: Condition
  predicate: PREREQUISITE_FOR
  reason: S2 lists a vertebra slipping forward as a cause of stenosis.
sources:
- id: S1
  title: Spinal Stenosis
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/spinalstenosis.html
  source_type: government_health_page
  audience: patient
  publication_date: '2025-09-24'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:spinalstenosis). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
- id: S2
  title: Spinal Stenosis
  publisher: National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH)
  url: https://www.niams.nih.gov/health-topics/spinal-stenosis
  source_type: government_health_page
  audience: patient
  publication_date: '2023-11-01'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (niams:spinal-stenosis). Licence: Public domain (U.S. federal government
    work, NIH/NIAMS); credit NIAMS'
- id: S3
  title: 'Effectiveness of Surgery for Lumbar Spinal Stenosis: A Systematic Review and Meta-Analysis'
  publisher: PLoS ONE
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4378944/
  source_type: journal_article
  audience: clinician
  publication_date: '2015'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC4378944). Licence: CC BY'
- id: S4
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
  - The NIAMS text in this pack (S2) stops after the physical exam section, so imaging and treatment details
    come only from S1, S3, and S4. Consider adding the NIAMS treatment page.
  - No source in this pack gives explicit "when to seek care" or emergency advice; the KO lists the severe
    signs S2 names (bowel, bladder, sexual function problems) and tells readers to ask a clinician. Clinician
    check needed.
  - S3 (2015) and S4 (2012) are older reviews; S4 rests on only one head-to-head trial of exercise versus
    surgery. Check for newer evidence.
  - MeSH ID and ICD-10-CM code are not stated in any source and remain <verify>.
  - Plain-language definitions of terms (e.g., ligaments, dural tears, laminectomy) were written by the
    drafter; check they match the sources.
  - No spine anatomy, imaging, or outcome-measure KOs exist in the registry, so AFFECTS, DIAGNOSED_BY,
    and MEASURED_BY links were proposed instead.
  - The link to Lumbar Disc Herniation is PREREQUISITE_FOR because S2 names a bulging disk as one cause
    of stenosis; confirm this link type.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus or NIAMS shows a new 'last updated' or 'last reviewed' date on a cited spinal stenosis page.
- A new systematic review or guideline compares surgery and non-surgical care for lumbar spinal stenosis.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Lumbar spinal stenosis is a narrowing of the spaces inside the lower spine that puts pressure on the spinal cord and nerve roots [S2][S3]. It most often affects people older than 50 and can cause low back pain and pain, numbness, or weakness in the legs that gets worse with standing or walking [S1][S2]. Doctors diagnose it with a physical exam and imaging tests [S1]. Treatment options include medicines, physical therapy, braces, and surgery [S1].

## Key Facts (claim → source)
- Spinal stenosis is a narrowing of spaces in the spine that presses on the spinal cord and nerve roots [S1][S2].
- It happens mostly in people older than 50, and the chance of getting it goes up with age [S1][S2].
- Age-related wear in the spine is the most common cause [S2].
- Leg pain, numbness, or cramping often gets worse with standing or walking and better with sitting or bending forward [S2][S3].
- Diagnosis uses a health history, a physical exam, and imaging tests [S1][S2].
- In one review, surgery improved function more than a land-based exercise program, but the authors still advised trying exercise first because the condition changes slowly and surgery has risks [S4].
- A review of trials found that adding spinal fusion to decompression surgery was not more effective than decompression alone [S3].

## Explanation
### What it is
Your spine protects your spinal cord, a bundle of nerves that runs from the base of the brain down the center of the backbone [S1][S2]. Nerve roots branch off the cord and leave the spine through small openings [S2]. In spinal stenosis, the spaces the cord and nerves pass through become narrow, which puts pressure on them [S1][S2]. "Lumbar" means the lower back, and the lumbar spine and the neck are where stenosis most often develops [S2]. The narrowing can be caused by bone and soft tissue around the spinal canal [S3].

### Causes and risk factors
The narrowing usually happens slowly over time [S2]. Causes include:
- **Age-related changes**, the most common cause: ligaments (bands of tissue that hold the spine bones in place) can thicken and harden, and bone spurs can grow [S2].
- **A bulging (herniated) disk**, where a cushion between the spine bones dries out, cracks, and bulges [S2].
- **Spondylolisthesis**, when one spine bone slips forward on another [S2].
- **Arthritis**, such as osteoarthritis or, less often, rheumatoid arthritis [S2].
- **Other conditions**, such as spine tumors, fractures, or Paget's disease of bone [S2].
- **Conditions present from birth**, such as a narrow spinal canal or scoliosis (a sideways curve of the spine) [S1][S2].

Spinal stenosis occurs mostly in people older than 50 [S1]. Younger people can get it if they have a spine injury or were born with a narrow spinal canal [S1][S2]. One review notes that in people aged 60 to 69, almost half show signs of stenosis on scans [S4].

### Symptoms
Symptoms often start and get worse slowly, and some people have none [S1][S2]. In the lower back, symptoms can include [S2]:
- Low back pain.
- Burning pain or aching that spreads down the buttocks and into the legs.
- Numbness, tingling, or cramping in the legs and feet.
- Weakness in the legs and feet.

Standing, walking, or bending backward can make symptoms worse, while sitting or bending forward may ease them [S2]. Bending forward opens up the spaces at the back of the spine [S2]. Doctors call leg pain that comes with walking or standing and eases with bending forward "neurogenic claudication" [S3]. People with more severe stenosis may have problems with bowel, bladder, or sexual function [S2].

### How it is diagnosed
Doctors diagnose spinal stenosis with a physical exam and imaging tests [S1]. They ask where the pain is, what it feels like, and when it began [S2]. The exam may check how far you can move, whether bending backward brings on pain or bending forward eases it, and your feeling, strength, reflexes, balance, and walking [S2]. Research studies often confirm stenosis with MRI or CT scans along with the person's symptoms [S4]. Scans and symptoms do not always match well [S4].

### Treatment options
Treatments include medicines, physical therapy, braces, and surgery [S1].
- **Exercise and physical therapy:** exercise aims to improve how the spine bends and moves, and it can be continued at home [S4]. Exercise programs showed early gains in function in the studies one review looked at [S4].
- **Surgery:** when other treatment has not helped, people are often referred for surgery [S3]. The standard operation is called bony decompression by laminectomy, which aims to take pressure off the nerves in the spinal canal [S3]. Some surgeons also add spinal fusion, but a review of trials found that this was not more helpful than decompression alone and can mean more repeat surgeries, complications, and costs [S3].

One review found surgery gave larger and longer-lasting gains in function than exercise over two years [S4]. Because the condition changes slowly and surgery has known risks, such as dural tears (tears in the thin covering around the nerves), the authors suggested trying exercise before surgery [S4].

### When to seek care
The sources in this pack do not give specific advice on when to see a doctor. They note that more severe stenosis can affect bowel, bladder, or sexual function [S2]. Leg numbness, weakness, or pain that spreads down the leg are also listed as symptoms [S1][S2]. Ask a health care provider about any of these symptoms and about which ones need urgent care.

## Common Misunderstandings
- **Myth:** Spinal stenosis only happens to older adults. **Fact:** It is most common after 50, but younger people with a spine injury or a narrow canal from birth can also get it [S1][S2].
- **Myth:** If scans show stenosis, you must have symptoms. **Fact:** Some people have no symptoms, and scan findings and symptoms often do not match well [S2][S4].
- **Myth:** Adding a spinal fusion always makes stenosis surgery work better. **Fact:** A review of trials found fusion plus decompression was not more effective than decompression alone [S3].
- **Myth:** Exercise is pointless for spinal stenosis. **Fact:** Exercise programs showed early gains, and one review advised trying exercise before surgery [S4].

## Questions to Ask Your Doctor
1. Is my leg or back pain caused by spinal stenosis, or could it be something else?
2. Do I need an imaging test, and what will it show?
3. Could physical therapy or an exercise program help me before we talk about surgery?
4. If I need surgery, would decompression alone be enough, or would I need a fusion too?
5. Which symptoms should make me call you right away?

## Test Questions
1. What happens in spinal stenosis? - Spaces in the spine narrow and press on the spinal cord and nerve roots [S1][S2].
2. What is the most common cause of spinal stenosis? - Age-related changes in the spine [S2].
3. What position often eases leg symptoms of lumbar spinal stenosis? - Sitting or bending forward [S2].
4. How do doctors diagnose spinal stenosis? - With a health history, a physical exam, and imaging tests [S1][S2].
5. Did adding fusion to decompression surgery work better in the trials one review studied? - No, it was not more effective than decompression alone [S3].

## Related Topics
- Read next: Physical Therapy for Low Back Pain (KO-SPINE-TRT-001), Spinal Fusion (KO-SPINE-PROC-001), Lumbar Disc Herniation (KO-SPINE-COND-002)
- Proposed topics (not yet in the library): lumbar spine anatomy, decompression surgery (laminectomy), spinal MRI, neurogenic claudication, Oswestry Disability Index, spondylolisthesis

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Spinal Stenosis.* https://medlineplus.gov/spinalstenosis.html (retrieved 2026-10-26)
2. [S2] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Spinal Stenosis.* https://www.niams.nih.gov/health-topics/spinal-stenosis (retrieved 2026-10-26)
3. [S3] PLoS ONE. *Effectiveness of Surgery for Lumbar Spinal Stenosis: A Systematic Review and Meta-Analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC4378944/ (retrieved 2026-10-26)
4. [S4] BMC Musculoskeletal Disorders. *The effectiveness of land based exercise compared to decompressive surgery in the management of lumbar spinal-canal stenosis: a systematic review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC3305601/ (retrieved 2026-10-26)
