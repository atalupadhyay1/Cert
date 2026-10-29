"""Technical option catalog for Exam AZ-204: Developing Solutions for Microsoft Azure.

Every option pairs a concrete Azure SDK call, CLI command, XML/JSON policy element,
or developer configuration choice with a concise technical explanation of what it
actually does — ensuring distractors represent real Azure capabilities applied to a
different requirement. `SEQUENCES` is merged at the bottom for `O` ordering items.
"""
from sequences import SEQUENCES

TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term key: {key}')
    if '→' in label:
        raise ValueError(f'Arrow reserved for SEQUENCES: {key}')
    TERMS[key] = (label, meaning)


# --- Domain 1: Develop Azure compute solutions (25-30%) ---
# 1.1 Container images & Dockerfiles
t('cmp_docker_multistage',
  'Use a multi-stage Dockerfile building in `mcr.microsoft.com/dotnet/sdk:8.0` and copying published output into `mcr.microsoft.com/dotnet/aspnet:8.0` with a non-root `USER app`',
  'Multi-stage Docker builds exclude compiler SDK layers and source files from the final runtime image, shrinking image size and attack surface.')
t('cmp_docker_single_sdk_root',
  'Ship a single-stage Dockerfile based on the full `dotnet/sdk:8.0` image running as `root` with source code and NuGet caches retained',
  'Shipping the full SDK image as root inflates pull size by hundreds of megabytes and leaves build tools exposed at runtime.')
t('cmp_docker_entrypoint_exec',
  'Declare `ENTRYPOINT ["dotnet", "Api.dll"]` in exec JSON-array form so `SIGTERM` reaches the .NET host cleanly during container shutdown',
  'Exec-form `ENTRYPOINT` runs the process as PID 1 without an intermediate `/bin/sh -c` wrapper that swallows POSIX termination signals.')
t('cmp_docker_dockerignore',
  'Add `bin/`, `obj/`, `.git/`, and local `.env` files to `.dockerignore` before running `docker build` or `az acr build`',
  '`.dockerignore` prevents streaming gigabytes of local build artifacts and stray secrets into the build context.')

# 1.2 Azure Container Registry (ACR)
t('cmp_acr_build_task',
  'Run `az acr build --registry <acrName> --image app:{{.Run.ID}} .` to build and push the container image remotely using ACR Tasks without a local Docker daemon',
  'ACR Tasks tar and upload the build context to Azure, executing the Dockerfile build and pushing tagged layers directly inside ACR.')
t('cmp_acr_pull_mi',
  'Disable the ACR admin account and assign the built-in `AcrPull` role on the registry to the compute resource managed identity',
  '`AcrPull` with Managed Identity eliminates shared registry passwords while granting least-privilege read-only image pulls.')
t('cmp_acr_georep_premium',
  'Upgrade Azure Container Registry to the `Premium` SKU and configure geo-replication into each target compute region',
  'ACR geo-replication requires the `Premium` tier and serves local regional layer pulls through a single registry login server FQDN.')
t('cmp_acr_purge_task',
  'Schedule an ACR Task executing `acr purge --filter "app:.*" --ago 30d --untagged` to clean stale untagged manifests and old tags automatically',
  'Scheduled `acr purge` tasks reclaim registry storage quota without manual tag deletion scripts.')
t('cmp_acr_admin_shared',
  'Enable `--admin-enabled true` on a Basic ACR and embed the single shared admin password in every developer and production YAML file',
  'ACR admin credentials share one registry-wide read/write identity with no per-service auditability or automatic rotation.')

# 1.3 Azure Container Instances (ACI)
t('cmp_aci_restart_onfailure',
  'Set `--restart-policy OnFailure` (or `Never`) on the Azure Container Instances container group so batch containers stop billing vCPU/memory seconds once exit code 0 completes',
  'ACI bills per second while containers run; `OnFailure` retries crashes (`exit != 0`) and halts cleanly on `exit == 0`, whereas `Always` loops forever.')
t('cmp_aci_restart_always',
  'Keep the default `--restart-policy Always` on a run-once batch container group',
  '`Always` restarts exited batch containers endlessly even after exit code 0, causing infinite execution loops and continuous compute billing.')
t('cmp_aci_sidecar_group',
  'Deploy the application container and Envoy/logging sidecar inside one multi-container ACI group sharing `localhost` network namespace and an `emptyDir` / Azure Files volume',
  'Containers in the same ACI container group share one IP/port namespace (`127.0.0.1`) and can mount shared Azure Files or `emptyDir` volumes on Linux.')
t('cmp_aci_secret_volume_env',
  'Pass sensitive tokens via `--secure-environment-variables` (or a secret volume mount) so values never appear in Azure Portal properties or `az container show` plaintext output',
  'Secure environment variables and secret volumes redact secret values from ARM/CLI read responses.')

# 1.4 Azure Container Apps (ACA)
t('cmp_aca_multi_rev_traffic',
  'Set `--revision-mode multiple` and apply `az containerapp ingress traffic set --revision-weight` to split live HTTP requests across named revisions',
  'Multiple-revision mode keeps more than one revision active simultaneously for weighted blue/green or canary traffic splitting.')
t('cmp_aca_single_rev_only',
  'Leave `--revision-mode single` enabled while attempting to route 20% of HTTP traffic to a second active revision',
  'Single-revision mode automatically deactivates the prior revision once a new revision activates, preventing weighted multi-revision splits.')
t('cmp_aca_keda_sb_mi',
  'Configure a custom KEDA `azure-servicebus` scale rule with `minReplicas: 0` and Managed Identity (`identity` property) so replicas scale to zero when idle and wake on queue depth',
  'Container Apps uses KEDA scalers to scale down to zero on consumption/workload profiles and authenticate scalers cleanly via Managed Identity.')
t('cmp_aca_jobs_event_scheduled',
  'Deploy an Azure Container Apps Job (`triggerType: Event` or `Schedule`) with `replicaCompletionCount` and `parallelism` instead of an always-listening HTTP container app',
  'Container Apps Jobs execute finite scheduled or event-driven workloads to completion without exposing unused HTTP ingress.')
