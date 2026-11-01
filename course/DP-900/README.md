# Microsoft Exam DP-900: Microsoft Azure Data Fundamentals — Practice Tests (`6 × 100 = 600` Questions)

Six full-length, blueprint-weighted practice exams (**600 original questions**) for **Microsoft Exam DP-900: Microsoft Azure Data Fundamentals** (`Microsoft Certified: Azure Data Fundamentals`), aligned to the official **July 21, 2026** Microsoft Learn *Skills measured* outline.

> **July 21, 2026 Blueprint & Fundamentals Exam Facts (Verified November 2026):**
> - **Credential:** `Microsoft Certified: Azure Data Fundamentals` (`Beginner` level · `Azure` product · `Data Engineer` / `Databases` · **no prerequisite** · **Active — Retirement date: none** · **Fundamentals certifications never expire and require no annual renewal**).
> - **July 21, 2026 Blueprint & Modern Azure Data Coverage:** Reflects Microsoft Learn's July 21, 2026 refreshes across *Describe ways to represent data*, *Describe the capabilities of Azure storage* (**Microsoft OneLake in Fabric** alongside Blob `Hot`/`Cool`/`Cold`/`Archive` tiers, **ADLS Gen2**, **Azure Files**, and **Azure Table storage**), and *Describe considerations for real-time data analytics* (**Microsoft Fabric Real-Time Intelligence** — `Eventstream`, `Eventhouse` `KQL` databases, `Real-Time Dashboards`, `Activator` — alongside **Azure Event Hubs**, **Azure Stream Analytics**, and **Apache Spark Structured Streaming**), plus **Microsoft Fabric** lakehouses/warehouses, **Microsoft Entra ID**, **Azure Migrate** (replacing retired standalone DMA), and **Azure Database for PostgreSQL / MySQL — Flexible Server** (without retired MariaDB or Single Server traps).
> - **Closed-Book & No Case Studies:** Live DP-900 delivers **40–60 standalone questions** in **45 minutes** (`~65 minutes` seat duration, `$99 USD` in the US via Pearson VUE or Certiport, **`700 / 1000`** scaled pass). Unlike Associate/Expert exams, **Microsoft Fundamentals exams are closed-book (NO split-screen Microsoft Learn access)** and include **no multi-tabbed case studies and no live labs**. Accordingly, this package contains **zero artificial case studies**; a **75-minute** timer on each 100-question set matches the live 45-second-per-question upper pace (`45 minutes` optional speed drill).

---

## Domain Allocation Across All 6 Mock Exams

| # | Official DP-900 Functional Group (Effective July 21, 2026) | Official Weight | Per Exam | 6-Exam Total |
|---:|---|---:|---:|---:|
| 1 | Describe core data concepts | 25–30% | **28** (`28.0%`) | **168** |
| 2 | Identify considerations for relational data on Azure | 20–25% | **24** (`24.0%`) | **144** |
| 3 | Describe considerations for working with non-relational data on Azure | 15–20% | **20** (`20.0%`) | **120** |
| 4 | Describe an analytics workload on Azure | 25–30% | **28** (`28.0%`) | **168** |
| **Total** | **All 4 Domains · All 30 Official Study-Guide Skills (`1.1`–`4.8`)** | **100%** | **100** | **600** |

---

## Six Practice Sets & Industry Themes

| Set | Practice Test Title | Industry Context | CSV Upload File |
|---:|---|---|---|
| 1 | Full-Length Mock Exam 1 | Omnichannel Retail & E-Commerce Analytics | `03-practice-sets/set-1/practice-set-1.csv` |
| 2 | Full-Length Mock Exam 2 | Healthcare Clinical & Patient Telemetry | `03-practice-sets/set-2/practice-set-2.csv` |
| 3 | Full-Length Mock Exam 3 | Smart City Transit & Municipal Services | `03-practice-sets/set-3/practice-set-3.csv` |
| 4 | Full-Length Mock Exam 4 | Connected Manufacturing & Industrial IoT | `03-practice-sets/set-4/practice-set-4.csv` |
| 5 | Full-Length Mock Exam 5 | Digital Banking & Fraud Risk Operations | `03-practice-sets/set-5/practice-set-5.csv` |
| 6 | Full-Length Mock Exam 6 | Global Logistics & Clean Energy Grid | `03-practice-sets/set-6/practice-set-6.csv` |

### Question Format Mix per 100-Question Set

