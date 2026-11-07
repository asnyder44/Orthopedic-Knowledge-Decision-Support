# Starter sources for the first 9 KOs

This file lists trusted web pages for each of the 9 starter topics in `data/registry.csv`.
Use it in the KO Generator, **step 3 (Sources)**. For each source, put the link in **Page link** and click **Fetch**. If Fetch fails, copy the page text yourself and paste it into **Source text**.
Then open **More details** and copy the **Source type**, **Written for**, and **Reuse rules** values from the table. Put "Date seen" in **Page date**.
Each KO needs at least 2 sources that have text. ★ marks the 2 best sources to start with.

**Date checked: 2026-11-01.** I opened every link on that day. "Date seen" is the review or update date shown on the page.

---

## Rules (read first)

> - **public_domain** (US government text, such as MedlinePlus summaries and tests, and NIAMS): you may paste it and fetch it. Still credit the source.
> - **open_license**: follow the license named in Notes.
>   - **CC BY 4.0** (most PMC articles listed here): paste is OK. Credit the authors and the journal.
>   - **CC BY-NC-ND 4.0** (StatPearls): non-commercial use only, no changed versions. Use it for facts only, rewrite everything, and never copy sentences. Treat it like link_and_paraphrase.
>   - **CC BY-SA 4.0** (Wikipedia): use it only as a backup. Rewrite the facts, and check each one in a second source.
> - **link_and_paraphrase** (copyrighted: AAOS OrthoInfo, AAOS guideline, Mayo Clinic, A.D.A.M. pages on MedlinePlus): link to the page and rewrite in your own words. Never copy sentences.
>   The Generator saves the pasted text in a source pack (`data/sources/packs/`). Do not publish packs that hold copyrighted text.
> - **Images** often have their own license. Do not copy images.
> - **Never use PHI** (protected health information). No patient records, case notes, forum posts, or anything that names or describes a real patient.
> - **Do not use these sources** for KOs:
>   - Cleveland Clinic: our catalog marks it restricted.
>   - OpenStax: its books ban use with AI.
>   - Radiopaedia: AI use needs an application and a fee.
> - **Clean the text** before you generate. Delete menus, ads, reference lists, and other topics.

**Fetch tips**
- **NCBI Bookshelf (StatPearls)** shows a "Checking your browser - reCAPTCHA" page to scripts. Fetch still fills the box with that short junk text. Delete it, open the page in your browser, and paste the text by hand.
- **PMC articles** fetch well, but they are long. Keep only the parts about your topic.
- **PDFs** cannot be fetched. For the AAOS guideline, use the OrthoGuidelines web page instead.
- **OrthoInfo** sometimes returns error 520. Wait and try again.
- **Mayo Clinic**: the carpal tunnel pages fetch well. The test and procedure pages (for example, Cortisone shots) return no text. Copy those by hand.
- **NINDS**: the carpal tunnel page now sends you to an archived copy, and it blocks scripts (error 403). It is not listed below.
- **ASSH HandCare** pages need JavaScript, so Fetch gets no text. They are not listed below.

---

## KO-HAND-COND-001 Carpal Tunnel Syndrome

| # | Source (title) | Publisher | URL | source_type | permitted_use | Readers | Date seen | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 ★ | Carpal Tunnel Syndrome | MedlinePlus (National Library of Medicine) | https://medlineplus.gov/carpaltunnelsyndrome.html | government_health_page | public_domain | patient | Last updated 2024-01-10 | Fetch works. Use the "Summary" part. The rest of the page is a list of links. |
| 2 ★ | Carpal Tunnel Syndrome: Pathophysiology and Comprehensive Guidelines for Clinical Evaluation and Treatment (Joshi et al.) | Cureus, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC9389835/ | journal_article | open_license | clinician | 2022 (accepted 2022-07-20) | CC BY. Review article: cause, exam tests, and treatment. One figure is CC BY-NC, so do not copy figures. |
| 3 | Carpal Tunnel Syndrome (Overview, Symptoms, & Causes) | NIAMS (NIH) | https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome | government_health_page | public_domain | patient | Last reviewed December 2023 | Fetch works. Also add its second page, "Diagnosis, Treatment, and Steps to Take" (see Carpal Tunnel Release). |
| 4 | Carpal Tunnel Syndrome (Sevy, Sina, Varacallo), StatPearls | StatPearls Publishing, via NCBI Bookshelf | https://www.ncbi.nlm.nih.gov/books/NBK448179/ | textbook | open_license | clinician, student | Last update 2023-10-29 | CC BY-NC-ND 4.0. Fetch is blocked (reCAPTCHA), so paste by hand. |
| 5 | Management of Carpal Tunnel Syndrome (2024) clinical practice guideline | AAOS, on OrthoGuidelines | https://www.orthoguidelines.org/topic?id=1048&tab=all_guidelines | guideline | link_and_paraphrase | clinician | Published 2024-05-18 | Fetch works (long). Put each recommendation's strength in **Evidence strength**. The full PDF is at aaos.org, but it cannot be fetched. |