t('cmp_aca_dapr_scopes',
  'Register a Dapr state or pub/sub component in the Container Apps environment and restrict access via the component `scopes` array to specific `daprAppId` values',
  'Dapr `scopes` confine which microservices inside a shared Container Apps environment can load or invoke a component.')
t('cmp_aca_kv_secret_ref',
  'Define a Container App secret using `keyVaultUrl` plus `identity` (managed identity resource ID or `system`) and map container environment variables via `secretRef`',
  'Key Vault secret references in Container Apps resolve secrets via Managed Identity without storing secret strings in ARM templates.')
t('cmp_aca_internal_ingress',
  'Configure `ingress.external: false` inside a VNet-integrated Container Apps environment so the endpoint resolves only to internal environment/VNet callers',
  'Setting `external: false` restricts the Container Appsenvoy ingress controller to private internal traffic.')

# 1.5 - 1.10 Azure App Service Web Apps
t('cmp_app_plan_standard_prod',
  'Provision at least a `Standard` (`S1+`) or `Premium v3` (`P1v3+`) App Service plan to unlock deployment slots, custom domain SNI SSL, and metric/schedule autoscaling',
  '`Free`, `Shared`, and `Basic` plans omit deployment slots (`S1` gives 5, `P1v3` gives 20) and rule-based autoscale (`S1+` required).')
t('cmp_app_plan_free_basic',
  'Use the `Free (F1)` or `Basic (B1)` App Service plan to configure staging deployment slots and CPU metric autoscaling rules',
  'Neither `F1` nor `B1` supports deployment slots, auto-swap, or rule-based horizontal autoscale.')
t('cmp_app_logs_blob_retention',
  'Enable Application Logging (Blob) and Web Server Logging to Azure Blob Storage rather than ephemeral local filesystem storage so logs persist beyond 12 hours and across scale-out instances',
  'Filesystem application diagnostics turn off automatically after 12 hours; Blob Storage diagnostics retain logs durably per retention policy.')
t('cmp_app_zipdeploy_runfrompkg',
  'Set `WEBSITE_RUN_FROM_PACKAGE=1` and deploy with `az webapp deploy --type zip` so the app mounts the read-only ZIP package directly with atomic cold-start replacement',
  'Running directly from a mounted ZIP eliminates file-lock copy conflicts during `wwwroot` sync and speeds cold starts.')
t('cmp_app_tls12_https_only',
  'Enable `httpsOnly: true`, set `minTlsVersion: "1.2"` (or `"1.3"`), and configure `clientCertEnabled` when mutual TLS client certificates are required',
  'Enforcing HTTPS redirection and minimum TLS 1.2/1.3 at the App Service front end rejects plaintext HTTP and legacy ciphers before app code runs.')
t('cmp_app_cors_allowed_origins',
  'Configure App Service `CORS` with explicit origin URLs (and `supportCredentials` only without wildcard `*`) so App Service handles preflight `OPTIONS` requests',
  'Platform-level App Service CORS intercepts `OPTIONS` preflight checks; credentialed CORS forbids wildcard `*` origins.')
t('cmp_app_autoscale_cooldown',
  'Pair every scale-out metric rule (e.g., CPU > 75% for 10 min) with a conservative scale-in rule (e.g., CPU < 35%) and an explicit `coolDown` window plus safe default/max instance bounds',
  'Asymmetric thresholds and cool-down periods prevent rapid flapping (thrashing) where instances repeatedly add and terminate.')
t('cmp_app_slot_sticky_setting',
  'Mark environment-specific settings such as `PaymentWebhookUrl` and production connection strings as `slotSetting: true` (Deployment slot setting) before swapping slots',
  'Slot-sticky settings stay pinned to their slot (`Production` vs `Staging`) across swaps instead of traveling with the swapped code.')
t('cmp_app_slot_autoswap_warmup',
  'Configure `applicationInitialization` custom warm-up paths plus `WEBSITE_SWAP_WARMUP_PING_PATH` and `WEBSITE_SWAP_WARMUP_PING_STATUSES` so App Service warms caches before completing slot swaps',
  'Custom warm-up ping paths verify HTTP readiness on the target worker instances before routing live production requests.')

# 1.11 - 1.13 Azure Functions
t('cmp_func_flex_premium_plan',
  'Host the Function App on `Flex Consumption` or `Elastic Premium (EP1+)` when VNet integration, longer execution timeouts beyond 10 minutes, or pre-warmed/always-ready instances are required',
  'Classic Consumption caps timeout at 10 minutes (`functionTimeout`) and cold-starts from zero; `Flex Consumption` and `Premium` add VNet outbound and pre-warmed readiness.')
t('cmp_func_classic_consumption_limit',
  'Keep the Function App on classic Linux Consumption while setting `functionTimeout` to `"02:00:00"` inside `host.json`',
  'Classic Consumption enforces a hard 10-minute maximum timeout regardless of larger values placed in `host.json`.')
t('cmp_func_isolated_multi_out',
  'In the .NET isolated worker model, return a custom POCO class uniting `[HttpResult]` (or `HttpResponseData`) with `[CosmosDBOutput]` / `[ServiceBusOutput]` properties',
  'Isolated-worker C# functions cannot use `out` parameters for bindings; multi-output types return structured properties on a single return object.')
t('cmp_func_ncrontab_6field',
  'Specify a six-field NCRONTAB expression `{second} {minute} {hour} {day} {month} {day-of-week}` such as `"0 */15 9-17 * * 1-5"` on `[TimerTrigger]`',
  'Azure Functions `[TimerTrigger]` uses 6-field NCRONTAB (leading seconds field), unlike 5-field Unix cron.')
t('cmp_func_blob_eventgrid_source',
  'Configure `[BlobTrigger(..., Source = BlobTriggerSource.EventGrid)]` with an Event Grid system topic subscription instead of default container-log polling',
  'Event Grid-sourced blob triggers eliminate storage-log scan latency and work reliably on Blob-only / high-scale storage accounts.')
