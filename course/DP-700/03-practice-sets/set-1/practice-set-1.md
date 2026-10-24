# Microsoft DP-700 — Full-Length Mock Exam 1

Fabric Data Engineer Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, interactive components in the Fabric portal, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A nightly notebook holds forty executors for two hours although most stages need eight. What should be enabled?

Domain: Implement and manage an analytics solution

- A. Enable dynamic allocation so idle executors are released during the run
- B. Pin the library version in the environment instead of installing it in the notebook
- C. Enable high concurrency mode for shared sessions
- D. Set a workspace-level custom Spark pool for the notebooks

### 2. A developer upgraded a library inside one notebook and every later run of that notebook fails. Which two practices apply? Select two.

Domain: Implement and manage an analytics solution

- A. Enable autoscale with a minimum and maximum node count
- B. Attach a custom Spark environment to the notebook
- C. Set the default environment at the workspace level
- D. Enable high concurrency mode for shared sessions
- E. Pin the library version in the environment instead of installing it in the notebook

### 3. Every new notebook starts without the approved libraries and the team fixes it by hand. What should be configured?

Domain: Implement and manage an analytics solution

- A. Set a workspace-level custom Spark pool for the notebooks
- B. Set the default environment at the workspace level
- C. Attach a custom Spark environment to the notebook
- D. Enable high concurrency mode for shared sessions

### 4. Analysts cannot find the four workspaces that belong to the supply chain subject area. What should be configured?

Domain: Implement and manage an analytics solution

- A. Create the workspace in the required region at creation time
- B. Keep OneLake availability enabled so other engines can read the same data
- C. Assign the workspace to a capacity that has headroom
- D. Assign the workspace to the domain that owns the subject area

### 5. A new workspace will hold data that may not leave the country. What must be decided before the workspace is created?

Domain: Implement and manage an analytics solution

- A. Assign the workspace to a capacity that has headroom
- B. Create the workspace in the required region at creation time
- C. Keep OneLake availability enabled so other engines can read the same data
- D. Assign the workspace to the domain that owns the subject area

### 6. Three heavy notebooks and a warehouse share one workspace and the nightly runs are being throttled. What should be checked first?

Domain: Implement and manage an analytics solution

- A. Assign the workspace to the domain that owns the subject area
- B. Create the workspace in the required region at creation time
- C. Assign the workspace to a capacity that has headroom
- D. Keep OneLake availability enabled so other engines can read the same data

### 7. The team already runs a Python DAG that orchestrates eleven external tasks. What should be used?

Domain: Implement and manage an analytics solution

- A. Enable the Apache Airflow job in the workspace and author the DAG
- B. Use a pipeline for the copy and the orchestration
- C. Sync the Airflow DAG from the connected Git repository
- D. Rewrite the existing orchestration as a Fabric pipeline instead

### 8. An Airflow DAG is edited directly in the workspace and no change is reviewable. What should be done?

Domain: Implement and manage an analytics solution

- A. Use a Dataflow Gen2 for the transformation
- B. Rewrite the existing orchestration as a Fabric pipeline instead
- C. Enable the Apache Airflow job in the workspace and author the DAG
- D. Sync the Airflow DAG from the connected Git repository

### 9. Two engineers edit the same pipeline in the live workspace and each overwrites the other. What should be configured?

Domain: Implement and manage an analytics solution

- A. Add the generated artefacts to the ignore file rather than committing them
- B. Work in a feature branch and merge through a pull request
- C. Connect the workspace to a Git repository and commit the item definitions
- D. Resolve the conflict by choosing the definition that must win, then commit

### 10. The warehouse schema is scripted by hand and drifts between environments. What should be created?

Domain: Implement and manage an analytics solution

- A. Use SQLCMD variables for the environment-specific values
- B. Connect the workspace to a Git repository and commit the item definitions
- C. Build the project into a DACPAC and deploy that artefact
- D. Create a database project and deploy the schema from it

### 11. One schema artefact must deploy to test and production, whose servers differ. Which two practices apply? Select two.

Domain: Implement and manage an analytics solution

- A. Work in a feature branch and merge through a pull request
- B. Create a database project and deploy the schema from it
- C. Add the generated artefacts to the ignore file rather than committing them
- D. Use SQLCMD variables for the environment-specific values
- E. Build the project into a DACPAC and deploy that artefact

### 12. A release broke the reporting model and the previous definition must come back. What should be done?

Domain: Implement and manage an analytics solution

- A. Add deployment rules so the target stage keeps its own connection and parameters
- B. Deploy backwards to recover the last known-good definition
- C. Create a deployment pipeline with development, test, and production stages
- D. Compare the stages before promoting

### 13. A finance analyst needs one report and nothing else in the workspace. What should be granted?

Domain: Implement and manage an analytics solution

- A. Share the single item with the user who needs only that item
- B. Grant Admin on the workspace to the platform team
- C. Share a link to the item with the required permission
- D. Grant the user a workspace role

### 14. A new starter must read every item in the workspace without editing anything. What should be granted?

Domain: Implement and manage an analytics solution

- A. Grant Read on the item
- B. Grant Viewer on the workspace
- C. Grant Admin on the workspace to the platform team
- D. Grant the user a workspace role

### 15. Branch managers may see only their own branch transactions. What should be defined?

Domain: Implement and manage an analytics solution

- A. Define a row-level security policy on the table
- B. Apply object-level security in the semantic model
- C. Apply column-level security so the column is hidden from the group
- D. Grant access at the folder that holds the restricted files

### 16. The salary column must stay hidden from analysts while the rest of the row stays readable. What should be applied?

Domain: Implement and manage an analytics solution

- A. Define a row-level security policy on the table
- B. Apply object-level security in the semantic model
- C. Apply column-level security so the column is hidden from the group
- D. Grant access at the individual file

### 17. A restricted folder must be closed to the analytics workspace and one table hidden from the model. Which two controls apply? Select two.

Domain: Implement and manage an analytics solution

- A. Apply object-level security in the semantic model
- B. Define a row-level security policy on the table
- C. Grant access at the individual file
- D. Grant access at the folder that holds the restricted files
- E. Apply column-level security so the column is hidden from the group

### 18. Analysts must keep querying the account table while national identifiers appear masked. What should be applied?

Domain: Implement and manage an analytics solution

- A. Apply column-level security so the column is hidden from the group
- B. Apply dynamic data masking to the column
- C. Mask the column in the report layer only
- D. Expose a view with the column omitted instead of masking it

### 19. After masking was applied, the financial crime team also sees masked identifiers. What is missing?

Domain: Implement and manage an analytics solution

- A. Expose a view with the column omitted instead of masking it
- B. Mask the column in the report layer only
- C. Apply dynamic data masking to the column
- D. Exempt the authorised group from the mask

### 20. Consumers keep copying an unreviewed table because nothing marks the reviewed one. What should be done?

Domain: Implement and manage an analytics solution

- A. Promote the item as ready for reuse
- B. Apply the sensitivity label to the item
- C. Set the default sensitivity label for the workspace
- D. Certify the item as the approved source

### 21. A finance extract must carry a classification that travels with it to every consumer. What should be applied?

Domain: Implement and manage an analytics solution

- A. Let the label inherit from the labelled source file
- B. Apply the sensitivity label to the item
- C. Promote the item as ready for reuse
- D. Certify the item as the approved source

### 22. An auditor asks who changed the customer table definition last month. Where should the answer be found?

Domain: Implement and manage an analytics solution

- A. Export the audit events before the retention window closes
- B. Filter the audit log by activity and by item
- C. Read the item activity log
- D. Read the Fabric audit log in the Microsoft Purview portal

### 23. Engineers with the Viewer role can read every lakehouse folder, including the restricted one. What should be configured?

Domain: Implement and manage an analytics solution

- A. Configure OneLake security roles for the lakehouse
- B. Scope the OneLake role to the folder that holds the restricted table
- C. Grant access at the folder that holds the restricted files
- D. Grant the OneLake role to a security group rather than to individuals

### 24. Data access must be governed independently of the workspace role and maintained once for a team. Which two practices apply? Select two.

Domain: Implement and manage an analytics solution

- A. Grant the user a workspace role
- B. Configure OneLake security roles for the lakehouse
- C. Grant the OneLake role to a security group rather than to individuals
- D. Scope the OneLake role to the folder that holds the restricted table
- E. Grant access at the folder that holds the restricted files

### 25. A run must copy a file and then start a notebook in that order. What should be used?

Domain: Implement and manage an analytics solution

- A. Use a notebook for the transformation
- B. Use a pipeline for the copy and the orchestration
- C. Use a T-SQL script against the warehouse
- D. Use a Dataflow Gen2 for the transformation

### 26. A transformation is a set of joins that the analysts already know how to express in Power Query. What should be used?

Domain: Implement and manage an analytics solution

- A. Use a notebook for the transformation
- B. Use a pipeline for the copy and the orchestration
- C. Use a Dataflow Gen2 for the transformation
- D. Use a T-SQL script against the warehouse

### 27. Extracts arrive at unpredictable times and an hourly check runs long after the file lands. What should be configured?

Domain: Implement and manage an analytics solution

- A. Add an event-based trigger so the run starts when the file arrives
- B. Add a schedule trigger with the cadence and time zone the business expects
- C. Trigger on the file-created event for the landing folder
- D. Pass the folder path as a pipeline parameter

### 28. One pipeline must serve several landing folders and start when a file arrives. Which two features apply? Select two.

Domain: Implement and manage an analytics solution

- A. Set the value in a pipeline variable and reference the variable
- B. Add an event-based trigger so the run starts when the file arrives
- C. Add a schedule trigger with the cadence and time zone the business expects
- D. Pass the folder path as a pipeline parameter
- E. Build the path with a dynamic expression at run time

### 29. A new governed workspace must be created for a subsidiary. Which sequence is correct?

Domain: Implement and manage an analytics solution

- A. Choose the capacity and region → create the workspace → assign the domain → grant the workspace roles
- B. Assign the domain → grant the roles → create the workspace → choose the capacity
- C. Create the workspace → choose the region after the first item is built → assign the domain → grant the roles
- D. Grant the workspace roles → create the workspace → choose the capacity → assign the domain

### 30. A team must move from hand-exported releases to a reviewed pipeline. Which sequence is correct?

Domain: Implement and manage an analytics solution

- A. Promote through the stages → create the deployment pipeline → commit the definitions → connect Git → add deployment rules
- B. Create the deployment pipeline → connect the workspace to Git → promote through the stages → add deployment rules → commit the definitions
- C. Connect the workspace to Git → commit the item definitions → create the deployment pipeline → add deployment rules → promote through the stages
- D. Commit the item definitions → connect the workspace to Git → add deployment rules → create the pipeline → promote the stages

### 31. A nightly load must move only new rows and must not lose a row when the run fails. Which two practices apply? Select two.

Domain: Ingest and transform data

- A. Merge the incoming rows into the target on the business key
- B. Store the last successful load timestamp in a control table
- C. Load only the rows newer than the stored watermark
- D. Deduplicate on the business key and keep the latest record
- E. Run a full load and overwrite the target

### 32. Forty rows fail validation but the remaining two million must load tonight. What should be done?

Domain: Ingest and transform data

- A. Route the failed rows to a reject table and continue the load
- B. Run a full load and overwrite the target
- C. Replace the missing value with a documented default
- D. Deduplicate on the business key and keep the latest record

### 33. Analysis must attribute last year's sales to the category the product had at the time. What should be built?

Domain: Ingest and transform data

- A. Deduplicate on the business key and keep the latest record
- B. Generate a surrogate key instead of reusing the source key
- C. Merge the incoming rows into the target on the business key
- D. Build a type 2 dimension with validity dates and a current flag

### 34. A source migration changes every product identifier in the ERP. What should the warehouse use?

Domain: Ingest and transform data

- A. Model the data as a star schema with conformed dimensions
- B. Generate a surrogate key instead of reusing the source key
- C. Build a type 2 dimension with validity dates and a current flag
- D. Merge the incoming rows into the target on the business key

### 35. A warehouse must keep facts narrow and preserve product history. Which two design choices apply? Select two.

Domain: Ingest and transform data

- A. Build a type 2 dimension with validity dates and a current flag
- B. Denormalize the model so the report needs no join
- C. Model the data as a star schema with conformed dimensions
- D. Pivot the rows into the reporting columns
- E. Union the sources after conforming the columns

### 36. A streaming job restarts and repeats every event already written. What is missing?

Domain: Ingest and transform data

- A. Store the stream in native tables in the eventhouse
- B. Set a checkpoint location for the streaming query
- C. Set a watermark so late events are handled deterministically
- D. Query the stream through a OneLake shortcut

### 37. The finance close needs multi-table transactions and a relational model. What should hold the data?

Domain: Ingest and transform data

- A. Store the telemetry in an eventhouse KQL database
- B. Create a KQL database for the time-series queries
- C. Load the curated model into the warehouse
- D. Land the extract in the lakehouse Files area

### 38. Curated Delta tables must serve T-SQL readers without a second copy. Which two capabilities apply? Select two.

Domain: Ingest and transform data

- A. Query the lakehouse through its SQL analytics endpoint
- B. Write the curated table into the lakehouse Tables area
- C. Store the telemetry in an eventhouse KQL database
- D. Load the curated model into the warehouse
- E. Land the extract in the lakehouse Files area

