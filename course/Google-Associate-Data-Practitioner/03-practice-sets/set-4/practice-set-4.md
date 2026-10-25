# Google Cloud Associate Data Practitioner — Full-Length Mock Exam 4

Associate Data Practitioner · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Data Preparation and Ingestion (Ingestion, Reporting, Pipelines, and Access)

### 1. Three teams keep extracting the same table because each one reshapes it differently. What should be adopted?

- A. Query the source system in place with a federated query
- B. Extract, transform outside the warehouse, then load the result
- C. Load the raw rows, then transform them inside the warehouse
- D. Transform on the source system before the export starts

### 2. The regulator wants evidence that a field was masked before the record was stored anywhere. What should be adopted?

- A. Land the extract in a staging table before any transform runs
- B. Load the raw rows, then transform them inside the warehouse
- C. Load into a staging area, apply a light transform, then transform again in the warehouse
- D. Extract, transform outside the warehouse, then load the result

### 3. A feed needs a cheap pre-warehouse scrub and the warehouse step must be retryable alone. Which two choices fit? Select two.

- A. Load into a staging area, apply a light transform, then transform again in the warehouse
- B. Extract, transform outside the warehouse, then load the result
- C. Land the extract in a staging table before any transform runs
- D. Query the source system in place with a federated query
- E. Combine the extracts in a spreadsheet and upload the result

### 4. A quarterly reconciliation needs one look at the vendor's table without keeping a copy. What should be used?

- A. Query the source system in place with a federated query
- B. Order a Transfer Appliance
- C. Stream the rows with the BigQuery Storage Write API
- D. Build the pipeline in Dataflow

### 5. Postal codes lost their leading zeros when the column was inferred as a number. What should be added?

- A. Profile the columns to measure the null rate before loading
- B. Select every column to be safe
- C. Cast the columns to the declared types before the load
- D. Load first and fix the rejected rows afterwards

### 6. Four sources spell the same country four different ways. What should be used to standardise them?

- A. Combine the extracts in a spreadsheet and upload the result
- B. Clean and standardise with Cloud Data Fusion
- C. Load the extract into a notebook and work in pandas
- D. Load first and fix the rejected rows afterwards

### 7. Expectations must be declared and the gaps must be measured before publication. Which two actions apply? Select two.

- A. Land the data as CSV
- B. Profile the columns to measure the null rate before loading
- C. Load first and fix the rejected rows afterwards
- D. Define data quality rules and run a quality scan
- E. Select every column to be safe

### 8. A nightly transfer truncates files above four gigabytes without reporting an error. What should be compared?

- A. Compare the source checksum with the delivered file
- B. Deduplicate on the business key in the cleaning step
- C. Compare the row count with the source after every load
- D. Select every column to be safe

### 9. Thirty terabytes must leave a data centre over a link that would take months. What should be used?

- A. Order a Transfer Appliance
- B. Use Storage Transfer Service
- C. Pull the files from the partner over FTP each night
- D. Copy the objects with the gcloud storage command

### 10. A social platform's organic data must land in a warehouse table every morning. What should be used?

- A. Load the rows with a client library from the application
- B. Use Database Migration Service
- C. Use BigQuery Data Transfer Service
- D. Replicate the changes with Datastream

### 11. Objects must be mirrored from another cloud, and a source table must be tracked continuously. Which two tools apply? Select two.

- A. Use BigQuery Data Transfer Service
- B. Replicate the changes with Datastream
- C. Use Storage Transfer Service
- D. Order a Transfer Appliance
- E. Copy the objects with the gcloud storage command

### 12. An operator must move a prefix between two buckets once, during a migration window. What should be used?

- A. Load the files with the bq load command
- B. Order a Transfer Appliance
- C. Copy the objects with the gcloud storage command
- D. Pull the files from the partner over FTP each night

### 13. One landing format must serve both Spark jobs and warehouse queries efficiently. Which format fits?

- A. Land the data as newline-delimited JSON
- B. Land the data as Parquet
- C. Land the data as XML
- D. Land the data as CSV

### 14. Log lines must be appended one record at a time with nesting preserved. Which format fits?

- A. Land the data as CSV
- B. Convert the data to ORC before the load
- C. Land the data as Avro
- D. Land the data as newline-delimited JSON

### 15. A producer must append one record at a time and the reader must not rely on an external contract. Which format fits?

- A. Land the data as Avro
- B. Land the data as CSV
- C. Convert the data to ORC before the load
- D. Land the data as newline-delimited JSON

### 16. A mainframe can only export fixed-width text with no schema file. Which format is in use?

- A. Land the data as Avro
- B. Land the data as CSV
- C. Land the data as Parquet
- D. Convert the data to ORC before the load

### 17. An SFTP feed from a partner must be extracted and mapped by a team without engineers. What should be used?

- A. Run the transformation as Spark on Dataproc
- B. Document the steps and have an analyst run them each morning
- C. Run a cron job on a Compute Engine instance
- D. Build the pipeline in Cloud Data Fusion

### 18. Records must be validated and rejected before they land in the table. What should be used?

- A. Copy the objects with the gcloud storage command
- B. Build the pipeline in Dataflow
- C. Load the files with the bq load command
- D. Load the rows with a client library from the application

### 19. A dashboard must aggregate eleven billion rows over a date range. Which store fits?

- A. Store the rows in BigQuery
- B. Store the rows in Bigtable
- C. Store the files in Cloud Storage
- D. Store the documents in Firestore

### 20. A chat client must read and update one conversation document quickly. Which store fits?

- A. Store the records in Cloud SQL
- B. Store the rows in Bigtable
- C. Store the records in Spanner
- D. Store the documents in Firestore

### 21. A device fleet needs millions of writes a second keyed by device, and the raw payloads must be archived. Which two stores apply? Select two.

- A. Store the records in Spanner
- B. Store the documents in Firestore
- C. Store the files in Cloud Storage
- D. Store the rows in BigQuery
- E. Store the rows in Bigtable

### 22. The regulator names the primary country and the failover country. Which location type fits?

- A. Choose a dual-region location
- B. Choose a zonal resource
- C. Choose a multi-region location
- D. Choose a regional location

### 23. A residency rule constrains the country, and latency then decides the city. Which two considerations apply? Select two.

- A. Choose a regional location
- B. Choose a zonal resource
- C. Place the data in the region the regulator names
- D. Place the data in the region nearest the largest user base
- E. Choose a multi-region location

### 24. A CSV arrives with a declared header and typed columns. How should it be classified?

- A. Apply a schema on read at query time
- B. Treat the records as semi-structured data
- C. Treat the records as structured data
- D. Treat the files as unstructured data

### 25. A folder holds audio recordings with no accompanying field model. How should they be classified?

- A. Treat the files as unstructured data
- B. Treat the records as structured data
- C. Treat the records as semi-structured data
- D. Apply a schema on read at query time

### 26. A Go service must insert rows it has already assembled in memory. What should be used?

- A. Load the files with the bq load command
- B. Stream the rows with the BigQuery Storage Write API
- C. Load the rows with a client library from the application
- D. Copy the objects with the gcloud storage command

### 27. A generated Avro file must become rows in a partitioned table. What should be used?

- A. Load the files with the bq load command
- B. Use Storage Transfer Service
- C. Copy the objects with the gcloud storage command
- D. Load the rows with a client library from the application

### 28. A source system emits files with inconsistent encodings that must be repaired before landing. What should be used?

- A. Build the pipeline in Dataflow
- B. Load the files with the bq load command
- C. Copy the objects with the gcloud storage command
- D. Load the rows with a client library from the application

### 29. A media archive must hold files up to five terabytes each at low cost. Which store fits?

- A. Store the rows in BigQuery
- B. Store the files in Cloud Storage
- C. Store the records in Spanner
- D. Store the rows in Bigtable

### 30. A development dataset is used from one city and cost is the only concern. Which location type fits?

- A. Choose a regional location
- B. Choose a zonal resource
- C. Choose a multi-region location
- D. Choose a dual-region location

---

## Domain 2 — Data Analysis and Presentation (Files, Formats, Dashboards, and Governance)

### 31. Analysts must read a curated subset and never see the identity columns. What should be used?

- A. Query the files through an external table
- B. Load the files into a native table
- C. Create a BigQuery materialized view
- D. Create a BigQuery view over the join

### 32. A dashboard recomputes an expensive join every few minutes with the same result. What should be used?

- A. Create a BigQuery view over the join
- B. Create a BigQuery materialized view
- C. Load the files into a native table
- D. Write a SQL query in BigQuery and save the result

### 33. A report filters one date range and the rows still sit in external files. Which two changes shrink the scan? Select two.

- A. Filter the query on the partition column
- B. Query the files through an external table
- C. Turn off the result cache to force a fresh read
- D. Select every column to be safe
- E. Load the files into a native table

### 34. Each analyst asks the same question with a different date range. What should be produced?

- A. Export the query result to a spreadsheet for the business team
- B. Write a SQL query in BigQuery and save the result
- C. Share the dashboard with a scheduled delivery
- D. Turn off the result cache to force a fresh read

### 35. Notebooks must run in the project with no virtual machine for the team to patch. What should be used?

- A. Keep the dataset on the analyst workstation
- B. Analyse the data in a Colab Enterprise notebook
- C. Upload a CSV extract into the notebook and analyse it there
- D. Load the extract into a notebook and work in pandas

### 36. A notebook must plot a warehouse query without an export step. What should be used?

- A. Upload a CSV extract into the notebook and analyse it there
- B. Load the extract into a notebook and work in pandas
- C. Export the query result to a spreadsheet for the business team
- D. Query BigQuery from the notebook with the %%bigquery magic

### 37. A manager asks which region explains the drop in renewals. What should be produced?

- A. Build a Looker Studio report
- B. Share the dashboard with a scheduled delivery
- C. Document the steps and have an analyst run them each morning
- D. Write a SQL query in BigQuery and save the result

### 38. The same answer is requested by email every Monday morning. What should be configured?

- A. Document the steps and have an analyst run them each morning
- B. Share the dashboard with a scheduled delivery
- C. Turn off the result cache to force a fresh read
- D. Export the query result to a spreadsheet for the business team

### 39. Every tile must inherit the same certified definition of churn. What should be used?

- A. Build a governed Looker dashboard
- B. Export the query result to a spreadsheet for the business team
- C. Select every column to be safe
- D. Build a Looker Studio report

### 40. A new dashboard must reuse the certified definition and reach people who never sign in. Which two components apply? Select two.

- A. Turn off the result cache to force a fresh read
- B. Select every column to be safe
- C. Build a Looker Studio report
- D. Share the dashboard with a scheduled delivery
- E. Add a LookML measure for the calculation

### 41. Two dashboard authors produced different churn numbers from the same table. What should be added?

- A. Change the LookML parameter in the view
- B. Turn off the result cache to force a fresh read
- C. Add a LookML measure for the calculation
- D. Export the query result to a spreadsheet for the business team

### 42. A two-person team needs a chart over one sheet this afternoon. What should be used?

- A. Add a LookML measure for the calculation
- B. Build a governed Looker dashboard
- C. Build a Looker Studio report
- D. Orchestrate the steps in Cloud Composer

