# Microsoft Exam AZ-204 — Curriculum Outline & 37-Skill Blueprint Map

> **Lifecycle Disclosure:** Exam AZ-204 (`Microsoft Certified: Azure Developer Associate`) retired on **July 31, 2026** and was succeeded by **Exam AI-200 (`Azure AI Cloud Developer Associate`)**. All six mock exams align strictly to the final official **January 14, 2026** AZ-204 Study Guide (`700 / 1000` scaled passing score; 100-minute exam window). Pre-2026 retired topics (VMs/ARM VM provisioning, Logic Apps, Notification Hubs, Azure CDN, and Azure Cache for Redis) are intentionally excluded.

---

## Course Structure: 6 Full-Length Mock Exams (`600` Questions)

| Practice Test | Theme & Industry Context | Enterprise Case Studies (`4 × 3 = 12` Qs) | Items | Recommended Time |
|---|---|---|---:|---:|
| **Practice Set 1** | Omnichannel Retail, Flash-Sale Checkout, and Loyalty APIs | `Vespera Retail`, `Kova Footwear`, `BriskCart Loyalty`, `Cinder Coffee Roasters` | 100 | 100 min |
| **Practice Set 2** | Healthcare Patient Portals, Clinical Lab Telemetry, and Claims EDI | `Aurelia Health`, `Trellis Diagnostics`, `Vireo Specialty Pharmacy`, `Solace Telemed` | 100 | 100 min |
| **Practice Set 3** | FinTech Instant Payments, Ledger Reconciliation, and Fraud Webhooks | `Crestline Clearing`, `Halcyon Custody`, `Pillar Remit`, `Bramble Insure` | 100 | 100 min |
| **Practice Set 4** | Connected Fleet IoT, Cold-Chain Logistics, and Port Customs | `Strider ColdChain`, `Mariner PortOps`, `Zephyr Parcel`, `Aegis Rail` | 100 | 100 min |
| **Practice Set 5** | Multi-Tenant B2B SaaS, DevTools Telemetry, and Document Workflows | `QuillSign SaaS`, `Pulsar Metrics`, `Loomis Cloud ERP`, `Cobalt FieldService` | 100 | 100 min |
| **Practice Set 6** | Digital Media Streaming, Live Ticketing, Gaming Backends, and Smart Energy | `Lyric Arena Ticketing`, `NovaGrid Energy`, `EmberPlay Studios`, `Prism Newsroom` | 100 | 100 min |

---

## 37-Skill Local Study Map (`SKILL_PLAN` Per 100-Item Set)

### Domain 1: Develop Azure compute solutions (`25–30%` -> `28` items/set, `168` total)
- **`1.1` (2/set):** Multi-stage Dockerfiles, `.dockerignore`, non-root `.NET 8` port `8080`, exec-form `ENTRYPOINT`
- **`1.2` (2/set):** Azure Container Registry (`az acr build` Tasks, `az acr import`, `Premium` geo-replication, `acr purge`, `AcrPull` Managed Identity)
- **`1.3` (2/set):** Azure Container Instances (`OnFailure`/`Never` vs `Always` restart policies, multi-container sidecar groups, secure env vars & volumes)
- **`1.4` (4/set):** Azure Container Apps (multiple-revision weighted ingress, internal-only VNet environments, KEDA scale-to-zero with Managed Identity, Jobs, Dapr `scopes`, Key Vault secret refs)
- **`1.5` (2/set):** App Service Plans (`Standard S1+` / `Premium v3` vs `Free`/`Shared`/`Basic` feature gates, container port routing)
- **`1.6` (2/set):** App Service Diagnostics (Blob application/web server logging retention vs 12-hour filesystem shutoff, `az webapp log tail`)
- **`1.7` (2/set):** App Service Deployment (`WEBSITE_RUN_FROM_PACKAGE=1` atomic ZIP mount, ACR Managed Identity container pulls)
- **`1.8` (2/set):** App Service Security & Config (`httpsOnly`, `minTlsVersion`, `clientCertEnabled` mTLS, credentialed `CORS`, `--slot-settings` SQL connection strings)
- **`1.9` (2/set):** App Service Autoscale & Readiness (hysteresis scale-out/scale-in rules, `coolDown` windows, `applicationInitialization` warm-up paths)
- **`1.10` (2/set):** App Service Deployment Slots (`slotSetting: true` sticky settings, staging validation, zero-downtime swaps, `autoSwapSlotName`)
- **`1.11` (2/set):** Azure Functions Hosting & `host.json` (`Flex Consumption` & `Elastic Premium` vs classic 10-min Consumption limit, VNet outbound, sampling exclusions)
- **`1.12` (2/set):** Azure Functions Bindings (.NET isolated-worker multi-output POCOs, `[CosmosDBTrigger]` leases, `[ExponentialBackoffRetry]`, `AuthorizationLevel`)
- **`1.13` (2/set):** Azure Functions Triggers (6-field `NCRONTAB` `[TimerTrigger]`, `BlobTriggerSource.EventGrid` push triggers)

