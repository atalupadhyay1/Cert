# Microsoft Exam AZ-204: Developing Solutions for Microsoft Azure — Full-Length Mock Exam 3

Exam AZ-204 (FinTech Instant Payments, Ledger Reconciliation, and Fraud Webhooks) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Credential Lifecycle Notice:** Microsoft retired Exam AZ-204 (`Microsoft Certified: Azure Developer Associate`) on **July 31, 2026** and succeeded it with **Exam AI-200 (`Azure AI Cloud Developer Associate`)**. This practice bank preserves the final official January 14, 2026 AZ-204 skills-measured baseline for archival certification prep, enterprise Azure developer benchmarking, and core compute/storage/security/monitoring/integration mastery.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` SDK/CLI/XML/JSON/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area code dropdowns, split-pane tabbed case exhibits, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn documentation — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. A card-authorization team is authoring a production Dockerfile and build pipeline for a .NET 8 ISO-8583 switch and wants minimal runtime image surface area plus zero local `obj/` or `.git/` uploads during `az acr build`. Which two practices should they apply? Select two.

Domain: Develop Azure compute solutions

- A. Add `bin/`, `obj/`, `.git/`, and local `.env` files to `.dockerignore` before running `docker build` or `az acr build`
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Use a multi-stage Dockerfile building in `mcr.microsoft.com/dotnet/sdk:8.0` and copying published output into `mcr.microsoft.com/dotnet/aspnet:8.0` with a non-root `USER app`
- E. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 2. When Container Apps scales in a SWIFT wire-parser container, `IHostApplicationLifetime.ApplicationStopping` never fires because `/bin/sh -c` swallows `SIGTERM` before hard-killing after 30 seconds (` ____ `). Which Dockerfile change fixes signal delivery?

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Declare `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form so `SIGTERM` reaches the .NET host cleanly during container shutdown

### 3. Security compliance bans Docker Desktop daemons on FinTech CI runners, so pipelines must stream source code to Azure Container Registry to compile and tag images remotely (` ____ `). Which CLI command performs remote cloud builds?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- C. Run `az acr build --registry <acrName> --image app:{{.Run.ID}} .` to build and push the container image remotely using ACR Tasks without a local Docker daemon
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 4. Continuous builds of a fraud-scoring image generate 400 ephemeral tags per week in ACR, inflating storage charges. Which native ACR mechanism deletes tags older than 30 days and untagged manifests automatically?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Schedule an ACR Task executing `acr purge --filter "app:.*" --ago 30d --untagged` to clean stale untagged manifests and old tags automatically

### 5. An ACH file-encryption container on Linux Azure Container Instances needs a local HSM PKCS#11 proxy reachable over `127.0.0.1:8443` and a shared `emptyDir` ramdisk for transient scratch files. How should ACI be deployed?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Deploy the application container and Envoy/logging sidecar inside one multi-container ACI group sharing `localhost` network namespace and an `emptyDir` / Azure Files volume

### 6. Proposed solution: Pass a SWIFT alliance passphrase to Azure Container Instances via standard `--environment-variables` so operators can inspect it via `az container show`. Why does bank audit fail this, and what fixes it?

Domain: Develop Azure compute solutions

- A. Pass sensitive tokens via `--secure-environment-variables` (or a secret volume mount) so values never appear in Azure Portal properties or `az container show` plaintext output
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 7. A treasury Container Apps platform needs 80/20 blue-green HTTP traffic weights, Dapr pub/sub access restricted strictly to `ledger-writer` and `audit-sink`, and container environment secrets backed by Key Vault via Managed Identity. Which three Container Apps features satisfy these rules? Select three.

Domain: Develop Azure compute solutions

- A. Set `--revision-mode multiple` and apply `az containerapp ingress traffic set --revision-weight` to split live HTTP requests across named revisions
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Define a Container App secret using `keyVaultUrl` plus `identity` (managed identity resource ID or `system`) and map container environment variables via `secretRef`
- D. Register a Dapr state or pub/sub component in the Container Apps environment and restrict access via the component `scopes` array to specific `daprAppId` values
- E. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- F. Keep the default `--restart-policy Always` on a run-once batch container group

### 8. At 23:00 UTC every business day, 12 parallel worker shards must reconcile Nostro Nostro bank statements for nine minutes and terminate with zero listening HTTP ports. Which Azure Container Apps resource type matches this execution model?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Deploy an Azure Container Apps Job (`triggerType: Event` or `Schedule`) with `replicaCompletionCount` and `parallelism` instead of an always-listening HTTP container app
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision

### 9. A wealth-management portal running on App Service `Free (F1)` in dev is moving to production and requires custom TLS certificates, staging deployment slots, and scheduled morning autoscale. Which minimum App Service plan tier unlocks these features?

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Provision at least a `Standard` (`S1+`) or `Premium v3` (`P1v3+`) App Service plan to unlock deployment slots, custom domain SNI SSL, and metric/schedule autoscaling
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 10. A FinTech risk engine containerized on `mcr.microsoft.com/dotnet/aspnet:8.0` runs as non-root `app` user (` ____ `) and must expose port `8080` cleanly to Container Apps / App Service ingress. Which Dockerfile statements match .NET 8 defaults?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Set `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` inside the final `.NET 8` runtime stage and match `targetPort: 8080` on Container Apps ingress
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 11. Proposed solution: Rely on App Service Application Logging (Filesystem) to preserve 180 days of payment-gateway diagnostic traces for PCI forensic audits. Why does this fail, and what replaces it?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances

### 12. During a live sandbox test of a wire-transfer webhook on App Service, a developer needs real-time stdout traces in their local bash session (` ____ `). Which Azure CLI commands enable and stream the logs?

Domain: Develop Azure compute solutions

- A. Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 13. High-frequency FX quote requests hit a Windows App Service app continuously, causing traditional MSBuild file-by-file deployments to fail with locked DLL errors. Which deployment mode eliminates locked-file collisions and cold-copy skew?

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Set `WEBSITE_RUN_FROM_PACKAGE=1` and deploy with `az webapp deploy --type zip` so the app mounts the read-only ZIP package directly with atomic cold-start replacement
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 14. Before deploying a custom Alpine reverse-proxy container to App Service for Linux, air-gapped FinTech CI scripts must copy the signed upstream image into private ACR without a local Docker client (` ____ `). Which CLI command executes the server-side import?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Execute `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine`
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 15. An open-banking PSD2 API hosted on Azure App Service must enforce HTTPS-only with minimum TLS 1.2 plus mutual TLS client certificates, while binding a slot-pinned `LedgerDb` SQL connection string via CLI. Which two configurations apply? Select two.

Domain: Develop Azure compute solutions

- A. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- B. Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `httpsOnly: true`, set `minTlsVersion: "1.2"` (or `"1.3"`), and configure `clientCertEnabled` when mutual TLS client certificates are required
- E. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 16. A trading SPA at `https://desk.crestline.example` sends credentialed XHR requests (`credentials: "include"`) to an App Service API, and configuring wildcard `*` on CORS fails in browsers. How must App Service CORS be configured?

Domain: Develop Azure compute solutions

- A. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Configure App Service `CORS` with explicit origin URLs (and `supportCredentials` only without wildcard `*`) so App Service handles preflight `OPTIONS` requests
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 17. At market open (09:30 EST), a brokerage App Service plan scales out from 3 to 12 instances and then oscillates wildly between 6 and 12 instances every 120 seconds because scale-out and scale-in both sit near 65% CPU. How should autoscale be tuned?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Pair every scale-out metric rule (e.g., CPU > 75% for 10 min) with a conservative scale-in rule (e.g., CPU < 35%) and an explicit `coolDown` window plus safe default/max instance bounds
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`

### 18. An FX pricing engine precomputes yield curves on startup taking 25 seconds, and slot swaps currently route live trades before curve initialization completes. Which App Service settings hold swap completion until `/ready` returns HTTP `200`?

Domain: Develop Azure compute solutions

- A. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- B. Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 19. A card-issuing team on App Service Standard S3 wants `staging` builds to swap automatically into `Production` right after deployment finishes and custom warm-up probes succeed (`autoSwapSlotName`). Which deployment-slot capability accomplishes hands-free swaps?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps
- D. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision

### 20. A developer stores `CardNetworkEnv=Sandbox` on `staging` and `CardNetworkEnv=Live` on `Production`, yet after swapping slots `Production` suddenly carries `Sandbox`. Which flag was omitted on `CardNetworkEnv`?

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Mark environment-specific settings such as `PaymentWebhookUrl` and production connection strings as `slotSetting: true` (Deployment slot setting) before swapping slots
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 21. An anti-money-laundering (AML) graph-scoring Function App requires private VNet access to an internal database, zero cold-start latency on real-time wire checks, and 22-minute batch scoring runs. Which hosting plan supports all three?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- D. Host the Function App on `Flex Consumption` or `Elastic Premium (EP1+)` when VNet integration, longer execution timeouts beyond 10 minutes, or pre-warmed/always-ready instances are required

### 22. A payment-dispute Function App requires a 10-minute execution limit and must exclude `Request` and `Exception` items from Application Insights adaptive sampling (`host.json`: ` ____ `). Which JSON configuration belongs in `host.json`?

Domain: Develop Azure compute solutions

- A. Configure `"functionTimeout": "00:10:00"` and `"logging": { "applicationInsights": { "samplingSettings": { "isEnabled": true, "excludedTypes": "Request;Exception" } } }` inside `host.json`
- B. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`

### 23. A FinTech .NET 8 isolated-worker Function App has one HTTP endpoint that writes an audit record to Cosmos DB while returning HTTP 201, and a second function triggered automatically whenever ledger items change in Cosmos DB. Which two C# patterns implement this? Select two.

Domain: Develop Azure compute solutions

- A. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- B. Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. In the .NET isolated worker model, return a custom POCO class uniting `[HttpResult]` (or `HttpResponseData`) with `[CosmosDBOutput]` / `[ServiceBusOutput]` properties
- E. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 24. An `[EventHubTrigger]` fraud-enrichment Function occasionally hits transient downstream HTTP 503 blips and should retry five times with exponential backoff (`4s` to `60s`) before advancing checkpoints (` ____ `). Which attribute accomplishes this?

Domain: Develop Azure compute solutions

- A. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Apply `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` (or `[FixedDelayRetry]`) on the `[EventHubTrigger]` / `[TimerTrigger]` function
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 25. An FX settlement `[TimerTrigger(" ____ ")]` Function must execute every 15 minutes during weekday trading hours (`09:00–17:45 UTC`, Monday–Friday). Which six-field NCRONTAB expression sets this schedule?

Domain: Develop Azure compute solutions

- A. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Specify a six-field NCRONTAB expression `{second} {minute} {hour} {day} {month} {day-of-week}` such as `"0 */15 9-17 * * 1-5"` on `[TimerTrigger]`
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 26. A high-throughput wallet ledger on Cosmos DB for NoSQL requires connection-pooled singleton client reuse, single-field `/retryCount` increments without fetching 90 KB wallet documents, and HTTP 412 optimistic concurrency protection on balance replacements. Which three SDK practices deliver this? Select three.

Domain: Develop for Azure storage

- A. Pass `new ItemRequestOptions { IfMatchEtag = item.ETag }` on `ReplaceItemAsync` and catch `CosmosException` when `StatusCode == HttpStatusCode.PreconditionFailed` (412)
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `await container.PatchItemAsync<Order>(id, new PartitionKey(pk), new[] { PatchOperation.Increment("/retryCount", 1), PatchOperation.Set("/lastStatus", "Queued") })`
- D. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- E. Register `CosmosClient` as a process-wide singleton in dependency injection and choose a high-cardinality `PartitionKey` path (or up to 3-level `Hierarchical` subpartition paths) that distributes RU/s evenly
- F. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 27. A FinTech dispute query `SELECT * FROM c WHERE c.merchantId = @m ORDER BY c.riskScore DESC, c.createdUtc ASC` fails in Cosmos DB until an index change is deployed. What must be added to the indexing policy?

Domain: Develop for Azure storage

- A. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- B. Add a `compositeIndexes` array matching the exact property sequence and sort directions (`ascending` / `descending`) in the container indexing policy JSON
- C. Configure `"indexingMode": "consistent"` with `"includedPaths": [{"path": "/customerId/?"}, {"path": "/createdUtc/?"}]` and `"excludedPaths": [{"path": "/*"}]`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 28. A statement API paginates `/accountId` transactions in 100-item chunks (`FeedIterator<Order> iter = ____ `) and records RU charges from each `FeedResponse`. Which C# SDK v3 loop implements this cleanly?

Domain: Develop for Azure storage

- A. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- B. Use `FeedIterator<Order> iter = container.GetItemQueryIterator<Order>(queryDef, requestOptions: new QueryRequestOptions { PartitionKey = new PartitionKey(pk), MaxItemCount = 100 })` and loop `while (iter.HasMoreResults) { FeedResponse<Order> page = await iter.ReadNextAsync(); }`
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 29. When a cardholder freezes their debit card in a mobile app, subsequent API calls routed to any web worker must immediately reflect `"status": "Frozen"` for that user without paying `Strong` consistency read RU costs. How should Cosmos DB be used?

Domain: Develop for Azure storage

- A. Use `Session` consistency (the default) and propagate `x-ms-session-token` (`RequestOptions.SessionToken`) across client/middle-tier hops to guarantee monotonic read-your-own-writes at half the read RU cost of `Strong`
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 30. Cross-border treasury nodes in Frankfurt and Tokyo read a primary London Cosmos DB ledger and require globally ordered reads lagging London by no more than `K = 200` writes or `T = 5` seconds. Which consistency level satisfies this?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency

### 31. A real-time AML screening worker deployed across six replicas uses Cosmos DB Change Feed Processor v3 and must replay historical wire items from container inception on initial deployment (` ____ `). Which builder configuration enables full replay across balanced replicas?

Domain: Develop for Azure storage

- A. Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 32. Both a sanctions-screening worker and a general-ledger replicator must process every Cosmos DB wire event independently, and hard-deleted draft wires must also emit change notifications. Which two Change Feed patterns are required? Select two.

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Use Change Feed `AllVersionsAndDeletes` mode (or soft-delete flag items with short TTL in `LatestVersion` mode) because default `LatestVersion` change feed omits hard-deleted items
- D. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- E. Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay

### 33. One-time 3DS payment challenge documents in Cosmos DB include `"ttl": 180`, yet expired challenges remain queryable forever because container `DefaultTimeToLive` was left `null`. What container setting activates per-item `ttl` without expiring permanent documents?

Domain: Develop for Azure storage

- A. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Enable container `DefaultTimeToLive = -1` (or positive seconds) and set item `ttl = 600` so Cosmos DB purges expired items automatically using background RU capacity

### 34. A clearinghouse stores 40 million ISO-20022 XML blobs across containers and needs instant server-side lookup of `@container = 'docs' AND status = 'pending'` (`await serviceClient. ____ `). Which Blob Storage feature supports indexed cross-container queries?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`)
- C. Attach searchable key-value `Tags` (`SetTagsAsync` / `BlobUploadOptions.Tags`) and query across containers with `FindBlobsByTagsAsync("@container = 'docs' AND status = 'pending'")`
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 35. A statement-archiver uploads PDF blobs and must set standard `Content-Type` / `Cache-Control` HTTP headers alongside custom `settlement_batch` user metadata (` ____ `). Which two `BlobClient` methods distinguish system properties from metadata?

Domain: Develop for Azure storage

- A. Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`)
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 36. Proposed solution: Let six concurrent reconciliation pods overwrite `ach-cutoff-checkpoint.json` in Blob Storage without request conditions, assuming last-writer-wins is safe. Why does this corrupt state, and what prevents concurrent writes?

Domain: Develop for Azure storage

- A. Use `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` (15–60 seconds or `-1` infinite) and pass `LeaseId` inside `BlobRequestConditions` on subsequent writes/deletes
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 37. At quarter-end, a vault service replicates 6 TB of check-image archives into an Escrowed storage account (`await destBlob. ____ `) without streaming bytes through worker pods. Which SDK method executes server-side copy?

Domain: Develop for Azure storage

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Invoke `BlobClient.StartCopyFromUriAsync(sourceSasUri)` to trigger asynchronous server-side blob copy and inspect `CopyStatus` without streaming bytes through the client VM

### 38. A wire-export API builds a 15-minute HTTPS-only read link restricted to single blob `exports/manifest.csv` (`new BlobSasBuilder { ____ }`). Which `BlobSasBuilder` configuration enforces least privilege?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 39. Check images in Blob Storage must move to `Cool` after 30 days and `Archive` after 90 days automatically, while central-bank audit subpoenas on <10 GB archived files require restoration within an hour. Which two features address both needs? Select two.

Domain: Develop for Azure storage

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`)
- D. Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob)
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 40. A dispute analyst requests a 2023 wire-transfer bundle currently stored in the offline `Archive` tier in Azure Blob Storage. Which ordered sequence restores and downloads the bundle cleanly?

Domain: Develop for Azure storage

- A. Download the archived blob stream directly → call SetAccessTier to Hot → poll ArchiveStatus → verify the Archive tier
- B. Verify the blob is currently in the Archive access tier → call SetAccessTier (or CopyBlob) targeting Hot or Cool with Standard or High rehydrate priority → poll ArchiveStatus until rehydration completes and tier updates → download the blob content
- C. Set blob metadata `tier=Hot` → download the blob immediately → call SetAccessTier to Archive → poll ArchiveStatus
- D. Acquire an infinite blob lease → delete the blob snapshot → download the archived blob directly → call SetAccessTier

### 41. A treasury trader desktop app built on WPF authenticates against Microsoft Entra ID without client secrets and refreshes FX API tokens silently from cache across an 8-hour trading session. Which two MSAL patterns must be implemented? Select two.

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- C. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- D. Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 42. An overnight Fedwire reconciliation daemon runs unattended with an X.509 certificate and acquires app-only tokens for `api://ledger/.default` (` ____ `). Which MSAL client class and method apply?

Domain: Implement Azure security

- A. Use `ConfidentialClientApplicationBuilder` authenticated with a client certificate (or workload identity assertion) calling `AcquireTokenForClient(new[] { "api://.../.default" })` for headless background daemons
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps

### 43. A relationship manager signed into a commercial-loan SPA calls a middle-tier ASP.NET Core Loan API, which must read the manager's Outlook contacts via Microsoft Graph using delegated permissions. Which sequence completes the OBO flow?

Domain: Implement Azure security

- A. Call Microsoft Graph anonymously → call AcquireTokenOnBehalfOf → validate the incoming token → expose the API scope
- B. Register the middle-tier API scope and delegated Graph permissions in Entra ID → validate the incoming user token → call ConfidentialClientApplication.AcquireTokenOnBehalfOf(UserAssertion) → invoke Microsoft Graph with the exchanged token
- C. Use PublicClientApplication without client credentials → call AcquireTokenForClient → pass UserAssertion → register delegated permissions
- D. Forward the front-end SPA access token directly to Microsoft Graph → validate the incoming token → register the API scope → call AcquireTokenOnBehalfOf

### 44. A high-value wire-approval endpoint (`[Authorize(Roles = "WireApprover")]`) must accept tokens from both human treasury officers and an automated sweep service principal. How must `WireApprover` be configured in Entra ID?

Domain: Implement Azure security

- A. Declare `appRoles` with `allowedMemberTypes: ["User", "Application"]` in the Entra app registration manifest and validate the `roles` claim (`[Authorize(Roles = "...")]`) in the web API
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 45. A corporate-treasury SaaS app lets finance teams from 200 enterprise customer Entra tenants sign in while rejecting personal Microsoft accounts and unlisted `tid` values. Which configuration enforces this boundary?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- C. Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 46. Programmatic partner webhooks calling an App Service API protected by Microsoft Entra Easy Auth fail when expired tokens return HTTP `302` redirects to an interactive login page. Which setting fixes this?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)

