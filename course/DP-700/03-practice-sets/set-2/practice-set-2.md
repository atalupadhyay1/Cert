# Microsoft DP-700 — Full-Length Mock Exam 2

Fabric Data Engineer Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, interactive components in the Fabric portal, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. The warehouse must read the same Delta files the lakehouse wrote. What must stay enabled?

Domain: Implement and manage an analytics solution

- A. Assign the workspace to a capacity that has headroom
- B. Keep OneLake availability enabled so other engines can read the same data
- C. Create the workspace in the required region at creation time
- D. Assign the workspace to the domain that owns the subject area

### 2. Governance wants the four finance workspaces discovered and managed together. What should be configured?

Domain: Implement and manage an analytics solution

- A. Keep OneLake availability enabled so other engines can read the same data
- B. Create the workspace in the required region at creation time
- C. Assign the workspace to the domain that owns the subject area
- D. Assign the workspace to a capacity that has headroom

### 3. A team wants to keep its existing Python DAG and run it inside Fabric. What should be used?

Domain: Implement and manage an analytics solution

- A. Use a pipeline for the copy and the orchestration
- B. Rewrite the existing orchestration as a Fabric pipeline instead
- C. Sync the Airflow DAG from the connected Git repository
- D. Enable the Apache Airflow job in the workspace and author the DAG

### 4. An existing DAG must run in Fabric and every change must be reviewed. Which two practices apply? Select two.

Domain: Implement and manage an analytics solution

- A. Rewrite the existing orchestration as a Fabric pipeline instead
- B. Enable the Apache Airflow job in the workspace and author the DAG
- C. Sync the Airflow DAG from the connected Git repository
- D. Use a pipeline for the copy and the orchestration
- E. Use a notebook for the transformation

### 5. A promoted pipeline keeps pointing at the test data source. What is missing?

Domain: Implement and manage an analytics solution

- A. Create a deployment pipeline with development, test, and production stages
- B. Select only the items that belong in the target stage
- C. Compare the stages before promoting
- D. Add deployment rules so the target stage keeps its own connection and parameters

### 6. A team wants to know exactly what a promotion will change before it runs. What should be used?

Domain: Implement and manage an analytics solution

- A. Compare the stages before promoting
- B. Create a deployment pipeline with development, test, and production stages
- C. Deploy backwards to recover the last known-good definition
- D. Add deployment rules so the target stage keeps its own connection and parameters

### 7. Twenty analysts need read access to every item in a new workspace. What should be granted?

Domain: Implement and manage an analytics solution

- A. Grant Read on the item
- B. Share the single item with the user who needs only that item
- C. Grant the user a workspace role
- D. Share a link to the item with the required permission

### 8. A partner must query one warehouse table and see nothing else. What should be granted?

Domain: Implement and manage an analytics solution

- A. Grant the user a workspace role
- B. Share the single item with the user who needs only that item
- C. Grant Read on the item
- D. Grant Admin on the workspace to the platform team

### 9. A large team must read the workspace and one external reviewer needs a single report. Which two grants apply? Select two.

Domain: Implement and manage an analytics solution

- A. Grant Read on the item
- B. Share the single item with the user who needs only that item
- C. Grant Admin on the workspace to the platform team
- D. Grant Viewer on the workspace
- E. Grant the user a workspace role

### 10. The margin table must disappear from the model for the sales role. What should be applied?

Domain: Implement and manage an analytics solution

- A. Grant access at the folder that holds the restricted files
- B. Define a row-level security policy on the table
- C. Apply column-level security so the column is hidden from the group
- D. Apply object-level security in the semantic model

### 11. One contract file inside a shared folder must be restricted on its own. What should be granted?

Domain: Implement and manage an analytics solution

- A. Grant access at the individual file
- B. Grant access at the folder that holds the restricted files
- C. Apply column-level security so the column is hidden from the group
- D. Define a row-level security policy on the table

### 12. A column must not appear in the analyst output at all, even masked. What should be done?

Domain: Implement and manage an analytics solution

- A. Apply dynamic data masking to the column
- B. Exempt the authorised group from the mask
- C. Expose a view with the column omitted instead of masking it
- D. Apply column-level security so the column is hidden from the group

### 13. A national identifier must stay queryable but unreadable for analysts. Which two settings apply? Select two.

Domain: Implement and manage an analytics solution

- A. Mask the column in the report layer only
- B. Exempt the authorised group from the mask
- C. Apply column-level security so the column is hidden from the group
- D. Apply dynamic data masking to the column
- E. Expose a view with the column omitted instead of masking it

### 14. New items are created with no classification because nobody labels them. What should be configured?

Domain: Implement and manage an analytics solution

- A. Certify the item as the approved source
- B. Set the default sensitivity label for the workspace
- C. Apply the sensitivity label to the item
- D. Let the label inherit from the labelled source file

### 15. A table is ready for reuse but has not been through a formal review. What should be applied?

Domain: Implement and manage an analytics solution

- A. Set the default sensitivity label for the workspace
- B. Certify the item as the approved source
- C. Apply the sensitivity label to the item
- D. Promote the item as ready for reuse

### 16. An investigation starts four months after the events and the log window is shorter. What should be done?

Domain: Implement and manage an analytics solution

- A. Filter the audit log by activity and by item
- B. Read the item activity log
- C. Read the Fabric audit log in the Microsoft Purview portal
- D. Export the audit events before the retention window closes

### 17. An auditor needs one user's actions on one warehouse over a week. Which two steps apply? Select two.

Domain: Implement and manage an analytics solution

- A. Export the audit events before the retention window closes
- B. Read the refresh history for the semantic model
- C. Read the Fabric audit log in the Microsoft Purview portal
- D. Filter the audit log by activity and by item
- E. Read the item activity log

### 18. Data access must be restricted even for users who are workspace Contributors. What should be configured?

Domain: Implement and manage an analytics solution

- A. Grant the user a workspace role
- B. Scope the OneLake role to the folder that holds the restricted table
- C. Grant access at the folder that holds the restricted files
- D. Configure OneLake security roles for the lakehouse

### 19. Thirty staff must all receive the same OneLake role. What should be done?

Domain: Implement and manage an analytics solution

- A. Grant Admin on the workspace to the platform team
- B. Configure OneLake security roles for the lakehouse
- C. Scope the OneLake role to the folder that holds the restricted table
- D. Grant the OneLake role to a security group rather than to individuals

### 20. The data is already in the warehouse and the transform is a multi-table update. What should be used?

Domain: Implement and manage an analytics solution

- A. Use a Dataflow Gen2 for the transformation
- B. Use a notebook for the transformation
- C. Use a T-SQL script against the warehouse
- D. Use a pipeline for the copy and the orchestration

### 21. The data is already in an eventhouse and the transform is a time-window filter. What should be used?

Domain: Implement and manage an analytics solution

- A. Use a notebook for the transformation
- B. Use a Dataflow Gen2 for the transformation
- C. Use a T-SQL script against the warehouse
- D. Use a KQL query against the eventhouse

### 22. One run must copy files and then run PySpark over them. Which two items apply? Select two.

Domain: Implement and manage an analytics solution

- A. Use a T-SQL script against the warehouse
- B. Use a pipeline for the copy and the orchestration
- C. Use a notebook for the transformation
- D. Use a Dataflow Gen2 for the transformation
- E. Use a KQL query against the eventhouse

### 23. A report must be rebuilt every weekday at 06:00 in local time. What should be configured?

Domain: Implement and manage an analytics solution

- A. Pass the folder path as a pipeline parameter
- B. Add an event-based trigger so the run starts when the file arrives
- C. Add a schedule trigger with the cadence and time zone the business expects
- D. Trigger on the file-created event for the landing folder

### 24. The same pipeline must run for six different landing folders. What should be added?

Domain: Implement and manage an analytics solution

- A. Pass the folder path as a pipeline parameter
- B. Set the value in a pipeline variable and reference the variable
- C. Look up the stored watermark before the copy
- D. Build the path with a dynamic expression at run time

### 25. A run must recur at a fixed hour and address a folder named for the period. Which two features apply? Select two.

Domain: Implement and manage an analytics solution

- A. Add a schedule trigger with the cadence and time zone the business expects
- B. Look up the stored watermark before the copy
- C. Add an event-based trigger so the run starts when the file arrives
- D. Build the path with a dynamic expression at run time
- E. Set the value in a pipeline variable and reference the variable

### 26. An item must be published as the approved source with evidence. Which sequence is correct?

Domain: Implement and manage an analytics solution

- A. Confirm the source of truth → apply the label → endorse the item → verify the audit entry
- B. Endorse the item → apply the label → confirm the source of truth → verify the audit entry
- C. Verify the audit entry → endorse the item → confirm the source of truth → apply the label
- D. Apply the label → verify the audit entry → endorse the item → confirm the source of truth

### 27. A reviewed change must reach production through a pipeline. Which sequence is correct?

Domain: Implement and manage an analytics solution

- A. Promote through the stages → create the deployment pipeline → commit the definitions → connect Git → add deployment rules
- B. Commit the item definitions → connect the workspace to Git → add deployment rules → create the pipeline → promote the stages
- C. Create the deployment pipeline → connect the workspace to Git → promote through the stages → add deployment rules → commit the definitions
- D. Connect the workspace to Git → commit the item definitions → create the deployment pipeline → add deployment rules → promote through the stages

### 28. A required measure is missing for a small number of rows and the total must stay correct. What should be done?

Domain: Ingest and transform data

- A. Deduplicate on the business key and keep the latest record
- B. Replace the missing value with a documented default
- C. Route the failed rows to a reject table and continue the load
- D. Reprocess the affected partitions when the data arrives late

### 29. A streaming write restarts and duplicates the last hour. What should be configured?

Domain: Ingest and transform data

- A. Run a batch job every few minutes over the landing folder
- B. Set a watermark so late events are handled deterministically
- C. Set a checkpoint location for the streaming query
- D. Store the stream in native tables in the eventhouse

### 30. The dashboards run range queries over a timestamp column. What should hold the data?

Domain: Ingest and transform data

- A. Land the extract in the lakehouse Files area
- B. Create a KQL database for the time-series queries
- C. Query the lakehouse through its SQL analytics endpoint
- D. Load the curated model into the warehouse

### 31. Analysts want T-SQL over the Delta tables without loading a warehouse. What should they use?

Domain: Ingest and transform data

- A. Query the lakehouse through its SQL analytics endpoint
- B. Store the telemetry in an eventhouse KQL database
- C. Write the curated table into the lakehouse Tables area
- D. Load the curated model into the warehouse

### 32. The transform needs per-partition ranking over forty million rows. What should be used?

Domain: Ingest and transform data

- A. Transform with Dataflow Gen2 and Power Query
- B. Transform with KQL in the eventhouse
- C. Transform with T-SQL against the warehouse
- D. Transform with PySpark in a notebook

### 33. A landing table must be filtered and enriched as records arrive. What should be used?

Domain: Ingest and transform data

- A. Transform with T-SQL against the warehouse
- B. Transform with KQL in the eventhouse
- C. Transform with PySpark in a notebook
- D. Transform with Dataflow Gen2 and Power Query

### 34. A governed table is authoritative elsewhere and must not be copied. What should be created?

Domain: Ingest and transform data

- A. Create an ADLS Gen2 shortcut to the external container
- B. Create a shortcut rather than a copy when the source stays authoritative
- C. Copy the remote data into a local table instead of shortcutting it
- D. Use a Copy activity in the pipeline

### 35. A report filters a shortcut-backed table on four columns and every query scans the remote source. What should be enabled?

Domain: Ingest and transform data

- A. Enable query acceleration on the shortcut
- B. Create an ADLS Gen2 shortcut to the external container
- C. Copy the remote data into a local table instead of shortcutting it
- D. Create an internal OneLake shortcut to the other lakehouse table

### 36. A mirrored database shows changes within seconds and no pipeline runs. Why?

Domain: Ingest and transform data

- A. Create an internal OneLake shortcut to the other lakehouse table
- B. Run a full load and overwrite the target
- C. Rely on change data capture so the mirror needs no pipeline schedule
- D. Use a Copy activity in the pipeline

### 37. A source database must be mirrored without competing with its own workload. Which two practices apply? Select two.

Domain: Ingest and transform data

- A. Enable mirroring for the operational database
- B. Rely on change data capture so the mirror needs no pipeline schedule
- C. Mirror from a read replica so the source database keeps its capacity
- D. Create an ADLS Gen2 shortcut to the external container
- E. Append the new files instead of overwriting the target

### 38. The source file must be preserved exactly as delivered and parsed later. What should be done?

Domain: Ingest and transform data

- A. Append the new files instead of overwriting the target
- B. Use a Copy activity in the pipeline
- C. Copy the files as binary and parse them downstream
- D. Use Get Metadata to list the files to process

### 39. The same nightly file is processed twice when a run is retried. What should be added?

Domain: Ingest and transform data

- A. Copy the files as binary and parse them downstream
- B. Append the new files instead of overwriting the target
- C. Delete the processed source file after the load succeeds
- D. Use Get Metadata to list the files to process

### 40. A folder arrives with an unknown file count and history must accumulate. Which two actions apply? Select two.

