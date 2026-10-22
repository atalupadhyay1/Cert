"""Original AI-200 alternative labels and explanatory definitions."""
TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term: {key}')
    TERMS[key] = (label, meaning)


# --- Containers -------------------------------------------------------------
t('acr', 'Build and store versioned images in Azure Container Registry',
  'ACR keeps tagged, versioned images next to the deployment target and supports identity-based pulls. Tagging strategy and retention still need a decision.')
t('acrtask', 'Run image builds on demand or on a trigger with ACR Tasks',
  'ACR Tasks builds images in Azure on a commit or schedule without a local Docker host. It removes build-host drift but not image review.')
t('acrretention', 'Apply an ACR retention policy to prune old untagged manifests',
  'A retention policy controls storage growth and registry clutter. It does not change which image tag a deployment references.')
t('acrgeo', 'Replicate the registry to each deployment region',
  'Geo-replication reduces cross-region pull latency and gives a local copy during a regional failure. It adds cost and replication management.')
t('appservice', 'Deploy the image to Azure App Service as a web app',
  'App Service runs a container with managed patching, deployment slots, and built-in authentication options. It is not a Kubernetes control plane.')
t('appsetting', 'Supply configuration through App Service application settings',
  'Application settings become environment variables for the container and can be swapped per slot. Sensitive values should still reference a vault.')
t('kvref', 'Reference a Key Vault secret from the app configuration instead of storing it',
  'A Key Vault reference resolves at runtime so the secret is never written into application settings. The app identity still needs permission to read it.')
t('slotswap', 'Stage the change in a deployment slot and swap after verification',
  'A slot swap warms the new version before it takes production traffic and makes rollback a second swap. Slot-local settings must be marked sticky.')
t('containerapps', 'Deploy the service to Azure Container Apps',
  'Container Apps provides a managed environment, revisions, and KEDA-based scaling without cluster administration. Platform limits differ from AKS.')
t('revision', 'Create a new Container Apps revision and shift traffic between revisions',
  'Revision-based traffic splitting enables canary and blue-green releases. Revision mode and scale rules must be set deliberately.')
t('ingress', 'Configure Container Apps ingress for internal-only access',
  'Internal ingress keeps the endpoint inside the environment virtual network. It is an exposure control, not an authorization control.')
t('keda', 'Scale the container app on an event source with a KEDA scaler',
  'KEDA scalers drive replica count from queue length, lag, or other event metrics, including scale to zero. Cool-down and max replicas bound the behavior.')
t('kedaqueue', 'Scale on the Service Bus queue length with a KEDA Azure Service Bus scaler',
  'A queue-length scaler adds replicas while work is backed up and removes them when the queue drains. Message lock duration must exceed processing time.')
t('cpuonly', 'Scale only on CPU utilization without an event scaler',
  'CPU-based scaling reacts after work is already queued and cannot scale to zero on an empty queue. It suits steady request-driven services.')
t('aks', 'Deploy the workload to Azure Kubernetes Service',
  'AKS gives full Kubernetes control, including custom controllers and networking. You own node pools, upgrades, and manifest hygiene.')
t('manifest', 'Apply a declarative Kubernetes manifest to the cluster',
  'A manifest declares the desired deployment, service, and probe configuration in version control. Applying it repeatedly is idempotent.')
t('hpa', 'Rely on the horizontal pod autoscaler on CPU',
  'HPA adjusts replicas from resource metrics but needs metrics-server and enough node capacity. It cannot scale to zero.')
t('probe', 'Add readiness and liveness probes to the pod specification',
  'Readiness gates traffic until the app can serve it, and liveness restarts a wedged container. Wrong thresholds cause restart loops.')
t('loganalytics', 'Query container logs and Kubernetes events in Log Analytics',
  'Container Apps and AKS surface stdout logs and platform events into a workspace for KQL analysis. Verbosity and retention cost money.')
t('connectivity', 'Test end-to-end connectivity from inside the container to each dependency',
  'Reaching a dependency from the pod or replica proves DNS, egress, and firewall paths together. Host-side tests can succeed while the container path fails.')
