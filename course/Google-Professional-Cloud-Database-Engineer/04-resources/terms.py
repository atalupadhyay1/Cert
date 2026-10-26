"""Option bank for the Professional Cloud Database Engineer practice sets.

Every option label is a product choice or an operational action, so an item can
ask which decision fits the stated constraints without the distractor collapsing
into a definition. Keys are authoring identifiers only and never appear in an
export.
"""

TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f"duplicate option key: {key}")
    TERMS[key] = (label, meaning)


# --- Choosing a database -----------------------------------------------------
t('cloud_sql', 'Use Cloud SQL for the relational workload',
  'A managed MySQL, PostgreSQL, or SQL Server instance with Google-operated backups, patching, and failover.')
t('alloydb', 'Use AlloyDB for the demanding relational workload',
  'A managed PostgreSQL-compatible database with a separate read pool and columnar acceleration for mixed transactional and analytical load.')
t('spanner', 'Use Spanner for the globally distributed relational workload',
  'A horizontally scalable relational database with strong consistency across regions and no manual sharding.')
t('bigtable', 'Use Bigtable for the high-throughput wide-column workload',
  'A wide-column NoSQL service built for very high write and read rates over a sparse, row-key-ordered model.')
t('firestore', 'Use Firestore for the document workload',
  'A document database with automatic multi-region replication, offline client support, and index-driven queries.')
t('memorystore', 'Use Memorystore as the caching tier',
  'A managed Redis-compatible in-memory store placed in front of the system of record.')
t('self_managed', 'Run the database on Compute Engine yourself',
  'A self-managed engine on virtual machines where the team owns patching, backups, and failover.')
t('bare_metal', 'Run the database on bare metal solution',
  'Dedicated hardware for engines that cannot be virtualized or licensed for a managed service.')
t('partner_offering', 'Use a partner-managed database offering',
  'A third-party database operated by its vendor on Google Cloud infrastructure.')
t('keep_current_engine', 'Keep the current engine and version',
  'A lift of the existing engine with no conversion work, retaining its behaviour and licensing.')
t('datastore_mode', 'Use Firestore in Datastore mode',
  'A schemaless mode that keeps the Datastore API and its strong consistency semantics.')

# --- Sizing and capacity ----------------------------------------------------
t('rightsize_from_metrics', 'Size the instance from the observed peak metrics',
  'Choose a shape from measured CPU, memory, and IOPS rather than from a guess.')
t('vertical_scale', 'Increase the machine type of the instance',
  'Move the instance to a larger shape so more vCPU and memory serve the same data.')
t('horizontal_shard', 'Shard the data across several instances',
  'Split rows by a key so each instance owns a subset of the workload.')
t('add_read_replica', 'Add a read replica for the read traffic',
  'Send reads to a copy so the primary keeps its capacity for writes.')
t('read_pool', 'Add nodes to the read pool',
  'Grow the AlloyDB read pool that serves read-only connections.')
t('increase_disk', 'Increase the disk size to raise throughput',
  'Buy more storage so the attached disk also yields more IOPS and throughput.')
t('ssd_storage', 'Move the data to SSD storage',
  'Trade a higher price per gigabyte for lower latency on random reads.')
t('hdd_storage', 'Move the data to HDD storage',
  'Trade latency for a lower price on large, throughput-oriented scans.')
t('add_processing_units', 'Add processing units to the Spanner instance',
  'Raise provisioned compute in 1000-unit node steps or 100-unit increments.')
t('add_bigtable_nodes', 'Add nodes to the Bigtable cluster',
  'Increase the cluster size so more tablet servers absorb the request rate.')
t('enable_autoscaling', 'Enable autoscaling on the instance',
  'Let compute follow a target utilization instead of a fixed size.')
t('reserve_headroom', 'Reserve headroom above the measured peak',
  'Keep spare capacity so a failover or a traffic spike does not saturate the instance.')
