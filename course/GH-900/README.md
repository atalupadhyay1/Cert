# Microsoft / GitHub Exam GH-900: GitHub Foundations — Udemy Practice-Test Course (`6 × 100 = 600` Questions)

Complete, production-ready Udemy Practice Test-Only course package for **Microsoft / GitHub Exam GH-900: GitHub Foundations** (`GitHub Foundations`), aligned strictly to Microsoft Learn's **January 2026** (*Last updated February 19, 2026*) official study guide across **all 7 functional groups** and **all 36 bullet skills (`1.1`–`7.6`)**.

---

## Official Exam GH-900 Snapshot (Verified November 2026)

| Attribute | Official Microsoft / GitHub Specification |
| :--- | :--- |
| **Exam Code & Title** | `Exam GH-900: GitHub Foundations` *(Active — Retirement date: none)* |
| **Credential Awarded** | `GitHub Foundations` *(Beginner / Fundamentals certification — **lifetime credential: never expires and does not require renewal**)* |
| **Prerequisite** | **None** *(designed for developers, PMs, designers, DevOps engineers, security analysts, students, and IT stakeholders)* |
| **Blueprint Baseline** | **January 2026** (*Last updated 02/19/2026*) — `7` functional groups, `36` skills (`28 / 14 / 14 / 14 / 8 / 14 / 8 = 100` items per exam) |
| **Live Exam Format** | **Standalone multiple-choice & multi-select items** · **100 minutes** exam time (`120 minutes` total seat duration) · **Zero case studies (`0`)** and **zero live labs (`0`)** |
| **Open-Book Policy** | **Closed-book** — split-screen **Microsoft Learn access is NOT available** on Fundamentals exams or GitHub exams |
| **Passing Score & Price** | **`700 / 1000`** scaled score (`100–1000` scale — **not** `70%` raw accuracy) · **`$99 USD`** via **Pearson VUE** · `5` languages (`EN`, `ES`, `PT-BR`, `KO`, `JA`) |

---

## Course Architecture & Telemetry (`6 × 100 = 600` Unique Questions)

| Set # | Practice-Test Theme | MC (`S` + `O`) | MS (`M2` + `M3`) | `____` Fills | `Proposed solution:` | Case Studies | Upload CSV |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | Product Engineering & Web Platform Teams | `84` (`76` + `8`) | `16` (`13` + `3`) | `21` | `7` | `0` | `03-practice-sets/set-1/practice-set-1.csv` |
| **2** | Design, Documentation & Developer Advocacy | `84` (`76` + `8`) | `16` (`13` + `3`) | `21` | `6` | `0` | `03-practice-sets/set-2/practice-set-2.csv` |
| **3** | Cloud SaaS & Platform Engineering | `84` (`76` + `8`) | `16` (`13` + `3`) | `21` | `6` | `0` | `03-practice-sets/set-3/practice-set-3.csv` |
| **4** | Agile Product Management & Release Operations | `84` (`76` + `8`) | `16` (`13` + `3`) | `20` | `7` | `0` | `03-practice-sets/set-4/practice-set-4.csv` |
| **5** | Regulated FinTech & Enterprise Governance | `84` (`76` + `8`) | `16` (`13` + `3`) | `21` | `6` | `0` | `03-practice-sets/set-5/practice-set-5.csv` |
| **6** | Open-Source Ecosystems & Global Collaboration | `84` (`76` + `8`) | `16` (`13` + `3`) | `20` | `7` | `0` | `03-practice-sets/set-6/practice-set-6.csv` |
| **Total** | **6 Distinct Real-World Organizational Contexts** | **504** | **96** | **124** | **39** | **0** | **6 CSVs + 14-row `sample-upload.csv`** |

- **100% Catalog Coverage:** All `169 / 169` canonical `TERMS` entries exercised (`0` unused keys).
- **Strict Uniqueness:** `600` unique stems (`0` duplicates across GH-900 and `0` overlaps against all `6,600` questions in the 11 sibling Microsoft `6×100` courses); max pairwise stem Jaccard similarity **`0.5263`** (`<= 0.72` gate).
- **Balanced Keying:** Every set's `84` `multiple-choice` items distribute keyed answers **`21 / 21 / 21 / 21`** across slots `1..4`.

---

## Directory Layout

```text
course/GH-900/
├── README.md                                 # Course overview, blueprint snapshot, and build commands
├── GH-900-6x100.zip                          # Distributable instructor archive (CSVs, MDs, landing page, reports)
├── 01-landing-page/
│   └── landing-page.md                       # Complete Udemy publishing copy (Fields 1-6, 6 exam descriptions, Welcome/Congrats)
├── 02-curriculum/
│   ├── curriculum-outline.md                 # 7-domain, 36-skill syllabus & January 2026 blueprint updates
│   └── blueprint-alignment.md                # Auto-verified domain/set telemetry table
├── 03-practice-sets/
│   └── set-{1..6}/
│       ├── practice-set-{1..6}.csv           # 100-question Udemy 17-column bulk-upload CSV (UTF-8 BOM)
│       ├── practice-set-{1..6}.md            # Human-readable instructor review key with full explanations
│       └── README.md                         # Set-specific Udemy upload & timer instructions
├── 04-resources/
│   ├── sources.py                            # 36 official GitHub Docs & Microsoft Learn URLs
│   ├── sequences.py                          # 10 workflow sequence groups (40 ordered 4-step options)
│   ├── terms.py                              # 129 atomic single/multi-select options + distractors (169 total terms)
│   ├── questions/{1..6}.txt                  # 600 authored scenario items (100 per set)
│   ├── bank.py                               # Loader & blueprint quota verifier
│   ├── build.py                              # Deterministic CSV/Markdown/manifest builder
│   ├── make_sample.py                        # 14-row (2 per domain) smoke-test CSV generator
│   ├── validate.py                           # Structural, blueprint, Jaccard & cross-course validator
│   ├── package.py                            # Builds GH-900-6x100.zip cleanly (no __pycache__)
│   ├── test_course.py                        # 6-test unittest suite
│   ├── SUMMARY.md                            # Generated telemetry report
│   ├── answer-manifest.json                  # Machine-readable answer key & option permutation manifest
│   ├── validation-report.json                # Machine-readable validation telemetry
│   ├── csv-format-spec.md                    # 17-column Udemy CSV contract
│   ├── sources-and-coverage.md               # Official 36-skill reference mapping
│   └── publication-checklist.md              # Step-by-step Udemy Instructor launch checklist
└── 05-sample-upload/
    ├── README.md                             # Smoke-test instructions
    └── sample-upload.csv                     # 14-question sample CSV (2 items from each of the 7 domains)
```

---

## Reproducible Build & Verification Commands

Run from `/home/user/Cert`:

```bash
python3 course/GH-900/04-resources/build.py
python3 course/GH-900/04-resources/make_sample.py
python3 course/GH-900/04-resources/validate.py --report
python3 course/GH-900/04-resources/package.py
python3 course/GH-900/04-resources/test_course.py
python3 course/check_csv_upload.py --all
python3 course/check_landing_page_fields.py GH-900
```

> **Disclaimer:** Independent educational practice material authored from official GitHub Docs and Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft or GitHub, and contains zero recalled exam content.
