---
schema_version: okds-ko-1.0
ko_id: KO-SPORT-PROC-001
title: ACL Reconstruction
preferred_term: ACL Reconstruction
alternate_terms:
- anterior cruciate ligament reconstruction
- ACLR
- anatomic ACL reconstruction
- arthroscopic ACL reconstruction
ko_type: Procedure
specialty: SPORT
cluster: 5
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: ACL reconstruction (ACLR) is surgery that replaces a torn anterior cruciate ligament (ACL)
  in the knee with a graft, a piece of tendon that is fixed in place to act as a new ligament [S2][S3].
  It aims to make the knee stable again and is usually followed by a long, step-by-step rehab program
  [S1][S3]. It is one of several options after an ACL tear, and the choice depends on the person's activities
  and goals [S1][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- knee surgery
- ACL tear treatment
- sports surgery
- tendon graft
- arthroscopy
- rehabilitation
- return to sport
relationships:
- predicate: TREATS
  target_id: KO-SPORT-COND-001
  target_label: Anterior Cruciate Ligament Tear
  source_ids:
  - S1
  - S2
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-JOINT-COND-001
  target_label: Knee Osteoarthritis
  source_ids:
  - S2
  - S4
proposed_concepts:
- term: Rehabilitation after ACL reconstruction
  suggested_type: RehabProtocol
  predicate: FOLLOWED_BY
  reason: S1, S2, and S3 describe phased, progressive rehabilitation after ACLR and criteria for return
    to sport.
- term: Non-operative rehabilitation for ACL tear
  suggested_type: Treatment
  predicate: ALTERNATIVE_TO
  reason: S1 and S3 present structured rehabilitation without surgery as a main alternative to ACLR.
- term: Hamstring tendon autograft
  suggested_type: Device
  predicate: USES_DEVICE
  reason: S2 says autografts are preferred and hamstring tendons are the most popular graft.
- term: Interference screw and suspensory fixation
  suggested_type: Device
  predicate: USES_DEVICE
  reason: S2 describes an interference screw at the shinbone and suspensory fixation at the thighbone
    as a preferred construct.
- term: Arthrofibrosis (knee stiffness after surgery)
  suggested_type: Condition
  predicate: COMPLICATION_OF
  reason: S2 lists arthrofibrosis as one of the most common complications after early ACLR.
- term: Anterior cruciate ligament (ACL)
  suggested_type: AnatomicalStructure
  predicate: PREREQUISITE_FOR
  reason: S3 describes the ACL's role as the main knee stabilizer, which the surgery aims to restore.
sources:
- id: S1
  title: Evidence-based recommendations for the management of anterior cruciate ligament (ACL) rupture
  publisher: Best practice & research. Clinical rheumatology
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6723618/
  source_type: journal_article
  audience: clinician
  publication_date: '2019'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: review. Text kept: abstract only.'
- id: S2
  title: 'Current Trends in Anterior Cruciate Ligament Reconstruction: A Review'
  publisher: Cureus
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4684270/
  source_type: journal_article
  audience: clinician
  publication_date: '2015'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC4684270). Licence: CC BY'
- id: S3
  title: 'Treatment after anterior cruciate ligament injury: Panther Symposium ACL Treatment Consensus
    Group'
  publisher: Knee Surgery, Sports Traumatology, Arthroscopy
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7524809/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC7524809). Licence: CC BY'
- id: S4
  title: Post-traumatic osteoarthritis following ACL injury
  publisher: Arthritis research & therapy
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7092615/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: review. Text kept: abstract only.'
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
  - 'Source gap: no patient-level page (MedlinePlus or NIAMS) on ACL reconstruction was found in the
    dataset; all sources are clinician reviews.'
  - 'Source gap: the pack does not list general surgical risks such as infection, blood clots, or graft
    failure rates; the Risks section covers only stiffness (arthrofibrosis) and osteoarthritis. Ask a clinician
    to confirm and consider adding a source.'
  - 'Source gap: no full return-to-sport timeline (months) is given in this pack; only the 4-12 week weakest-graft
    window (S3) is stated.'
  - 'Clinician check: S2 is a 2015 review; graft, fixation, and timing preferences may have changed. Confirm
    current practice.'
  - S1 and S4 are abstract-only in this pack.
  - MeSH ID and ICD-10-CM / procedure codes are unknown and left as <verify>.
  - Plain-language definitions (graft, autograft, arthroscopy) were written by the drafter; check them.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- Any cited page shows a new 'last reviewed' date.
