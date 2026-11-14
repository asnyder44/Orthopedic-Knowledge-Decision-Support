---
schema_version: okds-ko-1.0
ko_id: KO-HAND-COND-004
title: De Quervain Tenosynovitis
preferred_term: De Quervain Tenosynovitis
alternate_terms:
- de Quervain's tenosynovitis
- de Quervain syndrome
ko_type: Condition
specialty: HAND
cluster: 2
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: De Quervain tenosynovitis is a painful overuse condition of two thumb tendons where they pass
  through a tight tunnel on the thumb side of the wrist [S1][S3]. It causes pain and tenderness over and
  just above the bony bump on the thumb side of the wrist, and it is much more common in women, including
  new mothers [S1][S3]. Care often starts with activity advice, a thumb splint, or a steroid shot, and surgery
  is an option if these do not help [S1][S4].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- thumb pain
- wrist pain
- tendon sheath
- first dorsal compartment
- thumb spica splint
- pregnancy and new mothers
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-TRT-002
  target_label: Corticosteroid Injection
  source_ids:
  - S1
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-TRT-001
  target_label: Wrist Splinting
  source_ids:
  - S1
proposed_concepts:
- term: First dorsal (extensor) compartment of the wrist
  suggested_type: AnatomicalStructure
  predicate: AFFECTS
  reason: S1, S3, and S4 say de Quervain tenosynovitis involves this tendon tunnel; it is not in the registry.
- term: Finkelstein test
  suggested_type: DiagnosticTest
  predicate: DIAGNOSED_BY
  reason: S2 and S5 use the Finkelstein test to check for de Quervain tenosynovitis; it is not in the registry.
- term: Thumb spica splint
  suggested_type: Treatment
  predicate: PREREQUISITE_FOR
  reason: S1 found that adding 3 to 4 weeks in a thumb spica splint to a steroid shot gave a small extra
    benefit; Wrist Splinting (KO-HAND-TRT-001) covers wrist-only braces.
- term: De Quervain release (first dorsal compartment release)
  suggested_type: Procedure
  predicate: PREREQUISITE_FOR
  reason: S2 and S4 describe open surgical release; no Procedure KO exists for it yet.
sources:
- id: S1
  title: Management of de Quervain Tenosynovitis
  publisher: JAMA Network Open
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10611995/
  source_type: journal_article
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC10611995). Licence: CC BY'
- id: S2
  title: Surgical Management of De Quervain Tenosynovitis
  publisher: Asian Journal of Orthopaedic Research
  url: https://hal.science/hal-05200809v1
  source_type: journal_article
  audience: clinician
  publication_date: '2022'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via hal. Licence: not stated. Type: article. Text kept: abstract only.'
- id: S3
  title: Risk Factors Associated With de Quervain Tenosynovitis in Postpartum Women
  publisher: Hand (New York, N.Y.)
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11141414/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: article. Text kept: abstract only.'
- id: S4
  title: 'Optimal Skin Incision for the Surgical Treatment of De Quervain Tenosynovitis: A Systematic
    Review and Meta-Analysis'
  publisher: Medicina
  url: https://www.mdpi.com/1648-9144/62/3/590
  source_type: systematic_review
  audience: clinician
  publication_date: '2026'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via doaj. Licence: open access journal (licence per article: <verify>). Type: systematic
    review. Text kept: abstract only.'
- id: S5
  title: 'The association between smartphone addiction and thumb/wrist pain: A cross-sectional study'
  publisher: Medicine
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7478614/
  source_type: journal_article
  audience: clinician
  publication_date: '2020'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: article. Text kept: abstract only.'
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
  - No patient-level page (MedlinePlus/NIAMS) covering de Quervain tenosynovitis was found in the dataset
    or the candidates; all five sources are clinician-level. Consider adding a patient education page.
  - The sources do not give 'when to seek care' warning signs; that section says so and points to a clinician.
    Clinician should review.
  - S2 is a single-center surgical case series (abstract only, licence not stated) and S5 is a student survey
    on smartphone use; both are weaker evidence. S4's licence is unconfirmed (link_and_paraphrase).
  - The PREREQUISITE_FOR link to Wrist Splinting (KO-HAND-TRT-001) is loose; S1 studied a thumb spica splint,
    which also holds the thumb. Consider a Thumb Spica Splint KO (see proposed_concepts).
  - S1 names the HANDGUIDE expert consensus but the guideline itself is not in the pack.
  - MeSH ID and ICD-10-CM code are not stated in any source; left as verify.
  - Plain-language explanations of terms (e.g., 'radial styloid', 'sheath') were written by the drafter;
    check they match the sources.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- A clinical practice guideline for de Quervain tenosynovitis is published or the HANDGUIDE consensus is
  updated.
