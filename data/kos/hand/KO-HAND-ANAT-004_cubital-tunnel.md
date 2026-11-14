---
schema_version: okds-ko-1.0
ko_id: KO-HAND-ANAT-004
title: Cubital Tunnel
preferred_term: Cubital Tunnel
alternate_terms: []
ko_type: AnatomicalStructure
specialty: HAND
cluster: 1
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: The cubital tunnel is a narrow passage on the inner side of the elbow that the ulnar nerve passes
  through on its way from the upper arm to the forearm [S1][S2][S3]. It is bordered by the ulna bone, the
  two starting points of a forearm muscle, and a band of tough tissue that forms its roof [S1][S2]. Because
  the space is tight and changes shape when the elbow bends, the ulnar nerve can be squeezed here, which
  is called cubital tunnel syndrome [S2][S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- elbow
- ulnar nerve
- nerve compression
- Osborne's ligament
- inner elbow
relationships:
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
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-PROC-004
  target_label: Ulnar Nerve Transposition
  source_ids:
  - S1
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-TRT-004
  target_label: Elbow Splinting
  source_ids:
  - S1
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-DX-005
  target_label: Nerve Ultrasound
  source_ids:
  - S1
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-ANAT-002
  target_label: Carpal Tunnel
  source_ids:
  - S2
proposed_concepts:
- term: Osborne's ligament (cubital tunnel retinaculum)
  suggested_type: AnatomicalStructure
  predicate: PART_OF
  reason: S2 and S4 describe this band as the roof of the cubital tunnel and a common site of ulnar nerve
    compression; would allow Osborne's ligament PART_OF Cubital Tunnel.
- term: Elbow joint
  suggested_type: AnatomicalStructure
  predicate: PART_OF
  reason: S1 and S2 place the cubital tunnel at the inner elbow; would allow Cubital Tunnel PART_OF Elbow
    Joint.
- term: Medial epicondyle
  suggested_type: AnatomicalStructure
  predicate: PREREQUISITE_FOR
  reason: S1, S2, and S4 use this bony landmark to describe the tunnel; not in the registry.
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
  notes: 'From the OrthoInfo dataset (pmc:PMC8160369). Licence: CC BY'
- id: S2
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
  title: Anatomical Factors Affecting Ulnar Neuropathy
  publisher: International Journal of Pharmaceutical and Clinical Research
  url: https://zenodo.org/records/13244629
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-11-14'
  permitted_use: open_license
  notes: 'Found via zenodo. Licence: cc-by-4.0. Type: article. Text kept: abstract only.'
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
  - No patient-level page (MedlinePlus/NIAMS) about the cubital tunnel was found in the dataset or candidates;
    all four sources are clinician-level. Consider adding a patient page.
  - 'Sources name the roof differently: S1 calls the band between the two muscle heads the humeroulnar aponeurotic
    arcade, S2 calls the roof the cubital tunnel retinaculum and names Osborne''s ligament, and S4 describes
    Osborne''s ligament from cadavers. The KO uses plain wording; anatomist should confirm.'
  - S4 is an abstract-only cadaver study from a smaller journal; its percentages are not used in the KO.
  - The CONTRASTS_WITH link to Carpal Tunnel rests on S2 naming carpal tunnel syndrome as a separate, more
    common entrapment; no source compares the two tunnels directly.
  - MeSH ID is not stated in any source; left as verify. ICD-10-CM does not apply to an anatomical structure.
  - Plain-language explanations (e.g., 'medial epicondyle', 'aponeurosis') were written by the drafter; check
    they match the sources.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- A new review or guideline on ulnar nerve entrapment at the elbow is published.
- A patient-level page about the cubital tunnel or cubital tunnel syndrome is added to the dataset.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
The cubital tunnel is a narrow passage on the inner side of the elbow that the ulnar nerve passes through on its way from the upper arm to the forearm [S1][S2][S3]. It is bordered by the ulna bone, the two starting points of a forearm muscle, and a band of tough tissue that forms its roof [S1][S2]. Because the space is tight and changes shape when the elbow bends, the ulnar nerve can be squeezed here, which is called cubital tunnel syndrome [S2][S3].

## Key Facts (claim → source)
- The cubital tunnel is at the inner (medial) side of the elbow, just past the bony bump called the medial epicondyle [S1][S2].
- Its walls are formed by the ulna (a forearm bone) and the two heads of the flexor carpi ulnaris muscle, with a thick band of tissue joining the two heads [S1][S2].
- The ulnar nerve runs through it from the upper arm into the forearm [S1][S2][S3].
- The band over the nerve, often called Osborne's ligament, is thought to be the most common place where the ulnar nerve gets squeezed [S2][S4].
- At the elbow the nerve lies close to the skin and can be pressed or stretched when the elbow bends [S2].
- The shape of the tunnel's roof varies from person to person, and in some people a small extra muscle covers it [S1][S4].
- Pressure on the ulnar nerve in this area is called cubital tunnel syndrome [S3].

## Explanation
### Where it is
The cubital tunnel is on the inner side of the elbow [S1][S3]. Just above it, the ulnar nerve runs in a groove behind the medial epicondyle, the bony bump on the inner side of the elbow [S1][S2]. The nerve then enters the cubital tunnel itself [S1][S2]. The tunnel is a space between the ulna (one of the two forearm bones) and the two heads, or starting points, of the flexor carpi ulnaris muscle, which bends the wrist [S1]. A thick band of tissue that joins the two heads of this muscle forms the roof [S1][S2]. After leaving the tunnel, the nerve runs inside and then under this muscle down the forearm [S1].

### What it does
The cubital tunnel is the path that lets the ulnar nerve pass from the arm into the forearm at the elbow [S1][S2][S3]. A thin band over the groove behind the elbow is shorter when the elbow is straight and stretches as the elbow bends, and in some people it tightens enough to press on the nerve [S1]. The nerve is close to the surface here, so bending the elbow can press on or stretch it [S2].

Cadaver studies (studies of donated bodies) show that the band, often called Osborne's ligament, usually runs from the medial epicondyle to the olecranon, the bony tip of the elbow, and joins the two heads of the muscle [S4]. In some people, a small extra muscle called the anconeus epitrochlearis also covers the roof of the tunnel [S1][S4].

### Conditions that affect it
- **Cubital tunnel syndrome:** pressure on or irritation of the ulnar nerve as it goes through the cubital tunnel [S3]. It can cause numbness and tingling in the ring and little fingers, hand weakness, and pain along the inner elbow [S3].
- **Places where the nerve gets trapped:** the two main spots are the groove behind the elbow and under the band at the entrance to the tunnel [S1][S2].
- **Space-taking lumps and variations:** a ganglion (a fluid-filled lump), extra bone, unusual veins, or the extra anconeus epitrochlearis muscle can crowd the nerve [S1].
- **Nerve slipping:** in some people the nerve slips out of its groove when the elbow bends [S1].

Treatment for cubital tunnel syndrome often starts with rest, splints, medicines, and physical therapy, and surgery can free the nerve, either by opening the tunnel (decompression) or by moving the nerve to the front of the elbow (transposition) [S1][S3]. Ultrasound can show the nerve in the tunnel and check whether it stays in place as the elbow bends [S1].

## Common Misunderstandings
- **Myth:** The cubital tunnel is the same as the carpal tunnel. **Fact:** The cubital tunnel is at the elbow and carries the ulnar nerve; nerve trouble here is a separate problem from carpal tunnel syndrome at the wrist [S2][S3].
- **Myth:** Everyone's cubital tunnel is built the same way. **Fact:** The roof of the tunnel varies, and some people have an extra muscle over it [S1][S4].
- **Myth:** Elbow position does not matter for the nerve. **Fact:** The band over the groove behind the elbow stretches when the elbow bends, and bending can press on or stretch the nerve [S1][S2].

## Questions to Ask Your Doctor
1. Could my elbow position during sleep or work be pressing on the nerve in my cubital tunnel?
2. Would an ultrasound help show what is happening in my cubital tunnel?
3. Does my nerve stay in its groove when I bend my elbow?
4. Would an elbow splint help, and when would surgery to open the tunnel be considered?

## Test Questions
1. Which nerve passes through the cubital tunnel? - The ulnar nerve [S1][S3].
2. Where is the cubital tunnel? - On the inner side of the elbow, just past the medial epicondyle [S1][S2].
3. What forms the roof of the cubital tunnel? - A thick band of tissue joining the two heads of the flexor carpi ulnaris muscle, often called Osborne's ligament [S1][S2].
4. What happens to the band over the groove behind the elbow when the elbow bends? - It stretches, and in some people it gets tight enough to press on the nerve [S1].
5. What is pressure on the ulnar nerve in this tunnel called? - Cubital tunnel syndrome [S3].

## Related Topics
- Read next: Cubital Tunnel Syndrome (KO-HAND-COND-002)
- Tests: Nerve Ultrasound (KO-HAND-DX-005)
- Treatments: Elbow Splinting (KO-HAND-TRT-004), Cubital Tunnel Release (KO-HAND-PROC-003), Ulnar Nerve Transposition (KO-HAND-PROC-004)
- Often confused with: Carpal Tunnel (KO-HAND-ANAT-002)

## References
1. [S1] Frontiers in Neurology. *Ulnar Neuropathy at the Elbow: From Ultrasound Scanning to Treatment.* https://pmc.ncbi.nlm.nih.gov/articles/PMC8160369/ (retrieved 2026-10-26)
2. [S2] Diagnostics. *The Unpredictable Ulnar Nerve—Ulnar Nerve Entrapment from Anatomical, Pathophysiological, and Biopsychosocial Aspects.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10931116/ (retrieved 2026-10-26)
3. [S3] Cureus. *From Conservative Measures to Surgical Interventions, Treatment Approaches for Cubital Tunnel Syndrome: A Comprehensive Review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10823195/ (retrieved 2026-10-26)
4. [S4] International Journal of Pharmaceutical and Clinical Research. *Anatomical Factors Affecting Ulnar Neuropathy.* https://zenodo.org/records/13244629 (retrieved 2026-11-14)
