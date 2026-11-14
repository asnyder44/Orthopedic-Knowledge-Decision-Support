---
schema_version: okds-ko-1.0
ko_id: KO-HAND-OUT-001
title: Boston Carpal Tunnel Questionnaire
preferred_term: Boston Carpal Tunnel Questionnaire
alternate_terms:
- BCTQ
- Levine questionnaire
- Levine scale
- Brigham and Women's Carpal Tunnel Questionnaire
- Carpal Tunnel Syndrome Instrument
- CTQ
ko_type: OutcomeMeasure
specialty: HAND
cluster: 6
audience:
- clinician
- researcher
- student
reading_level: college
difficulty: intermediate
summary: The Boston Carpal Tunnel Questionnaire (BCTQ) is a disease-specific, patient-reported outcome
  measure of symptom severity and functional status in carpal tunnel syndrome [S1]. It has two scales,
  the 11-item Symptom Severity Scale and the 8-item Functional Status Scale, each scored from 1 to 5 with
  higher scores meaning greater disability [S1]. It is widely used as an outcome in carpal tunnel trials,
  including comparisons of surgical techniques [S1][S4].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- patient-reported outcome measure
- PROM
- questionnaire
- carpal tunnel
- symptom severity
- functional status
- psychometrics
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-REHAB-001
  target_label: Recovery After Carpal Tunnel Release
  source_ids:
  - S2
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-PROC-001
  target_label: Carpal Tunnel Release
  source_ids:
  - S3
  - S4
proposed_concepts:
- term: Six-Item Carpal Tunnel Symptoms Scale (CTS-6)
  suggested_type: OutcomeMeasure
  predicate: CONTRASTS_WITH
  reason: Shorter symptom scale often used alongside or instead of the BCTQ; showed better Rasch properties
    than the BCTQ Symptom Severity Scale after surgery [S2].
- term: Michigan Hand Outcomes Questionnaire (MHQ)
  suggested_type: OutcomeMeasure
  predicate: CONTRASTS_WITH
  reason: Hand outcome questionnaire compared with the BCTQ after carpal tunnel release [S3].
- term: PROMIS Upper Extremity and Pain Interference
  suggested_type: OutcomeMeasure
  predicate: CONTRASTS_WITH
  reason: Newer measures compared with the BCTQ for responsiveness after carpal tunnel release [S3].
sources:
- id: S1
  title: A systematic review of the psychometric properties of the Boston Carpal Tunnel Questionnaire
  publisher: BMC Musculoskeletal Disorders
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC1624826/
  source_type: journal_article
  audience: clinician
  publication_date: '2006'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC1624826). Licence: CC BY'
- id: S2
  title: 'Structural validity of the Boston Carpal Tunnel Questionnaire and its short version, the 6-Item
    CTS symptoms scale: a Rasch analysis one year after surgery'
  publisher: BMC musculoskeletal disorders
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7488577/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via doaj, europepmc. Licence: cc by. Type: article. Text kept: abstract only.'
- id: S3
  title: Comparison of the Michigan Hand Outcomes Questionnaire, Boston Carpal Tunnel Questionnaire, and
    PROMIS Instruments in Carpal Tunnel Syndrome
  publisher: Elsevier BV
  url: https://doi.org/10.1016/j.jhsa.2018.10.031
  source_type: journal_article
  audience: clinician
  publication_date: '2017'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via openaire. Licence: Open Access. Type: article. Text kept: abstract only.'
- id: S4
  title: 'Open versus endoscopic carpal tunnel release: a systematic review and meta-analysis of randomized
    controlled trials'
  publisher: BMC musculoskeletal disorders
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7187537/
  source_type: systematic_review
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: systematic review. Text kept: abstract only.'
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
  - S1 (2006) is the main source for scoring and psychometrics; its pack text stops after the face/content
    validity results, so detailed construct validity, reliability, and responsiveness numbers are not
    in the pack. Consider adding a more recent review.
  - S3 publication_date shows '2017', but the DOI (10.1016/j.jhsa.2018.10.031) suggests a 2018-2019 publication;
    verify the date. S3 is link_and_paraphrase (abstract only).
  - No minimal clinically important difference (MCID) values for the BCTQ are in the pack; the questionnaire
    item wording and response labels are also not in the pack.
  - No other OutcomeMeasure KO exists in the registry, so no CONTRASTS_WITH link could be made; CTS-6,
    MHQ, and PROMIS are listed as proposed concepts.
  - MEASURED_BY links should be added from the Carpal Tunnel Syndrome (KO-HAND-COND-001) and Carpal Tunnel
    Release (KO-HAND-PROC-001) KOs.
  - MeSH ID is unknown ('<verify>'); ICD-10-CM does not apply to an outcome measure.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- A new systematic review of BCTQ measurement properties (e.g., a COSMIN-based review) is published.
- Carpal tunnel guidelines or core outcome sets change which patient-reported measures they recommend.
- Any cited page shows a new 'last reviewed' date.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
The Boston Carpal Tunnel Questionnaire (BCTQ) is a standardised, patient-based outcome measure developed specifically for carpal tunnel syndrome (CTS) [S1]. It captures self-reported symptom severity and functional status through two separate scales [S1]. A 2006 systematic review judged it valid, reliable, responsive, and acceptable, and recommended it as a primary outcome in CTS trials [S1]. It is commonly used to compare treatments, such as open and endoscopic carpal tunnel release [S4].

