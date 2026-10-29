"""Candidate four-step orderings for AZ-204 sequencing (`DRAG DROP` sequence) items.

Every key maps to `(label, meaning)` and uses `→` between steps so `validate.py`
and `test_course.py` enforce all-four-option arrow formatting automatically.
"""
SEQUENCES = {}


def s(key, label, meaning):
    if key in SEQUENCES:
        raise ValueError(f'Duplicate sequence key: {key}')
    if '→' not in label:
        raise ValueError(f'Sequence label requires arrow: {key}')
    SEQUENCES[key] = (label, meaning)


# 1. User Delegation SAS generation (Azure.Storage.Blobs + Azure.Identity)
s('seq_ud_sas_ok',
  'Assign Storage Blob Data Contributor/Delegator RBAC to the identity → instantiate BlobServiceClient with DefaultAzureCredential → call GetUserDelegationKeyAsync for a bounded validity window → build BlobSasBuilder and sign with the user delegation key',
  'Entra RBAC must authorize delegation before BlobServiceClient requests a user delegation key, which then signs the BlobSasBuilder token without account keys.')
s('seq_ud_sas_b1',
  'Build BlobSasBuilder and sign → call GetUserDelegationKeyAsync → instantiate BlobServiceClient with shared account key → assign RBAC to the identity',
  'A SAS cannot be signed before obtaining the user delegation key, and shared account keys cannot mint Entra user delegation SAS tokens.')
s('seq_ud_sas_b2',
  'Call GetUserDelegationKeyAsync anonymously → build BlobSasBuilder → assign RBAC to the identity → instantiate BlobServiceClient',
  'GetUserDelegationKeyAsync requires an authenticated Entra client with RBAC already granted before the call executes.')
s('seq_ud_sas_b3',
  'Instantiate BlobServiceClient with SAS token → assign RBAC → build BlobSasBuilder → call GetUserDelegationKeyAsync',
  'The client must authenticate with Microsoft Entra credentials first so it can request the delegation key that mints the SAS.')

# 2. ACR image build + managed-identity pull into Azure Container Apps
s('seq_aca_acr_ok',
  'Build and push the image to ACR with az acr build → create a user-assigned managed identity and grant AcrPull on the registry → create the Container Apps environment → create the container app referencing the identity and registry server',
  'The image and AcrPull identity grant must exist before Container Apps pulls the image from ACR without admin credentials.')
s('seq_aca_acr_b1',
  'Create the container app referencing the registry → build and push the image with az acr build → create the Container Apps environment → grant AcrPull',
  'A container app cannot be created before its environment exists or pull an image before AcrPull and the image tag exist.')
s('seq_aca_acr_b2',
  'Grant AcrPull on the registry → create the container app → create the user-assigned identity → run az acr build',
  'Role assignment cannot precede creating the managed identity, and the container app revision fails if the image has not been pushed.')
s('seq_aca_acr_b3',
  'Create the Container Apps environment → create the container app → enable ACR admin passwords → revoke AcrPull',
  'Enabling admin passwords violates credential-free deployment, and revoking AcrPull breaks subsequent revision pulls.')

# 3. App Service deployment slot swap with slot-sticky production settings
s('seq_slot_swap_ok',
  'Create the staging deployment slot on the Standard/Premium Web App → mark production-only connection strings and webhook settings as deployment slot settings → deploy and warm up the new build in staging → swap staging into production and verify health',
  'Slot-sticky settings must be pinned before swapping so staging never inherits live payment webhooks or overwrites production secrets during swap.')
s('seq_slot_swap_b1',
  'Swap staging into production → create the staging slot → deploy the build → mark settings as deployment slot settings',
  'You cannot swap a slot before creating and deploying to it, and marking settings sticky after the swap leaks staging values into production.')
s('seq_slot_swap_b2',
  'Deploy directly to production → create the staging slot → swap staging into production → mark settings as slot settings',
  'Deploying directly to production bypasses zero-downtime validation and swapping an empty staging slot overwrites production.')
s('seq_slot_swap_b3',
  'Create the staging slot on a Free F1 plan → deploy the build → swap slots → mark settings sticky',
  'Free and Basic App Service plans do not support deployment slots; Standard, Premium, or Isolated is required first.')

