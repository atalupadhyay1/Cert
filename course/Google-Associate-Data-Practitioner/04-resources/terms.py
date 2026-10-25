"""Option bank for the Associate Data Practitioner practice course.

One label and one meaning per answer or distractor. Keys are stable and
referenced by questions/*.txt; build.py rejects an unknown key.
"""
TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term: {key}')
    TERMS[key] = (label, meaning)


# ------------------------------------------------------- preparation and methodology
t('etl_pipeline', 'Extract, transform outside the warehouse, then load the result',
  'ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows.')
t('elt_pipeline', 'Load the raw rows, then transform them inside the warehouse',
  'ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract.')
t('etlt_pipeline', 'Load into a staging area, apply a light transform, then transform again in the warehouse',
  'ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows.')
t('federated_query', 'Query the source system in place with a federated query',
  'A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load.')
t('staging_table', 'Land the extract in a staging table before any transform runs',
  'A staging table separates a failed load from a failed transform, so each can be retried on its own.')
t('transform_before_export', 'Transform on the source system before the export starts',
  'Transforming on the source loads the source with work and removes the raw evidence from the target.')
t('manual_spreadsheet', 'Combine the extracts in a spreadsheet and upload the result',
  'A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run.')

# ------------------------------------------------------- data quality and cleaning
t('sql_clean', 'Clean the rows with SQL in BigQuery',
  'SQL inside the warehouse removes duplicates, trims values, and casts types where the data already sits.')
t('dataflow_clean', 'Clean the stream with a Dataflow pipeline',
  'A Dataflow pipeline applies the same cleaning logic to streaming and batch records.')
t('fusion_clean', 'Clean and standardise with Cloud Data Fusion',
  'A Data Fusion pipeline expresses the cleanup visually and keeps the steps in one versioned definition.')
t('dataproc_clean', 'Clean the data with Spark on Dataproc',
  'Spark suits large files that need custom code rather than SQL.')
t('quality_rules', 'Define data quality rules and run a quality scan',
  'Declared rules turn a judgement about the data into a test that runs on every load.')
t('row_count_check', 'Compare the row count with the source after every load',
  'A row-count reconciliation catches a truncated or duplicated extract.')
t('null_profile', 'Profile the columns to measure the null rate before loading',
  'A profile quantifies what is missing before the gaps reach a dashboard.')
t('dedupe_key', 'Deduplicate on the business key in the cleaning step',
  'Retries and restatements create duplicate rows unless the load deduplicates on a stable key.')
t('schema_cast', 'Cast the columns to the declared types before the load',
  'An explicit cast turns a silent type drift into a visible failure at load time.')
t('skip_validation', 'Load first and fix the rejected rows afterwards',
  'Loading before validation lets bad rows reach the consumers who read the table.')
t('etag_check', 'Compare the source checksum with the delivered file',
  'A checksum proves the bytes arrived unchanged rather than merely arrived.')

# ------------------------------------------------------- transfer tools
t('storage_transfer_service', 'Use Storage Transfer Service',
  'Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule.')
t('transfer_appliance', 'Order a Transfer Appliance',
  'A Transfer Appliance ships the data physically when the network path would take longer than the deadline.')
t('bq_dts', 'Use BigQuery Data Transfer Service',
  'BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services.')
t('dms', 'Use Database Migration Service',
  'Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner.')
t('datastream_cdc', 'Replicate the changes with Datastream',
  'Datastream captures change data from a source database and streams it without a bulk copy of the whole table.')
t('gcloud_storage_cp', 'Copy the objects with the gcloud storage command',
  'A gcloud storage copy is the direct path for an ad hoc move between buckets.')
t('bq_load', 'Load the files with the bq load command',
  'The bq load command creates a load job that reads files from Cloud Storage into a table.')
t('client_library_load', 'Load the rows with a client library from the application',
  'A client library suits an application that already holds the rows in memory rather than files in a bucket.')
t('bigquery_storage_write', 'Stream the rows with the BigQuery Storage Write API',
  'The Storage Write API commits rows at high rate when a stream, not a file, produces them.')
t('ftp_pull', 'Pull the files from the partner over FTP each night',
  'A hand-built FTP pull has no retry, no manifest, and no record of what arrived.')

# ------------------------------------------------------- formats and structure
t('format_parquet', 'Land the data as Parquet',
  'Parquet is columnar and compressed, so a scan reads only the columns a query needs.')
t('format_avro', 'Land the data as Avro',
  'Avro carries its schema with the records and suits row-oriented streaming exchanges.')
t('format_csv', 'Land the data as CSV',
  'CSV is readable everywhere and carries no types, no schema, and no nesting.')
