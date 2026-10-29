# Microsoft Exam AZ-204: Developing Solutions for Microsoft Azure — Full-Length Mock Exam 4

Exam AZ-204 (Connected Fleet IoT, Cold-Chain Logistics, and Port Customs) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Credential Lifecycle Notice:** Microsoft retired Exam AZ-204 (`Microsoft Certified: Azure Developer Associate`) on **July 31, 2026** and succeeded it with **Exam AI-200 (`Azure AI Cloud Developer Associate`)**. This practice bank preserves the final official January 14, 2026 AZ-204 skills-measured baseline for archival certification prep, enterprise Azure developer benchmarking, and core compute/storage/security/monitoring/integration mastery.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` SDK/CLI/XML/JSON/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area code dropdowns, split-pane tabbed case exhibits, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn documentation — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. A maritime AIS-tracking team is containerizing a .NET 8 vessel-telemetry receiver and requires minimal runtime image size without SDK compilers plus clean `SIGTERM` handling when pods drain. Which two Dockerfile practices should they combine? Select two.

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Declare `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form so `SIGTERM` reaches the .NET host cleanly during container shutdown
- C. Use a multi-stage Dockerfile building in `mcr.microsoft.com/dotnet/sdk:8.0` and copying published output into `mcr.microsoft.com/dotnet/aspnet:8.0` with a non-root `USER app`
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Keep the default `--restart-policy Always` on a run-once batch container group

### 2. Remote `az acr build` runs on a logistics monorepo take four minutes just uploading 2.4 GB of local test recordings, `bin/`, `obj/`, and `.git/` history. Which repository file stops streaming unneeded local files?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Add `bin/`, `obj/`, `.git/`, and local `.env` files to `.dockerignore` before running `docker build` or `az acr build`

### 3. An IoT gateway firmware team builds container images from locked-down developer VMs that lack local Docker Engine (`az acr ____ `). Which Azure CLI command compiles and pushes the Dockerfile remotely in Azure?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Run `az acr build --registry <acrName> --image app:{{.Run.ID}} .` to build and push the container image remotely using ACR Tasks without a local Docker daemon

### 4. Proposed solution: Launch an on-demand route-optimization container group in Azure Container Instances using the default `--restart-policy Always` so it stops billing after exiting with code `0`. Why does this waste budget, and what fixes it?

Domain: Develop Azure compute solutions

- A. Set `--restart-policy OnFailure` (or `Never`) on the Azure Container Instances container group so batch containers stop billing vCPU/memory seconds once exit code 0 completes
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 5. A port crane-telemetry parser on Linux ACI requires a local Fluent Bit log shipper reachable via `localhost` and access to a shared scratch volume without exposing internal ports externally. Which ACI deployment pattern works?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Deploy the application container and Envoy/logging sidecar inside one multi-container ACI group sharing `localhost` network namespace and an `emptyDir` / Azure Files volume

### 6. Every night at 01:00 UTC, a fleet-maintenance container must compute 16 parallel brake-wear forecasts and exit completely with zero open HTTP ingress ports. Which Azure Container Apps resource matches this workload?

Domain: Develop Azure compute solutions

- A. Deploy an Azure Container Apps Job (`triggerType: Event` or `Schedule`) with `replicaCompletionCount` and `parallelism` instead of an always-listening HTTP container app
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 7. Inside a port-logistics Container Apps environment, customs workers must scale to zero on Service Bus queue depth via Managed Identity, restrict Dapr state store access strictly to `berth-planner`, and load secrets from Key Vault without ARM plaintext strings. Which three Container Apps features apply? Select three.

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- C. Configure a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0` and Managed Identity (`identity` property) so replicas scale to zero when idle and wake on queue depth
- D. Define a Container App secret using `keyVaultUrl` plus `identity` (managed identity resource ID or `system`) and map container environment variables via `secretRef`
- E. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- F. Register a Dapr state or pub/sub component in the Container Apps environment and restrict access via the component `scopes` array to specific `daprAppId` values

### 8. A rail-signaling telemetry service must deploy into a VNet-injected Container Apps environment with no public external Envoy IP (` ____ `). Which Azure CLI command creates the environment?

Domain: Develop Azure compute solutions

- A. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Execute `az containerapp env create --name <envName> --resource-group <rg> --infrastructure-subnet-resource-id <subnetId> --internal-only`

### 9. A carrier bill-of-lading portal hosted on a `Basic (B2)` App Service plan now requires staging deployment slots with auto-swap and weekday CPU metric autoscale rules. Which plan change unlocks both features?

Domain: Develop Azure compute solutions

- A. Provision at least a `Standard` (`S1+`) or `Premium v3` (`P1v3+`) App Service plan to unlock deployment slots, custom domain SNI SSL, and metric/schedule autoscaling
- B. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 10. A containerized .NET 8 warehouse-slotting API switches to Microsoft's non-root runtime image (` ____ `) and needs container port `8080` aligned with Container Apps ingress. Which Dockerfile lines match the .NET 8 convention?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Set `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` inside the final `.NET 8` runtime stage and match `targetPort: 8080` on Container Apps ingress
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 11. Maritime safety regulators require 120 days of Web Server and Application logs from a scaled-out App Service vessel portal without 12-hour automatic filesystem shutoff. How should diagnostics be configured?

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 12. While troubleshooting an EDI-214 shipment webhook on Linux App Service, an engineer wants verbose live stdout streamed straight to their terminal (` ____ `). Which CLI commands achieve this?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`

### 13. Deploying updated binaries to a high-traffic parcel-tracking App Service app via WebDeploy occasionally fails with file-in-use locks on `wwwroot`. Which setting switches deployments to atomic read-only package mounting?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Set `WEBSITE_RUN_FROM_PACKAGE=1` and deploy with `az webapp deploy --type zip` so the app mounts the read-only ZIP package directly with atomic cold-start replacement

### 14. A dispatcher map SPA at `https://ops.strider.example` makes credentialed API requests to `https://api.strider.example` on App Service, which must also enforce HTTPS redirection and TLS 1.2+. Which two App Service settings are needed? Select two.

Domain: Develop Azure compute solutions

- A. Enable `httpsOnly: true`, set `minTlsVersion: "1.2"` (or `"1.3"`), and configure `clientCertEnabled` when mutual TLS client certificates are required
- B. Configure App Service `CORS` with explicit origin URLs (and `supportCredentials` only without wildcard `*`) so App Service handles preflight `OPTIONS` requests
- C. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 15. A port-berthing App Service app needs its `LedgerDb` SQL connection string configured and pinned to its slot via Azure CLI (` ____ `). Which command accomplishes both?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`

### 16. Morning courier-manifest uploads spike App Service CPU, and narrow autoscale rules (`>70%` out, `<67%` in, 1-min cooldown) cause worker counts to bounce up and down every three minutes. What rule redesign stops flapping?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Pair every scale-out metric rule (e.g., CPU > 75% for 10 min) with a conservative scale-in rule (e.g., CPU < 35%) and an explicit `coolDown` window plus safe default/max instance bounds
- D. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`

### 17. A route-graph App Service app loads a 600 MB road-network index into memory on startup; how can engineers guarantee slot swaps wait until `/warmup/graph` returns HTTP `200` on every worker?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- C. Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 18. A customs-portal engineer is rolling out v3.2 on App Service Premium P2v3 and must validate warm-up on `staging` while keeping live customs EDI endpoints pinned strictly to `Production`. Which sequence executes this cleanly?

Domain: Develop Azure compute solutions

- A. Deploy directly to production → create the staging slot → swap staging into production → mark settings as slot settings
- B. Swap staging into production → create the staging slot → deploy the build → mark settings as deployment slot settings
- C. Create the staging slot on a Free F1 plan → deploy the build → swap slots → mark settings sticky
- D. Create the staging deployment slot on the Standard/Premium Web App → mark production-only connection strings and webhook settings as deployment slot settings → deploy and warm up the new build in staging → swap staging into production and verify health

### 19. After swapping `staging` into `Production` on a fleet-telematics web app, production trucks begin posting GPS heartbeats to the staging sandbox broker URL. Which configuration prevents environment URLs from moving during swaps?

Domain: Develop Azure compute solutions

- A. Mark environment-specific settings such as `PaymentWebhookUrl` and production connection strings as `slotSetting: true` (Deployment slot setting) before swapping slots
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 20. A vessel-routing optimization Function takes 16 minutes per voyage batch, queries a private-endpoint PostgreSQL server inside a VNet, and requires pre-warmed workers. Which Azure Functions plan satisfies all three constraints?

Domain: Develop Azure compute solutions

- A. Host the Function App on `Flex Consumption` or `Elastic Premium (EP1+)` when VNet integration, longer execution timeouts beyond 10 minutes, or pre-warmed/always-ready instances are required
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 21. A logistics webhook Function App sets a 10-minute host timeout and excludes `Request` and `Exception` items from Application Insights adaptive sampling (`host.json`: ` ____ `). Which JSON snippet belongs in `host.json`?

Domain: Develop Azure compute solutions

- A. Configure `"functionTimeout": "00:10:00"` and `"logging": { "applicationInsights": { "samplingSettings": { "isEnabled": true, "excludedTypes": "Request;Exception" } } }` inside `host.json`
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`

### 22. A .NET 8 isolated-worker Function App ingests port gate scans: an HTTP trigger must write a Cosmos document and return HTTP 202 without `out` parameters, while an Event Hub trigger must retry transient DB timeouts 5 times with exponential backoff. Which two C# patterns apply? Select two.

Domain: Develop Azure compute solutions

- A. Apply `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` (or `[FixedDelayRetry]`) on the `[EventHubTrigger]` / `[TimerTrigger]` function
- B. In the .NET isolated worker model, return a custom POCO class uniting `[HttpResult]` (or `HttpResponseData`) with `[CosmosDBOutput]` / `[ServiceBusOutput]` properties
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 23. Every updated shipment-milestone document in Cosmos DB container `shipments` must trigger a C# Function (` ____ `) to push customer ETA notifications. Which trigger attribute wires the Cosmos DB Change Feed?

Domain: Develop Azure compute solutions

- A. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`

### 24. A depot yard-check `[TimerTrigger(" ____ ")]` Function must fire every 15 minutes from `09:00` through `17:45` UTC on weekdays (`Mon–Fri`). Which six-field NCRONTAB expression configures this schedule?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Specify a six-field NCRONTAB expression `{second} {minute} {hour} {day} {month} {day-of-week}` such as `"0 */15 9-17 * * 1-5"` on `[TimerTrigger]`
- D. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`

### 25. Drivers upload 90,000 proof-of-delivery signature PNGs per hour to Blob Storage, and default log-scanning `[BlobTrigger]` Functions lag by six minutes. Which trigger change delivers sub-second push invocation?

Domain: Develop Azure compute solutions

- A. Configure `[BlobTrigger(..., Source = BlobTriggerSource.EventGrid)]` with an Event Grid system topic subscription instead of default container-log polling
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 26. A global telematics SaaS on Cosmos DB for NoSQL has mega-carrier `/tenantId` partitions exceeding 20 GB, queries frequently by `/tenantId` + `/siteId`, commits multi-item trip summaries atomically within one partition key, and guards concurrent dispatch edits via ETags. Which three Cosmos DB features solve all of these? Select three.

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use `container.CreateTransactionalBatch(new PartitionKey(pkValue))` to group multiple create/replace/upsert/delete operations atomically within the same logical partition
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Pass `new ItemRequestOptions { IfMatchEtag = item.ETag }` on `ReplaceItemAsync` and catch `CosmosException` when `StatusCode == HttpStatusCode.PreconditionFailed` (412)
- E. Define `new ContainerProperties(id: "telemetry", partitionKeyPaths: new List<string> { "/tenantId", "/siteId", "/deviceId" })` using `PartitionKeyBuilder` on reads and writes
- F. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 27. Refrigerated trailers write 25 KB sensor payloads to Cosmos DB every 10 seconds, queried solely by `/customerId` (carrier ID) and `/createdUtc`, and indexing all 140 nested sensor fields wastes write RUs (` ____ `). How should the indexing policy be optimized?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Configure `"indexingMode": "consistent"` with `"includedPaths": [{"path": "/customerId/?"}, {"path": "/createdUtc/?"}]` and `"excludedPaths": [{"path": "/*"}]`
- D. Add a `compositeIndexes` array matching the exact property sequence and sort directions (`ascending` / `descending`) in the container indexing policy JSON

### 28. When a customs hub scans a container seal, the API only needs to increment `/retryCount` and set `/lastStatus` on a 150 KB voyage document in Cosmos DB (`await container. ____ `). Which SDK method mutates just those paths server-side?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `await container.PatchItemAsync<Order>(id, new PartitionKey(pk), new[] { PatchOperation.Increment("/retryCount", 1), PatchOperation.Set("/lastStatus", "Queued") })`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction

### 29. Dispatchers execute `SELECT * FROM c WHERE c.depotId = @d ORDER BY c.priority ASC, c.etaUtc DESC` in Cosmos DB for NoSQL and receive a missing composite index error. How must the indexing policy be updated?

Domain: Develop for Azure storage

- A. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Add a `compositeIndexes` array matching the exact property sequence and sort directions (`ascending` / `descending`) in the container indexing policy JSON
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 30. A yard manager reassigns a trailer dock in a web app backed by Cosmos DB and immediately refreshes the dock board via another stateless API replica; how is read-your-own-writes guaranteed at minimal RU cost?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Use `Session` consistency (the default) and propagate `x-ms-session-token` (`RequestOptions.SessionToken`) across client/middle-tier hops to guarantee monotonic read-your-own-writes at half the read RU cost of `Strong`
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 31. Port operations centers in Hamburg and Busan read a replicated Cosmos DB vessel schedule and require globally ordered reads lagging the primary write region by at most `T = 10` seconds or `K = 500` updates. Which consistency level fits?

Domain: Develop for Azure storage

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency
- D. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction

### 32. A customs-audit worker written in .NET 8 must stream every manifest insert and update from Cosmos DB using the Change Feed Processor builder. Which ordered sequence sets up and starts the processor?

Domain: Develop for Azure storage

- A. Create only the monitored container → call Build and StartAsync → attach WithLeaseContainer → define the handler delegate
- B. Call StartAsync on the processor → call GetChangeFeedProcessorBuilder<T> → create the lease container → attach WithInstanceName
- C. Create the monitored container and a dedicated lease container → call GetChangeFeedProcessorBuilder<T> with processorName and delegate → attach WithInstanceName and WithLeaseContainer → call Build and StartAsync on the processor
- D. Attach WithLeaseContainer pointing to the monitored container without /id partition → call StartAsync → call GetChangeFeedProcessorBuilder<T> → call Build

### 33. Both a carbon-emissions calculator and a carrier-billing worker must consume every Cosmos DB trip change independently, and cancelled deleted draft trips must also trigger downstream cleanup. Which two Change Feed designs apply? Select two.

Domain: Develop for Azure storage

- A. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- E. Use Change Feed `AllVersionsAndDeletes` mode (or soft-delete flag items with short TTL in `LatestVersion` mode) because default `LatestVersion` change feed omits hard-deleted items

### 34. Ephemeral GPS breadcrumbs in Cosmos DB specify `"ttl": 86400`, while permanent geofence definitions in the same container omit `"ttl"`; currently nothing expires because `DefaultTimeToLive` is `null`. What container setting fixes this?

Domain: Develop for Azure storage

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Enable container `DefaultTimeToLive = -1` (or positive seconds) and set item `ttl = 600` so Cosmos DB purges expired items automatically using background RU capacity

### 35. Proposed solution: Save `port=NLRTM` and `status=pending` inside Blob `Metadata` across 30 million customs PDFs and filter server-side without listing containers. Why does this fail, and what replaces it?

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Attach searchable key-value `Tags` (`SetTagsAsync` / `BlobUploadOptions.Tags`) and query across containers with `FindBlobsByTagsAsync("@container = 'docs' AND status = 'pending'")`
- D. Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`)

### 36. An EDI uploader stores bill-of-lading blobs and needs to set `Content-Type: application/xml` plus custom `voyage_code` user metadata (`x-ms-meta-voyage_code`) via `Azure.Storage.Blobs` (` ____ `). Which SDK calls apply both?

Domain: Develop for Azure storage

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`)
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 37. Before running an automated OCR rewrite on a hazmat declaration blob, the pipeline takes a read-only point-in-time checkpoint (`await blobClient. ____ `) and also wants account-wide overwrite history. Which capabilities apply?

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `await blobClient.CreateSnapshotAsync()` for explicit point-in-time read-only checkpoints or enable account-level Blob Versioning so every `UploadAsync` overwrite retains an immutable `VersionId`

### 38. A rail-video archiver replicates 3 TB of locomotive forward-camera MP4 blobs to a cold disaster-recovery storage account (`await destBlob. ____ `) without streaming video through worker memory. Which SDK method performs this?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Invoke `BlobClient.StartCopyFromUriAsync(sourceSasUri)` to trigger asynchronous server-side blob copy and inspect `CopyStatus` without streaming bytes through the client VM
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 39. A customs broker API creates a 15-minute HTTPS-only read link scoped solely to blob `exports/manifest.csv` (`new BlobSasBuilder { ____ }`). Which builder properties enforce single-blob read-only access?

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 40. Maritime voyage data-recorder logs in Blob Storage must auto-tier from `Hot` to `Cool` at 30 days and `Archive` at 180 days, while accident-investigation blobs must remain WORM-locked against deletion by any admin. Which two Blob features satisfy both needs? Select two.

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`)
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage
- E. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 41. Refrigerated-trailer CSV logs under `reefer-logs/` have `AccessTracking` enabled and must move automatically to `Cool` whenever unread for 30 days (`daysAfterLastAccessTimeGreaterThan`) without custom scripts. Which Blob Storage feature automates this?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`)

### 42. Coast Guard inspectors demand a 4 GB archived port-radar log from `Archive` tier within one hour (`await blobClient. ____ `). Which SDK call initiates fastest restoration?

Domain: Develop for Azure storage

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob)

### 43. Ruggedized Android cab tablets run a .NET MAUI driver app authenticating with Microsoft Entra ID and refreshing dispatch API tokens silently across 11-hour drives without repeated sign-in popups. Which two MSAL patterns apply? Select two.

Domain: Implement Azure security

- A. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 44. An unattended customs-tariff sync service runs nightly on Linux using a client certificate and requests app-only tokens for `api://tariffs/.default` (` ____ `). Which MSAL builder and method fit this daemon?

Domain: Implement Azure security

- A. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- B. Use `ConfidentialClientApplicationBuilder` authenticated with a client certificate (or workload identity assertion) calling `AcquireTokenForClient(new[] { "api://.../.default" })` for headless background daemons
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 45. A yard-master desktop app calls MSAL `AcquireTokenInteractive` on every single REST call, annoying operators with browser flashes (`await pca. ____ `). How should token acquisition be refactored?

Domain: Implement Azure security