# 4. Cosmos DB Change Feed Processor setup (.NET SDK v3)
s('seq_cfp_ok',
  'Create the monitored container and a dedicated lease container → call GetChangeFeedProcessorBuilder<T> with processorName and delegate → attach WithInstanceName and WithLeaseContainer → call Build and StartAsync on the processor',
  'Both monitored and lease containers must exist before configuring the builder with instance/lease metadata, building the processor, and starting polling.')
s('seq_cfp_b1',
  'Call StartAsync on the processor → call GetChangeFeedProcessorBuilder<T> → create the lease container → attach WithInstanceName',
  'A processor cannot start before it is built or before its lease container exists.')
s('seq_cfp_b2',
  'Create only the monitored container → call Build and StartAsync → attach WithLeaseContainer → define the handler delegate',
  'Builder options cannot be attached after Build(), and omitting the lease container causes startup failure.')
s('seq_cfp_b3',
  'Attach WithLeaseContainer pointing to the monitored container without /id partition → call StartAsync → call GetChangeFeedProcessorBuilder<T> → call Build',
  'Builder method order is inverted, and using a separate dedicated lease container avoids RU contention and partition-key mismatches.')

# 5. Event Grid custom webhook subscription validation handshake
s('seq_eg_webhook_ok',
  'Deploy the HTTPS webhook endpoint accepting POST requests → create the Event Grid subscription pointing to the endpoint → inspect incoming SubscriptionValidationEvent and read validationCode → return HTTP 200 JSON containing validationResponse (or invoke validationUrl)',
  'Event Grid dispatches a SubscriptionValidationEvent during subscription creation and activates delivery only after the endpoint echoes validationResponse (or completes validationUrl).')
s('seq_eg_webhook_b1',
  'Create the Event Grid subscription → deploy the HTTPS endpoint later → return HTTP 202 empty body → parse SubscriptionValidationEvent',
  'If the endpoint is not live and returning validationResponse during creation, webhook validation fails before subscription creation completes.')
s('seq_eg_webhook_b2',
  'Deploy an HTTP-only port 80 endpoint → return validationCode as a response header → create the Event Grid subscription → enable TLS',
  'Event Grid requires HTTPS webhook endpoints and expects JSON `{"validationResponse": "..."}` in the response body (or GET on validationUrl).')
s('seq_eg_webhook_b3',
  'Return HTTP 200 validationResponse before reading the request → create the topic → deploy the endpoint → create the subscription',
  'The validation code is unique per subscription handshake and cannot be echoed before Event Grid sends the SubscriptionValidationEvent.')

# 6. MSAL OAuth 2.0 On-Behalf-Of (OBO) middle-tier API calling Microsoft Graph
s('seq_obo_graph_ok',
  'Register the middle-tier API scope and delegated Graph permissions in Entra ID → validate the incoming user token → call ConfidentialClientApplication.AcquireTokenOnBehalfOf(UserAssertion) → invoke Microsoft Graph with the exchanged token',
  'The middle-tier API must validate the caller token first and exchange it as a UserAssertion via ConfidentialClientApplication before calling Graph as that user.')
s('seq_obo_graph_b1',
  'Forward the front-end SPA access token directly to Microsoft Graph → validate the incoming token → register the API scope → call AcquireTokenOnBehalfOf',
  'A token whose audience (`aud`) is the custom middle-tier API is rejected by Microsoft Graph; OBO exchange must occur first.')
s('seq_obo_graph_b2',
  'Use PublicClientApplication without client credentials → call AcquireTokenForClient → pass UserAssertion → register delegated permissions',
  'OBO requires a confidential client with a secret or certificate and `AcquireTokenOnBehalfOf`, not app-only `AcquireTokenForClient`.')
s('seq_obo_graph_b3',
  'Call Microsoft Graph anonymously → call AcquireTokenOnBehalfOf → validate the incoming token → expose the API scope',
  'Graph rejects unauthenticated requests, and OBO cannot run before app registration and incoming token validation.')

