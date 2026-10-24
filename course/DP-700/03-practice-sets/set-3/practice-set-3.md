# Microsoft DP-700 — Full-Length Mock Exam 3

Fabric Data Engineer Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, interactive components in the Fabric portal, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. Streaming micro-batches on a pool with too little memory spill to disk every batch. What should change?

Domain: Implement and manage an analytics solution

- A. Enable autoscale with a minimum and maximum node count
- B. Size the pool for the node family and node count the workload needs
- C. Enable high concurrency mode for shared sessions
- D. Set a workspace-level custom Spark pool for the notebooks

### 2. The pool must add executors for a nightly burst and release them afterwards. What should be enabled?

Domain: Implement and manage an analytics solution

- A. Set the default environment at the workspace level
- B. Set a workspace-level custom Spark pool for the notebooks
- C. Enable autoscale with a minimum and maximum node count
- D. Enable dynamic allocation so idle executors are released during the run

### 3. A notebook must read the tables a warehouse created without exporting them. What must be enabled?

Domain: Implement and manage an analytics solution

- A. Create the workspace in the required region at creation time
- B. Keep OneLake availability enabled so other engines can read the same data
- C. Assign the workspace to a capacity that has headroom
- D. Assign the workspace to the domain that owns the subject area

### 4. A new workspace will host the real-time dashboards that already saturate one capacity. What should be checked?

Domain: Implement and manage an analytics solution

- A. Create the workspace in the required region at creation time
- B. Assign the workspace to the domain that owns the subject area
- C. Keep OneLake availability enabled so other engines can read the same data
- D. Assign the workspace to a capacity that has headroom

### 5. A DAG uses an operator Fabric does not provide and the team wants no rewrite. What should be reconsidered?

Domain: Implement and manage an analytics solution

- A. Enable the Apache Airflow job in the workspace and author the DAG
- B. Sync the Airflow DAG from the connected Git repository
- C. Rewrite the existing orchestration as a Fabric pipeline instead
- D. Use a pipeline for the copy and the orchestration

### 6. An Airflow DAG changes without review and breaks the nightly run. What should be done?

Domain: Implement and manage an analytics solution

- A. Sync the Airflow DAG from the connected Git repository
- B. Rewrite the existing orchestration as a Fabric pipeline instead
- C. Enable the Apache Airflow job in the workspace and author the DAG
- D. Use a pipeline for the copy and the orchestration

### 7. Every build rewrites artefacts and each one appears as a change in the repository. What should be done?

Domain: Implement and manage an analytics solution

- A. Resolve the conflict by choosing the definition that must win, then commit
- B. Add the generated artefacts to the ignore file rather than committing them
- C. Connect the workspace to a Git repository and commit the item definitions
- D. Work in a feature branch and merge through a pull request

### 8. A database project deploys to test but fails in production on the server name. What should be used?

Domain: Implement and manage an analytics solution

- A. Build the project into a DACPAC and deploy that artefact
- B. Connect the workspace to a Git repository and commit the item definitions
- C. Use SQLCMD variables for the environment-specific values
- D. Create a database project and deploy the schema from it

### 9. A promotion carried three unfinished notebooks into production. What should be configured?

Domain: Implement and manage an analytics solution

- A. Add deployment rules so the target stage keeps its own connection and parameters
- B. Create a deployment pipeline with development, test, and production stages
- C. Compare the stages before promoting
- D. Select only the items that belong in the target stage

### 10. A promotion broke the dashboards and the previous state must return quickly. What should be done?

Domain: Implement and manage an analytics solution

- A. Deploy backwards to recover the last known-good definition
- B. Create a deployment pipeline with development, test, and production stages
- C. Add deployment rules so the target stage keeps its own connection and parameters
- D. Compare the stages before promoting

### 11. A platform engineer must manage access and settings but not read the data. What should be granted, and what must be combined with it?

Domain: Implement and manage an analytics solution

- A. Grant Viewer on the workspace
- B. Grant the user a workspace role
- C. Grant Admin on the workspace to the platform team
- D. Grant Read on the item

### 12. A stakeholder needs to open exactly one dashboard from an email. What should be sent?

Domain: Implement and manage an analytics solution

- A. Share a link to the item with the required permission
- B. Share the single item with the user who needs only that item
- C. Grant the user a workspace role
- D. Grant Read on the item

### 13. An external reviewer needs one dashboard and must not see the workspace. Which two grants apply? Select two.

Domain: Implement and manage an analytics solution

- A. Grant the user a workspace role
- B. Grant Viewer on the workspace
- C. Share the single item with the user who needs only that item
- D. Share a link to the item with the required permission
- E. Grant Read on the item

### 14. One folder of raw telemetry must be closed while the rest of the lakehouse stays readable. What should be granted?

Domain: Implement and manage an analytics solution

- A. Define a row-level security policy on the table
- B. Apply column-level security so the column is hidden from the group
- C. Apply object-level security in the semantic model
- D. Grant access at the folder that holds the restricted files

### 15. The device identifier must be hidden from contractors while the rest of the row stays visible. What should be applied?

Domain: Implement and manage an analytics solution

- A. Apply column-level security so the column is hidden from the group
- B. Define a row-level security policy on the table
- C. Grant access at the folder that holds the restricted files
- D. Apply object-level security in the semantic model

### 16. A dashboard masks a field but the underlying table is exported unmasked. What is the defect?

Domain: Implement and manage an analytics solution

- A. Apply dynamic data masking to the column
- B. Mask the column in the report layer only
- C. Exempt the authorised group from the mask
- D. Expose a view with the column omitted instead of masking it

### 17. A column must be masked for most consumers and absent from one extract. Which two features apply? Select two.

Domain: Implement and manage an analytics solution

- A. Mask the column in the report layer only
- B. Apply dynamic data masking to the column
- C. Exempt the authorised group from the mask
- D. Expose a view with the column omitted instead of masking it
- E. Apply column-level security so the column is hidden from the group

### 18. A derived table is created from a labelled source and must not be less protected. What should happen?

Domain: Implement and manage an analytics solution

- A. Set the default sensitivity label for the workspace
- B. Apply the sensitivity label to the item
- C. Let the label inherit from the labelled source file
- D. Certify the item as the approved source

### 19. New items must be classified by default and derived items must not lose their classification. Which two practices apply? Select two.

Domain: Implement and manage an analytics solution

- A. Certify the item as the approved source
- B. Promote the item as ready for reuse
- C. Set the default sensitivity label for the workspace
- D. Let the label inherit from the labelled source file
- E. Apply the sensitivity label to the item

### 20. An investigator needs one engineer's reads on one eventhouse last Thursday. What should be done?

Domain: Implement and manage an analytics solution

- A. Read the Fabric audit log in the Microsoft Purview portal
- B. Export the audit events before the retention window closes
- C. Read the item activity log
- D. Filter the audit log by activity and by item

### 21. A compliance team must find an access event and keep it past the retention window. Which two steps apply? Select two.

Domain: Implement and manage an analytics solution

- A. Read the item activity log
- B. Read the Fabric audit log in the Microsoft Purview portal
- C. Filter the audit log by activity and by item
- D. Export the audit events before the retention window closes
- E. Read the refresh history for the semantic model

### 22. The raw telemetry folder must be closed even to workspace Contributors. What should be configured?

Domain: Implement and manage an analytics solution

- A. Scope the OneLake role to the folder that holds the restricted table
- B. Grant the OneLake role to a security group rather than to individuals
- C. Configure OneLake security roles for the lakehouse
- D. Grant access at the folder that holds the restricted files

### 23. Data must be protected independently of workspace roles and scoped to one folder. Which two settings apply? Select two.

Domain: Implement and manage an analytics solution

- A. Grant the user a workspace role
- B. Grant access at the folder that holds the restricted files
- C. Scope the OneLake role to the folder that holds the restricted table
- D. Grant the OneLake role to a security group rather than to individuals
- E. Configure OneLake security roles for the lakehouse

### 24. The transform needs stateful processing across micro-batches. What should be used?

Domain: Implement and manage an analytics solution

- A. Use a T-SQL script against the warehouse
- B. Use a Dataflow Gen2 for the transformation
- C. Use a pipeline for the copy and the orchestration
- D. Use a notebook for the transformation

### 25. The run must copy an archive and then start a transform in order. What should be used?

Domain: Implement and manage an analytics solution

- A. Use a pipeline for the copy and the orchestration
- B. Use a Dataflow Gen2 for the transformation
- C. Use a notebook for the transformation
- D. Use a KQL query against the eventhouse

### 26. One step copies files and another queries the eventhouse. Which two items apply? Select two.

Domain: Implement and manage an analytics solution

- A. Use a pipeline for the copy and the orchestration
- B. Use a KQL query against the eventhouse
- C. Use a Dataflow Gen2 for the transformation
- D. Use a notebook for the transformation
- E. Use a T-SQL script against the warehouse

### 27. A long-running check must repeat until a condition holds or a timeout expires. What should be used?

Domain: Implement and manage an analytics solution

- A. Add a schedule trigger with the cadence and time zone the business expects
- B. Set the value in a pipeline variable and reference the variable
- C. Use an Until loop with a timeout for the long-running check
- D. Look up the stored watermark before the copy

### 28. A computed value must be carried between three later activities. What should be used?

Domain: Implement and manage an analytics solution

- A. Look up the stored watermark before the copy
- B. Set the value in a pipeline variable and reference the variable
- C. Build the path with a dynamic expression at run time
- D. Pass the folder path as a pipeline parameter

### 29. A real-time workspace must be created and governed from the start. Which sequence is correct?

Domain: Implement and manage an analytics solution

- A. Assign the domain → grant the roles → create the workspace → choose the capacity
- B. Choose the capacity and region → create the workspace → assign the domain → grant the workspace roles
- C. Grant the workspace roles → create the workspace → choose the capacity → assign the domain
- D. Create the workspace → choose the region after the first item is built → assign the domain → grant the roles

### 30. A new orchestration must separate the copy from the PySpark step. Which sequence is correct?

Domain: Implement and manage an analytics solution

- A. Parameterise the run → add the notebook activity → build the pipeline → decide the work split
- B. Build the pipeline → decide the work split → parameterise the run → add the notebook activity
- C. Decide which work is copy, which is orchestration, and which needs PySpark → build the pipeline → add the notebook activity → parameterise the run
- D. Add the notebook activity → parameterise the run → decide the work split → build the pipeline

### 31. Readings arrive out of order when a device reconnects. What should the pipeline do?

Domain: Ingest and transform data

- A. Replace the missing value with a documented default
- B. Route the failed rows to a reject table and continue the load
- C. Deduplicate on the business key and keep the latest record
- D. Reprocess the affected partitions when the data arrives late

### 32. An event archive holds two years of history and only new files must load. What should change?

Domain: Ingest and transform data

- A. Merge the incoming rows into the target on the business key
- B. Load only the rows newer than the stored watermark
- C. Store the last successful load timestamp in a control table
- D. Run a full load and overwrite the target

### 33. A device identifier is reused after a meter is replaced. What should the warehouse key on?

Domain: Ingest and transform data

- A. Generate a surrogate key instead of reusing the source key
- B. Merge the incoming rows into the target on the business key
- C. Build a type 2 dimension with validity dates and a current flag
- D. Model the data as a star schema with conformed dimensions

### 34. Six dashboards read the same facts with different dimensions. What should be built?

Domain: Ingest and transform data

- A. Build a type 2 dimension with validity dates and a current flag
- B. Pivot the rows into the reporting columns
- C. Model the data as a star schema with conformed dimensions
- D. Denormalize the model so the report needs no join

### 35. A streaming query that restarts rewrites the last window. What is missing?

Domain: Ingest and transform data

- A. Set a checkpoint location for the streaming query
- B. Set a watermark so late events are handled deterministically
- C. Query the stream through a OneLake shortcut
- D. Store the stream in native tables in the eventhouse

### 36. A stream must resume without duplicates and tolerate late events. Which two settings apply? Select two.

Domain: Ingest and transform data

- A. Store the stream in native tables in the eventhouse
- B. Set a checkpoint location for the streaming query
- C. Query the stream through a OneLake shortcut
- D. Set a watermark so late events are handled deterministically
- E. Process the stream with an eventstream

### 37. The events must be joinable in KQL and kept hot for a day. What should hold them?

Domain: Ingest and transform data

- A. Create a KQL database for the time-series queries
- B. Store the stream in native tables in the eventhouse
- C. Load the curated model into the warehouse
- D. Query the stream through a OneLake shortcut

### 38. Engineers who do not query KQL must still read the event data. What should be created?

Domain: Ingest and transform data

- A. Store the stream in native tables in the eventhouse
- B. Create a KQL database for the time-series queries
- C. Store the telemetry in an eventhouse KQL database
- D. Query the stream through a OneLake shortcut

### 39. One team queries with KQL and another with Spark. Which two options apply? Select two.

