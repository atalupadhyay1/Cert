# Microsoft Exam PL-600: Practice Exam 6 — Utility Transmission PCF, M&A Tenant Consolidation & Go-Live Tuning — Reviewer Study Key

**Theme:** Reusable PCF & hierarchical asset rollups, Entra PIM + CoE Managed Environments, M&A deduplication, and Quick Find index & Administration mode cutover  
**Credential:** Microsoft Certified: Power Platform Solution Architect Expert (`One active Associate certification required: Microsoft Certified: Power Platform Functional Consultant Associate (PL-200) OR Microsoft Certified: Power Platform Developer Associate (PL-400)`)  
**Study guide baseline:** September 23, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-600)  
**Lifecycle notice:** Exam PL-600 retired on June 30, 2026; succeeded by `Exam AB-100: Agentic AI Business Solutions Architect (Microsoft Certified: Agentic AI Business Solutions Architect Expert)`.  
**Questions:** `100` (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice percentages do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`E6Q004`) — Perform solution envisioning and requirement analysis [1.2] · *Multi-Select (Select 2)*

A renewable-energy cooperative needs: (1) an external portal where 220,000 rooftop-solar homeowners submit net-metering interconnection applications stored in Dataverse, and (2) an internal desktop grid-engineering app managing 8-stage interconnection studies over Dataverse. Which two components fit best? Select two.

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Canvas Power App with a `Mobile Offline` profile and device-native camera/barcode UX tailored to frontline tasks
- **C.** Model-driven Power App over Microsoft Dataverse with responsive forms, views, dashboards, & Business Process Flows
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **E.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, D` (`CSV: 3,4`)

Correct answers: C and D (are correct). Microsoft Power Pages authenticates 220,000 external homeowners via `Table Permissions`, while a Model-driven Power App manages complex 8-stage engineering studies over Dataverse. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Incorrect. Canvas apps give pixel-level task UX and offline-first Dataverse synchronization for field workers operating without connectivity.
- **C:** Correct. Model-driven apps excel at structured, data-dense back-office case and lifecycle management directly atop Dataverse security.
- **D:** Correct. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **E:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.

</details>

### Q002 (`E6Q044`) — Perform solution envisioning and requirement analysis [1.17] · *Single-Answer Multiple Choice*

Computing `CO2e_Tonnes = MWh_Generated * Grid_Emission_Factor` automatically across related Dataverse columns without C# plug-ins uses a declarative `____`.

- **A.** Addressing gaps via supported extensibility (`Custom Pages`, `PCF`, `Power Fx Formula columns`, `Custom APIs`) over bespoke clones
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Dataverse **Power Fx Formula columns** evaluate cross-column and parent-lookup calculations natively without custom plug-in code. [Skill 1.17: Address functional gaps through supported low-code/pro-code alternate solutions | Source: Address functional gaps through low-code/pro-code alternate solutions (https://learn.microsoft.com/en-us/power-platform/well-architected/operational-excellence/overview)]

- **A:** Correct. Supported platform extensibility closes UX and logic gaps while preserving Microsoft wave-update compatibility.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q003 (`E6Q021`) — Perform solution envisioning and requirement analysis [1.8] · *Single-Answer Multiple Choice*

Evaluating how acquired utility employees in `acquired-grid.com` will authenticate (`Entra B2B` vs tenant migration) and satisfy Conditional Access device compliance belongs in `____`.

- **A.** Enterprise Architecture Context Diagram mapping systems of record, Entra tenants, hybrid networks, & sync/async SLAs
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Mapping multi-tenant identity trust, licensing rules, and network paths inside the Enterprise Architecture Context Diagram surfaces M&A integration dependencies early. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Correct. Evaluating the enterprise landscape clarifies authoritative boundaries, identity federation, firewall paths, and integration patterns.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.

</details>

### Q004 (`E6Q008`) — Perform solution envisioning and requirement analysis [1.3] · *Single-Answer Multiple Choice*

Whenever a high-voltage transformer oil-dissolved-gas reading crosses an alarm threshold in Dataverse, an AC load-flow contingency simulation runs in C++/Python for 16 minutes across 90,000 grid buses. Where must that simulation run?

- **A.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **B.** Azure pro-code extension (`Azure Functions`, `Service Bus`, `AKS`, or `Azure AI Foundry`) integrated with Power Platform
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Long-running AC load-flow simulations (`> 2 minutes`) belong in Azure pro-code compute (`Azure Batch` / `AKS` / `Azure Functions`) triggered asynchronously from Dataverse. [Skill 1.3: Identify and select components from existing apps, Dynamics 365, AppSource ISVs, and Azure | Source: Evaluate Dynamics 365 apps, AppSource ISVs, and Azure extensions (https://learn.microsoft.com/en-us/training/modules/discover-customer-needs/)]

- **A:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **B:** Correct. Heavy compute, long-running algorithms (> 2 minutes), and high-throughput brokered messaging offload cleanly to Azure extensions.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q005 (`E6Q011`) — Perform solution envisioning and requirement analysis [1.5] · *Multi-Select (Select 2)*

Utility executives think pole-attachment telecom permits clear in 10 days, yet telecom carriers wait 95 days while engineers email 14 private Excel sag-tension sheets across districts. Which two discovery methods uncover true bottlenecks? Select two.

- **A.** Power Automate Process Mining & Task Mining paired with cross-functional current-state discovery workshops
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Inventorying departmental Excel macros, Access databases, and shadow-IT workarounds to retire manual data silos
- **E.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Power Automate Process/Task Mining exposes true GIS-to-structural wait queues, while shadow-IT discovery catalogs the 14 unofficial Excel sag-tension workbooks. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Correct. Combining telemetry-driven Process/Task Mining with SME workshops exposes hidden rework loops and shadow processes objectively.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Correct. Uncovering unofficial spreadsheets and shadow tools during discovery prevents critical edge cases from surfacing post-go-live.
- **E:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q006 (`E6Q013`) — Perform solution envisioning and requirement analysis [1.5] · *Single-Answer Multiple Choice*

Substation reliability engineers want citizen-maker rights to build inspection checklists while central OT/IT security governs NERC-CIP boundaries and ALM promotions. Defining `____` establishes clear guardrails.

- **A.** Establishing a fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model
- **B.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model align field makers with OT/IT security and ALM governance. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Correct. Clear architectural ownership, ARB design gates, and CoE guardrails align business, citizen makers, pro-devs, and InfoSec.
- **B:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q007 (`E6Q039`) — Perform solution envisioning and requirement analysis [1.15] · *Single-Answer Multiple Choice*

A contractor proposes installing custom Windows services directly onto Microsoft’s hosted Dataverse sandbox VM nodes to run C++ GIS projections. How must fit/gap analysis classify this?

- **A.** Structured Fit/Gap matrix scoring requirements across `Out-of-the-Box`, `Configuration`, `AppSource ISV`, & `Custom Code`
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Dataverse is multi-tenant SaaS where host OS installation is impossible/unsupported; fit/gap maps C++ GIS projections to Azure Functions / Container Apps called via APIM or Service Bus. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Correct. Formal fit/gap scoring exposes customization TCO, licensing impacts, and upgrade maintenance trade-offs transparently.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q008 (`E6Q032`) — Perform solution envisioning and requirement analysis [1.13] · *Multi-Select (Select 3)*

A national grid outage-coordination system on Power Platform undergoes formal NFR sign-off. Which three items belong in the **Non-Functional Requirements (`NFRs`)** baseline? Select three.

- **A.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **B.** Power Platform Well-Architected `Reliability` pillar (RPO/RTO targets, fault isolation, retries, & circuit breakers)
- **C.** Capturing Non-Functional Requirements (`RPO`/`RTO`, peak concurrency, `p95` latency, API volume, `WCAG 2.1 AA`, & retention)
- **D.** Designing for `WCAG 2.1 AA` accessibility (`AccessibleLabel`, `TabIndex`, contrast) and `.resx` multi-language localization
- **E.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **F.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C, D` (`CSV: 2,3,4`)

Correct answers: B, C, and D (are correct). Storm-surge concurrency, sub-second `p95` latency, API throughput, & 25-year regulatory retention (`req_nfr_spec`), `RPO <= 15m` / `RTO <= 1h` disaster-recovery targets (`wa_reliability`), and bright-sunlight/gloved `WCAG 2.1 AA` accessibility + bilingual localization (`ux_wcag_accessible`) are essential NFRs. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Incorrect. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **B:** Correct. The Reliability pillar ensures mission-critical workloads withstand transient outages, throttling, and regional faults within defined RPO/RTO bounds.
- **C:** Correct. Non-functional requirements govern architectural sizing, BCDR, licensing capacity, offline design, and security controls.
- **D:** Correct. Building accessibility and localization into initial UX components avoids expensive retrofits before public or enterprise launch.
- **E:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **F:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q009 (`E6Q020`) — Perform solution envisioning and requirement analysis [1.8] · *Single-Answer Multiple Choice*

Exposing internal Esri ArcGIS and SAP IS-U APIs to Power Platform through a single governed gateway enforcing mTLS, OAuth scopes, IP filtering, and rate limits uses `____`.

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). **Azure API Management (`APIM`)** secures, throttles, and publishes versioned OpenAPI contracts for enterprise OT/IT backend APIs. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q010 (`E6Q097`) — Implement the solution [3.7] · *Multi-Select (Select 2)*

