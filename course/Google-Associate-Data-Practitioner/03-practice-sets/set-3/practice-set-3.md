# Google Cloud Associate Data Practitioner — Full-Length Mock Exam 3

Associate Data Practitioner · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Data Preparation and Ingestion (Ingestion, Reporting, Pipelines, and Access)

### 1. A marketplace wants every raw order event kept so aggregates can be rebuilt at will. Which approach fits?

- A. Combine the extracts in a spreadsheet and upload the result
- B. Extract, transform outside the warehouse, then load the result
- C. Query the source system in place with a federated query
- D. Load the raw rows, then transform them inside the warehouse

### 2. Card numbers must be masked before any warehouse write happens. Which approach is required?

- A. Land the extract in a staging table before any transform runs
- B. Transform on the source system before the export starts
- C. Load the raw rows, then transform them inside the warehouse
- D. Extract, transform outside the warehouse, then load the result

### 3. One feed needs the untouched rows preserved and another needs a scrub before the warehouse step. Which two designs apply? Select two.

- A. Query the source system in place with a federated query
- B. Combine the extracts in a spreadsheet and upload the result
- C. Extract, transform outside the warehouse, then load the result
- D. Load the raw rows, then transform them inside the warehouse
- E. Load into a staging area, apply a light transform, then transform again in the warehouse

### 4. A supplier's price list sits in Cloud SQL and is needed once for a negotiation. What should be used?

- A. Land the extract in a staging table before any transform runs
- B. Order a Transfer Appliance
- C. Build the pipeline in Dataflow
- D. Query the source system in place with a federated query

### 5. Ten years of call detail records need custom Scala logic that SQL cannot express. What should be used?

- A. Clean the stream with a Dataflow pipeline
- B. Define data quality rules and run a quality scan
- C. Clean the data with Spark on Dataproc
- D. Clean the rows with SQL in BigQuery

### 6. The email column must fail the load the moment it stops matching the pattern. What should be added?

- A. Load first and fix the rejected rows afterwards
- B. Define data quality rules and run a quality scan
- C. Profile the columns to measure the null rate before loading
- D. Select every column to be safe

### 7. Before publication the team must quantify what is missing and prove nothing was dropped. Which two actions apply? Select two.

- A. Land the data as CSV
- B. Select every column to be safe
- C. Compare the row count with the source after every load
- D. Profile the columns to measure the null rate before loading
- E. Load first and fix the rejected rows afterwards

### 8. A sender claims the delivered file is identical to theirs and the team must prove it. What should be compared?

- A. Compare the source checksum with the delivered file
- B. Select every column to be safe
- C. Load first and fix the rejected rows afterwards
- D. Deduplicate on the business key in the cleaning step

### 9. Half a petabyte of tape archives must be online in two weeks. What should be used?

- A. Order a Transfer Appliance
- B. Use BigQuery Data Transfer Service
- C. Replicate the changes with Datastream
- D. Use Storage Transfer Service

### 10. A channel analytics feed must be pulled into a warehouse table every night. What should be used?

- A. Use Storage Transfer Service
- B. Order a Transfer Appliance
- C. Replicate the changes with Datastream
- D. Use BigQuery Data Transfer Service

### 11. An engineer must move one folder between two buckets during an incident. What should be used?

- A. Pull the files from the partner over FTP each night
- B. Copy the objects with the gcloud storage command
- C. Order a Transfer Appliance
- D. Load the files with the bq load command

### 12. A legacy host holds both a database and a shared filesystem that must both move. Which two tools apply? Select two.

- A. Use Database Migration Service
- B. Use Storage Transfer Service
- C. Order a Transfer Appliance
- D. Document the steps and have an analyst run them each morning
- E. Pull the files from the partner over FTP each night

### 13. A streaming topic must carry its field definitions with every record. Which format fits?

- A. Land the data as Avro
- B. Land the data as CSV
- C. Land the data as XML
- D. Land the data as Parquet

### 14. A feature table is read column by column by a training job. Which format fits?

- A. Land the data as XML
- B. Land the data as newline-delimited JSON
- C. Land the data as CSV
- D. Land the data as Parquet

### 15. An API response contains nested arrays that must land exactly as returned. Which format fits?

- A. Land the data as Avro
- B. Land the data as CSV
- C. Land the data as newline-delimited JSON
- D. Convert the data to ORC before the load

### 16. Two landing formats carry no type information at all. Which two apply? Select two.

- A. Land the data as XML
- B. Land the data as Avro
- C. Land the data as Parquet
- D. Land the data as newline-delimited JSON
- E. Land the data as CSV

### 17. Files must be transformed as they are produced rather than after they accumulate. What should be used?

- A. Build the pipeline in Dataflow
- B. Load the rows with a client library from the application
- C. Load the files with the bq load command
- D. Run the handler as a Cloud Functions function

### 18. Only the rows that changed in a MySQL source are wanted, continuously. What should be used?

- A. Order a Transfer Appliance
- B. Replicate the changes with Datastream
- C. Use Database Migration Service
- D. Copy the objects with the gcloud storage command

### 19. A marketing suite's API must be extracted and mapped without hand-written code. What should be used?

- A. Run the transformation as Spark on Dataproc
- B. Run a cron job on a Compute Engine instance
- C. Build the pipeline in Cloud Data Fusion
- D. Document the steps and have an analyst run them each morning

### 20. A recommendation service needs single-digit millisecond lookups by user identifier at high volume. Which store fits?

- A. Store the rows in Bigtable
- B. Store the rows in BigQuery
- C. Store the records in Cloud SQL
- D. Store the documents in Firestore

### 21. Raw video files must sit cheaply until a transcoder picks them up. Which store fits?

- A. Store the records in Spanner
- B. Store the rows in BigQuery
- C. Store the files in Cloud Storage
- D. Store the records in Cloud SQL

### 22. A ticketing system must transact globally with no single regional primary. Which store fits?

- A. Store the rows in Bigtable
- B. Store the records in AlloyDB for PostgreSQL
- C. Store the records in Cloud SQL
- D. Store the records in Spanner

### 23. Clickstream analytics needs columnar scans, and the checkout service needs transactions. Which two stores apply? Select two.

- A. Store the documents in Firestore
- B. Store the rows in Bigtable
- C. Store the records in Cloud SQL
- D. Store the rows in BigQuery
- E. Keep the dataset on the analyst workstation

### 24. A public dataset is queried from three continents around the clock. Which location type fits?

- A. Choose a regional location
- B. Choose a dual-region location
- C. Choose a zonal resource
- D. Choose a multi-region location

### 25. A bank operates in one country and the storage bill is under review. Which location type fits?

- A. Choose a multi-region location
- B. Choose a regional location
- C. Place the data in the region nearest the largest user base
- D. Choose a dual-region location

### 26. The continuity plan names two specific cities for the primary and the secondary. Which location type fits?

- A. Choose a zonal resource
- B. Choose a regional location
- C. Choose a dual-region location
- D. Choose a multi-region location

### 27. A bucket holds scanned contracts and no field model has been declared. How should the files be classified?

- A. Apply a schema on read at query time
- B. Treat the records as semi-structured data
- C. Treat the files as unstructured data
- D. Treat the records as structured data

### 28. Records arrive as Avro with optional fields that differ between producers. How should they be classified?

- A. Treat the records as semi-structured data
- B. Treat the records as structured data
- C. Treat the files as unstructured data
- D. Apply a schema on read at query time

### 29. A telemetry service must commit events at the lowest possible latency. What should be used?

- A. Load the files with the bq load command
- B. Copy the objects with the gcloud storage command
- C. Stream the rows with the BigQuery Storage Write API
- D. Load the rows with a client library from the application

### 30. Parquet objects sitting in a bucket must be appended to an existing table. What should be used?

- A. Load the files with the bq load command
- B. Load the rows with a client library from the application
- C. Copy the objects with the gcloud storage command
- D. Use Storage Transfer Service

---

## Domain 2 — Data Analysis and Presentation (Files, Formats, Dashboards, and Governance)

### 31. A curated subset must be readable by analysts without copying any rows. What should be used?

- A. Create a BigQuery materialized view
- B. Load the files into a native table
- C. Query the files through an external table
- D. Create a BigQuery view over the join

### 32. Weekly active installs must be reproducible from the warehouse each time. What should be used?

- A. Export the query result to a spreadsheet for the business team
- B. Share the dashboard with a scheduled delivery
- C. Turn off the result cache to force a fresh read
- D. Write a SQL query in BigQuery and save the result

### 33. A report is slow because it reads external files and scans every partition. Which two changes help? Select two.

- A. Filter the query on the partition column
- B. Turn off the result cache to force a fresh read
- C. Load the files into a native table
- D. Select every column to be safe
- E. Query the files through an external table

### 34. The same five-table aggregation is recomputed every ten minutes. What should be used?

- A. Create a BigQuery view over the join
- B. Create a BigQuery materialized view
- C. Write a SQL query in BigQuery and save the result
- D. Query the files through an external table

### 35. A team needs a shared notebook runtime with project IAM and warehouse access. What should be used?

- A. Load the extract into a notebook and work in pandas
- B. Analyse the data in a Colab Enterprise notebook
- C. Keep the dataset on the analyst workstation
- D. Upload a CSV extract into the notebook and analyse it there

### 36. A notebook must query the warehouse without the analyst managing credentials. What should be used?

- A. Query BigQuery from the notebook with the %%bigquery magic
- B. Load the extract into a notebook and work in pandas
- C. Upload a CSV extract into the notebook and analyse it there
- D. Export the query result to a spreadsheet for the business team

### 37. A product owner asks which SKUs drove last month's return spike. What should be produced?

- A. Build a Looker Studio report
- B. Write a SQL query in BigQuery and save the result
- C. Share the dashboard with a scheduled delivery
- D. Turn off the result cache to force a fresh read

### 38. The answer must be explorable by the merchandising team every morning. What should be used?

- A. Build a governed Looker dashboard
- B. Upload a CSV extract into the notebook and analyse it there
- C. Document the steps and have an analyst run them each morning
- D. Export the query result to a spreadsheet for the business team

### 39. A governed dashboard must also reach people who never sign in. Which two components apply? Select two.

- A. Document the steps and have an analyst run them each morning
- B. Share the dashboard with a scheduled delivery
- C. Build a governed Looker dashboard
- D. Turn off the result cache to force a fresh read
- E. Build a Looker Studio report

### 40. No single tile may be allowed to redefine the revenue metric. What should be used?

- A. Export the query result to a spreadsheet for the business team
- B. Build a Looker Studio report
- C. Build a governed Looker dashboard
- D. Select every column to be safe

### 41. A board pack must combine a spreadsheet and one table before tomorrow's meeting. What should be used?

- A. Orchestrate the steps in Cloud Composer
- B. Build a Looker Studio report
- C. Expose the table through a LookML explore
- D. Build a governed Looker dashboard

### 42. A startup needs a quick report over three sheets with no modelling layer. What should be used?

- A. Build a governed Looker dashboard
- B. Add a LookML measure for the calculation
- C. Build a Looker Studio report
- D. Change the LookML parameter in the view