### 47. Proposed solution: Keep storage account `allowSharedKeyAccess: true` solely so a settlement microservice can sign 10-minute Blob download SAS links with `accountKey1`. Which change lets security disable Shared Key access completely?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Mint a short-lived HTTPS-only (`SasProtocol.HttpsOnly`) User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` instead of Account or Service SAS signed with storage account keys
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 48. A partner FinTech bank receives a Service SAS for container `iso-drop`, and operations must be able to revoke that single partner's SAS immediately without rotating storage account keys. How should the Service SAS be created?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Bind a Service SAS to a container/queue/table Stored Access Policy (`SignedIdentifier`, omitting inline start/expiry/permissions) so compromised tokens can be revoked instantly by modifying or deleting the policy

### 49. A brokerage tax-statement API mints a 15-minute HTTPS-only read token restricted strictly to blob `exports/manifest.csv` (`new BlobSasBuilder { ____ }`) signed with a user delegation key. Which builder setup enforces single-blob read scope?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`

### 50. A compliance attestation portal queries 18,000 bank employees via Microsoft Graph and fetches manager details in groups of 20 without triggering HTTP `429` throttling or over-privileged directory scopes. Which two Graph SDK practices apply? Select two.

Domain: Implement Azure security

- A. Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- E. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 51. Using Microsoft Graph .NET SDK v5, an audit job lists active bank employees (`accountEnabled eq true`) fetching strictly `id`, `displayName`, and `mail` (`await graphClient.Users.GetAsync( ____ )`). Which configuration completes the query?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Call `await graphClient.Users.GetAsync(rc => { rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }; rc.QueryParameters.Filter = "accountEnabled eq true"; })`

### 52. Inside a middle-tier wealth-advisory API controller holding an incoming Entra user bearer token, which MSAL call acquires a delegated downstream Microsoft Graph token (` ____ `)?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Call `await confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` inside the middle-tier API

### 53. A central clearing vault manages SQL connection secrets, HSM-backed RSA signing keys, and mTLS client certificates in Azure Key Vault while enforcing mandatory 90-day protection against permanent key purge. Which two Key Vault practices are required? Select two.

Domain: Implement Azure security

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Enable Soft Delete (mandatory on new vaults, 7–90 days) plus Purge Protection on Azure Key Vault so neither accidental deletion nor malicious principals can permanently destroy keys before retention expires
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Use `SecretClient` (`Azure.Security.KeyVault.Secrets`) for connection strings/tokens, `KeyClient` / `CryptographyClient` (`Azure.Security.KeyVault.Keys`) for RSA/EC wrap-unwrap-sign, and `CertificateClient` for X.509 lifecycle

### 54. A card-vault worker encrypts bulk PAN files locally with a 256-bit AES data key (`dekBytes`) and wraps `dekBytes` using a Key Vault RSA key (` ____ `). Which SDK client and method perform envelope key wrapping?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Instantiate `new CryptographyClient(keyVaultKey.Id, new DefaultAzureCredential())` and invoke `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync(...)`

### 55. A FinTech webhook app on Azure App Service reads `Environment.GetEnvironmentVariable("HmacWebhookSecret")` and wants rotated Key Vault secrets injected without SDK code changes (` ____ `). Which App Service setting syntax accomplishes this?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Configure App Service / Functions application settings using `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` (omitting secret version) paired with `Key Vault Secrets User` on the app Managed Identity
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 56. FinTech developers run a ledger worker locally via `dotnet run` (authenticated with Azure CLI) and deploy the identical container to Azure Container Apps with Managed Identity. Which `Azure.Identity` credential class supports both seamlessly?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- C. Instantiate `new DefaultAzureCredential()` (or explicit `ManagedIdentityCredential(clientId)` for user-assigned identities in production) so identical code authenticates via Azure CLI / Visual Studio locally and Managed Identity in Azure
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 57. Payment SREs diagnosing sporadic wire timeouts in Workspace-based Application Insights need 5-minute KQL buckets of failure counts + p95 latency and an inner join linking HTTP 500 `AppRequests` to failing `AppDependencies`. Which two KQL queries provide both views? Select two.

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Run `AppRequests | where TimeGenerated > ago(1h) | summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)`
- E. Run `AppRequests | where ResultCode == "500" | join kind=inner (AppDependencies | where Success == false) on OperationId | project TimeGenerated, Name, Target, DependencyType, ResultCode1`

### 58. An end-of-day ACH NACHA generator runs for 9 seconds inside a Container Apps Job and exits `Main()` immediately, causing final `TrackMetric` items to vanish before transmission. What shutdown step fixes this?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 59. Inside a .NET 8 instant-payment router using `UseAzureMonitor()`, engineers want custom timed child spans around sanctions-check logic (`using var span = ____ `) visible in Application Insights Transaction Search. How should they code this?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`

### 60. Pillar Remit wants 5-minute synthetic probes from five continents checking TLS certificate expiry and HTTP 200 status on `https://api.pillarremit.example`, paging SREs only when at least two locations fail simultaneously. What should be configured?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 61. Instant-payment volume surges 10x on payday Fridays and drops overnight, making static latency/error alerts noisy, and alerts must invoke an automated incident webhook. Which Azure Monitor alert configuration fits?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Create an Azure Monitor Metric Alert (Dynamic Thresholds or static p95 latency/5xx count) or Scheduled Query (KQL) Alert targeting an Action Group configured with webhook / Azure Function / email-SMS receivers
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 62. An internal Fedwire connector sits inside an isolated private VNet unreachable from public Azure Monitor POPs, yet compliance requires availability test results inside Application Insights Availability charts. How can synthetic availability be recorded?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group

### 63. A FinTech ledger team modernizing telemetry on .NET 8 needs connection-string OpenTelemetry auto-collection, consistent multi-service trace sampling that preserves full `operation_Id` call trees, and unsampled Live Metrics during releases. Which two choices meet all three goals? Select two.

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- E. Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments

### 64. Proposed solution: Disable all sampling on a 12,000 RPS payment gateway because engineers fear adaptive sampling will blind Live Metrics Stream during production rollouts. Is that fear accurate, and how does sampling interact with Live Metrics?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently

### 65. A global custodian bank operates an on-premises Zurich vault datacenter where local settlement microservices must route API calls locally inside the vault LAN while syncing API policies from Azure over outbound HTTPS. Which APIM architecture fits?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Select `Developer` (non-SLA) or `Premium` / `Standard v2` for VNet integration, and deploy the containerized APIM Self-Hosted Gateway (`mcr.microsoft.com/azure-api-management/gateway`) for hybrid on-premises/multi-cloud local traffic routing
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 66. An APIM gateway fronting an internal Entra-protected wire-initiation service must acquire and attach backend bearer tokens automatically via Managed Identity (`<inbound> ____ </inbound>`). Which XML policy snippet completes `<inbound>`?

Domain: Connect to and consume Azure services and third-party services

- A. Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`
- B. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 67. A payment API team stages a non-breaking OpenAPI header addition on `;rev=2` before making it current, while maintaining breaking `/v1/transfers` and `/v2/transfers` contracts in parallel for corporate ERPs. Which APIM constructs match each scenario?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Use APIM `Revisions` to stage, test, and swap non-breaking internal changes safely on the same consumer URL (`;rev=2`), and use APIM `Versions` (path/header/query) when publishing breaking contract changes side-by-side for distinct consumer cohorts
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 68. Partner neobank iOS engineers need mocked HTTP 200 FX quote JSON from APIM before the pricing engine launches, and later `/quotes/{id}` must rewrite cleanly to `/internal/v2/orders/{orderId}` (` ____ `). Which APIM policies handle both needs?

Domain: Connect to and consume Azure services and third-party services

- A. Use `<mock-response status-code="200" content-type="application/json" />` during frontend parallel development, or `<rewrite-uri template="/internal/v2/orders/{orderId}" />` with `<set-backend-service base-url="..." />` in `<inbound>`
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 69. When importing an HTTP-triggered Azure Function into APIM, the Function requires `x-functions-key` from APIM's Named Values rather than public anonymous calls or the `_master` admin key (`[HttpTrigger( ____ )]`). Which `AuthorizationLevel` is configured on the Function?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 70. A FinTech security engineer is migrating APIM backend authentication from static shared API keys to Managed Identity Entra tokens against an internal ledger API. Which ordered steps complete the rollout?

Domain: Connect to and consume Azure services and third-party services

- A. Hardcode a 2-year client secret inside `<set-header>` XML → disable Managed Identity → grant RBAC → inspect trace
- B. Enable Managed Identity on the APIM instance → grant that identity RBAC or app-role access on the target backend/Key Vault → add authentication-managed-identity in APIM policy XML → test backend calls and inspect APIM trace headers
- C. Add authentication-managed-identity policy → test backend invocation → enable Managed Identity on APIM → grant RBAC on the target
- D. Grant RBAC to the developer laptop user → add `<validate-jwt>` in `<outbound>` → enable APIM Managed Identity → test backend

### 71. Open-banking third-party providers (TPPs) calling Pillar's APIM edge must pass Product Subscription Keys, present an eIDAS mTLS client certificate thumbprint, and carry an Entra JWT with required role claims. Which two APIM `<inbound>` configurations enforce all three? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`
- D. Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 72. An APIM payment-initiation endpoint must return `401` at the edge whenever a caller's JWT lacks audience `api://orders` or the `Orders.Write` role claim (`<inbound> ____ </inbound>`). Which XML policy enforces this?

Domain: Connect to and consume Azure services and third-party services

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- C. Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 73. FX reference tables exposed through Pillar's gateway must throttle aggressive callers per minute while enforcing monthly billing ceilings without losing parent security rules, cache translated payloads per client locale, and mask transient upstream 500s while scrubbing server version banners. Which three gateway policy configurations achieve this? Select three.

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`
- F. Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`

### 74. Country corridor fee tables on `GET /corridors` rarely change, so a FinTech developer adds `<cache-lookup>` in `<inbound>` without modifying `<outbound>`, and backend hits stay at 100%. What policy change actually populates the cache?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 75. External PCI scanners detect `X-AspNet-Version` headers on responses through APIM, and brief single-pod HTTP 503 restarts surface directly to card networks. Where should retry and header-deletion XML policies be placed?

Domain: Connect to and consume Azure services and third-party services

- A. Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 76. Crestline operates a treasury webhook hub serving 2,200 correspondent banks where each bank must be restricted via Azure RBAC to its own dedicated event topic behind one publish endpoint. Which Event Grid resource fits?

Domain: Connect to and consume Azure services and third-party services

- A. Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 77. A white-label banking-as-a-service platform routes card-swipe webhook notifications to 1,800 fintech tenants under one Event Grid publish endpoint with per-tenant RBAC, `CloudEvents v1.0` filters, and 24-hour Blob dead-lettering. Which two Event Grid features fit? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization
- D. Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL
- E. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 78. Deploying a Bicep template that subscribes a custom fraud ASP.NET Core webhook to Event Grid fails with `Webhook validation handshake failed` (` ____ `). What logic must the webhook controller implement?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`
- D. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors

### 79. A fraud webhook only cares about `CardDeclined` events where `amountUsd > 5000` under `/corridor/swift/`, and if the partner endpoint stays down for 12 hours, undelivered events must be auditable in Blob Storage. How should the Event Grid subscription be configured?

Domain: Connect to and consume Azure services and third-party services

- A. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 80. Real-time card-authorization telemetry arrives in Azure Event Hubs at 80,000 events/sec, and a C# fraud scorer must consume partitions with durable Blob Storage checkpoints. Which sequence implements the consumer?

Domain: Connect to and consume Azure services and third-party services

- A. Call StartProcessingAsync → register ProcessEventAsync without ProcessErrorAsync → create the Event Hub → create the Blob container
- B. Instantiate EventHubProducerClient → call UpdateCheckpointAsync on the producer → register ProcessEventAsync → call StopProcessingAsync first
- C. Point all five independent microservices at `$Default` with one shared Blob prefix → call StopProcessingAsync → call StartProcessingAsync → skip UpdateCheckpointAsync
- D. Create the Event Hub, consumer group, and Blob checkpoint container → instantiate BlobContainerClient and EventProcessorClient → register ProcessEventAsync (calling UpdateCheckpointAsync) and ProcessErrorAsync → call StartProcessingAsync before StopProcessingAsync

### 81. Four independent FinTech services (velocity scoring, merchant analytics, SIEM export, and ML feature store) read a 90,000-msg/sec market-tick stream while compliance archives raw Avro/Parquet batches to ADLS Gen2 with zero custom code. Which architecture fits?

Domain: Connect to and consume Azure services and third-party services

- A. Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors

### 82. After scaling out an `EventProcessorClient` market-data deployment from 4 to 8 replicas, rebalanced partitions replay hours of already-scored trades (`await eventArgs. ____ `). Which missing call prevents duplicate replay?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Host `EventProcessorClient` backed by `BlobContainerClient` and call `await eventArgs.UpdateCheckpointAsync()` after idempotent batch persistence so partition leases resume cleanly after rebalancing
- D. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors

### 83. Ledger adjustments for a single `ibanAccount` must execute strictly in FIFO order across 20 C# worker pods without blocking adjustments for other IBAN accounts. Which ordered sequence configures Azure Service Bus?

Domain: Connect to and consume Azure services and third-party services

- A. Create the queue or subscription with RequiresSession = true at creation time → send ServiceBusMessage instances setting a non-empty SessionId → create a ServiceBusSessionProcessor (or AcceptNextSessionAsync receiver) → process messages in order and complete/renew session locks
- B. Create ServiceBusSessionProcessor → send messages with null SessionId → create the queue → complete messages before receiving
- C. Create a standard queue with RequiresSession = false → send messages without SessionId → toggle RequiresSession = true later → read with standard ServiceBusReceiver
- D. Send messages to Queue Storage with SessionId → attach ServiceBusSessionProcessor → toggle FIFO → complete locks

### 84. Settled FX trades published to Azure Service Bus must fan out by `Currency = 'JPY'` using fast header filters, survive mid-transaction pod crashes without data loss, and quarantine corrupt payloads in `$DeadLetterQueue`. Which two Service Bus practices apply? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false`, calling `CompleteMessageAsync` after commit, `AbandonMessageAsync` for transient retries, and `DeadLetterMessageAsync` on unrecoverable schema errors
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- E. Use Azure Service Bus Topics with `SqlRuleFilter` / `CorrelationRuleFilter` (`CorrelationRuleFilter` preferred for high throughput) and `SqlRuleAction` header stamping, inspecting `$DeadLetterQueue` (`SubQueue.DeadLetter`) after `MaxDeliveryCount` expires

### 85. ATM cash-dispense retries sent over cellular links occasionally submit the identical `MessageId` twice within 5 minutes, and both ATM sequence order and idempotent deduplication are mandatory on the Service Bus queue. Which two entity flags solve this?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 86. When a user initiates a cooling-off wire transfer with a 30-minute cancellation window, the API enqueues a delayed Service Bus message (`long seq = await sender. ____ `) that can be aborted if the user cancels within 30 minutes. Which SDK call pair works?

Domain: Connect to and consume Azure services and third-party services

- A. Call `long seq = await sender.ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` and persist `seq` to call `CancelScheduledMessageAsync(seq)` if the user cancels early
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 87. A FinTech back-office team needs a low-cost queue storing 150 TB of 4 KB historical statement-rendering pointers with visibility-timeout leases and no requirement for sessions or pub/sub topics. Which Azure queue service satisfies the 150 TB backlog?

Domain: Connect to and consume Azure services and third-party services

- A. Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 88. Proposed solution: Use `QueueClient.PeekMessagesAsync()` in statement-rendering workers to lease jobs invisibly for 2 minutes and delete completed jobs. Why does this fail, and what replaces it?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

---

## Case study — Bramble Insure

Bramble Insure processes roadside-claim photo uploads on Azure Functions triggered by Event Grid BlobCreated events rather than polling Blob Storage, cutting idle storage-transaction bills. Every claim workflow correlates front-end SPA telemetry, APIM gateway requests, Function executions, and SQL/Cosmos dependencies inside a single Application Insights transaction view.

The next 3 questions refer to **Bramble Insure**. Read the scenario brief once, then answer each item independently.

### 89. Roadside-claim photos land in Blob Storage unevenly throughout the week, and Bramble wants near-instant `[BlobTrigger]` activation without paying continuous container-log polling charges (`[BlobTrigger(..., ____ )]`). Which trigger option achieves this?

Domain: Develop Azure compute solutions

- A. Configure `[BlobTrigger(..., Source = BlobTriggerSource.EventGrid)]` with an Event Grid system topic subscription instead of default container-log polling
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 90. Claims adjusters report slow claim submissions spanning the SPA, APIM gateway, Azure Function, and Cosmos DB, and engineers need one correlation key in KQL to stitch every hop together. Which field links these tables?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Query Workspace-based Application Insights (`AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces` or classic `requests`/`dependencies`/`exceptions`) joining on `OperationId` (`operation_Id`) to reconstruct end-to-end distributed transactions

### 91. Bramble is onboarding a new subrogation .NET 8 microservice to Workspace-based Application Insights using OpenTelemetry and automated failure alerting. Which rollout sequence is correct?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Create a deprecated Classic InstrumentationKey-only resource → hardcode ikey without SDK → fire Action Group → provision Log Analytics later
- B. Create a KQL alert rule on an empty subscription → uninstall OpenTelemetry packages → copy connection string → provision Application Insights
- C. Set Adaptive Sampling to 0% maxTelemetryItemsPerSecond → deploy without connection string → query traces → attach Action Group
- D. Provision Workspace-based Application Insights and copy APPLICATIONINSIGHTS_CONNECTION_STRING → configure UseAzureMonitor() OpenTelemetry distro at startup → verify requests/dependencies in Logs → create a KQL or metric alert linked to an Action Group

---

## Case study — Crestline Clearing

Crestline Clearing runs containerized settlement workers in Azure Container Apps connected to an Azure Service Bus Premium namespace and an Azure Container Registry with admin user disabled. Settlement batches arrive on a Service Bus queue; KEDA must scale worker replicas from 0 to 30 based on active queue depth using a user-assigned managed identity, with zero credentials stored in YAML manifests.

The next 3 questions refer to **Crestline Clearing**. Read the scenario brief once, then answer each item independently.

### 92. Crestline's settlement worker Container App must pull images from an Azure Container Registry that has admin user disabled, with zero passwords in Bicep/YAML manifests. Which ordered steps configure passwordless deployment?

Domain: Develop Azure compute solutions

- A. Grant AcrPull on the registry → create the container app → create the user-assigned identity → run az acr build
- B. Build and push the image to ACR with az acr build → create a user-assigned managed identity and grant AcrPull on the registry → create the Container Apps environment → create the container app referencing the identity and registry server
- C. Create the Container Apps environment → create the container app → enable ACR admin passwords → revoke AcrPull
- D. Create the container app referencing the registry → build and push the image with az acr build → create the Container Apps environment → grant AcrPull

### 93. Crestline wants settlement worker replicas to scale down to `0` overnight when the Service Bus queue is empty and scale out up to `30` replicas on active backlog without connection-string secrets. How should the KEDA rule be authored?

Domain: Develop Azure compute solutions

