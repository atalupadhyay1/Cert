# 📊 Microsoft Exam DP-600 — Practice Test Course Package (`6 × 100 = 600` Questions)

Complete Udemy practice-test course package for **Microsoft Exam DP-600: Implementing Analytics Solutions Using Microsoft Fabric**, awarding the **Microsoft Certified: Fabric Analytics Engineer Associate** credential (Associate-level; no prerequisite certification required).

Aligned 1-to-1 to Microsoft Learn's live **October 19, 2026** DP-600 study guide across **SQL (T-SQL / Spark SQL)**, **KQL**, **DAX**, **PySpark**, **Power Query M**, and **TMDL / TMSL**.

---

## 📦 Key Metrics & Verification Summary

| Metric | Value |
|---|---|
| **Exam Code & Credential** | `DP-600` · `Microsoft Certified: Fabric Analytics Engineer Associate` |
| **Official Study Guide Baseline** | **October 19, 2026** (`learn.microsoft.com/credentials/certifications/resources/study-guides/dp-600`) |
| **Prerequisite Certification** | **None** (Associate-level) |
| **Official Passing Score & Seat Time** | **700 / 1000** scaled score · **100 min** exam time (~**120 min** seat) · **$165 USD** (US) |
| **Practice Sets & Total Questions** | **6 full-length mock exams × 100 questions = 600 original questions** |
| **Domain Weighting (Every Set)** | Domain 1: **26** (`25–30%`) · Domain 2: **47** (`45–50%`) · Domain 3: **27** (`25–30%`) |
| **Skills Mapped** | **41 / 41** official tasks (`1.1`–`1.11`, `2.1`–`2.18`, `3.1`–`3.12`) in every exam |
| **Question Formats (Every Set)** | `76` single-answer + `8` ordered 4-step (`→`) sequences = `84` `multiple-choice` (`21 A / 21 B / 21 C / 21 D`) + `16` `multi-select` (`13` two-answer + `3` three-answer) |
| **Code / Query Completion (`____`)** | **139 items total** (`24, 24, 23, 21, 24, 23` across Sets 1–6) spanning SQL, KQL, DAX, PySpark, Power Query M, and TMDL/TMSL |
| **Proposed Solution Evaluations** | **42 items total** (`7, 8, 8, 7, 6, 6` across Sets 1–6) |
| **Original Enterprise Case Studies** | **24 original non-Microsoft cases** (`4 cases × 3 questions = 12` case items per exam; `72` total) |
| **Vocabulary & Distractor Coverage** | **206 / 206 (`100.0%`)** technical options exercised; **0 unused terms**; max stem Jaccard **`0.6667`** (`<= 0.72` cap) |

---

## 🗂️ Directory Layout

```text
course/DP-600/
├── README.md                                   # Package overview, blueprint summary, and verification commands
├── DP-600-6x100.zip                            # Ready-to-distribute archive of CSVs, Markdown sets, and docs
├── 01-landing-page/
│   └── landing-page.md                         # Complete Udemy metadata (Fields 1–6), 6 exam descriptions, Welcome & Congrats messages
├── 02-curriculum/
│   └── curriculum-outline.md                   # Complete 6-exam curriculum structure, 41-skill matrix, and pacing guide
├── 03-practice-sets/
│   ├── set-1/                                  # Omnichannel Retail (practice-set-1.csv, case-embedded-set-1.csv, practice-set-1.md)
│   ├── set-2/                                  # Healthcare & Clinical IoT
│   ├── set-3/                                  # FinTech & Capital Markets
│   ├── set-4/                                  # Smart Manufacturing & Cold-Chain Logistics
│   ├── set-5/                                  # Subscription Media Streaming & Ad-Tech
│   └── set-6/                                  # Renewable Energy Grids, Telecom & Public Transit
├── 04-resources/
│   ├── questions/{1..6}.txt                    # 600 authored items (100 per exam)
│   ├── terms.py                                # 174 option definitions + 32 SQL/KQL/DAX/PySpark/M/TMDL syntax tokens
│   ├── sequences.py                            # 32 four-step (->) sequence options (8 workflows × 4 orderings)
│   ├── cases.py                                # 24 original enterprise Fabric case studies
│   ├── sources.py                              # Primary learn.microsoft.com URLs for all 41 skills
│   ├── bank.py                                 # Blueprint loader and structural plans
│   ├── build.py                                # Deterministic CSV, Markdown, manifest, and sample generator
│   ├── validate.py                             # 13-CSV + Jaccard + 100%-term-usage + banned-phrase validator
│   ├── package.py                              # Builds DP-600-6x100.zip
│   ├── test_course.py                          # 14-test unittest suite verifying end-to-end course integrity
│   ├── answer-manifest.json                    # Machine-readable answer indices and metadata for all 600 items
│   ├── validation-report.json                  # Full automated QA report
│   ├── case-studies.md                         # Reference compendium of all 24 enterprise case studies
│   ├── csv-format-spec.md                      # 16-column Udemy CSV contract specification
│   ├── case-study-upload-guide.md              # When to upload case-embedded-set-N.csv vs practice-set-N.csv
│   ├── sources-and-coverage.md                 # 41-skill Microsoft Learn bibliography and coverage matrix
│   ├── publication-checklist.md                # Pre-publish QA and Udemy upload steps
│   └── SUMMARY.md                              # Executive architecture & verification summary
└── 05-sample-upload/
    ├── README.md                               # Quick smoke-test upload instructions
    └── case-study-sample.csv                   # 12-question sample CSV (4 embedded cases from Set 1)
```

---

## 🔁 Rebuild, Validate & Test Commands

Run from the repository root (`/home/user/Cert`):

```bash
python3 course/DP-600/04-resources/build.py
python3 course/DP-600/04-resources/validate.py --report course/DP-600/04-resources/validation-report.json
python3 course/DP-600/04-resources/package.py
python3 -m unittest discover -s course/DP-600/04-resources -p 'test_*.py' -v
python3 course/check_csv_upload.py --all
python3 course/check_landing_page_fields.py
```

---

## ⚖️ Scope & Exam Policy Notice

- **Official study guide alignment:** Built from the **October 19, 2026** Microsoft Learn DP-600 study guide (`Maintain a data analytics solution` 25–30%, `Prepare data` 45–50%, `Implement and manage semantic models` 25–30%) across **SQL**, **KQL**, and **DAX**.
- **Scoring & format transparency:** Microsoft's live exam reports a **700 / 1000** criterion-referenced scaled score; raw practice percentages do not translate directly to scaled scores. Interactive drag-and-drop tiles, hot-area dropdowns, multi-tab case study panes, and locked non-returnable Yes/No series are represented as text-complete `multiple-choice` and `multi-select` CSV items.
