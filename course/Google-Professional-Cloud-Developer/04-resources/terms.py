"""Option bank for the Professional Cloud Developer practice sets.

Every option label is a platform choice or an engineering action, so an item can
ask which decision fits the stated constraints without the distractor collapsing
into a definition. Keys are authoring identifiers only and never appear in an
export.
"""

TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f"duplicate option key: {key}")
    TERMS[key] = (label, meaning)


# --- Compute platform and shape ---------------------------------------------
t('cloud_run', 'Deploy the service to Cloud Run',
  'A managed container runtime that scales to zero and bills per request while it serves traffic.')
t('gke', 'Deploy the workload to Google Kubernetes Engine',
  'A managed Kubernetes control plane where pods, node pools and cluster-scoped policy are yours to configure.')
t('compute_engine', 'Run the application on Compute Engine instances',
  'Virtual machines where the operating system, runtime and scaling group are all managed by the team.')
t('cloud_functions', 'Deploy the handler as a Cloud Functions function',
  'An event-triggered function runtime for a single-purpose handler rather than a long-lived service.')
t('app_engine', 'Deploy to App Engine standard',
  'A platform runtime that manages scaling for a supported language version and its sandbox limits.')
t('cloud_run_jobs', 'Run the batch work as a Cloud Run job',
  'A task-shaped execution that runs to completion instead of serving requests.')
t('gke_autopilot', 'Use GKE Autopilot for the cluster',
  'A cluster mode where node provisioning and sizing are handled for the workload.')
t('set_concurrency', 'Raise the per-instance concurrency limit',
  'Let each instance serve more simultaneous requests before another instance is started.')
t('set_min_instances', 'Keep a minimum number of instances warm',
  'Pay for idle capacity so a cold start never appears in the latency percentiles.')
t('set_max_instances', 'Cap the maximum instance count',
  'Bound the blast radius and the bill at the cost of queueing when the cap is reached.')
t('set_cpu_boost', 'Enable CPU boost at startup',
  'Give extra CPU during start-up so initialization finishes faster at a small extra charge.')
t('request_based_billing', 'Use request-based billing',
  'Charge only while a request is being handled, which suits bursty traffic.')
t('instance_based_billing', 'Use instance-based billing',
  'Charge for the whole instance lifetime, which suits steady background work.')
t('rightsize_requests', 'Set CPU and memory requests from measured use',
  'Give the scheduler real numbers so placement and scaling decisions are not guesses.')
t('raise_limits', 'Raise the container limits above the observed peak',
  'Allow the process the headroom it needs so it is not throttled or killed.')
t('node_pool_autoscaling', 'Enable node pool autoscaling',
  'Add or remove nodes as pending pods demand capacity.')
t('spot_nodes', 'Run the batch node pool on Spot VMs',
  'Use reclaimable capacity for work that can tolerate a node disappearing.')
t('committed_use', 'Buy committed use discounts for the steady baseline',
  'Trade a term commitment for a lower unit price on capacity that never idles.')

# --- Geography, availability, traffic --------------------------------------
t('regional_deployment', 'Deploy in one region across multiple zones',
  'Spread instances over zones of a single region so a zone failure does not stop the service.')
t('multi_region_deployment', 'Deploy the service in two regions behind a global load balancer',
  'Serve from two regions so a regional failure leaves capacity elsewhere.')
t('global_lb', 'Put a global external Application Load Balancer in front',
  'A single anycast address that routes to the nearest healthy backend.')
t('regional_lb', 'Use a regional load balancer',
  'A load balancer scoped to one region with a regional address.')
t('session_affinity', 'Enable session affinity on the backend service',
  'Pin a client to one backend for the life of its session.')
t('stateless_sessions', 'Store session state in a shared datastore',
  'Move the state out of the instance so any instance can serve any request.')
t('sticky_cookie', 'Use a generated cookie for stickiness',
  'Route the client by cookie rather than by address or header.')
t('health_check_lb', 'Add a health check endpoint to the backend service',
  'Let the load balancer stop sending traffic to an unhealthy instance.')
