# Google Cloud Associate Data Practitioner — Full-Length Mock Exam 2

Associate Data Practitioner · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Data Preparation and Ingestion (Ingestion, Reporting, Pipelines, and Access)

### 1. Raw clickstream must be kept exactly as received while the workshop rewrites its SQL weekly. Which approach fits?

- A. Load the raw rows, then transform them inside the warehouse
- B. Extract, transform outside the warehouse, then load the result
- C. Query the source system in place with a federated query
- D. Combine the extracts in a spreadsheet and upload the result

### 2. An unmasked clinical field must never reach the warehouse, not even for a minute. Which approach is required?

- A. Land the extract in a staging table before any transform runs
- B. Load the raw rows, then transform them inside the warehouse
- C. Extract, transform outside the warehouse, then load the result
- D. Query the source system in place with a federated query

### 3. Two design choices keep a replayable copy and let a failed transform be retried on its own. Which two? Select two.

- A. Extract, transform outside the warehouse, then load the result
- B. Load the raw rows, then transform them inside the warehouse
- C. Land the extract in a staging table before any transform runs
- D. Transform on the source system before the export starts
- E. Combine the extracts in a spreadsheet and upload the result

### 4. A cheap scrub before the warehouse step would remove records that currently fail late. Which design fits?

- A. Load into a staging area, apply a light transform, then transform again in the warehouse
- B. Query the source system in place with a federated query
- C. Load the raw rows, then transform them inside the warehouse
- D. Extract, transform outside the warehouse, then load the result

### 5. Two teams argue every week about whether a batch is acceptable and nothing is written down. What should be added?

- A. Profile the columns to measure the null rate before loading
- B. Select every column to be safe
- C. Load first and fix the rejected rows afterwards
- D. Define data quality rules and run a quality scan

### 6. A stream and a nightly file must be cleaned by identical logic. What should be used?

- A. Clean the stream with a Dataflow pipeline
- B. Clean the data with Spark on Dataproc
- C. Clean the rows with SQL in BigQuery
- D. Run a cron job on a Compute Engine instance

### 7. Duplicates must not reach the table and a type drift must fail loudly. Which two actions apply? Select two.

- A. Select every column to be safe
- B. Land the data as CSV
- C. Deduplicate on the business key in the cleaning step
- D. Cast the columns to the declared types before the load
- E. Load first and fix the rejected rows afterwards

### 8. Addresses differ only by trailing spaces and inconsistent casing across two sources. Where should the cleanup run?

- A. Load the extract into a notebook and work in pandas
- B. Clean the rows with SQL in BigQuery
- C. Combine the extracts in a spreadsheet and upload the result
- D. Load first and fix the rejected rows afterwards

### 9. A four terabyte Oracle database must move to Cloud SQL with a short cutover window. What should be used?

- A. Use Database Migration Service
- B. Order a Transfer Appliance
- C. Replicate the changes with Datastream
- D. Use BigQuery Data Transfer Service

### 10. Two million public URLs must be copied into a bucket by tomorrow. What should be used?

- A. Pull the files from the partner over FTP each night
- B. Order a Transfer Appliance
- C. Copy the objects with the gcloud storage command
- D. Use Storage Transfer Service

### 11. After the first bulk copy, only the last hour of inserts and updates matters. What should be used?

- A. Replicate the changes with Datastream
- B. Use Database Migration Service
- C. Use BigQuery Data Transfer Service
- D. Copy the objects with the gcloud storage command

### 12. Two recurring transfers must be scheduled by Google rather than coded by the team. Which two apply? Select two.

- A. Use Storage Transfer Service
- B. Copy the objects with the gcloud storage command
- C. Pull the files from the partner over FTP each night
- D. Use BigQuery Data Transfer Service
- E. Load the rows with a client library from the application

### 13. Nested order lines must survive the landing step intact. Which format fits?

- A. Convert the data to ORC before the load
- B. Land the data as Parquet
- C. Land the data as CSV
- D. Land the data as newline-delimited JSON

### 14. A two terabyte table is filtered on three columns in every query. Which format should be used?

- A. Land the data as Avro
- B. Land the data as Parquet
- C. Land the data as CSV
- D. Land the data as XML

### 15. A finance reviewer will open the file in Excel and check the figures by eye. Which format fits?

- A. Land the data as Parquet
- B. Land the data as CSV
- C. Land the data as newline-delimited JSON
- D. Land the data as Avro

### 16. The columns of an external file are only known when the query runs. Which approach is in use?

- A. Load the files into a native table
- B. Treat the records as structured data
- C. Apply a schema on read at query time
- D. Land the data as CSV

### 17. A paginated REST API holds forty million records and the extract must land in a bucket nightly. What should be used?

- A. Load the files with the bq load command
- B. Run the handler as a Cloud Functions function
- C. Load the rows with a client library from the application
- D. Build the pipeline in Dataflow

### 18. A Google Ads account must be pulled into a warehouse table every morning. What should be used?

- A. Replicate the changes with Datastream
- B. Use Storage Transfer Service
- C. Use BigQuery Data Transfer Service
- D. Order a Transfer Appliance

### 19. An on-premises SFTP feed needs a codeless extract with cleanup steps. What should be used?

- A. Run the transformation as Spark on Dataproc
- B. Build the pipeline in Cloud Data Fusion
- C. Document the steps and have an analyst run them each morning
- D. Run a cron job on a Compute Engine instance

### 20. A five terabyte fact table is joined to dimensions and aggregated in SQL. Which store fits?

- A. Store the rows in Bigtable
- B. Store the files in Cloud Storage
- C. Store the documents in Firestore
- D. Store the rows in BigQuery

### 21. A booking application needs relational transactions over a fixed schema. Which store fits?

- A. Store the records in Spanner
- B. Store the rows in Bigtable
- C. Store the records in Cloud SQL
- D. Store the records in AlloyDB for PostgreSQL

### 22. A PostgreSQL workload has outgrown its instance and wants PostgreSQL compatibility. Which store fits?

- A. Store the rows in BigQuery
- B. Store the documents in Firestore
- C. Store the records in Cloud SQL
- D. Store the records in AlloyDB for PostgreSQL

### 23. An app reads profile documents by identifier, and a ledger must stay consistent across two continents. Which two stores apply? Select two.

- A. Store the records in Spanner
- B. Store the files in Cloud Storage
- C. Store the rows in BigQuery
- D. Store the documents in Firestore
- E. Keep the dataset on the analyst workstation

### 24. Query latency tracks the distance between the data and the readers. What should drive the location choice?

- A. Choose a regional location
- B. Place the data in the region nearest the largest user base
- C. Choose a zonal resource
- D. Choose a dual-region location

### 25. A national health service requires records to stay inside the country. What should drive the location choice?

- A. Choose a zonal resource
- B. Place the data in the region nearest the largest user base
- C. Choose a multi-region location
- D. Place the data in the region the regulator names

### 26. A single-city user base wants the lowest storage cost that still meets the latency target. Which location type fits?

- A. Choose a multi-region location
- B. Choose a dual-region location
- C. Choose a regional location
- D. Place the data in the region nearest the largest user base

### 27. Photographs and call recordings arrive in the same bucket as JSON events. Which two classifications apply? Select two.

- A. Land the data as CSV
- B. Treat the records as semi-structured data
- C. Treat the files as unstructured data
- D. Apply a schema on read at query time
- E. Treat the records as structured data

### 28. Every record has the same twelve columns with declared types. How should the data be classified?

- A. Apply a schema on read at query time
- B. Treat the records as structured data
- C. Treat the records as semi-structured data
- D. Treat the files as unstructured data

### 29. A three hundred gigabyte daily export lands in a bucket as one object. What should be used?

- A. Stream the rows with the BigQuery Storage Write API
- B. Load the files with the bq load command
- C. Load the rows with a client library from the application
- D. Copy the objects with the gcloud storage command

### 30. A Java service produces batches and must write them as it goes. What should be used?

- A. Copy the objects with the gcloud storage command
- B. Load the rows with a client library from the application
- C. Use Storage Transfer Service
- D. Load the files with the bq load command

---

## Domain 2 — Data Analysis and Presentation (Files, Formats, Dashboards, and Governance)

### 31. Monthly cohort retention must be recomputed whenever a reviewer asks. What should be used?

- A. Create a BigQuery materialized view
- B. Export the query result to a spreadsheet for the business team
- C. Write a SQL query in BigQuery and save the result
- D. Create a BigQuery view over the join

### 32. Files in a bucket must be queried before anyone agrees to load them. What should be used?

- A. Create a BigQuery view over the join
- B. Create a BigQuery materialized view
- C. Load the files into a native table
- D. Query the files through an external table

### 33. A report filters on one date column and repeats the same heavy aggregation. Which two changes cut both cost and time? Select two.

- A. Export the query result to a spreadsheet for the business team
- B. Select every column to be safe
- C. Turn off the result cache to force a fresh read
- D. Filter the query on the partition column
- E. Create a BigQuery materialized view

### 34. A query over external files has become the slowest job in the warehouse. What should be done?

- A. Query the objects through BigLake tables
- B. Denormalise the tables into one wide table
- C. Query the files through an external table
- D. Load the files into a native table

### 35. A notebook runtime must exist inside the project with no virtual machine to patch. What should be used?

- A. Load the extract into a notebook and work in pandas
- B. Keep the dataset on the analyst workstation
- C. Upload a CSV extract into the notebook and analyse it there
- D. Analyse the data in a Colab Enterprise notebook

### 36. A cell must chart the result of a warehouse query without an export step. What should be used?

- A. Query BigQuery from the notebook with the %%bigquery magic
- B. Load the extract into a notebook and work in pandas
- C. Upload a CSV extract into the notebook and analyse it there
- D. Export the query result to a spreadsheet for the business team

### 37. An executive asks why margin fell in March and needs the driver by name. What should be produced?

- A. Turn off the result cache to force a fresh read
- B. Share the dashboard with a scheduled delivery
- C. Document the steps and have an analyst run them each morning
- D. Write a SQL query in BigQuery and save the result

### 38. Two reports disagree on churn because each author wrote a different ratio. What should be added?

- A. Add a LookML measure for the calculation
- B. Select every column to be safe
- C. Expose the table through a LookML explore
- D. Share the dashboard with a scheduled delivery

### 39. A new dashboard must reuse the certified revenue definition and stay governed. Which two components apply? Select two.

- A. Add a LookML measure for the calculation
- B. Turn off the result cache to force a fresh read
- C. Export the query result to a spreadsheet for the business team
- D. Build a Looker Studio report
- E. Build a governed Looker dashboard

### 40. Finance wants one surface where the metric definition cannot be edited tile by tile. What should be used?

- A. Export the query result to a spreadsheet for the business team
- B. Upload a CSV extract into the notebook and analyse it there
- C. Build a governed Looker dashboard
- D. Build a Looker Studio report

### 41. A distribution list must receive the dashboard every Monday without opening the tool. What should be configured?

- A. Share the dashboard with a scheduled delivery
- B. Export the query result to a spreadsheet for the business team
- C. Document the steps and have an analyst run them each morning
- D. Turn off the result cache to force a fresh read

### 42. One analyst, three sources, and a report needed before the end of the day. What should be used?

- A. Build a governed Looker dashboard
- B. Orchestrate the steps in Cloud Composer
- C. Change the LookML parameter in the view
- D. Build a Looker Studio report

