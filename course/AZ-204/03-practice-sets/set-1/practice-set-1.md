# Microsoft Exam AZ-204: Developing Solutions for Microsoft Azure — Full-Length Mock Exam 1

Exam AZ-204 (Omnichannel Retail, Flash-Sale Checkout, and Loyalty APIs) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Credential Lifecycle Notice:** Microsoft retired Exam AZ-204 (`Microsoft Certified: Azure Developer Associate`) on **July 31, 2026** and succeeded it with **Exam AI-200 (`Azure AI Cloud Developer Associate`)**. This practice bank preserves the final official January 14, 2026 AZ-204 skills-measured baseline for archival certification prep, enterprise Azure developer benchmarking, and core compute/storage/security/monitoring/integration mastery.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` SDK/CLI/XML/JSON/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area code dropdowns, split-pane tabbed case exhibits, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn documentation — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. Vespera's platform team is containerizing a .NET 8 catalog microservice (`FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build ... ____ `) and wants smaller pull sizes, non-root runtime execution, and zero local `bin/` or `.env` leakage in the build context. Which two practices achieve these goals? Select two.

Domain: Develop Azure compute solutions

- A. Use a multi-stage Dockerfile building in `mcr.microsoft.com/dotnet/sdk:8.0` and copying published output into `mcr.microsoft.com/dotnet/aspnet:8.0` with a non-root `USER app`
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Add `bin/`, `obj/`, `.git/`, and local `.env` files to `.dockerignore` before running `docker build` or `az acr build`
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- E. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 2. A developer upgrades a retail pricing API container from .NET 6 to official `mcr.microsoft.com/dotnet/aspnet:8.0` non-root images and completes the Dockerfile stage with ` ____ ` so Container Apps ingress connects cleanly without root port privileges. Which configuration belongs in the blank?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Set `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` inside the final `.NET 8` runtime stage and match `targetPort: 8080` on Container Apps ingress

### 3. A build agent in a locked-down retail VPC has Azure CLI installed without a local Docker daemon and must compile and push `catalog-api` from source (`az acr ____ `). Which command completes the workflow?

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Run `az acr build --registry <acrName> --image app:{{.Run.ID}} .` to build and push the container image remotely using ACR Tasks without a local Docker daemon

### 4. Nightly flash-sale builds create hundreds of tagged and untagged manifests in ACR, pushing storage consumption near quota. Proposed solution: Enable `--admin-enabled true` on Basic ACR so developers manually delete digests weekly. Which replacement automates cleanup safely?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Upgrade Azure Container Registry to the `Premium` SKU and configure geo-replication into each target compute region
- C. Schedule an ACR Task executing `acr purge --filter "app:.*" --ago 30d --untagged` to clean stale untagged manifests and old tags automatically
- D. Execute `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine`

### 5. Every midnight an Azure Container Instances group reconciles gift-card balances in four minutes, exits with status code `0`, and unexpectedly accrues 24-hour vCPU charges because it keeps restarting. How should the container group be fixed?

Domain: Develop Azure compute solutions

- A. Set `--restart-policy OnFailure` (or `Never`) on the Azure Container Instances container group so batch containers stop billing vCPU/memory seconds once exit code 0 completes
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 6. A storefront tax-calculation container needs a local Envoy mTLS proxy reachable over `127.0.0.1:9001` and a shared scratch directory on Linux ACI without exposing the raw app port publicly. Which ACI design works?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Deploy the application container and Envoy/logging sidecar inside one multi-container ACI group sharing `localhost` network namespace and an `emptyDir` / Azure Files volume
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 7. A merchandising team is deploying a promotion engine to Azure Container Apps and must pull private images from Azure Container Registry with zero shared registry passwords. Which ordered sequence configures passwordless pulls?

Domain: Develop Azure compute solutions

- A. Create the Container Apps environment → create the container app → enable ACR admin passwords → revoke AcrPull
- B. Create the container app referencing the registry → build and push the image with az acr build → create the Container Apps environment → grant AcrPull
- C. Build and push the image to ACR with az acr build → create a user-assigned managed identity and grant AcrPull on the registry → create the Container Apps environment → create the container app referencing the identity and registry server
- D. Grant AcrPull on the registry → create the container app → create the user-assigned identity → run az acr build

### 8. An e-commerce checkout team migrating microservices to Azure Container Apps requires 90/10 canary HTTP splits, scale-to-zero background workers driven by Service Bus queue depth using Managed Identity, and Key Vault-backed secrets without ARM plaintext values. Which three Container Apps features satisfy these requirements? Select three.

Domain: Develop Azure compute solutions

- A. Set `--revision-mode multiple` and apply `az containerapp ingress traffic set --revision-weight` to split live HTTP requests across named revisions
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Configure a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0` and Managed Identity (`identity` property) so replicas scale to zero when idle and wake on queue depth
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Define a Container App secret using `keyVaultUrl` plus `identity` (managed identity resource ID or `system`) and map container environment variables via `secretRef`
- F. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision

### 9. A retail payment-tokenization microservice must run in a Container Apps environment whose Envoy load balancer accepts traffic exclusively from private VNet subnets (` ____ `). Which Azure CLI command provisions the environment?

Domain: Develop Azure compute solutions

- A. Execute `az containerapp env create --name <envName> --resource-group <rg> --infrastructure-subnet-resource-id <subnetId> --internal-only`
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 10. After every flash-sale window closes, a finite Python container must generate 20 parallel warehouse pick-list shards and terminate cleanly with zero open HTTP listener ports. Which Container Apps resource fits this workload?

Domain: Develop Azure compute solutions

- A. Deploy an Azure Container Apps Job (`triggerType: Event` or `Schedule`) with `replicaCompletionCount` and `parallelism` instead of an always-listening HTTP container app
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 11. Proposed solution: Provision a `Basic (B1)` Linux App Service plan to host a seasonal storefront requiring two staging deployment slots and CPU metric autoscale between 2 and 8 instances. Why does the proposed solution fail, and which plan tier resolves it?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Provision at least a `Standard` (`S1+`) or `Premium v3` (`P1v3+`) App Service plan to unlock deployment slots, custom domain SNI SSL, and metric/schedule autoscaling
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 12. PCI-DSS auditors require a retail checkout App Service web app to redirect HTTP port 80 requests automatically, reject TLS 1.0/1.1 handshakes, and validate supplier X.509 client certificates at the platform edge. Which configuration meets all three controls?

Domain: Develop Azure compute solutions

- A. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- B. Enable `httpsOnly: true`, set `minTlsVersion: "1.2"` (or `"1.3"`), and configure `clientCertEnabled` when mutual TLS client certificates are required
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 13. Storefront engineers enabled App Service Application Logging (Filesystem) on Friday afternoon, and by Monday morning verbose logs from a Sunday night checkout outage had stopped capturing. What change retains application and HTTP logs durably for 60 days?

Domain: Develop Azure compute solutions

- A. Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`
- B. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances

### 14. While debugging a staging coupon API on App Service from a terminal, a developer wants to enable verbose filesystem output temporarily and attach a live console stream (` ____ `). Which CLI command sequence accomplishes this?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 15. During peak shopping traffic, deploying updated DLLs to a Windows App Service web app occasionally fails with `ERROR_FILE_IN_USE` locks and serves mixed old/new assemblies for several seconds. Which deployment setting makes package rollouts atomic?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- C. Set `WEBSITE_RUN_FROM_PACKAGE=1` and deploy with `az webapp deploy --type zip` so the app mounts the read-only ZIP package directly with atomic cold-start replacement
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 16. A custom containerized Node.js storefront on App Service for Linux currently authenticates to ACR using `DOCKER_REGISTRY_SERVER_PASSWORD`. How should the developer switch to credential-free image pulls?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Disable the ACR admin account and assign the built-in `AcrPull` role on the registry to the compute resource managed identity
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 17. A single-page storefront hosted at `https://shop.vespera.example` sends credentialed `fetch` requests to `https://api.vespera.example` on App Service, which also connects to a slot-specific Azure SQL database. Which two configurations should the team apply? Select two.

Domain: Develop Azure compute solutions

- A. Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Configure App Service `CORS` with explicit origin URLs (and `supportCredentials` only without wildcard `*`) so App Service handles preflight `OPTIONS` requests
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision

### 18. An ASP.NET Core storefront on App Service calls `Configuration.GetConnectionString("LedgerDb")` and must keep staging and production SQL databases isolated across slot swaps (`az webapp config connection-string set ____ `). Which CLI command completes the setup?

Domain: Develop Azure compute solutions

- A. Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`
- B. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 19. During flash sales, an App Service plan scales out when CPU exceeds 70% and scales in when CPU falls below 68% with a 1-minute cooldown, causing instances to add and terminate every two minutes. How should the autoscale profile be corrected?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Pair every scale-out metric rule (e.g., CPU > 75% for 10 min) with a conservative scale-in rule (e.g., CPU < 35%) and an explicit `coolDown` window plus safe default/max instance bounds
- C. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 20. When App Service scales out or swaps slots for a catalog API that preloads a 400 MB product taxonomy cache on startup, the first 30 seconds of requests hit cold instances and time out. Which configuration warms instances before live traffic arrives?

Domain: Develop Azure compute solutions

- A. Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision

### 21. A release engineer is rolling out v2.4 of a gift-registry web app on App Service Standard S2 and needs zero-downtime validation with environment-pinned settings before shifting customer traffic. Which sequence executes the release properly?

Domain: Develop Azure compute solutions

- A. Create the staging deployment slot on the Standard/Premium Web App → mark production-only connection strings and webhook settings as deployment slot settings → deploy and warm up the new build in staging → swap staging into production and verify health
- B. Create the staging slot on a Free F1 plan → deploy the build → swap slots → mark settings sticky
- C. Deploy directly to production → create the staging slot → swap staging into production → mark settings as slot settings
- D. Swap staging into production → create the staging slot → deploy the build → mark settings as deployment slot settings

### 22. Proposed solution: Host a C# coupon-settlement Function App on classic Linux Consumption with `functionTimeout` set to `00:25:00` so it can reach a private-endpoint SQL server inside a VNet and run 20-minute settlements with zero cold starts. Why does this fail, and which hosting choice meets all requirements?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Host the Function App on `Flex Consumption` or `Elastic Premium (EP1+)` when VNet integration, longer execution timeouts beyond 10 minutes, or pre-warmed/always-ready instances are required

### 23. A retail webhook Function App wants a 10-minute timeout ceiling and wants Application Insights adaptive sampling to never discard `Request` or `Exception` telemetry (`host.json`: ` ____ `). Which `host.json` configuration belongs in the file?

Domain: Develop Azure compute solutions

- A. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- B. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Configure `"functionTimeout": "00:10:00"` and `"logging": { "applicationInsights": { "samplingSettings": { "isEnabled": true, "excludedTypes": "Request;Exception" } } }` inside `host.json`

### 24. A C# Function App reacts to new order documents in Cosmos DB and also runs an Event Hub inventory aggregator that must retry transient downstream timeouts five times with exponential backoff before advancing checkpoints. Which two attributes should the developer apply? Select two.

Domain: Develop Azure compute solutions

- A. Apply `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` (or `[FixedDelayRetry]`) on the `[EventHubTrigger]` / `[TimerTrigger]` function
- B. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- C. Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 25. A store-replenishment `[TimerTrigger(" ____ ")]` Function must fire every 15 minutes from 09:00 through 17:45 UTC on Monday through Friday. Which schedule expression completes the attribute?

Domain: Develop Azure compute solutions

- A. Specify a six-field NCRONTAB expression `{second} {minute} {hour} {day} {month} {day-of-week}` such as `"0 */15 9-17 * * 1-5"` on `[TimerTrigger]`
- B. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 26. Suppliers upload 50,000 product images per hour into a Blob container, and default log-polling `[BlobTrigger]` Functions lag by several minutes. How should the trigger be reconfigured for near-instant invocation?

Domain: Develop Azure compute solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Configure `[BlobTrigger(..., Source = BlobTriggerSource.EventGrid)]` with an Event Grid system topic subscription instead of default container-log polling
- C. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 27. A shopping-cart service using Cosmos DB for NoSQL needs socket-safe client reuse, atomic creation of a cart header plus three line items sharing `/cartId`, and protection against lost updates when two browser tabs edit the same cart item concurrently. Which three SDK practices should the team combine? Select three.

Domain: Develop for Azure storage

- A. Use `container.CreateTransactionalBatch(new PartitionKey(pkValue))` to group multiple create/replace/upsert/delete operations atomically within the same logical partition
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Register `CosmosClient` as a process-wide singleton in dependency injection and choose a high-cardinality `PartitionKey` path (or up to 3-level `Hierarchical` subpartition paths) that distributes RU/s evenly
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- F. Pass `new ItemRequestOptions { IfMatchEtag = item.ETag }` on `ReplaceItemAsync` and catch `CosmosException` when `StatusCode == HttpStatusCode.PreconditionFailed` (412)

### 28. When a payment gateway webhook increments `/retryCount` by `1` and sets `/lastStatus` to `"Queued"` on a 180 KB Cosmos DB order document (`await container. ____ `), the team wants to avoid reading and resending the entire document. Which SDK call completes the code?

Domain: Develop for Azure storage

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `await container.PatchItemAsync<Order>(id, new PartitionKey(pk), new[] { PatchOperation.Increment("/retryCount", 1), PatchOperation.Set("/lastStatus", "Queued") })`
- D. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction

### 29. A storefront query `SELECT c.id, c.total FROM c WHERE c.storeId = @s ORDER BY c.category ASC, c.createdUtc DESC` throws a `400 BadRequest` indexing error in Cosmos DB for NoSQL. What must the developer add to the container indexing policy?

Domain: Develop for Azure storage

- A. Add a `compositeIndexes` array matching the exact property sequence and sort directions (`ascending` / `descending`) in the container indexing policy JSON
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Configure `"indexingMode": "consistent"` with `"includedPaths": [{"path": "/customerId/?"}, {"path": "/createdUtc/?"}]` and `"excludedPaths": [{"path": "/*"}]`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 30. After adding a sneaker to their cart, a shopper refreshes the page through a stateless load-balanced API tier and must immediately see their own write while paying half the read RU cost of `Strong` consistency. Which Cosmos DB configuration achieves this?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency
- D. Use `Session` consistency (the default) and propagate `x-ms-session-token` (`RequestOptions.SessionToken`) across client/middle-tier hops to guarantee monotonic read-your-own-writes at half the read RU cost of `Strong`

### 31. Global inventory dashboards read from three Cosmos DB regions and require reads to lag behind the primary write region by no more than 500 item versions (`K = 500`) or 10 seconds (`T = 10s`) in exact write order. Which consistency level fits?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency

### 32. A merchandising analytics worker in C# must stream every cart update from Cosmos DB using the .NET v3 Change Feed Processor library. Which sequence initializes and starts the processor properly?

Domain: Develop for Azure storage

- A. Call StartAsync on the processor → call GetChangeFeedProcessorBuilder<T> → create the lease container → attach WithInstanceName
- B. Create only the monitored container → call Build and StartAsync → attach WithLeaseContainer → define the handler delegate
- C. Create the monitored container and a dedicated lease container → call GetChangeFeedProcessorBuilder<T> with processorName and delegate → attach WithInstanceName and WithLeaseContainer → call Build and StartAsync on the processor
- D. Attach WithLeaseContainer pointing to the monitored container without /id partition → call StartAsync → call GetChangeFeedProcessorBuilder<T> → call Build

### 33. Two independent microservices — fraud scoring and search indexing — must each consume every Cosmos DB product mutation independently, and the search indexer must also remove documents when items are deleted. Which two Change Feed designs meet both needs? Select two.

Domain: Develop for Azure storage

- A. Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Use Change Feed `AllVersionsAndDeletes` mode (or soft-delete flag items with short TTL in `LatestVersion` mode) because default `LatestVersion` change feed omits hard-deleted items
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 34. Flash-sale promo-lock documents in Cosmos DB set `"ttl": 300`, yet expired documents never disappear because the container was created with `DefaultTimeToLive = null`. How should the container be configured so per-item `ttl` values take effect without expiring items that omit `ttl`?

Domain: Develop for Azure storage

- A. Enable container `DefaultTimeToLive = -1` (or positive seconds) and set item `ttl = 600` so Cosmos DB purges expired items automatically using background RU capacity
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 35. A receipt-export worker uploads PDF blobs and needs to set `Content-Type: application/pdf` plus custom `order_id` metadata (`x-ms-meta-order_id`) using `Azure.Storage.Blobs` v12 (` ____ `). Which SDK methods apply both correctly?

Domain: Develop for Azure storage

- A. Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`)
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 36. Proposed solution: Store `region=emea` and `taxYear=2026` inside Blob `Metadata` and query across 12 million invoice blobs without listing containers. Why does this fail, and which Blob feature enables direct server-side queries?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`)
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Attach searchable key-value `Tags` (`SetTagsAsync` / `BlobUploadOptions.Tags`) and query across containers with `FindBlobsByTagsAsync("@container = 'docs' AND status = 'pending'")`

### 37. Catalog editors frequently overwrite price-sheet JSON blobs by mistake, and the platform team wants every `UploadAsync` overwrite or delete to preserve an automatic recoverable `VersionId` without modifying editor upload code. What should they enable?

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `await blobClient.CreateSnapshotAsync()` for explicit point-in-time read-only checkpoints or enable account-level Blob Versioning so every `UploadAsync` overwrite retains an immutable `VersionId`

### 38. Fourscaled settlement pods periodically update the same `daily-reconciliation.json` blob and must guarantee only one pod writes during a 45-second window while others fail fast with HTTP 412. How should the C# worker coordinate access?

Domain: Develop for Azure storage

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Use `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` (15–60 seconds or `-1` infinite) and pass `LeaseId` inside `BlobRequestConditions` on subsequent writes/deletes
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 39. A seasonal backup tool needs to copy 4 TB of lookbook videos from a staging storage account to a DR storage account without downloading and re-uploading bytes through the runner container. Which SDK method performs this transfer?

Domain: Develop for Azure storage

- A. Invoke `BlobClient.StartCopyFromUriAsync(sourceSasUri)` to trigger asynchronous server-side blob copy and inspect `CopyStatus` without streaming bytes through the client VM
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained

### 40. A fulfillment service generates a 15-minute read-only HTTPS link scoped strictly to single blob `exports/manifest.csv` (`new BlobSasBuilder { ____ }`). Which `BlobSasBuilder` configuration completes the code?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 41. Retail tax auditors require signed fiscal-year archives to remain unmodifiable and undeletable even by subscription owners for seven years, and rare audit requests on `Archive`-tier files under 5 GB must restore in under one hour. Which two Blob Storage capabilities address both needs? Select two.

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage
- D. Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob)
- E. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 42. A merchandising analyst requests a 2024 clearance-sale Parquet file currently stored in the `Archive` access tier. Which sequence of SDK operations retrieves the file without throwing HTTP 409 `BlobArchived`?

Domain: Develop for Azure storage

- A. Download the archived blob stream directly → call SetAccessTier to Hot → poll ArchiveStatus → verify the Archive tier
- B. Verify the blob is currently in the Archive access tier → call SetAccessTier (or CopyBlob) targeting Hot or Cool with Standard or High rehydrate priority → poll ArchiveStatus until rehydration completes and tier updates → download the blob content
- C. Set blob metadata `tier=Hot` → download the blob immediately → call SetAccessTier to Archive → poll ArchiveStatus
- D. Acquire an infinite blob lease → delete the blob snapshot → download the archived blob directly → call SetAccessTier

### 43. A cross-platform desktop POS app built with .NET MAUI authenticates store associates against Microsoft Entra ID and calls a loyalty API repeatedly throughout an eight-hour shift. Which two MSAL patterns must the developer implement? Select two.

Domain: Implement Azure security

- A. Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`
- B. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps

### 44. A nightly headless inventory-sync daemon runs with no interactive user and authenticates with an X.509 client certificate to call an internal pricing API (`await app. ____ `). Which MSAL setup and scope format are required?

Domain: Implement Azure security

- A. Use `ConfidentialClientApplicationBuilder` authenticated with a client certificate (or workload identity assertion) calling `AcquireTokenForClient(new[] { "api://.../.default" })` for headless background daemons
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 45. A store manager signed into a React portal calls Vespera's middle-tier ASP.NET Core Shift API, which must read that manager's Microsoft 365 calendar via Microsoft Graph using delegated permissions. Which sequence implements the token exchange?

Domain: Implement Azure security

- A. Use PublicClientApplication without client credentials → call AcquireTokenForClient → pass UserAssertion → register delegated permissions
- B. Call Microsoft Graph anonymously → call AcquireTokenOnBehalfOf → validate the incoming token → expose the API scope
- C. Register the middle-tier API scope and delegated Graph permissions in Entra ID → validate the incoming user token → call ConfidentialClientApplication.AcquireTokenOnBehalfOf(UserAssertion) → invoke Microsoft Graph with the exchanged token
- D. Forward the front-end SPA access token directly to Microsoft Graph → validate the incoming token → register the API scope → call AcquireTokenOnBehalfOf

### 46. Mobile checkout clients calling an App Service REST API protected by built-in Microsoft Entra Authentication (`Easy Auth`) receive HTML `302 Found` redirects to `login.microsoftonline.com` instead of JSON-friendly auth errors when tokens expire. Which Easy Auth setting fixes this?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)

### 47. A B2B supplier-onboarding web app must allow procurement users from any external work/school Microsoft Entra tenant to sign in while blocking personal consumer Microsoft accounts and unsubscribed `tid` values. How should authentication be configured?

Domain: Implement Azure security

- A. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation

### 48. Proposed solution: Mint a 90-day Service SAS with inline `sv`, `st`, `se`, and `sp` parameters signed by `accountKey1`, and plan to revoke a single leaked partner token without affecting 40 other services using `accountKey1`. Why does this fail, and what fixes it?

Domain: Implement Azure security

