# Microsoft Exam AZ-204: Developing Solutions for Microsoft Azure — Full-Length Mock Exam 5

Exam AZ-204 (Multi-Tenant B2B SaaS, DevTools Telemetry, and Document Workflows) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Credential Lifecycle Notice:** Microsoft retired Exam AZ-204 (`Microsoft Certified: Azure Developer Associate`) on **July 31, 2026** and succeeded it with **Exam AI-200 (`Azure AI Cloud Developer Associate`)**. This practice bank preserves the final official January 14, 2026 AZ-204 skills-measured baseline for archival certification prep, enterprise Azure developer benchmarking, and core compute/storage/security/monitoring/integration mastery.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` SDK/CLI/XML/JSON/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area code dropdowns, split-pane tabbed case exhibits, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn documentation — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. A B2B PDF-rendering microservice written in .NET 8 is moving to containers; security requires excluding the .NET SDK compiler from production layers, running non-root, and stripping local `.git/` and `bin/` directories from build uploads. Which two steps accomplish this? Select two.

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Add `bin/`, `obj/`, `.git/`, and local `.env` files to `.dockerignore` before running `docker build` or `az acr build`
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Use a multi-stage Dockerfile building in `mcr.microsoft.com/dotnet/sdk:8.0` and copying published output into `mcr.microsoft.com/dotnet/aspnet:8.0` with a non-root `USER app`
- E. Keep the default `--restart-policy Always` on a run-once batch container group

### 2. A webhook-worker container ignores `SIGTERM` during rolling updates because shell-form `ENTRYPOINT "dotnet Worker.dll"` wraps execution under `/bin/sh -c` (` ____ `). Which Dockerfile syntax delivers OS stop signals directly to the .NET host?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Declare `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form so `SIGTERM` reaches the .NET host cleanly during container shutdown
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 3. Pull-request preview pipelines push 600 ephemeral container tags weekly into ACR, consuming 450 GB of stale layers. Which built-in ACR capability cleans manifests older than 30 days automatically without external CI runners?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Schedule an ACR Task executing `acr purge --filter "app:.*" --ago 30d --untagged` to clean stale untagged manifests and old tags automatically

### 4. Tenant data-export jobs run on Azure Container Instances for six minutes, exit with code `0`, and unexpectedly restart in an infinite billing loop. Which `--restart-policy` setting runs the export once on success while still retrying crashes?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Set `--restart-policy OnFailure` (or `Never`) on the Azure Container Instances container group so batch containers stop billing vCPU/memory seconds once exit code 0 completes

### 5. A customer-SSO SCIM provisioner running in ACI needs an OAuth bearer token passed at creation time without exposing the value inside Azure Portal properties or `az container show` JSON (` ____ `). Which ACI feature hides the value?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Pass sensitive tokens via `--secure-environment-variables` (or a secret volume mount) so values never appear in Azure Portal properties or `az container show` plaintext output

### 6. A SaaS workflow cluster on Azure Container Apps needs weighted canary HTTP splits across revisions, Managed Identity KEDA scale-to-zero on Service Bus queues, and Dapr pub/sub components restricted strictly to approved `daprAppId` services. Which three capabilities implement this? Select three.

Domain: Develop Azure compute solutions

- A. Configure a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0` and Managed Identity (`identity` property) so replicas scale to zero when idle and wake on queue depth
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- E. Set `--revision-mode multiple` and apply `az containerapp ingress traffic set --revision-weight` to split live HTTP requests across named revisions
- F. Register a Dapr state or pub/sub component in the Container Apps environment and restrict access via the component `scopes` array to specific `daprAppId` values

### 7. Proposed solution: Copy SMTP and webhook secrets as raw strings inside Container Apps Bicep parameters committed to a shared repo. Which Container Apps secret configuration eliminates plaintext secret parameters cleanly?

Domain: Develop Azure compute solutions

- A. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- B. Define a Container App secret using `keyVaultUrl` plus `identity` (managed identity resource ID or `system`) and map container environment variables via `secretRef`
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 8. A tenant-search indexer inside a VNet-integrated Container Apps environment should accept gRPC/HTTP calls solely from sibling SaaS microservices and never from public internet IPs (`ingress: { ____ }`). Which setting enforces private-only routing?

Domain: Develop Azure compute solutions

- A. Configure `ingress.external: false` inside a VNet-integrated Container Apps environment so the endpoint resolves only to internal environment/VNet callers
- B. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 9. A SaaS admin console hosted on a `Basic (B1)` Linux App Service plan needs blue-green deployment slots and CPU metric autoscale rules before onboarding enterprise customers. Which plan tier change is required?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Provision at least a `Standard` (`S1+`) or `Premium v3` (`P1v3+`) App Service plan to unlock deployment slots, custom domain SNI SSL, and metric/schedule autoscaling
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 10. After rebasing a SaaS billing API onto Microsoft's non-root `.NET 8` runtime image (` ____ `), health checks fail on port 80 because Kestrel binds an unprivileged port. Which Dockerfile configuration aligns the container listener?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Set `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` inside the final `.NET 8` runtime stage and match `targetPort: 8080` on Container Apps ingress
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 11. SOC 2 Type II auditors require 90-day retention of App Service application diagnostics across 8 scaled-out Linux/Windows web workers without 12-hour automatic shutoff. Where should diagnostics be written?

Domain: Develop Azure compute solutions

- A. Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 12. A SaaS developer debugging SAML assertion errors on a staging App Service web app wants live console log lines streamed into their local terminal (` ____ `). Which CLI command sequence works?

Domain: Develop Azure compute solutions

- A. Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 13. Deploying frequent hotfixes to a busy multi-tenant App Service portal causes transient 500 errors from half-copied DLLs in `wwwroot`. Which deployment approach switches releases atomically from a read-only archive?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Set `WEBSITE_RUN_FROM_PACKAGE=1` and deploy with `az webapp deploy --type zip` so the app mounts the read-only ZIP package directly with atomic cold-start replacement
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 14. Corporate security blocks developer laptops from pushing public base images into private ACR, requiring server-side ingestion of `nginx:1.27-alpine` directly into ACR (` ____ `). Which Azure CLI command performs this?

Domain: Develop Azure compute solutions

- A. Execute `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine`
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 15. Customer browser apps at `https://app.quillsign.example` send credentialed requests to `https://api.quillsign.example` on App Service, which must reject plaintext HTTP and legacy TLS 1.0/1.1 ciphers. Which two App Service settings satisfy both rules? Select two.

Domain: Develop Azure compute solutions

- A. Enable `httpsOnly: true`, set `minTlsVersion: "1.2"` (or `"1.3"`), and configure `clientCertEnabled` when mutual TLS client certificates are required
- B. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- C. Configure App Service `CORS` with explicit origin URLs (and `supportCredentials` only without wildcard `*`) so App Service handles preflight `OPTIONS` requests
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 16. A DevOps script configures a `SQLAzure` connection string named `LedgerDb` on App Service and pins it so slot swaps never carry staging DB strings into production (` ____ `). Which CLI command accomplishes this?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 17. Proposed solution: Set App Service autoscale to add 2 instances when CPU > 65% and remove 2 instances when CPU < 64% with a 1-minute cooldown. What operational issue results, and how is it prevented?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Pair every scale-out metric rule (e.g., CPU > 75% for 10 min) with a conservative scale-in rule (e.g., CPU < 35%) and an explicit `coolDown` window plus safe default/max instance bounds
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`

### 18. A tenant-metadata API preloads 50,000 schema definitions on boot; which App Service settings ensure `staging` workers return HTTP `200` on `/internal/warmup` before traffic shifts during a slot swap?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps
- C. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 19. A SaaS release manager is promoting build `v8.1` on App Service Standard S2 with zero downtime while keeping live Stripe billing webhook keys pinned strictly to `Production`. Which ordered sequence executes this safely?

Domain: Develop Azure compute solutions

- A. Deploy directly to production → create the staging slot → swap staging into production → mark settings as slot settings
- B. Create the staging slot on a Free F1 plan → deploy the build → swap slots → mark settings sticky
- C. Swap staging into production → create the staging slot → deploy the build → mark settings as deployment slot settings
- D. Create the staging deployment slot on the Standard/Premium Web App → mark production-only connection strings and webhook settings as deployment slot settings → deploy and warm up the new build in staging → swap staging into production and verify health

### 20. After swapping `staging` into `Production` on a CRM web app, customer emails start routing through the staging Mailtrap sandbox relay. Which flag must be enabled on the SMTP relay setting to keep each slot isolated?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Mark environment-specific settings such as `PaymentWebhookUrl` and production connection strings as `slotSetting: true` (Deployment slot setting) before swapping slots
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 21. A contract-OCR Function App requires outbound private-VNet connectivity to an internal SQL instance, zero cold-start latency for interactive uploads, and 15-minute batch PDF indexing runs. Which Functions plan fits?

Domain: Develop Azure compute solutions

- A. Host the Function App on `Flex Consumption` or `Elastic Premium (EP1+)` when VNet integration, longer execution timeouts beyond 10 minutes, or pre-warmed/always-ready instances are required
- B. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 22. A multi-tenant webhook Function App sets a 10-minute host timeout and prevents Application Insights sampling from discarding `Request` or `Exception` telemetry (`host.json`: ` ____ `). Which JSON snippet configures `host.json`?

Domain: Develop Azure compute solutions

- A. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- B. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Configure `"functionTimeout": "00:10:00"` and `"logging": { "applicationInsights": { "samplingSettings": { "isEnabled": true, "excludedTypes": "Request;Exception" } } }` inside `host.json`

### 23. A SaaS analytics Function App must react automatically to updated tenant-subscription documents in Cosmos DB and retry transient failures five times with exponential backoff on an Event Hub telemetry trigger. Which two attributes apply? Select two.

Domain: Develop Azure compute solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Apply `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` (or `[FixedDelayRetry]`) on the `[EventHubTrigger]` / `[TimerTrigger]` function
- C. Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- E. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`

### 24. Enterprise customers upload 70,000 signed contract PDFs per hour to Blob Storage, and default log-scanning `[BlobTrigger]` executions lag by several minutes. How should `[BlobTrigger]` be configured for instant push execution?

Domain: Develop Azure compute solutions

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- C. Configure `[BlobTrigger(..., Source = BlobTriggerSource.EventGrid)]` with an Event Grid system topic subscription instead of default container-log polling
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 25. Enterprise SaaS tenants on Cosmos DB for NoSQL grow past 20 GB per `/tenantId`, filter queries by `/tenantId` + `/siteId`, commit workspace + folder creates atomically in one partition key, and block concurrent lost edits via HTTP 412. Which three Cosmos DB designs solve all of these? Select three.

Domain: Develop for Azure storage

- A. Pass `new ItemRequestOptions { IfMatchEtag = item.ETag }` on `ReplaceItemAsync` and catch `CosmosException` when `StatusCode == HttpStatusCode.PreconditionFailed` (412)
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Define `new ContainerProperties(id: "telemetry", partitionKeyPaths: new List<string> { "/tenantId", "/siteId", "/deviceId" })` using `PartitionKeyBuilder` on reads and writes
- D. Use `container.CreateTransactionalBatch(new PartitionKey(pkValue))` to group multiple create/replace/upsert/delete operations atomically within the same logical partition
- E. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- F. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 26. Audit-log documents written to Cosmos DB contain 90 nested JSON properties yet are queried strictly by `/customerId` and `/createdUtc`, causing unnecessary write RU burn (` ____ `). Which indexing policy cuts write RU cost?

Domain: Develop for Azure storage

- A. Configure `"indexingMode": "consistent"` with `"includedPaths": [{"path": "/customerId/?"}, {"path": "/createdUtc/?"}]` and `"excludedPaths": [{"path": "/*"}]`
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 27. When a webhook delivery fails, a SaaS worker needs only to increment `/retryCount` by `1` and set `/lastStatus` to `"Queued"` on a 110 KB Cosmos DB webhook document (`await container. ____ `). Which SDK method avoids full-document replacement?

Domain: Develop for Azure storage

- A. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `await container.PatchItemAsync<Order>(id, new PartitionKey(pk), new[] { PatchOperation.Increment("/retryCount", 1), PatchOperation.Set("/lastStatus", "Queued") })`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 28. After a workspace admin renames a project in a SaaS SPA, immediate page reloads routed to any stateless API pod must display the new title for that admin at half the RU cost of `Strong` consistency. Which Cosmos DB setup achieves this?

Domain: Develop for Azure storage

- A. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- B. Use `Session` consistency (the default) and propagate `x-ms-session-token` (`RequestOptions.SessionToken`) across client/middle-tier hops to guarantee monotonic read-your-own-writes at half the read RU cost of `Strong`
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 29. Global SaaS read replicas in Sydney and Dublin must serve tenant audit logs in exact write order lagging the primary US write region by at most `T = 5` seconds or `K = 100` versions. Which consistency level provides this guarantee?

Domain: Develop for Azure storage

- A. Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 30. Proposed solution: Poll `SELECT * FROM c WHERE c._ts > @lastRun` every five seconds from a cron job to trigger SaaS search-index updates instead of subscribing to the Cosmos DB Change Feed. Which Change Feed trigger pattern eliminates polling RU waste?

Domain: Develop for Azure storage

- A. Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 31. Both an Elasticsearch indexer and a webhook notifier must consume every Cosmos DB contract change independently, and hard-deleted draft contracts must also trigger index removal. Which two Change Feed patterns apply? Select two.

Domain: Develop for Azure storage

- A. Use Change Feed `AllVersionsAndDeletes` mode (or soft-delete flag items with short TTL in `LatestVersion` mode) because default `LatestVersion` change feed omits hard-deleted items
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay
- E. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction

### 32. Magic-link login tokens stored in Cosmos DB carry `"ttl": 900` while tenant profile records in the same container have no `ttl`, yet tokens never expire because `DefaultTimeToLive` is `null`. What container setting activates per-item TTL?

Domain: Develop for Azure storage

- A. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Enable container `DefaultTimeToLive = -1` (or positive seconds) and set item `ttl = 600` so Cosmos DB purges expired items automatically using background RU capacity
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 33. A document-workflow SaaS stores 50 million signed PDFs across 80 containers and needs sub-second server-side queries for `@container = 'docs' AND status = 'pending'` (`await serviceClient. ____ `). Which Blob feature enables indexed cross-container search?

Domain: Develop for Azure storage

- A. Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`)
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Attach searchable key-value `Tags` (`SetTagsAsync` / `BlobUploadOptions.Tags`) and query across containers with `FindBlobsByTagsAsync("@container = 'docs' AND status = 'pending'")`

### 34. A contract-export service sets `Content-Disposition` / `Content-Type` HTTP system properties alongside custom `envelope_id` user metadata (`x-ms-meta-envelope_id`) on uploaded blobs (` ____ `). Which SDK v12 methods apply each correctly?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`)

### 35. SaaS customers edit template `.docx` blobs in place, and product managers want every `UploadAsync` overwrite to retain an automatic recoverable `VersionId` alongside optional explicit pre-migration checkpoints. What should be enabled?

Domain: Develop for Azure storage

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Call `await blobClient.CreateSnapshotAsync()` for explicit point-in-time read-only checkpoints or enable account-level Blob Versioning so every `UploadAsync` overwrite retains an immutable `VersionId`
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 36. Multiple SaaS billing workers coordinate updates to `tenant-invoice-seq.json` in Blob Storage and must lock the blob exclusively for 60 seconds so competing writers fail immediately with HTTP `412`. Which SDK mechanism enforces this?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` (15–60 seconds or `-1` infinite) and pass `LeaseId` inside `BlobRequestConditions` on subsequent writes/deletes
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 37. During tenant region migration, a tool copies 2 TB of contract attachments between Azure Storage accounts (`await destBlob. ____ `) without streaming gigabytes through the migration worker pod. Which SDK call executes server-to-server copy?

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Invoke `BlobClient.StartCopyFromUriAsync(sourceSasUri)` to trigger asynchronous server-side blob copy and inspect `CopyStatus` without streaming bytes through the client VM

### 38. An export endpoint constructs a 15-minute HTTPS-only read SAS scoped strictly to blob `exports/manifest.csv` (`new BlobSasBuilder { ____ }`). Which builder properties enforce single-blob read scope?

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 39. Executed legal contracts in Blob Storage must transition automatically to `Cool` at 30 days and `Archive` at 365 days while remaining WORM-protected against deletion during a 7-year statutory period. Which two features satisfy both rules? Select two.

Domain: Develop for Azure storage

- A. Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`)
- E. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 40. A legal-discovery paralegal requests a 2023 executed contract bundle stored in the offline `Archive` tier in Blob Storage. Which ordered steps restore and download the blob without HTTP `409 BlobArchived` failures?

Domain: Develop for Azure storage

- A. Set blob metadata `tier=Hot` → download the blob immediately → call SetAccessTier to Archive → poll ArchiveStatus
- B. Download the archived blob stream directly → call SetAccessTier to Hot → poll ArchiveStatus → verify the Archive tier
- C. Acquire an infinite blob lease → delete the blob snapshot → download the archived blob directly → call SetAccessTier
- D. Verify the blob is currently in the Archive access tier → call SetAccessTier (or CopyBlob) targeting Hot or Cool with Standard or High rehydrate priority → poll ArchiveStatus until rehydration completes and tier updates → download the blob content

### 41. Proposed solution: Call `DownloadContentAsync()` directly on an `Archive`-tier tenant backup under 6 GB when an urgent courtroom order requires restoration within one hour. Why does this throw HTTP `409`, and what fixes it?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob)
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 42. A developer CLI/desktop plugin authenticates SaaS users with Microsoft Entra ID without embedding client secrets and refreshes tokens silently from cache before falling back to interactive login. Which two MSAL patterns apply? Select two.

Domain: Implement Azure security

- A. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- B. Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 43. A background usage-metering daemon authenticates with an X.509 certificate and requests app-only Entra tokens for `api://metering/.default` (` ____ `). Which MSAL builder and method implement this?

Domain: Implement Azure security

- A. Use `ConfidentialClientApplicationBuilder` authenticated with a client certificate (or workload identity assertion) calling `AcquireTokenForClient(new[] { "api://.../.default" })` for headless background daemons
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps

### 44. A SaaS webhook-management endpoint (`[Authorize(Roles = "TenantAdmin")]`) must authorize both human tenant administrators and automated Terraform provisioning service principals. How must `TenantAdmin` be declared in Entra ID?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Declare `appRoles` with `allowedMemberTypes: ["User", "Application"]` in the Entra app registration manifest and validate the `roles` claim (`[Authorize(Roles = "...")]`) in the web API
- C. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 45. CLI automation scripts calling an App Service REST API protected by Easy Auth break because unauthenticated calls return `302 Redirect` to an interactive HTML login screen. Which Easy Auth setting fixes CLI callers?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)

