---
schema_version: okds-ko-1.0
ko_id: KO-HAND-ANAT-001
title: Median Nerve
preferred_term: Median Nerve
alternate_terms: []
ko_type: AnatomicalStructure
specialty: HAND
cluster: 1
audience:
- patient
- caregiver
- student
reading_level: grade 6-8
difficulty: beginner
summary: The median nerve is a nerve that runs from the forearm, through the carpal tunnel in the wrist,
  and into the palm [S1][S2]. It gives feeling to the thumb, index finger, middle finger, and part of
  the ring finger, and it controls small muscles at the base of the thumb [S1]. When it is squeezed at
  the wrist, the result is carpal tunnel syndrome [S1][S2].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- nerve
- hand anatomy
- wrist
- thumb muscles
- finger feeling
- carpal tunnel
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-COND-001
  target_label: Carpal Tunnel Syndrome
  source_ids:
  - S1
  - S2
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-DX-001
  target_label: Nerve Conduction Study
  source_ids:
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-DX-002
  target_label: Phalen's Test
  source_ids:
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-PROC-001
  target_label: Carpal Tunnel Release
  source_ids:
  - S3
proposed_concepts:
- term: Brachial Plexus
  suggested_type: AnatomicalStructure
  predicate: PART_OF
  reason: S3 says the median nerve arises from the brachial plexus (C5-T1); would allow Median Nerve PART_OF
    Brachial Plexus.
- term: Thenar Motor Branch (recurrent branch of the median nerve)
  suggested_type: AnatomicalStructure
  predicate: PART_OF
  reason: S3 describes this branch and its variations in detail; would allow Thenar Motor Branch PART_OF
    Median Nerve.
sources:
- id: S1
  title: Carpal Tunnel Syndrome (Overview, Symptoms, & Causes)
  publisher: NIAMS (NIH)
  url: https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome
  source_type: government_health_page
  audience: patient
  publication_date: 2023-12
  retrieved_date: '2026-11-01'
  permitted_use: public_domain
  notes: US government text. Page says 'Last reviewed December 2023' (no day shown).
- id: S2
  title: Carpal Tunnel Syndrome
  publisher: MedlinePlus (National Library of Medicine)
  url: https://medlineplus.gov/carpaltunnelsyndrome.html
  source_type: government_health_page
  audience: patient
  publication_date: '2024-01-10'
  retrieved_date: '2026-11-01'
  permitted_use: public_domain
  notes: 'US government text (MedlinePlus health-topic Summary). Credit: MedlinePlus, National Library
    of Medicine.'
- id: S3
  title: 'The Prevalence of Anatomical Variations of the Median Nerve in the Carpal Tunnel: A Systematic
    Review and Meta-Analysis (Henry et al.)'
  publisher: PLoS One, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4549253/
  source_type: systematic_review
  audience: clinician
  publication_date: '2015-08-25'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: CC BY (Creative Commons Attribution License). Henry BM, Zwinczewska H, Roy J, Vikse J, Ramakrishnan
    PK, Walocha JA, Tomaszewski KA. PLoS One 2015;10(8):e0136477. doi:10.1371/journal.pone.0136477. No
    figures used.
- id: S4
  title: 'Carpal Tunnel Syndrome: Pathophysiology and Comprehensive Guidelines for Clinical Evaluation
    and Treatment (Joshi et al.)'
  publisher: Cureus, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9389835/
  source_type: journal_article
  audience: clinician
  publication_date: '2022-07-20'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: CC BY (Creative Commons Attribution License). Joshi A, Patel K, Mohamed A, Oak S, Zhang MH, Hsiung
    H, Zhang A, Patel UK. Cureus 2022;14(7):e27053. doi:10.7759/cureus.27053. Figure 1 is CC BY-NC; no
    figures used.
