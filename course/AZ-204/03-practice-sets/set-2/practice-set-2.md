# Microsoft Exam AZ-204: Developing Solutions for Microsoft Azure — Full-Length Mock Exam 2

Exam AZ-204 (Healthcare Patient Portals, Clinical Lab Telemetry, and Claims EDI) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Credential Lifecycle Notice:** Microsoft retired Exam AZ-204 (`Microsoft Certified: Azure Developer Associate`) on **July 31, 2026** and succeeded it with **Exam AI-200 (`Azure AI Cloud Developer Associate`)**. This practice bank preserves the final official January 14, 2026 AZ-204 skills-measured baseline for archival certification prep, enterprise Azure developer benchmarking, and core compute/storage/security/monitoring/integration mastery.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` SDK/CLI/XML/JSON/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area code dropdowns, split-pane tabbed case exhibits, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn documentation — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. A biomedical imaging team is writing a Dockerfile for an ASP.NET Core 8 DICOM router (`ENTRYPOINT ____ `) and needs lean production layers plus clean `SIGTERM` graceful shutdowns when pods scale in. Which two Dockerfile practices should they adopt? Select two.

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Use a multi-stage Dockerfile building in `mcr.microsoft.com/dotnet/sdk:8.0` and copying published output into `mcr.microsoft.com/dotnet/aspnet:8.0` with a non-root `USER app`
- C. Declare `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form so `SIGTERM` reaches the .NET host cleanly during container shutdown
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Keep the default `--restart-policy Always` on a run-once batch container group

### 2. Running `az acr build` from a clinician portal monorepo uploads 1.9 GB of `bin/`, `obj/`, `.git/`, and developer `.env` files on every remote build. What single file change shrinks the uploaded build context immediately?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Add `bin/`, `obj/`, `.git/`, and local `.env` files to `.dockerignore` before running `docker build` or `az acr build`

### 3. Hospital firewall policy blocks build workstations from pulling public Docker Hub base images directly, so DevOps wants Azure Container Registry to copy `nginx:1.27-alpine` server-side into private ACR (` ____ `). Which CLI command performs this?

Domain: Develop Azure compute solutions

- A. Execute `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine`
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 4. Proposed solution: Keep Azure Container Registry on the `Basic` tier in East US while deploying clinical Container Apps across East US, West Europe, and Southeast Asia expecting local regional layer pulls from one registry FQDN. Why does this fail, and what solves it?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Upgrade Azure Container Registry to the `Premium` SKU and configure geo-replication into each target compute region
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 5. An HL7 parser running on Azure Container Instances requires an MLLP clinic token that must never appear in `az container show` output or Azure Portal environment-variable blades (`az container create ____ `). Which parameter protects the secret?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Pass sensitive tokens via `--secure-environment-variables` (or a secret volume mount) so values never appear in Azure Portal properties or `az container show` plaintext output
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 6. Nightly ICD-10 claims coding containers run on ACI for twelve minutes, exit with code `0`, and must retry automatically only when an unhandled exception returns a non-zero exit code without looping after success. Which restart policy fits?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Set `--restart-policy OnFailure` (or `Never`) on the Azure Container Instances container group so batch containers stop billing vCPU/memory seconds once exit code 0 completes
- C. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 7. A clinical scheduling team is deploying a triage microservice to Azure Container Apps that pulls container images from a private ACR with admin credentials disabled. Which ordered sequence configures Managed Identity pulls cleanly?

Domain: Develop Azure compute solutions

- A. Grant AcrPull on the registry → create the container app → create the user-assigned identity → run az acr build
- B. Build and push the image to ACR with az acr build → create a user-assigned managed identity and grant AcrPull on the registry → create the Container Apps environment → create the container app referencing the identity and registry server
- C. Create the container app referencing the registry → build and push the image with az acr build → create the Container Apps environment → grant AcrPull
- D. Create the Container Apps environment → create the container app → enable ACR admin passwords → revoke AcrPull

### 8. Inside a shared healthcare Container Apps environment, only `rx-verifier` and `rx-dispense` may access a Dapr state store, queue workers must scale down to zero via Managed Identity when idle, and container env vars must resolve Key Vault secrets safely. Which three Container Apps configurations meet all three rules? Select three.

Domain: Develop Azure compute solutions

- A. Register a Dapr state or pub/sub component in the Container Apps environment and restrict access via the component `scopes` array to specific `daprAppId` values
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- D. Keep the default `--restart-policy Always` on a run-once batch container group
- E. Define a Container App secret using `keyVaultUrl` plus `identity` (managed identity resource ID or `system`) and map container environment variables via `secretRef`
- F. Configure a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0` and Managed Identity (`identity` property) so replicas scale to zero when idle and wake on queue depth

### 9. Proposed solution: Leave an Azure Container App in `--revision-mode single` and run `az containerapp ingress traffic set` to send 15% of live patient-intake HTTP requests to a canary revision. Why does this fail, and what change enables canary routing?

Domain: Develop Azure compute solutions

- A. Set `--revision-mode multiple` and apply `az containerapp ingress traffic set --revision-weight` to split live HTTP requests across named revisions
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 10. A clinic appointment web app currently runs on an App Service `Shared (D1)` plan and now needs custom domain SNI TLS certificates, a pre-production staging slot, and weekday CPU autoscale rules. Which App Service plan change is required?

Domain: Develop Azure compute solutions

- A. Provision at least a `Standard` (`S1+`) or `Premium v3` (`P1v3+`) App Service plan to unlock deployment slots, custom domain SNI SSL, and metric/schedule autoscaling
- B. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 11. A containerized .NET 8 EHR viewer deployed to Linux App Service listens on non-root port `8080` (` ____ `), and health probes fail on port 80 until container port settings align. Which Dockerfile configuration sets the runtime port cleanly?

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Set `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` inside the final `.NET 8` runtime stage and match `targetPort: 8080` on Container Apps ingress
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 12. Compliance officers require 90-day retention of application diagnostics from a scaled-out Windows App Service patient portal without automatic 12-hour shutoff. Where must Application Logging be directed?

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 13. An on-call healthcare developer wants to watch live stdout trace lines from a Linux App Service triage API directly in their shell (` ____ `). Which Azure CLI command attaches to the live diagnostic stream?

Domain: Develop Azure compute solutions

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 14. Deploying updated assemblies to a busy claims-portal App Service web app via FTP leaves half-copied files and triggers `wwwroot` file-lock errors. Which deployment mechanism eliminates partial syncs and file locks?

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Set `WEBSITE_RUN_FROM_PACKAGE=1` and deploy with `az webapp deploy --type zip` so the app mounts the read-only ZIP package directly with atomic cold-start replacement
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 15. A containerized radiology viewer on App Service for Linux must pull images from Azure Container Registry after security disables `--admin-enabled` on ACR. How should registry authentication be configured?

Domain: Develop Azure compute solutions

- A. Disable the ACR admin account and assign the built-in `AcrPull` role on the registry to the compute resource managed identity
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 16. A browser-based clinician workstation at `https://chart.aurelia.example` calls `https://fhir-api.aurelia.example` on App Service with credentials, and HIPAA security policy requires TLS 1.2+ and automatic HTTP-to-HTTPS redirection. Which two App Service configurations are needed? Select two.

Domain: Develop Azure compute solutions

- A. Configure App Service `CORS` with explicit origin URLs (and `supportCredentials` only without wildcard `*`) so App Service handles preflight `OPTIONS` requests
- B. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Enable `httpsOnly: true`, set `minTlsVersion: "1.2"` (or `"1.3"`), and configure `clientCertEnabled` when mutual TLS client certificates are required
- E. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 17. A patient billing App Service web app must bind `LedgerDb` as a slot-pinned `SQLAzure` connection string from a CI script (` ____ `). Which Azure CLI command sets and pins the connection string?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Keep the default `--restart-policy Always` on a run-once batch container group

### 18. Every Monday at 08:00 AM clinic check-in spikes App Service CPU, and poorly tuned autoscale rules add 4 workers and remove 4 workers repeatedly every 3 minutes. Which adjustment stops instance thrashing?

Domain: Develop Azure compute solutions

- A. Pair every scale-out metric rule (e.g., CPU > 75% for 10 min) with a conservative scale-in rule (e.g., CPU < 35%) and an explicit `coolDown` window plus safe default/max instance bounds
- B. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 19. Before a swapped `staging` slot receives live telehealth API traffic, App Service must hit `/healthz/warmup` on every worker and wait for HTTP `200` after reference medical dictionaries finish loading. Which settings enforce this check?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps
- D. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision

### 20. A release engineer is promoting a validated patient-portal release on App Service Premium P1v3 without dropping active sessions or leaking staging HL7 endpoints into production. Which sequence performs the swap properly?

Domain: Develop Azure compute solutions

- A. Deploy directly to production → create the staging slot → swap staging into production → mark settings as slot settings
- B. Create the staging slot on a Free F1 plan → deploy the build → swap slots → mark settings sticky
- C. Create the staging deployment slot on the Standard/Premium Web App → mark production-only connection strings and webhook settings as deployment slot settings → deploy and warm up the new build in staging → swap staging into production and verify health
- D. Swap staging into production → create the staging slot → deploy the build → mark settings as deployment slot settings

### 21. After swapping `staging` into `Production` on a telemed App Service web app, production clinicians suddenly connect to the sandbox insurance clearinghouse URL configured earlier on `staging`. Which setting prevents this on future swaps?

Domain: Develop Azure compute solutions

- A. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Mark environment-specific settings such as `PaymentWebhookUrl` and production connection strings as `slotSetting: true` (Deployment slot setting) before swapping slots

### 22. An oncology genomics Function App takes 18 minutes to align sequence batches, connects outbound to a private VNet storage endpoint, and cannot tolerate cold-start delays on urgent stat orders. Which Functions hosting plan should the team select?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Host the Function App on `Flex Consumption` or `Elastic Premium (EP1+)` when VNet integration, longer execution timeouts beyond 10 minutes, or pre-warmed/always-ready instances are required
- D. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`

### 23. A clinical ingestion Function App needs a 10-minute timeout and wants Application Insights sampling to exclude `Request` and `Exception` items across all functions (`host.json`: ` ____ `). Which configuration completes `host.json`?

Domain: Develop Azure compute solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Configure `"functionTimeout": "00:10:00"` and `"logging": { "applicationInsights": { "samplingSettings": { "isEnabled": true, "excludedTypes": "Request;Exception" } } }` inside `host.json`

### 24. A .NET 8 isolated-worker Function App processes HL7 admissions: one HTTP trigger must emit both an HTTP response and a Service Bus message without `out` parameters, while an Event Hub trigger must retry transient FHIR timeouts five times with exponential backoff. Which two patterns apply? Select two.

Domain: Develop Azure compute solutions

- A. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- B. Apply `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` (or `[FixedDelayRetry]`) on the `[EventHubTrigger]` / `[TimerTrigger]` function
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. In the .NET isolated worker model, return a custom POCO class uniting `[HttpResult]` (or `HttpResponseData`) with `[CosmosDBOutput]` / `[ServiceBusOutput]` properties
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 25. An internal lab-instrument gateway invokes an HTTP-triggered Azure Function supplying an `x-functions-key` header scoped strictly to that single function rather than the `_master` host key (`[HttpTrigger( ____ )]`). Which `AuthorizationLevel` enum value matches this behavior?

Domain: Develop Azure compute solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`

### 26. A pharmacy refrigerator temperature audit Function uses `[TimerTrigger(" ____ ")]` to run every 15 minutes during weekday clinic hours (`09:00–17:45`). Which six-field NCRONTAB expression is valid?

Domain: Develop Azure compute solutions

- A. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Specify a six-field NCRONTAB expression `{second} {minute} {hour} {day} {month} {day-of-week}` such as `"0 */15 9-17 * * 1-5"` on `[TimerTrigger]`

### 27. Proposed solution: Use a default log-polling `[BlobTrigger]` on a Blob-only storage account receiving 80,000 pathology slide images per hour to guarantee sub-second trigger latency. Why does this lag, and what fixes it?

Domain: Develop Azure compute solutions

- A. Configure `[BlobTrigger(..., Source = BlobTriggerSource.EventGrid)]` with an Event Grid system topic subscription instead of default container-log polling
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 28. A multi-hospital telemetry platform using Cosmos DB for NoSQL has single hospital tenants exceeding 20 GB of data, needs efficient queries by `/tenantId` and `/siteId`, commits vitals batches atomically within one partition key, and rejects stale concurrent chart edits with HTTP 412. Which three Cosmos DB capabilities should the developer combine? Select three.

Domain: Develop for Azure storage

- A. Define `new ContainerProperties(id: "telemetry", partitionKeyPaths: new List<string> { "/tenantId", "/siteId", "/deviceId" })` using `PartitionKeyBuilder` on reads and writes
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use `container.CreateTransactionalBatch(new PartitionKey(pkValue))` to group multiple create/replace/upsert/delete operations atomically within the same logical partition
- D. Pass `new ItemRequestOptions { IfMatchEtag = item.ETag }` on `ReplaceItemAsync` and catch `CosmosException` when `StatusCode == HttpStatusCode.PreconditionFailed` (412)
- E. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- F. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction

### 29. A high-volume ECG waveform container in Cosmos DB writes 40 KB JSON documents queried exclusively by `/customerId` (patient ID) and `/createdUtc`, and write RU charges are triple budget (`"indexingPolicy": { ____ }`). Which indexing change cuts write RUs sharply?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Add a `compositeIndexes` array matching the exact property sequence and sort directions (`ascending` / `descending`) in the container indexing policy JSON
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Configure `"indexingMode": "consistent"` with `"includedPaths": [{"path": "/customerId/?"}, {"path": "/createdUtc/?"}]` and `"excludedPaths": [{"path": "/*"}]`

### 30. When a lab courier scans a specimen pouch, the API only needs to increment `/retryCount` and set `/lastStatus` on a 120 KB Cosmos DB specimen document (`await container. ____ `). Which SDK method avoids fetching and replacing the full JSON document?

Domain: Develop for Azure storage

- A. Call `await container.PatchItemAsync<Order>(id, new PartitionKey(pk), new[] { PatchOperation.Increment("/retryCount", 1), PatchOperation.Set("/lastStatus", "Queued") })`
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 31. Under peak morning clinic load, an ASP.NET Core FHIR service instantiating `new CosmosClient(endpoint, cred)` inside every controller action throws `SocketException` port exhaustion errors. How should client lifecycle be refactored?

Domain: Develop for Azure storage

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Register `CosmosClient` as a process-wide singleton in dependency injection and choose a high-cardinality `PartitionKey` path (or up to 3-level `Hierarchical` subpartition paths) that distributes RU/s evenly
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction

### 32. A patient updates allergy records in a portal backed by Cosmos DB and immediately reloads their chart via another web worker; they must read their own update immediately without paying `Strong` consistency read RU overhead. How should this be implemented?

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use `Session` consistency (the default) and propagate `x-ms-session-token` (`RequestOptions.SessionToken`) across client/middle-tier hops to guarantee monotonic read-your-own-writes at half the read RU cost of `Strong`

### 33. Regional disaster-recovery hospital sites read from secondary Cosmos DB regions and require guaranteed monotonic write ordering within at most 5 seconds (`T`) or 100 operations (`K`) of the primary region. Which consistency level provides this SLA?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency

### 34. A clinical analytics team is building a C# background service using Cosmos DB Change Feed Processor v3 to project patient encounter updates into a reporting store. Which sequence initializes and starts the processor?

Domain: Develop for Azure storage

- A. Create only the monitored container → call Build and StartAsync → attach WithLeaseContainer → define the handler delegate
- B. Attach WithLeaseContainer pointing to the monitored container without /id partition → call StartAsync → call GetChangeFeedProcessorBuilder<T> → call Build
- C. Call StartAsync on the processor → call GetChangeFeedProcessorBuilder<T> → create the lease container → attach WithInstanceName
- D. Create the monitored container and a dedicated lease container → call GetChangeFeedProcessorBuilder<T> with processorName and delegate → attach WithInstanceName and WithLeaseContainer → call Build and StartAsync on the processor

### 35. Both a billing microservice and an anonymization microservice must read every Cosmos DB encounter change independently, and purged test encounters must also emit change events. Which two Change Feed configurations are required? Select two.

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use Change Feed `AllVersionsAndDeletes` mode (or soft-delete flag items with short TTL in `LatestVersion` mode) because default `LatestVersion` change feed omits hard-deleted items
- D. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- E. Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay

### 36. A radiology archive holds 25 million study blobs across 40 containers and needs sub-second server-side filtering for `@container = 'docs' AND status = 'pending'` (` ____ `) without enumerating blobs. Which Blob SDK capability enables this?

Domain: Develop for Azure storage

- A. Attach searchable key-value `Tags` (`SetTagsAsync` / `BlobUploadOptions.Tags`) and query across containers with `FindBlobsByTagsAsync("@container = 'docs' AND status = 'pending'")`
- B. Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`)
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 37. A clinical document uploader calls `SetMetadataAsync` with key `"clinic-id"` containing a hyphen and receives HTTP `400 InvalidMetadata` (` ____ `). How must Blob metadata and HTTP headers be written via the .NET v12 SDK?

Domain: Develop for Azure storage

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`)
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 38. Before running an automated redaction pass over an uploaded consent PDF blob, the workflow wants an explicit read-only point-in-time checkpoint (`await blobClient. ____ `) plus account protection against accidental overwrites. Which feature set fits?

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Call `await blobClient.CreateSnapshotAsync()` for explicit point-in-time read-only checkpoints or enable account-level Blob Versioning so every `UploadAsync` overwrite retains an immutable `VersionId`

### 39. Three claims-export workers occasionally overwrite the same `edi-837-control.json` state blob simultaneously. How should each C# worker serialize exclusive 60-second write access?

Domain: Develop for Azure storage

- A. Use `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` (15–60 seconds or `-1` infinite) and pass `LeaseId` inside `BlobRequestConditions` on subsequent writes/deletes
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 40. A compliance replicator copies 900 GB of encrypted pathology archives to a secondary storage account (`await destBlob. ____ `) without routing medical bytes through the orchestrator pod's NIC. Which SDK call executes this?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained
- D. Invoke `BlobClient.StartCopyFromUriAsync(sourceSasUri)` to trigger asynchronous server-side blob copy and inspect `CopyStatus` without streaming bytes through the client VM

### 41. An export worker constructs a 15-minute HTTPS-only read SAS restricted strictly to blob `exports/manifest.csv` (`new BlobSasBuilder { ____ }`). Which properties and permission call complete the builder?

Domain: Develop for Azure storage

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 42. Telemetry archives in Blob Storage must transition automatically from `Hot` to `Cool` after 30 days and `Archive` after 180 days, while urgent clinical Subpoena requests for archived <10 GB files must restore in under an hour. Which two configurations solve both requirements? Select two.

Domain: Develop for Azure storage

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`)
- C. Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob)
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- E. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 43. Proposed solution: Call `DownloadStreamingAsync()` directly on a 3 GB oncology pathology archive stored in the `Archive` access tier when a surgeon requests immediate review. Why does this fail with HTTP `409 BlobArchived`, and which SDK call restores access fastest?

Domain: Develop for Azure storage

- A. Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob)
- B. Keep the default `--restart-policy Always` on a run-once batch container group
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 44. A bedside tablet app used by nurses signs in with Microsoft Entra ID and refreshes FHIR access tokens silently between patient rounds without repeatedly prompting for MFA. Which two MSAL coding practices are required? Select two.

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- C. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`

### 45. Proposed solution: Use `PublicClientApplicationBuilder` with interactive browser login inside an unattended Linux Kubernetes cron pod syncing HL7 lab codes at 02:00 AM. Why does this fail, and which MSAL pattern replaces it?

Domain: Implement Azure security

- A. Use `ConfidentialClientApplicationBuilder` authenticated with a client certificate (or workload identity assertion) calling `AcquireTokenForClient(new[] { "api://.../.default" })` for headless background daemons
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 46. An oncology review API must authorize both human oncologists and an automated tumour-board scheduler service principal under the same `[Authorize(Roles = "CaseReviewer")]` attribute. How must the Entra app registration define `CaseReviewer`?

Domain: Implement Azure security

- A. Declare `appRoles` with `allowedMemberTypes: ["User", "Application"]` in the Entra app registration manifest and validate the `roles` claim (`[Authorize(Roles = "...")]`) in the web API
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)

### 47. A clinical-trial SaaS portal invites research coordinators from 30 university hospital Entra tenants while rejecting personal `@outlook.com` accounts and unapproved tenant IDs. Which Entra configuration enforces this?

Domain: Implement Azure security

- A. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation

### 48. An iOS patient app calling an App Service API protected by Easy Auth fails JSON parsing whenever tokens expire because App Service responds with `302 Redirect` to an HTML sign-in page. What change fixes the API contract?

Domain: Implement Azure security

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 49. A diagnostic imaging portal needs to mint a 15-minute upload SAS for an MRI zip archive using Microsoft Entra credentials instead of storage account keys. Which ordered steps generate the User Delegation SAS?

Domain: Implement Azure security

- A. Instantiate BlobServiceClient with SAS token → assign RBAC → build BlobSasBuilder → call GetUserDelegationKeyAsync
- B. Call GetUserDelegationKeyAsync anonymously → build BlobSasBuilder → assign RBAC to the identity → instantiate BlobServiceClient
- C. Build BlobSasBuilder and sign → call GetUserDelegationKeyAsync → instantiate BlobServiceClient with shared account key → assign RBAC to the identity
- D. Assign Storage Blob Data Contributor/Delegator RBAC to the identity → instantiate BlobServiceClient with DefaultAzureCredential → call GetUserDelegationKeyAsync for a bounded validity window → build BlobSasBuilder and sign with the user delegation key