### 46. Enterprise tenants receive a Service SAS for container `bulk-imports`, and SaaS security requires revoking a compromised tenant SAS within seconds without rotating storage account keys. How should the SAS be structured?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Bind a Service SAS to a container/queue/table Stored Access Policy (`SignedIdentifier`, omitting inline start/expiry/permissions) so compromised tokens can be revoked instantly by modifying or deleting the policy
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 47. Security hardens all SaaS storage accounts with `allowSharedKeyAccess: false`; how can the export microservice continue minting 15-minute Blob download SAS links?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Mint a short-lived HTTPS-only (`SasProtocol.HttpsOnly`) User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` instead of Account or Service SAS signed with storage account keys
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 48. An org-chart builder in a B2B SaaS app fetches active Entra users projecting strictly `id`, `displayName`, and `mail`, and combines 18 group-lookup requests into one HTTP round-trip while respecting `429 Retry-After`. Which two Graph SDK patterns apply? Select two.

Domain: Implement Azure security

- A. Call `await graphClient.Users.GetAsync(rc => { rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }; rc.QueryParameters.Filter = "accountEnabled eq true"; })`
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- E. Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses

### 49. Inside a middle-tier document-sharing API controller holding `incomingBearerToken`, which MSAL C# call exchanges that token for a delegated OneDrive/SharePoint Graph token (` ____ `)?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Call `await confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` inside the middle-tier API

### 50. QuillSign's API fleet centralizes tenant feature flags and Key Vault secret references in Azure App Configuration with dynamic sentinel-key refresh. Which ordered sequence sets up this pipeline end to end?

Domain: Implement Azure security

- A. Copy plaintext Key Vault secret values into appsettings.json → commit to Git → wire ConfigureRefresh → enable Managed Identity
- B. Add Key Vault references → wire ConfigureRefresh without UseAzureAppConfiguration middleware → expect background timer push updates → grant RBAC later
- C. Enable Managed Identity with App Configuration Data Reader + Key Vault Secrets User → add Key Vault references and a sentinel key → wire AddAzureAppConfiguration with ConfigureKeyVault and ConfigureRefresh → invoke UseAzureAppConfiguration middleware
- D. Grant only App Configuration Data Reader (no Key Vault role) → invoke UseAzureAppConfiguration → add sentinel key → register AddAzureAppConfiguration

### 51. Proposed solution: Add Key Vault references in Azure App Configuration and call `options.Connect(endpoint, cred)` in C# without calling `ConfigureKeyVault`, expecting App Configuration to decrypt secrets server-side. Why does startup fail, and what fixes it?

Domain: Implement Azure security

- A. Wire `options.Connect(new Uri(endpoint), cred).ConfigureKeyVault(kv => kv.SetCredential(cred))` so App Configuration resolves Key Vault reference items using the app identity
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 52. QuillSign's document-signing vault stores database passwords, FIPS HSM RSA signing keys, and X.509 signing certificates in Azure Key Vault and requires mandatory 90-day protection against permanent key purge. Which two Key Vault practices apply? Select two.

Domain: Implement Azure security

- A. Use `SecretClient` (`Azure.Security.KeyVault.Secrets`) for connection strings/tokens, `KeyClient` / `CryptographyClient` (`Azure.Security.KeyVault.Keys`) for RSA/EC wrap-unwrap-sign, and `CertificateClient` for X.509 lifecycle
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable Soft Delete (mandatory on new vaults, 7–90 days) plus Purge Protection on Azure Key Vault so neither accidental deletion nor malicious principals can permanently destroy keys before retention expires
- E. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 53. Each customer PDF vault encrypts files locally with a unique 256-bit AES data key (`dekBytes`) wrapped by the tenant's RSA key in Azure Key Vault (` ____ `). Which SDK client and method perform key wrapping?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Instantiate `new CryptographyClient(keyVaultKey.Id, new DefaultAzureCredential())` and invoke `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync(...)`

### 54. A SaaS admin web app on Azure App Service reads `Environment.GetEnvironmentVariable("SendGridApiKey")` and wants rotated Key Vault secrets injected without SDK startup code (` ____ `). Which app-setting value accomplishes this?

Domain: Implement Azure security

- A. Configure App Service / Functions application settings using `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` (omitting secret version) paired with `Key Vault Secrets User` on the app Managed Identity
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 55. SaaS engineers debug an indexing worker locally signed into Azure CLI and deploy the identical container image to Azure Container Apps with Managed Identity. Which `Azure.Identity` credential class authenticates in both places without code changes?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Instantiate `new DefaultAzureCredential()` (or explicit `ManagedIdentityCredential(clientId)` for user-assigned identities in production) so identical code authenticates via Azure CLI / Visual Studio locally and Managed Identity in Azure
- D. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps

### 56. A multi-tenant worker Container App mounts two User-Assigned Managed Identities (`uami-acr` and `uami-kv`), causing bare `new DefaultAzureCredential()` calls to fail (` ____ `). How must the C# code target `uami-kv`?

Domain: Implement Azure security

- A. Instantiate `new DefaultAzureCredential(new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId })` (or set `AZURE_CLIENT_ID`)
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 57. SaaS customers report intermittent HTTP 500 failures on `POST /envelopes/sign`, and engineers need W3C distributed correlation plus a KQL inner join isolating which downstream dependency failed for each 500 request. Which two Application Insights practices apply? Select two.

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Query Workspace-based Application Insights (`AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces` or classic `requests`/`dependencies`/`exceptions`) joining on `OperationId` (`operation_Id`) to reconstruct end-to-end distributed transactions
- B. Run `AppRequests | where ResultCode == "500" | join kind=inner (AppDependencies | where Success == false) on OperationId | project TimeGenerated, Name, Target, DependencyType, ResultCode1`
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 58. Tenant reliability leads want a Log Analytics query against `AppRequests` calculating unsuccessful call totals alongside tail p95 execution milliseconds grouped into five-minute intervals per route (` ____ `). Which KQL statement computes this report?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Run `AppRequests | where TimeGenerated > ago(1h) | summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 59. Nightly Pulsar Container Apps Jobs run for 10 seconds, emit custom usage metrics, and terminate `Main()` immediately, losing buffered telemetry in memory. Which C# shutdown call prevents data loss?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits

### 60. Inside a .NET 8 PDF-stamper service using `UseAzureMonitor()`, developers want custom timed spans around `ApplyDigitalSignature` (`using var span = ____ `) exported to Application Insights Transaction Search. How should this be coded?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 61. B2B SaaS request volume peaks Tuesday–Thursday afternoons and falls 85% on weekends, causing static error thresholds to misfire; alerts must trigger a Slack/PagerDuty webhook receiver. Which alert design fits?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Create an Azure Monitor Metric Alert (Dynamic Thresholds or static p95 latency/5xx count) or Scheduled Query (KQL) Alert targeting an Action Group configured with webhook / Azure Function / email-SMS receivers
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 62. An internal ERP tax-calculation service runs inside a private VNet with zero public endpoints, yet SREs need synthetic availability percentages tracked inside Application Insights Availability. How should probes run?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group

### 63. Pulsar Metrics is wiring OpenTelemetry into a greenfield ASP.NET Core 8 ingestion service (`builder.Services.AddOpenTelemetry(). ____ `) pointed at `APPLICATIONINSIGHTS_CONNECTION_STRING`. Which extension method activates the official Azure Monitor distro?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 64. QuillSign's engineering org is standardizing telemetry across twelve .NET 8 services: they want official OpenTelemetry distro startup wiring plus trace volume reduction that keeps multi-hop call trees whole without blinding real-time Live Metrics. Which two capabilities should they combine? Select two.

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently
- E. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 65. Independent per-pod adaptive sampling across four SaaS microservices causes Transaction Search traces to show broken parent spans missing downstream dependency spans. Which sampling mode keeps whole `operation_Id` traces intact?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 66. Enterprise defence customers run air-buffered on-premises Kubernetes clusters where local Loomis ERP APIs must route locally inside the plant while syncing APIM gateway policies outbound over HTTPS from Azure. Which APIM setup supports this?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Select `Developer` (non-SLA) or `Premium` / `Standard v2` for VNet integration, and deploy the containerized APIM Self-Hosted Gateway (`mcr.microsoft.com/azure-api-management/gateway`) for hybrid on-premises/multi-cloud local traffic routing
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 67. QuillSign's APIM gateway routes requests to an internal Entra-protected document-vault API and must inject Managed Identity bearer tokens without static secrets (`<inbound> ____ </inbound>`). Which XML policy snippet completes `<inbound>`?

Domain: Connect to and consume Azure services and third-party services

- A. Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 68. Partner CRM frontend developers need mocked HTTP 200 `/templates` JSON from APIM before backend code ships, and later `/templates/{id}` must rewrite to `/internal/v2/orders/{orderId}` (` ____ `). Which APIM policies support both stages?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use `<mock-response status-code="200" content-type="application/json" />` during frontend parallel development, or `<rewrite-uri template="/internal/v2/orders/{orderId}" />` with `<set-backend-service base-url="..." />` in `<inbound>`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 69. When importing an HTTP-triggered Azure Function App into APIM, APIM stores a host key in Named Values and forwards `x-functions-key` because the trigger rejects anonymous requests (`[HttpTrigger( ____ )]`). Which `AuthorizationLevel` is set?

Domain: Connect to and consume Azure services and third-party services

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 70. Loomis Cloud ERP is replacing static backend API keys in APIM Named Values with Managed Identity authentication against its Entra-protected billing microservice. Which ordered steps complete the migration?

Domain: Connect to and consume Azure services and third-party services

- A. Grant RBAC to the developer laptop user → add `<validate-jwt>` in `<outbound>` → enable APIM Managed Identity → test backend
- B. Add authentication-managed-identity policy → test backend invocation → enable Managed Identity on APIM → grant RBAC on the target
- C. Enable Managed Identity on the APIM instance → grant that identity RBAC or app-role access on the target backend/Key Vault → add authentication-managed-identity in APIM policy XML → test backend calls and inspect APIM trace headers
- D. Hardcode a 2-year client secret inside `<set-header>` XML → disable Managed Identity → grant RBAC → inspect trace

### 71. Enterprise SaaS webhook management APIs on APIM must require Product Subscription Keys, verify partner mTLS client certificate thumbprints, and validate Entra JWT signatures and roles at the gateway edge. Which two APIM configurations enforce all three? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- E. Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers

### 72. An APIM contract-approval operation must reject callers with HTTP `401` whenever their bearer token lacks audience `api://orders` or the required write role (`<inbound> ____ </inbound>`). Which XML policy enforces pre-authentication?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps

### 73. QuillSign's public template-catalog gateway on APIM must enforce per-tenant burst limits plus monthly plan caps without losing parent policies, cache localized template JSON per language header, and retry backend 5xx blips while removing internal server headers. Which three APIM policy setups deliver these controls? Select three.

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`
- C. Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`
- F. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 74. Proposed solution: Configure `<quota-by-key calls="60" renewal-period="60" />` expecting HTTP `429` burst responses and delete `<base />` inside operation `<inbound>` XML. Why does this misbehave in two ways, and what fixes it?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 75. French and German SaaS users calling `GET /templates/localized` receive cached English responses from APIM because `<cache-lookup>` ignored the `Accept-Language` request header (` ____ `). Which caching policy pair fixes this?

Domain: Connect to and consume Azure services and third-party services

- A. Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 76. Loomis Cloud ERP needs to publish `PurchaseOrderApproved` events for 8,500 independent customer organizations under one Azure Event Grid ingestion endpoint while restricting each organization via Azure RBAC to its own topic. Which Event Grid architecture fits?

Domain: Connect to and consume Azure services and third-party services

- A. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization

### 77. QuillSign delivers `EnvelopeSigned` events to 6,000 enterprise SaaS customer tenants — isolating each tenant's topic via Azure RBAC behind one publish endpoint — using `CloudEvents v1.0` subject filters and 24-hour Blob dead-lettering. Which two Event Grid features fit? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization
- B. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 78. A tenant's custom ASP.NET Core webhook endpoint fails Event Grid subscription creation because it returns `204 No Content` on validation events (` ____ `). How must the endpoint respond?

Domain: Connect to and consume Azure services and third-party services

- A. Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`
- B. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 79. An enterprise ERP subscriber wants only `InvoiceOverdue` events under `/tenant/acme/` where `totalUsd >= 10000`, with undelivered payloads saved to Blob Storage if the ERP undergoes weekend maintenance. Which Event Grid settings achieve this?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- D. Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL

### 80. Pulsar Metrics ingests 75,000 SDK telemetry events/sec into Azure Event Hubs, and a .NET 8 rollup worker must consume partitions with durable Blob Storage checkpoints. Which ordered sequence implements the consumer?

Domain: Connect to and consume Azure services and third-party services

- A. Point all five independent microservices at `$Default` with one shared Blob prefix → call StopProcessingAsync → call StartProcessingAsync → skip UpdateCheckpointAsync
- B. Instantiate EventHubProducerClient → call UpdateCheckpointAsync on the producer → register ProcessEventAsync → call StopProcessingAsync first
- C. Call StartProcessingAsync → register ProcessEventAsync without ProcessErrorAsync → create the Event Hub → create the Blob container
- D. Create the Event Hub, consumer group, and Blob checkpoint container → instantiate BlobContainerClient and EventProcessorClient → register ProcessEventAsync (calling UpdateCheckpointAsync) and ProcessErrorAsync → call StartProcessingAsync before StopProcessingAsync

### 81. Three SaaS teams (anomaly detection, usage billing, and audit replay) read a 70,000-event/sec clickstream simultaneously while raw events archive automatically as Parquet in ADLS Gen2 with zero custom code. Which Event Hubs architecture works?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- C. Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 82. Rolling deployments of Pulsar's `EventProcessorClient` pods re-aggregate the previous hour's usage counts because partition progress is never saved (`await eventArgs. ____ `). Which call must follow idempotent batch writes?

Domain: Connect to and consume Azure services and third-party services

- A. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- B. Host `EventProcessorClient` backed by `BlobContainerClient` and call `await eventArgs.UpdateCheckpointAsync()` after idempotent batch persistence so partition leases resume cleanly after rebalancing
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 83. Multi-step contract-approval workflow commands for a single `envelopeId` must execute strictly in FIFO sequence across 15 worker replicas on Azure Service Bus. Which ordered setup enforces per-envelope FIFO?

Domain: Connect to and consume Azure services and third-party services

- A. Send messages to Queue Storage with SessionId → attach ServiceBusSessionProcessor → toggle FIFO → complete locks
- B. Create ServiceBusSessionProcessor → send messages with null SessionId → create the queue → complete messages before receiving
- C. Create the queue or subscription with RequiresSession = true at creation time → send ServiceBusMessage instances setting a non-empty SessionId → create a ServiceBusSessionProcessor (or AcceptNextSessionAsync receiver) → process messages in order and complete/renew session locks
- D. Create a standard queue with RequiresSession = false → send messages without SessionId → toggle RequiresSession = true later → read with standard ServiceBusReceiver

### 84. Tenant lifecycle events on Azure Service Bus must fan out by `PlanTier = 'Enterprise'` via fast header matching, survive mid-handler pod crashes without losing messages, and isolate poison payloads in `$DeadLetterQueue`. Which two Service Bus practices apply? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- D. Use Azure Service Bus Topics with `SqlRuleFilter` / `CorrelationRuleFilter` (`CorrelationRuleFilter` preferred for high throughput) and `SqlRuleAction` header stamping, inspecting `$DeadLetterQueue` (`SubQueue.DeadLetter`) after `MaxDeliveryCount` expires
- E. Use `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false`, calling `CompleteMessageAsync` after commit, `AbandonMessageAsync` for transient retries, and `DeadLetterMessageAsync` on unrecoverable schema errors

### 85. Webhook retries from partner CRMs occasionally post identical `MessageId` commands twice within three minutes, and per-tenant FIFO order plus automatic duplicate suppression are required on Service Bus. Which entity settings solve both?

Domain: Connect to and consume Azure services and third-party services

- A. Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 86. When a trial user starts onboarding, the API schedules a nudge message 30 minutes later on Service Bus (`long seq = await sender. ____ `) and cancels it if the user finishes setup early. Which SDK method pair handles this?

Domain: Connect to and consume Azure services and third-party services

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `long seq = await sender.ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` and persist `seq` to call `CancelScheduledMessageAsync(seq)` if the user cancels early
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 87. A SaaS document-thumbnail service queues 300 TB of 6 KB PDF page-render jobs needing simple visibility timeouts and low cost without FIFO sessions or topic routing. Why is Azure Queue Storage required instead of Service Bus?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics

### 88. A C# Queue Storage worker leasing PDF render jobs must quarantine corrupted jobs after 5 failed attempts and extend visibility leases on slow 400-page PDFs before deleting finished jobs (` ____ `). Which SDK workflow works?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`

---

## Case study — Cobalt FieldService

Cobalt FieldService dispatches technician work orders using Azure Functions (isolated worker model) with timer triggers running every 15 minutes during weekday business hours and Queue Storage output bindings. Field mobile apps download encrypted schematic blobs using short-lived HTTPS-only SAS tokens signed by Microsoft Entra credentials rather than storage account shared keys.

The next 3 questions refer to **Cobalt FieldService**. Read the scenario brief once, then answer each item independently.

### 89. Cobalt's isolated-worker dispatch Function (`[TimerTrigger(" ____ ")]`) must trigger every 15 minutes during weekday business hours (`09:00–17:45`, Mon–Fri). Which six-field NCRONTAB expression configures this schedule?

Domain: Develop Azure compute solutions

- A. Specify a six-field NCRONTAB expression `{second} {minute} {hour} {day} {month} {day-of-week}` such as `"0 */15 9-17 * * 1-5"` on `[TimerTrigger]`
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 90. Cobalt's HTTP work-order endpoint runs on .NET 8 isolated worker and must enqueue a Queue Storage / Service Bus dispatch payload while returning an HTTP 202 JSON acknowledgement without `out` parameters. Which C# return pattern works?

Domain: Develop Azure compute solutions

- A. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- B. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. In the .NET isolated worker model, return a custom POCO class uniting `[HttpResult]` (or `HttpResponseData`) with `[CosmosDBOutput]` / `[ServiceBusOutput]` properties

### 91. Field technician mobile apps request 15-minute HTTPS-only download links for encrypted schematic blobs signed with Microsoft Entra credentials rather than storage account keys. Which ordered steps mint the token?

Domain: Implement Azure security

