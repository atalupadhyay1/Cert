# Microsoft Exam PL-600: Microsoft Power Platform Solution Architect — Udemy Practice-Test Course (`6 × 100 = 600 Questions`)

Complete, deterministic, upload-ready Udemy practice-test course package for **Microsoft Exam PL-600: Microsoft Power Platform Solution Architect** (`Microsoft Certified: Power Platform Solution Architect Expert`), aligned 1-to-1 to the final official **September 23, 2024** Microsoft Learn study guide (`3` functional groups · `43` skills measured, including **Microsoft Power Platform Well-Architected**).

> **Important Lifecycle, Prerequisite & Successor Disclosure (Verified October 30, 2026):**
> - **Mandatory Historical Prerequisite:** Earning `Microsoft Certified: Power Platform Solution Architect Expert` required passing `PL-600` **plus** holding an active **`PL-200` (`Power Platform Functional Consultant Associate`)** **OR** **`PL-400` (`Power Platform Developer Associate`)** certification.
> - **Retirement & Successor:** Microsoft **retired Exam PL-600, its certification, and renewal assessment on June 30, 2026** (`11:59 PM CST`) and introduced **Exam AB-100: Agentic AI Business Solutions Architect** (`Microsoft Certified: Agentic AI Business Solutions Architect Expert`) as the successor AI-first Business Applications architect certification. This 600-question bank preserves the complete 43-skill PL-600 enterprise architecture benchmark for Solution Architect technical interviews, Architecture Review Boards (`ARBs`), Center of Excellence (`CoE`) governance, and foundational AB-100 readiness.

---

## Package Snapshot

| Metric | Verified Value |
| :--- | :--- |
| **Practice Exams** | `6` full-length practice sets × `100` questions = **`600` unique questions** |
| **Domain 1 (`45–50%`)** | Perform solution envisioning and requirement analysis — **`46` Qs / set (`276` total)** |
| **Domain 2 (`35–40%`)** | Architect a solution — **`37` Qs / set (`222` total)** |
| **Domain 3 (`15–20%`)** | Implement the solution — **`17` Qs / set (`102` total)** |
| **Question Mix / Set** | `76` single-choice (`S`) + `8` ordered 4-step sequences (`O`) + `13` two-answer (`M2`) + `3` three-answer (`M3`) = `84 multiple-choice` + `16 multi-select` |
| **Completion (`____`) Items** | `22–33` per set (**`173` total**) |
| **`Proposed solution:` Items** | `6–7` per set (**`37` total**) |
| **Case Studies** | `4` original 3-question Solution Architect case studies per set (**`24` case studies = `72` case items**) |
| **Canonical Option Library** | `124 / 124` reusable technical options exercised (`100.0%` coverage), max pairwise stem Jaccard `0.513` |
| **Cross-Course Uniqueness** | `0` duplicate stems across all 9 Microsoft courses in the catalog (`PL-900`, `PL-200`, `PL-400`, `PL-500`, `PL-600`, `AZ-204`, `AZ-400`, `AZ-401`, `DP-600`) |

---

## Directory Layout

```text
course/PL-600/
├── README.md                                 # Course overview, lifecycle notice, & quick-start CLI commands
├── PL-600-6x100.zip                          # Deterministic self-contained distribution archive
├── 01-landing-page/
│   └── landing-page.md                       # Complete Udemy publishing copy (Fields 1–6, 6 exam descriptions, Welcome & Congrats)
├── 02-curriculum/
│   ├── curriculum-outline.md                 # 6-exam curriculum structure, 24 case studies, & 43-skill remediation map
│   └── blueprint-alignment.md                # Auto-generated domain/skill/telemetry verification report
├── 03-practice-sets/
│   └── set-{1..6}/
│       ├── practice-set-{1..6}.csv           # Standard 100-row Udemy CSVs (compact Case study — <Name>: prefix)
│       ├── case-embedded-set-{1..6}.csv      # Recommended randomization-safe 100-row Udemy CSVs (inline scenario briefs)
│       ├── practice-set-{1..6}-review.md     # Offline Markdown Reviewer Study Key with <details> explanations
│       └── README.md                         # Per-set blueprint, format, & balanced A–D slot summary
├── 04-resources/
│   ├── sources.py                            # Official Microsoft Learn URLs mapped to all 43 skills
│   ├── cases.py                              # 24 original Solution Architect case-study scenarios
│   ├── sequences.py                          # 32 four-step ordered sequence options (8 groups × 4)
│   ├── terms.py                              # 124 canonical technical options & architect anti-pattern distractors
│   ├── bank.py                               # Blueprint constants & pipe-delimited question loader
│   ├── build.py                              # Deterministic CSV renderer (standard, case-embedded, & sample)
│   ├── validate.py                           # Strict blueprint, CSV, Jaccard, & banned-phrase validator
│   ├── package.py                            # Deterministic zip packager (PL-600-6x100.zip)
│   ├── test_course.py                        # End-to-end unittest suite (including cross-course overlap checks)
│   ├── questions/{1..6}.txt                  # 600 authored Expert-level questions (100 per file)
│   ├── csv-format-spec.md                    # 17-column Udemy CSV contract specification
│   ├── case-study-upload-guide.md            # Standard vs case-embedded upload workflow for randomized tests
│   ├── sources-and-coverage.md               # Official Microsoft Learn bibliography & 43-skill index
│   └── publication-checklist.md              # Pre-upload instructor verification checklist
└── 05-sample-upload/
    ├── README.md                             # 2-minute Udemy smoke-test instructions
    └── case-study-sample.csv                 # 12-row sample CSV (Set 1's four 3-question case studies)
```

---

## Reproducible Build & Validation Commands

Run from the repository root (`/home/user/Cert`):

```bash
# 1. Deterministically rebuild all 13 CSVs
python3 course/PL-600/04-resources/build.py

# 2. Validate all 600 items and regenerate 02-curriculum/blueprint-alignment.md
python3 course/PL-600/04-resources/validate.py --report

# 3. Package PL-600-6x100.zip
python3 course/PL-600/04-resources/package.py

# 4. Run the course unit-test suite and repo-wide Udemy validators
python3 course/PL-600/04-resources/test_course.py
python3 course/check_csv_upload.py --all
python3 course/check_landing_page_fields.py PL-600
```
