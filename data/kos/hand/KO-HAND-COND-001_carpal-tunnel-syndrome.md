---
schema_version: okds-ko-1.0
ko_id: KO-HAND-COND-001
title: Carpal Tunnel Syndrome
preferred_term: Carpal Tunnel Syndrome
alternate_terms:
- CTS
- median nerve compression at the wrist
- median nerve entrapment
ko_type: Condition
specialty: HAND
cluster: 2
audience:
- patient
- caregiver
- student
reading_level: grade 6-8
difficulty: beginner
summary: Carpal tunnel syndrome (CTS) is a common condition in which the median nerve, a nerve that carries
  feeling and movement signals into the hand, gets squeezed at the wrist [S1][S2]. It can cause numbness,
  tingling, burning, pain, or weakness, most often in the thumb, index finger, and middle finger [S1][S2].
  It is easier to treat early, and options range from a night splint to surgery [S1][S3].
codes:
  mesh: <verify>
  icd10cm: G56.0-
tags:
- hand numbness
- tingling fingers
- wrist
- median nerve
- nerve compression
- night splint
relationships:
- predicate: AFFECTS
  target_id: KO-HAND-ANAT-001
  target_label: Median Nerve
  source_ids:
  - S1
  - S2
  - S4
- predicate: AFFECTS
  target_id: KO-HAND-ANAT-002
  target_label: Carpal Tunnel
  source_ids:
  - S1
  - S2
  - S4
- predicate: DIAGNOSED_BY
  target_id: KO-HAND-DX-001
  target_label: Nerve Conduction Study
  source_ids:
  - S3
  - S4
- predicate: DIAGNOSED_BY
  target_id: KO-HAND-DX-002
  target_label: Phalen's Test
  source_ids:
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-TRT-001
  target_label: Wrist Splinting
  source_ids:
  - S1
  - S3
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-TRT-002
  target_label: Corticosteroid Injection
  source_ids:
  - S1
  - S3
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-PROC-001
  target_label: Carpal Tunnel Release
  source_ids:
  - S1
  - S3
proposed_concepts:
- term: Electromyography (EMG)
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S3 and S4 describe EMG as a test used for CTS; it is not in the registry.
- term: Wrist ultrasound
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S1, S3, and S4 say ultrasound can show a swollen median nerve in the tunnel.
- term: Numbness and tingling in the fingers
  suggested_type: Concept
  predicate: HAS_SYMPTOM
  reason: Main symptom in S1, S2, and S4; needs a Concept KO before a HAS_SYMPTOM link can be made.
- term: Repetitive hand and wrist motion
  suggested_type: Concept
  predicate: HAS_RISK_FACTOR
  reason: S1 and S2 list repeated hand motions and vibrating tools as factors; needs a Concept KO.
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
  title: Carpal Tunnel Syndrome (Overview, Symptoms, & Causes)
  publisher: NIAMS (NIH)
  url: https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome
  source_type: government_health_page
  audience: patient
  publication_date: 2023-12
  retrieved_date: '2026-11-01'
  permitted_use: public_domain
  notes: US government text. Page says 'Last reviewed December 2023' (no day shown).
