# Google Cloud Associate Data Practitioner — Full-Length Mock Exam 5

Associate Data Practitioner · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Data Preparation and Ingestion (Ingestion, Reporting, Pipelines, and Access)

### 1. Factory sensor readings must be normalised outside the analytics store so the store holds only clean rows. Which approach is described?

- A. Load into a staging area, apply a light transform, then transform again in the warehouse
- B. Load the raw rows, then transform them inside the warehouse
- C. Extract, transform outside the warehouse, then load the result
- D. Query the source system in place with a federated query

### 2. Legal wants the untouched event log retained because a discovery request could arrive years later. Which approach fits?

- A. Extract, transform outside the warehouse, then load the result
- B. Transform on the source system before the export starts
- C. Load into a staging area, apply a light transform, then transform again in the warehouse
- D. Load the raw rows, then transform them inside the warehouse

### 3. A nightly job must read a tenant's remote table once, and a failed transform must not force a fresh extract. Which two choices fit? Select two.

- A. Extract, transform outside the warehouse, then load the result
- B. Load the raw rows, then transform them inside the warehouse
- C. Combine the extracts in a spreadsheet and upload the result
- D. Land the extract in a staging table before any transform runs
- E. Query the source system in place with a federated query

### 4. A cheap standardisation before the warehouse write would reduce what the expensive engine has to read. Which design fits?

- A. Transform on the source system before the export starts
- B. Extract, transform outside the warehouse, then load the result
- C. Load into a staging area, apply a light transform, then transform again in the warehouse
- D. Load the raw rows, then transform them inside the warehouse

### 5. A join returns nothing because half the region values carry a trailing space. Where should the fix live?

- A. Load the extract into a notebook and work in pandas
- B. Load first and fix the rejected rows afterwards
- C. Combine the extracts in a spreadsheet and upload the result
- D. Clean the rows with SQL in BigQuery

### 6. A validator must run on the live stream and again on the historical backfill. What should be used?

- A. Clean the rows with SQL in BigQuery
- B. Run a cron job on a Compute Engine instance
- C. Clean the data with Spark on Dataproc
- D. Clean the stream with a Dataflow pipeline

### 7. The dashboard needs a badge that says whether today's data passed its checks. What should be added?

- A. Load first and fix the rejected rows afterwards
- B. Define data quality rules and run a quality scan
- C. Select every column to be safe
- D. Profile the columns to measure the null rate before loading

### 8. The same invoice appears twice after a retry, and nobody knows how many tax identifiers are missing. Which two actions apply? Select two.

- A. Load first and fix the rejected rows afterwards
- B. Deduplicate on the business key in the cleaning step
- C. Select every column to be safe
- D. Profile the columns to measure the null rate before loading
- E. Land the data as CSV

### 9. An analytics vendor publishes files in an object store on another cloud each night. What should be used?

- A. Use Storage Transfer Service
- B. Pull the files from the partner over FTP each night
- C. Copy the objects with the gcloud storage command
- D. Order a Transfer Appliance

### 10. A SQL Server estate must move to Cloud SQL with a cutover measured in minutes. What should be used?

- A. Order a Transfer Appliance
- B. Replicate the changes with Datastream
- C. Use BigQuery Data Transfer Service
- D. Use Database Migration Service

### 11. A Display and Video 360 export must appear in a warehouse table every morning. What should be used?

- A. Load the rows with a client library from the application
- B. Use BigQuery Data Transfer Service
- C. Replicate the changes with Datastream
- D. Use Storage Transfer Service

### 12. One transfer is a physical shipment of archived tapes, and another is a one-off copy between buckets. Which two tools apply? Select two.

- A. Order a Transfer Appliance
- B. Use BigQuery Data Transfer Service
- C. Copy the objects with the gcloud storage command
- D. Use Storage Transfer Service
- E. Pull the files from the partner over FTP each night

### 13. A forty-column fact table is aggregated on four of them in every query. Which format fits?

- A. Land the data as Parquet
- B. Land the data as CSV
- C. Land the data as newline-delimited JSON
- D. Land the data as XML

### 14. Webhook bodies arrive with nested arrays from four different senders. Which format fits?

- A. Land the data as newline-delimited JSON
- B. Land the data as CSV
- C. Convert the data to ORC before the load
- D. Land the data as Avro

### 15. A reviewer must diff two versions of a small reference file line by line. Which format fits?

- A. Convert the data to ORC before the load
- B. Land the data as Parquet
- C. Land the data as Avro
- D. Land the data as CSV

### 16. A file's columns are discovered only when somebody queries it. Which approach is in use?

- A. Land the data as Parquet
- B. Apply a schema on read at query time
- C. Treat the records as structured data
- D. Load the files into a native table

### 17. A one-off history of four hundred Parquet objects must become one table. What should be used?

- A. Load the files with the bq load command
- B. Stream the rows with the BigQuery Storage Write API
- C. Load the rows with a client library from the application
- D. Copy the objects with the gcloud storage command

### 18. An ad server must commit impressions at two hundred thousand rows a second. What should be used?

- A. Copy the objects with the gcloud storage command
- B. Stream the rows with the BigQuery Storage Write API
- C. Load the rows with a client library from the application
- D. Load the files with the bq load command

### 19. A paginated REST API must be walked nightly and the pages written as objects. What should be used?

- A. Load the rows with a client library from the application
- B. Build the pipeline in Dataflow
- C. Load the files with the bq load command
- D. Run the handler as a Cloud Functions function

### 20. A business intelligence layer must aggregate forty terabytes of orders. Which store fits?

- A. Store the rows in BigQuery
- B. Store the files in Cloud Storage
- C. Store the documents in Firestore
- D. Store the rows in Bigtable

### 21. A content management system needs joins and transactions over a fixed schema. Which store fits?

- A. Store the rows in Bigtable
- B. Store the records in AlloyDB for PostgreSQL
- C. Store the documents in Firestore
- D. Store the records in Cloud SQL

### 22. A fleet writes a row per device every second and reads back the last hour by device. Which store fits?

- A. Store the rows in Bigtable
- B. Store the records in Cloud SQL
- C. Store the records in Spanner
- D. Store the documents in Firestore

### 23. An application stores session documents, and a separate team reports over the same events. Which two stores apply? Select two.

- A. Store the rows in BigQuery
- B. Keep the dataset on the analyst workstation
- C. Store the files in Cloud Storage
- D. Store the documents in Firestore
- E. Store the rows in Bigtable

### 24. A global game leaderboard is read from every continent. Which location type fits?

- A. Choose a regional location
- B. Choose a multi-region location
- C. Choose a zonal resource
- D. Choose a dual-region location

### 25. A pilot serves one country and the finance team wants the lowest storage rate. Which location type fits?

- A. Choose a multi-region location
- B. Place the data in the region nearest the largest user base
- C. Choose a dual-region location
- D. Choose a regional location

### 26. The data must stay in one country, and a second city inside it must hold the failover copy. Which two choices apply? Select two.

- A. Choose a regional location
- B. Choose a dual-region location
- C. Place the data in the region the regulator names
- D. Choose a zonal resource
- E. Choose a multi-region location

### 27. A table arrives with a DDL that declares every column and type. How should it be classified?

- A. Treat the files as unstructured data
- B. Treat the records as semi-structured data
- C. Treat the records as structured data
- D. Apply a schema on read at query time

### 28. Parquet rows carry nested structs whose fields differ between producers. How should they be classified?

- A. Treat the records as semi-structured data
- B. Apply a schema on read at query time
- C. Treat the records as structured data
- D. Treat the files as unstructured data

### 29. A .NET service holds a batch of records and must write them to a table. What should be used?

- A. Stream the rows with the BigQuery Storage Write API
- B. Copy the objects with the gcloud storage command
- C. Load the rows with a client library from the application
- D. Load the files with the bq load command

### 30. A CI pipeline must publish test fixtures into a bucket before the suite starts. What should be used?

- A. Order a Transfer Appliance
- B. Use Storage Transfer Service
- C. Copy the objects with the gcloud storage command
- D. Load the files with the bq load command

---

## Domain 2 — Data Analysis and Presentation (Files, Formats, Dashboards, and Governance)

### 31. A salary column must exist in the table but never reach a specific group of analysts. What should be used?

- A. Load the files into a native table
- B. Create a BigQuery materialized view
- C. Create a BigQuery view over the join
- D. Query the files through an external table

### 32. A refresh every five minutes keeps repeating the same expensive aggregation. What should be used?

- A. Write a SQL query in BigQuery and save the result
- B. Create a BigQuery view over the join
- C. Create a BigQuery materialized view
- D. Load the files into a native table

### 33. Two physical changes make date-filtered queries cheaper on the same data. Which two apply? Select two.

- A. Select every column to be safe
- B. Turn off the result cache to force a fresh read
- C. Query the files through an external table
- D. Cluster the table on the filter column
- E. Filter the query on the partition column

### 34. The same weekly cohort question is asked with a different month each time. What should be produced?

- A. Write a SQL query in BigQuery and save the result
- B. Share the dashboard with a scheduled delivery
- C. Export the query result to a spreadsheet for the business team
- D. Turn off the result cache to force a fresh read

### 35. A data team needs notebook runtimes inside the project with no VM patching. What should be used?

- A. Analyse the data in a Colab Enterprise notebook
- B. Load the extract into a notebook and work in pandas
- C. Upload a CSV extract into the notebook and analyse it there
- D. Keep the dataset on the analyst workstation

### 36. An analyst must chart a warehouse query without exporting a file. What should be used?

- A. Query BigQuery from the notebook with the %%bigquery magic
- B. Export the query result to a spreadsheet for the business team
- C. Load the extract into a notebook and work in pandas
- D. Upload a CSV extract into the notebook and analyse it there

### 37. A merchandiser asks which promotion cannibalised a product line. What should be produced?

- A. Write a SQL query in BigQuery and save the result
- B. Turn off the result cache to force a fresh read
- C. Document the steps and have an analyst run them each morning
- D. Share the dashboard with a scheduled delivery

### 38. The regional leads want the same chart every morning without signing in. What should be configured?

- A. Share the dashboard with a scheduled delivery
- B. Document the steps and have an analyst run them each morning
- C. Export the query result to a spreadsheet for the business team
- D. Turn off the result cache to force a fresh read

### 39. Thirty tiles must share one certified definition of active user. What should be used?

- A. Build a Looker Studio report
- B. Select every column to be safe
- C. Build a governed Looker dashboard
- D. Export the query result to a spreadsheet for the business team

### 40. Two teams publish different retention rates from the same table. What should be added?

- A. Add a LookML measure for the calculation
- B. Change the LookML parameter in the view
- C. Export the query result to a spreadsheet for the business team
- D. Turn off the result cache to force a fresh read

### 41. Field access must be decided in the model, and a daily digest must leave the tool entirely. Which two components apply? Select two.

- A. Turn off the result cache to force a fresh read
- B. Select every column to be safe
- C. Build a Looker Studio report
- D. Expose the table through a LookML explore
- E. Share the dashboard with a scheduled delivery

### 42. A founder wants one chart over a spreadsheet before a morning call. What should be used?