t('aci', 'Run the batch job in Azure Container Instances',
  'Container Instances starts a single container group quickly for short tasks. It has no orchestrator-level scaling or revision model.')
t('imagetag', 'Deploy the mutable latest tag and let the platform resolve it',
  'A floating tag removes the link between a deployed revision and a specific build, so rollback and audit become guesswork.')

# --- Cosmos DB --------------------------------------------------------------
t('cosmos', 'Store the documents in Azure Cosmos DB for NoSQL',
  'Cosmos DB gives globally distributed, low-latency document access with tunable consistency. Partition key and RU planning determine the cost profile.')
t('cosmosquery', 'Query through the Cosmos DB SDK with parameterized queries',
  'SDK queries keep the client on the supported data plane and parameterization avoids injection and plan churn. Cross-partition queries still cost more.')
t('crosspartition', 'Include the partition key in the query predicate',
  'A point or single-partition query avoids fan-out across partitions. Cross-partition queries consume more RUs and add latency.')
t('indexpolicy', 'Restrict the indexing policy to the paths the queries use',
  'Selective indexing cuts write RU charge and storage for unused paths. Excluded paths cannot be filtered efficiently later.')
t('indexall', 'Index every property by using the default automatic policy',
  'Indexing everything is simple and makes ad hoc queries possible, at higher write cost and storage. It is a default, not an optimization.')
t('consistency', 'Choose the account consistency level that matches the read requirement',
  'Consistency trades freshness against latency, availability, and RU cost. The level is set at the account and can be relaxed per request.')
t('sessionconsistency', 'Use session consistency for reads within the same client session',
  'Session consistency guarantees monotonic reads for one session and is the common default for user-facing apps. It does not promise global freshness.')
t('strongconsistency', 'Use strong consistency for every read in the account',
  'Strong consistency guarantees the latest committed write globally at the cost of higher latency and reduced availability during partitions.')
t('eventualconsistency', 'Use eventual consistency to minimize read cost',
  'Eventual consistency is the cheapest and most available option but returns possibly stale data. It fits non-critical counters, not balances.')
t('ru', 'Increase provisioned throughput and watch the RU charge per query',
  'Request units measure the work a query performs, so tuning the query is often cheaper than adding throughput. Monitor normalized RU consumption.')
t('autoscale', 'Enable autoscale throughput with a maximum RU limit',
  'Autoscale follows demand between a minimum and maximum, avoiding throttling at peak without paying for peak all day. The maximum still caps the bill.')
t('partitionkey', 'Choose a high-cardinality partition key that spreads writes',
  'A good partition key distributes storage and throughput and keeps common queries single-partition. Low cardinality creates hot partitions.')
t('changefeed', 'Run a change feed processor to react to new and updated items',
  'The change feed delivers an ordered stream of changes per partition for downstream processing. It is not a delete feed, so deletions need a workaround.')
t('leasestore', 'Use a lease container to coordinate change feed readers',
  'Leases track partition ownership so multiple processor instances share work and resume from a continuation token. Lease writes consume RUs too.')
t('vectorcosmos', 'Store embeddings in a vector property and query with VectorDistance',
  'Cosmos DB for NoSQL supports vector properties and a distance function for similarity search in the same document store. Dimensions and index type must match the model.')
t('vectordimension', 'Declare the embedding dimensions and vector index type on the container policy',
  'The container vector policy fixes dimensions, distance function, and index type, so a model change requires a new policy. Mismatched dimensions fail at write time.')
t('bruteforce', 'Scan every document and compute similarity in application code',
  'Application-side scoring works for tiny collections and tests, but it moves all data over the wire and does not scale with corpus size.')
t('diskann', 'Use the DiskANN vector index for large collections',
  'DiskANN trades some recall for memory efficiency on large sets. Recall and latency should be measured on representative queries.')

# --- PostgreSQL -------------------------------------------------------------
t('pgvector', 'Store embeddings in PostgreSQL by using the pgvector extension',
  'pgvector keeps vectors beside relational data, so filters and joins run in one query. Index type and parameter tuning decide latency.')
t('hnsw', 'Create an HNSW index for low-latency approximate search',
  'HNSW gives fast approximate nearest-neighbour queries with a larger memory footprint and slower builds. Recall is tunable at query time.')