t('archive_old_rows', 'Archive closed rows to cheaper storage',
  'Move aged, rarely read rows out of the hot table into Cloud Storage or BigQuery.')

# --- Availability and disaster recovery -------------------------------------
t('regional_ha', 'Enable regional high availability with a standby zone',
  'A primary and standby in two zones of one region with automatic failover.')
t('multi_region_config', 'Choose a multi-region instance configuration',
  'A topology that places replicas in separate regions for regional-failure tolerance.')
t('cross_region_replica', 'Add a cross-region read replica',
  'A copy in a second region that serves reads and can be promoted.')
t('promote_replica', 'Promote the cross-region replica during the outage',
  'Turn the replica into an independent primary so the application can resume writes.')
t('zonal_instance', 'Run a single zonal instance',
  'One instance in one zone with no standby, so a zone failure stops writes.')
t('secondary_cluster', 'Add a secondary cluster in the second region',
  'An AlloyDB cross-region copy that can be promoted to a primary cluster.')
t('multi_cluster_routing', 'Route the app profile across both clusters',
  'A Bigtable app profile that fails over between clusters without a client change.')
t('single_cluster_routing', 'Pin the app profile to one cluster',
  'A Bigtable app profile that keeps a workload on one cluster for predictable latency.')
t('failover_test', 'Run a controlled failover test',
  'Trigger a switchover in a test window and observe how long writes are unavailable.')
t('deny_maintenance', 'Set a deny maintenance period over the peak event',
  'Block maintenance during a period when an interruption is unacceptable.')
t('maintenance_window', 'Schedule the maintenance window in the low-traffic period',
  'Choose the weekly window when patching may interrupt the instance.')
t('multi_zone_replica', 'Place the replica in the same region as the primary',
  'A same-region copy that protects against a zone failure, not a regional one.')
t('restore_second_region', 'Restore the backup into the second region',
  'Rebuild the database in the surviving region from the latest backup.')

# --- Connectivity -----------------------------------------------------------
t('auth_proxy', 'Connect through the Cloud SQL Auth Proxy',
  'A local proxy that adds IAM authorization and TLS without opening a network path.')
t('connector_lib', 'Use the language connector with IAM credentials',
  'A client library that resolves the instance and authorizes the connection with IAM.')
t('private_ip', 'Connect over private IP inside the VPC',
  'A private address reachable only from the VPC and connected networks.')
t('psc_endpoint', 'Publish the instance behind Private Service Connect',
  'A private endpoint in the consumer VPC that reaches the service without peering.')
t('authorized_network', 'Add the client range to authorized networks',
  'A public-IP allowlist that admits the caller range.')
t('public_ip_ssl', 'Use the public IP with enforced SSL',
  'A public address that requires encrypted connections from any client.')
t('iam_db_auth', 'Enable IAM database authentication',
  'Map an IAM principal to a database user so no password is stored.')
t('builtin_password', 'Keep a database password in the connection string',
  'A native database user whose credential must be rotated and stored.')
t('session_pooler', 'Put a session pooler in front of the instance',
  'A pooler that multiplexes many application connections onto few database sessions.')
t('raise_max_connections', 'Raise the max_connections database flag',
  'Increase the database-level connection ceiling on the instance.')
t('increase_tier_for_connections', 'Increase the machine tier to allow more connections',
  'Buy a larger shape because the connection limit scales with memory.')
t('fix_connection_leak', 'Fix the connection leak in the application',
  'Close sessions that the application opens and never returns to the pool.')
t('vpc_sc_perimeter', 'Add the projects to a VPC Service Controls perimeter',
  'A boundary that blocks data exfiltration even from an authorized identity.')
t('shared_vpc', 'Place the instance in a Shared VPC service project',
  'A centrally managed network that lends subnets to the database project.')

# --- Encryption, audit, policy ---------------------------------------------
t('cmek', 'Encrypt with a customer-managed key in Cloud KMS',
  'A key the customer owns and can rotate or revoke.')