t('format_json', 'Land the data as newline-delimited JSON',
  'Newline-delimited JSON keeps nested fields and can be appended one record at a time.')
t('format_orc', 'Convert the data to ORC before the load',
  'ORC is another columnar format; choosing it adds a conversion step without a benefit over Parquet here.')
t('format_xml', 'Land the data as XML',
  'XML nests well and is verbose, which makes it a poor fit for wide analytical scans.')
t('structured_data', 'Treat the records as structured data',
  'Structured data fits a declared schema of rows and columns.')
t('semi_structured_data', 'Treat the records as semi-structured data',
  'Semi-structured data has a flexible shape such as JSON, where fields vary between records.')
t('unstructured_data', 'Treat the files as unstructured data',
  'Unstructured data has no field model at all, such as images, audio, or free documents.')
t('schema_on_read', 'Apply a schema on read at query time',
  'A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load.')

# ------------------------------------------------------- storage selection
t('cloud_storage', 'Store the files in Cloud Storage',
  'Cloud Storage holds objects of any shape and is the landing zone every other service can read.')
t('bigquery', 'Store the rows in BigQuery',
  'BigQuery holds columnar tables that a SQL engine can scan at warehouse scale.')
t('cloud_sql', 'Store the records in Cloud SQL',
  'Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema.')
t('firestore', 'Store the documents in Firestore',
  'Firestore is a document store for application reads by key with a flexible shape.')
t('bigtable', 'Store the rows in Bigtable',
  'Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key.')
t('spanner', 'Store the records in Spanner',
  'Spanner gives strongly consistent relational transactions across regions at global scale.')
t('alloydb', 'Store the records in AlloyDB for PostgreSQL',
  'AlloyDB is a managed PostgreSQL option for transaction workloads that want PostgreSQL compatibility.')
t('biglake', 'Query the objects through BigLake tables',
  'BigLake tables extend BigQuery access control and performance to objects that stay in Cloud Storage.')
t('local_disk', 'Keep the dataset on the analyst workstation',
  'A workstation copy has no shared access control, no durability promise, and no audit trail.')

# ------------------------------------------------------- location types
t('loc_regional', 'Choose a regional location',
  'A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base.')
t('loc_dual_region', 'Choose a dual-region location',
  'A dual-region location keeps two copies in a named pair of regions with a defined recovery point.')
t('loc_multi_region', 'Choose a multi-region location',
  'A multi-region location spreads the data across a continent-scale geography for the widest availability.')
t('loc_zonal', 'Choose a zonal resource',
  'A zone is a single failure domain, so a zonal resource does not survive the loss of that zone.')
t('loc_follow_users', 'Place the data in the region nearest the largest user base',
  'Distance between the data and the readers shows up as latency on every query.')
t('loc_residency', 'Place the data in the region the regulator names',
  'A residency obligation fixes the geography, which removes the choice from the performance discussion.')

# ------------------------------------------------------- analysis
t('bq_sql_query', 'Write a SQL query in BigQuery and save the result',
  'A saved SQL query answers a business question and can be scheduled or exported.')
t('bq_view', 'Create a BigQuery view over the join',
  'A view stores the query rather than the rows, so the answer stays current at query time.')
t('bq_materialized_view', 'Create a BigQuery materialized view',
  'A materialized view stores the result and refreshes it, which trades storage for repeat-query speed.')
t('bq_export_sheets', 'Export the query result to a spreadsheet for the business team',
  'An export is a snapshot that goes stale the moment it is written.')
t('colab_enterprise', 'Analyse the data in a Colab Enterprise notebook',
  'Colab Enterprise gives a managed notebook runtime with project IAM and BigQuery access.')
t('notebook_bq_magic', 'Query BigQuery from the notebook with the %%bigquery magic',
  'The magic returns a DataFrame from a SQL statement inside the notebook cell.')
t('notebook_local_upload', 'Upload a CSV extract into the notebook and analyse it there',
  'A local extract leaves the governed table behind and cannot be reproduced from the notebook alone.')
t('looker_dashboard', 'Build a governed Looker dashboard',
  'A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules.')
t('looker_studio', 'Build a Looker Studio report',
  'Looker Studio is the fast self-serve reporting surface for a small number of sources.')
t('lookml_parameter', 'Change the LookML parameter in the view',
  'A LookML parameter changes the model for every dashboard that uses it rather than one tile.')
t('lookml_measure', 'Add a LookML measure for the calculation',
  'A measure declares the aggregation once so every report computes it the same way.')
t('lookml_explore', 'Expose the table through a LookML explore',
  'An explore defines which joins and fields a report author may use.')
