# Microsoft DP-700 — Full-Length Mock Exam 6

Fabric Data Engineer Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, interactive components in the Fabric portal, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A new notebook always starts with the libraries the platform team approved. What should be configured?

Domain: Implement and manage an analytics solution

- A. Attach a custom Spark environment to the notebook
- B. Enable high concurrency mode for shared sessions
- C. Set the default environment at the workspace level
- D. Set a workspace-level custom Spark pool for the notebooks

### 2. A notebook that joins two large tables spills to disk in every stage. What should change?

Domain: Implement and manage an analytics solution

- A. Set a workspace-level custom Spark pool for the notebooks
- B. Enable dynamic allocation so idle executors are released during the run
- C. Size the pool for the node family and node count the workload needs
- D. Enable autoscale with a minimum and maximum node count

### 3. A job keeps forty executors for an hour of stages that need six. What should be enabled?

Domain: Implement and manage an analytics solution

- A. Set a workspace-level custom Spark pool for the notebooks
- B. Enable dynamic allocation so idle executors are released during the run
- C. Enable high concurrency mode for shared sessions
- D. Enable autoscale with a minimum and maximum node count

### 4. One curated table must be readable by the warehouse, the endpoint, and a notebook. What must stay enabled?

Domain: Implement and manage an analytics solution

- A. Keep OneLake availability enabled so other engines can read the same data
- B. Create the workspace in the required region at creation time
- C. Assign the workspace to a capacity that has headroom
- D. Assign the workspace to the domain that owns the subject area

### 5. A subsidiary's data may not cross a border and the workspace already exists. What should have been decided first?

Domain: Implement and manage an analytics solution

- A. Keep OneLake availability enabled so other engines can read the same data
- B. Create the workspace in the required region at creation time
- C. Assign the workspace to the domain that owns the subject area
- D. Assign the workspace to a capacity that has headroom

### 6. A vendor keeps its orchestration as a Python DAG that must run inside Fabric. What should be used?

Domain: Implement and manage an analytics solution

- A. Sync the Airflow DAG from the connected Git repository
- B. Enable the Apache Airflow job in the workspace and author the DAG
- C. Rewrite the existing orchestration as a Fabric pipeline instead
- D. Use a pipeline for the copy and the orchestration

### 7. Every item change must be attributable and reversible. What should be configured?

Domain: Implement and manage an analytics solution

- A. Connect the workspace to a Git repository and commit the item definitions
- B. Add the generated artefacts to the ignore file rather than committing them
- C. Work in a feature branch and merge through a pull request
- D. Resolve the conflict by choosing the definition that must win, then commit

### 8. A database project fails in one environment because the server name is embedded. What should be used?

Domain: Implement and manage an analytics solution

- A. Work in a feature branch and merge through a pull request
- B. Create a database project and deploy the schema from it
- C. Use SQLCMD variables for the environment-specific values
- D. Build the project into a DACPAC and deploy that artefact

### 9. A group wants the same items to reach development, test, and production in order. What should be created?

Domain: Implement and manage an analytics solution

- A. Select only the items that belong in the target stage
- B. Compare the stages before promoting
- C. Add deployment rules so the target stage keeps its own connection and parameters
- D. Create a deployment pipeline with development, test, and production stages

### 10. An approver must see what a promotion changes before signing it. What should be used?

Domain: Implement and manage an analytics solution

- A. Add deployment rules so the target stage keeps its own connection and parameters
- B. Deploy backwards to recover the last known-good definition
- C. Create a deployment pipeline with development, test, and production stages
- D. Compare the stages before promoting

### 11. A platform owner must manage access and settings for a shared workspace. What should be granted?

Domain: Implement and manage an analytics solution

- A. Grant Admin on the workspace to the platform team
- B. Share the single item with the user who needs only that item
- C. Grant Viewer on the workspace
- D. Grant the user a workspace role

### 12. An external auditor must read one table and nothing else. What should be granted?

Domain: Implement and manage an analytics solution

- A. Grant the user a workspace role
- B. Grant Viewer on the workspace
- C. Grant Read on the item
- D. Share the single item with the user who needs only that item

### 13. A supplier may see only their own orders in a shared fact table. What should be defined?

Domain: Implement and manage an analytics solution

- A. Define a row-level security policy on the table
- B. Apply column-level security so the column is hidden from the group
- C. Apply object-level security in the semantic model
- D. Filter the table through a predicate that resolves the user to a region

### 14. A net-margin column must be hidden from the supplier role while the row stays readable. What should be applied?

Domain: Implement and manage an analytics solution

- A. Grant access at the folder that holds the restricted files
- B. Define a row-level security policy on the table
- C. Apply column-level security so the column is hidden from the group
- D. Apply object-level security in the semantic model

### 15. A whole table must not exist for the supplier role in the semantic model. What should be applied?

Domain: Implement and manage an analytics solution

- A. Apply object-level security in the semantic model
- B. Apply column-level security so the column is hidden from the group
- C. Define a row-level security policy on the table
- D. Grant access at the folder that holds the restricted files

### 16. Contact details must remain queryable while most staff see a masked value. What should be applied?

Domain: Implement and manage an analytics solution

- A. Expose a view with the column omitted instead of masking it
- B. Mask the column in the report layer only
- C. Apply dynamic data masking to the column
- D. Exempt the authorised group from the mask

### 17. Contact details must be masked except for the support team. Which two settings apply? Select two.

Domain: Implement and manage an analytics solution

- A. Apply column-level security so the column is hidden from the group
- B. Expose a view with the column omitted instead of masking it
- C. Exempt the authorised group from the mask
- D. Mask the column in the report layer only
- E. Apply dynamic data masking to the column

### 18. A customer extract must carry a classification that follows every copy. What should be applied?

Domain: Implement and manage an analytics solution

- A. Certify the item as the approved source
- B. Let the label inherit from the labelled source file
- C. Apply the sensitivity label to the item
- D. Set the default sensitivity label for the workspace

### 19. Consumers need to know which items are approved and new items must be classified. Which two practices apply? Select two.

Domain: Implement and manage an analytics solution

- A. Promote the item as ready for reuse
- B. Set the default sensitivity label for the workspace
- C. Certify the item as the approved source
- D. Let the label inherit from the labelled source file
- E. Apply the sensitivity label to the item

### 20. A regulator asks which engineer read the pricing table. Where is that recorded?

Domain: Implement and manage an analytics solution

- A. Read the item activity log
- B. Filter the audit log by activity and by item
- C. Read the Fabric audit log in the Microsoft Purview portal
- D. Export the audit events before the retention window closes

### 21. An access event must be found and preserved past the retention window. Which two steps apply? Select two.

Domain: Implement and manage an analytics solution

- A. Filter the audit log by activity and by item
- B. Export the audit events before the retention window closes
- C. Read the Fabric audit log in the Microsoft Purview portal
- D. Read the item activity log
- E. Read the refresh history for the semantic model

### 22. A pricing folder must be closed even to workspace Contributors. What should be configured?

Domain: Implement and manage an analytics solution

- A. Grant the OneLake role to a security group rather than to individuals
- B. Grant access at the folder that holds the restricted files
- C. Configure OneLake security roles for the lakehouse
- D. Scope the OneLake role to the folder that holds the restricted table

### 23. Data access must be governed outside the workspace role and maintained once. Which two settings apply? Select two.

Domain: Implement and manage an analytics solution

- A. Grant the OneLake role to a security group rather than to individuals
- B. Scope the OneLake role to the folder that holds the restricted table
- C. Grant access at the folder that holds the restricted files
- D. Configure OneLake security roles for the lakehouse
- E. Grant the user a workspace role

### 24. A network team needs a window filter over data already in an eventhouse. What should be used?

Domain: Implement and manage an analytics solution

- A. Use a T-SQL script against the warehouse
- B. Use a KQL query against the eventhouse
- C. Use a Dataflow Gen2 for the transformation
- D. Use a notebook for the transformation

### 25. A marketing analyst must maintain the transformation without writing code. What should be used?

Domain: Implement and manage an analytics solution

- A. Use a T-SQL script against the warehouse
- B. Use a pipeline for the copy and the orchestration
- C. Use a notebook for the transformation
- D. Use a Dataflow Gen2 for the transformation

### 26. One run must copy an archive and then apply PySpark. Which two items apply? Select two.

Domain: Implement and manage an analytics solution

- A. Use a KQL query against the eventhouse
- B. Use a T-SQL script against the warehouse
- C. Use a Dataflow Gen2 for the transformation
- D. Use a notebook for the transformation
- E. Use a pipeline for the copy and the orchestration

### 27. The run must read the stored last-load timestamp before it copies anything. What should be used?

Domain: Implement and manage an analytics solution

- A. Look up the stored watermark before the copy
- B. Build the path with a dynamic expression at run time
- C. Pass the folder path as a pipeline parameter
- D. Set the value in a pipeline variable and reference the variable

### 28. A feed arrives at no fixed hour and each feed writes its own folder. Which two features apply? Select two.

Domain: Implement and manage an analytics solution

- A. Trigger on the file-created event for the landing folder
- B. Add an event-based trigger so the run starts when the file arrives
- C. Add a schedule trigger with the cadence and time zone the business expects
- D. Pass the folder path as a pipeline parameter
- E. Use an Until loop with a timeout for the long-running check

### 29. A shared platform must protect supplier data from its first release. Which sequence is correct?

Domain: Implement and manage an analytics solution

- A. Add row-level security → grant the workspace role → classify the data → apply the label → test as each persona
- B. Classify the data → apply the sensitivity label → grant the workspace role → add row-level security → test as each persona
- C. Grant the workspace role → classify the data → test as each persona → apply the label → add row-level security
- D. Test as each persona → add row-level security → apply the label → classify the data → grant the role

### 30. An item must become the approved pricing source with evidence. Which sequence is correct?

Domain: Implement and manage an analytics solution

- A. Verify the audit entry → endorse the item → confirm the source of truth → apply the label
- B. Confirm the source of truth → apply the label → endorse the item → verify the audit entry
- C. Endorse the item → apply the label → confirm the source of truth → verify the audit entry
- D. Apply the label → verify the audit entry → endorse the item → confirm the source of truth

### 31. A sixty-million-row fact gains an hour of data every night. What should be used?

Domain: Ingest and transform data

- A. Merge the incoming rows into the target on the business key
- B. Load only the rows newer than the stored watermark
- C. Run a full load and overwrite the target
- D. Route the failed rows to a reject table and continue the load

### 32. A resumed load must restart at the row after the last success. What should be stored?

Domain: Ingest and transform data

- A. Look up the stored watermark before the copy
- B. Reprocess the affected partitions when the data arrives late
- C. Store the last successful load timestamp in a control table
- D. Load only the rows newer than the stored watermark

### 33. A supplier is renumbered in the ERP and must not look like a new supplier. What should the warehouse key on?

Domain: Ingest and transform data

- A. Deduplicate on the business key and keep the latest record
- B. Merge the incoming rows into the target on the business key
- C. Build a type 2 dimension with validity dates and a current flag
- D. Generate a surrogate key instead of reusing the source key

### 34. A price change in March must not rewrite January revenue. What should be built?

Domain: Ingest and transform data

- A. Build a type 2 dimension with validity dates and a current flag
- B. Generate a surrogate key instead of reusing the source key
- C. Model the data as a star schema with conformed dimensions
- D. Merge the incoming rows into the target on the business key

### 35. A streaming load restarts after a failure and repeats an hour of rows. What is missing?

Domain: Ingest and transform data

- A. Query the stream through a OneLake shortcut
- B. Store the stream in native tables in the eventhouse
- C. Set a checkpoint location for the streaming query
- D. Set a watermark so late events are handled deterministically

### 36. A stream must resume without duplicates and close windows deterministically. Which two settings apply? Select two.

Domain: Ingest and transform data

- A. Store the stream in native tables in the eventhouse
- B. Query the stream through a OneLake shortcut
- C. Process the stream with an eventstream
- D. Set a watermark so late events are handled deterministically
- E. Set a checkpoint location for the streaming query

### 37. A monthly close needs multi-table transactions and a relational model. What should hold the data?

Domain: Ingest and transform data

- A. Load the curated model into the warehouse
- B. Land the extract in the lakehouse Files area
- C. Store the telemetry in an eventhouse KQL database
- D. Create a KQL database for the time-series queries

### 38. Network events must be queried by time range within seconds of arrival. Where should they land?

Domain: Ingest and transform data

- A. Land the extract in the lakehouse Files area
- B. Load the curated model into the warehouse
- C. Store the telemetry in an eventhouse KQL database
- D. Query the lakehouse through its SQL analytics endpoint

### 39. The monthly close is a set-based update over warehouse tables. What should be used?

Domain: Ingest and transform data

- A. Transform with Dataflow Gen2 and Power Query
- B. Transform with KQL in the eventhouse
- C. Transform with PySpark in a notebook
- D. Transform with T-SQL against the warehouse