Domain: Ingest and transform data

- A. Store the stream in native tables in the eventhouse
- B. Query the lakehouse through its SQL analytics endpoint
- C. Query the stream through a OneLake shortcut
- D. Load the curated model into the warehouse
- E. Create a KQL database for the time-series queries

### 40. The stream needs the same PySpark logic that already runs in batch. What should be used?

Domain: Ingest and transform data

- A. Process the stream with Spark structured streaming
- B. Run a batch job every few minutes over the landing folder
- C. Process the stream with an eventstream
- D. Process the stream with a KQL update policy

### 41. A landing table must be filtered by device type as records arrive. What should be used?

Domain: Ingest and transform data

- A. Transform with KQL in the eventhouse
- B. Transform with PySpark in a notebook
- C. Transform with T-SQL against the warehouse
- D. Transform with Dataflow Gen2 and Power Query

### 42. One stream reuses batch PySpark and another filters on arrival. Which two engines apply? Select two.

Domain: Ingest and transform data

- A. Process the stream with Spark structured streaming
- B. Process the stream with an eventstream
- C. Transform with KQL in the eventhouse
- D. Transform with PySpark in a notebook
- E. Transform with Dataflow Gen2 and Power Query

### 43. Sixty devices write parquet into a container the company already owns. How should it appear in OneLake?

Domain: Ingest and transform data

- A. Create an ADLS Gen2 shortcut to the external container
- B. Copy the remote data into a local table instead of shortcutting it
- C. Create an internal OneLake shortcut to the other lakehouse table
- D. Copy the files as binary and parse them downstream

### 44. A dashboard filters the shortcut-backed parquet on three columns and each query scans the source. What should be enabled?

Domain: Ingest and transform data

- A. Create an ADLS Gen2 shortcut to the external container
- B. Enable query acceleration on the shortcut
- C. Copy the remote data into a local table instead of shortcutting it
- D. Create an internal OneLake shortcut to the other lakehouse table

### 45. A maintenance system must appear in Fabric without a scheduled copy. What should be enabled?

Domain: Ingest and transform data

- A. Use a Copy activity in the pipeline
- B. Enable mirroring for the operational database
- C. Run a full load and overwrite the target
- D. Create an internal OneLake shortcut to the other lakehouse table

### 46. Each nightly run replaces the archive and last week's files disappear. What should change?

Domain: Ingest and transform data

- A. Use Get Metadata to list the files to process
- B. Delete the processed source file after the load succeeds
- C. Append the new files instead of overwriting the target
- D. Copy the files as binary and parse them downstream

### 47. A depot folder contains a variable number of files each night. What should be used?

Domain: Ingest and transform data

- A. Copy the files as binary and parse them downstream
- B. Use Get Metadata to list the files to process
- C. Iterate a ForEach activity over the returned list
- D. Delete the processed source file after the load succeeds

### 48. Each parcel must carry its previous scan time on the same row. What should be used?

Domain: Ingest and transform data

- A. Union the sources after conforming the columns
- B. Pivot the rows into the reporting columns
- C. Use a window function to rank within the partition
- D. Group and aggregate to the grain the report needs

### 49. Large row-level cleansing and a per-device ranking are both needed. Which two features apply? Select two.

Domain: Ingest and transform data

- A. Pivot the rows into the reporting columns
- B. Transform with Dataflow Gen2 and Power Query
- C. Transform with PySpark in a notebook
- D. Use a window function to rank within the partition
- E. Transform with T-SQL against the warehouse

### 50. The curated table lives in the warehouse and needs a multi-table update. What should be used?

Domain: Ingest and transform data

- A. Transform with PySpark in a notebook
- B. Transform with KQL in the eventhouse
- C. Transform with T-SQL against the warehouse
- D. Transform with Dataflow Gen2 and Power Query

### 51. Every dashboard query joins the same five tables. What should be done?

Domain: Ingest and transform data

- A. Pivot the rows into the reporting columns
- B. Model the data as a star schema with conformed dimensions
- C. Denormalize the model so the report needs no join
- D. Group and aggregate to the grain the report needs

### 52. Three depots export the same data with different column orders. What must happen first?

Domain: Ingest and transform data

- A. Denormalize the model so the report needs no join
- B. Union the sources after conforming the columns
- C. Group and aggregate to the grain the report needs
- D. Pivot the rows into the reporting columns

### 53. A handheld re-synchronises and sends the same scan twice. What should be applied?

Domain: Ingest and transform data

- A. Deduplicate on the business key and keep the latest record
- B. Reprocess the affected partitions when the data arrives late
- C. Route the failed rows to a reject table and continue the load
- D. Replace the missing value with a documented default

### 54. A stream carries duplicate scans and an occasional replayed hour. Which two practices apply? Select two.

Domain: Ingest and transform data

- A. Replace the missing value with a documented default
- B. Route the failed rows to a reject table and continue the load
- C. Reprocess the affected partitions when the data arrives late
- D. Deduplicate on the business key and keep the latest record
- E. Run a full load and overwrite the target

### 55. A requirement allows a four-minute delay and the team has only a notebook. What should be used?

Domain: Ingest and transform data

- A. Process the stream with an eventstream
- B. Process the stream with Spark structured streaming
- C. Run a batch job every few minutes over the landing folder
- D. Process the stream with a KQL update policy

### 56. A live operational board must be built from an event hub. Which sequence is correct?

Domain: Ingest and transform data

- A. Define the eventstream source → add the destination → create the KQL table → build the materialized view → alert on the aggregate
- B. Add the destination → create the KQL table → build the view → define the source → alert on the aggregate
- C. Alert on the aggregate → build the materialized view → define the source → add the destination → create the KQL table
- D. Create the KQL table → define the source → alert on the aggregate → add the destination → build the view

### 57. A rolling thirty-minute vehicle count must overlap. Which window fits?

Domain: Ingest and transform data

- A. Use a tumbling window for the fixed five-minute aggregate
- B. Use a sliding window that emits when the condition is met
- C. Create a materialized view for the repeated aggregation
- D. Use a hopping window when the intervals must overlap

### 58. A dashboard tile recomputes the same aggregate on every refresh. What should be created?

Domain: Ingest and transform data

- A. Create a materialized view for the repeated aggregation
- B. Use a hopping window when the intervals must overlap
- C. Query the stream through a OneLake shortcut
- D. Use a tumbling window for the fixed five-minute aggregate

### 59. Landed event files must become a curated parcel table. Which sequence is correct?

Domain: Ingest and transform data

- A. Land the raw files unchanged → validate the schema and reject the bad rows → conform and deduplicate into silver → publish the gold table
- B. Publish the gold table → validate the schema → land the raw files → conform and deduplicate
- C. Validate the schema → publish the gold table → land the raw files → conform and deduplicate
- D. Conform and deduplicate → land the raw files → publish the gold table → validate the schema

### 60. A watermark-based load must be introduced for the archive. Which sequence is correct?

Domain: Ingest and transform data

- A. Update the watermark → extract the rows → read the watermark → merge into the target
- B. Merge into the target → read the watermark → update the watermark → extract the rows
- C. Extract the full table → merge into the target → read the watermark → update the watermark
- D. Read the watermark → extract only the rows after it → merge into the target → update the watermark

### 61. One eventstream's runs must be reviewed after a change. What should be read?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Read the refresh history for the semantic model
- C. Read the Fabric audit log in the Microsoft Purview portal
- D. Read the item activity log

### 62. A release must be reviewed as a whole and one item inspected closely. Which two sources apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Send the logs to a Log Analytics workspace
- C. Read the refresh history for the semantic model
- D. Read the item activity log
- E. Read the Fabric audit log in the Microsoft Purview portal

### 63. A dashboard's semantic model refresh succeeds but arrives after the morning meeting. What shows both facts?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Read the item activity log
- C. Send the logs to a Log Analytics workspace
- D. Read the refresh history for the semantic model

### 64. The team needs a quarter of refresh history that the product no longer shows. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Send the logs to a Log Analytics workspace
- B. Read the refresh history for the semantic model
- C. Use the Monitoring hub for the run history
- D. Read the Fabric audit log in the Microsoft Purview portal

### 65. A pipeline fails on one activity and the run summary is generic. What shows the cause?

Domain: Monitor and optimize an analytics solution

- A. Check the failing cell and the Spark driver log
- B. Read the T-SQL error message and then the query plan
- C. Read the activity output of the failed step
- D. Inspect the Dataflow Gen2 refresh error for the failing query step

### 66. A source times out twice a day and succeeds on the next attempt. What should be added?

Domain: Monitor and optimize an analytics solution

- A. Set the failure dependency so the handler runs when the step fails
- B. Add an error branch so the failure is handled rather than ignored
- C. Use an Until loop with a timeout for the long-running check
- D. Add a retry policy with a delay to the failing activity

### 67. A pipeline must survive intermittent timeouts and explain a real failure. Which two practices apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Read the activity output of the failed step
- B. Set the failure dependency so the handler runs when the step fails
- C. Inspect the Dataflow Gen2 refresh error for the failing query step
- D. Add a retry policy with a delay to the failing activity
- E. Add an error branch so the failure is handled rather than ignored

### 68. A notebook reports an executor loss with no cell output. Where should the team look?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Check the failing cell and the Spark driver log
- C. Inspect the failing cell output and exit value
- D. Open the Spark UI for the application

### 69. A streaming notebook falls behind and no stage reports an error. What should be opened?

Domain: Monitor and optimize an analytics solution

- A. Send the logs to a Log Analytics workspace
- B. Check the failing cell and the Spark driver log
- C. Inspect the failing cell output and exit value
- D. Open the Spark UI for the application

### 70. A notebook failed once and also processes batches more slowly. Which two views apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Send the logs to a Log Analytics workspace
- B. Inspect the failing cell output and exit value
- C. Check the failing cell and the Spark driver log
- D. Open the Spark UI for the application
- E. Use the Monitoring hub for the run history

### 71. Some events are dropped because a field no longer matches the table schema. Where are they listed?

Domain: Monitor and optimize an analytics solution

- A. Read the Fabric audit log in the Microsoft Purview portal
- B. Use the Monitoring hub for the run history
- C. Query the ingestion failures table in the KQL database
- D. Inspect the eventstream runtime metrics

### 72. A stored procedure fails after a schema change. What identifies the object?

Domain: Monitor and optimize an analytics solution

- A. Read the activity output of the failed step
- B. Check the failing cell and the Spark driver log
- C. Read the T-SQL error message and then the query plan
- D. Check the shortcut connection and the delegated permission

### 73. A shortcut-backed table returns rows for one team and nothing for another. What should be checked?

Domain: Monitor and optimize an analytics solution

- A. Check the shortcut connection and the delegated permission
- B. Read the activity output of the failed step
- C. Read the T-SQL error message and then the query plan
- D. Check the failing cell and the Spark driver log

### 74. A streaming table writes a file every minute and queries slow as the count grows. What should be run?

Domain: Monitor and optimize an analytics solution

- A. Run VACUUM to remove the files the table no longer references
- B. Enable V-Order on the table
- C. Partition the table on the date column
- D. Run OPTIMIZE to compact the small files

### 75. Every query filters on the event date and still scans the whole table. What should be added?

Domain: Monitor and optimize an analytics solution

- A. Run VACUUM to remove the files the table no longer references
- B. Apply Z-Order on the frequently filtered columns
- C. Run OPTIMIZE to compact the small files
- D. Partition the table on the date column

### 76. A table has per-minute files and every query filters on one date column. Which two actions apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Enable V-Order on the table
- B. Run VACUUM to remove the files the table no longer references
- C. Run OPTIMIZE to compact the small files
- D. Apply Z-Order on the frequently filtered columns
- E. Partition the table on the date column

### 77. A pipeline copies ninety device folders one after another. What should be changed?

Domain: Monitor and optimize an analytics solution

- A. Insert the warehouse rows in batches rather than one at a time
- B. Raise the parallelism of the copy so independent slices move together
- C. Cache the DataFrame that is used twice
- D. Coalesce the partitions before writing the small result

### 78. A join in the warehouse picks a nested loop after a large load. What should be updated?

Domain: Monitor and optimize an analytics solution

- A. Write fewer, larger files into the warehouse table
- B. Insert the warehouse rows in batches rather than one at a time
- C. Update statistics so the optimizer sees the current distribution
- D. Join on the distribution column so the rows stay on their node

### 79. One device identifier holds forty percent of the rows and one task never finishes. What should be applied?

Domain: Monitor and optimize an analytics solution

- A. Broadcast the small dimension to avoid the shuffle
- B. Salt the skewed key so the partitions even out
- C. Enable skew join handling for the hot key
- D. Keep adaptive query execution enabled so the shuffle is re-planned

### 80. A shuffle after a volume increase produces partitions of very uneven size. What should be set?

Domain: Monitor and optimize an analytics solution