- A. Build BlobSasBuilder and sign → call GetUserDelegationKeyAsync → instantiate BlobServiceClient with shared account key → assign RBAC to the identity
- B. Instantiate BlobServiceClient with SAS token → assign RBAC → build BlobSasBuilder → call GetUserDelegationKeyAsync
- C. Assign Storage Blob Data Contributor/Delegator RBAC to the identity → instantiate BlobServiceClient with DefaultAzureCredential → call GetUserDelegationKeyAsync for a bounded validity window → build BlobSasBuilder and sign with the user delegation key
- D. Call GetUserDelegationKeyAsync anonymously → build BlobSasBuilder → assign RBAC to the identity → instantiate BlobServiceClient

---

## Case study — Loomis Cloud ERP

Loomis Cloud ERP exposes versioned `/v1/invoices` and `/v2/invoices` endpoints in Azure API Management while testing non-breaking OpenAPI edits safely before making them current. When a downstream tax service intermittently returns HTTP 503, APIM must retry up to three times before falling back cleanly, and availability alerts must notify on-call teams if synthetic multi-region probes fail from two+ locations.

The next 3 questions refer to **Loomis Cloud ERP**. Read the scenario brief once, then answer each item independently.

### 92. Loomis maintains breaking `/v1/invoices` and `/v2/invoices` contracts simultaneously for ERP customers while staging non-breaking OpenAPI description edits safely before making them current. Which APIM features handle each requirement?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Use APIM `Revisions` to stage, test, and swap non-breaking internal changes safely on the same consumer URL (`;rev=2`), and use APIM `Versions` (path/header/query) when publishing breaking contract changes side-by-side for distinct consumer cohorts
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 93. When Loomis's downstream tax calculator intermittently returns HTTP `503`, APIM must retry forwarding up to three times while scrubbing internal stack headers on outbound responses. Where do those XML policies belong?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 94. Loomis wants synthetic multi-region HTTPS probes validating SSL expiry and HTTP 200 status on `/v2/invoices/health`, paging on-call engineers only when at least two regions fail concurrently. What should be configured?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

---

## Case study — Pulsar Metrics

Pulsar Metrics runs bursting nightly customer-usage rollups as containerized jobs without maintaining always-on HTTP ingress, pulling container images built in the cloud via ACR Tasks whenever commits land on `main`. Rollup results land in Cosmos DB where multi-field `ORDER BY tenantId ASC, recordedAt DESC` queries must execute with minimal RU consumption.

The next 3 questions refer to **Pulsar Metrics**. Read the scenario brief once, then answer each item independently.

### 95. Pulsar executes bursting nightly customer-usage rollups across containerized worker shards that must finish and terminate without keeping an HTTP listener open. Which Azure Container Apps resource fits this pattern?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- D. Deploy an Azure Container Apps Job (`triggerType: Event` or `Schedule`) with `replicaCompletionCount` and `parallelism` instead of an always-listening HTTP container app

### 96. Whenever engineers merge commits to `main`, Pulsar wants Azure Container Registry to compile the Dockerfile and push tagged rollup images in the cloud without running Docker daemons on CI agents (` ____ `). Which capability accomplishes this?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Run `az acr build --registry <acrName> --image app:{{.Run.ID}} .` to build and push the container image remotely using ACR Tasks without a local Docker daemon
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 97. Pulsar's billing dashboard runs `SELECT c.tenantId, c.units FROM c ORDER BY c.tenantId ASC, c.recordedAt DESC` in Cosmos DB for NoSQL and needs minimal RU charges without sorting errors. What must be configured in the indexing policy?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Configure `"indexingMode": "consistent"` with `"includedPaths": [{"path": "/customerId/?"}, {"path": "/createdUtc/?"}]` and `"excludedPaths": [{"path": "/*"}]`
- C. Add a `compositeIndexes` array matching the exact property sequence and sort directions (`ascending` / `descending`) in the container indexing policy JSON
- D. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction

---

## Case study — QuillSign SaaS

QuillSign SaaS is a multi-tenant contract-signing platform registered in Microsoft Entra ID to accept work accounts from any customer Entra tenant (`AzureADMultipleOrgs`). Backend APIs validate tenant scopes and call Microsoft Graph on behalf of the signed-in user to read organizational manager chains without requesting excessive directory-wide admin privileges.

The next 3 questions refer to **QuillSign SaaS**. Read the scenario brief once, then answer each item independently.

### 98. QuillSign's e-signature platform must accept sign-ins from any customer work or school Microsoft Entra directory while blocking personal consumer accounts and validating subscribed `tid` tenant claims. How should the app registration and API validation be configured?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)

### 99. When an enterprise user signs a contract in QuillSign's SPA, the middle-tier ASP.NET Core Routing API must query that user's organizational manager chain from Microsoft Graph using delegated permissions. Which ordered steps implement this token flow?

Domain: Implement Azure security

- A. Register the middle-tier API scope and delegated Graph permissions in Entra ID → validate the incoming user token → call ConfidentialClientApplication.AcquireTokenOnBehalfOf(UserAssertion) → invoke Microsoft Graph with the exchanged token
- B. Call Microsoft Graph anonymously → call AcquireTokenOnBehalfOf → validate the incoming token → expose the API scope
- C. Forward the front-end SPA access token directly to Microsoft Graph → validate the incoming token → register the API scope → call AcquireTokenOnBehalfOf
- D. Use PublicClientApplication without client credentials → call AcquireTokenForClient → pass UserAssertion → register delegated permissions

### 100. Enterprise customer admins reject QuillSign's consent prompt if it asks for `Directory.ReadWrite.All`, and manager-chain lookups across large orgs must paginate cleanly. How should the Graph SDK client be coded?

Domain: Implement Azure security

- A. Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

---

## Answer key and explanations

### Question 1 — B, D

Answers: Use a multi-stage Dockerfile building in `mcr.microsoft.com/dotnet/sdk:8.0` and copying published output into `mcr.microsoft.com/dotnet/aspnet:8.0` with a non-root `USER app`; Add `bin/`, `obj/`, `.git/`, and local `.env` files to `.dockerignore` before running `docker build` or `az acr build`. Using a multi-stage Dockerfile (`sdk:8.0` -> `aspnet:8.0` with non-root `USER`) trims build tooling, while `.dockerignore` blocks local build folders and `.env` files from the context. Local study-map skill 1.1 (Create and Manage Container Images and Multi-Stage Dockerfiles), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Using a multi-stage Dockerfile (`sdk:8.0` -> `aspnet:8.0` with non-root `USER`) trims build tooling, while `.dockerignore` blocks local build folders and `.env` files from the context.
- **B:** Correct. `.dockerignore` prevents streaming gigabytes of local build artifacts and stray secrets into the build context. In this scenario: Using a multi-stage Dockerfile (`sdk:8.0` -> `aspnet:8.0` with non-root `USER`) trims build tooling, while `.dockerignore` blocks local build folders and `.env` files from the context.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Using a multi-stage Dockerfile (`sdk:8.0` -> `aspnet:8.0` with non-root `USER`) trims build tooling, while `.dockerignore` blocks local build folders and `.env` files from the context.
- **D:** Correct. Multi-stage Docker builds exclude compiler SDK layers and source files from the final runtime image, shrinking image size and attack surface. In this scenario: Using a multi-stage Dockerfile (`sdk:8.0` -> `aspnet:8.0` with non-root `USER`) trims build tooling, while `.dockerignore` blocks local build folders and `.env` files from the context.
- **E:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Using a multi-stage Dockerfile (`sdk:8.0` -> `aspnet:8.0` with non-root `USER`) trims build tooling, while `.dockerignore` blocks local build folders and `.env` files from the context.

### Question 2 — C

Answer: Declare `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form so `SIGTERM` reaches the .NET host cleanly during container shutdown. Exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` (JSON array syntax) launches the .NET runtime as PID 1 so graceful cancellation tokens trigger on `SIGTERM`. Exec-form `ENTRYPOINT` runs the process as PID 1 without an intermediate `/bin/sh -c` wrapper that swallows POSIX termination signals. Local study-map skill 1.1 (Create and Manage Container Images and Multi-Stage Dockerfiles), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` (JSON array syntax) launches the .NET runtime as PID 1 so graceful cancellation tokens trigger on `SIGTERM`.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` (JSON array syntax) launches the .NET runtime as PID 1 so graceful cancellation tokens trigger on `SIGTERM`.
- **C:** Correct. Exec-form `ENTRYPOINT` runs the process as PID 1 without an intermediate `/bin/sh -c` wrapper that swallows POSIX termination signals. In this scenario: Exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` (JSON array syntax) launches the .NET runtime as PID 1 so graceful cancellation tokens trigger on `SIGTERM`.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` (JSON array syntax) launches the .NET runtime as PID 1 so graceful cancellation tokens trigger on `SIGTERM`.

### Question 3 — D

Answer: Schedule an ACR Task executing `acr purge --filter "app:.*" --ago 30d --untagged` to clean stale untagged manifests and old tags automatically. Scheduling an ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` reclaims registry quota on a recurring schedule. Scheduled `acr purge` tasks reclaim registry storage quota without manual tag deletion scripts. Local study-map skill 1.2 (Publish Images, Run ACR Tasks, and Manage Auth/Purge in Azure Container Registry), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Scheduling an ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` reclaims registry quota on a recurring schedule.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Scheduling an ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` reclaims registry quota on a recurring schedule.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Scheduling an ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` reclaims registry quota on a recurring schedule.
- **D:** Correct. Scheduled `acr purge` tasks reclaim registry storage quota without manual tag deletion scripts. In this scenario: Scheduling an ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` reclaims registry quota on a recurring schedule.

### Question 4 — D

Answer: Set `--restart-policy OnFailure` (or `Never`) on the Azure Container Instances container group so batch containers stop billing vCPU/memory seconds once exit code 0 completes. Setting `--restart-policy OnFailure` halts the container group after exit code `0` while restarting non-zero crash exits automatically. ACI bills per second while containers run; `OnFailure` retries crashes (`exit != 0`) and halts cleanly on `exit == 0`, whereas `Always` loops forever. Local study-map skill 1.3 (Run Container Groups, Sidecars, Volumes, and Restart Policies in Azure Container Instances), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting `--restart-policy OnFailure` halts the container group after exit code `0` while restarting non-zero crash exits automatically.
- **B:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Setting `--restart-policy OnFailure` halts the container group after exit code `0` while restarting non-zero crash exits automatically.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `--restart-policy OnFailure` halts the container group after exit code `0` while restarting non-zero crash exits automatically.
- **D:** Correct. ACI bills per second while containers run; `OnFailure` retries crashes (`exit != 0`) and halts cleanly on `exit == 0`, whereas `Always` loops forever. In this scenario: Setting `--restart-policy OnFailure` halts the container group after exit code `0` while restarting non-zero crash exits automatically.

### Question 5 — D

Answer: Pass sensitive tokens via `--secure-environment-variables` (or a secret volume mount) so values never appear in Azure Portal properties or `az container show` plaintext output. Using `--secure-environment-variables` (or mounting a secret volume) prevents ARM/CLI read calls from echoing secret values in cleartext. Secure environment variables and secret volumes redact secret values from ARM/CLI read responses. Local study-map skill 1.3 (Run Container Groups, Sidecars, Volumes, and Restart Policies in Azure Container Instances), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Using `--secure-environment-variables` (or mounting a secret volume) prevents ARM/CLI read calls from echoing secret values in cleartext.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Using `--secure-environment-variables` (or mounting a secret volume) prevents ARM/CLI read calls from echoing secret values in cleartext.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Using `--secure-environment-variables` (or mounting a secret volume) prevents ARM/CLI read calls from echoing secret values in cleartext.
- **D:** Correct. Secure environment variables and secret volumes redact secret values from ARM/CLI read responses. In this scenario: Using `--secure-environment-variables` (or mounting a secret volume) prevents ARM/CLI read calls from echoing secret values in cleartext.

### Question 6 — A, E, F

Answers: Set `--revision-mode multiple` and apply `az containerapp ingress traffic set --revision-weight` to split live HTTP requests across named revisions; Configure a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0` and Managed Identity (`identity` property) so replicas scale to zero when idle and wake on queue depth; Register a Dapr state or pub/sub component in the Container Apps environment and restrict access via the component `scopes` array to specific `daprAppId` values. Multiple-revision weighted ingress handles canary traffic, KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, and Dapr component `scopes` isolate microservice access. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Container Apps uses KEDA scalers to scale down to zero on consumption/workload profiles and authenticate scalers cleanly via Managed Identity. In this scenario: Multiple-revision weighted ingress handles canary traffic, KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, and Dapr component `scopes` isolate microservice access.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Multiple-revision weighted ingress handles canary traffic, KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, and Dapr component `scopes` isolate microservice access.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Multiple-revision weighted ingress handles canary traffic, KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, and Dapr component `scopes` isolate microservice access.
- **D:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Multiple-revision weighted ingress handles canary traffic, KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, and Dapr component `scopes` isolate microservice access.
- **E:** Correct. Multiple-revision mode keeps more than one revision active simultaneously for weighted blue/green or canary traffic splitting. In this scenario: Multiple-revision weighted ingress handles canary traffic, KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, and Dapr component `scopes` isolate microservice access.
- **F:** Correct. Dapr `scopes` confine which microservices inside a shared Container Apps environment can load or invoke a component. In this scenario: Multiple-revision weighted ingress handles canary traffic, KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, and Dapr component `scopes` isolate microservice access.

### Question 7 — B

Answer: Define a Container App secret using `keyVaultUrl` plus `identity` (managed identity resource ID or `system`) and map container environment variables via `secretRef`. Declaring Container App secrets with `keyVaultUrl` plus Managed Identity (`identity`) and binding container env vars via `secretRef` resolves secrets directly from Key Vault. Key Vault secret references in Container Apps resolve secrets via Managed Identity without storing secret strings in ARM templates. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Declaring Container App secrets with `keyVaultUrl` plus Managed Identity (`identity`) and binding container env vars via `secretRef` resolves secrets directly from Key Vault.
- **B:** Correct. Key Vault secret references in Container Apps resolve secrets via Managed Identity without storing secret strings in ARM templates. In this scenario: Declaring Container App secrets with `keyVaultUrl` plus Managed Identity (`identity`) and binding container env vars via `secretRef` resolves secrets directly from Key Vault.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Declaring Container App secrets with `keyVaultUrl` plus Managed Identity (`identity`) and binding container env vars via `secretRef` resolves secrets directly from Key Vault.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Declaring Container App secrets with `keyVaultUrl` plus Managed Identity (`identity`) and binding container env vars via `secretRef` resolves secrets directly from Key Vault.

### Question 8 — A

Answer: Configure `ingress.external: false` inside a VNet-integrated Container Apps environment so the endpoint resolves only to internal environment/VNet callers. Setting `ingress.external: false` scopes Envoy ingress visibility strictly to internal environment and VNet callers. Setting `external: false` restricts the Container Appsenvoy ingress controller to private internal traffic. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Setting `external: false` restricts the Container Appsenvoy ingress controller to private internal traffic. In this scenario: Setting `ingress.external: false` scopes Envoy ingress visibility strictly to internal environment and VNet callers.
- **B:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Setting `ingress.external: false` scopes Envoy ingress visibility strictly to internal environment and VNet callers.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `ingress.external: false` scopes Envoy ingress visibility strictly to internal environment and VNet callers.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting `ingress.external: false` scopes Envoy ingress visibility strictly to internal environment and VNet callers.

### Question 9 — B