### 40. Telemetry must be reduced to a per-tower average as it arrives. What should be used?

Domain: Ingest and transform data

- A. Transform with KQL in the eventhouse
- B. Transform with Dataflow Gen2 and Power Query
- C. Transform with PySpark in a notebook
- D. Transform with T-SQL against the warehouse

### 41. A partner writes parquet into a container the company owns. How should it appear in OneLake?

Domain: Ingest and transform data

- A. Copy the remote data into a local table instead of shortcutting it
- B. Copy the files as binary and parse them downstream
- C. Create an ADLS Gen2 shortcut to the external container
- D. Create an internal OneLake shortcut to the other lakehouse table

### 42. Two teams must read authoritative data without a second copy. Which two practices apply? Select two.

Domain: Ingest and transform data

- A. Copy the remote data into a local table instead of shortcutting it
- B. Use a Copy activity in the pipeline
- C. Create a shortcut rather than a copy when the source stays authoritative
- D. Create an internal OneLake shortcut to the other lakehouse table
- E. Create an ADLS Gen2 shortcut to the external container

### 43. An order system must appear in Fabric within seconds and no schedule exists. What should be enabled?

Domain: Ingest and transform data

- A. Create an internal OneLake shortcut to the other lakehouse table
- B. Enable mirroring for the operational database
- C. Use a Copy activity in the pipeline
- D. Run a full load and overwrite the target

### 44. A nightly file must be moved and then transformed in one ordered run. What should be used?

Domain: Ingest and transform data

- A. Copy the files as binary and parse them downstream
- B. Use a Copy activity in the pipeline
- C. Append the new files instead of overwriting the target
- D. Use Get Metadata to list the files to process

### 45. A landing folder holds an unknown number of vendor files each night. What should be used?

Domain: Ingest and transform data

- A. Copy the files as binary and parse them downstream
- B. Delete the processed source file after the load succeeds
- C. Iterate a ForEach activity over the returned list
- D. Use Get Metadata to list the files to process

### 46. Each order must carry its customer's previous order date on the same row. What should be used?

Domain: Ingest and transform data

- A. Use a window function to rank within the partition
- B. Pivot the rows into the reporting columns
- C. Union the sources after conforming the columns
- D. Group and aggregate to the grain the report needs

### 47. Large row-level cleansing and a per-customer ranking are both needed. Which two features apply? Select two.

Domain: Ingest and transform data

- A. Transform with Dataflow Gen2 and Power Query
- B. Transform with PySpark in a notebook
- C. Use a window function to rank within the partition
- D. Pivot the rows into the reporting columns
- E. Transform with T-SQL against the warehouse

### 48. A slowly changing dimension must be merged on its business key. What should be used?

Domain: Ingest and transform data

- A. Transform with PySpark in a notebook
- B. Transform with KQL in the eventhouse
- C. Transform with T-SQL against the warehouse
- D. Transform with Dataflow Gen2 and Power Query

### 49. A dimension needs a merge and the telemetry needs a window filter. Which two engines apply? Select two.

Domain: Ingest and transform data

- A. Transform with KQL in the eventhouse
- B. Transform with Dataflow Gen2 and Power Query
- C. Transform with PySpark in a notebook
- D. Transform with T-SQL against the warehouse
- E. Pivot the rows into the reporting columns

### 50. A board query joins the same seven tables every time. What should be done?

Domain: Ingest and transform data

- A. Pivot the rows into the reporting columns
- B. Group and aggregate to the grain the report needs
- C. Model the data as a star schema with conformed dimensions
- D. Denormalize the model so the report needs no join

### 51. A revenue report needs one column per region and one row per month. What should be used?

Domain: Ingest and transform data

- A. Group and aggregate to the grain the report needs
- B. Denormalize the model so the report needs no join
- C. Union the sources after conforming the columns
- D. Pivot the rows into the reporting columns

### 52. A store reconnects and uploads yesterday's sales after the close. What should be done?

Domain: Ingest and transform data

- A. Replace the missing value with a documented default
- B. Deduplicate on the business key and keep the latest record
- C. Route the failed rows to a reject table and continue the load
- D. Reprocess the affected partitions when the data arrives late

### 53. The stream must reuse the PySpark logic that already runs in batch. What should be used?

Domain: Ingest and transform data

- A. Process the stream with a KQL update policy
- B. Process the stream with Spark structured streaming
- C. Run a batch job every few minutes over the landing folder
- D. Process the stream with an eventstream

### 54. One stream needs a no-code path and another reuses batch PySpark. Which two engines apply? Select two.

Domain: Ingest and transform data

- A. Process the stream with a KQL update policy
- B. Set a checkpoint location for the streaming query
- C. Run a batch job every few minutes over the landing folder
- D. Process the stream with an eventstream
- E. Process the stream with Spark structured streaming

### 55. Late events arrive up to an hour after the window and must be handled deterministically. What should be set?

Domain: Ingest and transform data

- A. Store the stream in native tables in the eventhouse
- B. Set a watermark so late events are handled deterministically
- C. Query the stream through a OneLake shortcut
- D. Set a checkpoint location for the streaming query

### 56. Per-hour totals must be produced for each fixed hour. Which window fits?

Domain: Ingest and transform data

- A. Create a materialized view for the repeated aggregation
- B. Use a tumbling window for the fixed five-minute aggregate
- C. Use a sliding window that emits when the condition is met
- D. Use a hopping window when the intervals must overlap

### 57. Six tiles recompute the same hourly average. What should be created?

Domain: Ingest and transform data

- A. Use a hopping window when the intervals must overlap
- B. Create a materialized view for the repeated aggregation
- C. Use a tumbling window for the fixed five-minute aggregate
- D. Query the stream through a OneLake shortcut

### 58. The nightly fact load must become incremental. Which sequence is correct?

Domain: Ingest and transform data

- A. Read the watermark → extract only the rows after it → merge into the target → update the watermark
- B. Merge into the target → read the watermark → update the watermark → extract the rows
- C. Extract the full table → merge into the target → read the watermark → update the watermark
- D. Update the watermark → extract the rows → read the watermark → merge into the target

### 59. A published total is wrong because of duplicates and a late day. Which sequence is correct?

Domain: Ingest and transform data

- A. Detect the duplicates and the late rows → decide the surviving record → correct the affected partition → recompute the aggregate
- B. Decide the surviving record → recompute the aggregate → detect the duplicates → correct the partition
- C. Recompute the aggregate → detect the duplicates → correct the partition → decide the surviving record
- D. Correct the partition → recompute the aggregate → decide the surviving record → detect the duplicates

### 60. A live order board must be built from an event hub. Which sequence is correct?

Domain: Ingest and transform data

- A. Add the destination → create the KQL table → build the view → define the source → alert on the aggregate
- B. Create the KQL table → define the source → alert on the aggregate → add the destination → build the view
- C. Alert on the aggregate → build the materialized view → define the source → add the destination → create the KQL table
- D. Define the eventstream source → add the destination → create the KQL table → build the materialized view → alert on the aggregate

### 61. The whole nightly estate must be reviewed after a failed release. Where are the runs listed?

Domain: Monitor and optimize an analytics solution

- A. Read the item activity log
- B. Use the Monitoring hub for the run history
- C. Read the refresh history for the semantic model
- D. Send the logs to a Log Analytics workspace

### 62. One notebook's runs must be reviewed after a change. What should be read?

Domain: Monitor and optimize an analytics solution

- A. Read the item activity log
- B. Read the Fabric audit log in the Microsoft Purview portal
- C. Use the Monitoring hub for the run history
- D. Read the refresh history for the semantic model

### 63. A board refreshes late every Monday. Where is the duration recorded?

Domain: Monitor and optimize an analytics solution

- A. Read the refresh history for the semantic model
- B. Use the Monitoring hub for the run history
- C. Read the item activity log
- D. Send the logs to a Log Analytics workspace

### 64. Refresh behaviour must be triaged now and analysed after a quarter. Which two sources apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Read the refresh history for the semantic model
- B. Read the Fabric audit log in the Microsoft Purview portal
- C. Read the item activity log
- D. Use the Monitoring hub for the run history
- E. Send the logs to a Log Analytics workspace

### 65. A failed load was discovered by the sales team the next morning. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Alert on every successful run as well as every failure
- B. Send the alert to the team that owns the item
- C. Use a Data Activator rule that watches the streaming condition
- D. Configure an alert on the failing condition

### 66. A degradation must be detected from the network stream itself. What should be used?

Domain: Monitor and optimize an analytics solution

- A. Use a Data Activator rule that watches the streaming condition
- B. Build a real-time dashboard over the monitoring table
- C. Configure an alert on the failing condition
- D. Alert on every successful run as well as every failure

### 67. A source times out twice a night and succeeds on the next attempt. What should be added?

Domain: Monitor and optimize an analytics solution

- A. Add a retry policy with a delay to the failing activity
- B. Add an error branch so the failure is handled rather than ignored
- C. Set the failure dependency so the handler runs when the step fails
- D. Use an Until loop with a timeout for the long-running check

### 68. An error handler exists and never runs. What should be set?

Domain: Monitor and optimize an analytics solution

- A. Add an error branch so the failure is handled rather than ignored
- B. Use an Until loop with a timeout for the long-running check
- C. Add a retry policy with a delay to the failing activity
- D. Set the failure dependency so the handler runs when the step fails

### 69. A notebook fails on one table with no class name. Where is the stack?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Open the Spark UI for the application
- C. Check the failing cell and the Spark driver log
- D. Inspect the failing cell output and exit value

### 70. A consolidation succeeds but takes twice as long each week. What should be opened?

Domain: Monitor and optimize an analytics solution

- A. Check the failing cell and the Spark driver log
- B. Open the Spark UI for the application
- C. Send the logs to a Log Analytics workspace
- D. Inspect the failing cell output and exit value

### 71. A notebook failed once and is also slower than before. Which two views apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Open the Spark UI for the application
- B. Use the Monitoring hub for the run history
- C. Check the failing cell and the Spark driver log
- D. Send the logs to a Log Analytics workspace
- E. Inspect the failing cell output and exit value

### 72. Telemetry is rejected after a vendor changed a field. Where are the rejects listed?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Read the Fabric audit log in the Microsoft Purview portal
- C. Query the ingestion failures table in the KQL database
- D. Inspect the eventstream runtime metrics

### 73. A stream delivers less than the source during peak. What shows the constrained side?

Domain: Monitor and optimize an analytics solution

- A. Inspect the eventstream runtime metrics
- B. Use the Monitoring hub for the run history
- C. Read the refresh history for the semantic model
- D. Query the ingestion failures table in the KQL database

### 74. A stream loses throughput and some records fail validation. Which two views apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Query the ingestion failures table in the KQL database
- B. Use the Monitoring hub for the run history
- C. Read the Fabric audit log in the Microsoft Purview portal
- D. Read the refresh history for the semantic model
- E. Inspect the eventstream runtime metrics

### 75. The close procedure fails after a column rename. What identifies the object?

Domain: Monitor and optimize an analytics solution

- A. Check the failing cell and the Spark driver log
- B. Read the T-SQL error message and then the query plan
- C. Check the shortcut connection and the delegated permission
- D. Read the activity output of the failed step

### 76. A shortcut-backed table returns nothing after a source change. What should be checked?

Domain: Monitor and optimize an analytics solution

- A. Read the activity output of the failed step
- B. Check the failing cell and the Spark driver log
- C. Check the shortcut connection and the delegated permission
- D. Read the T-SQL error message and then the query plan

### 77. A stored procedure fails and a shortcut-backed view returns no rows. Which two checks apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Check the shortcut connection and the delegated permission
- B. Check the failing cell and the Spark driver log
- C. Query the ingestion failures table in the KQL database
- D. Read the T-SQL error message and then the query plan
- E. Read the activity output of the failed step

### 78. Every query filters on order date and still scans the whole table. What should be added?

Domain: Monitor and optimize an analytics solution

- A. Partition the table on the date column
- B. Run VACUUM to remove the files the table no longer references
- C. Run OPTIMIZE to compact the small files
- D. Apply Z-Order on the frequently filtered columns

### 79. Reports filter two columns that are not the partition key. What should be applied?

Domain: Monitor and optimize an analytics solution

- A. Run OPTIMIZE to compact the small files
- B. Enable V-Order on the table
- C. Partition the table on the date column
- D. Apply Z-Order on the frequently filtered columns

### 80. A copy step moves forty independent files one by one. What should be changed?

Domain: Monitor and optimize an analytics solution

- A. Insert the warehouse rows in batches rather than one at a time
- B. Coalesce the partitions before writing the small result
- C. Cache the DataFrame that is used twice
- D. Raise the parallelism of the copy so independent slices move together

### 81. The close query picks a nested loop after a large load. What should be updated?

