# Microsoft Exam AZ-204: Developing Solutions for Microsoft Azure — Practice Test Course (`6 × 100 = 600` Questions)

Complete Udemy bulk-upload practice-test course package for **Microsoft Exam AZ-204: Developing Solutions for Microsoft Azure**, containing **6 full-length mock exams of 100 original questions each (`600` questions total)** aligned to the final official **January 14, 2026** Microsoft Learn skills-measured baseline.

> **Important Credential Lifecycle & Retirement Disclosure (Retrieved October 2026):**
> Microsoft **retired Exam AZ-204** (`Microsoft Certified: Azure Developer Associate`) and its renewal assessment on **July 31, 2026 at 11:59 PM CST**, introducing **Exam AI-200 (`Microsoft Certified: Azure AI Cloud Developer Associate`)** as its successor. Earned AZ-204 certifications remain active on Microsoft Learn transcripts until their 12-month expiration window concludes. This repository package preserves the final official **January 14, 2026** AZ-204 objective blueprint as a comprehensive developer benchmark and archival exam-prep resource covering core Azure compute, storage, identity/security, OpenTelemetry monitoring, and API/event/messaging integration skills that also carry forward into cloud developer roles.

---

## Published Exam Snapshot & Package Architecture

| Attribute | Official Exam AZ-204 Fact (Final Published Baseline) | Course Package Design |
|---|---|---|
| **Exam Code & Credential** | `AZ-204` · `Microsoft Certified: Azure Developer Associate` | `course/AZ-204/` (`AZ-204-6x100.zip`) |
| **Credential Status** | Retired **July 31, 2026** · succeeded by **Exam AI-200** | Explicitly disclosed in README, landing page, curriculum, and test headers |
| **Exam Duration / Seat Time** | **100 minutes** exam time (~120 minutes seat time) | Recommended **100 minutes** per practice set |
| **Live Item Count vs. Practice Bank** | **40–60 questions** on the live Pearson VUE exam | **100 questions × 6 sets = 600 original items** (expanded full-blueprint bank) |
| **Passing Score** | **700 / 1000** scaled score (`100–1000` scale) | Scaled score is **not** a raw percentage; Udemy target threshold `75%–80%` is a study benchmark only |
| **Registration Price (Historical US)** | **$165 USD** (regional pricing applied via Pearson VUE) | Independent educational material; no Microsoft endorsement |
| **Languages & SDK Focus** | C# / .NET, Python, JavaScript, Azure CLI, PowerShell, ARM/Bicep | Heavy C# (.NET 8 SDK v12 / Cosmos v3 / MSAL / Graph v5), Azure CLI, APIM XML, JSON & KQL coverage |

---

## Blueprint Domain Weighting (Every Set = 100 Questions)

Every mock exam strictly matches the five functional groups in the **January 14, 2026** AZ-204 Study Guide (excluding retired pre-2026 topics such as Azure Virtual Machines, Logic Apps, Notification Hubs, Azure CDN, and Azure Cache for Redis):

| # | Official AZ-204 Functional Group | Published Weight | Questions / Set | 6-Set Total | Multi-Select / Set |
|---:|---|---:|---:|---:|---:|
| 1 | `Develop Azure compute solutions` | 25–30% | **28** (28%) | 168 | 4 |
| 2 | `Develop for Azure storage` | 15–20% | **18** (18%) | 108 | 3 |
| 3 | `Implement Azure security` | 15–20% | **19** (19%) | 114 | 3 |
| 4 | `Monitor, troubleshoot, and optimize Azure solutions` | 5–10% | **10** (10%) | 60 | 2 |
| 5 | `Connect to and consume Azure services and third-party services` | 20–25% | **25** (25%) | 150 | 4 |
| **Total** | **37 Local Study-Map Skills (`1.1`–`5.8`)** | **100%** | **100** | **600** | **16** |

---

## Question-Pattern Fidelity & Udemy CSV Boundaries

Each 100-question exam models authentic Microsoft Azure developer question styles adapted cleanly into Udemy's 16-column CSV schema (`multiple-choice` and `multi-select`):

