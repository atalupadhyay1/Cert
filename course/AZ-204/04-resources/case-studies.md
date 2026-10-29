# Exam AZ-204 Case Study Briefs (Sets 1–6)

Every mock exam contains 4 original developer case studies of 3 questions (12 items per set, 24 scenarios total). Paste the relevant scenario into a Udemy practice-test description if uploading `practice-set-N.csv`, or upload `case-embedded-set-N.csv` where each case stem embeds the full scenario directly.

## Exam 1: Omnichannel Retail, Flash-Sale Checkout, and Loyalty APIs

### Case study — BriskCart Loyalty

BriskCart Loyalty processes point redemptions across 1,200 stores. Store POS terminals enqueue redemption commands that must execute strictly in per-member FIFO order and ignore duplicate retries sent within ten minutes when store Wi-Fi flaps. A C# isolated-worker Azure Function processes redemptions, reads signing keys from Azure Key Vault, and exports distributed OpenTelemetry traces to Azure Monitor Application Insights without exceeding a 5 GB/day ingestion cap.

Questions in this block:

1. Store POS terminals resend loyalty redemption commands over flaky Wi-Fi and require strict per-member FIFO execution while discarding retries carrying the same `MessageId` within ten minutes. How should the queue be configured? _(C)_
2. BriskCart's .NET 8 isolated-worker redemption Function must return an HTTP 200 receipt payload and write an audit document to Cosmos DB from the same invocation without `out` parameters. Which C# return structure works in the isolated worker model? _(B)_
3. Distributed OpenTelemetry traces span BriskCart's POS gateway, Service Bus processor Function, and ledger API, and daily telemetry volume must stay under 5 GB without breaking multi-hop `operation_Id` call graphs. Which sampling strategy fits best? _(C)_

### Case study — Cinder Coffee Roasters

Cinder Coffee Roasters hosts a B2B wholesale portal registered in a single-tenant Microsoft Entra ID directory. Wholesale buyers with the `WholesaleBuyer` app role upload PDF purchase orders directly from a React SPA to Azure Blob Storage without proxying 80 MB files through the web API, and uploaded PDFs must transition automatically to Cool storage after 30 days and delete after 365 days.

Questions in this block:

1. Cinder must restrict its wholesale purchase-order upload API inside its single-tenant Entra directory to users and automated EDI apps assigned `WholesaleBuyer`. How should authorization be modeled? _(C)_
2. Cinder's React SPA requests a temporary upload URL from the ASP.NET Core API so buyers can upload 80 MB PDF orders directly to Blob Storage without exposing storage account keys. Which sequence of steps mints the token securely? _(C)_
3. Uploaded PDF purchase orders in the `po-uploads/` prefix must move to `Cool` storage 30 days after modification and purge automatically after 365 days without scheduled Function scripts. What should Cinder configure? _(B)_

### Case study — Kova Footwear

Kova Footwear ingests warehouse RFID scans into Azure Container Apps and stores inventory state in Cosmos DB. Every stock depletion must notify downstream marketplace partners within three seconds through HTTPS webhooks that strip internal warehouse IDs, while preserving failed partner deliveries for 24 hours in Blob Storage. External partner apps call Kova APIs through Azure API Management Developer/Standard v2 using Microsoft Entra bearer tokens.

Questions in this block:

1. Kova must push sub-3-second stock-depletion notifications to partner HTTPS webhooks while dead-lettering undelivered partner payloads for 24 hours in Azure Blob Storage. Which Event Grid configuration satisfies both requirements? _(D)_
2. Partner responses flowing out of Kova's Azure API Management gateway must strip internal backend fingerprinting headers while retrying transient HTTP 503 responses from Container Apps up to three times. Where should the XML policies be placed? _(D)_
3. Kova wants APIM to reject external partner calls lacking a valid Microsoft Entra token with the `Inventory.Read` role before forwarding requests (`<inbound> ____ </inbound>`). Which policy snippet completes the gateway configuration? _(C)_

