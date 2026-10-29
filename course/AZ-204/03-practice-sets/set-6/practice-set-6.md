# Microsoft Exam AZ-204: Developing Solutions for Microsoft Azure — Full-Length Mock Exam 6

Exam AZ-204 (Digital Media Streaming, Live Ticketing, Gaming Backends, and Smart Energy) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Credential Lifecycle Notice:** Microsoft retired Exam AZ-204 (`Microsoft Certified: Azure Developer Associate`) on **July 31, 2026** and succeeded it with **Exam AI-200 (`Azure AI Cloud Developer Associate`)**. This practice bank preserves the final official January 14, 2026 AZ-204 skills-measured baseline for archival certification prep, enterprise Azure developer benchmarking, and core compute/storage/security/monitoring/integration mastery.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` SDK/CLI/XML/JSON/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area code dropdowns, split-pane tabbed case exhibits, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn documentation — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. A live-streaming transcoder API in .NET 8 needs compact runtime container images free of SDK compilers plus clean `SIGTERM` graceful draining when live match servers scale in. Which two Dockerfile practices apply? Select two.

Domain: Develop Azure compute solutions

- A. Declare `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form so `SIGTERM` reaches the .NET host cleanly during container shutdown
- B. Use a multi-stage Dockerfile building in `mcr.microsoft.com/dotnet/sdk:8.0` and copying published output into `mcr.microsoft.com/dotnet/aspnet:8.0` with a non-root `USER app`
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- E. Keep the default `--restart-policy Always` on a run-once batch container group

### 2. Game-backend engineers running `az acr build` accidentally upload 3.1 GB of local Unity asset caches, `bin/`, `obj/`, and `.env` files on every build. Which single repository file excludes those paths from build uploads?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Add `bin/`, `obj/`, `.git/`, and local `.env` files to `.dockerignore` before running `docker build` or `az acr build`
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 3. Multiplayer matchmaker containers deploy simultaneously in Tokyo, Frankfurt, and Virginia and require low-latency regional layer pulls through a single ACR login server FQDN. Which ACR tier and feature are required?

Domain: Develop Azure compute solutions

- A. Upgrade Azure Container Registry to the `Premium` SKU and configure geo-replication into each target compute region
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 4. Broadcast security forbids workstation Docker pulls from public registries, requiring DevOps pipelines to copy `ffmpeg` Alpine base images server-side into private ACR (` ____ `). Which CLI command performs this?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Execute `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine`
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 5. Post-concert highlight reels render inside Azure Container Instances for eight minutes, exit with status `0`, and must stop accruing per-second vCPU charges immediately upon completion while retrying non-zero crashes. Which restart policy fits?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Set `--restart-policy OnFailure` (or `Never`) on the Azure Container Instances container group so batch containers stop billing vCPU/memory seconds once exit code 0 completes
- D. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision

### 6. An HLS manifest packager running on Linux ACI needs a local Nginx caching sidecar reachable over `127.0.0.1:8081` sharing a transient `emptyDir` scratch volume. How should ACI be structured?

Domain: Develop Azure compute solutions

- A. Deploy the application container and Envoy/logging sidecar inside one multi-container ACI group sharing `localhost` network namespace and an `emptyDir` / Azure Files volume
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 7. A smart-meter tariff microservice must run inside a subnet-injected Container Apps environment whose Envoy load balancer exposes zero public internet IP addresses (` ____ `). Which CLI command provisions this private environment?

Domain: Develop Azure compute solutions

- A. Execute `az containerapp env create --name <envName> --resource-group <rg> --infrastructure-subnet-resource-id <subnetId> --internal-only`
- B. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 8. EmberPlay's multiplayer backend on Container Apps wants telemetry processors to sleep at zero pods when queues drain using passwordless scaler auth, confine Dapr state store visibility solely to `match-scorer`, and inject DRM secrets from Key Vault without plaintext YAML strings. Which three features accomplish this? Select three.

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- D. Define a Container App secret using `keyVaultUrl` plus `identity` (managed identity resource ID or `system`) and map container environment variables via `secretRef`
- E. Register a Dapr state or pub/sub component in the Container Apps environment and restrict access via the component `scopes` array to specific `daprAppId` values
- F. Configure a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0` and Managed Identity (`identity` property) so replicas scale to zero when idle and wake on queue depth

### 9. Every hour on the hour, 24 parallel worker shards calculate regional solar-grid feed-in settlements for four minutes and shut down completely without open HTTP ports. Which Container Apps resource matches this workload?

Domain: Develop Azure compute solutions

- A. Deploy an Azure Container Apps Job (`triggerType: Event` or `Schedule`) with `replicaCompletionCount` and `parallelism` instead of an always-listening HTTP container app
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision

### 10. Proposed solution: Host a live concert-ticketing web app on a `Basic (B3)` App Service plan so engineers can configure pre-sale staging slots and automatic queue/CPU horizontal scaling. Why does this fail, and which plan tier resolves it?

Domain: Develop Azure compute solutions

- A. Provision at least a `Standard` (`S1+`) or `Premium v3` (`P1v3+`) App Service plan to unlock deployment slots, custom domain SNI SSL, and metric/schedule autoscaling
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 11. A containerized .NET 8 podcast-directory API adopts Microsoft's non-root `aspnet:8.0` base image (` ____ `) and needs its unprivileged HTTP port matched with ingress routing. Which Dockerfile statements configure the default .NET 8 port?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Set `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` inside the final `.NET 8` runtime stage and match `targetPort: 8080` on Container Apps ingress
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 12. Broadcast regulators require 180-day retention of Web Server and Application logs from a scaled-out App Service streaming portal without automatic 12-hour shutoff. How must App Service diagnostics be configured?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 13. During a live halftime show spike, an engineer wants real-time stdout trace output from a Linux App Service scoreboard API streamed straight to their shell (` ____ `). Which CLI commands attach the stream?

Domain: Develop Azure compute solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 14. Deploying updated assemblies to a high-concurrency newsroom App Service app during breaking news causes locked-DLL failures in `wwwroot`. Which deployment setting mounts packages atomically as read-only?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Set `WEBSITE_RUN_FROM_PACKAGE=1` and deploy with `az webapp deploy --type zip` so the app mounts the read-only ZIP package directly with atomic cold-start replacement
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 15. A containerized DRM license server on Linux App Service pulls images from ACR after security disables `--admin-enabled`. How should passwordless pulls be configured?

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Disable the ACR admin account and assign the built-in `AcrPull` role on the registry to the compute resource managed identity
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 16. NovaGrid's outage-reporting web app must reject plaintext HTTP and TLS 1.0/1.1 ciphers while requiring substation X.509 client certs, and its CI script must set `LedgerDb` as a slot-bound SQL connection string. Which two App Service actions satisfy both requirements? Select two.

Domain: Develop Azure compute solutions

- A. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `httpsOnly: true`, set `minTlsVersion: "1.2"` (or `"1.3"`), and configure `clientCertEnabled` when mutual TLS client certificates are required
- E. Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`

### 17. A web player at `https://watch.emberplay.example` makes credentialed API requests to `https://api.emberplay.example` on App Service, and wildcard `*` CORS fails preflight validation in browsers. How must CORS be configured?

Domain: Develop Azure compute solutions

- A. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Configure App Service `CORS` with explicit origin URLs (and `supportCredentials` only without wildcard `*`) so App Service handles preflight `OPTIONS` requests
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 18. Stadium ticket drops spike App Service CPU, and poorly separated autoscale rules (`>72%` out, `<70%` in, 1-min cooldown) cause instances to add and terminate repeatedly every two minutes. How should the rules be fixed?

Domain: Develop Azure compute solutions

- A. Pair every scale-out metric rule (e.g., CPU > 75% for 10 min) with a conservative scale-in rule (e.g., CPU < 35%) and an explicit `coolDown` window plus safe default/max instance bounds
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`

### 19. Before swapping a video-recommendation App Service slot into `Production`, every worker must finish warming a 500 MB embedding index and return HTTP `200` on `/warmup/ready`. Which App Service settings enforce this?

Domain: Develop Azure compute solutions

- A. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- B. Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 20. After swapping `Staging` into `Production` on Lyric Arena's box-office portal, live purchases accidentally point to the sandbox ad-yen gateway configured on `Staging`. Which flag keeps gateway settings pinned to their own slot?

Domain: Develop Azure compute solutions

- A. Mark environment-specific settings such as `PaymentWebhookUrl` and production connection strings as `slotSetting: true` (Deployment slot setting) before swapping slots
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 21. A broadcast loudness-normalization Function App runs 20-minute audio passes, connects outbound to a private-VNet media store, and needs pre-warmed workers for breaking-news clips. Which Functions plan fits all three needs?

Domain: Develop Azure compute solutions

- A. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Host the Function App on `Flex Consumption` or `Elastic Premium (EP1+)` when VNet integration, longer execution timeouts beyond 10 minutes, or pre-warmed/always-ready instances are required

### 22. EmberPlay's anti-cheat Function host needs all functions capped at ten minutes while keeping every `Request` and `Exception` record exempt from Application Insights sampling (`host.json`: ` ____ `). Which global host setting accomplishes both?

Domain: Develop Azure compute solutions

- A. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- B. Configure `"functionTimeout": "00:10:00"` and `"logging": { "applicationInsights": { "samplingSettings": { "isEnabled": true, "excludedTypes": "Request;Exception" } } }` inside `host.json`
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 23. An esports .NET 8 isolated-worker Function App has an HTTP match-report endpoint that writes to Cosmos DB while returning HTTP 201 without `out` parameters, plus a second function triggered automatically by leaderboard updates in Cosmos DB. Which two C# patterns apply? Select two.

Domain: Develop Azure compute solutions

- A. In the .NET isolated worker model, return a custom POCO class uniting `[HttpResult]` (or `HttpResponseData`) with `[CosmosDBOutput]` / `[ServiceBusOutput]` properties
- B. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 24. A smart-meter `[EventHubTrigger]` Function occasionally encounters brief downstream throttling and should retry 5 times with exponential backoff (`4s` to `60s`) before moving its checkpoint (` ____ `). Which C# attribute configures this?

Domain: Develop Azure compute solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Apply `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` (or `[FixedDelayRetry]`) on the `[EventHubTrigger]` / `[TimerTrigger]` function
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`

### 25. An energy-market tariff sync `[TimerTrigger(" ____ ")]` Function must run every 15 minutes during weekday market hours (`09:00–17:45`, Mon–Fri). Which six-field NCRONTAB expression sets this schedule?

Domain: Develop Azure compute solutions

- A. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Specify a six-field NCRONTAB expression `{second} {minute} {hour} {day} {month} {day-of-week}` such as `"0 */15 9-17 * * 1-5"` on `[TimerTrigger]`
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 26. Photojournalists upload 60,000 RAW press photos per hour into Blob Storage, and default log-polling `[BlobTrigger]` Functions lag behind breaking news. How should `[BlobTrigger]` be reconfigured for sub-second push activation?

Domain: Develop Azure compute solutions

- A. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Configure `[BlobTrigger(..., Source = BlobTriggerSource.EventGrid)]` with an Event Grid system topic subscription instead of default container-log polling
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 27. An MMO player-inventory service on Cosmos DB for NoSQL needs socket-safe singleton `CosmosClient` reuse, atomic multi-item loot trades within a single `/guildVaultId` partition, and lightweight server-side `/retryCount` increments without fetching 100 KB player profiles. Which three SDK patterns apply? Select three.

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `await container.PatchItemAsync<Order>(id, new PartitionKey(pk), new[] { PatchOperation.Increment("/retryCount", 1), PatchOperation.Set("/lastStatus", "Queued") })`
- C. Register `CosmosClient` as a process-wide singleton in dependency injection and choose a high-cardinality `PartitionKey` path (or up to 3-level `Hierarchical` subpartition paths) that distributes RU/s evenly
- D. Use `container.CreateTransactionalBatch(new PartitionKey(pkValue))` to group multiple create/replace/upsert/delete operations atomically within the same logical partition
- E. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- F. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 28. Smart-grid utilities on Cosmos DB store meter readings where large municipal `/tenantId` partitions exceed 20 GB, yet dashboards still filter efficiently by `/tenantId` and `/siteId` (`new ContainerProperties("telemetry", ____ )`). Which partitioning feature solves this?

Domain: Develop for Azure storage

- A. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- B. Define `new ContainerProperties(id: "telemetry", partitionKeyPaths: new List<string> { "/tenantId", "/siteId", "/deviceId" })` using `PartitionKeyBuilder` on reads and writes
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 29. A ticketing history endpoint streams a fan's past orders in 100-item pages scoped to one partition key while logging `RequestCharge` per page (`FeedIterator<Order> iter = ____ `). Which C# SDK v3 loop implements this?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use `FeedIterator<Order> iter = container.GetItemQueryIterator<Order>(queryDef, requestOptions: new QueryRequestOptions { PartitionKey = new PartitionKey(pk), MaxItemCount = 100 })` and loop `while (iter.HasMoreResults) { FeedResponse<Order> page = await iter.ReadNextAsync(); }`
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 30. When a gamer equips a new skin in a lobby backed by Cosmos DB, subsequent API calls across stateless lobby servers must reflect that gamer's update immediately at half the read RU cost of `Strong`. Which consistency setup works?

Domain: Develop for Azure storage

- A. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- B. Use `Session` consistency (the default) and propagate `x-ms-session-token` (`RequestOptions.SessionToken`) across client/middle-tier hops to guarantee monotonic read-your-own-writes at half the read RU cost of `Strong`
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 31. Global tournament scoreboards read from four Cosmos DB regions and require globally ordered score updates lagging the primary region by no more than `T = 5` seconds or `K = 100` writes. Which consistency level satisfies this?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency
- D. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction

### 32. A real-time royalty-accounting worker in .NET 8 must stream every track-play summary inserted or updated in Cosmos DB using the Change Feed Processor builder. Which ordered sequence initializes and starts the processor?

Domain: Develop for Azure storage

- A. Create the monitored container and a dedicated lease container → call GetChangeFeedProcessorBuilder<T> with processorName and delegate → attach WithInstanceName and WithLeaseContainer → call Build and StartAsync on the processor
- B. Attach WithLeaseContainer pointing to the monitored container without /id partition → call StartAsync → call GetChangeFeedProcessorBuilder<T> → call Build
- C. Create only the monitored container → call Build and StartAsync → attach WithLeaseContainer → define the handler delegate
- D. Call StartAsync on the processor → call GetChangeFeedProcessorBuilder<T> → create the lease container → attach WithInstanceName

### 33. Both a trending-videos recommender and a copyright-audit worker must consume every Cosmos DB media-asset update independently, and Takedown-deleted assets must also emit change notifications. Which two Change Feed designs apply? Select two.

Domain: Develop for Azure storage

- A. Use Change Feed `AllVersionsAndDeletes` mode (or soft-delete flag items with short TTL in `LatestVersion` mode) because default `LatestVersion` change feed omits hard-deleted items
- B. Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- E. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 34. A newsroom video archive stores 60 million clip blobs across 100 containers and needs sub-second server-side queries for `@container = 'docs' AND status = 'pending'` (`await serviceClient. ____ `). Which Blob Storage feature enables this without listing blobs?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Attach searchable key-value `Tags` (`SetTagsAsync` / `BlobUploadOptions.Tags`) and query across containers with `FindBlobsByTagsAsync("@container = 'docs' AND status = 'pending'")`
- C. Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`)
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 35. A podcast publisher uploads `.mp3` blobs and needs to set `Content-Type: audio/mpeg` plus custom `episode_code` user metadata (`x-ms-meta-episode_code`) via `Azure.Storage.Blobs` (` ____ `). Which two SDK calls apply these properly?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`)

### 36. Graphic designers overwrite stadium-poster `.psd` blobs repeatedly, and creative directors want every `UploadAsync` overwrite to preserve an automatic recoverable `VersionId` without modifying designer tools. What should be enabled?

Domain: Develop for Azure storage

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Call `await blobClient.CreateSnapshotAsync()` for explicit point-in-time read-only checkpoints or enable account-level Blob Versioning so every `UploadAsync` overwrite retains an immutable `VersionId`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 37. Four live-captioning workers coordinate updates to `stream-manifest.m3u8` in Blob Storage and must lock the blob exclusively for 60 seconds so competing writers fail fast with HTTP `412`. Which SDK mechanism enforces this?

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Use `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` (15–60 seconds or `-1` infinite) and pass `LeaseId` inside `BlobRequestConditions` on subsequent writes/deletes

### 38. After a festival wraps, an archiver copies 8 TB of 4K master `.mov` blobs to a vault storage account (`await destBlob. ____ `) without streaming video bytes through the orchestrator container. Which SDK method performs server-side copy?

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Invoke `BlobClient.StartCopyFromUriAsync(sourceSasUri)` to trigger asynchronous server-side blob copy and inspect `CopyStatus` without streaming bytes through the client VM
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 39. A press-kit API generates a 15-minute HTTPS-only read SAS scoped solely to blob `exports/manifest.csv` (`new BlobSasBuilder { ____ }`). Which builder setup enforces single-blob read-only access?

Domain: Develop for Azure storage

- A. Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 40. Energy-regulator outage recordings in Blob Storage must remain WORM-locked against deletion by any admin for 5 years, and urgent NERC audit subpoenas on <10 GB `Archive`-tier files must restore within an hour. Which two Blob capabilities solve both needs? Select two.

Domain: Develop for Azure storage

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob)
- E. Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage

### 41. A desktop broadcast-editing app built on WinUI 3 signs journalists in with Microsoft Entra ID without embedded secrets and refreshes asset-API tokens silently from cache across long editing sessions. Which two MSAL patterns apply? Select two.

Domain: Implement Azure security

- A. Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`
- B. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- E. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)

### 42. A headless royalty-payout daemon authenticates with an X.509 certificate at 03:00 UTC and requests app-only Entra tokens for `api://royalties/.default` (` ____ `). Which MSAL builder and method apply?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Use `ConfidentialClientApplicationBuilder` authenticated with a client certificate (or workload identity assertion) calling `AcquireTokenForClient(new[] { "api://.../.default" })` for headless background daemons

### 43. When a news producer calls an ASP.NET Core Assignment API with their Entra user bearer token, the API must exchange that token (` ____ `) to post a schedule card to Microsoft Graph on the producer's behalf. Which MSAL call performs this?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Call `await confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` inside the middle-tier API

### 44. A grid load-shedding API (`[Authorize(Roles = "GridOperator")]`) must authorize both human control-room engineers and an automated frequency-response service principal. How must `GridOperator` be defined in Entra ID?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- C. Declare `appRoles` with `allowedMemberTypes: ["User", "Application"]` in the Entra app registration manifest and validate the `roles` claim (`[Authorize(Roles = "...")]`) in the web API
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 45. A syndication portal lets editors from 150 partner newspaper Entra tenants sign in while rejecting personal Microsoft accounts and uncontracted `tid` tenants. How should authentication be configured?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation

### 46. Smart-home inverter gateways calling an App Service API protected by Easy Auth fail whenever expired tokens trigger `302 Redirect` HTML sign-in pages instead of HTTP status errors. Which Easy Auth setting fixes this?

