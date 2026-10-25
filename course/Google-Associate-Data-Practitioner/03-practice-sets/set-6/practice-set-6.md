# Google Cloud Associate Data Practitioner — Full-Length Mock Exam 6

Associate Data Practitioner · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Data Preparation and Ingestion (Ingestion, Reporting, Pipelines, and Access)

### 1. Point-of-sale feeds must be deduplicated and converted to one currency before analysts ever see them. Which approach is described?

- A. Load the raw rows, then transform them inside the warehouse
- B. Query the source system in place with a federated query
- C. Extract, transform outside the warehouse, then load the result
- D. Load into a staging area, apply a light transform, then transform again in the warehouse

### 2. The modelling team wants to derive new features without asking ingestion for another extract. Which approach fits?

- A. Transform on the source system before the export starts
- B. Extract, transform outside the warehouse, then load the result
- C. Load the raw rows, then transform them inside the warehouse
- D. Load into a staging area, apply a light transform, then transform again in the warehouse

### 3. One read of a partner's external table is needed, and the raw copy must stay replayable for later questions. Which two choices fit? Select two.

- A. Query the source system in place with a federated query
- B. Combine the extracts in a spreadsheet and upload the result
- C. Land the extract in a staging table before any transform runs
- D. Transform on the source system before the export starts
- E. Load the raw rows, then transform them inside the warehouse

### 4. A city government wants a light scrub at the edge so the warehouse has less to read. Which design fits?

- A. Load into a staging area, apply a light transform, then transform again in the warehouse
- B. Transform on the source system before the export starts
- C. Extract, transform outside the warehouse, then load the result
- D. Load the raw rows, then transform them inside the warehouse

### 5. A status column holds four spellings of the same cancelled state. Where should the values be reconciled?

- A. Load first and fix the rejected rows afterwards
- B. Load the extract into a notebook and work in pandas
- C. Combine the extracts in a spreadsheet and upload the result
- D. Clean the rows with SQL in BigQuery

### 6. Checkout events must be validated before they land and the same rules must run on replay. What should be used?

- A. Run a cron job on a Compute Engine instance
- B. Clean the data with Spark on Dataproc
- C. Clean the stream with a Dataflow pipeline
- D. Clean the rows with SQL in BigQuery

### 7. The chief data officer wants a weekly scorecard of which checks passed. What should be added?

- A. Load first and fix the rejected rows afterwards
- B. Define data quality rules and run a quality scan
- C. Profile the columns to measure the null rate before loading
- D. Select every column to be safe

### 8. A delivery must be proven complete, and the gaps must be quantified before publication. Which two actions apply? Select two.

- A. Profile the columns to measure the null rate before loading
- B. Land the data as CSV
- C. Select every column to be safe
- D. Compare the row count with the source after every load
- E. Load first and fix the rejected rows afterwards

### 9. A nightly set of files must be pulled from Azure Blob into a bucket. What should be used?

- A. Use Storage Transfer Service
- B. Copy the objects with the gcloud storage command
- C. Pull the files from the partner over FTP each night
- D. Order a Transfer Appliance

### 10. A PostgreSQL estate must move to Cloud SQL with a cutover at the weekend. What should be used?

- A. Use Database Migration Service
- B. Order a Transfer Appliance
- C. Replicate the changes with Datastream
- D. Use BigQuery Data Transfer Service

### 11. A Google Marketing Platform transfer must appear in a warehouse table each morning. What should be used?

- A. Use Storage Transfer Service
- B. Load the rows with a client library from the application
- C. Use BigQuery Data Transfer Service
- D. Replicate the changes with Datastream

### 12. The first full copy and every later change must both arrive without a second bulk read. Which two tools apply? Select two.

- A. Use BigQuery Data Transfer Service
- B. Order a Transfer Appliance
- C. Use Database Migration Service
- D. Replicate the changes with Datastream
- E. Pull the files from the partner over FTP each night

### 13. Sensor rollups are read by three of ninety columns on every dashboard refresh. Which format fits?

- A. Land the data as CSV
- B. Land the data as Parquet
- C. Land the data as newline-delimited JSON
- D. Land the data as XML

### 14. A write-ahead log must ship records whose schema is enforced by the writer. Which format fits?

- A. Convert the data to ORC before the load
- B. Land the data as Avro
- C. Land the data as newline-delimited JSON
- D. Land the data as CSV

### 15. Configuration documents carry optional fields that differ per tenant. Which format fits?

- A. Land the data as CSV
- B. Convert the data to ORC before the load
- C. Land the data as newline-delimited JSON
- D. Land the data as Avro

### 16. A hand-maintained lookup table is edited by a business user and re-uploaded weekly. Which format fits?

- A. Land the data as CSV
- B. Land the data as Avro
- C. Convert the data to ORC before the load
- D. Land the data as Parquet

### 17. A batch of gzipped JSON files must be appended to one table each hour. What should be used?

- A. Stream the rows with the BigQuery Storage Write API
- B. Load the rows with a client library from the application
- C. Load the files with the bq load command
- D. Copy the objects with the gcloud storage command

### 18. Every published message must be archived to a bucket as a raw file before any transform. What should be used?

- A. Run the handler as a Cloud Functions function
- B. Build the pipeline in Dataflow
- C. Load the files with the bq load command
- D. Load the rows with a client library from the application

### 19. A Node.js worker must append rows it has already assembled. What should be used?

- A. Copy the objects with the gcloud storage command
- B. Load the files with the bq load command
- C. Stream the rows with the BigQuery Storage Write API
- D. Load the rows with a client library from the application

### 20. An ad exchange logs bids by request identifier and reads the last minute back. Which store fits?

- A. Store the documents in Firestore
- B. Store the rows in Bigtable
- C. Store the records in Cloud SQL
- D. Store the rows in BigQuery

### 21. An ERP needs triggers and foreign keys over a fixed schema. Which store fits?

- A. Store the records in Spanner
- B. Store the records in Cloud SQL
- C. Store the records in AlloyDB for PostgreSQL
- D. Store the rows in Bigtable

### 22. A mapping workload needs PostgreSQL compatibility and more throughput than its current instance. Which store fits?

- A. Store the rows in BigQuery
- B. Store the records in Cloud SQL
- C. Store the records in AlloyDB for PostgreSQL
- D. Store the documents in Firestore

### 23. The curated tables must be queryable, and the raw files must stay available for a re-load. Which two stores apply? Select two.

- A. Keep the dataset on the analyst workstation
- B. Store the rows in Bigtable
- C. Store the documents in Firestore
- D. Store the rows in BigQuery
- E. Store the files in Cloud Storage

### 24. Readers in Sydney and São Paulo complain about query latency. What should drive the placement?

- A. Place the data in the region nearest the largest user base
- B. Choose a dual-region location
- C. Choose a zonal resource
- D. Choose a multi-region location

### 25. A metro-wide service has one user base and a fixed budget. Which location type fits?

- A. Choose a regional location
- B. Choose a dual-region location
- C. Choose a zonal resource
- D. Choose a multi-region location

### 26. The country is fixed by law, and one region already meets the latency target. Which two choices apply? Select two.

- A. Choose a regional location
- B. Place the data in the region the regulator names
- C. Place the data in the region nearest the largest user base
- D. Choose a zonal resource
- E. Choose a multi-region location

### 27. A spreadsheet export has one typed column per header. How should it be classified?

- A. Treat the records as structured data
- B. Apply a schema on read at query time
- C. Treat the files as unstructured data
- D. Treat the records as semi-structured data

### 28. A bucket holds scanned invoices and product photographs. How should the files be classified?

- A. Treat the records as semi-structured data
- B. Apply a schema on read at query time
- C. Treat the files as unstructured data
- D. Treat the records as structured data

### 29. A bidding service must commit rows with the lowest possible commit latency. What should be used?

- A. Load the files with the bq load command
- B. Stream the rows with the BigQuery Storage Write API
- C. Load the rows with a client library from the application
- D. Copy the objects with the gcloud storage command

### 30. A release script must publish fixtures to a bucket before the tests run. What should be used?

- A. Use Storage Transfer Service
- B. Order a Transfer Appliance
- C. Load the files with the bq load command
- D. Copy the objects with the gcloud storage command

---

## Domain 2 — Data Analysis and Presentation (Files, Formats, Dashboards, and Governance)

### 31. A column must stay in the table but be hidden from a group of analysts. What should be used?

- A. Create a BigQuery view over the join
- B. Load the files into a native table
- C. Create a BigQuery materialized view
- D. Query the files through an external table

### 32. A refresh every five minutes repeats one expensive aggregation. What should be used?

- A. Load the files into a native table
- B. Write a SQL query in BigQuery and save the result
- C. Create a BigQuery materialized view
- D. Create a BigQuery view over the join

### 33. The same aggregate is recomputed for one date range, and the table is scanned whole. Which two changes help? Select two.

- A. Turn off the result cache to force a fresh read
- B. Create a BigQuery materialized view
- C. Filter the query on the partition column
- D. Select every column to be safe
- E. Query the files through an external table

### 34. Files must be inspected before anyone agrees to load them into the warehouse. What should be used?

- A. Create a BigQuery view over the join
- B. Load the files into a native table
- C. Query the files through an external table
- D. Create a BigQuery materialized view

### 35. A data team wants a hosted runtime that reaches an internal metastore through the project VPC. What should be used?

- A. Keep the dataset on the analyst workstation
- B. Upload a CSV extract into the notebook and analyse it there
- C. Load the extract into a notebook and work in pandas
- D. Analyse the data in a Colab Enterprise notebook

### 36. Analysts keep emailing spreadsheet extracts because their notebook cannot query the warehouse directly. What should be used?

- A. Query BigQuery from the notebook with the %%bigquery magic
- B. Load the extract into a notebook and work in pandas
- C. Upload a CSV extract into the notebook and analyse it there
- D. Export the query result to a spreadsheet for the business team

### 37. A category manager asks which SKU cannibalised another during the promotion. What should be produced?

- A. Share the dashboard with a scheduled delivery
- B. Turn off the result cache to force a fresh read
- C. Write a SQL query in BigQuery and save the result
- D. Document the steps and have an analyst run them each morning

### 38. Regional leads want the morning numbers pushed to them without signing in anywhere. What should be configured?

- A. Export the query result to a spreadsheet for the business team
- B. Share the dashboard with a scheduled delivery
- C. Document the steps and have an analyst run them each morning
- D. Turn off the result cache to force a fresh read

### 39. Every tile must inherit one certified definition of active subscriber. What should be used?

- A. Build a governed Looker dashboard
- B. Select every column to be safe
- C. Build a Looker Studio report
- D. Export the query result to a spreadsheet for the business team

### 40. Two dashboards disagree about gross margin because each author typed the formula by hand. What should be added?

- A. Turn off the result cache to force a fresh read
- B. Build a Looker Studio report
- C. Add a LookML measure for the calculation
- D. Expose the table through a LookML explore

### 41. One governed surface is needed, and one certified metric must serve every tile. Which two components apply? Select two.

- A. Select every column to be safe
- B. Build a Looker Studio report
- C. Build a governed Looker dashboard
- D. Add a LookML measure for the calculation
- E. Turn off the result cache to force a fresh read

### 42. An intern needs a chart over one sheet this morning. What should be used?

- A. Build a Looker Studio report
- B. Orchestrate the steps in Cloud Composer
- C. Build a governed Looker dashboard
- D. Add a LookML measure for the calculation

