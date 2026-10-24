# Microsoft DP-700 — Full-Length Mock Exam 4

Fabric Data Engineer Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, interactive components in the Fabric portal, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A notebook works today and fails tomorrow because a library resolved to a new version. What should be done?

Domain: Implement and manage an analytics solution

- A. Attach a custom Spark environment to the notebook
- B. Pin the library version in the environment instead of installing it in the notebook
- C. Enable autoscale with a minimum and maximum node count
- D. Set a workspace-level custom Spark pool for the notebooks

### 2. Eight analysts open small notebooks and each waits for a session. What should be enabled?

Domain: Implement and manage an analytics solution

- A. Enable high concurrency mode for shared sessions
- B. Set a workspace-level custom Spark pool for the notebooks
- C. Enable autoscale with a minimum and maximum node count
- D. Enable dynamic allocation so idle executors are released during the run

### 3. Forty trial workspaces must be discovered and governed as one subject area. What should be configured?

Domain: Implement and manage an analytics solution

- A. Create the workspace in the required region at creation time
- B. Assign the workspace to the domain that owns the subject area
- C. Assign the workspace to a capacity that has headroom
- D. Keep OneLake availability enabled so other engines can read the same data

### 4. A science team wants to keep its DAG and let Fabric run it. What should be used?

Domain: Implement and manage an analytics solution

- A. Enable the Apache Airflow job in the workspace and author the DAG
- B. Rewrite the existing orchestration as a Fabric pipeline instead
- C. Use a notebook for the transformation
- D. Sync the Airflow DAG from the connected Git repository

### 5. A DAG must run in Fabric and a fallback is needed if an operator is unsupported. Which two options apply? Select two.

Domain: Implement and manage an analytics solution

- A. Use a pipeline for the copy and the orchestration
- B. Enable the Apache Airflow job in the workspace and author the DAG
- C. Sync the Airflow DAG from the connected Git repository
- D. Rewrite the existing orchestration as a Fabric pipeline instead
- E. Use a notebook for the transformation

### 6. A merge cannot proceed because the workspace and the branch both changed one notebook. What must be done?

Domain: Implement and manage an analytics solution

- A. Resolve the conflict by choosing the definition that must win, then commit
- B. Connect the workspace to a Git repository and commit the item definitions
- C. Add the generated artefacts to the ignore file rather than committing them
- D. Work in a feature branch and merge through a pull request

### 7. The warehouse schema exists only as a series of hand-run scripts. What should be created?

Domain: Implement and manage an analytics solution

- A. Create a database project and deploy the schema from it
- B. Connect the workspace to a Git repository and commit the item definitions
- C. Build the project into a DACPAC and deploy that artefact
- D. Use SQLCMD variables for the environment-specific values

### 8. Twelve researchers need every item in their own workspace. What should be granted?

Domain: Implement and manage an analytics solution

- A. Grant Viewer on the workspace
- B. Share the single item with the user who needs only that item
- C. Grant the user a workspace role
- D. Share a link to the item with the required permission

### 9. An auditor must read everything and a client must read one table. Which two grants apply? Select two.

Domain: Implement and manage an analytics solution

- A. Grant the user a workspace role
- B. Grant Viewer on the workspace
- C. Grant Read on the item
- D. Grant Admin on the workspace to the platform team
- E. Share the single item with the user who needs only that item

### 10. A whole table must be invisible to the engineering role in the model. What should be applied?

Domain: Implement and manage an analytics solution

- A. Apply column-level security so the column is hidden from the group
- B. Grant access at the folder that holds the restricted files
- C. Define a row-level security policy on the table
- D. Apply object-level security in the semantic model

### 11. Two trials share a lakehouse and an engineer must see only the trial they work on. What should be defined?

Domain: Implement and manage an analytics solution

- A. Define a row-level security policy on the table
- B. Filter the table through a predicate that resolves the user to a region
- C. Apply column-level security so the column is hidden from the group
- D. Apply object-level security in the semantic model

### 12. Participant identifiers must stay queryable while analysts see a masked value. What should be applied?

Domain: Implement and manage an analytics solution

- A. Apply dynamic data masking to the column
- B. Apply column-level security so the column is hidden from the group
- C. Mask the column in the report layer only
- D. Expose a view with the column omitted instead of masking it

### 13. The trial nurse can no longer read the identifier after masking was enabled. What is missing?

Domain: Implement and manage an analytics solution

- A. Mask the column in the report layer only
- B. Exempt the authorised group from the mask
- C. Apply dynamic data masking to the column
- D. Expose a view with the column omitted instead of masking it

### 14. Identifiers must be masked for most staff and readable for the nurse. Which two settings apply? Select two.

Domain: Implement and manage an analytics solution

- A. Exempt the authorised group from the mask
- B. Expose a view with the column omitted instead of masking it
- C. Apply dynamic data masking to the column
- D. Apply column-level security so the column is hidden from the group
- E. Mask the column in the report layer only

### 15. Nobody knows which of forty trial tables is the approved one. What should be done?

Domain: Implement and manage an analytics solution

- A. Set the default sensitivity label for the workspace
- B. Promote the item as ready for reuse
- C. Certify the item as the approved source
- D. Apply the sensitivity label to the item

### 16. Clinical data must be classified automatically and keep its class when copied. Which two practices apply? Select two.

Domain: Implement and manage an analytics solution

- A. Certify the item as the approved source
- B. Let the label inherit from the labelled source file
- C. Promote the item as ready for reuse
- D. Apply the sensitivity label to the item
- E. Set the default sensitivity label for the workspace

### 17. A contract requires access evidence for seven years and the log retains ninety days. What should be done?

Domain: Implement and manage an analytics solution

- A. Read the item activity log
- B. Filter the audit log by activity and by item
- C. Export the audit events before the retention window closes
- D. Read the Fabric audit log in the Microsoft Purview portal

### 18. A client asks who opened their trial data last month. Where is the answer recorded?

Domain: Implement and manage an analytics solution

- A. Read the Fabric audit log in the Microsoft Purview portal
- B. Export the audit events before the retention window closes
- C. Read the item activity log
- D. Filter the audit log by activity and by item

### 19. Engineers who are Contributors must still be blocked from one trial folder. What should be configured?

Domain: Implement and manage an analytics solution

- A. Scope the OneLake role to the folder that holds the restricted table
- B. Grant access at the folder that holds the restricted files
- C. Configure OneLake security roles for the lakehouse
- D. Grant the user a workspace role

### 20. One trial folder must be restricted to a named team. Which two settings apply? Select two.

Domain: Implement and manage an analytics solution

- A. Scope the OneLake role to the folder that holds the restricted table
- B. Grant the user a workspace role
- C. Grant the OneLake role to a security group rather than to individuals
- D. Grant access at the folder that holds the restricted files
- E. Configure OneLake security roles for the lakehouse

### 21. Two acquisitions load through a Power Query transform nobody wants to rewrite. What should be used?

Domain: Implement and manage an analytics solution

- A. Use a Dataflow Gen2 for the transformation
- B. Use a pipeline for the copy and the orchestration
- C. Use a notebook for the transformation
- D. Use a T-SQL script against the warehouse

### 22. One trial needs PySpark logic that cannot be expressed in a low-code transform. What should be used?

Domain: Implement and manage an analytics solution

- A. Use a Dataflow Gen2 for the transformation
- B. Use a notebook for the transformation
- C. Use a T-SQL script against the warehouse
- D. Use a pipeline for the copy and the orchestration

### 23. One run must copy files and then apply trial-specific PySpark. Which two items apply? Select two.

Domain: Implement and manage an analytics solution

- A. Use a KQL query against the eventhouse
- B. Use a Dataflow Gen2 for the transformation
- C. Use a pipeline for the copy and the orchestration
- D. Use a notebook for the transformation
- E. Use a T-SQL script against the warehouse

### 24. One notebook template must serve forty trials without being copied. What should be added?

Domain: Implement and manage an analytics solution

- A. Pass the folder path as a pipeline parameter
- B. Look up the stored watermark before the copy
- C. Set the value in a pipeline variable and reference the variable
- D. Build the path with a dynamic expression at run time

### 25. A paused trial must resume loading on a known cadence when it restarts. What should be configured?

Domain: Implement and manage an analytics solution

- A. Add an event-based trigger so the run starts when the file arrives
- B. Trigger on the file-created event for the landing folder
- C. Add a schedule trigger with the cadence and time zone the business expects
- D. Use an Until loop with a timeout for the long-running check

### 26. A workspace must adopt reviewed releases after years of hand exports. Which sequence is correct?

Domain: Implement and manage an analytics solution

- A. Connect the workspace to Git → commit the item definitions → create the deployment pipeline → add deployment rules → promote through the stages
- B. Create the deployment pipeline → connect the workspace to Git → promote through the stages → add deployment rules → commit the definitions
- C. Commit the item definitions → connect the workspace to Git → add deployment rules → create the pipeline → promote the stages
- D. Promote through the stages → create the deployment pipeline → commit the definitions → connect Git → add deployment rules

### 27. Forty trials must share one orchestration template. Which sequence is correct?

Domain: Implement and manage an analytics solution

- A. Parameterise the run → add the notebook activity → build the pipeline → decide the work split
- B. Decide which work is copy, which is orchestration, and which needs PySpark → build the pipeline → add the notebook activity → parameterise the run
- C. Build the pipeline → decide the work split → parameterise the run → add the notebook activity
- D. Add the notebook activity → parameterise the run → decide the work split → build the pipeline

### 28. Corrected transactions arrive after the close and must replace the earlier row. What should be used?

Domain: Ingest and transform data

- A. Load only the rows newer than the stored watermark
- B. Run a full load and overwrite the target
- C. Store the last successful load timestamp in a control table
- D. Merge the incoming rows into the target on the business key

### 29. Twelve franchisees upload daily files and only new files are relevant. What should change?

Domain: Ingest and transform data

- A. Run a full load and overwrite the target
- B. Store the last successful load timestamp in a control table
- C. Route the failed rows to a reject table and continue the load
- D. Load only the rows newer than the stored watermark

### 30. A streaming load restarts and writes the same hour twice. What is missing?

Domain: Ingest and transform data

- A. Set a checkpoint location for the streaming query
- B. Set a watermark so late events are handled deterministically
- C. Query the stream through a OneLake shortcut
- D. Store the stream in native tables in the eventhouse

### 31. Franchisee files arrive in slightly different formats and must be preserved. Where should they land?

Domain: Ingest and transform data

- A. Load the curated model into the warehouse
- B. Write the curated table into the lakehouse Tables area
- C. Store the telemetry in an eventhouse KQL database
- D. Land the extract in the lakehouse Files area

### 32. The royalty calculation needs multi-table transactions. What should hold the model?

Domain: Ingest and transform data

- A. Query the lakehouse through its SQL analytics endpoint
- B. Load the curated model into the warehouse
- C. Land the extract in the lakehouse Files area
- D. Create a KQL database for the time-series queries

### 33. Franchisee files differ in column order and a low-code team must fix them. What should be used?

Domain: Ingest and transform data

- A. Transform with Dataflow Gen2 and Power Query
- B. Transform with KQL in the eventhouse
- C. Transform with T-SQL against the warehouse
- D. Transform with PySpark in a notebook

### 34. The royalty calculation is set-based and the data is already in the warehouse. What should be used?

Domain: Ingest and transform data

- A. Transform with PySpark in a notebook
- B. Transform with T-SQL against the warehouse
- C. Transform with Dataflow Gen2 and Power Query
- D. Transform with KQL in the eventhouse

### 35. One step standardises file layouts and another applies a set-based royalty rule. Which two engines apply? Select two.

Domain: Ingest and transform data

- A. Use a notebook for the transformation
- B. Transform with PySpark in a notebook
- C. Transform with KQL in the eventhouse
- D. Transform with Dataflow Gen2 and Power Query
- E. Transform with T-SQL against the warehouse

### 36. The warehouse must read the lakehouse fact without a second copy. What should be created?

Domain: Ingest and transform data

- A. Use a Copy activity in the pipeline
- B. Copy the remote data into a local table instead of shortcutting it
- C. Create an ADLS Gen2 shortcut to the external container
- D. Create an internal OneLake shortcut to the other lakehouse table

### 37. The raw event files must stay authoritative outside Fabric and must not be duplicated. What should be created?

Domain: Ingest and transform data

- A. Create an ADLS Gen2 shortcut to the external container
- B. Create a shortcut rather than a copy when the source stays authoritative
- C. Create an internal OneLake shortcut to the other lakehouse table
- D. Copy the remote data into a local table instead of shortcutting it

### 38. A franchise operations database must appear in Fabric without a nightly job. What should be enabled?

Domain: Ingest and transform data

- A. Use a Copy activity in the pipeline
- B. Run a full load and overwrite the target
- C. Enable mirroring for the operational database
- D. Create an internal OneLake shortcut to the other lakehouse table

### 39. A daily upload must be moved and then transformed in a fixed order. What should be used?

