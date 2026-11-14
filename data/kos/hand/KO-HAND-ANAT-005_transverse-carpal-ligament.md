---
schema_version: okds-ko-1.0
ko_id: KO-HAND-ANAT-005
title: Transverse Carpal Ligament
preferred_term: Transverse Carpal Ligament
alternate_terms:
- flexor retinaculum
- TCL
- wrist ligament
ko_type: AnatomicalStructure
specialty: HAND
cluster: 1
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: The transverse carpal ligament is a strong band of tissue that stretches across the palm side
  of the wrist and forms the roof of the carpal tunnel [S1][S4]. The median nerve and the tendons that
  bend the fingers pass underneath it [S1]. In carpal tunnel release surgery, this ligament is cut to make
  more room for the nerve [S1][S5].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- wrist
- carpal tunnel
- ligament
- median nerve
- carpal tunnel release
relationships:
- predicate: PART_OF
  target_id: KO-HAND-ANAT-002
  target_label: Carpal Tunnel
  source_ids:
  - S1
  - S4
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-COND-001
  target_label: Carpal Tunnel Syndrome
  source_ids:
  - S1
  - S4
  - S5
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-PROC-001
  target_label: Carpal Tunnel Release
  source_ids:
  - S1
  - S5
- predicate: PREREQUISITE_FOR
  target_id: KO-HAND-ANAT-001
  target_label: Median Nerve
  source_ids:
  - S1
proposed_concepts:
- term: Carpal bones (scaphoid, pisiform, trapezium, hamate)
  suggested_type: AnatomicalStructure
  predicate: PREREQUISITE_FOR
  reason: S3 names these four wrist bones as the ligament's attachment points; no KO for the carpal bones
    exists.
- term: Flexor retinaculum reconstruction
  suggested_type: Procedure
  predicate: PREREQUISITE_FOR
  reason: S5 is a meta-analysis of carpal tunnel release with versus without rebuilding the ligament; not
    in the registry.
- term: Thenar and hypothenar muscles
  suggested_type: AnatomicalStructure
  predicate: PREREQUISITE_FOR
  reason: S4 says the ligament anchors these palm muscles; not in the registry.
sources:
- id: S1
  title: Carpal Tunnel Syndrome
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/carpaltunnelsyndrome.html
  source_type: government_health_page
  audience: patient
  publication_date: '2024-01-10'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:carpaltunnelsyndrome). Licence: Public domain (NLM-authored
    MedlinePlus summary); credit MedlinePlus'
- id: S2
  title: 11.5 Muscles of the Pectoral Girdle and Upper Limbs (Anatomy and Physiology 2e)
  publisher: OpenStax, Rice University
  url: https://openstax.org/books/anatomy-and-physiology-2e/pages/11-5-muscles-of-the-pectoral-girdle-and-upper-limbs
  source_type: textbook
  audience: student
  publication_date: '2022'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (openstax:anatomy-and-physiology-2e:11-5-muscles-of-the-pectoral-girdle-and-upper-limbs).
    Licence: CC BY 4.0 (OpenStax); attribute OpenStax and link to the book'
- id: S3
  title: 'The Transverse Carpal Ligament: Anatomy and Clinical Implications'
  publisher: Georg Thieme Verlag KG
  url: https://doi.org/10.1055/s-0034-1394150
  source_type: journal_article
  audience: clinician
  publication_date: '2014'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via openaire. Licence: Open Access. Type: article. Text kept: abstract only.'
- id: S4
  title: Biomechanical Role of the Transverse Carpal Ligament in Carpal Tunnel Compliance
  publisher: Georg Thieme Verlag KG
  url: https://doi.org/10.1055/s-0034-1394136
  source_type: journal_article
  audience: clinician
  publication_date: '2014'
  retrieved_date: '2026-11-14'
  permitted_use: link_and_paraphrase
  notes: 'Found via openaire. Licence: Open Access. Type: article. Text kept: abstract only.'