### 43. Certified metrics and per-group access must hold across forty reports. What should be used?

- A. Issue a signed URL with a short expiry
- B. Build a Looker Studio report
- C. Export the query result to a spreadsheet for the business team
- D. Build a governed Looker dashboard

### 44. The week-start day changed and every report must roll up differently. What should be changed?

- A. Add a LookML measure for the calculation
- B. Turn off the result cache to force a fresh read
- C. Expose the table through a LookML explore
- D. Change the LookML parameter in the view

### 45. A net-revenue ratio must be written once and reused everywhere. What should be added?

- A. Add a LookML measure for the calculation
- B. Change the LookML parameter in the view
- C. Turn off the result cache to force a fresh read
- D. Write a SQL query in BigQuery and save the result

### 46. Analysts keep joining a table that should only be reachable through one approved path. What should be added?

- A. Expose the table through a LookML explore
- B. Write a SQL query in BigQuery and save the result
- C. Change the LookML parameter in the view
- D. Add a LookML measure for the calculation

### 47. A support team wants the probability that a ticket breaches its SLA. Which model type fits?

- A. Train a BigQuery ML ARIMA_PLUS model
- B. Score the rows with ML.PREDICT
- C. Train a BigQuery ML linear regression model
- D. Train a BigQuery ML logistic regression model

### 48. Stores must be grouped by basket mix and no target column exists anywhere. What should be built?

- A. Train a BigQuery ML ARIMA_PLUS model
- B. Train a BigQuery ML k-means model
- C. Train a BigQuery ML logistic regression model
- D. Train an AutoML tabular model

### 49. A team has labels and no modelling code, and a monthly series must be forecast. Which two products apply? Select two.

- A. Train a BigQuery ML ARIMA_PLUS model
- B. Generate the forecast with ML.FORECAST
- C. Train a BigQuery ML logistic regression model
- D. Train a BigQuery ML k-means model
- E. Train an AutoML tabular model

### 50. Reviews must be labelled per row while the text stays under warehouse governance. What should be used?

- A. Land the data as newline-delimited JSON
- B. Fine-tune a Gemini model from the warehouse rows
- C. Create a BigQuery remote model over a Gemini model
- D. Load the extract into a notebook and work in pandas

### 51. A new remote model fails before its first prompt because no identity can reach the endpoint. What should be created?

- A. Copy the objects with the gcloud storage command
- B. Load the files with the bq load command
- C. Issue a signed URL with a short expiry
- D. Create the BigQuery connection that reaches the model endpoint

### 52. The sponsor wants the four stages and the acceptance test written down before any spend. What should be produced?

- A. Document the steps and have an analyst run them each morning
- B. Plan collection, training, evaluation, then prediction
- C. Run a cron job on a Compute Engine instance
- D. Ship the model once the training loss looks good

### 53. One account must not appear on both sides, and the score must come from rows the model never saw. Which two practices apply? Select two.

- A. Hold out whole entities so none spans both splits
- B. Ship the model once the training loss looks good
- C. Hold out a labelled split before training
- D. Hold the most recent period out as the test set
- E. Profile the columns to measure the null rate before loading

### 54. A model card must quote the holdout AUC produced by a SQL statement. What should be used?

- A. Score the rows with ML.PREDICT
- B. Explain the prediction with ML.EXPLAIN_PREDICT
- C. Generate the forecast with ML.FORECAST
- D. Evaluate the model with ML.EVALUATE

### 55. The reported score must come from rows the model never saw. What should be done?

- A. Denormalise the tables into one wide table
- B. Hold out a labelled split before training
- C. Evaluate the model with ML.EVALUATE
- D. Ship the model once the training loss looks good

### 56. Next week's shortage risk must be produced from a fitted time series model. What should be used?

- A. Score the rows with ML.PREDICT
- B. Generate the forecast with ML.FORECAST
- C. Evaluate the model with ML.EVALUATE
- D. Explain the prediction with ML.EXPLAIN_PREDICT

### 57. An incident review asks which binary produced last Tuesday's scores. What should have been used?

- A. Register the model version in Model Registry
- B. Keep the dataset on the analyst workstation
- C. Copy the objects with the gcloud storage command
- D. Export the query result to a spreadsheet for the business team

---

## Domain 3 — Data Pipeline Orchestration (Streaming, Scheduling, Modelling, and Recovery)

### 58. Transformations must be version-controlled and tested before they reach production. What should be used?

- A. Manage the SQL transformations in Dataform
- B. Run the transformation as Spark on Dataproc
- C. Build the pipeline in Cloud Data Fusion
- D. Run a cron job on a Compute Engine instance

### 59. Out-of-order events must be grouped by a window that closes after a watermark. What should be used?

- A. Sequence the API calls with Workflows
- B. Run the transformation as Spark on Dataproc
- C. Run the handler as a Cloud Functions function
- D. Build the pipeline in Dataflow

### 60. Decade-old Hadoop jobs must run unchanged on managed infrastructure. What should be used?

- A. Sequence the API calls with Workflows
- B. Run the transformation as Spark on Dataproc
- C. Manage the SQL transformations in Dataform
- D. Build the pipeline in Dataflow

### 61. One path needs streaming parity and another needs joins built with no code. Which two tools apply? Select two.

- A. Build the pipeline in Dataflow
- B. Run the handler as a Cloud Functions function
- C. Build the pipeline in Cloud Data Fusion
- D. Run the transformation as Spark on Dataproc
- E. Trigger the job from Cloud Scheduler

### 62. The source database is saturated, so the join work must move into the warehouse engine after a raw load. Which design fits?

- A. Query the source system in place with a federated query
- B. Extract, transform outside the warehouse, then load the result
- C. Load the raw rows, then transform them inside the warehouse
- D. Transform on the source system before the export starts

### 63. A payment contract forbids storing unmasked card data at any layer of the platform. Which design fits?

- A. Load the rows with a client library from the application
- B. Land the extract in a staging table before any transform runs
- C. Load the raw rows, then transform them inside the warehouse
- D. Extract, transform outside the warehouse, then load the result

### 64. A revenue aggregate must refresh itself at 02:00 with no operator logged in. What should be used?

- A. Schedule the SQL with a BigQuery scheduled query
- B. Trigger the job from Cloud Scheduler
- C. Sequence the API calls with Workflows
- D. Submit the job through a Dataproc workflow template

### 65. A scheduled run was skipped during maintenance and the gap must be filled. What should be done?

- A. Re-run the scheduled query with a wider date range
- B. Turn off the result cache to force a fresh read
- C. Select every column to be safe
- D. Schedule the SQL with a BigQuery scheduled query

### 66. Two triggers are needed: one for a warehouse statement and one for an HTTP endpoint. Which two components apply? Select two.

- A. Document the steps and have an analyst run them each morning
- B. Trigger the job from Cloud Scheduler
- C. Schedule the SQL with a BigQuery scheduled query
- D. Sequence the API calls with Workflows
- E. Run a cron job on a Compute Engine instance

### 67. A streaming job publishes late results and the team must see which stage holds the backlog. Where should the team look?

- A. Watch the job graph and per-step throughput in the Dataflow console
- B. Query the job logs in Logs Explorer
- C. Write a SQL query in BigQuery and save the result
- D. Turn off the result cache to force a fresh read

### 68. Malformed events must be replayable rather than lost. What should be added?

- A. Load first and fix the rejected rows afterwards
- B. Denormalise the tables into one wide table
- C. Write the rejected rows to a dead-letter table
- D. Select every column to be safe

### 69. A pipeline failed at 03:12 and only the log stream records what happened. Where should the team look?

- A. Share the dashboard with a scheduled delivery
- B. Write a SQL query in BigQuery and save the result
- C. Document the steps and have an analyst run them each morning
- D. Query the job logs in Logs Explorer

### 70. A freshness objective must notify an owner the moment it is breached. What should be added?

- A. Document the steps and have an analyst run them each morning
- B. Turn off the result cache to force a fresh read
- C. Create a Cloud Monitoring alert policy on the job metric
- D. Query the job logs in Logs Explorer

### 71. A late partner file must not skip the downstream steps, and the SLA must be recorded. What should orchestrate it?

- A. Sequence the API calls with Workflows
- B. Orchestrate the steps in Cloud Composer
- C. Schedule the SQL with a BigQuery scheduled query
- D. Run the handler as a Cloud Functions function

### 72. A reproducibility audit needs the same cluster shape and job arguments on every run. What should be used?

- A. Trigger the job from Cloud Scheduler
- B. Submit the job through a Dataproc workflow template
- C. Run a cron job on a Compute Engine instance
- D. Document the steps and have an analyst run them each morning

### 73. Delivery must be driven by a landing event and still honour a cross-system dependency order. Which two components apply? Select two.

- A. Start the pipeline from an Eventarc trigger
- B. Run a cron job on a Compute Engine instance
- C. Orchestrate the steps in Cloud Composer
- D. Schedule the SQL with a BigQuery scheduled query
- E. Run the handler as a Cloud Functions function

### 74. Published clicks must appear in a table within seconds with no subscriber to run. What should be used?

- A. Load the files with the bq load command
- B. Schedule the SQL with a BigQuery scheduled query
- C. Start the pipeline from an Eventarc trigger
- D. Subscribe BigQuery to the Pub/Sub topic

### 75. A manifest appearing in storage must kick off the transformation run within seconds. What should be used?

- A. Subscribe BigQuery to the Pub/Sub topic
- B. Start the pipeline from an Eventarc trigger
- C. Trigger the job from Cloud Scheduler
- D. Schedule the SQL with a BigQuery scheduled query

---

## Domain 4 — Data Management (Warehouse Analytics, Orchestration, and Key Management)

### 76. A partner's pipeline must write to one dataset and read nothing else. What should be granted?

- A. Grant the role to the whole domain
- B. Grant the basic Owner role to the team
- C. Grant the predefined role that matches the task
- D. Make the bucket public so the partner can read it

### 77. A scheduled query must run under its own identity rather than an employee's. What should be used?

- A. Run the job as a dedicated service account
- B. Grant the basic Owner role to the team
- C. Issue a signed URL with a short expiry
- D. Grant the role to the whole domain

### 78. A security team wants a hard boundary that no identity grant can cross. What should be applied?

- A. Make the bucket public so the partner can read it
- B. Add the project to a VPC Service Controls perimeter
- C. Grant the role to the whole domain
- D. Export the table to a bucket the partner owns

### 79. A contractor needs the managed role that matches reading one dataset. What should be granted?

- A. Make the bucket public so the partner can read it
- B. Grant the basic Owner role to the team
- C. Create a custom role with only the permissions used
- D. Assign a predefined role to the group

### 80. One role must be maintained by Google, and another must carry only the permissions in use. Which two role types apply? Select two.

- A. Grant the role to the whole domain
- B. Grant the basic Owner role to the team
- C. Assign a predefined role to the group
- D. Create a custom role with only the permissions used
- E. Make the bucket public so the partner can read it

### 81. A security review wants one permission model instead of thousands of object entries. What should be enabled?

- A. Make the bucket public so the partner can read it
- B. Manage per-object ACLs on the bucket
- C. Issue a signed URL with a short expiry
- D. Enable uniform bucket-level access

### 82. Two bucket-level choices must be weighed for one exception among many objects. Which two apply? Select two.