t('ivfflat', 'Create an IVFFlat index to save memory on a large table',
  'IVFFlat uses clustering lists and needs periodic rebuilds as data grows, but costs less memory than HNSW. Probes trade recall for speed.')
t('seqscan', 'Query without a vector index and let PostgreSQL scan the table',
  'An exact scan is accurate but scales linearly and burns compute. It is a baseline for measuring recall, not a production strategy.')
t('metadatafilter', 'Filter on metadata columns in the same query as the vector search',
  'Combining a WHERE filter with the distance operator keeps retrieval inside the caller\'s scope and improves relevance. Index the filter columns too.')
t('postfilter', 'Retrieve nearest neighbours first and discard unauthorized rows in the application',
  'Post-filtering can return fewer results than requested and can leak existence or counts if the filtering is careless. Push authorization into the query.')
t('pool', 'Reuse a bounded connection pool instead of opening a connection per request',
  'A bounded pool amortizes connection setup and protects the server from connection storms. Pool size must match server limits.')
t('pgbouncer', 'Place a connection pooler in front of PostgreSQL for many short-lived clients',
  'An external pooler multiplexes server connections for serverless or highly concurrent clients. Session-level features may be unavailable in transaction mode.')
t('prepared', 'Use prepared statements and batch round trips',
  'Prepared statements avoid repeated planning and reduce chatty network calls. They pair well with pooling but can interact with pool modes.')
t('pgcompute', 'Scale compute and memory to fit index size and query concurrency',
  'Vector indexes are memory-hungry, so undersized compute causes swapping and slow queries. Right-size before tuning index parameters.')
t('pgstorage', 'Increase storage throughput for index builds and bulk loads',
  'Index creation and bulk loads are I/O heavy, and throttled storage stretches maintenance windows. Storage limits are separate from compute.')
t('pgschema', 'Model typed columns for filters and one vector column for the embedding',
  'Explicit types keep filters fast and make the embedding contract clear. Storing vectors as text defeats index use.')
t('pgreplica', 'Add a read replica and send all vector queries to it',
  'A replica offloads read traffic but introduces replication lag, which is dangerous for freshly written evidence. It does not reduce index memory pressure.')

# --- Managed Redis ----------------------------------------------------------
t('redis', 'Cache responses in Azure Managed Redis',
  'A cache absorbs repeated reads and cuts latency for hot data. Cache keys, TTLs, and invalidation must match the freshness requirement.')
t('redisttl', 'Set a TTL on each cached entry',
  'A TTL bounds staleness and reclaims memory without a manual sweep. Too long a TTL hides source changes; too short wastes the cache.')
t('redisinvalidate', 'Invalidate or overwrite the cache entry when the source changes',
  'Write-through or explicit invalidation keeps cached answers consistent with the system of record. Without it, TTL is the only bound on staleness.')
t('redisvector', 'Create a vector index in Managed Redis for similarity search',
  'Redis vector search serves low-latency similarity queries from memory. The corpus must fit the memory budget and be rebuilt on model change.')
t('redissession', 'Store user session state in Managed Redis with an expiry',
  'Session storage in Redis survives instance restarts and supports distributed instances. Sessions must be scoped and expiring.')
t('redisevict', 'Rely on the eviction policy and skip explicit TTLs',
  'Eviction protects memory but evicts unpredictably, so a hot key can vanish before its freshness bound is reached. It is not a substitute for TTL design.')
t('redisclear', 'Flush the database after each deployment to guarantee fresh data',
  'Flushing removes all cached content at once, causing a stampede to the origin and a latency cliff. Targeted invalidation is safer.')
t('rediscachelock', 'Use a distributed lock in Redis to make processing idempotent',
  'A lock can serialize work across instances, but correctness under retries still needs idempotency keys in the data store. Locks expire and can be lost.')

# --- Messaging and Functions ------------------------------------------------
t('sbqueue', 'Queue the work on a Service Bus queue and process it with a worker',
  'A queue decouples producers from a single consumer group and smooths bursts. Delivery semantics depend on receive mode and completion.')