### 43. Definitions must be reusable and certified across sixty reports. What should be used?

- A. Issue a signed URL with a short expiry
- B. Build a governed Looker dashboard
- C. Export the query result to a spreadsheet for the business team
- D. Build a Looker Studio report

### 44. A margin ratio must be computed identically in ten reports. What should be added?

- A. Select every column to be safe
- B. Turn off the result cache to force a fresh read
- C. Expose the table through a LookML explore
- D. Add a LookML measure for the calculation

### 45. The fiscal year start and the margin definition must both change for every consumer. Which two changes belong in the model? Select two.

- A. Turn off the result cache to force a fresh read
- B. Change the LookML parameter in the view
- C. Add a LookML measure for the calculation
- D. Export the query result to a spreadsheet for the business team
- E. Share the dashboard with a scheduled delivery

### 46. A join must be offered only for one business question and hidden elsewhere. What should be added?

- A. Change the LookML parameter in the view
- B. Expose the table through a LookML explore
- C. Add a LookML measure for the calculation
- D. Create a BigQuery view over the join

### 47. No label exists but the team wants products grouped by behaviour. What should be built?

- A. Train a BigQuery ML linear regression model
- B. Score the rows with ML.PREDICT
- C. Train a BigQuery ML k-means model
- D. Train a BigQuery ML logistic regression model

### 48. Monthly energy demand has strong seasonality and few covariates. What should be built?

- A. Train a BigQuery ML boosted tree model
- B. Train a BigQuery ML ARIMA_PLUS model
- C. Train a BigQuery ML k-means model
- D. Train a BigQuery ML linear regression model

### 49. A default flag and a claim amount must both be predicted without leaving SQL. Which two model types apply? Select two.

- A. Generate the forecast with ML.FORECAST
- B. Train an AutoML tabular model
- C. Train a BigQuery ML linear regression model
- D. Train a BigQuery ML logistic regression model
- E. Train a BigQuery ML k-means model

### 50. Contract clauses must be summarised per row while the text stays in the warehouse. What should be used?

- A. Land the data as newline-delimited JSON
- B. Create a BigQuery remote model over a Gemini model
- C. Fine-tune a Gemini model from the warehouse rows
- D. Load the extract into a notebook and work in pandas

### 51. A remote model returns permission denied when it calls the endpoint. What should be fixed?

- A. Create the BigQuery connection that reaches the model endpoint
- B. Issue a signed URL with a short expiry
- C. Stream the rows with the BigQuery Storage Write API
- D. Load the files with the bq load command

### 52. The team wants to start training before anyone defines success. What should be done first?

- A. Run a cron job on a Compute Engine instance
- B. Plan collection, training, evaluation, then prediction
- C. Ship the model once the training loss looks good
- D. Document the steps and have an analyst run them each morning

### 53. A demand model must be judged on the quarter that follows its training window. How should the split be built?

- A. Hold out whole entities so none spans both splits
- B. Hold the most recent period out as the test set
- C. Hold out a labelled split before training
- D. Ship the model once the training loss looks good

### 54. The holdout metrics must be produced by a SQL statement for the pack. What should be used?

- A. Score the rows with ML.PREDICT
- B. Evaluate the model with ML.EVALUATE
- C. Generate the forecast with ML.FORECAST
- D. Explain the prediction with ML.EXPLAIN_PREDICT

### 55. A wide table has non-linear interactions and plenty of labelled rows. Which model type fits?

- A. Train a BigQuery ML linear regression model
- B. Train a BigQuery ML boosted tree model
- C. Train a BigQuery ML ARIMA_PLUS model
- D. Train a BigQuery ML k-means model

### 56. Tomorrow's applicants must be scored in a batch. What should be used?

- A. Evaluate the model with ML.EVALUATE
- B. Generate the forecast with ML.FORECAST
- C. Explain the prediction with ML.EXPLAIN_PREDICT
- D. Score the rows with ML.PREDICT

### 57. An audit asks which artifact served traffic in March. What should have been used?

- A. Copy the objects with the gcloud storage command
- B. Keep the dataset on the analyst workstation
- C. Register the model version in Model Registry
- D. Export the query result to a spreadsheet for the business team

---

## Domain 3 — Data Pipeline Orchestration (Streaming, Scheduling, Modelling, and Recovery)

### 58. Dependent SQL models must be rebuilt in the right order after a change. What should be used?

- A. Run a cron job on a Compute Engine instance
- B. Manage the SQL transformations in Dataform
- C. Run the transformation as Spark on Dataproc
- D. Build the pipeline in Cloud Data Fusion

### 59. A Python pipeline must window a stream into five-minute aggregates. What should be used?

- A. Build the pipeline in Dataflow
- B. Run the handler as a Cloud Functions function
- C. Run the transformation as Spark on Dataproc
- D. Sequence the API calls with Workflows

### 60. Ten sources must be joined on a canvas by analysts who do not write code. What should be used?

- A. Run the transformation as Spark on Dataproc
- B. Run a cron job on a Compute Engine instance
- C. Document the steps and have an analyst run them each morning
- D. Build the pipeline in Cloud Data Fusion

### 61. A Spark job must run, and a graph must wait for a partner file before it starts. Which two tools apply? Select two.

- A. Run a cron job on a Compute Engine instance
- B. Run the transformation as Spark on Dataproc
- C. Run the handler as a Cloud Functions function
- D. Orchestrate the steps in Cloud Composer
- E. Document the steps and have an analyst run them each morning

### 62. The warehouse engine should carry the heavy join rather than the source system. Which design fits?

- A. Extract, transform outside the warehouse, then load the result
- B. Query the source system in place with a federated query
- C. Transform on the source system before the export starts
- D. Load the raw rows, then transform them inside the warehouse

### 63. The destination refuses any record that has not already been cleansed. Which design fits?

- A. Extract, transform outside the warehouse, then load the result
- B. Stream the rows with the BigQuery Storage Write API
- C. Land the extract in a staging table before any transform runs
- D. Load the raw rows, then transform them inside the warehouse

### 64. An hourly rollup must be written to a table without an operator. What should be used?

- A. Trigger the job from Cloud Scheduler
- B. Schedule the SQL with a BigQuery scheduled query
- C. Sequence the API calls with Workflows
- D. Submit the job through a Dataproc workflow template

### 65. A Cloud Run endpoint must be called at 06:00 every weekday. What should be used?

- A. Orchestrate the steps in Cloud Composer
- B. Sequence the API calls with Workflows
- C. Schedule the SQL with a BigQuery scheduled query
- D. Trigger the job from Cloud Scheduler

### 66. One statement must run nightly and a separate endpoint must be called hourly. Which two components apply? Select two.

- A. Schedule the SQL with a BigQuery scheduled query
- B. Document the steps and have an analyst run them each morning
- C. Trigger the job from Cloud Scheduler
- D. Sequence the API calls with Workflows
- E. Run a cron job on a Compute Engine instance

### 67. Per-step throughput must be compared during a traffic spike. Where should the team look?

- A. Turn off the result cache to force a fresh read
- B. Query the job logs in Logs Explorer
- C. Watch the job graph and per-step throughput in the Dataflow console
- D. Write a SQL query in BigQuery and save the result

### 68. Malformed events must be recoverable after the fact rather than lost. What should be added?

- A. Select every column to be safe
- B. Load first and fix the rejected rows afterwards
- C. Write the rejected rows to a dead-letter table
- D. Denormalise the tables into one wide table

### 69. One request identifier must be traced through the pipeline logs. Where should the team look?

- A. Share the dashboard with a scheduled delivery
- B. Write a SQL query in BigQuery and save the result
- C. Query the job logs in Logs Explorer
- D. Document the steps and have an analyst run them each morning

### 70. A latency objective on the pipeline must notify an owner when it is breached. What should be added?

- A. Query the job logs in Logs Explorer
- B. Document the steps and have an analyst run them each morning
- C. Create a Cloud Monitoring alert policy on the job metric
- D. Turn off the result cache to force a fresh read

### 71. A weekly graph has four dependencies and an SLA to meet. What should orchestrate it?

- A. Sequence the API calls with Workflows
- B. Run the handler as a Cloud Functions function
- C. Run a cron job on a Compute Engine instance
- D. Orchestrate the steps in Cloud Composer

### 72. Provisioning steps across two APIs must run in sequence without a server. What should be used?

- A. Orchestrate the steps in Cloud Composer
- B. Run the handler as a Cloud Functions function
- C. Start the pipeline from an Eventarc trigger
- D. Sequence the API calls with Workflows

### 73. The SQL should be scheduled by the warehouse and the cross-system waits handled by a graph. Which two components apply? Select two.

- A. Run a cron job on a Compute Engine instance
- B. Document the steps and have an analyst run them each morning
- C. Orchestrate the steps in Cloud Composer
- D. Turn off the result cache to force a fresh read
- E. Schedule the SQL with a BigQuery scheduled query

### 74. Messages must be written into a table with no subscriber process to operate. What should be used?

- A. Start the pipeline from an Eventarc trigger
- B. Subscribe BigQuery to the Pub/Sub topic
- C. Load the files with the bq load command
- D. Schedule the SQL with a BigQuery scheduled query

### 75. A Dataform run must start when a control file lands in a bucket. What should be used?

- A. Start the pipeline from an Eventarc trigger
- B. Schedule the SQL with a BigQuery scheduled query
- C. Trigger the job from Cloud Scheduler
- D. Subscribe BigQuery to the Pub/Sub topic

---

## Domain 4 — Data Management (Warehouse Analytics, Orchestration, and Key Management)

### 76. A dashboard service only ever reads two views. What should be granted?

- A. Grant the basic Owner role to the team
- B. Grant the predefined role that matches the task
- C. Grant the role to the whole domain
- D. Make the bucket public so the partner can read it

### 77. A Cloud Run job must query the warehouse under its own identity. What should be used?

- A. Issue a signed URL with a short expiry
- B. Grant the basic Owner role to the team
- C. Grant the role to the whole domain
- D. Run the job as a dedicated service account

### 78. Two grants must be both narrow and time-boxed. Which two apply? Select two.

- A. Grant the basic Owner role to the team
- B. Make the bucket public so the partner can read it
- C. Issue a signed URL with a short expiry
- D. Grant the role to the whole domain
- E. Grant the predefined role that matches the task

### 79. The warehouse reader job function is covered by a managed role. What should be granted?

- A. Grant the basic Owner role to the team
- B. Create a custom role with only the permissions used
- C. Make the bucket public so the partner can read it
- D. Assign a predefined role to the group

### 80. The auditor wants one permission removed from a team while everything else stays. What should be created?

- A. Grant the role to the whole domain
- B. Assign a predefined role to the group
- C. Create a custom role with only the permissions used
- D. Grant the basic Owner role to the team

### 81. Access must be reviewable in one place rather than per object. What should be enabled?

- A. Enable uniform bucket-level access
- B. Make the bucket public so the partner can read it
- C. Manage per-object ACLs on the bucket
- D. Issue a signed URL with a short expiry