- **`84` `multiple-choice` items** (exact `21 A / 21 B / 21 C / 21 D` answer-slot balance):
  - `76` single-answer concept, service-selection, `____` Fundamentals completion (`23–29` per set; `155` total across SQL clauses, ACID, 1NF/2NF/3NF, Blob tiers, `PartitionKey`/`RowKey`, Cosmos DB APIs/consistency, stream windows, and Power BI DAX/semantic modeling), and `Proposed solution:` evaluation items (`6–8` per set; `38` total)
  - `8` four-step (`→`) ordered workflow sequence items (OLTP-to-OLAP datastore pipeline, DBA/Data Engineer/Data Analyst handoff, 1NF → 2NF → 3NF normalization, Azure Migrate SQL Server cutover, Blob Storage Hot → Cool → Cold → Archive lifecycle, Cosmos DB account/container/query provisioning, ELT Bronze → Silver → Gold lakehouse, and Power BI Desktop → Service → App workflow)
- **`16` `multi-select` items** (`5` in D1, `4` in D2, `3` in D3, `4` in D4):
  - `13` five-option `Select two.` items
  - `3` six-option `Select three.` items
- **`0` case studies** (matching Microsoft's published Fundamentals exam design)

---

## Repository Layout

```text
course/DP-900/
├── README.md
├── DP-900-6x100.zip                         # Deterministic distributable archive
├── 01-landing-page/
│   └── landing-page.md                      # Udemy metadata, Official Exam Overview, Welcome/Congrats & 6 exam descriptions
├── 02-curriculum/
│   ├── curriculum-outline.md                # 30-skill study map, July 2026 updates & timing guide
│   └── blueprint-alignment.md               # Generated domain, pattern & 30-skill verification report
├── 03-practice-sets/
│   └── set-{1..6}/
│       ├── README.md
│       ├── practice-set-{1..6}.csv          # 100-row Udemy bulk-upload CSV (UTF-8 BOM, LF, 17 cols)
│       └── practice-set-{1..6}.md           # Human-readable review copy with full rationales & links
├── 04-resources/
│   ├── bank.py                              # Blueprint constants, 30-skill plan & question loader
│   ├── sources.py                           # Official Microsoft Learn URLs per skill (1.1 - 4.8)
│   ├── sequences.py                         # 32 four-step ('→') workflow sequence options
│   ├── terms.py                             # 143 unique option & distractor definitions (100% exercised)
│   ├── questions/{1..6}.txt                 # 600 authored questions (100 per file)
│   ├── build.py                             # Deterministic CSV, Markdown & manifest exporter
│   ├── make_sample.py                       # 12-row mixed 4-domain sample CSV builder
│   ├── validate.py                          # Structural, blueprint, Jaccard (< 0.72) & overlap validator
│   ├── package.py                           # Reproducible ZIP packager
│   ├── test_course.py                       # End-to-end unittest suite (incl. cross-course overlap check)
│   ├── answer-manifest.json                 # Exact option-key & answer-index manifest
│   ├── validation-report.json               # Machine-readable validation summary
│   ├── SUMMARY.md                           # Generated skill & domain breakdown
│   ├── csv-format-spec.md                   # 17-column Udemy CSV contract
│   ├── sources-and-coverage.md              # Skill-to-Microsoft-Learn traceability matrix
│   └── publication-checklist.md             # Pre-publish instructor checklist
└── 05-sample-upload/
    ├── README.md
    └── sample-upload.csv                    # 12-question quick-smoke Udemy test CSV (3 per domain)
```

---

## Build, Validate, Test & Package Commands

Run from `/home/user/Cert` (Python 3.10+, standard library only):

```bash
python3 course/DP-900/04-resources/build.py
python3 course/DP-900/04-resources/make_sample.py
python3 course/DP-900/04-resources/validate.py --report
python3 course/DP-900/04-resources/package.py
python3 course/DP-900/04-resources/test_course.py
python3 course/check_csv_upload.py --all
python3 course/check_landing_page_fields.py DP-900
```

---

## Fidelity & Disclaimer

All 600 questions, scenarios, company names (`VeloMart Retail`, `CarePulse Hospitals`, `MetroPulse Transit`, `ForgeWorks Manufacturing`, `CrestVault Digital Bank`, `NordGrid Logistics`), and explanations are **100% original educational material** authored from public Microsoft Learn documentation. No recalled exam items or Microsoft fictional company scenarios (`Contoso`, `Fabrikam`, `Litware`, `Northwind`, `AdventureWorks`, `Tailwind Traders`, `VanArsdel`, `Coho Winery`, `Adatum`, `Woodgrove`, `Trey Research`, `Lamna`, `Wide World Importers`, `Alpine Ski House`) are used. Practice percentages on Udemy (`75%` suggested target) are study benchmarks only and do **not** translate directly to Microsoft's `700 / 1000` criterion-referenced scaled score. Interactive Pearson VUE widgets (drag-and-drop lists, hot-area dropdowns, multi-statement Yes/No grids) are adapted into standard Udemy `multiple-choice` and `multi-select` formats.