- id: S5
  title: Carpal tunnel release with versus without flexor retinaculum reconstruction for carpal tunnel
    syndrome at short- and long-term follow up—A meta-analysis of randomized controlled trials
  publisher: PLoS ONE
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6349326/
  source_type: journal_article
  audience: clinician
  publication_date: '2019'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC6349326). Licence: CC BY'
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
  - The patient source (S1, MedlinePlus) calls it 'the ligament that holds the wrist bones together' and
    'the wrist ligament' without naming it; S5 uses 'transverse carpal ligament' and 'flexor retinaculum'
    as the same structure. Anatomist should confirm the synonym is acceptable for patients.
  - S3 and S4 are abstract-only (Thieme, link_and_paraphrase, licence per article not confirmed); S2 (OpenStax)
    mentions the flexor retinaculum in one sentence only.
  - No condition KO links to it with AFFECTS yet; Carpal Tunnel Syndrome (KO-HAND-COND-001) could add 'AFFECTS
    KO-HAND-ANAT-005' if a source supports it.
  - MeSH ID is not stated in any source; left as verify. ICD-10-CM does not apply to an anatomical structure.
  - Plain-language explanations (e.g., 'proprioception', 'carpal arch') were written by the drafter; check
    they match the sources.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus publishes a new 'last updated' date for its Carpal Tunnel Syndrome page.
- A new review compares carpal tunnel release with and without ligament reconstruction.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
The transverse carpal ligament is a strong band of tissue that stretches across the palm side of the wrist and forms the roof of the carpal tunnel [S1][S4]. The median nerve and the tendons that bend the fingers pass underneath it [S1]. In carpal tunnel release surgery, this ligament is cut to make more room for the nerve [S1][S5].

## Key Facts (claim → source)
- The transverse carpal ligament (TCL), also called the flexor retinaculum, is a band of tough tissue on the palm side of the wrist [S2][S5].
- It forms the palm-side wall, or roof, of the carpal tunnel, a narrow passage between the wrist bones and this ligament [S1][S4].
- It attaches to four wrist bones: the scaphoid and pisiform nearer the forearm, and the trapezium and hamate nearer the fingers [S3].
- Its fibers run mainly across the wrist, and its thickness changes along its length [S3].
- It acts like a pulley for the finger-bending tendons and gives an anchor point to the muscles at the base of the thumb and little finger [S4].
- Carpal tunnel release, the most common surgery for carpal tunnel syndrome, cuts this ligament to relieve pressure on the median nerve [S1][S5].
- After the ligament is cut, the arch of wrist bones becomes more flexible [S4].

## Explanation
### Where it is
The transverse carpal ligament lies across the front (palm side) of the wrist, at the base of the hand [S1][S2]. Fibrous bands called retinacula hold the tendons in place at the wrist, and the flexor retinaculum is the one over the palm side [S2]. Medical studies use the names transverse carpal ligament and flexor retinaculum for the same structure [S5]. The ligament stretches between wrist bones on each side: the scaphoid and pisiform at its upper edge, and the trapezium and hamate at its lower edge [S3]. Together with the wrist bones, it forms the carpal tunnel [S1][S4].

### What it does
- **Forms the roof of the carpal tunnel:** the median nerve and the finger-bending tendons pass through the tunnel under the ligament [S1][S4].
- **Works like a pulley:** it acts as a pulley for the finger-bending tendons [S4].
- **Anchors muscles:** the small muscles at the base of the thumb (thenar muscles) and at the base of the little finger (hypothenar muscles) attach to it [S4].
- **Steadies the wrist bones:** it helps keep the arch of wrist bones stable and also helps the body sense wrist position, which is called proprioception [S4].

Its fibers mostly run straight across the wrist [S3]. Its thickness changes along the path of the median nerve, with the thickest parts at the lower edge on the little-finger side and at the upper edge on the thumb side [S3].