t('google_managed_key', 'Rely on Google-managed encryption keys',
  'Default encryption at rest with keys the customer neither sees nor manages.')
t('kms_rotation', 'Rotate the customer-managed key on a schedule',
  'Produce new key versions so an old version stops encrypting new data.')
t('data_access_logs', 'Enable Data Access audit logs',
  'Record reads and writes, which are not captured by default.')
t('admin_activity_logs', 'Rely on Admin Activity audit logs',
  'Record configuration changes only, leaving row-level reads unaudited.')
t('audit_sink', 'Route the audit logs to a locked log bucket',
  'Export entries to storage whose retention cannot be shortened.')
t('org_policy_location', 'Enforce the location with an organization policy',
  'A constraint that keeps database resources inside the approved regions.')
t('data_residency', 'Place the instance in the required region',
  'A location choice that keeps data inside the regulated boundary.')
t('row_level_retention', 'Apply a row-level retention policy',
  'Delete or expire records once the legal hold period ends.')

# --- Monitoring and diagnosis ----------------------------------------------
t('query_insights', 'Use Query Insights to find the heavy statements',
  'A per-query view of latency, load, and wait events on the instance.')
t('index_recommendation', 'Apply the recommended missing index',
  'Act on the advisor output for the statement that dominates latency.')
t('add_index', 'Add the index the slow query needs',
  'Create an index that turns a scan into a lookup for the predicate.')
t('drop_unused_index', 'Drop the unused index',
  'Remove write amplification from an index nothing reads.')
t('read_query_plan', 'Read the query plan for the statement',
  'Inspect the chosen scan and join order before changing anything.')
t('refresh_statistics', 'Refresh the table statistics',
  'Give the planner current cardinality so it stops choosing a poor plan.')
t('lock_inspection', 'Inspect lock waits and blocking sessions',
  'Find the transaction that holds the lock others wait on.')
t('vitals_dashboard', 'Watch CPU, memory, disk, and IOPS together',
  'Read the instance-level signals before attributing the symptom to the query.')
t('alert_policy', 'Create an alerting policy on the metric',
  'A condition that pages a human when the threshold is crossed.')
t('alert_on_error_rate', 'Alert on the database error rate',
  'Page on failed statements rather than on resource saturation alone.')
t('replica_lag_alert', 'Alert on replication lag',
  'Page when the copy falls behind the primary by more than the budget.')
t('log_based_metric', 'Build a log-based metric from the error entries',
  'Turn a recurring log pattern into a metric that can be charted and alerted on.')
t('database_center', 'Review the fleet in Database Center',
  'A single view of health, security, and version posture across database instances.')
t('gemini_explain', 'Ask Gemini in databases to explain the plan',
  'Use the assistant to interpret a query plan and propose a change to test.')
t('slow_query_log', 'Read the slow query log',
  'The engine log of statements that exceeded the long-query threshold.')
t('cache_hot_reads', 'Cache the hot read path in Memorystore',
  'Absorb repeated reads in memory so the database sees fewer of them.')
t('partition_table', 'Partition the large table',
  'Split one table into ranges so pruning and maintenance act on less data.')
t('batch_writes', 'Batch the writes into fewer round trips',
  'Cut per-row network and commit overhead in the application.')
t('increase_work_mem', 'Raise the per-operation memory flag',
  'Give sorts and joins more working memory on the instance.')
t('kill_blocking_session', 'Terminate the session that holds the lock',
  'End the blocking transaction so the queue drains.')

# --- Backup and recovery ----------------------------------------------------
t('automated_backups', 'Enable automated backups with a retention window',
  'Scheduled backups kept for a chosen number of days.')
t('pitr', 'Enable point-in-time recovery',
  'Continuous log capture that lets the instance return to an arbitrary moment.')
t('export_dump', 'Export a logical dump to Cloud Storage',
  'A portable SQL dump taken with the engine tooling.')