### 43. Row-level access must follow the user across twenty different reports. What should be used?

- A. Build a governed Looker dashboard
- B. Build a Looker Studio report
- C. Issue a signed URL with a short expiry
- D. Export the query result to a spreadsheet for the business team

### 44. The definition of an active account must change for every report at once. What should be changed?

- A. Export the query result to a spreadsheet for the business team
- B. Change the LookML parameter in the view
- C. Add a LookML measure for the calculation
- D. Turn off the result cache to force a fresh read

### 45. A fiscal calendar and a restricted join must both apply to every consumer. Which two changes belong in the model? Select two.

- A. Export the query result to a spreadsheet for the business team
- B. Change the LookML parameter in the view
- C. Turn off the result cache to force a fresh read
- D. Share the dashboard with a scheduled delivery
- E. Expose the table through a LookML explore

### 46. Report authors keep joining a table that should be off limits to them. What should be added?

- A. Add a LookML measure for the calculation
- B. Expose the table through a LookML explore
- C. Turn off the result cache to force a fresh read
- D. Write a SQL query in BigQuery and save the result

### 47. A product team has labelled images and no one who can write a training loop. What should be used?

- A. Land the data as Parquet
- B. Score the rows with ML.PREDICT
- C. Train a BigQuery ML linear regression model
- D. Train an AutoML tabular model

### 48. Two questions remain: which customers form natural groups, and which will churn in a non-linear way. Which two model types apply? Select two.

- A. Train an AutoML tabular model
- B. Train a BigQuery ML ARIMA_PLUS model
- C. Generate the forecast with ML.FORECAST
- D. Train a BigQuery ML boosted tree model
- E. Train a BigQuery ML k-means model

### 49. A yes-or-no outcome must come back as a probability. Which model type fits?

- A. Train a BigQuery ML ARIMA_PLUS model
- B. Train a BigQuery ML linear regression model
- C. Train a BigQuery ML logistic regression model
- D. Train a BigQuery ML k-means model

### 50. Free-text incident notes must be classified per row without an export. What should be used?

- A. Create a BigQuery remote model over a Gemini model
- B. Fine-tune a Gemini model from the warehouse rows
- C. Land the data as newline-delimited JSON
- D. Load the extract into a notebook and work in pandas

### 51. A new remote model cannot be created because no identity can reach the endpoint yet. What should be created?

- A. Stream the rows with the BigQuery Storage Write API
- B. Issue a signed URL with a short expiry
- C. Create the BigQuery connection that reaches the model endpoint
- D. Load the files with the bq load command

### 52. The team cannot agree on which metric matters before the first experiment. What should be settled first?

- A. Ship the model once the training loss looks good
- B. Run a cron job on a Compute Engine instance
- C. Plan collection, training, evaluation, then prediction
- D. Document the steps and have an analyst run them each morning

### 53. The final holdout must never inform a tuning decision. What should be done?

- A. Hold out a labelled split before training
- B. Denormalise the tables into one wide table
- C. Ship the model once the training loss looks good
- D. Evaluate the model with ML.EVALUATE

### 54. AUC and precision must both be reported to the risk committee. What should be used?

- A. Score the rows with ML.PREDICT
- B. Evaluate the model with ML.EVALUATE
- C. Generate the forecast with ML.FORECAST
- D. Explain the prediction with ML.EXPLAIN_PREDICT

### 55. A continuous target moves in a straight line with two predictors. Which model type fits?

- A. Train a BigQuery ML linear regression model
- B. Train a BigQuery ML boosted tree model
- C. Train a BigQuery ML k-means model
- D. Train a BigQuery ML logistic regression model

### 56. Every active customer must be scored weekly and the result written back. What should be used?

- A. Explain the prediction with ML.EXPLAIN_PREDICT
- B. Generate the forecast with ML.FORECAST
- C. Evaluate the model with ML.EVALUATE
- D. Score the rows with ML.PREDICT

### 57. Two teams deploy the same model and nobody can say which version is live. What should be done?

- A. Stream the rows with the BigQuery Storage Write API
- B. Register the model version in Model Registry
- C. Export the query result to a spreadsheet for the business team
- D. Keep the dataset on the analyst workstation

---

## Domain 3 — Data Pipeline Orchestration (Streaming, Scheduling, Modelling, and Recovery)

### 58. ELT SQL must be versioned in git and run in dependency order. What should be used?

- A. Manage the SQL transformations in Dataform
- B. Build the pipeline in Cloud Data Fusion
- C. Run a cron job on a Compute Engine instance
- D. Run the transformation as Spark on Dataproc

### 59. A team owns Scala code that reads Avro and needs a cluster to run it. What should be used?

- A. Build the pipeline in Dataflow
- B. Build the pipeline in Cloud Data Fusion
- C. Run the transformation as Spark on Dataproc
- D. Run the handler as a Cloud Functions function

### 60. The event path needs streaming parity and the SQL layer needs version control. Which two tools apply? Select two.

- A. Document the steps and have an analyst run them each morning
- B. Manage the SQL transformations in Dataform
- C. Run the handler as a Cloud Functions function
- D. Build the pipeline in Dataflow
- E. Trigger the job from Cloud Scheduler

### 61. Twelve sources must be joined by a team that does not write code. What should be used?

- A. Manage the SQL transformations in Dataform
- B. Run the transformation as Spark on Dataproc
- C. Build the pipeline in Cloud Data Fusion
- D. Sequence the API calls with Workflows

### 62. Warehouse compute is cheaper than the source system's, and the raw data must be kept. Which design fits?

- A. Transform on the source system before the export starts
- B. Load the raw rows, then transform them inside the warehouse
- C. Query the source system in place with a federated query
- D. Extract, transform outside the warehouse, then load the result

### 63. A cheap scrub before the warehouse step would cut the volume the warehouse has to read. Which design fits?

- A. Extract, transform outside the warehouse, then load the result
- B. Load the raw rows, then transform them inside the warehouse
- C. Load into a staging area, apply a light transform, then transform again in the warehouse
- D. Land the extract in a staging table before any transform runs

### 64. A daily aggregate must refresh at 03:00 with no operator present. What should be used?

- A. Sequence the API calls with Workflows
- B. Run a cron job on a Compute Engine instance
- C. Schedule the SQL with a BigQuery scheduled query
- D. Trigger the job from Cloud Scheduler

### 65. A job outside SQL must run hourly, and an owner must be paged when it fails. Which two components apply? Select two.

- A. Document the steps and have an analyst run them each morning
- B. Run a cron job on a Compute Engine instance
- C. Turn off the result cache to force a fresh read
- D. Create a Cloud Monitoring alert policy on the job metric
- E. Trigger the job from Cloud Scheduler

### 66. Yesterday's scheduled run failed and the missed window must be rebuilt. What should be done?

- A. Select every column to be safe
- B. Re-run the scheduled query with a wider date range
- C. Turn off the result cache to force a fresh read
- D. Schedule the SQL with a BigQuery scheduled query

### 67. The watermarks of a streaming job have stopped advancing. Where should the team look?

- A. Watch the job graph and per-step throughput in the Dataflow console
- B. Share the dashboard with a scheduled delivery
- C. Write a SQL query in BigQuery and save the result
- D. Query the job logs in Logs Explorer

### 68. A pipeline quietly rejects two per cent of its input and no one can inspect those rows. What should be added?

- A. Denormalise the tables into one wide table
- B. Write the rejected rows to a dead-letter table
- C. Load first and fix the rejected rows afterwards
- D. Select every column to be safe

### 69. A batch job exits with a code nobody on the team recognises. Where should the team look?

- A. Turn off the result cache to force a fresh read
- B. Query the job logs in Logs Explorer
- C. Document the steps and have an analyst run them each morning
- D. Write a SQL query in BigQuery and save the result

### 70. The team first learns about a failed load from the users of the report. What should be added?

- A. Share the dashboard with a scheduled delivery
- B. Query the job logs in Logs Explorer
- C. Create a Cloud Monitoring alert policy on the job metric
- D. Document the steps and have an analyst run them each morning

### 71. Two HTTP services must be called in sequence with no server to operate. What should be used?

- A. Run the handler as a Cloud Functions function
- B. Sequence the API calls with Workflows
- C. Orchestrate the steps in Cloud Composer
- D. Schedule the SQL with a BigQuery scheduled query

### 72. A run must start when a file lands and must hold dependencies across three systems. Which two components apply? Select two.

- A. Document the steps and have an analyst run them each morning
- B. Run a cron job on a Compute Engine instance
- C. Schedule the SQL with a BigQuery scheduled query
- D. Orchestrate the steps in Cloud Composer
- E. Start the pipeline from an Eventarc trigger

### 73. The same Spark job must be reproduced from a stored definition rather than hand-submitted. What should be used?

- A. Document the steps and have an analyst run them each morning
- B. Run a cron job on a Compute Engine instance
- C. Trigger the job from Cloud Scheduler
- D. Submit the job through a Dataproc workflow template

### 74. Sensor readings must appear in a table within seconds of being published. What should be used?

- A. Start the pipeline from an Eventarc trigger
- B. Schedule the SQL with a BigQuery scheduled query
- C. Subscribe BigQuery to the Pub/Sub topic
- D. Load the files with the bq load command

### 75. An object landing in a bucket must start a Cloud Run job immediately. What should be used?

- A. Subscribe BigQuery to the Pub/Sub topic
- B. Start the pipeline from an Eventarc trigger
- C. Trigger the job from Cloud Scheduler
- D. Schedule the SQL with a BigQuery scheduled query

---

## Domain 4 — Data Management (Warehouse Analytics, Orchestration, and Key Management)

### 76. A data engineer must run jobs in one project and read nothing else. What should be granted?

- A. Assign a predefined role to the group
- B. Create a custom role with only the permissions used
- C. Grant the basic Owner role to the team
- D. Make the bucket public so the partner can read it

### 77. A workload's identity and its network boundary must both be limited. Which two controls apply? Select two.

- A. Make the bucket public so the partner can read it
- B. Grant the role to the whole domain
- C. Grant the basic Owner role to the team
- D. Run the job as a dedicated service account
- E. Add the project to a VPC Service Controls perimeter

### 78. A vendor asks for BigQuery Admin so it can read a single view. What should be granted instead?

- A. Grant the predefined role that matches the task
- B. Make the bucket public so the partner can read it
- C. Grant the role to the whole domain
- D. Grant the basic Owner role to the team

### 79. Every matching predefined role carries permissions the auditor objects to. What should be created?

- A. Create a custom role with only the permissions used
- B. Grant the basic Owner role to the team
- C. Grant the role to the whole domain
- D. Assign a predefined role to the group

### 80. A new analyst needs the standard read permissions for the warehouse. What should be granted?

- A. Issue a signed URL with a short expiry
- B. Grant the basic Owner role to the team
- C. Create a custom role with only the permissions used
- D. Assign a predefined role to the group

### 81. IAM must be the only place where object access is decided. What should be enabled?

- A. Manage per-object ACLs on the bucket
- B. Enable uniform bucket-level access
- C. Make the bucket public so the partner can read it
- D. Issue a signed URL with a short expiry

### 82. A journalist needs thirty minutes of access to one recording. What should be issued?

- A. Issue a signed URL with a short expiry
- B. Enable uniform bucket-level access
- C. Make the bucket public so the partner can read it
- D. Export the table to a bucket the partner owns