t('traffic_split', 'Split traffic between revisions by percentage',
  'Send a fraction of requests to the new revision while the old one still serves the rest.')
t('tag_routing', 'Route by revision tag or header',
  'Send only tagged requests to the new revision for internal testing.')
t('rollback_revision', 'Shift traffic back to the previous revision',
  'Return all traffic to the known-good revision when the new one misbehaves.')
t('feature_flag', 'Gate the change behind a feature flag',
  'Ship the code dark and enable it per cohort without a redeploy.')
t('canary', 'Canary the release at a small percentage first',
  'Expose the new version to a slice of traffic before widening it.')

# --- Caching, APIs, messaging -----------------------------------------------
t('memorystore', 'Cache reads in Memorystore',
  'A managed Redis-compatible cache in front of the system of record.')
t('cache_aside', 'Load through a cache-aside pattern',
  'Read the cache, fall back to the database, and populate the cache on a miss.')
t('in_process_cache', 'Cache inside each instance process',
  'A per-instance cache that is fast but not shared between instances.')
t('cdn_cache', 'Serve static content from Cloud CDN',
  'Cache responses at the edge so repeated requests never reach the origin.')
t('rest_json', 'Expose a REST API with JSON payloads',
  'A resource-oriented HTTP interface that browsers and simple clients can call.')
t('grpc', 'Expose a gRPC service',
  'A binary, schema-driven RPC interface with streaming and generated clients.')
t('grpc_web', 'Serve gRPC-Web for browser clients',
  'A compatibility layer so browser code can call a gRPC service.')
t('openapi_spec', 'Publish an OpenAPI specification',
  'A machine-readable contract that generates clients and validates requests.')
t('apigee', 'Put Apigee in front of the API',
  'An API management layer for quotas, keys, mediation and analytics.')
t('api_gateway', 'Use API Gateway for the API',
  'A lighter managed gateway for routing and key-based quota enforcement.')
t('rate_limit', 'Apply a rate limit per client key',
  'Reject or queue requests above a threshold so one client cannot exhaust the service.')
t('quota_per_key', 'Set a quota per API key',
  'Bound how many calls a plan allows in a window.')
t('api_versioning', 'Introduce a new API version alongside the old one',
  'Keep the old contract working while the new one is adopted.')
t('backward_compatible', 'Add the field in a backward-compatible way',
  'Extend the contract so existing clients keep working unchanged.')
t('pubsub_topic', 'Publish the event to a Pub/Sub topic',
  'A durable, at-least-once message channel with independent subscribers.')
t('pubsub_push', 'Deliver to an HTTPS push subscription',
  'Push each message to an endpoint instead of having the consumer pull.')
t('pubsub_pull', 'Have the worker pull from the subscription',
  'The consumer controls the pace and acknowledges messages itself.')
t('eventarc', 'Route the event with Eventarc',
  'A trigger path that turns a Cloud Audit Log or resource event into a delivery.')
t('cloud_tasks', 'Queue the work as a Cloud Tasks task',
  'A task queue with retries and rate control aimed at a specific target.')
t('cloud_scheduler', 'Schedule the invocation with Cloud Scheduler',
  'A cron-style trigger that calls a target on a fixed timetable.')
t('workflows', 'Orchestrate the steps in Workflows',
  'A stateful sequence of service calls with retries and error branches.')
t('dead_letter', 'Add a dead-letter topic',
  'Hold messages that exhausted their delivery attempts for later inspection.')
t('idempotency_key', 'Make the handler idempotent with a deduplication key',
  'Recognise a repeated delivery and skip the duplicate work.')

# --- Security, identity, secrets --------------------------------------------
t('service_account', 'Give the workload its own service account',
  'A dedicated identity whose roles can be granted and revoked independently.')
t('default_sa', 'Let the workload use the default compute service account',
  'The automatically created identity that usually carries broad project access.')
t('workload_identity', 'Bind a Kubernetes service account to a Google service account',
  'Keyless credential issuance for pods through Workload Identity.')
t('wif', 'Federate the external identity with Workload Identity Federation',
  'Exchange an outside token for a short-lived Google credential.')
