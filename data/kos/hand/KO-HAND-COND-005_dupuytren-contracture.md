---
schema_version: okds-ko-1.0
ko_id: KO-HAND-COND-005
title: Dupuytren Contracture
preferred_term: Dupuytren Contracture
alternate_terms:
- Dupuytren's contracture
- Dupuytren disease
ko_type: Condition
specialty: HAND
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Dupuytren contracture is a slowly worsening, non-cancerous thickening of the tough tissue just
  under the skin of the palm, which forms knots and cords that pull fingers into a bent position [S1][S2][S4].
  It most often affects the ring and little fingers and is usually not painful [S2][S4]. No treatment cures
  it, but needle, injection, and surgical procedures can straighten the fingers, although it can come back
  [S4].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- bent fingers
- palm lump
- palmar fascia
- ring finger
- little finger
- family history
relationships:
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-COND-003
  target_label: Trigger Finger
  source_ids:
  - S1
proposed_concepts:
- term: Palmar fascia
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S2, S3, and S4 say Dupuytren disease forms knots and cords in the palmar fascia; it is not in the
    registry.
- term: Percutaneous needle fasciotomy
  suggested_type: Procedure
  predicate: PREREQUISITE_FOR
  reason: S4 and S5 describe this needle procedure as a minimally invasive treatment; no Procedure KO exists.
- term: Limited fasciectomy
  suggested_type: Procedure
  predicate: PREREQUISITE_FOR
  reason: S4 calls limited fasciectomy the durable reference operation; no Procedure KO exists.
- term: Collagenase injection for Dupuytren disease
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S4 lists collagenase injection as a minimally invasive option; no Treatment KO exists.
- term: Manual work and hand-arm vibration exposure
  suggested_type: Concept
  predicate: HAS_RISK_FACTOR
  reason: S3's meta-analysis links heavy manual work and vibration with Dupuytren contracture; needs a Concept
    KO before a HAS_RISK_FACTOR link can be made.
sources:
- id: S1
  title: Finger Injuries and Disorders
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/fingerinjuriesanddisorders.html
  source_type: government_health_page
  audience: patient
  publication_date: '2025-12-03'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:fingerinjuriesanddisorders). Licence: Public domain (NLM-authored
    MedlinePlus summary); credit MedlinePlus'
- id: S2
  title: 'The worldwide prevalence of the Dupuytren disease: a comprehensive systematic review and meta-analysis'
  publisher: Journal of Orthopaedic Surgery and Research
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7594412/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC7594412). Licence: CC BY'
- id: S3
  title: Should we consider Dupuytren's contracture as work-related? A review and meta-analysis of an
    old debate
  publisher: BMC Musculoskeletal Disorders
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3123614/
  source_type: journal_article
  audience: clinician
  publication_date: '2011'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC3123614). Licence: CC BY'
- id: S4
  title: Surgical Management of Dupuytren Disease
  publisher: International Journal of Medical Science and Clinical Research Studies
  url: https://zenodo.org/records/20623698
  source_type: journal_article
  audience: clinician
  publication_date: '2026'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via zenodo. Licence: cc-by-4.0. Type: article. Text kept: abstract only.'
- id: S5
  title: 'Percutaneous needle fasciotomy in Dupuytren contracture: a register-based, observational cohort
    study on complications in 3,331 treated fingers in 2,257 patients'
  publisher: Acta orthopaedica
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8023958/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via doaj, europepmc. Licence: cc by. Type: article. Text kept: abstract only.'
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
  - Only one relationship could be made; the registry has no KO for the palmar fascia or for Dupuytren treatments.
    See proposed_concepts.
  - 'None of the sources describe how Dupuytren contracture is diagnosed or give ''when to seek care'' advice;
    those sections say so and point to a clinician. Consider adding a patient page or review that covers
    diagnosis.'
  - The only patient-level source (S1) is a one-line MedlinePlus summary; no dedicated MedlinePlus or NIAMS
    Dupuytren page was found in the dataset.
  - 'S2 (prevalence meta-analysis) reports a pooled world prevalence of 8.2% with very wide variation between
    studies (0.2% to 56%); clinician should confirm the figure is suitable for patients.'
  - S4 is abstract-only from a smaller journal; S5 is a single-center registry study of one needle method.
  - MeSH ID and ICD-10-CM code are not stated in any source; left as verify.
  - Plain-language explanations of terms (e.g., 'fascia', 'nodule', 'cord') were written by the drafter;
    check they match the sources.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus publishes a new 'last updated' date for its Finger Injuries and Disorders page.