### 83. Two subsidiaries need the same curated dataset while the centre keeps control. What should be used?

- A. Publish the dataset through Analytics Hub
- B. Export the table to a bucket the partner owns
- C. Make the bucket public so the partner can read it
- D. Issue a signed URL with a short expiry

### 84. Data must not move outside the project boundary even for an authorised identity. What should be applied?

- A. Issue a signed URL with a short expiry
- B. Publish the dataset through Analytics Hub
- C. Make the bucket public so the partner can read it
- D. Add the project to a VPC Service Controls perimeter

### 85. A web tier reads the same images every minute. Which class fits?

- A. Keep the objects in the Standard class
- B. Move the objects to Archive
- C. Enable Autoclass on the bucket
- D. Move the objects to Nearline

### 86. Regulatory copies are read once in seven years. Which class fits?

- A. Move the objects to Nearline
- B. Move the objects to Coldline
- C. Keep the objects in the Standard class
- D. Move the objects to Archive

### 87. Nobody wants to classify four million objects by hand, and the bill must come down. Which two options apply? Select two.

- A. Keep every version in the Standard class forever
- B. Enable Autoclass on the bucket
- C. Leave the objects in place and review them next year
- D. Move the objects to Coldline
- E. Add a lifecycle rule that changes the storage class

### 88. Call recordings must disappear thirty days after upload with no manual step. What should be added?

- A. Leave the objects in place and review them next year
- B. Add a lifecycle rule that deletes objects after the retention period
- C. Enable object versioning on the bucket
- D. Keep every version in the Standard class forever

### 89. Tables created by an experiment must vanish a week after they are created. What should be set?

- A. Set a table expiration on the dataset
- B. Set a partition expiration on the table
- C. Add a lifecycle rule that deletes objects after the retention period
- D. Leave the objects in place and review them next year

### 90. Legal hold must make early deletion impossible even for an administrator. What should be applied?

- A. Leave the objects in place and review them next year
- B. Add a lifecycle rule that deletes objects after the retention period
- C. Apply a bucket retention policy with a lock
- D. Enable object versioning on the bucket

### 91. Objects must move to a cheaper class automatically after ninety days. What should be applied?

- A. Add a lifecycle rule that deletes objects after the retention period
- B. Move the objects to Nearline
- C. Enable Autoclass on the bucket
- D. Add a lifecycle rule that changes the storage class

### 92. An unproven backup protects nothing until someone proves that it restores. What should be done?

- A. Rely on the disk snapshot the platform keeps
- B. Deploy a single zonal instance to keep the cost down
- C. Restore into a scratch project on a schedule
- D. Copy the bucket to a second region with a scheduled transfer

### 93. A regional failure must not lose writes, and a bad migration must be reversible. Which two measures apply? Select two.

- A. Enable automated backups and point-in-time recovery on Cloud SQL
- B. Create a multi-region bucket
- C. Rely on the disk snapshot the platform keeps
- D. Deploy a single zonal instance to keep the cost down
- E. Create a Cloud SQL read replica in another region

### 94. Two specific regions must hold the objects, and the lag between them must be visible. What should be used?

- A. Rely on the disk snapshot the platform keeps
- B. Create a dual-region bucket with a replication policy
- C. Copy the bucket to a second region with a scheduled transfer
- D. Create a multi-region bucket

### 95. An accidental overwrite of one object must be reversible. What should be enabled?

- A. Leave the objects in place and review them next year
- B. Copy the bucket to a second region with a scheduled transfer
- C. Enable object versioning on the bucket
- D. Apply a bucket retention policy with a lock

### 96. The design must name an explicit primary and secondary region for the replica. Which location type fits?

- A. Choose a regional location
- B. Choose a multi-region location
- C. Choose a zonal resource
- D. Choose a dual-region location

### 97. The customer must control the key and a control framework requires yearly rotation. Which two apply? Select two.

- A. Set a rotation schedule on the key
- B. Encrypt with a customer-managed key from Cloud KMS
- C. Put the key in the application configuration file
- D. Supply a customer-supplied key with each request
- E. Use the Google-managed default encryption

### 98. The key must never exist in Google's infrastructure at any point. Which key model applies?

- A. Encrypt with a customer-managed key from Cloud KMS
- B. Create the key in a Cloud KMS key ring in the data region
- C. Supply a customer-supplied key with each request
- D. Use the Google-managed default encryption

### 99. The key must be created in the same region as the data it protects. What should be configured?

- A. Use the Google-managed default encryption
- B. Set a rotation schedule on the key
- C. Put the key in the application configuration file
- D. Create the key in a Cloud KMS key ring in the data region

### 100. An auditor asks how the stored bytes on the medium are protected after the client disconnects. What should be confirmed?

- A. Put the key in the application configuration file
- B. Enforce TLS for every connection to the service
- C. Confirm the data is encrypted at rest by the storage service
- D. Encrypt in the client and store the key next to the data

---

## Answer key and explanations

### Question 1 — A

Answer: Load the raw rows, then transform them inside the warehouse. ELT lands the raw rows and transforms them in place, so a rewrite needs no new extract. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT lands the raw rows and transforms them in place, so a rewrite needs no new extract.
- **B:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT lands the raw rows and transforms them in place, so a rewrite needs no new extract.
- **C:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ELT lands the raw rows and transforms them in place, so a rewrite needs no new extract.
- **D:** Incorrect for this question. A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run. Why the correct answer wins: ELT lands the raw rows and transforms them in place, so a rewrite needs no new extract.

### Question 2 — C

Answer: Extract, transform outside the warehouse, then load the result. ETL masks the record before it enters the warehouse, so the raw value is never stored there. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A staging table separates a failed load from a failed transform, so each can be retried on its own. Why the correct answer wins: ETL masks the record before it enters the warehouse, so the raw value is never stored there.
- **B:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETL masks the record before it enters the warehouse, so the raw value is never stored there.
- **C:** Correct. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. In this case: ETL masks the record before it enters the warehouse, so the raw value is never stored there.
- **D:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ETL masks the record before it enters the warehouse, so the raw value is never stored there.

### Question 3 — B, C

Answers: Load the raw rows, then transform them inside the warehouse; Land the extract in a staging table before any transform runs. ELT retains the raw rows, and a staging table isolates the failed step from the load. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. A staging table separates a failed load from a failed transform, so each can be retried on its own. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT retains the raw rows, and a staging table isolates the failed step from the load.
- **B:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT retains the raw rows, and a staging table isolates the failed step from the load.
- **C:** Correct. A staging table separates a failed load from a failed transform, so each can be retried on its own. In this case: ELT retains the raw rows, and a staging table isolates the failed step from the load.
- **D:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ELT retains the raw rows, and a staging table isolates the failed step from the load.
- **E:** Incorrect for this question. A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run. Why the correct answer wins: ELT retains the raw rows, and a staging table isolates the failed step from the load.

### Question 4 — A

Answer: Load into a staging area, apply a light transform, then transform again in the warehouse. ETLT adds a pre-warehouse cleanup so the warehouse transform starts from cleaner rows. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: ETLT adds a pre-warehouse cleanup so the warehouse transform starts from cleaner rows.
- **B:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ETLT adds a pre-warehouse cleanup so the warehouse transform starts from cleaner rows.
- **C:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETLT adds a pre-warehouse cleanup so the warehouse transform starts from cleaner rows.
- **D:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ETLT adds a pre-warehouse cleanup so the warehouse transform starts from cleaner rows.

### Question 5 — D

Answer: Define data quality rules and run a quality scan. Declared rules turn the argument into a test that runs on every load. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A profile quantifies what is missing before the gaps reach a dashboard. Why the correct answer wins: Declared rules turn the argument into a test that runs on every load.
- **B:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: Declared rules turn the argument into a test that runs on every load.
- **C:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: Declared rules turn the argument into a test that runs on every load.
- **D:** Correct. In this case: Declared rules turn the argument into a test that runs on every load.

### Question 6 — A

Answer: Clean the stream with a Dataflow pipeline. A Dataflow pipeline applies one cleaning definition to both streaming and batch input. A Dataflow pipeline applies the same cleaning logic to streaming and batch records. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A Dataflow pipeline applies the same cleaning logic to streaming and batch records. In this case: A Dataflow pipeline applies one cleaning definition to both streaming and batch input.
- **B:** Incorrect for this question. Spark suits large files that need custom code rather than SQL. Why the correct answer wins: A Dataflow pipeline applies one cleaning definition to both streaming and batch input.
- **C:** Incorrect for this question. SQL inside the warehouse removes duplicates, trims values, and casts types where the data already sits. Why the correct answer wins: A Dataflow pipeline applies one cleaning definition to both streaming and batch input.
- **D:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: A Dataflow pipeline applies one cleaning definition to both streaming and batch input.

### Question 7 — C, D

Answers: Deduplicate on the business key in the cleaning step; Cast the columns to the declared types before the load. A business key removes the duplicates, and an explicit cast surfaces the drift at load time. Retries and restatements create duplicate rows unless the load deduplicates on a stable key. An explicit cast turns a silent type drift into a visible failure at load time. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A business key removes the duplicates, and an explicit cast surfaces the drift at load time.
- **B:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: A business key removes the duplicates, and an explicit cast surfaces the drift at load time.
- **C:** Correct. Retries and restatements create duplicate rows unless the load deduplicates on a stable key. In this case: A business key removes the duplicates, and an explicit cast surfaces the drift at load time.
- **D:** Correct. An explicit cast turns a silent type drift into a visible failure at load time. In this case: A business key removes the duplicates, and an explicit cast surfaces the drift at load time.
- **E:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A business key removes the duplicates, and an explicit cast surfaces the drift at load time.

### Question 8 — B

Answer: Clean the rows with SQL in BigQuery. SQL in the warehouse fixes the values where the data already sits. SQL inside the warehouse removes duplicates, trims values, and casts types where the data already sits. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: SQL in the warehouse fixes the values where the data already sits.
- **B:** Correct. SQL inside the warehouse removes duplicates, trims values, and casts types where the data already sits. In this case: SQL in the warehouse fixes the values where the data already sits.
- **C:** Incorrect for this question. A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run. Why the correct answer wins: SQL in the warehouse fixes the values where the data already sits.
- **D:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: SQL in the warehouse fixes the values where the data already sits.

### Question 9 — A

Answer: Use Database Migration Service. Database Migration Service performs the move with continuous replication until the cutover. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. In this case: Database Migration Service performs the move with continuous replication until the cutover.
- **B:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: Database Migration Service performs the move with continuous replication until the cutover.
- **C:** Incorrect for this question. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Why the correct answer wins: Database Migration Service performs the move with continuous replication until the cutover.
- **D:** Incorrect for this question. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Why the correct answer wins: Database Migration Service performs the move with continuous replication until the cutover.

### Question 10 — D

Answer: Use Storage Transfer Service. Storage Transfer Service reads an HTTP list and copies the objects in parallel. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A hand-built FTP pull has no retry, no manifest, and no record of what arrived. Why the correct answer wins: Storage Transfer Service reads an HTTP list and copies the objects in parallel.
- **B:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: Storage Transfer Service reads an HTTP list and copies the objects in parallel.
- **C:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: Storage Transfer Service reads an HTTP list and copies the objects in parallel.
- **D:** Correct. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. In this case: Storage Transfer Service reads an HTTP list and copies the objects in parallel.

### Question 11 — A

