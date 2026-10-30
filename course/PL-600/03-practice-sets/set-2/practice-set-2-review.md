# Microsoft Exam PL-600: Practice Exam 2 — Multi-Hospital Consolidation, Mobile Offline & Segmented ALM — Reviewer Study Key

**Theme:** Virtual tables over 60M HL7 rows, rural iPad Mobile Offline, Elastic tables for IoT bursts, Solution Layers, and loop guards  
**Credential:** Microsoft Certified: Power Platform Solution Architect Expert (`One active Associate certification required: Microsoft Certified: Power Platform Functional Consultant Associate (PL-200) OR Microsoft Certified: Power Platform Developer Associate (PL-400)`)  
**Study guide baseline:** September 23, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-600)  
**Lifecycle notice:** Exam PL-600 retired on June 30, 2026; succeeded by `Exam AB-100: Agentic AI Business Solutions Architect (Microsoft Certified: Agentic AI Business Solutions Architect Expert)`.  
**Questions:** `100` (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice percentages do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`E2Q067`) — Architect a solution [2.11] · *Ordered Sequence (Multiple Choice)*

When a `Discharge_Order` commits in Dataverse, downstream billing, durable-medical-equipment, and pharmacy systems must receive asynchronous, durable pub/sub events with Dead-Letter Queue protection and idempotent upserts. Which integration sequence should you implement?

- **A.** Register a Dataverse Service Endpoint (`Service Bus` / `Event Grid`) → Publish row events asynchronously on commit → Buffer & transform via Azure Functions / Logic Apps with DLQ → Upsert idempotently into ERP via Alternate Keys
- **B.** Poll all 10 million Dataverse rows every 10 seconds without `modifiedon` or Change Tracking → Overrun 5-minute Service Protection limits → Overwrite newer ERP records blindly → Disable TLS
- **C.** Call slow on-premises ERP SOAP endpoints inside a synchronous Pre-Operation Dataverse plug-in → Hold SQL transaction locks for 90 seconds → Ignore HTTP 429/503 errors → Lose failed payloads permanently
- **D.** Embed ERP admin client secrets inside browser JavaScript web resources → Call ERP directly from user browsers bypassing CORS & DLP → Log failed payloads to browser `console.log` → Skip auditing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Publishing from a Dataverse Service Endpoint to Azure Service Bus / Event Grid asynchronously on commit, processing via Azure Functions / Logic Apps with DLQ, and upserting idempotently via Alternate Keys decouples clinical saves from downstream outages. [Skill 2.11: Design collaboration (Teams, SharePoint ACL nuances, Exchange) and Dynamics 365 Dual-write integrations | Source: Design Teams, SharePoint, Exchange, and Dynamics 365 (Dual-write) integrations (https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dual-write/dual-write-overview)]

- **A:** Correct. Asynchronous Dataverse Service Endpoints -> Azure Service Bus/Event Grid -> Azure Functions/Logic Apps with Dead-Letter Queues and idempotent Alternate Key upserts decouple Dataverse from ERP latency and outages.
- **B:** Incorrect. Full-table polling without Dataverse Change Tracking triggers `HTTP 429` throttling and causes lost-update race conditions.
- **C:** Incorrect. Long network calls inside synchronous plug-ins exhaust Dataverse worker threads, lock SQL transactions, and lose messages when endpoints go offline.
- **D:** Incorrect. Exposing secrets in client-side JavaScript is a critical security vulnerability.

</details>

### Q002 (`E2Q017`) — Perform solution envisioning and requirement analysis [1.7] · *Single-Answer Multiple Choice*