Also good (copyrighted, link_and_paraphrase): AAOS OrthoInfo, "Carpal Tunnel Syndrome", https://www.orthoinfo.org/en/diseases--conditions/carpal-tunnel-syndrome/ (patient; no review date shown).

---

## KO-HAND-ANAT-001 Median Nerve

| # | Source (title) | Publisher | URL | source_type | permitted_use | Readers | Date seen | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 ★ | Carpal Tunnel Syndrome (Overview) | NIAMS (NIH) | https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome | government_health_page | public_domain | patient | Last reviewed December 2023 | Says where the median nerve runs, which fingers it gives feeling to, and which thumb muscles it controls. |
| 2 ★ | Anatomy, Shoulder and Upper Limb, Median Nerve (Murphy, Ryan, Fakoya), StatPearls | StatPearls Publishing, via NCBI Bookshelf | https://www.ncbi.nlm.nih.gov/books/NBK448084/ | textbook | open_license | clinician, student | Last update 2025-12-01 | CC BY-NC-ND 4.0. The best full anatomy text in this list. Paste by hand (reCAPTCHA). |
| 3 | Carpal Tunnel Syndrome (Summary) | MedlinePlus (National Library of Medicine) | https://medlineplus.gov/carpaltunnelsyndrome.html | government_health_page | public_domain | patient | Last updated 2024-01-10 | Short plain-language text on the nerve's path and job. |
| 4 | The Prevalence of Anatomical Variations of the Median Nerve in the Carpal Tunnel: A Systematic Review and Meta-Analysis (Henry et al.) | PLoS One, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC4549253/ | systematic_review | open_license | clinician | 2015 | CC BY. Good for an advanced "variations" section. Very long, so trim it. |
| 5 | Median nerve | Wikipedia | https://en.wikipedia.org/wiki/Median_nerve | other | open_license | student | Last edited 2026-07-25 | CC BY-SA 4.0. Backup only. Check each fact in another source. |

Also good: StatPearls "Median Nerve Injury", https://www.ncbi.nlm.nih.gov/books/NBK553109/ (last update 2025-07-07, CC BY-NC-ND 4.0).

---

## KO-HAND-ANAT-002 Carpal Tunnel

| # | Source (title) | Publisher | URL | source_type | permitted_use | Readers | Date seen | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 ★ | Carpal Tunnel Syndrome (Summary) | MedlinePlus (National Library of Medicine) | https://medlineplus.gov/carpaltunnelsyndrome.html | government_health_page | public_domain | patient | Last updated 2024-01-10 | Defines the carpal tunnel: bones, ligament, nerve, and tendons. |
| 2 ★ | Clinical-applied anatomy of the carpal tunnel regarding mini-invasive carpal tunnel release (Kaiser et al.) | Archives of Orthopaedic and Trauma Surgery, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC11582268/ | journal_article | open_license | clinician | 2024 (accepted 2024-09-05) | CC BY 4.0. Detailed tunnel anatomy. Also useful for Carpal Tunnel Release. |
| 3 | Carpal Tunnel Syndrome (Overview) | NIAMS (NIH) | https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome | government_health_page | public_domain | patient | Last reviewed December 2023 | Says the tunnel is "a narrow, rigid tube of ligament and bones". |
| 4 | Anatomy, Shoulder and Upper Limb, Wrist Flexor Retinaculum (Deak, Black, Bordoni), StatPearls | StatPearls Publishing, via NCBI Bookshelf | https://www.ncbi.nlm.nih.gov/books/NBK545198/ | textbook | open_license | clinician, student | Last update 2023-10-24 | CC BY-NC-ND 4.0. The ligament that forms the tunnel's roof. Paste by hand. |
| 5 | Carpal tunnel | Wikipedia | https://en.wikipedia.org/wiki/Carpal_tunnel | other | open_license | student | Last edited 2026-02-04 | CC BY-SA 4.0. Backup only. |