t('export_csv', 'Export the table to CSV in Cloud Storage',
  'A flat-file extract for a downstream loader rather than a restore.')
t('on_demand_backup', 'Take an on-demand backup before the change',
  'A manual checkpoint taken immediately before a risky operation.')
t('clone_instance', 'Clone the instance for the test',
  'A copy of the current data created without touching the source.')
t('restore_to_timestamp', 'Restore to the timestamp before the bad change',
  'A point-in-time restore that discards the later writes on the same instance.')
t('extend_backup_retention', 'Extend the backup retention window',
  'Keep backups longer so an older restore point remains available.')
t('spanner_backup', 'Create a Spanner backup',
  'A consistent snapshot of the database held independently of version retention.')
t('extend_version_retention', 'Extend the version retention period',
  'Keep a longer window of Spanner change history for point-in-time reads.')
t('bigtable_backup', 'Create a Bigtable backup',
  'A snapshot of a table that survives a bad schema or data change.')
t('firestore_backup', 'Schedule a Firestore export',
  'A managed export of documents used as the restore point.')
t('bigtable_gc_policy', 'Set the garbage-collection policy on the column family',
  'A rule that drops versions by age or count, which also bounds recovery.')
t('export_lifecycle', 'Add a lifecycle rule to the export bucket',
  'Move or delete aged exports so the bucket does not grow without limit.')
t('rto_rpo_design', 'Design the restore path to the stated RTO and RPO',
  'Choose mechanisms by how much data and time the business can lose.')

# --- Cost and performance ---------------------------------------------------
t('commit_for_baseline', 'Commit to the steady baseline capacity',
  'A one- or three-year commitment that discounts the capacity always in use.')
t('stop_idle_instance', 'Stop or delete the idle instance',
  'Remove capacity that serves no traffic.')
t('autoscale_schedule', 'Scale down outside business hours',
  'Match capacity to the daily traffic shape.')
t('rightsize_down', 'Reduce the machine type to match observed use',
  'Shrink an instance whose peak fits a smaller shape.')
t('sustained_use_discount', 'Rely on sustained-use discounts',
  'The automatic discount that applies to long-running Compute Engine usage.')
t('separate_dev_from_prod', 'Split development workloads onto their own instance',
  'Keep experimentation off the production shape and budget.')
t('reduce_log_volume', 'Cut the log volume the instance emits',
  'Lower ingest cost by dropping or sampling low-value entries.')
t('storage_autogrow', 'Let the disk grow automatically',
  'Avoid a full-disk outage at the cost of unplanned storage growth.')
t('query_cost_review', 'Review the cost of the top queries',
  'Attribute spend to the statements that scan the most data.')
t('observability_sampling', 'Sample the database telemetry',
  'Keep a representative signal at a fraction of the ingest cost.')
t('reserve_capacity', 'Reserve capacity for the peak season',
  'Hold capacity ahead of a known surge rather than waiting for autoscaling.')

# --- Migration --------------------------------------------------------------
t('dms_homogeneous', 'Use Database Migration Service for the same engine',
  'A managed migration that moves a supported engine to the same engine on Google Cloud.')
t('dms_heterogeneous', 'Use Database Migration Service with schema conversion',
  'A managed path that converts schema and code from a different source engine.')
t('conversion_workspace', 'Build the schema in a conversion workspace',
  'Convert DDL and code with reviewable, editable output before the load starts.')
t('datastream_cdc', 'Stream changes with Datastream',
  'Change data capture from the source into a Google Cloud target.')
t('reverse_replication', 'Set up reverse replication to the source',
  'Keep writing back to the original system so a rollback loses nothing.')
t('native_logical_replication', 'Use the engine native logical replication',
  'Replicate row changes from the source using the engine feature itself.')
t('dump_and_restore', 'Dump, restore, then replay the changes',
  'A bulk load followed by a catch-up pass for the writes made during the load.')
