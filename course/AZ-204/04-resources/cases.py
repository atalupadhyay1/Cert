"""Twenty-four original Azure developer case-study scenarios (four 3-question cases per mock exam).

Every scenario packs concrete developer constraints — compute SKU, storage engine,
identity boundary, throughput/latency, and integration protocol — while staying
concise enough (<650 chars) for self-contained stem embedding under 1,000 chars.
Official Microsoft case studies (Contoso, Litware, VanArsdel, Wide World Importers,
Coho Winery) are never reused or paraphrased.
"""
CASES = {
    # --- Exam 1: Omnichannel Retail, Flash-Sale Checkout, and Loyalty APIs ---
    'Vespera Retail': (
        'Vespera Retail runs an ASP.NET Core storefront on Azure App Service (Standard S2, Linux) backed by '
        'Azure Cosmos DB for NoSQL partitioned by `/customerId` and Azure Blob Storage for receipts. Flash drops '
        'spike checkout requests 15x within two minutes. Zero-downtime deployments must keep the `Production` '
        'payment webhook URL strictly off `staging` slots, and developers are forbidden from storing connection '
        'strings in `appsettings.json` or GitHub repositories.'
    ),
    'Kova Footwear': (
        'Kova Footwear ingests warehouse RFID scans into Azure Container Apps and stores inventory state in '
        'Cosmos DB. Every stock depletion must notify downstream marketplace partners within three seconds '
        'through HTTPS webhooks that strip internal warehouse IDs, while preserving failed partner deliveries '
        'for 24 hours in Blob Storage. External partner apps call Kova APIs through Azure API Management '
        'Developer/Standard v2 using Microsoft Entra bearer tokens.'
    ),
    'BriskCart Loyalty': (
        'BriskCart Loyalty processes point redemptions across 1,200 stores. Store POS terminals enqueue '
        'redemption commands that must execute strictly in per-member FIFO order and ignore duplicate retries '
        'sent within ten minutes when store Wi-Fi flaps. A C# isolated-worker Azure Function processes '
        'redemptions, reads signing keys from Azure Key Vault, and exports distributed OpenTelemetry traces '
        'to Azure Monitor Application Insights without exceeding a 5 GB/day ingestion cap.'
    ),
    'Cinder Coffee Roasters': (
        'Cinder Coffee Roasters hosts a B2B wholesale portal registered in a single-tenant Microsoft Entra ID '
        'directory. Wholesale buyers with the `WholesaleBuyer` app role upload PDF purchase orders directly from '
        'a React SPA to Azure Blob Storage without proxying 80 MB files through the web API, and uploaded PDFs '
        'must transition automatically to Cool storage after 30 days and delete after 365 days.'
    ),

    # --- Exam 2: Healthcare Patient Portals, Clinical Lab Telemetry, and Claims EDI ---
    'Aurelia Health': (
        'Aurelia Health operates a patient-scheduling Web App on Azure App Service Premium v3 and an isolated '
        'worker Azure Functions app on Flex Consumption. Clinicians sign in with Microsoft Entra ID and view '
        'team shift calendars pulled from Microsoft Graph. Audit compliance requires capturing HTTP 5xx server '
        'diagnostics to Blob Storage for 90 days and rotating all Key Vault secrets without restarting web workers.'
    ),
    'Trellis Diagnostics': (
        'Trellis Diagnostics streams 40,000 analyzer telemetry frames per second from hospital labs into Azure '
        'Event Hubs (16 partitions). Two independent consumers — a live anomaly-scoring Container App and an '
        'archival compliance indexer — must read the full stream concurrently at their own offsets while raw '
        'Avro batches land automatically in Azure Data Lake Storage Gen2 every five minutes.'
    ),
    'Vireo Specialty Pharmacy': (
        'Vireo Specialty Pharmacy stores prescription fulfillment documents in Azure Cosmos DB for NoSQL using '
        'hierarchical partition keys (`/clinicId`, `/patientId`). Pharmacists must always read their own '
        'in-session writes immediately, while two downstream microservices — cold-chain label printing and '
        'insurer EDI notification — must react independently to every newly created or updated prescription item.'
    ),
    'Solace Telemed': (
        'Solace Telemed fronts twelve internal clinical microservices with Azure API Management inside a virtual '
        'network. Partner clinics authenticate with mutual TLS client certificates plus subscription keys, '
        'GET lookups on `/formulary` should be cached for 300 seconds per `Accept-Language` header, and backend '
        '`X-AspNet-Version` headers must never leak to external callers.'
    ),

    # --- Exam 3: FinTech Instant Payments, Ledger Reconciliation, and Fraud Webhooks ---
    'Crestline Clearing': (
        'Crestline Clearing runs containerized settlement workers in Azure Container Apps connected to an Azure '
        'Service Bus Premium namespace and an Azure Container Registry with admin user disabled. Settlement '
        'batches arrive on a Service Bus queue; KEDA must scale worker replicas from 0 to 30 based on active '
        'queue depth using a user-assigned managed identity, with zero credentials stored in YAML manifests.'
    ),
    'Halcyon Custody': (
        'Halcyon Custody stores immutable trade confirmations in Azure Blob Storage with versioning and legal '
        'hold policies enabled, and stores account ledger entries in Cosmos DB within single-partition batches. '
        'When a custodian updates multiple ledger lines for the same `/accountNumber`, either every write must '
        'commit atomically or the entire batch must roll back without partial state.'
    ),
    'Pillar Remit': (
        'Pillar Remit exposes a cross-border FX quote API via Azure API Management. Free-tier fintech sandboxes '
        'must be capped at 60 calls per minute per subscription (returning HTTP 429) and 5,000 calls per month '
        '(returning HTTP 403), while enterprise corridors call an App Configuration store using dynamic '
        'sentinel-key refresh and feature flags gated by rollout percentage.'
    ),
    'Bramble Insure': (
        'Bramble Insure processes roadside-claim photo uploads on Azure Functions triggered by Event Grid '
        'BlobCreated events rather than polling Blob Storage, cutting idle storage-transaction bills. Every '
        'claim workflow correlates front-end SPA telemetry, APIM gateway requests, Function executions, and '
        'SQL/Cosmos dependencies inside a single Application Insights transaction view.'
    ),

    # --- Exam 4: Connected Fleet IoT, Cold-Chain Logistics, and Port Customs ---
    'Strider ColdChain': (
        'Strider ColdChain monitors 25,000 refrigerated trailers emitting reefer temperatures every ten seconds '
        'into Azure Event Hubs. A .NET 8 `EventProcessorClient` hosted on Azure Container Apps checkpoints '
        'progress in Azure Blob Storage, while excursion events (`tempC > 4.0`) publish to an Azure Event Grid '
        'custom topic subscribed to by regional dispatchers filtered by subject prefix `/region/eu-west/`.'
    ),
    'Mariner PortOps': (
        'Mariner PortOps runs customs-manifest APIs on Azure App Service Linux containers deployed from a '
        'geo-replicated Azure Container Registry. Customs brokers upload XML manifests to Blob Storage where '
        'a single active processing worker must acquire a 60-second exclusive lock on each manifest blob before '
        'updating status metadata so concurrent workers never double-file customs declarations.'
    ),
    'Zephyr Parcel': (
        'Zephyr Parcel coordinates hub sorting across Service Bus topics. Hazardous-material parcels (`hazmat = true`) '
        'must route to a dedicated compliance subscription that stamps `Priority = High` onto brokered message '
        'properties, while unprocessable poison messages exceeding five delivery attempts move automatically to '
        'the subscription dead-letter queue for ops inspection.'
    ),
    'Aegis Rail': (
        'Aegis Rail hosts internal track-inspection web apps secured with App Service built-in authentication '
        '(Microsoft Entra provider) returning HTTP 401 rather than interactive redirects for unauthenticated '
        'API clients. Inspection microservices authenticate to Azure Key Vault and Azure Queue Storage via '
        '`DefaultAzureCredential` during both local Visual Studio debugging and deployed Azure hosting.'
    ),

    # --- Exam 5: Multi-Tenant B2B SaaS, DevTools Telemetry, and Document Workflows ---
    'QuillSign SaaS': (
        'QuillSign SaaS is a multi-tenant contract-signing platform registered in Microsoft Entra ID to accept '
        'work accounts from any customer Entra tenant (`AzureADMultipleOrgs`). Backend APIs validate tenant '
        'scopes and call Microsoft Graph on behalf of the signed-in user to read organizational manager chains '
        'without requesting excessive directory-wide admin privileges.'
    ),
    'Pulsar Metrics': (
        'Pulsar Metrics runs bursting nightly customer-usage rollups as containerized jobs without maintaining '
        'always-on HTTP ingress, pulling container images built in the cloud via ACR Tasks whenever commits land '
        'on `main`. Rollup results land in Cosmos DB where multi-field `ORDER BY tenantId ASC, recordedAt DESC` '
        'queries must execute with minimal RU consumption.'
    ),
    'Loomis Cloud ERP': (
        'Loomis Cloud ERP exposes versioned `/v1/invoices` and `/v2/invoices` endpoints in Azure API Management '
        'while testing non-breaking OpenAPI edits safely before making them current. When a downstream tax '
        'service intermittently returns HTTP 503, APIM must retry up to three times before falling back cleanly, '
        'and availability alerts must notify on-call teams if synthetic multi-region probes fail from two+ locations.'
    ),
    'Cobalt FieldService': (
        'Cobalt FieldService dispatches technician work orders using Azure Functions (isolated worker model) '
        'with timer triggers running every 15 minutes during weekday business hours and Queue Storage output '
        'bindings. Field mobile apps download encrypted schematic blobs using short-lived HTTPS-only SAS tokens '
        'signed by Microsoft Entra credentials rather than storage account shared keys.'
    ),

    # --- Exam 6: Digital Media Streaming, Live Ticketing, Gaming Backends, and Smart Energy ---
    'Lyric Arena Ticketing': (
        'Lyric Arena Ticketing handles stadium on-sale events on Azure Container Apps with HTTP scale rules and '
        'Cosmos DB for seat-hold documents that must expire and vanish automatically after 600 seconds if unpaid, '
        'without running background delete sweeps. Optimistic concurrency via ETags prevents two fans from '
        'claiming the same seat document simultaneously.'
    ),
    'NovaGrid Energy': (
        'NovaGrid Energy collects substation voltage alerts through Azure Event Grid domains serving 80 municipal '
        'utilities under tenant-scoped event topics. Critical transformer alerts forward to an Azure Service Bus '
        'queue consumed by an Azure Function, while Application Insights custom metrics and KQL log alerts watch '
        'for webhook delivery latency above 1,500 ms.'
    ),
    'EmberPlay Studios': (
        'EmberPlay Studios runs seasonal multiplayer leaderboards on Azure App Service with `Staging` and '
        '`Production` slots, routing 10% of live player traffic to `Staging` for canary validation before '
        'swapping. Player replay archives in Blob Storage move from Hot to Cold after 14 days and Archive after '
        '90 days, with priority rehydration required when dispute moderators request archived replays.'
    ),
    'Prism Newsroom': (
        'Prism Newsroom ingests breaking wire feeds into Azure Functions, enriches metadata via Azure App '
        'Configuration feature flags and Key Vault-backed secrets, and publishes partner feeds through Azure '
        'API Management. A self-hosted APIM gateway deployed in Prism on-premises broadcast centers keeps '
        'local newsroom API traffic inside the facility while syncing configuration from Azure every ten seconds.'
    ),
}
