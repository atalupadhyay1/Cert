# Microsoft Exam PL-900: Microsoft Power Platform Fundamentals — Practice Tests (`6 × 100 = 600` Questions)

Six full-length, blueprint-weighted practice exams (**600 original questions**) for **Microsoft Exam PL-900: Microsoft Power Platform Fundamentals** (`Microsoft Certified: Power Platform Fundamentals`), aligned to the official **July 24, 2026** Microsoft Learn *Skills measured* update.

> **July 24, 2026 Blueprint & Fundamentals Exam Facts:**
> - **Credential:** `Microsoft Certified: Power Platform Fundamentals` (`Beginner` level · `App Maker` role · **no prerequisite** · **Retirement date: none** · **Fundamentals certifications NEVER expire and require no annual renewal**).
> - **Major July 24, 2026 Blueprint Overhaul:** Microsoft removed standalone *Power BI* and *Build Power Pages* domains and replaced manual low-level app building with AI-first creation (**Plan designer**, **code apps**, **Power Apps vibe experience**, **Copilot in Dataverse / Power Apps / Power Automate**) plus a full **20–25% domain on agents in Microsoft Copilot Studio** (conversational & autonomous agents, **Topics**, **Knowledge sources**, **Tools / MCP servers / agent flows**, **Channels**, **Microsoft Agent 365** governance, analytics, and **Agent Evaluations**). *Power Pages* remains tested for its **business value** in building external websites under Domain 1.
> - **Closed-Book & No Case Studies:** Live PL-900 delivers **40–60 standalone questions** in **45 minutes** (`65 minutes` seat duration, `$99 USD` in the US via Pearson VUE or Certiport, **`700 / 1000`** scaled pass). Unlike Associate/Expert exams, **Microsoft Fundamentals exams are closed-book (NO split-screen Microsoft Learn access)** and include **no multi-tabbed case studies and no live labs**. Accordingly, this package contains **zero artificial case studies**; a **75-minute** timer on each 100-question set matches the live 45-second-per-question upper pace (`45 minutes` optional speed drill).

---

## Domain Allocation Across All 6 Mock Exams

| # | Official PL-900 Functional Group (Effective July 24, 2026) | Official Weight | Per Exam | 6-Exam Total |
|---:|---|---:|---:|---:|
| 1 | Describe the business value of Microsoft Power Platform | 5–10% | **8** (`8.0%`) | **48** |
| 2 | Manage the Microsoft Power Platform environment | 20–25% | **23** (`23.0%`) | **138** |
| 3 | Demonstrate the capabilities of Power Apps | 20–25% | **23** (`23.0%`) | **138** |
| 4 | Demonstrate the capabilities of Power Automate | 20–25% | **23** (`23.0%`) | **138** |
| 5 | Describe features and capabilities of agents in Microsoft Copilot Studio | 20–25% | **23** (`23.0%`) | **138** |
| **Total** | **All 5 Domains · 34 Local Study-Map Skills (`1.1`–`5.8`)** | **100%** | **100** | **600** |

---

## Six Practice Sets & Industry Themes

| Set | Practice Test Title | Industry Context | CSV Upload File |
|---:|---|---|---|
| 1 | Full-Length Mock Exam 1 | Retail Store Operations | `03-practice-sets/set-1/practice-set-1.csv` |
| 2 | Full-Length Mock Exam 2 | Healthcare Clinic Onboarding | `03-practice-sets/set-2/practice-set-2.csv` |
| 3 | Full-Length Mock Exam 3 | Municipal Citizen Services | `03-practice-sets/set-3/practice-set-3.csv` |
| 4 | Full-Length Mock Exam 4 | Manufacturing Field Quality | `03-practice-sets/set-4/practice-set-4.csv` |
| 5 | Full-Length Mock Exam 5 | Financial Client Services | `03-practice-sets/set-5/practice-set-5.csv` |
| 6 | Full-Length Mock Exam 6 | Global Logistics & Campus HR | `03-practice-sets/set-6/practice-set-6.csv` |

### Question Format Mix per 100-Question Set