# 7. Blob Archive rehydration before reading cold archival data
s('seq_rehydrate_ok',
  'Verify the blob is currently in the Archive access tier → call SetAccessTier (or CopyBlob) targeting Hot or Cool with Standard or High rehydrate priority → poll ArchiveStatus until rehydration completes and tier updates → download the blob content',
  'Archived blobs are offline and unreadable directly; changing tier or copying to Hot/Cool initiates asynchronous rehydration that must finish before download.')
s('seq_rehydrate_b1',
  'Download the archived blob stream directly → call SetAccessTier to Hot → poll ArchiveStatus → verify the Archive tier',
  'Calling Download directly on an Archive-tier blob immediately throws HTTP 409 Conflict (`BlobArchived`).')
s('seq_rehydrate_b2',
  'Set blob metadata `tier=Hot` → download the blob immediately → call SetAccessTier to Archive → poll ArchiveStatus',
  'User metadata does not trigger storage rehydration, and setting tier back to Archive keeps the blob offline.')
s('seq_rehydrate_b3',
  'Acquire an infinite blob lease → delete the blob snapshot → download the archived blob directly → call SetAccessTier',
  'Leasing does not bring an offline Archive blob online; rehydration to Hot or Cool must complete before any read succeeds.')

# 8. App Configuration dynamic refresh with Key Vault secret references
s('seq_appcfg_kv_ok',
  'Enable Managed Identity with App Configuration Data Reader + Key Vault Secrets User → add Key Vault references and a sentinel key → wire AddAzureAppConfiguration with ConfigureKeyVault and ConfigureRefresh → invoke UseAzureAppConfiguration middleware',
  'RBAC on both stores is required because App Configuration stores only the URI pointer; `ConfigureRefresh` + middleware poll the sentinel key on incoming requests.')
s('seq_appcfg_kv_b1',
  'Grant only App Configuration Data Reader (no Key Vault role) → invoke UseAzureAppConfiguration → add sentinel key → register AddAzureAppConfiguration',
  'Without Key Vault Secrets User on the vault itself, resolving a Key Vault reference throws 403 Forbidden at startup.')
s('seq_appcfg_kv_b2',
  'Add Key Vault references → wire ConfigureRefresh without UseAzureAppConfiguration middleware → expect background timer push updates → grant RBAC later',
  'In ASP.NET Core, dynamic refresh is request-driven via `UseAzureAppConfiguration()` middleware (or manual `TryRefreshAsync`), not an automatic push without it.')
s('seq_appcfg_kv_b3',
  'Copy plaintext Key Vault secret values into appsettings.json → commit to Git → wire ConfigureRefresh → enable Managed Identity',
  'Committing exported secret values defeats Key Vault reference rotation and violates secret hygiene.')

# 9. APIM Managed Identity authenticating to a backend Azure Function / Key Vault
s('seq_apim_mi_ok',
  'Enable Managed Identity on the APIM instance → grant that identity RBAC or app-role access on the target backend/Key Vault → add authentication-managed-identity in APIM policy XML → test backend calls and inspect APIM trace headers',
  'APIM needs an active managed identity and target RBAC/app-role grant before `<authentication-managed-identity>` can mint valid Entra bearer tokens.')
s('seq_apim_mi_b1',
  'Add authentication-managed-identity policy → test backend invocation → enable Managed Identity on APIM → grant RBAC on the target',
  'Saving or invoking `<authentication-managed-identity>` before enabling Managed Identity and target RBAC fails token acquisition or returns 401/403.')
s('seq_apim_mi_b2',
  'Hardcode a 2-year client secret inside `<set-header>` XML → disable Managed Identity → grant RBAC → inspect trace',
  'Hardcoding static secrets in policy XML creates rotation debt when `<authentication-managed-identity>` handles token lifecycle natively.')
s('seq_apim_mi_b3',
  'Grant RBAC to the developer laptop user → add `<validate-jwt>` in `<outbound>` → enable APIM Managed Identity → test backend',
  'Backend authorization checks the APIM gateway managed identity, not the developer workstation, and `<validate-jwt>` validates caller tokens in `<inbound>`.')