Answer: Replicate the changes with Datastream. Datastream captures the change stream rather than copying the table again. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. In this case: Datastream captures the change stream rather than copying the table again.
- **B:** Incorrect for this question. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. Why the correct answer wins: Datastream captures the change stream rather than copying the table again.
- **C:** Incorrect for this question. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Why the correct answer wins: Datastream captures the change stream rather than copying the table again.
- **D:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: Datastream captures the change stream rather than copying the table again.

### Question 12 — A, D

Answers: Use Storage Transfer Service; Use BigQuery Data Transfer Service. Storage Transfer Service schedules the object copy, and BigQuery Data Transfer Service schedules the warehouse load. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. In this case: Storage Transfer Service schedules the object copy, and BigQuery Data Transfer Service schedules the warehouse load.
- **B:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: Storage Transfer Service schedules the object copy, and BigQuery Data Transfer Service schedules the warehouse load.
- **C:** Incorrect for this question. A hand-built FTP pull has no retry, no manifest, and no record of what arrived. Why the correct answer wins: Storage Transfer Service schedules the object copy, and BigQuery Data Transfer Service schedules the warehouse load.
- **D:** Correct. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. In this case: Storage Transfer Service schedules the object copy, and BigQuery Data Transfer Service schedules the warehouse load.
- **E:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: Storage Transfer Service schedules the object copy, and BigQuery Data Transfer Service schedules the warehouse load.

### Question 13 — D

Answer: Land the data as newline-delimited JSON. Newline-delimited JSON keeps the nested structure record by record. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ORC is another columnar format; choosing it adds a conversion step without a benefit over Parquet here. Why the correct answer wins: Newline-delimited JSON keeps the nested structure record by record.
- **B:** Incorrect for this question. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Why the correct answer wins: Newline-delimited JSON keeps the nested structure record by record.
- **C:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Newline-delimited JSON keeps the nested structure record by record.
- **D:** Correct. Newline-delimited JSON keeps nested fields and can be appended one record at a time. In this case: Newline-delimited JSON keeps the nested structure record by record.

### Question 14 — B

Answer: Land the data as Parquet. Parquet reads only the columns the query touches. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Avro carries its schema with the records and suits row-oriented streaming exchanges. Why the correct answer wins: Parquet reads only the columns the query touches.
- **B:** Correct. Parquet is columnar and compressed, so a scan reads only the columns a query needs. In this case: Parquet reads only the columns the query touches.
- **C:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Parquet reads only the columns the query touches.
- **D:** Incorrect for this question. XML nests well and is verbose, which makes it a poor fit for wide analytical scans. Why the correct answer wins: Parquet reads only the columns the query touches.

### Question 15 — B

Answer: Land the data as CSV. CSV is plain text that any spreadsheet opens without tooling. CSV is readable everywhere and carries no types, no schema, and no nesting. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Why the correct answer wins: CSV is plain text that any spreadsheet opens without tooling.
- **B:** Correct. CSV is readable everywhere and carries no types, no schema, and no nesting. In this case: CSV is plain text that any spreadsheet opens without tooling.
- **C:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: CSV is plain text that any spreadsheet opens without tooling.
- **D:** Incorrect for this question. Avro carries its schema with the records and suits row-oriented streaming exchanges. Why the correct answer wins: CSV is plain text that any spreadsheet opens without tooling.

### Question 16 — C

Answer: Apply a schema on read at query time. Schema on read interprets the file at query time rather than at load time. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A native table gives the warehouse its own copy and the best scan performance. Why the correct answer wins: Schema on read interprets the file at query time rather than at load time.
- **B:** Incorrect for this question. Structured data fits a declared schema of rows and columns. Why the correct answer wins: Schema on read interprets the file at query time rather than at load time.
- **C:** Correct. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. In this case: Schema on read interprets the file at query time rather than at load time.
- **D:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Schema on read interprets the file at query time rather than at load time.

### Question 17 — D

Answer: Build the pipeline in Dataflow. A Dataflow pipeline pages through the API and writes the objects without a server to babysit. Dataflow runs the same code for streaming and batch and scales the workers with the load. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A Dataflow pipeline pages through the API and writes the objects without a server to babysit.
- **B:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: A Dataflow pipeline pages through the API and writes the objects without a server to babysit.
- **C:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: A Dataflow pipeline pages through the API and writes the objects without a server to babysit.
- **D:** Correct. Dataflow runs the same code for streaming and batch and scales the workers with the load. In this case: A Dataflow pipeline pages through the API and writes the objects without a server to babysit.

### Question 18 — C

Answer: Use BigQuery Data Transfer Service. BigQuery Data Transfer Service schedules recurring loads from Google and SaaS sources. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Why the correct answer wins: BigQuery Data Transfer Service schedules recurring loads from Google and SaaS sources.
- **B:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: BigQuery Data Transfer Service schedules recurring loads from Google and SaaS sources.
- **C:** Correct. In this case: BigQuery Data Transfer Service schedules recurring loads from Google and SaaS sources.
- **D:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: BigQuery Data Transfer Service schedules recurring loads from Google and SaaS sources.

### Question 19 — B

Answer: Build the pipeline in Cloud Data Fusion. Data Fusion expresses the extract and the cleanup on a canvas. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Data Fusion expresses the extract and the cleanup on a canvas.
- **B:** Correct. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. In this case: Data Fusion expresses the extract and the cleanup on a canvas.
- **C:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Data Fusion expresses the extract and the cleanup on a canvas.
- **D:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Data Fusion expresses the extract and the cleanup on a canvas.

### Question 20 — D

Answer: Store the rows in BigQuery. BigQuery holds columnar tables for warehouse-scale scans. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: BigQuery holds columnar tables for warehouse-scale scans.
- **B:** Incorrect for this question. Cloud Storage holds objects of any shape and is the landing zone every other service can read. Why the correct answer wins: BigQuery holds columnar tables for warehouse-scale scans.
- **C:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: BigQuery holds columnar tables for warehouse-scale scans.
- **D:** Correct. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. In this case: BigQuery holds columnar tables for warehouse-scale scans.

### Question 21 — C

Answer: Store the records in Cloud SQL. Cloud SQL is a managed relational database for transaction workloads. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Spanner gives strongly consistent relational transactions across regions at global scale. Why the correct answer wins: Cloud SQL is a managed relational database for transaction workloads.
- **B:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: Cloud SQL is a managed relational database for transaction workloads.
- **C:** Correct. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. In this case: Cloud SQL is a managed relational database for transaction workloads.
- **D:** Incorrect for this question. AlloyDB is a managed PostgreSQL option for transaction workloads that want PostgreSQL compatibility. Why the correct answer wins: Cloud SQL is a managed relational database for transaction workloads.

### Question 22 — D

Answer: Store the records in AlloyDB for PostgreSQL. AlloyDB is a managed PostgreSQL option for a heavier transaction load. AlloyDB is a managed PostgreSQL option for transaction workloads that want PostgreSQL compatibility. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Why the correct answer wins: AlloyDB is a managed PostgreSQL option for a heavier transaction load.
- **B:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: AlloyDB is a managed PostgreSQL option for a heavier transaction load.
- **C:** Incorrect for this question. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Why the correct answer wins: AlloyDB is a managed PostgreSQL option for a heavier transaction load.
- **D:** Correct. AlloyDB is a managed PostgreSQL option for transaction workloads that want PostgreSQL compatibility. In this case: AlloyDB is a managed PostgreSQL option for a heavier transaction load.

### Question 23 — A, D

Answers: Store the documents in Firestore; Store the records in Spanner. Firestore serves the key lookups, and Spanner gives the cross-region consistent transactions. Firestore is a document store for application reads by key with a flexible shape. Spanner gives strongly consistent relational transactions across regions at global scale. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Spanner gives strongly consistent relational transactions across regions at global scale. In this case: Firestore serves the key lookups, and Spanner gives the cross-region consistent transactions.
- **B:** Incorrect for this question. Cloud Storage holds objects of any shape and is the landing zone every other service can read. Why the correct answer wins: Firestore serves the key lookups, and Spanner gives the cross-region consistent transactions.
- **C:** Incorrect for this question. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Why the correct answer wins: Firestore serves the key lookups, and Spanner gives the cross-region consistent transactions.
- **D:** Correct. Firestore is a document store for application reads by key with a flexible shape. In this case: Firestore serves the key lookups, and Spanner gives the cross-region consistent transactions.
- **E:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Firestore serves the key lookups, and Spanner gives the cross-region consistent transactions.

### Question 24 — B

Answer: Place the data in the region nearest the largest user base. Placing the data near the largest user base removes the distance from every query. Distance between the data and the readers shows up as latency on every query. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: Placing the data near the largest user base removes the distance from every query.
- **B:** Correct. Distance between the data and the readers shows up as latency on every query. In this case: Placing the data near the largest user base removes the distance from every query.
- **C:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: Placing the data near the largest user base removes the distance from every query.
- **D:** Incorrect for this question. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Why the correct answer wins: Placing the data near the largest user base removes the distance from every query.

### Question 25 — D

Answer: Place the data in the region the regulator names. A residency obligation fixes the geography before performance is discussed. A residency obligation fixes the geography, which removes the choice from the performance discussion. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: A residency obligation fixes the geography before performance is discussed.
- **B:** Incorrect for this question. Distance between the data and the readers shows up as latency on every query. Why the correct answer wins: A residency obligation fixes the geography before performance is discussed.
- **C:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: A residency obligation fixes the geography before performance is discussed.
- **D:** Correct. A residency obligation fixes the geography, which removes the choice from the performance discussion. In this case: A residency obligation fixes the geography before performance is discussed.

### Question 26 — C

Answer: Choose a regional location. One region is the cheapest placement that still serves a local user base. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: One region is the cheapest placement that still serves a local user base.
- **B:** Incorrect for this question. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Why the correct answer wins: One region is the cheapest placement that still serves a local user base.
- **C:** Correct. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. In this case: One region is the cheapest placement that still serves a local user base.
- **D:** Incorrect for this question. Distance between the data and the readers shows up as latency on every query. Why the correct answer wins: One region is the cheapest placement that still serves a local user base.

### Question 27 — B, C

Answers: Treat the files as unstructured data; Treat the records as semi-structured data. Images and audio have no field model, and JSON varies between records. Unstructured data has no field model at all, such as images, audio, or free documents. Semi-structured data has a flexible shape such as JSON, where fields vary between records. Local study-map skill 1.8 (Structured, Semi-Structured, and Unstructured Data), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Images and audio have no field model, and JSON varies between records.
- **B:** Correct. Semi-structured data has a flexible shape such as JSON, where fields vary between records. In this case: Images and audio have no field model, and JSON varies between records.
- **C:** Correct. Unstructured data has no field model at all, such as images, audio, or free documents. In this case: Images and audio have no field model, and JSON varies between records.
- **D:** Incorrect for this question. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Why the correct answer wins: Images and audio have no field model, and JSON varies between records.
- **E:** Incorrect for this question. Structured data fits a declared schema of rows and columns. Why the correct answer wins: Images and audio have no field model, and JSON varies between records.

### Question 28 — B

