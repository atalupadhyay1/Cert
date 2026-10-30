# 🗺️ Microsoft Exam PL-200 — Curriculum Outline & 43-Skill Blueprint

**Course:** `PL-200 Power Platform Consultant: 6 Practice Exams (600 Q)`  
**Official Study Guide Baseline:** December 26, 2024 (`https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-200`)  
**Lifecycle Notice:** Exam PL-200 (`Microsoft Certified: Power Platform Functional Consultant Associate`) retired on **August 31, 2026** and was replaced by **Exam AB-410: Building Intelligent Applications (`Intelligent Applications Builder Associate`)**.

---

## 1. Course Structure in Udemy Practice-Test Mode

Udemy Practice-Test-Only courses publish **6 standalone timed practice exams** (`100 questions` · `100 minutes` each):

| Section / Practice Test | Industry Vertical | CSV File (Recommended Self-Contained Upload) | Case Studies (`4 × 3 = 12` Q) |
|---|---|---|---|
| **Practice Test 1** | Commercial Real Estate & Property Leasing | `03-practice-sets/set-1/case-embedded-set-1.csv` | *Harborstone Property Group*, *Crestview Tenant Portals*, *Vanguard Facility Maintenance*, *Oakridge Lease Renewals* |
| **Practice Test 2** | Specialty Healthcare & Clinical Referrals | `03-practice-sets/set-2/case-embedded-set-2.csv` | *Clearpath Specialty Clinics*, *MedBridge Referral Portal*, *Apex Medical Equipment*, *Beacon Clinical Trials* |
| **Practice Test 3** | Municipal Permitting & Utility Field Operations | `03-practice-sets/set-3/case-embedded-set-3.csv` | *Rivergate Civic Permits*, *MetroWater Field Operations*, *Greenway Parks & Events*, *Summit Transit Claims* |
| **Practice Test 4** | Industrial Manufacturing & Dealer Warranty | `03-practice-sets/set-4/case-embedded-set-4.csv` | *Ironclad Heavy Machinery*, *GearGrid Dealer Portal*, *Precision Quality Audits*, *Titan Spare Parts Supply* |
| **Practice Test 5** | Wealth Advisory & Insurance Underwriting | `03-practice-sets/set-5/case-embedded-set-5.csv` | *Sterling Surety Insurance*, *Kestrel Client Onboarding*, *Pinnacle Claims Resolution*, *Meridian Regulatory Filing* |
| **Practice Test 6** | Higher Education & Global Nonprofit Grants | `03-practice-sets/set-6/case-embedded-set-6.csv` | *Westbrook University Admissions*, *GlobalAid Grant Portal*, *Horizon Alumni Engagement*, *Atlas Field Scholarships* |

---

## 2. Domain & Question-Type Blueprint (Identical Across All 6 Exams)

| Domain | Official Weight | Per Exam | 6-Exam Total | `S` (Single) | `O` (4-Step `→`) | `M2` (Select 2) | `M3` (Select 3) |
|---|---:|---:|---:|---:|---:|---:|---:|
| **1. Configure Microsoft Dataverse** | 25–30% | **28** | **168** | 22 | 2 (`1.5`, `1.12`) | 3 | 1 (`1.6`) |
| **2. Create apps by using Microsoft Power Apps** | 25–30% | **28** | **168** | 21 | 2 (`2.9`, `2.12`) | 4 | 1 (`2.11`) |
| **3. Create and manage logic and process automation** | 25–30% | **27** | **162** | 21 | 2 (`3.8`, `3.11`) | 3 | 1 (`3.12`) |
| **4. Manage environments** | 15–20% | **17** | **102** | 12 | 2 (`4.5`, `4.6`) | 3 | 0 |
| **Total** | **100%** | **100** | **600** | **76** | **8** | **13** | **3** |

- **Exported Udemy `multiple-choice`:** `76 + 8 = 84` per exam (`21 A / 21 B / 21 C / 21 D` exact answer-slot balance)
- **Exported Udemy `multi-select`:** `13 + 3 = 16` per exam (`4 + 5 + 4 + 3` across Domains 1–4)
- **Completion (`____`) items:** `16` per exam (`96` total across Power Fx, WDL, OData, Low-code Plug-ins, Power Pages Table Permissions, Custom Cascading, and Word XML)
- **Evaluation (`Proposed solution:`) items:** `6–7` per exam (`37` total)

---

## 3. Detailed 43-Skill Mapping to Official Study Guide

