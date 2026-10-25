# Google Cloud Associate Data Practitioner — Full-Length Mock Exam 1

Associate Data Practitioner · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Data Preparation and Ingestion (Ingestion, Reporting, Pipelines, and Access)

### 1. A nightly feed must be cleansed and shaped before the warehouse holds it. Which approach is described?

- A. Extract, transform outside the warehouse, then load the result
- B. Load into a staging area, apply a light transform, then transform again in the warehouse
- C. Query the source system in place with a federated query
- D. Load the raw rows, then transform them inside the warehouse

### 2. Analysts keep changing the SQL and the raw extract must remain replayable. What should be used?

- A. Load the raw rows, then transform them inside the warehouse
- B. Combine the extracts in a spreadsheet and upload the result
- C. Query the source system in place with a federated query
- D. Extract, transform outside the warehouse, then load the result

### 3. A pipeline must keep an untouched copy, and a failed transform must not force another extract. Which two choices fit? Select two.

- A. Load the raw rows, then transform them inside the warehouse
- B. Transform on the source system before the export starts
- C. Extract, transform outside the warehouse, then load the result
- D. Combine the extracts in a spreadsheet and upload the result
- E. Land the extract in a staging table before any transform runs

### 4. A pricing team needs one comparison against a table that lives in Cloud SQL. What should be used?

- A. Load the raw rows, then transform them inside the warehouse
- B. Land the extract in a staging table before any transform runs
- C. Order a Transfer Appliance
- D. Query the source system in place with a federated query

### 5. Retried loads have created the same order three times in the table. What should be added?

- A. Load first and fix the rejected rows afterwards
- B. Profile the columns to measure the null rate before loading
- C. Select every column to be safe
- D. Deduplicate on the business key in the cleaning step

### 6. Nobody knows how many customer records are missing a region before the dashboard goes live. What should be done first?

- A. Profile the columns to measure the null rate before loading
- B. Select every column to be safe
- C. Clean the rows with SQL in BigQuery
- D. Load first and fix the rejected rows afterwards

### 7. A delivery must be proven complete and byte-identical to the source. Which two checks apply? Select two.

- A. Profile the columns to measure the null rate before loading
- B. Compare the row count with the source after every load
- C. Select every column to be safe
- D. Load first and fix the rejected rows afterwards
- E. Compare the source checksum with the delivered file

### 8. A partner silently started sending dates as free text and the join now returns nothing. What should be added?

- A. Select every column to be safe
- B. Land the data as CSV
- C. Cast the columns to the declared types before the load
- D. Load first and fix the rejected rows afterwards

### 9. Forty terabytes sit in a data centre and the network link would need eleven weeks. What should be used?

- A. Use BigQuery Data Transfer Service
- B. Replicate the changes with Datastream
- C. Order a Transfer Appliance
- D. Use Storage Transfer Service

### 10. An object store in another cloud must be mirrored into a bucket every night. What should be used?

- A. Load the files with the bq load command
- B. Order a Transfer Appliance
- C. Use Storage Transfer Service
- D. Copy the objects with the gcloud storage command

### 11. A marketing platform must deliver its daily campaign export into a warehouse table on a schedule. What should be used?

- A. Order a Transfer Appliance
- B. Use BigQuery Data Transfer Service
- C. Stream the rows with the BigQuery Storage Write API
- D. Load the rows with a client library from the application

### 12. A relational source must stay continuously replicated, and only the changes are wanted after the first copy. Which two tools apply? Select two.

- A. Order a Transfer Appliance
- B. Use Database Migration Service
- C. Copy the objects with the gcloud storage command
- D. Use BigQuery Data Transfer Service
- E. Replicate the changes with Datastream

### 13. Reports scan six of four hundred columns from a five terabyte extract. What format should be used?

- A. Land the data as XML
- B. Land the data as newline-delimited JSON
- C. Land the data as Parquet
- D. Land the data as CSV

### 14. A stream must carry its own field definitions so each record can be read years later. What format fits?

- A. Land the data as XML
- B. Land the data as Avro
- C. Land the data as CSV
- D. Convert the data to ORC before the load

### 15. A partner will only accept a flat text file with no types and no nesting. What format is required?

- A. Land the data as CSV
- B. Land the data as Parquet
- C. Land the data as newline-delimited JSON
- D. Land the data as Avro

### 16. A landing zone must accept a streaming writer and serve a columnar scan afterwards. Which two formats apply? Select two.

- A. Land the data as Parquet
- B. Land the data as Avro
- C. Land the data as CSV
- D. Convert the data to ORC before the load
- E. Land the data as XML

### 17. Two hundred CSV objects already sit in a bucket and must become one table. What should be used?

- A. Load the files with the bq load command
- B. Stream the rows with the BigQuery Storage Write API
- C. Load the rows with a client library from the application
- D. Copy the objects with the gcloud storage command

### 18. An application emits half a million rows a second and cannot write files first. What should be used?

- A. Stream the rows with the BigQuery Storage Write API
- B. Load the rows with a client library from the application
- C. Load the files with the bq load command
- D. Copy the objects with the gcloud storage command

### 19. A legacy extract must be rebuilt by a team that prefers a visual canvas over code. What should be used?

- A. Run the transformation as Spark on Dataproc
- B. Build the pipeline in Cloud Data Fusion
- C. Document the steps and have an analyst run them each morning
- D. Run a cron job on a Compute Engine instance

### 20. A telemetry service writes 200,000 rows a second and reads them back by device identifier. What should be used?

- A. Store the rows in Bigtable
- B. Store the rows in BigQuery
- C. Store the records in Cloud SQL
- D. Store the documents in Firestore

### 21. A ledger needs relational transactions that stay consistent across two continents. What should be used?

- A. Store the rows in Bigtable
- B. Store the documents in Firestore
- C. Store the records in Spanner
- D. Store the records in Cloud SQL

### 22. A mobile app must read a customer profile document by identifier with low latency. What should be used?

- A. Store the records in Cloud SQL
- B. Store the documents in Firestore
- C. Store the files in Cloud Storage
- D. Store the rows in Bigtable

### 23. A reporting layer must join warehouse tables and governed objects without copying the objects. Which two components apply? Select two.

- A. Store the rows in BigQuery
- B. Store the records in AlloyDB for PostgreSQL
- C. Store the files in Cloud Storage
- D. Keep the dataset on the analyst workstation
- E. Query the objects through BigLake tables

### 24. All users of a service live in one country and the budget is tight. Which location type fits?

- A. Choose a zonal resource
- B. Choose a regional location
- C. Choose a multi-region location
- D. Choose a dual-region location

### 25. The recovery plan names two specific regions with a defined recovery point. Which location type fits?

- A. Choose a regional location
- B. Choose a zonal resource
- C. Choose a dual-region location
- D. Choose a multi-region location

### 26. A public dataset must stay readable across a continent during a regional outage. Which location type fits?

- A. Choose a multi-region location
- B. Choose a dual-region location
- C. Choose a zonal resource
- D. Choose a regional location

### 27. A bucket holds product photographs and recorded support calls. How should they be classified?

- A. Treat the files as unstructured data
- B. Treat the records as semi-structured data
- C. Apply a schema on read at query time
- D. Treat the records as structured data

### 28. Event records arrive as JSON whose fields differ between sources. How should they be classified?

- A. Treat the records as structured data
- B. Treat the files as unstructured data
- C. Treat the records as semi-structured data
- D. Apply a schema on read at query time

### 29. An operator must stage a local export into a bucket from a shell script. What should be used?

- A. Copy the objects with the gcloud storage command
- B. Use Storage Transfer Service
- C. Load the files with the bq load command
- D. Load the rows with a client library from the application

### 30. A Python service already holds the rows in memory and must write them to a table. What should be used?

- A. Stream the rows with the BigQuery Storage Write API
- B. Load the files with the bq load command
- C. Copy the objects with the gcloud storage command
- D. Load the rows with a client library from the application

---

## Domain 2 — Data Analysis and Presentation (Files, Formats, Dashboards, and Governance)

### 31. A recurring revenue report must be reproducible from the warehouse itself. What should be used?

- A. Write a SQL query in BigQuery and save the result
- B. Create a BigQuery materialized view
- C. Export the query result to a spreadsheet for the business team
- D. Create a BigQuery view over the join

### 32. A join over two tables must stay current without storing a second copy. What should be used?

- A. Query the files through an external table
- B. Create a BigQuery view over the join
- C. Create a BigQuery materialized view
- D. Write a SQL query in BigQuery and save the result

### 33. A dashboard repeats a heavy join every fifteen minutes and the result changes little. What should be used?

- A. Create a BigQuery view over the join
- B. Load the files into a native table
- C. Create a BigQuery materialized view
- D. Write a SQL query in BigQuery and save the result

### 34. A report filters on one date column but still scans the whole table. Which two changes cut the bytes read? Select two.

- A. Export the query result to a spreadsheet for the business team
- B. Filter the query on the partition column
- C. Select every column to be safe
- D. Denormalise the tables into one wide table
- E. Cluster the table on the filter column

### 35. A data scientist needs a notebook runtime with project IAM and warehouse access. What should be used?

- A. Load the extract into a notebook and work in pandas
- B. Upload a CSV extract into the notebook and analyse it there
- C. Keep the dataset on the analyst workstation
- D. Analyse the data in a Colab Enterprise notebook

### 36. A notebook cell must return a DataFrame from a warehouse query without leaving the page. What should be used?

- A. Export the query result to a spreadsheet for the business team
- B. Query BigQuery from the notebook with the %%bigquery magic
- C. Upload a CSV extract into the notebook and analyse it there
- D. Load the extract into a notebook and work in pandas

### 37. Two teams report different totals for the same metric because each wrote its own SUM. What should be done?

- A. Turn off the result cache to force a fresh read
- B. Select every column to be safe
- C. Export the query result to a spreadsheet for the business team
- D. Add a LookML measure for the calculation

### 38. A regional manager will never open the analytics tool but needs the numbers each Monday. What should be done?

- A. Share the dashboard with a scheduled delivery
- B. Document the steps and have an analyst run them each morning
- C. Export the query result to a spreadsheet for the business team
- D. Turn off the result cache to force a fresh read

### 39. Finance needs a dashboard whose definitions and access rules cannot be edited per tile. What should be used?

- A. Load the extract into a notebook and work in pandas
- B. Build a governed Looker dashboard
- C. Build a Looker Studio report
- D. Export the query result to a spreadsheet for the business team

### 40. A new sales dashboard must reuse the governed model and restrict each seller to their own rows. Which two components apply? Select two.

- A. Expose the table through a LookML explore
- B. Turn off the result cache to force a fresh read
- C. Export the query result to a spreadsheet for the business team
- D. Build a Looker Studio report
- E. Build a governed Looker dashboard

### 41. A dashboard must show the same definition of active customer that finance already uses. What should be used?

- A. Build a Looker Studio report
- B. Export the query result to a spreadsheet for the business team
- C. Add a LookML measure for the calculation
- D. Change the LookML parameter in the view

### 42. A small team wants a quick report over one sheet and one table with no modelling effort. What should be used?

- A. Orchestrate the steps in Cloud Composer
- B. Build a Looker Studio report
- C. Change the LookML parameter in the view
- D. Build a governed Looker dashboard

### 43. Forty reports must share row-level access rules and one certified definition. What should be used?

- A. Build a Looker Studio report
- B. Share the dashboard with a scheduled delivery
- C. Export the query result to a spreadsheet for the business team
- D. Build a governed Looker dashboard

### 44. A single setting must change how every dashboard filters its data. What should be changed?

- A. Share the dashboard with a scheduled delivery
- B. Add a LookML measure for the calculation
- C. Change the LookML parameter in the view
- D. Turn off the result cache to force a fresh read

### 45. Report authors must be limited to defined joins and fields. What should be added?

- A. Turn off the result cache to force a fresh read
- B. Expose the table through a LookML explore
- C. Add a LookML measure for the calculation
- D. Create a BigQuery view over the join

### 46. Two changes must apply everywhere rather than to one tile. Which two belong in the model? Select two.

- A. Share the dashboard with a scheduled delivery
- B. Expose the table through a LookML explore
- C. Add a LookML measure for the calculation
- D. Export the query result to a spreadsheet for the business team
- E. Turn off the result cache to force a fresh read

