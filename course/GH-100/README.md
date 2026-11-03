# 🐙 Microsoft / GitHub Exam GH-100: GitHub Enterprise Administrator (`GitHub Administration`)

Complete **6 × 100 = 600-question** Udemy practice-test course for **Microsoft / GitHub Exam GH-100: GitHub Enterprise Administrator** (earning the **Microsoft Certified: GitHub Administration** intermediate credential), engineered from the ground up against Microsoft Learn's **July 2026** (*Last updated May 5, 2026*) *Skills measured* blueprint and 2026 `docs.github.com` Enterprise Cloud (`GHEC`) & Enterprise Server (`GHES`) specifications.

---

## 📊 Course Snapshot

| Attribute | Value |
|---|---|
| **Exam Code & Title** | **Exam GH-100: GitHub Enterprise Administrator** |
| **Credential Awarded** | **GitHub Administration** *(Intermediate — **valid for 2 years**; eligible for online renewal on Microsoft Learn)* |
| **Required Prerequisite** | **None** *(designed for Administrators, DevOps Engineers, and Technology Managers governing GitHub Enterprise)* |
| **Blueprint Baseline** | **July 2026** (*Last updated 05/05/2026*) — **5 functional domains** / **39 skills** (`1.1`–`5.5`) |
| **Practice Inventory** | **6 full-length mock exams × 100 questions = 600 original questions** (`0` case studies — matching the live GH-100 exam) |
| **Per-Exam Domain Split** | **19 / 14 / 29 / 24 / 14** (`Manage identities & access 19%` · `Administer environment 14%` · `Secure dev & compliance 29%` · `Manage GitHub Actions 24%` · `Monitor & optimize usage 14%`) |
| **Per-Exam Item Mix** | **76** `multiple-choice` + **8** `→` ordered 4-step sequences (`84` MC total, balanced `21/21/21/21` `A–D`) + **16** `multi-select` (`13` five-option `Select two.` + **3** six-option `Select three.`), **21–33** `____` completions/set, **6–8** `Proposed solution:` evaluations/set |
| **Live Exam Conditions** | **100 minutes** exam time (**120 minutes** seat duration) · **700 / 1000** scaled score · **$99 USD** via Pearson VUE (`English` only) · **Strictly closed-book** (**NO Microsoft Learn access**) |
| **Upload Archive** | `GH-100-6x100.zip` (**45 files**) + `05-sample-upload/sample-upload.csv` (**15 rows**, `3` per domain) |

---

## 🗂️ Directory Layout