- A. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- B. Configure a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0` and Managed Identity (`identity` property) so replicas scale to zero when idle and wake on queue depth
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 94. Crestline attaches separate user-assigned identities for ACR image pulls and Service Bus consumption, and `new DefaultAzureCredential()` in C# fails to disambiguate them (` ____ `). Which option fixes token acquisition?

Domain: Implement Azure security

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Instantiate `new DefaultAzureCredential(new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId })` (or set `AZURE_CLIENT_ID`)
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

---

## Case study — Halcyon Custody

Halcyon Custody stores immutable trade confirmations in Azure Blob Storage with versioning and legal hold policies enabled, and stores account ledger entries in Cosmos DB within single-partition batches. When a custodian updates multiple ledger lines for the same `/accountNumber`, either every write must commit atomically or the entire batch must roll back without partial state.

The next 3 questions refer to **Halcyon Custody**. Read the scenario brief once, then answer each item independently.

### 95. SEC Rule 17a-4 auditors require Halcyon's trade-confirmation PDFs in Blob Storage to enforce non-erasable WORM protection and suspend expiration whenever a regulatory investigation opens. Which Blob Storage controls meet both rules?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 96. Updating a custody settlement posts a debit entry, a fee entry, and a balance summary sharing `/accountNumber` in Cosmos DB (`container. ____ `), and partial writes are unacceptable. Which SDK feature guarantees atomic execution?

Domain: Develop for Azure storage

- A. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- B. Use `container.CreateTransactionalBatch(new PartitionKey(pkValue))` to group multiple create/replace/upsert/delete operations atomically within the same logical partition
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 97. Whenever an amended trade confirmation overwrites an existing blob key, Halcyon must retain every prior state automatically under an immutable `VersionId` without extra client SDK calls. What must be enabled on the storage account?

Domain: Develop for Azure storage

- A. Call `await blobClient.CreateSnapshotAsync()` for explicit point-in-time read-only checkpoints or enable account-level Blob Versioning so every `UploadAsync` overwrite retains an immutable `VersionId`
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

---

## Case study — Pillar Remit

Pillar Remit exposes a cross-border FX quote API via Azure API Management. Free-tier fintech sandboxes must be capped at 60 calls per minute per subscription (returning HTTP 429) and 5,000 calls per month (returning HTTP 403), while enterprise corridors call an App Configuration store using dynamic sentinel-key refresh and feature flags gated by rollout percentage.

The next 3 questions refer to **Pillar Remit**. Read the scenario brief once, then answer each item independently.

### 98. Free-tier FX sandbox callers on Azure API Management must receive HTTP `429` above 60 calls/minute and HTTP `403` above 5,000 calls/month per subscription while retaining parent `<inbound>` policies. Which XML policy block satisfies this?

Domain: Connect to and consume Azure services and third-party services

- A. Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 99. Enterprise remittance corridors read FX spread settings and Key Vault secret references from Azure App Configuration with dynamic sentinel-key refresh. Which sequence configures this architecture end to end?

Domain: Implement Azure security

- A. Grant only App Configuration Data Reader (no Key Vault role) → invoke UseAzureAppConfiguration → add sentinel key → register AddAzureAppConfiguration
- B. Add Key Vault references → wire ConfigureRefresh without UseAzureAppConfiguration middleware → expect background timer push updates → grant RBAC later
- C. Copy plaintext Key Vault secret values into appsettings.json → commit to Git → wire ConfigureRefresh → enable Managed Identity
- D. Enable Managed Identity with App Configuration Data Reader + Key Vault Secrets User → add Key Vault references and a sentinel key → wire AddAzureAppConfiguration with ConfigureKeyVault and ConfigureRefresh → invoke UseAzureAppConfiguration middleware

### 100. Pillar rolls out a new instant-SEPA corridor to 20% of requests via `.appconfig.featureflag/*` and updates three fee-tier keys simultaneously without mid-edit partial reloads. Which App Configuration setup accomplishes both?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Store environment-labeled settings and `.appconfig.featureflag/*` entries in Azure App Configuration, register `AddAzureAppConfiguration` + `AddFeatureManagement`, and watch a single `Sentinel` key with `refreshAll: true`
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

---

## Answer key and explanations

### Question 1 — A, D

Answers: Use a multi-stage Dockerfile building in `mcr.microsoft.com/dotnet/sdk:8.0` and copying published output into `mcr.microsoft.com/dotnet/aspnet:8.0` with a non-root `USER app`; Add `bin/`, `obj/`, `.git/`, and local `.env` files to `.dockerignore` before running `docker build` or `az acr build`. A multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root build strips SDK tools from production layers, while `.dockerignore` blocks local build folders and secrets from uploading. Local study-map skill 1.1 (Create and Manage Container Images and Multi-Stage Dockerfiles), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. `.dockerignore` prevents streaming gigabytes of local build artifacts and stray secrets into the build context. In this scenario: A multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root build strips SDK tools from production layers, while `.dockerignore` blocks local build folders and secrets from uploading.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: A multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root build strips SDK tools from production layers, while `.dockerignore` blocks local build folders and secrets from uploading.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: A multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root build strips SDK tools from production layers, while `.dockerignore` blocks local build folders and secrets from uploading.
- **D:** Correct. Multi-stage Docker builds exclude compiler SDK layers and source files from the final runtime image, shrinking image size and attack surface. In this scenario: A multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root build strips SDK tools from production layers, while `.dockerignore` blocks local build folders and secrets from uploading.
- **E:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: A multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root build strips SDK tools from production layers, while `.dockerignore` blocks local build folders and secrets from uploading.

### Question 2 — D

Answer: Declare `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form so `SIGTERM` reaches the .NET host cleanly during container shutdown. Declaring `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form launches `dotnet` directly as PID 1 so `SIGTERM` triggers graceful host shutdown. Exec-form `ENTRYPOINT` runs the process as PID 1 without an intermediate `/bin/sh -c` wrapper that swallows POSIX termination signals. Local study-map skill 1.1 (Create and Manage Container Images and Multi-Stage Dockerfiles), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Declaring `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form launches `dotnet` directly as PID 1 so `SIGTERM` triggers graceful host shutdown.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Declaring `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form launches `dotnet` directly as PID 1 so `SIGTERM` triggers graceful host shutdown.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Declaring `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form launches `dotnet` directly as PID 1 so `SIGTERM` triggers graceful host shutdown.
- **D:** Correct. Exec-form `ENTRYPOINT` runs the process as PID 1 without an intermediate `/bin/sh -c` wrapper that swallows POSIX termination signals. In this scenario: Declaring `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form launches `dotnet` directly as PID 1 so `SIGTERM` triggers graceful host shutdown.

### Question 3 — C

Answer: Run `az acr build --registry <acrName> --image app:{{.Run.ID}} .` to build and push the container image remotely using ACR Tasks without a local Docker daemon. `az acr build --registry <acrName> --image app:{{.Run.ID}} .` uploads the context and executes the Dockerfile inside ACR Tasks without local Docker Engine. ACR Tasks tar and upload the build context to Azure, executing the Dockerfile build and pushing tagged layers directly inside ACR. Local study-map skill 1.2 (Publish Images, Run ACR Tasks, and Manage Auth/Purge in Azure Container Registry), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az acr build --registry <acrName> --image app:{{.Run.ID}} .` uploads the context and executes the Dockerfile inside ACR Tasks without local Docker Engine.
- **B:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `az acr build --registry <acrName> --image app:{{.Run.ID}} .` uploads the context and executes the Dockerfile inside ACR Tasks without local Docker Engine.
- **C:** Correct. ACR Tasks tar and upload the build context to Azure, executing the Dockerfile build and pushing tagged layers directly inside ACR. In this scenario: `az acr build --registry <acrName> --image app:{{.Run.ID}} .` uploads the context and executes the Dockerfile inside ACR Tasks without local Docker Engine.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `az acr build --registry <acrName> --image app:{{.Run.ID}} .` uploads the context and executes the Dockerfile inside ACR Tasks without local Docker Engine.

### Question 4 — D

Answer: Schedule an ACR Task executing `acr purge --filter "app:.*" --ago 30d --untagged` to clean stale untagged manifests and old tags automatically. A scheduled ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` prunes aged tags and orphaned manifests server-side on a cron schedule. Scheduled `acr purge` tasks reclaim registry storage quota without manual tag deletion scripts. Local study-map skill 1.2 (Publish Images, Run ACR Tasks, and Manage Auth/Purge in Azure Container Registry), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: A scheduled ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` prunes aged tags and orphaned manifests server-side on a cron schedule.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: A scheduled ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` prunes aged tags and orphaned manifests server-side on a cron schedule.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: A scheduled ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` prunes aged tags and orphaned manifests server-side on a cron schedule.
- **D:** Correct. Scheduled `acr purge` tasks reclaim registry storage quota without manual tag deletion scripts. In this scenario: A scheduled ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` prunes aged tags and orphaned manifests server-side on a cron schedule.

### Question 5 — D

Answer: Deploy the application container and Envoy/logging sidecar inside one multi-container ACI group sharing `localhost` network namespace and an `emptyDir` / Azure Files volume. Co-locating both containers inside a single multi-container ACI group shares the `localhost` network stack and mounts a shared memory-backed `emptyDir` volume. Containers in the same ACI container group share one IP/port namespace (`127.0.0.1`) and can mount shared Azure Files or `emptyDir` volumes on Linux. Local study-map skill 1.3 (Run Container Groups, Sidecars, Volumes, and Restart Policies in Azure Container Instances), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Co-locating both containers inside a single multi-container ACI group shares the `localhost` network stack and mounts a shared memory-backed `emptyDir` volume.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Co-locating both containers inside a single multi-container ACI group shares the `localhost` network stack and mounts a shared memory-backed `emptyDir` volume.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Co-locating both containers inside a single multi-container ACI group shares the `localhost` network stack and mounts a shared memory-backed `emptyDir` volume.
- **D:** Correct. Containers in the same ACI container group share one IP/port namespace (`127.0.0.1`) and can mount shared Azure Files or `emptyDir` volumes on Linux. In this scenario: Co-locating both containers inside a single multi-container ACI group shares the `localhost` network stack and mounts a shared memory-backed `emptyDir` volume.

### Question 6 — A

Answer: Pass sensitive tokens via `--secure-environment-variables` (or a secret volume mount) so values never appear in Azure Portal properties or `az container show` plaintext output. Standard environment variables return in cleartext via ARM/CLI read APIs and the Azure Portal; using `--secure-environment-variables` or a secret volume redacts secret values from read outputs. Secure environment variables and secret volumes redact secret values from ARM/CLI read responses. Local study-map skill 1.3 (Run Container Groups, Sidecars, Volumes, and Restart Policies in Azure Container Instances), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Secure environment variables and secret volumes redact secret values from ARM/CLI read responses. In this scenario: Standard environment variables return in cleartext via ARM/CLI read APIs and the Azure Portal; using `--secure-environment-variables` or a secret volume redacts secret values from read outputs.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Standard environment variables return in cleartext via ARM/CLI read APIs and the Azure Portal; using `--secure-environment-variables` or a secret volume redacts secret values from read outputs.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Standard environment variables return in cleartext via ARM/CLI read APIs and the Azure Portal; using `--secure-environment-variables` or a secret volume redacts secret values from read outputs.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Standard environment variables return in cleartext via ARM/CLI read APIs and the Azure Portal; using `--secure-environment-variables` or a secret volume redacts secret values from read outputs.

### Question 7 — A, C, D

Answers: Set `--revision-mode multiple` and apply `az containerapp ingress traffic set --revision-weight` to split live HTTP requests across named revisions; Register a Dapr state or pub/sub component in the Container Apps environment and restrict access via the component `scopes` array to specific `daprAppId` values; Define a Container App secret using `keyVaultUrl` plus `identity` (managed identity resource ID or `system`) and map container environment variables via `secretRef`. Multiple-revision weighted ingress enables 80/20 splits, Dapr component `scopes` isolate `daprAppId` access, and `keyVaultUrl` + `identity` secret references inject Key Vault secrets without ARM plaintext. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Multiple-revision mode keeps more than one revision active simultaneously for weighted blue/green or canary traffic splitting. In this scenario: Multiple-revision weighted ingress enables 80/20 splits, Dapr component `scopes` isolate `daprAppId` access, and `keyVaultUrl` + `identity` secret references inject Key Vault secrets without ARM plaintext.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Multiple-revision weighted ingress enables 80/20 splits, Dapr component `scopes` isolate `daprAppId` access, and `keyVaultUrl` + `identity` secret references inject Key Vault secrets without ARM plaintext.
- **C:** Correct. Key Vault secret references in Container Apps resolve secrets via Managed Identity without storing secret strings in ARM templates. In this scenario: Multiple-revision weighted ingress enables 80/20 splits, Dapr component `scopes` isolate `daprAppId` access, and `keyVaultUrl` + `identity` secret references inject Key Vault secrets without ARM plaintext.
- **D:** Correct. Dapr `scopes` confine which microservices inside a shared Container Apps environment can load or invoke a component. In this scenario: Multiple-revision weighted ingress enables 80/20 splits, Dapr component `scopes` isolate `daprAppId` access, and `keyVaultUrl` + `identity` secret references inject Key Vault secrets without ARM plaintext.
- **E:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Multiple-revision weighted ingress enables 80/20 splits, Dapr component `scopes` isolate `daprAppId` access, and `keyVaultUrl` + `identity` secret references inject Key Vault secrets without ARM plaintext.
- **F:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Multiple-revision weighted ingress enables 80/20 splits, Dapr component `scopes` isolate `daprAppId` access, and `keyVaultUrl` + `identity` secret references inject Key Vault secrets without ARM plaintext.

### Question 8 — B

Answer: Deploy an Azure Container Apps Job (`triggerType: Event` or `Schedule`) with `replicaCompletionCount` and `parallelism` instead of an always-listening HTTP container app. Azure Container Apps Jobs (`triggerType: Schedule` or `Event`) run parallel finite completions (`parallelism` + `replicaCompletionCount`) and shut down cleanly afterward. Container Apps Jobs execute finite scheduled or event-driven workloads to completion without exposing unused HTTP ingress. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Azure Container Apps Jobs (`triggerType: Schedule` or `Event`) run parallel finite completions (`parallelism` + `replicaCompletionCount`) and shut down cleanly afterward.
- **B:** Correct. Container Apps Jobs execute finite scheduled or event-driven workloads to completion without exposing unused HTTP ingress. In this scenario: Azure Container Apps Jobs (`triggerType: Schedule` or `Event`) run parallel finite completions (`parallelism` + `replicaCompletionCount`) and shut down cleanly afterward.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Azure Container Apps Jobs (`triggerType: Schedule` or `Event`) run parallel finite completions (`parallelism` + `replicaCompletionCount`) and shut down cleanly afterward.
- **D:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Azure Container Apps Jobs (`triggerType: Schedule` or `Event`) run parallel finite completions (`parallelism` + `replicaCompletionCount`) and shut down cleanly afterward.

### Question 9 — B

Answer: Provision at least a `Standard` (`S1+`) or `Premium v3` (`P1v3+`) App Service plan to unlock deployment slots, custom domain SNI SSL, and metric/schedule autoscaling. Upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` provides SNI/IP TLS bindings, deployment slots, and metric/schedule autoscale rules unavailable on `F1`/`D1`/`B1`. `Free`, `Shared`, and `Basic` plans omit deployment slots (`S1` gives 5, `P1v3` gives 20) and rule-based autoscale (`S1+` required). Local study-map skill 1.5 (Create Azure App Service Plans and Web Apps Across Linux and Windows Runtimes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` provides SNI/IP TLS bindings, deployment slots, and metric/schedule autoscale rules unavailable on `F1`/`D1`/`B1`.
- **B:** Correct. `Free`, `Shared`, and `Basic` plans omit deployment slots (`S1` gives 5, `P1v3` gives 20) and rule-based autoscale (`S1+` required). In this scenario: Upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` provides SNI/IP TLS bindings, deployment slots, and metric/schedule autoscale rules unavailable on `F1`/`D1`/`B1`.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` provides SNI/IP TLS bindings, deployment slots, and metric/schedule autoscale rules unavailable on `F1`/`D1`/`B1`.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` provides SNI/IP TLS bindings, deployment slots, and metric/schedule autoscale rules unavailable on `F1`/`D1`/`B1`.

### Question 10 — C

Answer: Set `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` inside the final `.NET 8` runtime stage and match `targetPort: 8080` on Container Apps ingress. Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` aligns non-root .NET 8 HTTP listeners with platform `targetPort: 8080` routing. Starting in .NET 8, official Microsoft container images default to non-root port `8080` rather than privileged port `80`. Local study-map skill 1.5 (Create Azure App Service Plans and Web Apps Across Linux and Windows Runtimes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` aligns non-root .NET 8 HTTP listeners with platform `targetPort: 8080` routing.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` aligns non-root .NET 8 HTTP listeners with platform `targetPort: 8080` routing.
- **C:** Correct. Starting in .NET 8, official Microsoft container images default to non-root port `8080` rather than privileged port `80`. In this scenario: Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` aligns non-root .NET 8 HTTP listeners with platform `targetPort: 8080` routing.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` aligns non-root .NET 8 HTTP listeners with platform `targetPort: 8080` routing.

### Question 11 — D

Answer: Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances. Filesystem application logging turns off automatically after 12 hours and overwrites small local buffers; Application Logging (Blob) writes logs to Azure Blob Storage with durable retention policies. Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy. Local study-map skill 1.6 (Configure App Service Diagnostics, Application/Web Server Logging, and Log Streaming), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Filesystem application logging turns off automatically after 12 hours and overwrites small local buffers; Application Logging (Blob) writes logs to Azure Blob Storage with durable retention policies.
- **B:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Filesystem application logging turns off automatically after 12 hours and overwrites small local buffers; Application Logging (Blob) writes logs to Azure Blob Storage with durable retention policies.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Filesystem application logging turns off automatically after 12 hours and overwrites small local buffers; Application Logging (Blob) writes logs to Azure Blob Storage with durable retention policies.
- **D:** Correct. Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy. In this scenario: Filesystem application logging turns off automatically after 12 hours and overwrites small local buffers; Application Logging (Blob) writes logs to Azure Blob Storage with durable retention policies.

### Question 12 — A

Answer: Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`. Running `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu output. `az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting. Local study-map skill 1.6 (Configure App Service Diagnostics, Application/Web Server Logging, and Log Streaming), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. `az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting. In this scenario: Running `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu output.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Running `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu output.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Running `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu output.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Running `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu output.

### Question 13 — B

Answer: Set `WEBSITE_RUN_FROM_PACKAGE=1` and deploy with `az webapp deploy --type zip` so the app mounts the read-only ZIP package directly with atomic cold-start replacement. Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying via `az webapp deploy --type zip` mounts the ZIP archive read-only and switches versions atomically. Running directly from a mounted ZIP eliminates file-lock copy conflicts during `wwwroot` sync and speeds cold starts. Local study-map skill 1.7 (Deploy Code, Run-From-Package ZIPs, and Custom Containers to App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying via `az webapp deploy --type zip` mounts the ZIP archive read-only and switches versions atomically.
- **B:** Correct. Running directly from a mounted ZIP eliminates file-lock copy conflicts during `wwwroot` sync and speeds cold starts. In this scenario: Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying via `az webapp deploy --type zip` mounts the ZIP archive read-only and switches versions atomically.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying via `az webapp deploy --type zip` mounts the ZIP archive read-only and switches versions atomically.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying via `az webapp deploy --type zip` mounts the ZIP archive read-only and switches versions atomically.

### Question 14 — B

Answer: Execute `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine`. `az acr import --name <acrName> --source ... --image ...` copies external registry manifests directly into ACR inside Azure's backbone. `az acr import` copies public or cross-registry container images server-side into ACR without requiring `docker pull` / `docker push` on a local workstation. Local study-map skill 1.7 (Deploy Code, Run-From-Package ZIPs, and Custom Containers to App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az acr import --name <acrName> --source ... --image ...` copies external registry manifests directly into ACR inside Azure's backbone.
- **B:** Correct. `az acr import` copies public or cross-registry container images server-side into ACR without requiring `docker pull` / `docker push` on a local workstation. In this scenario: `az acr import --name <acrName> --source ... --image ...` copies external registry manifests directly into ACR inside Azure's backbone.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `az acr import --name <acrName> --source ... --image ...` copies external registry manifests directly into ACR inside Azure's backbone.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `az acr import --name <acrName> --source ... --image ...` copies external registry manifests directly into ACR inside Azure's backbone.

### Question 15 — B, D

Answers: Enable `httpsOnly: true`, set `minTlsVersion: "1.2"` (or `"1.3"`), and configure `clientCertEnabled` when mutual TLS client certificates are required; Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`. Enabling `httpsOnly: true`, `minTlsVersion: "1.2"`, and `clientCertEnabled` enforces mTLS transport security, while `az webapp config connection-string set --slot-settings` pins `LedgerDb` per slot. Local study-map skill 1.8 (Configure TLS, Mutual TLS, CORS, App Settings, and Service Connections on App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Enabling `httpsOnly: true`, `minTlsVersion: "1.2"`, and `clientCertEnabled` enforces mTLS transport security, while `az webapp config connection-string set --slot-settings` pins `LedgerDb` per slot.
- **B:** Correct. `--slot-settings` pins the connection string (`SQLCONNSTR_LedgerDb`) to the target slot so slot swaps never leak staging databases into production. In this scenario: Enabling `httpsOnly: true`, `minTlsVersion: "1.2"`, and `clientCertEnabled` enforces mTLS transport security, while `az webapp config connection-string set --slot-settings` pins `LedgerDb` per slot.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling `httpsOnly: true`, `minTlsVersion: "1.2"`, and `clientCertEnabled` enforces mTLS transport security, while `az webapp config connection-string set --slot-settings` pins `LedgerDb` per slot.
- **D:** Correct. Enforcing HTTPS redirection and minimum TLS 1.2/1.3 at the App Service front end rejects plaintext HTTP and legacy ciphers before app code runs. In this scenario: Enabling `httpsOnly: true`, `minTlsVersion: "1.2"`, and `clientCertEnabled` enforces mTLS transport security, while `az webapp config connection-string set --slot-settings` pins `LedgerDb` per slot.
- **E:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Enabling `httpsOnly: true`, `minTlsVersion: "1.2"`, and `clientCertEnabled` enforces mTLS transport security, while `az webapp config connection-string set --slot-settings` pins `LedgerDb` per slot.

### Question 16 — C

Answer: Configure App Service `CORS` with explicit origin URLs (and `supportCredentials` only without wildcard `*`) so App Service handles preflight `OPTIONS` requests. Specifying explicit allowed origin `https://desk.crestline.example` (never `*`) alongside `supportCredentials: true` satisfies browser credentialed preflight rules. Platform-level App Service CORS intercepts `OPTIONS` preflight checks; credentialed CORS forbids wildcard `*` origins. Local study-map skill 1.8 (Configure TLS, Mutual TLS, CORS, App Settings, and Service Connections on App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Specifying explicit allowed origin `https://desk.crestline.example` (never `*`) alongside `supportCredentials: true` satisfies browser credentialed preflight rules.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Specifying explicit allowed origin `https://desk.crestline.example` (never `*`) alongside `supportCredentials: true` satisfies browser credentialed preflight rules.
- **C:** Correct. Platform-level App Service CORS intercepts `OPTIONS` preflight checks; credentialed CORS forbids wildcard `*` origins. In this scenario: Specifying explicit allowed origin `https://desk.crestline.example` (never `*`) alongside `supportCredentials: true` satisfies browser credentialed preflight rules.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Specifying explicit allowed origin `https://desk.crestline.example` (never `*`) alongside `supportCredentials: true` satisfies browser credentialed preflight rules.

### Question 17 — B

Answer: Pair every scale-out metric rule (e.g., CPU > 75% for 10 min) with a conservative scale-in rule (e.g., CPU < 35%) and an explicit `coolDown` window plus safe default/max instance bounds. Pairing an upper scale-out threshold (e.g., >75% CPU) with a wide lower scale-in margin (e.g., <35% CPU) and an adequate `coolDown` window eliminates rapid scale flapping. Asymmetric thresholds and cool-down periods prevent rapid flapping (thrashing) where instances repeatedly add and terminate. Local study-map skill 1.9 (Implement Metric-Based and Schedule-Based App Service Autoscaling Rules and Cooldowns), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Pairing an upper scale-out threshold (e.g., >75% CPU) with a wide lower scale-in margin (e.g., <35% CPU) and an adequate `coolDown` window eliminates rapid scale flapping.
- **B:** Correct. Asymmetric thresholds and cool-down periods prevent rapid flapping (thrashing) where instances repeatedly add and terminate. In this scenario: Pairing an upper scale-out threshold (e.g., >75% CPU) with a wide lower scale-in margin (e.g., <35% CPU) and an adequate `coolDown` window eliminates rapid scale flapping.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Pairing an upper scale-out threshold (e.g., >75% CPU) with a wide lower scale-in margin (e.g., <35% CPU) and an adequate `coolDown` window eliminates rapid scale flapping.
- **D:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Pairing an upper scale-out threshold (e.g., >75% CPU) with a wide lower scale-in margin (e.g., <35% CPU) and an adequate `coolDown` window eliminates rapid scale flapping.

### Question 18 — B

Answer: Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps. Configuring `applicationInitialization` with `WEBSITE_SWAP_WARMUP_PING_PATH=/ready` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` verifies readiness on every worker before swapping production routing. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. Local study-map skill 1.9 (Implement Metric-Based and Schedule-Based App Service Autoscaling Rules and Cooldowns), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Configuring `applicationInitialization` with `WEBSITE_SWAP_WARMUP_PING_PATH=/ready` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` verifies readiness on every worker before swapping production routing.
- **B:** Correct. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. In this scenario: Configuring `applicationInitialization` with `WEBSITE_SWAP_WARMUP_PING_PATH=/ready` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` verifies readiness on every worker before swapping production routing.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Configuring `applicationInitialization` with `WEBSITE_SWAP_WARMUP_PING_PATH=/ready` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` verifies readiness on every worker before swapping production routing.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Configuring `applicationInitialization` with `WEBSITE_SWAP_WARMUP_PING_PATH=/ready` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` verifies readiness on every worker before swapping production routing.

### Question 19 — C

Answer: Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps. Configuring `autoSwapSlotName: "production"` alongside `applicationInitialization` warm-up paths promotes `staging` builds automatically once warm-up pings return HTTP `200`. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. Local study-map skill 1.10 (Configure App Service Deployment Slots, Slot-Sticky Settings, Warm-Up, and Traffic Routing), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Configuring `autoSwapSlotName: "production"` alongside `applicationInitialization` warm-up paths promotes `staging` builds automatically once warm-up pings return HTTP `200`.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Configuring `autoSwapSlotName: "production"` alongside `applicationInitialization` warm-up paths promotes `staging` builds automatically once warm-up pings return HTTP `200`.
- **C:** Correct. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. In this scenario: Configuring `autoSwapSlotName: "production"` alongside `applicationInitialization` warm-up paths promotes `staging` builds automatically once warm-up pings return HTTP `200`.
- **D:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Configuring `autoSwapSlotName: "production"` alongside `applicationInitialization` warm-up paths promotes `staging` builds automatically once warm-up pings return HTTP `200`.

### Question 20 — B

Answer: Mark environment-specific settings such as `PaymentWebhookUrl` and production connection strings as `slotSetting: true` (Deployment slot setting) before swapping slots. Marking `CardNetworkEnv` with `slotSetting: true` (Deployment slot setting) keeps each slot's environment variable bound to its slot across swaps. Slot-sticky settings stay pinned to their slot (`Production` vs `Staging`) across swaps instead of traveling with the swapped code. Local study-map skill 1.10 (Configure App Service Deployment Slots, Slot-Sticky Settings, Warm-Up, and Traffic Routing), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Marking `CardNetworkEnv` with `slotSetting: true` (Deployment slot setting) keeps each slot's environment variable bound to its slot across swaps.
- **B:** Correct. Slot-sticky settings stay pinned to their slot (`Production` vs `Staging`) across swaps instead of traveling with the swapped code. In this scenario: Marking `CardNetworkEnv` with `slotSetting: true` (Deployment slot setting) keeps each slot's environment variable bound to its slot across swaps.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Marking `CardNetworkEnv` with `slotSetting: true` (Deployment slot setting) keeps each slot's environment variable bound to its slot across swaps.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Marking `CardNetworkEnv` with `slotSetting: true` (Deployment slot setting) keeps each slot's environment variable bound to its slot across swaps.

### Question 21 — D

Answer: Host the Function App on `Flex Consumption` or `Elastic Premium (EP1+)` when VNet integration, longer execution timeouts beyond 10 minutes, or pre-warmed/always-ready instances are required. Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runs) provides VNet outbound, warm workers, and extended timeouts. Classic Consumption caps timeout at 10 minutes (`functionTimeout`) and cold-starts from zero; `Flex Consumption` and `Premium` add VNet outbound and pre-warmed readiness. Local study-map skill 1.11 (Create and Configure Azure Functions Apps, Hosting Plans, and host.json Settings), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runs) provides VNet outbound, warm workers, and extended timeouts.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runs) provides VNet outbound, warm workers, and extended timeouts.
- **C:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runs) provides VNet outbound, warm workers, and extended timeouts.
- **D:** Correct. Classic Consumption caps timeout at 10 minutes (`functionTimeout`) and cold-starts from zero; `Flex Consumption` and `Premium` add VNet outbound and pre-warmed readiness. In this scenario: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runs) provides VNet outbound, warm workers, and extended timeouts.

### Question 22 — A

Answer: Configure `"functionTimeout": "00:10:00"` and `"logging": { "applicationInsights": { "samplingSettings": { "isEnabled": true, "excludedTypes": "Request;Exception" } } }` inside `host.json`. Configuring `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` applies host-wide across all functions. `host.json` governs global Function host behaviors such as execution timeout and Application Insights telemetry sampling exclusions across all functions in the app. Local study-map skill 1.11 (Create and Configure Azure Functions Apps, Hosting Plans, and host.json Settings), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. `host.json` governs global Function host behaviors such as execution timeout and Application Insights telemetry sampling exclusions across all functions in the app. In this scenario: Configuring `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` applies host-wide across all functions.
- **B:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Configuring `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` applies host-wide across all functions.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Configuring `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` applies host-wide across all functions.
- **D:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Configuring `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` applies host-wide across all functions.

### Question 23 — B, D

Answers: In the .NET isolated worker model, return a custom POCO class uniting `[HttpResult]` (or `HttpResponseData`) with `[CosmosDBOutput]` / `[ServiceBusOutput]` properties; Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`. Returning a custom multi-output POCO with `[HttpResult]` + `[CosmosDBOutput]` works in isolated worker processes, while `[CosmosDBTrigger]` with a `leases` container streams ledger changes. Local study-map skill 1.12 (Implement Azure Functions Input and Output Bindings (Isolated Worker & Declarative Bindings)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Returning a custom multi-output POCO with `[HttpResult]` + `[CosmosDBOutput]` works in isolated worker processes, while `[CosmosDBTrigger]` with a `leases` container streams ledger changes.
- **B:** Correct. `CosmosDBTrigger` wraps the Change Feed Processor library and requires a lease container connection to coordinate partition checkpoints across scaled workers. In this scenario: Returning a custom multi-output POCO with `[HttpResult]` + `[CosmosDBOutput]` works in isolated worker processes, while `[CosmosDBTrigger]` with a `leases` container streams ledger changes.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Returning a custom multi-output POCO with `[HttpResult]` + `[CosmosDBOutput]` works in isolated worker processes, while `[CosmosDBTrigger]` with a `leases` container streams ledger changes.
- **D:** Correct. Isolated-worker C# functions cannot use `out` parameters for bindings; multi-output types return structured properties on a single return object. In this scenario: Returning a custom multi-output POCO with `[HttpResult]` + `[CosmosDBOutput]` works in isolated worker processes, while `[CosmosDBTrigger]` with a `leases` container streams ledger changes.
- **E:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Returning a custom multi-output POCO with `[HttpResult]` + `[CosmosDBOutput]` works in isolated worker processes, while `[CosmosDBTrigger]` with a `leases` container streams ledger changes.

### Question 24 — C

Answer: Apply `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` (or `[FixedDelayRetry]`) on the `[EventHubTrigger]` / `[TimerTrigger]` function. Decorating the function with `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries failed executions in-place before moving the trigger cursor forward. Function-level retry attributes replay failed executions in-memory before advancing trigger checkpoints on Event Hubs and Timer triggers. Local study-map skill 1.12 (Implement Azure Functions Input and Output Bindings (Isolated Worker & Declarative Bindings)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Decorating the function with `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries failed executions in-place before moving the trigger cursor forward.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Decorating the function with `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries failed executions in-place before moving the trigger cursor forward.
- **C:** Correct. Function-level retry attributes replay failed executions in-memory before advancing trigger checkpoints on Event Hubs and Timer triggers. In this scenario: Decorating the function with `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries failed executions in-place before moving the trigger cursor forward.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Decorating the function with `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries failed executions in-place before moving the trigger cursor forward.

### Question 25 — C

Answer: Specify a six-field NCRONTAB expression `{second} {minute} {hour} {day} {month} {day-of-week}` such as `"0 */15 9-17 * * 1-5"` on `[TimerTrigger]`. `"0 */15 9-17 * * 1-5"` places `0` in the leading seconds field and fires every 15 minutes across hours 9–17 on weekdays (`1-5`). Azure Functions `[TimerTrigger]` uses 6-field NCRONTAB (leading seconds field), unlike 5-field Unix cron. Local study-map skill 1.13 (Implement Function Triggers Using Cosmos DB/Blob Data Operations, NCRONTAB Timers, and Webhooks), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` places `0` in the leading seconds field and fires every 15 minutes across hours 9–17 on weekdays (`1-5`).
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` places `0` in the leading seconds field and fires every 15 minutes across hours 9–17 on weekdays (`1-5`).
- **C:** Correct. Azure Functions `[TimerTrigger]` uses 6-field NCRONTAB (leading seconds field), unlike 5-field Unix cron. In this scenario: `"0 */15 9-17 * * 1-5"` places `0` in the leading seconds field and fires every 15 minutes across hours 9–17 on weekdays (`1-5`).
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` places `0` in the leading seconds field and fires every 15 minutes across hours 9–17 on weekdays (`1-5`).