Domain: Ingest and transform data

- A. Use a Copy activity in the pipeline
- B. Append the new files instead of overwriting the target
- C. Use Get Metadata to list the files to process
- D. Copy the files as binary and parse them downstream

### 40. One franchisee sends a file with three malformed rows every week. What should be done?

Domain: Ingest and transform data

- A. Reprocess the affected partitions when the data arrives late
- B. Route the failed rows to a reject table and continue the load
- C. Replace the missing value with a documented default
- D. Deduplicate on the business key and keep the latest record

### 41. An upload must be moved in order and a bad row must not stop it. Which two practices apply? Select two.

Domain: Ingest and transform data

- A. Route the failed rows to a reject table and continue the load
- B. Append the new files instead of overwriting the target
- C. Use Get Metadata to list the files to process
- D. Use a Copy activity in the pipeline
- E. Copy the files as binary and parse them downstream

### 42. Each title must carry its previous month's loan count on the same row. What should be used?

Domain: Ingest and transform data

- A. Pivot the rows into the reporting columns
- B. Group and aggregate to the grain the report needs
- C. Union the sources after conforming the columns
- D. Use a window function to rank within the partition

### 43. Row-level cleansing across thirty thousand titles and a per-title ranking are needed. Which two features apply? Select two.

Domain: Ingest and transform data

- A. Pivot the rows into the reporting columns
- B. Transform with Dataflow Gen2 and Power Query
- C. Transform with T-SQL against the warehouse
- D. Use a window function to rank within the partition
- E. Transform with PySpark in a notebook

### 44. Reading events from the e-book platform must be summarized as they arrive. What should be used?

Domain: Ingest and transform data

- A. Transform with PySpark in a notebook
- B. Transform with T-SQL against the warehouse
- C. Transform with Dataflow Gen2 and Power Query
- D. Transform with KQL in the eventhouse

### 45. A warehouse dimension needs a merge and the reading events need a window filter. Which two engines apply? Select two.

Domain: Ingest and transform data

- A. Pivot the rows into the reporting columns
- B. Transform with Dataflow Gen2 and Power Query
- C. Transform with PySpark in a notebook
- D. Transform with KQL in the eventhouse
- E. Transform with T-SQL against the warehouse

### 46. A monthly loan report needs one column per month and one row per title. What should be used?

Domain: Ingest and transform data

- A. Denormalize the model so the report needs no join
- B. Union the sources after conforming the columns
- C. Group and aggregate to the grain the report needs
- D. Pivot the rows into the reporting columns

### 47. Six franchisees export the same columns in different orders. What must happen first?

Domain: Ingest and transform data

- A. Pivot the rows into the reporting columns
- B. Group and aggregate to the grain the report needs
- C. Denormalize the model so the report needs no join
- D. Union the sources after conforming the columns

### 48. The same title appears three times with different rights statuses and no version marker. What rule should be applied?

Domain: Ingest and transform data

- A. Replace the missing value with a documented default
- B. Deduplicate on the business key and keep the latest record
- C. Deduplicate on the business key and keep the latest version
- D. Route the failed rows to a reject table and continue the load

### 49. A missing royalty rate is replaced with zero and the monthly average drops. What is wrong with the default?

Domain: Ingest and transform data

- A. Replace the missing value with a documented default
- B. Replace the null with zero before the aggregate
- C. Deduplicate on the business key and keep the latest record
- D. Reprocess the closed window when a late event arrives

### 50. Reading events must reach a KQL table with no code. What should be used?

Domain: Ingest and transform data

- A. Process the stream with Spark structured streaming
- B. Process the stream with an eventstream
- C. Run a batch job every few minutes over the landing folder
- D. Process the stream with a KQL update policy

### 51. One stream reuses batch PySpark and another transforms on arrival. Which two engines apply? Select two.

Domain: Ingest and transform data

- A. Process the stream with a KQL update policy
- B. Process the stream with an eventstream
- C. Set a checkpoint location for the streaming query
- D. Process the stream with Spark structured streaming
- E. Run a batch job every few minutes over the landing folder

### 52. Late corrections arrive up to an hour after the window closes and must be handled deterministically. What should be set?

Domain: Ingest and transform data

- A. Query the stream through a OneLake shortcut
- B. Set a watermark so late events are handled deterministically
- C. Set a checkpoint location for the streaming query
- D. Store the stream in native tables in the eventhouse

### 53. Daily loan totals must be produced for each fixed day. Which window fits?

Domain: Ingest and transform data

- A. Create a materialized view for the repeated aggregation
- B. Use a sliding window that emits when the condition is met
- C. Use a tumbling window for the fixed five-minute aggregate
- D. Use a hopping window when the intervals must overlap

### 54. The same monthly total is recomputed by four reports. What should be created?

Domain: Ingest and transform data

- A. Use a hopping window when the intervals must overlap
- B. Create a materialized view for the repeated aggregation
- C. Use a tumbling window for the fixed five-minute aggregate
- D. Query the stream through a OneLake shortcut

### 55. A catalogue must be modelled with history for a rights dispute. Which sequence is correct?

Domain: Ingest and transform data

- A. Define the grain → add the surrogate keys → load the fact → profile the keys → build the dimensions
- B. Add the surrogate keys → load the fact → define the grain → profile the keys → build the dimensions
- C. Profile the source keys → define the grain of the fact → build the conformed dimensions → add the surrogate keys → load the fact
- D. Load the fact → build the conformed dimensions → profile the source keys → define the grain → add the surrogate keys

### 56. A published total is wrong because of versions and a late correction. Which sequence is correct?

Domain: Ingest and transform data

- A. Decide the surviving record → recompute the aggregate → detect the duplicates → correct the partition
- B. Detect the duplicates and the late rows → decide the surviving record → correct the affected partition → recompute the aggregate
- C. Recompute the aggregate → detect the duplicates → correct the partition → decide the surviving record
- D. Correct the partition → recompute the aggregate → decide the surviving record → detect the duplicates

### 57. Franchisee uploads must become a governed gold table. Which sequence is correct?

Domain: Ingest and transform data

- A. Publish the gold table → validate the schema → land the raw files → conform and deduplicate
- B. Validate the schema → publish the gold table → land the raw files → conform and deduplicate
- C. Conform and deduplicate → land the raw files → publish the gold table → validate the schema
- D. Land the raw files unchanged → validate the schema and reject the bad rows → conform and deduplicate into silver → publish the gold table

### 58. Six franchises' loads must be reviewed after a failed close. Where are the runs listed?

Domain: Monitor and optimize an analytics solution

- A. Read the item activity log
- B. Use the Monitoring hub for the run history
- C. Read the refresh history for the semantic model
- D. Send the logs to a Log Analytics workspace

### 59. One franchise pipeline must be reviewed over the last month. What should be read?

Domain: Monitor and optimize an analytics solution

- A. Read the item activity log
- B. Read the Fabric audit log in the Microsoft Purview portal
- C. Read the refresh history for the semantic model
- D. Use the Monitoring hub for the run history

### 60. A franchise dashboard refreshes late on the first of every month. Where is the pattern visible?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Send the logs to a Log Analytics workspace
- C. Read the refresh history for the semantic model
- D. Read the item activity log

### 61. The team needs a year of refresh history for a review. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Read the refresh history for the semantic model
- B. Read the Fabric audit log in the Microsoft Purview portal
- C. Use the Monitoring hub for the run history
- D. Send the logs to a Log Analytics workspace

### 62. A failed close is discovered when the statement is already late. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Use a Data Activator rule that watches the streaming condition
- B. Alert on every successful run as well as every failure
- C. Configure an alert on the failing condition
- D. Send the alert to the team that owns the item

### 63. A threshold must be evaluated on the incoming order stream. What should be used?

Domain: Monitor and optimize an analytics solution

- A. Alert on every successful run as well as every failure
- B. Build a real-time dashboard over the monitoring table
- C. Configure an alert on the failing condition
- D. Use a Data Activator rule that watches the streaming condition

### 64. A Dataflow Gen2 refresh fails after one franchisee changed a column name. Where is the step named?

Domain: Monitor and optimize an analytics solution

- A. Inspect the Dataflow Gen2 refresh error for the failing query step
- B. Check the shortcut connection and the delegated permission
- C. Check the failing cell and the Spark driver log
- D. Read the activity output of the failed step

### 65. A Copy activity fails and the message names no column. What shows the failing input?

Domain: Monitor and optimize an analytics solution

- A. Read the T-SQL error message and then the query plan
- B. Read the activity output of the failed step
- C. Check the failing cell and the Spark driver log
- D. Inspect the Dataflow Gen2 refresh error for the failing query step

### 66. Bad data reaches the gold layer and the run still reports success. What should be added?

Domain: Monitor and optimize an analytics solution

- A. Add a retry policy with a delay to the failing activity
- B. Set the failure dependency so the handler runs when the step fails
- C. Add an error branch so the failure is handled rather than ignored
- D. Use an Until loop with a timeout for the long-running check

### 67. The royalty notebook fails on one title with no class name. Where is the stack?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Check the failing cell and the Spark driver log
- C. Open the Spark UI for the application
- D. Inspect the failing cell output and exit value

### 68. The notebook reports an executor error that the cell output does not show. Where next?

Domain: Monitor and optimize an analytics solution

- A. Open the Spark UI for the application
- B. Inspect the failing cell output and exit value
- C. Check the failing cell and the Spark driver log
- D. Send the logs to a Log Analytics workspace

### 69. Reading events are rejected after a schema change on the e-book platform. Where are they listed?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Inspect the eventstream runtime metrics
- C. Query the ingestion failures table in the KQL database
- D. Read the Fabric audit log in the Microsoft Purview portal

### 70. A stream loses events and some land malformed. Which two sources apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Read the Fabric audit log in the Microsoft Purview portal
- C. Read the refresh history for the semantic model
- D. Inspect the eventstream runtime metrics
- E. Query the ingestion failures table in the KQL database

### 71. The royalty procedure fails after a column was renamed. What identifies the object?

Domain: Monitor and optimize an analytics solution

- A. Read the T-SQL error message and then the query plan
- B. Check the failing cell and the Spark driver log
- C. Read the activity output of the failed step
- D. Check the shortcut connection and the delegated permission

### 72. A shortcut-backed table returns nothing after a permission change upstream. What should be checked?

Domain: Monitor and optimize an analytics solution

- A. Read the T-SQL error message and then the query plan
- B. Check the failing cell and the Spark driver log
- C. Check the shortcut connection and the delegated permission
- D. Read the activity output of the failed step

### 73. The gold table is read by the warehouse and the endpoint and both reads are slow. What should be enabled?

Domain: Monitor and optimize an analytics solution

- A. Run VACUUM to remove the files the table no longer references
- B. Partition the table on the date column
- C. Enable V-Order on the table
- D. Run OPTIMIZE to compact the small files

### 74. A full rebuild leaves thousands of small files behind. What should be run?

Domain: Monitor and optimize an analytics solution

- A. Partition the table on the date column
- B. Run VACUUM to remove the files the table no longer references
- C. Run OPTIMIZE to compact the small files
- D. Enable V-Order on the table

### 75. A gold table has many small files and slow reads from two engines. Which two actions apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Run VACUUM to remove the files the table no longer references
- B. Partition the table on the date column
- C. Enable V-Order on the table
- D. Run OPTIMIZE to compact the small files
- E. Apply Z-Order on the frequently filtered columns

### 76. Six franchisee folders are copied one after another every night. What should be changed?

Domain: Monitor and optimize an analytics solution

- A. Raise the parallelism of the copy so independent slices move together
- B. Coalesce the partitions before writing the small result
- C. Cache the DataFrame that is used twice
- D. Insert the warehouse rows in batches rather than one at a time

### 77. A small gold result is written as four hundred files. What should be done?

Domain: Monitor and optimize an analytics solution

- A. Set the shuffle partition count to match the data volume
- B. Repartition before the write to control the file count
- C. Cache the DataFrame that is used twice
- D. Coalesce the partitions before writing the small result

### 78. A nightly load is slow to copy and writes too many small files. Which two practices apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Insert the warehouse rows in batches rather than one at a time
- B. Coalesce the partitions before writing the small result
- C. Raise the parallelism of the copy so independent slices move together
- D. Cache the DataFrame that is used twice
- E. Set the shuffle partition count to match the data volume

### 79. The month-end royalty query picks a nested loop after a large load. What should be updated?

Domain: Monitor and optimize an analytics solution

- A. Update statistics so the optimizer sees the current distribution
- B. Insert the warehouse rows in batches rather than one at a time
- C. Join on the distribution column so the rows stay on their node
- D. Write fewer, larger files into the warehouse table

### 80. A franchisee statement is written one row per statement and takes an hour. What should change?

Domain: Monitor and optimize an analytics solution

- A. Update statistics so the optimizer sees the current distribution
- B. Join on the distribution column so the rows stay on their node
- C. Write fewer, larger files into the warehouse table
- D. Insert the warehouse rows in batches rather than one at a time