Domain: Implement Azure security

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 47. Creator mobile apps need 15-minute HTTPS upload URLs for 4K vlog clips signed with Microsoft Entra credentials because storage account Shared Keys are disabled. Which ordered steps mint the User Delegation SAS?

Domain: Implement Azure security

- A. Call GetUserDelegationKeyAsync anonymously → build BlobSasBuilder → assign RBAC to the identity → instantiate BlobServiceClient
- B. Build BlobSasBuilder and sign → call GetUserDelegationKeyAsync → instantiate BlobServiceClient with shared account key → assign RBAC to the identity
- C. Assign Storage Blob Data Contributor/Delegator RBAC to the identity → instantiate BlobServiceClient with DefaultAzureCredential → call GetUserDelegationKeyAsync for a bounded validity window → build BlobSasBuilder and sign with the user delegation key
- D. Instantiate BlobServiceClient with SAS token → assign RBAC → build BlobSasBuilder → call GetUserDelegationKeyAsync

### 48. Proposed solution: Issue a 60-day inline Service SAS signed with `accountKey1` to an external press agency and expect to revoke just that agency's token without rotating `accountKey1`. Why does this fail, and what fixes it?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Bind a Service SAS to a container/queue/table Stored Access Policy (`SignedIdentifier`, omitting inline start/expiry/permissions) so compromised tokens can be revoked instantly by modifying or deleting the policy

### 49. All stadium ticketing storage accounts enforce `allowSharedKeyAccess: false`; which SAS mechanism allows the mobile-ticket API to continue issuing 5-minute Apple Wallet pass download links?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Mint a short-lived HTTPS-only (`SasProtocol.HttpsOnly`) User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` instead of Account or Service SAS signed with storage account keys
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 50. A studio crew-scheduling app pages through 14,000 production staff in Microsoft Graph using minimal permissions and bundles 16 studio room-calendar checks into single JSON batch calls respecting `429 Retry-After`. Which two Graph SDK practices apply? Select two.

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`
- E. Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses

### 51. Using Microsoft Graph .NET SDK v5, a broadcast roster service queries active staff (`accountEnabled eq true`) returning solely `id`, `displayName`, and `mail` (`await graphClient.Users.GetAsync( ____ )`). Which configuration completes the query?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Call `await graphClient.Users.GetAsync(rc => { rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }; rc.QueryParameters.Filter = "accountEnabled eq true"; })`

### 52. Proposed solution: Fire 18 sequential HTTP calls to Microsoft Graph on every newsroom dashboard load and immediately retry in a tight `while(true)` loop whenever HTTP `429` arrives. Why does this worsen throttling, and what fixes it?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 53. An esports matchmaking API loads feature flags and Key Vault references from Azure App Configuration (`options.Connect(uri, cred). ____ `), failing at startup until Key Vault credential resolution is wired. Which method call completes startup?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Wire `options.Connect(new Uri(endpoint), cred).ConfigureKeyVault(kv => kv.SetCredential(cred))` so App Configuration resolves Key Vault reference items using the app identity
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 54. A DRM content-protection platform stores database secrets, Widevine/FairPlay RSA keys, and TLS certificates in Azure Key Vault and requires mandatory 90-day protection against permanent key purge. Which two Key Vault practices apply? Select two.

Domain: Implement Azure security

- A. Use `SecretClient` (`Azure.Security.KeyVault.Secrets`) for connection strings/tokens, `KeyClient` / `CryptographyClient` (`Azure.Security.KeyVault.Keys`) for RSA/EC wrap-unwrap-sign, and `CertificateClient` for X.509 lifecycle
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Enable Soft Delete (mandatory on new vaults, 7–90 days) plus Purge Protection on Azure Key Vault so neither accidental deletion nor malicious principals can permanently destroy keys before retention expires

### 55. Pre-release movie masters are encrypted locally with a random 256-bit AES content key (`dekBytes`) whose bytes must be wrapped using an HSM-protected RSA key in Azure Key Vault (` ____ `). Which SDK client and method perform this?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Instantiate `new CryptographyClient(keyVaultKey.Id, new DefaultAzureCredential())` and invoke `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync(...)`

### 56. Sixty ephemeral ACI video-transcoding groups spin up for big sporting events and tear down afterward, and all sixty must share one pre-authorized Entra identity granted `Storage Blob Data Contributor` without re-creating RBAC assignments per job. Which identity model fits?

Domain: Implement Azure security

- A. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- B. Choose a User-Assigned Managed Identity when multiple compute resources must share one pre-provisioned identity lifecycle independent of individual app deletions; choose System-Assigned when 1-to-1 fate-sharing tied to a single resource is required
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 57. A streaming API Container App attaches both `uami-acr` and `uami-drm-kv`, causing bare `new DefaultAzureCredential()` calls in C# to fail disambiguation (` ____ `). How must the code select `uami-drm-kv`?

Domain: Implement Azure security

- A. Instantiate `new DefaultAzureCredential(new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId })` (or set `AZURE_CLIENT_ID`)
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 58. During a live championship stream, 2% of `POST /tickets/claim` calls return HTTP 500, and SREs need end-to-end W3C trace correlation plus a KQL inner join isolating which downstream dependency failed on each 500 request. Which two practices solve this? Select two.

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Run `AppRequests | where ResultCode == "500" | join kind=inner (AppDependencies | where Success == false) on OperationId | project TimeGenerated, Name, Target, DependencyType, ResultCode1`
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- E. Query Workspace-based Application Insights (`AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces` or classic `requests`/`dependencies`/`exceptions`) joining on `OperationId` (`operation_Id`) to reconstruct end-to-end distributed transactions

### 59. A broadcast NOC screen needs 5-minute buckets over the last hour showing failed request counts and p95 latency per API operation in Workspace-based Application Insights (` ____ `). Which KQL query produces these metrics?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Run `AppRequests | where TimeGenerated > ago(1h) | summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)`

### 60. Short-lived leaderboard-reset Container Apps Jobs run for 6 seconds and exit `Main()` immediately, dropping buffered telemetry items before export completes. Which shutdown step guarantees delivery?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 61. Inside a .NET 8 matchmaking service instrumented with `UseAzureMonitor()`, developers want custom timed spans around `ComputeSkillRating` (`using var span = ____ `) visible in Application Insights Transaction Search. How should they code this?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 62. Ahead of global concert on-sales, Lyric Arena wants outside-in synthetic monitors validating SSL cert renewal dates and HTTP 200 responses on its public ticketing domain without waking engineers for single-location internet blips. How should monitoring be set up?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group

### 63. A substation SCADA API runs inside an isolated private VNet unreachable from public Azure Monitor POPs, yet NovaGrid requires availability percentages tracked inside Application Insights Availability. How should synthetic probes be implemented?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 64. EmberPlay Studios is onboarding a brand-new .NET 8 clan-chat API onto Workspace-based Application Insights using OpenTelemetry and automated failure alerts. Which ordered rollout sequence follows official guidance?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Create a deprecated Classic InstrumentationKey-only resource → hardcode ikey without SDK → fire Action Group → provision Log Analytics later
- B. Set Adaptive Sampling to 0% maxTelemetryItemsPerSecond → deploy without connection string → query traces → attach Action Group
- C. Create a KQL alert rule on an empty subscription → uninstall OpenTelemetry packages → copy connection string → provision Application Insights
- D. Provision Workspace-based Application Insights and copy APPLICATIONINSIGHTS_CONNECTION_STRING → configure UseAzureMonitor() OpenTelemetry distro at startup → verify requests/dependencies in Logs → create a KQL or metric alert linked to an Action Group

### 65. Live-streaming engineers upgrading six .NET 8 playback services to OpenTelemetry want Microsoft's supported distro wired via connection string alongside server/workspace sampling that keeps cross-service trace graphs intact without affecting Live Metrics. Which two options should they use? Select two.

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments
- B. Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- E. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 66. Proposed solution: Configure a new .NET 8 media catalog microservice using a legacy Classic `InstrumentationKey` string without `APPLICATIONINSIGHTS_CONNECTION_STRING` or OpenTelemetry. Why is this rejected in code review, and what replaces it?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 67. Lyric Arena's APIM gateway calls an internal Entra-protected seat-inventory API and must acquire and attach bearer tokens automatically via APIM's Managed Identity (`<inbound> ____ </inbound>`). Which XML policy snippet completes `<inbound>`?

Domain: Connect to and consume Azure services and third-party services

- A. Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`
- B. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 68. A streaming metadata squad tests a non-breaking OpenAPI field addition on `;rev=2` before making it current, while running breaking `/v1/playlists` and `/v2/playlists` endpoints in parallel for smart-TV firmware cohorts. How do APIM `Revisions` and `Versions` apply?

Domain: Connect to and consume Azure services and third-party services

- A. Use APIM `Revisions` to stage, test, and swap non-breaking internal changes safely on the same consumer URL (`;rev=2`), and use APIM `Versions` (path/header/query) when publishing breaking contract changes side-by-side for distinct consumer cohorts
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 69. Console UI developers need mocked HTTP 200 `/leaderboards/season9` JSON from APIM two weeks before the backend ships, and once live, `/leaderboards/{id}` must rewrite to `/internal/v2/orders/{orderId}` (` ____ `). Which APIM policies handle both stages?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use `<mock-response status-code="200" content-type="application/json" />` during frontend parallel development, or `<rewrite-uri template="/internal/v2/orders/{orderId}" />` with `<set-backend-service base-url="..." />` in `<inbound>`
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 70. An HTTP-triggered Function App imported into APIM rejects direct anonymous requests and expects APIM to supply a function/host key in `x-functions-key` (`[HttpTrigger( ____ )]`). Which `AuthorizationLevel` is configured?

Domain: Connect to and consume Azure services and third-party services

- A. Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 71. Broadcast wire partners calling Prism's APIM gateway must supply a Product Subscription Key, pass X.509 client-certificate thumbprint checks, and carry a valid Microsoft Entra bearer token before hitting backend Functions. How should APIM secure inbound calls?

Domain: Connect to and consume Azure services and third-party services

- A. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers

### 72. High-security energy-trading endpoints on NovaGrid's gateway need three-factor caller verification (product key, mTLS certificate thumbprint, and Entra JWT) on the front door plus secretless Managed Identity token injection toward internal backends. Which two APIM configurations cover both hops? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- B. Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers
- C. Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 73. An APIM ticket-transfer endpoint must return HTTP `401` immediately whenever a caller's bearer JWT lacks audience `api://orders` or the required write role (`<inbound> ____ </inbound>`). Which XML policy enforces this?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`

### 74. EmberPlay's public tournament-schedule gateway on APIM must cap per-partner burst spikes and monthly call allowances without losing inherited rules, serve cached localized schedules per language header, and retry backend 5xx blips while deleting framework fingerprint headers. Which three APIM policy setups implement this? Select three.

Domain: Connect to and consume Azure services and third-party services

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- E. Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`
- F. Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`

### 75. Free-tier sports-widget developers on APIM must be throttled at 60 calls/minute (HTTP `429`) and capped at 5,000 calls/month (HTTP `403`) per subscription while keeping API-scope `<validate-jwt>` inheritance intact. How must `<inbound>` be authored?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`

### 76. Concert setlists on `GET /events/featured` are localized via `Accept-Language`, and adding `<cache-lookup>` without `vary-by-header` serves cached Japanese JSON to English browsers (` ____ `). Which policy pair caches localized responses properly?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 77. Security audits flag `X-AspNet-Version` on responses from Lyric Arena's APIM gateway, and single-pod HTTP 503 restarts surface directly to fan mobile apps. Which APIM policy sections handle 5xx retries and header deletion?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 78. NovaGrid is registering a municipal utility's custom outage-management HTTPS endpoint on an Azure Event Grid topic. Which ordered steps complete the mandatory webhook validation handshake?

Domain: Connect to and consume Azure services and third-party services

- A. Deploy the HTTPS webhook endpoint accepting POST requests → create the Event Grid subscription pointing to the endpoint → inspect incoming SubscriptionValidationEvent and read validationCode → return HTTP 200 JSON containing validationResponse (or invoke validationUrl)
- B. Return HTTP 200 validationResponse before reading the request → create the topic → deploy the endpoint → create the subscription
- C. Create the Event Grid subscription → deploy the HTTPS endpoint later → return HTTP 202 empty body → parse SubscriptionValidationEvent
- D. Deploy an HTTP-only port 80 endpoint → return validationCode as a response header → create the Event Grid subscription → enable TLS

### 79. A media-asset pipeline publishes `VideoTranscoded` events in `CloudEvents v1.0` schema filtered by `/channel/uhd/` with 24-hour Blob dead-lettering, and onboards a custom partner HTTPS webhook (` ____ `). Which two Event Grid implementations apply? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`
- C. Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors

### 80. An external ticketing-resale HTTPS webhook written in ASP.NET Core fails Event Grid subscription creation until validation logic is added (` ____ `). What response must the webhook return during subscription setup?

Domain: Connect to and consume Azure services and third-party services

- A. Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`
- B. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 81. Smart meters across 2 million homes stream 110,000 kWh readings/sec into Azure Event Hubs, and a .NET 8 grid-balancing worker must consume partitions with Blob Storage checkpoints. Which sequence implements the consumer?

Domain: Connect to and consume Azure services and third-party services

- A. Point all five independent microservices at `$Default` with one shared Blob prefix → call StopProcessingAsync → call StartProcessingAsync → skip UpdateCheckpointAsync
- B. Call StartProcessingAsync → register ProcessEventAsync without ProcessErrorAsync → create the Event Hub → create the Blob container
- C. Create the Event Hub, consumer group, and Blob checkpoint container → instantiate BlobContainerClient and EventProcessorClient → register ProcessEventAsync (calling UpdateCheckpointAsync) and ProcessErrorAsync → call StartProcessingAsync before StopProcessingAsync
- D. Instantiate EventHubProducerClient → call UpdateCheckpointAsync on the producer → register ProcessEventAsync → call StopProcessingAsync first

### 82. Proposed solution: Route 95,000 live game-telemetry packets per second through Azure Event Grid webhooks so anti-cheat, matchmaking, and replay analytics can each maintain independent offset cursors and archive Parquet batches to ADLS Gen2. Why does this fail, and what replaces it?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2

### 83. Whenever EmberPlay's `EventProcessorClient` telemetry pods autoscale, rebalanced partitions replay two hours of already-processed match events (`await eventArgs. ____ `). Which call must follow idempotent persistence?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Host `EventProcessorClient` backed by `BlobContainerClient` and call `await eventArgs.UpdateCheckpointAsync()` after idempotent batch persistence so partition leases resume cleanly after rebalancing
- C. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 84. Box-office order events on Azure Service Bus must fan out by `VenueCountry = 'DE'` via fast header matching, discard duplicate `MessageId` retries from stadium turnstiles, and isolate poison payloads in `$DeadLetterQueue`. Which two Service Bus designs apply? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Use Azure Service Bus Topics with `SqlRuleFilter` / `CorrelationRuleFilter` (`CorrelationRuleFilter` preferred for high throughput) and `SqlRuleAction` header stamping, inspecting `$DeadLetterQueue` (`SubQueue.DeadLetter`) after `MaxDeliveryCount` expires
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- E. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors

### 85. Turnstile scanners at Lyric Arena occasionally resend identical `MessageId` admission scans when Wi-Fi stutters and require strict per-gate FIFO processing order on Service Bus. Which two queue properties enforce both guarantees?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 86. When a fan starts a 30-minute VIP upgrade hold, the API enqueues a delayed release command on Service Bus (`long seq = await sender. ____ `) and cancels it if payment succeeds early. Which SDK method pair implements this?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `long seq = await sender.ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` and persist `seq` to call `CancelScheduledMessageAsync(seq)` if the user cancels early
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 87. A media studio queues 320 TB of 8 KB video-waveform thumbnail pointers requiring simple visibility leases and low storage cost without FIFO sessions or pub/sub topics. Which Azure queue service supports a 320 TB backlog?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics

### 88. Proposed solution: Call `QueueClient.PeekMessagesAsync()` across 12 transcoding workers to lease waveform jobs invisibly and pass peeked items to `DeleteMessageAsync()`. Why does every delete fail, and what fixes it?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

---

## Case study — EmberPlay Studios

EmberPlay Studios runs seasonal multiplayer leaderboards on Azure App Service with `Staging` and `Production` slots, routing 10% of live player traffic to `Staging` for canary validation before swapping. Player replay archives in Blob Storage move from Hot to Cold after 14 days and Archive after 90 days, with priority rehydration required when dispute moderators request archived replays.

The next 3 questions refer to **EmberPlay Studios**. Read the scenario brief once, then answer each item independently.

### 89. EmberPlay validates seasonal leaderboard builds on App Service `Staging` (with 10% canary routing) before swapping into `Production`, keeping live matchmaking keys pinned strictly to `Production`. Which sequence promotes releases cleanly?

Domain: Develop Azure compute solutions

- A. Create the staging slot on a Free F1 plan → deploy the build → swap slots → mark settings sticky
- B. Create the staging deployment slot on the Standard/Premium Web App → mark production-only connection strings and webhook settings as deployment slot settings → deploy and warm up the new build in staging → swap staging into production and verify health
- C. Deploy directly to production → create the staging slot → swap staging into production → mark settings as slot settings
- D. Swap staging into production → create the staging slot → deploy the build → mark settings as deployment slot settings

### 90. Match replay blobs under `replays/` must transition automatically from `Hot` to `Cold` after 14 days and to `Archive` after 90 days without custom cleanup workers. What should EmberPlay configure?

Domain: Develop for Azure storage

- A. Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`)
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 91. Esports tournament moderators request a 6-month-old match replay currently stored in the offline `Archive` tier in Blob Storage. Which ordered steps restore and download the replay cleanly?

Domain: Develop for Azure storage

- A. Acquire an infinite blob lease → delete the blob snapshot → download the archived blob directly → call SetAccessTier
- B. Download the archived blob stream directly → call SetAccessTier to Hot → poll ArchiveStatus → verify the Archive tier
- C. Verify the blob is currently in the Archive access tier → call SetAccessTier (or CopyBlob) targeting Hot or Cool with Standard or High rehydrate priority → poll ArchiveStatus until rehydration completes and tier updates → download the blob content
- D. Set blob metadata `tier=Hot` → download the blob immediately → call SetAccessTier to Archive → poll ArchiveStatus

---

## Case study — Lyric Arena Ticketing

Lyric Arena Ticketing handles stadium on-sale events on Azure Container Apps with HTTP scale rules and Cosmos DB for seat-hold documents that must expire and vanish automatically after 600 seconds if unpaid, without running background delete sweeps. Optimistic concurrency via ETags prevents two fans from claiming the same seat document simultaneously.

The next 3 questions refer to **Lyric Arena Ticketing**. Read the scenario brief once, then answer each item independently.

### 92. Ahead of a stadium tour on-sale, Lyric wants to route 5% of live HTTP seat-map requests on Azure Container Apps to a new revision while 95% remain on the current revision. How must the Container App be configured?

Domain: Develop Azure compute solutions