t('sbtopic', 'Publish to a Service Bus topic with multiple subscriptions',
  'Topics fan out one message to independent subscribers, each with its own filter and dead-letter queue. Subscribers process at their own pace.')
t('sbfilter', 'Add a SQL or correlation filter to a subscription',
  'Subscription filters route only matching messages to a handler, reducing wasted processing. Filter evaluation happens broker-side on message properties.')
t('sbsession', 'Use Service Bus sessions to keep related messages ordered',
  'Sessions give ordered, exclusive processing per session ID across competing consumers. They require session-aware senders and receivers.')
t('dlq', 'Inspect the dead-letter queue and resubmit corrected messages',
  'Dead-lettering preserves poison messages for diagnosis instead of losing them. Resubmission needs a fix and an idempotent handler.')
t('maxdelivery', 'Set a maximum delivery count and handle the dead-letter path',
  'A delivery cap stops infinite retries of a failing message and moves it to the dead-letter queue. The cap must exceed legitimate transient retries.')
t('duplicate', 'Enable duplicate detection on the queue',
  'A duplicate-detection window drops repeated sends within the window, which helps with at-least-once producers. The window is time-bounded.')
t('peeklock', 'Receive with peek-lock and complete or abandon explicitly',
  'Peek-lock keeps the message locked until the handler completes it, giving at-least-once processing with retry. Lock duration must exceed processing time.')
t('randdelete', 'Receive in receive-and-delete mode for at-most-once delivery',
  'Receive-and-delete removes the message on delivery, so a crash loses work silently. It suits telemetry, not payments.')
t('eventgrid', 'Publish the state change as an Event Grid event',
  'Event Grid delivers discrete notifications to subscribers with retries and filtering. It carries events, not large payloads or ordered streams.')
t('egfilter', 'Filter the Event Grid subscription by subject or event type',
  'Subject and event-type filters keep handlers focused and reduce cost. Filters are evaluated on event metadata, not payload body.')
t('egcustom', 'Define a custom event schema for the topic',
  'A custom schema fits domain events that are not resource lifecycle notifications. Consumers must version the schema contract.')
t('egretry', 'Rely on Event Grid retries with a dead-letter destination',
  'Event Grid retries failed deliveries with backoff and can store undeliverable events. Handlers must still be idempotent.')
t('eventhubs', 'Stream telemetry through Azure Event Hubs',
  'Event Hubs ingests high-volume ordered streams with partitions and consumer groups. It is a streaming log, not a task queue.')
t('queuestorage', 'Use Azure Queue Storage for the work items',
  'Queue Storage is simple and cheap for large backlogs with at-least-once delivery. It lacks topics, sessions, and scheduled messages.')
t('function', 'Implement the handler as an Azure Function',
  'Functions runs small event-driven code without managing a host. Execution limits and cold starts depend on the hosting plan.')
t('trigger', 'Bind a queue or event trigger to the function',
  'A trigger starts the function when work arrives and handles the receive loop for you. Poison-message behavior is configured in host settings.')
t('binding', 'Use input and output bindings instead of hand-written SDK calls',
  'Bindings reduce boilerplate for common inputs and outputs and are configured declaratively. Complex operations still need the SDK.')
t('durable', 'Orchestrate the multi-step workflow with Durable Functions',
  'Durable Functions provides orchestrations, activities, timers, and retries with checkpointed state. Orchestrator code must stay deterministic.')
t('httptrigger', 'Expose the endpoint through an HTTP trigger',
  'An HTTP trigger gives a synchronous API endpoint with route and authorization configuration. Long-running work should hand off to a queue.')
t('premiumplan', 'Host the function app on a premium plan with pre-warmed instances',
  'A premium plan reduces cold starts and supports virtual network integration and longer timeouts. It costs more than consumption.')
t('consumptionplan', 'Host the function app on the consumption plan',
  'Consumption bills per execution and scales automatically, with cold starts and a timeout ceiling. It fits spiky, short work.')
t('deployfunc', 'Deploy the function app through a CI pipeline with app settings applied',
  'Pipeline deployment keeps code and configuration versioned together and repeatable. Secrets belong in a vault reference, not in the pipeline file.')