Domain: Ingest and transform data

- A. Use Get Metadata to list the files to process
- B. Append the new files instead of overwriting the target
- C. Use a Copy activity in the pipeline
- D. Copy the files as binary and parse them downstream
- E. Delete the processed source file after the load succeeds

### 41. Each order line must carry the running total for its order. What should be used?

Domain: Ingest and transform data

- A. Group and aggregate to the grain the report needs
- B. Union the sources after conforming the columns
- C. Pivot the rows into the reporting columns
- D. Use a window function to rank within the partition

### 42. A slowly changing dimension must be updated with a merge on the business key. What should be used?

Domain: Ingest and transform data

- A. Transform with KQL in the eventhouse
- B. Transform with T-SQL against the warehouse
- C. Transform with Dataflow Gen2 and Power Query
- D. Transform with PySpark in a notebook

### 43. One step merges a warehouse dimension and another filters eventhouse rows. Which two engines apply? Select two.

Domain: Ingest and transform data

- A. Transform with PySpark in a notebook
- B. Transform with KQL in the eventhouse
- C. Pivot the rows into the reporting columns
- D. Transform with T-SQL against the warehouse
- E. Transform with Dataflow Gen2 and Power Query

### 44. Two sources must be combined although one renamed a column. What must happen first?

Domain: Ingest and transform data

- A. Pivot the rows into the reporting columns
- B. Denormalize the model so the report needs no join
- C. Union the sources after conforming the columns
- D. Group and aggregate to the grain the report needs

### 45. A report needs one column per month with one row per store. What should be used?

Domain: Ingest and transform data

- A. Union the sources after conforming the columns
- B. Use a window function to rank within the partition
- C. Pivot the rows into the reporting columns
- D. Group and aggregate to the grain the report needs

### 46. A customer record appears four times with different values and none is marked current. What rule should be applied?

Domain: Ingest and transform data

- A. Deduplicate on the business key and keep the latest record
- B. Deduplicate on the business key and keep the latest version
- C. Route the failed rows to a reject table and continue the load
- D. Replace the missing value with a documented default

### 47. A late event closes a window that was already published. What should be done?

Domain: Ingest and transform data

- A. Replace the null with zero before the aggregate
- B. Reprocess the closed window when a late event arrives
- C. Drop the late event because its window has closed
- D. Reprocess the affected partitions when the data arrives late

### 48. The stream needs stateful processing and the same PySpark logic used in batch. What should be used?

Domain: Ingest and transform data

- A. Process the stream with a KQL update policy
- B. Process the stream with Spark structured streaming
- C. Process the stream with an eventstream
- D. Run a batch job every few minutes over the landing folder

### 49. One stream needs a no-code path and another needs a landing-time transform. Which two features apply? Select two.

Domain: Ingest and transform data

- A. Set a checkpoint location for the streaming query
- B. Process the stream with an eventstream
- C. Process the stream with a KQL update policy
- D. Run a batch job every few minutes over the landing folder
- E. Process the stream with Spark structured streaming

### 50. A structured streaming job must resume after a cluster restart. What must be configured?

Domain: Ingest and transform data

- A. Set a watermark so late events are handled deterministically
- B. Set a checkpoint location for the streaming query
- C. Process the stream with an eventstream
- D. Store the stream in native tables in the eventhouse

### 51. Structured streaming must survive a restart and handle late events. Which two settings apply? Select two.

Domain: Ingest and transform data

- A. Query the stream through a OneLake shortcut
- B. Set a watermark so late events are handled deterministically
- C. Store the stream in native tables in the eventhouse
- D. Process the stream with an eventstream
- E. Set a checkpoint location for the streaming query

### 52. A star schema must be built from three source systems. Which sequence is correct?

Domain: Ingest and transform data

- A. Profile the source keys → define the grain of the fact → build the conformed dimensions → add the surrogate keys → load the fact
- B. Load the fact → build the conformed dimensions → profile the source keys → define the grain → add the surrogate keys
- C. Add the surrogate keys → load the fact → define the grain → profile the keys → build the dimensions
- D. Define the grain → add the surrogate keys → load the fact → profile the keys → build the dimensions

### 53. A raw extract must become a governed gold table. Which sequence is correct?

Domain: Ingest and transform data

- A. Land the raw files unchanged → validate the schema and reject the bad rows → conform and deduplicate into silver → publish the gold table
- B. Publish the gold table → validate the schema → land the raw files → conform and deduplicate
- C. Conform and deduplicate → land the raw files → publish the gold table → validate the schema
- D. Validate the schema → publish the gold table → land the raw files → conform and deduplicate

### 54. A published total is wrong because of duplicates and a late file. Which sequence is correct?

Domain: Ingest and transform data

- A. Decide the surviving record → recompute the aggregate → detect the duplicates → correct the partition
- B. Recompute the aggregate → detect the duplicates → correct the partition → decide the surviving record
- C. Correct the partition → recompute the aggregate → decide the surviving record → detect the duplicates
- D. Detect the duplicates and the late rows → decide the surviving record → correct the affected partition → recompute the aggregate

### 55. A telemetry feed arrives at ninety thousand events per second and is queried as it lands. Where should it be stored?

Domain: Ingest and transform data

- A. Load the curated model into the warehouse
- B. Create a KQL database for the time-series queries
- C. Store the telemetry in an eventhouse KQL database
- D. Query the lakehouse through its SQL analytics endpoint

### 56. Viewer counts must be produced for each non-overlapping five-minute bucket. Which window fits?

Domain: Ingest and transform data

- A. Use a tumbling window for the fixed five-minute aggregate
- B. Use a sliding window that emits when the condition is met
- C. Create a materialized view for the repeated aggregation
- D. Use a hopping window when the intervals must overlap

### 57. A source must reach a KQL table without a notebook or a scheduled job. What should be used?

Domain: Ingest and transform data

- A. Process the stream with Spark structured streaming
- B. Process the stream with a KQL update policy
- C. Run a batch job every few minutes over the landing folder
- D. Process the stream with an eventstream

### 58. A test suite of twenty runs must be reviewed after a release. Where are they listed together?

Domain: Monitor and optimize an analytics solution

- A. Send the logs to a Log Analytics workspace
- B. Use the Monitoring hub for the run history
- C. Read the refresh history for the semantic model
- D. Read the item activity log

### 59. One notebook's runs must be reviewed over the last week. What should be read?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Read the item activity log
- C. Read the refresh history for the semantic model
- D. Read the Fabric audit log in the Microsoft Purview portal

### 60. A semantic model refresh fails at the same minute every night. Where is the pattern visible?

Domain: Monitor and optimize an analytics solution

- A. Read the refresh history for the semantic model
- B. Send the logs to a Log Analytics workspace
- C. Use the Monitoring hub for the run history
- D. Read the item activity log

### 61. A refresh problem must be triaged now and analysed after 90 days. Which two sources apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Read the item activity log
- B. Read the refresh history for the semantic model
- C. Send the logs to a Log Analytics workspace
- D. Read the Fabric audit log in the Microsoft Purview portal
- E. Use the Monitoring hub for the run history

### 62. An alert fires into a shared mailbox nobody owns. What should be changed?

Domain: Monitor and optimize an analytics solution

- A. Send the alert to the team that owns the item
- B. Build a real-time dashboard over the monitoring table
- C. Use a Data Activator rule that watches the streaming condition
- D. Configure an alert on the failing condition

### 63. A channel receives two hundred alerts a week and the team ignores them. What is the defect?

Domain: Monitor and optimize an analytics solution

- A. Configure an alert on the failing condition
- B. Set the alert to fire only after the retry policy has been exhausted
- C. Send the alert to the team that owns the item
- D. Alert on every successful run as well as every failure

### 64. A failure leaves the run green and the bad data reaches the target. What should be added?

Domain: Monitor and optimize an analytics solution

- A. Add a retry policy with a delay to the failing activity
- B. Add an error branch so the failure is handled rather than ignored
- C. Use an Until loop with a timeout for the long-running check
- D. Set the failure dependency so the handler runs when the step fails

### 65. The handler exists but the pipeline still reports success. What should be set?

Domain: Monitor and optimize an analytics solution

- A. Use an Until loop with a timeout for the long-running check
- B. Add an error branch so the failure is handled rather than ignored
- C. Add a retry policy with a delay to the failing activity
- D. Set the failure dependency so the handler runs when the step fails

### 66. A notebook exits with a null reference and no class name. Where should the stack be read?

Domain: Monitor and optimize an analytics solution

- A. Inspect the failing cell output and exit value
- B. Check the failing cell and the Spark driver log
- C. Open the Spark UI for the application
- D. Use the Monitoring hub for the run history

### 67. A notebook succeeds but takes four times longer than last week. What should be opened?

Domain: Monitor and optimize an analytics solution

- A. Check the failing cell and the Spark driver log
- B. Inspect the failing cell output and exit value
- C. Open the Spark UI for the application
- D. Send the logs to a Log Analytics workspace

### 68. A KQL table receives fewer rows than the source sends and some are rejected. Where are the rejects?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Query the ingestion failures table in the KQL database
- C. Inspect the eventstream runtime metrics
- D. Read the Fabric audit log in the Microsoft Purview portal

### 69. An eventstream's throughput drops during peak. What shows the constrained side?

Domain: Monitor and optimize an analytics solution

- A. Query the ingestion failures table in the KQL database
- B. Read the refresh history for the semantic model
- C. Use the Monitoring hub for the run history
- D. Inspect the eventstream runtime metrics

### 70. A shortcut works for one team and returns nothing for another. What differs?

Domain: Monitor and optimize an analytics solution

- A. Check the shortcut connection and the delegated permission
- B. Read the activity output of the failed step
- C. Read the T-SQL error message and then the query plan
- D. Check the failing cell and the Spark driver log

### 71. A warehouse procedure fails and a shortcut-backed view is empty. Which two checks apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Read the activity output of the failed step
- B. Query the ingestion failures table in the KQL database
- C. Check the shortcut connection and the delegated permission
- D. Read the T-SQL error message and then the query plan
- E. Check the failing cell and the Spark driver log

### 72. A table's deleted versions still occupy storage a month after the delete. What should be run?

Domain: Monitor and optimize an analytics solution

- A. Enable V-Order on the table
- B. Run OPTIMIZE to compact the small files
- C. Run VACUUM to remove the files the table no longer references
- D. Partition the table on the date column

### 73. A table is filtered on two columns that are not the partition key. What should be applied?

Domain: Monitor and optimize an analytics solution

- A. Partition the table on the date column
- B. Apply Z-Order on the frequently filtered columns
- C. Enable V-Order on the table
- D. Run OPTIMIZE to compact the small files

### 74. The filter pattern changes every quarter and repartitioning is disruptive. What should be used?

Domain: Monitor and optimize an analytics solution

- A. Use liquid clustering instead of a fixed partition column
- B. Partition the table on the date column
- C. Run OPTIMIZE to compact the small files
- D. Apply Z-Order on the frequently filtered columns

### 75. A copy step processes forty independent files sequentially. What should be changed?

Domain: Monitor and optimize an analytics solution

- A. Coalesce the partitions before writing the small result
- B. Cache the DataFrame that is used twice
- C. Raise the parallelism of the copy so independent slices move together
- D. Insert the warehouse rows in batches rather than one at a time

### 76. A pipeline writes too many small files and copies them one at a time. Which two practices apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Insert the warehouse rows in batches rather than one at a time
- B. Coalesce the partitions before writing the small result
- C. Raise the parallelism of the copy so independent slices move together
- D. Cache the DataFrame that is used twice
- E. Set the shuffle partition count to match the data volume

### 77. A warehouse read scans thousands of small files per query. What should change?

Domain: Monitor and optimize an analytics solution

- A. Insert the warehouse rows in batches rather than one at a time
- B. Update statistics so the optimizer sees the current distribution
- C. Write fewer, larger files into the warehouse table
- D. Join on the distribution column so the rows stay on their node

### 78. A warehouse load inserts one row per statement and takes hours. What should change?

Domain: Monitor and optimize an analytics solution

- A. Update statistics so the optimizer sees the current distribution
- B. Insert the warehouse rows in batches rather than one at a time
- C. Write fewer, larger files into the warehouse table
- D. Join on the distribution column so the rows stay on their node

### 79. A warehouse load is slow to write and slow to read afterwards. Which two actions apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Insert the warehouse rows in batches rather than one at a time
- B. Write fewer, larger files into the warehouse table
- C. Update statistics so the optimizer sees the current distribution
- D. Join on the distribution column so the rows stay on their node
- E. Coalesce the partitions before writing the small result

### 80. A broadcast join was chosen but the plan still shows a shuffle. What should be checked?

Domain: Monitor and optimize an analytics solution

- A. Raise the broadcast threshold for the small table
- B. Keep adaptive query execution enabled so the shuffle is re-planned
- C. Enable skew join handling for the hot key
- D. Broadcast the small dimension to avoid the shuffle

### 81. One partition holds five million rows and the rest hold thousands. What should be applied?

Domain: Monitor and optimize an analytics solution