Answer: Treat the records as structured data. A declared schema of rows and columns is structured data. Local study-map skill 1.8 (Structured, Semi-Structured, and Unstructured Data), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Why the correct answer wins: A declared schema of rows and columns is structured data.
- **B:** Correct. In this case: A declared schema of rows and columns is structured data.
- **C:** Incorrect for this question. Semi-structured data has a flexible shape such as JSON, where fields vary between records. Why the correct answer wins: A declared schema of rows and columns is structured data.
- **D:** Incorrect for this question. Unstructured data has no field model at all, such as images, audio, or free documents. Why the correct answer wins: A declared schema of rows and columns is structured data.

### Question 29 — B

Answer: Load the files with the bq load command. A load job reads the object and writes the table in one operation. The bq load command creates a load job that reads files from Cloud Storage into a table. Local study-map skill 1.9 (Loading with CLIs and Client Libraries), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: A load job reads the object and writes the table in one operation.
- **B:** Correct. The bq load command creates a load job that reads files from Cloud Storage into a table. In this case: A load job reads the object and writes the table in one operation.
- **C:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: A load job reads the object and writes the table in one operation.
- **D:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A load job reads the object and writes the table in one operation.

### Question 30 — B

Answer: Load the rows with a client library from the application. A client library writes the rows the service already holds. A client library suits an application that already holds the rows in memory rather than files in a bucket. Local study-map skill 1.9 (Loading with CLIs and Client Libraries), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A client library writes the rows the service already holds.
- **B:** Correct. A client library suits an application that already holds the rows in memory rather than files in a bucket. In this case: A client library writes the rows the service already holds.
- **C:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: A client library writes the rows the service already holds.
- **D:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A client library writes the rows the service already holds.

### Question 31 — C

Answer: Write a SQL query in BigQuery and save the result. A saved SQL query is reproducible and can be scheduled or exported. A saved SQL query answers a business question and can be scheduled or exported. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. Why the correct answer wins: A saved SQL query is reproducible and can be scheduled or exported.
- **B:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A saved SQL query is reproducible and can be scheduled or exported.
- **C:** Correct. A saved SQL query answers a business question and can be scheduled or exported. In this case: A saved SQL query is reproducible and can be scheduled or exported.
- **D:** Incorrect for this question. A view stores the query rather than the rows, so the answer stays current at query time. Why the correct answer wins: A saved SQL query is reproducible and can be scheduled or exported.

### Question 32 — D

Answer: Query the files through an external table. An external table reads the objects where they sit without a copy. An external table reads the objects where they sit and does not copy them into storage. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A view stores the query rather than the rows, so the answer stays current at query time. Why the correct answer wins: An external table reads the objects where they sit without a copy.
- **B:** Incorrect for this question. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. Why the correct answer wins: An external table reads the objects where they sit without a copy.
- **C:** Incorrect for this question. A native table gives the warehouse its own copy and the best scan performance. Why the correct answer wins: An external table reads the objects where they sit without a copy.
- **D:** Correct. An external table reads the objects where they sit and does not copy them into storage. In this case: An external table reads the objects where they sit without a copy.

### Question 33 — D, E

Answers: Filter the query on the partition column; Create a BigQuery materialized view. A partition filter narrows the scan, and the materialized view stores the repeated result. A partition filter restricts the scan to the partitions the query needs. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A partition filter narrows the scan, and the materialized view stores the repeated result.
- **B:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A partition filter narrows the scan, and the materialized view stores the repeated result.
- **C:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A partition filter narrows the scan, and the materialized view stores the repeated result.
- **D:** Correct. A partition filter restricts the scan to the partitions the query needs. In this case: A partition filter narrows the scan, and the materialized view stores the repeated result.
- **E:** Correct. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. In this case: A partition filter narrows the scan, and the materialized view stores the repeated result.

### Question 34 — D

Answer: Load the files into a native table. Loading the files into a native table gives the engine its own copy. A native table gives the warehouse its own copy and the best scan performance. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. BigLake tables extend BigQuery access control and performance to objects that stay in Cloud Storage. Why the correct answer wins: Loading the files into a native table gives the engine its own copy.
- **B:** Incorrect for this question. A wide table removes the join, at the cost of duplicated rows and a wider scan. Why the correct answer wins: Loading the files into a native table gives the engine its own copy.
- **C:** Incorrect for this question. An external table reads the objects where they sit and does not copy them into storage. Why the correct answer wins: Loading the files into a native table gives the engine its own copy.
- **D:** Correct. A native table gives the warehouse its own copy and the best scan performance. In this case: Loading the files into a native table gives the engine its own copy.

### Question 35 — D

Answer: Analyse the data in a Colab Enterprise notebook. Colab Enterprise provides the managed runtime under project IAM. Colab Enterprise gives a managed notebook runtime with project IAM and BigQuery access. Local study-map skill 2.2 (Colab Enterprise and Jupyter Notebooks), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: Colab Enterprise provides the managed runtime under project IAM.
- **B:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Colab Enterprise provides the managed runtime under project IAM.
- **C:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: Colab Enterprise provides the managed runtime under project IAM.
- **D:** Correct. Colab Enterprise gives a managed notebook runtime with project IAM and BigQuery access. In this case: Colab Enterprise provides the managed runtime under project IAM.

### Question 36 — A

Answer: Query BigQuery from the notebook with the %%bigquery magic. The BigQuery magic returns the query result as a DataFrame in the cell. The magic returns a DataFrame from a SQL statement inside the notebook cell. Local study-map skill 2.2 (Colab Enterprise and Jupyter Notebooks), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. The magic returns a DataFrame from a SQL statement inside the notebook cell. In this case: The BigQuery magic returns the query result as a DataFrame in the cell.
- **B:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: The BigQuery magic returns the query result as a DataFrame in the cell.
- **C:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: The BigQuery magic returns the query result as a DataFrame in the cell.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: The BigQuery magic returns the query result as a DataFrame in the cell.

### Question 37 — D

Answer: Write a SQL query in BigQuery and save the result. A SQL query answers the question and can be re-run when the question changes. A saved SQL query answers a business question and can be scheduled or exported. Local study-map skill 2.3 (Business Question Analysis), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A SQL query answers the question and can be re-run when the question changes.
- **B:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: A SQL query answers the question and can be re-run when the question changes.
- **C:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A SQL query answers the question and can be re-run when the question changes.
- **D:** Correct. A saved SQL query answers a business question and can be scheduled or exported. In this case: A SQL query answers the question and can be re-run when the question changes.

### Question 38 — A

Answer: Add a LookML measure for the calculation. A shared measure computes the ratio once for every report. A measure declares the aggregation once so every report computes it the same way. Local study-map skill 2.3 (Business Question Analysis), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: A shared measure computes the ratio once for every report.
- **B:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A shared measure computes the ratio once for every report.
- **C:** Incorrect for this question. An explore defines which joins and fields a report author may use. Why the correct answer wins: A shared measure computes the ratio once for every report.
- **D:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: A shared measure computes the ratio once for every report.

### Question 39 — A, E

Answers: Add a LookML measure for the calculation; Build a governed Looker dashboard. The shared measure fixes the definition, and the Looker dashboard inherits the model. A measure declares the aggregation once so every report computes it the same way. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: The shared measure fixes the definition, and the Looker dashboard inherits the model.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The shared measure fixes the definition, and the Looker dashboard inherits the model.
- **C:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: The shared measure fixes the definition, and the Looker dashboard inherits the model.
- **D:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: The shared measure fixes the definition, and the Looker dashboard inherits the model.
- **E:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: The shared measure fixes the definition, and the Looker dashboard inherits the model.

### Question 40 — C

Answer: Build a governed Looker dashboard. A Looker dashboard reads the modelled layer for every tile. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A Looker dashboard reads the modelled layer for every tile.
- **B:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: A Looker dashboard reads the modelled layer for every tile.
- **C:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: A Looker dashboard reads the modelled layer for every tile.
- **D:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: A Looker dashboard reads the modelled layer for every tile.

### Question 41 — A

Answer: Share the dashboard with a scheduled delivery. A scheduled delivery pushes the answer to people who will not sign in. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A scheduled delivery pushes the answer to people who will not sign in.
- **B:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A scheduled delivery pushes the answer to people who will not sign in.
- **C:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A scheduled delivery pushes the answer to people who will not sign in.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A scheduled delivery pushes the answer to people who will not sign in.

### Question 42 — D

Answer: Build a Looker Studio report. Looker Studio is the fast self-serve option for a small number of sources. Local study-map skill 2.5 (Looker and Looker Studio Comparison), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Why the correct answer wins: Looker Studio is the fast self-serve option for a small number of sources.
- **B:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Looker Studio is the fast self-serve option for a small number of sources.
- **C:** Incorrect for this question. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Why the correct answer wins: Looker Studio is the fast self-serve option for a small number of sources.
- **D:** Correct. In this case: Looker Studio is the fast self-serve option for a small number of sources.

### Question 43 — A

Answer: Build a governed Looker dashboard. Looker applies one model, so access rules hold across every report built on it. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Local study-map skill 2.5 (Looker and Looker Studio Comparison), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: Looker applies one model, so access rules hold across every report built on it.
- **B:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: Looker applies one model, so access rules hold across every report built on it.
- **C:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Looker applies one model, so access rules hold across every report built on it.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: Looker applies one model, so access rules hold across every report built on it.

### Question 44 — B

Answer: Change the LookML parameter in the view. A LookML parameter changes the model for every consumer. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A LookML parameter changes the model for every consumer.
- **B:** Correct. A LookML parameter changes the model for every dashboard that uses it rather than one tile. In this case: A LookML parameter changes the model for every consumer.
- **C:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: A LookML parameter changes the model for every consumer.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A LookML parameter changes the model for every consumer.

### Question 45 — B, E

Answers: Change the LookML parameter in the view; Expose the table through a LookML explore. The parameter sets the calendar once, and the explore keeps authors off the restricted table. A LookML parameter changes the model for every dashboard that uses it rather than one tile. An explore defines which joins and fields a report author may use. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: The parameter sets the calendar once, and the explore keeps authors off the restricted table.
- **B:** Correct. A LookML parameter changes the model for every dashboard that uses it rather than one tile. In this case: The parameter sets the calendar once, and the explore keeps authors off the restricted table.
- **C:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The parameter sets the calendar once, and the explore keeps authors off the restricted table.
- **D:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: The parameter sets the calendar once, and the explore keeps authors off the restricted table.
- **E:** Correct. An explore defines which joins and fields a report author may use. In this case: The parameter sets the calendar once, and the explore keeps authors off the restricted table.

### Question 46 — B

Answer: Expose the table through a LookML explore. An explore declares which joins a report author may use. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: An explore declares which joins a report author may use.
- **B:** Correct. In this case: An explore declares which joins a report author may use.
- **C:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: An explore declares which joins a report author may use.
- **D:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: An explore declares which joins a report author may use.

### Question 47 — D

Answer: Train an AutoML tabular model. AutoML searches architectures and tuning for a team without modelling code. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Why the correct answer wins: AutoML searches architectures and tuning for a team without modelling code.
- **B:** Incorrect for this question. ML.PREDICT applies a trained model to new rows and returns the prediction. Why the correct answer wins: AutoML searches architectures and tuning for a team without modelling code.
- **C:** Incorrect for this question. Linear regression predicts a continuous value and trains with SQL against the table. Why the correct answer wins: AutoML searches architectures and tuning for a team without modelling code.
- **D:** Correct. In this case: AutoML searches architectures and tuning for a team without modelling code.

### Question 48 — D, E

