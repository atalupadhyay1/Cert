# PL-600: Microsoft Power Platform Solution Architect — Blueprint Alignment Report

## Official Exam & Lifecycle Metadata

- **Exam:** `PL-600: Microsoft Power Platform Solution Architect`
- **Credential:** `Microsoft Certified: Power Platform Solution Architect Expert`
- **Mandatory Prerequisite:** One active Associate certification required: Microsoft Certified: Power Platform Functional Consultant Associate (PL-200) OR Microsoft Certified: Power Platform Developer Associate (PL-400)
- **Final Official Study Guide Revision:** `September 23, 2024` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-600)
- **Lifecycle & Retirement Notice:** Exam `PL-600` and `Microsoft Certified: Power Platform Solution Architect Expert` retired on **`June 30, 2026`** (https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams). Microsoft introduced **`Exam AB-100: Agentic AI Business Solutions Architect (Microsoft Certified: Agentic AI Business Solutions Architect Expert)`** (https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-business-solutions-architect/) as the successor AI-first Business Applications architect certification.
- **Certification Overview:** https://learn.microsoft.com/en-us/credentials/certifications/power-platform-solution-architect-expert/
- **Exam Overview:** https://learn.microsoft.com/en-us/credentials/certifications/exams/pl-600/
- **Course Bank Volume:** `6 practice exams x 100 questions = 600 unique questions` (`0` duplicate stems, `0` duplicate explanations)
- **Option Library Coverage:** `124 / 124` canonical terms exercised (`100.0%`), max pairwise stem Jaccard similarity `0.513` (`E4Q063` vs `E5Q063`)

## Domain Weighting Verification (Every Practice Set = 100 Questions)

| Domain | Official Weight | Target / Set | Set 1 | Set 2 | Set 3 | Set 4 | Set 5 | Set 6 | Total (600) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Domain 1:** Perform solution envisioning and requirement analysis | 45–50% | 46% | 46 | 46 | 46 | 46 | 46 | 46 | **276** (46.0%) |
| **Domain 2:** Architect a solution | 35–40% | 37% | 37 | 37 | 37 | 37 | 37 | 37 | **222** (37.0%) |
| **Domain 3:** Implement the solution | 15–20% | 17% | 17 | 17 | 17 | 17 | 17 | 17 | **102** (17.0%) |
| **Total** | **100%** | **100** | **100** | **100** | **100** | **100** | **100** | **100** | **600** |

## Question-Format & Pattern Telemetry Across Practice Sets

| Set | Focus | Single (`S`) | Sequence (`O`) | Multi-2 (`M2`) | Multi-3 (`M3`) | `____` Completions | `Proposed solution:` | Case Items (`4x3`) | MC Key Pos `1/2/3/4` |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Multi-Geo sovereignty, Modernized BUs & CMK, 4.2M-row cutover throttling, Power Pages vs B2B, and VNet subnet delegation | 76 | 8 | 13 | 3 | 22 | 6 | 12 | `21/21/21/21` |
| 2 | Virtual tables over 60M HL7 rows, rural iPad Mobile Offline, Elastic tables for IoT bursts, Solution Layers, and loop guards | 76 | 8 | 13 | 3 | 28 | 7 | 12 | `21/21/21/21` |
| 3 | Dynamics 365 F&O Dual-write + ITAR Lockbox, Account-scoped Power Pages + AS/400 RPA, Fabric Link + Power BI RLS, and Canvas delegation | 76 | 8 | 13 | 3 | 29 | 6 | 12 | `21/21/21/21` |
| 4 | Well-Architected discovery & MVP fit/gap, Service Bus surge buffering & S2S pooling, Business Rule security traps & OBO, and ExpressRoute nuances | 76 | 8 | 13 | 3 | 33 | 6 | 12 | `21/21/21/21` |
| 5 | Organization vs User/Team ownership & Access Teams, File/Blob capacity offloading, ETag optimistic concurrency, and Application Insights KQL | 76 | 8 | 13 | 3 | 28 | 6 | 12 | `21/21/21/21` |
| 6 | Reusable PCF & hierarchical asset rollups, Entra PIM + CoE Managed Environments, M&A deduplication, and Quick Find index & Administration mode cutover | 76 | 8 | 13 | 3 | 33 | 6 | 12 | `21/21/21/21` |