### Case study — Vespera Retail

Vespera Retail runs an ASP.NET Core storefront on Azure App Service (Standard S2, Linux) backed by Azure Cosmos DB for NoSQL partitioned by `/customerId` and Azure Blob Storage for receipts. Flash drops spike checkout requests 15x within two minutes. Zero-downtime deployments must keep the `Production` payment webhook URL strictly off `staging` slots, and developers are forbidden from storing connection strings in `appsettings.json` or GitHub repositories.

Questions in this block:

1. During blue-green releases between `staging` and `Production` on the Standard S2 Linux plan, how should Vespera ensure the live `PaymentWebhookUrl` value never leaks onto the `staging` slot or gets overwritten during slot swaps? _(C)_
2. Vespera's order-history endpoint queries a single shopper's orders inside `/customerId` and must stream 100-item pages while logging per-page RU consumption (` ____ `). Which C# Cosmos DB SDK v3 pattern should the developer implement? _(D)_
3. Vespera's ASP.NET Core checkout app needs to read Cosmos DB and storage secrets without storing credentials in `appsettings.json` or writing Key Vault SDK startup code. Which configuration meets this policy? _(A)_

## Exam 2: Healthcare Patient Portals, Clinical Lab Telemetry, and Claims EDI

### Case study — Aurelia Health

Aurelia Health operates a patient-scheduling Web App on Azure App Service Premium v3 and an isolated worker Azure Functions app on Flex Consumption. Clinicians sign in with Microsoft Entra ID and view team shift calendars pulled from Microsoft Graph. Audit compliance requires capturing HTTP 5xx server diagnostics to Blob Storage for 90 days and rotating all Key Vault secrets without restarting web workers.

Questions in this block:

1. Aurelia's FHIR HL7 normalization service runs inside a VNet-injected Azure Container Apps environment and must be reachable exclusively by internal patient-portal pods rather than the public internet. Which ingress setting enforces this boundary? _(C)_
2. HIPAA retention rules require diagnostic DICOM radiology images stored in Azure Blob Storage to resist modification or deletion for seven years, even by subscription administrators. Which Blob Storage feature satisfies this mandate? _(A)_
3. Aurelia's clinical portal issues 10-minute HTTPS download links for DICOM study archives while Shared Key access is disabled across all clinical storage accounts. Which SAS mechanism must the C# API use? _(A)_

### Case study — Solace Telemed

Solace Telemed fronts twelve internal clinical microservices with Azure API Management inside a virtual network. Partner clinics authenticate with mutual TLS client certificates plus subscription keys, GET lookups on `/formulary` should be cached for 300 seconds per `Accept-Language` header, and backend `X-AspNet-Version` headers must never leak to external callers.

Questions in this block:

1. When a clinician signs into Solace's React portal and calls the ASP.NET Core Visit API, the API must exchange the clinician's bearer token (` ____ `) to book a Microsoft Teams meeting on their calendar via Microsoft Graph. Which MSAL call performs this exchange? _(B)_
2. Solace stores telehealth video-codec feature flags and Key Vault secret references in Azure App Configuration and requires zero-restart updates gated by a sentinel key. Which ordered setup enables dynamic refresh? _(A)_
3. Solace wants Application Insights to verify TLS certificate validity and HTTP 200 readiness on `https://intake.solacetelemed.example` from five geographies and page engineers only if two or more regions fail simultaneously. Which setup meets this requirement? _(B)_

### Case study — Trellis Diagnostics

Trellis Diagnostics streams 40,000 analyzer telemetry frames per second from hospital labs into Azure Event Hubs (16 partitions). Two independent consumers — a live anomaly-scoring Container App and an archival compliance indexer — must read the full stream concurrently at their own offsets while raw Avro batches land automatically in Azure Data Lake Storage Gen2 every five minutes.