### 43. Certified metrics and row-level security must hold across every report. What should be used?

- A. Share the dashboard with a scheduled delivery
- B. Build a Looker Studio report
- C. Build a governed Looker dashboard
- D. Export the query result to a spreadsheet for the business team

### 44. The organisation moved its fiscal year and every report must follow. What should be changed?

- A. Expose the table through a LookML explore
- B. Add a LookML measure for the calculation
- C. Change the LookML parameter in the view
- D. Turn off the result cache to force a fresh read

### 45. Model-wide control is needed over both the calendar and which joins authors may use. Which two LookML objects apply? Select two.

- A. Turn off the result cache to force a fresh read
- B. Expose the table through a LookML explore
- C. Add a LookML measure for the calculation
- D. Change the LookML parameter in the view
- E. Export the query result to a spreadsheet for the business team

### 46. One business question needs a join that must stay hidden from other authors. What should be added?

- A. Expose the table through a LookML explore
- B. Turn off the result cache to force a fresh read
- C. Write a SQL query in BigQuery and save the result
- D. Add a LookML measure for the calculation

### 47. A lab has labelled spectra and no one to write a training loop. What should be used?

- A. Score the rows with ML.PREDICT
- B. Train an AutoML tabular model
- C. Land the data as Parquet
- D. Train a BigQuery ML linear regression model

### 48. A wide table hides interactions, and a yes-or-no outcome must come back as a probability. Which two model types apply? Select two.

- A. Train an AutoML tabular model
- B. Train a BigQuery ML logistic regression model
- C. Train a BigQuery ML ARIMA_PLUS model
- D. Train a BigQuery ML boosted tree model
- E. Train a BigQuery ML k-means model

### 49. A single series has four years of hourly history and almost no covariates. Which model type fits?

- A. Train a BigQuery ML k-means model
- B. Train a BigQuery ML linear regression model
- C. Train a BigQuery ML ARIMA_PLUS model
- D. Train a BigQuery ML logistic regression model

### 50. Emails must be classified per row while the text remains under warehouse governance. What should be used?

- A. Create a BigQuery remote model over a Gemini model
- B. Fine-tune a Gemini model from the warehouse rows
- C. Load the extract into a notebook and work in pandas
- D. Land the data as newline-delimited JSON

### 51. A remote model cannot be created until an identity exists for the endpoint call. What should be created?

- A. Issue a signed URL with a short expiry
- B. Create the BigQuery connection that reaches the model endpoint
- C. Copy the objects with the gcloud storage command
- D. Load the files with the bq load command

### 52. Two teams disagree about success and neither has defined an acceptance test. What should be agreed first?

- A. Run a cron job on a Compute Engine instance
- B. Plan collection, training, evaluation, then prediction
- C. Document the steps and have an analyst run them each morning
- D. Ship the model once the training loss looks good

### 53. One large customer appears on both sides of the evaluation and inflates the score. What should be done?

- A. Hold the most recent period out as the test set
- B. Ship the model once the training loss looks good
- C. Hold out a labelled split before training
- D. Hold out whole entities so none spans both splits

### 54. The evaluation must be produced as SQL output for an audit pack. What should be used?

- A. Generate the forecast with ML.FORECAST
- B. Explain the prediction with ML.EXPLAIN_PREDICT
- C. Score the rows with ML.PREDICT
- D. Evaluate the model with ML.EVALUATE

### 55. A flag with two outcomes must be predicted from warehouse rows. Which model type fits?

- A. Land the data as Parquet
- B. Train a BigQuery ML linear regression model
- C. Train a BigQuery ML logistic regression model
- D. Train a BigQuery ML k-means model

### 56. A marketing list must be scored and written to a table overnight. What should be used?

- A. Evaluate the model with ML.EVALUATE
- B. Generate the forecast with ML.FORECAST
- C. Explain the prediction with ML.EXPLAIN_PREDICT
- D. Score the rows with ML.PREDICT

### 57. Two versions must be distinguishable before either is promoted. What should be done?

- A. Register the model version in Model Registry
- B. Export the query result to a spreadsheet for the business team
- C. Keep the dataset on the analyst workstation
- D. Stream the rows with the BigQuery Storage Write API

---

## Domain 3 — Data Pipeline Orchestration (Streaming, Scheduling, Modelling, and Recovery)

### 58. Dependent SQL models must rebuild in order after a schema change. What should be used?

- A. Run a cron job on a Compute Engine instance
- B. Run the transformation as Spark on Dataproc
- C. Build the pipeline in Cloud Data Fusion
- D. Manage the SQL transformations in Dataform

### 59. A Java Spark job must run over six terabytes of Avro. What should be used?

- A. Run the handler as a Cloud Functions function
- B. Sequence the API calls with Workflows
- C. Run the transformation as Spark on Dataproc
- D. Build the pipeline in Dataflow

### 60. A streaming path needs one definition and the SQL models need version control. Which two tools apply? Select two.

- A. Trigger the job from Cloud Scheduler
- B. Build the pipeline in Dataflow
- C. Run the handler as a Cloud Functions function
- D. Document the steps and have an analyst run them each morning
- E. Manage the SQL transformations in Dataform

### 61. A team without engineers must join eight sources on a canvas. What should be used?

- A. Run the transformation as Spark on Dataproc
- B. Build the pipeline in Cloud Data Fusion
- C. Sequence the API calls with Workflows
- D. Manage the SQL transformations in Dataform

### 62. The warehouse engine should take the heavy join off the source system. Which design fits?

- A. Load the raw rows, then transform them inside the warehouse
- B. Query the source system in place with a federated query
- C. Transform on the source system before the export starts
- D. Extract, transform outside the warehouse, then load the result

### 63. The destination rejects anything that has not already been cleansed. Which design fits?

- A. Load the raw rows, then transform them inside the warehouse
- B. Load the rows with a client library from the application
- C. Land the extract in a staging table before any transform runs
- D. Extract, transform outside the warehouse, then load the result

### 64. A nightly aggregate must run inside the warehouse with no operator. What should be used?

- A. Submit the job through a Dataproc workflow template
- B. Trigger the job from Cloud Scheduler
- C. Sequence the API calls with Workflows
- D. Schedule the SQL with a BigQuery scheduled query

### 65. The nightly aggregate must run unattended and alert an owner when it fails. Which two components apply? Select two.

- A. Document the steps and have an analyst run them each morning
- B. Create a Cloud Monitoring alert policy on the job metric
- C. Trigger the job from Cloud Scheduler
- D. Run a cron job on a Compute Engine instance
- E. Schedule the SQL with a BigQuery scheduled query

### 66. A Cloud Run endpoint must be called at 06:00 on weekdays. What should be used?

- A. Start the pipeline from an Eventarc trigger
- B. Trigger the job from Cloud Scheduler
- C. Schedule the SQL with a BigQuery scheduled query
- D. Orchestrate the steps in Cloud Composer

### 67. A single step lags while the others are idle, and the watermark is stuck. Where should the team look?

- A. Write a SQL query in BigQuery and save the result
- B. Turn off the result cache to force a fresh read
- C. Watch the job graph and per-step throughput in the Dataflow console
- D. Query the job logs in Logs Explorer

### 68. Two per cent of events fail validation and must be replayable later. What should be added?

- A. Write the rejected rows to a dead-letter table
- B. Denormalise the tables into one wide table
- C. Load first and fix the rejected rows afterwards
- D. Select every column to be safe

### 69. One worker keeps restarting and the reason is only in its logs. Where should the team look?

- A. Query the job logs in Logs Explorer
- B. Write a SQL query in BigQuery and save the result
- C. Document the steps and have an analyst run them each morning
- D. Share the dashboard with a scheduled delivery

### 70. The team learns about failures from the people waiting for the report. What should be added?

- A. Query the job logs in Logs Explorer
- B. Turn off the result cache to force a fresh read
- C. Create a Cloud Monitoring alert policy on the job metric
- D. Document the steps and have an analyst run them each morning

### 71. A four-step graph must survive a partner delay with retries and an SLA. What should orchestrate it?

- A. Orchestrate the steps in Cloud Composer
- B. Run the handler as a Cloud Functions function
- C. Schedule the SQL with a BigQuery scheduled query
- D. Sequence the API calls with Workflows

### 72. An object landing must start a chain of two API calls with no server to operate. Which two components apply? Select two.

- A. Schedule the SQL with a BigQuery scheduled query
- B. Run the handler as a Cloud Functions function
- C. Run a cron job on a Compute Engine instance
- D. Start the pipeline from an Eventarc trigger
- E. Sequence the API calls with Workflows

### 73. Two APIs must be called in order with no server to operate. What should be used?

- A. Run the handler as a Cloud Functions function
- B. Sequence the API calls with Workflows
- C. Orchestrate the steps in Cloud Composer
- D. Run a cron job on a Compute Engine instance

### 74. Readings must appear in a table within seconds of publication with no subscriber to run. What should be used?

- A. Subscribe BigQuery to the Pub/Sub topic
- B. Schedule the SQL with a BigQuery scheduled query
- C. Start the pipeline from an Eventarc trigger
- D. Load the files with the bq load command

### 75. A landing file must start a Composer DAG immediately. What should be used?

- A. Subscribe BigQuery to the Pub/Sub topic
- B. Schedule the SQL with a BigQuery scheduled query
- C. Start the pipeline from an Eventarc trigger
- D. Trigger the job from Cloud Scheduler

---

## Domain 4 — Data Management (Warehouse Analytics, Orchestration, and Key Management)

### 76. A support team must read one table and nothing else in the project. What should be granted?

- A. Make the bucket public so the partner can read it
- B. Grant the basic Owner role to the team
- C. Grant the role to the whole domain
- D. Grant the predefined role that matches the task

### 77. The grant must omit one permission, and no individual should be the principal. Which two controls apply? Select two.

- A. Run the job as a dedicated service account
- B. Create a custom role with only the permissions used
- C. Grant the basic Owner role to the team
- D. Grant the role to the whole domain
- E. Add the project to a VPC Service Controls perimeter

### 78. A pipeline must run without borrowing an employee's identity. What should be used?

- A. Grant the basic Owner role to the team
- B. Issue a signed URL with a short expiry
- C. Grant the role to the whole domain
- D. Run the job as a dedicated service account

### 79. A job function is already covered by a role Google maintains. What should be granted?

- A. Grant the basic Owner role to the team
- B. Make the bucket public so the partner can read it
- C. Assign a predefined role to the group
- D. Create a custom role with only the permissions used

### 80. The auditor requires one permission to be withheld from an otherwise matching role. What should be created?

- A. Grant the basic Owner role to the team
- B. Grant the role to the whole domain
- C. Create a custom role with only the permissions used
- D. Assign a predefined role to the group

### 81. Object access must be reviewable from IAM alone. What should be enabled?

- A. Enable uniform bucket-level access
- B. Issue a signed URL with a short expiry
- C. Manage per-object ACLs on the bucket
- D. Make the bucket public so the partner can read it

### 82. A contractor needs one object for two hours with no IAM change. What should be issued?