- **`84` `multiple-choice` items** (exact `21 A / 21 B / 21 C / 21 D` answer-slot balance):
  - `76` single-answer concept, scenario, `____` Fundamentals completion (`15` per set: Power Fx `Filter`/`Navigate`/`SubmitForm`/`NewForm`/`LookUp`/`User()`, Dataverse forms/Business Rules/DLP groups, Power Apps vibe `Publish draft tables`, Approvals/loops, Copilot Studio `Question` node, `MCP` server, `Microsoft Agent 365`, `Agent viewer` role), and `Proposed solution:` evaluation items (`6–8` per set)
  - `8` four-step (`→`) ordered workflow sequence items (Dataverse Copilot table creation, Power Platform pipelines ALM, Plan designer, Power Apps vibe, SharePoint Approvals cloud flow, Power Automate for desktop Recorder, Copilot Studio agent publishing, and Agent Evaluations)
- **`16` `multi-select` items** (`1` in D1, `4` in D2, `4` in D3, `3` in D4, `4` in D5):
  - `13` five-option `Select two.` items
  - `3` six-option `Select three.` items
- **`0` case studies** (matching Microsoft's published Fundamentals exam design)

---

## Repository Layout

```text
course/PL-900/
├── README.md
├── PL-900-6x100.zip                         # Deterministic distributable archive
├── 01-landing-page/
│   └── landing-page.md                      # Udemy metadata, Official Exam Overview, Welcome/Congrats & 6 exam descriptions
├── 02-curriculum/
│   └── curriculum-outline.md                # 34-skill study map, July 2026 changes & timing guide
├── 03-practice-sets/
│   ├── set-1/ ... set-6/
│   │   ├── README.md
│   │   ├── practice-set-{N}.csv             # 100-row Udemy bulk-upload CSV (UTF-8 BOM, LF, 17 cols)
│   │   └── practice-set-{N}.md              # Human-readable review copy with full rationales & links
├── 04-resources/
│   ├── bank.py                              # Blueprint constants, 34-skill plan & question loader
│   ├── sources.py                           # Official Microsoft Learn URLs per skill (1.1 - 5.8)
│   ├── sequences.py                         # 32 four-step ('→') workflow sequence options
│   ├── terms.py                             # 106 unique option & distractor definitions (100% exercised)
│   ├── questions/{1..6}.txt                 # 600 authored questions (100 per file)
│   ├── build.py                             # Deterministic CSV, Markdown & manifest exporter
│   ├── make_sample.py                       # 10-row mixed 5-domain sample CSV builder
│   ├── validate.py                          # Structural, blueprint, Jaccard (<= 0.72) & overlap validator
│   ├── package.py                           # Reproducible ZIP packager with stale-file guards
│   ├── test_course.py                       # End-to-end unittest suite
│   ├── answer-manifest.json                 # Exact option-key & answer-index manifest
│   ├── validation-report.json               # Machine-readable validation summary
│   ├── SUMMARY.md                           # Generated skill & domain breakdown
│   ├── csv-format-spec.md                   # 17-column Udemy CSV contract
│   ├── sources-and-coverage.md              # Skill-to-Microsoft-Learn traceability matrix
│   └── publication-checklist.md             # Pre-publish instructor checklist
└── 05-sample-upload/
    ├── README.md
    └── sample-upload.csv                    # 10-question quick-smoke Udemy test CSV (2 per domain)
```

---

## Build, Validate, Test & Package Commands

Run from `/home/user/Cert` (Python 3.10+, standard library only):

```bash
python3 course/PL-900/04-resources/build.py
python3 course/PL-900/04-resources/make_sample.py
python3 course/PL-900/04-resources/validate.py --report
python3 course/PL-900/04-resources/package.py
python3 course/PL-900/04-resources/test_course.py
python3 course/check_csv_upload.py --all
python3 course/check_landing_page_fields.py PL-900
```

---

## Fidelity & Disclaimer

All 600 questions, scenarios, company names, and explanations are **100% original educational material** authored from public Microsoft Learn documentation. No recalled exam items or Microsoft fictional company case scenarios (`Contoso`, `Fabrikam`, `Litware`, `Northwind`, `AdventureWorks`, `Tailwind Traders`, `VanArsdel`, `Coho Winery`, `Adatum`, `Woodgrove`, `Trey Research`, `Lamna`, `Wide World Importers`, `Alpine Ski House`) are used. Practice percentages on Udemy (`75%` suggested target) are study benchmarks only and do **not** translate directly to Microsoft's `700 / 1000` criterion-referenced scaled score. Interactive Pearson VUE widgets (drag-and-drop lists, hot-area dropdowns, multi-statement Yes/No grids) are adapted into standard Udemy `multiple-choice` and `multi-select` formats.
