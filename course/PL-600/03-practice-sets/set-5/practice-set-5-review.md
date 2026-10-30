# Microsoft Exam PL-600: Practice Exam 5 — Global Retail Omnichannel, Storage Tiering & ETag Concurrency — Reviewer Study Key

**Theme:** Organization vs User/Team ownership & Access Teams, File/Blob capacity offloading, ETag optimistic concurrency, and Application Insights KQL  
**Credential:** Microsoft Certified: Power Platform Solution Architect Expert (`One active Associate certification required: Microsoft Certified: Power Platform Functional Consultant Associate (PL-200) OR Microsoft Certified: Power Platform Developer Associate (PL-400)`)  
**Study guide baseline:** September 23, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-600)  
**Lifecycle notice:** Exam PL-600 retired on June 30, 2026; succeeded by `Exam AB-100: Agentic AI Business Solutions Architect (Microsoft Certified: Agentic AI Business Solutions Architect Expert)`.  
**Questions:** `100` (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice percentages do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`E5Q093`) — Implement the solution [3.5] · *Single-Answer Multiple Choice*

Store associates report a Canvas `Product Finder` screen takes 19 seconds to load because `App.OnStart` downloads 45,000 rows sequentially into local collections before rendering Screen 1. How should you remediate startup latency?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Fixing slowness via delegable `Filter`/`StartsWith` Canvas queries, indexed `Quick Find` columns (no leading `*` wildcards), & async plug-in refactoring
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Moving non-blocking data fetches out of `App.OnStart` (using `App.StartScreen`, `Concurrent()` for small lookups, and server-side **delegable `Filter`/`StartsWith` Dataverse views** instead of caching 45,000 rows client-side) cuts cold start to under 2 seconds. [Skill 3.5: Identify and resolve Canvas, Model-driven, Quick Find index, and synchronous plug-in performance issues | Source: Identify and resolve Canvas, Model-driven, Dataverse, & plug-in performance issues (https://learn.microsoft.com/en-us/power-platform/well-architected/performance-efficiency/overview)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Correct. Eliminating `N+1` gallery `LookUp`s, non-delegable predicates, leading-wildcard full table scans, and chained sync plug-ins restores sub-second UX.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q002 (`E5Q008`) — Perform solution envisioning and requirement analysis [1.3] · *Single-Answer Multiple Choice*

Every Sunday night, a dynamic markdown optimization engine solves linear-programming price elasticities across 400,000 SKUs × 1,100 stores for 22 minutes in Python/C++ before writing recommended markdowns to Dataverse. Where should this optimization run?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Azure pro-code extension (`Azure Functions`, `Service Bus`, `AKS`, or `Azure AI Foundry`) integrated with Power Platform
- **D.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Compute workloads exceeding Dataverse’s 2-minute sandbox limit (`22 minutes` of mathematical optimization) belong in Azure pro-code compute (`Azure Batch` / `AKS` / `Azure Functions`) integrated asynchronously. [Skill 1.3: Identify and select components from existing apps, Dynamics 365, AppSource ISVs, and Azure | Source: Evaluate Dynamics 365 apps, AppSource ISVs, and Azure extensions (https://learn.microsoft.com/en-us/training/modules/discover-customer-needs/)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Correct. Heavy compute, long-running algorithms (> 2 minutes), and high-throughput brokered messaging offload cleanly to Azure extensions.
- **D:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.

</details>

### Q003 (`E5Q032`) — Perform solution envisioning and requirement analysis [1.13] · *Multi-Select (Select 3)*

A global Black Friday order-exception workbench undergoes architecture sign-off. Which three items must be captured as **Non-Functional Requirements (`NFRs`)**? Select three.

- **A.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **B.** Designing for `WCAG 2.1 AA` accessibility (`AccessibleLabel`, `TabIndex`, contrast) and `.resx` multi-language localization
- **C.** Capturing Non-Functional Requirements (`RPO`/`RTO`, peak concurrency, `p95` latency, API volume, `WCAG 2.1 AA`, & retention)
- **D.** Power Platform Well-Architected `Reliability` pillar (RPO/RTO targets, fault isolation, retries, & circuit breakers)
- **E.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **F.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C, D` (`CSV: 2,3,4`)

Correct answers: B, C, and D (are correct). Peak Black Friday concurrency, sub-second `p95` latency, API throughput, & 7-year fiscal retention (`req_nfr_spec`), `99.95%` availability & `RPO`/`RTO` resilience (`wa_reliability`), and `WCAG 2.1 AA` accessibility + 11-language `.resx` localization (`ux_wcag_accessible`) are core NFRs. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Incorrect. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **B:** Correct. Building accessibility and localization into initial UX components avoids expensive retrofits before public or enterprise launch.
- **C:** Correct. Non-functional requirements govern architectural sizing, BCDR, licensing capacity, offline design, and security controls.
- **D:** Correct. The Reliability pillar ensures mission-critical workloads withstand transient outages, throttling, and regional faults within defined RPO/RTO bounds.
- **E:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **F:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q004 (`E5Q030`) — Perform solution envisioning and requirement analysis [1.12] · *Single-Answer Multiple Choice*

Which specification belongs in the **Functional Requirements** document for a franchise store-audit solution?

- **A.** Capturing Functional Requirements (persona workflows, state rules, approvals, offline CRUD scope, & statutory reports)
- **B.** Conforming to `Dataverse Service Protection` limits (`6,000` req / `20m` compute per `5-min` window), pooling `S2S Application Users`, & honoring `Retry-After`
- **C.** Capturing Non-Functional Requirements (`RPO`/`RTO`, peak concurrency, `p95` latency, API volume, `WCAG 2.1 AA`, & retention)
- **D.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Weighted food-safety scoring formulas, automatic critical-violation re-inspection scheduling, and regional director sign-off workflows define functional requirements (`req_functional_spec`). [Skill 1.12: Identify functional requirements across personas, business rules, approvals, and offline access | Source: Identify functional requirements across personas, offline, and workflows (https://learn.microsoft.com/en-us/power-apps/mobile/setup-mobile-offline)]

- **A:** Correct. Functional requirements specify what business behaviors and data transformations the solution must perform for each role.
- **B:** Incorrect. Service Protection enforces per-user/per-web-server 5-minute sliding caps (`HTTP 429`); pooling S2S Application Users and respecting `Retry-After` maximizes throughput.
- **C:** Incorrect. Non-functional requirements govern architectural sizing, BCDR, licensing capacity, offline design, and security controls.
- **D:** Incorrect. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.

</details>

### Q005 (`E5Q055`) — Architect a solution [2.5] · *Ordered Sequence (Multiple Choice)*

A retail acquisition requires migrating 6 million `Loyalty_Members`, `Households`, `Gift_Cards`, and circular `Primary_Member <-> Household` lookups into Dataverse without firing marketing SMS flows or randomizing tier-config GUIDs. Which four-step migration sequence should you execute?

- **A.** Cleanse & stage data with Alternate Keys / CMT GUIDs → Suppress non-essential flows & custom plug-ins → Load parent tables first (deferring circular lookups) → Bind deferred lookups, reconcile counts, & re-enable automations
- **B.** Execute `INSERT INTO account` over Dataverse TDS port 5558 → Remove platform SQL foreign keys → Copy `.mdf` database files from Azure SQL → Reboot the tenant
- **C.** Load child line-items before parent Account rows exist → Leave all welcome-email cloud flows enabled → Run single-row serial inserts with no batching → Fix orphaned lookups manually in Prod
- **D.** Let each environment generate random GUIDs for reference/configuration tables → Hardcode Dev GUIDs inside cloud flows → Import raw unvalidated CSVs → Skip reconciliation

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Staging cleansed data with Alternate Keys & CMT fixed GUIDs, suppressing flows & custom plug-ins, loading parents first (deferring circular household lookups), and binding deferred lookups before reconciling counts ensures clean cutover. [Skill 2.5: Design enterprise data migration strategies, load sequencing, Alternate Keys, and CMT tooling | Source: Design enterprise data migration strategies, load order, and tooling (https://learn.microsoft.com/en-us/power-platform/admin/create-schema-export-data)]

- **A:** Correct. Enterprise migrations stage cleansed data, suppress noisy automations (`BypassCustomPluginExecution`), load parents before children while resolving circular lookups in a second pass, and reconcile counts before re-enabling flows.
- **B:** Incorrect. Dataverse’s TDS endpoint (`5558`) is strictly read-only; all writes must use Dataverse Web API/SDK, Dataflows, ADF, or Configuration Migration Tool.
- **C:** Incorrect. Loading child rows first fails referential integrity, and leaving notification flows active spams thousands of customers.
- **D:** Incorrect. Mismatched reference-data GUIDs across Dev, UAT, and Prod break business rules, views, and workflow conditions.

</details>

### Q006 (`E5Q060`) — Architect a solution [2.7] · *Single-Answer Multiple Choice*

Guiding real-estate teams through `Site Nominated -> Demographics Study -> Lease Negotiation -> Store Buildout -> Grand Opening` across `Site_Candidate` and `Store_Lease` tables uses `____`.

- **A.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A multi-table **Business Process Flow (`BPF`)** enforces consistent cross-table stage gates and approvals across store-opening lifecycles. [Skill 2.7: Design automation strategies (sync vs async, BPF, Logic Apps) and multi-environment ALM topology | Source: Design automation & multi-environment strategies (CoE Starter Kit & ALM) (https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit)]

- **A:** Correct. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q007 (`E5Q010`) — Perform solution envisioning and requirement analysis [1.4] · *Single-Answer Multiple Choice*

Rather than loading 16 billion historical POS basket-line items (`2014–2025`) into Dataverse Database capacity just so data scientists can calculate affinity cohorts, which architectural alternative should you recommend?

- **A.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Retaining multi-billion POS basket lines in **Microsoft Fabric OneLake** (writing only summarized customer segments/RFM scores into Dataverse via Dataflows/Reverse ETL) keeps Dataverse lean and fast. [Skill 1.4: Identify and estimate data migration and integration efforts, complexity drivers, and alternatives | Source: Estimate migration and integration efforts and alternatives (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Correct. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.

</details>

### Q008 (`E5Q024`) — Perform solution envisioning and requirement analysis [1.9] · *Single-Answer Multiple Choice*

Modeling VIP shoppers as `Contact`, wholesale corporate buyers as `Account`, and boutique styling appointments as `Appointment` / `Activity` aligns retail schemas with `____`.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Aligning data entities to the Microsoft Common Data Model (`CDM`) standard tables (`Account`, `Contact`, `Activity`)
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Aligning with the Microsoft Common Data Model (`CDM`) ensures seamless compatibility with Dynamics 365 Customer Insights, Sales, Exchange sync, and AppSource ISVs. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Correct. Extending standard CDM tables preserves native Dynamics 365, AppSource ISV, Exchange, and AI Copilot interoperability.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q009 (`E5Q071`) — Architect a solution [2.12] · *Single-Answer Multiple Choice*

Unreleased haute-couture runway sketches attached to Dataverse `Collection_Brief` rows leaked when general intranet users browsed the default SharePoint Document Management library. How do you enforce Dataverse row ACLs on those files?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **C.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **D.** Mitigating SharePoint Document Management’s lack of automatic Dataverse ACL sync via Dataverse `File` columns, Azure Blob SAS, or custom ACL sync

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Storing confidential sketches in native **Dataverse `File` / `Image` columns** (or custom SAS-brokered Azure Blob containers) enforces exact Dataverse row and column Security Roles instead of open SharePoint folder ACLs. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **C:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **D:** Correct. Default SharePoint integration never copies Dataverse row permissions to SharePoint folders; confidential files require `File` columns or explicit ACL sync.

</details>

### Q010 (`E5Q021`) — Perform solution envisioning and requirement analysis [1.8] · *Single-Answer Multiple Choice*

When evaluating an acquired footwear brand whose store tablets still join an external MDM and separate Entra tenant, capturing identity trust and Conditional Access constraints belongs in `____`.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Enterprise Architecture Context Diagram mapping systems of record, Entra tenants, hybrid networks, & sync/async SLAs
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Documenting multi-tenant identity, device compliance, and network topologies inside the Enterprise Architecture Context Diagram prevents surprise rollout blockers. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Correct. Evaluating the enterprise landscape clarifies authoritative boundaries, identity federation, firewall paths, and integration patterns.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.

</details>

### Q011 (`E5Q013`) — Perform solution envisioning and requirement analysis [1.5] · *Single-Answer Multiple Choice*

Regional store-ops analysts want low-code agility to tweak visual merchandising checklists while global InfoSec governs POS APIs and PCI DSS boundaries. Defining `____` prevents ungoverned shadow deployments.

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Establishing a fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model balance regional agility with global PCI/InfoSec governance. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Clear architectural ownership, ARB design gates, and CoE guardrails align business, citizen makers, pro-devs, and InfoSec.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q012 (`E5Q042`) — Perform solution envisioning and requirement analysis [1.16] · *Single-Answer Multiple Choice*

Refrigeration maintenance contractors servicing 1,100 supermarkets need preventive maintenance plans, compressor `Customer Assets`, van parts inventory, and automated route dispatch (`RSO`). Which first-party app should you recommend?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Dynamics 365 first-party app (`Sales`, `Customer Service`, or `Field Service`) leveraging native schemas, SLAs, & RSO scheduling
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **Dynamics 365 Field Service** provides native `Work Orders`, `Customer Assets`, preventive agreements, van inventory, and `RSO` scheduling out of the box. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Correct. Adopting Dynamics 365 first-party apps avoids reinventing complex case routing, omnichannel queues, or Resource Scheduling Optimization.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q013 (`E5Q068`) — Architect a solution [2.11] · *Single-Answer Multiple Choice*

Store associates use Microsoft Teams on handheld devices and want instant VIP curbside-arrival notifications with inline `"Claim Handoff"` buttons updating Dataverse, while headquarters syncs Dynamics 365 Commerce/F&O customer masters near-real-time. Which capabilities fit best?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Integrating Microsoft Teams (`Adaptive Cards` / embedded apps), Dynamics 365 F&O `Dual-write` + `Business Events`, & `Server-Side Sync`
- **C.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **D.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Microsoft Teams **Adaptive Cards** plus **Dynamics 365 Dual-write** and **Business Events** unify frontline Teams collaboration with near-real-time ERP-Dataverse master sync. [Skill 2.11: Design collaboration (Teams, SharePoint ACL nuances, Exchange) and Dynamics 365 Dual-write integrations | Source: Design Teams, SharePoint, Exchange, and Dynamics 365 (Dual-write) integrations (https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dual-write/dual-write-overview)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Correct. Dual-write provides near-real-time bi-directional Dataverse-to-F&O sync, while Teams Adaptive Cards meet users directly in collaboration channels.
- **C:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **D:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.

</details>

### Q014 (`E5Q026`) — Perform solution envisioning and requirement analysis [1.10] · *Single-Answer Multiple Choice*

Marketing wants Dynamics 365 / AI Builder churn models trained on loyalty data where inactive accounts from closed stores were never flagged `Churned`. What must precede model training?

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **D.** Defining pre-cutover data quality standards (deduplication keys, mandatory completeness, referential integrity, & domain mappings)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Defining data quality standards and accurate outcome labeling for closed-store cohorts prevents skewed AI churn predictions. [Skill 1.10: Define use cases and data quality standards for existing data prior to migration or integration | Source: Define use cases and data quality standards for existing data (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **D:** Correct. Enforcing cleansing and deduplication gates before migration prevents garbage-in/garbage-out failures in Dataverse.

</details>

### Q015 (`E5Q062`) — Architect a solution [2.8] · *Single-Answer Multiple Choice*

Reassigning a flagship `Boutique_Store` record owning 250,000 historic `Styling_Session` child rows caused SQL lock timeouts because the `1:N` relationship used `Parental` cascading. Proposed solution: Reconfigure the relationship to `Custom` (`Cascade None` on `Assign`/`Share`/`Reparent` for historical closed sessions). Does this solve the timeout?

- **A.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Configuring `Custom` / `Referential` cascading (avoiding unintended `Parental` `Cascade All` reparent storms) and manual `N:N` intersect tables
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — replacing `Parental` (`Cascade All`) with `Custom` cascading stops synchronous 250,000-row update and `POA` sharing storms when store managers rotate. [Skill 2.8: Design Dataverse relationships (1:N, N:N, hierarchical, polymorphic) and cascading behaviors | Source: Design Dataverse relationships (1:N, N:N, hierarchical) & cascading behaviors (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Correct. Replacing `Parental` cascading on high-volume child tables prevents `POA` sharing storms, and manual `N:N` tables store rich relationship attributes.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q016 (`E5Q039`) — Perform solution envisioning and requirement analysis [1.15] · *Single-Answer Multiple Choice*

A web agency suggests modifying Power Pages’ internal Microsoft IIS container binaries directly to add custom payment routing. How must fit/gap review classify this?

- **A.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **B.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Structured Fit/Gap matrix scoring requirements across `Out-of-the-Box`, `Configuration`, `AppSource ISV`, & `Custom Code`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Pages runs as a Microsoft-managed PaaS service where underlying IIS host binaries are inaccessible/unsupported; fit/gap maps payment routing to supported Power Pages Web API / Cloud Flow / APIM patterns. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **B:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Correct. Formal fit/gap scoring exposes customization TCO, licensing impacts, and upgrade maintenance trade-offs transparently.

</details>

## Case Study Vignette — Luminary Luxury Retail

> Luminary Luxury Retail operates 600 boutiques across EMEA, Americas, and APAC with clienteling associates using mobile apps on store Wi-Fi. VIP client profiles are Organization-wide reference records vs regional `User/Team` clienteling notes, and regional marketing leads occasionally co-sell on flagship VIP accounts without changing primary BU ownership.

### Q017 (`E5Q066`) — Architect a solution [2.10] · *Single-Answer Multiple Choice*

Case study — Luminary Luxury Retail: Global ISO currency/size charts have identical visibility worldwide with zero BU security, whereas regional `Clienteling_Note` records require strict EMEA/Americas/APAC Business Unit isolation. How must table ownership be configured at creation time?

- **A.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Choosing `User or Team` table ownership for BU/row/team security vs `Organization` ownership for global config tables at creation time

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Create global size/currency reference tables with **`Organization` ownership** and `Clienteling_Note` with **`User or Team` ownership** from Day 1, because Dataverse table ownership cannot be changed after creation. [Skill 2.10: Design complex data models (ownership immutability, Elastic/Activity tables, binary storage offloading) | Source: Design complex data models (ownership, Elastic/Activity tables, storage capacity) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/elastic-tables)]

- **A:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Correct. Table ownership (`User/Team` vs `Organization`) is immutable once created and determines whether BU, Team, and Hierarchy security apply.

</details>

### Q018 (`E5Q077`) — Architect a solution [2.15] · *Single-Answer Multiple Choice*

Case study — Luminary Luxury Retail: Regional marketing leads occasionally co-sell on specific flagship VIP accounts alongside the primary boutique advisor without changing primary BU ownership or bloating `POA`, while global VIP directors need matrix access across both `EMEA` and `Americas` BUs. Which combination should you design?

- **A.** Combining `Modernized Business Units` (matrix access), `Microsoft Entra ID Security Group Teams`, & `Access Team Templates`
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). **Access Team Templates** handle ad-hoc co-selling on flagship VIP rows cleanly without `POA` bloat, while **Modernized Business Units** grant global directors matrix roles across `EMEA` and `Americas` without moving their home BU. [Skill 2.15: Design Business Units, Modernized BUs, Owner Teams, Access Team Templates, & Entra Group Teams | Source: Design Business Units, Modernized BUs, Owner/Access Teams, & Entra Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Correct. Modernized BUs enable cross-BU matrix roles, Entra Group Teams automate zero-touch RBAC, and Access Teams handle ad-hoc record collaboration cleanly.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q019 (`E5Q080`) — Architect a solution [2.16] · *Single-Answer Multiple Choice*

Case study — Luminary Luxury Retail: An older CRM instance suffered 11-second view queries because store staff manually clicked `"Share"` on 14 million styling notes, swelling `PrincipalObjectAccess` (`POA`) to 110 million rows. Which architectural rule prevents `POA` bloat?

- **A.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Preventing `PrincipalObjectAccess (POA)` table bloat by replacing manual per-record sharing and `Parental` cascades with `Access Team Templates`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Eliminating manual user-level record sharing and `Parental` cascades in favor of **Access Team Templates** and **Entra Security Group Teams** maintains `POA` table hygiene. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Correct. Millions of `POA` rows from manual sharing and `Cascade All` relationships degrade SQL query performance across Dataverse views.

</details>

### Q020 (`E5Q048`) — Architect a solution [2.1] · *Single-Answer Multiple Choice*

Why should `Customer`, `Store`, and `Product` table definitions live in a dedicated `Retail_Base` Managed Solution rather than being duplicated inside both `Clienteling_App` and `Concierge_App` unmanaged exports?

- **A.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Isolating shared core tables inside a foundational `Retail_Base` Managed Solution prevents cross-tribe lock contention, circular dependencies, and bloated solution imports. [Skill 2.1: Design segmented solution topology, custom Publisher strategy, and Managed Environments | Source: Design solution topology, publisher segmentation, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/alm/segmented-solutions-alm)]

- **A:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q021 (`E5Q028`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

Specifying `Given receipt age <= 30 days and tag attached = true, When associate scans return barcode, Then full original-tender refund auto-approves` establishes verifiable `____`.

- **A.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **B.** Refining prescriptive wishes into persona-based `User Stories` (`As a ... I need ... so that ...`) with testable Acceptance Criteria
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Structured `Given / When / Then` Acceptance Criteria define unambiguous return-policy boundaries for makers and automated tests. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **B:** Correct. Outcome-oriented User Stories decouple business intent from premature UI assumptions and anchor QA test cases.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q022 (`E5Q072`) — Architect a solution [2.13] · *Single-Answer Multiple Choice*

When a boutique manager requests a high-value fraud override via a custom connector to an internal Risk API, compliance logs must capture the **exact signed-in manager’s Entra identity**, whereas nightly catalog sync runs headlessly. Which auth pairing applies?

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Using `OAuth 2.0 On-Behalf-Of (OBO)` to preserve caller identity/audit trails vs `Entra Service Principal (S2S)` / `Managed Identity` for background jobs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Use **`OAuth 2.0 On-Behalf-Of (OBO)`** delegated auth for the interactive manager fraud override and **`Entra Service Principal (S2S)` / `Managed Identity`** for the headless catalog sync. [Skill 2.13: Design authentication (OBO vs S2S, Managed Identity), BCDR (RPO/RTO, geo-backups), and RPA | Source: Design authentication (OBO vs S2S, Managed Identity), BCDR, and RPA architectures (https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Correct. OBO propagates the signed-in user’s identity downstream for row-level authorization, whereas S2S/Managed Identity runs headless workloads.

</details>

### Q023 (`E5Q044`) — Perform solution envisioning and requirement analysis [1.17] · *Single-Answer Multiple Choice*

To let POS registers, Power Pages portals, and Canvas clienteling apps invoke one authoritative server-side `RedeemLoyaltyPoints` transaction inside Dataverse via a strongly typed OData action, you should create a `____`.

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Defining solution-aware Dataverse `Custom APIs` exposing strongly typed request/response contracts for internal and external callers
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A solution-aware Dataverse **`Custom API`** exposes a versioned, privilege-checked server-side message callable consistently across POS, web, and mobile clients. [Skill 1.17: Address functional gaps through supported low-code/pro-code alternate solutions | Source: Address functional gaps through low-code/pro-code alternate solutions (https://learn.microsoft.com/en-us/power-platform/well-architected/operational-excellence/overview)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Correct. Custom APIs replace legacy Custom Process Actions with code-first, solution-aware OData bound/unbound operations and granular privilege checks.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q024 (`E5Q037`) — Perform solution envisioning and requirement analysis [1.15] · *Ordered Sequence (Multiple Choice)*

A retail enterprise evaluates 175 omnichannel service and loyalty requirements. Which four-step fit/gap evaluation sequence keeps customization TCO lowest across Microsoft release waves?

- **A.** Inject unsupported DOM-scraping JavaScript into Model-driven forms → Modify SQL indexes directly via TDS → Bypass security roles → Lock out Microsoft updates
- **B.** Validate each requirement against out-of-the-box Dataverse & Dynamics 365 capabilities → Evaluate declarative low-code configuration → Assess vetted AppSource ISV solutions → Specify targeted pro-code extensions only for remaining gaps
- **C.** Build bespoke React SPAs and C# plug-ins for every requirement first → Replace standard Dynamics 365 tables with custom tables → Ignore AppSource → Check standard features last
- **D.** Accept every stakeholder wish into Phase 1 without feasibility scoring → Skip MVP boundaries → Hardcode workarounds in Production → Defer licensing impact checks until billing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Validating native Dataverse/Dynamics 365 features first, then declarative low-code configuration, then vetted AppSource ISVs, and finally targeted pro-code extensions protects upgradeability and TCO. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Unsupported DOM manipulation and direct SQL writes violate Microsoft supportability contracts and break on wave updates.
- **B:** Correct. Fit/gap analysis prioritizes standard platform/Dynamics 365 features first, then declarative configuration, then supported AppSource ISVs, reserving custom code strictly for true differentiators.
- **C:** Incorrect. Defaulting to custom code and duplicating restricted/standard Dynamics 365 tables inflates TCO and breaks product upgrades.
- **D:** Incorrect. Unbounded scope acceptance without feasibility or licensing evaluation derails timelines and budgets.

</details>

### Q025 (`E5Q049`) — Architect a solution [2.2] · *Single-Answer Multiple Choice*

Boutique stylists want to test one-handed iPhone ergonomics on simulated VIP lookbook screens before developers write custom code. How should you validate UX first?

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Validating interactive UX prototypes (`Figma-to-App` / `Custom Pages`) early and building `PCF` controls for specialized UI gaps
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Validating interactive `Figma` / rapid Canvas prototypes on iPhones with boutique stylists confirms thumb-reach ergonomics cheaply before building specialized `PCF` controls. [Skill 2.2: Identify app customization approaches and validate interactive user experience prototypes | Source: Select customization approaches for existing apps and validate UX prototypes (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/design-consistency)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Interactive prototyping validates user journeys cheaply, while Power Apps Component Framework (`PCF`) renders reusable custom TypeScript/React controls.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q026 (`E5Q018`) — Perform solution envisioning and requirement analysis [1.7] · *Single-Answer Multiple Choice*

Comparing pre-launch seasonal stockout resolution times (`36 hours`) against post-launch telemetry (`2.5 hours`) across 600 boutiques validates `____`.

- **A.** Defining baseline-backed `SMART` success KPIs (cycle-time reduction, error-rate drop, SLA adherence, & active adoption %)
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Tracking post-launch operational metrics against pre-launch baselines verifies achievement of agreed `SMART` KPIs. [Skill 1.7: Review and validate measurable key success criteria, KPIs, and adoption targets | Source: Review measurable key success criteria, KPIs, and adoption targets (https://learn.microsoft.com/en-us/power-platform/guidance/adoption/measure-business-value)]

- **A:** Correct. Quantifiable KPIs anchored to current-state baselines let stakeholders verify objective ROI after go-live.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q027 (`E5Q003`) — Perform solution envisioning and requirement analysis [1.1] · *Single-Answer Multiple Choice*

Store associates standing beside shoppers need a 2-tap clienteling lookup screen with zero horizontal scrolling and instant sizing badges. Optimizing this low-friction boutique interaction aligns with the Well-Architected `____` pillar.

- **A.** Power Platform Well-Architected `Security` pillar (Zero Trust Entra identity, least privilege, DLP, & encryption)
- **B.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)
- **C.** Power Platform Well-Architected `Operational Excellence` pillar (automated ALM pipelines, Application Insights, & CoE)
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Experience Optimization` streamlines persona-centered task flows, tactile ergonomics, and visual clarity. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Incorrect. The Security pillar protects confidentiality and integrity through Entra Conditional Access, least-privilege roles, DLP endpoint rules, and CMK/Lockbox.
- **B:** Correct. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.
- **C:** Incorrect. Operational Excellence standardizes CI/CD solution pipelines, automated Solution Checker gates, telemetry, and Managed Environment governance.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q028 (`E5Q017`) — Perform solution envisioning and requirement analysis [1.7] · *Single-Answer Multiple Choice*

A Chief Merchandising Officer says: `"Make vendor onboarding effortless this quarter."` Which rewritten target serves as a valid architectural key success criterion?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Defining baseline-backed `SMART` success KPIs (cycle-time reduction, error-rate drop, SLA adherence, & active adoption %)
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Baseline-anchored `SMART` KPIs (such as reducing vendor setup lead time from `21 days` to `< 48 hours`, cutting SKU attribute rejection rates below `1.5%`, and reaching `90%` vendor portal self-service in 60 days) measure real success. [Skill 1.7: Review and validate measurable key success criteria, KPIs, and adoption targets | Source: Review measurable key success criteria, KPIs, and adoption targets (https://learn.microsoft.com/en-us/power-platform/guidance/adoption/measure-business-value)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Correct. Quantifiable KPIs anchored to current-state baselines let stakeholders verify objective ROI after go-live.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q029 (`E5Q075`) — Architect a solution [2.14] · *Single-Answer Multiple Choice*

To prevent compromised store-associate credentials from accessing Dataverse outside store SD-WAN NAT IPs or unmanaged personal phones, enforce `____`.

- **A.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Enforcing `Microsoft Entra Conditional Access` (MFA & compliant device) plus `Power Platform IP Firewall` & `Cookie IP binding`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). **Microsoft Entra Conditional Access** (Intune-compliant device + MFA) combined with Managed Environment **Power Platform IP Firewall** and **Cookie IP binding** blocks unauthorized network/device access. [Skill 2.14: Assess VNet subnet delegation, Azure ExpressRoute nuances, Data Gateways, and IP firewall networking | Source: Assess VNet integration, Azure ExpressRoute, gateways, and IP firewall networking (https://learn.microsoft.com/en-us/power-platform/admin/vnet-support-overview)]

- **A:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Correct. Combining Entra Conditional Access with Managed Environment IP Firewall and session cookie binding blocks token replay from untrusted networks.

</details>

### Q030 (`E5Q087`) — Implement the solution [3.2] · *Single-Answer Multiple Choice*

Proposed solution: Use an `Entity`-scoped Business Rule to prevent store cashiers from reading wholesale `Supplier_Margin` columns via Excel Online export. Does this protect `Supplier_Margin`?

- **A.** Auditing server-side `Security Roles`, `Column Security`, & `Power Pages Table Permissions` rather than trusting client-side UI rules
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). No — Business Rules (`Form` or `Entity` scope) never restrict `Read` access over OData, Excel export, or Power BI; enable a **Column Security Profile** on `Supplier_Margin`. [Skill 3.2: Review security across Business Rules, Security Roles, Entra Conditional Access, & security boundaries | Source: Review end-to-end security across Business Rules, Roles, Entra ID, & boundaries (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Correct. Client JavaScript and `Form`-scoped Business Rules never block Web API/OData access; security boundaries must be enforced server-side in Dataverse.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.

</details>

### Q031 (`E5Q014`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

A luxury conglomerate operates boutiques in Mainland China (`21Vianet`), the European Union (`GDPR`), and North America, with strict cross-border personal-data transfer prohibitions. Which risk assessment must precede tenant/environment architecture?

- **A.** Assessing sovereign data-residency (`Multi-Geo`), PII/PHI/ITAR compliance, `CMK`, & cross-border connector risks upfront
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Sovereign cloud (`China 21Vianet` sovereign tenant isolation vs global `Multi-Geo` environments), `GDPR` residency, `CMK`, and cross-border connector restrictions must be architected upfront. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Correct. Identifying residency and regulatory encryption constraints during envisioning prevents illegal cross-region tenant/environment placement.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q032 (`E5Q078`) — Architect a solution [2.16] · *Multi-Select (Select 3)*

A luxury retail tenant requires: (1) masking `Annual_UHNW_Spend` and `Passport_Number` from regular cashiers, (2) zero standing Production `System Administrator` accounts, and (3) customer-controlled encryption keys (`CMK`) + Lockbox approval. Which three security layers apply? Select three.

- **A.** Power Platform Well-Architected `Security` pillar (Zero Trust Entra identity, least privilege, DLP, & encryption)
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access
- **D.** Enforcing `Microsoft Entra Conditional Access` (MFA & compliant device) plus `Power Platform IP Firewall` & `Cookie IP binding`
- **E.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **F.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C, D` (`CSV: 1,3,4`)

Correct answers: A, C, and D (are correct). `Column Security Profiles` + `Microsoft Entra PIM` just-in-time elevation + `CMK` / `Customer Lockbox` (`sec_col_hier_pim`), `Entra Conditional Access` + IP Firewall (`sec_cond_access_ip`), and Zero Trust `Security` pillar governance (`wa_security`) protect UHNW client PII. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Correct. The Security pillar protects confidentiality and integrity through Entra Conditional Access, least-privilege roles, DLP endpoint rules, and CMK/Lockbox.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.
- **D:** Correct. Combining Entra Conditional Access with Managed Environment IP Firewall and session cookie binding blocks token replay from untrusted networks.
- **E:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **F:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q033 (`E5Q022`) — Perform solution envisioning and requirement analysis [1.9] · *Ordered Sequence (Multiple Choice)*

A retail group holds master SKU hierarchies in PIM, live inventory counts in Manhattan WMS, and VIP preferences in Salesforce. In what four-step sequence should you evaluate data sources before modeling Dataverse?

- **A.** Expose on-premises SQL Server ports directly to the public internet → Share one SQL `sa` login across Canvas apps → Skip data classification → Disable Dataverse auditing
- **B.** Duplicate 100% of ERP tables into Dataverse nightly → Ignore master-data ownership → Allow dual uncoordinated edits without conflict rules → Cleanse duplicates manually after go-live
- **C.** Inventory candidate enterprise data sources & owners → Classify data sensitivity, residency, & compliance rules → Assess data quality, volume, & latency needs → Decide per entity whether to connect in place or replicate into Dataverse
- **D.** Email daily CSV exports between departments → Let business units invent conflicting customer IDs → Skip deduplication standards → Import dirty spreadsheets straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Inventorying owners first, classifying PII/PCI sensitivity & residency, assessing quality/volume/latency, and choosing virtual in-place lookups vs Dataverse replication per entity protects master integrity. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Incorrect. Exposing raw database ports and sharing `sa` logins violates zero-trust security and bypasses Dataverse governance.
- **B:** Incorrect. Blindly duplicating authoritative ERP tables without master-data ownership or conflict governance causes severe data drift.
- **C:** Correct. Architects identify authoritative systems of record first, classify regulatory sensitivity/residency, evaluate quality/volume/latency, and then choose virtual in-place access vs Dataverse replication.
- **D:** Incorrect. Manual CSV emailing without canonical keys or data quality standards corrupts downstream analytics and automations.

</details>

### Q034 (`E5Q074`) — Architect a solution [2.14] · *Single-Answer Multiple Choice*

Dataverse plug-ins calculating real-time tax and fraud scores must reach an internal Azure Kubernetes Service (`AKS`) microservice exposed exclusively on an Azure Private Link / VNet subnet (`10.60.2.0/24`) without VM gateways. Enabling `____` provides native private routing.

- **A.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **B.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources
- **C.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **Virtual Network (`VNet`) support for Power Platform** (`enterprisePolicies` subnet delegation) routes outbound Dataverse plug-in and connector calls directly into the private VNet subnet. [Skill 2.14: Assess VNet subnet delegation, Azure ExpressRoute nuances, Data Gateways, and IP firewall networking | Source: Assess VNet integration, Azure ExpressRoute, gateways, and IP firewall networking (https://learn.microsoft.com/en-us/power-platform/admin/vnet-support-overview)]

- **A:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **B:** Correct. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.
- **C:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **D:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.

</details>

### Q035 (`E5Q079`) — Architect a solution [2.16] · *Single-Answer Multiple Choice*

Regional Retail VPs need automatic read visibility across `Country Director -> District Manager -> Boutique Manager -> Stylist` positions up to 4 levels deep. Configuring `____` provides this natively.

- **A.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Dataverse **Position / Manager Hierarchy Security** enforces multi-level retail reporting visibility without custom sharing plug-ins. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.

</details>

### Q036 (`E5Q088`) — Implement the solution [3.3] · *Ordered Sequence (Multiple Choice)*

During Cyber Monday load rehearsals, OMS-to-Dataverse order sync jobs encounter bursts of `HTTP 429` throttling. Which four-step remediation sequence resolves Service Protection limits cleanly?

- **A.** Move bulk integration loops inside synchronous Dataverse plug-ins → Chain 8 child plug-in updates per row → Enable `RetrieveAllEntities` metadata calls on every transaction → Disable caching
- **B.** Buy 100 Power BI Free licenses expecting them to lift 5-minute Service Protection caps → Hardcode personal maker credentials → Ignore `x-ms-ratelimit-time-remaining-xrm-requests` headers → Discard throttled records silently
- **C.** Pinpoint throttled callers in Dataverse API analytics → Batch writes via `CreateMultiple` / `$batch` & use Change Tracking → Pool high-volume S2S loads across Entra Application Users → Honor HTTP `429` `Retry-After` backoff
- **D.** Spin up 50 parallel threads under one single user account → Retry HTTP 429 errors immediately with 0 ms delay → Replace filtered queries with full `SELECT *` scans → Open a ticket asking Microsoft to disable platform limits permanently

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Inspecting API analytics, batching with `CreateMultiple`/`UpdateMultiple`/`$batch` & Change Tracking, pooling S2S Application Users, and honoring `HTTP 429` `Retry-After` headers resolves throttling. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Heavy metadata calls and chained synchronous updates multiply execution time against the 20-minute per-5-minute sliding window limit.
- **B:** Incorrect. Service Protection limits protect real-time platform stability per user/web server over 5-minute windows regardless of license SKU.
- **C:** Correct. Resolving Service Protection (`6,000` req / `20` min compute per 5-min window) combines batch/bulk operations, Change Tracking, pooled S2S Application Users where appropriate, and honoring `Retry-After` backoff.
- **D:** Incorrect. Immediate zero-delay retries under a single user identity amplify `HTTP 429` throttling and extend penalty windows.

</details>

### Q037 (`E5Q064`) — Architect a solution [2.9] · *Single-Answer Multiple Choice*

Why must active `Store_Audit_Checklist` rows edited by freezer inspectors during Wi-Fi blackouts reside in **native Dataverse tables** instead of Virtual Tables?

- **A.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **B.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **C.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **D.** Replicating data into native Dataverse tables (`Dataflows` / `ADF`) when Mobile Offline, row-level security roles, auditing, or SLAs are required

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Virtual Tables do not support `Mobile Offline` read/write synchronization, `User/Team` row ownership security, or native Dataverse column auditing. [Skill 2.9: Determine when to connect external data in place (Virtual tables) versus import/replicate into Dataverse | Source: Connect external data in place (Virtual tables) vs import/replicate into Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-virtual-entities)]

- **A:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **B:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **C:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **D:** Correct. Virtual tables do not support Mobile Offline sync, Dataverse row-level User/Team ownership, or native column auditing.

</details>

### Q038 (`E5Q081`) — Architect a solution [2.17] · *Multi-Select (Select 2)*

Retail InfoSec must: (1) block makers from connecting `Microsoft Dataverse` to personal file-sharing connectors via DLP while filtering the `HTTP` connector strictly to `api.omnicart.internal`, and (2) enable 1.2 million loyalty shoppers to view points online without Entra B2B guest seats. Which two designs apply? Select two.

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Enforcing `DLP` + `Endpoint Filtering`, licensing external consumers via `Power Pages` (`Entra External ID`), & `Entra B2B` for internal-app guests
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **E.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Tenant **DLP + Connector Endpoint Filtering** (`sec_dlp_ext_access`) blocks exfiltration, while **Microsoft Power Pages** with `Entra External ID` + `Contact`-scoped `Table Permissions` (`comp_power_pages` & `sec_dlp_ext_access`) scales to 1.2M external shoppers. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Correct. Power Pages scales cost-effectively with `Table Permissions` for external portals, whereas Entra B2B suits external partners using internal apps.
- **C:** Correct. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **E:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.

</details>

### Q039 (`E5Q036`) — Perform solution envisioning and requirement analysis [1.14] · *Single-Answer Multiple Choice*

Harmonizing 9 acquired supermarket banners onto one canonical supplier-chargeback dispute workflow before configuring Dataverse BPFs represents `____`.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **C.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Standardizing fragmented banner processes first eliminates nine-way conditional sprawl and unifies executive KPIs. [Skill 1.14: Guide future-state business process optimization and standardization before automating | Source: Guide future-state business process optimization and standardization (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **C:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q040 (`E5Q043`) — Perform solution envisioning and requirement analysis [1.17] · *Multi-Select (Select 2)*

Visual merchandisers need: (1) an interactive store-planogram shelf-layout canvas rendered directly on a Model-driven `Store_Campaign` form, and (2) Power Fx calculated margin-tier columns evaluated automatically across related SKU lookups. Which two supported extensibility options fit best? Select two.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Validating interactive UX prototypes (`Figma-to-App` / `Custom Pages`) early and building `PCF` controls for specialized UI gaps
- **D.** Addressing gaps via supported extensibility (`Custom Pages`, `PCF`, `Power Fx Formula columns`, `Custom APIs`) over bespoke clones
- **E.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, D` (`CSV: 3,4`)

Correct answers: C and D (are correct). A **PCF** control (`ux_proto_pcf`) renders interactive SVG/React planogram shelves natively on forms, while **Power Fx Formula columns** (`gap_lowcode_alt`) calculate related-table margin tiers declaratively. [Skill 1.17: Address functional gaps through supported low-code/pro-code alternate solutions | Source: Address functional gaps through low-code/pro-code alternate solutions (https://learn.microsoft.com/en-us/power-platform/well-architected/operational-excellence/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Correct. Interactive prototyping validates user journeys cheaply, while Power Apps Component Framework (`PCF`) renders reusable custom TypeScript/React controls.
- **D:** Correct. Supported platform extensibility closes UX and logic gaps while preserving Microsoft wave-update compatibility.
- **E:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q041 (`E5Q023`) — Perform solution envisioning and requirement analysis [1.9] · *Single-Answer Multiple Choice*

Store associates edited SKU retail prices inside a Canvas app while Dynamics 365 Commerce overwrote them every hour, causing register mismatches. Enforcing `____` locks Dynamics 365 Commerce as sole price master while Dataverse owns clienteling wishlists.

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Designating a single authoritative System of Record per entity with explicit survivorship and conflict-resolution rules
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Clear System-of-Record master ownership per entity/attribute stops conflicting bi-directional edits across retail systems. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Correct. Every master entity (`Customer`, `Item`, `GL Account`) needs one clear authoritative owner to prevent bi-directional data corruption.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

## Case Study Vignette — OmniCart Fulfillment Hub

> OmniCart Fulfillment Hub integrates Power Platform order exception handling with 12 third-party 3PL carrier webhooks and an ERP warehouse system. Out-of-order webhook deliveries (`Shipped` arriving before `Packed`) and duplicate carrier retries caused stale state overwrites in Dataverse until architects introduced optimistic concurrency (`ETag` / row version) and ordered messaging.

### Q042 (`E5Q070`) — Architect a solution [2.12] · *Single-Answer Multiple Choice*

Case study — OmniCart Fulfillment Hub: OmniCart receives out-of-order 3PL carrier webhooks (`Shipped` arriving 400 ms before `Packed` for the same `Order_ID`) across 12 carriers. Which Azure messaging feature in front of Dataverse preserves strict per-order sequence ordering and isolates poison payloads?

- **A.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Ingesting carrier webhooks through **APIM** into **Azure Service Bus queues/topics with Sessions enabled (`SessionId = Order_ID`)** enforces FIFO ordering per order, deduplication, and Dead-Letter Queue isolation before updating Dataverse. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q043 (`E5Q091`) — Implement the solution [3.4] · *Multi-Select (Select 2)*

Case study — OmniCart Fulfillment Hub: Duplicate 3PL carrier retries and out-of-order updates caused stale state overwrites in Dataverse while an unfiltered bi-directional ERP flow looped infinitely, spiking `Log` storage. Which two fixes resolve these issues? Select two.

- **A.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **B.** Resolving automation/integration conflicts via `Select columns` (`filteringattributes`), `Trigger Conditions`, plug-in `Depth` checks, & `ETag` (`If-Match`) optimistic concurrency
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **E.** Governing `Database`, `File`, & `Log` storage pools via `Dataverse Long Term Retention`, `Fabric/Synapse Link` archival, & attachment offloading

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). Enforcing **`ETag` (`If-Match` `RowVersion`) optimistic concurrency** + state-rank guards + `Select columns`/`Trigger Conditions` (`res_conflict_loops`) and governing `Log`/`Database` capacity (`cap_storage_tiering`) eliminate stale overwrites and runaway audit logs. [Skill 3.4: Assess storage/resource impact and resolve automation loops, race conditions, & integration conflicts | Source: Assess storage/resource impact and resolve automation & integration conflicts (https://learn.microsoft.com/en-us/power-platform/admin/capacity-storage)]

- **A:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **B:** Correct. Column filters, actor exclusions, and `If-Match` row-version headers eliminate infinite ping-pong loops and silent lost-update race conditions.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **E:** Correct. Keeping relational `Database` capacity lean prevents tenant admin lockouts (`Copy`/`Restore` blocks) and controls storage overage costs.

</details>

### Q044 (`E5Q092`) — Implement the solution [3.4] · *Single-Answer Multiple Choice*

Case study — OmniCart Fulfillment Hub: When carrier worker B attempts to `PATCH` an `Order_Exception` row using `If-Match: W/"99120"` after worker A already advanced the row to `W/"99125"`, how does Dataverse protect data integrity?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Resolving automation/integration conflicts via `Select columns` (`filteringattributes`), `Trigger Conditions`, plug-in `Depth` checks, & `ETag` (`If-Match`) optimistic concurrency
- **C.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Dataverse rejects worker B’s stale `PATCH` with **`HTTP 412 Precondition Failed`**, forcing worker B to re-fetch version `99125` and evaluate whether `Shipped` already supersedes `Packed`. [Skill 3.4: Assess storage/resource impact and resolve automation loops, race conditions, & integration conflicts | Source: Assess storage/resource impact and resolve automation & integration conflicts (https://learn.microsoft.com/en-us/power-platform/admin/capacity-storage)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Correct. Column filters, actor exclusions, and `If-Match` row-version headers eliminate infinite ping-pong loops and silent lost-update race conditions.
- **C:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q045 (`E5Q004`) — Perform solution envisioning and requirement analysis [1.2] · *Multi-Select (Select 2)*

A consumer-electronics brand needs: (1) a self-service customer warranty & RMA status website serving 1.4 million shoppers authenticated with social/external logins, and (2) an embedded shopping-return Copilot on that website that checks return-window eligibility in Dataverse and escalates VIP exceptions to live chat agents. Which two components fit best? Select two.

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Canvas Power App with a `Mobile Offline` profile and device-native camera/barcode UX tailored to frontline tasks
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Microsoft Copilot Studio agent grounded in enterprise knowledge sources, Dataverse actions, & live omnichannel handoff
- **E.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Microsoft Power Pages scales securely to 1.4 million external shoppers via `Table Permissions`, while Microsoft Copilot Studio powers policy-grounded return agents with omnichannel live-agent handoff. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Correct. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Incorrect. Canvas apps give pixel-level task UX and offline-first Dataverse synchronization for field workers operating without connectivity.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Correct. Copilot Studio delivers governed conversational and autonomous agents across Teams, web portals, and customer service channels.
- **E:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.

</details>

### Q046 (`E5Q083`) — Architect a solution [2.17] · *Single-Answer Multiple Choice*

Connecting an Azure Logic App Standard workflow to Dataverse using a **Managed Identity** mapped to a Dataverse Application User exemplifies passwordless `____` authentication.

- **A.** Using `OAuth 2.0 On-Behalf-Of (OBO)` to preserve caller identity/audit trails vs `Entra Service Principal (S2S)` / `Managed Identity` for background jobs
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). **Managed Identity / S2S Application User** authentication eliminates stored client secrets and human MFA dependencies for background retail integrations. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Correct. OBO propagates the signed-in user’s identity downstream for row-level authorization, whereas S2S/Managed Identity runs headless workloads.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q047 (`E5Q033`) — Perform solution envisioning and requirement analysis [1.13] · *Single-Answer Multiple Choice*

European Accessibility Act (`EAA`) regulations require consumer-facing Power Pages return portals and boutique apps to meet `WCAG 2.1 AA` keyboard focus, contrast, and screen-reader standards under `____`.

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Designing for `WCAG 2.1 AA` accessibility (`AccessibleLabel`, `TabIndex`, contrast) and `.resx` multi-language localization

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Designing for `WCAG 2.1 AA` accessibility and multi-language localization from Sprint 1 ensures EAA compliance across European markets. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Correct. Building accessibility and localization into initial UX components avoids expensive retrofits before public or enterprise launch.

</details>

### Q048 (`E5Q089`) — Implement the solution [3.3] · *Single-Answer Multiple Choice*

To maximize Black Friday write throughput within Dataverse’s `6,000` req / `20m` compute per 5-minute Service Protection window, how should 16 parallel Azure Function order-ingestion workers authenticate?

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Conforming to `Dataverse Service Protection` limits (`6,000` req / `20m` compute per `5-min` window), pooling `S2S Application Users`, & honoring `Retry-After`
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Distributing workers across a **pool of Microsoft Entra S2S Application Users**, sending homogeneous `CreateMultiple`/`UpdateMultiple` bulk payloads, and honoring `Retry-After` maximizes parallel throughput cleanly. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Correct. Service Protection enforces per-user/per-web-server 5-minute sliding caps (`HTTP 429`); pooling S2S Application Users and respecting `Retry-After` maximizes throughput.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q049 (`E5Q086`) — Implement the solution [3.2] · *Multi-Select (Select 2)*

A pre-holiday PCI/PII review finds a maker used client JavaScript `setVisible(false)` to hide `Tax_Residency_ID` on forms and left a Power Pages `Web API` site setting enabled without `Table Permissions` on `Gift_Card`. Which two fixes are mandatory? Select two.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access
- **C.** Auditing server-side `Security Roles`, `Column Security`, & `Power Pages Table Permissions` rather than trusting client-side UI rules
- **D.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **E.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Enforcing server-side **Power Pages `Table Permissions`** (`val_sec_boundary_audit`) and protecting `Tax_Residency_ID` with a **`Column Security Profile`** (`sec_col_hier_pim`) close both Web API vulnerabilities. [Skill 3.2: Review security across Business Rules, Security Roles, Entra Conditional Access, & security boundaries | Source: Review end-to-end security across Business Rules, Roles, Entra ID, & boundaries (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.
- **C:** Correct. Client JavaScript and `Form`-scoped Business Rules never block Web API/OData access; security boundaries must be enforced server-side in Dataverse.
- **D:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **E:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q050 (`E5Q061`) — Architect a solution [2.8] · *Single-Answer Multiple Choice*

Retail corporate structures nest 4 levels deep (`Global Brand -> Region -> District -> Boutique Store`) requiring `Under` rollup queries, while `Gift_Registry` can belong to either a `Contact` or a corporate `Account`. Which relationship features model both?

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **C.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **D.** Modeling self-referential `Hierarchical` (`1:N` `Under` queries) and `Polymorphic` (`Customer` / multi-table) relationships

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A self-referential `1:N` **Hierarchical** relationship models the 4-level store tree with `Under` queries, while a **Polymorphic** (`Customer` / multi-table) lookup links `Contact` or `Account` cleanly. [Skill 2.8: Design Dataverse relationships (1:N, N:N, hierarchical, polymorphic) and cascading behaviors | Source: Design Dataverse relationships (1:N, N:N, hierarchical) & cascading behaviors (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **C:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **D:** Correct. Hierarchical relationships support native visual hierarchy rollups and `Under` OData operators across parent-child trees.

</details>

### Q051 (`E5Q069`) — Architect a solution [2.12] · *Multi-Select (Select 3)*

An enterprise retail integration hub connects 12 carrier webhooks, Shopify Plus, SAP/F&O, and Dataverse. Which three architectural elements guarantee secure API governance, ordered message durability, and clean reusable Dataverse operations? Select three.

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`
- **C.** Defining solution-aware Dataverse `Custom APIs` exposing strongly typed request/response contracts for internal and external callers
- **D.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources
- **E.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **F.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C, D` (`CSV: 2,3,4`)

Correct answers: B, C, and D (are correct). `APIM` + `Azure Service Bus` FIFO sessions/DLQ + `Event Grid` (`integ_async_asb_apim`), solution-aware Dataverse `Custom APIs` (`integ_custom_api`), and private `VNet` subnet delegation / gateway connectivity (`net_vnet_er_opdg`) form a resilient omnichannel backbone. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.
- **C:** Correct. Custom APIs replace legacy Custom Process Actions with code-first, solution-aware OData bound/unbound operations and granular privilege checks.
- **D:** Correct. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.
- **E:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **F:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q052 (`E5Q082`) — Architect a solution [2.17] · *Single-Answer Multiple Choice*

Forty external luxury-watch brand merchandisers from partner maisons need collaborative access inside Luminary’s **internal** Model-driven Assortment Planning app. Proposed solution: Onboard the 40 external partner merchandisers via `Microsoft Entra B2B` guest collaboration mapped to an Entra Security Group Team and least-privilege Security Role. Is this appropriate?

- **A.** Enforcing `DLP` + `Endpoint Filtering`, licensing external consumers via `Power Pages` (`Entra External ID`), & `Entra B2B` for internal-app guests
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Yes — small cohorts of external business partners collaborating inside internal Model-driven/Canvas apps fit **Microsoft Entra B2B** guest access cleanly. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Correct. Power Pages scales cost-effectively with `Table Permissions` for external portals, whereas Entra B2B suits external partners using internal apps.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q053 (`E5Q011`) — Perform solution envisioning and requirement analysis [1.5] · *Multi-Select (Select 2)*

Franchise onboarding executives believe store-lease approval takes 5 days, yet franchisees wait 7 weeks while regional managers pass private WhatsApp notes and 17 rogue Excel rent-calculators around. Which two discovery methods uncover objective reality? Select two.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Power Automate Process Mining & Task Mining paired with cross-functional current-state discovery workshops
- **C.** Inventorying departmental Excel macros, Access databases, and shadow-IT workarounds to retire manual data silos
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **E.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Power Automate Process/Task Mining reveals actual wait bottlenecks from system logs/desktop steps, while shadow-IT discovery catalogs the 17 unofficial Excel rent-calculators. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Correct. Combining telemetry-driven Process/Task Mining with SME workshops exposes hidden rework loops and shadow processes objectively.
- **C:** Correct. Uncovering unofficial spreadsheets and shadow tools during discovery prevents critical edge cases from surfacing post-go-live.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **E:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q054 (`E5Q073`) — Architect a solution [2.13] · *Single-Answer Multiple Choice*

A regional freight customs portal only offers a legacy Java applet desktop UI with no APIs, while Dataverse Production requires `28-day` point-in-time restore BCDR coverage. Which architecture covers both?

- **A.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **B.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **C.** Designing BCDR around Dataverse point-in-time backups (`28-day` Prod retention, cross-Geo failover limits) and `Hosted RPA` + `Work Queues` for legacy UI
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Dataverse’s managed geo-redundant Azure SQL backups (`28-day` Prod retention) paired with **Power Automate Hosted RPA** + **Work Queues** deliver verified BCDR and resilient UI customs automation. [Skill 2.13: Design authentication (OBO vs S2S, Managed Identity), BCDR (RPO/RTO, geo-backups), and RPA | Source: Design authentication (OBO vs S2S, Managed Identity), BCDR, and RPA architectures (https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments)]

- **A:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **B:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **C:** Correct. Architects align RPO/RTO to Microsoft’s managed geo-replication SLAs and isolate UI-only legacy integrations behind resilient RPA Work Queues.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q055 (`E5Q053`) — Architect a solution [2.4] · *Single-Answer Multiple Choice*

A supermarket chain serves warehouse forklift pickers (gloved rugged scanners), headquarters category analysts (multi-monitor desktop grids), and external suppliers (online ASN portal). How should you group apps?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **C.** Grouping capabilities into role- and task-specific apps (offline Canvas for field crews, Model-driven for back-office, Power Pages for externals)
- **D.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Building a focused rugged Canvas app for forklift pickers, a Model-driven app for category analysts, and a Power Pages site for suppliers matches UX, offline needs, and licensing per persona. [Skill 2.4: Design apps by grouping required features based on persona, role, task, and offline needs | Source: Design role-based and task-based app experiences across form factors (https://learn.microsoft.com/en-us/power-apps/guidance/planning/app-design)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **C:** Correct. Task-focused apps per persona outperform bloated one-size-fits-all apps in load speed, offline footprint, and usability.
- **D:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.

</details>

### Q056 (`E5Q016`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

A retail CTO demands zero manual zip imports into Production, mandatory automated PR static scans, and centralized telemetry before peak holiday freeze. Aligning to the Well-Architected `____` pillar fulfills these controls.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Power Platform Well-Architected `Operational Excellence` pillar (automated ALM pipelines, Application Insights, & CoE)
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Operational Excellence` institutionalizes automated CI/CD pipelines, Solution Checker gates, Managed Environments, and Application Insights observability. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Correct. Operational Excellence standardizes CI/CD solution pipelines, automated Solution Checker gates, telemetry, and Managed Environment governance.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q057 (`E5Q009`) — Perform solution envisioning and requirement analysis [1.4] · *Single-Answer Multiple Choice*

A department-store chain is retiring a 20-year-old AS/400 loyalty system holding 28 million shopper profiles (with 31% duplicate household emails, unmapped tier codes, and a strict 14-hour Sunday night cutover window). What governs your migration estimate?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Estimating migration/integration effort from source data cleanliness, transformations, API throughput windows, & cutover downtime
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Household deduplication rules, loyalty-tier transformations, 28M-row API throughput math (`6,000` req / 5-min pools), and delta cutover rehearsals inside the 14-hour freeze govern realistic sizing. [Skill 1.4: Identify and estimate data migration and integration efforts, complexity drivers, and alternatives | Source: Estimate migration and integration efforts and alternatives (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Correct. Realistic effort sizing accounts for legacy deduplication, schema mapping, historical volume, 5-minute API limits, and delta cutover rehearsals.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q058 (`E5Q046`) — Perform solution envisioning and requirement analysis [1.18] · *Single-Answer Multiple Choice*

Delivering `Must-have` order-cancellation and refund workflows before holiday peak while scheduling `Won't-have (this release)` influencer gifting dashboards to Wave 2 applies `____`.

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Scoping a high-value `MVP` Phase 1 release using MoSCoW prioritization and formal change-request governance
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Disciplined MoSCoW `MVP` scoping protects business-critical retail dates from non-essential scope creep. [Skill 1.18: Determine MVP vs phased solution scope boundaries and govern scope changes | Source: Determine MVP vs phased solution scope and manage scope boundaries (https://learn.microsoft.com/en-us/training/paths/become-solution-architect/)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Phased MVP delivery de-risks go-live, delivers early business value, and prevents uncontrolled scope creep.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q059 (`E5Q084`) — Implement the solution [3.1] · *Single-Answer Multiple Choice*

Before holiday freeze, your automated pipeline runs `pac solution check` and fails a pull request because a synchronous plug-in executes an unindexed `QueryExpression` with `NoLock` issues and `ColumnSet(true)`. Which validation control caught this?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Enforcing `Solution Checker` and `App Checker` gates in CI/CD pipelines alongside `Power Platform Well-Architected` design reviews

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). **Solution Checker** (paired with **App Checker** for Canvas apps) enforces static code and formula quality gates inside CI/CD pipelines. [Skill 3.1: Evaluate detailed designs and implementations with Solution Checker, App Checker, & Well-Architected | Source: Evaluate detailed designs with Solution Checker, App Checker, & Well-Architected (https://learn.microsoft.com/en-us/power-platform/alm/use-powershell-cmdlets-solution-checker)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Correct. Solution Checker flags unbounded queries and sync plug-in anti-patterns, while App Checker catches delegation warnings and WCAG errors before release.

</details>

### Q060 (`E5Q057`) — Architect a solution [2.6] · *Single-Answer Multiple Choice*

Store district managers want live exception charts (`Late BOPIS Orders`, `Open Audits`, `Cold-Chain Alerts`) inside their Model-driven dashboard honoring each manager’s regional Business Unit automatically with zero extra BI licenses. Which option fits best?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Native Dataverse **system charts and interactive experience dashboards** render live transactional drill-downs respecting Dataverse security natively. [Skill 2.6: Design data visualization strategies across Dataverse charts, Power BI RLS, and Fabric/Synapse Link | Source: Design data visualization (Dataverse charts, Power BI RLS, Fabric/Synapse Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-synapse)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Correct. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Incorrect. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.

</details>

### Q061 (`E5Q056`) — Architect a solution [2.5] · *Single-Answer Multiple Choice*

Loyalty tier rules reference exact GUIDs of 15 `VIP_Tier` configuration rows across Dev, QA, UAT, and Prod, while `ADF` upserts 6 million shoppers keyed by `Global_Loyalty_ID`. Which tooling combination fits best?

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Staging cleansed records via `ADF` / `SSIS` using Dataverse `Alternate Keys` (`Upsert`) and `Configuration Migration Tool` for fixed-GUID config rows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Exporting `VIP_Tier` rows with the **Configuration Migration Tool (`CMT`)** preserves fixed GUIDs across environments, while a Dataverse **`Alternate Key`** on `Global_Loyalty_ID` enables fast single-call `Upsert` loads. [Skill 2.5: Design enterprise data migration strategies, load sequencing, Alternate Keys, and CMT tooling | Source: Design enterprise data migration strategies, load order, and tooling (https://learn.microsoft.com/en-us/power-platform/admin/create-schema-export-data)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Correct. Alternate Keys eliminate GUID pre-lookup round-trips on upserts, while CMT preserves exact reference-record GUIDs across Dev/UAT/Prod.

</details>

### Q062 (`E5Q085`) — Implement the solution [3.1] · *Single-Answer Multiple Choice*

Canvas **App Checker** flags `Filter(Products, "Silk" in Product_Description)` over 350,000 SKUs inside a boutique lookup screen. Why must this be refactored before launch?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Enforcing `Solution Checker` and `App Checker` gates in CI/CD pipelines alongside `Power Platform Well-Architected` design reviews

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Substring `in` checks where non-delegable or leading-wildcard scans hurt scale; refactoring to delegable `StartsWith` or **Dataverse Search** (`Search` action) ensures accurate results across all 350,000 SKUs. [Skill 3.1: Evaluate detailed designs and implementations with Solution Checker, App Checker, & Well-Architected | Source: Evaluate detailed designs with Solution Checker, App Checker, & Well-Architected (https://learn.microsoft.com/en-us/power-platform/alm/use-powershell-cmdlets-solution-checker)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Correct. Solution Checker flags unbounded queries and sync plug-in anti-patterns, while App Checker catches delegation warnings and WCAG errors before release.

</details>

### Q063 (`E5Q040`) — Perform solution envisioning and requirement analysis [1.16] · *Multi-Select (Select 2)*

A luxury retailer’s VIP concierge desk needs omnichannel `Case` (`incident`) routing across WhatsApp, voice, email, and live chat, SLA timers, unified customer profiles, and a certified WhatsApp/telephony CTI connector. Which two selections fit best? Select two.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Dynamics 365 first-party app (`Sales`, `Customer Service`, or `Field Service`) leveraging native schemas, SLAs, & RSO scheduling
- **E.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). **Dynamics 365 Customer Service** (Omnichannel + `Case` + SLAs) paired with a certified **AppSource telephony/messaging ISV** delivers turnkey concierge service without bespoke queue code. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Correct. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Correct. Adopting Dynamics 365 first-party apps avoids reinventing complex case routing, omnichannel queues, or Resource Scheduling Optimization.
- **E:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.

</details>

### Q064 (`E5Q099`) — Implement the solution [3.8] · *Single-Answer Multiple Choice*

Putting Dataverse Production into `____` during the 4-hour pre-holiday cutover window guarantees store associates cannot create conflicting transactions while admins run final reconciliation checks.

- **A.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Enabling Dataverse `Administration mode` (blocking non-admins & background jobs) during cutover, followed by smoke tests & Application Insights hypercare

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Dataverse **`Administration mode`** locks out non-admin users and pauses optional background jobs until cutover smoke tests pass. [Skill 3.8: Identify go-live readiness gates, execute Administration mode cutovers, and manage hypercare telemetry | Source: Assess go-live readiness factors, Administration mode, and hypercare remediation (https://learn.microsoft.com/en-us/power-platform/admin/admin-mode)]

- **A:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Correct. `Administration mode` guarantees a quiet database during final schema upgrade and delta migration before opening Production to users.

</details>

### Q065 (`E5Q012`) — Perform solution envisioning and requirement analysis [1.5] · *Single-Answer Multiple Choice*

Ingesting order-management event traces (`Order_ID`, `Event_Type`, `Timestamp`, `Fulfillment_DC`) into `____` pinpoints which distribution centers trigger repeated split-shipment rework loops.

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **D.** Power Automate Process Mining & Task Mining paired with cross-functional current-state discovery workshops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate **Process Mining** visualizes variant frequencies, split-shipment loops, and DC dwell times directly from order event logs. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **D:** Correct. Combining telemetry-driven Process/Task Mining with SME workshops exposes hidden rework loops and shadow processes objectively.

</details>

### Q066 (`E5Q041`) — Perform solution envisioning and requirement analysis [1.16] · *Single-Answer Multiple Choice*

Can 800 seasonal holiday contact-center agents licensed only with standalone Power Apps per-app seats create and resolve standard Dynamics 365 `Case` (`incident`) rows directly?

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Validating Dynamics 365 restricted-table licensing (`Case / incident`, `Work Order`, `Entitlement`) during fit/gap analysis

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). No — `Case` (`incident`) is a Dynamics 365 **restricted table**; agents creating or updating `Case` records require qualifying Dynamics 365 Customer Service licenses. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Correct. Restricted Dynamics 365 tables require appropriate Dynamics 365 licenses for CRUD operations rather than standalone Power Apps licenses.

</details>

## Case Study Vignette — Solstice Peak Commerce

> Solstice Peak Commerce freezes schema changes two weeks before Black Friday and validates go-live readiness across 18 microservices and 9 Power Platform solutions. Architects are wiring Azure Application Insights (`dependencies`/`exceptions` KQL) to Dataverse & Canvas apps, sizing Power Platform Request add-ons, and resolving a circular dependency between two Managed Solutions.

### Q067 (`E5Q090`) — Implement the solution [3.3] · *Single-Answer Multiple Choice*

Case study — Solstice Peak Commerce: Solstice Peak Commerce forecasts 9.5 million automated order-exception API requests per 24 hours across Black Friday weekend. How should architects size 24-hour entitlements and minimize request consumption?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Sizing 24-hour `Power Platform Request (PPR)` capacity and using `CreateMultiple` / `UpdateMultiple` / `$batch` (`ExecuteMultiple` `<= 1,000`)
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Calculating 24-hour **Power Platform Request (`PPR`)** demand, provisioning **PPR capacity add-ons** (or Pay-As-You-Go), and consolidating writes via `CreateMultiple`/`UpdateMultiple`/`$batch` (`<= 1,000`) ensures zero licensing overage or throttling. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Correct. Bulk messages (`CreateMultiple`/`UpdateMultiple`) and `$batch` cut network round-trips dramatically while keeping daily PPR consumption within entitlements.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q068 (`E5Q094`) — Implement the solution [3.5] · *Single-Answer Multiple Choice*

Case study — Solstice Peak Commerce: Solstice Peak Commerce is wiring **Azure Application Insights** to both its Dataverse Production environment and its Canvas apps before Black Friday. Which KQL tables allow architects to correlate slow Canvas screens, outbound custom-connector calls, and plug-in exceptions?

- **A.** Running scale tests in UAT while streaming Dataverse and Canvas telemetry to `Azure Application Insights` (`dependencies` / `exceptions` KQL)
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Application Insights populates `pageViews` (screen loads), `dependencies` (outbound Dataverse/connector API calls), `requests` (plug-in/API executions), and `exceptions` / `traces` for end-to-end KQL observability. [Skill 3.5: Identify and resolve Canvas, Model-driven, Quick Find index, and synchronous plug-in performance issues | Source: Identify and resolve Canvas, Model-driven, Dataverse, & plug-in performance issues (https://learn.microsoft.com/en-us/power-platform/well-architected/performance-efficiency/overview)]

- **A:** Correct. Application Insights integration captures page-load latency, plug-in execution durations, and outbound dependency failures under realistic concurrency.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q069 (`E5Q097`) — Implement the solution [3.7] · *Multi-Select (Select 2)*

Case study — Solstice Peak Commerce: Two Managed Solutions (`Checkout_Exceptions` and `Carrier_Claims`) cannot build cleanly in pipelines due to a circular table-lookup dependency, and an unmanaged hotfix layer sits on the Production `Order` form. Which two actions resolve both blockers before holiday freeze? Select two.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix
- **E.** Resolving deployment failures by running `Remove active customizations`, refactoring circular solution dependencies into a base layer, & validating stage JSON bindings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). Extracting shared base tables into a foundational `Commerce_Core` Managed Solution (`sol_segmented_alm`) breaks the circular loop, while running **`Remove active customizations`** (`dep_layers_deps`) clears the Production `Active` unmanaged layer. [Skill 3.7: Resolve deployment plan issues, Unmanaged Active Solution Layers, and circular solution dependencies | Source: Resolve deployment plan, Solution Layer, and pipeline dependency issues (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.
- **E:** Correct. Stripping Unmanaged Active layers and decoupling circular references ensures repeatable, zero-touch Managed Solution Upgrades.

</details>

### Q070 (`E5Q054`) — Architect a solution [2.4] · *Single-Answer Multiple Choice*

Splitting a 110-screen store-associate mega-app into three fast task apps (`Clienteling`, `Cycle Count`, `BOPIS Curbside Pickup`) exemplifies `____`.

- **A.** Grouping capabilities into role- and task-specific apps (offline Canvas for field crews, Model-driven for back-office, Power Pages for externals)
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Task-based app decomposition dramatically cuts Canvas cold-start load time, memory footprint, and maker merge conflicts. [Skill 2.4: Design apps by grouping required features based on persona, role, task, and offline needs | Source: Design role-based and task-based app experiences across form factors (https://learn.microsoft.com/en-us/power-apps/guidance/planning/app-design)]

- **A:** Correct. Task-focused apps per persona outperform bloated one-size-fits-all apps in load speed, offline footprint, and usability.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q071 (`E5Q027`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

A store operations VP requests: `"Build a blue screen with 24 toggle switches and a floating calculator widget on the Return form."` How should the Solution Architect refine this request?

- **A.** Refining prescriptive wishes into persona-based `User Stories` (`As a ... I need ... so that ...`) with testable Acceptance Criteria
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Translating UI-prescriptive demands into persona-based `User Stories` (`As a Cashier, I need instant receipt-free exchange verification under 20 seconds so checkout lines keep moving`) with testable Acceptance Criteria uncovers the optimal workflow. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Correct. Outcome-oriented User Stories decouple business intent from premature UI assumptions and anchor QA test cases.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q072 (`E5Q050`) — Architect a solution [2.2] · *Single-Answer Multiple Choice*

Assortment planners need a high-density color-swatch matrix grid inside a Model-driven view supporting keyboard inline quantity entry across 500 size-color SKUs. Developing a `____` virtual dataset control delivers this cleanly.

- **A.** Validating interactive UX prototypes (`Figma-to-App` / `Custom Pages`) early and building `PCF` controls for specialized UI gaps
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A React virtual **Power Apps Component Framework (`PCF`)** dataset control renders fast, accessible size-color matrices bound directly to Dataverse datasets. [Skill 2.2: Identify app customization approaches and validate interactive user experience prototypes | Source: Select customization approaches for existing apps and validate UX prototypes (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/design-consistency)]

- **A:** Correct. Interactive prototyping validates user journeys cheaply, while Power Apps Component Framework (`PCF`) renders reusable custom TypeScript/React controls.
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.

</details>

### Q073 (`E5Q063`) — Architect a solution [2.9] · *Single-Answer Multiple Choice*

Concierge agents inside a Model-driven app need live online read-only lookups into 80 million historical e-commerce shipment tracking events stored in Azure SQL / Fabric without copying them into Dataverse storage. Using `____` surfaces those rows in place.

- **A.** Replicating data into native Dataverse tables (`Dataflows` / `ADF`) when Mobile Offline, row-level security roles, auditing, or SLAs are required
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Using the `Virtual Connector Provider` (`SQL Server`, `SharePoint`, `Fabric`) to expose external tables in Dataverse with low-code setup
- **D.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). The **`Virtual Connector Provider`** (`SQL Server` / `Fabric`) creates Dataverse **Virtual Tables** querying the 80M shipment events live without Dataverse Database duplication. [Skill 2.9: Determine when to connect external data in place (Virtual tables) versus import/replicate into Dataverse | Source: Connect external data in place (Virtual tables) vs import/replicate into Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-virtual-entities)]

- **A:** Incorrect. Virtual tables do not support Mobile Offline sync, Dataverse row-level User/Team ownership, or native column auditing.
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Correct. The Virtual Connector Provider creates Virtual Tables over supported connectors without authoring custom C# data-provider plug-ins.
- **D:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).

</details>

### Q074 (`E5Q015`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

Ninety store-replenishment Power Automate flows run under a former contractor’s account in the `Default` environment using unencrypted FTP connectors. Which risk mitigation strategy addresses this?

- **A.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **B.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)
- **C.** Mitigating single-maker bus-factor risk, unmonitored personal flows, & technical debt via Managed Environments and CoE
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Migrating business-critical flows into **Managed Environments** under Service Principal ownership with strict DLP connector blocks and CoE monitoring eliminates bus-factor and exfiltration exposure. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **B:** Incorrect. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.
- **C:** Correct. Unmanaged citizen sprawl and bespoke code without ALM pipelines represent top organizational operational risks.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q075 (`E5Q051`) — Architect a solution [2.3] · *Single-Answer Multiple Choice*

Five retail app squads need identical brand typography headers, barcode-EAN validation flows, and Shopify REST connectors, supported by clear `ERD` and `Sequence` architecture diagrams. Which practice enforces reuse?

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Reusing `Component Libraries`, `PCF`, `Child Flows`, & `Custom Connectors`, documented via `ERD`, `Sequence`, & `Context` diagrams
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Packaging shared UI/logic in `Canvas Component Libraries`, `PCF`, `Child Cloud Flows`, and `Custom Connectors` — documented with `ERD`, `Sequence`, and `Context` diagrams — eliminates duplicate code across squads. [Skill 2.3: Maximize component reuse (PCF, Component Libraries, Child Flows) and communicate designs visually | Source: Maximize component reuse (PCF, Component Libraries, Child Flows) & visual diagrams (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Shared component catalogs eliminate duplicate maintenance, while visual architecture diagrams align technical and business stakeholders.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q076 (`E5Q058`) — Architect a solution [2.6] · *Single-Answer Multiple Choice*

Merchandising VPs require global sell-through dashboards combining Dataverse clienteling appointments, 12 TB of POS basket parquet tables in OneLake, and foot-traffic sensors with regional **Row-Level Security (`RLS`)**. Which analytics design fits best?

- **A.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). **`Microsoft Fabric Link`** (`OneLake`) paired with **Power BI (`RLS`)** blends Dataverse and multi-terabyte POS lakehouse tables without impacting transactional Dataverse SQL. [Skill 2.6: Design data visualization strategies across Dataverse charts, Power BI RLS, and Fabric/Synapse Link | Source: Design data visualization (Dataverse charts, Power BI RLS, Fabric/Synapse Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-synapse)]

- **A:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Correct. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.

</details>

### Q077 (`E5Q052`) — Architect a solution [2.3] · *Single-Answer Multiple Choice*

Which visual architecture diagram best illustrates how 12 third-party 3PL carrier webhooks flow through APIM -> Azure Service Bus -> Azure Functions -> Dataverse `Order_Exception` rows over time?

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Reusing `Component Libraries`, `PCF`, `Child Flows`, & `Custom Connectors`, documented via `ERD`, `Sequence`, & `Context` diagrams
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A **UML Sequence diagram** (paired with a System Context diagram) clearly depicts chronological webhook ingestion, queue buffering, retry loops, and Dataverse upserts. [Skill 2.3: Maximize component reuse (PCF, Component Libraries, Child Flows) and communicate designs visually | Source: Maximize component reuse (PCF, Component Libraries, Child Flows) & visual diagrams (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Correct. Shared component catalogs eliminate duplicate maintenance, while visual architecture diagrams align technical and business stakeholders.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.

</details>

### Q078 (`E5Q047`) — Architect a solution [2.1] · *Multi-Select (Select 2)*

A global retailer runs four agile tribes (`Core Retail CDM`, `OMS Integrations`, `Boutique Clienteling`, `Concierge Service`) across `Dev -> QA -> UAT -> Prod` plus regional `EU`, `US`, and `APAC` environments. Which two designs govern solution segmentation and environments cleanly? Select two.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **E.** Dedicated `Dev -> Test -> UAT -> Prod` environments (plus sovereign `Multi-Geo` instances) governed by `Managed Environments` & `CoE Starter Kit`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). Segmented Managed Solutions (`Base CDM` -> `Shared Integrations` -> `Tribe Apps`) under one custom Publisher prefix (`sol_segmented_alm`) plus multi-tier / `Multi-Geo` **Managed Environments** & **CoE Starter Kit** (`env_multi_tier_coe`) enable safe parallel delivery. [Skill 2.1: Design segmented solution topology, custom Publisher strategy, and Managed Environments | Source: Design solution topology, publisher segmentation, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/alm/segmented-solutions-alm)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **E:** Correct. Multi-tier ALM environments isolate production workloads, Multi-Geo satisfies regional residency, and CoE + Managed Environments automate governance.

</details>

### Q079 (`E5Q096`) — Implement the solution [3.6] · *Single-Answer Multiple Choice*

During Sunday’s final 6-million-row loyalty cutover, suppressing custom sync/async plug-ins via `____` and disabling welcome-coupon cloud flows prevents sending 6 million duplicate discount texts.

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Accelerating bulk loads with `BypassCustomPluginExecution` (`BypassBusinessLogicExecution`), disabled flows/search indexes, & parallel `CreateMultiple` batches
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Passing `BypassCustomPluginExecution` (`BypassBusinessLogicExecution = CustomSync,CustomAsync`) and disabling notification cloud flows during bulk cutover stops unintended outbound messages and halves load time. [Skill 3.6: Escalate and resolve data migration bottlenecks (BypassCustomPluginExecution, delta loads, reconciliation) | Source: Escalate and remediate enterprise data migration bottlenecks and cutover issues (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/TVF-override-plugin-execution)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Correct. Bypassing non-essential custom sync/async logic and disabling cloud flows during cutover prevents throttling and unintended notification storms.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q080 (`E5Q038`) — Perform solution envisioning and requirement analysis [1.15] · *Single-Answer Multiple Choice*

During retail steering-committee review, you present a scored breakdown showing 130 requirements met natively, 28 via declarative flows/Power Fx, 11 via a payment/SMS AppSource ISV, and 6 via C# plug-ins. This deliverable is a `____`.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **C.** Structured Fit/Gap matrix scoring requirements across `Out-of-the-Box`, `Configuration`, `AppSource ISV`, & `Custom Code`
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A structured Fit/Gap matrix quantifies functional coverage, licensing needs, and custom-code maintenance across architectural tiers. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **C:** Correct. Formal fit/gap scoring exposes customization TCO, licensing impacts, and upgrade maintenance trade-offs transparently.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q081 (`E5Q001`) — Perform solution envisioning and requirement analysis [1.1] · *Ordered Sequence (Multiple Choice)*

A global apparel group operating 900 stores and 14 regional e-commerce sites is launching a unified loyalty and clienteling platform on Microsoft Power Platform. In what four-step sequence should you lead envisioning through Well-Architected alignment?

- **A.** Copy every legacy Access table 1-for-1 into Dataverse → Replicate broken manual steps verbatim → Ignore API and storage limits → Run fit/gap analysis during user acceptance testing
- **B.** Write custom C# plug-ins on Day 1 → Purchase all Dynamics 365 licenses blindly → Skip current-state discovery → Capture non-functional requirements after Production go-live
- **C.** Grant System Administrator to all stakeholders → Build prototypes in personal My Flows → Skip security & residency discovery → Export Unmanaged Default Solution to Production
- **D.** Capture business outcomes, KPIs, & risk constraints → Map current-state processes & existing enterprise systems → Refine functional & non-functional requirements → Align target architecture to Power Platform Well-Architected pillars

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Retail envisioning captures revenue/NPS KPIs and GDPR/PCI risks first, maps store/POS/OMS processes, refines functional & NFR specs, and aligns trade-offs to Power Platform Well-Architected pillars. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Incorrect. Lifting and shifting broken legacy schemas without process optimization or fit/gap analysis perpetuates technical debt.
- **B:** Incorrect. Coding or buying licenses before discovery and NFR capture causes costly rework and architectural mismatches.
- **C:** Incorrect. Prototyping in Default Solution with over-privileged accounts violates governance and creates un-deployable artifacts.
- **D:** Correct. Solution envisioning establishes measurable business outcomes and risks first, inventories current processes/systems, refines functional & NFR specs, and aligns design trade-offs to Well-Architected pillars.

</details>

### Q082 (`E5Q002`) — Perform solution envisioning and requirement analysis [1.1] · *Single-Answer Multiple Choice*

During Cyber Monday flash sales, checkout gift-card redemptions must survive regional payment-processor blips using exponential backoff, automatic circuit breakers, and zero duplicate balance deductions. Which Well-Architected pillar governs this design?

- **A.** Power Platform Well-Architected `Operational Excellence` pillar (automated ALM pipelines, Application Insights, & CoE)
- **B.** Power Platform Well-Architected `Reliability` pillar (RPO/RTO targets, fault isolation, retries, & circuit breakers)
- **C.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The Power Platform Well-Architected `Reliability` pillar governs transient fault recovery, circuit breakers, idempotency, and regional resiliency under peak retail operations. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Incorrect. Operational Excellence standardizes CI/CD solution pipelines, automated Solution Checker gates, telemetry, and Managed Environment governance.
- **B:** Correct. The Reliability pillar ensures mission-critical workloads withstand transient outages, throttling, and regional faults within defined RPO/RTO bounds.
- **C:** Incorrect. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q083 (`E5Q035`) — Perform solution envisioning and requirement analysis [1.14] · *Single-Answer Multiple Choice*

Store managers currently print daily cash-drawer variance sheets, fax them to district admins, and wait 4 days for emailed spreadsheet approvals. Proposed solution: Redesign and standardize a single digital future-state variance exception workflow in Dataverse that auto-clears variances under `$5` and routes outliers instantly. Is this right?

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — eliminating manual fax/spreadsheet loops and automating low-risk tolerances before building screens exemplifies future-state process optimization. [Skill 1.14: Guide future-state business process optimization and standardization before automating | Source: Guide future-state business process optimization and standardization (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/overview)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.

</details>

### Q084 (`E5Q100`) — Implement the solution [3.8] · *Single-Answer Multiple Choice*

Proposed solution: Roll out the new boutique clienteling suite to 15 pilot stores in Wave 1 with signed Go/No-Go gates, manual pre-cutover restore points, and real-time Application Insights hypercare dashboards before scaling to all 600 boutiques. Should you approve this go-live strategy?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Establishing signed-off `Go / No-Go` readiness gates, manual pre-cutover `Backup` restore points, rollback runbooks, & phased wave rollouts
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes — phased pilot waves, explicit Go/No-Go gates, manual backups, and telemetry-driven hypercare minimize global retail rollout risk. [Skill 3.8: Identify go-live readiness gates, execute Administration mode cutovers, and manage hypercare telemetry | Source: Assess go-live readiness factors, Administration mode, and hypercare remediation (https://learn.microsoft.com/en-us/power-platform/admin/admin-mode)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Correct. Clear Go/No-Go criteria, pre-upgrade backups, and phased pilot waves minimize blast radius during enterprise go-live.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q085 (`E5Q006`) — Perform solution envisioning and requirement analysis [1.2] · *Single-Answer Multiple Choice*

Merchandise category buyers work on desktop monitors managing vendor rebates, 7-stage seasonal assortment approvals, and multi-currency price-list subgrids in Dataverse. Proposed solution: Deliver a Model-driven Power App with Business Process Flows and custom system views. Does this match the persona?

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Model-driven Power App over Microsoft Dataverse with responsive forms, views, dashboards, & Business Process Flows
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes — structured, grid-heavy merchandising assortment and vendor-rebate workflows fit a Model-driven Power App natively. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Correct. Model-driven apps excel at structured, data-dense back-office case and lifecycle management directly atop Dataverse security.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.

</details>

### Q086 (`E5Q098`) — Implement the solution [3.7] · *Single-Answer Multiple Choice*

How do automated Power Platform Pipelines / Azure DevOps tasks switch Shopify webhook URLs and service-principal connections seamlessly between `UAT` and `Prod` without editing the Managed `.zip` package?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Resolving deployment failures by running `Remove active customizations`, refactoring circular solution dependencies into a base layer, & validating stage JSON bindings
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Supplying stage-specific **Deployment Settings JSON** files binds **Environment Variables** and **Connection References** cleanly during import without touching the immutable Managed package. [Skill 3.7: Resolve deployment plan issues, Unmanaged Active Solution Layers, and circular solution dependencies | Source: Resolve deployment plan, Solution Layer, and pipeline dependency issues (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Correct. Stripping Unmanaged Active layers and decoupling circular references ensures repeatable, zero-touch Managed Solution Upgrades.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q087 (`E5Q076`) — Architect a solution [2.15] · *Ordered Sequence (Multiple Choice)*

A global luxury retailer requires regional Business Unit isolation (`EMEA`, `Americas`, `APAC`), matrix cross-BU visibility for global trunk-show stylists, automated Entra group role assignment, and lightweight VIP co-selling teams. Which four-step security design sequence fits best?

- **A.** Place all users in one root BU with Organization-level Read/Write/Delete → Clone System Administrator for power users → Hide restricted fields using client-only JavaScript → Share individual records manually
- **B.** Model Business Units around isolation boundaries (with Modernized BUs for matrix access) → Author custom least-privilege Security Roles → Bind roles to Entra Security Group Teams → Layer Column Security & Access Team Templates
- **C.** Create 400 micro Business Units mirroring every HR cost center → Move users between BUs daily (wiping roles prior to modern settings) → Duplicate 400 identical copies of every Security Role → Audit nothing
- **D.** Store confidential M&A contracts in default SharePoint Document Management folders → Assume SharePoint automatically inherits Dataverse row-level Security Roles & Access Teams → Grant site-wide Read to all employees → Go live

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Modeling BUs around regional isolation boundaries (with Modernized BUs for matrix stylists), creating least-privilege custom Security Roles, binding roles to Entra Security Group Teams, and layering Column Security + Access Team Templates scales cleanly. [Skill 2.15: Design Business Units, Modernized BUs, Owner Teams, Access Team Templates, & Entra Group Teams | Source: Design Business Units, Modernized BUs, Owner/Access Teams, & Entra Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect. Client-side JavaScript never secures data at the API layer, and manual per-record sharing bloats the PrincipalObjectAccess (`POA`) table.
- **B:** Correct. Scalable Dataverse security aligns BUs to isolation boundaries, layers custom least-privilege roles onto Entra Security Group Teams for zero-touch provisioning, and handles exceptions via Access Teams and Column Security.
- **C:** Incorrect. Over-fragmenting Business Units for reporting rather than true security boundaries creates massive administrative overhead.
- **D:** Incorrect. Out-of-the-box SharePoint Document Management does NOT synchronize Dataverse row-level security ACLs to SharePoint folders automatically.

</details>

### Q088 (`E5Q059`) — Architect a solution [2.7] · *Multi-Select (Select 2)*

A retail supply-chain solution must: (1) block saving a `Purchase_Order` synchronously if vendor sanction status = `Blocked`, and (2) exchange `ANSI X12 850/856` EDI documents with 400 apparel factories inside VNet-isolated enterprise workflows. Which two automation tools should you select? Select two.

- **A.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **B.** Azure Logic Apps (Standard) for enterprise B2B EDI (`X12`/`AS2`/`EDIFACT`), VNet-isolated single-tenant workflows, & Azure Bicep ALM
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Synchronous Dataverse plug-ins (`<= 2m`) strictly for atomic transaction validation/rollback; Cloud Flows / Logic Apps for async orchestration
- **E.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). A fast synchronous Dataverse plug-in enforces atomic vendor-sanction rollback (`auto_sync_vs_async`), while **Azure Logic Apps (Standard)** processes `X12 850/856` B2B EDI flows inside private VNet compute (`auto_logic_apps`). [Skill 2.7: Design automation strategies (sync vs async, BPF, Logic Apps) and multi-environment ALM topology | Source: Design automation & multi-environment strategies (CoE Starter Kit & ALM) (https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit)]

- **A:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **B:** Correct. Logic Apps Standard complements Power Automate when Azure RBAC, private VNet compute, or B2B Enterprise Integration Pack codecs are required.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Correct. Keeping synchronous transaction pipelines fast and offloading external orchestrations asynchronously protects Dataverse SQL responsiveness.
- **E:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q089 (`E5Q067`) — Architect a solution [2.11] · *Ordered Sequence (Multiple Choice)*

Whenever a `Return_Authorized` row commits in Dataverse, downstream Manhattan WMS, ERP refund ledgers, and fraud analytics must receive asynchronous, durable, ordered events without slowing shopper return portals. Which four-step integration sequence fits best?

- **A.** Call slow on-premises ERP SOAP endpoints inside a synchronous Pre-Operation Dataverse plug-in → Hold SQL transaction locks for 90 seconds → Ignore HTTP 429/503 errors → Lose failed payloads permanently
- **B.** Embed ERP admin client secrets inside browser JavaScript web resources → Call ERP directly from user browsers bypassing CORS & DLP → Log failed payloads to browser `console.log` → Skip auditing
- **C.** Poll all 10 million Dataverse rows every 10 seconds without `modifiedon` or Change Tracking → Overrun 5-minute Service Protection limits → Overwrite newer ERP records blindly → Disable TLS
- **D.** Register a Dataverse Service Endpoint (`Service Bus` / `Event Grid`) → Publish row events asynchronously on commit → Buffer & transform via Azure Functions / Logic Apps with DLQ → Upsert idempotently into ERP via Alternate Keys

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Publishing asynchronously from a Dataverse Service Endpoint to Azure Service Bus / Event Grid, transforming via Azure Functions / Logic Apps with DLQ, and upserting idempotently via Alternate Keys decouples Dataverse from WMS/ERP latency. [Skill 2.11: Design collaboration (Teams, SharePoint ACL nuances, Exchange) and Dynamics 365 Dual-write integrations | Source: Design Teams, SharePoint, Exchange, and Dynamics 365 (Dual-write) integrations (https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dual-write/dual-write-overview)]

- **A:** Incorrect. Long network calls inside synchronous plug-ins exhaust Dataverse worker threads, lock SQL transactions, and lose messages when endpoints go offline.
- **B:** Incorrect. Exposing secrets in client-side JavaScript is a critical security vulnerability.
- **C:** Incorrect. Full-table polling without Dataverse Change Tracking triggers `HTTP 429` throttling and causes lost-update race conditions.
- **D:** Correct. Asynchronous Dataverse Service Endpoints -> Azure Service Bus/Event Grid -> Azure Functions/Logic Apps with Dead-Letter Queues and idempotent Alternate Key upserts decouple Dataverse from ERP latency and outages.

</details>

## Case Study Vignette — FreshBasket Grocery Chain

> FreshBasket Grocery Chain processes 900,000 daily store-audit photos and PDF cold-chain receipts across 1,100 supermarkets. Storing raw 8 MB photos inside relational Dataverse columns exhausted expensive Database capacity within 60 days. Architects must redesign file/blob offloading, retention policies, and AI Builder receipt automation.

### Q090 (`E5Q007`) — Perform solution envisioning and requirement analysis [1.3] · *Single-Answer Multiple Choice*

Case study — FreshBasket Grocery Chain: FreshBasket store receivers snap photos of 900,000 daily cold-chain supplier delivery dockets and need automated extraction of `Supplier_ID`, `Chiller_Temp_C`, and `Lot_Expiry` inside Power Automate without managing custom GPU clusters. Which component should you select?

- **A.** AI Builder prebuilt/custom document processing, text classification, & AI Prompts integrated natively in Power Platform
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Azure pro-code extension (`Azure Functions`, `Service Bus`, `AKS`, or `Azure AI Foundry`) integrated with Power Platform

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). **AI Builder** document processing extracts structured fields from receipt and delivery-docket images natively inside Power Automate cloud flows. [Skill 1.3: Identify and select components from existing apps, Dynamics 365, AppSource ISVs, and Azure | Source: Evaluate Dynamics 365 apps, AppSource ISVs, and Azure extensions (https://learn.microsoft.com/en-us/training/modules/discover-customer-needs/)]

- **A:** Correct. AI Builder embeds governed document extraction and generative AI prompts directly inside flows and apps without custom ML infrastructure.
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Incorrect. Heavy compute, long-running algorithms (> 2 minutes), and high-throughput brokered messaging offload cleanly to Azure extensions.

</details>

### Q091 (`E5Q034`) — Perform solution envisioning and requirement analysis [1.13] · *Single-Answer Multiple Choice*

Case study — FreshBasket Grocery Chain: FreshBasket captures 900,000 daily 8 MB store-audit photos + cold-chain PDFs (`> 7 TB/day` raw binary volume) with a 3-year health-code retention mandate. Why did storing photos inside relational columns exhaust Dataverse `Database` capacity in 60 days, and which storage tiering architecture solves it?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Governing `Database`, `File`, & `Log` storage pools via `Dataverse Long Term Retention`, `Fabric/Synapse Link` archival, & attachment offloading
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Relational Dataverse `Database` capacity is high-cost SQL storage never meant for multi-terabyte media; offloading binaries to **Azure Blob Storage** (with lifecycle cool/archive tiering + Dataverse metadata pointers) or governed `File` storage preserves Database capacity. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Correct. Keeping relational `Database` capacity lean prevents tenant admin lockouts (`Copy`/`Restore` blocks) and controls storage overage costs.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q092 (`E5Q065`) — Architect a solution [2.10] · *Multi-Select (Select 2)*

Case study — FreshBasket Grocery Chain: FreshBasket also ingests 20,000 IoT freezer-temperature JSON pings per minute (needed for 10 days only) alongside offloading its 8 MB store-audit photos, while enforcing regional BU security on `Supermarket_Store` rows. Which two data-modeling patterns fit best? Select two.

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Dataverse `Elastic tables` (Cosmos DB horizontal partitioning + `TTL`) for high-velocity telemetry, and `File`/SharePoint/Blob offloading for binaries
- **C.** Choosing `User or Team` table ownership for BU/row/team security vs `Organization` ownership for global config tables at creation time
- **D.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **E.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). **Dataverse Elastic tables** (`TTL = 10 days`) for freezer JSON bursts plus `File`/Azure Blob binary offloading (`tbl_elastic_activity`), paired with immutable `User or Team` ownership on `Supermarket_Store` (`tbl_ownership_choice`), keep Database storage lean and secure. [Skill 2.10: Design complex data models (ownership immutability, Elastic/Activity tables, binary storage offloading) | Source: Design complex data models (ownership, Elastic/Activity tables, storage capacity) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/elastic-tables)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Correct. Elastic tables ingest tens of thousands of ephemeral JSON/IoT writes per minute with automatic `TTL` expiry without relational index contention.
- **C:** Correct. Table ownership (`User/Team` vs `Organization`) is immutable once created and determines whether BU, Team, and Hierarchy security apply.
- **D:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **E:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q093 (`E5Q045`) — Perform solution envisioning and requirement analysis [1.18] · *Multi-Select (Select 2)*

Ten days before pre-Black-Friday code freeze, brand marketing asks to embed a metaverse 3D virtual dressing room into the core OMS exception workbench. Which two actions should the Solution Architect take? Select two.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Establishing a fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **E.** Scoping a high-value `MVP` Phase 1 release using MoSCoW prioritization and formal change-request governance

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). Enforcing the `MVP` peak-season freeze boundary via MoSCoW prioritization (`scope_mvp_phased`) and routing non-essential requests to Q1 via the Change Control / ARB board (`disc_raci_governance`) protects holiday stability. [Skill 1.18: Determine MVP vs phased solution scope boundaries and govern scope changes | Source: Determine MVP vs phased solution scope and manage scope boundaries (https://learn.microsoft.com/en-us/training/paths/become-solution-architect/)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Correct. Clear architectural ownership, ARB design gates, and CoE guardrails align business, citizen makers, pro-devs, and InfoSec.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **E:** Correct. Phased MVP delivery de-risks go-live, delivers early business value, and prevents uncontrolled scope creep.

</details>

### Q094 (`E5Q019`) — Perform solution envisioning and requirement analysis [1.8] · *Multi-Select (Select 2)*

An omnichannel retailer connects Shopify Plus, Dynamics 365 Commerce/F&O, Manhattan WMS, an acquired brand’s separate Entra tenant, and store SD-WAN circuits. Which two deliverables anchor enterprise architecture discovery? Select two.

- **A.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Enterprise Architecture Context Diagram mapping systems of record, Entra tenants, hybrid networks, & sync/async SLAs
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **E.** Designating a single authoritative System of Record per entity with explicit survivorship and conflict-resolution rules

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). An Enterprise Architecture Context Diagram (mapping e-commerce/ERP/WMS/identity/network boundaries and SLAs) plus a Master-Data System-of-Record matrix prevent omnichannel inventory/price collisions. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Correct. Evaluating the enterprise landscape clarifies authoritative boundaries, identity federation, firewall paths, and integration patterns.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **E:** Correct. Every master entity (`Customer`, `Item`, `GL Account`) needs one clear authoritative owner to prevent bi-directional data corruption.

</details>

### Q095 (`E5Q005`) — Perform solution envisioning and requirement analysis [1.2] · *Single-Answer Multiple Choice*

Pop-up festival merchandisers working in desert fairgrounds with overloaded cell towers need offline SKU barcode scanning, local cart receipt capture, and automatic evening sync via a `____`.

- **A.** Canvas Power App with a `Mobile Offline` profile and device-native camera/barcode UX tailored to frontline tasks
- **B.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A Canvas Power App with a `Mobile Offline` profile delivers native camera barcode scanning and local SQLite Dataverse sync during festival connectivity blackouts. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Correct. Canvas apps give pixel-level task UX and offline-first Dataverse synchronization for field workers operating without connectivity.
- **B:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.

</details>

### Q096 (`E5Q025`) — Perform solution envisioning and requirement analysis [1.10] · *Single-Answer Multiple Choice*

Legacy loyalty records contain 2.4 million invalid `"noemail@store.com"` bogus sentinel strings used as unique keys, causing household merges to lump 80,000 strangers into one profile! Defining `____` before migration blocks sentinel-value corruption.

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Defining pre-cutover data quality standards (deduplication keys, mandatory completeness, referential integrity, & domain mappings)
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Pre-migration data quality gates strip bogus sentinel emails (`noemail@store.com`), enforce phone+name composite survivorship rules, and validate completeness before loading Dataverse. [Skill 1.10: Define use cases and data quality standards for existing data prior to migration or integration | Source: Define use cases and data quality standards for existing data (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Correct. Enforcing cleansing and deduplication gates before migration prevents garbage-in/garbage-out failures in Dataverse.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q097 (`E5Q020`) — Perform solution envisioning and requirement analysis [1.8] · *Single-Answer Multiple Choice*

Exposing internal warehouse-inventory REST services to Power Platform and franchise portals behind centralized OAuth validation, spike arrest policies, and versioned OpenAPI specs uses `____`.

- **A.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). **Azure API Management (`APIM`)** governs API security, rate throttling, caching, and OpenAPI custom-connector publishing at the enterprise edge. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q098 (`E5Q029`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

EMEA stores allow store managers to comp `$150` goodwill vouchers while Americas stores cap managers at `$100` due to regional finance policy. How should you design the process without duplicating flows?

- **A.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Standardizing a single global goodwill-comp process that reads regional currency caps from a Dataverse configuration table avoids maintaining duplicate regional flows. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q099 (`E5Q095`) — Implement the solution [3.6] · *Ordered Sequence (Multiple Choice)*

Luminary cuts over 600 global boutiques during a Sunday maintenance window. Which four-step cutover sequence prevents store edits during delta load and validates readiness before Monday opening?

- **A.** Freeze changes & verify backup restore point → Enable Dataverse `Administration mode` (blocking regular users & async jobs) → Apply Managed Upgrades & run validated delta loads → Exit `Administration mode`, smoke-test, & monitor hypercare
- **B.** Delete existing Managed Solutions in Production (erasing live tables!) → Re-import from scratch → Manually re-type Connection References & Environment Variables → Disable backups
- **C.** Ignore Dataverse Database/File storage overages blocking admin ops → Skip Solution Checker critical findings → Leave Dev URLs in Environment Variables → Disband support team at launch minute
- **D.** Allow 5,000 users to edit records during live schema upgrade and migration → Import Unmanaged solutions into Production → Skip smoke tests → Turn on auditing two months later

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Verifying restore points, enabling `Administration mode` (blocking non-admins & async jobs), applying Managed Upgrades + validated delta loads, and exiting `Administration mode` after smoke tests ensures a clean global launch. [Skill 3.6: Escalate and resolve data migration bottlenecks (BypassCustomPluginExecution, delta loads, reconciliation) | Source: Escalate and remediate enterprise data migration bottlenecks and cutover issues (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/TVF-override-plugin-execution)]

- **A:** Correct. Controlled cutovers establish restore points, engage `Administration mode` to prevent user writes and background noise, apply Managed Upgrades + delta loads, validate smoke tests, and transition to monitored hypercare.
- **B:** Incorrect. Deleting a Managed Solution erases its custom Dataverse tables and production data; always use Managed `Stage for upgrade` -> `Apply upgrade`.
- **C:** Incorrect. Exceeded Dataverse storage entitlements block environment copy/restore/admin operations and sabotage cutover readiness.
- **D:** Incorrect. Concurrent user edits during cutover cause migration collisions, lock timeouts, and inconsistent business state.

</details>

### Q100 (`E5Q031`) — Perform solution envisioning and requirement analysis [1.12] · *Single-Answer Multiple Choice*

Walk-in freezer auditors inspecting underground cold-storage warehouses with zero Wi-Fi or LTE must score 60 checklist items and capture corrective photos offline. Documenting exact offline tables and conflict handling belongs in `____`.

- **A.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **B.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **C.** Capturing Functional Requirements (persona workflows, state rules, approvals, offline CRUD scope, & statutory reports)
- **D.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Specifying offline persona CRUD scope and reconnect conflict behavior is a foundational functional requirement for Mobile Offline profiles. [Skill 1.12: Identify functional requirements across personas, business rules, approvals, and offline access | Source: Identify functional requirements across personas, offline, and workflows (https://learn.microsoft.com/en-us/power-apps/mobile/setup-mobile-offline)]

- **A:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **B:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **C:** Correct. Functional requirements specify what business behaviors and data transformations the solution must perform for each role.
- **D:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.

</details>