t('dual_write', 'Write to both systems from the application',
  'Keep two databases current from application code during the transition.')
t('shadow_read', 'Replay read traffic against the target',
  'Compare the target answers with production before the switch.')
t('reconciliation', 'Reconcile row counts and checksums',
  'Prove the target holds the same rows as the source before cutover.')
t('cutover_runbook', 'Follow a cutover runbook with a rollback step',
  'A rehearsed sequence with a named decision point and a way back.')
t('freeze_writes', 'Freeze writes during the cutover',
  'Stop application writes so the last increment can be applied cleanly.')
t('dns_switch', 'Repoint the connection string at the target',
  'Move clients to the new endpoint as the final cutover action.')
t('extended_outage', 'Accept a scheduled extended outage',
  'Stop the source, load everything, and start the target in one window.')
t('decommission_after_parallel', 'Decommission the source after a parallel period',
  'Keep the old system read-only for a defined period, then remove it.')
t('dlq_conversion', 'Rewrite the stored procedures and DML by hand',
  'Port procedural code the conversion tool flags as unsupported.')
t('sequence_reset', 'Reset the sequences after the bulk load',
  'Set generated-key counters past the highest value so inserts do not collide.')
t('target_engine_choice', 'Choose the target engine with the cheapest conversion',
  'Weigh engine compatibility and code rewrite effort before selecting a destination.')
t('validate_cutover_window', 'Measure the catch-up rate before choosing the window',
  'Size the cutover from how fast changes replay, not from the data volume alone.')

# --- Deployment and operations ---------------------------------------------
t('terraform_module', 'Provision the instance with a Terraform module',
  'Declare the database so the same definition creates every environment.')
t('iac_pipeline', 'Apply the change through the infrastructure pipeline',
  'Send database changes through review and version control like any other code.')
t('manual_provision', 'Provision the instance once by hand',
  'Create the resource interactively with no stored definition.')
t('blue_green_instance', 'Stand up a parallel instance and switch over',
  'Run the new version beside the old one and move traffic when it is proven.')
t('test_on_clone', 'Test the upgrade on a clone first',
  'Rehearse the change against a copy before touching production.')
t('in_place_upgrade', 'Perform an in-place major version upgrade',
  'Change the engine version on the running instance during the window.')
t('rolling_restart', 'Restart the instance in the window',
  'Apply the configuration change with a brief restart.')
t('backup_before_upgrade', 'Take a backup before the upgrade',
  'A recovery point that makes the upgrade reversible in practice.')
t('monitor_post_upgrade', 'Watch the error rate after the change',
  'Compare the signal after cutover against the pre-change baseline.')
t('replica_promotion_drill', 'Rehearse the promotion in a test project',
  'Practise the failover that the runbook would perform for real.')
t('health_check_alert', 'Alert when the instance is unreachable',
  'A liveness signal that fires before users report the outage.')
t('connection_routing_primary', 'Route writes to the primary endpoint',
  'Keep read-write traffic pointed at the instance that accepts writes.')
t('read_split', 'Send reporting queries to the read replica',
  'Separate analytical reads from the write path.')
t('regional_ha_with_replica', 'Combine regional HA with a cross-region replica',
  'Zone tolerance inside the region plus a promotion path for a regional failure.')
t('scale_before_failover', 'Pre-size the promoted replica for the full load',
  'Give the standby enough capacity to carry production alone.')
t('spanner_read_only_region', 'Add a read-only region to the configuration',
  'Serve reads near users without making the region a write leader.')

# --- Data models, features, and integration --------------------------------
t('composite_index', 'Add the composite index for the query',
  'An index ordered so the filter and sort both resolve without a scan.')
t('ttl_policy', 'Set a time-to-live policy on the collection',
  'Expire documents once their usefulness ends.')
t('vector_index', 'Create a vector index for the embeddings',
  'An approximate-nearest-neighbour index over embedding columns.')