- A. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- B. Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 46. A port-crane override API (`[Authorize(Roles = "CraneSupervisor")]`) must authorize both human terminal supervisors and an automated storm-lockdown service principal. How must `CraneSupervisor` be defined in Entra ID?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Declare `appRoles` with `allowedMemberTypes: ["User", "Application"]` in the Entra app registration manifest and validate the `roles` claim (`[Authorize(Roles = "...")]`) in the web API
- D. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)

### 47. A freight-forwarding portal allows logistics coordinators from 400 partner carrier Entra tenants to sign in while blocking consumer `@live.com` accounts and uncontracted `tid` tenants. How should authentication be configured?

Domain: Implement Azure security

- A. Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 48. Driver mobile apps need 10-minute HTTPS upload URLs for damaged-cargo photos minted by an API using Microsoft Entra credentials because storage account Shared Keys are disabled. Which ordered steps generate the SAS?

Domain: Implement Azure security

- A. Build BlobSasBuilder and sign → call GetUserDelegationKeyAsync → instantiate BlobServiceClient with shared account key → assign RBAC to the identity
- B. Call GetUserDelegationKeyAsync anonymously → build BlobSasBuilder → assign RBAC to the identity → instantiate BlobServiceClient
- C. Assign Storage Blob Data Contributor/Delegator RBAC to the identity → instantiate BlobServiceClient with DefaultAzureCredential → call GetUserDelegationKeyAsync for a bounded validity window → build BlobSasBuilder and sign with the user delegation key
- D. Instantiate BlobServiceClient with SAS token → assign RBAC → build BlobSasBuilder → call GetUserDelegationKeyAsync

### 49. External drayage carriers use a Service SAS to upload manifests into container `drayage-inbox`; how can port security revoke one carrier's SAS immediately without rotating storage account keys?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Bind a Service SAS to a container/queue/table Stored Access Policy (`SignedIdentifier`, omitting inline start/expiry/permissions) so compromised tokens can be revoked instantly by modifying or deleting the policy
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 50. Proposed solution: Sign partner Blob download URLs using an Account SAS backed by `accountKey2` on a storage account where security policy mandates `allowSharedKeyAccess: false`. Why does this fail, and which SAS works?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Mint a short-lived HTTPS-only (`SasProtocol.HttpsOnly`) User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` instead of Account or Service SAS signed with storage account keys
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 51. A depot roster tool syncs 22,000 drivers from Microsoft Graph and fetches 16 depot calendar views per screen load without over-privileged scopes or HTTP `429` failures. Which two Graph SDK patterns apply? Select two.

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses
- D. Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`
- E. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 52. Using Microsoft Graph .NET SDK v5, a fleet directory sync queries active drivers (`accountEnabled eq true`) projecting solely `id`, `displayName`, and `mail` (`await graphClient.Users.GetAsync( ____ )`). Which lambda completes the call?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Call `await graphClient.Users.GetAsync(rc => { rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }; rc.QueryParameters.Filter = "accountEnabled eq true"; })`
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 53. Inside a middle-tier customs-clearance API that received a broker's Entra bearer token, which MSAL C# call exchanges it for a delegated Microsoft Graph `Mail.Send` token (` ____ `)?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `await confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` inside the middle-tier API
- D. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps

### 54. Fleet operations updates five dynamic toll-routing thresholds in Azure App Configuration and needs running .NET 8 services to reload all five atomically without seeing half-edited rules. Which pattern guarantees atomic refresh?

Domain: Implement Azure security

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Store environment-labeled settings and `.appconfig.featureflag/*` entries in Azure App Configuration, register `AddAzureAppConfiguration` + `AddFeatureManagement`, and watch a single `Sentinel` key with `refreshAll: true`
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 55. A cold-chain telemetry API loads settings and Key Vault secret references from Azure App Configuration (`options.Connect(uri, cred). ____ `), failing at startup until Key Vault resolution is wired. What call completes startup?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Wire `options.Connect(new Uri(endpoint), cred).ConfigureKeyVault(kv => kv.SetCredential(cred))` so App Configuration resolves Key Vault reference items using the app identity
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 56. Locomotive black-box archives are encrypted locally with a random symmetric AES DEK (`dekBytes`) whose bytes must be wrapped with an HSM-backed RSA key in Azure Key Vault (` ____ `). Which SDK client and method perform this?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Instantiate `new CryptographyClient(keyVaultKey.Id, new DefaultAzureCredential())` and invoke `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync(...)`
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 57. A customs EDI web app on Azure App Service reads `Environment.GetEnvironmentVariable("CustomsSftpKey")` and wants rotated Key Vault secrets injected without adding Key Vault SDK code (` ____ `). Which app setting format works?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Configure App Service / Functions application settings using `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` (omitting secret version) paired with `Key Vault Secrets User` on the app Managed Identity
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 58. Forty short-lived ACI vessel-simulation groups spin up and tear down daily and must all share one pre-provisioned Entra identity authorized on Blob Storage and Event Hubs without re-granting RBAC on every run. Which identity type fits?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Choose a User-Assigned Managed Identity when multiple compute resources must share one pre-provisioned identity lifecycle independent of individual app deletions; choose System-Assigned when 1-to-1 fate-sharing tied to a single resource is required

### 59. Port dispatchers see sporadic HTTP 500 errors on `POST /berths/assign`, and SREs need end-to-end W3C trace correlation plus a KQL inner join linking failed `AppRequests` to failing downstream `AppDependencies`. Which two Application Insights practices solve this? Select two.

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Query Workspace-based Application Insights (`AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces` or classic `requests`/`dependencies`/`exceptions`) joining on `OperationId` (`operation_Id`) to reconstruct end-to-end distributed transactions
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- E. Run `AppRequests | where ResultCode == "500" | join kind=inner (AppDependencies | where Success == false) on OperationId | project TimeGenerated, Name, Target, DependencyType, ResultCode1`

### 60. A fleet telemetry wallboard needs 5-minute buckets over the last hour showing request failure counts and p95 latency per API route in Workspace-based Application Insights (` ____ `). Which KQL query computes these metrics?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Run `AppRequests | where TimeGenerated > ago(1h) | summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)`

### 61. Proposed solution: Let a 7-second Container Apps Job exit `Main()` immediately after calling `TrackEvent("ManifestFiled")` without flushing buffers. Why are final events missing in Application Insights, and what fixes it?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 62. Engineers running `UseAzureMonitor()` on a .NET 8 route-solver API want custom child spans around `SolveVehicleRouting` (`using var span = ____ `) to appear in Application Insights Transaction Search. Which instrumentation pattern works?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 63. Mariner PortOps wants multi-region synthetic HTTPS probes validating SSL certificate expiration and HTTP 200 status on `https://edi.marinerport.example`, alerting only if two or more regions fail simultaneously. Which setup meets this?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 64. Parcel-hub scan volume surges every weekday evening at 18:00 and drops on Sundays, making static latency alerts noisy, and triggered alerts must invoke an Azure Function pager webhook. Which alert rule design fits best?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Create an Azure Monitor Metric Alert (Dynamic Thresholds or static p95 latency/5xx count) or Scheduled Query (KQL) Alert targeting an Action Group configured with webhook / Azure Function / email-SMS receivers
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 65. A rail-yard PLC gateway sits inside an air-gapped private VNet unreachable from public Azure Monitor POPs, yet SREs need synthetic availability telemetry inside Application Insights. How should probes be implemented?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 66. Zephyr Parcel is instrumenting a new .NET 8 hub-sorter API onto Workspace-based Application Insights with OpenTelemetry and automated failure alerts. Which ordered rollout sequence follows Microsoft Learn guidance?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Provision Workspace-based Application Insights and copy APPLICATIONINSIGHTS_CONNECTION_STRING → configure UseAzureMonitor() OpenTelemetry distro at startup → verify requests/dependencies in Logs → create a KQL or metric alert linked to an Action Group
- B. Set Adaptive Sampling to 0% maxTelemetryItemsPerSecond → deploy without connection string → query traces → attach Action Group
- C. Create a deprecated Classic InstrumentationKey-only resource → hardcode ikey without SDK → fire Action Group → provision Log Analytics later
- D. Create a KQL alert rule on an empty subscription → uninstall OpenTelemetry packages → copy connection string → provision Application Insights

### 67. A fleet-tracking platform adopting OpenTelemetry on .NET 8 needs connection-string auto-instrumentation, coordinated multi-service `operation_Id` trace sampling under a 10 GB/day cap, and unsampled Live Metrics. Which two choices satisfy these requirements? Select two.

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently
- E. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 68. A developer starts instrumenting a new .NET 8 cold-chain service (`builder.Services.AddOpenTelemetry(). ____ `) using `APPLICATIONINSIGHTS_CONNECTION_STRING`. Which extension method wires the official Azure Monitor OpenTelemetry Distro?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments

### 69. Container terminals in four seaports run local crane-control APIs that must remain routable inside the terminal LAN if submarine WAN links flap, while pulling APIM policy updates from Azure over HTTPS. Which APIM architecture supports this?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Select `Developer` (non-SLA) or `Premium` / `Standard v2` for VNet integration, and deploy the containerized APIM Self-Hosted Gateway (`mcr.microsoft.com/azure-api-management/gateway`) for hybrid on-premises/multi-cloud local traffic routing

### 70. Mariner's APIM gateway calls an internal Entra-protected customs Function App and must inject Managed Identity bearer tokens without storing client secrets (`<inbound> ____ </inbound>`). Which XML policy snippet accomplishes this?

Domain: Connect to and consume Azure services and third-party services

- A. Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 71. A logistics API team tests a non-breaking OpenAPI query-parameter addition on `;rev=2` before flipping it current, while exposing breaking `/v1/shipments` and `/v2/shipments` schemas simultaneously for legacy EDI partners. How do `Revisions` and `Versions` apply?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Use APIM `Revisions` to stage, test, and swap non-breaking internal changes safely on the same consumer URL (`;rev=2`), and use APIM `Versions` (path/header/query) when publishing breaking contract changes side-by-side for distinct consumer cohorts
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 72. Carrier portal developers need HTTP 200 mocked `/containers/eta` responses from APIM while backend services are still in development, and later `/containers/{id}` must rewrite to `/internal/v2/orders/{orderId}` (` ____ `). Which APIM policies handle both?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use `<mock-response status-code="200" content-type="application/json" />` during frontend parallel development, or `<rewrite-uri template="/internal/v2/orders/{orderId}" />` with `<set-backend-service base-url="..." />` in `<inbound>`

### 73. An HTTP-triggered Function App imported behind Azure API Management requires APIM to send a function/host key in `x-functions-key` rather than allowing unauthenticated calls (`[HttpTrigger( ____ )]`). Which `AuthorizationLevel` enforces this?

Domain: Connect to and consume Azure services and third-party services

- A. Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 74. Strider's API team is eliminating static backend API keys in APIM and switching to Managed Identity authentication toward an Entra-protected cold-chain backend. Which ordered steps complete the rollout?

Domain: Connect to and consume Azure services and third-party services

- A. Add authentication-managed-identity policy → test backend invocation → enable Managed Identity on APIM → grant RBAC on the target
- B. Enable Managed Identity on the APIM instance → grant that identity RBAC or app-role access on the target backend/Key Vault → add authentication-managed-identity in APIM policy XML → test backend calls and inspect APIM trace headers
- C. Hardcode a 2-year client secret inside `<set-header>` XML → disable Managed Identity → grant RBAC → inspect trace
- D. Grant RBAC to the developer laptop user → add `<validate-jwt>` in `<outbound>` → enable APIM Managed Identity → test backend

### 75. Customs-broker APIs on APIM must require Product Subscription Keys, verify broker mTLS client certificate thumbprints, and validate Entra JWT signatures/roles before forwarding requests. Which two APIM `<inbound>` configurations enforce all three? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers
- B. Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps

### 76. An APIM berth-booking endpoint must reject requests with HTTP `401` whenever the `Authorization` bearer JWT lacks audience `api://orders` or the required write role (`<inbound> ____ </inbound>`). Which XML policy enforces this at the gateway?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 77. A public port-schedule API on APIM needs 60-call/minute burst limits (`429`) + 5,000-call/month partner quotas (`403`) keeping `<base />`, 300-second caching varied by `Accept-Language`, and 3x backend 5xx retries with outbound `X-AspNet-Version` removal. Which three APIM policy setups deliver this? Select three.

Domain: Connect to and consume Azure services and third-party services

- A. Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`
- E. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- F. Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`

### 78. Partner freight forwarders must be throttled at 60 requests/minute (HTTP `429`) and capped at 5,000 requests/month (HTTP `403`) per APIM subscription without stripping inherited API-level `<validate-jwt>` policies. How must `<inbound>` be authored?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`

### 79. Proposed solution: Add `<cache-store duration="300" />` in `<outbound>` on `GET /schedules` without adding `<cache-lookup>` in `<inbound>`, expecting APIM to serve cached responses automatically. Why does every call still hit the backend, and what fixes it?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 80. Brief container restarts on a route-ETA backend return single HTTP 503 responses to APIM callers, and responses expose `X-AspNet-Version`. Which APIM policy sections handle transient 5xx retries and response-header deletion?

Domain: Connect to and consume Azure services and third-party services

- A. Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 81. Mariner PortOps is registering a third-party tugboat-dispatch HTTPS webhook on an Azure Event Grid custom topic. Which ordered steps complete the mandatory subscription validation handshake?

Domain: Connect to and consume Azure services and third-party services

- A. Deploy an HTTP-only port 80 endpoint → return validationCode as a response header → create the Event Grid subscription → enable TLS
- B. Deploy the HTTPS webhook endpoint accepting POST requests → create the Event Grid subscription pointing to the endpoint → inspect incoming SubscriptionValidationEvent and read validationCode → return HTTP 200 JSON containing validationResponse (or invoke validationUrl)
- C. Create the Event Grid subscription → deploy the HTTPS endpoint later → return HTTP 202 empty body → parse SubscriptionValidationEvent
- D. Return HTTP 200 validationResponse before reading the request → create the topic → deploy the endpoint → create the subscription

### 82. A global freight visibility hub pushes container-arrival events to 3,200 independent shipper tenants under one Event Grid publish endpoint with per-tenant RBAC, while onboarding custom HTTPS partner webhooks (` ____ `). Which two Event Grid patterns are required? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- C. Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`
- D. Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization
- E. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 83. A custom ASP.NET Core warehouse webhook throws HTTP 400 when Event Grid sends its initial `SubscriptionValidationEvent` (` ____ `), blocking subscription creation. What response must the endpoint return?

Domain: Connect to and consume Azure services and third-party services

- A. Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors

### 84. Locomotive vibration sensors stream 55,000 readings/sec into Azure Event Hubs, and a predictive-maintenance .NET 8 worker must consume partitions with Blob Storage offset checkpoints. Which sequence implements the consumer?

Domain: Connect to and consume Azure services and third-party services

- A. Create the Event Hub, consumer group, and Blob checkpoint container → instantiate BlobContainerClient and EventProcessorClient → register ProcessEventAsync (calling UpdateCheckpointAsync) and ProcessErrorAsync → call StartProcessingAsync before StopProcessingAsync
- B. Call StartProcessingAsync → register ProcessEventAsync without ProcessErrorAsync → create the Event Hub → create the Blob container
- C. Point all five independent microservices at `$Default` with one shared Blob prefix → call StopProcessingAsync → call StartProcessingAsync → skip UpdateCheckpointAsync
- D. Instantiate EventHubProducerClient → call UpdateCheckpointAsync on the producer → register ProcessEventAsync → call StopProcessingAsync first

### 85. Proposed solution: Push 40,000 raw crane-GPS readings per second into Azure Event Grid custom webhooks so three analytics services can replay 7-day partition offsets and write Parquet files to ADLS Gen2. Why does this fail, and what replaces it?

Domain: Connect to and consume Azure services and third-party services

- A. Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 86. Automated stacking-crane commands for a single `craneLaneId` must execute in strict FIFO order without blocking commands for 30 other crane lanes on Azure Service Bus. Which ordered setup enforces per-lane FIFO?

Domain: Connect to and consume Azure services and third-party services

- A. Create a standard queue with RequiresSession = false → send messages without SessionId → toggle RequiresSession = true later → read with standard ServiceBusReceiver
- B. Create the queue or subscription with RequiresSession = true at creation time → send ServiceBusMessage instances setting a non-empty SessionId → create a ServiceBusSessionProcessor (or AcceptNextSessionAsync receiver) → process messages in order and complete/renew session locks
- C. Send messages to Queue Storage with SessionId → attach ServiceBusSessionProcessor → toggle FIFO → complete locks
- D. Create ServiceBusSessionProcessor → send messages with null SessionId → create the queue → complete messages before receiving

### 87. Yard-gate RFID readers occasionally resend duplicate `MessageId` scans over cellular links, require per-gate FIFO ordering, and schedule demurrage-warning messages 30 minutes out (`CancelScheduledMessageAsync` if cleared early). Which two Service Bus capabilities solve this? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering
- E. Call `long seq = await sender.ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` and persist `seq` to call `CancelScheduledMessageAsync(seq)` if the user cancels early

### 88. A fleet dashcam pipeline queues 260 TB of 10 KB video-transcode job pointers needing simple HTTP visibility timeouts and low storage cost without FIFO sessions or topic fan-out. Which Azure messaging service handles a 260 TB backlog?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

---

## Case study — Aegis Rail

Aegis Rail hosts internal track-inspection web apps secured with App Service built-in authentication (Microsoft Entra provider) returning HTTP 401 rather than interactive redirects for unauthenticated API clients. Inspection microservices authenticate to Azure Key Vault and Azure Queue Storage via `DefaultAzureCredential` during both local Visual Studio debugging and deployed Azure hosting.

The next 3 questions refer to **Aegis Rail**. Read the scenario brief once, then answer each item independently.

### 89. Track-inspection tablet APIs hosted on App Service use built-in Microsoft Entra Authentication (`Easy Auth`) and must return HTTP `401` rather than HTML `302` login redirects when tokens are missing or expired. Which Easy Auth setting enforces this?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)

### 90. Rail-sensor microservices connect to Key Vault and Queue Storage without connection strings during both local Visual Studio debugging and deployed Azure hosting. Which `Azure.Identity` credential class meets this requirement?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- C. Instantiate `new DefaultAzureCredential()` (or explicit `ManagedIdentityCredential(clientId)` for user-assigned identities in production) so identical code authenticates via Azure CLI / Visual Studio locally and Managed Identity in Azure
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 91. Aegis stores wayside database secrets, locomotive RSA signing keys, and mTLS certificates in Azure Key Vault and requires mandatory 90-day protection against permanent key purge even by rogue admins. Which two Key Vault practices apply? Select two.

Domain: Implement Azure security

- A. Use `SecretClient` (`Azure.Security.KeyVault.Secrets`) for connection strings/tokens, `KeyClient` / `CryptographyClient` (`Azure.Security.KeyVault.Keys`) for RSA/EC wrap-unwrap-sign, and `CertificateClient` for X.509 lifecycle
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Enable Soft Delete (mandatory on new vaults, 7–90 days) plus Purge Protection on Azure Key Vault so neither accidental deletion nor malicious principals can permanently destroy keys before retention expires
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

---

## Case study — Mariner PortOps