- A. Enable uniform bucket-level access
- B. Export the table to a bucket the partner owns
- C. Issue a signed URL with a short expiry
- D. Manage per-object ACLs on the bucket
- E. Make the bucket public so the partner can read it

### 83. A partner must query the shared dataset live rather than receiving a copy each month. What should be used?

- A. Issue a signed URL with a short expiry
- B. Export the table to a bucket the partner owns
- C. Publish the dataset through Analytics Hub
- D. Make the bucket public so the partner can read it

### 84. An external auditor will work offline on their own infrastructure for a year. What should be done?

- A. Add the project to a VPC Service Controls perimeter
- B. Publish the dataset through Analytics Hub
- C. Export the table to a bucket the partner owns
- D. Issue a signed URL with a short expiry

### 85. Audit exports are retrieved about once a quarter. Which class fits?

- A. Move the objects to Nearline
- B. Keep the objects in the Standard class
- C. Move the objects to Archive
- D. Move the objects to Coldline

### 86. A bucket mixes hot and cold objects and nobody wants to classify them. What should be enabled?

- A. Enable Autoclass on the bucket
- B. Move the objects to Archive
- C. Move the objects to Nearline
- D. Keep the objects in the Standard class

### 87. Hot objects must stay instantly readable, and cold ones must demote on their own. Which two options apply? Select two.

- A. Keep the objects in the Standard class
- B. Keep every version in the Standard class forever
- C. Add a lifecycle rule that changes the storage class
- D. Leave the objects in place and review them next year
- E. Move the objects to Archive

### 88. Scratch landing objects must disappear a day after arrival. What should be added?

- A. Leave the objects in place and review them next year
- B. Add a lifecycle rule that deletes objects after the retention period
- C. Enable object versioning on the bucket
- D. Keep every version in the Standard class forever

### 89. A dataset collects one table per experiment and must clean up after itself. What should be set?

- A. Leave the objects in place and review them next year
- B. Add a lifecycle rule that deletes objects after the retention period
- C. Set a table expiration on the dataset
- D. Set a partition expiration on the table

### 90. A studio keeps raw camera footage for a decade and opens it only for a re-cut. Which class fits?

- A. Move the objects to Nearline
- B. Move the objects to Coldline
- C. Move the objects to Archive
- D. Keep the objects in the Standard class

### 91. Auditors require proof that deletion cannot happen during the statutory period. What should be applied?

- A. Add a lifecycle rule that deletes objects after the retention period
- B. Enable object versioning on the bucket
- C. Leave the objects in place and review them next year
- D. Apply a bucket retention policy with a lock

### 92. A dropped table must be recoverable to a chosen moment last night. What should be used?

- A. Rely on the disk snapshot the platform keeps
- B. Copy the bucket to a second region with a scheduled transfer
- C. Deploy a single zonal instance to keep the cost down
- D. Enable automated backups and point-in-time recovery on Cloud SQL

### 93. The standby must sit in a different failure domain from the primary. What should be deployed?

- A. Rely on the disk snapshot the platform keeps
- B. Deploy the instance as regional with a standby
- C. Copy the bucket to a second region with a scheduled transfer
- D. Deploy a single zonal instance to keep the cost down

### 94. The backup copy must span the continent rather than a single named pair. What should be used?

- A. Create a dual-region bucket with a replication policy
- B. Enable object versioning on the bucket
- C. Copy the bucket to a second region with a scheduled transfer
- D. Create a multi-region bucket

### 95. An overwrite must be reversible, and the second copy must sit in a named pair of regions. Which two measures apply? Select two.

- A. Enable object versioning on the bucket
- B. Copy the bucket to a second region with a scheduled transfer
- C. Rely on the disk snapshot the platform keeps
- D. Create a dual-region bucket with a replication policy
- E. Create a multi-region bucket

### 96. The secondary copy must span a continent rather than one region or one zone. Which location type fits?

- A. Choose a zonal resource
- B. Choose a multi-region location
- C. Choose a dual-region location
- D. Choose a regional location

### 97. A tenant insists that disabling a key they control must stop every read of their rows. Which key model applies?

- A. Encrypt with a customer-managed key from Cloud KMS
- B. Supply a customer-supplied key with each request
- C. Put the key in the application configuration file
- D. Use the Google-managed default encryption

### 98. The key must travel with each request and never be stored by the provider. Which key model applies?

- A. Create the key in a Cloud KMS key ring in the data region
- B. Supply a customer-supplied key with each request
- C. Use the Google-managed default encryption
- D. Encrypt with a customer-managed key from Cloud KMS

### 99. Production and test keys must never be the same key, and both must be inventoried. What should be configured?

- A. Set a rotation schedule on the key
- B. Put the key in the application configuration file
- C. Use the Google-managed default encryption
- D. Create the key in a Cloud KMS key ring in the data region

### 100. A disk from a decommissioned node must yield nothing readable to a forensic team. Which protection answers that?

- A. Enforce TLS for every connection to the service
- B. Encrypt in the client and store the key next to the data
- C. Put the key in the application configuration file
- D. Confirm the data is encrypted at rest by the storage service

---

## Answer key and explanations

### Question 1 — C

Answer: Extract, transform outside the warehouse, then load the result. ETL cleans and converts the record before the load, so analysts only meet curated rows. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETL cleans and converts the record before the load, so analysts only meet curated rows.
- **B:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ETL cleans and converts the record before the load, so analysts only meet curated rows.
- **C:** Correct. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. In this case: ETL cleans and converts the record before the load, so analysts only meet curated rows.
- **D:** Incorrect for this question. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. Why the correct answer wins: ETL cleans and converts the record before the load, so analysts only meet curated rows.

### Question 2 — C

Answer: Load the raw rows, then transform them inside the warehouse. ELT keeps the raw rows, so a new feature is a new query rather than a new extract. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ELT keeps the raw rows, so a new feature is a new query rather than a new extract.
- **B:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT keeps the raw rows, so a new feature is a new query rather than a new extract.
- **C:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT keeps the raw rows, so a new feature is a new query rather than a new extract.
- **D:** Incorrect for this question. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. Why the correct answer wins: ELT keeps the raw rows, so a new feature is a new query rather than a new extract.

### Question 3 — A, E

Answers: Query the source system in place with a federated query; Load the raw rows, then transform them inside the warehouse. The federated query reads the partner table once, and ELT keeps the raw copy replayable. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. In this case: The federated query reads the partner table once, and ELT keeps the raw copy replayable.
- **B:** Incorrect for this question. A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run. Why the correct answer wins: The federated query reads the partner table once, and ELT keeps the raw copy replayable.
- **C:** Incorrect for this question. A staging table separates a failed load from a failed transform, so each can be retried on its own. Why the correct answer wins: The federated query reads the partner table once, and ELT keeps the raw copy replayable.
- **D:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: The federated query reads the partner table once, and ELT keeps the raw copy replayable.
- **E:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: The federated query reads the partner table once, and ELT keeps the raw copy replayable.

### Question 4 — A

Answer: Load into a staging area, apply a light transform, then transform again in the warehouse. ETLT scrubs before the warehouse step and still transforms after the load. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. In this case: ETLT scrubs before the warehouse step and still transforms after the load.
- **B:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ETLT scrubs before the warehouse step and still transforms after the load.
- **C:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ETLT scrubs before the warehouse step and still transforms after the load.
- **D:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETLT scrubs before the warehouse step and still transforms after the load.

### Question 5 — D

Answer: Clean the rows with SQL in BigQuery. SQL in the warehouse reconciles the values where they sit. SQL inside the warehouse removes duplicates, trims values, and casts types where the data already sits. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: SQL in the warehouse reconciles the values where they sit.
- **B:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: SQL in the warehouse reconciles the values where they sit.
- **C:** Incorrect for this question. A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run. Why the correct answer wins: SQL in the warehouse reconciles the values where they sit.
- **D:** Correct. SQL inside the warehouse removes duplicates, trims values, and casts types where the data already sits. In this case: SQL in the warehouse reconciles the values where they sit.

### Question 6 — C

Answer: Clean the stream with a Dataflow pipeline. A Dataflow pipeline applies one validation definition to the live stream and the replay. A Dataflow pipeline applies the same cleaning logic to streaming and batch records. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: A Dataflow pipeline applies one validation definition to the live stream and the replay.
- **B:** Incorrect for this question. Spark suits large files that need custom code rather than SQL. Why the correct answer wins: A Dataflow pipeline applies one validation definition to the live stream and the replay.
- **C:** Correct. A Dataflow pipeline applies the same cleaning logic to streaming and batch records. In this case: A Dataflow pipeline applies one validation definition to the live stream and the replay.
- **D:** Incorrect for this question. SQL inside the warehouse removes duplicates, trims values, and casts types where the data already sits. Why the correct answer wins: A Dataflow pipeline applies one validation definition to the live stream and the replay.

### Question 7 — B

Answer: Define data quality rules and run a quality scan. Declared rules produce the pass and fail results the scorecard reports. Declared rules turn a judgement about the data into a test that runs on every load. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: Declared rules produce the pass and fail results the scorecard reports.
- **B:** Correct. Declared rules turn a judgement about the data into a test that runs on every load. In this case: Declared rules produce the pass and fail results the scorecard reports.
- **C:** Incorrect for this question. A profile quantifies what is missing before the gaps reach a dashboard. Why the correct answer wins: Declared rules produce the pass and fail results the scorecard reports.
- **D:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: Declared rules produce the pass and fail results the scorecard reports.

### Question 8 — A, D

Answers: Compare the row count with the source after every load; Profile the columns to measure the null rate before loading. The row-count reconciliation proves completeness, and the profile quantifies the gaps. A row-count reconciliation catches a truncated or duplicated extract. A profile quantifies what is missing before the gaps reach a dashboard. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A profile quantifies what is missing before the gaps reach a dashboard. In this case: The row-count reconciliation proves completeness, and the profile quantifies the gaps.
- **B:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: The row-count reconciliation proves completeness, and the profile quantifies the gaps.
- **C:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: The row-count reconciliation proves completeness, and the profile quantifies the gaps.
- **D:** Correct. A row-count reconciliation catches a truncated or duplicated extract. In this case: The row-count reconciliation proves completeness, and the profile quantifies the gaps.
- **E:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: The row-count reconciliation proves completeness, and the profile quantifies the gaps.

### Question 9 — A

Answer: Use Storage Transfer Service. Storage Transfer Service copies from another cloud on a schedule. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: Storage Transfer Service copies from another cloud on a schedule.
- **B:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: Storage Transfer Service copies from another cloud on a schedule.
- **C:** Incorrect for this question. A hand-built FTP pull has no retry, no manifest, and no record of what arrived. Why the correct answer wins: Storage Transfer Service copies from another cloud on a schedule.
- **D:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: Storage Transfer Service copies from another cloud on a schedule.

### Question 10 — A

Answer: Use Database Migration Service. Database Migration Service performs the move with continuous replication. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. In this case: Database Migration Service performs the move with continuous replication.
- **B:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: Database Migration Service performs the move with continuous replication.
- **C:** Incorrect for this question. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Why the correct answer wins: Database Migration Service performs the move with continuous replication.
- **D:** Incorrect for this question. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Why the correct answer wins: Database Migration Service performs the move with continuous replication.

### Question 11 — C