### 50. An external claims auditor receives a Service SAS for container `q3-audits`, and security requires a way to revoke that SAS within seconds if leaked without rotating account keys used by internal apps. How must the SAS be issued?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Bind a Service SAS to a container/queue/table Stored Access Policy (`SignedIdentifier`, omitting inline start/expiry/permissions) so compromised tokens can be revoked instantly by modifying or deleting the policy
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 51. A nurse-rostering portal queries shift leads via Microsoft Graph, needing minimal permission consent, reliable pagination across 12,000 staff records, and combined JSON batch calls for 15 shift rooms per page load. Which two Graph SDK patterns should the developer use? Select two.

Domain: Implement Azure security

- A. Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- E. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 52. A hospital directory widget built on Microsoft Graph .NET SDK v5 needs only active staff (`accountEnabled eq true`) returning strictly `id`, `displayName`, and `mail` (`await graphClient.Users.GetAsync( ____ )`). Which request configuration completes the call?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Call `await graphClient.Users.GetAsync(rc => { rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }; rc.QueryParameters.Filter = "accountEnabled eq true"; })`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 53. Proposed solution: Grant `Directory.ReadWrite.All` application permission to a clinic room-finder widget that only displays room names and availability via Microsoft Graph without `$select` or `PageIterator<T>`. Why does security reject this, and what replaces it?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`

### 54. A claims microservice loads feature flags and Key Vault secret references from Azure App Configuration (`options.Connect(uri, cred). ____ `), and startup fails resolving `application/vnd.microsoft.appconfig.keyvaultref+json` items. What call is missing?

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Wire `options.Connect(new Uri(endpoint), cred).ConfigureKeyVault(kv => kv.SetCredential(cred))` so App Configuration resolves Key Vault reference items using the app identity
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 55. A healthcare PKI and secrets platform uses Azure Key Vault for HL7 database credentials, RSA signing keys, and mTLS X.509 certificates, and compliance mandates immutable 90-day protection against permanent key purge. Which two Key Vault practices are required? Select two.

Domain: Implement Azure security

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Enable Soft Delete (mandatory on new vaults, 7–90 days) plus Purge Protection on Azure Key Vault so neither accidental deletion nor malicious principals can permanently destroy keys before retention expires
- C. Use `SecretClient` (`Azure.Security.KeyVault.Secrets`) for connection strings/tokens, `KeyClient` / `CryptographyClient` (`Azure.Security.KeyVault.Keys`) for RSA/EC wrap-unwrap-sign, and `CertificateClient` for X.509 lifecycle
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- E. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 56. A legacy .NET worker hosted on Azure App Service reads `Environment.GetEnvironmentVariable("FhirApiSecret")` and must pull rotated values from Key Vault without adding NuGet SDK packages (` ____ `). Which App Service feature accomplishes this?

Domain: Implement Azure security

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Configure App Service / Functions application settings using `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` (omitting secret version) paired with `Key Vault Secrets User` on the app Managed Identity
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 57. Twelve ephemeral ACI claims-processing groups are created and deleted hourly, yet all twelve must share one pre-authorized Entra identity granted RBAC on a single Key Vault and Blob container without re-creating role assignments every hour. Which identity model fits?

Domain: Implement Azure security

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Choose a User-Assigned Managed Identity when multiple compute resources must share one pre-provisioned identity lifecycle independent of individual app deletions; choose System-Assigned when 1-to-1 fate-sharing tied to a single resource is required

### 58. A clinical Container App attaches two User-Assigned Managed Identities (`uami-acr` and `uami-fhir`), and `new DefaultAzureCredential()` fails because IMDS cannot guess which identity to issue a token for (` ____ `). How must the code specify `uami-fhir`?

Domain: Implement Azure security

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Instantiate `new DefaultAzureCredential(new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId })` (or set `AZURE_CLIENT_ID`)
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps

### 59. Clinical reliability engineers investigating latency spikes across their patient portal need end-to-end W3C trace correlation across microservices plus 5-minute KQL buckets showing error counts and p95 latency per operation. Which two Application Insights techniques deliver both? Select two.

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Run `AppRequests | where TimeGenerated > ago(1h) | summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)`
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Query Workspace-based Application Insights (`AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces` or classic `requests`/`dependencies`/`exceptions`) joining on `OperationId` (`operation_Id`) to reconstruct end-to-end distributed transactions
- E. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 60. Nightly HL7 batch reconcilers run for 8 seconds inside Container Apps Jobs and exit `Main()` immediately after calling `TrackTrace`, losing the last 30 telemetry events in memory. Which C# shutdown step prevents lost telemetry?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 61. An eligibility microservice instrumented with `UseAzureMonitor()` needs a custom timed span around its `VerifyInsuranceCoverage` rules engine (`using var span = ____ `) so slow payer rules appear in Application Insights Transaction Search. How should this be coded?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`

### 62. Patient portal traffic triples on weekday mornings and drops 90% overnight, so static request-failure alerts either miss night outages or spam daytime false alarms; alerts must also invoke an Azure Function remediation receiver. Which alert setup works best?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Create an Azure Monitor Metric Alert (Dynamic Thresholds or static p95 latency/5xx count) or Scheduled Query (KQL) Alert targeting an Action Group configured with webhook / Azure Function / email-SMS receivers
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 63. A private VNet-isolated HL7 MLLP gateway has no public DNS endpoint, yet SREs need synthetic availability percentages in the Application Insights Availability blade with multi-failure alerting. How should probes be implemented?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 64. A telehealth platform migrating off legacy Application Insights SDKs onto OpenTelemetry must connect via `APPLICATIONINSIGHTS_CONNECTION_STRING`, keep multi-service `operation_Id` traces intact under sampling, and view real-time unsampled counters during deployments. Which two capabilities satisfy these goals? Select two.

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- E. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 65. Proposed solution: Instrument a brand-new .NET 8 clinical API using the deprecated `Microsoft.ApplicationInsights.AspNetCore` package configured solely with a bare Classic `InstrumentationKey` GUID. Why does Microsoft advise against this, and what replaces it?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 66. Three clinical microservices apply independent per-host adaptive sampling rates, causing Transaction Search to show broken parent spans with missing child dependency spans on the same `operation_Id`. Which sampling mode preserves whole traces across services?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently

### 67. Regional hospital campuses run local lab analyzers that must call local FHIR microservices even during temporary WAN fiber cuts, while centrally managed APIM policies sync from Azure when connectivity is up. Which APIM deployment model supports this?

Domain: Connect to and consume Azure services and third-party services

- A. Select `Developer` (non-SLA) or `Premium` / `Standard v2` for VNet integration, and deploy the containerized APIM Self-Hosted Gateway (`mcr.microsoft.com/azure-api-management/gateway`) for hybrid on-premises/multi-cloud local traffic routing
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 68. Aurelia's APIM instance forwards validated requests to an internal Entra-protected claims API and must acquire bearer tokens automatically using APIM's Managed Identity (`<inbound> ____ </inbound>`). Which XML policy achieves this?

Domain: Connect to and consume Azure services and third-party services

- A. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- B. Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps

### 69. A FHIR API team fixes an optional description typo without breaking clients (`;rev=2`) and next quarter introduces a breaking FHIR R4-to-R5 schema requiring `/r4/Patient` and `/r5/Patient` to coexist for 18 months. How should APIM `Revisions` and `Versions` be used?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Use APIM `Revisions` to stage, test, and swap non-breaking internal changes safely on the same consumer URL (`;rev=2`), and use APIM `Versions` (path/header/query) when publishing breaking contract changes side-by-side for distinct consumer cohorts
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 70. Partner mobile developers need realistic HTTP 200 FHIR Patient JSON responses from APIM while the backend container is still unbuilt, and later public `/patient/{id}` calls must rewrite to `/internal/v2/orders/{orderId}`-style legacy paths (` ____ `). Which APIM policies handle both stages?

Domain: Connect to and consume Azure services and third-party services

- A. Use `<mock-response status-code="200" content-type="application/json" />` during frontend parallel development, or `<rewrite-uri template="/internal/v2/orders/{orderId}" />` with `<set-backend-service base-url="..." />` in `<inbound>`
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 71. An Azure Function imported behind Azure API Management sets `AuthorizationLevel.Anonymous` because APIM enforces mTLS and `<validate-jwt>` at the gateway and VNet-locks the Function App. How does `AuthorizationLevel` behave across `Anonymous`, `Function`, and `Admin`?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation

### 72. A healthcare platform engineer is removing static client secrets from APIM Named Values and configuring APIM to authenticate via Managed Identity to a protected backend EHR API. Which sequence completes the setup?

Domain: Connect to and consume Azure services and third-party services

- A. Enable Managed Identity on the APIM instance → grant that identity RBAC or app-role access on the target backend/Key Vault → add authentication-managed-identity in APIM policy XML → test backend calls and inspect APIM trace headers
- B. Grant RBAC to the developer laptop user → add `<validate-jwt>` in `<outbound>` → enable APIM Managed Identity → test backend
- C. Hardcode a 2-year client secret inside `<set-header>` XML → disable Managed Identity → grant RBAC → inspect trace
- D. Add authentication-managed-identity policy → test backend invocation → enable Managed Identity on APIM → grant RBAC on the target

### 73. External health-information exchanges calling Aurelia's APIM gateway must supply a Product Subscription Key, pass mTLS client certificate thumbprint verification, and present an Entra JWT carrying `roles: ["Orders.Write"]` (or clinical write role). Which two APIM configurations enforce this defense-in-depth? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- B. Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers
- E. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 74. An APIM operation must return HTTP `401` immediately whenever a caller's `Authorization` bearer token lacks the expected Entra audience or required role claim (`<inbound> ____ </inbound>`). Which policy element performs this check?

Domain: Connect to and consume Azure services and third-party services

- A. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- B. Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 75. A public clinic-directory API on APIM needs per-subscription burst rate limits (`429`) and monthly quotas (`403`) preserving `<base />`, 300-second localized response caching by `Accept-Language`, and 3x backend 5xx retries with outbound `X-AspNet-Version` stripping. Which three APIM policy patterns implement this? Select three.

Domain: Connect to and consume Azure services and third-party services

- A. Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- E. Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`
- F. Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`

### 76. Spanish-speaking patients calling `GET /formulary` with `Accept-Language: es-MX` occasionally receive cached English JSON from APIM because `<cache-lookup>` omitted header variation (` ____ `). How must the caching policies be configured?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 77. Security penetration testers flag `X-AspNet-Version` and internal headers on responses from an APIM-fronted EHR service, and transient HTTP 502 blips from backend pods surface directly to partners. Which APIM policy placement resolves both findings?

Domain: Connect to and consume Azure services and third-party services

- A. Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 78. A regional health network notifies 600 affiliated clinics of patient discharge events — isolating each clinic's topic via Azure RBAC under one publish endpoint — using `CloudEvents v1.0` subject prefix filters and 24-hour Blob dead-lettering. Which two Event Grid capabilities fit? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization
- E. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors

### 79. A partner radiology HTTPS webhook written in ASP.NET Core rejects Event Grid subscription creation until endpoint ownership validation is added (` ____ `). How must the webhook handle the handshake?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- D. Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`

### 80. Proposed solution: Subscribe an oncology webhook to a storage account's Event Grid system topic with zero filters and discard 99% of non-DICOM `.txt` and `.tmp` uploads inside paid Function compute. Which Event Grid configuration eliminates wasted invocations?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors

### 81. A medical credentialing SaaS needs 4,000 tenant-isolated event topics so each hospital system subscribes strictly to its own physician-license alerts without hitting subscription custom-topic limits. Which Event Grid resource is built for this?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- C. Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

### 82. ICU bedside monitors emit 60,000 vitals packets per second; three clinical AI pipelines need independent stream cursors, and raw packets must also land as Parquet files in ADLS Gen2 for research with zero custom archiver code. Which Event Hubs setup meets all requirements?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- C. Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 83. Whenever a clinical `EventProcessorClient` pod restarts during rolling updates, it reprocesses every vitals batch since partition lease creation (`await eventArgs. ____ `). What call must be added after idempotent database writes?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Host `EventProcessorClient` backed by `BlobContainerClient` and call `await eventArgs.UpdateCheckpointAsync()` after idempotent batch persistence so partition leases resume cleanly after rebalancing
- C. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 84. Hospital pharmacy orders published to Azure Service Bus must fan out to cold-chain and controlled-substance subscribers via fast header matching, suppress duplicate `MessageId` resends from ward scanners, and isolate poison payloads after `MaxDeliveryCount` failures. Which two Service Bus designs apply? Select two.

Domain: Connect to and consume Azure services and third-party services

- A. Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors
- B. Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Use Azure Service Bus Topics with `SqlRuleFilter` / `CorrelationRuleFilter` (`CorrelationRuleFilter` preferred for high throughput) and `SqlRuleAction` header stamping, inspecting `$DeadLetterQueue` (`SubQueue.DeadLetter`) after `MaxDeliveryCount` expires
- E. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 85. Proposed solution: Configure `ServiceBusProcessor` in `ReceiveAndDelete` mode for critical HL7 billing claims so messages vanish from the queue the instant they arrive at the worker pod. Why is this risky, and what replaces it?

Domain: Connect to and consume Azure services and third-party services

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Use `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false`, calling `CompleteMessageAsync` after commit, `AbandonMessageAsync` for transient retries, and `DeadLetterMessageAsync` on unrecoverable schema errors
- C. Keep the default `--restart-policy Always` on a run-once batch container group
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 86. After booking a telemed consultation, the API schedules a reminder message 30 minutes before the visit (`long seq = await sender. ____ `) and cancels it if the patient reschedules. Which Service Bus SDK method pair handles this?

Domain: Connect to and consume Azure services and third-party services

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `long seq = await sender.ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` and persist `seq` to call `CancelScheduledMessageAsync(seq)` if the user cancels early

### 87. A genomics lab queues 220 TB of 12 KB pointer jobs pointing to FASTQ files in Blob Storage, needing simple visibility timeouts and 7-day retention at minimal cost without FIFO sessions. Why should the team pick Azure Queue Storage over Service Bus?

Domain: Connect to and consume Azure services and third-party services

- A. Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 88. A C# Queue Storage worker processing corrupted HL7 claim pointers sees the same bad message reappear endlessly after visibility timeouts expire (`if (msg. ____ > 5)`). How should poison messages and deletions be handled?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

---

## Case study — Aurelia Health

Aurelia Health operates a patient-scheduling Web App on Azure App Service Premium v3 and an isolated worker Azure Functions app on Flex Consumption. Clinicians sign in with Microsoft Entra ID and view team shift calendars pulled from Microsoft Graph. Audit compliance requires capturing HTTP 5xx server diagnostics to Blob Storage for 90 days and rotating all Key Vault secrets without restarting web workers.

The next 3 questions refer to **Aurelia Health**. Read the scenario brief once, then answer each item independently.

### 89. Aurelia's FHIR HL7 normalization service runs inside a VNet-injected Azure Container Apps environment and must be reachable exclusively by internal patient-portal pods rather than the public internet. Which ingress setting enforces this boundary?

Domain: Develop Azure compute solutions

- A. Keep the default `--restart-policy Always` on a run-once batch container group
- B. Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision
- C. Configure `ingress.external: false` inside a VNet-integrated Container Apps environment so the endpoint resolves only to internal environment/VNet callers
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 90. HIPAA retention rules require diagnostic DICOM radiology images stored in Azure Blob Storage to resist modification or deletion for seven years, even by subscription administrators. Which Blob Storage feature satisfies this mandate?

Domain: Develop for Azure storage

- A. Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

### 91. Aurelia's clinical portal issues 10-minute HTTPS download links for DICOM study archives while Shared Key access is disabled across all clinical storage accounts. Which SAS mechanism must the C# API use?

Domain: Implement Azure security

- A. Mint a short-lived HTTPS-only (`SasProtocol.HttpsOnly`) User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` instead of Account or Service SAS signed with storage account keys
- B. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

---

## Case study — Solace Telemed

Solace Telemed fronts twelve internal clinical microservices with Azure API Management inside a virtual network. Partner clinics authenticate with mutual TLS client certificates plus subscription keys, GET lookups on `/formulary` should be cached for 300 seconds per `Accept-Language` header, and backend `X-AspNet-Version` headers must never leak to external callers.

The next 3 questions refer to **Solace Telemed**. Read the scenario brief once, then answer each item independently.

### 92. When a clinician signs into Solace's React portal and calls the ASP.NET Core Visit API, the API must exchange the clinician's bearer token (` ____ `) to book a Microsoft Teams meeting on their calendar via Microsoft Graph. Which MSAL call performs this exchange?

Domain: Implement Azure security

- A. Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps
- B. Call `await confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` inside the middle-tier API
- C. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

### 93. Solace stores telehealth video-codec feature flags and Key Vault secret references in Azure App Configuration and requires zero-restart updates gated by a sentinel key. Which ordered setup enables dynamic refresh?

Domain: Implement Azure security

- A. Enable Managed Identity with App Configuration Data Reader + Key Vault Secrets User → add Key Vault references and a sentinel key → wire AddAzureAppConfiguration with ConfigureKeyVault and ConfigureRefresh → invoke UseAzureAppConfiguration middleware
- B. Copy plaintext Key Vault secret values into appsettings.json → commit to Git → wire ConfigureRefresh → enable Managed Identity
- C. Add Key Vault references → wire ConfigureRefresh without UseAzureAppConfiguration middleware → expect background timer push updates → grant RBAC later
- D. Grant only App Configuration Data Reader (no Key Vault role) → invoke UseAzureAppConfiguration → add sentinel key → register AddAzureAppConfiguration

### 94. Solace wants Application Insights to verify TLS certificate validity and HTTP 200 readiness on `https://intake.solacetelemed.example` from five geographies and page engineers only if two or more regions fail simultaneously. Which setup meets this requirement?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal

---

## Case study — Trellis Diagnostics

Trellis Diagnostics streams 40,000 analyzer telemetry frames per second from hospital labs into Azure Event Hubs (16 partitions). Two independent consumers — a live anomaly-scoring Container App and an archival compliance indexer — must read the full stream concurrently at their own offsets while raw Avro batches land automatically in Azure Data Lake Storage Gen2 every five minutes.

The next 3 questions refer to **Trellis Diagnostics**. Read the scenario brief once, then answer each item independently.

### 95. Trellis lab analyzers stream 25,000 blood-panel telemetry events per second into Azure Event Hubs, and a .NET 8 worker must consume partitions with durable Blob Storage offset checkpoints. Which sequence implements the consumer?

Domain: Connect to and consume Azure services and third-party services

- A. Point all five independent microservices at `$Default` with one shared Blob prefix → call StopProcessingAsync → call StartProcessingAsync → skip UpdateCheckpointAsync
- B. Create the Event Hub, consumer group, and Blob checkpoint container → instantiate BlobContainerClient and EventProcessorClient → register ProcessEventAsync (calling UpdateCheckpointAsync) and ProcessErrorAsync → call StartProcessingAsync before StopProcessingAsync
- C. Call StartProcessingAsync → register ProcessEventAsync without ProcessErrorAsync → create the Event Hub → create the Blob container
- D. Instantiate EventHubProducerClient → call UpdateCheckpointAsync on the producer → register ProcessEventAsync → call StopProcessingAsync first

### 96. Every newly inserted abnormal lab result in Trellis's Cosmos DB `specimens` container must invoke an isolated-worker C# Function (` ____ `) to notify on-call pathologists. Which trigger attribute wires this pipeline?

Domain: Develop for Azure storage

- A. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- B. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- C. Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction
- D. Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`

### 97. Intermittent HTTP 500 errors hit Trellis's lab-accessioning endpoint, and engineers want a KQL query joining failed `AppRequests` with failed downstream `AppDependencies` on shared correlation IDs (` ____ `). Which query isolates the failing downstream call?

Domain: Monitor, troubleshoot, and optimize Azure solutions

- A. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- B. Run `AppRequests | where ResultCode == "500" | join kind=inner (AppDependencies | where Success == false) on OperationId | project TimeGenerated, Name, Target, DependencyType, ResultCode1`
- C. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- D. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules

---

## Case study — Vireo Specialty Pharmacy

Vireo Specialty Pharmacy stores prescription fulfillment documents in Azure Cosmos DB for NoSQL using hierarchical partition keys (`/clinicId`, `/patientId`). Pharmacists must always read their own in-session writes immediately, while two downstream microservices — cold-chain label printing and insurer EDI notification — must react independently to every newly created or updated prescription item.

The next 3 questions refer to **Vireo Specialty Pharmacy**. Read the scenario brief once, then answer each item independently.

### 98. Prescription adjudication steps for a given `rxNumber` must execute in strict first-in-first-out sequence across scaled C# workers without interleaving different steps for the same prescription. Which sequence configures Azure Service Bus properly?

Domain: Connect to and consume Azure services and third-party services

- A. Create a standard queue with RequiresSession = false → send messages without SessionId → toggle RequiresSession = true later → read with standard ServiceBusReceiver
- B. Create ServiceBusSessionProcessor → send messages with null SessionId → create the queue → complete messages before receiving
- C. Send messages to Queue Storage with SessionId → attach ServiceBusSessionProcessor → toggle FIFO → complete locks
- D. Create the queue or subscription with RequiresSession = true at creation time → send ServiceBusMessage instances setting a non-empty SessionId → create a ServiceBusSessionProcessor (or AcceptNextSessionAsync receiver) → process messages in order and complete/renew session locks

### 99. Vireo encrypts Controlled Substance DEA audit exports locally with a per-file symmetric AES key (`dekBytes`) and wraps that key using an HSM-protected RSA key in Azure Key Vault (` ____ `). Which SDK client and method perform this operation?

Domain: Implement Azure security

- A. Instantiate `new CryptographyClient(keyVaultKey.Id, new DefaultAzureCredential())` and invoke `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync(...)`
- B. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file

### 100. External PBM clearinghouses call Vireo's formulary API through Azure API Management and must be capped at 60 burst calls per minute (HTTP `429`) and 5,000 calls per month (HTTP `403`) without losing parent `<inbound>` policies. How should the policy XML be authored?

Domain: Connect to and consume Azure services and third-party services

- A. Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules
- B. Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`
- C. Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal
- D. Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price