t('adc', 'Rely on Application Default Credentials',
  'Let the client library find credentials from the environment.')
t('json_key', 'Download a service account key file',
  'A long-lived credential that has to be stored and rotated by hand.')
t('secret_manager', 'Store the credential in Secret Manager',
  'A managed secret store with versioning and access audit.')
t('env_var_secret', 'Set the credential as an environment variable',
  'Inject the value into the process environment at start-up.')
t('mounted_secret', 'Mount the secret as a volume',
  'Present the value as a file that the process reads at runtime.')
t('kms_key', 'Encrypt with a Cloud KMS key',
  'A managed key whose use is authorized by IAM and recorded in audit logs.')
t('cmek', 'Use a customer-managed encryption key',
  'A key the customer owns, rotates and can disable.')
t('rotate_secret', 'Rotate the secret on a schedule',
  'Issue a new version and retire the old one so exposure has a bounded life.')
t('least_privilege', 'Grant only the roles the workload needs',
  'Scope permissions to the actions in use rather than the whole service.')
t('custom_role', 'Define a custom role for the narrow permission set',
  'A role built from an explicit permission list.')
t('basic_role', 'Grant the basic editor role',
  'A legacy broad role that can change most resources in the project.')
t('iap', 'Put Identity-Aware Proxy in front of the service',
  'Authenticate and authorize users before a request reaches the application.')
t('identity_platform', 'Use Identity Platform for end-user sign-in',
  'A managed identity service for customer accounts and tokens.')
t('network_policy', 'Apply a Kubernetes NetworkPolicy',
  'Restrict which pods may talk to which pods inside the cluster.')
t('service_mesh', 'Use Cloud Service Mesh for service-to-service traffic',
  'Mutual TLS, retries and traffic policy applied without changing application code.')
t('direct_vpc_egress', 'Send traffic through Direct VPC egress',
  'Give Cloud Run or functions a private path into the VPC.')
t('psc', 'Reach the service through Private Service Connect',
  'A private endpoint that consumes a published service without peering.')
t('binary_authorization', 'Enforce admission with Binary Authorization',
  'Only images that satisfy the attestation policy may be deployed.')
t('artifact_analysis', 'Scan the image with Artifact Analysis',
  'Report known vulnerabilities in the image layers and packages.')
t('scc', 'Review the finding in Security Command Center',
  'Aggregate and triage security findings across the project.')
t('iap_jwt', 'Validate the signed JWT from the proxy',
  'Check the assertion the proxy adds so only proxied requests are trusted.')

# --- Build, source, and testing --------------------------------------------
t('cloud_build', 'Build the image with Cloud Build',
  'A managed build service that runs the steps from a build configuration file.')
t('artifact_registry', 'Push the image to Artifact Registry',
  'A managed registry with IAM-scoped repositories per environment.')
t('container_registry', 'Push the image to Container Registry',
  'The older registry whose access model is project-wide Cloud Storage.')
t('cloud_build_trigger', 'Trigger the build from a repository push',
  'Start the pipeline when the branch changes rather than by hand.')
t('build_provenance', 'Generate build provenance in Cloud Build',
  'A signed record of what was built and from which source.')
t('slsa_level', 'Require a higher supply-chain level before release',
  'Demand a stronger provenance guarantee as a gate on the pipeline.')
t('cloud_code', 'Develop with Cloud Code in the IDE',
  'Editor integration for scaffolding, running and debugging on Google Cloud.')
t('cloud_shell', 'Use Cloud Shell for the session',
  'A browser terminal with the SDK and tooling already installed.')
t('cloud_workstations', 'Use Cloud Workstations for the environment',
  'A managed, container-defined development environment behind a private endpoint.')
t('skaffold', 'Iterate with Skaffold',
  'A loop that rebuilds and redeploys automatically on a source change.')
t('emulator', 'Run the service emulator locally',
  'A local stand-in for a managed service used for unit and integration work.')
t('gemini_assist', 'Ask Gemini Cloud Assist for a diagnosis',
  'An assistant that reads telemetry and proposes a cause and a next step.')