t('idempotent', 'Make the handler idempotent by using a message or business key',
  'At-least-once delivery means duplicates will happen, so the write must tolerate replay. A stored key makes the retry safe.')

# --- Security, configuration, observability ---------------------------------
t('keyvault', 'Store the secret in Azure Key Vault and read it at runtime',
  'A vault centralizes secret storage with access control and audit. Retrieval should use an identity, not a copied credential.')
t('managedidentity', 'Authenticate with a managed identity instead of a stored key',
  'A managed identity issues tokens from the platform, removing secret distribution from the app. Role assignment still scopes what it can reach.')
t('rotation', 'Rotate the secret on a schedule and let apps resolve the current version',
  'Rotation limits the value of a leaked secret, but callers must read the latest version rather than caching an old one forever.')
t('versioned', 'Pin the application to a specific secret version',
  'Pinning a version makes a rotation invisible to the app until it is redeployed, which is useful for break-glass and dangerous for routine rotation.')
t('appconfig', 'Store settings and feature flags in Azure App Configuration',
  'App Configuration separates configuration from code and supports labels, feature flags, and Key Vault references. Change still needs a refresh strategy.')
t('appconfigrefresh', 'Enable configuration refresh so changes apply without a restart',
  'Sentinel-key or polling refresh lets a running app pick up new settings. Refresh intervals trade responsiveness against request volume.')
t('labels', 'Use App Configuration labels to separate environments',
  'Labels keep dev, test, and prod values in one store with one key schema. A misconfigured label selector silently serves the wrong values.')
t('otel', 'Instrument the service with the OpenTelemetry SDK',
  'OpenTelemetry emits vendor-neutral traces, metrics, and logs with context propagation. Exporters and sampling decide what reaches the backend.')
t('otelcollector', 'Export telemetry through an OpenTelemetry collector',
  'A collector batches, filters, and routes telemetry, and decouples app configuration from the backend. It is another component to run and monitor.')
t('propagatetrace', 'Propagate trace context across every service and queue hop',
  'Propagation stitches one trace across HTTP, messaging, and Functions so the whole path is visible. Missing propagation breaks the trace at that hop.')
t('correlation', 'Correlate logs with the operation or trace identifier',
  'Including the trace ID in log records lets you pivot from a failed span to its log lines. Without it, logs and traces are separate worlds.')
t('kql', 'Query the workspace with KQL to find the failing operation',
  'KQL filters, projects, and aggregates log and metric tables in Log Analytics. Start narrow with a time range and a request ID.')
t('kqlsummarize', 'Aggregate with summarize and bin to see the failure rate over time',
  'Time-binned aggregation reveals the shape of an incident: a step change, a ramp, or a periodic spike. Averages alone hide short outages.')
t('kqltables', 'Join the requests and dependencies tables on the operation ID',
  'Joining request and dependency telemetry shows which downstream call fails inside a slow request. Cross-workspace joins need the right scope.')
t('alert', 'Create an alert rule on the failure rate or latency metric',
  'An alert turns a threshold breach into a notification or action. Thresholds need a baseline, or the alert is noise.')
t('appinsights', 'Send telemetry to Application Insights and inspect the transaction view',
  'Application Insights correlates requests, dependencies, and exceptions into end-to-end transactions. Sampling can hide rare failures.')
t('rbac', 'Assign a least-privilege role to the application identity',
  'A scoped role grants only the operations the app performs and limits blast radius. Prefer built-in roles over broad contributor grants.')
t('privateendpoint', 'Reach the data service through a private endpoint',
  'A private endpoint keeps traffic on the virtual network and removes public exposure. DNS resolution must be wired to the private zone.')
t('diagnostic', 'Enable diagnostic settings to route platform logs to the workspace',
  'Platform logs and metrics must be routed before they can be queried or alerted on. Retention and cost follow the workspace settings.')

# --- Ordering sequences -----------------------------------------------------
t('seqacr', 'Build the image → scan it → push a versioned tag to ACR → deploy that tag → verify health',
  'A build is scanned and versioned before deployment so the deployed artifact is the reviewed one and can be rolled back by tag.')