t('cmp_func_webhook_authlevel',
  'Set `AuthorizationLevel.Function` (requiring `x-functions-key` or `?code=`) or front `AuthorizationLevel.Anonymous` with Entra Easy Auth / APIM validation',
  '`AuthorizationLevel.Function` requires a function or host key, `Admin` requires `_master`, and `Anonymous` shifts auth responsibility to platform/gateway layers.')

# --- Domain 2: Develop for Azure storage (15-20%) ---
# 2.1 - 2.3 Azure Cosmos DB
t('stg_cosmos_singleton_pk',
  'Register `CosmosClient` as a process-wide singleton in dependency injection and choose a high-cardinality `PartitionKey` path (or up to 3-level `Hierarchical` subpartition paths) that distributes RU/s evenly',
  'Reusing one thread-safe `CosmosClient` avoids socket exhaustion, and hierarchical/high-cardinality partition keys prevent hot partitions and 20 GB single-partition caps.')
t('stg_cosmos_transactional_batch',
  'Use `container.CreateTransactionalBatch(new PartitionKey(pkValue))` to group multiple create/replace/upsert/delete operations atomically within the same logical partition',
  '`TransactionalBatch` guarantees ACID all-or-nothing execution serialized in one network round-trip, strictly scoped to a single logical partition key.')
t('stg_cosmos_cross_pk_tx_myth',
  'Call `CreateTransactionalBatch` spanning five different logical partition keys in one atomic distributed ACID transaction',
  'Cosmos DB `TransactionalBatch` and stored procedures are strictly bounded to a single logical partition key; cross-partition ACID transactions are not supported.')
t('stg_cosmos_etag_ifmatch',
  'Pass `new ItemRequestOptions { IfMatchEtag = item.ETag }` on `ReplaceItemAsync` and catch `CosmosException` when `StatusCode == HttpStatusCode.PreconditionFailed` (412)',
  'Supplying `IfMatchEtag` enforces optimistic concurrency control so concurrent writers fail with HTTP 412 rather than silently overwriting updates.')
t('stg_cosmos_ttl_container_item',
  'Enable container `DefaultTimeToLive = -1` (or positive seconds) and set item `ttl = 600` so Cosmos DB purges expired items automatically using background RU capacity',
  'Container TTL must be non-null (`-1` or `>0`) for per-item `ttl` seconds to take effect; setting `DefaultTimeToLive = null` ignores item-level `ttl`.')
t('stg_cosmos_composite_index',
  'Add a `compositeIndexes` array matching the exact property sequence and sort directions (`ascending` / `descending`) in the container indexing policy JSON',
  'Cosmos DB for NoSQL requires a matching composite index whenever a SQL query specifies `ORDER BY` across two or more properties.')
t('stg_cosmos_consistency_session',
  'Use `Session` consistency (the default) and propagate `x-ms-session-token` (`RequestOptions.SessionToken`) across client/middle-tier hops to guarantee monotonic read-your-own-writes at half the read RU cost of `Strong`',
  '`Session` consistency guarantees read-your-writes, monotonic reads, and write-follows-reads within a session token at 50% of `Strong` / `BoundedStaleness` read RUs.')
t('stg_cosmos_consistency_bounded',
  'Configure `BoundedStaleness` consistency with explicit lag bounds (`K` item versions and `T` seconds) when multi-region reads require global total order within a bounded window without single-region `Strong` write latency',
  '`Strong` consistency cannot be enabled on multi-write or unaligned multi-region setups the same way `BoundedStaleness` bounds staleness by `K` operations / `T` seconds.')
t('stg_cosmos_cfp_lease_groups',
  'Give each independent downstream consumer microservice its own unique `processorName` on `GetChangeFeedProcessorBuilder<T>` sharing (or separating) the `/id`-partitioned lease container, and enable `StartFromBeginning()` for historical replay',
  'In Change Feed Processor, `processorName` acts like an Event Hubs consumer group: distinct names receive independent copies of every insert/update, while identical names load-balance partitions.')
t('stg_cosmos_cf_delete_allversions',
  'Use Change Feed `AllVersionsAndDeletes` mode (or soft-delete flag items with short TTL in `LatestVersion` mode) because default `LatestVersion` change feed omits hard-deleted items',
  'Standard `LatestVersion` change feed emits only inserts and updates of current items; hard deletes require `AllVersionsAndDeletes` or soft-delete Tombstone items + TTL.')

# 2.4 - 2.6 Azure Blob Storage
t('stg_blob_props_metadata_headers',
  'Read properties/metadata with `BlobClient.GetPropertiesAsync()`, set HTTP system headers via `SetHttpHeadersAsync(BlobHttpHeaders)`, and write C#-identifier-valid key-value pairs via `SetMetadataAsync(IDictionary<string,string>)` (`x-ms-meta-*`)',
  'Blob user metadata keys are sent as `x-ms-meta-<name>` HTTP headers and must obey valid C# identifier naming rules; `SetMetadataAsync` replaces the metadata dictionary.')
t('stg_blob_index_tags_query',
  'Attach searchable key-value `Tags` (`SetTagsAsync` / `BlobUploadOptions.Tags`) and query across containers with `FindBlobsByTagsAsync("@container = \'docs\' AND status = \'pending\'")`',
  'Blob Index Tags are indexed natively by Azure Storage for server-side filtering, whereas `Metadata` is not searchable without listing every blob.')
t('stg_blob_lease_60s_lock',
  'Use `BlobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(60))` (15–60 seconds or `-1` infinite) and pass `LeaseId` inside `BlobRequestConditions` on subsequent writes/deletes',
  'Blob leases grant exclusive write/delete locks (`15` to `60` seconds or infinite `-1`) so competing workers immediately receive `412 LeaseIdMissing/Mismatch`.')
t('stg_blob_async_copy_server',
  'Invoke `BlobClient.StartCopyFromUriAsync(sourceSasUri)` to trigger asynchronous server-side blob copy and inspect `CopyStatus` without streaming bytes through the client VM',
  '`StartCopyFromUriAsync` instructs Azure Storage fabric to copy blobs asynchronously server-to-server using a readable source URI/SAS.')