- A. Add a LookML measure for the calculation
- B. Orchestrate the steps in Cloud Composer
- C. Build a governed Looker dashboard
- D. Build a Looker Studio report

### 43. Certified definitions and per-group access must hold across fifty reports. What should be used?

- A. Export the query result to a spreadsheet for the business team
- B. Issue a signed URL with a short expiry
- C. Build a governed Looker dashboard
- D. Build a Looker Studio report

### 44. The fiscal calendar changed and every report must roll up differently. What should be changed?

- A. Expose the table through a LookML explore
- B. Change the LookML parameter in the view
- C. Add a LookML measure for the calculation
- D. Turn off the result cache to force a fresh read

### 45. A margin ratio must be written once and reused by every report author. What should be added?

- A. Write a SQL query in BigQuery and save the result
- B. Change the LookML parameter in the view
- C. Turn off the result cache to force a fresh read
- D. Add a LookML measure for the calculation

### 46. One question needs a join that other authors must not be offered. What should be added?

- A. Add a LookML measure for the calculation
- B. Change the LookML parameter in the view
- C. Create a BigQuery view over the join
- D. Expose the table through a LookML explore

### 47. No outcome column exists but the team wants customers grouped. What should be built?

- A. Train a BigQuery ML ARIMA_PLUS model
- B. Train a BigQuery ML k-means model
- C. Train a BigQuery ML logistic regression model
- D. Score the rows with ML.PREDICT

### 48. A team has labelled rows and no one to choose an architecture. What should be used?

- A. Train a BigQuery ML linear regression model
- B. Train an AutoML tabular model
- C. Score the rows with ML.PREDICT
- D. Land the data as Parquet

### 49. A flag and a monthly series must both be produced inside the warehouse. Which two model types apply? Select two.

- A. Train a BigQuery ML ARIMA_PLUS model
- B. Train a BigQuery ML logistic regression model
- C. Train a BigQuery ML k-means model
- D. Train an AutoML tabular model
- E. Generate the forecast with ML.FORECAST

### 50. Support tickets must be labelled per row without an export to another system. What should be used?

- A. Fine-tune a Gemini model from the warehouse rows
- B. Land the data as newline-delimited JSON
- C. Load the extract into a notebook and work in pandas
- D. Create a BigQuery remote model over a Gemini model

### 51. A remote model returns an authorisation error before the first prompt. What should be created?

- A. Load the files with the bq load command
- B. Create the BigQuery connection that reaches the model endpoint
- C. Copy the objects with the gcloud storage command
- D. Issue a signed URL with a short expiry

### 52. Two stakeholders expect different outputs and neither has written an acceptance test. What should be agreed first?

- A. Run a cron job on a Compute Engine instance
- B. Document the steps and have an analyst run them each morning
- C. Plan collection, training, evaluation, then prediction
- D. Ship the model once the training loss looks good

### 53. A event feed must be judged on later periods, and one large account must not span both splits. Which two split designs apply? Select two.

- A. Profile the columns to measure the null rate before loading
- B. Hold out a labelled split before training
- C. Ship the model once the training loss looks good
- D. Hold out whole entities so none spans both splits
- E. Hold the most recent period out as the test set

### 54. Precision and recall must appear in the audit pack as SQL output. What should be used?

- A. Generate the forecast with ML.FORECAST
- B. Explain the prediction with ML.EXPLAIN_PREDICT
- C. Evaluate the model with ML.EVALUATE
- D. Score the rows with ML.PREDICT

### 55. A wide table hides interactions and the labels are plentiful. Which model type fits?

- A. Train a BigQuery ML k-means model
- B. Train a BigQuery ML linear regression model
- C. Train a BigQuery ML ARIMA_PLUS model
- D. Train a BigQuery ML boosted tree model

### 56. A nightly list of lapsed customers must be scored into a table. What should be used?

- A. Generate the forecast with ML.FORECAST
- B. Explain the prediction with ML.EXPLAIN_PREDICT
- C. Evaluate the model with ML.EVALUATE
- D. Score the rows with ML.PREDICT

### 57. Two teams must be able to say which artifact is the approved version. What should be done?

- A. Register the model version in Model Registry
- B. Export the query result to a spreadsheet for the business team
- C. Copy the objects with the gcloud storage command
- D. Keep the dataset on the analyst workstation

---

## Domain 3 — Data Pipeline Orchestration (Streaming, Scheduling, Modelling, and Recovery)

### 58. SQL models must rebuild in dependency order after a column rename. What should be used?

- A. Manage the SQL transformations in Dataform
- B. Run the transformation as Spark on Dataproc
- C. Build the pipeline in Cloud Data Fusion
- D. Run a cron job on a Compute Engine instance

### 59. Eleven campaign exports need lookup joins applied by an analyst with no coding background. What should be used?

- A. Sequence the API calls with Workflows
- B. Manage the SQL transformations in Dataform
- C. Run the transformation as Spark on Dataproc
- D. Build the pipeline in Cloud Data Fusion

### 60. A Scala job must run over eight terabytes of Avro on a cluster. What should be used?

- A. Run the transformation as Spark on Dataproc
- B. Run the handler as a Cloud Functions function
- C. Build the pipeline in Dataflow
- D. Sequence the API calls with Workflows

### 61. One path needs streaming parity and another needs an existing Spark job re-run. Which two tools apply? Select two.

- A. Run the handler as a Cloud Functions function
- B. Build the pipeline in Dataflow
- C. Manage the SQL transformations in Dataform
- D. Trigger the job from Cloud Scheduler
- E. Run the transformation as Spark on Dataproc

### 62. The warehouse engine should absorb the join load instead of the source database. Which design fits?

- A. Extract, transform outside the warehouse, then load the result
- B. Load the raw rows, then transform them inside the warehouse
- C. Transform on the source system before the export starts
- D. Query the source system in place with a federated query

### 63. The destination will reject any record that has not already been standardised. Which design fits?

- A. Land the extract in a staging table before any transform runs
- B. Extract, transform outside the warehouse, then load the result
- C. Load the raw rows, then transform them inside the warehouse
- D. Load the rows with a client library from the application

### 64. A nightly rollup inside the warehouse must run with nobody watching. What should be used?

- A. Trigger the job from Cloud Scheduler
- B. Submit the job through a Dataproc workflow template
- C. Sequence the API calls with Workflows
- D. Schedule the SQL with a BigQuery scheduled query

### 65. A closing webhook must fire at 23:30 every trading day. What should be used?

- A. Schedule the SQL with a BigQuery scheduled query
- B. Trigger the job from Cloud Scheduler
- C. Orchestrate the steps in Cloud Composer
- D. Start the pipeline from an Eventarc trigger

### 66. A job outside SQL must start on time and must page an owner when it fails. Which two components apply? Select two.

- A. Schedule the SQL with a BigQuery scheduled query
- B. Trigger the job from Cloud Scheduler
- C. Create a Cloud Monitoring alert policy on the job metric
- D. Document the steps and have an analyst run them each morning
- E. Run a cron job on a Compute Engine instance

### 67. A streaming job's watermark has stalled and one step lags. Where should the team look?

- A. Watch the job graph and per-step throughput in the Dataflow console
- B. Turn off the result cache to force a fresh read
- C. Query the job logs in Logs Explorer
- D. Write a SQL query in BigQuery and save the result

### 68. Rejected events must be recoverable instead of disappearing. What should be added?

- A. Load first and fix the rejected rows afterwards
- B. Select every column to be safe
- C. Write the rejected rows to a dead-letter table
- D. Denormalise the tables into one wide table

### 69. A single trace identifier must be followed across the pipeline logs. Where should the team look?

- A. Document the steps and have an analyst run them each morning
- B. Query the job logs in Logs Explorer
- C. Share the dashboard with a scheduled delivery
- D. Write a SQL query in BigQuery and save the result

### 70. A stale table is first reported by the sales team rather than the platform. What should be added?

- A. Document the steps and have an analyst run them each morning
- B. Turn off the result cache to force a fresh read
- C. Create a Cloud Monitoring alert policy on the job metric
- D. Query the job logs in Logs Explorer

### 71. A six-step graph must wait on a partner and retry a failed step twice. What should orchestrate it?

- A. Sequence the API calls with Workflows
- B. Orchestrate the steps in Cloud Composer
- C. Schedule the SQL with a BigQuery scheduled query
- D. Run the handler as a Cloud Functions function

### 72. An approval call must sit between two API calls with no server to operate. What should be used?

- A. Run a cron job on a Compute Engine instance
- B. Run the handler as a Cloud Functions function
- C. Orchestrate the steps in Cloud Composer
- D. Sequence the API calls with Workflows

### 73. A graph must hold the dependencies, and a sequence of API calls must run inside one of its steps. Which two components apply? Select two.

- A. Orchestrate the steps in Cloud Composer
- B. Run a cron job on a Compute Engine instance
- C. Run the handler as a Cloud Functions function
- D. Schedule the SQL with a BigQuery scheduled query
- E. Sequence the API calls with Workflows

### 74. Published telemetry must land in a table within seconds with no subscriber to run. What should be used?

- A. Subscribe BigQuery to the Pub/Sub topic
- B. Load the files with the bq load command
- C. Schedule the SQL with a BigQuery scheduled query
- D. Start the pipeline from an Eventarc trigger

### 75. A file arriving in a bucket must start a Cloud Run job at once. What should be used?

- A. Subscribe BigQuery to the Pub/Sub topic
- B. Schedule the SQL with a BigQuery scheduled query
- C. Start the pipeline from an Eventarc trigger
- D. Trigger the job from Cloud Scheduler

---

## Domain 4 — Data Management (Warehouse Analytics, Orchestration, and Key Management)

### 76. A contractor must read one table for the length of a project. What should be granted?

- A. Make the bucket public so the partner can read it
- B. Grant the predefined role that matches the task
- C. Grant the role to the whole domain
- D. Grant the basic Owner role to the team

### 77. A scheduled job must act without any employee's credentials. What should be used?

- A. Grant the role to the whole domain
- B. Issue a signed URL with a short expiry
- C. Grant the basic Owner role to the team
- D. Run the job as a dedicated service account

### 78. The grant must match a job Google already describes, and the principal must not be a person. Which two controls apply? Select two.

- A. Assign a predefined role to the group
- B. Grant the role to the whole domain
- C. Make the bucket public so the partner can read it
- D. Run the job as a dedicated service account
- E. Grant the basic Owner role to the team

### 79. A new hire needs the standard permissions for a data analyst. What should be granted?

- A. Make the bucket public so the partner can read it
- B. Create a custom role with only the permissions used
- C. Grant the basic Owner role to the team
- D. Assign a predefined role to the group

### 80. One permission in the matching role must be withheld from a vendor. What should be created?

- A. Assign a predefined role to the group
- B. Grant the basic Owner role to the team
- C. Create a custom role with only the permissions used
- D. Grant the role to the whole domain

### 81. Buckets in three projects must all be auditable from IAM alone. What should be enabled?

- A. Make the bucket public so the partner can read it
- B. Manage per-object ACLs on the bucket
- C. Issue a signed URL with a short expiry
- D. Enable uniform bucket-level access

