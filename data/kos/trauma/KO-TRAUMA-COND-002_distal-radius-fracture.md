---
schema_version: okds-ko-1.0
ko_id: KO-TRAUMA-COND-002
title: Distal Radius Fracture
preferred_term: Distal Radius Fracture
alternate_terms:
- broken wrist
- Colles fracture
- DRF
ko_type: Condition
specialty: TRAUMA
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: A distal radius fracture is a break in the radius, the larger forearm bone, at its end near the
  wrist [S1][S3]. It is one of the most common broken bones, and it often happens from a fall onto an
  outstretched hand [S3][S4]. Treatment may be a cast or splint, or surgery that holds the bone with metal
  hardware [S2][S5].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- broken wrist
- wrist fracture
- forearm
- falls
- osteoporosis
- cast
- volar plate
- older adults
- children
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-TRAUMA-TRT-001
  target_label: Cast Immobilization
  source_ids:
  - S2
  - S3
  - S5
- predicate: PREREQUISITE_FOR
  target_id: KO-TRAUMA-PROC-001
  target_label: Open Reduction and Internal Fixation
  source_ids:
  - S4
  - S5
- predicate: PREREQUISITE_FOR
  target_id: KO-TRAUMA-COND-003
  target_label: Osteoporotic Fracture
  source_ids:
  - S2
  - S3
proposed_concepts:
- term: Radius (forearm bone)
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: The break is in the distal radius (S1, S3); no radius or wrist anatomy KO exists in the registry.
- term: Disabilities of the Arm, Shoulder and Hand (DASH) questionnaire
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: S4 and S5 use DASH scores to compare surgery and casting.
- term: Patient-Rated Wrist Evaluation (PRWE)
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: S5 uses PRWE scores to compare ORIF and casting in older adults.
- term: Wrist x-ray (radiograph)
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S2 and S3 say evaluation includes x-rays (radiographs).
- term: Compartment syndrome
  suggested_type: Condition
  predicate: COMPLICATION_OF
  reason: S3 names forearm compartment syndrome as a rare complication of distal radius fractures.
sources:
- id: S1
  title: Wrist Injuries and Disorders
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/wristinjuriesanddisorders.html
  source_type: government_health_page
  audience: patient
  publication_date: '2025-08-10'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:wristinjuriesanddisorders). Licence: Public domain (NLM-authored
    MedlinePlus summary); credit MedlinePlus'
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
  title: 'Emergency Medicine Management of Distal Radius and Ulna Fractures: Narrative Review'
  publisher: Western Journal of Emergency Medicine
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13436675/
  source_type: journal_article
  audience: clinician
  publication_date: '2026'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC13436675). Licence: CC BY'