Answers: Train a BigQuery ML k-means model; Train a BigQuery ML boosted tree model. K-means discovers the groups without a label, and a boosted tree fits the non-linear churn pattern. K-means groups rows without a label column, so it segments rather than predicts. A boosted tree model fits non-linear relationships in tabular rows. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. AutoML searches architectures and tuning for a team that has labels but no modelling code. Why the correct answer wins: K-means discovers the groups without a label, and a boosted tree fits the non-linear churn pattern.
- **B:** Incorrect for this question. ARIMA_PLUS forecasts a series and returns an interval per period. Why the correct answer wins: K-means discovers the groups without a label, and a boosted tree fits the non-linear churn pattern.
- **C:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: K-means discovers the groups without a label, and a boosted tree fits the non-linear churn pattern.
- **D:** Correct. A boosted tree model fits non-linear relationships in tabular rows. In this case: K-means discovers the groups without a label, and a boosted tree fits the non-linear churn pattern.
- **E:** Correct. K-means groups rows without a label column, so it segments rather than predicts. In this case: K-means discovers the groups without a label, and a boosted tree fits the non-linear churn pattern.

### Question 49 — C

Answer: Train a BigQuery ML logistic regression model. Logistic regression returns a probability for a binary outcome. Logistic regression predicts a binary outcome and trains with SQL against the table. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ARIMA_PLUS forecasts a series and returns an interval per period. Why the correct answer wins: Logistic regression returns a probability for a binary outcome.
- **B:** Incorrect for this question. Linear regression predicts a continuous value and trains with SQL against the table. Why the correct answer wins: Logistic regression returns a probability for a binary outcome.
- **C:** Correct. Logistic regression predicts a binary outcome and trains with SQL against the table. In this case: Logistic regression returns a probability for a binary outcome.
- **D:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: Logistic regression returns a probability for a binary outcome.

### Question 50 — A

