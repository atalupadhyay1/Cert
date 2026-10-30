# 🟣 Microsoft Exam PL-200: Microsoft Power Platform Functional Consultant — Complete Practice Exam Course (`6 × 100 = 600` Questions)

> **Official Lifecycle & Successor Disclosure (Verified October 30, 2026):** Microsoft **retired Exam PL-200 (`Microsoft Certified: Power Platform Functional Consultant Associate`) and its renewal assessment on August 31, 2026** (`11:59 PM CST`; instructor-led courseware `PL-200T00` retired July 31, 2026) and introduced **Exam AB-410: Building Intelligent Applications (`Microsoft Certified: Intelligent Applications Builder Associate`)** as its official replacement. This package preserves the final official **December 26, 2024** Microsoft Learn PL-200 study-guide baseline (`4` domains · `43` granular skills) for Functional Consultant competency benchmarking, enterprise Power Platform solution architecture mastery, and foundational non-AI platform drills alongside `AB-410`.

---

## 📦 Package Snapshot

| Attribute | Value |
|---|---|
| **Exam Code & Title** | `Exam PL-200: Microsoft Power Platform Functional Consultant` |
| **Historical Credential** | `Microsoft Certified: Power Platform Functional Consultant Associate` (`Intermediate` / Associate — **no mandatory prerequisite exam**) |
| **Official Blueprint Baseline** | **December 26, 2024** (`learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-200`) |
| **Lifecycle Status** | **Retired August 31, 2026** → Succeeded by **Exam AB-410** (`Intelligent Applications Builder Associate`) |
| **Practice Question Bank** | **`600` original questions** across **`6` full-length 100-question exams** (`0` duplicate stems; `0` overlap with `PL-900`, `PL-400`, `AZ-204`, `AZ-400`, `AZ-401`, and `DP-600`) |
| **Domain Weighting per Exam** | **Domain 1:** `28` (`28%`, official `25–30%`) · **Domain 2:** `28` (`28%`, official `25–30%`) · **Domain 3:** `27` (`27%`, official `25–30%`) · **Domain 4:** `17` (`17%`, official `15–20%`) |
| **Udemy CSV Question Mix / Exam** | **`84` `multiple-choice`** (`76` single-answer + `8` four-step `→` ordered sequences; exact `21 A / 21 B / 21 C / 21 D` slot balance) + **`16` `multi-select`** (`13` Select-2 + `3` Select-3) |
| **Interactive Approximations / Exam** | `16` Power Fx / WDL / OData / XML completion (`____`) items · `6–7` `Proposed solution:` evaluations · `4` three-question case studies (`12` case items/exam, `24` unique scenarios total) |
| **Upload-Ready CSV Files** | `12` full 100-row CSVs (`practice-set-{1..6}.csv` + `case-embedded-set-{1..6}.csv`) + `1` 12-row `05-sample-upload/case-study-sample.csv` (`UTF-8 BOM`, `LF`, 17 Udemy columns) |
| **Release Archive** | `PL-200-6x100.zip` (built deterministically by `04-resources/package.py`) |

---

## 🗂️ Repository Layout

```text
course/PL-200/
├── README.md                                  # Course overview, retirement notice, blueprint & quickstart
├── PL-200-6x100.zip                           # Deterministic instructor release archive
├── 01-landing-page/
│   └── landing-page.md                        # Complete Udemy metadata (Fields 1-6, 6 Exam Descriptions, Welcome & Congrats)
├── 02-curriculum/
│   └── curriculum-outline.md                  # 4-domain, 43-skill study map + 6-exam industry progression
├── 03-practice-sets/
│   ├── set-1/                                 # Commercial Real Estate & Leasing (100 Q)
│   │   ├── README.md
│   │   ├── practice-set-1.csv                 # Option A: Standard 100-row Udemy CSV (pair with case-studies.md)
│   │   ├── case-embedded-set-1.csv            # Option B: Self-contained 100-row Udemy CSV (Recommended for randomization)
│   │   └── practice-set-1.md                  # Reviewer study key with collapsible rationales & Learn links
│   ├── set-2/                                 # Specialty Healthcare & Clinical Referrals (100 Q)
│   ├── set-3/                                 # Municipal Permitting & Utility Field Operations (100 Q)
│   ├── set-4/                                 # Industrial Manufacturing & Dealer Warranty (100 Q)
│   ├── set-5/                                 # Wealth Advisory & Insurance Underwriting (100 Q)
│   └── set-6/                                 # Higher Education & Global Nonprofit Grants (100 Q)
├── 04-resources/
│   ├── SUMMARY.md                             # Generated 6-exam verification matrix
│   ├── answer-manifest.json                   # Machine-readable answer key & skill traceability
│   ├── validation-report.json                 # Automated validator output (max Jaccard 0.6522)
│   ├── case-studies.md                        # All 24 original Functional Consultant case vignettes
│   ├── csv-format-spec.md                     # 17-column Udemy CSV contract & character limits
│   ├── case-study-upload-guide.md             # Option A vs Option B Udemy case-study upload workflow
│   ├── sources-and-coverage.md                # All 43 official Microsoft Learn links & coverage table
│   ├── publication-checklist.md               # Pre-publish QA & legal/trademark checklist
│   ├── sources.py / cases.py / sequences.py   # Source URLs, 24 case briefs, 32 four-step sequences
│   ├── terms.py / bank.py                     # 117 option/distractor definitions & question loader
│   ├── build.py / validate.py / package.py    # Deterministic builder, validator & ZIP packager
│   ├── test_course.py                         # End-to-end unittest suite (8 test groups)
│   └── questions/{1..6}.txt                   # 600 authored questions (100 per exam)
└── 05-sample-upload/
    ├── README.md                              # Smoke-test upload instructions
    └── case-study-sample.csv                  # 12-row case-embedded Udemy smoke-test CSV
```

