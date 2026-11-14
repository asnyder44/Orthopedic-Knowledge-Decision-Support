---
schema_version: okds-ko-1.0
ko_id: KO-JOINT-PROC-002
title: Total Hip Arthroplasty
preferred_term: Total Hip Arthroplasty
alternate_terms:
- total hip replacement
- THA
- THR
- hip replacement surgery
- hip arthroplasty
ko_type: Procedure
specialty: JOINT
cluster: 5
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Total hip arthroplasty (total hip replacement) is surgery in which a surgeon removes the damaged parts
  of the hip joint and replaces the ball and socket with artificial parts [S1][S2]. Osteoarthritis is the most
  common reason for it, and it is usually considered when other treatments have not helped enough [S1][S2].
  It is considered the most effective treatment for end-stage hip osteoarthritis [S3].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- hip surgery
- joint replacement
- hip osteoarthritis treatment
- artificial hip
- hip dislocation
- surgical approach
- recovery after surgery
relationships:
- predicate: TREATS
  target_id: KO-JOINT-COND-002
  target_label: Hip Osteoarthritis
  source_ids:
  - S1
  - S2
  - S3
- predicate: TREATS
  target_id: KO-TRAUMA-COND-001
  target_label: Hip Fracture
  source_ids:
  - S2
proposed_concepts:
- term: Hip implant (artificial hip prosthesis)
  suggested_type: Device
  predicate: USES_DEVICE
  reason: S2 describes the metal stem and socket and the metal, ceramic, or plastic bearing surfaces.
- term: Recovery after total hip replacement
  suggested_type: RehabProtocol
  predicate: FOLLOWED_BY
  reason: S2 and S4 mention activity limits and dislocation risk in the first months; a recovery KO would hold
    timing and warning signs.
- term: Hip dislocation after hip replacement
  suggested_type: Condition
  predicate: COMPLICATION_OF
  reason: S1 and S4 name dislocation as the most common problem after THA.
- term: Exercise therapy for hip osteoarthritis
  suggested_type: Treatment
  predicate: ALTERNATIVE_TO
  reason: S1 and S2 list physical therapy and exercise as treatments tried before hip replacement.
- term: Osteonecrosis of the hip
  suggested_type: Condition
  predicate: TREATS
  reason: S2 lists osteonecrosis as a reason for hip replacement.
sources:
- id: S1
  title: Hip Replacement
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/hipreplacement.html
  source_type: government_health_page
  audience: patient
  publication_date: '2025-06-25'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:hipreplacement). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
- id: S2
  title: Hip Replacement Surgery
  publisher: National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH)
  url: https://www.niams.nih.gov/health-topics/hip-replacement-surgery
  source_type: government_health_page
  audience: patient
  publication_date: '2023-08-01'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (niams:hip-replacement-surgery). Licence: Public domain (U.S. federal
    government work, NIH/NIAMS); credit NIAMS'
- id: S3
  title: 'The Direct Anterior Approach to Primary Total Hip Replacement: Radiological Analysis in Comparison
    to Other Approaches'
  publisher: Journal of Clinical Medicine
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8196856/
  source_type: journal_article
  audience: clinician
  publication_date: '2021'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC8196856). Licence: CC BY'
- id: S4
  title: The unstable total hip replacement
  publisher: Indian Journal of Orthopaedics
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2739467/
  source_type: journal_article
  audience: clinician
  publication_date: '2008'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC2739467). Licence: CC BY'
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
  - 'Recovery timeline: the NIAMS text in the pack is cut off before its recovery section, so the KO only states
    what S2 and S4 say about the first weeks and months. Consider adding a hip replacement recovery source.'
  - S4 (2008) is an older review; the 1-3% dislocation figures and risk factors should be checked against newer
    data.
  - S3 is a radiology-focused review of surgical approaches; claims that the anterior approach has faster rehab
    come from studies it cites, with no proven long-term advantage. Clinician should check balance.
  - No implant lifespan figure is in this pack; not stated in the KO.
  - Only 2 relationships could be supported by registry targets; device, rehab, and complication concepts are
    in proposed_concepts.
  - MeSH ID and ICD-10-CM code are unknown and set to <verify>; procedure coding is not in any source.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus or NIAMS shows a new 'last updated' or 'last reviewed' date on a cited hip replacement page.
