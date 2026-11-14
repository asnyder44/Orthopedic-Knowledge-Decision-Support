---
schema_version: okds-ko-1.0
ko_id: KO-FOOT-COND-001
title: Ankle Sprain
preferred_term: Ankle Sprain
alternate_terms:
- sprained ankle
- lateral ankle sprain
- acute ankle sprain
- ankle ligament sprain
ko_type: Condition
specialty: FOOT
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: An ankle sprain is a stretch or tear of the ligaments, the strong tissues that hold the ankle
  bones together [S1][S2]. Most ankle sprains happen when the foot rolls inward, and they usually hurt
  the ligaments on the outer side of the ankle [S3][S4]. Most sprains are treated without surgery, and
  exercise-based rehabilitation can lower the chance of spraining the ankle again [S4][S5].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- ankle
- ligament
- sprain
- sports injury
- rolled ankle
- chronic ankle instability
relationships: []
proposed_concepts:
- term: Lateral ankle ligaments (anterior talofibular ligament)
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S3, S4 and S5 say the anterior talofibular ligament on the outer ankle is the ligament most
    often hurt; no ankle anatomy KO is in the registry yet.
- term: Ankle X-ray
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S4 says X-rays are used in most acute ankle sprains, partly to look for a broken bone.
- term: Chronic ankle instability
  suggested_type: Condition
  predicate: PREREQUISITE_FOR
  reason: S5 says up to 40% of people develop chronic ankle instability after a sprain; that Condition
    KO would also carry COMPLICATION_OF -> Ankle Sprain.
- term: Exercise-based rehabilitation after ankle sprain
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S4 and S5 support supervised exercise to lower re-injury; a Treatment KO could then TREAT
    this Condition.
- term: RICE (rest, ice, compression, elevation)
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S1 and S4 describe rest, ice and compression as early care for sprains.
sources:
- id: S1
  title: Sprains and Strains
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/sprainsandstrains.html
  source_type: government_health_page
  audience: patient
  publication_date: '2025-09-22'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:sprainsandstrains). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
- id: S2
  title: Ankle Injuries and Disorders
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/ankleinjuriesanddisorders.html
  source_type: government_health_page
  audience: patient
  publication_date: '2024-09-30'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:ankleinjuriesanddisorders). Licence: Public domain (NLM-authored
    MedlinePlus summary); credit MedlinePlus'
- id: S3
  title: Understanding acute ankle ligamentous sprain injury in sports
  publisher: 'Sports Medicine, Arthroscopy, Rehabilitation, Therapy, and Technology : SMARTT'
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2724472/
  source_type: journal_article
  audience: clinician
  publication_date: '2009'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC2724472). Licence: CC BY'
- id: S4
  title: 'Acute Ankle Sprain Management: An Umbrella Review of Systematic Reviews'
  publisher: Frontiers in Medicine
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9301067/
  source_type: journal_article
  audience: clinician
  publication_date: '2022'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC9301067). Licence: CC BY'
- id: S5
  title: 'Exercise-based rehabilitation reduces reinjury following acute lateral ankle sprain: A systematic
    review update with meta-analysis'
  publisher: PLoS ONE
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8824326/
  source_type: journal_article
  audience: clinician
  publication_date: '2022'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC8824326). Licence: CC BY'
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
  - No registry KO is a valid link target for this Condition yet (no foot/ankle anatomy, test or treatment
    KOs), so relationships is empty; see proposed_concepts.
  - 'How it is diagnosed: the pack does not describe the physical exam or rules for when an X-ray is needed;
    S4 only says X-rays are used in 77-99% of cases. Consider adding a patient page or guideline on ankle
    sprain diagnosis (e.g., the Ottawa ankle rules).'
  - 'When to seek care: no source in the pack lists specific warning signs; the section is built from
    S3/S4 facts (possible fracture, lasting problems). A clinician should check the wording.'
  - 'Clinician check: S3 (2009) says immobilization should not be used; S4 (2022) says functional treatment
    "seems preferable" to immobilization. The KO states both.'
  - S4 mentions paracetamol, opioids and NSAIDs for pain; the KO names no medicines or doses on purpose.
  - The '80% of people will sprain an ankle in their lifetime' figure (S4) and risk-factor figures (S3,
    athletes) need clinician confirmation before publishing.
  - MeSH and ICD-10-CM codes are unknown and set to verify.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- Any cited page shows a new 'last reviewed' date.