t('dashboard_share', 'Share the dashboard with a scheduled delivery',
  'A scheduled delivery pushes the answer to people who will not open the tool.')
t('cache_toggle', 'Turn off the result cache to force a fresh read',
  'Disabling the cache makes every read hit the table, which costs more and slows the dashboard.')

# ------------------------------------------------------- machine learning
t('bqml_linear', 'Train a BigQuery ML linear regression model',
  'Linear regression predicts a continuous value and trains with SQL against the table.')
t('bqml_logistic', 'Train a BigQuery ML logistic regression model',
  'Logistic regression predicts a binary outcome and trains with SQL against the table.')
t('bqml_kmeans', 'Train a BigQuery ML k-means model',
  'K-means groups rows without a label column, so it segments rather than predicts.')
t('bqml_arima', 'Train a BigQuery ML ARIMA_PLUS model',
  'ARIMA_PLUS forecasts a series and returns an interval per period.')
t('bqml_boosted', 'Train a BigQuery ML boosted tree model',
  'A boosted tree model fits non-linear relationships in tabular rows.')
t('automl_tabular', 'Train an AutoML tabular model',
  'AutoML searches architectures and tuning for a team that has labels but no modelling code.')
t('remote_gemini_model', 'Create a BigQuery remote model over a Gemini model',
  'A remote model sends the prompt to Gemini from SQL while the rows stay in BigQuery.')
t('bqml_finetune', 'Fine-tune a Gemini model from the warehouse rows',
  'Fine-tuning adapts the model to the domain using labelled rows that stay in BigQuery.')
t('in_memory_pandas', 'Load the extract into a notebook and work in pandas',
  'A notebook copy of the extract is outside the governed table and cannot be reproduced later.')
t('bq_connection', 'Create the BigQuery connection that reaches the model endpoint',
  'The connection carries the service account that BigQuery uses to call the remote model.')
t('ml_evaluate', 'Evaluate the model with ML.EVALUATE',
  'ML.EVALUATE returns the model metrics against a labelled dataset.')
t('ml_predict', 'Score the rows with ML.PREDICT',
  'ML.PREDICT applies a trained model to new rows and returns the prediction.')
t('ml_forecast', 'Generate the forecast with ML.FORECAST',
  'ML.FORECAST returns future periods and their intervals from a time series model.')
t('ml_explain', 'Explain the prediction with ML.EXPLAIN_PREDICT',
  'ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row.')
t('model_registry_register', 'Register the model version in Model Registry',
  'Model Registry keeps each version with its lineage so a deployment names a version rather than a path.')
t('ml_project_plan', 'Plan collection, training, evaluation, then prediction',
  'A planned sequence fixes the data, the metric, and the acceptance test before any model is trained.')
t('split_by_time', 'Hold the most recent period out as the test set',
  'A time-ordered split tests the model on rows that come after the ones it learned from.')
t('split_by_entity', 'Hold out whole entities so none spans both splits',
  'A grouped split keeps one customer from appearing on both sides of the evaluation.')
t('train_test_split', 'Hold out a labelled split before training',
  'A held-out split gives an estimate that the training rows cannot inflate.')
t('skip_evaluation', 'Ship the model once the training loss looks good',
  'Training loss measures fit to the rows it has already seen, not the answer on new rows.')
t('bigquery_ml_unsupervised', 'Use BigQuery ML to cluster the rows without labels',
  'An unsupervised model answers a segmentation question where no outcome column exists.')

# ------------------------------------------------------- pipeline and orchestration
t('dataflow_pipeline', 'Build the pipeline in Dataflow',
  'Dataflow runs the same code for streaming and batch and scales the workers with the load.')
t('dataproc_spark', 'Run the transformation as Spark on Dataproc',
  'Dataproc runs Spark or Hadoop jobs when the team already owns that code.')
t('data_fusion', 'Build the pipeline in Cloud Data Fusion',
  'Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition.')
t('cloud_composer', 'Orchestrate the steps in Cloud Composer',
  'Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits.')
t('dataform', 'Manage the SQL transformations in Dataform',
  'Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse.')
t('workflows', 'Sequence the API calls with Workflows',
  'Workflows chains service calls and HTTP endpoints without running a server.')
t('scheduled_query', 'Schedule the SQL with a BigQuery scheduled query',
  'A scheduled query runs one statement on a cron schedule and writes its result.')
t('cloud_scheduler', 'Trigger the job from Cloud Scheduler',
  'Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query.')
t('dataproc_workflow_template', 'Submit the job through a Dataproc workflow template',
  'A workflow template defines the cluster and the steps so the same job can be re-run identically.')
