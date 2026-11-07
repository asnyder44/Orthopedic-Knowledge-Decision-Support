---
schema_version: okds-ko-1.0
ko_id: KO-HAND-TRT-001
title: Wrist Splinting
preferred_term: Wrist Splinting
alternate_terms:
- wrist brace
- night splint
- wrist orthosis
- night-resting splint
- bracing
ko_type: Treatment
specialty: HAND
cluster: 4
audience:
- patient
- caregiver
- student
reading_level: grade 6-8
difficulty: beginner
summary: Wrist splinting means wearing a brace that holds the wrist straight or tilted slightly back,
  usually at night, to ease carpal tunnel syndrome symptoms [S1][S2][S4]. It is a common, low-cost first
  treatment with few lasting side effects, but research shows only small, mostly short-term benefits [S1][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- carpal tunnel syndrome treatment
- non-surgical treatment
- wrist brace
- night splint
- orthosis
- self-care
- hand numbness at night
relationships:
- predicate: TREATS
  target_id: KO-HAND-COND-001
  target_label: Carpal Tunnel Syndrome
  source_ids:
  - S1
  - S2
  - S3
  - S4
- predicate: ALTERNATIVE_TO
  target_id: KO-HAND-TRT-002
  target_label: Corticosteroid Injection
  source_ids:
  - S1
  - S2
- predicate: ALTERNATIVE_TO
  target_id: KO-HAND-PROC-001
  target_label: Carpal Tunnel Release
  source_ids:
  - S1
  - S3
proposed_concepts:
- term: Wrist splint (wrist orthosis or brace)
  suggested_type: Device
  predicate: USES_DEVICE
  reason: S2, S3 and S4 describe the splint itself (neutral or slightly extended position, sizing, MP-joint
    designs).
- term: Hand therapy (nerve and tendon gliding exercises)
  suggested_type: Treatment
  predicate: ALTERNATIVE_TO
  reason: S4 lists hand therapy as another non-surgical option for carpal tunnel syndrome.
sources:
- id: S1
  title: 'Carpal Tunnel Syndrome: Diagnosis, Treatment, and Steps to Take'
  publisher: NIAMS (NIH)
  url: https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome/diagnosis-treatment-and-steps-to-take
  source_type: government_health_page
  audience: patient
  publication_date: 2023-12
  retrieved_date: '2026-11-01'
  permitted_use: public_domain
  notes: Page says "Last Reviewed December 2023". Pack keeps the treatment and self-care sections.
- id: S2
  title: The clinical and cost-effectiveness of corticosteroid injection versus night splints for carpal
    tunnel syndrome (INSTINCTS trial) (Chesterton et al.)
  publisher: The Lancet, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6196880/
  source_type: journal_article
  audience: clinician
  publication_date: '2018-10-20'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: CC BY 4.0. Chesterton LS, et al. Lancet. 2018;392(10156):1423-1433. Randomised trial, 234 adults,
    primary care in England. Dose details removed from the pack.
- id: S3
  title: Update on Efficacy of Conservative Treatments for Carpal Tunnel Syndrome (Karjalanen et al.)
  publisher: Journal of Clinical Medicine, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8877380/
  source_type: journal_article
  audience: clinician
  publication_date: '2022-02-11'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: CC BY. Karjalanen T, Raatikainen S, Jaatinen K, Lusa V. J Clin Med. 2022;11(4):950. Accepted
    2022-02-09. Narrative review; pack keeps the orthoses section.
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
  notes: CC BY. Joshi A, et al. Cureus. 2022;14(7):e27053. Narrative review; pack keeps the 'Treatment
    options' section only. One figure is CC BY-NC (not used).
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
  - 'Clinician check: S3 (narrative review) says splint benefits are small and may be below what people
    notice, while S4 says the AAOS guideline strongly recommends wrist immobilization. The KO reports
    both; confirm the balance and consider adding the AAOS 2024 guideline (OrthoGuidelines) as a direct
    source.'
  - 'Clinician check: side-effect figures (about 18% with mild side effects in S3; 6% could not wear the
    splint in S2) come from research studies; confirm they are suitable to show patients.'
  - S2 compares splints with a steroid injection in UK primary care for mild or moderate CTS; results
    may not apply to every setting.
  - No public-domain patient page explains how to wear or care for a splint. AAOS OrthoInfo 'Care of Casts
    and Splints' (link_and_paraphrase) could add practical detail.
  - codes.mesh and codes.icd10cm are <verify>. ICD-10-CM codes diagnoses, not treatments; check an official
    code source before filling.
  - 'S1 publication_date is the month only (2023-12) because the page shows ''Last Reviewed: December
    2023''.'
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-01'
last_updated: '2026-11-01'
update_triggers:
- AAOS publishes or updates its carpal tunnel syndrome guideline (bracing recommendation).
- The NIAMS carpal tunnel treatment page shows a new "Last Reviewed" date.
- A large new trial or systematic review reports long-term results of splinting for carpal tunnel syndrome.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-01'
  by: OKDS agent (Claude)
  change: Initial draft written by OKDS agent (Claude) (claude-opus-5-5, okds-gen-1.0) from source pack
    SP-KO-HAND-TRT-001.
