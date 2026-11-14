---
schema_version: okds-ko-1.0
ko_id: KO-TRAUMA-COND-003
title: Osteoporotic Fracture
preferred_term: Osteoporotic Fracture
alternate_terms:
- fragility fracture
- osteoporosis-related fracture
ko_type: Condition
specialty: TRAUMA
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: An osteoporotic fracture is a broken bone that happens because osteoporosis has made the bone
  weak [S1][S5]. These breaks are most common in the hip, the spine, and the wrist [S1]. Having one such
  fracture raises the chance of another [S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- osteoporosis
- fragility fracture
- weak bones
- bone density
- falls
- older adults
- hip fracture
- wrist fracture
- spine fracture
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-TRAUMA-COND-001
  target_label: Hip Fracture
  source_ids:
  - S1
  - S3
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-TRAUMA-COND-002
  target_label: Distal Radius Fracture
  source_ids:
  - S1
  - S5
- predicate: PREREQUISITE_FOR
  target_id: KO-TRAUMA-PROC-001
  target_label: Open Reduction and Internal Fixation
  source_ids:
  - S2
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-TRAUMA-TRT-001
  target_label: Cast Immobilization
  source_ids:
  - S2
  - S4
proposed_concepts:
- term: Osteoporosis
  suggested_type: Condition
  predicate: HAS_RISK_FACTOR
  reason: S1 and S5 describe osteoporosis as the bone disease behind these fractures; it needs its own
    KO (or a Concept KO so HAS_RISK_FACTOR can be used).
- term: Bone density scan
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S1 says a bone density scan is the usual test for osteoporosis.
- term: Fracture risk assessment tool (FRAX)
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: S1 describes a short questionnaire that estimates 10-year fracture risk; S3 is a study to update
    FRAX.
- term: Vertebral (spine) fracture
  suggested_type: Condition
  predicate: CONTRASTS_WITH
  reason: S1 names spine vertebrae as one of the most common sites; no spine fracture KO exists.
- term: Nonunion (bone that does not heal)
  suggested_type: Condition
  predicate: COMPLICATION_OF
  reason: S5 reviews whether osteoporosis raises the risk of nonunion or slow healing.
- term: Fall prevention
  suggested_type: Concept
  predicate: PREREQUISITE_FOR
  reason: S1, S2, and S4 stress falls as a cause and fall prevention as a way to prevent fractures.
sources:
- id: S1
  title: Osteoporosis
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/osteoporosis.html
  source_type: government_health_page
  audience: patient
  publication_date: '2025-09-30'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:osteoporosis). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
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
  title: 'Previous fracture and subsequent fracture risk: A meta-analysis to update FRAX'
  publisher: 'Osteoporosis international : a journal established as result of cooperation between the
    European Foundation for Osteoporosis and the National Osteoporosis Foundation of the USA'
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7615305/
  source_type: journal_article
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC7615305). Licence: CC BY'
- id: S4
  title: Biomechanics of Osteoporotic Fracture Fixation
  publisher: Current Osteoporosis Reports
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6944651/
  source_type: journal_article
  audience: clinician
  publication_date: '2019'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC6944651). Licence: CC BY'
- id: S5
  title: The effect of osteoporosis and its treatment on fracture healing a systematic review of animal
    and clinical studies
  publisher: Bone Reports
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8379440/
  source_type: journal_article
  audience: clinician
  publication_date: '2021'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC8379440). Licence: CC BY'
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
  - No source in this pack defines 'fragility fracture' or 'osteoporotic fracture' in plain words (for
    example, a break from a fall from standing height). The KO's definition is built from S1 and S5; a
    clinician should confirm it.
  - S4 says 69 percent of hip fractures are 'spontaneous'; this figure was left out because its meaning
    is unclear for patients. Check whether it should be added.
  - S5 includes mostly animal studies on healing; the KO says clinical evidence is limited. Confirm wording.
  - Medicines for osteoporosis are named only by type (bone-loss slowing, bone-building); no doses are
    given by design.
  - Osteoporosis itself is not in the registry, so the key link to the underlying disease is only a proposed
    concept.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus shows a new 'last updated' date on the Osteoporosis or Fractures page.