t('ai_coding_assistant', 'Use an AI coding assistant to draft the tests',
  'Generate a first draft from context, then review and correct it.')
t('mcp_server', 'Connect the assistant to an MCP server',
  'Give the assistant a defined tool surface instead of pasting context by hand.')
t('unit_test', 'Add a unit test with dependencies stubbed',
  'Exercise one unit in isolation with its collaborators replaced.')
t('integration_test', 'Run an integration test against the emulator',
  'Exercise the wire-up between components before deploying.')
t('build_test_step', 'Run the tests as a Cloud Build step',
  'Fail the pipeline at the test stage instead of after deployment.')
t('test_gate', 'Block the deploy on the test result',
  'Make a passing test suite a precondition for release.')
t('flaky_quarantine', 'Quarantine the flaky test and fix it',
  'Keep the suite trustworthy while the unstable test is repaired.')
t('load_test', 'Load-test the release before the rollout',
  'Measure behaviour under expected peak traffic rather than guessing.')

# --- Deployment specifics ---------------------------------------------------
t('deploy_from_source', 'Deploy from source and let the platform build it',
  'Hand the source to the managed builder instead of shipping an image.')
t('deploy_image', 'Deploy a pinned image digest',
  'Release exactly the artifact that was tested rather than a moving tag.')
t('cloud_run_invoker', 'Grant the invoker role to the calling identity',
  'Control who may call the service with IAM rather than a shared token.')
t('allow_unauthenticated', 'Allow unauthenticated invocations',
  'Let anyone reach the endpoint, which is only appropriate for public content.')
t('ingress_internal', 'Restrict ingress to internal traffic',
  'Accept only traffic from the VPC and internal load balancers.')
t('startup_probe', 'Configure a startup probe',
  'Hold traffic until the application is actually ready to serve.')
t('liveness_probe', 'Configure a liveness probe',
  'Restart the container when it can no longer make progress.')
t('readiness_probe', 'Configure a readiness probe',
  'Remove the instance from the endpoint list while it cannot serve.')
t('startup_cpu_boost', 'Raise CPU during start-up only',
  'Speed initialization without paying for the extra CPU afterwards.')
t('hpa_cpu', 'Scale pods on CPU utilization',
  'Add pods when average CPU crosses the target.')
t('hpa_custom', 'Scale pods on a custom or external metric',
  'Add pods on a signal that tracks demand better than CPU.')
t('hpa_min_replicas', 'Set a minimum replica count',
  'Keep capacity warm so scale-up does not cost the first requests.')
t('pdb', 'Add a PodDisruptionBudget',
  'Limit how many pods may be evicted at once during voluntary disruption.')
t('resource_quota', 'Set a namespace resource quota',
  'Bound the total capacity a namespace may consume.')
t('rolling_update', 'Use a rolling update strategy',
  'Replace pods gradually so the deployment stays available.')
t('max_unavailable', 'Tune maxSurge and maxUnavailable',
  'Control how much capacity may be missing while pods are replaced.')
t('node_affinity', 'Constrain pods to the intended node pool',
  'Place work on nodes whose shape and pricing match the workload.')

# --- Data, storage, integration --------------------------------------------
t('cloud_sql_proxy', 'Connect through the Cloud SQL Auth Proxy',
  'A local proxy that authorizes the connection with IAM and encrypts it.')
t('alloydb_proxy', 'Connect through the AlloyDB Auth Proxy',
  'The equivalent authorized connector for AlloyDB instances.')
t('private_ip_db', 'Connect over the database private IP',
  'A private address reachable from the VPC without a proxy process.')
t('connection_pool', 'Pool and reuse database connections',
  'Keep a small set of warm connections instead of opening one per request.')
t('connector_lib', 'Use the language connector with IAM',
  'A client library that resolves and authorizes the instance itself.')
t('firestore_native', 'Use Firestore in Native mode',
  'A document store with real-time listeners and mobile SDKs.')
t('bigtable_row_key', 'Design the row key for the read pattern',
  'Order the key so the query becomes a contiguous range scan.')
t('bigtable_hotspot', 'Hash the leading key component to avoid hotspots',
  'Spread writes so one tablet does not take the whole rate.')