```text
course/GH-100/
├── README.md                                   # Course overview, blueprint matrix & verification commands
├── GH-100-6x100.zip                            # Ready-to-distribute 45-file archive
├── 01-landing-page/
│   └── landing-page.md                         # Complete Udemy metadata (Fields 1–6, 6 exam descriptions, Welcome & Congratulations)
├── 02-curriculum/
│   ├── curriculum-outline.md                   # Complete 5-domain / 39-skill mapping & 6-exam scenario guide
│   └── blueprint-alignment.md                  # Auto-generated domain/skill/item-type verification table
├── 03-practice-sets/
│   ├── set-1/practice-set-1.{csv,md}           # Exam 1: KestrelPay Global (Identity, EMUs, Enterprise Teams & Rulesets)
│   ├── set-2/practice-set-2.{csv,md}           # Exam 2: HelioBio Sciences (Hybrid GHEC + GHES, Support Bundles & Connect)
│   ├── set-3/practice-set-3.{csv,md}           # Exam 3: VanguardGrid Energy (Security Configs, Incident Purge & API Limits)
│   ├── set-4/practice-set-4.{csv,md}           # Exam 4: StratusRail Logistics (Actions Reuse, Azure VNet Runners & OIDC)
│   ├── set-5/practice-set-5.{csv,md}           # Exam 5: ZephyrAero Avionics (Audit Streams, Copilot/GHAS Metrics & FinOps)
│   └── set-6/practice-set-6.{csv,md}           # Exam 6: MeridianVault Banking (Full-Spectrum July 2026 Capstone)
├── 04-resources/
│   ├── sources.py                              # Official July 2026 39-skill documentation link registry
│   ├── sequences.py                            # 10 four-step administrative workflow sequence definitions (40 keys)
│   ├── terms.py                                # 148-entry atomic & sequence terminology bank (100% exercised)
│   ├── bank.py                                 # Blueprint constants & pipe-escaped question bank loader
│   ├── build.py                                # Deterministic 17-column Udemy CSV + Markdown review builder
│   ├── make_sample.py                          # Deterministic 15-row 5-domain stratified sample extractor
│   ├── validate.py                             # Structural, Jaccard (<=0.72), banned-phrase & cross-course validator
│   ├── package.py                              # Deterministic GH-100-6x100.zip packager
│   ├── test_course.py                          # Comprehensive unittest suite (CSVs, manifest, docs, ZIP, sibling uniqueness)
│   ├── questions/{1..6}.txt                    # Canonical 6 × 100 authored scenario sources
│   ├── answer-manifest.json                    # Keyed answers, option counts & skill traceability for all 600 items
│   ├── validation-report.json                  # Machine-readable validation telemetry (max Jaccard 0.4595)
│   ├── SUMMARY.md                              # Per-set metrics summary
│   ├── csv-format-spec.md                      # 17-column Udemy CSV contract specification
│   ├── sources-and-coverage.md                 # Official Microsoft Learn & GitHub Docs mapping across all 39 skills
│   └── publication-checklist.md                # Pre-publish QA & Udemy instructor upload checklist
└── 05-sample-upload/
    ├── README.md                               # Quick-test instructions for Udemy bulk importer
    └── sample-upload.csv                       # 15-question stratified smoke-test CSV (3 items × 5 domains)
```

---

## 🧭 Official July 2026 Blueprint Alignment

| Domain | Official Weight | Per Exam (`100`) | Across 6 Exams (`600`) | Multi-Select / Exam (`16`) |
|---|---:|---:|---:|---:|
| **1. Manage GitHub identities and access** (`1.1`–`1.9`) | 15–20% | **19** (`19.0%`) | **114** | **3** (`2 M2 + 1 M3`) |
| **2. Administer GitHub Enterprise environment** (`2.1`–`2.7`) | 10–15% | **14** (`14.0%`) | **84** | **2** (`2 M2`) |
| **3. Implement secure software development and compliance** (`3.1`–`3.10`) | 25–30% | **29** (`29.0%`) | **174** | **5** (`4 M2 + 1 M3`) |
| **4. Manage GitHub Actions** (`4.1`–`4.8`) | 20–25% | **24** (`24.0%`) | **144** | **4** (`3 M2 + 1 M3`) |
| **5. Monitor and optimize GitHub usage** (`5.1`–`5.5`) | 10–15% | **14** (`14.0%`) | **84** | **2** (`2 M2`) |
| **Total** | **100%** | **100 (`100.0%`)** | **600** | **16 (`13 M2 + 3 M3`)** |

---

## 🔬 Reproducible Build & Verification Pipeline

Run from the repository root (`/home/user/Cert`):

```bash
python3 course/GH-100/04-resources/build.py
python3 course/GH-100/04-resources/make_sample.py
python3 course/GH-100/04-resources/validate.py --report
python3 course/GH-100/04-resources/package.py
python3 -m unittest course/GH-100/04-resources/test_course.py -v
python3 course/check_csv_upload.py --all
python3 course/check_landing_page_fields.py
```

---

## ⚖️ Intellectual Property & Honest Exam Disclaimers

All **600 scenarios**, enterprise architectures (`KestrelPay`, `HelioBio`, `VanguardGrid`, `StratusRail`, `ZephyrAero`, `MeridianVault`), options, and explanations are **100% original educational material** authored from public Microsoft Learn and GitHub Enterprise documentation. Practice exam percentage scores do **not** map directly to Microsoft's `700 / 1000` criterion-referenced scaled score.