- A. Bind a Service SAS to a container/queue/table Stored Access Policy (`SignedIdentifier`, omitting inline start/expiry/permissions) so compromised tokens can be revoked instantly by modifying or deleting the policy
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 49. Security policy disables Shared Key authorization (`allowSharedKeyAccess: false`) on all retail storage accounts, yet a shipping service still needs to issue 10-minute SAS URLs for packing-slip blobs. Which SAS type continues to work?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Mint a short-lived HTTPS-only (`SasProtocol.HttpsOnly`) User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` instead of Account or Service SAS signed with storage account keys
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 50. An associate directory sync tool reads `id`, `displayName`, and `mail` across 35,000 Entra users and fetches profile photos for 18 store leads per dashboard load without tripping Graph HTTP 429 limits. Which two Microsoft Graph SDK techniques should the developer combine? Select two.

Domain: Implement Azure security

- A. Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`

### 51. Using Microsoft Graph .NET SDK v5, a developer needs only active user accounts (`accountEnabled eq true`) and wants only `id`, `displayName`, and `mail` serialized over the wire (`await graphClient.Users.GetAsync( ____ )`). Which lambda completes the request?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `await graphClient.Users.GetAsync(rc => { rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }; rc.QueryParameters.Filter = "accountEnabled eq true"; })`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 52. Inside an ASP.NET Core controller that received an Entra user bearer token `incomingBearerToken`, which MSAL C# call exchanges that token for a downstream `Calendars.Read` Microsoft Graph token (` ____ `)?

Domain: Implement Azure security

- A. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Call `await confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` inside the middle-tier API
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 53. Vespera's checkout API reads Key Vault secret references stored inside Azure App Configuration (`options.Connect(new Uri(endpoint), cred). ____ `), yet startup throws a missing Key Vault credential error until the provider is wired completely. Which C# startup snippet completes the configuration?

Domain: Implement Azure security

- A. Wire `options.Connect(new Uri(endpoint), cred).ConfigureKeyVault(kv => kv.SetCredential(cred))` so App Configuration resolves Key Vault reference items using the app identity
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 54. During a Black Friday rollout, an engineer updates four related checkout timeout keys in Azure App Configuration and wants running ASP.NET Core pods to reload all four together rather than observing partial edits mid-update. Which pattern prevents partial reloads?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Store environment-labeled settings and `.appconfig.featureflag/*` entries in Azure App Configuration, register `AddAzureAppConfiguration` + `AddFeatureManagement`, and watch a single `Sentinel` key with `refreshAll: true`

### 55. A gift-card vault service must fetch database passwords, wrap symmetric AES keys using HSM-backed RSA keys, manage TLS certificates, and guarantee even compromised subscription admins cannot permanently purge deleted keys for 90 days. Which two Key Vault designs are required? Select two.

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use `SecretClient` (`Azure.Security.KeyVault.Secrets`) for connection strings/tokens, `KeyClient` / `CryptographyClient` (`Azure.Security.KeyVault.Keys`) for RSA/EC wrap-unwrap-sign, and `CertificateClient` for X.509 lifecycle
- D. Enable Soft Delete (mandatory on new vaults, 7–90 days) plus Purge Protection on Azure Key Vault so neither accidental deletion nor malicious principals can permanently destroy keys before retention expires
- E. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 56. A payment-archive worker encrypts 2 GB settlement files locally with a random 256-bit AES data encryption key (`dekBytes`) and wraps `dekBytes` using an RSA key stored in Azure Key Vault (` ____ `). Which SDK client and method perform the envelope wrap?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Instantiate `new CryptographyClient(keyVaultKey.Id, new DefaultAzureCredential())` and invoke `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync(...)`
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 57. Developers debug an order-enrichment service locally in Visual Studio signed into Azure CLI and deploy the exact same C# binary to Azure App Service with Managed Identity enabled. Which `Azure.Identity` credential class authenticates seamlessly in both environments?

Domain: Implement Azure security

- A. Instantiate `new DefaultAzureCredential()` (or explicit `ManagedIdentityCredential(clientId)` for user-assigned identities in production) so identical code authenticates via Azure CLI / Visual Studio locally and Managed Identity in Azure
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 58. An Azure Container App has three distinct user-assigned managed identities attached (one for ACR, one for Key Vault, one for Blob Storage), and `new DefaultAzureCredential()` fails with an ambiguous identity error at runtime (` ____ `). How must the C# code select the Key Vault identity?

Domain: Implement Azure security

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Instantiate `new DefaultAzureCredential(new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId })` (or set `AZURE_CLIENT_ID`)
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps

### 59. During flash-sale spikes, 3% of `POST /checkout` calls return HTTP 500, and on-call engineers need to trace each failed request across microservices into the exact downstream SQL or HTTP call that failed in Workspace-based Application Insights. Which two practices solve this? Select two.

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Query Workspace-based Application Insights (`AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces` or classic `requests`/`dependencies`/`exceptions`) joining on `OperationId` (`operation_Id`) to reconstruct end-to-end distributed transactions
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- E. Run `AppRequests | where ResultCode == "500" | join kind=inner (AppDependencies | where Success == false) on OperationId | project TimeGenerated, Name, Target, DependencyType, ResultCode1`

### 60. An SRE dashboard needs 5-minute time buckets over the past hour showing failed request counts and 95th-percentile latency per endpoint in Workspace-based Application Insights (` ____ `). Which KQL query produces those columns?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Run `AppRequests | where TimeGenerated > ago(1h) | summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)`
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 61. A short-lived console container runs a 12-second loyalty point expiration job, calls `TrackEvent("PointsExpired")`, and exits `Main` immediately, yet the final telemetry batch rarely appears in Application Insights. What fix ensures delivery?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 62. Inside a .NET 8 checkout API instrumented with `UseAzureMonitor()`, developers want a custom internal fraud-scoring method to appear as a timed child span inside Application Insights Transaction Search (` ____ `). How should they instrument the method?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 63. Vespera wants synthetic HTTPS probes from five global regions checking both HTTP 200 status and TLS certificate expiration on `https://shop.vespera.example`, paging on-call only when two or more regions fail simultaneously. What should be configured?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 64. Checkout traffic follows steep diurnal weekday/weekend curves, making static failure-count thresholds noisy at noon and blind at 03:00 AM, and alerts must trigger an automated PagerDuty webhook. Which Azure Monitor alert design fits?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Create an Azure Monitor Metric Alert (Dynamic Thresholds or static p95 latency/5xx count) or Scheduled Query (KQL) Alert targeting an Action Group configured with webhook / Azure Function / email-SMS receivers
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 65. An internal gift-card settlement API runs inside a private VNet with zero public ingress, so public Application Insights URL ping locations cannot reach it directly. How can the team publish synthetic availability probes into Application Insights and trigger alerts on multi-minute failures?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 66. A greenfield .NET 8 promotions API is adopting Microsoft's current recommended observability stack instead of deprecated Classic `InstrumentationKey` packages and needs both automatic ASP.NET Core request collection and custom domain spans. Which two steps should the developer take? Select two.

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`
- E. Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments

### 67. A newly formed storefront squad is onboarding an uninstrumented .NET 8 order API onto Workspace-based Application Insights with automated error alerting. Which rollout sequence follows official Azure Monitor guidance?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Set Adaptive Sampling to 0% maxTelemetryItemsPerSecond → deploy without connection string → query traces → attach Action Group
- B. Create a KQL alert rule on an empty subscription → uninstall OpenTelemetry packages → copy connection string → provision Application Insights
- C. Provision Workspace-based Application Insights and copy APPLICATIONINSIGHTS_CONNECTION_STRING → configure UseAzureMonitor() OpenTelemetry distro at startup → verify requests/dependencies in Logs → create a KQL or metric alert linked to an Action Group
- D. Create a deprecated Classic InstrumentationKey-only resource → hardcode ikey without SDK → fire Action Group → provision Log Analytics later

### 68. Vespera operates 40 flagship retail stores with local inventory microservices in each store LAN that must remain routable through local API gateway containers while pulling API policies from Azure over outbound port 443. Which APIM architecture supports this?

Domain: Connect to and consume Azure services and third-party services

- A. Select `Developer` (non-SLA) or `Premium` / `Standard v2` for VNet integration, and deploy the containerized APIM Self-Hosted Gateway (`mcr.microsoft.com/azure-api-management/gateway`) for hybrid on-premises/multi-cloud local traffic routing
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 69. Vespera's APIM gateway must call an internal Entra-protected pricing Function App without storing client secrets in Named Values (`<inbound> ____ </inbound>`). Which policy snippet authenticates the gateway to the backend?

Domain: Connect to and consume Azure services and third-party services

- A. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- B. Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 70. An API team wants to test a non-breaking OpenAPI schema patch at `;rev=2` and flip it live without changing mobile client URLs, while simultaneously publishing a breaking `/v2/cart` contract alongside `/v1/cart`. How do APIM `Revisions` and `Versions` map to these two tasks?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use APIM `Revisions` to stage, test, and swap non-breaking internal changes safely on the same consumer URL (`;rev=2`), and use APIM `Versions` (path/header/query) when publishing breaking contract changes side-by-side for distinct consumer cohorts

### 71. Mobile app developers need HTTP 200 sample payloads from `GET /loyalty/tiers` in APIM two weeks before the backend microservice exists, and once live, `/loyalty/tiers` must map to internal path `/internal/v2/orders/{orderId}` (` ____ `). Which APIM policies support both phases?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use `<mock-response status-code="200" content-type="application/json" />` during frontend parallel development, or `<rewrite-uri template="/internal/v2/orders/{orderId}" />` with `<set-backend-service base-url="..." />` in `<inbound>`

### 72. When importing an HTTP-triggered Azure Function App into Azure API Management as an API backend, APIM automatically stores a host key inside Named Values and sends `x-functions-key` on backend calls. Which Function `AuthorizationLevel` setting enforces that key check on the Function trigger?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 73. An inventory partner API exposed on Azure API Management requires each merchant tier to pass a Product Subscription Key, present an approved mTLS client certificate thumbprint, and carry a valid Entra bearer token. How should APIM enforce all three checks before calling backend pods?

Domain: Connect to and consume Azure services and third-party services

- A. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- B. Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 74. High-value B2B wholesale APIs on APIM must verify partner subscription keys, validate client X.509 certificate thumbprints plus caller Entra JWTs at the edge, and authenticate outbound from APIM to backend services via Managed Identity. Which two APIM security configurations cover both inbound and backend hops? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- C. Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- E. Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers

### 75. Vespera's public catalog API on APIM needs 60-call/minute burst throttling (`429`) plus 5,000-call/month partner monetization quotas (`403`) preserving `<base />`, 5-minute `Accept-Language`-aware response caching, and backend 5xx retries with outbound `X-AspNet-Version` removal. Which three APIM policy configurations implement all of these? Select three.

Domain: Connect to and consume Azure services and third-party services

- A. Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`
- B. Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`
- F. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 76. Proposed solution: Add `<rate-limit-by-key calls="100" renewal-period="60" counter-key="@(context.Request.IpAddress)" />` inside an operation's `<inbound>` block while deleting `<base />` to save XML lines. What unintended bug occurs, and what is the correct practice?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`

### 77. A developer adds `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` to `<inbound>` on `GET /catalog/featured`, yet every single request still misses the APIM cache and hits Cosmos DB. Why is nothing cached?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`

### 78. Vespera is registering a custom third-party warehouse HTTPS endpoint (`https://wms.partner.example/events`) on an Azure Event Grid custom topic. Which sequence completes the mandatory endpoint ownership handshake?

Domain: Connect to and consume Azure services and third-party services

- A. Deploy the HTTPS webhook endpoint accepting POST requests → create the Event Grid subscription pointing to the endpoint → inspect incoming SubscriptionValidationEvent and read validationCode → return HTTP 200 JSON containing validationResponse (or invoke validationUrl)
- B. Deploy an HTTP-only port 80 endpoint → return validationCode as a response header → create the Event Grid subscription → enable TLS
- C. Return HTTP 200 validationResponse before reading the request → create the topic → deploy the endpoint → create the subscription
- D. Create the Event Grid subscription → deploy the HTTPS endpoint later → return HTTP 202 empty body → parse SubscriptionValidationEvent

### 79. A retail marketplace platform pushes order-state events to 2,500 independent boutique merchants — each authorized strictly to its own topic — and exposes a custom webhook onboarding endpoint (` ____ `). Which two Event Grid implementations are required? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`
- C. Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization
- D. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- E. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 80. When creating an Event Grid webhook subscription against a custom ASP.NET Core controller, subscription deployment fails with `Webhook validation handshake failed`. What code (` ____ `) must the POST/OPTIONS endpoint implement?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`

### 81. Storefront clickstream events arrive at 30,000 events/sec, and both a real-time fraud engine and an hourly merchandising job must read the full stream independently without interfering with each other's cursors. How should Event Hubs be structured?

Domain: Connect to and consume Azure services and third-party services

- A. Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors

### 82. Proposed solution: Route 45,000 clickstream telemetry events per second into Azure Event Grid custom webhooks so three analytics teams can each replay the last 7 days from independent offsets and write Parquet batches to ADLS Gen2. Why does this fail, and what replaces it?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors

### 83. In an `EventProcessorClient` clickstream worker, redeploying pods causes every partition to replay two hours of already-processed events (`await eventArgs. ____ `). Which statement is missing inside `ProcessEventAsync`?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Host `EventProcessorClient` backed by `BlobContainerClient` and call `await eventArgs.UpdateCheckpointAsync()` after idempotent batch persistence so partition leases resume cleanly after rebalancing
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors

### 84. An order-confirmed event published to Azure Service Bus must fan out by `Region = 'EU'` at high throughput, preserve messages if a consumer pod crashes mid-flight, and isolate malformed payloads after `MaxDeliveryCount` retries. Which two Service Bus practices meet these needs? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false`, calling `CompleteMessageAsync` after commit, `AbandonMessageAsync` for transient retries, and `DeadLetterMessageAsync` on unrecoverable schema errors
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- E. Use Azure Service Bus Topics with `SqlRuleFilter` / `CorrelationRuleFilter` (`CorrelationRuleFilter` preferred for high throughput) and `SqlRuleAction` header stamping, inspecting `$DeadLetterQueue` (`SubQueue.DeadLetter`) after `MaxDeliveryCount` expires

### 85. When a shopper abandons checkout, Vespera wants to enqueue a reminder message invisible to consumers for 30 minutes (`long seq = await sender. ____ `) and cancel that message cleanly if the shopper completes payment within 10 minutes. Which Service Bus SDK call supports both?

Domain: Connect to and consume Azure services and third-party services

- A. Call `long seq = await sender.ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` and persist `seq` to call `CancelScheduledMessageAsync(seq)` if the user cancels early
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 86. A retail data-science team needs an inexpensive work queue holding 180 TB of 8 KB image-thumbnail tasks with simple HTTP visibility-timeout leases and no requirement for FIFO sessions or pub/sub topics. Which Azure messaging service fits this capacity requirement?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 87. Proposed solution: Call `QueueClient.PeekMessagesAsync()` in four worker instances to hide each thumbnail job for 60 seconds and pass the peeked message to `DeleteMessageAsync()`. Why does this fail, and which SDK pattern fixes it?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 88. A C# Queue Storage worker needs an extra 90 seconds to finish transcoding a product video before its lease expires (`await queueClient.UpdateMessageAsync(msg.MessageId, msg. ____ , msg.Body, TimeSpan.FromSeconds(90))`) and deletes the item afterward. Which Queue Storage workflow handles lease extension and deletion?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`

---

## Case study — BriskCart Loyalty

BriskCart Loyalty processes point redemptions across 1,200 stores. Store POS terminals enqueue redemption commands that must execute strictly in per-member FIFO order and ignore duplicate retries sent within ten minutes when store Wi-Fi flaps. A C# isolated-worker Azure Function processes redemptions, reads signing keys from Azure Key Vault, and exports distributed OpenTelemetry traces to Azure Monitor Application Insights without exceeding a 5 GB/day ingestion cap.

The next 3 questions refer to **BriskCart Loyalty**. Read the scenario brief once, then answer each item independently.

### 89. Store POS terminals resend loyalty redemption commands over flaky Wi-Fi and require strict per-member FIFO execution while discarding retries carrying the same `MessageId` within ten minutes. How should the queue be configured?

Domain: Connect to and consume Azure services and third-party services

- A. Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics
- B. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- C. Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 90. BriskCart's .NET 8 isolated-worker redemption Function must return an HTTP 200 receipt payload and write an audit document to Cosmos DB from the same invocation without `out` parameters. Which C# return structure works in the isolated worker model?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. In the .NET isolated worker model, return a custom POCO class uniting `[HttpResult]` (or `HttpResponseData`) with `[CosmosDBOutput]` / `[ServiceBusOutput]` properties
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`

### 91. Distributed OpenTelemetry traces span BriskCart's POS gateway, Service Bus processor Function, and ledger API, and daily telemetry volume must stay under 5 GB without breaking multi-hop `operation_Id` call graphs. Which sampling strategy fits best?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

---

## Case study — Cinder Coffee Roasters

Cinder Coffee Roasters hosts a B2B wholesale portal registered in a single-tenant Microsoft Entra ID directory. Wholesale buyers with the `WholesaleBuyer` app role upload PDF purchase orders directly from a React SPA to Azure Blob Storage without proxying 80 MB files through the web API, and uploaded PDFs must transition automatically to Cool storage after 30 days and delete after 365 days.

The next 3 questions refer to **Cinder Coffee Roasters**. Read the scenario brief once, then answer each item independently.

### 92. Cinder must restrict its wholesale purchase-order upload API inside its single-tenant Entra directory to users and automated EDI apps assigned `WholesaleBuyer`. How should authorization be modeled?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation
- C. Declare `appRoles` with `allowedMemberTypes: ["User", "Application"]` in the Entra app registration manifest and validate the `roles` claim (`[Authorize(Roles = "...")]`) in the web API
- D. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)

### 93. Cinder's React SPA requests a temporary upload URL from the ASP.NET Core API so buyers can upload 80 MB PDF orders directly to Blob Storage without exposing storage account keys. Which sequence of steps mints the token securely?

Domain: Implement Azure security

- A. Call GetUserDelegationKeyAsync anonymously → build BlobSasBuilder → assign RBAC to the identity → instantiate BlobServiceClient
- B. Instantiate BlobServiceClient with SAS token → assign RBAC → build BlobSasBuilder → call GetUserDelegationKeyAsync
- C. Assign Storage Blob Data Contributor/Delegator RBAC to the identity → instantiate BlobServiceClient with DefaultAzureCredential → call GetUserDelegationKeyAsync for a bounded validity window → build BlobSasBuilder and sign with the user delegation key
- D. Build BlobSasBuilder and sign → call GetUserDelegationKeyAsync → instantiate BlobServiceClient with shared account key → assign RBAC to the identity

### 94. Uploaded PDF purchase orders in the `po-uploads/` prefix must move to `Cool` storage 30 days after modification and purge automatically after 365 days without scheduled Function scripts. What should Cinder configure?

Domain: Develop for Azure storage

- A. Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob)
- B. Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`)
- C. Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

---

## Case study — Kova Footwear

Kova Footwear ingests warehouse RFID scans into Azure Container Apps and stores inventory state in Cosmos DB. Every stock depletion must notify downstream marketplace partners within three seconds through HTTPS webhooks that strip internal warehouse IDs, while preserving failed partner deliveries for 24 hours in Blob Storage. External partner apps call Kova APIs through Azure API Management Developer/Standard v2 using Microsoft Entra bearer tokens.

The next 3 questions refer to **Kova Footwear**. Read the scenario brief once, then answer each item independently.

### 95. Kova must push sub-3-second stock-depletion notifications to partner HTTPS webhooks while dead-lettering undelivered partner payloads for 24 hours in Azure Blob Storage. Which Event Grid configuration satisfies both requirements?

Domain: Connect to and consume Azure services and third-party services

- A. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL

### 96. Partner responses flowing out of Kova's Azure API Management gateway must strip internal backend fingerprinting headers while retrying transient HTTP 503 responses from Container Apps up to three times. Where should the XML policies be placed?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`

### 97. Kova wants APIM to reject external partner calls lacking a valid Microsoft Entra token with the `Inventory.Read` role before forwarding requests (`<inbound> ____ </inbound>`). Which policy snippet completes the gateway configuration?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- C. Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

---

## Case study — Vespera Retail

Vespera Retail runs an ASP.NET Core storefront on Azure App Service (Standard S2, Linux) backed by Azure Cosmos DB for NoSQL partitioned by `/customerId` and Azure Blob Storage for receipts. Flash drops spike checkout requests 15x within two minutes. Zero-downtime deployments must keep the `Production` payment webhook URL strictly off `staging` slots, and developers are forbidden from storing connection strings in `appsettings.json` or GitHub repositories.

The next 3 questions refer to **Vespera Retail**. Read the scenario brief once, then answer each item independently.

### 98. During blue-green releases between `staging` and `Production` on the Standard S2 Linux plan, how should Vespera ensure the live `PaymentWebhookUrl` value never leaks onto the `staging` slot or gets overwritten during slot swaps?

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Mark environment-specific settings such as `PaymentWebhookUrl` and production connection strings as `slotSetting: true` (Deployment slot setting) before swapping slots
- D. Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances

### 99. Vespera's order-history endpoint queries a single shopper's orders inside `/customerId` and must stream 100-item pages while logging per-page RU consumption (` ____ `). Which C# Cosmos DB SDK v3 pattern should the developer implement?

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use `FeedIterator<Order> iter = container.GetItemQueryIterator<Order>(queryDef, requestOptions: new QueryRequestOptions { PartitionKey = new PartitionKey(pk), MaxItemCount = 100 })` and loop `while (iter.HasMoreResults) { FeedResponse<Order> page = await iter.ReadNextAsync(); }`

### 100. Vespera's ASP.NET Core checkout app needs to read Cosmos DB and storage secrets without storing credentials in `appsettings.json` or writing Key Vault SDK startup code. Which configuration meets this policy?

Domain: Implement Azure security

- A. Configure App Service / Functions application settings using `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` (omitting secret version) paired with `Key Vault Secrets User` on the app Managed Identity
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

---

## Answer key and explanations

### Question 1 — A, C

