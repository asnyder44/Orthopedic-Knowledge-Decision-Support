---
schema_version: okds-ko-1.0
ko_id: KO-SPINE-PROC-001
title: Spinal Fusion
preferred_term: Spinal Fusion
alternate_terms:
- lumbar fusion
- spinal arthrodesis
- posterior spinal fusion
- anterior spinal fusion
- decompression plus fusion
ko_type: Procedure
specialty: SPINE
cluster: 5
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Spinal fusion is surgery that joins two or more bones of the spine (vertebrae) together [S1].
  It is used to help straighten severe scoliosis curves and is sometimes added to decompression surgery
  for lumbar spinal stenosis [S1][S2]. Studies in people with spinal stenosis found that adding fusion
  to decompression was not more effective than decompression alone [S2][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- spine surgery
- scoliosis surgery
- lumbar spinal stenosis
- spondylolisthesis
- rods and screws
- rehabilitation after surgery
relationships:
- predicate: TREATS
  target_id: KO-SPINE-COND-003
  target_label: Adolescent Idiopathic Scoliosis
  source_ids:
  - S1
  - S4
- predicate: TREATS
  target_id: KO-SPINE-COND-001
  target_label: Lumbar Spinal Stenosis
  source_ids:
  - S2
  - S3
proposed_concepts:
- term: Decompression surgery (laminectomy)
  suggested_type: Procedure
  predicate: ALTERNATIVE_TO
  reason: S2 and S3 compare decompression alone with decompression plus fusion for lumbar spinal stenosis.
- term: Pedicle screws and rods (spinal instrumentation)
  suggested_type: Device
  predicate: USES_DEVICE
  reason: S1 says metal rods and screws hold the spine straight while it heals; S4 describes pedicle screw-based
    systems.
- term: Rehabilitation after lumbar spine surgery
  suggested_type: RehabProtocol
  predicate: FOLLOWED_BY
  reason: S5 reviews supervised exercise and other rehabilitation after lumbar surgery.
- term: Vertebral body tethering
  suggested_type: Procedure
  predicate: ALTERNATIVE_TO
  reason: S4 describes tethering as a growth-guiding option that aims to avoid fusion in some younger
    AIS patients.
- term: Adjacent segment degeneration
  suggested_type: Condition
  predicate: COMPLICATION_OF
  reason: S4 says it is the most common long-term mechanical complication after long fusions.
- term: Oswestry Disability Index (ODI)
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: S3, S4, and S5 use the ODI to measure results after spine surgery.
sources:
- id: S1
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
- id: S2
  title: 'Effectiveness of Surgery for Lumbar Spinal Stenosis: A Systematic Review and Meta-Analysis'
  publisher: PLoS ONE
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4378944/
  source_type: journal_article
  audience: clinician
  publication_date: '2015'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC4378944). Licence: CC BY'
- id: S3
  title: Decompression alone or fusion in single-level lumbar spinal stenosis with spondylolisthesis?
    A systematic review and meta analysis
  publisher: BMC Musculoskeletal Disorders
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11386329/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC11386329). Licence: CC BY'
- id: S4
  title: 'Long-term outcomes of spinal fusion in adolescent idiopathic scoliosis: a literature review'
  publisher: European Journal of Medical Research
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11536752/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC11536752). Licence: CC BY'
- id: S5
  title: 'Rehabilitation after lumbar spine surgery in adults: a systematic review with meta-analysis'
  publisher: Archives of Physiotherapy
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10578022/
  source_type: journal_article
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC10578022). Licence: CC BY'
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
  - No patient-level page on spinal fusion itself was found in the local dataset; S1 (NIAMS scoliosis)
    is the only patient page and covers fusion only briefly. Consider adding a MedlinePlus or NIAMS page
    on spinal fusion or back surgery.
  - The pack does not describe step-by-step how fusion is done (incision, bone graft, anesthesia, hospital
    stay). The How it is done section is limited to what S1, S3, and S4 say. Clinician check.
  - No source gives a recovery timeline (time in hospital, return to school, work, or sports). The Recovery
    timeline section says so.
  - The original automatic pack for this KO held off-topic papers; all five were replaced.
  - S2 and S3 study lumbar spinal stenosis; S4 studies AIS. Their findings should not be applied across
    conditions. S3 found decompression alone not inferior even with single-level spondylolisthesis, but
    it notes earlier trials disagreed.
  - S4 says long-term data on AIS fusion are of low quality.
  - MeSH ID and ICD-10-CM code are not stated in any source and remain <verify>.
  - Plain-language definitions (e.g., vertebrae, spondylolisthesis, adjacent segment degeneration, junctional
    kyphosis, interbody and posterolateral fusion) were written by the drafter; check they match the sources.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- A new systematic review or trial compares decompression alone with decompression plus fusion.