### Domain 2: Develop for Azure storage (`15–20%` -> `18` items/set, `108` total)
- **`2.1` (4/set):** Cosmos DB SDK v3 (singleton `CosmosClient`, hierarchical partition keys, `TransactionalBatch`, `IfMatchEtag`, `PatchItemAsync`, `FeedIterator`, composite & excluded indexing)
- **`2.2` (2/set):** Cosmos DB Consistency (`Session` + `SessionToken` read-your-writes vs `BoundedStaleness` `K`/`T` lag bounds vs `Strong`)
- **`2.3` (3/set):** Cosmos DB Change Feed & TTL (`GetChangeFeedProcessorBuilder`, `/id` lease containers, distinct `processorName` cursors, `AllVersionsAndDeletes`, `DefaultTimeToLive = -1`)
- **`2.4` (3/set):** Blob Properties, Metadata & Tags (`SetHttpHeadersAsync` vs C#-identifier `SetMetadataAsync`, searchable `FindBlobsByTagsAsync`, Snapshots & Versioning)
- **`2.5` (3/set):** Blob Leases, Copy & SAS (`BlobLeaseClient` 15–60s locks + `BlobRequestConditions`, `StartCopyFromUriAsync`, single-blob `BlobSasBuilder`)
- **`2.6` (3/set):** Blob Tiers, Lifecycle & WORM (Lifecycle Management JSON rules, `Archive` 409 offline behavior, `RehydratePriority.High`, locked WORM Immutability & `LegalHold`)

### Domain 3: Implement Azure security (`15–20%` -> `19` items/set, `114` total)
- **`3.1` (3/set):** MSAL Authentication (`PublicClientApplication` PKCE + `AcquireTokenSilent` cache fallback, `ConfidentialClientApplication` certificate `/.default`, `AcquireTokenOnBehalfOf`)
- **`3.2` (3/set):** Entra ID Authorization (`appRoles` for Users & Applications, `AzureADMultipleOrgs` `/organizations` + `tid` validation, Easy Auth `401` vs `302`)
- **`3.3` (3/set):** Shared Access Signatures (User Delegation SAS via `GetUserDelegationKeyAsync` with Shared Key disabled, `StoredAccessPolicy` instant revocation)
- **`3.4` (3/set):** Microsoft Graph SDK v5 (least-privilege scopes, `$select` & `$filter`, `PageIterator<T>`, `BatchRequestContentCollection` `/$batch` + `429 Retry-After`)
- **`3.5` (2/set):** Azure App Configuration (`.appconfig.featureflag/*`, `Sentinel` key atomic refresh, `ConfigureKeyVault` secret URI resolution, `UseAzureAppConfiguration`)
- **`3.6` (3/set):** Azure Key Vault (`SecretClient` / `KeyClient` / `CryptographyClient` `WrapKeyAsync` / `CertificateClient`, Soft Delete + Purge Protection, `@Microsoft.KeyVault(...)` app references)
- **`3.7` (2/set):** Managed Identities (`DefaultAzureCredential` dev-to-cloud chain, `ManagedIdentityClientId` disambiguation, System-Assigned vs User-Assigned lifecycle)

### Domain 4: Monitor, troubleshoot, and optimize Azure solutions (`5–10%` -> `10` items/set, `60` total)
- **`4.1` (4/set):** Application Insights Diagnostics (W3C `OperationId` correlation, KQL `join` across `AppRequests`/`AppDependencies`, `percentile` + `bin()`, `Flush()` on short-lived jobs, `ActivitySource` spans)
- **`4.2` (3/set):** Availability & Alerting (Standard multi-region SSL/HTTP tests, `>=2` location alerts, private-VNet `TrackAvailability()`, Dynamic Threshold metric alerts & Action Groups)
- **`4.3` (3/set):** OpenTelemetry & Sampling (`Azure.Monitor.OpenTelemetry.AspNetCore` `UseAzureMonitor()`, `APPLICATIONINSIGHTS_CONNECTION_STRING`, Ingestion vs Adaptive Sampling, unsampled Live Metrics)

### Domain 5: Connect to and consume Azure services and third-party services (`20–25%` -> `25` items/set, `150` total)
- **`5.1` (2/set):** APIM Architecture (`Developer`/`Premium` tiers, Self-Hosted Gateway containerized local routing, `<authentication-managed-identity>`)
- **`5.2` (3/set):** APIM APIs (`Revisions` vs `Versions`, `<mock-response>`, `<rewrite-uri>` + `<set-backend-service>`, Function App import `AuthorizationLevel`)
- **`5.3` (3/set):** APIM Edge Security (Product Subscription Keys, mTLS `Certificate.Thumbprint`, `<validate-jwt>` OIDC/audience/role enforcement, Managed Identity backend auth)
- **`5.4` (4/set):** APIM Policy Execution (`<rate-limit-by-key>` `429` vs `<quota-by-key>` `403`, `<base />` inheritance, `<cache-lookup>` + `<cache-store>`, `<retry>` in `<backend>` + outbound header scrubbing)
- **`5.5` (4/set):** Azure Event Grid (`CloudEvents v1.0`, subject & advanced filters, 24h retry + Blob dead-lettering, Event Grid Domains multi-tenant RBAC, `SubscriptionValidationEvent` handshake)
- **`5.6` (3/set):** Azure Event Hubs (partitioned high-throughput streams vs Event Grid, dedicated Consumer Groups, `EventProcessorClient` + `UpdateCheckpointAsync`, Event Hubs Capture to ADLS Gen2)
- **`5.7` (4/set):** Azure Service Bus (Topics + `CorrelationRuleFilter`/`SqlRuleFilter` + `SqlRuleAction`, `$DeadLetterQueue`, `PeekLock` settlement, `RequiresSession` FIFO, `RequiresDuplicateDetection`, `ScheduleMessageAsync`)
- **`5.8` (2/set):** Azure Queue Storage (>80 GB to 500 TiB capacity selection vs Service Bus, `ReceiveMessagesAsync` vs `PeekMessagesAsync`, `PopReceipt` lease updates/deletes, `DequeueCount` poison handling)
