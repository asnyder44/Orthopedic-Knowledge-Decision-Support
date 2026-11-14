---
schema_version: okds-ko-1.0
ko_id: KO-TRAUMA-TRT-001
title: Cast Immobilization
preferred_term: Cast Immobilization
alternate_terms:
- casting
- plaster cast
- cast treatment
- conservative fracture treatment
ko_type: Treatment
specialty: TRAUMA
cluster: 4
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Cast immobilization means putting a hard cast around a broken bone so the bone cannot move while
  it heals [S1]. It is the most common treatment for broken bones and the main treatment for many wrist
  fractures [S1][S3]. If the bone pieces have shifted, they are often first moved back into place without
  surgery (closed reduction) [S2][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- cast
- plaster cast
- broken bone
- wrist fracture
- closed reduction
- non-surgical treatment
- blood clots
relationships:
- predicate: TREATS
  target_id: KO-TRAUMA-COND-002
  target_label: Distal Radius Fracture
  source_ids:
  - S3
  - S4
- predicate: TREATS
  target_id: KO-TRAUMA-COND-003
  target_label: Osteoporotic Fracture
  source_ids:
  - S1
- predicate: ALTERNATIVE_TO
  target_id: KO-TRAUMA-PROC-001
  target_label: Open Reduction and Internal Fixation
  source_ids:
  - S1
  - S2
  - S4
proposed_concepts:
- term: Closed reduction
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S2, S3, and S4 describe setting the bone without surgery before the cast is put on.
- term: Splint
  suggested_type: Device
  predicate: USES_DEVICE
  reason: S1 names a cast or splint as the most common fracture treatment; no cast or splint Device KO
    exists.
- term: K-wire fixation (pinning)
  suggested_type: Procedure
  predicate: ALTERNATIVE_TO
  reason: S4 describes adding K-wires to prevent the bone from slipping after reduction and casting in
    children.
- term: Venous thromboembolism (blood clots)
  suggested_type: Condition
  predicate: COMPLICATION_OF
  reason: S5 studies the risk of blood clots in people with a leg cast.
sources:
- id: S1
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
- id: S2
  title: '6.5 Fractures: Bone Repair (Anatomy and Physiology 2e)'
  publisher: OpenStax, Rice University
  url: https://openstax.org/books/anatomy-and-physiology-2e/pages/6-5-fractures-bone-repair
  source_type: textbook
  audience: student
  publication_date: '2022'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (openstax:anatomy-and-physiology-2e:6-5-fractures-bone-repair). Licence:
    CC BY 4.0 (OpenStax); attribute OpenStax and link to the book'
- id: S3
  title: 'Two casting methods compared in patients with Colles'' fracture: A pragmatic, randomized controlled
    trial'
  publisher: PLOS ONE
  url: https://doi.org/10.1371/journal.pone.0232153
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via plos. Licence: CC BY 4.0 (PLOS). Type: trial. Text kept: abstract only.'
- id: S4
  title: 'Risk factors for fracture redisplacement after reduction and cast immobilization of displaced
    distal radius fractures in children: a meta-analysis'
  publisher: European Journal of Trauma and Emergency Surgery
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7429528/
  source_type: journal_article
  audience: clinician
  publication_date: '2019'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC7429528). Licence: CC BY'
- id: S5
  title: 'Venous Thrombosis Risk after Cast Immobilization of the Lower Extremity: Derivation and Validation
    of a Clinical Prediction Score, L-TRiP(cast), in Three Population-Based Case–Control Studies'
  publisher: PLOS Medicine
  url: https://doi.org/10.1371/journal.pmed.1001899
  source_type: journal_article
  audience: clinician
  publication_date: '2015'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via plos. Licence: CC BY 4.0 (PLOS). Type: article. Text kept: abstract only.'
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
  - No patient page in this pack is only about casts. Cast care at home (keeping it dry, itching, swelling,
    when a cast feels too tight) is not covered; consider adding a patient cast-care page.
  - The TREATS link to Osteoporotic Fracture rests only on S1's general statement that a cast is the most
    common fracture treatment; confirm it is appropriate.
  - S3 is a single trial in older adults with one wrist fracture type; S4 is about children; S5 is about
    leg casts. Results may not apply to all casts.
  - Cast materials (plaster versus fiberglass) and typical wear times by bone are not given beyond 'often
    several weeks' (S1).
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus shows a new 'last updated' date on the Fractures page.
- A new guideline gives clear advice on blood-clot prevention for people with leg casts (S5 notes guidance
  varies).
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Cast immobilization means putting a hard cast around a broken bone so the bone cannot move while it heals [S1]. A cast or splint is the most common treatment for a broken bone, and casting remains the main treatment for many wrist fractures [S1][S3]. If the broken pieces have shifted, a clinician often first moves them back into place without surgery, which is called a closed reduction [S2][S3]. How long the cast stays on depends on the break and the bone, but it is often several weeks [S1].

## Key Facts (claim → source)
- A cast keeps a broken bone from moving while it heals [S1].
- Wearing a cast or splint is the most common treatment for a fracture [S1].
- A cast is often worn for several weeks, depending on the type of break and which bone is broken [S1].
- Setting a broken bone into place without surgery is called a closed reduction [S2].
- In children with shifted wrist fractures, reduction and casting is often the treatment of choice, but the bone slips out of place again in about 21 to 39 percent of cases [S4].
- In a trial of older adults with a wrist fracture, a cast holding the wrist in a more natural position was likely as good as or better than a bent-wrist cast [S3].
- A leg cast can raise the risk of blood clots in the veins, and a risk score can help predict who is at high risk [S5].

