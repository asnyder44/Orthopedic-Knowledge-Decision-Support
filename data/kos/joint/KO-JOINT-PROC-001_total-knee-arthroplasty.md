---
schema_version: okds-ko-1.0
ko_id: KO-JOINT-PROC-001
title: Total Knee Arthroplasty
preferred_term: Total Knee Arthroplasty
alternate_terms:
- total knee replacement
- TKA
- TKR
- knee replacement surgery
- knee arthroplasty
ko_type: Procedure
specialty: JOINT
cluster: 5
audience:
- patient
- caregiver
reading_level: grade 6-8
difficulty: beginner
summary: Total knee arthroplasty (total knee replacement) is surgery that replaces the damaged surfaces of
  the knee joint with artificial metal and plastic parts [S1]. Knee osteoarthritis is the most common reason
  for it, and it is usually done when other treatments have not helped enough [S1][S2]. The goal is to relieve
  pain and help a person move better [S1][S4].
codes:
  mesh: <verify>
  icd10cm: <verify>
tags:
- knee surgery
- joint replacement
- knee osteoarthritis treatment
- artificial knee
- recovery after surgery
- physical therapy
- chronic postsurgical pain
relationships:
- predicate: TREATS
  target_id: KO-JOINT-COND-001
  target_label: Knee Osteoarthritis
  source_ids:
  - S1
  - S2
  - S4
- predicate: ALTERNATIVE_TO
  target_id: KO-JOINT-TRT-001
  target_label: Exercise Therapy for Knee Osteoarthritis
  source_ids:
  - S1
  - S2
- predicate: CONTRASTS_WITH
  target_id: KO-JOINT-PROC-002
  target_label: Total Hip Arthroplasty
  source_ids:
  - S3
proposed_concepts:
- term: Knee implant (artificial knee prosthesis)
  suggested_type: Device
  predicate: USES_DEVICE
  reason: S1 says metal and plastic parts are attached to the shinbone, thighbone, and kneecap.
- term: Recovery after total knee replacement
  suggested_type: RehabProtocol
  predicate: FOLLOWED_BY
  reason: S1 and S3 describe physical therapy and recovery phases after surgery.
- term: Unicompartmental (partial) knee arthroplasty
  suggested_type: Procedure
  predicate: ALTERNATIVE_TO
  reason: S1, S2, and S4 describe partial knee replacement as an option when OA is limited to one part of the
    knee.
- term: Knee osteotomy
  suggested_type: Procedure
  predicate: ALTERNATIVE_TO
  reason: S2 lists unloading osteotomy as an option for younger, active patients.
- term: Oxford Knee Score
  suggested_type: OutcomeMeasure
  predicate: MEASURED_BY
  reason: S4 uses the Oxford knee score and Knee Society score to compare knee replacement results.
- term: Chronic postsurgical pain
  suggested_type: Condition
  predicate: COMPLICATION_OF
  reason: S3 describes long-lasting pain after TKA as a common complication.
sources:
- id: S1
  title: Knee Replacement
  publisher: MedlinePlus, U.S. National Library of Medicine
  url: https://medlineplus.gov/kneereplacement.html
  source_type: government_health_page
  audience: patient
  publication_date: '2023-12-26'
  retrieved_date: '2026-10-26'
  permitted_use: public_domain
  notes: 'From the OrthoInfo dataset (mplus:kneereplacement). Licence: Public domain (NLM-authored MedlinePlus
    summary); credit MedlinePlus'
- id: S2
  title: Current Surgical Treatment of Knee Osteoarthritis
  publisher: Arthritis
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3200113/
  source_type: journal_article
  audience: clinician
  publication_date: '2011'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC3200113). Licence: CC BY'
- id: S3
  title: 'Mechanisms and Preventative Strategies for Persistent Pain following Knee and Hip Joint Replacement
    Surgery: A Narrative Review'
  publisher: International Journal of Molecular Sciences
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11083264/
  source_type: journal_article
  audience: clinician
  publication_date: '2024'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC11083264). Licence: CC BY'
