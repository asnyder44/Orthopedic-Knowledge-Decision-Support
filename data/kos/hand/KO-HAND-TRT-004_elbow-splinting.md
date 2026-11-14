---
schema_version: okds-ko-1.0
ko_id: KO-HAND-TRT-004
title: Elbow Splinting
preferred_term: Elbow Splinting
alternate_terms:
- night elbow brace
- elbow extension splint
- cubital tunnel splint
- elbow orthosis
- night splint for cubital tunnel syndrome
- nocturnal elbow splinting
- elbow night splinting
ko_type: Treatment
specialty: HAND
cluster: 4
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Elbow splinting means wearing a splint or brace, usually at night, that stops the elbow from bending
  too far so there is less pressure and stretch on the ulnar nerve [S1]. It is a non-surgical treatment
  for early or mild cubital tunnel syndrome [S4]. Studies are small, and one trial found that night splints
  added no extra benefit to simple advice about avoiding positions that bring on symptoms [S1][S2].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- elbow splint
- night brace
- orthosis
- cubital tunnel syndrome treatment
- ulnar nerve
- non-surgical treatment
relationships:
- predicate: TREATS
  target_id: KO-HAND-COND-002
  target_label: Cubital Tunnel Syndrome
  source_ids:
  - S1
  - S2
  - S4
- predicate: ALTERNATIVE_TO
  target_id: KO-HAND-TRT-003
  target_label: Hand Therapy Exercises
  source_ids:
  - S1
  - S2
- predicate: ALTERNATIVE_TO
  target_id: KO-HAND-PROC-003
  target_label: Cubital Tunnel Release
  source_ids:
  - S1
  - S4
proposed_concepts:
- term: Elbow orthosis (night brace / elbow splint device)
  suggested_type: Device
  predicate: USES_DEVICE
  reason: S1 describes padded plastic splints, neoprene braces with aluminum supports, custom thermoplastic
    orthoses and a prefabricated brace that limits bending to 45 degrees; the registry has only a wrist
    orthosis device.
- term: Activity modification and patient education for cubital tunnel syndrome
  suggested_type: Treatment
  predicate: ALTERNATIVE_TO
  reason: S1 reports a trial where advice on avoiding provoking positions worked as well as night splints
    or nerve gliding.
sources:
- id: S1
  title: 'Ulnar Neuropathy at the Elbow: From Ultrasound Scanning to Treatment'
  publisher: Frontiers in Neurology
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8160369/
  source_type: journal_article
  audience: clinician
  publication_date: '2021'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC8160369 sections: non-surgical). Licence: CC BY'
- id: S2
  title: 'The Use of Physiotherapy in the Conservative Treatment of Cubital Tunnel Syndrome: A Critical
    Review of the Literature'
  publisher: Diagnostics
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11171884/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC11171884 sections: results). Licence: CC BY'
- id: S3
  title: 'The Effects of Physiotherapy in the Treatment of Cubital Tunnel Syndrome: A Systematic Review'
  publisher: Journal of Clinical Medicine
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9318553/
  source_type: journal_article
  audience: clinician
  publication_date: '2022'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC9318553 sections: interventions). Licence: CC BY'