Answers: Use a multi-stage Dockerfile building in `mcr.microsoft.com/dotnet/sdk:8.0` and copying published output into `mcr.microsoft.com/dotnet/aspnet:8.0` with a non-root `USER app`; Add `bin/`, `obj/`, `.git/`, and local `.env` files to `.dockerignore` before running `docker build` or `az acr build`. Combining a multi-stage Dockerfile targeting `dotnet/aspnet:8.0` under a non-root `USER` with a strict `.dockerignore` removes compiler layers and blocks local artifacts from entering the context. Local study-map skill 1.1 (Create and Manage Container Images and Multi-Stage Dockerfiles), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Multi-stage Docker builds exclude compiler SDK layers and source files from the final runtime image, shrinking image size and attack surface. In this scenario: Combining a multi-stage Dockerfile targeting `dotnet/aspnet:8.0` under a non-root `USER` with a strict `.dockerignore` removes compiler layers and blocks local artifacts from entering the context.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Combining a multi-stage Dockerfile targeting `dotnet/aspnet:8.0` under a non-root `USER` with a strict `.dockerignore` removes compiler layers and blocks local artifacts from entering the context.
- **C:** Correct. `.dockerignore` prevents streaming gigabytes of local build artifacts and stray secrets into the build context. In this scenario: Combining a multi-stage Dockerfile targeting `dotnet/aspnet:8.0` under a non-root `USER` with a strict `.dockerignore` removes compiler layers and blocks local artifacts from entering the context.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Combining a multi-stage Dockerfile targeting `dotnet/aspnet:8.0` under a non-root `USER` with a strict `.dockerignore` removes compiler layers and blocks local artifacts from entering the context.
- **E:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Combining a multi-stage Dockerfile targeting `dotnet/aspnet:8.0` under a non-root `USER` with a strict `.dockerignore` removes compiler layers and blocks local artifacts from entering the context.

### Question 2 — D

Answer: Set `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` inside the final `.NET 8` runtime stage and match `targetPort: 8080` on Container Apps ingress. Official .NET 8 container images bind port `8080` by default so non-root containers run without `CAP_NET_BIND_SERVICE`; matching `ASPNETCORE_HTTP_PORTS=8080`, `EXPOSE 8080`, and `targetPort: 8080` prevents 502 gateway errors. Starting in .NET 8, official Microsoft container images default to non-root port `8080` rather than privileged port `80`. Local study-map skill 1.1 (Create and Manage Container Images and Multi-Stage Dockerfiles), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Official .NET 8 container images bind port `8080` by default so non-root containers run without `CAP_NET_BIND_SERVICE`; matching `ASPNETCORE_HTTP_PORTS=8080`, `EXPOSE 8080`, and `targetPort: 8080` prevents 502 gateway errors.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Official .NET 8 container images bind port `8080` by default so non-root containers run without `CAP_NET_BIND_SERVICE`; matching `ASPNETCORE_HTTP_PORTS=8080`, `EXPOSE 8080`, and `targetPort: 8080` prevents 502 gateway errors.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Official .NET 8 container images bind port `8080` by default so non-root containers run without `CAP_NET_BIND_SERVICE`; matching `ASPNETCORE_HTTP_PORTS=8080`, `EXPOSE 8080`, and `targetPort: 8080` prevents 502 gateway errors.
- **D:** Correct. Starting in .NET 8, official Microsoft container images default to non-root port `8080` rather than privileged port `80`. In this scenario: Official .NET 8 container images bind port `8080` by default so non-root containers run without `CAP_NET_BIND_SERVICE`; matching `ASPNETCORE_HTTP_PORTS=8080`, `EXPOSE 8080`, and `targetPort: 8080` prevents 502 gateway errors.

### Question 3 — D

Answer: Run `az acr build --registry <acrName> --image app:{{.Run.ID}} .` to build and push the container image remotely using ACR Tasks without a local Docker daemon. `az acr build --registry <acrName> --image ... .` streams the build context to Azure Container Registry Tasks to build and push layers remotely without local Docker Engine. ACR Tasks tar and upload the build context to Azure, executing the Dockerfile build and pushing tagged layers directly inside ACR. Local study-map skill 1.2 (Publish Images, Run ACR Tasks, and Manage Auth/Purge in Azure Container Registry), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `az acr build --registry <acrName> --image ... .` streams the build context to Azure Container Registry Tasks to build and push layers remotely without local Docker Engine.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az acr build --registry <acrName> --image ... .` streams the build context to Azure Container Registry Tasks to build and push layers remotely without local Docker Engine.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `az acr build --registry <acrName> --image ... .` streams the build context to Azure Container Registry Tasks to build and push layers remotely without local Docker Engine.
- **D:** Correct. ACR Tasks tar and upload the build context to Azure, executing the Dockerfile build and pushing tagged layers directly inside ACR. In this scenario: `az acr build --registry <acrName> --image ... .` streams the build context to Azure Container Registry Tasks to build and push layers remotely without local Docker Engine.

### Question 4 — C

Answer: Schedule an ACR Task executing `acr purge --filter "app:.*" --ago 30d --untagged` to clean stale untagged manifests and old tags automatically. Scheduling an ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` automatically prunes stale tags and dangling manifests without sharing admin credentials. Scheduled `acr purge` tasks reclaim registry storage quota without manual tag deletion scripts. Local study-map skill 1.2 (Publish Images, Run ACR Tasks, and Manage Auth/Purge in Azure Container Registry), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Scheduling an ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` automatically prunes stale tags and dangling manifests without sharing admin credentials.
- **B:** Incorrect for this requirement. ACR geo-replication requires the `Premium` tier and serves local regional layer pulls through a single registry login server FQDN. Why the keyed choice wins: Scheduling an ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` automatically prunes stale tags and dangling manifests without sharing admin credentials.
- **C:** Correct. Scheduled `acr purge` tasks reclaim registry storage quota without manual tag deletion scripts. In this scenario: Scheduling an ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` automatically prunes stale tags and dangling manifests without sharing admin credentials.
- **D:** Incorrect for this requirement. `az acr import` copies public or cross-registry container images server-side into ACR without requiring `docker pull` / `docker push` on a local workstation. Why the keyed choice wins: Scheduling an ACR Task running `acr purge --filter "app:.*" --ago 30d --untagged` automatically prunes stale tags and dangling manifests without sharing admin credentials.

### Question 5 — A

Answer: Set `--restart-policy OnFailure` (or `Never`) on the Azure Container Instances container group so batch containers stop billing vCPU/memory seconds once exit code 0 completes. Setting `--restart-policy OnFailure` (or `Never`) stops execution and per-second billing as soon as the container exits with code `0`, while still retrying non-zero crashes under `OnFailure`. ACI bills per second while containers run; `OnFailure` retries crashes (`exit != 0`) and halts cleanly on `exit == 0`, whereas `Always` loops forever. Local study-map skill 1.3 (Run Container Groups, Sidecars, Volumes, and Restart Policies in Azure Container Instances), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. ACI bills per second while containers run; `OnFailure` retries crashes (`exit != 0`) and halts cleanly on `exit == 0`, whereas `Always` loops forever. In this scenario: Setting `--restart-policy OnFailure` (or `Never`) stops execution and per-second billing as soon as the container exits with code `0`, while still retrying non-zero crashes under `OnFailure`.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting `--restart-policy OnFailure` (or `Never`) stops execution and per-second billing as soon as the container exits with code `0`, while still retrying non-zero crashes under `OnFailure`.
- **C:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Setting `--restart-policy OnFailure` (or `Never`) stops execution and per-second billing as soon as the container exits with code `0`, while still retrying non-zero crashes under `OnFailure`.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `--restart-policy OnFailure` (or `Never`) stops execution and per-second billing as soon as the container exits with code `0`, while still retrying non-zero crashes under `OnFailure`.

### Question 6 — B

Answer: Deploy the application container and Envoy/logging sidecar inside one multi-container ACI group sharing `localhost` network namespace and an `emptyDir` / Azure Files volume. Deploying both containers inside a single Linux multi-container group shares the `localhost` network namespace and allows mounting a shared `emptyDir` or Azure Files volume. Containers in the same ACI container group share one IP/port namespace (`127.0.0.1`) and can mount shared Azure Files or `emptyDir` volumes on Linux. Local study-map skill 1.3 (Run Container Groups, Sidecars, Volumes, and Restart Policies in Azure Container Instances), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Deploying both containers inside a single Linux multi-container group shares the `localhost` network namespace and allows mounting a shared `emptyDir` or Azure Files volume.
- **B:** Correct. Containers in the same ACI container group share one IP/port namespace (`127.0.0.1`) and can mount shared Azure Files or `emptyDir` volumes on Linux. In this scenario: Deploying both containers inside a single Linux multi-container group shares the `localhost` network namespace and allows mounting a shared `emptyDir` or Azure Files volume.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Deploying both containers inside a single Linux multi-container group shares the `localhost` network namespace and allows mounting a shared `emptyDir` or Azure Files volume.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Deploying both containers inside a single Linux multi-container group shares the `localhost` network namespace and allows mounting a shared `emptyDir` or Azure Files volume.

### Question 7 — C

Answer: Build and push the image to ACR with az acr build → create a user-assigned managed identity and grant AcrPull on the registry → create the Container Apps environment → create the container app referencing the identity and registry server. Creating and assigning the user-assigned identity `AcrPull` on ACR before passing `--registry-identity` during `az containerapp create` guarantees the initial revision pull succeeds without admin keys. The image and AcrPull identity grant must exist before Container Apps pulls the image from ACR without admin credentials. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Enabling admin passwords violates credential-free deployment, and revoking AcrPull breaks subsequent revision pulls. Why the keyed choice wins: Creating and assigning the user-assigned identity `AcrPull` on ACR before passing `--registry-identity` during `az containerapp create` guarantees the initial revision pull succeeds without admin keys.
- **B:** Incorrect for this requirement. A container app cannot be created before its environment exists or pull an image before AcrPull and the image tag exist. Why the keyed choice wins: Creating and assigning the user-assigned identity `AcrPull` on ACR before passing `--registry-identity` during `az containerapp create` guarantees the initial revision pull succeeds without admin keys.
- **C:** Correct. The image and AcrPull identity grant must exist before Container Apps pulls the image from ACR without admin credentials. In this scenario: Creating and assigning the user-assigned identity `AcrPull` on ACR before passing `--registry-identity` during `az containerapp create` guarantees the initial revision pull succeeds without admin keys.
- **D:** Incorrect for this requirement. Role assignment cannot precede creating the managed identity, and the container app revision fails if the image has not been pushed. Why the keyed choice wins: Creating and assigning the user-assigned identity `AcrPull` on ACR before passing `--registry-identity` during `az containerapp create` guarantees the initial revision pull succeeds without admin keys.

### Question 8 — A, C, E

Answers: Set `--revision-mode multiple` and apply `az containerapp ingress traffic set --revision-weight` to split live HTTP requests across named revisions; Configure a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0` and Managed Identity (`identity` property) so replicas scale to zero when idle and wake on queue depth; Define a Container App secret using `keyVaultUrl` plus `identity` (managed identity resource ID or `system`) and map container environment variables via `secretRef`. Multiple-revision traffic weights handle 90/10 canary splits, KEDA `azure-servicebus` rules with `minReplicas: 0` and Managed Identity enable scale-to-zero consumers, and Key Vault `keyVaultUrl` + `identity` secret refs eliminate plaintext secrets. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Multiple-revision mode keeps more than one revision active simultaneously for weighted blue/green or canary traffic splitting. In this scenario: Multiple-revision traffic weights handle 90/10 canary splits, KEDA `azure-servicebus` rules with `minReplicas: 0` and Managed Identity enable scale-to-zero consumers, and Key Vault `keyVaultUrl` + `identity` secret refs eliminate plaintext secrets.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Multiple-revision traffic weights handle 90/10 canary splits, KEDA `azure-servicebus` rules with `minReplicas: 0` and Managed Identity enable scale-to-zero consumers, and Key Vault `keyVaultUrl` + `identity` secret refs eliminate plaintext secrets.
- **C:** Correct. Container Apps uses KEDA scalers to scale down to zero on consumption/workload profiles and authenticate scalers cleanly via Managed Identity. In this scenario: Multiple-revision traffic weights handle 90/10 canary splits, KEDA `azure-servicebus` rules with `minReplicas: 0` and Managed Identity enable scale-to-zero consumers, and Key Vault `keyVaultUrl` + `identity` secret refs eliminate plaintext secrets.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Multiple-revision traffic weights handle 90/10 canary splits, KEDA `azure-servicebus` rules with `minReplicas: 0` and Managed Identity enable scale-to-zero consumers, and Key Vault `keyVaultUrl` + `identity` secret refs eliminate plaintext secrets.
- **E:** Correct. Key Vault secret references in Container Apps resolve secrets via Managed Identity without storing secret strings in ARM templates. In this scenario: Multiple-revision traffic weights handle 90/10 canary splits, KEDA `azure-servicebus` rules with `minReplicas: 0` and Managed Identity enable scale-to-zero consumers, and Key Vault `keyVaultUrl` + `identity` secret refs eliminate plaintext secrets.
- **F:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Multiple-revision traffic weights handle 90/10 canary splits, KEDA `azure-servicebus` rules with `minReplicas: 0` and Managed Identity enable scale-to-zero consumers, and Key Vault `keyVaultUrl` + `identity` secret refs eliminate plaintext secrets.

### Question 9 — A

Answer: Execute `az containerapp env create --name <envName> --resource-group <rg> --infrastructure-subnet-resource-id <subnetId> --internal-only`. `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` injects the environment into the subnet with a private internal load balancer. Provisioning a VNet-injected `--internal-only` Container Apps environment isolates the Envoy ingress load balancer to private RFC1918 addresses. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Provisioning a VNet-injected `--internal-only` Container Apps environment isolates the Envoy ingress load balancer to private RFC1918 addresses. In this scenario: `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` injects the environment into the subnet with a private internal load balancer.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` injects the environment into the subnet with a private internal load balancer.
- **C:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` injects the environment into the subnet with a private internal load balancer.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `az containerapp env create ... --infrastructure-subnet-resource-id <subnetId> --internal-only` injects the environment into the subnet with a private internal load balancer.

### Question 10 — A

Answer: Deploy an Azure Container Apps Job (`triggerType: Event` or `Schedule`) with `replicaCompletionCount` and `parallelism` instead of an always-listening HTTP container app. Azure Container Apps Jobs (`triggerType: Event` or `Schedule`) run bounded batch executions with configurable `parallelism` and `replicaCompletionCount` rather than keeping an HTTP app running. Container Apps Jobs execute finite scheduled or event-driven workloads to completion without exposing unused HTTP ingress. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Container Apps Jobs execute finite scheduled or event-driven workloads to completion without exposing unused HTTP ingress. In this scenario: Azure Container Apps Jobs (`triggerType: Event` or `Schedule`) run bounded batch executions with configurable `parallelism` and `replicaCompletionCount` rather than keeping an HTTP app running.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Azure Container Apps Jobs (`triggerType: Event` or `Schedule`) run bounded batch executions with configurable `parallelism` and `replicaCompletionCount` rather than keeping an HTTP app running.
- **C:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Azure Container Apps Jobs (`triggerType: Event` or `Schedule`) run bounded batch executions with configurable `parallelism` and `replicaCompletionCount` rather than keeping an HTTP app running.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Azure Container Apps Jobs (`triggerType: Event` or `Schedule`) run bounded batch executions with configurable `parallelism` and `replicaCompletionCount` rather than keeping an HTTP app running.

### Question 11 — C