t('seqacrbad1', 'Push a versioned tag to ACR → build the image → deploy that tag → scan it → verify health',
  'The image cannot be pushed before it is built, and scanning after deployment leaves a window of unreviewed runtime.')
t('seqacrbad2', 'Build the image → deploy the latest tag → scan it → push a versioned tag → verify health',
  'Deploying an unversioned tag severs the link between what runs and what was built and scanned.')
t('seqacrbad3', 'Scan the image → build the image → verify health → push a versioned tag → deploy that tag',
  'Scanning requires a built image, and health verification cannot precede deployment.')
t('seqcapp', 'Build and push the image → deploy a new revision → shift a small traffic percentage → check metrics → promote or roll back',
  'A canary revision accepts a small share of traffic so metrics decide promotion rather than optimism.')
t('seqcappbad1', 'Shift all traffic to a new revision → deploy the revision → check metrics → build the image → promote',
  'Full traffic cannot move to a revision that does not exist yet, and the image must exist before the revision.')
t('seqcappbad2', 'Deploy a new revision → shift all traffic → build and push the image → check metrics → roll back',
  'Building after traffic is shifted means the running revision has no reviewed artifact behind it.')
t('seqcappbad3', 'Check metrics → deploy a new revision → build and push the image → shift a small traffic percentage → promote',
  'Metrics cannot be checked before the revision serves traffic.')
t('seqaks', 'Write the manifest → apply it to the cluster → wait for pod readiness → test ingress connectivity',
  'Readiness must pass before a connectivity test proves anything, and the manifest must exist before it is applied.')
t('seqaksbad1', 'Apply the manifest → write the manifest → test ingress connectivity → wait for pod readiness',
  'A manifest is authored before it is applied, and connectivity is meaningless while pods are not ready.')
t('seqaksbad2', 'Wait for pod readiness → apply the manifest → write the manifest → test ingress connectivity',
  'Pods cannot become ready before the manifest is applied.')
t('seqaksbad3', 'Write the manifest → test ingress connectivity → apply it to the cluster → wait for pod readiness',
  'Ingress cannot be tested before the workload exists in the cluster.')
t('seqcosmos', 'Create the container with a vector policy → upsert items with embeddings → query with VectorDistance → apply metadata filters',
  'The vector policy fixes dimensions and index type, so it must exist before vector writes and queries.')
t('seqcosmosbad1', 'Upsert items with embeddings → create the container with a vector policy → apply metadata filters → query with VectorDistance',
  'Items cannot be written before the container exists with a matching vector policy.')
t('seqcosmosbad2', 'Query with VectorDistance → upsert items with embeddings → create the container with a vector policy → apply metadata filters',
  'A similarity query needs indexed vectors, which require the container and its policy first.')
t('seqcosmosbad3', 'Apply metadata filters → query with VectorDistance → create the container with a vector policy → upsert items with embeddings',
  'Filtering and querying cannot precede the container and its vector data.')
t('seqpg', 'Create the vector extension → create the table with a vector column → build the index → query nearest neighbours with a distance operator',
  'The extension and typed column must exist before an index can be built, and the index before the query is efficient.')
t('seqpgbad1', 'Build the index → create the vector extension → create the table with a vector column → query nearest neighbours',
  'An index cannot be built before the extension and the table exist.')
t('seqpgbad2', 'Query nearest neighbours → build the index → create the vector extension → create the table with a vector column',
  'Querying before the schema exists cannot succeed, and the index cannot precede the table.')
t('seqpgbad3', 'Create the table with a vector column → query nearest neighbours → create the vector extension → build the index',
  'The extension is required for the vector type, and the query should follow index creation for usable latency.')
t('seqmsg', 'Publish the message → receive with peek-lock → process the work → complete the message → dead-letter after the delivery limit',
  'Peek-lock keeps the message until the handler succeeds, and only repeated failures should dead-letter it.')
t('seqmsgbad1', 'Receive with peek-lock → publish the message → complete the message → process the work → dead-letter after the delivery limit',
  'The message cannot be received before it is published, and completion must follow processing.')
