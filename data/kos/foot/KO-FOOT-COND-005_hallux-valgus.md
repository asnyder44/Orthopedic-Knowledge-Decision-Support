---
schema_version: okds-ko-1.0
ko_id: KO-FOOT-COND-005
title: Hallux Valgus
preferred_term: Hallux Valgus
alternate_terms:
- bunion
- HV
- bunion deformity
ko_type: Condition
specialty: FOOT
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Hallux valgus is a common foot deformity in which the big toe leans toward the other toes,
  causing a bony bump, called a bunion, at the big toe joint [S1][S2]. It is more common in women and
  in older people, and it can cause foot pain and trouble with shoes [S3][S4]. Treatment starts with
  shoe changes and pads, and surgery may be considered if these do not help [S2].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- bunion
- big toe
- forefoot
- foot deformity
- footwear
- first metatarsophalangeal joint
relationships: []
proposed_concepts:
- term: First metatarsophalangeal (MTP) joint / big toe joint
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S1, S2 and S4 place the deformity and pain at the big toe joint; no foot anatomy KO is in the
    registry.
- term: Foot X-ray (hallux valgus angles)
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S5 says X-ray measurements are often used, especially before surgery; S4 defines hallux valgus
    by an X-ray angle over 15 degrees.
- term: Manchester Scale
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: S5 describes the Manchester Scale as a simple, validated way to grade hallux valgus severity.
- term: Bunion surgery (osteotomy, soft tissue balancing, joint fusion)
  suggested_type: Procedure
  predicate: PREREQUISITE_FOR
  reason: S2 describes surgery for people who do not improve with non-surgical care.
- term: Footwear modification, toe pads and spacers
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S2 lists shoe changes, toe pads and positioning devices as non-surgical treatment.
sources:
- id: S1
  title: Foot Injuries and Disorders
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/footinjuriesanddisorders.html
  source_type: government_health_page
  audience: patient
  publication_date: '2026-07-11'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:footinjuriesanddisorders). Licence: Public domain (NLM-authored
    MedlinePlus summary); credit MedlinePlus'
- id: S2
  title: Hallux Valgus
  publisher: Foot & ankle orthopaedics
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8696753/
  source_type: journal_article
  audience: clinician
  publication_date: '2019'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via europepmc, openaire. Licence: cc by-nc. Type: review. Text kept: abstract only.'
- id: S3
  title: 'Prevalence of hallux valgus in the general population: a systematic review and meta-analysis'
  publisher: Journal of foot and ankle research
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2955707/
  source_type: systematic_review
  audience: clinician
  publication_date: '2010'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: systematic review. Text kept: abstract only.'
- id: S4
  title: 'Foot pain and functional limitation in healthy adults with hallux valgus: a cross-sectional
    study'
  publisher: BMC musculoskeletal disorders
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3526426/
  source_type: journal_article
  audience: clinician
  publication_date: '2012'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: article. Text kept: abstract only.'
- id: S5
  title: Radiographic correlates of hallux valgus severity in older people
  publisher: Journal of foot and ankle research
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2949715/
  source_type: journal_article
  audience: clinician
  publication_date: '2010'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: article. Text kept: abstract only.'
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
  - No registry KO is a valid link target for this Condition yet (no foot anatomy, test or treatment KOs),
    so relationships is empty; see proposed_concepts.
  - S1 (MedlinePlus Foot Injuries and Disorders) is a general page with only one line on bunions; there
    is no dedicated patient page on bunions in the dataset. Consider adding one (e.g., MedlinePlus or NIAMS).
  - All journal sources are abstract-only. S2 (Foot & Ankle Orthopaedics review) is CC BY-NC, recorded as
    link_and_paraphrase; confirm permitted use.
  - 'When to seek care: no source gives warning signs or advice on when to see a clinician; the section
    says so and uses S2/S3 facts on pain and function. Clinician check needed.'
  - 'Recovery after surgery, surgical risks and success rates are not covered by this pack; the KO makes
    no claims about them.'
  - MeSH and ICD-10-CM codes are unknown and set to verify.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- Any cited page shows a new 'last reviewed' date.
- A new clinical practice guideline or systematic review on hallux valgus treatment is published.
- Foot anatomy, imaging or bunion surgery KOs are added to the registry (add links).
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Hallux valgus is a common foot deformity in which the big toe leans toward the other toes, causing a bony bump, called a bunion, at the big toe joint [S1][S2]. It is more common in women and in older people, and it can cause foot pain and trouble with shoes [S3][S4]. Treatment starts with shoe changes and pads, and surgery may be considered if these do not help [S2].

## Key Facts (claim → source)
- A bunion is a hard, painful bump at the big toe joint [S1].
- In hallux valgus, the big toe turns toward the other toes and also rotates, and the bunion is only one part of this change in shape [S2].
- About 23% of adults aged 18 to 65 and about 36% of people over 65 have hallux valgus [S3].
- It is more common in women (about 30%) than in men (about 13%) [S3].
- Being female, getting older, tight shoes, and family history make it more likely [S2].
- People with hallux valgus report more foot pain, more trouble with shoes, and more worry about how their feet look [S4].
- Its severity can usually be seen by looking at the foot, and X-rays are often used, especially if surgery is being considered [S5].
- Non-surgical care includes education, shoe changes, toe pads, and changes in activity; surgery is an option if these do not help [S2].