- A new guideline or systematic review compares needle fasciotomy, collagenase injection, and fasciectomy
  for Dupuytren contracture.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Dupuytren contracture is a slowly worsening, non-cancerous thickening of the tough tissue just under the skin of the palm, which forms knots and cords that pull fingers into a bent position [S1][S2][S4]. It most often affects the ring and little fingers and is usually not painful [S2][S4]. No treatment cures it, but needle, injection, and surgical procedures can straighten the fingers, although it can come back [S4].

## Key Facts (claim → source)
- Dupuytren disease is a benign (not cancer) disorder in which extra collagen forms knots and fibers in the palmar fascia, the tough layer under the skin of the palm [S2][S4].
- Over time, firm cords pull the fingers toward the palm, so they become stiff and bent [S1][S2].
- The ring finger and little finger are affected most often [S2][S3][S4].
- It runs in families, and family history and being male have a strong effect on risk [S1][S2].
- Diabetes, smoking, heavy alcohol use, hand injuries, and older age are also linked to it [S2][S3].
- One large review estimated that about 8 in 100 people worldwide have it [S2].
- Treatments include needle fasciotomy, collagenase injection, and surgery to remove the diseased tissue, but no treatment is a cure and it can come back [S4].

## Explanation
### What it is
Under the skin of the palm is a tough sheet of tissue called the palmar fascia [S2][S4]. In Dupuytren disease, extra collagen (a strong protein in connective tissue) builds up in this tissue and forms small knots, called nodules, and rope-like cords [S2][S4]. The cords can slowly pull one or more fingers into a bent position that cannot be straightened, called a contracture [S2][S4]. The disease usually starts in the palm and spreads into the fingers [S2]. It can bend the knuckle joints at the base of the finger and the middle joints of the finger [S2]. It is not dangerous and is not a cancer, but it tends to get worse over the years and does not go away on its own [S2].

### Causes and risk factors
The main cause is not known, and changes in the immune system may play a part [S2]. Genes and family history matter a lot: Dupuytren disease is described as the most common genetic disorder of connective tissue, and people with a family history tend to get it at a younger age [S1][S2]. Other factors linked to it include [S2][S3]:
- Being male [S2].
- Older age [S2].
- Diabetes, especially type 1 diabetes [S2][S3].
- Smoking and heavy alcohol use [S2][S3].
- Hand injuries [S2].
- Heavy manual work and use of vibrating tools at work [S3].

Higher rates have also been reported in people with high blood pressure, high blood fats, heart disease, lung disease (COPD), epilepsy, and rheumatoid arthritis [S2].

### Symptoms
- Lumps (nodules) or firm cords in the palm [S2][S4].
- Fingers that slowly curl toward the palm, most often the ring and little fingers [S2][S3].
- Thick skin on the palm [S3].
- Trouble with everyday tasks such as washing, picking things up, putting on gloves, or putting a hand in a pocket [S2].

Dupuytren disease is usually not painful [S2].

### How it is diagnosed
The sources here do not describe how Dupuytren contracture is diagnosed, so ask a clinician how it is checked. The sources do describe what a provider may look for: knots and cords in the palm and fingers that are bent toward the palm [S2][S4].