A Chief Medical Officer states: `"Improve discharge coordination across wards."` Which version converts this wish into a valid architectural success criterion?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Defining baseline-backed `SMART` success KPIs (cycle-time reduction, error-rate drop, SLA adherence, & active adoption %)
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Rewriting vague goals into baseline-anchored `SMART` KPIs (such as reducing post-acute discharge delay from `18 hours` to `< 3 hours` and cutting readmission-form errors below `0.5%` within 90 days) enables objective validation. [Skill 1.7: Review and validate measurable key success criteria, KPIs, and adoption targets | Source: Review measurable key success criteria, KPIs, and adoption targets (https://learn.microsoft.com/en-us/power-platform/guidance/adoption/measure-business-value)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Correct. Quantifiable KPIs anchored to current-state baselines let stakeholders verify objective ROI after go-live.
- **D:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.

</details>

### Q003 (`E2Q079`) — Architect a solution [2.16] · *Single-Answer Multiple Choice*

Hospital compliance demands that even if Microsoft support opens a severity-A diagnostic ticket, no Microsoft engineer can access Dataverse PHI until the Hospital CISO explicitly approves a time-bound request. Enabling `____` in Power Platform admin center enforces this.

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). **Microsoft Purview Customer Lockbox for Power Platform** requires explicit customer approval (and logs every audit event) before Microsoft engineers can access customer data during support escalations. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.

</details>

### Q004 (`E2Q007`) — Perform solution envisioning and requirement analysis [1.3] · *Single-Answer Multiple Choice*

A surgical device manufacturer needs FDA `21 CFR Part 11` dual-factor electronic signatures with tamper-evident audit seals on Dataverse corrective-action (`CAPA`) approvals within 6 weeks. What should the Solution Architect recommend first?

- **A.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **B.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Selecting a vetted Microsoft AppSource ISV Managed Solution certified for FDA `21 CFR Part 11` compliance delivers validated audit seals with lower risk and TCO than custom cryptography. [Skill 1.3: Identify and select components from existing apps, Dynamics 365, AppSource ISVs, and Azure | Source: Evaluate Dynamics 365 apps, AppSource ISVs, and Azure extensions (https://learn.microsoft.com/en-us/training/modules/discover-customer-needs/)]

- **A:** Correct. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **B:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q005 (`E2Q001`) — Perform solution envisioning and requirement analysis [1.1] · *Ordered Sequence (Multiple Choice)*

A pediatric hospital network is replacing fragmented patient-referral trackers with Microsoft Power Platform and asks you to sequence solution envisioning through Well-Architected target-design alignment. Which four-step order should you recommend?

- **A.** Capture business outcomes, KPIs, & risk constraints → Map current-state processes & existing enterprise systems → Refine functional & non-functional requirements → Align target architecture to Power Platform Well-Architected pillars
- **B.** Copy every legacy Access table 1-for-1 into Dataverse → Replicate broken manual steps verbatim → Ignore API and storage limits → Run fit/gap analysis during user acceptance testing
- **C.** Grant System Administrator to all stakeholders → Build prototypes in personal My Flows → Skip security & residency discovery → Export Unmanaged Default Solution to Production
- **D.** Write custom C# plug-ins on Day 1 → Purchase all Dynamics 365 licenses blindly → Skip current-state discovery → Capture non-functional requirements after Production go-live

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Healthcare envisioning defines measurable clinical outcomes and HIPAA risk bounds first, maps existing referral workflows/EHR systems, captures functional & NFR specs, and aligns trade-offs to Power Platform Well-Architected pillars. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Correct. Solution envisioning establishes measurable business outcomes and risks first, inventories current processes/systems, refines functional & NFR specs, and aligns design trade-offs to Well-Architected pillars.
- **B:** Incorrect. Lifting and shifting broken legacy schemas without process optimization or fit/gap analysis perpetuates technical debt.
- **C:** Incorrect. Prototyping in Default Solution with over-privileged accounts violates governance and creates un-deployable artifacts.
- **D:** Incorrect. Coding or buying licenses before discovery and NFR capture causes costly rework and architectural mismatches.

</details>

### Q006 (`E2Q061`) — Architect a solution [2.8] · *Single-Answer Multiple Choice*

Hospital networks follow a 4-tier tree (`Health System -> Region -> Hospital Campus -> Outpatient Clinic`), and executives want native visual tree cards plus `Under` OData rollup queries. Which relationship pattern should you configure?

- **A.** Modeling self-referential `Hierarchical` (`1:N` `Under` queries) and `Polymorphic` (`Customer` / multi-table) relationships
- **B.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **C.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enabling a self-referential `1:N` **Hierarchical** relationship on the facility/Account table unlocks native hierarchy visualizations, `Under` / `Not Under` query operators, and rollup aggregations. [Skill 2.8: Design Dataverse relationships (1:N, N:N, hierarchical, polymorphic) and cascading behaviors | Source: Design Dataverse relationships (1:N, N:N, hierarchical) & cascading behaviors (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Correct. Hierarchical relationships support native visual hierarchy rollups and `Under` OData operators across parent-child trees.
- **B:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **C:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q007 (`E2Q042`) — Perform solution envisioning and requirement analysis [1.16] · *Single-Answer Multiple Choice*

A finance analyst asks whether 900 technicians with standalone Power Apps licenses can create and update standard Dynamics 365 `msdyn_workorder` rows directly. Which rule governs `msdyn_workorder`?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Validating Dynamics 365 restricted-table licensing (`Case / incident`, `Work Order`, `Entitlement`) during fit/gap analysis
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Work Order` (`msdyn_workorder`) is a Dynamics 365 **restricted table** requiring appropriate Dynamics 365 Field Service (or qualifying attach) licenses for full CRUD access. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Correct. Restricted Dynamics 365 tables require appropriate Dynamics 365 licenses for CRUD operations rather than standalone Power Apps licenses.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q008 (`E2Q012`) — Perform solution envisioning and requirement analysis [1.5] · *Single-Answer Multiple Choice*

Analyzing six months of timestamped case-state audit logs (`Case_ID`, `Activity_Name`, `Start_Time`, `End_Time`) to generate a visual bottleneck Variant Map uses `____`.

- **A.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Power Automate Process Mining & Task Mining paired with cross-functional current-state discovery workshops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate Process Mining ingests event logs (`Case ID`, `Activity`, `Timestamp`) to render process maps, loop variants, and cycle-time bottlenecks automatically. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Correct. Combining telemetry-driven Process/Task Mining with SME workshops exposes hidden rework loops and shadow processes objectively.

</details>

### Q009 (`E2Q027`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

A nursing director emails: `"Add 16 color-coded subgrids and a blinking banner on the Bed Board form."` How should the Solution Architect refine this request?

- **A.** Refining prescriptive wishes into persona-based `User Stories` (`As a ... I need ... so that ...`) with testable Acceptance Criteria
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Translating UI-prescriptive wishes into persona-based `User Stories` (`As a Charge Nurse, I need immediate sepsis-escalation visibility so high-acuity beds are prioritized`) with testable Acceptance Criteria uncovers true clinical intent. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Correct. Outcome-oriented User Stories decouple business intent from premature UI assumptions and anchor QA test cases.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q010 (`E2Q054`) — Architect a solution [2.4] · *Single-Answer Multiple Choice*

Phlebotomists walking hospital floors only scan wristband + vial barcodes in 4 seconds, whereas lab directors review 18 quality subgrids at desktop workstations. Splitting these experiences exemplifies `____`.

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Grouping capabilities into role- and task-specific apps (offline Canvas for field crews, Model-driven for back-office, Power Pages for externals)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Role- and task-based app grouping tailors a minimalist barcode Canvas app to phlebotomists and a rich Model-driven app to lab directors over the same Dataverse tables. [Skill 2.4: Design apps by grouping required features based on persona, role, task, and offline needs | Source: Design role-based and task-based app experiences across form factors (https://learn.microsoft.com/en-us/power-apps/guidance/planning/app-design)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Correct. Task-focused apps per persona outperform bloated one-size-fits-all apps in load speed, offline footprint, and usability.

</details>

### Q011 (`E2Q095`) — Implement the solution [3.6] · *Ordered Sequence (Multiple Choice)*

Nine hospitals cut over to HavenBridge’s consolidated Dataverse Production environment at 22:00 Saturday. Which four-step execution sequence guarantees zero concurrent user edits during final delta load and Managed Upgrade?

- **A.** Delete existing Managed Solutions in Production (erasing live tables!) → Re-import from scratch → Manually re-type Connection References & Environment Variables → Disable backups
- **B.** Allow 5,000 users to edit records during live schema upgrade and migration → Import Unmanaged solutions into Production → Skip smoke tests → Turn on auditing two months later
- **C.** Freeze changes & verify backup restore point → Enable Dataverse `Administration mode` (blocking regular users & async jobs) → Apply Managed Upgrades & run validated delta loads → Exit `Administration mode`, smoke-test, & monitor hypercare
- **D.** Ignore Dataverse Database/File storage overages blocking admin ops → Skip Solution Checker critical findings → Leave Dev URLs in Environment Variables → Disband support team at launch minute

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Verifying backups, engaging Dataverse `Administration mode` (blocking regular users & async jobs), applying Managed Upgrades + validated delta loads, and exiting `Administration mode` after smoke tests ensures safe cutover. [Skill 3.6: Escalate and resolve data migration bottlenecks (BypassCustomPluginExecution, delta loads, reconciliation) | Source: Escalate and remediate enterprise data migration bottlenecks and cutover issues (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/TVF-override-plugin-execution)]

- **A:** Incorrect. Deleting a Managed Solution erases its custom Dataverse tables and production data; always use Managed `Stage for upgrade` -> `Apply upgrade`.
- **B:** Incorrect. Concurrent user edits during cutover cause migration collisions, lock timeouts, and inconsistent business state.
- **C:** Correct. Controlled cutovers establish restore points, engage `Administration mode` to prevent user writes and background noise, apply Managed Upgrades + delta loads, validate smoke tests, and transition to monitored hypercare.
- **D:** Incorrect. Exceeded Dataverse storage entitlements block environment copy/restore/admin operations and sabotage cutover readiness.

</details>

### Q012 (`E2Q093`) — Implement the solution [3.5] · *Single-Answer Multiple Choice*

Nurses report a Canvas intake screen freezes for 16 seconds because a gallery runs `Filter(Patients, Lower(LastName) in txtSearch.Text)` over 400,000 rows and calls `LookUp(Wards, ...)` per row. Proposed solution: Refactor the gallery to use delegable `StartsWith(LastName, txtSearch.Text)` over an indexed Dataverse view and eliminate `N+1` per-row `LookUp`s. Does this resolve the bottleneck?

- **A.** Fixing slowness via delegable `Filter`/`StartsWith` Canvas queries, indexed `Quick Find` columns (no leading `*` wildcards), & async plug-in refactoring
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Yes — replacing non-delegable `Lower(...) in ...` predicates with delegable `StartsWith(LastName, txtSearch.Text)` over indexed Dataverse views and pre-fetching/joining `Wards` eliminates client-side row truncation and `N+1` network chatter. [Skill 3.5: Identify and resolve Canvas, Model-driven, Quick Find index, and synchronous plug-in performance issues | Source: Identify and resolve Canvas, Model-driven, Dataverse, & plug-in performance issues (https://learn.microsoft.com/en-us/power-platform/well-architected/performance-efficiency/overview)]

- **A:** Correct. Eliminating `N+1` gallery `LookUp`s, non-delegable predicates, leading-wildcard full table scans, and chained sync plug-ins restores sub-second UX.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q013 (`E2Q022`) — Perform solution envisioning and requirement analysis [1.9] · *Ordered Sequence (Multiple Choice)*

A healthcare payer stores member eligibility in Facets Core, provider credentials in SQL Server, and appeals spreadsheets on file shares. In what sequence should you evaluate these sources before modeling Dataverse?

- **A.** Inventory candidate enterprise data sources & owners → Classify data sensitivity, residency, & compliance rules → Assess data quality, volume, & latency needs → Decide per entity whether to connect in place or replicate into Dataverse
- **B.** Duplicate 100% of ERP tables into Dataverse nightly → Ignore master-data ownership → Allow dual uncoordinated edits without conflict rules → Cleanse duplicates manually after go-live
- **C.** Expose on-premises SQL Server ports directly to the public internet → Share one SQL `sa` login across Canvas apps → Skip data classification → Disable Dataverse auditing
- **D.** Email daily CSV exports between departments → Let business units invent conflicting customer IDs → Skip deduplication standards → Import dirty spreadsheets straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Inventorying owners first, classifying HIPAA/PHI sensitivity and residency, assessing quality/volume/latency, and then selecting virtual in-place access vs Dataverse replication prevents shadow master drift. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Correct. Architects identify authoritative systems of record first, classify regulatory sensitivity/residency, evaluate quality/volume/latency, and then choose virtual in-place access vs Dataverse replication.
- **B:** Incorrect. Blindly duplicating authoritative ERP tables without master-data ownership or conflict governance causes severe data drift.
- **C:** Incorrect. Exposing raw database ports and sharing `sa` logins violates zero-trust security and bypasses Dataverse governance.
- **D:** Incorrect. Manual CSV emailing without canonical keys or data quality standards corrupts downstream analytics and automations.

</details>

### Q014 (`E2Q004`) — Perform solution envisioning and requirement analysis [1.2] · *Multi-Select (Select 2)*

An oncology research institute wants: (1) an external authenticated portal where 65,000 trial volunteers complete weekly symptom questionnaires stored in Dataverse, and (2) an automated extraction step inside cloud flows that parses faxed lab referral PDFs. Which two Power Platform components should you choose? Select two.

- **A.** AI Builder prebuilt/custom document processing, text classification, & AI Prompts integrated natively in Power Platform
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **E.** Model-driven Power App over Microsoft Dataverse with responsive forms, views, dashboards, & Business Process Flows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). Microsoft Power Pages securely authenticates 65,000 external trial volunteers via `Table Permissions`, while AI Builder document processing extracts structured fields from faxed lab PDFs natively. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Correct. AI Builder embeds governed document extraction and generative AI prompts directly inside flows and apps without custom ML infrastructure.
- **B:** Correct. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **E:** Incorrect. Model-driven apps excel at structured, data-dense back-office case and lifecycle management directly atop Dataverse security.

</details>

### Q015 (`E2Q050`) — Architect a solution [2.2] · *Single-Answer Multiple Choice*

Triage coordinators inside a Model-driven app need a full-screen, pixel-custom multi-step intake wizard pulling data from three connectors simultaneously. Building a responsive `____` inside the Model-driven app meets this need natively.

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Addressing gaps via supported extensibility (`Custom Pages`, `PCF`, `Power Fx Formula columns`, `Custom APIs`) over bespoke clones
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Model-driven **`Custom Pages`** combine Canvas pixel-level layout flexibility and multi-connector Power Fx expressions directly inside Model-driven app navigation and dialogs. [Skill 2.2: Identify app customization approaches and validate interactive user experience prototypes | Source: Select customization approaches for existing apps and validate UX prototypes (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/design-consistency)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Correct. Supported platform extensibility closes UX and logic gaps while preserving Microsoft wave-update compatibility.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.

</details>

### Q016 (`E2Q059`) — Architect a solution [2.7] · *Multi-Select (Select 2)*

A pharmacy system must: (1) roll back saving a `Prescription` row immediately within the same database transaction if a lethal drug-allergy conflict exists locally in Dataverse, and (2) send ANSI `X12 837` EDI claims to clearinghouses over private VNet compute. Which two automation components should you select? Select two.

- **A.** Azure Logic Apps (Standard) for enterprise B2B EDI (`X12`/`AS2`/`EDIFACT`), VNet-isolated single-tenant workflows, & Azure Bicep ALM
- **B.** Synchronous Dataverse plug-ins (`<= 2m`) strictly for atomic transaction validation/rollback; Cloud Flows / Logic Apps for async orchestration
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **E.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). A fast synchronous Dataverse plug-in enforces atomic drug-allergy rollback (`auto_sync_vs_async`), while **Azure Logic Apps (Standard)** processes `X12 837` B2B EDI claims inside VNet-isolated single-tenant compute (`auto_logic_apps`). [Skill 2.7: Design automation strategies (sync vs async, BPF, Logic Apps) and multi-environment ALM topology | Source: Design automation & multi-environment strategies (CoE Starter Kit & ALM) (https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit)]

- **A:** Correct. Logic Apps Standard complements Power Automate when Azure RBAC, private VNet compute, or B2B Enterprise Integration Pack codecs are required.
- **B:** Correct. Keeping synchronous transaction pipelines fast and offloading external orchestrations asynchronously protects Dataverse SQL responsiveness.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **E:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

## Case Study Vignette — MedVantage Imaging Services

> MedVantage Imaging Services dispatches 900 MRI field engineers and tracks IoT helium-pressure alerts spiking to 15,000 telemetry events/minute. Architects must evaluate Dynamics 365 Field Service vs custom building, absorb high-velocity ephemeral telemetry without blowing Dataverse relational storage, and integrate SAP S/4HANA parts inventory.

### Q017 (`E2Q041`) — Perform solution envisioning and requirement analysis [1.16] · *Single-Answer Multiple Choice*

Case study — MedVantage Imaging Services: MedVantage Imaging Services dispatches 900 MRI field engineers requiring Preventive Maintenance plans, SLA entitlements, van-parts inventory, and route optimization. Should MedVantage build custom `new_workorder` tables on Power Apps or adopt Dynamics 365 Field Service?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Dynamics 365 first-party app (`Sales`, `Customer Service`, or `Field Service`) leveraging native schemas, SLAs, & RSO scheduling

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Adopting **Dynamics 365 Field Service** leverages native `msdyn_workorder` schemas, preventive-maintenance agreements, van inventory, offline mobile apps, and Resource Scheduling Optimization (`RSO`). [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Correct. Adopting Dynamics 365 first-party apps avoids reinventing complex case routing, omnichannel queues, or Resource Scheduling Optimization.

</details>

### Q018 (`E2Q065`) — Architect a solution [2.10] · *Multi-Select (Select 2)*

Case study — MedVantage Imaging Services: MedVantage MRI scanners burst 15,000 ephemeral helium-pressure JSON pings per minute (needed for 14 days only), and engineers also attach 25 MB diagnostic log bundles while requiring regional BU ownership on `Service_Asset` rows. Which two data-model choices fit best? Select two.

- **A.** Choosing `User or Team` table ownership for BU/row/team security vs `Organization` ownership for global config tables at creation time
- **B.** Dataverse `Elastic tables` (Cosmos DB horizontal partitioning + `TTL`) for high-velocity telemetry, and `File`/SharePoint/Blob offloading for binaries
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **E.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). Dataverse **`Elastic tables`** (Cosmos DB horizontal partitioning + `TTL` 14-day auto-expiry) plus `File`/Azure Blob offloading (`tbl_elastic_activity`) handle telemetry bursts and 25 MB bundles, while `User or Team` ownership (`tbl_ownership_choice`) supports regional BU security. [Skill 2.10: Design complex data models (ownership immutability, Elastic/Activity tables, binary storage offloading) | Source: Design complex data models (ownership, Elastic/Activity tables, storage capacity) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/elastic-tables)]

- **A:** Correct. Table ownership (`User/Team` vs `Organization`) is immutable once created and determines whether BU, Team, and Hierarchy security apply.
- **B:** Correct. Elastic tables ingest tens of thousands of ephemeral JSON/IoT writes per minute with automatic `TTL` expiry without relational index contention.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **E:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).

</details>

### Q019 (`E2Q070`) — Architect a solution [2.12] · *Single-Answer Multiple Choice*

Case study — MedVantage Imaging Services: MedVantage must synchronize MRI spare-parts reservations from Dataverse `Work Orders` to SAP S/4HANA reliably even when SAP undergoes 4-hour weekend patching windows. Which integration pattern prevents lost reservations and Dataverse timeouts?

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **D.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Publishing Dataverse parts-reservation events asynchronously to **Azure Service Bus** (with FIFO sessions and Dead-Letter Queues) fronted by **APIM** buffers orders safely throughout SAP maintenance windows. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **D:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.

</details>

### Q020 (`E2Q073`) — Architect a solution [2.13] · *Single-Answer Multiple Choice*

A county behavioral-health billing system runs on a 2004 Windows desktop thick client with zero APIs, while Dataverse Production requires `28-day` point-in-time backup retention and automated desktop queue retries. Which design covers both requirements?

- **A.** Designing BCDR around Dataverse point-in-time backups (`28-day` Prod retention, cross-Geo failover limits) and `Hosted RPA` + `Work Queues` for legacy UI
- **B.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **C.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Dataverse’s managed geo-redundant Azure SQL backups (`28-day` Production point-in-time restore) plus **Power Automate Hosted RPA** backed by **Work Queues** satisfy both BCDR and resilient legacy UI automation. [Skill 2.13: Design authentication (OBO vs S2S, Managed Identity), BCDR (RPO/RTO, geo-backups), and RPA | Source: Design authentication (OBO vs S2S, Managed Identity), BCDR, and RPA architectures (https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments)]

- **A:** Correct. Architects align RPO/RTO to Microsoft’s managed geo-replication SLAs and isolate UI-only legacy integrations behind resilient RPA Work Queues.
- **B:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **C:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q021 (`E2Q058`) — Architect a solution [2.6] · *Single-Answer Multiple Choice*

Epidemiologists need executive trend reports combining Dataverse infection cases, Epic Clarity warehouse tables, and CDC population datasets with dynamic **Row-Level Security (`RLS`)** by hospital region. Which visualization architecture should you design?

- **A.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). **Power BI** (backed by `Microsoft Fabric Link` / `Azure Synapse Link` and Entra SSO `RLS`) blends Dataverse and external clinical warehouses without taxing transactional Dataverse SQL. [Skill 2.6: Design data visualization strategies across Dataverse charts, Power BI RLS, and Fabric/Synapse Link | Source: Design data visualization (Dataverse charts, Power BI RLS, Fabric/Synapse Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-synapse)]

- **A:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Correct. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.

</details>

### Q022 (`E2Q003`) — Perform solution envisioning and requirement analysis [1.1] · *Single-Answer Multiple Choice*

Clinical triage nurses suffered severe alert fatigue in an older portal that forced 19 screen hops per admission. Redesigning cohesive, low-friction, task-aligned persona journeys maps directly to the Well-Architected `____` pillar.

- **A.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)
- **B.** Power Platform Well-Architected `Security` pillar (Zero Trust Entra identity, least privilege, DLP, & encryption)
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Power Platform Well-Architected `Operational Excellence` pillar (automated ALM pipelines, Application Insights, & CoE)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). The Power Platform Well-Architected `Experience Optimization` pillar centers on task-focused layouts, reduced cognitive load, accessibility, and cohesive persona flows. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Correct. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.
- **B:** Incorrect. The Security pillar protects confidentiality and integrity through Entra Conditional Access, least-privilege roles, DLP endpoint rules, and CMK/Lockbox.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Operational Excellence standardizes CI/CD solution pipelines, automated Solution Checker gates, telemetry, and Managed Environment governance.

</details>

### Q023 (`E2Q025`) — Perform solution envisioning and requirement analysis [1.10] · *Single-Answer Multiple Choice*

Nine regional hospital databases store `Gender`, `Discharge_Disposition`, and `Payer_Type` using incompatible integer codes, and 14% of patient rows share duplicate `MRN` numbers. What must precede data migration build?

- **A.** Defining pre-cutover data quality standards (deduplication keys, mandatory completeness, referential integrity, & domain mappings)
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Establishing pre-migration data quality rules (EMPI/`MRN` deduplication survivorship, canonical HL7 option-set crosswalks, and mandatory completeness gates) prevents corrupt clinical merges. [Skill 1.10: Define use cases and data quality standards for existing data prior to migration or integration | Source: Define use cases and data quality standards for existing data (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Correct. Enforcing cleansing and deduplication gates before migration prevents garbage-in/garbage-out failures in Dataverse.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q024 (`E2Q062`) — Architect a solution [2.8] · *Single-Answer Multiple Choice*

A `Clinical_Note` table has a `Parental` `1:N` relationship from `Patient`. Whenever a `Patient` row moves to a new primary clinician, 40,000 historical notes synchronously re-assign and share, causing timeouts. Proposed solution: Switch the relationship behavior to `Custom` and set `Reparent`, `Assign`, and `Share` cascading to `Cascade None` (or `Cascade Active` only where required). Does this fix the issue?

- **A.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **B.** Configuring `Custom` / `Referential` cascading (avoiding unintended `Parental` `Cascade All` reparent storms) and manual `N:N` intersect tables
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes — replacing `Parental` (`Cascade All`) with tailored `Custom` cascading stops synchronous mass updates and `POA` sharing storms across historical clinical notes. [Skill 2.8: Design Dataverse relationships (1:N, N:N, hierarchical, polymorphic) and cascading behaviors | Source: Design Dataverse relationships (1:N, N:N, hierarchical) & cascading behaviors (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **B:** Correct. Replacing `Parental` cascading on high-volume child tables prevents `POA` sharing storms, and manual `N:N` tables store rich relationship attributes.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q025 (`E2Q045`) — Perform solution envisioning and requirement analysis [1.18] · *Multi-Select (Select 2)*

Midway through Sprint 4 of a 5-sprint HIPAA compliance deadline, hospital marketing asks to add an alumni fundraising module and event-ticketing portal to Release 1. Which two actions should the Solution Architect take? Select two.

- **A.** Scoping a high-value `MVP` Phase 1 release using MoSCoW prioritization and formal change-request governance
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **E.** Establishing a fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E` (`CSV: 1,5`)

Correct answers: A and E (are correct). Enforcing the `MVP` Release 1 boundary via MoSCoW prioritization (`scope_mvp_phased`) and routing non-HIPAA marketing features to Phase 2 through the Change Control / ARB board (`disc_raci_governance`) protects the regulatory launch date. [Skill 1.18: Determine MVP vs phased solution scope boundaries and govern scope changes | Source: Determine MVP vs phased solution scope and manage scope boundaries (https://learn.microsoft.com/en-us/training/paths/become-solution-architect/)]

- **A:** Correct. Phased MVP delivery de-risks go-live, delivers early business value, and prevents uncontrolled scope creep.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **E:** Correct. Clear architectural ownership, ARB design gates, and CoE guardrails align business, citizen makers, pro-devs, and InfoSec.

</details>

### Q026 (`E2Q069`) — Architect a solution [2.12] · *Multi-Select (Select 3)*

A regional hospital hub integrates Dataverse with Epic FHIR APIs, SAP supply chain, and external lab webhooks. Which three architectural elements create a resilient, governed enterprise integration layer? Select three.

- **A.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources
- **B.** Defining solution-aware Dataverse `Custom APIs` exposing strongly typed request/response contracts for internal and external callers
- **C.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **E.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`
- **F.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B, E` (`CSV: 1,2,5`)

Correct answers: A, B, and E (are correct). `Azure API Management` + `Azure Service Bus` / `Event Grid` (`integ_async_asb_apim`), strongly typed Dataverse `Custom APIs` (`integ_custom_api`), and private `VNet` subnet delegation / `On-Premises Data Gateway` clusters (`net_vnet_er_opdg`) deliver governed, private, resilient integrations. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Correct. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.
- **B:** Correct. Custom APIs replace legacy Custom Process Actions with code-first, solution-aware OData bound/unbound operations and granular privilege checks.
- **C:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **E:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.
- **F:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q027 (`E2Q082`) — Architect a solution [2.17] · *Single-Answer Multiple Choice*

An outpatient portal built on Power Pages serves 420,000 patients viewing their own immunization records linked to their `Contact` row. Proposed solution: Authenticate patients via `Microsoft Entra External ID` and enforce `Contact`-scoped `Table Permissions` mapped to an authenticated `Web Role`. Does this meet security best practices?

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **C.** Enforcing `DLP` + `Endpoint Filtering`, licensing external consumers via `Power Pages` (`Entra External ID`), & `Entra B2B` for internal-app guests
- **D.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — Power Pages `Table Permissions` (`Contact` scope) + `Web Roles` + `Entra External ID` enforce server-side Dataverse row isolation for hundreds of thousands of external patients. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **C:** Correct. Power Pages scales cost-effectively with `Table Permissions` for external portals, whereas Entra B2B suits external partners using internal apps.
- **D:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.

</details>

### Q028 (`E2Q021`) — Perform solution envisioning and requirement analysis [1.8] · *Single-Answer Multiple Choice*

An acquired radiology group still authenticates staff in `radiology-legacy.onmicrosoft.com` while Dataverse runs in `havenbridge.onmicrosoft.com`. Mapping identity federation, `Entra B2B` trust, and licensing rules belongs in `____`.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Enterprise Architecture Context Diagram mapping systems of record, Entra tenants, hybrid networks, & sync/async SLAs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Evaluating multi-tenant Entra identity boundaries and cross-tenant Conditional Access policies is a foundational part of enterprise architecture landscape analysis. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Correct. Evaluating the enterprise landscape clarifies authoritative boundaries, identity federation, firewall paths, and integration patterns.

</details>

### Q029 (`E2Q043`) — Perform solution envisioning and requirement analysis [1.17] · *Multi-Select (Select 2)*

Clinicians need: (1) a calculated risk-tier badge computed automatically across related Dataverse columns without C# code, and (2) an interactive anatomical body-map selector embedded on a Model-driven form. Which two supported gap-resolution patterns should you recommend? Select two.

- **A.** Validating interactive UX prototypes (`Figma-to-App` / `Custom Pages`) early and building `PCF` controls for specialized UI gaps
- **B.** Addressing gaps via supported extensibility (`Custom Pages`, `PCF`, `Power Fx Formula columns`, `Custom APIs`) over bespoke clones
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **E.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). **Power Fx Formula columns** (`gap_lowcode_alt`) compute cross-column risk badges declaratively, while a **Power Apps Component Framework (`PCF`)** control (`ux_proto_pcf`) renders the interactive SVG body-map selector natively. [Skill 1.17: Address functional gaps through supported low-code/pro-code alternate solutions | Source: Address functional gaps through low-code/pro-code alternate solutions (https://learn.microsoft.com/en-us/power-platform/well-architected/operational-excellence/overview)]

- **A:** Correct. Interactive prototyping validates user journeys cheaply, while Power Apps Component Framework (`PCF`) renders reusable custom TypeScript/React controls.
- **B:** Correct. Supported platform extensibility closes UX and logic gaps while preserving Microsoft wave-update compatibility.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **E:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q030 (`E2Q094`) — Implement the solution [3.5] · *Single-Answer Multiple Choice*

To correlate slow Model-driven form `onLoad` scripts, UCI network latency, and failing C# plug-in `ITracingService` exceptions in a single KQL workspace before go-live, you should enable `____`.

- **A.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **B.** Running scale tests in UAT while streaming Dataverse and Canvas telemetry to `Azure Application Insights` (`dependencies` / `exceptions` KQL)
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Exporting Dataverse and Power Apps telemetry to **Azure Application Insights** surfaces correlated form load times, custom script durations, plug-in traces, and dependency failures via KQL. [Skill 3.5: Identify and resolve Canvas, Model-driven, Quick Find index, and synchronous plug-in performance issues | Source: Identify and resolve Canvas, Model-driven, Dataverse, & plug-in performance issues (https://learn.microsoft.com/en-us/power-platform/well-architected/performance-efficiency/overview)]

- **A:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **B:** Correct. Application Insights integration captures page-load latency, plug-in execution durations, and outbound dependency failures under realistic concurrency.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q031 (`E2Q056`) — Architect a solution [2.5] · *Single-Answer Multiple Choice*

Clinical triage Business Rules reference specific `Acuity_Level` lookup rows by GUID across Dev, QA, UAT, and Prod, while `ADF` pipelines upsert `Patient` rows using external `MRN` numbers. Which tooling combination solves both requirements?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Staging cleansed records via `ADF` / `SSIS` using Dataverse `Alternate Keys` (`Upsert`) and `Configuration Migration Tool` for fixed-GUID config rows
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Using the **Configuration Migration Tool (`CMT`)** preserves identical `Acuity_Level` GUIDs across environments, while **Dataverse Alternate Keys** on `MRN` enable fast `ADF` upserts without GUID pre-lookups. [Skill 2.5: Design enterprise data migration strategies, load sequencing, Alternate Keys, and CMT tooling | Source: Design enterprise data migration strategies, load order, and tooling (https://learn.microsoft.com/en-us/power-platform/admin/create-schema-export-data)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Correct. Alternate Keys eliminate GUID pre-lookup round-trips on upserts, while CMT preserves exact reference-record GUIDs across Dev/UAT/Prod.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q032 (`E2Q087`) — Implement the solution [3.2] · *Single-Answer Multiple Choice*

A maker needs to block unauthorized technicians from reading restricted patient `SSN` columns over Power BI and `/api/data/v9.2/`. Proposed solution: Create a Business Rule with scope set to `All Forms` that hides the `SSN` field. Does this secure the data boundary?

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Auditing server-side `Security Roles`, `Column Security`, & `Power Pages Table Permissions` rather than trusting client-side UI rules
- **C.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). No — `All Forms` Business Rules execute purely in Model-driven client browser scripts and provide **zero** server-side security over Web API, TDS, Excel export, or Power BI; server-side `Security Roles` and `Column Security Profiles` are required. [Skill 3.2: Review security across Business Rules, Security Roles, Entra Conditional Access, & security boundaries | Source: Review end-to-end security across Business Rules, Roles, Entra ID, & boundaries (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Correct. Client JavaScript and `Form`-scoped Business Rules never block Web API/OData access; security boundaries must be enforced server-side in Dataverse.
- **C:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q033 (`E2Q086`) — Implement the solution [3.2] · *Multi-Select (Select 2)*

A pre-go-live HIPAA security audit finds that a Power Pages `Entity List` exposed all clinics’ patients because `Enable Table Permissions` was unchecked, and a Model-driven form used JavaScript `setVisible(false)` to hide `SSN`. Which two fixes are required? Select two.

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Auditing server-side `Security Roles`, `Column Security`, & `Power Pages Table Permissions` rather than trusting client-side UI rules
- **D.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access
- **E.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, D` (`CSV: 3,4`)

Correct answers: C and D (are correct). Enforcing server-side **Power Pages `Table Permissions`** (`val_sec_boundary_audit`) and protecting `SSN` with a Dataverse **`Column Security Profile`** (`sec_col_hier_pim`) secure both OData portal feeds and Web API/Excel exports. [Skill 3.2: Review security across Business Rules, Security Roles, Entra Conditional Access, & security boundaries | Source: Review end-to-end security across Business Rules, Roles, Entra ID, & boundaries (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Correct. Client JavaScript and `Form`-scoped Business Rules never block Web API/OData access; security boundaries must be enforced server-side in Dataverse.
- **D:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.
- **E:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.

</details>

### Q034 (`E2Q053`) — Architect a solution [2.4] · *Single-Answer Multiple Choice*

A health system currently forces ambulance paramedics, billing coders, and external patients to share a single giant Canvas app. What app-grouping architecture should you recommend?

- **A.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **D.** Grouping capabilities into role- and task-specific apps (offline Canvas for field crews, Model-driven for back-office, Power Pages for externals)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Grouping features by persona and context — a lightweight offline Canvas app for paramedics, a Model-driven app for billing coders, and Power Pages for external patients — maximizes speed, security, and licensing efficiency. [Skill 2.4: Design apps by grouping required features based on persona, role, task, and offline needs | Source: Design role-based and task-based app experiences across form factors (https://learn.microsoft.com/en-us/power-apps/guidance/planning/app-design)]

- **A:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **D:** Correct. Task-focused apps per persona outperform bloated one-size-fits-all apps in load speed, offline footprint, and usability.

</details>

### Q035 (`E2Q055`) — Architect a solution [2.5] · *Ordered Sequence (Multiple Choice)*

During hospital consolidation, you must migrate 2.8 million Patients, Encounters, and circular Primary-Care-Provider lookups into Dataverse without firing patient SMS flows or breaking reference-table GUIDs across environments. Which sequence should you execute?

- **A.** Execute `INSERT INTO account` over Dataverse TDS port 5558 → Remove platform SQL foreign keys → Copy `.mdf` database files from Azure SQL → Reboot the tenant
- **B.** Cleanse & stage data with Alternate Keys / CMT GUIDs → Suppress non-essential flows & custom plug-ins → Load parent tables first (deferring circular lookups) → Bind deferred lookups, reconcile counts, & re-enable automations
- **C.** Load child line-items before parent Account rows exist → Leave all welcome-email cloud flows enabled → Run single-row serial inserts with no batching → Fix orphaned lookups manually in Prod
- **D.** Let each environment generate random GUIDs for reference/configuration tables → Hardcode Dev GUIDs inside cloud flows → Import raw unvalidated CSVs → Skip reconciliation

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Cleansing/staging with Alternate Keys & CMT fixed GUIDs, suppressing flows & custom plug-ins, loading parent tables first (deferring circular lookups), and binding deferred lookups before reconciling counts ensures clean clinical cutover. [Skill 2.5: Design enterprise data migration strategies, load sequencing, Alternate Keys, and CMT tooling | Source: Design enterprise data migration strategies, load order, and tooling (https://learn.microsoft.com/en-us/power-platform/admin/create-schema-export-data)]

- **A:** Incorrect. Dataverse’s TDS endpoint (`5558`) is strictly read-only; all writes must use Dataverse Web API/SDK, Dataflows, ADF, or Configuration Migration Tool.
- **B:** Correct. Enterprise migrations stage cleansed data, suppress noisy automations (`BypassCustomPluginExecution`), load parents before children while resolving circular lookups in a second pass, and reconcile counts before re-enabling flows.
- **C:** Incorrect. Loading child rows first fails referential integrity, and leaving notification flows active spams thousands of customers.
- **D:** Incorrect. Mismatched reference-data GUIDs across Dev, UAT, and Prod break business rules, views, and workflow conditions.

</details>

### Q036 (`E2Q060`) — Architect a solution [2.7] · *Single-Answer Multiple Choice*

An oncology tumor-board case progresses through `Referral -> Pathology Review -> Board Consensus -> Treatment Plan` across two Dataverse tables with mandatory sign-off columns per stage. Configuring `____` enforces this guided human workflow.

- **A.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **B.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A multi-table **Business Process Flow (`BPF`)** enforces stage-gated field capture and conditional clinical branching across linked Dataverse tables. [Skill 2.7: Design automation strategies (sync vs async, BPF, Logic Apps) and multi-environment ALM topology | Source: Design automation & multi-environment strategies (CoE Starter Kit & ALM) (https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit)]

- **A:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **B:** Correct. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q037 (`E2Q075`) — Architect a solution [2.14] · *Single-Answer Multiple Choice*

InfoSec mandates that stolen browser session cookies from home PCs cannot be replayed against Dataverse Production outside approved hospital egress NAT IPs. Which configuration enforces this network boundary?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Enforcing `Microsoft Entra Conditional Access` (MFA & compliant device) plus `Power Platform IP Firewall` & `Cookie IP binding`
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Combining **Microsoft Entra Conditional Access** (compliant managed device + MFA) with **Power Platform IP Firewall** and **IP cookie binding** inside Managed Environments blocks external session-token replay. [Skill 2.14: Assess VNet subnet delegation, Azure ExpressRoute nuances, Data Gateways, and IP firewall networking | Source: Assess VNet integration, Azure ExpressRoute, gateways, and IP firewall networking (https://learn.microsoft.com/en-us/power-platform/admin/vnet-support-overview)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Correct. Combining Entra Conditional Access with Managed Environment IP Firewall and session cookie binding blocks token replay from untrusted networks.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.

</details>

### Q038 (`E2Q080`) — Architect a solution [2.16] · *Single-Answer Multiple Choice*

Chief Nursing Officers need read visibility into quality incidents across `Nurse Manager -> Charge Nurse -> Staff Nurse` positions regardless of whether individuals report across different HR cost centers. Configuring `____` models this cleanly.

- **A.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access
- **B.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Dataverse **Position Hierarchy Security** models functional clinical trees (`Nursing Director -> Nurse Manager -> Charge Nurse`) cleanly even when direct HR manager fields differ. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.
- **B:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q039 (`E2Q090`) — Implement the solution [3.3] · *Single-Answer Multiple Choice*

When Dataverse returns `HTTP 429` because a background worker exceeded the `20-minute` (`1,200,000 ms`) execution-time cap inside a 5-minute sliding window, which HTTP response header tells the client how many seconds to wait before retrying?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Conforming to `Dataverse Service Protection` limits (`6,000` req / `20m` compute per `5-min` window), pooling `S2S Application Users`, & honoring `Retry-After`
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Honor the HTTP **`Retry-After`** header (alongside monitoring `x-ms-ratelimit-time-remaining-xrm-requests` and `x-ms-ratelimit-burst-remaining-xrm-requests`) before re-sending requests. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Correct. Service Protection enforces per-user/per-web-server 5-minute sliding caps (`HTTP 429`); pooling S2S Application Users and respecting `Retry-After` maximizes throughput.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q040 (`E2Q072`) — Architect a solution [2.13] · *Single-Answer Multiple Choice*

When a physician opens a Custom Page that queries an internal `HL7 FHIR` medication-history API, federal HIPAA logs must record the **individual physician’s Entra UPN** rather than a shared app service account. Which authentication flow must you configure?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Using `OAuth 2.0 On-Behalf-Of (OBO)` to preserve caller identity/audit trails vs `Entra Service Principal (S2S)` / `Managed Identity` for background jobs
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Designing BCDR around Dataverse point-in-time backups (`28-day` Prod retention, cross-Geo failover limits) and `Hosted RPA` + `Work Queues` for legacy UI

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **`OAuth 2.0 On-Behalf-Of (OBO)`** delegated authentication passes the signed-in physician’s identity token through the custom connector/APIM to the FHIR API for per-clinician access control and HIPAA audit trails. [Skill 2.13: Design authentication (OBO vs S2S, Managed Identity), BCDR (RPO/RTO, geo-backups), and RPA | Source: Design authentication (OBO vs S2S, Managed Identity), BCDR, and RPA architectures (https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Correct. OBO propagates the signed-in user’s identity downstream for row-level authorization, whereas S2S/Managed Identity runs headless workloads.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Architects align RPO/RTO to Microsoft’s managed geo-replication SLAs and isolate UI-only legacy integrations behind resilient RPA Work Queues.

</details>

### Q041 (`E2Q011`) — Perform solution envisioning and requirement analysis [1.5] · *Multi-Select (Select 2)*

Ambulatory clinic leaders believe surgical scheduling takes 15 minutes, yet patients wait 3 weeks due to hidden fax re-entries and private nurse-station Access files. Which two discovery methods uncover objective truth? Select two.

- **A.** Inventorying departmental Excel macros, Access databases, and shadow-IT workarounds to retire manual data silos
- **B.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **E.** Power Automate Process Mining & Task Mining paired with cross-functional current-state discovery workshops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E` (`CSV: 1,5`)

Correct answers: A and E (are correct). Power Automate Process/Task Mining exposes true EHR-to-scheduling wait times and UI rework, while shadow-IT discovery catalogs unofficial nurse-station Access files and spreadsheets. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Correct. Uncovering unofficial spreadsheets and shadow tools during discovery prevents critical edge cases from surfacing post-go-live.
- **B:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **E:** Correct. Combining telemetry-driven Process/Task Mining with SME workshops exposes hidden rework loops and shadow processes objectively.

</details>

## Case Study Vignette — HavenBridge Health System

> HavenBridge Health System is consolidating 9 regional hospital CRMs into one Power Platform tenant. Clinicians need real-time read-only visibility into 60 million HL7 lab rows stored in Azure SQL without duplicating PHI into Dataverse storage, while HIPAA auditors require three-tier Dataverse auditing and least-privilege Entra Group Teams.

### Q042 (`E2Q023`) — Perform solution envisioning and requirement analysis [1.9] · *Single-Answer Multiple Choice*

Case study — HavenBridge Health System: Nine consolidated hospital CRMs each claim ownership of physician `NPI` credential records, causing conflicting specialty updates. What governance rule must the Solution Architect establish first?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Designating a single authoritative System of Record per entity with explicit survivorship and conflict-resolution rules
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Designating one authoritative System of Record (`Master Data` owner) for physician `NPI` profiles with explicit attribute survivorship rules eliminates 9-way update conflicts. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Correct. Every master entity (`Customer`, `Item`, `GL Account`) needs one clear authoritative owner to prevent bi-directional data corruption.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q043 (`E2Q063`) — Architect a solution [2.9] · *Single-Answer Multiple Choice*

Case study — HavenBridge Health System: Clinicians need live read-only Model-driven subgrids over 60 million HL7 lab result rows stored in Azure SQL without duplicating PHI into Dataverse storage or writing custom C# data-provider plug-ins. Which capability should you select?

- **A.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **B.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **C.** Using the `Virtual Connector Provider` (`SQL Server`, `SharePoint`, `Fabric`) to expose external tables in Dataverse with low-code setup
- **D.** Replicating data into native Dataverse tables (`Dataflows` / `ADF`) when Mobile Offline, row-level security roles, auditing, or SLAs are required

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Using the **`Virtual Connector Provider`** for SQL Server creates Dataverse **Virtual Tables** querying the 60M Azure SQL lab rows in place with zero Dataverse Database duplication and no custom C# provider boilerplate. [Skill 2.9: Determine when to connect external data in place (Virtual tables) versus import/replicate into Dataverse | Source: Connect external data in place (Virtual tables) vs import/replicate into Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-virtual-entities)]

- **A:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **B:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **C:** Correct. The Virtual Connector Provider creates Virtual Tables over supported connectors without authoring custom C# data-provider plug-ins.
- **D:** Incorrect. Virtual tables do not support Mobile Offline sync, Dataverse row-level User/Team ownership, or native column auditing.

</details>

### Q044 (`E2Q077`) — Architect a solution [2.15] · *Single-Answer Multiple Choice*

Case study — HavenBridge Health System: HavenBridge must provision least-privilege roles automatically for 14,000 clinicians managed in Microsoft Entra security groups, allow Oncology float specialists to access two hospital BUs simultaneously, and maintain HIPAA audit logs across tenant/table/column tiers. Which security model fits best?

- **A.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **B.** Combining `Modernized Business Units` (matrix access), `Microsoft Entra ID Security Group Teams`, & `Access Team Templates`
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **Microsoft Entra ID Security Group Teams** automate zero-touch role inheritance on first sign-in, while **Modernized Business Units** grant cross-BU matrix role assignments alongside three-tier Dataverse auditing (environment, table, and column). [Skill 2.15: Design Business Units, Modernized BUs, Owner Teams, Access Team Templates, & Entra Group Teams | Source: Design Business Units, Modernized BUs, Owner/Access Teams, & Entra Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **B:** Correct. Modernized BUs enable cross-BU matrix roles, Entra Group Teams automate zero-touch RBAC, and Access Teams handle ad-hoc record collaboration cleanly.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.

</details>

### Q045 (`E2Q036`) — Perform solution envisioning and requirement analysis [1.14] · *Single-Answer Multiple Choice*

Nine hospitals use nine incompatible credentialing checklists even though 92% of Joint Commission verification steps are identical. Guiding stakeholders to adopt `____` cuts build and maintenance complexity dramatically.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating
- **D.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Standardizing on one unified future-state credentialing BPF (with parameterized state-specific addenda) eliminates nine-way maintenance sprawl. [Skill 1.14: Guide future-state business process optimization and standardization before automating | Source: Guide future-state business process optimization and standardization (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.
- **D:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.

</details>

### Q046 (`E2Q084`) — Implement the solution [3.1] · *Single-Answer Multiple Choice*

Before promoting a clinical Canvas + plug-in release to QA, your GitHub Actions workflow runs automated static analysis that fails the build if accessibility `AccessibleLabel` errors or synchronous plug-in `WebClient` HTTP calls appear. Which tool pair powers this gate?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Enforcing `Solution Checker` and `App Checker` gates in CI/CD pipelines alongside `Power Platform Well-Architected` design reviews

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). **Solution Checker** and **App Checker** catch C# plug-in performance/reliability anti-patterns, Canvas delegation warnings, and `WCAG` accessibility errors automatically inside CI pipelines. [Skill 3.1: Evaluate detailed designs and implementations with Solution Checker, App Checker, & Well-Architected | Source: Evaluate detailed designs with Solution Checker, App Checker, & Well-Architected (https://learn.microsoft.com/en-us/power-platform/alm/use-powershell-cmdlets-solution-checker)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Correct. Solution Checker flags unbounded queries and sync plug-in anti-patterns, while App Checker catches delegation warnings and WCAG errors before release.

</details>

### Q047 (`E2Q024`) — Perform solution envisioning and requirement analysis [1.9] · *Single-Answer Multiple Choice*

To ensure patient `Contact`, clinic `Account`, and `Appointment` entities integrate seamlessly with Microsoft Cloud for Healthcare accelerators and Exchange sync, you should model entities atop `____`.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Aligning data entities to the Microsoft Common Data Model (`CDM`) standard tables (`Account`, `Contact`, `Activity`)
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Aligning schemas to the Microsoft Common Data Model (`CDM`) standard tables preserves compatibility with Dynamics 365, Healthcare accelerators, and Exchange Server-Side Sync. [Skill 1.9: Identify authoritative data sources, master data ownership, and residency/classification rules | Source: Identify authoritative data sources and master data boundaries (https://learn.microsoft.com/en-us/training/paths/solution-architect-data/)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Correct. Extending standard CDM tables preserves native Dynamics 365, AppSource ISV, Exchange, and AI Copilot interoperability.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.

</details>

### Q048 (`E2Q057`) — Architect a solution [2.6] · *Single-Answer Multiple Choice*

Charge nurses want live ward-census bar charts inside their Model-driven dashboard where clicking a bar filters the adjacent Dataverse `Admission` view immediately using their existing Dataverse Security Role. Which option fits best?

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Native Dataverse interactive experience dashboards and system charts provide zero-latency operational drill-down honoring Dataverse security automatically. [Skill 2.6: Design data visualization strategies across Dataverse charts, Power BI RLS, and Fabric/Synapse Link | Source: Design data visualization (Dataverse charts, Power BI RLS, Fabric/Synapse Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-synapse)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Correct. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Incorrect. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.

</details>

### Q049 (`E2Q020`) — Perform solution envisioning and requirement analysis [1.8] · *Single-Answer Multiple Choice*

To expose internal `HL7 FHIR R4` patient-demographics endpoints to Power Platform custom connectors with OAuth JWT validation, schema transformation, and per-caller rate throttling, you should place `____` at the boundary.

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Azure API Management (`APIM`) acts as the governed API gateway enforcing JWT validation, mutual TLS, rate limits, and OpenAPI contracts in front of EHR services. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Correct. Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q050 (`E2Q018`) — Perform solution envisioning and requirement analysis [1.7] · *Single-Answer Multiple Choice*

During quarterly executive governance, you compare pre-launch baseline ambulance turnaround times (`47 min`) and claim denial rates (`8.4%`) against post-launch telemetry (`19 min` and `1.6%`). This validates `____`.

- **A.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **B.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **C.** Defining baseline-backed `SMART` success KPIs (cycle-time reduction, error-rate drop, SLA adherence, & active adoption %)
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Validating post-launch operational telemetry against pre-launch baselines proves achievement of agreed `SMART` key success criteria. [Skill 1.7: Review and validate measurable key success criteria, KPIs, and adoption targets | Source: Review measurable key success criteria, KPIs, and adoption targets (https://learn.microsoft.com/en-us/power-platform/guidance/adoption/measure-business-value)]

- **A:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **B:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **C:** Correct. Quantifiable KPIs anchored to current-state baselines let stakeholders verify objective ROI after go-live.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q051 (`E2Q015`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

Sixteen mission-critical credentialing cloud flows run under an ex-resident physician’s personal account in the `Default` environment and write PHI to personal cloud folders. Which risk-remediation package addresses this?

- **A.** Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)
- **B.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **C.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **D.** Mitigating single-maker bus-factor risk, unmonitored personal flows, & technical debt via Managed Environments and CoE

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Transitioning critical workloads into **Managed Environments** under Service Principal (`Application User`) ownership with strict DLP policies and CoE monitoring eliminates single-maker and exfiltration risks. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.
- **B:** Incorrect. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **C:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **D:** Correct. Unmanaged citizen sprawl and bespoke code without ALM pipelines represent top organizational operational risks.

</details>

### Q052 (`E2Q032`) — Perform solution envisioning and requirement analysis [1.13] · *Multi-Select (Select 3)*

A national organ-transplant matching application on Power Platform undergoes architecture sign-off. Which three items must be documented as **Non-Functional Requirements (`NFRs`)**? Select three.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Capturing Non-Functional Requirements (`RPO`/`RTO`, peak concurrency, `p95` latency, API volume, `WCAG 2.1 AA`, & retention)
- **C.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **D.** Power Platform Well-Architected `Reliability` pillar (RPO/RTO targets, fault isolation, retries, & circuit breakers)
- **E.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **F.** Designing for `WCAG 2.1 AA` accessibility (`AccessibleLabel`, `TabIndex`, contrast) and `.resx` multi-language localization

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D, F` (`CSV: 2,4,6`)

Correct answers: B, D, and F (are correct). Sub-second `p95` response latency, concurrency, API throughput, & 25-year retention (`req_nfr_spec`), `99.99%` availability & `RPO`/`RTO` targets (`wa_reliability`), and `WCAG 2.1 AA` screen-reader/contrast compliance (`ux_wcag_accessible`) are essential NFRs. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Correct. Non-functional requirements govern architectural sizing, BCDR, licensing capacity, offline design, and security controls.
- **C:** Incorrect. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **D:** Correct. The Reliability pillar ensures mission-critical workloads withstand transient outages, throttling, and regional faults within defined RPO/RTO bounds.
- **E:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **F:** Correct. Building accessibility and localization into initial UX components avoids expensive retrofits before public or enterprise launch.

</details>

### Q053 (`E2Q085`) — Implement the solution [3.1] · *Single-Answer Multiple Choice*

During architecture validation, you review a custom plug-in registered synchronously on `Update` of `Contact` with **Filtering Attributes** left blank (`All Attributes`). Why does Solution Checker flag this as high risk?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Enforcing `Solution Checker` and `App Checker` gates in CI/CD pipelines alongside `Power Platform Well-Architected` design reviews
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Leaving `Filtering Attributes` blank causes the synchronous plug-in to fire on *every* column update (including unrelated status or last-login timestamps), wasting CPU and triggering cascading loops. [Skill 3.1: Evaluate detailed designs and implementations with Solution Checker, App Checker, & Well-Architected | Source: Evaluate detailed designs with Solution Checker, App Checker, & Well-Architected (https://learn.microsoft.com/en-us/power-platform/alm/use-powershell-cmdlets-solution-checker)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Correct. Solution Checker flags unbounded queries and sync plug-in anti-patterns, while App Checker catches delegation warnings and WCAG errors before release.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q054 (`E2Q081`) — Architect a solution [2.17] · *Multi-Select (Select 2)*

A health network must: (1) block makers from combining `Microsoft Dataverse` with `Gmail` or `Dropbox` in the same cloud flow while allowing `Epic FHIR` custom connectors only to `https://fhir.havenbridge.org`, and (2) let 220 external accrediting auditors review specific rows inside an internal Model-driven app. Which two designs apply? Select two.

- **A.** Combining `Modernized Business Units` (matrix access), `Microsoft Entra ID Security Group Teams`, & `Access Team Templates`
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Enforcing `DLP` + `Endpoint Filtering`, licensing external consumers via `Power Pages` (`Entra External ID`), & `Entra B2B` for internal-app guests
- **D.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **E.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). **DLP `Business` / `Blocked` classification + Connector Endpoint Filtering** plus **Microsoft Entra B2B** guest access for the 220 external auditors (`sec_dlp_ext_access`), scoped via **Entra Security Group Teams / Access Teams** (`sec_modern_bu_teams`), meets both requirements. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Correct. Modernized BUs enable cross-BU matrix roles, Entra Group Teams automate zero-touch RBAC, and Access Teams handle ad-hoc record collaboration cleanly.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Correct. Power Pages scales cost-effectively with `Table Permissions` for external portals, whereas Entra B2B suits external partners using internal apps.
- **D:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **E:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.

</details>

### Q055 (`E2Q010`) — Perform solution envisioning and requirement analysis [1.4] · *Single-Answer Multiple Choice*

Instead of migrating 320 million historical pharmacy claim-adjudication lines from 2012–2023 into Dataverse Database capacity, which low-effort architectural option gives actuaries full analytical query access alongside current Dataverse cases?

- **A.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **B.** Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics
- **C.** Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Keeping multi-hundred-million historical claim lines in Microsoft Fabric OneLake / Azure Data Lake and blending them with live Dataverse tables via `Fabric Link` + Power BI avoids prohibitive Dataverse Database storage and cutover effort. [Skill 1.4: Identify and estimate data migration and integration efforts, complexity drivers, and alternatives | Source: Estimate migration and integration efforts and alternatives (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **B:** Correct. Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.
- **C:** Incorrect. Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q056 (`E2Q068`) — Architect a solution [2.11] · *Single-Answer Multiple Choice*

Care coordinators collaborate inside Microsoft Teams channels and want inline actionable approval cards that update Dataverse `Referral` rows without switching browsers, plus automatic inbox appointment sync with Exchange Online. Which native capabilities should you combine?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Integrating Microsoft Teams (`Adaptive Cards` / embedded apps), Dynamics 365 F&O `Dual-write` + `Business Events`, & `Server-Side Sync`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Microsoft Teams **Adaptive Cards** / embedded apps paired with **Exchange Server-Side Synchronization** deliver seamless in-channel approvals and calendar/email synchronization. [Skill 2.11: Design collaboration (Teams, SharePoint ACL nuances, Exchange) and Dynamics 365 Dual-write integrations | Source: Design Teams, SharePoint, Exchange, and Dynamics 365 (Dual-write) integrations (https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dual-write/dual-write-overview)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Correct. Dual-write provides near-real-time bi-directional Dataverse-to-F&O sync, while Teams Adaptive Cards meet users directly in collaboration channels.

</details>

### Q057 (`E2Q014`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

A biopharma sponsor operates clinical sites in Germany, Canada, and Japan where health ministry laws forbid storing patient identifiable data outside national borders. Which risk factor must shape tenant architecture immediately?

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Assessing sovereign data-residency (`Multi-Geo`), PII/PHI/ITAR compliance, `CMK`, & cross-border connector risks upfront
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Sovereign PHI data-residency statutes require upfront `Multi-Geo` Dataverse environment placement, `CMK`/Lockbox evaluation, and regional DLP connector isolation. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Correct. Identifying residency and regulatory encryption constraints during envisioning prevents illegal cross-region tenant/environment placement.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q058 (`E2Q013`) — Perform solution envisioning and requirement analysis [1.5] · *Single-Answer Multiple Choice*

Thirty clinical informaticists want to build departmental Power Apps while central IT owns Epic FHIR connectors and HIPAA security sign-off. Establishing `____` defines clear maker vs pro-dev vs InfoSec accountability.

- **A.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Establishing a fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A fusion-team `RACI` governance matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model empower clinical makers safely inside IT guardrails. [Skill 1.5: Guide discovery of current-state business processes using workshops and Process/Task Mining | Source: Guide discovery of current-state business processes and process mining (https://learn.microsoft.com/en-us/power-automate/minit/overview)]

- **A:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Clear architectural ownership, ARB design gates, and CoE guardrails align business, citizen makers, pro-devs, and InfoSec.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q059 (`E2Q028`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

Every refined clinical User Story in Azure Boards must include objective pass/fail verification rules (`Given / When / Then`) known as `____` before entering development sprints.

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **C.** Refining prescriptive wishes into persona-based `User Stories` (`As a ... I need ... so that ...`) with testable Acceptance Criteria
- **D.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Testable Acceptance Criteria attached to each User Story align clinical SMEs, developers, and UAT testers on exact completion rules. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **C:** Correct. Outcome-oriented User Stories decouple business intent from premature UI assumptions and anchor QA test cases.
- **D:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.

</details>

### Q060 (`E2Q031`) — Perform solution envisioning and requirement analysis [1.12] · *Single-Answer Multiple Choice*

Home-infusion pharmacists working in hospital basements without Wi-Fi must record lot numbers, verify allergies, and capture patient sign-off locally. Documenting these disconnected persona actions belongs in `____`.

- **A.** Capturing Functional Requirements (persona workflows, state rules, approvals, offline CRUD scope, & statutory reports)
- **B.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **C.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **D.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Capturing exact offline CRUD user actions and state transitions per persona is a critical functional requirement driving Mobile Offline design. [Skill 1.12: Identify functional requirements across personas, business rules, approvals, and offline access | Source: Identify functional requirements across personas, offline, and workflows (https://learn.microsoft.com/en-us/power-apps/mobile/setup-mobile-offline)]

- **A:** Correct. Functional requirements specify what business behaviors and data transformations the solution must perform for each role.
- **B:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **C:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **D:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.

</details>

### Q061 (`E2Q034`) — Perform solution envisioning and requirement analysis [1.13] · *Single-Answer Multiple Choice*

Pediatric medical-malpractice statutes require retaining clinical case history for `21 years` without slowing active daily views for 3,200 nurses. Which capacity architecture meets this NFR?

- **A.** Governing `Database`, `File`, & `Log` storage pools via `Dataverse Long Term Retention`, `Fabric/Synapse Link` archival, & attachment offloading
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Using **Dataverse Long Term Retention** policies and `Fabric/Synapse Link` archival moves cold multi-decade rows out of hot operational queries while preserving compliant audit access. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Correct. Keeping relational `Database` capacity lean prevents tenant admin lockouts (`Copy`/`Restore` blocks) and controls storage overage costs.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.

</details>

### Q062 (`E2Q037`) — Perform solution envisioning and requirement analysis [1.15] · *Ordered Sequence (Multiple Choice)*

A hospital system presents 210 clinical-CRM requirements and wants a disciplined decision order to minimize custom code maintenance across Microsoft release waves. Which four-step fit/gap sequence should you apply?

- **A.** Accept every stakeholder wish into Phase 1 without feasibility scoring → Skip MVP boundaries → Hardcode workarounds in Production → Defer licensing impact checks until billing
- **B.** Build bespoke React SPAs and C# plug-ins for every requirement first → Replace standard Dynamics 365 tables with custom tables → Ignore AppSource → Check standard features last
- **C.** Validate each requirement against out-of-the-box Dataverse & Dynamics 365 capabilities → Evaluate declarative low-code configuration → Assess vetted AppSource ISV solutions → Specify targeted pro-code extensions only for remaining gaps
- **D.** Inject unsupported DOM-scraping JavaScript into Model-driven forms → Modify SQL indexes directly via TDS → Bypass security roles → Lock out Microsoft updates

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Evaluating out-of-the-box Dataverse/Dynamics 365 fit first, then declarative low-code configuration, then vetted AppSource ISVs, and finally targeted pro-code extensions minimizes TCO and upgrade risk. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Unbounded scope acceptance without feasibility or licensing evaluation derails timelines and budgets.
- **B:** Incorrect. Defaulting to custom code and duplicating restricted/standard Dynamics 365 tables inflates TCO and breaks product upgrades.
- **C:** Correct. Fit/gap analysis prioritizes standard platform/Dynamics 365 features first, then declarative configuration, then supported AppSource ISVs, reserving custom code strictly for true differentiators.
- **D:** Incorrect. Unsupported DOM manipulation and direct SQL writes violate Microsoft supportability contracts and break on wave updates.

</details>

### Q063 (`E2Q096`) — Implement the solution [3.6] · *Single-Answer Multiple Choice*

After an initial 5-day bulk seed of 3.1 million historical patient encounters completes on Thursday, hospitals continue treating patients until Saturday 22:00 freeze. How do you migrate Thursday–Saturday changes inside a 90-minute cutover window and prove zero lost encounters?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Executing automated row-count/hash-total reconciliation and `Dataverse Change Tracking` / watermark delta loads during cutover freeze
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Running watermark / **Change Tracking delta loads** (`BypassCustomPluginExecution` enabled) paired with automated post-load row-count and checksum reconciliation keeps final cutover inside 90 minutes. [Skill 3.6: Escalate and resolve data migration bottlenecks (BypassCustomPluginExecution, delta loads, reconciliation) | Source: Escalate and remediate enterprise data migration bottlenecks and cutover issues (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/TVF-override-plugin-execution)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Correct. Delta loads keep downtime inside tight weekend cutover windows while automated financial/count reconciliation proves migration integrity.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.

</details>

### Q064 (`E2Q006`) — Perform solution envisioning and requirement analysis [1.2] · *Single-Answer Multiple Choice*

Hospital Utilization Review coordinators work at dual-monitor desks processing complex prior-authorization queues, multi-stage clinical review gates, and dense Dataverse grids. Proposed solution: Build a Model-driven Power App with Business Process Flows, system views, and interactive dashboards over Dataverse. Does this fit the persona?

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **C.** Model-driven Power App over Microsoft Dataverse with responsive forms, views, dashboards, & Business Process Flows
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — structured, data-dense back-office case and lifecycle management over Dataverse fits a Model-driven Power App natively. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **C:** Correct. Model-driven apps excel at structured, data-dense back-office case and lifecycle management directly atop Dataverse security.
- **D:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.

</details>

### Q065 (`E2Q049`) — Architect a solution [2.2] · *Single-Answer Multiple Choice*

Before building a specialized audiogram waveform plotter for audiology clinics, how should the Solution Architect validate workflow ergonomics with clinicians and then deliver the reusable UI control?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **D.** Validating interactive UX prototypes (`Figma-to-App` / `Custom Pages`) early and building `PCF` controls for specialized UI gaps

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Validating interactive UX wireframes/Figma prototypes with clinicians first and then implementing a reusable TypeScript/React **PCF** control minimizes rework and guarantees native form support. [Skill 2.2: Identify app customization approaches and validate interactive user experience prototypes | Source: Select customization approaches for existing apps and validate UX prototypes (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/design-consistency)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **D:** Correct. Interactive prototyping validates user journeys cheaply, while Power Apps Component Framework (`PCF`) renders reusable custom TypeScript/React controls.

</details>

### Q066 (`E2Q040`) — Perform solution envisioning and requirement analysis [1.16] · *Multi-Select (Select 2)*

A diagnostic equipment division needs mobile technician preventive-maintenance work orders, van-stock inventory, automated skill/territory travel-time optimization (`RSO`), and an embedded CTI softphone toolbar. Which two recommendations fit best? Select two.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **C.** Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **E.** Dynamics 365 first-party app (`Sales`, `Customer Service`, or `Field Service`) leveraging native schemas, SLAs, & RSO scheduling

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). Dynamics 365 Field Service (`Work Order`, technician van inventory, and `Resource Scheduling Optimization`) plus a Channel Integration Framework (`CIF`)-certified AppSource CTI softphone ISV cover both requirements natively. [Skill 1.16: Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options | Source: Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **C:** Correct. Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **E:** Correct. Adopting Dynamics 365 first-party apps avoids reinventing complex case routing, omnichannel queues, or Resource Scheduling Optimization.

</details>

## Case Study Vignette — CareStride Home Nursing

> CareStride Home Nursing equips 2,800 visiting nurses with iPads in rural dead zones lacking cellular signal for 6 hours at a time. Nurses need sub-second offline wound-care charting, barcode scanning, and conflict resolution on reconnect, paired with WCAG 2.1 AA accessibility and Power Platform Well-Architected reliability targets.

### Q067 (`E2Q002`) — Perform solution envisioning and requirement analysis [1.1] · *Single-Answer Multiple Choice*

Case study — CareStride Home Nursing: CareStride Home Nursing requires resilient offline wound-care charting during 6-hour rural cellular blackouts, automatic conflict handling on reconnect, and graceful degradation when EHR endpoints slow down. Which Power Platform Well-Architected pillar anchors these goals?

- **A.** Power Platform Well-Architected `Reliability` pillar (RPO/RTO targets, fault isolation, retries, & circuit breakers)
- **B.** Power Platform Well-Architected `Operational Excellence` pillar (automated ALM pipelines, Application Insights, & CoE)
- **C.** Power Platform Well-Architected `Security` pillar (Zero Trust Entra identity, least privilege, DLP, & encryption)
- **D.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). The Power Platform Well-Architected `Reliability` pillar governs offline resilience, graceful degradation, transient fault recovery, and business-continuity SLAs. [Skill 1.1: Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars | Source: Microsoft Power Platform Well-Architected overview (https://learn.microsoft.com/en-us/power-platform/well-architected/overview)]

- **A:** Correct. The Reliability pillar ensures mission-critical workloads withstand transient outages, throttling, and regional faults within defined RPO/RTO bounds.
- **B:** Incorrect. Operational Excellence standardizes CI/CD solution pipelines, automated Solution Checker gates, telemetry, and Managed Environment governance.
- **C:** Incorrect. The Security pillar protects confidentiality and integrity through Entra Conditional Access, least-privilege roles, DLP endpoint rules, and CMK/Lockbox.
- **D:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.

</details>

### Q068 (`E2Q005`) — Perform solution envisioning and requirement analysis [1.2] · *Single-Answer Multiple Choice*

Case study — CareStride Home Nursing: Visiting nurses need sub-second iPad charting, camera wound measurement, and medication barcode scans during 6-hour rural dead zones. You should architect a `____`.

- **A.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **D.** Canvas Power App with a `Mobile Offline` profile and device-native camera/barcode UX tailored to frontline tasks

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A Canvas Power App configured with a `Mobile Offline` profile delivers native iPad camera/barcode controls and local SQLite Dataverse synchronization across multi-hour dead zones. [Skill 1.2: Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents | Source: Identify Microsoft Power Platform solution components (https://learn.microsoft.com/en-us/training/modules/become-solution-architect/)]

- **A:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **D:** Correct. Canvas apps give pixel-level task UX and offline-first Dataverse synchronization for field workers operating without connectivity.

</details>

### Q069 (`E2Q033`) — Perform solution envisioning and requirement analysis [1.13] · *Single-Answer Multiple Choice*

Case study — CareStride Home Nursing: CareStride’s federal Medicare contract mandates `WCAG 2.1 AA` screen-reader labels, high-contrast outdoor legibility, and Spanish/English UI strings across all nurse iPad screens. Which design standard satisfies this NFR?

- **A.** Designing for `WCAG 2.1 AA` accessibility (`AccessibleLabel`, `TabIndex`, contrast) and `.resx` multi-language localization
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enforcing `WCAG 2.1 AA` accessibility (`AccessibleLabel`, `TabIndex`, contrast ratios) and multi-language `.resx` localization from initial component design fulfills federal accessibility NFRs. [Skill 1.13: Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention) | Source: Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG) (https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview)]

- **A:** Correct. Building accessibility and localization into initial UX components avoids expensive retrofits before public or enterprise launch.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q070 (`E2Q092`) — Implement the solution [3.4] · *Single-Answer Multiple Choice*

Inside a synchronous C# `Post-Operation` plug-in that updates a parent rollup summary, checking `if (context.Depth > ____)` prevents runaway recursive plug-in loops when unexpected self-triggers occur.

- **A.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **B.** Resolving automation/integration conflicts via `Select columns` (`filteringattributes`), `Trigger Conditions`, plug-in `Depth` checks, & `ETag` (`If-Match`) optimistic concurrency
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Evaluating `IPluginExecutionContext.Depth` (alongside explicit `Filtering Attributes` and correlation flags) guards custom plug-ins against accidental recursive infinite loops. [Skill 3.4: Assess storage/resource impact and resolve automation loops, race conditions, & integration conflicts | Source: Assess storage/resource impact and resolve automation & integration conflicts (https://learn.microsoft.com/en-us/power-platform/admin/capacity-storage)]

- **A:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **B:** Correct. Column filters, actor exclusions, and `If-Match` row-version headers eliminate infinite ping-pong loops and silent lost-update race conditions.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.

</details>

### Q071 (`E2Q035`) — Perform solution envisioning and requirement analysis [1.14] · *Single-Answer Multiple Choice*

A clinic’s paper intake form asks patients to write their name, DOB, and insurance ID six separate times across six clipboards. Proposed solution: Build six separate Power Pages forms that ask the patient to re-type name, DOB, and insurance ID six times so each department receives a familiar layout. Does this optimize the future-state process?

- **A.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). No — architects simplify and standardize the future-state process first, capturing patient demographics once into Dataverse and surfacing tailored departmental views automatically. [Skill 1.14: Guide future-state business process optimization and standardization before automating | Source: Guide future-state business process optimization and standardization (https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/overview)]

- **A:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.

</details>

### Q072 (`E2Q083`) — Architect a solution [2.17] · *Single-Answer Multiple Choice*

An Azure Function running inside your tenant needs passwordless authentication to Dataverse Web API without storing client secrets that expire every 12 months. Binding a federated `____` to a Dataverse Application User eliminates secret rotation risk.

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Using `OAuth 2.0 On-Behalf-Of (OBO)` to preserve caller identity/audit trails vs `Entra Service Principal (S2S)` / `Managed Identity` for background jobs
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Using **Azure Managed Identity** (via Microsoft Entra Workload Identity Federation mapped to a Dataverse `Application User`) eliminates stored client secrets and secret-expiry outages completely. [Skill 2.17: Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B) | Source: Identify Entra ID groups/App Registrations, DLP policies, and external user access (https://learn.microsoft.com/en-us/power-pages/security/authentication/overview)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Correct. OBO propagates the signed-in user’s identity downstream for row-level authorization, whereas S2S/Managed Identity runs headless workloads.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q073 (`E2Q100`) — Implement the solution [3.8] · *Single-Answer Multiple Choice*

Rather than cutting over all 9 hospitals simultaneously on Day 1, rolling out Hospital 1 as a 2-week monitored pilot wave with signed Go/No-Go gates and manual pre-cutover backups exemplifies `____`.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Establishing signed-off `Go / No-Go` readiness gates, manual pre-cutover `Backup` restore points, rollback runbooks, & phased wave rollouts
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Phased wave rollouts backed by explicit Go/No-Go readiness gates, manual restore points, and Application Insights hypercare war rooms minimize clinical go-live risk. [Skill 3.8: Identify go-live readiness gates, execute Administration mode cutovers, and manage hypercare telemetry | Source: Assess go-live readiness factors, Administration mode, and hypercare remediation (https://learn.microsoft.com/en-us/power-platform/admin/admin-mode)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Correct. Clear Go/No-Go criteria, pre-upgrade backups, and phased pilot waves minimize blast radius during enterprise go-live.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q074 (`E2Q008`) — Perform solution envisioning and requirement analysis [1.3] · *Single-Answer Multiple Choice*

A genomics lab triggers 25-minute whole-exome DICOM alignment pipelines whenever a specimen status flips to `Sequenced` in Dataverse. Which hybrid extension architecture handles the compute workload?

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Azure pro-code extension (`Azure Functions`, `Service Bus`, `AKS`, or `Azure AI Foundry`) integrated with Power Platform
- **D.** Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Long-running genomic and imaging compute (`> 2 minutes`) must run asynchronously in Azure pro-code services (`Azure Batch` / `AKS` / `Azure Functions`) triggered via Dataverse events. [Skill 1.3: Identify and select components from existing apps, Dynamics 365, AppSource ISVs, and Azure | Source: Evaluate Dynamics 365 apps, AppSource ISVs, and Azure extensions (https://learn.microsoft.com/en-us/training/modules/discover-customer-needs/)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Correct. Heavy compute, long-running algorithms (> 2 minutes), and high-throughput brokered messaging offload cleanly to Azure extensions.
- **D:** Incorrect. BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.

</details>

### Q075 (`E2Q088`) — Implement the solution [3.3] · *Ordered Sequence (Multiple Choice)*

An HL7 integration service syncing lab orders into Dataverse hits `HTTP 429` errors every morning at 08:00 shift change. Which four-step remediation sequence resolves Dataverse Service Protection throttling cleanly?

- **A.** Pinpoint throttled callers in Dataverse API analytics → Batch writes via `CreateMultiple` / `$batch` & use Change Tracking → Pool high-volume S2S loads across Entra Application Users → Honor HTTP `429` `Retry-After` backoff
- **B.** Buy 100 Power BI Free licenses expecting them to lift 5-minute Service Protection caps → Hardcode personal maker credentials → Ignore `x-ms-ratelimit-time-remaining-xrm-requests` headers → Discard throttled records silently
- **C.** Spin up 50 parallel threads under one single user account → Retry HTTP 429 errors immediately with 0 ms delay → Replace filtered queries with full `SELECT *` scans → Open a ticket asking Microsoft to disable platform limits permanently
- **D.** Move bulk integration loops inside synchronous Dataverse plug-ins → Chain 8 child plug-in updates per row → Enable `RetrieveAllEntities` metadata calls on every transaction → Disable caching

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Pinpointing throttled callers in API analytics, batching with `CreateMultiple`/`$batch` & Change Tracking, distributing S2S load across pooled Application Users, and honoring `Retry-After` backoff resolves `HTTP 429` throttling. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Correct. Resolving Service Protection (`6,000` req / `20` min compute per 5-min window) combines batch/bulk operations, Change Tracking, pooled S2S Application Users where appropriate, and honoring `Retry-After` backoff.
- **B:** Incorrect. Service Protection limits protect real-time platform stability per user/web server over 5-minute windows regardless of license SKU.
- **C:** Incorrect. Immediate zero-delay retries under a single user identity amplify `HTTP 429` throttling and extend penalty windows.
- **D:** Incorrect. Heavy metadata calls and chained synchronous updates multiply execution time against the 20-minute per-5-minute sliding window limit.

</details>

### Q076 (`E2Q039`) — Perform solution envisioning and requirement analysis [1.15] · *Single-Answer Multiple Choice*

A developer proposes manipulating undocumented internal React DOM nodes inside Model-driven forms via `window.parent.document` to color-code rows. How must you classify this in the fit/gap review?

- **A.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Structured Fit/Gap matrix scoring requirements across `Out-of-the-Box`, `Configuration`, `AppSource ISV`, & `Custom Code`
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). DOM scraping is unsupported and breaks during Microsoft service updates; fit/gap analysis rejects unsupported hacks in favor of a supported `PCF` dataset/field control or modern grid customizer. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Correct. Formal fit/gap scoring exposes customization TCO, licensing impacts, and upgrade maintenance trade-offs transparently.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q077 (`E2Q076`) — Architect a solution [2.15] · *Ordered Sequence (Multiple Choice)*

A multi-hospital system needs strict campus Business Unit isolation, matrix cross-campus roles for float physicians, zero-touch Entra group role assignment, and lightweight tumor-board case sharing. Which four-step security design sequence should you follow?

- **A.** Store confidential M&A contracts in default SharePoint Document Management folders → Assume SharePoint automatically inherits Dataverse row-level Security Roles & Access Teams → Grant site-wide Read to all employees → Go live
- **B.** Create 400 micro Business Units mirroring every HR cost center → Move users between BUs daily (wiping roles prior to modern settings) → Duplicate 400 identical copies of every Security Role → Audit nothing
- **C.** Place all users in one root BU with Organization-level Read/Write/Delete → Clone System Administrator for power users → Hide restricted fields using client-only JavaScript → Share individual records manually
- **D.** Model Business Units around isolation boundaries (with Modernized BUs for matrix access) → Author custom least-privilege Security Roles → Bind roles to Entra Security Group Teams → Layer Column Security & Access Team Templates

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Modeling BUs around campus isolation boundaries (enabling Modernized BUs for float matrix roles), building least-privilege Security Roles, binding roles to Entra Security Group Teams, and applying Column Security + Access Team Templates scales cleanly. [Skill 2.15: Design Business Units, Modernized BUs, Owner Teams, Access Team Templates, & Entra Group Teams | Source: Design Business Units, Modernized BUs, Owner/Access Teams, & Entra Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect. Out-of-the-box SharePoint Document Management does NOT synchronize Dataverse row-level security ACLs to SharePoint folders automatically.
- **B:** Incorrect. Over-fragmenting Business Units for reporting rather than true security boundaries creates massive administrative overhead.
- **C:** Incorrect. Client-side JavaScript never secures data at the API layer, and manual per-record sharing bloats the PrincipalObjectAccess (`POA`) table.
- **D:** Correct. Scalable Dataverse security aligns BUs to isolation boundaries, layers custom least-privilege roles onto Entra Security Group Teams for zero-touch provisioning, and handles exceptions via Access Teams and Column Security.

</details>

### Q078 (`E2Q016`) — Perform solution envisioning and requirement analysis [1.6] · *Single-Answer Multiple Choice*

Hospital IT has zero automated build pipelines and deploys hotfixes by editing Production forms live at midnight. Aligning to the Well-Architected `____` pillar introduces source-controlled ALM pipelines and telemetry.

- **A.** Power Platform Well-Architected `Operational Excellence` pillar (automated ALM pipelines, Application Insights, & CoE)
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Operational Excellence` replaces risky manual Production edits with automated CI/CD solution pipelines, Solution Checker gates, and Application Insights monitoring. [Skill 1.6: Assess organizational risk factors across residency, compliance, governance maturity, and debt | Source: Assess organizational risk factors, governance maturity, and compliance (https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview)]

- **A:** Correct. Operational Excellence standardizes CI/CD solution pipelines, automated Solution Checker gates, telemetry, and Managed Environment governance.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q079 (`E2Q026`) — Perform solution envisioning and requirement analysis [1.10] · *Single-Answer Multiple Choice*

An operations lead wants to feed raw, unvalidated physician free-text notes full of typos and missing timestamps directly into automated SLA penalty billing. Why must you enforce `____` first?

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **C.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **D.** Defining pre-cutover data quality standards (deduplication keys, mandatory completeness, referential integrity, & domain mappings)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Defining strict data quality standards (structured timestamps, completeness checks, and reference validation) is mandatory before using existing data for financial SLA billing. [Skill 1.10: Define use cases and data quality standards for existing data prior to migration or integration | Source: Define use cases and data quality standards for existing data (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **C:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **D:** Correct. Enforcing cleansing and deduplication gates before migration prevents garbage-in/garbage-out failures in Dataverse.

</details>

### Q080 (`E2Q038`) — Perform solution envisioning and requirement analysis [1.15] · *Single-Answer Multiple Choice*

Documenting every requirement’s classification (`Standard`, `Configuration`, `ISV`, `Custom Extension`), licensing impact, and maintenance risk in a traceable artifact produces a `____`.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Structured Fit/Gap matrix scoring requirements across `Out-of-the-Box`, `Configuration`, `AppSource ISV`, & `Custom Code`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A structured Fit/Gap matrix provides executive transparency into licensing, build effort, and long-term upgrade maintainability. [Skill 1.15: Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code | Source: Perform fit/gap analyses and classify configuration vs custom code (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Correct. Formal fit/gap scoring exposes customization TCO, licensing impacts, and upgrade maintenance trade-offs transparently.

</details>

### Q081 (`E2Q078`) — Architect a solution [2.16] · *Multi-Select (Select 3)*

A clinical genetics platform requires: (1) restricting `HIV_Status` and `Genetic_Marker` columns solely to authorized geneticists, (2) zero standing Production admin rights, and (3) preventing manual record sharing from bloating `PrincipalObjectAccess` (`POA`). Which three controls should you implement? Select three.

- **A.** Enforcing `Microsoft Entra Conditional Access` (MFA & compliant device) plus `Power Platform IP Firewall` & `Cookie IP binding`
- **B.** Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access
- **C.** Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities
- **D.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **E.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **F.** Preventing `PrincipalObjectAccess (POA)` table bloat by replacing manual per-record sharing and `Parental` cascades with `Access Team Templates`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B, F` (`CSV: 1,2,6`)

Correct answers: A, B, and F (are correct). `Column Security Profiles` + `Microsoft Entra PIM` just-in-time admin elevation (`sec_col_hier_pim`), `Access Team Templates` avoiding manual `POA` bloat (`sec_poa_hygiene`), and `Entra Conditional Access` + IP Firewall (`sec_cond_access_ip`) enforce clinical zero-trust security. [Skill 2.16: Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox) | Source: Design Security Roles, Column/Hierarchy security, and security governance (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Correct. Combining Entra Conditional Access with Managed Environment IP Firewall and session cookie binding blocks token replay from untrusted networks.
- **B:** Correct. Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.
- **C:** Incorrect. Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.
- **D:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **E:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **F:** Correct. Millions of `POA` rows from manual sharing and `Cascade All` relationships degrade SQL query performance across Dataverse views.

</details>

### Q082 (`E2Q030`) — Perform solution envisioning and requirement analysis [1.12] · *Single-Answer Multiple Choice*

Which specification belongs in the **Functional Requirements** document for a clinical prior-authorization solution?

- **A.** Capturing Non-Functional Requirements (`RPO`/`RTO`, peak concurrency, `p95` latency, API volume, `WCAG 2.1 AA`, & retention)
- **B.** Capturing Functional Requirements (persona workflows, state rules, approvals, offline CRUD scope, & statutory reports)
- **C.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources
- **D.** Conforming to `Dataverse Service Protection` limits (`6,000` req / `20m` compute per `5-min` window), pooling `S2S Application Users`, & honoring `Retry-After`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Medical-necessity routing rules, peer-to-peer physician review state transitions, and denial-letter generation define functional business behavior (`req_functional_spec`). [Skill 1.12: Identify functional requirements across personas, business rules, approvals, and offline access | Source: Identify functional requirements across personas, offline, and workflows (https://learn.microsoft.com/en-us/power-apps/mobile/setup-mobile-offline)]

- **A:** Incorrect. Non-functional requirements govern architectural sizing, BCDR, licensing capacity, offline design, and security controls.
- **B:** Correct. Functional requirements specify what business behaviors and data transformations the solution must perform for each role.
- **C:** Incorrect. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.
- **D:** Incorrect. Service Protection enforces per-user/per-web-server 5-minute sliding caps (`HTTP 429`); pooling S2S Application Users and respecting `Retry-After` maximizes throughput.

</details>

### Q083 (`E2Q047`) — Architect a solution [2.1] · *Multi-Select (Select 2)*

A life-sciences enterprise wants Automated Pipelines with Sharing Limits, Weekly Usage Digest telemetry, and isolated deployment cadences across `Core Clinical CDM`, `Common FHIR Integrations`, and `Trial Coordinator App`. Which two designs should you combine? Select two.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix
- **C.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **D.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **E.** Dedicated `Dev -> Test -> UAT -> Prod` environments (plus sovereign `Multi-Geo` instances) governed by `Managed Environments` & `CoE Starter Kit`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). Segmented Managed Solutions under a unified Publisher prefix (`sol_segmented_alm`) paired with multi-tier **Managed Environments** + **CoE Starter Kit** (`env_multi_tier_coe`) provide modular ALM and automated governance. [Skill 2.1: Design segmented solution topology, custom Publisher strategy, and Managed Environments | Source: Design solution topology, publisher segmentation, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/alm/segmented-solutions-alm)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.
- **C:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **D:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **E:** Correct. Multi-tier ALM environments isolate production workloads, Multi-Geo satisfies regional residency, and CoE + Managed Environments automate governance.

</details>

### Q084 (`E2Q098`) — Implement the solution [3.7] · *Single-Answer Multiple Choice*

Proposed solution: When retiring a deprecated custom column from Production, delete the entire Managed Solution in Production and re-import `v3.2` fresh. Should the Solution Architect approve this deployment plan?

- **A.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **B.** Resolving deployment failures by running `Remove active customizations`, refactoring circular solution dependencies into a base layer, & validating stage JSON bindings
- **C.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). No — deleting a Managed Solution in Production permanently **erases its custom tables and live production rows**! Always remove the column in Dev, increment version, and import as a Managed **Upgrade** (`Stage for upgrade` -> `Apply upgrade`). [Skill 3.7: Resolve deployment plan issues, Unmanaged Active Solution Layers, and circular solution dependencies | Source: Resolve deployment plan, Solution Layer, and pipeline dependency issues (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **B:** Correct. Stripping Unmanaged Active layers and decoupling circular references ensures repeatable, zero-touch Managed Solution Upgrades.
- **C:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q085 (`E2Q046`) — Perform solution envisioning and requirement analysis [1.18] · *Single-Answer Multiple Choice*

Deferring non-critical predictive readmission dashboards to Release 2 so core bedside safety workflows launch cleanly on schedule exemplifies `____`.

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Scoping a high-value `MVP` Phase 1 release using MoSCoW prioritization and formal change-request governance
- **D.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Phased `MVP` scoping prioritizes mandatory clinical safety outcomes in Release 1 and schedules secondary enhancements into controlled subsequent waves. [Skill 1.18: Determine MVP vs phased solution scope boundaries and govern scope changes | Source: Determine MVP vs phased solution scope and manage scope boundaries (https://learn.microsoft.com/en-us/training/paths/become-solution-architect/)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Correct. Phased MVP delivery de-risks go-live, delivers early business value, and prevents uncontrolled scope creep.
- **D:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q086 (`E2Q044`) — Perform solution envisioning and requirement analysis [1.17] · *Single-Answer Multiple Choice*

Multiple Power Apps, Power Pages portals, and an Epic middleware service all need to invoke the exact same server-side patient-eligibility calculation inside Dataverse via a versioned OData action. Defining a `____` solves this cleanly.

- **A.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **B.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **C.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **D.** Defining solution-aware Dataverse `Custom APIs` exposing strongly typed request/response contracts for internal and external callers

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A solution-aware Dataverse **`Custom API`** exposes a strongly typed, privilege-gated OData request/response contract reusable across apps, flows, and external callers. [Skill 1.17: Address functional gaps through supported low-code/pro-code alternate solutions | Source: Address functional gaps through low-code/pro-code alternate solutions (https://learn.microsoft.com/en-us/power-platform/well-architected/operational-excellence/overview)]

- **A:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **B:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **C:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **D:** Correct. Custom APIs replace legacy Custom Process Actions with code-first, solution-aware OData bound/unbound operations and granular privilege checks.

</details>

### Q087 (`E2Q019`) — Perform solution envisioning and requirement analysis [1.8] · *Multi-Select (Select 2)*

A consolidated health network runs Epic EHR (`HL7 FHIR`), Workday HR, Oracle ERP, an acquired clinic’s separate Entra tenant, and MPLS firewalls. Which two artifacts must the Solution Architect establish during landscape analysis? Select two.

- **A.** Designating a single authoritative System of Record per entity with explicit survivorship and conflict-resolution rules
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Enterprise Architecture Context Diagram mapping systems of record, Entra tenants, hybrid networks, & sync/async SLAs
- **D.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **E.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). An Enterprise Architecture Context Diagram (mapping identity forests, hybrid networks, and FHIR/batch SLAs) plus a Master-Data System-of-Record matrix prevent integration collisions. [Skill 1.8: Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries | Source: Evaluate an organization’s enterprise architecture landscape (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Correct. Every master entity (`Customer`, `Item`, `GL Account`) needs one clear authoritative owner to prevent bi-directional data corruption.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Correct. Evaluating the enterprise landscape clarifies authoritative boundaries, identity federation, firewall paths, and integration patterns.
- **D:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **E:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.

</details>

### Q088 (`E2Q051`) — Architect a solution [2.3] · *Single-Answer Multiple Choice*

Four hospital app teams need identical HIPAA privacy banners, NPI checksum validation flows, and HL7 API wrappers, plus clear visual documentation of entity cardinalities and integration sequences. Which architectural approach should you enforce?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Reusing `Component Libraries`, `PCF`, `Child Flows`, & `Custom Connectors`, documented via `ERD`, `Sequence`, & `Context` diagrams
- **C.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Packaging shared assets in `Canvas Component Libraries`, `PCF`, `Child Flows`, and `Custom Connectors` — documented via `ERD`, `Sequence`, and `Context` diagrams — maximizes reuse and design clarity. [Skill 2.3: Maximize component reuse (PCF, Component Libraries, Child Flows) and communicate designs visually | Source: Maximize component reuse (PCF, Component Libraries, Child Flows) & visual diagrams (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Correct. Shared component catalogs eliminate duplicate maintenance, while visual architecture diagrams align technical and business stakeholders.
- **C:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.

</details>

### Q089 (`E2Q066`) — Architect a solution [2.10] · *Single-Answer Multiple Choice*

Phone calls, portal messages, SMS reminders, and nurse check-ins must all roll up chronologically into a unified `Timeline` wall on the `Patient` form with `Regarding` polymorphic lookups. Creating custom `____` tables (or using standard Activity tables) enables this behavior.

- **A.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Dataverse `Elastic tables` (Cosmos DB horizontal partitioning + `TTL`) for high-velocity telemetry, and `File`/SharePoint/Blob offloading for binaries
- **D.** Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Modeling timeline interactions as **Activity tables** surfaces unified chronological `Timeline` entries and `Regarding` polymorphic associations across Dataverse forms (while keeping high-rate non-timeline IoT bursts in Elastic tables). [Skill 2.10: Design complex data models (ownership immutability, Elastic/Activity tables, binary storage offloading) | Source: Design complex data models (ownership, Elastic/Activity tables, storage capacity) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/elastic-tables)]

- **A:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Correct. Elastic tables ingest tens of thousands of ephemeral JSON/IoT writes per minute with automatic `TTL` expiry without relational index contention.
- **D:** Incorrect. Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.

</details>

## Case Study Vignette — Aegis Clinical Trials

> Aegis Clinical Trials promotes segmented Managed Solutions (`Core`, `Intake`, `Analytics`) across Dev, QA, UAT, and Prod via pipelines. During go-live rehearsal, an ad-hoc UAT form edit masked Managed v3.2 changes, and two bi-directional flows between Dataverse and CTMS entered an infinite update loop burning 500,000 daily API requests.

### Q090 (`E2Q048`) — Architect a solution [2.1] · *Single-Answer Multiple Choice*

Case study — Aegis Clinical Trials: Aegis Clinical Trials deploys `Core`, `Intake`, and `Analytics` across Dev, QA, UAT, and Prod. Why should shared lookup tables (`Site`, `Protocol`, `Investigator`) live exclusively inside the foundational `Core` Managed Solution?

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2
- **C.** Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service
- **D.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Placing foundational tables in a `Core` base Managed Solution prevents circular cross-solution dependencies and lets `Intake` and `Analytics` upgrade independently. [Skill 2.1: Design segmented solution topology, custom Publisher strategy, and Managed Environments | Source: Design solution topology, publisher segmentation, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/alm/segmented-solutions-alm)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.
- **C:** Incorrect. Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.
- **D:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.

</details>

### Q091 (`E2Q091`) — Implement the solution [3.4] · *Multi-Select (Select 2)*

Case study — Aegis Clinical Trials: Two bi-directional flows between Dataverse `Subject_Enrollment` and the external CTMS fired 500,000 ping-pong updates in 24 hours, exhausting daily API requests and swelling `Audit` log storage. Which two fixes resolve the incident? Select two.

- **A.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **B.** Resolving automation/integration conflicts via `Select columns` (`filteringattributes`), `Trigger Conditions`, plug-in `Depth` checks, & `ETag` (`If-Match`) optimistic concurrency
- **C.** Governing `Database`, `File`, & `Log` storage pools via `Dataverse Long Term Retention`, `Fabric/Synapse Link` archival, & attachment offloading
- **D.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **E.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Adding strict **`Select columns`** (`filteringattributes`), **`Trigger Conditions`** excluding the integration `modifiedby` Application User, and `ETag` concurrency (`res_conflict_loops`), plus cleaning/tiering `Log` capacity (`cap_storage_tiering`), stops the loop permanently. [Skill 3.4: Assess storage/resource impact and resolve automation loops, race conditions, & integration conflicts | Source: Assess storage/resource impact and resolve automation & integration conflicts (https://learn.microsoft.com/en-us/power-platform/admin/capacity-storage)]

- **A:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **B:** Correct. Column filters, actor exclusions, and `If-Match` row-version headers eliminate infinite ping-pong loops and silent lost-update race conditions.
- **C:** Correct. Keeping relational `Database` capacity lean prevents tenant admin lockouts (`Copy`/`Restore` blocks) and controls storage overage costs.
- **D:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **E:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q092 (`E2Q097`) — Implement the solution [3.7] · *Multi-Select (Select 2)*

Case study — Aegis Clinical Trials: During UAT rehearsal, an ad-hoc form edit made directly inside UAT prevented Managed Solution `Intake v3.2` column changes from appearing, while `Intake` failed to delete an obsolete column cleanly. Which two deployment practices resolve both issues? Select two.

- **A.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix
- **D.** Resolving deployment failures by running `Remove active customizations`, refactoring circular solution dependencies into a base layer, & validating stage JSON bindings
- **E.** Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, D` (`CSV: 3,4`)

Correct answers: C and D (are correct). Inspecting **Solution Layers** to run **`Remove active customizations`** on the form and importing `Intake v3.2` via Managed **`Stage for upgrade` -> `Apply upgrade`** (`dep_layers_deps` & `sol_segmented_alm`) strips the unmanaged layer and deletes obsolete components cleanly. [Skill 3.7: Resolve deployment plan issues, Unmanaged Active Solution Layers, and circular solution dependencies | Source: Resolve deployment plan, Solution Layer, and pipeline dependency issues (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Correct. Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.
- **D:** Correct. Stripping Unmanaged Active layers and decoupling circular references ensures repeatable, zero-touch Managed Solution Upgrades.
- **E:** Incorrect. Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.

</details>

### Q093 (`E2Q064`) — Architect a solution [2.9] · *Single-Answer Multiple Choice*

Why can CareStride Home Nursing **not** use Dataverse Virtual Tables for the `Patient_Visit_Chart` records that rural nurses create and update on iPads during 6-hour cellular dead zones?

- **A.** Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication
- **B.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways
- **C.** Replicating data into native Dataverse tables (`Dataflows` / `ADF`) when Mobile Offline, row-level security roles, auditing, or SLAs are required
- **D.** Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Virtual Tables require live online queries to the external source and do not support `Mobile Offline` synchronization, `User/Team` row-level security, or native Dataverse column auditing; `Patient_Visit_Chart` must reside in native Dataverse tables. [Skill 2.9: Determine when to connect external data in place (Virtual tables) versus import/replicate into Dataverse | Source: Connect external data in place (Virtual tables) vs import/replicate into Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-virtual-entities)]

- **A:** Incorrect. Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.
- **B:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.
- **C:** Correct. Virtual tables do not support Mobile Offline sync, Dataverse row-level User/Team ownership, or native column auditing.
- **D:** Incorrect. Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.

</details>

### Q094 (`E2Q029`) — Perform solution envisioning and requirement analysis [1.11] · *Single-Answer Multiple Choice*

During discovery, Clinic North requires two physician signatures for controlled-substance waste while Clinic South requires one nurse + one pharmacist witness under identical state law. What should the Solution Architect guide?

- **A.** Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating
- **B.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **C.** Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions
- **D.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Harmonizing divergent local habits into one standardized, state-compliant future-state witness process avoids maintaining conflicting workflow branches needlessly. [Skill 1.11: Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria | Source: Refine high-level requirements into testable user stories and acceptance criteria (https://learn.microsoft.com/en-us/training/modules/propose-solution/)]

- **A:** Correct. Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.
- **B:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **C:** Incorrect. Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.
- **D:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.

</details>

### Q095 (`E2Q071`) — Architect a solution [2.12] · *Single-Answer Multiple Choice*

Confidential psychiatric evaluation PDFs attached to Dataverse cases must strictly inherit the exact row-level Dataverse `Security Role` and `Access Team` permissions of each case. Why must you avoid default SharePoint Document Management here?

- **A.** Mitigating SharePoint Document Management’s lack of automatic Dataverse ACL sync via Dataverse `File` columns, Azure Blob SAS, or custom ACL sync
- **B.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down
- **C.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **D.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Default SharePoint Document Management never synchronizes Dataverse row ACLs to SharePoint folders; storing psychiatric PDFs in native **Dataverse `File` columns** enforces exact row and column security automatically. [Skill 2.12: Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs) | Source: Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM) (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions)]

- **A:** Correct. Default SharePoint integration never copies Dataverse row permissions to SharePoint folders; confidential files require `File` columns or explicit ACL sync.
- **B:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.
- **C:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **D:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.

</details>

### Q096 (`E2Q052`) — Architect a solution [2.3] · *Single-Answer Multiple Choice*

Which visual design artifact explicitly communicates `1:N`, `N:N`, ownership types (`User/Team` vs `Organization`), and Alternate Keys across 35 Dataverse clinical tables?

- **A.** Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign
- **B.** Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Reusing `Component Libraries`, `PCF`, `Child Flows`, & `Custom Connectors`, documented via `ERD`, `Sequence`, & `Context` diagrams

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). An **Entity Relationship Diagram (`ERD`)** communicates Dataverse table schemas, ownership types, primary/alternate keys, and relationship cardinalities clearly across architects and developers. [Skill 2.3: Maximize component reuse (PCF, Component Libraries, Child Flows) and communicate designs visually | Source: Maximize component reuse (PCF, Component Libraries, Child Flows) & visual diagrams (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)]

- **A:** Incorrect. Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.
- **B:** Incorrect. Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Correct. Shared component catalogs eliminate duplicate maintenance, while visual architecture diagrams align technical and business stakeholders.

</details>

### Q097 (`E2Q009`) — Perform solution envisioning and requirement analysis [1.4] · *Single-Answer Multiple Choice*

A health insurer is merging three acquired regional TPAs (with inconsistent ICD-10 mappings, unindexed mainframe flat files, and only a 24-hour Sunday maintenance freeze) into Dataverse. Which estimation driver analysis is most accurate?

- **A.** Estimating migration/integration effort from source data cleanliness, transformations, API throughput windows, & cutover downtime
- **B.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **C.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **D.** Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Source data dirtiness, code-set crosswalk transformations, API throughput windows, and tight cutover freeze budgets dictate realistic migration effort and rehearsal cycles. [Skill 1.4: Identify and estimate data migration and integration efforts, complexity drivers, and alternatives | Source: Estimate migration and integration efforts and alternatives (https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview)]

- **A:** Correct. Realistic effort sizing accounts for legacy deduplication, schema mapping, historical volume, 5-minute API limits, and delta cutover rehearsals.
- **B:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **C:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **D:** Incorrect. Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.

</details>

### Q098 (`E2Q074`) — Architect a solution [2.14] · *Single-Answer Multiple Choice*

An EHR SQL Server runs inside an on-premises hospital server room behind a strict firewall with no Azure VNet extension, and cloud flows need secure read/write access without opening inbound firewall ports. Deploying an active-active `____` cluster satisfies this requirement.

- **A.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **B.** `VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources
- **C.** Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`
- **D.** Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A clustered **On-Premises Data Gateway** establishes outbound-only TLS relay channels over port `443` from the hospital LAN to Azure Service Bus Relay with high-availability failover and load balancing. [Skill 2.14: Assess VNet subnet delegation, Azure ExpressRoute nuances, Data Gateways, and IP firewall networking | Source: Assess VNet integration, Azure ExpressRoute, gateways, and IP firewall networking (https://learn.microsoft.com/en-us/power-platform/admin/vnet-support-overview)]

- **A:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **B:** Correct. VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.
- **C:** Incorrect. Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.
- **D:** Incorrect. ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.

</details>

### Q099 (`E2Q099`) — Implement the solution [3.8] · *Single-Answer Multiple Choice*

During Sunday morning cutover smoke testing while `Administration mode` is still active, which built-in roles are permitted to sign in to verify Production forms and views before opening access to 14,000 clinicians?

- **A.** Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`
- **B.** Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production
- **C.** Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`
- **D.** Enabling Dataverse `Administration mode` (blocking non-admins & background jobs) during cutover, followed by smoke tests & Application Insights hypercare

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). When Dataverse **`Administration mode`** is enabled, only users with **System Administrator** or **System Customizer** security roles can access the environment to run smoke validations prior to opening Production. [Skill 3.8: Identify go-live readiness gates, execute Administration mode cutovers, and manage hypercare telemetry | Source: Assess go-live readiness factors, Administration mode, and hypercare remediation (https://learn.microsoft.com/en-us/power-platform/admin/admin-mode)]

- **A:** Incorrect. Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.
- **B:** Incorrect. Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.
- **C:** Incorrect. Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.
- **D:** Correct. `Administration mode` guarantees a quiet database during final schema upgrade and delta migration before opening Production to users.

</details>

### Q100 (`E2Q089`) — Implement the solution [3.3] · *Single-Answer Multiple Choice*

A developer writes a single C# call inserting 500 `Lab_Observation` rows into one elastic/standard table using the Dataverse bulk message `____`, which executes dramatically faster and consumes far less compute than 500 individual `Create` calls.

- **A.** Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in
- **B.** Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs
- **C.** Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow
- **D.** Sizing 24-hour `Power Platform Request (PPR)` capacity and using `CreateMultiple` / `UpdateMultiple` / `$batch` (`ExecuteMultiple` `<= 1,000`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Dataverse bulk operations (`CreateMultiple` and `UpdateMultiple`) process homogeneous multi-row payloads in optimized server pipelines, outperforming individual calls and even generic `ExecuteMultiple` batches. [Skill 3.3: Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits | Source: Ensure conformance to Dataverse Service Protection & Power Platform API limits (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits)]

- **A:** Incorrect. Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.
- **B:** Incorrect. Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.
- **C:** Incorrect. Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.
- **D:** Correct. Bulk messages (`CreateMultiple`/`UpdateMultiple`) and `$batch` cut network round-trips dramatically while keeping daily PPR consumption within entitlements.

</details>