- id: S4
  title: 'Unicondylar knee replacement versus total knee replacement for the treatment of medial knee osteoarthritis:
    a systematic review and meta-analysis'
  publisher: Archives of Orthopaedic and Trauma Surgery
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8295078/
  source_type: journal_article
  audience: clinician
  publication_date: '2021'
  retrieved_date: '2026-10-26'
  permitted_use: open_license
  notes: 'From the OrthoInfo dataset (pmc:PMC8295078). Licence: CC BY'
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
  - S2 (2011) is an older clinician review; check that its statements about indications and arthroscopy still
    reflect current practice.
  - S3 contains an internal inconsistency (it gives 0.83% and 1.52% as CPSP prevalence, which earlier in the
    same text are joint replacement prevalence figures); the KO uses only the 20.9% (TKA) vs 7.5% (THA) CPSP
    figures. Clinician should confirm.
  - Dissatisfaction rate (17-19%) and implant lifespan (15-20 years) come from S4 and S1; confirm.
  - S4 concludes partial knee replacement should be used instead of TKA for isolated medial OA; this is one
    meta-analysis and is presented as such. Clinician should check balance.
  - No device, rehab, or outcome-measure KO for the knee exists in the registry, so USES_DEVICE, FOLLOWED_BY,
    and MEASURED_BY links are in proposed_concepts only.
  - CONTRASTS_WITH Total Hip Arthroplasty is based on S3 comparing persistent pain after TKA and THA; confirm
    this link is useful.
  - MeSH ID and ICD-10-CM code are unknown and set to <verify>; procedure coding (e.g., ICD-10-PCS/CPT) is
    not in any source.
safety:
  not_medical_advice: true
  scope_note: General education only. Not a diagnosis or treatment plan.
version: 0.1.0
created: '2026-11-14'
last_updated: '2026-11-14'
update_triggers:
- MedlinePlus shows a new 'last updated' date on its Knee Replacement page.
- A new guideline or large review on total knee arthroplasty outcomes or chronic pain after TKA is published.
license: CC-BY-4.0
change_log:
- version: 0.1.0
  date: '2026-11-14'
  by: KO Collector + Claude (Claude Code session)
  change: Initial draft.
---

## Summary
Total knee arthroplasty (TKA), also called total knee replacement, is surgery that replaces the damaged surfaces of the knee joint with new, artificial parts made of metal and plastic [S1]. Knee osteoarthritis is the most common reason for it [S1]. It is usually done when knee pain and trouble with daily tasks have not improved enough with other treatments [S1][S2]. The goal is to relieve pain and help a person move better, though an artificial knee is not the same as a healthy one [S1][S4].

## Key Facts (claim → source)
- In TKA, the surgeon replaces three surfaces: the end of the thighbone, the end of the shinbone, and the back of the kneecap [S1].
- Knee osteoarthritis is the most common reason for knee replacement [S1][S3].
- Treatment of knee OA should start without surgery, and surgery is considered only if symptoms continue [S2].
- X-ray changes alone do not justify surgery; the decision depends on symptoms and how much the knee bothers the person [S1][S2].
- Possible problems include infection, blood clots, heart attack, stroke, nerve damage, and stiff scarring [S1].
- Long-lasting pain after surgery is a known complication and is more common after TKA than after hip replacement [S3].
- Most people who follow recovery instructions return to nearly all normal daily activities within 3 to 6 weeks [S1].
- An artificial knee may loosen or wear out after 15 to 20 years and may need another surgery [S1].

## Explanation
### What it is
Knee replacement surgery replaces parts of the knee joint with new, artificial parts [S1]. A total knee replacement replaces all the damaged parts of the knee, while a partial knee replacement replaces only one part [S1][S4]. TKA is a common and widely used surgery for people with late-stage knee OA [S2][S4]. The number of these surgeries has been rising for years [S3].

### Why it is done
Knee replacement treats conditions that make the knee's cartilage, the smooth tissue that covers the bone ends, wear away [S1]. These include [S1]:
- Knee osteoarthritis, the most common reason [S1].
- Knee damage from other types of arthritis [S1].
- Knee joints that did not form correctly [S1].

A person may need it if knee damage causes severe pain and makes it hard to walk or climb stairs [S1]. It is usually done after other treatments have not helped enough [S1][S2]. Signs of OA on an X-ray are not a reason for surgery by themselves; surgery is considered only when there are real symptoms as well [S2]. The decision depends on a person's overall health and how much the knee bothers them [S1].

### How it is done
The surgeon removes the damaged cartilage and some bone from the surfaces of the knee joint [S1]. Then the surgeon attaches the artificial parts to the bones, which gives the knee new, smooth surfaces [S1].

### Devices used
The artificial knee parts are made of metal and plastic [S1]. In a total knee replacement, they cover the end of the thighbone, the end of the shinbone, and the back of the kneecap [S1].

### Risks
The chance of problems after knee replacement is low, but every surgery has risks [S1]. Possible problems include [S1]:
- Infection.
- Blood clots.
- Heart attack or stroke.
- Nerve damage.
- Scarring that limits how far the knee can bend.

A person's age, general health, and activity level can affect the risk [S1]. Long-lasting pain after surgery, called chronic postsurgical pain, is a known complication [S3]. One study found it in about 21% of people after TKA, compared with about 8% after hip replacement [S3]. Things linked to a higher chance of long-lasting pain include more pain before surgery, anxiety, depression, and poor sleep [S3]. Even though most people do well, one review notes that 17% to 19% of people are not satisfied after TKA [S4].