---

## Answer key and explanations

### Question 1 — B, C

Answers: Use a multi-stage Dockerfile building in `mcr.microsoft.com/dotnet/sdk:8.0` and copying published output into `mcr.microsoft.com/dotnet/aspnet:8.0` with a non-root `USER app`; Declare `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form so `SIGTERM` reaches the .NET host cleanly during container shutdown. Using a multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root build trims compiler bloat, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to the .NET host as PID 1. Local study-map skill 1.1 (Create and Manage Container Images and Multi-Stage Dockerfiles), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Using a multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root build trims compiler bloat, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to the .NET host as PID 1.
- **B:** Correct. Multi-stage Docker builds exclude compiler SDK layers and source files from the final runtime image, shrinking image size and attack surface. In this scenario: Using a multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root build trims compiler bloat, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to the .NET host as PID 1.
- **C:** Correct. Exec-form `ENTRYPOINT` runs the process as PID 1 without an intermediate `/bin/sh -c` wrapper that swallows POSIX termination signals. In this scenario: Using a multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root build trims compiler bloat, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to the .NET host as PID 1.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Using a multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root build trims compiler bloat, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to the .NET host as PID 1.
- **E:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Using a multi-stage `dotnet/sdk:8.0` -> `dotnet/aspnet:8.0` non-root build trims compiler bloat, and exec-form `ENTRYPOINT ["dotnet", "Api.dll"]` delivers `SIGTERM` directly to the .NET host as PID 1.

### Question 2 — D

Answer: Add `bin/`, `obj/`, `.git/`, and local `.env` files to `.dockerignore` before running `docker build` or `az acr build`. Listing `bin/`, `obj/`, `.git/`, and `.env` inside `.dockerignore` excludes local build artifacts and stray secrets before the CLI tars and uploads the build context. `.dockerignore` prevents streaming gigabytes of local build artifacts and stray secrets into the build context. Local study-map skill 1.1 (Create and Manage Container Images and Multi-Stage Dockerfiles), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Listing `bin/`, `obj/`, `.git/`, and `.env` inside `.dockerignore` excludes local build artifacts and stray secrets before the CLI tars and uploads the build context.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Listing `bin/`, `obj/`, `.git/`, and `.env` inside `.dockerignore` excludes local build artifacts and stray secrets before the CLI tars and uploads the build context.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Listing `bin/`, `obj/`, `.git/`, and `.env` inside `.dockerignore` excludes local build artifacts and stray secrets before the CLI tars and uploads the build context.
- **D:** Correct. `.dockerignore` prevents streaming gigabytes of local build artifacts and stray secrets into the build context. In this scenario: Listing `bin/`, `obj/`, `.git/`, and `.env` inside `.dockerignore` excludes local build artifacts and stray secrets before the CLI tars and uploads the build context.

### Question 3 — A

Answer: Execute `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine`. `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine` imports external images server-side without a local Docker daemon. `az acr import` copies public or cross-registry container images server-side into ACR without requiring `docker pull` / `docker push` on a local workstation. Local study-map skill 1.2 (Publish Images, Run ACR Tasks, and Manage Auth/Purge in Azure Container Registry), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. `az acr import` copies public or cross-registry container images server-side into ACR without requiring `docker pull` / `docker push` on a local workstation. In this scenario: `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine` imports external images server-side without a local Docker daemon.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine` imports external images server-side without a local Docker daemon.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine` imports external images server-side without a local Docker daemon.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine` imports external images server-side without a local Docker daemon.

### Question 4 — B

Answer: Upgrade Azure Container Registry to the `Premium` SKU and configure geo-replication into each target compute region. `Basic` and `Standard` ACR tiers lack geo-replication; upgrading ACR to `Premium` and adding regional replicas serves fast local pulls under one login server FQDN. ACR geo-replication requires the `Premium` tier and serves local regional layer pulls through a single registry login server FQDN. Local study-map skill 1.2 (Publish Images, Run ACR Tasks, and Manage Auth/Purge in Azure Container Registry), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `Basic` and `Standard` ACR tiers lack geo-replication; upgrading ACR to `Premium` and adding regional replicas serves fast local pulls under one login server FQDN.
- **B:** Correct. ACR geo-replication requires the `Premium` tier and serves local regional layer pulls through a single registry login server FQDN. In this scenario: `Basic` and `Standard` ACR tiers lack geo-replication; upgrading ACR to `Premium` and adding regional replicas serves fast local pulls under one login server FQDN.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `Basic` and `Standard` ACR tiers lack geo-replication; upgrading ACR to `Premium` and adding regional replicas serves fast local pulls under one login server FQDN.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `Basic` and `Standard` ACR tiers lack geo-replication; upgrading ACR to `Premium` and adding regional replicas serves fast local pulls under one login server FQDN.

### Question 5 — C

Answer: Pass sensitive tokens via `--secure-environment-variables` (or a secret volume mount) so values never appear in Azure Portal properties or `az container show` plaintext output. Passing secrets via `--secure-environment-variables` (or mounting a secret volume) redacts sensitive values from ARM read responses and portal views. Secure environment variables and secret volumes redact secret values from ARM/CLI read responses. Local study-map skill 1.3 (Run Container Groups, Sidecars, Volumes, and Restart Policies in Azure Container Instances), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Passing secrets via `--secure-environment-variables` (or mounting a secret volume) redacts sensitive values from ARM read responses and portal views.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Passing secrets via `--secure-environment-variables` (or mounting a secret volume) redacts sensitive values from ARM read responses and portal views.
- **C:** Correct. Secure environment variables and secret volumes redact secret values from ARM/CLI read responses. In this scenario: Passing secrets via `--secure-environment-variables` (or mounting a secret volume) redacts sensitive values from ARM read responses and portal views.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Passing secrets via `--secure-environment-variables` (or mounting a secret volume) redacts sensitive values from ARM read responses and portal views.

### Question 6 — B

Answer: Set `--restart-policy OnFailure` (or `Never`) on the Azure Container Instances container group so batch containers stop billing vCPU/memory seconds once exit code 0 completes. `--restart-policy OnFailure` restarts crashed containers (`exit != 0`) while halting execution and billing once `exit == 0` succeeds. ACI bills per second while containers run; `OnFailure` retries crashes (`exit != 0`) and halts cleanly on `exit == 0`, whereas `Always` loops forever. Local study-map skill 1.3 (Run Container Groups, Sidecars, Volumes, and Restart Policies in Azure Container Instances), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `--restart-policy OnFailure` restarts crashed containers (`exit != 0`) while halting execution and billing once `exit == 0` succeeds.
- **B:** Correct. ACI bills per second while containers run; `OnFailure` retries crashes (`exit != 0`) and halts cleanly on `exit == 0`, whereas `Always` loops forever. In this scenario: `--restart-policy OnFailure` restarts crashed containers (`exit != 0`) while halting execution and billing once `exit == 0` succeeds.
- **C:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: `--restart-policy OnFailure` restarts crashed containers (`exit != 0`) while halting execution and billing once `exit == 0` succeeds.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `--restart-policy OnFailure` restarts crashed containers (`exit != 0`) while halting execution and billing once `exit == 0` succeeds.

### Question 7 — B

Answer: Build and push the image to ACR with az acr build → create a user-assigned managed identity and grant AcrPull on the registry → create the Container Apps environment → create the container app referencing the identity and registry server. Creating the user-assigned identity, granting `AcrPull` on ACR, and passing `--user-assigned` plus `--registry-identity` during `az containerapp create` authenticates image pulls on initial deployment. The image and AcrPull identity grant must exist before Container Apps pulls the image from ACR without admin credentials. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Role assignment cannot precede creating the managed identity, and the container app revision fails if the image has not been pushed. Why the keyed choice wins: Creating the user-assigned identity, granting `AcrPull` on ACR, and passing `--user-assigned` plus `--registry-identity` during `az containerapp create` authenticates image pulls on initial deployment.
- **B:** Correct. The image and AcrPull identity grant must exist before Container Apps pulls the image from ACR without admin credentials. In this scenario: Creating the user-assigned identity, granting `AcrPull` on ACR, and passing `--user-assigned` plus `--registry-identity` during `az containerapp create` authenticates image pulls on initial deployment.
- **C:** Incorrect for this requirement. A container app cannot be created before its environment exists or pull an image before AcrPull and the image tag exist. Why the keyed choice wins: Creating the user-assigned identity, granting `AcrPull` on ACR, and passing `--user-assigned` plus `--registry-identity` during `az containerapp create` authenticates image pulls on initial deployment.
- **D:** Incorrect for this requirement. Enabling admin passwords violates credential-free deployment, and revoking AcrPull breaks subsequent revision pulls. Why the keyed choice wins: Creating the user-assigned identity, granting `AcrPull` on ACR, and passing `--user-assigned` plus `--registry-identity` during `az containerapp create` authenticates image pulls on initial deployment.

### Question 8 — A, E, F