### Domain 1: Configure Microsoft Dataverse (`28` items/exam · `168` total)
- **Manage the data model**
  - `1.1` (`3/exam`): Standard vs `Activity` vs `Virtual` tables; creation-time `Ownership` immutability (`User or team` vs `Organization`); `Attachments`, `Quick-Create`, `Queues`, and `Track changes`.
  - `1.2` (`2/exam`): `1:N` and `N:N` relationships — native `N:N` hidden system intersect limitations vs manual intersect tables with two `1:N` lookups.
  - `1.3` (`3/exam`): Relationship behaviors (`Parental`, `Referential`, `Referential, Restrict Delete`, `Custom`) and cascading rules (`Assign = Cascade Active`, `Delete = Restrict`).
  - `1.4` (`3/exam`): Column types (`Customer` polymorphic lookup, `Choice`/`Choices`), `Alternate Keys` (natural-key uniqueness/upserts), `Rollup` columns (async 1-hour min), and live `Power Fx Formula` columns.
- **Manage Dataverse**
  - `1.5` (`2/exam`): `Dataverse Search` enablement in PPAC, `Quick Find View` `Find Columns` (indexed) vs `View Columns` (returned) vs row filters.
  - `1.6` (`2/exam`): Three-tier `Dataverse Auditing` (Environment + Table + Column), `Log` storage capacity, and retention policies.
  - `1.7` (`2/exam`): Data import/export (`Import from Excel/CSV`, `Power Platform Dataflows`, `Azure Synapse Link`/`Fabric Link`, `Excel Online` vs `Dynamic` vs `Static` exports).
  - `1.8` (`3/exam`): `Duplicate Detection Rules` (explicit publishing, 5-published-rule per-table cap) and recurring `Bulk Record Deletion` jobs.
- **Configure security settings**
  - `1.9` (`2/exam`): Business Units and `Modernized Business Units` (matrix cross-BU Security Role assignments).
  - `1.10` (`2/exam`): Custom `Security Roles` (copying `Basic User`, privilege depths, `Append` + `Append To` lookup pairing, `Direct User + Team` inheritance).
  - `1.11` (`2/exam`): Users, `Owner Teams`, `Access Team Templates` (ad-hoc row sharing), and `Microsoft Entra ID Group Teams`.
  - `1.12` (`2/exam`): `Column Security Profiles` (masking & field Read/Update/Create) and `Hierarchy Security` (`Manager` vs `Position` trees).

### Domain 2: Create apps by using Microsoft Power Apps (`28` items/exam · `168` total)
- **Create model-driven apps**
  - `2.1` (`3/exam`): Sitemap (`Areas`/`Groups`/`Subareas` auto-hiding by `Read` privilege) and multiple form types (`Main` `Form Order` + mandatory `Fallback`, `Quick Create`, `Quick View`, `Card`).
  - `2.2` (`2/exam`): Modern form designer controls (`Editable Grid`, `Form Component Control` inline parent editing vs `Quick View` read-only, Lookup `Filter by related rows`).
  - `2.3` (`2/exam`): Views (`Public` cross-table columns/filters, `Quick Find`, `Lookup`, `Associated`, user-shared `Personal` views).
  - `2.4` (`2/exam`): `Custom Pages` (responsive containers, modal/side-pane navigation, `GUID(Param("recordId"))`).
  - `2.5` (`3/exam`): `Modern Commanding` (`Power Fx` `Patch`, `Confirm`, `Notify`, `Self.Selected.Item` inside managed `Component Libraries`).
  - `2.6` (`2/exam`): Embedded Canvas apps (`ModelDrivenFormIntegration.Item` / `RefreshForm`) and contextual/system `Power BI` reports and dashboards.
- **Describe canvas apps**
  - `2.7` (`2/exam`): Canvas structure, responsive `Horizontal`/`Vertical` auto-layout containers (`Scale to fit = Off`), and shared `Component Libraries`.
  - `2.8` (`3/exam`): Navigation (`Navigate` context records), `Set` vs `UpdateContext` vs `App.Formulas`, `ClearCollect`, Dataverse delegation (`500`/`2,000` cap), and `IfError`.
  - `2.9` (`2/exam`): Calling solution cloud flows from Canvas (`Power Apps (V2)` trigger, `Respond to a Power App or flow`, `FlowName.Run()`, `Run-only users`).
