---
schema_version: okds-ko-1.0
ko_id: KO-TRAUMA-PROC-001
title: Open Reduction and Internal Fixation
preferred_term: Open Reduction and Internal Fixation
alternate_terms:
- ORIF
- open reduction
- surgical fracture fixation
- osteosynthesis
ko_type: Procedure
specialty: TRAUMA
cluster: 5
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Open reduction and internal fixation (ORIF) is surgery for a broken bone. The surgeon opens the
  skin to see the break, puts the bone pieces back in place (open reduction), and holds them with metal
  implants such as plates and screws (internal fixation) [S1][S2][S4]. It is one option when a cast or
  splint is not enough, such as for some wrist fractures [S2][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- fracture surgery
- broken bone
- plates and screws
- volar locking plate
- wrist fracture
- hip fracture
- osteoporosis
relationships:
- predicate: TREATS
  target_id: KO-TRAUMA-COND-002
  target_label: Distal Radius Fracture
  source_ids:
  - S3
  - S5
- predicate: TREATS
  target_id: KO-TRAUMA-COND-003
  target_label: Osteoporotic Fracture
  source_ids:
  - S4
- predicate: TREATS
  target_id: KO-TRAUMA-COND-001
  target_label: Hip Fracture
  source_ids:
  - S4
- predicate: ALTERNATIVE_TO
  target_id: KO-TRAUMA-TRT-001
  target_label: Cast Immobilization
  source_ids:
  - S2
  - S3
proposed_concepts:
- term: Volar locking plate
  suggested_type: Device
  predicate: USES_DEVICE
  reason: S3 and S5 describe ORIF of the wrist with a plate on the palm side of the radius; no plate Device
    KO exists.
- term: Bone screws, plates, and nails (osteosynthesis implants)
  suggested_type: Device
  predicate: USES_DEVICE
  reason: S2 and S4 name plates, pins, screws, and nails as the implants that hold the bone.
- term: Closed reduction
  suggested_type: Treatment
  predicate: ALTERNATIVE_TO
  reason: S1 contrasts closed reduction (setting a bone without surgery) with open reduction.
- term: External fixation
  suggested_type: Procedure
  predicate: ALTERNATIVE_TO
  reason: S3 compares ORIF with external fixation, pinning, and nail fixation for wrist fractures.
- term: Recovery after fracture surgery
  suggested_type: RehabProtocol
  predicate: FOLLOWED_BY
  reason: S4 stresses early movement and weight-bearing after fixation; a rehab KO would hold timing and
    warning signs.
- term: Flexor tendon rupture
  suggested_type: Condition
  predicate: COMPLICATION_OF
  reason: S5 reviews tendon rupture as a rare complication of wrist plate fixation.
sources:
- id: S1
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
  title: Association of Open Reduction and Internal Fixation With Volar Locking Plate for Distal Radius
    Fractures With Patient-Reported Outcomes in Older Adults
  publisher: JAMA Network Open
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10276304/
  source_type: journal_article
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC10276304). Licence: CC BY'
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
  title: 'Flexor tendon injuries following plate fixation of distal radius fractures: a systematic review
    of the literature'
  publisher: 'Journal of Orthopaedics and Traumatology : Official Journal of the Italian Society of Orthopaedics
    and Traumatology'
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3828490/
  source_type: journal_article
  audience: clinician
  publication_date: '2013'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC3828490). Licence: CC BY'
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
  - MeSH ID and ICD-10-CM code are unknown and set to verify; procedure codes (for example CPT or ICD-10-PCS)
    are not in any source.
  - No patient page in this pack is only about ORIF. Anesthesia, cut size, hospital stay, and infection
    risk are not described, so 'How it is done' and 'Risks' are limited. Consider adding an AAOS OrthoInfo
    or MedlinePlus page on internal fixation (check its licence).
  - 'Recovery timeline: the pack has general bone-healing stages (S1) and short-term results after wrist
    ORIF (S3), but no step-by-step recovery schedule after ORIF. Ask a clinician.'
  - Most evidence is about distal radius fractures in older adults (S3, S5) and osteoporotic bone (S4);
    results may not apply to other bones or younger people.
  - Plain-language explanation of 'internal fixation' as metal parts inside the body was written by the
    drafter from S2 and S4; check the wording.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- A new network meta-analysis or guideline compares ORIF with casting for distal radius fractures.