- A new network meta-analysis compares steroid injection, splinting, and surgery for de Quervain tenosynovitis.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
De Quervain tenosynovitis is a painful overuse condition of two thumb tendons where they pass through a tight tunnel on the thumb side of the wrist [S1][S3]. It causes pain and tenderness over and just above the bony bump on the thumb side of the wrist, and it is much more common in women, including new mothers [S1][S3]. Care often starts with activity advice, a thumb splint, or a steroid shot, and surgery is an option if these do not help [S1][S4].

## Key Facts (claim → source)
- De Quervain tenosynovitis affects two tendons that move the thumb, where they run through the first dorsal compartment, a tunnel on the thumb side of the wrist [S1][S3][S4].
- The tunnel's lining and covering get thicker, and overuse wear of the tendons seems more likely than inflammation to be the main cause [S1].
- Women get it about 6 times more often than men, and it is common during pregnancy and breastfeeding [S3].
- Diagnosis is mostly based on symptoms and an exam, and imaging such as ultrasound or MRI can help when the diagnosis is unclear [S1].
- There are no definitive treatment guidelines, but experts agree that care should start with advice about activity and pain, along with options such as anti-inflammatory medicines, splints, steroid shots, or surgery [S1].
- In a large review, a steroid shot plus 3 to 4 weeks in a thumb splint was the most likely option to improve hand function, though the splint added only a small benefit [S1].
- Open surgery to release the tunnel is a standard option when other treatments do not work [S2][S4].

## Explanation
### What it is
Two tendons that move the thumb (the abductor pollicis longus and the extensor pollicis brevis) pass through a narrow tunnel on the thumb side of the wrist called the first dorsal compartment [S1][S3]. In de Quervain tenosynovitis, this tunnel becomes too tight for the tendons [S3][S4]. The sheath around the tendons (a tube of tissue that lets them glide) and the band over it get thicker, and the tendons themselves may thin and wear down [S1]. Whether inflammation plays a part is still debated [S1].

### Causes and risk factors
The exact cause is not known, but overuse of the tendons is thought to be the most likely reason [S1]. Factors linked to it include:
- Being a woman: women are affected about 6 times as often as men [S3].
- Pregnancy and breastfeeding [S3].
- In new mothers, a first childbirth, a pregnancy longer than 40 weeks, and a higher body weight (BMI over 25) [S3].
- Manual work that uses the hands a lot [S2].

In one study of new mothers, the baby's birth weight and having twins did not raise the risk, even though they might add load when holding the baby [S3]. In a study of university students, heavy smartphone use was linked to more hand and wrist pain [S5].

### Symptoms
- Pain and tenderness over and just above the radial styloid, the bony bump on the thumb side of the wrist [S1].
- Sharp pain when this area is pressed or when the thumb tendons are stretched [S2].
- Pain is the most common reason people seek care, and the dominant hand is affected most often [S2].

The condition can make the hand hard to use, especially for people who do manual work [S2].

### How it is diagnosed
The diagnosis is mainly clinical, which means it is based on the history and a physical exam [S1]. Providers press on the thumb side of the wrist and do stretching tests, such as the Finkelstein test, that stretch the affected tendons to see if this causes pain [S2][S5]. Ultrasound or magnetic resonance imaging (MRI) can be useful when the diagnosis is not clear [S1].