Answer: Provision at least a `Standard` (`S1+`) or `Premium v3` (`P1v3+`) App Service plan to unlock deployment slots, custom domain SNI SSL, and metric/schedule autoscaling. `Free` and `Basic` plans support neither deployment slots nor rule-based autoscale; upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks both capabilities. `Free`, `Shared`, and `Basic` plans omit deployment slots (`S1` gives 5, `P1v3` gives 20) and rule-based autoscale (`S1+` required). Local study-map skill 1.5 (Create Azure App Service Plans and Web Apps Across Linux and Windows Runtimes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `Free` and `Basic` plans support neither deployment slots nor rule-based autoscale; upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks both capabilities.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `Free` and `Basic` plans support neither deployment slots nor rule-based autoscale; upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks both capabilities.
- **C:** Correct. `Free`, `Shared`, and `Basic` plans omit deployment slots (`S1` gives 5, `P1v3` gives 20) and rule-based autoscale (`S1+` required). In this scenario: `Free` and `Basic` plans support neither deployment slots nor rule-based autoscale; upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks both capabilities.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `Free` and `Basic` plans support neither deployment slots nor rule-based autoscale; upgrading to `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks both capabilities.

### Question 12 — B

Answer: Enable `httpsOnly: true`, set `minTlsVersion: "1.2"` (or `"1.3"`), and configure `clientCertEnabled` when mutual TLS client certificates are required. Enabling `httpsOnly: true`, setting `minTlsVersion: "1.2"` (or `"1.3"`), and turning on `clientCertEnabled` enforces HTTPS, modern TLS, and inbound mTLS forwarding (`X-ARR-ClientCert`) before app code runs. Enforcing HTTPS redirection and minimum TLS 1.2/1.3 at the App Service front end rejects plaintext HTTP and legacy ciphers before app code runs. Local study-map skill 1.5 (Create Azure App Service Plans and Web Apps Across Linux and Windows Runtimes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Enabling `httpsOnly: true`, setting `minTlsVersion: "1.2"` (or `"1.3"`), and turning on `clientCertEnabled` enforces HTTPS, modern TLS, and inbound mTLS forwarding (`X-ARR-ClientCert`) before app code runs.
- **B:** Correct. Enforcing HTTPS redirection and minimum TLS 1.2/1.3 at the App Service front end rejects plaintext HTTP and legacy ciphers before app code runs. In this scenario: Enabling `httpsOnly: true`, setting `minTlsVersion: "1.2"` (or `"1.3"`), and turning on `clientCertEnabled` enforces HTTPS, modern TLS, and inbound mTLS forwarding (`X-ARR-ClientCert`) before app code runs.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling `httpsOnly: true`, setting `minTlsVersion: "1.2"` (or `"1.3"`), and turning on `clientCertEnabled` enforces HTTPS, modern TLS, and inbound mTLS forwarding (`X-ARR-ClientCert`) before app code runs.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Enabling `httpsOnly: true`, setting `minTlsVersion: "1.2"` (or `"1.3"`), and turning on `clientCertEnabled` enforces HTTPS, modern TLS, and inbound mTLS forwarding (`X-ARR-ClientCert`) before app code runs.

### Question 13 — D

Answer: Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances. Filesystem application logging disables itself after 12 hours to protect local disk quota; routing Application and Web Server diagnostics to Azure Blob Storage enforces durable multi-day retention across all instances. Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy. Local study-map skill 1.6 (Configure App Service Diagnostics, Application/Web Server Logging, and Log Streaming), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting. Why the keyed choice wins: Filesystem application logging disables itself after 12 hours to protect local disk quota; routing Application and Web Server diagnostics to Azure Blob Storage enforces durable multi-day retention across all instances.
- **B:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Filesystem application logging disables itself after 12 hours to protect local disk quota; routing Application and Web Server diagnostics to Azure Blob Storage enforces durable multi-day retention across all instances.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Filesystem application logging disables itself after 12 hours to protect local disk quota; routing Application and Web Server diagnostics to Azure Blob Storage enforces durable multi-day retention across all instances.
- **D:** Correct. Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy. In this scenario: Filesystem application logging disables itself after 12 hours to protect local disk quota; routing Application and Web Server diagnostics to Azure Blob Storage enforces durable multi-day retention across all instances.

### Question 14 — C

Answer: Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`. `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail` streams real-time stdout/stderr output from Kudu `/api/logstream`. `az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting. Local study-map skill 1.6 (Configure App Service Diagnostics, Application/Web Server Logging, and Log Streaming), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail` streams real-time stdout/stderr output from Kudu `/api/logstream`.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail` streams real-time stdout/stderr output from Kudu `/api/logstream`.
- **C:** Correct. `az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting. In this scenario: `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail` streams real-time stdout/stderr output from Kudu `/api/logstream`.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail` streams real-time stdout/stderr output from Kudu `/api/logstream`.

### Question 15 — C

Answer: Set `WEBSITE_RUN_FROM_PACKAGE=1` and deploy with `az webapp deploy --type zip` so the app mounts the read-only ZIP package directly with atomic cold-start replacement. Setting `WEBSITE_RUN_FROM_PACKAGE=1` with `az webapp deploy --type zip` mounts the ZIP archive directly as read-only `wwwroot`, eliminating file-copy locks and switching versions atomically. Running directly from a mounted ZIP eliminates file-lock copy conflicts during `wwwroot` sync and speeds cold starts. Local study-map skill 1.7 (Deploy Code, Run-From-Package ZIPs, and Custom Containers to App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` with `az webapp deploy --type zip` mounts the ZIP archive directly as read-only `wwwroot`, eliminating file-copy locks and switching versions atomically.
- **B:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` with `az webapp deploy --type zip` mounts the ZIP archive directly as read-only `wwwroot`, eliminating file-copy locks and switching versions atomically.
- **C:** Correct. Running directly from a mounted ZIP eliminates file-lock copy conflicts during `wwwroot` sync and speeds cold starts. In this scenario: Setting `WEBSITE_RUN_FROM_PACKAGE=1` with `az webapp deploy --type zip` mounts the ZIP archive directly as read-only `wwwroot`, eliminating file-copy locks and switching versions atomically.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `WEBSITE_RUN_FROM_PACKAGE=1` with `az webapp deploy --type zip` mounts the ZIP archive directly as read-only `wwwroot`, eliminating file-copy locks and switching versions atomically.

### Question 16 — B

Answer: Disable the ACR admin account and assign the built-in `AcrPull` role on the registry to the compute resource managed identity. Disabling the shared ACR admin account, granting `AcrPull` to the Web App's Managed Identity, and enabling `acrUseManagedIdentityCreds: true` pulls container layers without static passwords. `AcrPull` with Managed Identity eliminates shared registry passwords while granting least-privilege read-only image pulls. Local study-map skill 1.7 (Deploy Code, Run-From-Package ZIPs, and Custom Containers to App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Disabling the shared ACR admin account, granting `AcrPull` to the Web App's Managed Identity, and enabling `acrUseManagedIdentityCreds: true` pulls container layers without static passwords.
- **B:** Correct. `AcrPull` with Managed Identity eliminates shared registry passwords while granting least-privilege read-only image pulls. In this scenario: Disabling the shared ACR admin account, granting `AcrPull` to the Web App's Managed Identity, and enabling `acrUseManagedIdentityCreds: true` pulls container layers without static passwords.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Disabling the shared ACR admin account, granting `AcrPull` to the Web App's Managed Identity, and enabling `acrUseManagedIdentityCreds: true` pulls container layers without static passwords.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Disabling the shared ACR admin account, granting `AcrPull` to the Web App's Managed Identity, and enabling `acrUseManagedIdentityCreds: true` pulls container layers without static passwords.

### Question 17 — A, C

Answers: Configure App Service `CORS` with explicit origin URLs (and `supportCredentials` only without wildcard `*`) so App Service handles preflight `OPTIONS` requests; Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`. Configuring explicit origins on App Service `CORS` (never wildcard `*` when credentials are enabled) handles browser `OPTIONS` preflights, and `az webapp config connection-string set --slot-settings` binds each slot's SQL connection string safely. Local study-map skill 1.8 (Configure TLS, Mutual TLS, CORS, App Settings, and Service Connections on App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. `--slot-settings` pins the connection string (`SQLCONNSTR_LedgerDb`) to the target slot so slot swaps never leak staging databases into production. In this scenario: Configuring explicit origins on App Service `CORS` (never wildcard `*` when credentials are enabled) handles browser `OPTIONS` preflights, and `az webapp config connection-string set --slot-settings` binds each slot's SQL connection string safely.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Configuring explicit origins on App Service `CORS` (never wildcard `*` when credentials are enabled) handles browser `OPTIONS` preflights, and `az webapp config connection-string set --slot-settings` binds each slot's SQL connection string safely.
- **C:** Correct. Platform-level App Service CORS intercepts `OPTIONS` preflight checks; credentialed CORS forbids wildcard `*` origins. In this scenario: Configuring explicit origins on App Service `CORS` (never wildcard `*` when credentials are enabled) handles browser `OPTIONS` preflights, and `az webapp config connection-string set --slot-settings` binds each slot's SQL connection string safely.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Configuring explicit origins on App Service `CORS` (never wildcard `*` when credentials are enabled) handles browser `OPTIONS` preflights, and `az webapp config connection-string set --slot-settings` binds each slot's SQL connection string safely.
- **E:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Configuring explicit origins on App Service `CORS` (never wildcard `*` when credentials are enabled) handles browser `OPTIONS` preflights, and `az webapp config connection-string set --slot-settings` binds each slot's SQL connection string safely.

### Question 18 — A

Answer: Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`. Passing `--connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` injects `SQLCONNSTR_LedgerDb` for `GetConnectionString("LedgerDb")` while pinning it to its deployment slot. `--slot-settings` pins the connection string (`SQLCONNSTR_LedgerDb`) to the target slot so slot swaps never leak staging databases into production. Local study-map skill 1.8 (Configure TLS, Mutual TLS, CORS, App Settings, and Service Connections on App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. `--slot-settings` pins the connection string (`SQLCONNSTR_LedgerDb`) to the target slot so slot swaps never leak staging databases into production. In this scenario: Passing `--connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` injects `SQLCONNSTR_LedgerDb` for `GetConnectionString("LedgerDb")` while pinning it to its deployment slot.
- **B:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Passing `--connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` injects `SQLCONNSTR_LedgerDb` for `GetConnectionString("LedgerDb")` while pinning it to its deployment slot.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Passing `--connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` injects `SQLCONNSTR_LedgerDb` for `GetConnectionString("LedgerDb")` while pinning it to its deployment slot.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Passing `--connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` injects `SQLCONNSTR_LedgerDb` for `GetConnectionString("LedgerDb")` while pinning it to its deployment slot.

### Question 19 — B

Answer: Pair every scale-out metric rule (e.g., CPU > 75% for 10 min) with a conservative scale-in rule (e.g., CPU < 35%) and an explicit `coolDown` window plus safe default/max instance bounds. Widening the gap between scale-out (e.g., >75%) and scale-in (e.g., <35%) thresholds and setting an explicit multi-minute `coolDown` window prevents oscillation (flapping) while metrics stabilize. Asymmetric thresholds and cool-down periods prevent rapid flapping (thrashing) where instances repeatedly add and terminate. Local study-map skill 1.9 (Implement Metric-Based and Schedule-Based App Service Autoscaling Rules and Cooldowns), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Widening the gap between scale-out (e.g., >75%) and scale-in (e.g., <35%) thresholds and setting an explicit multi-minute `coolDown` window prevents oscillation (flapping) while metrics stabilize.
- **B:** Correct. Asymmetric thresholds and cool-down periods prevent rapid flapping (thrashing) where instances repeatedly add and terminate. In this scenario: Widening the gap between scale-out (e.g., >75%) and scale-in (e.g., <35%) thresholds and setting an explicit multi-minute `coolDown` window prevents oscillation (flapping) while metrics stabilize.
- **C:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Widening the gap between scale-out (e.g., >75%) and scale-in (e.g., <35%) thresholds and setting an explicit multi-minute `coolDown` window prevents oscillation (flapping) while metrics stabilize.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Widening the gap between scale-out (e.g., >75%) and scale-in (e.g., <35%) thresholds and setting an explicit multi-minute `coolDown` window prevents oscillation (flapping) while metrics stabilize.

### Question 20 — A

Answer: Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps. Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` forces App Service to await HTTP 200 readiness on the warm-up endpoint before routing production traffic. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. Local study-map skill 1.9 (Implement Metric-Based and Schedule-Based App Service Autoscaling Rules and Cooldowns), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. In this scenario: Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` forces App Service to await HTTP 200 readiness on the warm-up endpoint before routing production traffic.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` forces App Service to await HTTP 200 readiness on the warm-up endpoint before routing production traffic.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` forces App Service to await HTTP 200 readiness on the warm-up endpoint before routing production traffic.
- **D:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Configuring `applicationInitialization` alongside `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` forces App Service to await HTTP 200 readiness on the warm-up endpoint before routing production traffic.

### Question 21 — A

Answer: Create the staging deployment slot on the Standard/Premium Web App → mark production-only connection strings and webhook settings as deployment slot settings → deploy and warm up the new build in staging → swap staging into production and verify health. Provisioning the staging slot, pinning slot-specific settings first, deploying and warming v2.4 in staging, and then swapping into production preserves zero downtime and config isolation. Slot-sticky settings must be pinned before swapping so staging never inherits live payment webhooks or overwrites production secrets during swap. Local study-map skill 1.10 (Configure App Service Deployment Slots, Slot-Sticky Settings, Warm-Up, and Traffic Routing), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Slot-sticky settings must be pinned before swapping so staging never inherits live payment webhooks or overwrites production secrets during swap. In this scenario: Provisioning the staging slot, pinning slot-specific settings first, deploying and warming v2.4 in staging, and then swapping into production preserves zero downtime and config isolation.
- **B:** Incorrect for this requirement. Free and Basic App Service plans do not support deployment slots; Standard, Premium, or Isolated is required first. Why the keyed choice wins: Provisioning the staging slot, pinning slot-specific settings first, deploying and warming v2.4 in staging, and then swapping into production preserves zero downtime and config isolation.
- **C:** Incorrect for this requirement. Deploying directly to production bypasses zero-downtime validation and swapping an empty staging slot overwrites production. Why the keyed choice wins: Provisioning the staging slot, pinning slot-specific settings first, deploying and warming v2.4 in staging, and then swapping into production preserves zero downtime and config isolation.
- **D:** Incorrect for this requirement. You cannot swap a slot before creating and deploying to it, and marking settings sticky after the swap leaks staging values into production. Why the keyed choice wins: Provisioning the staging slot, pinning slot-specific settings first, deploying and warming v2.4 in staging, and then swapping into production preserves zero downtime and config isolation.

### Question 22 — D

Answer: Host the Function App on `Flex Consumption` or `Elastic Premium (EP1+)` when VNet integration, longer execution timeouts beyond 10 minutes, or pre-warmed/always-ready instances are required. Classic Consumption caps execution at 10 minutes and lacks VNet integration / pre-warmed readiness; migrating to `Flex Consumption` or `Elastic Premium (EP1+)` supports VNet outbound, extended/unbounded timeouts, and pre-warmed instances. Classic Consumption caps timeout at 10 minutes (`functionTimeout`) and cold-starts from zero; `Flex Consumption` and `Premium` add VNet outbound and pre-warmed readiness. Local study-map skill 1.11 (Create and Configure Azure Functions Apps, Hosting Plans, and host.json Settings), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Classic Consumption caps execution at 10 minutes and lacks VNet integration / pre-warmed readiness; migrating to `Flex Consumption` or `Elastic Premium (EP1+)` supports VNet outbound, extended/unbounded timeouts, and pre-warmed instances.
- **B:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Classic Consumption caps execution at 10 minutes and lacks VNet integration / pre-warmed readiness; migrating to `Flex Consumption` or `Elastic Premium (EP1+)` supports VNet outbound, extended/unbounded timeouts, and pre-warmed instances.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Classic Consumption caps execution at 10 minutes and lacks VNet integration / pre-warmed readiness; migrating to `Flex Consumption` or `Elastic Premium (EP1+)` supports VNet outbound, extended/unbounded timeouts, and pre-warmed instances.
- **D:** Correct. Classic Consumption caps timeout at 10 minutes (`functionTimeout`) and cold-starts from zero; `Flex Consumption` and `Premium` add VNet outbound and pre-warmed readiness. In this scenario: Classic Consumption caps execution at 10 minutes and lacks VNet integration / pre-warmed readiness; migrating to `Flex Consumption` or `Elastic Premium (EP1+)` supports VNet outbound, extended/unbounded timeouts, and pre-warmed instances.

### Question 23 — D

Answer: Configure `"functionTimeout": "00:10:00"` and `"logging": { "applicationInsights": { "samplingSettings": { "isEnabled": true, "excludedTypes": "Request;Exception" } } }` inside `host.json`. Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` in `host.json` applies globally across every function in the app. `host.json` governs global Function host behaviors such as execution timeout and Application Insights telemetry sampling exclusions across all functions in the app. Local study-map skill 1.11 (Create and Configure Azure Functions Apps, Hosting Plans, and host.json Settings), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` in `host.json` applies globally across every function in the app.
- **B:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` in `host.json` applies globally across every function in the app.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` in `host.json` applies globally across every function in the app.
- **D:** Correct. `host.json` governs global Function host behaviors such as execution timeout and Application Insights telemetry sampling exclusions across all functions in the app. In this scenario: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` in `host.json` applies globally across every function in the app.

### Question 24 — A, C

Answers: Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`; Apply `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` (or `[FixedDelayRetry]`) on the `[EventHubTrigger]` / `[TimerTrigger]` function. `[CosmosDBTrigger]` with a configured `LeaseContainerName` streams new/updated Cosmos documents via the Change Feed, while `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries transient failures on Event Hub triggers. Local study-map skill 1.12 (Implement Azure Functions Input and Output Bindings (Isolated Worker & Declarative Bindings)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Function-level retry attributes replay failed executions in-memory before advancing trigger checkpoints on Event Hubs and Timer triggers. In this scenario: `[CosmosDBTrigger]` with a configured `LeaseContainerName` streams new/updated Cosmos documents via the Change Feed, while `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries transient failures on Event Hub triggers.
- **B:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: `[CosmosDBTrigger]` with a configured `LeaseContainerName` streams new/updated Cosmos documents via the Change Feed, while `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries transient failures on Event Hub triggers.
- **C:** Correct. `CosmosDBTrigger` wraps the Change Feed Processor library and requires a lease container connection to coordinate partition checkpoints across scaled workers. In this scenario: `[CosmosDBTrigger]` with a configured `LeaseContainerName` streams new/updated Cosmos documents via the Change Feed, while `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries transient failures on Event Hub triggers.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `[CosmosDBTrigger]` with a configured `LeaseContainerName` streams new/updated Cosmos documents via the Change Feed, while `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries transient failures on Event Hub triggers.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `[CosmosDBTrigger]` with a configured `LeaseContainerName` streams new/updated Cosmos documents via the Change Feed, while `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` retries transient failures on Event Hub triggers.

### Question 25 — A

Answer: Specify a six-field NCRONTAB expression `{second} {minute} {hour} {day} {month} {day-of-week}` such as `"0 */15 9-17 * * 1-5"` on `[TimerTrigger]`. Azure Functions uses six-field NCRONTAB (`{second} {minute} {hour} {day} {month} {day-of-week}`), so `"0 */15 9-17 * * 1-5"` triggers on the zero second every 15 minutes on weekdays. Azure Functions `[TimerTrigger]` uses 6-field NCRONTAB (leading seconds field), unlike 5-field Unix cron. Local study-map skill 1.13 (Implement Function Triggers Using Cosmos DB/Blob Data Operations, NCRONTAB Timers, and Webhooks), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Azure Functions `[TimerTrigger]` uses 6-field NCRONTAB (leading seconds field), unlike 5-field Unix cron. In this scenario: Azure Functions uses six-field NCRONTAB (`{second} {minute} {hour} {day} {month} {day-of-week}`), so `"0 */15 9-17 * * 1-5"` triggers on the zero second every 15 minutes on weekdays.
- **B:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Azure Functions uses six-field NCRONTAB (`{second} {minute} {hour} {day} {month} {day-of-week}`), so `"0 */15 9-17 * * 1-5"` triggers on the zero second every 15 minutes on weekdays.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Azure Functions uses six-field NCRONTAB (`{second} {minute} {hour} {day} {month} {day-of-week}`), so `"0 */15 9-17 * * 1-5"` triggers on the zero second every 15 minutes on weekdays.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Azure Functions uses six-field NCRONTAB (`{second} {minute} {hour} {day} {month} {day-of-week}`), so `"0 */15 9-17 * * 1-5"` triggers on the zero second every 15 minutes on weekdays.

### Question 26 — B

Answer: Configure `[BlobTrigger(..., Source = BlobTriggerSource.EventGrid)]` with an Event Grid system topic subscription instead of default container-log polling. Setting `Source = BlobTriggerSource.EventGrid` backed by an Event Grid `BlobCreated` subscription switches `[BlobTrigger]` from periodic storage-log scanning to low-latency push activation. Event Grid-sourced blob triggers eliminate storage-log scan latency and work reliably on Blob-only / high-scale storage accounts. Local study-map skill 1.13 (Implement Function Triggers Using Cosmos DB/Blob Data Operations, NCRONTAB Timers, and Webhooks), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `Source = BlobTriggerSource.EventGrid` backed by an Event Grid `BlobCreated` subscription switches `[BlobTrigger]` from periodic storage-log scanning to low-latency push activation.
- **B:** Correct. Event Grid-sourced blob triggers eliminate storage-log scan latency and work reliably on Blob-only / high-scale storage accounts. In this scenario: Setting `Source = BlobTriggerSource.EventGrid` backed by an Event Grid `BlobCreated` subscription switches `[BlobTrigger]` from periodic storage-log scanning to low-latency push activation.
- **C:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Setting `Source = BlobTriggerSource.EventGrid` backed by an Event Grid `BlobCreated` subscription switches `[BlobTrigger]` from periodic storage-log scanning to low-latency push activation.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `Source = BlobTriggerSource.EventGrid` backed by an Event Grid `BlobCreated` subscription switches `[BlobTrigger]` from periodic storage-log scanning to low-latency push activation.

### Question 27 — A, D, F

Answers: Register `CosmosClient` as a process-wide singleton in dependency injection and choose a high-cardinality `PartitionKey` path (or up to 3-level `Hierarchical` subpartition paths) that distributes RU/s evenly; Use `container.CreateTransactionalBatch(new PartitionKey(pkValue))` to group multiple create/replace/upsert/delete operations atomically within the same logical partition; Pass `new ItemRequestOptions { IfMatchEtag = item.ETag }` on `ReplaceItemAsync` and catch `CosmosException` when `StatusCode == HttpStatusCode.PreconditionFailed` (412). Registering one singleton `CosmosClient`, grouping `/cartId` mutations in `CreateTransactionalBatch`, and enforcing `IfMatchEtag` optimistic concurrency (`412 PreconditionFailed`) satisfy all three requirements. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. `TransactionalBatch` guarantees ACID all-or-nothing execution serialized in one network round-trip, strictly scoped to a single logical partition key. In this scenario: Registering one singleton `CosmosClient`, grouping `/cartId` mutations in `CreateTransactionalBatch`, and enforcing `IfMatchEtag` optimistic concurrency (`412 PreconditionFailed`) satisfy all three requirements.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Registering one singleton `CosmosClient`, grouping `/cartId` mutations in `CreateTransactionalBatch`, and enforcing `IfMatchEtag` optimistic concurrency (`412 PreconditionFailed`) satisfy all three requirements.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Registering one singleton `CosmosClient`, grouping `/cartId` mutations in `CreateTransactionalBatch`, and enforcing `IfMatchEtag` optimistic concurrency (`412 PreconditionFailed`) satisfy all three requirements.
- **D:** Correct. Reusing one thread-safe `CosmosClient` avoids socket exhaustion, and hierarchical/high-cardinality partition keys prevent hot partitions and 20 GB single-partition caps. In this scenario: Registering one singleton `CosmosClient`, grouping `/cartId` mutations in `CreateTransactionalBatch`, and enforcing `IfMatchEtag` optimistic concurrency (`412 PreconditionFailed`) satisfy all three requirements.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Registering one singleton `CosmosClient`, grouping `/cartId` mutations in `CreateTransactionalBatch`, and enforcing `IfMatchEtag` optimistic concurrency (`412 PreconditionFailed`) satisfy all three requirements.
- **F:** Correct. Supplying `IfMatchEtag` enforces optimistic concurrency control so concurrent writers fail with HTTP 412 rather than silently overwriting updates. In this scenario: Registering one singleton `CosmosClient`, grouping `/cartId` mutations in `CreateTransactionalBatch`, and enforcing `IfMatchEtag` optimistic concurrency (`412 PreconditionFailed`) satisfy all three requirements.

### Question 28 — C

Answer: Call `await container.PatchItemAsync<Order>(id, new PartitionKey(pk), new[] { PatchOperation.Increment("/retryCount", 1), PatchOperation.Set("/lastStatus", "Queued") })`. `PatchItemAsync<Order>` with `PatchOperation.Increment` and `PatchOperation.Set` performs server-side partial document mutation in a single round-trip, saving bandwidth and Request Units. Partial Document Update (`PatchItemAsync`) mutates specific JSON paths server-side without reading, deserializing, and replacing the full document payload. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `PatchItemAsync<Order>` with `PatchOperation.Increment` and `PatchOperation.Set` performs server-side partial document mutation in a single round-trip, saving bandwidth and Request Units.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `PatchItemAsync<Order>` with `PatchOperation.Increment` and `PatchOperation.Set` performs server-side partial document mutation in a single round-trip, saving bandwidth and Request Units.
- **C:** Correct. Partial Document Update (`PatchItemAsync`) mutates specific JSON paths server-side without reading, deserializing, and replacing the full document payload. In this scenario: `PatchItemAsync<Order>` with `PatchOperation.Increment` and `PatchOperation.Set` performs server-side partial document mutation in a single round-trip, saving bandwidth and Request Units.
- **D:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `PatchItemAsync<Order>` with `PatchOperation.Increment` and `PatchOperation.Set` performs server-side partial document mutation in a single round-trip, saving bandwidth and Request Units.

### Question 29 — A

Answer: Add a `compositeIndexes` array matching the exact property sequence and sort directions (`ascending` / `descending`) in the container indexing policy JSON. Multi-property `ORDER BY` queries in Cosmos DB require a `compositeIndexes` definition matching the exact property sequence (`/category` `ascending`, `/createdUtc` `descending`). Cosmos DB for NoSQL requires a matching composite index whenever a SQL query specifies `ORDER BY` across two or more properties. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Cosmos DB for NoSQL requires a matching composite index whenever a SQL query specifies `ORDER BY` across two or more properties. In this scenario: Multi-property `ORDER BY` queries in Cosmos DB require a `compositeIndexes` definition matching the exact property sequence (`/category` `ascending`, `/createdUtc` `descending`).
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Multi-property `ORDER BY` queries in Cosmos DB require a `compositeIndexes` definition matching the exact property sequence (`/category` `ascending`, `/createdUtc` `descending`).
- **C:** Incorrect for this requirement. Excluding wildcard `/*` and indexing only queried filter paths dramatically cuts write Request Unit (RU) cost and index storage on write-heavy containers. Why the keyed choice wins: Multi-property `ORDER BY` queries in Cosmos DB require a `compositeIndexes` definition matching the exact property sequence (`/category` `ascending`, `/createdUtc` `descending`).
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Multi-property `ORDER BY` queries in Cosmos DB require a `compositeIndexes` definition matching the exact property sequence (`/category` `ascending`, `/createdUtc` `descending`).

### Question 30 — D

Answer: Use `Session` consistency (the default) and propagate `x-ms-session-token` (`RequestOptions.SessionToken`) across client/middle-tier hops to guarantee monotonic read-your-own-writes at half the read RU cost of `Strong`. Using `Session` consistency and round-tripping `SessionToken` (`x-ms-session-token`) across stateless API instances guarantees read-your-own-writes at half the RU cost of `Strong`. `Session` consistency guarantees read-your-writes, monotonic reads, and write-follows-reads within a session token at 50% of `Strong` / `BoundedStaleness` read RUs. Local study-map skill 2.2 (Select and Override Cosmos DB Consistency Levels and Session Tokens), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Using `Session` consistency and round-tripping `SessionToken` (`x-ms-session-token`) across stateless API instances guarantees read-your-own-writes at half the RU cost of `Strong`.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Using `Session` consistency and round-tripping `SessionToken` (`x-ms-session-token`) across stateless API instances guarantees read-your-own-writes at half the RU cost of `Strong`.
- **C:** Incorrect for this requirement. `Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds. Why the keyed choice wins: Using `Session` consistency and round-tripping `SessionToken` (`x-ms-session-token`) across stateless API instances guarantees read-your-own-writes at half the RU cost of `Strong`.
- **D:** Correct. `Session` consistency guarantees read-your-writes, monotonic reads, and write-follows-reads within a session token at 50% of `Strong` / `BoundedStaleness` read RUs. In this scenario: Using `Session` consistency and round-tripping `SessionToken` (`x-ms-session-token`) across stateless API instances guarantees read-your-own-writes at half the RU cost of `Strong`.

### Question 31 — D

Answer: Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency. `BoundedStaleness` enforces global total write order outside the primary region within explicit `K` version and `T` time bounds without the single-region restrictions of `Strong`. `Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds. Local study-map skill 2.2 (Select and Override Cosmos DB Consistency Levels and Session Tokens), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `BoundedStaleness` enforces global total write order outside the primary region within explicit `K` version and `T` time bounds without the single-region restrictions of `Strong`.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `BoundedStaleness` enforces global total write order outside the primary region within explicit `K` version and `T` time bounds without the single-region restrictions of `Strong`.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `BoundedStaleness` enforces global total write order outside the primary region within explicit `K` version and `T` time bounds without the single-region restrictions of `Strong`.
- **D:** Correct. `Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds. In this scenario: `BoundedStaleness` enforces global total write order outside the primary region within explicit `K` version and `T` time bounds without the single-region restrictions of `Strong`.

### Question 32 — C

Answer: Create the monitored container and a dedicated lease container → call GetChangeFeedProcessorBuilder<T> with processorName and delegate → attach WithInstanceName and WithLeaseContainer → call Build and StartAsync on the processor. Provisioning both monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and then calling `Build()` and `StartAsync()` starts distributed polling cleanly. Both monitored and lease containers must exist before configuring the builder with instance/lease metadata, building the processor, and starting polling. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. A processor cannot start before it is built or before its lease container exists. Why the keyed choice wins: Provisioning both monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and then calling `Build()` and `StartAsync()` starts distributed polling cleanly.
- **B:** Incorrect for this requirement. Builder options cannot be attached after Build(), and omitting the lease container causes startup failure. Why the keyed choice wins: Provisioning both monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and then calling `Build()` and `StartAsync()` starts distributed polling cleanly.
- **C:** Correct. Both monitored and lease containers must exist before configuring the builder with instance/lease metadata, building the processor, and starting polling. In this scenario: Provisioning both monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and then calling `Build()` and `StartAsync()` starts distributed polling cleanly.
- **D:** Incorrect for this requirement. Builder method order is inverted, and using a separate dedicated lease container avoids RU contention and partition-key mismatches. Why the keyed choice wins: Provisioning both monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and then calling `Build()` and `StartAsync()` starts distributed polling cleanly.

### Question 33 — A, D

Answers: Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay; Use Change Feed `AllVersionsAndDeletes` mode (or soft-delete flag items with short TTL in `LatestVersion` mode) because default `LatestVersion` change feed omits hard-deleted items. Assigning each microservice a distinct `processorName` gives every service its own independent cursor, and using `AllVersionsAndDeletes` mode (or soft-delete `isDeleted` + TTL) captures deletions omitted by `LatestVersion`. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. In Change Feed Processor, `processorName` acts like an Event Hubs consumer group: distinct names receive independent copies of every insert/update, while identical names load-balance partitions. In this scenario: Assigning each microservice a distinct `processorName` gives every service its own independent cursor, and using `AllVersionsAndDeletes` mode (or soft-delete `isDeleted` + TTL) captures deletions omitted by `LatestVersion`.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Assigning each microservice a distinct `processorName` gives every service its own independent cursor, and using `AllVersionsAndDeletes` mode (or soft-delete `isDeleted` + TTL) captures deletions omitted by `LatestVersion`.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Assigning each microservice a distinct `processorName` gives every service its own independent cursor, and using `AllVersionsAndDeletes` mode (or soft-delete `isDeleted` + TTL) captures deletions omitted by `LatestVersion`.
- **D:** Correct. Standard `LatestVersion` change feed emits only inserts and updates of current items; hard deletes require `AllVersionsAndDeletes` or soft-delete Tombstone items + TTL. In this scenario: Assigning each microservice a distinct `processorName` gives every service its own independent cursor, and using `AllVersionsAndDeletes` mode (or soft-delete `isDeleted` + TTL) captures deletions omitted by `LatestVersion`.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Assigning each microservice a distinct `processorName` gives every service its own independent cursor, and using `AllVersionsAndDeletes` mode (or soft-delete `isDeleted` + TTL) captures deletions omitted by `LatestVersion`.

### Question 34 — A

Answer: Enable container `DefaultTimeToLive = -1` (or positive seconds) and set item `ttl = 600` so Cosmos DB purges expired items automatically using background RU capacity. Setting container `DefaultTimeToLive = -1` activates item-level TTL evaluation while keeping documents without a `ttl` property indefinitely. Container TTL must be non-null (`-1` or `>0`) for per-item `ttl` seconds to take effect; setting `DefaultTimeToLive = null` ignores item-level `ttl`. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Container TTL must be non-null (`-1` or `>0`) for per-item `ttl` seconds to take effect; setting `DefaultTimeToLive = null` ignores item-level `ttl`. In this scenario: Setting container `DefaultTimeToLive = -1` activates item-level TTL evaluation while keeping documents without a `ttl` property indefinitely.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` activates item-level TTL evaluation while keeping documents without a `ttl` property indefinitely.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` activates item-level TTL evaluation while keeping documents without a `ttl` property indefinitely.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting container `DefaultTimeToLive = -1` activates item-level TTL evaluation while keeping documents without a `ttl` property indefinitely.

### Question 35 — A

Answer: Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`). `SetHttpHeadersAsync(BlobHttpHeaders)` sets standard HTTP system properties like `ContentType`, whereas `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` user metadata pairs. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. In this scenario: `SetHttpHeadersAsync(BlobHttpHeaders)` sets standard HTTP system properties like `ContentType`, whereas `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` user metadata pairs.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` sets standard HTTP system properties like `ContentType`, whereas `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` user metadata pairs.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` sets standard HTTP system properties like `ContentType`, whereas `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` user metadata pairs.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `SetHttpHeadersAsync(BlobHttpHeaders)` sets standard HTTP system properties like `ContentType`, whereas `SetMetadataAsync` writes C#-identifier-valid `x-ms-meta-*` user metadata pairs.

### Question 36 — D

Answer: Attach searchable key-value `Tags` (`SetTagsAsync` / `BlobUploadOptions.Tags`) and query across containers with `FindBlobsByTagsAsync("@container = 'docs' AND status = 'pending'")`. Blob `Metadata` is not indexed and requires full enumeration; storing searchable `Tags` (`SetTagsAsync`) lets apps query `FindBlobsByTagsAsync` server-side across containers in milliseconds. Blob Index Tags are indexed natively by Azure Storage for server-side filtering, whereas `Metadata` is not searchable without listing every blob. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Blob `Metadata` is not indexed and requires full enumeration; storing searchable `Tags` (`SetTagsAsync`) lets apps query `FindBlobsByTagsAsync` server-side across containers in milliseconds.
- **B:** Incorrect for this requirement. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. Why the keyed choice wins: Blob `Metadata` is not indexed and requires full enumeration; storing searchable `Tags` (`SetTagsAsync`) lets apps query `FindBlobsByTagsAsync` server-side across containers in milliseconds.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Blob `Metadata` is not indexed and requires full enumeration; storing searchable `Tags` (`SetTagsAsync`) lets apps query `FindBlobsByTagsAsync` server-side across containers in milliseconds.
- **D:** Correct. Blob Index Tags are indexed natively by Azure Storage for server-side filtering, whereas `Metadata` is not searchable without listing every blob. In this scenario: Blob `Metadata` is not indexed and requires full enumeration; storing searchable `Tags` (`SetTagsAsync`) lets apps query `FindBlobsByTagsAsync` server-side across containers in milliseconds.

### Question 37 — D

Answer: Call `await blobClient.CreateSnapshotAsync()` for explicit point-in-time read-only checkpoints or enable account-level Blob Versioning so every `UploadAsync` overwrite retains an immutable `VersionId`. Enabling account-level Blob Versioning automatically preserves prior blob states under distinct `VersionId` values on every overwrite, whereas snapshots require explicit `CreateSnapshotAsync()` calls. Snapshots capture explicit developer-triggered checkpoints, whereas Blob Versioning automatically preserves prior state on every overwrite or delete. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Enabling account-level Blob Versioning automatically preserves prior blob states under distinct `VersionId` values on every overwrite, whereas snapshots require explicit `CreateSnapshotAsync()` calls.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Enabling account-level Blob Versioning automatically preserves prior blob states under distinct `VersionId` values on every overwrite, whereas snapshots require explicit `CreateSnapshotAsync()` calls.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Enabling account-level Blob Versioning automatically preserves prior blob states under distinct `VersionId` values on every overwrite, whereas snapshots require explicit `CreateSnapshotAsync()` calls.
- **D:** Correct. Snapshots capture explicit developer-triggered checkpoints, whereas Blob Versioning automatically preserves prior state on every overwrite or delete. In this scenario: Enabling account-level Blob Versioning automatically preserves prior blob states under distinct `VersionId` values on every overwrite, whereas snapshots require explicit `CreateSnapshotAsync()` calls.

### Question 38 — B

Answer: Use `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` (15–60 seconds or `-1` infinite) and pass `LeaseId` inside `BlobRequestConditions` on subsequent writes/deletes. Acquiring a finite 15–60 second lock via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` enforces exclusive blob write access. Blob leases grant exclusive write/delete locks (`15` to `60` seconds or infinite `-1`) so competing workers immediately receive `412 LeaseIdMissing/Mismatch`. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Acquiring a finite 15–60 second lock via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` enforces exclusive blob write access.
- **B:** Correct. Blob leases grant exclusive write/delete locks (`15` to `60` seconds or infinite `-1`) so competing workers immediately receive `412 LeaseIdMissing/Mismatch`. In this scenario: Acquiring a finite 15–60 second lock via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` enforces exclusive blob write access.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Acquiring a finite 15–60 second lock via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` enforces exclusive blob write access.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Acquiring a finite 15–60 second lock via `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and passing `LeaseId` in `BlobRequestConditions` enforces exclusive blob write access.

### Question 39 — A

Answer: Invoke `BlobClient.StartCopyFromUriAsync(sourceSasUri)` to trigger asynchronous server-side blob copy and inspect `CopyStatus` without streaming bytes through the client VM. `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` tracks completion. `StartCopyFromUriAsync` instructs Azure Storage fabric to copy blobs asynchronously server-to-server using a readable source URI/SAS. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. `StartCopyFromUriAsync` instructs Azure Storage fabric to copy blobs asynchronously server-to-server using a readable source URI/SAS. In this scenario: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` tracks completion.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` tracks completion.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` tracks completion.
- **D:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `BlobClient.StartCopyFromUriAsync(sourceSasUri)` triggers asynchronous server-to-server copy across Azure Storage fabric while `CopyStatus` tracks completion.

### Question 40 — B

Answer: Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`. Setting `Resource = "b"`, `BlobContainerName`, `BlobName`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` scopes the SAS strictly to that single blob. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName`, `BlobName`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` scopes the SAS strictly to that single blob.
- **B:** Correct. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. In this scenario: Setting `Resource = "b"`, `BlobContainerName`, `BlobName`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` scopes the SAS strictly to that single blob.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName`, `BlobName`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` scopes the SAS strictly to that single blob.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `Resource = "b"`, `BlobContainerName`, `BlobName`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `BlobSasPermissions.Read` scopes the SAS strictly to that single blob.

### Question 41 — C, D

Answers: Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage; Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob). Locked time-based Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention, and `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` restores <10 GB archived blobs rapidly. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Locked time-based Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention, and `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` restores <10 GB archived blobs rapidly.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Locked time-based Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention, and `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` restores <10 GB archived blobs rapidly.
- **C:** Correct. Time-based locked retention and legal holds block modification and deletion even by Storage Account Owners until retention expires and holds clear. In this scenario: Locked time-based Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention, and `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` restores <10 GB archived blobs rapidly.
- **D:** Correct. `SetAccessTierAsync` (or copy-to-Hot) initiates Archive rehydration; `RehydratePriority.High` prioritizes restoration (often under 1 hour for <10 GB blobs). In this scenario: Locked time-based Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention, and `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` restores <10 GB archived blobs rapidly.
- **E:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Locked time-based Version-Level Immutability Policies (or `LegalHold`) enforce WORM retention, and `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` restores <10 GB archived blobs rapidly.

### Question 42 — B

Answer: Verify the blob is currently in the Archive access tier → call SetAccessTier (or CopyBlob) targeting Hot or Cool with Standard or High rehydrate priority → poll ArchiveStatus until rehydration completes and tier updates → download the blob content. Confirming `Archive` status, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with a rehydrate priority, polling `ArchiveStatus` until online, and then downloading avoids `409 BlobArchived`. Archived blobs are offline and unreadable directly; changing tier or copying to Hot/Cool initiates asynchronous rehydration that must finish before download. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Calling Download directly on an Archive-tier blob immediately throws HTTP 409 Conflict (`BlobArchived`). Why the keyed choice wins: Confirming `Archive` status, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with a rehydrate priority, polling `ArchiveStatus` until online, and then downloading avoids `409 BlobArchived`.
- **B:** Correct. Archived blobs are offline and unreadable directly; changing tier or copying to Hot/Cool initiates asynchronous rehydration that must finish before download. In this scenario: Confirming `Archive` status, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with a rehydrate priority, polling `ArchiveStatus` until online, and then downloading avoids `409 BlobArchived`.
- **C:** Incorrect for this requirement. User metadata does not trigger storage rehydration, and setting tier back to Archive keeps the blob offline. Why the keyed choice wins: Confirming `Archive` status, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with a rehydrate priority, polling `ArchiveStatus` until online, and then downloading avoids `409 BlobArchived`.
- **D:** Incorrect for this requirement. Leasing does not bring an offline Archive blob online; rehydration to Hot or Cool must complete before any read succeeds. Why the keyed choice wins: Confirming `Archive` status, calling `SetAccessTier` (or `CopyBlob`) targeting `Hot`/`Cool` with a rehydrate priority, polling `ArchiveStatus` until online, and then downloading avoids `409 BlobArchived`.

### Question 43 — A, E

Answers: Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps; Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`. `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public clients without embedded secrets, and calling `AcquireTokenSilent` first with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens seamlessly. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. MSAL refreshes cached tokens transparently during `AcquireTokenSilent`; prompting interactively on every call degrades UX and hits rate limits. In this scenario: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public clients without embedded secrets, and calling `AcquireTokenSilent` first with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens seamlessly.
- **B:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public clients without embedded secrets, and calling `AcquireTokenSilent` first with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens seamlessly.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public clients without embedded secrets, and calling `AcquireTokenSilent` first with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens seamlessly.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public clients without embedded secrets, and calling `AcquireTokenSilent` first with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens seamlessly.
- **E:** Correct. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. In this scenario: `PublicClientApplicationBuilder` with Authorization Code + PKCE secures public clients without embedded secrets, and calling `AcquireTokenSilent` first with `MsalUiRequiredException` fallback to `AcquireTokenInteractive` refreshes cached tokens seamlessly.

### Question 44 — A

Answer: Use `ConfidentialClientApplicationBuilder` authenticated with a client certificate (or workload identity assertion) calling `AcquireTokenForClient(new[] { "api://.../.default" })` for headless background daemons. `ConfidentialClientApplicationBuilder` using `WithCertificate` and `AcquireTokenForClient(new[] { "api://pricing/.default" })` executes the OAuth 2.0 Client Credentials flow against pre-consented app permissions. Daemon apps without a signed-in user use OAuth 2.0 Client Credentials flow and must request the `.default` scope for pre-consented application permissions. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Daemon apps without a signed-in user use OAuth 2.0 Client Credentials flow and must request the `.default` scope for pre-consented application permissions. In this scenario: `ConfidentialClientApplicationBuilder` using `WithCertificate` and `AcquireTokenForClient(new[] { "api://pricing/.default" })` executes the OAuth 2.0 Client Credentials flow against pre-consented app permissions.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` using `WithCertificate` and `AcquireTokenForClient(new[] { "api://pricing/.default" })` executes the OAuth 2.0 Client Credentials flow against pre-consented app permissions.
- **C:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` using `WithCertificate` and `AcquireTokenForClient(new[] { "api://pricing/.default" })` executes the OAuth 2.0 Client Credentials flow against pre-consented app permissions.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `ConfidentialClientApplicationBuilder` using `WithCertificate` and `AcquireTokenForClient(new[] { "api://pricing/.default" })` executes the OAuth 2.0 Client Credentials flow against pre-consented app permissions.

### Question 45 — C

Answer: Register the middle-tier API scope and delegated Graph permissions in Entra ID → validate the incoming user token → call ConfidentialClientApplication.AcquireTokenOnBehalfOf(UserAssertion) → invoke Microsoft Graph with the exchanged token. Registering the middle-tier API scope + delegated Graph permissions, validating the incoming bearer token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated identity safely. The middle-tier API must validate the caller token first and exchange it as a UserAssertion via ConfidentialClientApplication before calling Graph as that user. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. OBO requires a confidential client with a secret or certificate and `AcquireTokenOnBehalfOf`, not app-only `AcquireTokenForClient`. Why the keyed choice wins: Registering the middle-tier API scope + delegated Graph permissions, validating the incoming bearer token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated identity safely.
- **B:** Incorrect for this requirement. Graph rejects unauthenticated requests, and OBO cannot run before app registration and incoming token validation. Why the keyed choice wins: Registering the middle-tier API scope + delegated Graph permissions, validating the incoming bearer token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated identity safely.
- **C:** Correct. The middle-tier API must validate the caller token first and exchange it as a UserAssertion via ConfidentialClientApplication before calling Graph as that user. In this scenario: Registering the middle-tier API scope + delegated Graph permissions, validating the incoming bearer token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated identity safely.
- **D:** Incorrect for this requirement. A token whose audience (`aud`) is the custom middle-tier API is rejected by Microsoft Graph; OBO exchange must occur first. Why the keyed choice wins: Registering the middle-tier API scope + delegated Graph permissions, validating the incoming bearer token, calling `AcquireTokenOnBehalfOf(UserAssertion)`, and invoking Graph preserves delegated identity safely.

### Question 46 — D

Answer: Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`). Setting the unauthenticated request action to `Return HTTP 401 Unauthorized` instead of `302 Redirect` lets programmatic REST/mobile clients detect token expiry and refresh bearer headers cleanly. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting the unauthenticated request action to `Return HTTP 401 Unauthorized` instead of `302 Redirect` lets programmatic REST/mobile clients detect token expiry and refresh bearer headers cleanly.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting the unauthenticated request action to `Return HTTP 401 Unauthorized` instead of `302 Redirect` lets programmatic REST/mobile clients detect token expiry and refresh bearer headers cleanly.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting the unauthenticated request action to `Return HTTP 401 Unauthorized` instead of `302 Redirect` lets programmatic REST/mobile clients detect token expiry and refresh bearer headers cleanly.
- **D:** Correct. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. In this scenario: Setting the unauthenticated request action to `Return HTTP 401 Unauthorized` instead of `302 Redirect` lets programmatic REST/mobile clients detect token expiry and refresh bearer headers cleanly.