- A. Export the table to a bucket the partner owns
- B. Issue a signed URL with a short expiry
- C. Make the bucket public so the partner can read it
- D. Enable uniform bucket-level access

### 83. Subscribers must read a curated dataset in place and stay current. What should be used?

- A. Export the table to a bucket the partner owns
- B. Make the bucket public so the partner can read it
- C. Issue a signed URL with a short expiry
- D. Publish the dataset through Analytics Hub

### 84. Data must not leave the boundary even when an authorised identity asks for it. What should be applied?

- A. Make the bucket public so the partner can read it
- B. Publish the dataset through Analytics Hub
- C. Issue a signed URL with a short expiry
- D. Add the project to a VPC Service Controls perimeter

### 85. Reference data is read about monthly and kept for two years. Which class fits?

- A. Move the objects to Coldline
- B. Move the objects to Nearline
- C. Move the objects to Archive
- D. Keep the objects in the Standard class

### 86. Objects move between hot and cold without warning, and the bill must fall anyway. Which two options apply? Select two.

- A. Move the objects to Coldline
- B. Add a lifecycle rule that changes the storage class
- C. Keep every version in the Standard class forever
- D. Leave the objects in place and review them next year
- E. Enable Autoclass on the bucket

### 87. A storefront reads its product images constantly. Which class fits?

- A. Enable Autoclass on the bucket
- B. Move the objects to Archive
- C. Move the objects to Nearline
- D. Keep the objects in the Standard class

### 88. Scratch exports must be removed after seven days. What should be added?

- A. Keep every version in the Standard class forever
- B. Leave the objects in place and review them next year
- C. Enable object versioning on the bucket
- D. Add a lifecycle rule that deletes objects after the retention period

### 89. Analysts create a table per experiment and never delete them, so the dataset must clean up after itself. What should be set?

- A. Set a table expiration on the dataset
- B. Leave the objects in place and review them next year
- C. Add a lifecycle rule that deletes objects after the retention period
- D. Set a partition expiration on the table

### 90. Raw firewall logs are opened only when an incident is audited, once or twice a year. Which class fits?

- A. Keep the objects in the Standard class
- B. Move the objects to Nearline
- C. Move the objects to Archive
- D. Move the objects to Coldline

### 91. Deletion must be impossible for the statutory period. What should be applied?

- A. Leave the objects in place and review them next year
- B. Enable object versioning on the bucket
- C. Apply a bucket retention policy with a lock
- D. Add a lifecycle rule that deletes objects after the retention period

### 92. A bad migration corrupted rows an hour ago. What should be used?

- A. Rely on the disk snapshot the platform keeps
- B. Enable automated backups and point-in-time recovery on Cloud SQL
- C. Deploy a single zonal instance to keep the cost down
- D. Copy the bucket to a second region with a scheduled transfer

### 93. Two measures together prove the database can be returned to an earlier moment. Which two apply? Select two.

- A. Deploy a single zonal instance to keep the cost down
- B. Rely on the disk snapshot the platform keeps
- C. Create a multi-region bucket
- D. Enable automated backups and point-in-time recovery on Cloud SQL
- E. Restore into a scratch project on a schedule

### 94. Two named regions must hold the objects with a visible replication lag. What should be used?

- A. Enable object versioning on the bucket
- B. Create a dual-region bucket with a replication policy
- C. Create a multi-region bucket
- D. Copy the bucket to a second region with a scheduled transfer

### 95. Read traffic must be served from a second region while the primary stays writable. What should be used?

- A. Copy the bucket to a second region with a scheduled transfer
- B. Enable object versioning on the bucket
- C. Create a Cloud SQL read replica in another region
- D. Create a dual-region bucket with a replication policy

### 96. A development sandbox may be lost with its failure domain. Which location type fits?

- A. Choose a dual-region location
- B. Choose a zonal resource
- C. Deploy the instance as regional with a standby
- D. Choose a regional location

### 97. The customer must revoke access to the data by controlling the key. Which key model applies?

- A. Put the key in the application configuration file
- B. Supply a customer-supplied key with each request
- C. Use the Google-managed default encryption
- D. Encrypt with a customer-managed key from Cloud KMS

### 98. Two models leave the customer with no rotation control of their own. Which two apply? Select two.

- A. Use the Google-managed default encryption
- B. Put the key in the application configuration file
- C. Encrypt with a customer-managed key from Cloud KMS
- D. Encrypt in the client and store the key next to the data
- E. Supply a customer-supplied key with each request

### 99. Keys for two environments must be provably separate and listed in one governed place. What should be configured?

- A. Put the key in the application configuration file
- B. Use the Google-managed default encryption
- C. Set a rotation schedule on the key
- D. Create the key in a Cloud KMS key ring in the data region

### 100. An auditor asks how the bytes are protected on the medium after the read ends. What should be confirmed?

- A. Encrypt in the client and store the key next to the data
- B. Confirm the data is encrypted at rest by the storage service
- C. Enforce TLS for every connection to the service
- D. Put the key in the application configuration file

---

## Answer key and explanations

### Question 1 — C

Answer: Load the raw rows, then transform them inside the warehouse. ELT extracts once and every team reshapes the raw copy in the warehouse. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ELT extracts once and every team reshapes the raw copy in the warehouse.
- **B:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT extracts once and every team reshapes the raw copy in the warehouse.
- **C:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT extracts once and every team reshapes the raw copy in the warehouse.
- **D:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ELT extracts once and every team reshapes the raw copy in the warehouse.

### Question 2 — D

Answer: Extract, transform outside the warehouse, then load the result. ETL masks the record before the warehouse write, which is what the evidence requires. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A staging table separates a failed load from a failed transform, so each can be retried on its own. Why the correct answer wins: ETL masks the record before the warehouse write, which is what the evidence requires.
- **B:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETL masks the record before the warehouse write, which is what the evidence requires.
- **C:** Incorrect for this question. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. Why the correct answer wins: ETL masks the record before the warehouse write, which is what the evidence requires.
- **D:** Correct. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. In this case: ETL masks the record before the warehouse write, which is what the evidence requires.

### Question 3 — A, C

Answers: Load into a staging area, apply a light transform, then transform again in the warehouse; Land the extract in a staging table before any transform runs. ETLT performs the early scrub, and a staging table keeps the retry of the warehouse step independent. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. A staging table separates a failed load from a failed transform, so each can be retried on its own. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. In this case: ETLT performs the early scrub, and a staging table keeps the retry of the warehouse step independent.
- **B:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ETLT performs the early scrub, and a staging table keeps the retry of the warehouse step independent.
- **C:** Correct. A staging table separates a failed load from a failed transform, so each can be retried on its own. In this case: ETLT performs the early scrub, and a staging table keeps the retry of the warehouse step independent.
- **D:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ETLT performs the early scrub, and a staging table keeps the retry of the warehouse step independent.
- **E:** Incorrect for this question. A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run. Why the correct answer wins: ETLT performs the early scrub, and a staging table keeps the retry of the warehouse step independent.

### Question 4 — A

Answer: Query the source system in place with a federated query. A federated query reads the vendor table once and stores nothing. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. In this case: A federated query reads the vendor table once and stores nothing.
- **B:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: A federated query reads the vendor table once and stores nothing.
- **C:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: A federated query reads the vendor table once and stores nothing.
- **D:** Incorrect for this question. Dataflow runs the same code for streaming and batch and scales the workers with the load. Why the correct answer wins: A federated query reads the vendor table once and stores nothing.

### Question 5 — C

Answer: Cast the columns to the declared types before the load. An explicit cast to the declared type keeps the value as text. An explicit cast turns a silent type drift into a visible failure at load time. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A profile quantifies what is missing before the gaps reach a dashboard. Why the correct answer wins: An explicit cast to the declared type keeps the value as text.
- **B:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: An explicit cast to the declared type keeps the value as text.
- **C:** Correct. An explicit cast turns a silent type drift into a visible failure at load time. In this case: An explicit cast to the declared type keeps the value as text.
- **D:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: An explicit cast to the declared type keeps the value as text.

### Question 6 — B

Answer: Clean and standardise with Cloud Data Fusion. A Data Fusion pipeline holds the standardisation in one versioned definition. A Data Fusion pipeline expresses the cleanup visually and keeps the steps in one versioned definition. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run. Why the correct answer wins: A Data Fusion pipeline holds the standardisation in one versioned definition.
- **B:** Correct. A Data Fusion pipeline expresses the cleanup visually and keeps the steps in one versioned definition. In this case: A Data Fusion pipeline holds the standardisation in one versioned definition.
- **C:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: A Data Fusion pipeline holds the standardisation in one versioned definition.
- **D:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A Data Fusion pipeline holds the standardisation in one versioned definition.

### Question 7 — B, D

Answers: Define data quality rules and run a quality scan; Profile the columns to measure the null rate before loading. Declared rules turn the expectations into tests, and a profile measures what is missing. Declared rules turn a judgement about the data into a test that runs on every load. A profile quantifies what is missing before the gaps reach a dashboard. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Declared rules turn the expectations into tests, and a profile measures what is missing.
- **B:** Correct. A profile quantifies what is missing before the gaps reach a dashboard. In this case: Declared rules turn the expectations into tests, and a profile measures what is missing.
- **C:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: Declared rules turn the expectations into tests, and a profile measures what is missing.
- **D:** Correct. Declared rules turn a judgement about the data into a test that runs on every load. In this case: Declared rules turn the expectations into tests, and a profile measures what is missing.
- **E:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: Declared rules turn the expectations into tests, and a profile measures what is missing.

### Question 8 — A

Answer: Compare the source checksum with the delivered file. A checksum proves the bytes arrived unchanged. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A checksum proves the bytes arrived unchanged.
- **B:** Incorrect for this question. Retries and restatements create duplicate rows unless the load deduplicates on a stable key. Why the correct answer wins: A checksum proves the bytes arrived unchanged.
- **C:** Incorrect for this question. A row-count reconciliation catches a truncated or duplicated extract. Why the correct answer wins: A checksum proves the bytes arrived unchanged.
- **D:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A checksum proves the bytes arrived unchanged.

### Question 9 — A

Answer: Order a Transfer Appliance. A Transfer Appliance moves the volume physically. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. In this case: A Transfer Appliance moves the volume physically.
- **B:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: A Transfer Appliance moves the volume physically.
- **C:** Incorrect for this question. A hand-built FTP pull has no retry, no manifest, and no record of what arrived. Why the correct answer wins: A Transfer Appliance moves the volume physically.
- **D:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A Transfer Appliance moves the volume physically.

### Question 10 — C

Answer: Use BigQuery Data Transfer Service. BigQuery Data Transfer Service schedules the recurring load. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: BigQuery Data Transfer Service schedules the recurring load.
- **B:** Incorrect for this question. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. Why the correct answer wins: BigQuery Data Transfer Service schedules the recurring load.
- **C:** Correct. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. In this case: BigQuery Data Transfer Service schedules the recurring load.
- **D:** Incorrect for this question. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Why the correct answer wins: BigQuery Data Transfer Service schedules the recurring load.

### Question 11 — B, C