### Treatment options
There are no definitive guidelines, and many treatments are available [S1]. Experts in a European consensus agreed that everyone with the condition should get advice about activity, hand use, and pain, together with one or more treatments [S1]. Treatment usually steps up from advice and anti-inflammatory medicines to surgery, based on how severe and how long-lasting the problem is [S1].
- **Steroid shot (corticosteroid injection):** this is one of the main treatments studied for this condition [S1]. In one large review, treatments that included a steroid shot guided by ultrasound ranked highest for pain relief [S1].
- **Thumb splint (thumb spica):** wearing a splint that holds the thumb and wrist for 3 to 4 weeks after a steroid shot gave a small extra gain in hand function [S1]. The review authors suggest this pairing as a first-line treatment [S1].
- **Other options:** treatments such as hyaluronic acid shots, shock wave therapy, acupuncture, and laser therapy have only limited evidence [S1].
- **Surgery:** in open surgery, the surgeon opens the tight tunnel to free the tendons, which is a standard option when other treatments fail [S2][S4]. Risks include injury to a small nearby skin nerve (the superficial branch of the radial nerve), a tendon, or veins, as well as thick scars or infection [S4]. In one review, the direction of the skin cut (across or along the wrist) did not change complication rates or pain relief [S4]. In one case series, most patients went back to work within a month after surgery [S2].

### When to seek care
The sources here do not list specific warning signs, so ask a clinician which symptoms need prompt attention. Ongoing pain on the thumb side of the wrist is worth checking with a health care provider, because this condition can make it hard to use the hand and to work [S1][S2].

## Common Misunderstandings
- **Myth:** De Quervain tenosynovitis is always caused by inflammation. **Fact:** The role of inflammation is debated, and tendon wear from overuse seems the most likely cause [S1].
- **Myth:** It is a minor problem that never affects daily life. **Fact:** It can be disabling and can keep manual workers away from their jobs [S2].
- **Myth:** Holding a heavy baby is the main reason new mothers get it. **Fact:** In one study, the baby's birth weight and having twins did not raise the risk, while a first or long pregnancy did [S3].
- **Myth:** Surgery must be done through one specific type of cut. **Fact:** A review found no clear difference in complications or pain between cuts made across or along the wrist [S4].

## Questions to Ask Your Doctor
1. Is my thumb and wrist pain de Quervain tenosynovitis, or could it be something else?
2. Do I need an ultrasound or other imaging?
3. Would a steroid shot, a thumb splint, or both make sense for me?
4. How can I change the way I use my hands to ease the pain?
5. If other treatments do not help, what would surgery involve and what are the risks?

## Test Questions
1. Where in the body does de Quervain tenosynovitis happen? - In the first dorsal compartment, a tendon tunnel on the thumb side of the wrist [S1][S3].
2. Who gets it more often? - Women, about 6 times more often than men, and it is common in pregnancy and breastfeeding [S3].
3. How is it usually diagnosed? - Mainly by history and physical exam, with ultrasound or MRI if the diagnosis is unclear [S1].
4. Which non-surgical pairing ranked well in a large review? - A steroid shot followed by 3 to 4 weeks in a thumb splint [S1].
5. When is surgery a standard option? - When other treatments have not worked [S4].

## Related Topics
- Read next: Corticosteroid Injection (KO-HAND-TRT-002), Wrist Splinting (KO-HAND-TRT-001)

## References
1. [S1] JAMA Network Open. *Management of de Quervain Tenosynovitis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10611995/ (retrieved 2026-10-26)
2. [S2] Asian Journal of Orthopaedic Research. *Surgical Management of De Quervain Tenosynovitis.* https://hal.science/hal-05200809v1 (retrieved 2026-11-14)
3. [S3] Hand (New York, N.Y.). *Risk Factors Associated With de Quervain Tenosynovitis in Postpartum Women.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11141414/ (retrieved 2026-11-14)
4. [S4] Medicina. *Optimal Skin Incision for the Surgical Treatment of De Quervain Tenosynovitis: A Systematic Review and Meta-Analysis.* https://www.mdpi.com/1648-9144/62/3/590 (retrieved 2026-11-14)
5. [S5] Medicine. *The association between smartphone addiction and thumb/wrist pain: A cross-sectional study.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7478614/ (retrieved 2026-11-14)
