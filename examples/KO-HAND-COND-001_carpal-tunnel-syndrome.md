---
schema_version: okds-ko-1.0
ko_id: KO-HAND-COND-001
title: Carpal Tunnel Syndrome
preferred_term: Carpal Tunnel Syndrome
alternate_terms:
- CTS
- median nerve compression at the wrist
ko_type: Condition
specialty: HAND
cluster: 2
audience:
- patient
- caregiver
- student
reading_level: grade 6-8
difficulty: beginner
summary: Carpal tunnel syndrome is a condition where the median nerve is squeezed as it passes through
  a narrow space in the wrist called the carpal tunnel. This can cause numbness, tingling, and weakness
  in the hand [S1][S2].
codes:
  mesh: <verify>
  icd10cm: G56.0-
tags:
- hand numbness
- wrist
- nerve
- tingling fingers
relationships:
- predicate: AFFECTS
  target_id: KO-HAND-ANAT-001
  target_label: Median Nerve
  source_ids:
  - S1
  - S2
- predicate: AFFECTS
  target_id: KO-HAND-ANAT-002
  target_label: Carpal Tunnel
  source_ids:
  - S2
- predicate: DIAGNOSED_BY
  target_id: KO-HAND-DX-001
  target_label: Nerve Conduction Study
  source_ids:
  - S2
  - S3
- predicate: CONTRASTS_WITH
  target_id: KO-HAND-COND-002
  target_label: Cubital Tunnel Syndrome
  source_ids:
  - S3
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-PROC-001
  target_label: Carpal Tunnel Release
  source_ids: []
proposed_concepts: []
sources:
- id: S1
  title: Carpal Tunnel Syndrome
  publisher: National Library of Medicine (MedlinePlus)
  url: https://medlineplus.gov/carpaltunnelsyndrome.html
  source_type: government_health_page
  audience: patient
  publication_date: <verify>
  retrieved_date: '2026-10-24'
  permitted_use: link_and_paraphrase
- id: S2
  title: Carpal Tunnel Syndrome
  publisher: National Institute of Neurological Disorders and Stroke (NIH)
  url: https://www.ninds.nih.gov/health-information/disorders/carpal-tunnel-syndrome
  source_type: government_health_page
  audience: patient
  publication_date: <verify>
  retrieved_date: '2026-10-24'
  permitted_use: <verify>
- id: S3
  title: Carpal Tunnel Syndrome
  publisher: American Academy of Orthopaedic Surgeons (OrthoInfo)
  url: https://orthoinfo.aaos.org/en/diseases--conditions/carpal-tunnel-syndrome/
  source_type: patient_education
  audience: patient
  publication_date: <verify>
  retrieved_date: '2026-10-24'
  permitted_use: link_and_paraphrase
review:
  status: draft
  author: OKDS team (example file)
  generated_by:
    model: null
    prompt_version: okds-template-1.0
  ai_check: null
  team_checker: null
  clinician_reviewer: null
  clinician_role: null
  review_date: null
  open_issues:
  - EXAMPLE FILE for testing the portal. Check every claim against S1-S3 before real use.
  - Verify the MeSH ID and the exact ICD-10-CM code.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-10-24'
last_updated: '2026-10-24'
update_triggers:
- AAOS publishes or updates its carpal tunnel syndrome guideline.
- Any cited page shows a new 'last reviewed' date.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-10-24'
  by: OKDS team
  change: Example KO based on docs/reference/knowledge-object-guide.md section 6.
---

## Summary
Carpal tunnel syndrome (CTS) happens when the median nerve, a nerve that runs from the forearm into the
hand, is squeezed inside the wrist [S1][S2]. People often feel numbness or tingling in the thumb and
first fingers [S2][S3].

## Key Facts (claim → source)
- The median nerve passes through the carpal tunnel, a narrow passage in the wrist [S2].
- Common symptoms are numbness, tingling, and pain in the thumb, index, middle, and part of the ring finger [S2][S3].
- Symptoms are often worse at night [S3].
- Diagnosis usually uses a medical history, a physical exam, and sometimes a nerve conduction study [S2][S3].
- Non-surgical treatments include wrist splinting and corticosteroid injections [S2][S3].
- Surgery (carpal tunnel release) may be an option when symptoms are severe or do not improve [S2][S3].

## Explanation
### What it is
The carpal tunnel is a narrow passage on the palm side of the wrist [S2]. When the median nerve inside
it is pressed, the hand can feel numb or weak [S1][S2].

### Causes and risk factors
Many things can add pressure inside the tunnel, and often there is more than one cause [S2].

### Symptoms
People may feel tingling, numbness, or pain in the thumb and nearby fingers, often at night [S2][S3].
Some people notice a weaker grip [S3].

### How it is diagnosed
A clinician asks about symptoms and examines the hand and wrist [S3]. A nerve conduction study measures
how well the nerve carries signals [S2].

### Treatment options
Treatment often starts without surgery, for example a wrist splint or a steroid injection [S2][S3].
See: Wrist Splinting (KO-HAND-TRT-001), Corticosteroid Injection (KO-HAND-TRT-002), Carpal Tunnel
Release (KO-HAND-PROC-001).

### When to seek care
See a clinician if numbness or tingling in the hand does not go away, or if the hand feels weak [S1][S3].

## Common Misunderstandings
- **Myth:** Only people who type a lot get CTS. **Fact:** Many factors can play a role [S2].
- **Myth:** CTS and cubital tunnel syndrome are the same. **Fact:** They affect different nerves at different places [S3].

## Questions to Ask Your Doctor
1. What tests do I need to confirm carpal tunnel syndrome?
2. Which non-surgical treatments should I try first?
3. When would surgery make sense?

## Test Questions
1. Which nerve is affected in CTS? - The median nerve [S1][S2].
2. Name one non-surgical treatment for CTS. - Wrist splinting or a corticosteroid injection [S2].
3. What test measures how well the nerve carries signals? - A nerve conduction study [S2].

## Related Topics
- Affects: Median Nerve, Carpal Tunnel
- Diagnosed by: Nerve Conduction Study
- Often confused with: Cubital Tunnel Syndrome
- Read next: Carpal Tunnel Release

## References
1. [S1] National Library of Medicine (MedlinePlus). *Carpal Tunnel Syndrome.* https://medlineplus.gov/carpaltunnelsyndrome.html (retrieved 2026-10-24)
2. [S2] National Institute of Neurological Disorders and Stroke (NIH). *Carpal Tunnel Syndrome.* https://www.ninds.nih.gov/health-information/disorders/carpal-tunnel-syndrome (retrieved 2026-10-24)
3. [S3] American Academy of Orthopaedic Surgeons (OrthoInfo). *Carpal Tunnel Syndrome.* https://orthoinfo.aaos.org/en/diseases--conditions/carpal-tunnel-syndrome/ (retrieved 2026-10-24)