### Question 26 — A, C, E

Answers: Register `CosmosClient` as a process-wide singleton in dependency injection and choose a high-cardinality `PartitionKey` path (or up to 3-level `Hierarchical` subpartition paths) that distributes RU/s evenly; Call `await container.PatchItemAsync<Order>(id, new PartitionKey(pk), new[] { PatchOperation.Increment("/retryCount", 1), PatchOperation.Set("/lastStatus", "Queued") })`; Pass `new ItemRequestOptions { IfMatchEtag = item.ETag }` on `ReplaceItemAsync` and catch `CosmosException` when `StatusCode == HttpStatusCode.PreconditionFailed` (412). Singleton `CosmosClient` DI registration prevents socket exhaustion, `PatchItemAsync` mutates individual paths server-side, and `IfMatchEtag` rejects concurrent lost updates with `412 PreconditionFailed`. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Supplying `IfMatchEtag` enforces optimistic concurrency control so concurrent writers fail with HTTP 412 rather than silently overwriting updates. In this scenario: Singleton `CosmosClient` DI registration prevents socket exhaustion, `PatchItemAsync` mutates individual paths server-side, and `IfMatchEtag` rejects concurrent lost updates with `412 PreconditionFailed`.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Singleton `CosmosClient` DI registration prevents socket exhaustion, `PatchItemAsync` mutates individual paths server-side, and `IfMatchEtag` rejects concurrent lost updates with `412 PreconditionFailed`.
- **C:** Correct. Partial Document Update (`PatchItemAsync`) mutates specific JSON paths server-side without reading, deserializing, and replacing the full document payload. In this scenario: Singleton `CosmosClient` DI registration prevents socket exhaustion, `PatchItemAsync` mutates individual paths server-side, and `IfMatchEtag` rejects concurrent lost updates with `412 PreconditionFailed`.
- **D:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Singleton `CosmosClient` DI registration prevents socket exhaustion, `PatchItemAsync` mutates individual paths server-side, and `IfMatchEtag` rejects concurrent lost updates with `412 PreconditionFailed`.
- **E:** Correct. Reusing one thread-safe `CosmosClient` avoids socket exhaustion, and hierarchical/high-cardinality partition keys prevent hot partitions and 20 GB single-partition caps. In this scenario: Singleton `CosmosClient` DI registration prevents socket exhaustion, `PatchItemAsync` mutates individual paths server-side, and `IfMatchEtag` rejects concurrent lost updates with `412 PreconditionFailed`.
- **F:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Singleton `CosmosClient` DI registration prevents socket exhaustion, `PatchItemAsync` mutates individual paths server-side, and `IfMatchEtag` rejects concurrent lost updates with `412 PreconditionFailed`.

### Question 27 — B

Answer: Add a `compositeIndexes` array matching the exact property sequence and sort directions (`ascending` / `descending`) in the container indexing policy JSON. A `compositeIndexes` entry listing `/riskScore` (`descending`) followed by `/createdUtc` (`ascending`) in exact `ORDER BY` order is mandatory for multi-property sorting. Cosmos DB for NoSQL requires a matching composite index whenever a SQL query specifies `ORDER BY` across two or more properties. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: A `compositeIndexes` entry listing `/riskScore` (`descending`) followed by `/createdUtc` (`ascending`) in exact `ORDER BY` order is mandatory for multi-property sorting.
- **B:** Correct. Cosmos DB for NoSQL requires a matching composite index whenever a SQL query specifies `ORDER BY` across two or more properties. In this scenario: A `compositeIndexes` entry listing `/riskScore` (`descending`) followed by `/createdUtc` (`ascending`) in exact `ORDER BY` order is mandatory for multi-property sorting.
- **C:** Incorrect for this requirement. Excluding wildcard `/*` and indexing only queried filter paths dramatically cuts write Request Unit (RU) cost and index storage on write-heavy containers. Why the keyed choice wins: A `compositeIndexes` entry listing `/riskScore` (`descending`) followed by `/createdUtc` (`ascending`) in exact `ORDER BY` order is mandatory for multi-property sorting.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: A `compositeIndexes` entry listing `/riskScore` (`descending`) followed by `/createdUtc` (`ascending`) in exact `ORDER BY` order is mandatory for multi-property sorting.

### Question 28 — B

Answer: Use `FeedIterator<Order> iter = container.GetItemQueryIterator<Order>(queryDef, requestOptions: new QueryRequestOptions { PartitionKey = new PartitionKey(pk), MaxItemCount = 100 })` and loop `while (iter.HasMoreResults) { FeedResponse<Order> page = await iter.ReadNextAsync(); }`. `container.GetItemQueryIterator<T>` scoped with `QueryRequestOptions { PartitionKey = ..., MaxItemCount = 100 }` and `while (iter.HasMoreResults) { await iter.ReadNextAsync(); }` streams bounded pages with `RequestCharge`. `GetItemQueryIterator<T>` streams paginated results via continuation tokens and inspects `page.RequestCharge` without buffering an entire partition in memory. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `container.GetItemQueryIterator<T>` scoped with `QueryRequestOptions { PartitionKey = ..., MaxItemCount = 100 }` and `while (iter.HasMoreResults) { await iter.ReadNextAsync(); }` streams bounded pages with `RequestCharge`.
- **B:** Correct. `GetItemQueryIterator<T>` streams paginated results via continuation tokens and inspects `page.RequestCharge` without buffering an entire partition in memory. In this scenario: `container.GetItemQueryIterator<T>` scoped with `QueryRequestOptions { PartitionKey = ..., MaxItemCount = 100 }` and `while (iter.HasMoreResults) { await iter.ReadNextAsync(); }` streams bounded pages with `RequestCharge`.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `container.GetItemQueryIterator<T>` scoped with `QueryRequestOptions { PartitionKey = ..., MaxItemCount = 100 }` and `while (iter.HasMoreResults) { await iter.ReadNextAsync(); }` streams bounded pages with `RequestCharge`.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `container.GetItemQueryIterator<T>` scoped with `QueryRequestOptions { PartitionKey = ..., MaxItemCount = 100 }` and `while (iter.HasMoreResults) { await iter.ReadNextAsync(); }` streams bounded pages with `RequestCharge`.