### 82. Uniform access is off, and one object needs an exception for a single principal. What should be used?

- A. Enable uniform bucket-level access
- B. Manage per-object ACLs on the bucket
- C. Export the table to a bucket the partner owns
- D. Make the bucket public so the partner can read it

### 83. A partner wants the curated dataset as a subscription that stays current. What should be used?

- A. Publish the dataset through Analytics Hub
- B. Make the bucket public so the partner can read it
- C. Issue a signed URL with a short expiry
- D. Export the table to a bucket the partner owns

### 84. A regulator requires the partner to hold a copy inside their own project. What should be done?

- A. Export the table to a bucket the partner owns
- B. Issue a signed URL with a short expiry
- C. Add the project to a VPC Service Controls perimeter
- D. Publish the dataset through Analytics Hub

### 85. Backup objects are read about twice a month. Which class fits?

- A. Keep the objects in the Standard class
- B. Move the objects to Coldline
- C. Move the objects to Archive
- D. Move the objects to Nearline

### 86. Audit records are retrieved once a quarter. Which class fits?

- A. Move the objects to Nearline
- B. Keep the objects in the Standard class
- C. Move the objects to Coldline
- D. Move the objects to Archive

### 87. One bucket holds hot thumbnails and cold archives, and the team wants a single bucket. Which two options apply? Select two.

- A. Move the objects to Archive
- B. Enable Autoclass on the bucket
- C. Keep every version in the Standard class forever
- D. Leave the objects in place and review them next year
- E. Keep the objects in the Standard class

### 88. Temporary exports must be removed seven days after they are written. What should be added?

- A. Add a lifecycle rule that deletes objects after the retention period
- B. Keep every version in the Standard class forever
- C. Enable object versioning on the bucket
- D. Leave the objects in place and review them next year

### 89. Raw event partitions must roll off after four hundred days while the table remains. What should be set?

- A. Set a table expiration on the dataset
- B. Add a lifecycle rule that deletes objects after the retention period
- C. Set a partition expiration on the table
- D. Leave the objects in place and review them next year

### 90. Closed case files must be kept at the lowest storage cost for a decade. Which class fits?

- A. Move the objects to Coldline
- B. Keep the objects in the Standard class
- C. Move the objects to Nearline
- D. Move the objects to Archive

### 91. Deletion must be blocked for the statutory period even for an administrator. What should be applied?

- A. Leave the objects in place and review them next year
- B. Add a lifecycle rule that deletes objects after the retention period
- C. Apply a bucket retention policy with a lock
- D. Enable object versioning on the bucket

### 92. A mistaken DELETE removed three hundred rows an hour ago. What should be used?

- A. Enable automated backups and point-in-time recovery on Cloud SQL
- B. Rely on the disk snapshot the platform keeps
- C. Copy the bucket to a second region with a scheduled transfer
- D. Deploy a single zonal instance to keep the cost down

### 93. The recovery plan must be tested, and a regional loss must not stop reads. Which two measures apply? Select two.

- A. Copy the bucket to a second region with a scheduled transfer
- B. Restore into a scratch project on a schedule
- C. Deploy a single zonal instance to keep the cost down
- D. Create a Cloud SQL read replica in another region
- E. Rely on the disk snapshot the platform keeps

### 94. A second copy must be rebuilt nightly and a gap between runs is acceptable. What should be used?

- A. Copy the bucket to a second region with a scheduled transfer
- B. Create a dual-region bucket with a replication policy
- C. Enable object versioning on the bucket
- D. Create a Cloud SQL read replica in another region

### 95. Reads must continue through a regional outage with no copy job to run. What should be used?

- A. Copy the bucket to a second region with a scheduled transfer
- B. Create a dual-region bucket with a replication policy
- C. Create a multi-region bucket
- D. Enable object versioning on the bucket

### 96. The standby must never share a failure domain with the primary. What should be deployed?

- A. Copy the bucket to a second region with a scheduled transfer
- B. Deploy a single zonal instance to keep the cost down
- C. Deploy the instance as regional with a standby
- D. Choose a regional location

### 97. One dataset needs no key operations at all, and another must be revocable by the customer. Which two key models apply? Select two.

- A. Use the Google-managed default encryption
- B. Encrypt with a customer-managed key from Cloud KMS
- C. Supply a customer-supplied key with each request
- D. Put the key in the application configuration file
- E. Encrypt in the client and store the key next to the data

### 98. The key must be supplied on each request and never stored anywhere. Which key model applies?

- A. Supply a customer-supplied key with each request
- B. Create the key in a Cloud KMS key ring in the data region
- C. Encrypt with a customer-managed key from Cloud KMS
- D. Use the Google-managed default encryption

### 99. The key must be rendered permanently unusable so the ciphertext can never be read again. What should be done?

- A. Put the key in the application configuration file
- B. Use the Google-managed default encryption
- C. Set a rotation schedule on the key
- D. Destroy the key version to stop access immediately

### 100. The connection between the client and the API must be encrypted. What should be confirmed?

- A. Enforce TLS for every connection to the service
- B. Encrypt in the client and store the key next to the data
- C. Confirm the data is encrypted at rest by the storage service
- D. Put the key in the application configuration file

---

## Answer key and explanations

### Question 1 — D

Answer: Load the raw rows, then transform them inside the warehouse. ELT retains the raw events and reshapes them inside the warehouse on demand. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run. Why the correct answer wins: ELT retains the raw events and reshapes them inside the warehouse on demand.
- **B:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT retains the raw events and reshapes them inside the warehouse on demand.
- **C:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ELT retains the raw events and reshapes them inside the warehouse on demand.
- **D:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT retains the raw events and reshapes them inside the warehouse on demand.

### Question 2 — D

Answer: Extract, transform outside the warehouse, then load the result. ETL masks the record outside the warehouse, so the raw value never lands there. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A staging table separates a failed load from a failed transform, so each can be retried on its own. Why the correct answer wins: ETL masks the record outside the warehouse, so the raw value never lands there.
- **B:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ETL masks the record outside the warehouse, so the raw value never lands there.
- **C:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETL masks the record outside the warehouse, so the raw value never lands there.
- **D:** Correct. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. In this case: ETL masks the record outside the warehouse, so the raw value never lands there.

### Question 3 — D, E

Answers: Load the raw rows, then transform them inside the warehouse; Load into a staging area, apply a light transform, then transform again in the warehouse. ELT keeps the raw copy, and ETLT adds the pre-warehouse cleanup. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ELT keeps the raw copy, and ETLT adds the pre-warehouse cleanup.
- **B:** Incorrect for this question. A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run. Why the correct answer wins: ELT keeps the raw copy, and ETLT adds the pre-warehouse cleanup.
- **C:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT keeps the raw copy, and ETLT adds the pre-warehouse cleanup.
- **D:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT keeps the raw copy, and ETLT adds the pre-warehouse cleanup.
- **E:** Correct. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. In this case: ELT keeps the raw copy, and ETLT adds the pre-warehouse cleanup.

### Question 4 — D

Answer: Query the source system in place with a federated query. A federated query reads the remote table for that one comparison. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A staging table separates a failed load from a failed transform, so each can be retried on its own. Why the correct answer wins: A federated query reads the remote table for that one comparison.
- **B:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: A federated query reads the remote table for that one comparison.
- **C:** Incorrect for this question. Dataflow runs the same code for streaming and batch and scales the workers with the load. Why the correct answer wins: A federated query reads the remote table for that one comparison.
- **D:** Correct. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. In this case: A federated query reads the remote table for that one comparison.

### Question 5 — C

Answer: Clean the data with Spark on Dataproc. Spark on Dataproc runs the custom code over the large record set. Spark suits large files that need custom code rather than SQL. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Dataflow pipeline applies the same cleaning logic to streaming and batch records. Why the correct answer wins: Spark on Dataproc runs the custom code over the large record set.
- **B:** Incorrect for this question. Declared rules turn a judgement about the data into a test that runs on every load. Why the correct answer wins: Spark on Dataproc runs the custom code over the large record set.
- **C:** Correct. Spark suits large files that need custom code rather than SQL. In this case: Spark on Dataproc runs the custom code over the large record set.
- **D:** Incorrect for this question. SQL inside the warehouse removes duplicates, trims values, and casts types where the data already sits. Why the correct answer wins: Spark on Dataproc runs the custom code over the large record set.

### Question 6 — B

Answer: Define data quality rules and run a quality scan. A declared rule turns the expectation into a test on every load. Declared rules turn a judgement about the data into a test that runs on every load. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A declared rule turns the expectation into a test on every load.
- **B:** Correct. Declared rules turn a judgement about the data into a test that runs on every load. In this case: A declared rule turns the expectation into a test on every load.
- **C:** Incorrect for this question. A profile quantifies what is missing before the gaps reach a dashboard. Why the correct answer wins: A declared rule turns the expectation into a test on every load.
- **D:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A declared rule turns the expectation into a test on every load.

### Question 7 — C, D

Answers: Profile the columns to measure the null rate before loading; Compare the row count with the source after every load. A null profile measures the gaps, and a row-count check catches a truncated extract. A profile quantifies what is missing before the gaps reach a dashboard. A row-count reconciliation catches a truncated or duplicated extract. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: A null profile measures the gaps, and a row-count check catches a truncated extract.
- **B:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A null profile measures the gaps, and a row-count check catches a truncated extract.
- **C:** Correct. A row-count reconciliation catches a truncated or duplicated extract. In this case: A null profile measures the gaps, and a row-count check catches a truncated extract.
- **D:** Correct. A profile quantifies what is missing before the gaps reach a dashboard. In this case: A null profile measures the gaps, and a row-count check catches a truncated extract.
- **E:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A null profile measures the gaps, and a row-count check catches a truncated extract.

### Question 8 — A

Answer: Compare the source checksum with the delivered file. A checksum proves the bytes arrived unchanged. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A checksum proves the bytes arrived unchanged.
- **B:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A checksum proves the bytes arrived unchanged.
- **C:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A checksum proves the bytes arrived unchanged.
- **D:** Incorrect for this question. Retries and restatements create duplicate rows unless the load deduplicates on a stable key. Why the correct answer wins: A checksum proves the bytes arrived unchanged.

### Question 9 — A

Answer: Order a Transfer Appliance. A Transfer Appliance moves the volume physically when the network cannot. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. In this case: A Transfer Appliance moves the volume physically when the network cannot.
- **B:** Incorrect for this question. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Why the correct answer wins: A Transfer Appliance moves the volume physically when the network cannot.
- **C:** Incorrect for this question. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Why the correct answer wins: A Transfer Appliance moves the volume physically when the network cannot.
- **D:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: A Transfer Appliance moves the volume physically when the network cannot.

### Question 10 — D

Answer: Use BigQuery Data Transfer Service. BigQuery Data Transfer Service schedules the recurring pull. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: BigQuery Data Transfer Service schedules the recurring pull.
- **B:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: BigQuery Data Transfer Service schedules the recurring pull.
- **C:** Incorrect for this question. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Why the correct answer wins: BigQuery Data Transfer Service schedules the recurring pull.
- **D:** Correct. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. In this case: BigQuery Data Transfer Service schedules the recurring pull.