t('pubsub_subscription', 'Subscribe BigQuery to the Pub/Sub topic',
  'A BigQuery subscription writes each published message into a table as it arrives.')
t('eventarc_trigger', 'Start the pipeline from an Eventarc trigger',
  'An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target.')
t('cloud_functions', 'Run the handler as a Cloud Functions function',
  'A Cloud Functions function handles a single event without a cluster to operate.')
t('cloud_run_service', 'Deploy the handler as a Cloud Run service',
  'A Cloud Run service takes the request and returns a response, and the pipeline calls it.')
t('cron_vm', 'Run a cron job on a Compute Engine instance',
  'A single VM cron job has no managed retry and fails silently when the instance is restarted.')
t('manual_runbook', 'Document the steps and have an analyst run them each morning',
  'A runbook depends on a person being present and leaves no execution record.')
t('dataflow_job_ui', 'Watch the job graph and per-step throughput in the Dataflow console',
  'The Dataflow job view shows the running graph, watermarks, and the step that is backlogged.')
t('logging_explorer', 'Query the job logs in Logs Explorer',
  'Logs Explorer filters the log entries that explain why a worker restarted.')
t('monitoring_alert', 'Create a Cloud Monitoring alert policy on the job metric',
  'An alert policy pages someone when the backlog or the failure rate crosses a threshold.')
t('failed_rows_table', 'Write the rejected rows to a dead-letter table',
  'A dead-letter table preserves the rows that failed so they can be repaired and replayed.')
t('bq_scheduled_backfill', 'Re-run the scheduled query with a wider date range',
  'A backfill re-reads the missed window rather than waiting for the next scheduled run.')

# ------------------------------------------------------- access control
t('iam_least_privilege', 'Grant the predefined role that matches the task',
  'A predefined role carries the permissions for one job and nothing else.')
t('basic_role', 'Grant the basic Owner role to the team',
  'A basic role spans every service, so it grants far more than the task needs.')
t('predefined_role', 'Assign a predefined role to the group',
  'A predefined role is maintained by Google and covers one service or one job function.')
t('custom_role', 'Create a custom role with only the permissions used',
  'A custom role narrows the grant when no predefined role matches the job exactly.')
t('service_account', 'Run the job as a dedicated service account',
  'A service account gives the workload its own identity instead of borrowing a person\'s.')
t('domain_wide_grant', 'Grant the role to the whole domain',
  'A domain-wide grant reaches every identity in the organisation, including the ones that never needed it.')
t('uniform_access', 'Enable uniform bucket-level access',
  'Uniform bucket-level access replaces per-object ACLs with IAM on the bucket.')
t('fine_grained_acl', 'Manage per-object ACLs on the bucket',
  'Per-object ACLs are hard to audit and are overridden when uniform access is enabled.')
t('public_bucket', 'Make the bucket public so the partner can read it',
  'A public bucket exposes every object in it to anyone with the URL.')
t('signed_url', 'Issue a signed URL with a short expiry',
  'A signed URL grants temporary read access to one object without changing IAM.')
t('analytics_hub', 'Publish the dataset through Analytics Hub',
  'Analytics Hub shares a curated dataset with a subscriber who reads it in place.')
t('dataset_export', 'Export the table to a bucket the partner owns',
  'An export hands over a copy that the publisher can no longer control or revoke.')
t('vpc_sc_perimeter', 'Add the project to a VPC Service Controls perimeter',
  'A perimeter blocks data movement outside the boundary even for an authorised identity.')

# ------------------------------------------------------- lifecycle and cost
t('gcs_standard', 'Keep the objects in the Standard class',
  'Standard is for objects read frequently, where access cost matters more than storage cost.')
t('gcs_nearline', 'Move the objects to Nearline',
  'Nearline costs less to store and charges for early deletion, so it suits reads about once a month.')
t('gcs_coldline', 'Move the objects to Coldline',
  'Coldline suits reads a few times a year and has a longer minimum storage duration.')
t('gcs_archive', 'Move the objects to Archive',
  'Archive is the cheapest class for data kept for compliance and read almost never.')
t('gcs_autoclass', 'Enable Autoclass on the bucket',
  'Autoclass moves each object between classes as its access pattern changes.')
t('lifecycle_delete', 'Add a lifecycle rule that deletes objects after the retention period',
  'A delete rule removes the objects once the retention period passes, without a person remembering.')
t('lifecycle_setclass', 'Add a lifecycle rule that changes the storage class',
  'A setStorageClass rule demotes an object after a number of days so the cost falls without a copy.')
t('bq_table_expiration', 'Set a table expiration on the dataset',
  'A dataset-level expiration removes tables created in it after the configured period.')