### 82. A supplier needs thirty minutes of access to one contract file. What should be issued?

- A. Enable uniform bucket-level access
- B. Export the table to a bucket the partner owns
- C. Issue a signed URL with a short expiry
- D. Make the bucket public so the partner can read it

### 83. A subsidiary must read a curated dataset that stays current without a copy. What should be used?

- A. Make the bucket public so the partner can read it
- B. Publish the dataset through Analytics Hub
- C. Export the table to a bucket the partner owns
- D. Issue a signed URL with a short expiry

### 84. An authorised identity must still be unable to move data out of the boundary. What should be applied?

- A. Publish the dataset through Analytics Hub
- B. Issue a signed URL with a short expiry
- C. Make the bucket public so the partner can read it
- D. Add the project to a VPC Service Controls perimeter

### 85. Monthly reconciliation files are read once and kept for two years. Which class fits?

- A. Keep the objects in the Standard class
- B. Move the objects to Coldline
- C. Move the objects to Archive
- D. Move the objects to Nearline

### 86. A ticketing site reads its static assets on every page load. Which class fits?

- A. Move the objects to Archive
- B. Keep the objects in the Standard class
- C. Enable Autoclass on the bucket
- D. Move the objects to Nearline

### 87. Objects must move to a cheaper class as they age, and expired ones must disappear. Which two options apply? Select two.

- A. Add a lifecycle rule that deletes objects after the retention period
- B. Keep every version in the Standard class forever
- C. Enable Autoclass on the bucket
- D. Leave the objects in place and review them next year
- E. Move the objects to Coldline

### 88. Temporary landing objects must be removed a day after they arrive. What should be added?

- A. Add a lifecycle rule that deletes objects after the retention period
- B. Keep every version in the Standard class forever
- C. Enable object versioning on the bucket
- D. Leave the objects in place and review them next year

### 89. Only the last thirteen months of partitions are queried, and the table must remain. What should be set?

- A. Set a table expiration on the dataset
- B. Set a partition expiration on the table
- C. Leave the objects in place and review them next year
- D. Add a lifecycle rule that deletes objects after the retention period

### 90. Video masters are re-opened only when a legal request names them. Which class fits?

- A. Move the objects to Nearline
- B. Move the objects to Archive
- C. Move the objects to Coldline
- D. Keep the objects in the Standard class

### 91. A litigation hold must survive an accidental lifecycle rule on the bucket. What should be applied?

- A. Apply a bucket retention policy with a lock
- B. Add a lifecycle rule that deletes objects after the retention period
- C. Enable object versioning on the bucket
- D. Leave the objects in place and review them next year

### 92. A bad script updated three thousand rows an hour ago. What should be used?

- A. Rely on the disk snapshot the platform keeps
- B. Deploy a single zonal instance to keep the cost down
- C. Enable automated backups and point-in-time recovery on Cloud SQL
- D. Copy the bucket to a second region with a scheduled transfer

### 93. The recovery plan exists on paper and has never been executed. What should be done?

- A. Copy the bucket to a second region with a scheduled transfer
- B. Rely on the disk snapshot the platform keeps
- C. Restore into a scratch project on a schedule
- D. Deploy a single zonal instance to keep the cost down

### 94. A continuity test must show how far the second region trails the first. What should be used?

- A. Copy the bucket to a second region with a scheduled transfer
- B. Enable object versioning on the bucket
- C. Create a dual-region bucket with a replication policy
- D. Create a multi-region bucket

### 95. An overwrite must be reversible, and a second copy must exist in another region. Which two measures apply? Select two.

- A. Copy the bucket to a second region with a scheduled transfer
- B. Rely on the disk snapshot the platform keeps
- C. Enable object versioning on the bucket
- D. Create a dual-region bucket with a replication policy
- E. Create a Cloud SQL read replica in another region

### 96. A contract names a second region that must hold the copy, alongside the primary one. Which location type fits?

- A. Choose a multi-region location
- B. Choose a zonal resource
- C. Choose a dual-region location
- D. Choose a regional location

### 97. The customer must be able to revoke access by disabling their own key. Which key model applies?

- A. Put the key in the application configuration file
- B. Encrypt with a customer-managed key from Cloud KMS
- C. Supply a customer-supplied key with each request
- D. Use the Google-managed default encryption

### 98. One dataset needs no key operations, and another must pass the key with each request. Which two models apply? Select two.

- A. Encrypt in the client and store the key next to the data
- B. Supply a customer-supplied key with each request
- C. Use the Google-managed default encryption
- D. Encrypt with a customer-managed key from Cloud KMS
- E. Put the key in the application configuration file

### 99. A control requires each key version to be replaced within twelve months. What should be set?

- A. Set a rotation schedule on the key
- B. Put the key in the application configuration file
- C. Destroy the key version to stop access immediately
- D. Use the Google-managed default encryption

### 100. Traffic between a client and the API must be unreadable on the network. What should be confirmed?

- A. Encrypt in the client and store the key next to the data
- B. Put the key in the application configuration file
- C. Enforce TLS for every connection to the service
- D. Confirm the data is encrypted at rest by the storage service

---

## Answer key and explanations

### Question 1 — C

Answer: Extract, transform outside the warehouse, then load the result. ETL normalises the readings before the load, so the store only receives curated rows. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. Why the correct answer wins: ETL normalises the readings before the load, so the store only receives curated rows.
- **B:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETL normalises the readings before the load, so the store only receives curated rows.
- **C:** Correct. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. In this case: ETL normalises the readings before the load, so the store only receives curated rows.
- **D:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ETL normalises the readings before the load, so the store only receives curated rows.

### Question 2 — D

Answer: Load the raw rows, then transform them inside the warehouse. ELT keeps the raw log and reshapes it in the warehouse when a question arrives. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT keeps the raw log and reshapes it in the warehouse when a question arrives.
- **B:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ELT keeps the raw log and reshapes it in the warehouse when a question arrives.
- **C:** Incorrect for this question. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. Why the correct answer wins: ELT keeps the raw log and reshapes it in the warehouse when a question arrives.
- **D:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT keeps the raw log and reshapes it in the warehouse when a question arrives.

### Question 3 — D, E

Answers: Query the source system in place with a federated query; Land the extract in a staging table before any transform runs. The federated query reads the remote table without a copy, and the staging table isolates the retry. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. A staging table separates a failed load from a failed transform, so each can be retried on its own. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: The federated query reads the remote table without a copy, and the staging table isolates the retry.
- **B:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: The federated query reads the remote table without a copy, and the staging table isolates the retry.
- **C:** Incorrect for this question. A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run. Why the correct answer wins: The federated query reads the remote table without a copy, and the staging table isolates the retry.
- **D:** Correct. A staging table separates a failed load from a failed transform, so each can be retried on its own. In this case: The federated query reads the remote table without a copy, and the staging table isolates the retry.
- **E:** Correct. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. In this case: The federated query reads the remote table without a copy, and the staging table isolates the retry.

### Question 4 — C

Answer: Load into a staging area, apply a light transform, then transform again in the warehouse. ETLT performs that early standardisation and still transforms inside the warehouse. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ETLT performs that early standardisation and still transforms inside the warehouse.
- **B:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ETLT performs that early standardisation and still transforms inside the warehouse.
- **C:** Correct. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. In this case: ETLT performs that early standardisation and still transforms inside the warehouse.
- **D:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETLT performs that early standardisation and still transforms inside the warehouse.

### Question 5 — D

Answer: Clean the rows with SQL in BigQuery. SQL in the warehouse trims the values where the data sits. SQL inside the warehouse removes duplicates, trims values, and casts types where the data already sits. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: SQL in the warehouse trims the values where the data sits.
- **B:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: SQL in the warehouse trims the values where the data sits.
- **C:** Incorrect for this question. A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run. Why the correct answer wins: SQL in the warehouse trims the values where the data sits.
- **D:** Correct. SQL inside the warehouse removes duplicates, trims values, and casts types where the data already sits. In this case: SQL in the warehouse trims the values where the data sits.

### Question 6 — D

Answer: Clean the stream with a Dataflow pipeline. A Dataflow pipeline applies one validation definition to both inputs. A Dataflow pipeline applies the same cleaning logic to streaming and batch records. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. SQL inside the warehouse removes duplicates, trims values, and casts types where the data already sits. Why the correct answer wins: A Dataflow pipeline applies one validation definition to both inputs.
- **B:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: A Dataflow pipeline applies one validation definition to both inputs.
- **C:** Incorrect for this question. Spark suits large files that need custom code rather than SQL. Why the correct answer wins: A Dataflow pipeline applies one validation definition to both inputs.
- **D:** Correct. A Dataflow pipeline applies the same cleaning logic to streaming and batch records. In this case: A Dataflow pipeline applies one validation definition to both inputs.

### Question 7 — B

Answer: Define data quality rules and run a quality scan. Declared rules produce a pass or fail result the dashboard can show. Declared rules turn a judgement about the data into a test that runs on every load. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: Declared rules produce a pass or fail result the dashboard can show.
- **B:** Correct. Declared rules turn a judgement about the data into a test that runs on every load. In this case: Declared rules produce a pass or fail result the dashboard can show.
- **C:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: Declared rules produce a pass or fail result the dashboard can show.
- **D:** Incorrect for this question. A profile quantifies what is missing before the gaps reach a dashboard. Why the correct answer wins: Declared rules produce a pass or fail result the dashboard can show.

### Question 8 — B, D

Answers: Deduplicate on the business key in the cleaning step; Profile the columns to measure the null rate before loading. A business key removes the duplicate, and a profile measures the missing values. Retries and restatements create duplicate rows unless the load deduplicates on a stable key. A profile quantifies what is missing before the gaps reach a dashboard. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A business key removes the duplicate, and a profile measures the missing values.
- **B:** Correct. Retries and restatements create duplicate rows unless the load deduplicates on a stable key. In this case: A business key removes the duplicate, and a profile measures the missing values.
- **C:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A business key removes the duplicate, and a profile measures the missing values.
- **D:** Correct. A profile quantifies what is missing before the gaps reach a dashboard. In this case: A business key removes the duplicate, and a profile measures the missing values.
- **E:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: A business key removes the duplicate, and a profile measures the missing values.

### Question 9 — A

Answer: Use Storage Transfer Service. Storage Transfer Service copies from another cloud on a schedule. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: Storage Transfer Service copies from another cloud on a schedule.
- **B:** Incorrect for this question. A hand-built FTP pull has no retry, no manifest, and no record of what arrived. Why the correct answer wins: Storage Transfer Service copies from another cloud on a schedule.
- **C:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: Storage Transfer Service copies from another cloud on a schedule.
- **D:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: Storage Transfer Service copies from another cloud on a schedule.

### Question 10 — D

Answer: Use Database Migration Service. Database Migration Service performs the move with continuous replication until the cutover. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: Database Migration Service performs the move with continuous replication until the cutover.
- **B:** Incorrect for this question. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Why the correct answer wins: Database Migration Service performs the move with continuous replication until the cutover.
- **C:** Incorrect for this question. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Why the correct answer wins: Database Migration Service performs the move with continuous replication until the cutover.
- **D:** Correct. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. In this case: Database Migration Service performs the move with continuous replication until the cutover.