### Conditions that affect it
- **Carpal tunnel syndrome:** when the tendons in the tunnel swell, they can press on the median nerve under the ligament, causing numbness, tingling, weakness, or pain [S1]. High pressure inside the carpal tunnel is thought to be part of the cause [S5].
- **Carpal tunnel release surgery:** a surgeon cuts this ligament to make more room for the nerve [S1][S5]. Recovery may take months, and carpal tunnel syndrome rarely comes back afterward, though mild symptoms may stay [S1]. Possible problems after release include nerve problems, pain at the sides of the palm (pillar pain), and loss of grip strength [S5].
- **Ligament reconstruction:** some surgeons rebuild the ligament during release [S5]. A review of trials found no clear long-term difference in grip strength, symptoms, or complications, but better long-term scores on a hand function scale [S5].

After the ligament is cut, the arch of wrist bones becomes more flexible and gives way more easily to pressure from inside the tunnel [S4].

## Common Misunderstandings
- **Myth:** The transverse carpal ligament and the flexor retinaculum are two different structures. **Fact:** Studies use both names for the same band over the carpal tunnel [S5].
- **Myth:** The ligament is only a cover with no job of its own. **Fact:** It also works as a pulley for tendons, anchors hand muscles, and helps steady the wrist bones [S4].
- **Myth:** Cutting the ligament in surgery changes nothing else in the wrist. **Fact:** After the ligament is cut, the arch of wrist bones becomes more flexible [S4].

## Questions to Ask Your Doctor
1. Where exactly is the transverse carpal ligament in my wrist?
2. If I have carpal tunnel release, how will cutting this ligament affect my grip?
3. What could cause pain at the sides of my palm after surgery?
4. Is rebuilding the ligament something to consider in my case?

## Test Questions
1. What part of the carpal tunnel does the transverse carpal ligament form? - The roof, on the palm side [S1][S4].
2. What is another name for the transverse carpal ligament? - The flexor retinaculum [S5].
3. Name two jobs of the ligament. - Examples: acting as a pulley for tendons, anchoring thumb and little-finger muscles, steadying the wrist bones [S4].
4. Which four wrist bones does it attach to? - The scaphoid, pisiform, trapezium, and hamate [S3].
5. What happens to the ligament in carpal tunnel release? - It is cut to take pressure off the median nerve [S1][S5].

## Related Topics
- Part of: Carpal Tunnel (KO-HAND-ANAT-002)
- Read next: Carpal Tunnel Syndrome (KO-HAND-COND-001), Carpal Tunnel Release (KO-HAND-PROC-001), Median Nerve (KO-HAND-ANAT-001)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Carpal Tunnel Syndrome.* https://medlineplus.gov/carpaltunnelsyndrome.html (retrieved 2026-10-26)
2. [S2] OpenStax, Rice University. *11.5 Muscles of the Pectoral Girdle and Upper Limbs (Anatomy and Physiology 2e).* https://openstax.org/books/anatomy-and-physiology-2e/pages/11-5-muscles-of-the-pectoral-girdle-and-upper-limbs (retrieved 2026-10-26)
3. [S3] Georg Thieme Verlag KG. *The Transverse Carpal Ligament: Anatomy and Clinical Implications.* https://doi.org/10.1055/s-0034-1394150 (retrieved 2026-11-14)
4. [S4] Georg Thieme Verlag KG. *Biomechanical Role of the Transverse Carpal Ligament in Carpal Tunnel Compliance.* https://doi.org/10.1055/s-0034-1394136 (retrieved 2026-11-14)
5. [S5] PLoS ONE. *Carpal tunnel release with versus without flexor retinaculum reconstruction for carpal tunnel syndrome at short- and long-term follow up—A meta-analysis of randomized controlled trials.* https://pmc.ncbi.nlm.nih.gov/articles/PMC6349326/ (retrieved 2026-10-26)
