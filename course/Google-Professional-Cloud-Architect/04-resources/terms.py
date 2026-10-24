"""Option bank for the Professional Cloud Architect practice course.

One label and one meaning per answer or distractor. Keys are stable and
referenced by questions/*.txt; build.py rejects an unknown key.
"""
TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term: {key}')
    TERMS[key] = (label, meaning)


# ------------------------------------------------------------- compute platforms
t('gke_autopilot', 'Use GKE Autopilot',
  'Autopilot manages nodes, scaling, and patching, so the team owns only the workloads.')
t('gke_standard', 'Use GKE Standard with a node pool per workload shape',
  'Standard exposes node configuration and patching, which the team must then run itself.')
t('gke_regional', 'Create a regional GKE cluster',
  'A regional cluster replicates the control plane across zones, so a zone loss does not stop scheduling.')
t('gke_zonal', 'Create a zonal GKE cluster',
  'A zonal cluster keeps its control plane in one zone, so that zone loss takes the cluster with it.')
t('gke_nap', 'Enable node auto-provisioning',
  'Auto-provisioning adds node pools on demand for pending pods instead of pre-sizing them.')
t('gke_workload_identity', 'Enable Workload Identity Federation for GKE',
  'The feature binds a Kubernetes service account to an IAM service account, so pods hold no keys.')
t('gke_private_nodes', 'Create private nodes with no external IP addresses',
  'Private nodes reach Google APIs through Private Google Access and cannot be addressed from the internet.')
t('gke_release_channel', 'Pin a release channel and a maintenance window',
  'The channel bounds the version drift and the window bounds when automatic upgrades may run.')
t('gke_netpol', 'Enable network policy enforcement',
  'Network policy restricts pod-to-pod traffic inside the cluster, which a firewall rule cannot see.')
t('gke_binauth', 'Enforce Binary Authorization at admission',
  'The admission controller rejects images without a valid attestation, so an unverified build cannot start.')
t('gke_fleet', 'Register the clusters in a fleet',
  'A fleet gives one policy and identity plane across clusters without merging their networks.')
t('cloudrun', 'Deploy the service on Cloud Run',
  'Cloud Run runs a stateless container per request and scales to zero when idle.')
t('cloudrun_min', 'Set a minimum instance count on the Cloud Run service',
  'Keeping warm instances removes cold starts at the cost of paying for idle capacity.')
t('cloudrun_concurrency', 'Raise the request concurrency setting',
  'Concurrency packs more simultaneous requests into each instance before another is started.')
t('cloudrun_gpu', 'Deploy the workload on Cloud Run with a GPU',
  'Serverless GPU attachment suits bursty inference where a reserved node would idle.')
t('cloud_functions', 'Use Cloud Run functions',
  'Functions bind one small handler to an event source and are the lightest way to react to one.')
t('gce_mig', 'Use a managed instance group with autoscaling',
  'The group replaces unhealthy instances and adds capacity from a template as load rises.')
t('gce_spot', 'Run the batch tier on Spot VMs',
  'Spot capacity costs far less but can be reclaimed with 30 seconds of notice.')
t('gce_cud', 'Buy committed use discounts for the steady baseline',
  'A one- or three-year commitment discounts the capacity that runs constantly, not the peaks.')
t('gce_custom', 'Use a custom machine type sized to the workload',
  'Custom vCPU and memory avoid paying for a fixed shape that over-provisions one dimension.')
t('gce_sole_tenant', 'Use sole-tenant nodes',
  'Sole tenancy keeps the physical host dedicated, which matters for licensing or isolation rules.')
t('gce_os_patch', 'Use VM Manager for OS patch compliance',
  'VM Manager inventories and applies OS patches across a fleet instead of relying on manual runs.')
t('batch', 'Submit the work as a Batch job',
  'Batch schedules containerised jobs onto managed or existing capacity and retires it when done.')
t('gcve', 'Run the legacy stack on Google Cloud VMware Engine',
  'VMware Engine keeps the existing hypervisor and operations model while moving the hardware into Google Cloud.')
t('app_engine_flex', 'Deploy on App Engine flexible environment',
  'The flexible environment runs a custom runtime on managed VMs but does not scale to zero.')

# ------------------------------------------------------------- storage
t('gcs_standard', 'Store the objects in Standard storage class',
  'Standard is for data read frequently and has no retrieval fee.')
t('gcs_nearline', 'Store the objects in Nearline storage class',
  'Nearline suits data read about once a month and charges for early deletion.')