- The U.S. Preventive Services Task Force updates its osteoporosis screening advice.
- FRAX is updated using the previous-fracture data described in S3.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
An osteoporotic fracture is a broken bone that happens because osteoporosis has made the bone weak and easy to break [S1][S5]. These breaks can happen in any bone, but they are most common in the hip, the spine, and the wrist [S1]. Osteoporosis often has no symptoms, so a broken bone may be the first sign of it [S1]. Having one fracture raises the chance of having another [S3].

## Key Facts (claim → source)
- Osteoporosis is a disease in which bones become weak and are likely to break [S1].
- Osteoporosis is called a "silent" disease because it usually causes no symptoms until a bone breaks [S1].
- These fractures are most common in the hip, the bones of the spine (vertebrae), and the wrist [S1].
- People who have had a fracture have almost twice the risk of another fracture compared with people who have not [S3].
- This higher risk after a fracture is similar in men and women [S3].
- Osteoporotic bone tends to break into more and smaller pieces, which can make the break harder to fix [S4].
- Weak bone holds metal screws and plates less well, so implants can loosen or fail [S4][S5].
- The number of osteoporotic fractures is expected to reach about 18 million worldwide by 2040 [S5].

## Explanation
### What it is
Bones are living tissue, and the body keeps breaking down old bone and replacing it with new bone [S1]. Osteoporosis happens when more bone is broken down than replaced, so bones lose mass and become weak [S1]. An osteoporotic fracture is a break in one of these weak bones [S1][S5]. Any bone can break, but the hip, the spine, and the wrist are the most common places [S1]. Low bone density and osteoporosis make a person much more likely to break a bone [S2].

### Causes and risk factors
The risk factors for osteoporosis include [S1]:
- Being a woman, especially after menopause [S1].
- Getting older, with osteoporosis most common after age 50 [S1].
- Being slim and thin-boned [S1].
- Having a parent with osteoporosis or a parent who broke a hip [S1].
- A diet low in calcium, vitamin D, or protein [S1].
- Long-term use of some medicines, such as corticosteroids (steroid medicines) [S1].
- Smoking, heavy drinking over a long time, or not being active [S1].

A past fracture is itself a strong risk factor for another fracture [S3]. Falls also matter: with age, poorer balance, coordination, and vision raise the chance of falling [S4].

### Symptoms
Osteoporosis usually does not cause symptoms, and many people do not know they have it until a bone breaks [S1]. When a bone breaks, signs can include strong pain, a limb that looks out of place, swelling, bruising, and trouble moving the injured part [S2]. A health care provider may also check for loss of height or changes in posture [S1].

### How it is diagnosed
A provider asks about the injury and does a physical exam, and will likely order an x-ray or other imaging to see if a bone is broken [S2]. To find osteoporosis, a provider asks about past broken bones and will likely order a bone density scan [S1]. A fracture risk assessment is a short questionnaire that estimates the chance of breaking a bone in the next 10 years [S1]. Large studies show that a past fracture should be counted in these risk tools, since it adds risk beyond bone density alone [S3]. Screening is advised for women 65 and older and for younger women after menopause who have risk factors [S1].