- id: S3
  title: 'Carpal Tunnel Syndrome: Diagnosis, Treatment, and Steps to Take'
  publisher: NIAMS (NIH)
  url: https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome/diagnosis-treatment-and-steps-to-take
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
  - 'Clinician check: S3 (NIAMS) says most cases can be diagnosed by physical exam, while S4 (Joshi) says
    exam tests alone are not enough for a definite diagnosis. The KO states both; confirm the wording.'
  - 'Clinician check: Phalen''s test timing (30 to 60 seconds) and the ''women about three times as likely''
    figure come from S1/S4; confirm.'
  - MeSH ID is unknown and set to verify. Confirm the ICD-10-CM code G56.0- from the registry and whether
    subcodes should be listed.
  - S4 cites an older AAOS guideline. The 2024 AAOS CTS guideline (OrthoGuidelines, link_and_paraphrase)
    is not in this pack, so no evidence strength is given for treatments; consider adding it.
  - NIAMS pages (S2, S3) show only 'Last reviewed December 2023', so publication_date is 2023-12 (no day).
  - No source in this pack compares CTS with Cubital Tunnel Syndrome, so no CONTRASTS_WITH link was added.
  - Short plain-language explanations of terms (e.g., 'rheumatoid arthritis, an autoimmune disease that
    inflames joints') were written by the drafter; check they match the sources.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-01'
last_updated: '2026-11-01'
update_triggers:
- MedlinePlus or NIAMS shows a new 'last updated' or 'last reviewed' date on a cited carpal tunnel page.
- AAOS updates its carpal tunnel syndrome clinical practice guideline.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-01'
  by: OKDS agent (Claude)
  change: Initial draft written by the OKDS agent from source pack SP-KO-HAND-COND-001 (claude-opus-5-5,
    okds-gen-1.0).
---

## Summary
Carpal tunnel syndrome (CTS) is a common condition in which the median nerve, a nerve that carries feeling and movement signals into the hand, gets squeezed at the wrist [S1][S2]. It can cause numbness, tingling, burning, pain, or weakness, most often in the thumb, index finger, and middle finger [S1][S2]. It is easier to treat early, and options range from a night splint to surgery [S1][S3].

## Key Facts (claim → source)
- CTS happens when the median nerve is squeezed inside the carpal tunnel, a narrow, stiff passage of wrist bones and ligament at the base of the hand [S1][S2].
- CTS, the most common trapped-nerve problem, usually affects adults, and women are about three times as likely as men to get it [S1][S2][S4].
- Symptoms often start slowly and at night, in the thumb, index, middle, and part of the ring finger, but not the little finger [S2][S4].
- Diagnosis starts with a health history and physical exam, and nerve tests, ultrasound, lab tests, or X-rays are added when needed [S1][S3].
- A night splint and a steroid shot are common non-surgical treatments, but their relief is usually short-term [S3][S4].
- Carpal tunnel release surgery cuts a ligament to take pressure off the nerve, and CTS rarely comes back after it [S1][S3].

## Explanation
### What it is
The carpal tunnel is a narrow opening at the base of the hand, formed by wrist bones and the ligament that holds them together [S1][S2]. The median nerve and the tendons that bend the fingers pass through it from the forearm into the hand [S1][S2]. If the tendons or the tissue around them swell, the tunnel gets crowded and the nerve is pressed [S1][S4].

### Causes and risk factors
Often no single cause is found, and a mix of factors that raise pressure in the tunnel is usually involved [S1][S2]. Linked factors include [S1][S2]:
- A wrist injury that causes swelling, such as a sprain or a broken bone [S1][S2].
- Diabetes, rheumatoid arthritis (an autoimmune disease that inflames joints), or thyroid or pituitary gland problems [S1][S2].
- Fluid buildup from hormone changes, such as in pregnancy or menopause [S1][S2].
- Repeating the same hand and wrist motions, or using tools that vibrate [S1][S2].
- Being a woman, or having a parent, brother, or sister who has had CTS [S1][S2].

One review suggests women may be at higher risk partly because their carpal tunnel tends to be smaller [S4]. Researchers are not sure whether long-term typing or computer use leads to CTS [S1].

### Symptoms
- Numbness, tingling, or burning in the thumb, index, and middle fingers, and sometimes part of the ring finger [S1][S2].
- Night symptoms that may wake a person, who then wants to "shake out" the hand [S2].
- Later, daytime symptoms during tasks like driving, holding a phone, or reading [S1][S2].
- A weaker grip and trouble holding small things like buttons or zippers [S2][S4].

Symptoms often affect both hands, and they are often worse at night because bent wrists during sleep add pressure in the tunnel [S1][S4].

### How it is diagnosed
A health care provider asks about symptoms and health history, and examines the hands, arms, shoulders, and neck to rule out other causes [S1][S3]. The provider may tap or press over the median nerve, or bend the wrist, to see if this brings on tingling [S3]. Named exam tests include Phalen's test, where the backs of the hands are pressed together for 30 to 60 seconds, and the Tinel sign, where the provider taps over the nerve [S4]. NIAMS says most cases can be diagnosed with a physical exam [S3]. One review adds that exam tests alone may not give a sure answer, so they are often paired with other tests [S4]:
- A nerve conduction study measures how fast signals travel along the nerve, to see if they slow down at the carpal tunnel [S3][S4].
- Electromyography (EMG) checks the muscles the nerve controls [S3][S4].
- Ultrasound can show if the median nerve is swollen in the tunnel [S1][S3].
- Lab tests and X-rays look for broken bones, arthritis, or nerve-damaging diseases such as diabetes [S1][S3].

### Treatment options
Treatment should start as soon as possible, beginning with any health problem that may be causing the symptoms, such as diabetes or arthritis [S1][S3].
- **Wrist splint:** a hand and wrist brace worn at night is a common first treatment [S1][S3]. It holds the wrist in a neutral position to ease pressure on the nerve [S4].
- **Medicines:** over-the-counter pain relievers or prescription steroids, as pills or a shot into the wrist, can reduce swelling and pain [S1]. A steroid shot can ease symptoms for a while, but symptoms may return [S3][S4].
- **Surgery (carpal tunnel release):** a surgeon cuts the ligament over the tunnel to make more room for the nerve, through an open cut or with a small camera (endoscopic surgery) [S1][S3]. It may be an option when symptoms are severe or other treatments do not work [S1][S4]. Recovery can take months, and risks include infection, nerve damage, stiffness, or scar pain [S1][S3].

Non-surgical treatments can help in the short term, but they do not fix the underlying problem with the nerve [S3].

### When to seek care
Early diagnosis and treatment can help prevent lasting nerve damage, such as lost feeling in some fingers or permanent thumb weakness [S1][S3]. So hand numbness, tingling, or weakness is worth checking with a health care provider [S1][S3]. In long-lasting or untreated CTS, the fingers can stay numb all the time, small objects become hard to grab, and the muscles at the base of the thumb can get weak [S2].

## Common Misunderstandings
- **Myth:** Typing on a computer is a proven cause of CTS. **Fact:** Researchers are not sure whether long-term typing or computer use leads to CTS [S1].
- **Myth:** A splint or a steroid shot cures CTS. **Fact:** They can ease symptoms for a while, but they do not fix the underlying problem [S3][S4].
- **Myth:** CTS makes all five fingers numb. **Fact:** The median nerve does not give feeling to the little finger, so CTS does not affect it [S2][S4].
- **Myth:** CTS usually comes back after surgery. **Fact:** It rarely returns after surgery, though some mild symptoms may last [S1][S3].

## Questions to Ask Your Doctor
1. Could my symptoms be carpal tunnel syndrome, or could something else be the cause?
2. Do I need a nerve conduction study, an EMG, or an ultrasound?
3. Should I try a night splint first, and how will we know if it is working?
4. When would a steroid shot or surgery make sense for me?

## Test Questions
1. Which nerve is squeezed in carpal tunnel syndrome, and where? - The median nerve, inside the carpal tunnel at the wrist [S1][S2].
2. Which fingers usually feel numb or tingly in CTS? - The thumb, index, middle, and part of the ring finger, but not the little finger [S2][S4].
3. Name two things that raise the chance of getting CTS. - Examples: a wrist injury, diabetes, rheumatoid arthritis, pregnancy, or repeated hand motions [S1][S2].
4. What does a nerve conduction study check in CTS? - How fast signals travel along the median nerve, to see if they slow down at the carpal tunnel [S3][S4].
5. What is a common first treatment for CTS symptoms? - Wearing a hand and wrist splint at night [S3].
6. What happens in carpal tunnel release surgery? - The surgeon cuts the ligament over the carpal tunnel to take pressure off the median nerve [S1][S3].

## Related Topics
- Affects: Median Nerve (KO-HAND-ANAT-001), Carpal Tunnel (KO-HAND-ANAT-002)
- Diagnosed by: Nerve Conduction Study (KO-HAND-DX-001), Phalen's Test (KO-HAND-DX-002)
- Read next: Wrist Splinting (KO-HAND-TRT-001), Corticosteroid Injection (KO-HAND-TRT-002), Carpal Tunnel Release (KO-HAND-PROC-001)

## References
1. [S1] MedlinePlus (National Library of Medicine). *Carpal Tunnel Syndrome.* https://medlineplus.gov/carpaltunnelsyndrome.html (retrieved 2026-11-01)
2. [S2] NIAMS (NIH). *Carpal Tunnel Syndrome (Overview, Symptoms, & Causes).* https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome (retrieved 2026-11-01)
3. [S3] NIAMS (NIH). *Carpal Tunnel Syndrome: Diagnosis, Treatment, and Steps to Take.* https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome/diagnosis-treatment-and-steps-to-take (retrieved 2026-11-01)
4. [S4] Cureus, via PubMed Central. *Carpal Tunnel Syndrome: Pathophysiology and Comprehensive Guidelines for Clinical Evaluation and Treatment (Joshi et al.).* https://pmc.ncbi.nlm.nih.gov/articles/PMC9389835/ (retrieved 2026-11-01)
