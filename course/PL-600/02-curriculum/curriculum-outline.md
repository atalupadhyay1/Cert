# Exam PL-600: Microsoft Power Platform Solution Architect — Curriculum Outline & Study Map

## 1. Course Structure (`6 × 100 = 600` Unique Questions)

Every practice exam mirrors the final **September 23, 2024** Microsoft Learn PL-600 domain weights (`46% / 37% / 17%`), tests **all 43 granular skills** in every single 100-question sitting, and rotates industry verticals and Solution Architect case studies across six distinct domains:

| Practice Set | Primary Vertical & Architectural Theme | Recommended CSV Upload | Four 3-Question Case Studies (`12` Items) |
| :---: | :--- | :--- | :--- |
| **Exam 1** | Sovereign Wealth Banking, Migration Throttling & VNet Integrations | `case-embedded-set-1.csv` | `SovereignCrest Private Bank`, `Alderbrook Commercial Leasing`, `Vespera Wealth Portal`, `Monarch Clearing Services` |
| **Exam 2** | Multi-Hospital Consolidation, Mobile Offline & Segmented ALM | `case-embedded-set-2.csv` | `HavenBridge Health System`, `CareStride Home Nursing`, `MedVantage Imaging Services`, `Aegis Clinical Trials` |
| **Exam 3** | Aerospace Dual-Write ERP, Dealer Portals & Fabric Analytics | `case-embedded-set-3.csv` | `StratosWing Aerospace`, `Kinetix Heavy Equipment`, `Vortex Turbine Aftermarket`, `IronPeak Plant Rollout` |
| **Exam 4** | Public-Sector Envisioning, Disaster Surge Messaging & OBO Security | `case-embedded-set-4.csv` | `MetroCivic Permitting Authority`, `Valor Disaster Relief Agency`, `Keystone State Licensing`, `CivicPulse Transit Network` |
| **Exam 5** | Global Retail Omnichannel, Storage Tiering & ETag Concurrency | `case-embedded-set-5.csv` | `Luminary Luxury Retail`, `FreshBasket Grocery Chain`, `OmniCart Fulfillment Hub`, `Solstice Peak Commerce` |
| **Exam 6** | Utility Transmission PCF, M&A Consolidation & Go-Live Tuning | `case-embedded-set-6.csv` | `GridVantage Transmission`, `EcoLedger Carbon Exchange`, `ApexGrid M&A Integration`, `Boreal Hydro Operations` |

---

## 2. Credential Lifecycle, Prerequisites & Exam AB-100 Continuity

- **Historical Credential:** `Microsoft Certified: Power Platform Solution Architect Expert` required passing **Exam PL-600** **plus** holding an active **`PL-200`** (`Functional Consultant Associate`) or **`PL-400`** (`Developer Associate`) credential.
- **Retirement & Successor:** Microsoft **retired Exam PL-600 on June 30, 2026** and introduced **Exam AB-100: Agentic AI Business Solutions Architect** (`Microsoft Certified: Agentic AI Business Solutions Architect Expert`).
- **Architectural Relevance:** Over 80% of enterprise Business Applications architecture failures stem from foundational platform decisions covered in this curriculum — Well-Architected Reliability/Security/Performance trade-offs, Dataverse schema ownership & cascading, Virtual vs Elastic vs replicated tables, Dual-write, APIM/Service Bus decoupling, VNet subnet delegation, Modernized BUs & Entra Group Teams, DLP endpoint filtering, API throttling (`HTTP 429`), and Solution Layer ALM.

---

## 3. Recommended Study Progression

1. **Diagnostic Pass (Exams 1 & 2 — Untimed Review Mode):** Read all four/six option rationales per question, paying special attention to why common anti-patterns fail (such as client-only Business Rules for column security, `Parental` cascading on historic activities, or SharePoint Document Management ACL assumptions).
2. **Targeted Skill Remediation:** Group any missed items by Skill ID (`1.1`–`3.8`) using the `[Skill X.Y: ... | Source: ...]` citation inside every `Overall Explanation`, and review the linked Microsoft Learn reference.
3. **Timed Simulation (Exams 3–6 — `100-Minute` Strict Clock):** Sit Exams 3 through 6 under timed exam conditions (`~1.0 minute/question` across 100 items, simulating high-density case + scenario pacing). Remember that raw practice percentages do **not** map 1-to-1 to Microsoft's historical `700 / 1000` scaled score.

---

## 4. Domain & Sub-Group Breakdown

