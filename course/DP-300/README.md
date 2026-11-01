# 🗄️ Microsoft Exam DP-300 — Practice Test Course Package (`6 × 100 = 600` Questions)

Complete Udemy practice-test course package for **Microsoft Exam DP-300: Administering Microsoft Azure SQL Solutions**, awarding the **Microsoft Certified: Azure Database Administrator Associate** credential (Associate-level; no prerequisite certification required).

Aligned 1-to-1 to Microsoft Learn's live **October 27, 2026** DP-300 study guide across **Azure SQL Database** (Single, Elastic Pools, Serverless, Hyperscale), **Azure SQL Managed Instance** (General Purpose, Next-gen General Purpose, Business Critical), **SQL Server on Azure Virtual Machines** (Windows & Linux), **SQL Server enabled by Azure Arc**, and **SQL database in Microsoft Fabric**, with hands-on syntax depth across **T-SQL**, **Azure PowerShell**, **Azure CLI**, **Bicep**, and **KQL**.

---

## 📦 Key Metrics & Verification Summary

| Metric | Value |
|---|---|
| **Exam Code & Credential** | `DP-300` · `Microsoft Certified: Azure Database Administrator Associate` |
| **Official Study Guide Baseline** | **October 27, 2026** (`learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300`) |
| **Prerequisite Certification** | **None** (Associate-level; annual free online renewal on Microsoft Learn) |
| **Official Passing Score & Seat Time** | **700 / 1000** scaled score · **100 min** non-lab / **120 min** lab-capable exam time · **$165 USD** (US) |
| **Practice Sets & Total Questions** | **6 full-length mock exams × 100 questions = 600 original questions** |
| **Domain Weighting (Every Set)** | D1: **18** (`15–20%`) · D2: **22** (`20–25%`) · D3: **23** (`20–25%`) · D4: **16** (`15–20%`) · D5: **21** (`20–25%`) |
| **Skills Mapped** | **59 / 59** local study-map skills (`1.1`–`1.12`, `2.1`–`2.14`, `3.1`–`3.14`, `4.1`–`4.8`, `5.1`–`5.11`) in every exam |
| **Question Formats (Every Set)** | `76` single-answer + `8` ordered 4-step (`→`) sequences = `84` `multiple-choice` (`21 A / 21 B / 21 C / 21 D`) + `16` `multi-select` (`13` two-answer + `3` three-answer) |
| **Code / Command Completion (`____`)** | **126 items total** (`30, 20, 19, 19, 19, 19` across Sets 1–6) spanning T-SQL, PowerShell, Azure CLI, Bicep, and KQL |
| **Proposed Solution Evaluations** | **40 items total** (`6, 6, 6, 7, 8, 7` across Sets 1–6) |
| **Original Enterprise Case Studies** | **24 original non-Microsoft cases** (`4 cases × 3 questions = 12` case items per exam; `72` total) |
| **Vocabulary & Distractor Coverage** | **187 / 187 (`100.0%`)** technical options exercised; **0 unused terms**; max stem Jaccard **`0.552`** (`<= 0.72` cap) |

---

## 🗂️ Directory Layout