Questions in this block:

1. Trellis lab analyzers stream 25,000 blood-panel telemetry events per second into Azure Event Hubs, and a .NET 8 worker must consume partitions with durable Blob Storage offset checkpoints. Which sequence implements the consumer? _(B)_
2. Every newly inserted abnormal lab result in Trellis's Cosmos DB `specimens` container must invoke an isolated-worker C# Function (` ____ `) to notify on-call pathologists. Which trigger attribute wires this pipeline? _(D)_
3. Intermittent HTTP 500 errors hit Trellis's lab-accessioning endpoint, and engineers want a KQL query joining failed `AppRequests` with failed downstream `AppDependencies` on shared correlation IDs (` ____ `). Which query isolates the failing downstream call? _(B)_

### Case study — Vireo Specialty Pharmacy

Vireo Specialty Pharmacy stores prescription fulfillment documents in Azure Cosmos DB for NoSQL using hierarchical partition keys (`/clinicId`, `/patientId`). Pharmacists must always read their own in-session writes immediately, while two downstream microservices — cold-chain label printing and insurer EDI notification — must react independently to every newly created or updated prescription item.

Questions in this block:

1. Prescription adjudication steps for a given `rxNumber` must execute in strict first-in-first-out sequence across scaled C# workers without interleaving different steps for the same prescription. Which sequence configures Azure Service Bus properly? _(D)_
2. Vireo encrypts Controlled Substance DEA audit exports locally with a per-file symmetric AES key (`dekBytes`) and wraps that key using an HSM-protected RSA key in Azure Key Vault (` ____ `). Which SDK client and method perform this operation? _(A)_
3. External PBM clearinghouses call Vireo's formulary API through Azure API Management and must be capped at 60 burst calls per minute (HTTP `429`) and 5,000 calls per month (HTTP `403`) without losing parent `<inbound>` policies. How should the policy XML be authored? _(B)_

## Exam 3: FinTech Instant Payments, Ledger Reconciliation, and Fraud Webhooks

### Case study — Bramble Insure

Bramble Insure processes roadside-claim photo uploads on Azure Functions triggered by Event Grid BlobCreated events rather than polling Blob Storage, cutting idle storage-transaction bills. Every claim workflow correlates front-end SPA telemetry, APIM gateway requests, Function executions, and SQL/Cosmos dependencies inside a single Application Insights transaction view.

Questions in this block:

1. Roadside-claim photos land in Blob Storage unevenly throughout the week, and Bramble wants near-instant `[BlobTrigger]` activation without paying continuous container-log polling charges (`[BlobTrigger(..., ____ )]`). Which trigger option achieves this? _(A)_
2. Claims adjusters report slow claim submissions spanning the SPA, APIM gateway, Azure Function, and Cosmos DB, and engineers need one correlation key in KQL to stitch every hop together. Which field links these tables? _(D)_
3. Bramble is onboarding a new subrogation .NET 8 microservice to Workspace-based Application Insights using OpenTelemetry and automated failure alerting. Which rollout sequence is correct? _(D)_

### Case study — Crestline Clearing

Crestline Clearing runs containerized settlement workers in Azure Container Apps connected to an Azure Service Bus Premium namespace and an Azure Container Registry with admin user disabled. Settlement batches arrive on a Service Bus queue; KEDA must scale worker replicas from 0 to 30 based on active queue depth using a user-assigned managed identity, with zero credentials stored in YAML manifests.

Questions in this block:

1. Crestline's settlement worker Container App must pull images from an Azure Container Registry that has admin user disabled, with zero passwords in Bicep/YAML manifests. Which ordered steps configure passwordless deployment? _(B)_
2. Crestline wants settlement worker replicas to scale down to `0` overnight when the Service Bus queue is empty and scale out up to `30` replicas on active backlog without connection-string secrets. How should the KEDA rule be authored? _(B)_
3. Crestline attaches separate user-assigned identities for ACR image pulls and Service Bus consumption, and `new DefaultAzureCredential()` in C# fails to disambiguate them (` ____ `). Which option fixes token acquisition? _(B)_