## Key Facts (claim → source)
- The BCTQ is also known as the Levine scale, the Brigham and Women's Carpal Tunnel Questionnaire, and the Carpal Tunnel Syndrome Instrument [S1].
- The Symptom Severity Scale (SSS) has 11 questions rated on a five-point scale [S1].
- The Functional Status Scale (FSS) has 8 activities rated for degree of difficulty on a five-point scale [S1].
- Each scale score is the sum of item scores divided by the number of items, giving a range of 1 to 5; higher scores mean greater disability [S1].
- The 2006 review found evidence from 10 studies on validity, reliability, responsiveness, interpretability, and acceptability [S1].
- A Rasch analysis one year after surgery supported the FSS but found disordered response categories in some SSS items [S2].
- After carpal tunnel release, the FSS was more responsive than the MHQ and PROMIS Upper Extremity measure [S3].

## Explanation
### What it measures
The BCTQ measures two things that patients see as the main reasons for seeking treatment: how severe their symptoms are and how well they can carry out daily activities [S1]. It is disease-specific, unlike region-specific upper-limb measures such as the DASH or generic quality-of-life measures such as the SF-36 [S1]. The FSS covers activities done by a broad range of patients, but it does not include items aimed at specific groups such as workers [S1].

### How it is scored
- The SSS contains 11 items, each answered on a five-point rating scale [S1].
- The FSS contains 8 items, each rated for difficulty on a five-point scale [S1].
- Each scale gives its own final score: the sum of the item scores divided by the number of items, from 1 to 5 [S1].
- Higher scores indicate greater disability, so improvement shows as a falling score [S1][S3].
- Example of change over time: in one cohort, the FSS mean rose from 2.3 before surgery to 2.6 at one week and then fell to 1.6 by three months, while the SSS fell from 3.1 to 2.3 as early as one week [S3].
- Rasch analysis suggests some SSS response categories may need merging to work in order, and some items behave differently by age or gender [S2].

### Where it is used
- Trials and systematic reviews of surgical and non-surgical CTS treatments use the BCTQ as an outcome [S1].
- A meta-analysis of randomized trials comparing endoscopic and open carpal tunnel release pooled BCTQ scores along with grip strength, return to work, and complications [S4].
- It is used to follow recovery after carpal tunnel release, alongside newer tools such as PROMIS and the shorter CTS-6 [S2][S3].
- PROMIS measures took less time to complete than the BCTQ, but the BCTQ FSS showed the largest effect sizes after surgery [S3].

## Common Misunderstandings
- **Myth:** The BCTQ gives one total score. **Fact:** It has two separate scales, symptom severity and functional status, each scored from 1 to 5 [S1].
- **Myth:** A higher BCTQ score means a better result. **Fact:** Higher scores mean greater disability [S1].
- **Myth:** The BCTQ is a diagnostic test for carpal tunnel syndrome. **Fact:** It is an outcome measure of symptoms and function in people with CTS; the 2006 review excluded studies that used it to detect CTS [S1].
- **Myth:** Every part of the BCTQ performs equally well. **Fact:** After surgery, the FSS showed good fit, while some SSS items had disordered response categories and the CTS-6 performed better for symptoms [S2].

## Test Questions
1. How many items are in the Symptom Severity Scale and the Functional Status Scale? - 11 and 8 [S1].
2. What is the score range of each BCTQ scale, and what does a higher score mean? - 1 to 5; greater disability [S1].
3. How is each scale score calculated? - The sum of item scores divided by the number of items [S1].
4. Which BCTQ scale was most responsive after carpal tunnel release when compared with the MHQ and PROMIS UE? - The Functional Status Scale [S3].
5. Which short scale outperformed the BCTQ SSS in a Rasch analysis after surgery? - The six-item CTS symptoms scale (CTS-6) [S2].
6. Name one surgical comparison in which BCTQ scores were pooled. - Endoscopic versus open carpal tunnel release [S4].

## Related Topics
- Read next: Recovery After Carpal Tunnel Release (KO-HAND-REHAB-001)
- Read next: Carpal Tunnel Release (KO-HAND-PROC-001)
- Measures outcomes for (link to be added from those KOs): Carpal Tunnel Syndrome (KO-HAND-COND-001); Carpal Tunnel Release (KO-HAND-PROC-001)
- Proposed topics (not in the registry yet): Six-Item Carpal Tunnel Symptoms Scale (CTS-6); Michigan Hand Outcomes Questionnaire (MHQ); PROMIS Upper Extremity and Pain Interference

## References
1. [S1] BMC Musculoskeletal Disorders. *A systematic review of the psychometric properties of the Boston Carpal Tunnel Questionnaire.* https://pmc.ncbi.nlm.nih.gov/articles/PMC1624826/ (retrieved 2026-10-26)
2. [S2] BMC musculoskeletal disorders. *Structural validity of the Boston Carpal Tunnel Questionnaire and its short version, the 6-Item CTS symptoms scale: a Rasch analysis one year after surgery.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7488577/ (retrieved 2026-11-14)
3. [S3] Elsevier BV. *Comparison of the Michigan Hand Outcomes Questionnaire, Boston Carpal Tunnel Questionnaire, and PROMIS Instruments in Carpal Tunnel Syndrome.* https://doi.org/10.1016/j.jhsa.2018.10.031 (retrieved 2026-11-14)
4. [S4] BMC musculoskeletal disorders. *Open versus endoscopic carpal tunnel release: a systematic review and meta-analysis of randomized controlled trials.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7187537/ (retrieved 2026-11-14)