- A new guideline or large review on total hip arthroplasty approaches or dislocation is published.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Total hip arthroplasty (THA), also called total hip replacement, is surgery in which a surgeon removes the damaged bone and cartilage of the hip joint and replaces them with artificial parts [S1][S2]. Osteoarthritis is the most common reason for it [S1]. It is usually considered when other treatments, such as pain medicine and physical therapy, have not helped enough [S1][S2]. The goals are to relieve pain, help the hip work better, and improve walking [S1][S2].

## Key Facts (claim → source)
- The hip is a ball-and-socket joint where the top of the thighbone (femur) fits into a socket in the pelvis [S2].
- In THA, the surgeon replaces the ball at the top of the thighbone and the surface of the socket with artificial parts [S2].
- Reasons for THA include osteoarthritis, rheumatoid arthritis, osteonecrosis (bone death from poor blood supply), and hip fractures [S2].
- THA is considered the most effective treatment for end-stage hip osteoarthritis [S3].
- Doctors may suggest pain medicine, physical therapy, activity changes, or a cane or walker before surgery [S2].
- Dislocation, when the ball comes out of the socket, is the most common problem after surgery [S1][S4].
- Other risks include blood clots and infection [S1].
- The surgery can be done through different approaches (paths to the joint), and experts still disagree about which is best [S3].

## Explanation
### What it is
The hip joint is one of the largest joints in the body [S2]. It is a ball-and-socket joint: the ball at the top of the thighbone (the femoral head) fits into a socket in the pelvis (the acetabulum) [S2]. In hip replacement, a surgeon removes the diseased parts of the joint and puts in new, artificial parts that work like a normal hip [S2]. THA is considered the most effective treatment for end-stage hip osteoarthritis [S3][S4].

### Why it is done
Hip replacement is for people with severe hip damage [S1]. It is most often done because of [S1][S2]:
- Osteoarthritis, the most common cause [S1][S2].
- Rheumatoid arthritis, a disease where the body's immune system attacks the joints [S2].
- Osteonecrosis, when part of a bone dies because it does not get enough blood [S2].
- A broken hip from a fall or a bone disease [S2].

Before surgery, a provider may suggest other treatments, such as pain medicine, physical therapy and exercise, changing activities to put less strain on the hip, or using a cane, crutch, or walker [S2]. If hip pain still limits daily activities after these, a doctor may recommend surgery [S1][S2]. Hip replacement may not be recommended for people with certain health conditions [S2].

### How it is done
The person receives anesthesia, either regional (numbing one area, often with a light medicine to relax) or general (fully asleep) [S2]. The surgeon makes a cut over the hip and removes the diseased bone and cartilage [S2]. Then the surgeon replaces the ball of the thighbone and the surface of the socket with artificial parts [S2]. Over time, surgeons have learned to use smaller cuts to cause less harm to nearby soft tissues [S2].

Surgeons can reach the hip from different directions, called approaches, such as from the front (direct anterior), the side, or the back (posterior) [S3]. The approach decides which muscles and tendons must be cut or moved [S3]. Some studies claim the front approach leads to faster rehab and less pain, but the benefit is usually seen only for a few months, and long-term superiority has not been proven [S3]. The approach may also affect how the parts are positioned [S3].

### Devices used
The main parts of most hip replacements that fit against the bone, the socket and the stem, are made of metal [S2]. The moving surfaces may be metal, ceramic, or plastic, for example a metal or ceramic ball with a plastic socket lining, or a ceramic ball with a ceramic socket [S2]. Surgeons rarely use metal-on-metal surfaces because of possible complications [S2]. Parts can be attached to bone in different ways [S2]:
- **Cemented:** the parts are fixed to the bone with a special cement [S2].
- **Uncemented:** the parts have a rough or porous surface that bone grows into [S2].
- **Hybrid:** a cemented thighbone part with an uncemented socket part [S2].

