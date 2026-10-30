"""Canonical reusable option & distractor library for Microsoft Exam PL-600 (Power Platform Solution Architect Expert)."""

from sequences import SEQUENCES

BASE_TERMS = {
    # Domain 1: Perform solution envisioning and requirement analysis (1.1 - 1.18)
    'wa_reliability': (
        'Power Platform Well-Architected `Reliability` pillar (RPO/RTO targets, fault isolation, retries, & circuit breakers)',
        'The Reliability pillar ensures mission-critical workloads withstand transient outages, throttling, and regional faults within defined RPO/RTO bounds.',
    ),
    'wa_security': (
        'Power Platform Well-Architected `Security` pillar (Zero Trust Entra identity, least privilege, DLP, & encryption)',
        'The Security pillar protects confidentiality and integrity through Entra Conditional Access, least-privilege roles, DLP endpoint rules, and CMK/Lockbox.',
    ),
    'wa_operational': (
        'Power Platform Well-Architected `Operational Excellence` pillar (automated ALM pipelines, Application Insights, & CoE)',
        'Operational Excellence standardizes CI/CD solution pipelines, automated Solution Checker gates, telemetry, and Managed Environment governance.',
    ),
    'wa_performance': (
        'Power Platform Well-Architected `Performance Efficiency` pillar (delegable queries, API throughput budgets, & elastic scaling)',
        'Performance Efficiency optimizes response latency and resource utilization via query delegation, indexing, batching, and Elastic/async patterns.',
    ),
    'wa_experience': (
        'Power Platform Well-Architected `Experience Optimization` pillar (task-focused UX, WCAG accessibility, & persona alignment)',
        'Experience Optimization designs intuitive, accessible, low-friction user journeys tailored to each persona’s cognitive workflow.',
    ),
    'comp_model_driven': (
        'Model-driven Power App over Microsoft Dataverse with responsive forms, views, dashboards, & Business Process Flows',
        'Model-driven apps excel at structured, data-dense back-office case and lifecycle management directly atop Dataverse security.',
    ),
    'comp_canvas_mobile': (
        'Canvas Power App with a `Mobile Offline` profile and device-native camera/barcode UX tailored to frontline tasks',
        'Canvas apps give pixel-level task UX and offline-first Dataverse synchronization for field workers operating without connectivity.',
    ),
    'comp_power_pages': (
        'Microsoft Power Pages external portal secured with `Table Permissions`, `Web Roles`, & `Entra External ID`',
        'Power Pages scales securely to thousands or millions of external customers, citizens, or partners accessing Dataverse rows online.',
    ),
    'comp_copilot_studio': (
        'Microsoft Copilot Studio agent grounded in enterprise knowledge sources, Dataverse actions, & live omnichannel handoff',
        'Copilot Studio delivers governed conversational and autonomous agents across Teams, web portals, and customer service channels.',
    ),
    'comp_ai_builder': (
        'AI Builder prebuilt/custom document processing, text classification, & AI Prompts integrated natively in Power Platform',
        'AI Builder embeds governed document extraction and generative AI prompts directly inside flows and apps without custom ML infrastructure.',
    ),
    'comp_d365_firstparty': (
        'Dynamics 365 first-party app (`Sales`, `Customer Service`, or `Field Service`) leveraging native schemas, SLAs, & RSO scheduling',
        'Adopting Dynamics 365 first-party apps avoids reinventing complex case routing, omnichannel queues, or Resource Scheduling Optimization.',
    ),
    'comp_appsource_isv': (
        'Vetted Microsoft AppSource ISV Managed Solution with vendor SLA support for specialized vertical compliance',
        'Certified AppSource ISV packages accelerate specialized capabilities (such as regulated e-signature, tax, or CTI) with lower TCO than bespoke builds.',
    ),
    'comp_azure_procode': (
        'Azure pro-code extension (`Azure Functions`, `Service Bus`, `AKS`, or `Azure AI Foundry`) integrated with Power Platform',
        'Heavy compute, long-running algorithms (> 2 minutes), and high-throughput brokered messaging offload cleanly to Azure extensions.',
    ),
    'est_migration_drivers': (
        'Estimating migration/integration effort from source data cleanliness, transformations, API throughput windows, & cutover downtime',
        'Realistic effort sizing accounts for legacy deduplication, schema mapping, historical volume, 5-minute API limits, and delta cutover rehearsals.',
    ),
    'disc_process_mining': (
        'Power Automate Process Mining & Task Mining paired with cross-functional current-state discovery workshops',
        'Combining telemetry-driven Process/Task Mining with SME workshops exposes hidden rework loops and shadow processes objectively.',
    ),
    'disc_shadow_it': (
        'Inventorying departmental Excel macros, Access databases, and shadow-IT workarounds to retire manual data silos',
        'Uncovering unofficial spreadsheets and shadow tools during discovery prevents critical edge cases from surfacing post-go-live.',
    ),
    'disc_raci_governance': (
        'Establishing a fusion-team `RACI` matrix, Architecture Review Board (`ARB`), and Center of Excellence (`CoE`) operating model',
        'Clear architectural ownership, ARB design gates, and CoE guardrails align business, citizen makers, pro-devs, and InfoSec.',
    ),
    'risk_regulatory_geo': (
        'Assessing sovereign data-residency (`Multi-Geo`), PII/PHI/ITAR compliance, `CMK`, & cross-border connector risks upfront',
        'Identifying residency and regulatory encryption constraints during envisioning prevents illegal cross-region tenant/environment placement.',
    ),
    'risk_spo_governance': (
        'Mitigating single-maker bus-factor risk, unmonitored personal flows, & technical debt via Managed Environments and CoE',
        'Unmanaged citizen sprawl and bespoke code without ALM pipelines represent top organizational operational risks.',
    ),
    'kpi_smart_metrics': (
        'Defining baseline-backed `SMART` success KPIs (cycle-time reduction, error-rate drop, SLA adherence, & active adoption %)',
        'Quantifiable KPIs anchored to current-state baselines let stakeholders verify objective ROI after go-live.',
    ),
    'ea_landscape_map': (
        'Enterprise Architecture Context Diagram mapping systems of record, Entra tenants, hybrid networks, & sync/async SLAs',
        'Evaluating the enterprise landscape clarifies authoritative boundaries, identity federation, firewall paths, and integration patterns.',
    ),
    'data_master_owner': (
        'Designating a single authoritative System of Record per entity with explicit survivorship and conflict-resolution rules',
        'Every master entity (`Customer`, `Item`, `GL Account`) needs one clear authoritative owner to prevent bi-directional data corruption.',
    ),
    'data_quality_rules': (
        'Defining pre-cutover data quality standards (deduplication keys, mandatory completeness, referential integrity, & domain mappings)',
        'Enforcing cleansing and deduplication gates before migration prevents garbage-in/garbage-out failures in Dataverse.',
    ),
    'data_cdm_schema': (
        'Aligning data entities to the Microsoft Common Data Model (`CDM`) standard tables (`Account`, `Contact`, `Activity`)',
        'Extending standard CDM tables preserves native Dynamics 365, AppSource ISV, Exchange, and AI Copilot interoperability.',
    ),
    'req_user_story_ac': (
        'Refining prescriptive wishes into persona-based `User Stories` (`As a ... I need ... so that ...`) with testable Acceptance Criteria',
        'Outcome-oriented User Stories decouple business intent from premature UI assumptions and anchor QA test cases.',
    ),
    'req_functional_spec': (
        'Capturing Functional Requirements (persona workflows, state rules, approvals, offline CRUD scope, & statutory reports)',
        'Functional requirements specify what business behaviors and data transformations the solution must perform for each role.',
    ),
    'req_nfr_spec': (
        'Capturing Non-Functional Requirements (`RPO`/`RTO`, peak concurrency, `p95` latency, API volume, `WCAG 2.1 AA`, & retention)',
        'Non-functional requirements govern architectural sizing, BCDR, licensing capacity, offline design, and security controls.',
    ),
    'ux_wcag_accessible': (
        'Designing for `WCAG 2.1 AA` accessibility (`AccessibleLabel`, `TabIndex`, contrast) and `.resx` multi-language localization',
        'Building accessibility and localization into initial UX components avoids expensive retrofits before public or enterprise launch.',
    ),
    'proc_standardize_first': (
        'Harmonizing and simplifying fragmented legacy processes into a standardized future-state flow before automating',
        'Automating a broken 14-step legacy process yields a fast broken process; architects standardize core flows and isolate true regulatory exceptions.',
    ),
    'fitgap_categorize': (
        'Structured Fit/Gap matrix scoring requirements across `Out-of-the-Box`, `Configuration`, `AppSource ISV`, & `Custom Code`',
        'Formal fit/gap scoring exposes customization TCO, licensing impacts, and upgrade maintenance trade-offs transparently.',
    ),
    'd365_restricted_tbl': (
        'Validating Dynamics 365 restricted-table licensing (`Case / incident`, `Work Order`, `Entitlement`) during fit/gap analysis',
        'Restricted Dynamics 365 tables require appropriate Dynamics 365 licenses for CRUD operations rather than standalone Power Apps licenses.',
    ),
    'gap_lowcode_alt': (
        'Addressing gaps via supported extensibility (`Custom Pages`, `PCF`, `Power Fx Formula columns`, `Custom APIs`) over bespoke clones',
        'Supported platform extensibility closes UX and logic gaps while preserving Microsoft wave-update compatibility.',
    ),
    'scope_mvp_phased': (
        'Scoping a high-value `MVP` Phase 1 release using MoSCoW prioritization and formal change-request governance',
        'Phased MVP delivery de-risks go-live, delivers early business value, and prevents uncontrolled scope creep.',
    ),

    # Domain 2: Architect a solution (2.1 - 2.17)
    'sol_segmented_alm': (
        'Segmented Managed Solution topology (`Base Schema` -> `Shared Logic` -> `Persona Apps`) under one custom Publisher prefix',
        'Layered solution segmentation isolates release cadences, shrinks import times, and prevents monolithic lock contention.',
    ),
    'ux_proto_pcf': (
        'Validating interactive UX prototypes (`Figma-to-App` / `Custom Pages`) early and building `PCF` controls for specialized UI gaps',
        'Interactive prototyping validates user journeys cheaply, while Power Apps Component Framework (`PCF`) renders reusable custom TypeScript/React controls.',
    ),
    'reuse_comp_diag': (
        'Reusing `Component Libraries`, `PCF`, `Child Flows`, & `Custom Connectors`, documented via `ERD`, `Sequence`, & `Context` diagrams',
        'Shared component catalogs eliminate duplicate maintenance, while visual architecture diagrams align technical and business stakeholders.',
    ),
    'app_persona_split': (
        'Grouping capabilities into role- and task-specific apps (offline Canvas for field crews, Model-driven for back-office, Power Pages for externals)',
        'Task-focused apps per persona outperform bloated one-size-fits-all apps in load speed, offline footprint, and usability.',
    ),
    'mig_staging_altkey': (
        'Staging cleansed records via `ADF` / `SSIS` using Dataverse `Alternate Keys` (`Upsert`) and `Configuration Migration Tool` for fixed-GUID config rows',
        'Alternate Keys eliminate GUID pre-lookup round-trips on upserts, while CMT preserves exact reference-record GUIDs across Dev/UAT/Prod.',
    ),
    'viz_dataverse_native': (
        'Native Dataverse system charts, interactive experience dashboards, and views for real-time operational row drill-down',
        'Built-in Dataverse charts and dashboards enforce row/column security natively with zero extra Power BI licensing.',
    ),
    'viz_powerbi_fabric': (
        'Power BI Embedded (with RLS) for cross-system insights and `Microsoft Fabric Link` / `Azure Synapse Link` for multi-TB lakehouse analytics',
        'Power BI combines enterprise sources with RLS, while Fabric OneLake / Synapse Link offloads heavy analytical queries from transactional Dataverse.',
    ),
    'auto_sync_vs_async': (
        'Synchronous Dataverse plug-ins (`<= 2m`) strictly for atomic transaction validation/rollback; Cloud Flows / Logic Apps for async orchestration',
        'Keeping synchronous transaction pipelines fast and offloading external orchestrations asynchronously protects Dataverse SQL responsiveness.',
    ),
    'auto_bpf_guided': (
        'Multi-table Business Process Flows (`<= 30` stages, conditional branching, & stage security) guiding human lifecycle stages',
        'BPFs enforce consistent cross-stage data capture, gate transitions, and trigger automated flows on stage entry/exit.',
    ),
    'auto_logic_apps': (
        'Azure Logic Apps (Standard) for enterprise B2B EDI (`X12`/`AS2`/`EDIFACT`), VNet-isolated single-tenant workflows, & Azure Bicep ALM',
        'Logic Apps Standard complements Power Automate when Azure RBAC, private VNet compute, or B2B Enterprise Integration Pack codecs are required.',
    ),
    'env_multi_tier_coe': (
        'Dedicated `Dev -> Test -> UAT -> Prod` environments (plus sovereign `Multi-Geo` instances) governed by `Managed Environments` & `CoE Starter Kit`',
        'Multi-tier ALM environments isolate production workloads, Multi-Geo satisfies regional residency, and CoE + Managed Environments automate governance.',
    ),
    'rel_cascade_types': (
        'Configuring `Custom` / `Referential` cascading (avoiding unintended `Parental` `Cascade All` reparent storms) and manual `N:N` intersect tables',
        'Replacing `Parental` cascading on high-volume child tables prevents `POA` sharing storms, and manual `N:N` tables store rich relationship attributes.',
    ),
    'rel_polymorphic_hier': (
        'Modeling self-referential `Hierarchical` (`1:N` `Under` queries) and `Polymorphic` (`Customer` / multi-table) relationships',
        'Hierarchical relationships support native visual hierarchy rollups and `Under` OData operators across parent-child trees.',
    ),
    'data_virtual_tables': (
        'Dataverse `Virtual Tables` (`Virtual Connector Provider` / custom OData v4 provider) querying external systems in place without storage duplication',
        'Virtual tables surface external Azure SQL, Fabric, or ERP rows live inside Dataverse views/lookups without consuming Dataverse Database storage.',
    ),
    'data_import_replicate': (
        'Replicating data into native Dataverse tables (`Dataflows` / `ADF`) when Mobile Offline, row-level security roles, auditing, or SLAs are required',
        'Virtual tables do not support Mobile Offline sync, Dataverse row-level User/Team ownership, or native column auditing.',
    ),
    'tbl_elastic_activity': (
        'Dataverse `Elastic tables` (Cosmos DB horizontal partitioning + `TTL`) for high-velocity telemetry, and `File`/SharePoint/Blob offloading for binaries',
        'Elastic tables ingest tens of thousands of ephemeral JSON/IoT writes per minute with automatic `TTL` expiry without relational index contention.',
    ),
    'tbl_ownership_choice': (
        'Choosing `User or Team` table ownership for BU/row/team security vs `Organization` ownership for global config tables at creation time',
        'Table ownership (`User/Team` vs `Organization`) is immutable once created and determines whether BU, Team, and Hierarchy security apply.',
    ),
    'integ_teams_sp_d365': (
        'Integrating Microsoft Teams (`Adaptive Cards` / embedded apps), Dynamics 365 F&O `Dual-write` + `Business Events`, & `Server-Side Sync`',
        'Dual-write provides near-real-time bi-directional Dataverse-to-F&O sync, while Teams Adaptive Cards meet users directly in collaboration channels.',
    ),
    'integ_sp_acl_gap': (
        'Mitigating SharePoint Document Management’s lack of automatic Dataverse ACL sync via Dataverse `File` columns, Azure Blob SAS, or custom ACL sync',
        'Default SharePoint integration never copies Dataverse row permissions to SharePoint folders; confidential files require `File` columns or explicit ACL sync.',
    ),
    'integ_async_asb_apim': (
        'Decoupling integrations via `Azure API Management`, Dataverse `Service Endpoints` (`Azure Service Bus` queues/topics with DLQ), & `Event Grid`',
        'Brokered pub/sub messaging via Service Bus and Event Grid absorbs downstream ERP outages, preserves FIFO sessions, and enforces APIM throttling/auth.',
    ),
    'integ_custom_api': (
        'Defining solution-aware Dataverse `Custom APIs` exposing strongly typed request/response contracts for internal and external callers',
        'Custom APIs replace legacy Custom Process Actions with code-first, solution-aware OData bound/unbound operations and granular privilege checks.',
    ),
    'integ_virtual_connector': (
        'Using the `Virtual Connector Provider` (`SQL Server`, `SharePoint`, `Fabric`) to expose external tables in Dataverse with low-code setup',
        'The Virtual Connector Provider creates Virtual Tables over supported connectors without authoring custom C# data-provider plug-ins.',
    ),
    'auth_obo_s2s_mi': (
        'Using `OAuth 2.0 On-Behalf-Of (OBO)` to preserve caller identity/audit trails vs `Entra Service Principal (S2S)` / `Managed Identity` for background jobs',
        'OBO propagates the signed-in user’s identity downstream for row-level authorization, whereas S2S/Managed Identity runs headless workloads.',
    ),
    'bcdr_geo_rpa': (
        'Designing BCDR around Dataverse point-in-time backups (`28-day` Prod retention, cross-Geo failover limits) and `Hosted RPA` + `Work Queues` for legacy UI',
        'Architects align RPO/RTO to Microsoft’s managed geo-replication SLAs and isolate UI-only legacy integrations behind resilient RPA Work Queues.',
    ),
    'net_vnet_er_opdg': (
        '`VNet support for Power Platform` (`enterprisePolicies` subnet delegation) for private endpoints; `On-Premises Data Gateway` clusters for LAN sources',
        'VNet subnet delegation lets Dataverse plug-ins and connectors reach private endpoints privately, whereas ExpressRoute alone uses public peering IPs.',
    ),
    'sec_modern_bu_teams': (
        'Combining `Modernized Business Units` (matrix access), `Microsoft Entra ID Security Group Teams`, & `Access Team Templates`',
        'Modernized BUs enable cross-BU matrix roles, Entra Group Teams automate zero-touch RBAC, and Access Teams handle ad-hoc record collaboration cleanly.',
    ),
    'sec_poa_hygiene': (
        'Preventing `PrincipalObjectAccess (POA)` table bloat by replacing manual per-record sharing and `Parental` cascades with `Access Team Templates`',
        'Millions of `POA` rows from manual sharing and `Cascade All` relationships degrade SQL query performance across Dataverse views.',
    ),
    'sec_col_hier_pim': (
        'Layering `Column Security Profiles`, `Hierarchy Security` (`Manager`/`Position`), `CMK`, `Customer Lockbox`, & `Entra PIM` just-in-time admin access',
        'Sensitive fields require Column Security, executive visibility uses Hierarchy Security, and zero standing admin privileges use Entra PIM.',
    ),
    'sec_cond_access_ip': (
        'Enforcing `Microsoft Entra Conditional Access` (MFA & compliant device) plus `Power Platform IP Firewall` & `Cookie IP binding`',
        'Combining Entra Conditional Access with Managed Environment IP Firewall and session cookie binding blocks token replay from untrusted networks.',
    ),
    'sec_dlp_ext_access': (
        'Enforcing `DLP` + `Endpoint Filtering`, licensing external consumers via `Power Pages` (`Entra External ID`), & `Entra B2B` for internal-app guests',
        'Power Pages scales cost-effectively with `Table Permissions` for external portals, whereas Entra B2B suits external partners using internal apps.',
    ),

    # Domain 3: Implement the solution (3.1 - 3.8)
    'val_sol_app_checker': (
        'Enforcing `Solution Checker` and `App Checker` gates in CI/CD pipelines alongside `Power Platform Well-Architected` design reviews',
        'Solution Checker flags unbounded queries and sync plug-in anti-patterns, while App Checker catches delegation warnings and WCAG errors before release.',
    ),
    'val_sec_boundary_audit': (
        'Auditing server-side `Security Roles`, `Column Security`, & `Power Pages Table Permissions` rather than trusting client-side UI rules',
        'Client JavaScript and `Form`-scoped Business Rules never block Web API/OData access; security boundaries must be enforced server-side in Dataverse.',
    ),
    'val_load_telemetry': (
        'Running scale tests in UAT while streaming Dataverse and Canvas telemetry to `Azure Application Insights` (`dependencies` / `exceptions` KQL)',
        'Application Insights integration captures page-load latency, plug-in execution durations, and outbound dependency failures under realistic concurrency.',
    ),
    'lim_service_protection': (
        'Conforming to `Dataverse Service Protection` limits (`6,000` req / `20m` compute per `5-min` window), pooling `S2S Application Users`, & honoring `Retry-After`',
        'Service Protection enforces per-user/per-web-server 5-minute sliding caps (`HTTP 429`); pooling S2S Application Users and respecting `Retry-After` maximizes throughput.',
    ),
    'lim_ppr_batch_opt': (
        'Sizing 24-hour `Power Platform Request (PPR)` capacity and using `CreateMultiple` / `UpdateMultiple` / `$batch` (`ExecuteMultiple` `<= 1,000`)',
        'Bulk messages (`CreateMultiple`/`UpdateMultiple`) and `$batch` cut network round-trips dramatically while keeping daily PPR consumption within entitlements.',
    ),
    'res_conflict_loops': (
        'Resolving automation/integration conflicts via `Select columns` (`filteringattributes`), `Trigger Conditions`, plug-in `Depth` checks, & `ETag` (`If-Match`) optimistic concurrency',
        'Column filters, actor exclusions, and `If-Match` row-version headers eliminate infinite ping-pong loops and silent lost-update race conditions.',
    ),
    'cap_storage_tiering': (
        'Governing `Database`, `File`, & `Log` storage pools via `Dataverse Long Term Retention`, `Fabric/Synapse Link` archival, & attachment offloading',
        'Keeping relational `Database` capacity lean prevents tenant admin lockouts (`Copy`/`Restore` blocks) and controls storage overage costs.',
    ),
    'perf_canvas_dataverse': (
        'Fixing slowness via delegable `Filter`/`StartsWith` Canvas queries, indexed `Quick Find` columns (no leading `*` wildcards), & async plug-in refactoring',
        'Eliminating `N+1` gallery `LookUp`s, non-delegable predicates, leading-wildcard full table scans, and chained sync plug-ins restores sub-second UX.',
    ),
    'mig_bypass_cutover': (
        'Accelerating bulk loads with `BypassCustomPluginExecution` (`BypassBusinessLogicExecution`), disabled flows/search indexes, & parallel `CreateMultiple` batches',
        'Bypassing non-essential custom sync/async logic and disabling cloud flows during cutover prevents throttling and unintended notification storms.',
    ),
    'mig_delta_reconcile': (
        'Executing automated row-count/hash-total reconciliation and `Dataverse Change Tracking` / watermark delta loads during cutover freeze',
        'Delta loads keep downtime inside tight weekend cutover windows while automated financial/count reconciliation proves migration integrity.',
    ),
    'dep_layers_deps': (
        'Resolving deployment failures by running `Remove active customizations`, refactoring circular solution dependencies into a base layer, & validating stage JSON bindings',
        'Stripping Unmanaged Active layers and decoupling circular references ensures repeatable, zero-touch Managed Solution Upgrades.',
    ),
    'golive_admin_hypercare': (
        'Enabling Dataverse `Administration mode` (blocking non-admins & background jobs) during cutover, followed by smoke tests & Application Insights hypercare',
        '`Administration mode` guarantees a quiet database during final schema upgrade and delta migration before opening Production to users.',
    ),
    'golive_rollback_plan': (
        'Establishing signed-off `Go / No-Go` readiness gates, manual pre-cutover `Backup` restore points, rollback runbooks, & phased wave rollouts',
        'Clear Go/No-Go criteria, pre-upgrade backups, and phased pilot waves minimize blast radius during enterprise go-live.',
    ),

    # 16 Solution Architect Anti-Pattern Distractors (bad_*)
    'bad_client_br_sec': (
        'Hiding sensitive SSN/salary columns solely with client JavaScript or `Form`-scoped Business Rules without `Column Security Profiles`',
        'Client-side UI hiding leaves columns completely readable via OData Web API, Advanced Find, Excel export, and Power BI.',
    ),
    'bad_sync_plugin_http': (
        'Executing slow `45-second` outbound HTTP/SOAP calls inside a synchronous `Pre-Operation` Dataverse plug-in',
        'Long synchronous HTTP calls hold SQL transaction locks, exhaust worker threads, and fail the strict 2-minute sandbox limit.',
    ),
    'bad_single_s2s_flood': (
        'Firing 50 parallel migration threads under a single user login with `0 ms` immediate retries whenever `HTTP 429` occurs',
        'Concentrating parallel load on one user account and ignoring `Retry-After` triggers prolonged Service Protection throttling.',
    ),
    'bad_columnset_all': (
        'Querying and updating all 250 attributes via `ColumnSet(true)` (`SELECT *`) inside every synchronous plug-in and cloud flow',
        'Retrieving or updating all columns inflates memory/network payloads and fires unintended downstream column-change automations.',
    ),
    'bad_cascade_all_storm': (
        'Leaving `1:N` Account-to-Activity/Case relationships on `Parental` (`Cascade All` Assign/Share) across accounts with 200,000 historic activities',
        'Reassigning a parent Account with `Parental` cascading synchronously updates and shares all 200,000 child rows, causing SQL lock timeouts and `POA` bloat.',
    ),
    'bad_sp_inherits_dv': (
        'Assuming default `SharePoint Document Management` automatically replicates Dataverse row-level Security Roles and Access Teams onto SharePoint folders',
        'Out-of-the-box SharePoint integration creates folders with broad site library permissions and never syncs Dataverse row ACLs.',
    ),
    'bad_er_private_ip': (
        'Assuming `Azure ExpressRoute` alone places Microsoft Dataverse inside your private RFC1918 LAN without `VNet` delegation or Data Gateways',
        'ExpressRoute routes Microsoft cloud traffic over private circuits using public peering IPs; reaching private VNet IPs requires Power Platform VNet integration or gateways.',
    ),
    'bad_b2b_for_millions': (
        'Inviting 200,000 external retail consumers as internal `Microsoft Entra B2B` directory guests on a Model-driven app instead of `Power Pages`',
        'Managing hundreds of thousands of external consumers in internal Entra B2B + per-user app licenses is prohibitively costly and complex compared to Power Pages.',
    ),
    'bad_clone_restricted': (
        'Building custom `new_case` and `new_workorder` tables from scratch to duplicate Dynamics 365 Customer Service / Field Service',
        'Cloning restricted/first-party Dynamics 365 workloads violates multiplexing/restricted-table rules and forfeits native SLAs, routing, and RSO upgrades.',
    ),
    'bad_org_own_convert': (
        'Creating core customer tables with `Organization` ownership in MVP and planning to switch them to `User or Team` ownership in Phase 2',
        'Dataverse table ownership (`Organization` vs `User/Team`) is permanently locked at table creation and cannot be changed without recreating/migrating the table.',
    ),
    'bad_blob_in_db_col': (
        'Storing Base64-encoded 10 MB inspection photos and PDFs inside `Multiline Text` relational columns in Dataverse `Database` capacity',
        'Storing large binaries in relational columns bloats expensive Dataverse Database storage and degrades table scan performance.',
    ),
    'bad_unmanaged_monolith': (
        'Shipping all enterprise schemas, apps, and flows in a single `Unmanaged` solution (`Default Publisher` `new_`) imported straight into Production',
        'Monolithic Unmanaged Production deployments create permanent Active layers, cause multi-hour imports, and break Managed Upgrade governance.',
    ),
    'bad_virtual_offline': (
        'Using read-only OData `Virtual Tables` for rural field crews requiring `6-hour` `Mobile Offline` read/write sync and Dataverse row ownership',
        'Virtual Tables require live online connectivity to the external data source and do not support Mobile Offline or User/Team row security.',
    ),
    'bad_dualwrite_batch': (
        'Streaming 15,000 ephemeral IoT sensor alerts per minute through synchronous `Dynamics 365 Dual-write` into standard relational Dataverse tables',
        'Dual-write is designed for business master/transactional ERP-CRM sync, not high-velocity IoT telemetry streams (which belong in Event Hubs / Elastic tables / Fabric).',
    ),
    'bad_no_depth_loop': (
        'Deploying bi-directional Dataverse-to-ERP flows without `Select columns`, `Trigger Conditions`, or service-account exclusions',
        'Unfiltered bi-directional triggers bounce updates infinitely between systems, exhausting daily API allocations and corrupting timestamps.',
    ),
    'bad_lift_broken_sop': (
        'Lifting and shifting 45-tab legacy screens and redundant paper sign-offs 1-for-1 into Power Apps without future-state process redesign',
        'Digitizing broken legacy screens verbatim misses cloud simplification opportunities and degrades user adoption.',
    ),
}

assert set(BASE_TERMS).isdisjoint(set(SEQUENCES)), 'Duplicate keys between BASE_TERMS and SEQUENCES'
TERMS = {**BASE_TERMS, **SEQUENCES}