- id: S4
  title: 'Cubital tunnel syndrome: current principles of diagnosis and treatment'
  publisher: Неврология, нейропсихиатрия, психосоматика
  url: https://nnp.ima-press.net/nnp/article/view/1126
  source_type: journal_article
  audience: clinician
  publication_date: '2019'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via doaj. Licence: open access journal (licence per article: <verify>). Type: article.
    Text kept: abstract only.'
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
  - 'Risks and side effects: no source in the pack reports harms or side effects of elbow splinting. The
    section says so. Add a source that reports safety or comfort/adherence problems.'
  - No patient-level page (MedlinePlus/NIAMS) on elbow splinting or cubital tunnel syndrome was found in
    the local dataset or the candidates; consider adding one (e.g. AAOS OrthoInfo 'Cubital tunnel syndrome').
  - The splint positions in S1 (about 30-35 degrees of elbow bend for 6 months; a brace limiting bending
    to 45 degrees) come from single studies, and S2 notes that the elbow angle varied widely between studies.
    Clinician check that the KO does not read as a recommended setting.
  - 'Evidence is weak: S1 says conservative care rests mostly on experience and small studies; S2 and S3
    say firm conclusions are not possible. S1''s Svernlov trial (51 completers) found no added benefit
    from night splints over advice alone. Clinician check that the KO is balanced.'
  - S3 contributes only that an orthosis was tested in one trial; S4 is an abstract with an unclear licence
    (link_and_paraphrase). The PMC10823195 review section on splinting (37,000 characters) is too long
    for the pack's size limit and could not be used.
  - codes.mesh and codes.icd10cm are <verify>; no source states a code.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- A new randomized trial or systematic review of night splinting for cubital tunnel syndrome is published.
- A guideline on non-surgical treatment of cubital tunnel syndrome is published or updated.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Elbow splinting is a non-surgical treatment for cubital tunnel syndrome, a condition where the ulnar nerve is squeezed at the elbow [S4]. The ulnar nerve is the nerve that runs past the inner elbow; when it is squeezed, people can have numbness and weakness in the hand [S4]. A splint or brace, usually worn at night, keeps the elbow from bending too far, which lowers the pressure and stretch on the nerve [S1]. Splinting is mainly used for early or mild cases, but the research behind it is limited [S2][S4].

## Key Facts (claim → source)
- Elbow splinting is one of the non-surgical options for early-stage and mild cubital tunnel syndrome [S4].
- The main idea of a splint is to limit elbow bending so there is less squeezing and stretching of the ulnar nerve [S1].
- Bending the elbow strongly increases strain on the ulnar nerve [S1].
- During sleep, the arm can bend sharply without the person knowing, so a night brace may be useful in some cases [S1].
- Splints range from a rolled towel held with an elastic bandage to braces and custom-made plastic splints [S1].
- In three studies without a comparison group, elbow night splinting was the main treatment, and 73% to 100% of people improved on the measures checked [S2].
- In one trial, people who wore a night brace did no better than people who only got advice on avoiding positions that cause symptoms [S1].

## Explanation
### What it is
An elbow splint or brace holds the elbow so it cannot bend too much [S1]. It is usually worn at night [S1][S2]. Types include [S1]:
- A rolled towel placed in the front crease of the elbow and held with an elastic bandage.
- A soft neoprene brace with aluminum strips for support.
- A padded plastic splint that runs from the middle of the upper arm to the hand.
- A rigid custom-made splint shaped from heat-molded plastic (thermoplastic).

### How it helps
Stretching (traction) is thought to be one of the main ways the ulnar nerve is harmed, and bending the elbow greatly raises the strain on the nerve [S1]. Splinting works by limiting how far the elbow bends, which lowers the squeezing and stretching of the nerve [S1]. People cannot control their arm position while asleep, and the elbow may bend sharply during the night [S1]. A night brace helps keep the elbow from staying in that bent position [S1].

### Who it may suit
- Non-surgical treatment, including elbow splinting, is advised for early-stage and mild cubital tunnel syndrome [S4].
- One review suggested that splinting and changing activities may help people with mild or moderate disease [S1].
- Non-surgical care seems less suitable for people whose symptoms started after an injury and have lasted [S1].
- Surgery is considered when non-surgical treatment does not work, or when hand muscles are clearly weak or shrinking [S4].

A doctor or hand therapist can say whether a splint fits a person's situation.

### Risks and side effects
The sources used here do not report side effects or harms of elbow splinting [S1][S2]. This does not prove there are none, so ask a clinician what to watch for.