t('stg_blob_lifecycle_json',
  'Create a Blob Storage Lifecycle Management policy JSON filtering `blockBlob` by `prefixMatch` / `blobIndexMatch` with `tierToCool`, `tierToCold`, `tierToArchive`, and `delete` (`daysAfterModificationGreaterThan` or `daysAfterLastAccessTimeGreaterThan`)',
  'Lifecycle management policies automate tier transitions and retention deletion server-side once per day without custom cron jobs.')
t('stg_blob_immutable_worm',
  'Configure Version-Level Immutability Policies with time-based retention (`Unlocked` -> `Locked`) or a `LegalHold` tag to enforce SEC 17a-4 / WORM non-erasable, non-modifiable storage',
  'Time-based locked retention and legal holds block modification and deletion even by Storage Account Owners until retention expires and holds clear.')
t('stg_blob_archive_direct_fail',
  'Read `Archive`-tier blobs directly via `DownloadStreamingAsync()` in synchronous user requests because Archive tier has the lowest per-GB storage price',
  '`Archive` is an offline tier; direct reads fail with `409 BlobArchived` until asynchronous rehydration to `Hot` or `Cool` completes (1–15 hours).')

# --- Domain 3: Implement Azure security (15-20%) ---
# 3.1 - 3.4 AuthN, AuthZ, SAS, Microsoft Graph
t('sec_msal_public_pkce',
  'Use `PublicClientApplicationBuilder.Create(clientId)` with Authorization Code flow + PKCE (`AcquireTokenInteractive` first, `AcquireTokenSilent` from token cache before every call) for SPA, mobile, or desktop apps',
  'Public clients cannot protect secrets; Authorization Code + PKCE plus silent cache lookup followed by `MsalUiRequiredException` fallback is the MSAL standard.')
t('sec_msal_confidential_daemon',
  'Use `ConfidentialClientApplicationBuilder` authenticated with a client certificate (or workload identity assertion) calling `AcquireTokenForClient(new[] { "api://.../.default" })` for headless background daemons',
  'Daemon apps without a signed-in user use OAuth 2.0 Client Credentials flow and must request the `.default` scope for pre-consented application permissions.')
t('sec_entra_approles_manifest',
  'Declare `appRoles` with `allowedMemberTypes: ["User", "Application"]` in the Entra app registration manifest and validate the `roles` claim (`[Authorize(Roles = "...")]`) in the web API',
  'Entra ID emits assigned app roles inside the `roles` JWT claim for both human users and service principals without requiring directory-level Entra admin roles.')
t('sec_entra_multitenant_issuer',
  'Set `signInAudience` to `AzureADMultipleOrgs`, authenticate against `/organizations`, and validate allowed `tid` (tenant ID) / issuer claims explicitly in API token validation',
  'Multi-tenant Entra apps accept tokens from external work/school tenants and must enforce tenant allowlists or subscription checks on `tid`/`iss`.')
t('sec_easyauth_401_api',
  'Enable App Service / Functions built-in Authentication (`Easy Auth`) with Microsoft Entra provider and set unauthenticated action to `Return HTTP 401 Unauthorized` for API endpoints (rather than `302 Redirect`)',
  'REST/XHR API clients break on HTML `302` login redirects; returning `401` instructs programmatic clients to attach a valid `Authorization: Bearer` header.')
t('sec_sas_user_delegation',
  'Mint a short-lived HTTPS-only (`SasProtocol.HttpsOnly`) User Delegation SAS signed by Microsoft Entra ID via `GetUserDelegationKeyAsync` instead of Account or Service SAS signed with storage account keys',
  'User Delegation SAS eliminates shared storage account keys, enforces Entra RBAC, and automatically invalidates if the signing identity loses permissions.')
t('sec_sas_stored_policy_revoke',
  'Bind a Service SAS to a container/queue/table Stored Access Policy (`SignedIdentifier`, omitting inline start/expiry/permissions) so compromised tokens can be revoked instantly by modifying or deleting the policy',
  'Up to 5 Stored Access Policies per container allow instant SAS revocation without rotating storage account keys; Note that User Delegation SAS uses key revocation instead of Stored Access Policies.')
t('sec_graph_sdk_least_priv',
  'Instantiate `GraphServiceClient` with `TokenCredential` (`OnBehalfOfCredential` or `ClientSecretCredential`), request minimal scopes like `User.Read` / `Calendars.Read` (`$select` specific fields), and iterate pages using `PageIterator<T>`',
  'Microsoft Graph enforces least-privilege consent scopes, trims payload size with `$select`, and paginates `@odata.nextLink` cleanly through `PageIterator<T>`.')
t('sec_graph_batch_throttling',
  'Combine up to 20 independent Microsoft Graph requests inside a `BatchRequestContentCollection` (`/$batch`) and honor `Retry-After` headers on HTTP `429` throttling responses',
  'Graph JSON batching (`/$batch`) bundles up to 20 sub-requests per round-trip, while built-in SDK retry middleware respects `Retry-After`.')

# 3.5 - 3.7 App Configuration, Key Vault, Managed Identity
t('sec_appcfg_feature_sentinel',
  'Store environment-labeled settings and `.appconfig.featureflag/*` entries in Azure App Configuration, register `AddAzureAppConfiguration` + `AddFeatureManagement`, and watch a single `Sentinel` key with `refreshAll: true`',
  'Updating one sentinel key after finishing multi-key edits prevents apps from reading half-updated configuration state mid-rollout.')
t('sec_kv_secret_key_cert_clients',
  'Use `SecretClient` (`Azure.Security.KeyVault.Secrets`) for connection strings/tokens, `KeyClient` / `CryptographyClient` (`Azure.Security.KeyVault.Keys`) for RSA/EC wrap-unwrap-sign, and `CertificateClient` for X.509 lifecycle',
  'Azure Key Vault SDK v4 splits secrets, cryptographic keys, and X.509 certificates into dedicated clients and RBAC data-plane roles (`Key Vault Secrets User`, `Crypto User`, `Certificates User`).')