Answer: Provision at least a `Standard` (`S1+`) or `Premium v3` (`P1v3+`) App Service plan to unlock deployment slots, custom domain SNI SSL, and metric/schedule autoscaling. Upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks deployment slots and rule-based horizontal autoscale omitted on `Free`/`Shared`/`Basic` plans. `Free`, `Shared`, and `Basic` plans omit deployment slots (`S1` gives 5, `P1v3` gives 20) and rule-based autoscale (`S1+` required). Local study-map skill 1.5 (Create Azure App Service Plans and Web Apps Across Linux and Windows Runtimes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks deployment slots and rule-based horizontal autoscale omitted on `Free`/`Shared`/`Basic` plans.
- **B:** Correct. `Free`, `Shared`, and `Basic` plans omit deployment slots (`S1` gives 5, `P1v3` gives 20) and rule-based autoscale (`S1+` required). In this scenario: Upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks deployment slots and rule-based horizontal autoscale omitted on `Free`/`Shared`/`Basic` plans.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks deployment slots and rule-based horizontal autoscale omitted on `Free`/`Shared`/`Basic` plans.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks deployment slots and rule-based horizontal autoscale omitted on `Free`/`Shared`/`Basic` plans.

### Question 10 — B

Answer: Set `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` inside the final `.NET 8` runtime stage and match `targetPort: 8080` on Container Apps ingress. Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` matches .NET 8's non-root port `8080` convention alongside `targetPort: 8080` / `WEBSITES_PORT=8080`. Starting in .NET 8, official Microsoft container images default to non-root port `8080` rather than privileged port `80`. Local study-map skill 1.5 (Create Azure App Service Plans and Web Apps Across Linux and Windows Runtimes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` matches .NET 8's non-root port `8080` convention alongside `targetPort: 8080` / `WEBSITES_PORT=8080`.
- **B:** Correct. Starting in .NET 8, official Microsoft container images default to non-root port `8080` rather than privileged port `80`. In this scenario: Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` matches .NET 8's non-root port `8080` convention alongside `targetPort: 8080` / `WEBSITES_PORT=8080`.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` matches .NET 8's non-root port `8080` convention alongside `targetPort: 8080` / `WEBSITES_PORT=8080`.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` matches .NET 8's non-root port `8080` convention alongside `targetPort: 8080` / `WEBSITES_PORT=8080`.

### Question 11 — A

Answer: Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances. Directing Application Logging (Blob) and Web Server Logging to Azure Blob Storage retains multi-instance diagnostic logs durably per retention policy. Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy. Local study-map skill 1.6 (Configure App Service Diagnostics, Application/Web Server Logging, and Log Streaming), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy. In this scenario: Directing Application Logging (Blob) and Web Server Logging to Azure Blob Storage retains multi-instance diagnostic logs durably per retention policy.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Directing Application Logging (Blob) and Web Server Logging to Azure Blob Storage retains multi-instance diagnostic logs durably per retention policy.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Directing Application Logging (Blob) and Web Server Logging to Azure Blob Storage retains multi-instance diagnostic logs durably per retention policy.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Directing Application Logging (Blob) and Web Server Logging to Azure Blob Storage retains multi-instance diagnostic logs durably per retention policy.

### Question 12 — A

Answer: Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`. Running `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>` attaches to Kudu's live log stream. `az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting. Local study-map skill 1.6 (Configure App Service Diagnostics, Application/Web Server Logging, and Log Streaming), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. `az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting. In this scenario: Running `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>` attaches to Kudu's live log stream.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Running `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>` attaches to Kudu's live log stream.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Running `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>` attaches to Kudu's live log stream.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Running `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>` attaches to Kudu's live log stream.

### Question 13 — C

Answer: Set `WEBSITE_RUN_FROM_PACKAGE=1` and deploy with `az webapp deploy --type zip` so the app mounts the read-only ZIP package directly with atomic cold-start replacement. Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying with `az webapp deploy --type zip` mounts the ZIP package directly without file-by-file `wwwroot` overwrites. Running directly from a mounted ZIP eliminates file-lock copy conflicts during `wwwroot` sync and speeds cold starts. Local study-map skill 1.7 (Deploy Code, Run-From-Package ZIPs, and Custom Containers to App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying with `az webapp deploy --type zip` mounts the ZIP package directly without file-by-file `wwwroot` overwrites.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying with `az webapp deploy --type zip` mounts the ZIP package directly without file-by-file `wwwroot` overwrites.
- **C:** Correct. Running directly from a mounted ZIP eliminates file-lock copy conflicts during `wwwroot` sync and speeds cold starts. In this scenario: Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying with `az webapp deploy --type zip` mounts the ZIP package directly without file-by-file `wwwroot` overwrites.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying with `az webapp deploy --type zip` mounts the ZIP package directly without file-by-file `wwwroot` overwrites.

### Question 14 — A

Answer: Execute `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine`. `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine` copies images server-side without local Docker pulls. `az acr import` copies public or cross-registry container images server-side into ACR without requiring `docker pull` / `docker push` on a local workstation. Local study-map skill 1.7 (Deploy Code, Run-From-Package ZIPs, and Custom Containers to App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. `az acr import` copies public or cross-registry container images server-side into ACR without requiring `docker pull` / `docker push` on a local workstation. In this scenario: `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine` copies images server-side without local Docker pulls.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine` copies images server-side without local Docker pulls.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine` copies images server-side without local Docker pulls.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine` copies images server-side without local Docker pulls.

### Question 15 — A, C

Answers: Enable `httpsOnly: true`, set `minTlsVersion: "1.2"` (or `"1.3"`), and configure `clientCertEnabled` when mutual TLS client certificates are required; Configure App Service `CORS` with explicit origin URLs (and `supportCredentials` only without wildcard `*`) so App Service handles preflight `OPTIONS` requests. Enabling `httpsOnly: true` with `minTlsVersion: "1.2"` secures transport, and listing `https://app.quillsign.example` explicitly in App Service `CORS` (without `*`) permits credentialed browser calls. Local study-map skill 1.8 (Configure TLS, Mutual TLS, CORS, App Settings, and Service Connections on App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Enforcing HTTPS redirection and minimum TLS 1.2/1.3 at the App Service front end rejects plaintext HTTP and legacy ciphers before app code runs. In this scenario: Enabling `httpsOnly: true` with `minTlsVersion: "1.2"` secures transport, and listing `https://app.quillsign.example` explicitly in App Service `CORS` (without `*`) permits credentialed browser calls.
- **B:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Enabling `httpsOnly: true` with `minTlsVersion: "1.2"` secures transport, and listing `https://app.quillsign.example` explicitly in App Service `CORS` (without `*`) permits credentialed browser calls.
- **C:** Correct. Platform-level App Service CORS intercepts `OPTIONS` preflight checks; credentialed CORS forbids wildcard `*` origins. In this scenario: Enabling `httpsOnly: true` with `minTlsVersion: "1.2"` secures transport, and listing `https://app.quillsign.example` explicitly in App Service `CORS` (without `*`) permits credentialed browser calls.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Enabling `httpsOnly: true` with `minTlsVersion: "1.2"` secures transport, and listing `https://app.quillsign.example` explicitly in App Service `CORS` (without `*`) permits credentialed browser calls.
- **E:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling `httpsOnly: true` with `minTlsVersion: "1.2"` secures transport, and listing `https://app.quillsign.example` explicitly in App Service `CORS` (without `*`) permits credentialed browser calls.

### Question 16 — C

Answer: Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`. `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` sets and slot-pins `SQLCONNSTR_LedgerDb`. `--slot-settings` pins the connection string (`SQLCONNSTR_LedgerDb`) to the target slot so slot swaps never leak staging databases into production. Local study-map skill 1.8 (Configure TLS, Mutual TLS, CORS, App Settings, and Service Connections on App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` sets and slot-pins `SQLCONNSTR_LedgerDb`.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` sets and slot-pins `SQLCONNSTR_LedgerDb`.
- **C:** Correct. `--slot-settings` pins the connection string (`SQLCONNSTR_LedgerDb`) to the target slot so slot swaps never leak staging databases into production. In this scenario: `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` sets and slot-pins `SQLCONNSTR_LedgerDb`.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` sets and slot-pins `SQLCONNSTR_LedgerDb`.

### Question 17 — B

Answer: Pair every scale-out metric rule (e.g., CPU > 75% for 10 min) with a conservative scale-in rule (e.g., CPU < 35%) and an explicit `coolDown` window plus safe default/max instance bounds. Near-identical thresholds cause rapid scale-out/scale-in thrashing; pairing >75% scale-out with <35% scale-in and a multi-minute `coolDown` stabilizes scaling. Asymmetric thresholds and cool-down periods prevent rapid flapping (thrashing) where instances repeatedly add and terminate. Local study-map skill 1.9 (Implement Metric-Based and Schedule-Based App Service Autoscaling Rules and Cooldowns), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Near-identical thresholds cause rapid scale-out/scale-in thrashing; pairing >75% scale-out with <35% scale-in and a multi-minute `coolDown` stabilizes scaling.
- **B:** Correct. Asymmetric thresholds and cool-down periods prevent rapid flapping (thrashing) where instances repeatedly add and terminate. In this scenario: Near-identical thresholds cause rapid scale-out/scale-in thrashing; pairing >75% scale-out with <35% scale-in and a multi-minute `coolDown` stabilizes scaling.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Near-identical thresholds cause rapid scale-out/scale-in thrashing; pairing >75% scale-out with <35% scale-in and a multi-minute `coolDown` stabilizes scaling.
- **D:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Near-identical thresholds cause rapid scale-out/scale-in thrashing; pairing >75% scale-out with <35% scale-in and a multi-minute `coolDown` stabilizes scaling.

### Question 18 — B

Answer: Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps. Configuring `applicationInitialization` plus `WEBSITE_SWAP_WARMUP_PING_PATH=/internal/warmup` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` gates swap completion on worker readiness. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. Local study-map skill 1.9 (Implement Metric-Based and Schedule-Based App Service Autoscaling Rules and Cooldowns), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Configuring `applicationInitialization` plus `WEBSITE_SWAP_WARMUP_PING_PATH=/internal/warmup` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` gates swap completion on worker readiness.
- **B:** Correct. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. In this scenario: Configuring `applicationInitialization` plus `WEBSITE_SWAP_WARMUP_PING_PATH=/internal/warmup` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` gates swap completion on worker readiness.
- **C:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Configuring `applicationInitialization` plus `WEBSITE_SWAP_WARMUP_PING_PATH=/internal/warmup` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` gates swap completion on worker readiness.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Configuring `applicationInitialization` plus `WEBSITE_SWAP_WARMUP_PING_PATH=/internal/warmup` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` gates swap completion on worker readiness.

### Question 19 — D

Answer: Create the staging deployment slot on the Standard/Premium Web App → mark production-only connection strings and webhook settings as deployment slot settings → deploy and warm up the new build in staging → swap staging into production and verify health. Provisioning the `staging` slot, pinning billing keys as slot-sticky settings first, deploying and warming `v8.1` on `staging`, and swapping into `Production` prevents downtime and secret drift. Slot-sticky settings must be pinned before swapping so staging never inherits live payment webhooks or overwrites production secrets during swap. Local study-map skill 1.10 (Configure App Service Deployment Slots, Slot-Sticky Settings, Warm-Up, and Traffic Routing), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Deploying directly to production bypasses zero-downtime validation and swapping an empty staging slot overwrites production. Why the keyed choice wins: Provisioning the `staging` slot, pinning billing keys as slot-sticky settings first, deploying and warming `v8.1` on `staging`, and swapping into `Production` prevents downtime and secret drift.
- **B:** Incorrect for this requirement. Free and Basic App Service plans do not support deployment slots; Standard, Premium, or Isolated is required first. Why the keyed choice wins: Provisioning the `staging` slot, pinning billing keys as slot-sticky settings first, deploying and warming `v8.1` on `staging`, and swapping into `Production` prevents downtime and secret drift.
- **C:** Incorrect for this requirement. You cannot swap a slot before creating and deploying to it, and marking settings sticky after the swap leaks staging values into production. Why the keyed choice wins: Provisioning the `staging` slot, pinning billing keys as slot-sticky settings first, deploying and warming `v8.1` on `staging`, and swapping into `Production` prevents downtime and secret drift.
- **D:** Correct. Slot-sticky settings must be pinned before swapping so staging never inherits live payment webhooks or overwrites production secrets during swap. In this scenario: Provisioning the `staging` slot, pinning billing keys as slot-sticky settings first, deploying and warming `v8.1` on `staging`, and swapping into `Production` prevents downtime and secret drift.

### Question 20 — B

Answer: Mark environment-specific settings such as `PaymentWebhookUrl` and production connection strings as `slotSetting: true` (Deployment slot setting) before swapping slots. Enabling `slotSetting: true` (Deployment slot setting) pins each slot's SMTP relay setting permanently to its own slot across swaps. Slot-sticky settings stay pinned to their slot (`Production` vs `Staging`) across swaps instead of traveling with the swapped code. Local study-map skill 1.10 (Configure App Service Deployment Slots, Slot-Sticky Settings, Warm-Up, and Traffic Routing), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling `slotSetting: true` (Deployment slot setting) pins each slot's SMTP relay setting permanently to its own slot across swaps.
- **B:** Correct. Slot-sticky settings stay pinned to their slot (`Production` vs `Staging`) across swaps instead of traveling with the swapped code. In this scenario: Enabling `slotSetting: true` (Deployment slot setting) pins each slot's SMTP relay setting permanently to its own slot across swaps.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Enabling `slotSetting: true` (Deployment slot setting) pins each slot's SMTP relay setting permanently to its own slot across swaps.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Enabling `slotSetting: true` (Deployment slot setting) pins each slot's SMTP relay setting permanently to its own slot across swaps.

### Question 21 — A

Answer: Host the Function App on `Flex Consumption` or `Elastic Premium (EP1+)` when VNet integration, longer execution timeouts beyond 10 minutes, or pre-warmed/always-ready instances are required. Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runs) satisfies VNet, warm-worker, and runtime needs. Classic Consumption caps timeout at 10 minutes (`functionTimeout`) and cold-starts from zero; `Flex Consumption` and `Premium` add VNet outbound and pre-warmed readiness. Local study-map skill 1.11 (Create and Configure Azure Functions Apps, Hosting Plans, and host.json Settings), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Classic Consumption caps timeout at 10 minutes (`functionTimeout`) and cold-starts from zero; `Flex Consumption` and `Premium` add VNet outbound and pre-warmed readiness. In this scenario: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runs) satisfies VNet, warm-worker, and runtime needs.
- **B:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runs) satisfies VNet, warm-worker, and runtime needs.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runs) satisfies VNet, warm-worker, and runtime needs.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runs) satisfies VNet, warm-worker, and runtime needs.

### Question 22 — D

Answer: Configure `"functionTimeout": "00:10:00"` and `"logging": { "applicationInsights": { "samplingSettings": { "isEnabled": true, "excludedTypes": "Request;Exception" } } }` inside `host.json`. Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` governs every function in the app. `host.json` governs global Function host behaviors such as execution timeout and Application Insights telemetry sampling exclusions across all functions in the app. Local study-map skill 1.11 (Create and Configure Azure Functions Apps, Hosting Plans, and host.json Settings), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` governs every function in the app.
- **B:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` governs every function in the app.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` governs every function in the app.
- **D:** Correct. `host.json` governs global Function host behaviors such as execution timeout and Application Insights telemetry sampling exclusions across all functions in the app. In this scenario: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` governs every function in the app.

### Question 23 — B, C

Answers: Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`; Apply `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` (or `[FixedDelayRetry]`) on the `[EventHubTrigger]` / `[TimerTrigger]` function. `[CosmosDBTrigger]` backed by a `leases` container streams document updates via Change Feed, while `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries transient Event Hub faults. Local study-map skill 1.12 (Implement Azure Functions Input and Output Bindings (Isolated Worker & Declarative Bindings)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `[CosmosDBTrigger]` backed by a `leases` container streams document updates via Change Feed, while `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries transient Event Hub faults.
- **B:** Correct. Function-level retry attributes replay failed executions in-memory before advancing trigger checkpoints on Event Hubs and Timer triggers. In this scenario: `[CosmosDBTrigger]` backed by a `leases` container streams document updates via Change Feed, while `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries transient Event Hub faults.
- **C:** Correct. `CosmosDBTrigger` wraps the Change Feed Processor library and requires a lease container connection to coordinate partition checkpoints across scaled workers. In this scenario: `[CosmosDBTrigger]` backed by a `leases` container streams document updates via Change Feed, while `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries transient Event Hub faults.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `[CosmosDBTrigger]` backed by a `leases` container streams document updates via Change Feed, while `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries transient Event Hub faults.
- **E:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: `[CosmosDBTrigger]` backed by a `leases` container streams document updates via Change Feed, while `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries transient Event Hub faults.

### Question 24 — C

Answer: Configure `[BlobTrigger(..., Source = BlobTriggerSource.EventGrid)]` with an Event Grid system topic subscription instead of default container-log polling. Setting `Source = BlobTriggerSource.EventGrid` paired with an Event Grid `BlobCreated` subscription triggers Functions immediately without container-log polling delays. Event Grid-sourced blob triggers eliminate storage-log scan latency and work reliably on Blob-only / high-scale storage accounts. Local study-map skill 1.13 (Implement Function Triggers Using Cosmos DB/Blob Data Operations, NCRONTAB Timers, and Webhooks), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `Source = BlobTriggerSource.EventGrid` paired with an Event Grid `BlobCreated` subscription triggers Functions immediately without container-log polling delays.
- **B:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Setting `Source = BlobTriggerSource.EventGrid` paired with an Event Grid `BlobCreated` subscription triggers Functions immediately without container-log polling delays.
- **C:** Correct. Event Grid-sourced blob triggers eliminate storage-log scan latency and work reliably on Blob-only / high-scale storage accounts. In this scenario: Setting `Source = BlobTriggerSource.EventGrid` paired with an Event Grid `BlobCreated` subscription triggers Functions immediately without container-log polling delays.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `Source = BlobTriggerSource.EventGrid` paired with an Event Grid `BlobCreated` subscription triggers Functions immediately without container-log polling delays.

### Question 25 — A, C, D

Answers: Define `new ContainerProperties(id: "telemetry", partitionKeyPaths: new List<string> { "/tenantId", "/siteId", "/deviceId" })` using `PartitionKeyBuilder` on reads and writes; Use `container.CreateTransactionalBatch(new PartitionKey(pkValue))` to group multiple create/replace/upsert/delete operations atomically within the same logical partition; Pass `new ItemRequestOptions { IfMatchEtag = item.ETag }` on `ReplaceItemAsync` and catch `CosmosException` when `StatusCode == HttpStatusCode.PreconditionFailed` (412). Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) overcome single-key 20 GB caps, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` enforces optimistic concurrency. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Supplying `IfMatchEtag` enforces optimistic concurrency control so concurrent writers fail with HTTP 412 rather than silently overwriting updates. In this scenario: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) overcome single-key 20 GB caps, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` enforces optimistic concurrency.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) overcome single-key 20 GB caps, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` enforces optimistic concurrency.
- **C:** Correct. Hierarchical partition keys (up to 3 levels) overcome the 20 GB logical-partition limit on large tenants while preserving efficient prefix queries on `/tenantId` alone. In this scenario: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) overcome single-key 20 GB caps, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` enforces optimistic concurrency.
- **D:** Correct. `TransactionalBatch` guarantees ACID all-or-nothing execution serialized in one network round-trip, strictly scoped to a single logical partition key. In this scenario: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) overcome single-key 20 GB caps, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` enforces optimistic concurrency.
- **E:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) overcome single-key 20 GB caps, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` enforces optimistic concurrency.
- **F:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) overcome single-key 20 GB caps, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` enforces optimistic concurrency.

### Question 26 — A

