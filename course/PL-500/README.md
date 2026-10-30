# Microsoft Exam PL-500: Microsoft Power Automate RPA Developer — Udemy Practice-Test Course (`6 × 100 = 600` Questions)

Complete, production-ready Udemy practice-test course package for **Microsoft Exam PL-500: Microsoft Power Automate RPA Developer** (*Microsoft Certified: Power Automate RPA Developer Associate*), aligned to the final published **July 8, 2024** official Microsoft Learn study guide (`3` functional groups · `42` skills).

> **Official Lifecycle & Retirement Disclosure (Verified October 30, 2026):** Microsoft **retired Exam PL-500, its `Power Automate RPA Developer Associate` certification, renewal assessment, and courseware `PL-500T00` on June 30, 2026** (`11:59 PM CST`) with **no direct 1:1 replacement RPA exam or certification** (broader Business Applications developer and AI skilling shifted toward **Exams AB-400 / AB-410** and Power Automate **Applied Skills**). This 600-question repository preserves the complete final **July 8, 2024** PL-500 RPA Developer blueprint for production Power Automate engineering, RPA Center of Excellence (CoE) governance benchmarks, and technical interviews.

---

## Package Snapshot

| Metric | Value |
|---|---|
| **Exam Blueprint Baseline** | Official Microsoft Learn `PL-500` Study Guide (`July 8, 2024` final update) |
| **Practice Exams** | **6 full-length exams × 100 questions = 600 unique questions** |
| **Domain Weighting per Exam** | D1 *Design automations* `28` (`25–30%`) · D2 *Develop automations* `48` (`45–50%`) · D3 *Deploy and manage automations* `24` (`20–25%`) |
| **Udemy Question Types per Exam** | `84` `multiple-choice` (`76` single-answer + `8` four-step `→` sequence items, balanced `21 A / 21 B / 21 C / 21 D`) + `16` `multi-select` (`13` Select-2 + `3` Select-3) |
| **Code / Selector / Expression (`____`) Items** | `16–19` per exam (`104` total across 6 exams) |
| **`Proposed solution:` Evaluations** | `6–7` per exam (`38` total across 6 exams) |
| **Companion Case Studies** | `24` original 3-question RPA Developer case studies (`4` per exam = `12` case items/exam, `72` total) |
| **Importable CSV Deliverables** | `13` UTF-8 BOM 17-column CSVs (`practice-set-{1..6}.csv`, `case-embedded-set-{1..6}.csv`, `05-sample-upload/case-study-sample.csv`) |
| **Max Stem Pairwise Jaccard** | `0.5556` across all `600` stems (`148/148` option terms exercised) |
| **Release Archive** | `PL-500-6x100.zip` |

---

## Directory Layout

```text
course/PL-500/
├── README.md                                   # Course overview, lifecycle notice, & build commands
├── PL-500-6x100.zip                            # Deterministic instructor release archive
├── 01-landing-page/
│   └── landing-page.md                         # Udemy metadata (Fields 1–6), 6 exam descriptions, Welcome & Congrats messages
├── 02-curriculum/
│   └── curriculum-outline.md                   # 6-exam curriculum map, 42-skill matrix, & study workflow
├── 03-practice-sets/
│   └── set-{1..6}/
│       ├── README.md                           # Per-exam blueprint stats & upload options
│       ├── practice-set-{1..6}.csv             # Option A: Standard 100-question Udemy CSV
│       ├── case-embedded-set-{1..6}.csv        # Option B: Self-contained case-embedded CSV (Recommended)
│       └── practice-set-{1..6}.md              # Reviewer & self-study answer key with Microsoft Learn links
├── 04-resources/
│   ├── bank.py                                 # 42-skill blueprint constants & pipe-delimited loader
│   ├── cases.py                                # 24 original RPA Developer case-study scenarios
│   ├── sequences.py                            # 32 four-step ordered sequence options (8 groups x 4)
│   ├── sources.py                              # Official Microsoft Learn documentation URLs per skill
│   ├── terms.py                                # 148 canonical RPA Developer options & distractor rationales
│   ├── build.py                                # Deterministic CSV, Markdown key, & manifest generator
│   ├── validate.py                             # Bank, CSV, slot-balance, banned-phrase, & Jaccard validator
│   ├── package.py                              # Deterministic ZIP packager (PL-500-6x100.zip)
│   ├── test_course.py                          # 8-test end-to-end unittest suite (incl. cross-course zero overlap)
│   ├── questions/{1..6}.txt                    # 600 authored PL-500 question records
│   ├── SUMMARY.md                              # Generated per-exam verification table
│   ├── case-studies.md                         # Generated 24-vignette companion booklet
│   ├── csv-format-spec.md                      # 17-column Udemy CSV import specification
│   ├── case-study-upload-guide.md              # Option A vs Option B Udemy case-study upload instructions
│   ├── sources-and-coverage.md                 # Official Microsoft Learn sources & 42-skill traceability
│   ├── publication-checklist.md                # Pre-publish QA & Udemy instructor checklist
│   ├── answer-manifest.json                    # Machine-readable answer key & metadata manifest
│   └── validation-report.json                  # Automated QA validation report
└── 05-sample-upload/
    ├── README.md                               # Quick-test 12-question Udemy sandbox import guide
    └── case-study-sample.csv                   # 12 case-embedded items from Exam 1 for dry-run testing
```

---

## Reproducible Build, Validation & Test Commands

Run from the repository root (`/home/user/Cert`):

```bash
# 1. Deterministically rebuild all 13 CSVs, 6 Markdown keys, SUMMARY.md, case-studies.md, & manifest
python3 course/PL-500/04-resources/build.py

# 2. Validate 600 items, 13 CSVs, 21/21/21/21 A/B/C/D balance, 148/148 terms, & Jaccard <= 0.72
python3 course/PL-500/04-resources/validate.py --report course/PL-500/04-resources/validation-report.json

# 3. Package deterministic instructor archive PL-500-6x100.zip
python3 course/PL-500/04-resources/package.py

# 4. Run end-to-end course unit tests (including cross-course zero stem overlap)
python3 course/PL-500/04-resources/test_course.py

# 5. Run repository-wide Udemy CSV & landing-page field validators
python3 course/check_csv_upload.py --course PL-500
python3 course/check_landing_page_fields.py course/PL-500/01-landing-page/landing-page.md
```

---

## Independent Educational Disclaimer

Independent educational material authored from official Microsoft Learn documentation. Not affiliated with, endorsed by, or sponsored by Microsoft Corporation or Pearson VUE. Practice test percentages do not correspond to Microsoft's historical `700 / 1000` scaled score.