review:
  status: draft
  author: OKDS agent (Claude)
  generated_by:
    model: claude-opus-5-5
    prompt_version: okds-gen-1.0
  ai_check: null
  team_checker: null
  clinician_reviewer: null
  clinician_role: null
  review_date: null
  open_issues:
  - 'The best anatomy source (StatPearls ''Anatomy, Shoulder and Upper Limb, Median Nerve'', NBK448084)
    could not be fetched (robot check). The nerve''s path above the wrist (arm, elbow, forearm branches)
    is thin; consider pasting it by hand (CC BY-NC-ND: paraphrase only).'
  - MeSH ID is unknown and set to verify. ICD-10-CM does not usually apply to a body part; the team should
    decide whether to leave it empty.
  - 'Clinician check: percentages from the 2015 meta-analysis (S3): thenar motor branch after the tunnel
    in about 75% of hands; same pattern in both hands in about 7 of 10 people studied.'
  - The vocab has no predicate for 'passes through', so there is no direct link between Median Nerve and
    Carpal Tunnel (KO-HAND-ANAT-002). Team decision needed.
  - Muscle names (opponens pollicis, abductor pollicis brevis, lumbricals) and 'medial and lateral branches'
    are kept as source terms for students; an editor may want simpler wording for patients.
  - NIAMS page (S1) shows only 'Last reviewed December 2023', so publication_date is 2023-12 (no day).
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-01'
last_updated: '2026-11-01'
update_triggers:
- NIAMS or MedlinePlus shows a new 'last reviewed' or 'last updated' date on a cited page.
- A new systematic review of median nerve variations in the carpal tunnel is published.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-01'
  by: OKDS agent (Claude)
  change: Initial draft written by the OKDS agent from source pack SP-KO-HAND-ANAT-001 (claude-opus-5-5,
    okds-gen-1.0).
---

## Summary
The median nerve is a nerve that runs from the forearm, through the carpal tunnel in the wrist, and into the palm [S1][S2]. It gives feeling to the thumb, index finger, middle finger, and part of the ring finger, and it controls small muscles at the base of the thumb [S1]. When it is squeezed at the wrist, the result is carpal tunnel syndrome [S1][S2].

## Key Facts (claim → source)
- The median nerve has both motor fibers, which move muscles, and sensory fibers, which carry feeling [S3].
- It starts from nerve roots in a network called the brachial plexus, at spinal levels C5 to T1 [S3].
- At the wrist it passes through the carpal tunnel, under the transverse carpal ligament, together with nine tendons that bend the fingers [S1][S3][S4].
- It gives feeling to the palm side of the thumb, index, middle, and half of the ring finger, but not the little finger [S1][S4].
- It controls small muscles at the base of the thumb and helps the thumb move [S1][S2].
- The branch that controls the thumb muscles takes different paths in different people, which matters in wrist surgery [S3].
- Squeezing of the median nerve at the wrist causes carpal tunnel syndrome [S1][S2].

## Explanation
### Where it is
The median nerve begins at the brachial plexus, a group of spinal nerve roots that supply the nerves of the arm [S3][S4]. It travels down the arm and forearm to the wrist [S1][S4]. At the wrist it passes through the carpal tunnel, a narrow, stiff tube of ligament and bones at the base of the hand [S1][S3]. Inside the tunnel it lies deep to (underneath) the transverse carpal ligament, next to nine flexor tendons: four flexor digitorum superficialis tendons, four flexor digitorum profundus tendons, and the flexor pollicis longus tendon [S3][S4]. Tendons are cords that connect arm muscles to finger bones so the fingers can bend [S2].

After it leaves the tunnel, the nerve splits into two main branches, called the medial and lateral branches [S3]. These branches become smaller nerves, called digital nerves, that go to the palm and fingers [S3].

### What it does
The median nerve does two jobs: it carries feeling and it moves muscles [S3].
- **Feeling:** it gives feeling to the thumb, index finger, middle finger, and part of the ring finger [S1][S4]. It does not give feeling to the little finger [S1].
- **Movement:** it controls small muscles at the base of the thumb, which helps the thumb move [S1][S2].

The thenar motor branch, also called the recurrent branch, is the part that controls the thumb muscles [S3]. These muscles are the opponens pollicis, the abductor pollicis brevis, and part of the flexor pollicis brevis [S3]. If this branch is damaged, the thumb can become weak and lose some of its normal movement [S3]. The nerve also controls two small hand muscles called the first and second lumbricals [S3].

Not everyone's median nerve looks the same [S3]. A large review of 31 studies (3,918 hands) found the thenar motor branch usually branches off after the tunnel, in about 75% of hands [S3]. In others it branches inside the tunnel and runs under or through the ligament, and the through-the-ligament path is at high risk of injury during carpal tunnel surgery [S3]. In about 7 of 10 people studied, both hands had the same branch pattern [S3].