- A. Set `--revision-mode multiple` and apply `az containerapp ingress traffic set --revision-weight` to split live HTTP requests across named revisions
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 93. Unpaid seat-hold documents in Cosmos DB specify `"ttl": 600` and must vanish automatically after 600 seconds without expiring permanent arena-map documents in the same container or running delete sweeps. How should the container be configured?

Domain: Develop for Azure storage

- A. Enable container `DefaultTimeToLive = -1` (or positive seconds) and set item `ttl = 600` so Cosmos DB purges expired items automatically using background RU capacity
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 94. Two fans attempt to claim seat `Sec104-RowB-12` in Cosmos DB within the same millisecond (`await container.ReplaceItemAsync(..., ____ )`). How must the C# API ensure one fan wins and the second immediately receives HTTP `412`?

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Pass `new ItemRequestOptions { IfMatchEtag = item.ETag }` on `ReplaceItemAsync` and catch `CosmosException` when `StatusCode == HttpStatusCode.PreconditionFailed` (412)
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

---

## Case study — NovaGrid Energy

NovaGrid Energy collects substation voltage alerts through Azure Event Grid domains serving 80 municipal utilities under tenant-scoped event topics. Critical transformer alerts forward to an Azure Service Bus queue consumed by an Azure Function, while Application Insights custom metrics and KQL log alerts watch for webhook delivery latency above 1,500 ms.

The next 3 questions refer to **NovaGrid Energy**. Read the scenario brief once, then answer each item independently.

### 95. NovaGrid routes substation voltage alerts to 80 municipal utilities under tenant-scoped event topics behind one publish endpoint with per-utility Azure RBAC isolation. Which Event Grid resource fits?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization

### 96. Critical transformer-overload alerts land on an Azure Service Bus queue consumed by a C# Function/worker that must never lose messages if a worker crashes mid-analysis and must dead-letter malformed payloads (` ____ `). Which receive pattern applies?

Domain: Connect to and consume Azure services and third-party services

- A. Use `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false`, calling `CompleteMessageAsync` after commit, `AbandonMessageAsync` for transient retries, and `DeadLetterMessageAsync` on unrecoverable schema errors
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 97. NovaGrid monitors custom webhook delivery latency in Application Insights / Azure Monitor and must page grid dispatchers via webhook/SMS whenever p95 latency exceeds 1,500 ms. Which alerting construct implements this?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Create an Azure Monitor Metric Alert (Dynamic Thresholds or static p95 latency/5xx count) or Scheduled Query (KQL) Alert targeting an Action Group configured with webhook / Azure Function / email-SMS receivers

---

## Case study — Prism Newsroom

Prism Newsroom ingests breaking wire feeds into Azure Functions, enriches metadata via Azure App Configuration feature flags and Key Vault-backed secrets, and publishes partner feeds through Azure API Management. A self-hosted APIM gateway deployed in Prism on-premises broadcast centers keeps local newsroom API traffic inside the facility while syncing configuration from Azure every ten seconds.

The next 3 questions refer to **Prism Newsroom**. Read the scenario brief once, then answer each item independently.

### 98. Prism's breaking-news Functions and APIs load feature flags and Key Vault secret references from Azure App Configuration with dynamic sentinel-key refresh. Which ordered steps configure this end to end?

Domain: Implement Azure security

- A. Add Key Vault references → wire ConfigureRefresh without UseAzureAppConfiguration middleware → expect background timer push updates → grant RBAC later
- B. Copy plaintext Key Vault secret values into appsettings.json → commit to Git → wire ConfigureRefresh → enable Managed Identity
- C. Grant only App Configuration Data Reader (no Key Vault role) → invoke UseAzureAppConfiguration → add sentinel key → register AddAzureAppConfiguration
- D. Enable Managed Identity with App Configuration Data Reader + Key Vault Secrets User → add Key Vault references and a sentinel key → wire AddAzureAppConfiguration with ConfigureKeyVault and ConfigureRefresh → invoke UseAzureAppConfiguration middleware

### 99. Prism's on-premises broadcast centers must route local newsroom API calls inside the studio LAN even if external links degrade, while syncing API policies from Azure every ten seconds. Which APIM deployment model works?

Domain: Connect to and consume Azure services and third-party services

- A. Select `Developer` (non-SLA) or `Premium` / `Standard v2` for VNet integration, and deploy the containerized APIM Self-Hosted Gateway (`mcr.microsoft.com/azure-api-management/gateway`) for hybrid on-premises/multi-cloud local traffic routing
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 100. Prism's Azure Function App reads wire-agency credentials from app settings and wants rotated Azure Key Vault secrets resolved automatically without writing `SecretClient` SDK code (` ____ `). Which configuration achieves this?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Configure App Service / Functions application settings using `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` (omitting secret version) paired with `Key Vault Secrets User` on the app Managed Identity

---

## Answer key and explanations

### Question 1 — A, B

Answers: Use a multi-stage Dockerfile building in `mcr.microsoft.com/dotnet/sdk:8.0` and copying published output into `mcr.microsoft.com/dotnet/aspnet:8.0` with a non-root `USER app`; Declare `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form so `SIGTERM` reaches the .NET host cleanly during container shutdown. A multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root Dockerfile strips compiler layers, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to PID 1. Local study-map skill 1.1 (Create and Manage Container Images and Multi-Stage Dockerfiles), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Exec-form `ENTRYPOINT` runs the process as PID 1 without an intermediate `/bin/sh -c` wrapper that swallows POSIX termination signals. In this scenario: A multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root Dockerfile strips compiler layers, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to PID 1.
- **B:** Correct. Multi-stage Docker builds exclude compiler SDK layers and source files from the final runtime image, shrinking image size and attack surface. In this scenario: A multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root Dockerfile strips compiler layers, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to PID 1.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: A multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root Dockerfile strips compiler layers, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to PID 1.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: A multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root Dockerfile strips compiler layers, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to PID 1.
- **E:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: A multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root Dockerfile strips compiler layers, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to PID 1.

### Question 2 — C

Answer: Add `bin/`, `obj/`, `.git/`, and local `.env` files to `.dockerignore` before running `docker build` or `az acr build`. Listing `bin/`, `obj/`, asset caches, and `.env` inside `.dockerignore` prevents streaming unneeded local directories and secrets into the build context. `.dockerignore` prevents streaming gigabytes of local build artifacts and stray secrets into the build context. Local study-map skill 1.1 (Create and Manage Container Images and Multi-Stage Dockerfiles), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Listing `bin/`, `obj/`, asset caches, and `.env` inside `.dockerignore` prevents streaming unneeded local directories and secrets into the build context.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Listing `bin/`, `obj/`, asset caches, and `.env` inside `.dockerignore` prevents streaming unneeded local directories and secrets into the build context.
- **C:** Correct. `.dockerignore` prevents streaming gigabytes of local build artifacts and stray secrets into the build context. In this scenario: Listing `bin/`, `obj/`, asset caches, and `.env` inside `.dockerignore` prevents streaming unneeded local directories and secrets into the build context.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Listing `bin/`, `obj/`, asset caches, and `.env` inside `.dockerignore` prevents streaming unneeded local directories and secrets into the build context.

### Question 3 — A

Answer: Upgrade Azure Container Registry to the `Premium` SKU and configure geo-replication into each target compute region. Upgrading Azure Container Registry to `Premium` and configuring geo-replication across Tokyo, Frankfurt, and Virginia serves local regional pulls under one FQDN. ACR geo-replication requires the `Premium` tier and serves local regional layer pulls through a single registry login server FQDN. Local study-map skill 1.2 (Publish Images, Run ACR Tasks, and Manage Auth/Purge in Azure Container Registry), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. ACR geo-replication requires the `Premium` tier and serves local regional layer pulls through a single registry login server FQDN. In this scenario: Upgrading Azure Container Registry to `Premium` and configuring geo-replication across Tokyo, Frankfurt, and Virginia serves local regional pulls under one FQDN.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Upgrading Azure Container Registry to `Premium` and configuring geo-replication across Tokyo, Frankfurt, and Virginia serves local regional pulls under one FQDN.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Upgrading Azure Container Registry to `Premium` and configuring geo-replication across Tokyo, Frankfurt, and Virginia serves local regional pulls under one FQDN.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Upgrading Azure Container Registry to `Premium` and configuring geo-replication across Tokyo, Frankfurt, and Virginia serves local regional pulls under one FQDN.

### Question 4 — B

Answer: Execute `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine`. `az acr import --name <acrName> --source ... --image ...` copies upstream container manifests server-side directly into ACR without a local Docker daemon. `az acr import` copies public or cross-registry container images server-side into ACR without requiring `docker pull` / `docker push` on a local workstation. Local study-map skill 1.2 (Publish Images, Run ACR Tasks, and Manage Auth/Purge in Azure Container Registry), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az acr import --name <acrName> --source ... --image ...` copies upstream container manifests server-side directly into ACR without a local Docker daemon.
- **B:** Correct. `az acr import` copies public or cross-registry container images server-side into ACR without requiring `docker pull` / `docker push` on a local workstation. In this scenario: `az acr import --name <acrName> --source ... --image ...` copies upstream container manifests server-side directly into ACR without a local Docker daemon.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `az acr import --name <acrName> --source ... --image ...` copies upstream container manifests server-side directly into ACR without a local Docker daemon.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `az acr import --name <acrName> --source ... --image ...` copies upstream container manifests server-side directly into ACR without a local Docker daemon.

### Question 5 — C

Answer: Set `--restart-policy OnFailure` (or `Never`) on the Azure Container Instances container group so batch containers stop billing vCPU/memory seconds once exit code 0 completes. Setting `--restart-policy OnFailure` stops container execution and billing once exit code `0` completes while retrying non-zero crash exits automatically. ACI bills per second while containers run; `OnFailure` retries crashes (`exit != 0`) and halts cleanly on `exit == 0`, whereas `Always` loops forever. Local study-map skill 1.3 (Run Container Groups, Sidecars, Volumes, and Restart Policies in Azure Container Instances), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `--restart-policy OnFailure` stops container execution and billing once exit code `0` completes while retrying non-zero crash exits automatically.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting `--restart-policy OnFailure` stops container execution and billing once exit code `0` completes while retrying non-zero crash exits automatically.
- **C:** Correct. ACI bills per second while containers run; `OnFailure` retries crashes (`exit != 0`) and halts cleanly on `exit == 0`, whereas `Always` loops forever. In this scenario: Setting `--restart-policy OnFailure` stops container execution and billing once exit code `0` completes while retrying non-zero crash exits automatically.
- **D:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Setting `--restart-policy OnFailure` stops container execution and billing once exit code `0` completes while retrying non-zero crash exits automatically.

### Question 6 — A

Answer: Deploy the application container and Envoy/logging sidecar inside one multi-container ACI group sharing `localhost` network namespace and an `emptyDir` / Azure Files volume. Deploying packager and sidecar inside one multi-container ACI group shares the `localhost` network namespace and mounts a shared `emptyDir` volume. Containers in the same ACI container group share one IP/port namespace (`127.0.0.1`) and can mount shared Azure Files or `emptyDir` volumes on Linux. Local study-map skill 1.3 (Run Container Groups, Sidecars, Volumes, and Restart Policies in Azure Container Instances), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Containers in the same ACI container group share one IP/port namespace (`127.0.0.1`) and can mount shared Azure Files or `emptyDir` volumes on Linux. In this scenario: Deploying packager and sidecar inside one multi-container ACI group shares the `localhost` network namespace and mounts a shared `emptyDir` volume.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Deploying packager and sidecar inside one multi-container ACI group shares the `localhost` network namespace and mounts a shared `emptyDir` volume.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Deploying packager and sidecar inside one multi-container ACI group shares the `localhost` network namespace and mounts a shared `emptyDir` volume.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Deploying packager and sidecar inside one multi-container ACI group shares the `localhost` network namespace and mounts a shared `emptyDir` volume.

### Question 7 — A

Answer: Execute `az containerapp env create --name <envName> --resource-group <rg> --infrastructure-subnet-resource-id <subnetId> --internal-only`. `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` creates a VNet-injected internal-only Container Apps environment. Provisioning a VNet-injected `--internal-only` Container Apps environment isolates the Envoy ingress load balancer to private RFC1918 addresses. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Provisioning a VNet-injected `--internal-only` Container Apps environment isolates the Envoy ingress load balancer to private RFC1918 addresses. In this scenario: `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` creates a VNet-injected internal-only Container Apps environment.
- **B:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` creates a VNet-injected internal-only Container Apps environment.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` creates a VNet-injected internal-only Container Apps environment.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` creates a VNet-injected internal-only Container Apps environment.

### Question 8 — D, E, F

Answers: Configure a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0` and Managed Identity (`identity` property) so replicas scale to zero when idle and wake on queue depth; Register a Dapr state or pub/sub component in the Container Apps environment and restrict access via the component `scopes` array to specific `daprAppId` values; Define a Container App secret using `keyVaultUrl` plus `identity` (managed identity resource ID or `system`) and map container environment variables via `secretRef`. KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, Dapr `scopes` confine component access by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, Dapr `scopes` confine component access by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, Dapr `scopes` confine component access by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely.
- **C:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, Dapr `scopes` confine component access by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely.
- **D:** Correct. Key Vault secret references in Container Apps resolve secrets via Managed Identity without storing secret strings in ARM templates. In this scenario: KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, Dapr `scopes` confine component access by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely.
- **E:** Correct. Dapr `scopes` confine which microservices inside a shared Container Apps environment can load or invoke a component. In this scenario: KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, Dapr `scopes` confine component access by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely.
- **F:** Correct. Container Apps uses KEDA scalers to scale down to zero on consumption/workload profiles and authenticate scalers cleanly via Managed Identity. In this scenario: KEDA `azure-servicebus` rules with `minReplicas: 0` + `identity` scale to zero, Dapr `scopes` confine component access by `daprAppId`, and `keyVaultUrl` + `identity` secret refs resolve Key Vault secrets safely.

### Question 9 — A

Answer: Deploy an Azure Container Apps Job (`triggerType: Event` or `Schedule`) with `replicaCompletionCount` and `parallelism` instead of an always-listening HTTP container app. Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` executes bounded batch work without idle HTTP listeners. Container Apps Jobs execute finite scheduled or event-driven workloads to completion without exposing unused HTTP ingress. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Container Apps Jobs execute finite scheduled or event-driven workloads to completion without exposing unused HTTP ingress. In this scenario: Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` executes bounded batch work without idle HTTP listeners.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` executes bounded batch work without idle HTTP listeners.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` executes bounded batch work without idle HTTP listeners.
- **D:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Deploying an Azure Container Apps Job (`triggerType: Schedule` or `Event`) with `parallelism` and `replicaCompletionCount` executes bounded batch work without idle HTTP listeners.

### Question 10 — A