- A. Broadcast the small dimension to avoid the shuffle
- B. Keep adaptive query execution enabled so the shuffle is re-planned
- C. Salt the skewed key so the partitions even out
- D. Enable skew join handling for the hot key

### 82. A write produces one file per partition and the reader suffers. What should be done before the write?

Domain: Monitor and optimize an analytics solution

- A. Repartition before the write to control the file count
- B. Cache the DataFrame that is used twice
- C. Coalesce the partitions before writing the small result
- D. Set the shuffle partition count to match the data volume

### 83. Four jobs start together, exceed the capacity for twenty minutes, and then idle. What should be enabled?

Domain: Monitor and optimize an analytics solution

- A. Move the workspace to a larger capacity
- B. Enable capacity smoothing so a burst can borrow from the burst allowance
- C. Set the retention policy to match the query window
- D. Scale the destination throughput for the event volume

### 84. Every workload in the workspace is throttled during business hours. What is the first thing to change?

Domain: Monitor and optimize an analytics solution

- A. Move the workspace to a larger capacity
- B. Set the retention policy to match the query window
- C. Enable capacity smoothing so a burst can borrow from the burst allowance
- D. Increase the eventhouse capacity so the queries keep up

### 85. An eventhouse holds two years but every dashboard reads one day. Which two settings apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Scale the destination throughput for the event volume
- B. Increase the eventhouse capacity so the queries keep up
- C. Set the retention policy to match the query window
- D. Set the caching policy on the KQL table
- E. Enable capacity smoothing so a burst can borrow from the burst allowance

### 86. A team must detect a failing load before its users do. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Review the alert history → enable the monitoring output → set the threshold → build the dashboard
- B. Build the dashboard → set the threshold → enable the output → review the history
- C. Enable the monitoring output → build the dashboard over it → set the alert threshold → review the alert history each week
- D. Set the alert threshold → build the dashboard → review the history → enable the output

### 87. A pipeline failure must be diagnosed and rerun without reloading everything. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Read the run history → isolate the failing activity → reproduce it with the same input → rerun only the failed activity
- B. Reproduce the input → isolate the activity → read the run history → rerun the activity
- C. Rerun only the failed activity → read the run history → isolate the activity → reproduce the input
- D. Isolate the failing activity → rerun the activity → read the run history → reproduce the input

### 88. A slow query must be improved and the improvement proven. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Optimize the table → re-measure the query → read the plan → reduce the file count
- B. Reduce the file count → read the plan → re-measure the query → optimize the table
- C. Re-measure the query → optimize the table → read the plan → reduce the file count
- D. Read the query plan → reduce the file count → optimize and Z-Order the table → re-measure the query

---

## Case study — Alpine Ski House

Alpine Ski House runs six resorts and a central analytics team. Each resort has its own workspace, and all six workspaces share one capacity. The engineering team has a development workspace, a test workspace, and a production workspace, and today a release means exporting items by hand and importing them again. Two resorts are on a different data source than the other four and must keep their own connection after any promotion. The team has just adopted Git and wants every change reviewed before it reaches production. A previous release overwrote a production parameter and pointed the nightly load at a test database for two days before anyone noticed.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. Every new notebook must inherit the approved libraries. What should be configured?

Domain: Implement and manage an analytics solution

- A. Set a workspace-level custom Spark pool for the notebooks
- B. Set the default environment at the workspace level
- C. Enable high concurrency mode for shared sessions
- D. Size the pool for the node family and node count the workload needs

### 90. Two resorts must keep their own connection after promotion. What should be configured?

Domain: Implement and manage an analytics solution

- A. Add deployment rules so the target stage keeps its own connection and parameters
- B. Create a deployment pipeline with development, test, and production stages
- C. Compare the stages before promoting
- D. Deploy backwards to recover the last known-good definition

### 91. A release must be reviewable before it reaches production. What should be configured?

Domain: Implement and manage an analytics solution

- A. Add the generated artefacts to the ignore file rather than committing them
- B. Connect the workspace to a Git repository and commit the item definitions
- C. Resolve the conflict by choosing the definition that must win, then commit
- D. Work in a feature branch and merge through a pull request

---

## Case study — Northwind Traders

Northwind Traders imports specialty food from 40 suppliers and sells to 4,000 restaurants. The warehouse must hold a star schema with one fact table for order lines, conformed product, customer, and date dimensions, and a supplier dimension that changes slowly. Product categories are reorganized roughly twice a year, and the analysis must still attribute last year sales to the category the product belonged to at the time. The nightly load runs at 02:00 and must finish before the 06:00 replenishment report. Two source systems disagree about the spelling of customer names, and the sales team has asked to see both spellings reconciled into one row.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. Sales must be attributed to the category a product had at the time. What should be built?

Domain: Ingest and transform data

- A. Generate a surrogate key instead of reusing the source key
- B. Merge the incoming rows into the target on the business key
- C. Model the data as a star schema with conformed dimensions
- D. Build a type 2 dimension with validity dates and a current flag

### 93. Two systems spell the same customer differently. What should the warehouse key on?

Domain: Ingest and transform data

- A. Generate a surrogate key instead of reusing the source key
- B. Merge the incoming rows into the target on the business key
- C. Model the data as a star schema with conformed dimensions
- D. Build a type 2 dimension with validity dates and a current flag

### 94. A corrected row must replace the earlier version. What should be used?

Domain: Ingest and transform data

- A. Merge the incoming rows into the target on the business key
- B. Store the last successful load timestamp in a control table
- C. Load only the rows newer than the stored watermark
- D. Route the failed rows to a reject table and continue the load

---

## Case study — Proseware Media

Proseware Media streams video to 12 million viewers and emits a playback event for every session start, stop, and quality change. The events arrive through an event hub at up to 90,000 per second during a live finale. The analytics team wants a rolling count of concurrent viewers per channel with five-minute granularity, and the operations team wants an alert when error rates exceed a threshold for ten minutes. The events must also be joined to a slowly changing subscriber dimension to attribute viewing to a subscription tier. The company has one eventhouse and a lakehouse, and the chief data officer has forbidden a second copy of the raw events.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. A streaming notebook fails on one transformation. What shows the exception?

Domain: Monitor and optimize an analytics solution

- A. Open the Spark UI for the application
- B. Check the failing cell and the Spark driver log
- C. Inspect the failing cell output and exit value
- D. Use the Monitoring hub for the run history

### 96. Two years of events are retained but only a day is queried. What should be set?

Domain: Monitor and optimize an analytics solution

- A. Move the workspace to a larger capacity
- B. Set the caching policy on the KQL table
- C. Increase the eventhouse capacity so the queries keep up
- D. Set the retention policy to match the query window

### 97. An error rate must notify the team within ten minutes. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Use a Data Activator rule that watches the streaming condition
- B. Set the alert to fire only after the retry policy has been exhausted
- C. Send the alert to the team that owns the item
- D. Configure an alert on the failing condition

---

## Case study — Woodgrove Bank

Woodgrove Bank loads transaction and customer data into a Fabric warehouse for a regulatory reporting team. The data includes account numbers, national identifiers, and balances. Only the financial crime team may see the full national identifier; analysts may see the rest of the row. Branch managers may see only their own branch transactions, while head office sees everything. The regulator requires a record of who accessed which report and when, retained for seven years. The bank has assigned a sensitivity label of Highly Confidential to all customer data, and auditors have asked how a label applied in Fabric prevents a copied table from escaping the classification.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. Every customer table must carry a classification that survives a copy. What should be applied?

Domain: Implement and manage an analytics solution

- A. Certify the item as the approved source
- B. Promote the item as ready for reuse
- C. Let the label inherit from the labelled source file
- D. Apply the sensitivity label to the item

### 99. Branch managers may see only their own branch transactions. What should be defined?

Domain: Implement and manage an analytics solution

- A. Filter the table through a predicate that resolves the user to a region
- B. Apply column-level security so the column is hidden from the group
- C. Define a row-level security policy on the table
- D. Apply object-level security in the semantic model

### 100. The regulator asks who accessed a report and when. Where is that recorded?

Domain: Implement and manage an analytics solution

- A. Filter the audit log by activity and by item
- B. Read the Fabric audit log in the Microsoft Purview portal
- C. Read the item activity log
- D. Export the audit events before the retention window closes

---

## Answer key and explanations

### Question 1 — B