### Question 29 — A

Answer: Use `Session` consistency (the default) and propagate `x-ms-session-token` (`RequestOptions.SessionToken`) across client/middle-tier hops to guarantee monotonic read-your-own-writes at half the read RU cost of `Strong`. Using `Session` consistency and forwarding `SessionToken` (`x-ms-session-token`) across mobile/API requests guarantees read-your-own-writes at 50% of `Strong` read RUs. `Session` consistency guarantees read-your-writes, monotonic reads, and write-follows-reads within a session token at 50% of `Strong` / `BoundedStaleness` read RUs. Local study-map skill 2.2 (Select and Override Cosmos DB Consistency Levels and Session Tokens), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. `Session` consistency guarantees read-your-writes, monotonic reads, and write-follows-reads within a session token at 50% of `Strong` / `BoundedStaleness` read RUs. In this scenario: Using `Session` consistency and forwarding `SessionToken` (`x-ms-session-token`) across mobile/API requests guarantees read-your-own-writes at 50% of `Strong` read RUs.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Using `Session` consistency and forwarding `SessionToken` (`x-ms-session-token`) across mobile/API requests guarantees read-your-own-writes at 50% of `Strong` read RUs.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Using `Session` consistency and forwarding `SessionToken` (`x-ms-session-token`) across mobile/API requests guarantees read-your-own-writes at 50% of `Strong` read RUs.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Using `Session` consistency and forwarding `SessionToken` (`x-ms-session-token`) across mobile/API requests guarantees read-your-own-writes at 50% of `Strong` read RUs.

### Question 30 — D

Answer: Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency. `BoundedStaleness` guarantees total global write order on remote read regions within configured `K` version and `T` time staleness bounds. `Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds. Local study-map skill 2.2 (Select and Override Cosmos DB Consistency Levels and Session Tokens), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `BoundedStaleness` guarantees total global write order on remote read regions within configured `K` version and `T` time staleness bounds.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `BoundedStaleness` guarantees total global write order on remote read regions within configured `K` version and `T` time staleness bounds.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `BoundedStaleness` guarantees total global write order on remote read regions within configured `K` version and `T` time staleness bounds.
- **D:** Correct. `Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds. In this scenario: `BoundedStaleness` guarantees total global write order on remote read regions within configured `K` version and `T` time staleness bounds.

### Question 31 — A

Answer: Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay. Sharing one `processorName` across all six AML replicas load-balances partitions via the `/id` lease container while `.WithStartTime(DateTime.MinValue.ToUniversalTime())` (`StartFromBeginning`) replays historical items. In Change Feed Processor, `processorName` acts like an Event Hubs consumer group: distinct names receive independent copies of every insert/update, while identical names load-balance partitions. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. In Change Feed Processor, `processorName` acts like an Event Hubs consumer group: distinct names receive independent copies of every insert/update, while identical names load-balance partitions. In this scenario: Sharing one `processorName` across all six AML replicas load-balances partitions via the `/id` lease container while `.WithStartTime(DateTime.MinValue.ToUniversalTime())` (`StartFromBeginning`) replays historical items.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Sharing one `processorName` across all six AML replicas load-balances partitions via the `/id` lease container while `.WithStartTime(DateTime.MinValue.ToUniversalTime())` (`StartFromBeginning`) replays historical items.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Sharing one `processorName` across all six AML replicas load-balances partitions via the `/id` lease container while `.WithStartTime(DateTime.MinValue.ToUniversalTime())` (`StartFromBeginning`) replays historical items.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Sharing one `processorName` across all six AML replicas load-balances partitions via the `/id` lease container while `.WithStartTime(DateTime.MinValue.ToUniversalTime())` (`StartFromBeginning`) replays historical items.

### Question 32 — C, E

Answers: Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay; Use Change Feed `AllVersionsAndDeletes` mode (or soft-delete flag items with short TTL in `LatestVersion` mode) because default `LatestVersion` change feed omits hard-deleted items. Giving each worker its own unique `processorName` provides independent partition cursors, and enabling `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) surfaces deleted items. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Giving each worker its own unique `processorName` provides independent partition cursors, and enabling `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) surfaces deleted items.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Giving each worker its own unique `processorName` provides independent partition cursors, and enabling `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) surfaces deleted items.
- **C:** Correct. Standard `LatestVersion` change feed emits only inserts and updates of current items; hard deletes require `AllVersionsAndDeletes` or soft-delete Tombstone items + TTL. In this scenario: Giving each worker its own unique `processorName` provides independent partition cursors, and enabling `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) surfaces deleted items.
- **D:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Giving each worker its own unique `processorName` provides independent partition cursors, and enabling `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) surfaces deleted items.
- **E:** Correct. In Change Feed Processor, `processorName` acts like an Event Hubs consumer group: distinct names receive independent copies of every insert/update, while identical names load-balance partitions. In this scenario: Giving each worker its own unique `processorName` provides independent partition cursors, and enabling `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) surfaces deleted items.

### Question 33 — D

Answer: Enable container `DefaultTimeToLive = -1` (or positive seconds) and set item `ttl = 600` so Cosmos DB purges expired items automatically using background RU capacity. Setting container `DefaultTimeToLive = -1` enables item-level `ttl` expiration using background RUs while leaving items without `ttl` untouched. Container TTL must be non-null (`-1` or `>0`) for per-item `ttl` seconds to take effect; setting `DefaultTimeToLive = null` ignores item-level `ttl`. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` enables item-level `ttl` expiration using background RUs while leaving items without `ttl` untouched.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` enables item-level `ttl` expiration using background RUs while leaving items without `ttl` untouched.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` enables item-level `ttl` expiration using background RUs while leaving items without `ttl` untouched.
- **D:** Correct. Container TTL must be non-null (`-1` or `>0`) for per-item `ttl` seconds to take effect; setting `DefaultTimeToLive = null` ignores item-level `ttl`. In this scenario: Setting container `DefaultTimeToLive = -1` enables item-level `ttl` expiration using background RUs while leaving items without `ttl` untouched.

### Question 34 — C

Answer: Attach searchable key-value `Tags` (`SetTagsAsync` / `BlobUploadOptions.Tags`) and query across containers with `FindBlobsByTagsAsync("@container = 'docs' AND status = 'pending'")`. Writing searchable Blob Index `Tags` (`SetTagsAsync`) and calling `FindBlobsByTagsAsync` queries Azure Storage's native tag index without container enumeration. Blob Index Tags are indexed natively by Azure Storage for server-side filtering, whereas `Metadata` is not searchable without listing every blob. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Writing searchable Blob Index `Tags` (`SetTagsAsync`) and calling `FindBlobsByTagsAsync` queries Azure Storage's native tag index without container enumeration.
- **B:** Incorrect for this requirement. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. Why the keyed choice wins: Writing searchable Blob Index `Tags` (`SetTagsAsync`) and calling `FindBlobsByTagsAsync` queries Azure Storage's native tag index without container enumeration.
- **C:** Correct. Blob Index Tags are indexed natively by Azure Storage for server-side filtering, whereas `Metadata` is not searchable without listing every blob. In this scenario: Writing searchable Blob Index `Tags` (`SetTagsAsync`) and calling `FindBlobsByTagsAsync` queries Azure Storage's native tag index without container enumeration.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Writing searchable Blob Index `Tags` (`SetTagsAsync`) and calling `FindBlobsByTagsAsync` queries Azure Storage's native tag index without container enumeration.

### Question 35 — A

Answer: Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`). `SetHttpHeadersAsync(BlobHttpHeaders)` sets standard HTTP system headers, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` key-value pairs. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. In this scenario: `SetHttpHeadersAsync(BlobHttpHeaders)` sets standard HTTP system headers, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` key-value pairs.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` sets standard HTTP system headers, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` key-value pairs.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` sets standard HTTP system headers, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` key-value pairs.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` sets standard HTTP system headers, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` key-value pairs.

### Question 36 — A

Answer: Use `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` (15–60 seconds or `-1` infinite) and pass `LeaseId` inside `BlobRequestConditions` on subsequent writes/deletes. Uncoordinated writes silently clobber concurrent checkpoint updates; acquiring a 60-second `BlobLeaseClient` lock and passing `LeaseId` in `BlobRequestConditions` enforces exclusive single-writer access. Blob leases grant exclusive write/delete locks (`15` to `60` seconds or infinite `-1`) so competing workers immediately receive `412 LeaseIdMissing/Mismatch`. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Blob leases grant exclusive write/delete locks (`15` to `60` seconds or infinite `-1`) so competing workers immediately receive `412 LeaseIdMissing/Mismatch`. In this scenario: Uncoordinated writes silently clobber concurrent checkpoint updates; acquiring a 60-second `BlobLeaseClient` lock and passing `LeaseId` in `BlobRequestConditions` enforces exclusive single-writer access.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Uncoordinated writes silently clobber concurrent checkpoint updates; acquiring a 60-second `BlobLeaseClient` lock and passing `LeaseId` in `BlobRequestConditions` enforces exclusive single-writer access.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Uncoordinated writes silently clobber concurrent checkpoint updates; acquiring a 60-second `BlobLeaseClient` lock and passing `LeaseId` in `BlobRequestConditions` enforces exclusive single-writer access.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Uncoordinated writes silently clobber concurrent checkpoint updates; acquiring a 60-second `BlobLeaseClient` lock and passing `LeaseId` in `BlobRequestConditions` enforces exclusive single-writer access.

### Question 37 — D

Answer: Invoke `BlobClient.StartCopyFromUriAsync(sourceSasUri)` to trigger asynchronous server-side blob copy and inspect `CopyStatus` without streaming bytes through the client VM. `BlobClient.StartCopyFromUriAsync(sourceSasUri)` copies blobs asynchronously across Azure Storage servers while `CopyStatus` tracks completion. `StartCopyFromUriAsync` instructs Azure Storage fabric to copy blobs asynchronously server-to-server using a readable source URI/SAS. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` copies blobs asynchronously across Azure Storage servers while `CopyStatus` tracks completion.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` copies blobs asynchronously across Azure Storage servers while `CopyStatus` tracks completion.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` copies blobs asynchronously across Azure Storage servers while `CopyStatus` tracks completion.
- **D:** Correct. `StartCopyFromUriAsync` instructs Azure Storage fabric to copy blobs asynchronously server-to-server using a readable source URI/SAS. In this scenario: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` copies blobs asynchronously across Azure Storage servers while `CopyStatus` tracks completion.

### Question 38 — B

Answer: Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`. Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` scopes access to that single blob. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` scopes access to that single blob.
- **B:** Correct. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. In this scenario: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` scopes access to that single blob.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` scopes access to that single blob.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` scopes access to that single blob.

### Question 39 — C, D

Answers: Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`); Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob). A Lifecycle Management policy JSON automates `tierToCool` and `tierToArchive` transitions, and `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` restores archived blobs with priority. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: A Lifecycle Management policy JSON automates `tierToCool` and `tierToArchive` transitions, and `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` restores archived blobs with priority.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: A Lifecycle Management policy JSON automates `tierToCool` and `tierToArchive` transitions, and `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` restores archived blobs with priority.
- **C:** Correct. Lifecycle management policies automate tier transitions and retention deletion server-side once per day without custom cron jobs. In this scenario: A Lifecycle Management policy JSON automates `tierToCool` and `tierToArchive` transitions, and `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` restores archived blobs with priority.
- **D:** Correct. `SetAccessTierAsync` (or copy-to-Hot) initiates Archive rehydration; `RehydratePriority.High` prioritizes restoration (often under 1 hour for <10 GB blobs). In this scenario: A Lifecycle Management policy JSON automates `tierToCool` and `tierToArchive` transitions, and `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` restores archived blobs with priority.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: A Lifecycle Management policy JSON automates `tierToCool` and `tierToArchive` transitions, and `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` restores archived blobs with priority.

### Question 40 — B

Answer: Verify the blob is currently in the Archive access tier → call SetAccessTier (or CopyBlob) targeting Hot or Cool with Standard or High rehydrate priority → poll ArchiveStatus until rehydration completes and tier updates → download the blob content. Verifying `Archive` tier, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with rehydrate priority, polling `ArchiveStatus` until online, and downloading prevents HTTP `409 BlobArchived`. Archived blobs are offline and unreadable directly; changing tier or copying to Hot/Cool initiates asynchronous rehydration that must finish before download. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Calling Download directly on an Archive-tier blob immediately throws HTTP 409 Conflict (`BlobArchived`). Why the keyed choice wins: Verifying `Archive` tier, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with rehydrate priority, polling `ArchiveStatus` until online, and downloading prevents HTTP `409 BlobArchived`.
- **B:** Correct. Archived blobs are offline and unreadable directly; changing tier or copying to Hot/Cool initiates asynchronous rehydration that must finish before download. In this scenario: Verifying `Archive` tier, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with rehydrate priority, polling `ArchiveStatus` until online, and downloading prevents HTTP `409 BlobArchived`.
- **C:** Incorrect for this requirement. User metadata does not trigger storage rehydration, and setting tier back to Archive keeps the blob offline. Why the keyed choice wins: Verifying `Archive` tier, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with rehydrate priority, polling `ArchiveStatus` until online, and downloading prevents HTTP `409 BlobArchived`.
- **D:** Incorrect for this requirement. Leasing does not bring an offline Archive blob online; rehydration to Hot or Cool must complete before any read succeeds. Why the keyed choice wins: Verifying `Archive` tier, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with rehydrate priority, polling `ArchiveStatus` until online, and downloading prevents HTTP `409 BlobArchived`.

### Question 41 — B, D

Answers: Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps; Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`. `PublicClientApplicationBuilder` with Authorization Code + PKCE protects public clients, while calling `AcquireTokenSilent` first and catching `MsalUiRequiredException` before `AcquireTokenInteractive` avoids unnecessary prompts. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE protects public clients, while calling `AcquireTokenSilent` first and catching `MsalUiRequiredException` before `AcquireTokenInteractive` avoids unnecessary prompts.
- **B:** Correct. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. In this scenario: `PublicClientApplicationBuilder` with Authorization Code + PKCE protects public clients, while calling `AcquireTokenSilent` first and catching `MsalUiRequiredException` before `AcquireTokenInteractive` avoids unnecessary prompts.
- **C:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE protects public clients, while calling `AcquireTokenSilent` first and catching `MsalUiRequiredException` before `AcquireTokenInteractive` avoids unnecessary prompts.
- **D:** Correct. MSAL refreshes cached tokens transparently during `AcquireTokenSilent`; prompting interactively on every call degrades UX and hits rate limits. In this scenario: `PublicClientApplicationBuilder` with Authorization Code + PKCE protects public clients, while calling `AcquireTokenSilent` first and catching `MsalUiRequiredException` before `AcquireTokenInteractive` avoids unnecessary prompts.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE protects public clients, while calling `AcquireTokenSilent` first and catching `MsalUiRequiredException` before `AcquireTokenInteractive` avoids unnecessary prompts.

### Question 42 — A

Answer: Use `ConfidentialClientApplicationBuilder` authenticated with a client certificate (or workload identity assertion) calling `AcquireTokenForClient(new[] { "api://.../.default" })` for headless background daemons. `ConfidentialClientApplicationBuilder` authenticated with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://ledger/.default" })` implements OAuth 2.0 Client Credentials cleanly. Daemon apps without a signed-in user use OAuth 2.0 Client Credentials flow and must request the `.default` scope for pre-consented application permissions. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Daemon apps without a signed-in user use OAuth 2.0 Client Credentials flow and must request the `.default` scope for pre-consented application permissions. In this scenario: `ConfidentialClientApplicationBuilder` authenticated with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://ledger/.default" })` implements OAuth 2.0 Client Credentials cleanly.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` authenticated with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://ledger/.default" })` implements OAuth 2.0 Client Credentials cleanly.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` authenticated with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://ledger/.default" })` implements OAuth 2.0 Client Credentials cleanly.
- **D:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` authenticated with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://ledger/.default" })` implements OAuth 2.0 Client Credentials cleanly.

### Question 43 — B

Answer: Register the middle-tier API scope and delegated Graph permissions in Entra ID → validate the incoming user token → call ConfidentialClientApplication.AcquireTokenOnBehalfOf(UserAssertion) → invoke Microsoft Graph with the exchanged token. Exposing the Loan API scope + delegated Graph permissions, validating the incoming user token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated user identity. The middle-tier API must validate the caller token first and exchange it as a UserAssertion via ConfidentialClientApplication before calling Graph as that user. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Graph rejects unauthenticated requests, and OBO cannot run before app registration and incoming token validation. Why the keyed choice wins: Exposing the Loan API scope + delegated Graph permissions, validating the incoming user token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated user identity.
- **B:** Correct. The middle-tier API must validate the caller token first and exchange it as a UserAssertion via ConfidentialClientApplication before calling Graph as that user. In this scenario: Exposing the Loan API scope + delegated Graph permissions, validating the incoming user token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated user identity.
- **C:** Incorrect for this requirement. OBO requires a confidential client with a secret or certificate and `AcquireTokenOnBehalfOf`, not app-only `AcquireTokenForClient`. Why the keyed choice wins: Exposing the Loan API scope + delegated Graph permissions, validating the incoming user token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated user identity.
- **D:** Incorrect for this requirement. A token whose audience (`aud`) is the custom middle-tier API is rejected by Microsoft Graph; OBO exchange must occur first. Why the keyed choice wins: Exposing the Loan API scope + delegated Graph permissions, validating the incoming user token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated user identity.

### Question 44 — A

Answer: Declare `appRoles` with `allowedMemberTypes: ["User", "Application"]` in the Entra app registration manifest and validate the `roles` claim (`[Authorize(Roles = "...")]`) in the web API. Declaring `WireApprover` inside `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both assigned users and service principals. Entra ID emits assigned app roles inside the `roles` JWT claim for both human users and service principals without requiring directory-level Entra admin roles. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Entra ID emits assigned app roles inside the `roles` JWT claim for both human users and service principals without requiring directory-level Entra admin roles. In this scenario: Declaring `WireApprover` inside `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both assigned users and service principals.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Declaring `WireApprover` inside `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both assigned users and service principals.
- **C:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Declaring `WireApprover` inside `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both assigned users and service principals.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Declaring `WireApprover` inside `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both assigned users and service principals.

### Question 45 — C

Answer: Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation. Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit token validation checks `tid` / issuer claims against subscribed corporate tenants. Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit token validation checks `tid` / issuer claims against subscribed corporate tenants.
- **B:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit token validation checks `tid` / issuer claims against subscribed corporate tenants.
- **C:** Correct. Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`. In this scenario: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit token validation checks `tid` / issuer claims against subscribed corporate tenants.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit token validation checks `tid` / issuer claims against subscribed corporate tenants.

### Question 46 — D

