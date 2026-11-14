---
schema_version: okds-ko-1.0
ko_id: KO-FOOT-COND-002
title: Plantar Fasciitis
preferred_term: Plantar Fasciitis
alternate_terms:
- plantar heel pain
- chronic plantar heel pain
- plantar fasciosis
- plantar fasciopathy
ko_type: Condition
specialty: FOOT
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Plantar fasciitis is a common cause of pain under the heel, where the plantar fascia, a thick
  band of tissue that supports the arch of the foot, attaches to the heel bone [S2][S4]. The pain is
  often worst with the first steps after rest, such as in the morning [S2][S3]. Most people get better
  with non-surgical care and time, and only a small number need surgery [S1][S2].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- heel pain
- plantar fascia
- arch of the foot
- morning heel pain
- heel spur
- running injury
relationships:
- predicate: CONTRASTS_WITH
  target_id: KO-FOOT-COND-004
  target_label: Achilles Tendinopathy
  source_ids:
  - S1
  - S3
proposed_concepts:
- term: Plantar fascia
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S2 describes the plantar fascia and its heel attachment as the site of the condition; no foot
    anatomy KO is in the registry.
- term: Calcaneus (heel bone)
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S1, S2 and S4 place the pain where the plantar fascia meets the heel bone.
- term: Foot ultrasound (plantar fascia thickness)
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S4 found a plantar fascia thicker than 4.0 mm on ultrasound is diagnostic of plantar fasciitis.
- term: Foot X-ray
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S2 says plain X-ray is the most commonly requested test; S4 links heel spurs to heel pain.
- term: Extracorporeal shockwave therapy
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S2 and S3 discuss shockwave therapy as a treatment; S3 reports consensus that it is effective.
- term: Plantar fascia release
  suggested_type: Procedure
  predicate: PREREQUISITE_FOR
  reason: S2 says surgical release works for the small share of patients who do not improve with conservative
    care.
- term: Obesity / high body mass index
  suggested_type: Concept
  predicate: HAS_RISK_FACTOR
  reason: S2 and S3 name obesity / higher BMI as a risk factor; needs a Concept KO.
sources:
- id: S1
  title: Heel Injuries and Disorders
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/heelinjuriesanddisorders.html
  source_type: government_health_page
  audience: patient
  publication_date: '2026-08-01'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:heelinjuriesanddisorders). Licence: Public domain (NLM-authored
    MedlinePlus summary); credit MedlinePlus'
- id: S2
  title: Plantar fasciitis
  publisher: Annals of The Royal College of Surgeons of England
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3954277/
  source_type: journal_article
  audience: clinician
  publication_date: '2012'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC3954277). Licence: CC BY'
- id: S3
  title: A Systematic Review of Systematic Reviews on the Epidemiology, Evaluation, and Treatment of Plantar
    Fasciitis
  publisher: Life
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8705263/
  source_type: journal_article
  audience: clinician
  publication_date: '2021'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC8705263). Licence: CC BY'
- id: S4
  title: 'Diagnostic imaging for chronic plantar heel pain: a systematic review and meta-analysis'
  publisher: Journal of Foot and Ankle Research
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2784446/
  source_type: journal_article
  audience: clinician
  publication_date: '2009'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC2784446). Licence: CC BY'
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
  - 'CONTRASTS_WITH Achilles Tendinopathy is weakly supported: S1 lists tendinitis and fasciitis as different
    heel problems and S3 compares the naming of the two; no source directly compares the two conditions.
    Confirm or remove.'
  - 'Treatment options: the pack has no full-text treatment section (S3 text stops at Methods). Stretching,
    night splints, orthoses and injections are not described in detail, so the KO only lists what S1-S3
    state. Consider adding a patient page or guideline on plantar fasciitis treatment.'
  - 'When to seek care: no source lists warning signs for heel pain; the section uses S2''s differential-diagnosis
    red flags (weight loss, night pain, fever). Clinician check needed.'
  - S2 (2012) mentions steroid injections and anti-inflammatory drugs; the KO names no medicines or doses
    on purpose.
  - MeSH and ICD-10-CM codes are unknown and set to verify.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- Any cited page shows a new 'last reviewed' date.