### Risks
The most common problem after hip replacement is dislocation, when the ball comes out of the socket [S1][S4]. This can happen because an artificial hip is smaller than the original joint [S1]. Dislocation is usually reported in about 1% to 3% of hip replacements [S4]. The risk is highest in the first few months, but it can happen years later [S4]. Things linked to a higher risk include the surgical approach, the size of the ball, the position of the parts, weak hip muscles, past hip surgery, and conditions that affect the nerves and muscles [S4]. Surgery can also cause blood clots and infections [S1]. Being overweight can raise the risk of problems during or after surgery [S2].

### Recovery timeline
Getting ready starts several weeks before surgery, because being as healthy as possible can help recovery and lower the chance of problems [S2]. Helpful steps include asking about exercises to strengthen the core, upper body, and legs, quitting or cutting back on smoking, and losing weight if needed [S2]. People should plan for help at home with cooking, shopping, and laundry for a week or two after coming home [S2]. Equipment like a raised toilet seat, a shower chair, safety bars, and a walker or crutches can help [S2]. With uncemented parts, activity may be limited for several months while bone grows into the parts [S2]. Good patient education and care after surgery are important to help prevent dislocation [S4]. After a hip replacement, people may need to avoid activities like jogging and high-impact sports [S1]. The sources in this pack do not give a full week-by-week recovery plan; ask the surgical team what to expect.

### Alternatives
Other treatments a provider may suggest before surgery include pain medicine, physical therapy and exercise programs, activity changes to ease strain on the hip, and walking aids such as a cane, crutch, or walker [S1][S2]. Hip replacement is usually considered when these have not helped enough and pain still limits activities [S1][S2].

## Common Misunderstandings
- **Myth:** Hip replacement is only for older people. **Fact:** Better artificial parts now last longer, so hip replacement can also work in younger people than in the past [S2].
- **Myth:** Once the first few weeks pass, dislocation is no longer possible. **Fact:** The risk is highest in the first few months, but dislocation can also happen many years later [S4].
- **Myth:** All hip replacement parts are the same. **Fact:** Parts can be metal, ceramic, or plastic, and can be cemented, uncemented, or hybrid [S2].
- **Myth:** The front (anterior) approach is proven to give better long-term results. **Fact:** Any advantage is usually seen only for a few months, and long-term superiority has not been shown [S3].

## Questions to Ask Your Doctor
1. Have I tried enough non-surgical treatments before choosing surgery?
2. Which surgical approach do you use, and why?
3. What kind of artificial parts and attachment (cemented or uncemented) do you plan to use?
4. What can I do to lower my risk of dislocation after surgery?
5. How should I prepare my home and get ready physically before surgery?
6. Which activities should I avoid after a hip replacement?

## Test Questions
1. What two parts of the hip joint are replaced in THA? - The ball at the top of the thighbone (femoral head) and the surface of the socket (acetabulum) [S2].
2. What is the most common reason for hip replacement? - Osteoarthritis [S1].
3. What is the most common problem after hip replacement? - Dislocation, when the ball comes out of the socket [S1][S4].
4. Name two materials used for the moving surfaces of an artificial hip. - Metal, ceramic, or plastic [S2].
5. What is an uncemented hip replacement? - One with a porous surface that the bone grows into to hold the parts in place [S2].
6. Name two treatments that may be tried before hip replacement. - Examples: pain medicine, physical therapy and exercise, activity changes, or a cane or walker [S2].

## Related Topics
- Treats: Hip Osteoarthritis (KO-JOINT-COND-002), Hip Fracture (KO-TRAUMA-COND-001)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Hip Replacement.* https://medlineplus.gov/hipreplacement.html (retrieved 2026-10-26)
2. [S2] National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIH). *Hip Replacement Surgery.* https://www.niams.nih.gov/health-topics/hip-replacement-surgery (retrieved 2026-10-26)
3. [S3] Journal of Clinical Medicine. *The Direct Anterior Approach to Primary Total Hip Replacement: Radiological Analysis in Comparison to Other Approaches.* https://pmc.ncbi.nlm.nih.gov/articles/PMC8196856/ (retrieved 2026-10-26)
4. [S4] Indian Journal of Orthopaedics. *The unstable total hip replacement.* https://pmc.ncbi.nlm.nih.gov/articles/PMC2739467/ (retrieved 2026-10-26)