### Case study — Halcyon Custody

Halcyon Custody stores immutable trade confirmations in Azure Blob Storage with versioning and legal hold policies enabled, and stores account ledger entries in Cosmos DB within single-partition batches. When a custodian updates multiple ledger lines for the same `/accountNumber`, either every write must commit atomically or the entire batch must roll back without partial state.

Questions in this block:

1. SEC Rule 17a-4 auditors require Halcyon's trade-confirmation PDFs in Blob Storage to enforce non-erasable WORM protection and suspend expiration whenever a regulatory investigation opens. Which Blob Storage controls meet both rules? _(C)_
2. Updating a custody settlement posts a debit entry, a fee entry, and a balance summary sharing `/accountNumber` in Cosmos DB (`container. ____ `), and partial writes are unacceptable. Which SDK feature guarantees atomic execution? _(B)_
3. Whenever an amended trade confirmation overwrites an existing blob key, Halcyon must retain every prior state automatically under an immutable `VersionId` without extra client SDK calls. What must be enabled on the storage account? _(A)_

### Case study — Pillar Remit

Pillar Remit exposes a cross-border FX quote API via Azure API Management. Free-tier fintech sandboxes must be capped at 60 calls per minute per subscription (returning HTTP 429) and 5,000 calls per month (returning HTTP 403), while enterprise corridors call an App Configuration store using dynamic sentinel-key refresh and feature flags gated by rollout percentage.

Questions in this block:

1. Free-tier FX sandbox callers on Azure API Management must receive HTTP `429` above 60 calls/minute and HTTP `403` above 5,000 calls/month per subscription while retaining parent `<inbound>` policies. Which XML policy block satisfies this? _(A)_
2. Enterprise remittance corridors read FX spread settings and Key Vault secret references from Azure App Configuration with dynamic sentinel-key refresh. Which sequence configures this architecture end to end? _(D)_
3. Pillar rolls out a new instant-SEPA corridor to 20% of requests via `.appconfig.featureflag/*` and updates three fee-tier keys simultaneously without mid-edit partial reloads. Which App Configuration setup accomplishes both? _(C)_

## Exam 4: Connected Fleet IoT, Cold-Chain Logistics, and Port Customs

### Case study — Aegis Rail

Aegis Rail hosts internal track-inspection web apps secured with App Service built-in authentication (Microsoft Entra provider) returning HTTP 401 rather than interactive redirects for unauthenticated API clients. Inspection microservices authenticate to Azure Key Vault and Azure Queue Storage via `DefaultAzureCredential` during both local Visual Studio debugging and deployed Azure hosting.

Questions in this block:

1. Track-inspection tablet APIs hosted on App Service use built-in Microsoft Entra Authentication (`Easy Auth`) and must return HTTP `401` rather than HTML `302` login redirects when tokens are missing or expired. Which Easy Auth setting enforces this? _(D)_
2. Rail-sensor microservices connect to Key Vault and Queue Storage without connection strings during both local Visual Studio debugging and deployed Azure hosting. Which `Azure.Identity` credential class meets this requirement? _(C)_
3. Aegis stores wayside database secrets, locomotive RSA signing keys, and mTLS certificates in Azure Key Vault and requires mandatory 90-day protection against permanent key purge even by rogue admins. Which two Key Vault practices apply? Select two. _(A, C)_

### Case study — Mariner PortOps

Mariner PortOps runs customs-manifest APIs on Azure App Service Linux containers deployed from a geo-replicated Azure Container Registry. Customs brokers upload XML manifests to Blob Storage where a single active processing worker must acquire a 60-second exclusive lock on each manifest blob before updating status metadata so concurrent workers never double-file customs declarations.