- **`76` Single-Answer (`multiple-choice`) Items:**
  - **`28–33` `____` Code / CLI / Policy / Query Completion Items (`>= 15` floor):** C# SDK v12 (`BlobClient`, `BlobSasBuilder`, `QueueClient`), Cosmos DB v3 (`FeedIterator`, `PatchItemAsync`, `TransactionalBatch`, `ContainerProperties`), MSAL (`AcquireTokenOnBehalfOf`, `AcquireTokenSilent`), Graph SDK v5, `CryptographyClient`, `DefaultAzureCredentialOptions`, `host.json`, multi-stage `.NET 8` Dockerfiles, Azure CLI (`az acr`, `az containerapp`, `az webapp`), APIM policy XML (`<validate-jwt>`, `<authentication-managed-identity>`, `<cache-lookup>`), and Application Insights KQL.
  - **`6–9` `Proposed solution:` Architecture & Code Evaluation Items (`>= 6` floor):** Evaluates why a flawed developer design fails (e.g., deleting `<base />` in APIM, `PeekMessagesAsync` for queue deletion, inline SAS revocation, classic Consumption >10-min timeouts, `Archive` direct reads) and identifies the exact fix.
- **`8` Four-Step `→` Sequence (`multiple-choice`) Items:** Adapts multi-step `DRAG DROP` workflows into four explicit `Step 1 → Step 2 → Step 3 → Step 4` options (combined with single-choice items for an exact `21 / 21 / 21 / 21` `A/B/C/D` answer-key slot distribution in every CSV).
- **`16` Multi-Select (`multi-select`) Items:** `13` five-option `Select two.` items and `3` six-option `Select three.` items spread `4 / 3 / 3 / 2 / 4` across Domains 1–5.
- **`4` Enterprise Case Studies × `3` Questions (`12` Case Items per Set, `24` Unique Scenarios):** Two CSV upload variants are provided for every exam:
  - `case-embedded-set-{1..6}.csv` *(recommended when Udemy randomizes question order)* — embeds the concise scenario brief inside each case stem (longest stem `751` characters, safely under Udemy's `1,000`-character limit).
  - `practice-set-{1..6}.csv` — compact stems (`Case study — <Name>: ...`) paired with `04-resources/case-studies.md`.

**What Udemy CSVs Cannot Reproduce:** Interactive drag-and-drop canvas widgets, inline multi-dropdown hot-area code boxes, split-pane tabbed case exhibits, live Azure sandbox labs, and locked non-returnable Yes/No problem-solution adaptive sequences cannot be imported via CSV and are adapted transparently as text-complete items.

---

## Directory Layout & Tooling

```text
course/AZ-204/
├── README.md
├── AZ-204-6x100.zip
├── 01-landing-page/
│   └── landing-page.md
├── 02-curriculum/
│   └── curriculum-outline.md
├── 03-practice-sets/
│   └── set-{1..6}/
│       ├── README.md
│       ├── practice-set-{1..6}.csv
│       ├── case-embedded-set-{1..6}.csv
│       └── practice-set-{1..6}.md
├── 04-resources/
│   ├── bank.py
│   ├── build.py
│   ├── cases.py
│   ├── sequences.py
│   ├── sources.py
│   ├── terms.py
│   ├── make_sample.py
│   ├── validate.py
│   ├── package.py
│   ├── test_course.py
│   ├── questions/{1..6}.txt
│   ├── answer-manifest.json
│   ├── validation-report.json
│   ├── case-studies.md
│   ├── case-study-upload-guide.md
│   ├── csv-format-spec.md
│   ├── sources-and-coverage.md
│   ├── publication-checklist.md
│   └── SUMMARY.md
└── 05-sample-upload/
    ├── README.md
    └── case-study-sample.csv
```

### Rebuild, Validate & Test Commands

```bash
python3 course/AZ-204/04-resources/build.py
python3 course/AZ-204/04-resources/make_sample.py
python3 course/AZ-204/04-resources/validate.py --report course/AZ-204/04-resources/validation-report.json
python3 course/AZ-204/04-resources/package.py
python3 -m unittest discover -s course/AZ-204/04-resources -p 'test_*.py' -v
python3 course/check_csv_upload.py --all
python3 course/check_landing_page_fields.py AZ-204
```

## Legal & Integrity Notice

All 600 questions, 24 enterprise case-study briefs, rationales, and code snippets are **100% original educational material** authored from official Microsoft Learn documentation. No recalled live exam questions and no Microsoft named case studies (`Contoso`, `Litware`, `VanArsdel`, `Wide World Importers`, `Coho Winery`, `Fabrikam`, `Adatum`) appear anywhere in this repository. Microsoft, Azure, and Microsoft Entra are trademarks of Microsoft Corporation, which does not sponsor or endorse this course.
