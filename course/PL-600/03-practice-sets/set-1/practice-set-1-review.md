# Microsoft Exam PL-600: Practice Exam 1 — Sovereign Wealth Banking, Migration Throttling & VNet Integrations — Reviewer Study Key

**Theme:** Multi-Geo sovereignty, Modernized BUs & CMK, 4.2M-row cutover throttling, Power Pages vs B2B, and VNet subnet delegation  
**Credential:** Microsoft Certified: Power Platform Solution Architect Expert (`One active Associate certification required: Microsoft Certified: Power Platform Functional Consultant Associate (PL-200) OR Microsoft Certified: Power Platform Developer Associate (PL-400)`)  
**Study guide baseline:** September 23, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-600)  
**Lifecycle notice:** Exam PL-600 retired on June 30, 2026; succeeded by `Exam AB-100: Agentic AI Business Solutions Architect (Microsoft Certified: Agentic AI Business Solutions Architect Expert)`.  
**Questions:** `100` (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice percentages do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`E1Q031`) — Perform solution envisioning and requirement analysis [1.12] · *Single-Answer Multiple Choice*

Private bankers traveling aboard trans-Atlantic flights must create client meeting memos and edit opportunity stages offline, with changes syncing upon landing. Documenting exact offline CRUD tables and conflict behavior belongs in `____`.