Answer: Create a BigQuery remote model over a Gemini model. A remote model runs the prompt from SQL while the rows stay put. Local study-map skill 2.8 (Remote Gemini Models in BigQuery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A remote model runs the prompt from SQL while the rows stay put.
- **B:** Incorrect for this question. Fine-tuning adapts the model to the domain using labelled rows that stay in BigQuery. Why the correct answer wins: A remote model runs the prompt from SQL while the rows stay put.
- **C:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: A remote model runs the prompt from SQL while the rows stay put.
- **D:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: A remote model runs the prompt from SQL while the rows stay put.

### Question 51 — C

Answer: Create the BigQuery connection that reaches the model endpoint. The connection supplies the service account that calls the model endpoint. The connection carries the service account that BigQuery uses to call the remote model. Local study-map skill 2.8 (Remote Gemini Models in BigQuery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: The connection supplies the service account that calls the model endpoint.
- **B:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: The connection supplies the service account that calls the model endpoint.
- **C:** Correct. The connection carries the service account that BigQuery uses to call the remote model. In this case: The connection supplies the service account that calls the model endpoint.
- **D:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: The connection supplies the service account that calls the model endpoint.

### Question 52 — C

Answer: Plan collection, training, evaluation, then prediction. A plan fixes the metric and the acceptance test before any training runs. A planned sequence fixes the data, the metric, and the acceptance test before any model is trained. Local study-map skill 2.9 (ML Project Planning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Training loss measures fit to the rows it has already seen, not the answer on new rows. Why the correct answer wins: A plan fixes the metric and the acceptance test before any training runs.
- **B:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: A plan fixes the metric and the acceptance test before any training runs.
- **C:** Correct. A planned sequence fixes the data, the metric, and the acceptance test before any model is trained. In this case: A plan fixes the metric and the acceptance test before any training runs.
- **D:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A plan fixes the metric and the acceptance test before any training runs.

### Question 53 — A

Answer: Hold out a labelled split before training. A held-out split keeps the estimate independent of the tuning. A held-out split gives an estimate that the training rows cannot inflate. Local study-map skill 2.9 (ML Project Planning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A held-out split gives an estimate that the training rows cannot inflate. In this case: A held-out split keeps the estimate independent of the tuning.
- **B:** Incorrect for this question. A wide table removes the join, at the cost of duplicated rows and a wider scan. Why the correct answer wins: A held-out split keeps the estimate independent of the tuning.
- **C:** Incorrect for this question. Training loss measures fit to the rows it has already seen, not the answer on new rows. Why the correct answer wins: A held-out split keeps the estimate independent of the tuning.
- **D:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: A held-out split keeps the estimate independent of the tuning.

### Question 54 — B

Answer: Evaluate the model with ML.EVALUATE. ML.EVALUATE returns the model metrics against a labelled dataset. Local study-map skill 2.10 (BigQuery ML Training and Evaluation), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.PREDICT applies a trained model to new rows and returns the prediction. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.
- **B:** Correct. In this case: ML.EVALUATE returns the model metrics against a labelled dataset.
- **C:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.
- **D:** Incorrect for this question. ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.

### Question 55 — A

Answer: Train a BigQuery ML linear regression model. Linear regression is the interpretable choice for a linear continuous target. Linear regression predicts a continuous value and trains with SQL against the table. Local study-map skill 2.10 (BigQuery ML Training and Evaluation), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Linear regression predicts a continuous value and trains with SQL against the table. In this case: Linear regression is the interpretable choice for a linear continuous target.
- **B:** Incorrect for this question. A boosted tree model fits non-linear relationships in tabular rows. Why the correct answer wins: Linear regression is the interpretable choice for a linear continuous target.
- **C:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: Linear regression is the interpretable choice for a linear continuous target.
- **D:** Incorrect for this question. Logistic regression predicts a binary outcome and trains with SQL against the table. Why the correct answer wins: Linear regression is the interpretable choice for a linear continuous target.

### Question 56 — D

Answer: Score the rows with ML.PREDICT. ML.PREDICT applies the model to the table of new rows. ML.PREDICT applies a trained model to new rows and returns the prediction. Local study-map skill 2.11 (BigQuery ML Inference), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row. Why the correct answer wins: ML.PREDICT applies the model to the table of new rows.
- **B:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: ML.PREDICT applies the model to the table of new rows.
- **C:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: ML.PREDICT applies the model to the table of new rows.
- **D:** Correct. ML.PREDICT applies a trained model to new rows and returns the prediction. In this case: ML.PREDICT applies the model to the table of new rows.

### Question 57 — B

Answer: Register the model version in Model Registry. Model Registry keeps each version with its lineage so a deployment names one. Local study-map skill 2.12 (Model Registry), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: Model Registry keeps each version with its lineage so a deployment names one.
- **B:** Correct. In this case: Model Registry keeps each version with its lineage so a deployment names one.
- **C:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: Model Registry keeps each version with its lineage so a deployment names one.
- **D:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Model Registry keeps each version with its lineage so a deployment names one.

### Question 58 — A

Answer: Manage the SQL transformations in Dataform. Dataform versions the SQL, resolves the dependencies, and runs the graph. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: Dataform versions the SQL, resolves the dependencies, and runs the graph.
- **B:** Incorrect for this question. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Why the correct answer wins: Dataform versions the SQL, resolves the dependencies, and runs the graph.
- **C:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Dataform versions the SQL, resolves the dependencies, and runs the graph.
- **D:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Dataform versions the SQL, resolves the dependencies, and runs the graph.

### Question 59 — C

Answer: Run the transformation as Spark on Dataproc. Dataproc runs the Spark code the team already maintains. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dataflow runs the same code for streaming and batch and scales the workers with the load. Why the correct answer wins: Dataproc runs the Spark code the team already maintains.
- **B:** Incorrect for this question. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Why the correct answer wins: Dataproc runs the Spark code the team already maintains.
- **C:** Correct. Dataproc runs Spark or Hadoop jobs when the team already owns that code. In this case: Dataproc runs the Spark code the team already maintains.
- **D:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Dataproc runs the Spark code the team already maintains.

### Question 60 — B, D

Answers: Build the pipeline in Dataflow; Manage the SQL transformations in Dataform. Dataflow gives one definition for streaming and batch, and Dataform versions the SQL graph. Dataflow runs the same code for streaming and batch and scales the workers with the load. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Dataflow gives one definition for streaming and batch, and Dataform versions the SQL graph.
- **B:** Correct. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. In this case: Dataflow gives one definition for streaming and batch, and Dataform versions the SQL graph.
- **C:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Dataflow gives one definition for streaming and batch, and Dataform versions the SQL graph.
- **D:** Correct. Dataflow runs the same code for streaming and batch and scales the workers with the load. In this case: Dataflow gives one definition for streaming and batch, and Dataform versions the SQL graph.
- **E:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: Dataflow gives one definition for streaming and batch, and Dataform versions the SQL graph.

### Question 61 — C

Answer: Build the pipeline in Cloud Data Fusion. Data Fusion joins the sources on a versioned canvas. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. Why the correct answer wins: Data Fusion joins the sources on a versioned canvas.
- **B:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Data Fusion joins the sources on a versioned canvas.
- **C:** Correct. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. In this case: Data Fusion joins the sources on a versioned canvas.
- **D:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Data Fusion joins the sources on a versioned canvas.

### Question 62 — B

Answer: Load the raw rows, then transform them inside the warehouse. ELT moves the work to the cheaper engine and keeps the raw copy. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 3.2 (ELT and ETL Pipeline Design), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ELT moves the work to the cheaper engine and keeps the raw copy.
- **B:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT moves the work to the cheaper engine and keeps the raw copy.
- **C:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ELT moves the work to the cheaper engine and keeps the raw copy.
- **D:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT moves the work to the cheaper engine and keeps the raw copy.

### Question 63 — C

Answer: Load into a staging area, apply a light transform, then transform again in the warehouse. ETLT cleans before the warehouse transform so less data reaches the expensive step. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. Local study-map skill 3.2 (ELT and ETL Pipeline Design), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ETLT cleans before the warehouse transform so less data reaches the expensive step.
- **B:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETLT cleans before the warehouse transform so less data reaches the expensive step.
- **C:** Correct. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. In this case: ETLT cleans before the warehouse transform so less data reaches the expensive step.
- **D:** Incorrect for this question. A staging table separates a failed load from a failed transform, so each can be retried on its own. Why the correct answer wins: ETLT cleans before the warehouse transform so less data reaches the expensive step.

### Question 64 — C

Answer: Schedule the SQL with a BigQuery scheduled query. A scheduled query runs one statement on a cron schedule. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **B:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **C:** Correct. In this case: A scheduled query runs one statement on a cron schedule.
- **D:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.

### Question 65 — D, E

Answers: Trigger the job from Cloud Scheduler; Create a Cloud Monitoring alert policy on the job metric. Cloud Scheduler calls the job, and the alert policy pages the owner. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. An alert policy pages someone when the backlog or the failure rate crosses a threshold. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Cloud Scheduler calls the job, and the alert policy pages the owner.
- **B:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Cloud Scheduler calls the job, and the alert policy pages the owner.
- **C:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: Cloud Scheduler calls the job, and the alert policy pages the owner.
- **D:** Correct. An alert policy pages someone when the backlog or the failure rate crosses a threshold. In this case: Cloud Scheduler calls the job, and the alert policy pages the owner.
- **E:** Correct. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. In this case: Cloud Scheduler calls the job, and the alert policy pages the owner.

### Question 66 — B

Answer: Re-run the scheduled query with a wider date range. A backfill re-reads the missed window instead of waiting for the next run. A backfill re-reads the missed window rather than waiting for the next scheduled run. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A backfill re-reads the missed window instead of waiting for the next run.
- **B:** Correct. A backfill re-reads the missed window rather than waiting for the next scheduled run. In this case: A backfill re-reads the missed window instead of waiting for the next run.
- **C:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A backfill re-reads the missed window instead of waiting for the next run.
- **D:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: A backfill re-reads the missed window instead of waiting for the next run.

### Question 67 — A

Answer: Watch the job graph and per-step throughput in the Dataflow console. The job view shows the graph, the watermarks, and the step that is stuck. The Dataflow job view shows the running graph, watermarks, and the step that is backlogged. Local study-map skill 3.4 (Dataflow Job Monitoring), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. The Dataflow job view shows the running graph, watermarks, and the step that is backlogged. In this case: The job view shows the graph, the watermarks, and the step that is stuck.
- **B:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: The job view shows the graph, the watermarks, and the step that is stuck.
- **C:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: The job view shows the graph, the watermarks, and the step that is stuck.
- **D:** Incorrect for this question. Logs Explorer filters the log entries that explain why a worker restarted. Why the correct answer wins: The job view shows the graph, the watermarks, and the step that is stuck.

### Question 68 — B

Answer: Write the rejected rows to a dead-letter table. A dead-letter table keeps the rejected rows for repair and replay. A dead-letter table preserves the rows that failed so they can be repaired and replayed. Local study-map skill 3.4 (Dataflow Job Monitoring), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A wide table removes the join, at the cost of duplicated rows and a wider scan. Why the correct answer wins: A dead-letter table keeps the rejected rows for repair and replay.
- **B:** Correct. A dead-letter table preserves the rows that failed so they can be repaired and replayed. In this case: A dead-letter table keeps the rejected rows for repair and replay.
- **C:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A dead-letter table keeps the rejected rows for repair and replay.
- **D:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A dead-letter table keeps the rejected rows for repair and replay.

### Question 69 — B

Answer: Query the job logs in Logs Explorer. Logs Explorer filters the log entries that explain the exit. Local study-map skill 3.5 (Logs and Monitoring Review), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: Logs Explorer filters the log entries that explain the exit.
- **B:** Correct. In this case: Logs Explorer filters the log entries that explain the exit.
- **C:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Logs Explorer filters the log entries that explain the exit.
- **D:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: Logs Explorer filters the log entries that explain the exit.

### Question 70 — C

Answer: Create a Cloud Monitoring alert policy on the job metric. An alert policy pages an owner when the job fails. An alert policy pages someone when the backlog or the failure rate crosses a threshold. Local study-map skill 3.5 (Logs and Monitoring Review), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: An alert policy pages an owner when the job fails.
- **B:** Incorrect for this question. Logs Explorer filters the log entries that explain why a worker restarted. Why the correct answer wins: An alert policy pages an owner when the job fails.
- **C:** Correct. An alert policy pages someone when the backlog or the failure rate crosses a threshold. In this case: An alert policy pages an owner when the job fails.
- **D:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: An alert policy pages an owner when the job fails.

### Question 71 — B

Answer: Sequence the API calls with Workflows. Workflows chains the calls without a server. Workflows chains service calls and HTTP endpoints without running a server. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Workflows chains the calls without a server.
- **B:** Correct. Workflows chains service calls and HTTP endpoints without running a server. In this case: Workflows chains the calls without a server.
- **C:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Workflows chains the calls without a server.
- **D:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Workflows chains the calls without a server.

### Question 72 — D, E

Answers: Start the pipeline from an Eventarc trigger; Orchestrate the steps in Cloud Composer. Eventarc routes the object event, and Composer holds the dependencies and the retries. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Eventarc routes the object event, and Composer holds the dependencies and the retries.
- **B:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Eventarc routes the object event, and Composer holds the dependencies and the retries.
- **C:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Eventarc routes the object event, and Composer holds the dependencies and the retries.
- **D:** Correct. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. In this case: Eventarc routes the object event, and Composer holds the dependencies and the retries.
- **E:** Correct. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. In this case: Eventarc routes the object event, and Composer holds the dependencies and the retries.

### Question 73 — D

Answer: Submit the job through a Dataproc workflow template. A workflow template defines the cluster and the steps so the run is identical. A workflow template defines the cluster and the steps so the same job can be re-run identically. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A workflow template defines the cluster and the steps so the run is identical.
- **B:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: A workflow template defines the cluster and the steps so the run is identical.
- **C:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: A workflow template defines the cluster and the steps so the run is identical.
- **D:** Correct. A workflow template defines the cluster and the steps so the same job can be re-run identically. In this case: A workflow template defines the cluster and the steps so the run is identical.

### Question 74 — C

Answer: Subscribe BigQuery to the Pub/Sub topic. A BigQuery subscription writes each message into the table on arrival. Local study-map skill 3.7 (Event-Driven Ingestion with Pub/Sub), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Why the correct answer wins: A BigQuery subscription writes each message into the table on arrival.
- **B:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: A BigQuery subscription writes each message into the table on arrival.
- **C:** Correct. In this case: A BigQuery subscription writes each message into the table on arrival.
- **D:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A BigQuery subscription writes each message into the table on arrival.

### Question 75 — B

Answer: Start the pipeline from an Eventarc trigger. An Eventarc trigger routes the object event to the Cloud Run target. Local study-map skill 3.8 (Eventarc Triggers), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A BigQuery subscription writes each published message into a table as it arrives. Why the correct answer wins: An Eventarc trigger routes the object event to the Cloud Run target.
- **B:** Correct. In this case: An Eventarc trigger routes the object event to the Cloud Run target.
- **C:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: An Eventarc trigger routes the object event to the Cloud Run target.
- **D:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: An Eventarc trigger routes the object event to the Cloud Run target.

### Question 76 — A

Answer: Assign a predefined role to the group. A predefined role for that job function carries the permissions it needs. A predefined role is maintained by Google and covers one service or one job function. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A predefined role is maintained by Google and covers one service or one job function. In this case: A predefined role for that job function carries the permissions it needs.
- **B:** Incorrect for this question. A custom role narrows the grant when no predefined role matches the job exactly. Why the correct answer wins: A predefined role for that job function carries the permissions it needs.
- **C:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A predefined role for that job function carries the permissions it needs.
- **D:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A predefined role for that job function carries the permissions it needs.

### Question 77 — D, E

Answers: Run the job as a dedicated service account; Add the project to a VPC Service Controls perimeter. A dedicated service account scopes the identity, and the perimeter blocks data movement out. A service account gives the workload its own identity instead of borrowing a person's. A perimeter blocks data movement outside the boundary even for an authorised identity. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A dedicated service account scopes the identity, and the perimeter blocks data movement out.
- **B:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A dedicated service account scopes the identity, and the perimeter blocks data movement out.
- **C:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A dedicated service account scopes the identity, and the perimeter blocks data movement out.
- **D:** Correct. A service account gives the workload its own identity instead of borrowing a person's. In this case: A dedicated service account scopes the identity, and the perimeter blocks data movement out.
- **E:** Correct. A perimeter blocks data movement outside the boundary even for an authorised identity. In this case: A dedicated service account scopes the identity, and the perimeter blocks data movement out.

### Question 78 — A

Answer: Grant the predefined role that matches the task. The narrowest role that reads that view keeps the rest of the project closed. A predefined role carries the permissions for one job and nothing else. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A predefined role carries the permissions for one job and nothing else. In this case: The narrowest role that reads that view keeps the rest of the project closed.
- **B:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: The narrowest role that reads that view keeps the rest of the project closed.
- **C:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: The narrowest role that reads that view keeps the rest of the project closed.
- **D:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: The narrowest role that reads that view keeps the rest of the project closed.

### Question 79 — A

Answer: Create a custom role with only the permissions used. A custom role narrows the grant to the permissions actually in use. A custom role narrows the grant when no predefined role matches the job exactly. Local study-map skill 4.2 (Basic, Predefined, and Custom Roles), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A custom role narrows the grant when no predefined role matches the job exactly. In this case: A custom role narrows the grant to the permissions actually in use.
- **B:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A custom role narrows the grant to the permissions actually in use.
- **C:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A custom role narrows the grant to the permissions actually in use.
- **D:** Incorrect for this question. A predefined role is maintained by Google and covers one service or one job function. Why the correct answer wins: A custom role narrows the grant to the permissions actually in use.

### Question 80 — D

Answer: Assign a predefined role to the group. A predefined reader role covers the job without the breadth of a basic role. A predefined role is maintained by Google and covers one service or one job function. Local study-map skill 4.2 (Basic, Predefined, and Custom Roles), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: A predefined reader role covers the job without the breadth of a basic role.
- **B:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A predefined reader role covers the job without the breadth of a basic role.
- **C:** Incorrect for this question. A custom role narrows the grant when no predefined role matches the job exactly. Why the correct answer wins: A predefined reader role covers the job without the breadth of a basic role.
- **D:** Correct. A predefined role is maintained by Google and covers one service or one job function. In this case: A predefined reader role covers the job without the breadth of a basic role.

### Question 81 — B

Answer: Enable uniform bucket-level access. Uniform bucket-level access removes per-object ACLs from the decision. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. Local study-map skill 4.3 (Cloud Storage Access Control), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Per-object ACLs are hard to audit and are overridden when uniform access is enabled. Why the correct answer wins: Uniform bucket-level access removes per-object ACLs from the decision.
- **B:** Correct. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. In this case: Uniform bucket-level access removes per-object ACLs from the decision.
- **C:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: Uniform bucket-level access removes per-object ACLs from the decision.
- **D:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Uniform bucket-level access removes per-object ACLs from the decision.

### Question 82 — A

Answer: Issue a signed URL with a short expiry. A signed URL grants short-lived access to that object alone. A signed URL grants temporary read access to one object without changing IAM. Local study-map skill 4.3 (Cloud Storage Access Control), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A signed URL grants temporary read access to one object without changing IAM. In this case: A signed URL grants short-lived access to that object alone.
- **B:** Incorrect for this question. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. Why the correct answer wins: A signed URL grants short-lived access to that object alone.
- **C:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A signed URL grants short-lived access to that object alone.
- **D:** Incorrect for this question. An export hands over a copy that the publisher can no longer control or revoke. Why the correct answer wins: A signed URL grants short-lived access to that object alone.

### Question 83 — A

Answer: Publish the dataset through Analytics Hub. Analytics Hub shares the dataset in place under the publisher's policy. Analytics Hub shares a curated dataset with a subscriber who reads it in place. Local study-map skill 4.4 (Analytics Hub Data Sharing), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Analytics Hub shares a curated dataset with a subscriber who reads it in place. In this case: Analytics Hub shares the dataset in place under the publisher's policy.
- **B:** Incorrect for this question. An export hands over a copy that the publisher can no longer control or revoke. Why the correct answer wins: Analytics Hub shares the dataset in place under the publisher's policy.
- **C:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: Analytics Hub shares the dataset in place under the publisher's policy.
- **D:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Analytics Hub shares the dataset in place under the publisher's policy.

### Question 84 — D

Answer: Add the project to a VPC Service Controls perimeter. A perimeter blocks the movement regardless of the identity's permissions. A perimeter blocks data movement outside the boundary even for an authorised identity. Local study-map skill 4.4 (Analytics Hub Data Sharing), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: A perimeter blocks the movement regardless of the identity's permissions.
- **B:** Incorrect for this question. Analytics Hub shares a curated dataset with a subscriber who reads it in place. Why the correct answer wins: A perimeter blocks the movement regardless of the identity's permissions.
- **C:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A perimeter blocks the movement regardless of the identity's permissions.
- **D:** Correct. A perimeter blocks data movement outside the boundary even for an authorised identity. In this case: A perimeter blocks the movement regardless of the identity's permissions.

### Question 85 — A

Answer: Keep the objects in the Standard class. Standard is for objects read frequently, where access cost dominates. Standard is for objects read frequently, where access cost matters more than storage cost. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Standard is for objects read frequently, where access cost matters more than storage cost. In this case: Standard is for objects read frequently, where access cost dominates.
- **B:** Incorrect for this question. Archive is the cheapest class for data kept for compliance and read almost never. Why the correct answer wins: Standard is for objects read frequently, where access cost dominates.
- **C:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes. Why the correct answer wins: Standard is for objects read frequently, where access cost dominates.
- **D:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: Standard is for objects read frequently, where access cost dominates.

### Question 86 — D

Answer: Move the objects to Archive. Archive is the cheapest class for data kept for compliance. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: Archive is the cheapest class for data kept for compliance.
- **B:** Incorrect for this question. Coldline suits reads a few times a year and has a longer minimum storage duration. Why the correct answer wins: Archive is the cheapest class for data kept for compliance.
- **C:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Archive is the cheapest class for data kept for compliance.
- **D:** Correct. In this case: Archive is the cheapest class for data kept for compliance.

### Question 87 — B, E

Answers: Enable Autoclass on the bucket; Add a lifecycle rule that changes the storage class. Autoclass moves each object as its access changes, and a rule demotes objects by age. Autoclass moves each object between classes as its access pattern changes. A setStorageClass rule demotes an object after a number of days so the cost falls without a copy. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keeping every version in the hot class pays the highest rate for data nobody reads. Why the correct answer wins: Autoclass moves each object as its access changes, and a rule demotes objects by age.
- **B:** Correct. Autoclass moves each object between classes as its access pattern changes. In this case: Autoclass moves each object as its access changes, and a rule demotes objects by age.
- **C:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: Autoclass moves each object as its access changes, and a rule demotes objects by age.
- **D:** Incorrect for this question. Coldline suits reads a few times a year and has a longer minimum storage duration. Why the correct answer wins: Autoclass moves each object as its access changes, and a rule demotes objects by age.
- **E:** Correct. A setStorageClass rule demotes an object after a number of days so the cost falls without a copy. In this case: Autoclass moves each object as its access changes, and a rule demotes objects by age.

### Question 88 — B

Answer: Add a lifecycle rule that deletes objects after the retention period. A lifecycle delete rule removes the object once the period passes. A delete rule removes the objects once the retention period passes, without a person remembering. Local study-map skill 4.6 (Lifecycle Rules and Expiration), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: A lifecycle delete rule removes the object once the period passes.
- **B:** Correct. A delete rule removes the objects once the retention period passes, without a person remembering. In this case: A lifecycle delete rule removes the object once the period passes.
- **C:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A lifecycle delete rule removes the object once the period passes.
- **D:** Incorrect for this question. Keeping every version in the hot class pays the highest rate for data nobody reads. Why the correct answer wins: A lifecycle delete rule removes the object once the period passes.

### Question 89 — A

Answer: Set a table expiration on the dataset. Dataset-level expiration removes tables created inside it after the period. Local study-map skill 4.6 (Lifecycle Rules and Expiration), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: Dataset-level expiration removes tables created inside it after the period.
- **B:** Incorrect for this question. Partition expiration drops old partitions while the table keeps the recent ones. Why the correct answer wins: Dataset-level expiration removes tables created inside it after the period.
- **C:** Incorrect for this question. A delete rule removes the objects once the retention period passes, without a person remembering. Why the correct answer wins: Dataset-level expiration removes tables created inside it after the period.
- **D:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: Dataset-level expiration removes tables created inside it after the period.

### Question 90 — C

Answer: Apply a bucket retention policy with a lock. A locked retention policy prevents deletion for the period. Local study-map skill 4.7 (Archiving Services), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: A locked retention policy prevents deletion for the period.
- **B:** Incorrect for this question. A delete rule removes the objects once the retention period passes, without a person remembering. Why the correct answer wins: A locked retention policy prevents deletion for the period.
- **C:** Correct. In this case: A locked retention policy prevents deletion for the period.
- **D:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A locked retention policy prevents deletion for the period.

### Question 91 — D

Answer: Add a lifecycle rule that changes the storage class. A setStorageClass rule demotes the object by age. A setStorageClass rule demotes an object after a number of days so the cost falls without a copy. Local study-map skill 4.7 (Archiving Services), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A delete rule removes the objects once the retention period passes, without a person remembering. Why the correct answer wins: A setStorageClass rule demotes the object by age.
- **B:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: A setStorageClass rule demotes the object by age.
- **C:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes. Why the correct answer wins: A setStorageClass rule demotes the object by age.
- **D:** Correct. A setStorageClass rule demotes an object after a number of days so the cost falls without a copy. In this case: A setStorageClass rule demotes the object by age.

### Question 92 — C

Answer: Restore into a scratch project on a schedule. A restore drill proves the backup can actually be used. A restore drill is the only evidence that the backup can actually be used. Local study-map skill 4.8 (Backup and Recovery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: A restore drill proves the backup can actually be used.
- **B:** Incorrect for this question. A zonal instance is lost with its zone and gives no automatic failover. Why the correct answer wins: A restore drill proves the backup can actually be used.
- **C:** Correct. A restore drill is the only evidence that the backup can actually be used. In this case: A restore drill proves the backup can actually be used.
- **D:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A restore drill proves the backup can actually be used.

### Question 93 — A, E

Answers: Create a Cloud SQL read replica in another region; Enable automated backups and point-in-time recovery on Cloud SQL. A replica can be promoted for the failure, and point-in-time recovery reverses the migration. A read replica serves reads from a second region and can be promoted during a regional failure. Automated backups with point-in-time recovery restore the instance to a chosen moment. Local study-map skill 4.8 (Backup and Recovery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Automated backups with point-in-time recovery restore the instance to a chosen moment. In this case: A replica can be promoted for the failure, and point-in-time recovery reverses the migration.
- **B:** Incorrect for this question. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. Why the correct answer wins: A replica can be promoted for the failure, and point-in-time recovery reverses the migration.
- **C:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: A replica can be promoted for the failure, and point-in-time recovery reverses the migration.
- **D:** Incorrect for this question. A zonal instance is lost with its zone and gives no automatic failover. Why the correct answer wins: A replica can be promoted for the failure, and point-in-time recovery reverses the migration.
- **E:** Correct. A read replica serves reads from a second region and can be promoted during a regional failure. In this case: A replica can be promoted for the failure, and point-in-time recovery reverses the migration.

### Question 94 — B

Answer: Create a dual-region bucket with a replication policy. A dual-region bucket states the pair and reports the lag. A dual-region bucket keeps a copy in a second region and reports the replication lag. Local study-map skill 4.9 (Replication), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: A dual-region bucket states the pair and reports the lag.
- **B:** Correct. A dual-region bucket keeps a copy in a second region and reports the replication lag. In this case: A dual-region bucket states the pair and reports the lag.
- **C:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A dual-region bucket states the pair and reports the lag.
- **D:** Incorrect for this question. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. Why the correct answer wins: A dual-region bucket states the pair and reports the lag.

### Question 95 — C

Answer: Enable object versioning on the bucket. Object versioning keeps the prior generation of the object. Local study-map skill 4.9 (Replication), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: Object versioning keeps the prior generation of the object.
- **B:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: Object versioning keeps the prior generation of the object.
- **C:** Correct. In this case: Object versioning keeps the prior generation of the object.
- **D:** Incorrect for this question. A locked retention policy prevents deletion for the period, even by an administrator. Why the correct answer wins: Object versioning keeps the prior generation of the object.

### Question 96 — D

Answer: Choose a dual-region location. A dual-region location names the primary and the secondary. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Local study-map skill 4.10 (Primary and Secondary Locations), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: A dual-region location names the primary and the secondary.
- **B:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: A dual-region location names the primary and the secondary.
- **C:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: A dual-region location names the primary and the secondary.
- **D:** Correct. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. In this case: A dual-region location names the primary and the secondary.

### Question 97 — A, B

Answers: Encrypt with a customer-managed key from Cloud KMS; Set a rotation schedule on the key. A customer-managed key can be revoked by the customer, and a rotation schedule limits each version. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. A rotation schedule limits how long one key version protects new data. Local study-map skill 4.11 (CMEK, CSEK, and GMEK), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A rotation schedule limits how long one key version protects new data. In this case: A customer-managed key can be revoked by the customer, and a rotation schedule limits each version.
- **B:** Correct. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. In this case: A customer-managed key can be revoked by the customer, and a rotation schedule limits each version.
- **C:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: A customer-managed key can be revoked by the customer, and a rotation schedule limits each version.
- **D:** Incorrect for this question. A customer-supplied key never reaches Google, and losing it loses the object. Why the correct answer wins: A customer-managed key can be revoked by the customer, and a rotation schedule limits each version.
- **E:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: A customer-managed key can be revoked by the customer, and a rotation schedule limits each version.

### Question 98 — C

Answer: Supply a customer-supplied key with each request. A customer-supplied key stays with the client and never reaches Google. A customer-supplied key never reaches Google, and losing it loses the object. Local study-map skill 4.11 (CMEK, CSEK, and GMEK), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. Why the correct answer wins: A customer-supplied key stays with the client and never reaches Google.
- **B:** Incorrect for this question. A key ring in the same region keeps the key and the ciphertext under the same residency rule. Why the correct answer wins: A customer-supplied key stays with the client and never reaches Google.
- **C:** Correct. A customer-supplied key never reaches Google, and losing it loses the object. In this case: A customer-supplied key stays with the client and never reaches Google.
- **D:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: A customer-supplied key stays with the client and never reaches Google.

### Question 99 — D

Answer: Create the key in a Cloud KMS key ring in the data region. A key ring in the data region keeps the key under the same residency rule. Local study-map skill 4.12 (Cloud KMS), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: A key ring in the data region keeps the key under the same residency rule.
- **B:** Incorrect for this question. A rotation schedule limits how long one key version protects new data. Why the correct answer wins: A key ring in the data region keeps the key under the same residency rule.
- **C:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: A key ring in the data region keeps the key under the same residency rule.
- **D:** Correct. In this case: A key ring in the data region keeps the key under the same residency rule.

### Question 100 — C

Answer: Confirm the data is encrypted at rest by the storage service. Encryption at rest protects the stored bytes on the medium. Local study-map skill 4.13 (Encryption in Transit and at Rest), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: Encryption at rest protects the stored bytes on the medium.
- **B:** Incorrect for this question. Encryption in transit protects the bytes while they are on the wire between client and service. Why the correct answer wins: Encryption at rest protects the stored bytes on the medium.
- **C:** Correct. In this case: Encryption at rest protects the stored bytes on the medium.
- **D:** Incorrect for this question. A key stored beside the data protects nothing against anyone who can read the store. Why the correct answer wins: Encryption at rest protects the stored bytes on the medium.