- id: S4
  title: 'Non-surgical vs. surgical treatment of distal radius fractures: a meta-analysis of randomized
    controlled trials'
  publisher: BMC Surgery
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11234633/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC11234633). Licence: CC BY'
- id: S5
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
  - 'Clinician check: S4 (2024 meta-analysis) found some benefit from surgery, while S3 and S5 report
    AAOS advice to cast most adults over 65 because outcomes at one year are similar. The KO states both;
    confirm the balance and wording.'
  - The AAOS distal radius fracture guideline itself is not in this pack; it is only reported second-hand
    by S3 and S5. Consider adding it (link_and_paraphrase).
  - No patient page in this pack is only about distal radius fractures; S1 (wrist injuries) and S2 (fractures)
    are general. Consider a patient-level distal radius fracture page.
  - '''Colles fracture'' is kept as an alternate term from the registry; S4 names it as a special kind
    of distal radius fracture, not an exact synonym. Check.'
  - S3 links distal radius fracture to acute carpal tunnel syndrome; the Carpal Tunnel Syndrome KO could
    add a link back.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- AAOS or the American Society for Surgery of the Hand updates its distal radius fracture guideline.
- A new meta-analysis of surgery versus casting for distal radius fractures in older adults is published.
- MedlinePlus shows a new 'last updated' date on the Wrist Injuries and Disorders or Fractures page.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
A distal radius fracture is a break in the radius, the larger of the two forearm bones, at the end closest to the wrist [S1][S3]. It is one of the most common broken bones, and it most often happens from a fall onto an outstretched hand [S3][S4]. Treatment depends on the break and the person's age, and may be a cast or splint, or surgery that holds the bone in place with metal hardware [S2][S3][S5].

## Key Facts (claim → source)
- The wrist joins the hand to the forearm, and it includes two large forearm bones and eight small wrist bones [S1].
- Distal radius fractures make up about one sixth of all fractures seen in emergency departments [S3].
- They are most common in two groups: children and teens (especially boys) and women over 65 [S3][S4].
- The most common cause is falling onto an outstretched hand [S3].
- Doctors check the wrist with an exam and x-rays, and test the nerves of the hand [S3].
- For adults over 65, studies have found that results are similar with or without surgery, so most are treated without surgery [S3][S5].
- In some patients, surgery led to better grip strength and arm function scores than non-surgical care [S4].
- A wrist fracture in an older adult can be an early sign of weak bones (osteoporosis), before hip or spine fractures happen [S3].

## Explanation
### What it is
Your wrist connects your hand to your forearm [S1]. It has two big forearm bones and eight small wrist bones called carpals [S1]. A fracture is a break in a bone [S2]. A distal radius fracture is a break in the radius near the wrist, and it can happen together with a break in the end of the other forearm bone, the ulna [S3]. In children, these breaks are described by how close they are to the growth plate, the area where a child's bone grows [S3].

### Causes and risk factors
- **Falls:** the most common cause is a fall onto an outstretched hand [S3]. Sports such as skating or snowboarding can lead to this kind of fall [S1].
- **Age and sex:** these breaks are most common in boys under 18 and women over 65 [S3]. A woman over 50 has about a 15 percent chance of having one during her life [S3].
- **Weak bones:** low bone density and osteoporosis make broken bones much more likely [S2]. Risk factors for weak bones include being female, older age, very low body weight, smoking, and earlier fractures [S3].
- **High-energy injuries:** in children, most of these breaks come from hard falls or sports [S3].

### Symptoms
- Wrist pain, swelling, and less wrist strength are common signs of a wrist problem [S1].
- With a broken bone, there may be strong pain, bruising, tenderness, trouble moving, or a wrist that looks out of place (deformity) [S2][S3].
- A visible deformity suggests the broken pieces have shifted [S3].
- A cut or puncture in the skin near the break can mean an open fracture, where the bone has broken through the skin [S2][S3].
- Sudden numbness or tingling can also happen with wrist injuries [S1].

### How it is diagnosed
A health care provider asks how the injury happened and examines the wrist [S2][S3]. The exam checks for deformity and tests the feeling and movement of the hand to look for nerve injury [S3]. X-rays (radiographs) are used to see the break [S2][S3]. Ultrasound is also being used more in managing these fractures [S3]. The provider may also ask about risk factors for weak bones [S3].

### Treatment options
Treatment and the goal for lining up the bone depend on how far the bone has moved, whether the break goes into the joint, and the person's age [S3].
- **Reduction:** if the pieces have shifted, a clinician may move them back into place without surgery; this is called a reduction [S3].
- **Splint or cast:** splints range from removable wrist braces to molded plaster or fiberglass splints [S3]. A cast or splint keeps the bone from moving while it heals, often for several weeks [S2].
- **Surgery:** surgery can use plates, pins, or screws to keep the bone in place [S2]. Options studied include open reduction and internal fixation with a plate on the palm side of the wrist (volar locking plate), external fixation, pins through the skin, and a rod inside the bone (nail) [S5].
- **Older adults:** U.S. orthopedic and hand surgery groups advise good non-surgical reduction for most adults over 65 and clear talks about the limits of surgery [S3]. One large review found that plate surgery gave faster short-term recovery than casting in older adults, with similar complications at one year [S5].
- **Evidence:** experts have not agreed on the single best treatment, and the choice can depend on what matters most to each person [S4][S5].

### When to seek care
If you think you may have broken a bone, get medical care right away [S2]. A rare but serious problem is compartment syndrome, where pressure builds up inside the forearm muscles [S3]. One warning sign is pain that seems much worse than expected for the injury [S3].

## Common Misunderstandings
- **Myth:** A broken wrist always needs surgery. **Fact:** Many are treated with a cast or splint, and most adults over 65 are treated without surgery [S2][S3].
- **Myth:** Surgery is always better for older adults. **Fact:** Results at one year are similar for many older adults with or without surgery, though surgery may speed up early recovery for some [S3][S5].
- **Myth:** A broken wrist has nothing to do with bone health. **Fact:** In older adults, a wrist fracture can be the first sign of weak bones and can come before hip or spine fractures [S3].
- **Myth:** Only older people break their wrists. **Fact:** These breaks are also very common in children and teens [S3][S4].

## Questions to Ask Your Doctor
1. Did the bone shift out of place, and does it need to be put back in line?
2. Will a cast or splint be enough, or would surgery help in my case?
3. What are the pros and cons of surgery compared with a cast for someone my age?
4. What warning signs should make me call or come back right away?
5. Should I be checked for osteoporosis after this fracture?

## Test Questions
1. Which bone breaks in a distal radius fracture? - The radius, one of the two forearm bones, near the wrist [S1][S3].
2. What is the most common way people get this fracture? - Falling onto an outstretched hand [S3].
3. Which two groups have these fractures most often? - Children and teens (especially boys) and women over 65 [S3].
4. What imaging test is used to see the break? - X-rays (radiographs) [S2][S3].
5. How are most distal radius fractures in adults over 65 treated? - Without surgery, because results are similar at one year [S3][S5].
6. Why can a wrist fracture matter for bone health? - It can be an early sign of osteoporosis, before hip or spine fractures [S3].

## Related Topics
- Read next: Cast Immobilization (KO-TRAUMA-TRT-001), Open Reduction and Internal Fixation (KO-TRAUMA-PROC-001), Osteoporotic Fracture (KO-TRAUMA-COND-003)
- Proposed new topics: Radius (anatomy), DASH questionnaire (outcome measure), Patient-Rated Wrist Evaluation (outcome measure), Wrist x-ray (diagnostic test), Compartment syndrome (condition)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Wrist Injuries and Disorders.* https://medlineplus.gov/wristinjuriesanddisorders.html (retrieved 2026-10-26)
2. [S2] MedlinePlus, U.S. National Library of Medicine. *Fractures.* https://medlineplus.gov/fractures.html (retrieved 2026-10-26)
3. [S3] Western Journal of Emergency Medicine. *Emergency Medicine Management of Distal Radius and Ulna Fractures: Narrative Review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC13436675/ (retrieved 2026-10-26)
4. [S4] BMC Surgery. *Non-surgical vs. surgical treatment of distal radius fractures: a meta-analysis of randomized controlled trials.* https://pmc.ncbi.nlm.nih.gov/articles/PMC11234633/ (retrieved 2026-10-26)
5. [S5] JAMA Network Open. *Association of Open Reduction and Internal Fixation With Volar Locking Plate for Distal Radius Fractures With Patient-Reported Outcomes in Older Adults.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10276304/ (retrieved 2026-10-26)