---

## KO-HAND-COND-002 Cubital Tunnel Syndrome

| # | Source (title) | Publisher | URL | source_type | permitted_use | Readers | Date seen | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 ★ | Ulnar Neuropathy at the Elbow: From Ultrasound Scanning to Treatment (Mezian et al.) | Frontiers in Neurology, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC8160369/ | journal_article | open_license | clinician | 2021 (accepted 2021-03-23) | CC BY. Covers causes, tests, splints, injections, and surgery. Very long, so trim it. |
| 2 ★ | Ulnar Nerve Entrapment at the Elbow (Cubital Tunnel Syndrome) | AAOS OrthoInfo | https://www.orthoinfo.org/en/diseases--conditions/ulnar-nerve-entrapment-at-the-elbow/ | patient_education | link_and_paraphrase | patient | No review date shown | Copyrighted. Rewrite only. Fetch works. |
| 3 | Surgical Approaches and Their Outcomes in the Treatment of Cubital Tunnel Syndrome (Carlton, Khalid) | Frontiers in Surgery, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC6071516/ | journal_article | open_license | clinician | 2018 (accepted 2018-07-05) | CC BY. Surgery options. |
| 4 | Ulnar Nerve Entrapment (Davis, Kane), StatPearls | StatPearls Publishing, via NCBI Bookshelf | https://www.ncbi.nlm.nih.gov/books/NBK555929/ | textbook | open_license | clinician, student | Last update 2023-08-07 | CC BY-NC-ND 4.0. Covers the elbow (cubital tunnel) and the wrist (Guyon canal). Paste by hand. |
| 5 | Ulnar nerve dysfunction | A.D.A.M., on MedlinePlus Medical Encyclopedia | https://medlineplus.gov/ency/article/000789.htm | patient_education | link_and_paraphrase | patient | Review date 2026-05-04 | Copyrighted (A.D.A.M.), even though it is on a .gov site. Rewrite only. |

Also good: AAOS OrthoInfo "Cubital Tunnel Release", https://www.orthoinfo.org/en/treatment/cubital-tunnel-release/ (patient, copyrighted).

---

## KO-HAND-DX-001 Nerve Conduction Study

| # | Source (title) | Publisher | URL | source_type | permitted_use | Readers | Date seen | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 ★ | Electromyography (EMG) and Nerve Conduction Studies | MedlinePlus Medical Tests (National Library of Medicine) | https://medlineplus.gov/lab-tests/electromyography-emg-and-nerve-conduction-studies/ | government_health_page | public_domain | patient | Last updated 2024-04-10 | Fetch works. What the tests are, why they are done, what happens, and what results mean. |
| 2 ★ | Electrodiagnostic Studies in the Surgical Treatment of Carpal Tunnel Syndrome: A Systematic Review (Osiak et al.) | Journal of Clinical Medicine, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC8235020/ | systematic_review | open_license | clinician | 2021 (accepted 2021-06-17) | CC BY. How nerve tests are used for carpal tunnel. |
| 3 | Nerve Conduction Studies and Electromyography (Ramani, Lui, Arya), StatPearls | StatPearls Publishing, via NCBI Bookshelf | https://www.ncbi.nlm.nih.gov/books/NBK611987/ | textbook | open_license | clinician, student | Last update 2025-02-10 | CC BY-NC-ND 4.0. A full general chapter. Paste by hand. |
| 4 | Electrodiagnostic Evaluation of Carpal Tunnel Syndrome (Rosario, Dokukin, De Jesus), StatPearls | StatPearls Publishing, via NCBI Bookshelf | https://www.ncbi.nlm.nih.gov/books/NBK562235/ | textbook | open_license | clinician | Last update 2023-08-23 | CC BY-NC-ND 4.0. Test findings in carpal tunnel. Paste by hand. |
| 5 | Electrodiagnostic Testing | AAOS OrthoInfo | https://www.orthoinfo.org/en/treatment/electrodiagnostic-testing/ | patient_education | link_and_paraphrase | patient | No review date shown | Copyrighted. Rewrite only. Fetch works. |

Also good: A.D.A.M. "Nerve conduction velocity", https://medlineplus.gov/ency/article/003927.htm (review date 2025-04-16, copyrighted).

---

## KO-HAND-DX-002 Phalen's Test