Mariner PortOps runs customs-manifest APIs on Azure App Service Linux containers deployed from a geo-replicated Azure Container Registry. Customs brokers upload XML manifests to Blob Storage where a single active processing worker must acquire a 60-second exclusive lock on each manifest blob before updating status metadata so concurrent workers never double-file customs declarations.

The next 3 questions refer to **Mariner PortOps**. Read the scenario brief once, then answer each item independently.

### 92. Mariner deploys Linux customs-manifest containers across port regions in Rotterdam, Singapore, and Los Angeles and needs local regional image layer pulls from a single registry FQDN. Which ACR configuration is required?

Domain: Develop Azure compute solutions

- A. Upgrade Azure Container Registry to the `Premium` SKU and configure geo-replication into each target compute region
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 93. When customs brokers upload XML manifests to Blob Storage, Mariner must ensure only one worker pod locks each manifest blob for 60 seconds before updating status metadata so duplicate customs filings never occur. Which SDK call enforces this?

Domain: Develop for Azure storage

- A. Use `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` (15–60 seconds or `-1` infinite) and pass `LeaseId` inside `BlobRequestConditions` on subsequent writes/deletes
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 94. Mariner's Linux App Service customs API pulls container images from ACR, and port security policy forbids shared ACR admin credentials. How should image pulls be authenticated?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- C. Disable the ACR admin account and assign the built-in `AcrPull` role on the registry to the compute resource managed identity
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

---

## Case study — Strider ColdChain

Strider ColdChain monitors 25,000 refrigerated trailers emitting reefer temperatures every ten seconds into Azure Event Hubs. A .NET 8 `EventProcessorClient` hosted on Azure Container Apps checkpoints progress in Azure Blob Storage, while excursion events (`tempC > 4.0`) publish to an Azure Event Grid custom topic subscribed to by regional dispatchers filtered by subject prefix `/region/eu-west/`.

The next 3 questions refer to **Strider ColdChain**. Read the scenario brief once, then answer each item independently.

### 95. Strider's .NET 8 worker on Container Apps consumes 25,000 reefer telemetry readings every ten seconds from Event Hubs (` ____ `) and must persist partition progress in Blob Storage so scaling events never replay hours of readings. Which pattern implements this?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Host `EventProcessorClient` backed by `BlobContainerClient` and call `await eventArgs.UpdateCheckpointAsync()` after idempotent batch persistence so partition leases resume cleanly after rebalancing
- D. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors

### 96. Temperature excursions (`tempC > 4.0`) publish to an Event Grid custom topic and must push only `/region/eu-west/` alerts to Rotterdam dispatchers while dead-lettering undelivered alerts to Blob Storage. Which Event Grid subscription configuration works?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL
- C. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 97. Strider wants to test a new anomaly-threshold build of its HTTP telemetry-query API on Azure Container Apps by sending 10% of live dispatcher requests to the new revision. How must the Container App be configured?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Set `--revision-mode multiple` and apply `az containerapp ingress traffic set --revision-weight` to split live HTTP requests across named revisions

---

## Case study — Zephyr Parcel

Zephyr Parcel coordinates hub sorting across Service Bus topics. Hazardous-material parcels (`hazmat = true`) must route to a dedicated compliance subscription that stamps `Priority = High` onto brokered message properties, while unprocessable poison messages exceeding five delivery attempts move automatically to the subscription dead-letter queue for ops inspection.

The next 3 questions refer to **Zephyr Parcel**. Read the scenario brief once, then answer each item independently.

### 98. Hub-sorting events published to a Service Bus topic must route `hazmat = true` parcels to a compliance subscription that stamps `Priority = High` onto brokered properties, while isolating messages exceeding 5 failed deliveries. Which Service Bus setup accomplishes this?

Domain: Connect to and consume Azure services and third-party services

- A. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Use Azure Service Bus Topics with `SqlRuleFilter` / `CorrelationRuleFilter` (`CorrelationRuleFilter` preferred for high throughput) and `SqlRuleAction` header stamping, inspecting `$DeadLetterQueue` (`SubQueue.DeadLetter`) after `MaxDeliveryCount` expires
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 99. Zephyr's compliance consumer must keep hazmat messages locked on the broker during processing, return transient faults for immediate retry, and explicitly quarantine malformed XML schemas into the dead-letter sub-queue (` ____ `). Which `ServiceBusProcessor` pattern works?

Domain: Connect to and consume Azure services and third-party services

- A. Use `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false`, calling `CompleteMessageAsync` after commit, `AbandonMessageAsync` for transient retries, and `DeadLetterMessageAsync` on unrecoverable schema errors
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 100. Label-printer edge workers read parcel barcode jobs from Azure Queue Storage and need to extend visibility leases when paper jams slow printing (`UpdateMessageAsync`) before deleting finished jobs. Which parameters must the C# worker pass?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

---

## Answer key and explanations

### Question 1 — B, C

Answers: Use a multi-stage Dockerfile building in `mcr.microsoft.com/dotnet/sdk:8.0` and copying published output into `mcr.microsoft.com/dotnet/aspnet:8.0` with a non-root `USER app`; Declare `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form so `SIGTERM` reaches the .NET host cleanly during container shutdown. Multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root builds strip build tools, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to PID 1. Local study-map skill 1.1 (Create and Manage Container Images and Multi-Stage Dockerfiles), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root builds strip build tools, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to PID 1.
- **B:** Correct. Exec-form `ENTRYPOINT` runs the process as PID 1 without an intermediate `/bin/sh -c` wrapper that swallows POSIX termination signals. In this scenario: Multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root builds strip build tools, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to PID 1.
- **C:** Correct. Multi-stage Docker builds exclude compiler SDK layers and source files from the final runtime image, shrinking image size and attack surface. In this scenario: Multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root builds strip build tools, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to PID 1.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root builds strip build tools, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to PID 1.
- **E:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root builds strip build tools, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to PID 1.

### Question 2 — D

Answer: Add `bin/`, `obj/`, `.git/`, and local `.env` files to `.dockerignore` before running `docker build` or `az acr build`. Adding `bin/`, `obj/`, `.git/`, and test-artifact directories to `.dockerignore` excludes them from the uploaded ACR Tasks build context. `.dockerignore` prevents streaming gigabytes of local build artifacts and stray secrets into the build context. Local study-map skill 1.1 (Create and Manage Container Images and Multi-Stage Dockerfiles), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Adding `bin/`, `obj/`, `.git/`, and test-artifact directories to `.dockerignore` excludes them from the uploaded ACR Tasks build context.
- **B:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Adding `bin/`, `obj/`, `.git/`, and test-artifact directories to `.dockerignore` excludes them from the uploaded ACR Tasks build context.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Adding `bin/`, `obj/`, `.git/`, and test-artifact directories to `.dockerignore` excludes them from the uploaded ACR Tasks build context.
- **D:** Correct. `.dockerignore` prevents streaming gigabytes of local build artifacts and stray secrets into the build context. In this scenario: Adding `bin/`, `obj/`, `.git/`, and test-artifact directories to `.dockerignore` excludes them from the uploaded ACR Tasks build context.

### Question 3 — D

Answer: Run `az acr build --registry <acrName> --image app:{{.Run.ID}} .` to build and push the container image remotely using ACR Tasks without a local Docker daemon. `az acr build --registry <acrName> --image gateway:{{.Run.ID}} .` tars the source context and builds/pushes layers inside ACR Tasks. ACR Tasks tar and upload the build context to Azure, executing the Dockerfile build and pushing tagged layers directly inside ACR. Local study-map skill 1.2 (Publish Images, Run ACR Tasks, and Manage Auth/Purge in Azure Container Registry), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `az acr build --registry <acrName> --image gateway:{{.Run.ID}} .` tars the source context and builds/pushes layers inside ACR Tasks.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az acr build --registry <acrName> --image gateway:{{.Run.ID}} .` tars the source context and builds/pushes layers inside ACR Tasks.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `az acr build --registry <acrName> --image gateway:{{.Run.ID}} .` tars the source context and builds/pushes layers inside ACR Tasks.
- **D:** Correct. ACR Tasks tar and upload the build context to Azure, executing the Dockerfile build and pushing tagged layers directly inside ACR. In this scenario: `az acr build --registry <acrName> --image gateway:{{.Run.ID}} .` tars the source context and builds/pushes layers inside ACR Tasks.

### Question 4 — A

Answer: Set `--restart-policy OnFailure` (or `Never`) on the Azure Container Instances container group so batch containers stop billing vCPU/memory seconds once exit code 0 completes. Default `Always` restarts exited containers indefinitely even on exit code `0`; setting `--restart-policy OnFailure` (or `Never`) halts execution and per-second billing once exit `0` completes. ACI bills per second while containers run; `OnFailure` retries crashes (`exit != 0`) and halts cleanly on `exit == 0`, whereas `Always` loops forever. Local study-map skill 1.3 (Run Container Groups, Sidecars, Volumes, and Restart Policies in Azure Container Instances), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. ACI bills per second while containers run; `OnFailure` retries crashes (`exit != 0`) and halts cleanly on `exit == 0`, whereas `Always` loops forever. In this scenario: Default `Always` restarts exited containers indefinitely even on exit code `0`; setting `--restart-policy OnFailure` (or `Never`) halts execution and per-second billing once exit `0` completes.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Default `Always` restarts exited containers indefinitely even on exit code `0`; setting `--restart-policy OnFailure` (or `Never`) halts execution and per-second billing once exit `0` completes.
- **C:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Default `Always` restarts exited containers indefinitely even on exit code `0`; setting `--restart-policy OnFailure` (or `Never`) halts execution and per-second billing once exit `0` completes.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Default `Always` restarts exited containers indefinitely even on exit code `0`; setting `--restart-policy OnFailure` (or `Never`) halts execution and per-second billing once exit `0` completes.

### Question 5 — D

Answer: Deploy the application container and Envoy/logging sidecar inside one multi-container ACI group sharing `localhost` network namespace and an `emptyDir` / Azure Files volume. Deploying parser and log shipper inside one multi-container ACI group shares `127.0.0.1` loopback networking and mounts a shared `emptyDir` / Azure Files volume. Containers in the same ACI container group share one IP/port namespace (`127.0.0.1`) and can mount shared Azure Files or `emptyDir` volumes on Linux. Local study-map skill 1.3 (Run Container Groups, Sidecars, Volumes, and Restart Policies in Azure Container Instances), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Deploying parser and log shipper inside one multi-container ACI group shares `127.0.0.1` loopback networking and mounts a shared `emptyDir` / Azure Files volume.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Deploying parser and log shipper inside one multi-container ACI group shares `127.0.0.1` loopback networking and mounts a shared `emptyDir` / Azure Files volume.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Deploying parser and log shipper inside one multi-container ACI group shares `127.0.0.1` loopback networking and mounts a shared `emptyDir` / Azure Files volume.
- **D:** Correct. Containers in the same ACI container group share one IP/port namespace (`127.0.0.1`) and can mount shared Azure Files or `emptyDir` volumes on Linux. In this scenario: Deploying parser and log shipper inside one multi-container ACI group shares `127.0.0.1` loopback networking and mounts a shared `emptyDir` / Azure Files volume.

### Question 6 — A

Answer: Deploy an Azure Container Apps Job (`triggerType: Event` or `Schedule`) with `replicaCompletionCount` and `parallelism` instead of an always-listening HTTP container app. Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` executes finite batch tasks without keeping an HTTP app running. Container Apps Jobs execute finite scheduled or event-driven workloads to completion without exposing unused HTTP ingress. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Container Apps Jobs execute finite scheduled or event-driven workloads to completion without exposing unused HTTP ingress. In this scenario: Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` executes finite batch tasks without keeping an HTTP app running.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` executes finite batch tasks without keeping an HTTP app running.
- **C:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` executes finite batch tasks without keeping an HTTP app running.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` executes finite batch tasks without keeping an HTTP app running.

### Question 7 — C, D, F

Answers: Configure a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0` and Managed Identity (`identity` property) so replicas scale to zero when idle and wake on queue depth; Register a Dapr state or pub/sub component in the Container Apps environment and restrict access via the component `scopes` array to specific `daprAppId` values; Define a Container App secret using `keyVaultUrl` plus `identity` (managed identity resource ID or `system`) and map container environment variables via `secretRef`. KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, Dapr `scopes` confine component visibility by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, Dapr `scopes` confine component visibility by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely.
- **B:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, Dapr `scopes` confine component visibility by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely.
- **C:** Correct. Container Apps uses KEDA scalers to scale down to zero on consumption/workload profiles and authenticate scalers cleanly via Managed Identity. In this scenario: KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, Dapr `scopes` confine component visibility by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely.
- **D:** Correct. Key Vault secret references in Container Apps resolve secrets via Managed Identity without storing secret strings in ARM templates. In this scenario: KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, Dapr `scopes` confine component visibility by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely.
- **E:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, Dapr `scopes` confine component visibility by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely.
- **F:** Correct. Dapr `scopes` confine which microservices inside a shared Container Apps environment can load or invoke a component. In this scenario: KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, Dapr `scopes` confine component visibility by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely.

### Question 8 — D

Answer: Execute `az containerapp env create --name <envName> --resource-group <rg> --infrastructure-subnet-resource-id <subnetId> --internal-only`. `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` provisions an internal-only VNet-integrated environment. Provisioning a VNet-injected `--internal-only` Container Apps environment isolates the Envoy ingress load balancer to private RFC1918 addresses. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` provisions an internal-only VNet-integrated environment.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` provisions an internal-only VNet-integrated environment.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` provisions an internal-only VNet-integrated environment.
- **D:** Correct. Provisioning a VNet-injected `--internal-only` Container Apps environment isolates the Envoy ingress load balancer to private RFC1918 addresses. In this scenario: `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` provisions an internal-only VNet-integrated environment.

### Question 9 — A

Answer: Provision at least a `Standard` (`S1+`) or `Premium v3` (`P1v3+`) App Service plan to unlock deployment slots, custom domain SNI SSL, and metric/schedule autoscaling. Scaling up to `Standard (S1+)` or `Premium v3 (P1v3+)` enables deployment slots and rule-based horizontal autoscale unavailable on `Basic` plans. `Free`, `Shared`, and `Basic` plans omit deployment slots (`S1` gives 5, `P1v3` gives 20) and rule-based autoscale (`S1+` required). Local study-map skill 1.5 (Create Azure App Service Plans and Web Apps Across Linux and Windows Runtimes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. `Free`, `Shared`, and `Basic` plans omit deployment slots (`S1` gives 5, `P1v3` gives 20) and rule-based autoscale (`S1+` required). In this scenario: Scaling up to `Standard (S1+)` or `Premium v3 (P1v3+)` enables deployment slots and rule-based horizontal autoscale unavailable on `Basic` plans.
- **B:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Scaling up to `Standard (S1+)` or `Premium v3 (P1v3+)` enables deployment slots and rule-based horizontal autoscale unavailable on `Basic` plans.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Scaling up to `Standard (S1+)` or `Premium v3 (P1v3+)` enables deployment slots and rule-based horizontal autoscale unavailable on `Basic` plans.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Scaling up to `Standard (S1+)` or `Premium v3 (P1v3+)` enables deployment slots and rule-based horizontal autoscale unavailable on `Basic` plans.

### Question 10 — B

Answer: Set `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` inside the final `.NET 8` runtime stage and match `targetPort: 8080` on Container Apps ingress. Declaring `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` configures Kestrel on unprivileged port `8080` matching `targetPort: 8080`. Starting in .NET 8, official Microsoft container images default to non-root port `8080` rather than privileged port `80`. Local study-map skill 1.5 (Create Azure App Service Plans and Web Apps Across Linux and Windows Runtimes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Declaring `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` configures Kestrel on unprivileged port `8080` matching `targetPort: 8080`.
- **B:** Correct. Starting in .NET 8, official Microsoft container images default to non-root port `8080` rather than privileged port `80`. In this scenario: Declaring `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` configures Kestrel on unprivileged port `8080` matching `targetPort: 8080`.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Declaring `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` configures Kestrel on unprivileged port `8080` matching `targetPort: 8080`.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Declaring `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` configures Kestrel on unprivileged port `8080` matching `targetPort: 8080`.

### Question 11 — C

Answer: Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances. Directing Application Logging (Blob) and Web Server Logging to an Azure Blob Storage container enforces durable multi-month retention across all instances. Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy. Local study-map skill 1.6 (Configure App Service Diagnostics, Application/Web Server Logging, and Log Streaming), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Directing Application Logging (Blob) and Web Server Logging to an Azure Blob Storage container enforces durable multi-month retention across all instances.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Directing Application Logging (Blob) and Web Server Logging to an Azure Blob Storage container enforces durable multi-month retention across all instances.
- **C:** Correct. Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy. In this scenario: Directing Application Logging (Blob) and Web Server Logging to an Azure Blob Storage container enforces durable multi-month retention across all instances.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Directing Application Logging (Blob) and Web Server Logging to an Azure Blob Storage container enforces durable multi-month retention across all instances.

### Question 12 — D

Answer: Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`. Enabling verbose filesystem logging with `az webapp log config` and running `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu console logs. `az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting. Local study-map skill 1.6 (Configure App Service Diagnostics, Application/Web Server Logging, and Log Streaming), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling verbose filesystem logging with `az webapp log config` and running `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu console logs.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Enabling verbose filesystem logging with `az webapp log config` and running `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu console logs.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Enabling verbose filesystem logging with `az webapp log config` and running `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu console logs.
- **D:** Correct. `az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting. In this scenario: Enabling verbose filesystem logging with `az webapp log config` and running `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu console logs.

### Question 13 — D

Answer: Set `WEBSITE_RUN_FROM_PACKAGE=1` and deploy with `az webapp deploy --type zip` so the app mounts the read-only ZIP package directly with atomic cold-start replacement. Setting `WEBSITE_RUN_FROM_PACKAGE=1` with `az webapp deploy --type zip` mounts the uploaded ZIP package directly without copying individual files into `wwwroot`. Running directly from a mounted ZIP eliminates file-lock copy conflicts during `wwwroot` sync and speeds cold starts. Local study-map skill 1.7 (Deploy Code, Run-From-Package ZIPs, and Custom Containers to App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` with `az webapp deploy --type zip` mounts the uploaded ZIP package directly without copying individual files into `wwwroot`.
- **B:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` with `az webapp deploy --type zip` mounts the uploaded ZIP package directly without copying individual files into `wwwroot`.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` with `az webapp deploy --type zip` mounts the uploaded ZIP package directly without copying individual files into `wwwroot`.
- **D:** Correct. Running directly from a mounted ZIP eliminates file-lock copy conflicts during `wwwroot` sync and speeds cold starts. In this scenario: Setting `WEBSITE_RUN_FROM_PACKAGE=1` with `az webapp deploy --type zip` mounts the uploaded ZIP package directly without copying individual files into `wwwroot`.

### Question 14 — A, B