- A new systematic review or clinical practice guideline on acute ankle sprain management is published.
- Foot and ankle anatomy, test or treatment KOs are added to the registry (add links).
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
An ankle sprain is a stretch or tear of the ligaments, the strong tissues that hold the ankle bones together [S1][S2]. Most ankle sprains happen when the foot rolls inward, and they usually hurt the ligaments on the outer side of the ankle [S3][S4]. Most sprains are treated without surgery, and exercise-based rehabilitation can lower the chance of spraining the ankle again [S4][S5].

## Key Facts (claim → source)
- A sprain is a stretched or torn ligament, and ankle sprains are common [S1][S2].
- Ankle sprains are among the most common sports injuries, and one review estimates that about 80% of people will sprain an ankle at some point in life [S2][S4].
- Most ankle sprains affect the ligaments on the outer (lateral) side of the ankle, and the anterior talofibular ligament is the one hurt most often [S3][S4][S5].
- Common signs are pain, swelling, bruising, and trouble moving the joint, sometimes with a pop felt at the time of injury [S1].
- Fewer than 15% of acute ankle sprains also involve a broken bone in the ankle or foot [S4].
- Treatment is mostly non-surgical, and moving the ankle early (functional treatment) seems better than keeping it still in a cast [S3][S4].
- Exercise-based rehabilitation lowered the chance of a repeat sprain over 12 months compared with usual care [S5].
- A sprain can take a few weeks to many months to heal fully [S2].

## Explanation
### What it is
The ankle joint is made of the ankle bone and the ends of the two lower leg bones [S2]. Ligaments, bands of tissue that connect bone to bone, keep the joint steady [S1][S2]. A sprain happens when one or more of these ligaments is stretched or torn [S1][S2]. About 85% of ankle sprains involve the group of ligaments on the outer side of the ankle [S4]. This group has three ligaments, and the anterior talofibular ligament (ATFL) at the front is the weakest [S4][S5]. In more severe sprains, other ligaments may also be hurt [S5].

Doctors often sort sprains into three grades [S4]:
- **Grade I:** the ligaments are stretched but not visibly torn [S4].
- **Grade II:** the ligaments are partly torn [S4].
- **Grade III:** the ligaments are completely torn [S4].

### Causes and risk factors
Falling, twisting, or being hit can cause a sprain [S1]. Most ankle sprains happen when the foot lands in the wrong position and rolls inward very fast, in about one-twentieth of a second [S3]. Sprains are very common in sports, especially indoor sports such as volleyball, basketball, and dance [S2][S4]. One review says they are more common in women than in men, and more common in children than in teens and adults [S4].

A review of sports studies linked these factors to a higher chance of an ankle sprain [S3]:
- Having sprained the ankle before [S3].
- Poor balance when standing on one leg [S3].
- Being overweight [S3].
- Not stretching before exercise [S3].
- Wearing shoes with air cells [S3].

The same review says wearing an ankle support (orthosis) lowered the risk [S3].

### Symptoms
- Pain and swelling around the ankle [S1].
- Bruising [S1].
- Trouble moving the joint [S1].
- A pop or tearing feeling at the moment of injury [S1].

Some people still have problems later, such as pain, a feeling that the ankle is unstable, weakness, stiffness, or swelling [S3]. Chronic ankle instability means the ankle keeps spraining again or feels like it "gives way," and up to 40% of people may develop it [S5].

### How it is diagnosed
The sources in this pack do not describe the exam step by step, so ask a clinician how they check an ankle sprain [S3]. One review notes that the ways of diagnosing and grading ankle sprains vary [S3]. Another review says X-rays are used in most cases, which helps because a small share of sprains also involve a broken bone [S4]. Clinicians may also grade the sprain from I to III based on how badly the ligaments are torn [S4].