| # | Source (title) | Publisher | URL | source_type | permitted_use | Readers | Date seen | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 ★ | Correlations of Tinel and Phalen Signs with Nerve Conduction Study Test Results in a Randomly Chosen Population of Patients with Carpal Tunnel Syndrome (Kaczmarek et al.) | NeuroSci, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC12550957/ | journal_article | open_license | clinician | 2025 (accepted 2025-09-25) | CC BY. Compares Phalen and Tinel signs with nerve test results. |
| 2 ★ | Carpal Tunnel Syndrome: Pathophysiology and Comprehensive Guidelines for Clinical Evaluation and Treatment (Joshi et al.) | Cureus, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC9389835/ | journal_article | open_license | clinician | 2022 | CC BY. Puts Phalen's test next to other exam tests. |
| 3 | Usefulness of the Phalen Test and the Tinel Sign in the Prognosis and the Impact on Quality of Life of Patients with Carpal Tunnel Syndrome Undergoing Classical Open Carpal Tunnel Release (Pimentel et al.) | Revista Brasileira de Ortopedia, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC10957282/ | journal_article | open_license | clinician | 2024 (accepted 2023-06-26) | CC BY. |
| 4 | Carpal tunnel syndrome | A.D.A.M., on MedlinePlus Medical Encyclopedia | https://medlineplus.gov/ency/article/000433.htm | patient_education | link_and_paraphrase | patient | Review date 2025-06-04 | Copyrighted. Names the Phalen and Tinel tests in plain words. Rewrite only. |
| 5 | Phalen maneuver | Wikipedia | https://en.wikipedia.org/wiki/Phalen_maneuver | other | open_license | student | Last edited 2025-10-16 | CC BY-SA 4.0. Backup only. |

Weak spot: no US government page explains this test. Patient-level text is thin.

---

## KO-HAND-PROC-001 Carpal Tunnel Release

| # | Source (title) | Publisher | URL | source_type | permitted_use | Readers | Date seen | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 ★ | Carpal Tunnel Syndrome: Diagnosis, Treatment, and Steps to Take | NIAMS (NIH) | https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome/diagnosis-treatment-and-steps-to-take | government_health_page | public_domain | patient | Last reviewed December 2023 | Fetch works. Has a surgery section (open and endoscopic). |
| 2 ★ | Open versus endoscopic carpal tunnel release: a systematic review and meta-analysis of randomized controlled trials (Li et al.) | BMC Musculoskeletal Disorders, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC7187537/ | systematic_review | open_license | clinician | 2020 (accepted 2020-04-21) | CC BY 4.0. Compares the two surgery types. |
| 3 | Carpal tunnel release | A.D.A.M., on MedlinePlus Medical Encyclopedia | https://medlineplus.gov/ency/article/002976.htm | patient_education | link_and_paraphrase | patient | Review date 2025-06-04 | Copyrighted. Before, during, and after surgery. Rewrite only. |
| 4 | Management of Carpal Tunnel Syndrome (2024) clinical practice guideline | AAOS, on OrthoGuidelines | https://www.orthoguidelines.org/topic?id=1048&tab=all_guidelines | guideline | link_and_paraphrase | clinician | Published 2024-05-18 | Surgery recommendations with evidence strength. |
| 5 | Carpal Tunnel Syndrome (surgery section) | AAOS OrthoInfo | https://www.orthoinfo.org/en/diseases--conditions/carpal-tunnel-syndrome/ | patient_education | link_and_paraphrase | patient | No review date shown | Copyrighted. Rewrite only. |

---

## KO-HAND-TRT-001 Wrist Splinting

| # | Source (title) | Publisher | URL | source_type | permitted_use | Readers | Date seen | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 ★ | Carpal Tunnel Syndrome: Diagnosis, Treatment, and Steps to Take | NIAMS (NIH) | https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome/diagnosis-treatment-and-steps-to-take | government_health_page | public_domain | patient | Last reviewed December 2023 | Says a night splint on the hand and wrist is a common first treatment. |
| 2 ★ | The clinical and cost-effectiveness of corticosteroid injection versus night splints for carpal tunnel syndrome (INSTINCTS trial) (Chesterton et al.) | The Lancet, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC6196880/ | journal_article | open_license | clinician | 2018 | CC BY 4.0. A large trial of splints versus injection. Also use it for Corticosteroid Injection. |
| 3 | Update on Efficacy of Conservative Treatments for Carpal Tunnel Syndrome (Karjalanen et al.) | Journal of Clinical Medicine, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC8877380/ | journal_article | open_license | clinician | 2022 (accepted 2022-02-09) | CC BY. Evidence for splints and other non-surgery care. |
| 4 | Wrist Splint (Howell, Bechmann, Underwood), StatPearls | StatPearls Publishing, via NCBI Bookshelf | https://www.ncbi.nlm.nih.gov/books/NBK557630/ | textbook | open_license | clinician, student | Last update 2023-08-08 | CC BY-NC-ND 4.0. General wrist splints, not only for carpal tunnel. Paste by hand. |
| 5 | Carpal Tunnel Syndrome (bracing section) | AAOS OrthoInfo | https://www.orthoinfo.org/en/diseases--conditions/carpal-tunnel-syndrome/ | patient_education | link_and_paraphrase | patient | No review date shown | Copyrighted. Rewrite only. |