### 81. A two-gigabyte fact joins a five-thousand-row calendar and the shuffle dominates. What should be done?

Domain: Monitor and optimize an analytics solution

- A. Salt the skewed key so the partitions even out
- B. Cache the DataFrame that is used twice
- C. Broadcast the small dimension to avoid the shuffle
- D. Set the shuffle partition count to match the data volume

### 82. One franchisee sends a fifth of the rows and one task never finishes. What should be enabled?

Domain: Monitor and optimize an analytics solution

- A. Enable skew join handling for the hot key
- B. Broadcast the small dimension to avoid the shuffle
- C. Keep adaptive query execution enabled so the shuffle is re-planned
- D. Salt the skewed key so the partitions even out

### 83. A join shuffles a large table and the shuffle is planned from wrong sizes. Which two features apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Keep adaptive query execution enabled so the shuffle is re-planned
- B. Salt the skewed key so the partitions even out
- C. Set the shuffle partition count to match the data volume
- D. Enable skew join handling for the hot key
- E. Broadcast the small dimension to avoid the shuffle

### 84. All forty trial workspaces throttle together at month end. What should be changed?

Domain: Monitor and optimize an analytics solution

- A. Set the retention policy to match the query window
- B. Move the workspace to a larger capacity
- C. Enable capacity smoothing so a burst can borrow from the burst allowance
- D. Scale the destination throughput for the event volume

### 85. An eventhouse must keep two years and answer one-day queries quickly. Which two settings apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Move the workspace to a larger capacity
- B. Set the caching policy on the KQL table
- C. Set the retention policy to match the query window
- D. Increase the eventhouse capacity so the queries keep up
- E. Scale the destination throughput for the event volume

### 86. A franchise close must be watched instead of chased. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Set the alert threshold → build the dashboard → review the history → enable the output
- B. Build the dashboard → set the threshold → enable the output → review the history
- C. Review the alert history → enable the monitoring output → set the threshold → build the dashboard
- D. Enable the monitoring output → build the dashboard over it → set the alert threshold → review the alert history each week

### 87. A failed franchise load must be corrected and rerun. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Read the run history → isolate the failing activity → reproduce it with the same input → rerun only the failed activity
- B. Isolate the failing activity → rerun the activity → read the run history → reproduce the input
- C. Reproduce the input → isolate the activity → read the run history → rerun the activity
- D. Rerun only the failed activity → read the run history → isolate the activity → reproduce the input

### 88. A royalty query must be made faster and the gain proven. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Optimize the table → re-measure the query → read the plan → reduce the file count
- B. Read the query plan → reduce the file count → optimize and Z-Order the table → re-measure the query
- C. Re-measure the query → optimize the table → read the plan → reduce the file count
- D. Reduce the file count → read the plan → re-measure the query → optimize the table

---

## Case study — Coho Winery

Coho Winery sells to distributors in nine countries and has grown by acquiring three smaller wineries. Each acquisition brought its own workspace, its own naming convention, and its own capacity. The board wants one governed model of shipments, inventory, and distributor orders, and the legal team needs each country data to stay in its own region. The engineering team has adopted Git and deployment pipelines but has not yet assigned workspaces to domains. Two acquisitions still load their data through Dataflow Gen2 that nobody owns, and the audit committee wants to know which items are certified and which are not.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. Three acquisitions sit in workspaces nobody can find. What should be configured?

Domain: Implement and manage an analytics solution

- A. Create the workspace in the required region at creation time
- B. Assign the workspace to the domain that owns the subject area
- C. Assign the workspace to a capacity that has headroom
- D. Keep OneLake availability enabled so other engines can read the same data

### 90. Every release is still an export and an import. What should be created?

Domain: Implement and manage an analytics solution

- A. Add deployment rules so the target stage keeps its own connection and parameters
- B. Compare the stages before promoting
- C. Create a deployment pipeline with development, test, and production stages
- D. Select only the items that belong in the target stage

### 91. The audit committee asks which items are approved. What should be applied?

Domain: Implement and manage an analytics solution

- A. Promote the item as ready for reuse
- B. Apply the sensitivity label to the item
- C. Set the default sensitivity label for the workspace
- D. Certify the item as the approved source

---

## Case study — Fourth Coffee Roasters

Fourth Coffee Roasters franchises 1,400 cafes in six countries. Each franchisee uploads a daily sales file in a slightly different format, and the central team currently fixes the differences by hand. Coffee prices change quarterly, and the royalty calculation must use the price that applied on the transaction date. The finance team needs a monthly statement per franchisee, and the operations team needs a daily exception list of stores that did not upload. The company has a lakehouse and a warehouse, and the data engineering team has asked whether the files should be loaded through pipelines, dataflows, or a notebook.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. A failed daily load is noticed only when a store complains. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Insert the warehouse rows in batches rather than one at a time
- B. Join on the distribution column so the rows stay on their node
- C. Write fewer, larger files into the warehouse table
- D. Update statistics so the optimizer sees the current distribution

### 93. The team must see every franchisee upload and its status. Where should they look?

Domain: Monitor and optimize an analytics solution

- A. Read the item activity log
- B. Use the Monitoring hub for the run history
- C. Read the refresh history for the semantic model
- D. Send the logs to a Log Analytics workspace

### 94. A franchisee that did not upload must be told the same morning. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Send the alert to the team that owns the item
- B. Alert on every successful run as well as every failure
- C. Configure an alert on the failing condition
- D. Use a Data Activator rule that watches the streaming condition

---

## Case study — Nod Publishers

Nod Publishers distributes 30,000 titles to libraries and retailers and tracks reading events from its e-book platform. Events land as JSON in OneLake, and the warehouse holds a title catalogue, a library dimension, and a monthly fact table of loans. The catalogue changes constantly as rights expire and are renewed. The analytics team wants a report that shows loans by title and by the rights status the title had on the loan date. A rights dispute requires the team to reconstruct the catalogue exactly as it stood on a date eighteen months ago. The company also wants to stop copying the raw event files into the warehouse.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. Loans must be attributed to the rights status the title had on the loan date. What should be built?

Domain: Ingest and transform data

- A. Merge the incoming rows into the target on the business key
- B. Generate a surrogate key instead of reusing the source key
- C. Model the data as a star schema with conformed dimensions
- D. Build a type 2 dimension with validity dates and a current flag

### 96. The catalogue and monthly loans must be joined and updated transactionally. What should hold them?

Domain: Ingest and transform data

- A. Load the curated model into the warehouse
- B. Store the telemetry in an eventhouse KQL database
- C. Land the extract in the lakehouse Files area
- D. Query the lakehouse through its SQL analytics endpoint

### 97. The raw event files must be read without another copy. What should be created?

Domain: Ingest and transform data

- A. Copy the remote data into a local table instead of shortcutting it
- B. Create an ADLS Gen2 shortcut to the external container
- C. Use a Copy activity in the pipeline
- D. Create an internal OneLake shortcut to the other lakehouse table

---

## Case study — Trey Research

Trey Research runs clinical trials for pharmaceutical clients and must keep each trial data isolated from every other trial. The data engineering team builds a lakehouse per trial and shares one capacity across forty trials. Each trial defines its own schema, and a trial can be paused and resumed months later. Client contracts require that an engineer working on one trial cannot read another trial data, even accidentally, and that every access is auditable. The team wants to reuse one notebook template across all trials without copying it forty times. A recent audit found a shortcut that exposed one trial folder to the whole engineering workspace.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. A shortcut exposed one trial folder to the whole workspace. What should be configured?

Domain: Implement and manage an analytics solution

- A. Grant the OneLake role to a security group rather than to individuals
- B. Grant access at the folder that holds the restricted files
- C. Scope the OneLake role to the folder that holds the restricted table
- D. Configure OneLake security roles for the lakehouse

### 99. An engineer must see only their own trial rows. What should be defined?

Domain: Implement and manage an analytics solution

- A. Filter the table through a predicate that resolves the user to a region
- B. Apply object-level security in the semantic model
- C. Apply column-level security so the column is hidden from the group
- D. Define a row-level security policy on the table

### 100. Each trial contract requires proof of every access. What records it?

Domain: Implement and manage an analytics solution

- A. Export the audit events before the retention window closes
- B. Read the Fabric audit log in the Microsoft Purview portal
- C. Filter the audit log by activity and by item
- D. Read the item activity log

---

## Answer key and explanations

### Question 1 — B

Answer: Pin the library version in the environment instead of installing it in the notebook. Pinning the version in an environment keeps the run reproducible. An inline install changes the dependency per notebook and makes a run impossible to reproduce. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. An environment carries the library set and Spark properties, so every run starts from the same definition. Why the correct answer wins: Pinning the version in an environment keeps the run reproducible.
- **B:** Correct. An inline install changes the dependency per notebook and makes a run impossible to reproduce. In this case: Pinning the version in an environment keeps the run reproducible.
- **C:** Incorrect for this question. Autoscale adds executors while the job runs and releases them afterwards, so idle capacity is not billed. Why the correct answer wins: Pinning the version in an environment keeps the run reproducible.
- **D:** Incorrect for this question. A workspace Spark pool applies one node size and autoscale bound to every notebook that does not override it. Why the correct answer wins: Pinning the version in an environment keeps the run reproducible.

### Question 2 — A

Answer: Enable high concurrency mode for shared sessions. High concurrency lets them share one session. High concurrency lets several notebooks share one Spark session instead of starting a session each. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. High concurrency lets several notebooks share one Spark session instead of starting a session each. In this case: High concurrency lets them share one session.
- **B:** Incorrect for this question. A workspace Spark pool applies one node size and autoscale bound to every notebook that does not override it. Why the correct answer wins: High concurrency lets them share one session.
- **C:** Incorrect for this question. Autoscale adds executors while the job runs and releases them afterwards, so idle capacity is not billed. Why the correct answer wins: High concurrency lets them share one session.
- **D:** Incorrect for this question. Dynamic allocation shrinks the executor set between stages, which matters when the stages are uneven. Why the correct answer wins: High concurrency lets them share one session.

### Question 3 — B