### Treatment options
- **Early care:** at first, a sprain is usually treated with rest, ice, a bandage or device that presses gently on the area (compression), and medicines [S1]. Which pain medicine is right is a question for a clinician [S4].
- **Moving early instead of a cast:** one review found that functional treatment, which lets the ankle move with support, seems better than keeping the ankle still [S4]. An older review warns that keeping the ankle still can lead to stiffness, muscle loss, and poorer balance sense [S3].
- **Exercise and physical therapy:** later treatment may include exercise and physical therapy [S1]. Supervised exercise and hands-on (manipulative) therapy can help prevent another sprain and restore the ankle's ability to bend upward [S4]. In a review of 14 trials, exercise-based rehabilitation lowered the chance of a repeat sprain at 12 months compared with usual care [S5].
- **Surgery:** treatment options range from physical therapy to surgery, but most ankle sprains are managed without an operation [S3][S4].

In athletes, return to sport after an outer-ankle sprain takes about 16 to 24 days on average, but many have another sprain or longer-term problems [S5].

### When to seek care
The sources here do not list specific warning signs, so ask a health care provider about your own injury [S1][S4]. A sprain can come with a broken bone in some cases, which an X-ray can help find [S4]. Severe ankle injuries can sometimes lead to lasting problems such as an unstable ankle, weaker muscles, or trouble moving, and without proper treatment and rehabilitation, sports injuries may raise the chance of arthritis later [S3].

## Common Misunderstandings
- **Myth:** A sprain is just a minor twist that always heals in a few days. **Fact:** A sprain can take a few weeks to many months to heal completely [S2].
- **Myth:** The best treatment is to keep the ankle still in a cast. **Fact:** Reviews found that early, supported movement seems better than keeping the ankle still [S3][S4].
- **Myth:** Once the pain is gone, the ankle is back to normal. **Fact:** Many people sprain the ankle again, and up to 40% may develop chronic ankle instability [S5].
- **Myth:** Rehab exercises are optional. **Fact:** Exercise-based rehabilitation lowered the chance of a repeat sprain over 12 months compared with usual care [S5].

## Questions to Ask Your Doctor
1. How bad is my sprain, and which ligaments are hurt?
2. Do I need an X-ray to check for a broken bone?
3. How much should I move or put weight on my ankle while it heals?
4. Which exercises or physical therapy can help lower my chance of another sprain?
5. When is it safe for me to go back to sports or work?

## Test Questions
1. What is a sprain? - A stretched or torn ligament, the tissue that connects bones at a joint [S1].
2. Which ligament is hurt most often in an ankle sprain? - The anterior talofibular ligament on the outer side of the ankle [S3][S4].
3. Name two common symptoms of an ankle sprain. - Examples: pain, swelling, bruising, or trouble moving the joint [S1].
4. Name one factor linked to a higher chance of an ankle sprain. - Examples: a past sprain, poor one-leg balance, or being overweight [S3].
5. What did a review of 14 trials find about exercise-based rehabilitation? - It lowered the chance of a repeat sprain at 12 months compared with usual care [S5].
6. What is chronic ankle instability? - Repeated sprains and a feeling that the ankle gives way [S5].

## Related Topics
- No linked KOs yet: the registry has no ankle anatomy, test, or treatment KOs that this Condition can link to.
- Proposed topics: Lateral ankle ligaments (anterior talofibular ligament), Ankle X-ray, Chronic ankle instability, Exercise-based rehabilitation after ankle sprain, RICE (rest, ice, compression, elevation).

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Sprains and Strains.* https://medlineplus.gov/sprainsandstrains.html (retrieved 2026-10-26)
2. [S2] MedlinePlus, U.S. National Library of Medicine. *Ankle Injuries and Disorders.* https://medlineplus.gov/ankleinjuriesanddisorders.html (retrieved 2026-10-26)
3. [S3] Sports Medicine, Arthroscopy, Rehabilitation, Therapy, and Technology : SMARTT. *Understanding acute ankle ligamentous sprain injury in sports.* https://pmc.ncbi.nlm.nih.gov/articles/PMC2724472/ (retrieved 2026-10-26)
4. [S4] Frontiers in Medicine. *Acute Ankle Sprain Management: An Umbrella Review of Systematic Reviews.* https://pmc.ncbi.nlm.nih.gov/articles/PMC9301067/ (retrieved 2026-10-26)
5. [S5] PLoS ONE. *Exercise-based rehabilitation reduces reinjury following acute lateral ankle sprain: A systematic review update with meta-analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC8824326/ (retrieved 2026-10-26)