### Question 11 — B

Answer: Copy the objects with the gcloud storage command. A gcloud storage copy is the direct path for an ad hoc move. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A hand-built FTP pull has no retry, no manifest, and no record of what arrived. Why the correct answer wins: A gcloud storage copy is the direct path for an ad hoc move.
- **B:** Correct. In this case: A gcloud storage copy is the direct path for an ad hoc move.
- **C:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: A gcloud storage copy is the direct path for an ad hoc move.
- **D:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A gcloud storage copy is the direct path for an ad hoc move.

### Question 12 — A, B

Answers: Use Database Migration Service; Use Storage Transfer Service. Database Migration Service moves the database, and Storage Transfer Service copies the files. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. In this case: Database Migration Service moves the database, and Storage Transfer Service copies the files.
- **B:** Correct. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. In this case: Database Migration Service moves the database, and Storage Transfer Service copies the files.
- **C:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: Database Migration Service moves the database, and Storage Transfer Service copies the files.
- **D:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Database Migration Service moves the database, and Storage Transfer Service copies the files.
- **E:** Incorrect for this question. A hand-built FTP pull has no retry, no manifest, and no record of what arrived. Why the correct answer wins: Database Migration Service moves the database, and Storage Transfer Service copies the files.

### Question 13 — A

Answer: Land the data as Avro. Avro embeds the schema with the records. Avro carries its schema with the records and suits row-oriented streaming exchanges. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Avro carries its schema with the records and suits row-oriented streaming exchanges. In this case: Avro embeds the schema with the records.
- **B:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Avro embeds the schema with the records.
- **C:** Incorrect for this question. XML nests well and is verbose, which makes it a poor fit for wide analytical scans. Why the correct answer wins: Avro embeds the schema with the records.
- **D:** Incorrect for this question. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Why the correct answer wins: Avro embeds the schema with the records.

### Question 14 — D

Answer: Land the data as Parquet. Parquet reads only the columns the training job needs. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. XML nests well and is verbose, which makes it a poor fit for wide analytical scans. Why the correct answer wins: Parquet reads only the columns the training job needs.
- **B:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: Parquet reads only the columns the training job needs.
- **C:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Parquet reads only the columns the training job needs.
- **D:** Correct. Parquet is columnar and compressed, so a scan reads only the columns a query needs. In this case: Parquet reads only the columns the training job needs.

### Question 15 — C

Answer: Land the data as newline-delimited JSON. Newline-delimited JSON keeps the nesting intact. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Avro carries its schema with the records and suits row-oriented streaming exchanges. Why the correct answer wins: Newline-delimited JSON keeps the nesting intact.
- **B:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Newline-delimited JSON keeps the nesting intact.
- **C:** Correct. Newline-delimited JSON keeps nested fields and can be appended one record at a time. In this case: Newline-delimited JSON keeps the nesting intact.
- **D:** Incorrect for this question. ORC is another columnar format; choosing it adds a conversion step without a benefit over Parquet here. Why the correct answer wins: Newline-delimited JSON keeps the nesting intact.

### Question 16 — A, E

Answers: Land the data as CSV; Land the data as XML. CSV and XML both hold text without declared column types. CSV is readable everywhere and carries no types, no schema, and no nesting. XML nests well and is verbose, which makes it a poor fit for wide analytical scans. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. XML nests well and is verbose, which makes it a poor fit for wide analytical scans. In this case: CSV and XML both hold text without declared column types.
- **B:** Incorrect for this question. Avro carries its schema with the records and suits row-oriented streaming exchanges. Why the correct answer wins: CSV and XML both hold text without declared column types.
- **C:** Incorrect for this question. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Why the correct answer wins: CSV and XML both hold text without declared column types.
- **D:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: CSV and XML both hold text without declared column types.
- **E:** Correct. CSV is readable everywhere and carries no types, no schema, and no nesting. In this case: CSV and XML both hold text without declared column types.

### Question 17 — A

Answer: Build the pipeline in Dataflow. A streaming Dataflow pipeline transforms each file as it arrives. Dataflow runs the same code for streaming and batch and scales the workers with the load. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Dataflow runs the same code for streaming and batch and scales the workers with the load. In this case: A streaming Dataflow pipeline transforms each file as it arrives.
- **B:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: A streaming Dataflow pipeline transforms each file as it arrives.
- **C:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A streaming Dataflow pipeline transforms each file as it arrives.
- **D:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: A streaming Dataflow pipeline transforms each file as it arrives.

### Question 18 — B

Answer: Replicate the changes with Datastream. Datastream captures the change stream instead of copying the table again. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: Datastream captures the change stream instead of copying the table again.
- **B:** Correct. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. In this case: Datastream captures the change stream instead of copying the table again.
- **C:** Incorrect for this question. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. Why the correct answer wins: Datastream captures the change stream instead of copying the table again.
- **D:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: Datastream captures the change stream instead of copying the table again.

### Question 19 — C

Answer: Build the pipeline in Cloud Data Fusion. Data Fusion expresses the extract and the mapping on a canvas. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Data Fusion expresses the extract and the mapping on a canvas.
- **B:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Data Fusion expresses the extract and the mapping on a canvas.
- **C:** Correct. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. In this case: Data Fusion expresses the extract and the mapping on a canvas.
- **D:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Data Fusion expresses the extract and the mapping on a canvas.

### Question 20 — A

Answer: Store the rows in Bigtable. Bigtable gives low-latency lookups keyed by one row key at high write rates. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. In this case: Bigtable gives low-latency lookups keyed by one row key at high write rates.
- **B:** Incorrect for this question. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Why the correct answer wins: Bigtable gives low-latency lookups keyed by one row key at high write rates.
- **C:** Incorrect for this question. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Why the correct answer wins: Bigtable gives low-latency lookups keyed by one row key at high write rates.
- **D:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: Bigtable gives low-latency lookups keyed by one row key at high write rates.

### Question 21 — C

Answer: Store the files in Cloud Storage. Cloud Storage holds objects of any shape and any size. Cloud Storage holds objects of any shape and is the landing zone every other service can read. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Spanner gives strongly consistent relational transactions across regions at global scale. Why the correct answer wins: Cloud Storage holds objects of any shape and any size.
- **B:** Incorrect for this question. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Why the correct answer wins: Cloud Storage holds objects of any shape and any size.
- **C:** Correct. Cloud Storage holds objects of any shape and is the landing zone every other service can read. In this case: Cloud Storage holds objects of any shape and any size.
- **D:** Incorrect for this question. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Why the correct answer wins: Cloud Storage holds objects of any shape and any size.

### Question 22 — D

Answer: Store the records in Spanner. Spanner gives strongly consistent transactions across regions. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: Spanner gives strongly consistent transactions across regions.
- **B:** Incorrect for this question. AlloyDB is a managed PostgreSQL option for transaction workloads that want PostgreSQL compatibility. Why the correct answer wins: Spanner gives strongly consistent transactions across regions.
- **C:** Incorrect for this question. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Why the correct answer wins: Spanner gives strongly consistent transactions across regions.
- **D:** Correct. In this case: Spanner gives strongly consistent transactions across regions.

### Question 23 — C, D

Answers: Store the rows in BigQuery; Store the records in Cloud SQL. BigQuery serves the columnar scans, and Cloud SQL serves the transactions. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: BigQuery serves the columnar scans, and Cloud SQL serves the transactions.
- **B:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: BigQuery serves the columnar scans, and Cloud SQL serves the transactions.
- **C:** Correct. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. In this case: BigQuery serves the columnar scans, and Cloud SQL serves the transactions.
- **D:** Correct. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. In this case: BigQuery serves the columnar scans, and Cloud SQL serves the transactions.
- **E:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: BigQuery serves the columnar scans, and Cloud SQL serves the transactions.

### Question 24 — D

Answer: Choose a multi-region location. A multi-region location spreads the copies across the geography. A multi-region location spreads the data across a continent-scale geography for the widest availability. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: A multi-region location spreads the copies across the geography.
- **B:** Incorrect for this question. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Why the correct answer wins: A multi-region location spreads the copies across the geography.
- **C:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: A multi-region location spreads the copies across the geography.
- **D:** Correct. A multi-region location spreads the data across a continent-scale geography for the widest availability. In this case: A multi-region location spreads the copies across the geography.

### Question 25 — B

Answer: Choose a regional location. One region is the cheapest placement that still meets the latency target. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: One region is the cheapest placement that still meets the latency target.
- **B:** Correct. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. In this case: One region is the cheapest placement that still meets the latency target.
- **C:** Incorrect for this question. Distance between the data and the readers shows up as latency on every query. Why the correct answer wins: One region is the cheapest placement that still meets the latency target.
- **D:** Incorrect for this question. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Why the correct answer wins: One region is the cheapest placement that still meets the latency target.

### Question 26 — C

Answer: Choose a dual-region location. A dual-region location states the pair explicitly. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: A dual-region location states the pair explicitly.
- **B:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: A dual-region location states the pair explicitly.
- **C:** Correct. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. In this case: A dual-region location states the pair explicitly.
- **D:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: A dual-region location states the pair explicitly.

### Question 27 — C

Answer: Treat the files as unstructured data. Scanned documents have no field model, which makes them unstructured. Unstructured data has no field model at all, such as images, audio, or free documents. Local study-map skill 1.8 (Structured, Semi-Structured, and Unstructured Data), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Why the correct answer wins: Scanned documents have no field model, which makes them unstructured.
- **B:** Incorrect for this question. Semi-structured data has a flexible shape such as JSON, where fields vary between records. Why the correct answer wins: Scanned documents have no field model, which makes them unstructured.
- **C:** Correct. Unstructured data has no field model at all, such as images, audio, or free documents. In this case: Scanned documents have no field model, which makes them unstructured.
- **D:** Incorrect for this question. Structured data fits a declared schema of rows and columns. Why the correct answer wins: Scanned documents have no field model, which makes them unstructured.

### Question 28 — A

Answer: Treat the records as semi-structured data. A flexible shape that varies between records is semi-structured data. Semi-structured data has a flexible shape such as JSON, where fields vary between records. Local study-map skill 1.8 (Structured, Semi-Structured, and Unstructured Data), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Semi-structured data has a flexible shape such as JSON, where fields vary between records. In this case: A flexible shape that varies between records is semi-structured data.
- **B:** Incorrect for this question. Structured data fits a declared schema of rows and columns. Why the correct answer wins: A flexible shape that varies between records is semi-structured data.
- **C:** Incorrect for this question. Unstructured data has no field model at all, such as images, audio, or free documents. Why the correct answer wins: A flexible shape that varies between records is semi-structured data.
- **D:** Incorrect for this question. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Why the correct answer wins: A flexible shape that varies between records is semi-structured data.

### Question 29 — C