Domain: Monitor and optimize an analytics solution

- A. Insert the warehouse rows in batches rather than one at a time
- B. Update statistics so the optimizer sees the current distribution
- C. Write fewer, larger files into the warehouse table
- D. Join on the distribution column so the rows stay on their node

### 82. A warehouse query suffers from a stale estimate and a cross-node shuffle. Which two actions apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Join on the distribution column so the rows stay on their node
- B. Update statistics so the optimizer sees the current distribution
- C. Coalesce the partitions before writing the small result
- D. Insert the warehouse rows in batches rather than one at a time
- E. Write fewer, larger files into the warehouse table

### 83. One tower sends a fifth of the events and one task never finishes. What should be applied?

Domain: Monitor and optimize an analytics solution

- A. Enable skew join handling for the hot key
- B. Broadcast the small dimension to avoid the shuffle
- C. Keep adaptive query execution enabled so the shuffle is re-planned
- D. Salt the skewed key so the partitions even out

### 84. A large fact joins a small calendar table and the shuffle dominates. What should be done?

Domain: Monitor and optimize an analytics solution

- A. Cache the DataFrame that is used twice
- B. Salt the skewed key so the partitions even out
- C. Broadcast the small dimension to avoid the shuffle
- D. Set the shuffle partition count to match the data volume

### 85. Two years are retained although dashboards read one day. What should be set?

Domain: Monitor and optimize an analytics solution

- A. Increase the eventhouse capacity so the queries keep up
- B. Set the retention policy to match the query window
- C. Set the caching policy on the KQL table
- D. Move the workspace to a larger capacity

### 86. A slow board must be improved with evidence. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Optimize the table → re-measure the query → read the plan → reduce the file count
- B. Re-measure the query → optimize the table → read the plan → reduce the file count
- C. Read the query plan → reduce the file count → optimize and Z-Order the table → re-measure the query
- D. Reduce the file count → read the plan → re-measure the query → optimize the table

### 87. A failed load must be corrected and rerun. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Reproduce the input → isolate the activity → read the run history → rerun the activity
- B. Rerun only the failed activity → read the run history → isolate the activity → reproduce the input
- C. Read the run history → isolate the failing activity → reproduce it with the same input → rerun only the failed activity
- D. Isolate the failing activity → rerun the activity → read the run history → reproduce the input

### 88. One Spark task never finishes while the others complete. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Salt the join → re-run the job → open the Spark UI → find the skewed stage
- B. Find the skewed stage → open the Spark UI → re-run the job → broadcast the join
- C. Open the Spark UI → find the stage with the skewed task → broadcast or salt the join → re-run and compare the stage time
- D. Re-run and compare the stage time → open the Spark UI → find the skewed stage → salt the join

---

## Case study — Bellows College

Bellows College has 14,000 students, six faculties, and a data platform built by a team of three. Each faculty keeps its own spreadsheet of admissions, enrolment, and results, and the registrar needs one authoritative student record. The college has adopted Fabric with a lakehouse per faculty and a shared warehouse. Student records carry personal data that only the registrar may see in full, while faculty staff may see their own students. The academic year ends with a statutory return that must reconcile exactly to the student record system, and the college cannot afford a data engineer on call overnight.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. A faculty keeps its orchestration as a Python DAG. What should be used?

Domain: Implement and manage an analytics solution

- A. Sync the Airflow DAG from the connected Git repository
- B. Use a pipeline for the copy and the orchestration
- C. Rewrite the existing orchestration as a Fabric pipeline instead
- D. Enable the Apache Airflow job in the workspace and author the DAG

### 90. A faculty may see only its own students. What should be defined?

Domain: Implement and manage an analytics solution

- A. Apply object-level security in the semantic model
- B. Define a row-level security policy on the table
- C. Apply column-level security so the column is hidden from the group
- D. Filter the table through a predicate that resolves the user to a region

### 91. Only the registrar may read the full personal identifier. What should be applied?

Domain: Implement and manage an analytics solution

- A. Expose a view with the column omitted instead of masking it
- B. Apply dynamic data masking to the column
- C. Mask the column in the report layer only
- D. Exempt the authorised group from the mask

---

## Case study — Granite Peak Outfitters

Granite Peak Outfitters sells outdoor equipment online in four countries and runs a seasonal business in which traffic triples for six weeks each year. Orders, inventory, and clickstream events all land in OneLake, and a warehouse serves the finance and merchandising teams. The data engineering team has one capacity that is sized for the quiet season. Last year the nightly load missed its window throughout the peak, and the merchandising dashboards timed out. The team wants a plan that keeps the load inside its window in the peak season without paying for a second capacity all year, and the finance team needs a monthly revenue figure that can be reproduced from the gold layer.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. The peak season triples traffic on one capacity. What should be changed first?

Domain: Monitor and optimize an analytics solution

- A. Enable capacity smoothing so a burst can borrow from the burst allowance
- B. Set the retention policy to match the query window
- C. Scale the destination throughput for the event volume
- D. Move the workspace to a larger capacity

### 93. A burst of four jobs must not be throttled. What should be enabled?

Domain: Monitor and optimize an analytics solution

- A. Enable capacity smoothing so a burst can borrow from the burst allowance
- B. Increase the eventhouse capacity so the queries keep up
- C. Set the retention policy to match the query window
- D. Move the workspace to a larger capacity

### 94. The peak load writes far more small files. What should be run?

Domain: Monitor and optimize an analytics solution

- A. Enable V-Order on the table
- B. Partition the table on the date column
- C. Run VACUUM to remove the files the table no longer references
- D. Run OPTIMIZE to compact the small files

---

## Case study — Munson Sporting Goods

Munson Sporting Goods supplies 2,600 independent sports retailers and runs its own warehouse. Orders arrive through an API, a dealer portal, and a legacy EDI feed. The data engineering team has one lakehouse, one warehouse, one eventhouse, and one capacity. The supply chain director wants a single order-status view across all three channels, the finance team wants a month-end close that reconciles to the ERP, and the operations team wants an alert when an order sits unshipped for more than a day. The team has adopted Git, deployment pipelines, and sensitivity labels, and a recent audit asked for evidence that every promotion was reviewed and that no engineer could read another team data.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. Three channels arrive as files that must be moved before transform. What should be used?

Domain: Ingest and transform data

- A. Use Get Metadata to list the files to process
- B. Append the new files instead of overwriting the target
- C. Copy the files as binary and parse them downstream
- D. Use a Copy activity in the pipeline

### 96. A channel retries and the same order appears twice. What should be applied?

Domain: Ingest and transform data

- A. Reprocess the affected partitions when the data arrives late
- B. Deduplicate on the business key and keep the latest record
- C. Route the failed rows to a reject table and continue the load
- D. Replace the missing value with a documented default

### 97. Finance needs one row per channel-day. What should be produced?

Domain: Ingest and transform data

- A. Group and aggregate to the grain the report needs
- B. Denormalize the model so the report needs no join
- C. Union the sources after conforming the columns
- D. Pivot the rows into the reporting columns

---

## Case study — Relecloud Telecom

Relecloud Telecom serves 3.8 million mobile subscribers and generates 140,000 network events per second at peak. The network operations team needs an alert within two minutes of a cell tower degradation, and the regulatory team needs call detail records retained for two years. Events arrive from three vendors with different schemas and different timestamp precisions. The company runs one eventhouse and one lakehouse on a single capacity that is already at 80 percent utilisation during peak hours. A previous attempt to store every event in the lakehouse proved too slow to query, and a previous attempt to keep everything in the eventhouse proved too expensive to retain.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. Nobody can say which pipeline failed in the peak. Where should the team look?

Domain: Monitor and optimize an analytics solution

- A. Read the refresh history for the semantic model
- B. Send the logs to a Log Analytics workspace
- C. Use the Monitoring hub for the run history
- D. Read the item activity log

### 99. A tower degradation must be flagged within two minutes. What should be used?

Domain: Monitor and optimize an analytics solution

- A. Alert on every successful run as well as every failure
- B. Send the alert to the team that owns the item
- C. Configure an alert on the failing condition
- D. Use a Data Activator rule that watches the streaming condition

### 100. Queries slow down as more towers are monitored. What should be increased?

Domain: Monitor and optimize an analytics solution

- A. Increase the eventhouse capacity so the queries keep up
- B. Move the workspace to a larger capacity
- C. Set the caching policy on the KQL table
- D. Set the retention policy to match the query window

---

## Answer key and explanations

### Question 1 — C

Answer: Set the default environment at the workspace level. A workspace default environment applies the approved libraries automatically. A workspace default environment means a new notebook inherits the approved libraries without a decision. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. An environment carries the library set and Spark properties, so every run starts from the same definition. Why the correct answer wins: A workspace default environment applies the approved libraries automatically.
- **B:** Incorrect for this question. High concurrency lets several notebooks share one Spark session instead of starting a session each. Why the correct answer wins: A workspace default environment applies the approved libraries automatically.
- **C:** Correct. A workspace default environment means a new notebook inherits the approved libraries without a decision. In this case: A workspace default environment applies the approved libraries automatically.
- **D:** Incorrect for this question. A workspace Spark pool applies one node size and autoscale bound to every notebook that does not override it. Why the correct answer wins: A workspace default environment applies the approved libraries automatically.

### Question 2 — C

Answer: Size the pool for the node family and node count the workload needs. The node family sets the memory-to-core ratio the join needs. The node family sets the memory-to-core ratio, and the node count sets the parallelism ceiling. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace Spark pool applies one node size and autoscale bound to every notebook that does not override it. Why the correct answer wins: The node family sets the memory-to-core ratio the join needs.
- **B:** Incorrect for this question. Dynamic allocation shrinks the executor set between stages, which matters when the stages are uneven. Why the correct answer wins: The node family sets the memory-to-core ratio the join needs.
- **C:** Correct. The node family sets the memory-to-core ratio, and the node count sets the parallelism ceiling. In this case: The node family sets the memory-to-core ratio the join needs.
- **D:** Incorrect for this question. Autoscale adds executors while the job runs and releases them afterwards, so idle capacity is not billed. Why the correct answer wins: The node family sets the memory-to-core ratio the join needs.

### Question 3 — B

Answer: Enable dynamic allocation so idle executors are released during the run. Dynamic allocation releases executors a stage does not need. Dynamic allocation shrinks the executor set between stages, which matters when the stages are uneven. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace Spark pool applies one node size and autoscale bound to every notebook that does not override it. Why the correct answer wins: Dynamic allocation releases executors a stage does not need.
- **B:** Correct. Dynamic allocation shrinks the executor set between stages, which matters when the stages are uneven. In this case: Dynamic allocation releases executors a stage does not need.
- **C:** Incorrect for this question. High concurrency lets several notebooks share one Spark session instead of starting a session each. Why the correct answer wins: Dynamic allocation releases executors a stage does not need.
- **D:** Incorrect for this question. Autoscale adds executors while the job runs and releases them afterwards, so idle capacity is not billed. Why the correct answer wins: Dynamic allocation releases executors a stage does not need.

### Question 4 — A