Answers: Use Storage Transfer Service; Replicate the changes with Datastream. Storage Transfer Service mirrors the objects, and Datastream tracks the row changes. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Why the correct answer wins: Storage Transfer Service mirrors the objects, and Datastream tracks the row changes.
- **B:** Correct. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. In this case: Storage Transfer Service mirrors the objects, and Datastream tracks the row changes.
- **C:** Correct. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. In this case: Storage Transfer Service mirrors the objects, and Datastream tracks the row changes.
- **D:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: Storage Transfer Service mirrors the objects, and Datastream tracks the row changes.
- **E:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: Storage Transfer Service mirrors the objects, and Datastream tracks the row changes.

### Question 12 — C

Answer: Copy the objects with the gcloud storage command. A gcloud storage copy is the direct path for a one-off move. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A gcloud storage copy is the direct path for a one-off move.
- **B:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: A gcloud storage copy is the direct path for a one-off move.
- **C:** Correct. In this case: A gcloud storage copy is the direct path for a one-off move.
- **D:** Incorrect for this question. A hand-built FTP pull has no retry, no manifest, and no record of what arrived. Why the correct answer wins: A gcloud storage copy is the direct path for a one-off move.

### Question 13 — B

Answer: Land the data as Parquet. Parquet is columnar and readable by both Spark and the warehouse. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: Parquet is columnar and readable by both Spark and the warehouse.
- **B:** Correct. Parquet is columnar and compressed, so a scan reads only the columns a query needs. In this case: Parquet is columnar and readable by both Spark and the warehouse.
- **C:** Incorrect for this question. XML nests well and is verbose, which makes it a poor fit for wide analytical scans. Why the correct answer wins: Parquet is columnar and readable by both Spark and the warehouse.
- **D:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Parquet is columnar and readable by both Spark and the warehouse.

### Question 14 — D

Answer: Land the data as newline-delimited JSON. Newline-delimited JSON appends record by record and keeps the nesting. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Newline-delimited JSON appends record by record and keeps the nesting.
- **B:** Incorrect for this question. ORC is another columnar format; choosing it adds a conversion step without a benefit over Parquet here. Why the correct answer wins: Newline-delimited JSON appends record by record and keeps the nesting.
- **C:** Incorrect for this question. Avro carries its schema with the records and suits row-oriented streaming exchanges. Why the correct answer wins: Newline-delimited JSON appends record by record and keeps the nesting.
- **D:** Correct. Newline-delimited JSON keeps nested fields and can be appended one record at a time. In this case: Newline-delimited JSON appends record by record and keeps the nesting.

### Question 15 — A

Answer: Land the data as Avro. Avro embeds the schema with each record, so the reader needs no separate contract. Avro carries its schema with the records and suits row-oriented streaming exchanges. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Avro carries its schema with the records and suits row-oriented streaming exchanges. In this case: Avro embeds the schema with each record, so the reader needs no separate contract.
- **B:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Avro embeds the schema with each record, so the reader needs no separate contract.
- **C:** Incorrect for this question. ORC is another columnar format; choosing it adds a conversion step without a benefit over Parquet here. Why the correct answer wins: Avro embeds the schema with each record, so the reader needs no separate contract.
- **D:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: Avro embeds the schema with each record, so the reader needs no separate contract.

### Question 16 — B

Answer: Land the data as CSV. CSV carries text with no types and no schema. CSV is readable everywhere and carries no types, no schema, and no nesting. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Avro carries its schema with the records and suits row-oriented streaming exchanges. Why the correct answer wins: CSV carries text with no types and no schema.
- **B:** Correct. CSV is readable everywhere and carries no types, no schema, and no nesting. In this case: CSV carries text with no types and no schema.
- **C:** Incorrect for this question. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Why the correct answer wins: CSV carries text with no types and no schema.
- **D:** Incorrect for this question. ORC is another columnar format; choosing it adds a conversion step without a benefit over Parquet here. Why the correct answer wins: CSV carries text with no types and no schema.

### Question 17 — D

Answer: Build the pipeline in Cloud Data Fusion. Data Fusion expresses the extract and the mapping on a canvas. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Data Fusion expresses the extract and the mapping on a canvas.
- **B:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Data Fusion expresses the extract and the mapping on a canvas.
- **C:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Data Fusion expresses the extract and the mapping on a canvas.
- **D:** Correct. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. In this case: Data Fusion expresses the extract and the mapping on a canvas.

### Question 18 — B

Answer: Build the pipeline in Dataflow. A Dataflow pipeline validates each record before the write. Dataflow runs the same code for streaming and batch and scales the workers with the load. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A Dataflow pipeline validates each record before the write.
- **B:** Correct. Dataflow runs the same code for streaming and batch and scales the workers with the load. In this case: A Dataflow pipeline validates each record before the write.
- **C:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A Dataflow pipeline validates each record before the write.
- **D:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: A Dataflow pipeline validates each record before the write.

### Question 19 — A

Answer: Store the rows in BigQuery. BigQuery scans columnar tables at warehouse scale. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. In this case: BigQuery scans columnar tables at warehouse scale.
- **B:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: BigQuery scans columnar tables at warehouse scale.
- **C:** Incorrect for this question. Cloud Storage holds objects of any shape and is the landing zone every other service can read. Why the correct answer wins: BigQuery scans columnar tables at warehouse scale.
- **D:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: BigQuery scans columnar tables at warehouse scale.

### Question 20 — D

Answer: Store the documents in Firestore. Firestore serves document reads and writes by key for an application. Firestore is a document store for application reads by key with a flexible shape. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Why the correct answer wins: Firestore serves document reads and writes by key for an application.
- **B:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: Firestore serves document reads and writes by key for an application.
- **C:** Incorrect for this question. Spanner gives strongly consistent relational transactions across regions at global scale. Why the correct answer wins: Firestore serves document reads and writes by key for an application.
- **D:** Correct. Firestore is a document store for application reads by key with a flexible shape. In this case: Firestore serves document reads and writes by key for an application.

### Question 21 — C, E

Answers: Store the rows in Bigtable; Store the files in Cloud Storage. Bigtable absorbs the keyed writes, and Cloud Storage holds the payloads. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Cloud Storage holds objects of any shape and is the landing zone every other service can read. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Spanner gives strongly consistent relational transactions across regions at global scale. Why the correct answer wins: Bigtable absorbs the keyed writes, and Cloud Storage holds the payloads.
- **B:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: Bigtable absorbs the keyed writes, and Cloud Storage holds the payloads.
- **C:** Correct. Cloud Storage holds objects of any shape and is the landing zone every other service can read. In this case: Bigtable absorbs the keyed writes, and Cloud Storage holds the payloads.
- **D:** Incorrect for this question. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Why the correct answer wins: Bigtable absorbs the keyed writes, and Cloud Storage holds the payloads.
- **E:** Correct. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. In this case: Bigtable absorbs the keyed writes, and Cloud Storage holds the payloads.

### Question 22 — A

Answer: Choose a dual-region location. A dual-region location names both places explicitly. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. In this case: A dual-region location names both places explicitly.
- **B:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: A dual-region location names both places explicitly.
- **C:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: A dual-region location names both places explicitly.
- **D:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: A dual-region location names both places explicitly.

### Question 23 — C, D

Answers: Place the data in the region the regulator names; Place the data in the region nearest the largest user base. Residency fixes the country, and the user base decides the city inside it. A residency obligation fixes the geography, which removes the choice from the performance discussion. Distance between the data and the readers shows up as latency on every query. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: Residency fixes the country, and the user base decides the city inside it.
- **B:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: Residency fixes the country, and the user base decides the city inside it.
- **C:** Correct. A residency obligation fixes the geography, which removes the choice from the performance discussion. In this case: Residency fixes the country, and the user base decides the city inside it.
- **D:** Correct. Distance between the data and the readers shows up as latency on every query. In this case: Residency fixes the country, and the user base decides the city inside it.
- **E:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: Residency fixes the country, and the user base decides the city inside it.

### Question 24 — C

Answer: Treat the records as structured data. Declared columns with types are structured data. Structured data fits a declared schema of rows and columns. Local study-map skill 1.8 (Structured, Semi-Structured, and Unstructured Data), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Why the correct answer wins: Declared columns with types are structured data.
- **B:** Incorrect for this question. Semi-structured data has a flexible shape such as JSON, where fields vary between records. Why the correct answer wins: Declared columns with types are structured data.
- **C:** Correct. Structured data fits a declared schema of rows and columns. In this case: Declared columns with types are structured data.
- **D:** Incorrect for this question. Unstructured data has no field model at all, such as images, audio, or free documents. Why the correct answer wins: Declared columns with types are structured data.

### Question 25 — A

Answer: Treat the files as unstructured data. Audio has no field model, which makes it unstructured. Unstructured data has no field model at all, such as images, audio, or free documents. Local study-map skill 1.8 (Structured, Semi-Structured, and Unstructured Data), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Unstructured data has no field model at all, such as images, audio, or free documents. In this case: Audio has no field model, which makes it unstructured.
- **B:** Incorrect for this question. Structured data fits a declared schema of rows and columns. Why the correct answer wins: Audio has no field model, which makes it unstructured.
- **C:** Incorrect for this question. Semi-structured data has a flexible shape such as JSON, where fields vary between records. Why the correct answer wins: Audio has no field model, which makes it unstructured.
- **D:** Incorrect for this question. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Why the correct answer wins: Audio has no field model, which makes it unstructured.

### Question 26 — C

Answer: Load the rows with a client library from the application. A client library writes rows the service already holds. A client library suits an application that already holds the rows in memory rather than files in a bucket. Local study-map skill 1.9 (Loading with CLIs and Client Libraries), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A client library writes rows the service already holds.
- **B:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: A client library writes rows the service already holds.
- **C:** Correct. A client library suits an application that already holds the rows in memory rather than files in a bucket. In this case: A client library writes rows the service already holds.
- **D:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A client library writes rows the service already holds.

### Question 27 — A

Answer: Load the files with the bq load command. A load job reads the file and writes the partitioned table. The bq load command creates a load job that reads files from Cloud Storage into a table. Local study-map skill 1.9 (Loading with CLIs and Client Libraries), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. The bq load command creates a load job that reads files from Cloud Storage into a table. In this case: A load job reads the file and writes the partitioned table.
- **B:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: A load job reads the file and writes the partitioned table.
- **C:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A load job reads the file and writes the partitioned table.
- **D:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: A load job reads the file and writes the partitioned table.

### Question 28 — A

Answer: Build the pipeline in Dataflow. A Dataflow pipeline repairs each file as it arrives, before the write. Dataflow runs the same code for streaming and batch and scales the workers with the load. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Dataflow runs the same code for streaming and batch and scales the workers with the load. In this case: A Dataflow pipeline repairs each file as it arrives, before the write.
- **B:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A Dataflow pipeline repairs each file as it arrives, before the write.
- **C:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A Dataflow pipeline repairs each file as it arrives, before the write.
- **D:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: A Dataflow pipeline repairs each file as it arrives, before the write.

### Question 29 — B