### 47. A subscription team wants the probability that a trial converts. What should be built?

- A. Train a BigQuery ML ARIMA_PLUS model
- B. Train a BigQuery ML linear regression model
- C. Train a BigQuery ML logistic regression model
- D. Train a BigQuery ML k-means model

### 48. A retailer wants behavioural groups but has no target column. What should be built?

- A. Train an AutoML tabular model
- B. Train a BigQuery ML linear regression model
- C. Train a BigQuery ML logistic regression model
- D. Train a BigQuery ML k-means model

### 49. The quarterly plan needs a revenue forecast and a churn flag. Which two model types apply? Select two.

- A. Train an AutoML tabular model
- B. Train a BigQuery ML ARIMA_PLUS model
- C. Train a BigQuery ML logistic regression model
- D. Generate the forecast with ML.FORECAST
- E. Train a BigQuery ML k-means model

### 50. Support transcripts must be summarised per row without leaving the warehouse. What should be used?

- A. Land the data as newline-delimited JSON
- B. Fine-tune a Gemini model from the warehouse rows
- C. Load the extract into a notebook and work in pandas
- D. Create a BigQuery remote model over a Gemini model

### 51. A remote model fails because the warehouse has no identity to call the endpoint. What should be created?

- A. Load the rows with a client library from the application
- B. Create the BigQuery connection that reaches the model endpoint
- C. Load the files with the bq load command
- D. Stream the rows with the BigQuery Storage Write API

### 52. A team is about to train without agreeing on the data, the metric, or the acceptance test. What should be done first?

- A. Document the steps and have an analyst run them each morning
- B. Ship the model once the training loss looks good
- C. Plan collection, training, evaluation, then prediction
- D. Transform on the source system before the export starts

### 53. The model scores 0.99 on the rows it learned from and the team is ready to ship. What was skipped?

- A. Hold out a labelled split before training
- B. Denormalise the tables into one wide table
- C. Ship the model once the training loss looks good
- D. Evaluate the model with ML.EVALUATE

### 54. The risk committee wants precision and recall before launch. What should be used?

- A. Score the rows with ML.PREDICT
- B. Evaluate the model with ML.EVALUATE
- C. Generate the forecast with ML.FORECAST
- D. Explain the prediction with ML.EXPLAIN_PREDICT

### 55. A facilities team must predict next month's energy cost per site. Which model type fits?

- A. Train a BigQuery ML k-means model
- B. Train a BigQuery ML linear regression model
- C. Train a BigQuery ML logistic regression model
- D. Land the data as CSV

### 56. Last night's orders must be scored and written to a table. What should be used?

- A. Generate the forecast with ML.FORECAST
- B. Explain the prediction with ML.EXPLAIN_PREDICT
- C. Evaluate the model with ML.EVALUATE
- D. Score the rows with ML.PREDICT

### 57. A deployment must name a specific model version rather than a storage path. What should be done?

- A. Export the query result to a spreadsheet for the business team
- B. Keep the dataset on the analyst workstation
- C. Stream the rows with the BigQuery Storage Write API
- D. Register the model version in Model Registry

---

## Domain 3 — Data Pipeline Orchestration (Streaming, Scheduling, Modelling, and Recovery)

### 58. A team already owns forty PySpark jobs and the files are large. What should be used?

- A. Build the pipeline in Dataflow
- B. Manage the SQL transformations in Dataform
- C. Run the transformation as Spark on Dataproc
- D. Build the pipeline in Cloud Data Fusion

### 59. The same cleanup logic must run on a stream and on a nightly batch. What should be used?

- A. Build the pipeline in Dataflow
- B. Run the transformation as Spark on Dataproc
- C. Orchestrate the steps in Cloud Composer
- D. Sequence the API calls with Workflows

### 60. A pipeline must be assembled visually by analysts who do not write code. What should be used?

- A. Run a cron job on a Compute Engine instance
- B. Run the transformation as Spark on Dataproc
- C. Manage the SQL transformations in Dataform
- D. Build the pipeline in Cloud Data Fusion

### 61. One team writes SQL transformations and another ships Spark jobs. Which two tools fit? Select two.

- A. Manage the SQL transformations in Dataform
- B. Document the steps and have an analyst run them each morning
- C. Run the handler as a Cloud Functions function
- D. Run the transformation as Spark on Dataproc
- E. Run a cron job on a Compute Engine instance

### 62. The transformation must be re-runnable without extracting the source again. Which design fits?

- A. Query the source system in place with a federated query
- B. Load the raw rows, then transform them inside the warehouse
- C. Transform on the source system before the export starts
- D. Extract, transform outside the warehouse, then load the result

### 63. A partner will not accept raw records and demands a cleansed file. Which design fits?

- A. Load the raw rows, then transform them inside the warehouse
- B. Extract, transform outside the warehouse, then load the result
- C. Stream the rows with the BigQuery Storage Write API
- D. Land the extract in a staging table before any transform runs

### 64. One SQL statement must run at 05:00 and write its result to a table. What should be used?

- A. Schedule the SQL with a BigQuery scheduled query
- B. Sequence the API calls with Workflows
- C. Submit the job through a Dataproc workflow template
- D. Trigger the job from Cloud Scheduler

### 65. A job that is not a single query must be called every hour by an HTTP request. What should be used?

- A. Orchestrate the steps in Cloud Composer
- B. Schedule the SQL with a BigQuery scheduled query
- C. Sequence the API calls with Workflows
- D. Trigger the job from Cloud Scheduler

### 66. A nightly load must run unattended and must page someone when it fails. Which two components apply? Select two.

- A. Document the steps and have an analyst run them each morning
- B. Schedule the SQL with a BigQuery scheduled query
- C. Run a cron job on a Compute Engine instance
- D. Turn off the result cache to force a fresh read
- E. Create a Cloud Monitoring alert policy on the job metric

### 67. One step of a streaming pipeline is falling behind and the others are idle. Where should the team look first?

- A. Turn off the result cache to force a fresh read
- B. Write a SQL query in BigQuery and save the result
- C. Query the job logs in Logs Explorer
- D. Watch the job graph and per-step throughput in the Dataflow console

### 68. A pipeline drops malformed records and nobody can see what was lost. What should be added?

- A. Load first and fix the rejected rows afterwards
- B. Write the rejected rows to a dead-letter table
- C. Select every column to be safe
- D. Export the query result to a spreadsheet for the business team

### 69. Workers restart every few minutes and the reason is only in the job logs. Where should the team look?

- A. Write a SQL query in BigQuery and save the result
- B. Query the job logs in Logs Explorer
- C. Turn off the result cache to force a fresh read
- D. Share the dashboard with a scheduled delivery

### 70. Nobody notices a pipeline failure until a report is empty the next morning. What should be added?

- A. Turn off the result cache to force a fresh read
- B. Query the job logs in Logs Explorer
- C. Create a Cloud Monitoring alert policy on the job metric
- D. Document the steps and have an analyst run them each morning

### 71. A chain must wait for a partner file, then a warehouse load, then a deploy, with retries. What should orchestrate it?

- A. Orchestrate the steps in Cloud Composer
- B. Schedule the SQL with a BigQuery scheduled query
- C. Run a cron job on a Compute Engine instance
- D. Sequence the API calls with Workflows

### 72. Three service calls must run in order with no server to operate. What should be used?

- A. Run a cron job on a Compute Engine instance
- B. Sequence the API calls with Workflows
- C. Orchestrate the steps in Cloud Composer
- D. Run the handler as a Cloud Functions function

### 73. A nightly run must wait for a partner file and then submit a Spark job identically each time. Which two components apply? Select two.

- A. Orchestrate the steps in Cloud Composer
- B. Turn off the result cache to force a fresh read
- C. Submit the job through a Dataproc workflow template
- D. Document the steps and have an analyst run them each morning
- E. Run a cron job on a Compute Engine instance

### 74. Published order events must appear in a table as they arrive. What should be used?

- A. Subscribe BigQuery to the Pub/Sub topic
- B. Start the pipeline from an Eventarc trigger
- C. Schedule the SQL with a BigQuery scheduled query
- D. Load the files with the bq load command

### 75. A newly landed object in a bucket must start the pipeline immediately. What should be used?

- A. Trigger the job from Cloud Scheduler
- B. Start the pipeline from an Eventarc trigger
- C. Schedule the SQL with a BigQuery scheduled query
- D. Subscribe BigQuery to the Pub/Sub topic

---

## Domain 4 — Data Management (Warehouse Analytics, Orchestration, and Key Management)

### 76. An analyst needs to read one dataset and nothing else. What should be granted?

- A. Grant the predefined role that matches the task
- B. Grant the role to the whole domain
- C. Grant the basic Owner role to the team
- D. Make the bucket public so the partner can read it

### 77. A scheduled job must act without borrowing a person's identity. What should be used?

- A. Grant the role to the whole domain
- B. Grant the basic Owner role to the team
- C. Issue a signed URL with a short expiry
- D. Run the job as a dedicated service account

### 78. Two practices keep a data grant minimal and attributable. Which two apply? Select two.

- A. Grant the role to the whole domain
- B. Grant the predefined role that matches the task
- C. Run the job as a dedicated service account
- D. Make the bucket public so the partner can read it
- E. Grant the basic Owner role to the team

### 79. No Google-managed role matches the exact permission set the team uses. What should be created?

- A. Assign a predefined role to the group
- B. Grant the basic Owner role to the team
- C. Grant the role to the whole domain
- D. Create a custom role with only the permissions used

### 80. A team asks for Owner because it is the only role they recognise. What should be granted instead?

- A. Assign a predefined role to the group
- B. Grant the basic Owner role to the team
- C. Create a custom role with only the permissions used
- D. Make the bucket public so the partner can read it

### 81. Per-object ACLs have made the bucket impossible to audit. What should be enabled?

- A. Make the bucket public so the partner can read it
- B. Enable uniform bucket-level access
- C. Issue a signed URL with a short expiry
- D. Manage per-object ACLs on the bucket

### 82. A partner needs to read one object for the next four hours. What should be issued?

- A. Make the bucket public so the partner can read it
- B. Enable uniform bucket-level access
- C. Issue a signed URL with a short expiry
- D. Export the table to a bucket the partner owns

### 83. Six business units need one curated dataset and the publisher must keep control. What should be used?

- A. Issue a signed URL with a short expiry
- B. Export the table to a bucket the partner owns
- C. Make the bucket public so the partner can read it
- D. Publish the dataset through Analytics Hub

### 84. A partner insists on holding their own copy offline for a year. What should be done?

- A. Issue a signed URL with a short expiry
- B. Export the table to a bucket the partner owns
- C. Add the project to a VPC Service Controls perimeter
- D. Publish the dataset through Analytics Hub

### 85. Objects are read roughly once a month and stored for two years. Which class fits?

- A. Keep the objects in the Standard class
- B. Move the objects to Archive
- C. Move the objects to Nearline
- D. Enable Autoclass on the bucket

### 86. Records are read a few times a year and must stay retrievable within hours. Which class fits?

- A. Move the objects to Coldline
- B. Move the objects to Nearline
- C. Enable Autoclass on the bucket
- D. Keep the objects in the Standard class

### 87. Access patterns differ per object and the team does not want to guess a class. Which two options apply? Select two.

- A. Move the objects to Coldline
- B. Keep every version in the Standard class forever
- C. Add a lifecycle rule that changes the storage class
- D. Enable Autoclass on the bucket
- E. Leave the objects in place and review them next year

### 88. Objects older than ninety days must disappear without anyone remembering. What should be added?

- A. Keep every version in the Standard class forever
- B. Set a table expiration on the dataset
- C. Leave the objects in place and review them next year
- D. Add a lifecycle rule that deletes objects after the retention period

### 89. A table keeps three years of rows but only ninety days are queried. What should be set?

- A. Leave the objects in place and review them next year
- B. Add a lifecycle rule that deletes objects after the retention period
- C. Set a partition expiration on the table
- D. Set a table expiration on the dataset

### 90. Seven years of invoices must be retained at the lowest storage cost and read almost never. Which class fits?

- A. Export the query result to a spreadsheet for the business team
- B. Move the objects to Nearline
- C. Keep the objects in the Standard class
- D. Move the objects to Archive

### 91. The compliance officer must be able to prove that no one can delete the archive early. What should be applied?