Questions in this block:

1. Mariner deploys Linux customs-manifest containers across port regions in Rotterdam, Singapore, and Los Angeles and needs local regional image layer pulls from a single registry FQDN. Which ACR configuration is required? _(A)_
2. When customs brokers upload XML manifests to Blob Storage, Mariner must ensure only one worker pod locks each manifest blob for 60 seconds before updating status metadata so duplicate customs filings never occur. Which SDK call enforces this? _(A)_
3. Mariner's Linux App Service customs API pulls container images from ACR, and port security policy forbids shared ACR admin credentials. How should image pulls be authenticated? _(C)_

### Case study — Strider ColdChain

Strider ColdChain monitors 25,000 refrigerated trailers emitting reefer temperatures every ten seconds into Azure Event Hubs. A .NET 8 `EventProcessorClient` hosted on Azure Container Apps checkpoints progress in Azure Blob Storage, while excursion events (`tempC > 4.0`) publish to an Azure Event Grid custom topic subscribed to by regional dispatchers filtered by subject prefix `/region/eu-west/`.

Questions in this block:

1. Strider's .NET 8 worker on Container Apps consumes 25,000 reefer telemetry readings every ten seconds from Event Hubs (` ____ `) and must persist partition progress in Blob Storage so scaling events never replay hours of readings. Which pattern implements this? _(C)_
2. Temperature excursions (`tempC > 4.0`) publish to an Event Grid custom topic and must push only `/region/eu-west/` alerts to Rotterdam dispatchers while dead-lettering undelivered alerts to Blob Storage. Which Event Grid subscription configuration works? _(B)_
3. Strider wants to test a new anomaly-threshold build of its HTTP telemetry-query API on Azure Container Apps by sending 10% of live dispatcher requests to the new revision. How must the Container App be configured? _(D)_

### Case study — Zephyr Parcel

Zephyr Parcel coordinates hub sorting across Service Bus topics. Hazardous-material parcels (`hazmat = true`) must route to a dedicated compliance subscription that stamps `Priority = High` onto brokered message properties, while unprocessable poison messages exceeding five delivery attempts move automatically to the subscription dead-letter queue for ops inspection.

Questions in this block:

1. Hub-sorting events published to a Service Bus topic must route `hazmat = true` parcels to a compliance subscription that stamps `Priority = High` onto brokered properties, while isolating messages exceeding 5 failed deliveries. Which Service Bus setup accomplishes this? _(C)_
2. Zephyr's compliance consumer must keep hazmat messages locked on the broker during processing, return transient faults for immediate retry, and explicitly quarantine malformed XML schemas into the dead-letter sub-queue (` ____ `). Which `ServiceBusProcessor` pattern works? _(A)_
3. Label-printer edge workers read parcel barcode jobs from Azure Queue Storage and need to extend visibility leases when paper jams slow printing (`UpdateMessageAsync`) before deleting finished jobs. Which parameters must the C# worker pass? _(A)_

## Exam 5: Multi-Tenant B2B SaaS, DevTools Telemetry, and Document Workflows

### Case study — Cobalt FieldService

Cobalt FieldService dispatches technician work orders using Azure Functions (isolated worker model) with timer triggers running every 15 minutes during weekday business hours and Queue Storage output bindings. Field mobile apps download encrypted schematic blobs using short-lived HTTPS-only SAS tokens signed by Microsoft Entra credentials rather than storage account shared keys.

Questions in this block:

1. Cobalt's isolated-worker dispatch Function (`[TimerTrigger(" ____ ")]`) must trigger every 15 minutes during weekday business hours (`09:00–17:45`, Mon–Fri). Which six-field NCRONTAB expression configures this schedule? _(A)_
2. Cobalt's HTTP work-order endpoint runs on .NET 8 isolated worker and must enqueue a Queue Storage / Service Bus dispatch payload while returning an HTTP 202 JSON acknowledgement without `out` parameters. Which C# return pattern works? _(D)_
3. Field technician mobile apps request 15-minute HTTPS-only download links for encrypted schematic blobs signed with Microsoft Entra credentials rather than storage account keys. Which ordered steps mint the token? _(C)_