## Explanation
### What it is
A fracture is a broken bone [S1][S2]. A cast is a hard covering placed around the injured area to keep the bone from moving while it heals [S1]. Some casts are made of plaster [S5]. Before a cast is put on, a clinician may need to move the broken pieces back into line without surgery, called a closed reduction [S2][S3]. Your provider will tell you when the cast can come off [S1].

### How it helps
A broken bone will heal whether or not it is set in its normal position, but if it is not set correctly it will heal in a bent or wrong position [S2]. Keeping the bone still in a cast lets it heal in place [S1]. During healing, a blood clot forms at the break, then a soft bridge of new tissue called a callus forms within about two days, and over several weeks it is replaced by bone [S2].

### Who it may suit
- People with many kinds of fractures, since a cast or splint is the most common fracture treatment [S1].
- Many people with distal radius (wrist) fractures, including older adults [S3].
- Children with shifted wrist fractures, after the bone is set back into place [S4].

Some fractures need surgery with plates, pins, or screws instead [S1]. In children, a break that was fully shifted, a break of both forearm bones, or a bone that could not be lined up well raises the chance that the bone slips again in the cast [S4]. These children may benefit from added pins (K-wires) to hold the bone [S4].

### Risks and side effects
- **Bone slipping out of place:** after reduction and casting, the bone can shift again [S3][S4]. In one trial of older adults with wrist casts, 8 to 13 percent later needed surgery because the bone lost its position [S3].
- **Blood clots:** having a leg in a plaster cast is linked to a risk of blood clots in a deep vein (deep vein thrombosis), which can cause pain, swelling, and redness in the leg [S5]. Part of a clot can travel to the lungs, which can be life-threatening [S5].
- **Varying advice on clot prevention:** guidelines differ on whether people with a leg cast should get medicine to prevent clots, and a risk score may help decide [S5].

### Evidence summary
- A cast is the most common fracture treatment, according to MedlinePlus [S1].
- A trial of 105 older adults with a common wrist fracture found that the cast position made only a small, uncertain difference at 12 months, though a more natural wrist position was likely better [S3].
- A review of 12 studies with 1,256 children found that full displacement, a break of both forearm bones, and imperfect lining up of the bone raised the risk of the bone slipping in the cast [S4].
- A study of three large groups created a simple score that predicted blood clots in people with leg casts fairly well [S5].

## Common Misunderstandings
- **Myth:** Once a cast is on, the bone cannot shift. **Fact:** A broken bone can slip out of place again inside a cast, and some people later need surgery [S3][S4].
- **Myth:** A bone only heals if it is in a cast or fixed with surgery. **Fact:** A bone can heal on its own, but it may heal in the wrong position if it is not set correctly [S2].
- **Myth:** A leg cast has no effect beyond the leg bone. **Fact:** A leg cast is linked to a risk of blood clots in the veins [S5].
- **Myth:** Every broken bone is treated the same way. **Fact:** How long a cast is worn depends on the type of fracture and which bone is broken, and some breaks need surgery [S1].

## Questions to Ask Your Doctor
1. Does my bone need to be set (reduced) before the cast goes on?
2. How long will I likely wear the cast, and how will we check that the bone stays in place?
3. What signs mean I should call or come back right away?
4. If I have a leg cast, what is my risk of blood clots, and is anything needed to prevent them?
5. When would surgery be a better choice than a cast for my break?

## Test Questions
1. What does a cast do for a broken bone? - It keeps the bone from moving while it heals [S1].
2. What is a closed reduction? - Setting a broken bone into place without surgery [S2].
3. About how long is a cast often worn? - Often several weeks, depending on the break and the bone [S1].
4. Name one risk factor for a child's wrist fracture slipping in a cast. - Examples: full displacement, a break of both forearm bones, or imperfect reduction [S4].
5. What serious problem is linked to wearing a leg cast? - Blood clots in the veins (venous thromboembolism) [S5].

## Related Topics
- Treats: Distal Radius Fracture (KO-TRAUMA-COND-002), Osteoporotic Fracture (KO-TRAUMA-COND-003)
- Alternative to: Open Reduction and Internal Fixation (KO-TRAUMA-PROC-001)
- Proposed new topics: Closed reduction (treatment), Splint (device), K-wire fixation (procedure), Venous thromboembolism (condition)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Fractures.* https://medlineplus.gov/fractures.html (retrieved 2026-10-26)
2. [S2] OpenStax, Rice University. *6.5 Fractures: Bone Repair (Anatomy and Physiology 2e).* https://openstax.org/books/anatomy-and-physiology-2e/pages/6-5-fractures-bone-repair (retrieved 2026-10-26)
3. [S3] PLOS ONE. *Two casting methods compared in patients with Colles' fracture: A pragmatic, randomized controlled trial.* https://doi.org/10.1371/journal.pone.0232153 (retrieved 2026-11-14)
4. [S4] European Journal of Trauma and Emergency Surgery. *Risk factors for fracture redisplacement after reduction and cast immobilization of displaced distal radius fractures in children: a meta-analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC7429528/ (retrieved 2026-10-26)
5. [S5] PLOS Medicine. *Venous Thrombosis Risk after Cast Immobilization of the Lower Extremity: Derivation and Validation of a Clinical Prediction Score, L-TRiP(cast), in Three Population-Based Case–Control Studies.* https://doi.org/10.1371/journal.pmed.1001899 (retrieved 2026-11-14)