```text
course/DP-300/
├── README.md                                   # Package overview, blueprint summary, and verification commands
├── DP-300-6x100.zip                            # Ready-to-distribute archive of CSVs, Markdown sets, and docs
├── 01-landing-page/
│   └── landing-page.md                         # Complete Udemy metadata (Fields 1–6), 6 exam descriptions, Welcome & Congrats messages
├── 02-curriculum/
│   ├── curriculum-outline.md                   # Complete 6-exam curriculum structure, 59-skill matrix, and pacing guide
│   └── blueprint-alignment.md                  # Auto-generated domain & per-set telemetry table
├── 03-practice-sets/
│   ├── set-1/                                  # Omnichannel E-Commerce (practice-set-1.csv, case-embedded-set-1.csv, practice-set-1.md)
│   ├── set-2/                                  # Healthcare EHR, HIPAA SQL Ledger & SQL Managed Instance
│   ├── set-3/                                  # Global FinTech Payments, VBS Enclaves & Zero-Data-Loss HA/DR
│   ├── set-4/                                  # Smart Manufacturing ERP, SQL Server on Azure VMs & Elastic Jobs
│   ├── set-5/                                  # Multi-Tenant SaaS, Sharded Elastic Pools & Query Store Tuning
│   └── set-6/                                  # Public Transit, Energy Grids, Hybrid Always On & Cloud Backup/Restore
├── 04-resources/
│   ├── questions/{1..6}.txt                    # 600 authored items (100 per exam)
│   ├── terms.py                                # 147 technical option definitions + 40 ordered sequence definitions (187 total)
│   ├── sequences.py                            # 40 four-step (->) sequence options (10 workflows × 4 orderings)
│   ├── cases.py                                # 24 original enterprise Azure SQL case studies
│   ├── sources.py                              # Primary learn.microsoft.com URLs for all 59 skills + Oct 27, 2026 study guide
│   ├── bank.py                                 # Blueprint loader and structural plans
│   ├── build.py                                # Deterministic 17-column CSV, Markdown, manifest, and sample generator
│   ├── validate.py                             # 13-CSV + sibling-6000-stem + Jaccard + 100%-term-usage + banned-phrase validator
│   ├── package.py                              # Builds DP-300-6x100.zip
│   ├── test_course.py                          # 7-test unittest suite verifying end-to-end course & cross-course integrity
│   ├── answer-manifest.json                    # Machine-readable answer indices and metadata for all 600 items
│   ├── validation-report.json                  # Full automated QA telemetry report
│   ├── case-studies.md                         # Reference compendium of all 24 enterprise case studies
│   ├── csv-format-spec.md                      # 17-column Udemy CSV contract specification
│   ├── case-study-upload-guide.md              # When to upload case-embedded-set-N.csv vs practice-set-N.csv
│   ├── sources-and-coverage.md                 # 59-skill Microsoft Learn bibliography and coverage matrix
│   ├── publication-checklist.md                # Pre-publish QA and Udemy upload steps
│   └── SUMMARY.md                              # Executive architecture & verification summary
└── 05-sample-upload/
    ├── README.md                               # Quick smoke-test upload instructions
    └── case-study-sample.csv                   # 12-question sample CSV (4 embedded retail cases from Set 1)
```

---

## 🔁 Rebuild, Validate & Test Commands

Run from the repository root (`/home/user/Cert`):

```bash
python3 course/DP-300/04-resources/build.py
python3 course/DP-300/04-resources/validate.py --report
python3 course/DP-300/04-resources/package.py
python3 -m unittest discover -s course/DP-300/04-resources -p 'test_*.py' -v
python3 course/check_csv_upload.py --all
python3 course/check_landing_page_fields.py
```

---

## ⚖️ Scope, Tooling Lifecycle & Exam Policy Notice

- **Official study guide alignment:** Built from the **October 27, 2026** Microsoft Learn DP-300 study guide (`Plan and implement data platform resources` 15–20%, `Implement a secure environment` 20–25%, `Monitor, configure, and optimize database resources` 20–25%, `Configure and manage automation of tasks` 15–20%, `Plan and configure a high availability and disaster recovery (HA/DR) environment` 20–25%).
- **Current Microsoft SQL lifecycle coverage:** Reflects **DMA retirement (July 2025)** in favor of **Azure Migrate** and **Azure SQL Migration extension**, **`database watcher` (preview) freeze/retirement roadmap (`Nov 9, 2026` / `Apr 30, 2027`)** transitioning to **Database Hub in Microsoft Fabric**, **SQL database in Microsoft Fabric**, and **SQL Server enabled by Azure Arc**.
- **Scoring & format transparency:** Microsoft's live exam reports a **700 / 1000** criterion-referenced scaled score; raw practice percentages do not translate directly to scaled scores. Interactive drag-and-drop tiles, hot-area dropdowns, multi-tab case study panes, live labs, and locked non-returnable Yes/No series are represented as text-complete `multiple-choice` and `multi-select` CSV items.