## Granular Skill Coverage Across All 43 Official September 23, 2024 Study-Guide Skills

| Skill ID | Domain | Official Skill Measured | Per Set | 6-Set Total | Primary Microsoft Learn Reference |
| :---: | :---: | :--- | :---: | :---: | :--- |
| `1.1` | D1 | Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | 3 | 18 | [Microsoft Power Platform Well-Architected overview](https://learn.microsoft.com/en-us/power-platform/well-architected/overview) |
| `1.2` | D1 | Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | 3 | 18 | [Identify Microsoft Power Platform solution components](https://learn.microsoft.com/en-us/training/modules/become-solution-architect/) |
| `1.3` | D1 | Identify and select components from existing apps, Dynamics 365, AppSource ISVs, and Azure | 2 | 12 | [Evaluate Dynamics 365 apps, AppSource ISVs, and Azure extensions](https://learn.microsoft.com/en-us/training/modules/discover-customer-needs/) |
| `1.4` | D1 | Identify and estimate data migration and integration efforts, complexity drivers, and alternatives | 2 | 12 | [Estimate migration and integration efforts and alternatives](https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview) |
| `1.5` | D1 | Guide discovery of current-state business processes using workshops and Process/Task Mining | 3 | 18 | [Guide discovery of current-state business processes and process mining](https://learn.microsoft.com/en-us/power-automate/minit/overview) |
| `1.6` | D1 | Assess organizational risk factors across residency, compliance, governance maturity, and debt | 3 | 18 | [Assess organizational risk factors, governance maturity, and compliance](https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview) |
| `1.7` | D1 | Review and validate measurable key success criteria, KPIs, and adoption targets | 2 | 12 | [Review measurable key success criteria, KPIs, and adoption targets](https://learn.microsoft.com/en-us/power-platform/guidance/adoption/measure-business-value) |
| `1.8` | D1 | Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | 3 | 18 | [Evaluate an organization’s enterprise architecture landscape](https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview) |
| `1.9` | D1 | Identify authoritative data sources, master data ownership, and residency/classification rules | 3 | 18 | [Identify authoritative data sources and master data boundaries](https://learn.microsoft.com/en-us/training/paths/solution-architect-data/) |
| `1.10` | D1 | Define use cases and data quality standards for existing data prior to migration or integration | 2 | 12 | [Define use cases and data quality standards for existing data](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export) |
| `1.11` | D1 | Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | 3 | 18 | [Refine high-level requirements into testable user stories and acceptance criteria](https://learn.microsoft.com/en-us/training/modules/propose-solution/) |
| `1.12` | D1 | Identify functional requirements across personas, business rules, approvals, and offline access | 2 | 12 | [Identify functional requirements across personas, offline, and workflows](https://learn.microsoft.com/en-us/power-apps/mobile/setup-mobile-offline) |
| `1.13` | D1 | Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | 3 | 18 | [Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG)](https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview) |
| `1.14` | D1 | Guide future-state business process optimization and standardization before automating | 2 | 12 | [Guide future-state business process optimization and standardization](https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/overview) |
| `1.15` | D1 | Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | 3 | 18 | [Perform fit/gap analyses and classify configuration vs custom code](https://learn.microsoft.com/en-us/training/modules/propose-solution/) |
| `1.16` | D1 | Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | 3 | 18 | [Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities) |
| `1.17` | D1 | Address functional gaps through supported low-code/pro-code alternate solutions | 2 | 12 | [Address functional gaps through low-code/pro-code alternate solutions](https://learn.microsoft.com/en-us/power-platform/well-architected/operational-excellence/overview) |
| `1.18` | D1 | Determine MVP vs phased solution scope boundaries and govern scope changes | 2 | 12 | [Determine MVP vs phased solution scope and manage scope boundaries](https://learn.microsoft.com/en-us/training/paths/become-solution-architect/) |
| `2.1` | D2 | Design segmented solution topology, custom Publisher strategy, and Managed Environments | 2 | 12 | [Design solution topology, publisher segmentation, and Managed Environments](https://learn.microsoft.com/en-us/power-platform/alm/segmented-solutions-alm) |
| `2.2` | D2 | Identify app customization approaches and validate interactive user experience prototypes | 2 | 12 | [Select customization approaches for existing apps and validate UX prototypes](https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/design-consistency) |
| `2.3` | D2 | Maximize component reuse (PCF, Component Libraries, Child Flows) and communicate designs visually | 2 | 12 | [Maximize component reuse (PCF, Component Libraries, Child Flows) & visual diagrams](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview) |
| `2.4` | D2 | Design apps by grouping required features based on persona, role, task, and offline needs | 2 | 12 | [Design role-based and task-based app experiences across form factors](https://learn.microsoft.com/en-us/power-apps/guidance/planning/app-design) |
| `2.5` | D2 | Design enterprise data migration strategies, load sequencing, Alternate Keys, and CMT tooling | 2 | 12 | [Design enterprise data migration strategies, load order, and tooling](https://learn.microsoft.com/en-us/power-platform/admin/create-schema-export-data) |
| `2.6` | D2 | Design data visualization strategies across Dataverse charts, Power BI RLS, and Fabric/Synapse Link | 2 | 12 | [Design data visualization (Dataverse charts, Power BI RLS, Fabric/Synapse Link)](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-synapse) |
| `2.7` | D2 | Design automation strategies (sync vs async, BPF, Logic Apps) and multi-environment ALM topology | 2 | 12 | [Design automation & multi-environment strategies (CoE Starter Kit & ALM)](https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit) |
| `2.8` | D2 | Design Dataverse relationships (1:N, N:N, hierarchical, polymorphic) and cascading behaviors | 2 | 12 | [Design Dataverse relationships (1:N, N:N, hierarchical) & cascading behaviors](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships) |
| `2.9` | D2 | Determine when to connect external data in place (Virtual tables) versus import/replicate into Dataverse | 2 | 12 | [Connect external data in place (Virtual tables) vs import/replicate into Dataverse](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-virtual-entities) |
| `2.10` | D2 | Design complex data models (ownership immutability, Elastic/Activity tables, binary storage offloading) | 2 | 12 | [Design complex data models (ownership, Elastic/Activity tables, storage capacity)](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/elastic-tables) |
| `2.11` | D2 | Design collaboration (Teams, SharePoint ACL nuances, Exchange) and Dynamics 365 Dual-write integrations | 2 | 12 | [Design Teams, SharePoint, Exchange, and Dynamics 365 (Dual-write) integrations](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dual-write/dual-write-overview) |
| `2.12` | D2 | Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | 3 | 18 | [Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM)](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions) |
| `2.13` | D2 | Design authentication (OBO vs S2S, Managed Identity), BCDR (RPO/RTO, geo-backups), and RPA | 2 | 12 | [Design authentication (OBO vs S2S, Managed Identity), BCDR, and RPA architectures](https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments) |
| `2.14` | D2 | Assess VNet subnet delegation, Azure ExpressRoute nuances, Data Gateways, and IP firewall networking | 2 | 12 | [Assess VNet integration, Azure ExpressRoute, gateways, and IP firewall networking](https://learn.microsoft.com/en-us/power-platform/admin/vnet-support-overview) |
| `2.15` | D2 | Design Business Units, Modernized BUs, Owner Teams, Access Team Templates, & Entra Group Teams | 2 | 12 | [Design Business Units, Modernized BUs, Owner/Access Teams, & Entra Group Teams](https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges) |
| `2.16` | D2 | Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | 3 | 18 | [Design Security Roles, Column/Hierarchy security, and security governance](https://learn.microsoft.com/en-us/power-platform/admin/field-level-security) |
| `2.17` | D2 | Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | 3 | 18 | [Identify Entra ID groups/App Registrations, DLP policies, and external user access](https://learn.microsoft.com/en-us/power-pages/security/authentication/overview) |
| `3.1` | D3 | Evaluate detailed designs and implementations with Solution Checker, App Checker, & Well-Architected | 2 | 12 | [Evaluate detailed designs with Solution Checker, App Checker, & Well-Architected](https://learn.microsoft.com/en-us/power-platform/alm/use-powershell-cmdlets-solution-checker) |
| `3.2` | D3 | Review security across Business Rules, Security Roles, Entra Conditional Access, & security boundaries | 2 | 12 | [Review end-to-end security across Business Rules, Roles, Entra ID, & boundaries](https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview) |
| `3.3` | D3 | Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | 3 | 18 | [Ensure conformance to Dataverse Service Protection & Power Platform API limits](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits) |
| `3.4` | D3 | Assess storage/resource impact and resolve automation loops, race conditions, & integration conflicts | 2 | 12 | [Assess storage/resource impact and resolve automation & integration conflicts](https://learn.microsoft.com/en-us/power-platform/admin/capacity-storage) |
| `3.5` | D3 | Identify and resolve Canvas, Model-driven, Quick Find index, and synchronous plug-in performance issues | 2 | 12 | [Identify and resolve Canvas, Model-driven, Dataverse, & plug-in performance issues](https://learn.microsoft.com/en-us/power-platform/well-architected/performance-efficiency/overview) |
| `3.6` | D3 | Escalate and resolve data migration bottlenecks (BypassCustomPluginExecution, delta loads, reconciliation) | 2 | 12 | [Escalate and remediate enterprise data migration bottlenecks and cutover issues](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/TVF-override-plugin-execution) |
| `3.7` | D3 | Resolve deployment plan issues, Unmanaged Active Solution Layers, and circular solution dependencies | 2 | 12 | [Resolve deployment plan, Solution Layer, and pipeline dependency issues](https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm) |
| `3.8` | D3 | Identify go-live readiness gates, execute Administration mode cutovers, and manage hypercare telemetry | 2 | 12 | [Assess go-live readiness factors, Administration mode, and hypercare remediation](https://learn.microsoft.com/en-us/power-platform/admin/admin-mode) |

## Original Multi-Question Case Studies (24 Case Studies = 72 Case Items)

| Set | Case Study 1 | Case Study 2 | Case Study 3 | Case Study 4 |
| :---: | :--- | :--- | :--- | :--- |
| **Set 1** | SovereignCrest Private Bank (`3 Qs`) | Alderbrook Commercial Leasing (`3 Qs`) | Vespera Wealth Portal (`3 Qs`) | Monarch Clearing Services (`3 Qs`) |
| **Set 2** | HavenBridge Health System (`3 Qs`) | CareStride Home Nursing (`3 Qs`) | MedVantage Imaging Services (`3 Qs`) | Aegis Clinical Trials (`3 Qs`) |
| **Set 3** | StratosWing Aerospace (`3 Qs`) | Kinetix Heavy Equipment (`3 Qs`) | Vortex Turbine Aftermarket (`3 Qs`) | IronPeak Plant Rollout (`3 Qs`) |
| **Set 4** | MetroCivic Permitting Authority (`3 Qs`) | Valor Disaster Relief Agency (`3 Qs`) | Keystone State Licensing (`3 Qs`) | CivicPulse Transit Network (`3 Qs`) |
| **Set 5** | Luminary Luxury Retail (`3 Qs`) | FreshBasket Grocery Chain (`3 Qs`) | OmniCart Fulfillment Hub (`3 Qs`) | Solstice Peak Commerce (`3 Qs`) |
| **Set 6** | GridVantage Transmission (`3 Qs`) | EcoLedger Carbon Exchange (`3 Qs`) | ApexGrid M&A Integration (`3 Qs`) | Boreal Hydro Operations (`3 Qs`) |