Answer: Keep OneLake availability enabled so other engines can read the same data. OneLake availability is what exposes the same files to other engines. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. Local study-map skill 1.2 (Domain and OneLake Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. Why the correct answer wins: OneLake availability is what exposes the same files to other engines.
- **B:** Correct. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. In this case: OneLake availability is what exposes the same files to other engines.
- **C:** Incorrect for this question. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. Why the correct answer wins: OneLake availability is what exposes the same files to other engines.
- **D:** Incorrect for this question. A domain groups workspaces for governance and discovery without moving the data. Why the correct answer wins: OneLake availability is what exposes the same files to other engines.

### Question 2 — C

Answer: Assign the workspace to the domain that owns the subject area. A domain groups workspaces by subject area for governance. A domain groups workspaces for governance and discovery without moving the data. Local study-map skill 1.2 (Domain and OneLake Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. Why the correct answer wins: A domain groups workspaces by subject area for governance.
- **B:** Incorrect for this question. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. Why the correct answer wins: A domain groups workspaces by subject area for governance.
- **C:** Correct. A domain groups workspaces for governance and discovery without moving the data. In this case: A domain groups workspaces by subject area for governance.
- **D:** Incorrect for this question. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. Why the correct answer wins: A domain groups workspaces by subject area for governance.

### Question 3 — D

Answer: Enable the Apache Airflow job in the workspace and author the DAG. The Airflow job runs the DAG without a rewrite. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. Local study-map skill 1.3 (Apache Airflow Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: The Airflow job runs the DAG without a rewrite.
- **B:** Incorrect for this question. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. Why the correct answer wins: The Airflow job runs the DAG without a rewrite.
- **C:** Incorrect for this question. Source-controlled DAGs keep the orchestration reviewable like any other item definition. Why the correct answer wins: The Airflow job runs the DAG without a rewrite.
- **D:** Correct. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. In this case: The Airflow job runs the DAG without a rewrite.

### Question 4 — B, C

Answers: Enable the Apache Airflow job in the workspace and author the DAG; Sync the Airflow DAG from the connected Git repository. The Airflow job runs the DAG, and Git keeps the change reviewable. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. Source-controlled DAGs keep the orchestration reviewable like any other item definition. Local study-map skill 1.3 (Apache Airflow Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. Why the correct answer wins: The Airflow job runs the DAG, and Git keeps the change reviewable.
- **B:** Correct. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. In this case: The Airflow job runs the DAG, and Git keeps the change reviewable.
- **C:** Correct. Source-controlled DAGs keep the orchestration reviewable like any other item definition. In this case: The Airflow job runs the DAG, and Git keeps the change reviewable.
- **D:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: The Airflow job runs the DAG, and Git keeps the change reviewable.
- **E:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: The Airflow job runs the DAG, and Git keeps the change reviewable.

### Question 5 — D

Answer: Add deployment rules so the target stage keeps its own connection and parameters. A deployment rule preserves the target stage's own connection. A rule stops a promotion from overwriting the target stage environment-specific settings. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The pipeline promotes the same item definitions through the stages instead of rebuilding them. Why the correct answer wins: A deployment rule preserves the target stage's own connection.
- **B:** Incorrect for this question. Promoting every item drags unrelated work into the release. Why the correct answer wins: A deployment rule preserves the target stage's own connection.
- **C:** Incorrect for this question. The comparison shows what the promotion will change in the target before it happens. Why the correct answer wins: A deployment rule preserves the target stage's own connection.
- **D:** Correct. A rule stops a promotion from overwriting the target stage environment-specific settings. In this case: A deployment rule preserves the target stage's own connection.

### Question 6 — A

Answer: Compare the stages before promoting. The stage comparison shows the pending change. The comparison shows what the promotion will change in the target before it happens. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The comparison shows what the promotion will change in the target before it happens. In this case: The stage comparison shows the pending change.
- **B:** Incorrect for this question. The pipeline promotes the same item definitions through the stages instead of rebuilding them. Why the correct answer wins: The stage comparison shows the pending change.
- **C:** Incorrect for this question. A backward deployment is the supported way to restore a previous stage state. Why the correct answer wins: The stage comparison shows the pending change.
- **D:** Incorrect for this question. A rule stops a promotion from overwriting the target stage environment-specific settings. Why the correct answer wins: The stage comparison shows the pending change.

### Question 7 — C

Answer: Grant the user a workspace role. A workspace role is the coarse grant that every item inherits. A workspace role is the coarse grant that every item in the workspace inherits. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Read is the narrowest grant that still lets the item be consumed. Why the correct answer wins: A workspace role is the coarse grant that every item inherits.
- **B:** Incorrect for this question. Item-level sharing avoids granting a workspace role for one report. Why the correct answer wins: A workspace role is the coarse grant that every item inherits.
- **C:** Correct. A workspace role is the coarse grant that every item in the workspace inherits. In this case: A workspace role is the coarse grant that every item inherits.
- **D:** Incorrect for this question. A link is a shortcut to the item, not a substitute for the permission behind it. Why the correct answer wins: A workspace role is the coarse grant that every item inherits.

### Question 8 — C

Answer: Grant Read on the item. Read on the item is the narrowest grant that still allows use. Read is the narrowest grant that still lets the item be consumed. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: Read on the item is the narrowest grant that still allows use.
- **B:** Incorrect for this question. Item-level sharing avoids granting a workspace role for one report. Why the correct answer wins: Read on the item is the narrowest grant that still allows use.
- **C:** Correct. Read is the narrowest grant that still lets the item be consumed. In this case: Read on the item is the narrowest grant that still allows use.
- **D:** Incorrect for this question. Admin is needed to manage access and settings, not to read the data. Why the correct answer wins: Read on the item is the narrowest grant that still allows use.

### Question 9 — B, D

Answers: Grant Viewer on the workspace; Share the single item with the user who needs only that item. Viewer covers the team, and item sharing covers the reviewer. Viewer allows reading the items without editing them. Item-level sharing avoids granting a workspace role for one report. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Read is the narrowest grant that still lets the item be consumed. Why the correct answer wins: Viewer covers the team, and item sharing covers the reviewer.
- **B:** Correct. Item-level sharing avoids granting a workspace role for one report. In this case: Viewer covers the team, and item sharing covers the reviewer.
- **C:** Incorrect for this question. Admin is needed to manage access and settings, not to read the data. Why the correct answer wins: Viewer covers the team, and item sharing covers the reviewer.
- **D:** Correct. Viewer allows reading the items without editing them. In this case: Viewer covers the team, and item sharing covers the reviewer.
- **E:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: Viewer covers the team, and item sharing covers the reviewer.

### Question 10 — D

Answer: Apply object-level security in the semantic model. Object-level security hides the table from the role. Object-level security hides a table or column from a role in the semantic model. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: Object-level security hides the table from the role.
- **B:** Incorrect for this question. Row-level security filters rows per identity, so one table returns different rows to different users. Why the correct answer wins: Object-level security hides the table from the role.
- **C:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: Object-level security hides the table from the role.
- **D:** Correct. Object-level security hides a table or column from a role in the semantic model. In this case: Object-level security hides the table from the role.

### Question 11 — A

Answer: Grant access at the individual file. A file-level grant is the narrowest path restriction available. A file-level grant is the narrowest path restriction the platform offers. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A file-level grant is the narrowest path restriction the platform offers. In this case: A file-level grant is the narrowest path restriction available.
- **B:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: A file-level grant is the narrowest path restriction available.
- **C:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: A file-level grant is the narrowest path restriction available.
- **D:** Incorrect for this question. Row-level security filters rows per identity, so one table returns different rows to different users. Why the correct answer wins: A file-level grant is the narrowest path restriction available.

### Question 12 — C

Answer: Expose a view with the column omitted instead of masking it. A view removes the column entirely rather than masking its value. A view removes the column entirely, which is not the same as masking the value. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Masking shows a masked value to unauthorised users while the stored data stays intact. Why the correct answer wins: A view removes the column entirely rather than masking its value.
- **B:** Incorrect for this question. The masking rule needs the exemption, or the authorised group sees masked values too. Why the correct answer wins: A view removes the column entirely rather than masking its value.
- **C:** Correct. A view removes the column entirely, which is not the same as masking the value. In this case: A view removes the column entirely rather than masking its value.
- **D:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: A view removes the column entirely rather than masking its value.

### Question 13 — B, D

Answers: Apply dynamic data masking to the column; Exempt the authorised group from the mask. The mask hides the value, and the exemption restores it for the authorised group. Masking shows a masked value to unauthorised users while the stored data stays intact. The masking rule needs the exemption, or the authorised group sees masked values too. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A report-level mask protects one visual and leaves every other consumer unmasked. Why the correct answer wins: The mask hides the value, and the exemption restores it for the authorised group.
- **B:** Correct. The masking rule needs the exemption, or the authorised group sees masked values too. In this case: The mask hides the value, and the exemption restores it for the authorised group.
- **C:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: The mask hides the value, and the exemption restores it for the authorised group.
- **D:** Correct. Masking shows a masked value to unauthorised users while the stored data stays intact. In this case: The mask hides the value, and the exemption restores it for the authorised group.
- **E:** Incorrect for this question. A view removes the column entirely, which is not the same as masking the value. Why the correct answer wins: The mask hides the value, and the exemption restores it for the authorised group.

### Question 14 — B

Answer: Set the default sensitivity label for the workspace. A workspace default label classifies items nobody labels by hand. A default label classifies new items that nobody labels by hand. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Certification tells consumers the item has been reviewed as authoritative. Why the correct answer wins: A workspace default label classifies items nobody labels by hand.
- **B:** Correct. A default label classifies new items that nobody labels by hand. In this case: A workspace default label classifies items nobody labels by hand.
- **C:** Incorrect for this question. The label travels with the item and drives the protection downstream consumers inherit. Why the correct answer wins: A workspace default label classifies items nobody labels by hand.
- **D:** Incorrect for this question. Inheritance keeps one classification instead of a second opinion on the same data. Why the correct answer wins: A workspace default label classifies items nobody labels by hand.

### Question 15 — D

Answer: Promote the item as ready for reuse. Promotion signals readiness without claiming a review. Promotion signals readiness without the review that certification implies. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A default label classifies new items that nobody labels by hand. Why the correct answer wins: Promotion signals readiness without claiming a review.
- **B:** Incorrect for this question. Certification tells consumers the item has been reviewed as authoritative. Why the correct answer wins: Promotion signals readiness without claiming a review.
- **C:** Incorrect for this question. The label travels with the item and drives the protection downstream consumers inherit. Why the correct answer wins: Promotion signals readiness without claiming a review.
- **D:** Correct. Promotion signals readiness without the review that certification implies. In this case: Promotion signals readiness without claiming a review.

### Question 16 — D

Answer: Export the audit events before the retention window closes. Exporting the events before the window closes preserves the evidence. The audit log has a retention window, so an investigation that starts late needs the export. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Filtering turns a very large log into the events that answer the question. Why the correct answer wins: Exporting the events before the window closes preserves the evidence.
- **B:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: Exporting the events before the window closes preserves the evidence.
- **C:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: Exporting the events before the window closes preserves the evidence.
- **D:** Correct. The audit log has a retention window, so an investigation that starts late needs the export. In this case: Exporting the events before the window closes preserves the evidence.

### Question 17 — C, D

Answers: Read the Fabric audit log in the Microsoft Purview portal; Filter the audit log by activity and by item. The audit log holds the events, and filtering narrows them to the question. The audit log records who did what to which item and when. Filtering turns a very large log into the events that answer the question. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The audit log has a retention window, so an investigation that starts late needs the export. Why the correct answer wins: The audit log holds the events, and filtering narrows them to the question.
- **B:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The audit log holds the events, and filtering narrows them to the question.
- **C:** Correct. The audit log records who did what to which item and when. In this case: The audit log holds the events, and filtering narrows them to the question.
- **D:** Correct. Filtering turns a very large log into the events that answer the question. In this case: The audit log holds the events, and filtering narrows them to the question.
- **E:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The audit log holds the events, and filtering narrows them to the question.

### Question 18 — D

Answer: Configure OneLake security roles for the lakehouse. OneLake security governs the data independently of the workspace role. OneLake security governs data access independently of the workspace role. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: OneLake security governs the data independently of the workspace role.
- **B:** Incorrect for this question. A folder-scoped role restricts exactly the data rather than the whole lakehouse. Why the correct answer wins: OneLake security governs the data independently of the workspace role.
- **C:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: OneLake security governs the data independently of the workspace role.
- **D:** Correct. OneLake security governs data access independently of the workspace role. In this case: OneLake security governs the data independently of the workspace role.

### Question 19 — D

Answer: Grant the OneLake role to a security group rather than to individuals. A group grant is maintained once rather than once per person. A group grant is maintained once instead of once per person. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Admin is needed to manage access and settings, not to read the data. Why the correct answer wins: A group grant is maintained once rather than once per person.
- **B:** Incorrect for this question. OneLake security governs data access independently of the workspace role. Why the correct answer wins: A group grant is maintained once rather than once per person.
- **C:** Incorrect for this question. A folder-scoped role restricts exactly the data rather than the whole lakehouse. Why the correct answer wins: A group grant is maintained once rather than once per person.
- **D:** Correct. A group grant is maintained once instead of once per person. In this case: A group grant is maintained once rather than once per person.

### Question 20 — C

Answer: Use a T-SQL script against the warehouse. Set-based T-SQL is the natural engine once the data is relational there. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: Set-based T-SQL is the natural engine once the data is relational there.
- **B:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: Set-based T-SQL is the natural engine once the data is relational there.
- **C:** Correct. Set-based T-SQL is the natural choice when the data already sits in the warehouse. In this case: Set-based T-SQL is the natural engine once the data is relational there.
- **D:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: Set-based T-SQL is the natural engine once the data is relational there.

### Question 21 — D

Answer: Use a KQL query against the eventhouse. KQL is the native language of the eventhouse tables. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: KQL is the native language of the eventhouse tables.
- **B:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: KQL is the native language of the eventhouse tables.
- **C:** Incorrect for this question. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Why the correct answer wins: KQL is the native language of the eventhouse tables.
- **D:** Correct. In this case: KQL is the native language of the eventhouse tables.

### Question 22 — B, C

Answers: Use a pipeline for the copy and the orchestration; Use a notebook for the transformation. The pipeline owns the copy and the order, and the notebook holds the PySpark. A pipeline owns the scheduling, the copy activity, and the dependency between steps. A notebook is the right place for PySpark that a low-code transform cannot express. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Why the correct answer wins: The pipeline owns the copy and the order, and the notebook holds the PySpark.
- **B:** Correct. A pipeline owns the scheduling, the copy activity, and the dependency between steps. In this case: The pipeline owns the copy and the order, and the notebook holds the PySpark.
- **C:** Correct. A notebook is the right place for PySpark that a low-code transform cannot express. In this case: The pipeline owns the copy and the order, and the notebook holds the PySpark.
- **D:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: The pipeline owns the copy and the order, and the notebook holds the PySpark.
- **E:** Incorrect for this question. KQL is the native language of the eventhouse tables. Why the correct answer wins: The pipeline owns the copy and the order, and the notebook holds the PySpark.

### Question 23 — C

Answer: Add a schedule trigger with the cadence and time zone the business expects. A schedule trigger recurs without a person starting the run. The schedule trigger is what makes the run recur without a person starting it. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A parameter makes one pipeline reusable across folders and environments. Why the correct answer wins: A schedule trigger recurs without a person starting the run.
- **B:** Incorrect for this question. An event trigger removes the gap between the file landing and the run starting. Why the correct answer wins: A schedule trigger recurs without a person starting the run.
- **C:** Correct. The schedule trigger is what makes the run recur without a person starting it. In this case: A schedule trigger recurs without a person starting the run.
- **D:** Incorrect for this question. The file-created event is the signal that the extract has finished arriving. Why the correct answer wins: A schedule trigger recurs without a person starting the run.

### Question 24 — A

Answer: Pass the folder path as a pipeline parameter. A parameter makes one pipeline reusable across folders. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. In this case: A parameter makes one pipeline reusable across folders.
- **B:** Incorrect for this question. A variable carries the computed value between the activities that need it. Why the correct answer wins: A parameter makes one pipeline reusable across folders.
- **C:** Incorrect for this question. The lookup is what makes the load incremental rather than a full reload. Why the correct answer wins: A parameter makes one pipeline reusable across folders.
- **D:** Incorrect for this question. A dynamic expression computes the path instead of hard-coding a date. Why the correct answer wins: A parameter makes one pipeline reusable across folders.

### Question 25 — A, D

Answers: Add a schedule trigger with the cadence and time zone the business expects; Build the path with a dynamic expression at run time. The schedule sets the cadence, and the expression builds the folder name. The schedule trigger is what makes the run recur without a person starting it. A dynamic expression computes the path instead of hard-coding a date. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The schedule trigger is what makes the run recur without a person starting it. In this case: The schedule sets the cadence, and the expression builds the folder name.
- **B:** Incorrect for this question. The lookup is what makes the load incremental rather than a full reload. Why the correct answer wins: The schedule sets the cadence, and the expression builds the folder name.
- **C:** Incorrect for this question. An event trigger removes the gap between the file landing and the run starting. Why the correct answer wins: The schedule sets the cadence, and the expression builds the folder name.
- **D:** Correct. A dynamic expression computes the path instead of hard-coding a date. In this case: The schedule sets the cadence, and the expression builds the folder name.
- **E:** Incorrect for this question. A variable carries the computed value between the activities that need it. Why the correct answer wins: The schedule sets the cadence, and the expression builds the folder name.

### Question 26 — A

Answer: Confirm the source of truth → apply the label → endorse the item → verify the audit entry. Authority is confirmed before the endorsement claims it. Endorsement claims authority, so the authority is confirmed first, and the audit entry is the proof that the governance action was recorded. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Endorsement claims authority, so the authority is confirmed first, and the audit entry is the proof that the governance action was recorded. In this case: Authority is confirmed before the endorsement claims it.
- **B:** Incorrect for this question. Endorsing before confirming the source of truth endorses whatever happened to be there. Why the correct answer wins: Authority is confirmed before the endorsement claims it.
- **C:** Incorrect for this question. The audit entry records actions that have already happened, so it cannot come first. Why the correct answer wins: Authority is confirmed before the endorsement claims it.
- **D:** Incorrect for this question. The label follows the classification, and the audit entry follows the actions it records. Why the correct answer wins: Authority is confirmed before the endorsement claims it.

### Question 27 — D

Answer: Connect the workspace to Git → commit the item definitions → create the deployment pipeline → add deployment rules → promote through the stages. The definitions are committed before the pipeline promotes them. The definitions have to be in source control before the pipeline promotes them, and the rules are added before the first promotion. Local study-map skill 1.4 (Version Control and Database Projects), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Every step is in the wrong order: a promotion needs the pipeline, the pipeline needs the definitions in Git, and the rules come first. Why the correct answer wins: The definitions are committed before the pipeline promotes them.
- **B:** Incorrect for this question. There is nothing to commit before the repository is connected, and the rules belong to a pipeline that does not exist yet. Why the correct answer wins: The definitions are committed before the pipeline promotes them.
- **C:** Incorrect for this question. Promoting before the definitions are committed and before the rules exist overwrites the target with the wrong settings. Why the correct answer wins: The definitions are committed before the pipeline promotes them.
- **D:** Correct. The definitions have to be in source control before the pipeline promotes them, and the rules are added before the first promotion. In this case: The definitions are committed before the pipeline promotes them.

### Question 28 — B

Answer: Replace the missing value with a documented default. A documented default keeps the aggregate correct. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: A documented default keeps the aggregate correct.
- **B:** Correct. In this case: A documented default keeps the aggregate correct.
- **C:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: A documented default keeps the aggregate correct.
- **D:** Incorrect for this question. Reprocessing the partition corrects the aggregate that was already published. Why the correct answer wins: A documented default keeps the aggregate correct.

### Question 29 — C

Answer: Set a checkpoint location for the streaming query. The checkpoint records where the stream should resume. The checkpoint is what makes the stream restart from where it stopped. Local study-map skill 2.3 (Streaming Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A batch job over the landing folder adds latency the streaming requirement may not allow. Why the correct answer wins: The checkpoint records where the stream should resume.
- **B:** Incorrect for this question. A watermark sets how long the engine waits for late events before closing a window. Why the correct answer wins: The checkpoint records where the stream should resume.
- **C:** Correct. The checkpoint is what makes the stream restart from where it stopped. In this case: The checkpoint records where the stream should resume.
- **D:** Incorrect for this question. Native tables give full KQL capability over the streaming data. Why the correct answer wins: The checkpoint records where the stream should resume.

### Question 30 — B

Answer: Create a KQL database for the time-series queries. A KQL database indexes the timestamp for those range queries. A KQL database indexes the timestamp column for the range queries the dashboards run. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The Files area keeps the raw extract in its original format. Why the correct answer wins: A KQL database indexes the timestamp for those range queries.
- **B:** Correct. A KQL database indexes the timestamp column for the range queries the dashboards run. In this case: A KQL database indexes the timestamp for those range queries.
- **C:** Incorrect for this question. The endpoint gives read-only T-SQL over the Delta tables without a copy. Why the correct answer wins: A KQL database indexes the timestamp for those range queries.
- **D:** Incorrect for this question. A warehouse gives multi-table T-SQL transactions and a governed relational model. Why the correct answer wins: A KQL database indexes the timestamp for those range queries.

### Question 31 — A

Answer: Query the lakehouse through its SQL analytics endpoint. The SQL analytics endpoint reads the Delta tables in place. The endpoint gives read-only T-SQL over the Delta tables without a copy. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. The endpoint gives read-only T-SQL over the Delta tables without a copy. In this case: The SQL analytics endpoint reads the Delta tables in place.
- **B:** Incorrect for this question. An eventhouse is optimized for high-volume time-series queries. Why the correct answer wins: The SQL analytics endpoint reads the Delta tables in place.
- **C:** Incorrect for this question. A Delta table in Tables is what the SQL analytics endpoint exposes. Why the correct answer wins: The SQL analytics endpoint reads the Delta tables in place.
- **D:** Incorrect for this question. A warehouse gives multi-table T-SQL transactions and a governed relational model. Why the correct answer wins: The SQL analytics endpoint reads the Delta tables in place.

### Question 32 — D

Answer: Transform with PySpark in a notebook. PySpark handles the windowed transformation at that scale. PySpark handles the row-level and windowed transformations that Spark scales. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: PySpark handles the windowed transformation at that scale.
- **B:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: PySpark handles the windowed transformation at that scale.
- **C:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: PySpark handles the windowed transformation at that scale.
- **D:** Correct. PySpark handles the row-level and windowed transformations that Spark scales. In this case: PySpark handles the windowed transformation at that scale.

### Question 33 — B

Answer: Transform with KQL in the eventhouse. KQL is the native language for the eventhouse tables. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: KQL is the native language for the eventhouse tables.
- **B:** Correct. In this case: KQL is the native language for the eventhouse tables.
- **C:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: KQL is the native language for the eventhouse tables.
- **D:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: KQL is the native language for the eventhouse tables.

### Question 34 — B

Answer: Create a shortcut rather than a copy when the source stays authoritative. A shortcut has no second copy to keep in step. Local study-map skill 2.6 (OneLake Shortcuts), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The shortcut exposes the external container as if the files were in OneLake. Why the correct answer wins: A shortcut has no second copy to keep in step.
- **B:** Correct. In this case: A shortcut has no second copy to keep in step.
- **C:** Incorrect for this question. A copy duplicates the data, so the source of truth is no longer one place. Why the correct answer wins: A shortcut has no second copy to keep in step.
- **D:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: A shortcut has no second copy to keep in step.

### Question 35 — A

Answer: Enable query acceleration on the shortcut. Query acceleration caches the columns the report reads. Query acceleration caches the columns a report reads, so the remote source is not scanned per query. Local study-map skill 2.6 (OneLake Shortcuts), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Query acceleration caches the columns a report reads, so the remote source is not scanned per query. In this case: Query acceleration caches the columns the report reads.
- **B:** Incorrect for this question. The shortcut exposes the external container as if the files were in OneLake. Why the correct answer wins: Query acceleration caches the columns the report reads.
- **C:** Incorrect for this question. A copy duplicates the data, so the source of truth is no longer one place. Why the correct answer wins: Query acceleration caches the columns the report reads.
- **D:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: Query acceleration caches the columns the report reads.

### Question 36 — C

Answer: Rely on change data capture so the mirror needs no pipeline schedule. Change data capture streams the changes into the mirror. Change data capture streams the changes instead of a periodic full compare. Local study-map skill 2.7 (Mirroring), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: Change data capture streams the changes into the mirror.
- **B:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: Change data capture streams the changes into the mirror.
- **C:** Correct. Change data capture streams the changes instead of a periodic full compare. In this case: Change data capture streams the changes into the mirror.
- **D:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: Change data capture streams the changes into the mirror.

### Question 37 — A, C

Answers: Enable mirroring for the operational database; Mirror from a read replica so the source database keeps its capacity. Mirroring replicates the tables, and the replica absorbs the read load. Mirroring replicates the source tables continuously into OneLake. The replica absorbs the read load the mirror creates. Local study-map skill 2.7 (Mirroring), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Mirroring replicates the source tables continuously into OneLake. In this case: Mirroring replicates the tables, and the replica absorbs the read load.
- **B:** Incorrect for this question. Change data capture streams the changes instead of a periodic full compare. Why the correct answer wins: Mirroring replicates the tables, and the replica absorbs the read load.
- **C:** Correct. The replica absorbs the read load the mirror creates. In this case: Mirroring replicates the tables, and the replica absorbs the read load.
- **D:** Incorrect for this question. The shortcut exposes the external container as if the files were in OneLake. Why the correct answer wins: Mirroring replicates the tables, and the replica absorbs the read load.
- **E:** Incorrect for this question. Appending preserves the earlier loads that the incremental pattern depends on. Why the correct answer wins: Mirroring replicates the tables, and the replica absorbs the read load.

### Question 38 — C

Answer: Copy the files as binary and parse them downstream. A binary copy keeps the file exactly as the source delivered it. A binary copy keeps the source exactly as delivered for later validation. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Appending preserves the earlier loads that the incremental pattern depends on. Why the correct answer wins: A binary copy keeps the file exactly as the source delivered it.
- **B:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: A binary copy keeps the file exactly as the source delivered it.
- **C:** Correct. A binary copy keeps the source exactly as delivered for later validation. In this case: A binary copy keeps the file exactly as the source delivered it.
- **D:** Incorrect for this question. Get Metadata turns an unknown folder into a list the loop can iterate. Why the correct answer wins: A binary copy keeps the file exactly as the source delivered it.

### Question 39 — C

Answer: Delete the processed source file after the load succeeds. Deleting the source after success stops the second pickup. Deleting after success prevents the same file being loaded twice. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: Deleting the source after success stops the second pickup.
- **B:** Incorrect for this question. Appending preserves the earlier loads that the incremental pattern depends on. Why the correct answer wins: Deleting the source after success stops the second pickup.
- **C:** Correct. Deleting after success prevents the same file being loaded twice. In this case: Deleting the source after success stops the second pickup.
- **D:** Incorrect for this question. Get Metadata turns an unknown folder into a list the loop can iterate. Why the correct answer wins: Deleting the source after success stops the second pickup.

### Question 40 — A, B

Answers: Use Get Metadata to list the files to process; Append the new files instead of overwriting the target. Get Metadata lists the files, and appending keeps the history. Get Metadata turns an unknown folder into a list the loop can iterate. Appending preserves the earlier loads that the incremental pattern depends on. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Get Metadata turns an unknown folder into a list the loop can iterate. In this case: Get Metadata lists the files, and appending keeps the history.
- **B:** Correct. Appending preserves the earlier loads that the incremental pattern depends on. In this case: Get Metadata lists the files, and appending keeps the history.
- **C:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: Get Metadata lists the files, and appending keeps the history.
- **D:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: Get Metadata lists the files, and appending keeps the history.
- **E:** Incorrect for this question. Deleting after success prevents the same file being loaded twice. Why the correct answer wins: Get Metadata lists the files, and appending keeps the history.

### Question 41 — D

Answer: Use a window function to rank within the partition. A window function accumulates within the partition. A window computes across related rows without collapsing them into one. Local study-map skill 2.9 (PySpark Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: A window function accumulates within the partition.
- **B:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: A window function accumulates within the partition.
- **C:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: A window function accumulates within the partition.
- **D:** Correct. A window computes across related rows without collapsing them into one. In this case: A window function accumulates within the partition.

### Question 42 — B

Answer: Transform with T-SQL against the warehouse. T-SQL is the right engine when the dimension already lives in the warehouse. T-SQL is the right engine once the data is relational and already in the warehouse. Local study-map skill 2.10 (T-SQL and KQL Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: T-SQL is the right engine when the dimension already lives in the warehouse.
- **B:** Correct. T-SQL is the right engine once the data is relational and already in the warehouse. In this case: T-SQL is the right engine when the dimension already lives in the warehouse.
- **C:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: T-SQL is the right engine when the dimension already lives in the warehouse.
- **D:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: T-SQL is the right engine when the dimension already lives in the warehouse.

### Question 43 — B, D

Answers: Transform with T-SQL against the warehouse; Transform with KQL in the eventhouse. T-SQL performs the merge, and KQL filters the eventhouse rows. T-SQL is the right engine once the data is relational and already in the warehouse. KQL is the native language for the eventhouse tables. Local study-map skill 2.10 (T-SQL and KQL Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: T-SQL performs the merge, and KQL filters the eventhouse rows.
- **B:** Correct. KQL is the native language for the eventhouse tables. In this case: T-SQL performs the merge, and KQL filters the eventhouse rows.
- **C:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: T-SQL performs the merge, and KQL filters the eventhouse rows.
- **D:** Correct. T-SQL is the right engine once the data is relational and already in the warehouse. In this case: T-SQL performs the merge, and KQL filters the eventhouse rows.
- **E:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: T-SQL performs the merge, and KQL filters the eventhouse rows.

### Question 44 — C

Answer: Union the sources after conforming the columns. The columns must be conformed before the union is valid. Conforming the columns first is what makes the union valid. Local study-map skill 2.11 (Denormalization, Grouping, and Aggregation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: The columns must be conformed before the union is valid.
- **B:** Incorrect for this question. Denormalization trades storage for the query shape the report actually uses. Why the correct answer wins: The columns must be conformed before the union is valid.
- **C:** Correct. Conforming the columns first is what makes the union valid. In this case: The columns must be conformed before the union is valid.
- **D:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: The columns must be conformed before the union is valid.

### Question 45 — C

Answer: Pivot the rows into the reporting columns. The pivot produces one column per period. The pivot is what produces one column per period the report expects. Local study-map skill 2.11 (Denormalization, Grouping, and Aggregation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: The pivot produces one column per period.
- **B:** Incorrect for this question. A window computes across related rows without collapsing them into one. Why the correct answer wins: The pivot produces one column per period.
- **C:** Correct. The pivot is what produces one column per period the report expects. In this case: The pivot produces one column per period.
- **D:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: The pivot produces one column per period.

### Question 46 — B

Answer: Deduplicate on the business key and keep the latest version. Keeping the latest version means the surviving row is the one already acted on. Keeping the latest version means the surviving row is the one the business already acted on. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: Keeping the latest version means the surviving row is the one already acted on.
- **B:** Correct. Keeping the latest version means the surviving row is the one the business already acted on. In this case: Keeping the latest version means the surviving row is the one already acted on.
- **C:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Keeping the latest version means the surviving row is the one already acted on.
- **D:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Keeping the latest version means the surviving row is the one already acted on.

### Question 47 — B

Answer: Reprocess the closed window when a late event arrives. Reprocessing the window corrects the total that was reported. Reprocessing the window is what corrects a total that was already reported. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Zero is a value, so it changes an average even when the measure is a sum. Why the correct answer wins: Reprocessing the window corrects the total that was reported.
- **B:** Correct. Reprocessing the window is what corrects a total that was already reported. In this case: Reprocessing the window corrects the total that was reported.
- **C:** Incorrect for this question. Dropping the event silently understates the total it belonged to. Why the correct answer wins: Reprocessing the window corrects the total that was reported.
- **D:** Incorrect for this question. Reprocessing the partition corrects the aggregate that was already published. Why the correct answer wins: Reprocessing the window corrects the total that was reported.

### Question 48 — B

Answer: Process the stream with Spark structured streaming. Structured streaming reuses the batch logic over an unbounded source. Structured streaming suits stateful processing and the same PySpark logic used in batch. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. An update policy transforms the data as it lands in the KQL table. Why the correct answer wins: Structured streaming reuses the batch logic over an unbounded source.
- **B:** Correct. Structured streaming suits stateful processing and the same PySpark logic used in batch. In this case: Structured streaming reuses the batch logic over an unbounded source.
- **C:** Incorrect for this question. An eventstream is the no-code path from a source to a destination. Why the correct answer wins: Structured streaming reuses the batch logic over an unbounded source.
- **D:** Incorrect for this question. A batch job over the landing folder adds latency the streaming requirement may not allow. Why the correct answer wins: Structured streaming reuses the batch logic over an unbounded source.

### Question 49 — B, C

Answers: Process the stream with an eventstream; Process the stream with a KQL update policy. The eventstream is the no-code path, and the update policy transforms on arrival. An eventstream is the no-code path from a source to a destination. An update policy transforms the data as it lands in the KQL table. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The checkpoint is what makes the stream restart from where it stopped. Why the correct answer wins: The eventstream is the no-code path, and the update policy transforms on arrival.
- **B:** Correct. An eventstream is the no-code path from a source to a destination. In this case: The eventstream is the no-code path, and the update policy transforms on arrival.
- **C:** Correct. An update policy transforms the data as it lands in the KQL table. In this case: The eventstream is the no-code path, and the update policy transforms on arrival.
- **D:** Incorrect for this question. A batch job over the landing folder adds latency the streaming requirement may not allow. Why the correct answer wins: The eventstream is the no-code path, and the update policy transforms on arrival.
- **E:** Incorrect for this question. Structured streaming suits stateful processing and the same PySpark logic used in batch. Why the correct answer wins: The eventstream is the no-code path, and the update policy transforms on arrival.

### Question 50 — B

Answer: Set a checkpoint location for the streaming query. The checkpoint is what lets the query resume. The checkpoint is what makes the stream restart from where it stopped. Local study-map skill 2.14 (Eventstream and Spark Structured Streaming), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A watermark sets how long the engine waits for late events before closing a window. Why the correct answer wins: The checkpoint is what lets the query resume.
- **B:** Correct. The checkpoint is what makes the stream restart from where it stopped. In this case: The checkpoint is what lets the query resume.
- **C:** Incorrect for this question. An eventstream is the no-code path from a source to a destination. Why the correct answer wins: The checkpoint is what lets the query resume.
- **D:** Incorrect for this question. Native tables give full KQL capability over the streaming data. Why the correct answer wins: The checkpoint is what lets the query resume.

### Question 51 — B, E

Answers: Set a checkpoint location for the streaming query; Set a watermark so late events are handled deterministically. The checkpoint resumes the query, and the watermark bounds the lateness. The checkpoint is what makes the stream restart from where it stopped. A watermark sets how long the engine waits for late events before closing a window. Local study-map skill 2.14 (Eventstream and Spark Structured Streaming), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: The checkpoint resumes the query, and the watermark bounds the lateness.
- **B:** Correct. A watermark sets how long the engine waits for late events before closing a window. In this case: The checkpoint resumes the query, and the watermark bounds the lateness.
- **C:** Incorrect for this question. Native tables give full KQL capability over the streaming data. Why the correct answer wins: The checkpoint resumes the query, and the watermark bounds the lateness.
- **D:** Incorrect for this question. An eventstream is the no-code path from a source to a destination. Why the correct answer wins: The checkpoint resumes the query, and the watermark bounds the lateness.
- **E:** Correct. The checkpoint is what makes the stream restart from where it stopped. In this case: The checkpoint resumes the query, and the watermark bounds the lateness.

### Question 52 — A

Answer: Profile the source keys → define the grain of the fact → build the conformed dimensions → add the surrogate keys → load the fact. The keys are profiled before the grain, the dimensions, and the fact. Profiling the keys settles the grain, the grain settles the dimensions, and the fact loads against the keys those dimensions own. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Profiling the keys settles the grain, the grain settles the dimensions, and the fact loads against the keys those dimensions own. In this case: The keys are profiled before the grain, the dimensions, and the fact.
- **B:** Incorrect for this question. The fact is loaded before the keys it references exist. Why the correct answer wins: The keys are profiled before the grain, the dimensions, and the fact.
- **C:** Incorrect for this question. Surrogate keys are assigned by the dimensions, which do not exist yet. Why the correct answer wins: The keys are profiled before the grain, the dimensions, and the fact.
- **D:** Incorrect for this question. The keys are profiled and the dimensions built before the fact can be loaded. Why the correct answer wins: The keys are profiled before the grain, the dimensions, and the fact.

### Question 53 — A

Answer: Land the raw files unchanged → validate the schema and reject the bad rows → conform and deduplicate into silver → publish the gold table. Validation follows landing and precedes publication. Raw data is preserved, validation happens before any transformation hides a problem, and the curated table is the last thing published. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Raw data is preserved, validation happens before any transformation hides a problem, and the curated table is the last thing published. In this case: Validation follows landing and precedes publication.
- **B:** Incorrect for this question. The published table would be rebuilt from data that has not landed yet. Why the correct answer wins: Validation follows landing and precedes publication.
- **C:** Incorrect for this question. Conforming before the raw data lands transforms whatever was already there, and validation after publication is too late. Why the correct answer wins: Validation follows landing and precedes publication.
- **D:** Incorrect for this question. There is nothing to validate and nothing to publish before the raw files exist. Why the correct answer wins: Validation follows landing and precedes publication.

### Question 54 — D

Answer: Detect the duplicates and the late rows → decide the surviving record → correct the affected partition → recompute the aggregate. Detection and the survivor rule precede the correction and the recompute. The detection comes first, the rule decides the survivor, the partition is corrected, and only then is the published total recomputed. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A rule chosen before the duplicates are known is chosen blind. Why the correct answer wins: Detection and the survivor rule precede the correction and the recompute.
- **B:** Incorrect for this question. Recomputing before the data is corrected republishes the same wrong total. Why the correct answer wins: Detection and the survivor rule precede the correction and the recompute.
- **C:** Incorrect for this question. The partition cannot be corrected before the rule decides which record survives. Why the correct answer wins: Detection and the survivor rule precede the correction and the recompute.
- **D:** Correct. The detection comes first, the rule decides the survivor, the partition is corrected, and only then is the published total recomputed. In this case: Detection and the survivor rule precede the correction and the recompute.

### Question 55 — C

Answer: Store the telemetry in an eventhouse KQL database. An eventhouse is optimized for high-volume arrival and range queries. An eventhouse is optimized for high-volume time-series queries. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A warehouse gives multi-table T-SQL transactions and a governed relational model. Why the correct answer wins: An eventhouse is optimized for high-volume arrival and range queries.
- **B:** Incorrect for this question. A KQL database indexes the timestamp column for the range queries the dashboards run. Why the correct answer wins: An eventhouse is optimized for high-volume arrival and range queries.
- **C:** Correct. An eventhouse is optimized for high-volume time-series queries. In this case: An eventhouse is optimized for high-volume arrival and range queries.
- **D:** Incorrect for this question. The endpoint gives read-only T-SQL over the Delta tables without a copy. Why the correct answer wins: An eventhouse is optimized for high-volume arrival and range queries.

### Question 56 — A

Answer: Use a tumbling window for the fixed five-minute aggregate. A tumbling window covers fixed, non-overlapping intervals. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. In this case: A tumbling window covers fixed, non-overlapping intervals.
- **B:** Incorrect for this question. A sliding window emits on the event that satisfies the condition rather than on a fixed boundary. Why the correct answer wins: A tumbling window covers fixed, non-overlapping intervals.
- **C:** Incorrect for this question. A materialized view keeps the aggregate fresh instead of recomputing it per query. Why the correct answer wins: A tumbling window covers fixed, non-overlapping intervals.
- **D:** Incorrect for this question. A hopping window covers overlapping intervals so a trend can be smoothed. Why the correct answer wins: A tumbling window covers fixed, non-overlapping intervals.

### Question 57 — D

Answer: Process the stream with an eventstream. An eventstream is the no-code path between source and destination. An eventstream is the no-code path from a source to a destination. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Structured streaming suits stateful processing and the same PySpark logic used in batch. Why the correct answer wins: An eventstream is the no-code path between source and destination.
- **B:** Incorrect for this question. An update policy transforms the data as it lands in the KQL table. Why the correct answer wins: An eventstream is the no-code path between source and destination.
- **C:** Incorrect for this question. A batch job over the landing folder adds latency the streaming requirement may not allow. Why the correct answer wins: An eventstream is the no-code path between source and destination.
- **D:** Correct. An eventstream is the no-code path from a source to a destination. In this case: An eventstream is the no-code path between source and destination.

### Question 58 — B

Answer: Use the Monitoring hub for the run history. The Monitoring hub lists every run with its status. The hub lists every run with its status, duration, and owning item. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The Monitoring hub lists every run with its status.
- **B:** Correct. The hub lists every run with its status, duration, and owning item. In this case: The Monitoring hub lists every run with its status.
- **C:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The Monitoring hub lists every run with its status.
- **D:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The Monitoring hub lists every run with its status.

### Question 59 — B

Answer: Read the item activity log. The item activity log covers that item's runs. The activity log records the runs of one item with their outcomes. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The item activity log covers that item's runs.
- **B:** Correct. The activity log records the runs of one item with their outcomes. In this case: The item activity log covers that item's runs.
- **C:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The item activity log covers that item's runs.
- **D:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The item activity log covers that item's runs.

### Question 60 — A

Answer: Read the refresh history for the semantic model. The refresh history records each attempt and its outcome. The refresh history separates a failed refresh from a slow one. Local study-map skill 3.2 (Monitoring Semantic Model Refresh), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The refresh history separates a failed refresh from a slow one. In this case: The refresh history records each attempt and its outcome.
- **B:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The refresh history records each attempt and its outcome.
- **C:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The refresh history records each attempt and its outcome.
- **D:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The refresh history records each attempt and its outcome.

### Question 61 — B, C

Answers: Read the refresh history for the semantic model; Send the logs to a Log Analytics workspace. The refresh history triages, and Log Analytics keeps the longer record. The refresh history separates a failed refresh from a slow one. Log Analytics keeps the history that the in-product views expire. Local study-map skill 3.2 (Monitoring Semantic Model Refresh), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The refresh history triages, and Log Analytics keeps the longer record.
- **B:** Correct. The refresh history separates a failed refresh from a slow one. In this case: The refresh history triages, and Log Analytics keeps the longer record.
- **C:** Correct. Log Analytics keeps the history that the in-product views expire. In this case: The refresh history triages, and Log Analytics keeps the longer record.
- **D:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The refresh history triages, and Log Analytics keeps the longer record.
- **E:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The refresh history triages, and Log Analytics keeps the longer record.

### Question 62 — A

Answer: Send the alert to the team that owns the item. The alert must reach the team that owns the item. The alert must reach the owner, or it becomes noise nobody acts on. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The alert must reach the owner, or it becomes noise nobody acts on. In this case: The alert must reach the team that owns the item.
- **B:** Incorrect for this question. A dashboard over the monitoring table makes the trend visible between runs. Why the correct answer wins: The alert must reach the team that owns the item.
- **C:** Incorrect for this question. An activator rule evaluates the stream and fires when the condition holds. Why the correct answer wins: The alert must reach the team that owns the item.
- **D:** Incorrect for this question. An alert turns a silent failure into a notification. Why the correct answer wins: The alert must reach the team that owns the item.

### Question 63 — D

Answer: Alert on every successful run as well as every failure. Alerting on success as well as failure trains the team to ignore it. Alerting on success as well as failure trains the team to ignore the alert. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. An alert turns a silent failure into a notification. Why the correct answer wins: Alerting on success as well as failure trains the team to ignore it.
- **B:** Incorrect for this question. Waiting for the retries stops a transient failure being reported as an outage. Why the correct answer wins: Alerting on success as well as failure trains the team to ignore it.
- **C:** Incorrect for this question. The alert must reach the owner, or it becomes noise nobody acts on. Why the correct answer wins: Alerting on success as well as failure trains the team to ignore it.
- **D:** Correct. Alerting on success as well as failure trains the team to ignore the alert. In this case: Alerting on success as well as failure trains the team to ignore it.

### Question 64 — B

Answer: Add an error branch so the failure is handled rather than ignored. An error branch turns a silent failure into an explicit outcome. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. A retry absorbs a transient failure that the next attempt would not repeat. Why the correct answer wins: An error branch turns a silent failure into an explicit outcome.
- **B:** Correct. In this case: An error branch turns a silent failure into an explicit outcome.
- **C:** Incorrect for this question. Until repeats the check and stops when the condition is met or the timeout expires. Why the correct answer wins: An error branch turns a silent failure into an explicit outcome.
- **D:** Incorrect for this question. The dependency is what makes the failure path execute at all. Why the correct answer wins: An error branch turns a silent failure into an explicit outcome.

### Question 65 — D

Answer: Set the failure dependency so the handler runs when the step fails. The failure dependency is what makes the handler run. The dependency is what makes the failure path execute at all. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Until repeats the check and stops when the condition is met or the timeout expires. Why the correct answer wins: The failure dependency is what makes the handler run.
- **B:** Incorrect for this question. An error branch turns a silent failure into an explicit outcome. Why the correct answer wins: The failure dependency is what makes the handler run.
- **C:** Incorrect for this question. A retry absorbs a transient failure that the next attempt would not repeat. Why the correct answer wins: The failure dependency is what makes the handler run.
- **D:** Correct. The dependency is what makes the failure path execute at all. In this case: The failure dependency is what makes the handler run.

### Question 66 — A

Answer: Inspect the failing cell output and exit value. The failing cell's output reports the exception with its stack. The cell output is where the exception is reported with its stack. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The cell output is where the exception is reported with its stack. In this case: The failing cell's output reports the exception with its stack.
- **B:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The failing cell's output reports the exception with its stack.
- **C:** Incorrect for this question. The Spark UI shows the stages and tasks where the time went. Why the correct answer wins: The failing cell's output reports the exception with its stack.
- **D:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The failing cell's output reports the exception with its stack.

### Question 67 — C

Answer: Open the Spark UI for the application. The Spark UI shows where the stages spent the time. The Spark UI shows the stages and tasks where the time went. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The Spark UI shows where the stages spent the time.
- **B:** Incorrect for this question. The cell output is where the exception is reported with its stack. Why the correct answer wins: The Spark UI shows where the stages spent the time.
- **C:** Correct. The Spark UI shows the stages and tasks where the time went. In this case: The Spark UI shows where the stages spent the time.
- **D:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The Spark UI shows where the stages spent the time.

### Question 68 — B

Answer: Query the ingestion failures table in the KQL database. The ingestion failures table records each rejected record. The failures table records the rejected records and the reason for each. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The ingestion failures table records each rejected record.
- **B:** Correct. The failures table records the rejected records and the reason for each. In this case: The ingestion failures table records each rejected record.
- **C:** Incorrect for this question. The runtime metrics show whether the source or the destination is blocking. Why the correct answer wins: The ingestion failures table records each rejected record.
- **D:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The ingestion failures table records each rejected record.

### Question 69 — D

Answer: Inspect the eventstream runtime metrics. The runtime metrics show which side is limiting. The runtime metrics show whether the source or the destination is blocking. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The failures table records the rejected records and the reason for each. Why the correct answer wins: The runtime metrics show which side is limiting.
- **B:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The runtime metrics show which side is limiting.
- **C:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The runtime metrics show which side is limiting.
- **D:** Correct. The runtime metrics show whether the source or the destination is blocking. In this case: The runtime metrics show which side is limiting.

### Question 70 — A

Answer: Check the shortcut connection and the delegated permission. The delegated permission behind the shortcut differs by identity. A shortcut fails for a connection or permission reason more often than for a data reason. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. A shortcut fails for a connection or permission reason more often than for a data reason. In this case: The delegated permission behind the shortcut differs by identity.
- **B:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The delegated permission behind the shortcut differs by identity.
- **C:** Incorrect for this question. The message names the object or the conversion; the plan explains the cost. Why the correct answer wins: The delegated permission behind the shortcut differs by identity.
- **D:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The delegated permission behind the shortcut differs by identity.

### Question 71 — C, D

Answers: Read the T-SQL error message and then the query plan; Check the shortcut connection and the delegated permission. The T-SQL message names the failing object, and the shortcut needs its permission checked. The message names the object or the conversion; the plan explains the cost. A shortcut fails for a connection or permission reason more often than for a data reason. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The T-SQL message names the failing object, and the shortcut needs its permission checked.
- **B:** Incorrect for this question. The failures table records the rejected records and the reason for each. Why the correct answer wins: The T-SQL message names the failing object, and the shortcut needs its permission checked.
- **C:** Correct. A shortcut fails for a connection or permission reason more often than for a data reason. In this case: The T-SQL message names the failing object, and the shortcut needs its permission checked.
- **D:** Correct. The message names the object or the conversion; the plan explains the cost. In this case: The T-SQL message names the failing object, and the shortcut needs its permission checked.
- **E:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The T-SQL message names the failing object, and the shortcut needs its permission checked.

### Question 72 — C

Answer: Run VACUUM to remove the files the table no longer references. VACUUM removes the files the table no longer references. VACUUM reclaims the storage that deleted versions still hold. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. V-Order writes the files in a layout the Fabric engines read faster. Why the correct answer wins: VACUUM removes the files the table no longer references.
- **B:** Incorrect for this question. OPTIMIZE rewrites many small files into fewer larger ones. Why the correct answer wins: VACUUM removes the files the table no longer references.
- **C:** Correct. VACUUM reclaims the storage that deleted versions still hold. In this case: VACUUM removes the files the table no longer references.
- **D:** Incorrect for this question. A partition on the filter column lets the engine skip the rows it does not need. Why the correct answer wins: VACUUM removes the files the table no longer references.

### Question 73 — B

Answer: Apply Z-Order on the frequently filtered columns. Z-Order clusters the values so the filtered read touches fewer files. Z-Order clusters related values so a filtered read touches fewer files. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. A partition on the filter column lets the engine skip the rows it does not need. Why the correct answer wins: Z-Order clusters the values so the filtered read touches fewer files.
- **B:** Correct. Z-Order clusters related values so a filtered read touches fewer files. In this case: Z-Order clusters the values so the filtered read touches fewer files.
- **C:** Incorrect for this question. V-Order writes the files in a layout the Fabric engines read faster. Why the correct answer wins: Z-Order clusters the values so the filtered read touches fewer files.
- **D:** Incorrect for this question. OPTIMIZE rewrites many small files into fewer larger ones. Why the correct answer wins: Z-Order clusters the values so the filtered read touches fewer files.

### Question 74 — A

Answer: Use liquid clustering instead of a fixed partition column. Liquid clustering adapts to the query pattern. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. In this case: Liquid clustering adapts to the query pattern.
- **B:** Incorrect for this question. A partition on the filter column lets the engine skip the rows it does not need. Why the correct answer wins: Liquid clustering adapts to the query pattern.
- **C:** Incorrect for this question. OPTIMIZE rewrites many small files into fewer larger ones. Why the correct answer wins: Liquid clustering adapts to the query pattern.
- **D:** Incorrect for this question. Z-Order clusters related values so a filtered read touches fewer files. Why the correct answer wins: Liquid clustering adapts to the query pattern.

### Question 75 — C

Answer: Raise the parallelism of the copy so independent slices move together. Raising the parallelism moves the independent slices together. Independent slices that run one after another waste the capacity the run already has. Local study-map skill 3.9 (Optimizing Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Coalesce reduces the file count without a full shuffle. Why the correct answer wins: Raising the parallelism moves the independent slices together.
- **B:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: Raising the parallelism moves the independent slices together.
- **C:** Correct. Independent slices that run one after another waste the capacity the run already has. In this case: Raising the parallelism moves the independent slices together.
- **D:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Raising the parallelism moves the independent slices together.

### Question 76 — B, C

Answers: Raise the parallelism of the copy so independent slices move together; Coalesce the partitions before writing the small result. More parallelism moves them together, and coalesce reduces the file count. Independent slices that run one after another waste the capacity the run already has. Coalesce reduces the file count without a full shuffle. Local study-map skill 3.9 (Optimizing Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: More parallelism moves them together, and coalesce reduces the file count.
- **B:** Correct. Coalesce reduces the file count without a full shuffle. In this case: More parallelism moves them together, and coalesce reduces the file count.
- **C:** Correct. Independent slices that run one after another waste the capacity the run already has. In this case: More parallelism moves them together, and coalesce reduces the file count.
- **D:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: More parallelism moves them together, and coalesce reduces the file count.
- **E:** Incorrect for this question. Too few partitions leave large tasks; too many add scheduling overhead. Why the correct answer wins: More parallelism moves them together, and coalesce reduces the file count.

### Question 77 — C

Answer: Write fewer, larger files into the warehouse table. Fewer, larger files cost less to scan. Many small files cost more to scan than the same rows in fewer files. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Fewer, larger files cost less to scan.
- **B:** Incorrect for this question. The warehouse optimizer plans from statistics, not from the data itself. Why the correct answer wins: Fewer, larger files cost less to scan.
- **C:** Correct. Many small files cost more to scan than the same rows in fewer files. In this case: Fewer, larger files cost less to scan.
- **D:** Incorrect for this question. A join on a different column forces a shuffle of both sides. Why the correct answer wins: Fewer, larger files cost less to scan.

### Question 78 — B

Answer: Insert the warehouse rows in batches rather than one at a time. Batched inserts stop paying the transaction overhead per row. Row-by-row inserts pay the transaction overhead once per row. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The warehouse optimizer plans from statistics, not from the data itself. Why the correct answer wins: Batched inserts stop paying the transaction overhead per row.
- **B:** Correct. Row-by-row inserts pay the transaction overhead once per row. In this case: Batched inserts stop paying the transaction overhead per row.
- **C:** Incorrect for this question. Many small files cost more to scan than the same rows in fewer files. Why the correct answer wins: Batched inserts stop paying the transaction overhead per row.
- **D:** Incorrect for this question. A join on a different column forces a shuffle of both sides. Why the correct answer wins: Batched inserts stop paying the transaction overhead per row.

### Question 79 — A, B

Answers: Write fewer, larger files into the warehouse table; Insert the warehouse rows in batches rather than one at a time. Batching the writes cuts the load time, and the file count cuts the read time. Many small files cost more to scan than the same rows in fewer files. Row-by-row inserts pay the transaction overhead once per row. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. Row-by-row inserts pay the transaction overhead once per row. In this case: Batching the writes cuts the load time, and the file count cuts the read time.
- **B:** Correct. Many small files cost more to scan than the same rows in fewer files. In this case: Batching the writes cuts the load time, and the file count cuts the read time.
- **C:** Incorrect for this question. The warehouse optimizer plans from statistics, not from the data itself. Why the correct answer wins: Batching the writes cuts the load time, and the file count cuts the read time.
- **D:** Incorrect for this question. A join on a different column forces a shuffle of both sides. Why the correct answer wins: Batching the writes cuts the load time, and the file count cuts the read time.
- **E:** Incorrect for this question. Coalesce reduces the file count without a full shuffle. Why the correct answer wins: Batching the writes cuts the load time, and the file count cuts the read time.

### Question 80 — A

Answer: Raise the broadcast threshold for the small table. A threshold below the table size silently disables the broadcast. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. In this case: A threshold below the table size silently disables the broadcast.
- **B:** Incorrect for this question. Adaptive execution re-plans from the actual partition sizes at run time. Why the correct answer wins: A threshold below the table size silently disables the broadcast.
- **C:** Incorrect for this question. Skew handling splits the oversized partition instead of leaving one task to finish alone. Why the correct answer wins: A threshold below the table size silently disables the broadcast.
- **D:** Incorrect for this question. Broadcasting removes the shuffle of the large side of the join. Why the correct answer wins: A threshold below the table size silently disables the broadcast.

### Question 81 — C

Answer: Salt the skewed key so the partitions even out. Salting spreads the hot key across partitions. Salting spreads one hot key across several partitions. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Broadcasting removes the shuffle of the large side of the join. Why the correct answer wins: Salting spreads the hot key across partitions.
- **B:** Incorrect for this question. Adaptive execution re-plans from the actual partition sizes at run time. Why the correct answer wins: Salting spreads the hot key across partitions.
- **C:** Correct. Salting spreads one hot key across several partitions. In this case: Salting spreads the hot key across partitions.
- **D:** Incorrect for this question. Skew handling splits the oversized partition instead of leaving one task to finish alone. Why the correct answer wins: Salting spreads the hot key across partitions.

### Question 82 — A

Answer: Repartition before the write to control the file count. Repartitioning decides how many files the write produces. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. In this case: Repartitioning decides how many files the write produces.
- **B:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: Repartitioning decides how many files the write produces.
- **C:** Incorrect for this question. Coalesce reduces the file count without a full shuffle. Why the correct answer wins: Repartitioning decides how many files the write produces.
- **D:** Incorrect for this question. Too few partitions leave large tasks; too many add scheduling overhead. Why the correct answer wins: Repartitioning decides how many files the write produces.

### Question 83 — B

Answer: Enable capacity smoothing so a burst can borrow from the burst allowance. Smoothing lets a short burst use the burst allowance. Smoothing lets a short burst use the capacity allowance instead of being throttled. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: Smoothing lets a short burst use the burst allowance.
- **B:** Correct. Smoothing lets a short burst use the capacity allowance instead of being throttled. In this case: Smoothing lets a short burst use the burst allowance.
- **C:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: Smoothing lets a short burst use the burst allowance.
- **D:** Incorrect for this question. The destination throughput caps how much the eventstream can deliver. Why the correct answer wins: Smoothing lets a short burst use the burst allowance.

### Question 84 — A

Answer: Move the workspace to a larger capacity. Capacity units are the ceiling on everything the workspace runs. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. In this case: Capacity units are the ceiling on everything the workspace runs.
- **B:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.
- **C:** Incorrect for this question. Smoothing lets a short burst use the capacity allowance instead of being throttled. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.
- **D:** Incorrect for this question. Query throughput is bounded by the eventhouse capacity. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.

### Question 85 — B, C

Answers: Set the retention policy to match the query window; Increase the eventhouse capacity so the queries keep up. Retention matches the query window, and the capacity supports the concurrency. Retention beyond the query window pays for data nobody reads. Query throughput is bounded by the eventhouse capacity. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The destination throughput caps how much the eventstream can deliver. Why the correct answer wins: Retention matches the query window, and the capacity supports the concurrency.
- **B:** Correct. Query throughput is bounded by the eventhouse capacity. In this case: Retention matches the query window, and the capacity supports the concurrency.
- **C:** Correct. Retention beyond the query window pays for data nobody reads. In this case: Retention matches the query window, and the capacity supports the concurrency.
- **D:** Incorrect for this question. The caching policy keeps the hot window on fast storage. Why the correct answer wins: Retention matches the query window, and the capacity supports the concurrency.
- **E:** Incorrect for this question. Smoothing lets a short burst use the capacity allowance instead of being throttled. Why the correct answer wins: Retention matches the query window, and the capacity supports the concurrency.

### Question 86 — C

Answer: Enable the monitoring output → build the dashboard over it → set the alert threshold → review the alert history each week. The output exists before anything is charted or alerted. There is nothing to chart or alert on until the output exists, and the review is what keeps the threshold honest. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. There is no alert history before the alert exists. Why the correct answer wins: The output exists before anything is charted or alerted.
- **B:** Incorrect for this question. The dashboard and the threshold both read an output that does not exist yet. Why the correct answer wins: The output exists before anything is charted or alerted.
- **C:** Correct. There is nothing to chart or alert on until the output exists, and the review is what keeps the threshold honest. In this case: The output exists before anything is charted or alerted.
- **D:** Incorrect for this question. A threshold with no output behind it cannot be evaluated. Why the correct answer wins: The output exists before anything is charted or alerted.

### Question 87 — A

Answer: Read the run history → isolate the failing activity → reproduce it with the same input → rerun only the failed activity. The failure is located before anything is rerun. The history identifies the failure, the input reproduces it, and the rerun is scoped to what failed. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The history identifies the failure, the input reproduces it, and the rerun is scoped to what failed. In this case: The failure is located before anything is rerun.
- **B:** Incorrect for this question. The failing activity has to be known before its input can be reproduced. Why the correct answer wins: The failure is located before anything is rerun.
- **C:** Incorrect for this question. Rerunning before reading the history repeats the failure without explaining it. Why the correct answer wins: The failure is located before anything is rerun.
- **D:** Incorrect for this question. The rerun happens before the cause is reproduced, so the second failure looks like a new one. Why the correct answer wins: The failure is located before anything is rerun.

### Question 88 — D

Answer: Read the query plan → reduce the file count → optimize and Z-Order the table → re-measure the query. The plan decides the action and the second run measures it. The plan identifies the cost, compaction and clustering address it, and the measurement proves the effect. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The plan is what should have decided whether compaction was the right fix at all. Why the correct answer wins: The plan decides the action and the second run measures it.
- **B:** Incorrect for this question. Measuring before the change and again after it is what makes the comparison possible. Why the correct answer wins: The plan decides the action and the second run measures it.
- **C:** Incorrect for this question. Optimizing before reading the plan optimizes whatever seemed slow rather than what was costly. Why the correct answer wins: The plan decides the action and the second run measures it.
- **D:** Correct. The plan identifies the cost, compaction and clustering address it, and the measurement proves the effect. In this case: The plan decides the action and the second run measures it.

### Question 89 — B

Answer: Set the default environment at the workspace level. A workspace default environment gives the notebook the approved libraries. A workspace default environment means a new notebook inherits the approved libraries without a decision. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace Spark pool applies one node size and autoscale bound to every notebook that does not override it. Why the correct answer wins: A workspace default environment gives the notebook the approved libraries.
- **B:** Correct. A workspace default environment means a new notebook inherits the approved libraries without a decision. In this case: A workspace default environment gives the notebook the approved libraries.
- **C:** Incorrect for this question. High concurrency lets several notebooks share one Spark session instead of starting a session each. Why the correct answer wins: A workspace default environment gives the notebook the approved libraries.
- **D:** Incorrect for this question. The node family sets the memory-to-core ratio, and the node count sets the parallelism ceiling. Why the correct answer wins: A workspace default environment gives the notebook the approved libraries.

### Question 90 — A

Answer: Add deployment rules so the target stage keeps its own connection and parameters. A deployment rule preserves the target stage's connection. A rule stops a promotion from overwriting the target stage environment-specific settings. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A rule stops a promotion from overwriting the target stage environment-specific settings. In this case: A deployment rule preserves the target stage's connection.
- **B:** Incorrect for this question. The pipeline promotes the same item definitions through the stages instead of rebuilding them. Why the correct answer wins: A deployment rule preserves the target stage's connection.
- **C:** Incorrect for this question. The comparison shows what the promotion will change in the target before it happens. Why the correct answer wins: A deployment rule preserves the target stage's connection.
- **D:** Incorrect for this question. A backward deployment is the supported way to restore a previous stage state. Why the correct answer wins: A deployment rule preserves the target stage's connection.

### Question 91 — B

Answer: Connect the workspace to a Git repository and commit the item definitions. Connecting the workspace to Git puts every change through review. Git keeps a reviewable history of every item definition instead of an untracked live workspace. Local study-map skill 1.4 (Version Control and Database Projects), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Committing build output makes every run look like a change. Why the correct answer wins: Connecting the workspace to Git puts every change through review.
- **B:** Correct. Git keeps a reviewable history of every item definition instead of an untracked live workspace. In this case: Connecting the workspace to Git puts every change through review.
- **C:** Incorrect for this question. An unresolved conflict blocks the update and leaves the workspace and the branch out of step. Why the correct answer wins: Connecting the workspace to Git puts every change through review.
- **D:** Incorrect for this question. Branching keeps unfinished work out of the shared workspace and makes the change reviewable. Why the correct answer wins: Connecting the workspace to Git puts every change through review.

### Question 92 — D

Answer: Build a type 2 dimension with validity dates and a current flag. A type 2 dimension preserves the attribute history. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. Local study-map skill 2.2 (Dimensional Model Preparation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A surrogate key decouples the warehouse from the source system identifiers. Why the correct answer wins: A type 2 dimension preserves the attribute history.
- **B:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: A type 2 dimension preserves the attribute history.
- **C:** Incorrect for this question. A star schema keeps the fact table narrow and the dimensions reusable. Why the correct answer wins: A type 2 dimension preserves the attribute history.
- **D:** Correct. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. In this case: A type 2 dimension preserves the attribute history.

### Question 93 — A

Answer: Generate a surrogate key instead of reusing the source key. A surrogate key gives one stable key for the reconciled row. A surrogate key decouples the warehouse from the source system identifiers. Local study-map skill 2.2 (Dimensional Model Preparation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. A surrogate key decouples the warehouse from the source system identifiers. In this case: A surrogate key gives one stable key for the reconciled row.
- **B:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: A surrogate key gives one stable key for the reconciled row.
- **C:** Incorrect for this question. A star schema keeps the fact table narrow and the dimensions reusable. Why the correct answer wins: A surrogate key gives one stable key for the reconciled row.
- **D:** Incorrect for this question. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. Why the correct answer wins: A surrogate key gives one stable key for the reconciled row.

### Question 94 — A

Answer: Merge the incoming rows into the target on the business key. A merge updates the existing row in place. A merge updates the existing row and inserts the new one in the same step. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. A merge updates the existing row and inserts the new one in the same step. In this case: A merge updates the existing row in place.
- **B:** Incorrect for this question. The control table is what lets the next run know where this one stopped. Why the correct answer wins: A merge updates the existing row in place.
- **C:** Incorrect for this question. An incremental load moves the delta instead of the history. Why the correct answer wins: A merge updates the existing row in place.
- **D:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: A merge updates the existing row in place.

### Question 95 — C

Answer: Inspect the failing cell output and exit value. The failing cell's output reports the exception. The cell output is where the exception is reported with its stack. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The Spark UI shows the stages and tasks where the time went. Why the correct answer wins: The failing cell's output reports the exception.
- **B:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The failing cell's output reports the exception.
- **C:** Correct. The cell output is where the exception is reported with its stack. In this case: The failing cell's output reports the exception.
- **D:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The failing cell's output reports the exception.

### Question 96 — D

Answer: Set the retention policy to match the query window. Retention should match the query window. Retention beyond the query window pays for data nobody reads. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: Retention should match the query window.
- **B:** Incorrect for this question. The caching policy keeps the hot window on fast storage. Why the correct answer wins: Retention should match the query window.
- **C:** Incorrect for this question. Query throughput is bounded by the eventhouse capacity. Why the correct answer wins: Retention should match the query window.
- **D:** Correct. Retention beyond the query window pays for data nobody reads. In this case: Retention should match the query window.

### Question 97 — D

Answer: Configure an alert on the failing condition. An alert fires on the condition the business cares about. An alert turns a silent failure into a notification. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. An activator rule evaluates the stream and fires when the condition holds. Why the correct answer wins: An alert fires on the condition the business cares about.
- **B:** Incorrect for this question. Waiting for the retries stops a transient failure being reported as an outage. Why the correct answer wins: An alert fires on the condition the business cares about.
- **C:** Incorrect for this question. The alert must reach the owner, or it becomes noise nobody acts on. Why the correct answer wins: An alert fires on the condition the business cares about.
- **D:** Correct. An alert turns a silent failure into a notification. In this case: An alert fires on the condition the business cares about.

### Question 98 — D

Answer: Apply the sensitivity label to the item. The sensitivity label travels with the item and its copies. The label travels with the item and drives the protection downstream consumers inherit. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Certification tells consumers the item has been reviewed as authoritative. Why the correct answer wins: The sensitivity label travels with the item and its copies.
- **B:** Incorrect for this question. Promotion signals readiness without the review that certification implies. Why the correct answer wins: The sensitivity label travels with the item and its copies.
- **C:** Incorrect for this question. Inheritance keeps one classification instead of a second opinion on the same data. Why the correct answer wins: The sensitivity label travels with the item and its copies.
- **D:** Correct. The label travels with the item and drives the protection downstream consumers inherit. In this case: The sensitivity label travels with the item and its copies.

### Question 99 — C

Answer: Define a row-level security policy on the table. Row-level security filters the rows per identity. Row-level security filters rows per identity, so one table returns different rows to different users. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The predicate must resolve the identity to the region, or every user sees the same rows. Why the correct answer wins: Row-level security filters the rows per identity.
- **B:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: Row-level security filters the rows per identity.
- **C:** Correct. Row-level security filters rows per identity, so one table returns different rows to different users. In this case: Row-level security filters the rows per identity.
- **D:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: Row-level security filters the rows per identity.

### Question 100 — B

Answer: Read the Fabric audit log in the Microsoft Purview portal. The audit log records access with the identity and the timestamp. The audit log records who did what to which item and when. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Filtering turns a very large log into the events that answer the question. Why the correct answer wins: The audit log records access with the identity and the timestamp.
- **B:** Correct. The audit log records who did what to which item and when. In this case: The audit log records access with the identity and the timestamp.
- **C:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The audit log records access with the identity and the timestamp.
- **D:** Incorrect for this question. The audit log has a retention window, so an investigation that starts late needs the export. Why the correct answer wins: The audit log records access with the identity and the timestamp.