Answer: Provision at least a `Standard` (`S1+`) or `Premium v3` (`P1v3+`) App Service plan to unlock deployment slots, custom domain SNI SSL, and metric/schedule autoscaling. `Basic` App Service plans lack both deployment slots and rule-based autoscale; upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks slots and autoscale rules. `Free`, `Shared`, and `Basic` plans omit deployment slots (`S1` gives 5, `P1v3` gives 20) and rule-based autoscale (`S1+` required). Local study-map skill 1.5 (Create Azure App Service Plans and Web Apps Across Linux and Windows Runtimes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. `Free`, `Shared`, and `Basic` plans omit deployment slots (`S1` gives 5, `P1v3` gives 20) and rule-based autoscale (`S1+` required). In this scenario: `Basic` App Service plans lack both deployment slots and rule-based autoscale; upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks slots and autoscale rules.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `Basic` App Service plans lack both deployment slots and rule-based autoscale; upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks slots and autoscale rules.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `Basic` App Service plans lack both deployment slots and rule-based autoscale; upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks slots and autoscale rules.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `Basic` App Service plans lack both deployment slots and rule-based autoscale; upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks slots and autoscale rules.

### Question 11 — B

Answer: Set `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` inside the final `.NET 8` runtime stage and match `targetPort: 8080` on Container Apps ingress. Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` aligns non-root Kestrel listeners with `targetPort: 8080` / `WEBSITES_PORT=8080`. Starting in .NET 8, official Microsoft container images default to non-root port `8080` rather than privileged port `80`. Local study-map skill 1.5 (Create Azure App Service Plans and Web Apps Across Linux and Windows Runtimes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` aligns non-root Kestrel listeners with `targetPort: 8080` / `WEBSITES_PORT=8080`.
- **B:** Correct. Starting in .NET 8, official Microsoft container images default to non-root port `8080` rather than privileged port `80`. In this scenario: Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` aligns non-root Kestrel listeners with `targetPort: 8080` / `WEBSITES_PORT=8080`.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` aligns non-root Kestrel listeners with `targetPort: 8080` / `WEBSITES_PORT=8080`.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` aligns non-root Kestrel listeners with `targetPort: 8080` / `WEBSITES_PORT=8080`.

### Question 12 — C

Answer: Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances. Enabling Application Logging (Blob) and Web Server Logging pointed at an Azure Blob Storage container persists logs across all scaled workers per retention policy. Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy. Local study-map skill 1.6 (Configure App Service Diagnostics, Application/Web Server Logging, and Log Streaming), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Enabling Application Logging (Blob) and Web Server Logging pointed at an Azure Blob Storage container persists logs across all scaled workers per retention policy.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling Application Logging (Blob) and Web Server Logging pointed at an Azure Blob Storage container persists logs across all scaled workers per retention policy.
- **C:** Correct. Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy. In this scenario: Enabling Application Logging (Blob) and Web Server Logging pointed at an Azure Blob Storage container persists logs across all scaled workers per retention policy.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Enabling Application Logging (Blob) and Web Server Logging pointed at an Azure Blob Storage container persists logs across all scaled workers per retention policy.

### Question 13 — B

Answer: Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`. Enabling filesystem logging via `az webapp log config` and running `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu console logs. `az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting. Local study-map skill 1.6 (Configure App Service Diagnostics, Application/Web Server Logging, and Log Streaming), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Enabling filesystem logging via `az webapp log config` and running `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu console logs.
- **B:** Correct. `az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting. In this scenario: Enabling filesystem logging via `az webapp log config` and running `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu console logs.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Enabling filesystem logging via `az webapp log config` and running `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu console logs.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling filesystem logging via `az webapp log config` and running `az webapp log tail --name <app> --resource-group <rg>` streams live Kudu console logs.

### Question 14 — B

Answer: Set `WEBSITE_RUN_FROM_PACKAGE=1` and deploy with `az webapp deploy --type zip` so the app mounts the read-only ZIP package directly with atomic cold-start replacement. Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying via `az webapp deploy --type zip` mounts the ZIP archive directly and flips versions atomically without file-lock collisions. Running directly from a mounted ZIP eliminates file-lock copy conflicts during `wwwroot` sync and speeds cold starts. Local study-map skill 1.7 (Deploy Code, Run-From-Package ZIPs, and Custom Containers to App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying via `az webapp deploy --type zip` mounts the ZIP archive directly and flips versions atomically without file-lock collisions.
- **B:** Correct. Running directly from a mounted ZIP eliminates file-lock copy conflicts during `wwwroot` sync and speeds cold starts. In this scenario: Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying via `az webapp deploy --type zip` mounts the ZIP archive directly and flips versions atomically without file-lock collisions.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying via `az webapp deploy --type zip` mounts the ZIP archive directly and flips versions atomically without file-lock collisions.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` and deploying via `az webapp deploy --type zip` mounts the ZIP archive directly and flips versions atomically without file-lock collisions.

### Question 15 — C

Answer: Disable the ACR admin account and assign the built-in `AcrPull` role on the registry to the compute resource managed identity. Granting `AcrPull` on ACR to the Web App's Managed Identity and enabling Managed Identity registry authentication (`acrUseManagedIdentityCreds: true`) eliminates static registry passwords. `AcrPull` with Managed Identity eliminates shared registry passwords while granting least-privilege read-only image pulls. Local study-map skill 1.7 (Deploy Code, Run-From-Package ZIPs, and Custom Containers to App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Granting `AcrPull` on ACR to the Web App's Managed Identity and enabling Managed Identity registry authentication (`acrUseManagedIdentityCreds: true`) eliminates static registry passwords.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Granting `AcrPull` on ACR to the Web App's Managed Identity and enabling Managed Identity registry authentication (`acrUseManagedIdentityCreds: true`) eliminates static registry passwords.
- **C:** Correct. `AcrPull` with Managed Identity eliminates shared registry passwords while granting least-privilege read-only image pulls. In this scenario: Granting `AcrPull` on ACR to the Web App's Managed Identity and enabling Managed Identity registry authentication (`acrUseManagedIdentityCreds: true`) eliminates static registry passwords.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Granting `AcrPull` on ACR to the Web App's Managed Identity and enabling Managed Identity registry authentication (`acrUseManagedIdentityCreds: true`) eliminates static registry passwords.

### Question 16 — D, E

Answers: Enable `httpsOnly: true`, set `minTlsVersion: "1.2"` (or `"1.3"`), and configure `clientCertEnabled` when mutual TLS client certificates are required; Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`. Enabling `httpsOnly: true`, `minTlsVersion: "1.2"`, and `clientCertEnabled` enforces mTLS transport security, while `az webapp config connection-string set --slot-settings` pins `LedgerDb` per slot. Local study-map skill 1.8 (Configure TLS, Mutual TLS, CORS, App Settings, and Service Connections on App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Enabling `httpsOnly: true`, `minTlsVersion: "1.2"`, and `clientCertEnabled` enforces mTLS transport security, while `az webapp config connection-string set --slot-settings` pins `LedgerDb` per slot.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Enabling `httpsOnly: true`, `minTlsVersion: "1.2"`, and `clientCertEnabled` enforces mTLS transport security, while `az webapp config connection-string set --slot-settings` pins `LedgerDb` per slot.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling `httpsOnly: true`, `minTlsVersion: "1.2"`, and `clientCertEnabled` enforces mTLS transport security, while `az webapp config connection-string set --slot-settings` pins `LedgerDb` per slot.
- **D:** Correct. Enforcing HTTPS redirection and minimum TLS 1.2/1.3 at the App Service front end rejects plaintext HTTP and legacy ciphers before app code runs. In this scenario: Enabling `httpsOnly: true`, `minTlsVersion: "1.2"`, and `clientCertEnabled` enforces mTLS transport security, while `az webapp config connection-string set --slot-settings` pins `LedgerDb` per slot.
- **E:** Correct. `--slot-settings` pins the connection string (`SQLCONNSTR_LedgerDb`) to the target slot so slot swaps never leak staging databases into production. In this scenario: Enabling `httpsOnly: true`, `minTlsVersion: "1.2"`, and `clientCertEnabled` enforces mTLS transport security, while `az webapp config connection-string set --slot-settings` pins `LedgerDb` per slot.

### Question 17 — C

Answer: Configure App Service `CORS` with explicit origin URLs (and `supportCredentials` only without wildcard `*`) so App Service handles preflight `OPTIONS` requests. Registering explicit origin `https://watch.emberplay.example` (never `*`) when `supportCredentials` is enabled satisfies browser CORS preflight checks. Platform-level App Service CORS intercepts `OPTIONS` preflight checks; credentialed CORS forbids wildcard `*` origins. Local study-map skill 1.8 (Configure TLS, Mutual TLS, CORS, App Settings, and Service Connections on App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Registering explicit origin `https://watch.emberplay.example` (never `*`) when `supportCredentials` is enabled satisfies browser CORS preflight checks.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Registering explicit origin `https://watch.emberplay.example` (never `*`) when `supportCredentials` is enabled satisfies browser CORS preflight checks.
- **C:** Correct. Platform-level App Service CORS intercepts `OPTIONS` preflight checks; credentialed CORS forbids wildcard `*` origins. In this scenario: Registering explicit origin `https://watch.emberplay.example` (never `*`) when `supportCredentials` is enabled satisfies browser CORS preflight checks.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Registering explicit origin `https://watch.emberplay.example` (never `*`) when `supportCredentials` is enabled satisfies browser CORS preflight checks.

### Question 18 — A

Answer: Pair every scale-out metric rule (e.g., CPU > 75% for 10 min) with a conservative scale-in rule (e.g., CPU < 35%) and an explicit `coolDown` window plus safe default/max instance bounds. Widening the hysteresis band (e.g., >75% scale-out, <35% scale-in) and configuring an explicit multi-minute `coolDown` period prevents oscillation. Asymmetric thresholds and cool-down periods prevent rapid flapping (thrashing) where instances repeatedly add and terminate. Local study-map skill 1.9 (Implement Metric-Based and Schedule-Based App Service Autoscaling Rules and Cooldowns), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Asymmetric thresholds and cool-down periods prevent rapid flapping (thrashing) where instances repeatedly add and terminate. In this scenario: Widening the hysteresis band (e.g., >75% scale-out, <35% scale-in) and configuring an explicit multi-minute `coolDown` period prevents oscillation.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Widening the hysteresis band (e.g., >75% scale-out, <35% scale-in) and configuring an explicit multi-minute `coolDown` period prevents oscillation.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Widening the hysteresis band (e.g., >75% scale-out, <35% scale-in) and configuring an explicit multi-minute `coolDown` period prevents oscillation.
- **D:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Widening the hysteresis band (e.g., >75% scale-out, <35% scale-in) and configuring an explicit multi-minute `coolDown` period prevents oscillation.

### Question 19 — B

Answer: Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps. Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH=/warmup/ready` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` holds swap completion until warm-up succeeds. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. Local study-map skill 1.9 (Implement Metric-Based and Schedule-Based App Service Autoscaling Rules and Cooldowns), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH=/warmup/ready` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` holds swap completion until warm-up succeeds.
- **B:** Correct. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. In this scenario: Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH=/warmup/ready` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` holds swap completion until warm-up succeeds.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH=/warmup/ready` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` holds swap completion until warm-up succeeds.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH=/warmup/ready` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` holds swap completion until warm-up succeeds.

### Question 20 — A

Answer: Mark environment-specific settings such as `PaymentWebhookUrl` and production connection strings as `slotSetting: true` (Deployment slot setting) before swapping slots. Marking the gateway setting with `slotSetting: true` (Deployment slot setting) prevents staging and production values from swapping places. Slot-sticky settings stay pinned to their slot (`Production` vs `Staging`) across swaps instead of traveling with the swapped code. Local study-map skill 1.10 (Configure App Service Deployment Slots, Slot-Sticky Settings, Warm-Up, and Traffic Routing), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Slot-sticky settings stay pinned to their slot (`Production` vs `Staging`) across swaps instead of traveling with the swapped code. In this scenario: Marking the gateway setting with `slotSetting: true` (Deployment slot setting) prevents staging and production values from swapping places.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Marking the gateway setting with `slotSetting: true` (Deployment slot setting) prevents staging and production values from swapping places.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Marking the gateway setting with `slotSetting: true` (Deployment slot setting) prevents staging and production values from swapping places.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Marking the gateway setting with `slotSetting: true` (Deployment slot setting) prevents staging and production values from swapping places.

### Question 21 — D

Answer: Host the Function App on `Flex Consumption` or `Elastic Premium (EP1+)` when VNet integration, longer execution timeouts beyond 10 minutes, or pre-warmed/always-ready instances are required. Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runtimes) meets VNet, warm-readiness, and duration requirements. Classic Consumption caps timeout at 10 minutes (`functionTimeout`) and cold-starts from zero; `Flex Consumption` and `Premium` add VNet outbound and pre-warmed readiness. Local study-map skill 1.11 (Create and Configure Azure Functions Apps, Hosting Plans, and host.json Settings), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runtimes) meets VNet, warm-readiness, and duration requirements.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runtimes) meets VNet, warm-readiness, and duration requirements.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runtimes) meets VNet, warm-readiness, and duration requirements.
- **D:** Correct. Classic Consumption caps timeout at 10 minutes (`functionTimeout`) and cold-starts from zero; `Flex Consumption` and `Premium` add VNet outbound and pre-warmed readiness. In this scenario: Hosting on `Elastic Premium (EP1+)` (or `Flex Consumption` with always-ready instances and VNet integration; Premium for >10-min/unbounded runtimes) meets VNet, warm-readiness, and duration requirements.

### Question 22 — B

