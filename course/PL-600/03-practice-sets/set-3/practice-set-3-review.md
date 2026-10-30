# Microsoft Exam PL-600: Practice Exam 3 — Aerospace Dual-Write ERP, Dealer Portals & Fabric Analytics — Reviewer Study Key

**Theme:** Dynamics 365 F&O Dual-write + ITAR Lockbox, Account-scoped Power Pages + AS/400 RPA, Fabric Link + Power BI RLS, and Canvas delegation  
**Credential:** Microsoft Certified: Power Platform Solution Architect Expert (`One active Associate certification required: Microsoft Certified: Power Platform Functional Consultant Associate (PL-200) OR Microsoft Certified: Power Platform Developer Associate (PL-400)`)  
**Study guide baseline:** September 23, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-600)  
**Lifecycle notice:** Exam PL-600 retired on June 30, 2026; succeeded by `Exam AB-100: Agentic AI Business Solutions Architect (Microsoft Certified: Agentic AI Business Solutions Architect Expert)`.  
**Questions:** `100` (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice percentages do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`E3Q074`) — Architect a solution [2.14] · *Single-Answer Multiple Choice*

Dataverse C# plug-ins need outbound private TCP/HTTPS access to an internal Siemens Teamcenter API hosted on an Azure Private Endpoint (`10.80.4.12`) with public internet access disabled. Configuring `____` enables direct private routing without VM gateways.