t('sec_kv_softdelete_purge',
  'Enable Soft Delete (mandatory on new vaults, 7–90 days) plus Purge Protection on Azure Key Vault so neither accidental deletion nor malicious principals can permanently destroy keys before retention expires',
  'Soft Delete allows recovery via `StartRecoverDeletedSecretAsync`, while Purge Protection blocks permanent `PurgeDeletedSecretAsync` calls during retention.')
t('sec_kv_webapp_reference',
  'Configure App Service / Functions application settings using `@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/<name>)` (omitting secret version) paired with `Key Vault Secrets User` on the app Managed Identity',
  'Versionless Key Vault references automatically pull rotated secret versions within 24 hours (or immediately on config change / manual sync) with zero SDK boilerplate.')
t('sec_mi_defaultazurecred',
  'Instantiate `new DefaultAzureCredential()` (or explicit `ManagedIdentityCredential(clientId)` for user-assigned identities in production) so identical code authenticates via Azure CLI / Visual Studio locally and Managed Identity in Azure',
  '`DefaultAzureCredential` chains developer workstation credentials locally and IMDS Managed Identity in Azure; passing `managedIdentityClientId` is required when selecting a specific user-assigned identity.')
t('sec_mi_system_vs_user',
  'Choose a User-Assigned Managed Identity when multiple compute resources must share one pre-provisioned identity lifecycle independent of individual app deletions; choose System-Assigned when 1-to-1 fate-sharing tied to a single resource is required',
  'System-assigned identities are deleted automatically with their parent resource; user-assigned identities have an independent ARM lifecycle and reusable RBAC grants.')

# --- Domain 4: Monitor, troubleshoot, and optimize Azure solutions (5-10%) ---
t('mon_appi_kql_correlate',
  'Query Workspace-based Application Insights (`AppRequests`, `AppDependencies`, `AppExceptions`, `AppTraces` or classic `requests`/`dependencies`/`exceptions`) joining on `OperationId` (`operation_Id`) to reconstruct end-to-end distributed transactions',
  'W3C Trace-Context propagates `traceparent` into `operation_Id` across services so KQL joins pinpoint exact failing downstream dependencies.')
t('mon_appi_sampling_adaptive',
  'Enable Adaptive Sampling on server SDKs (excluding critical `Event` / `Availability` types if needed) or Ingestion Sampling when multiple services must sample identical `operation_Id` traces consistently',
  'Ingestion sampling hashes `operation_Id` at the endpoint to preserve intact multi-service call graphs when per-host adaptive sampling would discard partial spans; Live Metrics remains 100% unsampled.')
t('mon_appi_otel_distro',
  'Add `Azure.Monitor.OpenTelemetry.AspNetCore` calling `builder.Services.AddOpenTelemetry().UseAzureMonitor()` with `APPLICATIONINSIGHTS_CONNECTION_STRING` and custom `ActivitySource` / `Meter` instruments',
  'Microsoft recommends the Azure Monitor OpenTelemetry Distro for modern .NET/Java/Node/Python apps rather than deprecated Classic InstrumentationKey setups.')
t('mon_appi_avail_standard_track',
  'Configure Application Insights Standard multi-region Availability Tests (checking SSL certificate expiry + HTTP status) or custom Functions calling `TelemetryClient.TrackAvailability()` for private VNet endpoints, wired to a >=2-location alert rule and Action Group',
  'Multi-location synthetic probes alert only when >=N regions fail simultaneously, avoiding false-positive pages from transient single-POP network blips.')
t('mon_appi_alert_dynamic_ag',
  'Create an Azure Monitor Metric Alert (Dynamic Thresholds or static p95 latency/5xx count) or Scheduled Query (KQL) Alert targeting an Action Group configured with webhook / Azure Function / email-SMS receivers',
  'Metric alerts offer sub-minute stateful evaluation on numeric signals, whereas Scheduled Query Rules run expressive KQL joins on log tables at configured intervals.')

# --- Domain 5: Connect to and consume Azure services and third-party services (20-25%) ---
# 5.1 - 5.4 Azure API Management (APIM)
t('int_apim_tiers_selfhosted',
  'Select `Developer` (non-SLA) or `Premium` / `Standard v2` for VNet integration, and deploy the containerized APIM Self-Hosted Gateway (`mcr.microsoft.com/azure-api-management/gateway`) for hybrid on-premises/multi-cloud local traffic routing',
  'Self-hosted gateways require `Developer` or `Premium` tier and keep data-plane traffic local while pulling policy updates outbound over HTTPS/443 from Azure.')
t('int_apim_revisions_vs_versions',
  'Use APIM `Revisions` to stage, test, and swap non-breaking internal changes safely on the same consumer URL (`;rev=2`), and use APIM `Versions` (path/header/query) when publishing breaking contract changes side-by-side for distinct consumer cohorts',
  'Revisions let authors edit and flip the `current` implementation transparently; Versions expose distinct URLs/headers so legacy clients keep working.')
t('int_apim_subkey_jwt_cert',
  'Require Product/API Subscription Keys (`Ocp-Apim-Subscription-Key`), validate Microsoft Entra bearer tokens in `<inbound>` via `<validate-jwt>`, and verify `context.Request.Certificate.Thumbprint` for mutual TLS callers',
  'Combining gateway `<validate-jwt>` pre-authentication with subscription scoping and client-certificate thumbprint checks blocks invalid traffic before hitting backends.')
t('int_apim_ratelimit_vs_quota',
  'Place `<rate-limit-by-key calls="60" renewal-period="60" counter-key="@(context.Subscription?.Id)" />` (HTTP `429`) and `<quota-by-key calls="5000" renewal-period="2592000" ... />` (HTTP `403`) inside `<inbound>` alongside `<base />`',
  'Rate-limit protects burst concurrency (`429 Too Many Requests` + `Retry-After`), Quota enforces long-window monetization caps (`403 Forbidden`), and omitting `<base />` silently drops parent-scope policies!')