### Question 11 — B

Answer: Use BigQuery Data Transfer Service. BigQuery Data Transfer Service schedules the recurring pull from Google sources. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: BigQuery Data Transfer Service schedules the recurring pull from Google sources.
- **B:** Correct. In this case: BigQuery Data Transfer Service schedules the recurring pull from Google sources.
- **C:** Incorrect for this question. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Why the correct answer wins: BigQuery Data Transfer Service schedules the recurring pull from Google sources.
- **D:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: BigQuery Data Transfer Service schedules the recurring pull from Google sources.

### Question 12 — A, C

Answers: Order a Transfer Appliance; Copy the objects with the gcloud storage command. The appliance moves the tapes, and the gcloud copy handles the one-off bucket move. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. A gcloud storage copy is the direct path for an ad hoc move between buckets. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. In this case: The appliance moves the tapes, and the gcloud copy handles the one-off bucket move.
- **B:** Incorrect for this question. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Why the correct answer wins: The appliance moves the tapes, and the gcloud copy handles the one-off bucket move.
- **C:** Correct. A gcloud storage copy is the direct path for an ad hoc move between buckets. In this case: The appliance moves the tapes, and the gcloud copy handles the one-off bucket move.
- **D:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: The appliance moves the tapes, and the gcloud copy handles the one-off bucket move.
- **E:** Incorrect for this question. A hand-built FTP pull has no retry, no manifest, and no record of what arrived. Why the correct answer wins: The appliance moves the tapes, and the gcloud copy handles the one-off bucket move.

### Question 13 — A

Answer: Land the data as Parquet. Parquet reads only the four columns the aggregate needs. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Parquet is columnar and compressed, so a scan reads only the columns a query needs. In this case: Parquet reads only the four columns the aggregate needs.
- **B:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Parquet reads only the four columns the aggregate needs.
- **C:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: Parquet reads only the four columns the aggregate needs.
- **D:** Incorrect for this question. XML nests well and is verbose, which makes it a poor fit for wide analytical scans. Why the correct answer wins: Parquet reads only the four columns the aggregate needs.

### Question 14 — A

Answer: Land the data as newline-delimited JSON. Newline-delimited JSON keeps each sender's nesting intact. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Newline-delimited JSON keeps nested fields and can be appended one record at a time. In this case: Newline-delimited JSON keeps each sender's nesting intact.
- **B:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Newline-delimited JSON keeps each sender's nesting intact.
- **C:** Incorrect for this question. ORC is another columnar format; choosing it adds a conversion step without a benefit over Parquet here. Why the correct answer wins: Newline-delimited JSON keeps each sender's nesting intact.
- **D:** Incorrect for this question. Avro carries its schema with the records and suits row-oriented streaming exchanges. Why the correct answer wins: Newline-delimited JSON keeps each sender's nesting intact.

### Question 15 — D

Answer: Land the data as CSV. CSV lines can be compared directly in a diff. CSV is readable everywhere and carries no types, no schema, and no nesting. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ORC is another columnar format; choosing it adds a conversion step without a benefit over Parquet here. Why the correct answer wins: CSV lines can be compared directly in a diff.
- **B:** Incorrect for this question. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Why the correct answer wins: CSV lines can be compared directly in a diff.
- **C:** Incorrect for this question. Avro carries its schema with the records and suits row-oriented streaming exchanges. Why the correct answer wins: CSV lines can be compared directly in a diff.
- **D:** Correct. CSV is readable everywhere and carries no types, no schema, and no nesting. In this case: CSV lines can be compared directly in a diff.

### Question 16 — B

Answer: Apply a schema on read at query time. Schema on read interprets the file at query time. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Why the correct answer wins: Schema on read interprets the file at query time.
- **B:** Correct. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. In this case: Schema on read interprets the file at query time.
- **C:** Incorrect for this question. Structured data fits a declared schema of rows and columns. Why the correct answer wins: Schema on read interprets the file at query time.
- **D:** Incorrect for this question. A native table gives the warehouse its own copy and the best scan performance. Why the correct answer wins: Schema on read interprets the file at query time.

### Question 17 — A

Answer: Load the files with the bq load command. A load job reads the objects and writes the table in one pass. The bq load command creates a load job that reads files from Cloud Storage into a table. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. The bq load command creates a load job that reads files from Cloud Storage into a table. In this case: A load job reads the objects and writes the table in one pass.
- **B:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: A load job reads the objects and writes the table in one pass.
- **C:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: A load job reads the objects and writes the table in one pass.
- **D:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A load job reads the objects and writes the table in one pass.

### Question 18 — B

Answer: Stream the rows with the BigQuery Storage Write API. The Storage Write API commits rows as the stream produces them. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: The Storage Write API commits rows as the stream produces them.
- **B:** Correct. In this case: The Storage Write API commits rows as the stream produces them.
- **C:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: The Storage Write API commits rows as the stream produces them.
- **D:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: The Storage Write API commits rows as the stream produces them.

### Question 19 — B

Answer: Build the pipeline in Dataflow. A Dataflow pipeline pages through the API and writes the objects. Dataflow runs the same code for streaming and batch and scales the workers with the load. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: A Dataflow pipeline pages through the API and writes the objects.
- **B:** Correct. Dataflow runs the same code for streaming and batch and scales the workers with the load. In this case: A Dataflow pipeline pages through the API and writes the objects.
- **C:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A Dataflow pipeline pages through the API and writes the objects.
- **D:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: A Dataflow pipeline pages through the API and writes the objects.

### Question 20 — A

Answer: Store the rows in BigQuery. BigQuery scans columnar tables at warehouse scale. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. In this case: BigQuery scans columnar tables at warehouse scale.
- **B:** Incorrect for this question. Cloud Storage holds objects of any shape and is the landing zone every other service can read. Why the correct answer wins: BigQuery scans columnar tables at warehouse scale.
- **C:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: BigQuery scans columnar tables at warehouse scale.
- **D:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: BigQuery scans columnar tables at warehouse scale.

### Question 21 — D

Answer: Store the records in Cloud SQL. Cloud SQL is a managed relational database for transaction workloads. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: Cloud SQL is a managed relational database for transaction workloads.
- **B:** Incorrect for this question. AlloyDB is a managed PostgreSQL option for transaction workloads that want PostgreSQL compatibility. Why the correct answer wins: Cloud SQL is a managed relational database for transaction workloads.
- **C:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: Cloud SQL is a managed relational database for transaction workloads.
- **D:** Correct. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. In this case: Cloud SQL is a managed relational database for transaction workloads.

### Question 22 — A

Answer: Store the rows in Bigtable. Bigtable gives keyed writes and reads at very high rate. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. In this case: Bigtable gives keyed writes and reads at very high rate.
- **B:** Incorrect for this question. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Why the correct answer wins: Bigtable gives keyed writes and reads at very high rate.
- **C:** Incorrect for this question. Spanner gives strongly consistent relational transactions across regions at global scale. Why the correct answer wins: Bigtable gives keyed writes and reads at very high rate.
- **D:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: Bigtable gives keyed writes and reads at very high rate.

### Question 23 — A, D

Answers: Store the documents in Firestore; Store the rows in BigQuery. Firestore serves the session documents, and BigQuery serves the reporting layer. Firestore is a document store for application reads by key with a flexible shape. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. In this case: Firestore serves the session documents, and BigQuery serves the reporting layer.
- **B:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Firestore serves the session documents, and BigQuery serves the reporting layer.
- **C:** Incorrect for this question. Cloud Storage holds objects of any shape and is the landing zone every other service can read. Why the correct answer wins: Firestore serves the session documents, and BigQuery serves the reporting layer.
- **D:** Correct. Firestore is a document store for application reads by key with a flexible shape. In this case: Firestore serves the session documents, and BigQuery serves the reporting layer.
- **E:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: Firestore serves the session documents, and BigQuery serves the reporting layer.

### Question 24 — B

Answer: Choose a multi-region location. A multi-region location spreads the copies across the geography. A multi-region location spreads the data across a continent-scale geography for the widest availability. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: A multi-region location spreads the copies across the geography.
- **B:** Correct. A multi-region location spreads the data across a continent-scale geography for the widest availability. In this case: A multi-region location spreads the copies across the geography.
- **C:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: A multi-region location spreads the copies across the geography.
- **D:** Incorrect for this question. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Why the correct answer wins: A multi-region location spreads the copies across the geography.

### Question 25 — D

Answer: Choose a regional location. One region is the cheapest placement for a single-country pilot. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: One region is the cheapest placement for a single-country pilot.
- **B:** Incorrect for this question. Distance between the data and the readers shows up as latency on every query. Why the correct answer wins: One region is the cheapest placement for a single-country pilot.
- **C:** Incorrect for this question. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Why the correct answer wins: One region is the cheapest placement for a single-country pilot.
- **D:** Correct. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. In this case: One region is the cheapest placement for a single-country pilot.

### Question 26 — B, C

Answers: Place the data in the region the regulator names; Choose a dual-region location. Residency fixes the country, and the dual-region pair names the second city. A residency obligation fixes the geography, which removes the choice from the performance discussion. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: Residency fixes the country, and the dual-region pair names the second city.
- **B:** Correct. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. In this case: Residency fixes the country, and the dual-region pair names the second city.
- **C:** Correct. A residency obligation fixes the geography, which removes the choice from the performance discussion. In this case: Residency fixes the country, and the dual-region pair names the second city.
- **D:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: Residency fixes the country, and the dual-region pair names the second city.
- **E:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: Residency fixes the country, and the dual-region pair names the second city.

### Question 27 — C

Answer: Treat the records as structured data. A declared DDL of columns and types is structured data. Structured data fits a declared schema of rows and columns. Local study-map skill 1.8 (Structured, Semi-Structured, and Unstructured Data), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Unstructured data has no field model at all, such as images, audio, or free documents. Why the correct answer wins: A declared DDL of columns and types is structured data.
- **B:** Incorrect for this question. Semi-structured data has a flexible shape such as JSON, where fields vary between records. Why the correct answer wins: A declared DDL of columns and types is structured data.
- **C:** Correct. Structured data fits a declared schema of rows and columns. In this case: A declared DDL of columns and types is structured data.
- **D:** Incorrect for this question. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Why the correct answer wins: A declared DDL of columns and types is structured data.

### Question 28 — A

Answer: Treat the records as semi-structured data. A flexible shape with optional nested fields is semi-structured data. Semi-structured data has a flexible shape such as JSON, where fields vary between records. Local study-map skill 1.8 (Structured, Semi-Structured, and Unstructured Data), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Semi-structured data has a flexible shape such as JSON, where fields vary between records. In this case: A flexible shape with optional nested fields is semi-structured data.
- **B:** Incorrect for this question. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Why the correct answer wins: A flexible shape with optional nested fields is semi-structured data.
- **C:** Incorrect for this question. Structured data fits a declared schema of rows and columns. Why the correct answer wins: A flexible shape with optional nested fields is semi-structured data.
- **D:** Incorrect for this question. Unstructured data has no field model at all, such as images, audio, or free documents. Why the correct answer wins: A flexible shape with optional nested fields is semi-structured data.