### Question 47 — D

Answer: Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation. Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations` authority) excludes personal accounts, while custom token validation checks `tid` / `iss` against onboarded partner tenants. Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations` authority) excludes personal accounts, while custom token validation checks `tid` / `iss` against onboarded partner tenants.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations` authority) excludes personal accounts, while custom token validation checks `tid` / `iss` against onboarded partner tenants.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations` authority) excludes personal accounts, while custom token validation checks `tid` / `iss` against onboarded partner tenants.
- **D:** Correct. Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`. In this scenario: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations` authority) excludes personal accounts, while custom token validation checks `tid` / `iss` against onboarded partner tenants.

### Question 48 — A

Answer: Bind a Service SAS to a container/queue/table Stored Access Policy (`SignedIdentifier`, omitting inline start/expiry/permissions) so compromised tokens can be revoked instantly by modifying or deleting the policy. Inline Service SAS tokens can only be revoked by rotating the signing storage account key; binding the SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets operators revoke it instantly by deleting or editing that policy. Up to 5 Stored Access Policies per container allow instant SAS revocation without rotating storage account keys; Note that User Delegation SAS uses key revocation instead of Stored Access Policies. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Up to 5 Stored Access Policies per container allow instant SAS revocation without rotating storage account keys; Note that User Delegation SAS uses key revocation instead of Stored Access Policies. In this scenario: Inline Service SAS tokens can only be revoked by rotating the signing storage account key; binding the SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets operators revoke it instantly by deleting or editing that policy.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Inline Service SAS tokens can only be revoked by rotating the signing storage account key; binding the SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets operators revoke it instantly by deleting or editing that policy.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Inline Service SAS tokens can only be revoked by rotating the signing storage account key; binding the SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets operators revoke it instantly by deleting or editing that policy.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Inline Service SAS tokens can only be revoked by rotating the signing storage account key; binding the SAS to a container `StoredAccessPolicy` (`SignedIdentifier`) lets operators revoke it instantly by deleting or editing that policy.

### Question 49 — B