### Treatment options
No treatment cures Dupuytren disease, and the chance that it comes back is a key part of choosing a treatment [S4]. Options include [S4]:
- **Needle fasciotomy (also called needle aponeurotomy):** a minimally invasive procedure done with a needle through the skin, without an open cut [S4][S5]. A large registry study found that serious problems, such as tendon or nerve injury, were rare with the method studied [S5].
- **Collagenase injection:** a shot of a medicine called collagenase clostridium histolyticum, another minimally invasive option [S4].
- **Limited fasciectomy:** surgery to remove the diseased tissue; it is a long-lasting standard option for disease that limits hand use [S4].
- **Dermofasciectomy:** a bigger surgery that removes diseased tissue together with skin and uses a skin graft; it is mainly used for severe, fast-growing, or returning disease [S4].

The less invasive options (needle and injection) allow a quick recovery, but the contracture tends to come back sooner and more often than after surgery [S4]. The best choice depends on how bent the finger is, which joint is involved, past treatments, skin condition, other health problems, and the person's own priorities, so shared decision-making with a clinician is recommended [S4].

### When to seek care
The sources here do not list specific warning signs, so ask a clinician which changes need prompt attention. Because the disease slowly worsens and can make daily tasks hard, it is reasonable to talk with a health care provider when fingers start to curl or hand use becomes limited [S2][S4].

## Common Misunderstandings
- **Myth:** Dupuytren contracture is a type of cancer. **Fact:** It is a benign (non-cancerous) disorder of the tissue in the palm [S2][S4].
- **Myth:** Dupuytren contracture is always painful. **Fact:** It is usually not painful, but it can limit how the hand moves [S2].
- **Myth:** Once treated, it is cured for good. **Fact:** No treatment is curative, and the contracture can come back, especially after needle or injection treatments [S4].
- **Myth:** Work has nothing to do with it. **Fact:** A review found that heavy manual work and vibration exposure are linked to Dupuytren contracture in some cases, along with genes and other factors [S3].

## Questions to Ask Your Doctor
1. Are the lumps or cords in my palm from Dupuytren disease?
2. How will we track whether my fingers are bending more over time?
3. At what point would a treatment make sense for me?
4. What are the pros and cons of needle treatment, an injection, and surgery for my hand?
5. What is the chance that the contracture comes back after each treatment?

## Test Questions
1. What tissue is affected in Dupuytren disease? - The palmar fascia, the tough layer under the skin of the palm [S2][S4].
2. Which fingers are affected most often? - The ring and little fingers [S2][S4].
3. Name two risk factors. - Examples: family history, being male, diabetes, smoking, heavy alcohol use, hand injury, or heavy manual work [S2][S3].
4. Is Dupuytren disease usually painful? - No, it is usually not painful, though it can limit hand use [S2].
5. What is a downside of the less invasive treatments? - The contracture tends to come back sooner and more often [S4].

## Related Topics
- Often confused with: Trigger Finger (KO-HAND-COND-003)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Finger Injuries and Disorders.* https://medlineplus.gov/fingerinjuriesanddisorders.html (retrieved 2026-10-26)
2. [S2] Journal of Orthopaedic Surgery and Research. *The worldwide prevalence of the Dupuytren disease: a comprehensive systematic review and meta-analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC7594412/ (retrieved 2026-10-26)
3. [S3] BMC Musculoskeletal Disorders. *Should we consider Dupuytren's contracture as work-related? A review and meta-analysis of an old debate.* https://pmc.ncbi.nlm.nih.gov/articles/PMC3123614/ (retrieved 2026-10-26)
4. [S4] International Journal of Medical Science and Clinical Research Studies. *Surgical Management of Dupuytren Disease.* https://zenodo.org/records/20623698 (retrieved 2026-11-14)
5. [S5] Acta orthopaedica. *Percutaneous needle fasciotomy in Dupuytren contracture: a register-based, observational cohort study on complications in 3,331 treated fingers in 2,257 patients.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8023958/ (retrieved 2026-11-14)