t('pgvector_extension', 'Enable the vector extension on PostgreSQL',
  'Store embeddings beside relational rows and search them in the same engine.')
t('alloydb_vector', 'Use AlloyDB vector search with a ScaNN index',
  'A vector index tuned for large embedding sets on AlloyDB.')
t('bigquery_federation', 'Query the source through BigQuery federated queries',
  'Read the operational table from BigQuery without copying it first.')
t('datastream_to_bigquery', 'Stream changes into BigQuery',
  'Keep an analytics copy current by applying change data capture.')
t('export_to_bigquery', 'Export the table into BigQuery',
  'Copy the analytical slice into the warehouse on a schedule.')
t('hybrid_link', 'Keep part of the estate on-premises with a hybrid link',
  'Interconnect the remaining on-premises system rather than moving it.')
t('cache_as_source', 'Make the cache the system of record',
  'Hold the only copy of the data in memory.')
t('denormalize', 'Denormalize the model for the read pattern',
  'Duplicate fields so a hot query avoids joins.')
t('interleave_tables', 'Interleave the child table in the parent',
  'Store child rows near their parent row so reads stay local.')
t('hash_first_key', 'Hash the leading key component',
  'Spread writes across the key space so no range takes all the traffic.')
t('reverse_timestamp_key', 'Reverse the timestamp in the row key',
  'Keep recent writes from landing on one tablet.')
t('change_key_design', 'Change the row-key design',
  'Fix the access pattern that concentrates load on a narrow key range.')
t('hot_tablet_investigate', 'Investigate the overloaded tablet',
  'Find the key range that receives disproportionate traffic.')

# --- Access and identity ----------------------------------------------------
t('predefined_role', 'Grant the predefined database role',
  'A Google-managed role that carries the permissions the operator needs.')
t('custom_role', 'Grant a custom role limited to the needed permissions',
  'A role built from an explicit permission list.')
t('basic_role', 'Grant the basic editor role',
  'A broad legacy role that can change most resources in the project.')
t('per_user_db_account', 'Create one database user per person',
  'Individual accountability at the engine layer rather than a shared login.')
t('shared_app_account', 'Share one application database user',
  'A single credential used by every workload that touches the database.')
t('least_privilege_schema', 'Limit the user to the required schema',
  'Grant access to named objects instead of the whole instance.')
t('group_based_access', 'Bind access to a Google group',
  'Manage membership in a group rather than editing bindings per person.')
t('service_account_app', 'Have the application authenticate as a service account',
  'A workload identity that can be authorized by IAM without a stored password.')

# --- Scheduling, quotas, and service levels ---------------------------------
t('quota_review', 'Request a quota increase for the project',
  'Raise the project-level ceiling so the operation is no longer refused.')
t('retry_backoff', 'Retry the failed operation with exponential backoff',
  'Repeat the call after a growing delay so a transient refusal clears.')
t('schedule_offpeak', 'Move the job outside the contention window',
  'Stagger the work so concurrent operations stop colliding on the same limit.')
t('scheduled_job', 'Run the task on a managed schedule',
  'A recurring trigger that performs the work with nobody present.')
t('slo_tracking', 'Track the availability signal against the agreed objective',
  'Compare observed service levels with the commitment rather than watching raw resource metrics.')
t('apply_cdc_backlog', 'Apply the captured change backlog before cutover',
  'Replay the writes made during the bulk load so the target is current at the switch.')
t('fence_old_primary', 'Fence the old primary before promotion',
  'Stop the former primary from accepting writes so two instances cannot both claim the role.')

# --- Additional authoring options -------------------------------------------
t('load_test', 'Load-test the workload to derive the size',
  'Generate representative traffic and read the resource curve before choosing a shape.')
t('import_dump', 'Import the dump into the target instance',
  'Load a logical dump file into the database through the managed import path.')
t('connection_inventory', 'Confirm no client still uses the old endpoint',
  'Check the connection and traffic evidence before retiring an instance.')