### Conditions that affect it
- **Carpal tunnel syndrome (CTS):** the median nerve gets pressed or squeezed at the wrist, often because swollen tendons or tissue crowd the tunnel [S1][S2]. This can cause numbness, weakness, and other symptoms in the hand [S2].
- **Long-term pressure:** in long-lasting or untreated CTS, the fingers can stay numb and the thumb muscles can become very weak [S1][S2].
- **Injury during surgery:** because the nerve's branches vary so much, surgeons need good knowledge of its anatomy to avoid harming it during carpal tunnel release [S3].
- **Problems that look similar:** a pinched nerve root in the spine, for example from a slipped disc, can cause hand symptoms like CTS, so doctors map where the numbness is to tell them apart [S4].

Tests can check how well the median nerve works [S4]. A nerve conduction study measures how fast signals travel along the nerve across the carpal tunnel [S4]. Electromyography (EMG) tests a thumb muscle the nerve controls, the abductor pollicis brevis [S4]. On ultrasound, a nerve that is squeezed in the tunnel can look larger than normal [S4]. In Phalen's test, the backs of the hands are pressed together, which adds pressure on the nerve to see if symptoms appear [S4].

## Common Misunderstandings
- **Myth:** The median nerve gives feeling to all five fingers. **Fact:** It covers the thumb, index, middle, and part of the ring finger, but not the little finger [S1][S4].
- **Myth:** The median nerve only carries feeling. **Fact:** It has motor fibers too and controls muscles at the base of the thumb [S1][S3].
- **Myth:** Everyone's median nerve follows the same path in the wrist. **Fact:** Its course and branches vary widely, and the pattern can even differ between a person's two hands [S3].
- **Myth:** Tingling in the hand always means a problem at the wrist. **Fact:** A pinched nerve root in the spine can cause similar hand symptoms [S4].

## Questions to Ask Your Doctor
1. Is my numbness in the area that the median nerve covers?
2. Could the problem be at my wrist, or higher up, such as in my spine?
3. Which tests can show how well my median nerve is working?
4. If I need wrist surgery, how will the surgeon protect the nerve and its branches?

## Test Questions
1. Where does the median nerve pass through at the wrist? - The carpal tunnel [S1][S2].
2. Which fingers get feeling from the median nerve? - The thumb, index finger, middle finger, and part of the ring finger [S1].
3. What does the thenar motor branch of the median nerve control? - Muscles at the base of the thumb, such as the abductor pollicis brevis [S3].
4. What condition happens when the median nerve is squeezed at the wrist? - Carpal tunnel syndrome [S1][S2].
5. Which test measures how fast signals travel along the median nerve across the carpal tunnel? - A nerve conduction study [S4].
6. Where does the thenar motor branch most often split off from the median nerve? - After the carpal tunnel, in about 75% of hands [S3].

## Related Topics
- Read next: Carpal Tunnel Syndrome (KO-HAND-COND-001)
- Read next: Nerve Conduction Study (KO-HAND-DX-001), Phalen's Test (KO-HAND-DX-002)
- Read next: Carpal Tunnel Release (KO-HAND-PROC-001)

## References
1. [S1] NIAMS (NIH). *Carpal Tunnel Syndrome (Overview, Symptoms, & Causes).* https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome (retrieved 2026-11-01)
2. [S2] MedlinePlus (National Library of Medicine). *Carpal Tunnel Syndrome.* https://medlineplus.gov/carpaltunnelsyndrome.html (retrieved 2026-11-01)
3. [S3] PLoS One, via PubMed Central. *The Prevalence of Anatomical Variations of the Median Nerve in the Carpal Tunnel: A Systematic Review and Meta-Analysis (Henry et al.).* https://pmc.ncbi.nlm.nih.gov/articles/PMC4549253/ (retrieved 2026-11-01)
4. [S4] Cureus, via PubMed Central. *Carpal Tunnel Syndrome: Pathophysiology and Comprehensive Guidelines for Clinical Evaluation and Treatment (Joshi et al.).* https://pmc.ncbi.nlm.nih.gov/articles/PMC9389835/ (retrieved 2026-11-01)
