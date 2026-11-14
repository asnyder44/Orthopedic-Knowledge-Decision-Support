---
schema_version: okds-ko-1.0
ko_id: KO-HAND-ANAT-003
title: Ulnar Nerve
preferred_term: Ulnar Nerve
alternate_terms: []
ko_type: AnatomicalStructure
specialty: HAND
cluster: 1
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: The ulnar nerve is one of the main nerves of the arm, running from the neck area down the inner
  side of the arm, behind the elbow, and into the hand [S1][S2]. It carries feeling from the ring and little
  fingers and controls many small muscles of the hand [S1][S3]. Because it lies close to the skin at the
  elbow, it is easily squeezed or stretched there, which can cause numbness, tingling, and weakness [S1][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- nerve
- elbow
- ring and little fingers
- hand numbness
- nerve compression
- Guyon's canal
relationships:
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-ANAT-004
  target_label: Cubital Tunnel
  source_ids:
  - S1
  - S2
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-COND-002
  target_label: Cubital Tunnel Syndrome
  source_ids:
  - S1
  - S2
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-PROC-003
  target_label: Cubital Tunnel Release
  source_ids:
  - S1
  - S2
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-PROC-004
  target_label: Ulnar Nerve Transposition
  source_ids:
  - S1
  - S2
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-DX-001
  target_label: Nerve Conduction Study
  source_ids:
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-DX-005
  target_label: Nerve Ultrasound
  source_ids:
  - S2
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-ANAT-001
  target_label: Median Nerve
  source_ids:
  - S1
  - S4
proposed_concepts:
- term: Brachial plexus
  suggested_type: AnatomicalStructure
  predicate: PART_OF
  reason: S1 and S2 say the ulnar nerve is the end branch of the medial cord of the brachial plexus (C8-T1);
    would allow Ulnar Nerve PART_OF Brachial Plexus.
- term: Guyon's canal (ulnar tunnel at the wrist)
  suggested_type: AnatomicalStructure
  predicate: PREREQUISITE_FOR
  reason: S1 and S4 describe Guyon's canal as the second main place the ulnar nerve can be squeezed; not in
    the registry.
- term: Ulnar tunnel syndrome (ulnar nerve entrapment at the wrist)
  suggested_type: Condition
  predicate: PREREQUISITE_FOR
  reason: S1 and S4 describe ulnar nerve compression at the wrist; no Condition KO exists.
sources:
- id: S1
  title: The Unpredictable Ulnar Nerve—Ulnar Nerve Entrapment from Anatomical, Pathophysiological, and
    Biopsychosocial Aspects
  publisher: Diagnostics
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10931116/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC10931116). Licence: CC BY'
- id: S2
  title: 'Ulnar Neuropathy at the Elbow: From Ultrasound Scanning to Treatment'
  publisher: Frontiers in Neurology
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8160369/
  source_type: journal_article
  audience: clinician
  publication_date: '2021'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC8160369). Licence: CC BY'
- id: S3
  title: 'From Conservative Measures to Surgical Interventions, Treatment Approaches for Cubital Tunnel
    Syndrome: A Comprehensive Review'
  publisher: Cureus
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10823195/
  source_type: journal_article
  audience: clinician
  publication_date: '2023'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC10823195). Licence: CC BY'
- id: S4
  title: 'Double entrapment neuropathy of the ulnar nerve at the elbow and the wrist : double crush syndrome?'
  publisher: BMC Musculoskeletal Disorders
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11170863/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC11170863). Licence: CC BY'
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
  - No patient-level page (MedlinePlus/NIAMS) about the ulnar nerve was found in the dataset or the candidates;
    all four sources are clinician-level reviews or case series. Consider adding a patient page or the OpenStax
    nervous system chapter.
  - 'The pack keeps only the first sections of S1 and S2; S1''s section on Guyon''s canal was cut off, so
    wrist details come from S1''s anatomy section and S4 (a small case series).'
  - The CONTRASTS_WITH link to Median Nerve is based on S1 and S4 naming carpal tunnel syndrome (median nerve)
    as a separate, more common entrapment; no source directly compares the two nerves. Clinician should confirm.
  - S1 says its review reflects mainly the opinion of its own region; consensus on diagnosis and surgery is
    lacking.
  - MeSH ID is not stated in any source; left as verify. ICD-10-CM does not apply to an anatomical structure.
  - Plain-language explanations (e.g., 'medial epicondyle', 'brachial plexus') were written by the drafter;
    check they match the sources.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- A new review or guideline on ulnar nerve entrapment at the elbow or wrist is published.
- A patient-level page about the ulnar nerve or cubital tunnel syndrome is added to the dataset.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
The ulnar nerve is one of the main nerves of the arm, running from the neck area down the inner side of the arm, behind the elbow, and into the hand [S1][S2]. It carries feeling from the ring and little fingers and controls many small muscles of the hand [S1][S3]. Because it lies close to the skin at the elbow, it is easily squeezed or stretched there, which can cause numbness, tingling, and weakness [S1][S3].

## Key Facts (claim → source)
- The ulnar nerve starts from nerve roots in the lower neck (C8 and T1) and is an end branch of the brachial plexus, a network of nerves near the shoulder [S1][S2].
- It runs down the inner side of the upper arm, behind the elbow, through the cubital tunnel, along the forearm, and into the hand through Guyon's canal at the wrist [S1][S2].
- It gives feeling to the ring and little fingers and the little-finger side of the hand [S1][S3].
- It controls a forearm muscle that bends the wrist, part of a muscle that bends the fingers, and most of the small muscles inside the hand [S1].
- At the elbow it lies close to the surface, so it can be pressed or stretched when the elbow bends [S1].
- Squeezing of the ulnar nerve is the second most common nerve entrapment after carpal tunnel syndrome, and it happens most often at the elbow [S1][S2].
- Early signs of a squeezed ulnar nerve are tingling and numbness in the ring and little fingers, which can be followed by weakness [S1][S3].