Answer: Mint a short-lived HTTPS-only (`SasProtocol.HttpsOnly`) User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` instead of Account or Service SAS signed with storage account keys. User Delegation SAS is signed by Microsoft Entra ID credentials (`GetUserDelegationKeyAsync`) rather than storage account keys, so it works cleanly when `allowSharedKeyAccess` is disabled. User Delegation SAS eliminates shared storage account keys, enforces Entra RBAC, and automatically invalidates if the signing identity loses permissions. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: User Delegation SAS is signed by Microsoft Entra ID credentials (`GetUserDelegationKeyAsync`) rather than storage account keys, so it works cleanly when `allowSharedKeyAccess` is disabled.
- **B:** Correct. User Delegation SAS eliminates shared storage account keys, enforces Entra RBAC, and automatically invalidates if the signing identity loses permissions. In this scenario: User Delegation SAS is signed by Microsoft Entra ID credentials (`GetUserDelegationKeyAsync`) rather than storage account keys, so it works cleanly when `allowSharedKeyAccess` is disabled.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: User Delegation SAS is signed by Microsoft Entra ID credentials (`GetUserDelegationKeyAsync`) rather than storage account keys, so it works cleanly when `allowSharedKeyAccess` is disabled.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: User Delegation SAS is signed by Microsoft Entra ID credentials (`GetUserDelegationKeyAsync`) rather than storage account keys, so it works cleanly when `allowSharedKeyAccess` is disabled.

### Question 50 — A, E

Answers: Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`; Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses. Requesting least-privilege `User.Read.All` with `$select` + `PageIterator<T>` minimizes page payload size, and bundling up to 20 sub-requests in `BatchRequestContentCollection` (`/$batch`) while honoring `Retry-After` curbs throttling. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Graph JSON batching (`/$batch`) bundles up to 20 sub-requests per round-trip, while built-in SDK retry middleware respects `Retry-After`. In this scenario: Requesting least-privilege `User.Read.All` with `$select` + `PageIterator<T>` minimizes page payload size, and bundling up to 20 sub-requests in `BatchRequestContentCollection` (`/$batch`) while honoring `Retry-After` curbs throttling.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Requesting least-privilege `User.Read.All` with `$select` + `PageIterator<T>` minimizes page payload size, and bundling up to 20 sub-requests in `BatchRequestContentCollection` (`/$batch`) while honoring `Retry-After` curbs throttling.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Requesting least-privilege `User.Read.All` with `$select` + `PageIterator<T>` minimizes page payload size, and bundling up to 20 sub-requests in `BatchRequestContentCollection` (`/$batch`) while honoring `Retry-After` curbs throttling.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Requesting least-privilege `User.Read.All` with `$select` + `PageIterator<T>` minimizes page payload size, and bundling up to 20 sub-requests in `BatchRequestContentCollection` (`/$batch`) while honoring `Retry-After` curbs throttling.
- **E:** Correct. Microsoft Graph enforces least-privilege consent scopes, trims payload size with `$select`, and paginates `@odata.nextLink` cleanly through `PageIterator<T>`. In this scenario: Requesting least-privilege `User.Read.All` with `$select` + `PageIterator<T>` minimizes page payload size, and bundling up to 20 sub-requests in `BatchRequestContentCollection` (`/$batch`) while honoring `Retry-After` curbs throttling.

### Question 51 — B

Answer: Call `await graphClient.Users.GetAsync(rc => { rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }; rc.QueryParameters.Filter = "accountEnabled eq true"; })`. Configuring `rc.QueryParameters.Select` and `rc.QueryParameters.Filter = "accountEnabled eq true"` in Graph SDK v5 applies server-side `$select` and `$filter` projection. In Microsoft Graph .NET SDK v5, `$select` and `$filter` query parameters reduce payload size and network transfer on collection endpoints. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Configuring `rc.QueryParameters.Select` and `rc.QueryParameters.Filter = "accountEnabled eq true"` in Graph SDK v5 applies server-side `$select` and `$filter` projection.
- **B:** Correct. In Microsoft Graph .NET SDK v5, `$select` and `$filter` query parameters reduce payload size and network transfer on collection endpoints. In this scenario: Configuring `rc.QueryParameters.Select` and `rc.QueryParameters.Filter = "accountEnabled eq true"` in Graph SDK v5 applies server-side `$select` and `$filter` projection.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Configuring `rc.QueryParameters.Select` and `rc.QueryParameters.Filter = "accountEnabled eq true"` in Graph SDK v5 applies server-side `$select` and `$filter` projection.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Configuring `rc.QueryParameters.Select` and `rc.QueryParameters.Filter = "accountEnabled eq true"` in Graph SDK v5 applies server-side `$select` and `$filter` projection.

### Question 52 — C

Answer: Call `await confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` inside the middle-tier API. `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` performs the OBO exchange preserving user context. OAuth 2.0 On-Behalf-Of (`AcquireTokenOnBehalfOf`) exchanges an incoming user access token for a downstream API token while preserving delegated user identity and consent. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` performs the OBO exchange preserving user context.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` performs the OBO exchange preserving user context.
- **C:** Correct. OAuth 2.0 On-Behalf-Of (`AcquireTokenOnBehalfOf`) exchanges an incoming user access token for a downstream API token while preserving delegated user identity and consent. In this scenario: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` performs the OBO exchange preserving user context.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` performs the OBO exchange preserving user context.

### Question 53 — A

Answer: Wire `options.Connect(new Uri(endpoint), cred).ConfigureKeyVault(kv => kv.SetCredential(cred))` so App Configuration resolves Key Vault reference items using the app identity. Calling `.ConfigureKeyVault(kv => kv.SetCredential(cred))` supplies the `TokenCredential` needed to resolve Key Vault URI pointers stored in App Configuration. App Configuration stores only the Key Vault secret URI metadata; client code still requires `ConfigureKeyVault` credentials with `Key Vault Secrets User` rights on the target vault. Local study-map skill 3.5 (Manage Feature Flags, Labels, Sentinel Dynamic Refresh, and Key Vault References in Azure App Configuration), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. App Configuration stores only the Key Vault secret URI metadata; client code still requires `ConfigureKeyVault` credentials with `Key Vault Secrets User` rights on the target vault. In this scenario: Calling `.ConfigureKeyVault(kv => kv.SetCredential(cred))` supplies the `TokenCredential` needed to resolve Key Vault URI pointers stored in App Configuration.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Calling `.ConfigureKeyVault(kv => kv.SetCredential(cred))` supplies the `TokenCredential` needed to resolve Key Vault URI pointers stored in App Configuration.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Calling `.ConfigureKeyVault(kv => kv.SetCredential(cred))` supplies the `TokenCredential` needed to resolve Key Vault URI pointers stored in App Configuration.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Calling `.ConfigureKeyVault(kv => kv.SetCredential(cred))` supplies the `TokenCredential` needed to resolve Key Vault URI pointers stored in App Configuration.

### Question 54 — D

Answer: Store environment-labeled settings and `.appconfig.featureflag/*` entries in Azure App Configuration, register `AddAzureAppConfiguration` + `AddFeatureManagement`, and watch a single `Sentinel` key with `refreshAll: true`. Watching a single `Sentinel` key with `refreshAll: true` and incrementing that sentinel only after all four keys are saved ensures atomic batch configuration reloads. Updating one sentinel key after finishing multi-key edits prevents apps from reading half-updated configuration state mid-rollout. Local study-map skill 3.5 (Manage Feature Flags, Labels, Sentinel Dynamic Refresh, and Key Vault References in Azure App Configuration), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Watching a single `Sentinel` key with `refreshAll: true` and incrementing that sentinel only after all four keys are saved ensures atomic batch configuration reloads.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Watching a single `Sentinel` key with `refreshAll: true` and incrementing that sentinel only after all four keys are saved ensures atomic batch configuration reloads.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Watching a single `Sentinel` key with `refreshAll: true` and incrementing that sentinel only after all four keys are saved ensures atomic batch configuration reloads.
- **D:** Correct. Updating one sentinel key after finishing multi-key edits prevents apps from reading half-updated configuration state mid-rollout. In this scenario: Watching a single `Sentinel` key with `refreshAll: true` and incrementing that sentinel only after all four keys are saved ensures atomic batch configuration reloads.

### Question 55 — C, D

Answers: Use `SecretClient` (`Azure.Security.KeyVault.Secrets`) for connection strings/tokens, `KeyClient` / `CryptographyClient` (`Azure.Security.KeyVault.Keys`) for RSA/EC wrap-unwrap-sign, and `CertificateClient` for X.509 lifecycle; Enable Soft Delete (mandatory on new vaults, 7–90 days) plus Purge Protection on Azure Key Vault so neither accidental deletion nor malicious principals can permanently destroy keys before retention expires. Using `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` separates secret/key/cert operations cleanly, while enabling Soft Delete + Purge Protection blocks permanent deletion throughout the 90-day retention period. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Using `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` separates secret/key/cert operations cleanly, while enabling Soft Delete + Purge Protection blocks permanent deletion throughout the 90-day retention period.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Using `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` separates secret/key/cert operations cleanly, while enabling Soft Delete + Purge Protection blocks permanent deletion throughout the 90-day retention period.
- **C:** Correct. Azure Key Vault SDK v4 splits secrets, cryptographic keys, and X.509 certificates into dedicated clients and RBAC data-plane roles (`Key Vault Secrets User`, `Crypto User`, `Certificates User`). In this scenario: Using `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` separates secret/key/cert operations cleanly, while enabling Soft Delete + Purge Protection blocks permanent deletion throughout the 90-day retention period.
- **D:** Correct. Soft Delete allows recovery via `StartRecoverDeletedSecretAsync`, while Purge Protection blocks permanent `PurgeDeletedSecretAsync` calls during retention. In this scenario: Using `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` separates secret/key/cert operations cleanly, while enabling Soft Delete + Purge Protection blocks permanent deletion throughout the 90-day retention period.
- **E:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Using `SecretClient`, `KeyClient`/`CryptographyClient`, and `CertificateClient` separates secret/key/cert operations cleanly, while enabling Soft Delete + Purge Protection blocks permanent deletion throughout the 90-day retention period.

### Question 56 — B

Answer: Instantiate `new CryptographyClient(keyVaultKey.Id, new DefaultAzureCredential())` and invoke `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync(...)`. `CryptographyClient` (`Azure.Security.KeyVault.Keys.Cryptography`) calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` wraps and unwraps symmetric DEKs without sending bulk payloads to Key Vault. Envelope encryption keeps bulk data encryption keys (`DEK`) wrapped by hardware/software-protected Key Vault KEKs without sending large payloads through Key Vault. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `CryptographyClient` (`Azure.Security.KeyVault.Keys.Cryptography`) calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` wraps and unwraps symmetric DEKs without sending bulk payloads to Key Vault.
- **B:** Correct. Envelope encryption keeps bulk data encryption keys (`DEK`) wrapped by hardware/software-protected Key Vault KEKs without sending large payloads through Key Vault. In this scenario: `CryptographyClient` (`Azure.Security.KeyVault.Keys.Cryptography`) calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` wraps and unwraps symmetric DEKs without sending bulk payloads to Key Vault.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `CryptographyClient` (`Azure.Security.KeyVault.Keys.Cryptography`) calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` wraps and unwraps symmetric DEKs without sending bulk payloads to Key Vault.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `CryptographyClient` (`Azure.Security.KeyVault.Keys.Cryptography`) calling `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` wraps and unwraps symmetric DEKs without sending bulk payloads to Key Vault.

### Question 57 — A

Answer: Instantiate `new DefaultAzureCredential()` (or explicit `ManagedIdentityCredential(clientId)` for user-assigned identities in production) so identical code authenticates via Azure CLI / Visual Studio locally and Managed Identity in Azure. `DefaultAzureCredential` probes local developer toolchains (`VisualStudioCredential`, `AzureCliCredential`) during development and switches automatically to `ManagedIdentityCredential` in Azure. `DefaultAzureCredential` chains developer workstation credentials locally and IMDS Managed Identity in Azure; passing `managedIdentityClientId` is required when selecting a specific user-assigned identity. Local study-map skill 3.7 (Implement System-Assigned and User-Assigned Managed Identities and DefaultAzureCredential), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. `DefaultAzureCredential` chains developer workstation credentials locally and IMDS Managed Identity in Azure; passing `managedIdentityClientId` is required when selecting a specific user-assigned identity. In this scenario: `DefaultAzureCredential` probes local developer toolchains (`VisualStudioCredential`, `AzureCliCredential`) during development and switches automatically to `ManagedIdentityCredential` in Azure.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `DefaultAzureCredential` probes local developer toolchains (`VisualStudioCredential`, `AzureCliCredential`) during development and switches automatically to `ManagedIdentityCredential` in Azure.
- **C:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `DefaultAzureCredential` probes local developer toolchains (`VisualStudioCredential`, `AzureCliCredential`) during development and switches automatically to `ManagedIdentityCredential` in Azure.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `DefaultAzureCredential` probes local developer toolchains (`VisualStudioCredential`, `AzureCliCredential`) during development and switches automatically to `ManagedIdentityCredential` in Azure.

### Question 58 — B

Answer: Instantiate `new DefaultAzureCredential(new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId })` (or set `AZURE_CLIENT_ID`). Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) tells IMDS exactly which user-assigned identity token to mint. When a host has multiple user-assigned managed identities attached, IMDS rejects ambiguous token requests unless the target `clientId` (or resource ID) is specified. Local study-map skill 3.7 (Implement System-Assigned and User-Assigned Managed Identities and DefaultAzureCredential), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) tells IMDS exactly which user-assigned identity token to mint.
- **B:** Correct. When a host has multiple user-assigned managed identities attached, IMDS rejects ambiguous token requests unless the target `clientId` (or resource ID) is specified. In this scenario: Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) tells IMDS exactly which user-assigned identity token to mint.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) tells IMDS exactly which user-assigned identity token to mint.
- **D:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Passing `ManagedIdentityClientId = userAssignedClientId` in `DefaultAzureCredentialOptions` (or setting `AZURE_CLIENT_ID`) tells IMDS exactly which user-assigned identity token to mint.

### Question 59 — C, E

Answers: Query Workspace-based Application Insights (`AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces` or classic `requests`/`dependencies`/`exceptions`) joining on `OperationId` (`operation_Id`) to reconstruct end-to-end distributed transactions; Run `AppRequests | where ResultCode == "500" | join kind=inner (AppDependencies | where Success == false) on OperationId | project TimeGenerated, Name, Target, DependencyType, ResultCode1`. Propagating W3C `OperationId` across `AppRequests`/`AppDependencies`/`AppExceptions` and executing an inner KQL `join` between failed `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` on `OperationId` pinpoints root causes. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Propagating W3C `OperationId` across `AppRequests`/`AppDependencies`/`AppExceptions` and executing an inner KQL `join` between failed `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` on `OperationId` pinpoints root causes.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Propagating W3C `OperationId` across `AppRequests`/`AppDependencies`/`AppExceptions` and executing an inner KQL `join` between failed `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` on `OperationId` pinpoints root causes.
- **C:** Correct. W3C Trace-Context propagates `traceparent` into `operation_Id` across services so KQL joins pinpoint exact failing downstream dependencies. In this scenario: Propagating W3C `OperationId` across `AppRequests`/`AppDependencies`/`AppExceptions` and executing an inner KQL `join` between failed `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` on `OperationId` pinpoints root causes.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Propagating W3C `OperationId` across `AppRequests`/`AppDependencies`/`AppExceptions` and executing an inner KQL `join` between failed `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` on `OperationId` pinpoints root causes.
- **E:** Correct. Joining `AppRequests` and `AppDependencies` on `OperationId` isolates which exact downstream SQL, HTTP, or Storage dependency triggered HTTP 500 responses. In this scenario: Propagating W3C `OperationId` across `AppRequests`/`AppDependencies`/`AppExceptions` and executing an inner KQL `join` between failed `AppRequests` (`ResultCode == "500"`) and failed `AppDependencies` on `OperationId` pinpoints root causes.

### Question 60 — A

Answer: Run `AppRequests | where TimeGenerated > ago(1h) | summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)`. Grouping `AppRequests` over `ago(1h)` with `summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` computes error counts and p95 latency per 5-minute bucket. KQL `countif` and `percentile(..., 95)` grouped by `bin(TimeGenerated, 5m)` quantify error spikes and tail latency per operation over fixed time buckets. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. KQL `countif` and `percentile(..., 95)` grouped by `bin(TimeGenerated, 5m)` quantify error spikes and tail latency per operation over fixed time buckets. In this scenario: Grouping `AppRequests` over `ago(1h)` with `summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` computes error counts and p95 latency per 5-minute bucket.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Grouping `AppRequests` over `ago(1h)` with `summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` computes error counts and p95 latency per 5-minute bucket.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Grouping `AppRequests` over `ago(1h)` with `summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` computes error counts and p95 latency per 5-minute bucket.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Grouping `AppRequests` over `ago(1h)` with `summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` computes error counts and p95 latency per 5-minute bucket.

### Question 61 — B

Answer: Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits. Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry `TracerProvider`) followed by a short delay before process exit drains the in-memory telemetry buffer to the ingestion endpoint. Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry `TracerProvider`) followed by a short delay before process exit drains the in-memory telemetry buffer to the ingestion endpoint.
- **B:** Correct. Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics. In this scenario: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry `TracerProvider`) followed by a short delay before process exit drains the in-memory telemetry buffer to the ingestion endpoint.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry `TracerProvider`) followed by a short delay before process exit drains the in-memory telemetry buffer to the ingestion endpoint.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry `TracerProvider`) followed by a short delay before process exit drains the in-memory telemetry buffer to the ingestion endpoint.

### Question 62 — B

