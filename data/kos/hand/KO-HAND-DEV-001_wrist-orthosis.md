---
schema_version: okds-ko-1.0
ko_id: KO-HAND-DEV-001
title: Wrist Orthosis
preferred_term: Wrist Orthosis
alternate_terms:
- wrist orthotic device
- wrist splint
- wrist brace
- hand-wrist orthosis
- neutral wrist orthosis
- night splint
ko_type: Device
specialty: HAND
cluster: 5
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: A wrist orthosis is a splint or brace worn on the hand and wrist [S1][S4]. Wearing one at night
  is a common first treatment for carpal tunnel syndrome, and static (non-moving) hand-wrist orthoses
  are also used after a stroke to help prevent contractures and a clenched fist [S1][S5].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- brace
- splint
- orthosis
- carpal tunnel
- nonsurgical treatment
- stroke
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-TRT-001
  target_label: Wrist Splinting
  source_ids:
  - S1
  - S2
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-TRT-003
  target_label: Hand Therapy Exercises
  source_ids:
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-TRT-002
  target_label: Corticosteroid Injection
  source_ids:
  - S2
proposed_concepts: []
sources:
- id: S1
  title: Carpal Tunnel Syndrome
  publisher: National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH)
  url: https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome
  source_type: government_health_page
  audience: patient
  publication_date: '2023-12-22'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (niams:carpal-tunnel-syndrome). Licence: Public domain (U.S. federal
    government work, NIH/NIAMS); credit NIAMS'
- id: S2
  title: 'Steroid versus placebo injections and wrist splints in patients with carpal tunnel syndrome:
    a systematic review and network meta-analysis'
  publisher: The Journal of Hand Surgery, European Volume
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11523550/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC11523550). Licence: CC BY'
- id: S3
  title: 'The Effects of Orthosis and Exercise on The Median Nerve Morphology and Functional Status of
    Patients with Carpal Tunnel Syndrome: A Randomized Pilot Study'
  publisher: Bezmiâlem Science
  url: https://www.bezmialemscience.org/articles/the-effects-of-orthosis-and-exercise-on-the-median-nerve-morphology-and-functional-status-of-patients-with-carpal-tunnel-syndrome-a-randomized-pilot-study/doi/bas.galenos.2024.38981
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via doaj. Licence: open access journal (licence per article: <verify>). Type: trial. Text
    kept: abstract only.'
- id: S4
  title: Effect of wrist orthoses on upper limb function, activities of daily living, and stress response
  publisher: Journal of rehabilitation and assistive technologies engineering
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11047247/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via europepmc. Licence: cc by-nc. Type: article. Text kept: abstract only.'
- id: S5
  title: 'Long-term use of a static hand-wrist orthosis in chronic stroke patients: a pilot study'
  publisher: Stroke research and treatment
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3600191/
  source_type: journal_article
  audience: clinician
  publication_date: '2013'
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
  - The sources here do not cover regulatory status (for example FDA device class) or makers of wrist
    orthoses; those subsections say so. Add a regulatory source (e.g., FDA product classification) and
    maker information before publishing.
  - The sources do not say exactly what wrist angle a 'neutral' orthosis uses, how many hours to wear
    it, or whether prefabricated or custom-made orthoses work better.
  - S3 (Bezmialem Science, small pilot RCT, 27 wrists) licence is '<verify>' per article; S4 is CC BY-NC
    (link_and_paraphrase); only abstracts are in the pack.
  - S4 tested healthy adults, not patients; its findings on function limits may not apply to people with
    carpal tunnel syndrome.
  - S5 is a small stroke pilot study (11 patients); it is used only to show that static hand-wrist orthoses
    are used in stroke care.
  - The USES_DEVICE link should be added from the Wrist Splinting (KO-HAND-TRT-001) KO, since a Device
    KO cannot state it.
  - MeSH ID is unknown ('<verify>'); ICD-10-CM does not apply to a device.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- NIAMS updates the treatment section of its carpal tunnel syndrome page.
- A new systematic review compares wrist splints with other carpal tunnel treatments.
- Any cited page shows a new 'last reviewed' date.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
A wrist orthosis is a splint or brace worn on the hand and wrist [S1][S4]. Wearing one at night is a common first treatment for carpal tunnel syndrome (CTS), a condition in which the median nerve is squeezed at the wrist [S1]. Orthoses can be made from different materials, such as padded fiberglass or thermoplastic [S4]. A splint can ease CTS symptoms for a while, but it does not fix the underlying problem with the nerve [S1].

## Key Facts (claim → source)
- Using a splint on the hand and wrist at night is a common first treatment for CTS symptoms [S1].
- Nonsurgical treatments such as splints can improve CTS symptoms in the short term but do not lead to long-term improvement of the nerve problem [S1].
- In a small study, people with mild to moderate CTS who wore a neutral wrist orthosis for 6 weeks had better scores for daily function [S3].
- A review of trials found that steroid injections gave only small, short-lived benefits compared with wrist splints [S2].
- Wearing a wrist orthosis can limit how well the hand and arm work during daily tasks [S4].
- Static (non-moving) hand-wrist orthoses are widely used after a stroke to help prevent contractures, which can leave the hand stuck in a clenched fist [S5].
- Some stroke patients stop wearing their orthosis because of discomfort, pain, or muscle tightness [S5].