Answer: Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`). Setting Easy Auth's unauthenticated action to `Return HTTP 401 Unauthorized` returns standards-compliant API status codes instead of browser `302` redirects. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting Easy Auth's unauthenticated action to `Return HTTP 401 Unauthorized` returns standards-compliant API status codes instead of browser `302` redirects.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting Easy Auth's unauthenticated action to `Return HTTP 401 Unauthorized` returns standards-compliant API status codes instead of browser `302` redirects.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting Easy Auth's unauthenticated action to `Return HTTP 401 Unauthorized` returns standards-compliant API status codes instead of browser `302` redirects.
- **D:** Correct. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. In this scenario: Setting Easy Auth's unauthenticated action to `Return HTTP 401 Unauthorized` returns standards-compliant API status codes instead of browser `302` redirects.

### Question 47 — B

Answer: Mint a short-lived HTTPS-only (`SasProtocol.HttpsOnly`) User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` instead of Account or Service SAS signed with storage account keys. Switching to User Delegation SAS signed via `GetUserDelegationKeyAsync` uses Microsoft Entra RBAC credentials so `allowSharedKeyAccess` can be set to `false`. User Delegation SAS eliminates shared storage account keys, enforces Entra RBAC, and automatically invalidates if the signing identity loses permissions. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Switching to User Delegation SAS signed via `GetUserDelegationKeyAsync` uses Microsoft Entra RBAC credentials so `allowSharedKeyAccess` can be set to `false`.
- **B:** Correct. User Delegation SAS eliminates shared storage account keys, enforces Entra RBAC, and automatically invalidates if the signing identity loses permissions. In this scenario: Switching to User Delegation SAS signed via `GetUserDelegationKeyAsync` uses Microsoft Entra RBAC credentials so `allowSharedKeyAccess` can be set to `false`.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Switching to User Delegation SAS signed via `GetUserDelegationKeyAsync` uses Microsoft Entra RBAC credentials so `allowSharedKeyAccess` can be set to `false`.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Switching to User Delegation SAS signed via `GetUserDelegationKeyAsync` uses Microsoft Entra RBAC credentials so `allowSharedKeyAccess` can be set to `false`.

### Question 48 — D

Answer: Bind a Service SAS to a container/queue/table Stored Access Policy (`SignedIdentifier`, omitting inline start/expiry/permissions) so compromised tokens can be revoked instantly by modifying or deleting the policy. Referencing a container `StoredAccessPolicy` (`SignedIdentifier`) with expiry/permissions defined on the policy allows instant revocation by deleting or updating that policy. Up to 5 Stored Access Policies per container allow instant SAS revocation without rotating storage account keys; Note that User Delegation SAS uses key revocation instead of Stored Access Policies. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Referencing a container `StoredAccessPolicy` (`SignedIdentifier`) with expiry/permissions defined on the policy allows instant revocation by deleting or updating that policy.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Referencing a container `StoredAccessPolicy` (`SignedIdentifier`) with expiry/permissions defined on the policy allows instant revocation by deleting or updating that policy.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Referencing a container `StoredAccessPolicy` (`SignedIdentifier`) with expiry/permissions defined on the policy allows instant revocation by deleting or updating that policy.
- **D:** Correct. Up to 5 Stored Access Policies per container allow instant SAS revocation without rotating storage account keys; Note that User Delegation SAS uses key revocation instead of Stored Access Policies. In this scenario: Referencing a container `StoredAccessPolicy` (`SignedIdentifier`) with expiry/permissions defined on the policy allows instant revocation by deleting or updating that policy.

### Question 49 — D

Answer: Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`. Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` restricts the token to that exact blob. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` restricts the token to that exact blob.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` restricts the token to that exact blob.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` restricts the token to that exact blob.
- **D:** Correct. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. In this scenario: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` restricts the token to that exact blob.

### Question 50 — A, C

Answers: Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`; Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses. Requesting least-privilege read scopes with `$select` + `PageIterator<T>` streamlines paging, and grouping up to 20 calls in `BatchRequestContentCollection` (`/$batch`) while respecting `Retry-After` prevents throttling. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Microsoft Graph enforces least-privilege consent scopes, trims payload size with `$select`, and paginates `@odata.nextLink` cleanly through `PageIterator<T>`. In this scenario: Requesting least-privilege read scopes with `$select` + `PageIterator<T>` streamlines paging, and grouping up to 20 calls in `BatchRequestContentCollection` (`/$batch`) while respecting `Retry-After` prevents throttling.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Requesting least-privilege read scopes with `$select` + `PageIterator<T>` streamlines paging, and grouping up to 20 calls in `BatchRequestContentCollection` (`/$batch`) while respecting `Retry-After` prevents throttling.
- **C:** Correct. Graph JSON batching (`/$batch`) bundles up to 20 sub-requests per round-trip, while built-in SDK retry middleware respects `Retry-After`. In this scenario: Requesting least-privilege read scopes with `$select` + `PageIterator<T>` streamlines paging, and grouping up to 20 calls in `BatchRequestContentCollection` (`/$batch`) while respecting `Retry-After` prevents throttling.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Requesting least-privilege read scopes with `$select` + `PageIterator<T>` streamlines paging, and grouping up to 20 calls in `BatchRequestContentCollection` (`/$batch`) while respecting `Retry-After` prevents throttling.
- **E:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Requesting least-privilege read scopes with `$select` + `PageIterator<T>` streamlines paging, and grouping up to 20 calls in `BatchRequestContentCollection` (`/$batch`) while respecting `Retry-After` prevents throttling.

### Question 51 — D

Answer: Call `await graphClient.Users.GetAsync(rc => { rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }; rc.QueryParameters.Filter = "accountEnabled eq true"; })`. Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` applies OData projection and filtering server-side. In Microsoft Graph .NET SDK v5, `$select` and `$filter` query parameters reduce payload size and network transfer on collection endpoints. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` applies OData projection and filtering server-side.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` applies OData projection and filtering server-side.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` applies OData projection and filtering server-side.
- **D:** Correct. In Microsoft Graph .NET SDK v5, `$select` and `$filter` query parameters reduce payload size and network transfer on collection endpoints. In this scenario: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` applies OData projection and filtering server-side.

### Question 52 — D

Answer: Call `await confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` inside the middle-tier API. `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the user assertion via OAuth 2.0 On-Behalf-Of. OAuth 2.0 On-Behalf-Of (`AcquireTokenOnBehalfOf`) exchanges an incoming user access token for a downstream API token while preserving delegated user identity and consent. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the user assertion via OAuth 2.0 On-Behalf-Of.
- **B:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the user assertion via OAuth 2.0 On-Behalf-Of.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the user assertion via OAuth 2.0 On-Behalf-Of.
- **D:** Correct. OAuth 2.0 On-Behalf-Of (`AcquireTokenOnBehalfOf`) exchanges an incoming user access token for a downstream API token while preserving delegated user identity and consent. In this scenario: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the user assertion via OAuth 2.0 On-Behalf-Of.

### Question 53 — C, E

Answers: Use `SecretClient` (`Azure.Security.KeyVault.Secrets`) for connection strings/tokens, `KeyClient` / `CryptographyClient` (`Azure.Security.KeyVault.Keys`) for RSA/EC wrap-unwrap-sign, and `CertificateClient` for X.509 lifecycle; Enable Soft Delete (mandatory on new vaults, 7–90 days) plus Purge Protection on Azure Key Vault so neither accidental deletion nor malicious principals can permanently destroy keys before retention expires. Using dedicated `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete + Purge Protection meets all operational and compliance goals. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Using dedicated `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete + Purge Protection meets all operational and compliance goals.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Using dedicated `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete + Purge Protection meets all operational and compliance goals.
- **C:** Correct. Soft Delete allows recovery via `StartRecoverDeletedSecretAsync`, while Purge Protection blocks permanent `PurgeDeletedSecretAsync` calls during retention. In this scenario: Using dedicated `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete + Purge Protection meets all operational and compliance goals.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Using dedicated `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete + Purge Protection meets all operational and compliance goals.
- **E:** Correct. Azure Key Vault SDK v4 splits secrets, cryptographic keys, and X.509 certificates into dedicated clients and RBAC data-plane roles (`Key Vault Secrets User`, `Crypto User`, `Certificates User`). In this scenario: Using dedicated `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete + Purge Protection meets all operational and compliance goals.

### Question 54 — D

Answer: Instantiate `new CryptographyClient(keyVaultKey.Id, new DefaultAzureCredential())` and invoke `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync(...)`. `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` protects symmetric DEKs via Key Vault without uploading bulk PAN files. Envelope encryption keeps bulk data encryption keys (`DEK`) wrapped by hardware/software-protected Key Vault KEKs without sending large payloads through Key Vault. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` protects symmetric DEKs via Key Vault without uploading bulk PAN files.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` protects symmetric DEKs via Key Vault without uploading bulk PAN files.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` protects symmetric DEKs via Key Vault without uploading bulk PAN files.
- **D:** Correct. Envelope encryption keeps bulk data encryption keys (`DEK`) wrapped by hardware/software-protected Key Vault KEKs without sending large payloads through Key Vault. In this scenario: `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` protects symmetric DEKs via Key Vault without uploading bulk PAN files.

### Question 55 — B

Answer: Configure App Service / Functions application settings using `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` (omitting secret version) paired with `Key Vault Secrets User` on the app Managed Identity. `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity resolves rotated secret versions automatically. Versionless Key Vault references automatically pull rotated secret versions within 24 hours (or immediately on config change / manual sync) with zero SDK boilerplate. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity resolves rotated secret versions automatically.
- **B:** Correct. Versionless Key Vault references automatically pull rotated secret versions within 24 hours (or immediately on config change / manual sync) with zero SDK boilerplate. In this scenario: `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity resolves rotated secret versions automatically.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity resolves rotated secret versions automatically.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity resolves rotated secret versions automatically.

### Question 56 — C

Answer: Instantiate `new DefaultAzureCredential()` (or explicit `ManagedIdentityCredential(clientId)` for user-assigned identities in production) so identical code authenticates via Azure CLI / Visual Studio locally and Managed Identity in Azure. `DefaultAzureCredential` chains local developer credentials (`AzureCliCredential`, `VisualStudioCredential`) in dev and IMDS `ManagedIdentityCredential` in Azure without code branches. `DefaultAzureCredential` chains developer workstation credentials locally and IMDS Managed Identity in Azure; passing `managedIdentityClientId` is required when selecting a specific user-assigned identity. Local study-map skill 3.7 (Implement System-Assigned and User-Assigned Managed Identities and DefaultAzureCredential), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `DefaultAzureCredential` chains local developer credentials (`AzureCliCredential`, `VisualStudioCredential`) in dev and IMDS `ManagedIdentityCredential` in Azure without code branches.
- **B:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `DefaultAzureCredential` chains local developer credentials (`AzureCliCredential`, `VisualStudioCredential`) in dev and IMDS `ManagedIdentityCredential` in Azure without code branches.
- **C:** Correct. `DefaultAzureCredential` chains developer workstation credentials locally and IMDS Managed Identity in Azure; passing `managedIdentityClientId` is required when selecting a specific user-assigned identity. In this scenario: `DefaultAzureCredential` chains local developer credentials (`AzureCliCredential`, `VisualStudioCredential`) in dev and IMDS `ManagedIdentityCredential` in Azure without code branches.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `DefaultAzureCredential` chains local developer credentials (`AzureCliCredential`, `VisualStudioCredential`) in dev and IMDS `ManagedIdentityCredential` in Azure without code branches.

### Question 57 — D, E

Answers: Run `AppRequests | where TimeGenerated > ago(1h) | summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)`; Run `AppRequests | where ResultCode == "500" | join kind=inner (AppDependencies | where Success == false) on OperationId | project TimeGenerated, Name, Target, DependencyType, ResultCode1`. `summarize countif(Success == false), percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` tracks error/latency buckets, and joining failed `AppRequests` with failed `AppDependencies` on `OperationId` isolates root-cause dependencies. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `summarize countif(Success == false), percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` tracks error/latency buckets, and joining failed `AppRequests` with failed `AppDependencies` on `OperationId` isolates root-cause dependencies.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `summarize countif(Success == false), percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` tracks error/latency buckets, and joining failed `AppRequests` with failed `AppDependencies` on `OperationId` isolates root-cause dependencies.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `summarize countif(Success == false), percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` tracks error/latency buckets, and joining failed `AppRequests` with failed `AppDependencies` on `OperationId` isolates root-cause dependencies.
- **D:** Correct. KQL `countif` and `percentile(..., 95)` grouped by `bin(TimeGenerated, 5m)` quantify error spikes and tail latency per operation over fixed time buckets. In this scenario: `summarize countif(Success == false), percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` tracks error/latency buckets, and joining failed `AppRequests` with failed `AppDependencies` on `OperationId` isolates root-cause dependencies.
- **E:** Correct. Joining `AppRequests` and `AppDependencies` on `OperationId` isolates which exact downstream SQL, HTTP, or Storage dependency triggered HTTP 500 responses. In this scenario: `summarize countif(Success == false), percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` tracks error/latency buckets, and joining failed `AppRequests` with failed `AppDependencies` on `OperationId` isolates root-cause dependencies.

### Question 58 — A

Answer: Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits. Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry `TracerProvider`/`MeterProvider`) and waiting briefly before exit drains buffered telemetry to Azure Monitor. Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics. In this scenario: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry `TracerProvider`/`MeterProvider`) and waiting briefly before exit drains buffered telemetry to Azure Monitor.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry `TracerProvider`/`MeterProvider`) and waiting briefly before exit drains buffered telemetry to Azure Monitor.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry `TracerProvider`/`MeterProvider`) and waiting briefly before exit drains buffered telemetry to Azure Monitor.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry `TracerProvider`/`MeterProvider`) and waiting briefly before exit drains buffered telemetry to Azure Monitor.

### Question 59 — D

Answer: Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`. Registering a custom `ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively as `AppDependencies`. `System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Registering a custom `ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively as `AppDependencies`.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Registering a custom `ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively as `AppDependencies`.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Registering a custom `ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively as `AppDependencies`.
- **D:** Correct. `System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro. In this scenario: Registering a custom `ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively as `AppDependencies`.

### Question 60 — C

Answer: Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group. Application Insights Standard Availability Tests validate SSL expiry and HTTP status from multiple POPs, and a `>= 2` location alert rule wired to an Action Group prevents single-region false pages. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Application Insights Standard Availability Tests validate SSL expiry and HTTP status from multiple POPs, and a `>= 2` location alert rule wired to an Action Group prevents single-region false pages.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Application Insights Standard Availability Tests validate SSL expiry and HTTP status from multiple POPs, and a `>= 2` location alert rule wired to an Action Group prevents single-region false pages.
- **C:** Correct. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. In this scenario: Application Insights Standard Availability Tests validate SSL expiry and HTTP status from multiple POPs, and a `>= 2` location alert rule wired to an Action Group prevents single-region false pages.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Application Insights Standard Availability Tests validate SSL expiry and HTTP status from multiple POPs, and a `>= 2` location alert rule wired to an Action Group prevents single-region false pages.

### Question 61 — C

Answer: Create an Azure Monitor Metric Alert (Dynamic Thresholds or static p95 latency/5xx count) or Scheduled Query (KQL) Alert targeting an Action Group configured with webhook / Azure Function / email-SMS receivers. An Azure Monitor Metric Alert using Dynamic Thresholds learns historical payday/weekday patterns and triggers an Action Group webhook receiver. Metric alerts offer sub-minute stateful evaluation on numeric signals, whereas Scheduled Query Rules run expressive KQL joins on log tables at configured intervals. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: An Azure Monitor Metric Alert using Dynamic Thresholds learns historical payday/weekday patterns and triggers an Action Group webhook receiver.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: An Azure Monitor Metric Alert using Dynamic Thresholds learns historical payday/weekday patterns and triggers an Action Group webhook receiver.
- **C:** Correct. Metric alerts offer sub-minute stateful evaluation on numeric signals, whereas Scheduled Query Rules run expressive KQL joins on log tables at configured intervals. In this scenario: An Azure Monitor Metric Alert using Dynamic Thresholds learns historical payday/weekday patterns and triggers an Action Group webhook receiver.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: An Azure Monitor Metric Alert using Dynamic Thresholds learns historical payday/weekday patterns and triggers an Action Group webhook receiver.

### Question 62 — D

Answer: Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group. Deploying a VNet-integrated Timer-Triggered Function that tests the internal endpoint and calls `TelemetryClient.TrackAvailability()` publishes custom availability results for Azure Monitor alerts. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Deploying a VNet-integrated Timer-Triggered Function that tests the internal endpoint and calls `TelemetryClient.TrackAvailability()` publishes custom availability results for Azure Monitor alerts.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Deploying a VNet-integrated Timer-Triggered Function that tests the internal endpoint and calls `TelemetryClient.TrackAvailability()` publishes custom availability results for Azure Monitor alerts.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Deploying a VNet-integrated Timer-Triggered Function that tests the internal endpoint and calls `TelemetryClient.TrackAvailability()` publishes custom availability results for Azure Monitor alerts.
- **D:** Correct. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. In this scenario: Deploying a VNet-integrated Timer-Triggered Function that tests the internal endpoint and calls `TelemetryClient.TrackAvailability()` publishes custom availability results for Azure Monitor alerts.

### Question 63 — A, E