Answer: Configure `"indexingMode": "consistent"` with `"includedPaths": [{"path": "/customerId/?"}, {"path": "/createdUtc/?"}]` and `"excludedPaths": [{"path": "/*"}]`. Excluding `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing eliminates index maintenance on unqueried document paths. Excluding wildcard `/*` and indexing only queried filter paths dramatically cuts write Request Unit (RU) cost and index storage on write-heavy containers. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Excluding wildcard `/*` and indexing only queried filter paths dramatically cuts write Request Unit (RU) cost and index storage on write-heavy containers. In this scenario: Excluding `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing eliminates index maintenance on unqueried document paths.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Excluding `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing eliminates index maintenance on unqueried document paths.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Excluding `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing eliminates index maintenance on unqueried document paths.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Excluding `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing eliminates index maintenance on unqueried document paths.

### Question 27 — C

Answer: Call `await container.PatchItemAsync<Order>(id, new PartitionKey(pk), new[] { PatchOperation.Increment("/retryCount", 1), PatchOperation.Set("/lastStatus", "Queued") })`. `PatchItemAsync<T>` executes server-side `PatchOperation.Increment` and `PatchOperation.Set` mutations without reading and resending the entire document. Partial Document Update (`PatchItemAsync`) mutates specific JSON paths server-side without reading, deserializing, and replacing the full document payload. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `PatchItemAsync<T>` executes server-side `PatchOperation.Increment` and `PatchOperation.Set` mutations without reading and resending the entire document.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `PatchItemAsync<T>` executes server-side `PatchOperation.Increment` and `PatchOperation.Set` mutations without reading and resending the entire document.
- **C:** Correct. Partial Document Update (`PatchItemAsync`) mutates specific JSON paths server-side without reading, deserializing, and replacing the full document payload. In this scenario: `PatchItemAsync<T>` executes server-side `PatchOperation.Increment` and `PatchOperation.Set` mutations without reading and resending the entire document.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `PatchItemAsync<T>` executes server-side `PatchOperation.Increment` and `PatchOperation.Set` mutations without reading and resending the entire document.

### Question 28 — B

Answer: Use `Session` consistency (the default) and propagate `x-ms-session-token` (`RequestOptions.SessionToken`) across client/middle-tier hops to guarantee monotonic read-your-own-writes at half the read RU cost of `Strong`. Keeping `Session` consistency and round-tripping `SessionToken` (`x-ms-session-token`) across stateless API hops guarantees read-your-own-writes economically. `Session` consistency guarantees read-your-writes, monotonic reads, and write-follows-reads within a session token at 50% of `Strong` / `BoundedStaleness` read RUs. Local study-map skill 2.2 (Select and Override Cosmos DB Consistency Levels and Session Tokens), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Keeping `Session` consistency and round-tripping `SessionToken` (`x-ms-session-token`) across stateless API hops guarantees read-your-own-writes economically.
- **B:** Correct. `Session` consistency guarantees read-your-writes, monotonic reads, and write-follows-reads within a session token at 50% of `Strong` / `BoundedStaleness` read RUs. In this scenario: Keeping `Session` consistency and round-tripping `SessionToken` (`x-ms-session-token`) across stateless API hops guarantees read-your-own-writes economically.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Keeping `Session` consistency and round-tripping `SessionToken` (`x-ms-session-token`) across stateless API hops guarantees read-your-own-writes economically.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Keeping `Session` consistency and round-tripping `SessionToken` (`x-ms-session-token`) across stateless API hops guarantees read-your-own-writes economically.

### Question 29 — A

Answer: Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency. `BoundedStaleness` enforces global write order on secondary regions bounded by `K` item versions and `T` seconds. `Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds. Local study-map skill 2.2 (Select and Override Cosmos DB Consistency Levels and Session Tokens), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. `Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds. In this scenario: `BoundedStaleness` enforces global write order on secondary regions bounded by `K` item versions and `T` seconds.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `BoundedStaleness` enforces global write order on secondary regions bounded by `K` item versions and `T` seconds.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `BoundedStaleness` enforces global write order on secondary regions bounded by `K` item versions and `T` seconds.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `BoundedStaleness` enforces global write order on secondary regions bounded by `K` item versions and `T` seconds.

### Question 30 — A

Answer: Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`. Using `[CosmosDBTrigger]` (or Change Feed Processor) backed by a dedicated `leases` container pushes inserted and updated workspace documents in order across scaled workers without repetitive SQL scans. `CosmosDBTrigger` wraps the Change Feed Processor library and requires a lease container connection to coordinate partition checkpoints across scaled workers. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. `CosmosDBTrigger` wraps the Change Feed Processor library and requires a lease container connection to coordinate partition checkpoints across scaled workers. In this scenario: Using `[CosmosDBTrigger]` (or Change Feed Processor) backed by a dedicated `leases` container pushes inserted and updated workspace documents in order across scaled workers without repetitive SQL scans.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Using `[CosmosDBTrigger]` (or Change Feed Processor) backed by a dedicated `leases` container pushes inserted and updated workspace documents in order across scaled workers without repetitive SQL scans.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Using `[CosmosDBTrigger]` (or Change Feed Processor) backed by a dedicated `leases` container pushes inserted and updated workspace documents in order across scaled workers without repetitive SQL scans.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Using `[CosmosDBTrigger]` (or Change Feed Processor) backed by a dedicated `leases` container pushes inserted and updated workspace documents in order across scaled workers without repetitive SQL scans.

### Question 31 — A, D

Answers: Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay; Use Change Feed `AllVersionsAndDeletes` mode (or soft-delete flag items with short TTL in `LatestVersion` mode) because default `LatestVersion` change feed omits hard-deleted items. Distinct `processorName` values isolate each consumer's lease checkpoints, and `AllVersionsAndDeletes` mode (or soft-delete Tombstone items + TTL) surfaces deletions omitted by `LatestVersion`. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Standard `LatestVersion` change feed emits only inserts and updates of current items; hard deletes require `AllVersionsAndDeletes` or soft-delete Tombstone items + TTL. In this scenario: Distinct `processorName` values isolate each consumer's lease checkpoints, and `AllVersionsAndDeletes` mode (or soft-delete Tombstone items + TTL) surfaces deletions omitted by `LatestVersion`.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Distinct `processorName` values isolate each consumer's lease checkpoints, and `AllVersionsAndDeletes` mode (or soft-delete Tombstone items + TTL) surfaces deletions omitted by `LatestVersion`.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Distinct `processorName` values isolate each consumer's lease checkpoints, and `AllVersionsAndDeletes` mode (or soft-delete Tombstone items + TTL) surfaces deletions omitted by `LatestVersion`.
- **D:** Correct. In Change Feed Processor, `processorName` acts like an Event Hubs consumer group: distinct names receive independent copies of every insert/update, while identical names load-balance partitions. In this scenario: Distinct `processorName` values isolate each consumer's lease checkpoints, and `AllVersionsAndDeletes` mode (or soft-delete Tombstone items + TTL) surfaces deletions omitted by `LatestVersion`.
- **E:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Distinct `processorName` values isolate each consumer's lease checkpoints, and `AllVersionsAndDeletes` mode (or soft-delete Tombstone items + TTL) surfaces deletions omitted by `LatestVersion`.

### Question 32 — C

Answer: Enable container `DefaultTimeToLive = -1` (or positive seconds) and set item `ttl = 600` so Cosmos DB purges expired items automatically using background RU capacity. Setting container `DefaultTimeToLive = -1` enables item-level `ttl` expiration while preserving items that omit `ttl` indefinitely. Container TTL must be non-null (`-1` or `>0`) for per-item `ttl` seconds to take effect; setting `DefaultTimeToLive = null` ignores item-level `ttl`. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` enables item-level `ttl` expiration while preserving items that omit `ttl` indefinitely.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` enables item-level `ttl` expiration while preserving items that omit `ttl` indefinitely.
- **C:** Correct. Container TTL must be non-null (`-1` or `>0`) for per-item `ttl` seconds to take effect; setting `DefaultTimeToLive = null` ignores item-level `ttl`. In this scenario: Setting container `DefaultTimeToLive = -1` enables item-level `ttl` expiration while preserving items that omit `ttl` indefinitely.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` enables item-level `ttl` expiration while preserving items that omit `ttl` indefinitely.

### Question 33 — D

Answer: Attach searchable key-value `Tags` (`SetTagsAsync` / `BlobUploadOptions.Tags`) and query across containers with `FindBlobsByTagsAsync("@container = 'docs' AND status = 'pending'")`. Attaching Blob Index `Tags` (`SetTagsAsync`) and invoking `FindBlobsByTagsAsync` queries Azure Storage's native tag index without listing blobs. Blob Index Tags are indexed natively by Azure Storage for server-side filtering, whereas `Metadata` is not searchable without listing every blob. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. Why the keyed choice wins: Attaching Blob Index `Tags` (`SetTagsAsync`) and invoking `FindBlobsByTagsAsync` queries Azure Storage's native tag index without listing blobs.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Attaching Blob Index `Tags` (`SetTagsAsync`) and invoking `FindBlobsByTagsAsync` queries Azure Storage's native tag index without listing blobs.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Attaching Blob Index `Tags` (`SetTagsAsync`) and invoking `FindBlobsByTagsAsync` queries Azure Storage's native tag index without listing blobs.
- **D:** Correct. Blob Index Tags are indexed natively by Azure Storage for server-side filtering, whereas `Metadata` is not searchable without listing every blob. In this scenario: Attaching Blob Index `Tags` (`SetTagsAsync`) and invoking `FindBlobsByTagsAsync` queries Azure Storage's native tag index without listing blobs.

### Question 34 — D

Answer: Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`). `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata pairs. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata pairs.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata pairs.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata pairs.
- **D:** Correct. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. In this scenario: `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata pairs.

### Question 35 — B

Answer: Call `await blobClient.CreateSnapshotAsync()` for explicit point-in-time read-only checkpoints or enable account-level Blob Versioning so every `UploadAsync` overwrite retains an immutable `VersionId`. Account-level Blob Versioning automatically preserves prior `VersionId` states on every overwrite, while `CreateSnapshotAsync()` captures explicit read-only checkpoints. Snapshots capture explicit developer-triggered checkpoints, whereas Blob Versioning automatically preserves prior state on every overwrite or delete. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Account-level Blob Versioning automatically preserves prior `VersionId` states on every overwrite, while `CreateSnapshotAsync()` captures explicit read-only checkpoints.
- **B:** Correct. Snapshots capture explicit developer-triggered checkpoints, whereas Blob Versioning automatically preserves prior state on every overwrite or delete. In this scenario: Account-level Blob Versioning automatically preserves prior `VersionId` states on every overwrite, while `CreateSnapshotAsync()` captures explicit read-only checkpoints.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Account-level Blob Versioning automatically preserves prior `VersionId` states on every overwrite, while `CreateSnapshotAsync()` captures explicit read-only checkpoints.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Account-level Blob Versioning automatically preserves prior `VersionId` states on every overwrite, while `CreateSnapshotAsync()` captures explicit read-only checkpoints.

### Question 36 — B

Answer: Use `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` (15–60 seconds or `-1` infinite) and pass `LeaseId` inside `BlobRequestConditions` on subsequent writes/deletes. Calling `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` serializes exclusive single-writer access. Blob leases grant exclusive write/delete locks (`15` to `60` seconds or infinite `-1`) so competing workers immediately receive `412 LeaseIdMissing/Mismatch`. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Calling `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` serializes exclusive single-writer access.
- **B:** Correct. Blob leases grant exclusive write/delete locks (`15` to `60` seconds or infinite `-1`) so competing workers immediately receive `412 LeaseIdMissing/Mismatch`. In this scenario: Calling `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` serializes exclusive single-writer access.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Calling `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` serializes exclusive single-writer access.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Calling `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` serializes exclusive single-writer access.

### Question 37 — D

Answer: Invoke `BlobClient.StartCopyFromUriAsync(sourceSasUri)` to trigger asynchronous server-side blob copy and inspect `CopyStatus` without streaming bytes through the client VM. `BlobClient.StartCopyFromUriAsync(sourceSasUri)` delegates asynchronous server-side blob copy to Azure Storage fabric while `CopyStatus` tracks completion. `StartCopyFromUriAsync` instructs Azure Storage fabric to copy blobs asynchronously server-to-server using a readable source URI/SAS. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` delegates asynchronous server-side blob copy to Azure Storage fabric while `CopyStatus` tracks completion.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` delegates asynchronous server-side blob copy to Azure Storage fabric while `CopyStatus` tracks completion.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` delegates asynchronous server-side blob copy to Azure Storage fabric while `CopyStatus` tracks completion.
- **D:** Correct. `StartCopyFromUriAsync` instructs Azure Storage fabric to copy blobs asynchronously server-to-server using a readable source URI/SAS. In this scenario: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` delegates asynchronous server-side blob copy to Azure Storage fabric while `CopyStatus` tracks completion.

### Question 38 — B

Answer: Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`. Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` upholds least privilege. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` upholds least privilege.
- **B:** Correct. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. In this scenario: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` upholds least privilege.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` upholds least privilege.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` upholds least privilege.

### Question 39 — A, D

Answers: Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`); Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage. Lifecycle Management policy JSON rules automate `tierToCool` and `tierToArchive` transitions, while locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Time-based locked retention and legal holds block modification and deletion even by Storage Account Owners until retention expires and holds clear. In this scenario: Lifecycle Management policy JSON rules automate `tierToCool` and `tierToArchive` transitions, while locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Lifecycle Management policy JSON rules automate `tierToCool` and `tierToArchive` transitions, while locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Lifecycle Management policy JSON rules automate `tierToCool` and `tierToArchive` transitions, while locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention.
- **D:** Correct. Lifecycle management policies automate tier transitions and retention deletion server-side once per day without custom cron jobs. In this scenario: Lifecycle Management policy JSON rules automate `tierToCool` and `tierToArchive` transitions, while locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention.
- **E:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Lifecycle Management policy JSON rules automate `tierToCool` and `tierToArchive` transitions, while locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention.

### Question 40 — D

Answer: Verify the blob is currently in the Archive access tier → call SetAccessTier (or CopyBlob) targeting Hot or Cool with Standard or High rehydrate priority → poll ArchiveStatus until rehydration completes and tier updates → download the blob content. Confirming `Archive` tier, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with rehydrate priority, polling `ArchiveStatus` until online, and downloading retrieves the archive safely. Archived blobs are offline and unreadable directly; changing tier or copying to Hot/Cool initiates asynchronous rehydration that must finish before download. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. User metadata does not trigger storage rehydration, and setting tier back to Archive keeps the blob offline. Why the keyed choice wins: Confirming `Archive` tier, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with rehydrate priority, polling `ArchiveStatus` until online, and downloading retrieves the archive safely.
- **B:** Incorrect for this requirement. Calling Download directly on an Archive-tier blob immediately throws HTTP 409 Conflict (`BlobArchived`). Why the keyed choice wins: Confirming `Archive` tier, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with rehydrate priority, polling `ArchiveStatus` until online, and downloading retrieves the archive safely.
- **C:** Incorrect for this requirement. Leasing does not bring an offline Archive blob online; rehydration to Hot or Cool must complete before any read succeeds. Why the keyed choice wins: Confirming `Archive` tier, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with rehydrate priority, polling `ArchiveStatus` until online, and downloading retrieves the archive safely.
- **D:** Correct. Archived blobs are offline and unreadable directly; changing tier or copying to Hot/Cool initiates asynchronous rehydration that must finish before download. In this scenario: Confirming `Archive` tier, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with rehydrate priority, polling `ArchiveStatus` until online, and downloading retrieves the archive safely.

### Question 41 — B

Answer: Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob). `Archive` blobs cannot be read directly while offline; calling `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` triggers priority rehydration completing typically under an hour. `SetAccessTierAsync` (or copy-to-Hot) initiates Archive rehydration; `RehydratePriority.High` prioritizes restoration (often under 1 hour for <10 GB blobs). Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `Archive` blobs cannot be read directly while offline; calling `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` triggers priority rehydration completing typically under an hour.
- **B:** Correct. `SetAccessTierAsync` (or copy-to-Hot) initiates Archive rehydration; `RehydratePriority.High` prioritizes restoration (often under 1 hour for <10 GB blobs). In this scenario: `Archive` blobs cannot be read directly while offline; calling `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` triggers priority rehydration completing typically under an hour.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `Archive` blobs cannot be read directly while offline; calling `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` triggers priority rehydration completing typically under an hour.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `Archive` blobs cannot be read directly while offline; calling `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` triggers priority rehydration completing typically under an hour.

### Question 42 — B, C

Answers: Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps; Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`. `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public clients, while calling `AcquireTokenSilent` first and catching `MsalUiRequiredException` before `AcquireTokenInteractive` provides silent renewal. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public clients, while calling `AcquireTokenSilent` first and catching `MsalUiRequiredException` before `AcquireTokenInteractive` provides silent renewal.
- **B:** Correct. MSAL refreshes cached tokens transparently during `AcquireTokenSilent`; prompting interactively on every call degrades UX and hits rate limits. In this scenario: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public clients, while calling `AcquireTokenSilent` first and catching `MsalUiRequiredException` before `AcquireTokenInteractive` provides silent renewal.
- **C:** Correct. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. In this scenario: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public clients, while calling `AcquireTokenSilent` first and catching `MsalUiRequiredException` before `AcquireTokenInteractive` provides silent renewal.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public clients, while calling `AcquireTokenSilent` first and catching `MsalUiRequiredException` before `AcquireTokenInteractive` provides silent renewal.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public clients, while calling `AcquireTokenSilent` first and catching `MsalUiRequiredException` before `AcquireTokenInteractive` provides silent renewal.

### Question 43 — A

Answer: Use `ConfidentialClientApplicationBuilder` authenticated with a client certificate (or workload identity assertion) calling `AcquireTokenForClient(new[] { "api://.../.default" })` for headless background daemons. `ConfidentialClientApplicationBuilder` with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://metering/.default" })` executes OAuth 2.0 Client Credentials for headless services. Daemon apps without a signed-in user use OAuth 2.0 Client Credentials flow and must request the `.default` scope for pre-consented application permissions. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Daemon apps without a signed-in user use OAuth 2.0 Client Credentials flow and must request the `.default` scope for pre-consented application permissions. In this scenario: `ConfidentialClientApplicationBuilder` with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://metering/.default" })` executes OAuth 2.0 Client Credentials for headless services.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://metering/.default" })` executes OAuth 2.0 Client Credentials for headless services.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://metering/.default" })` executes OAuth 2.0 Client Credentials for headless services.
- **D:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://metering/.default" })` executes OAuth 2.0 Client Credentials for headless services.

### Question 44 — B

Answer: Declare `appRoles` with `allowedMemberTypes: ["User", "Application"]` in the Entra app registration manifest and validate the `roles` claim (`[Authorize(Roles = "...")]`) in the web API. Declaring `TenantAdmin` in `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both human users and service principals. Entra ID emits assigned app roles inside the `roles` JWT claim for both human users and service principals without requiring directory-level Entra admin roles. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Declaring `TenantAdmin` in `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both human users and service principals.
- **B:** Correct. Entra ID emits assigned app roles inside the `roles` JWT claim for both human users and service principals without requiring directory-level Entra admin roles. In this scenario: Declaring `TenantAdmin` in `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both human users and service principals.
- **C:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Declaring `TenantAdmin` in `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both human users and service principals.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Declaring `TenantAdmin` in `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both human users and service principals.

### Question 45 — D

Answer: Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`). Configuring unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean HTTP status codes instead of interactive `302` redirects. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Configuring unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean HTTP status codes instead of interactive `302` redirects.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Configuring unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean HTTP status codes instead of interactive `302` redirects.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Configuring unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean HTTP status codes instead of interactive `302` redirects.
- **D:** Correct. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. In this scenario: Configuring unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean HTTP status codes instead of interactive `302` redirects.

### Question 46 — B

Answer: Bind a Service SAS to a container/queue/table Stored Access Policy (`SignedIdentifier`, omitting inline start/expiry/permissions) so compromised tokens can be revoked instantly by modifying or deleting the policy. Binding the Service SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets operators revoke that token immediately by deleting or updating the policy. Up to 5 Stored Access Policies per container allow instant SAS revocation without rotating storage account keys; Note that User Delegation SAS uses key revocation instead of Stored Access Policies. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Binding the Service SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets operators revoke that token immediately by deleting or updating the policy.
- **B:** Correct. Up to 5 Stored Access Policies per container allow instant SAS revocation without rotating storage account keys; Note that User Delegation SAS uses key revocation instead of Stored Access Policies. In this scenario: Binding the Service SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets operators revoke that token immediately by deleting or updating the policy.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Binding the Service SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets operators revoke that token immediately by deleting or updating the policy.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Binding the Service SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets operators revoke that token immediately by deleting or updating the policy.

### Question 47 — B

Answer: Mint a short-lived HTTPS-only (`SasProtocol.HttpsOnly`) User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` instead of Account or Service SAS signed with storage account keys. Issuing User Delegation SAS tokens signed via `GetUserDelegationKeyAsync` uses Microsoft Entra RBAC credentials rather than disabled storage account shared keys. User Delegation SAS eliminates shared storage account keys, enforces Entra RBAC, and automatically invalidates if the signing identity loses permissions. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Issuing User Delegation SAS tokens signed via `GetUserDelegationKeyAsync` uses Microsoft Entra RBAC credentials rather than disabled storage account shared keys.
- **B:** Correct. User Delegation SAS eliminates shared storage account keys, enforces Entra RBAC, and automatically invalidates if the signing identity loses permissions. In this scenario: Issuing User Delegation SAS tokens signed via `GetUserDelegationKeyAsync` uses Microsoft Entra RBAC credentials rather than disabled storage account shared keys.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Issuing User Delegation SAS tokens signed via `GetUserDelegationKeyAsync` uses Microsoft Entra RBAC credentials rather than disabled storage account shared keys.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Issuing User Delegation SAS tokens signed via `GetUserDelegationKeyAsync` uses Microsoft Entra RBAC credentials rather than disabled storage account shared keys.

### Question 48 — A, E

Answers: Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses; Call `await graphClient.Users.GetAsync(rc => { rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }; rc.QueryParameters.Filter = "accountEnabled eq true"; })`. Using `QueryParameters.Select` + `QueryParameters.Filter` in Graph SDK v5 trims payloads, while `BatchRequestContentCollection` (`/$batch`) bundles up to 20 sub-requests and honors `Retry-After`. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. In Microsoft Graph .NET SDK v5, `$select` and `$filter` query parameters reduce payload size and network transfer on collection endpoints. In this scenario: Using `QueryParameters.Select` + `QueryParameters.Filter` in Graph SDK v5 trims payloads, while `BatchRequestContentCollection` (`/$batch`) bundles up to 20 sub-requests and honors `Retry-After`.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Using `QueryParameters.Select` + `QueryParameters.Filter` in Graph SDK v5 trims payloads, while `BatchRequestContentCollection` (`/$batch`) bundles up to 20 sub-requests and honors `Retry-After`.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Using `QueryParameters.Select` + `QueryParameters.Filter` in Graph SDK v5 trims payloads, while `BatchRequestContentCollection` (`/$batch`) bundles up to 20 sub-requests and honors `Retry-After`.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Using `QueryParameters.Select` + `QueryParameters.Filter` in Graph SDK v5 trims payloads, while `BatchRequestContentCollection` (`/$batch`) bundles up to 20 sub-requests and honors `Retry-After`.
- **E:** Correct. Graph JSON batching (`/$batch`) bundles up to 20 sub-requests per round-trip, while built-in SDK retry middleware respects `Retry-After`. In this scenario: Using `QueryParameters.Select` + `QueryParameters.Filter` in Graph SDK v5 trims payloads, while `BatchRequestContentCollection` (`/$batch`) bundles up to 20 sub-requests and honors `Retry-After`.

### Question 49 — D

Answer: Call `await confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` inside the middle-tier API. `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the user token via OAuth 2.0 On-Behalf-Of. OAuth 2.0 On-Behalf-Of (`AcquireTokenOnBehalfOf`) exchanges an incoming user access token for a downstream API token while preserving delegated user identity and consent. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the user token via OAuth 2.0 On-Behalf-Of.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the user token via OAuth 2.0 On-Behalf-Of.
- **C:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the user token via OAuth 2.0 On-Behalf-Of.
- **D:** Correct. OAuth 2.0 On-Behalf-Of (`AcquireTokenOnBehalfOf`) exchanges an incoming user access token for a downstream API token while preserving delegated user identity and consent. In this scenario: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the user token via OAuth 2.0 On-Behalf-Of.

### Question 50 — C

Answer: Enable Managed Identity with App Configuration Data Reader + Key Vault Secrets User → add Key Vault references and a sentinel key → wire AddAzureAppConfiguration with ConfigureKeyVault and ConfigureRefresh → invoke UseAzureAppConfiguration middleware. Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware enables atomic reload. RBAC on both stores is required because App Configuration stores only the URI pointer; `ConfigureRefresh` + middleware poll the sentinel key on incoming requests. Local study-map skill 3.5 (Manage Feature Flags, Labels, Sentinel Dynamic Refresh, and Key Vault References in Azure App Configuration), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Committing exported secret values defeats Key Vault reference rotation and violates secret hygiene. Why the keyed choice wins: Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware enables atomic reload.
- **B:** Incorrect for this requirement. In ASP.NET Core, dynamic refresh is request-driven via `UseAzureAppConfiguration()` middleware (or manual `TryRefreshAsync`), not an automatic push without it. Why the keyed choice wins: Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware enables atomic reload.
- **C:** Correct. RBAC on both stores is required because App Configuration stores only the URI pointer; `ConfigureRefresh` + middleware poll the sentinel key on incoming requests. In this scenario: Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware enables atomic reload.
- **D:** Incorrect for this requirement. Without Key Vault Secrets User on the vault itself, resolving a Key Vault reference throws 403 Forbidden at startup. Why the keyed choice wins: Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware enables atomic reload.

### Question 51 — A

Answer: Wire `options.Connect(new Uri(endpoint), cred).ConfigureKeyVault(kv => kv.SetCredential(cred))` so App Configuration resolves Key Vault reference items using the app identity. App Configuration returns only the Key Vault secret URI metadata; chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` lets the client resolve secrets directly from Key Vault using `Key Vault Secrets User`. App Configuration stores only the Key Vault secret URI metadata; client code still requires `ConfigureKeyVault` credentials with `Key Vault Secrets User` rights on the target vault. Local study-map skill 3.5 (Manage Feature Flags, Labels, Sentinel Dynamic Refresh, and Key Vault References in Azure App Configuration), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. App Configuration stores only the Key Vault secret URI metadata; client code still requires `ConfigureKeyVault` credentials with `Key Vault Secrets User` rights on the target vault. In this scenario: App Configuration returns only the Key Vault secret URI metadata; chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` lets the client resolve secrets directly from Key Vault using `Key Vault Secrets User`.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: App Configuration returns only the Key Vault secret URI metadata; chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` lets the client resolve secrets directly from Key Vault using `Key Vault Secrets User`.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: App Configuration returns only the Key Vault secret URI metadata; chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` lets the client resolve secrets directly from Key Vault using `Key Vault Secrets User`.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: App Configuration returns only the Key Vault secret URI metadata; chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` lets the client resolve secrets directly from Key Vault using `Key Vault Secrets User`.

### Question 52 — A, D

Answers: Use `SecretClient` (`Azure.Security.KeyVault.Secrets`) for connection strings/tokens, `KeyClient` / `CryptographyClient` (`Azure.Security.KeyVault.Keys`) for RSA/EC wrap-unwrap-sign, and `CertificateClient` for X.509 lifecycle; Enable Soft Delete (mandatory on new vaults, 7–90 days) plus Purge Protection on Azure Key Vault so neither accidental deletion nor malicious principals can permanently destroy keys before retention expires. Using dedicated `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete and Purge Protection meets both operational and compliance rules. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Azure Key Vault SDK v4 splits secrets, cryptographic keys, and X.509 certificates into dedicated clients and RBAC data-plane roles (`Key Vault Secrets User`, `Crypto User`, `Certificates User`). In this scenario: Using dedicated `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete and Purge Protection meets both operational and compliance rules.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Using dedicated `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete and Purge Protection meets both operational and compliance rules.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Using dedicated `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete and Purge Protection meets both operational and compliance rules.
- **D:** Correct. Soft Delete allows recovery via `StartRecoverDeletedSecretAsync`, while Purge Protection blocks permanent `PurgeDeletedSecretAsync` calls during retention. In this scenario: Using dedicated `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete and Purge Protection meets both operational and compliance rules.
- **E:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Using dedicated `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete and Purge Protection meets both operational and compliance rules.

### Question 53 — D

Answer: Instantiate `new CryptographyClient(keyVaultKey.Id, new DefaultAzureCredential())` and invoke `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync(...)`. `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` implements envelope encryption without uploading PDF bytes to Key Vault. Envelope encryption keeps bulk data encryption keys (`DEK`) wrapped by hardware/software-protected Key Vault KEKs without sending large payloads through Key Vault. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` implements envelope encryption without uploading PDF bytes to Key Vault.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` implements envelope encryption without uploading PDF bytes to Key Vault.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` implements envelope encryption without uploading PDF bytes to Key Vault.
- **D:** Correct. Envelope encryption keeps bulk data encryption keys (`DEK`) wrapped by hardware/software-protected Key Vault KEKs without sending large payloads through Key Vault. In this scenario: `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` implements envelope encryption without uploading PDF bytes to Key Vault.

### Question 54 — A

Answer: Configure App Service / Functions application settings using `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` (omitting secret version) paired with `Key Vault Secrets User` on the app Managed Identity. `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity resolves rotated versions transparently. Versionless Key Vault references automatically pull rotated secret versions within 24 hours (or immediately on config change / manual sync) with zero SDK boilerplate. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Versionless Key Vault references automatically pull rotated secret versions within 24 hours (or immediately on config change / manual sync) with zero SDK boilerplate. In this scenario: `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity resolves rotated versions transparently.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity resolves rotated versions transparently.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity resolves rotated versions transparently.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity resolves rotated versions transparently.

### Question 55 — C

Answer: Instantiate `new DefaultAzureCredential()` (or explicit `ManagedIdentityCredential(clientId)` for user-assigned identities in production) so identical code authenticates via Azure CLI / Visual Studio locally and Managed Identity in Azure. `DefaultAzureCredential` probes developer workstation credentials locally and switches automatically to IMDS `ManagedIdentityCredential` in Azure. `DefaultAzureCredential` chains developer workstation credentials locally and IMDS Managed Identity in Azure; passing `managedIdentityClientId` is required when selecting a specific user-assigned identity. Local study-map skill 3.7 (Implement System-Assigned and User-Assigned Managed Identities and DefaultAzureCredential), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `DefaultAzureCredential` probes developer workstation credentials locally and switches automatically to IMDS `ManagedIdentityCredential` in Azure.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `DefaultAzureCredential` probes developer workstation credentials locally and switches automatically to IMDS `ManagedIdentityCredential` in Azure.
- **C:** Correct. `DefaultAzureCredential` chains developer workstation credentials locally and IMDS Managed Identity in Azure; passing `managedIdentityClientId` is required when selecting a specific user-assigned identity. In this scenario: `DefaultAzureCredential` probes developer workstation credentials locally and switches automatically to IMDS `ManagedIdentityCredential` in Azure.
- **D:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `DefaultAzureCredential` probes developer workstation credentials locally and switches automatically to IMDS `ManagedIdentityCredential` in Azure.

### Question 56 — A

Answer: Instantiate `new DefaultAzureCredential(new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId })` (or set `AZURE_CLIENT_ID`). Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) selects the exact user-assigned identity. When a host has multiple user-assigned managed identities attached, IMDS rejects ambiguous token requests unless the target `clientId` (or resource ID) is specified. Local study-map skill 3.7 (Implement System-Assigned and User-Assigned Managed Identities and DefaultAzureCredential), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. When a host has multiple user-assigned managed identities attached, IMDS rejects ambiguous token requests unless the target `clientId` (or resource ID) is specified. In this scenario: Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) selects the exact user-assigned identity.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) selects the exact user-assigned identity.
- **C:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) selects the exact user-assigned identity.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) selects the exact user-assigned identity.

### Question 57 — A, B

Answers: Query Workspace-based Application Insights (`AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces` or classic `requests`/`dependencies`/`exceptions`) joining on `OperationId` (`operation_Id`) to reconstruct end-to-end distributed transactions; Run `AppRequests | where ResultCode == "500" | join kind=inner (AppDependencies | where Success == false) on OperationId | project TimeGenerated, Name, Target, DependencyType, ResultCode1`. Joining `AppRequests` (`ResultCode == "500"`) with failed `AppDependencies` on shared W3C `OperationId` (`operation_Id`) pinpoints exact failing downstream dependencies across services. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. W3C Trace-Context propagates `traceparent` into `operation_Id` across services so KQL joins pinpoint exact failing downstream dependencies. In this scenario: Joining `AppRequests` (`ResultCode == "500"`) with failed `AppDependencies` on shared W3C `OperationId` (`operation_Id`) pinpoints exact failing downstream dependencies across services.
- **B:** Correct. Joining `AppRequests` and `AppDependencies` on `OperationId` isolates which exact downstream SQL, HTTP, or Storage dependency triggered HTTP 500 responses. In this scenario: Joining `AppRequests` (`ResultCode == "500"`) with failed `AppDependencies` on shared W3C `OperationId` (`operation_Id`) pinpoints exact failing downstream dependencies across services.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Joining `AppRequests` (`ResultCode == "500"`) with failed `AppDependencies` on shared W3C `OperationId` (`operation_Id`) pinpoints exact failing downstream dependencies across services.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Joining `AppRequests` (`ResultCode == "500"`) with failed `AppDependencies` on shared W3C `OperationId` (`operation_Id`) pinpoints exact failing downstream dependencies across services.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Joining `AppRequests` (`ResultCode == "500"`) with failed `AppDependencies` on shared W3C `OperationId` (`operation_Id`) pinpoints exact failing downstream dependencies across services.

### Question 58 — C

Answer: Run `AppRequests | where TimeGenerated > ago(1h) | summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)`. Running `AppRequests` over `ago(1h)` with `summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` computes 5-minute failure and p95 latency series. KQL `countif` and `percentile(..., 95)` grouped by `bin(TimeGenerated, 5m)` quantify error spikes and tail latency per operation over fixed time buckets. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Running `AppRequests` over `ago(1h)` with `summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` computes 5-minute failure and p95 latency series.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Running `AppRequests` over `ago(1h)` with `summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` computes 5-minute failure and p95 latency series.
- **C:** Correct. KQL `countif` and `percentile(..., 95)` grouped by `bin(TimeGenerated, 5m)` quantify error spikes and tail latency per operation over fixed time buckets. In this scenario: Running `AppRequests` over `ago(1h)` with `summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` computes 5-minute failure and p95 latency series.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Running `AppRequests` over `ago(1h)` with `summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` computes 5-minute failure and p95 latency series.

### Question 59 — D

Answer: Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits. Invoking `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) followed by a brief delay before process exit flushes buffered items to Azure Monitor. Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Invoking `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) followed by a brief delay before process exit flushes buffered items to Azure Monitor.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Invoking `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) followed by a brief delay before process exit flushes buffered items to Azure Monitor.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Invoking `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) followed by a brief delay before process exit flushes buffered items to Azure Monitor.
- **D:** Correct. Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics. In this scenario: Invoking `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) followed by a brief delay before process exit flushes buffered items to Azure Monitor.

### Question 60 — A

Answer: Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`. Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` emits standard OpenTelemetry spans. `System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. `System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro. In this scenario: Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` emits standard OpenTelemetry spans.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` emits standard OpenTelemetry spans.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` emits standard OpenTelemetry spans.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` emits standard OpenTelemetry spans.

### Question 61 — C

Answer: Create an Azure Monitor Metric Alert (Dynamic Thresholds or static p95 latency/5xx count) or Scheduled Query (KQL) Alert targeting an Action Group configured with webhook / Azure Function / email-SMS receivers. An Azure Monitor Metric Alert with Dynamic Thresholds adapts automatically to weekly seasonality and fires an Action Group webhook receiver. Metric alerts offer sub-minute stateful evaluation on numeric signals, whereas Scheduled Query Rules run expressive KQL joins on log tables at configured intervals. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: An Azure Monitor Metric Alert with Dynamic Thresholds adapts automatically to weekly seasonality and fires an Action Group webhook receiver.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: An Azure Monitor Metric Alert with Dynamic Thresholds adapts automatically to weekly seasonality and fires an Action Group webhook receiver.
- **C:** Correct. Metric alerts offer sub-minute stateful evaluation on numeric signals, whereas Scheduled Query Rules run expressive KQL joins on log tables at configured intervals. In this scenario: An Azure Monitor Metric Alert with Dynamic Thresholds adapts automatically to weekly seasonality and fires an Action Group webhook receiver.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: An Azure Monitor Metric Alert with Dynamic Thresholds adapts automatically to weekly seasonality and fires an Action Group webhook receiver.

### Question 62 — D

Answer: Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group. Deploying a VNet-integrated Timer-Triggered Function that probes the private endpoint and calls `TelemetryClient.TrackAvailability()` publishes synthetic availability results for Azure Monitor alerts. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Deploying a VNet-integrated Timer-Triggered Function that probes the private endpoint and calls `TelemetryClient.TrackAvailability()` publishes synthetic availability results for Azure Monitor alerts.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Deploying a VNet-integrated Timer-Triggered Function that probes the private endpoint and calls `TelemetryClient.TrackAvailability()` publishes synthetic availability results for Azure Monitor alerts.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Deploying a VNet-integrated Timer-Triggered Function that probes the private endpoint and calls `TelemetryClient.TrackAvailability()` publishes synthetic availability results for Azure Monitor alerts.
- **D:** Correct. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. In this scenario: Deploying a VNet-integrated Timer-Triggered Function that probes the private endpoint and calls `TelemetryClient.TrackAvailability()` publishes synthetic availability results for Azure Monitor alerts.

### Question 63 — C

Answer: Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments. Calling `.UseAzureMonitor()` from `Azure.Monitor.OpenTelemetry.AspNetCore` registers trace, metric, and log exporters targeting the Workspace-based Application Insights connection string. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Calling `.UseAzureMonitor()` from `Azure.Monitor.OpenTelemetry.AspNetCore` registers trace, metric, and log exporters targeting the Workspace-based Application Insights connection string.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Calling `.UseAzureMonitor()` from `Azure.Monitor.OpenTelemetry.AspNetCore` registers trace, metric, and log exporters targeting the Workspace-based Application Insights connection string.
- **C:** Correct. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. In this scenario: Calling `.UseAzureMonitor()` from `Azure.Monitor.OpenTelemetry.AspNetCore` registers trace, metric, and log exporters targeting the Workspace-based Application Insights connection string.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Calling `.UseAzureMonitor()` from `Azure.Monitor.OpenTelemetry.AspNetCore` registers trace, metric, and log exporters targeting the Workspace-based Application Insights connection string.

### Question 64 — A, D

Answers: Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments; Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently. `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles modern OpenTelemetry collection, while Ingestion/Adaptive Sampling controls stored volume without sampling Live Metrics. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. In this scenario: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles modern OpenTelemetry collection, while Ingestion/Adaptive Sampling controls stored volume without sampling Live Metrics.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles modern OpenTelemetry collection, while Ingestion/Adaptive Sampling controls stored volume without sampling Live Metrics.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles modern OpenTelemetry collection, while Ingestion/Adaptive Sampling controls stored volume without sampling Live Metrics.
- **D:** Correct. Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled. In this scenario: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles modern OpenTelemetry collection, while Ingestion/Adaptive Sampling controls stored volume without sampling Live Metrics.
- **E:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles modern OpenTelemetry collection, while Ingestion/Adaptive Sampling controls stored volume without sampling Live Metrics.

### Question 65 — B

Answer: Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently. Ingestion Sampling at the Application Insights workspace hashes `operation_Id` centrally so every span of a sampled distributed transaction is retained together. Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Ingestion Sampling at the Application Insights workspace hashes `operation_Id` centrally so every span of a sampled distributed transaction is retained together.
- **B:** Correct. Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled. In this scenario: Ingestion Sampling at the Application Insights workspace hashes `operation_Id` centrally so every span of a sampled distributed transaction is retained together.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Ingestion Sampling at the Application Insights workspace hashes `operation_Id` centrally so every span of a sampled distributed transaction is retained together.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Ingestion Sampling at the Application Insights workspace hashes `operation_Id` centrally so every span of a sampled distributed transaction is retained together.

### Question 66 — C

Answer: Select `Developer` (non-SLA) or `Premium` / `Standard v2` for VNet integration, and deploy the containerized APIM Self-Hosted Gateway (`mcr.microsoft.com/azure-api-management/gateway`) for hybrid on-premises/multi-cloud local traffic routing. Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway in the customer cluster keeps data-plane traffic local while syncing config from Azure. Self-hosted gateways require `Developer` or `Premium` tier and keep data-plane traffic local while pulling policy updates outbound over HTTPS/443 from Azure. Local study-map skill 5.1 (Provision Azure API Management Tiers, VNet Modes, and Self-Hosted Hybrid Gateways), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway in the customer cluster keeps data-plane traffic local while syncing config from Azure.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway in the customer cluster keeps data-plane traffic local while syncing config from Azure.
- **C:** Correct. Self-hosted gateways require `Developer` or `Premium` tier and keep data-plane traffic local while pulling policy updates outbound over HTTPS/443 from Azure. In this scenario: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway in the customer cluster keeps data-plane traffic local while syncing config from Azure.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway in the customer cluster keeps data-plane traffic local while syncing config from Azure.

### Question 67 — A

Answer: Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`. `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens minted for APIM. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. Local study-map skill 5.1 (Provision Azure API Management Tiers, VNet Modes, and Self-Hosted Hybrid Gateways), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. In this scenario: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens minted for APIM.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens minted for APIM.
- **C:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens minted for APIM.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens minted for APIM.

### Question 68 — C

Answer: Use `<mock-response status-code="200" content-type="application/json" />` during frontend parallel development, or `<rewrite-uri template="/internal/v2/orders/{orderId}" />` with `<set-backend-service base-url="..." />` in `<inbound>`. `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI examples early, while `<rewrite-uri>` + `<set-backend-service>` remap external URLs onto internal routes. `<mock-response>` short-circuits backend forwarding using OpenAPI example payloads, while `<rewrite-uri>` maps public clean paths onto legacy internal routes. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI examples early, while `<rewrite-uri>` + `<set-backend-service>` remap external URLs onto internal routes.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI examples early, while `<rewrite-uri>` + `<set-backend-service>` remap external URLs onto internal routes.
- **C:** Correct. `<mock-response>` short-circuits backend forwarding using OpenAPI example payloads, while `<rewrite-uri>` maps public clean paths onto legacy internal routes. In this scenario: `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI examples early, while `<rewrite-uri>` + `<set-backend-service>` remap external URLs onto internal routes.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI examples early, while `<rewrite-uri>` + `<set-backend-service>` remap external URLs onto internal routes.

### Question 69 — B

Answer: Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation. `AuthorizationLevel.Function` requires a function or host key (`x-functions-key` or `?code=`), matching APIM's automated Function import binding. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `AuthorizationLevel.Function` requires a function or host key (`x-functions-key` or `?code=`), matching APIM's automated Function import binding.
- **B:** Correct. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. In this scenario: `AuthorizationLevel.Function` requires a function or host key (`x-functions-key` or `?code=`), matching APIM's automated Function import binding.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `AuthorizationLevel.Function` requires a function or host key (`x-functions-key` or `?code=`), matching APIM's automated Function import binding.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `AuthorizationLevel.Function` requires a function or host key (`x-functions-key` or `?code=`), matching APIM's automated Function import binding.

### Question 70 — C

Answer: Enable Managed Identity on the APIM instance → grant that identity RBAC or app-role access on the target backend/Key Vault → add authentication-managed-identity in APIM policy XML → test backend calls and inspect APIM trace headers. Enabling Managed Identity on APIM, granting that identity RBAC/app-role access on the billing backend, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying APIM trace headers completes rollout safely. APIM needs an active managed identity and target RBAC/app-role grant before `<authentication-managed-identity>` can mint valid Entra bearer tokens. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Backend authorization checks the APIM gateway managed identity, not the developer workstation, and `<validate-jwt>` validates caller tokens in `<inbound>`. Why the keyed choice wins: Enabling Managed Identity on APIM, granting that identity RBAC/app-role access on the billing backend, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying APIM trace headers completes rollout safely.
- **B:** Incorrect for this requirement. Saving or invoking `<authentication-managed-identity>` before enabling Managed Identity and target RBAC fails token acquisition or returns 401/403. Why the keyed choice wins: Enabling Managed Identity on APIM, granting that identity RBAC/app-role access on the billing backend, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying APIM trace headers completes rollout safely.
- **C:** Correct. APIM needs an active managed identity and target RBAC/app-role grant before `<authentication-managed-identity>` can mint valid Entra bearer tokens. In this scenario: Enabling Managed Identity on APIM, granting that identity RBAC/app-role access on the billing backend, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying APIM trace headers completes rollout safely.
- **D:** Incorrect for this requirement. Hardcoding static secrets in policy XML creates rotation debt when `<authentication-managed-identity>` handles token lifecycle natively. Why the keyed choice wins: Enabling Managed Identity on APIM, granting that identity RBAC/app-role access on the billing backend, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying APIM trace headers completes rollout safely.

### Question 71 — B, E

Answers: Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers; Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`. Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` checks with `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) blocks invalid partner calls before hitting backends. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` checks with `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) blocks invalid partner calls before hitting backends.
- **B:** Correct. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. In this scenario: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` checks with `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) blocks invalid partner calls before hitting backends.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` checks with `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) blocks invalid partner calls before hitting backends.
- **D:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` checks with `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) blocks invalid partner calls before hitting backends.
- **E:** Correct. Combining gateway `<validate-jwt>` pre-authentication with subscription scoping and client-certificate thumbprint checks blocks invalid traffic before hitting backends. In this scenario: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` checks with `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) blocks invalid partner calls before hitting backends.

### Question 72 — B

Answer: Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`. `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates JWTs at the APIM edge. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates JWTs at the APIM edge.
- **B:** Correct. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. In this scenario: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates JWTs at the APIM edge.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates JWTs at the APIM edge.
- **D:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates JWTs at the APIM edge.

### Question 73 — B, C, E

Answers: Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`; Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`; Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`. `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` implement all three. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` implement all three.
- **B:** Correct. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` implement all three.
- **C:** Correct. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` implement all three.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` implement all three.
- **E:** Correct. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` implement all three.
- **F:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` implement all three.

### Question 74 — C

Answer: Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`. `<quota-by-key>` returns `403 Forbidden` (meant for long-term monetization caps) rather than `429` (`<rate-limit-by-key>`), and deleting `<base />` drops parent-scope `<validate-jwt>` policies. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<quota-by-key>` returns `403 Forbidden` (meant for long-term monetization caps) rather than `429` (`<rate-limit-by-key>`), and deleting `<base />` drops parent-scope `<validate-jwt>` policies.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `<quota-by-key>` returns `403 Forbidden` (meant for long-term monetization caps) rather than `429` (`<rate-limit-by-key>`), and deleting `<base />` drops parent-scope `<validate-jwt>` policies.
- **C:** Correct. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! In this scenario: `<quota-by-key>` returns `403 Forbidden` (meant for long-term monetization caps) rather than `429` (`<rate-limit-by-key>`), and deleting `<base />` drops parent-scope `<validate-jwt>` policies.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<quota-by-key>` returns `403 Forbidden` (meant for long-term monetization caps) rather than `429` (`<rate-limit-by-key>`), and deleting `<base />` drops parent-scope `<validate-jwt>` policies.

### Question 75 — A

Answer: Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`. Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` keys cache entries per language. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. In this scenario: Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` keys cache entries per language.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` keys cache entries per language.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` keys cache entries per language.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` keys cache entries per language.

### Question 76 — D

Answer: Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization. Provisioning an Azure Event Grid Domain manages tens of thousands of tenant-isolated domain topics behind one endpoint with granular per-topic Azure RBAC. Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Provisioning an Azure Event Grid Domain manages tens of thousands of tenant-isolated domain topics behind one endpoint with granular per-topic Azure RBAC.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Provisioning an Azure Event Grid Domain manages tens of thousands of tenant-isolated domain topics behind one endpoint with granular per-topic Azure RBAC.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Provisioning an Azure Event Grid Domain manages tens of thousands of tenant-isolated domain topics behind one endpoint with granular per-topic Azure RBAC.
- **D:** Correct. Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures. In this scenario: Provisioning an Azure Event Grid Domain manages tens of thousands of tenant-isolated domain topics behind one endpoint with granular per-topic Azure RBAC.

### Question 77 — A, D

Answers: Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL; Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization. Event Grid Domains host thousands of RBAC-isolated tenant topics behind one endpoint, while `CloudEvents v1.0` subscriptions with subject filters and Blob dead-lettering handle filtered durable push delivery. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures. In this scenario: Event Grid Domains host thousands of RBAC-isolated tenant topics behind one endpoint, while `CloudEvents v1.0` subscriptions with subject filters and Blob dead-lettering handle filtered durable push delivery.
- **B:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Event Grid Domains host thousands of RBAC-isolated tenant topics behind one endpoint, while `CloudEvents v1.0` subscriptions with subject filters and Blob dead-lettering handle filtered durable push delivery.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Event Grid Domains host thousands of RBAC-isolated tenant topics behind one endpoint, while `CloudEvents v1.0` subscriptions with subject filters and Blob dead-lettering handle filtered durable push delivery.
- **D:** Correct. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. In this scenario: Event Grid Domains host thousands of RBAC-isolated tenant topics behind one endpoint, while `CloudEvents v1.0` subscriptions with subject filters and Blob dead-lettering handle filtered durable push delivery.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Event Grid Domains host thousands of RBAC-isolated tenant topics behind one endpoint, while `CloudEvents v1.0` subscriptions with subject filters and Blob dead-lettering handle filtered durable push delivery.

### Question 78 — A

Answer: Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`. Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` proves endpoint ownership. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. In this scenario: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` proves endpoint ownership.
- **B:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` proves endpoint ownership.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` proves endpoint ownership.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` proves endpoint ownership.

### Question 79 — D

Answer: Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL. Configuring `subjectBeginsWith: "/tenant/acme/"`, `advancedFilters` (`NumberGreaterThanOrEquals`), retry TTL up to 24h, and a Blob dead-letter endpoint satisfies both filtering and durability. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Configuring `subjectBeginsWith: "/tenant/acme/"`, `advancedFilters` (`NumberGreaterThanOrEquals`), retry TTL up to 24h, and a Blob dead-letter endpoint satisfies both filtering and durability.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Configuring `subjectBeginsWith: "/tenant/acme/"`, `advancedFilters` (`NumberGreaterThanOrEquals`), retry TTL up to 24h, and a Blob dead-letter endpoint satisfies both filtering and durability.
- **C:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Configuring `subjectBeginsWith: "/tenant/acme/"`, `advancedFilters` (`NumberGreaterThanOrEquals`), retry TTL up to 24h, and a Blob dead-letter endpoint satisfies both filtering and durability.
- **D:** Correct. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. In this scenario: Configuring `subjectBeginsWith: "/tenant/acme/"`, `advancedFilters` (`NumberGreaterThanOrEquals`), retry TTL up to 24h, and a Blob dead-letter endpoint satisfies both filtering and durability.

### Question 80 — D

Answer: Create the Event Hub, consumer group, and Blob checkpoint container → instantiate BlobContainerClient and EventProcessorClient → register ProcessEventAsync (calling UpdateCheckpointAsync) and ProcessErrorAsync → call StartProcessingAsync before StopProcessingAsync. Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly. `EventProcessorClient` coordinates partition ownership and offset checkpoints in Blob Storage and requires both event and error handlers registered prior to `StartProcessingAsync`. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Sharing one consumer group and checkpoint prefix across distinct apps causes them to steal partitions from each other instead of each reading the full stream. Why the keyed choice wins: Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly.
- **B:** Incorrect for this requirement. Producers publish events and never hold partition checkpoints; `EventProcessorClient` handles balanced consumer checkpointing. Why the keyed choice wins: Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly.
- **C:** Incorrect for this requirement. `EventProcessorClient` throws `InvalidOperationException` if started before registering both `ProcessEventAsync` and `ProcessErrorAsync`. Why the keyed choice wins: Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly.
- **D:** Correct. `EventProcessorClient` coordinates partition ownership and offset checkpoints in Blob Storage and requires both event and error handlers registered prior to `StartProcessingAsync`. In this scenario: Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly.

### Question 81 — C

Answer: Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2. Provisioning a dedicated Consumer Group per downstream team plus enabling Event Hubs Capture to ADLS Gen2 isolates cursors and automates cold Parquet archival. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Provisioning a dedicated Consumer Group per downstream team plus enabling Event Hubs Capture to ADLS Gen2 isolates cursors and automates cold Parquet archival.
- **B:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Provisioning a dedicated Consumer Group per downstream team plus enabling Event Hubs Capture to ADLS Gen2 isolates cursors and automates cold Parquet archival.
- **C:** Correct. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. In this scenario: Provisioning a dedicated Consumer Group per downstream team plus enabling Event Hubs Capture to ADLS Gen2 isolates cursors and automates cold Parquet archival.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Provisioning a dedicated Consumer Group per downstream team plus enabling Event Hubs Capture to ADLS Gen2 isolates cursors and automates cold Parquet archival.

### Question 82 — B

Answer: Host `EventProcessorClient` backed by `BlobContainerClient` and call `await eventArgs.UpdateCheckpointAsync()` after idempotent batch persistence so partition leases resume cleanly after rebalancing. Calling `await eventArgs.UpdateCheckpointAsync()` persists the latest sequence/offset in Blob metadata so new partition owners resume from the checkpoint. `EventProcessorClient` coordinates partition ownership via Azure Blob leases and records per-partition sequence/offset checkpoints in Blob metadata. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Calling `await eventArgs.UpdateCheckpointAsync()` persists the latest sequence/offset in Blob metadata so new partition owners resume from the checkpoint.
- **B:** Correct. `EventProcessorClient` coordinates partition ownership via Azure Blob leases and records per-partition sequence/offset checkpoints in Blob metadata. In this scenario: Calling `await eventArgs.UpdateCheckpointAsync()` persists the latest sequence/offset in Blob metadata so new partition owners resume from the checkpoint.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Calling `await eventArgs.UpdateCheckpointAsync()` persists the latest sequence/offset in Blob metadata so new partition owners resume from the checkpoint.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Calling `await eventArgs.UpdateCheckpointAsync()` persists the latest sequence/offset in Blob metadata so new partition owners resume from the checkpoint.

### Question 83 — C

Answer: Create the queue or subscription with RequiresSession = true at creation time → send ServiceBusMessage instances setting a non-empty SessionId → create a ServiceBusSessionProcessor (or AcceptNextSessionAsync receiver) → process messages in order and complete/renew session locks. Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = envelopeId` on every message, and consuming via `ServiceBusSessionProcessor` locks per-envelope FIFO order. `RequiresSession` can only be enabled when creating the entity, producers must populate `SessionId`, and consumers must use session-aware receivers/processors. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Azure Queue Storage does not support brokered `SessionId` FIFO locks; Azure Service Bus session entities are required. Why the keyed choice wins: Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = envelopeId` on every message, and consuming via `ServiceBusSessionProcessor` locks per-envelope FIFO order.
- **B:** Incorrect for this requirement. Entity creation precedes processor connection, and session queues reject messages lacking a `SessionId`. Why the keyed choice wins: Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = envelopeId` on every message, and consuming via `ServiceBusSessionProcessor` locks per-envelope FIFO order.
- **C:** Correct. `RequiresSession` can only be enabled when creating the entity, producers must populate `SessionId`, and consumers must use session-aware receivers/processors. In this scenario: Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = envelopeId` on every message, and consuming via `ServiceBusSessionProcessor` locks per-envelope FIFO order.
- **D:** Incorrect for this requirement. `RequiresSession` is immutable after creation, messages without `SessionId` are rejected on session queues, and non-session receivers fail. Why the keyed choice wins: Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = envelopeId` on every message, and consuming via `ServiceBusSessionProcessor` locks per-envelope FIFO order.

### Question 84 — D, E

Answers: Use Azure Service Bus Topics with `SqlRuleFilter` / `CorrelationRuleFilter` (`CorrelationRuleFilter` preferred for high throughput) and `SqlRuleAction` header stamping, inspecting `$DeadLetterQueue` (`SubQueue.DeadLetter`) after `MaxDeliveryCount` expires; Use `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false`, calling `CompleteMessageAsync` after commit, `AbandonMessageAsync` for transient retries, and `DeadLetterMessageAsync` on unrecoverable schema errors. Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route filtered copies and quarantine poison retries, while `PeekLock` (`AutoCompleteMessages = false`) protects in-flight durability. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route filtered copies and quarantine poison retries, while `PeekLock` (`AutoCompleteMessages = false`) protects in-flight durability.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route filtered copies and quarantine poison retries, while `PeekLock` (`AutoCompleteMessages = false`) protects in-flight durability.
- **C:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route filtered copies and quarantine poison retries, while `PeekLock` (`AutoCompleteMessages = false`) protects in-flight durability.
- **D:** Correct. `CorrelationRuleFilter` matches brokered/application properties in-memory far faster than SQL evaluation, while `MaxDeliveryCount` isolates poison messages in the sub-queue DLQ. In this scenario: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route filtered copies and quarantine poison retries, while `PeekLock` (`AutoCompleteMessages = false`) protects in-flight durability.
- **E:** Correct. `ReceiveAndDelete` loses messages if a worker crashes mid-processing; `PeekLock` retains broker durability until explicit settlement or lock expiry. In this scenario: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route filtered copies and quarantine poison retries, while `PeekLock` (`AutoCompleteMessages = false`) protects in-flight durability.

### Question 85 — A

Answer: Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering. Enabling `RequiresDuplicateDetection = true` (covering the retry window) alongside `RequiresSession = true` discards duplicate `MessageId` resends and preserves per-tenant FIFO order. Service Bus discards duplicate `MessageId` resends inside the history window and locks all messages sharing a `SessionId` to one active session receiver at a time. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Service Bus discards duplicate `MessageId` resends inside the history window and locks all messages sharing a `SessionId` to one active session receiver at a time. In this scenario: Enabling `RequiresDuplicateDetection = true` (covering the retry window) alongside `RequiresSession = true` discards duplicate `MessageId` resends and preserves per-tenant FIFO order.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Enabling `RequiresDuplicateDetection = true` (covering the retry window) alongside `RequiresSession = true` discards duplicate `MessageId` resends and preserves per-tenant FIFO order.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling `RequiresDuplicateDetection = true` (covering the retry window) alongside `RequiresSession = true` discards duplicate `MessageId` resends and preserves per-tenant FIFO order.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Enabling `RequiresDuplicateDetection = true` (covering the retry window) alongside `RequiresSession = true` discards duplicate `MessageId` resends and preserves per-tenant FIFO order.

### Question 86 — C

Answer: Call `long seq = await sender.ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` and persist `seq` to call `CancelScheduledMessageAsync(seq)` if the user cancels early. `ScheduleMessageAsync` returns a `sequenceNumber` (`seq`) that `CancelScheduledMessageAsync(seq)` uses to cancel pending delivery cleanly. Service Bus native scheduled messages stay invisible until `ScheduledEnqueueTime` and can be canceled cleanly via their broker sequence number. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `ScheduleMessageAsync` returns a `sequenceNumber` (`seq`) that `CancelScheduledMessageAsync(seq)` uses to cancel pending delivery cleanly.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `ScheduleMessageAsync` returns a `sequenceNumber` (`seq`) that `CancelScheduledMessageAsync(seq)` uses to cancel pending delivery cleanly.
- **C:** Correct. Service Bus native scheduled messages stay invisible until `ScheduledEnqueueTime` and can be canceled cleanly via their broker sequence number. In this scenario: `ScheduleMessageAsync` returns a `sequenceNumber` (`seq`) that `CancelScheduledMessageAsync(seq)` uses to cancel pending delivery cleanly.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `ScheduleMessageAsync` returns a `sequenceNumber` (`seq`) that `CancelScheduledMessageAsync(seq)` uses to cancel pending delivery cleanly.

### Question 87 — D

Answer: Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics. Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, whereas Service Bus queues cap out at 80 GB. Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub. Local study-map skill 5.8 (Implement Queue Workflows with Azure Queue Storage SDK, Visibility Leases, PopReceipts, and Poison Handling), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, whereas Service Bus queues cap out at 80 GB.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, whereas Service Bus queues cap out at 80 GB.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, whereas Service Bus queues cap out at 80 GB.
- **D:** Correct. Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub. In this scenario: Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, whereas Service Bus queues cap out at 80 GB.

### Question 88 — D

Answer: Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`. Leasing via `ReceiveMessagesAsync(visibilityTimeout)`, inspecting `DequeueCount`, and passing `MessageId` + `PopReceipt` to `UpdateMessageAsync` and `DeleteMessageAsync` manages leases and poison messages safely. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. Local study-map skill 5.8 (Implement Queue Workflows with Azure Queue Storage SDK, Visibility Leases, PopReceipts, and Poison Handling), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Leasing via `ReceiveMessagesAsync(visibilityTimeout)`, inspecting `DequeueCount`, and passing `MessageId` + `PopReceipt` to `UpdateMessageAsync` and `DeleteMessageAsync` manages leases and poison messages safely.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Leasing via `ReceiveMessagesAsync(visibilityTimeout)`, inspecting `DequeueCount`, and passing `MessageId` + `PopReceipt` to `UpdateMessageAsync` and `DeleteMessageAsync` manages leases and poison messages safely.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Leasing via `ReceiveMessagesAsync(visibilityTimeout)`, inspecting `DequeueCount`, and passing `MessageId` + `PopReceipt` to `UpdateMessageAsync` and `DeleteMessageAsync` manages leases and poison messages safely.
- **D:** Correct. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. In this scenario: Leasing via `ReceiveMessagesAsync(visibilityTimeout)`, inspecting `DequeueCount`, and passing `MessageId` + `PopReceipt` to `UpdateMessageAsync` and `DeleteMessageAsync` manages leases and poison messages safely.

### Question 89 — A

Answer: Specify a six-field NCRONTAB expression `{second} {minute} {hour} {day} {month} {day-of-week}` such as `"0 */15 9-17 * * 1-5"` on `[TimerTrigger]`. `"0 */15 9-17 * * 1-5"` includes the leading seconds field (`0`) and fires every 15 minutes across hours 9–17 Monday through Friday. Azure Functions `[TimerTrigger]` uses 6-field NCRONTAB (leading seconds field), unlike 5-field Unix cron. Local study-map skill 1.13 (Implement Function Triggers Using Cosmos DB/Blob Data Operations, NCRONTAB Timers, and Webhooks), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Azure Functions `[TimerTrigger]` uses 6-field NCRONTAB (leading seconds field), unlike 5-field Unix cron. In this scenario: `"0 */15 9-17 * * 1-5"` includes the leading seconds field (`0`) and fires every 15 minutes across hours 9–17 Monday through Friday.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` includes the leading seconds field (`0`) and fires every 15 minutes across hours 9–17 Monday through Friday.
- **C:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` includes the leading seconds field (`0`) and fires every 15 minutes across hours 9–17 Monday through Friday.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` includes the leading seconds field (`0`) and fires every 15 minutes across hours 9–17 Monday through Friday.