- A. Leave the objects in place and review them next year
- B. Enable object versioning on the bucket
- C. Apply a bucket retention policy with a lock
- D. Add a lifecycle rule that deletes objects after the retention period

### 92. A database must survive a bad deploy and the loss of its region. Which two measures apply? Select two.

- A. Rely on the disk snapshot the platform keeps
- B. Create a Cloud SQL read replica in another region
- C. Deploy a single zonal instance to keep the cost down
- D. Create a multi-region bucket
- E. Enable automated backups and point-in-time recovery on Cloud SQL

### 93. The backup has run nightly for a year and has never been restored. What should be done?

- A. Rely on the disk snapshot the platform keeps
- B. Deploy a single zonal instance to keep the cost down
- C. Restore into a scratch project on a schedule
- D. Copy the bucket to a second region with a scheduled transfer

### 94. A bucket must keep a copy in a chosen pair of regions and report the replication lag. What should be used?

- A. Copy the bucket to a second region with a scheduled transfer
- B. Rely on the disk snapshot the platform keeps
- C. Create a dual-region bucket with a replication policy
- D. Create a multi-region bucket

### 95. A bucket must stay readable through the loss of any single region in a continent. What should be used?

- A. Copy the bucket to a second region with a scheduled transfer
- B. Enable object versioning on the bucket
- C. Create a dual-region bucket with a replication policy
- D. Create a multi-region bucket

### 96. The architecture document must name both a primary and a secondary region. Which location type fits?

- A. Choose a regional location
- B. Choose a multi-region location
- C. Choose a zonal resource
- D. Choose a dual-region location

### 97. The regulator requires the customer to revoke access to the data and the key must never reach Google. Which two key models apply? Select two.

- A. Put the key in the application configuration file
- B. Encrypt in the client and store the key next to the data
- C. Use the Google-managed default encryption
- D. Supply a customer-supplied key with each request
- E. Encrypt with a customer-managed key from Cloud KMS

### 98. A team has no key-management capacity and accepts the platform default. Which key model applies?

- A. Supply a customer-supplied key with each request
- B. Encrypt with a customer-managed key from Cloud KMS
- C. Put the key in the application configuration file
- D. Use the Google-managed default encryption

### 99. A control framework demands that one key version never protects new data for more than a year. What should be set?

- A. Set a rotation schedule on the key
- B. Destroy the key version to stop access immediately
- C. Use the Google-managed default encryption
- D. Put the key in the application configuration file

### 100. An auditor asks how the bytes are protected while a client reads the table. What should be confirmed?

- A. Put the key in the application configuration file
- B. Encrypt in the client and store the key next to the data
- C. Enforce TLS for every connection to the service
- D. Confirm the data is encrypted at rest by the storage service

---

## Answer key and explanations

### Question 1 — A

Answer: Extract, transform outside the warehouse, then load the result. ETL transforms the records before the load, so only curated rows reach the warehouse. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. In this case: ETL transforms the records before the load, so only curated rows reach the warehouse.
- **B:** Incorrect for this question. ETLT adds a pre-warehouse cleanup step so the warehouse transform starts from cleaner rows. Why the correct answer wins: ETL transforms the records before the load, so only curated rows reach the warehouse.
- **C:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ETL transforms the records before the load, so only curated rows reach the warehouse.
- **D:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETL transforms the records before the load, so only curated rows reach the warehouse.

### Question 2 — A

Answer: Load the raw rows, then transform them inside the warehouse. ELT keeps the raw rows and transforms them in the warehouse, so a rewrite needs no new extract. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT keeps the raw rows and transforms them in the warehouse, so a rewrite needs no new extract.
- **B:** Incorrect for this question. A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run. Why the correct answer wins: ELT keeps the raw rows and transforms them in the warehouse, so a rewrite needs no new extract.
- **C:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ELT keeps the raw rows and transforms them in the warehouse, so a rewrite needs no new extract.
- **D:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT keeps the raw rows and transforms them in the warehouse, so a rewrite needs no new extract.

### Question 3 — A, E

Answers: Load the raw rows, then transform them inside the warehouse; Land the extract in a staging table before any transform runs. ELT preserves the raw copy, and a staging table separates a failed load from a failed transform. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT preserves the raw copy, and a staging table separates a failed load from a failed transform.
- **B:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ELT preserves the raw copy, and a staging table separates a failed load from a failed transform.
- **C:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT preserves the raw copy, and a staging table separates a failed load from a failed transform.
- **D:** Incorrect for this question. A spreadsheet step is unversioned, unauditable, and cannot be scheduled, so it does not survive a second run. Why the correct answer wins: ELT preserves the raw copy, and a staging table separates a failed load from a failed transform.
- **E:** Correct. In this case: ELT preserves the raw copy, and a staging table separates a failed load from a failed transform.

### Question 4 — D

Answer: Query the source system in place with a federated query. A federated query reads the remote source in place, which suits a one-off look. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Local study-map skill 1.1 (ETL, ELT, and ETLT Methodologies), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: A federated query reads the remote source in place, which suits a one-off look.
- **B:** Incorrect for this question. A staging table separates a failed load from a failed transform, so each can be retried on its own. Why the correct answer wins: A federated query reads the remote source in place, which suits a one-off look.
- **C:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: A federated query reads the remote source in place, which suits a one-off look.
- **D:** Correct. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. In this case: A federated query reads the remote source in place, which suits a one-off look.

### Question 5 — D

Answer: Deduplicate on the business key in the cleaning step. Deduplicating on a stable business key removes the rows that retries created. Retries and restatements create duplicate rows unless the load deduplicates on a stable key. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: Deduplicating on a stable business key removes the rows that retries created.
- **B:** Incorrect for this question. A profile quantifies what is missing before the gaps reach a dashboard. Why the correct answer wins: Deduplicating on a stable business key removes the rows that retries created.
- **C:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: Deduplicating on a stable business key removes the rows that retries created.
- **D:** Correct. Retries and restatements create duplicate rows unless the load deduplicates on a stable key. In this case: Deduplicating on a stable business key removes the rows that retries created.

### Question 6 — A

Answer: Profile the columns to measure the null rate before loading. A column profile quantifies the gaps before they reach a report. A profile quantifies what is missing before the gaps reach a dashboard. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A profile quantifies what is missing before the gaps reach a dashboard. In this case: A column profile quantifies the gaps before they reach a report.
- **B:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A column profile quantifies the gaps before they reach a report.
- **C:** Incorrect for this question. SQL inside the warehouse removes duplicates, trims values, and casts types where the data already sits. Why the correct answer wins: A column profile quantifies the gaps before they reach a report.
- **D:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A column profile quantifies the gaps before they reach a report.

### Question 7 — B, E

Answers: Compare the row count with the source after every load; Compare the source checksum with the delivered file. A row-count reconciliation catches a truncated extract, and a checksum proves the bytes arrived unchanged. A row-count reconciliation catches a truncated or duplicated extract. A checksum proves the bytes arrived unchanged rather than merely arrived. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A profile quantifies what is missing before the gaps reach a dashboard. Why the correct answer wins: A row-count reconciliation catches a truncated extract, and a checksum proves the bytes arrived unchanged.
- **B:** Correct. A row-count reconciliation catches a truncated or duplicated extract. In this case: A row-count reconciliation catches a truncated extract, and a checksum proves the bytes arrived unchanged.
- **C:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A row-count reconciliation catches a truncated extract, and a checksum proves the bytes arrived unchanged.
- **D:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A row-count reconciliation catches a truncated extract, and a checksum proves the bytes arrived unchanged.
- **E:** Correct. A checksum proves the bytes arrived unchanged rather than merely arrived. In this case: A row-count reconciliation catches a truncated extract, and a checksum proves the bytes arrived unchanged.

### Question 8 — C