Answer: Store the files in Cloud Storage. Cloud Storage holds objects of any size without a schema. Cloud Storage holds objects of any shape and is the landing zone every other service can read. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Why the correct answer wins: Cloud Storage holds objects of any size without a schema.
- **B:** Correct. Cloud Storage holds objects of any shape and is the landing zone every other service can read. In this case: Cloud Storage holds objects of any size without a schema.
- **C:** Incorrect for this question. Spanner gives strongly consistent relational transactions across regions at global scale. Why the correct answer wins: Cloud Storage holds objects of any size without a schema.
- **D:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: Cloud Storage holds objects of any size without a schema.

### Question 30 — A

Answer: Choose a regional location. One region is the cheapest placement for a single-city user base. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. In this case: One region is the cheapest placement for a single-city user base.
- **B:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: One region is the cheapest placement for a single-city user base.
- **C:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: One region is the cheapest placement for a single-city user base.
- **D:** Incorrect for this question. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Why the correct answer wins: One region is the cheapest placement for a single-city user base.

### Question 31 — D

Answer: Create a BigQuery view over the join. A view projects the columns to expose and reads the table beneath it. A view stores the query rather than the rows, so the answer stays current at query time. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An external table reads the objects where they sit and does not copy them into storage. Why the correct answer wins: A view projects the columns to expose and reads the table beneath it.
- **B:** Incorrect for this question. A native table gives the warehouse its own copy and the best scan performance. Why the correct answer wins: A view projects the columns to expose and reads the table beneath it.
- **C:** Incorrect for this question. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. Why the correct answer wins: A view projects the columns to expose and reads the table beneath it.
- **D:** Correct. A view stores the query rather than the rows, so the answer stays current at query time. In this case: A view projects the columns to expose and reads the table beneath it.

### Question 32 — B

Answer: Create a BigQuery materialized view. A materialized view stores the result and refreshes it. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A view stores the query rather than the rows, so the answer stays current at query time. Why the correct answer wins: A materialized view stores the result and refreshes it.
- **B:** Correct. In this case: A materialized view stores the result and refreshes it.
- **C:** Incorrect for this question. A native table gives the warehouse its own copy and the best scan performance. Why the correct answer wins: A materialized view stores the result and refreshes it.
- **D:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: A materialized view stores the result and refreshes it.

### Question 33 — A, E

Answers: Filter the query on the partition column; Load the files into a native table. The partition filter restricts the scan, and the native table removes the external read. A partition filter restricts the scan to the partitions the query needs. A native table gives the warehouse its own copy and the best scan performance. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A partition filter restricts the scan to the partitions the query needs. In this case: The partition filter restricts the scan, and the native table removes the external read.
- **B:** Incorrect for this question. An external table reads the objects where they sit and does not copy them into storage. Why the correct answer wins: The partition filter restricts the scan, and the native table removes the external read.
- **C:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The partition filter restricts the scan, and the native table removes the external read.
- **D:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: The partition filter restricts the scan, and the native table removes the external read.
- **E:** Correct. A native table gives the warehouse its own copy and the best scan performance. In this case: The partition filter restricts the scan, and the native table removes the external read.

### Question 34 — B

Answer: Write a SQL query in BigQuery and save the result. A parameterised saved query answers each variation without a new artefact. A saved SQL query answers a business question and can be scheduled or exported. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A parameterised saved query answers each variation without a new artefact.
- **B:** Correct. A saved SQL query answers a business question and can be scheduled or exported. In this case: A parameterised saved query answers each variation without a new artefact.
- **C:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: A parameterised saved query answers each variation without a new artefact.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A parameterised saved query answers each variation without a new artefact.

### Question 35 — B

Answer: Analyse the data in a Colab Enterprise notebook. Colab Enterprise provides a managed runtime under project IAM. Colab Enterprise gives a managed notebook runtime with project IAM and BigQuery access. Local study-map skill 2.2 (Colab Enterprise and Jupyter Notebooks), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Colab Enterprise provides a managed runtime under project IAM.
- **B:** Correct. Colab Enterprise gives a managed notebook runtime with project IAM and BigQuery access. In this case: Colab Enterprise provides a managed runtime under project IAM.
- **C:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: Colab Enterprise provides a managed runtime under project IAM.
- **D:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: Colab Enterprise provides a managed runtime under project IAM.

### Question 36 — D

Answer: Query BigQuery from the notebook with the %%bigquery magic. The BigQuery magic returns the result as a DataFrame for plotting. The magic returns a DataFrame from a SQL statement inside the notebook cell. Local study-map skill 2.2 (Colab Enterprise and Jupyter Notebooks), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: The BigQuery magic returns the result as a DataFrame for plotting.
- **B:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: The BigQuery magic returns the result as a DataFrame for plotting.
- **C:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: The BigQuery magic returns the result as a DataFrame for plotting.
- **D:** Correct. The magic returns a DataFrame from a SQL statement inside the notebook cell. In this case: The BigQuery magic returns the result as a DataFrame for plotting.

### Question 37 — D

Answer: Write a SQL query in BigQuery and save the result. A SQL query returns the region breakdown and can be re-run. A saved SQL query answers a business question and can be scheduled or exported. Local study-map skill 2.3 (Business Question Analysis), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: A SQL query returns the region breakdown and can be re-run.
- **B:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: A SQL query returns the region breakdown and can be re-run.
- **C:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A SQL query returns the region breakdown and can be re-run.
- **D:** Correct. A saved SQL query answers a business question and can be scheduled or exported. In this case: A SQL query returns the region breakdown and can be re-run.

### Question 38 — B

Answer: Share the dashboard with a scheduled delivery. A scheduled delivery sends the answer without anyone assembling it. A scheduled delivery pushes the answer to people who will not open the tool. Local study-map skill 2.3 (Business Question Analysis), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A scheduled delivery sends the answer without anyone assembling it.
- **B:** Correct. A scheduled delivery pushes the answer to people who will not open the tool. In this case: A scheduled delivery sends the answer without anyone assembling it.
- **C:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A scheduled delivery sends the answer without anyone assembling it.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A scheduled delivery sends the answer without anyone assembling it.

### Question 39 — A

Answer: Build a governed Looker dashboard. A Looker dashboard inherits the model, so no tile can redefine churn. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: A Looker dashboard inherits the model, so no tile can redefine churn.
- **B:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A Looker dashboard inherits the model, so no tile can redefine churn.
- **C:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A Looker dashboard inherits the model, so no tile can redefine churn.
- **D:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: A Looker dashboard inherits the model, so no tile can redefine churn.

### Question 40 — D, E

Answers: Add a LookML measure for the calculation; Share the dashboard with a scheduled delivery. The shared measure fixes the definition, and the delivery pushes the answer outward. A measure declares the aggregation once so every report computes it the same way. A scheduled delivery pushes the answer to people who will not open the tool. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The shared measure fixes the definition, and the delivery pushes the answer outward.
- **B:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: The shared measure fixes the definition, and the delivery pushes the answer outward.
- **C:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: The shared measure fixes the definition, and the delivery pushes the answer outward.
- **D:** Correct. A scheduled delivery pushes the answer to people who will not open the tool. In this case: The shared measure fixes the definition, and the delivery pushes the answer outward.
- **E:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: The shared measure fixes the definition, and the delivery pushes the answer outward.

### Question 41 — C

Answer: Add a LookML measure for the calculation. A shared measure computes churn once for both dashboards. A measure declares the aggregation once so every report computes it the same way. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Why the correct answer wins: A shared measure computes churn once for both dashboards.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A shared measure computes churn once for both dashboards.
- **C:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: A shared measure computes churn once for both dashboards.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A shared measure computes churn once for both dashboards.

### Question 42 — C

Answer: Build a Looker Studio report. Looker Studio connects a handful of sources without modelling work. Looker Studio is the fast self-serve reporting surface for a small number of sources. Local study-map skill 2.5 (Looker and Looker Studio Comparison), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: Looker Studio connects a handful of sources without modelling work.
- **B:** Incorrect for this question. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Why the correct answer wins: Looker Studio connects a handful of sources without modelling work.
- **C:** Correct. Looker Studio is the fast self-serve reporting surface for a small number of sources. In this case: Looker Studio connects a handful of sources without modelling work.
- **D:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Looker Studio connects a handful of sources without modelling work.

### Question 43 — C

Answer: Build a governed Looker dashboard. Looker serves every report from one governed model. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Local study-map skill 2.5 (Looker and Looker Studio Comparison), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: Looker serves every report from one governed model.
- **B:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: Looker serves every report from one governed model.
- **C:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: Looker serves every report from one governed model.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: Looker serves every report from one governed model.

### Question 44 — C

Answer: Change the LookML parameter in the view. A LookML parameter changes the calendar for every consumer. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An explore defines which joins and fields a report author may use. Why the correct answer wins: A LookML parameter changes the calendar for every consumer.
- **B:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: A LookML parameter changes the calendar for every consumer.
- **C:** Correct. A LookML parameter changes the model for every dashboard that uses it rather than one tile. In this case: A LookML parameter changes the calendar for every consumer.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A LookML parameter changes the calendar for every consumer.

### Question 45 — B, D

Answers: Expose the table through a LookML explore; Change the LookML parameter in the view. The parameter holds the calendar once, and the explore gates the joins. An explore defines which joins and fields a report author may use. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The parameter holds the calendar once, and the explore gates the joins.
- **B:** Correct. An explore defines which joins and fields a report author may use. In this case: The parameter holds the calendar once, and the explore gates the joins.
- **C:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: The parameter holds the calendar once, and the explore gates the joins.
- **D:** Correct. A LookML parameter changes the model for every dashboard that uses it rather than one tile. In this case: The parameter holds the calendar once, and the explore gates the joins.
- **E:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: The parameter holds the calendar once, and the explore gates the joins.

### Question 46 — A

Answer: Expose the table through a LookML explore. An explore declares which joins a report author may use. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: An explore declares which joins a report author may use.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: An explore declares which joins a report author may use.
- **C:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: An explore declares which joins a report author may use.
- **D:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: An explore declares which joins a report author may use.

### Question 47 — B

Answer: Train an AutoML tabular model. AutoML searches architectures for a team without modelling code. AutoML searches architectures and tuning for a team that has labels but no modelling code. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.PREDICT applies a trained model to new rows and returns the prediction. Why the correct answer wins: AutoML searches architectures for a team without modelling code.
- **B:** Correct. AutoML searches architectures and tuning for a team that has labels but no modelling code. In this case: AutoML searches architectures for a team without modelling code.
- **C:** Incorrect for this question. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Why the correct answer wins: AutoML searches architectures for a team without modelling code.
- **D:** Incorrect for this question. Linear regression predicts a continuous value and trains with SQL against the table. Why the correct answer wins: AutoML searches architectures for a team without modelling code.

### Question 48 — B, D