- NIAMS updates its scoliosis page, or new long-term outcome data on spinal fusion for AIS are published.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Spinal fusion is surgery that joins two or more bones of the spine (vertebrae) together [S1]. It is used to help straighten scoliosis curves that keep getting worse [S1][S4]. Surgeons sometimes add it to decompression surgery for lumbar spinal stenosis, but studies found that adding fusion was not more effective than decompression alone [S2][S3]. Supervised exercise after lumbar spine surgery may help with pain and daily function [S5].

## Key Facts (claim → source)
- Spinal fusion joins two or more vertebrae so they heal together [S1].
- In scoliosis, fusion can help straighten the curve, and metal rods and screws often hold the spine straight while it heals [S1].
- For lumbar spinal stenosis, a review of trials found decompression plus fusion was not better than decompression alone for pain, disability, or walking [S2].
- Adding fusion has been linked to more repeat surgeries, complications, and costs than decompression alone [S2].
- In people with stenosis and a slipped vertebra at one level, decompression alone took less time in surgery and caused less blood loss than adding fusion [S3].
- After long fusions for AIS, wear of the spine segments next to the fusion is the most common long-term mechanical problem [S4].
- Supervised exercise after lumbar surgery may reduce pain and disability, but the evidence is of low quality [S5].

## Explanation
### What it is
Spinal fusion is an operation that joins two or more vertebrae, the bones of the spine, together [S1]. Fusion reduces the number of moving segments in the spine, which changes how the spine works mechanically [S4]. In research papers, fusion is also called arthrodesis [S3].

### Why it is done
- **Scoliosis:** if a child or teen is still growing and the curve keeps getting worse, a doctor may recommend surgery such as spinal fusion [S1]. In AIS, surgery aims to correct the curve, balance the trunk, even out the shoulders and waist, and fix the twist of the spine [S4].
- **Lumbar spinal stenosis:** when non-surgical care has not helped, people with stenosis are often referred for surgery [S2]. Because the spine can become unstable after decompression (surgery to take pressure off the nerves), fusion has been recommended for some patients [S2].
- **Stenosis with spondylolisthesis:** spondylolisthesis is when one vertebra shifts forward on the one below it [S3]. In some regions, decompression with fusion makes up more than 90 out of 100 operations for this problem [S3].

### How it is done
The type of surgery depends on where the curve is and how severe it is [S1]. For scoliosis, fusion can be done from the back (posterior fusion), from the front (anterior fusion), or both [S4]. In lumbar surgery, fusion is added to a decompression, and it can be done between the vertebral bodies (interbody fusion) or along the side and back of the spine (posterolateral fusion) [S3]. The sources here do not describe the steps of the operation in detail; ask the surgeon how it would be done.

### Devices used
The surgeon may use metal rods and screws to keep the spine straight while it heals [S1]. Today's systems for AIS use screws placed in the vertebrae (pedicle screws) that allow the curve to be corrected in three dimensions [S4]. Older Harrington rods often caused problems and corrected the curve in only one direction [S4].

### Risks
All surgeries carry a risk of complications [S1]. Known risks and downsides of spinal fusion include:
- More repeat surgeries, more complications after surgery, and higher costs than decompression alone in spinal stenosis [S2].
- Longer surgery and more blood loss than decompression alone in single-level stenosis with spondylolisthesis [S3].
- Wear and tear of the spine segments next to the fusion (adjacent segment degeneration), and new forward bending of the spine above or below the fusion (junctional kyphosis) [S4].
- Slightly higher rates of cesarean birth in later pregnancies after scoliosis fusion [S4].

