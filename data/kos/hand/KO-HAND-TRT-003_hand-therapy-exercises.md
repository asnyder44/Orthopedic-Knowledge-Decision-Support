---
schema_version: okds-ko-1.0
ko_id: KO-HAND-TRT-003
title: Hand Therapy Exercises
preferred_term: Hand Therapy Exercises
alternate_terms:
- nerve gliding exercises
- tendon gliding exercises
- nerve gliding
- tendon gliding
- neurodynamic techniques
- neurodynamic modulation
- ulnar nerve gliding exercise
ko_type: Treatment
specialty: HAND
cluster: 4
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Hand therapy exercises such as nerve gliding and tendon gliding are movements of the arm, wrist,
  and fingers meant to help a squeezed nerve slide more freely [S1][S4]. They are a non-surgical treatment
  for carpal tunnel syndrome and cubital tunnel syndrome, and they are also used after carpal tunnel surgery
  [S1][S4][S5]. Studies suggest they may ease symptoms, mostly when combined with other usual treatments
  [S2][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- hand therapy
- nerve gliding
- tendon gliding
- physical therapy
- occupational therapy
- carpal tunnel syndrome treatment
- cubital tunnel syndrome treatment
- non-surgical treatment
relationships:
- predicate: TREATS
  target_id: KO-HAND-COND-001
  target_label: Carpal Tunnel Syndrome
  source_ids:
  - S1
  - S2
  - S3
- predicate: TREATS
  target_id: KO-HAND-COND-002
  target_label: Cubital Tunnel Syndrome
  source_ids:
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-REHAB-001
  target_label: Recovery After Carpal Tunnel Release
  source_ids:
  - S5
proposed_concepts:
- term: Carpal bone mobilization technique
  suggested_type: Treatment
  predicate: ALTERNATIVE_TO
  reason: S3 compares neurodynamic techniques with carpal bone mobilization, both combined with tendon
    gliding exercises.
- term: Elbow flexion test
  suggested_type: DiagnosticTest
  predicate: PREREQUISITE_FOR
  reason: S4 uses the elbow flexion test to track cubital tunnel symptoms before and after ulnar nerve
    gliding exercise.
sources:
- id: S1
  title: 'Neurodynamic Techniques in the Treatment of Mild-to-Moderate Carpal Tunnel Syndrome: A Systematic
    Review and Meta-Analysis'
  publisher: Journal of clinical medicine
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10419623/
  source_type: systematic_review
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via europepmc. Licence: cc by. Type: systematic review. Text kept: abstract only.'
- id: S2
  title: 'Efficacy of tendon and nerve gliding exercises for carpal tunnel syndrome: a systematic review
    of randomized controlled trials'
  publisher: Journal of physical therapy science
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4563334/
  source_type: systematic_review
  audience: clinician
  publication_date: '2015'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via europepmc. Licence: cc by-nc-nd. Type: systematic review. Text kept: abstract only.'
- id: S3
  title: Comparison of Two Manual Therapy Programs, including Tendon Gliding Exercises as a Common Adjunct,
    While Managing the Participants with Chronic Carpal Tunnel Syndrome
  publisher: Pain research & management
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9200595/
  source_type: journal_article
  audience: clinician
  publication_date: '2022'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via doaj, europepmc. Licence: cc by. Type: trial. Text kept: abstract only.'
- id: S4
  title: Clinical outcomes of ulnar nerve gliding exercise in the nonoperative treatment of cubital tunnel
    syndrome
  publisher: Elsevier BV
  url: https://doi.org/10.1016/j.jseint.2025.02.001
  source_type: journal_article
  audience: clinician
  publication_date: '2025'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via openaire. Licence: Open Access. Type: article. Text kept: abstract only.'
- id: S5
  title: Sensory Nerve Conduction Velocity Predicts Improvement of Hand Function with Nerve Gliding Exercise
    Following Carpal Tunnel Release Surgery
  publisher: Journal of clinical medicine
  url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8470096/
  source_type: journal_article
  audience: clinician
  publication_date: '2021'
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
  - 'Risks and side effects: none of the five sources (all abstracts) report harms or side effects of
    nerve or tendon gliding. The section says so. Add a source that reports safety (e.g. a full-text
    trial or a hand therapy guideline).'
  - No source in the pack explains step by step how tendon gliding or median nerve gliding exercises
    are done; only S4 describes its ulnar nerve gliding method. A patient-level page (e.g. NIAMS or
    MedlinePlus) or a hand therapy text with exercise descriptions would help. No MedlinePlus/NIAMS page
    in the local dataset covers these exercises.
  - All five sources are abstracts only. S2 is CC BY-NC-ND (link_and_paraphrase) and S4 has an unclear
    licence (link_and_paraphrase); paraphrase only.
  - S4 is a small case series (17 patients) with no control group; the KO describes it as one small
    study. Clinician check that the cubital tunnel claims are not overstated.
  - S1 pools 'neurodynamic techniques', which include therapist-applied nerve mobilization as well as
    self-done gliding exercises; confirm the KO's wording keeps these apart.
  - codes.mesh and codes.icd10cm are <verify>; no source states a code.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- A new systematic review or large randomized trial of nerve or tendon gliding exercises for carpal or
  cubital tunnel syndrome is published.
- AAOS or another guideline body updates its recommendations on exercise therapy for carpal or cubital
  tunnel syndrome.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Hand therapy exercises are planned movements of the arm, wrist, and fingers [S1][S4]. Nerve gliding exercises aim to help a nerve slide smoothly as the arm moves, and tendon gliding exercises move the finger tendons (cords that connect muscle to bone) [S1][S3]. They are used as a non-surgical treatment for carpal tunnel syndrome (CTS) and cubital tunnel syndrome, and also after carpal tunnel surgery [S1][S4][S5]. Research suggests they may help, mostly when they are added to other usual treatments [S2][S3].

## Key Facts (claim → source)
- Carpal tunnel syndrome is pressure on the median nerve at the wrist that can cause numbness, tingling, and weakness in the hand [S1][S3].
- Non-surgical care for CTS can include techniques that help the median nerve glide during arm movements [S1].
- A review of 12 randomized trials with about 1,000 people found that these nerve techniques lowered CTS symptom scores and pain, but did not change grip strength [S1].
- A review of 4 trials found that tendon or nerve gliding plus usual treatment worked better than usual treatment alone [S2].
- In cubital tunnel syndrome, swelling around the ulnar nerve at the elbow can stop it from gliding normally [S4].
- In one small study, an ulnar nerve gliding program led by an occupational therapist reduced tingling and improved grip strength in people with cubital tunnel syndrome [S4].
- After carpal tunnel surgery, adding nerve gliding exercise was linked with better grip, pinch, and feeling in the hand, but not less pain [S5].

## Explanation
### What it is
Hand therapy exercises are a treatment that does not involve surgery [S1]. This topic covers two main kinds [S2]:
- **Nerve gliding exercises** are arm, wrist, and hand movements meant to help a nerve slide back and forth as the limb moves [S1]. Researchers also call these neurodynamic techniques [S1].
- **Tendon gliding exercises** move the tendons that bend the fingers; one study used them as an add-on to other hand treatments [S3].

For the elbow, one team designed an ulnar nerve gliding exercise in which a therapist moved the wrist back and forth while the elbow was fully bent [S4]. The ulnar nerve is the nerve that runs past the inside of the elbow to the ring and little fingers [S4].

### How it helps
In carpal tunnel syndrome, the median nerve is squeezed at the wrist [S3]. Nerve gliding aims to help this nerve slide normally during upper limb movements so the arm keeps working well [S1]. In cubital tunnel syndrome, swelling and irritation around the ulnar nerve can block its normal gliding, which can cause pain, tingling (paresthesia), and muscle weakness [S4]. The gliding exercise aims to restore that movement [S4]. Tendon gliding exercises were used to boost the effect of other hands-on treatments [S3].

### Who it may suit
- People with mild to moderate carpal tunnel syndrome were the focus of one large review [S1].
- People with long-lasting (chronic) carpal tunnel syndrome were studied in a trial that used tendon gliding [S3].
- One small study found the ulnar nerve gliding exercise may be a useful option for moderate cubital tunnel syndrome [S4]. In that study, one person with severe cubital tunnel syndrome did not improve and went on to have surgery [S4].
- People recovering from carpal tunnel release surgery were studied in another report [S5].

A doctor or hand therapist can say whether these exercises fit a person's situation.

### Risks and side effects
The sources used here do not report side effects or harms of nerve or tendon gliding exercises [S1][S2]. This does not prove the exercises have no risks, so ask a clinician or hand therapist about what to watch for. In one study, nerve gliding after carpal tunnel surgery did not reduce pain [S5].

### Evidence summary
- A 2023 review pooled 12 randomized trials with 1,003 people with mild to moderate CTS [S1]. Nerve techniques lowered symptom severity and pain and improved nerve test results, but grip strength did not change [S1]. The studies differed a lot and some had risk of bias [S1].
- A 2015 review found only 4 trials, with low to moderate risk of bias [S2]. Gliding exercises plus usual care seemed to help symptoms and hand function [S2]. The authors said more trials are needed to test the exercises on their own [S2].
- A small trial of 30 people with chronic CTS found that tendon gliding was a helpful add-on to two kinds of hands-on therapy [S3].
- A study of 17 people with cubital tunnel syndrome, followed for about 5 years on average, found less tingling and better grip and pinch strength after ulnar nerve gliding [S4]. This study had no comparison group [S4].
- In 86 people after carpal tunnel surgery, surgery plus nerve gliding was linked with better grip, pinch, and feeling in the hand [S5].

## Common Misunderstandings
- **Myth:** Gliding exercises are proven to work on their own. **Fact:** Much of the evidence comes from studies that combined the exercises with other treatments, and reviewers say more trials of the exercises alone are needed [S2][S3].
- **Myth:** Nerve gliding makes the hand stronger. **Fact:** A large review found less pain and fewer symptoms, but no clear change in grip strength [S1].
- **Myth:** Exercises only matter before surgery. **Fact:** Nerve gliding has also been studied after carpal tunnel release surgery [S5].
- **Myth:** Exercises always work, even for severe nerve problems. **Fact:** In one study, a person with severe cubital tunnel syndrome did not improve with the exercise and later had surgery [S4].

## Questions to Ask Your Doctor
1. Could nerve or tendon gliding exercises help my hand or elbow symptoms?
2. Should I learn these exercises from a hand therapist or physical therapist?
3. Should I do these exercises along with other treatments, such as a splint?
4. What should I do if an exercise makes my numbness or pain worse?
5. How long should I try the exercises before we talk about other options?
6. Should I do nerve gliding exercises after my surgery?

## Test Questions
1. What is the goal of nerve gliding exercises? - To help a nerve slide smoothly during arm and hand movements [S1].
2. Which nerve is squeezed in carpal tunnel syndrome? - The median nerve at the wrist [S3].
3. In the 2023 review, what did nerve techniques improve, and what did they not change? - They lowered symptoms and pain but did not change grip strength [S1].
4. According to the 2015 review, when did gliding exercises seem to help? - When combined with conventional treatments [S2].
5. What can stop the ulnar nerve from gliding in cubital tunnel syndrome? - Swelling and inflammation around the nerve [S4].
6. Name one result linked with nerve gliding after carpal tunnel surgery. - Better grip strength, pinch strength, or feeling in the hand [S5].

## Related Topics
- Treats: Carpal Tunnel Syndrome (KO-HAND-COND-001), Cubital Tunnel Syndrome (KO-HAND-COND-002)
- Read before: Recovery After Carpal Tunnel Release (KO-HAND-REHAB-001)
- Proposed new topics: Carpal bone mobilization technique (treatment), Elbow flexion test (diagnostic test)

## References
1. [S1] Journal of clinical medicine. *Neurodynamic Techniques in the Treatment of Mild-to-Moderate Carpal Tunnel Syndrome: A Systematic Review and Meta-Analysis.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10419623/ (retrieved 2026-11-14)
2. [S2] Journal of physical therapy science. *Efficacy of tendon and nerve gliding exercises for carpal tunnel syndrome: a systematic review of randomized controlled trials.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4563334/ (retrieved 2026-11-14)
3. [S3] Pain research & management. *Comparison of Two Manual Therapy Programs, including Tendon Gliding Exercises as a Common Adjunct, While Managing the Participants with Chronic Carpal Tunnel Syndrome.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9200595/ (retrieved 2026-11-14)
4. [S4] Elsevier BV. *Clinical outcomes of ulnar nerve gliding exercise in the nonoperative treatment of cubital tunnel syndrome.* https://doi.org/10.1016/j.jseint.2025.02.001 (retrieved 2026-11-14)
5. [S5] Journal of clinical medicine. *Sensory Nerve Conduction Velocity Predicts Improvement of Hand Function with Nerve Gliding Exercise Following Carpal Tunnel Release Surgery.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8470096/ (retrieved 2026-11-14)