t('gcs_coldline', 'Store the objects in Coldline storage class',
  'Coldline suits data read about once a quarter and has a higher retrieval cost.')
t('gcs_archive', 'Store the objects in Archive storage class',
  'Archive is cheapest to hold and slowest and most expensive to retrieve.')
t('gcs_autoclass', 'Enable Autoclass on the bucket',
  'Autoclass moves each object between classes as its access pattern changes, with no lifecycle rules to maintain.')
t('gcs_lifecycle', 'Add a lifecycle rule that transitions and then deletes',
  'A lifecycle rule acts on object age or class, so retention stops depending on a person.')
t('gcs_retention', 'Apply a bucket retention policy with a locked period',
  'A locked retention policy prevents deletion or shortening, which is what an auditor tests.')
t('gcs_versioning', 'Enable object versioning',
  'Versioning keeps a noncurrent copy when an object is overwritten or deleted.')
t('gcs_dual_region', 'Use a dual-region bucket',
  'A dual-region bucket keeps two replicas in a chosen pair of regions and survives one region loss.')
t('gcs_multi_region', 'Use a multi-region bucket',
  'A multi-region bucket spreads replicas across a continent for reads and regional failure.')
t('gcs_cache', 'Attach a Rapid Cache or Anywhere Cache to the bucket',
  'The cache keeps hot objects close to the compute that reads them, cutting repeated egress and latency.')
t('gcs_signed_url', 'Issue a short-lived signed URL',
  'A signed URL grants one object for a fixed time without exposing credentials or making the bucket public.')
t('sts', 'Use Storage Transfer Service for the recurring copy',
  'The service runs scheduled, filtered transfers from another cloud or an HTTP source.')
t('transfer_appliance', 'Use a Transfer Appliance for the one-off bulk move',
  'The appliance ships the data physically when the network would take months to carry it.')
t('filestore', 'Mount a Filestore instance for the shared file path',
  'Filestore provides a managed NFS export that many clients can mount at once.')
t('netapp', 'Use Google Cloud NetApp Volumes',
  'NetApp Volumes offers NFS and SMB with enterprise features such as snapshots and snapmirror.')
t('pd_ssd', 'Attach a Hyperdisk or SSD persistent disk',
  'A persistent disk gives block storage that follows the VM and supports snapshots.')
t('local_ssd', 'Use local SSD for the scratch space',
  'Local SSD is the fastest ephemeral option and loses its data when the VM stops.')

# ------------------------------------------------------------- databases and analytics
t('bigquery', 'Load the data into BigQuery',
  'BigQuery is serverless, columnar, and separates storage from compute, so a scan pays for the bytes read.')
t('bigquery_bi_engine', 'Reserve BigQuery BI Engine capacity',
  'BI Engine holds a working set in memory so dashboards answer without scanning the table each time.')
t('bigquery_slots', 'Buy BigQuery slot commitments with autoscaling',
  'Slots are the unit of compute, and autoscaling adds them only while queries queue.')
t('bigquery_ondemand', 'Leave the project on on-demand pricing',
  'On-demand bills per byte scanned, which is cheap for sparse use and unpredictable at scale.')
t('bigquery_partition', 'Partition the table on the date column',
  'Partitioning limits a query to the date ranges it names, so it scans less.')
t('bigquery_cluster', 'Cluster the table on the filter columns',
  'Clustering sorts within partitions so a filtered query reads fewer blocks.')
t('bigquery_matview', 'Create a materialized view for the repeated aggregate',
  'The view stores the aggregate result and refreshes incrementally as base data arrives.')
t('bigquery_storage_write', 'Write through the Storage Write API',
  'The Storage Write API gives exactly-once semantics and higher throughput than the legacy insert call.')
t('bigquery_insertall', 'Stream rows with the legacy insertAll call',
  'InsertAll is best-effort and only deduplicates on a provided insert ID, so duplicates can land.')
t('bigquery_external', 'Query the files as an external table',
  'An external table reads the files in place, so governance depends on the underlying bucket.')
t('bigquery_biglake', 'Create a BigLake table over the Cloud Storage files',
  'BigLake adds fine-grained access and row and column controls to data that stays in object storage.')
t('bigquery_omni', 'Use BigQuery Omni for the other cloud',
  'Omni runs BigQuery compute against data held in another cloud without copying it first.')
t('bigquery_dts', 'Use the BigQuery Data Transfer Service',
  'The service runs scheduled loads from SaaS sources and other clouds into BigQuery.')