Spine surgery in the lower back can also lead to muscle weakness, stiffness, and fear of moving [S5].

### Recovery timeline
The sources in this pack do not give a timeline for recovery, such as hospital stay or return to school, work, or sports; ask the surgical team. Rehabilitation after lumbar surgery aims to ease pain, restore function, help people return to work, and prevent long-term pain [S5]. A review found supervised exercise may improve pain and disability after lumbar surgery, but the evidence is low in quality [S5]. Over 15 or more years, results after AIS fusion appear satisfactory, but they fall short of people without scoliosis [S4].

### Alternatives
- **Decompression alone:** for lumbar spinal stenosis, decompression without fusion worked about as well as decompression plus fusion in a review of trials [S2]. A second review found decompression alone was not worse in single-level stenosis with spondylolisthesis [S3].
- **Non-surgical care for stenosis:** physical therapy, medicines, or acupuncture can ease symptoms to some degree [S3].
- **Bracing and observation for scoliosis:** milder curves may only need check-ups, and moderate curves in growing children may be treated with a brace [S1].
- **Growth-friendly surgery for scoliosis:** an expandable rod can be lengthened as a child grows [S1]. Tethering systems aim to keep the spine moving and avoid fusion in some younger teens [S4].

## Common Misunderstandings
- **Myth:** Adding a fusion always makes back surgery for stenosis work better. **Fact:** A review of trials found decompression plus fusion was not more effective than decompression alone [S2][S3].
- **Myth:** Fusion is the first treatment for scoliosis. **Fact:** Many children need only check-ups or a brace; surgery is for curves that keep getting worse [S1].
- **Myth:** Once a fusion heals, there are no long-term effects. **Fact:** Wear of the spine segments next to a long fusion is a known long-term problem [S4].
- **Myth:** Rehabilitation does not matter after spine surgery. **Fact:** Supervised exercise may improve pain and disability after lumbar surgery, though more research is needed [S5].

## Questions to Ask Your Doctor
1. Why do you recommend fusion for me (or my child), and what would happen without it?
2. Would decompression alone, a brace, or another option work instead?
3. Which levels of my spine would be fused, and what devices would you use?
4. What are the main risks for me, including the chance of another surgery?
5. What will recovery and rehabilitation look like, and how long will it take?

## Test Questions
1. What does spinal fusion do? - It joins two or more vertebrae together [S1].
2. Why are metal rods and screws used in scoliosis fusion? - To keep the spine straight while it heals [S1].
3. In lumbar spinal stenosis, was decompression plus fusion better than decompression alone in a review of trials? - No, it was not more effective [S2].
4. What is the most common long-term mechanical problem after long fusions for AIS? - Wear of the spine segments next to the fusion (adjacent segment degeneration) [S4].
5. What kind of rehabilitation may help after lumbar spine surgery? - Supervised exercise [S5].

## Related Topics
- Treats: Adolescent Idiopathic Scoliosis (KO-SPINE-COND-003), Lumbar Spinal Stenosis (KO-SPINE-COND-001)
- Proposed topics (not yet in the library): decompression surgery (laminectomy), pedicle screws and rods, rehabilitation after lumbar spine surgery, vertebral body tethering, adjacent segment degeneration, Oswestry Disability Index

## References
1. [S1] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Scoliosis in Children and Teens.* https://www.niams.nih.gov/health-topics/scoliosis (retrieved 2026-10-26)
2. [S2] PLoS ONE. *Effectiveness of Surgery for Lumbar Spinal Stenosis: A Systematic Review and Meta-Analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC4378944/ (retrieved 2026-10-26)
3. [S3] BMC Musculoskeletal Disorders. *Decompression alone or fusion in single-level lumbar spinal stenosis with spondylolisthesis? A systematic review and meta analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC11386329/ (retrieved 2026-10-26)
4. [S4] European Journal of Medical Research. *Long-term outcomes of spinal fusion in adolescent idiopathic scoliosis: a literature review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC11536752/ (retrieved 2026-10-26)
5. [S5] Archives of Physiotherapy. *Rehabilitation after lumbar spine surgery in adults: a systematic review with meta-analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10578022/ (retrieved 2026-10-26)