### Question 90 — D

Answer: In the .NET isolated worker model, return a custom POCO class uniting `[HttpResult]` (or `HttpResponseData`) with `[CosmosDBOutput]` / `[ServiceBusOutput]` properties. Returning a custom multi-output POCO class containing `[HttpResult]` (or `HttpResponseData`) alongside the declarative output-binding property emits both outputs cleanly. Isolated-worker C# functions cannot use `out` parameters for bindings; multi-output types return structured properties on a single return object. Local study-map skill 1.12 (Implement Azure Functions Input and Output Bindings (Isolated Worker & Declarative Bindings)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Returning a custom multi-output POCO class containing `[HttpResult]` (or `HttpResponseData`) alongside the declarative output-binding property emits both outputs cleanly.
- **B:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Returning a custom multi-output POCO class containing `[HttpResult]` (or `HttpResponseData`) alongside the declarative output-binding property emits both outputs cleanly.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Returning a custom multi-output POCO class containing `[HttpResult]` (or `HttpResponseData`) alongside the declarative output-binding property emits both outputs cleanly.
- **D:** Correct. Isolated-worker C# functions cannot use `out` parameters for bindings; multi-output types return structured properties on a single return object. In this scenario: Returning a custom multi-output POCO class containing `[HttpResult]` (or `HttpResponseData`) alongside the declarative output-binding property emits both outputs cleanly.