Answers: Train a BigQuery ML boosted tree model; Train a BigQuery ML logistic regression model. A boosted tree fits the interactions, and logistic regression returns the probability. A boosted tree model fits non-linear relationships in tabular rows. Logistic regression predicts a binary outcome and trains with SQL against the table. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. AutoML searches architectures and tuning for a team that has labels but no modelling code. Why the correct answer wins: A boosted tree fits the interactions, and logistic regression returns the probability.
- **B:** Correct. Logistic regression predicts a binary outcome and trains with SQL against the table. In this case: A boosted tree fits the interactions, and logistic regression returns the probability.
- **C:** Incorrect for this question. ARIMA_PLUS forecasts a series and returns an interval per period. Why the correct answer wins: A boosted tree fits the interactions, and logistic regression returns the probability.
- **D:** Correct. A boosted tree model fits non-linear relationships in tabular rows. In this case: A boosted tree fits the interactions, and logistic regression returns the probability.
- **E:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: A boosted tree fits the interactions, and logistic regression returns the probability.

### Question 49 — C

Answer: Train a BigQuery ML ARIMA_PLUS model. ARIMA_PLUS models trend and seasonality for one series. ARIMA_PLUS forecasts a series and returns an interval per period. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: ARIMA_PLUS models trend and seasonality for one series.
- **B:** Incorrect for this question. Linear regression predicts a continuous value and trains with SQL against the table. Why the correct answer wins: ARIMA_PLUS models trend and seasonality for one series.
- **C:** Correct. ARIMA_PLUS forecasts a series and returns an interval per period. In this case: ARIMA_PLUS models trend and seasonality for one series.
- **D:** Incorrect for this question. Logistic regression predicts a binary outcome and trains with SQL against the table. Why the correct answer wins: ARIMA_PLUS models trend and seasonality for one series.

### Question 50 — A