### 39. Analysts must maintain the transformation themselves and they do not write Python. What should be used?

Domain: Ingest and transform data

- A. Transform with Dataflow Gen2 and Power Query
- B. Transform with KQL in the eventhouse
- C. Transform with T-SQL against the warehouse
- D. Use a notebook for the transformation

### 40. The data is already relational in the warehouse and the transform is a set-based join. What should be used?

Domain: Ingest and transform data

- A. Transform with PySpark in a notebook
- B. Transform with T-SQL against the warehouse
- C. Transform with Dataflow Gen2 and Power Query
- D. Transform with KQL in the eventhouse

### 41. A second workspace must read the same table and no copy may exist. What should be created?

Domain: Ingest and transform data

- A. Create an internal OneLake shortcut to the other lakehouse table
- B. Copy the remote data into a local table instead of shortcutting it
- C. Use a Copy activity in the pipeline
- D. Create an ADLS Gen2 shortcut to the external container

### 42. Files already sit in an ADLS container the company owns. How should they appear in OneLake?

Domain: Ingest and transform data

- A. Copy the files as binary and parse them downstream
- B. Create an internal OneLake shortcut to the other lakehouse table
- C. Copy the remote data into a local table instead of shortcutting it
- D. Create an ADLS Gen2 shortcut to the external container

### 43. Store systems write to Azure SQL and analysts need near-real-time data. What should be enabled?

Domain: Ingest and transform data

- A. Enable mirroring for the operational database
- B. Run a full load and overwrite the target
- C. Use a Copy activity in the pipeline
- D. Create an internal OneLake shortcut to the other lakehouse table

### 44. The database team will not allow a read workload that competes with store transactions. What should be used?

Domain: Ingest and transform data

- A. Append the new files instead of overwriting the target
- B. Rely on change data capture so the mirror needs no pipeline schedule
- C. Create an ADLS Gen2 shortcut to the external container
- D. Mirror from a read replica so the source database keeps its capacity

### 45. Every run overwrites the target and last month's rows disappear. What should change?

Domain: Ingest and transform data

- A. Run a full load and overwrite the target
- B. Append the new files instead of overwriting the target
- C. Copy the files as binary and parse them downstream
- D. Delete the processed source file after the load succeeds

### 46. A file that already loaded is picked up again the next night. What should be added?

Domain: Ingest and transform data

- A. Copy the files as binary and parse them downstream
- B. Use Get Metadata to list the files to process
- C. Delete the processed source file after the load succeeds
- D. Append the new files instead of overwriting the target

### 47. The previous reading for each meter must appear on the same row as the current one. What should be used?

Domain: Ingest and transform data

- A. Group and aggregate to the grain the report needs
- B. Union the sources after conforming the columns
- C. Use a window function to rank within the partition
- D. Pivot the rows into the reporting columns

### 48. Row-level cleansing and a per-partition ranking must both run over a large table. Which two features apply? Select two.

Domain: Ingest and transform data

- A. Pivot the rows into the reporting columns
- B. Use a window function to rank within the partition
- C. Transform with Dataflow Gen2 and Power Query
- D. Transform with PySpark in a notebook
- E. Transform with T-SQL against the warehouse

### 49. The eventhouse table must be filtered and summarized as records arrive. What should be used?

Domain: Ingest and transform data

- A. Transform with Dataflow Gen2 and Power Query
- B. Transform with KQL in the eventhouse
- C. Transform with PySpark in a notebook
- D. Transform with T-SQL against the warehouse

### 50. A report joins six tables on every refresh and the join dominates the query time. What should be done?

Domain: Ingest and transform data

- A. Pivot the rows into the reporting columns
- B. Model the data as a star schema with conformed dimensions
- C. Denormalize the model so the report needs no join
- D. Group and aggregate to the grain the report needs

### 51. A report needs one column per month and one row per store. Which two transformations apply? Select two.

Domain: Ingest and transform data

- A. Use a window function to rank within the partition
- B. Pivot the rows into the reporting columns
- C. Union the sources after conforming the columns
- D. Group and aggregate to the grain the report needs
- E. Denormalize the model so the report needs no join

### 52. A concentrator reconnects and replays six hours of readings that were already aggregated. What should be done?

Domain: Ingest and transform data

- A. Route the failed rows to a reject table and continue the load
- B. Replace the missing value with a documented default
- C. Deduplicate on the business key and keep the latest record
- D. Reprocess the affected partitions when the data arrives late

### 53. A no-code path is needed from the event hub to a KQL table. What should be used?

Domain: Ingest and transform data

- A. Process the stream with an eventstream
- B. Process the stream with a KQL update policy
- C. Process the stream with Spark structured streaming
- D. Run a batch job every few minutes over the landing folder

### 54. A nightly incremental load must never lose a row. Which sequence is correct?

Domain: Ingest and transform data

- A. Merge into the target → read the watermark → update the watermark → extract the rows
- B. Extract the full table → merge into the target → read the watermark → update the watermark
- C. Read the watermark → extract only the rows after it → merge into the target → update the watermark
- D. Update the watermark → extract the rows → read the watermark → merge into the target

### 55. Raw files must become a curated table without losing the original. Which sequence is correct?

Domain: Ingest and transform data

- A. Validate the schema → publish the gold table → land the raw files → conform and deduplicate
- B. Land the raw files unchanged → validate the schema and reject the bad rows → conform and deduplicate into silver → publish the gold table
- C. Conform and deduplicate → land the raw files → publish the gold table → validate the schema
- D. Publish the gold table → validate the schema → land the raw files → conform and deduplicate

### 56. Every dashboard tile recomputes the same five-minute aggregate. What should be created?

Domain: Ingest and transform data

- A. Query the stream through a OneLake shortcut
- B. Create a materialized view for the repeated aggregation
- C. Use a tumbling window for the fixed five-minute aggregate
- D. Use a hopping window when the intervals must overlap

### 57. A real-time aggregate must feed an alert. Which sequence is correct?

Domain: Ingest and transform data

- A. Create the KQL table → define the source → alert on the aggregate → add the destination → build the view
- B. Add the destination → create the KQL table → build the view → define the source → alert on the aggregate
- C. Define the eventstream source → add the destination → create the KQL table → build the materialized view → alert on the aggregate
- D. Alert on the aggregate → build the materialized view → define the source → add the destination → create the KQL table

### 58. A pipeline failed overnight and the team needs the run's status and duration. Where should they look first?

Domain: Monitor and optimize an analytics solution

- A. Read the refresh history for the semantic model
- B. Send the logs to a Log Analytics workspace
- C. Read the item activity log
- D. Use the Monitoring hub for the run history

### 59. One lakehouse load needs its own run history rather than the whole tenant's. What should be read?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Read the Fabric audit log in the Microsoft Purview portal
- C. Read the refresh history for the semantic model
- D. Read the item activity log

### 60. A semantic model refresh takes longer than before and sometimes fails. What shows which?

Domain: Monitor and optimize an analytics solution

- A. Read the item activity log
- B. Send the logs to a Log Analytics workspace
- C. Read the refresh history for the semantic model
- D. Use the Monitoring hub for the run history

### 61. The team needs refresh history older than the in-product views keep. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Read the item activity log
- B. Send the logs to a Log Analytics workspace
- C. Read the Fabric audit log in the Microsoft Purview portal
- D. Read the refresh history for the semantic model

### 62. A transient failure retries successfully, and the team is paged for every attempt. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Set the alert to fire only after the retry policy has been exhausted
- B. Send the alert to the team that owns the item
- C. Alert on every successful run as well as every failure
- D. Build a real-time dashboard over the monitoring table

### 63. A Dataflow Gen2 refresh fails after a schema change upstream. Where is the failing step named?

Domain: Monitor and optimize an analytics solution

- A. Check the shortcut connection and the delegated permission
- B. Check the failing cell and the Spark driver log
- C. Read the activity output of the failed step
- D. Inspect the Dataflow Gen2 refresh error for the failing query step

### 64. A failure handler exists but never runs when the step before it fails. What should be set?

Domain: Monitor and optimize an analytics solution

- A. Add an error branch so the failure is handled rather than ignored
- B. Add a retry policy with a delay to the failing activity
- C. Set the failure dependency so the handler runs when the step fails
- D. Use an Until loop with a timeout for the long-running check

### 65. A source returns a transient timeout twice a week and succeeds on the next attempt. What should be added?

Domain: Monitor and optimize an analytics solution

- A. Set the failure dependency so the handler runs when the step fails
- B. Use an Until loop with a timeout for the long-running check
- C. Add an error branch so the failure is handled rather than ignored
- D. Add a retry policy with a delay to the failing activity

### 66. A notebook fails on one transformation and the stack names no dataframe. Where should the error be read?

Domain: Monitor and optimize an analytics solution

- A. Open the Spark UI for the application
- B. Inspect the failing cell output and exit value
- C. Check the failing cell and the Spark driver log
- D. Use the Monitoring hub for the run history

### 67. A notebook reports a serialization error that the cell output does not show. Where should the team look?

Domain: Monitor and optimize an analytics solution

- A. Check the failing cell and the Spark driver log
- B. Open the Spark UI for the application
- C. Send the logs to a Log Analytics workspace
- D. Inspect the failing cell output and exit value

### 68. A notebook fails intermittently and the cause is not in the cell output. Which two sources apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Inspect the failing cell output and exit value
- B. Check the failing cell and the Spark driver log
- C. Open the Spark UI for the application
- D. Send the logs to a Log Analytics workspace
- E. Use the Monitoring hub for the run history

### 69. A KQL table rejects part of an incoming batch. Where are the rejected records listed?

Domain: Monitor and optimize an analytics solution

- A. Query the ingestion failures table in the KQL database
- B. Inspect the eventstream runtime metrics
- C. Use the Monitoring hub for the run history
- D. Read the Fabric audit log in the Microsoft Purview portal

### 70. An eventstream delivers less than the source sends. What shows where it is blocked?

Domain: Monitor and optimize an analytics solution

- A. Query the ingestion failures table in the KQL database
- B. Use the Monitoring hub for the run history
- C. Inspect the eventstream runtime metrics
- D. Read the item activity log

### 71. A warehouse query fails after a column was renamed. What identifies the object at fault?

Domain: Monitor and optimize an analytics solution

- A. Read the activity output of the failed step
- B. Check the failing cell and the Spark driver log
- C. Check the shortcut connection and the delegated permission
- D. Read the T-SQL error message and then the query plan

### 72. A shortcut that worked yesterday now returns nothing. What should be checked first?

Domain: Monitor and optimize an analytics solution

- A. Check the failing cell and the Spark driver log
- B. Read the T-SQL error message and then the query plan
- C. Check the shortcut connection and the delegated permission
- D. Read the activity output of the failed step

### 73. A table has two hundred thousand small files after a month of incremental writes. What should be run?

Domain: Monitor and optimize an analytics solution

- A. Run OPTIMIZE to compact the small files
- B. Enable V-Order on the table
- C. Run VACUUM to remove the files the table no longer references
- D. Partition the table on the date column

### 74. A report filters on order date but the query still scans every file. What should be added?

Domain: Monitor and optimize an analytics solution

- A. Apply Z-Order on the frequently filtered columns
- B. Run OPTIMIZE to compact the small files
- C. Run VACUUM to remove the files the table no longer references
- D. Partition the table on the date column

### 75. A table has too many small files and every query filters on one date column. Which two actions apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Partition the table on the date column
- B. Enable V-Order on the table
- C. Run OPTIMIZE to compact the small files
- D. Run VACUUM to remove the files the table no longer references
- E. Apply Z-Order on the frequently filtered columns

### 76. A copy of forty independent files runs one file after another. What should be changed?

Domain: Monitor and optimize an analytics solution

- A. Coalesce the partitions before writing the small result
- B. Insert the warehouse rows in batches rather than one at a time
- C. Raise the parallelism of the copy so independent slices move together
- D. Cache the DataFrame that is used twice

### 77. A join to a small dimension shuffles the large fact and one key dominates. Which two practices apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Broadcast the small dimension to avoid the shuffle
- B. Coalesce the partitions before writing the small result
- C. Cache the DataFrame that is used twice
- D. Set the shuffle partition count to match the data volume
- E. Salt the skewed key so the partitions even out

### 78. A warehouse join moves every row between nodes before it completes. What should change?

Domain: Monitor and optimize an analytics solution

- A. Join on the distribution column so the rows stay on their node
- B. Write fewer, larger files into the warehouse table
- C. Insert the warehouse rows in batches rather than one at a time
- D. Update statistics so the optimizer sees the current distribution

### 79. A warehouse query is slow and the plan shows both a bad estimate and a reshuffle. Which two actions apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Insert the warehouse rows in batches rather than one at a time
- B. Join on the distribution column so the rows stay on their node
- C. Update statistics so the optimizer sees the current distribution
- D. Coalesce the partitions before writing the small result
- E. Write fewer, larger files into the warehouse table

### 80. One customer key holds a fifth of the rows and one task runs for an hour. What should be applied?

Domain: Monitor and optimize an analytics solution

- A. Broadcast the small dimension to avoid the shuffle
- B. Set the shuffle partition count to match the data volume
- C. Salt the skewed key so the partitions even out
- D. Keep adaptive query execution enabled so the shuffle is re-planned

### 81. A shuffle produces two hundred partitions of uneven size after a volume increase. What should be set?

Domain: Monitor and optimize an analytics solution