t('bigquery_row_access', 'Add row-level access policies to the table',
  'Row-level policies filter which rows each principal sees inside BigQuery itself.')
t('bigquery_column_masking', 'Apply column-level data masking policies',
  'The policy replaces the column value for unauthorised principals while leaving the column queryable.')
t('bigquery_authorized_view', 'Expose the data through an authorized view',
  'The view runs with its own identity, so a consumer reads columns without table access.')
t('bigquery_editions', 'Choose the BigQuery edition that matches the workload',
  'The edition sets slot capacity, commitments, and the governance features included.')
t('cloud_sql', 'Use Cloud SQL',
  'Cloud SQL is a managed MySQL, PostgreSQL, or SQL Server instance with a familiar connection model.')
t('cloud_sql_ha', 'Enable Cloud SQL high availability with a standby',
  'A regional standby takes over automatically when the primary zone fails.')
t('cloud_sql_read_replica', 'Add a read replica and route reads to it',
  'A replica offloads read traffic but lags the primary, so it is not a failover target.')
t('spanner', 'Use Spanner',
  'Spanner gives strongly consistent reads and writes across regions with a 99.999% multi-region target.')
t('firestore', 'Use Firestore',
  'Firestore is a document store with real-time listeners and per-document transactions.')
t('bigtable', 'Use Bigtable',
  'Bigtable is a wide-column store for high-throughput key reads and writes at low latency.')
t('bigtable_ssd', 'Use Bigtable SSD nodes',
  'SSD nodes give the lowest read latency for latency-sensitive serving workloads.')
t('alloydb', 'Use AlloyDB for PostgreSQL',
  'AlloyDB is PostgreSQL-compatible with a columnar engine for mixed transactional and analytical work.')
t('memorystore', 'Use Memorystore',
  'Memorystore provides managed Redis or Memcached for sub-millisecond cache lookups.')
t('datastream', 'Use Datastream for change data capture',
  'Datastream reads the source log and streams inserts, updates, and deletes with ordering preserved.')
t('dms', 'Use Database Migration Service',
  'The service moves a database with continuous replication and a short cutover window.')
t('composer', 'Use Managed Service for Apache Airflow',
  'Airflow expresses dependencies between scheduled jobs and retries a failed task without rerunning the rest.')
t('dataflow', 'Use Dataflow',
  'Dataflow runs an Apache Beam pipeline with autoscaling and a single programming model for batch and streaming.')
t('dataflow_streaming', 'Run a streaming Dataflow pipeline with windowing',
  'Streaming mode applies windowing, watermarks, and triggers, and can emit results before the stream ends.')
t('dataflow_prime', 'Enable Dataflow Prime',
  'Prime adds right-fitting and memory-aware autoscaling per step, which suits uneven stages.')
t('dataproc', 'Use a Dataproc cluster',
  'A Dataproc cluster runs open-source Spark and Hadoop with jobs that need a persistent cluster.')
t('dataproc_serverless', 'Use Dataproc Serverless',
  'Serverless Spark runs the batch without cluster sizing or idle cost between jobs.')
t('pubsub', 'Publish events to Pub/Sub',
  'Pub/Sub decouples producers from consumers and holds each message until every subscription acknowledges it.')
t('pubsub_ordering', 'Set an ordering key on the Pub/Sub topic',
  'An ordering key keeps messages with the same key in publish order within a region.')
t('pubsub_exactly_once', 'Use an exactly-once subscription',
  'The subscription redelivers after a failure but suppresses duplicate delivery within the ack deadline window.')
t('pubsub_deadletter', 'Attach a dead-letter topic',
  'The dead-letter topic holds messages that fail repeatedly so the subscription can keep moving.')
t('eventarc', 'Route the event with Eventarc',
  'Eventarc delivers Google Cloud and custom events to Cloud Run, functions, or Workflows.')
t('workflows', 'Orchestrate the steps with Workflows',
  'Workflows chains HTTP calls and service connectors with retries and without a running server.')
t('cloud_scheduler', 'Trigger the job with Cloud Scheduler',
  'Scheduler fires a job on a cron or App Engine schedule and retries on failure.')
t('cloud_tasks', 'Queue the work in Cloud Tasks',
  'Tasks dispatches HTTP or App Engine requests with rate limits and per-queue retry policy.')
t('dataplex', 'Govern the estate with Dataplex',
  'Dataplex catalogs, profiles, and applies policy across lake, warehouse, and files in one control plane.')
