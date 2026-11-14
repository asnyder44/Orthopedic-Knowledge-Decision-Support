---
schema_version: okds-ko-1.0
ko_id: KO-HAND-TRT-002
title: Corticosteroid Injection
preferred_term: Corticosteroid Injection
alternate_terms:
- steroid shot
- steroid injection
- local steroid injection
- local corticosteroid injection
- glucocorticoid injection
ko_type: Treatment
specialty: HAND
cluster: 4
audience:
- patient
- caregiver
- student
reading_level: grade 6-8
difficulty: beginner
summary: A corticosteroid injection (steroid shot) puts a strong anti-inflammatory medicine into one spot
  in the hand or wrist, such as the carpal tunnel [S1][S2]. For carpal tunnel syndrome it can ease symptoms
  for a while, up to about six months in studies, but for many people the benefit fades and they later
  have surgery [S1][S2][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- carpal tunnel syndrome treatment
- non-surgical treatment
- steroid shot
- hand injection
- trigger finger
- de Quervain tenosynovitis
- side effects
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
  target_id: KO-HAND-TRT-001
  target_label: Wrist Splinting
  source_ids:
  - S1
  - S4
- predicate: ALTERNATIVE_TO
  target_id: KO-HAND-PROC-001
  target_label: Carpal Tunnel Release
  source_ids:
  - S1
  - S2
  - S3
- predicate: TREATS
  target_id: KO-HAND-COND-003
  target_label: Trigger Finger
  source_ids:
  - S2
- predicate: TREATS
  target_id: KO-HAND-COND-004
  target_label: De Quervain Tenosynovitis
  source_ids:
  - S2
proposed_concepts:
- term: Ultrasound-guided injection
  suggested_type: Concept
  predicate: PREREQUISITE_FOR
  reason: S2 says ultrasound guidance can improve accuracy and safety for some hand injections; a separate
    KO could explain it.
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
  notes: Page says "Last Reviewed December 2023". Short on this topic (one sentence on steroid injection).
- id: S2
  title: 'Local Corticosteroid Injection in Hand Surgery: A Review of Molecular Mechanisms, Steroid Selection,
    and Clinical Outcomes (Patel, Alkadaa, Franco)'
  publisher: Cureus, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13717673/
  source_type: journal_article
  audience: clinician
  publication_date: '2026-09-29'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: CC BY 4.0. Patel AU, Alkadaa L, Franco MJ. Cureus. 2026;18(9):e117128. Accepted 2026-09-28. Narrative
    review; molecular detail, drug comparisons and dosing removed from the pack.
- id: S3
  title: 'Extended Follow-up of Local Steroid Injection for Carpal Tunnel Syndrome: A Randomized Clinical
    Trial (Hofer, Ranstam, Atroshi)'
  publisher: JAMA Network Open, via PubMed Central
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8536954/
  source_type: journal_article
  audience: clinician
  publication_date: '2021-10-22'
  retrieved_date: '2026-11-01'
  permitted_use: open_license
  notes: CC BY. Hofer M, Ranstam J, Atroshi I. JAMA Netw Open. 2021;4(10):e2130753. 5-year follow-up of
    a placebo-controlled RCT (111 adults, Sweden). Dose amounts replaced with 'higher-dose'/'lower-dose'
    in the pack.
- id: S4
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
  - 'Clinician check: most content comes from research papers written for clinicians (S2 narrative review,
    S3 and S4 trials). There is no public-domain patient page about steroid shots in the hand; S1 has
    only one sentence. Check every risk and benefit statement before patient use.'
  - 'Clinician check: the ''2023 Cochrane review'' findings (improves symptoms up to about six months;
    may lower surgery at one year) are as summarized by S2, not taken from the Cochrane review itself.'
  - 'Clinician check: the pregnancy sentence (S2) is a sensitive claim; confirm or remove before publishing.'
  - 'Clinician check: side-effect rates (46% more pain after the shot, 15% hot flushes, 3% skin changes)
    are from one trial (S4) in UK primary care; confirm they are suitable to show patients.'
  - 'Dosing and drug-choice details were removed on purpose (OKDS rule: no doses). S3 compared two dose
    levels; the KO does not report dose-specific results.'
  - codes.mesh and codes.icd10cm are <verify>. ICD-10-CM codes diagnoses, not treatments; check an official
    code source before filling.
  - 'S1 publication_date is the month only (2023-12) because the page shows ''Last Reviewed: December
    2023''.'
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.1
created: '2026-11-01'
last_updated: '2026-11-14'
update_triggers:
- A new Cochrane or other systematic review on steroid injection for carpal tunnel syndrome is published.
- AAOS publishes or updates its carpal tunnel syndrome guideline (injection recommendation).
- The NIAMS carpal tunnel treatment page shows a new "Last Reviewed" date.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-01'
  by: OKDS agent (Claude)
  change: Initial draft written by OKDS agent (Claude) (claude-opus-5-5, okds-gen-1.0) from source pack
    SP-KO-HAND-TRT-002.