## Explanation
### What it is
The big toe is also called the hallux [S2]. In hallux valgus, the big toe drifts toward the second toe and also twists, which changes the shape of the front of the foot in three directions [S2]. The bunion, the bump on the inner side of the foot at the base of the big toe, is only one part of this deformity [S1][S2]. Hallux valgus can cause a lot of pain and changes in how the big toe joint works [S2].

### Causes and risk factors
The exact cause is still debated [S2]. Factors that make it more likely include [S2]:
- Being female [S2][S3].
- Getting older [S2][S3].
- Wearing tight, narrow shoes [S1][S2].
- Having family members with bunions [S2].

Foot problems like bunions are often caused by shoes that do not fit well, and aging and being overweight also raise the chance of foot problems [S1]. One study suggests that a longer first foot bone (first metatarsal) compared with the second may help cause the deformity or make it worse [S5]. Other foot problems, such as flat feet, hammertoes, and a tight calf, often occur along with hallux valgus [S2].

### Symptoms
- A hard, painful bump at the big toe joint [S1].
- Foot pain and trouble with daily foot function [S3][S4].
- Trouble finding shoes that fit, and concern about how the foot looks [S4].
- Weaker big toe muscles and a little less steady balance [S4].

In one study, people with hallux valgus had more foot pain, but their general physical activity was not affected [S4].

### How it is diagnosed
How severe hallux valgus is can usually be seen just by looking at the foot [S5]. X-rays are often used too, especially if surgery is being considered [S5]. On X-rays, doctors measure the angles of the big toe and nearby bones [S5]. In one study, hallux valgus was defined as an X-ray angle of more than 15 degrees [S4]. The Manchester Scale is a simple, tested way to grade how severe it is [S5]. As hallux valgus gets more severe, X-rays more often show wear-and-tear arthritis in the big toe joint [S5].

### Treatment options
- **Non-surgical care:** this includes learning about the condition, changing shoes, toe pads, devices that help hold the toe in position, and changing activities [S2].
- **Surgery:** surgery may be considered when non-surgical care has not helped [S2]. The goals are to ease pain, correct the deformity, make the big toe area more stable, and improve quality of life [S2]. More than 100 different operations have been described, including balancing the soft tissues, cutting and moving a foot bone (osteotomy), and joining (fusing) a joint [S2]. The choice depends on how severe the deformity is, where it is, and the surgeon's preference [S2]. Newer methods include minimally invasive surgery [S2].

### When to seek care
The sources here do not list specific warning signs, so ask a health care provider if a bunion is painful or makes it hard to wear shoes [S1][S2]. Hallux valgus can cause a lot of pain and affect how the foot works [S2][S4].

## Common Misunderstandings
- **Myth:** A bunion is just a bump that grows on the side of the foot. **Fact:** The bump is only one part of a change in the position of the big toe and its foot bone [S2].
- **Myth:** Bunions are rare. **Fact:** About 23% of adults aged 18 to 65 and about 36% of people over 65 have hallux valgus [S3].
- **Myth:** Surgery is the first and only treatment. **Fact:** Non-surgical care such as shoe changes and toe pads comes first, and surgery is considered if it does not help [S2].
- **Myth:** There is one standard bunion operation. **Fact:** More than 100 different procedures have been described, and the choice depends on the deformity [S2].

## Questions to Ask Your Doctor
1. How severe is my hallux valgus, and do I need an X-ray?
2. What kinds of shoes, pads, or devices could help my foot?
3. Are there activities I should change?
4. When would surgery be worth considering for me, and what type would fit my foot?
5. Is there arthritis in my big toe joint?

## Test Questions
1. What is a bunion? - A hard, painful bump at the big toe joint [S1].
2. Who is more likely to have hallux valgus? - Women and older people [S2][S3].
3. Name one non-surgical treatment. - Examples: shoe changes, toe pads, positioning devices, or changes in activity [S2].
4. How is the severity of hallux valgus often checked? - By looking at the foot, and with X-ray measurements, especially before surgery [S5].
5. What problems did people with hallux valgus report in one study? - More foot pain, trouble with shoes, and concern about how their feet look [S4].

## Related Topics
- No linked KOs yet: the registry has no foot anatomy, test, or treatment KOs that this Condition can link to.
- Proposed topics: First metatarsophalangeal (big toe) joint, Foot X-ray, Manchester Scale, Bunion surgery, Footwear modification and toe pads.

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Foot Injuries and Disorders.* https://medlineplus.gov/footinjuriesanddisorders.html (retrieved 2026-10-26)
2. [S2] Foot & ankle orthopaedics. *Hallux Valgus.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8696753/ (retrieved 2026-11-14)
3. [S3] Journal of foot and ankle research. *Prevalence of hallux valgus in the general population: a systematic review and meta-analysis.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2955707/ (retrieved 2026-11-14)
4. [S4] BMC musculoskeletal disorders. *Foot pain and functional limitation in healthy adults with hallux valgus: a cross-sectional study.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3526426/ (retrieved 2026-11-14)
5. [S5] Journal of foot and ankle research. *Radiographic correlates of hallux valgus severity in older people.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2949715/ (retrieved 2026-11-14)