Answer: Use BigQuery Data Transfer Service. BigQuery Data Transfer Service schedules the recurring Google-source load. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: BigQuery Data Transfer Service schedules the recurring Google-source load.
- **B:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: BigQuery Data Transfer Service schedules the recurring Google-source load.
- **C:** Correct. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. In this case: BigQuery Data Transfer Service schedules the recurring Google-source load.
- **D:** Incorrect for this question. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Why the correct answer wins: BigQuery Data Transfer Service schedules the recurring Google-source load.

### Question 12 — C, D

Answers: Use Database Migration Service; Replicate the changes with Datastream. Database Migration Service performs the initial copy, and Datastream carries the changes. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Why the correct answer wins: Database Migration Service performs the initial copy, and Datastream carries the changes.
- **B:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: Database Migration Service performs the initial copy, and Datastream carries the changes.
- **C:** Correct. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. In this case: Database Migration Service performs the initial copy, and Datastream carries the changes.
- **D:** Correct. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. In this case: Database Migration Service performs the initial copy, and Datastream carries the changes.
- **E:** Incorrect for this question. A hand-built FTP pull has no retry, no manifest, and no record of what arrived. Why the correct answer wins: Database Migration Service performs the initial copy, and Datastream carries the changes.

### Question 13 — B

Answer: Land the data as Parquet. Parquet reads only the three columns in the query. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Parquet reads only the three columns in the query.
- **B:** Correct. Parquet is columnar and compressed, so a scan reads only the columns a query needs. In this case: Parquet reads only the three columns in the query.
- **C:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: Parquet reads only the three columns in the query.
- **D:** Incorrect for this question. XML nests well and is verbose, which makes it a poor fit for wide analytical scans. Why the correct answer wins: Parquet reads only the three columns in the query.

### Question 14 — B

Answer: Land the data as Avro. Avro enforces and carries the writer's schema with each record. Avro carries its schema with the records and suits row-oriented streaming exchanges. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ORC is another columnar format; choosing it adds a conversion step without a benefit over Parquet here. Why the correct answer wins: Avro enforces and carries the writer's schema with each record.
- **B:** Correct. Avro carries its schema with the records and suits row-oriented streaming exchanges. In this case: Avro enforces and carries the writer's schema with each record.
- **C:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: Avro enforces and carries the writer's schema with each record.
- **D:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Avro enforces and carries the writer's schema with each record.

### Question 15 — C

Answer: Land the data as newline-delimited JSON. Newline-delimited JSON tolerates optional and differing fields per record. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Newline-delimited JSON tolerates optional and differing fields per record.
- **B:** Incorrect for this question. ORC is another columnar format; choosing it adds a conversion step without a benefit over Parquet here. Why the correct answer wins: Newline-delimited JSON tolerates optional and differing fields per record.
- **C:** Correct. Newline-delimited JSON keeps nested fields and can be appended one record at a time. In this case: Newline-delimited JSON tolerates optional and differing fields per record.
- **D:** Incorrect for this question. Avro carries its schema with the records and suits row-oriented streaming exchanges. Why the correct answer wins: Newline-delimited JSON tolerates optional and differing fields per record.

### Question 16 — A

Answer: Land the data as CSV. CSV is editable in a spreadsheet and needs no tooling. CSV is readable everywhere and carries no types, no schema, and no nesting. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. CSV is readable everywhere and carries no types, no schema, and no nesting. In this case: CSV is editable in a spreadsheet and needs no tooling.
- **B:** Incorrect for this question. Avro carries its schema with the records and suits row-oriented streaming exchanges. Why the correct answer wins: CSV is editable in a spreadsheet and needs no tooling.
- **C:** Incorrect for this question. ORC is another columnar format; choosing it adds a conversion step without a benefit over Parquet here. Why the correct answer wins: CSV is editable in a spreadsheet and needs no tooling.
- **D:** Incorrect for this question. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Why the correct answer wins: CSV is editable in a spreadsheet and needs no tooling.

### Question 17 — C

Answer: Load the files with the bq load command. A load job reads the compressed files and appends the rows. The bq load command creates a load job that reads files from Cloud Storage into a table. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: A load job reads the compressed files and appends the rows.
- **B:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: A load job reads the compressed files and appends the rows.
- **C:** Correct. The bq load command creates a load job that reads files from Cloud Storage into a table. In this case: A load job reads the compressed files and appends the rows.
- **D:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A load job reads the compressed files and appends the rows.

### Question 18 — B

Answer: Build the pipeline in Dataflow. A Dataflow pipeline writes each message to the raw archive before the transform. Dataflow runs the same code for streaming and batch and scales the workers with the load. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: A Dataflow pipeline writes each message to the raw archive before the transform.
- **B:** Correct. Dataflow runs the same code for streaming and batch and scales the workers with the load. In this case: A Dataflow pipeline writes each message to the raw archive before the transform.
- **C:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A Dataflow pipeline writes each message to the raw archive before the transform.
- **D:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: A Dataflow pipeline writes each message to the raw archive before the transform.

### Question 19 — D

Answer: Load the rows with a client library from the application. A client library writes the rows the worker holds. A client library suits an application that already holds the rows in memory rather than files in a bucket. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A client library writes the rows the worker holds.
- **B:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A client library writes the rows the worker holds.
- **C:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: A client library writes the rows the worker holds.
- **D:** Correct. A client library suits an application that already holds the rows in memory rather than files in a bucket. In this case: A client library writes the rows the worker holds.

### Question 20 — B

Answer: Store the rows in Bigtable. Bigtable takes keyed writes and reads at very high rate. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: Bigtable takes keyed writes and reads at very high rate.
- **B:** Correct. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. In this case: Bigtable takes keyed writes and reads at very high rate.
- **C:** Incorrect for this question. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Why the correct answer wins: Bigtable takes keyed writes and reads at very high rate.
- **D:** Incorrect for this question. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Why the correct answer wins: Bigtable takes keyed writes and reads at very high rate.

### Question 21 — B

Answer: Store the records in Cloud SQL. Cloud SQL is a managed relational database for transaction workloads. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Spanner gives strongly consistent relational transactions across regions at global scale. Why the correct answer wins: Cloud SQL is a managed relational database for transaction workloads.
- **B:** Correct. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. In this case: Cloud SQL is a managed relational database for transaction workloads.
- **C:** Incorrect for this question. AlloyDB is a managed PostgreSQL option for transaction workloads that want PostgreSQL compatibility. Why the correct answer wins: Cloud SQL is a managed relational database for transaction workloads.
- **D:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: Cloud SQL is a managed relational database for transaction workloads.

### Question 22 — C

Answer: Store the records in AlloyDB for PostgreSQL. AlloyDB is a managed PostgreSQL option for a heavier workload. AlloyDB is a managed PostgreSQL option for transaction workloads that want PostgreSQL compatibility. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Why the correct answer wins: AlloyDB is a managed PostgreSQL option for a heavier workload.
- **B:** Incorrect for this question. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Why the correct answer wins: AlloyDB is a managed PostgreSQL option for a heavier workload.
- **C:** Correct. AlloyDB is a managed PostgreSQL option for transaction workloads that want PostgreSQL compatibility. In this case: AlloyDB is a managed PostgreSQL option for a heavier workload.
- **D:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: AlloyDB is a managed PostgreSQL option for a heavier workload.

### Question 23 — D, E

Answers: Store the rows in BigQuery; Store the files in Cloud Storage. BigQuery serves the curated tables, and Cloud Storage keeps the raw files. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Cloud Storage holds objects of any shape and is the landing zone every other service can read. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: BigQuery serves the curated tables, and Cloud Storage keeps the raw files.
- **B:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: BigQuery serves the curated tables, and Cloud Storage keeps the raw files.
- **C:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: BigQuery serves the curated tables, and Cloud Storage keeps the raw files.
- **D:** Correct. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. In this case: BigQuery serves the curated tables, and Cloud Storage keeps the raw files.
- **E:** Correct. Cloud Storage holds objects of any shape and is the landing zone every other service can read. In this case: BigQuery serves the curated tables, and Cloud Storage keeps the raw files.

### Question 24 — A

Answer: Place the data in the region nearest the largest user base. Placing the data near the readers removes the distance from every query. Distance between the data and the readers shows up as latency on every query. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Distance between the data and the readers shows up as latency on every query. In this case: Placing the data near the readers removes the distance from every query.
- **B:** Incorrect for this question. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Why the correct answer wins: Placing the data near the readers removes the distance from every query.
- **C:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: Placing the data near the readers removes the distance from every query.
- **D:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: Placing the data near the readers removes the distance from every query.

### Question 25 — A

Answer: Choose a regional location. One region is the cheapest placement for a single metro. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. In this case: One region is the cheapest placement for a single metro.
- **B:** Incorrect for this question. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Why the correct answer wins: One region is the cheapest placement for a single metro.
- **C:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: One region is the cheapest placement for a single metro.
- **D:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: One region is the cheapest placement for a single metro.

### Question 26 — A, B

Answers: Place the data in the region the regulator names; Choose a regional location. Residency fixes the country, and a single region meets the latency without paying for copies. A residency obligation fixes the geography, which removes the choice from the performance discussion. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. In this case: Residency fixes the country, and a single region meets the latency without paying for copies.
- **B:** Correct. A residency obligation fixes the geography, which removes the choice from the performance discussion. In this case: Residency fixes the country, and a single region meets the latency without paying for copies.
- **C:** Incorrect for this question. Distance between the data and the readers shows up as latency on every query. Why the correct answer wins: Residency fixes the country, and a single region meets the latency without paying for copies.
- **D:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: Residency fixes the country, and a single region meets the latency without paying for copies.
- **E:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: Residency fixes the country, and a single region meets the latency without paying for copies.

### Question 27 — A

Answer: Treat the records as structured data. Typed columns under a header form structured data. Structured data fits a declared schema of rows and columns. Local study-map skill 1.8 (Structured, Semi-Structured, and Unstructured Data), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Structured data fits a declared schema of rows and columns. In this case: Typed columns under a header form structured data.
- **B:** Incorrect for this question. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Why the correct answer wins: Typed columns under a header form structured data.
- **C:** Incorrect for this question. Unstructured data has no field model at all, such as images, audio, or free documents. Why the correct answer wins: Typed columns under a header form structured data.
- **D:** Incorrect for this question. Semi-structured data has a flexible shape such as JSON, where fields vary between records. Why the correct answer wins: Typed columns under a header form structured data.

### Question 28 — C

Answer: Treat the files as unstructured data. Scans and photographs have no field model, which makes them unstructured. Unstructured data has no field model at all, such as images, audio, or free documents. Local study-map skill 1.8 (Structured, Semi-Structured, and Unstructured Data), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Semi-structured data has a flexible shape such as JSON, where fields vary between records. Why the correct answer wins: Scans and photographs have no field model, which makes them unstructured.
- **B:** Incorrect for this question. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Why the correct answer wins: Scans and photographs have no field model, which makes them unstructured.
- **C:** Correct. Unstructured data has no field model at all, such as images, audio, or free documents. In this case: Scans and photographs have no field model, which makes them unstructured.
- **D:** Incorrect for this question. Structured data fits a declared schema of rows and columns. Why the correct answer wins: Scans and photographs have no field model, which makes them unstructured.

### Question 29 — B