- MedlinePlus shows a new 'last updated' date on the Fractures page.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Open reduction and internal fixation (ORIF) is a type of surgery to repair a broken bone [S1][S2]. In "open reduction," the surgeon makes a cut to see the break and puts the bone pieces back where they belong [S1]. In "internal fixation," metal implants such as plates, screws, pins, or nails are placed to hold the bone still while it heals [S2][S4]. It is one option when a cast or splint alone is not enough, and it is often studied for wrist fractures [S2][S3].

## Key Facts (claim → source)
- Open reduction means surgery that exposes the fracture and resets the bone; closed reduction means setting the bone without surgery [S1].
- A broken bone can heal even if it is not reset, but it may then heal in a bent or wrong position [S1].
- Implants used to hold broken bones include screws, plates, and nails [S4].
- For wrist fractures in adults 50 and older, ORIF with a plate gave better arm and wrist scores than casting at 3 months [S3].
- In that same review, complication rates at one year were about the same for all treatments [S3].
- Weak (osteoporotic) bone holds metal implants less well, so fixation can fail [S4].
- A rare but serious problem after wrist plate surgery is a tear (rupture) of a finger or thumb tendon [S5].

## Explanation
### What it is
A fracture is a broken bone [S1]. "Reduction" means putting the broken pieces back into their normal position [S1]. When this is done without surgery, it is called a closed reduction; when surgery is needed to open the area and reset the bone, it is called an open reduction [S1]. "Internal fixation" means placing implants such as screws, plates, or nails inside the body to hold the bone pieces together [S4]. For a broken wrist, a common form of ORIF uses a plate on the palm side of the radius bone, called a volar locking plate [S3][S5].

### Why it is done
A bone needs to be kept still to heal, either with a cast or brace or with surgery and implants [S4]. If a bone heals out of place, it can stay in that bent position [S1]. Some fractures need surgery to put in plates, pins, or screws to keep the bone in place [S2]. Older adults do much better when they can get up and move soon after a fracture, so they need a repair strong enough to bear weight right away [S4]. For wrist fractures in older adults, some people value getting back to daily tasks quickly, which ORIF may help with [S3].

### How it is done
The surgeon opens the skin over the fracture, lines up the bone pieces, and resets the bone [S1]. Implants such as screws, plates, or nails are then used to hold the pieces in place [S4]. Weak bone can break into many small pieces, which takes extra skill to put back together [S4]. The sources here do not explain anesthesia or the steps of the operation in detail, so ask the surgeon what to expect.

### Devices used
- **Plates, pins, and screws:** used to keep the bone in place [S2][S4].
- **Nails:** rods used inside the bone to hold it [S4].
- **Volar locking plate:** a plate used for wrist fractures, placed on the palm side of the radius [S3][S5].
- **Reinforced implants:** for weak bone, newer implant designs or added reinforcement can give more stability [S4].

### Risks
- **Implant problems:** in osteoporotic bone, implants can loosen or cut out of the bone, and new breaks can happen near the implant [S4].
- **Tendon injury (wrist plates):** a tendon that bends the thumb or a finger can wear against the edge of a plate and tear, often months after surgery [S5]. Warning signs reported include not being able to bend the tip of the thumb or finger, pain, a rubbing feeling, wrist swelling, or a pop or click [S5]. Placing the plate in the right spot and removing a plate that sticks out can lower this risk [S5].
- **Overall complications:** in older adults with wrist fractures, one-year complication rates after ORIF were similar to casting and other treatments [S3].

