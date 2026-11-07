---
schema_version: okds-ko-1.0
ko_id: KO-HAND-ANAT-002
title: Carpal Tunnel
preferred_term: Carpal Tunnel
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
summary: The carpal tunnel is a narrow, stiff passage at the base of the hand, made of wrist bones and
  a ligament that forms its roof [S1][S3][S4]. The median nerve and the tendons that bend the fingers
  pass through it from the forearm into the hand [S1][S3]. Because the space is tight, swelling inside
  it can press on the nerve and cause carpal tunnel syndrome [S1][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- wrist anatomy
- transverse carpal ligament
- flexor retinaculum
- flexor tendons
- median nerve
- carpal bones
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-COND-001
  target_label: Carpal Tunnel Syndrome
  source_ids:
  - S1
  - S3
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-DX-002
  target_label: Phalen's Test
  source_ids:
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-TRT-002
  target_label: Corticosteroid Injection
  source_ids:
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-PROC-001
  target_label: Carpal Tunnel Release
  source_ids:
  - S1
  - S2
proposed_concepts:
- term: Transverse Carpal Ligament (flexor retinaculum)
  suggested_type: AnatomicalStructure
  predicate: PART_OF
  reason: S2 and S4 say this ligament forms the tunnel's roof; would allow Transverse Carpal Ligament
    PART_OF Carpal Tunnel.
- term: Carpal Bones
  suggested_type: AnatomicalStructure
  predicate: PART_OF
  reason: S4 says the two rows of carpal bones form the tunnel; would allow Carpal Bones PART_OF Carpal
    Tunnel or the reverse.
sources:
- id: S1
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
- id: S2
  title: Clinical-applied anatomy of the carpal tunnel regarding mini-invasive carpal tunnel release (Kaiser
    et al.)
  publisher: Archives of Orthopaedic and Trauma Surgery, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11582268/
  source_type: journal_article
  audience: clinician
  publication_date: '2024-10-16'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: CC BY 4.0. Kaiser P, Schmidle G, Bode S, Seeher U, Honis HR, Moriggl B, Pechriggl E, Stofferin
    H, Konschake M. Arch Orthop Trauma Surg 2024;144(11):4753-4765. doi:10.1007/s00402-024-05560-7. Accepted
    2024-09-05. Cadaver study (104 wrists). No figures used.
- id: S3
  title: Carpal Tunnel Syndrome (Overview, Symptoms, & Causes)
  publisher: NIAMS (NIH)
  url: https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome
  source_type: government_health_page
  audience: patient
  publication_date: 2023-12
  retrieved_date: '2026-11-01'
  permitted_use: public_domain
  notes: US government text. Page says 'Last reviewed December 2023' (no day shown).
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
  - Measurements (ligament about 25 mm long; tunnel about 15-17 mm wide; about a quarter of wrists with
    a nerve or vessel within 3 mm of the cutting path) come from one cadaver study (S2, 104 wrists, donors'
    mean age 81). Clinician check that they are presented fairly.
  - S4 says the tunnel's 'depression' is made of carpal bones; the KO states this as 'floor and sides'.
    Clinician check.
  - Short plain-language definitions (e.g., 'radius (a forearm bone)', 'synovial tissue, the lining around
    the tendons') were written by the drafter; check them.
  - The StatPearls flexor retinaculum chapter (NBK545198) was not used (robot check blocks Fetch; paste
    by hand if needed, paraphrase only).
  - MeSH ID is unknown and set to verify. ICD-10-CM does not usually apply to a body part; the team should
    decide whether to leave it empty.
  - The vocab has no predicate for 'passes through', so there is no direct link between Carpal Tunnel
    and Median Nerve (KO-HAND-ANAT-001). Team decision needed.
  - NIAMS page (S3) shows only 'Last reviewed December 2023', so publication_date is 2023-12 (no day).
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-01'
last_updated: '2026-11-01'
update_triggers:
- MedlinePlus or NIAMS shows a new 'last updated' or 'last reviewed' date on a cited page.
- New anatomy or ultrasound studies change advice on checking the carpal tunnel before minimally invasive
  release.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-01'
  by: OKDS agent (Claude)
  change: Initial draft written by the OKDS agent from source pack SP-KO-HAND-ANAT-002 (claude-opus-5-5,
    okds-gen-1.0).
---

## Summary
The carpal tunnel is a narrow, stiff passage at the base of the hand, made of wrist bones and a ligament that forms its roof [S1][S3][S4]. The median nerve and the tendons that bend the fingers pass through it from the forearm into the hand [S1][S3]. Because the space is tight, swelling inside it can press on the nerve and cause carpal tunnel syndrome [S1][S3].

## Key Facts (claim → source)
- The carpal tunnel is a narrow opening between the wrist bones and the ligament that holds them together [S1].
- The wrist bones, called carpal bones, form its floor and sides [S4].
- Its roof is the transverse carpal ligament, also called the flexor retinaculum [S2][S4].
- Nine tendons that bend the fingers pass through it, along with the median nerve [S3][S4].
- The tunnel keeps the finger-bending tendons from bowing out when the wrist bends [S4].
- In one study of 104 wrists, the ligament roof was about 25 mm (about 1 inch) long on average [S2].
- Swelling or crowding in the tunnel can squeeze the median nerve, which causes carpal tunnel syndrome [S1][S3].
- Carpal tunnel release surgery cuts the ligament roof to give the nerve more room [S1][S2].

## Explanation
### Where it is
The carpal tunnel sits in the wrist at the base of the hand [S1][S3]. Its floor and sides are made by two rows of carpal bones, the bones of the wrist [S4]. Across the top runs the transverse carpal ligament, also called the flexor retinaculum, which is the roof of the tunnel [S2][S4]. A ligament is tissue that holds bones together [S1]. The roof is anchored to bony points on both sides of the wrist: the scaphoid and trapezium on one side, and the pisiform and the hook of the hamate on the other [S2][S4].

In a study of 104 wrists from 52 body donors, the ligament averaged about 25 mm long, and the tunnel was about 17 mm wide at the forearm end and 15 mm wide at the hand end [S2]. The tunnel is a "rigid" space, which means its walls do not stretch much [S3]. One review reports that women tend to have a smaller tunnel than men [S4].

### What it does
The carpal tunnel is the pathway that the median nerve and the finger-bending tendons use to get from the forearm into the hand [S1][S3]. These structures pass through it [S3][S4]:
- **The median nerve**, which gives feeling to the thumb, index, middle, and part of the ring finger and controls small thumb muscles [S3].
- **Nine flexor tendons**: four flexor digitorum superficialis tendons, four flexor digitorum profundus tendons, and the flexor pollicis longus tendon [S4].

Tendons are cords that connect muscles in the arm to the finger bones, so the fingers can bend [S1]. The tunnel keeps these tendons from bowing out of place when the wrist bends [S4]. The ligament roof also steadies the wrist bones and acts like a pulley for the finger-bending tendons [S2].

### Conditions that affect it
- **Carpal tunnel syndrome (CTS):** if the tendons in the tunnel swell or get irritated, they can press on the median nerve, leading to numbness, weakness, and other symptoms [S1][S3].
- **Swollen tendon lining:** the most common way pressure builds is thickening of the synovial tissue, the lining around the tendons, from heavy use, injury, or arthritis [S4].
- **Rheumatoid arthritis:** joint lining that grows too much can narrow the space in the tunnel [S4].
- **Bent wrists:** bending the wrist for a long time raises pressure in the tunnel, which is one reason symptoms are often worse at night [S4]. Phalen's test uses this idea: pressing the backs of the hands together squeezes the nerve between the ligament and the end of the radius (a forearm bone) to see if symptoms appear [S4].
- **Treatment inside the tunnel:** steroid injections into the carpal tunnel are a non-surgical way to calm swelling of the tendon lining [S4].
- **Wrist injury:** rarely, a fall on an outstretched hand or a car crash can push a wrist bone, the lunate, into the tunnel and block it [S4].

In carpal tunnel release surgery, the surgeon cuts the ligament roof to take pressure off the nerve [S1][S2]. This can be done through an open cut, with a small camera (endoscopic), or with ultrasound guidance [S2]. The surgery helps most people, but nearby nerves and blood vessels can sometimes be injured [S2]. A study of donor wrists found that in about a quarter of wrists, a nerve or blood vessel sat very close to where a cutting tool goes in minimally invasive surgery [S2]. The authors suggest an ultrasound check before these small-opening surgeries and open surgery for high-risk patients [S2].

## Common Misunderstandings
- **Myth:** "Carpal tunnel" is the name of a disease. **Fact:** The carpal tunnel is a normal part of the wrist; carpal tunnel syndrome is the condition that happens when the nerve inside it is squeezed [S1][S3].
- **Myth:** The carpal tunnel can stretch to make room when tissues swell. **Fact:** It is a narrow, rigid tube, so swelling inside it presses on the nerve [S1][S3].
- **Myth:** Only the median nerve goes through the carpal tunnel. **Fact:** Nine finger-bending tendons pass through it too [S3][S4].
- **Myth:** Everyone's carpal tunnel area looks the same. **Fact:** The nerves and blood vessels near the tunnel vary a lot from person to person [S2].

## Questions to Ask Your Doctor
1. Is something crowding my carpal tunnel, such as swollen tendons?
2. Could an imaging test, such as ultrasound, show what is happening inside my carpal tunnel?
3. If I need carpal tunnel surgery, which type do you suggest, and why?
4. Are there nerves or blood vessels near my carpal tunnel that need extra care during surgery?

## Test Questions
1. What forms the roof of the carpal tunnel? - The transverse carpal ligament, also called the flexor retinaculum [S2][S4].
2. What passes through the carpal tunnel? - The median nerve and nine tendons that bend the fingers [S3][S4].
3. What forms the floor and sides of the carpal tunnel? - The carpal bones of the wrist [S4].
4. Why can swelling in the carpal tunnel cause symptoms? - The tunnel is narrow and rigid, so swelling presses on the median nerve [S1][S3].
5. What is cut in carpal tunnel release surgery? - The transverse carpal ligament, the roof of the tunnel [S1][S2].

## Related Topics
- Read next: Carpal Tunnel Syndrome (KO-HAND-COND-001)
- Read next: Phalen's Test (KO-HAND-DX-002)
- Read next: Corticosteroid Injection (KO-HAND-TRT-002)
- Read next: Carpal Tunnel Release (KO-HAND-PROC-001)

## References
1. [S1] MedlinePlus (National Library of Medicine). *Carpal Tunnel Syndrome.* https://medlineplus.gov/carpaltunnelsyndrome.html (retrieved 2026-11-01)
2. [S2] Archives of Orthopaedic and Trauma Surgery, via PubMed Central. *Clinical-applied anatomy of the carpal tunnel regarding mini-invasive carpal tunnel release (Kaiser et al.).* https://pmc.ncbi.nlm.nih.gov/articles/PMC11582268/ (retrieved 2026-11-01)
3. [S3] NIAMS (NIH). *Carpal Tunnel Syndrome (Overview, Symptoms, & Causes).* https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome (retrieved 2026-11-01)
4. [S4] Cureus, via PubMed Central. *Carpal Tunnel Syndrome: Pathophysiology and Comprehensive Guidelines for Clinical Evaluation and Treatment (Joshi et al.).* https://pmc.ncbi.nlm.nih.gov/articles/PMC9389835/ (retrieved 2026-11-01)