t('looker', 'Model the metrics in Looker',
  'Looker keeps one governed semantic definition so every dashboard computes the metric the same way.')
t('looker_studio', 'Build the dashboard in Looker Studio',
  'Looker Studio renders the visualisation but inherits whatever query and permissions sit beneath it.')

# ------------------------------------------------------------- networking
t('shared_vpc', 'Use Shared VPC with host and service projects',
  'One host project owns the subnets and firewall rules while each team keeps its own service project.')
t('vpc_peering', 'Peer the two VPC networks',
  'Peering joins two networks at layer three but does not share firewalls or transitive routes.')
t('ncc', 'Build a Network Connectivity Center hub',
  'The hub gives transitive routing between spokes, which peering alone cannot provide.')
t('ha_vpn', 'Use HA VPN with two tunnels',
  'Two tunnels across two interfaces survive one path failing, and the SLA depends on that.')
t('dedicated_interconnect', 'Order a Dedicated Interconnect',
  'A dedicated circuit gives predictable bandwidth and a private path at a colocation facility.')
t('partner_interconnect', 'Order Partner Interconnect',
  'A partner circuit reaches Google Cloud through a provider when the site is not in a colocation facility.')
t('interconnect_attachment', 'Add a VLAN attachment with a Cloud Router',
  'The attachment terminates the circuit, and the router exchanges routes with the on-premises network.')
t('psc', 'Publish the service through Private Service Connect',
  'A PSC endpoint gives a private IP in the consumer VPC without peering or exposing the service publicly.')
t('cloud_nat', 'Deploy Cloud NAT for outbound traffic',
  'Cloud NAT lets private instances reach the internet without an external address.')
t('pga', 'Enable Private Google Access on the subnet',
  'Private Google Access reaches Google APIs from an internal address without a proxy or a NAT gateway.')
t('global_lb', 'Use a global external Application Load Balancer',
  'The global load balancer terminates TLS at the edge and routes to the nearest healthy backend.')
t('internal_lb', 'Use an internal passthrough load balancer',
  'An internal load balancer distributes traffic inside the VPC without exposing it to the internet.')
t('traffic_director', 'Add global load balancing with failover',
  'Health-checked failover moves traffic to the surviving region instead of waiting for DNS to expire.')
t('cloud_armor', 'Attach a Cloud Armor security policy',
  'Cloud Armor filters requests at the edge with allow and deny rules and adaptive protection.')
t('cloud_cdn', 'Enable Cloud CDN on the backend',
  'CDN caches responses at edge locations, which cuts origin load and latency for repeat reads.')
t('cloud_dns', 'Manage the zone in Cloud DNS',
  'Cloud DNS serves the records with anycast resolution and health-checked routing policies.')
t('dns_peering', 'Create a DNS peering zone',
  'DNS peering resolves names across networks without transferring zone ownership.')
t('serverless_vpc', 'Attach a Serverless VPC Access connector',
  'The connector gives serverless workloads a route to internal addresses in the VPC.')
t('hierarchical_firewall', 'Apply a hierarchical firewall policy at the organization or folder',
  'A policy above the project applies to every current and future network beneath it.')
t('vpc_flow_logs', 'Enable VPC Flow Logs on the subnet',
  'Flow logs record which addresses talked to which, which a firewall rule alone cannot show.')
t('private_service_access', 'Allocate private services access for the peered services',
  'The allocated range lets managed services such as Cloud SQL use internal addresses in your network.')

# ------------------------------------------------------------- identity and access
t('iam_predefined', 'Grant a predefined role at the narrowest resource',
  'A predefined role grants the curated permission set for one job at the level it is bound to.')
t('iam_custom', 'Define a custom role with only the required permissions',
  'A custom role expresses least privilege when no predefined role matches the job exactly.')
t('iam_conditional', 'Add an IAM condition on the binding',
  'A condition narrows when a grant applies, for example to a time window or a resource prefix.')
t('iam_deny', 'Apply an IAM deny policy',
  'A deny policy overrides every allow beneath it, which is how an exception is made impossible.')
t('sa_per_service', 'Give each service its own service account',
  'A per-service identity keeps the blast radius of a leaked credential to one workload.')
t('sa_impersonation', 'Grant service account impersonation instead of a key',
  'Impersonation issues short-lived credentials and records who used the identity.')
t('sa_key', 'Create a service account key file for the pipeline',
  'A key file is a long-lived credential that works until it is noticed and revoked.')
t('wif', 'Use Workload Identity Federation for the external pipeline',
  'Federation exchanges an external token for short-lived Google Cloud credentials, so no key leaves the provider.')