- version: 0.1.1
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: 'Proposed concepts that now have KOs became relationships (same sources): treats → Trigger Finger
    (KO-HAND-COND-003); treats → De Quervain Tenosynovitis (KO-HAND-COND-004)'
---

## Summary
A corticosteroid injection, often called a steroid shot, puts a steroid medicine directly into one spot, such as the carpal tunnel at the wrist [S1][S2]. Corticosteroids (also called glucocorticoids) are medicines that calm inflammation, the body's swelling and irritation response [S2]. For carpal tunnel syndrome (CTS), a shot can ease symptoms for a while [S1]. Many people still need surgery later, so the shot often buys time rather than fixing the problem [S2][S3].

## Key Facts (claim → source)
- A steroid shot into the carpal tunnel can ease CTS symptoms for a while [S1].
- The shot is best suited to mild or moderate CTS; it does not undo severe nerve damage [S2].
- A review reports that steroid shots probably improve CTS symptoms and hand function for up to about six months [S2].
- In a large trial, one steroid shot improved symptoms faster than night splints at 6 weeks [S4].
- In a 5-year study, about 90% of people had CTS surgery within 5 years; the shot delayed surgery by about 2 months and slightly lowered the number of surgeries [S3].
- Possible side effects include more pain after the shot, hot flushes, skin color changes, short-term high blood sugar, and rarely tendon damage or infection [S2][S4].

## Explanation
### What it is
A corticosteroid injection is a shot of steroid medicine given into a specific place, such as the carpal tunnel [S1][S2]. It is one of the most common procedures in hand surgery and is used for several hand and wrist problems [S2]. Examples are CTS, trigger finger (a finger that catches or locks when it bends), de Quervain tenosynovitis (swelling around tendons that move the thumb), and arthritis at the base of the thumb [S2]. The evidence is strongest for trigger finger, de Quervain tenosynovitis, and mild to moderate CTS [S2].

### How it helps
In CTS, the shot reduces swelling in and around the median nerve, shrinks thickened tissue inside the tunnel, and lowers the pressure in the tunnel [S2]. Inside cells, steroids switch on genes that calm inflammation and block signals that drive it [S2]. Some people feel better within hours, which suggests the medicine also works in faster ways that do not depend on genes [S2]. However, the shot does not reverse nerve damage that is already severe [S2]. Like other non-surgical treatments, it can help symptoms in the short term but does not treat the underlying nerve problem [S1].

### Who it may suit
- People with mild to moderate CTS are the best fit [S2][S4].
- A shot may be used to help confirm the diagnosis, to manage symptoms while waiting for surgery, or as the main treatment for someone who is not a good candidate for surgery [S2].
- People with advanced CTS should usually be offered a surgery evaluation instead of repeated shots [S2]. Signs of advanced CTS include symptoms that never go away, shrinking muscles at the base of the thumb, loss of feeling, or very abnormal nerve test results [S2].
- In pregnancy, a shot is generally seen as a reasonable option for CTS when splints and changing activities have not helped [S2].

### Risks and side effects
- **Pain:** In one trial, almost half (46%) of people said their hand or wrist hurt more after the shot [S4]. About a third of those had pain lasting more than 3 days before it eased [S4].
- **Hot flushes:** About 15% of people in that trial had hot flushes [S4].
- **Skin changes:** Some people get thinning, lightening, or darkening of the skin where the shot was given [S4]. Lighter skin (hypopigmentation) and loss of fat under the skin (fat atrophy) happen when the medicine is placed too close to the surface [S2]. These changes may show more on darker skin and can last a long time or be permanent [S2].
- **Blood sugar:** The shot can raise blood sugar for a short time [S2]. This matters most for people with diabetes, especially if it is not well controlled, and diabetes can also change how well a shot works [S2].
- **Tendons:** Tendon rupture (a tendon tearing) is uncommon, but repeated shots near tendons may raise the risk over time [S2].
- **Infection:** Infection is rare but can be serious in the hand [S2]. Shots should not be given through infected, broken, or inflamed skin [S2].