Answers: Enable `httpsOnly: true`, set `minTlsVersion: "1.2"` (or `"1.3"`), and configure `clientCertEnabled` when mutual TLS client certificates are required; Configure App Service `CORS` with explicit origin URLs (and `supportCredentials` only without wildcard `*`) so App Service handles preflight `OPTIONS` requests. Enabling `httpsOnly: true` + `minTlsVersion: "1.2"` secures transport, while configuring explicit origin `https://ops.strider.example` (never `*`) in App Service `CORS` permits credentialed requests. Local study-map skill 1.8 (Configure TLS, Mutual TLS, CORS, App Settings, and Service Connections on App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Enforcing HTTPS redirection and minimum TLS 1.2/1.3 at the App Service front end rejects plaintext HTTP and legacy ciphers before app code runs. In this scenario: Enabling `httpsOnly: true` + `minTlsVersion: "1.2"` secures transport, while configuring explicit origin `https://ops.strider.example` (never `*`) in App Service `CORS` permits credentialed requests.
- **B:** Correct. Platform-level App Service CORS intercepts `OPTIONS` preflight checks; credentialed CORS forbids wildcard `*` origins. In this scenario: Enabling `httpsOnly: true` + `minTlsVersion: "1.2"` secures transport, while configuring explicit origin `https://ops.strider.example` (never `*`) in App Service `CORS` permits credentialed requests.
- **C:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Enabling `httpsOnly: true` + `minTlsVersion: "1.2"` secures transport, while configuring explicit origin `https://ops.strider.example` (never `*`) in App Service `CORS` permits credentialed requests.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Enabling `httpsOnly: true` + `minTlsVersion: "1.2"` secures transport, while configuring explicit origin `https://ops.strider.example` (never `*`) in App Service `CORS` permits credentialed requests.
- **E:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling `httpsOnly: true` + `minTlsVersion: "1.2"` secures transport, while configuring explicit origin `https://ops.strider.example` (never `*`) in App Service `CORS` permits credentialed requests.

### Question 15 — D

Answer: Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`. `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` sets and pins the typed SQL connection string. `--slot-settings` pins the connection string (`SQLCONNSTR_LedgerDb`) to the target slot so slot swaps never leak staging databases into production. Local study-map skill 1.8 (Configure TLS, Mutual TLS, CORS, App Settings, and Service Connections on App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` sets and pins the typed SQL connection string.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` sets and pins the typed SQL connection string.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` sets and pins the typed SQL connection string.
- **D:** Correct. `--slot-settings` pins the connection string (`SQLCONNSTR_LedgerDb`) to the target slot so slot swaps never leak staging databases into production. In this scenario: `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` sets and pins the typed SQL connection string.

### Question 16 — C

Answer: Pair every scale-out metric rule (e.g., CPU > 75% for 10 min) with a conservative scale-in rule (e.g., CPU < 35%) and an explicit `coolDown` window plus safe default/max instance bounds. Widening hysteresis between scale-out (>75%) and scale-in (<35%) CPU rules and adding a conservative `coolDown` window stabilizes worker counts. Asymmetric thresholds and cool-down periods prevent rapid flapping (thrashing) where instances repeatedly add and terminate. Local study-map skill 1.9 (Implement Metric-Based and Schedule-Based App Service Autoscaling Rules and Cooldowns), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Widening hysteresis between scale-out (>75%) and scale-in (<35%) CPU rules and adding a conservative `coolDown` window stabilizes worker counts.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Widening hysteresis between scale-out (>75%) and scale-in (<35%) CPU rules and adding a conservative `coolDown` window stabilizes worker counts.
- **C:** Correct. Asymmetric thresholds and cool-down periods prevent rapid flapping (thrashing) where instances repeatedly add and terminate. In this scenario: Widening hysteresis between scale-out (>75%) and scale-in (<35%) CPU rules and adding a conservative `coolDown` window stabilizes worker counts.
- **D:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Widening hysteresis between scale-out (>75%) and scale-in (<35%) CPU rules and adding a conservative `coolDown` window stabilizes worker counts.

### Question 17 — C

Answer: Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps. Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH=/warmup/graph` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` blocks traffic cutover until warm-up succeeds. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. Local study-map skill 1.9 (Implement Metric-Based and Schedule-Based App Service Autoscaling Rules and Cooldowns), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH=/warmup/graph` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` blocks traffic cutover until warm-up succeeds.
- **B:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH=/warmup/graph` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` blocks traffic cutover until warm-up succeeds.
- **C:** Correct. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. In this scenario: Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH=/warmup/graph` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` blocks traffic cutover until warm-up succeeds.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH=/warmup/graph` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` blocks traffic cutover until warm-up succeeds.

### Question 18 — D

Answer: Create the staging deployment slot on the Standard/Premium Web App → mark production-only connection strings and webhook settings as deployment slot settings → deploy and warm up the new build in staging → swap staging into production and verify health. Provisioning the `staging` slot, marking EDI endpoint settings as slot-sticky first, deploying and verifying v3.2 in `staging`, and swapping into `Production` prevents downtime and config leakage. Slot-sticky settings must be pinned before swapping so staging never inherits live payment webhooks or overwrites production secrets during swap. Local study-map skill 1.10 (Configure App Service Deployment Slots, Slot-Sticky Settings, Warm-Up, and Traffic Routing), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Deploying directly to production bypasses zero-downtime validation and swapping an empty staging slot overwrites production. Why the keyed choice wins: Provisioning the `staging` slot, marking EDI endpoint settings as slot-sticky first, deploying and verifying v3.2 in `staging`, and swapping into `Production` prevents downtime and config leakage.
- **B:** Incorrect for this requirement. You cannot swap a slot before creating and deploying to it, and marking settings sticky after the swap leaks staging values into production. Why the keyed choice wins: Provisioning the `staging` slot, marking EDI endpoint settings as slot-sticky first, deploying and verifying v3.2 in `staging`, and swapping into `Production` prevents downtime and config leakage.
- **C:** Incorrect for this requirement. Free and Basic App Service plans do not support deployment slots; Standard, Premium, or Isolated is required first. Why the keyed choice wins: Provisioning the `staging` slot, marking EDI endpoint settings as slot-sticky first, deploying and verifying v3.2 in `staging`, and swapping into `Production` prevents downtime and config leakage.
- **D:** Correct. Slot-sticky settings must be pinned before swapping so staging never inherits live payment webhooks or overwrites production secrets during swap. In this scenario: Provisioning the `staging` slot, marking EDI endpoint settings as slot-sticky first, deploying and verifying v3.2 in `staging`, and swapping into `Production` prevents downtime and config leakage.

### Question 19 — A

Answer: Mark environment-specific settings such as `PaymentWebhookUrl` and production connection strings as `slotSetting: true` (Deployment slot setting) before swapping slots. Marking the broker URL setting with `slotSetting: true` (Deployment slot setting) pins staging and production values permanently to their own slots. Slot-sticky settings stay pinned to their slot (`Production` vs `Staging`) across swaps instead of traveling with the swapped code. Local study-map skill 1.10 (Configure App Service Deployment Slots, Slot-Sticky Settings, Warm-Up, and Traffic Routing), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Slot-sticky settings stay pinned to their slot (`Production` vs `Staging`) across swaps instead of traveling with the swapped code. In this scenario: Marking the broker URL setting with `slotSetting: true` (Deployment slot setting) pins staging and production values permanently to their own slots.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Marking the broker URL setting with `slotSetting: true` (Deployment slot setting) pins staging and production values permanently to their own slots.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Marking the broker URL setting with `slotSetting: true` (Deployment slot setting) pins staging and production values permanently to their own slots.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Marking the broker URL setting with `slotSetting: true` (Deployment slot setting) pins staging and production values permanently to their own slots.

### Question 20 — A

Answer: Host the Function App on `Flex Consumption` or `Elastic Premium (EP1+)` when VNet integration, longer execution timeouts beyond 10 minutes, or pre-warmed/always-ready instances are required. Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` for VNet + always-ready, with Premium supporting >10-min/unbounded runtimes) meets private networking, warm start, and long-execution needs. Classic Consumption caps timeout at 10 minutes (`functionTimeout`) and cold-starts from zero; `Flex Consumption` and `Premium` add VNet outbound and pre-warmed readiness. Local study-map skill 1.11 (Create and Configure Azure Functions Apps, Hosting Plans, and host.json Settings), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Classic Consumption caps timeout at 10 minutes (`functionTimeout`) and cold-starts from zero; `Flex Consumption` and `Premium` add VNet outbound and pre-warmed readiness. In this scenario: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` for VNet + always-ready, with Premium supporting >10-min/unbounded runtimes) meets private networking, warm start, and long-execution needs.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` for VNet + always-ready, with Premium supporting >10-min/unbounded runtimes) meets private networking, warm start, and long-execution needs.
- **C:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` for VNet + always-ready, with Premium supporting >10-min/unbounded runtimes) meets private networking, warm start, and long-execution needs.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` for VNet + always-ready, with Premium supporting >10-min/unbounded runtimes) meets private networking, warm start, and long-execution needs.

### Question 21 — A

Answer: Configure `"functionTimeout": "00:10:00"` and `"logging": { "applicationInsights": { "samplingSettings": { "isEnabled": true, "excludedTypes": "Request;Exception" } } }` inside `host.json`. Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` configures every function in the host. `host.json` governs global Function host behaviors such as execution timeout and Application Insights telemetry sampling exclusions across all functions in the app. Local study-map skill 1.11 (Create and Configure Azure Functions Apps, Hosting Plans, and host.json Settings), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. `host.json` governs global Function host behaviors such as execution timeout and Application Insights telemetry sampling exclusions across all functions in the app. In this scenario: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` configures every function in the host.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` configures every function in the host.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` configures every function in the host.
- **D:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` configures every function in the host.

### Question 22 — A, B

