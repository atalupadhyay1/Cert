"""32 four-step ordered sequence options (8 groups x 4) for Exam PL-600 (all labels <= 255 chars)."""

SEQUENCES = {
    # 1. Domain 1 (1.1): Power Platform Well-Architected Envisioning & Discovery Sequence
    'seq_envision_wa_ok': (
        'Capture business outcomes, KPIs, & risk constraints → Map current-state processes & existing enterprise systems → Refine functional & non-functional requirements → Align target architecture to Power Platform Well-Architected pillars',
        'Solution envisioning establishes measurable business outcomes and risks first, inventories current processes/systems, refines functional & NFR specs, and aligns design trade-offs to Well-Architected pillars.',
    ),
    'seq_envision_wa_bad_code': (
        'Write custom C# plug-ins on Day 1 → Purchase all Dynamics 365 licenses blindly → Skip current-state discovery → Capture non-functional requirements after Production go-live',
        'Coding or buying licenses before discovery and NFR capture causes costly rework and architectural mismatches.',
    ),
    'seq_envision_wa_bad_lift': (
        'Copy every legacy Access table 1-for-1 into Dataverse → Replicate broken manual steps verbatim → Ignore API and storage limits → Run fit/gap analysis during user acceptance testing',
        'Lifting and shifting broken legacy schemas without process optimization or fit/gap analysis perpetuates technical debt.',
    ),
    'seq_envision_wa_bad_dlp': (
        'Grant System Administrator to all stakeholders → Build prototypes in personal My Flows → Skip security & residency discovery → Export Unmanaged Default Solution to Production',
        'Prototyping in Default Solution with over-privileged accounts violates governance and creates un-deployable artifacts.',
    ),

    # 2. Domain 1 (1.9): Authoritative Data Source & Master Data Discovery Sequence
    'seq_datasource_disc_ok': (
        'Inventory candidate enterprise data sources & owners → Classify data sensitivity, residency, & compliance rules → Assess data quality, volume, & latency needs → Decide per entity whether to connect in place or replicate into Dataverse',
        'Architects identify authoritative systems of record first, classify regulatory sensitivity/residency, evaluate quality/volume/latency, and then choose virtual in-place access vs Dataverse replication.',
    ),
    'seq_datasource_disc_bad_dup': (
        'Duplicate 100% of ERP tables into Dataverse nightly → Ignore master-data ownership → Allow dual uncoordinated edits without conflict rules → Cleanse duplicates manually after go-live',
        'Blindly duplicating authoritative ERP tables without master-data ownership or conflict governance causes severe data drift.',
    ),
    'seq_datasource_disc_bad_sql': (
        'Expose on-premises SQL Server ports directly to the public internet → Share one SQL `sa` login across Canvas apps → Skip data classification → Disable Dataverse auditing',
        'Exposing raw database ports and sharing `sa` logins violates zero-trust security and bypasses Dataverse governance.',
    ),
    'seq_datasource_disc_bad_csv': (
        'Email daily CSV exports between departments → Let business units invent conflicting customer IDs → Skip deduplication standards → Import dirty spreadsheets straight into Production',
        'Manual CSV emailing without canonical keys or data quality standards corrupts downstream analytics and automations.',
    ),

    # 3. Domain 1 (1.15): Structured Fit/Gap Analysis & Resolution Prioritization Sequence
    'seq_fitgap_order_ok': (
        'Validate each requirement against out-of-the-box Dataverse & Dynamics 365 capabilities → Evaluate declarative low-code configuration → Assess vetted AppSource ISV solutions → Specify targeted pro-code extensions only for remaining gaps',
        'Fit/gap analysis prioritizes standard platform/Dynamics 365 features first, then declarative configuration, then supported AppSource ISVs, reserving custom code strictly for true differentiators.',
    ),
    'seq_fitgap_order_bad_code': (
        'Build bespoke React SPAs and C# plug-ins for every requirement first → Replace standard Dynamics 365 tables with custom tables → Ignore AppSource → Check standard features last',
        'Defaulting to custom code and duplicating restricted/standard Dynamics 365 tables inflates TCO and breaks product upgrades.',
    ),
    'seq_fitgap_order_bad_scope': (
        'Accept every stakeholder wish into Phase 1 without feasibility scoring → Skip MVP boundaries → Hardcode workarounds in Production → Defer licensing impact checks until billing',
        'Unbounded scope acceptance without feasibility or licensing evaluation derails timelines and budgets.',
    ),
    'seq_fitgap_order_bad_unsupported': (
        'Inject unsupported DOM-scraping JavaScript into Model-driven forms → Modify SQL indexes directly via TDS → Bypass security roles → Lock out Microsoft updates',
        'Unsupported DOM manipulation and direct SQL writes violate Microsoft supportability contracts and break on wave updates.',
    ),

    # 4. Domain 2 (2.5): Enterprise Data Migration Sequencing for Relational & Circular Schemas
    'seq_datamig_order_ok': (
        'Cleanse & stage data with Alternate Keys / CMT GUIDs → Suppress non-essential flows & custom plug-ins → Load parent tables first (deferring circular lookups) → Bind deferred lookups, reconcile counts, & re-enable automations',
        'Enterprise migrations stage cleansed data, suppress noisy automations (`BypassCustomPluginExecution`), load parents before children while resolving circular lookups in a second pass, and reconcile counts before re-enabling flows.',
    ),
    'seq_datamig_order_bad_child': (
        'Load child line-items before parent Account rows exist → Leave all welcome-email cloud flows enabled → Run single-row serial inserts with no batching → Fix orphaned lookups manually in Prod',
        'Loading child rows first fails referential integrity, and leaving notification flows active spams thousands of customers.',
    ),
    'seq_datamig_order_bad_guid': (
        'Let each environment generate random GUIDs for reference/configuration tables → Hardcode Dev GUIDs inside cloud flows → Import raw unvalidated CSVs → Skip reconciliation',
        'Mismatched reference-data GUIDs across Dev, UAT, and Prod break business rules, views, and workflow conditions.',
    ),
    'seq_datamig_order_bad_tds': (
        'Execute `INSERT INTO account` over Dataverse TDS port 5558 → Remove platform SQL foreign keys → Copy `.mdf` database files from Azure SQL → Reboot the tenant',
        'Dataverse’s TDS endpoint (`5558`) is strictly read-only; all writes must use Dataverse Web API/SDK, Dataflows, ADF, or Configuration Migration Tool.',
    ),

    # 5. Domain 2 (2.11): Decoupled Enterprise Event Integration Pattern (Dataverse -> Azure -> ERP)
    'seq_event_integ_ok': (
        'Register a Dataverse Service Endpoint (`Service Bus` / `Event Grid`) → Publish row events asynchronously on commit → Buffer & transform via Azure Functions / Logic Apps with DLQ → Upsert idempotently into ERP via Alternate Keys',
        'Asynchronous Dataverse Service Endpoints -> Azure Service Bus/Event Grid -> Azure Functions/Logic Apps with Dead-Letter Queues and idempotent Alternate Key upserts decouple Dataverse from ERP latency and outages.',
    ),
    'seq_event_integ_bad_sync': (
        'Call slow on-premises ERP SOAP endpoints inside a synchronous Pre-Operation Dataverse plug-in → Hold SQL transaction locks for 90 seconds → Ignore HTTP 429/503 errors → Lose failed payloads permanently',
        'Long network calls inside synchronous plug-ins exhaust Dataverse worker threads, lock SQL transactions, and lose messages when endpoints go offline.',
    ),
    'seq_event_integ_bad_poll': (
        'Poll all 10 million Dataverse rows every 10 seconds without `modifiedon` or Change Tracking → Overrun 5-minute Service Protection limits → Overwrite newer ERP records blindly → Disable TLS',
        'Full-table polling without Dataverse Change Tracking triggers `HTTP 429` throttling and causes lost-update race conditions.',
    ),
    'seq_event_integ_bad_client': (
        'Embed ERP admin client secrets inside browser JavaScript web resources → Call ERP directly from user browsers bypassing CORS & DLP → Log failed payloads to browser `console.log` → Skip auditing',
        'Exposing secrets in client-side JavaScript is a critical security vulnerability.',
    ),

    # 6. Domain 2 (2.15): Designing Least-Privilege Entra Group Team & Matrix BU Security
    'seq_sec_model_ok': (
        'Model Business Units around isolation boundaries (with Modernized BUs for matrix access) → Author custom least-privilege Security Roles → Bind roles to Entra Security Group Teams → Layer Column Security & Access Team Templates',
        'Scalable Dataverse security aligns BUs to isolation boundaries, layers custom least-privilege roles onto Entra Security Group Teams for zero-touch provisioning, and handles exceptions via Access Teams and Column Security.',
    ),
    'seq_sec_model_bad_sysadmin': (
        'Place all users in one root BU with Organization-level Read/Write/Delete → Clone System Administrator for power users → Hide restricted fields using client-only JavaScript → Share individual records manually',
        'Client-side JavaScript never secures data at the API layer, and manual per-record sharing bloats the PrincipalObjectAccess (`POA`) table.',
    ),
    'seq_sec_model_bad_bu': (
        'Create 400 micro Business Units mirroring every HR cost center → Move users between BUs daily (wiping roles prior to modern settings) → Duplicate 400 identical copies of every Security Role → Audit nothing',
        'Over-fragmenting Business Units for reporting rather than true security boundaries creates massive administrative overhead.',
    ),
    'seq_sec_model_bad_sharepoint': (
        'Store confidential M&A contracts in default SharePoint Document Management folders → Assume SharePoint automatically inherits Dataverse row-level Security Roles & Access Teams → Grant site-wide Read to all employees → Go live',
        'Out-of-the-box SharePoint Document Management does NOT synchronize Dataverse row-level security ACLs to SharePoint folders automatically.',
    ),

    # 7. Domain 3 (3.3): Remediating Dataverse HTTP 429 Service Protection Throttling at Scale
    'seq_api_throttle_ok': (
        'Pinpoint throttled callers in Dataverse API analytics → Batch writes via `CreateMultiple` / `$batch` & use Change Tracking → Pool high-volume S2S loads across Entra Application Users → Honor HTTP `429` `Retry-After` backoff',
        'Resolving Service Protection (`6,000` req / `20` min compute per 5-min window) combines batch/bulk operations, Change Tracking, pooled S2S Application Users where appropriate, and honoring `Retry-After` backoff.',
    ),
    'seq_api_throttle_bad_loop': (
        'Spin up 50 parallel threads under one single user account → Retry HTTP 429 errors immediately with 0 ms delay → Replace filtered queries with full `SELECT *` scans → Open a ticket asking Microsoft to disable platform limits permanently',
        'Immediate zero-delay retries under a single user identity amplify `HTTP 429` throttling and extend penalty windows.',
    ),
    'seq_api_throttle_bad_sync': (
        'Move bulk integration loops inside synchronous Dataverse plug-ins → Chain 8 child plug-in updates per row → Enable `RetrieveAllEntities` metadata calls on every transaction → Disable caching',
        'Heavy metadata calls and chained synchronous updates multiply execution time against the 20-minute per-5-minute sliding window limit.',
    ),
    'seq_api_throttle_bad_lic': (
        'Buy 100 Power BI Free licenses expecting them to lift 5-minute Service Protection caps → Hardcode personal maker credentials → Ignore `x-ms-ratelimit-time-remaining-xrm-requests` headers → Discard throttled records silently',
        'Service Protection limits protect real-time platform stability per user/web server over 5-minute windows regardless of license SKU.',
    ),

    # 8. Domain 3 (3.6): Production Cutover & Hypercare Go-Live Execution Sequence
    'seq_cutover_golive_ok': (
        'Freeze changes & verify backup restore point → Enable Dataverse `Administration mode` (blocking regular users & async jobs) → Apply Managed Upgrades & run validated delta loads → Exit `Administration mode`, smoke-test, & monitor hypercare',
        'Controlled cutovers establish restore points, engage `Administration mode` to prevent user writes and background noise, apply Managed Upgrades + delta loads, validate smoke tests, and transition to monitored hypercare.',
    ),
    'seq_cutover_golive_bad_live': (
        'Allow 5,000 users to edit records during live schema upgrade and migration → Import Unmanaged solutions into Production → Skip smoke tests → Turn on auditing two months later',
        'Concurrent user edits during cutover cause migration collisions, lock timeouts, and inconsistent business state.',
    ),
    'seq_cutover_golive_bad_delete': (
        'Delete existing Managed Solutions in Production (erasing live tables!) → Re-import from scratch → Manually re-type Connection References & Environment Variables → Disable backups',
        'Deleting a Managed Solution erases its custom Dataverse tables and production data; always use Managed `Stage for upgrade` -> `Apply upgrade`.',
    ),
    'seq_cutover_golive_bad_nocap': (
        'Ignore Dataverse Database/File storage overages blocking admin ops → Skip Solution Checker critical findings → Leave Dev URLs in Environment Variables → Disband support team at launch minute',
        'Exceeded Dataverse storage entitlements block environment copy/restore/admin operations and sabotage cutover readiness.',
    ),
}