t('seqmsgbad2', 'Publish the message → complete the message → receive with peek-lock → process the work → dead-letter after the delivery limit',
  'Completing a message before processing discards the work and defeats at-least-once delivery.')
t('seqmsgbad3', 'Process the work → receive with peek-lock → publish the message → complete the message → dead-letter after the delivery limit',
  'Work cannot be processed before the message is published and received.')
t('seqeg', 'Publish a custom event → evaluate the subscription filter → deliver to the handler → retry on failure → dead-letter undeliverable events',
  'Filtering happens before delivery, retries handle transient failures, and dead-lettering preserves what cannot be delivered.')
t('seqegbad1', 'Deliver to the handler → publish a custom event → evaluate the subscription filter → retry on failure → dead-letter undeliverable events',
  'Delivery cannot precede publication and filtering.')
t('seqegbad2', 'Publish a custom event → deliver to the handler → evaluate the subscription filter → dead-letter undeliverable events → retry on failure',
  'A filter is evaluated before delivery, and retries must occur before dead-lettering.')
t('seqegbad3', 'Evaluate the subscription filter → publish a custom event → dead-letter undeliverable events → deliver to the handler → retry on failure',
  'A filter cannot evaluate an event that has not been published.')
t('seqkv', 'Store the secret in Key Vault → grant the app identity access → reference the secret from the app → rotate the secret → the app reads the new version',
  'Access must be granted before the reference resolves, and the app must read the current version after rotation.')
t('seqkvbad1', 'Grant the app identity access → store the secret in Key Vault → rotate the secret → reference the secret from the app → the app reads the new version',
  'Access can be granted first, but rotation cannot precede storing the secret.')
t('seqkvbad2', 'Reference the secret from the app → rotate the secret → store the secret in Key Vault → grant the app identity access → the app reads the new version',
  'A reference cannot resolve before the secret and the access grant exist.')
t('seqkvbad3', 'Rotate the secret → reference the secret from the app → store the secret in Key Vault → grant the app identity access → the app reads the new version',
  'There is nothing to rotate or reference before the secret is stored.')

# --- Additional service options ---------------------------------------------
t('minreplicas', 'Set a minimum replica count above zero for the container app',
  'A warm minimum replica removes scale-to-zero cold starts for latency-critical endpoints. It keeps paying for idle capacity.')
t('cooldown', 'Tune the scale rule cool-down period and maximum replicas',
  'Cool-down prevents replica flapping, and a maximum replica cap bounds cost and downstream load. Both are per-rule settings.')
t('serviceconnector', 'Create an Azure service connector binding between the app and the dependency',
  'A service connector writes connection details and can provision identity-based access. The resulting configuration should still be reviewed.')
t('privatezone', 'Link the private DNS zone so the private endpoint name resolves',
  'A private endpoint needs matching name resolution or clients still resolve the public address. The zone must be linked to the workload network.')
t('cosmospartitionhot', 'Accept a low-cardinality partition key for simpler queries',
  'A low-cardinality key concentrates throughput on one partition, causing throttling even when total throughput looks sufficient.')
t('cosmosvectorindex', 'Match the vector index type and dimensions to the embedding model',
  'The container vector policy is fixed at creation, so a model or dimension change needs a new container and a re-index.')
t('cosine', 'Use the cosine distance function that matches how the embeddings were trained',
  'Distance function choice must match the embedding model and the normalization used at indexing time. A mismatch degrades recall silently.')
t('vacuum', 'Run VACUUM and ANALYZE after bulk loads and large deletes',
  'Statistics and dead-tuple cleanup change plan quality and index performance. Autovacuum tuning matters for churn-heavy vector tables.')
t('pgworkmem', 'Increase maintenance and query memory settings for index builds and sorts',
  'Index builds and large sorts spill to disk when work memory is too small, stretching maintenance windows and slowing queries.')
t('pgreadonly', 'Send only reporting queries to the read replica',
  'Read replicas lag, so routing fresh evidence reads to them can return stale or missing rows. Keep write-after-read paths on the primary.')
t('keyvaultaccess', 'Grant the app identity data-plane access to the vault',
  'Vault access is a separate authorization decision from the app identity. Without a data-plane role or policy the reference fails at runtime.')