t('org_policy', 'Enforce the control with an organization policy constraint',
  'An organization policy blocks the action across every project regardless of who holds the role.')
t('folder', 'Create a folder per environment and bind roles there',
  'A folder binding inherits to every project beneath it, so new projects start with the right access.')
t('project', 'Create a separate project per environment',
  'A project is the boundary for quota, billing, and most IAM inheritance.')
t('labels', 'Tag the resources with labels for cost reporting',
  'Labels attribute spend in billing export; they do not grant or restrict access.')
t('kms_cmek', 'Encrypt with a customer-managed key in Cloud KMS',
  'CMEK lets you control the key lifecycle, rotation, and the ability to revoke access to the data.')
t('kms_csek', 'Supply a customer-supplied encryption key',
  'CSEK is held by the caller and never stored by Google, so losing it loses the object.')
t('kms_rotation', 'Set an automatic rotation period on the key',
  'Rotation issues a new key version on schedule and keeps old versions for decryption.')
t('kms_regional', 'Create the key ring in the same region as the data',
  'A regional key cannot encrypt a resource in another region, which is why residency drives key placement.')
t('cloud_hsm', 'Use Cloud HSM for the key',
  'Cloud HSM keeps the key material in a hardware module that meets FIPS 140-2 level 3.')
t('secret_manager', 'Store the credential in Secret Manager',
  'Secret Manager versions the secret, controls access by IAM, and can rotate it.')
t('secret_env', 'Put the credential in an environment variable on the instance',
  'An environment variable is visible to anything that can read the instance metadata or the process list.')

# ------------------------------------------------------------- access, perimeter, supply chain
t('iap', 'Put Identity-Aware Proxy in front of the application',
  'IAP authenticates and authorises each request before it reaches the backend, with no VPN.')
t('cep', 'Use Chrome Enterprise Premium for the workforce',
  'Context-aware access evaluates device and identity signals for every application, not just the network.')
t('os_login', 'Use OS Login for administrative SSH',
  'OS Login ties the SSH identity to the IAM account and records the session.')
t('bastion', 'Run a bastion host with a public address',
  'A bastion is still an internet-facing host that must be patched and watched.')
t('vpc_sc', 'Put the projects inside a VPC Service Controls perimeter',
  'The perimeter blocks data movement out of the services it covers even for a principal with the role.')
t('vpc_sc_dry', 'Run the perimeter in dry-run mode first',
  'Dry run logs the requests that would be blocked without breaking a legitimate flow.')
t('access_context', 'Require an access level in the perimeter',
  'The access level adds device and network conditions to the perimeter rule.')
t('binary_authorization', 'Require Binary Authorization attestations',
  'Only images with a valid attestation from a trusted builder may deploy.')
t('artifact_registry', 'Store the images in Artifact Registry',
  'Artifact Registry holds the image with IAM-scoped access and vulnerability metadata.')
t('artifact_analysis', 'Enable Artifact Analysis scanning on the repository',
  'Scanning reports known vulnerabilities in the image layers before deployment.')
t('slsa_provenance', 'Record build provenance for the artifact',
  'Provenance states what built the artifact from which source, which is the evidence a supply-chain audit asks for.')
t('model_armor', 'Screen prompts and responses with Model Armor',
  'Model Armor detects prompt injection, jailbreak attempts, and unsafe content before and after the model call.')
t('dlp', 'De-identify the data with Sensitive Data Protection',
  'Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts sensitive fields.')
t('scc', 'Turn on Security Command Center findings',
  'Security Command Center aggregates misconfiguration and threat findings across the organization.')
t('audit_admin', 'Rely on Admin Activity audit logs',
  'Admin Activity records configuration changes and cannot be disabled.')
t('audit_data', 'Enable Data Access audit logs',
  'Data Access logging is off by default and must be enabled per service before reads and writes are recorded.')
t('log_sink', 'Route the logs with an aggregated sink',
  'An aggregated sink collects logs from every project in the organization into one destination.')
t('log_bucket_lock', 'Use a locked log bucket with a fixed retention',
  'A locked bucket prevents deletion and retention changes for the period the auditor requires.')
t('access_transparency', 'Review Access Transparency logs',
  'Access Transparency records when Google staff access your content, which is evidence of oversight, not of user activity.')

# ------------------------------------------------------------- AI and ML
t('gemini_vertex', 'Call Gemini through Agent Platform',
  'The managed endpoint adds IAM, audit logging, regional processing, and data-use terms that a public endpoint does not.')