Answer: Configure `"functionTimeout": "00:10:00"` and `"logging": { "applicationInsights": { "samplingSettings": { "isEnabled": true, "excludedTypes": "Request;Exception" } } }` inside `host.json`. Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` configures the entire Function host. `host.json` governs global Function host behaviors such as execution timeout and Application Insights telemetry sampling exclusions across all functions in the app. Local study-map skill 1.11 (Create and Configure Azure Functions Apps, Hosting Plans, and host.json Settings), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` configures the entire Function host.
- **B:** Correct. `host.json` governs global Function host behaviors such as execution timeout and Application Insights telemetry sampling exclusions across all functions in the app. In this scenario: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` configures the entire Function host.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` configures the entire Function host.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` inside `logging.applicationInsights.samplingSettings` configures the entire Function host.

### Question 23 — A, D

Answers: In the .NET isolated worker model, return a custom POCO class uniting `[HttpResult]` (or `HttpResponseData`) with `[CosmosDBOutput]` / `[ServiceBusOutput]` properties; Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`. Returning a multi-output POCO uniting `[HttpResult]` + `[CosmosDBOutput]` works in isolated worker processes, while `[CosmosDBTrigger]` with a `leases` container streams leaderboard changes. Local study-map skill 1.12 (Implement Azure Functions Input and Output Bindings (Isolated Worker & Declarative Bindings)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Isolated-worker C# functions cannot use `out` parameters for bindings; multi-output types return structured properties on a single return object. In this scenario: Returning a multi-output POCO uniting `[HttpResult]` + `[CosmosDBOutput]` works in isolated worker processes, while `[CosmosDBTrigger]` with a `leases` container streams leaderboard changes.
- **B:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Returning a multi-output POCO uniting `[HttpResult]` + `[CosmosDBOutput]` works in isolated worker processes, while `[CosmosDBTrigger]` with a `leases` container streams leaderboard changes.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Returning a multi-output POCO uniting `[HttpResult]` + `[CosmosDBOutput]` works in isolated worker processes, while `[CosmosDBTrigger]` with a `leases` container streams leaderboard changes.
- **D:** Correct. `CosmosDBTrigger` wraps the Change Feed Processor library and requires a lease container connection to coordinate partition checkpoints across scaled workers. In this scenario: Returning a multi-output POCO uniting `[HttpResult]` + `[CosmosDBOutput]` works in isolated worker processes, while `[CosmosDBTrigger]` with a `leases` container streams leaderboard changes.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Returning a multi-output POCO uniting `[HttpResult]` + `[CosmosDBOutput]` works in isolated worker processes, while `[CosmosDBTrigger]` with a `leases` container streams leaderboard changes.

### Question 24 — B

Answer: Apply `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` (or `[FixedDelayRetry]`) on the `[EventHubTrigger]` / `[TimerTrigger]` function. Applying `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` replays failed trigger executions in-memory before advancing partition checkpoints. Function-level retry attributes replay failed executions in-memory before advancing trigger checkpoints on Event Hubs and Timer triggers. Local study-map skill 1.12 (Implement Azure Functions Input and Output Bindings (Isolated Worker & Declarative Bindings)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Applying `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` replays failed trigger executions in-memory before advancing partition checkpoints.
- **B:** Correct. Function-level retry attributes replay failed executions in-memory before advancing trigger checkpoints on Event Hubs and Timer triggers. In this scenario: Applying `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` replays failed trigger executions in-memory before advancing partition checkpoints.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Applying `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` replays failed trigger executions in-memory before advancing partition checkpoints.
- **D:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Applying `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` replays failed trigger executions in-memory before advancing partition checkpoints.

### Question 25 — C

Answer: Specify a six-field NCRONTAB expression `{second} {minute} {hour} {day} {month} {day-of-week}` such as `"0 */15 9-17 * * 1-5"` on `[TimerTrigger]`. `"0 */15 9-17 * * 1-5"` specifies `0` seconds at the start and runs every 15 minutes across hours 9–17 Monday through Friday. Azure Functions `[TimerTrigger]` uses 6-field NCRONTAB (leading seconds field), unlike 5-field Unix cron. Local study-map skill 1.13 (Implement Function Triggers Using Cosmos DB/Blob Data Operations, NCRONTAB Timers, and Webhooks), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` specifies `0` seconds at the start and runs every 15 minutes across hours 9–17 Monday through Friday.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` specifies `0` seconds at the start and runs every 15 minutes across hours 9–17 Monday through Friday.
- **C:** Correct. Azure Functions `[TimerTrigger]` uses 6-field NCRONTAB (leading seconds field), unlike 5-field Unix cron. In this scenario: `"0 */15 9-17 * * 1-5"` specifies `0` seconds at the start and runs every 15 minutes across hours 9–17 Monday through Friday.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` specifies `0` seconds at the start and runs every 15 minutes across hours 9–17 Monday through Friday.

### Question 26 — C

Answer: Configure `[BlobTrigger(..., Source = BlobTriggerSource.EventGrid)]` with an Event Grid system topic subscription instead of default container-log polling. Setting `Source = BlobTriggerSource.EventGrid` with an Event Grid `BlobCreated` subscription replaces periodic storage-log polling with immediate push invocation. Event Grid-sourced blob triggers eliminate storage-log scan latency and work reliably on Blob-only / high-scale storage accounts. Local study-map skill 1.13 (Implement Function Triggers Using Cosmos DB/Blob Data Operations, NCRONTAB Timers, and Webhooks), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Setting `Source = BlobTriggerSource.EventGrid` with an Event Grid `BlobCreated` subscription replaces periodic storage-log polling with immediate push invocation.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `Source = BlobTriggerSource.EventGrid` with an Event Grid `BlobCreated` subscription replaces periodic storage-log polling with immediate push invocation.
- **C:** Correct. Event Grid-sourced blob triggers eliminate storage-log scan latency and work reliably on Blob-only / high-scale storage accounts. In this scenario: Setting `Source = BlobTriggerSource.EventGrid` with an Event Grid `BlobCreated` subscription replaces periodic storage-log polling with immediate push invocation.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `Source = BlobTriggerSource.EventGrid` with an Event Grid `BlobCreated` subscription replaces periodic storage-log polling with immediate push invocation.

### Question 27 — B, C, D

Answers: Register `CosmosClient` as a process-wide singleton in dependency injection and choose a high-cardinality `PartitionKey` path (or up to 3-level `Hierarchical` subpartition paths) that distributes RU/s evenly; Use `container.CreateTransactionalBatch(new PartitionKey(pkValue))` to group multiple create/replace/upsert/delete operations atomically within the same logical partition; Call `await container.PatchItemAsync<Order>(id, new PartitionKey(pk), new[] { PatchOperation.Increment("/retryCount", 1), PatchOperation.Set("/lastStatus", "Queued") })`. Registering singleton `CosmosClient` prevents socket exhaustion, `CreateTransactionalBatch` commits single-partition writes atomically, and `PatchItemAsync` mutates individual JSON paths server-side. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Registering singleton `CosmosClient` prevents socket exhaustion, `CreateTransactionalBatch` commits single-partition writes atomically, and `PatchItemAsync` mutates individual JSON paths server-side.
- **B:** Correct. Partial Document Update (`PatchItemAsync`) mutates specific JSON paths server-side without reading, deserializing, and replacing the full document payload. In this scenario: Registering singleton `CosmosClient` prevents socket exhaustion, `CreateTransactionalBatch` commits single-partition writes atomically, and `PatchItemAsync` mutates individual JSON paths server-side.
- **C:** Correct. Reusing one thread-safe `CosmosClient` avoids socket exhaustion, and hierarchical/high-cardinality partition keys prevent hot partitions and 20 GB single-partition caps. In this scenario: Registering singleton `CosmosClient` prevents socket exhaustion, `CreateTransactionalBatch` commits single-partition writes atomically, and `PatchItemAsync` mutates individual JSON paths server-side.
- **D:** Correct. `TransactionalBatch` guarantees ACID all-or-nothing execution serialized in one network round-trip, strictly scoped to a single logical partition key. In this scenario: Registering singleton `CosmosClient` prevents socket exhaustion, `CreateTransactionalBatch` commits single-partition writes atomically, and `PatchItemAsync` mutates individual JSON paths server-side.
- **E:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Registering singleton `CosmosClient` prevents socket exhaustion, `CreateTransactionalBatch` commits single-partition writes atomically, and `PatchItemAsync` mutates individual JSON paths server-side.
- **F:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Registering singleton `CosmosClient` prevents socket exhaustion, `CreateTransactionalBatch` commits single-partition writes atomically, and `PatchItemAsync` mutates individual JSON paths server-side.

### Question 28 — B

Answer: Define `new ContainerProperties(id: "telemetry", partitionKeyPaths: new List<string> { "/tenantId", "/siteId", "/deviceId" })` using `PartitionKeyBuilder` on reads and writes. Defining Hierarchical Partition Keys (`partitionKeyPaths: ["/tenantId", "/siteId", "/deviceId"]`) scales individual tenants past 20 GB while preserving targeted prefix queries. Hierarchical partition keys (up to 3 levels) overcome the 20 GB logical-partition limit on large tenants while preserving efficient prefix queries on `/tenantId` alone. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Defining Hierarchical Partition Keys (`partitionKeyPaths: ["/tenantId", "/siteId", "/deviceId"]`) scales individual tenants past 20 GB while preserving targeted prefix queries.
- **B:** Correct. Hierarchical partition keys (up to 3 levels) overcome the 20 GB logical-partition limit on large tenants while preserving efficient prefix queries on `/tenantId` alone. In this scenario: Defining Hierarchical Partition Keys (`partitionKeyPaths: ["/tenantId", "/siteId", "/deviceId"]`) scales individual tenants past 20 GB while preserving targeted prefix queries.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Defining Hierarchical Partition Keys (`partitionKeyPaths: ["/tenantId", "/siteId", "/deviceId"]`) scales individual tenants past 20 GB while preserving targeted prefix queries.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Defining Hierarchical Partition Keys (`partitionKeyPaths: ["/tenantId", "/siteId", "/deviceId"]`) scales individual tenants past 20 GB while preserving targeted prefix queries.

### Question 29 — B

Answer: Use `FeedIterator<Order> iter = container.GetItemQueryIterator<Order>(queryDef, requestOptions: new QueryRequestOptions { PartitionKey = new PartitionKey(pk), MaxItemCount = 100 })` and loop `while (iter.HasMoreResults) { FeedResponse<Order> page = await iter.ReadNextAsync(); }`. `container.GetItemQueryIterator<Order>` with `QueryRequestOptions { PartitionKey = ..., MaxItemCount = 100 }` and `while (iter.HasMoreResults) { await iter.ReadNextAsync(); }` paginates cleanly. `GetItemQueryIterator<T>` streams paginated results via continuation tokens and inspects `page.RequestCharge` without buffering an entire partition in memory. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `container.GetItemQueryIterator<Order>` with `QueryRequestOptions { PartitionKey = ..., MaxItemCount = 100 }` and `while (iter.HasMoreResults) { await iter.ReadNextAsync(); }` paginates cleanly.
- **B:** Correct. `GetItemQueryIterator<T>` streams paginated results via continuation tokens and inspects `page.RequestCharge` without buffering an entire partition in memory. In this scenario: `container.GetItemQueryIterator<Order>` with `QueryRequestOptions { PartitionKey = ..., MaxItemCount = 100 }` and `while (iter.HasMoreResults) { await iter.ReadNextAsync(); }` paginates cleanly.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `container.GetItemQueryIterator<Order>` with `QueryRequestOptions { PartitionKey = ..., MaxItemCount = 100 }` and `while (iter.HasMoreResults) { await iter.ReadNextAsync(); }` paginates cleanly.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `container.GetItemQueryIterator<Order>` with `QueryRequestOptions { PartitionKey = ..., MaxItemCount = 100 }` and `while (iter.HasMoreResults) { await iter.ReadNextAsync(); }` paginates cleanly.

### Question 30 — B

Answer: Use `Session` consistency (the default) and propagate `x-ms-session-token` (`RequestOptions.SessionToken`) across client/middle-tier hops to guarantee monotonic read-your-own-writes at half the read RU cost of `Strong`. Keeping `Session` consistency and forwarding `SessionToken` (`x-ms-session-token`) across client/server requests guarantees read-your-own-writes at 50% of `Strong` read RUs. `Session` consistency guarantees read-your-writes, monotonic reads, and write-follows-reads within a session token at 50% of `Strong` / `BoundedStaleness` read RUs. Local study-map skill 2.2 (Select and Override Cosmos DB Consistency Levels and Session Tokens), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Keeping `Session` consistency and forwarding `SessionToken` (`x-ms-session-token`) across client/server requests guarantees read-your-own-writes at 50% of `Strong` read RUs.
- **B:** Correct. `Session` consistency guarantees read-your-writes, monotonic reads, and write-follows-reads within a session token at 50% of `Strong` / `BoundedStaleness` read RUs. In this scenario: Keeping `Session` consistency and forwarding `SessionToken` (`x-ms-session-token`) across client/server requests guarantees read-your-own-writes at 50% of `Strong` read RUs.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Keeping `Session` consistency and forwarding `SessionToken` (`x-ms-session-token`) across client/server requests guarantees read-your-own-writes at 50% of `Strong` read RUs.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Keeping `Session` consistency and forwarding `SessionToken` (`x-ms-session-token`) across client/server requests guarantees read-your-own-writes at 50% of `Strong` read RUs.

### Question 31 — C

Answer: Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency. `BoundedStaleness` enforces global write ordering across read regions within explicit `K` item-version and `T` time bounds. `Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds. Local study-map skill 2.2 (Select and Override Cosmos DB Consistency Levels and Session Tokens), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `BoundedStaleness` enforces global write ordering across read regions within explicit `K` item-version and `T` time bounds.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `BoundedStaleness` enforces global write ordering across read regions within explicit `K` item-version and `T` time bounds.
- **C:** Correct. `Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds. In this scenario: `BoundedStaleness` enforces global write ordering across read regions within explicit `K` item-version and `T` time bounds.
- **D:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `BoundedStaleness` enforces global write ordering across read regions within explicit `K` item-version and `T` time bounds.

### Question 32 — A

Answer: Create the monitored container and a dedicated lease container → call GetChangeFeedProcessorBuilder<T> with processorName and delegate → attach WithInstanceName and WithLeaseContainer → call Build and StartAsync on the processor. Provisioning the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` boots distributed polling cleanly. Both monitored and lease containers must exist before configuring the builder with instance/lease metadata, building the processor, and starting polling. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Both monitored and lease containers must exist before configuring the builder with instance/lease metadata, building the processor, and starting polling. In this scenario: Provisioning the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` boots distributed polling cleanly.
- **B:** Incorrect for this requirement. Builder method order is inverted, and using a separate dedicated lease container avoids RU contention and partition-key mismatches. Why the keyed choice wins: Provisioning the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` boots distributed polling cleanly.
- **C:** Incorrect for this requirement. Builder options cannot be attached after Build(), and omitting the lease container causes startup failure. Why the keyed choice wins: Provisioning the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` boots distributed polling cleanly.
- **D:** Incorrect for this requirement. A processor cannot start before it is built or before its lease container exists. Why the keyed choice wins: Provisioning the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` boots distributed polling cleanly.

### Question 33 — A, B

Answers: Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay; Use Change Feed `AllVersionsAndDeletes` mode (or soft-delete flag items with short TTL in `LatestVersion` mode) because default `LatestVersion` change feed omits hard-deleted items. Distinct `processorName` registrations give each service its own independent lease cursor, while `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) surfaces deleted assets. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Standard `LatestVersion` change feed emits only inserts and updates of current items; hard deletes require `AllVersionsAndDeletes` or soft-delete Tombstone items + TTL. In this scenario: Distinct `processorName` registrations give each service its own independent lease cursor, while `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) surfaces deleted assets.
- **B:** Correct. In Change Feed Processor, `processorName` acts like an Event Hubs consumer group: distinct names receive independent copies of every insert/update, while identical names load-balance partitions. In this scenario: Distinct `processorName` registrations give each service its own independent lease cursor, while `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) surfaces deleted assets.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Distinct `processorName` registrations give each service its own independent lease cursor, while `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) surfaces deleted assets.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Distinct `processorName` registrations give each service its own independent lease cursor, while `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) surfaces deleted assets.
- **E:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Distinct `processorName` registrations give each service its own independent lease cursor, while `AllVersionsAndDeletes` mode (or soft-delete flags + TTL) surfaces deleted assets.

### Question 34 — B

Answer: Attach searchable key-value `Tags` (`SetTagsAsync` / `BlobUploadOptions.Tags`) and query across containers with `FindBlobsByTagsAsync("@container = 'docs' AND status = 'pending'")`. Writing Blob Index `Tags` (`SetTagsAsync`) and calling `FindBlobsByTagsAsync` searches Azure Storage's native tag index across containers directly. Blob Index Tags are indexed natively by Azure Storage for server-side filtering, whereas `Metadata` is not searchable without listing every blob. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Writing Blob Index `Tags` (`SetTagsAsync`) and calling `FindBlobsByTagsAsync` searches Azure Storage's native tag index across containers directly.
- **B:** Correct. Blob Index Tags are indexed natively by Azure Storage for server-side filtering, whereas `Metadata` is not searchable without listing every blob. In this scenario: Writing Blob Index `Tags` (`SetTagsAsync`) and calling `FindBlobsByTagsAsync` searches Azure Storage's native tag index across containers directly.
- **C:** Incorrect for this requirement. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. Why the keyed choice wins: Writing Blob Index `Tags` (`SetTagsAsync`) and calling `FindBlobsByTagsAsync` searches Azure Storage's native tag index across containers directly.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Writing Blob Index `Tags` (`SetTagsAsync`) and calling `FindBlobsByTagsAsync` searches Azure Storage's native tag index across containers directly.

### Question 35 — D

Answer: Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`). `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata keys. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata keys.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata keys.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata keys.
- **D:** Correct. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. In this scenario: `SetHttpHeadersAsync(BlobHttpHeaders)` updates standard HTTP system properties, while `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` metadata keys.

### Question 36 — C

Answer: Call `await blobClient.CreateSnapshotAsync()` for explicit point-in-time read-only checkpoints or enable account-level Blob Versioning so every `UploadAsync` overwrite retains an immutable `VersionId`. Account-level Blob Versioning automatically preserves an immutable `VersionId` on every overwrite or delete, whereas snapshots require explicit `CreateSnapshotAsync()` calls. Snapshots capture explicit developer-triggered checkpoints, whereas Blob Versioning automatically preserves prior state on every overwrite or delete. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Account-level Blob Versioning automatically preserves an immutable `VersionId` on every overwrite or delete, whereas snapshots require explicit `CreateSnapshotAsync()` calls.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Account-level Blob Versioning automatically preserves an immutable `VersionId` on every overwrite or delete, whereas snapshots require explicit `CreateSnapshotAsync()` calls.
- **C:** Correct. Snapshots capture explicit developer-triggered checkpoints, whereas Blob Versioning automatically preserves prior state on every overwrite or delete. In this scenario: Account-level Blob Versioning automatically preserves an immutable `VersionId` on every overwrite or delete, whereas snapshots require explicit `CreateSnapshotAsync()` calls.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Account-level Blob Versioning automatically preserves an immutable `VersionId` on every overwrite or delete, whereas snapshots require explicit `CreateSnapshotAsync()` calls.

### Question 37 — D

Answer: Use `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` (15–60 seconds or `-1` infinite) and pass `LeaseId` inside `BlobRequestConditions` on subsequent writes/deletes. Acquiring a 60-second lease via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` enforces exclusive single-writer access. Blob leases grant exclusive write/delete locks (`15` to `60` seconds or infinite `-1`) so competing workers immediately receive `412 LeaseIdMissing/Mismatch`. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Acquiring a 60-second lease via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` enforces exclusive single-writer access.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Acquiring a 60-second lease via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` enforces exclusive single-writer access.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Acquiring a 60-second lease via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` enforces exclusive single-writer access.
- **D:** Correct. Blob leases grant exclusive write/delete locks (`15` to `60` seconds or infinite `-1`) so competing workers immediately receive `412 LeaseIdMissing/Mismatch`. In this scenario: Acquiring a 60-second lease via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` enforces exclusive single-writer access.

### Question 38 — B

Answer: Invoke `BlobClient.StartCopyFromUriAsync(sourceSasUri)` to trigger asynchronous server-side blob copy and inspect `CopyStatus` without streaming bytes through the client VM. `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` reports progress. `StartCopyFromUriAsync` instructs Azure Storage fabric to copy blobs asynchronously server-to-server using a readable source URI/SAS. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` reports progress.
- **B:** Correct. `StartCopyFromUriAsync` instructs Azure Storage fabric to copy blobs asynchronously server-to-server using a readable source URI/SAS. In this scenario: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` reports progress.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` reports progress.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` reports progress.

### Question 39 — A

Answer: Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`. Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` restricts the token strictly. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. In this scenario: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` restricts the token strictly.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` restricts the token strictly.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` restricts the token strictly.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Protocol = SasProtocol.HttpsOnly`, 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` restricts the token strictly.

### Question 40 — D, E

Answers: Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage; Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob). Locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention, while `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` expedites Archive rehydration. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention, while `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` expedites Archive rehydration.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention, while `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` expedites Archive rehydration.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention, while `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` expedites Archive rehydration.
- **D:** Correct. `SetAccessTierAsync` (or copy-to-Hot) initiates Archive rehydration; `RehydratePriority.High` prioritizes restoration (often under 1 hour for <10 GB blobs). In this scenario: Locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention, while `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` expedites Archive rehydration.
- **E:** Correct. Time-based locked retention and legal holds block modification and deletion even by Storage Account Owners until retention expires and holds clear. In this scenario: Locked Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention, while `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` expedites Archive rehydration.

### Question 41 — A, B

Answers: Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps; Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`. `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public desktop clients, while `AcquireTokenSilent` with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens cleanly. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. MSAL refreshes cached tokens transparently during `AcquireTokenSilent`; prompting interactively on every call degrades UX and hits rate limits. In this scenario: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public desktop clients, while `AcquireTokenSilent` with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens cleanly.
- **B:** Correct. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. In this scenario: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public desktop clients, while `AcquireTokenSilent` with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens cleanly.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public desktop clients, while `AcquireTokenSilent` with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens cleanly.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public desktop clients, while `AcquireTokenSilent` with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens cleanly.
- **E:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public desktop clients, while `AcquireTokenSilent` with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens cleanly.

### Question 42 — D

Answer: Use `ConfidentialClientApplicationBuilder` authenticated with a client certificate (or workload identity assertion) calling `AcquireTokenForClient(new[] { "api://.../.default" })` for headless background daemons. `ConfidentialClientApplicationBuilder` using `WithCertificate` and calling `AcquireTokenForClient(new[] { "api://royalties/.default" })` executes OAuth 2.0 Client Credentials without user interaction. Daemon apps without a signed-in user use OAuth 2.0 Client Credentials flow and must request the `.default` scope for pre-consented application permissions. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` using `WithCertificate` and calling `AcquireTokenForClient(new[] { "api://royalties/.default" })` executes OAuth 2.0 Client Credentials without user interaction.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` using `WithCertificate` and calling `AcquireTokenForClient(new[] { "api://royalties/.default" })` executes OAuth 2.0 Client Credentials without user interaction.
- **C:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` using `WithCertificate` and calling `AcquireTokenForClient(new[] { "api://royalties/.default" })` executes OAuth 2.0 Client Credentials without user interaction.
- **D:** Correct. Daemon apps without a signed-in user use OAuth 2.0 Client Credentials flow and must request the `.default` scope for pre-consented application permissions. In this scenario: `ConfidentialClientApplicationBuilder` using `WithCertificate` and calling `AcquireTokenForClient(new[] { "api://royalties/.default" })` executes OAuth 2.0 Client Credentials without user interaction.

### Question 43 — D

Answer: Call `await confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` inside the middle-tier API. `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` executes the OAuth 2.0 On-Behalf-Of exchange. OAuth 2.0 On-Behalf-Of (`AcquireTokenOnBehalfOf`) exchanges an incoming user access token for a downstream API token while preserving delegated user identity and consent. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` executes the OAuth 2.0 On-Behalf-Of exchange.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` executes the OAuth 2.0 On-Behalf-Of exchange.
- **C:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` executes the OAuth 2.0 On-Behalf-Of exchange.
- **D:** Correct. OAuth 2.0 On-Behalf-Of (`AcquireTokenOnBehalfOf`) exchanges an incoming user access token for a downstream API token while preserving delegated user identity and consent. In this scenario: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` executes the OAuth 2.0 On-Behalf-Of exchange.

### Question 44 — C

Answer: Declare `appRoles` with `allowedMemberTypes: ["User", "Application"]` in the Entra app registration manifest and validate the `roles` claim (`[Authorize(Roles = "...")]`) in the web API. Declaring `GridOperator` under `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits `roles` JWT claims for both assigned users and service principals. Entra ID emits assigned app roles inside the `roles` JWT claim for both human users and service principals without requiring directory-level Entra admin roles. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Declaring `GridOperator` under `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits `roles` JWT claims for both assigned users and service principals.
- **B:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Declaring `GridOperator` under `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits `roles` JWT claims for both assigned users and service principals.
- **C:** Correct. Entra ID emits assigned app roles inside the `roles` JWT claim for both human users and service principals without requiring directory-level Entra admin roles. In this scenario: Declaring `GridOperator` under `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits `roles` JWT claims for both assigned users and service principals.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Declaring `GridOperator` under `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits `roles` JWT claims for both assigned users and service principals.

### Question 45 — D

Answer: Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation. Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) blocks personal accounts while explicit `tid` / issuer validation enforces the contracted partner allowlist. Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) blocks personal accounts while explicit `tid` / issuer validation enforces the contracted partner allowlist.
- **B:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) blocks personal accounts while explicit `tid` / issuer validation enforces the contracted partner allowlist.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) blocks personal accounts while explicit `tid` / issuer validation enforces the contracted partner allowlist.
- **D:** Correct. Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`. In this scenario: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) blocks personal accounts while explicit `tid` / issuer validation enforces the contracted partner allowlist.

### Question 46 — B

Answer: Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`). Setting unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean REST status codes instead of browser `302` redirects. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean REST status codes instead of browser `302` redirects.
- **B:** Correct. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. In this scenario: Setting unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean REST status codes instead of browser `302` redirects.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean REST status codes instead of browser `302` redirects.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean REST status codes instead of browser `302` redirects.

### Question 47 — C

Answer: Assign Storage Blob Data Contributor/Delegator RBAC to the identity → instantiate BlobServiceClient with DefaultAzureCredential → call GetUserDelegationKeyAsync for a bounded validity window → build BlobSasBuilder and sign with the user delegation key. Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) creates a User Delegation SAS. Entra RBAC must authorize delegation before BlobServiceClient requests a user delegation key, which then signs the BlobSasBuilder token without account keys. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. GetUserDelegationKeyAsync requires an authenticated Entra client with RBAC already granted before the call executes. Why the keyed choice wins: Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) creates a User Delegation SAS.
- **B:** Incorrect for this requirement. A SAS cannot be signed before obtaining the user delegation key, and shared account keys cannot mint Entra user delegation SAS tokens. Why the keyed choice wins: Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) creates a User Delegation SAS.
- **C:** Correct. Entra RBAC must authorize delegation before BlobServiceClient requests a user delegation key, which then signs the BlobSasBuilder token without account keys. In this scenario: Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) creates a User Delegation SAS.
- **D:** Incorrect for this requirement. The client must authenticate with Microsoft Entra credentials first so it can request the delegation key that mints the SAS. Why the keyed choice wins: Granting `Storage Blob Delegator` + Blob RBAC, creating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) creates a User Delegation SAS.

### Question 48 — D

Answer: Bind a Service SAS to a container/queue/table Stored Access Policy (`SignedIdentifier`, omitting inline start/expiry/permissions) so compromised tokens can be revoked instantly by modifying or deleting the policy. Inline Service SAS tokens lack independent revocation; binding the SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets admins revoke access instantly by deleting or updating that policy. Up to 5 Stored Access Policies per container allow instant SAS revocation without rotating storage account keys; Note that User Delegation SAS uses key revocation instead of Stored Access Policies. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Inline Service SAS tokens lack independent revocation; binding the SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets admins revoke access instantly by deleting or updating that policy.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Inline Service SAS tokens lack independent revocation; binding the SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets admins revoke access instantly by deleting or updating that policy.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Inline Service SAS tokens lack independent revocation; binding the SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets admins revoke access instantly by deleting or updating that policy.
- **D:** Correct. Up to 5 Stored Access Policies per container allow instant SAS revocation without rotating storage account keys; Note that User Delegation SAS uses key revocation instead of Stored Access Policies. In this scenario: Inline Service SAS tokens lack independent revocation; binding the SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets admins revoke access instantly by deleting or updating that policy.

### Question 49 — C

Answer: Mint a short-lived HTTPS-only (`SasProtocol.HttpsOnly`) User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` instead of Account or Service SAS signed with storage account keys. User Delegation SAS signed via `GetUserDelegationKeyAsync` uses Microsoft Entra credentials rather than disabled storage account shared keys. User Delegation SAS eliminates shared storage account keys, enforces Entra RBAC, and automatically invalidates if the signing identity loses permissions. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: User Delegation SAS signed via `GetUserDelegationKeyAsync` uses Microsoft Entra credentials rather than disabled storage account shared keys.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: User Delegation SAS signed via `GetUserDelegationKeyAsync` uses Microsoft Entra credentials rather than disabled storage account shared keys.
- **C:** Correct. User Delegation SAS eliminates shared storage account keys, enforces Entra RBAC, and automatically invalidates if the signing identity loses permissions. In this scenario: User Delegation SAS signed via `GetUserDelegationKeyAsync` uses Microsoft Entra credentials rather than disabled storage account shared keys.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: User Delegation SAS signed via `GetUserDelegationKeyAsync` uses Microsoft Entra credentials rather than disabled storage account shared keys.