t('keyvaultpurge', 'Enable purge protection and soft delete on the vault',
  'Soft delete and purge protection stop accidental or malicious permanent loss of secrets. They also constrain how names can be reused.')
t('appconfigkvref', 'Reference the Key Vault secret from an App Configuration key value',
  'A Key Vault reference keeps non-secret settings in App Configuration while the value stays in the vault. The app identity needs both sets of permissions.')
t('otelsampling', 'Use head or tail sampling so trace volume stays within budget',
  'Sampling keeps telemetry cost bounded, but aggressive sampling can hide rare failures. Tail sampling can retain errors preferentially.')
t('sbprefetch', 'Increase prefetch count to reduce round trips',
  'Prefetch reduces latency per message by batching receives, at the cost of holding more locked messages. Lock duration must cover the batch.')
t('sbautoforward', 'Use auto-forwarding to chain a queue into a topic',
  'Auto-forwarding moves messages between entities without custom code, which can simplify topology. It adds a hop that complicates diagnosis.')
t('egsystemtopic', 'Subscribe to a system topic for resource events',
  'System topics carry Azure resource lifecycle events. Domain events that are not resource changes need a custom topic and schema.')
t('funcidentity', 'Assign a managed identity to the function app and use it for downstream calls',
  'A function app can authenticate with a managed identity, so no connection secret is needed in app settings.')
t('kqlproject', 'Project only the columns needed and filter by time first',
  'Reducing columns and rows early lowers query cost and latency. Broad queries over long ranges are the usual cause of slow KQL.')
t('kqlmaterialize', 'Store repeated aggregations in a materialized view or update policy',
  'Precomputed results avoid recomputing expensive aggregations on every dashboard refresh. The trade-off is storage and freshness lag.')
t('durabletimeout', 'Move long-running work out of the HTTP request into a queue',
  'HTTP requests have platform timeout limits, so long work belongs behind a queue or orchestration with a status endpoint.')
t('containerappsjob', 'Run the batch work as a Container Apps job',
  'Container Apps jobs run to completion with their own trigger and retry semantics, unlike a long-lived revision. They fit scheduled or queue-driven batches.')
t('cosmosttl', 'Set an item time-to-live on the container',
  'Item TTL expires documents automatically, which controls storage growth and data retention. It does not archive the expired content.')
t('cosmosbatch', 'Batch related writes in a transactional batch within one partition key',
  'A transactional batch applies all-or-nothing within a single partition key. It cannot span partitions and still consumes RU per operation.')
t('pgexplain', 'Inspect the plan with EXPLAIN ANALYZE before changing indexes',
  'The plan shows whether PostgreSQL uses the vector index and where the time goes. Adding indexes without reading the plan often misses the cause.')
t('monitormetrics', 'Alert on platform metrics rather than only on log queries',
  'Platform metrics are cheap and near-real-time, so they suit latency and failure-rate alerts. Log-based alerts add latency and query cost.')
t('functionslot', 'Use a deployment slot on the function app for staging',
  'A staging slot lets a new build warm up and be validated before the swap. Slot settings that must not move are marked sticky.')
t('workloadidentity', 'Federate a Kubernetes service account to a managed identity',
  'Workload identity lets pods obtain tokens without stored secrets. Each workload should get its own identity and narrow role.')
t('sbscheduled', 'Schedule the message for future enqueueing',
  'A scheduled message becomes visible at a set time, which supports reminders and delayed retries. It is not a substitute for a durable timer.')
t('egidentity', 'Deliver events by using a managed identity instead of a key',
  'Identity-based delivery removes a shared key from the subscription. The receiver still validates the caller and payload.')
t('containerappsenv', 'Deploy into a Container Apps environment attached to the workload virtual network',
  'A virtual-network-attached environment enables private access to dependencies and internal ingress. It also shifts DNS and egress design to you.')
t('kedascaleidentity', 'Give the KEDA scaler a managed identity to read the event source',
  'A scaler needs permission to read queue metrics; identity-based access avoids a stored connection string. Least privilege still applies to that identity.')