Answer: Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`. Registering a custom `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and wrapping the method body in `using var span = Source.StartActivity("ValidateFraud")` emits native OpenTelemetry spans. `System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Registering a custom `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and wrapping the method body in `using var span = Source.StartActivity("ValidateFraud")` emits native OpenTelemetry spans.
- **B:** Correct. `System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro. In this scenario: Registering a custom `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and wrapping the method body in `using var span = Source.StartActivity("ValidateFraud")` emits native OpenTelemetry spans.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Registering a custom `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and wrapping the method body in `using var span = Source.StartActivity("ValidateFraud")` emits native OpenTelemetry spans.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Registering a custom `System.Diagnostics.ActivitySource` via `.WithTracing(b => b.AddSource(...))` and wrapping the method body in `using var span = Source.StartActivity("ValidateFraud")` emits native OpenTelemetry spans.

### Question 63 — C

Answer: Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group. Application Insights Standard Availability Tests enable TLS expiry validation and multi-POP probing, and a `>= 2` failed-locations alert rule wired to an Action Group eliminates single-region false alarms. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Application Insights Standard Availability Tests enable TLS expiry validation and multi-POP probing, and a `>= 2` failed-locations alert rule wired to an Action Group eliminates single-region false alarms.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Application Insights Standard Availability Tests enable TLS expiry validation and multi-POP probing, and a `>= 2` failed-locations alert rule wired to an Action Group eliminates single-region false alarms.
- **C:** Correct. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. In this scenario: Application Insights Standard Availability Tests enable TLS expiry validation and multi-POP probing, and a `>= 2` failed-locations alert rule wired to an Action Group eliminates single-region false alarms.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Application Insights Standard Availability Tests enable TLS expiry validation and multi-POP probing, and a `>= 2` failed-locations alert rule wired to an Action Group eliminates single-region false alarms.

### Question 64 — C

Answer: Create an Azure Monitor Metric Alert (Dynamic Thresholds or static p95 latency/5xx count) or Scheduled Query (KQL) Alert targeting an Action Group configured with webhook / Azure Function / email-SMS receivers. A Metric Alert using Dynamic Thresholds learns seasonal historical baselines automatically and invokes an Action Group configured with a secure webhook receiver. Metric alerts offer sub-minute stateful evaluation on numeric signals, whereas Scheduled Query Rules run expressive KQL joins on log tables at configured intervals. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: A Metric Alert using Dynamic Thresholds learns seasonal historical baselines automatically and invokes an Action Group configured with a secure webhook receiver.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: A Metric Alert using Dynamic Thresholds learns seasonal historical baselines automatically and invokes an Action Group configured with a secure webhook receiver.
- **C:** Correct. Metric alerts offer sub-minute stateful evaluation on numeric signals, whereas Scheduled Query Rules run expressive KQL joins on log tables at configured intervals. In this scenario: A Metric Alert using Dynamic Thresholds learns seasonal historical baselines automatically and invokes an Action Group configured with a secure webhook receiver.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: A Metric Alert using Dynamic Thresholds learns seasonal historical baselines automatically and invokes an Action Group configured with a secure webhook receiver.

### Question 65 — C

Answer: Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group. Running a VNet-integrated Timer-Triggered Function that probes the private endpoint, calls `TelemetryClient.TrackAvailability()`, and wires an availability alert rule to an Action Group monitors private endpoints cleanly. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Running a VNet-integrated Timer-Triggered Function that probes the private endpoint, calls `TelemetryClient.TrackAvailability()`, and wires an availability alert rule to an Action Group monitors private endpoints cleanly.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Running a VNet-integrated Timer-Triggered Function that probes the private endpoint, calls `TelemetryClient.TrackAvailability()`, and wires an availability alert rule to an Action Group monitors private endpoints cleanly.
- **C:** Correct. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. In this scenario: Running a VNet-integrated Timer-Triggered Function that probes the private endpoint, calls `TelemetryClient.TrackAvailability()`, and wires an availability alert rule to an Action Group monitors private endpoints cleanly.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Running a VNet-integrated Timer-Triggered Function that probes the private endpoint, calls `TelemetryClient.TrackAvailability()`, and wires an availability alert rule to an Action Group monitors private endpoints cleanly.

### Question 66 — D, E

Answers: Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments; Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`. Installing `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()` + `APPLICATIONINSIGHTS_CONNECTION_STRING`) enables auto-instrumentation, while registering `ActivitySource` adds custom business spans. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Installing `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()` + `APPLICATIONINSIGHTS_CONNECTION_STRING`) enables auto-instrumentation, while registering `ActivitySource` adds custom business spans.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Installing `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()` + `APPLICATIONINSIGHTS_CONNECTION_STRING`) enables auto-instrumentation, while registering `ActivitySource` adds custom business spans.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Installing `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()` + `APPLICATIONINSIGHTS_CONNECTION_STRING`) enables auto-instrumentation, while registering `ActivitySource` adds custom business spans.
- **D:** Correct. `System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro. In this scenario: Installing `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()` + `APPLICATIONINSIGHTS_CONNECTION_STRING`) enables auto-instrumentation, while registering `ActivitySource` adds custom business spans.
- **E:** Correct. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. In this scenario: Installing `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()` + `APPLICATIONINSIGHTS_CONNECTION_STRING`) enables auto-instrumentation, while registering `ActivitySource` adds custom business spans.

### Question 67 — C

Answer: Provision Workspace-based Application Insights and copy APPLICATIONINSIGHTS_CONNECTION_STRING → configure UseAzureMonitor() OpenTelemetry distro at startup → verify requests/dependencies in Logs → create a KQL or metric alert linked to an Action Group. Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, wiring `UseAzureMonitor()`, verifying live spans in Logs, and creating an Action Group-backed alert rule completes the rollout cleanly. Workspace-based Application Insights and connection-string OpenTelemetry setup emit telemetry first so KQL/metric alerts and Action Groups monitor real signals. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Zero telemetry rate and missing connection strings discard all telemetry before it reaches Azure Monitor. Why the keyed choice wins: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, wiring `UseAzureMonitor()`, verifying live spans in Logs, and creating an Action Group-backed alert rule completes the rollout cleanly.
- **B:** Incorrect for this requirement. Alert queries require a target Application Insights / Log Analytics resource and instrumented telemetry emission. Why the keyed choice wins: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, wiring `UseAzureMonitor()`, verifying live spans in Logs, and creating an Action Group-backed alert rule completes the rollout cleanly.
- **C:** Correct. Workspace-based Application Insights and connection-string OpenTelemetry setup emit telemetry first so KQL/metric alerts and Action Groups monitor real signals. In this scenario: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, wiring `UseAzureMonitor()`, verifying live spans in Logs, and creating an Action Group-backed alert rule completes the rollout cleanly.
- **D:** Incorrect for this requirement. Classic Application Insights and bare Instrumentation Keys are retired in favor of Workspace-based resources and `APPLICATIONINSIGHTS_CONNECTION_STRING`. Why the keyed choice wins: Provisioning Workspace-based Application Insights and copying `APPLICATIONINSIGHTS_CONNECTION_STRING`, wiring `UseAzureMonitor()`, verifying live spans in Logs, and creating an Action Group-backed alert rule completes the rollout cleanly.

### Question 68 — A

Answer: Select `Developer` (non-SLA) or `Premium` / `Standard v2` for VNet integration, and deploy the containerized APIM Self-Hosted Gateway (`mcr.microsoft.com/azure-api-management/gateway`) for hybrid on-premises/multi-cloud local traffic routing. Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway inside each store cluster keeps data-plane calls local while syncing policies from Azure. Self-hosted gateways require `Developer` or `Premium` tier and keep data-plane traffic local while pulling policy updates outbound over HTTPS/443 from Azure. Local study-map skill 5.1 (Provision Azure API Management Tiers, VNet Modes, and Self-Hosted Hybrid Gateways), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Self-hosted gateways require `Developer` or `Premium` tier and keep data-plane traffic local while pulling policy updates outbound over HTTPS/443 from Azure. In this scenario: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway inside each store cluster keeps data-plane calls local while syncing policies from Azure.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway inside each store cluster keeps data-plane calls local while syncing policies from Azure.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway inside each store cluster keeps data-plane calls local while syncing policies from Azure.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Provisioning APIM `Developer` or `Premium` tier and deploying the containerized APIM Self-Hosted Gateway inside each store cluster keeps data-plane calls local while syncing policies from Azure.

### Question 69 — B

Answer: Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`. `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra bearer tokens minted for APIM's Managed Identity. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. Local study-map skill 5.1 (Provision Azure API Management Tiers, VNet Modes, and Self-Hosted Hybrid Gateways), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra bearer tokens minted for APIM's Managed Identity.
- **B:** Correct. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. In this scenario: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra bearer tokens minted for APIM's Managed Identity.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra bearer tokens minted for APIM's Managed Identity.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects cached Entra bearer tokens minted for APIM's Managed Identity.

### Question 70 — D

Answer: Use APIM `Revisions` to stage, test, and swap non-breaking internal changes safely on the same consumer URL (`;rev=2`), and use APIM `Versions` (path/header/query) when publishing breaking contract changes side-by-side for distinct consumer cohorts. APIM `Revisions` stage and swap non-breaking updates transparently on the current URL, whereas APIM `Versions` expose separate consumer-visible `/v1` and `/v2` contracts side by side. Revisions let authors edit and flip the `current` implementation transparently; Versions expose distinct URLs/headers so legacy clients keep working. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: APIM `Revisions` stage and swap non-breaking updates transparently on the current URL, whereas APIM `Versions` expose separate consumer-visible `/v1` and `/v2` contracts side by side.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: APIM `Revisions` stage and swap non-breaking updates transparently on the current URL, whereas APIM `Versions` expose separate consumer-visible `/v1` and `/v2` contracts side by side.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: APIM `Revisions` stage and swap non-breaking updates transparently on the current URL, whereas APIM `Versions` expose separate consumer-visible `/v1` and `/v2` contracts side by side.
- **D:** Correct. Revisions let authors edit and flip the `current` implementation transparently; Versions expose distinct URLs/headers so legacy clients keep working. In this scenario: APIM `Revisions` stage and swap non-breaking updates transparently on the current URL, whereas APIM `Versions` expose separate consumer-visible `/v1` and `/v2` contracts side by side.

### Question 71 — D

Answer: Use `<mock-response status-code="200" content-type="application/json" />` during frontend parallel development, or `<rewrite-uri template="/internal/v2/orders/{orderId}" />` with `<set-backend-service base-url="..." />` in `<inbound>`. `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI sample payloads before backend readiness, and `<rewrite-uri>` + `<set-backend-service>` map clean public routes to internal backend paths. `<mock-response>` short-circuits backend forwarding using OpenAPI example payloads, while `<rewrite-uri>` maps public clean paths onto legacy internal routes. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI sample payloads before backend readiness, and `<rewrite-uri>` + `<set-backend-service>` map clean public routes to internal backend paths.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI sample payloads before backend readiness, and `<rewrite-uri>` + `<set-backend-service>` map clean public routes to internal backend paths.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI sample payloads before backend readiness, and `<rewrite-uri>` + `<set-backend-service>` map clean public routes to internal backend paths.
- **D:** Correct. `<mock-response>` short-circuits backend forwarding using OpenAPI example payloads, while `<rewrite-uri>` maps public clean paths onto legacy internal routes. In this scenario: `<mock-response status-code="200" content-type="application/json" />` returns OpenAPI sample payloads before backend readiness, and `<rewrite-uri>` + `<set-backend-service>` map clean public routes to internal backend paths.

### Question 72 — B

Answer: Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation. `AuthorizationLevel.Function` requires a function-specific or host key (`x-functions-key` header or `code` query parameter), which APIM wires automatically during Function App import. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `AuthorizationLevel.Function` requires a function-specific or host key (`x-functions-key` header or `code` query parameter), which APIM wires automatically during Function App import.
- **B:** Correct. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. In this scenario: `AuthorizationLevel.Function` requires a function-specific or host key (`x-functions-key` header or `code` query parameter), which APIM wires automatically during Function App import.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `AuthorizationLevel.Function` requires a function-specific or host key (`x-functions-key` header or `code` query parameter), which APIM wires automatically during Function App import.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `AuthorizationLevel.Function` requires a function-specific or host key (`x-functions-key` header or `code` query parameter), which APIM wires automatically during Function App import.

### Question 73 — B

Answer: Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers. Combining Product Subscription Key enforcement with `<validate-jwt>` and `context.Request.Certificate.Thumbprint` condition checks inside `<inbound>` blocks unauthorized partner traffic at the gateway edge. Combining gateway `<validate-jwt>` pre-authentication with subscription scoping and client-certificate thumbprint checks blocks invalid traffic before hitting backends. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Combining Product Subscription Key enforcement with `<validate-jwt>` and `context.Request.Certificate.Thumbprint` condition checks inside `<inbound>` blocks unauthorized partner traffic at the gateway edge.
- **B:** Correct. Combining gateway `<validate-jwt>` pre-authentication with subscription scoping and client-certificate thumbprint checks blocks invalid traffic before hitting backends. In this scenario: Combining Product Subscription Key enforcement with `<validate-jwt>` and `context.Request.Certificate.Thumbprint` condition checks inside `<inbound>` blocks unauthorized partner traffic at the gateway edge.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Combining Product Subscription Key enforcement with `<validate-jwt>` and `context.Request.Certificate.Thumbprint` condition checks inside `<inbound>` blocks unauthorized partner traffic at the gateway edge.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Combining Product Subscription Key enforcement with `<validate-jwt>` and `context.Request.Certificate.Thumbprint` condition checks inside `<inbound>` blocks unauthorized partner traffic at the gateway edge.

### Question 74 — C, E

Answers: Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers; Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`. Combining Product Subscription Keys, `<validate-jwt>`, and `context.Request.Certificate.Thumbprint` secures inbound partner calls, while `<authentication-managed-identity>` secures the hop from APIM to the backend. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Combining Product Subscription Keys, `<validate-jwt>`, and `context.Request.Certificate.Thumbprint` secures inbound partner calls, while `<authentication-managed-identity>` secures the hop from APIM to the backend.
- **B:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Combining Product Subscription Keys, `<validate-jwt>`, and `context.Request.Certificate.Thumbprint` secures inbound partner calls, while `<authentication-managed-identity>` secures the hop from APIM to the backend.
- **C:** Correct. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. In this scenario: Combining Product Subscription Keys, `<validate-jwt>`, and `context.Request.Certificate.Thumbprint` secures inbound partner calls, while `<authentication-managed-identity>` secures the hop from APIM to the backend.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Combining Product Subscription Keys, `<validate-jwt>`, and `context.Request.Certificate.Thumbprint` secures inbound partner calls, while `<authentication-managed-identity>` secures the hop from APIM to the backend.
- **E:** Correct. Combining gateway `<validate-jwt>` pre-authentication with subscription scoping and client-certificate thumbprint checks blocks invalid traffic before hitting backends. In this scenario: Combining Product Subscription Keys, `<validate-jwt>`, and `context.Request.Certificate.Thumbprint` secures inbound partner calls, while `<authentication-managed-identity>` secures the hop from APIM to the backend.

### Question 75 — A, B, E

Answers: Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`; Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`; Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`. `<rate-limit-by-key>` + `<quota-by-key>` alongside `<base />` handle burst/monthly limits, `<cache-lookup>` + `<cache-store>` cache localized responses, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` add resilience and header hygiene. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` alongside `<base />` handle burst/monthly limits, `<cache-lookup>` + `<cache-store>` cache localized responses, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` add resilience and header hygiene.
- **B:** Correct. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` alongside `<base />` handle burst/monthly limits, `<cache-lookup>` + `<cache-store>` cache localized responses, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` add resilience and header hygiene.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` alongside `<base />` handle burst/monthly limits, `<cache-lookup>` + `<cache-store>` cache localized responses, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` add resilience and header hygiene.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` alongside `<base />` handle burst/monthly limits, `<cache-lookup>` + `<cache-store>` cache localized responses, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` add resilience and header hygiene.
- **E:** Correct. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` alongside `<base />` handle burst/monthly limits, `<cache-lookup>` + `<cache-store>` cache localized responses, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` add resilience and header hygiene.
- **F:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` alongside `<base />` handle burst/monthly limits, `<cache-lookup>` + `<cache-store>` cache localized responses, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` add resilience and header hygiene.

### Question 76 — D

Answer: Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`. Deleting `<base />` silently skips all parent API-, Product-, and Global-scope `<inbound>` policies (such as `<validate-jwt>` or CORS); keeping `<base />` alongside `<rate-limit-by-key>` and `<quota-by-key>` preserves policy inheritance. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Deleting `<base />` silently skips all parent API-, Product-, and Global-scope `<inbound>` policies (such as `<validate-jwt>` or CORS); keeping `<base />` alongside `<rate-limit-by-key>` and `<quota-by-key>` preserves policy inheritance.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Deleting `<base />` silently skips all parent API-, Product-, and Global-scope `<inbound>` policies (such as `<validate-jwt>` or CORS); keeping `<base />` alongside `<rate-limit-by-key>` and `<quota-by-key>` preserves policy inheritance.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Deleting `<base />` silently skips all parent API-, Product-, and Global-scope `<inbound>` policies (such as `<validate-jwt>` or CORS); keeping `<base />` alongside `<rate-limit-by-key>` and `<quota-by-key>` preserves policy inheritance.
- **D:** Correct. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! In this scenario: Deleting `<base />` silently skips all parent API-, Product-, and Global-scope `<inbound>` policies (such as `<validate-jwt>` or CORS); keeping `<base />` alongside `<rate-limit-by-key>` and `<quota-by-key>` preserves policy inheritance.

### Question 77 — D

Answer: Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`. APIM response caching requires pairing `<cache-lookup>` inside `<inbound>` with `<cache-store duration="..." />` inside `<outbound>` so backend responses actually populate the cache. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: APIM response caching requires pairing `<cache-lookup>` inside `<inbound>` with `<cache-store duration="..." />` inside `<outbound>` so backend responses actually populate the cache.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: APIM response caching requires pairing `<cache-lookup>` inside `<inbound>` with `<cache-store duration="..." />` inside `<outbound>` so backend responses actually populate the cache.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: APIM response caching requires pairing `<cache-lookup>` inside `<inbound>` with `<cache-store duration="..." />` inside `<outbound>` so backend responses actually populate the cache.
- **D:** Correct. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. In this scenario: APIM response caching requires pairing `<cache-lookup>` inside `<inbound>` with `<cache-store duration="..." />` inside `<outbound>` so backend responses actually populate the cache.

### Question 78 — A

Answer: Deploy the HTTPS webhook endpoint accepting POST requests → create the Event Grid subscription pointing to the endpoint → inspect incoming SubscriptionValidationEvent and read validationCode → return HTTP 200 JSON containing validationResponse (or invoke validationUrl). Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, parsing `SubscriptionValidationEvent.validationCode`, and returning HTTP 200 `{"validationResponse": ...}` completes webhook validation. Event Grid dispatches a SubscriptionValidationEvent during subscription creation and activates delivery only after the endpoint echoes validationResponse (or completes validationUrl). Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Event Grid dispatches a SubscriptionValidationEvent during subscription creation and activates delivery only after the endpoint echoes validationResponse (or completes validationUrl). In this scenario: Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, parsing `SubscriptionValidationEvent.validationCode`, and returning HTTP 200 `{"validationResponse": ...}` completes webhook validation.
- **B:** Incorrect for this requirement. Event Grid requires HTTPS webhook endpoints and expects JSON `{"validationResponse": "..."}` in the response body (or GET on validationUrl). Why the keyed choice wins: Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, parsing `SubscriptionValidationEvent.validationCode`, and returning HTTP 200 `{"validationResponse": ...}` completes webhook validation.
- **C:** Incorrect for this requirement. The validation code is unique per subscription handshake and cannot be echoed before Event Grid sends the SubscriptionValidationEvent. Why the keyed choice wins: Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, parsing `SubscriptionValidationEvent.validationCode`, and returning HTTP 200 `{"validationResponse": ...}` completes webhook validation.
- **D:** Incorrect for this requirement. If the endpoint is not live and returning validationResponse during creation, webhook validation fails before subscription creation completes. Why the keyed choice wins: Deploying the HTTPS POST endpoint first, creating the Event Grid subscription, parsing `SubscriptionValidationEvent.validationCode`, and returning HTTP 200 `{"validationResponse": ...}` completes webhook validation.

### Question 79 — B, C

Answers: Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization; Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`. Provisioning an Event Grid Domain scales thousands of tenant-isolated domain topics under one endpoint with per-topic RBAC, while echoing `validationResponse` (or `WebHook-Allowed-Origin` for CloudEvents) validates custom webhooks. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Provisioning an Event Grid Domain scales thousands of tenant-isolated domain topics under one endpoint with per-topic RBAC, while echoing `validationResponse` (or `WebHook-Allowed-Origin` for CloudEvents) validates custom webhooks.
- **B:** Correct. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. In this scenario: Provisioning an Event Grid Domain scales thousands of tenant-isolated domain topics under one endpoint with per-topic RBAC, while echoing `validationResponse` (or `WebHook-Allowed-Origin` for CloudEvents) validates custom webhooks.
- **C:** Correct. Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures. In this scenario: Provisioning an Event Grid Domain scales thousands of tenant-isolated domain topics under one endpoint with per-topic RBAC, while echoing `validationResponse` (or `WebHook-Allowed-Origin` for CloudEvents) validates custom webhooks.
- **D:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Provisioning an Event Grid Domain scales thousands of tenant-isolated domain topics under one endpoint with per-topic RBAC, while echoing `validationResponse` (or `WebHook-Allowed-Origin` for CloudEvents) validates custom webhooks.
- **E:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Provisioning an Event Grid Domain scales thousands of tenant-isolated domain topics under one endpoint with per-topic RBAC, while echoing `validationResponse` (or `WebHook-Allowed-Origin` for CloudEvents) validates custom webhooks.

### Question 80 — D

Answer: Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`. Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` proves endpoint ownership. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` proves endpoint ownership.
- **B:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` proves endpoint ownership.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` proves endpoint ownership.
- **D:** Correct. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. In this scenario: Detecting `Microsoft.EventGrid.SubscriptionValidationEvent` (or CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin`) and returning HTTP 200 with `{"validationResponse": validationCode}` proves endpoint ownership.

### Question 81 — A

Answer: Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2. Creating a dedicated Event Hubs Consumer Group for each independent downstream reader isolates partition offset cursors while allowing optional Event Hubs Capture to archive Parquet batches. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. In this scenario: Creating a dedicated Event Hubs Consumer Group for each independent downstream reader isolates partition offset cursors while allowing optional Event Hubs Capture to archive Parquet batches.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Creating a dedicated Event Hubs Consumer Group for each independent downstream reader isolates partition offset cursors while allowing optional Event Hubs Capture to archive Parquet batches.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Creating a dedicated Event Hubs Consumer Group for each independent downstream reader isolates partition offset cursors while allowing optional Event Hubs Capture to archive Parquet batches.
- **D:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Creating a dedicated Event Hubs Consumer Group for each independent downstream reader isolates partition offset cursors while allowing optional Event Hubs Capture to archive Parquet batches.

### Question 82 — B

Answer: Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2. Event Grid is a push router without replayable partition logs; Azure Event Hubs provides partitioned pull streams, isolated Consumer Groups per reader, and zero-code Event Hubs Capture to Avro/Parquet in Blob/ADLS Gen2. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Event Grid is a push router without replayable partition logs; Azure Event Hubs provides partitioned pull streams, isolated Consumer Groups per reader, and zero-code Event Hubs Capture to Avro/Parquet in Blob/ADLS Gen2.
- **B:** Correct. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. In this scenario: Event Grid is a push router without replayable partition logs; Azure Event Hubs provides partitioned pull streams, isolated Consumer Groups per reader, and zero-code Event Hubs Capture to Avro/Parquet in Blob/ADLS Gen2.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Event Grid is a push router without replayable partition logs; Azure Event Hubs provides partitioned pull streams, isolated Consumer Groups per reader, and zero-code Event Hubs Capture to Avro/Parquet in Blob/ADLS Gen2.
- **D:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Event Grid is a push router without replayable partition logs; Azure Event Hubs provides partitioned pull streams, isolated Consumer Groups per reader, and zero-code Event Hubs Capture to Avro/Parquet in Blob/ADLS Gen2.

### Question 83 — B

Answer: Host `EventProcessorClient` backed by `BlobContainerClient` and call `await eventArgs.UpdateCheckpointAsync()` after idempotent batch persistence so partition leases resume cleanly after rebalancing. Calling `await eventArgs.UpdateCheckpointAsync()` after persisting a batch writes the latest sequence/offset into Azure Blob Storage metadata so rebalanced pods resume from the checkpoint. `EventProcessorClient` coordinates partition ownership via Azure Blob leases and records per-partition sequence/offset checkpoints in Blob metadata. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Calling `await eventArgs.UpdateCheckpointAsync()` after persisting a batch writes the latest sequence/offset into Azure Blob Storage metadata so rebalanced pods resume from the checkpoint.
- **B:** Correct. `EventProcessorClient` coordinates partition ownership via Azure Blob leases and records per-partition sequence/offset checkpoints in Blob metadata. In this scenario: Calling `await eventArgs.UpdateCheckpointAsync()` after persisting a batch writes the latest sequence/offset into Azure Blob Storage metadata so rebalanced pods resume from the checkpoint.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Calling `await eventArgs.UpdateCheckpointAsync()` after persisting a batch writes the latest sequence/offset into Azure Blob Storage metadata so rebalanced pods resume from the checkpoint.
- **D:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Calling `await eventArgs.UpdateCheckpointAsync()` after persisting a batch writes the latest sequence/offset into Azure Blob Storage metadata so rebalanced pods resume from the checkpoint.

### Question 84 — B, E