Answer: Stream the rows with the BigQuery Storage Write API. The Storage Write API commits rows as they are produced. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Local study-map skill 1.9 (Loading with CLIs and Client Libraries), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: The Storage Write API commits rows as they are produced.
- **B:** Correct. The Storage Write API commits rows at high rate when a stream, not a file, produces them. In this case: The Storage Write API commits rows as they are produced.
- **C:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: The Storage Write API commits rows as they are produced.
- **D:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: The Storage Write API commits rows as they are produced.

### Question 30 — D

Answer: Copy the objects with the gcloud storage command. A gcloud storage copy publishes the fixtures from the release step. A gcloud storage copy is the direct path for an ad hoc move between buckets. Local study-map skill 1.9 (Loading with CLIs and Client Libraries), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: A gcloud storage copy publishes the fixtures from the release step.
- **B:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: A gcloud storage copy publishes the fixtures from the release step.
- **C:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A gcloud storage copy publishes the fixtures from the release step.
- **D:** Correct. A gcloud storage copy is the direct path for an ad hoc move between buckets. In this case: A gcloud storage copy publishes the fixtures from the release step.

### Question 31 — A

Answer: Create a BigQuery view over the join. A view projects the exposed columns and reads the table beneath it. A view stores the query rather than the rows, so the answer stays current at query time. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A view stores the query rather than the rows, so the answer stays current at query time. In this case: A view projects the exposed columns and reads the table beneath it.
- **B:** Incorrect for this question. A native table gives the warehouse its own copy and the best scan performance. Why the correct answer wins: A view projects the exposed columns and reads the table beneath it.
- **C:** Incorrect for this question. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. Why the correct answer wins: A view projects the exposed columns and reads the table beneath it.
- **D:** Incorrect for this question. An external table reads the objects where they sit and does not copy them into storage. Why the correct answer wins: A view projects the exposed columns and reads the table beneath it.

### Question 32 — C

Answer: Create a BigQuery materialized view. A materialized view stores the aggregate and refreshes it. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A native table gives the warehouse its own copy and the best scan performance. Why the correct answer wins: A materialized view stores the aggregate and refreshes it.
- **B:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: A materialized view stores the aggregate and refreshes it.
- **C:** Correct. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. In this case: A materialized view stores the aggregate and refreshes it.
- **D:** Incorrect for this question. A view stores the query rather than the rows, so the answer stays current at query time. Why the correct answer wins: A materialized view stores the aggregate and refreshes it.

### Question 33 — B, C

Answers: Create a BigQuery materialized view; Filter the query on the partition column. The materialized view stores the repeated aggregate, and the partition filter narrows the scan. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. A partition filter restricts the scan to the partitions the query needs. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The materialized view stores the repeated aggregate, and the partition filter narrows the scan.
- **B:** Correct. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. In this case: The materialized view stores the repeated aggregate, and the partition filter narrows the scan.
- **C:** Correct. A partition filter restricts the scan to the partitions the query needs. In this case: The materialized view stores the repeated aggregate, and the partition filter narrows the scan.
- **D:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: The materialized view stores the repeated aggregate, and the partition filter narrows the scan.
- **E:** Incorrect for this question. An external table reads the objects where they sit and does not copy them into storage. Why the correct answer wins: The materialized view stores the repeated aggregate, and the partition filter narrows the scan.

### Question 34 — C

Answer: Query the files through an external table. An external table reads the objects where they sit without a copy. An external table reads the objects where they sit and does not copy them into storage. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A view stores the query rather than the rows, so the answer stays current at query time. Why the correct answer wins: An external table reads the objects where they sit without a copy.
- **B:** Incorrect for this question. A native table gives the warehouse its own copy and the best scan performance. Why the correct answer wins: An external table reads the objects where they sit without a copy.
- **C:** Correct. An external table reads the objects where they sit and does not copy them into storage. In this case: An external table reads the objects where they sit without a copy.
- **D:** Incorrect for this question. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. Why the correct answer wins: An external table reads the objects where they sit without a copy.

### Question 35 — D

Answer: Analyse the data in a Colab Enterprise notebook. Colab Enterprise gives a hosted runtime with VPC connectivity and project IAM. Colab Enterprise gives a managed notebook runtime with project IAM and BigQuery access. Local study-map skill 2.2 (Colab Enterprise and Jupyter Notebooks), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Colab Enterprise gives a hosted runtime with VPC connectivity and project IAM.
- **B:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: Colab Enterprise gives a hosted runtime with VPC connectivity and project IAM.
- **C:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: Colab Enterprise gives a hosted runtime with VPC connectivity and project IAM.
- **D:** Correct. Colab Enterprise gives a managed notebook runtime with project IAM and BigQuery access. In this case: Colab Enterprise gives a hosted runtime with VPC connectivity and project IAM.

### Question 36 — A

Answer: Query BigQuery from the notebook with the %%bigquery magic. The BigQuery magic runs the SQL in the cell and returns a DataFrame. The magic returns a DataFrame from a SQL statement inside the notebook cell. Local study-map skill 2.2 (Colab Enterprise and Jupyter Notebooks), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. The magic returns a DataFrame from a SQL statement inside the notebook cell. In this case: The BigQuery magic runs the SQL in the cell and returns a DataFrame.
- **B:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: The BigQuery magic runs the SQL in the cell and returns a DataFrame.
- **C:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: The BigQuery magic runs the SQL in the cell and returns a DataFrame.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: The BigQuery magic runs the SQL in the cell and returns a DataFrame.

### Question 37 — C

Answer: Write a SQL query in BigQuery and save the result. A SQL query answers the question and can be re-run for another SKU. A saved SQL query answers a business question and can be scheduled or exported. Local study-map skill 2.3 (Business Question Analysis), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: A SQL query answers the question and can be re-run for another SKU.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A SQL query answers the question and can be re-run for another SKU.
- **C:** Correct. A saved SQL query answers a business question and can be scheduled or exported. In this case: A SQL query answers the question and can be re-run for another SKU.
- **D:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A SQL query answers the question and can be re-run for another SKU.

### Question 38 — B

Answer: Share the dashboard with a scheduled delivery. A scheduled delivery pushes the answer to the distribution list. A scheduled delivery pushes the answer to people who will not open the tool. Local study-map skill 2.3 (Business Question Analysis), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A scheduled delivery pushes the answer to the distribution list.
- **B:** Correct. A scheduled delivery pushes the answer to people who will not open the tool. In this case: A scheduled delivery pushes the answer to the distribution list.
- **C:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A scheduled delivery pushes the answer to the distribution list.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A scheduled delivery pushes the answer to the distribution list.

### Question 39 — A

Answer: Build a governed Looker dashboard. A Looker dashboard inherits the model for every tile. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: A Looker dashboard inherits the model for every tile.
- **B:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A Looker dashboard inherits the model for every tile.
- **C:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: A Looker dashboard inherits the model for every tile.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A Looker dashboard inherits the model for every tile.

### Question 40 — C

Answer: Add a LookML measure for the calculation. A shared measure declares the formula once. A measure declares the aggregation once so every report computes it the same way. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A shared measure declares the formula once.
- **B:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: A shared measure declares the formula once.
- **C:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: A shared measure declares the formula once.
- **D:** Incorrect for this question. An explore defines which joins and fields a report author may use. Why the correct answer wins: A shared measure declares the formula once.

### Question 41 — C, D

Answers: Build a governed Looker dashboard; Add a LookML measure for the calculation. The Looker dashboard provides the surface, and the measure provides the certified metric. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. A measure declares the aggregation once so every report computes it the same way. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: The Looker dashboard provides the surface, and the measure provides the certified metric.
- **B:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: The Looker dashboard provides the surface, and the measure provides the certified metric.
- **C:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: The Looker dashboard provides the surface, and the measure provides the certified metric.
- **D:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: The Looker dashboard provides the surface, and the measure provides the certified metric.
- **E:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The Looker dashboard provides the surface, and the measure provides the certified metric.

### Question 42 — A

Answer: Build a Looker Studio report. Looker Studio connects a sheet quickly without modelling work. Looker Studio is the fast self-serve reporting surface for a small number of sources. Local study-map skill 2.5 (Looker and Looker Studio Comparison), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Looker Studio is the fast self-serve reporting surface for a small number of sources. In this case: Looker Studio connects a sheet quickly without modelling work.
- **B:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Looker Studio connects a sheet quickly without modelling work.
- **C:** Incorrect for this question. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Why the correct answer wins: Looker Studio connects a sheet quickly without modelling work.
- **D:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: Looker Studio connects a sheet quickly without modelling work.

### Question 43 — D

Answer: Build a governed Looker dashboard. Looker serves every report from one governed model. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Local study-map skill 2.5 (Looker and Looker Studio Comparison), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Looker serves every report from one governed model.
- **B:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: Looker serves every report from one governed model.
- **C:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: Looker serves every report from one governed model.
- **D:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: Looker serves every report from one governed model.

### Question 44 — D

Answer: Change the LookML parameter in the view. A LookML parameter changes the calendar for every consumer. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: A LookML parameter changes the calendar for every consumer.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A LookML parameter changes the calendar for every consumer.
- **C:** Incorrect for this question. An explore defines which joins and fields a report author may use. Why the correct answer wins: A LookML parameter changes the calendar for every consumer.
- **D:** Correct. A LookML parameter changes the model for every dashboard that uses it rather than one tile. In this case: A LookML parameter changes the calendar for every consumer.

### Question 45 — A

Answer: Add a LookML measure for the calculation. A measure declares the ratio once. A measure declares the aggregation once so every report computes it the same way. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: A measure declares the ratio once.
- **B:** Incorrect for this question. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Why the correct answer wins: A measure declares the ratio once.
- **C:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A measure declares the ratio once.
- **D:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: A measure declares the ratio once.

### Question 46 — A

Answer: Expose the table through a LookML explore. An explore declares which joins a report author may use. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: An explore declares which joins a report author may use.
- **B:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: An explore declares which joins a report author may use.
- **C:** Incorrect for this question. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Why the correct answer wins: An explore declares which joins a report author may use.
- **D:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: An explore declares which joins a report author may use.

### Question 47 — D

Answer: Train a BigQuery ML logistic regression model. Logistic regression returns a probability for a binary outcome. Logistic regression predicts a binary outcome and trains with SQL against the table. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ARIMA_PLUS forecasts a series and returns an interval per period. Why the correct answer wins: Logistic regression returns a probability for a binary outcome.
- **B:** Incorrect for this question. ML.PREDICT applies a trained model to new rows and returns the prediction. Why the correct answer wins: Logistic regression returns a probability for a binary outcome.
- **C:** Incorrect for this question. Linear regression predicts a continuous value and trains with SQL against the table. Why the correct answer wins: Logistic regression returns a probability for a binary outcome.
- **D:** Correct. Logistic regression predicts a binary outcome and trains with SQL against the table. In this case: Logistic regression returns a probability for a binary outcome.

### Question 48 — B

Answer: Train a BigQuery ML k-means model. K-means discovers groups without a labelled outcome. K-means groups rows without a label column, so it segments rather than predicts. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ARIMA_PLUS forecasts a series and returns an interval per period. Why the correct answer wins: K-means discovers groups without a labelled outcome.
- **B:** Correct. K-means groups rows without a label column, so it segments rather than predicts. In this case: K-means discovers groups without a labelled outcome.
- **C:** Incorrect for this question. Logistic regression predicts a binary outcome and trains with SQL against the table. Why the correct answer wins: K-means discovers groups without a labelled outcome.
- **D:** Incorrect for this question. AutoML searches architectures and tuning for a team that has labels but no modelling code. Why the correct answer wins: K-means discovers groups without a labelled outcome.