Answer: Stream the rows with the BigQuery Storage Write API. The Storage Write API commits rows as the stream produces them. Local study-map skill 1.9 (Loading with CLIs and Client Libraries), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: The Storage Write API commits rows as the stream produces them.
- **B:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: The Storage Write API commits rows as the stream produces them.
- **C:** Correct. In this case: The Storage Write API commits rows as the stream produces them.
- **D:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: The Storage Write API commits rows as the stream produces them.

### Question 30 — A

Answer: Load the files with the bq load command. A load job reads the objects and appends the rows to the table. The bq load command creates a load job that reads files from Cloud Storage into a table. Local study-map skill 1.9 (Loading with CLIs and Client Libraries), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. The bq load command creates a load job that reads files from Cloud Storage into a table. In this case: A load job reads the objects and appends the rows to the table.
- **B:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: A load job reads the objects and appends the rows to the table.
- **C:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A load job reads the objects and appends the rows to the table.
- **D:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: A load job reads the objects and appends the rows to the table.

### Question 31 — D

Answer: Create a BigQuery view over the join. A view stores the query and returns current rows on read. A view stores the query rather than the rows, so the answer stays current at query time. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. Why the correct answer wins: A view stores the query and returns current rows on read.
- **B:** Incorrect for this question. A native table gives the warehouse its own copy and the best scan performance. Why the correct answer wins: A view stores the query and returns current rows on read.
- **C:** Incorrect for this question. An external table reads the objects where they sit and does not copy them into storage. Why the correct answer wins: A view stores the query and returns current rows on read.
- **D:** Correct. A view stores the query rather than the rows, so the answer stays current at query time. In this case: A view stores the query and returns current rows on read.

### Question 32 — D

Answer: Write a SQL query in BigQuery and save the result. A saved query answers the question and can be re-run. A saved SQL query answers a business question and can be scheduled or exported. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A saved query answers the question and can be re-run.
- **B:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: A saved query answers the question and can be re-run.
- **C:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A saved query answers the question and can be re-run.
- **D:** Correct. A saved SQL query answers a business question and can be scheduled or exported. In this case: A saved query answers the question and can be re-run.

### Question 33 — A, C

Answers: Load the files into a native table; Filter the query on the partition column. Loading into a native table removes the external read, and the partition filter narrows the scan. A native table gives the warehouse its own copy and the best scan performance. A partition filter restricts the scan to the partitions the query needs. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A partition filter restricts the scan to the partitions the query needs. In this case: Loading into a native table removes the external read, and the partition filter narrows the scan.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: Loading into a native table removes the external read, and the partition filter narrows the scan.
- **C:** Correct. A native table gives the warehouse its own copy and the best scan performance. In this case: Loading into a native table removes the external read, and the partition filter narrows the scan.
- **D:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: Loading into a native table removes the external read, and the partition filter narrows the scan.
- **E:** Incorrect for this question. An external table reads the objects where they sit and does not copy them into storage. Why the correct answer wins: Loading into a native table removes the external read, and the partition filter narrows the scan.

### Question 34 — B

Answer: Create a BigQuery materialized view. A materialized view stores the result and refreshes it. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A view stores the query rather than the rows, so the answer stays current at query time. Why the correct answer wins: A materialized view stores the result and refreshes it.
- **B:** Correct. In this case: A materialized view stores the result and refreshes it.
- **C:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: A materialized view stores the result and refreshes it.
- **D:** Incorrect for this question. An external table reads the objects where they sit and does not copy them into storage. Why the correct answer wins: A materialized view stores the result and refreshes it.

### Question 35 — B

Answer: Analyse the data in a Colab Enterprise notebook. Colab Enterprise provides the managed runtime inside the project. Colab Enterprise gives a managed notebook runtime with project IAM and BigQuery access. Local study-map skill 2.2 (Colab Enterprise and Jupyter Notebooks), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: Colab Enterprise provides the managed runtime inside the project.
- **B:** Correct. Colab Enterprise gives a managed notebook runtime with project IAM and BigQuery access. In this case: Colab Enterprise provides the managed runtime inside the project.
- **C:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Colab Enterprise provides the managed runtime inside the project.
- **D:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: Colab Enterprise provides the managed runtime inside the project.

### Question 36 — A

Answer: Query BigQuery from the notebook with the %%bigquery magic. The BigQuery magic uses the runtime's own identity for the query. The magic returns a DataFrame from a SQL statement inside the notebook cell. Local study-map skill 2.2 (Colab Enterprise and Jupyter Notebooks), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. The magic returns a DataFrame from a SQL statement inside the notebook cell. In this case: The BigQuery magic uses the runtime's own identity for the query.
- **B:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: The BigQuery magic uses the runtime's own identity for the query.
- **C:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: The BigQuery magic uses the runtime's own identity for the query.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: The BigQuery magic uses the runtime's own identity for the query.

### Question 37 — B

Answer: Write a SQL query in BigQuery and save the result. A SQL query returns the drivers and can be re-run as the question evolves. A saved SQL query answers a business question and can be scheduled or exported. Local study-map skill 2.3 (Business Question Analysis), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: A SQL query returns the drivers and can be re-run as the question evolves.
- **B:** Correct. A saved SQL query answers a business question and can be scheduled or exported. In this case: A SQL query returns the drivers and can be re-run as the question evolves.
- **C:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: A SQL query returns the drivers and can be re-run as the question evolves.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A SQL query returns the drivers and can be re-run as the question evolves.

### Question 38 — A

Answer: Build a governed Looker dashboard. A governed dashboard lets the team explore the result without a new request. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Local study-map skill 2.3 (Business Question Analysis), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: A governed dashboard lets the team explore the result without a new request.
- **B:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: A governed dashboard lets the team explore the result without a new request.
- **C:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A governed dashboard lets the team explore the result without a new request.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A governed dashboard lets the team explore the result without a new request.

### Question 39 — B, C

Answers: Build a governed Looker dashboard; Share the dashboard with a scheduled delivery. The Looker dashboard holds the governed definitions, and the delivery pushes it outward. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. A scheduled delivery pushes the answer to people who will not open the tool. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: The Looker dashboard holds the governed definitions, and the delivery pushes it outward.
- **B:** Correct. A scheduled delivery pushes the answer to people who will not open the tool. In this case: The Looker dashboard holds the governed definitions, and the delivery pushes it outward.
- **C:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: The Looker dashboard holds the governed definitions, and the delivery pushes it outward.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The Looker dashboard holds the governed definitions, and the delivery pushes it outward.
- **E:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: The Looker dashboard holds the governed definitions, and the delivery pushes it outward.

### Question 40 — C

Answer: Build a governed Looker dashboard. A Looker dashboard reads one model, so no tile can change the definition. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A Looker dashboard reads one model, so no tile can change the definition.
- **B:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: A Looker dashboard reads one model, so no tile can change the definition.
- **C:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: A Looker dashboard reads one model, so no tile can change the definition.
- **D:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A Looker dashboard reads one model, so no tile can change the definition.

### Question 41 — B

Answer: Build a Looker Studio report. Looker Studio connects a handful of sources quickly. Looker Studio is the fast self-serve reporting surface for a small number of sources. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Looker Studio connects a handful of sources quickly.
- **B:** Correct. Looker Studio is the fast self-serve reporting surface for a small number of sources. In this case: Looker Studio connects a handful of sources quickly.
- **C:** Incorrect for this question. An explore defines which joins and fields a report author may use. Why the correct answer wins: Looker Studio connects a handful of sources quickly.
- **D:** Incorrect for this question. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Why the correct answer wins: Looker Studio connects a handful of sources quickly.

### Question 42 — C

Answer: Build a Looker Studio report. Looker Studio is the self-serve option for a small number of sources. Looker Studio is the fast self-serve reporting surface for a small number of sources. Local study-map skill 2.5 (Looker and Looker Studio Comparison), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Why the correct answer wins: Looker Studio is the self-serve option for a small number of sources.
- **B:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: Looker Studio is the self-serve option for a small number of sources.
- **C:** Correct. Looker Studio is the fast self-serve reporting surface for a small number of sources. In this case: Looker Studio is the self-serve option for a small number of sources.
- **D:** Incorrect for this question. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Why the correct answer wins: Looker Studio is the self-serve option for a small number of sources.

### Question 43 — B

Answer: Build a governed Looker dashboard. Looker serves every report from one modelled definition. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Local study-map skill 2.5 (Looker and Looker Studio Comparison), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Looker serves every report from one modelled definition.
- **B:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: Looker serves every report from one modelled definition.
- **C:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: Looker serves every report from one modelled definition.
- **D:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: Looker serves every report from one modelled definition.

### Question 44 — D

Answer: Add a LookML measure for the calculation. A measure declares the ratio once for every report. A measure declares the aggregation once so every report computes it the same way. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A measure declares the ratio once for every report.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A measure declares the ratio once for every report.
- **C:** Incorrect for this question. An explore defines which joins and fields a report author may use. Why the correct answer wins: A measure declares the ratio once for every report.
- **D:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: A measure declares the ratio once for every report.

### Question 45 — B, C

Answers: Change the LookML parameter in the view; Add a LookML measure for the calculation. The parameter sets the calendar once, and the measure fixes the definition. A LookML parameter changes the model for every dashboard that uses it rather than one tile. A measure declares the aggregation once so every report computes it the same way. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The parameter sets the calendar once, and the measure fixes the definition.
- **B:** Correct. A LookML parameter changes the model for every dashboard that uses it rather than one tile. In this case: The parameter sets the calendar once, and the measure fixes the definition.
- **C:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: The parameter sets the calendar once, and the measure fixes the definition.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: The parameter sets the calendar once, and the measure fixes the definition.
- **E:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: The parameter sets the calendar once, and the measure fixes the definition.

### Question 46 — B

Answer: Expose the table through a LookML explore. An explore declares which joins a report author may use. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Why the correct answer wins: An explore declares which joins a report author may use.
- **B:** Correct. In this case: An explore declares which joins a report author may use.
- **C:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: An explore declares which joins a report author may use.
- **D:** Incorrect for this question. A view stores the query rather than the rows, so the answer stays current at query time. Why the correct answer wins: An explore declares which joins a report author may use.

### Question 47 — C

Answer: Train a BigQuery ML k-means model. K-means groups rows without a label. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Linear regression predicts a continuous value and trains with SQL against the table. Why the correct answer wins: K-means groups rows without a label.
- **B:** Incorrect for this question. ML.PREDICT applies a trained model to new rows and returns the prediction. Why the correct answer wins: K-means groups rows without a label.
- **C:** Correct. In this case: K-means groups rows without a label.
- **D:** Incorrect for this question. Logistic regression predicts a binary outcome and trains with SQL against the table. Why the correct answer wins: K-means groups rows without a label.

### Question 48 — B

Answer: Train a BigQuery ML ARIMA_PLUS model. ARIMA_PLUS models trend and seasonality and returns an interval. ARIMA_PLUS forecasts a series and returns an interval per period. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A boosted tree model fits non-linear relationships in tabular rows. Why the correct answer wins: ARIMA_PLUS models trend and seasonality and returns an interval.
- **B:** Correct. ARIMA_PLUS forecasts a series and returns an interval per period. In this case: ARIMA_PLUS models trend and seasonality and returns an interval.
- **C:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: ARIMA_PLUS models trend and seasonality and returns an interval.
- **D:** Incorrect for this question. Linear regression predicts a continuous value and trains with SQL against the table. Why the correct answer wins: ARIMA_PLUS models trend and seasonality and returns an interval.