Answer: Create a BigQuery remote model over a Gemini model. A remote model runs the prompt from SQL where the rows already sit. A remote model sends the prompt to Gemini from SQL while the rows stay in BigQuery. Local study-map skill 2.8 (Remote Gemini Models in BigQuery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A remote model sends the prompt to Gemini from SQL while the rows stay in BigQuery. In this case: A remote model runs the prompt from SQL where the rows already sit.
- **B:** Incorrect for this question. Fine-tuning adapts the model to the domain using labelled rows that stay in BigQuery. Why the correct answer wins: A remote model runs the prompt from SQL where the rows already sit.
- **C:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: A remote model runs the prompt from SQL where the rows already sit.
- **D:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: A remote model runs the prompt from SQL where the rows already sit.

### Question 51 — B

Answer: Create the BigQuery connection that reaches the model endpoint. The connection supplies the identity used to reach the endpoint. The connection carries the service account that BigQuery uses to call the remote model. Local study-map skill 2.8 (Remote Gemini Models in BigQuery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: The connection supplies the identity used to reach the endpoint.
- **B:** Correct. The connection carries the service account that BigQuery uses to call the remote model. In this case: The connection supplies the identity used to reach the endpoint.
- **C:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: The connection supplies the identity used to reach the endpoint.
- **D:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: The connection supplies the identity used to reach the endpoint.

### Question 52 — B

Answer: Plan collection, training, evaluation, then prediction. A plan fixes the metric and the acceptance test before training starts. A planned sequence fixes the data, the metric, and the acceptance test before any model is trained. Local study-map skill 2.9 (ML Project Planning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: A plan fixes the metric and the acceptance test before training starts.
- **B:** Correct. A planned sequence fixes the data, the metric, and the acceptance test before any model is trained. In this case: A plan fixes the metric and the acceptance test before training starts.
- **C:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A plan fixes the metric and the acceptance test before training starts.
- **D:** Incorrect for this question. Training loss measures fit to the rows it has already seen, not the answer on new rows. Why the correct answer wins: A plan fixes the metric and the acceptance test before training starts.

### Question 53 — D

Answer: Hold out whole entities so none spans both splits. A grouped split holds out whole entities so none spans both sides. A grouped split keeps one customer from appearing on both sides of the evaluation. Local study-map skill 2.9 (ML Project Planning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A time-ordered split tests the model on rows that come after the ones it learned from. Why the correct answer wins: A grouped split holds out whole entities so none spans both sides.
- **B:** Incorrect for this question. Training loss measures fit to the rows it has already seen, not the answer on new rows. Why the correct answer wins: A grouped split holds out whole entities so none spans both sides.
- **C:** Incorrect for this question. A held-out split gives an estimate that the training rows cannot inflate. Why the correct answer wins: A grouped split holds out whole entities so none spans both sides.
- **D:** Correct. A grouped split keeps one customer from appearing on both sides of the evaluation. In this case: A grouped split holds out whole entities so none spans both sides.

### Question 54 — D

Answer: Evaluate the model with ML.EVALUATE. ML.EVALUATE returns the metrics against a labelled dataset. Local study-map skill 2.10 (BigQuery ML Training and Evaluation), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: ML.EVALUATE returns the metrics against a labelled dataset.
- **B:** Incorrect for this question. ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row. Why the correct answer wins: ML.EVALUATE returns the metrics against a labelled dataset.
- **C:** Incorrect for this question. ML.PREDICT applies a trained model to new rows and returns the prediction. Why the correct answer wins: ML.EVALUATE returns the metrics against a labelled dataset.
- **D:** Correct. In this case: ML.EVALUATE returns the metrics against a labelled dataset.

### Question 55 — C

Answer: Train a BigQuery ML logistic regression model. Logistic regression predicts a binary outcome with a probability. Logistic regression predicts a binary outcome and trains with SQL against the table. Local study-map skill 2.10 (BigQuery ML Training and Evaluation), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Why the correct answer wins: Logistic regression predicts a binary outcome with a probability.
- **B:** Incorrect for this question. Linear regression predicts a continuous value and trains with SQL against the table. Why the correct answer wins: Logistic regression predicts a binary outcome with a probability.
- **C:** Correct. Logistic regression predicts a binary outcome and trains with SQL against the table. In this case: Logistic regression predicts a binary outcome with a probability.
- **D:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: Logistic regression predicts a binary outcome with a probability.

### Question 56 — D

Answer: Score the rows with ML.PREDICT. ML.PREDICT applies the model to the list of new rows. ML.PREDICT applies a trained model to new rows and returns the prediction. Local study-map skill 2.11 (BigQuery ML Inference), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: ML.PREDICT applies the model to the list of new rows.
- **B:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: ML.PREDICT applies the model to the list of new rows.
- **C:** Incorrect for this question. ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row. Why the correct answer wins: ML.PREDICT applies the model to the list of new rows.
- **D:** Correct. ML.PREDICT applies a trained model to new rows and returns the prediction. In this case: ML.PREDICT applies the model to the list of new rows.

### Question 57 — A

Answer: Register the model version in Model Registry. Model Registry keeps each version with its lineage and metrics. Model Registry keeps each version with its lineage so a deployment names a version rather than a path. Local study-map skill 2.12 (Model Registry), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Model Registry keeps each version with its lineage so a deployment names a version rather than a path. In this case: Model Registry keeps each version with its lineage and metrics.
- **B:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: Model Registry keeps each version with its lineage and metrics.
- **C:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Model Registry keeps each version with its lineage and metrics.
- **D:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: Model Registry keeps each version with its lineage and metrics.

### Question 58 — D

Answer: Manage the SQL transformations in Dataform. Dataform resolves the dependencies and runs the graph. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Dataform resolves the dependencies and runs the graph.
- **B:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Dataform resolves the dependencies and runs the graph.
- **C:** Incorrect for this question. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Why the correct answer wins: Dataform resolves the dependencies and runs the graph.
- **D:** Correct. In this case: Dataform resolves the dependencies and runs the graph.

### Question 59 — C

Answer: Run the transformation as Spark on Dataproc. Dataproc runs the Spark job the team already owns. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Dataproc runs the Spark job the team already owns.
- **B:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Dataproc runs the Spark job the team already owns.
- **C:** Correct. Dataproc runs Spark or Hadoop jobs when the team already owns that code. In this case: Dataproc runs the Spark job the team already owns.
- **D:** Incorrect for this question. Dataflow runs the same code for streaming and batch and scales the workers with the load. Why the correct answer wins: Dataproc runs the Spark job the team already owns.

### Question 60 — B, E

Answers: Build the pipeline in Dataflow; Manage the SQL transformations in Dataform. Dataflow defines the streaming path once, and Dataform versions the SQL. Dataflow runs the same code for streaming and batch and scales the workers with the load. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: Dataflow defines the streaming path once, and Dataform versions the SQL.
- **B:** Correct. Dataflow runs the same code for streaming and batch and scales the workers with the load. In this case: Dataflow defines the streaming path once, and Dataform versions the SQL.
- **C:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Dataflow defines the streaming path once, and Dataform versions the SQL.
- **D:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Dataflow defines the streaming path once, and Dataform versions the SQL.
- **E:** Correct. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. In this case: Dataflow defines the streaming path once, and Dataform versions the SQL.

### Question 61 — B

Answer: Build the pipeline in Cloud Data Fusion. Data Fusion joins the sources in a versioned visual pipeline. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Data Fusion joins the sources in a versioned visual pipeline.
- **B:** Correct. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. In this case: Data Fusion joins the sources in a versioned visual pipeline.
- **C:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Data Fusion joins the sources in a versioned visual pipeline.
- **D:** Incorrect for this question. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. Why the correct answer wins: Data Fusion joins the sources in a versioned visual pipeline.

### Question 62 — A

Answer: Load the raw rows, then transform them inside the warehouse. ELT moves the transformation to the warehouse engine. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 3.2 (ELT and ETL Pipeline Design), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT moves the transformation to the warehouse engine.
- **B:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ELT moves the transformation to the warehouse engine.
- **C:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ELT moves the transformation to the warehouse engine.
- **D:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT moves the transformation to the warehouse engine.

### Question 63 — D

Answer: Extract, transform outside the warehouse, then load the result. ETL cleans the record before the destination receives it. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Local study-map skill 3.2 (ELT and ETL Pipeline Design), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETL cleans the record before the destination receives it.
- **B:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: ETL cleans the record before the destination receives it.
- **C:** Incorrect for this question. A staging table separates a failed load from a failed transform, so each can be retried on its own. Why the correct answer wins: ETL cleans the record before the destination receives it.
- **D:** Correct. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. In this case: ETL cleans the record before the destination receives it.

### Question 64 — D

Answer: Schedule the SQL with a BigQuery scheduled query. A scheduled query runs one statement on a cron schedule. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A workflow template defines the cluster and the steps so the same job can be re-run identically. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **B:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **C:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **D:** Correct. In this case: A scheduled query runs one statement on a cron schedule.

### Question 65 — B, E

Answers: Schedule the SQL with a BigQuery scheduled query; Create a Cloud Monitoring alert policy on the job metric. The scheduled query runs the aggregate, and the alert policy pages the owner. A scheduled query runs one statement on a cron schedule and writes its result. An alert policy pages someone when the backlog or the failure rate crosses a threshold. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: The scheduled query runs the aggregate, and the alert policy pages the owner.
- **B:** Correct. An alert policy pages someone when the backlog or the failure rate crosses a threshold. In this case: The scheduled query runs the aggregate, and the alert policy pages the owner.
- **C:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: The scheduled query runs the aggregate, and the alert policy pages the owner.
- **D:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: The scheduled query runs the aggregate, and the alert policy pages the owner.
- **E:** Correct. A scheduled query runs one statement on a cron schedule and writes its result. In this case: The scheduled query runs the aggregate, and the alert policy pages the owner.

### Question 66 — B

Answer: Trigger the job from Cloud Scheduler. Cloud Scheduler calls the endpoint on the schedule. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Why the correct answer wins: Cloud Scheduler calls the endpoint on the schedule.
- **B:** Correct. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. In this case: Cloud Scheduler calls the endpoint on the schedule.
- **C:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Cloud Scheduler calls the endpoint on the schedule.
- **D:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Cloud Scheduler calls the endpoint on the schedule.

### Question 67 — C

Answer: Watch the job graph and per-step throughput in the Dataflow console. The job view shows the throughput per step and the watermark. The Dataflow job view shows the running graph, watermarks, and the step that is backlogged. Local study-map skill 3.4 (Dataflow Job Monitoring), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: The job view shows the throughput per step and the watermark.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The job view shows the throughput per step and the watermark.
- **C:** Correct. The Dataflow job view shows the running graph, watermarks, and the step that is backlogged. In this case: The job view shows the throughput per step and the watermark.
- **D:** Incorrect for this question. Logs Explorer filters the log entries that explain why a worker restarted. Why the correct answer wins: The job view shows the throughput per step and the watermark.

### Question 68 — A

Answer: Write the rejected rows to a dead-letter table. A dead-letter table keeps the rejected events for replay. A dead-letter table preserves the rows that failed so they can be repaired and replayed. Local study-map skill 3.4 (Dataflow Job Monitoring), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A dead-letter table preserves the rows that failed so they can be repaired and replayed. In this case: A dead-letter table keeps the rejected events for replay.
- **B:** Incorrect for this question. A wide table removes the join, at the cost of duplicated rows and a wider scan. Why the correct answer wins: A dead-letter table keeps the rejected events for replay.
- **C:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A dead-letter table keeps the rejected events for replay.
- **D:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A dead-letter table keeps the rejected events for replay.

### Question 69 — A

Answer: Query the job logs in Logs Explorer. Logs Explorer filters the entries for that worker. Local study-map skill 3.5 (Logs and Monitoring Review), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: Logs Explorer filters the entries for that worker.
- **B:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: Logs Explorer filters the entries for that worker.
- **C:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Logs Explorer filters the entries for that worker.
- **D:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: Logs Explorer filters the entries for that worker.

### Question 70 — C

Answer: Create a Cloud Monitoring alert policy on the job metric. An alert policy pages an owner when the job fails. An alert policy pages someone when the backlog or the failure rate crosses a threshold. Local study-map skill 3.5 (Logs and Monitoring Review), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Logs Explorer filters the log entries that explain why a worker restarted. Why the correct answer wins: An alert policy pages an owner when the job fails.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: An alert policy pages an owner when the job fails.
- **C:** Correct. An alert policy pages someone when the backlog or the failure rate crosses a threshold. In this case: An alert policy pages an owner when the job fails.
- **D:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: An alert policy pages an owner when the job fails.

### Question 71 — A

Answer: Orchestrate the steps in Cloud Composer. Cloud Composer runs an Airflow DAG with dependencies and retries. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: Cloud Composer runs an Airflow DAG with dependencies and retries.
- **B:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Cloud Composer runs an Airflow DAG with dependencies and retries.
- **C:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Cloud Composer runs an Airflow DAG with dependencies and retries.
- **D:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Cloud Composer runs an Airflow DAG with dependencies and retries.

### Question 72 — D, E

Answers: Sequence the API calls with Workflows; Start the pipeline from an Eventarc trigger. Eventarc routes the object event, and Workflows chains the calls. Workflows chains service calls and HTTP endpoints without running a server. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Eventarc routes the object event, and Workflows chains the calls.
- **B:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Eventarc routes the object event, and Workflows chains the calls.
- **C:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Eventarc routes the object event, and Workflows chains the calls.
- **D:** Correct. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. In this case: Eventarc routes the object event, and Workflows chains the calls.
- **E:** Correct. Workflows chains service calls and HTTP endpoints without running a server. In this case: Eventarc routes the object event, and Workflows chains the calls.

### Question 73 — B

Answer: Sequence the API calls with Workflows. Workflows chains the calls without a server. Workflows chains service calls and HTTP endpoints without running a server. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Workflows chains the calls without a server.
- **B:** Correct. Workflows chains service calls and HTTP endpoints without running a server. In this case: Workflows chains the calls without a server.
- **C:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Workflows chains the calls without a server.
- **D:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Workflows chains the calls without a server.

### Question 74 — A

Answer: Subscribe BigQuery to the Pub/Sub topic. A BigQuery subscription writes each message into the table. Local study-map skill 3.7 (Event-Driven Ingestion with Pub/Sub), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A BigQuery subscription writes each message into the table.
- **B:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: A BigQuery subscription writes each message into the table.
- **C:** Incorrect for this question. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Why the correct answer wins: A BigQuery subscription writes each message into the table.
- **D:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A BigQuery subscription writes each message into the table.

### Question 75 — C

Answer: Start the pipeline from an Eventarc trigger. An Eventarc trigger routes the object event to the DAG target. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Local study-map skill 3.8 (Eventarc Triggers), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A BigQuery subscription writes each published message into a table as it arrives. Why the correct answer wins: An Eventarc trigger routes the object event to the DAG target.
- **B:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: An Eventarc trigger routes the object event to the DAG target.
- **C:** Correct. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. In this case: An Eventarc trigger routes the object event to the DAG target.
- **D:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: An Eventarc trigger routes the object event to the DAG target.

### Question 76 — D

Answer: Grant the predefined role that matches the task. The narrowest role that reads that table keeps everything else closed. A predefined role carries the permissions for one job and nothing else. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: The narrowest role that reads that table keeps everything else closed.
- **B:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: The narrowest role that reads that table keeps everything else closed.
- **C:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: The narrowest role that reads that table keeps everything else closed.
- **D:** Correct. A predefined role carries the permissions for one job and nothing else. In this case: The narrowest role that reads that table keeps everything else closed.

### Question 77 — A, B

Answers: Create a custom role with only the permissions used; Run the job as a dedicated service account. The custom role omits the permission, and the service account keeps the principal non-human. A custom role narrows the grant when no predefined role matches the job exactly. A service account gives the workload its own identity instead of borrowing a person's. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A service account gives the workload its own identity instead of borrowing a person's. In this case: The custom role omits the permission, and the service account keeps the principal non-human.
- **B:** Correct. A custom role narrows the grant when no predefined role matches the job exactly. In this case: The custom role omits the permission, and the service account keeps the principal non-human.
- **C:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: The custom role omits the permission, and the service account keeps the principal non-human.
- **D:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: The custom role omits the permission, and the service account keeps the principal non-human.
- **E:** Incorrect for this question. A perimeter blocks data movement outside the boundary even for an authorised identity. Why the correct answer wins: The custom role omits the permission, and the service account keeps the principal non-human.

### Question 78 — D

Answer: Run the job as a dedicated service account. A service account gives the pipeline its own identity. A service account gives the workload its own identity instead of borrowing a person's. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A service account gives the pipeline its own identity.
- **B:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: A service account gives the pipeline its own identity.
- **C:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A service account gives the pipeline its own identity.
- **D:** Correct. A service account gives the workload its own identity instead of borrowing a person's. In this case: A service account gives the pipeline its own identity.

### Question 79 — C

Answer: Assign a predefined role to the group. A predefined role covers the function and avoids the breadth of a basic role. A predefined role is maintained by Google and covers one service or one job function. Local study-map skill 4.2 (Basic, Predefined, and Custom Roles), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A predefined role covers the function and avoids the breadth of a basic role.
- **B:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A predefined role covers the function and avoids the breadth of a basic role.
- **C:** Correct. A predefined role is maintained by Google and covers one service or one job function. In this case: A predefined role covers the function and avoids the breadth of a basic role.
- **D:** Incorrect for this question. A custom role narrows the grant when no predefined role matches the job exactly. Why the correct answer wins: A predefined role covers the function and avoids the breadth of a basic role.

### Question 80 — C

Answer: Create a custom role with only the permissions used. A custom role withholds that permission without widening anything else. A custom role narrows the grant when no predefined role matches the job exactly. Local study-map skill 4.2 (Basic, Predefined, and Custom Roles), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A custom role withholds that permission without widening anything else.
- **B:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A custom role withholds that permission without widening anything else.
- **C:** Correct. A custom role narrows the grant when no predefined role matches the job exactly. In this case: A custom role withholds that permission without widening anything else.
- **D:** Incorrect for this question. A predefined role is maintained by Google and covers one service or one job function. Why the correct answer wins: A custom role withholds that permission without widening anything else.

### Question 81 — A

Answer: Enable uniform bucket-level access. Uniform bucket-level access puts every decision in IAM. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. Local study-map skill 4.3 (Cloud Storage Access Control), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. In this case: Uniform bucket-level access puts every decision in IAM.
- **B:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Uniform bucket-level access puts every decision in IAM.
- **C:** Incorrect for this question. Per-object ACLs are hard to audit and are overridden when uniform access is enabled. Why the correct answer wins: Uniform bucket-level access puts every decision in IAM.
- **D:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: Uniform bucket-level access puts every decision in IAM.

### Question 82 — B

Answer: Issue a signed URL with a short expiry. A signed URL grants short-lived access to that object alone. A signed URL grants temporary read access to one object without changing IAM. Local study-map skill 4.3 (Cloud Storage Access Control), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export hands over a copy that the publisher can no longer control or revoke. Why the correct answer wins: A signed URL grants short-lived access to that object alone.
- **B:** Correct. A signed URL grants temporary read access to one object without changing IAM. In this case: A signed URL grants short-lived access to that object alone.
- **C:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A signed URL grants short-lived access to that object alone.
- **D:** Incorrect for this question. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. Why the correct answer wins: A signed URL grants short-lived access to that object alone.

### Question 83 — D

Answer: Publish the dataset through Analytics Hub. Analytics Hub shares the dataset in place under the publisher's policy. Analytics Hub shares a curated dataset with a subscriber who reads it in place. Local study-map skill 4.4 (Analytics Hub Data Sharing), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export hands over a copy that the publisher can no longer control or revoke. Why the correct answer wins: Analytics Hub shares the dataset in place under the publisher's policy.
- **B:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: Analytics Hub shares the dataset in place under the publisher's policy.
- **C:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Analytics Hub shares the dataset in place under the publisher's policy.
- **D:** Correct. Analytics Hub shares a curated dataset with a subscriber who reads it in place. In this case: Analytics Hub shares the dataset in place under the publisher's policy.

### Question 84 — D

Answer: Add the project to a VPC Service Controls perimeter. A perimeter blocks movement regardless of the identity's permissions. A perimeter blocks data movement outside the boundary even for an authorised identity. Local study-map skill 4.4 (Analytics Hub Data Sharing), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A perimeter blocks movement regardless of the identity's permissions.
- **B:** Incorrect for this question. Analytics Hub shares a curated dataset with a subscriber who reads it in place. Why the correct answer wins: A perimeter blocks movement regardless of the identity's permissions.
- **C:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: A perimeter blocks movement regardless of the identity's permissions.
- **D:** Correct. A perimeter blocks data movement outside the boundary even for an authorised identity. In this case: A perimeter blocks movement regardless of the identity's permissions.

### Question 85 — B

Answer: Move the objects to Nearline. Nearline suits reads about once a month. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Coldline suits reads a few times a year and has a longer minimum storage duration. Why the correct answer wins: Nearline suits reads about once a month.
- **B:** Correct. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. In this case: Nearline suits reads about once a month.
- **C:** Incorrect for this question. Archive is the cheapest class for data kept for compliance and read almost never. Why the correct answer wins: Nearline suits reads about once a month.
- **D:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Nearline suits reads about once a month.

### Question 86 — B, E

Answers: Enable Autoclass on the bucket; Add a lifecycle rule that changes the storage class. Autoclass follows each object's access, and a rule demotes objects by age. Autoclass moves each object between classes as its access pattern changes. A setStorageClass rule demotes an object after a number of days so the cost falls without a copy. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Coldline suits reads a few times a year and has a longer minimum storage duration. Why the correct answer wins: Autoclass follows each object's access, and a rule demotes objects by age.
- **B:** Correct. A setStorageClass rule demotes an object after a number of days so the cost falls without a copy. In this case: Autoclass follows each object's access, and a rule demotes objects by age.
- **C:** Incorrect for this question. Keeping every version in the hot class pays the highest rate for data nobody reads. Why the correct answer wins: Autoclass follows each object's access, and a rule demotes objects by age.
- **D:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: Autoclass follows each object's access, and a rule demotes objects by age.
- **E:** Correct. Autoclass moves each object between classes as its access pattern changes. In this case: Autoclass follows each object's access, and a rule demotes objects by age.

### Question 87 — D

Answer: Keep the objects in the Standard class. Standard is for objects read frequently. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes. Why the correct answer wins: Standard is for objects read frequently.
- **B:** Incorrect for this question. Archive is the cheapest class for data kept for compliance and read almost never. Why the correct answer wins: Standard is for objects read frequently.
- **C:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: Standard is for objects read frequently.
- **D:** Correct. In this case: Standard is for objects read frequently.

### Question 88 — D

Answer: Add a lifecycle rule that deletes objects after the retention period. A lifecycle delete rule removes the object on age. A delete rule removes the objects once the retention period passes, without a person remembering. Local study-map skill 4.6 (Lifecycle Rules and Expiration), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keeping every version in the hot class pays the highest rate for data nobody reads. Why the correct answer wins: A lifecycle delete rule removes the object on age.
- **B:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: A lifecycle delete rule removes the object on age.
- **C:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A lifecycle delete rule removes the object on age.
- **D:** Correct. A delete rule removes the objects once the retention period passes, without a person remembering. In this case: A lifecycle delete rule removes the object on age.

### Question 89 — A

Answer: Set a table expiration on the dataset. Dataset-level expiration removes the tables created inside it. A dataset-level expiration removes tables created in it after the configured period. Local study-map skill 4.6 (Lifecycle Rules and Expiration), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A dataset-level expiration removes tables created in it after the configured period. In this case: Dataset-level expiration removes the tables created inside it.
- **B:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: Dataset-level expiration removes the tables created inside it.
- **C:** Incorrect for this question. A delete rule removes the objects once the retention period passes, without a person remembering. Why the correct answer wins: Dataset-level expiration removes the tables created inside it.
- **D:** Incorrect for this question. Partition expiration drops old partitions while the table keeps the recent ones. Why the correct answer wins: Dataset-level expiration removes the tables created inside it.

### Question 90 — C

Answer: Move the objects to Archive. Archive is the cheapest class for data read almost never. Local study-map skill 4.7 (Archiving Services), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Archive is the cheapest class for data read almost never.
- **B:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: Archive is the cheapest class for data read almost never.
- **C:** Correct. In this case: Archive is the cheapest class for data read almost never.
- **D:** Incorrect for this question. Coldline suits reads a few times a year and has a longer minimum storage duration. Why the correct answer wins: Archive is the cheapest class for data read almost never.

### Question 91 — C

Answer: Apply a bucket retention policy with a lock. A locked retention policy prevents deletion for the period. Local study-map skill 4.7 (Archiving Services), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: A locked retention policy prevents deletion for the period.
- **B:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A locked retention policy prevents deletion for the period.
- **C:** Correct. In this case: A locked retention policy prevents deletion for the period.
- **D:** Incorrect for this question. A delete rule removes the objects once the retention period passes, without a person remembering. Why the correct answer wins: A locked retention policy prevents deletion for the period.

### Question 92 — B

Answer: Enable automated backups and point-in-time recovery on Cloud SQL. Point-in-time recovery restores the state before the migration. Automated backups with point-in-time recovery restore the instance to a chosen moment. Local study-map skill 4.8 (Backup and Recovery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: Point-in-time recovery restores the state before the migration.
- **B:** Correct. Automated backups with point-in-time recovery restore the instance to a chosen moment. In this case: Point-in-time recovery restores the state before the migration.
- **C:** Incorrect for this question. A zonal instance is lost with its zone and gives no automatic failover. Why the correct answer wins: Point-in-time recovery restores the state before the migration.
- **D:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: Point-in-time recovery restores the state before the migration.

### Question 93 — D, E

Answers: Enable automated backups and point-in-time recovery on Cloud SQL; Restore into a scratch project on a schedule. The automated backup captures the state, and the drill proves it can be restored. Automated backups with point-in-time recovery restore the instance to a chosen moment. A restore drill is the only evidence that the backup can actually be used. Local study-map skill 4.8 (Backup and Recovery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A zonal instance is lost with its zone and gives no automatic failover. Why the correct answer wins: The automated backup captures the state, and the drill proves it can be restored.
- **B:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: The automated backup captures the state, and the drill proves it can be restored.
- **C:** Incorrect for this question. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. Why the correct answer wins: The automated backup captures the state, and the drill proves it can be restored.
- **D:** Correct. Automated backups with point-in-time recovery restore the instance to a chosen moment. In this case: The automated backup captures the state, and the drill proves it can be restored.
- **E:** Correct. A restore drill is the only evidence that the backup can actually be used. In this case: The automated backup captures the state, and the drill proves it can be restored.

### Question 94 — B

Answer: Create a dual-region bucket with a replication policy. A dual-region bucket states the pair and reports the lag. A dual-region bucket keeps a copy in a second region and reports the replication lag. Local study-map skill 4.9 (Replication), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A dual-region bucket states the pair and reports the lag.
- **B:** Correct. A dual-region bucket keeps a copy in a second region and reports the replication lag. In this case: A dual-region bucket states the pair and reports the lag.
- **C:** Incorrect for this question. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. Why the correct answer wins: A dual-region bucket states the pair and reports the lag.
- **D:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A dual-region bucket states the pair and reports the lag.

### Question 95 — C

Answer: Create a Cloud SQL read replica in another region. A read replica serves the reads from another region without taking writes. A read replica serves reads from a second region and can be promoted during a regional failure. Local study-map skill 4.9 (Replication), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A read replica serves the reads from another region without taking writes.
- **B:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A read replica serves the reads from another region without taking writes.
- **C:** Correct. A read replica serves reads from a second region and can be promoted during a regional failure. In this case: A read replica serves the reads from another region without taking writes.
- **D:** Incorrect for this question. A dual-region bucket keeps a copy in a second region and reports the replication lag. Why the correct answer wins: A read replica serves the reads from another region without taking writes.

### Question 96 — B

Answer: Choose a zonal resource. A zone is a single failure domain, which is acceptable for a sandbox. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Local study-map skill 4.10 (Primary and Secondary Locations), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Why the correct answer wins: A zone is a single failure domain, which is acceptable for a sandbox.
- **B:** Correct. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. In this case: A zone is a single failure domain, which is acceptable for a sandbox.
- **C:** Incorrect for this question. A regional instance fails over to a standby in another zone inside the same region. Why the correct answer wins: A zone is a single failure domain, which is acceptable for a sandbox.
- **D:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: A zone is a single failure domain, which is acceptable for a sandbox.

### Question 97 — D

Answer: Encrypt with a customer-managed key from Cloud KMS. A customer-managed key can be revoked by the customer. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. Local study-map skill 4.11 (CMEK, CSEK, and GMEK), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: A customer-managed key can be revoked by the customer.
- **B:** Incorrect for this question. A customer-supplied key never reaches Google, and losing it loses the object. Why the correct answer wins: A customer-managed key can be revoked by the customer.
- **C:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: A customer-managed key can be revoked by the customer.
- **D:** Correct. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. In this case: A customer-managed key can be revoked by the customer.

### Question 98 — A, E

Answers: Supply a customer-supplied key with each request; Use the Google-managed default encryption. A supplied key is per request with no schedule, and a Google-managed key is rotated by Google. A customer-supplied key never reaches Google, and losing it loses the object. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Local study-map skill 4.11 (CMEK, CSEK, and GMEK), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. In this case: A supplied key is per request with no schedule, and a Google-managed key is rotated by Google.
- **B:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: A supplied key is per request with no schedule, and a Google-managed key is rotated by Google.
- **C:** Incorrect for this question. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. Why the correct answer wins: A supplied key is per request with no schedule, and a Google-managed key is rotated by Google.
- **D:** Incorrect for this question. A key stored beside the data protects nothing against anyone who can read the store. Why the correct answer wins: A supplied key is per request with no schedule, and a Google-managed key is rotated by Google.
- **E:** Correct. A customer-supplied key never reaches Google, and losing it loses the object. In this case: A supplied key is per request with no schedule, and a Google-managed key is rotated by Google.

### Question 99 — D

Answer: Create the key in a Cloud KMS key ring in the data region. A key ring per environment keeps the keys separate and auditable in one place. A key ring in the same region keeps the key and the ciphertext under the same residency rule. Local study-map skill 4.12 (Cloud KMS), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: A key ring per environment keeps the keys separate and auditable in one place.
- **B:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: A key ring per environment keeps the keys separate and auditable in one place.
- **C:** Incorrect for this question. A rotation schedule limits how long one key version protects new data. Why the correct answer wins: A key ring per environment keeps the keys separate and auditable in one place.
- **D:** Correct. A key ring in the same region keeps the key and the ciphertext under the same residency rule. In this case: A key ring per environment keeps the keys separate and auditable in one place.

### Question 100 — B

Answer: Confirm the data is encrypted at rest by the storage service. Encryption at rest protects the stored bytes on the medium. Local study-map skill 4.13 (Encryption in Transit and at Rest), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key stored beside the data protects nothing against anyone who can read the store. Why the correct answer wins: Encryption at rest protects the stored bytes on the medium.
- **B:** Correct. In this case: Encryption at rest protects the stored bytes on the medium.
- **C:** Incorrect for this question. Encryption in transit protects the bytes while they are on the wire between client and service. Why the correct answer wins: Encryption at rest protects the stored bytes on the medium.
- **D:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: Encryption at rest protects the stored bytes on the medium.