- A. Cache the DataFrame that is used twice
- B. Salt the skewed key so the partitions even out
- C. Set the shuffle partition count to match the data volume
- D. Broadcast the small dimension to avoid the shuffle

### 82. The same DataFrame is read by two actions and recomputed both times. What should be done?

Domain: Monitor and optimize an analytics solution

- A. Salt the skewed key so the partitions even out
- B. Coalesce the partitions before writing the small result
- C. Broadcast the small dimension to avoid the shuffle
- D. Cache the DataFrame that is used twice

### 83. Every item in the workspace is throttled at the same time each morning. What should be checked first?

Domain: Monitor and optimize an analytics solution

- A. Set the retention policy to match the query window
- B. Scale the destination throughput for the event volume
- C. Enable capacity smoothing so a burst can borrow from the burst allowance
- D. Move the workspace to a larger capacity

### 84. A burst of four nightly jobs exceeds the capacity for twenty minutes and then idles. What should be enabled?

Domain: Monitor and optimize an analytics solution

- A. Enable capacity smoothing so a burst can borrow from the burst allowance
- B. Move the workspace to a larger capacity
- C. Set the caching policy on the KQL table
- D. Set the retention policy to match the query window

### 85. An eventhouse keeps two years but every query reads the last day. Which two policies apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Set the retention policy to match the query window
- B. Scale the destination throughput for the event volume
- C. Increase the eventhouse capacity so the queries keep up
- D. Move the workspace to a larger capacity
- E. Set the caching policy on the KQL table

### 86. A slow report must be tuned with evidence. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Read the query plan → reduce the file count → optimize and Z-Order the table → re-measure the query
- B. Reduce the file count → read the plan → re-measure the query → optimize the table
- C. Optimize the table → re-measure the query → read the plan → reduce the file count
- D. Re-measure the query → optimize the table → read the plan → reduce the file count

### 87. A failed pipeline run must be fixed and rerun safely. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Read the run history → isolate the failing activity → reproduce it with the same input → rerun only the failed activity
- B. Reproduce the input → isolate the activity → read the run history → rerun the activity
- C. Rerun only the failed activity → read the run history → isolate the activity → reproduce the input
- D. Isolate the failing activity → rerun the activity → read the run history → reproduce the input

### 88. A team must stop learning about failures from its users. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Set the alert threshold → build the dashboard → review the history → enable the output
- B. Review the alert history → enable the monitoring output → set the threshold → build the dashboard
- C. Enable the monitoring output → build the dashboard over it → set the alert threshold → review the alert history each week
- D. Build the dashboard → set the threshold → enable the output → review the history

---

## Case study — Adventure Works Cycles

Adventure Works Cycles sells bicycles through 900 dealers and a direct web store. Orders, returns, and inventory snapshots arrive nightly as CSV extracts from three regional ERPs, and the files land in an ADLS Gen2 container the company already owns. The data engineering team has built a lakehouse with bronze, silver, and gold layers, and analysts read the gold tables through the SQL analytics endpoint. A nightly run takes five hours and rewrites every table in full. The finance team has asked for order history that shows what the dealer price was on the day the order was placed, not what it is today. The platform team owns a single Fabric capacity and wants every deployment to be reproducible from source control.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. A release currently means exporting and importing items by hand. What should be created?

Domain: Implement and manage an analytics solution

- A. Add deployment rules so the target stage keeps its own connection and parameters
- B. Create a deployment pipeline with development, test, and production stages
- C. Select only the items that belong in the target stage
- D. Deploy backwards to recover the last known-good definition

### 90. Finance data must carry a classification that every consumer inherits. What should be applied?

Domain: Implement and manage an analytics solution

- A. Apply the sensitivity label to the item
- B. Certify the item as the approved source
- C. Let the label inherit from the labelled source file
- D. Promote the item as ready for reuse

### 91. The restricted folder must stay unreadable to the analytics workspace and to its Contributors. Which two controls apply? Select two.

Domain: Implement and manage an analytics solution

- A. Grant access at the folder that holds the restricted files
- B. Grant the user a workspace role
- C. Grant the OneLake role to a security group rather than to individuals
- D. Scope the OneLake role to the folder that holds the restricted table
- E. Configure OneLake security roles for the lakehouse

---

## Case study — Contoso Energy

Contoso Energy operates 2.4 million smart meters and receives about 40,000 readings per second during peak hours. The readings must be queryable within two minutes of arrival for outage detection, and the regulator requires seven years of retention for daily aggregates. The company is moving from an on-premises time-series platform to Fabric Real-Time Intelligence. A separate batch process already loads billing data into a warehouse once a day. The data engineering team has one Fabric capacity and has been told not to add another. Meter identifiers arrive with occasional duplicates and readings sometimes arrive up to six hours late when a concentrator reconnects.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. Forty thousand readings per second must be queryable within two minutes. Where should they land?

Domain: Ingest and transform data

- A. Write the curated table into the lakehouse Tables area
- B. Load the curated model into the warehouse
- C. Create a KQL database for the time-series queries
- D. Store the telemetry in an eventhouse KQL database

### 93. A regulator and a dashboard both read the same daily total. What should be created?

Domain: Ingest and transform data

- A. Use a hopping window when the intervals must overlap
- B. Use a tumbling window for the fixed five-minute aggregate
- C. Query the stream through a OneLake shortcut
- D. Create a materialized view for the repeated aggregation

### 94. A concentrator reconnects six hours late with readings already counted. What should be done?

Domain: Ingest and transform data

- A. Route the failed rows to a reject table and continue the load
- B. Reprocess the affected partitions when the data arrives late
- C. Replace the missing value with a documented default
- D. Deduplicate on the business key and keep the latest record

---

## Case study — Fabrikam Logistics

Fabrikam Logistics moves 60,000 parcels a day and receives a scan event from every depot gate. Events arrive through an event hub and are currently landed as JSON files that a nightly notebook parses. Operations wants a live board of parcels stuck at a depot for more than four hours, and the finance team wants a daily invoice line for each parcel by service level. Scans are occasionally duplicated when a gate retries, and a depot that loses connectivity can replay several hours of events in a burst. The company standardises on OneLake and has four workspaces: landing, engineering, analytics, and operations. Nothing may be copied into a second storage account.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. A depot gate retries and the same scan arrives twice. What should be applied?

Domain: Ingest and transform data

- A. Replace the missing value with a documented default
- B. Reprocess the affected partitions when the data arrives late
- C. Route the failed rows to a reject table and continue the load
- D. Deduplicate on the business key and keep the latest record

### 96. Operations wants a live board with no batch job in the path. What should be used?

Domain: Ingest and transform data

- A. Process the stream with an eventstream
- B. Run a batch job every few minutes over the landing folder
- C. Process the stream with a KQL update policy
- D. Process the stream with Spark structured streaming

### 97. The daily invoice line is built from the landed events. What should be used?

Domain: Ingest and transform data

- A. Use Get Metadata to list the files to process
- B. Copy the files as binary and parse them downstream
- C. Use a Copy activity in the pipeline
- D. Append the new files instead of overwriting the target

---

## Case study — Litware Retail

Litware Retail runs 320 stores and keeps its point-of-sale transactions in an Azure SQL database that the store systems write to directly. Analysts want near-real-time sales by store, and the finance team needs a governed monthly close that reconciles to the general ledger. The database team refuses to allow any read workload that competes with store transactions. Transaction rows can be corrected after the fact when a cashier voids a sale. The company has a Fabric capacity, a purview account, and a policy that all finance data must carry a sensitivity label. The engineering team has no licence for a second database and cannot enable change tracking on the source tables.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. The reconciliation query fails with a conversion error after a schema change. What identifies the fault?

Domain: Monitor and optimize an analytics solution

- A. Read the T-SQL error message and then the query plan
- B. Read the activity output of the failed step
- C. Check the failing cell and the Spark driver log
- D. Check the shortcut connection and the delegated permission

### 99. A failed load is discovered by the finance team the next morning. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Alert on every successful run as well as every failure
- B. Configure an alert on the failing condition
- C. Send the alert to the team that owns the item
- D. Use a Data Activator rule that watches the streaming condition

### 100. The month-end join slowed sharply as the volume grew. What should be updated first?

Domain: Monitor and optimize an analytics solution

- A. Write fewer, larger files into the warehouse table
- B. Raise the parallelism of the copy so independent slices move together
- C. Join on the distribution column so the rows stay on their node
- D. Update statistics so the optimizer sees the current distribution

---

## Answer key and explanations

### Question 1 — A

Answer: Enable dynamic allocation so idle executors are released during the run. Dynamic allocation releases the executors an idle stage does not need. Dynamic allocation shrinks the executor set between stages, which matters when the stages are uneven. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Dynamic allocation shrinks the executor set between stages, which matters when the stages are uneven. In this case: Dynamic allocation releases the executors an idle stage does not need.
- **B:** Incorrect for this question. An inline install changes the dependency per notebook and makes a run impossible to reproduce. Why the correct answer wins: Dynamic allocation releases the executors an idle stage does not need.
- **C:** Incorrect for this question. High concurrency lets several notebooks share one Spark session instead of starting a session each. Why the correct answer wins: Dynamic allocation releases the executors an idle stage does not need.
- **D:** Incorrect for this question. A workspace Spark pool applies one node size and autoscale bound to every notebook that does not override it. Why the correct answer wins: Dynamic allocation releases the executors an idle stage does not need.

### Question 2 — B, E

Answers: Attach a custom Spark environment to the notebook; Pin the library version in the environment instead of installing it in the notebook. An environment holds the library set, and pinning the version keeps a run reproducible. An environment carries the library set and Spark properties, so every run starts from the same definition. An inline install changes the dependency per notebook and makes a run impossible to reproduce. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Autoscale adds executors while the job runs and releases them afterwards, so idle capacity is not billed. Why the correct answer wins: An environment holds the library set, and pinning the version keeps a run reproducible.
- **B:** Correct. An environment carries the library set and Spark properties, so every run starts from the same definition. In this case: An environment holds the library set, and pinning the version keeps a run reproducible.
- **C:** Incorrect for this question. A workspace default environment means a new notebook inherits the approved libraries without a decision. Why the correct answer wins: An environment holds the library set, and pinning the version keeps a run reproducible.
- **D:** Incorrect for this question. High concurrency lets several notebooks share one Spark session instead of starting a session each. Why the correct answer wins: An environment holds the library set, and pinning the version keeps a run reproducible.
- **E:** Correct. An inline install changes the dependency per notebook and makes a run impossible to reproduce. In this case: An environment holds the library set, and pinning the version keeps a run reproducible.

### Question 3 — B

Answer: Set the default environment at the workspace level. A workspace default environment gives a new notebook the approved libraries automatically. A workspace default environment means a new notebook inherits the approved libraries without a decision. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace Spark pool applies one node size and autoscale bound to every notebook that does not override it. Why the correct answer wins: A workspace default environment gives a new notebook the approved libraries automatically.
- **B:** Correct. A workspace default environment means a new notebook inherits the approved libraries without a decision. In this case: A workspace default environment gives a new notebook the approved libraries automatically.
- **C:** Incorrect for this question. An environment carries the library set and Spark properties, so every run starts from the same definition. Why the correct answer wins: A workspace default environment gives a new notebook the approved libraries automatically.
- **D:** Incorrect for this question. High concurrency lets several notebooks share one Spark session instead of starting a session each. Why the correct answer wins: A workspace default environment gives a new notebook the approved libraries automatically.

### Question 4 — D