### Question 50 — D, E

Answers: Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`; Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses. Requesting least-privilege scopes with `$select` + `PageIterator<T>` handles clean paging, while `BatchRequestContentCollection` (`/$batch`) combines up to 20 calls and honors `Retry-After`. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Requesting least-privilege scopes with `$select` + `PageIterator<T>` handles clean paging, while `BatchRequestContentCollection` (`/$batch`) combines up to 20 calls and honors `Retry-After`.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Requesting least-privilege scopes with `$select` + `PageIterator<T>` handles clean paging, while `BatchRequestContentCollection` (`/$batch`) combines up to 20 calls and honors `Retry-After`.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Requesting least-privilege scopes with `$select` + `PageIterator<T>` handles clean paging, while `BatchRequestContentCollection` (`/$batch`) combines up to 20 calls and honors `Retry-After`.
- **D:** Correct. Microsoft Graph enforces least-privilege consent scopes, trims payload size with `$select`, and paginates `@odata.nextLink` cleanly through `PageIterator<T>`. In this scenario: Requesting least-privilege scopes with `$select` + `PageIterator<T>` handles clean paging, while `BatchRequestContentCollection` (`/$batch`) combines up to 20 calls and honors `Retry-After`.
- **E:** Correct. Graph JSON batching (`/$batch`) bundles up to 20 sub-requests per round-trip, while built-in SDK retry middleware respects `Retry-After`. In this scenario: Requesting least-privilege scopes with `$select` + `PageIterator<T>` handles clean paging, while `BatchRequestContentCollection` (`/$batch`) combines up to 20 calls and honors `Retry-After`.

### Question 51 — D

Answer: Call `await graphClient.Users.GetAsync(rc => { rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }; rc.QueryParameters.Filter = "accountEnabled eq true"; })`. Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` applies OData projection and filtering server-side. In Microsoft Graph .NET SDK v5, `$select` and `$filter` query parameters reduce payload size and network transfer on collection endpoints. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` applies OData projection and filtering server-side.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` applies OData projection and filtering server-side.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` applies OData projection and filtering server-side.
- **D:** Correct. In Microsoft Graph .NET SDK v5, `$select` and `$filter` query parameters reduce payload size and network transfer on collection endpoints. In this scenario: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` applies OData projection and filtering server-side.

### Question 52 — B

Answer: Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses. Tight immediate retries amplify `429` throttling bans; bundling up to 20 independent requests via `BatchRequestContentCollection` (`/$batch`) and honoring the `Retry-After` header resolves both latency and rate limits. Graph JSON batching (`/$batch`) bundles up to 20 sub-requests per round-trip, while built-in SDK retry middleware respects `Retry-After`. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Tight immediate retries amplify `429` throttling bans; bundling up to 20 independent requests via `BatchRequestContentCollection` (`/$batch`) and honoring the `Retry-After` header resolves both latency and rate limits.
- **B:** Correct. Graph JSON batching (`/$batch`) bundles up to 20 sub-requests per round-trip, while built-in SDK retry middleware respects `Retry-After`. In this scenario: Tight immediate retries amplify `429` throttling bans; bundling up to 20 independent requests via `BatchRequestContentCollection` (`/$batch`) and honoring the `Retry-After` header resolves both latency and rate limits.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Tight immediate retries amplify `429` throttling bans; bundling up to 20 independent requests via `BatchRequestContentCollection` (`/$batch`) and honoring the `Retry-After` header resolves both latency and rate limits.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Tight immediate retries amplify `429` throttling bans; bundling up to 20 independent requests via `BatchRequestContentCollection` (`/$batch`) and honoring the `Retry-After` header resolves both latency and rate limits.

### Question 53 — C

Answer: Wire `options.Connect(new Uri(endpoint), cred).ConfigureKeyVault(kv => kv.SetCredential(cred))` so App Configuration resolves Key Vault reference items using the app identity. Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` registers the `TokenCredential` required to resolve Key Vault secret URIs stored in App Configuration. App Configuration stores only the Key Vault secret URI metadata; client code still requires `ConfigureKeyVault` credentials with `Key Vault Secrets User` rights on the target vault. Local study-map skill 3.5 (Manage Feature Flags, Labels, Sentinel Dynamic Refresh, and Key Vault References in Azure App Configuration), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` registers the `TokenCredential` required to resolve Key Vault secret URIs stored in App Configuration.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` registers the `TokenCredential` required to resolve Key Vault secret URIs stored in App Configuration.
- **C:** Correct. App Configuration stores only the Key Vault secret URI metadata; client code still requires `ConfigureKeyVault` credentials with `Key Vault Secrets User` rights on the target vault. In this scenario: Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` registers the `TokenCredential` required to resolve Key Vault secret URIs stored in App Configuration.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` registers the `TokenCredential` required to resolve Key Vault secret URIs stored in App Configuration.

### Question 54 — A, E

Answers: Use `SecretClient` (`Azure.Security.KeyVault.Secrets`) for connection strings/tokens, `KeyClient` / `CryptographyClient` (`Azure.Security.KeyVault.Keys`) for RSA/EC wrap-unwrap-sign, and `CertificateClient` for X.509 lifecycle; Enable Soft Delete (mandatory on new vaults, 7–90 days) plus Purge Protection on Azure Key Vault so neither accidental deletion nor malicious principals can permanently destroy keys before retention expires. Separating operations across `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` with RBAC roles plus enabling Soft Delete and Purge Protection satisfies both requirements. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Azure Key Vault SDK v4 splits secrets, cryptographic keys, and X.509 certificates into dedicated clients and RBAC data-plane roles (`Key Vault Secrets User`, `Crypto User`, `Certificates User`). In this scenario: Separating operations across `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` with RBAC roles plus enabling Soft Delete and Purge Protection satisfies both requirements.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Separating operations across `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` with RBAC roles plus enabling Soft Delete and Purge Protection satisfies both requirements.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Separating operations across `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` with RBAC roles plus enabling Soft Delete and Purge Protection satisfies both requirements.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Separating operations across `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` with RBAC roles plus enabling Soft Delete and Purge Protection satisfies both requirements.
- **E:** Correct. Soft Delete allows recovery via `StartRecoverDeletedSecretAsync`, while Purge Protection blocks permanent `PurgeDeletedSecretAsync` calls during retention. In this scenario: Separating operations across `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` with RBAC roles plus enabling Soft Delete and Purge Protection satisfies both requirements.

### Question 55 — D

Answer: Instantiate `new CryptographyClient(keyVaultKey.Id, new DefaultAzureCredential())` and invoke `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync(...)`. `CryptographyClient` invoking `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` performs envelope key wrapping without sending multi-GB video masters to Key Vault. Envelope encryption keeps bulk data encryption keys (`DEK`) wrapped by hardware/software-protected Key Vault KEKs without sending large payloads through Key Vault. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `CryptographyClient` invoking `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` performs envelope key wrapping without sending multi-GB video masters to Key Vault.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `CryptographyClient` invoking `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` performs envelope key wrapping without sending multi-GB video masters to Key Vault.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `CryptographyClient` invoking `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` performs envelope key wrapping without sending multi-GB video masters to Key Vault.
- **D:** Correct. Envelope encryption keeps bulk data encryption keys (`DEK`) wrapped by hardware/software-protected Key Vault KEKs without sending large payloads through Key Vault. In this scenario: `CryptographyClient` invoking `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync` performs envelope key wrapping without sending multi-GB video masters to Key Vault.

### Question 56 — B

Answer: Choose a User-Assigned Managed Identity when multiple compute resources must share one pre-provisioned identity lifecycle independent of individual app deletions; choose System-Assigned when 1-to-1 fate-sharing tied to a single resource is required. A User-Assigned Managed Identity has a standalone ARM lifecycle and reusable RBAC grants shared across ephemeral compute groups, unlike 1-to-1 System-Assigned identities. System-assigned identities are deleted automatically with their parent resource; user-assigned identities have an independent ARM lifecycle and reusable RBAC grants. Local study-map skill 3.7 (Implement System-Assigned and User-Assigned Managed Identities and DefaultAzureCredential), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: A User-Assigned Managed Identity has a standalone ARM lifecycle and reusable RBAC grants shared across ephemeral compute groups, unlike 1-to-1 System-Assigned identities.
- **B:** Correct. System-assigned identities are deleted automatically with their parent resource; user-assigned identities have an independent ARM lifecycle and reusable RBAC grants. In this scenario: A User-Assigned Managed Identity has a standalone ARM lifecycle and reusable RBAC grants shared across ephemeral compute groups, unlike 1-to-1 System-Assigned identities.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: A User-Assigned Managed Identity has a standalone ARM lifecycle and reusable RBAC grants shared across ephemeral compute groups, unlike 1-to-1 System-Assigned identities.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: A User-Assigned Managed Identity has a standalone ARM lifecycle and reusable RBAC grants shared across ephemeral compute groups, unlike 1-to-1 System-Assigned identities.

### Question 57 — A

Answer: Instantiate `new DefaultAzureCredential(new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId })` (or set `AZURE_CLIENT_ID`). Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) explicitly selects the target user-assigned identity. When a host has multiple user-assigned managed identities attached, IMDS rejects ambiguous token requests unless the target `clientId` (or resource ID) is specified. Local study-map skill 3.7 (Implement System-Assigned and User-Assigned Managed Identities and DefaultAzureCredential), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. When a host has multiple user-assigned managed identities attached, IMDS rejects ambiguous token requests unless the target `clientId` (or resource ID) is specified. In this scenario: Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) explicitly selects the target user-assigned identity.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) explicitly selects the target user-assigned identity.
- **C:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) explicitly selects the target user-assigned identity.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) explicitly selects the target user-assigned identity.

### Question 58 — B, E

Answers: Query Workspace-based Application Insights (`AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces` or classic `requests`/`dependencies`/`exceptions`) joining on `OperationId` (`operation_Id`) to reconstruct end-to-end distributed transactions; Run `AppRequests | where ResultCode == "500" | join kind=inner (AppDependencies | where Success == false) on OperationId | project TimeGenerated, Name, Target, DependencyType, ResultCode1`. Correlating tables on W3C `OperationId` (`operation_Id`) and running a KQL `join kind=inner` between failed `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` pinpoints root-cause dependencies. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Correlating tables on W3C `OperationId` (`operation_Id`) and running a KQL `join kind=inner` between failed `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` pinpoints root-cause dependencies.
- **B:** Correct. Joining `AppRequests` and `AppDependencies` on `OperationId` isolates which exact downstream SQL, HTTP, or Storage dependency triggered HTTP 500 responses. In this scenario: Correlating tables on W3C `OperationId` (`operation_Id`) and running a KQL `join kind=inner` between failed `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` pinpoints root-cause dependencies.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Correlating tables on W3C `OperationId` (`operation_Id`) and running a KQL `join kind=inner` between failed `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` pinpoints root-cause dependencies.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Correlating tables on W3C `OperationId` (`operation_Id`) and running a KQL `join kind=inner` between failed `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` pinpoints root-cause dependencies.
- **E:** Correct. W3C Trace-Context propagates `traceparent` into `operation_Id` across services so KQL joins pinpoint exact failing downstream dependencies. In this scenario: Correlating tables on W3C `OperationId` (`operation_Id`) and running a KQL `join kind=inner` between failed `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` pinpoints root-cause dependencies.

### Question 59 — D

Answer: Run `AppRequests | where TimeGenerated > ago(1h) | summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)`. Summarizing `AppRequests` over `ago(1h)` with `Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` outputs 5-minute error and p95 series. KQL `countif` and `percentile(..., 95)` grouped by `bin(TimeGenerated, 5m)` quantify error spikes and tail latency per operation over fixed time buckets. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Summarizing `AppRequests` over `ago(1h)` with `Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` outputs 5-minute error and p95 series.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Summarizing `AppRequests` over `ago(1h)` with `Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` outputs 5-minute error and p95 series.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Summarizing `AppRequests` over `ago(1h)` with `Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` outputs 5-minute error and p95 series.
- **D:** Correct. KQL `countif` and `percentile(..., 95)` grouped by `bin(TimeGenerated, 5m)` quantify error spikes and tail latency per operation over fixed time buckets. In this scenario: Summarizing `AppRequests` over `ago(1h)` with `Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` outputs 5-minute error and p95 series.

### Question 60 — A

Answer: Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits. Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) plus a brief drain delay before exit transmits buffered spans and metrics cleanly. Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics. In this scenario: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) plus a brief drain delay before exit transmits buffered spans and metrics cleanly.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) plus a brief drain delay before exit transmits buffered spans and metrics cleanly.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) plus a brief drain delay before exit transmits buffered spans and metrics cleanly.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) plus a brief drain delay before exit transmits buffered spans and metrics cleanly.

### Question 61 — C

Answer: Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`. Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively. `System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively.
- **C:** Correct. `System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro. In this scenario: Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Registering a `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` exports custom spans natively.

### Question 62 — D

Answer: Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group. Application Insights Standard Availability Tests validate SSL expiry and HTTP status across global POPs, and a `>= 2` failed-locations alert wired to an Action Group prevents single-region false alarms. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Application Insights Standard Availability Tests validate SSL expiry and HTTP status across global POPs, and a `>= 2` failed-locations alert wired to an Action Group prevents single-region false alarms.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Application Insights Standard Availability Tests validate SSL expiry and HTTP status across global POPs, and a `>= 2` failed-locations alert wired to an Action Group prevents single-region false alarms.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Application Insights Standard Availability Tests validate SSL expiry and HTTP status across global POPs, and a `>= 2` failed-locations alert wired to an Action Group prevents single-region false alarms.
- **D:** Correct. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. In this scenario: Application Insights Standard Availability Tests validate SSL expiry and HTTP status across global POPs, and a `>= 2` failed-locations alert wired to an Action Group prevents single-region false alarms.

### Question 63 — B

Answer: Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group. Running a VNet-integrated Timer-Triggered Function that tests the private SCADA endpoint and calls `TelemetryClient.TrackAvailability()` publishes custom availability telemetry for alerts. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Running a VNet-integrated Timer-Triggered Function that tests the private SCADA endpoint and calls `TelemetryClient.TrackAvailability()` publishes custom availability telemetry for alerts.
- **B:** Correct. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. In this scenario: Running a VNet-integrated Timer-Triggered Function that tests the private SCADA endpoint and calls `TelemetryClient.TrackAvailability()` publishes custom availability telemetry for alerts.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Running a VNet-integrated Timer-Triggered Function that tests the private SCADA endpoint and calls `TelemetryClient.TrackAvailability()` publishes custom availability telemetry for alerts.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Running a VNet-integrated Timer-Triggered Function that tests the private SCADA endpoint and calls `TelemetryClient.TrackAvailability()` publishes custom availability telemetry for alerts.

### Question 64 — D

Answer: Provision Workspace-based Application Insights and copy APPLICATIONINSIGHTS_CONNECTION_STRING → configure UseAzureMonitor() OpenTelemetry distro at startup → verify requests/dependencies in Logs → create a KQL or metric alert linked to an Action Group. Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, configuring `UseAzureMonitor()`, verifying spans in Logs, and creating an Action Group alert completes onboarding cleanly. Workspace-based Application Insights and connection-string OpenTelemetry setup emit telemetry first so KQL/metric alerts and Action Groups monitor real signals. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Classic Application Insights and bare Instrumentation Keys are retired in favor of Workspace-based resources and `APPLICATIONINSIGHTS_CONNECTION_STRING`. Why the keyed choice wins: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, configuring `UseAzureMonitor()`, verifying spans in Logs, and creating an Action Group alert completes onboarding cleanly.
- **B:** Incorrect for this requirement. Zero telemetry rate and missing connection strings discard all telemetry before it reaches Azure Monitor. Why the keyed choice wins: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, configuring `UseAzureMonitor()`, verifying spans in Logs, and creating an Action Group alert completes onboarding cleanly.
- **C:** Incorrect for this requirement. Alert queries require a target Application Insights / Log Analytics resource and instrumented telemetry emission. Why the keyed choice wins: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, configuring `UseAzureMonitor()`, verifying spans in Logs, and creating an Action Group alert completes onboarding cleanly.
- **D:** Correct. Workspace-based Application Insights and connection-string OpenTelemetry setup emit telemetry first so KQL/metric alerts and Action Groups monitor real signals. In this scenario: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, configuring `UseAzureMonitor()`, verifying spans in Logs, and creating an Action Group alert completes onboarding cleanly.

### Question 65 — A, B

Answers: Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments; Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently. `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps stored volume without sampling Live Metrics. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. In this scenario: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps stored volume without sampling Live Metrics.
- **B:** Correct. Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled. In this scenario: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps stored volume without sampling Live Metrics.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps stored volume without sampling Live Metrics.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps stored volume without sampling Live Metrics.
- **E:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) handles OpenTelemetry instrumentation, while Ingestion/Adaptive Sampling caps stored volume without sampling Live Metrics.

### Question 66 — B

Answer: Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments. Classic Instrumentation Keys are retired in favor of Workspace-based Application Insights instrumented with `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) and `APPLICATIONINSIGHTS_CONNECTION_STRING`. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Classic Instrumentation Keys are retired in favor of Workspace-based Application Insights instrumented with `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) and `APPLICATIONINSIGHTS_CONNECTION_STRING`.
- **B:** Correct. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. In this scenario: Classic Instrumentation Keys are retired in favor of Workspace-based Application Insights instrumented with `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) and `APPLICATIONINSIGHTS_CONNECTION_STRING`.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Classic Instrumentation Keys are retired in favor of Workspace-based Application Insights instrumented with `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) and `APPLICATIONINSIGHTS_CONNECTION_STRING`.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Classic Instrumentation Keys are retired in favor of Workspace-based Application Insights instrumented with `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) and `APPLICATIONINSIGHTS_CONNECTION_STRING`.

### Question 67 — A