Answer: Cast the columns to the declared types before the load. An explicit cast turns a silent type drift into a load-time failure. Local study-map skill 1.2 (Data Quality Assessment and Cleaning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: An explicit cast turns a silent type drift into a load-time failure.
- **B:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: An explicit cast turns a silent type drift into a load-time failure.
- **C:** Correct. In this case: An explicit cast turns a silent type drift into a load-time failure.
- **D:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: An explicit cast turns a silent type drift into a load-time failure.

### Question 9 — C

Answer: Order a Transfer Appliance. A Transfer Appliance ships the data physically when the wire is too slow for the deadline. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Why the correct answer wins: A Transfer Appliance ships the data physically when the wire is too slow for the deadline.
- **B:** Incorrect for this question. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Why the correct answer wins: A Transfer Appliance ships the data physically when the wire is too slow for the deadline.
- **C:** Correct. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. In this case: A Transfer Appliance ships the data physically when the wire is too slow for the deadline.
- **D:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: A Transfer Appliance ships the data physically when the wire is too slow for the deadline.

### Question 10 — C

Answer: Use Storage Transfer Service. Storage Transfer Service copies from another cloud on a schedule and records what moved. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: Storage Transfer Service copies from another cloud on a schedule and records what moved.
- **B:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: Storage Transfer Service copies from another cloud on a schedule and records what moved.
- **C:** Correct. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. In this case: Storage Transfer Service copies from another cloud on a schedule and records what moved.
- **D:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: Storage Transfer Service copies from another cloud on a schedule and records what moved.

### Question 11 — B

Answer: Use BigQuery Data Transfer Service. BigQuery Data Transfer Service schedules recurring loads from SaaS sources. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: BigQuery Data Transfer Service schedules recurring loads from SaaS sources.
- **B:** Correct. In this case: BigQuery Data Transfer Service schedules recurring loads from SaaS sources.
- **C:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: BigQuery Data Transfer Service schedules recurring loads from SaaS sources.
- **D:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: BigQuery Data Transfer Service schedules recurring loads from SaaS sources.

### Question 12 — B, E

Answers: Use Database Migration Service; Replicate the changes with Datastream. Database Migration Service performs the initial move, and Datastream streams the changes afterwards. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. Local study-map skill 1.3 (Transfer Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A Transfer Appliance ships the data physically when the network path would take longer than the deadline. Why the correct answer wins: Database Migration Service performs the initial move, and Datastream streams the changes afterwards.
- **B:** Correct. Database Migration Service moves a live relational database with continuous replication into Cloud SQL or Spanner. In this case: Database Migration Service performs the initial move, and Datastream streams the changes afterwards.
- **C:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: Database Migration Service performs the initial move, and Datastream streams the changes afterwards.
- **D:** Incorrect for this question. BigQuery Data Transfer Service schedules recurring loads from SaaS sources and other Google services. Why the correct answer wins: Database Migration Service performs the initial move, and Datastream streams the changes afterwards.
- **E:** Correct. Datastream captures change data from a source database and streams it without a bulk copy of the whole table. In this case: Database Migration Service performs the initial move, and Datastream streams the changes afterwards.

### Question 13 — C

Answer: Land the data as Parquet. Parquet is columnar, so a scan reads only the columns the query needs. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. XML nests well and is verbose, which makes it a poor fit for wide analytical scans. Why the correct answer wins: Parquet is columnar, so a scan reads only the columns the query needs.
- **B:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: Parquet is columnar, so a scan reads only the columns the query needs.
- **C:** Correct. In this case: Parquet is columnar, so a scan reads only the columns the query needs.
- **D:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Parquet is columnar, so a scan reads only the columns the query needs.

### Question 14 — B

Answer: Land the data as Avro. Avro embeds the schema with the records, so a reader can interpret them without an external contract. Avro carries its schema with the records and suits row-oriented streaming exchanges. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. XML nests well and is verbose, which makes it a poor fit for wide analytical scans. Why the correct answer wins: Avro embeds the schema with the records, so a reader can interpret them without an external contract.
- **B:** Correct. Avro carries its schema with the records and suits row-oriented streaming exchanges. In this case: Avro embeds the schema with the records, so a reader can interpret them without an external contract.
- **C:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Avro embeds the schema with the records, so a reader can interpret them without an external contract.
- **D:** Incorrect for this question. ORC is another columnar format; choosing it adds a conversion step without a benefit over Parquet here. Why the correct answer wins: Avro embeds the schema with the records, so a reader can interpret them without an external contract.

### Question 15 — A

Answer: Land the data as CSV. CSV is plain text with no schema, which is exactly the constraint the partner imposed. CSV is readable everywhere and carries no types, no schema, and no nesting. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. CSV is readable everywhere and carries no types, no schema, and no nesting. In this case: CSV is plain text with no schema, which is exactly the constraint the partner imposed.
- **B:** Incorrect for this question. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Why the correct answer wins: CSV is plain text with no schema, which is exactly the constraint the partner imposed.
- **C:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: CSV is plain text with no schema, which is exactly the constraint the partner imposed.
- **D:** Incorrect for this question. Avro carries its schema with the records and suits row-oriented streaming exchanges. Why the correct answer wins: CSV is plain text with no schema, which is exactly the constraint the partner imposed.

### Question 16 — A, B

Answers: Land the data as Avro; Land the data as Parquet. Avro carries the schema for the row-oriented writer, and Parquet serves the columnar scan. Avro carries its schema with the records and suits row-oriented streaming exchanges. Parquet is columnar and compressed, so a scan reads only the columns a query needs. Local study-map skill 1.4 (Data Formats), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Parquet is columnar and compressed, so a scan reads only the columns a query needs. In this case: Avro carries the schema for the row-oriented writer, and Parquet serves the columnar scan.
- **B:** Correct. Avro carries its schema with the records and suits row-oriented streaming exchanges. In this case: Avro carries the schema for the row-oriented writer, and Parquet serves the columnar scan.
- **C:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Avro carries the schema for the row-oriented writer, and Parquet serves the columnar scan.
- **D:** Incorrect for this question. ORC is another columnar format; choosing it adds a conversion step without a benefit over Parquet here. Why the correct answer wins: Avro carries the schema for the row-oriented writer, and Parquet serves the columnar scan.
- **E:** Incorrect for this question. XML nests well and is verbose, which makes it a poor fit for wide analytical scans. Why the correct answer wins: Avro carries the schema for the row-oriented writer, and Parquet serves the columnar scan.

### Question 17 — A

Answer: Load the files with the bq load command. A load job reads the objects in the bucket and writes them into a table. The bq load command creates a load job that reads files from Cloud Storage into a table. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. The bq load command creates a load job that reads files from Cloud Storage into a table. In this case: A load job reads the objects in the bucket and writes them into a table.
- **B:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: A load job reads the objects in the bucket and writes them into a table.
- **C:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: A load job reads the objects in the bucket and writes them into a table.
- **D:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A load job reads the objects in the bucket and writes them into a table.

### Question 18 — A

Answer: Stream the rows with the BigQuery Storage Write API. The Storage Write API commits rows at high rate straight from the producing stream. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. The Storage Write API commits rows at high rate when a stream, not a file, produces them. In this case: The Storage Write API commits rows at high rate straight from the producing stream.
- **B:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: The Storage Write API commits rows at high rate straight from the producing stream.
- **C:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: The Storage Write API commits rows at high rate straight from the producing stream.
- **D:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: The Storage Write API commits rows at high rate straight from the producing stream.

### Question 19 — B

Answer: Build the pipeline in Cloud Data Fusion. Data Fusion expresses the extraction and cleanup steps in a versioned visual pipeline. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Local study-map skill 1.5 (Extraction Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Data Fusion expresses the extraction and cleanup steps in a versioned visual pipeline.
- **B:** Correct. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. In this case: Data Fusion expresses the extraction and cleanup steps in a versioned visual pipeline.
- **C:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Data Fusion expresses the extraction and cleanup steps in a versioned visual pipeline.
- **D:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Data Fusion expresses the extraction and cleanup steps in a versioned visual pipeline.

### Question 20 — A

Answer: Store the rows in Bigtable. Bigtable gives low-latency reads and very high write rates keyed by one row key. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. In this case: Bigtable gives low-latency reads and very high write rates keyed by one row key.
- **B:** Incorrect for this question. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. Why the correct answer wins: Bigtable gives low-latency reads and very high write rates keyed by one row key.
- **C:** Incorrect for this question. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Why the correct answer wins: Bigtable gives low-latency reads and very high write rates keyed by one row key.
- **D:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: Bigtable gives low-latency reads and very high write rates keyed by one row key.

### Question 21 — C

Answer: Store the records in Spanner. Spanner gives strongly consistent relational transactions across regions. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: Spanner gives strongly consistent relational transactions across regions.
- **B:** Incorrect for this question. Firestore is a document store for application reads by key with a flexible shape. Why the correct answer wins: Spanner gives strongly consistent relational transactions across regions.
- **C:** Correct. In this case: Spanner gives strongly consistent relational transactions across regions.
- **D:** Incorrect for this question. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Why the correct answer wins: Spanner gives strongly consistent relational transactions across regions.

### Question 22 — B

Answer: Store the documents in Firestore. Firestore is a document store built for key lookups from an application. Firestore is a document store for application reads by key with a flexible shape. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud SQL is a managed relational database for transaction-shaped workloads with a fixed schema. Why the correct answer wins: Firestore is a document store built for key lookups from an application.
- **B:** Correct. Firestore is a document store for application reads by key with a flexible shape. In this case: Firestore is a document store built for key lookups from an application.
- **C:** Incorrect for this question. Cloud Storage holds objects of any shape and is the landing zone every other service can read. Why the correct answer wins: Firestore is a document store built for key lookups from an application.
- **D:** Incorrect for this question. Bigtable is a wide, sparse, low-latency store for very high write rates keyed by a single row key. Why the correct answer wins: Firestore is a document store built for key lookups from an application.

### Question 23 — A, E

Answers: Store the rows in BigQuery; Query the objects through BigLake tables. BigQuery holds the native tables, and BigLake applies warehouse access control to the objects in place. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. BigLake tables extend BigQuery access control and performance to objects that stay in Cloud Storage. Local study-map skill 1.6 (Storage Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. BigQuery holds columnar tables that a SQL engine can scan at warehouse scale. In this case: BigQuery holds the native tables, and BigLake applies warehouse access control to the objects in place.
- **B:** Incorrect for this question. AlloyDB is a managed PostgreSQL option for transaction workloads that want PostgreSQL compatibility. Why the correct answer wins: BigQuery holds the native tables, and BigLake applies warehouse access control to the objects in place.
- **C:** Incorrect for this question. Cloud Storage holds objects of any shape and is the landing zone every other service can read. Why the correct answer wins: BigQuery holds the native tables, and BigLake applies warehouse access control to the objects in place.
- **D:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: BigQuery holds the native tables, and BigLake applies warehouse access control to the objects in place.
- **E:** Correct. BigLake tables extend BigQuery access control and performance to objects that stay in Cloud Storage. In this case: BigQuery holds the native tables, and BigLake applies warehouse access control to the objects in place.

### Question 24 — B

Answer: Choose a regional location. A regional location keeps one copy in one region, which is the cheapest per gigabyte. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: A regional location keeps one copy in one region, which is the cheapest per gigabyte.
- **B:** Correct. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. In this case: A regional location keeps one copy in one region, which is the cheapest per gigabyte.
- **C:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: A regional location keeps one copy in one region, which is the cheapest per gigabyte.
- **D:** Incorrect for this question. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Why the correct answer wins: A regional location keeps one copy in one region, which is the cheapest per gigabyte.

### Question 25 — C

Answer: Choose a dual-region location. A dual-region location keeps a copy in a named pair and states the recovery point. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: A dual-region location keeps a copy in a named pair and states the recovery point.
- **B:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: A dual-region location keeps a copy in a named pair and states the recovery point.
- **C:** Correct. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. In this case: A dual-region location keeps a copy in a named pair and states the recovery point.
- **D:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: A dual-region location keeps a copy in a named pair and states the recovery point.

### Question 26 — A

Answer: Choose a multi-region location. A multi-region location spreads the copies across a geography rather than one pair. A multi-region location spreads the data across a continent-scale geography for the widest availability. Local study-map skill 1.7 (Storage Location Types), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A multi-region location spreads the data across a continent-scale geography for the widest availability. In this case: A multi-region location spreads the copies across a geography rather than one pair.
- **B:** Incorrect for this question. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Why the correct answer wins: A multi-region location spreads the copies across a geography rather than one pair.
- **C:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: A multi-region location spreads the copies across a geography rather than one pair.
- **D:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: A multi-region location spreads the copies across a geography rather than one pair.

### Question 27 — A

Answer: Treat the files as unstructured data. Images and audio have no field model, which makes them unstructured. Unstructured data has no field model at all, such as images, audio, or free documents. Local study-map skill 1.8 (Structured, Semi-Structured, and Unstructured Data), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Unstructured data has no field model at all, such as images, audio, or free documents. In this case: Images and audio have no field model, which makes them unstructured.
- **B:** Incorrect for this question. Semi-structured data has a flexible shape such as JSON, where fields vary between records. Why the correct answer wins: Images and audio have no field model, which makes them unstructured.
- **C:** Incorrect for this question. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Why the correct answer wins: Images and audio have no field model, which makes them unstructured.
- **D:** Incorrect for this question. Structured data fits a declared schema of rows and columns. Why the correct answer wins: Images and audio have no field model, which makes them unstructured.

### Question 28 — C

Answer: Treat the records as semi-structured data. Semi-structured data has a flexible shape that varies between records. Semi-structured data has a flexible shape such as JSON, where fields vary between records. Local study-map skill 1.8 (Structured, Semi-Structured, and Unstructured Data), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Structured data fits a declared schema of rows and columns. Why the correct answer wins: Semi-structured data has a flexible shape that varies between records.
- **B:** Incorrect for this question. Unstructured data has no field model at all, such as images, audio, or free documents. Why the correct answer wins: Semi-structured data has a flexible shape that varies between records.
- **C:** Correct. Semi-structured data has a flexible shape such as JSON, where fields vary between records. In this case: Semi-structured data has a flexible shape that varies between records.
- **D:** Incorrect for this question. A schema-on-read approach interprets external files when queried, so a bad file fails the query rather than the load. Why the correct answer wins: Semi-structured data has a flexible shape that varies between records.

### Question 29 — A

Answer: Copy the objects with the gcloud storage command. A gcloud storage copy moves files from the workstation into the bucket. A gcloud storage copy is the direct path for an ad hoc move between buckets. Local study-map skill 1.9 (Loading with CLIs and Client Libraries), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A gcloud storage copy is the direct path for an ad hoc move between buckets. In this case: A gcloud storage copy moves files from the workstation into the bucket.
- **B:** Incorrect for this question. Storage Transfer Service copies from another cloud, an HTTP list, or a bucket on a schedule. Why the correct answer wins: A gcloud storage copy moves files from the workstation into the bucket.
- **C:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A gcloud storage copy moves files from the workstation into the bucket.
- **D:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: A gcloud storage copy moves files from the workstation into the bucket.

### Question 30 — D

Answer: Load the rows with a client library from the application. A client library writes rows the application already holds, without staging a file. A client library suits an application that already holds the rows in memory rather than files in a bucket. Local study-map skill 1.9 (Loading with CLIs and Client Libraries), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 1 (data preparation and ingestion): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: A client library writes rows the application already holds, without staging a file.
- **B:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A client library writes rows the application already holds, without staging a file.
- **C:** Incorrect for this question. A gcloud storage copy is the direct path for an ad hoc move between buckets. Why the correct answer wins: A client library writes rows the application already holds, without staging a file.
- **D:** Correct. A client library suits an application that already holds the rows in memory rather than files in a bucket. In this case: A client library writes rows the application already holds, without staging a file.

### Question 31 — A

Answer: Write a SQL query in BigQuery and save the result. A saved SQL query answers the question and can be re-run or scheduled. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A saved SQL query answers the question and can be re-run or scheduled.
- **B:** Incorrect for this question. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. Why the correct answer wins: A saved SQL query answers the question and can be re-run or scheduled.
- **C:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A saved SQL query answers the question and can be re-run or scheduled.
- **D:** Incorrect for this question. A view stores the query rather than the rows, so the answer stays current at query time. Why the correct answer wins: A saved SQL query answers the question and can be re-run or scheduled.

### Question 32 — B

Answer: Create a BigQuery view over the join. A view stores the query rather than the rows, so the answer is current at read time. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An external table reads the objects where they sit and does not copy them into storage. Why the correct answer wins: A view stores the query rather than the rows, so the answer is current at read time.
- **B:** Correct. In this case: A view stores the query rather than the rows, so the answer is current at read time.
- **C:** Incorrect for this question. A materialized view stores the result and refreshes it, which trades storage for repeat-query speed. Why the correct answer wins: A view stores the query rather than the rows, so the answer is current at read time.
- **D:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: A view stores the query rather than the rows, so the answer is current at read time.

### Question 33 — C

Answer: Create a BigQuery materialized view. A materialized view stores the result and refreshes it, which trades storage for speed. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A view stores the query rather than the rows, so the answer stays current at query time. Why the correct answer wins: A materialized view stores the result and refreshes it, which trades storage for speed.
- **B:** Incorrect for this question. A native table gives the warehouse its own copy and the best scan performance. Why the correct answer wins: A materialized view stores the result and refreshes it, which trades storage for speed.
- **C:** Correct. In this case: A materialized view stores the result and refreshes it, which trades storage for speed.
- **D:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: A materialized view stores the result and refreshes it, which trades storage for speed.

### Question 34 — B, E

Answers: Filter the query on the partition column; Cluster the table on the filter column. A partition filter restricts the scan, and clustering co-locates the values it filters on. A partition filter restricts the scan to the partitions the query needs. Clustering co-locates similar values so a filtered query reads fewer blocks. Local study-map skill 2.1 (BigQuery SQL for Reporting), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A partition filter restricts the scan, and clustering co-locates the values it filters on.
- **B:** Correct. A partition filter restricts the scan to the partitions the query needs. In this case: A partition filter restricts the scan, and clustering co-locates the values it filters on.
- **C:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A partition filter restricts the scan, and clustering co-locates the values it filters on.
- **D:** Incorrect for this question. A wide table removes the join, at the cost of duplicated rows and a wider scan. Why the correct answer wins: A partition filter restricts the scan, and clustering co-locates the values it filters on.
- **E:** Correct. Clustering co-locates similar values so a filtered query reads fewer blocks. In this case: A partition filter restricts the scan, and clustering co-locates the values it filters on.

### Question 35 — D

Answer: Analyse the data in a Colab Enterprise notebook. Colab Enterprise provides a managed runtime inside the project. Colab Enterprise gives a managed notebook runtime with project IAM and BigQuery access. Local study-map skill 2.2 (Colab Enterprise and Jupyter Notebooks), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: Colab Enterprise provides a managed runtime inside the project.
- **B:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: Colab Enterprise provides a managed runtime inside the project.
- **C:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Colab Enterprise provides a managed runtime inside the project.
- **D:** Correct. Colab Enterprise gives a managed notebook runtime with project IAM and BigQuery access. In this case: Colab Enterprise provides a managed runtime inside the project.

### Question 36 — B

Answer: Query BigQuery from the notebook with the %%bigquery magic. The BigQuery magic runs the SQL and hands back a DataFrame. The magic returns a DataFrame from a SQL statement inside the notebook cell. Local study-map skill 2.2 (Colab Enterprise and Jupyter Notebooks), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: The BigQuery magic runs the SQL and hands back a DataFrame.
- **B:** Correct. The magic returns a DataFrame from a SQL statement inside the notebook cell. In this case: The BigQuery magic runs the SQL and hands back a DataFrame.
- **C:** Incorrect for this question. A local extract leaves the governed table behind and cannot be reproduced from the notebook alone. Why the correct answer wins: The BigQuery magic runs the SQL and hands back a DataFrame.
- **D:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: The BigQuery magic runs the SQL and hands back a DataFrame.

### Question 37 — D

Answer: Add a LookML measure for the calculation. A measure declares the aggregation once, so both reports compute the same number. A measure declares the aggregation once so every report computes it the same way. Local study-map skill 2.3 (Business Question Analysis), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A measure declares the aggregation once, so both reports compute the same number.
- **B:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A measure declares the aggregation once, so both reports compute the same number.
- **C:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A measure declares the aggregation once, so both reports compute the same number.
- **D:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: A measure declares the aggregation once, so both reports compute the same number.

### Question 38 — A

Answer: Share the dashboard with a scheduled delivery. A scheduled delivery pushes the answer to someone who will not open the tool. Local study-map skill 2.3 (Business Question Analysis), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A scheduled delivery pushes the answer to someone who will not open the tool.
- **B:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A scheduled delivery pushes the answer to someone who will not open the tool.
- **C:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A scheduled delivery pushes the answer to someone who will not open the tool.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A scheduled delivery pushes the answer to someone who will not open the tool.

### Question 39 — B

Answer: Build a governed Looker dashboard. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: A Looker dashboard reads the modelled layer, so every tile obeys the same definitions.
- **B:** Correct. In this case: A Looker dashboard reads the modelled layer, so every tile obeys the same definitions.
- **C:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: A Looker dashboard reads the modelled layer, so every tile obeys the same definitions.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A Looker dashboard reads the modelled layer, so every tile obeys the same definitions.

### Question 40 — A, E

Answers: Build a governed Looker dashboard; Expose the table through a LookML explore. The Looker dashboard reads the model, and the explore defines the fields and the access path. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. An explore defines which joins and fields a report author may use. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. An explore defines which joins and fields a report author may use. In this case: The Looker dashboard reads the model, and the explore defines the fields and the access path.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The Looker dashboard reads the model, and the explore defines the fields and the access path.
- **C:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: The Looker dashboard reads the model, and the explore defines the fields and the access path.
- **D:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: The Looker dashboard reads the model, and the explore defines the fields and the access path.
- **E:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: The Looker dashboard reads the model, and the explore defines the fields and the access path.

### Question 41 — C

Answer: Add a LookML measure for the calculation. A shared measure keeps one definition across every report. A measure declares the aggregation once so every report computes it the same way. Local study-map skill 2.4 (Looker Dashboards), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: A shared measure keeps one definition across every report.
- **B:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A shared measure keeps one definition across every report.
- **C:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: A shared measure keeps one definition across every report.
- **D:** Incorrect for this question. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Why the correct answer wins: A shared measure keeps one definition across every report.

### Question 42 — B

Answer: Build a Looker Studio report. Looker Studio is the fast self-serve surface for a handful of sources. Looker Studio is the fast self-serve reporting surface for a small number of sources. Local study-map skill 2.5 (Looker and Looker Studio Comparison), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Looker Studio is the fast self-serve surface for a handful of sources.
- **B:** Correct. Looker Studio is the fast self-serve reporting surface for a small number of sources. In this case: Looker Studio is the fast self-serve surface for a handful of sources.
- **C:** Incorrect for this question. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Why the correct answer wins: Looker Studio is the fast self-serve surface for a handful of sources.
- **D:** Incorrect for this question. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Why the correct answer wins: Looker Studio is the fast self-serve surface for a handful of sources.

### Question 43 — D

Answer: Build a governed Looker dashboard. Looker serves many governed reports from one model with consistent access. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. Local study-map skill 2.5 (Looker and Looker Studio Comparison), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Looker Studio is the fast self-serve reporting surface for a small number of sources. Why the correct answer wins: Looker serves many governed reports from one model with consistent access.
- **B:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: Looker serves many governed reports from one model with consistent access.
- **C:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: Looker serves many governed reports from one model with consistent access.
- **D:** Correct. A Looker dashboard reads the modelled layer, so every tile obeys the same definitions and access rules. In this case: Looker serves many governed reports from one model with consistent access.

### Question 44 — C

Answer: Change the LookML parameter in the view. A LookML parameter changes the model for every consumer, not one tile. A LookML parameter changes the model for every dashboard that uses it rather than one tile. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: A LookML parameter changes the model for every consumer, not one tile.
- **B:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: A LookML parameter changes the model for every consumer, not one tile.
- **C:** Correct. A LookML parameter changes the model for every dashboard that uses it rather than one tile. In this case: A LookML parameter changes the model for every consumer, not one tile.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A LookML parameter changes the model for every consumer, not one tile.

### Question 45 — B

Answer: Expose the table through a LookML explore. An explore declares which joins and fields a report author may use. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: An explore declares which joins and fields a report author may use.
- **B:** Correct. In this case: An explore declares which joins and fields a report author may use.
- **C:** Incorrect for this question. A measure declares the aggregation once so every report computes it the same way. Why the correct answer wins: An explore declares which joins and fields a report author may use.
- **D:** Incorrect for this question. A view stores the query rather than the rows, so the answer stays current at query time. Why the correct answer wins: An explore declares which joins and fields a report author may use.

### Question 46 — B, C

Answers: Add a LookML measure for the calculation; Expose the table through a LookML explore. A shared measure fixes the aggregation, and an explore controls the joins authors may use. A measure declares the aggregation once so every report computes it the same way. An explore defines which joins and fields a report author may use. Local study-map skill 2.6 (LookML Parameters), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: A shared measure fixes the aggregation, and an explore controls the joins authors may use.
- **B:** Correct. An explore defines which joins and fields a report author may use. In this case: A shared measure fixes the aggregation, and an explore controls the joins authors may use.
- **C:** Correct. A measure declares the aggregation once so every report computes it the same way. In this case: A shared measure fixes the aggregation, and an explore controls the joins authors may use.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A shared measure fixes the aggregation, and an explore controls the joins authors may use.
- **E:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: A shared measure fixes the aggregation, and an explore controls the joins authors may use.

### Question 47 — C

Answer: Train a BigQuery ML logistic regression model. Logistic regression predicts a binary outcome and trains with SQL. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ARIMA_PLUS forecasts a series and returns an interval per period. Why the correct answer wins: Logistic regression predicts a binary outcome and trains with SQL.
- **B:** Incorrect for this question. Linear regression predicts a continuous value and trains with SQL against the table. Why the correct answer wins: Logistic regression predicts a binary outcome and trains with SQL.
- **C:** Correct. In this case: Logistic regression predicts a binary outcome and trains with SQL.
- **D:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: Logistic regression predicts a binary outcome and trains with SQL.

### Question 48 — D

Answer: Train a BigQuery ML k-means model. K-means groups rows without a label, which is what a segmentation question needs. K-means groups rows without a label column, so it segments rather than predicts. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. AutoML searches architectures and tuning for a team that has labels but no modelling code. Why the correct answer wins: K-means groups rows without a label, which is what a segmentation question needs.
- **B:** Incorrect for this question. Linear regression predicts a continuous value and trains with SQL against the table. Why the correct answer wins: K-means groups rows without a label, which is what a segmentation question needs.
- **C:** Incorrect for this question. Logistic regression predicts a binary outcome and trains with SQL against the table. Why the correct answer wins: K-means groups rows without a label, which is what a segmentation question needs.
- **D:** Correct. K-means groups rows without a label column, so it segments rather than predicts. In this case: K-means groups rows without a label, which is what a segmentation question needs.

### Question 49 — B, C

Answers: Train a BigQuery ML ARIMA_PLUS model; Train a BigQuery ML logistic regression model. ARIMA_PLUS forecasts a series, and logistic regression returns the churn probability. ARIMA_PLUS forecasts a series and returns an interval per period. Logistic regression predicts a binary outcome and trains with SQL against the table. Local study-map skill 2.7 (BigQuery ML and AutoML Use Cases), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. AutoML searches architectures and tuning for a team that has labels but no modelling code. Why the correct answer wins: ARIMA_PLUS forecasts a series, and logistic regression returns the churn probability.
- **B:** Correct. ARIMA_PLUS forecasts a series and returns an interval per period. In this case: ARIMA_PLUS forecasts a series, and logistic regression returns the churn probability.
- **C:** Correct. Logistic regression predicts a binary outcome and trains with SQL against the table. In this case: ARIMA_PLUS forecasts a series, and logistic regression returns the churn probability.
- **D:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: ARIMA_PLUS forecasts a series, and logistic regression returns the churn probability.
- **E:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: ARIMA_PLUS forecasts a series, and logistic regression returns the churn probability.

### Question 50 — D

Answer: Create a BigQuery remote model over a Gemini model. A remote model sends the prompt from SQL while the rows stay in BigQuery. Local study-map skill 2.8 (Remote Gemini Models in BigQuery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Newline-delimited JSON keeps nested fields and can be appended one record at a time. Why the correct answer wins: A remote model sends the prompt from SQL while the rows stay in BigQuery.
- **B:** Incorrect for this question. Fine-tuning adapts the model to the domain using labelled rows that stay in BigQuery. Why the correct answer wins: A remote model sends the prompt from SQL while the rows stay in BigQuery.
- **C:** Incorrect for this question. A notebook copy of the extract is outside the governed table and cannot be reproduced later. Why the correct answer wins: A remote model sends the prompt from SQL while the rows stay in BigQuery.
- **D:** Correct. In this case: A remote model sends the prompt from SQL while the rows stay in BigQuery.

### Question 51 — B

Answer: Create the BigQuery connection that reaches the model endpoint. The connection carries the service account that reaches the model endpoint. The connection carries the service account that BigQuery uses to call the remote model. Local study-map skill 2.8 (Remote Gemini Models in BigQuery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A client library suits an application that already holds the rows in memory rather than files in a bucket. Why the correct answer wins: The connection carries the service account that reaches the model endpoint.
- **B:** Correct. The connection carries the service account that BigQuery uses to call the remote model. In this case: The connection carries the service account that reaches the model endpoint.
- **C:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: The connection carries the service account that reaches the model endpoint.
- **D:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: The connection carries the service account that reaches the model endpoint.

### Question 52 — C

Answer: Plan collection, training, evaluation, then prediction. A plan fixes the data, the metric, and the acceptance test before any training runs. A planned sequence fixes the data, the metric, and the acceptance test before any model is trained. Local study-map skill 2.9 (ML Project Planning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: A plan fixes the data, the metric, and the acceptance test before any training runs.
- **B:** Incorrect for this question. Training loss measures fit to the rows it has already seen, not the answer on new rows. Why the correct answer wins: A plan fixes the data, the metric, and the acceptance test before any training runs.
- **C:** Correct. A planned sequence fixes the data, the metric, and the acceptance test before any model is trained. In this case: A plan fixes the data, the metric, and the acceptance test before any training runs.
- **D:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: A plan fixes the data, the metric, and the acceptance test before any training runs.

### Question 53 — A

Answer: Hold out a labelled split before training. A held-out split is the only way to estimate the answer on unseen rows. A held-out split gives an estimate that the training rows cannot inflate. Local study-map skill 2.9 (ML Project Planning), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A held-out split gives an estimate that the training rows cannot inflate. In this case: A held-out split is the only way to estimate the answer on unseen rows.
- **B:** Incorrect for this question. A wide table removes the join, at the cost of duplicated rows and a wider scan. Why the correct answer wins: A held-out split is the only way to estimate the answer on unseen rows.
- **C:** Incorrect for this question. Training loss measures fit to the rows it has already seen, not the answer on new rows. Why the correct answer wins: A held-out split is the only way to estimate the answer on unseen rows.
- **D:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: A held-out split is the only way to estimate the answer on unseen rows.

### Question 54 — B

Answer: Evaluate the model with ML.EVALUATE. ML.EVALUATE returns the model metrics against a labelled dataset. Local study-map skill 2.10 (BigQuery ML Training and Evaluation), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.PREDICT applies a trained model to new rows and returns the prediction. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.
- **B:** Correct. In this case: ML.EVALUATE returns the model metrics against a labelled dataset.
- **C:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.
- **D:** Incorrect for this question. ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.

### Question 55 — B

Answer: Train a BigQuery ML linear regression model. Linear regression predicts a continuous value such as a cost. Linear regression predicts a continuous value and trains with SQL against the table. Local study-map skill 2.10 (BigQuery ML Training and Evaluation), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. K-means groups rows without a label column, so it segments rather than predicts. Why the correct answer wins: Linear regression predicts a continuous value such as a cost.
- **B:** Correct. Linear regression predicts a continuous value and trains with SQL against the table. In this case: Linear regression predicts a continuous value such as a cost.
- **C:** Incorrect for this question. Logistic regression predicts a binary outcome and trains with SQL against the table. Why the correct answer wins: Linear regression predicts a continuous value such as a cost.
- **D:** Incorrect for this question. CSV is readable everywhere and carries no types, no schema, and no nesting. Why the correct answer wins: Linear regression predicts a continuous value such as a cost.

### Question 56 — D

Answer: Score the rows with ML.PREDICT. ML.PREDICT applies the trained model to the new rows. Local study-map skill 2.11 (BigQuery ML Inference), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ML.FORECAST returns future periods and their intervals from a time series model. Why the correct answer wins: ML.PREDICT applies the trained model to the new rows.
- **B:** Incorrect for this question. ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row. Why the correct answer wins: ML.PREDICT applies the trained model to the new rows.
- **C:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: ML.PREDICT applies the trained model to the new rows.
- **D:** Correct. In this case: ML.PREDICT applies the trained model to the new rows.

### Question 57 — D

Answer: Register the model version in Model Registry. Model Registry keeps versions with lineage so a deployment can name one. Model Registry keeps each version with its lineage so a deployment names a version rather than a path. Local study-map skill 2.12 (Model Registry), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 2 (data analysis and presentation): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: Model Registry keeps versions with lineage so a deployment can name one.
- **B:** Incorrect for this question. A workstation copy has no shared access control, no durability promise, and no audit trail. Why the correct answer wins: Model Registry keeps versions with lineage so a deployment can name one.
- **C:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: Model Registry keeps versions with lineage so a deployment can name one.
- **D:** Correct. Model Registry keeps each version with its lineage so a deployment names a version rather than a path. In this case: Model Registry keeps versions with lineage so a deployment can name one.

### Question 58 — C

Answer: Run the transformation as Spark on Dataproc. Dataproc runs the Spark code the team already maintains. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Dataflow runs the same code for streaming and batch and scales the workers with the load. Why the correct answer wins: Dataproc runs the Spark code the team already maintains.
- **B:** Incorrect for this question. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. Why the correct answer wins: Dataproc runs the Spark code the team already maintains.
- **C:** Correct. Dataproc runs Spark or Hadoop jobs when the team already owns that code. In this case: Dataproc runs the Spark code the team already maintains.
- **D:** Incorrect for this question. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Why the correct answer wins: Dataproc runs the Spark code the team already maintains.

### Question 59 — A

Answer: Build the pipeline in Dataflow. Dataflow runs one pipeline definition for both streaming and batch input. Dataflow runs the same code for streaming and batch and scales the workers with the load. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Dataflow runs the same code for streaming and batch and scales the workers with the load. In this case: Dataflow runs one pipeline definition for both streaming and batch input.
- **B:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Dataflow runs one pipeline definition for both streaming and batch input.
- **C:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Dataflow runs one pipeline definition for both streaming and batch input.
- **D:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Dataflow runs one pipeline definition for both streaming and batch input.

### Question 60 — D

Answer: Build the pipeline in Cloud Data Fusion. Data Fusion expresses the steps on a canvas and keeps them in a versioned definition. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Data Fusion expresses the steps on a canvas and keeps them in a versioned definition.
- **B:** Incorrect for this question. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Why the correct answer wins: Data Fusion expresses the steps on a canvas and keeps them in a versioned definition.
- **C:** Incorrect for this question. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. Why the correct answer wins: Data Fusion expresses the steps on a canvas and keeps them in a versioned definition.
- **D:** Correct. Data Fusion expresses a pipeline visually and keeps the transformation in a versioned definition. In this case: Data Fusion expresses the steps on a canvas and keeps them in a versioned definition.

### Question 61 — A, D

Answers: Manage the SQL transformations in Dataform; Run the transformation as Spark on Dataproc. Dataform manages the SQL graph, and Dataproc runs the Spark jobs. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. Dataproc runs Spark or Hadoop jobs when the team already owns that code. Local study-map skill 3.1 (Transformation Tool Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Dataform versions the ELT SQL, resolves dependencies, and runs the graph inside the warehouse. In this case: Dataform manages the SQL graph, and Dataproc runs the Spark jobs.
- **B:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Dataform manages the SQL graph, and Dataproc runs the Spark jobs.
- **C:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Dataform manages the SQL graph, and Dataproc runs the Spark jobs.
- **D:** Correct. Dataproc runs Spark or Hadoop jobs when the team already owns that code. In this case: Dataform manages the SQL graph, and Dataproc runs the Spark jobs.
- **E:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Dataform manages the SQL graph, and Dataproc runs the Spark jobs.

### Question 62 — B

Answer: Load the raw rows, then transform them inside the warehouse. ELT keeps the raw rows so the transform can be rewritten and re-run. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Local study-map skill 3.2 (ELT and ETL Pipeline Design), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A federated query reads the remote source without copying it, which suits a one-off look rather than a repeatable load. Why the correct answer wins: ELT keeps the raw rows so the transform can be rewritten and re-run.
- **B:** Correct. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. In this case: ELT keeps the raw rows so the transform can be rewritten and re-run.
- **C:** Incorrect for this question. Transforming on the source loads the source with work and removes the raw evidence from the target. Why the correct answer wins: ELT keeps the raw rows so the transform can be rewritten and re-run.
- **D:** Incorrect for this question. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Why the correct answer wins: ELT keeps the raw rows so the transform can be rewritten and re-run.

### Question 63 — B

Answer: Extract, transform outside the warehouse, then load the result. ETL cleans the records before the target store ever sees them. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. Local study-map skill 3.2 (ELT and ETL Pipeline Design), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. ELT keeps the raw copy and uses the warehouse engine to transform it, so the transform can be re-run without another extract. Why the correct answer wins: ETL cleans the records before the target store ever sees them.
- **B:** Correct. ETL cleans and reshapes records before they ever land in the target store, so the warehouse only holds curated rows. In this case: ETL cleans the records before the target store ever sees them.
- **C:** Incorrect for this question. The Storage Write API commits rows at high rate when a stream, not a file, produces them. Why the correct answer wins: ETL cleans the records before the target store ever sees them.
- **D:** Incorrect for this question. A staging table separates a failed load from a failed transform, so each can be retried on its own. Why the correct answer wins: ETL cleans the records before the target store ever sees them.

### Question 64 — A

Answer: Schedule the SQL with a BigQuery scheduled query. A scheduled query runs one statement on a cron schedule. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A scheduled query runs one statement on a cron schedule.
- **B:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **C:** Incorrect for this question. A workflow template defines the cluster and the steps so the same job can be re-run identically. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.
- **D:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: A scheduled query runs one statement on a cron schedule.

### Question 65 — D

Answer: Trigger the job from Cloud Scheduler. Cloud Scheduler calls the endpoint on the schedule. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Cloud Scheduler calls the endpoint on the schedule.
- **B:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Cloud Scheduler calls the endpoint on the schedule.
- **C:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Cloud Scheduler calls the endpoint on the schedule.
- **D:** Correct. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. In this case: Cloud Scheduler calls the endpoint on the schedule.

### Question 66 — B, E

Answers: Schedule the SQL with a BigQuery scheduled query; Create a Cloud Monitoring alert policy on the job metric. The scheduled query runs the load, and the alert policy pages an owner on failure. A scheduled query runs one statement on a cron schedule and writes its result. An alert policy pages someone when the backlog or the failure rate crosses a threshold. Local study-map skill 3.3 (Scheduled Queries and Job Scheduling), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: The scheduled query runs the load, and the alert policy pages an owner on failure.
- **B:** Correct. A scheduled query runs one statement on a cron schedule and writes its result. In this case: The scheduled query runs the load, and the alert policy pages an owner on failure.
- **C:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: The scheduled query runs the load, and the alert policy pages an owner on failure.
- **D:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The scheduled query runs the load, and the alert policy pages an owner on failure.
- **E:** Correct. An alert policy pages someone when the backlog or the failure rate crosses a threshold. In this case: The scheduled query runs the load, and the alert policy pages an owner on failure.

### Question 67 — D

Answer: Watch the job graph and per-step throughput in the Dataflow console. The Dataflow job view shows the running graph and the step that is backlogged. Local study-map skill 3.4 (Dataflow Job Monitoring), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: The Dataflow job view shows the running graph and the step that is backlogged.
- **B:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: The Dataflow job view shows the running graph and the step that is backlogged.
- **C:** Incorrect for this question. Logs Explorer filters the log entries that explain why a worker restarted. Why the correct answer wins: The Dataflow job view shows the running graph and the step that is backlogged.
- **D:** Correct. In this case: The Dataflow job view shows the running graph and the step that is backlogged.

### Question 68 — B

Answer: Write the rejected rows to a dead-letter table. A dead-letter table preserves the rejected rows for repair and replay. A dead-letter table preserves the rows that failed so they can be repaired and replayed. Local study-map skill 3.4 (Dataflow Job Monitoring), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Loading before validation lets bad rows reach the consumers who read the table. Why the correct answer wins: A dead-letter table preserves the rejected rows for repair and replay.
- **B:** Correct. A dead-letter table preserves the rows that failed so they can be repaired and replayed. In this case: A dead-letter table preserves the rejected rows for repair and replay.
- **C:** Incorrect for this question. Selecting every column scans columns the report never uses and raises the cost. Why the correct answer wins: A dead-letter table preserves the rejected rows for repair and replay.
- **D:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: A dead-letter table preserves the rejected rows for repair and replay.

### Question 69 — B

Answer: Query the job logs in Logs Explorer. Logs Explorer filters the entries that explain why a worker restarted. Local study-map skill 3.5 (Logs and Monitoring Review), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A saved SQL query answers a business question and can be scheduled or exported. Why the correct answer wins: Logs Explorer filters the entries that explain why a worker restarted.
- **B:** Correct. In this case: Logs Explorer filters the entries that explain why a worker restarted.
- **C:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: Logs Explorer filters the entries that explain why a worker restarted.
- **D:** Incorrect for this question. A scheduled delivery pushes the answer to people who will not open the tool. Why the correct answer wins: Logs Explorer filters the entries that explain why a worker restarted.

### Question 70 — C

Answer: Create a Cloud Monitoring alert policy on the job metric. An alert policy on the job metric pages an owner when the run fails. An alert policy pages someone when the backlog or the failure rate crosses a threshold. Local study-map skill 3.5 (Logs and Monitoring Review), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: An alert policy on the job metric pages an owner when the run fails.
- **B:** Incorrect for this question. Logs Explorer filters the log entries that explain why a worker restarted. Why the correct answer wins: An alert policy on the job metric pages an owner when the run fails.
- **C:** Correct. An alert policy pages someone when the backlog or the failure rate crosses a threshold. In this case: An alert policy on the job metric pages an owner when the run fails.
- **D:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: An alert policy on the job metric pages an owner when the run fails.

### Question 71 — A

Answer: Orchestrate the steps in Cloud Composer. Cloud Composer runs an Airflow DAG with dependencies and retries. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: Cloud Composer runs an Airflow DAG with dependencies and retries.
- **B:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: Cloud Composer runs an Airflow DAG with dependencies and retries.
- **C:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Cloud Composer runs an Airflow DAG with dependencies and retries.
- **D:** Incorrect for this question. Workflows chains service calls and HTTP endpoints without running a server. Why the correct answer wins: Cloud Composer runs an Airflow DAG with dependencies and retries.

### Question 72 — B

Answer: Sequence the API calls with Workflows. Workflows chains service calls and endpoints without a server. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Workflows chains service calls and endpoints without a server.
- **B:** Correct. In this case: Workflows chains service calls and endpoints without a server.
- **C:** Incorrect for this question. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. Why the correct answer wins: Workflows chains service calls and endpoints without a server.
- **D:** Incorrect for this question. A Cloud Functions function handles a single event without a cluster to operate. Why the correct answer wins: Workflows chains service calls and endpoints without a server.

### Question 73 — A, C

Answers: Orchestrate the steps in Cloud Composer; Submit the job through a Dataproc workflow template. Composer holds the dependency and the retry, and the workflow template reproduces the Spark job. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. A workflow template defines the cluster and the steps so the same job can be re-run identically. Local study-map skill 3.6 (Orchestration Solution Selection), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. Cloud Composer runs an Airflow DAG with retries, dependencies, and cross-system waits. In this case: Composer holds the dependency and the retry, and the workflow template reproduces the Spark job.
- **B:** Incorrect for this question. Disabling the cache makes every read hit the table, which costs more and slows the dashboard. Why the correct answer wins: Composer holds the dependency and the retry, and the workflow template reproduces the Spark job.
- **C:** Correct. A workflow template defines the cluster and the steps so the same job can be re-run identically. In this case: Composer holds the dependency and the retry, and the workflow template reproduces the Spark job.
- **D:** Incorrect for this question. A runbook depends on a person being present and leaves no execution record. Why the correct answer wins: Composer holds the dependency and the retry, and the workflow template reproduces the Spark job.
- **E:** Incorrect for this question. A single VM cron job has no managed retry and fails silently when the instance is restarted. Why the correct answer wins: Composer holds the dependency and the retry, and the workflow template reproduces the Spark job.

### Question 74 — A

Answer: Subscribe BigQuery to the Pub/Sub topic. A BigQuery subscription writes each message into the table on arrival. Local study-map skill 3.7 (Event-Driven Ingestion with Pub/Sub), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A BigQuery subscription writes each message into the table on arrival.
- **B:** Incorrect for this question. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Why the correct answer wins: A BigQuery subscription writes each message into the table on arrival.
- **C:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: A BigQuery subscription writes each message into the table on arrival.
- **D:** Incorrect for this question. The bq load command creates a load job that reads files from Cloud Storage into a table. Why the correct answer wins: A BigQuery subscription writes each message into the table on arrival.

### Question 75 — B

Answer: Start the pipeline from an Eventarc trigger. An Eventarc trigger routes the object event to the pipeline target. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. Local study-map skill 3.8 (Eventarc Triggers), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 3 (data pipeline orchestration): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Cloud Scheduler calls an endpoint on a schedule, which suits a job that is not a single query. Why the correct answer wins: An Eventarc trigger routes the object event to the pipeline target.
- **B:** Correct. An Eventarc trigger routes an event such as an object finalise to a Cloud Run or Workflows target. In this case: An Eventarc trigger routes the object event to the pipeline target.
- **C:** Incorrect for this question. A scheduled query runs one statement on a cron schedule and writes its result. Why the correct answer wins: An Eventarc trigger routes the object event to the pipeline target.
- **D:** Incorrect for this question. A BigQuery subscription writes each published message into a table as it arrives. Why the correct answer wins: An Eventarc trigger routes the object event to the pipeline target.

### Question 76 — A

Answer: Grant the predefined role that matches the task. The predefined role for that task carries the permissions the job needs and no more. A predefined role carries the permissions for one job and nothing else. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A predefined role carries the permissions for one job and nothing else. In this case: The predefined role for that task carries the permissions the job needs and no more.
- **B:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: The predefined role for that task carries the permissions the job needs and no more.
- **C:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: The predefined role for that task carries the permissions the job needs and no more.
- **D:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: The predefined role for that task carries the permissions the job needs and no more.

### Question 77 — D

Answer: Run the job as a dedicated service account. A service account gives the workload its own identity. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A service account gives the workload its own identity.
- **B:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A service account gives the workload its own identity.
- **C:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: A service account gives the workload its own identity.
- **D:** Correct. In this case: A service account gives the workload its own identity.

### Question 78 — B, C

Answers: Grant the predefined role that matches the task; Run the job as a dedicated service account. A role scoped to the task limits what it can do, and a dedicated identity records who did it. A predefined role carries the permissions for one job and nothing else. A service account gives the workload its own identity instead of borrowing a person's. Local study-map skill 4.1 (IAM Least Privilege), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A role scoped to the task limits what it can do, and a dedicated identity records who did it.
- **B:** Correct. A predefined role carries the permissions for one job and nothing else. In this case: A role scoped to the task limits what it can do, and a dedicated identity records who did it.
- **C:** Correct. A service account gives the workload its own identity instead of borrowing a person's. In this case: A role scoped to the task limits what it can do, and a dedicated identity records who did it.
- **D:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A role scoped to the task limits what it can do, and a dedicated identity records who did it.
- **E:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A role scoped to the task limits what it can do, and a dedicated identity records who did it.

### Question 79 — D

Answer: Create a custom role with only the permissions used. A custom role narrows the grant to the permissions in use. A custom role narrows the grant when no predefined role matches the job exactly. Local study-map skill 4.2 (Basic, Predefined, and Custom Roles), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A predefined role is maintained by Google and covers one service or one job function. Why the correct answer wins: A custom role narrows the grant to the permissions in use.
- **B:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A custom role narrows the grant to the permissions in use.
- **C:** Incorrect for this question. A domain-wide grant reaches every identity in the organisation, including the ones that never needed it. Why the correct answer wins: A custom role narrows the grant to the permissions in use.
- **D:** Correct. A custom role narrows the grant when no predefined role matches the job exactly. In this case: A custom role narrows the grant to the permissions in use.

### Question 80 — A

Answer: Assign a predefined role to the group. A predefined role for the job function avoids the breadth of a basic role. A predefined role is maintained by Google and covers one service or one job function. Local study-map skill 4.2 (Basic, Predefined, and Custom Roles), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. A predefined role is maintained by Google and covers one service or one job function. In this case: A predefined role for the job function avoids the breadth of a basic role.
- **B:** Incorrect for this question. A basic role spans every service, so it grants far more than the task needs. Why the correct answer wins: A predefined role for the job function avoids the breadth of a basic role.
- **C:** Incorrect for this question. A custom role narrows the grant when no predefined role matches the job exactly. Why the correct answer wins: A predefined role for the job function avoids the breadth of a basic role.
- **D:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A predefined role for the job function avoids the breadth of a basic role.

### Question 81 — B

Answer: Enable uniform bucket-level access. Uniform bucket-level access replaces object ACLs with IAM on the bucket. Local study-map skill 4.3 (Cloud Storage Access Control), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: Uniform bucket-level access replaces object ACLs with IAM on the bucket.
- **B:** Correct. In this case: Uniform bucket-level access replaces object ACLs with IAM on the bucket.
- **C:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Uniform bucket-level access replaces object ACLs with IAM on the bucket.
- **D:** Incorrect for this question. Per-object ACLs are hard to audit and are overridden when uniform access is enabled. Why the correct answer wins: Uniform bucket-level access replaces object ACLs with IAM on the bucket.

### Question 82 — C

Answer: Issue a signed URL with a short expiry. A signed URL grants temporary access to one object without changing IAM. Local study-map skill 4.3 (Cloud Storage Access Control), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: A signed URL grants temporary access to one object without changing IAM.
- **B:** Incorrect for this question. Uniform bucket-level access replaces per-object ACLs with IAM on the bucket. Why the correct answer wins: A signed URL grants temporary access to one object without changing IAM.
- **C:** Correct. In this case: A signed URL grants temporary access to one object without changing IAM.
- **D:** Incorrect for this question. An export hands over a copy that the publisher can no longer control or revoke. Why the correct answer wins: A signed URL grants temporary access to one object without changing IAM.

### Question 83 — D

Answer: Publish the dataset through Analytics Hub. Analytics Hub shares the dataset in place under the publisher's policy. Analytics Hub shares a curated dataset with a subscriber who reads it in place. Local study-map skill 4.4 (Analytics Hub Data Sharing), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: Analytics Hub shares the dataset in place under the publisher's policy.
- **B:** Incorrect for this question. An export hands over a copy that the publisher can no longer control or revoke. Why the correct answer wins: Analytics Hub shares the dataset in place under the publisher's policy.
- **C:** Incorrect for this question. A public bucket exposes every object in it to anyone with the URL. Why the correct answer wins: Analytics Hub shares the dataset in place under the publisher's policy.
- **D:** Correct. Analytics Hub shares a curated dataset with a subscriber who reads it in place. In this case: Analytics Hub shares the dataset in place under the publisher's policy.

### Question 84 — B

Answer: Export the table to a bucket the partner owns. An export hands over a copy, which is what an offline requirement forces. An export hands over a copy that the publisher can no longer control or revoke. Local study-map skill 4.4 (Analytics Hub Data Sharing), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A signed URL grants temporary read access to one object without changing IAM. Why the correct answer wins: An export hands over a copy, which is what an offline requirement forces.
- **B:** Correct. An export hands over a copy that the publisher can no longer control or revoke. In this case: An export hands over a copy, which is what an offline requirement forces.
- **C:** Incorrect for this question. A perimeter blocks data movement outside the boundary even for an authorised identity. Why the correct answer wins: An export hands over a copy, which is what an offline requirement forces.
- **D:** Incorrect for this question. Analytics Hub shares a curated dataset with a subscriber who reads it in place. Why the correct answer wins: An export hands over a copy, which is what an offline requirement forces.

### Question 85 — C

Answer: Move the objects to Nearline. Nearline costs less to store and suits reads about once a month. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Nearline costs less to store and suits reads about once a month.
- **B:** Incorrect for this question. Archive is the cheapest class for data kept for compliance and read almost never. Why the correct answer wins: Nearline costs less to store and suits reads about once a month.
- **C:** Correct. In this case: Nearline costs less to store and suits reads about once a month.
- **D:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes. Why the correct answer wins: Nearline costs less to store and suits reads about once a month.

### Question 86 — A

Answer: Move the objects to Coldline. Coldline suits occasional reads with a longer minimum storage duration. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: Coldline suits occasional reads with a longer minimum storage duration.
- **B:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: Coldline suits occasional reads with a longer minimum storage duration.
- **C:** Incorrect for this question. Autoclass moves each object between classes as its access pattern changes. Why the correct answer wins: Coldline suits occasional reads with a longer minimum storage duration.
- **D:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Coldline suits occasional reads with a longer minimum storage duration.

### Question 87 — C, D

Answers: Enable Autoclass on the bucket; Add a lifecycle rule that changes the storage class. Autoclass moves each object as its access changes, and a rule demotes objects after a set number of days. Autoclass moves each object between classes as its access pattern changes. A setStorageClass rule demotes an object after a number of days so the cost falls without a copy. Local study-map skill 4.5 (Cloud Storage Classes), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Coldline suits reads a few times a year and has a longer minimum storage duration. Why the correct answer wins: Autoclass moves each object as its access changes, and a rule demotes objects after a set number of days.
- **B:** Incorrect for this question. Keeping every version in the hot class pays the highest rate for data nobody reads. Why the correct answer wins: Autoclass moves each object as its access changes, and a rule demotes objects after a set number of days.
- **C:** Correct. A setStorageClass rule demotes an object after a number of days so the cost falls without a copy. In this case: Autoclass moves each object as its access changes, and a rule demotes objects after a set number of days.
- **D:** Correct. Autoclass moves each object between classes as its access pattern changes. In this case: Autoclass moves each object as its access changes, and a rule demotes objects after a set number of days.
- **E:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: Autoclass moves each object as its access changes, and a rule demotes objects after a set number of days.

### Question 88 — D

Answer: Add a lifecycle rule that deletes objects after the retention period. A lifecycle delete rule removes the object once the period passes. A delete rule removes the objects once the retention period passes, without a person remembering. Local study-map skill 4.6 (Lifecycle Rules and Expiration), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. Keeping every version in the hot class pays the highest rate for data nobody reads. Why the correct answer wins: A lifecycle delete rule removes the object once the period passes.
- **B:** Incorrect for this question. A dataset-level expiration removes tables created in it after the configured period. Why the correct answer wins: A lifecycle delete rule removes the object once the period passes.
- **C:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: A lifecycle delete rule removes the object once the period passes.
- **D:** Correct. A delete rule removes the objects once the retention period passes, without a person remembering. In this case: A lifecycle delete rule removes the object once the period passes.

### Question 89 — C

Answer: Set a partition expiration on the table. Partition expiration drops the old partitions while the table keeps the recent ones. Local study-map skill 4.6 (Lifecycle Rules and Expiration), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: Partition expiration drops the old partitions while the table keeps the recent ones.
- **B:** Incorrect for this question. A delete rule removes the objects once the retention period passes, without a person remembering. Why the correct answer wins: Partition expiration drops the old partitions while the table keeps the recent ones.
- **C:** Correct. In this case: Partition expiration drops the old partitions while the table keeps the recent ones.
- **D:** Incorrect for this question. A dataset-level expiration removes tables created in it after the configured period. Why the correct answer wins: Partition expiration drops the old partitions while the table keeps the recent ones.

### Question 90 — D

Answer: Move the objects to Archive. Archive is the cheapest class for data kept for compliance. Local study-map skill 4.7 (Archiving Services), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An export is a snapshot that goes stale the moment it is written. Why the correct answer wins: Archive is the cheapest class for data kept for compliance.
- **B:** Incorrect for this question. Nearline costs less to store and charges for early deletion, so it suits reads about once a month. Why the correct answer wins: Archive is the cheapest class for data kept for compliance.
- **C:** Incorrect for this question. Standard is for objects read frequently, where access cost matters more than storage cost. Why the correct answer wins: Archive is the cheapest class for data kept for compliance.
- **D:** Correct. In this case: Archive is the cheapest class for data kept for compliance.

### Question 91 — C

Answer: Apply a bucket retention policy with a lock. A locked retention policy prevents deletion for the period, even by an administrator. Local study-map skill 4.7 (Archiving Services), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An ageing bucket with no rule grows without a decision about what is still needed. Why the correct answer wins: A locked retention policy prevents deletion for the period, even by an administrator.
- **B:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A locked retention policy prevents deletion for the period, even by an administrator.
- **C:** Correct. In this case: A locked retention policy prevents deletion for the period, even by an administrator.
- **D:** Incorrect for this question. A delete rule removes the objects once the retention period passes, without a person remembering. Why the correct answer wins: A locked retention policy prevents deletion for the period, even by an administrator.

### Question 92 — B, E

Answers: Enable automated backups and point-in-time recovery on Cloud SQL; Create a Cloud SQL read replica in another region. Point-in-time recovery restores the state before the deploy, and a replica can be promoted. Automated backups with point-in-time recovery restore the instance to a chosen moment. A read replica serves reads from a second region and can be promoted during a regional failure. Local study-map skill 4.8 (Backup and Recovery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: Point-in-time recovery restores the state before the deploy, and a replica can be promoted.
- **B:** Correct. A read replica serves reads from a second region and can be promoted during a regional failure. In this case: Point-in-time recovery restores the state before the deploy, and a replica can be promoted.
- **C:** Incorrect for this question. A zonal instance is lost with its zone and gives no automatic failover. Why the correct answer wins: Point-in-time recovery restores the state before the deploy, and a replica can be promoted.
- **D:** Incorrect for this question. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. Why the correct answer wins: Point-in-time recovery restores the state before the deploy, and a replica can be promoted.
- **E:** Correct. Automated backups with point-in-time recovery restore the instance to a chosen moment. In this case: Point-in-time recovery restores the state before the deploy, and a replica can be promoted.

### Question 93 — C

Answer: Restore into a scratch project on a schedule. A restore drill is the only evidence that the backup is usable. Local study-map skill 4.8 (Backup and Recovery), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: A restore drill is the only evidence that the backup is usable.
- **B:** Incorrect for this question. A zonal instance is lost with its zone and gives no automatic failover. Why the correct answer wins: A restore drill is the only evidence that the backup is usable.
- **C:** Correct. In this case: A restore drill is the only evidence that the backup is usable.
- **D:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A restore drill is the only evidence that the backup is usable.

### Question 94 — C

Answer: Create a dual-region bucket with a replication policy. A dual-region bucket keeps a copy in a named pair and reports the lag. A dual-region bucket keeps a copy in a second region and reports the replication lag. Local study-map skill 4.9 (Replication), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A dual-region bucket keeps a copy in a named pair and reports the lag.
- **B:** Incorrect for this question. An unmanaged snapshot has no restore test and no defined retention. Why the correct answer wins: A dual-region bucket keeps a copy in a named pair and reports the lag.
- **C:** Correct. A dual-region bucket keeps a copy in a second region and reports the replication lag. In this case: A dual-region bucket keeps a copy in a named pair and reports the lag.
- **D:** Incorrect for this question. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. Why the correct answer wins: A dual-region bucket keeps a copy in a named pair and reports the lag.

### Question 95 — D

Answer: Create a multi-region bucket. A multi-region bucket spreads the objects across the geography. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. Local study-map skill 4.9 (Replication), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A scheduled copy rebuilds a second copy but leaves a gap between runs. Why the correct answer wins: A multi-region bucket spreads the objects across the geography.
- **B:** Incorrect for this question. Object versioning keeps a prior generation so an overwrite or delete can be reversed. Why the correct answer wins: A multi-region bucket spreads the objects across the geography.
- **C:** Incorrect for this question. A dual-region bucket keeps a copy in a second region and reports the replication lag. Why the correct answer wins: A multi-region bucket spreads the objects across the geography.
- **D:** Correct. A multi-region bucket spreads the objects across a geography for availability rather than a named pair. In this case: A multi-region bucket spreads the objects across the geography.

### Question 96 — D

Answer: Choose a dual-region location. A dual-region location states the primary and the secondary explicitly. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. Local study-map skill 4.10 (Primary and Secondary Locations), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A regional location keeps the data in one region and is the cheapest and lowest-latency choice for one user base. Why the correct answer wins: A dual-region location states the primary and the secondary explicitly.
- **B:** Incorrect for this question. A multi-region location spreads the data across a continent-scale geography for the widest availability. Why the correct answer wins: A dual-region location states the primary and the secondary explicitly.
- **C:** Incorrect for this question. A zone is a single failure domain, so a zonal resource does not survive the loss of that zone. Why the correct answer wins: A dual-region location states the primary and the secondary explicitly.
- **D:** Correct. A dual-region location keeps two copies in a named pair of regions with a defined recovery point. In this case: A dual-region location states the primary and the secondary explicitly.

### Question 97 — D, E

Answers: Encrypt with a customer-managed key from Cloud KMS; Supply a customer-supplied key with each request. A customer-managed key can be revoked by the customer, and a customer-supplied key never leaves the client. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. A customer-supplied key never reaches Google, and losing it loses the object. Local study-map skill 4.11 (CMEK, CSEK, and GMEK), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: A customer-managed key can be revoked by the customer, and a customer-supplied key never leaves the client.
- **B:** Incorrect for this question. A key stored beside the data protects nothing against anyone who can read the store. Why the correct answer wins: A customer-managed key can be revoked by the customer, and a customer-supplied key never leaves the client.
- **C:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: A customer-managed key can be revoked by the customer, and a customer-supplied key never leaves the client.
- **D:** Correct. A customer-supplied key never reaches Google, and losing it loses the object. In this case: A customer-managed key can be revoked by the customer, and a customer-supplied key never leaves the client.
- **E:** Correct. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. In this case: A customer-managed key can be revoked by the customer, and a customer-supplied key never leaves the client.

### Question 98 — D

Answer: Use the Google-managed default encryption. Google-managed encryption needs no work from the customer and cannot be rotated by them. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Local study-map skill 4.11 (CMEK, CSEK, and GMEK), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A customer-supplied key never reaches Google, and losing it loses the object. Why the correct answer wins: Google-managed encryption needs no work from the customer and cannot be rotated by them.
- **B:** Incorrect for this question. A customer-managed key is created, rotated, and revoked by the customer while Google holds the ciphertext. Why the correct answer wins: Google-managed encryption needs no work from the customer and cannot be rotated by them.
- **C:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: Google-managed encryption needs no work from the customer and cannot be rotated by them.
- **D:** Correct. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. In this case: Google-managed encryption needs no work from the customer and cannot be rotated by them.

### Question 99 — A

Answer: Set a rotation schedule on the key. A rotation schedule limits how long one version protects new data. Local study-map skill 4.12 (Cloud KMS), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Correct. In this case: A rotation schedule limits how long one version protects new data.
- **B:** Incorrect for this question. Destroying the key makes the ciphertext permanently unreadable, including for a restore. Why the correct answer wins: A rotation schedule limits how long one version protects new data.
- **C:** Incorrect for this question. Google-managed keys need no work from the customer and cannot be rotated or revoked by them. Why the correct answer wins: A rotation schedule limits how long one version protects new data.
- **D:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: A rotation schedule limits how long one version protects new data.

### Question 100 — C

Answer: Enforce TLS for every connection to the service. Encryption in transit protects the bytes while they travel between client and service. Local study-map skill 4.13 (Encryption in Transit and at Rest), mapped to the official guide: Google Cloud Associate Data Practitioner exam guide (v1.0). Primary reference: Associate Data Practitioner exam guide, section 4 (data management): https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf.

- **A:** Incorrect for this question. A key in a configuration file is copied into every environment and every backup of that file. Why the correct answer wins: Encryption in transit protects the bytes while they travel between client and service.
- **B:** Incorrect for this question. A key stored beside the data protects nothing against anyone who can read the store. Why the correct answer wins: Encryption in transit protects the bytes while they travel between client and service.
- **C:** Correct. In this case: Encryption in transit protects the bytes while they travel between client and service.
- **D:** Incorrect for this question. Encryption at rest protects the stored bytes on the medium, not the connection that reads them. Why the correct answer wins: Encryption in transit protects the bytes while they travel between client and service.