- A. Cache the DataFrame that is used twice
- B. Broadcast the small dimension to avoid the shuffle
- C. Coalesce the partitions before writing the small result
- D. Set the shuffle partition count to match the data volume

### 81. A streaming job's shuffle is planned from the wrong sizes and one key is hot. Which two features apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Broadcast the small dimension to avoid the shuffle
- B. Enable skew join handling for the hot key
- C. Set the shuffle partition count to match the data volume
- D. Salt the skewed key so the partitions even out
- E. Keep adaptive query execution enabled so the shuffle is re-planned

### 82. Two years of telemetry are retained although every query reads one day. What should be set?

Domain: Monitor and optimize an analytics solution

- A. Set the caching policy on the KQL table
- B. Move the workspace to a larger capacity
- C. Increase the eventhouse capacity so the queries keep up
- D. Set the retention policy to match the query window

### 83. Dashboard queries over the last day read from slow storage. What should be set?

Domain: Monitor and optimize an analytics solution

- A. Move the workspace to a larger capacity
- B. Set the retention policy to match the query window
- C. Set the caching policy on the KQL table
- D. Increase the eventhouse capacity so the queries keep up

### 84. The eventstream cannot deliver what the source produces at peak. What should be scaled?

Domain: Monitor and optimize an analytics solution

- A. Move the workspace to a larger capacity
- B. Increase the eventhouse capacity so the queries keep up
- C. Set the retention policy to match the query window
- D. Scale the destination throughput for the event volume

### 85. A team must be told about a failing stream, not find out later. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Review the alert history → enable the monitoring output → set the threshold → build the dashboard
- B. Build the dashboard → set the threshold → enable the output → review the history
- C. Enable the monitoring output → build the dashboard over it → set the alert threshold → review the alert history each week
- D. Set the alert threshold → build the dashboard → review the history → enable the output

### 86. A stream stops delivering and must be restored safely. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Isolate the failing activity → rerun the activity → read the run history → reproduce the input
- B. Rerun only the failed activity → read the run history → isolate the activity → reproduce the input
- C. Read the run history → isolate the failing activity → reproduce it with the same input → rerun only the failed activity
- D. Reproduce the input → isolate the activity → read the run history → rerun the activity

### 87. A dashboard query must be made faster with evidence. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Re-measure the query → optimize the table → read the plan → reduce the file count
- B. Read the query plan → reduce the file count → optimize and Z-Order the table → re-measure the query
- C. Optimize the table → re-measure the query → read the plan → reduce the file count
- D. Reduce the file count → read the plan → re-measure the query → optimize the table

### 88. Three years of telemetry must be kept while only a month is ever queried. What should be set?

Domain: Monitor and optimize an analytics solution

- A. Move the workspace to a larger capacity
- B. Increase the eventhouse capacity so the queries keep up
- C. Set the caching policy on the KQL table
- D. Set the retention policy to match the query window

---

## Case study — Beacon Health

Beacon Health monitors 4,000 patients at home with connected devices that emit a reading every minute. The clinical team needs an alert within five minutes when a reading crosses a personalised threshold, and the compliance team needs every reading retained for six years. Readings sometimes arrive out of order when a device reconnects, and a device can emit a duplicate reading for the same minute. Clinicians may see only the patients on their own caseload, and the data carries a sensitivity label that must not be lost. The organisation has an eventhouse and a warehouse and wants the alerting path separated from the reporting path.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. Clinicians may see only their own caseload patients. What should be defined?

Domain: Implement and manage an analytics solution

- A. Apply column-level security so the column is hidden from the group
- B. Define a row-level security policy on the table
- C. Apply object-level security in the semantic model
- D. Grant access at the folder that holds the restricted files

### 90. A patient reading must carry its classification into every derived table. What should be applied?

Domain: Implement and manage an analytics solution

- A. Apply the sensitivity label to the item
- B. Certify the item as the approved source
- C. Promote the item as ready for reuse
- D. Let the label inherit from the labelled source file

### 91. Every access to a patient record must be attributable. Where is that recorded?

Domain: Implement and manage an analytics solution

- A. Filter the audit log by activity and by item
- B. Export the audit events before the retention window closes
- C. Read the Fabric audit log in the Microsoft Purview portal
- D. Read the item activity log

---

## Case study — Consolidated Courier

Consolidated Courier receives a parcel scan from 1,100 depots and 90 line-haul hubs. Each scan carries a parcel identifier, a location, a scan type, and a device timestamp. The network team wants a live count of parcels at each hub, and the customer service team wants a per-parcel status that is no more than one minute old. Some depots batch their scans and upload them every fifteen minutes, so the event time and the arrival time differ. A parcel can be scanned more than once at the same location because a handheld is re-synchronised. The company has strict latency targets and cannot afford a batch job in the path.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. A quarter of delivery history must be kept for analysis. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Read the Fabric audit log in the Microsoft Purview portal
- B. Send the logs to a Log Analytics workspace
- C. Read the refresh history for the semantic model
- D. Use the Monitoring hub for the run history

### 93. Scans stop appearing at one hub during a burst. What shows the blocked side?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Read the refresh history for the semantic model
- C. Query the ingestion failures table in the KQL database
- D. Inspect the eventstream runtime metrics

### 94. A hub stops forwarding scans and nobody notices for an hour. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Set the alert to fire only after the retry policy has been exhausted
- B. Configure an alert on the failing condition
- C. Use a Data Activator rule that watches the streaming condition
- D. Send the alert to the team that owns the item

---

## Case study — Riverside Transit

Riverside Transit operates 700 buses and receives a GPS position every ten seconds from each vehicle. The operations centre needs a map of vehicle positions no more than 30 seconds old, and the planning team needs a monthly on-time performance report per route. Positions are broadcast through an event hub, and the same vehicle can appear twice in a batch when a driver swaps terminals. The transit authority publishes the on-time report to the public, so the numbers must be reproducible and the query definitions must be reviewable. The authority has one Fabric capacity that is shared with the finance department.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. Position batches must be moved and then transformed in order. What should be used?

Domain: Ingest and transform data

- A. Copy the files as binary and parse them downstream
- B. Use a Copy activity in the pipeline
- C. Append the new files instead of overwriting the target
- D. Use Get Metadata to list the files to process

### 96. The same vehicle appears twice when a driver swaps terminals. What should be applied?

Domain: Ingest and transform data

- A. Replace the missing value with a documented default
- B. Deduplicate on the business key and keep the latest record
- C. Route the failed rows to a reject table and continue the load
- D. Reprocess the affected partitions when the data arrives late

### 97. Positions must reach the map with no batch job in the path. What should be used?

Domain: Ingest and transform data

- A. Process the stream with an eventstream
- B. Run a batch job every few minutes over the landing folder
- C. Process the stream with a KQL update policy
- D. Process the stream with Spark structured streaming

---

## Case study — Tailspin Toys

Tailspin Toys manufactures toys in four plants, and every machine emits a telemetry record every five seconds. The plants have inconsistent time zones and one plant clock drifts by up to 90 seconds. The reliability team wants to detect a machine that exceeds a temperature threshold for ten consecutive readings, and the quality team wants a daily defect rate by line. Telemetry must be available for three years, but only the last 30 days are queried interactively. A plant that loses network connectivity buffers locally and replays its events when the link returns, sometimes out of order by several hours.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. Nobody can say which plant pipeline failed last night. Where should the team look?

Domain: Monitor and optimize an analytics solution

- A. Send the logs to a Log Analytics workspace
- B. Use the Monitoring hub for the run history
- C. Read the item activity log
- D. Read the refresh history for the semantic model

### 99. A machine must be flagged after ten consecutive readings above threshold. What should be used?

Domain: Monitor and optimize an analytics solution

- A. Set the alert to fire only after the retry policy has been exhausted
- B. Use a Data Activator rule that watches the streaming condition
- C. Send the alert to the team that owns the item
- D. Configure an alert on the failing condition

### 100. One plant sends most of the telemetry and one task dominates. What should be applied?

Domain: Monitor and optimize an analytics solution

- A. Salt the skewed key so the partitions even out
- B. Enable skew join handling for the hot key
- C. Broadcast the small dimension to avoid the shuffle
- D. Keep adaptive query execution enabled so the shuffle is re-planned

---

## Answer key and explanations

### Question 1 — B

Answer: Size the pool for the node family and node count the workload needs. The node family sets the memory-to-core ratio the workload needs. The node family sets the memory-to-core ratio, and the node count sets the parallelism ceiling. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Autoscale adds executors while the job runs and releases them afterwards, so idle capacity is not billed. Why the correct answer wins: The node family sets the memory-to-core ratio the workload needs.
- **B:** Correct. The node family sets the memory-to-core ratio, and the node count sets the parallelism ceiling. In this case: The node family sets the memory-to-core ratio the workload needs.
- **C:** Incorrect for this question. High concurrency lets several notebooks share one Spark session instead of starting a session each. Why the correct answer wins: The node family sets the memory-to-core ratio the workload needs.
- **D:** Incorrect for this question. A workspace Spark pool applies one node size and autoscale bound to every notebook that does not override it. Why the correct answer wins: The node family sets the memory-to-core ratio the workload needs.

### Question 2 — C

Answer: Enable autoscale with a minimum and maximum node count. Autoscale adds executors for the burst and releases them. Autoscale adds executors while the job runs and releases them afterwards, so idle capacity is not billed. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace default environment means a new notebook inherits the approved libraries without a decision. Why the correct answer wins: Autoscale adds executors for the burst and releases them.
- **B:** Incorrect for this question. A workspace Spark pool applies one node size and autoscale bound to every notebook that does not override it. Why the correct answer wins: Autoscale adds executors for the burst and releases them.
- **C:** Correct. Autoscale adds executors while the job runs and releases them afterwards, so idle capacity is not billed. In this case: Autoscale adds executors for the burst and releases them.
- **D:** Incorrect for this question. Dynamic allocation shrinks the executor set between stages, which matters when the stages are uneven. Why the correct answer wins: Autoscale adds executors for the burst and releases them.

### Question 3 — B