Answers: Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments; Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently. `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles modern OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps daily volume without sampling Live Metrics. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled. In this scenario: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles modern OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps daily volume without sampling Live Metrics.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles modern OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps daily volume without sampling Live Metrics.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles modern OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps daily volume without sampling Live Metrics.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles modern OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps daily volume without sampling Live Metrics.
- **E:** Correct. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. In this scenario: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles modern OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps daily volume without sampling Live Metrics.

### Question 64 — D

Answer: Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently. Live Metrics Stream is always 100% unsampled in real time; enabling Adaptive or Ingestion Sampling reduces stored Log Analytics ingestion bills while keeping Live Metrics completely intact. Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Live Metrics Stream is always 100% unsampled in real time; enabling Adaptive or Ingestion Sampling reduces stored Log Analytics ingestion bills while keeping Live Metrics completely intact.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Live Metrics Stream is always 100% unsampled in real time; enabling Adaptive or Ingestion Sampling reduces stored Log Analytics ingestion bills while keeping Live Metrics completely intact.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Live Metrics Stream is always 100% unsampled in real time; enabling Adaptive or Ingestion Sampling reduces stored Log Analytics ingestion bills while keeping Live Metrics completely intact.
- **D:** Correct. Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled. In this scenario: Live Metrics Stream is always 100% unsampled in real time; enabling Adaptive or Ingestion Sampling reduces stored Log Analytics ingestion bills while keeping Live Metrics completely intact.

### Question 65 — B

Answer: Select `Developer` (non-SLA) or `Premium` / `Standard v2` for VNet integration, and deploy the containerized APIM Self-Hosted Gateway (`mcr.microsoft.com/azure-api-management/gateway`) for hybrid on-premises/multi-cloud local traffic routing. Provisioning APIM `Developer` or `Premium` tier and running the containerized Self-Hosted Gateway in Zurich keeps data-plane traffic local while pulling policy updates from Azure. Self-hosted gateways require `Developer` or `Premium` tier and keep data-plane traffic local while pulling policy updates outbound over HTTPS/443 from Azure. Local study-map skill 5.1 (Provision Azure API Management Tiers, VNet Modes, and Self-Hosted Hybrid Gateways), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and running the containerized Self-Hosted Gateway in Zurich keeps data-plane traffic local while pulling policy updates from Azure.
- **B:** Correct. Self-hosted gateways require `Developer` or `Premium` tier and keep data-plane traffic local while pulling policy updates outbound over HTTPS/443 from Azure. In this scenario: Provisioning APIM `Developer` or `Premium` tier and running the containerized Self-Hosted Gateway in Zurich keeps data-plane traffic local while pulling policy updates from Azure.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and running the containerized Self-Hosted Gateway in Zurich keeps data-plane traffic local while pulling policy updates from Azure.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and running the containerized Self-Hosted Gateway in Zurich keeps data-plane traffic local while pulling policy updates from Azure.

### Question 66 — A

Answer: Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`. `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens without client secrets. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. Local study-map skill 5.1 (Provision Azure API Management Tiers, VNet Modes, and Self-Hosted Hybrid Gateways), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. In this scenario: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens without client secrets.
- **B:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens without client secrets.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens without client secrets.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens without client secrets.

### Question 67 — C

Answer: Use APIM `Revisions` to stage, test, and swap non-breaking internal changes safely on the same consumer URL (`;rev=2`), and use APIM `Versions` (path/header/query) when publishing breaking contract changes side-by-side for distinct consumer cohorts. APIM `Revisions` stage and swap non-breaking edits transparently on the active URL, while APIM `Versions` publish breaking `/v1` and `/v2` contracts side by side. Revisions let authors edit and flip the `current` implementation transparently; Versions expose distinct URLs/headers so legacy clients keep working. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: APIM `Revisions` stage and swap non-breaking edits transparently on the active URL, while APIM `Versions` publish breaking `/v1` and `/v2` contracts side by side.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: APIM `Revisions` stage and swap non-breaking edits transparently on the active URL, while APIM `Versions` publish breaking `/v1` and `/v2` contracts side by side.
- **C:** Correct. Revisions let authors edit and flip the `current` implementation transparently; Versions expose distinct URLs/headers so legacy clients keep working. In this scenario: APIM `Revisions` stage and swap non-breaking edits transparently on the active URL, while APIM `Versions` publish breaking `/v1` and `/v2` contracts side by side.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: APIM `Revisions` stage and swap non-breaking edits transparently on the active URL, while APIM `Versions` publish breaking `/v1` and `/v2` contracts side by side.

### Question 68 — A

Answer: Use `<mock-response status-code="200" content-type="application/json" />` during frontend parallel development, or `<rewrite-uri template="/internal/v2/orders/{orderId}" />` with `<set-backend-service base-url="..." />` in `<inbound>`. `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI samples early, while `<rewrite-uri>` + `<set-backend-service>` map external paths to internal routes in production. `<mock-response>` short-circuits backend forwarding using OpenAPI example payloads, while `<rewrite-uri>` maps public clean paths onto legacy internal routes. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. `<mock-response>` short-circuits backend forwarding using OpenAPI example payloads, while `<rewrite-uri>` maps public clean paths onto legacy internal routes. In this scenario: `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI samples early, while `<rewrite-uri>` + `<set-backend-service>` map external paths to internal routes in production.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI samples early, while `<rewrite-uri>` + `<set-backend-service>` map external paths to internal routes in production.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI samples early, while `<rewrite-uri>` + `<set-backend-service>` map external paths to internal routes in production.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI samples early, while `<rewrite-uri>` + `<set-backend-service>` map external paths to internal routes in production.

### Question 69 — C

Answer: Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation. `AuthorizationLevel.Function` enforces function-key or host-key validation via `x-functions-key`, matching APIM's automated Function import credential binding. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `AuthorizationLevel.Function` enforces function-key or host-key validation via `x-functions-key`, matching APIM's automated Function import credential binding.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `AuthorizationLevel.Function` enforces function-key or host-key validation via `x-functions-key`, matching APIM's automated Function import credential binding.
- **C:** Correct. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. In this scenario: `AuthorizationLevel.Function` enforces function-key or host-key validation via `x-functions-key`, matching APIM's automated Function import credential binding.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `AuthorizationLevel.Function` enforces function-key or host-key validation via `x-functions-key`, matching APIM's automated Function import credential binding.

### Question 70 — B

Answer: Enable Managed Identity on the APIM instance → grant that identity RBAC or app-role access on the target backend/Key Vault → add authentication-managed-identity in APIM policy XML → test backend calls and inspect APIM trace headers. Enabling Managed Identity on APIM, granting that identity the target backend app role/RBAC, adding `<authentication-managed-identity>` in `<inbound>`, and testing via APIM trace completes migration safely. APIM needs an active managed identity and target RBAC/app-role grant before `<authentication-managed-identity>` can mint valid Entra bearer tokens. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Hardcoding static secrets in policy XML creates rotation debt when `<authentication-managed-identity>` handles token lifecycle natively. Why the keyed choice wins: Enabling Managed Identity on APIM, granting that identity the target backend app role/RBAC, adding `<authentication-managed-identity>` in `<inbound>`, and testing via APIM trace completes migration safely.
- **B:** Correct. APIM needs an active managed identity and target RBAC/app-role grant before `<authentication-managed-identity>` can mint valid Entra bearer tokens. In this scenario: Enabling Managed Identity on APIM, granting that identity the target backend app role/RBAC, adding `<authentication-managed-identity>` in `<inbound>`, and testing via APIM trace completes migration safely.
- **C:** Incorrect for this requirement. Saving or invoking `<authentication-managed-identity>` before enabling Managed Identity and target RBAC fails token acquisition or returns 401/403. Why the keyed choice wins: Enabling Managed Identity on APIM, granting that identity the target backend app role/RBAC, adding `<authentication-managed-identity>` in `<inbound>`, and testing via APIM trace completes migration safely.
- **D:** Incorrect for this requirement. Backend authorization checks the APIM gateway managed identity, not the developer workstation, and `<validate-jwt>` validates caller tokens in `<inbound>`. Why the keyed choice wins: Enabling Managed Identity on APIM, granting that identity the target backend app role/RBAC, adding `<authentication-managed-identity>` in `<inbound>`, and testing via APIM trace completes migration safely.

### Question 71 — C, D

Answers: Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers; Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`. Enforcing Product Subscription Keys + `context.Request.Certificate.Thumbprint` checks alongside `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) blocks invalid TPP calls at the gateway. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Enforcing Product Subscription Keys + `context.Request.Certificate.Thumbprint` checks alongside `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) blocks invalid TPP calls at the gateway.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Enforcing Product Subscription Keys + `context.Request.Certificate.Thumbprint` checks alongside `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) blocks invalid TPP calls at the gateway.
- **C:** Correct. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. In this scenario: Enforcing Product Subscription Keys + `context.Request.Certificate.Thumbprint` checks alongside `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) blocks invalid TPP calls at the gateway.
- **D:** Correct. Combining gateway `<validate-jwt>` pre-authentication with subscription scoping and client-certificate thumbprint checks blocks invalid traffic before hitting backends. In this scenario: Enforcing Product Subscription Keys + `context.Request.Certificate.Thumbprint` checks alongside `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) blocks invalid TPP calls at the gateway.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Enforcing Product Subscription Keys + `context.Request.Certificate.Thumbprint` checks alongside `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) blocks invalid TPP calls at the gateway.

### Question 72 — C

Answer: Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`. `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` configured with `<openid-config>`, `<audiences>`, and `<required-claims>` validates JWT signatures and claims pre-backend. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` configured with `<openid-config>`, `<audiences>`, and `<required-claims>` validates JWT signatures and claims pre-backend.
- **B:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` configured with `<openid-config>`, `<audiences>`, and `<required-claims>` validates JWT signatures and claims pre-backend.
- **C:** Correct. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. In this scenario: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` configured with `<openid-config>`, `<audiences>`, and `<required-claims>` validates JWT signatures and claims pre-backend.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` configured with `<openid-config>`, `<audiences>`, and `<required-claims>` validates JWT signatures and claims pre-backend.

### Question 73 — C, E, F

Answers: Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`; Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`; Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`. `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three capabilities. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three capabilities.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three capabilities.
- **C:** Correct. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three capabilities.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three capabilities.
- **E:** Correct. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three capabilities.
- **F:** Correct. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three capabilities.

### Question 74 — C

Answer: Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`. Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` stores backend responses in the APIM cache. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` stores backend responses in the APIM cache.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` stores backend responses in the APIM cache.
- **C:** Correct. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. In this scenario: Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` stores backend responses in the APIM cache.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` stores backend responses in the APIM cache.

### Question 75 — A

Answer: Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`. Place `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` wrapping `<forward-request />` in `<backend>`, and `<set-header name="X-AspNet-Version" exists-action="delete" />` in `<outbound>`. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. In this scenario: Place `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` wrapping `<forward-request />` in `<backend>`, and `<set-header name="X-AspNet-Version" exists-action="delete" />` in `<outbound>`.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Place `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` wrapping `<forward-request />` in `<backend>`, and `<set-header name="X-AspNet-Version" exists-action="delete" />` in `<outbound>`.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Place `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` wrapping `<forward-request />` in `<backend>`, and `<set-header name="X-AspNet-Version" exists-action="delete" />` in `<outbound>`.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Place `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` wrapping `<forward-request />` in `<backend>`, and `<set-header name="X-AspNet-Version" exists-action="delete" />` in `<outbound>`.

### Question 76 — A

Answer: Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization. An Azure Event Grid Domain manages thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization. Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures. In this scenario: An Azure Event Grid Domain manages thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: An Azure Event Grid Domain manages thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization.
- **C:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: An Azure Event Grid Domain manages thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: An Azure Event Grid Domain manages thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization.

### Question 77 — C, D

Answers: Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL; Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization. Event Grid Domains isolate thousands of tenant topics behind one endpoint with RBAC, while `CloudEvents v1.0` subscriptions with subject/advanced filters and Blob dead-lettering ensure reliable push delivery. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Event Grid Domains isolate thousands of tenant topics behind one endpoint with RBAC, while `CloudEvents v1.0` subscriptions with subject/advanced filters and Blob dead-lettering ensure reliable push delivery.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Event Grid Domains isolate thousands of tenant topics behind one endpoint with RBAC, while `CloudEvents v1.0` subscriptions with subject/advanced filters and Blob dead-lettering ensure reliable push delivery.
- **C:** Correct. Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures. In this scenario: Event Grid Domains isolate thousands of tenant topics behind one endpoint with RBAC, while `CloudEvents v1.0` subscriptions with subject/advanced filters and Blob dead-lettering ensure reliable push delivery.
- **D:** Correct. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. In this scenario: Event Grid Domains isolate thousands of tenant topics behind one endpoint with RBAC, while `CloudEvents v1.0` subscriptions with subject/advanced filters and Blob dead-lettering ensure reliable push delivery.
- **E:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Event Grid Domains isolate thousands of tenant topics behind one endpoint with RBAC, while `CloudEvents v1.0` subscriptions with subject/advanced filters and Blob dead-lettering ensure reliable push delivery.

### Question 78 — C