t('int_apim_cache_lookup_store',
  'Pair `<cache-lookup vary-by-developer="false" vary-by-header="Accept-Language" />` in `<inbound>` with `<cache-store duration="300" />` in `<outbound>`',
  'APIM response caching requires both an inbound lookup policy (keyed on relevant headers/query params) and a matching outbound store policy.')
t('int_apim_outbound_scrub_retry',
  'Use `<retry condition="@(context.Response.StatusCode >= 500)" count="3" interval="2">` inside `<backend>` and `<set-header name="X-AspNet-Version" exists-action="delete" />` inside `<outbound>`',
  'Transient backend retries wrap `<forward-request />` in `<backend>`, while response-header scrubbing belongs in `<outbound>`.')

# 5.5 - 5.6 Event Grid & Event Hubs
t('int_eg_cloudevents_filters',
  'Publish discrete state-change events in `CloudEvents v1.0` (or `EventGridEvent`) schema (<=1 MB/event), filter subscriptions by `subjectBeginsWith`, `subjectEndsWith`, and `advancedFilters`, and configure Blob dead-lettering plus retry TTL',
  'Event Grid push-routes discrete reactive events with exponential-backoff retries up to 24 hours / 30 attempts before writing undelivered events to a dead-letter Blob container.')
t('int_eg_domains_multitenant',
  'Provision an Azure Event Grid Domain to manage thousands of tenant-isolated domain topics under a single publish endpoint with per-topic Azure RBAC authorization',
  'Event Grid Domains avoid provisioning thousands of standalone custom topics in multi-tenant B2B notification architectures.')
t('int_eh_partitions_cg_capture',
  'Stream high-throughput telemetry into Azure Event Hubs using partition keys (or round-robin for maximum throughput), create a dedicated Consumer Group per downstream application, and enable Event Hubs Capture to write Avro/Parquet batches to Blob/ADLS Gen2',
  'Event Hubs retains ordered replayable partition logs for millions of events/sec; separate consumer groups isolate each reader cursor, and Capture archives cold streams with zero code.')
t('int_eh_vs_eg_confusion',
  'Send 50,000 raw IoT telemetry points per second through Azure Event Grid custom webhooks expecting ordered partition replay and consumer-group offset cursors',
  'Event Grid is a push pub/sub router for discrete state changes, not a partitioned pull-stream log with replayable consumer offsets like Event Hubs.')

# 5.7 - 5.8 Service Bus & Queue Storage
t('int_sb_topics_sqlfilter_dlq',
  'Use Azure Service Bus Topics with `SqlRuleFilter` / `CorrelationRuleFilter` (`CorrelationRuleFilter` preferred for high throughput) and `SqlRuleAction` header stamping, inspecting `$DeadLetterQueue` (`SubQueue.DeadLetter`) after `MaxDeliveryCount` expires',
  '`CorrelationRuleFilter` matches brokered/application properties in-memory far faster than SQL evaluation, while `MaxDeliveryCount` isolates poison messages in the sub-queue DLQ.')
t('int_sb_dupdetect_sessions',
  'Enable `RequiresDuplicateDetection = true` with `DuplicateDetectionHistoryTimeWindow` (keyed on `MessageId`) for idempotent ingestion and `RequiresSession = true` (keyed on `SessionId`) for strict per-entity FIFO ordering',
  'Service Bus discards duplicate `MessageId` resends inside the history window and locks all messages sharing a `SessionId` to one active session receiver at a time.')
t('int_sb_vs_queuestorage',
  'Choose Azure Queue Storage when simple HTTP/REST-accessible queues exceeding 80 GB total backlog (up to 500 TiB storage account capacity, 64 KB messages, 7-day+ TTL) are needed without FIFO sessions, transactions, or pub/sub topics',
  'Queue Storage scales cheaply to hundreds of terabytes with visibility-timeout leases (`ReceiveMessagesAsync` + `DeleteMessageAsync(messageId, popReceipt)`), whereas Service Bus provides enterprise FIFO, transactions, and pub/sub.')
t('int_qs_receive_popreceipt',
  'Call `QueueClient.ReceiveMessagesAsync(visibilityTimeout)` to hide leased messages temporarily, check `DequeueCount` to quarantine poison messages, and pass both `MessageId` and current `PopReceipt` to `UpdateMessageAsync` or `DeleteMessageAsync`',
  '`PeekMessagesAsync` neither hides messages nor returns a `PopReceipt`, so peeked messages cannot be deleted; `ReceiveMessagesAsync` leases them safely.')
t('int_qs_peek_delete_bug',
  'Call `QueueClient.PeekMessagesAsync()` and pass the peeked message directly to `DeleteMessageAsync()` expecting exclusive lock removal',
  '`PeekMessagesAsync` leaves messages visible to every worker and omits `PopReceipt`, making deletion impossible without `ReceiveMessagesAsync`.')

# --- Code, CLI, APIM XML, Cosmos JSON, and KQL Completion Options ---
t('code_d1_acr_import',
  'Execute `az acr import --name <acrName> --source docker.io/library/nginx:1.27-alpine --image base/nginx:1.27-alpine`',
  '`az acr import` copies public or cross-registry container images server-side into ACR without requiring `docker pull` / `docker push` on a local workstation.')
t('code_d1_aca_env_create',
  'Execute `az containerapp env create --name <envName> --resource-group <rg> --infrastructure-subnet-resource-id <subnetId> --internal-only`',
  'Provisioning a VNet-injected `--internal-only` Container Apps environment isolates the Envoy ingress load balancer to private RFC1918 addresses.')
t('code_d1_webapp_config_conn',
  'Execute `az webapp config connection-string set --name <app> --resource-group <rg> --connection-string-type SQLAzure --slot-settings LedgerDb="<value>"`',
  '`--slot-settings` pins the connection string (`SQLCONNSTR_LedgerDb`) to the target slot so slot swaps never leak staging databases into production.')
t('code_d1_webapp_log_tail',
  'Execute `az webapp log config --application-logging filesystem --level verbose` followed by `az webapp log tail --name <app> --resource-group <rg>`',
  '`az webapp log tail` attaches a live console stream to Kudu `/api/logstream` for real-time developer troubleshooting.')