### Case study — Loomis Cloud ERP

Loomis Cloud ERP exposes versioned `/v1/invoices` and `/v2/invoices` endpoints in Azure API Management while testing non-breaking OpenAPI edits safely before making them current. When a downstream tax service intermittently returns HTTP 503, APIM must retry up to three times before falling back cleanly, and availability alerts must notify on-call teams if synthetic multi-region probes fail from two+ locations.

Questions in this block:

1. Loomis maintains breaking `/v1/invoices` and `/v2/invoices` contracts simultaneously for ERP customers while staging non-breaking OpenAPI description edits safely before making them current. Which APIM features handle each requirement? _(C)_
2. When Loomis's downstream tax calculator intermittently returns HTTP `503`, APIM must retry forwarding up to three times while scrubbing internal stack headers on outbound responses. Where do those XML policies belong? _(B)_
3. Loomis wants synthetic multi-region HTTPS probes validating SSL expiry and HTTP 200 status on `/v2/invoices/health`, paging on-call engineers only when at least two regions fail concurrently. What should be configured? _(A)_

### Case study — Pulsar Metrics

Pulsar Metrics runs bursting nightly customer-usage rollups as containerized jobs without maintaining always-on HTTP ingress, pulling container images built in the cloud via ACR Tasks whenever commits land on `main`. Rollup results land in Cosmos DB where multi-field `ORDER BY tenantId ASC, recordedAt DESC` queries must execute with minimal RU consumption.

Questions in this block:

1. Pulsar executes bursting nightly customer-usage rollups across containerized worker shards that must finish and terminate without keeping an HTTP listener open. Which Azure Container Apps resource fits this pattern? _(D)_
2. Whenever engineers merge commits to `main`, Pulsar wants Azure Container Registry to compile the Dockerfile and push tagged rollup images in the cloud without running Docker daemons on CI agents (` ____ `). Which capability accomplishes this? _(B)_
3. Pulsar's billing dashboard runs `SELECT c.tenantId, c.units FROM c ORDER BY c.tenantId ASC, c.recordedAt DESC` in Cosmos DB for NoSQL and needs minimal RU charges without sorting errors. What must be configured in the indexing policy? _(C)_

### Case study — QuillSign SaaS

QuillSign SaaS is a multi-tenant contract-signing platform registered in Microsoft Entra ID to accept work accounts from any customer Entra tenant (`AzureADMultipleOrgs`). Backend APIs validate tenant scopes and call Microsoft Graph on behalf of the signed-in user to read organizational manager chains without requesting excessive directory-wide admin privileges.

Questions in this block:

1. QuillSign's e-signature platform must accept sign-ins from any customer work or school Microsoft Entra directory while blocking personal consumer accounts and validating subscribed `tid` tenant claims. How should the app registration and API validation be configured? _(B)_
2. When an enterprise user signs a contract in QuillSign's SPA, the middle-tier ASP.NET Core Routing API must query that user's organizational manager chain from Microsoft Graph using delegated permissions. Which ordered steps implement this token flow? _(A)_
3. Enterprise customer admins reject QuillSign's consent prompt if it asks for `Directory.ReadWrite.All`, and manager-chain lookups across large orgs must paginate cleanly. How should the Graph SDK client be coded? _(A)_

## Exam 6: Digital Media Streaming, Live Ticketing, Gaming Backends, and Smart Energy

### Case study — EmberPlay Studios

EmberPlay Studios runs seasonal multiplayer leaderboards on Azure App Service with `Staging` and `Production` slots, routing 10% of live player traffic to `Staging` for canary validation before swapping. Player replay archives in Blob Storage move from Hot to Cold after 14 days and Archive after 90 days, with priority rehydration required when dispute moderators request archived replays.