- **A.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **D.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). **Virtual Network (`VNet`) support for Power Platform** (`enterprisePolicies` subnet delegation) injects Dataverse plug-in and connector outbound calls directly into your Azure VNet to reach Private Endpoints privately. [Skill 2.14: Assess VNet subnet delegation, Azure ExpressRoute nuances, Data Gateways, and IP firewall networking | Source: Assess VNet integration, Azure ExpressRoute, gateways, and IP firewall networking (https://learn.microsoft.com/en-us/power-platform/admin/vnet-support-overview)]

- **A:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **D:** Correct. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.

</details>

### Q002 (`E3Q070`) — Architect a solution [2.12] · *Single-Answer Multiple Choice*

A defense contractor attaches `ITAR`-controlled CAD specs to Dataverse `Engineering_Change` rows and learns default SharePoint Document Management grants library readers access regardless of Dataverse row security. How should you remediate document storage?

- **A.** Mitigating SharePoint Document Management’s lack of automatic Dataverse ACL sync via Dataverse `File` columns, Azure Blob SAS, or custom ACL sync
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Storing controlled files inside native **Dataverse `File` columns** (backed by Dataverse-managed Azure Blob storage enforcing exact row/column Security Roles and CMK) or custom-secured Azure Blob SAS endpoints eliminates the SharePoint ACL gap. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Correct. Default SharePoint integration never copies Dataverse row permissions to SharePoint folders; confidential files require `File` columns or explicit ACL sync.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.

</details>

### Q003 (`E3Q022`) — Perform solution envisioning and requirement analysis [1.9] · *Ordered Sequence (Multiple Choice)*

A machinery manufacturer holds part masters in Teamcenter PLM, inventory costs in Dynamics 365 F&O, and dealer contacts in legacy SQL. Which four-step sequence should govern data-source evaluation?

- **A.** Expose on-premises SQL Server ports directly to the public internet → Share one SQL `sa` login across Canvas apps → Skip data classification → Disable Dataverse auditing
- **B.** Duplicate 100% of ERP tables into Dataverse nightly → Ignore master-data ownership → Allow dual uncoordinated edits without conflict rules → Cleanse duplicates manually after go-live
- **C.** Email daily CSV exports between departments → Let business units invent conflicting customer IDs → Skip deduplication standards → Import dirty spreadsheets straight into Production
- **D.** Inventory candidate enterprise data sources & owners → Classify data sensitivity, residency, & compliance rules → Assess data quality, volume, & latency needs → Decide per entity whether to connect in place or replicate into Dataverse

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Inventorying candidate sources & owners, classifying ITAR/PII sensitivity & residency, assessing quality/volume/latency, and deciding per entity between virtual in-place queries vs Dataverse replication prevents master-data chaos. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Incorrect. Exposing raw database ports and sharing `sa` logins violates zero-trust security and bypasses Dataverse governance.
- **B:** Incorrect. Blindly duplicating authoritative ERP tables without master-data ownership or conflict governance causes severe data drift.
- **C:** Incorrect. Manual CSV emailing without canonical keys or data quality standards corrupts downstream analytics and automations.
- **D:** Correct. Architects identify authoritative systems of record first, classify regulatory sensitivity/residency, evaluate quality/volume/latency, and then choose virtual in-place access vs Dataverse replication.

</details>

### Q004 (`E3Q055`) — Architect a solution [2.5] · *Ordered Sequence (Multiple Choice)*

An industrial OEM is migrating 5 million serialized `Assets`, `Dealerships`, `Warranties`, and circular `Current_Replacement_Asset` self-lookups into Dataverse over a weekend. Which four-step migration sequence ensures referential integrity and repeatable config GUIDs?

- **A.** Cleanse & stage data with Alternate Keys / CMT GUIDs → Suppress non-essential flows & custom plug-ins → Load parent tables first (deferring circular lookups) → Bind deferred lookups, reconcile counts, & re-enable automations
- **B.** Load child line-items before parent Account rows exist → Leave all welcome-email cloud flows enabled → Run single-row serial inserts with no batching → Fix orphaned lookups manually in Prod
- **C.** Let each environment generate random GUIDs for reference/configuration tables → Hardcode Dev GUIDs inside cloud flows → Import raw unvalidated CSVs → Skip reconciliation
- **D.** Execute `INSERT INTO account` over Dataverse TDS port 5558 → Remove platform SQL foreign keys → Copy `.mdf` database files from Azure SQL → Reboot the tenant

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Staging cleansed rows with Alternate Keys & CMT fixed GUIDs, suppressing flows & custom plug-ins, loading parents first (deferring circular self-lookups), and running a second-pass lookup bind + count reconciliation guarantees clean cutover. [Skill 2.5: Design enterprise data migration strategies, load sequencing, Alternate Keys, and CMT tooling | Source: Design enterprise data migration strategies, load order, and tooling (https://learn.microsoft.com/en-us/power-platform/admin/create-schema-export-data)]

- **A:** Correct. Enterprise migrations stage cleansed data, suppress noisy automations (`BypassCustomPluginExecution`), load parents before children while resolving circular lookups in a second pass, and reconcile counts before re-enabling flows.
- **B:** Incorrect. Loading child rows first fails referential integrity, and leaving notification flows active spams thousands of customers.
- **C:** Incorrect. Mismatched reference-data GUIDs across Dev, UAT, and Prod break business rules, views, and workflow conditions.
- **D:** Incorrect. Dataverse’s TDS endpoint (`5558`) is strictly read-only; all writes must use Dataverse Web API/SDK, Dataflows, ADF, or Configuration Migration Tool.

</details>

### Q005 (`E3Q084`) — Implement the solution [3.1] · *Single-Answer Multiple Choice*

An automated build pipeline runs `pac solution check` on every pull request and blocks promotion when severity `High` rules fire for synchronous plug-in `Thread.Sleep` calls or deprecated XRM client APIs. Which validation gate is executing?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Enforcing `Solution Checker` and `App Checker` gates in CI/CD pipelines alongside `Power Platform Well-Architected` design reviews
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **Power Platform Solution Checker** statically analyzes plug-in IL, custom workflow activities, JavaScript web resources, and SDK message configurations inside CI/CD pipelines. [Skill 3.1: Evaluate detailed designs and implementations with Solution Checker, App Checker, & Well-Architected | Source: Evaluate detailed designs with Solution Checker, App Checker, & Well-Architected (https://learn.microsoft.com/en-us/power-platform/alm/use-powershell-cmdlets-solution-checker)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Correct. Solution Checker flags unbounded queries and sync plug-in anti-patterns, while App Checker catches delegation warnings and WCAG errors before release.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q006 (`E3Q083`) — Architect a solution [2.17] · *Single-Answer Multiple Choice*

Proposed solution: Register dedicated Microsoft Entra ID **App Registrations (`Application Users`)** per integration workload (`SAP-Sync-AppUser`, `PLM-Sync-AppUser`) with least-privilege custom Security Roles instead of sharing one human `System Administrator` login. Should you approve this?

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Using `OAuth 2.0 On-Behalf-Of (OBO)` to preserve caller identity/audit trails vs `Entra Service Principal (S2S)` / `Managed Identity` for background jobs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — dedicated S2S Application Users enforce workload-level least privilege, independent audit attribution, isolated 5-minute Service Protection pools, and immunity to human password/MFA resets. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Correct. OBO propagates the signed-in user’s identity downstream for row-level authorization, whereas S2S/Managed Identity runs headless workloads.

</details>

### Q007 (`E3Q050`) — Architect a solution [2.2] · *Single-Answer Multiple Choice*

Dispatchers require a custom interactive Gantt timeline bound directly to a Model-driven subgrid dataset with sub-second drag-free keyboard rescheduling. Developing a `____` dataset control satisfies this cleanly.

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Validating interactive UX prototypes (`Figma-to-App` / `Custom Pages`) early and building `PCF` controls for specialized UI gaps
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A **Power Apps Component Framework (`PCF`)** dataset control binds natively to Model-driven views/subgrids, honoring paging, filtering, and security roles. [Skill 2.2: Identify app customization approaches and validate interactive user experience prototypes | Source: Select customization approaches for existing apps and validate UX prototypes (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/design-consistency)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Correct. Interactive prototyping validates user journeys cheaply, while Power Apps Component Framework (`PCF`) renders reusable custom TypeScript/React controls.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.

</details>

### Q008 (`E3Q061`) — Architect a solution [2.8] · *Single-Answer Multiple Choice*

An aftermarket `Ticket` can reference either a corporate `Account` OR an individual owner-operator `Contact` in a single lookup column, while `Equipment_Assembly` nests 5 levels deep (`Turbine -> Nacelle -> Gearbox -> Shaft -> Bearing`). Which Dataverse relationship features model both cleanly?

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Modeling self-referential `Hierarchical` (`1:N` `Under` queries) and `Polymorphic` (`Customer` / multi-table) relationships
- **C.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **D.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Dataverse **Polymorphic (`Customer` / multi-table) lookups** link `Account` or `Contact` in one column, while a self-referential `1:N` **Hierarchical** relationship models the 5-level `Equipment_Assembly` tree with `Under` rollup queries. [Skill 2.8: Design Dataverse relationships (1:N, N:N, hierarchical, polymorphic) and cascading behaviors | Source: Design Dataverse relationships (1:N, N:N, hierarchical) & cascading behaviors (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Correct. Hierarchical relationships support native visual hierarchy rollups and `Under` OData operators across parent-child trees.
- **C:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **D:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.

</details>

### Q009 (`E3Q069`) — Architect a solution [2.12] · *Multi-Select (Select 3)*

An enterprise manufacturing integration architecture must govern outbound API policies, buffer bursty freight-carrier events with FIFO ordering and Dead-Letter Queues, and expose clean internal OData operations inside Dataverse. Which three components achieve this? Select three.

- **A.** Using the `Virtual Connector Provider` (`SQL Server`, `SharePoint`, `Fabric`) to expose external tables in Dataverse with low-code setup
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Defining solution-aware Dataverse `Custom APIs` exposing strongly typed request/response contracts for internal and external callers
- **D.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`
- **E.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **F.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C, D` (`CSV: 1,3,4`)

Correct answers: A, C, and D (are correct). `APIM` + `Azure Service Bus` FIFO sessions/DLQ + `Event Grid` (`integ_async_asb_apim`), solution-aware Dataverse `Custom APIs` (`integ_custom_api`), and `Virtual Connector Provider` for live catalog lookups (`integ_virtual_connector`) provide a cohesive integration stack. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Correct. The Virtual Connector Provider creates Virtual Tables over supported connectors without authoring custom C# data-provider plug-ins.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Correct. Custom APIs replace legacy Custom Process Actions with code-first, solution-aware OData bound/unbound operations and granular privilege checks.
- **D:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.
- **E:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **F:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q010 (`E3Q019`) — Perform solution envisioning and requirement analysis [1.8] · *Multi-Select (Select 2)*

An aerospace OEM operates Dynamics 365 F&O, Siemens Teamcenter PLM, two Entra ID tenants, and private factory firewalls. Which two deliverables must anchor enterprise landscape analysis? Select two.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **D.** Designating a single authoritative System of Record per entity with explicit survivorship and conflict-resolution rules
- **E.** Enterprise Architecture Context Diagram mapping systems of record, Entra tenants, hybrid networks, & sync/async SLAs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). An Enterprise Architecture Context Diagram (mapping PLM/ERP/identity/network boundaries and SLAs) plus a Master-Data System-of-Record matrix establish unambiguous architectural ownership. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **D:** Correct. Every master entity (`Customer`, `Item`, `GL Account`) needs one clear authoritative owner to prevent bi-directional data corruption.
- **E:** Correct. Evaluating the enterprise landscape clarifies authoritative boundaries, identity federation, firewall paths, and integration patterns.

</details>

### Q011 (`E3Q002`) — Perform solution envisioning and requirement analysis [1.1] · *Single-Answer Multiple Choice*

Plant-floor quality tablets must query 6 million serialized part records in under 800 milliseconds without hitting delegation truncations or API throttling. Under Microsoft Power Platform Well-Architected, this target maps to the `____` pillar.

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Power Platform Well-Architected `Performance Efficiency` pillar (delegable queries, API throughput budgets, & elastic scaling)
- **C.** Power Platform Well-Architected `Security` pillar (Zero Trust Entra identity, least privilege, DLP, & encryption)
- **D.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The Power Platform Well-Architected `Performance Efficiency` pillar governs delegable queries, indexing, throughput budgeting, and elastic scaling under load. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Correct. Performance Efficiency optimizes response latency and resource utilization via query delegation, indexing, batching, and Elastic/async patterns.
- **C:** Incorrect. The Security pillar protects confidentiality and integrity through Entra Conditional Access, least-privilege roles, DLP endpoint rules, and CMK/Lockbox.
- **D:** Incorrect. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.

</details>

### Q012 (`E3Q003`) — Perform solution envisioning and requirement analysis [1.1] · *Single-Answer Multiple Choice*

An industrial robotics division wants automated PR validation, telemetry-driven alerting, and repeatable multi-stage releases across 11 factories. Which Well-Architected pillar directly addresses these engineering practices?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Power Platform Well-Architected `Performance Efficiency` pillar (delegable queries, API throughput budgets, & elastic scaling)
- **C.** Power Platform Well-Architected `Operational Excellence` pillar (automated ALM pipelines, Application Insights, & CoE)
- **D.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Operational Excellence` governs automated ALM pipelines, Solution Checker gates, Application Insights observability, and Center of Excellence governance. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Performance Efficiency optimizes response latency and resource utilization via query delegation, indexing, batching, and Elastic/async patterns.
- **C:** Correct. Operational Excellence standardizes CI/CD solution pipelines, automated Solution Checker gates, telemetry, and Managed Environment governance.
- **D:** Incorrect. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.

</details>

### Q013 (`E3Q089`) — Implement the solution [3.3] · *Single-Answer Multiple Choice*

A developer wraps `ExecuteMultipleRequest` calls **inside** a synchronous C# Dataverse plug-in step and wonders why Solution Checker and Microsoft docs prohibit nested batch requests inside plug-ins. What should you recommend instead?

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Sizing 24-hour `Power Platform Request (PPR)` capacity and using `CreateMultiple` / `UpdateMultiple` / `$batch` (`ExecuteMultiple` `<= 1,000`)
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Microsoft recommends avoiding `ExecuteMultiple` inside plug-ins/workflow activities due to sandbox timeout/throttling instability; invoke **`CreateMultiple` / `UpdateMultiple`** bulk messages from external client batches (`<= 1,000` operations) instead. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Correct. Bulk messages (`CreateMultiple`/`UpdateMultiple`) and `$batch` cut network round-trips dramatically while keeping daily PPR consumption within entitlements.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q014 (`E3Q067`) — Architect a solution [2.11] · *Ordered Sequence (Multiple Choice)*

Whenever a `Supplier_NonConformance` record commits in Dataverse, three downstream plant MES systems and an archival data hub must receive durable, asynchronous, retryable events without slowing inspector saves. Which four-step integration sequence should you design?

- **A.** Poll all 10 million Dataverse rows every 10 seconds without `modifiedon` or Change Tracking → Overrun 5-minute Service Protection limits → Overwrite newer ERP records blindly → Disable TLS
- **B.** Call slow on-premises ERP SOAP endpoints inside a synchronous Pre-Operation Dataverse plug-in → Hold SQL transaction locks for 90 seconds → Ignore HTTP 429/503 errors → Lose failed payloads permanently
- **C.** Register a Dataverse Service Endpoint (`Service Bus` / `Event Grid`) → Publish row events asynchronously on commit → Buffer & transform via Azure Functions / Logic Apps with DLQ → Upsert idempotently into ERP via Alternate Keys
- **D.** Embed ERP admin client secrets inside browser JavaScript web resources → Call ERP directly from user browsers bypassing CORS & DLP → Log failed payloads to browser `console.log` → Skip auditing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Registering a Dataverse Service Endpoint (`Service Bus` / `Event Grid`) to publish events asynchronously on commit, transforming via Azure Functions / Logic Apps with DLQ, and upserting idempotently via Alternate Keys decouples Dataverse from MES outages. [Skill 2.11: Design collaboration (Teams, SharePoint ACL nuances, Exchange) and Dynamics 365 Dual-write integrations | Source: Design Teams, SharePoint, Exchange, and Dynamics 365 (Dual-write) integrations (https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dual-write/dual-write-overview)]

- **A:** Incorrect. Full-table polling without Dataverse Change Tracking triggers `HTTP 429` throttling and causes lost-update race conditions.
- **B:** Incorrect. Long network calls inside synchronous plug-ins exhaust Dataverse worker threads, lock SQL transactions, and lose messages when endpoints go offline.
- **C:** Correct. Asynchronous Dataverse Service Endpoints -> Azure Service Bus/Event Grid -> Azure Functions/Logic Apps with Dead-Letter Queues and idempotent Alternate Key upserts decouple Dataverse from ERP latency and outages.
- **D:** Incorrect. Exposing secrets in client-side JavaScript is a critical security vulnerability.

</details>

### Q015 (`E3Q026`) — Perform solution envisioning and requirement analysis [1.10] · *Single-Answer Multiple Choice*

Aftermarket planners want AI Builder to predict warranty part failures from historical claim rows, but 55% of legacy claims recorded `"9999-MISC"` as the fault code. What must you address first?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **C.** Defining pre-cutover data quality standards (deduplication keys, mandatory completeness, referential integrity, & domain mappings)
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Validating historical data quality and fault-code completeness is mandatory before committing existing datasets to predictive AI Builder use cases. [Skill 1.10: Define use cases and data quality standards for existing data prior to migration or integration | Source: Define use cases and data quality standards for existing data (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **C:** Correct. Enforcing cleansing and deduplication gates before migration prevents garbage-in/garbage-out failures in Dataverse.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q016 (`E3Q011`) — Perform solution envisioning and requirement analysis [1.5] · *Multi-Select (Select 2)*

Procurement VPs assume supplier onboarding takes 3 days, yet suppliers wait 29 days while buyers email secret macro workbooks across engineering and export-control desks. Which two discovery techniques expose the real current state? Select two.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Inventorying departmental Excel macros, Access databases, and shadow-IT workarounds to retire manual data silos
- **E.** Power Automate Process Mining & Task Mining paired with cross-functional current-state discovery workshops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). Power Automate Process/Task Mining quantifies true step wait times and rework loops from ERP/desktop logs, while shadow-IT discovery surfaces hidden departmental macro workbooks. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Correct. Uncovering unofficial spreadsheets and shadow tools during discovery prevents critical edge cases from surfacing post-go-live.
- **E:** Correct. Combining telemetry-driven Process/Task Mining with SME workshops exposes hidden rework loops and shadow processes objectively.

</details>

## Case Study Vignette — Kinetix Heavy Equipment

> Kinetix Heavy Equipment supports 4,500 independent franchise dealerships submitting warranty claims and ordering parts. Dealership managers must see all claims filed by any technician at their own dealership (`Account` hierarchy) without seeing rival dealers, and legacy AS/400 warranty green screens still lack REST APIs.

### Q017 (`E3Q006`) — Perform solution envisioning and requirement analysis [1.2] · *Single-Answer Multiple Choice*

Case study — Kinetix Heavy Equipment: Kinetix Heavy Equipment needs an external web portal where 4,500 independent franchise dealerships submit warranty claims, upload serial photos, and track part credits stored in Dataverse. Proposed solution: Build a Microsoft Power Pages portal using `Account`-scoped `Table Permissions` and authenticated `Web Roles`. Does this meet the architectural need?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Model-driven Power App over Microsoft Dataverse with responsive forms, views, dashboards, & Business Process Flows
- **C.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Yes — Microsoft Power Pages scales securely to thousands of external partner dealerships accessing Dataverse warranty rows through hierarchical `Account`-scoped `Table Permissions`. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Correct. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Incorrect. Model-driven apps excel at structured, data-dense back-office case and lifecycle management directly atop Dataverse security.
- **C:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q018 (`E3Q073`) — Architect a solution [2.13] · *Single-Answer Multiple Choice*

Case study — Kinetix Heavy Equipment: Kinetix’s 1996 AS/400 warranty-claim green-screen app has zero REST/ODBC APIs and must process 8,000 nightly claims resiliently with automatic item retries, SLA monitoring, and zero physical workstation hardware maintenance. What should you design?

- **A.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Designing BCDR around Dataverse point-in-time backups (`28-day` Prod retention, cross-Geo failover limits) and `Hosted RPA` + `Work Queues` for legacy UI
- **D.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Deploying **Power Automate Hosted RPA** (Microsoft-managed cloud bot VMs) pulling items from **Dataverse Work Queues** automates legacy 5250 terminal screens with item-level retries, Dead-Letter handling, and BCDR resilience. [Skill 2.13: Design authentication (OBO vs S2S, Managed Identity), BCDR (RPO/RTO, geo-backups), and RPA | Source: Design authentication (OBO vs S2S, Managed Identity), BCDR, and RPA architectures (https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments)]

- **A:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Correct. Architects align RPO/RTO to Microsoft’s managed geo-replication SLAs and isolate UI-only legacy integrations behind resilient RPA Work Queues.
- **D:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.

</details>

### Q019 (`E3Q082`) — Architect a solution [2.17] · *Single-Answer Multiple Choice*

Case study — Kinetix Heavy Equipment: On Kinetix’s Power Pages portal, a Service Manager at `Midwest Tractor LLC` (`Account`) must view and approve warranty claims filed by all 18 technicians employed at `Midwest Tractor LLC`, while seeing zero claims from `Pacific Equipment Inc.`. Which Power Pages permission scope models this natively?

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Enforcing `DLP` + `Endpoint Filtering`, licensing external consumers via `Power Pages` (`Entra External ID`), & `Entra B2B` for internal-app guests
- **D.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Configuring a Power Pages **`Table Permission` with `Account` access type** (scoped via the authenticated Contact’s parent `Company Name / parentcustomerid` Account relationship) grants dealership-wide isolation without seeing rival dealers. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Correct. Power Pages scales cost-effectively with `Table Permissions` for external portals, whereas Entra B2B suits external partners using internal apps.
- **D:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.

</details>

### Q020 (`E3Q094`) — Implement the solution [3.5] · *Single-Answer Multiple Choice*

During final scale rehearsals for 6,000 plant users, you query `dependencies | where duration > 2000` in KQL to pinpoint slow outbound custom-connector calls from Canvas apps. Which platform integration powers this query?

- **A.** Running scale tests in UAT while streaming Dataverse and Canvas telemetry to `Azure Application Insights` (`dependencies` / `exceptions` KQL)
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Connecting Canvas apps and Dataverse environments to **Azure Application Insights** populates `requests`, `pageViews`, `dependencies`, and `exceptions` tables for KQL root-cause analysis. [Skill 3.5: Identify and resolve Canvas, Model-driven, Quick Find index, and synchronous plug-in performance issues | Source: Identify and resolve Canvas, Model-driven, Dataverse, & plug-in performance issues (https://learn.microsoft.com/en-us/power-platform/well-architected/performance-efficiency/overview)]

- **A:** Correct. Application Insights integration captures page-load latency, plug-in execution durations, and outbound dependency failures under realistic concurrency.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q021 (`E3Q047`) — Architect a solution [2.1] · *Multi-Select (Select 2)*

An aerospace enterprise deploys across `Dev -> QA -> UAT -> Prod` plus sovereign `US` and `EU` regional environments, with three autonomous engineering squads sharing common `Asset` and `Part` tables. Which two architectural patterns should you establish? Select two.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **E.** Dedicated `Dev -> Test -> UAT -> Prod` environments (plus sovereign `Multi-Geo` instances) governed by `Managed Environments` & `CoE Starter Kit`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). Segmented Managed Solutions (`Core Schema` -> `Shared Integrations` -> `App Solutions`) under one custom Publisher prefix (`sol_segmented_alm`) plus multi-tier / `Multi-Geo` **Managed Environments** & **CoE Starter Kit** (`env_multi_tier_coe`) scale enterprise ALM cleanly. [Skill 2.1: Design segmented solution topology, custom Publisher strategy, and Managed Environments | Source: Design solution topology, publisher segmentation, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/alm/segmented-solutions-alm)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **E:** Correct. Multi-tier ALM environments isolate production workloads, Multi-Geo satisfies regional residency, and CoE + Managed Environments automate governance.

</details>

### Q022 (`E3Q087`) — Implement the solution [3.2] · *Single-Answer Multiple Choice*

A maker argues that setting a Business Rule’s scope to `Entity` prevents Power Automate flows owned by low-privilege users from reading restricted columns. Why is that assumption false?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Auditing server-side `Security Roles`, `Column Security`, & `Power Pages Table Permissions` rather than trusting client-side UI rules
- **D.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Entity`-scoped Business Rules run server-side field validations/defaults on create/update, **not** read-access authorization; restricting who can read a column requires a **Column Security Profile** (or table-level **Security Role**). [Skill 3.2: Review security across Business Rules, Security Roles, Entra Conditional Access, & security boundaries | Source: Review end-to-end security across Business Rules, Roles, Entra ID, & boundaries (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Correct. Client JavaScript and `Form`-scoped Business Rules never block Web API/OData access; security boundaries must be enforced server-side in Dataverse.
- **D:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.

</details>

### Q023 (`E3Q096`) — Implement the solution [3.6] · *Single-Answer Multiple Choice*

During Saturday’s 5-million-row `Asset` migration rehearsal, synchronous custom roll-up plug-ins and search indexing slowed throughput to 120 rows/sec. Adding `____` to SDK/Web API requests and disabling non-essential flows accelerates cutover safely.

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Accelerating bulk loads with `BypassCustomPluginExecution` (`BypassBusinessLogicExecution`), disabled flows/search indexes, & parallel `CreateMultiple` batches
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Passing `BypassCustomPluginExecution` (`BypassBusinessLogicExecution = CustomSync,CustomAsync`) skips custom business logic during validated bulk loads while preserving core Microsoft platform integrity. [Skill 3.6: Escalate and resolve data migration bottlenecks (BypassCustomPluginExecution, delta loads, reconciliation) | Source: Escalate and remediate enterprise data migration bottlenecks and cutover issues (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/TVF-override-plugin-execution)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Correct. Bypassing non-essential custom sync/async logic and disabling cloud flows during cutover prevents throttling and unintended notification storms.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q024 (`E3Q048`) — Architect a solution [2.1] · *Single-Answer Multiple Choice*

Why must all delivery squads at an OEM share a single custom **Solution Publisher** (`aero_`) rather than letting each developer use the `Default Publisher` (`cr8a1_` / `new_`)?

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Using a unified custom Publisher (`aero_`) enforces consistent schema naming, enables cross-solution layering/upgrades by the same publisher key, and prevents `Default Publisher` clutter. [Skill 2.1: Design segmented solution topology, custom Publisher strategy, and Managed Environments | Source: Design solution topology, publisher segmentation, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/alm/segmented-solutions-alm)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q025 (`E3Q005`) — Perform solution envisioning and requirement analysis [1.2] · *Single-Answer Multiple Choice*

Wind-farm blade inspectors climbing offshore nacelles 40 km from shore with zero cellular connectivity need custom touch checklists and thermal-photo capture stored locally via a `____`.

- **A.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **B.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Canvas Power App with a `Mobile Offline` profile and device-native camera/barcode UX tailored to frontline tasks

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A Canvas Power App with a `Mobile Offline` profile supports offline-first SQLite Dataverse sync and native device camera integration offshore. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **B:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Correct. Canvas apps give pixel-level task UX and offline-first Dataverse synchronization for field workers operating without connectivity.

</details>

### Q026 (`E3Q066`) — Architect a solution [2.10] · *Single-Answer Multiple Choice*

Global ISO unit-of-measure codes (`KG`, `PSI`, `NM`, `KWH`) are read identically by every user across every Business Unit worldwide and never belong to individual teams. Creating `Unit_Of_Measure` with `____` ownership skips unnecessary `POA`/BU security joins.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Choosing `User or Team` table ownership for BU/row/team security vs `Organization` ownership for global config tables at creation time
- **D.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Global, non-confidential reference tables shared identically across the entire tenant fit **`Organization` ownership** cleanly (chosen permanently at table creation). [Skill 2.10: Design complex data models (ownership immutability, Elastic/Activity tables, binary storage offloading) | Source: Design complex data models (ownership, Elastic/Activity tables, storage capacity) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/elastic-tables)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Correct. Table ownership (`User/Team` vs `Organization`) is immutable once created and determines whether BU, Team, and Hierarchy security apply.
- **D:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.

</details>

### Q027 (`E3Q018`) — Perform solution envisioning and requirement analysis [1.7] · *Single-Answer Multiple Choice*

Tracking mean-time-to-dispatch (`MTTD`), first-time-fix rate (`FTFR` rising from `68%` to `86%`), and SLA breach reduction 90 days post-launch validates `____`.

- **A.** Defining baseline-backed `SMART` success KPIs (cycle-time reduction, error-rate drop, SLA adherence, & active adoption %)
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Measuring operational outcome shifts against pre-project baselines validates agreed architectural key success criteria. [Skill 1.7: Review and validate measurable key success criteria, KPIs, and adoption targets | Source: Review measurable key success criteria, KPIs, and adoption targets (https://learn.microsoft.com/en-us/power-platform/guidance/adoption/measure-business-value)]

- **A:** Correct. Quantifiable KPIs anchored to current-state baselines let stakeholders verify objective ROI after go-live.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q028 (`E3Q001`) — Perform solution envisioning and requirement analysis [1.1] · *Ordered Sequence (Multiple Choice)*

An aircraft avionics manufacturer is kicking off a global supplier-quality transformation on Microsoft Power Platform and wants envisioning structured cleanly into Power Platform Well-Architected alignment. Which four-step sequence should you lead?

- **A.** Copy every legacy Access table 1-for-1 into Dataverse → Replicate broken manual steps verbatim → Ignore API and storage limits → Run fit/gap analysis during user acceptance testing
- **B.** Capture business outcomes, KPIs, & risk constraints → Map current-state processes & existing enterprise systems → Refine functional & non-functional requirements → Align target architecture to Power Platform Well-Architected pillars
- **C.** Grant System Administrator to all stakeholders → Build prototypes in personal My Flows → Skip security & residency discovery → Export Unmanaged Default Solution to Production
- **D.** Write custom C# plug-ins on Day 1 → Purchase all Dynamics 365 licenses blindly → Skip current-state discovery → Capture non-functional requirements after Production go-live

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Capturing measurable quality KPIs and defense-compliance risks first, mapping current supplier processes and ERP systems, refining functional & NFR specs, and aligning trade-offs to Well-Architected pillars prevents costly rework. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Incorrect. Lifting and shifting broken legacy schemas without process optimization or fit/gap analysis perpetuates technical debt.
- **B:** Correct. Solution envisioning establishes measurable business outcomes and risks first, inventories current processes/systems, refines functional & NFR specs, and aligns design trade-offs to Well-Architected pillars.
- **C:** Incorrect. Prototyping in Default Solution with over-privileged accounts violates governance and creates un-deployable artifacts.
- **D:** Incorrect. Coding or buying licenses before discovery and NFR capture causes costly rework and architectural mismatches.

</details>

### Q029 (`E3Q081`) — Architect a solution [2.17] · *Multi-Select (Select 2)*

An industrial OEM wants to: (1) block makers from connecting Dataverse to consumer social-media connectors tenant-wide while restricting the `SQL Server` connector to approved factory FQDN endpoints, and (2) grant 140 external defense quality inspectors guest access to an internal Model-driven `CAPA` app. Which two designs apply? Select two.

- **A.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Enforcing `DLP` + `Endpoint Filtering`, licensing external consumers via `Power Pages` (`Entra External ID`), & `Entra B2B` for internal-app guests
- **D.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **E.** Enforcing `Microsoft Entra Conditional Access` (MFA & compliant device) plus `Power Platform IP Firewall` & `Cookie IP binding`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). Tenant **DLP policies + Connector Endpoint Filtering** plus **Microsoft Entra B2B** guest invitations for the 140 inspectors (`sec_dlp_ext_access`), enforced with **Entra Conditional Access** MFA (`sec_cond_access_ip`), secure both vectors. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Correct. Power Pages scales cost-effectively with `Table Permissions` for external portals, whereas Entra B2B suits external partners using internal apps.
- **D:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **E:** Correct. Combining Entra Conditional Access with Managed Environment IP Firewall and session cookie binding blocks token replay from untrusted networks.

</details>

### Q030 (`E3Q079`) — Architect a solution [2.16] · *Single-Answer Multiple Choice*

Supplier unit-cost margins (`Unit_Cost_Internal`) on the `Part` table must be hidden from general sales engineers across forms, views, OData, Excel exports, and Power BI while remaining editable by Strategic Sourcing leads. Configuring `____` enforces this server-side.

- **A.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **B.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Enabling **Column-level Security** on `Unit_Cost_Internal` and assigning a **`Column Security Profile`** (`Read`/`Update`) solely to the Strategic Sourcing Entra group enforces field protection across every API surface. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **B:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q031 (`E3Q021`) — Perform solution envisioning and requirement analysis [1.8] · *Single-Answer Multiple Choice*

Before promising plant engineers single-sign-on access across Dataverse, Dynamics 365 F&O, and embedded Power BI reports, what must you verify in the enterprise architecture landscape?

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Enterprise Architecture Context Diagram mapping systems of record, Entra tenants, hybrid networks, & sync/async SLAs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Verifying shared **Microsoft Entra ID** tenant alignment (because Dynamics 365 F&O Dual-write and seamless Power BI SSO depend on tenant/identity boundaries) in the landscape map prevents late deployment blockers. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Correct. Evaluating the enterprise landscape clarifies authoritative boundaries, identity federation, firewall paths, and integration patterns.

</details>

### Q032 (`E3Q059`) — Architect a solution [2.7] · *Multi-Select (Select 2)*

An aerospace supply chain solution must: (1) validate synchronously before commit that an `Export_Permit` is active on controlled shipments, and (2) exchange `EDIFACT` ASN messages with logistics carriers inside VNet-isolated Azure workflows. Which two automation technologies should you combine? Select two.

- **A.** Synchronous Dataverse plug-ins (`<= 2m`) strictly for atomic transaction validation/rollback; Cloud Flows / Logic Apps for async orchestration
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Azure Logic Apps (Standard) for enterprise B2B EDI (`X12`/`AS2`/`EDIFACT`), VNet-isolated single-tenant workflows, & Azure Bicep ALM
- **E.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). A fast synchronous Dataverse plug-in enforces atomic export-control transaction validation (`auto_sync_vs_async`), while **Azure Logic Apps (Standard)** processes `EDIFACT` B2B carrier messages inside private VNet compute (`auto_logic_apps`). [Skill 2.7: Design automation strategies (sync vs async, BPF, Logic Apps) and multi-environment ALM topology | Source: Design automation & multi-environment strategies (CoE Starter Kit & ALM) (https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit)]

- **A:** Correct. Keeping synchronous transaction pipelines fast and offloading external orchestrations asynchronously protects Dataverse SQL responsiveness.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Correct. Logic Apps Standard complements Power Automate when Azure RBAC, private VNet compute, or B2B Enterprise Integration Pack codecs are required.
- **E:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q033 (`E3Q051`) — Architect a solution [2.3] · *Single-Answer Multiple Choice*

Eight factory app squads need standardized safety-header bars, barcode-checksum Power Automate logic, and SAP OData wrappers, backed by visual diagrams showing table relationships and async message flows. Which design strategy maximizes reuse?

- **A.** Reusing `Component Libraries`, `PCF`, `Child Flows`, & `Custom Connectors`, documented via `ERD`, `Sequence`, & `Context` diagrams
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Publishing shared `Canvas Component Libraries`, `PCF` controls, `Child Cloud Flows`, and `Custom Connectors` — documented via `ERD`, `Sequence`, and `Context` diagrams — eliminates duplicate code across squads. [Skill 2.3: Maximize component reuse (PCF, Component Libraries, Child Flows) and communicate designs visually | Source: Maximize component reuse (PCF, Component Libraries, Child Flows) & visual diagrams (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)]

- **A:** Correct. Shared component catalogs eliminate duplicate maintenance, while visual architecture diagrams align technical and business stakeholders.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q034 (`E3Q027`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

A plant manager demands: `"Put 19 mandatory text boxes and five approval tabs on the Scrap Ticket screen."` How should the Solution Architect refine this requirement?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Refining prescriptive wishes into persona-based `User Stories` (`As a ... I need ... so that ...`) with testable Acceptance Criteria
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Refining solution-prescriptive demands into persona-driven `User Stories` (`As a Line Supervisor, I need to quarantine defective lots in < 30 seconds so bad parts never ship`) with testable Acceptance Criteria uncovers optimal UX. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Correct. Outcome-oriented User Stories decouple business intent from premature UI assumptions and anchor QA test cases.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q035 (`E3Q037`) — Perform solution envisioning and requirement analysis [1.15] · *Ordered Sequence (Multiple Choice)*

An industrial equipment group submits 195 CRM/Field-Service requirements and asks how to evaluate standard features vs ISVs vs custom C# extensions. Which four-step fit/gap sequence should you apply?

- **A.** Build bespoke React SPAs and C# plug-ins for every requirement first → Replace standard Dynamics 365 tables with custom tables → Ignore AppSource → Check standard features last
- **B.** Inject unsupported DOM-scraping JavaScript into Model-driven forms → Modify SQL indexes directly via TDS → Bypass security roles → Lock out Microsoft updates
- **C.** Accept every stakeholder wish into Phase 1 without feasibility scoring → Skip MVP boundaries → Hardcode workarounds in Production → Defer licensing impact checks until billing
- **D.** Validate each requirement against out-of-the-box Dataverse & Dynamics 365 capabilities → Evaluate declarative low-code configuration → Assess vetted AppSource ISV solutions → Specify targeted pro-code extensions only for remaining gaps

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Checking native Dataverse/Dynamics 365 fit first, then declarative low-code configuration, then vetted AppSource ISVs, and finally targeted pro-code extensions protects TCO and wave-update compatibility. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Defaulting to custom code and duplicating restricted/standard Dynamics 365 tables inflates TCO and breaks product upgrades.
- **B:** Incorrect. Unsupported DOM manipulation and direct SQL writes violate Microsoft supportability contracts and break on wave updates.
- **C:** Incorrect. Unbounded scope acceptance without feasibility or licensing evaluation derails timelines and budgets.
- **D:** Correct. Fit/gap analysis prioritizes standard platform/Dynamics 365 features first, then declarative configuration, then supported AppSource ISVs, reserving custom code strictly for true differentiators.

</details>

### Q036 (`E3Q062`) — Architect a solution [2.8] · *Single-Answer Multiple Choice*

When a regional `Dealership` (`Account`) with 95,000 closed `Warranty_Claim` rows changes Territory Owner, a `Parental` `1:N` relationship triggers a 95,000-row synchronous `Assign` cascade that times out after 2 minutes. Switching relationship behavior to `____` (`Cascade None` or `Cascade Active` on `Assign`) prevents the timeout.

- **A.** Configuring `Custom` / `Referential` cascading (avoiding unintended `Parental` `Cascade All` reparent storms) and manual `N:N` intersect tables
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Configuring `Custom` cascading (`Cascade None` or `Cascade Active` on `Assign`/`Share`/`Reparent`) prevents synchronous mass reassignments across historical closed claims. [Skill 2.8: Design Dataverse relationships (1:N, N:N, hierarchical, polymorphic) and cascading behaviors | Source: Design Dataverse relationships (1:N, N:N, hierarchical) & cascading behaviors (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Correct. Replacing `Parental` cascading on high-volume child tables prevents `POA` sharing storms, and manual `N:N` tables store rich relationship attributes.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.

</details>

### Q037 (`E3Q100`) — Implement the solution [3.8] · *Single-Answer Multiple Choice*

Before authorizing Go-Live for 6,000 plant workers, you verify signed UAT defect gates, capture a manual Production Dataverse backup, rehearse rollback timing, and staff a 14-day Application Insights war room. This governance discipline represents `____`.

- **A.** Establishing signed-off `Go / No-Go` readiness gates, manual pre-cutover `Backup` restore points, rollback runbooks, & phased wave rollouts
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Formal Go/No-Go readiness gates, manual pre-cutover restore points, tested rollback runbooks, and structured hypercare protect mission-critical manufacturing launches. [Skill 3.8: Identify go-live readiness gates, execute Administration mode cutovers, and manage hypercare telemetry | Source: Assess go-live readiness factors, Administration mode, and hypercare remediation (https://learn.microsoft.com/en-us/power-platform/admin/admin-mode)]

- **A:** Correct. Clear Go/No-Go criteria, pre-upgrade backups, and phased pilot waves minimize blast radius during enterprise go-live.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q038 (`E3Q054`) — Architect a solution [2.4] · *Single-Answer Multiple Choice*

Proposed solution: Combine shop-floor barcode scanning, executive M&A financials, HR disciplinary cases, and dealer self-service into one 140-screen Canvas app so IT only maintains a single `.msapp` file. Should you approve this app-grouping design?

- **A.** Grouping capabilities into role- and task-specific apps (offline Canvas for field crews, Model-driven for back-office, Power Pages for externals)
- **B.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). No — monolithic 140-screen multi-persona Canvas apps suffer severe cold-start latency, co-authoring merge conflicts, and over-broad permission surfaces; group features into focused persona/task apps. [Skill 2.4: Design apps by grouping required features based on persona, role, task, and offline needs | Source: Design role-based and task-based app experiences across form factors (https://learn.microsoft.com/en-us/power-apps/guidance/planning/app-design)]

- **A:** Correct. Task-focused apps per persona outperform bloated one-size-fits-all apps in load speed, offline footprint, and usability.
- **B:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q039 (`E3Q065`) — Architect a solution [2.10] · *Multi-Select (Select 2)*

A smart-factory solution ingests 30,000 high-frequency CNC spindle-temperature JSON readings per minute (retained for 7 days) and 40 MB ultrasonic NDT scan files while enforcing plant Business Unit security on `Machine_Center` rows. Which two modeling choices are essential? Select two.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **C.** Dataverse `Elastic tables` (Cosmos DB horizontal partitioning + `TTL`) for high-velocity telemetry, and `File`/SharePoint/Blob offloading for binaries
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **E.** Choosing `User or Team` table ownership for BU/row/team security vs `Organization` ownership for global config tables at creation time

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). Using **Dataverse Elastic tables** (`TTL = 7 days`) for high-velocity CNC JSON bursts plus `File`/Azure Blob offloading for 40 MB NDT scans (`tbl_elastic_activity`), alongside immutable `User or Team` ownership on `Machine_Center` (`tbl_ownership_choice`), keeps relational storage fast and secure. [Skill 2.10: Design complex data models (ownership immutability, Elastic/Activity tables, binary storage offloading) | Source: Design complex data models (ownership, Elastic/Activity tables, storage capacity) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/elastic-tables)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **C:** Correct. Elastic tables ingest tens of thousands of ephemeral JSON/IoT writes per minute with automatic `TTL` expiry without relational index contention.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **E:** Correct. Table ownership (`User/Team` vs `Organization`) is immutable once created and determines whether BU, Team, and Hierarchy security apply.

</details>

### Q040 (`E3Q031`) — Perform solution envisioning and requirement analysis [1.12] · *Single-Answer Multiple Choice*

Aircraft hangar mechanics working inside Faraday-shielded fuselage bays must read job cards, sign off torque values, and log defects offline. Specifying exact offline read/write tables belongs in `____`.

- **A.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **B.** Capturing Functional Requirements (persona workflows, state rules, approvals, offline CRUD scope, & statutory reports)
- **C.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **D.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Defining exact disconnected persona CRUD actions and sync conflict expectations is a core functional requirement for Mobile Offline architecture. [Skill 1.12: Identify functional requirements across personas, business rules, approvals, and offline access | Source: Identify functional requirements across personas, offline, and workflows (https://learn.microsoft.com/en-us/power-apps/mobile/setup-mobile-offline)]

- **A:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **B:** Correct. Functional requirements specify what business behaviors and data transformations the solution must perform for each role.
- **C:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **D:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.

</details>

### Q041 (`E3Q030`) — Perform solution envisioning and requirement analysis [1.12] · *Single-Answer Multiple Choice*

Which requirement belongs in the **Functional Requirements** specification for an aerospace supplier corrective-action (`SCAR`) system?

- **A.** Conforming to `Dataverse Service Protection` limits (`6,000` req / `20m` compute per `5-min` window), pooling `S2S Application Users`, & honoring `Retry-After`
- **B.** Capturing Non-Functional Requirements (`RPO`/`RTO`, peak concurrency, `p95` latency, API volume, `WCAG 2.1 AA`, & retention)
- **C.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources
- **D.** Capturing Functional Requirements (persona workflows, state rules, approvals, offline CRUD scope, & statutory reports)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `8D` root-cause state transitions, supplier containment response deadlines, and QA effectiveness sign-off rules define functional system behavior (`req_functional_spec`). [Skill 1.12: Identify functional requirements across personas, business rules, approvals, and offline access | Source: Identify functional requirements across personas, offline, and workflows (https://learn.microsoft.com/en-us/power-apps/mobile/setup-mobile-offline)]

- **A:** Incorrect. Service Protection enforces per-user/per-web-server 5-minute sliding caps (`HTTP 429`); pooling S2S Application Users and respecting `Retry-After` maximizes throughput.
- **B:** Incorrect. Non-functional requirements govern architectural sizing, BCDR, licensing capacity, offline design, and security controls.
- **C:** Incorrect. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.
- **D:** Correct. Functional requirements specify what business behaviors and data transformations the solution must perform for each role.

</details>

## Case Study Vignette — IronPeak Plant Rollout

> IronPeak Plant Rollout is 72 hours from cutting over 6,000 plant users onto a new Canvas + Model-driven quality suite. Load testing revealed a Canvas gallery taking 28 seconds due to non-delegable `Filter(Search(...))` calls and N+1 `LookUp` formulas per row, plus background jobs interfering with final schema maintenance.

### Q042 (`E3Q053`) — Architect a solution [2.4] · *Single-Answer Multiple Choice*

Case study — IronPeak Plant Rollout: IronPeak has 5,200 line operators wearing nitrile gloves who only log 3-field defect tallies on tablets, 700 quality engineers managing 12-stage `CAPA` root-cause investigations at desks, and 100 external suppliers submitting `8D` responses. How should you group apps?

- **A.** Grouping capabilities into role- and task-specific apps (offline Canvas for field crews, Model-driven for back-office, Power Pages for externals)
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **D.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Splitting into a large-button task Canvas app for gloved line operators, a Model-driven app with BPFs for desktop quality engineers, and Power Pages for external suppliers aligns UX, performance, and licensing per persona. [Skill 2.4: Design apps by grouping required features based on persona, role, task, and offline needs | Source: Design role-based and task-based app experiences across form factors (https://learn.microsoft.com/en-us/power-apps/guidance/planning/app-design)]

- **A:** Correct. Task-focused apps per persona outperform bloated one-size-fits-all apps in load speed, offline footprint, and usability.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **D:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.

</details>

### Q043 (`E3Q093`) — Implement the solution [3.5] · *Single-Answer Multiple Choice*

Case study — IronPeak Plant Rollout: IronPeak’s Canvas quality app takes 28 seconds to render because its gallery uses non-delegable `Filter(Search(Inspections, ...))` and executes an `N+1` `LookUp` per row. Proposed solution: Replace the formula with delegable `StartsWith` / indexed Dataverse views, use `AddColumns`/server views or cached collections for reference lookups, and turn on `Explicit column selection`. Does this fix the 28-second stall?

- **A.** Fixing slowness via delegable `Filter`/`StartsWith` Canvas queries, indexed `Quick Find` columns (no leading `*` wildcards), & async plug-in refactoring
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Yes — delegable `StartsWith`/`Filter` predicates over indexed Dataverse columns, eliminating `N+1` gallery `LookUp`s, and enabling `Explicit column selection` shrink payload and latency to sub-second levels. [Skill 3.5: Identify and resolve Canvas, Model-driven, Quick Find index, and synchronous plug-in performance issues | Source: Identify and resolve Canvas, Model-driven, Dataverse, & plug-in performance issues (https://learn.microsoft.com/en-us/power-platform/well-architected/performance-efficiency/overview)]

- **A:** Correct. Eliminating `N+1` gallery `LookUp`s, non-delegable predicates, leading-wildcard full table scans, and chained sync plug-ins restores sub-second UX.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q044 (`E3Q099`) — Implement the solution [3.8] · *Single-Answer Multiple Choice*

Case study — IronPeak Plant Rollout: IronPeak noticed background asynchronous workflows firing mid-cutover and interfering with final schema maintenance 72 hours before launch. Which environment setting blocks both regular plant logins and background asynchronous operations during cutover?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **D.** Enabling Dataverse `Administration mode` (blocking non-admins & background jobs) during cutover, followed by smoke tests & Application Insights hypercare

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enabling Dataverse **`Administration mode`** with **Background operations disabled** pauses async workflows/flows and restricts interactive logins strictly to System Administrators/Customizers. [Skill 3.8: Identify go-live readiness gates, execute Administration mode cutovers, and manage hypercare telemetry | Source: Assess go-live readiness factors, Administration mode, and hypercare remediation (https://learn.microsoft.com/en-us/power-platform/admin/admin-mode)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **D:** Correct. `Administration mode` guarantees a quiet database during final schema upgrade and delta migration before opening Production to users.

</details>

### Q045 (`E3Q025`) — Perform solution envisioning and requirement analysis [1.10] · *Single-Answer Multiple Choice*

Legacy dealer spreadsheets list `"Caterpillar"`, `"CAT Inc."`, and `"Cat-North"` as separate customer rows with missing ISO country codes and broken parent IDs. Enforcing `____` before cutover prevents duplicate `Account` hierarchies.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Defining pre-cutover data quality standards (deduplication keys, mandatory completeness, referential integrity, & domain mappings)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Pre-migration data quality gates (fuzzy/DUNS deduplication, ISO lookup normalization, and parent-key integrity) ensure clean Dataverse master hierarchies. [Skill 1.10: Define use cases and data quality standards for existing data prior to migration or integration | Source: Define use cases and data quality standards for existing data (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Correct. Enforcing cleansing and deduplication gates before migration prevents garbage-in/garbage-out failures in Dataverse.

</details>

### Q046 (`E3Q044`) — Perform solution envisioning and requirement analysis [1.17] · *Single-Answer Multiple Choice*

Instead of maintaining synchronous C# plug-ins just to concatenate part prefixes and compute `Margin_Percent = (Price - Cost) / Price`, configuring a `____` solves this gap declaratively in Dataverse.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Addressing gaps via supported extensibility (`Custom Pages`, `PCF`, `Power Fx Formula columns`, `Custom APIs`) over bespoke clones
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Dataverse **Power Fx Formula columns** compute arithmetic, string, and related-parent expressions at query time without custom C# plug-in maintenance. [Skill 1.17: Address functional gaps through supported low-code/pro-code alternate solutions | Source: Address functional gaps through low-code/pro-code alternate solutions (https://learn.microsoft.com/en-us/power-platform/well-architected/operational-excellence/overview)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Correct. Supported platform extensibility closes UX and logic gaps while preserving Microsoft wave-update compatibility.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q047 (`E3Q007`) — Perform solution envisioning and requirement analysis [1.3] · *Single-Answer Multiple Choice*

Receiving clerks photograph 25,000 crumpled packing slips per week on loading docks and want automated SKU/quantity extraction inside Power Automate without managing Python GPU servers. Which component should you recommend?

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Azure pro-code extension (`Azure Functions`, `Service Bus`, `AKS`, or `Azure AI Foundry`) integrated with Power Platform
- **C.** AI Builder prebuilt/custom document processing, text classification, & AI Prompts integrated natively in Power Platform
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). AI Builder custom/prebuilt document processing extracts tabular line items from packing-slip images natively inside Power Automate cloud flows. [Skill 1.3: Identify and select components from existing apps, Dynamics 365, AppSource ISVs, and Azure | Source: Evaluate Dynamics 365 apps, AppSource ISVs, and Azure extensions (https://learn.microsoft.com/en-us/training/modules/discover-customer-needs/)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Incorrect. Heavy compute, long-running algorithms (> 2 minutes), and high-throughput brokered messaging offload cleanly to Azure extensions.
- **C:** Correct. AI Builder embeds governed document extraction and generative AI prompts directly inside flows and apps without custom ML infrastructure.
- **D:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.

</details>

### Q048 (`E3Q052`) — Architect a solution [2.3] · *Single-Answer Multiple Choice*

To present executive and security stakeholders with a high-level birds-eye map showing Power Platform, Dynamics 365 F&O, Teamcenter PLM, APIM, and external dealers, you should author a `____`.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Reusing `Component Libraries`, `PCF`, `Child Flows`, & `Custom Connectors`, documented via `ERD`, `Sequence`, & `Context` diagrams
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A **System Context (`C4`) architecture diagram** communicates system boundaries, personas, and external dependencies clearly alongside detailed `ERD` and `Sequence` diagrams. [Skill 2.3: Maximize component reuse (PCF, Component Libraries, Child Flows) and communicate designs visually | Source: Maximize component reuse (PCF, Component Libraries, Child Flows) & visual diagrams (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Correct. Shared component catalogs eliminate duplicate maintenance, while visual architecture diagrams align technical and business stakeholders.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q049 (`E3Q046`) — Perform solution envisioning and requirement analysis [1.18] · *Single-Answer Multiple Choice*

Prioritizing `Must-have` safety recall and warranty-claim flows into Phase 1 while scheduling `Could-have` dealer gamification badges into Phase 2 applies `____`.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Scoping a high-value `MVP` Phase 1 release using MoSCoW prioritization and formal change-request governance

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). MoSCoW-driven `MVP` phasing delivers core business value early and prevents scope creep from jeopardizing critical launches. [Skill 1.18: Determine MVP vs phased solution scope boundaries and govern scope changes | Source: Determine MVP vs phased solution scope and manage scope boundaries (https://learn.microsoft.com/en-us/training/paths/become-solution-architect/)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Correct. Phased MVP delivery de-risks go-live, delivers early business value, and prevents uncontrolled scope creep.

</details>

### Q050 (`E3Q064`) — Architect a solution [2.9] · *Single-Answer Multiple Choice*

Field turbine technicians working offline inside concrete dam powerhouses need local CRUD access, audit history, and BU security on `Active_Work_Orders`. Why must `Active_Work_Orders` be replicated/stored natively in Dataverse rather than surfaced as Virtual Tables?

- **A.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **B.** Replicating data into native Dataverse tables (`Dataflows` / `ADF`) when Mobile Offline, row-level security roles, auditing, or SLAs are required
- **C.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **D.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Native Dataverse tables are required whenever **Mobile Offline** read/write sync, `User/Team` BU security roles, column auditing, or native SLA/BPF capabilities apply. [Skill 2.9: Determine when to connect external data in place (Virtual tables) versus import/replicate into Dataverse | Source: Connect external data in place (Virtual tables) vs import/replicate into Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-virtual-entities)]

- **A:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **B:** Correct. Virtual tables do not support Mobile Offline sync, Dataverse row-level User/Team ownership, or native column auditing.
- **C:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **D:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.

</details>

### Q051 (`E3Q009`) — Perform solution envisioning and requirement analysis [1.4] · *Single-Answer Multiple Choice*

An aerospace conglomerate is consolidating 7 legacy MRP systems containing unstandardized part revisions, 18 million bill-of-material (`BOM`) child links, and a strict 18-hour Thanksgiving plant shutdown window. What drives your migration effort estimate?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Estimating migration/integration effort from source data cleanliness, transformations, API throughput windows, & cutover downtime
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Part-revision deduplication, multi-level `BOM` parent-child dependency ordering, 5-minute API throughput limits, and the 18-hour cutover freeze govern realistic migration sizing. [Skill 1.4: Identify and estimate data migration and integration efforts, complexity drivers, and alternatives | Source: Estimate migration and integration efforts and alternatives (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Correct. Realistic effort sizing accounts for legacy deduplication, schema mapping, historical volume, 5-minute API limits, and delta cutover rehearsals.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q052 (`E3Q080`) — Architect a solution [2.16] · *Single-Answer Multiple Choice*

After years of manual `"Share"` clicks on 6 million `Quote` records, SQL queries against `PrincipalObjectAccess` (`POA`) slow view loads by 9 seconds. Adopting `____` prevents further `POA` growth.

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Preventing `PrincipalObjectAccess (POA)` table bloat by replacing manual per-record sharing and `Parental` cascades with `Access Team Templates`
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Replacing manual user sharing and `Parental` cascades with **Access Team Templates** and **Entra Group Teams** preserves clean `POA` hygiene at enterprise scale. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Correct. Millions of `POA` rows from manual sharing and `Cascade All` relationships degrade SQL query performance across Dataverse views.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.

</details>

### Q053 (`E3Q097`) — Implement the solution [3.7] · *Multi-Select (Select 2)*

Solution `Warranty_Portal v2.4` fails import into UAT because `Asset_Core` references `Warranty_Portal` while `Warranty_Portal` references `Asset_Core`, and a previous unmanaged hotfix sits atop the `Claim` form in Prod. Which two actions resolve both deployment issues? Select two.

- **A.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **E.** Resolving deployment failures by running `Remove active customizations`, refactoring circular solution dependencies into a base layer, & validating stage JSON bindings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E` (`CSV: 1,5`)

Correct answers: A and E (are correct). Refactoring shared tables/lookups into a foundational `Base` layer to break circular dependencies (`sol_segmented_alm`) and running **`Remove active customizations`** on the `Claim` form (`dep_layers_deps`) unblock clean Managed upgrades. [Skill 3.7: Resolve deployment plan issues, Unmanaged Active Solution Layers, and circular solution dependencies | Source: Resolve deployment plan, Solution Layer, and pipeline dependency issues (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **E:** Correct. Stripping Unmanaged Active layers and decoupling circular references ensures repeatable, zero-touch Managed Solution Upgrades.

</details>

### Q054 (`E3Q015`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

An acquired valve factory runs 85 undocumented desktop & cloud flows bound to a retired plant clerk’s personal credentials inside the `Default` environment. How should you remediate this organizational risk?

- **A.** Mitigating single-maker bus-factor risk, unmonitored personal flows, & technical debt via Managed Environments and CoE
- **B.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **C.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Migrating production flows into **Managed Environments** owned by Service Principals / co-owners with DLP policies and CoE Starter Kit inventory monitoring eliminates single-maker continuity risk. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Correct. Unmanaged citizen sprawl and bespoke code without ALM pipelines represent top organizational operational risks.
- **B:** Incorrect. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **C:** Incorrect. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q055 (`E3Q013`) — Perform solution envisioning and requirement analysis [1.5] · *Single-Answer Multiple Choice*

Plant continuous-improvement engineers want to build frontline Canvas apps while central enterprise architects govern SAP connectors and ALM pipelines. Defining `____` clarifies decision authority and review gates.

- **A.** Establishing a fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model align plant makers with central IT security and ALM standards. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Correct. Clear architectural ownership, ARB design gates, and CoE guardrails align business, citizen makers, pro-devs, and InfoSec.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q056 (`E3Q023`) — Perform solution envisioning and requirement analysis [1.9] · *Single-Answer Multiple Choice*

Engineering edits part tolerances in Teamcenter PLM while sales reps accidentally overwrite part descriptions inside Dataverse quotes. Establishing `____` locks Teamcenter as authoritative for engineering specs while Dataverse owns commercial quote notes.

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **C.** Designating a single authoritative System of Record per entity with explicit survivorship and conflict-resolution rules
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Attribute- and entity-level System-of-Record ownership rules prevent downstream transactional apps from corrupting authoritative engineering master data. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **C:** Correct. Every master entity (`Customer`, `Item`, `GL Account`) needs one clear authoritative owner to prevent bi-directional data corruption.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q057 (`E3Q057`) — Architect a solution [2.6] · *Single-Answer Multiple Choice*

Service dispatchers inside a Model-driven app want live multi-stream queue charts (`Open`, `Escalated`, `Breaching SLA`) with instant row filtering and zero additional BI licensing. Which native capability should you select?

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Native Dataverse **interactive experience dashboards** and system charts deliver real-time operational filtering while honoring Dataverse security roles natively. [Skill 2.6: Design data visualization strategies across Dataverse charts, Power BI RLS, and Fabric/Synapse Link | Source: Design data visualization (Dataverse charts, Power BI RLS, Fabric/Synapse Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-synapse)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Correct. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.
- **D:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.

</details>

### Q058 (`E3Q072`) — Architect a solution [2.13] · *Single-Answer Multiple Choice*

An automated nightly BOM-costing job runs at 01:00 with zero signed-in users, whereas an interactive Canvas export-compliance lookup must enforce the signed-in engineer’s security clearance on a downstream API. How should authentication differ across the two workloads?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Using `OAuth 2.0 On-Behalf-Of (OBO)` to preserve caller identity/audit trails vs `Entra Service Principal (S2S)` / `Managed Identity` for background jobs
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). The interactive clearance lookup uses **`OAuth 2.0 On-Behalf-Of (OBO)`** delegated identity to preserve user context, while the headless 01:00 batch job uses a **`Microsoft Entra Service Principal (S2S)`** or **Managed Identity**. [Skill 2.13: Design authentication (OBO vs S2S, Managed Identity), BCDR (RPO/RTO, geo-backups), and RPA | Source: Design authentication (OBO vs S2S, Managed Identity), BCDR, and RPA architectures (https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Correct. OBO propagates the signed-in user’s identity downstream for row-level authorization, whereas S2S/Managed Identity runs headless workloads.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q059 (`E3Q040`) — Perform solution envisioning and requirement analysis [1.16] · *Multi-Select (Select 2)*

An elevator manufacturer needs: (1) technician Preventive Maintenance `Work Orders`, SLA entitlements, IoT Connected Field Service alerts, and automated territory route scheduling (`RSO`), plus (2) a certified global sales-tax calculation engine on quotes. Which two options should you recommend? Select two.

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **C.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **D.** Dynamics 365 first-party app (`Sales`, `Customer Service`, or `Field Service`) leveraging native schemas, SLAs, & RSO scheduling
- **E.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, D` (`CSV: 3,4`)

Correct answers: C and D (are correct). Dynamics 365 Field Service (`Work Order` + Connected Field Service + `RSO`) paired with a certified AppSource global tax-engine ISV avoids reinventing complex scheduling and tax-compliance rules. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **C:** Correct. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **D:** Correct. Adopting Dynamics 365 first-party apps avoids reinventing complex case routing, omnichannel queues, or Resource Scheduling Optimization.
- **E:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.

</details>

### Q060 (`E3Q042`) — Perform solution envisioning and requirement analysis [1.16] · *Single-Answer Multiple Choice*

When 85% of a manufacturer’s complex multi-territory quote-to-cash and forecasting requirements match native **Dynamics 365 Sales**, why should you adopt the first-party app over building custom opportunity tables?

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Dynamics 365 first-party app (`Sales`, `Customer Service`, or `Field Service`) leveraging native schemas, SLAs, & RSO scheduling
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Adopting Dynamics 365 Sales delivers native Opportunity-to-Quote pipelines, AI Copilot insights, Dual-write ERP mappings, and continuous Microsoft wave enhancements at lower total TCO. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Correct. Adopting Dynamics 365 first-party apps avoids reinventing complex case routing, omnichannel queues, or Resource Scheduling Optimization.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q061 (`E3Q028`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

Attaching explicit `Given / When / Then` pass/fail conditions (including boundary tolerances and error states) to every User Story establishes testable `____`.

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Refining prescriptive wishes into persona-based `User Stories` (`As a ... I need ... so that ...`) with testable Acceptance Criteria
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Testable Acceptance Criteria eliminate ambiguity between business SMEs, pro-code/low-code makers, and UAT validators. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Correct. Outcome-oriented User Stories decouple business intent from premature UI assumptions and anchor QA test cases.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q062 (`E3Q077`) — Architect a solution [2.15] · *Single-Answer Multiple Choice*

Every tiger-team failure investigation adds 5 temporary cross-functional engineers for 3 weeks and then disbands. Why should you use an **Access Team Template** instead of creating 4,000 permanent Owner Teams or manually sharing rows?

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Combining `Modernized Business Units` (matrix access), `Microsoft Entra ID Security Group Teams`, & `Access Team Templates`
- **D.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). **Access Team Templates** auto-create lightweight record-scoped teams on demand without owning records, needing cached Security Roles, or exploding `PrincipalObjectAccess` (`POA`) share descriptors. [Skill 2.15: Design Business Units, Modernized BUs, Owner Teams, Access Team Templates, & Entra Group Teams | Source: Design Business Units, Modernized BUs, Owner/Access Teams, & Entra Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Correct. Modernized BUs enable cross-BU matrix roles, Entra Group Teams automate zero-touch RBAC, and Access Teams handle ad-hoc record collaboration cleanly.
- **D:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.

</details>

### Q063 (`E3Q016`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

A manufacturing CIO worries that rapid low-code adoption without automated testing or telemetry will recreate their brittle 2010 Lotus Notes sprawl. Which Well-Architected pillar directly addresses this concern?

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Power Platform Well-Architected `Operational Excellence` pillar (automated ALM pipelines, Application Insights, & CoE)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Operational Excellence` institutes automated ALM pipelines, Solution Checker gates, Managed Environments, and Application Insights telemetry to prevent ungoverned sprawl. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Correct. Operational Excellence standardizes CI/CD solution pipelines, automated Solution Checker gates, telemetry, and Managed Environment governance.

</details>

### Q064 (`E3Q095`) — Implement the solution [3.6] · *Ordered Sequence (Multiple Choice)*

Six factories cut over to the new quality suite during Sunday’s 6-hour maintenance window. Which four-step cutover sequence protects Production integrity from user writes and validates go-live?

- **A.** Allow 5,000 users to edit records during live schema upgrade and migration → Import Unmanaged solutions into Production → Skip smoke tests → Turn on auditing two months later
- **B.** Freeze changes & verify backup restore point → Enable Dataverse `Administration mode` (blocking regular users & async jobs) → Apply Managed Upgrades & run validated delta loads → Exit `Administration mode`, smoke-test, & monitor hypercare
- **C.** Delete existing Managed Solutions in Production (erasing live tables!) → Re-import from scratch → Manually re-type Connection References & Environment Variables → Disable backups
- **D.** Ignore Dataverse Database/File storage overages blocking admin ops → Skip Solution Checker critical findings → Leave Dev URLs in Environment Variables → Disband support team at launch minute

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Verifying restore points, enabling `Administration mode` (blocking non-admins & async background jobs), applying Managed Solution Upgrades + delta migrations, and exiting `Administration mode` after smoke tests ensures a controlled launch. [Skill 3.6: Escalate and resolve data migration bottlenecks (BypassCustomPluginExecution, delta loads, reconciliation) | Source: Escalate and remediate enterprise data migration bottlenecks and cutover issues (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/TVF-override-plugin-execution)]

- **A:** Incorrect. Concurrent user edits during cutover cause migration collisions, lock timeouts, and inconsistent business state.
- **B:** Correct. Controlled cutovers establish restore points, engage `Administration mode` to prevent user writes and background noise, apply Managed Upgrades + delta loads, validate smoke tests, and transition to monitored hypercare.
- **C:** Incorrect. Deleting a Managed Solution erases its custom Dataverse tables and production data; always use Managed `Stage for upgrade` -> `Apply upgrade`.
- **D:** Incorrect. Exceeded Dataverse storage entitlements block environment copy/restore/admin operations and sabotage cutover readiness.

</details>

### Q065 (`E3Q088`) — Implement the solution [3.3] · *Ordered Sequence (Multiple Choice)*

A PLM-to-Dataverse engineering BOM sync hits `HTTP 429` throttling every afternoon when 200,000 part revisions release simultaneously. Which four-step remediation sequence resolves the bottleneck cleanly?

- **A.** Move bulk integration loops inside synchronous Dataverse plug-ins → Chain 8 child plug-in updates per row → Enable `RetrieveAllEntities` metadata calls on every transaction → Disable caching
- **B.** Buy 100 Power BI Free licenses expecting them to lift 5-minute Service Protection caps → Hardcode personal maker credentials → Ignore `x-ms-ratelimit-time-remaining-xrm-requests` headers → Discard throttled records silently
- **C.** Spin up 50 parallel threads under one single user account → Retry HTTP 429 errors immediately with 0 ms delay → Replace filtered queries with full `SELECT *` scans → Open a ticket asking Microsoft to disable platform limits permanently
- **D.** Pinpoint throttled callers in Dataverse API analytics → Batch writes via `CreateMultiple` / `$batch` & use Change Tracking → Pool high-volume S2S loads across Entra Application Users → Honor HTTP `429` `Retry-After` backoff

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Analyzing Dataverse API telemetry, switching to `UpdateMultiple`/`CreateMultiple`/`$batch` + Change Tracking, pooling S2S Application Users, and honoring `HTTP 429` `Retry-After` headers eliminates throttling. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Heavy metadata calls and chained synchronous updates multiply execution time against the 20-minute per-5-minute sliding window limit.
- **B:** Incorrect. Service Protection limits protect real-time platform stability per user/web server over 5-minute windows regardless of license SKU.
- **C:** Incorrect. Immediate zero-delay retries under a single user identity amplify `HTTP 429` throttling and extend penalty windows.
- **D:** Correct. Resolving Service Protection (`6,000` req / `20` min compute per 5-min window) combines batch/bulk operations, Change Tracking, pooled S2S Application Users where appropriate, and honoring `Retry-After` backoff.

</details>

### Q066 (`E3Q091`) — Implement the solution [3.4] · *Multi-Select (Select 2)*

Two concurrent warehouse scanners update `Bin_Quantity` on the same `Inventory_Lot` row (`HTTP PATCH`), causing lost decrements, while unfiltered `When a row is modified` flows fire 40 times per lot and bloat Dataverse `Log` storage. Which two fixes resolve these issues? Select two.

- **A.** Resolving automation/integration conflicts via `Select columns` (`filteringattributes`), `Trigger Conditions`, plug-in `Depth` checks, & `ETag` (`If-Match`) optimistic concurrency
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Governing `Database`, `File`, & `Log` storage pools via `Dataverse Long Term Retention`, `Fabric/Synapse Link` archival, & attachment offloading
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **E.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). Enforcing **`If-Match` (`ETag`) optimistic concurrency** plus `Select columns` / `Trigger Conditions` (`res_conflict_loops`) and governing `Log`/`Database` storage pools (`cap_storage_tiering`) eliminate lost updates and runaway audit growth. [Skill 3.4: Assess storage/resource impact and resolve automation loops, race conditions, & integration conflicts | Source: Assess storage/resource impact and resolve automation & integration conflicts (https://learn.microsoft.com/en-us/power-platform/admin/capacity-storage)]

- **A:** Correct. Column filters, actor exclusions, and `If-Match` row-version headers eliminate infinite ping-pong loops and silent lost-update race conditions.
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Correct. Keeping relational `Database` capacity lean prevents tenant admin lockouts (`Copy`/`Restore` blocks) and controls storage overage costs.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **E:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

## Case Study Vignette — Vortex Turbine Aftermarket

> Vortex Turbine Aftermarket executives demand unified analytics combining 1.2M Dataverse service orders with 8 TB of historical turbine sensor parquet files. Operational leads also want embedded contextual Power BI visuals filtered by the user’s Dataverse security role directly inside Model-driven forms without granting direct SQL table access.

### Q067 (`E3Q010`) — Perform solution envisioning and requirement analysis [1.4] · *Single-Answer Multiple Choice*

Case study — Vortex Turbine Aftermarket: Rather than migrating 8 TB of historical turbine sensor parquet files into expensive Dataverse relational tables, which architecture minimizes migration effort while enabling unified executive analytics alongside 1.2M Dataverse service orders?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **D.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Keeping the 8 TB parquet history in OneLake / Azure Data Lake and linking Dataverse via **`Microsoft Fabric Link`** (`Azure Synapse Link`) delivers unified Power BI analytics with zero telemetry migration into Dataverse Database storage. [Skill 1.4: Identify and estimate data migration and integration efforts, complexity drivers, and alternatives | Source: Estimate migration and integration efforts and alternatives (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **D:** Correct. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.

</details>

### Q068 (`E3Q058`) — Architect a solution [2.6] · *Single-Answer Multiple Choice*

Case study — Vortex Turbine Aftermarket: Vortex executives need reports blending 1.2M Dataverse service orders with 8 TB of turbine parquet files, AND operational leads want contextual Power BI tiles embedded on Model-driven forms filtered dynamically by each user’s security identity without direct SQL table access. Which design meets both needs?

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics
- **D.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Using **`Microsoft Fabric Link`** (`OneLake`) for the 8 TB + 1.2M lakehouse model and embedding **Power BI reports configured with Entra SSO and Row-Level Security (`RLS`)** on Model-driven forms delivers both big-data scale and contextual user security. [Skill 2.6: Design data visualization strategies across Dataverse charts, Power BI RLS, and Fabric/Synapse Link | Source: Design data visualization (Dataverse charts, Power BI RLS, Fabric/Synapse Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-synapse)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Correct. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.
- **D:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).

</details>

### Q069 (`E3Q063`) — Architect a solution [2.9] · *Single-Answer Multiple Choice*

Case study — Vortex Turbine Aftermarket: Service engineers inside a Model-driven app occasionally inspect read-only historical calibration certificates stored in an external SQL/Fabric warehouse (40 million rows) while online, with zero need for offline sync or Dataverse row ownership. Which data pattern avoids duplicating 40 million rows into Dataverse?

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Replicating data into native Dataverse tables (`Dataflows` / `ADF`) when Mobile Offline, row-level security roles, auditing, or SLAs are required
- **C.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **D.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Exposing the external warehouse in place via **Dataverse Virtual Tables** (`Virtual Connector Provider` or custom OData v4 provider) enables live Model-driven views and lookups without consuming Dataverse Database capacity. [Skill 2.9: Determine when to connect external data in place (Virtual tables) versus import/replicate into Dataverse | Source: Connect external data in place (Virtual tables) vs import/replicate into Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-virtual-entities)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Incorrect. Virtual tables do not support Mobile Offline sync, Dataverse row-level User/Team ownership, or native column auditing.
- **C:** Correct. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **D:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).

</details>

### Q070 (`E3Q032`) — Perform solution envisioning and requirement analysis [1.13] · *Multi-Select (Select 3)*

A defense propulsion maintenance system on Power Platform undergoes formal NFR review. Which three specifications belong in the **Non-Functional Requirements (`NFRs`)** baseline? Select three.

- **A.** Capturing Non-Functional Requirements (`RPO`/`RTO`, peak concurrency, `p95` latency, API volume, `WCAG 2.1 AA`, & retention)
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Designing for `WCAG 2.1 AA` accessibility (`AccessibleLabel`, `TabIndex`, contrast) and `.resx` multi-language localization
- **D.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **E.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **F.** Power Platform Well-Architected `Reliability` pillar (RPO/RTO targets, fault isolation, retries, & circuit breakers)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C, F` (`CSV: 1,3,6`)

Correct answers: A, C, and F (are correct). Peak concurrent users, `p95` form latency, daily API requests, & 30-year airworthiness retention (`req_nfr_spec`), `RPO`/`RTO` disaster-recovery bounds (`wa_reliability`), and gloved-hand/high-contrast `WCAG 2.1 AA` accessibility (`ux_wcag_accessible`) are core NFRs. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Correct. Non-functional requirements govern architectural sizing, BCDR, licensing capacity, offline design, and security controls.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Correct. Building accessibility and localization into initial UX components avoids expensive retrofits before public or enterprise launch.
- **D:** Incorrect. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **E:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **F:** Correct. The Reliability pillar ensures mission-critical workloads withstand transient outages, throttling, and regional faults within defined RPO/RTO bounds.

</details>

### Q071 (`E3Q017`) — Perform solution envisioning and requirement analysis [1.7] · *Single-Answer Multiple Choice*

A VP of Quality states: `"Make non-conformance reporting world-class."` Proposed solution: Rewrite the goal into baseline-backed `SMART` KPIs (such as cutting scrap-disposition cycle time from `11 days` to `< 8 hours`, reducing incomplete NCR submissions below `1%`, and hitting `92%` plant-inspector adoption within 60 days). Is this valid?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Defining baseline-backed `SMART` success KPIs (cycle-time reduction, error-rate drop, SLA adherence, & active adoption %)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — quantifiable `SMART` metrics anchored to pre-launch baselines enable objective post-go-live ROI verification. [Skill 1.7: Review and validate measurable key success criteria, KPIs, and adoption targets | Source: Review measurable key success criteria, KPIs, and adoption targets (https://learn.microsoft.com/en-us/power-platform/guidance/adoption/measure-business-value)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Correct. Quantifiable KPIs anchored to current-state baselines let stakeholders verify objective ROI after go-live.

</details>

### Q072 (`E3Q043`) — Perform solution envisioning and requirement analysis [1.17] · *Multi-Select (Select 2)*

Product engineers need: (1) an interactive 3D CAD `.gltf` part viewer embedded directly on a Model-driven `Asset` form, and (2) reusable server-side warranty-entitlement logic callable via OData from Power Pages, Canvas apps, and SAP. Which two supported gap solutions fit best? Select two.

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Defining solution-aware Dataverse `Custom APIs` exposing strongly typed request/response contracts for internal and external callers
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Validating interactive UX prototypes (`Figma-to-App` / `Custom Pages`) early and building `PCF` controls for specialized UI gaps
- **E.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). A **Power Apps Component Framework (`PCF`)** control (`ux_proto_pcf`) renders interactive WebGL/3D CAD components natively on forms, while a Dataverse **`Custom API`** (`integ_custom_api`) exposes a reusable, versioned server-side OData operation. [Skill 1.17: Address functional gaps through supported low-code/pro-code alternate solutions | Source: Address functional gaps through low-code/pro-code alternate solutions (https://learn.microsoft.com/en-us/power-platform/well-architected/operational-excellence/overview)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Correct. Custom APIs replace legacy Custom Process Actions with code-first, solution-aware OData bound/unbound operations and granular privilege checks.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Correct. Interactive prototyping validates user journeys cheaply, while Power Apps Component Framework (`PCF`) renders reusable custom TypeScript/React controls.
- **E:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q073 (`E3Q086`) — Implement the solution [3.2] · *Multi-Select (Select 2)*

A security review reveals a developer hid export-controlled fields using `formContext.getControl('aero_itarspec').setVisible(false)` and left `Anonymous Users` Web Role mapped to a `Global` Read Table Permission on Power Pages. Which two fixes are required? Select two.

- **A.** Auditing server-side `Security Roles`, `Column Security`, & `Power Pages Table Permissions` rather than trusting client-side UI rules
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **E.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E` (`CSV: 1,5`)

Correct answers: A and E (are correct). Removing `Global` anonymous `Table Permissions` during server-side boundary audit (`val_sec_boundary_audit`) and securing `aero_itarspec` with a server-side **`Column Security Profile`** (`sec_col_hier_pim`) close both data leaks. [Skill 3.2: Review security across Business Rules, Security Roles, Entra Conditional Access, & security boundaries | Source: Review end-to-end security across Business Rules, Roles, Entra ID, & boundaries (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Correct. Client JavaScript and `Form`-scoped Business Rules never block Web API/OData access; security boundaries must be enforced server-side in Dataverse.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **E:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.

</details>

### Q074 (`E3Q090`) — Implement the solution [3.3] · *Single-Answer Multiple Choice*

Dataverse’s real-time **Service Protection** API limits enforce `6,000` requests or `1,200,000 ms` (`20 minutes`) of combined execution time per user account per web server within each `____` sliding window.

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Conforming to `Dataverse Service Protection` limits (`6,000` req / `20m` compute per `5-min` window), pooling `S2S Application Users`, & honoring `Retry-After`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Dataverse Service Protection evaluates request count (`6,000`) and cumulative server execution time (`20 minutes`) over a **5-minute (`300-second`) sliding window**. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Correct. Service Protection enforces per-user/per-web-server 5-minute sliding caps (`HTTP 429`); pooling S2S Application Users and respecting `Retry-After` maximizes throughput.

</details>

### Q075 (`E3Q060`) — Architect a solution [2.7] · *Single-Answer Multiple Choice*

Guiding engineering change requests across `Draft -> Impact Analysis -> CCB Vote -> Tooling Update -> Released` spanning `Change_Request` and `ECO_Order` tables uses `____`.

- **A.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A multi-table **Business Process Flow (`BPF`)** enforces consistent cross-table stage gates and conditional branching for engineering approvals. [Skill 2.7: Design automation strategies (sync vs async, BPF, Logic Apps) and multi-environment ALM topology | Source: Design automation & multi-environment strategies (CoE Starter Kit & ALM) (https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit)]

- **A:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Correct. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q076 (`E3Q098`) — Implement the solution [3.7] · *Single-Answer Multiple Choice*

When promoting a Managed Solution that contains 8 Power Automate cloud flows and 3 Custom Connectors across `Dev -> QA -> UAT -> Prod`, how should target SAP URLs and service-principal connections bind automatically per stage?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Resolving deployment failures by running `Remove active customizations`, refactoring circular solution dependencies into a base layer, & validating stage JSON bindings
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Using **Deployment Settings JSON** (`pac solution create-settings`) binds stage-specific **Environment Variables** and **Connection References** automatically during pipeline import. [Skill 3.7: Resolve deployment plan issues, Unmanaged Active Solution Layers, and circular solution dependencies | Source: Resolve deployment plan, Solution Layer, and pipeline dependency issues (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Correct. Stripping Unmanaged Active layers and decoupling circular references ensures repeatable, zero-touch Managed Solution Upgrades.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q077 (`E3Q029`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

Plant East requires QA sign-off above `$1,000` scrap value while Plant West requires QA sign-off above `$1,200` with no regulatory basis for the difference. What should the Solution Architect recommend?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **D.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Guiding leadership to harmonize arbitrary plant variations into one standardized enterprise scrap-approval threshold simplifies future-state automation and reporting. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **D:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.

</details>

### Q078 (`E3Q036`) — Perform solution envisioning and requirement analysis [1.14] · *Single-Answer Multiple Choice*

Fourteen global service depots each invented different RMA return codes over 15 years. Standardizing on one global RMA taxonomy and BPF before configuring Dataverse exemplifies `____`.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **D.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Future-state process harmonization establishes consistent global taxonomies and streamlined workflows prior to build. [Skill 1.14: Guide future-state business process optimization and standardization before automating | Source: Guide future-state business process optimization and standardization (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **D:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.

</details>

### Q079 (`E3Q071`) — Architect a solution [2.12] · *Single-Answer Multiple Choice*

Why should you replace legacy Dataverse `Custom Process Actions` with code-first **Dataverse `Custom APIs`** when designing new reusable integration messages?

- **A.** Defining solution-aware Dataverse `Custom APIs` exposing strongly typed request/response contracts for internal and external callers
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Dataverse `Custom APIs` support granular custom privilege gating (`ExecutePrivilegeName`), `IsPrivate` visibility control, strongly typed parameters, and lightweight plug-in execution without workflow-AML overhead. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Correct. Custom APIs replace legacy Custom Process Actions with code-first, solution-aware OData bound/unbound operations and granular privilege checks.
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q080 (`E3Q038`) — Perform solution envisioning and requirement analysis [1.15] · *Single-Answer Multiple Choice*

Scoring each requirement across `Standard Fit`, `Declarative Configuration`, `AppSource ISV`, and `Custom Code` alongside license SKU and maintenance impact produces a `____`.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Structured Fit/Gap matrix scoring requirements across `Out-of-the-Box`, `Configuration`, `AppSource ISV`, & `Custom Code`
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A formal Fit/Gap matrix documents architectural rationale, licensing requirements, and long-term TCO per requirement. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Correct. Formal fit/gap scoring exposes customization TCO, licensing impacts, and upgrade maintenance trade-offs transparently.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q081 (`E3Q041`) — Perform solution envisioning and requirement analysis [1.16] · *Single-Answer Multiple Choice*

Procurement asks whether 1,200 field technicians licensed only with Power Apps per-app plans can update Dynamics 365 `Work Order` (`msdyn_workorder`) and `Agreement` restricted tables directly. What must you advise?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Validating Dynamics 365 restricted-table licensing (`Case / incident`, `Work Order`, `Entitlement`) during fit/gap analysis
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Dynamics 365 **restricted tables** (`msdyn_workorder`, `Case / incident`, `Entitlement`) require qualifying Dynamics 365 licenses for CRUD operations rather than standalone Power Apps licenses. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Correct. Restricted Dynamics 365 tables require appropriate Dynamics 365 licenses for CRUD operations rather than standalone Power Apps licenses.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q082 (`E3Q092`) — Implement the solution [3.4] · *Single-Answer Multiple Choice*

Configuring the Dataverse connector’s **`Select columns`** (`filteringattributes`) and **`Filter rows`** (`Trigger Conditions` OData expression) ensures a Power Automate flow triggers **only** when `aero_status eq 100000003` and ignores unrelated column saves. This prevents `____`.

- **A.** Resolving automation/integration conflicts via `Select columns` (`filteringattributes`), `Trigger Conditions`, plug-in `Depth` checks, & `ETag` (`If-Match`) optimistic concurrency
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Column-scoped triggers (`Select columns`) and OData `Filter rows` eliminate unnecessary flow runs, API waste, and bi-directional update loops. [Skill 3.4: Assess storage/resource impact and resolve automation loops, race conditions, & integration conflicts | Source: Assess storage/resource impact and resolve automation & integration conflicts (https://learn.microsoft.com/en-us/power-platform/admin/capacity-storage)]

- **A:** Correct. Column filters, actor exclusions, and `If-Match` row-version headers eliminate infinite ping-pong loops and silent lost-update race conditions.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q083 (`E3Q085`) — Implement the solution [3.1] · *Single-Answer Multiple Choice*

Canvas **App Checker** reports `Delegation warning: The highlighted part of this formula might not work correctly on large data sets` on `Filter(Serial_Parts, Year(Manufactured_Date) = 2025)` over 900,000 rows. Why is this a critical pre-go-live defect?

- **A.** Enforcing `Solution Checker` and `App Checker` gates in CI/CD pipelines alongside `Power Platform Well-Architected` design reviews
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Non-delegable predicates (`Year(...)`) silently truncate evaluation to only the first `500` (max `2,000`) local rows, returning incomplete/wrong search results across 900,000 serialized parts; rewrite using delegable date-range bounds (`>= Date(2025,1,1) && < Date(2026,1,1)`). [Skill 3.1: Evaluate detailed designs and implementations with Solution Checker, App Checker, & Well-Architected | Source: Evaluate detailed designs with Solution Checker, App Checker, & Well-Architected (https://learn.microsoft.com/en-us/power-platform/alm/use-powershell-cmdlets-solution-checker)]

- **A:** Correct. Solution Checker flags unbounded queries and sync plug-in anti-patterns, while App Checker catches delegation warnings and WCAG errors before release.
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.

</details>

### Q084 (`E3Q035`) — Perform solution envisioning and requirement analysis [1.14] · *Single-Answer Multiple Choice*

Currently, warranty clerks print claims, walk them across two buildings for rubber stamps, and type totals into three spreadsheets. Proposed solution: Harmonize and redesign the workflow into a single digital future-state Dataverse process with automated threshold routing before building screens. Is this the right architectural sequence?

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes — optimizing and standardizing future-state processes before automating eliminates manual handoffs instead of digitizing waste. [Skill 1.14: Guide future-state business process optimization and standardization before automating | Source: Guide future-state business process optimization and standardization (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/overview)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q085 (`E3Q056`) — Architect a solution [2.5] · *Single-Answer Multiple Choice*

Warranty routing workflows check exact GUIDs of 120 `Defect_Category` reference records across Dev, QA, UAT, and Prod, while `SSIS`/KingswaySoft upserts 5 million `Assets` keyed by `Serial_Number`. Which migration pattern should you use?

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Staging cleansed records via `ADF` / `SSIS` using Dataverse `Alternate Keys` (`Upsert`) and `Configuration Migration Tool` for fixed-GUID config rows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Exporting/importing `Defect_Category` via the **Configuration Migration Tool (`CMT`)** preserves identical GUIDs across environments, while a Dataverse **`Alternate Key`** on `Serial_Number` powers fast `Upsert` loads. [Skill 2.5: Design enterprise data migration strategies, load sequencing, Alternate Keys, and CMT tooling | Source: Design enterprise data migration strategies, load order, and tooling (https://learn.microsoft.com/en-us/power-platform/admin/create-schema-export-data)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Correct. Alternate Keys eliminate GUID pre-lookup round-trips on upserts, while CMT preserves exact reference-record GUIDs across Dev/UAT/Prod.

</details>

### Q086 (`E3Q034`) — Perform solution envisioning and requirement analysis [1.13] · *Single-Answer Multiple Choice*

Aviation authorities mandate retaining airworthiness inspection logs for `30 years` while keeping live work-order views sub-second. Which storage strategy satisfies both NFRs?

- **A.** Governing `Database`, `File`, & `Log` storage pools via `Dataverse Long Term Retention`, `Fabric/Synapse Link` archival, & attachment offloading
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Using **Dataverse Long Term Retention** and `Microsoft Fabric Link` archival tiers cold multi-decade airworthiness logs out of hot transactional tables cleanly. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Correct. Keeping relational `Database` capacity lean prevents tenant admin lockouts (`Copy`/`Restore` blocks) and controls storage overage costs.
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q087 (`E3Q039`) — Perform solution envisioning and requirement analysis [1.15] · *Single-Answer Multiple Choice*

A developer suggests writing SQL `UPDATE` triggers directly inside Dataverse’s underlying Azure SQL database to close a rollup gap. How must you classify this in fit/gap analysis?

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Structured Fit/Gap matrix scoring requirements across `Out-of-the-Box`, `Configuration`, `AppSource ISV`, & `Custom Code`
- **C.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **D.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Direct SQL access/triggers on Dataverse’s managed SQL engine are completely blocked/unsupported; fit/gap analysis maps the gap to supported Dataverse Rollup/Formula columns or plug-ins. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Correct. Formal fit/gap scoring exposes customization TCO, licensing impacts, and upgrade maintenance trade-offs transparently.
- **C:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **D:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.

</details>

### Q088 (`E3Q020`) — Perform solution envisioning and requirement analysis [1.8] · *Single-Answer Multiple Choice*

To publish Teamcenter PLM engineering-BOM APIs to Power Platform custom connectors with centralized certificate rotation, throttling, and schema versioning, you should route calls through `____`.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Azure API Management (`APIM`) provides centralized OAuth/mTLS enforcement, rate throttling, and OpenAPI contract governance for enterprise backend APIs. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q089 (`E3Q075`) — Architect a solution [2.14] · *Single-Answer Multiple Choice*

For an on-premises AS/400 DB2 database sitting inside a regional plant LAN that is **not** connected to an Azure VNet, how should Power Automate cloud flows connect securely without opening inbound firewall ports?

- **A.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources
- **B.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Installing a multi-node active-active **On-Premises Data Gateway** cluster inside the plant LAN provides outbound-only TLS relay connectivity with high availability. [Skill 2.14: Assess VNet subnet delegation, Azure ExpressRoute nuances, Data Gateways, and IP firewall networking | Source: Assess VNet integration, Azure ExpressRoute, gateways, and IP firewall networking (https://learn.microsoft.com/en-us/power-platform/admin/vnet-support-overview)]

- **A:** Correct. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.
- **B:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

## Case Study Vignette — StratosWing Aerospace

> StratosWing Aerospace runs Dynamics 365 Supply Chain Management (`F&O`) alongside Dynamics 365 Sales & Power Platform for 1,400 defense suppliers. Near-real-time customer/quote synchronization between F&O and Dataverse is mandatory, while ITAR export-controlled drawings require defense-in-depth DLP, Customer Lockbox, and Entra Conditional Access.

### Q090 (`E3Q014`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

Case study — StratosWing Aerospace: StratosWing Aerospace handles defense drawings subject to US `ITAR` sovereign-cloud / citizenship access controls and strict data-exfiltration penalties. Which risk factor must the Solution Architect assess before selecting commercial vs US Government (`GCC High`) cloud environments?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Assessing sovereign data-residency (`Multi-Geo`), PII/PHI/ITAR compliance, `CMK`, & cross-border connector risks upfront

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `ITAR` export-control and sovereign residency rules dictate cloud boundary selection (`GCC High` vs commercial Geo), `CMK`, `Customer Lockbox`, and strict DLP exfiltration blocks before provisioning environments. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Correct. Identifying residency and regulatory encryption constraints during envisioning prevents illegal cross-region tenant/environment placement.

</details>

### Q091 (`E3Q068`) — Architect a solution [2.11] · *Single-Answer Multiple Choice*

Case study — StratosWing Aerospace: StratosWing runs Dynamics 365 Supply Chain Management (`F&O`) and Dynamics 365 Sales in the same tenant and requires near-real-time bi-directional `Customer`, `Released Product`, and `Quotation` sync plus asynchronous ERP `Purchase Order Confirmed` triggers. Which native integration pairing should you architect?

- **A.** Integrating Microsoft Teams (`Adaptive Cards` / embedded apps), Dynamics 365 F&O `Dual-write` + `Business Events`, & `Server-Side Sync`
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). **Dynamics 365 Dual-write** synchronizes `Customer`, `Product`, and `Quotation` rows near-real-time between F&O and Dataverse, while **Dynamics 365 F&O Business Events** emit lightweight asynchronous lifecycle triggers to Power Automate / Service Bus. [Skill 2.11: Design collaboration (Teams, SharePoint ACL nuances, Exchange) and Dynamics 365 Dual-write integrations | Source: Design Teams, SharePoint, Exchange, and Dynamics 365 (Dual-write) integrations (https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dual-write/dual-write-overview)]

- **A:** Correct. Dual-write provides near-real-time bi-directional Dataverse-to-F&O sync, while Teams Adaptive Cards meet users directly in collaboration channels.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **D:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.

</details>

### Q092 (`E3Q078`) — Architect a solution [2.16] · *Multi-Select (Select 3)*

Case study — StratosWing Aerospace: To satisfy defense compliance across its Dataverse environments, StratosWing requires: (1) explicit executive approval before Microsoft support touches data, (2) time-bound MFA-gated elevation for `System Administrator` duties, and (3) IP firewall + Conditional Access device checks. Which three controls deliver this? Select three.

- **A.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access
- **B.** Enforcing `Microsoft Entra Conditional Access` (MFA & compliant device) plus `Power Platform IP Firewall` & `Cookie IP binding`
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **E.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **F.** Power Platform Well-Architected `Security` pillar (Zero Trust Entra identity, least privilege, DLP, & encryption)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B, F` (`CSV: 1,2,6`)

Correct answers: A, B, and F (are correct). `Customer Lockbox` + `CMK` + `Microsoft Entra PIM` just-in-time admin elevation (`sec_col_hier_pim`), `Entra Conditional Access` + `Power Platform IP Firewall` (`sec_cond_access_ip`), and defense-in-depth Zero Trust `Security` pillar governance (`wa_security`) satisfy `ITAR`/defense audits. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.
- **B:** Correct. Combining Entra Conditional Access with Managed Environment IP Firewall and session cookie binding blocks token replay from untrusted networks.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **E:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **F:** Correct. The Security pillar protects confidentiality and integrity through Entra Conditional Access, least-privilege roles, DLP endpoint rules, and CMK/Lockbox.

</details>

### Q093 (`E3Q012`) — Perform solution envisioning and requirement analysis [1.5] · *Single-Answer Multiple Choice*

Feeding ERP purchase-requisition event logs (`Req_ID`, `Step`, `Timestamp`, `Plant_Code`) into `____` visualizes bottleneck handoffs and non-compliant maverick buying paths automatically.

- **A.** Power Automate Process Mining & Task Mining paired with cross-functional current-state discovery workshops
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Power Automate Process Mining transforms timestamped event logs into interactive process maps highlighting bottlenecks, root causes, and compliance deviations. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Correct. Combining telemetry-driven Process/Task Mining with SME workshops exposes hidden rework loops and shadow processes objectively.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q094 (`E3Q045`) — Perform solution envisioning and requirement analysis [1.18] · *Multi-Select (Select 2)*

During UAT of a global dealer warranty MVP, regional sales directors demand adding a dealer-marketing co-op rebate portal and AR VR showroom app before launch. Which two governance steps should the Solution Architect take? Select two.

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Scoping a high-value `MVP` Phase 1 release using MoSCoW prioritization and formal change-request governance
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Establishing a fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model
- **E.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Protecting the `MVP` Phase 1 scope via MoSCoW prioritization (`scope_mvp_phased`) and evaluating net-new requests through formal Change Control / ARB governance (`disc_raci_governance`) safeguards go-live quality and schedule. [Skill 1.18: Determine MVP vs phased solution scope boundaries and govern scope changes | Source: Determine MVP vs phased solution scope and manage scope boundaries (https://learn.microsoft.com/en-us/training/paths/become-solution-architect/)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Correct. Phased MVP delivery de-risks go-live, delivers early business value, and prevents uncontrolled scope creep.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Correct. Clear architectural ownership, ARB design gates, and CoE guardrails align business, citizen makers, pro-devs, and InfoSec.
- **E:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q095 (`E3Q004`) — Perform solution envisioning and requirement analysis [1.2] · *Multi-Select (Select 2)*

A heavy-machinery OEM requires: (1) an internal AI Copilot embedded in plant Teams channels that answers torque-spec questions from SharePoint engineering manuals and logs service tickets in Dataverse, and (2) a dense desktop engineering-change-order (`ECO`) app with 6-stage BPFs. Which two components fit best? Select two.

- **A.** Microsoft Copilot Studio agent grounded in enterprise knowledge sources, Dataverse actions, & live omnichannel handoff
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Model-driven Power App over Microsoft Dataverse with responsive forms, views, dashboards, & Business Process Flows
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **E.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). Microsoft Copilot Studio grounds conversational agents in engineering manuals with Dataverse actions, while a Model-driven Power App manages multi-stage `ECO` lifecycles over Dataverse. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Correct. Copilot Studio delivers governed conversational and autonomous agents across Teams, web portals, and customer service channels.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Correct. Model-driven apps excel at structured, data-dense back-office case and lifecycle management directly atop Dataverse security.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **E:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.

</details>

### Q096 (`E3Q008`) — Perform solution envisioning and requirement analysis [1.3] · *Single-Answer Multiple Choice*

When a turbine vibration threshold trips in Dataverse, a Python finite-element fatigue solver must run for 14 minutes using 16 GB of RAM before posting remaining-useful-life metrics back to Dataverse. Offloading compute to `____` avoids Dataverse’s 2-minute plug-in sandbox limit.

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **D.** Azure pro-code extension (`Azure Functions`, `Service Bus`, `AKS`, or `Azure AI Foundry`) integrated with Power Platform

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Compute workloads exceeding Dataverse’s 2-minute/memory sandbox caps belong in Azure pro-code services (`Azure Functions` Premium, `Azure Container Apps`, or `AKS`) invoked asynchronously. [Skill 1.3: Identify and select components from existing apps, Dynamics 365, AppSource ISVs, and Azure | Source: Evaluate Dynamics 365 apps, AppSource ISVs, and Azure extensions (https://learn.microsoft.com/en-us/training/modules/discover-customer-needs/)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **D:** Correct. Heavy compute, long-running algorithms (> 2 minutes), and high-throughput brokered messaging offload cleanly to Azure extensions.

</details>

### Q097 (`E3Q024`) — Perform solution envisioning and requirement analysis [1.9] · *Single-Answer Multiple Choice*

Modeling dealerships as `Account`, dealer technicians as `Contact`, and field inspections as `Activity`/standard entities aligns your schema with `____`.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Aligning data entities to the Microsoft Common Data Model (`CDM`) standard tables (`Account`, `Contact`, `Activity`)
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Aligning with the Microsoft Common Data Model (`CDM`) ensures native compatibility with Dynamics 365 Sales/Field Service, Dual-write, and AppSource ISVs. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Correct. Extending standard CDM tables preserves native Dynamics 365, AppSource ISV, Exchange, and AI Copilot interoperability.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.

</details>

### Q098 (`E3Q033`) — Perform solution envisioning and requirement analysis [1.13] · *Single-Answer Multiple Choice*

Factory kiosks operated under bright sodium lighting by multilingual crews in 6 countries require high-contrast tokens, keyboard/scanner focus order, and `.resx` translations under `____`.

- **A.** Designing for `WCAG 2.1 AA` accessibility (`AccessibleLabel`, `TabIndex`, contrast) and `.resx` multi-language localization
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Building `WCAG 2.1 AA` accessibility and `.resx` localization into initial Canvas/Model-driven components satisfies global shop-floor usability and compliance NFRs. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Correct. Building accessibility and localization into initial UX components avoids expensive retrofits before public or enterprise launch.
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.

</details>

### Q099 (`E3Q049`) — Architect a solution [2.2] · *Single-Answer Multiple Choice*

Shop-floor supervisors skeptical of new software want to tap through realistic tablet screens before your team builds custom controls. How should you lead UX customization?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Validating interactive UX prototypes (`Figma-to-App` / `Custom Pages`) early and building `PCF` controls for specialized UI gaps
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Validating interactive wireframes (`Figma-to-App` / rapid Canvas `Custom Page` prototypes) with shop-floor crews first confirms ergonomics cheaply before coding specialized `PCF` controls. [Skill 2.2: Identify app customization approaches and validate interactive user experience prototypes | Source: Select customization approaches for existing apps and validate UX prototypes (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/design-consistency)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Correct. Interactive prototyping validates user journeys cheaply, while Power Apps Component Framework (`PCF`) renders reusable custom TypeScript/React controls.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q100 (`E3Q076`) — Architect a solution [2.15] · *Ordered Sequence (Multiple Choice)*

A defense manufacturer requires plant Business Unit isolation, matrix cross-BU visibility for central quality auditors, zero-touch Entra security-group role mapping, and ad-hoctiger-team sharing on root-cause investigations. Which four-step security design sequence should you apply?

- **A.** Create 400 micro Business Units mirroring every HR cost center → Move users between BUs daily (wiping roles prior to modern settings) → Duplicate 400 identical copies of every Security Role → Audit nothing
- **B.** Place all users in one root BU with Organization-level Read/Write/Delete → Clone System Administrator for power users → Hide restricted fields using client-only JavaScript → Share individual records manually
- **C.** Store confidential M&A contracts in default SharePoint Document Management folders → Assume SharePoint automatically inherits Dataverse row-level Security Roles & Access Teams → Grant site-wide Read to all employees → Go live
- **D.** Model Business Units around isolation boundaries (with Modernized BUs for matrix access) → Author custom least-privilege Security Roles → Bind roles to Entra Security Group Teams → Layer Column Security & Access Team Templates

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Modeling BUs around isolation boundaries (with Modernized BUs for matrix auditors), copying least-privilege custom Security Roles, binding roles to Entra Security Group Teams, and layering Column Security + Access Team Templates scales cleanly. [Skill 2.15: Design Business Units, Modernized BUs, Owner Teams, Access Team Templates, & Entra Group Teams | Source: Design Business Units, Modernized BUs, Owner/Access Teams, & Entra Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect. Over-fragmenting Business Units for reporting rather than true security boundaries creates massive administrative overhead.
- **B:** Incorrect. Client-side JavaScript never secures data at the API layer, and manual per-record sharing bloats the PrincipalObjectAccess (`POA`) table.
- **C:** Incorrect. Out-of-the-box SharePoint Document Management does NOT synchronize Dataverse row-level security ACLs to SharePoint folders automatically.
- **D:** Correct. Scalable Dataverse security aligns BUs to isolation boundaries, layers custom least-privilege roles onto Entra Security Group Teams for zero-touch provisioning, and handles exceptions via Access Teams and Column Security.

</details>