## Explanation
### Where it is
The ulnar nerve begins from nerve roots in the lower neck, called C8 and T1 [S1][S2]. These form part of the brachial plexus, a network of nerves near the shoulder, and the ulnar nerve is one of its end branches [S1][S2]. The nerve travels down the inner side of the upper arm [S1][S2]. At the elbow it runs in a groove behind the medial epicondyle, the bony bump on the inner side of the elbow, and then enters the cubital tunnel [S1][S2]. It then passes under a band of tissue between the two heads of the flexor carpi ulnaris muscle and goes down the forearm [S1][S2]. Near the wrist it travels with the ulnar artery and enters the hand through a passage called Guyon's canal [S1].

In the hand, the nerve splits into three branches [S1]:
- A branch that gives feeling to the back of the hand on the little-finger side [S1].
- A branch that gives feeling to the palm side of the fingers [S1].
- A deep motor branch that powers most of the small muscles of the hand [S1].

### What it does
The ulnar nerve carries both feeling (sensory) and movement (motor) signals for the forearm and hand [S3]. It gives feeling to the ring and little fingers [S3]. In the forearm, it controls the flexor carpi ulnaris, a muscle that bends the wrist, and part of the muscle that bends the fingers [S1]. In the hand, it controls most of the small muscles that make fine finger movements possible [S1]. Its blood vessels are coiled, which lets the nerve move as the elbow bends and straightens [S1].

### Conditions that affect it
- **Cubital tunnel syndrome (ulnar neuropathy at the elbow):** pressure on or irritation of the ulnar nerve at the elbow [S2][S3]. It can cause numbness and tingling in the ring and little fingers, hand weakness, and pain on the inner elbow [S3]. Risk factors include obesity, smoking, diabetes, vibration at work, older age, and male sex [S1][S2]. If it is not treated in time, it can lead to lasting loss of feeling and weakness [S2][S3].
- **Nerve slipping out of its groove:** in some people the ulnar nerve slides out of its groove behind the elbow when the elbow bends, which may add to nerve irritation [S2].
- **Compression at the wrist:** the nerve can also be squeezed in Guyon's canal at the wrist, and rarely at both the elbow and the wrist at the same time [S1][S4].

Electrical nerve tests (nerve conduction studies and electromyography) are the standard tests for nerve problems, and ultrasound can show the nerve's shape and whether it stays in place as the elbow moves [S2][S4]. Mild to moderate symptoms are usually treated without surgery, and surgery to free the nerve is an option when that does not work or symptoms are severe [S1].

## Common Misunderstandings
- **Myth:** The ulnar nerve only matters at the elbow. **Fact:** It runs from the neck to the hand, and it can be squeezed at the elbow or at the wrist [S1][S4].
- **Myth:** Numbness in the ring and little fingers comes from the same nerve problem as carpal tunnel syndrome. **Fact:** Those fingers are mainly served by the ulnar nerve, and ulnar nerve entrapment is a separate problem from carpal tunnel syndrome [S1][S3].
- **Myth:** The ulnar nerve only gives feeling. **Fact:** It also controls most of the small muscles inside the hand [S1].

## Questions to Ask Your Doctor
1. Could my numbness in the ring and little fingers come from my ulnar nerve?
2. Is the problem at my elbow, my wrist, or somewhere else?
3. Do I need a nerve conduction study, EMG, or an ultrasound?
4. Are there ways to hold or use my elbow that would put less pressure on the nerve?
5. When would surgery to free the nerve be worth considering?

## Test Questions
1. Which fingers get feeling from the ulnar nerve? - The ring and little fingers [S3].
2. Where is the ulnar nerve most often squeezed? - At the elbow [S1][S2].
3. Name the passage at the wrist that the ulnar nerve goes through. - Guyon's canal [S1].
4. Why is the ulnar nerve easily hurt at the elbow? - It lies close to the surface and can be pressed or stretched when the elbow bends [S1].
5. What are early signs that the ulnar nerve is squeezed? - Tingling and numbness in the ring and little fingers [S1][S3].

## Related Topics
- Read next: Cubital Tunnel (KO-HAND-ANAT-004), Cubital Tunnel Syndrome (KO-HAND-COND-002)
- Tests: Nerve Conduction Study (KO-HAND-DX-001), Nerve Ultrasound (KO-HAND-DX-005)
- Surgery: Cubital Tunnel Release (KO-HAND-PROC-003), Ulnar Nerve Transposition (KO-HAND-PROC-004)
- Often confused with: Median Nerve (KO-HAND-ANAT-001)

## References
1. [S1] Diagnostics. *The Unpredictable Ulnar Nerve—Ulnar Nerve Entrapment from Anatomical, Pathophysiological, and Biopsychosocial Aspects.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10931116/ (retrieved 2026-10-26)
2. [S2] Frontiers in Neurology. *Ulnar Neuropathy at the Elbow: From Ultrasound Scanning to Treatment.* https://pmc.ncbi.nlm.nih.gov/articles/PMC8160369/ (retrieved 2026-10-26)
3. [S3] Cureus. *From Conservative Measures to Surgical Interventions, Treatment Approaches for Cubital Tunnel Syndrome: A Comprehensive Review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10823195/ (retrieved 2026-10-26)
4. [S4] BMC Musculoskeletal Disorders. *Double entrapment neuropathy of the ulnar nerve at the elbow and the wrist : double crush syndrome?.* https://pmc.ncbi.nlm.nih.gov/articles/PMC11170863/ (retrieved 2026-10-26)