Questions in this block:

1. EmberPlay validates seasonal leaderboard builds on App Service `Staging` (with 10% canary routing) before swapping into `Production`, keeping live matchmaking keys pinned strictly to `Production`. Which sequence promotes releases cleanly? _(B)_
2. Match replay blobs under `replays/` must transition automatically from `Hot` to `Cold` after 14 days and to `Archive` after 90 days without custom cleanup workers. What should EmberPlay configure? _(A)_
3. Esports tournament moderators request a 6-month-old match replay currently stored in the offline `Archive` tier in Blob Storage. Which ordered steps restore and download the replay cleanly? _(C)_

### Case study — Lyric Arena Ticketing

Lyric Arena Ticketing handles stadium on-sale events on Azure Container Apps with HTTP scale rules and Cosmos DB for seat-hold documents that must expire and vanish automatically after 600 seconds if unpaid, without running background delete sweeps. Optimistic concurrency via ETags prevents two fans from claiming the same seat document simultaneously.

Questions in this block:

1. Ahead of a stadium tour on-sale, Lyric wants to route 5% of live HTTP seat-map requests on Azure Container Apps to a new revision while 95% remain on the current revision. How must the Container App be configured? _(A)_
2. Unpaid seat-hold documents in Cosmos DB specify `"ttl": 600` and must vanish automatically after 600 seconds without expiring permanent arena-map documents in the same container or running delete sweeps. How should the container be configured? _(A)_
3. Two fans attempt to claim seat `Sec104-RowB-12` in Cosmos DB within the same millisecond (`await container.ReplaceItemAsync(..., ____ )`). How must the C# API ensure one fan wins and the second immediately receives HTTP `412`? _(C)_

### Case study — NovaGrid Energy

NovaGrid Energy collects substation voltage alerts through Azure Event Grid domains serving 80 municipal utilities under tenant-scoped event topics. Critical transformer alerts forward to an Azure Service Bus queue consumed by an Azure Function, while Application Insights custom metrics and KQL log alerts watch for webhook delivery latency above 1,500 ms.

Questions in this block:

1. NovaGrid routes substation voltage alerts to 80 municipal utilities under tenant-scoped event topics behind one publish endpoint with per-utility Azure RBAC isolation. Which Event Grid resource fits? _(D)_
2. Critical transformer-overload alerts land on an Azure Service Bus queue consumed by a C# Function/worker that must never lose messages if a worker crashes mid-analysis and must dead-letter malformed payloads (` ____ `). Which receive pattern applies? _(A)_
3. NovaGrid monitors custom webhook delivery latency in Application Insights / Azure Monitor and must page grid dispatchers via webhook/SMS whenever p95 latency exceeds 1,500 ms. Which alerting construct implements this? _(D)_

### Case study — Prism Newsroom

Prism Newsroom ingests breaking wire feeds into Azure Functions, enriches metadata via Azure App Configuration feature flags and Key Vault-backed secrets, and publishes partner feeds through Azure API Management. A self-hosted APIM gateway deployed in Prism on-premises broadcast centers keeps local newsroom API traffic inside the facility while syncing configuration from Azure every ten seconds.

Questions in this block:

1. Prism's breaking-news Functions and APIs load feature flags and Key Vault secret references from Azure App Configuration with dynamic sentinel-key refresh. Which ordered steps configure this end to end? _(D)_
2. Prism's on-premises broadcast centers must route local newsroom API calls inside the studio LAN even if external links degrade, while syncing API policies from Azure every ten seconds. Which APIM deployment model works? _(A)_
3. Prism's Azure Function App reads wire-agency credentials from app settings and wants rotated Azure Key Vault secrets resolved automatically without writing `SecretClient` SDK code (` ____ `). Which configuration achieves this? _(D)_