t('spanner', 'Store the ledger in Spanner',
  'A relational database with strongly consistent multi-region transactions.')
t('cloud_storage', 'Store the objects in Cloud Storage',
  'Durable object storage addressed by name rather than a database row.')
t('signed_url', 'Issue a signed URL with a short expiry',
  'A time-limited grant to one object without exposing credentials.')
t('public_bucket', 'Make the bucket public',
  'Serve every object to anyone, which removes the need to authorize at all.')
t('lifecycle_rule', 'Add a lifecycle rule to the bucket',
  'Transition or delete objects by age so retention happens without a job.')
t('retention_lock', 'Lock the bucket retention policy',
  'Make the retention period impossible to shorten, even by an owner.')
t('bigquery_stream', 'Stream the events into BigQuery',
  'Land analytics rows in the warehouse for SQL and ML use.')
t('bigquery_export', 'Export the batch to BigQuery',
  'Load a periodic extract rather than a continuous stream.')
t('pubsub_bigquery_sub', 'Use a BigQuery subscription on the topic',
  'Write topic messages straight into a table without a consumer.')
t('datastore_mode', 'Use Firestore in Datastore mode',
  'Keep the Datastore API and its strong consistency semantics.')
t('cache_invalidation', 'Invalidate the cache on write',
  'Remove or refresh the cached value so readers do not see stale data.')

# --- Observability ----------------------------------------------------------
t('structured_logs', 'Emit structured JSON logs',
  'Emit fields the log viewer can index so queries and alerts are possible.')
t('log_severity', 'Set the correct severity on each entry',
  'Let filters and alerting distinguish routine output from errors.')
t('trace_span', 'Instrument a span around the downstream call',
  'Show where time goes inside a request that crosses services.')
t('trace_id_propagation', 'Propagate the trace ID between services',
  'Join spans from different services into one trace.')
t('custom_metric', 'Emit a custom metric from the code',
  'Publish an application signal that infrastructure metrics cannot see.')
t('error_reporting', 'Send the exception to Error Reporting',
  'Group and count application errors instead of grepping logs.')
t('alert_policy', 'Create an alerting policy on the metric',
  'Notify a human when a threshold is crossed.')
t('slo_alert', 'Alert on the error budget burn rate',
  'Page on the rate at which reliability is being spent.')
t('profiler', 'Profile the service with Cloud Profiler',
  'Find the function consuming CPU or memory under real traffic.')
t('log_based_metric', 'Build a log-based metric',
  'Turn a recurring log pattern into a number that can be charted and alerted on.')
t('debugger', 'Inspect the live process with Cloud Debugger',
  'Read variable state in a running deployment without redeploying.')

# --- Additional authoring options -------------------------------------------
t('deploy_container', 'Package the monolith into a container image',
  'Wrap the existing process in a portable artifact that a managed runtime can execute.')
t('zonal_instance_mistake', 'Place the workload in a single zone',
  'Run in one zone only, so a zone failure stops the service entirely.')

# --- API consumption practices ----------------------------------------------
t('backoff_retry', 'Retry with exponential backoff and jitter',
  'Space out repeated attempts so a throttled quota can recover instead of being hammered.')
t('paginate', 'Follow the page token until results are exhausted',
  'Request each page in turn so a truncated response is completed rather than assumed whole.')
t('restrict_fields', 'Request only the fields the caller needs',
  'Trim the response payload so latency and cost follow actual use.')
t('cache_results', 'Cache the response for its freshness window',
  'Reuse a result that has not changed, avoiding an identical call.')
t('batch_requests', 'Batch many small calls into one request',
  'Reduce per-call overhead when the API supports a batch surface.')
t('public_ip_ssl', 'Expose the database on a public address with enforced SSL',
  'A reachable address that requires encrypted connections from any client.')
t('connection_limit_flag', 'Raise the database connection ceiling by flag',
  'Change the engine-level connection limit without resizing the machine.')

# --- More authoring options -------------------------------------------------
t('manual_build', 'Keep building the image by hand',
  'Run the build steps locally and push the result when someone remembers.')