Answer: Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`. Inspecting for `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` completes ownership validation. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Inspecting for `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` completes ownership validation.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Inspecting for `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` completes ownership validation.
- **C:** Correct. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. In this scenario: Inspecting for `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` completes ownership validation.
- **D:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Inspecting for `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` completes ownership validation.

### Question 79 — C

Answer: Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL. Setting `subjectBeginsWith: "/corridor/swift/"`, `advancedFilters` (`NumberGreaterThan` on `data.amountUsd`), retry TTL, and a dead-letter Blob container filters at the broker and preserves exhausted deliveries. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Setting `subjectBeginsWith: "/corridor/swift/"`, `advancedFilters` (`NumberGreaterThan` on `data.amountUsd`), retry TTL, and a dead-letter Blob container filters at the broker and preserves exhausted deliveries.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `subjectBeginsWith: "/corridor/swift/"`, `advancedFilters` (`NumberGreaterThan` on `data.amountUsd`), retry TTL, and a dead-letter Blob container filters at the broker and preserves exhausted deliveries.
- **C:** Correct. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. In this scenario: Setting `subjectBeginsWith: "/corridor/swift/"`, `advancedFilters` (`NumberGreaterThan` on `data.amountUsd`), retry TTL, and a dead-letter Blob container filters at the broker and preserves exhausted deliveries.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `subjectBeginsWith: "/corridor/swift/"`, `advancedFilters` (`NumberGreaterThan` on `data.amountUsd`), retry TTL, and a dead-letter Blob container filters at the broker and preserves exhausted deliveries.

### Question 80 — D

Answer: Create the Event Hub, consumer group, and Blob checkpoint container → instantiate BlobContainerClient and EventProcessorClient → register ProcessEventAsync (calling UpdateCheckpointAsync) and ProcessErrorAsync → call StartProcessingAsync before StopProcessingAsync. Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly. `EventProcessorClient` coordinates partition ownership and offset checkpoints in Blob Storage and requires both event and error handlers registered prior to `StartProcessingAsync`. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `EventProcessorClient` throws `InvalidOperationException` if started before registering both `ProcessEventAsync` and `ProcessErrorAsync`. Why the keyed choice wins: Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly.
- **B:** Incorrect for this requirement. Producers publish events and never hold partition checkpoints; `EventProcessorClient` handles balanced consumer checkpointing. Why the keyed choice wins: Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly.
- **C:** Incorrect for this requirement. Sharing one consumer group and checkpoint prefix across distinct apps causes them to steal partitions from each other instead of each reading the full stream. Why the keyed choice wins: Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly.
- **D:** Correct. `EventProcessorClient` coordinates partition ownership and offset checkpoints in Blob Storage and requires both event and error handlers registered prior to `StartProcessingAsync`. In this scenario: Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly.

### Question 81 — A

Answer: Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2. Azure Event Hubs with four separate Consumer Groups plus Event Hubs Capture writing directly to ADLS Gen2 isolates reader offsets and automates cold archival. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. In this scenario: Azure Event Hubs with four separate Consumer Groups plus Event Hubs Capture writing directly to ADLS Gen2 isolates reader offsets and automates cold archival.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Azure Event Hubs with four separate Consumer Groups plus Event Hubs Capture writing directly to ADLS Gen2 isolates reader offsets and automates cold archival.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Azure Event Hubs with four separate Consumer Groups plus Event Hubs Capture writing directly to ADLS Gen2 isolates reader offsets and automates cold archival.
- **D:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Azure Event Hubs with four separate Consumer Groups plus Event Hubs Capture writing directly to ADLS Gen2 isolates reader offsets and automates cold archival.

### Question 82 — C

Answer: Host `EventProcessorClient` backed by `BlobContainerClient` and call `await eventArgs.UpdateCheckpointAsync()` after idempotent batch persistence so partition leases resume cleanly after rebalancing. Calling `await eventArgs.UpdateCheckpointAsync()` after idempotent persistence records the partition offset in Blob metadata so new lease owners resume accurately. `EventProcessorClient` coordinates partition ownership via Azure Blob leases and records per-partition sequence/offset checkpoints in Blob metadata. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Calling `await eventArgs.UpdateCheckpointAsync()` after idempotent persistence records the partition offset in Blob metadata so new lease owners resume accurately.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Calling `await eventArgs.UpdateCheckpointAsync()` after idempotent persistence records the partition offset in Blob metadata so new lease owners resume accurately.
- **C:** Correct. `EventProcessorClient` coordinates partition ownership via Azure Blob leases and records per-partition sequence/offset checkpoints in Blob metadata. In this scenario: Calling `await eventArgs.UpdateCheckpointAsync()` after idempotent persistence records the partition offset in Blob metadata so new lease owners resume accurately.
- **D:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Calling `await eventArgs.UpdateCheckpointAsync()` after idempotent persistence records the partition offset in Blob metadata so new lease owners resume accurately.

### Question 83 — A

Answer: Create the queue or subscription with RequiresSession = true at creation time → send ServiceBusMessage instances setting a non-empty SessionId → create a ServiceBusSessionProcessor (or AcceptNextSessionAsync receiver) → process messages in order and complete/renew session locks. Creating the queue with `RequiresSession = true` at creation time, populating `SessionId = ibanAccount` on every message, and consuming via `ServiceBusSessionProcessor` enforces per-IBAN FIFO ordering. `RequiresSession` can only be enabled when creating the entity, producers must populate `SessionId`, and consumers must use session-aware receivers/processors. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. `RequiresSession` can only be enabled when creating the entity, producers must populate `SessionId`, and consumers must use session-aware receivers/processors. In this scenario: Creating the queue with `RequiresSession = true` at creation time, populating `SessionId = ibanAccount` on every message, and consuming via `ServiceBusSessionProcessor` enforces per-IBAN FIFO ordering.
- **B:** Incorrect for this requirement. Entity creation precedes processor connection, and session queues reject messages lacking a `SessionId`. Why the keyed choice wins: Creating the queue with `RequiresSession = true` at creation time, populating `SessionId = ibanAccount` on every message, and consuming via `ServiceBusSessionProcessor` enforces per-IBAN FIFO ordering.
- **C:** Incorrect for this requirement. `RequiresSession` is immutable after creation, messages without `SessionId` are rejected on session queues, and non-session receivers fail. Why the keyed choice wins: Creating the queue with `RequiresSession = true` at creation time, populating `SessionId = ibanAccount` on every message, and consuming via `ServiceBusSessionProcessor` enforces per-IBAN FIFO ordering.
- **D:** Incorrect for this requirement. Azure Queue Storage does not support brokered `SessionId` FIFO locks; Azure Service Bus session entities are required. Why the keyed choice wins: Creating the queue with `RequiresSession = true` at creation time, populating `SessionId = ibanAccount` on every message, and consuming via `ServiceBusSessionProcessor` enforces per-IBAN FIFO ordering.

### Question 84 — B, E

Answers: Use Azure Service Bus Topics with `SqlRuleFilter` / `CorrelationRuleFilter` (`CorrelationRuleFilter` preferred for high throughput) and `SqlRuleAction` header stamping, inspecting `$DeadLetterQueue` (`SubQueue.DeadLetter`) after `MaxDeliveryCount` expires; Use `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false`, calling `CompleteMessageAsync` after commit, `AbandonMessageAsync` for transient retries, and `DeadLetterMessageAsync` on unrecoverable schema errors. Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route high-speed filtered copies and isolate poison messages, while `PeekLock` (`AutoCompleteMessages = false`) guarantees at-least-once broker durability. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route high-speed filtered copies and isolate poison messages, while `PeekLock` (`AutoCompleteMessages = false`) guarantees at-least-once broker durability.
- **B:** Correct. `ReceiveAndDelete` loses messages if a worker crashes mid-processing; `PeekLock` retains broker durability until explicit settlement or lock expiry. In this scenario: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route high-speed filtered copies and isolate poison messages, while `PeekLock` (`AutoCompleteMessages = false`) guarantees at-least-once broker durability.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route high-speed filtered copies and isolate poison messages, while `PeekLock` (`AutoCompleteMessages = false`) guarantees at-least-once broker durability.
- **D:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route high-speed filtered copies and isolate poison messages, while `PeekLock` (`AutoCompleteMessages = false`) guarantees at-least-once broker durability.
- **E:** Correct. `CorrelationRuleFilter` matches brokered/application properties in-memory far faster than SQL evaluation, while `MaxDeliveryCount` isolates poison messages in the sub-queue DLQ. In this scenario: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route high-speed filtered copies and isolate poison messages, while `PeekLock` (`AutoCompleteMessages = false`) guarantees at-least-once broker durability.

### Question 85 — C

Answer: Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering. Enabling both `RequiresDuplicateDetection = true` (with a `DuplicateDetectionHistoryTimeWindow` >= 5 min) and `RequiresSession = true` deduplicates retries and preserves per-ATM FIFO order. Service Bus discards duplicate `MessageId` resends inside the history window and locks all messages sharing a `SessionId` to one active session receiver at a time. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Enabling both `RequiresDuplicateDetection = true` (with a `DuplicateDetectionHistoryTimeWindow` >= 5 min) and `RequiresSession = true` deduplicates retries and preserves per-ATM FIFO order.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Enabling both `RequiresDuplicateDetection = true` (with a `DuplicateDetectionHistoryTimeWindow` >= 5 min) and `RequiresSession = true` deduplicates retries and preserves per-ATM FIFO order.
- **C:** Correct. Service Bus discards duplicate `MessageId` resends inside the history window and locks all messages sharing a `SessionId` to one active session receiver at a time. In this scenario: Enabling both `RequiresDuplicateDetection = true` (with a `DuplicateDetectionHistoryTimeWindow` >= 5 min) and `RequiresSession = true` deduplicates retries and preserves per-ATM FIFO order.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling both `RequiresDuplicateDetection = true` (with a `DuplicateDetectionHistoryTimeWindow` >= 5 min) and `RequiresSession = true` deduplicates retries and preserves per-ATM FIFO order.

### Question 86 — A

Answer: Call `long seq = await sender.ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` and persist `seq` to call `CancelScheduledMessageAsync(seq)` if the user cancels early. `ScheduleMessageAsync` holds the wire invisible until `ScheduledEnqueueTime` and returns `seq` so `CancelScheduledMessageAsync(seq)` can revoke it cleanly. Service Bus native scheduled messages stay invisible until `ScheduledEnqueueTime` and can be canceled cleanly via their broker sequence number. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Service Bus native scheduled messages stay invisible until `ScheduledEnqueueTime` and can be canceled cleanly via their broker sequence number. In this scenario: `ScheduleMessageAsync` holds the wire invisible until `ScheduledEnqueueTime` and returns `seq` so `CancelScheduledMessageAsync(seq)` can revoke it cleanly.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `ScheduleMessageAsync` holds the wire invisible until `ScheduledEnqueueTime` and returns `seq` so `CancelScheduledMessageAsync(seq)` can revoke it cleanly.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `ScheduleMessageAsync` holds the wire invisible until `ScheduledEnqueueTime` and returns `seq` so `CancelScheduledMessageAsync(seq)` can revoke it cleanly.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `ScheduleMessageAsync` holds the wire invisible until `ScheduledEnqueueTime` and returns `seq` so `CancelScheduledMessageAsync(seq)` can revoke it cleanly.

### Question 87 — A

Answer: Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics. Azure Queue Storage scales up to the 500 TiB storage account capacity limit for messages <=64 KB, whereas Service Bus queues top out at 80 GB. Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub. Local study-map skill 5.8 (Implement Queue Workflows with Azure Queue Storage SDK, Visibility Leases, PopReceipts, and Poison Handling), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub. In this scenario: Azure Queue Storage scales up to the 500 TiB storage account capacity limit for messages <=64 KB, whereas Service Bus queues top out at 80 GB.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Azure Queue Storage scales up to the 500 TiB storage account capacity limit for messages <=64 KB, whereas Service Bus queues top out at 80 GB.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Azure Queue Storage scales up to the 500 TiB storage account capacity limit for messages <=64 KB, whereas Service Bus queues top out at 80 GB.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Azure Queue Storage scales up to the 500 TiB storage account capacity limit for messages <=64 KB, whereas Service Bus queues top out at 80 GB.

### Question 88 — B

Answer: Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`. `PeekMessagesAsync` neither hides messages from competing workers nor returns a `PopReceipt`; `ReceiveMessagesAsync(visibilityTimeout)` leases messages and supplies `MessageId` + `PopReceipt` for `DeleteMessageAsync` (with `DequeueCount` poison checks). `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. Local study-map skill 5.8 (Implement Queue Workflows with Azure Queue Storage SDK, Visibility Leases, PopReceipts, and Poison Handling), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `PeekMessagesAsync` neither hides messages from competing workers nor returns a `PopReceipt`; `ReceiveMessagesAsync(visibilityTimeout)` leases messages and supplies `MessageId` + `PopReceipt` for `DeleteMessageAsync` (with `DequeueCount` poison checks).
- **B:** Correct. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. In this scenario: `PeekMessagesAsync` neither hides messages from competing workers nor returns a `PopReceipt`; `ReceiveMessagesAsync(visibilityTimeout)` leases messages and supplies `MessageId` + `PopReceipt` for `DeleteMessageAsync` (with `DequeueCount` poison checks).
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `PeekMessagesAsync` neither hides messages from competing workers nor returns a `PopReceipt`; `ReceiveMessagesAsync(visibilityTimeout)` leases messages and supplies `MessageId` + `PopReceipt` for `DeleteMessageAsync` (with `DequeueCount` poison checks).
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `PeekMessagesAsync` neither hides messages from competing workers nor returns a `PopReceipt`; `ReceiveMessagesAsync(visibilityTimeout)` leases messages and supplies `MessageId` + `PopReceipt` for `DeleteMessageAsync` (with `DequeueCount` poison checks).

### Question 89 — A

Answer: Configure `[BlobTrigger(..., Source = BlobTriggerSource.EventGrid)]` with an Event Grid system topic subscription instead of default container-log polling. Configuring `Source = BlobTriggerSource.EventGrid` with an Event Grid `BlobCreated` subscription eliminates storage-log polling latency and idle transaction overhead. Event Grid-sourced blob triggers eliminate storage-log scan latency and work reliably on Blob-only / high-scale storage accounts. Local study-map skill 1.13 (Implement Function Triggers Using Cosmos DB/Blob Data Operations, NCRONTAB Timers, and Webhooks), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Event Grid-sourced blob triggers eliminate storage-log scan latency and work reliably on Blob-only / high-scale storage accounts. In this scenario: Configuring `Source = BlobTriggerSource.EventGrid` with an Event Grid `BlobCreated` subscription eliminates storage-log polling latency and idle transaction overhead.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Configuring `Source = BlobTriggerSource.EventGrid` with an Event Grid `BlobCreated` subscription eliminates storage-log polling latency and idle transaction overhead.
- **C:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Configuring `Source = BlobTriggerSource.EventGrid` with an Event Grid `BlobCreated` subscription eliminates storage-log polling latency and idle transaction overhead.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Configuring `Source = BlobTriggerSource.EventGrid` with an Event Grid `BlobCreated` subscription eliminates storage-log polling latency and idle transaction overhead.

### Question 90 — D

Answer: Query Workspace-based Application Insights (`AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces` or classic `requests`/`dependencies`/`exceptions`) joining on `OperationId` (`operation_Id`) to reconstruct end-to-end distributed transactions. W3C Trace-Context propagates `traceparent` into `OperationId` (`operation_Id`) across `AppRequests`, `AppDependencies`, `AppExceptions`, and `AppTraces` for end-to-end KQL joins. W3C Trace-Context propagates `traceparent` into `operation_Id` across services so KQL joins pinpoint exact failing downstream dependencies. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: W3C Trace-Context propagates `traceparent` into `OperationId` (`operation_Id`) across `AppRequests`, `AppDependencies`, `AppExceptions`, and `AppTraces` for end-to-end KQL joins.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: W3C Trace-Context propagates `traceparent` into `OperationId` (`operation_Id`) across `AppRequests`, `AppDependencies`, `AppExceptions`, and `AppTraces` for end-to-end KQL joins.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: W3C Trace-Context propagates `traceparent` into `OperationId` (`operation_Id`) across `AppRequests`, `AppDependencies`, `AppExceptions`, and `AppTraces` for end-to-end KQL joins.
- **D:** Correct. W3C Trace-Context propagates `traceparent` into `operation_Id` across services so KQL joins pinpoint exact failing downstream dependencies. In this scenario: W3C Trace-Context propagates `traceparent` into `OperationId` (`operation_Id`) across `AppRequests`, `AppDependencies`, `AppExceptions`, and `AppTraces` for end-to-end KQL joins.

### Question 91 — D

Answer: Provision Workspace-based Application Insights and copy APPLICATIONINSIGHTS_CONNECTION_STRING → configure UseAzureMonitor() OpenTelemetry distro at startup → verify requests/dependencies in Logs → create a KQL or metric alert linked to an Action Group. Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, wiring `UseAzureMonitor()`, verifying spans in Logs, and attaching an Action Group alert completes onboarding cleanly. Workspace-based Application Insights and connection-string OpenTelemetry setup emit telemetry first so KQL/metric alerts and Action Groups monitor real signals. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Classic Application Insights and bare Instrumentation Keys are retired in favor of Workspace-based resources and `APPLICATIONINSIGHTS_CONNECTION_STRING`. Why the keyed choice wins: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, wiring `UseAzureMonitor()`, verifying spans in Logs, and attaching an Action Group alert completes onboarding cleanly.
- **B:** Incorrect for this requirement. Alert queries require a target Application Insights / Log Analytics resource and instrumented telemetry emission. Why the keyed choice wins: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, wiring `UseAzureMonitor()`, verifying spans in Logs, and attaching an Action Group alert completes onboarding cleanly.
- **C:** Incorrect for this requirement. Zero telemetry rate and missing connection strings discard all telemetry before it reaches Azure Monitor. Why the keyed choice wins: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, wiring `UseAzureMonitor()`, verifying spans in Logs, and attaching an Action Group alert completes onboarding cleanly.
- **D:** Correct. Workspace-based Application Insights and connection-string OpenTelemetry setup emit telemetry first so KQL/metric alerts and Action Groups monitor real signals. In this scenario: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, wiring `UseAzureMonitor()`, verifying spans in Logs, and attaching an Action Group alert completes onboarding cleanly.

### Question 92 — B

Answer: Build and push the image to ACR with az acr build → create a user-assigned managed identity and grant AcrPull on the registry → create the Container Apps environment → create the container app referencing the identity and registry server. Provisioning the user-assigned identity, granting `AcrPull` on ACR, and passing `--user-assigned` plus `--registry-identity` on `az containerapp create` enables Managed Identity pulls from revision one. The image and AcrPull identity grant must exist before Container Apps pulls the image from ACR without admin credentials. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Role assignment cannot precede creating the managed identity, and the container app revision fails if the image has not been pushed. Why the keyed choice wins: Provisioning the user-assigned identity, granting `AcrPull` on ACR, and passing `--user-assigned` plus `--registry-identity` on `az containerapp create` enables Managed Identity pulls from revision one.
- **B:** Correct. The image and AcrPull identity grant must exist before Container Apps pulls the image from ACR without admin credentials. In this scenario: Provisioning the user-assigned identity, granting `AcrPull` on ACR, and passing `--user-assigned` plus `--registry-identity` on `az containerapp create` enables Managed Identity pulls from revision one.
- **C:** Incorrect for this requirement. Enabling admin passwords violates credential-free deployment, and revoking AcrPull breaks subsequent revision pulls. Why the keyed choice wins: Provisioning the user-assigned identity, granting `AcrPull` on ACR, and passing `--user-assigned` plus `--registry-identity` on `az containerapp create` enables Managed Identity pulls from revision one.
- **D:** Incorrect for this requirement. A container app cannot be created before its environment exists or pull an image before AcrPull and the image tag exist. Why the keyed choice wins: Provisioning the user-assigned identity, granting `AcrPull` on ACR, and passing `--user-assigned` plus `--registry-identity` on `az containerapp create` enables Managed Identity pulls from revision one.

### Question 93 — B

Answer: Configure a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0` and Managed Identity (`identity` property) so replicas scale to zero when idle and wake on queue depth. Configuring a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0`, `maxReplicas: 30`, and the user-assigned Managed Identity (`identity` property) wakes from zero without shared SAS connection strings. Container Apps uses KEDA scalers to scale down to zero on consumption/workload profiles and authenticate scalers cleanly via Managed Identity. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Configuring a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0`, `maxReplicas: 30`, and the user-assigned Managed Identity (`identity` property) wakes from zero without shared SAS connection strings.
- **B:** Correct. Container Apps uses KEDA scalers to scale down to zero on consumption/workload profiles and authenticate scalers cleanly via Managed Identity. In this scenario: Configuring a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0`, `maxReplicas: 30`, and the user-assigned Managed Identity (`identity` property) wakes from zero without shared SAS connection strings.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Configuring a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0`, `maxReplicas: 30`, and the user-assigned Managed Identity (`identity` property) wakes from zero without shared SAS connection strings.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Configuring a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0`, `maxReplicas: 30`, and the user-assigned Managed Identity (`identity` property) wakes from zero without shared SAS connection strings.

### Question 94 — B

Answer: Instantiate `new DefaultAzureCredential(new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId })` (or set `AZURE_CLIENT_ID`). Supplying `ManagedIdentityClientId` inside `DefaultAzureCredentialOptions` (or `AZURE_CLIENT_ID`) tells IMDS which attached user-assigned identity to select. When a host has multiple user-assigned managed identities attached, IMDS rejects ambiguous token requests unless the target `clientId` (or resource ID) is specified. Local study-map skill 3.7 (Implement System-Assigned and User-Assigned Managed Identities and DefaultAzureCredential), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Supplying `ManagedIdentityClientId` inside `DefaultAzureCredentialOptions` (or `AZURE_CLIENT_ID`) tells IMDS which attached user-assigned identity to select.
- **B:** Correct. When a host has multiple user-assigned managed identities attached, IMDS rejects ambiguous token requests unless the target `clientId` (or resource ID) is specified. In this scenario: Supplying `ManagedIdentityClientId` inside `DefaultAzureCredentialOptions` (or `AZURE_CLIENT_ID`) tells IMDS which attached user-assigned identity to select.
- **C:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Supplying `ManagedIdentityClientId` inside `DefaultAzureCredentialOptions` (or `AZURE_CLIENT_ID`) tells IMDS which attached user-assigned identity to select.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Supplying `ManagedIdentityClientId` inside `DefaultAzureCredentialOptions` (or `AZURE_CLIENT_ID`) tells IMDS which attached user-assigned identity to select.

### Question 95 — C

Answer: Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage. Combining locked time-based Version-Level Immutability Policies with a `LegalHold` tag blocks modification or deletion even by subscription owners until all holds clear and retention expires. Time-based locked retention and legal holds block modification and deletion even by Storage Account Owners until retention expires and holds clear. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Combining locked time-based Version-Level Immutability Policies with a `LegalHold` tag blocks modification or deletion even by subscription owners until all holds clear and retention expires.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Combining locked time-based Version-Level Immutability Policies with a `LegalHold` tag blocks modification or deletion even by subscription owners until all holds clear and retention expires.
- **C:** Correct. Time-based locked retention and legal holds block modification and deletion even by Storage Account Owners until retention expires and holds clear. In this scenario: Combining locked time-based Version-Level Immutability Policies with a `LegalHold` tag blocks modification or deletion even by subscription owners until all holds clear and retention expires.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Combining locked time-based Version-Level Immutability Policies with a `LegalHold` tag blocks modification or deletion even by subscription owners until all holds clear and retention expires.

### Question 96 — B

Answer: Use `container.CreateTransactionalBatch(new PartitionKey(pkValue))` to group multiple create/replace/upsert/delete operations atomically within the same logical partition. `container.CreateTransactionalBatch(new PartitionKey(accountNumber))` executes all operations serialized in one ACID transaction within that single logical partition, rolling back all changes if any step fails. `TransactionalBatch` guarantees ACID all-or-nothing execution serialized in one network round-trip, strictly scoped to a single logical partition key. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `container.CreateTransactionalBatch(new PartitionKey(accountNumber))` executes all operations serialized in one ACID transaction within that single logical partition, rolling back all changes if any step fails.
- **B:** Correct. `TransactionalBatch` guarantees ACID all-or-nothing execution serialized in one network round-trip, strictly scoped to a single logical partition key. In this scenario: `container.CreateTransactionalBatch(new PartitionKey(accountNumber))` executes all operations serialized in one ACID transaction within that single logical partition, rolling back all changes if any step fails.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `container.CreateTransactionalBatch(new PartitionKey(accountNumber))` executes all operations serialized in one ACID transaction within that single logical partition, rolling back all changes if any step fails.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `container.CreateTransactionalBatch(new PartitionKey(accountNumber))` executes all operations serialized in one ACID transaction within that single logical partition, rolling back all changes if any step fails.

### Question 97 — A

Answer: Call `await blobClient.CreateSnapshotAsync()` for explicit point-in-time read-only checkpoints or enable account-level Blob Versioning so every `UploadAsync` overwrite retains an immutable `VersionId`. Account-level Blob Versioning automatically preserves an immutable prior version (`VersionId`) on every overwrite or delete operation. Snapshots capture explicit developer-triggered checkpoints, whereas Blob Versioning automatically preserves prior state on every overwrite or delete. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Snapshots capture explicit developer-triggered checkpoints, whereas Blob Versioning automatically preserves prior state on every overwrite or delete. In this scenario: Account-level Blob Versioning automatically preserves an immutable prior version (`VersionId`) on every overwrite or delete operation.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Account-level Blob Versioning automatically preserves an immutable prior version (`VersionId`) on every overwrite or delete operation.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Account-level Blob Versioning automatically preserves an immutable prior version (`VersionId`) on every overwrite or delete operation.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Account-level Blob Versioning automatically preserves an immutable prior version (`VersionId`) on every overwrite or delete operation.

### Question 98 — A

Answer: Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`. Adding `<rate-limit-by-key calls="60" renewal-period="60" ... />` and `<quota-by-key calls="5000" renewal-period="2592000" ... />` alongside `<base />` inside `<inbound>` enforces both limits cleanly. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! In this scenario: Adding `<rate-limit-by-key calls="60" renewal-period="60" ... />` and `<quota-by-key calls="5000" renewal-period="2592000" ... />` alongside `<base />` inside `<inbound>` enforces both limits cleanly.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Adding `<rate-limit-by-key calls="60" renewal-period="60" ... />` and `<quota-by-key calls="5000" renewal-period="2592000" ... />` alongside `<base />` inside `<inbound>` enforces both limits cleanly.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Adding `<rate-limit-by-key calls="60" renewal-period="60" ... />` and `<quota-by-key calls="5000" renewal-period="2592000" ... />` alongside `<base />` inside `<inbound>` enforces both limits cleanly.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Adding `<rate-limit-by-key calls="60" renewal-period="60" ... />` and `<quota-by-key calls="5000" renewal-period="2592000" ... />` alongside `<base />` inside `<inbound>` enforces both limits cleanly.

### Question 99 — D

Answer: Enable Managed Identity with App Configuration Data Reader + Key Vault Secrets User → add Key Vault references and a sentinel key → wire AddAzureAppConfiguration with ConfigureKeyVault and ConfigureRefresh → invoke UseAzureAppConfiguration middleware. Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware enables live reload. RBAC on both stores is required because App Configuration stores only the URI pointer; `ConfigureRefresh` + middleware poll the sentinel key on incoming requests. Local study-map skill 3.5 (Manage Feature Flags, Labels, Sentinel Dynamic Refresh, and Key Vault References in Azure App Configuration), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Without Key Vault Secrets User on the vault itself, resolving a Key Vault reference throws 403 Forbidden at startup. Why the keyed choice wins: Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware enables live reload.
- **B:** Incorrect for this requirement. In ASP.NET Core, dynamic refresh is request-driven via `UseAzureAppConfiguration()` middleware (or manual `TryRefreshAsync`), not an automatic push without it. Why the keyed choice wins: Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware enables live reload.
- **C:** Incorrect for this requirement. Committing exported secret values defeats Key Vault reference rotation and violates secret hygiene. Why the keyed choice wins: Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware enables live reload.
- **D:** Correct. RBAC on both stores is required because App Configuration stores only the URI pointer; `ConfigureRefresh` + middleware poll the sentinel key on incoming requests. In this scenario: Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware enables live reload.

### Question 100 — C

Answer: Store environment-labeled settings and `.appconfig.featureflag/*` entries in Azure App Configuration, register `AddAzureAppConfiguration` + `AddFeatureManagement`, and watch a single `Sentinel` key with `refreshAll: true`. Registering `AddAzureAppConfiguration` + `AddFeatureManagement` while watching a single `Sentinel` key (`refreshAll: true`) evaluates percentage feature flags and reloads multi-key edits atomically. Updating one sentinel key after finishing multi-key edits prevents apps from reading half-updated configuration state mid-rollout. Local study-map skill 3.5 (Manage Feature Flags, Labels, Sentinel Dynamic Refresh, and Key Vault References in Azure App Configuration), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Registering `AddAzureAppConfiguration` + `AddFeatureManagement` while watching a single `Sentinel` key (`refreshAll: true`) evaluates percentage feature flags and reloads multi-key edits atomically.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Registering `AddAzureAppConfiguration` + `AddFeatureManagement` while watching a single `Sentinel` key (`refreshAll: true`) evaluates percentage feature flags and reloads multi-key edits atomically.
- **C:** Correct. Updating one sentinel key after finishing multi-key edits prevents apps from reading half-updated configuration state mid-rollout. In this scenario: Registering `AddAzureAppConfiguration` + `AddFeatureManagement` while watching a single `Sentinel` key (`refreshAll: true`) evaluates percentage feature flags and reloads multi-key edits atomically.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Registering `AddAzureAppConfiguration` + `AddFeatureManagement` while watching a single `Sentinel` key (`refreshAll: true`) evaluates percentage feature flags and reloads multi-key edits atomically.