Two Managed Solutions (`Grid_Dispatch` and `Grid_Assets`) fail pipeline import due to mutual lookup references, and an unmanaged Production form edit blocks `Grid_Dispatch v5.1` updates. Which two actions resolve both deployment issues? Select two.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **E.** Resolving deployment failures by running `Remove active customizations`, refactoring circular solution dependencies into a base layer, & validating stage JSON bindings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). Extracting shared base tables into a foundational `Grid_Core` Managed Solution (`sol_segmented_alm`) breaks circularity, while running **`Remove active customizations`** (`dep_layers_deps`) strips the blocking `Active` unmanaged layer. [Skill 3.7: Resolve deployment plan issues, Unmanaged Active Solution Layers, and circular solution dependencies | Source: Resolve deployment plan, Solution Layer, and pipeline dependency issues (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **E:** Correct. Stripping Unmanaged Active layers and decoupling circular references ensures repeatable, zero-touch Managed Solution Upgrades.

</details>

### Q011 (`E6Q029`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

North Division requires two engineer approvals for vegetation work above `$10,000` while South Division requires two approvals above `$9,500` out of habit. What should the Solution Architect guide?

- **A.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Harmonizing arbitrary historical thresholds into one standardized enterprise vegetation-approval process eliminates unnecessary maintenance debt. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.

</details>

### Q012 (`E6Q006`) — Perform solution envisioning and requirement analysis [1.2] · *Single-Answer Multiple Choice*

Grid dispatchers want an internal Microsoft Teams conversational agent grounded in approved switching-safety SOP manuals that also creates draft outage tickets in Dataverse. Proposed solution: Build a Microsoft Copilot Studio agent connected to the SOP knowledge repository and Dataverse actions. Does this meet the goal?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **C.** Microsoft Copilot Studio agent grounded in enterprise knowledge sources, Dataverse actions, & live omnichannel handoff
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — Microsoft Copilot Studio builds governed Teams agents grounded in approved enterprise SOP knowledge with native Dataverse action execution. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **C:** Correct. Copilot Studio delivers governed conversational and autonomous agents across Teams, web portals, and customer service channels.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.

</details>

### Q013 (`E6Q088`) — Implement the solution [3.3] · *Ordered Sequence (Multiple Choice)*

During winter ice-storm drills, automated AMI outage-ticket ingestion into Dataverse triggers bursts of `HTTP 429` throttling. Which four-step remediation sequence resolves Service Protection throttling cleanly?

- **A.** Buy 100 Power BI Free licenses expecting them to lift 5-minute Service Protection caps → Hardcode personal maker credentials → Ignore `x-ms-ratelimit-time-remaining-xrm-requests` headers → Discard throttled records silently
- **B.** Pinpoint throttled callers in Dataverse API analytics → Batch writes via `CreateMultiple` / `$batch` & use Change Tracking → Pool high-volume S2S loads across Entra Application Users → Honor HTTP `429` `Retry-After` backoff
- **C.** Spin up 50 parallel threads under one single user account → Retry HTTP 429 errors immediately with 0 ms delay → Replace filtered queries with full `SELECT *` scans → Open a ticket asking Microsoft to disable platform limits permanently
- **D.** Move bulk integration loops inside synchronous Dataverse plug-ins → Chain 8 child plug-in updates per row → Enable `RetrieveAllEntities` metadata calls on every transaction → Disable caching

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Pinpointing throttled callers in API analytics, batching via `CreateMultiple`/`$batch` & Change Tracking, pooling S2S Application Users, and honoring `HTTP 429` `Retry-After` backoff resolves storm-surge throttling. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Service Protection limits protect real-time platform stability per user/web server over 5-minute windows regardless of license SKU.
- **B:** Correct. Resolving Service Protection (`6,000` req / `20` min compute per 5-min window) combines batch/bulk operations, Change Tracking, pooled S2S Application Users where appropriate, and honoring `Retry-After` backoff.
- **C:** Incorrect. Immediate zero-delay retries under a single user identity amplify `HTTP 429` throttling and extend penalty windows.
- **D:** Incorrect. Heavy metadata calls and chained synchronous updates multiply execution time against the 20-minute per-5-minute sliding window limit.

</details>

### Q014 (`E6Q057`) — Architect a solution [2.6] · *Single-Answer Multiple Choice*

Control-room shift leads want live operational subgrid charts (`Active Switching Orders`, `Crew Dispatch Status`, `Critical Defects`) inside their Model-driven workspace honoring Dataverse BU security automatically. Which native option fits best?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Native Dataverse **interactive experience dashboards** and system charts deliver instant operational filtering honoring Dataverse security roles out of the box. [Skill 2.6: Design data visualization strategies across Dataverse charts, Power BI RLS, and Fabric/Synapse Link | Source: Design data visualization (Dataverse charts, Power BI RLS, Fabric/Synapse Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-synapse)]

- **A:** Correct. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.

</details>

### Q015 (`E6Q036`) — Perform solution envisioning and requirement analysis [1.14] · *Single-Answer Multiple Choice*

Unifying three merged regional utilities onto one standardized outage root-cause taxonomy (`IEEE 1366`) before configuring Dataverse tables exemplifies `____`.

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Harmonizing taxonomies and processes prior to build enables unified regulatory `SAIDI`/`SAIFI` reporting from Day 1. [Skill 1.14: Guide future-state business process optimization and standardization before automating | Source: Guide future-state business process optimization and standardization (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/overview)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.

</details>

### Q016 (`E6Q085`) — Implement the solution [3.1] · *Single-Answer Multiple Choice*

Why does **Solution Checker** flag C# plug-in classes that store mutable per-request `IOrganizationService` or `Entity` state in `private` class member fields?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Enforcing `Solution Checker` and `App Checker` gates in CI/CD pipelines alongside `Power Platform Well-Architected` design reviews
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Dataverse caches and reuses a single plug-in class instance across multiple concurrent threads; storing request state in class fields causes severe thread-safety race leaks across users! [Skill 3.1: Evaluate detailed designs and implementations with Solution Checker, App Checker, & Well-Architected | Source: Evaluate detailed designs with Solution Checker, App Checker, & Well-Architected (https://learn.microsoft.com/en-us/power-platform/alm/use-powershell-cmdlets-solution-checker)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Correct. Solution Checker flags unbounded queries and sync plug-in anti-patterns, while App Checker catches delegation warnings and WCAG errors before release.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

## Case Study Vignette — Boreal Hydro Operations

> Boreal Hydro Operations experienced severe afternoon slowdowns in Production Model-driven views after going live with 18 million meter-ticket rows. Telemetry revealed wildcard `*4491` Quick Find searches scanning 14 unindexed text columns, 6 synchronous post-update plug-ins chaining external HTTP calls, and unmanaged hotfixes blocking emergency pipeline deployments.

### Q017 (`E6Q093`) — Implement the solution [3.5] · *Single-Answer Multiple Choice*

Case study — Boreal Hydro Operations: Afternoon views stall across 18M `Meter_Ticket` rows from `*4491` Quick Find wildcards scanning 14 unindexed columns and 6 sync HTTP plug-ins. Proposed solution: Limit Quick Find to indexed columns with prefix/Dataverse Search and move the 6 HTTP plug-ins to async Service Bus patterns. Does this fix the slowdowns?

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Fixing slowness via delegable `Filter`/`StartsWith` Canvas queries, indexed `Quick Find` columns (no leading `*` wildcards), & async plug-in refactoring
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — eliminating leading-wildcard full scans across 14 unindexed columns and decoupling synchronous HTTP calls into asynchronous Service Bus patterns restores sub-second SQL view and save performance. [Skill 3.5: Identify and resolve Canvas, Model-driven, Quick Find index, and synchronous plug-in performance issues | Source: Identify and resolve Canvas, Model-driven, Dataverse, & plug-in performance issues (https://learn.microsoft.com/en-us/power-platform/well-architected/performance-efficiency/overview)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Correct. Eliminating `N+1` gallery `LookUp`s, non-delegable predicates, leading-wildcard full table scans, and chained sync plug-ins restores sub-second UX.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q018 (`E6Q098`) — Implement the solution [3.7] · *Single-Answer Multiple Choice*

Case study — Boreal Hydro Operations: Emergency Managed pipeline promotions failed to apply updated views and ribbons in Production because previous admins edited components directly inside Production (`Active` unmanaged layer). Which specific action in Solution Layers unblocks the Managed changes without losing data?

- **A.** Resolving deployment failures by running `Remove active customizations`, refactoring circular solution dependencies into a base layer, & validating stage JSON bindings
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Inspecting **Solution Layers** on the affected views/forms/ribbons and executing **`Remove active customizations`** removes the top unmanaged `Active` layer so the underlying Managed upgrade takes effect immediately. [Skill 3.7: Resolve deployment plan issues, Unmanaged Active Solution Layers, and circular solution dependencies | Source: Resolve deployment plan, Solution Layer, and pipeline dependency issues (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Correct. Stripping Unmanaged Active layers and decoupling circular references ensures repeatable, zero-touch Managed Solution Upgrades.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q019 (`E6Q099`) — Implement the solution [3.8] · *Single-Answer Multiple Choice*

Case study — Boreal Hydro Operations: Before deploying the weekend remediation release across 18 million meter tickets, Boreal Hydro must block 2,400 dispatchers and linemen from editing rows, halt background async jobs, run smoke tests, and monitor KQL telemetry post-launch. Which cutover governance pattern applies?

- **A.** Enabling Dataverse `Administration mode` (blocking non-admins & background jobs) during cutover, followed by smoke tests & Application Insights hypercare
- **B.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enabling Dataverse **`Administration mode`** (with background operations disabled) during upgrade + smoke testing, followed by an **Application Insights hypercare** war room, ensures a quiet, verified cutover. [Skill 3.8: Identify go-live readiness gates, execute Administration mode cutovers, and manage hypercare telemetry | Source: Assess go-live readiness factors, Administration mode, and hypercare remediation (https://learn.microsoft.com/en-us/power-platform/admin/admin-mode)]

- **A:** Correct. `Administration mode` guarantees a quiet database during final schema upgrade and delta migration before opening Production to users.
- **B:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q020 (`E6Q084`) — Implement the solution [3.1] · *Single-Answer Multiple Choice*

Before promoting `Grid_FieldApp v4.0` to UAT, automated CI gates run `pac solution check` and **App Checker**, catching a synchronous plug-in calling `HttpClient.PostAsync` and 9 Canvas delegation warnings. Which validation discipline is operating?

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Enforcing `Solution Checker` and `App Checker` gates in CI/CD pipelines alongside `Power Platform Well-Architected` design reviews
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). **Solution Checker** and **App Checker** enforce automated static code, delegation, and accessibility gates aligned with Power Platform Well-Architected. [Skill 3.1: Evaluate detailed designs and implementations with Solution Checker, App Checker, & Well-Architected | Source: Evaluate detailed designs with Solution Checker, App Checker, & Well-Architected (https://learn.microsoft.com/en-us/power-platform/alm/use-powershell-cmdlets-solution-checker)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Solution Checker flags unbounded queries and sync plug-in anti-patterns, while App Checker catches delegation warnings and WCAG errors before release.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q021 (`E6Q023`) — Perform solution envisioning and requirement analysis [1.9] · *Single-Answer Multiple Choice*

Allowing field crews in Dataverse to edit GPS tower coordinates mastered in Esri ArcGIS caused switching-map discrepancies. Enforcing `____` keeps Esri GIS authoritative for spatial coordinates while Dataverse masters inspection findings.

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **D.** Designating a single authoritative System of Record per entity with explicit survivorship and conflict-resolution rules

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Explicit System-of-Record ownership rules per entity/attribute prevent field apps from corrupting authoritative spatial GIS masters. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **D:** Correct. Every master entity (`Customer`, `Item`, `GL Account`) needs one clear authoritative owner to prevent bi-directional data corruption.

</details>

### Q022 (`E6Q017`) — Perform solution envisioning and requirement analysis [1.7] · *Single-Answer Multiple Choice*

A VP of Grid Operations says: `"Make storm restoration coordination smoother this winter."` How should the Solution Architect rewrite this into valid key success criteria?

- **A.** Defining baseline-backed `SMART` success KPIs (cycle-time reduction, error-rate drop, SLA adherence, & active adoption %)
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Defining baseline-backed `SMART` KPIs (such as cutting crew dispatch assignment latency from `48 minutes` to `< 5 minutes`, reducing duplicate truck rolls by `60%`, and reaching `95%` crew mobile adoption) establishes measurable ROI. [Skill 1.7: Review and validate measurable key success criteria, KPIs, and adoption targets | Source: Review measurable key success criteria, KPIs, and adoption targets (https://learn.microsoft.com/en-us/power-platform/guidance/adoption/measure-business-value)]

- **A:** Correct. Quantifiable KPIs anchored to current-state baselines let stakeholders verify objective ROI after go-live.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q023 (`E6Q063`) — Architect a solution [2.9] · *Single-Answer Multiple Choice*

Grid engineers inside a Model-driven app need live online read-only subgrid visibility into 90 million archival lightning-strike records hosted in Azure SQL / Fabric without copying them into Dataverse storage. Using `____` surfaces them in place.

- **A.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Replicating data into native Dataverse tables (`Dataflows` / `ADF`) when Mobile Offline, row-level security roles, auditing, or SLAs are required
- **D.** Using the `Virtual Connector Provider` (`SQL Server`, `SharePoint`, `Fabric`) to expose external tables in Dataverse with low-code setup

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). The **`Virtual Connector Provider`** (`SQL Server` / `Fabric`) exposes external tables live as Dataverse **Virtual Tables** with zero Dataverse Database duplication. [Skill 2.9: Determine when to connect external data in place (Virtual tables) versus import/replicate into Dataverse | Source: Connect external data in place (Virtual tables) vs import/replicate into Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-virtual-entities)]

- **A:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Incorrect. Virtual tables do not support Mobile Offline sync, Dataverse row-level User/Team ownership, or native column auditing.
- **D:** Correct. The Virtual Connector Provider creates Virtual Tables over supported connectors without authoring custom C# data-provider plug-ins.

</details>

### Q024 (`E6Q062`) — Architect a solution [2.8] · *Single-Answer Multiple Choice*

Reassigning a `Transmission_District` record owning 300,000 historical `Meter_Ticket` child rows triggered SQL timeouts because the `1:N` relationship was `Parental`. Switching relationship cascading to `____` eliminates historic reassignment storms.

- **A.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Configuring `Custom` / `Referential` cascading (avoiding unintended `Parental` `Cascade All` reparent storms) and manual `N:N` intersect tables
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Configuring `Custom` cascading (`Cascade None` or `Cascade Active` on `Assign`/`Share`/`Reparent`) stops synchronous updates and `POA` sharing storms across historical closed tickets. [Skill 2.8: Design Dataverse relationships (1:N, N:N, hierarchical, polymorphic) and cascading behaviors | Source: Design Dataverse relationships (1:N, N:N, hierarchical) & cascading behaviors (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Correct. Replacing `Parental` cascading on high-volume child tables prevents `POA` sharing storms, and manual `N:N` tables store rich relationship attributes.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q025 (`E6Q034`) — Perform solution envisioning and requirement analysis [1.13] · *Single-Answer Multiple Choice*

Energy regulators mandate retaining immutable carbon-credit and switching audit histories for `20 years` without bloating active Dataverse Database capacity. Which governance design satisfies this NFR?

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Governing `Database`, `File`, & `Log` storage pools via `Dataverse Long Term Retention`, `Fabric/Synapse Link` archival, & attachment offloading
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Tiering historical audit and transactional records via **Dataverse Long Term Retention** and `Fabric/Synapse Link` archival preserves 20-year auditability while keeping operational Database storage lean. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Correct. Keeping relational `Database` capacity lean prevents tenant admin lockouts (`Copy`/`Restore` blocks) and controls storage overage costs.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q026 (`E6Q043`) — Perform solution envisioning and requirement analysis [1.17] · *Multi-Select (Select 2)*

Carbon-exchange traders need: (1) a full-screen multi-source order-matching blotter dialog launched inside their Model-driven app, and (2) a strongly typed server-side `RetireCreditBatch` operation callable from portals, flows, and external verifiers. Which two supported extensibility options fit best? Select two.

- **A.** Defining solution-aware Dataverse `Custom APIs` exposing strongly typed request/response contracts for internal and external callers
- **B.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Addressing gaps via supported extensibility (`Custom Pages`, `PCF`, `Power Fx Formula columns`, `Custom APIs`) over bespoke clones
- **E.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Model-driven **`Custom Pages`** (`gap_lowcode_alt`) deliver rich multi-connector full-screen dialogs, while solution-aware Dataverse **`Custom APIs`** (`integ_custom_api`) expose strongly typed reusable OData operations. [Skill 1.17: Address functional gaps through supported low-code/pro-code alternate solutions | Source: Address functional gaps through low-code/pro-code alternate solutions (https://learn.microsoft.com/en-us/power-platform/well-architected/operational-excellence/overview)]

- **A:** Correct. Custom APIs replace legacy Custom Process Actions with code-first, solution-aware OData bound/unbound operations and granular privilege checks.
- **B:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Correct. Supported platform extensibility closes UX and logic gaps while preserving Microsoft wave-update compatibility.
- **E:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q027 (`E6Q071`) — Architect a solution [2.12] · *Single-Answer Multiple Choice*

Storm-room dispatchers in Microsoft Teams channels want automated Dataverse `Feeder_Lockout` cards with inline `"Acknowledge & Dispatch"` buttons plus Exchange Server-Side Sync for regulatory outage emails. Which native pairing applies?

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Integrating Microsoft Teams (`Adaptive Cards` / embedded apps), Dynamics 365 F&O `Dual-write` + `Business Events`, & `Server-Side Sync`
- **D.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Microsoft Teams **Adaptive Cards** paired with **Exchange Server-Side Synchronization** streamline storm-room collaboration directly inside Dataverse. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Correct. Dual-write provides near-real-time bi-directional Dataverse-to-F&O sync, while Teams Adaptive Cards meet users directly in collaboration channels.
- **D:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.

</details>

### Q028 (`E6Q069`) — Architect a solution [2.12] · *Multi-Select (Select 3)*

An energy enterprise connects Dataverse, SAP S/4HANA, Dynamics 365 Finance, Teams storm channels, and external carbon verifiers. Which three integration patterns work together cleanly? Select three.

- **A.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`
- **E.** Integrating Microsoft Teams (`Adaptive Cards` / embedded apps), Dynamics 365 F&O `Dual-write` + `Business Events`, & `Server-Side Sync`
- **F.** Defining solution-aware Dataverse `Custom APIs` exposing strongly typed request/response contracts for internal and external callers

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E, F` (`CSV: 4,5,6`)

Correct answers: D, E, and F (are correct). `APIM` + `Azure Service Bus` / `Event Grid` with DLQ (`integ_async_asb_apim`), `Teams Adaptive Cards` + `Dynamics 365 Dual-write` / `Business Events` (`integ_teams_sp_d365`), and solution-aware Dataverse `Custom APIs` (`integ_custom_api`) provide a unified integration architecture. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.
- **E:** Correct. Dual-write provides near-real-time bi-directional Dataverse-to-F&O sync, while Teams Adaptive Cards meet users directly in collaboration channels.
- **F:** Correct. Custom APIs replace legacy Custom Process Actions with code-first, solution-aware OData bound/unbound operations and granular privilege checks.

</details>

### Q029 (`E6Q035`) — Perform solution envisioning and requirement analysis [1.14] · *Single-Answer Multiple Choice*

Substation crews currently fill out paper switching logs, radio values to a clerk who types them into Excel, and mail carbon copies to compliance. Proposed solution: Standardize and optimize a single digital future-state switching process in Dataverse before building mobile and control-room screens. Should you recommend this?

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes — eliminating radio-to-Excel transcription and paper carbon copies through future-state process optimization cuts errors and latency dramatically. [Skill 1.14: Guide future-state business process optimization and standardization before automating | Source: Guide future-state business process optimization and standardization (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/overview)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q030 (`E6Q003`) — Perform solution envisioning and requirement analysis [1.1] · *Single-Answer Multiple Choice*

Critical-infrastructure NERC-CIP auditors mandate defense-in-depth identity, zero standing privileges, endpoint DLP filtering, and customer-managed encryption keys under the Well-Architected `____` pillar.

- **A.** Power Platform Well-Architected `Security` pillar (Zero Trust Entra identity, least privilege, DLP, & encryption)
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Power Platform Well-Architected `Performance Efficiency` pillar (delegable queries, API throughput budgets, & elastic scaling)
- **D.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). The `Security` pillar governs Zero Trust Entra Conditional Access, least-privilege PIM, DLP endpoint rules, CMK, and Customer Lockbox. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Correct. The Security pillar protects confidentiality and integrity through Entra Conditional Access, least-privilege roles, DLP endpoint rules, and CMK/Lockbox.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Performance Efficiency optimizes response latency and resource utilization via query delegation, indexing, batching, and Elastic/async patterns.
- **D:** Incorrect. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.

</details>

### Q031 (`E6Q015`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

Seventy outage-escalation flows run inside the `Default` environment under a retired chief dispatcher’s personal login with zero DLP rules. Which mitigation strategy resolves this exposure?

- **A.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **B.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)
- **C.** Mitigating single-maker bus-factor risk, unmonitored personal flows, & technical debt via Managed Environments and CoE
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Moving critical workflows into **Managed Environments** owned by Service Principals with tenant DLP policies and CoE Starter Kit monitoring eliminates bus-factor and exfiltration risks. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **B:** Incorrect. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.
- **C:** Correct. Unmanaged citizen sprawl and bespoke code without ALM pipelines represent top organizational operational risks.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q032 (`E6Q054`) — Architect a solution [2.4] · *Single-Answer Multiple Choice*

Why should meter-disconnect technicians receive a focused 4-screen task app rather than the full 80-table enterprise Finance & Regulatory Model-driven workspace?

- **A.** Grouping capabilities into role- and task-specific apps (offline Canvas for field crews, Model-driven for back-office, Power Pages for externals)
- **B.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Focused task grouping shrinks mobile offline metadata sync, minimizes cognitive clutter, and enforces least-privilege attack surfaces. [Skill 2.4: Design apps by grouping required features based on persona, role, task, and offline needs | Source: Design role-based and task-based app experiences across form factors (https://learn.microsoft.com/en-us/power-apps/guidance/planning/app-design)]

- **A:** Correct. Task-focused apps per persona outperform bloated one-size-fits-all apps in load speed, offline footprint, and usability.
- **B:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q033 (`E6Q019`) — Perform solution envisioning and requirement analysis [1.8] · *Multi-Select (Select 2)*

Following an acquisition, an energy utility spans SAP S/4HANA IS-U, Esri ArcGIS Utility Network, two separate Microsoft Entra tenants, and OT air-gapped DMZ firewalls. Which two deliverables must anchor enterprise landscape analysis? Select two.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Designating a single authoritative System of Record per entity with explicit survivorship and conflict-resolution rules
- **C.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **D.** Enterprise Architecture Context Diagram mapping systems of record, Entra tenants, hybrid networks, & sync/async SLAs
- **E.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). An Enterprise Architecture Context Diagram (mapping GIS/SAP/identity/DMZ network boundaries and SLAs) plus a Master-Data System-of-Record matrix prevent asset and customer drift. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Correct. Every master entity (`Customer`, `Item`, `GL Account`) needs one clear authoritative owner to prevent bi-directional data corruption.
- **C:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **D:** Correct. Evaluating the enterprise landscape clarifies authoritative boundaries, identity federation, firewall paths, and integration patterns.
- **E:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.

</details>

### Q034 (`E6Q051`) — Architect a solution [2.3] · *Single-Answer Multiple Choice*

Seven utility project squads need shared NERC-CIP warning headers, meter-checksum child flows, and SAP PM connectors, backed by standardized `ERD`, `Sequence`, and `Context` architecture diagrams. Which strategy enforces reuse?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Reusing `Component Libraries`, `PCF`, `Child Flows`, & `Custom Connectors`, documented via `ERD`, `Sequence`, & `Context` diagrams
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Maintaining shared `Component Libraries`, `PCF` controls, `Child Cloud Flows`, and `Custom Connectors` — documented with `ERD`, `Sequence`, and `Context` diagrams — eliminates duplicate debt across squads. [Skill 2.3: Maximize component reuse (PCF, Component Libraries, Child Flows) and communicate designs visually | Source: Maximize component reuse (PCF, Component Libraries, Child Flows) & visual diagrams (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Correct. Shared component catalogs eliminate duplicate maintenance, while visual architecture diagrams align technical and business stakeholders.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q035 (`E6Q087`) — Implement the solution [3.2] · *Single-Answer Multiple Choice*

A developer must stop traders from reading restricted pricing columns over Power BI and `/api/data/v9.2/`. Proposed solution: Hide the pricing tab on forms using JavaScript `formContext.ui.tabs.get("tab_pricing").setVisible(false)`. Does this secure the data boundary?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **C.** Auditing server-side `Security Roles`, `Column Security`, & `Power Pages Table Permissions` rather than trusting client-side UI rules
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). No — client JavaScript `setVisible(false)` is purely cosmetic UI customization; server-side Dataverse `Security Roles` and `Column Security Profiles` are required to enforce real security boundaries. [Skill 3.2: Review security across Business Rules, Security Roles, Entra Conditional Access, & security boundaries | Source: Review end-to-end security across Business Rules, Roles, Entra ID, & boundaries (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **C:** Correct. Client JavaScript and `Form`-scoped Business Rules never block Web API/OData access; security boundaries must be enforced server-side in Dataverse.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q036 (`E6Q053`) — Architect a solution [2.4] · *Single-Answer Multiple Choice*

A utility serves three distinct personas: offline helicopter linemen on iPads, control-room dispatchers on 4-monitor desktops, and corporate carbon-credit buyers online. Proposed solution: Group features into role- and task-specific apps (offline Canvas app for linemen, Model-driven app for dispatchers, Power Pages portal for buyers). Is this optimal?

- **A.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **B.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **C.** Grouping capabilities into role- and task-specific apps (offline Canvas for field crews, Model-driven for back-office, Power Pages for externals)
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — persona- and task-aligned apps optimize offline sync payloads, load performance, UX density, and external licensing. [Skill 2.4: Design apps by grouping required features based on persona, role, task, and offline needs | Source: Design role-based and task-based app experiences across form factors (https://learn.microsoft.com/en-us/power-apps/guidance/planning/app-design)]

- **A:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **B:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **C:** Correct. Task-focused apps per persona outperform bloated one-size-fits-all apps in load speed, offline footprint, and usability.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q037 (`E6Q012`) — Perform solution envisioning and requirement analysis [1.5] · *Single-Answer Multiple Choice*

Analyzing SAP PM work-order status logs (`Order_ID`, `Status`, `Changed_At`, `District`) inside `____` reveals that 41% of crew dispatches bounce back to `"Awaiting Switching Permit"` twice.

- **A.** Power Automate Process Mining & Task Mining paired with cross-functional current-state discovery workshops
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Power Automate **Process Mining** uncovers hidden rework loops and district cycle-time outliers directly from timestamped SAP status logs. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Correct. Combining telemetry-driven Process/Task Mining with SME workshops exposes hidden rework loops and shadow processes objectively.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.

</details>

### Q038 (`E6Q024`) — Perform solution envisioning and requirement analysis [1.9] · *Single-Answer Multiple Choice*

Modeling corporate energy buyers as `Account`, site facility managers as `Contact`, and field site visits as `Appointment` / `Activity` aligns utility schemas with `____`.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Aligning data entities to the Microsoft Common Data Model (`CDM`) standard tables (`Account`, `Contact`, `Activity`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Aligning schemas to the Microsoft Common Data Model (`CDM`) ensures native Dynamics 365 Field Service, Sales, Power Pages, and ISV compatibility. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Correct. Extending standard CDM tables preserves native Dynamics 365, AppSource ISV, Exchange, and AI Copilot interoperability.

</details>

### Q039 (`E6Q096`) — Implement the solution [3.6] · *Single-Answer Multiple Choice*

Passing `BypassBusinessLogicExecution = CustomSync,CustomAsync` (`BypassCustomPluginExecution`) while running Change Tracking delta loads and financial hash-total checks combines `____` with post-load reconciliation.

- **A.** Accelerating bulk loads with `BypassCustomPluginExecution` (`BypassBusinessLogicExecution`), disabled flows/search indexes, & parallel `CreateMultiple` batches
- **B.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Suppressing non-essential custom business logic (`mig_bypass_cutover`) and verifying delta checksums keeps multi-million-row utility cutovers inside tight weekend freeze windows. [Skill 3.6: Escalate and resolve data migration bottlenecks (BypassCustomPluginExecution, delta loads, reconciliation) | Source: Escalate and remediate enterprise data migration bottlenecks and cutover issues (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/TVF-override-plugin-execution)]

- **A:** Correct. Bypassing non-essential custom sync/async logic and disabling cloud flows during cutover prevents throttling and unintended notification storms.
- **B:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q040 (`E6Q007`) — Perform solution envisioning and requirement analysis [1.3] · *Single-Answer Multiple Choice*

Right-of-way land agents receive 18,000 scanned vegetation-easement deeds monthly and want automated extraction of `Easement_Book_Page`, `Tower_Span`, and landowner signatures inside Power Automate. Which component fits best?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Azure pro-code extension (`Azure Functions`, `Service Bus`, `AKS`, or `Azure AI Foundry`) integrated with Power Platform
- **C.** AI Builder prebuilt/custom document processing, text classification, & AI Prompts integrated natively in Power Platform
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). AI Builder custom document processing extracts structured fields from scanned easement deeds directly inside Power Automate cloud flows. [Skill 1.3: Identify and select components from existing apps, Dynamics 365, AppSource ISVs, and Azure | Source: Evaluate Dynamics 365 apps, AppSource ISVs, and Azure extensions (https://learn.microsoft.com/en-us/training/modules/discover-customer-needs/)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Incorrect. Heavy compute, long-running algorithms (> 2 minutes), and high-throughput brokered messaging offload cleanly to Azure extensions.
- **C:** Correct. AI Builder embeds governed document extraction and generative AI prompts directly inside flows and apps without custom ML infrastructure.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.

</details>

### Q041 (`E6Q064`) — Architect a solution [2.9] · *Single-Answer Multiple Choice*

Why must `Tower_Inspection` rows created and edited by helicopter crews flying 7 hours offline in mountain corridors reside in **native Dataverse tables** rather than Virtual Tables?

- **A.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **B.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **C.** Replicating data into native Dataverse tables (`Dataflows` / `ADF`) when Mobile Offline, row-level security roles, auditing, or SLAs are required
- **D.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Virtual Tables require live online connectivity and do not support `Mobile Offline` sync, `User/Team` BU security, or native Dataverse column auditing. [Skill 2.9: Determine when to connect external data in place (Virtual tables) versus import/replicate into Dataverse | Source: Connect external data in place (Virtual tables) vs import/replicate into Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-virtual-entities)]

- **A:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **B:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **C:** Correct. Virtual tables do not support Mobile Offline sync, Dataverse row-level User/Team ownership, or native column auditing.
- **D:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.

</details>

## Case Study Vignette — GridVantage Transmission

> GridVantage Transmission manages 140,000 high-voltage transmission towers inspected by helicopter and ground crews using Dynamics 365 Field Service & Power Apps. Crews need Reusable PCF geospatial map controls across both Model-driven and Canvas screens, hierarchical asset rollups (`Substation -> Feeder -> Tower`), and SAP PM work-order synchronization.

### Q042 (`E6Q041`) — Perform solution envisioning and requirement analysis [1.16] · *Single-Answer Multiple Choice*

Case study — GridVantage Transmission: GridVantage inspects 140,000 high-voltage towers with helicopter and ground crews requiring Preventive Maintenance schedules, asset hierarchies, crew skills, and offline mobile execution. Should GridVantage build custom `new_workorder` tables or adopt Dynamics 365 Field Service?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Dynamics 365 first-party app (`Sales`, `Customer Service`, or `Field Service`) leveraging native schemas, SLAs, & RSO scheduling
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). **Dynamics 365 Field Service** natively delivers `Work Orders`, `Customer Assets` hierarchies, preventive maintenance agreements, crew scheduling, and offline mobile capabilities. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Adopting Dynamics 365 first-party apps avoids reinventing complex case routing, omnichannel queues, or Resource Scheduling Optimization.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q043 (`E6Q050`) — Architect a solution [2.2] · *Single-Answer Multiple Choice*

Case study — GridVantage Transmission: GridVantage needs a **single reusable geospatial transmission-corridor map control** (written in TypeScript/Mapbox GL) that embeds cleanly inside **both** Model-driven `Work Order` forms and offline-capable Canvas crew screens. Which extensibility technology should you select?

- **A.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **B.** Validating interactive UX prototypes (`Figma-to-App` / `Custom Pages`) early and building `PCF` controls for specialized UI gaps
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A **Power Apps Component Framework (`PCF`)** code component packages TypeScript/React visual controls once for native reuse across Model-driven apps, Canvas apps, and Power Pages. [Skill 2.2: Identify app customization approaches and validate interactive user experience prototypes | Source: Select customization approaches for existing apps and validate UX prototypes (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/design-consistency)]

- **A:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **B:** Correct. Interactive prototyping validates user journeys cheaply, while Power Apps Component Framework (`PCF`) renders reusable custom TypeScript/React controls.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q044 (`E6Q061`) — Architect a solution [2.8] · *Single-Answer Multiple Choice*

Case study — GridVantage Transmission: GridVantage models its physical grid hierarchy (`Substation -> Feeder -> Transmission Tower`) and needs native hierarchical visual cards plus `Under` OData rollup queries for open defects beneath any Substation, alongside `Land_Easement` lookups pointing to either an individual `Contact` or corporate `Account`. Which Dataverse relationship features model both?

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **C.** Modeling self-referential `Hierarchical` (`1:N` `Under` queries) and `Polymorphic` (`Customer` / multi-table) relationships
- **D.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A self-referential `1:N` **Hierarchical** asset relationship supports visual hierarchy trees and `Under` rollups across `Substation -> Feeder -> Tower`, while **Polymorphic** (`Customer` / multi-table) lookups link `Contact` or `Account` cleanly. [Skill 2.8: Design Dataverse relationships (1:N, N:N, hierarchical, polymorphic) and cascading behaviors | Source: Design Dataverse relationships (1:N, N:N, hierarchical) & cascading behaviors (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **C:** Correct. Hierarchical relationships support native visual hierarchy rollups and `Under` OData operators across parent-child trees.
- **D:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.

</details>

### Q045 (`E6Q031`) — Perform solution envisioning and requirement analysis [1.12] · *Single-Answer Multiple Choice*

Transmission helicopter crews flying mountain corridors with zero cellular reception for 7 hours must read tower histories, log thermal anomalies, and attach infrared photos offline. Capturing exact offline CRUD scope belongs in `____`.

- **A.** Capturing Functional Requirements (persona workflows, state rules, approvals, offline CRUD scope, & statutory reports)
- **B.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **C.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **D.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Specifying disconnected persona CRUD tables, photo sync rules, and conflict behavior defines core Mobile Offline functional requirements. [Skill 1.12: Identify functional requirements across personas, business rules, approvals, and offline access | Source: Identify functional requirements across personas, offline, and workflows (https://learn.microsoft.com/en-us/power-apps/mobile/setup-mobile-offline)]

- **A:** Correct. Functional requirements specify what business behaviors and data transformations the solution must perform for each role.
- **B:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **C:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **D:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.

</details>

### Q046 (`E6Q026`) — Perform solution envisioning and requirement analysis [1.10] · *Single-Answer Multiple Choice*

Asset engineers want AI Builder to predict transformer bushing failures from 10 years of oil-test logs where 48% of pre-2020 rows omitted ambient temperature and unit labels (`ppm` vs `%`). What must precede AI modeling?

- **A.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Defining pre-cutover data quality standards (deduplication keys, mandatory completeness, referential integrity, & domain mappings)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enforcing unit normalization, completeness thresholds, and cohort cleansing ensures reliable AI Builder predictive training. [Skill 1.10: Define use cases and data quality standards for existing data prior to migration or integration | Source: Define use cases and data quality standards for existing data (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Correct. Enforcing cleansing and deduplication gates before migration prevents garbage-in/garbage-out failures in Dataverse.

</details>

### Q047 (`E6Q027`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

A chief lineman demands: `"Give me a yellow screen with 31 dropdown menus matching our 2003 clipboard sheet."` How should the Solution Architect refine this request?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Refining prescriptive wishes into persona-based `User Stories` (`As a ... I need ... so that ...`) with testable Acceptance Criteria

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Refining UI-prescriptive demands into persona-based `User Stories` (`As a Helicopter Lineman, I need 3-tap insulator-flashover logging with auto-tagged tower IDs so hazards route to dispatch immediately`) with testable Acceptance Criteria drives superior UX. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Correct. Outcome-oriented User Stories decouple business intent from premature UI assumptions and anchor QA test cases.

</details>

### Q048 (`E6Q091`) — Implement the solution [3.4] · *Multi-Select (Select 2)*

Two concurrent automated dispatchers overwrite each other’s `Assigned_Crew` on the same `Outage_Ticket` row, while a bi-directional SAP sync flow triggers itself infinitely on every column edit, filling `Log` capacity. Which two fixes resolve both defects? Select two.

- **A.** Governing `Database`, `File`, & `Log` storage pools via `Dataverse Long Term Retention`, `Fabric/Synapse Link` archival, & attachment offloading
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Resolving automation/integration conflicts via `Select columns` (`filteringattributes`), `Trigger Conditions`, plug-in `Depth` checks, & `ETag` (`If-Match`) optimistic concurrency
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **E.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). Enforcing **`ETag` (`If-Match`) optimistic concurrency** plus `Select columns` / `Trigger Conditions` / actor exclusions (`res_conflict_loops`) and governing `Log`/`Database` storage pools (`cap_storage_tiering`) eliminate race overwrites and infinite loops. [Skill 3.4: Assess storage/resource impact and resolve automation loops, race conditions, & integration conflicts | Source: Assess storage/resource impact and resolve automation & integration conflicts (https://learn.microsoft.com/en-us/power-platform/admin/capacity-storage)]

- **A:** Correct. Keeping relational `Database` capacity lean prevents tenant admin lockouts (`Copy`/`Restore` blocks) and controls storage overage costs.
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Correct. Column filters, actor exclusions, and `If-Match` row-version headers eliminate infinite ping-pong loops and silent lost-update race conditions.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **E:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q049 (`E6Q065`) — Architect a solution [2.10] · *Multi-Select (Select 2)*

A smart-substation platform ingests 35,000 phasor-telemetry JSON events per minute (needed for 14 days only) and 50 MB drone LiDAR point-cloud files while requiring regional Business Unit ownership on `Substation` rows. Which two data-modeling choices apply? Select two.

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **D.** Choosing `User or Team` table ownership for BU/row/team security vs `Organization` ownership for global config tables at creation time
- **E.** Dataverse `Elastic tables` (Cosmos DB horizontal partitioning + `TTL`) for high-velocity telemetry, and `File`/SharePoint/Blob offloading for binaries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). **Dataverse Elastic tables** (`TTL = 14 days`) for phasor JSON bursts plus Azure Blob / `File` offloading for 50 MB LiDAR files (`tbl_elastic_activity`), paired with immutable `User or Team` ownership on `Substation` (`tbl_ownership_choice`), keep relational storage fast and secure. [Skill 2.10: Design complex data models (ownership immutability, Elastic/Activity tables, binary storage offloading) | Source: Design complex data models (ownership, Elastic/Activity tables, storage capacity) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/elastic-tables)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **D:** Correct. Table ownership (`User/Team` vs `Organization`) is immutable once created and determines whether BU, Team, and Hierarchy security apply.
- **E:** Correct. Elastic tables ingest tens of thousands of ephemeral JSON/IoT writes per minute with automatic `TTL` expiry without relational index contention.

</details>

### Q050 (`E6Q049`) — Architect a solution [2.2] · *Single-Answer Multiple Choice*

Helicopter linemen wearing flight gloves need to test touch target sizes and high-glare contrast on tablet mockups before developers code custom map widgets. What should you do first?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Validating interactive UX prototypes (`Figma-to-App` / `Custom Pages`) early and building `PCF` controls for specialized UI gaps
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Validating interactive `Figma` / rapid tablet prototypes with gloved flight crews first confirms usability cheaply before building specialized `PCF` controls. [Skill 2.2: Identify app customization approaches and validate interactive user experience prototypes | Source: Select customization approaches for existing apps and validate UX prototypes (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/design-consistency)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Correct. Interactive prototyping validates user journeys cheaply, while Power Apps Component Framework (`PCF`) renders reusable custom TypeScript/React controls.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q051 (`E6Q046`) — Perform solution envisioning and requirement analysis [1.18] · *Single-Answer Multiple Choice*

Locking `Must-have` tower-safety and switching features into Release 1 while deferring `Could-have` drone-video highlight reels to Release 2 applies `____`.

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Scoping a high-value `MVP` Phase 1 release using MoSCoW prioritization and formal change-request governance

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). MoSCoW-driven `MVP` phasing ensures regulatory safety scope ships on time without scope-creep delays. [Skill 1.18: Determine MVP vs phased solution scope boundaries and govern scope changes | Source: Determine MVP vs phased solution scope and manage scope boundaries (https://learn.microsoft.com/en-us/training/paths/become-solution-architect/)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Correct. Phased MVP delivery de-risks go-live, delivers early business value, and prevents uncontrolled scope creep.

</details>

### Q052 (`E6Q001`) — Perform solution envisioning and requirement analysis [1.1] · *Ordered Sequence (Multiple Choice)*

A national electric-grid operator is replacing legacy substation inspection and carbon-accounting systems with Microsoft Power Platform and asks you to sequence envisioning through Well-Architected alignment. Which four-step order should you recommend?

- **A.** Grant System Administrator to all stakeholders → Build prototypes in personal My Flows → Skip security & residency discovery → Export Unmanaged Default Solution to Production
- **B.** Capture business outcomes, KPIs, & risk constraints → Map current-state processes & existing enterprise systems → Refine functional & non-functional requirements → Align target architecture to Power Platform Well-Architected pillars
- **C.** Copy every legacy Access table 1-for-1 into Dataverse → Replicate broken manual steps verbatim → Ignore API and storage limits → Run fit/gap analysis during user acceptance testing
- **D.** Write custom C# plug-ins on Day 1 → Purchase all Dynamics 365 licenses blindly → Skip current-state discovery → Capture non-functional requirements after Production go-live

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Grid-utility envisioning defines NERC-CIP/outage KPIs and risks first, maps current field/SCADA/ERP workflows, refines functional & NFR specs, and aligns trade-offs to Power Platform Well-Architected pillars. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Incorrect. Prototyping in Default Solution with over-privileged accounts violates governance and creates un-deployable artifacts.
- **B:** Correct. Solution envisioning establishes measurable business outcomes and risks first, inventories current processes/systems, refines functional & NFR specs, and aligns design trade-offs to Well-Architected pillars.
- **C:** Incorrect. Lifting and shifting broken legacy schemas without process optimization or fit/gap analysis perpetuates technical debt.
- **D:** Incorrect. Coding or buying licenses before discovery and NFR capture causes costly rework and architectural mismatches.

</details>

### Q053 (`E6Q066`) — Architect a solution [2.10] · *Single-Answer Multiple Choice*

Immutable IEEE equipment-class reference codes are read globally by all utility staff with zero BU partitioning. Creating `IEEE_Class` with `____` ownership avoids unnecessary row-security joins.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Choosing `User or Team` table ownership for BU/row/team security vs `Organization` ownership for global config tables at creation time
- **D.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Global, non-confidential reference tables fit **`Organization` ownership** (selected permanently at table creation). [Skill 2.10: Design complex data models (ownership immutability, Elastic/Activity tables, binary storage offloading) | Source: Design complex data models (ownership, Elastic/Activity tables, storage capacity) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/elastic-tables)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Correct. Table ownership (`User/Team` vs `Organization`) is immutable once created and determines whether BU, Team, and Hierarchy security apply.
- **D:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.

</details>

### Q054 (`E6Q077`) — Architect a solution [2.15] · *Single-Answer Multiple Choice*

During major ice storms, 300 mutual-aid linemen from neighboring utilities are added to an Entra security group for 10 days and removed once power is restored. Binding custom Security Roles to `____` automates instant grant and revocation.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Combining `Modernized Business Units` (matrix access), `Microsoft Entra ID Security Group Teams`, & `Access Team Templates`
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **Microsoft Entra ID Security Group Teams** enforce dynamic zero-touch Dataverse access that revokes immediately upon Entra group removal. [Skill 2.15: Design Business Units, Modernized BUs, Owner Teams, Access Team Templates, & Entra Group Teams | Source: Design Business Units, Modernized BUs, Owner/Access Teams, & Entra Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Correct. Modernized BUs enable cross-BU matrix roles, Entra Group Teams automate zero-touch RBAC, and Access Teams handle ad-hoc record collaboration cleanly.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.

</details>

### Q055 (`E6Q067`) — Architect a solution [2.11] · *Ordered Sequence (Multiple Choice)*

Whenever a `Critical_Tower_Defect` commits in Dataverse, GridVantage must synchronize work orders reliably to SAP PM (even during nightly SAP batch locks) without blocking crew saves. Which four-step integration sequence fits best?

- **A.** Call slow on-premises ERP SOAP endpoints inside a synchronous Pre-Operation Dataverse plug-in → Hold SQL transaction locks for 90 seconds → Ignore HTTP 429/503 errors → Lose failed payloads permanently
- **B.** Poll all 10 million Dataverse rows every 10 seconds without `modifiedon` or Change Tracking → Overrun 5-minute Service Protection limits → Overwrite newer ERP records blindly → Disable TLS
- **C.** Embed ERP admin client secrets inside browser JavaScript web resources → Call ERP directly from user browsers bypassing CORS & DLP → Log failed payloads to browser `console.log` → Skip auditing
- **D.** Register a Dataverse Service Endpoint (`Service Bus` / `Event Grid`) → Publish row events asynchronously on commit → Buffer & transform via Azure Functions / Logic Apps with DLQ → Upsert idempotently into ERP via Alternate Keys

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Publishing asynchronously from a Dataverse Service Endpoint to Azure Service Bus / Event Grid, transforming via Azure Functions / Logic Apps with DLQ, and upserting idempotently into SAP PM via Alternate Keys decouples crew saves from SAP maintenance locks. [Skill 2.11: Design collaboration (Teams, SharePoint ACL nuances, Exchange) and Dynamics 365 Dual-write integrations | Source: Design Teams, SharePoint, Exchange, and Dynamics 365 (Dual-write) integrations (https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dual-write/dual-write-overview)]

- **A:** Incorrect. Long network calls inside synchronous plug-ins exhaust Dataverse worker threads, lock SQL transactions, and lose messages when endpoints go offline.
- **B:** Incorrect. Full-table polling without Dataverse Change Tracking triggers `HTTP 429` throttling and causes lost-update race conditions.
- **C:** Incorrect. Exposing secrets in client-side JavaScript is a critical security vulnerability.
- **D:** Correct. Asynchronous Dataverse Service Endpoints -> Azure Service Bus/Event Grid -> Azure Functions/Logic Apps with Dead-Letter Queues and idempotent Alternate Key upserts decouple Dataverse from ERP latency and outages.

</details>

### Q056 (`E6Q002`) — Perform solution envisioning and requirement analysis [1.1] · *Single-Answer Multiple Choice*

Substation switching apps must sustain sub-second query delegation across 18 million meter-ticket rows and scale API ingestion elastically during winter ice-storm outages. This maps to the Well-Architected `____` pillar.

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Power Platform Well-Architected `Performance Efficiency` pillar (delegable queries, API throughput budgets, & elastic scaling)
- **C.** Power Platform Well-Architected `Security` pillar (Zero Trust Entra identity, least privilege, DLP, & encryption)
- **D.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The Power Platform Well-Architected `Performance Efficiency` pillar governs delegable queries, indexing, API throughput budgets, and elastic storm-surge scaling. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Correct. Performance Efficiency optimizes response latency and resource utilization via query delegation, indexing, batching, and Elastic/async patterns.
- **C:** Incorrect. The Security pillar protects confidentiality and integrity through Entra Conditional Access, least-privilege roles, DLP endpoint rules, and CMK/Lockbox.
- **D:** Incorrect. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.

</details>

### Q057 (`E6Q083`) — Architect a solution [2.17] · *Single-Answer Multiple Choice*

Proposed solution: Authenticate automated Azure DevOps deployment pipelines and SAP sync Functions using federated **Microsoft Entra App Registrations / Managed Identities (`Application Users`)** rather than shared human admin passwords. Should you approve this?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Using `OAuth 2.0 On-Behalf-Of (OBO)` to preserve caller identity/audit trails vs `Entra Service Principal (S2S)` / `Managed Identity` for background jobs
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes — passwordless Workload Identity Federation / Managed Identity `Application Users` eliminate secret rotation failures, MFA prompt breakages, and shared-credential audit gaps. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Correct. OBO propagates the signed-in user’s identity downstream for row-level authorization, whereas S2S/Managed Identity runs headless workloads.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q058 (`E6Q028`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

Documenting `Given insulator severity = Critical-A, When lineman submits inspection, Then emergency SAP work order dispatches within 60 seconds` defines testable `____`.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Refining prescriptive wishes into persona-based `User Stories` (`As a ... I need ... so that ...`) with testable Acceptance Criteria

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Given / When / Then` Acceptance Criteria make safety-critical dispatch rules verifiable across build and UAT. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Correct. Outcome-oriented User Stories decouple business intent from premature UI assumptions and anchor QA test cases.

</details>

### Q059 (`E6Q037`) — Perform solution envisioning and requirement analysis [1.15] · *Ordered Sequence (Multiple Choice)*

A utility conglomerate evaluates 205 field-inspection, asset-hierarchy, and carbon-trading requirements. Which four-step fit/gap evaluation sequence minimizes custom-code debt across Microsoft release waves?

- **A.** Accept every stakeholder wish into Phase 1 without feasibility scoring → Skip MVP boundaries → Hardcode workarounds in Production → Defer licensing impact checks until billing
- **B.** Validate each requirement against out-of-the-box Dataverse & Dynamics 365 capabilities → Evaluate declarative low-code configuration → Assess vetted AppSource ISV solutions → Specify targeted pro-code extensions only for remaining gaps
- **C.** Inject unsupported DOM-scraping JavaScript into Model-driven forms → Modify SQL indexes directly via TDS → Bypass security roles → Lock out Microsoft updates
- **D.** Build bespoke React SPAs and C# plug-ins for every requirement first → Replace standard Dynamics 365 tables with custom tables → Ignore AppSource → Check standard features last

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Checking native Dataverse/Dynamics 365 fit first, then declarative low-code configuration, then vetted AppSource ISVs, and finally targeted pro-code extensions protects TCO and wave-upgrade safety. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Unbounded scope acceptance without feasibility or licensing evaluation derails timelines and budgets.
- **B:** Correct. Fit/gap analysis prioritizes standard platform/Dynamics 365 features first, then declarative configuration, then supported AppSource ISVs, reserving custom code strictly for true differentiators.
- **C:** Incorrect. Unsupported DOM manipulation and direct SQL writes violate Microsoft supportability contracts and break on wave updates.
- **D:** Incorrect. Defaulting to custom code and duplicating restricted/standard Dynamics 365 tables inflates TCO and breaks product upgrades.

</details>

### Q060 (`E6Q058`) — Architect a solution [2.6] · *Single-Answer Multiple Choice*

Grid planners need long-horizon load-forecasting dashboards combining 1.5M Dataverse interconnection requests with 19 TB of smart-meter OneLake parquet tables and weather models under regional **Row-Level Security (`RLS`)**. Which design fits best?

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics
- **C.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **`Microsoft Fabric Link`** (`OneLake`) paired with **Power BI (`RLS`)** blends Dataverse and multi-terabyte smart-meter datasets without taxing transactional Dataverse SQL. [Skill 2.6: Design data visualization strategies across Dataverse charts, Power BI RLS, and Fabric/Synapse Link | Source: Design data visualization (Dataverse charts, Power BI RLS, Fabric/Synapse Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-synapse)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Correct. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.
- **C:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q061 (`E6Q089`) — Implement the solution [3.3] · *Single-Answer Multiple Choice*

When ingesting 400 homogeneous `Outage_Ping` rows in a single call, why should C# workers prefer `CreateMultipleRequest` over wrapping 400 individual `CreateRequest` items inside `ExecuteMultipleRequest`?

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Sizing 24-hour `Power Platform Request (PPR)` capacity and using `CreateMultiple` / `UpdateMultiple` / `$batch` (`ExecuteMultiple` `<= 1,000`)
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Microsoft’s **`CreateMultiple` / `UpdateMultiple`** bulk messages optimize single-table multi-row SQL/plug-in pipelines natively and consume significantly lower server execution time against the 20-minute Service Protection cap. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Correct. Bulk messages (`CreateMultiple`/`UpdateMultiple`) and `$batch` cut network round-trips dramatically while keeping daily PPR consumption within entitlements.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q062 (`E6Q022`) — Perform solution envisioning and requirement analysis [1.9] · *Ordered Sequence (Multiple Choice)*

A transmission company stores spatial conductor topology in Esri GIS, asset financial depreciation in SAP PM, and field inspection notes in legacy SQL. In what four-step sequence should you evaluate these data sources?

- **A.** Inventory candidate enterprise data sources & owners → Classify data sensitivity, residency, & compliance rules → Assess data quality, volume, & latency needs → Decide per entity whether to connect in place or replicate into Dataverse
- **B.** Duplicate 100% of ERP tables into Dataverse nightly → Ignore master-data ownership → Allow dual uncoordinated edits without conflict rules → Cleanse duplicates manually after go-live
- **C.** Email daily CSV exports between departments → Let business units invent conflicting customer IDs → Skip deduplication standards → Import dirty spreadsheets straight into Production
- **D.** Expose on-premises SQL Server ports directly to the public internet → Share one SQL `sa` login across Canvas apps → Skip data classification → Disable Dataverse auditing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Inventorying candidate sources & owners, classifying NERC-CIP sensitivity & residency, assessing quality/volume/latency, and choosing virtual in-place access vs Dataverse replication per entity protects authoritative boundaries. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Correct. Architects identify authoritative systems of record first, classify regulatory sensitivity/residency, evaluate quality/volume/latency, and then choose virtual in-place access vs Dataverse replication.
- **B:** Incorrect. Blindly duplicating authoritative ERP tables without master-data ownership or conflict governance causes severe data drift.
- **C:** Incorrect. Manual CSV emailing without canonical keys or data quality standards corrupts downstream analytics and automations.
- **D:** Incorrect. Exposing raw database ports and sharing `sa` logins violates zero-trust security and bypasses Dataverse governance.

</details>

### Q063 (`E6Q095`) — Implement the solution [3.6] · *Ordered Sequence (Multiple Choice)*

ApexGrid merges 3.8 million acquired utility rows and Managed Solution upgrades into Production over a Sunday 28-hour billing freeze. Which four-step cutover sequence prevents user collisions and validates readiness?

- **A.** Freeze changes & verify backup restore point → Enable Dataverse `Administration mode` (blocking regular users & async jobs) → Apply Managed Upgrades & run validated delta loads → Exit `Administration mode`, smoke-test, & monitor hypercare
- **B.** Ignore Dataverse Database/File storage overages blocking admin ops → Skip Solution Checker critical findings → Leave Dev URLs in Environment Variables → Disband support team at launch minute
- **C.** Delete existing Managed Solutions in Production (erasing live tables!) → Re-import from scratch → Manually re-type Connection References & Environment Variables → Disable backups
- **D.** Allow 5,000 users to edit records during live schema upgrade and migration → Import Unmanaged solutions into Production → Skip smoke tests → Turn on auditing two months later

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Verifying restore points, enabling `Administration mode` (blocking non-admins & async jobs), applying Managed Upgrades + validated delta loads, and exiting `Administration mode` after smoke tests ensures a clean utility cutover. [Skill 3.6: Escalate and resolve data migration bottlenecks (BypassCustomPluginExecution, delta loads, reconciliation) | Source: Escalate and remediate enterprise data migration bottlenecks and cutover issues (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/TVF-override-plugin-execution)]

- **A:** Correct. Controlled cutovers establish restore points, engage `Administration mode` to prevent user writes and background noise, apply Managed Upgrades + delta loads, validate smoke tests, and transition to monitored hypercare.
- **B:** Incorrect. Exceeded Dataverse storage entitlements block environment copy/restore/admin operations and sabotage cutover readiness.
- **C:** Incorrect. Deleting a Managed Solution erases its custom Dataverse tables and production data; always use Managed `Stage for upgrade` -> `Apply upgrade`.
- **D:** Incorrect. Concurrent user edits during cutover cause migration collisions, lock timeouts, and inconsistent business state.

</details>

### Q064 (`E6Q038`) — Perform solution envisioning and requirement analysis [1.15] · *Single-Answer Multiple Choice*

Presenting an executive governance scorecard classifying every grid-modernization requirement into `Out-of-the-Box`, `Configuration`, `AppSource ISV`, or `Custom Extension` with TCO and license impact produces a `____`.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Structured Fit/Gap matrix scoring requirements across `Out-of-the-Box`, `Configuration`, `AppSource ISV`, & `Custom Code`
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A formal Fit/Gap matrix documents transparent trade-offs across configuration, ISVs, licensing, and custom extensions. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Correct. Formal fit/gap scoring exposes customization TCO, licensing impacts, and upgrade maintenance trade-offs transparently.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q065 (`E6Q082`) — Architect a solution [2.17] · *Single-Answer Multiple Choice*

Sixty accredited third-party ISO-14064 carbon verifiers need temporary access inside EcoLedger’s **internal** Model-driven Verification Workbench app to sign off audit findings. Which external identity pattern fits best?

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Enforcing `DLP` + `Endpoint Filtering`, licensing external consumers via `Power Pages` (`Entra External ID`), & `Entra B2B` for internal-app guests
- **D.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Onboarding the 60 external verifiers via **Microsoft Entra B2B** guest invitations mapped to an Entra Security Group Team and least-privilege verifier Security Role fits internal Model-driven collaboration cleanly. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Correct. Power Pages scales cost-effectively with `Table Permissions` for external portals, whereas Entra B2B suits external partners using internal apps.
- **D:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.

</details>

### Q066 (`E6Q014`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

A cross-border pipeline operator runs control rooms in Canada, Norway, and the United Kingdom where national energy-security laws forbid exporting critical-infrastructure asset coordinates outside domestic cloud Geos. Which risk factor must be addressed first?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Assessing sovereign data-residency (`Multi-Geo`), PII/PHI/ITAR compliance, `CMK`, & cross-border connector risks upfront
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Sovereign national data-residency statutes require `Multi-Geo` regional Dataverse environments, `CMK`, `Customer Lockbox`, and strict cross-border DLP connector isolation upfront. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Correct. Identifying residency and regulatory encryption constraints during envisioning prevents illegal cross-region tenant/environment placement.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

## Case Study Vignette — EcoLedger Carbon Exchange

> EcoLedger Carbon Exchange tracks immutable carbon-credit retirement certificates across multinational corporate buyers, external verifiers, and internal traders. Auditors require tamper-evident audit retention, separation of duties via Microsoft Entra Privileged Identity Management (PIM), and zero unapproved SaaS exfiltration across 14 environments using CoE Starter Kit + Managed Environments.

### Q067 (`E6Q047`) — Architect a solution [2.1] · *Multi-Select (Select 2)*

Case study — EcoLedger Carbon Exchange: EcoLedger operates 14 Power Platform environments across `Dev`, `QA`, `UAT`, and `Prod` tiers and requires centralized maker inventory telemetry, Sharing Limits, Weekly Usage Digests, and modular Managed Solution layers under one Publisher prefix. Which two architectural practices deliver this? Select two.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix
- **D.** Dedicated `Dev -> Test -> UAT -> Prod` environments (plus sovereign `Multi-Geo` instances) governed by `Managed Environments` & `CoE Starter Kit`
- **E.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, D` (`CSV: 3,4`)

Correct answers: C and D (are correct). **Managed Environments + CoE Starter Kit** across multi-tier environments (`env_multi_tier_coe`) paired with **segmented Managed Solutions** under a unified Publisher prefix (`sol_segmented_alm`) enforce automated governance across all 14 environments. [Skill 2.1: Design segmented solution topology, custom Publisher strategy, and Managed Environments | Source: Design solution topology, publisher segmentation, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/alm/segmented-solutions-alm)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.
- **D:** Correct. Multi-tier ALM environments isolate production workloads, Multi-Geo satisfies regional residency, and CoE + Managed Environments automate governance.
- **E:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q068 (`E6Q078`) — Architect a solution [2.16] · *Multi-Select (Select 3)*

Case study — EcoLedger Carbon Exchange: Auditors require EcoLedger to enforce: (1) separation of duties with zero standing Production `System Administrator` accounts via time-bound MFA elevation + tamper-evident audit retention, (2) restricted `Bilateral_Strike_Price` column masking, and (3) IP firewall + Conditional Access session controls. Which three controls deliver this? Select three.

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **E.** Governing `Database`, `File`, & `Log` storage pools via `Dataverse Long Term Retention`, `Fabric/Synapse Link` archival, & attachment offloading
- **F.** Enforcing `Microsoft Entra Conditional Access` (MFA & compliant device) plus `Power Platform IP Firewall` & `Cookie IP binding`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E, F` (`CSV: 3,5,6`)

Correct answers: C, E, and F (are correct). **Microsoft Entra PIM** just-in-time admin elevation + **`Column Security Profiles`** + `CMK`/`Lockbox` (`sec_col_hier_pim`), **Entra Conditional Access + Power Platform IP Firewall** (`sec_cond_access_ip`), and multi-year Dataverse **Audit + Long Term Retention** (`cap_storage_tiering`) satisfy exchange audits. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **E:** Correct. Keeping relational `Database` capacity lean prevents tenant admin lockouts (`Copy`/`Restore` blocks) and controls storage overage costs.
- **F:** Correct. Combining Entra Conditional Access with Managed Environment IP Firewall and session cookie binding blocks token replay from untrusted networks.

</details>

### Q069 (`E6Q081`) — Architect a solution [2.17] · *Multi-Select (Select 2)*

Case study — EcoLedger Carbon Exchange: EcoLedger must guarantee **zero unapproved SaaS exfiltration across all 14 environments** (blocking non-business connectors and filtering HTTP/SQL endpoints strictly to approved FQDNs) while allowing 8,500 external corporate buyers to retire carbon certificates online via `Account`-scoped permissions. Which two designs apply? Select two.

- **A.** Enforcing `DLP` + `Endpoint Filtering`, licensing external consumers via `Power Pages` (`Entra External ID`), & `Entra B2B` for internal-app guests
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **E.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Tenant-level **DLP policies (`Default` = `Blocked`) + Connector Endpoint Filtering** (`sec_dlp_ext_access`) prevent SaaS exfiltration across all 14 environments, while **Microsoft Power Pages** with `Entra External ID` + `Account`-scoped `Table Permissions` (`comp_power_pages` & `sec_dlp_ext_access`) serves the 8,500 corporate buyers securely. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Correct. Power Pages scales cost-effectively with `Table Permissions` for external portals, whereas Entra B2B suits external partners using internal apps.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **D:** Correct. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **E:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.

</details>

### Q070 (`E6Q080`) — Architect a solution [2.16] · *Single-Answer Multiple Choice*

Chief Grid Engineers need read visibility across `VP Operations -> Regional Superintendent -> Substation Foreman -> Lineman` positions 4 levels deep. Enabling `____` delivers this natively.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access
- **C.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Dataverse **Position / Manager Hierarchy Security** models multi-tier operational reporting trees cleanly without custom plug-ins. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.
- **C:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q071 (`E6Q075`) — Architect a solution [2.14] · *Single-Answer Multiple Choice*

For a legacy substation historian SQL database sitting inside an on-premises regional plant LAN without Azure VNet connectivity, deploying an active-active `____` cluster provides outbound-only TLS connectivity.

- **A.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A multi-node **On-Premises Data Gateway** cluster establishes outbound HTTPS/TLS relay connections without opening inbound plant firewall ports. [Skill 2.14: Assess VNet subnet delegation, Azure ExpressRoute nuances, Data Gateways, and IP firewall networking | Source: Assess VNet integration, Azure ExpressRoute, gateways, and IP firewall networking (https://learn.microsoft.com/en-us/power-platform/admin/vnet-support-overview)]

- **A:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Correct. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.

</details>

### Q072 (`E6Q055`) — Architect a solution [2.5] · *Ordered Sequence (Multiple Choice)*

During M&A utility consolidation, you must migrate 3.8 million `Premises`, `Meters`, `Accounts`, and circular `Primary_Meter <-> Premise` lookups into Dataverse without firing outage-SMS flows or breaking tariff-reference GUIDs. Which four-step migration sequence applies?

- **A.** Let each environment generate random GUIDs for reference/configuration tables → Hardcode Dev GUIDs inside cloud flows → Import raw unvalidated CSVs → Skip reconciliation
- **B.** Load child line-items before parent Account rows exist → Leave all welcome-email cloud flows enabled → Run single-row serial inserts with no batching → Fix orphaned lookups manually in Prod
- **C.** Execute `INSERT INTO account` over Dataverse TDS port 5558 → Remove platform SQL foreign keys → Copy `.mdf` database files from Azure SQL → Reboot the tenant
- **D.** Cleanse & stage data with Alternate Keys / CMT GUIDs → Suppress non-essential flows & custom plug-ins → Load parent tables first (deferring circular lookups) → Bind deferred lookups, reconcile counts, & re-enable automations

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Staging cleansed data with Alternate Keys & CMT fixed GUIDs, suppressing flows & custom plug-ins, loading parents first (deferring circular meter lookups), and binding deferred lookups before reconciling counts ensures clean cutover. [Skill 2.5: Design enterprise data migration strategies, load sequencing, Alternate Keys, and CMT tooling | Source: Design enterprise data migration strategies, load order, and tooling (https://learn.microsoft.com/en-us/power-platform/admin/create-schema-export-data)]

- **A:** Incorrect. Mismatched reference-data GUIDs across Dev, UAT, and Prod break business rules, views, and workflow conditions.
- **B:** Incorrect. Loading child rows first fails referential integrity, and leaving notification flows active spams thousands of customers.
- **C:** Incorrect. Dataverse’s TDS endpoint (`5558`) is strictly read-only; all writes must use Dataverse Web API/SDK, Dataflows, ADF, or Configuration Migration Tool.
- **D:** Correct. Enterprise migrations stage cleansed data, suppress noisy automations (`BypassCustomPluginExecution`), load parents before children while resolving circular lookups in a second pass, and reconcile counts before re-enabling flows.

</details>

### Q073 (`E6Q033`) — Perform solution envisioning and requirement analysis [1.13] · *Single-Answer Multiple Choice*

Bilingual French/English hydro control rooms and public outage portals must satisfy `WCAG 2.1 AA` contrast, keyboard navigation, `AccessibleLabel`, and `.resx` localization under `____`.

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Designing for `WCAG 2.1 AA` accessibility (`AccessibleLabel`, `TabIndex`, contrast) and `.resx` multi-language localization

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Designing `WCAG 2.1 AA` accessibility and `.resx` localization into initial components ensures regulatory compliance across control rooms and public portals. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Correct. Building accessibility and localization into initial UX components avoids expensive retrofits before public or enterprise launch.

</details>

### Q074 (`E6Q076`) — Architect a solution [2.15] · *Ordered Sequence (Multiple Choice)*

A transmission operator requires strict operating-company Business Unit isolation, matrix cross-BU visibility for NERC compliance auditors, dynamic Entra security-group role mapping, and lightweight storm-restoration task teams. Which four-step security sequence fits best?

- **A.** Store confidential M&A contracts in default SharePoint Document Management folders → Assume SharePoint automatically inherits Dataverse row-level Security Roles & Access Teams → Grant site-wide Read to all employees → Go live
- **B.** Place all users in one root BU with Organization-level Read/Write/Delete → Clone System Administrator for power users → Hide restricted fields using client-only JavaScript → Share individual records manually
- **C.** Model Business Units around isolation boundaries (with Modernized BUs for matrix access) → Author custom least-privilege Security Roles → Bind roles to Entra Security Group Teams → Layer Column Security & Access Team Templates
- **D.** Create 400 micro Business Units mirroring every HR cost center → Move users between BUs daily (wiping roles prior to modern settings) → Duplicate 400 identical copies of every Security Role → Audit nothing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Modeling BUs around operating-company boundaries (with Modernized BUs for matrix auditors), copying least-privilege Security Roles, binding roles to Entra Security Group Teams, and layering Column Security + Access Team Templates scales cleanly. [Skill 2.15: Design Business Units, Modernized BUs, Owner Teams, Access Team Templates, & Entra Group Teams | Source: Design Business Units, Modernized BUs, Owner/Access Teams, & Entra Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect. Out-of-the-box SharePoint Document Management does NOT synchronize Dataverse row-level security ACLs to SharePoint folders automatically.
- **B:** Incorrect. Client-side JavaScript never secures data at the API layer, and manual per-record sharing bloats the PrincipalObjectAccess (`POA`) table.
- **C:** Correct. Scalable Dataverse security aligns BUs to isolation boundaries, layers custom least-privilege roles onto Entra Security Group Teams for zero-touch provisioning, and handles exceptions via Access Teams and Column Security.
- **D:** Incorrect. Over-fragmenting Business Units for reporting rather than true security boundaries creates massive administrative overhead.

</details>

### Q075 (`E6Q009`) — Perform solution envisioning and requirement analysis [1.4] · *Single-Answer Multiple Choice*

An energy utility acquiring a neighboring gas distributor must merge 3.8 million premise/meter histories containing dirty duplicate tax IDs, conflicting tariff option sets, and a 28-hour weekend billing freeze. What governs your migration effort estimate?

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Estimating migration/integration effort from source data cleanliness, transformations, API throughput windows, & cutover downtime

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). TIN deduplication, tariff code crosswalks, parent-child premise/meter load sequencing, 5-minute API limits, and the 28-hour billing freeze drive realistic migration effort. [Skill 1.4: Identify and estimate data migration and integration efforts, complexity drivers, and alternatives | Source: Estimate migration and integration efforts and alternatives (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Correct. Realistic effort sizing accounts for legacy deduplication, schema mapping, historical volume, 5-minute API limits, and delta cutover rehearsals.

</details>

### Q076 (`E6Q018`) — Perform solution envisioning and requirement analysis [1.7] · *Single-Answer Multiple Choice*

Validating 90-day post-launch `SAIDI`/`CAIDI` dispatch latency drops and carbon-certificate error-rate reductions (`4.1% -> 0.2%`) against pre-launch baselines confirms `____`.

- **A.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Defining baseline-backed `SMART` success KPIs (cycle-time reduction, error-rate drop, SLA adherence, & active adoption %)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Post-launch telemetry measured against documented pre-project baselines validates achievement of agreed `SMART` KPIs. [Skill 1.7: Review and validate measurable key success criteria, KPIs, and adoption targets | Source: Review measurable key success criteria, KPIs, and adoption targets (https://learn.microsoft.com/en-us/power-platform/guidance/adoption/measure-business-value)]

- **A:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Correct. Quantifiable KPIs anchored to current-state baselines let stakeholders verify objective ROI after go-live.

</details>

### Q077 (`E6Q074`) — Architect a solution [2.14] · *Single-Answer Multiple Choice*

Dataverse C# plug-ins and custom connectors must reach an internal SAP S/4HANA Gateway hosted inside a private Azure VNet (`10.90.0.0/16`) with public IPs disabled and zero self-managed gateway VMs. Configuring `____` enables private outbound VNet injection.

- **A.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **B.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **C.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). **Virtual Network (`VNet`) support for Power Platform** (`enterprisePolicies` subnet delegation) injects Dataverse plug-in and connector outbound traffic directly into the private Azure VNet. [Skill 2.14: Assess VNet subnet delegation, Azure ExpressRoute nuances, Data Gateways, and IP firewall networking | Source: Assess VNet integration, Azure ExpressRoute, gateways, and IP firewall networking (https://learn.microsoft.com/en-us/power-platform/admin/vnet-support-overview)]

- **A:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **B:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **C:** Correct. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.
- **D:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.

</details>

### Q078 (`E6Q100`) — Implement the solution [3.8] · *Single-Answer Multiple Choice*

Establishing formal executive Go/No-Go sign-off criteria, taking a manual Production Dataverse backup immediately prior to upgrade, rehearsing Point-in-Time Restore timing, and rolling out Operating Company 1 as a pilot wave defines `____`.

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Establishing signed-off `Go / No-Go` readiness gates, manual pre-cutover `Backup` restore points, rollback runbooks, & phased wave rollouts
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Signed Go/No-Go gates, manual pre-cutover restore points, tested rollback runbooks, and phased pilot waves protect critical utility operations during go-live. [Skill 3.8: Identify go-live readiness gates, execute Administration mode cutovers, and manage hypercare telemetry | Source: Assess go-live readiness factors, Administration mode, and hypercare remediation (https://learn.microsoft.com/en-us/power-platform/admin/admin-mode)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Clear Go/No-Go criteria, pre-upgrade backups, and phased pilot waves minimize blast radius during enterprise go-live.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q079 (`E6Q079`) — Architect a solution [2.16] · *Single-Answer Multiple Choice*

Preventing manual per-record sharing across 18 million `Meter_Ticket` rows so `PrincipalObjectAccess` (`POA`) never degrades SQL view joins exemplifies `____`.

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **D.** Preventing `PrincipalObjectAccess (POA)` table bloat by replacing manual per-record sharing and `Parental` cascades with `Access Team Templates`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enforcing **`POA` hygiene** via **Access Team Templates** and **Entra Group Teams** instead of manual shares or `Parental` cascades protects SQL performance at 18M-row scale. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **D:** Correct. Millions of `POA` rows from manual sharing and `Cascade All` relationships degrade SQL query performance across Dataverse views.

</details>

### Q080 (`E6Q052`) — Architect a solution [2.3] · *Single-Answer Multiple Choice*

Which visual artifact communicates the exact parent-child cardinalities, Alternate Keys, and `User/Team` vs `Organization` ownership across `Substation`, `Feeder`, `Tower`, and `Work_Order` tables?

- **A.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Reusing `Component Libraries`, `PCF`, `Child Flows`, & `Custom Connectors`, documented via `ERD`, `Sequence`, & `Context` diagrams

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). An **Entity Relationship Diagram (`ERD`)** documents Dataverse schema cardinalities, keys, cascading rules, and ownership types unambiguously. [Skill 2.3: Maximize component reuse (PCF, Component Libraries, Child Flows) and communicate designs visually | Source: Maximize component reuse (PCF, Component Libraries, Child Flows) & visual diagrams (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)]

- **A:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Correct. Shared component catalogs eliminate duplicate maintenance, while visual architecture diagrams align technical and business stakeholders.

</details>

### Q081 (`E6Q059`) — Architect a solution [2.7] · *Multi-Select (Select 2)*

A carbon-trading and grid platform must: (1) reject saving a `Credit_Retirement` row synchronously if `Available_Serial_Balance < Retirement_Qty`, and (2) run `CIM IEC 61968` XML enterprise grid-exchange workflows inside VNet-isolated Azure single-tenant compute. Which two automation tools fit best? Select two.

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Synchronous Dataverse plug-ins (`<= 2m`) strictly for atomic transaction validation/rollback; Cloud Flows / Logic Apps for async orchestration
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **E.** Azure Logic Apps (Standard) for enterprise B2B EDI (`X12`/`AS2`/`EDIFACT`), VNet-isolated single-tenant workflows, & Azure Bicep ALM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). A fast synchronous Dataverse plug-in enforces atomic balance validation (`auto_sync_vs_async`), while **Azure Logic Apps (Standard)** executes VNet-isolated `IEC 61968` XML transformations under Azure Bicep ALM (`auto_logic_apps`). [Skill 2.7: Design automation strategies (sync vs async, BPF, Logic Apps) and multi-environment ALM topology | Source: Design automation & multi-environment strategies (CoE Starter Kit & ALM) (https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Keeping synchronous transaction pipelines fast and offloading external orchestrations asynchronously protects Dataverse SQL responsiveness.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **E:** Correct. Logic Apps Standard complements Power Automate when Azure RBAC, private VNet compute, or B2B Enterprise Integration Pack codecs are required.

</details>

### Q082 (`E6Q094`) — Implement the solution [3.5] · *Single-Answer Multiple Choice*

To diagnose exact SQL/plug-in duration percentiles (`p95`, `p99`) and exception stack traces across Boreal Hydro’s 18-million-row Production environment via KQL, you query telemetry streamed to `____`.

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Running scale tests in UAT while streaming Dataverse and Canvas telemetry to `Azure Application Insights` (`dependencies` / `exceptions` KQL)
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **Azure Application Insights** captures Dataverse `requests`, `dependencies`, `exceptions`, and plug-in `ITracingService` traces for real-time KQL performance diagnostics. [Skill 3.5: Identify and resolve Canvas, Model-driven, Quick Find index, and synchronous plug-in performance issues | Source: Identify and resolve Canvas, Model-driven, Dataverse, & plug-in performance issues (https://learn.microsoft.com/en-us/power-platform/well-architected/performance-efficiency/overview)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Correct. Application Insights integration captures page-load latency, plug-in execution durations, and outbound dependency failures under realistic concurrency.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q083 (`E6Q045`) — Perform solution envisioning and requirement analysis [1.18] · *Multi-Select (Select 2)*

During UAT for a NERC-CIP mandatory winter readiness deadline, commercial marketing asks to bundle an EV home-charger marketplace into Phase 1. Which two governance actions should the Solution Architect take? Select two.

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Scoping a high-value `MVP` Phase 1 release using MoSCoW prioritization and formal change-request governance
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **E.** Establishing a fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). Protecting the NERC-CIP `MVP` Phase 1 boundary via MoSCoW prioritization (`scope_mvp_phased`) and routing commercial EV requests to Phase 2 via Change Control / ARB governance (`disc_raci_governance`) safeguards winter grid compliance. [Skill 1.18: Determine MVP vs phased solution scope boundaries and govern scope changes | Source: Determine MVP vs phased solution scope and manage scope boundaries (https://learn.microsoft.com/en-us/training/paths/become-solution-architect/)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Correct. Phased MVP delivery de-risks go-live, delivers early business value, and prevents uncontrolled scope creep.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **E:** Correct. Clear architectural ownership, ARB design gates, and CoE guardrails align business, citizen makers, pro-devs, and InfoSec.

</details>

### Q084 (`E6Q060`) — Architect a solution [2.7] · *Single-Answer Multiple Choice*

Guiding interconnection engineers across `Application -> Screening -> System Impact Study -> Facilities Upgrade -> Permission to Operate` spanning two Dataverse tables uses `____`.

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **C.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A multi-table **Business Process Flow (`BPF`)** enforces consistent engineering stage gates, required fields, and conditional branching. [Skill 2.7: Design automation strategies (sync vs async, BPF, Logic Apps) and multi-environment ALM topology | Source: Design automation & multi-environment strategies (CoE Starter Kit & ALM) (https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Correct. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **C:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q085 (`E6Q092`) — Implement the solution [3.4] · *Single-Answer Multiple Choice*

Adding an OData **`Trigger Condition`** such as `@not(equals(triggerOutputs()?['body/_modifiedby_value'], '<sap-app-user-guid>'))` alongside **`Select columns`** prevents a Power Automate flow from re-triggering on its own service principal’s writes. This eliminates `____`.

- **A.** Resolving automation/integration conflicts via `Select columns` (`filteringattributes`), `Trigger Conditions`, plug-in `Depth` checks, & `ETag` (`If-Match`) optimistic concurrency
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Service-principal actor exclusions combined with `Select columns` break bi-directional Dataverse-to-ERP infinite ping-pong loops cleanly. [Skill 3.4: Assess storage/resource impact and resolve automation loops, race conditions, & integration conflicts | Source: Assess storage/resource impact and resolve automation & integration conflicts (https://learn.microsoft.com/en-us/power-platform/admin/capacity-storage)]

- **A:** Correct. Column filters, actor exclusions, and `If-Match` row-version headers eliminate infinite ping-pong loops and silent lost-update race conditions.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q086 (`E6Q090`) — Implement the solution [3.3] · *Single-Answer Multiple Choice*

Monitoring response headers `x-ms-ratelimit-time-remaining-xrm-requests` and `x-ms-ratelimit-burst-remaining-xrm-requests` lets high-throughput S2S integrations self-pace proactively before tripping `____`.

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Conforming to `Dataverse Service Protection` limits (`6,000` req / `20m` compute per `5-min` window), pooling `S2S Application Users`, & honoring `Retry-After`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Proactively reading Dataverse rate-limit headers prevents tripping `HTTP 429` **Service Protection** (`6,000` req / `20m` compute per 5-minute sliding window). [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Correct. Service Protection enforces per-user/per-web-server 5-minute sliding caps (`HTTP 429`); pooling S2S Application Users and respecting `Retry-After` maximizes throughput.

</details>

### Q087 (`E6Q016`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

After three uncoordinated Production hotfixes broke carbon-credit settlement views, leadership wants automated CI/CD gates, telemetry, and safe deployment standards under the Well-Architected `____` pillar.

- **A.** Power Platform Well-Architected `Operational Excellence` pillar (automated ALM pipelines, Application Insights, & CoE)
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Operational Excellence` enforces source-controlled pipelines, Solution Checker gates, Managed Upgrades, and Application Insights telemetry. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Correct. Operational Excellence standardizes CI/CD solution pipelines, automated Solution Checker gates, telemetry, and Managed Environment governance.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q088 (`E6Q042`) — Perform solution envisioning and requirement analysis [1.16] · *Single-Answer Multiple Choice*

Why can GridVantage **not** license 1,500 field linemen purely with standalone Power Apps per-app seats to create and complete standard `msdyn_workorder` records?

- **A.** Validating Dynamics 365 restricted-table licensing (`Case / incident`, `Work Order`, `Entitlement`) during fit/gap analysis
- **B.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Work Order` (`msdyn_workorder`) is a Dynamics 365 **restricted table** requiring qualifying Dynamics 365 Field Service licenses for CRUD operations. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Correct. Restricted Dynamics 365 tables require appropriate Dynamics 365 licenses for CRUD operations rather than standalone Power Apps licenses.
- **B:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q089 (`E6Q030`) — Perform solution envisioning and requirement analysis [1.12] · *Single-Answer Multiple Choice*

Which requirement belongs in the **Functional Requirements** specification for a carbon-credit retirement registry?

- **A.** Capturing Non-Functional Requirements (`RPO`/`RTO`, peak concurrency, `p95` latency, API volume, `WCAG 2.1 AA`, & retention)
- **B.** Capturing Functional Requirements (persona workflows, state rules, approvals, offline CRUD scope, & statutory reports)
- **C.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources
- **D.** Conforming to `Dataverse Service Protection` limits (`6,000` req / `20m` compute per `5-min` window), pooling `S2S Application Users`, & honoring `Retry-After`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Serial-block retirement state rules, double-counting prevention checks, verifier sign-off workflows, and public retirement-certificate PDF generation define functional system behavior (`req_functional_spec`). [Skill 1.12: Identify functional requirements across personas, business rules, approvals, and offline access | Source: Identify functional requirements across personas, offline, and workflows (https://learn.microsoft.com/en-us/power-apps/mobile/setup-mobile-offline)]

- **A:** Incorrect. Non-functional requirements govern architectural sizing, BCDR, licensing capacity, offline design, and security controls.
- **B:** Correct. Functional requirements specify what business behaviors and data transformations the solution must perform for each role.
- **C:** Incorrect. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.
- **D:** Incorrect. Service Protection enforces per-user/per-web-server 5-minute sliding caps (`HTTP 429`); pooling S2S Application Users and respecting `Retry-After` maximizes throughput.

</details>

## Case Study Vignette — ApexGrid M&A Integration

> Following an acquisition, ApexGrid M&A Integration must merge an acquired utility’s standalone Dataverse CRM (containing dirty duplicate customer TINs and conflicting option-set integer codes) into ApexGrid’s global Power Platform tenant while keeping legacy SCADA green-screen apps running via Hosted RPA + Work Queues.

### Q090 (`E6Q025`) — Perform solution envisioning and requirement analysis [1.10] · *Single-Answer Multiple Choice*

Case study — ApexGrid M&A Integration: The acquired utility’s CRM contains 17% duplicate corporate customer TINs (`94-1122334` vs `941122334`) and conflicting integer option-set codes (`Voltage_Class = 1` means `13.8 kV` in Source A but `230 kV` in ApexGrid). What must you establish before migration build?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Defining pre-cutover data quality standards (deduplication keys, mandatory completeness, referential integrity, & domain mappings)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Defining rigorous pre-migration **data quality and crosswalk rules** (canonical TIN normalization, deduplication survivorship, and explicit `Voltage_Class` integer-value translation tables) prevents catastrophic high-voltage misclassifications. [Skill 1.10: Define use cases and data quality standards for existing data prior to migration or integration | Source: Define use cases and data quality standards for existing data (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Correct. Enforcing cleansing and deduplication gates before migration prevents garbage-in/garbage-out failures in Dataverse.

</details>

### Q091 (`E6Q056`) — Architect a solution [2.5] · *Single-Answer Multiple Choice*

Case study — ApexGrid M&A Integration: ApexGrid needs `ADF` pipelines to upsert acquired `Customer` and `Meter` records idempotently using external `Legacy_Utility_TIN` keys without GUID pre-lookups, while keeping `Tariff_Rate` reference-row GUIDs identical across Dev, UAT, and Prod. Which migration design fits best?

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Staging cleansed records via `ADF` / `SSIS` using Dataverse `Alternate Keys` (`Upsert`) and `Configuration Migration Tool` for fixed-GUID config rows
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Staging transformed/deduplicated rows in `ADF` using **Dataverse Alternate Keys** (`Upsert`) paired with the **Configuration Migration Tool (`CMT`)** for fixed-GUID `Tariff_Rate` config tables solves both requirements cleanly. [Skill 2.5: Design enterprise data migration strategies, load sequencing, Alternate Keys, and CMT tooling | Source: Design enterprise data migration strategies, load order, and tooling (https://learn.microsoft.com/en-us/power-platform/admin/create-schema-export-data)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Correct. Alternate Keys eliminate GUID pre-lookup round-trips on upserts, while CMT preserves exact reference-record GUIDs across Dev/UAT/Prod.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q092 (`E6Q073`) — Architect a solution [2.13] · *Single-Answer Multiple Choice*

Case study — ApexGrid M&A Integration: During transition, the acquired utility’s legacy SCADA outage-logging Windows thick client has zero APIs and must process 4,000 queued tickets daily with automatic retries and zero physical bot-PC maintenance, alongside `28-day` Dataverse Production backup coverage. What should you design?

- **A.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **B.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Designing BCDR around Dataverse point-in-time backups (`28-day` Prod retention, cross-Geo failover limits) and `Hosted RPA` + `Work Queues` for legacy UI

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Pairing Dataverse geo-redundant backups (`28-day` Prod retention) with **Power Automate Hosted RPA** + **Dataverse Work Queues** automates legacy SCADA UI queues resiliently without managing physical desktops. [Skill 2.13: Design authentication (OBO vs S2S, Managed Identity), BCDR (RPO/RTO, geo-backups), and RPA | Source: Design authentication (OBO vs S2S, Managed Identity), BCDR, and RPA architectures (https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments)]

- **A:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **B:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Correct. Architects align RPO/RTO to Microsoft’s managed geo-replication SLAs and isolate UI-only legacy integrations behind resilient RPA Work Queues.

</details>

### Q093 (`E6Q010`) — Perform solution envisioning and requirement analysis [1.4] · *Single-Answer Multiple Choice*

Smart-grid AMI meters generate 45 billion 15-minute kWh interval readings per year (`19 TB`). Rather than migrating raw interval readings into Dataverse Database storage, how should you surface interval analytics alongside Dataverse outage cases?

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **D.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Storing 19 TB AMI interval streams in **Microsoft Fabric OneLake / Eventhouse** and joining them with Dataverse cases via `Fabric Link` + Power BI avoids prohibitive Dataverse Database storage costs. [Skill 1.4: Identify and estimate data migration and integration efforts, complexity drivers, and alternatives | Source: Estimate migration and integration efforts and alternatives (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **D:** Correct. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.

</details>

### Q094 (`E6Q086`) — Implement the solution [3.2] · *Multi-Select (Select 2)*

A pre-go-live NERC-CIP security audit discovers makers hid `Critical_Substation_AccessCode` using a client `Form` Business Rule and left `Organization`-level `Write` privileges on `Switching_Plan` assigned to apprentice trainees. Which two fixes are mandatory? Select two.

- **A.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Auditing server-side `Security Roles`, `Column Security`, & `Power Pages Table Permissions` rather than trusting client-side UI rules
- **E.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Protecting `Critical_Substation_AccessCode` with a server-side **`Column Security Profile`** (`sec_col_hier_pim`) and tightening trainee **Security Roles** during server-side boundary audit (`val_sec_boundary_audit`) secure Web API, OData, and UI access. [Skill 3.2: Review security across Business Rules, Security Roles, Entra Conditional Access, & security boundaries | Source: Review end-to-end security across Business Rules, Roles, Entra ID, & boundaries (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Correct. Client JavaScript and `Form`-scoped Business Rules never block Web API/OData access; security boundaries must be enforced server-side in Dataverse.
- **E:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q095 (`E6Q068`) — Architect a solution [2.11] · *Single-Answer Multiple Choice*

Critical substation one-line schematics attached to Dataverse `Switching_Plan` rows must strictly enforce Dataverse NERC-CIP row-level Security Roles rather than open SharePoint site folder permissions. How should you store those schematics?

- **A.** Mitigating SharePoint Document Management’s lack of automatic Dataverse ACL sync via Dataverse `File` columns, Azure Blob SAS, or custom ACL sync
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Storing NERC-CIP schematics in native **Dataverse `File` columns** (or custom SAS-gated Azure Blob containers) guarantees server-side Dataverse row/column ACL enforcement. [Skill 2.11: Design collaboration (Teams, SharePoint ACL nuances, Exchange) and Dynamics 365 Dual-write integrations | Source: Design Teams, SharePoint, Exchange, and Dynamics 365 (Dual-write) integrations (https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dual-write/dual-write-overview)]

- **A:** Correct. Default SharePoint integration never copies Dataverse row permissions to SharePoint folders; confidential files require `File` columns or explicit ACL sync.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.

</details>

### Q096 (`E6Q072`) — Architect a solution [2.13] · *Single-Answer Multiple Choice*

When a switching engineer triggers a real-time NERC-CIP clearance check via a custom connector to an internal OT Authorization API, audit logs must record the **engineer’s individual Entra UPN**, whereas nightly weather-feed sync runs headlessly. How should authentication be configured?

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Using `OAuth 2.0 On-Behalf-Of (OBO)` to preserve caller identity/audit trails vs `Entra Service Principal (S2S)` / `Managed Identity` for background jobs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Use **`OAuth 2.0 On-Behalf-Of (OBO)`** delegated authentication for the interactive engineer clearance check and **`Entra Service Principal (S2S)` / `Managed Identity`** for the headless weather sync. [Skill 2.13: Design authentication (OBO vs S2S, Managed Identity), BCDR (RPO/RTO, geo-backups), and RPA | Source: Design authentication (OBO vs S2S, Managed Identity), BCDR, and RPA architectures (https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Correct. OBO propagates the signed-in user’s identity downstream for row-level authorization, whereas S2S/Managed Identity runs headless workloads.

</details>

### Q097 (`E6Q005`) — Perform solution envisioning and requirement analysis [1.2] · *Single-Answer Multiple Choice*

Hydroelectric dam technicians inspecting underground turbine penstocks 120 meters below rock with zero wireless signal need offline crack-measurement forms and photo logging via a `____`.

- **A.** Canvas Power App with a `Mobile Offline` profile and device-native camera/barcode UX tailored to frontline tasks
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **D.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A Canvas Power App configured with a `Mobile Offline` profile synchronizes Dataverse tables locally on rugged tablets for deep-underground inspections. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Correct. Canvas apps give pixel-level task UX and offline-first Dataverse synchronization for field workers operating without connectivity.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **D:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.

</details>

### Q098 (`E6Q040`) — Perform solution envisioning and requirement analysis [1.16] · *Multi-Select (Select 2)*

A gas-distribution utility needs emergency leak `Work Orders`, technician hazard certifications, truck tool inventory, automated territory dispatch (`RSO`), and a certified Esri ArcGIS linear-asset map add-on. Which two selections fit best? Select two.

- **A.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **B.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Dynamics 365 first-party app (`Sales`, `Customer Service`, or `Field Service`) leveraging native schemas, SLAs, & RSO scheduling
- **E.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Adopting **Dynamics 365 Field Service** (`Work Orders`, skills/certifications, inventory, `RSO`) paired with a vetted **AppSource Esri GIS ISV** avoids rebuilding complex utility dispatch from scratch. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **B:** Correct. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Correct. Adopting Dynamics 365 first-party apps avoids reinventing complex case routing, omnichannel queues, or Resource Scheduling Optimization.
- **E:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.

</details>

### Q099 (`E6Q070`) — Architect a solution [2.12] · *Single-Answer Multiple Choice*

External independent carbon-verification registries push signed webhook callbacks that must traverse centralized mutual-TLS validation, IP allowlists, and queue buffering before touching Dataverse. Which edge architecture fits best?

- **A.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Fronting webhook ingestion with **Azure API Management (`APIM`)** writing into **Azure Service Bus** queues decouples and authenticates external verifier callbacks safely. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q100 (`E6Q048`) — Architect a solution [2.1] · *Single-Answer Multiple Choice*

Breaking a 900-component utility monolith into `Grid_CoreSchema`, `Grid_SAPIntegrations`, `Grid_FieldApp`, and `Grid_DispatchApp` Managed Solutions exemplifies `____`.

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Horizontal/vertical **segmented Managed Solution topology** accelerates pipeline imports, isolates team blast radius, and avoids circular dependencies. [Skill 2.1: Design segmented solution topology, custom Publisher strategy, and Managed Environments | Source: Design solution topology, publisher segmentation, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/alm/segmented-solutions-alm)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