### Question 49 — C, D

Answers: Train a BigQuery ML logistic regression model; Train a BigQuery ML linear regression model. Logistic regression returns the flag, and linear regression returns the amount. Logistic regression predicts a binary outcome and trains with SQL against the table. Linear regression predicts a continuous value and trains with SQL against the table. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: Logistic regression returns the flag, and linear regression returns the amount.
- **B:** Incorrect for this question. AutoML searches architectures and tuning for a team that has labels but no modelling code. Why the correct answer wins: Logistic regression returns the flag, and linear regression returns the amount.
- **C:** Correct. Linear regression predicts a continuous value and trains with SQL against the table. In this case: Logistic regression returns the flag, and linear regression returns the amount.
- **D:** Correct. Logistic regression predicts a binary outcome and trains with SQL against the table. In this case: Logistic regression returns the flag, and linear regression returns the amount.
- **E:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: Logistic regression returns the flag, and linear regression returns the amount.

### Question 50 — B

Answer: Create a BigQuery remote model over a Gemini model. A remote model sends the prompt from SQL and the rows never move. A remote model sends the prompt to Gemini from SQL while the rows stay in BigQuery. Local study-map skill 2.8 (Remote Gemini Models in BigQuery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: A remote model sends the prompt from SQL and the rows never move.
- **B:** Correct. A remote model sends the prompt to Gemini from SQL while the rows stay in BigQuery. In this case: A remote model sends the prompt from SQL and the rows never move.
- **C:** Incorrect for this question. Fine-tuning adapts the model to the domain using labelled rows that stay in BigQuery. Why the correct answer wins: A remote model sends the prompt from SQL and the rows never move.
- **D:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: A remote model sends the prompt from SQL and the rows never move.

### Question 51 — A

Answer: Create the BigQuery connection that reaches the model endpoint. The connection supplies the identity that reaches the endpoint. The connection carries the service account that BigQuery uses to call the remote model. Local study-map skill 2.8 (Remote Gemini Models in BigQuery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. The connection carries the service account that BigQuery uses to call the remote model. In this case: The connection supplies the identity that reaches the endpoint.
- **B:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: The connection supplies the identity that reaches the endpoint.
- **C:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: The connection supplies the identity that reaches the endpoint.
- **D:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: The connection supplies the identity that reaches the endpoint.

### Question 52 — B

Answer: Plan collection, training, evaluation, then prediction. A plan fixes the metric and the acceptance test before training starts. A planned sequence fixes the data, the metric, and the acceptance test before any model is trained. Local study-map skill 2.9 (ML Project Planning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: A plan fixes the metric and the acceptance test before training starts.
- **B:** Correct. A planned sequence fixes the data, the metric, and the acceptance test before any model is trained. In this case: A plan fixes the metric and the acceptance test before training starts.
- **C:** Incorrect for this question. Training loss measures fit to the rows it has already seen, not the answer on new rows. Why the correct answer wins: A plan fixes the metric and the acceptance test before training starts.
- **D:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A plan fixes the metric and the acceptance test before training starts.

### Question 53 — B

Answer: Hold the most recent period out as the test set. A time-based split tests the model on later periods. A time-ordered split tests the model on rows that come after the ones it learned from. Local study-map skill 2.9 (ML Project Planning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A grouped split keeps one customer from appearing on both sides of the evaluation. Why the correct answer wins: A time-based split tests the model on later periods.
- **B:** Correct. A time-ordered split tests the model on rows that come after the ones it learned from. In this case: A time-based split tests the model on later periods.
- **C:** Incorrect for this question. A held-out split gives an estimate that the training rows cannot inflate. Why the correct answer wins: A time-based split tests the model on later periods.
- **D:** Incorrect for this question. Training loss measures fit to the rows it has already seen, not the answer on new rows. Why the correct answer wins: A time-based split tests the model on later periods.

### Question 54 — B

Answer: Evaluate the model with ML.EVALUATE. ML.EVALUATE returns the metrics against a labelled dataset. Local study-map skill 2.10 (BigQuery ML Training and Evaluation), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.PREDICT applies a trained model to new rows and returns the prediction. Why the correct answer wins: ML.EVALUATE returns the metrics against a labelled dataset.
- **B:** Correct. In this case: ML.EVALUATE returns the metrics against a labelled dataset.
- **C:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: ML.EVALUATE returns the metrics against a labelled dataset.
- **D:** Incorrect for this question. ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row. Why the correct answer wins: ML.EVALUATE returns the metrics against a labelled dataset.

### Question 55 — B

Answer: Train a BigQuery ML boosted tree model. A boosted tree fits non-linear tabular relationships. Local study-map skill 2.10 (BigQuery ML Training and Evaluation), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Linear regression predicts a continuous value and trains with SQL against the table. Why the correct answer wins: A boosted tree fits non-linear tabular relationships.
- **B:** Correct. In this case: A boosted tree fits non-linear tabular relationships.
- **C:** Incorrect for this question. ARIMA_PLUS forecasts a series and returns an interval per period. Why the correct answer wins: A boosted tree fits non-linear tabular relationships.
- **D:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: A boosted tree fits non-linear tabular relationships.

### Question 56 — D

Answer: Score the rows with ML.PREDICT. ML.PREDICT applies the model to the new rows. ML.PREDICT applies a trained model to new rows and returns the prediction. Local study-map skill 2.11 (BigQuery ML Inference), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: ML.PREDICT applies the model to the new rows.
- **B:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: ML.PREDICT applies the model to the new rows.
- **C:** Incorrect for this question. ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row. Why the correct answer wins: ML.PREDICT applies the model to the new rows.
- **D:** Correct. ML.PREDICT applies a trained model to new rows and returns the prediction. In this case: ML.PREDICT applies the model to the new rows.

### Question 57 — C

Answer: Register the model version in Model Registry. Model Registry keeps each version with its lineage and dates. Model Registry keeps each version with its lineage so a deployment names a version rather than a path. Local study-map skill 2.12 (Model Registry), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: Model Registry keeps each version with its lineage and dates.
- **B:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Model Registry keeps each version with its lineage and dates.
- **C:** Correct. Model Registry keeps each version with its lineage so a deployment names a version rather than a path. In this case: Model Registry keeps each version with its lineage and dates.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: Model Registry keeps each version with its lineage and dates.

### Question 58 — B

Answer: Manage the SQL transformations in Dataform. Dataform resolves the dependencies and runs the graph. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Dataform resolves the dependencies and runs the graph.
- **B:** Correct. In this case: Dataform resolves the dependencies and runs the graph.
- **C:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Dataform resolves the dependencies and runs the graph.
- **D:** Incorrect for this question. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Why the correct answer wins: Dataform resolves the dependencies and runs the graph.

### Question 59 — A

Answer: Build the pipeline in Dataflow. Dataflow windows the stream and runs the same code for batch input. Dataflow runs the same code for streaming and batch and scales the workers with the load. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Dataflow runs the same code for streaming and batch and scales the workers with the load. In this case: Dataflow windows the stream and runs the same code for batch input.
- **B:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Dataflow windows the stream and runs the same code for batch input.
- **C:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Dataflow windows the stream and runs the same code for batch input.
- **D:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Dataflow windows the stream and runs the same code for batch input.

### Question 60 — D

Answer: Build the pipeline in Cloud Data Fusion. Data Fusion joins the sources in a versioned visual pipeline. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Data Fusion joins the sources in a versioned visual pipeline.
- **B:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Data Fusion joins the sources in a versioned visual pipeline.
- **C:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Data Fusion joins the sources in a versioned visual pipeline.
- **D:** Correct. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. In this case: Data Fusion joins the sources in a versioned visual pipeline.

### Question 61 — B, D

Answers: Run the transformation as Spark on Dataproc; Orchestrate the steps in Cloud Composer. Dataproc runs the Spark job, and Composer holds the dependency and the retry. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Dataproc runs the Spark job, and Composer holds the dependency and the retry.
- **B:** Correct. Dataproc runs Spark or Hadoop jobs when the team already owns that code. In this case: Dataproc runs the Spark job, and Composer holds the dependency and the retry.
- **C:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Dataproc runs the Spark job, and Composer holds the dependency and the retry.
- **D:** Correct. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. In this case: Dataproc runs the Spark job, and Composer holds the dependency and the retry.
- **E:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Dataproc runs the Spark job, and Composer holds the dependency and the retry.

### Question 62 — D

Answer: Load the raw rows, then transform them inside the warehouse. ELT pushes the transformation to the warehouse engine. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 3.2 (ELT and ETL Pipeline Design), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT pushes the transformation to the warehouse engine.
- **B:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ELT pushes the transformation to the warehouse engine.
- **C:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ELT pushes the transformation to the warehouse engine.
- **D:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT pushes the transformation to the warehouse engine.

### Question 63 — A

Answer: Extract, transform outside the warehouse, then load the result. ETL cleans the record before the destination sees it. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Local study-map skill 3.2 (ELT and ETL Pipeline Design), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. In this case: ETL cleans the record before the destination sees it.
- **B:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: ETL cleans the record before the destination sees it.
- **C:** Incorrect for this question. A staging table separates a failed load from a failed transform, so each can be retried on its own. Why the correct answer wins: ETL cleans the record before the destination sees it.
- **D:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETL cleans the record before the destination sees it.

### Question 64 — B

Answer: Schedule the SQL with a BigQuery scheduled query. A scheduled query runs one statement on a cron schedule. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **B:** Correct. In this case: A scheduled query runs one statement on a cron schedule.
- **C:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **D:** Incorrect for this question. A workflow template defines the cluster and the steps so the same job can be re-run identically. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.

### Question 65 — D

Answer: Trigger the job from Cloud Scheduler. Cloud Scheduler calls the endpoint on the schedule. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Cloud Scheduler calls the endpoint on the schedule.
- **B:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Cloud Scheduler calls the endpoint on the schedule.
- **C:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Cloud Scheduler calls the endpoint on the schedule.
- **D:** Correct. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. In this case: Cloud Scheduler calls the endpoint on the schedule.

### Question 66 — A, C

Answers: Schedule the SQL with a BigQuery scheduled query; Trigger the job from Cloud Scheduler. The scheduled query runs the statement, and the scheduler calls the endpoint. A scheduled query runs one statement on a cron schedule and writes its result. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A scheduled query runs one statement on a cron schedule and writes its result. In this case: The scheduled query runs the statement, and the scheduler calls the endpoint.
- **B:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: The scheduled query runs the statement, and the scheduler calls the endpoint.
- **C:** Correct. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. In this case: The scheduled query runs the statement, and the scheduler calls the endpoint.
- **D:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: The scheduled query runs the statement, and the scheduler calls the endpoint.
- **E:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: The scheduled query runs the statement, and the scheduler calls the endpoint.

### Question 67 — C

Answer: Watch the job graph and per-step throughput in the Dataflow console. The job view shows the throughput of each step in the graph. The Dataflow job view shows the running graph, watermarks, and the step that is backlogged. Local study-map skill 3.4 (Dataflow Job Monitoring), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The job view shows the throughput of each step in the graph.
- **B:** Incorrect for this question. Logs Explorer filters the log entries that explain why a worker restarted. Why the correct answer wins: The job view shows the throughput of each step in the graph.
- **C:** Correct. The Dataflow job view shows the running graph, watermarks, and the step that is backlogged. In this case: The job view shows the throughput of each step in the graph.
- **D:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: The job view shows the throughput of each step in the graph.

### Question 68 — C

Answer: Write the rejected rows to a dead-letter table. A dead-letter table keeps the rejected events for replay. A dead-letter table preserves the rows that failed so they can be repaired and replayed. Local study-map skill 3.4 (Dataflow Job Monitoring), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A dead-letter table keeps the rejected events for replay.
- **B:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A dead-letter table keeps the rejected events for replay.
- **C:** Correct. A dead-letter table preserves the rows that failed so they can be repaired and replayed. In this case: A dead-letter table keeps the rejected events for replay.
- **D:** Incorrect for this question. A wide table removes the join, at the cost of duplicated rows and a wider scan. Why the correct answer wins: A dead-letter table keeps the rejected events for replay.

### Question 69 — C

Answer: Query the job logs in Logs Explorer. Logs Explorer filters the entries for that identifier. Logs Explorer filters the log entries that explain why a worker restarted. Local study-map skill 3.5 (Logs and Monitoring Review), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: Logs Explorer filters the entries for that identifier.
- **B:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: Logs Explorer filters the entries for that identifier.
- **C:** Correct. Logs Explorer filters the log entries that explain why a worker restarted. In this case: Logs Explorer filters the entries for that identifier.
- **D:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Logs Explorer filters the entries for that identifier.

### Question 70 — C

Answer: Create a Cloud Monitoring alert policy on the job metric. An alert policy on the job metric pages the owner. An alert policy pages someone when the backlog or the failure rate crosses a threshold. Local study-map skill 3.5 (Logs and Monitoring Review), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Logs Explorer filters the log entries that explain why a worker restarted. Why the correct answer wins: An alert policy on the job metric pages the owner.
- **B:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: An alert policy on the job metric pages the owner.
- **C:** Correct. An alert policy pages someone when the backlog or the failure rate crosses a threshold. In this case: An alert policy on the job metric pages the owner.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: An alert policy on the job metric pages the owner.

### Question 71 — D

Answer: Orchestrate the steps in Cloud Composer. Cloud Composer runs an Airflow DAG with dependencies and retries. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Cloud Composer runs an Airflow DAG with dependencies and retries.
- **B:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Cloud Composer runs an Airflow DAG with dependencies and retries.
- **C:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Cloud Composer runs an Airflow DAG with dependencies and retries.
- **D:** Correct. In this case: Cloud Composer runs an Airflow DAG with dependencies and retries.

### Question 72 — D

Answer: Sequence the API calls with Workflows. Workflows chains the calls without a server. Workflows chains service calls and HTTP endpoints without running a server. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Workflows chains the calls without a server.
- **B:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Workflows chains the calls without a server.
- **C:** Incorrect for this question. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Why the correct answer wins: Workflows chains the calls without a server.
- **D:** Correct. Workflows chains service calls and HTTP endpoints without running a server. In this case: Workflows chains the calls without a server.

### Question 73 — C, E

Answers: Orchestrate the steps in Cloud Composer; Schedule the SQL with a BigQuery scheduled query. The scheduled query runs the SQL, and Composer handles the waits and retries. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. A scheduled query runs one statement on a cron schedule and writes its result. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: The scheduled query runs the SQL, and Composer handles the waits and retries.
- **B:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: The scheduled query runs the SQL, and Composer handles the waits and retries.
- **C:** Correct. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. In this case: The scheduled query runs the SQL, and Composer handles the waits and retries.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The scheduled query runs the SQL, and Composer handles the waits and retries.
- **E:** Correct. A scheduled query runs one statement on a cron schedule and writes its result. In this case: The scheduled query runs the SQL, and Composer handles the waits and retries.

### Question 74 — B

Answer: Subscribe BigQuery to the Pub/Sub topic. A BigQuery subscription writes each message into the table. Local study-map skill 3.7 (Event-Driven Ingestion with Pub/Sub), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Why the correct answer wins: A BigQuery subscription writes each message into the table.
- **B:** Correct. In this case: A BigQuery subscription writes each message into the table.
- **C:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A BigQuery subscription writes each message into the table.
- **D:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: A BigQuery subscription writes each message into the table.

### Question 75 — A

Answer: Start the pipeline from an Eventarc trigger. An Eventarc trigger routes the object event to the Dataform target. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Local study-map skill 3.8 (Eventarc Triggers), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. In this case: An Eventarc trigger routes the object event to the Dataform target.
- **B:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: An Eventarc trigger routes the object event to the Dataform target.
- **C:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: An Eventarc trigger routes the object event to the Dataform target.
- **D:** Incorrect for this question. A BigQuery subscription writes each published message into a table as it arrives. Why the correct answer wins: An Eventarc trigger routes the object event to the Dataform target.

### Question 76 — B

Answer: Grant the predefined role that matches the task. The narrowest role that reads those views keeps the rest closed. A predefined role carries the permissions for one job and nothing else. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: The narrowest role that reads those views keeps the rest closed.
- **B:** Correct. A predefined role carries the permissions for one job and nothing else. In this case: The narrowest role that reads those views keeps the rest closed.
- **C:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: The narrowest role that reads those views keeps the rest closed.
- **D:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: The narrowest role that reads those views keeps the rest closed.

### Question 77 — D

Answer: Run the job as a dedicated service account. A service account gives the job an identity of its own. A service account gives the workload its own identity instead of borrowing a person's. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: A service account gives the job an identity of its own.
- **B:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A service account gives the job an identity of its own.
- **C:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A service account gives the job an identity of its own.
- **D:** Correct. A service account gives the workload its own identity instead of borrowing a person's. In this case: A service account gives the job an identity of its own.

### Question 78 — C, E

Answers: Grant the predefined role that matches the task; Issue a signed URL with a short expiry. A scoped role limits what the principal can do, and a signed URL expires on its own. A predefined role carries the permissions for one job and nothing else. A signed URL grants temporary read access to one object without changing IAM. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A scoped role limits what the principal can do, and a signed URL expires on its own.
- **B:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A scoped role limits what the principal can do, and a signed URL expires on its own.
- **C:** Correct. A signed URL grants temporary read access to one object without changing IAM. In this case: A scoped role limits what the principal can do, and a signed URL expires on its own.
- **D:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A scoped role limits what the principal can do, and a signed URL expires on its own.
- **E:** Correct. A predefined role carries the permissions for one job and nothing else. In this case: A scoped role limits what the principal can do, and a signed URL expires on its own.

### Question 79 — D

Answer: Assign a predefined role to the group. A predefined role for that function is maintained by Google. Local study-map skill 4.2 (Basic, Predefined, and Custom Roles), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A predefined role for that function is maintained by Google.
- **B:** Incorrect for this question. A custom role narrows the grant when no predefined role matches the job exactly. Why the correct answer wins: A predefined role for that function is maintained by Google.
- **C:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A predefined role for that function is maintained by Google.
- **D:** Correct. In this case: A predefined role for that function is maintained by Google.

### Question 80 — C

Answer: Create a custom role with only the permissions used. A custom role removes the permission without widening anything else. A custom role narrows the grant when no predefined role matches the job exactly. Local study-map skill 4.2 (Basic, Predefined, and Custom Roles), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A custom role removes the permission without widening anything else.
- **B:** Incorrect for this question. A predefined role is maintained by Google and covers one service or one job function. Why the correct answer wins: A custom role removes the permission without widening anything else.
- **C:** Correct. A custom role narrows the grant when no predefined role matches the job exactly. In this case: A custom role removes the permission without widening anything else.
- **D:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A custom role removes the permission without widening anything else.

### Question 81 — A

Answer: Enable uniform bucket-level access. Uniform bucket-level access puts every decision in IAM. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. Local study-map skill 4.3 (Cloud Storage Access Control), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. In this case: Uniform bucket-level access puts every decision in IAM.
- **B:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: Uniform bucket-level access puts every decision in IAM.
- **C:** Incorrect for this question. Per-object ACLs are hard to audit and are overridden when uniform access is enabled. Why the correct answer wins: Uniform bucket-level access puts every decision in IAM.
- **D:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Uniform bucket-level access puts every decision in IAM.

### Question 82 — B

Answer: Manage per-object ACLs on the bucket. A per-object ACL grants that one exception while uniform access stays off. Per-object ACLs are hard to audit and are overridden when uniform access is enabled. Local study-map skill 4.3 (Cloud Storage Access Control), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. Why the correct answer wins: A per-object ACL grants that one exception while uniform access stays off.
- **B:** Correct. Per-object ACLs are hard to audit and are overridden when uniform access is enabled. In this case: A per-object ACL grants that one exception while uniform access stays off.
- **C:** Incorrect for this question. An export hands over a copy that the publisher can no longer control or revoke. Why the correct answer wins: A per-object ACL grants that one exception while uniform access stays off.
- **D:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A per-object ACL grants that one exception while uniform access stays off.

### Question 83 — A

Answer: Publish the dataset through Analytics Hub. Analytics Hub shares the dataset in place and keeps it current. Analytics Hub shares a curated dataset with a subscriber who reads it in place. Local study-map skill 4.4 (Analytics Hub Data Sharing), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Analytics Hub shares a curated dataset with a subscriber who reads it in place. In this case: Analytics Hub shares the dataset in place and keeps it current.
- **B:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: Analytics Hub shares the dataset in place and keeps it current.
- **C:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Analytics Hub shares the dataset in place and keeps it current.
- **D:** Incorrect for this question. An export hands over a copy that the publisher can no longer control or revoke. Why the correct answer wins: Analytics Hub shares the dataset in place and keeps it current.

### Question 84 — A

Answer: Export the table to a bucket the partner owns. An export places the copy under the partner's control. An export hands over a copy that the publisher can no longer control or revoke. Local study-map skill 4.4 (Analytics Hub Data Sharing), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. An export hands over a copy that the publisher can no longer control or revoke. In this case: An export places the copy under the partner's control.
- **B:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: An export places the copy under the partner's control.
- **C:** Incorrect for this question. A perimeter blocks data movement outside the boundary even for an authorised identity. Why the correct answer wins: An export places the copy under the partner's control.
- **D:** Incorrect for this question. Analytics Hub shares a curated dataset with a subscriber who reads it in place. Why the correct answer wins: An export places the copy under the partner's control.

### Question 85 — D

Answer: Move the objects to Nearline. Nearline suits reads about once a month. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Nearline suits reads about once a month.
- **B:** Incorrect for this question. Coldline suits reads a few times a year and has a longer minimum storage duration. Why the correct answer wins: Nearline suits reads about once a month.
- **C:** Incorrect for this question. Archive is the cheapest class for data kept for compliance and read almost never. Why the correct answer wins: Nearline suits reads about once a month.
- **D:** Correct. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. In this case: Nearline suits reads about once a month.

### Question 86 — C

Answer: Move the objects to Coldline. Coldline suits a few reads a year with a longer minimum duration. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: Coldline suits a few reads a year with a longer minimum duration.
- **B:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Coldline suits a few reads a year with a longer minimum duration.
- **C:** Correct. In this case: Coldline suits a few reads a year with a longer minimum duration.
- **D:** Incorrect for this question. Archive is the cheapest class for data kept for compliance and read almost never. Why the correct answer wins: Coldline suits a few reads a year with a longer minimum duration.

### Question 87 — B, E

Answers: Keep the objects in the Standard class; Enable Autoclass on the bucket. Standard serves the hot reads, and Autoclass moves each object as its access changes. Standard is for objects read frequently, where access cost matters more than storage cost. Autoclass moves each object between classes as its access pattern changes. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Archive is the cheapest class for data kept for compliance and read almost never. Why the correct answer wins: Standard serves the hot reads, and Autoclass moves each object as its access changes.
- **B:** Correct. Autoclass moves each object between classes as its access pattern changes. In this case: Standard serves the hot reads, and Autoclass moves each object as its access changes.
- **C:** Incorrect for this question. Keeping every version in the hot class pays the highest rate for data nobody reads. Why the correct answer wins: Standard serves the hot reads, and Autoclass moves each object as its access changes.
- **D:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: Standard serves the hot reads, and Autoclass moves each object as its access changes.
- **E:** Correct. Standard is for objects read frequently, where access cost matters more than storage cost. In this case: Standard serves the hot reads, and Autoclass moves each object as its access changes.

### Question 88 — A

Answer: Add a lifecycle rule that deletes objects after the retention period. A lifecycle delete rule removes the object on age. A delete rule removes the objects once the retention period passes, without a person remembering. Local study-map skill 4.6 (Lifecycle Rules and Expiration), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A delete rule removes the objects once the retention period passes, without a person remembering. In this case: A lifecycle delete rule removes the object on age.
- **B:** Incorrect for this question. Keeping every version in the hot class pays the highest rate for data nobody reads. Why the correct answer wins: A lifecycle delete rule removes the object on age.
- **C:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A lifecycle delete rule removes the object on age.
- **D:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: A lifecycle delete rule removes the object on age.

### Question 89 — C

Answer: Set a partition expiration on the table. Partition expiration drops the old partitions only. Partition expiration drops old partitions while the table keeps the recent ones. Local study-map skill 4.6 (Lifecycle Rules and Expiration), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dataset-level expiration removes tables created in it after the configured period. Why the correct answer wins: Partition expiration drops the old partitions only.
- **B:** Incorrect for this question. A delete rule removes the objects once the retention period passes, without a person remembering. Why the correct answer wins: Partition expiration drops the old partitions only.
- **C:** Correct. Partition expiration drops old partitions while the table keeps the recent ones. In this case: Partition expiration drops the old partitions only.
- **D:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: Partition expiration drops the old partitions only.

### Question 90 — D

Answer: Move the objects to Archive. Archive is the cheapest class for rarely read compliance data. Archive is the cheapest class for data kept for compliance and read almost never. Local study-map skill 4.7 (Archiving Services), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Coldline suits reads a few times a year and has a longer minimum storage duration. Why the correct answer wins: Archive is the cheapest class for rarely read compliance data.
- **B:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Archive is the cheapest class for rarely read compliance data.
- **C:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: Archive is the cheapest class for rarely read compliance data.
- **D:** Correct. Archive is the cheapest class for data kept for compliance and read almost never. In this case: Archive is the cheapest class for rarely read compliance data.

### Question 91 — C

Answer: Apply a bucket retention policy with a lock. A locked retention policy prevents deletion. Local study-map skill 4.7 (Archiving Services), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: A locked retention policy prevents deletion.
- **B:** Incorrect for this question. A delete rule removes the objects once the retention period passes, without a person remembering. Why the correct answer wins: A locked retention policy prevents deletion.
- **C:** Correct. In this case: A locked retention policy prevents deletion.
- **D:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A locked retention policy prevents deletion.

### Question 92 — A

Answer: Enable automated backups and point-in-time recovery on Cloud SQL. Point-in-time recovery restores the state before the delete. Automated backups with point-in-time recovery restore the instance to a chosen moment. Local study-map skill 4.8 (Backup and Recovery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Automated backups with point-in-time recovery restore the instance to a chosen moment. In this case: Point-in-time recovery restores the state before the delete.
- **B:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: Point-in-time recovery restores the state before the delete.
- **C:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: Point-in-time recovery restores the state before the delete.
- **D:** Incorrect for this question. A zonal instance is lost with its zone and gives no automatic failover. Why the correct answer wins: Point-in-time recovery restores the state before the delete.

### Question 93 — B, D

Answers: Restore into a scratch project on a schedule; Create a Cloud SQL read replica in another region. A restore drill proves the backup works, and the replica serves reads from another region. A restore drill is the only evidence that the backup can actually be used. A read replica serves reads from a second region and can be promoted during a regional failure. Local study-map skill 4.8 (Backup and Recovery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A restore drill proves the backup works, and the replica serves reads from another region.
- **B:** Correct. A restore drill is the only evidence that the backup can actually be used. In this case: A restore drill proves the backup works, and the replica serves reads from another region.
- **C:** Incorrect for this question. A zonal instance is lost with its zone and gives no automatic failover. Why the correct answer wins: A restore drill proves the backup works, and the replica serves reads from another region.
- **D:** Correct. A read replica serves reads from a second region and can be promoted during a regional failure. In this case: A restore drill proves the backup works, and the replica serves reads from another region.
- **E:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: A restore drill proves the backup works, and the replica serves reads from another region.

### Question 94 — A

Answer: Copy the bucket to a second region with a scheduled transfer. A scheduled transfer rebuilds the copy but leaves a gap. A scheduled copy rebuilds a second copy but leaves a gap between runs. Local study-map skill 4.9 (Replication), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A scheduled copy rebuilds a second copy but leaves a gap between runs. In this case: A scheduled transfer rebuilds the copy but leaves a gap.
- **B:** Incorrect for this question. A dual-region bucket keeps a copy in a second region and reports the replication lag. Why the correct answer wins: A scheduled transfer rebuilds the copy but leaves a gap.
- **C:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A scheduled transfer rebuilds the copy but leaves a gap.
- **D:** Incorrect for this question. A read replica serves reads from a second region and can be promoted during a regional failure. Why the correct answer wins: A scheduled transfer rebuilds the copy but leaves a gap.

### Question 95 — C

Answer: Create a multi-region bucket. A multi-region bucket spreads the objects across the geography. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. Local study-map skill 4.9 (Replication), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A multi-region bucket spreads the objects across the geography.
- **B:** Incorrect for this question. A dual-region bucket keeps a copy in a second region and reports the replication lag. Why the correct answer wins: A multi-region bucket spreads the objects across the geography.
- **C:** Correct. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. In this case: A multi-region bucket spreads the objects across the geography.
- **D:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A multi-region bucket spreads the objects across the geography.

### Question 96 — C

Answer: Deploy the instance as regional with a standby. A regional instance keeps a standby in another zone of the same region. Local study-map skill 4.10 (Primary and Secondary Locations), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A regional instance keeps a standby in another zone of the same region.
- **B:** Incorrect for this question. A zonal instance is lost with its zone and gives no automatic failover. Why the correct answer wins: A regional instance keeps a standby in another zone of the same region.
- **C:** Correct. In this case: A regional instance keeps a standby in another zone of the same region.
- **D:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: A regional instance keeps a standby in another zone of the same region.

### Question 97 — A, B

Answers: Use the Google-managed default encryption; Encrypt with a customer-managed key from Cloud KMS. Google-managed encryption needs no work, and a customer-managed key can be revoked. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. Local study-map skill 4.11 (CMEK, CSEK, and GMEK), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. In this case: Google-managed encryption needs no work, and a customer-managed key can be revoked.
- **B:** Correct. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. In this case: Google-managed encryption needs no work, and a customer-managed key can be revoked.
- **C:** Incorrect for this question. A customer-supplied key never reaches Google, and losing it loses the object. Why the correct answer wins: Google-managed encryption needs no work, and a customer-managed key can be revoked.
- **D:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: Google-managed encryption needs no work, and a customer-managed key can be revoked.
- **E:** Incorrect for this question. A key stored beside the data protects nothing against anyone who can read the store. Why the correct answer wins: Google-managed encryption needs no work, and a customer-managed key can be revoked.

### Question 98 — A

Answer: Supply a customer-supplied key with each request. A customer-supplied key is provided per request and held by the client. A customer-supplied key never reaches Google, and losing it loses the object. Local study-map skill 4.11 (CMEK, CSEK, and GMEK), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A customer-supplied key never reaches Google, and losing it loses the object. In this case: A customer-supplied key is provided per request and held by the client.
- **B:** Incorrect for this question. A key ring in the same region keeps the key and the ciphertext under the same residency rule. Why the correct answer wins: A customer-supplied key is provided per request and held by the client.
- **C:** Incorrect for this question. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. Why the correct answer wins: A customer-supplied key is provided per request and held by the client.
- **D:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: A customer-supplied key is provided per request and held by the client.

### Question 99 — D

Answer: Destroy the key version to stop access immediately. Destroying the key version makes the ciphertext unreadable for good. Destroying the key makes the ciphertext permanently unreadable, including for a restore. Local study-map skill 4.12 (Cloud KMS), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: Destroying the key version makes the ciphertext unreadable for good.
- **B:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: Destroying the key version makes the ciphertext unreadable for good.
- **C:** Incorrect for this question. A rotation schedule limits how long one key version protects new data. Why the correct answer wins: Destroying the key version makes the ciphertext unreadable for good.
- **D:** Correct. Destroying the key makes the ciphertext permanently unreadable, including for a restore. In this case: Destroying the key version makes the ciphertext unreadable for good.

### Question 100 — A

Answer: Enforce TLS for every connection to the service. Encryption in transit protects the bytes on the wire. Encryption in transit protects the bytes while they are on the wire between client and service. Local study-map skill 4.13 (Encryption in Transit and at Rest), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Encryption in transit protects the bytes while they are on the wire between client and service. In this case: Encryption in transit protects the bytes on the wire.
- **B:** Incorrect for this question. A key stored beside the data protects nothing against anyone who can read the store. Why the correct answer wins: Encryption in transit protects the bytes on the wire.
- **C:** Incorrect for this question. Encryption at rest protects the stored bytes on the medium, not the connection that reads them. Why the correct answer wins: Encryption in transit protects the bytes on the wire.
- **D:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: Encryption in transit protects the bytes on the wire.