### Question 29 — C

Answer: Load the rows with a client library from the application. A client library writes the rows the service already holds. A client library suits an application that already holds the rows in memory rather than files in a bucket. Local study-map skill 1.9 (Loading with CLIs and Client Libraries), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: A client library writes the rows the service already holds.
- **B:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A client library writes the rows the service already holds.
- **C:** Correct. A client library suits an application that already holds the rows in memory rather than files in a bucket. In this case: A client library writes the rows the service already holds.
- **D:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A client library writes the rows the service already holds.

### Question 30 — C

Answer: Copy the objects with the gcloud storage command. A gcloud storage copy publishes the fixtures from the build step. A gcloud storage copy is the direct path for an ad hoc move between buckets. Local study-map skill 1.9 (Loading with CLIs and Client Libraries), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: A gcloud storage copy publishes the fixtures from the build step.
- **B:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: A gcloud storage copy publishes the fixtures from the build step.
- **C:** Correct. A gcloud storage copy is the direct path for an ad hoc move between buckets. In this case: A gcloud storage copy publishes the fixtures from the build step.
- **D:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A gcloud storage copy publishes the fixtures from the build step.

### Question 31 — C

Answer: Create a BigQuery view over the join. A view exposes the other columns and reads the table beneath it. A view stores the query rather than the rows, so the answer stays current at query time. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A native table gives the warehouse its own copy and the best scan performance. Why the correct answer wins: A view exposes the other columns and reads the table beneath it.
- **B:** Incorrect for this question. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. Why the correct answer wins: A view exposes the other columns and reads the table beneath it.
- **C:** Correct. A view stores the query rather than the rows, so the answer stays current at query time. In this case: A view exposes the other columns and reads the table beneath it.
- **D:** Incorrect for this question. An external table reads the objects where they sit and does not copy them into storage. Why the correct answer wins: A view exposes the other columns and reads the table beneath it.

### Question 32 — C

Answer: Create a BigQuery materialized view. A materialized view stores the aggregate and refreshes it. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: A materialized view stores the aggregate and refreshes it.
- **B:** Incorrect for this question. A view stores the query rather than the rows, so the answer stays current at query time. Why the correct answer wins: A materialized view stores the aggregate and refreshes it.
- **C:** Correct. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. In this case: A materialized view stores the aggregate and refreshes it.
- **D:** Incorrect for this question. A native table gives the warehouse its own copy and the best scan performance. Why the correct answer wins: A materialized view stores the aggregate and refreshes it.

### Question 33 — D, E

Answers: Filter the query on the partition column; Cluster the table on the filter column. Partitioning by the date column prunes the scan, and clustering co-locates the filtered values. A partition filter restricts the scan to the partitions the query needs. Clustering co-locates similar values so a filtered query reads fewer blocks. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: Partitioning by the date column prunes the scan, and clustering co-locates the filtered values.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: Partitioning by the date column prunes the scan, and clustering co-locates the filtered values.
- **C:** Incorrect for this question. An external table reads the objects where they sit and does not copy them into storage. Why the correct answer wins: Partitioning by the date column prunes the scan, and clustering co-locates the filtered values.
- **D:** Correct. Clustering co-locates similar values so a filtered query reads fewer blocks. In this case: Partitioning by the date column prunes the scan, and clustering co-locates the filtered values.
- **E:** Correct. A partition filter restricts the scan to the partitions the query needs. In this case: Partitioning by the date column prunes the scan, and clustering co-locates the filtered values.

### Question 34 — A

Answer: Write a SQL query in BigQuery and save the result. A parameterised saved query answers each month without a new artefact. A saved SQL query answers a business question and can be scheduled or exported. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A saved SQL query answers a business question and can be scheduled or exported. In this case: A parameterised saved query answers each month without a new artefact.
- **B:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: A parameterised saved query answers each month without a new artefact.
- **C:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A parameterised saved query answers each month without a new artefact.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A parameterised saved query answers each month without a new artefact.

### Question 35 — A

Answer: Analyse the data in a Colab Enterprise notebook. Colab Enterprise provides managed runtimes under project IAM. Colab Enterprise gives a managed notebook runtime with project IAM and BigQuery access. Local study-map skill 2.2 (Colab Enterprise and Jupyter Notebooks), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Colab Enterprise gives a managed notebook runtime with project IAM and BigQuery access. In this case: Colab Enterprise provides managed runtimes under project IAM.
- **B:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: Colab Enterprise provides managed runtimes under project IAM.
- **C:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: Colab Enterprise provides managed runtimes under project IAM.
- **D:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Colab Enterprise provides managed runtimes under project IAM.

### Question 36 — A

Answer: Query BigQuery from the notebook with the %%bigquery magic. The BigQuery magic returns the result as a DataFrame for plotting. The magic returns a DataFrame from a SQL statement inside the notebook cell. Local study-map skill 2.2 (Colab Enterprise and Jupyter Notebooks), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. The magic returns a DataFrame from a SQL statement inside the notebook cell. In this case: The BigQuery magic returns the result as a DataFrame for plotting.
- **B:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: The BigQuery magic returns the result as a DataFrame for plotting.
- **C:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: The BigQuery magic returns the result as a DataFrame for plotting.
- **D:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: The BigQuery magic returns the result as a DataFrame for plotting.

### Question 37 — A

Answer: Write a SQL query in BigQuery and save the result. A SQL query answers the question and can be re-run for another line. A saved SQL query answers a business question and can be scheduled or exported. Local study-map skill 2.3 (Business Question Analysis), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A saved SQL query answers a business question and can be scheduled or exported. In this case: A SQL query answers the question and can be re-run for another line.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A SQL query answers the question and can be re-run for another line.
- **C:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A SQL query answers the question and can be re-run for another line.
- **D:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: A SQL query answers the question and can be re-run for another line.

### Question 38 — A

Answer: Share the dashboard with a scheduled delivery. A scheduled delivery sends the chart to the list. A scheduled delivery pushes the answer to people who will not open the tool. Local study-map skill 2.3 (Business Question Analysis), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A scheduled delivery pushes the answer to people who will not open the tool. In this case: A scheduled delivery sends the chart to the list.
- **B:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A scheduled delivery sends the chart to the list.
- **C:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A scheduled delivery sends the chart to the list.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A scheduled delivery sends the chart to the list.

### Question 39 — C

Answer: Build a governed Looker dashboard. A Looker dashboard inherits the model for every tile. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: A Looker dashboard inherits the model for every tile.
- **B:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A Looker dashboard inherits the model for every tile.
- **C:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: A Looker dashboard inherits the model for every tile.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A Looker dashboard inherits the model for every tile.

### Question 40 — A

Answer: Add a LookML measure for the calculation. A shared measure computes retention once for both. A measure declares the aggregation once so every report computes it the same way. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: A shared measure computes retention once for both.
- **B:** Incorrect for this question. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Why the correct answer wins: A shared measure computes retention once for both.
- **C:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A shared measure computes retention once for both.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A shared measure computes retention once for both.

### Question 41 — D, E

Answers: Expose the table through a LookML explore; Share the dashboard with a scheduled delivery. The explore decides which fields are offered, and the delivery leaves the tool on a schedule. An explore defines which joins and fields a report author may use. A scheduled delivery pushes the answer to people who will not open the tool. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The explore decides which fields are offered, and the delivery leaves the tool on a schedule.
- **B:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: The explore decides which fields are offered, and the delivery leaves the tool on a schedule.
- **C:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: The explore decides which fields are offered, and the delivery leaves the tool on a schedule.
- **D:** Correct. An explore defines which joins and fields a report author may use. In this case: The explore decides which fields are offered, and the delivery leaves the tool on a schedule.
- **E:** Correct. A scheduled delivery pushes the answer to people who will not open the tool. In this case: The explore decides which fields are offered, and the delivery leaves the tool on a schedule.

### Question 42 — D

Answer: Build a Looker Studio report. Looker Studio connects a spreadsheet quickly without modelling work. Looker Studio is the fast self-serve reporting surface for a small number of sources. Local study-map skill 2.5 (Looker and Looker Studio Comparison), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: Looker Studio connects a spreadsheet quickly without modelling work.
- **B:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Looker Studio connects a spreadsheet quickly without modelling work.
- **C:** Incorrect for this question. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Why the correct answer wins: Looker Studio connects a spreadsheet quickly without modelling work.
- **D:** Correct. Looker Studio is the fast self-serve reporting surface for a small number of sources. In this case: Looker Studio connects a spreadsheet quickly without modelling work.

### Question 43 — C

Answer: Build a governed Looker dashboard. Looker serves every report from one governed model. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Local study-map skill 2.5 (Looker and Looker Studio Comparison), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: Looker serves every report from one governed model.
- **B:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Looker serves every report from one governed model.
- **C:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: Looker serves every report from one governed model.
- **D:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: Looker serves every report from one governed model.

### Question 44 — B

Answer: Change the LookML parameter in the view. A LookML parameter changes the calendar for every consumer. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An explore defines which joins and fields a report author may use. Why the correct answer wins: A LookML parameter changes the calendar for every consumer.
- **B:** Correct. A LookML parameter changes the model for every dashboard that uses it rather than one tile. In this case: A LookML parameter changes the calendar for every consumer.
- **C:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: A LookML parameter changes the calendar for every consumer.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A LookML parameter changes the calendar for every consumer.

### Question 45 — D

Answer: Add a LookML measure for the calculation. A measure declares the ratio once. A measure declares the aggregation once so every report computes it the same way. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: A measure declares the ratio once.
- **B:** Incorrect for this question. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Why the correct answer wins: A measure declares the ratio once.
- **C:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A measure declares the ratio once.
- **D:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: A measure declares the ratio once.

### Question 46 — D

Answer: Expose the table through a LookML explore. An explore declares which joins a report author may use. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: An explore declares which joins a report author may use.
- **B:** Incorrect for this question. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Why the correct answer wins: An explore declares which joins a report author may use.
- **C:** Incorrect for this question. A view stores the query rather than the rows, so the answer stays current at query time. Why the correct answer wins: An explore declares which joins a report author may use.
- **D:** Correct. In this case: An explore declares which joins a report author may use.

### Question 47 — B

Answer: Train a BigQuery ML k-means model. K-means groups rows without a label. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ARIMA_PLUS forecasts a series and returns an interval per period. Why the correct answer wins: K-means groups rows without a label.
- **B:** Correct. In this case: K-means groups rows without a label.
- **C:** Incorrect for this question. Logistic regression predicts a binary outcome and trains with SQL against the table. Why the correct answer wins: K-means groups rows without a label.
- **D:** Incorrect for this question. ML.PREDICT applies a trained model to new rows and returns the prediction. Why the correct answer wins: K-means groups rows without a label.

### Question 48 — B