t('code_d1_func_host_timeout',
  'Configure `"functionTimeout": "00:10:00"` and `"logging": { "applicationInsights": { "samplingSettings": { "isEnabled": true, "excludedTypes": "Request;Exception" } } }` inside `host.json`',
  '`host.json` governs global Function host behaviors such as execution timeout and Application Insights telemetry sampling exclusions across all functions in the app.')
t('code_d1_func_cosmos_trigger',
  'Decorate the method with `[CosmosDBTrigger(databaseName: "core", containerName: "orders", Connection = "CosmosConn", LeaseContainerName = "leases", CreateLeaseContainerIfNotExists = true)]`',
  '`CosmosDBTrigger` wraps the Change Feed Processor library and requires a lease container connection to coordinate partition checkpoints across scaled workers.')
t('code_d1_func_retry_attr',
  'Apply `[ExponentialBackoffRetry(5, "00:00:04", "00:01:00")]` (or `[FixedDelayRetry]`) on the `[EventHubTrigger]` / `[TimerTrigger]` function',
  'Function-level retry attributes replay failed executions in-memory before advancing trigger checkpoints on Event Hubs and Timer triggers.')
t('code_d1_docker_expose_env',
  'Set `ENV ASPNETCORE_HTTP_PORTS=8080` and `EXPOSE 8080` inside the final `.NET 8` runtime stage and match `targetPort: 8080` on Container Apps ingress',
  'Starting in .NET 8, official Microsoft container images default to non-root port `8080` rather than privileged port `80`.')

t('code_d2_cosmos_feediterator',
  'Use `FeedIterator<Order> iter = container.GetItemQueryIterator<Order>(queryDef, requestOptions: new QueryRequestOptions { PartitionKey = new PartitionKey(pk), MaxItemCount = 100 })` and loop `while (iter.HasMoreResults) { FeedResponse<Order> page = await iter.ReadNextAsync(); }`',
  '`GetItemQueryIterator<T>` streams paginated results via continuation tokens and inspects `page.RequestCharge` without buffering an entire partition in memory.')
t('code_d2_cosmos_patch_op',
  'Call `await container.PatchItemAsync<Order>(id, new PartitionKey(pk), new[] { PatchOperation.Increment("/retryCount", 1), PatchOperation.Set("/lastStatus", "Queued") })`',
  'Partial Document Update (`PatchItemAsync`) mutates specific JSON paths server-side without reading, deserializing, and replacing the full document payload.')
t('code_d2_cosmos_hierarchical_pk',
  'Define `new ContainerProperties(id: "telemetry", partitionKeyPaths: new List<string> { "/tenantId", "/siteId", "/deviceId" })` using `PartitionKeyBuilder` on reads and writes',
  'Hierarchical partition keys (up to 3 levels) overcome the 20 GB logical-partition limit on large tenants while preserving efficient prefix queries on `/tenantId` alone.')
t('code_d2_cosmos_indexing_exclude',
  'Configure `"indexingMode": "consistent"` with `"includedPaths": [{"path": "/customerId/?"}, {"path": "/createdUtc/?"}]` and `"excludedPaths": [{"path": "/*"}]`',
  'Excluding wildcard `/*` and indexing only queried filter paths dramatically cuts write Request Unit (RU) cost and index storage on write-heavy containers.')
t('code_d2_blob_rehydrate_high',
  'Call `await blobClient.SetAccessTierAsync(AccessTier.Hot, rehydratePriority: RehydratePriority.High)` (or `StartCopyFromUriAsync` to a new `Hot` blob)',
  '`SetAccessTierAsync` (or copy-to-Hot) initiates Archive rehydration; `RehydratePriority.High` prioritizes restoration (often under 1 hour for <10 GB blobs).')
t('code_d2_blob_sas_builder',
  'Configure `new BlobSasBuilder { BlobContainerName = "exports", BlobName = "manifest.csv", Resource = "b", ExpiresOn = DateTimeOffset.UtcNow.AddMinutes(15), Protocol = SasProtocol.HttpsOnly }` with `SetPermissions(BlobSasPermissions.Read)`',
  'Scoping `Resource = "b"`, HTTPS-only, minimal `Read` permission, and a tight expiry window upholds least privilege for single-blob SAS grants.')
t('code_d2_blob_version_snapshot',
  'Call `await blobClient.CreateSnapshotAsync()` for explicit point-in-time read-only checkpoints or enable account-level Blob Versioning so every `UploadAsync` overwrite retains an immutable `VersionId`',
  'Snapshots capture explicit developer-triggered checkpoints, whereas Blob Versioning automatically preserves prior state on every overwrite or delete.')

t('code_d3_msal_obo_flow',
  'Call `await confidentialClient.AcquireTokenOnBehalfOf(downstreamScopes, new UserAssertion(incomingBearerToken)).ExecuteAsync()` inside the middle-tier API',
  'OAuth 2.0 On-Behalf-Of (`AcquireTokenOnBehalfOf`) exchanges an incoming user access token for a downstream API token while preserving delegated user identity and consent.')
t('code_d3_msal_silent_fallback',
  'Invoke `await pca.AcquireTokenSilent(scopes, accounts.FirstOrDefault()).ExecuteAsync()` first and call `AcquireTokenInteractive(scopes)` only inside `catch (MsalUiRequiredException)`',
  'MSAL refreshes cached tokens transparently during `AcquireTokenSilent`; prompting interactively on every call degrades UX and hits rate limits.')
t('code_d3_graph_select_filter',
  'Call `await graphClient.Users.GetAsync(rc => { rc.QueryParameters.Select = new[] { "id", "displayName", "mail" }; rc.QueryParameters.Filter = "accountEnabled eq true"; })`',
  'In Microsoft Graph .NET SDK v5, `$select` and `$filter` query parameters reduce payload size and network transfer on collection endpoints.')