t('model_garden', 'Select the model from Model Garden',
  'Model Garden lists first-party and open models with deployment options and licensing.')
t('agent_builder', 'Build the assistant with Agent Builder',
  'Agent Builder supplies grounding, retrieval, and tool calling without a bespoke orchestration layer.')
t('agent_platform_pipelines', 'Orchestrate the workflow in Agent Platform Pipelines',
  'Pipelines runs each step as a container with lineage and caching, so the run is reproducible.')
t('feature_store', 'Serve features from Agent Platform Feature Store',
  'Feature Store keeps one definition for training and serving, which prevents training-serving skew.')
t('vertex_endpoint', 'Deploy to an online prediction endpoint',
  'An endpoint keeps capacity ready for low-latency per-request predictions.')
t('vertex_batch', 'Run batch prediction',
  'Batch prediction reads a file and writes predictions without holding serving capacity.')
t('vertex_monitoring', 'Enable model monitoring on the endpoint',
  'Monitoring compares live traffic against the training baseline and reports skew and drift.')
t('ai_hypercomputer', 'Size the training on AI Hypercomputer with TPUs',
  'AI Hypercomputer pairs accelerators with a scheduling stack tuned for large distributed training.')
t('gemini_enterprise', 'Use Gemini Enterprise for the knowledge assistant',
  'Gemini Enterprise adds enterprise search, agents, and governance over the connected corpus.')
t('search_api', 'Index the corpus with Vertex AI Search',
  'Vertex AI Search returns grounded, cited results over private documents without a custom index.')
t('vision_api', 'Use the Vision API for the images',
  'The prebuilt Vision model labels, detects, and reads text without training a model.')
t('speech_api', 'Use the Speech-to-Text API',
  'The prebuilt speech model transcribes audio including domain phrases through adaptation.')
t('translation_api', 'Use the Translation API',
  'The translation model handles 100 or more languages without custom training.')
t('document_ai', 'Use Document AI with a specialised processor',
  'A Document AI processor extracts structured fields from forms and invoices with layout awareness.')
t('gemini_cloud_assist', 'Use Gemini Cloud Assist for the investigation',
  'Cloud Assist explains configurations and proposes changes inside the console with your permissions.')
t('adk', 'Build the agent with the Agent Development Kit',
  'The kit gives code-first control over tools and state when a low-code builder is not enough.')

# ------------------------------------------------------------- operations
t('cloud_monitoring', 'Define dashboards and metrics in Cloud Monitoring',
  'Monitoring collects the platform and application metrics that the first alert will use.')
t('cloud_logging', 'Query the entries in Cloud Logging',
  'Logging holds the event text and structured fields that explain what happened at a moment.')
t('cloud_trace', 'Inspect the trace waterfall in Cloud Trace',
  'Trace shows how one request spent its time across services and calls.')
t('cloud_profiler', 'Attach Cloud Profiler to the service',
  'Profiler samples the running code and attributes CPU and heap to the functions responsible.')
t('error_reporting', 'Group the exceptions in Error Reporting',
  'Error Reporting clusters recurring stack traces so a new failure is not lost in the log volume.')
t('ops_agent', 'Install the Ops Agent on the instances',
  'The Ops Agent ships host metrics and application logs to Cloud Monitoring and Logging.')
t('uptime_check', 'Add an uptime check from several regions',
  'The check measures availability from outside, which no internal metric can prove.')
t('slo', 'Define an SLO with an error budget',
  'An SLO ties the alert to the promise the users care about rather than to a raw resource threshold.')
t('log_metric', 'Create a log-based metric',
  'The metric turns a log pattern into a series that can be alerted on and charted.')
t('alerting_policy', 'Create an alerting policy on the metric',
  'The policy fires when the series crosses the condition for the stated duration.')
t('dashboard', 'Publish a shared dashboard',
  'The dashboard gives the team one view of the same signals during an incident.')
t('cloud_build', 'Run the build in Cloud Build',
  'Cloud Build executes the pipeline steps in a managed, isolated worker with recorded provenance.')
t('cloud_build_pool', 'Use a private Cloud Build pool',
  'A private pool keeps build traffic on your network so it can reach internal package mirrors.')
t('terraform', 'Manage the resources with Terraform',
  'Terraform holds desired state in code, plans the diff, and applies it through a provider.')
t('config_connector', 'Manage the resources with Config Connector',
  'Config Connector reconciles Google Cloud resources from Kubernetes manifests alongside the workloads.')