Answer: Train an AutoML tabular model. AutoML searches architectures for a team without modelling code. AutoML searches architectures and tuning for a team that has labels but no modelling code. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Linear regression predicts a continuous value and trains with SQL against the table. Why the correct answer wins: AutoML searches architectures for a team without modelling code.
- **B:** Correct. AutoML searches architectures and tuning for a team that has labels but no modelling code. In this case: AutoML searches architectures for a team without modelling code.
- **C:** Incorrect for this question. ML.PREDICT applies a trained model to new rows and returns the prediction. Why the correct answer wins: AutoML searches architectures for a team without modelling code.
- **D:** Incorrect for this question. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Why the correct answer wins: AutoML searches architectures for a team without modelling code.

### Question 49 — A, B

Answers: Train a BigQuery ML logistic regression model; Train a BigQuery ML ARIMA_PLUS model. Logistic regression returns the flag, and ARIMA_PLUS returns the series. Logistic regression predicts a binary outcome and trains with SQL against the table. ARIMA_PLUS forecasts a series and returns an interval per period. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. ARIMA_PLUS forecasts a series and returns an interval per period. In this case: Logistic regression returns the flag, and ARIMA_PLUS returns the series.
- **B:** Correct. Logistic regression predicts a binary outcome and trains with SQL against the table. In this case: Logistic regression returns the flag, and ARIMA_PLUS returns the series.
- **C:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: Logistic regression returns the flag, and ARIMA_PLUS returns the series.
- **D:** Incorrect for this question. AutoML searches architectures and tuning for a team that has labels but no modelling code. Why the correct answer wins: Logistic regression returns the flag, and ARIMA_PLUS returns the series.
- **E:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: Logistic regression returns the flag, and ARIMA_PLUS returns the series.

### Question 50 — D