---

## 🎯 Six-Exam Industry Progression (`6 × 100 = 600` Questions)

| Exam | Industry Theme | Featured Case Studies (`4 × 3 = 12` Items) | Signature PL-200 Focus |
|---:|---|---|---|
| **Exam 1** | Commercial Real Estate & Leasing | *Harborstone Property Group*, *Crestview Tenant Portals*, *Vanguard Facility Maintenance*, *Oakridge Lease Renewals* | Modernized Matrix BUs, Manual `N:N` Intersects, Power Pages `Account` vs `Contact` Scope, Modern Commanding & Solution Layers |
| **Exam 2** | Specialty Healthcare & Referrals | *Clearpath Specialty Clinics*, *MedBridge Referral Portal*, *Apex Medical Equipment*, *Beacon Clinical Trials* | Dataverse Search Quick Find, 3-Tier Auditing, Multi-Step Form Branching, Embedded Canvas (`ModelDrivenFormIntegration`) & Minimal Sandbox Copy |
| **Exam 3** | Municipal & Utility Permitting | *Rivergate Civic Permits*, *MetroWater Field Operations*, *Greenway Parks & Events*, *Summit Transit Claims* | Access Team Templates, Canvas Delegation (`350k` rows) + `IfError`, WDL `coalesce` & Trigger Conditions, Managed `Upgrade` vs `Update` |
| **Exam 4** | Industrial Manufacturing & Warranty | *Ironclad Heavy Machinery*, *GearGrid Dealer Portal*, *Precision Quality Audits*, *Titan Spare Parts Supply* | Virtual Tables, Alternate Keys, Hierarchy Security (`4` tiers), Cross-Table BPFs, Classic Workflow Logs & Low-Code Power Fx Plug-ins |
| **Exam 5** | Wealth Advisory & Insurance | *Sterling Surety Insurance*, *Kestrel Client Onboarding*, *Pinnacle Claims Resolution*, *Meridian Regulatory Filing* | Custom Cascading (`Assign = Cascade Active`), Form Component Control, Dataverse `Expand Query`, `Compose` vs `Set variable` & Solution Checker |
| **Exam 6** | Higher Education & Global Grants | *Westbrook University Admissions*, *GlobalAid Grant Portal*, *Horizon Alumni Engagement*, *Atlas Field Scholarships* | Custom `Activity` Tables, Entra ID Group Teams, Page Access Control Rules, Dynamic Excel PivotTables, Word XML Templates & SharePoint ACLs |

---

## 🛠️ Build, Validate & Test Commands

Run from `/home/user/Cert`:

```bash
python3 course/PL-200/04-resources/build.py
python3 course/PL-200/04-resources/validate.py --report course/PL-200/04-resources/validation-report.json
python3 course/PL-200/04-resources/package.py
python3 course/PL-200/04-resources/test_course.py
python3 course/check_csv_upload.py --all
python3 course/check_csv_upload.py course/PL-200/05-sample-upload/case-study-sample.csv
python3 course/check_landing_page_fields.py
```

---

## ⚖️ Independent Educational Disclaimer

This practice-test course is independent educational material authored from publicly available Microsoft Learn documentation. It is **not** affiliated with, endorsed by, or sponsored by Microsoft Corporation or Pearson VUE. Zero recalled exam items and zero copyrighted Microsoft sample company names (`Contoso`, `Fabrikam`, `Litware`, `Northwind`, `AdventureWorks`, `Wide World Importers`, `Tailwind Traders`, `VanArsdel`, `Adatum`, `Coho Winery`) appear anywhere in this course. Practice-test percentage scores do not translate to Microsoft’s historical `700 / 1000` scaled score.