- **Build Microsoft Power Pages**
  - `2.10` (`2/exam`): Design Studio workspaces (`Pages`, `Styling`, `Data`, `Set up`), `Lists`, `Basic Forms` (`Insert`/`Edit`/`ReadOnly`), and `Sync` with `Power Pages Management`.
  - `2.11` (`2/exam`): `Multi-Step Forms` (`Condition` step branching), SharePoint document subgrids, portal search, and `Power BI Embedded` with `RLS`.
  - `2.12` (`3/exam`): Website security (`Table Permissions` `Global`/`Contact`/`Account`/`Parent`/`Self`, `Web Roles`, `Page Access Control Rules`) and `Microsoft Entra External ID` / OIDC authentication.

### Domain 3: Create and manage logic and process automation (`27` items/exam · `162` total)
- **Create and manage cloud flows**
  - `3.1` (`2/exam`): Choosing `Automated`/`Instant`/`Scheduled` cloud flows vs `Business Process Flows` vs synchronous `Real-time workflows` / `Low-code plug-ins`.
  - `3.2` (`2/exam`): Connector `Triggers` (webhooks vs polling), `Actions`, `Connections`, and solution `Connection References`.
  - `3.3` (`3/exam`): Logic controls (`Scope` `Configure run after` Try/Catch + `Terminate`, `Apply to each` `Concurrency Control` race conditions with `Set variable` vs `Compose`).
  - `3.4` (`3/exam`): Dynamic content, WDL expressions (`coalesce`, `empty`, `formatDateTime`, `addDays`, `length`), and `@and(...)` `Trigger Conditions`.
  - `3.5` (`3/exam`): Dataverse connector (`Select columns`, OData `Filter rows`, `Row scope`, `Expand Query`, `Relate rows`/`Unrelate rows`, bound/unbound actions, `Child Flows`).
  - `3.6` (`2/exam`): `Flow Checker`, `Static Result` mock testing, `28-day Run History` (`Resubmit`), and `Run-only users` vs `Co-owner`.
- **Create and manage business process flows**
  - `3.7` (`2/exam`): BPF limits (`<= 30` stages, `<= 5` related tables), `If/Else` branching from preceding-stage steps, Security Roles, and `Order Process Flow`.
  - `3.8` (`2/exam`): Adding classic workflows (`Stage Entry`/`Exit`) and solution `Cloud Flow Steps`, plus reporting on the auto-created BPF Dataverse table.
- **Create and manage classic Dataverse workflows**
  - `3.9` (`2/exam`): `Real-time (synchronous)` (`Calling User` vs `Workflow Owner`, pre-commit `Canceled` rollback) vs `Background (asynchronous)` workflows.
  - `3.10` (`2/exam`): Troubleshooting `System Jobs` (`ProcessSession`), recursion depth loops, and `Automatically delete completed workflow jobs`.
- **Implement low-code logic**
  - `3.11` (`2/exam`): `Dataverse Accelerator` low-code Power Fx plug-ins (`Instant` Custom APIs & `Automated` `Pre-operation`/`Post-operation` `Error()`).
  - `3.12` (`2/exam`): `Business Rules` (`Entity` vs form scopes; tab/section and `MultiSelect Choice` limits) and reusable `Power Fx Functions`.

### Domain 4: Manage environments (`17` items/exam · `102` total)
- **Participate in application lifecycle management (ALM)**
  - `4.1` (`2/exam`): `App Checker` (Studio formulas/accessibility/delegation) vs `Solution Checker` (full-solution static analysis & Managed Environment import gates).
  - `4.2` (`3/exam`): Custom `Solution Publishers` (schema & option-value prefixes), `Segmented Solutions`, and `Clone a Patch` / `Clone to Solution`.
  - `4.3` (`3/exam`): `Managed` vs `Unmanaged` solutions, `See solution layers` (`Remove Active Customizations`), and `Solution Upgrade` (`Stage for upgrade` -> `Apply upgrade`) vs `Update`.
  - `4.4` (`2/exam`): Sandbox `Full Copy` vs `Minimal Copy`, `Administration mode`, `Reset`, 7/28-day Backups, `DLP` policies, and `Managed Environments`.
  - `4.5` (`3/exam`): `Environment Variables` (`Text`, `Decimal`, `JSON`, SharePoint `Data Source`, Key Vault `Secret`), `Connection References`, and `Power Platform pipelines`.
- **Manage interoperability with other services**
  - `4.6` (`2/exam`): `Server-Side Synchronization`, `Approve Email` + `Test & Enable Mailbox`, `Private` vs `Public` `Queues` (`Pick`/`Release`), and `Dynamics 365 App for Outlook`.
  - `4.7` (`2/exam`): `SharePoint Document Management` (folder hierarchy & non-inherited SharePoint ACLs vs Dataverse `File` columns) and `Microsoft Word Templates` (`XML Mapping Pane` `Repeating` control, `<= 100` child rows).