### Treatment options
- **Treating the break:** the most common treatment for a fracture is a cast or splint to keep the bone still while it heals [S2]. Some breaks need surgery with plates, pins, or screws [S2][S4].
- **Surgery in weak bone:** older adults do much better when they can get up and move soon after a fracture, so surgeons aim for a fixation strong enough to bear weight right away [S4]. Newer implants and ways to reinforce them can help with this [S4].
- **Healing:** some studies suggest osteoporosis may slow healing, but strong evidence in people is still lacking [S5].
- **Treating osteoporosis:** the goals are to slow or stop bone loss and prevent more fractures [S1]. This can include a healthy diet with calcium, vitamin D, and protein, weight-bearing and balance exercise, quitting smoking, limiting alcohol, fall prevention, and medicines that slow bone loss or help rebuild bone [S1].
- **Medicines and healing:** one review found no clear harm to fracture healing from common osteoporosis medicines [S5].

### When to seek care
If you think you may have broken a bone, get medical care right away [S2]. After a fracture, it is worth asking about osteoporosis testing and treatment, because one fracture raises the chance of another [S1][S3].

## Common Misunderstandings
- **Myth:** You would feel it if your bones were getting weak. **Fact:** Osteoporosis usually causes no symptoms until a bone breaks [S1].
- **Myth:** After one broken bone heals, the risk is over. **Fact:** A past fracture nearly doubles the risk of another fracture [S3].
- **Myth:** Only women get osteoporotic fractures. **Fact:** Osteoporosis is more common in women, but men get it too, and the extra risk after a fracture is similar in men and women [S1][S3].
- **Myth:** Weak bones cannot be helped. **Fact:** Diet, exercise, fall prevention, and medicines can help slow bone loss and prevent fractures [S1].

## Questions to Ask Your Doctor
1. Could this broken bone be a sign of osteoporosis?
2. Should I have a bone density scan or a fracture risk assessment?
3. What can I do to lower my chance of another fracture?
4. How can I make my home safer to prevent falls?
5. Would treatment for osteoporosis make sense for me?

## Test Questions
1. Why is osteoporosis called a "silent" disease? - It usually has no symptoms until a bone breaks [S1].
2. Name the three most common places for osteoporotic fractures. - The hip, the spine (vertebrae), and the wrist [S1].
3. How does a past fracture change the risk of another fracture? - It almost doubles the risk [S3].
4. What test is usually used to check for osteoporosis? - A bone density scan [S1].
5. Why can surgery be harder in osteoporotic bone? - The bone breaks into more pieces and holds screws and plates less well [S4][S5].
6. Name two ways to help prevent fractures. - Examples: enough calcium and vitamin D, weight-bearing exercise, and preventing falls [S1][S2].

## Related Topics
- Read next: Hip Fracture (KO-TRAUMA-COND-001), Distal Radius Fracture (KO-TRAUMA-COND-002), Open Reduction and Internal Fixation (KO-TRAUMA-PROC-001), Cast Immobilization (KO-TRAUMA-TRT-001)
- Proposed new topics: Osteoporosis (condition), Bone density scan (diagnostic test), FRAX fracture risk tool (outcome measure), Vertebral fracture (condition), Nonunion (condition), Fall prevention (concept)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Osteoporosis.* https://medlineplus.gov/osteoporosis.html (retrieved 2026-10-26)
2. [S2] MedlinePlus, U.S. National Library of Medicine. *Fractures.* https://medlineplus.gov/fractures.html (retrieved 2026-10-26)
3. [S3] Osteoporosis international : a journal established as result of cooperation between the European Foundation for Osteoporosis and the National Osteoporosis Foundation of the USA. *Previous fracture and subsequent fracture risk: A meta-analysis to update FRAX.* https://pmc.ncbi.nlm.nih.gov/articles/PMC7615305/ (retrieved 2026-10-26)
4. [S4] Current Osteoporosis Reports. *Biomechanics of Osteoporotic Fracture Fixation.* https://pmc.ncbi.nlm.nih.gov/articles/PMC6944651/ (retrieved 2026-10-26)
5. [S5] Bone Reports. *The effect of osteoporosis and its treatment on fracture healing a systematic review of animal and clinical studies.* https://pmc.ncbi.nlm.nih.gov/articles/PMC8379440/ (retrieved 2026-10-26)