Answer: Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`. `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens without static secrets. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. Local study-map skill 5.1 (Provision Azure API Management Tiers, VNet Modes, and Self-Hosted Hybrid Gateways), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. In this scenario: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens without static secrets.
- **B:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens without static secrets.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens without static secrets.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra tokens without static secrets.

### Question 68 — A

Answer: Use APIM `Revisions` to stage, test, and swap non-breaking internal changes safely on the same consumer URL (`;rev=2`), and use APIM `Versions` (path/header/query) when publishing breaking contract changes side-by-side for distinct consumer cohorts. `Revisions` stage and swap non-breaking edits transparently on the active URL, while `Versions` expose separate consumer-visible `/v1` and `/v2` contracts side by side. Revisions let authors edit and flip the `current` implementation transparently; Versions expose distinct URLs/headers so legacy clients keep working. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Revisions let authors edit and flip the `current` implementation transparently; Versions expose distinct URLs/headers so legacy clients keep working. In this scenario: `Revisions` stage and swap non-breaking edits transparently on the active URL, while `Versions` expose separate consumer-visible `/v1` and `/v2` contracts side by side.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `Revisions` stage and swap non-breaking edits transparently on the active URL, while `Versions` expose separate consumer-visible `/v1` and `/v2` contracts side by side.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `Revisions` stage and swap non-breaking edits transparently on the active URL, while `Versions` expose separate consumer-visible `/v1` and `/v2` contracts side by side.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `Revisions` stage and swap non-breaking edits transparently on the active URL, while `Versions` expose separate consumer-visible `/v1` and `/v2` contracts side by side.

### Question 69 — B

Answer: Use `<mock-response status-code="200" content-type="application/json" />` during frontend parallel development, or `<rewrite-uri template="/internal/v2/orders/{orderId}" />` with `<set-backend-service base-url="..." />` in `<inbound>`. `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI samples during UI work, while `<rewrite-uri>` + `<set-backend-service>` remap clean public URLs onto internal routes. `<mock-response>` short-circuits backend forwarding using OpenAPI example payloads, while `<rewrite-uri>` maps public clean paths onto legacy internal routes. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI samples during UI work, while `<rewrite-uri>` + `<set-backend-service>` remap clean public URLs onto internal routes.
- **B:** Correct. `<mock-response>` short-circuits backend forwarding using OpenAPI example payloads, while `<rewrite-uri>` maps public clean paths onto legacy internal routes. In this scenario: `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI samples during UI work, while `<rewrite-uri>` + `<set-backend-service>` remap clean public URLs onto internal routes.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI samples during UI work, while `<rewrite-uri>` + `<set-backend-service>` remap clean public URLs onto internal routes.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI samples during UI work, while `<rewrite-uri>` + `<set-backend-service>` remap clean public URLs onto internal routes.

### Question 70 — A

Answer: Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation. `AuthorizationLevel.Function` enforces function-key or host-key validation (`x-functions-key` / `?code=`), matching APIM's Named Value backend binding. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. In this scenario: `AuthorizationLevel.Function` enforces function-key or host-key validation (`x-functions-key` / `?code=`), matching APIM's Named Value backend binding.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `AuthorizationLevel.Function` enforces function-key or host-key validation (`x-functions-key` / `?code=`), matching APIM's Named Value backend binding.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `AuthorizationLevel.Function` enforces function-key or host-key validation (`x-functions-key` / `?code=`), matching APIM's Named Value backend binding.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `AuthorizationLevel.Function` enforces function-key or host-key validation (`x-functions-key` / `?code=`), matching APIM's Named Value backend binding.

### Question 71 — D

Answer: Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers. Enforcing Product Subscription Keys together with `context.Request.Certificate.Thumbprint` verification and `<validate-jwt>` inside `<inbound>` validates all three credentials at the gateway edge. Combining gateway `<validate-jwt>` pre-authentication with subscription scoping and client-certificate thumbprint checks blocks invalid traffic before hitting backends. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Enforcing Product Subscription Keys together with `context.Request.Certificate.Thumbprint` verification and `<validate-jwt>` inside `<inbound>` validates all three credentials at the gateway edge.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Enforcing Product Subscription Keys together with `context.Request.Certificate.Thumbprint` verification and `<validate-jwt>` inside `<inbound>` validates all three credentials at the gateway edge.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Enforcing Product Subscription Keys together with `context.Request.Certificate.Thumbprint` verification and `<validate-jwt>` inside `<inbound>` validates all three credentials at the gateway edge.
- **D:** Correct. Combining gateway `<validate-jwt>` pre-authentication with subscription scoping and client-certificate thumbprint checks blocks invalid traffic before hitting backends. In this scenario: Enforcing Product Subscription Keys together with `context.Request.Certificate.Thumbprint` verification and `<validate-jwt>` inside `<inbound>` validates all three credentials at the gateway edge.

### Question 72 — B, C

Answers: Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers; Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`. Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` + `<validate-jwt>` secures inbound partner calls, while `<authentication-managed-identity>` authenticates APIM to backend services. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` + `<validate-jwt>` secures inbound partner calls, while `<authentication-managed-identity>` authenticates APIM to backend services.
- **B:** Correct. Combining gateway `<validate-jwt>` pre-authentication with subscription scoping and client-certificate thumbprint checks blocks invalid traffic before hitting backends. In this scenario: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` + `<validate-jwt>` secures inbound partner calls, while `<authentication-managed-identity>` authenticates APIM to backend services.
- **C:** Correct. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. In this scenario: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` + `<validate-jwt>` secures inbound partner calls, while `<authentication-managed-identity>` authenticates APIM to backend services.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` + `<validate-jwt>` secures inbound partner calls, while `<authentication-managed-identity>` authenticates APIM to backend services.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Combining Product Subscription Keys + `context.Request.Certificate.Thumbprint` + `<validate-jwt>` secures inbound partner calls, while `<authentication-managed-identity>` authenticates APIM to backend services.

### Question 73 — D

Answer: Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`. `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates caller JWTs at the APIM edge. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates caller JWTs at the APIM edge.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates caller JWTs at the APIM edge.
- **C:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates caller JWTs at the APIM edge.
- **D:** Correct. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. In this scenario: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` validates caller JWTs at the APIM edge.

### Question 74 — B, E, F

Answers: Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`; Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`; Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`. `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three.
- **B:** Correct. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three.
- **E:** Correct. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three.
- **F:** Correct. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` deliver all three.

### Question 75 — D

Answer: Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`. Retaining `<base />` inside `<inbound>` alongside `<rate-limit-by-key>` (`429`) and `<quota-by-key>` (`403`) keyed on `context.Subscription?.Id` enforces both limits cleanly. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Retaining `<base />` inside `<inbound>` alongside `<rate-limit-by-key>` (`429`) and `<quota-by-key>` (`403`) keyed on `context.Subscription?.Id` enforces both limits cleanly.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Retaining `<base />` inside `<inbound>` alongside `<rate-limit-by-key>` (`429`) and `<quota-by-key>` (`403`) keyed on `context.Subscription?.Id` enforces both limits cleanly.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Retaining `<base />` inside `<inbound>` alongside `<rate-limit-by-key>` (`429`) and `<quota-by-key>` (`403`) keyed on `context.Subscription?.Id` enforces both limits cleanly.
- **D:** Correct. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! In this scenario: Retaining `<base />` inside `<inbound>` alongside `<rate-limit-by-key>` (`429`) and `<quota-by-key>` (`403`) keyed on `context.Subscription?.Id` enforces both limits cleanly.

### Question 76 — C

Answer: Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`. Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` isolates cached entries per language header. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` isolates cached entries per language header.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` isolates cached entries per language header.
- **C:** Correct. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. In this scenario: Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` isolates cached entries per language header.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Pairing `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>` isolates cached entries per language header.

### Question 77 — B

Answer: Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`. Wrapping `<forward-request />` inside `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` in `<backend>` masks transient 5xx blips, and `<set-header exists-action="delete" />` in `<outbound>` strips internal headers. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Wrapping `<forward-request />` inside `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` in `<backend>` masks transient 5xx blips, and `<set-header exists-action="delete" />` in `<outbound>` strips internal headers.
- **B:** Correct. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. In this scenario: Wrapping `<forward-request />` inside `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` in `<backend>` masks transient 5xx blips, and `<set-header exists-action="delete" />` in `<outbound>` strips internal headers.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Wrapping `<forward-request />` inside `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` in `<backend>` masks transient 5xx blips, and `<set-header exists-action="delete" />` in `<outbound>` strips internal headers.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Wrapping `<forward-request />` inside `<retry condition="@(context.Response.StatusCode >= 500)" count="3" ...>` in `<backend>` masks transient 5xx blips, and `<set-header exists-action="delete" />` in `<outbound>` strips internal headers.

### Question 78 — A

Answer: Deploy the HTTPS webhook endpoint accepting POST requests → create the Event Grid subscription pointing to the endpoint → inspect incoming SubscriptionValidationEvent and read validationCode → return HTTP 200 JSON containing validationResponse (or invoke validationUrl). Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, reading `SubscriptionValidationEvent.validationCode`, and echoing HTTP 200 `{"validationResponse": ...}` activates delivery. Event Grid dispatches a SubscriptionValidationEvent during subscription creation and activates delivery only after the endpoint echoes validationResponse (or completes validationUrl). Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Event Grid dispatches a SubscriptionValidationEvent during subscription creation and activates delivery only after the endpoint echoes validationResponse (or completes validationUrl). In this scenario: Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, reading `SubscriptionValidationEvent.validationCode`, and echoing HTTP 200 `{"validationResponse": ...}` activates delivery.
- **B:** Incorrect for this requirement. The validation code is unique per subscription handshake and cannot be echoed before Event Grid sends the SubscriptionValidationEvent. Why the keyed choice wins: Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, reading `SubscriptionValidationEvent.validationCode`, and echoing HTTP 200 `{"validationResponse": ...}` activates delivery.
- **C:** Incorrect for this requirement. If the endpoint is not live and returning validationResponse during creation, webhook validation fails before subscription creation completes. Why the keyed choice wins: Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, reading `SubscriptionValidationEvent.validationCode`, and echoing HTTP 200 `{"validationResponse": ...}` activates delivery.
- **D:** Incorrect for this requirement. Event Grid requires HTTPS webhook endpoints and expects JSON `{"validationResponse": "..."}` in the response body (or GET on validationUrl). Why the keyed choice wins: Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, reading `SubscriptionValidationEvent.validationCode`, and echoing HTTP 200 `{"validationResponse": ...}` activates delivery.

### Question 79 — B, C

Answers: Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL; Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`. `CloudEvents v1.0` subscriptions with `subjectBeginsWith` filters + Blob dead-lettering route events durably, while returning `{"validationResponse": validationCode}` (or `WebHook-Allowed-Origin`) completes webhook validation. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `CloudEvents v1.0` subscriptions with `subjectBeginsWith` filters + Blob dead-lettering route events durably, while returning `{"validationResponse": validationCode}` (or `WebHook-Allowed-Origin`) completes webhook validation.
- **B:** Correct. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. In this scenario: `CloudEvents v1.0` subscriptions with `subjectBeginsWith` filters + Blob dead-lettering route events durably, while returning `{"validationResponse": validationCode}` (or `WebHook-Allowed-Origin`) completes webhook validation.
- **C:** Correct. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. In this scenario: `CloudEvents v1.0` subscriptions with `subjectBeginsWith` filters + Blob dead-lettering route events durably, while returning `{"validationResponse": validationCode}` (or `WebHook-Allowed-Origin`) completes webhook validation.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `CloudEvents v1.0` subscriptions with `subjectBeginsWith` filters + Blob dead-lettering route events durably, while returning `{"validationResponse": validationCode}` (or `WebHook-Allowed-Origin`) completes webhook validation.
- **E:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: `CloudEvents v1.0` subscriptions with `subjectBeginsWith` filters + Blob dead-lettering route events durably, while returning `{"validationResponse": validationCode}` (or `WebHook-Allowed-Origin`) completes webhook validation.

### Question 80 — A

Answer: Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`. Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` preflight) and returning HTTP 200 JSON `{"validationResponse": validationCode}` proves endpoint ownership. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. In this scenario: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` preflight) and returning HTTP 200 JSON `{"validationResponse": validationCode}` proves endpoint ownership.
- **B:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` preflight) and returning HTTP 200 JSON `{"validationResponse": validationCode}` proves endpoint ownership.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` preflight) and returning HTTP 200 JSON `{"validationResponse": validationCode}` proves endpoint ownership.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents `OPTIONS` preflight) and returning HTTP 200 JSON `{"validationResponse": validationCode}` proves endpoint ownership.

### Question 81 — C

Answer: Create the Event Hub, consumer group, and Blob checkpoint container → instantiate BlobContainerClient and EventProcessorClient → register ProcessEventAsync (calling UpdateCheckpointAsync) and ProcessErrorAsync → call StartProcessingAsync before StopProcessingAsync. Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition consumption. `EventProcessorClient` coordinates partition ownership and offset checkpoints in Blob Storage and requires both event and error handlers registered prior to `StartProcessingAsync`. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Sharing one consumer group and checkpoint prefix across distinct apps causes them to steal partitions from each other instead of each reading the full stream. Why the keyed choice wins: Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition consumption.
- **B:** Incorrect for this requirement. `EventProcessorClient` throws `InvalidOperationException` if started before registering both `ProcessEventAsync` and `ProcessErrorAsync`. Why the keyed choice wins: Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition consumption.
- **C:** Correct. `EventProcessorClient` coordinates partition ownership and offset checkpoints in Blob Storage and requires both event and error handlers registered prior to `StartProcessingAsync`. In this scenario: Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition consumption.
- **D:** Incorrect for this requirement. Producers publish events and never hold partition checkpoints; `EventProcessorClient` handles balanced consumer checkpointing. Why the keyed choice wins: Provisioning the Event Hub, dedicated consumer group, and Blob checkpoint container, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition consumption.

### Question 82 — D

Answer: Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2. Event Grid is a push router without replayable partition logs; Azure Event Hubs provides partitioned pull streams, isolated Consumer Groups per reader, and zero-code Event Hubs Capture to ADLS Gen2. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Event Grid is a push router without replayable partition logs; Azure Event Hubs provides partitioned pull streams, isolated Consumer Groups per reader, and zero-code Event Hubs Capture to ADLS Gen2.
- **B:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Event Grid is a push router without replayable partition logs; Azure Event Hubs provides partitioned pull streams, isolated Consumer Groups per reader, and zero-code Event Hubs Capture to ADLS Gen2.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Event Grid is a push router without replayable partition logs; Azure Event Hubs provides partitioned pull streams, isolated Consumer Groups per reader, and zero-code Event Hubs Capture to ADLS Gen2.
- **D:** Correct. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. In this scenario: Event Grid is a push router without replayable partition logs; Azure Event Hubs provides partitioned pull streams, isolated Consumer Groups per reader, and zero-code Event Hubs Capture to ADLS Gen2.

### Question 83 — B

Answer: Host `EventProcessorClient` backed by `BlobContainerClient` and call `await eventArgs.UpdateCheckpointAsync()` after idempotent batch persistence so partition leases resume cleanly after rebalancing. Invoking `await eventArgs.UpdateCheckpointAsync()` writes the processed sequence/offset into Blob Storage metadata so rebalanced workers resume cleanly. `EventProcessorClient` coordinates partition ownership via Azure Blob leases and records per-partition sequence/offset checkpoints in Blob metadata. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Invoking `await eventArgs.UpdateCheckpointAsync()` writes the processed sequence/offset into Blob Storage metadata so rebalanced workers resume cleanly.
- **B:** Correct. `EventProcessorClient` coordinates partition ownership via Azure Blob leases and records per-partition sequence/offset checkpoints in Blob metadata. In this scenario: Invoking `await eventArgs.UpdateCheckpointAsync()` writes the processed sequence/offset into Blob Storage metadata so rebalanced workers resume cleanly.
- **C:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Invoking `await eventArgs.UpdateCheckpointAsync()` writes the processed sequence/offset into Blob Storage metadata so rebalanced workers resume cleanly.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Invoking `await eventArgs.UpdateCheckpointAsync()` writes the processed sequence/offset into Blob Storage metadata so rebalanced workers resume cleanly.

### Question 84 — A, C

Answers: Use Azure Service Bus Topics with `SqlRuleFilter` / `CorrelationRuleFilter` (`CorrelationRuleFilter` preferred for high throughput) and `SqlRuleAction` header stamping, inspecting `$DeadLetterQueue` (`SubQueue.DeadLetter`) after `MaxDeliveryCount` expires; Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering. Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` provide fast header routing and poison isolation, while `RequiresDuplicateDetection = true` suppresses duplicate `MessageId` resends. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Service Bus discards duplicate `MessageId` resends inside the history window and locks all messages sharing a `SessionId` to one active session receiver at a time. In this scenario: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` provide fast header routing and poison isolation, while `RequiresDuplicateDetection = true` suppresses duplicate `MessageId` resends.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` provide fast header routing and poison isolation, while `RequiresDuplicateDetection = true` suppresses duplicate `MessageId` resends.
- **C:** Correct. `CorrelationRuleFilter` matches brokered/application properties in-memory far faster than SQL evaluation, while `MaxDeliveryCount` isolates poison messages in the sub-queue DLQ. In this scenario: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` provide fast header routing and poison isolation, while `RequiresDuplicateDetection = true` suppresses duplicate `MessageId` resends.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` provide fast header routing and poison isolation, while `RequiresDuplicateDetection = true` suppresses duplicate `MessageId` resends.
- **E:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` provide fast header routing and poison isolation, while `RequiresDuplicateDetection = true` suppresses duplicate `MessageId` resends.

### Question 85 — C

Answer: Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering. Enabling `RequiresSession = true` (keyed by gate `SessionId`) alongside `RequiresDuplicateDetection = true` enforces per-gate FIFO ordering and idempotent deduplication. Service Bus discards duplicate `MessageId` resends inside the history window and locks all messages sharing a `SessionId` to one active session receiver at a time. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Enabling `RequiresSession = true` (keyed by gate `SessionId`) alongside `RequiresDuplicateDetection = true` enforces per-gate FIFO ordering and idempotent deduplication.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Enabling `RequiresSession = true` (keyed by gate `SessionId`) alongside `RequiresDuplicateDetection = true` enforces per-gate FIFO ordering and idempotent deduplication.
- **C:** Correct. Service Bus discards duplicate `MessageId` resends inside the history window and locks all messages sharing a `SessionId` to one active session receiver at a time. In this scenario: Enabling `RequiresSession = true` (keyed by gate `SessionId`) alongside `RequiresDuplicateDetection = true` enforces per-gate FIFO ordering and idempotent deduplication.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling `RequiresSession = true` (keyed by gate `SessionId`) alongside `RequiresDuplicateDetection = true` enforces per-gate FIFO ordering and idempotent deduplication.

### Question 86 — C

Answer: Call `long seq = await sender.ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` and persist `seq` to call `CancelScheduledMessageAsync(seq)` if the user cancels early. `ScheduleMessageAsync` holds the message invisible until enqueue time and returns `seq` so `CancelScheduledMessageAsync(seq)` can abort it cleanly. Service Bus native scheduled messages stay invisible until `ScheduledEnqueueTime` and can be canceled cleanly via their broker sequence number. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `ScheduleMessageAsync` holds the message invisible until enqueue time and returns `seq` so `CancelScheduledMessageAsync(seq)` can abort it cleanly.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `ScheduleMessageAsync` holds the message invisible until enqueue time and returns `seq` so `CancelScheduledMessageAsync(seq)` can abort it cleanly.
- **C:** Correct. Service Bus native scheduled messages stay invisible until `ScheduledEnqueueTime` and can be canceled cleanly via their broker sequence number. In this scenario: `ScheduleMessageAsync` holds the message invisible until enqueue time and returns `seq` so `CancelScheduledMessageAsync(seq)` can abort it cleanly.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `ScheduleMessageAsync` holds the message invisible until enqueue time and returns `seq` so `CancelScheduledMessageAsync(seq)` can abort it cleanly.

### Question 87 — D

Answer: Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics. Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, far exceeding Service Bus's 80 GB entity limit. Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub. Local study-map skill 5.8 (Implement Queue Workflows with Azure Queue Storage SDK, Visibility Leases, PopReceipts, and Poison Handling), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, far exceeding Service Bus's 80 GB entity limit.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, far exceeding Service Bus's 80 GB entity limit.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, far exceeding Service Bus's 80 GB entity limit.
- **D:** Correct. Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub. In this scenario: Azure Queue Storage scales up to the 500 TiB storage account ceiling for <=64 KB messages, far exceeding Service Bus's 80 GB entity limit.

### Question 88 — C

Answer: Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`; calling `ReceiveMessagesAsync(visibilityTimeout)` (checking `DequeueCount` for poison items) supplies `MessageId` + `PopReceipt` for `UpdateMessageAsync` / `DeleteMessageAsync`. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. Local study-map skill 5.8 (Implement Queue Workflows with Azure Queue Storage SDK, Visibility Leases, PopReceipts, and Poison Handling), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`; calling `ReceiveMessagesAsync(visibilityTimeout)` (checking `DequeueCount` for poison items) supplies `MessageId` + `PopReceipt` for `UpdateMessageAsync` / `DeleteMessageAsync`.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`; calling `ReceiveMessagesAsync(visibilityTimeout)` (checking `DequeueCount` for poison items) supplies `MessageId` + `PopReceipt` for `UpdateMessageAsync` / `DeleteMessageAsync`.
- **C:** Correct. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. In this scenario: `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`; calling `ReceiveMessagesAsync(visibilityTimeout)` (checking `DequeueCount` for poison items) supplies `MessageId` + `PopReceipt` for `UpdateMessageAsync` / `DeleteMessageAsync`.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`; calling `ReceiveMessagesAsync(visibilityTimeout)` (checking `DequeueCount` for poison items) supplies `MessageId` + `PopReceipt` for `UpdateMessageAsync` / `DeleteMessageAsync`.

### Question 89 — B

Answer: Create the staging deployment slot on the Standard/Premium Web App → mark production-only connection strings and webhook settings as deployment slot settings → deploy and warm up the new build in staging → swap staging into production and verify health. Creating the `Staging` slot, marking matchmaking keys as slot-sticky first, deploying and canary-validating on `Staging`, and executing the slot swap promotes code with zero downtime. Slot-sticky settings must be pinned before swapping so staging never inherits live payment webhooks or overwrites production secrets during swap. Local study-map skill 1.10 (Configure App Service Deployment Slots, Slot-Sticky Settings, Warm-Up, and Traffic Routing), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Free and Basic App Service plans do not support deployment slots; Standard, Premium, or Isolated is required first. Why the keyed choice wins: Creating the `Staging` slot, marking matchmaking keys as slot-sticky first, deploying and canary-validating on `Staging`, and executing the slot swap promotes code with zero downtime.
- **B:** Correct. Slot-sticky settings must be pinned before swapping so staging never inherits live payment webhooks or overwrites production secrets during swap. In this scenario: Creating the `Staging` slot, marking matchmaking keys as slot-sticky first, deploying and canary-validating on `Staging`, and executing the slot swap promotes code with zero downtime.
- **C:** Incorrect for this requirement. Deploying directly to production bypasses zero-downtime validation and swapping an empty staging slot overwrites production. Why the keyed choice wins: Creating the `Staging` slot, marking matchmaking keys as slot-sticky first, deploying and canary-validating on `Staging`, and executing the slot swap promotes code with zero downtime.
- **D:** Incorrect for this requirement. You cannot swap a slot before creating and deploying to it, and marking settings sticky after the swap leaks staging values into production. Why the keyed choice wins: Creating the `Staging` slot, marking matchmaking keys as slot-sticky first, deploying and canary-validating on `Staging`, and executing the slot swap promotes code with zero downtime.

### Question 90 — A

Answer: Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`). A Blob Storage Lifecycle Management policy JSON scoped to `prefixMatch: ["replays/"]` with `tierToCold` (`14` days) and `tierToArchive` (`90` days) automates server-side tiering. Lifecycle management policies automate tier transitions and retention deletion server-side once per day without custom cron jobs. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Lifecycle management policies automate tier transitions and retention deletion server-side once per day without custom cron jobs. In this scenario: A Blob Storage Lifecycle Management policy JSON scoped to `prefixMatch: ["replays/"]` with `tierToCold` (`14` days) and `tierToArchive` (`90` days) automates server-side tiering.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: A Blob Storage Lifecycle Management policy JSON scoped to `prefixMatch: ["replays/"]` with `tierToCold` (`14` days) and `tierToArchive` (`90` days) automates server-side tiering.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: A Blob Storage Lifecycle Management policy JSON scoped to `prefixMatch: ["replays/"]` with `tierToCold` (`14` days) and `tierToArchive` (`90` days) automates server-side tiering.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: A Blob Storage Lifecycle Management policy JSON scoped to `prefixMatch: ["replays/"]` with `tierToCold` (`14` days) and `tierToArchive` (`90` days) automates server-side tiering.