t('bq_partition_expiration', 'Set a partition expiration on the table',
  'Partition expiration drops old partitions while the table keeps the recent ones.')
t('no_lifecycle', 'Leave the objects in place and review them next year',
  'An ageing bucket with no rule grows without a decision about what is still needed.')
t('keep_forever_standard', 'Keep every version in the Standard class forever',
  'Keeping every version in the hot class pays the highest rate for data nobody reads.')

# ------------------------------------------------------- availability and recovery
t('gcs_versioning', 'Enable object versioning on the bucket',
  'Object versioning keeps a prior generation so an overwrite or delete can be reversed.')
t('gcs_retention_lock', 'Apply a bucket retention policy with a lock',
  'A locked retention policy prevents deletion for the period, even by an administrator.')
t('dual_region_bucket', 'Create a dual-region bucket with a replication policy',
  'A dual-region bucket keeps a copy in a second region and reports the replication lag.')
t('multi_region_bucket', 'Create a multi-region bucket',
  'A multi-region bucket spreads the objects across a geography for availability rather than a named pair.')
t('cloud_sql_backup', 'Enable automated backups and point-in-time recovery on Cloud SQL',
  'Automated backups with point-in-time recovery restore the instance to a chosen moment.')
t('read_replica', 'Create a Cloud SQL read replica in another region',
  'A read replica serves reads from a second region and can be promoted during a regional failure.')
t('cross_region_copy', 'Copy the bucket to a second region with a scheduled transfer',
  'A scheduled copy rebuilds a second copy but leaves a gap between runs.')
t('no_backup', 'Rely on the disk snapshot the platform keeps',
  'An unmanaged snapshot has no restore test and no defined retention.')
t('restore_drill', 'Restore into a scratch project on a schedule',
  'A restore drill is the only evidence that the backup can actually be used.')
t('ha_regional', 'Deploy the instance as regional with a standby',
  'A regional instance fails over to a standby in another zone inside the same region.')
t('zonal_single', 'Deploy a single zonal instance to keep the cost down',
  'A zonal instance is lost with its zone and gives no automatic failover.')

# ------------------------------------------------------- encryption and keys
t('cmek', 'Encrypt with a customer-managed key from Cloud KMS',
  'A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext.')
t('csek', 'Supply a customer-supplied key with each request',
  'A customer-supplied key never reaches Google, and losing it loses the object.')
t('gmek', 'Use the Google-managed default encryption',
  'Google-managed keys need no work from the customer and cannot be rotated or revoked by them.')
t('kms_keyring', 'Create the key in a Cloud KMS key ring in the data region',
  'A key ring in the same region keeps the key and the ciphertext under the same residency rule.')
t('kms_rotation', 'Set a rotation schedule on the key',
  'A rotation schedule limits how long one key version protects new data.')
t('kms_destroy', 'Destroy the key version to stop access immediately',
  'Destroying the key makes the ciphertext permanently unreadable, including for a restore.')
t('tls_in_transit', 'Enforce TLS for every connection to the service',
  'Encryption in transit protects the bytes while they are on the wire between client and service.')
t('aes_at_rest', 'Confirm the data is encrypted at rest by the storage service',
  'Encryption at rest protects the stored bytes on the medium, not the connection that reads them.')
t('client_side_only', 'Encrypt in the client and store the key next to the data',
  'A key stored beside the data protects nothing against anyone who can read the store.')
t('key_in_code', 'Put the key in the application configuration file',
  'A key in a configuration file is copied into every environment and every backup of that file.')

# ------------------------------------------------------- costs, quotas, misc
t('flat_rate_slots', 'Buy BigQuery slots as a reservation',
  'A reservation fixes the compute capacity and the bill, which suits a predictable workload.')
t('on_demand', 'Leave the workload on on-demand pricing',
  'On-demand pricing charges per byte scanned, which suits spiky or small workloads.')
t('partition_filter', 'Filter the query on the partition column',
  'A partition filter restricts the scan to the partitions the query needs.')
t('select_star', 'Select every column to be safe',
  'Selecting every column scans columns the report never uses and raises the cost.')
t('cluster_table', 'Cluster the table on the filter column',
  'Clustering co-locates similar values so a filtered query reads fewer blocks.')
t('denormalise', 'Denormalise the tables into one wide table',
  'A wide table removes the join, at the cost of duplicated rows and a wider scan.')
t('external_table', 'Query the files through an external table',
  'An external table reads the objects where they sit and does not copy them into storage.')
t('load_to_native', 'Load the files into a native table',
  'A native table gives the warehouse its own copy and the best scan performance.')