### Recovery timeline
Bone healing follows the same steps after any break: a blood clot forms in the first hours, a soft "callus" (new tissue that bridges the gap) starts within about two days, and over the next several weeks it is replaced by bone [S1]. With strong fixation, many older adults can put weight on the limb right after surgery and heal on time, even with osteoporosis [S4]. For wrist fractures in older adults, people who had ORIF reported better function than those with a cast at 3 months and up to one year [S3]. The sources here do not give a full recovery schedule, so ask the care team.

### Alternatives
- **Cast or splint:** the most common fracture treatment, which keeps the bone still while it heals, often for several weeks [S2].
- **Other surgeries for wrist fractures:** external fixation, pins placed through the skin (percutaneous pinning), or a nail inside the bone [S3].
- **Choosing together:** for older adults with wrist fractures, shared decision-making about each person's goals for recovery may help pick the best option [S3].

## Common Misunderstandings
- **Myth:** A broken bone only heals if it is fixed with surgery. **Fact:** A broken bone can heal without surgery, but it may heal in the wrong position if it is not set correctly [S1].
- **Myth:** ORIF and casting give the same early results for older adults with wrist fractures. **Fact:** One large review found better arm and wrist scores with ORIF at 3 months, with similar one-year complications [S3].
- **Myth:** Plates and screws hold equally well in every bone. **Fact:** Weak osteoporotic bone holds implants less well, so special implants or reinforcement may be needed [S4].
- **Myth:** Problems from a wrist plate show up right after surgery. **Fact:** Tendon tears linked to wrist plates often happen months after surgery [S5].

## Questions to Ask Your Doctor
1. Why do you recommend surgery instead of a cast or splint for my break?
2. What implants will be used, and will they stay in for good?
3. When can I start moving and using the arm or leg again?
4. What warning signs after surgery should make me call you?
5. Does weak bone or osteoporosis change how my fracture will be fixed?

## Test Questions
1. What is the difference between open and closed reduction? - Open reduction uses surgery to expose and reset the bone; closed reduction sets it without surgery [S1].
2. Name two kinds of implants used for internal fixation. - Examples: plates, screws, pins, or nails [S2][S4].
3. What did a review find when comparing ORIF with casting for wrist fractures in older adults? - ORIF gave better scores at 3 months, with similar one-year complications [S3].
4. Why is fixing a fracture in osteoporotic bone harder? - The bone breaks into more pieces and holds implants less well [S4].
5. What rare complication can happen after a wrist plate? - A thumb or finger tendon can tear, often months later [S5].

## Related Topics
- Treats: Distal Radius Fracture (KO-TRAUMA-COND-002), Osteoporotic Fracture (KO-TRAUMA-COND-003), Hip Fracture (KO-TRAUMA-COND-001)
- Alternative to: Cast Immobilization (KO-TRAUMA-TRT-001)
- Proposed new topics: Volar locking plate (device), Bone screws, plates, and nails (device), Closed reduction (treatment), External fixation (procedure), Recovery after fracture surgery (rehab protocol), Flexor tendon rupture (condition)

## References
1. [S1] OpenStax, Rice University. *6.5 Fractures: Bone Repair (Anatomy and Physiology 2e).* https://openstax.org/books/anatomy-and-physiology-2e/pages/6-5-fractures-bone-repair (retrieved 2026-10-26)
2. [S2] MedlinePlus, U.S. National Library of Medicine. *Fractures.* https://medlineplus.gov/fractures.html (retrieved 2026-10-26)
3. [S3] JAMA Network Open. *Association of Open Reduction and Internal Fixation With Volar Locking Plate for Distal Radius Fractures With Patient-Reported Outcomes in Older Adults.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10276304/ (retrieved 2026-10-26)
4. [S4] Current Osteoporosis Reports. *Biomechanics of Osteoporotic Fracture Fixation.* https://pmc.ncbi.nlm.nih.gov/articles/PMC6944651/ (retrieved 2026-10-26)
5. [S5] Journal of Orthopaedics and Traumatology : Official Journal of the Italian Society of Orthopaedics and Traumatology. *Flexor tendon injuries following plate fixation of distal radius fractures: a systematic review of the literature.* https://pmc.ncbi.nlm.nih.gov/articles/PMC3828490/ (retrieved 2026-10-26)