- A new clinical practice guideline on plantar heel pain / plantar fasciitis is published.
- Foot anatomy, imaging or treatment KOs are added to the registry (add links).
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Plantar fasciitis is a common cause of pain under the heel, where the plantar fascia, a thick band of tissue that supports the arch of the foot, attaches to the heel bone [S2][S4]. The pain is often worst with the first steps after rest, such as in the morning [S2][S3]. Most people get better with non-surgical care and time, and only a small number need surgery [S1][S2].

## Key Facts (claim → source)
- About 80% of people with heel pain have plantar fasciitis, and it leads to over 1 million doctor visits a year in the United States [S2][S3].
- The plantar fascia is a broad band of tissue that runs from the heel bone toward the toes and helps hold up the arch [S2].
- Pain is usually on the inner part of the bottom of the heel and is worst with the first steps after rest [S2][S3].
- Being overweight, a stiff ankle, and a tight Achilles tendon are linked to the condition [S2][S3].
- Despite the name, which suggests swelling (inflammation), many experts now see it as wear-and-tear damage to the tissue [S2][S3].
- Diagnosis is mainly based on symptoms and an exam, and imaging is added only when needed [S2][S4].
- Most cases get better with non-surgical care and time; about 1% of patients need surgery [S2].

## Explanation
### What it is
The plantar fascia is a broad, strong band of connective tissue on the sole of the foot [S2]. It starts at the heel bone (calcaneus) and splits into five bands that reach the toes [S2]. It supports the arch and helps the foot act like a stiff lever when you push off to walk [S2]. In plantar fasciitis, the area where this band attaches to the heel becomes painful [S2][S4]. Plantar fasciitis is the most common cause of long-lasting pain under the heel, and the two terms are often used to mean the same thing [S4].

Experts do not fully understand what happens in the tissue [S2]. One idea is that many small injuries build up where the fascia meets the heel [S2]. Studies of tissue removed in surgery did not find signs of inflammation, so some experts call it "fasciosis" or "fasciopathy," meaning a wear-and-tear problem rather than swelling [S2][S3].

### Causes and risk factors
Heel problems often come from too much stress on the heel bone and the tissues around it [S1]. That stress can come from [S1]:
- Injuries or bruises from walking, running, or jumping [S1].
- Shoes that do not fit well or are poorly made [S1].
- Being overweight [S1].

Obesity and an ankle that does not bend up well are known risk factors [S2]. Reviews agree that a higher body mass index (BMI, a measure of weight for height) is a risk factor [S3]. The condition is also linked to a tight Achilles tendon and to feet with very high or very flat arches [S2]. It is common in runners, affecting up to about 17% of them [S3]. People with gout or some types of inflammatory arthritis may get it more often [S2].

### Symptoms
- Pain on the inner part of the bottom of the heel [S2][S3].
- Pain that is worst with the first steps after rest, often in the morning, and then eases a bit with walking [S2][S3].
- Pain that gets worse with long walks or exercise, especially on hard ground [S2].
- Pain that may last for weeks or months, and often more than a year [S2][S3].

### How it is diagnosed
Plantar fasciitis is first of all diagnosed from the person's story and an exam [S2]. Other tests depend on what the clinician finds [S2]:
- **X-ray:** the most common test, mainly to look at the bone [S2]. About half of people with plantar fasciitis have a heel spur, a small bony growth, but spurs also show up in people without heel pain [S2]. One review found spurs are strongly linked to pain under the heel [S4].
- **Ultrasound:** it can measure the thickness of the plantar fascia, and a thickness over 4.0 mm points to plantar fasciitis [S4].
- **Other tests:** MRI, bone scans, nerve tests, or blood tests may be used to look for other causes, such as a hidden break, a pinched nerve, arthritis, or infection [S2].