### Domain 1: Perform solution envisioning and requirement analysis (`45–50%` → `46` Questions / Exam)
- **Initiate solution planning (`1.1`–`1.4`, `10` Qs/exam):** Power Platform Well-Architected (`Reliability`, `Security`, `Operational Excellence`, `Performance Efficiency`, `Experience Optimization`), component selection (`Model-driven`, `Canvas Mobile Offline`, `Power Pages`, `Copilot Studio`, `AI Builder`, `Dynamics 365`, `AppSource ISVs`, `Azure pro-code`), and migration/integration effort estimation + Fabric archival alternatives.
- **Identify organization information and metrics (`1.5`–`1.7`, `8` Qs/exam):** Current-state workshops + Power Automate `Process Mining` & `Task Mining`, shadow-IT discovery, fusion-team `RACI`/ARB/CoE governance, sovereign `Multi-Geo`/`CMK`/`ITAR` risk assessment, and baseline-anchored `SMART` KPIs.
- **Identify existing solutions and systems (`1.8`–`1.10`, `8` Qs/exam):** Enterprise Architecture Context Diagrams, multi-tenant Entra boundaries, APIM gateways, authoritative Master-Data System-of-Record survivorship, Common Data Model (`CDM`) alignment, and pre-migration data quality gates.
- **Capture requirements (`1.11`–`1.14`, `10` Qs/exam):** Outcome-driven `User Stories` + `Given/When/Then` Acceptance Criteria, persona Functional Requirements (including disconnected offline scope), Non-Functional Requirements (`RPO`/`RTO`, concurrency, `p95` latency, API volume, `WCAG 2.1 AA`, multi-decade retention), and future-state process harmonization before automating.
- **Perform fit/gap analyses (`1.15`–`1.18`, `10` Qs/exam):** `Standard -> Configuration -> AppSource ISV -> Pro-Code` prioritization, Dynamics 365 **restricted tables** (`Case / incident`, `Work Order / msdyn_workorder`, `Entitlement`), supported extensibility (`Custom Pages`, `PCF`, `Power Fx Formula columns`, `Custom APIs`), and MoSCoW `MVP` scope governance.

### Domain 2: Architect a solution (`35–40%` → `37` Questions / Exam)
- **Lead the design process (`2.1`–`2.7`, `14` Qs/exam):** Segmented Managed Solutions under one custom Publisher, `Figma`/prototype validation + `PCF`, `Component Libraries`/`Child Flows`/`ERD` & `Sequence` diagrams, persona/task app decomposition, `Alternate Keys` + `CMT` fixed-GUID migrations, native Dataverse charts vs `Power BI RLS` + `Microsoft Fabric Link`, `sync` vs `async` automation (`BPF`, `Logic Apps Standard`), and multi-tier/`Multi-Geo` Managed Environments + CoE Starter Kit.
- **Design the data model (`2.8`–`2.10`, `6` Qs/exam):** `Custom` vs `Parental` cascading (`POA` protection) + manual `N:N` intersect tables + `Hierarchical` (`Under`) & `Polymorphic` lookups, `Virtual Tables` (`Virtual Connector Provider`) vs native Dataverse replication, immutable `User/Team` vs `Organization` ownership, `Elastic tables` (`TTL`), `Activity` tables, and `File`/Azure Blob binary offloading.
- **Design integrations (`2.11`–`2.14`, `9` Qs/exam):** Teams `Adaptive Cards` + Exchange Server-Side Sync + Dynamics 365 F&O `Dual-write` & `Business Events`, SharePoint ACL nuances, `APIM` + `Service Bus` (FIFO sessions & DLQ) + `Event Grid` + `Custom APIs`, `OAuth 2.0 OBO` vs `S2S` / `Managed Identity`, `28-day` geo-redundant BCDR + `Hosted RPA` / `Work Queues`, and `VNet` subnet delegation vs `ExpressRoute` & `On-Premises Data Gateways`.
- **Design the security model (`2.15`–`2.17`, `8` Qs/exam):** Business Units + `Modernized BUs` + `Entra Security Group Teams` + `Access Team Templates`, `POA` hygiene, `Column Security Profiles`, `Hierarchy Security`, `Entra PIM`, `CMK`, `Customer Lockbox`, `Conditional Access` + `IP Firewall` / cookie binding, tenant `DLP` + `Endpoint Filtering`, and external access (`Power Pages` `Entra External ID` + `Table Permissions` vs `Entra B2B`).

### Domain 3: Implement the solution (`15–20%` → `17` Questions / Exam)
- **Validate the solution design (`3.1`–`3.4`, `9` Qs/exam):** `Solution Checker` & `App Checker` CI gates, server-side security boundary reviews (`Form`/`Entity` Business Rules vs `Column Security`), 5-minute `Dataverse Service Protection` (`6,000` req / `20m` compute, `Retry-After`, S2S pooling) vs 24-hour `PPR` (`CreateMultiple`/`UpdateMultiple`/`$batch`), `Database`/`File`/`Log` capacity tiering, and loop/race resolution (`Select columns`, `Trigger Conditions`, `Depth`, `If-Match` `ETag` -> `HTTP 412`).
- **Support go-live (`3.5`–`3.8`, `8` Qs/exam):** Canvas delegation & `N+1` `LookUp` fixes, indexed `Quick Find` vs leading `*` wildcards, async plug-in refactoring, `Azure Application Insights` KQL, `BypassCustomPluginExecution` + Change Tracking delta reconciliation, `Remove active customizations` on Solution Layers + Deployment Settings JSON, and Go/No-Go gates + `Administration mode` cutovers + hypercare war rooms.