### Recovery timeline
Some people go home the same day, and others stay in the hospital for a few days [S1]. To help prevent blood clots, people usually take blood thinners and wear special leg coverings for a short time [S1]. A physical therapist teaches exercises to make the knee stronger and help it bend, and doing them regularly is important [S1]. A cane or walker may be needed for several weeks, and driving usually waits several weeks too [S1]. Most people who follow their recovery plan get back to nearly all normal daily activities within 3 to 6 weeks [S1]. Recovery then continues in stages over months, with near-full improvement often reached within about a year [S3].

To protect the new knee, people are advised to stay at a healthy weight, keep active, and choose low-impact activities like walking, biking, and swimming instead of running or jumping [S1]. The artificial parts may become loose or worn after 15 to 20 years, and another surgery may then be needed [S1].

### Alternatives
Knee OA treatment should start without surgery, using options such as physical therapy, bracing, education, weight loss, and joint injections [S2]. Other surgeries include arthroscopy (cleaning out the joint through small cuts), cartilage repair, osteotomy (cutting and realigning a bone to shift weight off the worn part), and partial knee replacement [S2]. Arthroscopic cleaning does not change how OA progresses and is not a routine treatment for knee OA [S2]. Partial knee replacement or osteotomy may be considered when OA is limited to one part of the knee, especially in younger, active people [S2]. One review found that, for OA only on the inner side of the knee, partial replacement gave better function and fewer complications than TKA, with no clear difference in repeat surgery in the first years [S4].

## Common Misunderstandings
- **Myth:** If an X-ray shows knee arthritis, you need a knee replacement. **Fact:** X-ray signs alone do not justify surgery; it is considered only when symptoms are significant and other treatments have not helped enough [S1][S2].
- **Myth:** A new knee is just like a natural knee. **Fact:** Most people move better with less pain, but an artificial knee is not the same as a normal, healthy knee [S1].
- **Myth:** A knee replacement lasts forever. **Fact:** After 15 to 20 years, the parts may become loose or worn and another surgery may be needed [S1].
- **Myth:** Everyone is pain-free after knee replacement. **Fact:** Long-lasting pain after surgery is a known complication of TKA [S3].

## Questions to Ask Your Doctor
1. Have I tried enough non-surgical treatments before thinking about surgery?
2. Would a total or a partial knee replacement fit my knee better?
3. What risks matter most for me, given my health?
4. How long will I likely be in the hospital, and what will physical therapy involve?
5. What can I do before surgery to lower my chance of long-lasting pain?
6. What activities should I avoid with a new knee?

## Test Questions
1. Which three surfaces are replaced in a total knee replacement? - The end of the thighbone, the end of the shinbone, and the back of the kneecap [S1].
2. What is the most common reason for knee replacement? - Knee osteoarthritis [S1].
3. Is an X-ray showing arthritis enough reason for surgery? - No; surgery is considered only when there are significant symptoms as well [S2].
4. Name two possible risks of knee replacement. - Examples: infection, blood clots, nerve damage, or scarring that limits bending [S1].
5. Within what time do most people return to nearly normal daily activities? - About 3 to 6 weeks, if they follow their recovery plan [S1].
6. How long may an artificial knee last before parts wear or loosen? - About 15 to 20 years [S1].

## Related Topics
- Treats: Knee Osteoarthritis (KO-JOINT-COND-001)
- Alternative to: Exercise Therapy for Knee Osteoarthritis (KO-JOINT-TRT-001)
- Contrasts with: Total Hip Arthroplasty (KO-JOINT-PROC-002)

## References
1. [S1] MedlinePlus, U.S. National Library of Medicine. *Knee Replacement.* https://medlineplus.gov/kneereplacement.html (retrieved 2026-10-26)
2. [S2] Arthritis. *Current Surgical Treatment of Knee Osteoarthritis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC3200113/ (retrieved 2026-10-26)
3. [S3] International Journal of Molecular Sciences. *Mechanisms and Preventative Strategies for Persistent Pain following Knee and Hip Joint Replacement Surgery: A Narrative Review.* https://pmc.ncbi.nlm.nih.gov/articles/PMC11083264/ (retrieved 2026-10-26)
4. [S4] Archives of Orthopaedic and Trauma Surgery. *Unicondylar knee replacement versus total knee replacement for the treatment of medial knee osteoarthritis: a systematic review and meta-analysis.* https://pmc.ncbi.nlm.nih.gov/articles/PMC8295078/ (retrieved 2026-10-26)