t('deployment_manager', 'Use Deployment Manager templates',
  'Deployment Manager is the native but older templating service with no plan step.')
t('cloud_shell', 'Use Cloud Shell for the one-off task',
  'Cloud Shell provides an authenticated terminal and editor with no local installation.')
t('cloud_code', 'Use Cloud Code in the IDE',
  'Cloud Code gives the editor run, debug, and deploy targets for the cluster without leaving it.')
t('gcloud', 'Automate the step with the gcloud CLI',
  'The CLI exposes every API as a command that can be scripted and logged.')
t('bq_cli', 'Use the bq command-line tool',
  'The bq tool runs jobs and manages datasets from a terminal or a script.')
t('gsutil', 'Use gcloud storage commands',
  'The storage commands copy and sync objects with resumable, parallel transfers.')
t('emulator', 'Run the emulator in the pipeline',
  'The emulator provides a local endpoint for tests without a billable cloud resource.')
t('client_library', 'Use the Google API client library with retries',
  'The client library applies the recommended retry and backoff behaviour for the API.')
t('api_key', 'Authenticate the call with an API key',
  'An API key identifies a project and does not authorise a user, so it cannot express least privilege.')
t('impersonation_curl', 'Impersonate a service account for a curl test',
  'Impersonation issues a short-lived token so the test runs as the real workload identity.')

# ------------------------------------------------------------- delivery and releases
t('blue_green', 'Deploy blue/green with a traffic switch',
  'Two identical environments let the switch be reversed instantly if the new one misbehaves.')
t('canary', 'Roll out a canary to a small share of traffic',
  'A canary limits the blast radius while the error and latency signals are compared.')
t('rolling', 'Roll the change out instance by instance',
  'A rolling replacement keeps capacity but exposes the whole fleet before the signal is trusted.')
t('feature_flag', 'Put the change behind a feature flag',
  'The flag separates deployment from release, so the code can ship dark and be turned off instantly.')
t('rollback_digest', 'Keep the previous image digest ready for rollback',
  'A pinned digest restores the exact artifact that was known good, not a rebuild of it.')
t('trunk_based', 'Adopt trunk-based development with short-lived branches',
  'Short branches reduce merge conflict and keep the mainline deployable.')
t('pr_gate', 'Require a reviewed pull request and a passing plan',
  'The gate makes a second person check the change and its plan before it can apply.')
t('artifact_promotion', 'Promote the same tested artifact between environments',
  'Promotion moves one immutable artifact forward, so what was tested is what runs.')
t('env_branch', 'Rebuild the artifact separately for each environment',
  'A rebuild produces a different artifact, so the test result no longer applies to production.')
t('test_pyramid', 'Cover the change with unit, integration, and a few end-to-end tests',
  'The pyramid puts volume where it is cheap and keeps end-to-end tests for the critical paths.')
t('load_test', 'Run a load test at the expected peak',
  'The load test measures the system at the concurrency the business expects, before launch.')
t('chaos', 'Run a chaos experiment against a zone',
  'The experiment proves the failover path works while the impact is controlled.')
t('pen_test', 'Commission a penetration test',
  'An independent test attempts the attack the design claims to prevent.')
t('contract_test', 'Add a contract test on the API',
  'The contract test fails the build when a breaking change reaches a consumer.')

# ------------------------------------------------------------- continuity and cost
t('pilot_light', 'Run a pilot-light standby',
  'Only the core data and configuration stay warm, so recovery starts the compute and takes minutes.')
t('warm_standby', 'Run a warm standby at reduced capacity',
  'A running but smaller copy recovers in a short window at a continuous cost.')
t('active_active', 'Run active-active across two regions',
  'Both regions serve traffic, so a regional loss is absorbed without a failover decision.')
t('backup_restore', 'Use backup and restore',
  'Restoring from backup is the cheapest option and the slowest to recover.')
t('backup_dr', 'Use the Backup and DR Service',
  'The service takes application-consistent backups of VMs and databases on a schedule you define.')
t('rpo_rto', 'Set the RPO and RTO with the business owner',
  'The targets come from the business impact of data loss and downtime, not from the technology.')
t('multi_region_data', 'Replicate the data to the second region',
  'The data must exist in the second region before any compute there can serve it.')
t('recommender', 'Act on the Recommender suggestions',
  'Recommender reports idle and over-provisioned resources with the estimated saving.')
t('billing_export', 'Export billing to BigQuery and review it per label',
  'The export attributes cost to the team and service that caused it.')