### Question 91 — C

Answer: Assign Storage Blob Data Contributor/Delegator RBAC to the identity → instantiate BlobServiceClient with DefaultAzureCredential → call GetUserDelegationKeyAsync for a bounded validity window → build BlobSasBuilder and sign with the user delegation key. Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) mints a User Delegation SAS. Entra RBAC must authorize delegation before BlobServiceClient requests a user delegation key, which then signs the BlobSasBuilder token without account keys. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. A SAS cannot be signed before obtaining the user delegation key, and shared account keys cannot mint Entra user delegation SAS tokens. Why the keyed choice wins: Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) mints a User Delegation SAS.
- **B:** Incorrect for this requirement. The client must authenticate with Microsoft Entra credentials first so it can request the delegation key that mints the SAS. Why the keyed choice wins: Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) mints a User Delegation SAS.
- **C:** Correct. Entra RBAC must authorize delegation before BlobServiceClient requests a user delegation key, which then signs the BlobSasBuilder token without account keys. In this scenario: Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) mints a User Delegation SAS.
- **D:** Incorrect for this requirement. GetUserDelegationKeyAsync requires an authenticated Entra client with RBAC already granted before the call executes. Why the keyed choice wins: Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) mints a User Delegation SAS.

### Question 92 — C

Answer: Use APIM `Revisions` to stage, test, and swap non-breaking internal changes safely on the same consumer URL (`;rev=2`), and use APIM `Versions` (path/header/query) when publishing breaking contract changes side-by-side for distinct consumer cohorts. APIM `Versions` publish breaking `/v1` and `/v2` contracts side by side, whereas APIM `Revisions` stage, test (`;rev=2`), and swap non-breaking edits transparently. Revisions let authors edit and flip the `current` implementation transparently; Versions expose distinct URLs/headers so legacy clients keep working. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: APIM `Versions` publish breaking `/v1` and `/v2` contracts side by side, whereas APIM `Revisions` stage, test (`;rev=2`), and swap non-breaking edits transparently.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: APIM `Versions` publish breaking `/v1` and `/v2` contracts side by side, whereas APIM `Revisions` stage, test (`;rev=2`), and swap non-breaking edits transparently.
- **C:** Correct. Revisions let authors edit and flip the `current` implementation transparently; Versions expose distinct URLs/headers so legacy clients keep working. In this scenario: APIM `Versions` publish breaking `/v1` and `/v2` contracts side by side, whereas APIM `Revisions` stage, test (`;rev=2`), and swap non-breaking edits transparently.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: APIM `Versions` publish breaking `/v1` and `/v2` contracts side by side, whereas APIM `Revisions` stage, test (`;rev=2`), and swap non-breaking edits transparently.