Answers: Use Azure Service Bus Topics with `SqlRuleFilter` / `CorrelationRuleFilter` (`CorrelationRuleFilter` preferred for high throughput) and `SqlRuleAction` header stamping, inspecting `$DeadLetterQueue` (`SubQueue.DeadLetter`) after `MaxDeliveryCount` expires; Use `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false`, calling `CompleteMessageAsync` after commit, `AbandonMessageAsync` for transient retries, and `DeadLetterMessageAsync` on unrecoverable schema errors. Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route high-throughput filtered copies and quarantine poison retries, while `ServiceBusReceiveMode.PeekLock` (`AutoCompleteMessages = false`) protects in-flight durability. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route high-throughput filtered copies and quarantine poison retries, while `ServiceBusReceiveMode.PeekLock` (`AutoCompleteMessages = false`) protects in-flight durability.
- **B:** Correct. `ReceiveAndDelete` loses messages if a worker crashes mid-processing; `PeekLock` retains broker durability until explicit settlement or lock expiry. In this scenario: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route high-throughput filtered copies and quarantine poison retries, while `ServiceBusReceiveMode.PeekLock` (`AutoCompleteMessages = false`) protects in-flight durability.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route high-throughput filtered copies and quarantine poison retries, while `ServiceBusReceiveMode.PeekLock` (`AutoCompleteMessages = false`) protects in-flight durability.
- **D:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route high-throughput filtered copies and quarantine poison retries, while `ServiceBusReceiveMode.PeekLock` (`AutoCompleteMessages = false`) protects in-flight durability.
- **E:** Correct. `CorrelationRuleFilter` matches brokered/application properties in-memory far faster than SQL evaluation, while `MaxDeliveryCount` isolates poison messages in the sub-queue DLQ. In this scenario: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` route high-throughput filtered copies and quarantine poison retries, while `ServiceBusReceiveMode.PeekLock` (`AutoCompleteMessages = false`) protects in-flight durability.

### Question 85 — A

Answer: Call `long seq = await sender.ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` and persist `seq` to call `CancelScheduledMessageAsync(seq)` if the user cancels early. `ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` holds the message invisible on the broker and returns `sequenceNumber` so `CancelScheduledMessageAsync(seq)` can abort delivery if paid early. Service Bus native scheduled messages stay invisible until `ScheduledEnqueueTime` and can be canceled cleanly via their broker sequence number. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Service Bus native scheduled messages stay invisible until `ScheduledEnqueueTime` and can be canceled cleanly via their broker sequence number. In this scenario: `ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` holds the message invisible on the broker and returns `sequenceNumber` so `CancelScheduledMessageAsync(seq)` can abort delivery if paid early.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` holds the message invisible on the broker and returns `sequenceNumber` so `CancelScheduledMessageAsync(seq)` can abort delivery if paid early.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` holds the message invisible on the broker and returns `sequenceNumber` so `CancelScheduledMessageAsync(seq)` can abort delivery if paid early.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` holds the message invisible on the broker and returns `sequenceNumber` so `CancelScheduledMessageAsync(seq)` can abort delivery if paid early.

### Question 86 — C

Answer: Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics. Standard/Premium Service Bus queues cap entity size at 1–80 GB, whereas Azure Queue Storage scales up to the 500 TiB storage account ceiling for simple visibility-leased messages up to 64 KB. Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Standard/Premium Service Bus queues cap entity size at 1–80 GB, whereas Azure Queue Storage scales up to the 500 TiB storage account ceiling for simple visibility-leased messages up to 64 KB.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Standard/Premium Service Bus queues cap entity size at 1–80 GB, whereas Azure Queue Storage scales up to the 500 TiB storage account ceiling for simple visibility-leased messages up to 64 KB.
- **C:** Correct. Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub. In this scenario: Standard/Premium Service Bus queues cap entity size at 1–80 GB, whereas Azure Queue Storage scales up to the 500 TiB storage account ceiling for simple visibility-leased messages up to 64 KB.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Standard/Premium Service Bus queues cap entity size at 1–80 GB, whereas Azure Queue Storage scales up to the 500 TiB storage account ceiling for simple visibility-leased messages up to 64 KB.

### Question 87 — C

Answer: Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`; calling `ReceiveMessagesAsync(visibilityTimeout)`, checking `DequeueCount` for poison items, and passing `MessageId` + `PopReceipt` to `DeleteMessageAsync` leases and deletes safely. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. Local study-map skill 5.8 (Implement Queue Workflows with Azure Queue Storage SDK, Visibility Leases, PopReceipts, and Poison Handling), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`; calling `ReceiveMessagesAsync(visibilityTimeout)`, checking `DequeueCount` for poison items, and passing `MessageId` + `PopReceipt` to `DeleteMessageAsync` leases and deletes safely.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`; calling `ReceiveMessagesAsync(visibilityTimeout)`, checking `DequeueCount` for poison items, and passing `MessageId` + `PopReceipt` to `DeleteMessageAsync` leases and deletes safely.
- **C:** Correct. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. In this scenario: `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`; calling `ReceiveMessagesAsync(visibilityTimeout)`, checking `DequeueCount` for poison items, and passing `MessageId` + `PopReceipt` to `DeleteMessageAsync` leases and deletes safely.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`; calling `ReceiveMessagesAsync(visibilityTimeout)`, checking `DequeueCount` for poison items, and passing `MessageId` + `PopReceipt` to `DeleteMessageAsync` leases and deletes safely.

### Question 88 — D

Answer: Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`. Passing both `MessageId` and current `PopReceipt` returned by `ReceiveMessagesAsync` to `UpdateMessageAsync` extends `visibilityTimeout` and returns a refreshed `PopReceipt` required for `DeleteMessageAsync`. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. Local study-map skill 5.8 (Implement Queue Workflows with Azure Queue Storage SDK, Visibility Leases, PopReceipts, and Poison Handling), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Passing both `MessageId` and current `PopReceipt` returned by `ReceiveMessagesAsync` to `UpdateMessageAsync` extends `visibilityTimeout` and returns a refreshed `PopReceipt` required for `DeleteMessageAsync`.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Passing both `MessageId` and current `PopReceipt` returned by `ReceiveMessagesAsync` to `UpdateMessageAsync` extends `visibilityTimeout` and returns a refreshed `PopReceipt` required for `DeleteMessageAsync`.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Passing both `MessageId` and current `PopReceipt` returned by `ReceiveMessagesAsync` to `UpdateMessageAsync` extends `visibilityTimeout` and returns a refreshed `PopReceipt` required for `DeleteMessageAsync`.
- **D:** Correct. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. In this scenario: Passing both `MessageId` and current `PopReceipt` returned by `ReceiveMessagesAsync` to `UpdateMessageAsync` extends `visibilityTimeout` and returns a refreshed `PopReceipt` required for `DeleteMessageAsync`.

### Question 89 — C

Answer: Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering. Enabling `RequiresSession = true` (partitioned by member `SessionId`) enforces single-consumer FIFO order per member, while `RequiresDuplicateDetection = true` with a 10-minute window suppresses duplicate `MessageId` retries. Service Bus discards duplicate `MessageId` resends inside the history window and locks all messages sharing a `SessionId` to one active session receiver at a time. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub. Why the keyed choice wins: Enabling `RequiresSession = true` (partitioned by member `SessionId`) enforces single-consumer FIFO order per member, while `RequiresDuplicateDetection = true` with a 10-minute window suppresses duplicate `MessageId` retries.
- **B:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Enabling `RequiresSession = true` (partitioned by member `SessionId`) enforces single-consumer FIFO order per member, while `RequiresDuplicateDetection = true` with a 10-minute window suppresses duplicate `MessageId` retries.
- **C:** Correct. Service Bus discards duplicate `MessageId` resends inside the history window and locks all messages sharing a `SessionId` to one active session receiver at a time. In this scenario: Enabling `RequiresSession = true` (partitioned by member `SessionId`) enforces single-consumer FIFO order per member, while `RequiresDuplicateDetection = true` with a 10-minute window suppresses duplicate `MessageId` retries.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Enabling `RequiresSession = true` (partitioned by member `SessionId`) enforces single-consumer FIFO order per member, while `RequiresDuplicateDetection = true` with a 10-minute window suppresses duplicate `MessageId` retries.

### Question 90 — B

Answer: In the .NET isolated worker model, return a custom POCO class uniting `[HttpResult]` (or `HttpResponseData`) with `[CosmosDBOutput]` / `[ServiceBusOutput]` properties. Because .NET isolated worker functions run out-of-process, multiple outputs are emitted by returning a custom POCO class decorated with `[HttpResult]` (or `HttpResponseData`) alongside `[CosmosDBOutput]`. Isolated-worker C# functions cannot use `out` parameters for bindings; multi-output types return structured properties on a single return object. Local study-map skill 1.12 (Implement Azure Functions Input and Output Bindings (Isolated Worker & Declarative Bindings)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Because .NET isolated worker functions run out-of-process, multiple outputs are emitted by returning a custom POCO class decorated with `[HttpResult]` (or `HttpResponseData`) alongside `[CosmosDBOutput]`.
- **B:** Correct. Isolated-worker C# functions cannot use `out` parameters for bindings; multi-output types return structured properties on a single return object. In this scenario: Because .NET isolated worker functions run out-of-process, multiple outputs are emitted by returning a custom POCO class decorated with `[HttpResult]` (or `HttpResponseData`) alongside `[CosmosDBOutput]`.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Because .NET isolated worker functions run out-of-process, multiple outputs are emitted by returning a custom POCO class decorated with `[HttpResult]` (or `HttpResponseData`) alongside `[CosmosDBOutput]`.
- **D:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Because .NET isolated worker functions run out-of-process, multiple outputs are emitted by returning a custom POCO class decorated with `[HttpResult]` (or `HttpResponseData`) alongside `[CosmosDBOutput]`.

### Question 91 — C

Answer: Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently. Ingestion sampling (or coordinated adaptive sampling) hashes `operation_Id` consistently so complete multi-service transactions are retained or discarded together while keeping Live Metrics unsampled. Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics. Why the keyed choice wins: Ingestion sampling (or coordinated adaptive sampling) hashes `operation_Id` consistently so complete multi-service transactions are retained or discarded together while keeping Live Metrics unsampled.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Ingestion sampling (or coordinated adaptive sampling) hashes `operation_Id` consistently so complete multi-service transactions are retained or discarded together while keeping Live Metrics unsampled.
- **C:** Correct. Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled. In this scenario: Ingestion sampling (or coordinated adaptive sampling) hashes `operation_Id` consistently so complete multi-service transactions are retained or discarded together while keeping Live Metrics unsampled.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Ingestion sampling (or coordinated adaptive sampling) hashes `operation_Id` consistently so complete multi-service transactions are retained or discarded together while keeping Live Metrics unsampled.

### Question 92 — C

Answer: Declare `appRoles` with `allowedMemberTypes: ["User", "Application"]` in the Entra app registration manifest and validate the `roles` claim (`[Authorize(Roles = "...")]`) in the web API. Declaring `WholesaleBuyer` inside `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` JWT claim cleanly for `[Authorize(Roles = "WholesaleBuyer")]` checks. Entra ID emits assigned app roles inside the `roles` JWT claim for both human users and service principals without requiring directory-level Entra admin roles. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Declaring `WholesaleBuyer` inside `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` JWT claim cleanly for `[Authorize(Roles = "WholesaleBuyer")]` checks.
- **B:** Incorrect for this requirement. Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`. Why the keyed choice wins: Declaring `WholesaleBuyer` inside `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` JWT claim cleanly for `[Authorize(Roles = "WholesaleBuyer")]` checks.
- **C:** Correct. Entra ID emits assigned app roles inside the `roles` JWT claim for both human users and service principals without requiring directory-level Entra admin roles. In this scenario: Declaring `WholesaleBuyer` inside `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` JWT claim cleanly for `[Authorize(Roles = "WholesaleBuyer")]` checks.
- **D:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Declaring `WholesaleBuyer` inside `appRoles` with `allowedMemberTypes: ["User", "Application"]` emits the `roles` JWT claim cleanly for `[Authorize(Roles = "WholesaleBuyer")]` checks.

### Question 93 — C

Answer: Assign Storage Blob Data Contributor/Delegator RBAC to the identity → instantiate BlobServiceClient with DefaultAzureCredential → call GetUserDelegationKeyAsync for a bounded validity window → build BlobSasBuilder and sign with the user delegation key. Acquiring a User Delegation Key via Entra RBAC (`Storage Blob Delegator`) and signing a short-lived HTTPS-only `BlobSasBuilder` grants direct client upload access with zero shared storage keys. Entra RBAC must authorize delegation before BlobServiceClient requests a user delegation key, which then signs the BlobSasBuilder token without account keys. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. GetUserDelegationKeyAsync requires an authenticated Entra client with RBAC already granted before the call executes. Why the keyed choice wins: Acquiring a User Delegation Key via Entra RBAC (`Storage Blob Delegator`) and signing a short-lived HTTPS-only `BlobSasBuilder` grants direct client upload access with zero shared storage keys.
- **B:** Incorrect for this requirement. The client must authenticate with Microsoft Entra credentials first so it can request the delegation key that mints the SAS. Why the keyed choice wins: Acquiring a User Delegation Key via Entra RBAC (`Storage Blob Delegator`) and signing a short-lived HTTPS-only `BlobSasBuilder` grants direct client upload access with zero shared storage keys.
- **C:** Correct. Entra RBAC must authorize delegation before BlobServiceClient requests a user delegation key, which then signs the BlobSasBuilder token without account keys. In this scenario: Acquiring a User Delegation Key via Entra RBAC (`Storage Blob Delegator`) and signing a short-lived HTTPS-only `BlobSasBuilder` grants direct client upload access with zero shared storage keys.
- **D:** Incorrect for this requirement. A SAS cannot be signed before obtaining the user delegation key, and shared account keys cannot mint Entra user delegation SAS tokens. Why the keyed choice wins: Acquiring a User Delegation Key via Entra RBAC (`Storage Blob Delegator`) and signing a short-lived HTTPS-only `BlobSasBuilder` grants direct client upload access with zero shared storage keys.

### Question 94 — B

Answer: Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`). A Blob Storage Lifecycle Management rule scoped to `prefixMatch: ["po-uploads/"]` with `tierToCool` (`daysAfterModificationGreaterThan: 30`) and `delete` (`365`) automates tiering and retention server-side. Lifecycle management policies automate tier transitions and retention deletion server-side once per day without custom cron jobs. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `SetAccessTierAsync` (or copy-to-Hot) initiates Archive rehydration; `RehydratePriority.High` prioritizes restoration (often under 1 hour for <10 GB blobs). Why the keyed choice wins: A Blob Storage Lifecycle Management rule scoped to `prefixMatch: ["po-uploads/"]` with `tierToCool` (`daysAfterModificationGreaterThan: 30`) and `delete` (`365`) automates tiering and retention server-side.
- **B:** Correct. Lifecycle management policies automate tier transitions and retention deletion server-side once per day without custom cron jobs. In this scenario: A Blob Storage Lifecycle Management rule scoped to `prefixMatch: ["po-uploads/"]` with `tierToCool` (`daysAfterModificationGreaterThan: 30`) and `delete` (`365`) automates tiering and retention server-side.
- **C:** Incorrect for this requirement. Time-based locked retention and legal holds block modification and deletion even by Storage Account Owners until retention expires and holds clear. Why the keyed choice wins: A Blob Storage Lifecycle Management rule scoped to `prefixMatch: ["po-uploads/"]` with `tierToCool` (`daysAfterModificationGreaterThan: 30`) and `delete` (`365`) automates tiering and retention server-side.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: A Blob Storage Lifecycle Management rule scoped to `prefixMatch: ["po-uploads/"]` with `tierToCool` (`daysAfterModificationGreaterThan: 30`) and `delete` (`365`) automates tiering and retention server-side.

### Question 95 — D

Answer: Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL. Event Grid push subscriptions deliver `CloudEvents v1.0` within seconds, retry transiently with exponential backoff up to 24 hours, and write exhausted events into a configured Blob dead-letter container. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Event Grid push subscriptions deliver `CloudEvents v1.0` within seconds, retry transiently with exponential backoff up to 24 hours, and write exhausted events into a configured Blob dead-letter container.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Event Grid push subscriptions deliver `CloudEvents v1.0` within seconds, retry transiently with exponential backoff up to 24 hours, and write exhausted events into a configured Blob dead-letter container.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Event Grid push subscriptions deliver `CloudEvents v1.0` within seconds, retry transiently with exponential backoff up to 24 hours, and write exhausted events into a configured Blob dead-letter container.
- **D:** Correct. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. In this scenario: Event Grid push subscriptions deliver `CloudEvents v1.0` within seconds, retry transiently with exponential backoff up to 24 hours, and write exhausted events into a configured Blob dead-letter container.

### Question 96 — D

Answer: Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`. Wrapping `<forward-request />` inside `<retry>` in `<backend>` retries transient 5xx responses, while `<set-header exists-action="delete" />` in `<outbound>` removes internal headers before partners receive the payload. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Wrapping `<forward-request />` inside `<retry>` in `<backend>` retries transient 5xx responses, while `<set-header exists-action="delete" />` in `<outbound>` removes internal headers before partners receive the payload.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Wrapping `<forward-request />` inside `<retry>` in `<backend>` retries transient 5xx responses, while `<set-header exists-action="delete" />` in `<outbound>` removes internal headers before partners receive the payload.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Wrapping `<forward-request />` inside `<retry>` in `<backend>` retries transient 5xx responses, while `<set-header exists-action="delete" />` in `<outbound>` removes internal headers before partners receive the payload.
- **D:** Correct. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. In this scenario: Wrapping `<forward-request />` inside `<retry>` in `<backend>` retries transient 5xx responses, while `<set-header exists-action="delete" />` in `<outbound>` removes internal headers before partners receive the payload.

### Question 97 — C

Answer: Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`. Placing `<validate-jwt>` with `<openid-config>`, `<audiences>`, and `<required-claims>` inside `<inbound>` enforces cryptographic JWT validation at the APIM edge before backend compute executes. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Placing `<validate-jwt>` with `<openid-config>`, `<audiences>`, and `<required-claims>` inside `<inbound>` enforces cryptographic JWT validation at the APIM edge before backend compute executes.
- **B:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Placing `<validate-jwt>` with `<openid-config>`, `<audiences>`, and `<required-claims>` inside `<inbound>` enforces cryptographic JWT validation at the APIM edge before backend compute executes.
- **C:** Correct. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. In this scenario: Placing `<validate-jwt>` with `<openid-config>`, `<audiences>`, and `<required-claims>` inside `<inbound>` enforces cryptographic JWT validation at the APIM edge before backend compute executes.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Placing `<validate-jwt>` with `<openid-config>`, `<audiences>`, and `<required-claims>` inside `<inbound>` enforces cryptographic JWT validation at the APIM edge before backend compute executes.

### Question 98 — C

Answer: Mark environment-specific settings such as `PaymentWebhookUrl` and production connection strings as `slotSetting: true` (Deployment slot setting) before swapping slots. Marking `PaymentWebhookUrl` as a deployment slot setting (`slotSetting: true`) pins each value to its own slot across swaps so staging builds never trigger live payment webhooks. Slot-sticky settings stay pinned to their slot (`Production` vs `Staging`) across swaps instead of traveling with the swapped code. Local study-map skill 1.10 (Configure App Service Deployment Slots, Slot-Sticky Settings, Warm-Up, and Traffic Routing), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Marking `PaymentWebhookUrl` as a deployment slot setting (`slotSetting: true`) pins each value to its own slot across swaps so staging builds never trigger live payment webhooks.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Marking `PaymentWebhookUrl` as a deployment slot setting (`slotSetting: true`) pins each value to its own slot across swaps so staging builds never trigger live payment webhooks.
- **C:** Correct. Slot-sticky settings stay pinned to their slot (`Production` vs `Staging`) across swaps instead of traveling with the swapped code. In this scenario: Marking `PaymentWebhookUrl` as a deployment slot setting (`slotSetting: true`) pins each value to its own slot across swaps so staging builds never trigger live payment webhooks.
- **D:** Incorrect for this requirement. Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy. Why the keyed choice wins: Marking `PaymentWebhookUrl` as a deployment slot setting (`slotSetting: true`) pins each value to its own slot across swaps so staging builds never trigger live payment webhooks.

### Question 99 — D

Answer: Use `FeedIterator<Order> iter = container.GetItemQueryIterator<Order>(queryDef, requestOptions: new QueryRequestOptions { PartitionKey = new PartitionKey(pk), MaxItemCount = 100 })` and loop `while (iter.HasMoreResults) { FeedResponse<Order> page = await iter.ReadNextAsync(); }`. Scoping `QueryRequestOptions.PartitionKey` to `/customerId` avoids cross-partition fan-out while `GetItemQueryIterator<Order>` with `ReadNextAsync()` streams bounded pages and exposes `RequestCharge`. `GetItemQueryIterator<T>` streams paginated results via continuation tokens and inspects `page.RequestCharge` without buffering an entire partition in memory. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Scoping `QueryRequestOptions.PartitionKey` to `/customerId` avoids cross-partition fan-out while `GetItemQueryIterator<Order>` with `ReadNextAsync()` streams bounded pages and exposes `RequestCharge`.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Scoping `QueryRequestOptions.PartitionKey` to `/customerId` avoids cross-partition fan-out while `GetItemQueryIterator<Order>` with `ReadNextAsync()` streams bounded pages and exposes `RequestCharge`.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Scoping `QueryRequestOptions.PartitionKey` to `/customerId` avoids cross-partition fan-out while `GetItemQueryIterator<Order>` with `ReadNextAsync()` streams bounded pages and exposes `RequestCharge`.
- **D:** Correct. `GetItemQueryIterator<T>` streams paginated results via continuation tokens and inspects `page.RequestCharge` without buffering an entire partition in memory. In this scenario: Scoping `QueryRequestOptions.PartitionKey` to `/customerId` avoids cross-partition fan-out while `GetItemQueryIterator<Order>` with `ReadNextAsync()` streams bounded pages and exposes `RequestCharge`.

### Question 100 — A

Answer: Configure App Service / Functions application settings using `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` (omitting secret version) paired with `Key Vault Secrets User` on the app Managed Identity. Versionless `@Microsoft.KeyVault(SecretUri=...)` app-setting references paired with `Key Vault Secrets User` on the web app's Managed Identity inject rotated secrets as environment variables with zero code changes. Versionless Key Vault references automatically pull rotated secret versions within 24 hours (or immediately on config change / manual sync) with zero SDK boilerplate. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Versionless Key Vault references automatically pull rotated secret versions within 24 hours (or immediately on config change / manual sync) with zero SDK boilerplate. In this scenario: Versionless `@Microsoft.KeyVault(SecretUri=...)` app-setting references paired with `Key Vault Secrets User` on the web app's Managed Identity inject rotated secrets as environment variables with zero code changes.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Versionless `@Microsoft.KeyVault(SecretUri=...)` app-setting references paired with `Key Vault Secrets User` on the web app's Managed Identity inject rotated secrets as environment variables with zero code changes.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Versionless `@Microsoft.KeyVault(SecretUri=...)` app-setting references paired with `Key Vault Secrets User` on the web app's Managed Identity inject rotated secrets as environment variables with zero code changes.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Versionless `@Microsoft.KeyVault(SecretUri=...)` app-setting references paired with `Key Vault Secrets User` on the web app's Managed Identity inject rotated secrets as environment variables with zero code changes.