Answer: Create a BigQuery remote model over a Gemini model. A remote model sends the prompt from SQL while the rows stay put. Local study-map skill 2.8 (Remote Gemini Models in BigQuery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Fine-tuning adapts the model to the domain using labelled rows that stay in BigQuery. Why the correct answer wins: A remote model sends the prompt from SQL while the rows stay put.
- **B:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: A remote model sends the prompt from SQL while the rows stay put.
- **C:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: A remote model sends the prompt from SQL while the rows stay put.
- **D:** Correct. In this case: A remote model sends the prompt from SQL while the rows stay put.

### Question 51 — B

Answer: Create the BigQuery connection that reaches the model endpoint. The connection supplies the identity that reaches the endpoint. The connection carries the service account that BigQuery uses to call the remote model. Local study-map skill 2.8 (Remote Gemini Models in BigQuery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: The connection supplies the identity that reaches the endpoint.
- **B:** Correct. The connection carries the service account that BigQuery uses to call the remote model. In this case: The connection supplies the identity that reaches the endpoint.
- **C:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: The connection supplies the identity that reaches the endpoint.
- **D:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: The connection supplies the identity that reaches the endpoint.

### Question 52 — C

Answer: Plan collection, training, evaluation, then prediction. A plan fixes the target and the acceptance test before training begins. A planned sequence fixes the data, the metric, and the acceptance test before any model is trained. Local study-map skill 2.9 (ML Project Planning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: A plan fixes the target and the acceptance test before training begins.
- **B:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A plan fixes the target and the acceptance test before training begins.
- **C:** Correct. A planned sequence fixes the data, the metric, and the acceptance test before any model is trained. In this case: A plan fixes the target and the acceptance test before training begins.
- **D:** Incorrect for this question. Training loss measures fit to the rows it has already seen, not the answer on new rows. Why the correct answer wins: A plan fixes the target and the acceptance test before training begins.

### Question 53 — D, E

Answers: Hold the most recent period out as the test set; Hold out whole entities so none spans both splits. A time split tests later periods, and a grouped split holds the account out entirely. A time-ordered split tests the model on rows that come after the ones it learned from. A grouped split keeps one customer from appearing on both sides of the evaluation. Local study-map skill 2.9 (ML Project Planning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A profile quantifies what is missing before the gaps reach a dashboard. Why the correct answer wins: A time split tests later periods, and a grouped split holds the account out entirely.
- **B:** Incorrect for this question. A held-out split gives an estimate that the training rows cannot inflate. Why the correct answer wins: A time split tests later periods, and a grouped split holds the account out entirely.
- **C:** Incorrect for this question. Training loss measures fit to the rows it has already seen, not the answer on new rows. Why the correct answer wins: A time split tests later periods, and a grouped split holds the account out entirely.
- **D:** Correct. A grouped split keeps one customer from appearing on both sides of the evaluation. In this case: A time split tests later periods, and a grouped split holds the account out entirely.
- **E:** Correct. A time-ordered split tests the model on rows that come after the ones it learned from. In this case: A time split tests later periods, and a grouped split holds the account out entirely.

### Question 54 — C

Answer: Evaluate the model with ML.EVALUATE. ML.EVALUATE returns the metrics against a labelled dataset. Local study-map skill 2.10 (BigQuery ML Training and Evaluation), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: ML.EVALUATE returns the metrics against a labelled dataset.
- **B:** Incorrect for this question. ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row. Why the correct answer wins: ML.EVALUATE returns the metrics against a labelled dataset.
- **C:** Correct. In this case: ML.EVALUATE returns the metrics against a labelled dataset.
- **D:** Incorrect for this question. ML.PREDICT applies a trained model to new rows and returns the prediction. Why the correct answer wins: ML.EVALUATE returns the metrics against a labelled dataset.

### Question 55 — D

Answer: Train a BigQuery ML boosted tree model. A boosted tree fits non-linear tabular interactions. A boosted tree model fits non-linear relationships in tabular rows. Local study-map skill 2.10 (BigQuery ML Training and Evaluation), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: A boosted tree fits non-linear tabular interactions.
- **B:** Incorrect for this question. Linear regression predicts a continuous value and trains with SQL against the table. Why the correct answer wins: A boosted tree fits non-linear tabular interactions.
- **C:** Incorrect for this question. ARIMA_PLUS forecasts a series and returns an interval per period. Why the correct answer wins: A boosted tree fits non-linear tabular interactions.
- **D:** Correct. A boosted tree model fits non-linear relationships in tabular rows. In this case: A boosted tree fits non-linear tabular interactions.

### Question 56 — D

Answer: Score the rows with ML.PREDICT. ML.PREDICT applies the model to the new rows. ML.PREDICT applies a trained model to new rows and returns the prediction. Local study-map skill 2.11 (BigQuery ML Inference), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: ML.PREDICT applies the model to the new rows.
- **B:** Incorrect for this question. ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row. Why the correct answer wins: ML.PREDICT applies the model to the new rows.
- **C:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: ML.PREDICT applies the model to the new rows.
- **D:** Correct. ML.PREDICT applies a trained model to new rows and returns the prediction. In this case: ML.PREDICT applies the model to the new rows.

### Question 57 — A

Answer: Register the model version in Model Registry. Model Registry keeps each version with its lineage and approval state. Model Registry keeps each version with its lineage so a deployment names a version rather than a path. Local study-map skill 2.12 (Model Registry), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Model Registry keeps each version with its lineage so a deployment names a version rather than a path. In this case: Model Registry keeps each version with its lineage and approval state.
- **B:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: Model Registry keeps each version with its lineage and approval state.
- **C:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: Model Registry keeps each version with its lineage and approval state.
- **D:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Model Registry keeps each version with its lineage and approval state.

### Question 58 — A

Answer: Manage the SQL transformations in Dataform. Dataform resolves the dependencies and runs the graph. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: Dataform resolves the dependencies and runs the graph.
- **B:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Dataform resolves the dependencies and runs the graph.
- **C:** Incorrect for this question. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Why the correct answer wins: Dataform resolves the dependencies and runs the graph.
- **D:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Dataform resolves the dependencies and runs the graph.

### Question 59 — D

Answer: Build the pipeline in Cloud Data Fusion. Data Fusion applies the lookups and joins in a versioned visual pipeline. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Data Fusion applies the lookups and joins in a versioned visual pipeline.
- **B:** Incorrect for this question. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. Why the correct answer wins: Data Fusion applies the lookups and joins in a versioned visual pipeline.
- **C:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Data Fusion applies the lookups and joins in a versioned visual pipeline.
- **D:** Correct. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. In this case: Data Fusion applies the lookups and joins in a versioned visual pipeline.

### Question 60 — A

Answer: Run the transformation as Spark on Dataproc. Dataproc runs the Spark code the team already maintains. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Dataproc runs Spark or Hadoop jobs when the team already owns that code. In this case: Dataproc runs the Spark code the team already maintains.
- **B:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Dataproc runs the Spark code the team already maintains.
- **C:** Incorrect for this question. Dataflow runs the same code for streaming and batch and scales the workers with the load. Why the correct answer wins: Dataproc runs the Spark code the team already maintains.
- **D:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Dataproc runs the Spark code the team already maintains.

### Question 61 — B, E

Answers: Build the pipeline in Dataflow; Run the transformation as Spark on Dataproc. Dataflow gives one definition for streaming and batch, and Dataproc runs the Spark job. Dataflow runs the same code for streaming and batch and scales the workers with the load. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Dataflow gives one definition for streaming and batch, and Dataproc runs the Spark job.
- **B:** Correct. Dataflow runs the same code for streaming and batch and scales the workers with the load. In this case: Dataflow gives one definition for streaming and batch, and Dataproc runs the Spark job.
- **C:** Incorrect for this question. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. Why the correct answer wins: Dataflow gives one definition for streaming and batch, and Dataproc runs the Spark job.
- **D:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: Dataflow gives one definition for streaming and batch, and Dataproc runs the Spark job.
- **E:** Correct. Dataproc runs Spark or Hadoop jobs when the team already owns that code. In this case: Dataflow gives one definition for streaming and batch, and Dataproc runs the Spark job.

### Question 62 — B

Answer: Load the raw rows, then transform them inside the warehouse. ELT moves the transformation to the warehouse engine. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 3.2 (ELT and ETL Pipeline Design), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT moves the transformation to the warehouse engine.
- **B:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT moves the transformation to the warehouse engine.
- **C:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ELT moves the transformation to the warehouse engine.
- **D:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ELT moves the transformation to the warehouse engine.

### Question 63 — B

Answer: Extract, transform outside the warehouse, then load the result. ETL standardises the record before the destination sees it. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Local study-map skill 3.2 (ELT and ETL Pipeline Design), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A staging table separates a failed load from a failed transform, so each can be retried on its own. Why the correct answer wins: ETL standardises the record before the destination sees it.
- **B:** Correct. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. In this case: ETL standardises the record before the destination sees it.
- **C:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETL standardises the record before the destination sees it.
- **D:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: ETL standardises the record before the destination sees it.

### Question 64 — D

Answer: Schedule the SQL with a BigQuery scheduled query. A scheduled query runs one statement on a cron schedule. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **B:** Incorrect for this question. A workflow template defines the cluster and the steps so the same job can be re-run identically. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **C:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **D:** Correct. In this case: A scheduled query runs one statement on a cron schedule.

### Question 65 — B

Answer: Trigger the job from Cloud Scheduler. Cloud Scheduler calls the webhook on the cron expression. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Cloud Scheduler calls the webhook on the cron expression.
- **B:** Correct. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. In this case: Cloud Scheduler calls the webhook on the cron expression.
- **C:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Cloud Scheduler calls the webhook on the cron expression.
- **D:** Incorrect for this question. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Why the correct answer wins: Cloud Scheduler calls the webhook on the cron expression.

### Question 66 — B, C

Answers: Trigger the job from Cloud Scheduler; Create a Cloud Monitoring alert policy on the job metric. Cloud Scheduler starts the job, and the alert policy pages the owner. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. An alert policy pages someone when the backlog or the failure rate crosses a threshold. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Cloud Scheduler starts the job, and the alert policy pages the owner.
- **B:** Correct. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. In this case: Cloud Scheduler starts the job, and the alert policy pages the owner.
- **C:** Correct. An alert policy pages someone when the backlog or the failure rate crosses a threshold. In this case: Cloud Scheduler starts the job, and the alert policy pages the owner.
- **D:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Cloud Scheduler starts the job, and the alert policy pages the owner.
- **E:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Cloud Scheduler starts the job, and the alert policy pages the owner.

### Question 67 — A

Answer: Watch the job graph and per-step throughput in the Dataflow console. The job view shows the throughput per step and the watermark. The Dataflow job view shows the running graph, watermarks, and the step that is backlogged. Local study-map skill 3.4 (Dataflow Job Monitoring), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. The Dataflow job view shows the running graph, watermarks, and the step that is backlogged. In this case: The job view shows the throughput per step and the watermark.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The job view shows the throughput per step and the watermark.
- **C:** Incorrect for this question. Logs Explorer filters the log entries that explain why a worker restarted. Why the correct answer wins: The job view shows the throughput per step and the watermark.
- **D:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: The job view shows the throughput per step and the watermark.

### Question 68 — C

Answer: Write the rejected rows to a dead-letter table. A dead-letter table keeps the rejected events for replay. A dead-letter table preserves the rows that failed so they can be repaired and replayed. Local study-map skill 3.4 (Dataflow Job Monitoring), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A dead-letter table keeps the rejected events for replay.
- **B:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A dead-letter table keeps the rejected events for replay.
- **C:** Correct. A dead-letter table preserves the rows that failed so they can be repaired and replayed. In this case: A dead-letter table keeps the rejected events for replay.
- **D:** Incorrect for this question. A wide table removes the join, at the cost of duplicated rows and a wider scan. Why the correct answer wins: A dead-letter table keeps the rejected events for replay.

### Question 69 — B

Answer: Query the job logs in Logs Explorer. Logs Explorer filters the entries for that identifier. Logs Explorer filters the log entries that explain why a worker restarted. Local study-map skill 3.5 (Logs and Monitoring Review), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Logs Explorer filters the entries for that identifier.
- **B:** Correct. Logs Explorer filters the log entries that explain why a worker restarted. In this case: Logs Explorer filters the entries for that identifier.
- **C:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: Logs Explorer filters the entries for that identifier.
- **D:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: Logs Explorer filters the entries for that identifier.

### Question 70 — C

Answer: Create a Cloud Monitoring alert policy on the job metric. An alert policy pages an owner when the load fails or lags. An alert policy pages someone when the backlog or the failure rate crosses a threshold. Local study-map skill 3.5 (Logs and Monitoring Review), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: An alert policy pages an owner when the load fails or lags.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: An alert policy pages an owner when the load fails or lags.
- **C:** Correct. An alert policy pages someone when the backlog or the failure rate crosses a threshold. In this case: An alert policy pages an owner when the load fails or lags.
- **D:** Incorrect for this question. Logs Explorer filters the log entries that explain why a worker restarted. Why the correct answer wins: An alert policy pages an owner when the load fails or lags.

### Question 71 — B

Answer: Orchestrate the steps in Cloud Composer. Cloud Composer runs an Airflow DAG with dependencies and retries. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Cloud Composer runs an Airflow DAG with dependencies and retries.
- **B:** Correct. In this case: Cloud Composer runs an Airflow DAG with dependencies and retries.
- **C:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Cloud Composer runs an Airflow DAG with dependencies and retries.
- **D:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Cloud Composer runs an Airflow DAG with dependencies and retries.

### Question 72 — D

Answer: Sequence the API calls with Workflows. Workflows chains the approval step and the calls without a server. Workflows chains service calls and HTTP endpoints without running a server. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Workflows chains the approval step and the calls without a server.
- **B:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Workflows chains the approval step and the calls without a server.
- **C:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Workflows chains the approval step and the calls without a server.
- **D:** Correct. Workflows chains service calls and HTTP endpoints without running a server. In this case: Workflows chains the approval step and the calls without a server.

### Question 73 — A, E

Answers: Orchestrate the steps in Cloud Composer; Sequence the API calls with Workflows. Composer holds the graph, and Workflows runs the API sequence. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Workflows chains service calls and HTTP endpoints without running a server. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. In this case: Composer holds the graph, and Workflows runs the API sequence.
- **B:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Composer holds the graph, and Workflows runs the API sequence.
- **C:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Composer holds the graph, and Workflows runs the API sequence.
- **D:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Composer holds the graph, and Workflows runs the API sequence.
- **E:** Correct. Workflows chains service calls and HTTP endpoints without running a server. In this case: Composer holds the graph, and Workflows runs the API sequence.

### Question 74 — A

Answer: Subscribe BigQuery to the Pub/Sub topic. A BigQuery subscription writes each message into the table. Local study-map skill 3.7 (Event-Driven Ingestion with Pub/Sub), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A BigQuery subscription writes each message into the table.
- **B:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A BigQuery subscription writes each message into the table.
- **C:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: A BigQuery subscription writes each message into the table.
- **D:** Incorrect for this question. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Why the correct answer wins: A BigQuery subscription writes each message into the table.

### Question 75 — C

Answer: Start the pipeline from an Eventarc trigger. An Eventarc trigger routes the object event to the Cloud Run target. Local study-map skill 3.8 (Eventarc Triggers), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A BigQuery subscription writes each published message into a table as it arrives. Why the correct answer wins: An Eventarc trigger routes the object event to the Cloud Run target.
- **B:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: An Eventarc trigger routes the object event to the Cloud Run target.
- **C:** Correct. In this case: An Eventarc trigger routes the object event to the Cloud Run target.
- **D:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: An Eventarc trigger routes the object event to the Cloud Run target.

### Question 76 — B

Answer: Grant the predefined role that matches the task. The narrowest role that reads that table keeps the rest closed. A predefined role carries the permissions for one job and nothing else. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: The narrowest role that reads that table keeps the rest closed.
- **B:** Correct. A predefined role carries the permissions for one job and nothing else. In this case: The narrowest role that reads that table keeps the rest closed.
- **C:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: The narrowest role that reads that table keeps the rest closed.
- **D:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: The narrowest role that reads that table keeps the rest closed.

### Question 77 — D

Answer: Run the job as a dedicated service account. A service account gives the job an identity of its own. A service account gives the workload its own identity instead of borrowing a person's. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A service account gives the job an identity of its own.
- **B:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: A service account gives the job an identity of its own.
- **C:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A service account gives the job an identity of its own.
- **D:** Correct. A service account gives the workload its own identity instead of borrowing a person's. In this case: A service account gives the job an identity of its own.

### Question 78 — A, D

Answers: Assign a predefined role to the group; Run the job as a dedicated service account. A predefined role matches the job, and the service account keeps the principal non-human. A predefined role is maintained by Google and covers one service or one job function. A service account gives the workload its own identity instead of borrowing a person's. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A predefined role is maintained by Google and covers one service or one job function. In this case: A predefined role matches the job, and the service account keeps the principal non-human.
- **B:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A predefined role matches the job, and the service account keeps the principal non-human.
- **C:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A predefined role matches the job, and the service account keeps the principal non-human.
- **D:** Correct. A service account gives the workload its own identity instead of borrowing a person's. In this case: A predefined role matches the job, and the service account keeps the principal non-human.
- **E:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A predefined role matches the job, and the service account keeps the principal non-human.

### Question 79 — D

Answer: Assign a predefined role to the group. A predefined role covers that job function without basic-role breadth. A predefined role is maintained by Google and covers one service or one job function. Local study-map skill 4.2 (Basic, Predefined, and Custom Roles), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A predefined role covers that job function without basic-role breadth.
- **B:** Incorrect for this question. A custom role narrows the grant when no predefined role matches the job exactly. Why the correct answer wins: A predefined role covers that job function without basic-role breadth.
- **C:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A predefined role covers that job function without basic-role breadth.
- **D:** Correct. A predefined role is maintained by Google and covers one service or one job function. In this case: A predefined role covers that job function without basic-role breadth.

### Question 80 — C

Answer: Create a custom role with only the permissions used. A custom role withholds that one permission. A custom role narrows the grant when no predefined role matches the job exactly. Local study-map skill 4.2 (Basic, Predefined, and Custom Roles), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A predefined role is maintained by Google and covers one service or one job function. Why the correct answer wins: A custom role withholds that one permission.
- **B:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A custom role withholds that one permission.
- **C:** Correct. A custom role narrows the grant when no predefined role matches the job exactly. In this case: A custom role withholds that one permission.
- **D:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A custom role withholds that one permission.

### Question 81 — D

Answer: Enable uniform bucket-level access. Uniform bucket-level access puts every decision in IAM. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. Local study-map skill 4.3 (Cloud Storage Access Control), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: Uniform bucket-level access puts every decision in IAM.
- **B:** Incorrect for this question. Per-object ACLs are hard to audit and are overridden when uniform access is enabled. Why the correct answer wins: Uniform bucket-level access puts every decision in IAM.
- **C:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Uniform bucket-level access puts every decision in IAM.
- **D:** Correct. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. In this case: Uniform bucket-level access puts every decision in IAM.

### Question 82 — C

Answer: Issue a signed URL with a short expiry. A signed URL grants short-lived access to that object. A signed URL grants temporary read access to one object without changing IAM. Local study-map skill 4.3 (Cloud Storage Access Control), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. Why the correct answer wins: A signed URL grants short-lived access to that object.
- **B:** Incorrect for this question. An export hands over a copy that the publisher can no longer control or revoke. Why the correct answer wins: A signed URL grants short-lived access to that object.
- **C:** Correct. A signed URL grants temporary read access to one object without changing IAM. In this case: A signed URL grants short-lived access to that object.
- **D:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A signed URL grants short-lived access to that object.

### Question 83 — B

Answer: Publish the dataset through Analytics Hub. Analytics Hub shares the dataset in place under the publisher's policy. Analytics Hub shares a curated dataset with a subscriber who reads it in place. Local study-map skill 4.4 (Analytics Hub Data Sharing), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: Analytics Hub shares the dataset in place under the publisher's policy.
- **B:** Correct. Analytics Hub shares a curated dataset with a subscriber who reads it in place. In this case: Analytics Hub shares the dataset in place under the publisher's policy.
- **C:** Incorrect for this question. An export hands over a copy that the publisher can no longer control or revoke. Why the correct answer wins: Analytics Hub shares the dataset in place under the publisher's policy.
- **D:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Analytics Hub shares the dataset in place under the publisher's policy.

### Question 84 — D

Answer: Add the project to a VPC Service Controls perimeter. A perimeter blocks movement regardless of the identity's permissions. A perimeter blocks data movement outside the boundary even for an authorised identity. Local study-map skill 4.4 (Analytics Hub Data Sharing), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Analytics Hub shares a curated dataset with a subscriber who reads it in place. Why the correct answer wins: A perimeter blocks movement regardless of the identity's permissions.
- **B:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: A perimeter blocks movement regardless of the identity's permissions.
- **C:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A perimeter blocks movement regardless of the identity's permissions.
- **D:** Correct. A perimeter blocks data movement outside the boundary even for an authorised identity. In this case: A perimeter blocks movement regardless of the identity's permissions.

### Question 85 — D

Answer: Move the objects to Nearline. Nearline suits reads about once a month. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Nearline suits reads about once a month.
- **B:** Incorrect for this question. Coldline suits reads a few times a year and has a longer minimum storage duration. Why the correct answer wins: Nearline suits reads about once a month.
- **C:** Incorrect for this question. Archive is the cheapest class for data kept for compliance and read almost never. Why the correct answer wins: Nearline suits reads about once a month.
- **D:** Correct. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. In this case: Nearline suits reads about once a month.

### Question 86 — B

Answer: Keep the objects in the Standard class. Standard is for objects read frequently. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Archive is the cheapest class for data kept for compliance and read almost never. Why the correct answer wins: Standard is for objects read frequently.
- **B:** Correct. In this case: Standard is for objects read frequently.
- **C:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes. Why the correct answer wins: Standard is for objects read frequently.
- **D:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: Standard is for objects read frequently.

### Question 87 — A, C

Answers: Enable Autoclass on the bucket; Add a lifecycle rule that deletes objects after the retention period. Autoclass follows each object's access, and the delete rule removes what has expired. Autoclass moves each object between classes as its access pattern changes. A delete rule removes the objects once the retention period passes, without a person remembering. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A delete rule removes the objects once the retention period passes, without a person remembering. In this case: Autoclass follows each object's access, and the delete rule removes what has expired.
- **B:** Incorrect for this question. Keeping every version in the hot class pays the highest rate for data nobody reads. Why the correct answer wins: Autoclass follows each object's access, and the delete rule removes what has expired.
- **C:** Correct. Autoclass moves each object between classes as its access pattern changes. In this case: Autoclass follows each object's access, and the delete rule removes what has expired.
- **D:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: Autoclass follows each object's access, and the delete rule removes what has expired.
- **E:** Incorrect for this question. Coldline suits reads a few times a year and has a longer minimum storage duration. Why the correct answer wins: Autoclass follows each object's access, and the delete rule removes what has expired.

### Question 88 — A

Answer: Add a lifecycle rule that deletes objects after the retention period. A lifecycle delete rule removes the object on age. A delete rule removes the objects once the retention period passes, without a person remembering. Local study-map skill 4.6 (Lifecycle Rules and Expiration), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A delete rule removes the objects once the retention period passes, without a person remembering. In this case: A lifecycle delete rule removes the object on age.
- **B:** Incorrect for this question. Keeping every version in the hot class pays the highest rate for data nobody reads. Why the correct answer wins: A lifecycle delete rule removes the object on age.
- **C:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A lifecycle delete rule removes the object on age.
- **D:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: A lifecycle delete rule removes the object on age.

### Question 89 — B

Answer: Set a partition expiration on the table. Partition expiration drops the old partitions only. Partition expiration drops old partitions while the table keeps the recent ones. Local study-map skill 4.6 (Lifecycle Rules and Expiration), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dataset-level expiration removes tables created in it after the configured period. Why the correct answer wins: Partition expiration drops the old partitions only.
- **B:** Correct. Partition expiration drops old partitions while the table keeps the recent ones. In this case: Partition expiration drops the old partitions only.
- **C:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: Partition expiration drops the old partitions only.
- **D:** Incorrect for this question. A delete rule removes the objects once the retention period passes, without a person remembering. Why the correct answer wins: Partition expiration drops the old partitions only.

### Question 90 — B

Answer: Move the objects to Archive. Archive is the cheapest class for data read almost never. Local study-map skill 4.7 (Archiving Services), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: Archive is the cheapest class for data read almost never.
- **B:** Correct. In this case: Archive is the cheapest class for data read almost never.
- **C:** Incorrect for this question. Coldline suits reads a few times a year and has a longer minimum storage duration. Why the correct answer wins: Archive is the cheapest class for data read almost never.
- **D:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Archive is the cheapest class for data read almost never.

### Question 91 — A

Answer: Apply a bucket retention policy with a lock. A locked retention policy outranks deletion for the period. A locked retention policy prevents deletion for the period, even by an administrator. Local study-map skill 4.7 (Archiving Services), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A locked retention policy prevents deletion for the period, even by an administrator. In this case: A locked retention policy outranks deletion for the period.
- **B:** Incorrect for this question. A delete rule removes the objects once the retention period passes, without a person remembering. Why the correct answer wins: A locked retention policy outranks deletion for the period.
- **C:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A locked retention policy outranks deletion for the period.
- **D:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: A locked retention policy outranks deletion for the period.

### Question 92 — C

Answer: Enable automated backups and point-in-time recovery on Cloud SQL. Point-in-time recovery restores the state before the update. Automated backups with point-in-time recovery restore the instance to a chosen moment. Local study-map skill 4.8 (Backup and Recovery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: Point-in-time recovery restores the state before the update.
- **B:** Incorrect for this question. A zonal instance is lost with its zone and gives no automatic failover. Why the correct answer wins: Point-in-time recovery restores the state before the update.
- **C:** Correct. Automated backups with point-in-time recovery restore the instance to a chosen moment. In this case: Point-in-time recovery restores the state before the update.
- **D:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: Point-in-time recovery restores the state before the update.

### Question 93 — C

Answer: Restore into a scratch project on a schedule. A restore drill proves the plan can actually be followed. A restore drill is the only evidence that the backup can actually be used. Local study-map skill 4.8 (Backup and Recovery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A restore drill proves the plan can actually be followed.
- **B:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: A restore drill proves the plan can actually be followed.
- **C:** Correct. A restore drill is the only evidence that the backup can actually be used. In this case: A restore drill proves the plan can actually be followed.
- **D:** Incorrect for this question. A zonal instance is lost with its zone and gives no automatic failover. Why the correct answer wins: A restore drill proves the plan can actually be followed.

### Question 94 — C

Answer: Create a dual-region bucket with a replication policy. A dual-region bucket reports the replication lag between the pair. A dual-region bucket keeps a copy in a second region and reports the replication lag. Local study-map skill 4.9 (Replication), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A dual-region bucket reports the replication lag between the pair.
- **B:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A dual-region bucket reports the replication lag between the pair.
- **C:** Correct. A dual-region bucket keeps a copy in a second region and reports the replication lag. In this case: A dual-region bucket reports the replication lag between the pair.
- **D:** Incorrect for this question. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. Why the correct answer wins: A dual-region bucket reports the replication lag between the pair.

### Question 95 — A, C

Answers: Enable object versioning on the bucket; Copy the bucket to a second region with a scheduled transfer. Versioning restores the prior generation, and the scheduled copy places the second copy. Object versioning keeps a prior generation so an overwrite or delete can be reversed. A scheduled copy rebuilds a second copy but leaves a gap between runs. Local study-map skill 4.9 (Replication), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A scheduled copy rebuilds a second copy but leaves a gap between runs. In this case: Versioning restores the prior generation, and the scheduled copy places the second copy.
- **B:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: Versioning restores the prior generation, and the scheduled copy places the second copy.
- **C:** Correct. Object versioning keeps a prior generation so an overwrite or delete can be reversed. In this case: Versioning restores the prior generation, and the scheduled copy places the second copy.
- **D:** Incorrect for this question. A dual-region bucket keeps a copy in a second region and reports the replication lag. Why the correct answer wins: Versioning restores the prior generation, and the scheduled copy places the second copy.
- **E:** Incorrect for this question. A read replica serves reads from a second region and can be promoted during a regional failure. Why the correct answer wins: Versioning restores the prior generation, and the scheduled copy places the second copy.

### Question 96 — C

Answer: Choose a dual-region location. A dual-region location names the second region in the contract. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Local study-map skill 4.10 (Primary and Secondary Locations), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: A dual-region location names the second region in the contract.
- **B:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: A dual-region location names the second region in the contract.
- **C:** Correct. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. In this case: A dual-region location names the second region in the contract.
- **D:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: A dual-region location names the second region in the contract.

### Question 97 — B

Answer: Encrypt with a customer-managed key from Cloud KMS. A customer-managed key can be revoked by the customer. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. Local study-map skill 4.11 (CMEK, CSEK, and GMEK), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: A customer-managed key can be revoked by the customer.
- **B:** Correct. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. In this case: A customer-managed key can be revoked by the customer.
- **C:** Incorrect for this question. A customer-supplied key never reaches Google, and losing it loses the object. Why the correct answer wins: A customer-managed key can be revoked by the customer.
- **D:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: A customer-managed key can be revoked by the customer.

### Question 98 — B, C

Answers: Use the Google-managed default encryption; Supply a customer-supplied key with each request. Google-managed encryption needs no work, and the supplied key travels per request. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. A customer-supplied key never reaches Google, and losing it loses the object. Local study-map skill 4.11 (CMEK, CSEK, and GMEK), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data protects nothing against anyone who can read the store. Why the correct answer wins: Google-managed encryption needs no work, and the supplied key travels per request.
- **B:** Correct. A customer-supplied key never reaches Google, and losing it loses the object. In this case: Google-managed encryption needs no work, and the supplied key travels per request.
- **C:** Correct. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. In this case: Google-managed encryption needs no work, and the supplied key travels per request.
- **D:** Incorrect for this question. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. Why the correct answer wins: Google-managed encryption needs no work, and the supplied key travels per request.
- **E:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: Google-managed encryption needs no work, and the supplied key travels per request.

### Question 99 — A

Answer: Set a rotation schedule on the key. A rotation schedule limits how long a version protects new data. Local study-map skill 4.12 (Cloud KMS), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A rotation schedule limits how long a version protects new data.
- **B:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: A rotation schedule limits how long a version protects new data.
- **C:** Incorrect for this question. Destroying the key makes the ciphertext permanently unreadable, including for a restore. Why the correct answer wins: A rotation schedule limits how long a version protects new data.
- **D:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: A rotation schedule limits how long a version protects new data.

### Question 100 — C

Answer: Enforce TLS for every connection to the service. Encryption in transit protects the bytes on the wire. Encryption in transit protects the bytes while they are on the wire between client and service. Local study-map skill 4.13 (Encryption in Transit and at Rest), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data protects nothing against anyone who can read the store. Why the correct answer wins: Encryption in transit protects the bytes on the wire.
- **B:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: Encryption in transit protects the bytes on the wire.
- **C:** Correct. Encryption in transit protects the bytes while they are on the wire between client and service. In this case: Encryption in transit protects the bytes on the wire.
- **D:** Incorrect for this question. Encryption at rest protects the stored bytes on the medium, not the connection that reads them. Why the correct answer wins: Encryption in transit protects the bytes on the wire.