### Question 91 — C

Answer: Verify the blob is currently in the Archive access tier → call SetAccessTier (or CopyBlob) targeting Hot or Cool with Standard or High rehydrate priority → poll ArchiveStatus until rehydration completes and tier updates → download the blob content. Confirming `Archive` status, calling `SetAccessTier` (or `CopyBlob`) to `Hot`/`Cool` with `High` rehydrate priority, polling `ArchiveStatus` until online, and downloading prevents `409 BlobArchived`. Archived blobs are offline and unreadable directly; changing tier or copying to Hot/Cool initiates asynchronous rehydration that must finish before download. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Leasing does not bring an offline Archive blob online; rehydration to Hot or Cool must complete before any read succeeds. Why the keyed choice wins: Confirming `Archive` status, calling `SetAccessTier` (or `CopyBlob`) to `Hot`/`Cool` with `High` rehydrate priority, polling `ArchiveStatus` until online, and downloading prevents `409 BlobArchived`.
- **B:** Incorrect for this requirement. Calling Download directly on an Archive-tier blob immediately throws HTTP 409 Conflict (`BlobArchived`). Why the keyed choice wins: Confirming `Archive` status, calling `SetAccessTier` (or `CopyBlob`) to `Hot`/`Cool` with `High` rehydrate priority, polling `ArchiveStatus` until online, and downloading prevents `409 BlobArchived`.
- **C:** Correct. Archived blobs are offline and unreadable directly; changing tier or copying to Hot/Cool initiates asynchronous rehydration that must finish before download. In this scenario: Confirming `Archive` status, calling `SetAccessTier` (or `CopyBlob`) to `Hot`/`Cool` with `High` rehydrate priority, polling `ArchiveStatus` until online, and downloading prevents `409 BlobArchived`.
- **D:** Incorrect for this requirement. User metadata does not trigger storage rehydration, and setting tier back to Archive keeps the blob offline. Why the keyed choice wins: Confirming `Archive` status, calling `SetAccessTier` (or `CopyBlob`) to `Hot`/`Cool` with `High` rehydrate priority, polling `ArchiveStatus` until online, and downloading prevents `409 BlobArchived`.

### Question 92 — A

Answer: Set `--revision-mode multiple` and apply `az containerapp ingress traffic set --revision-weight` to split live HTTP requests across named revisions. Setting `--revision-mode multiple` and configuring weighted ingress rules (`az containerapp ingress traffic set --revision-weight`) splits live HTTP requests across active revisions. Multiple-revision mode keeps more than one revision active simultaneously for weighted blue/green or canary traffic splitting. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Multiple-revision mode keeps more than one revision active simultaneously for weighted blue/green or canary traffic splitting. In this scenario: Setting `--revision-mode multiple` and configuring weighted ingress rules (`az containerapp ingress traffic set --revision-weight`) splits live HTTP requests across active revisions.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting `--revision-mode multiple` and configuring weighted ingress rules (`az containerapp ingress traffic set --revision-weight`) splits live HTTP requests across active revisions.
- **C:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Setting `--revision-mode multiple` and configuring weighted ingress rules (`az containerapp ingress traffic set --revision-weight`) splits live HTTP requests across active revisions.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `--revision-mode multiple` and configuring weighted ingress rules (`az containerapp ingress traffic set --revision-weight`) splits live HTTP requests across active revisions.

### Question 93 — A

Answer: Enable container `DefaultTimeToLive = -1` (or positive seconds) and set item `ttl = 600` so Cosmos DB purges expired items automatically using background RU capacity. Setting container `DefaultTimeToLive = -1` activates item-level `ttl` expiration using background RUs while retaining documents that omit `ttl` indefinitely. Container TTL must be non-null (`-1` or `>0`) for per-item `ttl` seconds to take effect; setting `DefaultTimeToLive = null` ignores item-level `ttl`. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Container TTL must be non-null (`-1` or `>0`) for per-item `ttl` seconds to take effect; setting `DefaultTimeToLive = null` ignores item-level `ttl`. In this scenario: Setting container `DefaultTimeToLive = -1` activates item-level `ttl` expiration using background RUs while retaining documents that omit `ttl` indefinitely.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` activates item-level `ttl` expiration using background RUs while retaining documents that omit `ttl` indefinitely.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` activates item-level `ttl` expiration using background RUs while retaining documents that omit `ttl` indefinitely.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` activates item-level `ttl` expiration using background RUs while retaining documents that omit `ttl` indefinitely.

### Question 94 — C

Answer: Pass `new ItemRequestOptions { IfMatchEtag = item.ETag }` on `ReplaceItemAsync` and catch `CosmosException` when `StatusCode == HttpStatusCode.PreconditionFailed` (412). Passing `new ItemRequestOptions { IfMatchEtag = seatDoc.ETag }` enforces optimistic concurrency so the second concurrent `ReplaceItemAsync` throws `CosmosException` (`412 PreconditionFailed`). Supplying `IfMatchEtag` enforces optimistic concurrency control so concurrent writers fail with HTTP 412 rather than silently overwriting updates. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Passing `new ItemRequestOptions { IfMatchEtag = seatDoc.ETag }` enforces optimistic concurrency so the second concurrent `ReplaceItemAsync` throws `CosmosException` (`412 PreconditionFailed`).
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Passing `new ItemRequestOptions { IfMatchEtag = seatDoc.ETag }` enforces optimistic concurrency so the second concurrent `ReplaceItemAsync` throws `CosmosException` (`412 PreconditionFailed`).
- **C:** Correct. Supplying `IfMatchEtag` enforces optimistic concurrency control so concurrent writers fail with HTTP 412 rather than silently overwriting updates. In this scenario: Passing `new ItemRequestOptions { IfMatchEtag = seatDoc.ETag }` enforces optimistic concurrency so the second concurrent `ReplaceItemAsync` throws `CosmosException` (`412 PreconditionFailed`).
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Passing `new ItemRequestOptions { IfMatchEtag = seatDoc.ETag }` enforces optimistic concurrency so the second concurrent `ReplaceItemAsync` throws `CosmosException` (`412 PreconditionFailed`).

### Question 95 — D

Answer: Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization. An Azure Event Grid Domain manages tenant-isolated domain topics under a single publish endpoint with granular per-topic Azure RBAC authorization. Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: An Azure Event Grid Domain manages tenant-isolated domain topics under a single publish endpoint with granular per-topic Azure RBAC authorization.
- **B:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: An Azure Event Grid Domain manages tenant-isolated domain topics under a single publish endpoint with granular per-topic Azure RBAC authorization.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: An Azure Event Grid Domain manages tenant-isolated domain topics under a single publish endpoint with granular per-topic Azure RBAC authorization.
- **D:** Correct. Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures. In this scenario: An Azure Event Grid Domain manages tenant-isolated domain topics under a single publish endpoint with granular per-topic Azure RBAC authorization.

### Question 96 — A

Answer: Use `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false`, calling `CompleteMessageAsync` after commit, `AbandonMessageAsync` for transient retries, and `DeadLetterMessageAsync` on unrecoverable schema errors. Running `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` (`AutoCompleteMessages = false`) with explicit `CompleteMessageAsync`, `AbandonMessageAsync`, and `DeadLetterMessageAsync` guarantees broker durability. `ReceiveAndDelete` loses messages if a worker crashes mid-processing; `PeekLock` retains broker durability until explicit settlement or lock expiry. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. `ReceiveAndDelete` loses messages if a worker crashes mid-processing; `PeekLock` retains broker durability until explicit settlement or lock expiry. In this scenario: Running `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` (`AutoCompleteMessages = false`) with explicit `CompleteMessageAsync`, `AbandonMessageAsync`, and `DeadLetterMessageAsync` guarantees broker durability.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Running `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` (`AutoCompleteMessages = false`) with explicit `CompleteMessageAsync`, `AbandonMessageAsync`, and `DeadLetterMessageAsync` guarantees broker durability.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Running `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` (`AutoCompleteMessages = false`) with explicit `CompleteMessageAsync`, `AbandonMessageAsync`, and `DeadLetterMessageAsync` guarantees broker durability.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Running `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` (`AutoCompleteMessages = false`) with explicit `CompleteMessageAsync`, `AbandonMessageAsync`, and `DeadLetterMessageAsync` guarantees broker durability.

### Question 97 — D

Answer: Create an Azure Monitor Metric Alert (Dynamic Thresholds or static p95 latency/5xx count) or Scheduled Query (KQL) Alert targeting an Action Group configured with webhook / Azure Function / email-SMS receivers. Creating an Azure Monitor Metric Alert or Scheduled Query (KQL) Alert targeting an Action Group configured with SMS and webhook receivers notifies grid ops automatically. Metric alerts offer sub-minute stateful evaluation on numeric signals, whereas Scheduled Query Rules run expressive KQL joins on log tables at configured intervals. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Creating an Azure Monitor Metric Alert or Scheduled Query (KQL) Alert targeting an Action Group configured with SMS and webhook receivers notifies grid ops automatically.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Creating an Azure Monitor Metric Alert or Scheduled Query (KQL) Alert targeting an Action Group configured with SMS and webhook receivers notifies grid ops automatically.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Creating an Azure Monitor Metric Alert or Scheduled Query (KQL) Alert targeting an Action Group configured with SMS and webhook receivers notifies grid ops automatically.
- **D:** Correct. Metric alerts offer sub-minute stateful evaluation on numeric signals, whereas Scheduled Query Rules run expressive KQL joins on log tables at configured intervals. In this scenario: Creating an Azure Monitor Metric Alert or Scheduled Query (KQL) Alert targeting an Action Group configured with SMS and webhook receivers notifies grid ops automatically.

### Question 98 — D

Answer: Enable Managed Identity with App Configuration Data Reader + Key Vault Secrets User → add Key Vault references and a sentinel key → wire AddAzureAppConfiguration with ConfigureKeyVault and ConfigureRefresh → invoke UseAzureAppConfiguration middleware. Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking refresh middleware enables atomic reload. RBAC on both stores is required because App Configuration stores only the URI pointer; `ConfigureRefresh` + middleware poll the sentinel key on incoming requests. Local study-map skill 3.5 (Manage Feature Flags, Labels, Sentinel Dynamic Refresh, and Key Vault References in Azure App Configuration), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. In ASP.NET Core, dynamic refresh is request-driven via `UseAzureAppConfiguration()` middleware (or manual `TryRefreshAsync`), not an automatic push without it. Why the keyed choice wins: Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking refresh middleware enables atomic reload.
- **B:** Incorrect for this requirement. Committing exported secret values defeats Key Vault reference rotation and violates secret hygiene. Why the keyed choice wins: Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking refresh middleware enables atomic reload.
- **C:** Incorrect for this requirement. Without Key Vault Secrets User on the vault itself, resolving a Key Vault reference throws 403 Forbidden at startup. Why the keyed choice wins: Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking refresh middleware enables atomic reload.
- **D:** Correct. RBAC on both stores is required because App Configuration stores only the URI pointer; `ConfigureRefresh` + middleware poll the sentinel key on incoming requests. In this scenario: Granting `App Configuration Data Reader` + `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, wiring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking refresh middleware enables atomic reload.

### Question 99 — A

Answer: Select `Developer` (non-SLA) or `Premium` / `Standard v2` for VNet integration, and deploy the containerized APIM Self-Hosted Gateway (`mcr.microsoft.com/azure-api-management/gateway`) for hybrid on-premises/multi-cloud local traffic routing. Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway on-premises keeps studio API traffic local while pulling config updates over outbound port 443. Self-hosted gateways require `Developer` or `Premium` tier and keep data-plane traffic local while pulling policy updates outbound over HTTPS/443 from Azure. Local study-map skill 5.1 (Provision Azure API Management Tiers, VNet Modes, and Self-Hosted Hybrid Gateways), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Self-hosted gateways require `Developer` or `Premium` tier and keep data-plane traffic local while pulling policy updates outbound over HTTPS/443 from Azure. In this scenario: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway on-premises keeps studio API traffic local while pulling config updates over outbound port 443.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway on-premises keeps studio API traffic local while pulling config updates over outbound port 443.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway on-premises keeps studio API traffic local while pulling config updates over outbound port 443.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway on-premises keeps studio API traffic local while pulling config updates over outbound port 443.

### Question 100 — D

Answer: Configure App Service / Functions application settings using `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` (omitting secret version) paired with `Key Vault Secrets User` on the app Managed Identity. Using versionless `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` app settings paired with `Key Vault Secrets User` on Managed Identity resolves secrets at the platform layer. Versionless Key Vault references automatically pull rotated secret versions within 24 hours (or immediately on config change / manual sync) with zero SDK boilerplate. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Using versionless `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` app settings paired with `Key Vault Secrets User` on Managed Identity resolves secrets at the platform layer.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Using versionless `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` app settings paired with `Key Vault Secrets User` on Managed Identity resolves secrets at the platform layer.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Using versionless `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` app settings paired with `Key Vault Secrets User` on Managed Identity resolves secrets at the platform layer.
- **D:** Correct. Versionless Key Vault references automatically pull rotated secret versions within 24 hours (or immediately on config change / manual sync) with zero SDK boilerplate. In this scenario: Using versionless `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` app settings paired with `Key Vault Secrets User` on Managed Identity resolves secrets at the platform layer.