---

## Summary
Wrist splinting is a non-surgical treatment for carpal tunnel syndrome (CTS), a condition where the median nerve is squeezed at the wrist [S2]. A splint, also called a brace or orthosis, is worn on the hand and wrist to hold the wrist still [S1][S3]. Wearing a splint at night is a common first treatment for CTS symptoms [S1]. Splints are cheap and probably cause no long-term harm, but studies show their benefits are small and mostly short-term [S3].

## Key Facts (claim → source)
- Using a splint on the hand and wrist at night is a common first treatment for CTS [S1].
- For CTS, the splint usually holds the wrist in a neutral (straight) position or tilted slightly back [S2][S4].
- Splints can ease symptoms in the short term, but they do not fix the underlying problem with the median nerve [S1].
- Research has not shown whether splints work better when worn only at night or all day, or how many weeks to wear them [S3].
- In a large trial, a steroid shot improved symptoms faster than night splints at 6 weeks, but by 6 months the two groups were about the same [S2].
- A review reports that guidelines from the American Academy of Orthopaedic Surgeons (AAOS) strongly recommend keeping the wrist still (immobilizing it) for CTS [S4].

## Explanation
### What it is
A wrist splint is a support you wear on your hand and wrist [S1]. For CTS, it keeps the wrist in a neutral position, and sometimes tilted slightly back (extended) [S2][S4]. It is usually worn at night [S1][S4]. A doctor may also suggest wearing it during activities that make symptoms worse, such as typing on a keyboard [S4]. Some splint designs also hold the knuckle joints (called MP joints) straight [S3].

### How it helps
Pressure inside the carpal tunnel goes up when the wrist is bent forward (flexion) or bent back (extension) [S3]. Holding the wrist in a neutral position may lower the time spent at high pressure and ease symptoms [S3]. By keeping the wrist steady, the brace helps reduce the squeeze on the median nerve [S4]. Another idea is that keeping the knuckles straight moves small hand muscles away from the tunnel, which could also lower pressure [S3].

### Who it may suit
Splints are one of the main treatments for mild or moderate CTS [S2]. Because splints probably cause no long-term harm, they can be tried as a first treatment, especially by people who do not want surgery, shots, or supervised therapy [S3]. NIAMS lists a night splint as one way to manage early CTS symptoms, along with resting the hands, taking short breaks from repeated hand tasks, using ice packs, and using ergonomic tools and furniture [S1]. If CTS is caused by another health problem, such as diabetes or arthritis, that problem should be treated first [S1]. When CTS is severe or does not get better with non-surgical care, surgery is usually considered [S2].

### Risks and side effects
The side effects people report are not likely to last after they stop using the splint [S3]. In studies, about 18% of people using splints reported side effects, mostly trouble falling asleep and short-lived tingling (paresthesia) [S3]. In one large trial, 6% of people could not wear the splint as told because it was uncomfortable [S2]. Wearing a brace for a long time may weaken wrist muscles, because the joint is kept still [S4]. In that trial, people were taught gentle range-of-motion exercises (moving the wrist through its normal motions) when taking the splint off, to prevent stiffness [S2].