### Evidence summary
- Non-surgical care for this condition is based more on experience than on strong research, and most studies are small case reports or case series [S1].
- In one small study, wearing a padded night splint with the elbow slightly bent for 6 months led to clearly better symptoms [S1]. In practice, night splinting may be shorter, depending on how fast symptoms improve [S1].
- In a trial of manual workers with mild to moderate symptoms, a night brace, nerve gliding exercises, and advice alone gave similar results after 6 months [S1]. About 90% improved, and the night splints did not add benefit beyond advice on avoiding positions that cause symptoms [S1].
- A 2024 review found three studies without comparison groups in which night splinting was the main treatment; most participants improved [S2]. The angle of the elbow in the splint varied a lot between studies [S2].
- An orthosis was one of the treatments tested in a randomized trial included in a 2022 review [S3]. Reviews say that there are too few good trials to draw firm conclusions about physical therapy treatments for this condition [S2][S3].

## Common Misunderstandings
- **Myth:** A splint is proven to work better than other simple steps. **Fact:** In one trial, night braces did not add benefit beyond advice on avoiding positions that cause symptoms [S1].
- **Myth:** The splint should hold the arm bent so it feels relaxed. **Fact:** The goal of splinting is to limit elbow bending, because bending raises strain on the ulnar nerve [S1].
- **Myth:** Splinting is the right treatment for every case. **Fact:** Non-surgical care is mainly for early or mild cases, and surgery is considered when it does not work or the hand muscles are weak [S4].
- **Myth:** A special brace is always needed. **Fact:** Options range from a rolled towel and elastic bandage to custom-made splints [S1].

## Questions to Ask Your Doctor
1. Could a night elbow splint help my symptoms?
2. What type of splint or brace should I use, and who should fit it?
3. How long should I wear it, and when should I expect to notice a change?
4. Which arm positions or activities should I avoid during the day?
5. What should I do if the splint is uncomfortable or my symptoms get worse?
6. At what point should we talk about other treatments or surgery?

## Test Questions
1. What is the main purpose of an elbow splint for cubital tunnel syndrome? - To limit elbow bending and reduce pressure and stretch on the ulnar nerve [S1].
2. Why is the splint usually worn at night? - Because the elbow may bend sharply during sleep without the person controlling it [S1].
3. Name two types of elbow splint. - A rolled towel with an elastic bandage, a neoprene brace, or a custom thermoplastic splint [S1].
4. For which stage of cubital tunnel syndrome is non-surgical treatment like splinting mainly used? - Early-stage and mild disease [S4].
5. In the trial of manual workers, did night splints add benefit beyond advice alone? - No, results were similar [S1].
6. In the studies where night splinting was the main treatment, what share of people improved? - Between 73% and 100% on the measures checked [S2].

## Related Topics
- Treats: Cubital Tunnel Syndrome (KO-HAND-COND-002)
- Alternative to: Hand Therapy Exercises (KO-HAND-TRT-003), Cubital Tunnel Release (KO-HAND-PROC-003)
- Proposed new topics: Elbow orthosis (device), Activity modification and patient education for cubital tunnel syndrome (treatment)

## References
1. [S1] Frontiers in Neurology. *Ulnar Neuropathy at the Elbow: From Ultrasound Scanning to Treatment.* https://pmc.ncbi.nlm.nih.gov/articles/PMC8160369/ (retrieved 2026-10-26)
2. [S2] Diagnostics. *The Use of Physiotherapy in the Conservative Treatment of Cubital Tunnel Syndrome: A Critical Review of the Literature.* https://pmc.ncbi.nlm.nih.gov/articles/PMC11171884/ (retrieved 2026-10-26)
3. [S3] Journal of Clinical Medicine. *The Effects of Physiotherapy in the Treatment of Cubital Tunnel Syndrome: A Systematic Review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC9318553/ (retrieved 2026-10-26)
4. [S4] Неврология, нейропсихиатрия, психосоматика. *Cubital tunnel syndrome: current principles of diagnosis and treatment.* https://nnp.ima-press.net/nnp/article/view/1126 (retrieved 2026-11-14)