### Question 93 — B

Answer: Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`. Wrapping `<forward-request />` inside `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` in `<backend>` retries 503 blips, and `<set-header exists-action="delete" />` in `<outbound>` scrubs headers. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Wrapping `<forward-request />` inside `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` in `<backend>` retries 503 blips, and `<set-header exists-action="delete" />` in `<outbound>` scrubs headers.
- **B:** Correct. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. In this scenario: Wrapping `<forward-request />` inside `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` in `<backend>` retries 503 blips, and `<set-header exists-action="delete" />` in `<outbound>` scrubs headers.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Wrapping `<forward-request />` inside `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` in `<backend>` retries 503 blips, and `<set-header exists-action="delete" />` in `<outbound>` scrubs headers.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Wrapping `<forward-request />` inside `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` in `<backend>` retries 503 blips, and `<set-header exists-action="delete" />` in `<outbound>` scrubs headers.

### Question 94 — A

Answer: Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group. Application Insights Standard Availability Tests coupled with a `>= 2` failed-locations alert rule and Action Group validate TLS + HTTP health without single-POP false positives. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. In this scenario: Application Insights Standard Availability Tests coupled with a `>= 2` failed-locations alert rule and Action Group validate TLS + HTTP health without single-POP false positives.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Application Insights Standard Availability Tests coupled with a `>= 2` failed-locations alert rule and Action Group validate TLS + HTTP health without single-POP false positives.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Application Insights Standard Availability Tests coupled with a `>= 2` failed-locations alert rule and Action Group validate TLS + HTTP health without single-POP false positives.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Application Insights Standard Availability Tests coupled with a `>= 2` failed-locations alert rule and Action Group validate TLS + HTTP health without single-POP false positives.

### Question 95 — D

Answer: Deploy an Azure Container Apps Job (`triggerType: Event` or `Schedule`) with `replicaCompletionCount` and `parallelism` instead of an always-listening HTTP container app. Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` runs finite batch containers to completion cleanly. Container Apps Jobs execute finite scheduled or event-driven workloads to completion without exposing unused HTTP ingress. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` runs finite batch containers to completion cleanly.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` runs finite batch containers to completion cleanly.
- **C:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` runs finite batch containers to completion cleanly.
- **D:** Correct. Container Apps Jobs execute finite scheduled or event-driven workloads to completion without exposing unused HTTP ingress. In this scenario: Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` runs finite batch containers to completion cleanly.

### Question 96 — B

Answer: Run `az acr build --registry <acrName> --image app:{{.Run.ID}} .` to build and push the container image remotely using ACR Tasks without a local Docker daemon. ACR Tasks (`az acr build` or Git-commit-triggered ACR Tasks) stream the repository context to Azure and build/push container layers inside ACR. ACR Tasks tar and upload the build context to Azure, executing the Dockerfile build and pushing tagged layers directly inside ACR. Local study-map skill 1.2 (Publish Images, Run ACR Tasks, and Manage Auth/Purge in Azure Container Registry), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: ACR Tasks (`az acr build` or Git-commit-triggered ACR Tasks) stream the repository context to Azure and build/push container layers inside ACR.
- **B:** Correct. ACR Tasks tar and upload the build context to Azure, executing the Dockerfile build and pushing tagged layers directly inside ACR. In this scenario: ACR Tasks (`az acr build` or Git-commit-triggered ACR Tasks) stream the repository context to Azure and build/push container layers inside ACR.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: ACR Tasks (`az acr build` or Git-commit-triggered ACR Tasks) stream the repository context to Azure and build/push container layers inside ACR.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: ACR Tasks (`az acr build` or Git-commit-triggered ACR Tasks) stream the repository context to Azure and build/push container layers inside ACR.

### Question 97 — C

Answer: Add a `compositeIndexes` array matching the exact property sequence and sort directions (`ascending` / `descending`) in the container indexing policy JSON. Defining a `compositeIndexes` entry matching `/tenantId` (`ascending`) and `/recordedAt` (`descending`) enables multi-property `ORDER BY` execution directly from the index. Cosmos DB for NoSQL requires a matching composite index whenever a SQL query specifies `ORDER BY` across two or more properties. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Defining a `compositeIndexes` entry matching `/tenantId` (`ascending`) and `/recordedAt` (`descending`) enables multi-property `ORDER BY` execution directly from the index.
- **B:** Incorrect for this requirement. Excluding wildcard `/*` and indexing only queried filter paths dramatically cuts write Request Unit (RU) cost and index storage on write-heavy containers. Why the keyed choice wins: Defining a `compositeIndexes` entry matching `/tenantId` (`ascending`) and `/recordedAt` (`descending`) enables multi-property `ORDER BY` execution directly from the index.
- **C:** Correct. Cosmos DB for NoSQL requires a matching composite index whenever a SQL query specifies `ORDER BY` across two or more properties. In this scenario: Defining a `compositeIndexes` entry matching `/tenantId` (`ascending`) and `/recordedAt` (`descending`) enables multi-property `ORDER BY` execution directly from the index.
- **D:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Defining a `compositeIndexes` entry matching `/tenantId` (`ascending`) and `/recordedAt` (`descending`) enables multi-property `ORDER BY` execution directly from the index.

### Question 98 — B

Answer: Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation. Configuring `signInAudience` as `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit token validation enforces an allowlist on `tid` / issuer claims. Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Configuring `signInAudience` as `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit token validation enforces an allowlist on `tid` / issuer claims.
- **B:** Correct. Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`. In this scenario: Configuring `signInAudience` as `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit token validation enforces an allowlist on `tid` / issuer claims.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Configuring `signInAudience` as `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit token validation enforces an allowlist on `tid` / issuer claims.
- **D:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Configuring `signInAudience` as `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit token validation enforces an allowlist on `tid` / issuer claims.

### Question 99 — A

Answer: Register the middle-tier API scope and delegated Graph permissions in Entra ID → validate the incoming user token → call ConfidentialClientApplication.AcquireTokenOnBehalfOf(UserAssertion) → invoke Microsoft Graph with the exchanged token. Exposing the middle-tier API scope + delegated Graph permissions, validating the incoming user token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated user context. The middle-tier API must validate the caller token first and exchange it as a UserAssertion via ConfidentialClientApplication before calling Graph as that user. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. The middle-tier API must validate the caller token first and exchange it as a UserAssertion via ConfidentialClientApplication before calling Graph as that user. In this scenario: Exposing the middle-tier API scope + delegated Graph permissions, validating the incoming user token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated user context.
- **B:** Incorrect for this requirement. Graph rejects unauthenticated requests, and OBO cannot run before app registration and incoming token validation. Why the keyed choice wins: Exposing the middle-tier API scope + delegated Graph permissions, validating the incoming user token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated user context.
- **C:** Incorrect for this requirement. A token whose audience (`aud`) is the custom middle-tier API is rejected by Microsoft Graph; OBO exchange must occur first. Why the keyed choice wins: Exposing the middle-tier API scope + delegated Graph permissions, validating the incoming user token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated user context.
- **D:** Incorrect for this requirement. OBO requires a confidential client with a secret or certificate and `AcquireTokenOnBehalfOf`, not app-only `AcquireTokenForClient`. Why the keyed choice wins: Exposing the middle-tier API scope + delegated Graph permissions, validating the incoming user token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated user context.

### Question 100 — A

Answer: Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`. Requesting minimal delegated read scopes (`User.Read` / `User.ReadBasic.All`), projecting fields via `$select`, and paging `@odata.nextLink` with `PageIterator<T>` honors least privilege. Microsoft Graph enforces least-privilege consent scopes, trims payload size with `$select`, and paginates `@odata.nextLink` cleanly through `PageIterator<T>`. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Microsoft Graph enforces least-privilege consent scopes, trims payload size with `$select`, and paginates `@odata.nextLink` cleanly through `PageIterator<T>`. In this scenario: Requesting minimal delegated read scopes (`User.Read` / `User.ReadBasic.All`), projecting fields via `$select`, and paging `@odata.nextLink` with `PageIterator<T>` honors least privilege.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Requesting minimal delegated read scopes (`User.Read` / `User.ReadBasic.All`), projecting fields via `$select`, and paging `@odata.nextLink` with `PageIterator<T>` honors least privilege.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Requesting minimal delegated read scopes (`User.Read` / `User.ReadBasic.All`), projecting fields via `$select`, and paging `@odata.nextLink` with `PageIterator<T>` honors least privilege.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Requesting minimal delegated read scopes (`User.Read` / `User.ReadBasic.All`), projecting fields via `$select`, and paging `@odata.nextLink` with `PageIterator<T>` honors least privilege.