### Question 49 — A, E

Answers: Train an AutoML tabular model; Train a BigQuery ML ARIMA_PLUS model. AutoML searches architectures for the team, and ARIMA_PLUS forecasts the series. AutoML searches architectures and tuning for a team that has labels but no modelling code. ARIMA_PLUS forecasts a series and returns an interval per period. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. ARIMA_PLUS forecasts a series and returns an interval per period. In this case: AutoML searches architectures for the team, and ARIMA_PLUS forecasts the series.
- **B:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: AutoML searches architectures for the team, and ARIMA_PLUS forecasts the series.
- **C:** Incorrect for this question. Logistic regression predicts a binary outcome and trains with SQL against the table. Why the correct answer wins: AutoML searches architectures for the team, and ARIMA_PLUS forecasts the series.
- **D:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: AutoML searches architectures for the team, and ARIMA_PLUS forecasts the series.
- **E:** Correct. AutoML searches architectures and tuning for a team that has labels but no modelling code. In this case: AutoML searches architectures for the team, and ARIMA_PLUS forecasts the series.

### Question 50 — C

Answer: Create a BigQuery remote model over a Gemini model. A remote model runs the prompt from SQL where the rows already sit. A remote model sends the prompt to Gemini from SQL while the rows stay in BigQuery. Local study-map skill 2.8 (Remote Gemini Models in BigQuery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: A remote model runs the prompt from SQL where the rows already sit.
- **B:** Incorrect for this question. Fine-tuning adapts the model to the domain using labelled rows that stay in BigQuery. Why the correct answer wins: A remote model runs the prompt from SQL where the rows already sit.
- **C:** Correct. A remote model sends the prompt to Gemini from SQL while the rows stay in BigQuery. In this case: A remote model runs the prompt from SQL where the rows already sit.
- **D:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: A remote model runs the prompt from SQL where the rows already sit.

### Question 51 — D

Answer: Create the BigQuery connection that reaches the model endpoint. The connection carries the service account that calls the model endpoint. The connection carries the service account that BigQuery uses to call the remote model. Local study-map skill 2.8 (Remote Gemini Models in BigQuery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: The connection carries the service account that calls the model endpoint.
- **B:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: The connection carries the service account that calls the model endpoint.
- **C:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: The connection carries the service account that calls the model endpoint.
- **D:** Correct. The connection carries the service account that BigQuery uses to call the remote model. In this case: The connection carries the service account that calls the model endpoint.

### Question 52 — B

Answer: Plan collection, training, evaluation, then prediction. A plan fixes the stages and the acceptance test before training. A planned sequence fixes the data, the metric, and the acceptance test before any model is trained. Local study-map skill 2.9 (ML Project Planning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A plan fixes the stages and the acceptance test before training.
- **B:** Correct. A planned sequence fixes the data, the metric, and the acceptance test before any model is trained. In this case: A plan fixes the stages and the acceptance test before training.
- **C:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: A plan fixes the stages and the acceptance test before training.
- **D:** Incorrect for this question. Training loss measures fit to the rows it has already seen, not the answer on new rows. Why the correct answer wins: A plan fixes the stages and the acceptance test before training.

### Question 53 — A, C

Answers: Hold out whole entities so none spans both splits; Hold out a labelled split before training. The grouped split holds the account out, and the held-out split produces an unseen-rows score. A grouped split keeps one customer from appearing on both sides of the evaluation. A held-out split gives an estimate that the training rows cannot inflate. Local study-map skill 2.9 (ML Project Planning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A grouped split keeps one customer from appearing on both sides of the evaluation. In this case: The grouped split holds the account out, and the held-out split produces an unseen-rows score.
- **B:** Incorrect for this question. Training loss measures fit to the rows it has already seen, not the answer on new rows. Why the correct answer wins: The grouped split holds the account out, and the held-out split produces an unseen-rows score.
- **C:** Correct. A held-out split gives an estimate that the training rows cannot inflate. In this case: The grouped split holds the account out, and the held-out split produces an unseen-rows score.
- **D:** Incorrect for this question. A time-ordered split tests the model on rows that come after the ones it learned from. Why the correct answer wins: The grouped split holds the account out, and the held-out split produces an unseen-rows score.
- **E:** Incorrect for this question. A profile quantifies what is missing before the gaps reach a dashboard. Why the correct answer wins: The grouped split holds the account out, and the held-out split produces an unseen-rows score.

### Question 54 — D

Answer: Evaluate the model with ML.EVALUATE. ML.EVALUATE returns the metrics against a labelled dataset. Local study-map skill 2.10 (BigQuery ML Training and Evaluation), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.PREDICT applies a trained model to new rows and returns the prediction. Why the correct answer wins: ML.EVALUATE returns the metrics against a labelled dataset.
- **B:** Incorrect for this question. ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row. Why the correct answer wins: ML.EVALUATE returns the metrics against a labelled dataset.
- **C:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: ML.EVALUATE returns the metrics against a labelled dataset.
- **D:** Correct. In this case: ML.EVALUATE returns the metrics against a labelled dataset.

### Question 55 — B

Answer: Hold out a labelled split before training. A held-out split measures the answer on unseen rows. A held-out split gives an estimate that the training rows cannot inflate. Local study-map skill 2.10 (BigQuery ML Training and Evaluation), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A wide table removes the join, at the cost of duplicated rows and a wider scan. Why the correct answer wins: A held-out split measures the answer on unseen rows.
- **B:** Correct. A held-out split gives an estimate that the training rows cannot inflate. In this case: A held-out split measures the answer on unseen rows.
- **C:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: A held-out split measures the answer on unseen rows.
- **D:** Incorrect for this question. Training loss measures fit to the rows it has already seen, not the answer on new rows. Why the correct answer wins: A held-out split measures the answer on unseen rows.

### Question 56 — B

Answer: Generate the forecast with ML.FORECAST. ML.FORECAST returns the future periods and their intervals. ML.FORECAST returns future periods and their intervals from a time series model. Local study-map skill 2.11 (BigQuery ML Inference), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.PREDICT applies a trained model to new rows and returns the prediction. Why the correct answer wins: ML.FORECAST returns the future periods and their intervals.
- **B:** Correct. ML.FORECAST returns future periods and their intervals from a time series model. In this case: ML.FORECAST returns the future periods and their intervals.
- **C:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: ML.FORECAST returns the future periods and their intervals.
- **D:** Incorrect for this question. ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row. Why the correct answer wins: ML.FORECAST returns the future periods and their intervals.

### Question 57 — A

Answer: Register the model version in Model Registry. Model Registry names the version that produced a given output. Model Registry keeps each version with its lineage so a deployment names a version rather than a path. Local study-map skill 2.12 (Model Registry), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Model Registry keeps each version with its lineage so a deployment names a version rather than a path. In this case: Model Registry names the version that produced a given output.
- **B:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Model Registry names the version that produced a given output.
- **C:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: Model Registry names the version that produced a given output.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: Model Registry names the version that produced a given output.

### Question 58 — A

Answer: Manage the SQL transformations in Dataform. Dataform versions the SQL and runs the tests before promotion. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. In this case: Dataform versions the SQL and runs the tests before promotion.
- **B:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Dataform versions the SQL and runs the tests before promotion.
- **C:** Incorrect for this question. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Why the correct answer wins: Dataform versions the SQL and runs the tests before promotion.
- **D:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Dataform versions the SQL and runs the tests before promotion.

### Question 59 — D

Answer: Build the pipeline in Dataflow. Dataflow applies the window and the watermark to the unordered stream. Dataflow runs the same code for streaming and batch and scales the workers with the load. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Dataflow applies the window and the watermark to the unordered stream.
- **B:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Dataflow applies the window and the watermark to the unordered stream.
- **C:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Dataflow applies the window and the watermark to the unordered stream.
- **D:** Correct. Dataflow runs the same code for streaming and batch and scales the workers with the load. In this case: Dataflow applies the window and the watermark to the unordered stream.

### Question 60 — B

Answer: Run the transformation as Spark on Dataproc. Dataproc runs the existing Hadoop and Spark code without a rewrite. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Dataproc runs the existing Hadoop and Spark code without a rewrite.
- **B:** Correct. Dataproc runs Spark or Hadoop jobs when the team already owns that code. In this case: Dataproc runs the existing Hadoop and Spark code without a rewrite.
- **C:** Incorrect for this question. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. Why the correct answer wins: Dataproc runs the existing Hadoop and Spark code without a rewrite.
- **D:** Incorrect for this question. Dataflow runs the same code for streaming and batch and scales the workers with the load. Why the correct answer wins: Dataproc runs the existing Hadoop and Spark code without a rewrite.

### Question 61 — A, C

Answers: Build the pipeline in Dataflow; Build the pipeline in Cloud Data Fusion. Dataflow gives one definition for streaming and batch, and Data Fusion builds the joins visually. Dataflow runs the same code for streaming and batch and scales the workers with the load. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Dataflow runs the same code for streaming and batch and scales the workers with the load. In this case: Dataflow gives one definition for streaming and batch, and Data Fusion builds the joins visually.
- **B:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Dataflow gives one definition for streaming and batch, and Data Fusion builds the joins visually.
- **C:** Correct. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. In this case: Dataflow gives one definition for streaming and batch, and Data Fusion builds the joins visually.
- **D:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Dataflow gives one definition for streaming and batch, and Data Fusion builds the joins visually.
- **E:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: Dataflow gives one definition for streaming and batch, and Data Fusion builds the joins visually.

### Question 62 — C

Answer: Load the raw rows, then transform them inside the warehouse. ELT loads the raw rows and lets the warehouse engine do the joins. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 3.2 (ELT and ETL Pipeline Design), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ELT loads the raw rows and lets the warehouse engine do the joins.
- **B:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT loads the raw rows and lets the warehouse engine do the joins.
- **C:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT loads the raw rows and lets the warehouse engine do the joins.
- **D:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ELT loads the raw rows and lets the warehouse engine do the joins.

### Question 63 — D

Answer: Extract, transform outside the warehouse, then load the result. ETL masks the record before any layer stores it. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Local study-map skill 3.2 (ELT and ETL Pipeline Design), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: ETL masks the record before any layer stores it.
- **B:** Incorrect for this question. A staging table separates a failed load from a failed transform, so each can be retried on its own. Why the correct answer wins: ETL masks the record before any layer stores it.
- **C:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETL masks the record before any layer stores it.
- **D:** Correct. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. In this case: ETL masks the record before any layer stores it.

### Question 64 — A

Answer: Schedule the SQL with a BigQuery scheduled query. A scheduled query runs one statement on a cron schedule. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A scheduled query runs one statement on a cron schedule.
- **B:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **C:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **D:** Incorrect for this question. A workflow template defines the cluster and the steps so the same job can be re-run identically. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.

### Question 65 — A

Answer: Re-run the scheduled query with a wider date range. A backfill re-reads the skipped window rather than waiting for the next run. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A backfill re-reads the skipped window rather than waiting for the next run.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A backfill re-reads the skipped window rather than waiting for the next run.
- **C:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A backfill re-reads the skipped window rather than waiting for the next run.
- **D:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: A backfill re-reads the skipped window rather than waiting for the next run.

### Question 66 — B, C

Answers: Trigger the job from Cloud Scheduler; Schedule the SQL with a BigQuery scheduled query. The scheduled query owns the statement, and the scheduler owns the endpoint call. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. A scheduled query runs one statement on a cron schedule and writes its result. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: The scheduled query owns the statement, and the scheduler owns the endpoint call.
- **B:** Correct. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. In this case: The scheduled query owns the statement, and the scheduler owns the endpoint call.
- **C:** Correct. A scheduled query runs one statement on a cron schedule and writes its result. In this case: The scheduled query owns the statement, and the scheduler owns the endpoint call.
- **D:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: The scheduled query owns the statement, and the scheduler owns the endpoint call.
- **E:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: The scheduled query owns the statement, and the scheduler owns the endpoint call.

### Question 67 — A

Answer: Watch the job graph and per-step throughput in the Dataflow console. The job view shows the throughput and watermark of every stage. The Dataflow job view shows the running graph, watermarks, and the step that is backlogged. Local study-map skill 3.4 (Dataflow Job Monitoring), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. The Dataflow job view shows the running graph, watermarks, and the step that is backlogged. In this case: The job view shows the throughput and watermark of every stage.
- **B:** Incorrect for this question. Logs Explorer filters the log entries that explain why a worker restarted. Why the correct answer wins: The job view shows the throughput and watermark of every stage.
- **C:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: The job view shows the throughput and watermark of every stage.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The job view shows the throughput and watermark of every stage.

### Question 68 — C

Answer: Write the rejected rows to a dead-letter table. A dead-letter table keeps the rejected events for replay. A dead-letter table preserves the rows that failed so they can be repaired and replayed. Local study-map skill 3.4 (Dataflow Job Monitoring), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A dead-letter table keeps the rejected events for replay.
- **B:** Incorrect for this question. A wide table removes the join, at the cost of duplicated rows and a wider scan. Why the correct answer wins: A dead-letter table keeps the rejected events for replay.
- **C:** Correct. A dead-letter table preserves the rows that failed so they can be repaired and replayed. In this case: A dead-letter table keeps the rejected events for replay.
- **D:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A dead-letter table keeps the rejected events for replay.

### Question 69 — D

Answer: Query the job logs in Logs Explorer. Logs Explorer filters the entries from that window. Logs Explorer filters the log entries that explain why a worker restarted. Local study-map skill 3.5 (Logs and Monitoring Review), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: Logs Explorer filters the entries from that window.
- **B:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: Logs Explorer filters the entries from that window.
- **C:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Logs Explorer filters the entries from that window.
- **D:** Correct. Logs Explorer filters the log entries that explain why a worker restarted. In this case: Logs Explorer filters the entries from that window.

### Question 70 — C

Answer: Create a Cloud Monitoring alert policy on the job metric. An alert policy on the freshness metric pages the owner. An alert policy pages someone when the backlog or the failure rate crosses a threshold. Local study-map skill 3.5 (Logs and Monitoring Review), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: An alert policy on the freshness metric pages the owner.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: An alert policy on the freshness metric pages the owner.
- **C:** Correct. An alert policy pages someone when the backlog or the failure rate crosses a threshold. In this case: An alert policy on the freshness metric pages the owner.
- **D:** Incorrect for this question. Logs Explorer filters the log entries that explain why a worker restarted. Why the correct answer wins: An alert policy on the freshness metric pages the owner.

### Question 71 — B

Answer: Orchestrate the steps in Cloud Composer. Cloud Composer retries the wait, keeps the order, and records the run. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Cloud Composer retries the wait, keeps the order, and records the run.
- **B:** Correct. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. In this case: Cloud Composer retries the wait, keeps the order, and records the run.
- **C:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Cloud Composer retries the wait, keeps the order, and records the run.
- **D:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Cloud Composer retries the wait, keeps the order, and records the run.

### Question 72 — B

Answer: Submit the job through a Dataproc workflow template. A workflow template stores the cluster and the steps for an identical rerun. A workflow template defines the cluster and the steps so the same job can be re-run identically. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: A workflow template stores the cluster and the steps for an identical rerun.
- **B:** Correct. A workflow template defines the cluster and the steps so the same job can be re-run identically. In this case: A workflow template stores the cluster and the steps for an identical rerun.
- **C:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: A workflow template stores the cluster and the steps for an identical rerun.
- **D:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A workflow template stores the cluster and the steps for an identical rerun.

### Question 73 — A, C

Answers: Orchestrate the steps in Cloud Composer; Start the pipeline from an Eventarc trigger. Eventarc supplies the landing event, and Composer supplies the dependency order. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. In this case: Eventarc supplies the landing event, and Composer supplies the dependency order.
- **B:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Eventarc supplies the landing event, and Composer supplies the dependency order.
- **C:** Correct. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. In this case: Eventarc supplies the landing event, and Composer supplies the dependency order.
- **D:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Eventarc supplies the landing event, and Composer supplies the dependency order.
- **E:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Eventarc supplies the landing event, and Composer supplies the dependency order.

### Question 74 — D

Answer: Subscribe BigQuery to the Pub/Sub topic. A BigQuery subscription writes each message into the table. Local study-map skill 3.7 (Event-Driven Ingestion with Pub/Sub), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A BigQuery subscription writes each message into the table.
- **B:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: A BigQuery subscription writes each message into the table.
- **C:** Incorrect for this question. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Why the correct answer wins: A BigQuery subscription writes each message into the table.
- **D:** Correct. In this case: A BigQuery subscription writes each message into the table.

### Question 75 — B

Answer: Start the pipeline from an Eventarc trigger. An Eventarc trigger routes the storage event to the run target. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Local study-map skill 3.8 (Eventarc Triggers), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A BigQuery subscription writes each published message into a table as it arrives. Why the correct answer wins: An Eventarc trigger routes the storage event to the run target.
- **B:** Correct. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. In this case: An Eventarc trigger routes the storage event to the run target.
- **C:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: An Eventarc trigger routes the storage event to the run target.
- **D:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: An Eventarc trigger routes the storage event to the run target.

### Question 76 — C

Answer: Grant the predefined role that matches the task. The narrowest role that writes that dataset keeps the rest closed. A predefined role carries the permissions for one job and nothing else. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: The narrowest role that writes that dataset keeps the rest closed.
- **B:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: The narrowest role that writes that dataset keeps the rest closed.
- **C:** Correct. A predefined role carries the permissions for one job and nothing else. In this case: The narrowest role that writes that dataset keeps the rest closed.
- **D:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: The narrowest role that writes that dataset keeps the rest closed.

### Question 77 — A

Answer: Run the job as a dedicated service account. A service account gives the query an identity of its own. A service account gives the workload its own identity instead of borrowing a person's. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A service account gives the workload its own identity instead of borrowing a person's. In this case: A service account gives the query an identity of its own.
- **B:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A service account gives the query an identity of its own.
- **C:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: A service account gives the query an identity of its own.
- **D:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A service account gives the query an identity of its own.

### Question 78 — B

Answer: Add the project to a VPC Service Controls perimeter. A perimeter blocks the movement of data out of the boundary. A perimeter blocks data movement outside the boundary even for an authorised identity. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A perimeter blocks the movement of data out of the boundary.
- **B:** Correct. A perimeter blocks data movement outside the boundary even for an authorised identity. In this case: A perimeter blocks the movement of data out of the boundary.
- **C:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A perimeter blocks the movement of data out of the boundary.
- **D:** Incorrect for this question. An export hands over a copy that the publisher can no longer control or revoke. Why the correct answer wins: A perimeter blocks the movement of data out of the boundary.

### Question 79 — D

Answer: Assign a predefined role to the group. A predefined role matches that job without basic-role breadth. A predefined role is maintained by Google and covers one service or one job function. Local study-map skill 4.2 (Basic, Predefined, and Custom Roles), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A predefined role matches that job without basic-role breadth.
- **B:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A predefined role matches that job without basic-role breadth.
- **C:** Incorrect for this question. A custom role narrows the grant when no predefined role matches the job exactly. Why the correct answer wins: A predefined role matches that job without basic-role breadth.
- **D:** Correct. A predefined role is maintained by Google and covers one service or one job function. In this case: A predefined role matches that job without basic-role breadth.

### Question 80 — C, D

Answers: Assign a predefined role to the group; Create a custom role with only the permissions used. A predefined role is maintained by Google, and a custom role carries only what is used. A predefined role is maintained by Google and covers one service or one job function. A custom role narrows the grant when no predefined role matches the job exactly. Local study-map skill 4.2 (Basic, Predefined, and Custom Roles), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A predefined role is maintained by Google, and a custom role carries only what is used.
- **B:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A predefined role is maintained by Google, and a custom role carries only what is used.
- **C:** Correct. A predefined role is maintained by Google and covers one service or one job function. In this case: A predefined role is maintained by Google, and a custom role carries only what is used.
- **D:** Correct. A custom role narrows the grant when no predefined role matches the job exactly. In this case: A predefined role is maintained by Google, and a custom role carries only what is used.
- **E:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A predefined role is maintained by Google, and a custom role carries only what is used.

### Question 81 — D

Answer: Enable uniform bucket-level access. Uniform bucket-level access replaces the object ACLs with IAM. Local study-map skill 4.3 (Cloud Storage Access Control), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: Uniform bucket-level access replaces the object ACLs with IAM.
- **B:** Incorrect for this question. Per-object ACLs are hard to audit and are overridden when uniform access is enabled. Why the correct answer wins: Uniform bucket-level access replaces the object ACLs with IAM.
- **C:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Uniform bucket-level access replaces the object ACLs with IAM.
- **D:** Correct. In this case: Uniform bucket-level access replaces the object ACLs with IAM.

### Question 82 — A, D

Answers: Enable uniform bucket-level access; Manage per-object ACLs on the bucket. Uniform access keeps the default in IAM, and the per-object ACL carries the single exception. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. Per-object ACLs are hard to audit and are overridden when uniform access is enabled. Local study-map skill 4.3 (Cloud Storage Access Control), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. In this case: Uniform access keeps the default in IAM, and the per-object ACL carries the single exception.
- **B:** Incorrect for this question. An export hands over a copy that the publisher can no longer control or revoke. Why the correct answer wins: Uniform access keeps the default in IAM, and the per-object ACL carries the single exception.
- **C:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Uniform access keeps the default in IAM, and the per-object ACL carries the single exception.
- **D:** Correct. Per-object ACLs are hard to audit and are overridden when uniform access is enabled. In this case: Uniform access keeps the default in IAM, and the per-object ACL carries the single exception.
- **E:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: Uniform access keeps the default in IAM, and the per-object ACL carries the single exception.

### Question 83 — C

Answer: Publish the dataset through Analytics Hub. Analytics Hub lets the subscriber read the dataset in place. Analytics Hub shares a curated dataset with a subscriber who reads it in place. Local study-map skill 4.4 (Analytics Hub Data Sharing), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Analytics Hub lets the subscriber read the dataset in place.
- **B:** Incorrect for this question. An export hands over a copy that the publisher can no longer control or revoke. Why the correct answer wins: Analytics Hub lets the subscriber read the dataset in place.
- **C:** Correct. Analytics Hub shares a curated dataset with a subscriber who reads it in place. In this case: Analytics Hub lets the subscriber read the dataset in place.
- **D:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: Analytics Hub lets the subscriber read the dataset in place.

### Question 84 — C

Answer: Export the table to a bucket the partner owns. An export places the copy under the auditor's control. An export hands over a copy that the publisher can no longer control or revoke. Local study-map skill 4.4 (Analytics Hub Data Sharing), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A perimeter blocks data movement outside the boundary even for an authorised identity. Why the correct answer wins: An export places the copy under the auditor's control.
- **B:** Incorrect for this question. Analytics Hub shares a curated dataset with a subscriber who reads it in place. Why the correct answer wins: An export places the copy under the auditor's control.
- **C:** Correct. An export hands over a copy that the publisher can no longer control or revoke. In this case: An export places the copy under the auditor's control.
- **D:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: An export places the copy under the auditor's control.

### Question 85 — D

Answer: Move the objects to Coldline. Coldline suits a few reads a year with a longer minimum duration. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: Coldline suits a few reads a year with a longer minimum duration.
- **B:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Coldline suits a few reads a year with a longer minimum duration.
- **C:** Incorrect for this question. Archive is the cheapest class for data kept for compliance and read almost never. Why the correct answer wins: Coldline suits a few reads a year with a longer minimum duration.
- **D:** Correct. In this case: Coldline suits a few reads a year with a longer minimum duration.

### Question 86 — A

Answer: Enable Autoclass on the bucket. Autoclass moves each object as its access changes. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: Autoclass moves each object as its access changes.
- **B:** Incorrect for this question. Archive is the cheapest class for data kept for compliance and read almost never. Why the correct answer wins: Autoclass moves each object as its access changes.
- **C:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: Autoclass moves each object as its access changes.
- **D:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Autoclass moves each object as its access changes.

### Question 87 — A, C

Answers: Keep the objects in the Standard class; Add a lifecycle rule that changes the storage class. Standard keeps the hot reads instant, and the rule demotes the cold objects by age. Standard is for objects read frequently, where access cost matters more than storage cost. A setStorageClass rule demotes an object after a number of days so the cost falls without a copy. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Standard is for objects read frequently, where access cost matters more than storage cost. In this case: Standard keeps the hot reads instant, and the rule demotes the cold objects by age.
- **B:** Incorrect for this question. Keeping every version in the hot class pays the highest rate for data nobody reads. Why the correct answer wins: Standard keeps the hot reads instant, and the rule demotes the cold objects by age.
- **C:** Correct. A setStorageClass rule demotes an object after a number of days so the cost falls without a copy. In this case: Standard keeps the hot reads instant, and the rule demotes the cold objects by age.
- **D:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: Standard keeps the hot reads instant, and the rule demotes the cold objects by age.
- **E:** Incorrect for this question. Archive is the cheapest class for data kept for compliance and read almost never. Why the correct answer wins: Standard keeps the hot reads instant, and the rule demotes the cold objects by age.

### Question 88 — B

Answer: Add a lifecycle rule that deletes objects after the retention period. A lifecycle delete rule removes the object on age. A delete rule removes the objects once the retention period passes, without a person remembering. Local study-map skill 4.6 (Lifecycle Rules and Expiration), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: A lifecycle delete rule removes the object on age.
- **B:** Correct. A delete rule removes the objects once the retention period passes, without a person remembering. In this case: A lifecycle delete rule removes the object on age.
- **C:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A lifecycle delete rule removes the object on age.
- **D:** Incorrect for this question. Keeping every version in the hot class pays the highest rate for data nobody reads. Why the correct answer wins: A lifecycle delete rule removes the object on age.

### Question 89 — C

Answer: Set a table expiration on the dataset. Dataset-level expiration removes the tables created inside it. A dataset-level expiration removes tables created in it after the configured period. Local study-map skill 4.6 (Lifecycle Rules and Expiration), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: Dataset-level expiration removes the tables created inside it.
- **B:** Incorrect for this question. A delete rule removes the objects once the retention period passes, without a person remembering. Why the correct answer wins: Dataset-level expiration removes the tables created inside it.
- **C:** Correct. A dataset-level expiration removes tables created in it after the configured period. In this case: Dataset-level expiration removes the tables created inside it.
- **D:** Incorrect for this question. Partition expiration drops old partitions while the table keeps the recent ones. Why the correct answer wins: Dataset-level expiration removes the tables created inside it.

### Question 90 — C

Answer: Move the objects to Archive. Archive is the cheapest class for data read almost never. Local study-map skill 4.7 (Archiving Services), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: Archive is the cheapest class for data read almost never.
- **B:** Incorrect for this question. Coldline suits reads a few times a year and has a longer minimum storage duration. Why the correct answer wins: Archive is the cheapest class for data read almost never.
- **C:** Correct. In this case: Archive is the cheapest class for data read almost never.
- **D:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Archive is the cheapest class for data read almost never.

### Question 91 — D

Answer: Apply a bucket retention policy with a lock. A locked retention policy prevents deletion for the period. Local study-map skill 4.7 (Archiving Services), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A delete rule removes the objects once the retention period passes, without a person remembering. Why the correct answer wins: A locked retention policy prevents deletion for the period.
- **B:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A locked retention policy prevents deletion for the period.
- **C:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: A locked retention policy prevents deletion for the period.
- **D:** Correct. In this case: A locked retention policy prevents deletion for the period.

### Question 92 — D

Answer: Enable automated backups and point-in-time recovery on Cloud SQL. Point-in-time recovery restores the state to the chosen moment. Automated backups with point-in-time recovery restore the instance to a chosen moment. Local study-map skill 4.8 (Backup and Recovery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: Point-in-time recovery restores the state to the chosen moment.
- **B:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: Point-in-time recovery restores the state to the chosen moment.
- **C:** Incorrect for this question. A zonal instance is lost with its zone and gives no automatic failover. Why the correct answer wins: Point-in-time recovery restores the state to the chosen moment.
- **D:** Correct. Automated backups with point-in-time recovery restore the instance to a chosen moment. In this case: Point-in-time recovery restores the state to the chosen moment.

### Question 93 — B

Answer: Deploy the instance as regional with a standby. A regional instance keeps the standby in another zone. A regional instance fails over to a standby in another zone inside the same region. Local study-map skill 4.8 (Backup and Recovery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: A regional instance keeps the standby in another zone.
- **B:** Correct. A regional instance fails over to a standby in another zone inside the same region. In this case: A regional instance keeps the standby in another zone.
- **C:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A regional instance keeps the standby in another zone.
- **D:** Incorrect for this question. A zonal instance is lost with its zone and gives no automatic failover. Why the correct answer wins: A regional instance keeps the standby in another zone.

### Question 94 — D

Answer: Create a multi-region bucket. A multi-region bucket spreads the objects across the geography. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. Local study-map skill 4.9 (Replication), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dual-region bucket keeps a copy in a second region and reports the replication lag. Why the correct answer wins: A multi-region bucket spreads the objects across the geography.
- **B:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A multi-region bucket spreads the objects across the geography.
- **C:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A multi-region bucket spreads the objects across the geography.
- **D:** Correct. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. In this case: A multi-region bucket spreads the objects across the geography.

### Question 95 — A, D

Answers: Enable object versioning on the bucket; Create a dual-region bucket with a replication policy. Versioning restores the prior generation, and the dual-region bucket states the pair. Object versioning keeps a prior generation so an overwrite or delete can be reversed. A dual-region bucket keeps a copy in a second region and reports the replication lag. Local study-map skill 4.9 (Replication), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Object versioning keeps a prior generation so an overwrite or delete can be reversed. In this case: Versioning restores the prior generation, and the dual-region bucket states the pair.
- **B:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: Versioning restores the prior generation, and the dual-region bucket states the pair.
- **C:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: Versioning restores the prior generation, and the dual-region bucket states the pair.
- **D:** Correct. A dual-region bucket keeps a copy in a second region and reports the replication lag. In this case: Versioning restores the prior generation, and the dual-region bucket states the pair.
- **E:** Incorrect for this question. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. Why the correct answer wins: Versioning restores the prior generation, and the dual-region bucket states the pair.

### Question 96 — B

Answer: Choose a multi-region location. A multi-region location spreads the copies across the geography. A multi-region location spreads the data across a continent-scale geography for the widest availability. Local study-map skill 4.10 (Primary and Secondary Locations), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: A multi-region location spreads the copies across the geography.
- **B:** Correct. A multi-region location spreads the data across a continent-scale geography for the widest availability. In this case: A multi-region location spreads the copies across the geography.
- **C:** Incorrect for this question. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Why the correct answer wins: A multi-region location spreads the copies across the geography.
- **D:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: A multi-region location spreads the copies across the geography.

### Question 97 — A

Answer: Encrypt with a customer-managed key from Cloud KMS. A customer-managed key can be disabled by the tenant. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. Local study-map skill 4.11 (CMEK, CSEK, and GMEK), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. In this case: A customer-managed key can be disabled by the tenant.
- **B:** Incorrect for this question. A customer-supplied key never reaches Google, and losing it loses the object. Why the correct answer wins: A customer-managed key can be disabled by the tenant.
- **C:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: A customer-managed key can be disabled by the tenant.
- **D:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: A customer-managed key can be disabled by the tenant.

### Question 98 — B

Answer: Supply a customer-supplied key with each request. A customer-supplied key is provided per request and held by the client. A customer-supplied key never reaches Google, and losing it loses the object. Local study-map skill 4.11 (CMEK, CSEK, and GMEK), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key ring in the same region keeps the key and the ciphertext under the same residency rule. Why the correct answer wins: A customer-supplied key is provided per request and held by the client.
- **B:** Correct. A customer-supplied key never reaches Google, and losing it loses the object. In this case: A customer-supplied key is provided per request and held by the client.
- **C:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: A customer-supplied key is provided per request and held by the client.
- **D:** Incorrect for this question. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. Why the correct answer wins: A customer-supplied key is provided per request and held by the client.

### Question 99 — D

Answer: Create the key in a Cloud KMS key ring in the data region. A key ring per environment separates the keys and inventories them. A key ring in the same region keeps the key and the ciphertext under the same residency rule. Local study-map skill 4.12 (Cloud KMS), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A rotation schedule limits how long one key version protects new data. Why the correct answer wins: A key ring per environment separates the keys and inventories them.
- **B:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: A key ring per environment separates the keys and inventories them.
- **C:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: A key ring per environment separates the keys and inventories them.
- **D:** Correct. A key ring in the same region keeps the key and the ciphertext under the same residency rule. In this case: A key ring per environment separates the keys and inventories them.

### Question 100 — D

Answer: Confirm the data is encrypted at rest by the storage service. Encryption at rest keeps the stored bytes unreadable on the medium. Encryption at rest protects the stored bytes on the medium, not the connection that reads them. Local study-map skill 4.13 (Encryption in Transit and at Rest), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Encryption in transit protects the bytes while they are on the wire between client and service. Why the correct answer wins: Encryption at rest keeps the stored bytes unreadable on the medium.
- **B:** Incorrect for this question. A key stored beside the data protects nothing against anyone who can read the store. Why the correct answer wins: Encryption at rest keeps the stored bytes unreadable on the medium.
- **C:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: Encryption at rest keeps the stored bytes unreadable on the medium.
- **D:** Correct. Encryption at rest protects the stored bytes on the medium, not the connection that reads them. In this case: Encryption at rest keeps the stored bytes unreadable on the medium.