Answers: Register a Dapr state or pub/sub component in the Container Apps environment and restrict access via the component `scopes` array to specific `daprAppId` values; Configure a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0` and Managed Identity (`identity` property) so replicas scale to zero when idle and wake on queue depth; Define a Container App secret using `keyVaultUrl` plus `identity` (managed identity resource ID or `system`) and map container environment variables via `secretRef`. Restricting Dapr component `scopes` to target `daprAppId` values isolates state access, KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, and `keyVaultUrl` + `identity` secret references inject secrets cleanly. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Dapr `scopes` confine which microservices inside a shared Container Apps environment can load or invoke a component. In this scenario: Restricting Dapr component `scopes` to target `daprAppId` values isolates state access, KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, and `keyVaultUrl` + `identity` secret references inject secrets cleanly.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Restricting Dapr component `scopes` to target `daprAppId` values isolates state access, KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, and `keyVaultUrl` + `identity` secret references inject secrets cleanly.
- **C:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Restricting Dapr component `scopes` to target `daprAppId` values isolates state access, KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, and `keyVaultUrl` + `identity` secret references inject secrets cleanly.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Restricting Dapr component `scopes` to target `daprAppId` values isolates state access, KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, and `keyVaultUrl` + `identity` secret references inject secrets cleanly.
- **E:** Correct. Key Vault secret references in Container Apps resolve secrets via Managed Identity without storing secret strings in ARM templates. In this scenario: Restricting Dapr component `scopes` to target `daprAppId` values isolates state access, KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, and `keyVaultUrl` + `identity` secret references inject secrets cleanly.
- **F:** Correct. Container Apps uses KEDA scalers to scale down to zero on consumption/workload profiles and authenticate scalers cleanly via Managed Identity. In this scenario: Restricting Dapr component `scopes` to target `daprAppId` values isolates state access, KEDA `azure-servicebus` rules with `minReplicas: 0` + Managed Identity scale to zero, and `keyVaultUrl` + `identity` secret references inject secrets cleanly.

### Question 9 — A

Answer: Set `--revision-mode multiple` and apply `az containerapp ingress traffic set --revision-weight` to split live HTTP requests across named revisions. Single-revision mode deactivates old revisions automatically; switching to `--revision-mode multiple` keeps concurrent revisions active for weighted HTTP traffic splitting. Multiple-revision mode keeps more than one revision active simultaneously for weighted blue/green or canary traffic splitting. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Multiple-revision mode keeps more than one revision active simultaneously for weighted blue/green or canary traffic splitting. In this scenario: Single-revision mode deactivates old revisions automatically; switching to `--revision-mode multiple` keeps concurrent revisions active for weighted HTTP traffic splitting.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Single-revision mode deactivates old revisions automatically; switching to `--revision-mode multiple` keeps concurrent revisions active for weighted HTTP traffic splitting.
- **C:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Single-revision mode deactivates old revisions automatically; switching to `--revision-mode multiple` keeps concurrent revisions active for weighted HTTP traffic splitting.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Single-revision mode deactivates old revisions automatically; switching to `--revision-mode multiple` keeps concurrent revisions active for weighted HTTP traffic splitting.

### Question 10 — A

Answer: Provision at least a `Standard` (`S1+`) or `Premium v3` (`P1v3+`) App Service plan to unlock deployment slots, custom domain SNI SSL, and metric/schedule autoscaling. Upgrading from `Shared (D1)` to at least `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks custom domain SSL, deployment slots, and rule-based horizontal autoscale. `Free`, `Shared`, and `Basic` plans omit deployment slots (`S1` gives 5, `P1v3` gives 20) and rule-based autoscale (`S1+` required). Local study-map skill 1.5 (Create Azure App Service Plans and Web Apps Across Linux and Windows Runtimes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. `Free`, `Shared`, and `Basic` plans omit deployment slots (`S1` gives 5, `P1v3` gives 20) and rule-based autoscale (`S1+` required). In this scenario: Upgrading from `Shared (D1)` to at least `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks custom domain SSL, deployment slots, and rule-based horizontal autoscale.
- **B:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Upgrading from `Shared (D1)` to at least `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks custom domain SSL, deployment slots, and rule-based horizontal autoscale.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Upgrading from `Shared (D1)` to at least `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks custom domain SSL, deployment slots, and rule-based horizontal autoscale.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Upgrading from `Shared (D1)` to at least `Standard (S1+)` or `Premium v3 (P1v3+)` unlocks custom domain SSL, deployment slots, and rule-based horizontal autoscale.

### Question 11 — C

Answer: Set `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` inside the final `.NET 8` runtime stage and match `targetPort: 8080` on Container Apps ingress. Declaring `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` (paired with `WEBSITES_PORT=8080` on App Service or `targetPort: 8080`) aligns non-root .NET 8 listeners with platform routing. Starting in .NET 8, official Microsoft container images default to non-root port `8080` rather than privileged port `80`. Local study-map skill 1.5 (Create Azure App Service Plans and Web Apps Across Linux and Windows Runtimes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Declaring `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` (paired with `WEBSITES_PORT=8080` on App Service or `targetPort: 8080`) aligns non-root .NET 8 listeners with platform routing.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Declaring `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` (paired with `WEBSITES_PORT=8080` on App Service or `targetPort: 8080`) aligns non-root .NET 8 listeners with platform routing.
- **C:** Correct. Starting in .NET 8, official Microsoft container images default to non-root port `8080` rather than privileged port `80`. In this scenario: Declaring `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` (paired with `WEBSITES_PORT=8080` on App Service or `targetPort: 8080`) aligns non-root .NET 8 listeners with platform routing.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Declaring `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` (paired with `WEBSITES_PORT=8080` on App Service or `targetPort: 8080`) aligns non-root .NET 8 listeners with platform routing.

### Question 12 — C

Answer: Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances. Enabling Application Logging (Blob) pointed at an Azure Blob Storage container persists logs across all scaled instances according to the configured retention days without 12-hour filesystem shutoff. Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy. Local study-map skill 1.6 (Configure App Service Diagnostics, Application/Web Server Logging, and Log Streaming), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Enabling Application Logging (Blob) pointed at an Azure Blob Storage container persists logs across all scaled instances according to the configured retention days without 12-hour filesystem shutoff.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Enabling Application Logging (Blob) pointed at an Azure Blob Storage container persists logs across all scaled instances according to the configured retention days without 12-hour filesystem shutoff.
- **C:** Correct. Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy. In this scenario: Enabling Application Logging (Blob) pointed at an Azure Blob Storage container persists logs across all scaled instances according to the configured retention days without 12-hour filesystem shutoff.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enabling Application Logging (Blob) pointed at an Azure Blob Storage container persists logs across all scaled instances according to the configured retention days without 12-hour filesystem shutoff.

### Question 13 — B

Answer: Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`. Running `az webapp log tail --name <app> --resource-group <rg>` after enabling filesystem logging streams Kudu live application logs to the terminal. `az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting. Local study-map skill 1.6 (Configure App Service Diagnostics, Application/Web Server Logging, and Log Streaming), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Running `az webapp log tail --name <app> --resource-group <rg>` after enabling filesystem logging streams Kudu live application logs to the terminal.
- **B:** Correct. `az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting. In this scenario: Running `az webapp log tail --name <app> --resource-group <rg>` after enabling filesystem logging streams Kudu live application logs to the terminal.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Running `az webapp log tail --name <app> --resource-group <rg>` after enabling filesystem logging streams Kudu live application logs to the terminal.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Running `az webapp log tail --name <app> --resource-group <rg>` after enabling filesystem logging streams Kudu live application logs to the terminal.

### Question 14 — C

Answer: Set `WEBSITE_RUN_FROM_PACKAGE=1` and deploy with `az webapp deploy --type zip` so the app mounts the read-only ZIP package directly with atomic cold-start replacement. Deploying an archive with `az webapp deploy --type zip` while `WEBSITE_RUN_FROM_PACKAGE=1` is set mounts the immutable ZIP directly as `wwwroot` and flips versions atomically. Running directly from a mounted ZIP eliminates file-lock copy conflicts during `wwwroot` sync and speeds cold starts. Local study-map skill 1.7 (Deploy Code, Run-From-Package ZIPs, and Custom Containers to App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Deploying an archive with `az webapp deploy --type zip` while `WEBSITE_RUN_FROM_PACKAGE=1` is set mounts the immutable ZIP directly as `wwwroot` and flips versions atomically.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Deploying an archive with `az webapp deploy --type zip` while `WEBSITE_RUN_FROM_PACKAGE=1` is set mounts the immutable ZIP directly as `wwwroot` and flips versions atomically.
- **C:** Correct. Running directly from a mounted ZIP eliminates file-lock copy conflicts during `wwwroot` sync and speeds cold starts. In this scenario: Deploying an archive with `az webapp deploy --type zip` while `WEBSITE_RUN_FROM_PACKAGE=1` is set mounts the immutable ZIP directly as `wwwroot` and flips versions atomically.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Deploying an archive with `az webapp deploy --type zip` while `WEBSITE_RUN_FROM_PACKAGE=1` is set mounts the immutable ZIP directly as `wwwroot` and flips versions atomically.

### Question 15 — A

Answer: Disable the ACR admin account and assign the built-in `AcrPull` role on the registry to the compute resource managed identity. Assigning `AcrPull` on ACR to the Web App's system- or user-assigned Managed Identity and enabling Managed Identity pulls on the web app eliminates static registry credentials. `AcrPull` with Managed Identity eliminates shared registry passwords while granting least-privilege read-only image pulls. Local study-map skill 1.7 (Deploy Code, Run-From-Package ZIPs, and Custom Containers to App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. `AcrPull` with Managed Identity eliminates shared registry passwords while granting least-privilege read-only image pulls. In this scenario: Assigning `AcrPull` on ACR to the Web App's system- or user-assigned Managed Identity and enabling Managed Identity pulls on the web app eliminates static registry credentials.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Assigning `AcrPull` on ACR to the Web App's system- or user-assigned Managed Identity and enabling Managed Identity pulls on the web app eliminates static registry credentials.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Assigning `AcrPull` on ACR to the Web App's system- or user-assigned Managed Identity and enabling Managed Identity pulls on the web app eliminates static registry credentials.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Assigning `AcrPull` on ACR to the Web App's system- or user-assigned Managed Identity and enabling Managed Identity pulls on the web app eliminates static registry credentials.

### Question 16 — A, D

Answers: Enable `httpsOnly: true`, set `minTlsVersion: "1.2"` (or `"1.3"`), and configure `clientCertEnabled` when mutual TLS client certificates are required; Configure App Service `CORS` with explicit origin URLs (and `supportCredentials` only without wildcard `*`) so App Service handles preflight `OPTIONS` requests. Enforcing `httpsOnly: true` with `minTlsVersion: "1.2"` secures transport, and registering `https://chart.aurelia.example` explicitly in App Service `CORS` (without wildcard `*`) allows credentialed browser requests. Local study-map skill 1.8 (Configure TLS, Mutual TLS, CORS, App Settings, and Service Connections on App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Platform-level App Service CORS intercepts `OPTIONS` preflight checks; credentialed CORS forbids wildcard `*` origins. In this scenario: Enforcing `httpsOnly: true` with `minTlsVersion: "1.2"` secures transport, and registering `https://chart.aurelia.example` explicitly in App Service `CORS` (without wildcard `*`) allows credentialed browser requests.
- **B:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Enforcing `httpsOnly: true` with `minTlsVersion: "1.2"` secures transport, and registering `https://chart.aurelia.example` explicitly in App Service `CORS` (without wildcard `*`) allows credentialed browser requests.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Enforcing `httpsOnly: true` with `minTlsVersion: "1.2"` secures transport, and registering `https://chart.aurelia.example` explicitly in App Service `CORS` (without wildcard `*`) allows credentialed browser requests.
- **D:** Correct. Enforcing HTTPS redirection and minimum TLS 1.2/1.3 at the App Service front end rejects plaintext HTTP and legacy ciphers before app code runs. In this scenario: Enforcing `httpsOnly: true` with `minTlsVersion: "1.2"` secures transport, and registering `https://chart.aurelia.example` explicitly in App Service `CORS` (without wildcard `*`) allows credentialed browser requests.
- **E:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Enforcing `httpsOnly: true` with `minTlsVersion: "1.2"` secures transport, and registering `https://chart.aurelia.example` explicitly in App Service `CORS` (without wildcard `*`) allows credentialed browser requests.

### Question 17 — B

Answer: Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`. `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` configures and pins the typed SQL connection string to the target slot. `--slot-settings` pins the connection string (`SQLCONNSTR_LedgerDb`) to the target slot so slot swaps never leak staging databases into production. Local study-map skill 1.8 (Configure TLS, Mutual TLS, CORS, App Settings, and Service Connections on App Service), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` configures and pins the typed SQL connection string to the target slot.
- **B:** Correct. `--slot-settings` pins the connection string (`SQLCONNSTR_LedgerDb`) to the target slot so slot swaps never leak staging databases into production. In this scenario: `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` configures and pins the typed SQL connection string to the target slot.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` configures and pins the typed SQL connection string to the target slot.
- **D:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `az webapp config connection-string set ... --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"` configures and pins the typed SQL connection string to the target slot.

### Question 18 — A

Answer: Pair every scale-out metric rule (e.g., CPU > 75% for 10 min) with a conservative scale-in rule (e.g., CPU < 35%) and an explicit `coolDown` window plus safe default/max instance bounds. Separating scale-out (>75%) and scale-in (<35%) CPU thresholds and configuring a conservative `coolDown` interval gives newly added workers time to absorb load before re-evaluating. Asymmetric thresholds and cool-down periods prevent rapid flapping (thrashing) where instances repeatedly add and terminate. Local study-map skill 1.9 (Implement Metric-Based and Schedule-Based App Service Autoscaling Rules and Cooldowns), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Asymmetric thresholds and cool-down periods prevent rapid flapping (thrashing) where instances repeatedly add and terminate. In this scenario: Separating scale-out (>75%) and scale-in (<35%) CPU thresholds and configuring a conservative `coolDown` interval gives newly added workers time to absorb load before re-evaluating.
- **B:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Separating scale-out (>75%) and scale-in (<35%) CPU thresholds and configuring a conservative `coolDown` interval gives newly added workers time to absorb load before re-evaluating.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Separating scale-out (>75%) and scale-in (<35%) CPU thresholds and configuring a conservative `coolDown` interval gives newly added workers time to absorb load before re-evaluating.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Separating scale-out (>75%) and scale-in (<35%) CPU thresholds and configuring a conservative `coolDown` interval gives newly added workers time to absorb load before re-evaluating.

### Question 19 — C

Answer: Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps. Setting `WEBSITE_SWAP_WARMUP_PING_PATH=/healthz/warmup` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` (with `applicationInitialization`) blocks swap completion until workers report ready. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. Local study-map skill 1.9 (Implement Metric-Based and Schedule-Based App Service Autoscaling Rules and Cooldowns), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting `WEBSITE_SWAP_WARMUP_PING_PATH=/healthz/warmup` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` (with `applicationInitialization`) blocks swap completion until workers report ready.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `WEBSITE_SWAP_WARMUP_PING_PATH=/healthz/warmup` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` (with `applicationInitialization`) blocks swap completion until workers report ready.
- **C:** Correct. Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests. In this scenario: Setting `WEBSITE_SWAP_WARMUP_PING_PATH=/healthz/warmup` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` (with `applicationInitialization`) blocks swap completion until workers report ready.
- **D:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Setting `WEBSITE_SWAP_WARMUP_PING_PATH=/healthz/warmup` and `WEBSITE_SWAP_WARMUP_PING_STATUSES=200` (with `applicationInitialization`) blocks swap completion until workers report ready.

### Question 20 — C

Answer: Create the staging deployment slot on the Standard/Premium Web App → mark production-only connection strings and webhook settings as deployment slot settings → deploy and warm up the new build in staging → swap staging into production and verify health. Creating the staging slot, marking HL7 endpoint settings as slot-sticky, deploying and warming the release in staging, and executing the slot swap promotes code with zero downtime. Slot-sticky settings must be pinned before swapping so staging never inherits live payment webhooks or overwrites production secrets during swap. Local study-map skill 1.10 (Configure App Service Deployment Slots, Slot-Sticky Settings, Warm-Up, and Traffic Routing), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Deploying directly to production bypasses zero-downtime validation and swapping an empty staging slot overwrites production. Why the keyed choice wins: Creating the staging slot, marking HL7 endpoint settings as slot-sticky, deploying and warming the release in staging, and executing the slot swap promotes code with zero downtime.
- **B:** Incorrect for this requirement. Free and Basic App Service plans do not support deployment slots; Standard, Premium, or Isolated is required first. Why the keyed choice wins: Creating the staging slot, marking HL7 endpoint settings as slot-sticky, deploying and warming the release in staging, and executing the slot swap promotes code with zero downtime.
- **C:** Correct. Slot-sticky settings must be pinned before swapping so staging never inherits live payment webhooks or overwrites production secrets during swap. In this scenario: Creating the staging slot, marking HL7 endpoint settings as slot-sticky, deploying and warming the release in staging, and executing the slot swap promotes code with zero downtime.
- **D:** Incorrect for this requirement. You cannot swap a slot before creating and deploying to it, and marking settings sticky after the swap leaks staging values into production. Why the keyed choice wins: Creating the staging slot, marking HL7 endpoint settings as slot-sticky, deploying and warming the release in staging, and executing the slot swap promotes code with zero downtime.

### Question 21 — D

Answer: Mark environment-specific settings such as `PaymentWebhookUrl` and production connection strings as `slotSetting: true` (Deployment slot setting) before swapping slots. Marking the clearinghouse URL app setting as `slotSetting: true` (Deployment slot setting) keeps sandbox and production URLs pinned to their respective slots during swaps. Slot-sticky settings stay pinned to their slot (`Production` vs `Staging`) across swaps instead of traveling with the swapped code. Local study-map skill 1.10 (Configure App Service Deployment Slots, Slot-Sticky Settings, Warm-Up, and Traffic Routing), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Marking the clearinghouse URL app setting as `slotSetting: true` (Deployment slot setting) keeps sandbox and production URLs pinned to their respective slots during swaps.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Marking the clearinghouse URL app setting as `slotSetting: true` (Deployment slot setting) keeps sandbox and production URLs pinned to their respective slots during swaps.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Marking the clearinghouse URL app setting as `slotSetting: true` (Deployment slot setting) keeps sandbox and production URLs pinned to their respective slots during swaps.
- **D:** Correct. Slot-sticky settings stay pinned to their slot (`Production` vs `Staging`) across swaps instead of traveling with the swapped code. In this scenario: Marking the clearinghouse URL app setting as `slotSetting: true` (Deployment slot setting) keeps sandbox and production URLs pinned to their respective slots during swaps.

### Question 22 — C

Answer: Host the Function App on `Flex Consumption` or `Elastic Premium (EP1+)` when VNet integration, longer execution timeouts beyond 10 minutes, or pre-warmed/always-ready instances are required. `Elastic Premium (EP1+)` or `Flex Consumption` (configured with always-ready instances and VNet integration; Premium for >10-minute/unbounded timeouts) satisfies VNet connectivity, long runtimes, and warm readiness. Classic Consumption caps timeout at 10 minutes (`functionTimeout`) and cold-starts from zero; `Flex Consumption` and `Premium` add VNet outbound and pre-warmed readiness. Local study-map skill 1.11 (Create and Configure Azure Functions Apps, Hosting Plans, and host.json Settings), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `Elastic Premium (EP1+)` or `Flex Consumption` (configured with always-ready instances and VNet integration; Premium for >10-minute/unbounded timeouts) satisfies VNet connectivity, long runtimes, and warm readiness.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `Elastic Premium (EP1+)` or `Flex Consumption` (configured with always-ready instances and VNet integration; Premium for >10-minute/unbounded timeouts) satisfies VNet connectivity, long runtimes, and warm readiness.
- **C:** Correct. Classic Consumption caps timeout at 10 minutes (`functionTimeout`) and cold-starts from zero; `Flex Consumption` and `Premium` add VNet outbound and pre-warmed readiness. In this scenario: `Elastic Premium (EP1+)` or `Flex Consumption` (configured with always-ready instances and VNet integration; Premium for >10-minute/unbounded timeouts) satisfies VNet connectivity, long runtimes, and warm readiness.
- **D:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: `Elastic Premium (EP1+)` or `Flex Consumption` (configured with always-ready instances and VNet integration; Premium for >10-minute/unbounded timeouts) satisfies VNet connectivity, long runtimes, and warm readiness.

### Question 23 — D

Answer: Configure `"functionTimeout": "00:10:00"` and `"logging": { "applicationInsights": { "samplingSettings": { "isEnabled": true, "excludedTypes": "Request;Exception" } } }` inside `host.json`. Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` in `host.json` governs the entire Function host. `host.json` governs global Function host behaviors such as execution timeout and Application Insights telemetry sampling exclusions across all functions in the app. Local study-map skill 1.11 (Create and Configure Azure Functions Apps, Hosting Plans, and host.json Settings), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` in `host.json` governs the entire Function host.
- **B:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` in `host.json` governs the entire Function host.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` in `host.json` governs the entire Function host.
- **D:** Correct. `host.json` governs global Function host behaviors such as execution timeout and Application Insights telemetry sampling exclusions across all functions in the app. In this scenario: Setting `"functionTimeout": "00:10:00"` and `"excludedTypes": "Request;Exception"` under `logging.applicationInsights.samplingSettings` in `host.json` governs the entire Function host.

### Question 24 — B, D

Answers: In the .NET isolated worker model, return a custom POCO class uniting `[HttpResult]` (or `HttpResponseData`) with `[CosmosDBOutput]` / `[ServiceBusOutput]` properties; Apply `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` (or `[FixedDelayRetry]`) on the `[EventHubTrigger]` / `[TimerTrigger]` function. Returning a multi-output POCO uniting `[HttpResult]` and `[ServiceBusOutput]` handles isolated-worker bindings, and `[ExponentialBackoffRetry]` replays transient Event Hub failures before checkpointing. Local study-map skill 1.12 (Implement Azure Functions Input and Output Bindings (Isolated Worker & Declarative Bindings)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Returning a multi-output POCO uniting `[HttpResult]` and `[ServiceBusOutput]` handles isolated-worker bindings, and `[ExponentialBackoffRetry]` replays transient Event Hub failures before checkpointing.
- **B:** Correct. Function-level retry attributes replay failed executions in-memory before advancing trigger checkpoints on Event Hubs and Timer triggers. In this scenario: Returning a multi-output POCO uniting `[HttpResult]` and `[ServiceBusOutput]` handles isolated-worker bindings, and `[ExponentialBackoffRetry]` replays transient Event Hub failures before checkpointing.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Returning a multi-output POCO uniting `[HttpResult]` and `[ServiceBusOutput]` handles isolated-worker bindings, and `[ExponentialBackoffRetry]` replays transient Event Hub failures before checkpointing.
- **D:** Correct. Isolated-worker C# functions cannot use `out` parameters for bindings; multi-output types return structured properties on a single return object. In this scenario: Returning a multi-output POCO uniting `[HttpResult]` and `[ServiceBusOutput]` handles isolated-worker bindings, and `[ExponentialBackoffRetry]` replays transient Event Hub failures before checkpointing.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Returning a multi-output POCO uniting `[HttpResult]` and `[ServiceBusOutput]` handles isolated-worker bindings, and `[ExponentialBackoffRetry]` replays transient Event Hub failures before checkpointing.

### Question 25 — B

Answer: Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation. `AuthorizationLevel.Function` accepts either a function-specific key or a host key via `x-functions-key` / `?code=`, whereas `Admin` demands the `_master` key. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. Local study-map skill 1.12 (Implement Azure Functions Input and Output Bindings (Isolated Worker & Declarative Bindings)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `AuthorizationLevel.Function` accepts either a function-specific key or a host key via `x-functions-key` / `?code=`, whereas `Admin` demands the `_master` key.
- **B:** Correct. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. In this scenario: `AuthorizationLevel.Function` accepts either a function-specific key or a host key via `x-functions-key` / `?code=`, whereas `Admin` demands the `_master` key.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `AuthorizationLevel.Function` accepts either a function-specific key or a host key via `x-functions-key` / `?code=`, whereas `Admin` demands the `_master` key.
- **D:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: `AuthorizationLevel.Function` accepts either a function-specific key or a host key via `x-functions-key` / `?code=`, whereas `Admin` demands the `_master` key.

### Question 26 — D

Answer: Specify a six-field NCRONTAB expression `{second} {minute} {hour} {day} {month} {day-of-week}` such as `"0 */15 9-17 * * 1-5"` on `[TimerTrigger]`. `"0 */15 9-17 * * 1-5"` includes the mandatory leading `{second}` field required by Azure Functions NCRONTAB expressions. Azure Functions `[TimerTrigger]` uses 6-field NCRONTAB (leading seconds field), unlike 5-field Unix cron. Local study-map skill 1.13 (Implement Function Triggers Using Cosmos DB/Blob Data Operations, NCRONTAB Timers, and Webhooks), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` includes the mandatory leading `{second}` field required by Azure Functions NCRONTAB expressions.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` includes the mandatory leading `{second}` field required by Azure Functions NCRONTAB expressions.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `"0 */15 9-17 * * 1-5"` includes the mandatory leading `{second}` field required by Azure Functions NCRONTAB expressions.
- **D:** Correct. Azure Functions `[TimerTrigger]` uses 6-field NCRONTAB (leading seconds field), unlike 5-field Unix cron. In this scenario: `"0 */15 9-17 * * 1-5"` includes the mandatory leading `{second}` field required by Azure Functions NCRONTAB expressions.

### Question 27 — A

Answer: Configure `[BlobTrigger(..., Source = BlobTriggerSource.EventGrid)]` with an Event Grid system topic subscription instead of default container-log polling. Default `[BlobTrigger]` scans storage logs periodically with multi-minute latency; switching to `Source = BlobTriggerSource.EventGrid` triggers executions immediately via Event Grid push notifications. Event Grid-sourced blob triggers eliminate storage-log scan latency and work reliably on Blob-only / high-scale storage accounts. Local study-map skill 1.13 (Implement Function Triggers Using Cosmos DB/Blob Data Operations, NCRONTAB Timers, and Webhooks), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Correct. Event Grid-sourced blob triggers eliminate storage-log scan latency and work reliably on Blob-only / high-scale storage accounts. In this scenario: Default `[BlobTrigger]` scans storage logs periodically with multi-minute latency; switching to `Source = BlobTriggerSource.EventGrid` triggers executions immediately via Event Grid push notifications.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Default `[BlobTrigger]` scans storage logs periodically with multi-minute latency; switching to `Source = BlobTriggerSource.EventGrid` triggers executions immediately via Event Grid push notifications.
- **C:** Incorrect for this requirement. Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`. Why the keyed choice wins: Default `[BlobTrigger]` scans storage logs periodically with multi-minute latency; switching to `Source = BlobTriggerSource.EventGrid` triggers executions immediately via Event Grid push notifications.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Default `[BlobTrigger]` scans storage logs periodically with multi-minute latency; switching to `Source = BlobTriggerSource.EventGrid` triggers executions immediately via Event Grid push notifications.

### Question 28 — A, C, D

Answers: Define `new ContainerProperties(id: "telemetry", partitionKeyPaths: new List<string> { "/tenantId", "/siteId", "/deviceId" })` using `PartitionKeyBuilder` on reads and writes; Use `container.CreateTransactionalBatch(new PartitionKey(pkValue))` to group multiple create/replace/upsert/delete operations atomically within the same logical partition; Pass `new ItemRequestOptions { IfMatchEtag = item.ETag }` on `ReplaceItemAsync` and catch `CosmosException` when `StatusCode == HttpStatusCode.PreconditionFailed` (412). Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale tenants past 20 GB while preserving prefix queries, `CreateTransactionalBatch` commits same-partition writes atomically, and `IfMatchEtag` prevents lost updates. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Hierarchical partition keys (up to 3 levels) overcome the 20 GB logical-partition limit on large tenants while preserving efficient prefix queries on `/tenantId` alone. In this scenario: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale tenants past 20 GB while preserving prefix queries, `CreateTransactionalBatch` commits same-partition writes atomically, and `IfMatchEtag` prevents lost updates.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale tenants past 20 GB while preserving prefix queries, `CreateTransactionalBatch` commits same-partition writes atomically, and `IfMatchEtag` prevents lost updates.
- **C:** Correct. `TransactionalBatch` guarantees ACID all-or-nothing execution serialized in one network round-trip, strictly scoped to a single logical partition key. In this scenario: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale tenants past 20 GB while preserving prefix queries, `CreateTransactionalBatch` commits same-partition writes atomically, and `IfMatchEtag` prevents lost updates.
- **D:** Correct. Supplying `IfMatchEtag` enforces optimistic concurrency control so concurrent writers fail with HTTP 412 rather than silently overwriting updates. In this scenario: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale tenants past 20 GB while preserving prefix queries, `CreateTransactionalBatch` commits same-partition writes atomically, and `IfMatchEtag` prevents lost updates.
- **E:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale tenants past 20 GB while preserving prefix queries, `CreateTransactionalBatch` commits same-partition writes atomically, and `IfMatchEtag` prevents lost updates.
- **F:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Hierarchical partition keys (`/tenantId`, `/siteId`, `/deviceId`) scale tenants past 20 GB while preserving prefix queries, `CreateTransactionalBatch` commits same-partition writes atomically, and `IfMatchEtag` prevents lost updates.

### Question 29 — D

Answer: Configure `"indexingMode": "consistent"` with `"includedPaths": [{"path": "/customerId/?"}, {"path": "/createdUtc/?"}]` and `"excludedPaths": [{"path": "/*"}]`. Excluding wildcard `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing eliminates inverted-index maintenance on hundreds of unqueried waveform array fields. Excluding wildcard `/*` and indexing only queried filter paths dramatically cuts write Request Unit (RU) cost and index storage on write-heavy containers. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Excluding wildcard `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing eliminates inverted-index maintenance on hundreds of unqueried waveform array fields.
- **B:** Incorrect for this requirement. Cosmos DB for NoSQL requires a matching composite index whenever a SQL query specifies `ORDER BY` across two or more properties. Why the keyed choice wins: Excluding wildcard `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing eliminates inverted-index maintenance on hundreds of unqueried waveform array fields.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Excluding wildcard `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing eliminates inverted-index maintenance on hundreds of unqueried waveform array fields.
- **D:** Correct. Excluding wildcard `/*` and indexing only queried filter paths dramatically cuts write Request Unit (RU) cost and index storage on write-heavy containers. In this scenario: Excluding wildcard `"/*"` and including only `/customerId/?` and `/createdUtc/?` in consistent indexing eliminates inverted-index maintenance on hundreds of unqueried waveform array fields.

### Question 30 — A

Answer: Call `await container.PatchItemAsync<Order>(id, new PartitionKey(pk), new[] { PatchOperation.Increment("/retryCount", 1), PatchOperation.Set("/lastStatus", "Queued") })`. `container.PatchItemAsync<T>` applies atomic server-side `PatchOperation.Increment` and `PatchOperation.Set` mutations without round-tripping the full item body. Partial Document Update (`PatchItemAsync`) mutates specific JSON paths server-side without reading, deserializing, and replacing the full document payload. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Partial Document Update (`PatchItemAsync`) mutates specific JSON paths server-side without reading, deserializing, and replacing the full document payload. In this scenario: `container.PatchItemAsync<T>` applies atomic server-side `PatchOperation.Increment` and `PatchOperation.Set` mutations without round-tripping the full item body.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `container.PatchItemAsync<T>` applies atomic server-side `PatchOperation.Increment` and `PatchOperation.Set` mutations without round-tripping the full item body.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `container.PatchItemAsync<T>` applies atomic server-side `PatchOperation.Increment` and `PatchOperation.Set` mutations without round-tripping the full item body.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `container.PatchItemAsync<T>` applies atomic server-side `PatchOperation.Increment` and `PatchOperation.Set` mutations without round-tripping the full item body.

### Question 31 — B

Answer: Register `CosmosClient` as a process-wide singleton in dependency injection and choose a high-cardinality `PartitionKey` path (or up to 3-level `Hierarchical` subpartition paths) that distributes RU/s evenly. Registering a single thread-safe `CosmosClient` instance as a DI singleton reuses underlying TCP connections and partition routing caches across all requests. Reusing one thread-safe `CosmosClient` avoids socket exhaustion, and hierarchical/high-cardinality partition keys prevent hot partitions and 20 GB single-partition caps. Local study-map skill 2.1 (Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Registering a single thread-safe `CosmosClient` instance as a DI singleton reuses underlying TCP connections and partition routing caches across all requests.
- **B:** Correct. Reusing one thread-safe `CosmosClient` avoids socket exhaustion, and hierarchical/high-cardinality partition keys prevent hot partitions and 20 GB single-partition caps. In this scenario: Registering a single thread-safe `CosmosClient` instance as a DI singleton reuses underlying TCP connections and partition routing caches across all requests.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Registering a single thread-safe `CosmosClient` instance as a DI singleton reuses underlying TCP connections and partition routing caches across all requests.
- **D:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Registering a single thread-safe `CosmosClient` instance as a DI singleton reuses underlying TCP connections and partition routing caches across all requests.

### Question 32 — D

Answer: Use `Session` consistency (the default) and propagate `x-ms-session-token` (`RequestOptions.SessionToken`) across client/middle-tier hops to guarantee monotonic read-your-own-writes at half the read RU cost of `Strong`. Keeping `Session` consistency and passing `x-ms-session-token` (`QueryRequestOptions.SessionToken`) across client requests guarantees read-your-writes at half the RU charge of `Strong`. `Session` consistency guarantees read-your-writes, monotonic reads, and write-follows-reads within a session token at 50% of `Strong` / `BoundedStaleness` read RUs. Local study-map skill 2.2 (Select and Override Cosmos DB Consistency Levels and Session Tokens), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Keeping `Session` consistency and passing `x-ms-session-token` (`QueryRequestOptions.SessionToken`) across client requests guarantees read-your-writes at half the RU charge of `Strong`.
- **B:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Keeping `Session` consistency and passing `x-ms-session-token` (`QueryRequestOptions.SessionToken`) across client requests guarantees read-your-writes at half the RU charge of `Strong`.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Keeping `Session` consistency and passing `x-ms-session-token` (`QueryRequestOptions.SessionToken`) across client requests guarantees read-your-writes at half the RU charge of `Strong`.
- **D:** Correct. `Session` consistency guarantees read-your-writes, monotonic reads, and write-follows-reads within a session token at 50% of `Strong` / `BoundedStaleness` read RUs. In this scenario: Keeping `Session` consistency and passing `x-ms-session-token` (`QueryRequestOptions.SessionToken`) across client requests guarantees read-your-writes at half the RU charge of `Strong`.

### Question 33 — D

Answer: Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency. `BoundedStaleness` enforces global write order on secondary regions bounded by `K` versions and `T` seconds without single-region `Strong` constraints. `Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds. Local study-map skill 2.2 (Select and Override Cosmos DB Consistency Levels and Session Tokens), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `BoundedStaleness` enforces global write order on secondary regions bounded by `K` versions and `T` seconds without single-region `Strong` constraints.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `BoundedStaleness` enforces global write order on secondary regions bounded by `K` versions and `T` seconds without single-region `Strong` constraints.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `BoundedStaleness` enforces global write order on secondary regions bounded by `K` versions and `T` seconds without single-region `Strong` constraints.
- **D:** Correct. `Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds. In this scenario: `BoundedStaleness` enforces global write order on secondary regions bounded by `K` versions and `T` seconds without single-region `Strong` constraints.

### Question 34 — D

Answer: Create the monitored container and a dedicated lease container → call GetChangeFeedProcessorBuilder<T> with processorName and delegate → attach WithInstanceName and WithLeaseContainer → call Build and StartAsync on the processor. Creating the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` boots distributed change consumption cleanly. Both monitored and lease containers must exist before configuring the builder with instance/lease metadata, building the processor, and starting polling. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Builder options cannot be attached after Build(), and omitting the lease container causes startup failure. Why the keyed choice wins: Creating the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` boots distributed change consumption cleanly.
- **B:** Incorrect for this requirement. Builder method order is inverted, and using a separate dedicated lease container avoids RU contention and partition-key mismatches. Why the keyed choice wins: Creating the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` boots distributed change consumption cleanly.
- **C:** Incorrect for this requirement. A processor cannot start before it is built or before its lease container exists. Why the keyed choice wins: Creating the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` boots distributed change consumption cleanly.
- **D:** Correct. Both monitored and lease containers must exist before configuring the builder with instance/lease metadata, building the processor, and starting polling. In this scenario: Creating the monitored and `/id` lease containers first, configuring `GetChangeFeedProcessorBuilder<T>` with `WithInstanceName` and `WithLeaseContainer`, and calling `Build()` then `StartAsync()` boots distributed change consumption cleanly.

### Question 35 — C, E

Answers: Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay; Use Change Feed `AllVersionsAndDeletes` mode (or soft-delete flag items with short TTL in `LatestVersion` mode) because default `LatestVersion` change feed omits hard-deleted items. Distinct `processorName` registrations give billing and anonymization independent lease cursors, while `AllVersionsAndDeletes` mode (or soft-delete Tombstone items + TTL) captures deletions omitted by `LatestVersion`. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Distinct `processorName` registrations give billing and anonymization independent lease cursors, while `AllVersionsAndDeletes` mode (or soft-delete Tombstone items + TTL) captures deletions omitted by `LatestVersion`.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Distinct `processorName` registrations give billing and anonymization independent lease cursors, while `AllVersionsAndDeletes` mode (or soft-delete Tombstone items + TTL) captures deletions omitted by `LatestVersion`.
- **C:** Correct. Standard `LatestVersion` change feed emits only inserts and updates of current items; hard deletes require `AllVersionsAndDeletes` or soft-delete Tombstone items + TTL. In this scenario: Distinct `processorName` registrations give billing and anonymization independent lease cursors, while `AllVersionsAndDeletes` mode (or soft-delete Tombstone items + TTL) captures deletions omitted by `LatestVersion`.
- **D:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Distinct `processorName` registrations give billing and anonymization independent lease cursors, while `AllVersionsAndDeletes` mode (or soft-delete Tombstone items + TTL) captures deletions omitted by `LatestVersion`.
- **E:** Correct. In Change Feed Processor, `processorName` acts like an Event Hubs consumer group: distinct names receive independent copies of every insert/update, while identical names load-balance partitions. In this scenario: Distinct `processorName` registrations give billing and anonymization independent lease cursors, while `AllVersionsAndDeletes` mode (or soft-delete Tombstone items + TTL) captures deletions omitted by `LatestVersion`.

### Question 36 — A

Answer: Attach searchable key-value `Tags` (`SetTagsAsync` / `BlobUploadOptions.Tags`) and query across containers with `FindBlobsByTagsAsync("@container = 'docs' AND status = 'pending'")`. Attaching Blob Index `Tags` (`SetTagsAsync`) and querying `FindBlobsByTagsAsync` uses Azure Storage's native tag index without scanning containers. Blob Index Tags are indexed natively by Azure Storage for server-side filtering, whereas `Metadata` is not searchable without listing every blob. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Blob Index Tags are indexed natively by Azure Storage for server-side filtering, whereas `Metadata` is not searchable without listing every blob. In this scenario: Attaching Blob Index `Tags` (`SetTagsAsync`) and querying `FindBlobsByTagsAsync` uses Azure Storage's native tag index without scanning containers.
- **B:** Incorrect for this requirement. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. Why the keyed choice wins: Attaching Blob Index `Tags` (`SetTagsAsync`) and querying `FindBlobsByTagsAsync` uses Azure Storage's native tag index without scanning containers.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Attaching Blob Index `Tags` (`SetTagsAsync`) and querying `FindBlobsByTagsAsync` uses Azure Storage's native tag index without scanning containers.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Attaching Blob Index `Tags` (`SetTagsAsync`) and querying `FindBlobsByTagsAsync` uses Azure Storage's native tag index without scanning containers.

### Question 37 — C

Answer: Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`). Blob `Metadata` keys (`x-ms-meta-*`) must be valid C# identifiers (letters, digits, underscores — no hyphens) set via `SetMetadataAsync`, while standard HTTP headers use `SetHttpHeadersAsync(BlobHttpHeaders)`. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Blob `Metadata` keys (`x-ms-meta-*`) must be valid C# identifiers (letters, digits, underscores — no hyphens) set via `SetMetadataAsync`, while standard HTTP headers use `SetHttpHeadersAsync(BlobHttpHeaders)`.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Blob `Metadata` keys (`x-ms-meta-*`) must be valid C# identifiers (letters, digits, underscores — no hyphens) set via `SetMetadataAsync`, while standard HTTP headers use `SetHttpHeadersAsync(BlobHttpHeaders)`.
- **C:** Correct. Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary. In this scenario: Blob `Metadata` keys (`x-ms-meta-*`) must be valid C# identifiers (letters, digits, underscores — no hyphens) set via `SetMetadataAsync`, while standard HTTP headers use `SetHttpHeadersAsync(BlobHttpHeaders)`.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Blob `Metadata` keys (`x-ms-meta-*`) must be valid C# identifiers (letters, digits, underscores — no hyphens) set via `SetMetadataAsync`, while standard HTTP headers use `SetHttpHeadersAsync(BlobHttpHeaders)`.

### Question 38 — D

Answer: Call `await blobClient.CreateSnapshotAsync()` for explicit point-in-time read-only checkpoints or enable account-level Blob Versioning so every `UploadAsync` overwrite retains an immutable `VersionId`. Calling `CreateSnapshotAsync()` captures explicit point-in-time checkpoints while enabling Blob Versioning preserves automatic `VersionId` history on every overwrite. Snapshots capture explicit developer-triggered checkpoints, whereas Blob Versioning automatically preserves prior state on every overwrite or delete. Local study-map skill 2.4 (Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Calling `CreateSnapshotAsync()` captures explicit point-in-time checkpoints while enabling Blob Versioning preserves automatic `VersionId` history on every overwrite.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Calling `CreateSnapshotAsync()` captures explicit point-in-time checkpoints while enabling Blob Versioning preserves automatic `VersionId` history on every overwrite.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Calling `CreateSnapshotAsync()` captures explicit point-in-time checkpoints while enabling Blob Versioning preserves automatic `VersionId` history on every overwrite.
- **D:** Correct. Snapshots capture explicit developer-triggered checkpoints, whereas Blob Versioning automatically preserves prior state on every overwrite or delete. In this scenario: Calling `CreateSnapshotAsync()` captures explicit point-in-time checkpoints while enabling Blob Versioning preserves automatic `VersionId` history on every overwrite.

### Question 39 — A

Answer: Use `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` (15–60 seconds or `-1` infinite) and pass `LeaseId` inside `BlobRequestConditions` on subsequent writes/deletes. Calling `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and supplying the resulting `LeaseId` inside `BlobRequestConditions` blocks competing writers with HTTP `412`. Blob leases grant exclusive write/delete locks (`15` to `60` seconds or infinite `-1`) so competing workers immediately receive `412 LeaseIdMissing/Mismatch`. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Blob leases grant exclusive write/delete locks (`15` to `60` seconds or infinite `-1`) so competing workers immediately receive `412 LeaseIdMissing/Mismatch`. In this scenario: Calling `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and supplying the resulting `LeaseId` inside `BlobRequestConditions` blocks competing writers with HTTP `412`.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Calling `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and supplying the resulting `LeaseId` inside `BlobRequestConditions` blocks competing writers with HTTP `412`.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Calling `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and supplying the resulting `LeaseId` inside `BlobRequestConditions` blocks competing writers with HTTP `412`.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Calling `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` and supplying the resulting `LeaseId` inside `BlobRequestConditions` blocks competing writers with HTTP `412`.

### Question 40 — D

Answer: Invoke `BlobClient.StartCopyFromUriAsync(sourceSasUri)` to trigger asynchronous server-side blob copy and inspect `CopyStatus` without streaming bytes through the client VM. `StartCopyFromUriAsync(sourceSasUri)` delegates asynchronous server-side blob copying directly to Azure Storage fabric while `CopyStatus` reports progress. `StartCopyFromUriAsync` instructs Azure Storage fabric to copy blobs asynchronously server-to-server using a readable source URI/SAS. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `StartCopyFromUriAsync(sourceSasUri)` delegates asynchronous server-side blob copying directly to Azure Storage fabric while `CopyStatus` reports progress.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `StartCopyFromUriAsync(sourceSasUri)` delegates asynchronous server-side blob copying directly to Azure Storage fabric while `CopyStatus` reports progress.
- **C:** Incorrect for this requirement. Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime. Why the keyed choice wins: `StartCopyFromUriAsync(sourceSasUri)` delegates asynchronous server-side blob copying directly to Azure Storage fabric while `CopyStatus` reports progress.
- **D:** Correct. `StartCopyFromUriAsync` instructs Azure Storage fabric to copy blobs asynchronously server-to-server using a readable source URI/SAS. In this scenario: `StartCopyFromUriAsync(sourceSasUri)` delegates asynchronous server-side blob copying directly to Azure Storage fabric while `CopyStatus` reports progress.

### Question 41 — B

Answer: Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`. Setting `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Resource = "b"`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` enforces single-blob least privilege. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. Local study-map skill 2.5 (Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Resource = "b"`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` enforces single-blob least privilege.
- **B:** Correct. Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants. In this scenario: Setting `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Resource = "b"`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` enforces single-blob least privilege.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Resource = "b"`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` enforces single-blob least privilege.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `BlobContainerName = "exports"`, `BlobName = "manifest.csv"`, `Resource = "b"`, `Protocol = SasProtocol.HttpsOnly`, a 15-minute `ExpiresOn`, and `SetPermissions(BlobSasPermissions.Read)` enforces single-blob least privilege.

### Question 42 — B, C

Answers: Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`); Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob). A Lifecycle Management policy JSON automates `tierToCool` and `tierToArchive` age rules, while `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` expedites Archive restoration. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: A Lifecycle Management policy JSON automates `tierToCool` and `tierToArchive` age rules, while `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` expedites Archive restoration.
- **B:** Correct. Lifecycle management policies automate tier transitions and retention deletion server-side once per day without custom cron jobs. In this scenario: A Lifecycle Management policy JSON automates `tierToCool` and `tierToArchive` age rules, while `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` expedites Archive restoration.
- **C:** Correct. `SetAccessTierAsync` (or copy-to-Hot) initiates Archive rehydration; `RehydratePriority.High` prioritizes restoration (often under 1 hour for <10 GB blobs). In this scenario: A Lifecycle Management policy JSON automates `tierToCool` and `tierToArchive` age rules, while `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` expedites Archive restoration.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: A Lifecycle Management policy JSON automates `tierToCool` and `tierToArchive` age rules, while `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` expedites Archive restoration.
- **E:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: A Lifecycle Management policy JSON automates `tierToCool` and `tierToArchive` age rules, while `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` expedites Archive restoration.

### Question 43 — A

Answer: Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob). `Archive` blobs are offline and unreadable directly; calling `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or copying to a `Hot` blob) initiates priority rehydration. `SetAccessTierAsync` (or copy-to-Hot) initiates Archive rehydration; `RehydratePriority.High` prioritizes restoration (often under 1 hour for <10 GB blobs). Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. `SetAccessTierAsync` (or copy-to-Hot) initiates Archive rehydration; `RehydratePriority.High` prioritizes restoration (often under 1 hour for <10 GB blobs). In this scenario: `Archive` blobs are offline and unreadable directly; calling `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or copying to a `Hot` blob) initiates priority rehydration.
- **B:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `Archive` blobs are offline and unreadable directly; calling `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or copying to a `Hot` blob) initiates priority rehydration.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `Archive` blobs are offline and unreadable directly; calling `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or copying to a `Hot` blob) initiates priority rehydration.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `Archive` blobs are offline and unreadable directly; calling `SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or copying to a `Hot` blob) initiates priority rehydration.

### Question 44 — B, E

Answers: Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps; Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`. Building a `PublicClientApplication` using Authorization Code + PKCE and calling `AcquireTokenSilent` from the token cache before falling back on `MsalUiRequiredException` to `AcquireTokenInteractive` provides secure silent renewal. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Building a `PublicClientApplication` using Authorization Code + PKCE and calling `AcquireTokenSilent` from the token cache before falling back on `MsalUiRequiredException` to `AcquireTokenInteractive` provides secure silent renewal.
- **B:** Correct. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. In this scenario: Building a `PublicClientApplication` using Authorization Code + PKCE and calling `AcquireTokenSilent` from the token cache before falling back on `MsalUiRequiredException` to `AcquireTokenInteractive` provides secure silent renewal.
- **C:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Building a `PublicClientApplication` using Authorization Code + PKCE and calling `AcquireTokenSilent` from the token cache before falling back on `MsalUiRequiredException` to `AcquireTokenInteractive` provides secure silent renewal.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Building a `PublicClientApplication` using Authorization Code + PKCE and calling `AcquireTokenSilent` from the token cache before falling back on `MsalUiRequiredException` to `AcquireTokenInteractive` provides secure silent renewal.
- **E:** Correct. MSAL refreshes cached tokens transparently during `AcquireTokenSilent`; prompting interactively on every call degrades UX and hits rate limits. In this scenario: Building a `PublicClientApplication` using Authorization Code + PKCE and calling `AcquireTokenSilent` from the token cache before falling back on `MsalUiRequiredException` to `AcquireTokenInteractive` provides secure silent renewal.

### Question 45 — A

Answer: Use `ConfidentialClientApplicationBuilder` authenticated with a client certificate (or workload identity assertion) calling `AcquireTokenForClient(new[] { "api://.../.default" })` for headless background daemons. Headless daemons have no interactive browser user; `ConfidentialClientApplicationBuilder` with a certificate/workload assertion calling `AcquireTokenForClient` (`/.default` scope) authenticates background services cleanly. Daemon apps without a signed-in user use OAuth 2.0 Client Credentials flow and must request the `.default` scope for pre-consented application permissions. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Daemon apps without a signed-in user use OAuth 2.0 Client Credentials flow and must request the `.default` scope for pre-consented application permissions. In this scenario: Headless daemons have no interactive browser user; `ConfidentialClientApplicationBuilder` with a certificate/workload assertion calling `AcquireTokenForClient` (`/.default` scope) authenticates background services cleanly.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Headless daemons have no interactive browser user; `ConfidentialClientApplicationBuilder` with a certificate/workload assertion calling `AcquireTokenForClient` (`/.default` scope) authenticates background services cleanly.
- **C:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Headless daemons have no interactive browser user; `ConfidentialClientApplicationBuilder` with a certificate/workload assertion calling `AcquireTokenForClient` (`/.default` scope) authenticates background services cleanly.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Headless daemons have no interactive browser user; `ConfidentialClientApplicationBuilder` with a certificate/workload assertion calling `AcquireTokenForClient` (`/.default` scope) authenticates background services cleanly.

### Question 46 — A

Answer: Declare `appRoles` with `allowedMemberTypes: ["User", "Application"]` in the Entra app registration manifest and validate the `roles` claim (`[Authorize(Roles = "...")]`) in the web API. Defining `CaseReviewer` in `appRoles` with `allowedMemberTypes: ["User", "Application"]` lets admins assign the role to both user groups and enterprise service principals, emitting `roles` claims in both tokens. Entra ID emits assigned app roles inside the `roles` JWT claim for both human users and service principals without requiring directory-level Entra admin roles. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Entra ID emits assigned app roles inside the `roles` JWT claim for both human users and service principals without requiring directory-level Entra admin roles. In this scenario: Defining `CaseReviewer` in `appRoles` with `allowedMemberTypes: ["User", "Application"]` lets admins assign the role to both user groups and enterprise service principals, emitting `roles` claims in both tokens.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Defining `CaseReviewer` in `appRoles` with `allowedMemberTypes: ["User", "Application"]` lets admins assign the role to both user groups and enterprise service principals, emitting `roles` claims in both tokens.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Defining `CaseReviewer` in `appRoles` with `allowedMemberTypes: ["User", "Application"]` lets admins assign the role to both user groups and enterprise service principals, emitting `roles` claims in both tokens.
- **D:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Defining `CaseReviewer` in `appRoles` with `allowedMemberTypes: ["User", "Application"]` lets admins assign the role to both user groups and enterprise service principals, emitting `roles` claims in both tokens.

### Question 47 — D

Answer: Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation. Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) blocks personal accounts, while custom `tid` / issuer validation restricts sign-ins to enrolled hospital tenants. Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) blocks personal accounts, while custom `tid` / issuer validation restricts sign-ins to enrolled hospital tenants.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) blocks personal accounts, while custom `tid` / issuer validation restricts sign-ins to enrolled hospital tenants.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) blocks personal accounts, while custom `tid` / issuer validation restricts sign-ins to enrolled hospital tenants.
- **D:** Correct. Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`. In this scenario: Setting `signInAudience` to `AzureADMultipleOrgs` (`/organizations`) blocks personal accounts, while custom `tid` / issuer validation restricts sign-ins to enrolled hospital tenants.

### Question 48 — C

Answer: Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`). Configuring Easy Auth unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean HTTP status codes expected by native mobile and SPA API clients. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. Local study-map skill 3.2 (Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Configuring Easy Auth unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean HTTP status codes expected by native mobile and SPA API clients.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Configuring Easy Auth unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean HTTP status codes expected by native mobile and SPA API clients.
- **C:** Correct. REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header. In this scenario: Configuring Easy Auth unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean HTTP status codes expected by native mobile and SPA API clients.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Configuring Easy Auth unauthenticated requests to `Return HTTP 401 Unauthorized` returns clean HTTP status codes expected by native mobile and SPA API clients.

### Question 49 — D

Answer: Assign Storage Blob Data Contributor/Delegator RBAC to the identity → instantiate BlobServiceClient with DefaultAzureCredential → call GetUserDelegationKeyAsync for a bounded validity window → build BlobSasBuilder and sign with the user delegation key. Assigning `Storage Blob Delegator` + data RBAC, authenticating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) produces a key-free User Delegation SAS. Entra RBAC must authorize delegation before BlobServiceClient requests a user delegation key, which then signs the BlobSasBuilder token without account keys. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. The client must authenticate with Microsoft Entra credentials first so it can request the delegation key that mints the SAS. Why the keyed choice wins: Assigning `Storage Blob Delegator` + data RBAC, authenticating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) produces a key-free User Delegation SAS.
- **B:** Incorrect for this requirement. GetUserDelegationKeyAsync requires an authenticated Entra client with RBAC already granted before the call executes. Why the keyed choice wins: Assigning `Storage Blob Delegator` + data RBAC, authenticating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) produces a key-free User Delegation SAS.
- **C:** Incorrect for this requirement. A SAS cannot be signed before obtaining the user delegation key, and shared account keys cannot mint Entra user delegation SAS tokens. Why the keyed choice wins: Assigning `Storage Blob Delegator` + data RBAC, authenticating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) produces a key-free User Delegation SAS.
- **D:** Correct. Entra RBAC must authorize delegation before BlobServiceClient requests a user delegation key, which then signs the BlobSasBuilder token without account keys. In this scenario: Assigning `Storage Blob Delegator` + data RBAC, authenticating `BlobServiceClient` with `DefaultAzureCredential`, calling `GetUserDelegationKeyAsync`, and signing `BlobSasBuilder` (`HttpsOnly`) produces a key-free User Delegation SAS.

### Question 50 — C

Answer: Bind a Service SAS to a container/queue/table Stored Access Policy (`SignedIdentifier`, omitting inline start/expiry/permissions) so compromised tokens can be revoked instantly by modifying or deleting the policy. Issuing the Service SAS bound to a container `StoredAccessPolicy` (`SignedIdentifier`, omitting inline expiry/permissions) lets admins revoke access immediately by deleting or modifying that stored policy. Up to 5 Stored Access Policies per container allow instant SAS revocation without rotating storage account keys; Note that User Delegation SAS uses key revocation instead of Stored Access Policies. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Issuing the Service SAS bound to a container `StoredAccessPolicy` (`SignedIdentifier`, omitting inline expiry/permissions) lets admins revoke access immediately by deleting or modifying that stored policy.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Issuing the Service SAS bound to a container `StoredAccessPolicy` (`SignedIdentifier`, omitting inline expiry/permissions) lets admins revoke access immediately by deleting or modifying that stored policy.
- **C:** Correct. Up to 5 Stored Access Policies per container allow instant SAS revocation without rotating storage account keys; Note that User Delegation SAS uses key revocation instead of Stored Access Policies. In this scenario: Issuing the Service SAS bound to a container `StoredAccessPolicy` (`SignedIdentifier`, omitting inline expiry/permissions) lets admins revoke access immediately by deleting or modifying that stored policy.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Issuing the Service SAS bound to a container `StoredAccessPolicy` (`SignedIdentifier`, omitting inline expiry/permissions) lets admins revoke access immediately by deleting or modifying that stored policy.

### Question 51 — A, C

Answers: Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`; Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses. Requesting least-privilege scopes with `$select` + `PageIterator<T>` handles efficient paging, while `BatchRequestContentCollection` (`/$batch`) bundles up to 20 sub-requests and honors `Retry-After` on `429` responses. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Graph JSON batching (`/$batch`) bundles up to 20 sub-requests per round-trip, while built-in SDK retry middleware respects `Retry-After`. In this scenario: Requesting least-privilege scopes with `$select` + `PageIterator<T>` handles efficient paging, while `BatchRequestContentCollection` (`/$batch`) bundles up to 20 sub-requests and honors `Retry-After` on `429` responses.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Requesting least-privilege scopes with `$select` + `PageIterator<T>` handles efficient paging, while `BatchRequestContentCollection` (`/$batch`) bundles up to 20 sub-requests and honors `Retry-After` on `429` responses.
- **C:** Correct. Microsoft Graph enforces least-privilege consent scopes, trims payload size with `$select`, and paginates `@odata.nextLink` cleanly through `PageIterator<T>`. In this scenario: Requesting least-privilege scopes with `$select` + `PageIterator<T>` handles efficient paging, while `BatchRequestContentCollection` (`/$batch`) bundles up to 20 sub-requests and honors `Retry-After` on `429` responses.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Requesting least-privilege scopes with `$select` + `PageIterator<T>` handles efficient paging, while `BatchRequestContentCollection` (`/$batch`) bundles up to 20 sub-requests and honors `Retry-After` on `429` responses.
- **E:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Requesting least-privilege scopes with `$select` + `PageIterator<T>` handles efficient paging, while `BatchRequestContentCollection` (`/$batch`) bundles up to 20 sub-requests and honors `Retry-After` on `429` responses.

### Question 52 — C

Answer: Call `await graphClient.Users.GetAsync(rc => { rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }; rc.QueryParameters.Filter = "accountEnabled eq true"; })`. Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` trims payload fields and filters server-side. In Microsoft Graph .NET SDK v5, `$select` and `$filter` query parameters reduce payload size and network transfer on collection endpoints. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` trims payload fields and filters server-side.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` trims payload fields and filters server-side.
- **C:** Correct. In Microsoft Graph .NET SDK v5, `$select` and `$filter` query parameters reduce payload size and network transfer on collection endpoints. In this scenario: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` trims payload fields and filters server-side.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting `rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }` and `rc.QueryParameters.Filter = "accountEnabled eq true"` trims payload fields and filters server-side.

### Question 53 — D

Answer: Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`. `Directory.ReadWrite.All` violates least privilege by granting tenant-wide write control; requesting minimal read scopes (`Place.Read.All` / `Calendars.Read`) with `$select` and `PageIterator<T>` follows Graph security best practices. Microsoft Graph enforces least-privilege consent scopes, trims payload size with `$select`, and paginates `@odata.nextLink` cleanly through `PageIterator<T>`. Local study-map skill 3.4 (Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `Directory.ReadWrite.All` violates least privilege by granting tenant-wide write control; requesting minimal read scopes (`Place.Read.All` / `Calendars.Read`) with `$select` and `PageIterator<T>` follows Graph security best practices.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `Directory.ReadWrite.All` violates least privilege by granting tenant-wide write control; requesting minimal read scopes (`Place.Read.All` / `Calendars.Read`) with `$select` and `PageIterator<T>` follows Graph security best practices.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `Directory.ReadWrite.All` violates least privilege by granting tenant-wide write control; requesting minimal read scopes (`Place.Read.All` / `Calendars.Read`) with `$select` and `PageIterator<T>` follows Graph security best practices.
- **D:** Correct. Microsoft Graph enforces least-privilege consent scopes, trims payload size with `$select`, and paginates `@odata.nextLink` cleanly through `PageIterator<T>`. In this scenario: `Directory.ReadWrite.All` violates least privilege by granting tenant-wide write control; requesting minimal read scopes (`Place.Read.All` / `Calendars.Read`) with `$select` and `PageIterator<T>` follows Graph security best practices.

### Question 54 — C

Answer: Wire `options.Connect(new Uri(endpoint), cred).ConfigureKeyVault(kv => kv.SetCredential(cred))` so App Configuration resolves Key Vault reference items using the app identity. Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` registers the `TokenCredential` required by the App Configuration provider to fetch referenced secrets from Key Vault. App Configuration stores only the Key Vault secret URI metadata; client code still requires `ConfigureKeyVault` credentials with `Key Vault Secrets User` rights on the target vault. Local study-map skill 3.5 (Manage Feature Flags, Labels, Sentinel Dynamic Refresh, and Key Vault References in Azure App Configuration), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` registers the `TokenCredential` required by the App Configuration provider to fetch referenced secrets from Key Vault.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` registers the `TokenCredential` required by the App Configuration provider to fetch referenced secrets from Key Vault.
- **C:** Correct. App Configuration stores only the Key Vault secret URI metadata; client code still requires `ConfigureKeyVault` credentials with `Key Vault Secrets User` rights on the target vault. In this scenario: Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` registers the `TokenCredential` required by the App Configuration provider to fetch referenced secrets from Key Vault.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Chaining `.ConfigureKeyVault(kv => kv.SetCredential(cred))` registers the `TokenCredential` required by the App Configuration provider to fetch referenced secrets from Key Vault.

### Question 55 — B, C

Answers: Use `SecretClient` (`Azure.Security.KeyVault.Secrets`) for connection strings/tokens, `KeyClient` / `CryptographyClient` (`Azure.Security.KeyVault.Keys`) for RSA/EC wrap-unwrap-sign, and `CertificateClient` for X.509 lifecycle; Enable Soft Delete (mandatory on new vaults, 7–90 days) plus Purge Protection on Azure Key Vault so neither accidental deletion nor malicious principals can permanently destroy keys before retention expires. Separating operations across `SecretClient`, `KeyClient`, and `CertificateClient` with RBAC data-plane roles plus enabling Soft Delete + Purge Protection satisfies both requirements. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Separating operations across `SecretClient`, `KeyClient`, and `CertificateClient` with RBAC data-plane roles plus enabling Soft Delete + Purge Protection satisfies both requirements.
- **B:** Correct. Soft Delete allows recovery via `StartRecoverDeletedSecretAsync`, while Purge Protection blocks permanent `PurgeDeletedSecretAsync` calls during retention. In this scenario: Separating operations across `SecretClient`, `KeyClient`, and `CertificateClient` with RBAC data-plane roles plus enabling Soft Delete + Purge Protection satisfies both requirements.
- **C:** Correct. Azure Key Vault SDK v4 splits secrets, cryptographic keys, and X.509 certificates into dedicated clients and RBAC data-plane roles (`Key Vault Secrets User`, `Crypto User`, `Certificates User`). In this scenario: Separating operations across `SecretClient`, `KeyClient`, and `CertificateClient` with RBAC data-plane roles plus enabling Soft Delete + Purge Protection satisfies both requirements.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Separating operations across `SecretClient`, `KeyClient`, and `CertificateClient` with RBAC data-plane roles plus enabling Soft Delete + Purge Protection satisfies both requirements.
- **E:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Separating operations across `SecretClient`, `KeyClient`, and `CertificateClient` with RBAC data-plane roles plus enabling Soft Delete + Purge Protection satisfies both requirements.

### Question 56 — C

Answer: Configure App Service / Functions application settings using `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` (omitting secret version) paired with `Key Vault Secrets User` on the app Managed Identity. Setting the app configuration value to `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` with `Key Vault Secrets User` on Managed Identity resolves secrets transparently at the platform layer. Versionless Key Vault references automatically pull rotated secret versions within 24 hours (or immediately on config change / manual sync) with zero SDK boilerplate. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Setting the app configuration value to `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` with `Key Vault Secrets User` on Managed Identity resolves secrets transparently at the platform layer.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Setting the app configuration value to `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` with `Key Vault Secrets User` on Managed Identity resolves secrets transparently at the platform layer.
- **C:** Correct. Versionless Key Vault references automatically pull rotated secret versions within 24 hours (or immediately on config change / manual sync) with zero SDK boilerplate. In this scenario: Setting the app configuration value to `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` with `Key Vault Secrets User` on Managed Identity resolves secrets transparently at the platform layer.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting the app configuration value to `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` with `Key Vault Secrets User` on Managed Identity resolves secrets transparently at the platform layer.

### Question 57 — D

Answer: Choose a User-Assigned Managed Identity when multiple compute resources must share one pre-provisioned identity lifecycle independent of individual app deletions; choose System-Assigned when 1-to-1 fate-sharing tied to a single resource is required. A User-Assigned Managed Identity has an independent ARM lifecycle and reusable RBAC assignments shared across ephemeral resources, unlike System-Assigned identities tied 1-to-1 to a single resource's deletion. System-assigned identities are deleted automatically with their parent resource; user-assigned identities have an independent ARM lifecycle and reusable RBAC grants. Local study-map skill 3.7 (Implement System-Assigned and User-Assigned Managed Identities and DefaultAzureCredential), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: A User-Assigned Managed Identity has an independent ARM lifecycle and reusable RBAC assignments shared across ephemeral resources, unlike System-Assigned identities tied 1-to-1 to a single resource's deletion.
- **B:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: A User-Assigned Managed Identity has an independent ARM lifecycle and reusable RBAC assignments shared across ephemeral resources, unlike System-Assigned identities tied 1-to-1 to a single resource's deletion.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: A User-Assigned Managed Identity has an independent ARM lifecycle and reusable RBAC assignments shared across ephemeral resources, unlike System-Assigned identities tied 1-to-1 to a single resource's deletion.
- **D:** Correct. System-assigned identities are deleted automatically with their parent resource; user-assigned identities have an independent ARM lifecycle and reusable RBAC grants. In this scenario: A User-Assigned Managed Identity has an independent ARM lifecycle and reusable RBAC assignments shared across ephemeral resources, unlike System-Assigned identities tied 1-to-1 to a single resource's deletion.

### Question 58 — B

Answer: Instantiate `new DefaultAzureCredential(new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId })` (or set `AZURE_CLIENT_ID`). Passing `new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId }` (or setting `AZURE_CLIENT_ID`) explicitly selects the target user-assigned identity. When a host has multiple user-assigned managed identities attached, IMDS rejects ambiguous token requests unless the target `clientId` (or resource ID) is specified. Local study-map skill 3.7 (Implement System-Assigned and User-Assigned Managed Identities and DefaultAzureCredential), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Passing `new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId }` (or setting `AZURE_CLIENT_ID`) explicitly selects the target user-assigned identity.
- **B:** Correct. When a host has multiple user-assigned managed identities attached, IMDS rejects ambiguous token requests unless the target `clientId` (or resource ID) is specified. In this scenario: Passing `new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId }` (or setting `AZURE_CLIENT_ID`) explicitly selects the target user-assigned identity.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Passing `new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId }` (or setting `AZURE_CLIENT_ID`) explicitly selects the target user-assigned identity.
- **D:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Passing `new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId }` (or setting `AZURE_CLIENT_ID`) explicitly selects the target user-assigned identity.

### Question 59 — A, D

Answers: Query Workspace-based Application Insights (`AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces` or classic `requests`/`dependencies`/`exceptions`) joining on `OperationId` (`operation_Id`) to reconstruct end-to-end distributed transactions; Run `AppRequests | where TimeGenerated > ago(1h) | summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)`. Correlating `AppRequests`, `AppDependencies`, and `AppExceptions` on `OperationId` reconstructs call graphs, while `summarize countif(Success == false), percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` tracks tail latency. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. KQL `countif` and `percentile(..., 95)` grouped by `bin(TimeGenerated, 5m)` quantify error spikes and tail latency per operation over fixed time buckets. In this scenario: Correlating `AppRequests`, `AppDependencies`, and `AppExceptions` on `OperationId` reconstructs call graphs, while `summarize countif(Success == false), percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` tracks tail latency.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Correlating `AppRequests`, `AppDependencies`, and `AppExceptions` on `OperationId` reconstructs call graphs, while `summarize countif(Success == false), percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` tracks tail latency.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Correlating `AppRequests`, `AppDependencies`, and `AppExceptions` on `OperationId` reconstructs call graphs, while `summarize countif(Success == false), percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` tracks tail latency.
- **D:** Correct. W3C Trace-Context propagates `traceparent` into `operation_Id` across services so KQL joins pinpoint exact failing downstream dependencies. In this scenario: Correlating `AppRequests`, `AppDependencies`, and `AppExceptions` on `OperationId` reconstructs call graphs, while `summarize countif(Success == false), percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` tracks tail latency.
- **E:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Correlating `AppRequests`, `AppDependencies`, and `AppExceptions` on `OperationId` reconstructs call graphs, while `summarize countif(Success == false), percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)` tracks tail latency.

### Question 60 — B

Answer: Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits. Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) and awaiting a short drain delay before terminating ensures buffered telemetry transmits. Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) and awaiting a short drain delay before terminating ensures buffered telemetry transmits.
- **B:** Correct. Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics. In this scenario: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) and awaiting a short drain delay before terminating ensures buffered telemetry transmits.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) and awaiting a short drain delay before terminating ensures buffered telemetry transmits.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Calling `telemetryClient.Flush()` (or disposing the OpenTelemetry provider) and awaiting a short drain delay before terminating ensures buffered telemetry transmits.

### Question 61 — D

Answer: Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`. Registering `ActivitySource("OrderPipeline")` (or domain source) with `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` emits standard OpenTelemetry spans into Application Insights. `System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Registering `ActivitySource("OrderPipeline")` (or domain source) with `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` emits standard OpenTelemetry spans into Application Insights.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Registering `ActivitySource("OrderPipeline")` (or domain source) with `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` emits standard OpenTelemetry spans into Application Insights.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Registering `ActivitySource("OrderPipeline")` (or domain source) with `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` emits standard OpenTelemetry spans into Application Insights.
- **D:** Correct. `System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro. In this scenario: Registering `ActivitySource("OrderPipeline")` (or domain source) with `.WithTracing(b => b.AddSource(...))` and calling `Source.StartActivity(...)` emits standard OpenTelemetry spans into Application Insights.

### Question 62 — B

Answer: Create an Azure Monitor Metric Alert (Dynamic Thresholds or static p95 latency/5xx count) or Scheduled Query (KQL) Alert targeting an Action Group configured with webhook / Azure Function / email-SMS receivers. An Azure Monitor Metric Alert with Dynamic Thresholds adapts to daily/weekly seasonality and triggers an Action Group wired to the remediation Azure Function. Metric alerts offer sub-minute stateful evaluation on numeric signals, whereas Scheduled Query Rules run expressive KQL joins on log tables at configured intervals. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: An Azure Monitor Metric Alert with Dynamic Thresholds adapts to daily/weekly seasonality and triggers an Action Group wired to the remediation Azure Function.
- **B:** Correct. Metric alerts offer sub-minute stateful evaluation on numeric signals, whereas Scheduled Query Rules run expressive KQL joins on log tables at configured intervals. In this scenario: An Azure Monitor Metric Alert with Dynamic Thresholds adapts to daily/weekly seasonality and triggers an Action Group wired to the remediation Azure Function.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: An Azure Monitor Metric Alert with Dynamic Thresholds adapts to daily/weekly seasonality and triggers an Action Group wired to the remediation Azure Function.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: An Azure Monitor Metric Alert with Dynamic Thresholds adapts to daily/weekly seasonality and triggers an Action Group wired to the remediation Azure Function.

### Question 63 — C

Answer: Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group. Running a VNet-injected timer Function that tests the private HL7 endpoint and calls `TelemetryClient.TrackAvailability()` populates Application Insights Availability metrics for alert rules and Action Groups. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Running a VNet-injected timer Function that tests the private HL7 endpoint and calls `TelemetryClient.TrackAvailability()` populates Application Insights Availability metrics for alert rules and Action Groups.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Running a VNet-injected timer Function that tests the private HL7 endpoint and calls `TelemetryClient.TrackAvailability()` populates Application Insights Availability metrics for alert rules and Action Groups.
- **C:** Correct. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. In this scenario: Running a VNet-injected timer Function that tests the private HL7 endpoint and calls `TelemetryClient.TrackAvailability()` populates Application Insights Availability metrics for alert rules and Action Groups.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Running a VNet-injected timer Function that tests the private HL7 endpoint and calls `TelemetryClient.TrackAvailability()` populates Application Insights Availability metrics for alert rules and Action Groups.

### Question 64 — A, C

Answers: Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments; Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently. Adopting `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) modernizes instrumentation, while Ingestion/Adaptive Sampling controls ingestion cost without sampling Live Metrics. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Correct. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. In this scenario: Adopting `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) modernizes instrumentation, while Ingestion/Adaptive Sampling controls ingestion cost without sampling Live Metrics.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Adopting `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) modernizes instrumentation, while Ingestion/Adaptive Sampling controls ingestion cost without sampling Live Metrics.
- **C:** Correct. Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled. In this scenario: Adopting `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) modernizes instrumentation, while Ingestion/Adaptive Sampling controls ingestion cost without sampling Live Metrics.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Adopting `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) modernizes instrumentation, while Ingestion/Adaptive Sampling controls ingestion cost without sampling Live Metrics.
- **E:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Adopting `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) modernizes instrumentation, while Ingestion/Adaptive Sampling controls ingestion cost without sampling Live Metrics.

### Question 65 — C

Answer: Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments. Bare Classic `InstrumentationKey` ingestion and legacy SDK setup are superseded by Workspace-based Application Insights using `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) and `APPLICATIONINSIGHTS_CONNECTION_STRING`. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Bare Classic `InstrumentationKey` ingestion and legacy SDK setup are superseded by Workspace-based Application Insights using `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) and `APPLICATIONINSIGHTS_CONNECTION_STRING`.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Bare Classic `InstrumentationKey` ingestion and legacy SDK setup are superseded by Workspace-based Application Insights using `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) and `APPLICATIONINSIGHTS_CONNECTION_STRING`.
- **C:** Correct. Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups. In this scenario: Bare Classic `InstrumentationKey` ingestion and legacy SDK setup are superseded by Workspace-based Application Insights using `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) and `APPLICATIONINSIGHTS_CONNECTION_STRING`.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Bare Classic `InstrumentationKey` ingestion and legacy SDK setup are superseded by Workspace-based Application Insights using `Azure.Monitor.OpenTelemetry.AspNetCore` (`UseAzureMonitor()`) and `APPLICATIONINSIGHTS_CONNECTION_STRING`.

### Question 66 — D

Answer: Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently. Switching to Ingestion Sampling at the Application Insights workspace hashes `operation_Id` centrally so all spans belonging to a sampled transaction are kept together. Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled. Local study-map skill 4.3 (Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Switching to Ingestion Sampling at the Application Insights workspace hashes `operation_Id` centrally so all spans belonging to a sampled transaction are kept together.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Switching to Ingestion Sampling at the Application Insights workspace hashes `operation_Id` centrally so all spans belonging to a sampled transaction are kept together.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Switching to Ingestion Sampling at the Application Insights workspace hashes `operation_Id` centrally so all spans belonging to a sampled transaction are kept together.
- **D:** Correct. Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled. In this scenario: Switching to Ingestion Sampling at the Application Insights workspace hashes `operation_Id` centrally so all spans belonging to a sampled transaction are kept together.

### Question 67 — A

Answer: Select `Developer` (non-SLA) or `Premium` / `Standard v2` for VNet integration, and deploy the containerized APIM Self-Hosted Gateway (`mcr.microsoft.com/azure-api-management/gateway`) for hybrid on-premises/multi-cloud local traffic routing. Using APIM `Developer` or `Premium` tier with the containerized Self-Hosted Gateway deployed on-premises routes local hospital API traffic inside the LAN while syncing policy configuration outbound over port 443. Self-hosted gateways require `Developer` or `Premium` tier and keep data-plane traffic local while pulling policy updates outbound over HTTPS/443 from Azure. Local study-map skill 5.1 (Provision Azure API Management Tiers, VNet Modes, and Self-Hosted Hybrid Gateways), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Self-hosted gateways require `Developer` or `Premium` tier and keep data-plane traffic local while pulling policy updates outbound over HTTPS/443 from Azure. In this scenario: Using APIM `Developer` or `Premium` tier with the containerized Self-Hosted Gateway deployed on-premises routes local hospital API traffic inside the LAN while syncing policy configuration outbound over port 443.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Using APIM `Developer` or `Premium` tier with the containerized Self-Hosted Gateway deployed on-premises routes local hospital API traffic inside the LAN while syncing policy configuration outbound over port 443.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Using APIM `Developer` or `Premium` tier with the containerized Self-Hosted Gateway deployed on-premises routes local hospital API traffic inside the LAN while syncing policy configuration outbound over port 443.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Using APIM `Developer` or `Premium` tier with the containerized Self-Hosted Gateway deployed on-premises routes local hospital API traffic inside the LAN while syncing policy configuration outbound over port 443.

### Question 68 — B

Answer: Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`. `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects Managed Identity bearer tokens cleanly. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. Local study-map skill 5.1 (Provision Azure API Management Tiers, VNet Modes, and Self-Hosted Hybrid Gateways), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects Managed Identity bearer tokens cleanly.
- **B:** Correct. APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services. In this scenario: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects Managed Identity bearer tokens cleanly.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects Managed Identity bearer tokens cleanly.
- **D:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` paired with `<set-header name="Authorization">` injects Managed Identity bearer tokens cleanly.

### Question 69 — C

Answer: Use APIM `Revisions` to stage, test, and swap non-breaking internal changes safely on the same consumer URL (`;rev=2`), and use APIM `Versions` (path/header/query) when publishing breaking contract changes side-by-side for distinct consumer cohorts. Use `Revisions` to stage and swap non-breaking edits transparently on the existing URL, and use `Versions` to publish `/r4` and `/r5` side-by-side for distinct client cohorts. Revisions let authors edit and flip the `current` implementation transparently; Versions expose distinct URLs/headers so legacy clients keep working. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Use `Revisions` to stage and swap non-breaking edits transparently on the existing URL, and use `Versions` to publish `/r4` and `/r5` side-by-side for distinct client cohorts.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Use `Revisions` to stage and swap non-breaking edits transparently on the existing URL, and use `Versions` to publish `/r4` and `/r5` side-by-side for distinct client cohorts.
- **C:** Correct. Revisions let authors edit and flip the `current` implementation transparently; Versions expose distinct URLs/headers so legacy clients keep working. In this scenario: Use `Revisions` to stage and swap non-breaking edits transparently on the existing URL, and use `Versions` to publish `/r4` and `/r5` side-by-side for distinct client cohorts.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Use `Revisions` to stage and swap non-breaking edits transparently on the existing URL, and use `Versions` to publish `/r4` and `/r5` side-by-side for distinct client cohorts.

### Question 70 — A

Answer: Use `<mock-response status-code="200" content-type="application/json" />` during frontend parallel development, or `<rewrite-uri template="/internal/v2/orders/{orderId}" />` with `<set-backend-service base-url="..." />` in `<inbound>`. `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI examples during parallel frontend work, and `<rewrite-uri>` + `<set-backend-service>` remap public paths once the backend goes live. `<mock-response>` short-circuits backend forwarding using OpenAPI example payloads, while `<rewrite-uri>` maps public clean paths onto legacy internal routes. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. `<mock-response>` short-circuits backend forwarding using OpenAPI example payloads, while `<rewrite-uri>` maps public clean paths onto legacy internal routes. In this scenario: `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI examples during parallel frontend work, and `<rewrite-uri>` + `<set-backend-service>` remap public paths once the backend goes live.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI examples during parallel frontend work, and `<rewrite-uri>` + `<set-backend-service>` remap public paths once the backend goes live.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI examples during parallel frontend work, and `<rewrite-uri>` + `<set-backend-service>` remap public paths once the backend goes live.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<mock-response status-code="200" content-type="application/json" />` serves OpenAPI examples during parallel frontend work, and `<rewrite-uri>` + `<set-backend-service>` remap public paths once the backend goes live.

### Question 71 — D

Answer: Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation. `Anonymous` requires no function key (relying on APIM/Easy Auth/VNet restrictions), `Function` requires a function or host key (`x-functions-key`), and `Admin` requires the `_master` host key. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. Local study-map skill 5.2 (Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `Anonymous` requires no function key (relying on APIM/Easy Auth/VNet restrictions), `Function` requires a function or host key (`x-functions-key`), and `Admin` requires the `_master` host key.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `Anonymous` requires no function key (relying on APIM/Easy Auth/VNet restrictions), `Function` requires a function or host key (`x-functions-key`), and `Admin` requires the `_master` host key.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `Anonymous` requires no function key (relying on APIM/Easy Auth/VNet restrictions), `Function` requires a function or host key (`x-functions-key`), and `Admin` requires the `_master` host key.
- **D:** Correct. `AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers. In this scenario: `Anonymous` requires no function key (relying on APIM/Easy Auth/VNet restrictions), `Function` requires a function or host key (`x-functions-key`), and `Admin` requires the `_master` host key.

### Question 72 — A

Answer: Enable Managed Identity on the APIM instance → grant that identity RBAC or app-role access on the target backend/Key Vault → add authentication-managed-identity in APIM policy XML → test backend calls and inspect APIM trace headers. Enabling Managed Identity on APIM, granting that identity the backend Entra app role/RBAC, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying trace execution completes passwordless backend auth. APIM needs an active managed identity and target RBAC/app-role grant before `<authentication-managed-identity>` can mint valid Entra bearer tokens. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. APIM needs an active managed identity and target RBAC/app-role grant before `<authentication-managed-identity>` can mint valid Entra bearer tokens. In this scenario: Enabling Managed Identity on APIM, granting that identity the backend Entra app role/RBAC, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying trace execution completes passwordless backend auth.
- **B:** Incorrect for this requirement. Backend authorization checks the APIM gateway managed identity, not the developer workstation, and `<validate-jwt>` validates caller tokens in `<inbound>`. Why the keyed choice wins: Enabling Managed Identity on APIM, granting that identity the backend Entra app role/RBAC, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying trace execution completes passwordless backend auth.
- **C:** Incorrect for this requirement. Hardcoding static secrets in policy XML creates rotation debt when `<authentication-managed-identity>` handles token lifecycle natively. Why the keyed choice wins: Enabling Managed Identity on APIM, granting that identity the backend Entra app role/RBAC, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying trace execution completes passwordless backend auth.
- **D:** Incorrect for this requirement. Saving or invoking `<authentication-managed-identity>` before enabling Managed Identity and target RBAC fails token acquisition or returns 401/403. Why the keyed choice wins: Enabling Managed Identity on APIM, granting that identity the backend Entra app role/RBAC, adding `<authentication-managed-identity>` inside `<inbound>`, and verifying trace execution completes passwordless backend auth.

### Question 73 — B, D

Answers: Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers; Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`. Enforcing Product Subscription Keys + client certificate thumbprint checks alongside `<validate-jwt>` with `<openid-config>`, `<audiences>`, and `<required-claims>` inside `<inbound>` validates every caller credential at the edge. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: Enforcing Product Subscription Keys + client certificate thumbprint checks alongside `<validate-jwt>` with `<openid-config>`, `<audiences>`, and `<required-claims>` inside `<inbound>` validates every caller credential at the edge.
- **B:** Correct. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. In this scenario: Enforcing Product Subscription Keys + client certificate thumbprint checks alongside `<validate-jwt>` with `<openid-config>`, `<audiences>`, and `<required-claims>` inside `<inbound>` validates every caller credential at the edge.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Enforcing Product Subscription Keys + client certificate thumbprint checks alongside `<validate-jwt>` with `<openid-config>`, `<audiences>`, and `<required-claims>` inside `<inbound>` validates every caller credential at the edge.
- **D:** Correct. Combining gateway `<validate-jwt>` pre-authentication with subscription scoping and client-certificate thumbprint checks blocks invalid traffic before hitting backends. In this scenario: Enforcing Product Subscription Keys + client certificate thumbprint checks alongside `<validate-jwt>` with `<openid-config>`, `<audiences>`, and `<required-claims>` inside `<inbound>` validates every caller credential at the edge.
- **E:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Enforcing Product Subscription Keys + client certificate thumbprint checks alongside `<validate-jwt>` with `<openid-config>`, `<audiences>`, and `<required-claims>` inside `<inbound>` validates every caller credential at the edge.

### Question 74 — B

Answer: Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`. `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` rejects invalid JWTs before backend forwarding. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. Local study-map skill 5.3 (Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` rejects invalid JWTs before backend forwarding.
- **B:** Correct. `<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge. In this scenario: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` rejects invalid JWTs before backend forwarding.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` rejects invalid JWTs before backend forwarding.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims>` rejects invalid JWTs before backend forwarding.

### Question 75 — A, E, F

Answers: Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`; Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`; Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`. `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` fulfill all three requirements. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` fulfill all three requirements.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` fulfill all three requirements.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` fulfill all three requirements.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` fulfill all three requirements.
- **E:** Correct. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` fulfill all three requirements.
- **F:** Correct. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. In this scenario: `<rate-limit-by-key>` + `<quota-by-key>` with `<base />`, `<cache-lookup vary-by-header="Accept-Language">` + `<cache-store duration="300">`, and `<retry>` in `<backend>` + `<set-header exists-action="delete">` in `<outbound>` fulfill all three requirements.

### Question 76 — C

Answer: Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`. Including `vary-by-header="Accept-Language"` on `<cache-lookup>` inside `<inbound>` paired with `<cache-store duration="300" />` inside `<outbound>` partitions cached responses per language header. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Including `vary-by-header="Accept-Language"` on `<cache-lookup>` inside `<inbound>` paired with `<cache-store duration="300" />` inside `<outbound>` partitions cached responses per language header.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Including `vary-by-header="Accept-Language"` on `<cache-lookup>` inside `<inbound>` paired with `<cache-store duration="300" />` inside `<outbound>` partitions cached responses per language header.
- **C:** Correct. APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy. In this scenario: Including `vary-by-header="Accept-Language"` on `<cache-lookup>` inside `<inbound>` paired with `<cache-store duration="300" />` inside `<outbound>` partitions cached responses per language header.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Including `vary-by-header="Accept-Language"` on `<cache-lookup>` inside `<inbound>` paired with `<cache-store duration="300" />` inside `<outbound>` partitions cached responses per language header.

### Question 77 — A

Answer: Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`. Wrapping `<forward-request />` in `<retry condition="@(context.Response.StatusCode >= 500)">` inside `<backend>` masks transient 5xx blips, while `<set-header exists-action="delete" />` in `<outbound>` strips fingerprinting headers. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`. In this scenario: Wrapping `<forward-request />` in `<retry condition="@(context.Response.StatusCode >= 500)">` inside `<backend>` masks transient 5xx blips, while `<set-header exists-action="delete" />` in `<outbound>` strips fingerprinting headers.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Wrapping `<forward-request />` in `<retry condition="@(context.Response.StatusCode >= 500)">` inside `<backend>` masks transient 5xx blips, while `<set-header exists-action="delete" />` in `<outbound>` strips fingerprinting headers.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Wrapping `<forward-request />` in `<retry condition="@(context.Response.StatusCode >= 500)">` inside `<backend>` masks transient 5xx blips, while `<set-header exists-action="delete" />` in `<outbound>` strips fingerprinting headers.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Wrapping `<forward-request />` in `<retry condition="@(context.Response.StatusCode >= 500)">` inside `<backend>` masks transient 5xx blips, while `<set-header exists-action="delete" />` in `<outbound>` strips fingerprinting headers.

### Question 78 — A, D

Answers: Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL; Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization. An Event Grid Domain manages hundreds of RBAC-isolated clinic topics under one endpoint, while `CloudEvents v1.0` subscriptions with subject filters and Blob dead-lettering guarantee filtered, resilient push delivery. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. In this scenario: An Event Grid Domain manages hundreds of RBAC-isolated clinic topics under one endpoint, while `CloudEvents v1.0` subscriptions with subject filters and Blob dead-lettering guarantee filtered, resilient push delivery.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: An Event Grid Domain manages hundreds of RBAC-isolated clinic topics under one endpoint, while `CloudEvents v1.0` subscriptions with subject filters and Blob dead-lettering guarantee filtered, resilient push delivery.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: An Event Grid Domain manages hundreds of RBAC-isolated clinic topics under one endpoint, while `CloudEvents v1.0` subscriptions with subject filters and Blob dead-lettering guarantee filtered, resilient push delivery.
- **D:** Correct. Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures. In this scenario: An Event Grid Domain manages hundreds of RBAC-isolated clinic topics under one endpoint, while `CloudEvents v1.0` subscriptions with subject filters and Blob dead-lettering guarantee filtered, resilient push delivery.
- **E:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: An Event Grid Domain manages hundreds of RBAC-isolated clinic topics under one endpoint, while `CloudEvents v1.0` subscriptions with subject filters and Blob dead-lettering guarantee filtered, resilient push delivery.

### Question 79 — D

Answer: Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`. Echoing `{"validationResponse": validationCode}` with HTTP 200 on `SubscriptionValidationEvent` (or returning `WebHook-Allowed-Origin` on CloudEvents HTTP `OPTIONS` preflight) completes validation. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Echoing `{"validationResponse": validationCode}` with HTTP 200 on `SubscriptionValidationEvent` (or returning `WebHook-Allowed-Origin` on CloudEvents HTTP `OPTIONS` preflight) completes validation.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Echoing `{"validationResponse": validationCode}` with HTTP 200 on `SubscriptionValidationEvent` (or returning `WebHook-Allowed-Origin` on CloudEvents HTTP `OPTIONS` preflight) completes validation.
- **C:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Echoing `{"validationResponse": validationCode}` with HTTP 200 on `SubscriptionValidationEvent` (or returning `WebHook-Allowed-Origin` on CloudEvents HTTP `OPTIONS` preflight) completes validation.
- **D:** Correct. Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET. In this scenario: Echoing `{"validationResponse": validationCode}` with HTTP 200 on `SubscriptionValidationEvent` (or returning `WebHook-Allowed-Origin` on CloudEvents HTTP `OPTIONS` preflight) completes validation.

### Question 80 — B

Answer: Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL. Configuring `subjectBeginsWith`, `subjectEndsWith` (e.g., `.dcm`), and `advancedFilters` on the Event Grid subscription filters events at the broker before invoking the webhook. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Configuring `subjectBeginsWith`, `subjectEndsWith` (e.g., `.dcm`), and `advancedFilters` on the Event Grid subscription filters events at the broker before invoking the webhook.
- **B:** Correct. Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container. In this scenario: Configuring `subjectBeginsWith`, `subjectEndsWith` (e.g., `.dcm`), and `advancedFilters` on the Event Grid subscription filters events at the broker before invoking the webhook.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Configuring `subjectBeginsWith`, `subjectEndsWith` (e.g., `.dcm`), and `advancedFilters` on the Event Grid subscription filters events at the broker before invoking the webhook.
- **D:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Configuring `subjectBeginsWith`, `subjectEndsWith` (e.g., `.dcm`), and `advancedFilters` on the Event Grid subscription filters events at the broker before invoking the webhook.

### Question 81 — C

Answer: Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization. An Azure Event Grid Domain hosts up to 100,000 domain topics behind a single ingestion endpoint with granular per-topic Azure RBAC authorization. Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures. Local study-map skill 5.5 (Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: An Azure Event Grid Domain hosts up to 100,000 domain topics behind a single ingestion endpoint with granular per-topic Azure RBAC authorization.
- **B:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: An Azure Event Grid Domain hosts up to 100,000 domain topics behind a single ingestion endpoint with granular per-topic Azure RBAC authorization.
- **C:** Correct. Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures. In this scenario: An Azure Event Grid Domain hosts up to 100,000 domain topics behind a single ingestion endpoint with granular per-topic Azure RBAC authorization.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: An Azure Event Grid Domain hosts up to 100,000 domain topics behind a single ingestion endpoint with granular per-topic Azure RBAC authorization.

### Question 82 — C

Answer: Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2. Streaming into Azure Event Hubs with a dedicated Consumer Group per AI pipeline and enabling Event Hubs Capture writes time/size-windowed Avro or Parquet files directly to ADLS Gen2. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Streaming into Azure Event Hubs with a dedicated Consumer Group per AI pipeline and enabling Event Hubs Capture writes time/size-windowed Avro or Parquet files directly to ADLS Gen2.
- **B:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Streaming into Azure Event Hubs with a dedicated Consumer Group per AI pipeline and enabling Event Hubs Capture writes time/size-windowed Avro or Parquet files directly to ADLS Gen2.
- **C:** Correct. Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code. In this scenario: Streaming into Azure Event Hubs with a dedicated Consumer Group per AI pipeline and enabling Event Hubs Capture writes time/size-windowed Avro or Parquet files directly to ADLS Gen2.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Streaming into Azure Event Hubs with a dedicated Consumer Group per AI pipeline and enabling Event Hubs Capture writes time/size-windowed Avro or Parquet files directly to ADLS Gen2.

### Question 83 — B

Answer: Host `EventProcessorClient` backed by `BlobContainerClient` and call `await eventArgs.UpdateCheckpointAsync()` after idempotent batch persistence so partition leases resume cleanly after rebalancing. Invoking `await eventArgs.UpdateCheckpointAsync()` persists the processed sequence/offset to the Blob checkpoint store so restarted pods resume cleanly. `EventProcessorClient` coordinates partition ownership via Azure Blob leases and records per-partition sequence/offset checkpoints in Blob metadata. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Invoking `await eventArgs.UpdateCheckpointAsync()` persists the processed sequence/offset to the Blob checkpoint store so restarted pods resume cleanly.
- **B:** Correct. `EventProcessorClient` coordinates partition ownership via Azure Blob leases and records per-partition sequence/offset checkpoints in Blob metadata. In this scenario: Invoking `await eventArgs.UpdateCheckpointAsync()` persists the processed sequence/offset to the Blob checkpoint store so restarted pods resume cleanly.
- **C:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Invoking `await eventArgs.UpdateCheckpointAsync()` persists the processed sequence/offset to the Blob checkpoint store so restarted pods resume cleanly.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Invoking `await eventArgs.UpdateCheckpointAsync()` persists the processed sequence/offset to the Blob checkpoint store so restarted pods resume cleanly.

### Question 84 — B, D

Answers: Use Azure Service Bus Topics with `SqlRuleFilter` / `CorrelationRuleFilter` (`CorrelationRuleFilter` preferred for high throughput) and `SqlRuleAction` header stamping, inspecting `$DeadLetterQueue` (`SubQueue.DeadLetter`) after `MaxDeliveryCount` expires; Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering. Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` provide fast header routing and poison isolation, while `RequiresDuplicateDetection = true` discards duplicate `MessageId` retries within the history window. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs. Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` provide fast header routing and poison isolation, while `RequiresDuplicateDetection = true` discards duplicate `MessageId` retries within the history window.
- **B:** Correct. Service Bus discards duplicate `MessageId` resends inside the history window and locks all messages sharing a `SessionId` to one active session receiver at a time. In this scenario: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` provide fast header routing and poison isolation, while `RequiresDuplicateDetection = true` discards duplicate `MessageId` retries within the history window.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` provide fast header routing and poison isolation, while `RequiresDuplicateDetection = true` discards duplicate `MessageId` retries within the history window.
- **D:** Correct. `CorrelationRuleFilter` matches brokered/application properties in-memory far faster than SQL evaluation, while `MaxDeliveryCount` isolates poison messages in the sub-queue DLQ. In this scenario: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` provide fast header routing and poison isolation, while `RequiresDuplicateDetection = true` discards duplicate `MessageId` retries within the history window.
- **E:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Service Bus Topics with `CorrelationRuleFilter` + `$DeadLetterQueue` provide fast header routing and poison isolation, while `RequiresDuplicateDetection = true` discards duplicate `MessageId` retries within the history window.

### Question 85 — B

Answer: Use `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false`, calling `CompleteMessageAsync` after commit, `AbandonMessageAsync` for transient retries, and `DeadLetterMessageAsync` on unrecoverable schema errors. `ReceiveAndDelete` permanently loses claims if the pod crashes mid-transaction; `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false` and explicit `CompleteMessageAsync` / `AbandonMessageAsync` / `DeadLetterMessageAsync` preserves durability. `ReceiveAndDelete` loses messages if a worker crashes mid-processing; `PeekLock` retains broker durability until explicit settlement or lock expiry. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `ReceiveAndDelete` permanently loses claims if the pod crashes mid-transaction; `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false` and explicit `CompleteMessageAsync` / `AbandonMessageAsync` / `DeadLetterMessageAsync` preserves durability.
- **B:** Correct. `ReceiveAndDelete` loses messages if a worker crashes mid-processing; `PeekLock` retains broker durability until explicit settlement or lock expiry. In this scenario: `ReceiveAndDelete` permanently loses claims if the pod crashes mid-transaction; `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false` and explicit `CompleteMessageAsync` / `AbandonMessageAsync` / `DeadLetterMessageAsync` preserves durability.
- **C:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: `ReceiveAndDelete` permanently loses claims if the pod crashes mid-transaction; `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false` and explicit `CompleteMessageAsync` / `AbandonMessageAsync` / `DeadLetterMessageAsync` preserves durability.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `ReceiveAndDelete` permanently loses claims if the pod crashes mid-transaction; `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false` and explicit `CompleteMessageAsync` / `AbandonMessageAsync` / `DeadLetterMessageAsync` preserves durability.

### Question 86 — D

Answer: Call `long seq = await sender.ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` and persist `seq` to call `CancelScheduledMessageAsync(seq)` if the user cancels early. `ScheduleMessageAsync` returns a broker `sequenceNumber` that `CancelScheduledMessageAsync(seq)` uses to delete the pending message before enqueue time. Service Bus native scheduled messages stay invisible until `ScheduledEnqueueTime` and can be canceled cleanly via their broker sequence number. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `ScheduleMessageAsync` returns a broker `sequenceNumber` that `CancelScheduledMessageAsync(seq)` uses to delete the pending message before enqueue time.
- **B:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: `ScheduleMessageAsync` returns a broker `sequenceNumber` that `CancelScheduledMessageAsync(seq)` uses to delete the pending message before enqueue time.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `ScheduleMessageAsync` returns a broker `sequenceNumber` that `CancelScheduledMessageAsync(seq)` uses to delete the pending message before enqueue time.
- **D:** Correct. Service Bus native scheduled messages stay invisible until `ScheduledEnqueueTime` and can be canceled cleanly via their broker sequence number. In this scenario: `ScheduleMessageAsync` returns a broker `sequenceNumber` that `CancelScheduledMessageAsync(seq)` uses to delete the pending message before enqueue time.

### Question 87 — A

Answer: Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics. Azure Queue Storage scales past Service Bus's 80 GB queue cap up to the storage account capacity limit (hundreds of TiB) for simple HTTP visibility-leased messages up to 64 KB. Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub. Local study-map skill 5.8 (Implement Queue Workflows with Azure Queue Storage SDK, Visibility Leases, PopReceipts, and Poison Handling), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Correct. Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub. In this scenario: Azure Queue Storage scales past Service Bus's 80 GB queue cap up to the storage account capacity limit (hundreds of TiB) for simple HTTP visibility-leased messages up to 64 KB.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Azure Queue Storage scales past Service Bus's 80 GB queue cap up to the storage account capacity limit (hundreds of TiB) for simple HTTP visibility-leased messages up to 64 KB.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: Azure Queue Storage scales past Service Bus's 80 GB queue cap up to the storage account capacity limit (hundreds of TiB) for simple HTTP visibility-leased messages up to 64 KB.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Azure Queue Storage scales past Service Bus's 80 GB queue cap up to the storage account capacity limit (hundreds of TiB) for simple HTTP visibility-leased messages up to 64 KB.

### Question 88 — C

Answer: Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`. Leasing messages via `ReceiveMessagesAsync`, inspecting `msg.DequeueCount` to move poison items to a quarantine queue, and passing `MessageId` + `PopReceipt` to `DeleteMessageAsync` stops infinite poison loops. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. Local study-map skill 5.8 (Implement Queue Workflows with Azure Queue Storage SDK, Visibility Leases, PopReceipts, and Poison Handling), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Leasing messages via `ReceiveMessagesAsync`, inspecting `msg.DequeueCount` to move poison items to a quarantine queue, and passing `MessageId` + `PopReceipt` to `DeleteMessageAsync` stops infinite poison loops.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Leasing messages via `ReceiveMessagesAsync`, inspecting `msg.DequeueCount` to move poison items to a quarantine queue, and passing `MessageId` + `PopReceipt` to `DeleteMessageAsync` stops infinite poison loops.
- **C:** Correct. `PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely. In this scenario: Leasing messages via `ReceiveMessagesAsync`, inspecting `msg.DequeueCount` to move poison items to a quarantine queue, and passing `MessageId` + `PopReceipt` to `DeleteMessageAsync` stops infinite poison loops.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Leasing messages via `ReceiveMessagesAsync`, inspecting `msg.DequeueCount` to move poison items to a quarantine queue, and passing `MessageId` + `PopReceipt` to `DeleteMessageAsync` stops infinite poison loops.

### Question 89 — C

Answer: Configure `ingress.external: false` inside a VNet-integrated Container Apps environment so the endpoint resolves only to internal environment/VNet callers. Setting `ingress.external: false` inside a VNet-integrated Container Apps environment restricts Envoy ingress routing strictly to internal environment and VNet callers. Setting `external: false` restricts the Container Appsenvoy ingress controller to private internal traffic. Local study-map skill 1.4 (Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/container-apps/overview

- **A:** Incorrect for this requirement. `Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing. Why the keyed choice wins: Setting `ingress.external: false` inside a VNet-integrated Container Apps environment restricts Envoy ingress routing strictly to internal environment and VNet callers.
- **B:** Incorrect for this requirement. Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits. Why the keyed choice wins: Setting `ingress.external: false` inside a VNet-integrated Container Apps environment restricts Envoy ingress routing strictly to internal environment and VNet callers.
- **C:** Correct. Setting `external: false` restricts the Container Appsenvoy ingress controller to private internal traffic. In this scenario: Setting `ingress.external: false` inside a VNet-integrated Container Apps environment restricts Envoy ingress routing strictly to internal environment and VNet callers.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Setting `ingress.external: false` inside a VNet-integrated Container Apps environment restricts Envoy ingress routing strictly to internal environment and VNet callers.

### Question 90 — A

Answer: Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage. Configuring a locked time-based Version-Level Immutability Policy (or `LegalHold`) enforces WORM non-modifiable, non-erasable storage until retention expires. Time-based locked retention and legal holds block modification and deletion even by Storage Account Owners until retention expires and holds clear. Local study-map skill 2.6 (Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Correct. Time-based locked retention and legal holds block modification and deletion even by Storage Account Owners until retention expires and holds clear. In this scenario: Configuring a locked time-based Version-Level Immutability Policy (or `LegalHold`) enforces WORM non-modifiable, non-erasable storage until retention expires.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Configuring a locked time-based Version-Level Immutability Policy (or `LegalHold`) enforces WORM non-modifiable, non-erasable storage until retention expires.
- **C:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Configuring a locked time-based Version-Level Immutability Policy (or `LegalHold`) enforces WORM non-modifiable, non-erasable storage until retention expires.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Configuring a locked time-based Version-Level Immutability Policy (or `LegalHold`) enforces WORM non-modifiable, non-erasable storage until retention expires.

### Question 91 — A

Answer: Mint a short-lived HTTPS-only (`SasProtocol.HttpsOnly`) User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` instead of Account or Service SAS signed with storage account keys. Minting an HTTPS-only User Delegation SAS via `GetUserDelegationKeyAsync` signs tokens with Microsoft Entra credentials instead of disabled storage account keys. User Delegation SAS eliminates shared storage account keys, enforces Entra RBAC, and automatically invalidates if the signing identity loses permissions. Local study-map skill 3.3 (Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. User Delegation SAS eliminates shared storage account keys, enforces Entra RBAC, and automatically invalidates if the signing identity loses permissions. In this scenario: Minting an HTTPS-only User Delegation SAS via `GetUserDelegationKeyAsync` signs tokens with Microsoft Entra credentials instead of disabled storage account keys.
- **B:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: Minting an HTTPS-only User Delegation SAS via `GetUserDelegationKeyAsync` signs tokens with Microsoft Entra credentials instead of disabled storage account keys.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Minting an HTTPS-only User Delegation SAS via `GetUserDelegationKeyAsync` signs tokens with Microsoft Entra credentials instead of disabled storage account keys.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Minting an HTTPS-only User Delegation SAS via `GetUserDelegationKeyAsync` signs tokens with Microsoft Entra credentials instead of disabled storage account keys.

### Question 92 — B

Answer: Call `await confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` inside the middle-tier API. `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the middle-tier user token for a delegated Graph token. OAuth 2.0 On-Behalf-Of (`AcquireTokenOnBehalfOf`) exchanges an incoming user access token for a downstream API token while preserving delegated user identity and consent. Local study-map skill 3.1 (Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Incorrect for this requirement. Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the middle-tier user token for a delegated Graph token.
- **B:** Correct. OAuth 2.0 On-Behalf-Of (`AcquireTokenOnBehalfOf`) exchanges an incoming user access token for a downstream API token while preserving delegated user identity and consent. In this scenario: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the middle-tier user token for a delegated Graph token.
- **C:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the middle-tier user token for a delegated Graph token.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` exchanges the middle-tier user token for a delegated Graph token.

### Question 93 — A

Answer: Enable Managed Identity with App Configuration Data Reader + Key Vault Secrets User → add Key Vault references and a sentinel key → wire AddAzureAppConfiguration with ConfigureKeyVault and ConfigureRefresh → invoke UseAzureAppConfiguration middleware. Assigning `App Configuration Data Reader` plus `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, configuring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware delivers atomic live refresh. RBAC on both stores is required because App Configuration stores only the URI pointer; `ConfigureRefresh` + middleware poll the sentinel key on incoming requests. Local study-map skill 3.5 (Manage Feature Flags, Labels, Sentinel Dynamic Refresh, and Key Vault References in Azure App Configuration), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. RBAC on both stores is required because App Configuration stores only the URI pointer; `ConfigureRefresh` + middleware poll the sentinel key on incoming requests. In this scenario: Assigning `App Configuration Data Reader` plus `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, configuring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware delivers atomic live refresh.
- **B:** Incorrect for this requirement. Committing exported secret values defeats Key Vault reference rotation and violates secret hygiene. Why the keyed choice wins: Assigning `App Configuration Data Reader` plus `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, configuring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware delivers atomic live refresh.
- **C:** Incorrect for this requirement. In ASP.NET Core, dynamic refresh is request-driven via `UseAzureAppConfiguration()` middleware (or manual `TryRefreshAsync`), not an automatic push without it. Why the keyed choice wins: Assigning `App Configuration Data Reader` plus `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, configuring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware delivers atomic live refresh.
- **D:** Incorrect for this requirement. Without Key Vault Secrets User on the vault itself, resolving a Key Vault reference throws 403 Forbidden at startup. Why the keyed choice wins: Assigning `App Configuration Data Reader` plus `Key Vault Secrets User` to Managed Identity, adding Key Vault references and a sentinel key, configuring `ConfigureKeyVault` + `ConfigureRefresh`, and invoking `UseAzureAppConfiguration` middleware delivers atomic live refresh.

### Question 94 — B

Answer: Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group. Configuring a multi-region Application Insights Standard Availability Test with SSL expiry checks and a `>= 2` failed-location alert rule wired to an Action Group prevents single-POP false alarms. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. Local study-map skill 4.2 (Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Configuring a multi-region Application Insights Standard Availability Test with SSL expiry checks and a `>= 2` failed-location alert rule wired to an Action Group prevents single-POP false alarms.
- **B:** Correct. Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips. In this scenario: Configuring a multi-region Application Insights Standard Availability Test with SSL expiry checks and a `>= 2` failed-location alert rule wired to an Action Group prevents single-POP false alarms.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Configuring a multi-region Application Insights Standard Availability Test with SSL expiry checks and a `>= 2` failed-location alert rule wired to an Action Group prevents single-POP false alarms.
- **D:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Configuring a multi-region Application Insights Standard Availability Test with SSL expiry checks and a `>= 2` failed-location alert rule wired to an Action Group prevents single-POP false alarms.

### Question 95 — B

Answer: Create the Event Hub, consumer group, and Blob checkpoint container → instantiate BlobContainerClient and EventProcessorClient → register ProcessEventAsync (calling UpdateCheckpointAsync) and ProcessErrorAsync → call StartProcessingAsync before StopProcessingAsync. Provisioning the Event Hub, dedicated consumer group, and Blob container first, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly. `EventProcessorClient` coordinates partition ownership and offset checkpoints in Blob Storage and requires both event and error handlers registered prior to `StartProcessingAsync`. Local study-map skill 5.6 (Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Sharing one consumer group and checkpoint prefix across distinct apps causes them to steal partitions from each other instead of each reading the full stream. Why the keyed choice wins: Provisioning the Event Hub, dedicated consumer group, and Blob container first, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly.
- **B:** Correct. `EventProcessorClient` coordinates partition ownership and offset checkpoints in Blob Storage and requires both event and error handlers registered prior to `StartProcessingAsync`. In this scenario: Provisioning the Event Hub, dedicated consumer group, and Blob container first, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly.
- **C:** Incorrect for this requirement. `EventProcessorClient` throws `InvalidOperationException` if started before registering both `ProcessEventAsync` and `ProcessErrorAsync`. Why the keyed choice wins: Provisioning the Event Hub, dedicated consumer group, and Blob container first, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly.
- **D:** Incorrect for this requirement. Producers publish events and never hold partition checkpoints; `EventProcessorClient` handles balanced consumer checkpointing. Why the keyed choice wins: Provisioning the Event Hub, dedicated consumer group, and Blob container first, instantiating `EventProcessorClient`, registering event (`UpdateCheckpointAsync`) and error handlers, and calling `StartProcessingAsync` coordinates partition leases cleanly.

### Question 96 — D

Answer: Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`. `[CosmosDBTrigger]` backed by a dedicated `leases` container listens to the Cosmos DB Change Feed and distributes partition work across Function instances automatically. `CosmosDBTrigger` wraps the Change Feed Processor library and requires a lease container connection to coordinate partition checkpoints across scaled workers. Local study-map skill 2.3 (Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-dotnet-v3

- **A:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `[CosmosDBTrigger]` backed by a dedicated `leases` container listens to the Cosmos DB Change Feed and distributes partition work across Function instances automatically.
- **B:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `[CosmosDBTrigger]` backed by a dedicated `leases` container listens to the Cosmos DB Change Feed and distributes partition work across Function instances automatically.
- **C:** Incorrect for this requirement. Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported. Why the keyed choice wins: `[CosmosDBTrigger]` backed by a dedicated `leases` container listens to the Cosmos DB Change Feed and distributes partition work across Function instances automatically.
- **D:** Correct. `CosmosDBTrigger` wraps the Change Feed Processor library and requires a lease container connection to coordinate partition checkpoints across scaled workers. In this scenario: `[CosmosDBTrigger]` backed by a dedicated `leases` container listens to the Cosmos DB Change Feed and distributes partition work across Function instances automatically.

### Question 97 — B

Answer: Run `AppRequests | where ResultCode == "500" | join kind=inner (AppDependencies | where Success == false) on OperationId | project TimeGenerated, Name, Target, DependencyType, ResultCode1`. Joining `AppRequests` (`ResultCode == "500"`) with `AppDependencies` (`Success == false`) on `OperationId` pinpoints the exact failing SQL, FHIR, or Storage call inside each distributed trace. Joining `AppRequests` and `AppDependencies` on `OperationId` isolates which exact downstream SQL, HTTP, or Storage dependency triggered HTTP 500 responses. Local study-map skill 4.1 (Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

- **A:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Joining `AppRequests` (`ResultCode == "500"`) with `AppDependencies` (`Success == false`) on `OperationId` pinpoints the exact failing SQL, FHIR, or Storage call inside each distributed trace.
- **B:** Correct. Joining `AppRequests` and `AppDependencies` on `OperationId` isolates which exact downstream SQL, HTTP, or Storage dependency triggered HTTP 500 responses. In this scenario: Joining `AppRequests` (`ResultCode == "500"`) with `AppDependencies` (`Success == false`) on `OperationId` pinpoints the exact failing SQL, FHIR, or Storage call inside each distributed trace.
- **C:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Joining `AppRequests` (`ResultCode == "500"`) with `AppDependencies` (`Success == false`) on `OperationId` pinpoints the exact failing SQL, FHIR, or Storage call inside each distributed trace.
- **D:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Joining `AppRequests` (`ResultCode == "500"`) with `AppDependencies` (`Success == false`) on `OperationId` pinpoints the exact failing SQL, FHIR, or Storage call inside each distributed trace.

### Question 98 — D

Answer: Create the queue or subscription with RequiresSession = true at creation time → send ServiceBusMessage instances setting a non-empty SessionId → create a ServiceBusSessionProcessor (or AcceptNextSessionAsync receiver) → process messages in order and complete/renew session locks. Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = rxNumber` on outbound messages, and consuming via `ServiceBusSessionProcessor` locks per-prescription FIFO order to one worker at a time. `RequiresSession` can only be enabled when creating the entity, producers must populate `SessionId`, and consumers must use session-aware receivers/processors. Local study-map skill 5.7 (Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. `RequiresSession` is immutable after creation, messages without `SessionId` are rejected on session queues, and non-session receivers fail. Why the keyed choice wins: Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = rxNumber` on outbound messages, and consuming via `ServiceBusSessionProcessor` locks per-prescription FIFO order to one worker at a time.
- **B:** Incorrect for this requirement. Entity creation precedes processor connection, and session queues reject messages lacking a `SessionId`. Why the keyed choice wins: Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = rxNumber` on outbound messages, and consuming via `ServiceBusSessionProcessor` locks per-prescription FIFO order to one worker at a time.
- **C:** Incorrect for this requirement. Azure Queue Storage does not support brokered `SessionId` FIFO locks; Azure Service Bus session entities are required. Why the keyed choice wins: Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = rxNumber` on outbound messages, and consuming via `ServiceBusSessionProcessor` locks per-prescription FIFO order to one worker at a time.
- **D:** Correct. `RequiresSession` can only be enabled when creating the entity, producers must populate `SessionId`, and consumers must use session-aware receivers/processors. In this scenario: Creating the queue with `RequiresSession = true` at creation time, setting `SessionId = rxNumber` on outbound messages, and consuming via `ServiceBusSessionProcessor` locks per-prescription FIFO order to one worker at a time.

### Question 99 — A

Answer: Instantiate `new CryptographyClient(keyVaultKey.Id, new DefaultAzureCredential())` and invoke `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync(...)`. `CryptographyClient` invoking `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` performs envelope key wrapping without transmitting multi-gigabyte audit payloads over Key Vault REST calls. Envelope encryption keeps bulk data encryption keys (`DEK`) wrapped by hardware/software-protected Key Vault KEKs without sending large payloads through Key Vault. Local study-map skill 3.6 (Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview

- **A:** Correct. Envelope encryption keeps bulk data encryption keys (`DEK`) wrapped by hardware/software-protected Key Vault KEKs without sending large payloads through Key Vault. In this scenario: `CryptographyClient` invoking `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` performs envelope key wrapping without transmitting multi-gigabyte audit payloads over Key Vault REST calls.
- **B:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: `CryptographyClient` invoking `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` performs envelope key wrapping without transmitting multi-gigabyte audit payloads over Key Vault REST calls.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: `CryptographyClient` invoking `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` performs envelope key wrapping without transmitting multi-gigabyte audit payloads over Key Vault REST calls.
- **D:** Incorrect for this requirement. ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation. Why the keyed choice wins: `CryptographyClient` invoking `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` performs envelope key wrapping without transmitting multi-gigabyte audit payloads over Key Vault REST calls.

### Question 100 — B

Answer: Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`. Placing `<rate-limit-by-key>` and `<quota-by-key>` inside `<inbound>` while retaining `<base />` enforces both burst `429` and monthly `403` limits without bypassing inherited security policies. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! Local study-map skill 5.4 (Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes), aligned to the official AZ-204 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204 Primary Microsoft Learn reference: https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts

- **A:** Incorrect for this requirement. Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale. Why the keyed choice wins: Placing `<rate-limit-by-key>` and `<quota-by-key>` inside `<inbound>` while retaining `<base />` enforces both burst `429` and monthly `403` limits without bypassing inherited security policies.
- **B:** Correct. Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies! In this scenario: Placing `<rate-limit-by-key>` and `<quota-by-key>` inside `<inbound>` while retaining `<base />` enforces both burst `429` and monthly `403` limits without bypassing inherited security policies.
- **C:** Incorrect for this requirement. `PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`. Why the keyed choice wins: Placing `<rate-limit-by-key>` and `<quota-by-key>` inside `<inbound>` while retaining `<base />` enforces both burst `429` and monthly `403` limits without bypassing inherited security policies.
- **D:** Incorrect for this requirement. `Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours). Why the keyed choice wins: Placing `<rate-limit-by-key>` and `<quota-by-key>` inside `<inbound>` while retaining `<base />` enforces both burst `429` and monthly `403` limits without bypassing inherited security policies.