Answer: Keep OneLake availability enabled so other engines can read the same data. OneLake availability exposes the same files to every engine. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. Local study-map skill 1.2 (Domain and OneLake Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. In this case: OneLake availability exposes the same files to every engine.
- **B:** Incorrect for this question. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. Why the correct answer wins: OneLake availability exposes the same files to every engine.
- **C:** Incorrect for this question. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. Why the correct answer wins: OneLake availability exposes the same files to every engine.
- **D:** Incorrect for this question. A domain groups workspaces for governance and discovery without moving the data. Why the correct answer wins: OneLake availability exposes the same files to every engine.

### Question 5 — B

Answer: Create the workspace in the required region at creation time. The region is fixed at creation, so it decides where the data can live. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. Local study-map skill 1.2 (Domain and OneLake Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. Why the correct answer wins: The region is fixed at creation, so it decides where the data can live.
- **B:** Correct. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. In this case: The region is fixed at creation, so it decides where the data can live.
- **C:** Incorrect for this question. A domain groups workspaces for governance and discovery without moving the data. Why the correct answer wins: The region is fixed at creation, so it decides where the data can live.
- **D:** Incorrect for this question. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. Why the correct answer wins: The region is fixed at creation, so it decides where the data can live.

### Question 6 — B

Answer: Enable the Apache Airflow job in the workspace and author the DAG. The Airflow job runs the existing DAG without a rewrite. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. Local study-map skill 1.3 (Apache Airflow Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Source-controlled DAGs keep the orchestration reviewable like any other item definition. Why the correct answer wins: The Airflow job runs the existing DAG without a rewrite.
- **B:** Correct. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. In this case: The Airflow job runs the existing DAG without a rewrite.
- **C:** Incorrect for this question. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. Why the correct answer wins: The Airflow job runs the existing DAG without a rewrite.
- **D:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: The Airflow job runs the existing DAG without a rewrite.

### Question 7 — A

Answer: Connect the workspace to a Git repository and commit the item definitions. Connecting to Git gives every change a commit and a history. Git keeps a reviewable history of every item definition instead of an untracked live workspace. Local study-map skill 1.4 (Version Control and Database Projects), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Git keeps a reviewable history of every item definition instead of an untracked live workspace. In this case: Connecting to Git gives every change a commit and a history.
- **B:** Incorrect for this question. Committing build output makes every run look like a change. Why the correct answer wins: Connecting to Git gives every change a commit and a history.
- **C:** Incorrect for this question. Branching keeps unfinished work out of the shared workspace and makes the change reviewable. Why the correct answer wins: Connecting to Git gives every change a commit and a history.
- **D:** Incorrect for this question. An unresolved conflict blocks the update and leaves the workspace and the branch out of step. Why the correct answer wins: Connecting to Git gives every change a commit and a history.

### Question 8 — C

Answer: Use SQLCMD variables for the environment-specific values. SQLCMD variables keep the environment values out of the artefact. SQLCMD variables keep one project artefact deployable to both test and production. Local study-map skill 1.4 (Version Control and Database Projects), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Branching keeps unfinished work out of the shared workspace and makes the change reviewable. Why the correct answer wins: SQLCMD variables keep the environment values out of the artefact.
- **B:** Incorrect for this question. A database project keeps the warehouse schema in source control and deploys it repeatably. Why the correct answer wins: SQLCMD variables keep the environment values out of the artefact.
- **C:** Correct. SQLCMD variables keep one project artefact deployable to both test and production. In this case: SQLCMD variables keep the environment values out of the artefact.
- **D:** Incorrect for this question. The DACPAC is the versioned schema artefact that the deployment consumes. Why the correct answer wins: SQLCMD variables keep the environment values out of the artefact.

### Question 9 — D

Answer: Create a deployment pipeline with development, test, and production stages. A deployment pipeline promotes the same definitions through the stages. The pipeline promotes the same item definitions through the stages instead of rebuilding them. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Promoting every item drags unrelated work into the release. Why the correct answer wins: A deployment pipeline promotes the same definitions through the stages.
- **B:** Incorrect for this question. The comparison shows what the promotion will change in the target before it happens. Why the correct answer wins: A deployment pipeline promotes the same definitions through the stages.
- **C:** Incorrect for this question. A rule stops a promotion from overwriting the target stage environment-specific settings. Why the correct answer wins: A deployment pipeline promotes the same definitions through the stages.
- **D:** Correct. The pipeline promotes the same item definitions through the stages instead of rebuilding them. In this case: A deployment pipeline promotes the same definitions through the stages.

### Question 10 — D

Answer: Compare the stages before promoting. The stage comparison shows the pending change. The comparison shows what the promotion will change in the target before it happens. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A rule stops a promotion from overwriting the target stage environment-specific settings. Why the correct answer wins: The stage comparison shows the pending change.
- **B:** Incorrect for this question. A backward deployment is the supported way to restore a previous stage state. Why the correct answer wins: The stage comparison shows the pending change.
- **C:** Incorrect for this question. The pipeline promotes the same item definitions through the stages instead of rebuilding them. Why the correct answer wins: The stage comparison shows the pending change.
- **D:** Correct. The comparison shows what the promotion will change in the target before it happens. In this case: The stage comparison shows the pending change.

### Question 11 — A

Answer: Grant Admin on the workspace to the platform team. Admin manages the workspace access and settings. Admin is needed to manage access and settings, not to read the data. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Admin is needed to manage access and settings, not to read the data. In this case: Admin manages the workspace access and settings.
- **B:** Incorrect for this question. Item-level sharing avoids granting a workspace role for one report. Why the correct answer wins: Admin manages the workspace access and settings.
- **C:** Incorrect for this question. Viewer allows reading the items without editing them. Why the correct answer wins: Admin manages the workspace access and settings.
- **D:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: Admin manages the workspace access and settings.

### Question 12 — C

Answer: Grant Read on the item. Read on the item is the narrowest grant that still allows use. Read is the narrowest grant that still lets the item be consumed. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: Read on the item is the narrowest grant that still allows use.
- **B:** Incorrect for this question. Viewer allows reading the items without editing them. Why the correct answer wins: Read on the item is the narrowest grant that still allows use.
- **C:** Correct. Read is the narrowest grant that still lets the item be consumed. In this case: Read on the item is the narrowest grant that still allows use.
- **D:** Incorrect for this question. Item-level sharing avoids granting a workspace role for one report. Why the correct answer wins: Read on the item is the narrowest grant that still allows use.

### Question 13 — A

Answer: Define a row-level security policy on the table. Row-level security filters the rows per identity. Row-level security filters rows per identity, so one table returns different rows to different users. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Row-level security filters rows per identity, so one table returns different rows to different users. In this case: Row-level security filters the rows per identity.
- **B:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: Row-level security filters the rows per identity.
- **C:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: Row-level security filters the rows per identity.
- **D:** Incorrect for this question. The predicate must resolve the identity to the region, or every user sees the same rows. Why the correct answer wins: Row-level security filters the rows per identity.

### Question 14 — C

Answer: Apply column-level security so the column is hidden from the group. Column-level security hides the column and leaves the table readable. Column-level security hides the column while leaving the rest of the table readable. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: Column-level security hides the column and leaves the table readable.
- **B:** Incorrect for this question. Row-level security filters rows per identity, so one table returns different rows to different users. Why the correct answer wins: Column-level security hides the column and leaves the table readable.
- **C:** Correct. Column-level security hides the column while leaving the rest of the table readable. In this case: Column-level security hides the column and leaves the table readable.
- **D:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: Column-level security hides the column and leaves the table readable.

### Question 15 — A

Answer: Apply object-level security in the semantic model. Object-level security hides the table from the role. Object-level security hides a table or column from a role in the semantic model. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Object-level security hides a table or column from a role in the semantic model. In this case: Object-level security hides the table from the role.
- **B:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: Object-level security hides the table from the role.
- **C:** Incorrect for this question. Row-level security filters rows per identity, so one table returns different rows to different users. Why the correct answer wins: Object-level security hides the table from the role.
- **D:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: Object-level security hides the table from the role.

### Question 16 — C

Answer: Apply dynamic data masking to the column. Dynamic data masking masks the value and keeps the table queryable. Masking shows a masked value to unauthorised users while the stored data stays intact. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A view removes the column entirely, which is not the same as masking the value. Why the correct answer wins: Dynamic data masking masks the value and keeps the table queryable.
- **B:** Incorrect for this question. A report-level mask protects one visual and leaves every other consumer unmasked. Why the correct answer wins: Dynamic data masking masks the value and keeps the table queryable.
- **C:** Correct. Masking shows a masked value to unauthorised users while the stored data stays intact. In this case: Dynamic data masking masks the value and keeps the table queryable.
- **D:** Incorrect for this question. The masking rule needs the exemption, or the authorised group sees masked values too. Why the correct answer wins: Dynamic data masking masks the value and keeps the table queryable.

### Question 17 — C, E

Answers: Apply dynamic data masking to the column; Exempt the authorised group from the mask. The mask hides the value, and the exemption restores it for support. Masking shows a masked value to unauthorised users while the stored data stays intact. The masking rule needs the exemption, or the authorised group sees masked values too. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: The mask hides the value, and the exemption restores it for support.
- **B:** Incorrect for this question. A view removes the column entirely, which is not the same as masking the value. Why the correct answer wins: The mask hides the value, and the exemption restores it for support.
- **C:** Correct. The masking rule needs the exemption, or the authorised group sees masked values too. In this case: The mask hides the value, and the exemption restores it for support.
- **D:** Incorrect for this question. A report-level mask protects one visual and leaves every other consumer unmasked. Why the correct answer wins: The mask hides the value, and the exemption restores it for support.
- **E:** Correct. Masking shows a masked value to unauthorised users while the stored data stays intact. In this case: The mask hides the value, and the exemption restores it for support.

### Question 18 — C

Answer: Apply the sensitivity label to the item. The sensitivity label travels with the item and its copies. The label travels with the item and drives the protection downstream consumers inherit. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Certification tells consumers the item has been reviewed as authoritative. Why the correct answer wins: The sensitivity label travels with the item and its copies.
- **B:** Incorrect for this question. Inheritance keeps one classification instead of a second opinion on the same data. Why the correct answer wins: The sensitivity label travels with the item and its copies.
- **C:** Correct. The label travels with the item and drives the protection downstream consumers inherit. In this case: The sensitivity label travels with the item and its copies.
- **D:** Incorrect for this question. A default label classifies new items that nobody labels by hand. Why the correct answer wins: The sensitivity label travels with the item and its copies.

### Question 19 — B, C

Answers: Certify the item as the approved source; Set the default sensitivity label for the workspace. Certification marks the approved items, and the default labels the new ones. Certification tells consumers the item has been reviewed as authoritative. A default label classifies new items that nobody labels by hand. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Promotion signals readiness without the review that certification implies. Why the correct answer wins: Certification marks the approved items, and the default labels the new ones.
- **B:** Correct. A default label classifies new items that nobody labels by hand. In this case: Certification marks the approved items, and the default labels the new ones.
- **C:** Correct. Certification tells consumers the item has been reviewed as authoritative. In this case: Certification marks the approved items, and the default labels the new ones.
- **D:** Incorrect for this question. Inheritance keeps one classification instead of a second opinion on the same data. Why the correct answer wins: Certification marks the approved items, and the default labels the new ones.
- **E:** Incorrect for this question. The label travels with the item and drives the protection downstream consumers inherit. Why the correct answer wins: Certification marks the approved items, and the default labels the new ones.

### Question 20 — C

Answer: Read the Fabric audit log in the Microsoft Purview portal. The audit log records the identity, the item, and the time. The audit log records who did what to which item and when. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The audit log records the identity, the item, and the time.
- **B:** Incorrect for this question. Filtering turns a very large log into the events that answer the question. Why the correct answer wins: The audit log records the identity, the item, and the time.
- **C:** Correct. The audit log records who did what to which item and when. In this case: The audit log records the identity, the item, and the time.
- **D:** Incorrect for this question. The audit log has a retention window, so an investigation that starts late needs the export. Why the correct answer wins: The audit log records the identity, the item, and the time.

### Question 21 — B, C

Answers: Read the Fabric audit log in the Microsoft Purview portal; Export the audit events before the retention window closes. The audit log holds the events, and the export preserves them. The audit log records who did what to which item and when. The audit log has a retention window, so an investigation that starts late needs the export. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Filtering turns a very large log into the events that answer the question. Why the correct answer wins: The audit log holds the events, and the export preserves them.
- **B:** Correct. The audit log has a retention window, so an investigation that starts late needs the export. In this case: The audit log holds the events, and the export preserves them.
- **C:** Correct. The audit log records who did what to which item and when. In this case: The audit log holds the events, and the export preserves them.
- **D:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The audit log holds the events, and the export preserves them.
- **E:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The audit log holds the events, and the export preserves them.

### Question 22 — D

Answer: Scope the OneLake role to the folder that holds the restricted table. A folder-scoped OneLake role restricts the data itself. A folder-scoped role restricts exactly the data rather than the whole lakehouse. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A group grant is maintained once instead of once per person. Why the correct answer wins: A folder-scoped OneLake role restricts the data itself.
- **B:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: A folder-scoped OneLake role restricts the data itself.
- **C:** Incorrect for this question. OneLake security governs data access independently of the workspace role. Why the correct answer wins: A folder-scoped OneLake role restricts the data itself.
- **D:** Correct. A folder-scoped role restricts exactly the data rather than the whole lakehouse. In this case: A folder-scoped OneLake role restricts the data itself.

### Question 23 — A, D

Answers: Configure OneLake security roles for the lakehouse; Grant the OneLake role to a security group rather than to individuals. OneLake security governs the data, and the group grant is maintained once. OneLake security governs data access independently of the workspace role. A group grant is maintained once instead of once per person. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A group grant is maintained once instead of once per person. In this case: OneLake security governs the data, and the group grant is maintained once.
- **B:** Incorrect for this question. A folder-scoped role restricts exactly the data rather than the whole lakehouse. Why the correct answer wins: OneLake security governs the data, and the group grant is maintained once.
- **C:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: OneLake security governs the data, and the group grant is maintained once.
- **D:** Correct. OneLake security governs data access independently of the workspace role. In this case: OneLake security governs the data, and the group grant is maintained once.
- **E:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: OneLake security governs the data, and the group grant is maintained once.

### Question 24 — B

Answer: Use a KQL query against the eventhouse. KQL is the native language of the eventhouse tables. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Why the correct answer wins: KQL is the native language of the eventhouse tables.
- **B:** Correct. In this case: KQL is the native language of the eventhouse tables.
- **C:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: KQL is the native language of the eventhouse tables.
- **D:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: KQL is the native language of the eventhouse tables.

### Question 25 — D

Answer: Use a Dataflow Gen2 for the transformation. A Dataflow Gen2 is the low-code engine for that analyst. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Why the correct answer wins: A Dataflow Gen2 is the low-code engine for that analyst.
- **B:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: A Dataflow Gen2 is the low-code engine for that analyst.
- **C:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: A Dataflow Gen2 is the low-code engine for that analyst.
- **D:** Correct. A Dataflow Gen2 suits a transformation that is expressible in Power Query. In this case: A Dataflow Gen2 is the low-code engine for that analyst.

### Question 26 — D, E

Answers: Use a pipeline for the copy and the orchestration; Use a notebook for the transformation. The pipeline copies and orders, and the notebook holds the PySpark. A pipeline owns the scheduling, the copy activity, and the dependency between steps. A notebook is the right place for PySpark that a low-code transform cannot express. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. KQL is the native language of the eventhouse tables. Why the correct answer wins: The pipeline copies and orders, and the notebook holds the PySpark.
- **B:** Incorrect for this question. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Why the correct answer wins: The pipeline copies and orders, and the notebook holds the PySpark.
- **C:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: The pipeline copies and orders, and the notebook holds the PySpark.
- **D:** Correct. A notebook is the right place for PySpark that a low-code transform cannot express. In this case: The pipeline copies and orders, and the notebook holds the PySpark.
- **E:** Correct. A pipeline owns the scheduling, the copy activity, and the dependency between steps. In this case: The pipeline copies and orders, and the notebook holds the PySpark.

### Question 27 — A

Answer: Look up the stored watermark before the copy. A lookup reads the stored watermark before the copy. The lookup is what makes the load incremental rather than a full reload. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The lookup is what makes the load incremental rather than a full reload. In this case: A lookup reads the stored watermark before the copy.
- **B:** Incorrect for this question. A dynamic expression computes the path instead of hard-coding a date. Why the correct answer wins: A lookup reads the stored watermark before the copy.
- **C:** Incorrect for this question. A parameter makes one pipeline reusable across folders and environments. Why the correct answer wins: A lookup reads the stored watermark before the copy.
- **D:** Incorrect for this question. A variable carries the computed value between the activities that need it. Why the correct answer wins: A lookup reads the stored watermark before the copy.

### Question 28 — A, B

Answers: Add an event-based trigger so the run starts when the file arrives; Trigger on the file-created event for the landing folder. The event trigger starts the run, and the file event scopes it. An event trigger removes the gap between the file landing and the run starting. The file-created event is the signal that the extract has finished arriving. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The file-created event is the signal that the extract has finished arriving. In this case: The event trigger starts the run, and the file event scopes it.
- **B:** Correct. An event trigger removes the gap between the file landing and the run starting. In this case: The event trigger starts the run, and the file event scopes it.
- **C:** Incorrect for this question. The schedule trigger is what makes the run recur without a person starting it. Why the correct answer wins: The event trigger starts the run, and the file event scopes it.
- **D:** Incorrect for this question. A parameter makes one pipeline reusable across folders and environments. Why the correct answer wins: The event trigger starts the run, and the file event scopes it.
- **E:** Incorrect for this question. Until repeats the check and stops when the condition is met or the timeout expires. Why the correct answer wins: The event trigger starts the run, and the file event scopes it.

### Question 29 — B

Answer: Classify the data → apply the sensitivity label → grant the workspace role → add row-level security → test as each persona. Classification drives the label, access follows, and the filter is proven last. The classification drives the label, the role grants the access, and the row filter is proven against each persona after both are in place. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A row filter written before the access model exists is written against the wrong identities. Why the correct answer wins: Classification drives the label, access follows, and the filter is proven last.
- **B:** Correct. The classification drives the label, the role grants the access, and the row filter is proven against each persona after both are in place. In this case: Classification drives the label, access follows, and the filter is proven last.
- **C:** Incorrect for this question. Testing before the row filter exists proves nothing, and the label follows the classification rather than preceding it. Why the correct answer wins: Classification drives the label, access follows, and the filter is proven last.
- **D:** Incorrect for this question. The persona test is the last step, and a label applied before the data is classified is a guess. Why the correct answer wins: Classification drives the label, access follows, and the filter is proven last.

### Question 30 — B

Answer: Confirm the source of truth → apply the label → endorse the item → verify the audit entry. Authority is confirmed before the endorsement claims it. Endorsement claims authority, so the authority is confirmed first, and the audit entry is the proof that the governance action was recorded. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The audit entry records actions that have already happened, so it cannot come first. Why the correct answer wins: Authority is confirmed before the endorsement claims it.
- **B:** Correct. Endorsement claims authority, so the authority is confirmed first, and the audit entry is the proof that the governance action was recorded. In this case: Authority is confirmed before the endorsement claims it.
- **C:** Incorrect for this question. Endorsing before confirming the source of truth endorses whatever happened to be there. Why the correct answer wins: Authority is confirmed before the endorsement claims it.
- **D:** Incorrect for this question. The label follows the classification, and the audit entry follows the actions it records. Why the correct answer wins: Authority is confirmed before the endorsement claims it.

### Question 31 — B

Answer: Load only the rows newer than the stored watermark. An incremental load moves the delta instead of the history. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: An incremental load moves the delta instead of the history.
- **B:** Correct. In this case: An incremental load moves the delta instead of the history.
- **C:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: An incremental load moves the delta instead of the history.
- **D:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: An incremental load moves the delta instead of the history.

### Question 32 — C

Answer: Store the last successful load timestamp in a control table. The watermark records the last successful position. The control table is what lets the next run know where this one stopped. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The lookup is what makes the load incremental rather than a full reload. Why the correct answer wins: The watermark records the last successful position.
- **B:** Incorrect for this question. Reprocessing the partition corrects the aggregate that was already published. Why the correct answer wins: The watermark records the last successful position.
- **C:** Correct. The control table is what lets the next run know where this one stopped. In this case: The watermark records the last successful position.
- **D:** Incorrect for this question. An incremental load moves the delta instead of the history. Why the correct answer wins: The watermark records the last successful position.

### Question 33 — D

Answer: Generate a surrogate key instead of reusing the source key. A surrogate key keeps the identity stable when the source key changes. A surrogate key decouples the warehouse from the source system identifiers. Local study-map skill 2.2 (Dimensional Model Preparation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: A surrogate key keeps the identity stable when the source key changes.
- **B:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: A surrogate key keeps the identity stable when the source key changes.
- **C:** Incorrect for this question. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. Why the correct answer wins: A surrogate key keeps the identity stable when the source key changes.
- **D:** Correct. A surrogate key decouples the warehouse from the source system identifiers. In this case: A surrogate key keeps the identity stable when the source key changes.

### Question 34 — A

Answer: Build a type 2 dimension with validity dates and a current flag. A type 2 dimension preserves the value that applied at the time. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. Local study-map skill 2.2 (Dimensional Model Preparation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. In this case: A type 2 dimension preserves the value that applied at the time.
- **B:** Incorrect for this question. A surrogate key decouples the warehouse from the source system identifiers. Why the correct answer wins: A type 2 dimension preserves the value that applied at the time.
- **C:** Incorrect for this question. A star schema keeps the fact table narrow and the dimensions reusable. Why the correct answer wins: A type 2 dimension preserves the value that applied at the time.
- **D:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: A type 2 dimension preserves the value that applied at the time.

### Question 35 — C

Answer: Set a checkpoint location for the streaming query. The checkpoint records where the stream should resume. The checkpoint is what makes the stream restart from where it stopped. Local study-map skill 2.3 (Streaming Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: The checkpoint records where the stream should resume.
- **B:** Incorrect for this question. Native tables give full KQL capability over the streaming data. Why the correct answer wins: The checkpoint records where the stream should resume.
- **C:** Correct. The checkpoint is what makes the stream restart from where it stopped. In this case: The checkpoint records where the stream should resume.
- **D:** Incorrect for this question. A watermark sets how long the engine waits for late events before closing a window. Why the correct answer wins: The checkpoint records where the stream should resume.

### Question 36 — D, E

Answers: Set a checkpoint location for the streaming query; Set a watermark so late events are handled deterministically. The checkpoint resumes the query, and the watermark closes the window. The checkpoint is what makes the stream restart from where it stopped. A watermark sets how long the engine waits for late events before closing a window. Local study-map skill 2.3 (Streaming Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Native tables give full KQL capability over the streaming data. Why the correct answer wins: The checkpoint resumes the query, and the watermark closes the window.
- **B:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: The checkpoint resumes the query, and the watermark closes the window.
- **C:** Incorrect for this question. An eventstream is the no-code path from a source to a destination. Why the correct answer wins: The checkpoint resumes the query, and the watermark closes the window.
- **D:** Correct. A watermark sets how long the engine waits for late events before closing a window. In this case: The checkpoint resumes the query, and the watermark closes the window.
- **E:** Correct. The checkpoint is what makes the stream restart from where it stopped. In this case: The checkpoint resumes the query, and the watermark closes the window.

### Question 37 — A

Answer: Load the curated model into the warehouse. A warehouse supports the transactional T-SQL the close needs. A warehouse gives multi-table T-SQL transactions and a governed relational model. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. A warehouse gives multi-table T-SQL transactions and a governed relational model. In this case: A warehouse supports the transactional T-SQL the close needs.
- **B:** Incorrect for this question. The Files area keeps the raw extract in its original format. Why the correct answer wins: A warehouse supports the transactional T-SQL the close needs.
- **C:** Incorrect for this question. An eventhouse is optimized for high-volume time-series queries. Why the correct answer wins: A warehouse supports the transactional T-SQL the close needs.
- **D:** Incorrect for this question. A KQL database indexes the timestamp column for the range queries the dashboards run. Why the correct answer wins: A warehouse supports the transactional T-SQL the close needs.

### Question 38 — C

Answer: Store the telemetry in an eventhouse KQL database. An eventhouse is optimized for high-volume time-range queries. An eventhouse is optimized for high-volume time-series queries. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The Files area keeps the raw extract in its original format. Why the correct answer wins: An eventhouse is optimized for high-volume time-range queries.
- **B:** Incorrect for this question. A warehouse gives multi-table T-SQL transactions and a governed relational model. Why the correct answer wins: An eventhouse is optimized for high-volume time-range queries.
- **C:** Correct. An eventhouse is optimized for high-volume time-series queries. In this case: An eventhouse is optimized for high-volume time-range queries.
- **D:** Incorrect for this question. The endpoint gives read-only T-SQL over the Delta tables without a copy. Why the correct answer wins: An eventhouse is optimized for high-volume time-range queries.

### Question 39 — D

Answer: Transform with T-SQL against the warehouse. T-SQL is the natural engine once the data is relational there. T-SQL is the right engine once the data is relational and already in the warehouse. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: T-SQL is the natural engine once the data is relational there.
- **B:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: T-SQL is the natural engine once the data is relational there.
- **C:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: T-SQL is the natural engine once the data is relational there.
- **D:** Correct. T-SQL is the right engine once the data is relational and already in the warehouse. In this case: T-SQL is the natural engine once the data is relational there.

### Question 40 — A

Answer: Transform with KQL in the eventhouse. KQL is the native language for the eventhouse tables. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. In this case: KQL is the native language for the eventhouse tables.
- **B:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: KQL is the native language for the eventhouse tables.
- **C:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: KQL is the native language for the eventhouse tables.
- **D:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: KQL is the native language for the eventhouse tables.

### Question 41 — C

Answer: Create an ADLS Gen2 shortcut to the external container. An ADLS Gen2 shortcut exposes the container without a copy. The shortcut exposes the external container as if the files were in OneLake. Local study-map skill 2.6 (OneLake Shortcuts), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A copy duplicates the data, so the source of truth is no longer one place. Why the correct answer wins: An ADLS Gen2 shortcut exposes the container without a copy.
- **B:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: An ADLS Gen2 shortcut exposes the container without a copy.
- **C:** Correct. The shortcut exposes the external container as if the files were in OneLake. In this case: An ADLS Gen2 shortcut exposes the container without a copy.
- **D:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: An ADLS Gen2 shortcut exposes the container without a copy.

### Question 42 — C, D

Answers: Create an internal OneLake shortcut to the other lakehouse table; Create a shortcut rather than a copy when the source stays authoritative. The internal shortcut points at a Fabric item, and a shortcut avoids the copy. An internal shortcut points at another Fabric item without copying the data. A shortcut has no second copy to keep in step with the source. Local study-map skill 2.6 (OneLake Shortcuts), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A copy duplicates the data, so the source of truth is no longer one place. Why the correct answer wins: The internal shortcut points at a Fabric item, and a shortcut avoids the copy.
- **B:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: The internal shortcut points at a Fabric item, and a shortcut avoids the copy.
- **C:** Correct. A shortcut has no second copy to keep in step with the source. In this case: The internal shortcut points at a Fabric item, and a shortcut avoids the copy.
- **D:** Correct. An internal shortcut points at another Fabric item without copying the data. In this case: The internal shortcut points at a Fabric item, and a shortcut avoids the copy.
- **E:** Incorrect for this question. The shortcut exposes the external container as if the files were in OneLake. Why the correct answer wins: The internal shortcut points at a Fabric item, and a shortcut avoids the copy.

### Question 43 — B

Answer: Enable mirroring for the operational database. Mirroring replicates the source tables continuously. Local study-map skill 2.7 (Mirroring), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: Mirroring replicates the source tables continuously.
- **B:** Correct. In this case: Mirroring replicates the source tables continuously.
- **C:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: Mirroring replicates the source tables continuously.
- **D:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: Mirroring replicates the source tables continuously.

### Question 44 — B

Answer: Use a Copy activity in the pipeline. A Copy activity moves the rows as one orchestrated step. The Copy activity moves the files or rows as one orchestrated step. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.
- **B:** Correct. The Copy activity moves the files or rows as one orchestrated step. In this case: A Copy activity moves the rows as one orchestrated step.
- **C:** Incorrect for this question. Appending preserves the earlier loads that the incremental pattern depends on. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.
- **D:** Incorrect for this question. Get Metadata turns an unknown folder into a list the loop can iterate. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.

### Question 45 — D

Answer: Use Get Metadata to list the files to process. Get Metadata turns the folder into a list the loop can iterate. Get Metadata turns an unknown folder into a list the loop can iterate. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: Get Metadata turns the folder into a list the loop can iterate.
- **B:** Incorrect for this question. Deleting after success prevents the same file being loaded twice. Why the correct answer wins: Get Metadata turns the folder into a list the loop can iterate.
- **C:** Incorrect for this question. ForEach applies the same pattern to every object the lookup returned. Why the correct answer wins: Get Metadata turns the folder into a list the loop can iterate.
- **D:** Correct. Get Metadata turns an unknown folder into a list the loop can iterate. In this case: Get Metadata turns the folder into a list the loop can iterate.

### Question 46 — A

Answer: Use a window function to rank within the partition. A window function reads the previous row without collapsing it. A window computes across related rows without collapsing them into one. Local study-map skill 2.9 (PySpark Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. A window computes across related rows without collapsing them into one. In this case: A window function reads the previous row without collapsing it.
- **B:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: A window function reads the previous row without collapsing it.
- **C:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: A window function reads the previous row without collapsing it.
- **D:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: A window function reads the previous row without collapsing it.

### Question 47 — B, C

Answers: Transform with PySpark in a notebook; Use a window function to rank within the partition. PySpark scales the cleansing, and the window function ranks. PySpark handles the row-level and windowed transformations that Spark scales. A window computes across related rows without collapsing them into one. Local study-map skill 2.9 (PySpark Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: PySpark scales the cleansing, and the window function ranks.
- **B:** Correct. PySpark handles the row-level and windowed transformations that Spark scales. In this case: PySpark scales the cleansing, and the window function ranks.
- **C:** Correct. A window computes across related rows without collapsing them into one. In this case: PySpark scales the cleansing, and the window function ranks.
- **D:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: PySpark scales the cleansing, and the window function ranks.
- **E:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: PySpark scales the cleansing, and the window function ranks.

### Question 48 — C

Answer: Transform with T-SQL against the warehouse. T-SQL performs the merge when the dimension is already in the warehouse. T-SQL is the right engine once the data is relational and already in the warehouse. Local study-map skill 2.10 (T-SQL and KQL Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: T-SQL performs the merge when the dimension is already in the warehouse.
- **B:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: T-SQL performs the merge when the dimension is already in the warehouse.
- **C:** Correct. T-SQL is the right engine once the data is relational and already in the warehouse. In this case: T-SQL performs the merge when the dimension is already in the warehouse.
- **D:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: T-SQL performs the merge when the dimension is already in the warehouse.

### Question 49 — A, D

Answers: Transform with T-SQL against the warehouse; Transform with KQL in the eventhouse. T-SQL performs the merge, and KQL filters the telemetry. T-SQL is the right engine once the data is relational and already in the warehouse. KQL is the native language for the eventhouse tables. Local study-map skill 2.10 (T-SQL and KQL Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. KQL is the native language for the eventhouse tables. In this case: T-SQL performs the merge, and KQL filters the telemetry.
- **B:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: T-SQL performs the merge, and KQL filters the telemetry.
- **C:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: T-SQL performs the merge, and KQL filters the telemetry.
- **D:** Correct. T-SQL is the right engine once the data is relational and already in the warehouse. In this case: T-SQL performs the merge, and KQL filters the telemetry.
- **E:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: T-SQL performs the merge, and KQL filters the telemetry.

### Question 50 — D

Answer: Denormalize the model so the report needs no join. Denormalization trades storage for the query shape actually used. Denormalization trades storage for the query shape the report actually uses. Local study-map skill 2.11 (Denormalization, Grouping, and Aggregation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: Denormalization trades storage for the query shape actually used.
- **B:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: Denormalization trades storage for the query shape actually used.
- **C:** Incorrect for this question. A star schema keeps the fact table narrow and the dimensions reusable. Why the correct answer wins: Denormalization trades storage for the query shape actually used.
- **D:** Correct. Denormalization trades storage for the query shape the report actually uses. In this case: Denormalization trades storage for the query shape actually used.

### Question 51 — D

Answer: Pivot the rows into the reporting columns. The pivot produces one column per region. The pivot is what produces one column per period the report expects. Local study-map skill 2.11 (Denormalization, Grouping, and Aggregation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: The pivot produces one column per region.
- **B:** Incorrect for this question. Denormalization trades storage for the query shape the report actually uses. Why the correct answer wins: The pivot produces one column per region.
- **C:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: The pivot produces one column per region.
- **D:** Correct. The pivot is what produces one column per period the report expects. In this case: The pivot produces one column per region.

### Question 52 — D

Answer: Reprocess the affected partitions when the data arrives late. Reprocessing the affected partitions corrects the published total. Reprocessing the partition corrects the aggregate that was already published. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Reprocessing the affected partitions corrects the published total.
- **B:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: Reprocessing the affected partitions corrects the published total.
- **C:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Reprocessing the affected partitions corrects the published total.
- **D:** Correct. Reprocessing the partition corrects the aggregate that was already published. In this case: Reprocessing the affected partitions corrects the published total.

### Question 53 — B

Answer: Process the stream with Spark structured streaming. Structured streaming reuses the batch logic on an unbounded source. Structured streaming suits stateful processing and the same PySpark logic used in batch. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. An update policy transforms the data as it lands in the KQL table. Why the correct answer wins: Structured streaming reuses the batch logic on an unbounded source.
- **B:** Correct. Structured streaming suits stateful processing and the same PySpark logic used in batch. In this case: Structured streaming reuses the batch logic on an unbounded source.
- **C:** Incorrect for this question. A batch job over the landing folder adds latency the streaming requirement may not allow. Why the correct answer wins: Structured streaming reuses the batch logic on an unbounded source.
- **D:** Incorrect for this question. An eventstream is the no-code path from a source to a destination. Why the correct answer wins: Structured streaming reuses the batch logic on an unbounded source.

### Question 54 — D, E

Answers: Process the stream with an eventstream; Process the stream with Spark structured streaming. The eventstream is the no-code path, and structured streaming reuses the logic. An eventstream is the no-code path from a source to a destination. Structured streaming suits stateful processing and the same PySpark logic used in batch. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. An update policy transforms the data as it lands in the KQL table. Why the correct answer wins: The eventstream is the no-code path, and structured streaming reuses the logic.
- **B:** Incorrect for this question. The checkpoint is what makes the stream restart from where it stopped. Why the correct answer wins: The eventstream is the no-code path, and structured streaming reuses the logic.
- **C:** Incorrect for this question. A batch job over the landing folder adds latency the streaming requirement may not allow. Why the correct answer wins: The eventstream is the no-code path, and structured streaming reuses the logic.
- **D:** Correct. An eventstream is the no-code path from a source to a destination. In this case: The eventstream is the no-code path, and structured streaming reuses the logic.
- **E:** Correct. Structured streaming suits stateful processing and the same PySpark logic used in batch. In this case: The eventstream is the no-code path, and structured streaming reuses the logic.

### Question 55 — B

Answer: Set a watermark so late events are handled deterministically. A watermark sets how long the engine waits before closing a window. A watermark sets how long the engine waits for late events before closing a window. Local study-map skill 2.14 (Eventstream and Spark Structured Streaming), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Native tables give full KQL capability over the streaming data. Why the correct answer wins: A watermark sets how long the engine waits before closing a window.
- **B:** Correct. A watermark sets how long the engine waits for late events before closing a window. In this case: A watermark sets how long the engine waits before closing a window.
- **C:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: A watermark sets how long the engine waits before closing a window.
- **D:** Incorrect for this question. The checkpoint is what makes the stream restart from where it stopped. Why the correct answer wins: A watermark sets how long the engine waits before closing a window.

### Question 56 — B

Answer: Use a tumbling window for the fixed five-minute aggregate. A tumbling window covers fixed, non-overlapping intervals. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A materialized view keeps the aggregate fresh instead of recomputing it per query. Why the correct answer wins: A tumbling window covers fixed, non-overlapping intervals.
- **B:** Correct. In this case: A tumbling window covers fixed, non-overlapping intervals.
- **C:** Incorrect for this question. A sliding window emits on the event that satisfies the condition rather than on a fixed boundary. Why the correct answer wins: A tumbling window covers fixed, non-overlapping intervals.
- **D:** Incorrect for this question. A hopping window covers overlapping intervals so a trend can be smoothed. Why the correct answer wins: A tumbling window covers fixed, non-overlapping intervals.

### Question 57 — B

Answer: Create a materialized view for the repeated aggregation. A materialized view keeps the aggregate fresh for every consumer. A materialized view keeps the aggregate fresh instead of recomputing it per query. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A hopping window covers overlapping intervals so a trend can be smoothed. Why the correct answer wins: A materialized view keeps the aggregate fresh for every consumer.
- **B:** Correct. A materialized view keeps the aggregate fresh instead of recomputing it per query. In this case: A materialized view keeps the aggregate fresh for every consumer.
- **C:** Incorrect for this question. A tumbling window covers fixed, non-overlapping intervals. Why the correct answer wins: A materialized view keeps the aggregate fresh for every consumer.
- **D:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: A materialized view keeps the aggregate fresh for every consumer.

### Question 58 — A

Answer: Read the watermark → extract only the rows after it → merge into the target → update the watermark. The watermark bounds the extract and moves after the merge. The watermark bounds the extract, the merge applies the delta, and the watermark advances only after the merge succeeds. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. The watermark bounds the extract, the merge applies the delta, and the watermark advances only after the merge succeeds. In this case: The watermark bounds the extract and moves after the merge.
- **B:** Incorrect for this question. Nothing has been extracted, so there is nothing to merge, and the watermark moves before the data does. Why the correct answer wins: The watermark bounds the extract and moves after the merge.
- **C:** Incorrect for this question. A full extract ignores the watermark, so reading it afterwards adds nothing and the target reloads the history. Why the correct answer wins: The watermark bounds the extract and moves after the merge.
- **D:** Incorrect for this question. Advancing the watermark before the merge loses every row the failed merge did not write. Why the correct answer wins: The watermark bounds the extract and moves after the merge.

### Question 59 — A

Answer: Detect the duplicates and the late rows → decide the surviving record → correct the affected partition → recompute the aggregate. Detection and the survivor rule precede correction and recompute. The detection comes first, the rule decides the survivor, the partition is corrected, and only then is the published total recomputed. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. The detection comes first, the rule decides the survivor, the partition is corrected, and only then is the published total recomputed. In this case: Detection and the survivor rule precede correction and recompute.
- **B:** Incorrect for this question. A rule chosen before the duplicates are known is chosen blind. Why the correct answer wins: Detection and the survivor rule precede correction and recompute.
- **C:** Incorrect for this question. Recomputing before the data is corrected republishes the same wrong total. Why the correct answer wins: Detection and the survivor rule precede correction and recompute.
- **D:** Incorrect for this question. The partition cannot be corrected before the rule decides which record survives. Why the correct answer wins: Detection and the survivor rule precede correction and recompute.

### Question 60 — D

Answer: Define the eventstream source → add the destination → create the KQL table → build the materialized view → alert on the aggregate. Source and destination precede the table, the view, and the alert. The source and destination define the pipeline, the table receives the events, the view aggregates them, and the alert reads the aggregate. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A destination with no source receives nothing, and the source is the first decision. Why the correct answer wins: Source and destination precede the table, the view, and the alert.
- **B:** Incorrect for this question. The alert fires before the destination and the view that produce the aggregate. Why the correct answer wins: Source and destination precede the table, the view, and the alert.
- **C:** Incorrect for this question. The alert has nothing to read until the view, the table, and the stream exist. Why the correct answer wins: Source and destination precede the table, the view, and the alert.
- **D:** Correct. The source and destination define the pipeline, the table receives the events, the view aggregates them, and the alert reads the aggregate. In this case: Source and destination precede the table, the view, and the alert.

### Question 61 — B

Answer: Use the Monitoring hub for the run history. The Monitoring hub lists every run with its status and duration. The hub lists every run with its status, duration, and owning item. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **B:** Correct. The hub lists every run with its status, duration, and owning item. In this case: The Monitoring hub lists every run with its status and duration.
- **C:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **D:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.

### Question 62 — A

Answer: Read the item activity log. The item activity log covers that item's runs. The activity log records the runs of one item with their outcomes. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The activity log records the runs of one item with their outcomes. In this case: The item activity log covers that item's runs.
- **B:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The item activity log covers that item's runs.
- **C:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The item activity log covers that item's runs.
- **D:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The item activity log covers that item's runs.

### Question 63 — A

Answer: Read the refresh history for the semantic model. The refresh history records each attempt and its duration. The refresh history separates a failed refresh from a slow one. Local study-map skill 3.2 (Monitoring Semantic Model Refresh), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The refresh history separates a failed refresh from a slow one. In this case: The refresh history records each attempt and its duration.
- **B:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The refresh history records each attempt and its duration.
- **C:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The refresh history records each attempt and its duration.
- **D:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The refresh history records each attempt and its duration.

### Question 64 — A, E

Answers: Read the refresh history for the semantic model; Send the logs to a Log Analytics workspace. The refresh history triages, and Log Analytics keeps the longer record. The refresh history separates a failed refresh from a slow one. Log Analytics keeps the history that the in-product views expire. Local study-map skill 3.2 (Monitoring Semantic Model Refresh), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The refresh history separates a failed refresh from a slow one. In this case: The refresh history triages, and Log Analytics keeps the longer record.
- **B:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The refresh history triages, and Log Analytics keeps the longer record.
- **C:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The refresh history triages, and Log Analytics keeps the longer record.
- **D:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The refresh history triages, and Log Analytics keeps the longer record.
- **E:** Correct. Log Analytics keeps the history that the in-product views expire. In this case: The refresh history triages, and Log Analytics keeps the longer record.

### Question 65 — D

Answer: Configure an alert on the failing condition. An alert turns the silent failure into a notification. An alert turns a silent failure into a notification. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Alerting on success as well as failure trains the team to ignore the alert. Why the correct answer wins: An alert turns the silent failure into a notification.
- **B:** Incorrect for this question. The alert must reach the owner, or it becomes noise nobody acts on. Why the correct answer wins: An alert turns the silent failure into a notification.
- **C:** Incorrect for this question. An activator rule evaluates the stream and fires when the condition holds. Why the correct answer wins: An alert turns the silent failure into a notification.
- **D:** Correct. An alert turns a silent failure into a notification. In this case: An alert turns the silent failure into a notification.

### Question 66 — A

Answer: Use a Data Activator rule that watches the streaming condition. A Data Activator rule evaluates the streaming condition. An activator rule evaluates the stream and fires when the condition holds. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. An activator rule evaluates the stream and fires when the condition holds. In this case: A Data Activator rule evaluates the streaming condition.
- **B:** Incorrect for this question. A dashboard over the monitoring table makes the trend visible between runs. Why the correct answer wins: A Data Activator rule evaluates the streaming condition.
- **C:** Incorrect for this question. An alert turns a silent failure into a notification. Why the correct answer wins: A Data Activator rule evaluates the streaming condition.
- **D:** Incorrect for this question. Alerting on success as well as failure trains the team to ignore the alert. Why the correct answer wins: A Data Activator rule evaluates the streaming condition.

### Question 67 — A

Answer: Add a retry policy with a delay to the failing activity. A retry policy absorbs a transient failure. A retry absorbs a transient failure that the next attempt would not repeat. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. A retry absorbs a transient failure that the next attempt would not repeat. In this case: A retry policy absorbs a transient failure.
- **B:** Incorrect for this question. An error branch turns a silent failure into an explicit outcome. Why the correct answer wins: A retry policy absorbs a transient failure.
- **C:** Incorrect for this question. The dependency is what makes the failure path execute at all. Why the correct answer wins: A retry policy absorbs a transient failure.
- **D:** Incorrect for this question. Until repeats the check and stops when the condition is met or the timeout expires. Why the correct answer wins: A retry policy absorbs a transient failure.

### Question 68 — D

Answer: Set the failure dependency so the handler runs when the step fails. The failure dependency is what makes the handler execute. The dependency is what makes the failure path execute at all. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. An error branch turns a silent failure into an explicit outcome. Why the correct answer wins: The failure dependency is what makes the handler execute.
- **B:** Incorrect for this question. Until repeats the check and stops when the condition is met or the timeout expires. Why the correct answer wins: The failure dependency is what makes the handler execute.
- **C:** Incorrect for this question. A retry absorbs a transient failure that the next attempt would not repeat. Why the correct answer wins: The failure dependency is what makes the handler execute.
- **D:** Correct. The dependency is what makes the failure path execute at all. In this case: The failure dependency is what makes the handler execute.

### Question 69 — D

Answer: Inspect the failing cell output and exit value. The failing cell's output reports the exception with its stack. The cell output is where the exception is reported with its stack. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The failing cell's output reports the exception with its stack.
- **B:** Incorrect for this question. The Spark UI shows the stages and tasks where the time went. Why the correct answer wins: The failing cell's output reports the exception with its stack.
- **C:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The failing cell's output reports the exception with its stack.
- **D:** Correct. The cell output is where the exception is reported with its stack. In this case: The failing cell's output reports the exception with its stack.

### Question 70 — B

Answer: Open the Spark UI for the application. The Spark UI shows where the stages spend their time. The Spark UI shows the stages and tasks where the time went. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The Spark UI shows where the stages spend their time.
- **B:** Correct. The Spark UI shows the stages and tasks where the time went. In this case: The Spark UI shows where the stages spend their time.
- **C:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The Spark UI shows where the stages spend their time.
- **D:** Incorrect for this question. The cell output is where the exception is reported with its stack. Why the correct answer wins: The Spark UI shows where the stages spend their time.

### Question 71 — A, E

Answers: Inspect the failing cell output and exit value; Open the Spark UI for the application. The cell output explains the failure, and the UI explains the time. The cell output is where the exception is reported with its stack. The Spark UI shows the stages and tasks where the time went. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The Spark UI shows the stages and tasks where the time went. In this case: The cell output explains the failure, and the UI explains the time.
- **B:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The cell output explains the failure, and the UI explains the time.
- **C:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The cell output explains the failure, and the UI explains the time.
- **D:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The cell output explains the failure, and the UI explains the time.
- **E:** Correct. The cell output is where the exception is reported with its stack. In this case: The cell output explains the failure, and the UI explains the time.

### Question 72 — C

Answer: Query the ingestion failures table in the KQL database. The ingestion failures table records each rejected record. The failures table records the rejected records and the reason for each. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The ingestion failures table records each rejected record.
- **B:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The ingestion failures table records each rejected record.
- **C:** Correct. The failures table records the rejected records and the reason for each. In this case: The ingestion failures table records each rejected record.
- **D:** Incorrect for this question. The runtime metrics show whether the source or the destination is blocking. Why the correct answer wins: The ingestion failures table records each rejected record.

### Question 73 — A

Answer: Inspect the eventstream runtime metrics. The runtime metrics show whether source or destination is limiting. The runtime metrics show whether the source or the destination is blocking. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The runtime metrics show whether the source or the destination is blocking. In this case: The runtime metrics show whether source or destination is limiting.
- **B:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The runtime metrics show whether source or destination is limiting.
- **C:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The runtime metrics show whether source or destination is limiting.
- **D:** Incorrect for this question. The failures table records the rejected records and the reason for each. Why the correct answer wins: The runtime metrics show whether source or destination is limiting.

### Question 74 — A, E

Answers: Query the ingestion failures table in the KQL database; Inspect the eventstream runtime metrics. The metrics show the gap, and the failures table shows the records. The failures table records the rejected records and the reason for each. The runtime metrics show whether the source or the destination is blocking. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The failures table records the rejected records and the reason for each. In this case: The metrics show the gap, and the failures table shows the records.
- **B:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The metrics show the gap, and the failures table shows the records.
- **C:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The metrics show the gap, and the failures table shows the records.
- **D:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The metrics show the gap, and the failures table shows the records.
- **E:** Correct. The runtime metrics show whether the source or the destination is blocking. In this case: The metrics show the gap, and the failures table shows the records.

### Question 75 — B

Answer: Read the T-SQL error message and then the query plan. The T-SQL message names the object or the conversion. The message names the object or the conversion; the plan explains the cost. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The T-SQL message names the object or the conversion.
- **B:** Correct. The message names the object or the conversion; the plan explains the cost. In this case: The T-SQL message names the object or the conversion.
- **C:** Incorrect for this question. A shortcut fails for a connection or permission reason more often than for a data reason. Why the correct answer wins: The T-SQL message names the object or the conversion.
- **D:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The T-SQL message names the object or the conversion.

### Question 76 — C

Answer: Check the shortcut connection and the delegated permission. The delegated permission behind the shortcut must be rechecked. A shortcut fails for a connection or permission reason more often than for a data reason. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The delegated permission behind the shortcut must be rechecked.
- **B:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The delegated permission behind the shortcut must be rechecked.
- **C:** Correct. A shortcut fails for a connection or permission reason more often than for a data reason. In this case: The delegated permission behind the shortcut must be rechecked.
- **D:** Incorrect for this question. The message names the object or the conversion; the plan explains the cost. Why the correct answer wins: The delegated permission behind the shortcut must be rechecked.

### Question 77 — A, D

Answers: Read the T-SQL error message and then the query plan; Check the shortcut connection and the delegated permission. The message names the object, and the shortcut needs its permission checked. The message names the object or the conversion; the plan explains the cost. A shortcut fails for a connection or permission reason more often than for a data reason. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. A shortcut fails for a connection or permission reason more often than for a data reason. In this case: The message names the object, and the shortcut needs its permission checked.
- **B:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The message names the object, and the shortcut needs its permission checked.
- **C:** Incorrect for this question. The failures table records the rejected records and the reason for each. Why the correct answer wins: The message names the object, and the shortcut needs its permission checked.
- **D:** Correct. The message names the object or the conversion; the plan explains the cost. In this case: The message names the object, and the shortcut needs its permission checked.
- **E:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The message names the object, and the shortcut needs its permission checked.

### Question 78 — A

Answer: Partition the table on the date column. Partitioning on the filtered column lets the engine skip files. A partition on the filter column lets the engine skip the rows it does not need. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. A partition on the filter column lets the engine skip the rows it does not need. In this case: Partitioning on the filtered column lets the engine skip files.
- **B:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: Partitioning on the filtered column lets the engine skip files.
- **C:** Incorrect for this question. OPTIMIZE rewrites many small files into fewer larger ones. Why the correct answer wins: Partitioning on the filtered column lets the engine skip files.
- **D:** Incorrect for this question. Z-Order clusters related values so a filtered read touches fewer files. Why the correct answer wins: Partitioning on the filtered column lets the engine skip files.

### Question 79 — D

Answer: Apply Z-Order on the frequently filtered columns. Z-Order clusters the values so the read touches fewer files. Z-Order clusters related values so a filtered read touches fewer files. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. OPTIMIZE rewrites many small files into fewer larger ones. Why the correct answer wins: Z-Order clusters the values so the read touches fewer files.
- **B:** Incorrect for this question. V-Order writes the files in a layout the Fabric engines read faster. Why the correct answer wins: Z-Order clusters the values so the read touches fewer files.
- **C:** Incorrect for this question. A partition on the filter column lets the engine skip the rows it does not need. Why the correct answer wins: Z-Order clusters the values so the read touches fewer files.
- **D:** Correct. Z-Order clusters related values so a filtered read touches fewer files. In this case: Z-Order clusters the values so the read touches fewer files.

### Question 80 — D

Answer: Raise the parallelism of the copy so independent slices move together. Raising the parallelism moves the independent slices together. Independent slices that run one after another waste the capacity the run already has. Local study-map skill 3.9 (Optimizing Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Raising the parallelism moves the independent slices together.
- **B:** Incorrect for this question. Coalesce reduces the file count without a full shuffle. Why the correct answer wins: Raising the parallelism moves the independent slices together.
- **C:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: Raising the parallelism moves the independent slices together.
- **D:** Correct. Independent slices that run one after another waste the capacity the run already has. In this case: Raising the parallelism moves the independent slices together.

### Question 81 — B

Answer: Update statistics so the optimizer sees the current distribution. Statistics are what the optimizer plans from. The warehouse optimizer plans from statistics, not from the data itself. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Statistics are what the optimizer plans from.
- **B:** Correct. The warehouse optimizer plans from statistics, not from the data itself. In this case: Statistics are what the optimizer plans from.
- **C:** Incorrect for this question. Many small files cost more to scan than the same rows in fewer files. Why the correct answer wins: Statistics are what the optimizer plans from.
- **D:** Incorrect for this question. A join on a different column forces a shuffle of both sides. Why the correct answer wins: Statistics are what the optimizer plans from.

### Question 82 — A, B

Answers: Update statistics so the optimizer sees the current distribution; Join on the distribution column so the rows stay on their node. Statistics fix the estimate, and the distribution key removes the reshuffle. The warehouse optimizer plans from statistics, not from the data itself. A join on a different column forces a shuffle of both sides. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. A join on a different column forces a shuffle of both sides. In this case: Statistics fix the estimate, and the distribution key removes the reshuffle.
- **B:** Correct. The warehouse optimizer plans from statistics, not from the data itself. In this case: Statistics fix the estimate, and the distribution key removes the reshuffle.
- **C:** Incorrect for this question. Coalesce reduces the file count without a full shuffle. Why the correct answer wins: Statistics fix the estimate, and the distribution key removes the reshuffle.
- **D:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Statistics fix the estimate, and the distribution key removes the reshuffle.
- **E:** Incorrect for this question. Many small files cost more to scan than the same rows in fewer files. Why the correct answer wins: Statistics fix the estimate, and the distribution key removes the reshuffle.

### Question 83 — D

Answer: Salt the skewed key so the partitions even out. Salting spreads the hot key across partitions. Salting spreads one hot key across several partitions. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Skew handling splits the oversized partition instead of leaving one task to finish alone. Why the correct answer wins: Salting spreads the hot key across partitions.
- **B:** Incorrect for this question. Broadcasting removes the shuffle of the large side of the join. Why the correct answer wins: Salting spreads the hot key across partitions.
- **C:** Incorrect for this question. Adaptive execution re-plans from the actual partition sizes at run time. Why the correct answer wins: Salting spreads the hot key across partitions.
- **D:** Correct. Salting spreads one hot key across several partitions. In this case: Salting spreads the hot key across partitions.

### Question 84 — C

Answer: Broadcast the small dimension to avoid the shuffle. Broadcasting the small side removes the shuffle of the large side. Broadcasting removes the shuffle of the large side of the join. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: Broadcasting the small side removes the shuffle of the large side.
- **B:** Incorrect for this question. Salting spreads one hot key across several partitions. Why the correct answer wins: Broadcasting the small side removes the shuffle of the large side.
- **C:** Correct. Broadcasting removes the shuffle of the large side of the join. In this case: Broadcasting the small side removes the shuffle of the large side.
- **D:** Incorrect for this question. Too few partitions leave large tasks; too many add scheduling overhead. Why the correct answer wins: Broadcasting the small side removes the shuffle of the large side.

### Question 85 — B

Answer: Set the retention policy to match the query window. Retention should match the query window. Retention beyond the query window pays for data nobody reads. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Query throughput is bounded by the eventhouse capacity. Why the correct answer wins: Retention should match the query window.
- **B:** Correct. Retention beyond the query window pays for data nobody reads. In this case: Retention should match the query window.
- **C:** Incorrect for this question. The caching policy keeps the hot window on fast storage. Why the correct answer wins: Retention should match the query window.
- **D:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: Retention should match the query window.

### Question 86 — C

Answer: Read the query plan → reduce the file count → optimize and Z-Order the table → re-measure the query. The plan decides the action and the second measurement proves it. The plan identifies the cost, compaction and clustering address it, and the measurement proves the effect. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The plan is what should have decided whether compaction was the right fix at all. Why the correct answer wins: The plan decides the action and the second measurement proves it.
- **B:** Incorrect for this question. Optimizing before reading the plan optimizes whatever seemed slow rather than what was costly. Why the correct answer wins: The plan decides the action and the second measurement proves it.
- **C:** Correct. The plan identifies the cost, compaction and clustering address it, and the measurement proves the effect. In this case: The plan decides the action and the second measurement proves it.
- **D:** Incorrect for this question. Measuring before the change and again after it is what makes the comparison possible. Why the correct answer wins: The plan decides the action and the second measurement proves it.

### Question 87 — C

Answer: Read the run history → isolate the failing activity → reproduce it with the same input → rerun only the failed activity. The failure is located before anything is rerun. The history identifies the failure, the input reproduces it, and the rerun is scoped to what failed. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The failing activity has to be known before its input can be reproduced. Why the correct answer wins: The failure is located before anything is rerun.
- **B:** Incorrect for this question. Rerunning before reading the history repeats the failure without explaining it. Why the correct answer wins: The failure is located before anything is rerun.
- **C:** Correct. The history identifies the failure, the input reproduces it, and the rerun is scoped to what failed. In this case: The failure is located before anything is rerun.
- **D:** Incorrect for this question. The rerun happens before the cause is reproduced, so the second failure looks like a new one. Why the correct answer wins: The failure is located before anything is rerun.

### Question 88 — C

Answer: Open the Spark UI → find the stage with the skewed task → broadcast or salt the join → re-run and compare the stage time. The UI locates the skew before the join is changed. The UI locates the skew, the join strategy addresses it, and the second run is the evidence. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Salting before locating the skew fixes a guess. Why the correct answer wins: The UI locates the skew before the join is changed.
- **B:** Incorrect for this question. The UI is what does the finding, so it cannot come after it. Why the correct answer wins: The UI locates the skew before the join is changed.
- **C:** Correct. The UI locates the skew, the join strategy addresses it, and the second run is the evidence. In this case: The UI locates the skew before the join is changed.
- **D:** Incorrect for this question. A comparison before any change compares the job with itself. Why the correct answer wins: The UI locates the skew before the join is changed.

### Question 89 — D

Answer: Enable the Apache Airflow job in the workspace and author the DAG. The Airflow job runs the existing DAG inside Fabric. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. Local study-map skill 1.3 (Apache Airflow Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Source-controlled DAGs keep the orchestration reviewable like any other item definition. Why the correct answer wins: The Airflow job runs the existing DAG inside Fabric.
- **B:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: The Airflow job runs the existing DAG inside Fabric.
- **C:** Incorrect for this question. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. Why the correct answer wins: The Airflow job runs the existing DAG inside Fabric.
- **D:** Correct. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. In this case: The Airflow job runs the existing DAG inside Fabric.

### Question 90 — B

Answer: Define a row-level security policy on the table. Row-level security filters the rows per identity. Row-level security filters rows per identity, so one table returns different rows to different users. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: Row-level security filters the rows per identity.
- **B:** Correct. Row-level security filters rows per identity, so one table returns different rows to different users. In this case: Row-level security filters the rows per identity.
- **C:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: Row-level security filters the rows per identity.
- **D:** Incorrect for this question. The predicate must resolve the identity to the region, or every user sees the same rows. Why the correct answer wins: Row-level security filters the rows per identity.

### Question 91 — B

Answer: Apply dynamic data masking to the column. Dynamic data masking masks the value for everyone else. Masking shows a masked value to unauthorised users while the stored data stays intact. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A view removes the column entirely, which is not the same as masking the value. Why the correct answer wins: Dynamic data masking masks the value for everyone else.
- **B:** Correct. Masking shows a masked value to unauthorised users while the stored data stays intact. In this case: Dynamic data masking masks the value for everyone else.
- **C:** Incorrect for this question. A report-level mask protects one visual and leaves every other consumer unmasked. Why the correct answer wins: Dynamic data masking masks the value for everyone else.
- **D:** Incorrect for this question. The masking rule needs the exemption, or the authorised group sees masked values too. Why the correct answer wins: Dynamic data masking masks the value for everyone else.

### Question 92 — D

Answer: Move the workspace to a larger capacity. Capacity units are the ceiling on everything the workspace runs. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Smoothing lets a short burst use the capacity allowance instead of being throttled. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.
- **B:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.
- **C:** Incorrect for this question. The destination throughput caps how much the eventstream can deliver. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.
- **D:** Correct. In this case: Capacity units are the ceiling on everything the workspace runs.

### Question 93 — A

Answer: Enable capacity smoothing so a burst can borrow from the burst allowance. Smoothing lets the burst use the burst allowance. Smoothing lets a short burst use the capacity allowance instead of being throttled. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. Smoothing lets a short burst use the capacity allowance instead of being throttled. In this case: Smoothing lets the burst use the burst allowance.
- **B:** Incorrect for this question. Query throughput is bounded by the eventhouse capacity. Why the correct answer wins: Smoothing lets the burst use the burst allowance.
- **C:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: Smoothing lets the burst use the burst allowance.
- **D:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: Smoothing lets the burst use the burst allowance.

### Question 94 — D

Answer: Run OPTIMIZE to compact the small files. OPTIMIZE compacts the small files into larger ones. OPTIMIZE rewrites many small files into fewer larger ones. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. V-Order writes the files in a layout the Fabric engines read faster. Why the correct answer wins: OPTIMIZE compacts the small files into larger ones.
- **B:** Incorrect for this question. A partition on the filter column lets the engine skip the rows it does not need. Why the correct answer wins: OPTIMIZE compacts the small files into larger ones.
- **C:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: OPTIMIZE compacts the small files into larger ones.
- **D:** Correct. OPTIMIZE rewrites many small files into fewer larger ones. In this case: OPTIMIZE compacts the small files into larger ones.

### Question 95 — D

Answer: Use a Copy activity in the pipeline. A Copy activity moves the rows as one orchestrated step. The Copy activity moves the files or rows as one orchestrated step. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Get Metadata turns an unknown folder into a list the loop can iterate. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.
- **B:** Incorrect for this question. Appending preserves the earlier loads that the incremental pattern depends on. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.
- **C:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.
- **D:** Correct. The Copy activity moves the files or rows as one orchestrated step. In this case: A Copy activity moves the rows as one orchestrated step.

### Question 96 — B

Answer: Deduplicate on the business key and keep the latest record. Deduplication leaves one row per business key. Deduplication makes the target one row per business key. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Reprocessing the partition corrects the aggregate that was already published. Why the correct answer wins: Deduplication leaves one row per business key.
- **B:** Correct. Deduplication makes the target one row per business key. In this case: Deduplication leaves one row per business key.
- **C:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Deduplication leaves one row per business key.
- **D:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Deduplication leaves one row per business key.

### Question 97 — A

Answer: Group and aggregate to the grain the report needs. Grouping to the report grain removes the rows finance discards. Aggregating to the report grain removes rows the report would otherwise discard. Local study-map skill 2.11 (Denormalization, Grouping, and Aggregation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Aggregating to the report grain removes rows the report would otherwise discard. In this case: Grouping to the report grain removes the rows finance discards.
- **B:** Incorrect for this question. Denormalization trades storage for the query shape the report actually uses. Why the correct answer wins: Grouping to the report grain removes the rows finance discards.
- **C:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: Grouping to the report grain removes the rows finance discards.
- **D:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: Grouping to the report grain removes the rows finance discards.

### Question 98 — C

Answer: Use the Monitoring hub for the run history. The Monitoring hub lists every run with its status and duration. The hub lists every run with its status, duration, and owning item. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **B:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **C:** Correct. The hub lists every run with its status, duration, and owning item. In this case: The Monitoring hub lists every run with its status and duration.
- **D:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.

### Question 99 — C

Answer: Configure an alert on the failing condition. A Data Activator rule fires on the streaming condition. An alert turns a silent failure into a notification. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Alerting on success as well as failure trains the team to ignore the alert. Why the correct answer wins: A Data Activator rule fires on the streaming condition.
- **B:** Incorrect for this question. The alert must reach the owner, or it becomes noise nobody acts on. Why the correct answer wins: A Data Activator rule fires on the streaming condition.
- **C:** Correct. An alert turns a silent failure into a notification. In this case: A Data Activator rule fires on the streaming condition.
- **D:** Incorrect for this question. An activator rule evaluates the stream and fires when the condition holds. Why the correct answer wins: A Data Activator rule fires on the streaming condition.

### Question 100 — A

Answer: Increase the eventhouse capacity so the queries keep up. Query throughput is bounded by the eventhouse capacity. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. In this case: Query throughput is bounded by the eventhouse capacity.
- **B:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: Query throughput is bounded by the eventhouse capacity.
- **C:** Incorrect for this question. The caching policy keeps the hot window on fast storage. Why the correct answer wins: Query throughput is bounded by the eventhouse capacity.
- **D:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: Query throughput is bounded by the eventhouse capacity.