### Evidence summary
- Steroid shots work better than a placebo (fake) shot in the short term, but proof of long-term benefit has been limited [S3][S4].
- A 2023 Cochrane review, as summarized by one hand surgery review, found that shots probably improve symptoms and function for up to six months and may reduce the need for surgery at one year [S2].
- The INSTINCTS trial included 234 adults with mild or moderate CTS [S4]. At 6 weeks, one steroid shot gave better symptom and function scores than night splints, and by 6 months the groups no longer differed [S4]. No serious or unexpected side effects were reported [S4].
- Another trial followed 111 adults for 5 years after one shot or a placebo shot [S3]. By 5 years, symptom scores were similar in all groups, and about 90% of people had had surgery [S3]. The steroid shot delayed surgery by about 2 months and slightly lowered the surgery rate [S3].
- In that trial, people who had surgery after a steroid shot improved just as much as people who had surgery after a placebo shot [S3]. It is not known whether repeated shots affect later surgery results [S3].

## Common Misunderstandings
- **Myth:** A steroid shot cures carpal tunnel syndrome for good. **Fact:** The relief is usually temporary, and in a 5-year study most people later had surgery [S1][S3].
- **Myth:** You will feel better right away with no pain. **Fact:** Some people feel better within hours, but in one trial almost half had more hand or wrist pain after the shot [S2][S4].
- **Myth:** Having a shot first makes later surgery work worse. **Fact:** In one trial, people who had surgery after a single steroid shot did as well as those who had a placebo shot first [S3].
- **Myth:** Steroid shots help every hand problem equally. **Fact:** Evidence is strong for some problems, like mild to moderate CTS, while the evidence does not support using them for others, like ganglion cysts (a type of cyst near a joint) [S2].

## Questions to Ask Your Doctor
1. Is my CTS mild or moderate enough for a steroid shot to help?
2. How long might the relief last for someone like me?
3. What side effects should I watch for, and when should I call you?
4. I have diabetes. What should I do about my blood sugar after a shot?
5. How many shots are safe for me, and what happens if the first one does not help?

## Test Questions
1. What is a corticosteroid injection? - A shot of steroid medicine that calms inflammation, given into one spot such as the carpal tunnel [S1][S2].
2. How does a steroid shot help carpal tunnel syndrome? - It reduces swelling around the median nerve and lowers pressure inside the carpal tunnel [S2].
3. Which people with carpal tunnel syndrome are the best fit for a steroid shot? - People with mild to moderate CTS [S2].
4. Name two side effects of a steroid shot reported in the INSTINCTS trial. - More hand or wrist pain after the shot, hot flushes, or skin thinning or color change [S4].
5. Why should people with diabetes talk to their doctor before a steroid shot? - The shot can raise blood sugar for a short time [S2].
6. What happened in the long term in the 5-year steroid injection trial? - About 90% had surgery within 5 years; the shot delayed surgery by about 2 months [S3].

## Related Topics
- Treats: Carpal Tunnel Syndrome (KO-HAND-COND-001)
- Alternative to: Wrist Splinting (KO-HAND-TRT-001), Carpal Tunnel Release (KO-HAND-PROC-001)
- Proposed new topics: Trigger Finger (condition), De Quervain Tenosynovitis (condition), Ultrasound-guided injection (concept)
- Background reading: Carpal Tunnel (KO-HAND-ANAT-002), Median Nerve (KO-HAND-ANAT-001)
- treats → Trigger Finger (KO-HAND-COND-003)
- treats → De Quervain Tenosynovitis (KO-HAND-COND-004)

## References
1. [S1] NIAMS (NIH). *Carpal Tunnel Syndrome: Diagnosis, Treatment, and Steps to Take.* https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome/diagnosis-treatment-and-steps-to-take (retrieved 2026-11-01)
2. [S2] Cureus, via PubMed Central. *Local Corticosteroid Injection in Hand Surgery: A Review of Molecular Mechanisms, Steroid Selection, and Clinical Outcomes (Patel, Alkadaa, Franco).* https://pmc.ncbi.nlm.nih.gov/articles/PMC13717673/ (retrieved 2026-11-01)
3. [S3] JAMA Network Open, via PubMed Central. *Extended Follow-up of Local Steroid Injection for Carpal Tunnel Syndrome: A Randomized Clinical Trial (Hofer, Ranstam, Atroshi).* https://pmc.ncbi.nlm.nih.gov/articles/PMC8536954/ (retrieved 2026-11-01)
4. [S4] The Lancet, via PubMed Central. *The clinical and cost-effectiveness of corticosteroid injection versus night splints for carpal tunnel syndrome (INSTINCTS trial) (Chesterton et al.).* https://pmc.ncbi.nlm.nih.gov/articles/PMC6196880/ (retrieved 2026-11-01)