- A new consensus or guideline on ACL reconstruction timing, graft choice, or rehabilitation is published.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
ACL reconstruction (ACLR) is surgery that replaces a torn anterior cruciate ligament (ACL) in the knee with a graft, a piece of tendon that is fixed in place to act as a new ligament [S2][S3]. It aims to make the knee stable again and is usually followed by a long, step-by-step rehab program [S1][S3]. It is one of several options after an ACL tear, and the choice depends on the person's activities and goals [S1][S3].

## Key Facts (claim → source)
- ACLR is an accepted, widely used operation for ACL injuries, with about 100,000 done each year in the United States [S2].
- The surgery tries to rebuild the ACL in its natural size and attachment points; this is called anatomic reconstruction [S3].
- Grafts taken from the patient's own body (autografts) are preferred, and hamstring tendons are the most popular choice [S2].
- Early reconstruction is advised for very active people in jumping, cutting, and pivoting sports, because waiting raises the risk of more meniscus and cartilage damage [S3].
- Surgery done very soon after injury has been linked to a higher chance of knee stiffness (arthrofibrosis) [S2].
- The graft is at its weakest about 4 to 12 weeks after surgery, as it slowly changes to become more like a real ligament [S3].
- Most people get good short-term results, but ACLR has not been clearly shown to prevent knee osteoarthritis later [S2][S4].

## Explanation
### What it is
The ACL is the main ligament that keeps the knee stable, stopping the shinbone from sliding forward and twisting inward [S3]. In ACL reconstruction, a surgeon replaces the torn ligament with a graft and fixes it in place [S2][S3]. The aim of anatomic reconstruction is to restore the ACL to its natural size, fiber direction, and attachment sites [S3]. It can use a single-bundle or double-bundle technique, meaning the new ligament is built as one strand or two [S2][S3].