Answers: In the .NET isolated worker model, return a custom POCO class uniting `[HttpResult]` (or `HttpResponseData`) with `[CosmosDBOutput]` / `[ServiceBusOutput]` properties; Apply `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` (or `[FixedDelayRetry]`) on the `[EventHubTrigger]` / `[TimerTrigger]` function. Returning a custom POCO combining `[HttpResult]` and `[CosmosDBOutput]` handles isolated multi-output bindings, while `[ExponentialBackoffRetry]` retries transient Event Hub trigger faults. Local study-map skill 1.12 (Implement Azure Functions Input and Output Bindings (Isolated Worker & Declarative Bindings)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Function-level retry attributes replay failed executions in-memory before advancing trigger checkpoints on Event Hubs and Timer triggers. In this scenario: Returning a custom POCO combining `[HttpResult]` and `[CosmosDBOutput]` handles isolated multi-output bindings, while `[ExponentialBackoffRetry]` retries transient Event Hub trigger faults.
- **B:** Correct. Isolated-worker C# functions cannot use `out` parameters for bindings; multi-output types return structured properties on a single return object. In this scenario: Returning a custom POCO combining `[HttpResult]` and `[CosmosDBOutput]` handles isolated multi-output bindings, while `[ExponentialBackoffRetry]` retries transient Event Hub trigger faults.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Returning a custom POCO combining `[HttpResult]` and `[CosmosDBOutput]` handles isolated multi-output bindings, while `[ExponentialBackoffRetry]` retries transient Event Hub trigger faults.
- **D:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Returning a custom POCO combining `[HttpResult]` and `[CosmosDBOutput]` handles isolated multi-output bindings, while `[ExponentialBackoffRetry]` retries transient Event Hub trigger faults.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Returning a custom POCO combining `[HttpResult]` and `[CosmosDBOutput]` handles isolated multi-output bindings, while `[ExponentialBackoffRetry]` retries transient Event Hub trigger faults.

### Question 23 — D

Answer: Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`. `[CosmosDBTrigger(databaseName: "core", containerName: "shipments", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]` coordinates distributed change-feed processing. `CosmosDBTrigger` wraps the Change Feed Processor library and requires a lease container connection to coordinate partition checkpoints across scaled workers. Local study-map skill 1.12 (Implement Azure Functions Input and Output Bindings (Isolated Worker & Declarative Bindings)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: `[CosmosDBTrigger(databaseName: "core", containerName: "shipments", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]` coordinates distributed change-feed processing.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `[CosmosDBTrigger(databaseName: "core", containerName: "shipments", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]` coordinates distributed change-feed processing.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `[CosmosDBTrigger(databaseName: "core", containerName: "shipments", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]` coordinates distributed change-feed processing.
- **D:** Correct. `CosmosDBTrigger` wraps the Change Feed Processor library and requires a lease container connection to coordinate partition checkpoints across scaled workers. In this scenario: `[CosmosDBTrigger(databaseName: "core", containerName: "shipments", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]` coordinates distributed change-feed processing.

### Question 24 — C

Answer: Specify a six-field NCRONTAB expression `{second} {minute} {hour} {day} {month} {day-of-week}` such as `"0 */15 9-17 * * 1-5"` on `[TimerTrigger]`. `"0 */15 9-17 * * 1-5"` supplies `0` for seconds and triggers every 15 minutes across hours 9–17 Monday through Friday. Azure Functions `[TimerTrigger]` uses 6-field NCRONTAB (leading seconds field), unlike 5-field Unix cron. Local study-map skill 1.13 (Implement Function Triggers Using Cosmos DB/Blob Data Operations, NCRONTAB Timers, and Webhooks), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` supplies `0` for seconds and triggers every 15 minutes across hours 9–17 Monday through Friday.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` supplies `0` for seconds and triggers every 15 minutes across hours 9–17 Monday through Friday.
- **C:** Correct. Azure Functions `[TimerTrigger]` uses 6-field NCRONTAB (leading seconds field), unlike 5-field Unix cron. In this scenario: `"0 */15 9-17 * * 1-5"` supplies `0` for seconds and triggers every 15 minutes across hours 9–17 Monday through Friday.
- **D:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` supplies `0` for seconds and triggers every 15 minutes across hours 9–17 Monday through Friday.

### Question 25 — A

Answer: Configure `[BlobTrigger(..., Source = BlobTriggerSource.EventGrid)]` with an Event Grid system topic subscription instead of default container-log polling. Setting `Source = BlobTriggerSource.EventGrid` backed by an Event Grid system topic switches `[BlobTrigger]` from periodic storage-log polling to event-driven push execution. Event Grid-sourced blob triggers eliminate storage-log scan latency and work reliably on Blob-only / high-scale storage accounts. Local study-map skill 1.13 (Implement Function Triggers Using Cosmos DB/Blob Data Operations, NCRONTAB Timers, and Webhooks), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Event Grid-sourced blob triggers eliminate storage-log scan latency and work reliably on Blob-only / high-scale storage accounts. In this scenario: Setting `Source = BlobTriggerSource.EventGrid` backed by an Event Grid system topic switches `[BlobTrigger]` from periodic storage-log polling to event-driven push execution.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `Source = BlobTriggerSource.EventGrid` backed by an Event Grid system topic switches `[BlobTrigger]` from periodic storage-log polling to event-driven push execution.
- **C:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Setting `Source = BlobTriggerSource.EventGrid` backed by an Event Grid system topic switches `[BlobTrigger]` from periodic storage-log polling to event-driven push execution.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `Source = BlobTriggerSource.EventGrid` backed by an Event Grid system topic switches `[BlobTrigger]` from periodic storage-log polling to event-driven push execution.

### Question 26 — B, D, E

Answers: Define `new ContainerProperties(id: "telemetry", partitionKeyPaths: new List<string> { "/tenantId", "/siteId", "/deviceId" })` using `PartitionKeyBuilder` on reads and writes; Use `container.CreateTransactionalBatch(new PartitionKey(pkValue))` to group multiple create/replace/upsert/delete operations atomically within the same logical partition; Pass `new ItemRequestOptions { IfMatchEtag = item.ETag }` on `ReplaceItemAsync` and catch `CosmosException` when `StatusCode == HttpStatusCode.PreconditionFailed` (412). Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale past 20 GB per tenant, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` prevents concurrent lost updates. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale past 20 GB per tenant, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` prevents concurrent lost updates.
- **B:** Correct. `TransactionalBatch` guarantees ACID all-or-nothing execution serialized in one network round-trip, strictly scoped to a single logical partition key. In this scenario: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale past 20 GB per tenant, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` prevents concurrent lost updates.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale past 20 GB per tenant, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` prevents concurrent lost updates.
- **D:** Correct. Supplying `IfMatchEtag` enforces optimistic concurrency control so concurrent writers fail with HTTP 412 rather than silently overwriting updates. In this scenario: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale past 20 GB per tenant, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` prevents concurrent lost updates.
- **E:** Correct. Hierarchical partition keys (up to 3 levels) overcome the 20 GB logical-partition limit on large tenants while preserving efficient prefix queries on `/tenantId` alone. In this scenario: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale past 20 GB per tenant, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` prevents concurrent lost updates.
- **F:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale past 20 GB per tenant, `CreateTransactionalBatch` executes atomic single-partition writes, and `IfMatchEtag` prevents concurrent lost updates.

### Question 27 — C

Answer: Configure `"indexingMode": "consistent"` with `"includedPaths": [{"path": "/customerId/?"}, {"path": "/createdUtc/?"}]` and `"excludedPaths": [{"path": "/*"}]`. Excluding wildcard `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing slashes write RU charges and index storage overhead. Excluding wildcard `/*` and indexing only queried filter paths dramatically cuts write Request Unit (RU) cost and index storage on write-heavy containers. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Excluding wildcard `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing slashes write RU charges and index storage overhead.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Excluding wildcard `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing slashes write RU charges and index storage overhead.
- **C:** Correct. Excluding wildcard `/*` and indexing only queried filter paths dramatically cuts write Request Unit (RU) cost and index storage on write-heavy containers. In this scenario: Excluding wildcard `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing slashes write RU charges and index storage overhead.
- **D:** Incorrect for this requirement. Cosmos DB for NoSQL requires a matching composite index whenever a SQL query specifies `ORDER BY` across two or more properties. Why the keyed choice wins: Excluding wildcard `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing slashes write RU charges and index storage overhead.

### Question 28 — B

Answer: Call `await container.PatchItemAsync<Order>(id, new PartitionKey(pk), new[] { PatchOperation.Increment("/retryCount", 1), PatchOperation.Set("/lastStatus", "Queued") })`. `container.PatchItemAsync<T>` applies `PatchOperation.Increment` and `PatchOperation.Set` on the server without fetching and replacing the full JSON payload. Partial Document Update (`PatchItemAsync`) mutates specific JSON paths server-side without reading, deserializing, and replacing the full document payload. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `container.PatchItemAsync<T>` applies `PatchOperation.Increment` and `PatchOperation.Set` on the server without fetching and replacing the full JSON payload.
- **B:** Correct. Partial Document Update (`PatchItemAsync`) mutates specific JSON paths server-side without reading, deserializing, and replacing the full document payload. In this scenario: `container.PatchItemAsync<T>` applies `PatchOperation.Increment` and `PatchOperation.Set` on the server without fetching and replacing the full JSON payload.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `container.PatchItemAsync<T>` applies `PatchOperation.Increment` and `PatchOperation.Set` on the server without fetching and replacing the full JSON payload.
- **D:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `container.PatchItemAsync<T>` applies `PatchOperation.Increment` and `PatchOperation.Set` on the server without fetching and replacing the full JSON payload.

### Question 29 — C

Answer: Add a `compositeIndexes` array matching the exact property sequence and sort directions (`ascending` / `descending`) in the container indexing policy JSON. Adding a `compositeIndexes` definition listing `/priority` (`ascending`) and `/etaUtc` (`descending`) in matching order enables multi-property `ORDER BY` queries. Cosmos DB for NoSQL requires a matching composite index whenever a SQL query specifies `ORDER BY` across two or more properties. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Adding a `compositeIndexes` definition listing `/priority` (`ascending`) and `/etaUtc` (`descending`) in matching order enables multi-property `ORDER BY` queries.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Adding a `compositeIndexes` definition listing `/priority` (`ascending`) and `/etaUtc` (`descending`) in matching order enables multi-property `ORDER BY` queries.
- **C:** Correct. Cosmos DB for NoSQL requires a matching composite index whenever a SQL query specifies `ORDER BY` across two or more properties. In this scenario: Adding a `compositeIndexes` definition listing `/priority` (`ascending`) and `/etaUtc` (`descending`) in matching order enables multi-property `ORDER BY` queries.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Adding a `compositeIndexes` definition listing `/priority` (`ascending`) and `/etaUtc` (`descending`) in matching order enables multi-property `ORDER BY` queries.

### Question 30 — C

Answer: Use `Session` consistency (the default) and propagate `x-ms-session-token` (`RequestOptions.SessionToken`) across client/middle-tier hops to guarantee monotonic read-your-own-writes at half the read RU cost of `Strong`. Using `Session` consistency and passing `x-ms-session-token` (`SessionToken`) across client/API hops guarantees monotonic read-your-writes at half the RU charge of `Strong`. `Session` consistency guarantees read-your-writes, monotonic reads, and write-follows-reads within a session token at 50% of `Strong` / `BoundedStaleness` read RUs. Local study-map skill 2.2 (Select and Override Cosmos DB Consistency Levels and Session Tokens), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Using `Session` consistency and passing `x-ms-session-token` (`SessionToken`) across client/API hops guarantees monotonic read-your-writes at half the RU charge of `Strong`.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Using `Session` consistency and passing `x-ms-session-token` (`SessionToken`) across client/API hops guarantees monotonic read-your-writes at half the RU charge of `Strong`.
- **C:** Correct. `Session` consistency guarantees read-your-writes, monotonic reads, and write-follows-reads within a session token at 50% of `Strong` / `BoundedStaleness` read RUs. In this scenario: Using `Session` consistency and passing `x-ms-session-token` (`SessionToken`) across client/API hops guarantees monotonic read-your-writes at half the RU charge of `Strong`.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Using `Session` consistency and passing `x-ms-session-token` (`SessionToken`) across client/API hops guarantees monotonic read-your-writes at half the RU charge of `Strong`.

### Question 31 — C

Answer: Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency. `BoundedStaleness` enforces global write ordering across read regions within explicit `K` version and `T` time staleness limits. `Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds. Local study-map skill 2.2 (Select and Override Cosmos DB Consistency Levels and Session Tokens), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `BoundedStaleness` enforces global write ordering across read regions within explicit `K` version and `T` time staleness limits.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `BoundedStaleness` enforces global write ordering across read regions within explicit `K` version and `T` time staleness limits.
- **C:** Correct. `Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds. In this scenario: `BoundedStaleness` enforces global write ordering across read regions within explicit `K` version and `T` time staleness limits.
- **D:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `BoundedStaleness` enforces global write ordering across read regions within explicit `K` version and `T` time staleness limits.

### Question 32 — C

Answer: Create the monitored container and a dedicated lease container → call GetChangeFeedProcessorBuilder<T> with processorName and delegate → attach WithInstanceName and WithLeaseContainer → call Build and StartAsync on the processor. Provisioning the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` starts distributed processing cleanly. Both monitored and lease containers must exist before configuring the builder with instance/lease metadata, building the processor, and starting polling. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Builder options cannot be attached after Build(), and omitting the lease container causes startup failure. Why the keyed choice wins: Provisioning the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` starts distributed processing cleanly.
- **B:** Incorrect for this requirement. A processor cannot start before it is built or before its lease container exists. Why the keyed choice wins: Provisioning the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` starts distributed processing cleanly.
- **C:** Correct. Both monitored and lease containers must exist before configuring the builder with instance/lease metadata, building the processor, and starting polling. In this scenario: Provisioning the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` starts distributed processing cleanly.
- **D:** Incorrect for this requirement. Builder method order is inverted, and using a separate dedicated lease container avoids RU contention and partition-key mismatches. Why the keyed choice wins: Provisioning the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` starts distributed processing cleanly.

### Question 33 — C, E

Answers: Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay; Use Change Feed `AllVersionsAndDeletes` mode (or soft-delete flag items with short TTL in `LatestVersion` mode) because default `LatestVersion` change feed omits hard-deleted items. Distinct `processorName` values isolate each microservice's lease checkpoints, while `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) captures deleted items omitted by `LatestVersion`. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Distinct `processorName` values isolate each microservice's lease checkpoints, while `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) captures deleted items omitted by `LatestVersion`.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Distinct `processorName` values isolate each microservice's lease checkpoints, while `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) captures deleted items omitted by `LatestVersion`.
- **C:** Correct. In Change Feed Processor, `processorName` acts like an Event Hubs consumer group: distinct names receive independent copies of every insert/update, while identical names load-balance partitions. In this scenario: Distinct `processorName` values isolate each microservice's lease checkpoints, while `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) captures deleted items omitted by `LatestVersion`.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Distinct `processorName` values isolate each microservice's lease checkpoints, while `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) captures deleted items omitted by `LatestVersion`.
- **E:** Correct. Standard `LatestVersion` change feed emits only inserts and updates of current items; hard deletes require `AllVersionsAndDeletes` or soft-delete Tombstone items + TTL. In this scenario: Distinct `processorName` values isolate each microservice's lease checkpoints, while `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) captures deleted items omitted by `LatestVersion`.

### Question 34 — D

Answer: Enable container `DefaultTimeToLive = -1` (or positive seconds) and set item `ttl = 600` so Cosmos DB purges expired items automatically using background RU capacity. Setting container `DefaultTimeToLive = -1` honors per-document `ttl` expiration while retaining documents without a `ttl` field indefinitely. Container TTL must be non-null (`-1` or `>0`) for per-item `ttl` seconds to take effect; setting `DefaultTimeToLive = null` ignores item-level `ttl`. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` honors per-document `ttl` expiration while retaining documents without a `ttl` field indefinitely.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` honors per-document `ttl` expiration while retaining documents without a `ttl` field indefinitely.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` honors per-document `ttl` expiration while retaining documents without a `ttl` field indefinitely.
- **D:** Correct. Container TTL must be non-null (`-1` or `>0`) for per-item `ttl` seconds to take effect; setting `DefaultTimeToLive = null` ignores item-level `ttl`. In this scenario: Setting container `DefaultTimeToLive = -1` honors per-document `ttl` expiration while retaining documents without a `ttl` field indefinitely.

### Question 35 — C

Answer: Attach searchable key-value `Tags` (`SetTagsAsync` / `BlobUploadOptions.Tags`) and query across containers with `FindBlobsByTagsAsync("@container = 'docs' AND status = 'pending'")`. Blob `Metadata` cannot be queried server-side without enumerating blobs; setting Blob Index `Tags` (`SetTagsAsync`) enables direct `FindBlobsByTagsAsync` queries across containers. Blob Index Tags are indexed natively by Azure Storage for server-side filtering, whereas `Metadata` is not searchable without listing every blob. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Blob `Metadata` cannot be queried server-side without enumerating blobs; setting Blob Index `Tags` (`SetTagsAsync`) enables direct `FindBlobsByTagsAsync` queries across containers.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Blob `Metadata` cannot be queried server-side without enumerating blobs; setting Blob Index `Tags` (`SetTagsAsync`) enables direct `FindBlobsByTagsAsync` queries across containers.
- **C:** Correct. Blob Index Tags are indexed natively by Azure Storage for server-side filtering, whereas `Metadata` is not searchable without listing every blob. In this scenario: Blob `Metadata` cannot be queried server-side without enumerating blobs; setting Blob Index `Tags` (`SetTagsAsync`) enables direct `FindBlobsByTagsAsync` queries across containers.
- **D:** Incorrect for this requirement. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. Why the keyed choice wins: Blob `Metadata` cannot be queried server-side without enumerating blobs; setting Blob Index `Tags` (`SetTagsAsync`) enables direct `FindBlobsByTagsAsync` queries across containers.

### Question 36 — B

Answer: Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`). `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata keys. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata keys.
- **B:** Correct. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. In this scenario: `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata keys.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata keys.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata keys.

### Question 37 — D

Answer: Call `await blobClient.CreateSnapshotAsync()` for explicit point-in-time read-only checkpoints or enable account-level Blob Versioning so every `UploadAsync` overwrite retains an immutable `VersionId`. `CreateSnapshotAsync()` creates explicit read-only snapshots, while account Blob Versioning automatically retains a recoverable `VersionId` on every overwrite. Snapshots capture explicit developer-triggered checkpoints, whereas Blob Versioning automatically preserves prior state on every overwrite or delete. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `CreateSnapshotAsync()` creates explicit read-only snapshots, while account Blob Versioning automatically retains a recoverable `VersionId` on every overwrite.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `CreateSnapshotAsync()` creates explicit read-only snapshots, while account Blob Versioning automatically retains a recoverable `VersionId` on every overwrite.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `CreateSnapshotAsync()` creates explicit read-only snapshots, while account Blob Versioning automatically retains a recoverable `VersionId` on every overwrite.
- **D:** Correct. Snapshots capture explicit developer-triggered checkpoints, whereas Blob Versioning automatically preserves prior state on every overwrite or delete. In this scenario: `CreateSnapshotAsync()` creates explicit read-only snapshots, while account Blob Versioning automatically retains a recoverable `VersionId` on every overwrite.

### Question 38 — B

Answer: Invoke `BlobClient.StartCopyFromUriAsync(sourceSasUri)` to trigger asynchronous server-side blob copy and inspect `CopyStatus` without streaming bytes through the client VM. `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` monitors completion. `StartCopyFromUriAsync` instructs Azure Storage fabric to copy blobs asynchronously server-to-server using a readable source URI/SAS. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` monitors completion.
- **B:** Correct. `StartCopyFromUriAsync` instructs Azure Storage fabric to copy blobs asynchronously server-to-server using a readable source URI/SAS. In this scenario: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` monitors completion.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` monitors completion.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` monitors completion.

### Question 39 — C

Answer: Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`. Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` enforces least privilege. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` enforces least privilege.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` enforces least privilege.
- **C:** Correct. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. In this scenario: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` enforces least privilege.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` enforces least privilege.

### Question 40 — B, D

Answers: Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`); Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage. Lifecycle Management policy JSON rules automate `tierToCool` / `tierToArchive` transitions, and locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM protection. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Lifecycle Management policy JSON rules automate `tierToCool` / `tierToArchive` transitions, and locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM protection.
- **B:** Correct. Lifecycle management policies automate tier transitions and retention deletion server-side once per day without custom cron jobs. In this scenario: Lifecycle Management policy JSON rules automate `tierToCool` / `tierToArchive` transitions, and locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM protection.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Lifecycle Management policy JSON rules automate `tierToCool` / `tierToArchive` transitions, and locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM protection.
- **D:** Correct. Time-based locked retention and legal holds block modification and deletion even by Storage Account Owners until retention expires and holds clear. In this scenario: Lifecycle Management policy JSON rules automate `tierToCool` / `tierToArchive` transitions, and locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM protection.
- **E:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Lifecycle Management policy JSON rules automate `tierToCool` / `tierToArchive` transitions, and locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM protection.

### Question 41 — D

Answer: Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`). A Blob Storage Lifecycle Management policy JSON filtering `prefixMatch: ["reefer-logs/"]` with `daysAfterLastAccessTimeGreaterThan: 30` transitions unaccessed blobs server-side. Lifecycle management policies automate tier transitions and retention deletion server-side once per day without custom cron jobs. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: A Blob Storage Lifecycle Management policy JSON filtering `prefixMatch: ["reefer-logs/"]` with `daysAfterLastAccessTimeGreaterThan: 30` transitions unaccessed blobs server-side.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: A Blob Storage Lifecycle Management policy JSON filtering `prefixMatch: ["reefer-logs/"]` with `daysAfterLastAccessTimeGreaterThan: 30` transitions unaccessed blobs server-side.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: A Blob Storage Lifecycle Management policy JSON filtering `prefixMatch: ["reefer-logs/"]` with `daysAfterLastAccessTimeGreaterThan: 30` transitions unaccessed blobs server-side.
- **D:** Correct. Lifecycle management policies automate tier transitions and retention deletion server-side once per day without custom cron jobs. In this scenario: A Blob Storage Lifecycle Management policy JSON filtering `prefixMatch: ["reefer-logs/"]` with `daysAfterLastAccessTimeGreaterThan: 30` transitions unaccessed blobs server-side.

### Question 42 — D

Answer: Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob). `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` triggers high-priority rehydration that typically restores <10 GB blobs in under an hour. `SetAccessTierAsync` (or copy-to-Hot) initiates Archive rehydration; `RehydratePriority.High` prioritizes restoration (often under 1 hour for <10 GB blobs). Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` triggers high-priority rehydration that typically restores <10 GB blobs in under an hour.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` triggers high-priority rehydration that typically restores <10 GB blobs in under an hour.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` triggers high-priority rehydration that typically restores <10 GB blobs in under an hour.
- **D:** Correct. `SetAccessTierAsync` (or copy-to-Hot) initiates Archive rehydration; `RehydratePriority.High` prioritizes restoration (often under 1 hour for <10 GB blobs). In this scenario: `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` triggers high-priority rehydration that typically restores <10 GB blobs in under an hour.

### Question 43 — C, D

Answers: Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps; Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`. `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public mobile apps, and calling `AcquireTokenSilent` first with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens cleanly. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public mobile apps, and calling `AcquireTokenSilent` first with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens cleanly.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public mobile apps, and calling `AcquireTokenSilent` first with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens cleanly.
- **C:** Correct. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. In this scenario: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public mobile apps, and calling `AcquireTokenSilent` first with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens cleanly.
- **D:** Correct. MSAL refreshes cached tokens transparently during `AcquireTokenSilent`; prompting interactively on every call degrades UX and hits rate limits. In this scenario: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public mobile apps, and calling `AcquireTokenSilent` first with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens cleanly.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public mobile apps, and calling `AcquireTokenSilent` first with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens cleanly.

### Question 44 — B

Answer: Use `ConfidentialClientApplicationBuilder` authenticated with a client certificate (or workload identity assertion) calling `AcquireTokenForClient(new[] { "api://.../.default" })` for headless background daemons. `ConfidentialClientApplicationBuilder` with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://tariffs/.default" })` executes OAuth 2.0 Client Credentials without a user. Daemon apps without a signed-in user use OAuth 2.0 Client Credentials flow and must request the `.default` scope for pre-consented application permissions. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://tariffs/.default" })` executes OAuth 2.0 Client Credentials without a user.
- **B:** Correct. Daemon apps without a signed-in user use OAuth 2.0 Client Credentials flow and must request the `.default` scope for pre-consented application permissions. In this scenario: `ConfidentialClientApplicationBuilder` with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://tariffs/.default" })` executes OAuth 2.0 Client Credentials without a user.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://tariffs/.default" })` executes OAuth 2.0 Client Credentials without a user.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` with `WithCertificate` calling `AcquireTokenForClient(new[] { "api://tariffs/.default" })` executes OAuth 2.0 Client Credentials without a user.

### Question 45 — B

Answer: Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`. Calling `AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and invoking `AcquireTokenInteractive` solely inside `catch (MsalUiRequiredException)` reuses and refreshes cached tokens silently. MSAL refreshes cached tokens transparently during `AcquireTokenSilent`; prompting interactively on every call degrades UX and hits rate limits. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Calling `AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and invoking `AcquireTokenInteractive` solely inside `catch (MsalUiRequiredException)` reuses and refreshes cached tokens silently.
- **B:** Correct. MSAL refreshes cached tokens transparently during `AcquireTokenSilent`; prompting interactively on every call degrades UX and hits rate limits. In this scenario: Calling `AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and invoking `AcquireTokenInteractive` solely inside `catch (MsalUiRequiredException)` reuses and refreshes cached tokens silently.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Calling `AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and invoking `AcquireTokenInteractive` solely inside `catch (MsalUiRequiredException)` reuses and refreshes cached tokens silently.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Calling `AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and invoking `AcquireTokenInteractive` solely inside `catch (MsalUiRequiredException)` reuses and refreshes cached tokens silently.

### Question 46 — C

Answer: Declare `appRoles` with `allowedMemberTypes: ["User", "Application"]` in the Entra app registration manifest and validate the `roles` claim (`[Authorize(Roles = "...")]`) in the web API. Declaring `CraneSupervisor` under `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both human users and service principals. Entra ID emits assigned app roles inside the `roles` JWT claim for both human users and service principals without requiring directory-level Entra admin roles. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Declaring `CraneSupervisor` under `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both human users and service principals.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Declaring `CraneSupervisor` under `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both human users and service principals.
- **C:** Correct. Entra ID emits assigned app roles inside the `roles` JWT claim for both human users and service principals without requiring directory-level Entra admin roles. In this scenario: Declaring `CraneSupervisor` under `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both human users and service principals.
- **D:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Declaring `CraneSupervisor` under `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` claim for both human users and service principals.

### Question 47 — A

Answer: Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation. Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit `tid` / issuer validation enforces the contracted carrier allowlist. Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`. In this scenario: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit `tid` / issuer validation enforces the contracted carrier allowlist.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit `tid` / issuer validation enforces the contracted carrier allowlist.
- **C:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit `tid` / issuer validation enforces the contracted carrier allowlist.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) excludes personal accounts while explicit `tid` / issuer validation enforces the contracted carrier allowlist.

### Question 48 — C

Answer: Assign Storage Blob Data Contributor/Delegator RBAC to the identity → instantiate BlobServiceClient with DefaultAzureCredential → call GetUserDelegationKeyAsync for a bounded validity window → build BlobSasBuilder and sign with the user delegation key. Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) creates a User Delegation SAS. Entra RBAC must authorize delegation before BlobServiceClient requests a user delegation key, which then signs the BlobSasBuilder token without account keys. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. A SAS cannot be signed before obtaining the user delegation key, and shared account keys cannot mint Entra user delegation SAS tokens. Why the keyed choice wins: Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) creates a User Delegation SAS.
- **B:** Incorrect for this requirement. GetUserDelegationKeyAsync requires an authenticated Entra client with RBAC already granted before the call executes. Why the keyed choice wins: Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) creates a User Delegation SAS.
- **C:** Correct. Entra RBAC must authorize delegation before BlobServiceClient requests a user delegation key, which then signs the BlobSasBuilder token without account keys. In this scenario: Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) creates a User Delegation SAS.
- **D:** Incorrect for this requirement. The client must authenticate with Microsoft Entra credentials first so it can request the delegation key that mints the SAS. Why the keyed choice wins: Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) creates a User Delegation SAS.

### Question 49 — C

Answer: Bind a Service SAS to a container/queue/table Stored Access Policy (`SignedIdentifier`, omitting inline start/expiry/permissions) so compromised tokens can be revoked instantly by modifying or deleting the policy. Binding the Service SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets admins revoke that SAS instantly by deleting or modifying the stored policy. Up to 5 Stored Access Policies per container allow instant SAS revocation without rotating storage account keys; Note that User Delegation SAS uses key revocation instead of Stored Access Policies. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Binding the Service SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets admins revoke that SAS instantly by deleting or modifying the stored policy.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Binding the Service SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets admins revoke that SAS instantly by deleting or modifying the stored policy.
- **C:** Correct. Up to 5 Stored Access Policies per container allow instant SAS revocation without rotating storage account keys; Note that User Delegation SAS uses key revocation instead of Stored Access Policies. In this scenario: Binding the Service SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets admins revoke that SAS instantly by deleting or modifying the stored policy.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Binding the Service SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets admins revoke that SAS instantly by deleting or modifying the stored policy.

### Question 50 — C

Answer: Mint a short-lived HTTPS-only (`SasProtocol.HttpsOnly`) User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` instead of Account or Service SAS signed with storage account keys. Account SAS and key-signed Service SAS fail with `403` when `allowSharedKeyAccess` is `false`; User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` remains fully supported. User Delegation SAS eliminates shared storage account keys, enforces Entra RBAC, and automatically invalidates if the signing identity loses permissions. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Account SAS and key-signed Service SAS fail with `403` when `allowSharedKeyAccess` is `false`; User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` remains fully supported.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Account SAS and key-signed Service SAS fail with `403` when `allowSharedKeyAccess` is `false`; User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` remains fully supported.
- **C:** Correct. User Delegation SAS eliminates shared storage account keys, enforces Entra RBAC, and automatically invalidates if the signing identity loses permissions. In this scenario: Account SAS and key-signed Service SAS fail with `403` when `allowSharedKeyAccess` is `false`; User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` remains fully supported.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Account SAS and key-signed Service SAS fail with `403` when `allowSharedKeyAccess` is `false`; User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` remains fully supported.

### Question 51 — C, D

Answers: Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`; Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses. Using minimal read scopes with `$select` + `PageIterator<T>` streamlines paging, and batching up to 20 sub-requests via `BatchRequestContentCollection` (`/$batch`) while honoring `Retry-After` curbs throttling. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Using minimal read scopes with `$select` + `PageIterator<T>` streamlines paging, and batching up to 20 sub-requests via `BatchRequestContentCollection` (`/$batch`) while honoring `Retry-After` curbs throttling.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Using minimal read scopes with `$select` + `PageIterator<T>` streamlines paging, and batching up to 20 sub-requests via `BatchRequestContentCollection` (`/$batch`) while honoring `Retry-After` curbs throttling.
- **C:** Correct. Graph JSON batching (`/$batch`) bundles up to 20 sub-requests per round-trip, while built-in SDK retry middleware respects `Retry-After`. In this scenario: Using minimal read scopes with `$select` + `PageIterator<T>` streamlines paging, and batching up to 20 sub-requests via `BatchRequestContentCollection` (`/$batch`) while honoring `Retry-After` curbs throttling.
- **D:** Correct. Microsoft Graph enforces least-privilege consent scopes, trims payload size with `$select`, and paginates `@odata.nextLink` cleanly through `PageIterator<T>`. In this scenario: Using minimal read scopes with `$select` + `PageIterator<T>` streamlines paging, and batching up to 20 sub-requests via `BatchRequestContentCollection` (`/$batch`) while honoring `Retry-After` curbs throttling.
- **E:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Using minimal read scopes with `$select` + `PageIterator<T>` streamlines paging, and batching up to 20 sub-requests via `BatchRequestContentCollection` (`/$batch`) while honoring `Retry-After` curbs throttling.

### Question 52 — B

Answer: Call `await graphClient.Users.GetAsync(rc => { rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }; rc.QueryParameters.Filter = "accountEnabled eq true"; })`. Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` projects fields and filters server-side. In Microsoft Graph .NET SDK v5, `$select` and `$filter` query parameters reduce payload size and network transfer on collection endpoints. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` projects fields and filters server-side.
- **B:** Correct. In Microsoft Graph .NET SDK v5, `$select` and `$filter` query parameters reduce payload size and network transfer on collection endpoints. In this scenario: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` projects fields and filters server-side.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` projects fields and filters server-side.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` projects fields and filters server-side.

### Question 53 — C

Answer: Call `await confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` inside the middle-tier API. `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` performs the OAuth 2.0 On-Behalf-Of exchange. OAuth 2.0 On-Behalf-Of (`AcquireTokenOnBehalfOf`) exchanges an incoming user access token for a downstream API token while preserving delegated user identity and consent. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` performs the OAuth 2.0 On-Behalf-Of exchange.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` performs the OAuth 2.0 On-Behalf-Of exchange.
- **C:** Correct. OAuth 2.0 On-Behalf-Of (`AcquireTokenOnBehalfOf`) exchanges an incoming user access token for a downstream API token while preserving delegated user identity and consent. In this scenario: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` performs the OAuth 2.0 On-Behalf-Of exchange.
- **D:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` performs the OAuth 2.0 On-Behalf-Of exchange.

### Question 54 — B

Answer: Store environment-labeled settings and `.appconfig.featureflag/*` entries in Azure App Configuration, register `AddAzureAppConfiguration` + `AddFeatureManagement`, and watch a single `Sentinel` key with `refreshAll: true`. Watching a single `Sentinel` key with `refreshAll: true` and updating that sentinel last triggers a coordinated atomic configuration reload. Updating one sentinel key after finishing multi-key edits prevents apps from reading half-updated configuration state mid-rollout. Local study-map skill 3.5 (Manage Feature Flags, Labels, Sentinel Dynamic Refresh, and Key Vault References in Azure App Configuration), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Watching a single `Sentinel` key with `refreshAll: true` and updating that sentinel last triggers a coordinated atomic configuration reload.
- **B:** Correct. Updating one sentinel key after finishing multi-key edits prevents apps from reading half-updated configuration state mid-rollout. In this scenario: Watching a single `Sentinel` key with `refreshAll: true` and updating that sentinel last triggers a coordinated atomic configuration reload.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Watching a single `Sentinel` key with `refreshAll: true` and updating that sentinel last triggers a coordinated atomic configuration reload.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Watching a single `Sentinel` key with `refreshAll: true` and updating that sentinel last triggers a coordinated atomic configuration reload.

### Question 55 — B

Answer: Wire `options.Connect(new Uri(endpoint), cred).ConfigureKeyVault(kv => kv.SetCredential(cred))` so App Configuration resolves Key Vault reference items using the app identity. Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` supplies the credential needed to resolve Key Vault secret URIs referenced in App Configuration. App Configuration stores only the Key Vault secret URI metadata; client code still requires `ConfigureKeyVault` credentials with `Key Vault Secrets User` rights on the target vault. Local study-map skill 3.5 (Manage Feature Flags, Labels, Sentinel Dynamic Refresh, and Key Vault References in Azure App Configuration), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` supplies the credential needed to resolve Key Vault secret URIs referenced in App Configuration.
- **B:** Correct. App Configuration stores only the Key Vault secret URI metadata; client code still requires `ConfigureKeyVault` credentials with `Key Vault Secrets User` rights on the target vault. In this scenario: Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` supplies the credential needed to resolve Key Vault secret URIs referenced in App Configuration.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` supplies the credential needed to resolve Key Vault secret URIs referenced in App Configuration.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` supplies the credential needed to resolve Key Vault secret URIs referenced in App Configuration.

### Question 56 — B

Answer: Instantiate `new CryptographyClient(keyVaultKey.Id, new DefaultAzureCredential())` and invoke `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync(...)`. `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` executes envelope key wrapping without sending multi-GB black-box files to Key Vault. Envelope encryption keeps bulk data encryption keys (`DEK`) wrapped by hardware/software-protected Key Vault KEKs without sending large payloads through Key Vault. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` executes envelope key wrapping without sending multi-GB black-box files to Key Vault.
- **B:** Correct. Envelope encryption keeps bulk data encryption keys (`DEK`) wrapped by hardware/software-protected Key Vault KEKs without sending large payloads through Key Vault. In this scenario: `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` executes envelope key wrapping without sending multi-GB black-box files to Key Vault.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` executes envelope key wrapping without sending multi-GB black-box files to Key Vault.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `CryptographyClient` calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` executes envelope key wrapping without sending multi-GB black-box files to Key Vault.

### Question 57 — B

Answer: Configure App Service / Functions application settings using `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` (omitting secret version) paired with `Key Vault Secrets User` on the app Managed Identity. `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity injects rotated secrets automatically. Versionless Key Vault references automatically pull rotated secret versions within 24 hours (or immediately on config change / manual sync) with zero SDK boilerplate. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity injects rotated secrets automatically.
- **B:** Correct. Versionless Key Vault references automatically pull rotated secret versions within 24 hours (or immediately on config change / manual sync) with zero SDK boilerplate. In this scenario: `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity injects rotated secrets automatically.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity injects rotated secrets automatically.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` paired with `Key Vault Secrets User` on Managed Identity injects rotated secrets automatically.

### Question 58 — D

Answer: Choose a User-Assigned Managed Identity when multiple compute resources must share one pre-provisioned identity lifecycle independent of individual app deletions; choose System-Assigned when 1-to-1 fate-sharing tied to a single resource is required. A User-Assigned Managed Identity has a standalone lifecycle and reusable RBAC grants shared across many ephemeral compute instances, unlike 1-to-1 System-Assigned identities. System-assigned identities are deleted automatically with their parent resource; user-assigned identities have an independent ARM lifecycle and reusable RBAC grants. Local study-map skill 3.7 (Implement System-Assigned and User-Assigned Managed Identities and DefaultAzureCredential), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: A User-Assigned Managed Identity has a standalone lifecycle and reusable RBAC grants shared across many ephemeral compute instances, unlike 1-to-1 System-Assigned identities.
- **B:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: A User-Assigned Managed Identity has a standalone lifecycle and reusable RBAC grants shared across many ephemeral compute instances, unlike 1-to-1 System-Assigned identities.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: A User-Assigned Managed Identity has a standalone lifecycle and reusable RBAC grants shared across many ephemeral compute instances, unlike 1-to-1 System-Assigned identities.
- **D:** Correct. System-assigned identities are deleted automatically with their parent resource; user-assigned identities have an independent ARM lifecycle and reusable RBAC grants. In this scenario: A User-Assigned Managed Identity has a standalone lifecycle and reusable RBAC grants shared across many ephemeral compute instances, unlike 1-to-1 System-Assigned identities.

### Question 59 — C, E

Answers: Query Workspace-based Application Insights (`AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces` or classic `requests`/`dependencies`/`exceptions`) joining on `OperationId` (`operation_Id`) to reconstruct end-to-end distributed transactions; Run `AppRequests | where ResultCode == "500" | join kind=inner (AppDependencies | where Success == false) on OperationId | project TimeGenerated, Name, Target, DependencyType, ResultCode1`. Correlating tables on `OperationId` (`operation_Id`) and running a KQL `join kind=inner` between `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` isolates the failing downstream dependency. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Correlating tables on `OperationId` (`operation_Id`) and running a KQL `join kind=inner` between `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` isolates the failing downstream dependency.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Correlating tables on `OperationId` (`operation_Id`) and running a KQL `join kind=inner` between `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` isolates the failing downstream dependency.
- **C:** Correct. W3C Trace-Context propagates `traceparent` into `operation_Id` across services so KQL joins pinpoint exact failing downstream dependencies. In this scenario: Correlating tables on `OperationId` (`operation_Id`) and running a KQL `join kind=inner` between `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` isolates the failing downstream dependency.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Correlating tables on `OperationId` (`operation_Id`) and running a KQL `join kind=inner` between `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` isolates the failing downstream dependency.
- **E:** Correct. Joining `AppRequests` and `AppDependencies` on `OperationId` isolates which exact downstream SQL, HTTP, or Storage dependency triggered HTTP 500 responses. In this scenario: Correlating tables on `OperationId` (`operation_Id`) and running a KQL `join kind=inner` between `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` isolates the failing downstream dependency.

### Question 60 — D

Answer: Run `AppRequests | where TimeGenerated > ago(1h) | summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)`. Summarizing `AppRequests` over `ago(1h)` with `Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` outputs 5-minute error and p95 buckets. KQL `countif` and `percentile(..., 95)` grouped by `bin(TimeGenerated, 5m)` quantify error spikes and tail latency per operation over fixed time buckets. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Summarizing `AppRequests` over `ago(1h)` with `Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` outputs 5-minute error and p95 buckets.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Summarizing `AppRequests` over `ago(1h)` with `Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` outputs 5-minute error and p95 buckets.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Summarizing `AppRequests` over `ago(1h)` with `Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` outputs 5-minute error and p95 buckets.
- **D:** Correct. KQL `countif` and `percentile(..., 95)` grouped by `bin(TimeGenerated, 5m)` quantify error spikes and tail latency per operation over fixed time buckets. In this scenario: Summarizing `AppRequests` over `ago(1h)` with `Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` outputs 5-minute error and p95 buckets.

### Question 61 — C

Answer: Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits. In-memory telemetry channels batch asynchronously and lose unflushed items on immediate process exit; calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) plus a brief delay drains buffers cleanly. Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: In-memory telemetry channels batch asynchronously and lose unflushed items on immediate process exit; calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) plus a brief delay drains buffers cleanly.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: In-memory telemetry channels batch asynchronously and lose unflushed items on immediate process exit; calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) plus a brief delay drains buffers cleanly.
- **C:** Correct. Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics. In this scenario: In-memory telemetry channels batch asynchronously and lose unflushed items on immediate process exit; calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) plus a brief delay drains buffers cleanly.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: In-memory telemetry channels batch asynchronously and lose unflushed items on immediate process exit; calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) plus a brief delay drains buffers cleanly.

### Question 62 — B

Answer: Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`. Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively. `System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively.
- **B:** Correct. `System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro. In this scenario: Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively.

### Question 63 — A

Answer: Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group. Application Insights Standard Availability Tests check TLS expiry and HTTP status across global POPs, and a `>= 2` failed-locations alert wired to an Action Group suppresses single-region blips. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. In this scenario: Application Insights Standard Availability Tests check TLS expiry and HTTP status across global POPs, and a `>= 2` failed-locations alert wired to an Action Group suppresses single-region blips.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Application Insights Standard Availability Tests check TLS expiry and HTTP status across global POPs, and a `>= 2` failed-locations alert wired to an Action Group suppresses single-region blips.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Application Insights Standard Availability Tests check TLS expiry and HTTP status across global POPs, and a `>= 2` failed-locations alert wired to an Action Group suppresses single-region blips.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Application Insights Standard Availability Tests check TLS expiry and HTTP status across global POPs, and a `>= 2` failed-locations alert wired to an Action Group suppresses single-region blips.

### Question 64 — B

Answer: Create an Azure Monitor Metric Alert (Dynamic Thresholds or static p95 latency/5xx count) or Scheduled Query (KQL) Alert targeting an Action Group configured with webhook / Azure Function / email-SMS receivers. An Azure Monitor Metric Alert with Dynamic Thresholds adapts to weekday/weekend seasonality and triggers an Action Group targeting the Function/webhook receiver. Metric alerts offer sub-minute stateful evaluation on numeric signals, whereas Scheduled Query Rules run expressive KQL joins on log tables at configured intervals. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: An Azure Monitor Metric Alert with Dynamic Thresholds adapts to weekday/weekend seasonality and triggers an Action Group targeting the Function/webhook receiver.
- **B:** Correct. Metric alerts offer sub-minute stateful evaluation on numeric signals, whereas Scheduled Query Rules run expressive KQL joins on log tables at configured intervals. In this scenario: An Azure Monitor Metric Alert with Dynamic Thresholds adapts to weekday/weekend seasonality and triggers an Action Group targeting the Function/webhook receiver.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: An Azure Monitor Metric Alert with Dynamic Thresholds adapts to weekday/weekend seasonality and triggers an Action Group targeting the Function/webhook receiver.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: An Azure Monitor Metric Alert with Dynamic Thresholds adapts to weekday/weekend seasonality and triggers an Action Group targeting the Function/webhook receiver.

### Question 65 — A

Answer: Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group. Running a VNet-injected Timer-Triggered Function that probes the private PLC gateway and invokes `TelemetryClient.TrackAvailability()` feeds custom availability metrics and alerts. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. In this scenario: Running a VNet-injected Timer-Triggered Function that probes the private PLC gateway and invokes `TelemetryClient.TrackAvailability()` feeds custom availability metrics and alerts.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Running a VNet-injected Timer-Triggered Function that probes the private PLC gateway and invokes `TelemetryClient.TrackAvailability()` feeds custom availability metrics and alerts.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Running a VNet-injected Timer-Triggered Function that probes the private PLC gateway and invokes `TelemetryClient.TrackAvailability()` feeds custom availability metrics and alerts.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Running a VNet-injected Timer-Triggered Function that probes the private PLC gateway and invokes `TelemetryClient.TrackAvailability()` feeds custom availability metrics and alerts.

### Question 66 — A

Answer: Provision Workspace-based Application Insights and copy APPLICATIONINSIGHTS_CONNECTION_STRING → configure UseAzureMonitor() OpenTelemetry distro at startup → verify requests/dependencies in Logs → create a KQL or metric alert linked to an Action Group. Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, configuring `UseAzureMonitor()`, verifying spans in Logs, and creating an Action Group alert completes onboarding cleanly. Workspace-based Application Insights and connection-string OpenTelemetry setup emit telemetry first so KQL/metric alerts and Action Groups monitor real signals. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. Workspace-based Application Insights and connection-string OpenTelemetry setup emit telemetry first so KQL/metric alerts and Action Groups monitor real signals. In this scenario: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, configuring `UseAzureMonitor()`, verifying spans in Logs, and creating an Action Group alert completes onboarding cleanly.
- **B:** Incorrect for this requirement. Zero telemetry rate and missing connection strings discard all telemetry before it reaches Azure Monitor. Why the keyed choice wins: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, configuring `UseAzureMonitor()`, verifying spans in Logs, and creating an Action Group alert completes onboarding cleanly.
- **C:** Incorrect for this requirement. Classic Application Insights and bare Instrumentation Keys are retired in favor of Workspace-based resources and `APPLICATIONINSIGHTS_CONNECTION_STRING`. Why the keyed choice wins: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, configuring `UseAzureMonitor()`, verifying spans in Logs, and creating an Action Group alert completes onboarding cleanly.
- **D:** Incorrect for this requirement. Alert queries require a target Application Insights / Log Analytics resource and instrumented telemetry emission. Why the keyed choice wins: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, configuring `UseAzureMonitor()`, verifying spans in Logs, and creating an Action Group alert completes onboarding cleanly.

### Question 67 — B, D

Answers: Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments; Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently. `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) provides OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps stored volume without sampling Live Metrics. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) provides OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps stored volume without sampling Live Metrics.
- **B:** Correct. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. In this scenario: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) provides OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps stored volume without sampling Live Metrics.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) provides OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps stored volume without sampling Live Metrics.
- **D:** Correct. Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled. In this scenario: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) provides OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps stored volume without sampling Live Metrics.
- **E:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) provides OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps stored volume without sampling Live Metrics.

### Question 68 — D

Answer: Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments. Calling `.UseAzureMonitor()` from `Azure.Monitor.OpenTelemetry.AspNetCore` configures traces, metrics, and logs against `APPLICATIONINSIGHTS_CONNECTION_STRING`. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Calling `.UseAzureMonitor()` from `Azure.Monitor.OpenTelemetry.AspNetCore` configures traces, metrics, and logs against `APPLICATIONINSIGHTS_CONNECTION_STRING`.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Calling `.UseAzureMonitor()` from `Azure.Monitor.OpenTelemetry.AspNetCore` configures traces, metrics, and logs against `APPLICATIONINSIGHTS_CONNECTION_STRING`.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Calling `.UseAzureMonitor()` from `Azure.Monitor.OpenTelemetry.AspNetCore` configures traces, metrics, and logs against `APPLICATIONINSIGHTS_CONNECTION_STRING`.
- **D:** Correct. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. In this scenario: Calling `.UseAzureMonitor()` from `Azure.Monitor.OpenTelemetry.AspNetCore` configures traces, metrics, and logs against `APPLICATIONINSIGHTS_CONNECTION_STRING`.

### Question 69 — D

Answer: Select `Developer` (non-SLA) or `Premium` / `Standard v2` for VNet integration, and deploy the containerized APIM Self-Hosted Gateway (`mcr.microsoft.com/azure-api-management/gateway`) for hybrid on-premises/multi-cloud local traffic routing. Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway inside each terminal cluster keeps data-plane traffic local while syncing config from Azure. Self-hosted gateways require `Developer` or `Premium` tier and keep data-plane traffic local while pulling policy updates outbound over HTTPS/443 from Azure. Local study-map skill 5.1 (Provision Azure API Management Tiers, VNet Modes, and Self-Hosted Hybrid Gateways), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway inside each terminal cluster keeps data-plane traffic local while syncing config from Azure.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway inside each terminal cluster keeps data-plane traffic local while syncing config from Azure.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway inside each terminal cluster keeps data-plane traffic local while syncing config from Azure.
- **D:** Correct. Self-hosted gateways require `Developer` or `Premium` tier and keep data-plane traffic local while pulling policy updates outbound over HTTPS/443 from Azure. In this scenario: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway inside each terminal cluster keeps data-plane traffic local while syncing config from Azure.

### Question 70 — A

Answer: Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`. `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` acquires and attaches cached Entra tokens. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. Local study-map skill 5.1 (Provision Azure API Management Tiers, VNet Modes, and Self-Hosted Hybrid Gateways), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. In this scenario: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` acquires and attaches cached Entra tokens.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` acquires and attaches cached Entra tokens.
- **C:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` acquires and attaches cached Entra tokens.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` acquires and attaches cached Entra tokens.

### Question 71 — B

Answer: Use APIM `Revisions` to stage, test, and swap non-breaking internal changes safely on the same consumer URL (`;rev=2`), and use APIM `Versions` (path/header/query) when publishing breaking contract changes side-by-side for distinct consumer cohorts. `Revisions` stage and swap non-breaking edits transparently on the current URL, whereas `Versions` expose separate consumer-visible `/v1` and `/v2` endpoints side by side. Revisions let authors edit and flip the `current` implementation transparently; Versions expose distinct URLs/headers so legacy clients keep working. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `Revisions` stage and swap non-breaking edits transparently on the current URL, whereas `Versions` expose separate consumer-visible `/v1` and `/v2` endpoints side by side.
- **B:** Correct. Revisions let authors edit and flip the `current` implementation transparently; Versions expose distinct URLs/headers so legacy clients keep working. In this scenario: `Revisions` stage and swap non-breaking edits transparently on the current URL, whereas `Versions` expose separate consumer-visible `/v1` and `/v2` endpoints side by side.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `Revisions` stage and swap non-breaking edits transparently on the current URL, whereas `Versions` expose separate consumer-visible `/v1` and `/v2` endpoints side by side.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `Revisions` stage and swap non-breaking edits transparently on the current URL, whereas `Versions` expose separate consumer-visible `/v1` and `/v2` endpoints side by side.

### Question 72 — D

Answer: Use `<mock-response status-code="200" content-type="application/json" />` during frontend parallel development, or `<rewrite-uri template="/internal/v2/orders/{orderId}" />` with `<set-backend-service base-url="..." />` in `<inbound>`. `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI sample payloads early, while `<rewrite-uri>` + `<set-backend-service>` map clean public URLs onto internal routes. `<mock-response>` short-circuits backend forwarding using OpenAPI example payloads, while `<rewrite-uri>` maps public clean paths onto legacy internal routes. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI sample payloads early, while `<rewrite-uri>` + `<set-backend-service>` map clean public URLs onto internal routes.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI sample payloads early, while `<rewrite-uri>` + `<set-backend-service>` map clean public URLs onto internal routes.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI sample payloads early, while `<rewrite-uri>` + `<set-backend-service>` map clean public URLs onto internal routes.
- **D:** Correct. `<mock-response>` short-circuits backend forwarding using OpenAPI example payloads, while `<rewrite-uri>` maps public clean paths onto legacy internal routes. In this scenario: `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI sample payloads early, while `<rewrite-uri>` + `<set-backend-service>` map clean public URLs onto internal routes.

### Question 73 — A

Answer: Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation. `AuthorizationLevel.Function` mandates a valid function or host key in `x-functions-key` (or `?code=`), which APIM populates via Named Values during import. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. In this scenario: `AuthorizationLevel.Function` mandates a valid function or host key in `x-functions-key` (or `?code=`), which APIM populates via Named Values during import.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `AuthorizationLevel.Function` mandates a valid function or host key in `x-functions-key` (or `?code=`), which APIM populates via Named Values during import.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `AuthorizationLevel.Function` mandates a valid function or host key in `x-functions-key` (or `?code=`), which APIM populates via Named Values during import.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `AuthorizationLevel.Function` mandates a valid function or host key in `x-functions-key` (or `?code=`), which APIM populates via Named Values during import.

### Question 74 — B

Answer: Enable Managed Identity on the APIM instance → grant that identity RBAC or app-role access on the target backend/Key Vault → add authentication-managed-identity in APIM policy XML → test backend calls and inspect APIM trace headers. Enabling Managed Identity on APIM, granting that identity RBAC/app-role access on the backend, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying APIM trace headers completes migration safely. APIM needs an active managed identity and target RBAC/app-role grant before `<authentication-managed-identity>` can mint valid Entra bearer tokens. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Saving or invoking `<authentication-managed-identity>` before enabling Managed Identity and target RBAC fails token acquisition or returns 401/403. Why the keyed choice wins: Enabling Managed Identity on APIM, granting that identity RBAC/app-role access on the backend, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying APIM trace headers completes migration safely.
- **B:** Correct. APIM needs an active managed identity and target RBAC/app-role grant before `<authentication-managed-identity>` can mint valid Entra bearer tokens. In this scenario: Enabling Managed Identity on APIM, granting that identity RBAC/app-role access on the backend, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying APIM trace headers completes migration safely.
- **C:** Incorrect for this requirement. Hardcoding static secrets in policy XML creates rotation debt when `<authentication-managed-identity>` handles token lifecycle natively. Why the keyed choice wins: Enabling Managed Identity on APIM, granting that identity RBAC/app-role access on the backend, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying APIM trace headers completes migration safely.
- **D:** Incorrect for this requirement. Backend authorization checks the APIM gateway managed identity, not the developer workstation, and `<validate-jwt>` validates caller tokens in `<inbound>`. Why the keyed choice wins: Enabling Managed Identity on APIM, granting that identity RBAC/app-role access on the backend, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying APIM trace headers completes migration safely.

### Question 75 — A, B

Answers: Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers; Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`. Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` verification alongside `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) enforces multi-layer edge security. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Combining gateway `<validate-jwt>` pre-authentication with subscription scoping and client-certificate thumbprint checks blocks invalid traffic before hitting backends. In this scenario: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` verification alongside `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) enforces multi-layer edge security.
- **B:** Correct. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. In this scenario: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` verification alongside `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) enforces multi-layer edge security.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` verification alongside `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) enforces multi-layer edge security.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` verification alongside `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) enforces multi-layer edge security.
- **E:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` verification alongside `<validate-jwt>` (`<openid-config>`, `<audiences>`, `<required-claims>`) enforces multi-layer edge security.

### Question 76 — B

Answer: Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`. `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates caller JWTs before backend execution. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates caller JWTs before backend execution.
- **B:** Correct. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. In this scenario: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates caller JWTs before backend execution.
- **C:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates caller JWTs before backend execution.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates caller JWTs before backend execution.

### Question 77 — A, D, F

Answers: Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`; Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`; Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`. `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` satisfy every requirement. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` satisfy every requirement.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` satisfy every requirement.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` satisfy every requirement.
- **D:** Correct. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` satisfy every requirement.
- **E:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` satisfy every requirement.
- **F:** Correct. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` satisfy every requirement.

### Question 78 — D

Answer: Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`. Keeping `<base />` inside `<inbound>` alongside `<rate-limit-by-key>` (`429`) and `<quota-by-key>` (`403`) keyed on `context.Subscription?.Id` enforces both limits while preserving parent policies. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Keeping `<base />` inside `<inbound>` alongside `<rate-limit-by-key>` (`429`) and `<quota-by-key>` (`403`) keyed on `context.Subscription?.Id` enforces both limits while preserving parent policies.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Keeping `<base />` inside `<inbound>` alongside `<rate-limit-by-key>` (`429`) and `<quota-by-key>` (`403`) keyed on `context.Subscription?.Id` enforces both limits while preserving parent policies.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Keeping `<base />` inside `<inbound>` alongside `<rate-limit-by-key>` (`429`) and `<quota-by-key>` (`403`) keyed on `context.Subscription?.Id` enforces both limits while preserving parent policies.
- **D:** Correct. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! In this scenario: Keeping `<base />` inside `<inbound>` alongside `<rate-limit-by-key>` (`429`) and `<quota-by-key>` (`403`) keyed on `context.Subscription?.Id` enforces both limits while preserving parent policies.

### Question 79 — B

Answer: Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`. APIM never checks cached entries unless `<cache-lookup>` (keyed with appropriate `vary-by-header` attributes) appears inside `<inbound>` paired with `<cache-store>` inside `<outbound>`. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: APIM never checks cached entries unless `<cache-lookup>` (keyed with appropriate `vary-by-header` attributes) appears inside `<inbound>` paired with `<cache-store>` inside `<outbound>`.
- **B:** Correct. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. In this scenario: APIM never checks cached entries unless `<cache-lookup>` (keyed with appropriate `vary-by-header` attributes) appears inside `<inbound>` paired with `<cache-store>` inside `<outbound>`.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: APIM never checks cached entries unless `<cache-lookup>` (keyed with appropriate `vary-by-header` attributes) appears inside `<inbound>` paired with `<cache-store>` inside `<outbound>`.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: APIM never checks cached entries unless `<cache-lookup>` (keyed with appropriate `vary-by-header` attributes) appears inside `<inbound>` paired with `<cache-store>` inside `<outbound>`.

### Question 80 — A

Answer: Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`. `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` wraps `<forward-request />` in `<backend>`, while `<set-header name="X-AspNet-Version" exists-action="delete" />` runs in `<outbound>`. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. In this scenario: `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` wraps `<forward-request />` in `<backend>`, while `<set-header name="X-AspNet-Version" exists-action="delete" />` runs in `<outbound>`.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` wraps `<forward-request />` in `<backend>`, while `<set-header name="X-AspNet-Version" exists-action="delete" />` runs in `<outbound>`.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` wraps `<forward-request />` in `<backend>`, while `<set-header name="X-AspNet-Version" exists-action="delete" />` runs in `<outbound>`.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` wraps `<forward-request />` in `<backend>`, while `<set-header name="X-AspNet-Version" exists-action="delete" />` runs in `<outbound>`.

### Question 81 — B

Answer: Deploy the HTTPS webhook endpoint accepting POST requests → create the Event Grid subscription pointing to the endpoint → inspect incoming SubscriptionValidationEvent and read validationCode → return HTTP 200 JSON containing validationResponse (or invoke validationUrl). Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, parsing `SubscriptionValidationEvent.validationCode`, and echoing HTTP 200 `{"validationResponse": ...}` completes validation. Event Grid dispatches a SubscriptionValidationEvent during subscription creation and activates delivery only after the endpoint echoes validationResponse (or completes validationUrl). Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Event Grid requires HTTPS webhook endpoints and expects JSON `{"validationResponse": "..."}` in the response body (or GET on validationUrl). Why the keyed choice wins: Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, parsing `SubscriptionValidationEvent.validationCode`, and echoing HTTP 200 `{"validationResponse": ...}` completes validation.
- **B:** Correct. Event Grid dispatches a SubscriptionValidationEvent during subscription creation and activates delivery only after the endpoint echoes validationResponse (or completes validationUrl). In this scenario: Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, parsing `SubscriptionValidationEvent.validationCode`, and echoing HTTP 200 `{"validationResponse": ...}` completes validation.
- **C:** Incorrect for this requirement. If the endpoint is not live and returning validationResponse during creation, webhook validation fails before subscription creation completes. Why the keyed choice wins: Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, parsing `SubscriptionValidationEvent.validationCode`, and echoing HTTP 200 `{"validationResponse": ...}` completes validation.
- **D:** Incorrect for this requirement. The validation code is unique per subscription handshake and cannot be echoed before Event Grid sends the SubscriptionValidationEvent. Why the keyed choice wins: Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, parsing `SubscriptionValidationEvent.validationCode`, and echoing HTTP 200 `{"validationResponse": ...}` completes validation.

### Question 82 — C, D

Answers: Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization; Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`. Provisioning an Event Grid Domain scales thousands of RBAC-isolated shipper topics behind one endpoint, and returning `{"validationResponse": validationCode}` (or `WebHook-Allowed-Origin`) validates custom webhooks. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Provisioning an Event Grid Domain scales thousands of RBAC-isolated shipper topics behind one endpoint, and returning `{"validationResponse": validationCode}` (or `WebHook-Allowed-Origin`) validates custom webhooks.
- **B:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Provisioning an Event Grid Domain scales thousands of RBAC-isolated shipper topics behind one endpoint, and returning `{"validationResponse": validationCode}` (or `WebHook-Allowed-Origin`) validates custom webhooks.
- **C:** Correct. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. In this scenario: Provisioning an Event Grid Domain scales thousands of RBAC-isolated shipper topics behind one endpoint, and returning `{"validationResponse": validationCode}` (or `WebHook-Allowed-Origin`) validates custom webhooks.
- **D:** Correct. Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures. In this scenario: Provisioning an Event Grid Domain scales thousands of RBAC-isolated shipper topics behind one endpoint, and returning `{"validationResponse": validationCode}` (or `WebHook-Allowed-Origin`) validates custom webhooks.
- **E:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Provisioning an Event Grid Domain scales thousands of RBAC-isolated shipper topics behind one endpoint, and returning `{"validationResponse": validationCode}` (or `WebHook-Allowed-Origin`) validates custom webhooks.

### Question 83 — A

Answer: Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`. Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` preflight) and returning HTTP 200 JSON `{"validationResponse": validationCode}` proves endpoint ownership. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. In this scenario: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` preflight) and returning HTTP 200 JSON `{"validationResponse": validationCode}` proves endpoint ownership.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` preflight) and returning HTTP 200 JSON `{"validationResponse": validationCode}` proves endpoint ownership.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` preflight) and returning HTTP 200 JSON `{"validationResponse": validationCode}` proves endpoint ownership.
- **D:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` preflight) and returning HTTP 200 JSON `{"validationResponse": validationCode}` proves endpoint ownership.

### Question 84 — A

Answer: Create the Event Hub, consumer group, and Blob checkpoint container → instantiate BlobContainerClient and EventProcessorClient → register ProcessEventAsync (calling UpdateCheckpointAsync) and ProcessErrorAsync → call StartProcessingAsync before StopProcessingAsync. Creating the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition consumption. `EventProcessorClient` coordinates partition ownership and offset checkpoints in Blob Storage and requires both event and error handlers registered prior to `StartProcessingAsync`. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. `EventProcessorClient` coordinates partition ownership and offset checkpoints in Blob Storage and requires both event and error handlers registered prior to `StartProcessingAsync`. In this scenario: Creating the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition consumption.
- **B:** Incorrect for this requirement. `EventProcessorClient` throws `InvalidOperationException` if started before registering both `ProcessEventAsync` and `ProcessErrorAsync`. Why the keyed choice wins: Creating the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition consumption.
- **C:** Incorrect for this requirement. Sharing one consumer group and checkpoint prefix across distinct apps causes them to steal partitions from each other instead of each reading the full stream. Why the keyed choice wins: Creating the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition consumption.
- **D:** Incorrect for this requirement. Producers publish events and never hold partition checkpoints; `EventProcessorClient` handles balanced consumer checkpointing. Why the keyed choice wins: Creating the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition consumption.

### Question 85 — A

Answer: Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2. Event Grid is a discrete push router lacking replayable partition streams; Azure Event Hubs provides partitioned pull logs, dedicated Consumer Groups per service, and zero-code Event Hubs Capture to ADLS Gen2. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. In this scenario: Event Grid is a discrete push router lacking replayable partition streams; Azure Event Hubs provides partitioned pull logs, dedicated Consumer Groups per service, and zero-code Event Hubs Capture to ADLS Gen2.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Event Grid is a discrete push router lacking replayable partition streams; Azure Event Hubs provides partitioned pull logs, dedicated Consumer Groups per service, and zero-code Event Hubs Capture to ADLS Gen2.
- **C:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Event Grid is a discrete push router lacking replayable partition streams; Azure Event Hubs provides partitioned pull logs, dedicated Consumer Groups per service, and zero-code Event Hubs Capture to ADLS Gen2.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Event Grid is a discrete push router lacking replayable partition streams; Azure Event Hubs provides partitioned pull logs, dedicated Consumer Groups per service, and zero-code Event Hubs Capture to ADLS Gen2.

### Question 86 — B

Answer: Create the queue or subscription with RequiresSession = true at creation time → send ServiceBusMessage instances setting a non-empty SessionId → create a ServiceBusSessionProcessor (or AcceptNextSessionAsync receiver) → process messages in order and complete/renew session locks. Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = craneLaneId` on outbound messages, and consuming with `ServiceBusSessionProcessor` locks per-lane FIFO execution. `RequiresSession` can only be enabled when creating the entity, producers must populate `SessionId`, and consumers must use session-aware receivers/processors. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `RequiresSession` is immutable after creation, messages without `SessionId` are rejected on session queues, and non-session receivers fail. Why the keyed choice wins: Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = craneLaneId` on outbound messages, and consuming with `ServiceBusSessionProcessor` locks per-lane FIFO execution.
- **B:** Correct. `RequiresSession` can only be enabled when creating the entity, producers must populate `SessionId`, and consumers must use session-aware receivers/processors. In this scenario: Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = craneLaneId` on outbound messages, and consuming with `ServiceBusSessionProcessor` locks per-lane FIFO execution.
- **C:** Incorrect for this requirement. Azure Queue Storage does not support brokered `SessionId` FIFO locks; Azure Service Bus session entities are required. Why the keyed choice wins: Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = craneLaneId` on outbound messages, and consuming with `ServiceBusSessionProcessor` locks per-lane FIFO execution.
- **D:** Incorrect for this requirement. Entity creation precedes processor connection, and session queues reject messages lacking a `SessionId`. Why the keyed choice wins: Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = craneLaneId` on outbound messages, and consuming with `ServiceBusSessionProcessor` locks per-lane FIFO execution.

### Question 87 — D, E

Answers: Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering; Call `long seq = await sender.ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` and persist `seq` to call `CancelScheduledMessageAsync(seq)` if the user cancels early. Enabling `RequiresDuplicateDetection = true` + `RequiresSession = true` deduplicates retries in FIFO order, while `ScheduleMessageAsync` / `CancelScheduledMessageAsync(seq)` manages cancellable delayed warnings. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Enabling `RequiresDuplicateDetection = true` + `RequiresSession = true` deduplicates retries in FIFO order, while `ScheduleMessageAsync` / `CancelScheduledMessageAsync(seq)` manages cancellable delayed warnings.
- **B:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Enabling `RequiresDuplicateDetection = true` + `RequiresSession = true` deduplicates retries in FIFO order, while `ScheduleMessageAsync` / `CancelScheduledMessageAsync(seq)` manages cancellable delayed warnings.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Enabling `RequiresDuplicateDetection = true` + `RequiresSession = true` deduplicates retries in FIFO order, while `ScheduleMessageAsync` / `CancelScheduledMessageAsync(seq)` manages cancellable delayed warnings.
- **D:** Correct. Service Bus discards duplicate `MessageId` resends inside the history window and locks all messages sharing a `SessionId` to one active session receiver at a time. In this scenario: Enabling `RequiresDuplicateDetection = true` + `RequiresSession = true` deduplicates retries in FIFO order, while `ScheduleMessageAsync` / `CancelScheduledMessageAsync(seq)` manages cancellable delayed warnings.
- **E:** Correct. Service Bus native scheduled messages stay invisible until `ScheduledEnqueueTime` and can be canceled cleanly via their broker sequence number. In this scenario: Enabling `RequiresDuplicateDetection = true` + `RequiresSession = true` deduplicates retries in FIFO order, while `ScheduleMessageAsync` / `CancelScheduledMessageAsync(seq)` manages cancellable delayed warnings.

### Question 88 — B

Answer: Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics. Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, far beyond Azure Service Bus's 80 GB queue size limit. Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub. Local study-map skill 5.8 (Implement Queue Workflows with Azure Queue Storage SDK, Visibility Leases, PopReceipts, and Poison Handling), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, far beyond Azure Service Bus's 80 GB queue size limit.
- **B:** Correct. Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub. In this scenario: Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, far beyond Azure Service Bus's 80 GB queue size limit.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, far beyond Azure Service Bus's 80 GB queue size limit.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, far beyond Azure Service Bus's 80 GB queue size limit.

### Question 89 — D

Answer: Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`). Setting unauthenticated requests to `Return HTTP 401 Unauthorized` prevents broken HTML `302` redirects in programmatic tablet REST clients. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting unauthenticated requests to `Return HTTP 401 Unauthorized` prevents broken HTML `302` redirects in programmatic tablet REST clients.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting unauthenticated requests to `Return HTTP 401 Unauthorized` prevents broken HTML `302` redirects in programmatic tablet REST clients.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting unauthenticated requests to `Return HTTP 401 Unauthorized` prevents broken HTML `302` redirects in programmatic tablet REST clients.
- **D:** Correct. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. In this scenario: Setting unauthenticated requests to `Return HTTP 401 Unauthorized` prevents broken HTML `302` redirects in programmatic tablet REST clients.

### Question 90 — C

Answer: Instantiate `new DefaultAzureCredential()` (or explicit `ManagedIdentityCredential(clientId)` for user-assigned identities in production) so identical code authenticates via Azure CLI / Visual Studio locally and Managed Identity in Azure. `DefaultAzureCredential` resolves developer workstation credentials (`VisualStudioCredential` / `AzureCliCredential`) locally and switches automatically to Managed Identity in Azure. `DefaultAzureCredential` chains developer workstation credentials locally and IMDS Managed Identity in Azure; passing `managedIdentityClientId` is required when selecting a specific user-assigned identity. Local study-map skill 3.7 (Implement System-Assigned and User-Assigned Managed Identities and DefaultAzureCredential), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `DefaultAzureCredential` resolves developer workstation credentials (`VisualStudioCredential` / `AzureCliCredential`) locally and switches automatically to Managed Identity in Azure.
- **B:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `DefaultAzureCredential` resolves developer workstation credentials (`VisualStudioCredential` / `AzureCliCredential`) locally and switches automatically to Managed Identity in Azure.
- **C:** Correct. `DefaultAzureCredential` chains developer workstation credentials locally and IMDS Managed Identity in Azure; passing `managedIdentityClientId` is required when selecting a specific user-assigned identity. In this scenario: `DefaultAzureCredential` resolves developer workstation credentials (`VisualStudioCredential` / `AzureCliCredential`) locally and switches automatically to Managed Identity in Azure.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `DefaultAzureCredential` resolves developer workstation credentials (`VisualStudioCredential` / `AzureCliCredential`) locally and switches automatically to Managed Identity in Azure.

### Question 91 — A, C

Answers: Use `SecretClient` (`Azure.Security.KeyVault.Secrets`) for connection strings/tokens, `KeyClient` / `CryptographyClient` (`Azure.Security.KeyVault.Keys`) for RSA/EC wrap-unwrap-sign, and `CertificateClient` for X.509 lifecycle; Enable Soft Delete (mandatory on new vaults, 7–90 days) plus Purge Protection on Azure Key Vault so neither accidental deletion nor malicious principals can permanently destroy keys before retention expires. Using dedicated `SecretClient`, `KeyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete and Purge Protection satisfies both operational and security mandates. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Azure Key Vault SDK v4 splits secrets, cryptographic keys, and X.509 certificates into dedicated clients and RBAC data-plane roles (`Key Vault Secrets User`, `Crypto User`, `Certificates User`). In this scenario: Using dedicated `SecretClient`, `KeyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete and Purge Protection satisfies both operational and security mandates.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Using dedicated `SecretClient`, `KeyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete and Purge Protection satisfies both operational and security mandates.
- **C:** Correct. Soft Delete allows recovery via `StartRecoverDeletedSecretAsync`, while Purge Protection blocks permanent `PurgeDeletedSecretAsync` calls during retention. In this scenario: Using dedicated `SecretClient`, `KeyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete and Purge Protection satisfies both operational and security mandates.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Using dedicated `SecretClient`, `KeyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete and Purge Protection satisfies both operational and security mandates.
- **E:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Using dedicated `SecretClient`, `KeyClient`, and `CertificateClient` SDKs with RBAC roles plus enabling Soft Delete and Purge Protection satisfies both operational and security mandates.

### Question 92 — A

Answer: Upgrade Azure Container Registry to the `Premium` SKU and configure geo-replication into each target compute region. Upgrading Azure Container Registry to the `Premium` SKU and enabling geo-replication into each port region serves fast local pulls under one registry login server. ACR geo-replication requires the `Premium` tier and serves local regional layer pulls through a single registry login server FQDN. Local study-map skill 1.2 (Publish Images, Run ACR Tasks, and Manage Auth/Purge in Azure Container Registry), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. ACR geo-replication requires the `Premium` tier and serves local regional layer pulls through a single registry login server FQDN. In this scenario: Upgrading Azure Container Registry to the `Premium` SKU and enabling geo-replication into each port region serves fast local pulls under one registry login server.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Upgrading Azure Container Registry to the `Premium` SKU and enabling geo-replication into each port region serves fast local pulls under one registry login server.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Upgrading Azure Container Registry to the `Premium` SKU and enabling geo-replication into each port region serves fast local pulls under one registry login server.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Upgrading Azure Container Registry to the `Premium` SKU and enabling geo-replication into each port region serves fast local pulls under one registry login server.

### Question 93 — A

Answer: Use `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` (15–60 seconds or `-1` infinite) and pass `LeaseId` inside `BlobRequestConditions` on subsequent writes/deletes. Acquiring a 60-second lock via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` inside `BlobRequestConditions` rejects concurrent writers with HTTP `412`. Blob leases grant exclusive write/delete locks (`15` to `60` seconds or infinite `-1`) so competing workers immediately receive `412 LeaseIdMissing/Mismatch`. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Blob leases grant exclusive write/delete locks (`15` to `60` seconds or infinite `-1`) so competing workers immediately receive `412 LeaseIdMissing/Mismatch`. In this scenario: Acquiring a 60-second lock via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` inside `BlobRequestConditions` rejects concurrent writers with HTTP `412`.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Acquiring a 60-second lock via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` inside `BlobRequestConditions` rejects concurrent writers with HTTP `412`.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Acquiring a 60-second lock via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` inside `BlobRequestConditions` rejects concurrent writers with HTTP `412`.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Acquiring a 60-second lock via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` inside `BlobRequestConditions` rejects concurrent writers with HTTP `412`.

### Question 94 — C

Answer: Disable the ACR admin account and assign the built-in `AcrPull` role on the registry to the compute resource managed identity. Disabling the ACR admin user, granting `AcrPull` on ACR to the Web App's Managed Identity, and enabling Managed Identity registry authentication pulls layers without static passwords. `AcrPull` with Managed Identity eliminates shared registry passwords while granting least-privilege read-only image pulls. Local study-map skill 1.7 (Deploy Code, Run-From-Package ZIPs, and Custom Containers to App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Disabling the ACR admin user, granting `AcrPull` on ACR to the Web App's Managed Identity, and enabling Managed Identity registry authentication pulls layers without static passwords.
- **B:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Disabling the ACR admin user, granting `AcrPull` on ACR to the Web App's Managed Identity, and enabling Managed Identity registry authentication pulls layers without static passwords.
- **C:** Correct. `AcrPull` with Managed Identity eliminates shared registry passwords while granting least-privilege read-only image pulls. In this scenario: Disabling the ACR admin user, granting `AcrPull` on ACR to the Web App's Managed Identity, and enabling Managed Identity registry authentication pulls layers without static passwords.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Disabling the ACR admin user, granting `AcrPull` on ACR to the Web App's Managed Identity, and enabling Managed Identity registry authentication pulls layers without static passwords.

### Question 95 — C

Answer: Host `EventProcessorClient` backed by `BlobContainerClient` and call `await eventArgs.UpdateCheckpointAsync()` after idempotent batch persistence so partition leases resume cleanly after rebalancing. Hosting `EventProcessorClient` backed by `BlobContainerClient` and calling `await eventArgs.UpdateCheckpointAsync()` after idempotent persistence coordinates partition leases and checkpoints cleanly. `EventProcessorClient` coordinates partition ownership via Azure Blob leases and records per-partition sequence/offset checkpoints in Blob metadata. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Hosting `EventProcessorClient` backed by `BlobContainerClient` and calling `await eventArgs.UpdateCheckpointAsync()` after idempotent persistence coordinates partition leases and checkpoints cleanly.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Hosting `EventProcessorClient` backed by `BlobContainerClient` and calling `await eventArgs.UpdateCheckpointAsync()` after idempotent persistence coordinates partition leases and checkpoints cleanly.
- **C:** Correct. `EventProcessorClient` coordinates partition ownership via Azure Blob leases and records per-partition sequence/offset checkpoints in Blob metadata. In this scenario: Hosting `EventProcessorClient` backed by `BlobContainerClient` and calling `await eventArgs.UpdateCheckpointAsync()` after idempotent persistence coordinates partition leases and checkpoints cleanly.
- **D:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Hosting `EventProcessorClient` backed by `BlobContainerClient` and calling `await eventArgs.UpdateCheckpointAsync()` after idempotent persistence coordinates partition leases and checkpoints cleanly.

### Question 96 — B

Answer: Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL. Publishing `CloudEvents v1.0` events filtered by `subjectBeginsWith: "/region/eu-west/"` and `advancedFilters` with a configured Blob dead-letter container routes regional excursions reliably. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Publishing `CloudEvents v1.0` events filtered by `subjectBeginsWith: "/region/eu-west/"` and `advancedFilters` with a configured Blob dead-letter container routes regional excursions reliably.
- **B:** Correct. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. In this scenario: Publishing `CloudEvents v1.0` events filtered by `subjectBeginsWith: "/region/eu-west/"` and `advancedFilters` with a configured Blob dead-letter container routes regional excursions reliably.
- **C:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Publishing `CloudEvents v1.0` events filtered by `subjectBeginsWith: "/region/eu-west/"` and `advancedFilters` with a configured Blob dead-letter container routes regional excursions reliably.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Publishing `CloudEvents v1.0` events filtered by `subjectBeginsWith: "/region/eu-west/"` and `advancedFilters` with a configured Blob dead-letter container routes regional excursions reliably.

### Question 97 — D

Answer: Set `--revision-mode multiple` and apply `az containerapp ingress traffic set --revision-weight` to split live HTTP requests across named revisions. Enabling `--revision-mode multiple` and applying `az containerapp ingress traffic set --revision-weight` splits live HTTP traffic across active revisions. Multiple-revision mode keeps more than one revision active simultaneously for weighted blue/green or canary traffic splitting. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling `--revision-mode multiple` and applying `az containerapp ingress traffic set --revision-weight` splits live HTTP traffic across active revisions.
- **B:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Enabling `--revision-mode multiple` and applying `az containerapp ingress traffic set --revision-weight` splits live HTTP traffic across active revisions.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Enabling `--revision-mode multiple` and applying `az containerapp ingress traffic set --revision-weight` splits live HTTP traffic across active revisions.
- **D:** Correct. Multiple-revision mode keeps more than one revision active simultaneously for weighted blue/green or canary traffic splitting. In this scenario: Enabling `--revision-mode multiple` and applying `az containerapp ingress traffic set --revision-weight` splits live HTTP traffic across active revisions.

### Question 98 — C

Answer: Use Azure Service Bus Topics with `SqlRuleFilter` / `CorrelationRuleFilter` (`CorrelationRuleFilter` preferred for high throughput) and `SqlRuleAction` header stamping, inspecting `$DeadLetterQueue` (`SubQueue.DeadLetter`) after `MaxDeliveryCount` expires. Configuring a Topic Subscription with `SqlRuleFilter` (`hazmat = true`), `SqlRuleAction` (`SET Priority = 'High'`), and `MaxDeliveryCount = 5` routing poison retries to `$DeadLetterQueue` fulfills all three rules. `CorrelationRuleFilter` matches brokered/application properties in-memory far faster than SQL evaluation, while `MaxDeliveryCount` isolates poison messages in the sub-queue DLQ. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Configuring a Topic Subscription with `SqlRuleFilter` (`hazmat = true`), `SqlRuleAction` (`SET Priority = 'High'`), and `MaxDeliveryCount = 5` routing poison retries to `$DeadLetterQueue` fulfills all three rules.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Configuring a Topic Subscription with `SqlRuleFilter` (`hazmat = true`), `SqlRuleAction` (`SET Priority = 'High'`), and `MaxDeliveryCount = 5` routing poison retries to `$DeadLetterQueue` fulfills all three rules.
- **C:** Correct. `CorrelationRuleFilter` matches brokered/application properties in-memory far faster than SQL evaluation, while `MaxDeliveryCount` isolates poison messages in the sub-queue DLQ. In this scenario: Configuring a Topic Subscription with `SqlRuleFilter` (`hazmat = true`), `SqlRuleAction` (`SET Priority = 'High'`), and `MaxDeliveryCount = 5` routing poison retries to `$DeadLetterQueue` fulfills all three rules.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Configuring a Topic Subscription with `SqlRuleFilter` (`hazmat = true`), `SqlRuleAction` (`SET Priority = 'High'`), and `MaxDeliveryCount = 5` routing poison retries to `$DeadLetterQueue` fulfills all three rules.

### Question 99 — A

Answer: Use `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false`, calling `CompleteMessageAsync` after commit, `AbandonMessageAsync` for transient retries, and `DeadLetterMessageAsync` on unrecoverable schema errors. Running `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false` and calling `CompleteMessageAsync`, `AbandonMessageAsync`, or `DeadLetterMessageAsync` preserves broker durability and poison control. `ReceiveAndDelete` loses messages if a worker crashes mid-processing; `PeekLock` retains broker durability until explicit settlement or lock expiry. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. `ReceiveAndDelete` loses messages if a worker crashes mid-processing; `PeekLock` retains broker durability until explicit settlement or lock expiry. In this scenario: Running `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false` and calling `CompleteMessageAsync`, `AbandonMessageAsync`, or `DeadLetterMessageAsync` preserves broker durability and poison control.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Running `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false` and calling `CompleteMessageAsync`, `AbandonMessageAsync`, or `DeadLetterMessageAsync` preserves broker durability and poison control.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Running `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false` and calling `CompleteMessageAsync`, `AbandonMessageAsync`, or `DeadLetterMessageAsync` preserves broker durability and poison control.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Running `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false` and calling `CompleteMessageAsync`, `AbandonMessageAsync`, or `DeadLetterMessageAsync` preserves broker durability and poison control.

### Question 100 — A

Answer: Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`. Calling `ReceiveMessagesAsync` first and passing both `MessageId` and the current `PopReceipt` to `UpdateMessageAsync` and `DeleteMessageAsync` (while checking `DequeueCount`) manages leases properly. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. Local study-map skill 5.8 (Implement Queue Workflows with Azure Queue Storage SDK, Visibility Leases, PopReceipts, and Poison Handling), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. In this scenario: Calling `ReceiveMessagesAsync` first and passing both `MessageId` and the current `PopReceipt` to `UpdateMessageAsync` and `DeleteMessageAsync` (while checking `DequeueCount`) manages leases properly.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Calling `ReceiveMessagesAsync` first and passing both `MessageId` and the current `PopReceipt` to `UpdateMessageAsync` and `DeleteMessageAsync` (while checking `DequeueCount`) manages leases properly.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Calling `ReceiveMessagesAsync` first and passing both `MessageId` and the current `PopReceipt` to `UpdateMessageAsync` and `DeleteMessageAsync` (while checking `DequeueCount`) manages leases properly.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Calling `ReceiveMessagesAsync` first and passing both `MessageId` and the current `PopReceipt` to `UpdateMessageAsync` and `DeleteMessageAsync` (while checking `DequeueCount`) manages leases properly.