# 10. Service Bus session-enabled FIFO message processing
s('seq_sb_session_ok',
  'Create the queue or subscription with RequiresSession = true at creation time → send ServiceBusMessage instances setting a non-empty SessionId → create a ServiceBusSessionProcessor (or AcceptNextSessionAsync receiver) → process messages in order and complete/renew session locks',
  '`RequiresSession` can only be enabled when creating the entity, producers must populate `SessionId`, and consumers must use session-aware receivers/processors.')
s('seq_sb_session_b1',
  'Create a standard queue with RequiresSession = false → send messages without SessionId → toggle RequiresSession = true later → read with standard ServiceBusReceiver',
  '`RequiresSession` is immutable after creation, messages without `SessionId` are rejected on session queues, and non-session receivers fail.')
s('seq_sb_session_b2',
  'Create ServiceBusSessionProcessor → send messages with null SessionId → create the queue → complete messages before receiving',
  'Entity creation precedes processor connection, and session queues reject messages lacking a `SessionId`.')
s('seq_sb_session_b3',
  'Send messages to Queue Storage with SessionId → attach ServiceBusSessionProcessor → toggle FIFO → complete locks',
  'Azure Queue Storage does not support brokered `SessionId` FIFO locks; Azure Service Bus session entities are required.')

# 11. Event Hubs .NET v5 EventProcessorClient checkpointed consumption
s('seq_eh_epc_ok',
  'Create the Event Hub, consumer group, and Blob checkpoint container → instantiate BlobContainerClient and EventProcessorClient → register ProcessEventAsync (calling UpdateCheckpointAsync) and ProcessErrorAsync → call StartProcessingAsync before StopProcessingAsync',
  '`EventProcessorClient` coordinates partition ownership and offset checkpoints in Blob Storage and requires both event and error handlers registered prior to `StartProcessingAsync`.')
s('seq_eh_epc_b1',
  'Call StartProcessingAsync → register ProcessEventAsync without ProcessErrorAsync → create the Event Hub → create the Blob container',
  '`EventProcessorClient` throws `InvalidOperationException` if started before registering both `ProcessEventAsync` and `ProcessErrorAsync`.')
s('seq_eh_epc_b2',
  'Instantiate EventHubProducerClient → call UpdateCheckpointAsync on the producer → register ProcessEventAsync → call StopProcessingAsync first',
  'Producers publish events and never hold partition checkpoints; `EventProcessorClient` handles balanced consumer checkpointing.')
s('seq_eh_epc_b3',
  'Point all five independent microservices at `$Default` with one shared Blob prefix → call StopProcessingAsync → call StartProcessingAsync → skip UpdateCheckpointAsync',
  'Sharing one consumer group and checkpoint prefix across distinct apps causes them to steal partitions from each other instead of each reading the full stream.')

# 12. Application Insights OpenTelemetry instrumentation + KQL alert rollout
s('seq_appi_otel_ok',
  'Provision Workspace-based Application Insights and copy APPLICATIONINSIGHTS_CONNECTION_STRING → configure UseAzureMonitor() OpenTelemetry distro at startup → verify requests/dependencies in Logs → create a KQL or metric alert linked to an Action Group',
  'Workspace-based Application Insights and connection-string OpenTelemetry setup emit telemetry first so KQL/metric alerts and Action Groups monitor real signals.')
s('seq_appi_otel_b1',
  'Create a deprecated Classic InstrumentationKey-only resource → hardcode ikey without SDK → fire Action Group → provision Log Analytics later',
  'Classic Application Insights and bare Instrumentation Keys are retired in favor of Workspace-based resources and `APPLICATIONINSIGHTS_CONNECTION_STRING`.')
s('seq_appi_otel_b2',
  'Create a KQL alert rule on an empty subscription → uninstall OpenTelemetry packages → copy connection string → provision Application Insights',
  'Alert queries require a target Application Insights / Log Analytics resource and instrumented telemetry emission.')
s('seq_appi_otel_b3',
  'Set Adaptive Sampling to 0% maxTelemetryItemsPerSecond → deploy without connection string → query traces → attach Action Group',
  'Zero telemetry rate and missing connection strings discard all telemetry before it reaches Azure Monitor.')