t('budgets', 'Set a budget with alert thresholds',
  'A budget alerts on spend but does not stop it.')
t('active_assist', 'Share the cost view with the engineering teams',
  'Showing owners their own spend changes behaviour more reliably than a central report.')
t('e2_machine', 'Move the steady services to E2 machine types',
  'E2 shapes trade peak performance for a lower price on workloads that do not need it.')
t('autoscale_down', 'Scale the batch tier to zero between runs',
  'Idle capacity is the largest avoidable cost in a bursty workload.')
t('quota_review', 'Raise the quota before the peak',
  'A quota limit is a hard ceiling that no autoscaler can exceed.')

# ------------------------------------------------------------- migration and support
t('migration_center', 'Assess the estate in Migration Center',
  'Migration Center inventories the servers and estimates the target size and cost.')
t('migrate_containers', 'Convert the VMs with Migrate to Containers',
  'The tool rewrites a VM workload into a container image so it can run on GKE.')
t('storage_transfer', 'Copy the files with Storage Transfer Service',
  'The service moves object data between buckets or clouds on a schedule.')
t('database_migration', 'Migrate the database with Database Migration Service',
  'The service replicates continuously and cuts over in a short window.')
t('apigee', 'Publish the API through Apigee',
  'Apigee adds quotas, keys, mediation, and analytics at the gateway.')
t('api_gateway', 'Use API Gateway',
  'API Gateway fronts a Cloud Run or functions backend with a managed OpenAPI definition.')
t('cloud_endpoints', 'Use Cloud Endpoints',
  'Endpoints validates and monitors an API described by an OpenAPI or gRPC spec.')
t('support_tiers', 'Match the support plan to the recovery commitment',
  'The support tier sets the response time and the escalation path the business expects.')
t('oncall', 'Define an on-call rotation with an escalation path',
  'A named rotation turns an alert into a person who is already accountable for it.')
t('runbook', 'Publish a runbook per alert',
  'The runbook records the diagnostic steps so the response does not depend on who is awake.')
t('change_board', 'Route the change through a change advisory board',
  'The board reviews risk and timing for changes that affect regulated or shared systems.')
t('stakeholder_map', 'Agree the decision rights with the stakeholders',
  'Naming who decides each trade-off prevents the design being reopened late.')
t('service_catalog', 'Publish a service catalog entry with an approved template',
  'A catalog entry gives teams a pre-approved, policy-compliant way to request the resource.')
t('postmortem', 'Write a blameless postmortem with actions',
  'The postmortem records cause and follow-up work, which is how the same failure is prevented.')

# ------------------------------------------------------------- programme-level choices
t('kpi_baseline', 'Define the baseline and target as a KPI with an owner',
  'A measured baseline and a named owner make the outcome testable after the migration.')
t('tco_model', 'Build a three-year total cost of ownership model',
  'The model compares run cost, people cost, and exit cost rather than the monthly bill alone.')
t('pilot_run', 'Run a limited pilot with a success criterion agreed in advance',
  'The pilot produces evidence on the real workload before the whole estate commits.')
t('data_residency', 'Keep the data in the region the regulator requires',
  'Residency fixes where storage and processing may happen, which then constrains every service choice.')
t('exit_plan', 'Document the exit plan and data portability',
  'The exit plan keeps the migration reversible and constrains how proprietary the design may become.')
t('risk_register', 'Record the risk and its owner in a risk register',
  'The register keeps the decision visible to the people who carry the consequence.')
t('skill_gap', 'Assess the team skills and plan the training',
  'A design the operating team cannot run becomes an outage with a schedule.')
t('deprecation_policy', 'Publish a versioning and deprecation policy',
  'The policy tells consumers how long a version lives and when it is removed.')
t('sla_contract', 'Put the recovery commitment in the contract',
  'The contract converts an internal target into an obligation with a consequence.')
t('cost_owner', 'Assign a cost owner to each business unit',
  'A named owner per unit is what makes a cost report change behaviour.')
t('budget_alert_team', 'Give each team a budget and an alert on its own spend',
  'A team-level budget fires before the central monthly bill is reconciled.')

# The sequencing bank is merged last so a sequencing item can be authored as
# an ordinary single-answer item whose four options are four candidate orders.
from sequences import SEQUENCES  # noqa: E402

for _key, _value in SEQUENCES.items():
    if _key in TERMS:
        raise ValueError(f'Duplicate term: {_key}')
    TERMS[_key] = _value