Also good: AAOS OrthoInfo "Care of Casts and Splints", https://www.orthoinfo.org/en/recovery/care-of-casts-and-splints/ (general splint care, copyrighted). The AAOS guideline (see Carpal Tunnel Syndrome) has a bracing recommendation.

---

## KO-HAND-TRT-002 Corticosteroid Injection

| # | Source (title) | Publisher | URL | source_type | permitted_use | Readers | Date seen | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 ★ | Carpal Tunnel Syndrome: Diagnosis, Treatment, and Steps to Take | NIAMS (NIH) | https://www.niams.nih.gov/health-topics/carpal-tunnel-syndrome/diagnosis-treatment-and-steps-to-take | government_health_page | public_domain | patient | Last reviewed December 2023 | Says a steroid shot into the carpal tunnel can ease symptoms for a while. It is short on this topic. |
| 2 ★ | Local Corticosteroid Injection in Hand Surgery: A Review of Molecular Mechanisms, Steroid Selection, and Clinical Outcomes (Patel, Alkadaa, Franco) | Cureus, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC13717673/ | journal_article | open_license | clinician | 2026 (accepted 2026-09-28) | CC BY 4.0. Hand-focused review: how injections work, which drugs, and results. |
| 3 | Extended Follow-up of Local Steroid Injection for Carpal Tunnel Syndrome: A Randomized Clinical Trial (Hofer, Ranstam, Atroshi) | JAMA Network Open, via PubMed Central | https://pmc.ncbi.nlm.nih.gov/articles/PMC8536954/ | journal_article | open_license | clinician | Published 2021-10-22 | CC BY. A trial with long-term results of one steroid shot. |
| 4 | Cortisone Shot (Steroid Injection) | AAOS OrthoInfo | https://www.orthoinfo.org/en/treatment/cortisone-shot-steroid-injection/ | patient_education | link_and_paraphrase | patient | No review date shown | Copyrighted. Rewrite only. It sometimes gives error 520, so retry. |
| 5 | Steroid injections - tendon, bursa, joint | A.D.A.M., on MedlinePlus Medical Encyclopedia | https://medlineplus.gov/ency/article/007678.htm | patient_education | link_and_paraphrase | patient | Review date 2026-06-27 | Copyrighted. Why it is done, risks, and aftercare. Rewrite only. |

Also good: the INSTINCTS trial (see Wrist Splinting), and Mayo Clinic "Cortisone shots", https://www.mayoclinic.org/tests-procedures/cortisone-shots/about/pac-20384794 (copyrighted; Fetch gets no text).
Weak spot: there is no public-domain patient page just about steroid shots in the hand.

---

## Suggested order

1. **Carpal Tunnel Syndrome** (KO-HAND-COND-001). Most other topics link to it, and it has the best sources.
2. **Median Nerve** (KO-HAND-ANAT-001) and **Carpal Tunnel** (KO-HAND-ANAT-002). They are the anatomy behind CTS and reuse the same MedlinePlus and NIAMS pages.
3. **Nerve Conduction Study** (KO-HAND-DX-001). It has a strong public-domain test page.
4. **Wrist Splinting** (KO-HAND-TRT-001), then **Corticosteroid Injection** (KO-HAND-TRT-002). They share the NIAMS page and the INSTINCTS trial.
5. **Carpal Tunnel Release** (KO-HAND-PROC-001).
6. **Phalen's Test** (KO-HAND-DX-002). It has weaker patient sources, so take extra care.
7. **Cubital Tunnel Syndrome** (KO-HAND-COND-002). Do it last so it can contrast with CTS. It has no US government page.