- **A.** Capturing Functional Requirements (persona workflows, state rules, approvals, offline CRUD scope, & statutory reports)
- **B.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **C.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **D.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Specifying exact tables, persona actions, and conflict rules required during disconnected Mobile Offline operation is a core functional requirement. [Skill 1.12: Identify functional requirements across personas, business rules, approvals, and offline access | Source: Identify functional requirements across personas, offline, and workflows (https://learn.microsoft.com/en-us/power-apps/mobile/setup-mobile-offline)]

- **A:** Correct. Functional requirements specify what business behaviors and data transformations the solution must perform for each role.
- **B:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **C:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **D:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.

</details>

### Q002 (`E1Q049`) — Architect a solution [2.2] · *Single-Answer Multiple Choice*

Before writing TypeScript code for a complex trade-blotter grid, UX designers built interactive wireframes in Figma and want rapid business validation on tablets. What should the Solution Architect recommend?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Validating interactive UX prototypes (`Figma-to-App` / `Custom Pages`) early and building `PCF` controls for specialized UI gaps

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Validating interactive UX prototypes early (`Create app from Figma` / `Custom Pages`) confirms persona ergonomics cheaply before investing pro-dev effort in a custom `PCF` virtual dataset control. [Skill 2.2: Identify app customization approaches and validate interactive user experience prototypes | Source: Select customization approaches for existing apps and validate UX prototypes (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/design-consistency)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Correct. Interactive prototyping validates user journeys cheaply, while Power Apps Component Framework (`PCF`) renders reusable custom TypeScript/React controls.

</details>

### Q003 (`E1Q019`) — Perform solution envisioning and requirement analysis [1.8] · *Multi-Select (Select 2)*

Before designing integrations for a multinational clearinghouse running mainframe settlement, SAP GL, two Microsoft Entra tenants, and private MPLS circuits, which two enterprise architecture deliverables must the Solution Architect establish? Select two.

- **A.** Enterprise Architecture Context Diagram mapping systems of record, Entra tenants, hybrid networks, & sync/async SLAs
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Designating a single authoritative System of Record per entity with explicit survivorship and conflict-resolution rules
- **D.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **E.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). An Enterprise Architecture Context Diagram (mapping Entra boundaries, networks, and sync/async SLAs) plus an authoritative System-of-Record ownership matrix establish clean integration boundaries. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Correct. Evaluating the enterprise landscape clarifies authoritative boundaries, identity federation, firewall paths, and integration patterns.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Correct. Every master entity (`Customer`, `Item`, `GL Account`) needs one clear authoritative owner to prevent bi-directional data corruption.
- **D:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **E:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q004 (`E1Q061`) — Architect a solution [2.8] · *Single-Answer Multiple Choice*

Every time an institutional `Account` owning 180,000 historic `Email` and `Task` activity rows is reassigned to a new Relationship Manager, Dataverse stalls with SQL lock timeouts and inserts 180,000 share rows. What relationship change fixes this?

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Configuring `Custom` / `Referential` cascading (avoiding unintended `Parental` `Cascade All` reparent storms) and manual `N:N` intersect tables
- **D.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Changing the `1:N` relationship behavior from `Parental` (`Cascade All`) to `Custom` (`Cascade None` or `Cascade Active` on `Assign`/`Share`/`Reparent`) stops synchronous historic activity cascades and `POA` bloat. [Skill 2.8: Design Dataverse relationships (1:N, N:N, hierarchical, polymorphic) and cascading behaviors | Source: Design Dataverse relationships (1:N, N:N, hierarchical) & cascading behaviors (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Correct. Replacing `Parental` cascading on high-volume child tables prevents `POA` sharing storms, and manual `N:N` tables store rich relationship attributes.
- **D:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.

</details>

### Q005 (`E1Q007`) — Perform solution envisioning and requirement analysis [1.3] · *Single-Answer Multiple Choice*

A private wealth firm processes 40,000 structured wire-instruction PDFs monthly and wants low-code extraction of IBAN, SWIFT BIC, and beneficiary fields directly inside Power Automate cloud flows without standing up custom Azure Kubernetes ML clusters. Which component should you select?

- **A.** AI Builder prebuilt/custom document processing, text classification, & AI Prompts integrated natively in Power Platform
- **B.** Azure pro-code extension (`Azure Functions`, `Service Bus`, `AKS`, or `Azure AI Foundry`) integrated with Power Platform
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). AI Builder document processing extracts structured fields from PDFs natively inside Power Automate and Power Apps without managing custom ML infrastructure. [Skill 1.3: Identify and select components from existing apps, Dynamics 365, AppSource ISVs, and Azure | Source: Evaluate Dynamics 365 apps, AppSource ISVs, and Azure extensions (https://learn.microsoft.com/en-us/training/modules/discover-customer-needs/)]

- **A:** Correct. AI Builder embeds governed document extraction and generative AI prompts directly inside flows and apps without custom ML infrastructure.
- **B:** Incorrect. Heavy compute, long-running algorithms (> 2 minutes), and high-throughput brokered messaging offload cleanly to Azure extensions.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.

</details>

### Q006 (`E1Q081`) — Architect a solution [2.17] · *Multi-Select (Select 2)*

InfoSec requires blocking Power Automate flows from posting Dataverse data to `api.publicpaste.example` via the `HTTP` connector while permitting calls to `https://sanctions.internalbank.com`, and must license 350 external institutional CPAs who collaborate inside an internal Model-driven app. Which two designs meet these requirements? Select two.

- **A.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **B.** Enforcing `Microsoft Entra Conditional Access` (MFA & compliant device) plus `Power Platform IP Firewall` & `Cookie IP binding`
- **C.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **D.** Enforcing `DLP` + `Endpoint Filtering`, licensing external consumers via `Power Pages` (`Entra External ID`), & `Entra B2B` for internal-app guests
- **E.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). **DLP Connector Endpoint Filtering** (`Allow` `sanctions.internalbank.com`, `Deny` `*`) plus **Microsoft Entra B2B** guest access for the 350 external CPAs using an internal Model-driven app (`sec_dlp_ext_access`), hardened by **Entra Conditional Access** MFA (`sec_cond_access_ip`), satisfies both requirements. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **B:** Correct. Combining Entra Conditional Access with Managed Environment IP Firewall and session cookie binding blocks token replay from untrusted networks.
- **C:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **D:** Correct. Power Pages scales cost-effectively with `Table Permissions` for external portals, whereas Entra B2B suits external partners using internal apps.
- **E:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q007 (`E1Q048`) — Architect a solution [2.1] · *Single-Answer Multiple Choice*

Two internal development vendors created tables using `new_loan` (`Default Publisher`) and `vendorA_loan` across unmanaged Production imports. Standardizing on `____` establishes one enterprise Publisher prefix (`scb_`) and clean Managed Solution layering.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A segmented Managed Solution topology under a single custom enterprise Publisher prefix eliminates `new_` namespace pollution and unmanaged Active layers in Production. [Skill 2.1: Design segmented solution topology, custom Publisher strategy, and Managed Environments | Source: Design solution topology, publisher segmentation, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/alm/segmented-solutions-alm)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.

</details>

### Q008 (`E1Q005`) — Perform solution envisioning and requirement analysis [1.2] · *Single-Answer Multiple Choice*

Field property appraisers at a mortgage lender inspect collateral buildings in underground vaults with zero cellular coverage and require custom camera annotation plus barcode scanning synced locally via a `____`.

- **A.** Canvas Power App with a `Mobile Offline` profile and device-native camera/barcode UX tailored to frontline tasks
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **D.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A Canvas Power App configured with a `Mobile Offline` profile delivers custom device-native camera/barcode UX and local Dataverse SQLite sync without live connectivity. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Correct. Canvas apps give pixel-level task UX and offline-first Dataverse synchronization for field workers operating without connectivity.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **D:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.

</details>

### Q009 (`E1Q098`) — Implement the solution [3.7] · *Single-Answer Multiple Choice*

After importing a Managed Solution into UAT via Power Platform Pipelines, cloud flows fail immediately because they still point to Dev REST URLs and unshared personal connections. Validating `____` before promotion fixes this.

- **A.** Resolving deployment failures by running `Remove active customizations`, refactoring circular solution dependencies into a base layer, & validating stage JSON bindings
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Populating **Deployment Settings JSON** (`Environment Variables` for target URLs and `Connection References` bound to service principals) ensures zero-touch promotion across environments. [Skill 3.7: Resolve deployment plan issues, Unmanaged Active Solution Layers, and circular solution dependencies | Source: Resolve deployment plan, Solution Layer, and pipeline dependency issues (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Correct. Stripping Unmanaged Active layers and decoupling circular references ensures repeatable, zero-touch Managed Solution Upgrades.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q010 (`E1Q025`) — Perform solution envisioning and requirement analysis [1.10] · *Single-Answer Multiple Choice*

A legacy leasing extract contains 19% duplicate borrower records with differently formatted tax IDs (`12-3456789` vs `123456789`), null mandatory country codes, and orphaned collateral foreign keys. What must the Solution Architect establish before building migration pipelines?

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Defining pre-cutover data quality standards (deduplication keys, mandatory completeness, referential integrity, & domain mappings)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Defining pre-cutover data quality standards (canonical tax-ID formatting, deduplication survivorship, mandatory completeness, and orphaned key remediation) prevents dirty loads and Alternate Key collisions. [Skill 1.10: Define use cases and data quality standards for existing data prior to migration or integration | Source: Define use cases and data quality standards for existing data (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Correct. Enforcing cleansing and deduplication gates before migration prevents garbage-in/garbage-out failures in Dataverse.

</details>

### Q011 (`E1Q051`) — Architect a solution [2.3] · *Single-Answer Multiple Choice*

Six squads are each building duplicate header banners, currency-conversion Power Automate logic, and custom REST wrappers for the bank’s sanctions API. How should the Solution Architect maximize component reuse and communicate interactions?

- **A.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **B.** Reusing `Component Libraries`, `PCF`, `Child Flows`, & `Custom Connectors`, documented via `ERD`, `Sequence`, & `Context` diagrams
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Centralizing UI in `Canvas Component Libraries` / `PCF`, shared automation in `Child Cloud Flows`, and REST contracts in `Custom Connectors` — documented via `ERD`, `Sequence`, and `C4 Context` diagrams — eliminates duplicate debt. [Skill 2.3: Maximize component reuse (PCF, Component Libraries, Child Flows) and communicate designs visually | Source: Maximize component reuse (PCF, Component Libraries, Child Flows) & visual diagrams (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)]

- **A:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **B:** Correct. Shared component catalogs eliminate duplicate maintenance, while visual architecture diagrams align technical and business stakeholders.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q012 (`E1Q030`) — Perform solution envisioning and requirement analysis [1.12] · *Single-Answer Multiple Choice*

During requirements workshops for a commercial credit workbench, which artifact captures persona workflows, state transitions, multi-tier approval thresholds, and statutory adverse-action letter outputs?

- **A.** Capturing Non-Functional Requirements (`RPO`/`RTO`, peak concurrency, `p95` latency, API volume, `WCAG 2.1 AA`, & retention)
- **B.** Capturing Functional Requirements (persona workflows, state rules, approvals, offline CRUD scope, & statutory reports)
- **C.** Conforming to `Dataverse Service Protection` limits (`6,000` req / `20m` compute per `5-min` window), pooling `S2S Application Users`, & honoring `Retry-After`
- **D.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Functional Requirements specify *what* business behaviors, state rules, approvals, and regulatory outputs the solution must execute for each persona. [Skill 1.12: Identify functional requirements across personas, business rules, approvals, and offline access | Source: Identify functional requirements across personas, offline, and workflows (https://learn.microsoft.com/en-us/power-apps/mobile/setup-mobile-offline)]

- **A:** Incorrect. Non-functional requirements govern architectural sizing, BCDR, licensing capacity, offline design, and security controls.
- **B:** Correct. Functional requirements specify what business behaviors and data transformations the solution must perform for each role.
- **C:** Incorrect. Service Protection enforces per-user/per-web-server 5-minute sliding caps (`HTTP 429`); pooling S2S Application Users and respecting `Retry-After` maximizes throughput.
- **D:** Incorrect. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.

</details>

### Q013 (`E1Q058`) — Architect a solution [2.6] · *Single-Answer Multiple Choice*

Board risk officers require cross-system dashboards blending Dataverse commercial exposures with 14 TB of historical market-var parquet tables in OneLake without impacting transactional Dataverse SQL CPU. Which architecture should you recommend?

- **A.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Microsoft Fabric Link for Dataverse` (`OneLake` / `Azure Synapse Link`) offloads analytical workloads from transactional SQL and powers cross-source Power BI reports with Row-Level Security (`RLS`). [Skill 2.6: Design data visualization strategies across Dataverse charts, Power BI RLS, and Fabric/Synapse Link | Source: Design data visualization (Dataverse charts, Power BI RLS, Fabric/Synapse Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-synapse)]

- **A:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Correct. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.

</details>

### Q014 (`E1Q037`) — Perform solution envisioning and requirement analysis [1.15] · *Ordered Sequence (Multiple Choice)*

A wealth management client presents 180 business requirements and asks how your architecture team decides between standard configuration, third-party packages, and custom C# code. Which sequence represents best-practice Power Platform fit/gap analysis?

- **A.** Validate each requirement against out-of-the-box Dataverse & Dynamics 365 capabilities → Evaluate declarative low-code configuration → Assess vetted AppSource ISV solutions → Specify targeted pro-code extensions only for remaining gaps
- **B.** Build bespoke React SPAs and C# plug-ins for every requirement first → Replace standard Dynamics 365 tables with custom tables → Ignore AppSource → Check standard features last
- **C.** Accept every stakeholder wish into Phase 1 without feasibility scoring → Skip MVP boundaries → Hardcode workarounds in Production → Defer licensing impact checks until billing
- **D.** Inject unsupported DOM-scraping JavaScript into Model-driven forms → Modify SQL indexes directly via TDS → Bypass security roles → Lock out Microsoft updates

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Structured fit/gap validates native Dataverse/Dynamics 365 features first, then declarative low-code configuration, then vetted AppSource ISVs, reserving custom pro-code strictly for remaining high-value gaps. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Correct. Fit/gap analysis prioritizes standard platform/Dynamics 365 features first, then declarative configuration, then supported AppSource ISVs, reserving custom code strictly for true differentiators.
- **B:** Incorrect. Defaulting to custom code and duplicating restricted/standard Dynamics 365 tables inflates TCO and breaks product upgrades.
- **C:** Incorrect. Unbounded scope acceptance without feasibility or licensing evaluation derails timelines and budgets.
- **D:** Incorrect. Unsupported DOM manipulation and direct SQL writes violate Microsoft supportability contracts and break on wave updates.

</details>

### Q015 (`E1Q010`) — Perform solution envisioning and requirement analysis [1.4] · *Single-Answer Multiple Choice*

A brokerage plans to migrate 650,000 open client accounts while leaving 19 years of closed cold archival trade tickets (1.4 billion rows) accessible only for annual compliance queries. Which architectural alternative best minimizes Dataverse migration effort and Database storage cost?

- **A.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Migrating only active operational accounts into Dataverse while surfacing cold multi-terabyte historical archives through Microsoft Fabric / Azure Data Lake + Power BI avoids costly, multi-week Dataverse relational loads. [Skill 1.4: Identify and estimate data migration and integration efforts, complexity drivers, and alternatives | Source: Estimate migration and integration efforts and alternatives (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Correct. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).

</details>

### Q016 (`E1Q029`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

Two regional VPs give contradictory approval rules during workshops: Zurich says relationship managers approve fee waivers up to `$25,000`, while Frankfurt says compliance must sign off above `$5,000`. What should the Solution Architect lead before sprint commitment?

- **A.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Harmonizing core approval workflows into a standardized future-state process (with data-driven threshold parameters for genuine regulatory differences) resolves stakeholder conflicts cleanly. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.

</details>

## Case Study Vignette — SovereignCrest Private Bank

> SovereignCrest Private Bank operates across Zurich, Frankfurt, and New York under strict Swiss/EU data-residency laws, replacing 14 Lotus Notes apps with Dynamics 365 Sales & Power Platform. Advisors need cross-BU wealth matrix visibility, column-masked net-worth fields, and Customer-Managed Keys (CMK) in Managed Environments.

### Q017 (`E1Q003`) — Perform solution envisioning and requirement analysis [1.1] · *Single-Answer Multiple Choice*

Case study — SovereignCrest Private Bank: Regulators require SovereignCrest Private Bank to enforce Zero Trust conditional access, customer-managed encryption keys (`CMK`), and strict cross-border connector blocking across Zurich and Frankfurt environments. Which Well-Architected pillar directly governs these controls?

- **A.** Power Platform Well-Architected `Performance Efficiency` pillar (delegable queries, API throughput budgets, & elastic scaling)
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)
- **D.** Power Platform Well-Architected `Security` pillar (Zero Trust Entra identity, least privilege, DLP, & encryption)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). The Power Platform Well-Architected `Security` pillar governs defense-in-depth identity, least-privilege access, Customer-Managed Keys (`CMK`), and Data Loss Prevention (`DLP`) guardrails. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Incorrect. Performance Efficiency optimizes response latency and resource utilization via query delegation, indexing, batching, and Elastic/async patterns.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.
- **D:** Correct. The Security pillar protects confidentiality and integrity through Entra Conditional Access, least-privilege roles, DLP endpoint rules, and CMK/Lockbox.

</details>

### Q018 (`E1Q014`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

Case study — SovereignCrest Private Bank: SovereignCrest Private Bank must keep Swiss private-banking client PII physically inside Switzerland while Frankfurt corporate-banking records reside in EU sovereign data centers. Which risk assessment priority must the Solution Architect raise before provisioning environments?

- **A.** Assessing sovereign data-residency (`Multi-Geo`), PII/PHI/ITAR compliance, `CMK`, & cross-border connector risks upfront
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Swiss FINMA and EU GDPR sovereignty rules require upfront `Multi-Geo` regional environment placement, `CMK` encryption evaluation, and cross-border connector restrictions before creating Dataverse instances. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Correct. Identifying residency and regulatory encryption constraints during envisioning prevents illegal cross-region tenant/environment placement.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q019 (`E1Q077`) — Architect a solution [2.15] · *Single-Answer Multiple Choice*

Case study — SovereignCrest Private Bank: SovereignCrest Private Bank has Zurich advisors domiciled in the `Switzerland BU` who also hold regulated mandate rights to view selected `Germany BU` family-office portfolios without changing their home Business Unit, plus ad-hoc 4-person deal teams per mandate. Which combination should you design?

- **A.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **B.** Combining `Modernized Business Units` (matrix access), `Microsoft Entra ID Security Group Teams`, & `Access Team Templates`
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **Modernized Business Units** allow assigning a user Security Roles directly in secondary BUs (`Germany BU`) without moving their home BU, while **Access Team Templates** grant lightweight deal-team access without `POA` bloat. [Skill 2.15: Design Business Units, Modernized BUs, Owner Teams, Access Team Templates, & Entra Group Teams | Source: Design Business Units, Modernized BUs, Owner/Access Teams, & Entra Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **B:** Correct. Modernized BUs enable cross-BU matrix roles, Entra Group Teams automate zero-touch RBAC, and Access Teams handle ad-hoc record collaboration cleanly.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q020 (`E1Q016`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

A merchant acquirer’s legacy CRM team insists on copying 38 custom C# batch executables and undocumented SQL triggers into the new project without source control. Adopting the `____` pillar mitigates this technical-debt risk through CI/CD pipelines and automated checks.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Power Platform Well-Architected `Operational Excellence` pillar (automated ALM pipelines, Application Insights, & CoE)
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Power Platform Well-Architected `Operational Excellence` mitigates technical-debt risk through source-controlled ALM pipelines, Solution Checker gates, and Application Insights observability. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Correct. Operational Excellence standardizes CI/CD solution pipelines, automated Solution Checker gates, telemetry, and Managed Environment governance.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q021 (`E1Q015`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

An audit of an insurer’s existing tenant reveals 140 business-critical Power Automate flows owned by a single departing contractor inside the `Default` environment with zero DLP policies. Which risk mitigation approach addresses this exposure?

- **A.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **B.** Mitigating single-maker bus-factor risk, unmonitored personal flows, & technical debt via Managed Environments and CoE
- **C.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Single-maker bus-factor ownership in the `Default` environment without DLP policies creates severe continuity and exfiltration risk, mitigated via Managed Environments, service-principal ownership, and CoE governance. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **B:** Correct. Unmanaged citizen sprawl and bespoke code without ALM pipelines represent top organizational operational risks.
- **C:** Incorrect. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q022 (`E1Q024`) — Perform solution envisioning and requirement analysis [1.9] · *Single-Answer Multiple Choice*

When modeling corporate borrowers, contact signatories, and call appointments in Dataverse so future AppSource banking ISVs and Copilot features plug in natively, you should align entities to `____`.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Aligning data entities to the Microsoft Common Data Model (`CDM`) standard tables (`Account`, `Contact`, `Activity`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Aligning schemas to the Microsoft Common Data Model (`CDM`) standard tables (`Account`, `Contact`, `Activity`) preserves Dynamics 365, ISV, Exchange, and Copilot interoperability. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Correct. Extending standard CDM tables preserves native Dynamics 365, AppSource ISV, Exchange, and AI Copilot interoperability.

</details>

### Q023 (`E1Q080`) — Architect a solution [2.16] · *Single-Answer Multiple Choice*

Wealth Regional Managing Directors need automatic read access to rows owned by their direct reports and read-only visibility 3 levels down their reporting tree without custom plug-ins. Configuring `____` satisfies this requirement natively.

- **A.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Dataverse **Hierarchy Security** (`Manager` hierarchy or `Position` hierarchy with configurable depth) grants direct-report Read/Write/Update and deeper-descendant Read access natively. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.

</details>

### Q024 (`E1Q099`) — Implement the solution [3.8] · *Single-Answer Multiple Choice*

Thirty minutes before Production cutover, you need to block all non-administrator logins and pause background asynchronous workflows so final delta records reconcile cleanly. Enabling `____` in the Power Platform admin center enforces this quiet state.

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Enabling Dataverse `Administration mode` (blocking non-admins & background jobs) during cutover, followed by smoke tests & Application Insights hypercare
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enabling Dataverse **`Administration mode`** (with background operations disabled) restricts environment access strictly to System Administrators/Customizers during cutover maintenance. [Skill 3.8: Identify go-live readiness gates, execute Administration mode cutovers, and manage hypercare telemetry | Source: Assess go-live readiness factors, Administration mode, and hypercare remediation (https://learn.microsoft.com/en-us/power-platform/admin/admin-mode)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. `Administration mode` guarantees a quiet database during final schema upgrade and delta migration before opening Production to users.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q025 (`E1Q097`) — Implement the solution [3.7] · *Multi-Select (Select 2)*

A Managed Solution `Stage for upgrade` import into Production fails to show updated form layouts because an emergency hotfix had been edited directly in Production last month, and two solutions (`Loans` and `Collateral`) fail CI builds due to mutual table-lookup references. Which two actions resolve both deployment blockers? Select two.

- **A.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix
- **B.** Resolving deployment failures by running `Remove active customizations`, refactoring circular solution dependencies into a base layer, & validating stage JSON bindings
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **E.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). Running **`Remove active customizations`** to strip the Unmanaged Active layer plus extracting shared base tables into a foundational layer (`dep_layers_deps` & `sol_segmented_alm`) eliminates circular solution dependencies and unmasks Managed upgrades. [Skill 3.7: Resolve deployment plan issues, Unmanaged Active Solution Layers, and circular solution dependencies | Source: Resolve deployment plan, Solution Layer, and pipeline dependency issues (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.
- **B:** Correct. Stripping Unmanaged Active layers and decoupling circular references ensures repeatable, zero-touch Managed Solution Upgrades.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **E:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q026 (`E1Q034`) — Perform solution envisioning and requirement analysis [1.13] · *Single-Answer Multiple Choice*

A compliance statute mandates retaining immutable KYC audit logs for `10 years` while keeping sub-2-second interactive form loads for 4,500 concurrent advisors. Which storage governance strategy aligns with this retention NFR?

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Governing `Database`, `File`, & `Log` storage pools via `Dataverse Long Term Retention`, `Fabric/Synapse Link` archival, & attachment offloading

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Governing Dataverse `Database`, `File`, and `Log` capacity via Dataverse Long Term Retention and Fabric/Synapse archival keeps active operational tables lean while satisfying 10-year compliance retention. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Correct. Keeping relational `Database` capacity lean prevents tenant admin lockouts (`Copy`/`Restore` blocks) and controls storage overage costs.

</details>

### Q027 (`E1Q054`) — Architect a solution [2.4] · *Single-Answer Multiple Choice*

Which persona scenario warrants a dedicated task-focused Canvas app rather than adding 40 custom tabs onto a back-office Model-driven app?

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Grouping capabilities into role- and task-specific apps (offline Canvas for field crews, Model-driven for back-office, Power Pages for externals)
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Frontline couriers performing rapid 3-tap barcode chain-of-custody scans offline benefit from a lightweight task-specific Canvas app while back-office staff work in a Model-driven app. [Skill 2.4: Design apps by grouping required features based on persona, role, task, and offline needs | Source: Design role-based and task-based app experiences across form factors (https://learn.microsoft.com/en-us/power-apps/guidance/planning/app-design)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Correct. Task-focused apps per persona outperform bloated one-size-fits-all apps in load speed, offline footprint, and usability.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q028 (`E1Q087`) — Implement the solution [3.2] · *Single-Answer Multiple Choice*

A maker sets a Business Rule scope to `Entity` to validate that `Credit_Limit <= 500000`, assuming it also prevents unauthorized users from reading `Credit_Limit` via `/api/data/v9.2/accounts`. Proposed solution: Enable `Column Security` on `Credit_Limit` and assign a `Column Security Profile` only to authorized underwriting teams. Does this fix the vulnerability?

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Auditing server-side `Security Roles`, `Column Security`, & `Power Pages Table Permissions` rather than trusting client-side UI rules

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — even `Entity`-scoped Business Rules only enforce server-side validation/field values on writes and **never** restrict column-level `Read` access over OData/SDK; restricting column reads requires `Column Security Profiles`. [Skill 3.2: Review security across Business Rules, Security Roles, Entra Conditional Access, & security boundaries | Source: Review end-to-end security across Business Rules, Roles, Entra ID, & boundaries (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Correct. Client JavaScript and `Form`-scoped Business Rules never block Web API/OData access; security boundaries must be enforced server-side in Dataverse.

</details>

### Q029 (`E1Q013`) — Perform solution envisioning and requirement analysis [1.5] · *Single-Answer Multiple Choice*

To prevent departmental citizen makers and pro-code developers from colliding over environment permissions and architectural standards, which governance operating model should the Solution Architect establish during discovery?

- **A.** Establishing a fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model align maker, pro-dev, and InfoSec responsibilities early. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Correct. Clear architectural ownership, ARB design gates, and CoE guardrails align business, citizen makers, pro-devs, and InfoSec.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q030 (`E1Q032`) — Perform solution envisioning and requirement analysis [1.13] · *Multi-Select (Select 3)*

A central-bank reporting system on Power Platform must pass architecture review. Which three specifications must be captured as **Non-Functional Requirements (`NFRs`)**? Select three.

- **A.** Capturing Non-Functional Requirements (`RPO`/`RTO`, peak concurrency, `p95` latency, API volume, `WCAG 2.1 AA`, & retention)
- **B.** Power Platform Well-Architected `Reliability` pillar (RPO/RTO targets, fault isolation, retries, & circuit breakers)
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **E.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **F.** Designing for `WCAG 2.1 AA` accessibility (`AccessibleLabel`, `TabIndex`, contrast) and `.resx` multi-language localization

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B, F` (`CSV: 1,2,6`)

Correct answers: A, B, and F (are correct). Peak concurrency/latency/API volume/retention (`req_nfr_spec`), `WCAG 2.1 AA` accessibility & multi-language localization (`ux_wcag_accessible`), and `RPO`/`RTO` disaster-recovery resilience (`wa_reliability`) are core NFRs. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Correct. Non-functional requirements govern architectural sizing, BCDR, licensing capacity, offline design, and security controls.
- **B:** Correct. The Reliability pillar ensures mission-critical workloads withstand transient outages, throttling, and regional faults within defined RPO/RTO bounds.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **E:** Incorrect. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **F:** Correct. Building accessibility and localization into initial UX components avoids expensive retrofits before public or enterprise launch.

</details>

### Q031 (`E1Q084`) — Implement the solution [3.1] · *Single-Answer Multiple Choice*

Before promoting Release Candidate `v1.0` to UAT, your automated Azure DevOps pipeline runs static analysis that flags `new ColumnSet(true)` inside C# plug-ins and 14 Canvas non-delegable `Filter` warnings. Which quality gate enforces these checks?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Enforcing `Solution Checker` and `App Checker` gates in CI/CD pipelines alongside `Power Platform Well-Architected` design reviews

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Running **Solution Checker** (for plug-ins, workflows, and web resources) and **App Checker** (for Canvas delegation, performance, and WCAG accessibility) inside CI/CD pipelines catches architectural anti-patterns before UAT. [Skill 3.1: Evaluate detailed designs and implementations with Solution Checker, App Checker, & Well-Architected | Source: Evaluate detailed designs with Solution Checker, App Checker, & Well-Architected (https://learn.microsoft.com/en-us/power-platform/alm/use-powershell-cmdlets-solution-checker)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Correct. Solution Checker flags unbounded queries and sync plug-in anti-patterns, while App Checker catches delegation warnings and WCAG errors before release.

</details>

### Q032 (`E1Q039`) — Perform solution envisioning and requirement analysis [1.15] · *Single-Answer Multiple Choice*

Stakeholders ask to modify Dataverse’s underlying SQL `sys.indexes` directly via SSMS over TDS port `5558` to close a reporting gap. How should you address this during fit/gap analysis?

- **A.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Structured Fit/Gap matrix scoring requirements across `Out-of-the-Box`, `Configuration`, `AppSource ISV`, & `Custom Code`
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Formal fit/gap analysis flags direct SQL DDL over read-only TDS (`5558`) as unsupported/infeasible and maps the requirement to supported Dataverse indexing or Microsoft Fabric Link. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Correct. Formal fit/gap scoring exposes customization TCO, licensing impacts, and upgrade maintenance trade-offs transparently.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q033 (`E1Q018`) — Perform solution envisioning and requirement analysis [1.7] · *Single-Answer Multiple Choice*

Sixty days after launching a treasury exceptions portal, leadership wants objective proof that reduced manual rework matches the approved business case. Which validation approach should you use?

- **A.** Defining baseline-backed `SMART` success KPIs (cycle-time reduction, error-rate drop, SLA adherence, & active adoption %)
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Tracking baseline-anchored cycle-time reduction, straight-through processing (`STP`) error-rate drop, SLA compliance percentage, and active persona adoption validates tangible business value. [Skill 1.7: Review and validate measurable key success criteria, KPIs, and adoption targets | Source: Review measurable key success criteria, KPIs, and adoption targets (https://learn.microsoft.com/en-us/power-platform/guidance/adoption/measure-business-value)]

- **A:** Correct. Quantifiable KPIs anchored to current-state baselines let stakeholders verify objective ROI after go-live.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q034 (`E1Q075`) — Architect a solution [2.14] · *Single-Answer Multiple Choice*

A bank’s network team states: `"Because our data center already has Azure ExpressRoute Microsoft Peering, Dataverse now sits inside our private `10.0.0.0/8` LAN automatically."` Proposed solution: Explain that ExpressRoute routes public Microsoft peering traffic over private fiber, and configure Power Platform VNet subnet delegation or an On-Premises Data Gateway cluster to reach private RFC1918 endpoints. Is this architecturally accurate?

- **A.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — Azure ExpressRoute does NOT place Dataverse inside private VNet/LAN RFC1918 IP space by itself; private backend reachability requires Power Platform VNet integration or an On-Premises Data Gateway cluster. [Skill 2.14: Assess VNet subnet delegation, Azure ExpressRoute nuances, Data Gateways, and IP firewall networking | Source: Assess VNet integration, Azure ExpressRoute, gateways, and IP firewall networking (https://learn.microsoft.com/en-us/power-platform/admin/vnet-support-overview)]

- **A:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Correct. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q035 (`E1Q036`) — Perform solution envisioning and requirement analysis [1.14] · *Single-Answer Multiple Choice*

Twelve acquired regional brokerages each use different 9-stage opportunity pipelines, preventing consolidated board forecasting. How should the Solution Architect guide future-state process design?

- **A.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating
- **B.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Harmonizing all 12 brokerages onto one canonical future-state pipeline (isolating only legally mandated regional steps via conditional branching) enables unified forecasting. [Skill 1.14: Guide future-state business process optimization and standardization before automating | Source: Guide future-state business process optimization and standardization (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/overview)]

- **A:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.
- **B:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q036 (`E1Q041`) — Perform solution envisioning and requirement analysis [1.16] · *Single-Answer Multiple Choice*

A project manager suggests buying standalone Power Apps per-app licenses for 600 dispute agents and granting them CRUD rights on the standard Dynamics 365 `Case` (`incident`) and `Entitlement` tables. Which constraint must you flag?

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Validating Dynamics 365 restricted-table licensing (`Case / incident`, `Work Order`, `Entitlement`) during fit/gap analysis
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Case` (`incident`) and `Entitlement` are Dynamics 365 **restricted tables**; users creating, updating, or deleting rows in restricted tables require qualifying Dynamics 365 licenses. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Correct. Restricted Dynamics 365 tables require appropriate Dynamics 365 licenses for CRUD operations rather than standalone Power Apps licenses.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q037 (`E1Q086`) — Implement the solution [3.2] · *Multi-Select (Select 2)*

During a pre-go-live security review, you discover makers hid `Tax_ID` and `Bonus_Compensation` using a `Form`-scoped Business Rule and relied on browser network location checks instead of Conditional Access. Which two remediation actions are mandatory? Select two.

- **A.** Auditing server-side `Security Roles`, `Column Security`, & `Power Pages Table Permissions` rather than trusting client-side UI rules
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Enforcing `Microsoft Entra Conditional Access` (MFA & compliant device) plus `Power Platform IP Firewall` & `Cookie IP binding`
- **D.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **E.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). Auditing server-side Dataverse boundaries (`Column Security Profiles` + `Security Roles`, never trusting client `Form` Business Rules) (`val_sec_boundary_audit`) and enforcing `Microsoft Entra Conditional Access` + `Power Platform IP Firewall` (`sec_cond_access_ip`) secure API, OData, and session access. [Skill 3.2: Review security across Business Rules, Security Roles, Entra Conditional Access, & security boundaries | Source: Review end-to-end security across Business Rules, Roles, Entra ID, & boundaries (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Correct. Client JavaScript and `Form`-scoped Business Rules never block Web API/OData access; security boundaries must be enforced server-side in Dataverse.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Correct. Combining Entra Conditional Access with Managed Environment IP Firewall and session cookie binding blocks token replay from untrusted networks.
- **D:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **E:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q038 (`E1Q033`) — Perform solution envisioning and requirement analysis [1.13] · *Single-Answer Multiple Choice*

Public-sector banking procurement mandates screen-reader landmarks, keyboard-only `TabIndex` navigation, and `4.5:1` contrast ratios across all Canvas and Power Pages screens under `____`.

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Designing for `WCAG 2.1 AA` accessibility (`AccessibleLabel`, `TabIndex`, contrast) and `.resx` multi-language localization
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Designing for `WCAG 2.1 AA` accessibility (`AccessibleLabel`, logical `TabIndex`, contrast tokens) and `.resx` localization from day one satisfies regulatory accessibility NFRs. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Correct. Building accessibility and localization into initial UX components avoids expensive retrofits before public or enterprise launch.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q039 (`E1Q017`) — Perform solution envisioning and requirement analysis [1.7] · *Single-Answer Multiple Choice*

An executive sponsor states the project goal as `"Make commercial loan servicing feel modern and fast."` How should the Solution Architect refine this statement into valid key success criteria?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Defining baseline-backed `SMART` success KPIs (cycle-time reduction, error-rate drop, SLA adherence, & active adoption %)
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Subjective phrases cannot verify go-live ROI; architects rewrite them into baseline-backed `SMART` KPIs (such as cutting average loan cycle time from `9 days` to `< 6 hours` with `>= 90%` 60-day underwriter adoption). [Skill 1.7: Review and validate measurable key success criteria, KPIs, and adoption targets | Source: Review measurable key success criteria, KPIs, and adoption targets (https://learn.microsoft.com/en-us/power-platform/guidance/adoption/measure-business-value)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Correct. Quantifiable KPIs anchored to current-state baselines let stakeholders verify objective ROI after go-live.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q040 (`E1Q047`) — Architect a solution [2.1] · *Multi-Select (Select 2)*

An enterprise bank has four independent delivery squads (`Core CDM Schema`, `Shared Integrations`, `Commercial Lending App`, `Private Wealth App`) deploying to Production on independent bi-weekly cadences. Which two architectural practices should govern solution topology and environments? Select two.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Dedicated `Dev -> Test -> UAT -> Prod` environments (plus sovereign `Multi-Geo` instances) governed by `Managed Environments` & `CoE Starter Kit`
- **D.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix
- **E.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, D` (`CSV: 3,4`)

Correct answers: C and D (are correct). Segmented Managed Solutions (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix paired with multi-tier Managed Environments (`Dev -> Test -> UAT -> Prod`) enable independent, safe ALM releases. [Skill 2.1: Design segmented solution topology, custom Publisher strategy, and Managed Environments | Source: Design solution topology, publisher segmentation, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/alm/segmented-solutions-alm)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Correct. Multi-tier ALM environments isolate production workloads, Multi-Geo satisfies regional residency, and CoE + Managed Environments automate governance.
- **D:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.
- **E:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q041 (`E1Q028`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

In a refined backlog item — `"As a Margin Officer, I need automated margin breach freezes so over-leveraged accounts halt trading within 60 seconds"` — attaching testable `Given / When / Then` conditions exemplifies `____`.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Refining prescriptive wishes into persona-based `User Stories` (`As a ... I need ... so that ...`) with testable Acceptance Criteria

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Pairing outcome-driven User Stories with testable `Given / When / Then` Acceptance Criteria anchors developer implementation and QA verification. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Correct. Outcome-oriented User Stories decouple business intent from premature UI assumptions and anchor QA test cases.

</details>

## Case Study Vignette — Vespera Wealth Portal

> Vespera Wealth Portal serves 180,000 external retail investors submitting KYC renewals and viewing household portfolios online, alongside 350 external CPAs collaborating on institutional Dataverse rows. Architects must select external identity providers, prevent SharePoint document ACL leaks, and enforce strict DLP endpoint rules.

### Q042 (`E1Q068`) — Architect a solution [2.11] · *Single-Answer Multiple Choice*

Case study — Vespera Wealth Portal: Advisors attach highly confidential client trust deeds in Dataverse, and InfoSec discovered that out-of-the-box SharePoint Document Management allowed site members outside the Dataverse Access Team to open those folders in SharePoint. How should you remediate this?

- **A.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **B.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **C.** Mitigating SharePoint Document Management’s lack of automatic Dataverse ACL sync via Dataverse `File` columns, Azure Blob SAS, or custom ACL sync
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Default SharePoint Document Management never syncs Dataverse row ACLs to SharePoint; storing sensitive trust deeds in native Dataverse `File` columns (enforcing Dataverse row/column security) or implementing Azure Blob SAS / custom ACL sync closes the leak. [Skill 2.11: Design collaboration (Teams, SharePoint ACL nuances, Exchange) and Dynamics 365 Dual-write integrations | Source: Design Teams, SharePoint, Exchange, and Dynamics 365 (Dual-write) integrations (https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dual-write/dual-write-overview)]

- **A:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **B:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **C:** Correct. Default SharePoint integration never copies Dataverse row permissions to SharePoint folders; confidential files require `File` columns or explicit ACL sync.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q043 (`E1Q079`) — Architect a solution [2.16] · *Single-Answer Multiple Choice*

Case study — Vespera Wealth Portal: Vespera’s historic CRM accumulated 92 million rows in the `PrincipalObjectAccess` (`POA`) SQL table from years of manual per-record sharing and `Parental` cascades, slowing every Account view to 14 seconds. How do you prevent `POA` bloat in the new Dataverse architecture?

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Preventing `PrincipalObjectAccess (POA)` table bloat by replacing manual per-record sharing and `Parental` cascades with `Access Team Templates`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Replacing manual user-by-user sharing and `Parental` `Cascade All` relationships with **Access Team Templates** (which store team rows cleanly without exploding `POA` security descriptors) and **Entra Group Owner Teams** keeps `POA` lean. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Correct. Millions of `POA` rows from manual sharing and `Cascade All` relationships degrade SQL query performance across Dataverse views.

</details>

### Q044 (`E1Q082`) — Architect a solution [2.17] · *Single-Answer Multiple Choice*

Case study — Vespera Wealth Portal: Vespera Wealth Portal must authenticate 180,000 external retail investors submitting KYC renewals online while restricting each investor strictly to rows linked to their own `Contact` and household `Account`. What should you architect?

- **A.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Enforcing `DLP` + `Endpoint Filtering`, licensing external consumers via `Power Pages` (`Entra External ID`), & `Entra B2B` for internal-app guests
- **D.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Deploying **Microsoft Power Pages** with **`Microsoft Entra External ID`** (`Azure AD B2C`) authentication and `Contact`-/`Account`-scoped **`Table Permissions`** scales securely to 180,000 external retail investors. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Correct. Power Pages scales cost-effectively with `Table Permissions` for external portals, whereas Entra B2B suits external partners using internal apps.
- **D:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.

</details>

### Q045 (`E1Q044`) — Perform solution envisioning and requirement analysis [1.17] · *Single-Answer Multiple Choice*

Relationship managers want an inline interactive yield-curve slider rendered directly on a Model-driven Opportunity form column instead of opening an external web app. Which supported extensibility option closes this UI gap?

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **D.** Addressing gaps via supported extensibility (`Custom Pages`, `PCF`, `Power Fx Formula columns`, `Custom APIs`) over bespoke clones

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Building a Power Apps Component Framework (`PCF`) code component (or `Custom Page`) closes specialized UI gaps natively inside Model-driven forms while preserving wave-update supportability. [Skill 1.17: Address functional gaps through supported low-code/pro-code alternate solutions | Source: Address functional gaps through low-code/pro-code alternate solutions (https://learn.microsoft.com/en-us/power-platform/well-architected/operational-excellence/overview)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **D:** Correct. Supported platform extensibility closes UX and logic gaps while preserving Microsoft wave-update compatibility.

</details>

### Q046 (`E1Q001`) — Perform solution envisioning and requirement analysis [1.1] · *Ordered Sequence (Multiple Choice)*

A global custody bank is launching an enterprise client-onboarding program on Microsoft Power Platform and wants the Solution Architect to sequence envisioning and architecture alignment in accordance with Microsoft Power Platform Well-Architected. Which four-step sequence should you follow?

- **A.** Copy every legacy Access table 1-for-1 into Dataverse → Replicate broken manual steps verbatim → Ignore API and storage limits → Run fit/gap analysis during user acceptance testing
- **B.** Capture business outcomes, KPIs, & risk constraints → Map current-state processes & existing enterprise systems → Refine functional & non-functional requirements → Align target architecture to Power Platform Well-Architected pillars
- **C.** Write custom C# plug-ins on Day 1 → Purchase all Dynamics 365 licenses blindly → Skip current-state discovery → Capture non-functional requirements after Production go-live
- **D.** Grant System Administrator to all stakeholders → Build prototypes in personal My Flows → Skip security & residency discovery → Export Unmanaged Default Solution to Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Solution envisioning starts by anchoring measurable business outcomes, KPIs, and risk constraints, then maps current-state processes and systems, refines functional and non-functional specs, and aligns architectural trade-offs to Power Platform Well-Architected pillars. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Incorrect. Lifting and shifting broken legacy schemas without process optimization or fit/gap analysis perpetuates technical debt.
- **B:** Correct. Solution envisioning establishes measurable business outcomes and risks first, inventories current processes/systems, refines functional & NFR specs, and aligns design trade-offs to Well-Architected pillars.
- **C:** Incorrect. Coding or buying licenses before discovery and NFR capture causes costly rework and architectural mismatches.
- **D:** Incorrect. Prototyping in Default Solution with over-privileged accounts violates governance and creates un-deployable artifacts.

</details>

### Q047 (`E1Q021`) — Perform solution envisioning and requirement analysis [1.8] · *Single-Answer Multiple Choice*

During enterprise landscape review, you discover an acquired wealth subsidiary authenticates employees in a separate `Entra ID` tenant while the parent bank runs Dataverse in its primary tenant. Which artifact captures cross-tenant identity, licensing, and network boundaries?

- **A.** Enterprise Architecture Context Diagram mapping systems of record, Entra tenants, hybrid networks, & sync/async SLAs
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Mapping cross-tenant identity (`Entra B2B` trust, Conditional Access, licensing assignment) and network paths inside the Enterprise Architecture Context Diagram surfaces tenant blockers early. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Correct. Evaluating the enterprise landscape clarifies authoritative boundaries, identity federation, firewall paths, and integration patterns.
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q048 (`E1Q092`) — Implement the solution [3.4] · *Single-Answer Multiple Choice*

Two automated treasury workers read `Margin_Balance = 100,000` simultaneously and both write updates without checking row versions, silently losing the first debit. Passing the HTTP `____` header (`ETag` / `RowVersion`) on Dataverse Web API `PATCH` calls prevents lost updates.

- **A.** Resolving automation/integration conflicts via `Select columns` (`filteringattributes`), `Trigger Conditions`, plug-in `Depth` checks, & `ETag` (`If-Match`) optimistic concurrency
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enforcing **Optimistic Concurrency** via `If-Match: W/"<RowVersion>"` (`ConcurrencyBehavior.IfRowVersionMatches` in SDK) rejects stale concurrent writes with `HTTP 412 Precondition Failed` instead of silently overwriting data. [Skill 3.4: Assess storage/resource impact and resolve automation loops, race conditions, & integration conflicts | Source: Assess storage/resource impact and resolve automation & integration conflicts (https://learn.microsoft.com/en-us/power-platform/admin/capacity-storage)]

- **A:** Correct. Column filters, actor exclusions, and `If-Match` row-version headers eliminate infinite ping-pong loops and silent lost-update race conditions.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q049 (`E1Q002`) — Perform solution envisioning and requirement analysis [1.1] · *Single-Answer Multiple Choice*

An institutional treasury desk requires automated circuit breakers, idempotent retries, and validated 15-minute `RPO` / 2-hour `RTO` targets across its Power Platform trade-settlement workflows. In the Microsoft Power Platform Well-Architected framework, these design requirements map primarily to the `____` pillar.

- **A.** Power Platform Well-Architected `Performance Efficiency` pillar (delegable queries, API throughput budgets, & elastic scaling)
- **B.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Power Platform Well-Architected `Reliability` pillar (RPO/RTO targets, fault isolation, retries, & circuit breakers)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). The Power Platform Well-Architected `Reliability` pillar governs fault isolation, transient retry/circuit-breaker patterns, and disaster recovery RPO/RTO resilience. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Incorrect. Performance Efficiency optimizes response latency and resource utilization via query delegation, indexing, batching, and Elastic/async patterns.
- **B:** Incorrect. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Correct. The Reliability pillar ensures mission-critical workloads withstand transient outages, throttling, and regional faults within defined RPO/RTO bounds.

</details>

### Q050 (`E1Q012`) — Perform solution envisioning and requirement analysis [1.5] · *Single-Answer Multiple Choice*

Desktop underwriters copy borrower figures across four legacy apps and an unapproved desktop macro. Applying `____` captures recorded user UI actions and screen transitions alongside event logs to quantify repetitive manual steps prior to redesign.

- **A.** Power Automate Process Mining & Task Mining paired with cross-functional current-state discovery workshops
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Power Automate Task Mining and Process Mining analyze desktop actions and event logs objectively to pinpoint repetitive copy-paste bottlenecks. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Correct. Combining telemetry-driven Process/Task Mining with SME workshops exposes hidden rework loops and shadow processes objectively.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.

</details>

### Q051 (`E1Q090`) — Implement the solution [3.3] · *Single-Answer Multiple Choice*

Separate from 5-minute real-time Service Protection spikes, an integration architect must verify that 1.8 million daily automated ERP flow actions will not exhaust 24-hour tenant licensing entitlements. How do you govern 24-hour capacity and reduce per-call consumption?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Sizing 24-hour `Power Platform Request (PPR)` capacity and using `CreateMultiple` / `UpdateMultiple` / `$batch` (`ExecuteMultiple` `<= 1,000`)
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Sizing 24-hour **Power Platform Request (`PPR`)** entitlements (adding PPR capacity packs or Pay-As-You-Go where needed) and consolidating single-row calls into `CreateMultiple`, `UpdateMultiple`, or `$batch` (`ExecuteMultiple` `<= 1,000`) cuts daily request burn dramatically. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Correct. Bulk messages (`CreateMultiple`/`UpdateMultiple`) and `$batch` cut network round-trips dramatically while keeping daily PPR consumption within entitlements.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q052 (`E1Q069`) — Architect a solution [2.12] · *Multi-Select (Select 3)*

A capital-markets enterprise integration hub must expose internal REST services safely to Power Platform, decouple Dataverse commits via brokered queues with Dead-Letter Queues, and expose reusable bound operations inside Dataverse solutions. Which three components work together cleanly? Select three.

- **A.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **E.** Integrating Microsoft Teams (`Adaptive Cards` / embedded apps), Dynamics 365 F&O `Dual-write` + `Business Events`, & `Server-Side Sync`
- **F.** Defining solution-aware Dataverse `Custom APIs` exposing strongly typed request/response contracts for internal and external callers

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E, F` (`CSV: 3,5,6`)

Correct answers: C, E, and F (are correct). `Azure API Management` + Dataverse `Service Endpoints` (`Service Bus` / `Event Grid` with DLQ) (`integ_async_asb_apim`), solution-aware `Custom APIs` (`integ_custom_api`), and `Dynamics 365 Dual-write` / `Business Events` / `Teams Adaptive Cards` (`integ_teams_sp_d365`) form a complete enterprise integration architecture. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **E:** Correct. Dual-write provides near-real-time bi-directional Dataverse-to-F&O sync, while Teams Adaptive Cards meet users directly in collaboration channels.
- **F:** Correct. Custom APIs replace legacy Custom Process Actions with code-first, solution-aware OData bound/unbound operations and granular privilege checks.

</details>

### Q053 (`E1Q020`) — Perform solution envisioning and requirement analysis [1.8] · *Single-Answer Multiple Choice*

An enterprise architecture board prohibits external SaaS connectors from reaching internal treasury APIs without centralized mutual-TLS validation, IP rate limiting, and OpenAPI schema governance. Fronting internal APIs with `____` satisfies this enterprise boundary.

- **A.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Fronting internal APIs with Azure API Management (`APIM`) paired with brokered Service Bus/Event Grid messaging enforces mutual TLS, OAuth token validation, rate quotas, and versioned OpenAPI contracts. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.

</details>

### Q054 (`E1Q078`) — Architect a solution [2.16] · *Multi-Select (Select 3)*

A sovereign wealth fund requires: (1) masking `Liquid_Net_Worth` from general bankers while allowing Wealth Directors to view it, (2) zero standing `System Administrator` accounts in Production, and (3) explicit bank-executive approval before any Microsoft support engineer inspects tenant data. Which three controls must you combine? Select three.

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access
- **C.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **D.** Enforcing `Microsoft Entra Conditional Access` (MFA & compliant device) plus `Power Platform IP Firewall` & `Cookie IP binding`
- **E.** Preventing `PrincipalObjectAccess (POA)` table bloat by replacing manual per-record sharing and `Parental` cascades with `Access Team Templates`
- **F.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D, E` (`CSV: 2,4,5`)

Correct answers: B, D, and E (are correct). `Column Security Profiles` + `Microsoft Entra PIM` just-in-time admin elevation + `Customer Lockbox` / `CMK` (`sec_col_hier_pim`), paired with `Entra Conditional Access` + `Power Platform IP Firewall` (`sec_cond_access_ip`) and `POA` sharing hygiene (`sec_poa_hygiene`), deliver defense-in-depth governance. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.
- **C:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **D:** Correct. Combining Entra Conditional Access with Managed Environment IP Firewall and session cookie binding blocks token replay from untrusted networks.
- **E:** Correct. Millions of `POA` rows from manual sharing and `Cascade All` relationships degrade SQL query performance across Dataverse views.
- **F:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q055 (`E1Q073`) — Architect a solution [2.13] · *Single-Answer Multiple Choice*

A treasury legacy mainframe terminal from 1998 has zero APIs or database connectors and requires automated nightly reconciliation across 12 VMs resilient to individual bot crashes. Which architecture meets both BCDR and legacy-automation needs?

- **A.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **B.** Designing BCDR around Dataverse point-in-time backups (`28-day` Prod retention, cross-Geo failover limits) and `Hosted RPA` + `Work Queues` for legacy UI
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Pairing Dataverse geo-redundant point-in-time backups (`28-day` Prod retention) with **Hosted RPA machine groups** + **Work Queues** processes UI-only mainframe items resiliently with automatic retry and SLA tracking. [Skill 2.13: Design authentication (OBO vs S2S, Managed Identity), BCDR (RPO/RTO, geo-backups), and RPA | Source: Design authentication (OBO vs S2S, Managed Identity), BCDR, and RPA architectures (https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments)]

- **A:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **B:** Correct. Architects align RPO/RTO to Microsoft’s managed geo-replication SLAs and isolate UI-only legacy integrations behind resilient RPA Work Queues.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.

</details>

### Q056 (`E1Q064`) — Architect a solution [2.9] · *Single-Answer Multiple Choice*

Field relationship managers need `Mobile Offline` read/write access, Dataverse `User/Team` row-level security, column-level auditing, and native SLA timers on 120,000 active wealth prospects sourced from an external CRM. Should you use Virtual Tables or replicate into native Dataverse tables?

- **A.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **B.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **C.** Replicating data into native Dataverse tables (`Dataflows` / `ADF`) when Mobile Offline, row-level security roles, auditing, or SLAs are required
- **D.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Replicating into native Dataverse tables (`Dataflows` / `ADF`) is mandatory whenever `Mobile Offline`, `User/Team` row ownership security, column auditing, or native SLAs are required. [Skill 2.9: Determine when to connect external data in place (Virtual tables) versus import/replicate into Dataverse | Source: Connect external data in place (Virtual tables) vs import/replicate into Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-virtual-entities)]

- **A:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **B:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **C:** Correct. Virtual tables do not support Mobile Offline sync, Dataverse row-level User/Team ownership, or native column auditing.
- **D:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.

</details>

### Q057 (`E1Q023`) — Perform solution envisioning and requirement analysis [1.9] · *Single-Answer Multiple Choice*

Both Dynamics 365 Sales and the core banking ledger allow staff to edit a corporate client’s legal tax address without ownership rules, causing nightly overwrites. Enforcing `____` designates one authoritative system and conflict-resolution rules.

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Designating a single authoritative System of Record per entity with explicit survivorship and conflict-resolution rules
- **C.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Designating a single authoritative System of Record per entity/attribute with explicit survivorship rules eliminates dual-master data corruption. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Correct. Every master entity (`Customer`, `Item`, `GL Account`) needs one clear authoritative owner to prevent bi-directional data corruption.
- **C:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q058 (`E1Q088`) — Implement the solution [3.3] · *Ordered Sequence (Multiple Choice)*

An overnight core-banking sync job fails every night at 02:15 with bursts of `HTTP 429 Too Many Requests` from Dataverse. Which four-step remediation sequence aligns with Microsoft’s Service Protection architecture?

- **A.** Move bulk integration loops inside synchronous Dataverse plug-ins → Chain 8 child plug-in updates per row → Enable `RetrieveAllEntities` metadata calls on every transaction → Disable caching
- **B.** Buy 100 Power BI Free licenses expecting them to lift 5-minute Service Protection caps → Hardcode personal maker credentials → Ignore `x-ms-ratelimit-time-remaining-xrm-requests` headers → Discard throttled records silently
- **C.** Spin up 50 parallel threads under one single user account → Retry HTTP 429 errors immediately with 0 ms delay → Replace filtered queries with full `SELECT *` scans → Open a ticket asking Microsoft to disable platform limits permanently
- **D.** Pinpoint throttled callers in Dataverse API analytics → Batch writes via `CreateMultiple` / `$batch` & use Change Tracking → Pool high-volume S2S loads across Entra Application Users → Honor HTTP `429` `Retry-After` backoff

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Inspecting Dataverse API analytics, batching via `CreateMultiple`/`$batch` with Change Tracking, pooling S2S Application Users where appropriate, and honoring `HTTP 429` `Retry-After` headers eliminates Service Protection throttling cleanly. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Heavy metadata calls and chained synchronous updates multiply execution time against the 20-minute per-5-minute sliding window limit.
- **B:** Incorrect. Service Protection limits protect real-time platform stability per user/web server over 5-minute windows regardless of license SKU.
- **C:** Incorrect. Immediate zero-delay retries under a single user identity amplify `HTTP 429` throttling and extend penalty windows.
- **D:** Correct. Resolving Service Protection (`6,000` req / `20` min compute per 5-min window) combines batch/bulk operations, Change Tracking, pooled S2S Application Users where appropriate, and honoring `Retry-After` backoff.

</details>

### Q059 (`E1Q050`) — Architect a solution [2.2] · *Single-Answer Multiple Choice*

Traders require a virtualized 10,000-row real-time keyboard-navigable matrix with sub-row sparklines bound directly to a Model-driven view dataset. Which customization approach fits best?

- **A.** Validating interactive UX prototypes (`Figma-to-App` / `Custom Pages`) early and building `PCF` controls for specialized UI gaps
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A React virtual Power Apps Component Framework (`PCF`) dataset control renders high-density interactive grids bound natively to Dataverse view paging and security. [Skill 2.2: Identify app customization approaches and validate interactive user experience prototypes | Source: Select customization approaches for existing apps and validate UX prototypes (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/design-consistency)]

- **A:** Correct. Interactive prototyping validates user journeys cheaply, while Power Apps Component Framework (`PCF`) renders reusable custom TypeScript/React controls.
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q060 (`E1Q035`) — Perform solution envisioning and requirement analysis [1.14] · *Single-Answer Multiple Choice*

A legacy mortgage process prints a loan packet three times so three desks in the same building can wet-sign a paper cover sheet. Proposed solution: Harmonize and simplify the workflow into a single standardized digital Dataverse approval flow before building screens. Does this follow future-state optimization best practices?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **C.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — simplifying and standardizing fragmented paper loops into a streamlined digital future-state process before automating eliminates waste and maximizes adoption. [Skill 1.14: Guide future-state business process optimization and standardization before automating | Source: Guide future-state business process optimization and standardization (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **C:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q061 (`E1Q008`) — Perform solution envisioning and requirement analysis [1.3] · *Single-Answer Multiple Choice*

A quantitative risk team runs Monte Carlo portfolio simulations in C++ taking 9 minutes of CPU compute across 32 cores whenever a Dataverse margin call triggers. Because Dataverse sandbox plug-ins enforce a strict 2-minute execution cap, you should offload compute to `____`.

- **A.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **B.** Azure pro-code extension (`Azure Functions`, `Service Bus`, `AKS`, or `Azure AI Foundry`) integrated with Power Platform
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Dataverse sandbox plug-ins enforce a 2-minute timeout; CPU-intensive multi-minute quantitative compute must offload to Azure pro-code services (`Azure Functions` Premium / `AKS`) invoked asynchronously. [Skill 1.3: Identify and select components from existing apps, Dynamics 365, AppSource ISVs, and Azure | Source: Evaluate Dynamics 365 apps, AppSource ISVs, and Azure extensions (https://learn.microsoft.com/en-us/training/modules/discover-customer-needs/)]

- **A:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **B:** Correct. Heavy compute, long-running algorithms (> 2 minutes), and high-throughput brokered messaging offload cleanly to Azure extensions.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q062 (`E1Q043`) — Perform solution envisioning and requirement analysis [1.17] · *Multi-Select (Select 2)*

During fit/gap workshops, underwriters need a multi-table wizard dialog embedded inside a Model-driven app plus a reusable server-side calculation callable from both Canvas apps and external portals. Which two supported low-code/pro-code extensibility options close these gaps cleanly? Select two.

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **C.** Defining solution-aware Dataverse `Custom APIs` exposing strongly typed request/response contracts for internal and external callers
- **D.** Addressing gaps via supported extensibility (`Custom Pages`, `PCF`, `Power Fx Formula columns`, `Custom APIs`) over bespoke clones
- **E.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, D` (`CSV: 3,4`)

Correct answers: C and D (are correct). Embedded `Custom Pages` / `PCF` / `Power Fx` extensions (`gap_lowcode_alt`) handle multi-table responsive dialogs inside Model-driven apps, while Dataverse `Custom APIs` (`integ_custom_api`) expose strongly typed reusable server-side operations. [Skill 1.17: Address functional gaps through supported low-code/pro-code alternate solutions | Source: Address functional gaps through low-code/pro-code alternate solutions (https://learn.microsoft.com/en-us/power-platform/well-architected/operational-excellence/overview)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **C:** Correct. Custom APIs replace legacy Custom Process Actions with code-first, solution-aware OData bound/unbound operations and granular privilege checks.
- **D:** Correct. Supported platform extensibility closes UX and logic gaps while preserving Microsoft wave-update compatibility.
- **E:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q063 (`E1Q006`) — Perform solution envisioning and requirement analysis [1.2] · *Single-Answer Multiple Choice*

A corporate bond registrar wants 90,000 external bondholders to log in online with external identities, update tax withholding forms, and view only their own Dataverse holdings. Proposed solution: Deploy a Microsoft Power Pages site configured with `Entra External ID`, `Web Roles`, and `Contact`-scoped `Table Permissions`. Does this meet the architectural goal?

- **A.** Model-driven Power App over Microsoft Dataverse with responsive forms, views, dashboards, & Business Process Flows
- **B.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — external high-volume retail self-service over Dataverse belongs on Microsoft Power Pages secured with `Table Permissions`, `Web Roles`, and `Entra External ID`. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Incorrect. Model-driven apps excel at structured, data-dense back-office case and lifecycle management directly atop Dataverse security.
- **B:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **C:** Correct. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q064 (`E1Q060`) — Architect a solution [2.7] · *Single-Answer Multiple Choice*

To guide relationship managers and compliance officers across five sequential onboarding stages (`Lead -> KYC -> Credit -> Legal -> Funded`) spanning three Dataverse tables with stage-exit gates, you should configure `____`.

- **A.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **B.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A multi-table Business Process Flow (`BPF`, up to 30 stages with conditional branching and stage-gated privileges) guides human lifecycle progressions cleanly across Dataverse tables. [Skill 2.7: Design automation strategies (sync vs async, BPF, Logic Apps) and multi-environment ALM topology | Source: Design automation & multi-environment strategies (CoE Starter Kit & ALM) (https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit)]

- **A:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **B:** Correct. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q065 (`E1Q022`) — Perform solution envisioning and requirement analysis [1.9] · *Ordered Sequence (Multiple Choice)*

A banking conglomerate stores customer KYC profiles in Finacle Core, credit scores in Snowflake, and relationship notes in Lotus Notes. In what order should the Solution Architect evaluate these data sources before designing the Dataverse model?

- **A.** Duplicate 100% of ERP tables into Dataverse nightly → Ignore master-data ownership → Allow dual uncoordinated edits without conflict rules → Cleanse duplicates manually after go-live
- **B.** Expose on-premises SQL Server ports directly to the public internet → Share one SQL `sa` login across Canvas apps → Skip data classification → Disable Dataverse auditing
- **C.** Email daily CSV exports between departments → Let business units invent conflicting customer IDs → Skip deduplication standards → Import dirty spreadsheets straight into Production
- **D.** Inventory candidate enterprise data sources & owners → Classify data sensitivity, residency, & compliance rules → Assess data quality, volume, & latency needs → Decide per entity whether to connect in place or replicate into Dataverse

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Architects first inventory candidate data sources and owners, classify sensitivity/residency rules, assess quality/volume/latency, and then decide per entity whether to query in place or replicate into Dataverse. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Incorrect. Blindly duplicating authoritative ERP tables without master-data ownership or conflict governance causes severe data drift.
- **B:** Incorrect. Exposing raw database ports and sharing `sa` logins violates zero-trust security and bypasses Dataverse governance.
- **C:** Incorrect. Manual CSV emailing without canonical keys or data quality standards corrupts downstream analytics and automations.
- **D:** Correct. Architects identify authoritative systems of record first, classify regulatory sensitivity/residency, evaluate quality/volume/latency, and then choose virtual in-place access vs Dataverse replication.

</details>

### Q066 (`E1Q091`) — Implement the solution [3.4] · *Multi-Select (Select 2)*

Two bi-directional Dataverse-to-ERP flows entered an infinite update loop that also pushed Dataverse `Log` and `Database` storage capacity to 99%, blocking sandbox refresh operations. Which two architectural actions resolve both the automation conflict and the capacity crisis? Select two.

- **A.** Governing `Database`, `File`, & `Log` storage pools via `Dataverse Long Term Retention`, `Fabric/Synapse Link` archival, & attachment offloading
- **B.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Resolving automation/integration conflicts via `Select columns` (`filteringattributes`), `Trigger Conditions`, plug-in `Depth` checks, & `ETag` (`If-Match`) optimistic concurrency
- **E.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Adding `Select columns` (`filteringattributes`), `Trigger Conditions`, service-account exclusions, and `ETag` optimistic concurrency (`res_conflict_loops`) halts ping-pong loops, while governing `Database`/`File`/`Log` pools via Long Term Retention and Fabric archival (`cap_storage_tiering`) unblocks environment admin operations. [Skill 3.4: Assess storage/resource impact and resolve automation loops, race conditions, & integration conflicts | Source: Assess storage/resource impact and resolve automation & integration conflicts (https://learn.microsoft.com/en-us/power-platform/admin/capacity-storage)]

- **A:** Correct. Keeping relational `Database` capacity lean prevents tenant admin lockouts (`Copy`/`Restore` blocks) and controls storage overage costs.
- **B:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Correct. Column filters, actor exclusions, and `If-Match` row-version headers eliminate infinite ping-pong loops and silent lost-update race conditions.
- **E:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

## Case Study Vignette — Monarch Clearing Services

> Monarch Clearing Services integrates Dataverse trade exceptions with an Azure-hosted risk engine inside a private Azure VNet with zero public endpoints. Currently, a synchronous C# plug-in calls an external credit API that occasionally stalls for 45 seconds, exhausting SQL locks and failing the 2-minute sandbox boundary.

### Q067 (`E1Q070`) — Architect a solution [2.12] · *Single-Answer Multiple Choice*

Case study — Monarch Clearing Services: Monarch Clearing Services must eliminate SQL lock timeouts caused by its synchronous C# plug-in stalling for 45 seconds on an external credit API while guaranteeing zero lost trade-exception checks. Which refactoring pattern should you prescribe?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Replacing the synchronous outbound HTTP call inside the SQL transaction with an asynchronous Dataverse `Service Endpoint` -> `Azure Service Bus` queue + background worker updating the credit status asynchronously eliminates SQL lock contention and 2-minute sandbox failures. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q068 (`E1Q074`) — Architect a solution [2.14] · *Single-Answer Multiple Choice*

Case study — Monarch Clearing Services: Monarch Clearing Services hosts its Azure risk engine inside a private Azure VNet (`10.40.0.0/16`) with public network access disabled and refuses to manage Windows VM gateway clusters. Which networking capability lets Dataverse plug-ins and Power Platform connectors call the private endpoint privately?

- **A.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources
- **B.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **C.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enabling **`Virtual Network (VNet) support for Power Platform`** (`Microsoft.PowerPlatform/enterprisePolicies` subnet delegation) injects outbound Dataverse plug-in and connector traffic directly into the private VNet without On-Premises Data Gateway VMs. [Skill 2.14: Assess VNet subnet delegation, Azure ExpressRoute nuances, Data Gateways, and IP firewall networking | Source: Assess VNet integration, Azure ExpressRoute, gateways, and IP firewall networking (https://learn.microsoft.com/en-us/power-platform/admin/vnet-support-overview)]

- **A:** Correct. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.
- **B:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **C:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **D:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.

</details>

### Q069 (`E1Q093`) — Implement the solution [3.5] · *Single-Answer Multiple Choice*

Case study — Monarch Clearing Services: After refactoring its synchronous plug-in, Monarch Clearing Services notices traders typing `*7741` into a Model-driven Quick Find box wait 19 seconds across 8 million trade exceptions, while a companion Canvas screen fires 200 serial `LookUp` calls inside a gallery. How should you remediate both bottlenecks?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Fixing slowness via delegable `Filter`/`StartsWith` Canvas queries, indexed `Quick Find` columns (no leading `*` wildcards), & async plug-in refactoring
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Eliminating leading-wildcard (`*term`) searches in favor of indexed `StartsWith` Quick Find columns / Dataverse Search, and replacing `N+1` Canvas gallery `LookUp`s with delegable `Filter` views or pre-joined Dataverse views restores sub-second responsiveness. [Skill 3.5: Identify and resolve Canvas, Model-driven, Quick Find index, and synchronous plug-in performance issues | Source: Identify and resolve Canvas, Model-driven, Dataverse, & plug-in performance issues (https://learn.microsoft.com/en-us/power-platform/well-architected/performance-efficiency/overview)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Correct. Eliminating `N+1` gallery `LookUp`s, non-delegable predicates, leading-wildcard full table scans, and chained sync plug-ins restores sub-second UX.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q070 (`E1Q095`) — Implement the solution [3.6] · *Ordered Sequence (Multiple Choice)*

Your global banking program cuts over to Production this Saturday night with 5,000 users, Managed Solution upgrades, and a final 180,000-row delta migration. Which four-step cutover sequence prevents user data collisions and validates launch readiness?

- **A.** Ignore Dataverse Database/File storage overages blocking admin ops → Skip Solution Checker critical findings → Leave Dev URLs in Environment Variables → Disband support team at launch minute
- **B.** Allow 5,000 users to edit records during live schema upgrade and migration → Import Unmanaged solutions into Production → Skip smoke tests → Turn on auditing two months later
- **C.** Freeze changes & verify backup restore point → Enable Dataverse `Administration mode` (blocking regular users & async jobs) → Apply Managed Upgrades & run validated delta loads → Exit `Administration mode`, smoke-test, & monitor hypercare
- **D.** Delete existing Managed Solutions in Production (erasing live tables!) → Re-import from scratch → Manually re-type Connection References & Environment Variables → Disable backups

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Freezing changes and taking a restore point, enabling Dataverse `Administration mode` (blocking regular logins and async jobs), applying Managed Upgrades + delta loads, and exiting `Administration mode` after smoke tests ensures a clean launch. [Skill 3.6: Escalate and resolve data migration bottlenecks (BypassCustomPluginExecution, delta loads, reconciliation) | Source: Escalate and remediate enterprise data migration bottlenecks and cutover issues (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/TVF-override-plugin-execution)]

- **A:** Incorrect. Exceeded Dataverse storage entitlements block environment copy/restore/admin operations and sabotage cutover readiness.
- **B:** Incorrect. Concurrent user edits during cutover cause migration collisions, lock timeouts, and inconsistent business state.
- **C:** Correct. Controlled cutovers establish restore points, engage `Administration mode` to prevent user writes and background noise, apply Managed Upgrades + delta loads, validate smoke tests, and transition to monitored hypercare.
- **D:** Incorrect. Deleting a Managed Solution erases its custom Dataverse tables and production data; always use Managed `Stage for upgrade` -> `Apply upgrade`.

</details>

### Q071 (`E1Q094`) — Implement the solution [3.5] · *Single-Answer Multiple Choice*

During pre-launch load testing in UAT, 1,500 simulated users experience intermittent 8-second spikes on a Custom Page, and architects need KQL correlation across client `pageViews` and Dataverse `dependencies`. Which telemetry integration provides end-to-end diagnostics?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Running scale tests in UAT while streaming Dataverse and Canvas telemetry to `Azure Application Insights` (`dependencies` / `exceptions` KQL)
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Linking both the Dataverse environment and Canvas/Custom Pages to **Azure Application Insights** streams correlated `pageViews`, `requests`, `dependencies`, and `exceptions` telemetry queryable via KQL during scale tests. [Skill 3.5: Identify and resolve Canvas, Model-driven, Quick Find index, and synchronous plug-in performance issues | Source: Identify and resolve Canvas, Model-driven, Dataverse, & plug-in performance issues (https://learn.microsoft.com/en-us/power-platform/well-architected/performance-efficiency/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Correct. Application Insights integration captures page-load latency, plug-in execution durations, and outbound dependency failures under realistic concurrency.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q072 (`E1Q063`) — Architect a solution [2.9] · *Single-Answer Multiple Choice*

Compliance officers inside a Model-driven app need read-only lookup and view access to 45 million archival SWIFT wire confirmations hosted in Azure SQL without consuming Dataverse Database storage or needing offline access. Which pattern fits best?

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **C.** Replicating data into native Dataverse tables (`Dataflows` / `ADF`) when Mobile Offline, row-level security roles, auditing, or SLAs are required
- **D.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Dataverse `Virtual Tables` (`Virtual Connector Provider` for SQL Server or custom OData v4 provider) query external rows in place with zero Dataverse Database duplication. [Skill 2.9: Determine when to connect external data in place (Virtual tables) versus import/replicate into Dataverse | Source: Connect external data in place (Virtual tables) vs import/replicate into Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-virtual-entities)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **C:** Incorrect. Virtual tables do not support Mobile Offline sync, Dataverse row-level User/Team ownership, or native column auditing.
- **D:** Correct. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.

</details>

### Q073 (`E1Q040`) — Perform solution envisioning and requirement analysis [1.16] · *Multi-Select (Select 2)*

A retail bank wants SLA-driven dispute `Case` (`incident`) routing, entitlement tracking, omnichannel skills-based queues, and legally binding EU eIDAS qualified digital signatures. Which two recommendations should the Solution Architect make? Select two.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **C.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **E.** Dynamics 365 first-party app (`Sales`, `Customer Service`, or `Field Service`) leveraging native schemas, SLAs, & RSO scheduling

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). Adopting Dynamics 365 Customer Service (`Case`/`Entitlement`/omnichannel routing) paired with a certified AppSource eIDAS e-signature ISV solution avoids cloning restricted tables or building bespoke cryptography. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **C:** Correct. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **E:** Correct. Adopting Dynamics 365 first-party apps avoids reinventing complex case routing, omnichannel queues, or Resource Scheduling Optimization.

</details>

### Q074 (`E1Q042`) — Perform solution envisioning and requirement analysis [1.16] · *Single-Answer Multiple Choice*

Rather than building custom `bank_customcase`, `bank_customsla`, and `bank_customqueue` tables from scratch to avoid Dynamics 365 licensing, what should the Solution Architect recommend when `> 80%` of dispute routing matches standard service capabilities?

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Dynamics 365 first-party app (`Sales`, `Customer Service`, or `Field Service`) leveraging native schemas, SLAs, & RSO scheduling
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Adopting Dynamics 365 Customer Service leverages native SLA timers, omnichannel routing, and Microsoft wave updates while avoiding restricted-table compliance violations. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Correct. Adopting Dynamics 365 first-party apps avoids reinventing complex case routing, omnichannel queues, or Resource Scheduling Optimization.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q075 (`E1Q055`) — Architect a solution [2.5] · *Ordered Sequence (Multiple Choice)*

A leasing company must migrate 3.5 million Accounts, Contacts, Leases, and circular Primary-Contact/Parent-Lease lookups into Dataverse without firing customer emails or creating random reference-table GUIDs across environments. Which four-step migration sequence should you architect?

- **A.** Execute `INSERT INTO account` over Dataverse TDS port 5558 → Remove platform SQL foreign keys → Copy `.mdf` database files from Azure SQL → Reboot the tenant
- **B.** Cleanse & stage data with Alternate Keys / CMT GUIDs → Suppress non-essential flows & custom plug-ins → Load parent tables first (deferring circular lookups) → Bind deferred lookups, reconcile counts, & re-enable automations
- **C.** Let each environment generate random GUIDs for reference/configuration tables → Hardcode Dev GUIDs inside cloud flows → Import raw unvalidated CSVs → Skip reconciliation
- **D.** Load child line-items before parent Account rows exist → Leave all welcome-email cloud flows enabled → Run single-row serial inserts with no batching → Fix orphaned lookups manually in Prod

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Staging cleansed data with Alternate Keys and CMT fixed GUIDs, suppressing flows/custom plug-ins, loading parents first while deferring circular lookups, and binding deferred lookups before reconciling counts ensures clean cutover. [Skill 2.5: Design enterprise data migration strategies, load sequencing, Alternate Keys, and CMT tooling | Source: Design enterprise data migration strategies, load order, and tooling (https://learn.microsoft.com/en-us/power-platform/admin/create-schema-export-data)]

- **A:** Incorrect. Dataverse’s TDS endpoint (`5558`) is strictly read-only; all writes must use Dataverse Web API/SDK, Dataflows, ADF, or Configuration Migration Tool.
- **B:** Correct. Enterprise migrations stage cleansed data, suppress noisy automations (`BypassCustomPluginExecution`), load parents before children while resolving circular lookups in a second pass, and reconcile counts before re-enabling flows.
- **C:** Incorrect. Mismatched reference-data GUIDs across Dev, UAT, and Prod break business rules, views, and workflow conditions.
- **D:** Incorrect. Loading child rows first fails referential integrity, and leaving notification flows active spams thousands of customers.

</details>

### Q076 (`E1Q085`) — Implement the solution [3.1] · *Single-Answer Multiple Choice*

During detailed design review, a developer’s C# plug-in calls `RetrieveMultiple` without `<top>` paging or column filtering inside a `Pre-Operation` step. Which automated tool surfaces rule `il-specify-column` so the build fails automatically?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Enforcing `Solution Checker` and `App Checker` gates in CI/CD pipelines alongside `Power Platform Well-Architected` design reviews
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Power Platform **Solution Checker** (`pac solution check` / build task) flags unbounded `ColumnSet(true)` (`il-specify-column`) and synchronous plug-in anti-patterns as actionable SARIF build findings. [Skill 3.1: Evaluate detailed designs and implementations with Solution Checker, App Checker, & Well-Architected | Source: Evaluate detailed designs with Solution Checker, App Checker, & Well-Architected (https://learn.microsoft.com/en-us/power-platform/alm/use-powershell-cmdlets-solution-checker)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Correct. Solution Checker flags unbounded queries and sync plug-in anti-patterns, while App Checker catches delegation warnings and WCAG errors before release.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q077 (`E1Q052`) — Architect a solution [2.3] · *Single-Answer Multiple Choice*

To illustrate synchronous vs asynchronous message timing, OAuth token exchange, and error compensation across Power Pages, Dataverse, APIM, and Finacle Core, the Solution Architect should publish a `____` diagram.

- **A.** Reusing `Component Libraries`, `PCF`, `Child Flows`, & `Custom Connectors`, documented via `ERD`, `Sequence`, & `Context` diagrams
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). UML `Sequence` diagrams communicate chronological request/response hops, async Service Bus handoffs, and retry boundaries clearly across integration teams, complementing `ERD` and `Context` diagrams. [Skill 2.3: Maximize component reuse (PCF, Component Libraries, Child Flows) and communicate designs visually | Source: Maximize component reuse (PCF, Component Libraries, Child Flows) & visual diagrams (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)]

- **A:** Correct. Shared component catalogs eliminate duplicate maintenance, while visual architecture diagrams align technical and business stakeholders.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q078 (`E1Q038`) — Perform solution envisioning and requirement analysis [1.15] · *Single-Answer Multiple Choice*

During fit/gap workshops, 74% of requirements match native Dataverse forms/views, 16% need Power Fx formula columns and cloud flows, 6% match a qualified e-signature ISV, and 4% need a custom C# tax-lot engine. Scoring TCO and upgrade risk across these four buckets produces a `____`.

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Structured Fit/Gap matrix scoring requirements across `Out-of-the-Box`, `Configuration`, `AppSource ISV`, & `Custom Code`
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A formal Fit/Gap matrix categorizing requirements across Out-of-the-Box, Configuration, AppSource ISV, and Custom Code gives leadership transparent TCO and wave-upgrade governance. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Formal fit/gap scoring exposes customization TCO, licensing impacts, and upgrade maintenance trade-offs transparently.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q079 (`E1Q065`) — Architect a solution [2.10] · *Multi-Select (Select 2)*

A digital payment processor ingests 25,000 ephemeral fraud-telemetry JSON pings per minute (auto-expiring after 30 days) and also stores 15 MB signed mortgage deeds while requiring BU-level security on `Loan` records. Which two data-modeling decisions are critical? Select two.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **C.** Dataverse `Elastic tables` (Cosmos DB horizontal partitioning + `TTL`) for high-velocity telemetry, and `File`/SharePoint/Blob offloading for binaries
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **E.** Choosing `User or Team` table ownership for BU/row/team security vs `Organization` ownership for global config tables at creation time

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). `Elastic tables` (`TTL` + Cosmos DB horizontal partitioning) plus `File`/Blob binary offloading (`tbl_elastic_activity`) handle high-velocity JSON and 15 MB deeds, while choosing `User or Team` ownership at creation time (`tbl_ownership_choice`) is irrevocable for BU security. [Skill 2.10: Design complex data models (ownership immutability, Elastic/Activity tables, binary storage offloading) | Source: Design complex data models (ownership, Elastic/Activity tables, storage capacity) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/elastic-tables)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **C:** Correct. Elastic tables ingest tens of thousands of ephemeral JSON/IoT writes per minute with automatic `TTL` expiry without relational index contention.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **E:** Correct. Table ownership (`User/Team` vs `Organization`) is immutable once created and determines whether BU, Team, and Hierarchy security apply.

</details>

### Q080 (`E1Q057`) — Architect a solution [2.6] · *Single-Answer Multiple Choice*

Branch supervisors want real-time interactive drill-down charts on open KYC cases directly inside their Model-driven workspace, automatically honoring each supervisor’s Dataverse Business Unit and Team security with zero extra BI licenses. Which visualization option should you select?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Native Dataverse system charts and interactive experience dashboards render live transactional rows while enforcing Dataverse row and column security automatically. [Skill 2.6: Design data visualization strategies across Dataverse charts, Power BI RLS, and Fabric/Synapse Link | Source: Design data visualization (Dataverse charts, Power BI RLS, Fabric/Synapse Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-synapse)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Incorrect. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.
- **C:** Correct. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.

</details>

### Q081 (`E1Q059`) — Architect a solution [2.7] · *Multi-Select (Select 2)*

A clearing bank must (1) block saving a Wire Transfer row synchronously if the beneficiary country is sanctioned, and (2) orchestrate multi-day asynchronous SWIFT `ISO 20022` B2B EDI confirmations inside a VNet-isolated Azure resource group deployed via Bicep. Which two automation choices fit best? Select two.

- **A.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Azure Logic Apps (Standard) for enterprise B2B EDI (`X12`/`AS2`/`EDIFACT`), VNet-isolated single-tenant workflows, & Azure Bicep ALM
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **E.** Synchronous Dataverse plug-ins (`<= 2m`) strictly for atomic transaction validation/rollback; Cloud Flows / Logic Apps for async orchestration

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). A fast synchronous `Pre-Validation`/`Pre-Operation` Dataverse plug-in enforces atomic transaction rollback on sanctioned countries (`auto_sync_vs_async`), while `Azure Logic Apps (Standard)` handles VNet-isolated B2B/EDI orchestrations under Azure Bicep ALM (`auto_logic_apps`). [Skill 2.7: Design automation strategies (sync vs async, BPF, Logic Apps) and multi-environment ALM topology | Source: Design automation & multi-environment strategies (CoE Starter Kit & ALM) (https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit)]

- **A:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Logic Apps Standard complements Power Automate when Azure RBAC, private VNet compute, or B2B Enterprise Integration Pack codecs are required.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **E:** Correct. Keeping synchronous transaction pipelines fast and offloading external orchestrations asynchronously protects Dataverse SQL responsiveness.

</details>

### Q082 (`E1Q046`) — Perform solution envisioning and requirement analysis [1.18] · *Single-Answer Multiple Choice*

To deliver core KYC onboarding within a regulatory 4-month deadline while deferring optional secondary-market analytics to Wave 2, the Solution Architect defines a `____` backlog using MoSCoW prioritization.

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Scoping a high-value `MVP` Phase 1 release using MoSCoW prioritization and formal change-request governance
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Scoping a high-value `MVP` Phase 1 release via MoSCoW (`Must-have`, `Should-have`, `Could-have`, `Won't-have`) de-risks regulatory deadlines and controls scope creep. [Skill 1.18: Determine MVP vs phased solution scope boundaries and govern scope changes | Source: Determine MVP vs phased solution scope and manage scope boundaries (https://learn.microsoft.com/en-us/training/paths/become-solution-architect/)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Correct. Phased MVP delivery de-risks go-live, delivers early business value, and prevents uncontrolled scope creep.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q083 (`E1Q066`) — Architect a solution [2.10] · *Single-Answer Multiple Choice*

A junior maker proposes creating the `Portfolio` table with `Organization` ownership for MVP and toggling its ownership property to `User or Team` in Release 2 when Frankfurt opens. Why must you block this design immediately?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Choosing `User or Team` table ownership for BU/row/team security vs `Organization` ownership for global config tables at creation time
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Dataverse table ownership (`User or Team` vs `Organization`) is immutable once created; tables that will ever need BU, Team, or Hierarchy row security must be created as `User or Team` from Day 1. [Skill 2.10: Design complex data models (ownership immutability, Elastic/Activity tables, binary storage offloading) | Source: Design complex data models (ownership, Elastic/Activity tables, storage capacity) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/elastic-tables)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Correct. Table ownership (`User/Team` vs `Organization`) is immutable once created and determines whether BU, Team, and Hierarchy security apply.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.

</details>

### Q084 (`E1Q100`) — Implement the solution [3.8] · *Single-Answer Multiple Choice*

Proposed solution: Before signing off Go/No-Go for a 12-country wealth rollout, capture a manual Dataverse Production backup restore point, validate rollback runbooks, and phase go-live starting with a single pilot country wave under Application Insights hypercare. Does this follow Microsoft go-live best practices?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Establishing signed-off `Go / No-Go` readiness gates, manual pre-cutover `Backup` restore points, rollback runbooks, & phased wave rollouts
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes — formal Go/No-Go readiness gates, manual pre-cutover restore points, rehearsed rollback runbooks, and phased regional waves minimize enterprise cutover blast radius. [Skill 3.8: Identify go-live readiness gates, execute Administration mode cutovers, and manage hypercare telemetry | Source: Assess go-live readiness factors, Administration mode, and hypercare remediation (https://learn.microsoft.com/en-us/power-platform/admin/admin-mode)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Correct. Clear Go/No-Go criteria, pre-upgrade backups, and phased pilot waves minimize blast radius during enterprise go-live.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q085 (`E1Q072`) — Architect a solution [2.13] · *Single-Answer Multiple Choice*

When a relationship manager clicks `"Fetch Central Credit Bureau Report"` inside a Canvas app, the downstream internal REST API behind APIM must verify the **signed-in banker’s exact Microsoft Entra user identity** for per-user regulatory audit logging. Which authentication pattern is required?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Designing BCDR around Dataverse point-in-time backups (`28-day` Prod retention, cross-Geo failover limits) and `Hosted RPA` + `Work Queues` for legacy UI
- **D.** Using `OAuth 2.0 On-Behalf-Of (OBO)` to preserve caller identity/audit trails vs `Entra Service Principal (S2S)` / `Managed Identity` for background jobs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Configuring a custom connector with Microsoft Entra ID **`OAuth 2.0 On-Behalf-Of (OBO)`** delegated authentication propagates the caller’s identity token end-to-end, whereas S2S Service Principals run headless background jobs. [Skill 2.13: Design authentication (OBO vs S2S, Managed Identity), BCDR (RPO/RTO, geo-backups), and RPA | Source: Design authentication (OBO vs S2S, Managed Identity), BCDR, and RPA architectures (https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Architects align RPO/RTO to Microsoft’s managed geo-replication SLAs and isolate UI-only legacy integrations behind resilient RPA Work Queues.
- **D:** Correct. OBO propagates the signed-in user’s identity downstream for row-level authorization, whereas S2S/Managed Identity runs headless workloads.

</details>

### Q086 (`E1Q053`) — Architect a solution [2.4] · *Single-Answer Multiple Choice*

A single 95-screen Canvas app serving mobile vault couriers, desktop credit analysts, and external borrowers takes 34 seconds to open and exceeds memory limits on courier phones. Proposed solution: Split capabilities into role- and task-specific apps (offline Canvas app for vault couriers, Model-driven app for credit analysts, Power Pages for external borrowers). Does this resolve the architectural flaw?

- **A.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **D.** Grouping capabilities into role- and task-specific apps (offline Canvas for field crews, Model-driven for back-office, Power Pages for externals)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — decomposing bloated monoliths into persona- and task-focused apps optimizes load performance, offline sync payloads, licensing, and security boundaries. [Skill 2.4: Design apps by grouping required features based on persona, role, task, and offline needs | Source: Design role-based and task-based app experiences across form factors (https://learn.microsoft.com/en-us/power-apps/guidance/planning/app-design)]

- **A:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **D:** Correct. Task-focused apps per persona outperform bloated one-size-fits-all apps in load speed, offline footprint, and usability.

</details>

### Q087 (`E1Q071`) — Architect a solution [2.12] · *Single-Answer Multiple Choice*

An investment bank wants near-real-time bi-directional synchronization of `Customer` and `Vendor` master records between Dynamics 365 Finance (`F&O`) and Microsoft Dataverse alongside ERP `Business Events`. Which native integration capability should you select?

- **A.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Integrating Microsoft Teams (`Adaptive Cards` / embedded apps), Dynamics 365 F&O `Dual-write` + `Business Events`, & `Server-Side Sync`
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Dynamics 365 `Dual-write` provides tightly coupled, near-real-time bi-directional master/transactional synchronization between Finance & Operations apps and Dataverse, complemented by `Business Events`. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Correct. Dual-write provides near-real-time bi-directional Dataverse-to-F&O sync, while Teams Adaptive Cards meet users directly in collaboration channels.
- **D:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.

</details>

### Q088 (`E1Q045`) — Perform solution envisioning and requirement analysis [1.18] · *Multi-Select (Select 2)*

Three weeks before UAT freeze, two business directors request adding an unbudgeted AI wealth-robo-advisor module and 14 non-essential partner feeds to Phase 1. Which two scope-management actions should the Solution Architect take? Select two.

- **A.** Establishing a fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Scoping a high-value `MVP` Phase 1 release using MoSCoW prioritization and formal change-request governance
- **E.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Protecting the `MVP` Phase 1 boundary via MoSCoW prioritization and routing new requests through formal Change Control / Architecture Review Board (`ARB`) governance prevents timeline derailment. [Skill 1.18: Determine MVP vs phased solution scope boundaries and govern scope changes | Source: Determine MVP vs phased solution scope and manage scope boundaries (https://learn.microsoft.com/en-us/training/paths/become-solution-architect/)]

- **A:** Correct. Clear architectural ownership, ARB design gates, and CoE guardrails align business, citizen makers, pro-devs, and InfoSec.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Correct. Phased MVP delivery de-risks go-live, delivers early business value, and prevents uncontrolled scope creep.
- **E:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q089 (`E1Q076`) — Architect a solution [2.15] · *Ordered Sequence (Multiple Choice)*

A global private bank wants zero-touch role provisioning from Microsoft Entra ID, strict regional data isolation per country Business Unit, matrix cross-BU visibility for global UHNW advisors, and lightweight deal-team sharing without `POA` bloat. Which four-step security design sequence should you implement?

- **A.** Store confidential M&A contracts in default SharePoint Document Management folders → Assume SharePoint automatically inherits Dataverse row-level Security Roles & Access Teams → Grant site-wide Read to all employees → Go live
- **B.** Create 400 micro Business Units mirroring every HR cost center → Move users between BUs daily (wiping roles prior to modern settings) → Duplicate 400 identical copies of every Security Role → Audit nothing
- **C.** Model Business Units around isolation boundaries (with Modernized BUs for matrix access) → Author custom least-privilege Security Roles → Bind roles to Entra Security Group Teams → Layer Column Security & Access Team Templates
- **D.** Place all users in one root BU with Organization-level Read/Write/Delete → Clone System Administrator for power users → Hide restricted fields using client-only JavaScript → Share individual records manually

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Modeling BUs around isolation boundaries (with Modernized BUs enabled for matrix roles), authoring custom least-privilege roles, binding roles to Entra Security Group Teams, and using Column Security + Access Team Templates delivers scalable Zero Trust RBAC. [Skill 2.15: Design Business Units, Modernized BUs, Owner Teams, Access Team Templates, & Entra Group Teams | Source: Design Business Units, Modernized BUs, Owner/Access Teams, & Entra Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect. Out-of-the-box SharePoint Document Management does NOT synchronize Dataverse row-level security ACLs to SharePoint folders automatically.
- **B:** Incorrect. Over-fragmenting Business Units for reporting rather than true security boundaries creates massive administrative overhead.
- **C:** Correct. Scalable Dataverse security aligns BUs to isolation boundaries, layers custom least-privilege roles onto Entra Security Group Teams for zero-touch provisioning, and handles exceptions via Access Teams and Column Security.
- **D:** Incorrect. Client-side JavaScript never secures data at the API layer, and manual per-record sharing bloats the PrincipalObjectAccess (`POA`) table.

</details>

## Case Study Vignette — Alderbrook Commercial Leasing

> Alderbrook Commercial Leasing is migrating 4.2 million historical lease, guarantor, and circular parent-child asset rows from Oracle into Dataverse over a 36-hour weekend cutover window. Initial UAT dry runs hit HTTP 429 Service Protection throttling and triggered 4.2M unintended welcome emails from active cloud flows.

### Q090 (`E1Q056`) — Architect a solution [2.5] · *Single-Answer Multiple Choice*

Case study — Alderbrook Commercial Leasing: Alderbrook Commercial Leasing needs Oracle `Lease_Number` upserts without extra GUID pre-lookup queries, plus identical GUIDs for 450 `Fee_Schedule` configuration rows referenced by cloud flows across Dev, UAT, and Prod. Which migration design should you specify?

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Staging cleansed records via `ADF` / `SSIS` using Dataverse `Alternate Keys` (`Upsert`) and `Configuration Migration Tool` for fixed-GUID config rows
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Defining Dataverse `Alternate Keys` on `Lease_Number` enables single-call `Upsert` via `ADF`/KingswaySoft, while the `Configuration Migration Tool (CMT)` preserves exact `Fee_Schedule` GUIDs across environments. [Skill 2.5: Design enterprise data migration strategies, load sequencing, Alternate Keys, and CMT tooling | Source: Design enterprise data migration strategies, load order, and tooling (https://learn.microsoft.com/en-us/power-platform/admin/create-schema-export-data)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Correct. Alternate Keys eliminate GUID pre-lookup round-trips on upserts, while CMT preserves exact reference-record GUIDs across Dev/UAT/Prod.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q091 (`E1Q062`) — Architect a solution [2.8] · *Single-Answer Multiple Choice*

Case study — Alderbrook Commercial Leasing: Each commercial `Lease` can have multiple `Guarantors`, each `Guarantor` backs multiple `Leases`, and underwriters must store `Guarantee_Cap_Amount`, `Effective_Date`, and attach security roles on each link. How should you model this relationship?

- **A.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **B.** Configuring `Custom` / `Referential` cascading (avoiding unintended `Parental` `Cascade All` reparent storms) and manual `N:N` intersect tables
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Native out-of-the-box `N:N` intersect tables cannot hold custom business columns or independent forms; creating a **manual `N:N` intersect table** (`Lease_Guarantor`) with two `1:N` lookups stores `Guarantee_Cap_Amount` and `Effective_Date`. [Skill 2.8: Design Dataverse relationships (1:N, N:N, hierarchical, polymorphic) and cascading behaviors | Source: Design Dataverse relationships (1:N, N:N, hierarchical) & cascading behaviors (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **B:** Correct. Replacing `Parental` cascading on high-volume child tables prevents `POA` sharing storms, and manual `N:N` tables store rich relationship attributes.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.

</details>

### Q092 (`E1Q089`) — Implement the solution [3.3] · *Single-Answer Multiple Choice*

Case study — Alderbrook Commercial Leasing: Alderbrook Commercial Leasing must load 4.2 million rows within 36 hours without hitting Dataverse’s per-user **5-minute sliding window** Service Protection limits (`____` requests or `20 minutes` combined execution time). Which design maximizes throughput safely?

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Conforming to `Dataverse Service Protection` limits (`6,000` req / `20m` compute per `5-min` window), pooling `S2S Application Users`, & honoring `Retry-After`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Dataverse Service Protection caps each user/web server at **`6,000` requests or `20 minutes` (`1,200,000 ms`)** execution time per 5-minute window; pooling parallel **S2S Application Users**, using `CreateMultiple` batches, and honoring `Retry-After` scales cutover throughput safely. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Correct. Service Protection enforces per-user/per-web-server 5-minute sliding caps (`HTTP 429`); pooling S2S Application Users and respecting `Retry-After` maximizes throughput.

</details>

### Q093 (`E1Q009`) — Perform solution envisioning and requirement analysis [1.4] · *Single-Answer Multiple Choice*

During pre-sales discovery for a legacy core-banking replacement, the PMO asks why your data-migration estimate spans 9 weeks instead of 3 days for 8 million customer rows. Which factor set primarily drives enterprise Power Platform migration and integration effort?

- **A.** Estimating migration/integration effort from source data cleanliness, transformations, API throughput windows, & cutover downtime
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enterprise migration effort is driven by legacy source dirtiness/deduplication, complex schema/option-set transformations, historical audit volume, 5-minute API throughput limits, and cutover downtime windows. [Skill 1.4: Identify and estimate data migration and integration efforts, complexity drivers, and alternatives | Source: Estimate migration and integration efforts and alternatives (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Correct. Realistic effort sizing accounts for legacy deduplication, schema mapping, historical volume, 5-minute API limits, and delta cutover rehearsals.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q094 (`E1Q027`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

A branch operations director submits a requirement: `"Put 28 red checkboxes and three pop-up dialogs on the Account tab."` How should the Solution Architect refine this high-level request?

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Refining prescriptive wishes into persona-based `User Stories` (`As a ... I need ... so that ...`) with testable Acceptance Criteria
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Refining UI-prescriptive demands into persona-based `User Stories` (`As a <role>, I need <capability> so that <business value>`) with testable Acceptance Criteria uncovers the underlying compliance need cleanly. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Outcome-oriented User Stories decouple business intent from premature UI assumptions and anchor QA test cases.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q095 (`E1Q004`) — Perform solution envisioning and requirement analysis [1.2] · *Multi-Select (Select 2)*

A commercial bank needs two Power Platform components: (1) a structured back-office credit-underwriting desktop workspace with stage-gated Business Process Flows over Dataverse, and (2) an AI-grounded conversational assistant embedded in Microsoft Teams that answers policy questions and escalates complex cases to live underwriters. Which two components should you recommend? Select two.

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Model-driven Power App over Microsoft Dataverse with responsive forms, views, dashboards, & Business Process Flows
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Microsoft Copilot Studio agent grounded in enterprise knowledge sources, Dataverse actions, & live omnichannel handoff
- **E.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). A Model-driven Power App fits structured back-office underwriting with BPFs over Dataverse, while Microsoft Copilot Studio delivers enterprise-grounded Teams conversational agents with live handoff. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Correct. Model-driven apps excel at structured, data-dense back-office case and lifecycle management directly atop Dataverse security.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Correct. Copilot Studio delivers governed conversational and autonomous agents across Teams, web portals, and customer service channels.
- **E:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.

</details>

### Q096 (`E1Q083`) — Architect a solution [2.17] · *Single-Answer Multiple Choice*

Why should automated CI/CD deployment pipelines and nightly ERP sync jobs authenticate to Dataverse using dedicated **Microsoft Entra ID App Registrations (`Application Users`)** rather than a licensed human admin’s username and password?

- **A.** Using `OAuth 2.0 On-Behalf-Of (OBO)` to preserve caller identity/audit trails vs `Entra Service Principal (S2S)` / `Managed Identity` for background jobs
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Headless `S2S` Application Users (backed by certificates or Managed Identities) never break on human MFA prompts, password expirations, or employee offboarding, and isolate API throughput pools cleanly. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Correct. OBO propagates the signed-in user’s identity downstream for row-level authorization, whereas S2S/Managed Identity runs headless workloads.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q097 (`E1Q096`) — Implement the solution [3.6] · *Single-Answer Multiple Choice*

During UAT cutover rehearsal, loading 4.2 million historical leases triggered 9 custom synchronous/asynchronous roll-up plug-ins and 14 Power Automate flows, stretching a 12-hour load to 78 hours. Passing `____` in migration API requests resolves this safely.

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Accelerating bulk loads with `BypassCustomPluginExecution` (`BypassBusinessLogicExecution`), disabled flows/search indexes, & parallel `CreateMultiple` batches
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Passing `BypassCustomPluginExecution` (`BypassBusinessLogicExecution = CustomSync,CustomAsync` with the `prvBypassCustomBusinessLogic` privilege) and temporarily disabling non-essential cloud flows cuts bulk migration duration dramatically. [Skill 3.6: Escalate and resolve data migration bottlenecks (BypassCustomPluginExecution, delta loads, reconciliation) | Source: Escalate and remediate enterprise data migration bottlenecks and cutover issues (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/TVF-override-plugin-execution)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Correct. Bypassing non-essential custom sync/async logic and disabling cloud flows during cutover prevents throttling and unintended notification storms.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q098 (`E1Q011`) — Perform solution envisioning and requirement analysis [1.5] · *Multi-Select (Select 2)*

An investment operations VP claims loan onboarding takes 4 steps, yet branch staff complain loans stall for 11 days. Which two discovery approaches should the Solution Architect combine to uncover actual current-state bottlenecks and unofficial spreadsheets? Select two.

- **A.** Inventorying departmental Excel macros, Access databases, and shadow-IT workarounds to retire manual data silos
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Power Automate Process Mining & Task Mining paired with cross-functional current-state discovery workshops
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **E.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). Combining Power Automate Process/Task Mining (objective event/desktop telemetry) with shadow-IT spreadsheet/Access inventories uncovers hidden rework loops and undocumented departmental silos. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Correct. Uncovering unofficial spreadsheets and shadow tools during discovery prevents critical edge cases from surfacing post-go-live.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Correct. Combining telemetry-driven Process/Task Mining with SME workshops exposes hidden rework loops and shadow processes objectively.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **E:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q099 (`E1Q026`) — Perform solution envisioning and requirement analysis [1.10] · *Single-Answer Multiple Choice*

Compliance analysts want to use 12 years of historical loan-default rows to train an AI Builder prediction model, but 62% of pre-2019 rows lack outcome labels and verified income fields. What must you define before approving this data use case?

- **A.** Defining pre-cutover data quality standards (deduplication keys, mandatory completeness, referential integrity, & domain mappings)
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enforcing data quality standards (completeness thresholds, canonical domain mappings, and labeled cohort filtering) prevents biased or failing AI Builder training runs. [Skill 1.10: Define use cases and data quality standards for existing data prior to migration or integration | Source: Define use cases and data quality standards for existing data (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Correct. Enforcing cleansing and deduplication gates before migration prevents garbage-in/garbage-out failures in Dataverse.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.

</details>

### Q100 (`E1Q067`) — Architect a solution [2.11] · *Ordered Sequence (Multiple Choice)*

Whenever a `Trade_Settlement` row commits in Dataverse, downstream treasury SAP systems (which undergo nightly 2-hour maintenance blackouts) must receive guaranteed, ordered, retryable delivery without slowing user saves. Which integration sequence should you design?

- **A.** Register a Dataverse Service Endpoint (`Service Bus` / `Event Grid`) → Publish row events asynchronously on commit → Buffer & transform via Azure Functions / Logic Apps with DLQ → Upsert idempotently into ERP via Alternate Keys
- **B.** Embed ERP admin client secrets inside browser JavaScript web resources → Call ERP directly from user browsers bypassing CORS & DLP → Log failed payloads to browser `console.log` → Skip auditing
- **C.** Call slow on-premises ERP SOAP endpoints inside a synchronous Pre-Operation Dataverse plug-in → Hold SQL transaction locks for 90 seconds → Ignore HTTP 429/503 errors → Lose failed payloads permanently
- **D.** Poll all 10 million Dataverse rows every 10 seconds without `modifiedon` or Change Tracking → Overrun 5-minute Service Protection limits → Overwrite newer ERP records blindly → Disable TLS

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Registering a Dataverse Service Endpoint (`Azure Service Bus` / `Event Grid`) to publish events asynchronously on commit, buffering via Azure Functions/Logic Apps with DLQ, and upserting idempotently via Alternate Keys isolates Dataverse from ERP blackouts. [Skill 2.11: Design collaboration (Teams, SharePoint ACL nuances, Exchange) and Dynamics 365 Dual-write integrations | Source: Design Teams, SharePoint, Exchange, and Dynamics 365 (Dual-write) integrations (https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dual-write/dual-write-overview)]

- **A:** Correct. Asynchronous Dataverse Service Endpoints -> Azure Service Bus/Event Grid -> Azure Functions/Logic Apps with Dead-Letter Queues and idempotent Alternate Key upserts decouple Dataverse from ERP latency and outages.
- **B:** Incorrect. Exposing secrets in client-side JavaScript is a critical security vulnerability.
- **C:** Incorrect. Long network calls inside synchronous plug-ins exhaust Dataverse worker threads, lock SQL transactions, and lose messages when endpoints go offline.
- **D:** Incorrect. Full-table polling without Dataverse Change Tracking triggers `HTTP 429` throttling and causes lost-update race conditions.

</details>