Answer: Keep OneLake availability enabled so other engines can read the same data. OneLake availability exposes the same files to every engine. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. Local study-map skill 1.2 (Domain and OneLake Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. Why the correct answer wins: OneLake availability exposes the same files to every engine.
- **B:** Correct. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. In this case: OneLake availability exposes the same files to every engine.
- **C:** Incorrect for this question. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. Why the correct answer wins: OneLake availability exposes the same files to every engine.
- **D:** Incorrect for this question. A domain groups workspaces for governance and discovery without moving the data. Why the correct answer wins: OneLake availability exposes the same files to every engine.

### Question 4 — D

Answer: Assign the workspace to a capacity that has headroom. Every item draws on one capacity, so headroom decides where it goes. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. Local study-map skill 1.2 (Domain and OneLake Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. Why the correct answer wins: Every item draws on one capacity, so headroom decides where it goes.
- **B:** Incorrect for this question. A domain groups workspaces for governance and discovery without moving the data. Why the correct answer wins: Every item draws on one capacity, so headroom decides where it goes.
- **C:** Incorrect for this question. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. Why the correct answer wins: Every item draws on one capacity, so headroom decides where it goes.
- **D:** Correct. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. In this case: Every item draws on one capacity, so headroom decides where it goes.

### Question 5 — C

Answer: Rewrite the existing orchestration as a Fabric pipeline instead. A DAG that cannot run in Fabric is not a reason to discard working orchestration without a decision. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. Local study-map skill 1.3 (Apache Airflow Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. Why the correct answer wins: A DAG that cannot run in Fabric is not a reason to discard working orchestration without a decision.
- **B:** Incorrect for this question. Source-controlled DAGs keep the orchestration reviewable like any other item definition. Why the correct answer wins: A DAG that cannot run in Fabric is not a reason to discard working orchestration without a decision.
- **C:** Correct. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. In this case: A DAG that cannot run in Fabric is not a reason to discard working orchestration without a decision.
- **D:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: A DAG that cannot run in Fabric is not a reason to discard working orchestration without a decision.

### Question 6 — A

Answer: Sync the Airflow DAG from the connected Git repository. Syncing the DAG from Git makes the change reviewable. Source-controlled DAGs keep the orchestration reviewable like any other item definition. Local study-map skill 1.3 (Apache Airflow Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Source-controlled DAGs keep the orchestration reviewable like any other item definition. In this case: Syncing the DAG from Git makes the change reviewable.
- **B:** Incorrect for this question. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. Why the correct answer wins: Syncing the DAG from Git makes the change reviewable.
- **C:** Incorrect for this question. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. Why the correct answer wins: Syncing the DAG from Git makes the change reviewable.
- **D:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: Syncing the DAG from Git makes the change reviewable.

### Question 7 — B

Answer: Add the generated artefacts to the ignore file rather than committing them. Build output belongs in the ignore file, not in the commit. Committing build output makes every run look like a change. Local study-map skill 1.4 (Version Control and Database Projects), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. An unresolved conflict blocks the update and leaves the workspace and the branch out of step. Why the correct answer wins: Build output belongs in the ignore file, not in the commit.
- **B:** Correct. Committing build output makes every run look like a change. In this case: Build output belongs in the ignore file, not in the commit.
- **C:** Incorrect for this question. Git keeps a reviewable history of every item definition instead of an untracked live workspace. Why the correct answer wins: Build output belongs in the ignore file, not in the commit.
- **D:** Incorrect for this question. Branching keeps unfinished work out of the shared workspace and makes the change reviewable. Why the correct answer wins: Build output belongs in the ignore file, not in the commit.

### Question 8 — C

Answer: Use SQLCMD variables for the environment-specific values. SQLCMD variables keep the environment values out of the artefact. SQLCMD variables keep one project artefact deployable to both test and production. Local study-map skill 1.4 (Version Control and Database Projects), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The DACPAC is the versioned schema artefact that the deployment consumes. Why the correct answer wins: SQLCMD variables keep the environment values out of the artefact.
- **B:** Incorrect for this question. Git keeps a reviewable history of every item definition instead of an untracked live workspace. Why the correct answer wins: SQLCMD variables keep the environment values out of the artefact.
- **C:** Correct. SQLCMD variables keep one project artefact deployable to both test and production. In this case: SQLCMD variables keep the environment values out of the artefact.
- **D:** Incorrect for this question. A database project keeps the warehouse schema in source control and deploys it repeatably. Why the correct answer wins: SQLCMD variables keep the environment values out of the artefact.

### Question 9 — D

Answer: Select only the items that belong in the target stage. Selecting the items keeps unfinished work out of the release. Promoting every item drags unrelated work into the release. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A rule stops a promotion from overwriting the target stage environment-specific settings. Why the correct answer wins: Selecting the items keeps unfinished work out of the release.
- **B:** Incorrect for this question. The pipeline promotes the same item definitions through the stages instead of rebuilding them. Why the correct answer wins: Selecting the items keeps unfinished work out of the release.
- **C:** Incorrect for this question. The comparison shows what the promotion will change in the target before it happens. Why the correct answer wins: Selecting the items keeps unfinished work out of the release.
- **D:** Correct. Promoting every item drags unrelated work into the release. In this case: Selecting the items keeps unfinished work out of the release.

### Question 10 — A

Answer: Deploy backwards to recover the last known-good definition. A backward deployment restores the previous stage state. A backward deployment is the supported way to restore a previous stage state. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A backward deployment is the supported way to restore a previous stage state. In this case: A backward deployment restores the previous stage state.
- **B:** Incorrect for this question. The pipeline promotes the same item definitions through the stages instead of rebuilding them. Why the correct answer wins: A backward deployment restores the previous stage state.
- **C:** Incorrect for this question. A rule stops a promotion from overwriting the target stage environment-specific settings. Why the correct answer wins: A backward deployment restores the previous stage state.
- **D:** Incorrect for this question. The comparison shows what the promotion will change in the target before it happens. Why the correct answer wins: A backward deployment restores the previous stage state.

### Question 11 — C

Answer: Grant Admin on the workspace to the platform team. Admin manages access and settings, and the data controls limit what is read. Admin is needed to manage access and settings, not to read the data. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Viewer allows reading the items without editing them. Why the correct answer wins: Admin manages access and settings, and the data controls limit what is read.
- **B:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: Admin manages access and settings, and the data controls limit what is read.
- **C:** Correct. Admin is needed to manage access and settings, not to read the data. In this case: Admin manages access and settings, and the data controls limit what is read.
- **D:** Incorrect for this question. Read is the narrowest grant that still lets the item be consumed. Why the correct answer wins: Admin manages access and settings, and the data controls limit what is read.

### Question 12 — A

Answer: Share a link to the item with the required permission. A link with the required permission opens that item. A link is a shortcut to the item, not a substitute for the permission behind it. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A link is a shortcut to the item, not a substitute for the permission behind it. In this case: A link with the required permission opens that item.
- **B:** Incorrect for this question. Item-level sharing avoids granting a workspace role for one report. Why the correct answer wins: A link with the required permission opens that item.
- **C:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: A link with the required permission opens that item.
- **D:** Incorrect for this question. Read is the narrowest grant that still lets the item be consumed. Why the correct answer wins: A link with the required permission opens that item.

### Question 13 — C, E

Answers: Share the single item with the user who needs only that item; Grant Read on the item. Item sharing gives the item, and Read is the narrowest permission on it. Item-level sharing avoids granting a workspace role for one report. Read is the narrowest grant that still lets the item be consumed. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: Item sharing gives the item, and Read is the narrowest permission on it.
- **B:** Incorrect for this question. Viewer allows reading the items without editing them. Why the correct answer wins: Item sharing gives the item, and Read is the narrowest permission on it.
- **C:** Correct. Item-level sharing avoids granting a workspace role for one report. In this case: Item sharing gives the item, and Read is the narrowest permission on it.
- **D:** Incorrect for this question. A link is a shortcut to the item, not a substitute for the permission behind it. Why the correct answer wins: Item sharing gives the item, and Read is the narrowest permission on it.
- **E:** Correct. Read is the narrowest grant that still lets the item be consumed. In this case: Item sharing gives the item, and Read is the narrowest permission on it.

### Question 14 — D

Answer: Grant access at the folder that holds the restricted files. A folder grant restricts the path and leaves the lakehouse readable. A folder grant restricts the path without hiding the whole lakehouse. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Row-level security filters rows per identity, so one table returns different rows to different users. Why the correct answer wins: A folder grant restricts the path and leaves the lakehouse readable.
- **B:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: A folder grant restricts the path and leaves the lakehouse readable.
- **C:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: A folder grant restricts the path and leaves the lakehouse readable.
- **D:** Correct. A folder grant restricts the path without hiding the whole lakehouse. In this case: A folder grant restricts the path and leaves the lakehouse readable.

### Question 15 — A

Answer: Apply column-level security so the column is hidden from the group. Column-level security hides the column and leaves the table readable. Column-level security hides the column while leaving the rest of the table readable. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Column-level security hides the column while leaving the rest of the table readable. In this case: Column-level security hides the column and leaves the table readable.
- **B:** Incorrect for this question. Row-level security filters rows per identity, so one table returns different rows to different users. Why the correct answer wins: Column-level security hides the column and leaves the table readable.
- **C:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: Column-level security hides the column and leaves the table readable.
- **D:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: Column-level security hides the column and leaves the table readable.

### Question 16 — B

Answer: Mask the column in the report layer only. A mask applied in the report protects one visual only. A report-level mask protects one visual and leaves every other consumer unmasked. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Masking shows a masked value to unauthorised users while the stored data stays intact. Why the correct answer wins: A mask applied in the report protects one visual only.
- **B:** Correct. A report-level mask protects one visual and leaves every other consumer unmasked. In this case: A mask applied in the report protects one visual only.
- **C:** Incorrect for this question. The masking rule needs the exemption, or the authorised group sees masked values too. Why the correct answer wins: A mask applied in the report protects one visual only.
- **D:** Incorrect for this question. A view removes the column entirely, which is not the same as masking the value. Why the correct answer wins: A mask applied in the report protects one visual only.

### Question 17 — B, D

Answers: Apply dynamic data masking to the column; Expose a view with the column omitted instead of masking it. The mask protects the value, and the view removes the column. Masking shows a masked value to unauthorised users while the stored data stays intact. A view removes the column entirely, which is not the same as masking the value. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A report-level mask protects one visual and leaves every other consumer unmasked. Why the correct answer wins: The mask protects the value, and the view removes the column.
- **B:** Correct. Masking shows a masked value to unauthorised users while the stored data stays intact. In this case: The mask protects the value, and the view removes the column.
- **C:** Incorrect for this question. The masking rule needs the exemption, or the authorised group sees masked values too. Why the correct answer wins: The mask protects the value, and the view removes the column.
- **D:** Correct. A view removes the column entirely, which is not the same as masking the value. In this case: The mask protects the value, and the view removes the column.
- **E:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: The mask protects the value, and the view removes the column.

### Question 18 — C

Answer: Let the label inherit from the labelled source file. Inheritance keeps one classification instead of a second opinion. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A default label classifies new items that nobody labels by hand. Why the correct answer wins: Inheritance keeps one classification instead of a second opinion.
- **B:** Incorrect for this question. The label travels with the item and drives the protection downstream consumers inherit. Why the correct answer wins: Inheritance keeps one classification instead of a second opinion.
- **C:** Correct. In this case: Inheritance keeps one classification instead of a second opinion.
- **D:** Incorrect for this question. Certification tells consumers the item has been reviewed as authoritative. Why the correct answer wins: Inheritance keeps one classification instead of a second opinion.

### Question 19 — C, D

Answers: Let the label inherit from the labelled source file; Set the default sensitivity label for the workspace. The default labels new items, and inheritance carries the classification. Inheritance keeps one classification instead of a second opinion on the same data. A default label classifies new items that nobody labels by hand. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Certification tells consumers the item has been reviewed as authoritative. Why the correct answer wins: The default labels new items, and inheritance carries the classification.
- **B:** Incorrect for this question. Promotion signals readiness without the review that certification implies. Why the correct answer wins: The default labels new items, and inheritance carries the classification.
- **C:** Correct. A default label classifies new items that nobody labels by hand. In this case: The default labels new items, and inheritance carries the classification.
- **D:** Correct. Inheritance keeps one classification instead of a second opinion on the same data. In this case: The default labels new items, and inheritance carries the classification.
- **E:** Incorrect for this question. The label travels with the item and drives the protection downstream consumers inherit. Why the correct answer wins: The default labels new items, and inheritance carries the classification.

### Question 20 — D

Answer: Filter the audit log by activity and by item. Filtering the audit log turns it into the events that answer the question. Filtering turns a very large log into the events that answer the question. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: Filtering the audit log turns it into the events that answer the question.
- **B:** Incorrect for this question. The audit log has a retention window, so an investigation that starts late needs the export. Why the correct answer wins: Filtering the audit log turns it into the events that answer the question.
- **C:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: Filtering the audit log turns it into the events that answer the question.
- **D:** Correct. Filtering turns a very large log into the events that answer the question. In this case: Filtering the audit log turns it into the events that answer the question.

### Question 21 — B, D

Answers: Read the Fabric audit log in the Microsoft Purview portal; Export the audit events before the retention window closes. The audit log holds the event, and the export preserves it. The audit log records who did what to which item and when. The audit log has a retention window, so an investigation that starts late needs the export. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The audit log holds the event, and the export preserves it.
- **B:** Correct. The audit log records who did what to which item and when. In this case: The audit log holds the event, and the export preserves it.
- **C:** Incorrect for this question. Filtering turns a very large log into the events that answer the question. Why the correct answer wins: The audit log holds the event, and the export preserves it.
- **D:** Correct. The audit log has a retention window, so an investigation that starts late needs the export. In this case: The audit log holds the event, and the export preserves it.
- **E:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The audit log holds the event, and the export preserves it.

### Question 22 — A

Answer: Scope the OneLake role to the folder that holds the restricted table. A folder-scoped OneLake role restricts the data itself. A folder-scoped role restricts exactly the data rather than the whole lakehouse. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A folder-scoped role restricts exactly the data rather than the whole lakehouse. In this case: A folder-scoped OneLake role restricts the data itself.
- **B:** Incorrect for this question. A group grant is maintained once instead of once per person. Why the correct answer wins: A folder-scoped OneLake role restricts the data itself.
- **C:** Incorrect for this question. OneLake security governs data access independently of the workspace role. Why the correct answer wins: A folder-scoped OneLake role restricts the data itself.
- **D:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: A folder-scoped OneLake role restricts the data itself.

### Question 23 — C, E

Answers: Configure OneLake security roles for the lakehouse; Scope the OneLake role to the folder that holds the restricted table. OneLake security governs the data, and the folder scope limits it. OneLake security governs data access independently of the workspace role. A folder-scoped role restricts exactly the data rather than the whole lakehouse. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: OneLake security governs the data, and the folder scope limits it.
- **B:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: OneLake security governs the data, and the folder scope limits it.
- **C:** Correct. A folder-scoped role restricts exactly the data rather than the whole lakehouse. In this case: OneLake security governs the data, and the folder scope limits it.
- **D:** Incorrect for this question. A group grant is maintained once instead of once per person. Why the correct answer wins: OneLake security governs the data, and the folder scope limits it.
- **E:** Correct. OneLake security governs data access independently of the workspace role. In this case: OneLake security governs the data, and the folder scope limits it.

### Question 24 — D

Answer: Use a notebook for the transformation. A notebook is the place for PySpark that low-code cannot express. A notebook is the right place for PySpark that a low-code transform cannot express. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Why the correct answer wins: A notebook is the place for PySpark that low-code cannot express.
- **B:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: A notebook is the place for PySpark that low-code cannot express.
- **C:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: A notebook is the place for PySpark that low-code cannot express.
- **D:** Correct. A notebook is the right place for PySpark that a low-code transform cannot express. In this case: A notebook is the place for PySpark that low-code cannot express.

### Question 25 — A

Answer: Use a pipeline for the copy and the orchestration. A pipeline owns the copy, the order, and the dependency. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A pipeline owns the scheduling, the copy activity, and the dependency between steps. In this case: A pipeline owns the copy, the order, and the dependency.
- **B:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: A pipeline owns the copy, the order, and the dependency.
- **C:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: A pipeline owns the copy, the order, and the dependency.
- **D:** Incorrect for this question. KQL is the native language of the eventhouse tables. Why the correct answer wins: A pipeline owns the copy, the order, and the dependency.

### Question 26 — A, B

Answers: Use a pipeline for the copy and the orchestration; Use a KQL query against the eventhouse. The pipeline copies and orders, and KQL queries the eventhouse. A pipeline owns the scheduling, the copy activity, and the dependency between steps. KQL is the native language of the eventhouse tables. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A pipeline owns the scheduling, the copy activity, and the dependency between steps. In this case: The pipeline copies and orders, and KQL queries the eventhouse.
- **B:** Correct. KQL is the native language of the eventhouse tables. In this case: The pipeline copies and orders, and KQL queries the eventhouse.
- **C:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: The pipeline copies and orders, and KQL queries the eventhouse.
- **D:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: The pipeline copies and orders, and KQL queries the eventhouse.
- **E:** Incorrect for this question. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Why the correct answer wins: The pipeline copies and orders, and KQL queries the eventhouse.

### Question 27 — C

Answer: Use an Until loop with a timeout for the long-running check. Until repeats the check and stops at the timeout. Until repeats the check and stops when the condition is met or the timeout expires. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The schedule trigger is what makes the run recur without a person starting it. Why the correct answer wins: Until repeats the check and stops at the timeout.
- **B:** Incorrect for this question. A variable carries the computed value between the activities that need it. Why the correct answer wins: Until repeats the check and stops at the timeout.
- **C:** Correct. Until repeats the check and stops when the condition is met or the timeout expires. In this case: Until repeats the check and stops at the timeout.
- **D:** Incorrect for this question. The lookup is what makes the load incremental rather than a full reload. Why the correct answer wins: Until repeats the check and stops at the timeout.

### Question 28 — B

Answer: Set the value in a pipeline variable and reference the variable. A pipeline variable carries the value between activities. A variable carries the computed value between the activities that need it. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The lookup is what makes the load incremental rather than a full reload. Why the correct answer wins: A pipeline variable carries the value between activities.
- **B:** Correct. A variable carries the computed value between the activities that need it. In this case: A pipeline variable carries the value between activities.
- **C:** Incorrect for this question. A dynamic expression computes the path instead of hard-coding a date. Why the correct answer wins: A pipeline variable carries the value between activities.
- **D:** Incorrect for this question. A parameter makes one pipeline reusable across folders and environments. Why the correct answer wins: A pipeline variable carries the value between activities.

### Question 29 — B

Answer: Choose the capacity and region → create the workspace → assign the domain → grant the workspace roles. The region and capacity come before the workspace, and access after it. The region is fixed at creation, so it is decided before the workspace exists, and access is granted after it does. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A domain assignment and a role grant both need the workspace, and the capacity is not a last step. Why the correct answer wins: The region and capacity come before the workspace, and access after it.
- **B:** Correct. The region is fixed at creation, so it is decided before the workspace exists, and access is granted after it does. In this case: The region and capacity come before the workspace, and access after it.
- **C:** Incorrect for this question. Roles cannot be granted before the workspace exists, and the capacity is chosen before, not after. Why the correct answer wins: The region and capacity come before the workspace, and access after it.
- **D:** Incorrect for this question. The region cannot be changed after creation, so choosing it later is not possible. Why the correct answer wins: The region and capacity come before the workspace, and access after it.

### Question 30 — C

Answer: Decide which work is copy, which is orchestration, and which needs PySpark → build the pipeline → add the notebook activity → parameterise the run. The work split decides the items before anything is built. The work split decides the items, and the parameter is added once the pipeline has a step to parameterise. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. There is no run to parameterise and no pipeline to hold the activity before either exists. Why the correct answer wins: The work split decides the items before anything is built.
- **B:** Incorrect for this question. Building before the split produces the wrong items, and a parameter without the notebook has nothing to drive. Why the correct answer wins: The work split decides the items before anything is built.
- **C:** Correct. The work split decides the items, and the parameter is added once the pipeline has a step to parameterise. In this case: The work split decides the items before anything is built.
- **D:** Incorrect for this question. The activity needs the pipeline, and the split is the decision that tells you which activities to add. Why the correct answer wins: The work split decides the items before anything is built.

### Question 31 — D

Answer: Reprocess the affected partitions when the data arrives late. Reprocessing the affected partitions corrects the published totals. Reprocessing the partition corrects the aggregate that was already published. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Reprocessing the affected partitions corrects the published totals.
- **B:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Reprocessing the affected partitions corrects the published totals.
- **C:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: Reprocessing the affected partitions corrects the published totals.
- **D:** Correct. Reprocessing the partition corrects the aggregate that was already published. In this case: Reprocessing the affected partitions corrects the published totals.

### Question 32 — B

Answer: Load only the rows newer than the stored watermark. An incremental load moves the delta instead of the history. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: An incremental load moves the delta instead of the history.
- **B:** Correct. In this case: An incremental load moves the delta instead of the history.
- **C:** Incorrect for this question. The control table is what lets the next run know where this one stopped. Why the correct answer wins: An incremental load moves the delta instead of the history.
- **D:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: An incremental load moves the delta instead of the history.

### Question 33 — A

Answer: Generate a surrogate key instead of reusing the source key. A surrogate key keeps the two devices apart even when the source key repeats. A surrogate key decouples the warehouse from the source system identifiers. Local study-map skill 2.2 (Dimensional Model Preparation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. A surrogate key decouples the warehouse from the source system identifiers. In this case: A surrogate key keeps the two devices apart even when the source key repeats.
- **B:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: A surrogate key keeps the two devices apart even when the source key repeats.
- **C:** Incorrect for this question. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. Why the correct answer wins: A surrogate key keeps the two devices apart even when the source key repeats.
- **D:** Incorrect for this question. A star schema keeps the fact table narrow and the dimensions reusable. Why the correct answer wins: A surrogate key keeps the two devices apart even when the source key repeats.

### Question 34 — C

Answer: Model the data as a star schema with conformed dimensions. A star schema keeps the facts narrow and the dimensions reusable. A star schema keeps the fact table narrow and the dimensions reusable. Local study-map skill 2.2 (Dimensional Model Preparation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. Why the correct answer wins: A star schema keeps the facts narrow and the dimensions reusable.
- **B:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: A star schema keeps the facts narrow and the dimensions reusable.
- **C:** Correct. A star schema keeps the fact table narrow and the dimensions reusable. In this case: A star schema keeps the facts narrow and the dimensions reusable.
- **D:** Incorrect for this question. Denormalization trades storage for the query shape the report actually uses. Why the correct answer wins: A star schema keeps the facts narrow and the dimensions reusable.

### Question 35 — A

Answer: Set a checkpoint location for the streaming query. The checkpoint records where the query should resume. The checkpoint is what makes the stream restart from where it stopped. Local study-map skill 2.3 (Streaming Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. The checkpoint is what makes the stream restart from where it stopped. In this case: The checkpoint records where the query should resume.
- **B:** Incorrect for this question. A watermark sets how long the engine waits for late events before closing a window. Why the correct answer wins: The checkpoint records where the query should resume.
- **C:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: The checkpoint records where the query should resume.
- **D:** Incorrect for this question. Native tables give full KQL capability over the streaming data. Why the correct answer wins: The checkpoint records where the query should resume.

### Question 36 — B, D

Answers: Set a checkpoint location for the streaming query; Set a watermark so late events are handled deterministically. The checkpoint resumes the query, and the watermark bounds the lateness. The checkpoint is what makes the stream restart from where it stopped. A watermark sets how long the engine waits for late events before closing a window. Local study-map skill 2.3 (Streaming Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Native tables give full KQL capability over the streaming data. Why the correct answer wins: The checkpoint resumes the query, and the watermark bounds the lateness.
- **B:** Correct. The checkpoint is what makes the stream restart from where it stopped. In this case: The checkpoint resumes the query, and the watermark bounds the lateness.
- **C:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: The checkpoint resumes the query, and the watermark bounds the lateness.
- **D:** Correct. A watermark sets how long the engine waits for late events before closing a window. In this case: The checkpoint resumes the query, and the watermark bounds the lateness.
- **E:** Incorrect for this question. An eventstream is the no-code path from a source to a destination. Why the correct answer wins: The checkpoint resumes the query, and the watermark bounds the lateness.

### Question 37 — B

Answer: Store the stream in native tables in the eventhouse. Native tables give full KQL capability over the streaming data. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A KQL database indexes the timestamp column for the range queries the dashboards run. Why the correct answer wins: Native tables give full KQL capability over the streaming data.
- **B:** Correct. In this case: Native tables give full KQL capability over the streaming data.
- **C:** Incorrect for this question. A warehouse gives multi-table T-SQL transactions and a governed relational model. Why the correct answer wins: Native tables give full KQL capability over the streaming data.
- **D:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: Native tables give full KQL capability over the streaming data.

### Question 38 — D

Answer: Query the stream through a OneLake shortcut. A OneLake shortcut exposes the data to the other engines. The shortcut exposes the data to engines that do not query KQL directly. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Native tables give full KQL capability over the streaming data. Why the correct answer wins: A OneLake shortcut exposes the data to the other engines.
- **B:** Incorrect for this question. A KQL database indexes the timestamp column for the range queries the dashboards run. Why the correct answer wins: A OneLake shortcut exposes the data to the other engines.
- **C:** Incorrect for this question. An eventhouse is optimized for high-volume time-series queries. Why the correct answer wins: A OneLake shortcut exposes the data to the other engines.
- **D:** Correct. The shortcut exposes the data to engines that do not query KQL directly. In this case: A OneLake shortcut exposes the data to the other engines.

### Question 39 — A, C

Answers: Store the stream in native tables in the eventhouse; Query the stream through a OneLake shortcut. Native tables serve KQL, and the shortcut serves the other engines. Native tables give full KQL capability over the streaming data. The shortcut exposes the data to engines that do not query KQL directly. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Native tables give full KQL capability over the streaming data. In this case: Native tables serve KQL, and the shortcut serves the other engines.
- **B:** Incorrect for this question. The endpoint gives read-only T-SQL over the Delta tables without a copy. Why the correct answer wins: Native tables serve KQL, and the shortcut serves the other engines.
- **C:** Correct. The shortcut exposes the data to engines that do not query KQL directly. In this case: Native tables serve KQL, and the shortcut serves the other engines.
- **D:** Incorrect for this question. A warehouse gives multi-table T-SQL transactions and a governed relational model. Why the correct answer wins: Native tables serve KQL, and the shortcut serves the other engines.
- **E:** Incorrect for this question. A KQL database indexes the timestamp column for the range queries the dashboards run. Why the correct answer wins: Native tables serve KQL, and the shortcut serves the other engines.

### Question 40 — A

Answer: Process the stream with Spark structured streaming. Structured streaming reuses the batch logic on an unbounded source. Structured streaming suits stateful processing and the same PySpark logic used in batch. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Structured streaming suits stateful processing and the same PySpark logic used in batch. In this case: Structured streaming reuses the batch logic on an unbounded source.
- **B:** Incorrect for this question. A batch job over the landing folder adds latency the streaming requirement may not allow. Why the correct answer wins: Structured streaming reuses the batch logic on an unbounded source.
- **C:** Incorrect for this question. An eventstream is the no-code path from a source to a destination. Why the correct answer wins: Structured streaming reuses the batch logic on an unbounded source.
- **D:** Incorrect for this question. An update policy transforms the data as it lands in the KQL table. Why the correct answer wins: Structured streaming reuses the batch logic on an unbounded source.

### Question 41 — A

Answer: Transform with KQL in the eventhouse. KQL is the native language for the eventhouse tables. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. In this case: KQL is the native language for the eventhouse tables.
- **B:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: KQL is the native language for the eventhouse tables.
- **C:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: KQL is the native language for the eventhouse tables.
- **D:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: KQL is the native language for the eventhouse tables.

### Question 42 — A, C

Answers: Process the stream with Spark structured streaming; Transform with KQL in the eventhouse. Structured streaming reuses the logic, and KQL transforms on arrival. Structured streaming suits stateful processing and the same PySpark logic used in batch. KQL is the native language for the eventhouse tables. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Structured streaming suits stateful processing and the same PySpark logic used in batch. In this case: Structured streaming reuses the logic, and KQL transforms on arrival.
- **B:** Incorrect for this question. An eventstream is the no-code path from a source to a destination. Why the correct answer wins: Structured streaming reuses the logic, and KQL transforms on arrival.
- **C:** Correct. KQL is the native language for the eventhouse tables. In this case: Structured streaming reuses the logic, and KQL transforms on arrival.
- **D:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: Structured streaming reuses the logic, and KQL transforms on arrival.
- **E:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: Structured streaming reuses the logic, and KQL transforms on arrival.

### Question 43 — A

Answer: Create an ADLS Gen2 shortcut to the external container. An ADLS Gen2 shortcut exposes the container without a copy. The shortcut exposes the external container as if the files were in OneLake. Local study-map skill 2.6 (OneLake Shortcuts), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. The shortcut exposes the external container as if the files were in OneLake. In this case: An ADLS Gen2 shortcut exposes the container without a copy.
- **B:** Incorrect for this question. A copy duplicates the data, so the source of truth is no longer one place. Why the correct answer wins: An ADLS Gen2 shortcut exposes the container without a copy.
- **C:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: An ADLS Gen2 shortcut exposes the container without a copy.
- **D:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: An ADLS Gen2 shortcut exposes the container without a copy.

### Question 44 — B

Answer: Enable query acceleration on the shortcut. Query acceleration caches the columns the report reads. Query acceleration caches the columns a report reads, so the remote source is not scanned per query. Local study-map skill 2.6 (OneLake Shortcuts), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The shortcut exposes the external container as if the files were in OneLake. Why the correct answer wins: Query acceleration caches the columns the report reads.
- **B:** Correct. Query acceleration caches the columns a report reads, so the remote source is not scanned per query. In this case: Query acceleration caches the columns the report reads.
- **C:** Incorrect for this question. A copy duplicates the data, so the source of truth is no longer one place. Why the correct answer wins: Query acceleration caches the columns the report reads.
- **D:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: Query acceleration caches the columns the report reads.

### Question 45 — B

Answer: Enable mirroring for the operational database. Mirroring replicates the source tables continuously into OneLake without a schedule. Local study-map skill 2.7 (Mirroring), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: Mirroring replicates the source tables continuously into OneLake without a schedule.
- **B:** Correct. In this case: Mirroring replicates the source tables continuously into OneLake without a schedule.
- **C:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: Mirroring replicates the source tables continuously into OneLake without a schedule.
- **D:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: Mirroring replicates the source tables continuously into OneLake without a schedule.

### Question 46 — C

Answer: Append the new files instead of overwriting the target. Appending keeps the loads the incremental pattern depends on. Appending preserves the earlier loads that the incremental pattern depends on. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Get Metadata turns an unknown folder into a list the loop can iterate. Why the correct answer wins: Appending keeps the loads the incremental pattern depends on.
- **B:** Incorrect for this question. Deleting after success prevents the same file being loaded twice. Why the correct answer wins: Appending keeps the loads the incremental pattern depends on.
- **C:** Correct. Appending preserves the earlier loads that the incremental pattern depends on. In this case: Appending keeps the loads the incremental pattern depends on.
- **D:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: Appending keeps the loads the incremental pattern depends on.

### Question 47 — B

Answer: Use Get Metadata to list the files to process. Get Metadata turns the folder into a list the loop can iterate. Get Metadata turns an unknown folder into a list the loop can iterate. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: Get Metadata turns the folder into a list the loop can iterate.
- **B:** Correct. Get Metadata turns an unknown folder into a list the loop can iterate. In this case: Get Metadata turns the folder into a list the loop can iterate.
- **C:** Incorrect for this question. ForEach applies the same pattern to every object the lookup returned. Why the correct answer wins: Get Metadata turns the folder into a list the loop can iterate.
- **D:** Incorrect for this question. Deleting after success prevents the same file being loaded twice. Why the correct answer wins: Get Metadata turns the folder into a list the loop can iterate.

### Question 48 — C

Answer: Use a window function to rank within the partition. A window function reads the previous row without collapsing it. A window computes across related rows without collapsing them into one. Local study-map skill 2.9 (PySpark Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: A window function reads the previous row without collapsing it.
- **B:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: A window function reads the previous row without collapsing it.
- **C:** Correct. A window computes across related rows without collapsing them into one. In this case: A window function reads the previous row without collapsing it.
- **D:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: A window function reads the previous row without collapsing it.

### Question 49 — C, D

Answers: Transform with PySpark in a notebook; Use a window function to rank within the partition. PySpark scales the cleansing, and the window function ranks. PySpark handles the row-level and windowed transformations that Spark scales. A window computes across related rows without collapsing them into one. Local study-map skill 2.9 (PySpark Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: PySpark scales the cleansing, and the window function ranks.
- **B:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: PySpark scales the cleansing, and the window function ranks.
- **C:** Correct. PySpark handles the row-level and windowed transformations that Spark scales. In this case: PySpark scales the cleansing, and the window function ranks.
- **D:** Correct. A window computes across related rows without collapsing them into one. In this case: PySpark scales the cleansing, and the window function ranks.
- **E:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: PySpark scales the cleansing, and the window function ranks.

### Question 50 — C

Answer: Transform with T-SQL against the warehouse. T-SQL is the natural engine once the data is relational there. T-SQL is the right engine once the data is relational and already in the warehouse. Local study-map skill 2.10 (T-SQL and KQL Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: T-SQL is the natural engine once the data is relational there.
- **B:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: T-SQL is the natural engine once the data is relational there.
- **C:** Correct. T-SQL is the right engine once the data is relational and already in the warehouse. In this case: T-SQL is the natural engine once the data is relational there.
- **D:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: T-SQL is the natural engine once the data is relational there.

### Question 51 — C

Answer: Denormalize the model so the report needs no join. Denormalization trades storage for the query shape actually used. Denormalization trades storage for the query shape the report actually uses. Local study-map skill 2.11 (Denormalization, Grouping, and Aggregation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: Denormalization trades storage for the query shape actually used.
- **B:** Incorrect for this question. A star schema keeps the fact table narrow and the dimensions reusable. Why the correct answer wins: Denormalization trades storage for the query shape actually used.
- **C:** Correct. Denormalization trades storage for the query shape the report actually uses. In this case: Denormalization trades storage for the query shape actually used.
- **D:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: Denormalization trades storage for the query shape actually used.

### Question 52 — B

Answer: Union the sources after conforming the columns. The columns must be conformed before the union is valid. Conforming the columns first is what makes the union valid. Local study-map skill 2.11 (Denormalization, Grouping, and Aggregation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Denormalization trades storage for the query shape the report actually uses. Why the correct answer wins: The columns must be conformed before the union is valid.
- **B:** Correct. Conforming the columns first is what makes the union valid. In this case: The columns must be conformed before the union is valid.
- **C:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: The columns must be conformed before the union is valid.
- **D:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: The columns must be conformed before the union is valid.

### Question 53 — A

Answer: Deduplicate on the business key and keep the latest record. Deduplication leaves one row per business key. Deduplication makes the target one row per business key. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Deduplication makes the target one row per business key. In this case: Deduplication leaves one row per business key.
- **B:** Incorrect for this question. Reprocessing the partition corrects the aggregate that was already published. Why the correct answer wins: Deduplication leaves one row per business key.
- **C:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Deduplication leaves one row per business key.
- **D:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Deduplication leaves one row per business key.

### Question 54 — C, D

Answers: Deduplicate on the business key and keep the latest record; Reprocess the affected partitions when the data arrives late. Deduplication resolves the duplicates, and reprocessing handles the replay. Deduplication makes the target one row per business key. Reprocessing the partition corrects the aggregate that was already published. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Deduplication resolves the duplicates, and reprocessing handles the replay.
- **B:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Deduplication resolves the duplicates, and reprocessing handles the replay.
- **C:** Correct. Reprocessing the partition corrects the aggregate that was already published. In this case: Deduplication resolves the duplicates, and reprocessing handles the replay.
- **D:** Correct. Deduplication makes the target one row per business key. In this case: Deduplication resolves the duplicates, and reprocessing handles the replay.
- **E:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: Deduplication resolves the duplicates, and reprocessing handles the replay.

### Question 55 — C

Answer: Run a batch job every few minutes over the landing folder. A batch job adds latency the requirement may not allow, so the engine choice must be revisited. A batch job over the landing folder adds latency the streaming requirement may not allow. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. An eventstream is the no-code path from a source to a destination. Why the correct answer wins: A batch job adds latency the requirement may not allow, so the engine choice must be revisited.
- **B:** Incorrect for this question. Structured streaming suits stateful processing and the same PySpark logic used in batch. Why the correct answer wins: A batch job adds latency the requirement may not allow, so the engine choice must be revisited.
- **C:** Correct. A batch job over the landing folder adds latency the streaming requirement may not allow. In this case: A batch job adds latency the requirement may not allow, so the engine choice must be revisited.
- **D:** Incorrect for this question. An update policy transforms the data as it lands in the KQL table. Why the correct answer wins: A batch job adds latency the requirement may not allow, so the engine choice must be revisited.

### Question 56 — A

Answer: Define the eventstream source → add the destination → create the KQL table → build the materialized view → alert on the aggregate. Source and destination precede the table, the view, and the alert. The source and destination define the pipeline, the table receives the events, the view aggregates them, and the alert reads the aggregate. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. The source and destination define the pipeline, the table receives the events, the view aggregates them, and the alert reads the aggregate. In this case: Source and destination precede the table, the view, and the alert.
- **B:** Incorrect for this question. A destination with no source receives nothing, and the source is the first decision. Why the correct answer wins: Source and destination precede the table, the view, and the alert.
- **C:** Incorrect for this question. The alert has nothing to read until the view, the table, and the stream exist. Why the correct answer wins: Source and destination precede the table, the view, and the alert.
- **D:** Incorrect for this question. The alert fires before the destination and the view that produce the aggregate. Why the correct answer wins: Source and destination precede the table, the view, and the alert.

### Question 57 — D

Answer: Use a hopping window when the intervals must overlap. A hopping window covers overlapping intervals. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A tumbling window covers fixed, non-overlapping intervals. Why the correct answer wins: A hopping window covers overlapping intervals.
- **B:** Incorrect for this question. A sliding window emits on the event that satisfies the condition rather than on a fixed boundary. Why the correct answer wins: A hopping window covers overlapping intervals.
- **C:** Incorrect for this question. A materialized view keeps the aggregate fresh instead of recomputing it per query. Why the correct answer wins: A hopping window covers overlapping intervals.
- **D:** Correct. In this case: A hopping window covers overlapping intervals.

### Question 58 — A

Answer: Create a materialized view for the repeated aggregation. A materialized view keeps the aggregate fresh. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. In this case: A materialized view keeps the aggregate fresh.
- **B:** Incorrect for this question. A hopping window covers overlapping intervals so a trend can be smoothed. Why the correct answer wins: A materialized view keeps the aggregate fresh.
- **C:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: A materialized view keeps the aggregate fresh.
- **D:** Incorrect for this question. A tumbling window covers fixed, non-overlapping intervals. Why the correct answer wins: A materialized view keeps the aggregate fresh.

### Question 59 — A

Answer: Land the raw files unchanged → validate the schema and reject the bad rows → conform and deduplicate into silver → publish the gold table. Landing and validation precede conformity and publication. Raw data is preserved, validation happens before any transformation hides a problem, and the curated table is the last thing published. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Raw data is preserved, validation happens before any transformation hides a problem, and the curated table is the last thing published. In this case: Landing and validation precede conformity and publication.
- **B:** Incorrect for this question. The published table would be rebuilt from data that has not landed yet. Why the correct answer wins: Landing and validation precede conformity and publication.
- **C:** Incorrect for this question. There is nothing to validate and nothing to publish before the raw files exist. Why the correct answer wins: Landing and validation precede conformity and publication.
- **D:** Incorrect for this question. Conforming before the raw data lands transforms whatever was already there, and validation after publication is too late. Why the correct answer wins: Landing and validation precede conformity and publication.

### Question 60 — D

Answer: Read the watermark → extract only the rows after it → merge into the target → update the watermark. The watermark bounds the extract and moves only after the merge. The watermark bounds the extract, the merge applies the delta, and the watermark advances only after the merge succeeds. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Advancing the watermark before the merge loses every row the failed merge did not write. Why the correct answer wins: The watermark bounds the extract and moves only after the merge.
- **B:** Incorrect for this question. Nothing has been extracted, so there is nothing to merge, and the watermark moves before the data does. Why the correct answer wins: The watermark bounds the extract and moves only after the merge.
- **C:** Incorrect for this question. A full extract ignores the watermark, so reading it afterwards adds nothing and the target reloads the history. Why the correct answer wins: The watermark bounds the extract and moves only after the merge.
- **D:** Correct. The watermark bounds the extract, the merge applies the delta, and the watermark advances only after the merge succeeds. In this case: The watermark bounds the extract and moves only after the merge.

### Question 61 — D

Answer: Read the item activity log. The item activity log covers that item's runs. The activity log records the runs of one item with their outcomes. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The item activity log covers that item's runs.
- **B:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The item activity log covers that item's runs.
- **C:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The item activity log covers that item's runs.
- **D:** Correct. The activity log records the runs of one item with their outcomes. In this case: The item activity log covers that item's runs.

### Question 62 — A, D

Answers: Use the Monitoring hub for the run history; Read the item activity log. The hub covers the estate, and the activity log covers one item. The hub lists every run with its status, duration, and owning item. The activity log records the runs of one item with their outcomes. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The hub lists every run with its status, duration, and owning item. In this case: The hub covers the estate, and the activity log covers one item.
- **B:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The hub covers the estate, and the activity log covers one item.
- **C:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The hub covers the estate, and the activity log covers one item.
- **D:** Correct. The activity log records the runs of one item with their outcomes. In this case: The hub covers the estate, and the activity log covers one item.
- **E:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The hub covers the estate, and the activity log covers one item.

### Question 63 — D

Answer: Read the refresh history for the semantic model. The refresh history records each attempt and its duration. The refresh history separates a failed refresh from a slow one. Local study-map skill 3.2 (Monitoring Semantic Model Refresh), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The refresh history records each attempt and its duration.
- **B:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The refresh history records each attempt and its duration.
- **C:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The refresh history records each attempt and its duration.
- **D:** Correct. The refresh history separates a failed refresh from a slow one. In this case: The refresh history records each attempt and its duration.

### Question 64 — A

Answer: Send the logs to a Log Analytics workspace. Log Analytics retains what the in-product views expire. Log Analytics keeps the history that the in-product views expire. Local study-map skill 3.2 (Monitoring Semantic Model Refresh), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. Log Analytics keeps the history that the in-product views expire. In this case: Log Analytics retains what the in-product views expire.
- **B:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: Log Analytics retains what the in-product views expire.
- **C:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: Log Analytics retains what the in-product views expire.
- **D:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: Log Analytics retains what the in-product views expire.

### Question 65 — C

Answer: Read the activity output of the failed step. The activity output carries the error and its input. The activity output carries the error and the input that produced it. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The activity output carries the error and its input.
- **B:** Incorrect for this question. The message names the object or the conversion; the plan explains the cost. Why the correct answer wins: The activity output carries the error and its input.
- **C:** Correct. The activity output carries the error and the input that produced it. In this case: The activity output carries the error and its input.
- **D:** Incorrect for this question. The refresh error names the step, which is where the transform diverged. Why the correct answer wins: The activity output carries the error and its input.

### Question 66 — D

Answer: Add a retry policy with a delay to the failing activity. A retry policy absorbs a transient failure. A retry absorbs a transient failure that the next attempt would not repeat. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The dependency is what makes the failure path execute at all. Why the correct answer wins: A retry policy absorbs a transient failure.
- **B:** Incorrect for this question. An error branch turns a silent failure into an explicit outcome. Why the correct answer wins: A retry policy absorbs a transient failure.
- **C:** Incorrect for this question. Until repeats the check and stops when the condition is met or the timeout expires. Why the correct answer wins: A retry policy absorbs a transient failure.
- **D:** Correct. A retry absorbs a transient failure that the next attempt would not repeat. In this case: A retry policy absorbs a transient failure.

### Question 67 — A, D

Answers: Read the activity output of the failed step; Add a retry policy with a delay to the failing activity. The retry absorbs the transient case, and the output explains the real one. The activity output carries the error and the input that produced it. A retry absorbs a transient failure that the next attempt would not repeat. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The activity output carries the error and the input that produced it. In this case: The retry absorbs the transient case, and the output explains the real one.
- **B:** Incorrect for this question. The dependency is what makes the failure path execute at all. Why the correct answer wins: The retry absorbs the transient case, and the output explains the real one.
- **C:** Incorrect for this question. The refresh error names the step, which is where the transform diverged. Why the correct answer wins: The retry absorbs the transient case, and the output explains the real one.
- **D:** Correct. A retry absorbs a transient failure that the next attempt would not repeat. In this case: The retry absorbs the transient case, and the output explains the real one.
- **E:** Incorrect for this question. An error branch turns a silent failure into an explicit outcome. Why the correct answer wins: The retry absorbs the transient case, and the output explains the real one.

### Question 68 — B

Answer: Check the failing cell and the Spark driver log. The driver log carries the executor errors the cell output omits. The driver log carries the executor and serialization errors the cell output omits. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The driver log carries the executor errors the cell output omits.
- **B:** Correct. The driver log carries the executor and serialization errors the cell output omits. In this case: The driver log carries the executor errors the cell output omits.
- **C:** Incorrect for this question. The cell output is where the exception is reported with its stack. Why the correct answer wins: The driver log carries the executor errors the cell output omits.
- **D:** Incorrect for this question. The Spark UI shows the stages and tasks where the time went. Why the correct answer wins: The driver log carries the executor errors the cell output omits.

### Question 69 — D

Answer: Open the Spark UI for the application. The Spark UI shows where the micro-batches spend their time. The Spark UI shows the stages and tasks where the time went. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The Spark UI shows where the micro-batches spend their time.
- **B:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The Spark UI shows where the micro-batches spend their time.
- **C:** Incorrect for this question. The cell output is where the exception is reported with its stack. Why the correct answer wins: The Spark UI shows where the micro-batches spend their time.
- **D:** Correct. The Spark UI shows the stages and tasks where the time went. In this case: The Spark UI shows where the micro-batches spend their time.

### Question 70 — B, D

Answers: Inspect the failing cell output and exit value; Open the Spark UI for the application. The cell output explains the failure, and the UI explains the time. The cell output is where the exception is reported with its stack. The Spark UI shows the stages and tasks where the time went. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The cell output explains the failure, and the UI explains the time.
- **B:** Correct. The cell output is where the exception is reported with its stack. In this case: The cell output explains the failure, and the UI explains the time.
- **C:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The cell output explains the failure, and the UI explains the time.
- **D:** Correct. The Spark UI shows the stages and tasks where the time went. In this case: The cell output explains the failure, and the UI explains the time.
- **E:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The cell output explains the failure, and the UI explains the time.

### Question 71 — C

Answer: Query the ingestion failures table in the KQL database. The ingestion failures table records the rejected records. The failures table records the rejected records and the reason for each. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The ingestion failures table records the rejected records.
- **B:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The ingestion failures table records the rejected records.
- **C:** Correct. The failures table records the rejected records and the reason for each. In this case: The ingestion failures table records the rejected records.
- **D:** Incorrect for this question. The runtime metrics show whether the source or the destination is blocking. Why the correct answer wins: The ingestion failures table records the rejected records.

### Question 72 — C

Answer: Read the T-SQL error message and then the query plan. The T-SQL message names the object or the conversion. The message names the object or the conversion; the plan explains the cost. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The T-SQL message names the object or the conversion.
- **B:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The T-SQL message names the object or the conversion.
- **C:** Correct. The message names the object or the conversion; the plan explains the cost. In this case: The T-SQL message names the object or the conversion.
- **D:** Incorrect for this question. A shortcut fails for a connection or permission reason more often than for a data reason. Why the correct answer wins: The T-SQL message names the object or the conversion.

### Question 73 — A

Answer: Check the shortcut connection and the delegated permission. The delegated permission behind the shortcut differs by identity. A shortcut fails for a connection or permission reason more often than for a data reason. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. A shortcut fails for a connection or permission reason more often than for a data reason. In this case: The delegated permission behind the shortcut differs by identity.
- **B:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The delegated permission behind the shortcut differs by identity.
- **C:** Incorrect for this question. The message names the object or the conversion; the plan explains the cost. Why the correct answer wins: The delegated permission behind the shortcut differs by identity.
- **D:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The delegated permission behind the shortcut differs by identity.

### Question 74 — D

Answer: Run OPTIMIZE to compact the small files. OPTIMIZE compacts the small files into fewer larger ones. OPTIMIZE rewrites many small files into fewer larger ones. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: OPTIMIZE compacts the small files into fewer larger ones.
- **B:** Incorrect for this question. V-Order writes the files in a layout the Fabric engines read faster. Why the correct answer wins: OPTIMIZE compacts the small files into fewer larger ones.
- **C:** Incorrect for this question. A partition on the filter column lets the engine skip the rows it does not need. Why the correct answer wins: OPTIMIZE compacts the small files into fewer larger ones.
- **D:** Correct. OPTIMIZE rewrites many small files into fewer larger ones. In this case: OPTIMIZE compacts the small files into fewer larger ones.

### Question 75 — D

Answer: Partition the table on the date column. Partitioning on the filtered column lets the engine skip files. A partition on the filter column lets the engine skip the rows it does not need. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: Partitioning on the filtered column lets the engine skip files.
- **B:** Incorrect for this question. Z-Order clusters related values so a filtered read touches fewer files. Why the correct answer wins: Partitioning on the filtered column lets the engine skip files.
- **C:** Incorrect for this question. OPTIMIZE rewrites many small files into fewer larger ones. Why the correct answer wins: Partitioning on the filtered column lets the engine skip files.
- **D:** Correct. A partition on the filter column lets the engine skip the rows it does not need. In this case: Partitioning on the filtered column lets the engine skip files.

### Question 76 — C, E

Answers: Run OPTIMIZE to compact the small files; Partition the table on the date column. Compaction reduces the files, and the partition prunes by date. OPTIMIZE rewrites many small files into fewer larger ones. A partition on the filter column lets the engine skip the rows it does not need. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. V-Order writes the files in a layout the Fabric engines read faster. Why the correct answer wins: Compaction reduces the files, and the partition prunes by date.
- **B:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: Compaction reduces the files, and the partition prunes by date.
- **C:** Correct. OPTIMIZE rewrites many small files into fewer larger ones. In this case: Compaction reduces the files, and the partition prunes by date.
- **D:** Incorrect for this question. Z-Order clusters related values so a filtered read touches fewer files. Why the correct answer wins: Compaction reduces the files, and the partition prunes by date.
- **E:** Correct. A partition on the filter column lets the engine skip the rows it does not need. In this case: Compaction reduces the files, and the partition prunes by date.

### Question 77 — B

Answer: Raise the parallelism of the copy so independent slices move together. Raising the parallelism moves the independent slices together. Independent slices that run one after another waste the capacity the run already has. Local study-map skill 3.9 (Optimizing Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Raising the parallelism moves the independent slices together.
- **B:** Correct. Independent slices that run one after another waste the capacity the run already has. In this case: Raising the parallelism moves the independent slices together.
- **C:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: Raising the parallelism moves the independent slices together.
- **D:** Incorrect for this question. Coalesce reduces the file count without a full shuffle. Why the correct answer wins: Raising the parallelism moves the independent slices together.

### Question 78 — C

Answer: Update statistics so the optimizer sees the current distribution. Statistics are what the optimizer plans from. The warehouse optimizer plans from statistics, not from the data itself. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Many small files cost more to scan than the same rows in fewer files. Why the correct answer wins: Statistics are what the optimizer plans from.
- **B:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Statistics are what the optimizer plans from.
- **C:** Correct. The warehouse optimizer plans from statistics, not from the data itself. In this case: Statistics are what the optimizer plans from.
- **D:** Incorrect for this question. A join on a different column forces a shuffle of both sides. Why the correct answer wins: Statistics are what the optimizer plans from.

### Question 79 — B

Answer: Salt the skewed key so the partitions even out. Salting spreads the hot key across partitions. Salting spreads one hot key across several partitions. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Broadcasting removes the shuffle of the large side of the join. Why the correct answer wins: Salting spreads the hot key across partitions.
- **B:** Correct. Salting spreads one hot key across several partitions. In this case: Salting spreads the hot key across partitions.
- **C:** Incorrect for this question. Skew handling splits the oversized partition instead of leaving one task to finish alone. Why the correct answer wins: Salting spreads the hot key across partitions.
- **D:** Incorrect for this question. Adaptive execution re-plans from the actual partition sizes at run time. Why the correct answer wins: Salting spreads the hot key across partitions.

### Question 80 — D

Answer: Set the shuffle partition count to match the data volume. The shuffle partition count must match the data volume. Too few partitions leave large tasks; too many add scheduling overhead. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: The shuffle partition count must match the data volume.
- **B:** Incorrect for this question. Broadcasting removes the shuffle of the large side of the join. Why the correct answer wins: The shuffle partition count must match the data volume.
- **C:** Incorrect for this question. Coalesce reduces the file count without a full shuffle. Why the correct answer wins: The shuffle partition count must match the data volume.
- **D:** Correct. Too few partitions leave large tasks; too many add scheduling overhead. In this case: The shuffle partition count must match the data volume.

### Question 81 — B, E

Answers: Keep adaptive query execution enabled so the shuffle is re-planned; Enable skew join handling for the hot key. Adaptive execution re-plans at run time, and skew handling splits the hot partition. Adaptive execution re-plans from the actual partition sizes at run time. Skew handling splits the oversized partition instead of leaving one task to finish alone. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Broadcasting removes the shuffle of the large side of the join. Why the correct answer wins: Adaptive execution re-plans at run time, and skew handling splits the hot partition.
- **B:** Correct. Skew handling splits the oversized partition instead of leaving one task to finish alone. In this case: Adaptive execution re-plans at run time, and skew handling splits the hot partition.
- **C:** Incorrect for this question. Too few partitions leave large tasks; too many add scheduling overhead. Why the correct answer wins: Adaptive execution re-plans at run time, and skew handling splits the hot partition.
- **D:** Incorrect for this question. Salting spreads one hot key across several partitions. Why the correct answer wins: Adaptive execution re-plans at run time, and skew handling splits the hot partition.
- **E:** Correct. Adaptive execution re-plans from the actual partition sizes at run time. In this case: Adaptive execution re-plans at run time, and skew handling splits the hot partition.

### Question 82 — D

Answer: Set the retention policy to match the query window. Retention should match the query window. Retention beyond the query window pays for data nobody reads. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The caching policy keeps the hot window on fast storage. Why the correct answer wins: Retention should match the query window.
- **B:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: Retention should match the query window.
- **C:** Incorrect for this question. Query throughput is bounded by the eventhouse capacity. Why the correct answer wins: Retention should match the query window.
- **D:** Correct. Retention beyond the query window pays for data nobody reads. In this case: Retention should match the query window.

### Question 83 — C

Answer: Set the caching policy on the KQL table. The caching policy keeps the hot window on fast storage. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: The caching policy keeps the hot window on fast storage.
- **B:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: The caching policy keeps the hot window on fast storage.
- **C:** Correct. In this case: The caching policy keeps the hot window on fast storage.
- **D:** Incorrect for this question. Query throughput is bounded by the eventhouse capacity. Why the correct answer wins: The caching policy keeps the hot window on fast storage.

### Question 84 — D

Answer: Scale the destination throughput for the event volume. The destination throughput caps what the eventstream can deliver. The destination throughput caps how much the eventstream can deliver. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: The destination throughput caps what the eventstream can deliver.
- **B:** Incorrect for this question. Query throughput is bounded by the eventhouse capacity. Why the correct answer wins: The destination throughput caps what the eventstream can deliver.
- **C:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: The destination throughput caps what the eventstream can deliver.
- **D:** Correct. The destination throughput caps how much the eventstream can deliver. In this case: The destination throughput caps what the eventstream can deliver.

### Question 85 — C

Answer: Enable the monitoring output → build the dashboard over it → set the alert threshold → review the alert history each week. The monitoring output comes before the dashboard and the alert. There is nothing to chart or alert on until the output exists, and the review is what keeps the threshold honest. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. There is no alert history before the alert exists. Why the correct answer wins: The monitoring output comes before the dashboard and the alert.
- **B:** Incorrect for this question. The dashboard and the threshold both read an output that does not exist yet. Why the correct answer wins: The monitoring output comes before the dashboard and the alert.
- **C:** Correct. There is nothing to chart or alert on until the output exists, and the review is what keeps the threshold honest. In this case: The monitoring output comes before the dashboard and the alert.
- **D:** Incorrect for this question. A threshold with no output behind it cannot be evaluated. Why the correct answer wins: The monitoring output comes before the dashboard and the alert.

### Question 86 — C

Answer: Read the run history → isolate the failing activity → reproduce it with the same input → rerun only the failed activity. The history locates the failure before anything is rerun. The history identifies the failure, the input reproduces it, and the rerun is scoped to what failed. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The rerun happens before the cause is reproduced, so the second failure looks like a new one. Why the correct answer wins: The history locates the failure before anything is rerun.
- **B:** Incorrect for this question. Rerunning before reading the history repeats the failure without explaining it. Why the correct answer wins: The history locates the failure before anything is rerun.
- **C:** Correct. The history identifies the failure, the input reproduces it, and the rerun is scoped to what failed. In this case: The history locates the failure before anything is rerun.
- **D:** Incorrect for this question. The failing activity has to be known before its input can be reproduced. Why the correct answer wins: The history locates the failure before anything is rerun.

### Question 87 — B

Answer: Read the query plan → reduce the file count → optimize and Z-Order the table → re-measure the query. The plan decides the action and the second measurement proves it. The plan identifies the cost, compaction and clustering address it, and the measurement proves the effect. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Optimizing before reading the plan optimizes whatever seemed slow rather than what was costly. Why the correct answer wins: The plan decides the action and the second measurement proves it.
- **B:** Correct. The plan identifies the cost, compaction and clustering address it, and the measurement proves the effect. In this case: The plan decides the action and the second measurement proves it.
- **C:** Incorrect for this question. The plan is what should have decided whether compaction was the right fix at all. Why the correct answer wins: The plan decides the action and the second measurement proves it.
- **D:** Incorrect for this question. Measuring before the change and again after it is what makes the comparison possible. Why the correct answer wins: The plan decides the action and the second measurement proves it.

### Question 88 — D

Answer: Set the retention policy to match the query window. Retention beyond the query window pays for data nobody reads. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: Retention beyond the query window pays for data nobody reads.
- **B:** Incorrect for this question. Query throughput is bounded by the eventhouse capacity. Why the correct answer wins: Retention beyond the query window pays for data nobody reads.
- **C:** Incorrect for this question. The caching policy keeps the hot window on fast storage. Why the correct answer wins: Retention beyond the query window pays for data nobody reads.
- **D:** Correct. In this case: Retention beyond the query window pays for data nobody reads.

### Question 89 — A

Answer: Apply column-level security so the column is hidden from the group. Row-level security filters the rows per identity. Column-level security hides the column while leaving the rest of the table readable. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Column-level security hides the column while leaving the rest of the table readable. In this case: Row-level security filters the rows per identity.
- **B:** Incorrect for this question. Row-level security filters rows per identity, so one table returns different rows to different users. Why the correct answer wins: Row-level security filters the rows per identity.
- **C:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: Row-level security filters the rows per identity.
- **D:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: Row-level security filters the rows per identity.

### Question 90 — A

Answer: Apply the sensitivity label to the item. The sensitivity label travels with the item and its copies. The label travels with the item and drives the protection downstream consumers inherit. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The label travels with the item and drives the protection downstream consumers inherit. In this case: The sensitivity label travels with the item and its copies.
- **B:** Incorrect for this question. Certification tells consumers the item has been reviewed as authoritative. Why the correct answer wins: The sensitivity label travels with the item and its copies.
- **C:** Incorrect for this question. Promotion signals readiness without the review that certification implies. Why the correct answer wins: The sensitivity label travels with the item and its copies.
- **D:** Incorrect for this question. Inheritance keeps one classification instead of a second opinion on the same data. Why the correct answer wins: The sensitivity label travels with the item and its copies.

### Question 91 — C

Answer: Read the Fabric audit log in the Microsoft Purview portal. The audit log records the identity, the item, and the time. The audit log records who did what to which item and when. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Filtering turns a very large log into the events that answer the question. Why the correct answer wins: The audit log records the identity, the item, and the time.
- **B:** Incorrect for this question. The audit log has a retention window, so an investigation that starts late needs the export. Why the correct answer wins: The audit log records the identity, the item, and the time.
- **C:** Correct. The audit log records who did what to which item and when. In this case: The audit log records the identity, the item, and the time.
- **D:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The audit log records the identity, the item, and the time.

### Question 92 — B

Answer: Send the logs to a Log Analytics workspace. Log Analytics retains what the in-product views expire. Log Analytics keeps the history that the in-product views expire. Local study-map skill 3.2 (Monitoring Semantic Model Refresh), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: Log Analytics retains what the in-product views expire.
- **B:** Correct. Log Analytics keeps the history that the in-product views expire. In this case: Log Analytics retains what the in-product views expire.
- **C:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: Log Analytics retains what the in-product views expire.
- **D:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: Log Analytics retains what the in-product views expire.

### Question 93 — D

Answer: Inspect the eventstream runtime metrics. The runtime metrics show whether the source or the destination is limiting. The runtime metrics show whether the source or the destination is blocking. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The runtime metrics show whether the source or the destination is limiting.
- **B:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The runtime metrics show whether the source or the destination is limiting.
- **C:** Incorrect for this question. The failures table records the rejected records and the reason for each. Why the correct answer wins: The runtime metrics show whether the source or the destination is limiting.
- **D:** Correct. The runtime metrics show whether the source or the destination is blocking. In this case: The runtime metrics show whether the source or the destination is limiting.

### Question 94 — B

Answer: Configure an alert on the failing condition. An alert turns the silent gap into a notification the hub team can act on. An alert turns a silent failure into a notification. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Waiting for the retries stops a transient failure being reported as an outage. Why the correct answer wins: An alert turns the silent gap into a notification the hub team can act on.
- **B:** Correct. An alert turns a silent failure into a notification. In this case: An alert turns the silent gap into a notification the hub team can act on.
- **C:** Incorrect for this question. An activator rule evaluates the stream and fires when the condition holds. Why the correct answer wins: An alert turns the silent gap into a notification the hub team can act on.
- **D:** Incorrect for this question. The alert must reach the owner, or it becomes noise nobody acts on. Why the correct answer wins: An alert turns the silent gap into a notification the hub team can act on.

### Question 95 — B

Answer: Use a Copy activity in the pipeline. A Copy activity moves the rows as one orchestrated step. The Copy activity moves the files or rows as one orchestrated step. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.
- **B:** Correct. The Copy activity moves the files or rows as one orchestrated step. In this case: A Copy activity moves the rows as one orchestrated step.
- **C:** Incorrect for this question. Appending preserves the earlier loads that the incremental pattern depends on. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.
- **D:** Incorrect for this question. Get Metadata turns an unknown folder into a list the loop can iterate. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.

### Question 96 — B

Answer: Deduplicate on the business key and keep the latest record. Deduplication leaves one row per business key. Deduplication makes the target one row per business key. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Deduplication leaves one row per business key.
- **B:** Correct. Deduplication makes the target one row per business key. In this case: Deduplication leaves one row per business key.
- **C:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Deduplication leaves one row per business key.
- **D:** Incorrect for this question. Reprocessing the partition corrects the aggregate that was already published. Why the correct answer wins: Deduplication leaves one row per business key.

### Question 97 — A

Answer: Process the stream with an eventstream. An eventstream carries the events without a scheduled batch. An eventstream is the no-code path from a source to a destination. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. An eventstream is the no-code path from a source to a destination. In this case: An eventstream carries the events without a scheduled batch.
- **B:** Incorrect for this question. A batch job over the landing folder adds latency the streaming requirement may not allow. Why the correct answer wins: An eventstream carries the events without a scheduled batch.
- **C:** Incorrect for this question. An update policy transforms the data as it lands in the KQL table. Why the correct answer wins: An eventstream carries the events without a scheduled batch.
- **D:** Incorrect for this question. Structured streaming suits stateful processing and the same PySpark logic used in batch. Why the correct answer wins: An eventstream carries the events without a scheduled batch.

### Question 98 — B

Answer: Use the Monitoring hub for the run history. The Monitoring hub lists every run with its status and duration. The hub lists every run with its status, duration, and owning item. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **B:** Correct. The hub lists every run with its status, duration, and owning item. In this case: The Monitoring hub lists every run with its status and duration.
- **C:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **D:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.

### Question 99 — D

Answer: Configure an alert on the failing condition. An alert fires on the condition the business cares about. An alert turns a silent failure into a notification. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Waiting for the retries stops a transient failure being reported as an outage. Why the correct answer wins: An alert fires on the condition the business cares about.
- **B:** Incorrect for this question. An activator rule evaluates the stream and fires when the condition holds. Why the correct answer wins: An alert fires on the condition the business cares about.
- **C:** Incorrect for this question. The alert must reach the owner, or it becomes noise nobody acts on. Why the correct answer wins: An alert fires on the condition the business cares about.
- **D:** Correct. An alert turns a silent failure into a notification. In this case: An alert fires on the condition the business cares about.

### Question 100 — A

Answer: Salt the skewed key so the partitions even out. Salting spreads the hot key across partitions. Salting spreads one hot key across several partitions. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. Salting spreads one hot key across several partitions. In this case: Salting spreads the hot key across partitions.
- **B:** Incorrect for this question. Skew handling splits the oversized partition instead of leaving one task to finish alone. Why the correct answer wins: Salting spreads the hot key across partitions.
- **C:** Incorrect for this question. Broadcasting removes the shuffle of the large side of the join. Why the correct answer wins: Salting spreads the hot key across partitions.
- **D:** Incorrect for this question. Adaptive execution re-plans from the actual partition sizes at run time. Why the correct answer wins: Salting spreads the hot key across partitions.