### Evidence summary
- A review of eight studies comparing splints with no treatment or fake (sham) treatment found little or no benefit in the short term [S3].
- The benefits found were small, may be less than what people notice in daily life, and there is little data beyond 6 months [S3].
- None of the studies measured relief of night-time symptoms, even though that is a main reason people wear splints [S3].
- In the INSTINCTS trial of 234 adults with mild or moderate CTS, people who got one steroid shot had better symptom and hand-function scores at 6 weeks than people who wore night splints [S2].
- By 6 months, the splint group kept improving and the scores of the two groups no longer differed [S2].
- A review notes that the AAOS guideline strongly recommends immobilizing the wrist to improve results [S4].

## Common Misunderstandings
- **Myth:** A splint cures carpal tunnel syndrome. **Fact:** A splint can ease symptoms in the short term, but it does not fix the underlying nerve problem [S1].
- **Myth:** A splint only works if you wear it all day. **Fact:** Research has not shown whether night-only or full-time wear is better [S3].
- **Myth:** A splint works as fast as a steroid shot. **Fact:** In one large trial, the shot improved symptoms faster at 6 weeks, although the groups were similar by 6 months [S2].
- **Myth:** Splints are risky. **Fact:** Splints probably cause no long-term harm, and reported side effects, such as trouble falling asleep or brief tingling, are not likely to last after stopping [S3].

## Questions to Ask Your Doctor
1. What kind of splint should I use, and how should it fit?
2. Should I wear it only at night, or also during the day?
3. How long should I try the splint before we decide if it is working?
4. Are there exercises I should do so my wrist does not get stiff or weak?
5. What are my next options if my symptoms do not improve?

## Test Questions
1. What is wrist splinting for carpal tunnel syndrome? - Wearing a brace on the hand and wrist, usually at night, to hold the wrist still and ease symptoms [S1][S4].
2. What position does a carpal tunnel splint usually hold the wrist in? - Neutral (straight) or tilted slightly back [S2][S4].
3. How might a splint help carpal tunnel syndrome? - Keeping the wrist neutral may lower pressure inside the carpal tunnel and on the median nerve [S3][S4].
4. Who may splinting suit? - People with mild or moderate CTS, especially those who do not want surgery or shots [S2][S3].
5. Name one possible side effect of wearing a splint. - Trouble falling asleep, brief tingling, discomfort, or wrist muscle weakness with long use [S2][S3][S4].
6. In the INSTINCTS trial, how did night splints compare with a steroid shot? - The shot worked better at 6 weeks, but by 6 months the groups were about the same [S2].

## Related Topics
- Treats: Carpal Tunnel Syndrome (KO-HAND-COND-001)
- Alternative to: Corticosteroid Injection (KO-HAND-TRT-002), Carpal Tunnel Release (KO-HAND-PROC-001)
- Proposed new topics: Wrist splint (device), Hand therapy (treatment)
- Background reading: Carpal Tunnel (KO-HAND-ANAT-002), Median Nerve (KO-HAND-ANAT-001)

## References
1. [S1] NIAMS (NIH). *Carpal Tunnel Syndrome: Diagnosis, Treatment, and Steps to Take.* https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome/diagnosis-treatment-and-steps-to-take (retrieved 2026-11-01)
2. [S2] The Lancet, via PubMed Central. *The clinical and cost-effectiveness of corticosteroid injection versus night splints for carpal tunnel syndrome (INSTINCTS trial) (Chesterton et al.).* https://pmc.ncbi.nlm.nih.gov/articles/PMC6196880/ (retrieved 2026-11-01)
3. [S3] Journal of Clinical Medicine, via PubMed Central. *Update on Efficacy of Conservative Treatments for Carpal Tunnel Syndrome (Karjalanen et al.).* https://pmc.ncbi.nlm.nih.gov/articles/PMC8877380/ (retrieved 2026-11-01)
4. [S4] Cureus, via PubMed Central. *Carpal Tunnel Syndrome: Pathophysiology and Comprehensive Guidelines for Clinical Evaluation and Treatment (Joshi et al.).* https://pmc.ncbi.nlm.nih.gov/articles/PMC9389835/ (retrieved 2026-11-01)