### Treatment options
Most cases get better with non-surgical care and the passage of time [S2]. Because the natural course is not well understood, it is hard to tell who gets better on their own and who is helped by a treatment [S2].
- **Self-care and simple measures:** treatments for heel problems may include rest, medicines, exercises, taping, and special shoes [S1]. Many people have already tried over-the-counter shoe or heel inserts before they see a doctor [S2].
- **Injections:** some patients seem to respond to steroid shots into the heel, but in older people, repeated shots may speed up thinning of the fat pad under the heel [S2].
- **Shockwave therapy:** reviews generally agree that extracorporeal shockwave therapy, which sends sound-wave pulses into the heel, is an effective treatment [S3].
- **Surgery:** surgery is rarely needed [S1]. Cutting part of the plantar fascia (surgical release) works for the small number of people who do not improve with other care [S2].

### When to seek care
The sources here do not give a list of warning signs, so ask a health care provider about heel pain that does not improve [S1][S2]. Heel pain can also come from other problems, such as arthritis, a hidden bone break, a pinched nerve, or infection [S2]. Weight loss, pain at night, or fever along with heel pain can point to infection or, rarely, a tumor, and these need a clinician's attention [S2].

## Common Misunderstandings
- **Myth:** Plantar fasciitis is caused by a heel spur. **Fact:** Many people without heel pain also have heel spurs, and many experts think the spur is often an incidental finding [S2].
- **Myth:** The "-itis" means the tissue is always swollen and inflamed. **Fact:** Studies have found mostly wear-and-tear changes rather than inflammation [S2][S3].
- **Myth:** Most people with plantar fasciitis need surgery. **Fact:** Surgery is rarely needed, and only about 1% of patients have it [S1][S2].
- **Myth:** All heel pain is plantar fasciitis. **Fact:** It is the most common cause, but arthritis, nerve problems, and hidden fractures can also cause heel pain [S2][S4].

## Questions to Ask Your Doctor
1. Is my heel pain from plantar fasciitis, or could it be something else?
2. Do I need an X-ray or ultrasound?
3. What kinds of shoes, inserts, or exercises might help my heel?
4. What other treatments could we try if simple measures do not help?
5. How long does it usually take for this kind of heel pain to get better?

## Test Questions
1. What does the plantar fascia do? - It supports the arch of the foot and helps the foot push off when walking [S2].
2. When is plantar fasciitis pain usually worst? - With the first steps after rest, such as in the morning [S2][S3].
3. Name one risk factor for plantar fasciitis. - Examples: being overweight, a stiff ankle, or a tight Achilles tendon [S2][S3].
4. What can an ultrasound show in plantar fasciitis? - A thickened plantar fascia, over 4.0 mm [S4].
5. About how many people with plantar fasciitis need surgery? - About 1% [S2].

## Related Topics
- Often confused with / contrasts with: Achilles Tendinopathy (KO-FOOT-COND-004)
- Proposed topics: Plantar fascia, Calcaneus (heel bone), Foot ultrasound, Foot X-ray, Extracorporeal shockwave therapy, Plantar fascia release, Obesity / high body mass index.

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Heel Injuries and Disorders.* https://medlineplus.gov/heelinjuriesanddisorders.html (retrieved 2026-10-26)
2. [S2] Annals of The Royal College of Surgeons of England. *Plantar fasciitis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC3954277/ (retrieved 2026-10-26)
3. [S3] Life. *A Systematic Review of Systematic Reviews on the Epidemiology, Evaluation, and Treatment of Plantar Fasciitis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC8705263/ (retrieved 2026-10-26)
4. [S4] Journal of Foot and Ankle Research. *Diagnostic imaging for chronic plantar heel pain: a systematic review and meta-analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC2784446/ (retrieved 2026-10-26)