t('code_d3_kv_crypto_wrap',
  'Instantiate `new CryptographyClient(keyVaultKey.Id, new DefaultAzureCredential())` and invoke `WrapKeyAsync(KeyWrapAlgorithm.RsaOaep256, dekBytes)` / `UnwrapKeyAsync(...)`',
  'Envelope encryption keeps bulk data encryption keys (`DEK`) wrapped by hardware/software-protected Key Vault KEKs without sending large payloads through Key Vault.')
t('code_d3_appcfg_kv_ref',
  'Wire `options.Connect(new Uri(endpoint), cred).ConfigureKeyVault(kv => kv.SetCredential(cred))` so App Configuration resolves Key Vault reference items using the app identity',
  'App Configuration stores only the Key Vault secret URI metadata; client code still requires `ConfigureKeyVault` credentials with `Key Vault Secrets User` rights on the target vault.')
t('code_d3_mi_client_id_opt',
  'Instantiate `new DefaultAzureCredential(new DefaultAzureCredentialOptions { ManagedIdentityClientId = userAssignedClientId })` (or set `AZURE_CLIENT_ID`)',
  'When a host has multiple user-assigned managed identities attached, IMDS rejects ambiguous token requests unless the target `clientId` (or resource ID) is specified.')

t('code_d4_kql_p95_bin',
  'Run `AppRequests | where TimeGenerated > ago(1h) | summarize Failures = countif(Success == false), P95Ms = percentile(DurationMs, 95) by Name, bin(TimeGenerated, 5m)`',
  'KQL `countif` and `percentile(..., 95)` grouped by `bin(TimeGenerated, 5m)` quantify error spikes and tail latency per operation over fixed time buckets.')
t('code_d4_kql_dep_join',
  'Run `AppRequests | where ResultCode == "500" | join kind=inner (AppDependencies | where Success == false) on OperationId | project TimeGenerated, Name, Target, DependencyType, ResultCode1`',
  'Joining `AppRequests` and `AppDependencies` on `OperationId` isolates which exact downstream SQL, HTTP, or Storage dependency triggered HTTP 500 responses.')
t('code_d4_otel_custom_span',
  'Create a static `ActivitySource("OrderPipeline")` registered via `.WithTracing(b => b.AddSource("OrderPipeline"))` and wrap custom work in `using var span = Source.StartActivity("ValidateFraud")`',
  '`System.Diagnostics.ActivitySource` is the native .NET OpenTelemetry API exported as `AppDependencies` spans by the Azure Monitor OpenTelemetry Distro.')
t('code_d4_appi_flush_worker',
  'Invoke `telemetryClient.Flush()` (or dispose the `TracerProvider` / `MeterProvider`) and wait briefly (`await Task.Delay(5000)`) before a console job or short-lived container exits',
  'Telemetry channels batch items asynchronously in memory; exiting `Main` immediately without flushing drops final buffered spans and metrics.')

t('code_d5_apim_validate_jwt',
  'Place `<validate-jwt header-name="Authorization" failed-validation-httpcode="401">` with `<openid-config>`, `<audiences>`, and `<required-claims><claim name="roles">...</claim></required-claims>` inside `<inbound>`',
  '`<validate-jwt>` verifies token signature via OIDC JWKS metadata, audience (`aud`), expiration (`exp`), and required `roles`/`scp` claims at the APIM edge.')
t('code_d5_apim_mi_backend',
  'Place `<authentication-managed-identity resource="api://backend-app" output-token-variable-name="msi-token" />` and `<set-header name="Authorization" exists-action="override">` injecting `Bearer @(context.Variables["msi-token"])` in `<inbound>`',
  'APIM uses its own system- or user-assigned Managed Identity to acquire Entra bearer tokens cached automatically for protected backend services.')
t('code_d5_apim_mock_rewrite',
  'Use `<mock-response status-code="200" content-type="application/json" />` during frontend parallel development, or `<rewrite-uri template="/internal/v2/orders/{orderId}" />` with `<set-backend-service base-url="..." />` in `<inbound>`',
  '`<mock-response>` short-circuits backend forwarding using OpenAPI example payloads, while `<rewrite-uri>` maps public clean paths onto legacy internal routes.')
t('code_d5_eg_validation_code',
  'Detect `Microsoft.EventGrid.SubscriptionValidationEvent` (or respond to the CloudEvents HTTP `OPTIONS` `WebHook-Request-Origin` preflight with `WebHook-Allowed-Origin`) and return HTTP 200 containing `{"validationResponse": validationCode}`',
  'Event Grid refuses to deliver events to custom HTTPS webhooks until endpoint ownership is proven via synchronous validation code echo or async `validationUrl` GET.')
t('code_d5_eh_processor_ckpt',
  'Host `EventProcessorClient` backed by `BlobContainerClient` and call `await eventArgs.UpdateCheckpointAsync()` after idempotent batch persistence so partition leases resume cleanly after rebalancing',
  '`EventProcessorClient` coordinates partition ownership via Azure Blob leases and records per-partition sequence/offset checkpoints in Blob metadata.')
t('code_d5_sb_peeklock_abandon',
  'Use `ServiceBusProcessor` in `ServiceBusReceiveMode.PeekLock` with `AutoCompleteMessages = false`, calling `CompleteMessageAsync` after commit, `AbandonMessageAsync` for transient retries, and `DeadLetterMessageAsync` on unrecoverable schema errors',
  '`ReceiveAndDelete` loses messages if a worker crashes mid-processing; `PeekLock` retains broker durability until explicit settlement or lock expiry.')
t('code_d5_sb_scheduled_msg',
  'Call `long seq = await sender.ScheduleMessageAsync(message, DateTimeOffset.UtcNow.AddMinutes(30))` and persist `seq` to call `CancelScheduledMessageAsync(seq)` if the user cancels early',
  'Service Bus native scheduled messages stay invisible until `ScheduledEnqueueTime` and can be canceled cleanly via their broker sequence number.')

# Merge ordering sequences for O items
for _k, _v in SEQUENCES.items():
    if _k in TERMS:
        raise ValueError(f'Sequence collides with term key: {_k}')
    TERMS[_k] = _v