Answer: Assign the workspace to the domain that owns the subject area. A domain groups the workspaces that share a subject area. A domain groups workspaces for governance and discovery without moving the data. Local study-map skill 1.2 (Domain and OneLake Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. Why the correct answer wins: A domain groups the workspaces that share a subject area.
- **B:** Incorrect for this question. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. Why the correct answer wins: A domain groups the workspaces that share a subject area.
- **C:** Incorrect for this question. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. Why the correct answer wins: A domain groups the workspaces that share a subject area.
- **D:** Correct. A domain groups workspaces for governance and discovery without moving the data. In this case: A domain groups the workspaces that share a subject area.

### Question 5 — B

Answer: Create the workspace in the required region at creation time. The region is fixed at creation, so it has to be chosen before the workspace exists. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. Local study-map skill 1.2 (Domain and OneLake Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. Why the correct answer wins: The region is fixed at creation, so it has to be chosen before the workspace exists.
- **B:** Correct. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. In this case: The region is fixed at creation, so it has to be chosen before the workspace exists.
- **C:** Incorrect for this question. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. Why the correct answer wins: The region is fixed at creation, so it has to be chosen before the workspace exists.
- **D:** Incorrect for this question. A domain groups workspaces for governance and discovery without moving the data. Why the correct answer wins: The region is fixed at creation, so it has to be chosen before the workspace exists.

### Question 6 — C

Answer: Assign the workspace to a capacity that has headroom. Every item draws on one capacity, so the capacity is the first thing to check. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. Local study-map skill 1.2 (Domain and OneLake Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A domain groups workspaces for governance and discovery without moving the data. Why the correct answer wins: Every item draws on one capacity, so the capacity is the first thing to check.
- **B:** Incorrect for this question. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. Why the correct answer wins: Every item draws on one capacity, so the capacity is the first thing to check.
- **C:** Correct. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. In this case: Every item draws on one capacity, so the capacity is the first thing to check.
- **D:** Incorrect for this question. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. Why the correct answer wins: Every item draws on one capacity, so the capacity is the first thing to check.

### Question 7 — A

Answer: Enable the Apache Airflow job in the workspace and author the DAG. The Airflow job runs the existing DAG inside Fabric without a rewrite. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. Local study-map skill 1.3 (Apache Airflow Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. In this case: The Airflow job runs the existing DAG inside Fabric without a rewrite.
- **B:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: The Airflow job runs the existing DAG inside Fabric without a rewrite.
- **C:** Incorrect for this question. Source-controlled DAGs keep the orchestration reviewable like any other item definition. Why the correct answer wins: The Airflow job runs the existing DAG inside Fabric without a rewrite.
- **D:** Incorrect for this question. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. Why the correct answer wins: The Airflow job runs the existing DAG inside Fabric without a rewrite.

### Question 8 — D

Answer: Sync the Airflow DAG from the connected Git repository. A DAG synced from Git is reviewable like any other item definition. Source-controlled DAGs keep the orchestration reviewable like any other item definition. Local study-map skill 1.3 (Apache Airflow Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: A DAG synced from Git is reviewable like any other item definition.
- **B:** Incorrect for this question. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. Why the correct answer wins: A DAG synced from Git is reviewable like any other item definition.
- **C:** Incorrect for this question. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. Why the correct answer wins: A DAG synced from Git is reviewable like any other item definition.
- **D:** Correct. Source-controlled DAGs keep the orchestration reviewable like any other item definition. In this case: A DAG synced from Git is reviewable like any other item definition.

### Question 9 — C

Answer: Connect the workspace to a Git repository and commit the item definitions. Connecting the workspace to Git puts every change through a commit. Git keeps a reviewable history of every item definition instead of an untracked live workspace. Local study-map skill 1.4 (Version Control and Database Projects), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Committing build output makes every run look like a change. Why the correct answer wins: Connecting the workspace to Git puts every change through a commit.
- **B:** Incorrect for this question. Branching keeps unfinished work out of the shared workspace and makes the change reviewable. Why the correct answer wins: Connecting the workspace to Git puts every change through a commit.
- **C:** Correct. Git keeps a reviewable history of every item definition instead of an untracked live workspace. In this case: Connecting the workspace to Git puts every change through a commit.
- **D:** Incorrect for this question. An unresolved conflict blocks the update and leaves the workspace and the branch out of step. Why the correct answer wins: Connecting the workspace to Git puts every change through a commit.

### Question 10 — C

Answer: Build the project into a DACPAC and deploy that artefact. A database project builds one schema artefact that every environment deploys. The DACPAC is the versioned schema artefact that the deployment consumes. Local study-map skill 1.4 (Version Control and Database Projects), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. SQLCMD variables keep one project artefact deployable to both test and production. Why the correct answer wins: A database project builds one schema artefact that every environment deploys.
- **B:** Incorrect for this question. Git keeps a reviewable history of every item definition instead of an untracked live workspace. Why the correct answer wins: A database project builds one schema artefact that every environment deploys.
- **C:** Correct. The DACPAC is the versioned schema artefact that the deployment consumes. In this case: A database project builds one schema artefact that every environment deploys.
- **D:** Incorrect for this question. A database project keeps the warehouse schema in source control and deploys it repeatably. Why the correct answer wins: A database project builds one schema artefact that every environment deploys.

### Question 11 — B, D

Answers: Create a database project and deploy the schema from it; Use SQLCMD variables for the environment-specific values. The database project holds the schema, and SQLCMD variables hold the environment values. A database project keeps the warehouse schema in source control and deploys it repeatably. SQLCMD variables keep one project artefact deployable to both test and production. Local study-map skill 1.4 (Version Control and Database Projects), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Branching keeps unfinished work out of the shared workspace and makes the change reviewable. Why the correct answer wins: The database project holds the schema, and SQLCMD variables hold the environment values.
- **B:** Correct. A database project keeps the warehouse schema in source control and deploys it repeatably. In this case: The database project holds the schema, and SQLCMD variables hold the environment values.
- **C:** Incorrect for this question. Committing build output makes every run look like a change. Why the correct answer wins: The database project holds the schema, and SQLCMD variables hold the environment values.
- **D:** Correct. SQLCMD variables keep one project artefact deployable to both test and production. In this case: The database project holds the schema, and SQLCMD variables hold the environment values.
- **E:** Incorrect for this question. The DACPAC is the versioned schema artefact that the deployment consumes. Why the correct answer wins: The database project holds the schema, and SQLCMD variables hold the environment values.

### Question 12 — B

Answer: Deploy backwards to recover the last known-good definition. A backward deployment restores the last known-good definition. A backward deployment is the supported way to restore a previous stage state. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A rule stops a promotion from overwriting the target stage environment-specific settings. Why the correct answer wins: A backward deployment restores the last known-good definition.
- **B:** Correct. A backward deployment is the supported way to restore a previous stage state. In this case: A backward deployment restores the last known-good definition.
- **C:** Incorrect for this question. The pipeline promotes the same item definitions through the stages instead of rebuilding them. Why the correct answer wins: A backward deployment restores the last known-good definition.
- **D:** Incorrect for this question. The comparison shows what the promotion will change in the target before it happens. Why the correct answer wins: A backward deployment restores the last known-good definition.

### Question 13 — A

Answer: Share the single item with the user who needs only that item. Item-level sharing gives exactly the item that is needed. Item-level sharing avoids granting a workspace role for one report. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Item-level sharing avoids granting a workspace role for one report. In this case: Item-level sharing gives exactly the item that is needed.
- **B:** Incorrect for this question. Admin is needed to manage access and settings, not to read the data. Why the correct answer wins: Item-level sharing gives exactly the item that is needed.
- **C:** Incorrect for this question. A link is a shortcut to the item, not a substitute for the permission behind it. Why the correct answer wins: Item-level sharing gives exactly the item that is needed.
- **D:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: Item-level sharing gives exactly the item that is needed.

### Question 14 — B

Answer: Grant Viewer on the workspace. Viewer allows reading the items without editing them. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Read is the narrowest grant that still lets the item be consumed. Why the correct answer wins: Viewer allows reading the items without editing them.
- **B:** Correct. In this case: Viewer allows reading the items without editing them.
- **C:** Incorrect for this question. Admin is needed to manage access and settings, not to read the data. Why the correct answer wins: Viewer allows reading the items without editing them.
- **D:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: Viewer allows reading the items without editing them.

### Question 15 — A

Answer: Define a row-level security policy on the table. Row-level security filters the rows per identity. Row-level security filters rows per identity, so one table returns different rows to different users. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Row-level security filters rows per identity, so one table returns different rows to different users. In this case: Row-level security filters the rows per identity.
- **B:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: Row-level security filters the rows per identity.
- **C:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: Row-level security filters the rows per identity.
- **D:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: Row-level security filters the rows per identity.

### Question 16 — C

Answer: Apply column-level security so the column is hidden from the group. Column-level security hides one column and leaves the table readable. Column-level security hides the column while leaving the rest of the table readable. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Row-level security filters rows per identity, so one table returns different rows to different users. Why the correct answer wins: Column-level security hides one column and leaves the table readable.
- **B:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: Column-level security hides one column and leaves the table readable.
- **C:** Correct. Column-level security hides the column while leaving the rest of the table readable. In this case: Column-level security hides one column and leaves the table readable.
- **D:** Incorrect for this question. A file-level grant is the narrowest path restriction the platform offers. Why the correct answer wins: Column-level security hides one column and leaves the table readable.

### Question 17 — A, D

Answers: Grant access at the folder that holds the restricted files; Apply object-level security in the semantic model. The folder grant restricts the path, and object-level security hides the table. A folder grant restricts the path without hiding the whole lakehouse. Object-level security hides a table or column from a role in the semantic model. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Object-level security hides a table or column from a role in the semantic model. In this case: The folder grant restricts the path, and object-level security hides the table.
- **B:** Incorrect for this question. Row-level security filters rows per identity, so one table returns different rows to different users. Why the correct answer wins: The folder grant restricts the path, and object-level security hides the table.
- **C:** Incorrect for this question. A file-level grant is the narrowest path restriction the platform offers. Why the correct answer wins: The folder grant restricts the path, and object-level security hides the table.
- **D:** Correct. A folder grant restricts the path without hiding the whole lakehouse. In this case: The folder grant restricts the path, and object-level security hides the table.
- **E:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: The folder grant restricts the path, and object-level security hides the table.

### Question 18 — B

Answer: Apply dynamic data masking to the column. Dynamic data masking masks the value and leaves the table queryable. Masking shows a masked value to unauthorised users while the stored data stays intact. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: Dynamic data masking masks the value and leaves the table queryable.
- **B:** Correct. Masking shows a masked value to unauthorised users while the stored data stays intact. In this case: Dynamic data masking masks the value and leaves the table queryable.
- **C:** Incorrect for this question. A report-level mask protects one visual and leaves every other consumer unmasked. Why the correct answer wins: Dynamic data masking masks the value and leaves the table queryable.
- **D:** Incorrect for this question. A view removes the column entirely, which is not the same as masking the value. Why the correct answer wins: Dynamic data masking masks the value and leaves the table queryable.

### Question 19 — D

Answer: Exempt the authorised group from the mask. The authorised group needs the exemption from the mask. The masking rule needs the exemption, or the authorised group sees masked values too. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A view removes the column entirely, which is not the same as masking the value. Why the correct answer wins: The authorised group needs the exemption from the mask.
- **B:** Incorrect for this question. A report-level mask protects one visual and leaves every other consumer unmasked. Why the correct answer wins: The authorised group needs the exemption from the mask.
- **C:** Incorrect for this question. Masking shows a masked value to unauthorised users while the stored data stays intact. Why the correct answer wins: The authorised group needs the exemption from the mask.
- **D:** Correct. The masking rule needs the exemption, or the authorised group sees masked values too. In this case: The authorised group needs the exemption from the mask.

### Question 20 — D

Answer: Certify the item as the approved source. Certification marks the item as the reviewed, authoritative source. Certification tells consumers the item has been reviewed as authoritative. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Promotion signals readiness without the review that certification implies. Why the correct answer wins: Certification marks the item as the reviewed, authoritative source.
- **B:** Incorrect for this question. The label travels with the item and drives the protection downstream consumers inherit. Why the correct answer wins: Certification marks the item as the reviewed, authoritative source.
- **C:** Incorrect for this question. A default label classifies new items that nobody labels by hand. Why the correct answer wins: Certification marks the item as the reviewed, authoritative source.
- **D:** Correct. Certification tells consumers the item has been reviewed as authoritative. In this case: Certification marks the item as the reviewed, authoritative source.

### Question 21 — B

Answer: Apply the sensitivity label to the item. The sensitivity label travels with the item to its consumers. The label travels with the item and drives the protection downstream consumers inherit. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Inheritance keeps one classification instead of a second opinion on the same data. Why the correct answer wins: The sensitivity label travels with the item to its consumers.
- **B:** Correct. The label travels with the item and drives the protection downstream consumers inherit. In this case: The sensitivity label travels with the item to its consumers.
- **C:** Incorrect for this question. Promotion signals readiness without the review that certification implies. Why the correct answer wins: The sensitivity label travels with the item to its consumers.
- **D:** Incorrect for this question. Certification tells consumers the item has been reviewed as authoritative. Why the correct answer wins: The sensitivity label travels with the item to its consumers.

### Question 22 — D

Answer: Read the Fabric audit log in the Microsoft Purview portal. The audit log records who changed which item and when. The audit log records who did what to which item and when. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The audit log has a retention window, so an investigation that starts late needs the export. Why the correct answer wins: The audit log records who changed which item and when.
- **B:** Incorrect for this question. Filtering turns a very large log into the events that answer the question. Why the correct answer wins: The audit log records who changed which item and when.
- **C:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The audit log records who changed which item and when.
- **D:** Correct. The audit log records who did what to which item and when. In this case: The audit log records who changed which item and when.

### Question 23 — B

Answer: Scope the OneLake role to the folder that holds the restricted table. A folder-scoped OneLake role restricts exactly the data it names. A folder-scoped role restricts exactly the data rather than the whole lakehouse. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. OneLake security governs data access independently of the workspace role. Why the correct answer wins: A folder-scoped OneLake role restricts exactly the data it names.
- **B:** Correct. A folder-scoped role restricts exactly the data rather than the whole lakehouse. In this case: A folder-scoped OneLake role restricts exactly the data it names.
- **C:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: A folder-scoped OneLake role restricts exactly the data it names.
- **D:** Incorrect for this question. A group grant is maintained once instead of once per person. Why the correct answer wins: A folder-scoped OneLake role restricts exactly the data it names.

### Question 24 — B, C

Answers: Configure OneLake security roles for the lakehouse; Grant the OneLake role to a security group rather than to individuals. OneLake security governs the data, and a group grant is maintained once. OneLake security governs data access independently of the workspace role. A group grant is maintained once instead of once per person. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: OneLake security governs the data, and a group grant is maintained once.
- **B:** Correct. OneLake security governs data access independently of the workspace role. In this case: OneLake security governs the data, and a group grant is maintained once.
- **C:** Correct. A group grant is maintained once instead of once per person. In this case: OneLake security governs the data, and a group grant is maintained once.
- **D:** Incorrect for this question. A folder-scoped role restricts exactly the data rather than the whole lakehouse. Why the correct answer wins: OneLake security governs the data, and a group grant is maintained once.
- **E:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: OneLake security governs the data, and a group grant is maintained once.

### Question 25 — B

Answer: Use a pipeline for the copy and the orchestration. A pipeline owns the copy, the dependency, and the order. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: A pipeline owns the copy, the dependency, and the order.
- **B:** Correct. A pipeline owns the scheduling, the copy activity, and the dependency between steps. In this case: A pipeline owns the copy, the dependency, and the order.
- **C:** Incorrect for this question. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Why the correct answer wins: A pipeline owns the copy, the dependency, and the order.
- **D:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: A pipeline owns the copy, the dependency, and the order.

### Question 26 — C

Answer: Use a Dataflow Gen2 for the transformation. A Dataflow Gen2 suits a transformation expressible in Power Query. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: A Dataflow Gen2 suits a transformation expressible in Power Query.
- **B:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: A Dataflow Gen2 suits a transformation expressible in Power Query.
- **C:** Correct. A Dataflow Gen2 suits a transformation that is expressible in Power Query. In this case: A Dataflow Gen2 suits a transformation expressible in Power Query.
- **D:** Incorrect for this question. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Why the correct answer wins: A Dataflow Gen2 suits a transformation expressible in Power Query.

### Question 27 — A

Answer: Add an event-based trigger so the run starts when the file arrives. An event trigger starts the run when the file arrives. An event trigger removes the gap between the file landing and the run starting. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. An event trigger removes the gap between the file landing and the run starting. In this case: An event trigger starts the run when the file arrives.
- **B:** Incorrect for this question. The schedule trigger is what makes the run recur without a person starting it. Why the correct answer wins: An event trigger starts the run when the file arrives.
- **C:** Incorrect for this question. The file-created event is the signal that the extract has finished arriving. Why the correct answer wins: An event trigger starts the run when the file arrives.
- **D:** Incorrect for this question. A parameter makes one pipeline reusable across folders and environments. Why the correct answer wins: An event trigger starts the run when the file arrives.

### Question 28 — B, D

Answers: Add an event-based trigger so the run starts when the file arrives; Pass the folder path as a pipeline parameter. The event trigger starts the run, and the parameter makes it reusable. An event trigger removes the gap between the file landing and the run starting. A parameter makes one pipeline reusable across folders and environments. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A variable carries the computed value between the activities that need it. Why the correct answer wins: The event trigger starts the run, and the parameter makes it reusable.
- **B:** Correct. An event trigger removes the gap between the file landing and the run starting. In this case: The event trigger starts the run, and the parameter makes it reusable.
- **C:** Incorrect for this question. The schedule trigger is what makes the run recur without a person starting it. Why the correct answer wins: The event trigger starts the run, and the parameter makes it reusable.
- **D:** Correct. A parameter makes one pipeline reusable across folders and environments. In this case: The event trigger starts the run, and the parameter makes it reusable.
- **E:** Incorrect for this question. A dynamic expression computes the path instead of hard-coding a date. Why the correct answer wins: The event trigger starts the run, and the parameter makes it reusable.

### Question 29 — A

Answer: Choose the capacity and region → create the workspace → assign the domain → grant the workspace roles. The fixed region and capacity are decided before the workspace exists, and access follows it. The region is fixed at creation, so it is decided before the workspace exists, and access is granted after it does. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The region is fixed at creation, so it is decided before the workspace exists, and access is granted after it does. In this case: The fixed region and capacity are decided before the workspace exists, and access follows it.
- **B:** Incorrect for this question. A domain assignment and a role grant both need the workspace, and the capacity is not a last step. Why the correct answer wins: The fixed region and capacity are decided before the workspace exists, and access follows it.
- **C:** Incorrect for this question. The region cannot be changed after creation, so choosing it later is not possible. Why the correct answer wins: The fixed region and capacity are decided before the workspace exists, and access follows it.
- **D:** Incorrect for this question. Roles cannot be granted before the workspace exists, and the capacity is chosen before, not after. Why the correct answer wins: The fixed region and capacity are decided before the workspace exists, and access follows it.

### Question 30 — C

Answer: Connect the workspace to Git → commit the item definitions → create the deployment pipeline → add deployment rules → promote through the stages. The definitions must be in Git before the pipeline promotes them. The definitions have to be in source control before the pipeline promotes them, and the rules are added before the first promotion. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Every step is in the wrong order: a promotion needs the pipeline, the pipeline needs the definitions in Git, and the rules come first. Why the correct answer wins: The definitions must be in Git before the pipeline promotes them.
- **B:** Incorrect for this question. Promoting before the definitions are committed and before the rules exist overwrites the target with the wrong settings. Why the correct answer wins: The definitions must be in Git before the pipeline promotes them.
- **C:** Correct. The definitions have to be in source control before the pipeline promotes them, and the rules are added before the first promotion. In this case: The definitions must be in Git before the pipeline promotes them.
- **D:** Incorrect for this question. There is nothing to commit before the repository is connected, and the rules belong to a pipeline that does not exist yet. Why the correct answer wins: The definitions must be in Git before the pipeline promotes them.

### Question 31 — B, C

Answers: Load only the rows newer than the stored watermark; Store the last successful load timestamp in a control table. The watermark bounds the extract, and it advances only after the load succeeds. An incremental load moves the delta instead of the history. The control table is what lets the next run know where this one stopped. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: The watermark bounds the extract, and it advances only after the load succeeds.
- **B:** Correct. The control table is what lets the next run know where this one stopped. In this case: The watermark bounds the extract, and it advances only after the load succeeds.
- **C:** Correct. An incremental load moves the delta instead of the history. In this case: The watermark bounds the extract, and it advances only after the load succeeds.
- **D:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: The watermark bounds the extract, and it advances only after the load succeeds.
- **E:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: The watermark bounds the extract, and it advances only after the load succeeds.

### Question 32 — A

Answer: Route the failed rows to a reject table and continue the load. A reject table preserves the bad rows and lets the load continue. A reject table preserves the bad rows for correction without stopping the load. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. A reject table preserves the bad rows for correction without stopping the load. In this case: A reject table preserves the bad rows and lets the load continue.
- **B:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: A reject table preserves the bad rows and lets the load continue.
- **C:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: A reject table preserves the bad rows and lets the load continue.
- **D:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: A reject table preserves the bad rows and lets the load continue.

### Question 33 — D

Answer: Build a type 2 dimension with validity dates and a current flag. A type 2 dimension keeps the attribute history the analysis needs. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. Local study-map skill 2.2 (Dimensional Model Preparation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: A type 2 dimension keeps the attribute history the analysis needs.
- **B:** Incorrect for this question. A surrogate key decouples the warehouse from the source system identifiers. Why the correct answer wins: A type 2 dimension keeps the attribute history the analysis needs.
- **C:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: A type 2 dimension keeps the attribute history the analysis needs.
- **D:** Correct. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. In this case: A type 2 dimension keeps the attribute history the analysis needs.

### Question 34 — B

Answer: Generate a surrogate key instead of reusing the source key. A surrogate key decouples the warehouse from the source identifiers. A surrogate key decouples the warehouse from the source system identifiers. Local study-map skill 2.2 (Dimensional Model Preparation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A star schema keeps the fact table narrow and the dimensions reusable. Why the correct answer wins: A surrogate key decouples the warehouse from the source identifiers.
- **B:** Correct. A surrogate key decouples the warehouse from the source system identifiers. In this case: A surrogate key decouples the warehouse from the source identifiers.
- **C:** Incorrect for this question. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. Why the correct answer wins: A surrogate key decouples the warehouse from the source identifiers.
- **D:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: A surrogate key decouples the warehouse from the source identifiers.

### Question 35 — A, C

Answers: Model the data as a star schema with conformed dimensions; Build a type 2 dimension with validity dates and a current flag. The star schema keeps the facts narrow, and type 2 keeps the history. A star schema keeps the fact table narrow and the dimensions reusable. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. Local study-map skill 2.2 (Dimensional Model Preparation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. In this case: The star schema keeps the facts narrow, and type 2 keeps the history.
- **B:** Incorrect for this question. Denormalization trades storage for the query shape the report actually uses. Why the correct answer wins: The star schema keeps the facts narrow, and type 2 keeps the history.
- **C:** Correct. A star schema keeps the fact table narrow and the dimensions reusable. In this case: The star schema keeps the facts narrow, and type 2 keeps the history.
- **D:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: The star schema keeps the facts narrow, and type 2 keeps the history.
- **E:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: The star schema keeps the facts narrow, and type 2 keeps the history.

### Question 36 — B

Answer: Set a checkpoint location for the streaming query. A checkpoint is what lets the stream resume from where it stopped. The checkpoint is what makes the stream restart from where it stopped. Local study-map skill 2.3 (Streaming Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Native tables give full KQL capability over the streaming data. Why the correct answer wins: A checkpoint is what lets the stream resume from where it stopped.
- **B:** Correct. The checkpoint is what makes the stream restart from where it stopped. In this case: A checkpoint is what lets the stream resume from where it stopped.
- **C:** Incorrect for this question. A watermark sets how long the engine waits for late events before closing a window. Why the correct answer wins: A checkpoint is what lets the stream resume from where it stopped.
- **D:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: A checkpoint is what lets the stream resume from where it stopped.

### Question 37 — C

Answer: Load the curated model into the warehouse. A warehouse supports the transactional T-SQL the close needs. A warehouse gives multi-table T-SQL transactions and a governed relational model. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. An eventhouse is optimized for high-volume time-series queries. Why the correct answer wins: A warehouse supports the transactional T-SQL the close needs.
- **B:** Incorrect for this question. A KQL database indexes the timestamp column for the range queries the dashboards run. Why the correct answer wins: A warehouse supports the transactional T-SQL the close needs.
- **C:** Correct. A warehouse gives multi-table T-SQL transactions and a governed relational model. In this case: A warehouse supports the transactional T-SQL the close needs.
- **D:** Incorrect for this question. The Files area keeps the raw extract in its original format. Why the correct answer wins: A warehouse supports the transactional T-SQL the close needs.

### Question 38 — A, B

Answers: Write the curated table into the lakehouse Tables area; Query the lakehouse through its SQL analytics endpoint. The Tables area holds the Delta table, and the endpoint serves T-SQL over it. A Delta table in Tables is what the SQL analytics endpoint exposes. The endpoint gives read-only T-SQL over the Delta tables without a copy. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. The endpoint gives read-only T-SQL over the Delta tables without a copy. In this case: The Tables area holds the Delta table, and the endpoint serves T-SQL over it.
- **B:** Correct. A Delta table in Tables is what the SQL analytics endpoint exposes. In this case: The Tables area holds the Delta table, and the endpoint serves T-SQL over it.
- **C:** Incorrect for this question. An eventhouse is optimized for high-volume time-series queries. Why the correct answer wins: The Tables area holds the Delta table, and the endpoint serves T-SQL over it.
- **D:** Incorrect for this question. A warehouse gives multi-table T-SQL transactions and a governed relational model. Why the correct answer wins: The Tables area holds the Delta table, and the endpoint serves T-SQL over it.
- **E:** Incorrect for this question. The Files area keeps the raw extract in its original format. Why the correct answer wins: The Tables area holds the Delta table, and the endpoint serves T-SQL over it.

### Question 39 — A

Answer: Transform with Dataflow Gen2 and Power Query. A Dataflow Gen2 is the low-code engine for that team. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. In this case: A Dataflow Gen2 is the low-code engine for that team.
- **B:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: A Dataflow Gen2 is the low-code engine for that team.
- **C:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: A Dataflow Gen2 is the low-code engine for that team.
- **D:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: A Dataflow Gen2 is the low-code engine for that team.

### Question 40 — B

Answer: Transform with T-SQL against the warehouse. T-SQL is the right engine once the data is already relational there. T-SQL is the right engine once the data is relational and already in the warehouse. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: T-SQL is the right engine once the data is already relational there.
- **B:** Correct. T-SQL is the right engine once the data is relational and already in the warehouse. In this case: T-SQL is the right engine once the data is already relational there.
- **C:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: T-SQL is the right engine once the data is already relational there.
- **D:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: T-SQL is the right engine once the data is already relational there.

### Question 41 — A

Answer: Create an internal OneLake shortcut to the other lakehouse table. An internal shortcut points at the table without copying it. An internal shortcut points at another Fabric item without copying the data. Local study-map skill 2.6 (OneLake Shortcuts), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. An internal shortcut points at another Fabric item without copying the data. In this case: An internal shortcut points at the table without copying it.
- **B:** Incorrect for this question. A copy duplicates the data, so the source of truth is no longer one place. Why the correct answer wins: An internal shortcut points at the table without copying it.
- **C:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: An internal shortcut points at the table without copying it.
- **D:** Incorrect for this question. The shortcut exposes the external container as if the files were in OneLake. Why the correct answer wins: An internal shortcut points at the table without copying it.

### Question 42 — D

Answer: Create an ADLS Gen2 shortcut to the external container. An ADLS Gen2 shortcut exposes the container without a copy. The shortcut exposes the external container as if the files were in OneLake. Local study-map skill 2.6 (OneLake Shortcuts), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: An ADLS Gen2 shortcut exposes the container without a copy.
- **B:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: An ADLS Gen2 shortcut exposes the container without a copy.
- **C:** Incorrect for this question. A copy duplicates the data, so the source of truth is no longer one place. Why the correct answer wins: An ADLS Gen2 shortcut exposes the container without a copy.
- **D:** Correct. The shortcut exposes the external container as if the files were in OneLake. In this case: An ADLS Gen2 shortcut exposes the container without a copy.

### Question 43 — A

Answer: Enable mirroring for the operational database. Mirroring replicates the source tables continuously. Local study-map skill 2.7 (Mirroring), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. In this case: Mirroring replicates the source tables continuously.
- **B:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: Mirroring replicates the source tables continuously.
- **C:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: Mirroring replicates the source tables continuously.
- **D:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: Mirroring replicates the source tables continuously.

### Question 44 — D

Answer: Mirror from a read replica so the source database keeps its capacity. A read replica absorbs the load the mirror creates. The replica absorbs the read load the mirror creates. Local study-map skill 2.7 (Mirroring), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Appending preserves the earlier loads that the incremental pattern depends on. Why the correct answer wins: A read replica absorbs the load the mirror creates.
- **B:** Incorrect for this question. Change data capture streams the changes instead of a periodic full compare. Why the correct answer wins: A read replica absorbs the load the mirror creates.
- **C:** Incorrect for this question. The shortcut exposes the external container as if the files were in OneLake. Why the correct answer wins: A read replica absorbs the load the mirror creates.
- **D:** Correct. The replica absorbs the read load the mirror creates. In this case: A read replica absorbs the load the mirror creates.

### Question 45 — B

Answer: Append the new files instead of overwriting the target. Appending preserves the loads the incremental pattern depends on. Appending preserves the earlier loads that the incremental pattern depends on. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: Appending preserves the loads the incremental pattern depends on.
- **B:** Correct. Appending preserves the earlier loads that the incremental pattern depends on. In this case: Appending preserves the loads the incremental pattern depends on.
- **C:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: Appending preserves the loads the incremental pattern depends on.
- **D:** Incorrect for this question. Deleting after success prevents the same file being loaded twice. Why the correct answer wins: Appending preserves the loads the incremental pattern depends on.

### Question 46 — C

Answer: Delete the processed source file after the load succeeds. Deleting the source after a successful load stops the second pickup. Deleting after success prevents the same file being loaded twice. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: Deleting the source after a successful load stops the second pickup.
- **B:** Incorrect for this question. Get Metadata turns an unknown folder into a list the loop can iterate. Why the correct answer wins: Deleting the source after a successful load stops the second pickup.
- **C:** Correct. Deleting after success prevents the same file being loaded twice. In this case: Deleting the source after a successful load stops the second pickup.
- **D:** Incorrect for this question. Appending preserves the earlier loads that the incremental pattern depends on. Why the correct answer wins: Deleting the source after a successful load stops the second pickup.

### Question 47 — C

Answer: Use a window function to rank within the partition. A window function reads across related rows without collapsing them. A window computes across related rows without collapsing them into one. Local study-map skill 2.9 (PySpark Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: A window function reads across related rows without collapsing them.
- **B:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: A window function reads across related rows without collapsing them.
- **C:** Correct. A window computes across related rows without collapsing them into one. In this case: A window function reads across related rows without collapsing them.
- **D:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: A window function reads across related rows without collapsing them.

### Question 48 — B, D

Answers: Transform with PySpark in a notebook; Use a window function to rank within the partition. PySpark scales the cleansing, and the window function does the ranking. PySpark handles the row-level and windowed transformations that Spark scales. A window computes across related rows without collapsing them into one. Local study-map skill 2.9 (PySpark Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: PySpark scales the cleansing, and the window function does the ranking.
- **B:** Correct. A window computes across related rows without collapsing them into one. In this case: PySpark scales the cleansing, and the window function does the ranking.
- **C:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: PySpark scales the cleansing, and the window function does the ranking.
- **D:** Correct. PySpark handles the row-level and windowed transformations that Spark scales. In this case: PySpark scales the cleansing, and the window function does the ranking.
- **E:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: PySpark scales the cleansing, and the window function does the ranking.

### Question 49 — B

Answer: Transform with KQL in the eventhouse. KQL is the native language of the eventhouse tables. KQL is the native language for the eventhouse tables. Local study-map skill 2.10 (T-SQL and KQL Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: KQL is the native language of the eventhouse tables.
- **B:** Correct. KQL is the native language for the eventhouse tables. In this case: KQL is the native language of the eventhouse tables.
- **C:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: KQL is the native language of the eventhouse tables.
- **D:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: KQL is the native language of the eventhouse tables.

### Question 50 — C

Answer: Denormalize the model so the report needs no join. Denormalization trades storage for the query shape the report actually uses. Local study-map skill 2.11 (Denormalization, Grouping, and Aggregation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: Denormalization trades storage for the query shape the report actually uses.
- **B:** Incorrect for this question. A star schema keeps the fact table narrow and the dimensions reusable. Why the correct answer wins: Denormalization trades storage for the query shape the report actually uses.
- **C:** Correct. In this case: Denormalization trades storage for the query shape the report actually uses.
- **D:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: Denormalization trades storage for the query shape the report actually uses.

### Question 51 — B, D

Answers: Group and aggregate to the grain the report needs; Pivot the rows into the reporting columns. The grouping sets the grain, and the pivot produces the monthly columns. Aggregating to the report grain removes rows the report would otherwise discard. The pivot is what produces one column per period the report expects. Local study-map skill 2.11 (Denormalization, Grouping, and Aggregation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A window computes across related rows without collapsing them into one. Why the correct answer wins: The grouping sets the grain, and the pivot produces the monthly columns.
- **B:** Correct. The pivot is what produces one column per period the report expects. In this case: The grouping sets the grain, and the pivot produces the monthly columns.
- **C:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: The grouping sets the grain, and the pivot produces the monthly columns.
- **D:** Correct. Aggregating to the report grain removes rows the report would otherwise discard. In this case: The grouping sets the grain, and the pivot produces the monthly columns.
- **E:** Incorrect for this question. Denormalization trades storage for the query shape the report actually uses. Why the correct answer wins: The grouping sets the grain, and the pivot produces the monthly columns.

### Question 52 — D

Answer: Reprocess the affected partitions when the data arrives late. Reprocessing the affected partitions corrects the published total. Reprocessing the partition corrects the aggregate that was already published. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Reprocessing the affected partitions corrects the published total.
- **B:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Reprocessing the affected partitions corrects the published total.
- **C:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: Reprocessing the affected partitions corrects the published total.
- **D:** Correct. Reprocessing the partition corrects the aggregate that was already published. In this case: Reprocessing the affected partitions corrects the published total.

### Question 53 — A

Answer: Process the stream with an eventstream. An eventstream is the no-code path between source and destination. An eventstream is the no-code path from a source to a destination. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. An eventstream is the no-code path from a source to a destination. In this case: An eventstream is the no-code path between source and destination.
- **B:** Incorrect for this question. An update policy transforms the data as it lands in the KQL table. Why the correct answer wins: An eventstream is the no-code path between source and destination.
- **C:** Incorrect for this question. Structured streaming suits stateful processing and the same PySpark logic used in batch. Why the correct answer wins: An eventstream is the no-code path between source and destination.
- **D:** Incorrect for this question. A batch job over the landing folder adds latency the streaming requirement may not allow. Why the correct answer wins: An eventstream is the no-code path between source and destination.

### Question 54 — C

Answer: Read the watermark → extract only the rows after it → merge into the target → update the watermark. The watermark bounds the extract and advances only after the merge succeeds. The watermark bounds the extract, the merge applies the delta, and the watermark advances only after the merge succeeds. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Nothing has been extracted, so there is nothing to merge, and the watermark moves before the data does. Why the correct answer wins: The watermark bounds the extract and advances only after the merge succeeds.
- **B:** Incorrect for this question. A full extract ignores the watermark, so reading it afterwards adds nothing and the target reloads the history. Why the correct answer wins: The watermark bounds the extract and advances only after the merge succeeds.
- **C:** Correct. The watermark bounds the extract, the merge applies the delta, and the watermark advances only after the merge succeeds. In this case: The watermark bounds the extract and advances only after the merge succeeds.
- **D:** Incorrect for this question. Advancing the watermark before the merge loses every row the failed merge did not write. Why the correct answer wins: The watermark bounds the extract and advances only after the merge succeeds.

### Question 55 — B

Answer: Land the raw files unchanged → validate the schema and reject the bad rows → conform and deduplicate into silver → publish the gold table. Raw data is preserved and validated before anything is published. Raw data is preserved, validation happens before any transformation hides a problem, and the curated table is the last thing published. Local study-map skill 2.14 (Eventstream and Spark Structured Streaming), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. There is nothing to validate and nothing to publish before the raw files exist. Why the correct answer wins: Raw data is preserved and validated before anything is published.
- **B:** Correct. Raw data is preserved, validation happens before any transformation hides a problem, and the curated table is the last thing published. In this case: Raw data is preserved and validated before anything is published.
- **C:** Incorrect for this question. Conforming before the raw data lands transforms whatever was already there, and validation after publication is too late. Why the correct answer wins: Raw data is preserved and validated before anything is published.
- **D:** Incorrect for this question. The published table would be rebuilt from data that has not landed yet. Why the correct answer wins: Raw data is preserved and validated before anything is published.

### Question 56 — B

Answer: Create a materialized view for the repeated aggregation. A materialized view keeps the aggregate fresh instead of recomputing it. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: A materialized view keeps the aggregate fresh instead of recomputing it.
- **B:** Correct. In this case: A materialized view keeps the aggregate fresh instead of recomputing it.
- **C:** Incorrect for this question. A tumbling window covers fixed, non-overlapping intervals. Why the correct answer wins: A materialized view keeps the aggregate fresh instead of recomputing it.
- **D:** Incorrect for this question. A hopping window covers overlapping intervals so a trend can be smoothed. Why the correct answer wins: A materialized view keeps the aggregate fresh instead of recomputing it.

### Question 57 — C

Answer: Define the eventstream source → add the destination → create the KQL table → build the materialized view → alert on the aggregate. The source and destination come first, and the alert reads what the view produces. The source and destination define the pipeline, the table receives the events, the view aggregates them, and the alert reads the aggregate. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The alert fires before the destination and the view that produce the aggregate. Why the correct answer wins: The source and destination come first, and the alert reads what the view produces.
- **B:** Incorrect for this question. A destination with no source receives nothing, and the source is the first decision. Why the correct answer wins: The source and destination come first, and the alert reads what the view produces.
- **C:** Correct. The source and destination define the pipeline, the table receives the events, the view aggregates them, and the alert reads the aggregate. In this case: The source and destination come first, and the alert reads what the view produces.
- **D:** Incorrect for this question. The alert has nothing to read until the view, the table, and the stream exist. Why the correct answer wins: The source and destination come first, and the alert reads what the view produces.

### Question 58 — D

Answer: Use the Monitoring hub for the run history. The Monitoring hub lists every run with its status and duration. The hub lists every run with its status, duration, and owning item. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **B:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **C:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **D:** Correct. The hub lists every run with its status, duration, and owning item. In this case: The Monitoring hub lists every run with its status and duration.

### Question 59 — D

Answer: Read the item activity log. The item activity log records that item's runs and outcomes. The activity log records the runs of one item with their outcomes. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The item activity log records that item's runs and outcomes.
- **B:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The item activity log records that item's runs and outcomes.
- **C:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The item activity log records that item's runs and outcomes.
- **D:** Correct. The activity log records the runs of one item with their outcomes. In this case: The item activity log records that item's runs and outcomes.

### Question 60 — C

Answer: Read the refresh history for the semantic model. The refresh history separates a failed refresh from a slow one. Local study-map skill 3.2 (Monitoring Semantic Model Refresh), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The refresh history separates a failed refresh from a slow one.
- **B:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The refresh history separates a failed refresh from a slow one.
- **C:** Correct. In this case: The refresh history separates a failed refresh from a slow one.
- **D:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The refresh history separates a failed refresh from a slow one.

### Question 61 — B

Answer: Send the logs to a Log Analytics workspace. Log Analytics retains the history that the in-product views expire. Log Analytics keeps the history that the in-product views expire. Local study-map skill 3.2 (Monitoring Semantic Model Refresh), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: Log Analytics retains the history that the in-product views expire.
- **B:** Correct. Log Analytics keeps the history that the in-product views expire. In this case: Log Analytics retains the history that the in-product views expire.
- **C:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: Log Analytics retains the history that the in-product views expire.
- **D:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: Log Analytics retains the history that the in-product views expire.

### Question 62 — A

Answer: Set the alert to fire only after the retry policy has been exhausted. The alert should wait for the retry policy to be exhausted. Waiting for the retries stops a transient failure being reported as an outage. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. Waiting for the retries stops a transient failure being reported as an outage. In this case: The alert should wait for the retry policy to be exhausted.
- **B:** Incorrect for this question. The alert must reach the owner, or it becomes noise nobody acts on. Why the correct answer wins: The alert should wait for the retry policy to be exhausted.
- **C:** Incorrect for this question. Alerting on success as well as failure trains the team to ignore the alert. Why the correct answer wins: The alert should wait for the retry policy to be exhausted.
- **D:** Incorrect for this question. A dashboard over the monitoring table makes the trend visible between runs. Why the correct answer wins: The alert should wait for the retry policy to be exhausted.

### Question 63 — D

Answer: Inspect the Dataflow Gen2 refresh error for the failing query step. The refresh error names the query step that diverged. The refresh error names the step, which is where the transform diverged. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. A shortcut fails for a connection or permission reason more often than for a data reason. Why the correct answer wins: The refresh error names the query step that diverged.
- **B:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The refresh error names the query step that diverged.
- **C:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The refresh error names the query step that diverged.
- **D:** Correct. The refresh error names the step, which is where the transform diverged. In this case: The refresh error names the query step that diverged.

### Question 64 — C

Answer: Set the failure dependency so the handler runs when the step fails. The failure dependency is what makes the handler execute. The dependency is what makes the failure path execute at all. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. An error branch turns a silent failure into an explicit outcome. Why the correct answer wins: The failure dependency is what makes the handler execute.
- **B:** Incorrect for this question. A retry absorbs a transient failure that the next attempt would not repeat. Why the correct answer wins: The failure dependency is what makes the handler execute.
- **C:** Correct. The dependency is what makes the failure path execute at all. In this case: The failure dependency is what makes the handler execute.
- **D:** Incorrect for this question. Until repeats the check and stops when the condition is met or the timeout expires. Why the correct answer wins: The failure dependency is what makes the handler execute.

### Question 65 — D

Answer: Add a retry policy with a delay to the failing activity. A retry policy absorbs a transient failure. A retry absorbs a transient failure that the next attempt would not repeat. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The dependency is what makes the failure path execute at all. Why the correct answer wins: A retry policy absorbs a transient failure.
- **B:** Incorrect for this question. Until repeats the check and stops when the condition is met or the timeout expires. Why the correct answer wins: A retry policy absorbs a transient failure.
- **C:** Incorrect for this question. An error branch turns a silent failure into an explicit outcome. Why the correct answer wins: A retry policy absorbs a transient failure.
- **D:** Correct. A retry absorbs a transient failure that the next attempt would not repeat. In this case: A retry policy absorbs a transient failure.

### Question 66 — B

Answer: Inspect the failing cell output and exit value. The failing cell's output is where the exception is reported with its stack. The cell output is where the exception is reported with its stack. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The Spark UI shows the stages and tasks where the time went. Why the correct answer wins: The failing cell's output is where the exception is reported with its stack.
- **B:** Correct. The cell output is where the exception is reported with its stack. In this case: The failing cell's output is where the exception is reported with its stack.
- **C:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The failing cell's output is where the exception is reported with its stack.
- **D:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The failing cell's output is where the exception is reported with its stack.

### Question 67 — A

Answer: Check the failing cell and the Spark driver log. The Spark driver log carries the errors the cell output omits. The driver log carries the executor and serialization errors the cell output omits. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The driver log carries the executor and serialization errors the cell output omits. In this case: The Spark driver log carries the errors the cell output omits.
- **B:** Incorrect for this question. The Spark UI shows the stages and tasks where the time went. Why the correct answer wins: The Spark driver log carries the errors the cell output omits.
- **C:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The Spark driver log carries the errors the cell output omits.
- **D:** Incorrect for this question. The cell output is where the exception is reported with its stack. Why the correct answer wins: The Spark driver log carries the errors the cell output omits.

### Question 68 — A, B

Answers: Inspect the failing cell output and exit value; Check the failing cell and the Spark driver log. The cell output shows the exception, and the driver log shows the rest. The cell output is where the exception is reported with its stack. The driver log carries the executor and serialization errors the cell output omits. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The cell output is where the exception is reported with its stack. In this case: The cell output shows the exception, and the driver log shows the rest.
- **B:** Correct. The driver log carries the executor and serialization errors the cell output omits. In this case: The cell output shows the exception, and the driver log shows the rest.
- **C:** Incorrect for this question. The Spark UI shows the stages and tasks where the time went. Why the correct answer wins: The cell output shows the exception, and the driver log shows the rest.
- **D:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The cell output shows the exception, and the driver log shows the rest.
- **E:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The cell output shows the exception, and the driver log shows the rest.

### Question 69 — A

Answer: Query the ingestion failures table in the KQL database. The ingestion failures table records the rejected records and the reason. The failures table records the rejected records and the reason for each. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The failures table records the rejected records and the reason for each. In this case: The ingestion failures table records the rejected records and the reason.
- **B:** Incorrect for this question. The runtime metrics show whether the source or the destination is blocking. Why the correct answer wins: The ingestion failures table records the rejected records and the reason.
- **C:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The ingestion failures table records the rejected records and the reason.
- **D:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The ingestion failures table records the rejected records and the reason.

### Question 70 — C

Answer: Inspect the eventstream runtime metrics. The runtime metrics show whether the source or the destination is limiting. The runtime metrics show whether the source or the destination is blocking. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The failures table records the rejected records and the reason for each. Why the correct answer wins: The runtime metrics show whether the source or the destination is limiting.
- **B:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The runtime metrics show whether the source or the destination is limiting.
- **C:** Correct. The runtime metrics show whether the source or the destination is blocking. In this case: The runtime metrics show whether the source or the destination is limiting.
- **D:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The runtime metrics show whether the source or the destination is limiting.

### Question 71 — D

Answer: Read the T-SQL error message and then the query plan. The T-SQL message names the object or the conversion that failed. The message names the object or the conversion; the plan explains the cost. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The T-SQL message names the object or the conversion that failed.
- **B:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The T-SQL message names the object or the conversion that failed.
- **C:** Incorrect for this question. A shortcut fails for a connection or permission reason more often than for a data reason. Why the correct answer wins: The T-SQL message names the object or the conversion that failed.
- **D:** Correct. The message names the object or the conversion; the plan explains the cost. In this case: The T-SQL message names the object or the conversion that failed.

### Question 72 — C

Answer: Check the shortcut connection and the delegated permission. A shortcut fails on its connection or delegated permission more often than on data. A shortcut fails for a connection or permission reason more often than for a data reason. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: A shortcut fails on its connection or delegated permission more often than on data.
- **B:** Incorrect for this question. The message names the object or the conversion; the plan explains the cost. Why the correct answer wins: A shortcut fails on its connection or delegated permission more often than on data.
- **C:** Correct. A shortcut fails for a connection or permission reason more often than for a data reason. In this case: A shortcut fails on its connection or delegated permission more often than on data.
- **D:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: A shortcut fails on its connection or delegated permission more often than on data.

### Question 73 — A

Answer: Run OPTIMIZE to compact the small files. OPTIMIZE compacts the small files into fewer larger ones. OPTIMIZE rewrites many small files into fewer larger ones. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. OPTIMIZE rewrites many small files into fewer larger ones. In this case: OPTIMIZE compacts the small files into fewer larger ones.
- **B:** Incorrect for this question. V-Order writes the files in a layout the Fabric engines read faster. Why the correct answer wins: OPTIMIZE compacts the small files into fewer larger ones.
- **C:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: OPTIMIZE compacts the small files into fewer larger ones.
- **D:** Incorrect for this question. A partition on the filter column lets the engine skip the rows it does not need. Why the correct answer wins: OPTIMIZE compacts the small files into fewer larger ones.

### Question 74 — D

Answer: Partition the table on the date column. Partitioning on the filtered column lets the engine skip files. A partition on the filter column lets the engine skip the rows it does not need. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Z-Order clusters related values so a filtered read touches fewer files. Why the correct answer wins: Partitioning on the filtered column lets the engine skip files.
- **B:** Incorrect for this question. OPTIMIZE rewrites many small files into fewer larger ones. Why the correct answer wins: Partitioning on the filtered column lets the engine skip files.
- **C:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: Partitioning on the filtered column lets the engine skip files.
- **D:** Correct. A partition on the filter column lets the engine skip the rows it does not need. In this case: Partitioning on the filtered column lets the engine skip files.

### Question 75 — A, C

Answers: Run OPTIMIZE to compact the small files; Partition the table on the date column. Compaction reduces the file count, and the partition prunes by date. OPTIMIZE rewrites many small files into fewer larger ones. A partition on the filter column lets the engine skip the rows it does not need. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. A partition on the filter column lets the engine skip the rows it does not need. In this case: Compaction reduces the file count, and the partition prunes by date.
- **B:** Incorrect for this question. V-Order writes the files in a layout the Fabric engines read faster. Why the correct answer wins: Compaction reduces the file count, and the partition prunes by date.
- **C:** Correct. OPTIMIZE rewrites many small files into fewer larger ones. In this case: Compaction reduces the file count, and the partition prunes by date.
- **D:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: Compaction reduces the file count, and the partition prunes by date.
- **E:** Incorrect for this question. Z-Order clusters related values so a filtered read touches fewer files. Why the correct answer wins: Compaction reduces the file count, and the partition prunes by date.

### Question 76 — C

Answer: Raise the parallelism of the copy so independent slices move together. Raising the copy parallelism moves the independent slices together. Independent slices that run one after another waste the capacity the run already has. Local study-map skill 3.9 (Optimizing Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Coalesce reduces the file count without a full shuffle. Why the correct answer wins: Raising the copy parallelism moves the independent slices together.
- **B:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Raising the copy parallelism moves the independent slices together.
- **C:** Correct. Independent slices that run one after another waste the capacity the run already has. In this case: Raising the copy parallelism moves the independent slices together.
- **D:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: Raising the copy parallelism moves the independent slices together.

### Question 77 — A, E

Answers: Broadcast the small dimension to avoid the shuffle; Salt the skewed key so the partitions even out. The broadcast removes the shuffle, and salting splits the hot key. Broadcasting removes the shuffle of the large side of the join. Salting spreads one hot key across several partitions. Local study-map skill 3.9 (Optimizing Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. Broadcasting removes the shuffle of the large side of the join. In this case: The broadcast removes the shuffle, and salting splits the hot key.
- **B:** Incorrect for this question. Coalesce reduces the file count without a full shuffle. Why the correct answer wins: The broadcast removes the shuffle, and salting splits the hot key.
- **C:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: The broadcast removes the shuffle, and salting splits the hot key.
- **D:** Incorrect for this question. Too few partitions leave large tasks; too many add scheduling overhead. Why the correct answer wins: The broadcast removes the shuffle, and salting splits the hot key.
- **E:** Correct. Salting spreads one hot key across several partitions. In this case: The broadcast removes the shuffle, and salting splits the hot key.

### Question 78 — A

Answer: Join on the distribution column so the rows stay on their node. Joining on the distribution column keeps the rows on their node. A join on a different column forces a shuffle of both sides. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. A join on a different column forces a shuffle of both sides. In this case: Joining on the distribution column keeps the rows on their node.
- **B:** Incorrect for this question. Many small files cost more to scan than the same rows in fewer files. Why the correct answer wins: Joining on the distribution column keeps the rows on their node.
- **C:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Joining on the distribution column keeps the rows on their node.
- **D:** Incorrect for this question. The warehouse optimizer plans from statistics, not from the data itself. Why the correct answer wins: Joining on the distribution column keeps the rows on their node.

### Question 79 — B, C

Answers: Update statistics so the optimizer sees the current distribution; Join on the distribution column so the rows stay on their node. Statistics fix the estimate, and the distribution key removes the reshuffle. The warehouse optimizer plans from statistics, not from the data itself. A join on a different column forces a shuffle of both sides. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Statistics fix the estimate, and the distribution key removes the reshuffle.
- **B:** Correct. A join on a different column forces a shuffle of both sides. In this case: Statistics fix the estimate, and the distribution key removes the reshuffle.
- **C:** Correct. The warehouse optimizer plans from statistics, not from the data itself. In this case: Statistics fix the estimate, and the distribution key removes the reshuffle.
- **D:** Incorrect for this question. Coalesce reduces the file count without a full shuffle. Why the correct answer wins: Statistics fix the estimate, and the distribution key removes the reshuffle.
- **E:** Incorrect for this question. Many small files cost more to scan than the same rows in fewer files. Why the correct answer wins: Statistics fix the estimate, and the distribution key removes the reshuffle.

### Question 80 — C

Answer: Salt the skewed key so the partitions even out. Salting spreads the hot key across several partitions. Salting spreads one hot key across several partitions. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Broadcasting removes the shuffle of the large side of the join. Why the correct answer wins: Salting spreads the hot key across several partitions.
- **B:** Incorrect for this question. Too few partitions leave large tasks; too many add scheduling overhead. Why the correct answer wins: Salting spreads the hot key across several partitions.
- **C:** Correct. Salting spreads one hot key across several partitions. In this case: Salting spreads the hot key across several partitions.
- **D:** Incorrect for this question. Adaptive execution re-plans from the actual partition sizes at run time. Why the correct answer wins: Salting spreads the hot key across several partitions.

### Question 81 — C

Answer: Set the shuffle partition count to match the data volume. The shuffle partition count must match the data volume. Too few partitions leave large tasks; too many add scheduling overhead. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: The shuffle partition count must match the data volume.
- **B:** Incorrect for this question. Salting spreads one hot key across several partitions. Why the correct answer wins: The shuffle partition count must match the data volume.
- **C:** Correct. Too few partitions leave large tasks; too many add scheduling overhead. In this case: The shuffle partition count must match the data volume.
- **D:** Incorrect for this question. Broadcasting removes the shuffle of the large side of the join. Why the correct answer wins: The shuffle partition count must match the data volume.

### Question 82 — D

Answer: Cache the DataFrame that is used twice. Caching the reused DataFrame avoids the second computation. Caching the reused DataFrame avoids recomputing it for the second action. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Salting spreads one hot key across several partitions. Why the correct answer wins: Caching the reused DataFrame avoids the second computation.
- **B:** Incorrect for this question. Coalesce reduces the file count without a full shuffle. Why the correct answer wins: Caching the reused DataFrame avoids the second computation.
- **C:** Incorrect for this question. Broadcasting removes the shuffle of the large side of the join. Why the correct answer wins: Caching the reused DataFrame avoids the second computation.
- **D:** Correct. Caching the reused DataFrame avoids recomputing it for the second action. In this case: Caching the reused DataFrame avoids the second computation.

### Question 83 — D

Answer: Move the workspace to a larger capacity. Capacity units are the ceiling on everything the workspace runs. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.
- **B:** Incorrect for this question. The destination throughput caps how much the eventstream can deliver. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.
- **C:** Incorrect for this question. Smoothing lets a short burst use the capacity allowance instead of being throttled. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.
- **D:** Correct. In this case: Capacity units are the ceiling on everything the workspace runs.

### Question 84 — B

Answer: Move the workspace to a larger capacity. Capacity smoothing lets the burst borrow the burst allowance. Capacity units are the ceiling on everything the workspace runs. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Smoothing lets a short burst use the capacity allowance instead of being throttled. Why the correct answer wins: Capacity smoothing lets the burst borrow the burst allowance.
- **B:** Correct. Capacity units are the ceiling on everything the workspace runs. In this case: Capacity smoothing lets the burst borrow the burst allowance.
- **C:** Incorrect for this question. The caching policy keeps the hot window on fast storage. Why the correct answer wins: Capacity smoothing lets the burst borrow the burst allowance.
- **D:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: Capacity smoothing lets the burst borrow the burst allowance.

### Question 85 — A, E

Answers: Set the retention policy to match the query window; Set the caching policy on the KQL table. Retention matches the query window, and caching keeps the hot window fast. Retention beyond the query window pays for data nobody reads. The caching policy keeps the hot window on fast storage. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. Retention beyond the query window pays for data nobody reads. In this case: Retention matches the query window, and caching keeps the hot window fast.
- **B:** Incorrect for this question. The destination throughput caps how much the eventstream can deliver. Why the correct answer wins: Retention matches the query window, and caching keeps the hot window fast.
- **C:** Incorrect for this question. Query throughput is bounded by the eventhouse capacity. Why the correct answer wins: Retention matches the query window, and caching keeps the hot window fast.
- **D:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: Retention matches the query window, and caching keeps the hot window fast.
- **E:** Correct. The caching policy keeps the hot window on fast storage. In this case: Retention matches the query window, and caching keeps the hot window fast.

### Question 86 — A

Answer: Read the query plan → reduce the file count → optimize and Z-Order the table → re-measure the query. The plan identifies the cost, and the second measurement proves the effect. The plan identifies the cost, compaction and clustering address it, and the measurement proves the effect. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The plan identifies the cost, compaction and clustering address it, and the measurement proves the effect. In this case: The plan identifies the cost, and the second measurement proves the effect.
- **B:** Incorrect for this question. Measuring before the change and again after it is what makes the comparison possible. Why the correct answer wins: The plan identifies the cost, and the second measurement proves the effect.
- **C:** Incorrect for this question. The plan is what should have decided whether compaction was the right fix at all. Why the correct answer wins: The plan identifies the cost, and the second measurement proves the effect.
- **D:** Incorrect for this question. Optimizing before reading the plan optimizes whatever seemed slow rather than what was costly. Why the correct answer wins: The plan identifies the cost, and the second measurement proves the effect.

### Question 87 — A

Answer: Read the run history → isolate the failing activity → reproduce it with the same input → rerun only the failed activity. The history identifies the failure before anything is rerun. The history identifies the failure, the input reproduces it, and the rerun is scoped to what failed. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The history identifies the failure, the input reproduces it, and the rerun is scoped to what failed. In this case: The history identifies the failure before anything is rerun.
- **B:** Incorrect for this question. The failing activity has to be known before its input can be reproduced. Why the correct answer wins: The history identifies the failure before anything is rerun.
- **C:** Incorrect for this question. Rerunning before reading the history repeats the failure without explaining it. Why the correct answer wins: The history identifies the failure before anything is rerun.
- **D:** Incorrect for this question. The rerun happens before the cause is reproduced, so the second failure looks like a new one. Why the correct answer wins: The history identifies the failure before anything is rerun.

### Question 88 — C

Answer: Enable the monitoring output → build the dashboard over it → set the alert threshold → review the alert history each week. Nothing can be charted or alerted until the monitoring output exists. There is nothing to chart or alert on until the output exists, and the review is what keeps the threshold honest. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. A threshold with no output behind it cannot be evaluated. Why the correct answer wins: Nothing can be charted or alerted until the monitoring output exists.
- **B:** Incorrect for this question. There is no alert history before the alert exists. Why the correct answer wins: Nothing can be charted or alerted until the monitoring output exists.
- **C:** Correct. There is nothing to chart or alert on until the output exists, and the review is what keeps the threshold honest. In this case: Nothing can be charted or alerted until the monitoring output exists.
- **D:** Incorrect for this question. The dashboard and the threshold both read an output that does not exist yet. Why the correct answer wins: Nothing can be charted or alerted until the monitoring output exists.

### Question 89 — B

Answer: Create a deployment pipeline with development, test, and production stages. A deployment pipeline promotes the same definitions through each stage. The pipeline promotes the same item definitions through the stages instead of rebuilding them. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A rule stops a promotion from overwriting the target stage environment-specific settings. Why the correct answer wins: A deployment pipeline promotes the same definitions through each stage.
- **B:** Correct. The pipeline promotes the same item definitions through the stages instead of rebuilding them. In this case: A deployment pipeline promotes the same definitions through each stage.
- **C:** Incorrect for this question. Promoting every item drags unrelated work into the release. Why the correct answer wins: A deployment pipeline promotes the same definitions through each stage.
- **D:** Incorrect for this question. A backward deployment is the supported way to restore a previous stage state. Why the correct answer wins: A deployment pipeline promotes the same definitions through each stage.

### Question 90 — A

Answer: Apply the sensitivity label to the item. The sensitivity label travels with the item to its consumers. The label travels with the item and drives the protection downstream consumers inherit. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The label travels with the item and drives the protection downstream consumers inherit. In this case: The sensitivity label travels with the item to its consumers.
- **B:** Incorrect for this question. Certification tells consumers the item has been reviewed as authoritative. Why the correct answer wins: The sensitivity label travels with the item to its consumers.
- **C:** Incorrect for this question. Inheritance keeps one classification instead of a second opinion on the same data. Why the correct answer wins: The sensitivity label travels with the item to its consumers.
- **D:** Incorrect for this question. Promotion signals readiness without the review that certification implies. Why the correct answer wins: The sensitivity label travels with the item to its consumers.

### Question 91 — D, E

Answers: Configure OneLake security roles for the lakehouse; Scope the OneLake role to the folder that holds the restricted table. OneLake security governs the data, and the folder scope limits it to the restricted table. OneLake security governs data access independently of the workspace role. A folder-scoped role restricts exactly the data rather than the whole lakehouse. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: OneLake security governs the data, and the folder scope limits it to the restricted table.
- **B:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: OneLake security governs the data, and the folder scope limits it to the restricted table.
- **C:** Incorrect for this question. A group grant is maintained once instead of once per person. Why the correct answer wins: OneLake security governs the data, and the folder scope limits it to the restricted table.
- **D:** Correct. A folder-scoped role restricts exactly the data rather than the whole lakehouse. In this case: OneLake security governs the data, and the folder scope limits it to the restricted table.
- **E:** Correct. OneLake security governs data access independently of the workspace role. In this case: OneLake security governs the data, and the folder scope limits it to the restricted table.

### Question 92 — D

Answer: Store the telemetry in an eventhouse KQL database. An eventhouse is optimized for high-volume time-series queries. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A Delta table in Tables is what the SQL analytics endpoint exposes. Why the correct answer wins: An eventhouse is optimized for high-volume time-series queries.
- **B:** Incorrect for this question. A warehouse gives multi-table T-SQL transactions and a governed relational model. Why the correct answer wins: An eventhouse is optimized for high-volume time-series queries.
- **C:** Incorrect for this question. A KQL database indexes the timestamp column for the range queries the dashboards run. Why the correct answer wins: An eventhouse is optimized for high-volume time-series queries.
- **D:** Correct. In this case: An eventhouse is optimized for high-volume time-series queries.

### Question 93 — D

Answer: Create a materialized view for the repeated aggregation. A materialized view computes the total once for every consumer. A materialized view keeps the aggregate fresh instead of recomputing it per query. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A hopping window covers overlapping intervals so a trend can be smoothed. Why the correct answer wins: A materialized view computes the total once for every consumer.
- **B:** Incorrect for this question. A tumbling window covers fixed, non-overlapping intervals. Why the correct answer wins: A materialized view computes the total once for every consumer.
- **C:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: A materialized view computes the total once for every consumer.
- **D:** Correct. A materialized view keeps the aggregate fresh instead of recomputing it per query. In this case: A materialized view computes the total once for every consumer.

### Question 94 — B

Answer: Reprocess the affected partitions when the data arrives late. Reprocessing the affected partitions corrects the published total. Reprocessing the partition corrects the aggregate that was already published. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Reprocessing the affected partitions corrects the published total.
- **B:** Correct. Reprocessing the partition corrects the aggregate that was already published. In this case: Reprocessing the affected partitions corrects the published total.
- **C:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Reprocessing the affected partitions corrects the published total.
- **D:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: Reprocessing the affected partitions corrects the published total.

### Question 95 — D

Answer: Deduplicate on the business key and keep the latest record. Deduplication leaves one row per business key. Deduplication makes the target one row per business key. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Deduplication leaves one row per business key.
- **B:** Incorrect for this question. Reprocessing the partition corrects the aggregate that was already published. Why the correct answer wins: Deduplication leaves one row per business key.
- **C:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Deduplication leaves one row per business key.
- **D:** Correct. Deduplication makes the target one row per business key. In this case: Deduplication leaves one row per business key.

### Question 96 — A

Answer: Process the stream with an eventstream. An eventstream carries the events without a scheduled batch. An eventstream is the no-code path from a source to a destination. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. An eventstream is the no-code path from a source to a destination. In this case: An eventstream carries the events without a scheduled batch.
- **B:** Incorrect for this question. A batch job over the landing folder adds latency the streaming requirement may not allow. Why the correct answer wins: An eventstream carries the events without a scheduled batch.
- **C:** Incorrect for this question. An update policy transforms the data as it lands in the KQL table. Why the correct answer wins: An eventstream carries the events without a scheduled batch.
- **D:** Incorrect for this question. Structured streaming suits stateful processing and the same PySpark logic used in batch. Why the correct answer wins: An eventstream carries the events without a scheduled batch.

### Question 97 — C

Answer: Use a Copy activity in the pipeline. A Copy activity moves the rows as one orchestrated step. The Copy activity moves the files or rows as one orchestrated step. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Get Metadata turns an unknown folder into a list the loop can iterate. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.
- **B:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.
- **C:** Correct. The Copy activity moves the files or rows as one orchestrated step. In this case: A Copy activity moves the rows as one orchestrated step.
- **D:** Incorrect for this question. Appending preserves the earlier loads that the incremental pattern depends on. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.

### Question 98 — A

Answer: Read the T-SQL error message and then the query plan. The T-SQL message names the object or the conversion that failed. The message names the object or the conversion; the plan explains the cost. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The message names the object or the conversion; the plan explains the cost. In this case: The T-SQL message names the object or the conversion that failed.
- **B:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The T-SQL message names the object or the conversion that failed.
- **C:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The T-SQL message names the object or the conversion that failed.
- **D:** Incorrect for this question. A shortcut fails for a connection or permission reason more often than for a data reason. Why the correct answer wins: The T-SQL message names the object or the conversion that failed.

### Question 99 — B

Answer: Configure an alert on the failing condition. An alert turns the silent failure into a notification. An alert turns a silent failure into a notification. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Alerting on success as well as failure trains the team to ignore the alert. Why the correct answer wins: An alert turns the silent failure into a notification.
- **B:** Correct. An alert turns a silent failure into a notification. In this case: An alert turns the silent failure into a notification.
- **C:** Incorrect for this question. The alert must reach the owner, or it becomes noise nobody acts on. Why the correct answer wins: An alert turns the silent failure into a notification.
- **D:** Incorrect for this question. An activator rule evaluates the stream and fires when the condition holds. Why the correct answer wins: An alert turns the silent failure into a notification.

### Question 100 — D

Answer: Update statistics so the optimizer sees the current distribution. Statistics are what the optimizer plans from. The warehouse optimizer plans from statistics, not from the data itself. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Many small files cost more to scan than the same rows in fewer files. Why the correct answer wins: Statistics are what the optimizer plans from.
- **B:** Incorrect for this question. Independent slices that run one after another waste the capacity the run already has. Why the correct answer wins: Statistics are what the optimizer plans from.
- **C:** Incorrect for this question. A join on a different column forces a shuffle of both sides. Why the correct answer wins: Statistics are what the optimizer plans from.
- **D:** Correct. The warehouse optimizer plans from statistics, not from the data itself. In this case: Statistics are what the optimizer plans from.