### Why it is done
The goals of managing an ACL tear are to restore knee function, help the person get back to activity, prevent more injury and arthritis, and protect long-term quality of life [S1]. Surgery is meant to reduce looseness (laxity) in the knee [S3]. For very active people in jumping, cutting, and pivoting sports, early reconstruction is recommended because delaying surgery raises the risk of more damage to the menisci (the knee's cartilage cushions) and cartilage [S3]. Reconstruction is also advised when the knee keeps feeling unstable or keeps "giving way" after rehab [S1][S3]. Treatment without surgery can work for less active people, but active people may not be able to return to high-level sport without surgery [S2].

### How it is done
ACLR is commonly done by arthroscopy, a type of surgery that uses small cuts and a camera [S2]. The surgeon makes bone tunnels in the thighbone and shinbone to hold the graft [S2]. For a single-bundle hamstring graft, making the thighbone tunnel through a separate entry point (the transportal approach) has become more popular than drilling it through the shinbone tunnel (the trans-tibial approach) [S2]. Single-bundle reconstruction is done by most surgeons, while double-bundle reconstruction is getting more popular because it may copy the natural ligament more closely [S2].

Timing matters [S2]. Before surgery, doctors look at swelling, warmth, and how well the knee moves [S2]. One study found worse results at two years when thigh (quadriceps) strength before surgery was below 80% of normal, so building strength first was suggested [S2]. Delaying surgery for more than a year has been linked to more meniscus and cartilage damage [S2].

### Devices used
- **Graft:** Autografts, tendons taken from the patient's own body, are the preferred choice for a first reconstruction, and hamstring tendons are used most often [S2].
- **Fixation devices:** A common setup uses an interference screw (often a "bio-screw") in the shinbone tunnel and a suspensory device that hangs the graft from the thighbone [S2].
- **Healing boosters:** Add-ons such as platelet-rich plasma (PRP) have been tried, but there is no clear proof that they help [S2].

### Risks
- **Stiffness (arthrofibrosis):** This is one of the most common problems after early ACLR, and the chance goes up when surgery is done within about three weeks of injury [S2]. In one study, it happened in 17.6% of people who had surgery at seven days and 6.1% of those who waited four weeks [S2].
- **Arthritis later:** Many people with an ACL injury still develop osteoarthritis after a joint injury (post-traumatic osteoarthritis), and there is no convincing evidence that ACLR prevents it better than non-surgical care [S4].

The sources in this pack do not list other surgical risks, so ask a surgeon about the full list of risks.

### Recovery timeline
Rehab after ACLR is staged, meaning it moves through phases [S3]. In the first phase, rehab works on swelling, pain, knee motion, and turning on and strengthening the thigh muscle [S3]. Next, balance and knee-control training help the knee become stable [S3]. The last phase builds strength, practices sport-specific skills, and checks whether the person feels mentally ready to return to sport [S3]. The graft is at its weakest about 4 to 12 weeks after surgery [S3]. Accelerated rehabilitation, which starts activity sooner, seems to be widely accepted right after ACLR [S2]. Return-to-sport decisions are guided by phase-specific criteria [S1].

### Alternatives
There are three main approaches after an ACL tear [S1]:
1. Rehab first, with reconstruction later only if the knee becomes unstable [S1].
2. Reconstruction first, followed by rehab [S1].
3. Rehab before surgery, then reconstruction, then more rehab [S1].

For people who want to return to straight-line activities, structured rehab without surgery is an acceptable option [S3]. Some people, called "copers," return to their old activity level without surgery and without the knee feeling unstable [S3].

## Common Misunderstandings
- **Myth:** The surgery sews the torn ACL back together. **Fact:** ACLR replaces the torn ligament with a graft, usually a tendon from the patient's own body [S2][S3].
- **Myth:** The new ligament is at full strength as soon as surgery is over. **Fact:** The graft goes through a slow change and is weakest about 4 to 12 weeks after surgery [S3].
- **Myth:** Having surgery as fast as possible is always best. **Fact:** Surgery in the first few weeks has been linked to more stiffness, while waiting more than a year has been linked to more meniscus and cartilage damage [S2].
- **Myth:** ACL reconstruction prevents arthritis. **Fact:** There is no convincing evidence that ACLR lowers the rate of post-traumatic arthritis better than non-surgical care [S4].
- **Myth:** Surgery is the only option after an ACL tear. **Fact:** Rehab without surgery is a main option, with surgery later if the knee stays unstable [S1][S3].

## Questions to Ask Your Doctor
1. Based on my activities and goals, is surgery, rehab alone, or rehab first a better fit for me?
2. When would be the right time for my surgery, and what should my knee be like before it?
3. Which graft would you use, and why?
4. What are the risks of this surgery for me, including stiffness?
5. What will rehab look like, and how will we decide when I can return to sport?
6. What can I do to protect my knee from arthritis over time?

## Test Questions
1. What does ACL reconstruction do? - It replaces the torn ACL with a graft fixed in place to act as a new ligament [S2][S3].
2. Which type of graft is used most often for a first ACLR? - Autografts, most often hamstring tendons [S2].
3. What common problem is more likely if surgery is done very soon after injury? - Knee stiffness, called arthrofibrosis [S2].
4. When is the graft at its weakest? - About 4 to 12 weeks after surgery [S3].
5. Name the three main treatment paths after an ACL tear. - Rehab first; surgery first then rehab; rehab before and after surgery [S1].
6. Does ACLR clearly prevent knee osteoarthritis? - No, convincing evidence for that is still lacking [S4].

## Related Topics
- Treats: Anterior Cruciate Ligament Tear (KO-SPORT-COND-001)
- Read next: Knee Osteoarthritis (KO-JOINT-COND-001)

## References
1. [S1] Best practice & research. Clinical rheumatology. *Evidence-based recommendations for the management of anterior cruciate ligament (ACL) rupture.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6723618/ (retrieved 2026-11-14)
2. [S2] Cureus. *Current Trends in Anterior Cruciate Ligament Reconstruction: A Review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC4684270/ (retrieved 2026-10-26)
3. [S3] Knee Surgery, Sports Traumatology, Arthroscopy. *Treatment after anterior cruciate ligament injury: Panther Symposium ACL Treatment Consensus Group.* https://pmc.ncbi.nlm.nih.gov/articles/PMC7524809/ (retrieved 2026-10-26)
4. [S4] Arthritis research & therapy. *Post-traumatic osteoarthritis following ACL injury.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7092615/ (retrieved 2026-11-14)