Answer: Assign the workspace to the domain that owns the subject area. A domain groups the workspaces for governance and discovery. A domain groups workspaces for governance and discovery without moving the data. Local study-map skill 1.2 (Domain and OneLake Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. Why the correct answer wins: A domain groups the workspaces for governance and discovery.
- **B:** Correct. A domain groups workspaces for governance and discovery without moving the data. In this case: A domain groups the workspaces for governance and discovery.
- **C:** Incorrect for this question. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. Why the correct answer wins: A domain groups the workspaces for governance and discovery.
- **D:** Incorrect for this question. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. Why the correct answer wins: A domain groups the workspaces for governance and discovery.

### Question 4 — A

Answer: Enable the Apache Airflow job in the workspace and author the DAG. The Airflow job runs the existing DAG. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. Local study-map skill 1.3 (Apache Airflow Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. In this case: The Airflow job runs the existing DAG.
- **B:** Incorrect for this question. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. Why the correct answer wins: The Airflow job runs the existing DAG.
- **C:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: The Airflow job runs the existing DAG.
- **D:** Incorrect for this question. Source-controlled DAGs keep the orchestration reviewable like any other item definition. Why the correct answer wins: The Airflow job runs the existing DAG.

### Question 5 — B, D

Answers: Enable the Apache Airflow job in the workspace and author the DAG; Rewrite the existing orchestration as a Fabric pipeline instead. The Airflow job runs the DAG, and rewriting as a pipeline is the fallback. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. Local study-map skill 1.3 (Apache Airflow Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: The Airflow job runs the DAG, and rewriting as a pipeline is the fallback.
- **B:** Correct. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. In this case: The Airflow job runs the DAG, and rewriting as a pipeline is the fallback.
- **C:** Incorrect for this question. Source-controlled DAGs keep the orchestration reviewable like any other item definition. Why the correct answer wins: The Airflow job runs the DAG, and rewriting as a pipeline is the fallback.
- **D:** Correct. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. In this case: The Airflow job runs the DAG, and rewriting as a pipeline is the fallback.
- **E:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: The Airflow job runs the DAG, and rewriting as a pipeline is the fallback.

### Question 6 — A

Answer: Resolve the conflict by choosing the definition that must win, then commit. The conflict must be resolved before the workspace can update. An unresolved conflict blocks the update and leaves the workspace and the branch out of step. Local study-map skill 1.4 (Version Control and Database Projects), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. An unresolved conflict blocks the update and leaves the workspace and the branch out of step. In this case: The conflict must be resolved before the workspace can update.
- **B:** Incorrect for this question. Git keeps a reviewable history of every item definition instead of an untracked live workspace. Why the correct answer wins: The conflict must be resolved before the workspace can update.
- **C:** Incorrect for this question. Committing build output makes every run look like a change. Why the correct answer wins: The conflict must be resolved before the workspace can update.
- **D:** Incorrect for this question. Branching keeps unfinished work out of the shared workspace and makes the change reviewable. Why the correct answer wins: The conflict must be resolved before the workspace can update.

### Question 7 — A

Answer: Create a database project and deploy the schema from it. A database project keeps the schema in source control. A database project keeps the warehouse schema in source control and deploys it repeatably. Local study-map skill 1.4 (Version Control and Database Projects), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A database project keeps the warehouse schema in source control and deploys it repeatably. In this case: A database project keeps the schema in source control.
- **B:** Incorrect for this question. Git keeps a reviewable history of every item definition instead of an untracked live workspace. Why the correct answer wins: A database project keeps the schema in source control.
- **C:** Incorrect for this question. The DACPAC is the versioned schema artefact that the deployment consumes. Why the correct answer wins: A database project keeps the schema in source control.
- **D:** Incorrect for this question. SQLCMD variables keep one project artefact deployable to both test and production. Why the correct answer wins: A database project keeps the schema in source control.

### Question 8 — C

Answer: Grant the user a workspace role. A workspace role grants access to every item in it. A workspace role is the coarse grant that every item in the workspace inherits. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Viewer allows reading the items without editing them. Why the correct answer wins: A workspace role grants access to every item in it.
- **B:** Incorrect for this question. Item-level sharing avoids granting a workspace role for one report. Why the correct answer wins: A workspace role grants access to every item in it.
- **C:** Correct. A workspace role is the coarse grant that every item in the workspace inherits. In this case: A workspace role grants access to every item in it.
- **D:** Incorrect for this question. A link is a shortcut to the item, not a substitute for the permission behind it. Why the correct answer wins: A workspace role grants access to every item in it.

### Question 9 — B, C

Answers: Grant Viewer on the workspace; Grant Read on the item. Viewer covers the auditor, and Read on the item covers the client. Viewer allows reading the items without editing them. Read is the narrowest grant that still lets the item be consumed. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: Viewer covers the auditor, and Read on the item covers the client.
- **B:** Correct. Viewer allows reading the items without editing them. In this case: Viewer covers the auditor, and Read on the item covers the client.
- **C:** Correct. Read is the narrowest grant that still lets the item be consumed. In this case: Viewer covers the auditor, and Read on the item covers the client.
- **D:** Incorrect for this question. Admin is needed to manage access and settings, not to read the data. Why the correct answer wins: Viewer covers the auditor, and Read on the item covers the client.
- **E:** Incorrect for this question. Item-level sharing avoids granting a workspace role for one report. Why the correct answer wins: Viewer covers the auditor, and Read on the item covers the client.

### Question 10 — D

Answer: Apply object-level security in the semantic model. Object-level security hides the table from the role. Object-level security hides a table or column from a role in the semantic model. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: Object-level security hides the table from the role.
- **B:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: Object-level security hides the table from the role.
- **C:** Incorrect for this question. Row-level security filters rows per identity, so one table returns different rows to different users. Why the correct answer wins: Object-level security hides the table from the role.
- **D:** Correct. Object-level security hides a table or column from a role in the semantic model. In this case: Object-level security hides the table from the role.

### Question 11 — A

Answer: Define a row-level security policy on the table. Row-level security filters the rows per identity. Row-level security filters rows per identity, so one table returns different rows to different users. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Row-level security filters rows per identity, so one table returns different rows to different users. In this case: Row-level security filters the rows per identity.
- **B:** Incorrect for this question. The predicate must resolve the identity to the region, or every user sees the same rows. Why the correct answer wins: Row-level security filters the rows per identity.
- **C:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: Row-level security filters the rows per identity.
- **D:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: Row-level security filters the rows per identity.

### Question 12 — A

Answer: Apply dynamic data masking to the column. Dynamic data masking masks the value and keeps the table queryable. Masking shows a masked value to unauthorised users while the stored data stays intact. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Masking shows a masked value to unauthorised users while the stored data stays intact. In this case: Dynamic data masking masks the value and keeps the table queryable.
- **B:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: Dynamic data masking masks the value and keeps the table queryable.
- **C:** Incorrect for this question. A report-level mask protects one visual and leaves every other consumer unmasked. Why the correct answer wins: Dynamic data masking masks the value and keeps the table queryable.
- **D:** Incorrect for this question. A view removes the column entirely, which is not the same as masking the value. Why the correct answer wins: Dynamic data masking masks the value and keeps the table queryable.

### Question 13 — B

Answer: Exempt the authorised group from the mask. The authorised group needs the exemption from the mask. The masking rule needs the exemption, or the authorised group sees masked values too. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A report-level mask protects one visual and leaves every other consumer unmasked. Why the correct answer wins: The authorised group needs the exemption from the mask.
- **B:** Correct. The masking rule needs the exemption, or the authorised group sees masked values too. In this case: The authorised group needs the exemption from the mask.
- **C:** Incorrect for this question. Masking shows a masked value to unauthorised users while the stored data stays intact. Why the correct answer wins: The authorised group needs the exemption from the mask.
- **D:** Incorrect for this question. A view removes the column entirely, which is not the same as masking the value. Why the correct answer wins: The authorised group needs the exemption from the mask.

### Question 14 — A, C

Answers: Apply dynamic data masking to the column; Exempt the authorised group from the mask. The mask hides the value, and the exemption restores it for the nurse. Masking shows a masked value to unauthorised users while the stored data stays intact. The masking rule needs the exemption, or the authorised group sees masked values too. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The masking rule needs the exemption, or the authorised group sees masked values too. In this case: The mask hides the value, and the exemption restores it for the nurse.
- **B:** Incorrect for this question. A view removes the column entirely, which is not the same as masking the value. Why the correct answer wins: The mask hides the value, and the exemption restores it for the nurse.
- **C:** Correct. Masking shows a masked value to unauthorised users while the stored data stays intact. In this case: The mask hides the value, and the exemption restores it for the nurse.
- **D:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: The mask hides the value, and the exemption restores it for the nurse.
- **E:** Incorrect for this question. A report-level mask protects one visual and leaves every other consumer unmasked. Why the correct answer wins: The mask hides the value, and the exemption restores it for the nurse.

### Question 15 — C

Answer: Certify the item as the approved source. Certification marks the reviewed, authoritative source. Certification tells consumers the item has been reviewed as authoritative. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A default label classifies new items that nobody labels by hand. Why the correct answer wins: Certification marks the reviewed, authoritative source.
- **B:** Incorrect for this question. Promotion signals readiness without the review that certification implies. Why the correct answer wins: Certification marks the reviewed, authoritative source.
- **C:** Correct. Certification tells consumers the item has been reviewed as authoritative. In this case: Certification marks the reviewed, authoritative source.
- **D:** Incorrect for this question. The label travels with the item and drives the protection downstream consumers inherit. Why the correct answer wins: Certification marks the reviewed, authoritative source.

### Question 16 — D, E

Answers: Apply the sensitivity label to the item; Set the default sensitivity label for the workspace. The default labels new items, and the label follows the copy. The label travels with the item and drives the protection downstream consumers inherit. A default label classifies new items that nobody labels by hand. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Certification tells consumers the item has been reviewed as authoritative. Why the correct answer wins: The default labels new items, and the label follows the copy.
- **B:** Incorrect for this question. Inheritance keeps one classification instead of a second opinion on the same data. Why the correct answer wins: The default labels new items, and the label follows the copy.
- **C:** Incorrect for this question. Promotion signals readiness without the review that certification implies. Why the correct answer wins: The default labels new items, and the label follows the copy.
- **D:** Correct. The label travels with the item and drives the protection downstream consumers inherit. In this case: The default labels new items, and the label follows the copy.
- **E:** Correct. A default label classifies new items that nobody labels by hand. In this case: The default labels new items, and the label follows the copy.

### Question 17 — C

Answer: Export the audit events before the retention window closes. Exporting the events preserves them beyond the retention window. The audit log has a retention window, so an investigation that starts late needs the export. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: Exporting the events preserves them beyond the retention window.
- **B:** Incorrect for this question. Filtering turns a very large log into the events that answer the question. Why the correct answer wins: Exporting the events preserves them beyond the retention window.
- **C:** Correct. The audit log has a retention window, so an investigation that starts late needs the export. In this case: Exporting the events preserves them beyond the retention window.
- **D:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: Exporting the events preserves them beyond the retention window.

### Question 18 — A

Answer: Read the Fabric audit log in the Microsoft Purview portal. The audit log records the identity, the item, and the time. The audit log records who did what to which item and when. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The audit log records who did what to which item and when. In this case: The audit log records the identity, the item, and the time.
- **B:** Incorrect for this question. The audit log has a retention window, so an investigation that starts late needs the export. Why the correct answer wins: The audit log records the identity, the item, and the time.
- **C:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The audit log records the identity, the item, and the time.
- **D:** Incorrect for this question. Filtering turns a very large log into the events that answer the question. Why the correct answer wins: The audit log records the identity, the item, and the time.

### Question 19 — C

Answer: Configure OneLake security roles for the lakehouse. OneLake security governs the data independently of workspace roles. OneLake security governs data access independently of the workspace role. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A folder-scoped role restricts exactly the data rather than the whole lakehouse. Why the correct answer wins: OneLake security governs the data independently of workspace roles.
- **B:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: OneLake security governs the data independently of workspace roles.
- **C:** Correct. OneLake security governs data access independently of the workspace role. In this case: OneLake security governs the data independently of workspace roles.
- **D:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: OneLake security governs the data independently of workspace roles.

### Question 20 — A, C

Answers: Scope the OneLake role to the folder that holds the restricted table; Grant the OneLake role to a security group rather than to individuals. The OneLake role governs the data, and the folder scope limits it. A folder-scoped role restricts exactly the data rather than the whole lakehouse. A group grant is maintained once instead of once per person. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A folder-scoped role restricts exactly the data rather than the whole lakehouse. In this case: The OneLake role governs the data, and the folder scope limits it.
- **B:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: The OneLake role governs the data, and the folder scope limits it.
- **C:** Correct. A group grant is maintained once instead of once per person. In this case: The OneLake role governs the data, and the folder scope limits it.
- **D:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: The OneLake role governs the data, and the folder scope limits it.
- **E:** Incorrect for this question. OneLake security governs data access independently of the workspace role. Why the correct answer wins: The OneLake role governs the data, and the folder scope limits it.

### Question 21 — A

Answer: Use a Dataflow Gen2 for the transformation. A Dataflow Gen2 keeps the transformation that already works. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A Dataflow Gen2 suits a transformation that is expressible in Power Query. In this case: A Dataflow Gen2 keeps the transformation that already works.
- **B:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: A Dataflow Gen2 keeps the transformation that already works.
- **C:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: A Dataflow Gen2 keeps the transformation that already works.
- **D:** Incorrect for this question. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Why the correct answer wins: A Dataflow Gen2 keeps the transformation that already works.

### Question 22 — B

Answer: Use a notebook for the transformation. A notebook is the place for PySpark the low-code engine cannot express. A notebook is the right place for PySpark that a low-code transform cannot express. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: A notebook is the place for PySpark the low-code engine cannot express.
- **B:** Correct. A notebook is the right place for PySpark that a low-code transform cannot express. In this case: A notebook is the place for PySpark the low-code engine cannot express.
- **C:** Incorrect for this question. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Why the correct answer wins: A notebook is the place for PySpark the low-code engine cannot express.
- **D:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: A notebook is the place for PySpark the low-code engine cannot express.

### Question 23 — C, D

Answers: Use a pipeline for the copy and the orchestration; Use a notebook for the transformation. The pipeline owns the copy and the order, and the notebook holds the PySpark. A pipeline owns the scheduling, the copy activity, and the dependency between steps. A notebook is the right place for PySpark that a low-code transform cannot express. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. KQL is the native language of the eventhouse tables. Why the correct answer wins: The pipeline owns the copy and the order, and the notebook holds the PySpark.
- **B:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: The pipeline owns the copy and the order, and the notebook holds the PySpark.
- **C:** Correct. A pipeline owns the scheduling, the copy activity, and the dependency between steps. In this case: The pipeline owns the copy and the order, and the notebook holds the PySpark.
- **D:** Correct. A notebook is the right place for PySpark that a low-code transform cannot express. In this case: The pipeline owns the copy and the order, and the notebook holds the PySpark.
- **E:** Incorrect for this question. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Why the correct answer wins: The pipeline owns the copy and the order, and the notebook holds the PySpark.

### Question 24 — A

Answer: Pass the folder path as a pipeline parameter. A parameter makes one pipeline reusable across trials. A parameter makes one pipeline reusable across folders and environments. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A parameter makes one pipeline reusable across folders and environments. In this case: A parameter makes one pipeline reusable across trials.
- **B:** Incorrect for this question. The lookup is what makes the load incremental rather than a full reload. Why the correct answer wins: A parameter makes one pipeline reusable across trials.
- **C:** Incorrect for this question. A variable carries the computed value between the activities that need it. Why the correct answer wins: A parameter makes one pipeline reusable across trials.
- **D:** Incorrect for this question. A dynamic expression computes the path instead of hard-coding a date. Why the correct answer wins: A parameter makes one pipeline reusable across trials.

### Question 25 — C

Answer: Add a schedule trigger with the cadence and time zone the business expects. A schedule trigger recurs without a person starting the run. The schedule trigger is what makes the run recur without a person starting it. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. An event trigger removes the gap between the file landing and the run starting. Why the correct answer wins: A schedule trigger recurs without a person starting the run.
- **B:** Incorrect for this question. The file-created event is the signal that the extract has finished arriving. Why the correct answer wins: A schedule trigger recurs without a person starting the run.
- **C:** Correct. The schedule trigger is what makes the run recur without a person starting it. In this case: A schedule trigger recurs without a person starting the run.
- **D:** Incorrect for this question. Until repeats the check and stops when the condition is met or the timeout expires. Why the correct answer wins: A schedule trigger recurs without a person starting the run.

### Question 26 — A

Answer: Connect the workspace to Git → commit the item definitions → create the deployment pipeline → add deployment rules → promote through the stages. Definitions are committed before the pipeline promotes them. The definitions have to be in source control before the pipeline promotes them, and the rules are added before the first promotion. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The definitions have to be in source control before the pipeline promotes them, and the rules are added before the first promotion. In this case: Definitions are committed before the pipeline promotes them.
- **B:** Incorrect for this question. Promoting before the definitions are committed and before the rules exist overwrites the target with the wrong settings. Why the correct answer wins: Definitions are committed before the pipeline promotes them.
- **C:** Incorrect for this question. There is nothing to commit before the repository is connected, and the rules belong to a pipeline that does not exist yet. Why the correct answer wins: Definitions are committed before the pipeline promotes them.
- **D:** Incorrect for this question. Every step is in the wrong order: a promotion needs the pipeline, the pipeline needs the definitions in Git, and the rules come first. Why the correct answer wins: Definitions are committed before the pipeline promotes them.

### Question 27 — B

Answer: Decide which work is copy, which is orchestration, and which needs PySpark → build the pipeline → add the notebook activity → parameterise the run. The work split is decided before anything is built or parameterised. The work split decides the items, and the parameter is added once the pipeline has a step to parameterise. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. There is no run to parameterise and no pipeline to hold the activity before either exists. Why the correct answer wins: The work split is decided before anything is built or parameterised.
- **B:** Correct. The work split decides the items, and the parameter is added once the pipeline has a step to parameterise. In this case: The work split is decided before anything is built or parameterised.
- **C:** Incorrect for this question. Building before the split produces the wrong items, and a parameter without the notebook has nothing to drive. Why the correct answer wins: The work split is decided before anything is built or parameterised.
- **D:** Incorrect for this question. The activity needs the pipeline, and the split is the decision that tells you which activities to add. Why the correct answer wins: The work split is decided before anything is built or parameterised.

### Question 28 — D

Answer: Merge the incoming rows into the target on the business key. A merge updates the existing row in place. A merge updates the existing row and inserts the new one in the same step. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. An incremental load moves the delta instead of the history. Why the correct answer wins: A merge updates the existing row in place.
- **B:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: A merge updates the existing row in place.
- **C:** Incorrect for this question. The control table is what lets the next run know where this one stopped. Why the correct answer wins: A merge updates the existing row in place.
- **D:** Correct. A merge updates the existing row and inserts the new one in the same step. In this case: A merge updates the existing row in place.

### Question 29 — D

Answer: Load only the rows newer than the stored watermark. An incremental load moves the delta instead of the history. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: An incremental load moves the delta instead of the history.
- **B:** Incorrect for this question. The control table is what lets the next run know where this one stopped. Why the correct answer wins: An incremental load moves the delta instead of the history.
- **C:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: An incremental load moves the delta instead of the history.
- **D:** Correct. In this case: An incremental load moves the delta instead of the history.

### Question 30 — A

Answer: Set a checkpoint location for the streaming query. The checkpoint records where the stream should resume. The checkpoint is what makes the stream restart from where it stopped. Local study-map skill 2.3 (Streaming Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. The checkpoint is what makes the stream restart from where it stopped. In this case: The checkpoint records where the stream should resume.
- **B:** Incorrect for this question. A watermark sets how long the engine waits for late events before closing a window. Why the correct answer wins: The checkpoint records where the stream should resume.
- **C:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: The checkpoint records where the stream should resume.
- **D:** Incorrect for this question. Native tables give full KQL capability over the streaming data. Why the correct answer wins: The checkpoint records where the stream should resume.

### Question 31 — D

Answer: Land the extract in the lakehouse Files area. The Files area keeps each file as the franchisee sent it. The Files area keeps the raw extract in its original format. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A warehouse gives multi-table T-SQL transactions and a governed relational model. Why the correct answer wins: The Files area keeps each file as the franchisee sent it.
- **B:** Incorrect for this question. A Delta table in Tables is what the SQL analytics endpoint exposes. Why the correct answer wins: The Files area keeps each file as the franchisee sent it.
- **C:** Incorrect for this question. An eventhouse is optimized for high-volume time-series queries. Why the correct answer wins: The Files area keeps each file as the franchisee sent it.
- **D:** Correct. The Files area keeps the raw extract in its original format. In this case: The Files area keeps each file as the franchisee sent it.

### Question 32 — B

Answer: Load the curated model into the warehouse. A warehouse supports the transactional T-SQL the calculation needs. A warehouse gives multi-table T-SQL transactions and a governed relational model. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The endpoint gives read-only T-SQL over the Delta tables without a copy. Why the correct answer wins: A warehouse supports the transactional T-SQL the calculation needs.
- **B:** Correct. A warehouse gives multi-table T-SQL transactions and a governed relational model. In this case: A warehouse supports the transactional T-SQL the calculation needs.
- **C:** Incorrect for this question. The Files area keeps the raw extract in its original format. Why the correct answer wins: A warehouse supports the transactional T-SQL the calculation needs.
- **D:** Incorrect for this question. A KQL database indexes the timestamp column for the range queries the dashboards run. Why the correct answer wins: A warehouse supports the transactional T-SQL the calculation needs.

### Question 33 — A

Answer: Transform with Dataflow Gen2 and Power Query. A Dataflow Gen2 is the low-code engine for that team. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. In this case: A Dataflow Gen2 is the low-code engine for that team.
- **B:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: A Dataflow Gen2 is the low-code engine for that team.
- **C:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: A Dataflow Gen2 is the low-code engine for that team.
- **D:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: A Dataflow Gen2 is the low-code engine for that team.

### Question 34 — B

Answer: Transform with T-SQL against the warehouse. T-SQL is the natural engine for a set-based calculation there. T-SQL is the right engine once the data is relational and already in the warehouse. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: T-SQL is the natural engine for a set-based calculation there.
- **B:** Correct. T-SQL is the right engine once the data is relational and already in the warehouse. In this case: T-SQL is the natural engine for a set-based calculation there.
- **C:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: T-SQL is the natural engine for a set-based calculation there.
- **D:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: T-SQL is the natural engine for a set-based calculation there.

### Question 35 — D, E

Answers: Transform with Dataflow Gen2 and Power Query; Transform with T-SQL against the warehouse. Dataflow Gen2 standardises the layouts, and T-SQL applies the rule. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. T-SQL is the right engine once the data is relational and already in the warehouse. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: Dataflow Gen2 standardises the layouts, and T-SQL applies the rule.
- **B:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: Dataflow Gen2 standardises the layouts, and T-SQL applies the rule.
- **C:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: Dataflow Gen2 standardises the layouts, and T-SQL applies the rule.
- **D:** Correct. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. In this case: Dataflow Gen2 standardises the layouts, and T-SQL applies the rule.
- **E:** Correct. T-SQL is the right engine once the data is relational and already in the warehouse. In this case: Dataflow Gen2 standardises the layouts, and T-SQL applies the rule.

### Question 36 — D

Answer: Create an internal OneLake shortcut to the other lakehouse table. An internal shortcut points at the table without copying it. An internal shortcut points at another Fabric item without copying the data. Local study-map skill 2.6 (OneLake Shortcuts), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: An internal shortcut points at the table without copying it.
- **B:** Incorrect for this question. A copy duplicates the data, so the source of truth is no longer one place. Why the correct answer wins: An internal shortcut points at the table without copying it.
- **C:** Incorrect for this question. The shortcut exposes the external container as if the files were in OneLake. Why the correct answer wins: An internal shortcut points at the table without copying it.
- **D:** Correct. An internal shortcut points at another Fabric item without copying the data. In this case: An internal shortcut points at the table without copying it.

### Question 37 — B

Answer: Create a shortcut rather than a copy when the source stays authoritative. A shortcut has no second copy to keep in step. Local study-map skill 2.6 (OneLake Shortcuts), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The shortcut exposes the external container as if the files were in OneLake. Why the correct answer wins: A shortcut has no second copy to keep in step.
- **B:** Correct. In this case: A shortcut has no second copy to keep in step.
- **C:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: A shortcut has no second copy to keep in step.
- **D:** Incorrect for this question. A copy duplicates the data, so the source of truth is no longer one place. Why the correct answer wins: A shortcut has no second copy to keep in step.

### Question 38 — C

Answer: Enable mirroring for the operational database. Mirroring replicates the tables continuously into OneLake. Mirroring replicates the source tables continuously into OneLake. Local study-map skill 2.7 (Mirroring), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: Mirroring replicates the tables continuously into OneLake.
- **B:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: Mirroring replicates the tables continuously into OneLake.
- **C:** Correct. Mirroring replicates the source tables continuously into OneLake. In this case: Mirroring replicates the tables continuously into OneLake.
- **D:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: Mirroring replicates the tables continuously into OneLake.

### Question 39 — A

Answer: Use a Copy activity in the pipeline. A Copy activity moves the rows as one orchestrated step. The Copy activity moves the files or rows as one orchestrated step. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. The Copy activity moves the files or rows as one orchestrated step. In this case: A Copy activity moves the rows as one orchestrated step.
- **B:** Incorrect for this question. Appending preserves the earlier loads that the incremental pattern depends on. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.
- **C:** Incorrect for this question. Get Metadata turns an unknown folder into a list the loop can iterate. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.
- **D:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: A Copy activity moves the rows as one orchestrated step.

### Question 40 — B

Answer: Route the failed rows to a reject table and continue the load. A reject table preserves the bad rows and lets the load finish. A reject table preserves the bad rows for correction without stopping the load. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Reprocessing the partition corrects the aggregate that was already published. Why the correct answer wins: A reject table preserves the bad rows and lets the load finish.
- **B:** Correct. A reject table preserves the bad rows for correction without stopping the load. In this case: A reject table preserves the bad rows and lets the load finish.
- **C:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: A reject table preserves the bad rows and lets the load finish.
- **D:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: A reject table preserves the bad rows and lets the load finish.

### Question 41 — A, D

Answers: Use a Copy activity in the pipeline; Route the failed rows to a reject table and continue the load. The copy moves the file, and the reject table isolates the bad row. The Copy activity moves the files or rows as one orchestrated step. A reject table preserves the bad rows for correction without stopping the load. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. A reject table preserves the bad rows for correction without stopping the load. In this case: The copy moves the file, and the reject table isolates the bad row.
- **B:** Incorrect for this question. Appending preserves the earlier loads that the incremental pattern depends on. Why the correct answer wins: The copy moves the file, and the reject table isolates the bad row.
- **C:** Incorrect for this question. Get Metadata turns an unknown folder into a list the loop can iterate. Why the correct answer wins: The copy moves the file, and the reject table isolates the bad row.
- **D:** Correct. The Copy activity moves the files or rows as one orchestrated step. In this case: The copy moves the file, and the reject table isolates the bad row.
- **E:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: The copy moves the file, and the reject table isolates the bad row.

### Question 42 — D

Answer: Use a window function to rank within the partition. A window function reads the previous row without collapsing it. A window computes across related rows without collapsing them into one. Local study-map skill 2.9 (PySpark Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: A window function reads the previous row without collapsing it.
- **B:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: A window function reads the previous row without collapsing it.
- **C:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: A window function reads the previous row without collapsing it.
- **D:** Correct. A window computes across related rows without collapsing them into one. In this case: A window function reads the previous row without collapsing it.

### Question 43 — D, E

Answers: Transform with PySpark in a notebook; Use a window function to rank within the partition. PySpark scales the cleansing, and the window function ranks. PySpark handles the row-level and windowed transformations that Spark scales. A window computes across related rows without collapsing them into one. Local study-map skill 2.9 (PySpark Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: PySpark scales the cleansing, and the window function ranks.
- **B:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: PySpark scales the cleansing, and the window function ranks.
- **C:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: PySpark scales the cleansing, and the window function ranks.
- **D:** Correct. A window computes across related rows without collapsing them into one. In this case: PySpark scales the cleansing, and the window function ranks.
- **E:** Correct. PySpark handles the row-level and windowed transformations that Spark scales. In this case: PySpark scales the cleansing, and the window function ranks.

### Question 44 — D

Answer: Transform with KQL in the eventhouse. KQL is the native language for the eventhouse tables. Local study-map skill 2.10 (T-SQL and KQL Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: KQL is the native language for the eventhouse tables.
- **B:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: KQL is the native language for the eventhouse tables.
- **C:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: KQL is the native language for the eventhouse tables.
- **D:** Correct. In this case: KQL is the native language for the eventhouse tables.

### Question 45 — D, E

Answers: Transform with T-SQL against the warehouse; Transform with KQL in the eventhouse. T-SQL performs the merge, and KQL filters the events. T-SQL is the right engine once the data is relational and already in the warehouse. KQL is the native language for the eventhouse tables. Local study-map skill 2.10 (T-SQL and KQL Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: T-SQL performs the merge, and KQL filters the events.
- **B:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: T-SQL performs the merge, and KQL filters the events.
- **C:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: T-SQL performs the merge, and KQL filters the events.
- **D:** Correct. KQL is the native language for the eventhouse tables. In this case: T-SQL performs the merge, and KQL filters the events.
- **E:** Correct. T-SQL is the right engine once the data is relational and already in the warehouse. In this case: T-SQL performs the merge, and KQL filters the events.

### Question 46 — D

Answer: Pivot the rows into the reporting columns. The pivot produces one column per period. The pivot is what produces one column per period the report expects. Local study-map skill 2.11 (Denormalization, Grouping, and Aggregation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Denormalization trades storage for the query shape the report actually uses. Why the correct answer wins: The pivot produces one column per period.
- **B:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: The pivot produces one column per period.
- **C:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: The pivot produces one column per period.
- **D:** Correct. The pivot is what produces one column per period the report expects. In this case: The pivot produces one column per period.

### Question 47 — D

Answer: Union the sources after conforming the columns. The columns must be conformed before the union is valid. Conforming the columns first is what makes the union valid. Local study-map skill 2.11 (Denormalization, Grouping, and Aggregation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: The columns must be conformed before the union is valid.
- **B:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: The columns must be conformed before the union is valid.
- **C:** Incorrect for this question. Denormalization trades storage for the query shape the report actually uses. Why the correct answer wins: The columns must be conformed before the union is valid.
- **D:** Correct. Conforming the columns first is what makes the union valid. In this case: The columns must be conformed before the union is valid.

### Question 48 — C

Answer: Deduplicate on the business key and keep the latest version. Keeping the latest version means the surviving row is the one already used. Keeping the latest version means the surviving row is the one the business already acted on. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Keeping the latest version means the surviving row is the one already used.
- **B:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: Keeping the latest version means the surviving row is the one already used.
- **C:** Correct. Keeping the latest version means the surviving row is the one the business already acted on. In this case: Keeping the latest version means the surviving row is the one already used.
- **D:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Keeping the latest version means the surviving row is the one already used.

### Question 49 — B

Answer: Replace the null with zero before the aggregate. Zero is a value, so it changes an average even when the measure is a sum. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Zero is a value, so it changes an average even when the measure is a sum.
- **B:** Correct. In this case: Zero is a value, so it changes an average even when the measure is a sum.
- **C:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: Zero is a value, so it changes an average even when the measure is a sum.
- **D:** Incorrect for this question. Reprocessing the window is what corrects a total that was already reported. Why the correct answer wins: Zero is a value, so it changes an average even when the measure is a sum.

### Question 50 — B

Answer: Process the stream with an eventstream. An eventstream is the no-code path between source and destination. An eventstream is the no-code path from a source to a destination. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Structured streaming suits stateful processing and the same PySpark logic used in batch. Why the correct answer wins: An eventstream is the no-code path between source and destination.
- **B:** Correct. An eventstream is the no-code path from a source to a destination. In this case: An eventstream is the no-code path between source and destination.
- **C:** Incorrect for this question. A batch job over the landing folder adds latency the streaming requirement may not allow. Why the correct answer wins: An eventstream is the no-code path between source and destination.
- **D:** Incorrect for this question. An update policy transforms the data as it lands in the KQL table. Why the correct answer wins: An eventstream is the no-code path between source and destination.

### Question 51 — A, D

Answers: Process the stream with Spark structured streaming; Process the stream with a KQL update policy. Structured streaming reuses the logic, and the update policy transforms on arrival. Structured streaming suits stateful processing and the same PySpark logic used in batch. An update policy transforms the data as it lands in the KQL table. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. An update policy transforms the data as it lands in the KQL table. In this case: Structured streaming reuses the logic, and the update policy transforms on arrival.
- **B:** Incorrect for this question. An eventstream is the no-code path from a source to a destination. Why the correct answer wins: Structured streaming reuses the logic, and the update policy transforms on arrival.
- **C:** Incorrect for this question. The checkpoint is what makes the stream restart from where it stopped. Why the correct answer wins: Structured streaming reuses the logic, and the update policy transforms on arrival.
- **D:** Correct. Structured streaming suits stateful processing and the same PySpark logic used in batch. In this case: Structured streaming reuses the logic, and the update policy transforms on arrival.
- **E:** Incorrect for this question. A batch job over the landing folder adds latency the streaming requirement may not allow. Why the correct answer wins: Structured streaming reuses the logic, and the update policy transforms on arrival.

### Question 52 — B

Answer: Set a watermark so late events are handled deterministically. A watermark sets how long the engine waits before closing a window. A watermark sets how long the engine waits for late events before closing a window. Local study-map skill 2.14 (Eventstream and Spark Structured Streaming), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: A watermark sets how long the engine waits before closing a window.
- **B:** Correct. A watermark sets how long the engine waits for late events before closing a window. In this case: A watermark sets how long the engine waits before closing a window.
- **C:** Incorrect for this question. The checkpoint is what makes the stream restart from where it stopped. Why the correct answer wins: A watermark sets how long the engine waits before closing a window.
- **D:** Incorrect for this question. Native tables give full KQL capability over the streaming data. Why the correct answer wins: A watermark sets how long the engine waits before closing a window.

### Question 53 — C

Answer: Use a tumbling window for the fixed five-minute aggregate. A tumbling window covers fixed, non-overlapping intervals. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A materialized view keeps the aggregate fresh instead of recomputing it per query. Why the correct answer wins: A tumbling window covers fixed, non-overlapping intervals.
- **B:** Incorrect for this question. A sliding window emits on the event that satisfies the condition rather than on a fixed boundary. Why the correct answer wins: A tumbling window covers fixed, non-overlapping intervals.
- **C:** Correct. In this case: A tumbling window covers fixed, non-overlapping intervals.
- **D:** Incorrect for this question. A hopping window covers overlapping intervals so a trend can be smoothed. Why the correct answer wins: A tumbling window covers fixed, non-overlapping intervals.

### Question 54 — B

Answer: Create a materialized view for the repeated aggregation. A materialized view keeps the aggregate fresh for every consumer. A materialized view keeps the aggregate fresh instead of recomputing it per query. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A hopping window covers overlapping intervals so a trend can be smoothed. Why the correct answer wins: A materialized view keeps the aggregate fresh for every consumer.
- **B:** Correct. A materialized view keeps the aggregate fresh instead of recomputing it per query. In this case: A materialized view keeps the aggregate fresh for every consumer.
- **C:** Incorrect for this question. A tumbling window covers fixed, non-overlapping intervals. Why the correct answer wins: A materialized view keeps the aggregate fresh for every consumer.
- **D:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: A materialized view keeps the aggregate fresh for every consumer.

### Question 55 — C

Answer: Profile the source keys → define the grain of the fact → build the conformed dimensions → add the surrogate keys → load the fact. Keys are profiled before the grain, the dimensions, and the fact. Profiling the keys settles the grain, the grain settles the dimensions, and the fact loads against the keys those dimensions own. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The keys are profiled and the dimensions built before the fact can be loaded. Why the correct answer wins: Keys are profiled before the grain, the dimensions, and the fact.
- **B:** Incorrect for this question. Surrogate keys are assigned by the dimensions, which do not exist yet. Why the correct answer wins: Keys are profiled before the grain, the dimensions, and the fact.
- **C:** Correct. Profiling the keys settles the grain, the grain settles the dimensions, and the fact loads against the keys those dimensions own. In this case: Keys are profiled before the grain, the dimensions, and the fact.
- **D:** Incorrect for this question. The fact is loaded before the keys it references exist. Why the correct answer wins: Keys are profiled before the grain, the dimensions, and the fact.

### Question 56 — B

Answer: Detect the duplicates and the late rows → decide the surviving record → correct the affected partition → recompute the aggregate. Detection and the survivor rule precede correction and recompute. The detection comes first, the rule decides the survivor, the partition is corrected, and only then is the published total recomputed. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A rule chosen before the duplicates are known is chosen blind. Why the correct answer wins: Detection and the survivor rule precede correction and recompute.
- **B:** Correct. The detection comes first, the rule decides the survivor, the partition is corrected, and only then is the published total recomputed. In this case: Detection and the survivor rule precede correction and recompute.
- **C:** Incorrect for this question. Recomputing before the data is corrected republishes the same wrong total. Why the correct answer wins: Detection and the survivor rule precede correction and recompute.
- **D:** Incorrect for this question. The partition cannot be corrected before the rule decides which record survives. Why the correct answer wins: Detection and the survivor rule precede correction and recompute.

### Question 57 — D

Answer: Land the raw files unchanged → validate the schema and reject the bad rows → conform and deduplicate into silver → publish the gold table. Landing and validation precede conformity and publication. Raw data is preserved, validation happens before any transformation hides a problem, and the curated table is the last thing published. Local study-map skill 2.2 (Dimensional Model Preparation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The published table would be rebuilt from data that has not landed yet. Why the correct answer wins: Landing and validation precede conformity and publication.
- **B:** Incorrect for this question. There is nothing to validate and nothing to publish before the raw files exist. Why the correct answer wins: Landing and validation precede conformity and publication.
- **C:** Incorrect for this question. Conforming before the raw data lands transforms whatever was already there, and validation after publication is too late. Why the correct answer wins: Landing and validation precede conformity and publication.
- **D:** Correct. Raw data is preserved, validation happens before any transformation hides a problem, and the curated table is the last thing published. In this case: Landing and validation precede conformity and publication.

### Question 58 — B

Answer: Use the Monitoring hub for the run history. The Monitoring hub lists every run with its status and duration. The hub lists every run with its status, duration, and owning item. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **B:** Correct. The hub lists every run with its status, duration, and owning item. In this case: The Monitoring hub lists every run with its status and duration.
- **C:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **D:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.

### Question 59 — A

Answer: Read the item activity log. The item activity log covers that item's runs. The activity log records the runs of one item with their outcomes. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The activity log records the runs of one item with their outcomes. In this case: The item activity log covers that item's runs.
- **B:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The item activity log covers that item's runs.
- **C:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The item activity log covers that item's runs.
- **D:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The item activity log covers that item's runs.

### Question 60 — C

Answer: Read the refresh history for the semantic model. The refresh history records each attempt and its duration. The refresh history separates a failed refresh from a slow one. Local study-map skill 3.2 (Monitoring Semantic Model Refresh), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The refresh history records each attempt and its duration.
- **B:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The refresh history records each attempt and its duration.
- **C:** Correct. The refresh history separates a failed refresh from a slow one. In this case: The refresh history records each attempt and its duration.
- **D:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The refresh history records each attempt and its duration.

### Question 61 — D

Answer: Send the logs to a Log Analytics workspace. Log Analytics retains what the in-product views expire. Log Analytics keeps the history that the in-product views expire. Local study-map skill 3.2 (Monitoring Semantic Model Refresh), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: Log Analytics retains what the in-product views expire.
- **B:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: Log Analytics retains what the in-product views expire.
- **C:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: Log Analytics retains what the in-product views expire.
- **D:** Correct. Log Analytics keeps the history that the in-product views expire. In this case: Log Analytics retains what the in-product views expire.

### Question 62 — C

Answer: Configure an alert on the failing condition. An alert turns the silent failure into a notification. An alert turns a silent failure into a notification. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. An activator rule evaluates the stream and fires when the condition holds. Why the correct answer wins: An alert turns the silent failure into a notification.
- **B:** Incorrect for this question. Alerting on success as well as failure trains the team to ignore the alert. Why the correct answer wins: An alert turns the silent failure into a notification.
- **C:** Correct. An alert turns a silent failure into a notification. In this case: An alert turns the silent failure into a notification.
- **D:** Incorrect for this question. The alert must reach the owner, or it becomes noise nobody acts on. Why the correct answer wins: An alert turns the silent failure into a notification.

### Question 63 — D

Answer: Use a Data Activator rule that watches the streaming condition. A Data Activator rule evaluates the streaming condition. An activator rule evaluates the stream and fires when the condition holds. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Alerting on success as well as failure trains the team to ignore the alert. Why the correct answer wins: A Data Activator rule evaluates the streaming condition.
- **B:** Incorrect for this question. A dashboard over the monitoring table makes the trend visible between runs. Why the correct answer wins: A Data Activator rule evaluates the streaming condition.
- **C:** Incorrect for this question. An alert turns a silent failure into a notification. Why the correct answer wins: A Data Activator rule evaluates the streaming condition.
- **D:** Correct. An activator rule evaluates the stream and fires when the condition holds. In this case: A Data Activator rule evaluates the streaming condition.

### Question 64 — A

Answer: Inspect the Dataflow Gen2 refresh error for the failing query step. The refresh error names the query step that diverged. The refresh error names the step, which is where the transform diverged. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The refresh error names the step, which is where the transform diverged. In this case: The refresh error names the query step that diverged.
- **B:** Incorrect for this question. A shortcut fails for a connection or permission reason more often than for a data reason. Why the correct answer wins: The refresh error names the query step that diverged.
- **C:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The refresh error names the query step that diverged.
- **D:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The refresh error names the query step that diverged.

### Question 65 — B

Answer: Read the activity output of the failed step. The activity output carries the error and its input. The activity output carries the error and the input that produced it. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The message names the object or the conversion; the plan explains the cost. Why the correct answer wins: The activity output carries the error and its input.
- **B:** Correct. The activity output carries the error and the input that produced it. In this case: The activity output carries the error and its input.
- **C:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The activity output carries the error and its input.
- **D:** Incorrect for this question. The refresh error names the step, which is where the transform diverged. Why the correct answer wins: The activity output carries the error and its input.

### Question 66 — C

Answer: Add an error branch so the failure is handled rather than ignored. An error branch turns a silent failure into an explicit outcome. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. A retry absorbs a transient failure that the next attempt would not repeat. Why the correct answer wins: An error branch turns a silent failure into an explicit outcome.
- **B:** Incorrect for this question. The dependency is what makes the failure path execute at all. Why the correct answer wins: An error branch turns a silent failure into an explicit outcome.
- **C:** Correct. In this case: An error branch turns a silent failure into an explicit outcome.
- **D:** Incorrect for this question. Until repeats the check and stops when the condition is met or the timeout expires. Why the correct answer wins: An error branch turns a silent failure into an explicit outcome.

### Question 67 — D

Answer: Inspect the failing cell output and exit value. The failing cell's output reports the exception with its stack. The cell output is where the exception is reported with its stack. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The failing cell's output reports the exception with its stack.
- **B:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The failing cell's output reports the exception with its stack.
- **C:** Incorrect for this question. The Spark UI shows the stages and tasks where the time went. Why the correct answer wins: The failing cell's output reports the exception with its stack.
- **D:** Correct. The cell output is where the exception is reported with its stack. In this case: The failing cell's output reports the exception with its stack.

### Question 68 — C

Answer: Check the failing cell and the Spark driver log. The driver log carries the errors the cell output omits. The driver log carries the executor and serialization errors the cell output omits. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The Spark UI shows the stages and tasks where the time went. Why the correct answer wins: The driver log carries the errors the cell output omits.
- **B:** Incorrect for this question. The cell output is where the exception is reported with its stack. Why the correct answer wins: The driver log carries the errors the cell output omits.
- **C:** Correct. The driver log carries the executor and serialization errors the cell output omits. In this case: The driver log carries the errors the cell output omits.
- **D:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The driver log carries the errors the cell output omits.

### Question 69 — C

Answer: Query the ingestion failures table in the KQL database. The ingestion failures table records each rejected record. The failures table records the rejected records and the reason for each. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The ingestion failures table records each rejected record.
- **B:** Incorrect for this question. The runtime metrics show whether the source or the destination is blocking. Why the correct answer wins: The ingestion failures table records each rejected record.
- **C:** Correct. The failures table records the rejected records and the reason for each. In this case: The ingestion failures table records each rejected record.
- **D:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The ingestion failures table records each rejected record.

### Question 70 — D, E

Answers: Query the ingestion failures table in the KQL database; Inspect the eventstream runtime metrics. The metrics show the gap, and the failures table shows the records. The failures table records the rejected records and the reason for each. The runtime metrics show whether the source or the destination is blocking. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The metrics show the gap, and the failures table shows the records.
- **B:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The metrics show the gap, and the failures table shows the records.
- **C:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The metrics show the gap, and the failures table shows the records.
- **D:** Correct. The runtime metrics show whether the source or the destination is blocking. In this case: The metrics show the gap, and the failures table shows the records.
- **E:** Correct. The failures table records the rejected records and the reason for each. In this case: The metrics show the gap, and the failures table shows the records.

### Question 71 — A

Answer: Read the T-SQL error message and then the query plan. The T-SQL message names the object or the conversion. The message names the object or the conversion; the plan explains the cost. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The message names the object or the conversion; the plan explains the cost. In this case: The T-SQL message names the object or the conversion.
- **B:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The T-SQL message names the object or the conversion.
- **C:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The T-SQL message names the object or the conversion.
- **D:** Incorrect for this question. A shortcut fails for a connection or permission reason more often than for a data reason. Why the correct answer wins: The T-SQL message names the object or the conversion.

### Question 72 — C

Answer: Check the shortcut connection and the delegated permission. The delegated permission behind the shortcut must be rechecked. A shortcut fails for a connection or permission reason more often than for a data reason. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The message names the object or the conversion; the plan explains the cost. Why the correct answer wins: The delegated permission behind the shortcut must be rechecked.
- **B:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The delegated permission behind the shortcut must be rechecked.
- **C:** Correct. A shortcut fails for a connection or permission reason more often than for a data reason. In this case: The delegated permission behind the shortcut must be rechecked.
- **D:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The delegated permission behind the shortcut must be rechecked.

### Question 73 — C

Answer: Enable V-Order on the table. V-Order writes the files in the layout the Fabric engines read fastest. V-Order writes the files in a layout the Fabric engines read faster. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: V-Order writes the files in the layout the Fabric engines read fastest.
- **B:** Incorrect for this question. A partition on the filter column lets the engine skip the rows it does not need. Why the correct answer wins: V-Order writes the files in the layout the Fabric engines read fastest.
- **C:** Correct. V-Order writes the files in a layout the Fabric engines read faster. In this case: V-Order writes the files in the layout the Fabric engines read fastest.
- **D:** Incorrect for this question. OPTIMIZE rewrites many small files into fewer larger ones. Why the correct answer wins: V-Order writes the files in the layout the Fabric engines read fastest.

### Question 74 — C

Answer: Run OPTIMIZE to compact the small files. OPTIMIZE compacts the small files into larger ones. OPTIMIZE rewrites many small files into fewer larger ones. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. A partition on the filter column lets the engine skip the rows it does not need. Why the correct answer wins: OPTIMIZE compacts the small files into larger ones.
- **B:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: OPTIMIZE compacts the small files into larger ones.
- **C:** Correct. OPTIMIZE rewrites many small files into fewer larger ones. In this case: OPTIMIZE compacts the small files into larger ones.
- **D:** Incorrect for this question. V-Order writes the files in a layout the Fabric engines read faster. Why the correct answer wins: OPTIMIZE compacts the small files into larger ones.

### Question 75 — C, D

Answers: Run OPTIMIZE to compact the small files; Enable V-Order on the table. Compaction fixes the file count, and V-Order fixes the read layout. OPTIMIZE rewrites many small files into fewer larger ones. V-Order writes the files in a layout the Fabric engines read faster. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: Compaction fixes the file count, and V-Order fixes the read layout.
- **B:** Incorrect for this question. A partition on the filter column lets the engine skip the rows it does not need. Why the correct answer wins: Compaction fixes the file count, and V-Order fixes the read layout.
- **C:** Correct. V-Order writes the files in a layout the Fabric engines read faster. In this case: Compaction fixes the file count, and V-Order fixes the read layout.
- **D:** Correct. OPTIMIZE rewrites many small files into fewer larger ones. In this case: Compaction fixes the file count, and V-Order fixes the read layout.
- **E:** Incorrect for this question. Z-Order clusters related values so a filtered read touches fewer files. Why the correct answer wins: Compaction fixes the file count, and V-Order fixes the read layout.

### Question 76 — A

Answer: Raise the parallelism of the copy so independent slices move together. Raising the parallelism moves the independent slices together. Independent slices that run one after another waste the capacity the run already has. Local study-map skill 3.9 (Optimizing Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. Independent slices that run one after another waste the capacity the run already has. In this case: Raising the parallelism moves the independent slices together.
- **B:** Incorrect for this question. Coalesce reduces the file count without a full shuffle. Why the correct answer wins: Raising the parallelism moves the independent slices together.
- **C:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: Raising the parallelism moves the independent slices together.
- **D:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Raising the parallelism moves the independent slices together.

### Question 77 — D

Answer: Coalesce the partitions before writing the small result. Coalesce reduces the file count without a full shuffle. Local study-map skill 3.9 (Optimizing Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Too few partitions leave large tasks; too many add scheduling overhead. Why the correct answer wins: Coalesce reduces the file count without a full shuffle.
- **B:** Incorrect for this question. Repartitioning decides how many files the write produces. Why the correct answer wins: Coalesce reduces the file count without a full shuffle.
- **C:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: Coalesce reduces the file count without a full shuffle.
- **D:** Correct. In this case: Coalesce reduces the file count without a full shuffle.

### Question 78 — B, C

Answers: Raise the parallelism of the copy so independent slices move together; Coalesce the partitions before writing the small result. More parallelism moves the copies together, and coalesce reduces the files. Independent slices that run one after another waste the capacity the run already has. Coalesce reduces the file count without a full shuffle. Local study-map skill 3.9 (Optimizing Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: More parallelism moves the copies together, and coalesce reduces the files.
- **B:** Correct. Coalesce reduces the file count without a full shuffle. In this case: More parallelism moves the copies together, and coalesce reduces the files.
- **C:** Correct. Independent slices that run one after another waste the capacity the run already has. In this case: More parallelism moves the copies together, and coalesce reduces the files.
- **D:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: More parallelism moves the copies together, and coalesce reduces the files.
- **E:** Incorrect for this question. Too few partitions leave large tasks; too many add scheduling overhead. Why the correct answer wins: More parallelism moves the copies together, and coalesce reduces the files.

### Question 79 — A

Answer: Update statistics so the optimizer sees the current distribution. Statistics are what the optimizer plans from. The warehouse optimizer plans from statistics, not from the data itself. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The warehouse optimizer plans from statistics, not from the data itself. In this case: Statistics are what the optimizer plans from.
- **B:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Statistics are what the optimizer plans from.
- **C:** Incorrect for this question. A join on a different column forces a shuffle of both sides. Why the correct answer wins: Statistics are what the optimizer plans from.
- **D:** Incorrect for this question. Many small files cost more to scan than the same rows in fewer files. Why the correct answer wins: Statistics are what the optimizer plans from.

### Question 80 — D

Answer: Insert the warehouse rows in batches rather than one at a time. Batched inserts stop paying the transaction overhead per row. Row-by-row inserts pay the transaction overhead once per row. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The warehouse optimizer plans from statistics, not from the data itself. Why the correct answer wins: Batched inserts stop paying the transaction overhead per row.
- **B:** Incorrect for this question. A join on a different column forces a shuffle of both sides. Why the correct answer wins: Batched inserts stop paying the transaction overhead per row.
- **C:** Incorrect for this question. Many small files cost more to scan than the same rows in fewer files. Why the correct answer wins: Batched inserts stop paying the transaction overhead per row.
- **D:** Correct. Row-by-row inserts pay the transaction overhead once per row. In this case: Batched inserts stop paying the transaction overhead per row.

### Question 81 — C

Answer: Broadcast the small dimension to avoid the shuffle. Broadcasting the small side removes the shuffle of the large side. Broadcasting removes the shuffle of the large side of the join. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Salting spreads one hot key across several partitions. Why the correct answer wins: Broadcasting the small side removes the shuffle of the large side.
- **B:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: Broadcasting the small side removes the shuffle of the large side.
- **C:** Correct. Broadcasting removes the shuffle of the large side of the join. In this case: Broadcasting the small side removes the shuffle of the large side.
- **D:** Incorrect for this question. Too few partitions leave large tasks; too many add scheduling overhead. Why the correct answer wins: Broadcasting the small side removes the shuffle of the large side.

### Question 82 — A

Answer: Enable skew join handling for the hot key. Skew handling splits the oversized partition. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. In this case: Skew handling splits the oversized partition.
- **B:** Incorrect for this question. Broadcasting removes the shuffle of the large side of the join. Why the correct answer wins: Skew handling splits the oversized partition.
- **C:** Incorrect for this question. Adaptive execution re-plans from the actual partition sizes at run time. Why the correct answer wins: Skew handling splits the oversized partition.
- **D:** Incorrect for this question. Salting spreads one hot key across several partitions. Why the correct answer wins: Skew handling splits the oversized partition.

### Question 83 — A, E

Answers: Broadcast the small dimension to avoid the shuffle; Keep adaptive query execution enabled so the shuffle is re-planned. The broadcast removes the shuffle, and adaptive execution re-plans it. Broadcasting removes the shuffle of the large side of the join. Adaptive execution re-plans from the actual partition sizes at run time. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. Adaptive execution re-plans from the actual partition sizes at run time. In this case: The broadcast removes the shuffle, and adaptive execution re-plans it.
- **B:** Incorrect for this question. Salting spreads one hot key across several partitions. Why the correct answer wins: The broadcast removes the shuffle, and adaptive execution re-plans it.
- **C:** Incorrect for this question. Too few partitions leave large tasks; too many add scheduling overhead. Why the correct answer wins: The broadcast removes the shuffle, and adaptive execution re-plans it.
- **D:** Incorrect for this question. Skew handling splits the oversized partition instead of leaving one task to finish alone. Why the correct answer wins: The broadcast removes the shuffle, and adaptive execution re-plans it.
- **E:** Correct. Broadcasting removes the shuffle of the large side of the join. In this case: The broadcast removes the shuffle, and adaptive execution re-plans it.

### Question 84 — B

Answer: Move the workspace to a larger capacity. Capacity units are the ceiling on everything the workspaces run. Capacity units are the ceiling on everything the workspace runs. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: Capacity units are the ceiling on everything the workspaces run.
- **B:** Correct. Capacity units are the ceiling on everything the workspace runs. In this case: Capacity units are the ceiling on everything the workspaces run.
- **C:** Incorrect for this question. Smoothing lets a short burst use the capacity allowance instead of being throttled. Why the correct answer wins: Capacity units are the ceiling on everything the workspaces run.
- **D:** Incorrect for this question. The destination throughput caps how much the eventstream can deliver. Why the correct answer wins: Capacity units are the ceiling on everything the workspaces run.

### Question 85 — B, C

Answers: Set the retention policy to match the query window; Set the caching policy on the KQL table. Retention controls the history, and caching keeps the hot window fast. Retention beyond the query window pays for data nobody reads. The caching policy keeps the hot window on fast storage. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: Retention controls the history, and caching keeps the hot window fast.
- **B:** Correct. The caching policy keeps the hot window on fast storage. In this case: Retention controls the history, and caching keeps the hot window fast.
- **C:** Correct. Retention beyond the query window pays for data nobody reads. In this case: Retention controls the history, and caching keeps the hot window fast.
- **D:** Incorrect for this question. Query throughput is bounded by the eventhouse capacity. Why the correct answer wins: Retention controls the history, and caching keeps the hot window fast.
- **E:** Incorrect for this question. The destination throughput caps how much the eventstream can deliver. Why the correct answer wins: Retention controls the history, and caching keeps the hot window fast.

### Question 86 — D

Answer: Enable the monitoring output → build the dashboard over it → set the alert threshold → review the alert history each week. The output exists before the dashboard and the alert. There is nothing to chart or alert on until the output exists, and the review is what keeps the threshold honest. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. A threshold with no output behind it cannot be evaluated. Why the correct answer wins: The output exists before the dashboard and the alert.
- **B:** Incorrect for this question. The dashboard and the threshold both read an output that does not exist yet. Why the correct answer wins: The output exists before the dashboard and the alert.
- **C:** Incorrect for this question. There is no alert history before the alert exists. Why the correct answer wins: The output exists before the dashboard and the alert.
- **D:** Correct. There is nothing to chart or alert on until the output exists, and the review is what keeps the threshold honest. In this case: The output exists before the dashboard and the alert.

### Question 87 — A

Answer: Read the run history → isolate the failing activity → reproduce it with the same input → rerun only the failed activity. The failure is located before anything is rerun. The history identifies the failure, the input reproduces it, and the rerun is scoped to what failed. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The history identifies the failure, the input reproduces it, and the rerun is scoped to what failed. In this case: The failure is located before anything is rerun.
- **B:** Incorrect for this question. The rerun happens before the cause is reproduced, so the second failure looks like a new one. Why the correct answer wins: The failure is located before anything is rerun.
- **C:** Incorrect for this question. The failing activity has to be known before its input can be reproduced. Why the correct answer wins: The failure is located before anything is rerun.
- **D:** Incorrect for this question. Rerunning before reading the history repeats the failure without explaining it. Why the correct answer wins: The failure is located before anything is rerun.

### Question 88 — B

Answer: Read the query plan → reduce the file count → optimize and Z-Order the table → re-measure the query. The plan decides the action and the second measurement proves the effect. The plan identifies the cost, compaction and clustering address it, and the measurement proves the effect. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The plan is what should have decided whether compaction was the right fix at all. Why the correct answer wins: The plan decides the action and the second measurement proves the effect.
- **B:** Correct. The plan identifies the cost, compaction and clustering address it, and the measurement proves the effect. In this case: The plan decides the action and the second measurement proves the effect.
- **C:** Incorrect for this question. Optimizing before reading the plan optimizes whatever seemed slow rather than what was costly. Why the correct answer wins: The plan decides the action and the second measurement proves the effect.
- **D:** Incorrect for this question. Measuring before the change and again after it is what makes the comparison possible. Why the correct answer wins: The plan decides the action and the second measurement proves the effect.

### Question 89 — B

Answer: Assign the workspace to the domain that owns the subject area. A domain groups the workspaces by subject area. A domain groups workspaces for governance and discovery without moving the data. Local study-map skill 1.2 (Domain and OneLake Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. Why the correct answer wins: A domain groups the workspaces by subject area.
- **B:** Correct. A domain groups workspaces for governance and discovery without moving the data. In this case: A domain groups the workspaces by subject area.
- **C:** Incorrect for this question. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. Why the correct answer wins: A domain groups the workspaces by subject area.
- **D:** Incorrect for this question. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. Why the correct answer wins: A domain groups the workspaces by subject area.

### Question 90 — C

Answer: Create a deployment pipeline with development, test, and production stages. A deployment pipeline promotes the same definitions through each stage. The pipeline promotes the same item definitions through the stages instead of rebuilding them. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A rule stops a promotion from overwriting the target stage environment-specific settings. Why the correct answer wins: A deployment pipeline promotes the same definitions through each stage.
- **B:** Incorrect for this question. The comparison shows what the promotion will change in the target before it happens. Why the correct answer wins: A deployment pipeline promotes the same definitions through each stage.
- **C:** Correct. The pipeline promotes the same item definitions through the stages instead of rebuilding them. In this case: A deployment pipeline promotes the same definitions through each stage.
- **D:** Incorrect for this question. Promoting every item drags unrelated work into the release. Why the correct answer wins: A deployment pipeline promotes the same definitions through each stage.

### Question 91 — D

Answer: Certify the item as the approved source. Certification marks the reviewed, authoritative items. Certification tells consumers the item has been reviewed as authoritative. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Promotion signals readiness without the review that certification implies. Why the correct answer wins: Certification marks the reviewed, authoritative items.
- **B:** Incorrect for this question. The label travels with the item and drives the protection downstream consumers inherit. Why the correct answer wins: Certification marks the reviewed, authoritative items.
- **C:** Incorrect for this question. A default label classifies new items that nobody labels by hand. Why the correct answer wins: Certification marks the reviewed, authoritative items.
- **D:** Correct. Certification tells consumers the item has been reviewed as authoritative. In this case: Certification marks the reviewed, authoritative items.

### Question 92 — D

Answer: Update statistics so the optimizer sees the current distribution. Statistics are what the optimizer plans from, so the plan is read first. The warehouse optimizer plans from statistics, not from the data itself. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Statistics are what the optimizer plans from, so the plan is read first.
- **B:** Incorrect for this question. A join on a different column forces a shuffle of both sides. Why the correct answer wins: Statistics are what the optimizer plans from, so the plan is read first.
- **C:** Incorrect for this question. Many small files cost more to scan than the same rows in fewer files. Why the correct answer wins: Statistics are what the optimizer plans from, so the plan is read first.
- **D:** Correct. The warehouse optimizer plans from statistics, not from the data itself. In this case: Statistics are what the optimizer plans from, so the plan is read first.

### Question 93 — B

Answer: Use the Monitoring hub for the run history. The Monitoring hub lists every run with its status. The hub lists every run with its status, duration, and owning item. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The Monitoring hub lists every run with its status.
- **B:** Correct. The hub lists every run with its status, duration, and owning item. In this case: The Monitoring hub lists every run with its status.
- **C:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The Monitoring hub lists every run with its status.
- **D:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The Monitoring hub lists every run with its status.

### Question 94 — C

Answer: Configure an alert on the failing condition. An alert turns the missing upload into a notification. An alert turns a silent failure into a notification. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The alert must reach the owner, or it becomes noise nobody acts on. Why the correct answer wins: An alert turns the missing upload into a notification.
- **B:** Incorrect for this question. Alerting on success as well as failure trains the team to ignore the alert. Why the correct answer wins: An alert turns the missing upload into a notification.
- **C:** Correct. An alert turns a silent failure into a notification. In this case: An alert turns the missing upload into a notification.
- **D:** Incorrect for this question. An activator rule evaluates the stream and fires when the condition holds. Why the correct answer wins: An alert turns the missing upload into a notification.

### Question 95 — D

Answer: Build a type 2 dimension with validity dates and a current flag. A type 2 dimension preserves the attribute history. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. Local study-map skill 2.2 (Dimensional Model Preparation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: A type 2 dimension preserves the attribute history.
- **B:** Incorrect for this question. A surrogate key decouples the warehouse from the source system identifiers. Why the correct answer wins: A type 2 dimension preserves the attribute history.
- **C:** Incorrect for this question. A star schema keeps the fact table narrow and the dimensions reusable. Why the correct answer wins: A type 2 dimension preserves the attribute history.
- **D:** Correct. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. In this case: A type 2 dimension preserves the attribute history.

### Question 96 — A

Answer: Load the curated model into the warehouse. A warehouse supports the multi-table transactions the model needs. A warehouse gives multi-table T-SQL transactions and a governed relational model. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. A warehouse gives multi-table T-SQL transactions and a governed relational model. In this case: A warehouse supports the multi-table transactions the model needs.
- **B:** Incorrect for this question. An eventhouse is optimized for high-volume time-series queries. Why the correct answer wins: A warehouse supports the multi-table transactions the model needs.
- **C:** Incorrect for this question. The Files area keeps the raw extract in its original format. Why the correct answer wins: A warehouse supports the multi-table transactions the model needs.
- **D:** Incorrect for this question. The endpoint gives read-only T-SQL over the Delta tables without a copy. Why the correct answer wins: A warehouse supports the multi-table transactions the model needs.

### Question 97 — D

Answer: Create an internal OneLake shortcut to the other lakehouse table. An internal shortcut points at the data without copying it. An internal shortcut points at another Fabric item without copying the data. Local study-map skill 2.14 (Eventstream and Spark Structured Streaming), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A copy duplicates the data, so the source of truth is no longer one place. Why the correct answer wins: An internal shortcut points at the data without copying it.
- **B:** Incorrect for this question. The shortcut exposes the external container as if the files were in OneLake. Why the correct answer wins: An internal shortcut points at the data without copying it.
- **C:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: An internal shortcut points at the data without copying it.
- **D:** Correct. An internal shortcut points at another Fabric item without copying the data. In this case: An internal shortcut points at the data without copying it.

### Question 98 — C

Answer: Scope the OneLake role to the folder that holds the restricted table. A folder-scoped OneLake role restricts exactly the trial data. A folder-scoped role restricts exactly the data rather than the whole lakehouse. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A group grant is maintained once instead of once per person. Why the correct answer wins: A folder-scoped OneLake role restricts exactly the trial data.
- **B:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: A folder-scoped OneLake role restricts exactly the trial data.
- **C:** Correct. A folder-scoped role restricts exactly the data rather than the whole lakehouse. In this case: A folder-scoped OneLake role restricts exactly the trial data.
- **D:** Incorrect for this question. OneLake security governs data access independently of the workspace role. Why the correct answer wins: A folder-scoped OneLake role restricts exactly the trial data.

### Question 99 — D

Answer: Define a row-level security policy on the table. Row-level security filters the rows per identity. Row-level security filters rows per identity, so one table returns different rows to different users. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The predicate must resolve the identity to the region, or every user sees the same rows. Why the correct answer wins: Row-level security filters the rows per identity.
- **B:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: Row-level security filters the rows per identity.
- **C:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: Row-level security filters the rows per identity.
- **D:** Correct. Row-level security filters rows per identity, so one table returns different rows to different users. In this case: Row-level security filters the rows per identity.

### Question 100 — B

Answer: Read the Fabric audit log in the Microsoft Purview portal. The audit log records who opened which item and when. The audit log records who did what to which item and when. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The audit log has a retention window, so an investigation that starts late needs the export. Why the correct answer wins: The audit log records who opened which item and when.
- **B:** Correct. The audit log records who did what to which item and when. In this case: The audit log records who opened which item and when.
- **C:** Incorrect for this question. Filtering turns a very large log into the events that answer the question. Why the correct answer wins: The audit log records who opened which item and when.
- **D:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The audit log records who opened which item and when.