## Explanation
### What it is
A wrist orthosis is a device worn on the hand and wrist, and the sources also call it a splint or brace [S1][S4]. For carpal tunnel syndrome, NIAMS describes splinting or bracing as using a splint on the hand and wrist, often at night [S1]. One type studied in people with CTS is called a neutral wrist orthosis [S3]. Static hand-wrist orthoses, which do not move, are used for other conditions such as arm weakness after a stroke [S5].

### Where it is used
- **Carpal tunnel syndrome:** A splint worn at night is a common first treatment, and NIAMS lists wearing one at night as a way to manage early symptoms [S1]. In a pilot study, all groups who wore a neutral orthosis for 6 weeks, with or without nerve and tendon gliding exercises, improved in daily function [S3]. Adding nerve gliding exercises to the orthosis also reduced swelling of the median nerve on ultrasound [S3].
- **Comparison with injections:** In a review of 10 trials, steroid injections eased pain slightly more than wrist splints, but the difference was too small to matter to patients [S2].
- **Stroke:** Static hand-wrist orthoses are used long term in people with arm weakness after a stroke to prevent contractures and a clenched fist [S5].

### Types
- **Static orthoses** hold the wrist and hand still in one position [S5].
- **Neutral wrist orthoses** have been studied for CTS, alone or combined with exercises [S3].
- **By material:** orthoses can be made of padded fiberglass or thermoplastic [S4]. In healthy adults, thermoplastic orthoses limited hand and arm movement less than padded fiberglass ones, but limited some daily activities more [S4].
- **By time of use:** splints for CTS are usually worn at night [S1].

### Regulatory status
The sources used here do not cover how wrist orthoses are regulated (for example, by the U.S. Food and Drug Administration). This needs to be added from a regulatory source before publishing.

### Makers
The sources used here do not name companies that make wrist orthoses. This needs to be added from another source before publishing.

## Common Misunderstandings
- **Myth:** A wrist splint cures carpal tunnel syndrome. **Fact:** Splints can ease symptoms in the short term, but they do not treat the underlying problem with the nerve [S1].
- **Myth:** A steroid shot always works much better than a splint. **Fact:** A review of trials found only a small, short-lived benefit of injections over splints that was below what patients notice as meaningful [S2].
- **Myth:** Wearing a wrist orthosis has no downside. **Fact:** Orthoses can limit how well the hand and arm work in daily tasks [S4].
- **Myth:** Everyone can wear an orthosis comfortably for a long time. **Fact:** Some stroke patients could not wear their orthosis as long as advised because it was uncomfortable [S5].

## Questions to Ask Your Doctor
1. What type of wrist orthosis is right for my condition?
2. When should I wear it, and for how long each day or night?
3. What should I do if the orthosis is uncomfortable or causes pain?
4. Should I do exercises while I use the orthosis?
5. What other treatments could I try if the orthosis does not help?

## Test Questions
1. When is a wrist splint usually worn for carpal tunnel syndrome? - At night [S1].
2. Does a splint fix the underlying nerve problem in CTS? - No; it can improve symptoms in the short term only [S1].
3. What two materials were compared in a study of wrist orthoses? - Padded fiberglass and thermoplastic [S4].
4. Why are static hand-wrist orthoses used after a stroke? - To help prevent contractures and a clenched fist [S5].
5. What extra benefit did nerve gliding exercises add to orthosis use in one study? - Less swelling of the median nerve [S3].

## Related Topics
- Read next: Wrist Splinting (KO-HAND-TRT-001), the treatment that uses this device
- Read next: Hand Therapy Exercises (KO-HAND-TRT-003), exercises sometimes combined with an orthosis
- Read next: Corticosteroid Injection (KO-HAND-TRT-002), a treatment compared with wrist splints
- Used in (link to be added from the treatment KO): Wrist Splinting (KO-HAND-TRT-001)

## References
1. [S1] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Carpal Tunnel Syndrome.* https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome (retrieved 2026-10-26)
2. [S2] The Journal of Hand Surgery, European Volume. *Steroid versus placebo injections and wrist splints in patients with carpal tunnel syndrome: a systematic review and network meta-analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC11523550/ (retrieved 2026-10-26)
3. [S3] Bezmiâlem Science. *The Effects of Orthosis and Exercise on The Median Nerve Morphology and Functional Status of Patients with Carpal Tunnel Syndrome: A Randomized Pilot Study.* https://www.bezmialemscience.org/articles/the-effects-of-orthosis-and-exercise-on-the-median-nerve-morphology-and-functional-status-of-patients-with-carpal-tunnel-syndrome-a-randomized-pilot-study/doi/bas.galenos.2024.38981 (retrieved 2026-11-14)
4. [S4] Journal of rehabilitation and assistive technologies engineering. *Effect of wrist orthoses on upper limb function, activities of daily living, and stress response.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11047247/ (retrieved 2026-11-14)
5. [S5] Stroke research and treatment. *Long-term use of a static hand-wrist orthosis in chronic stroke patients: a pilot study.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3600191/ (retrieved 2026-11-14)
