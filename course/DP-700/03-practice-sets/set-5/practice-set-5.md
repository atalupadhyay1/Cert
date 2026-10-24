# Microsoft DP-700 — Full-Length Mock Exam 5

Fabric Data Engineer Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, interactive components in the Fabric portal, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. The nightly job holds forty executors through a stage that needs six. What should be enabled?

Domain: Implement and manage an analytics solution

- A. Set the default environment at the workspace level
- B. Enable autoscale with a minimum and maximum node count
- C. Enable dynamic allocation so idle executors are released during the run
- D. Set a workspace-level custom Spark pool for the notebooks

### 2. A notebook must run against a fixed library set that differs from another team's. What should be attached?

Domain: Implement and manage an analytics solution

- A. Pin the library version in the environment instead of installing it in the notebook
- B. Set the default environment at the workspace level
- C. Attach a custom Spark environment to the notebook
- D. Set a workspace-level custom Spark pool for the notebooks

### 3. A new workspace will join a capacity that already runs four heavy workloads. What should be checked?

Domain: Implement and manage an analytics solution

- A. Keep OneLake availability enabled so other engines can read the same data
- B. Assign the workspace to a capacity that has headroom
- C. Create the workspace in the required region at creation time
- D. Assign the workspace to the domain that owns the subject area

### 4. Four brand workspaces must be governed as one subject area. What should be configured?

Domain: Implement and manage an analytics solution

- A. Keep OneLake availability enabled so other engines can read the same data
- B. Assign the workspace to a capacity that has headroom
- C. Assign the workspace to the domain that owns the subject area
- D. Create the workspace in the required region at creation time

### 5. A DAG is edited in the portal and no one can see who changed what. What should be done?

Domain: Implement and manage an analytics solution

- A. Sync the Airflow DAG from the connected Git repository
- B. Rewrite the existing orchestration as a Fabric pipeline instead
- C. Enable the Apache Airflow job in the workspace and author the DAG
- D. Use a pipeline for the copy and the orchestration

### 6. A DAG relies on an operator that Fabric does not support. What should the team evaluate?

Domain: Implement and manage an analytics solution

- A. Sync the Airflow DAG from the connected Git repository
- B. Enable the Apache Airflow job in the workspace and author the DAG
- C. Use a notebook for the transformation
- D. Rewrite the existing orchestration as a Fabric pipeline instead

### 7. Two engineers must change the same notebook without blocking each other. What should they use?

Domain: Implement and manage an analytics solution

- A. Resolve the conflict by choosing the definition that must win, then commit
- B. Work in a feature branch and merge through a pull request
- C. Connect the workspace to a Git repository and commit the item definitions
- D. Add the generated artefacts to the ignore file rather than committing them

### 8. A schema change must reach three environments from one artefact. What should be built?

Domain: Implement and manage an analytics solution

- A. Create a database project and deploy the schema from it
- B. Connect the workspace to a Git repository and commit the item definitions
- C. Build the project into a DACPAC and deploy that artefact
- D. Use SQLCMD variables for the environment-specific values

### 9. A promotion degraded the revenue model and the previous state is required now. What should be done?

Domain: Implement and manage an analytics solution

- A. Deploy backwards to recover the last known-good definition
- B. Compare the stages before promoting
- C. Create a deployment pipeline with development, test, and production stages
- D. Add deployment rules so the target stage keeps its own connection and parameters

### 10. Half the notebooks in the workspace are unfinished but every promotion carries them. What should be configured?

Domain: Implement and manage an analytics solution

- A. Select only the items that belong in the target stage
- B. Compare the stages before promoting
- C. Add deployment rules so the target stage keeps its own connection and parameters
- D. Create a deployment pipeline with development, test, and production stages

### 11. A brand team must read every item in its own workspace and change nothing. What should be granted?

Domain: Implement and manage an analytics solution

- A. Grant Admin on the workspace to the platform team
- B. Grant the user a workspace role
- C. Grant Read on the item
- D. Grant Viewer on the workspace

### 12. A brand manager needs one dashboard outside their workspace. What should be done?

Domain: Implement and manage an analytics solution

- A. Grant the user a workspace role
- B. Share a link to the item with the required permission
- C. Share the single item with the user who needs only that item
- D. Grant Admin on the workspace to the platform team

### 13. A row filter is defined but each brand manager still sees every brand. What should be fixed?

Domain: Implement and manage an analytics solution

- A. Filter the table through a predicate that resolves the user to a region
- B. Apply object-level security in the semantic model
- C. Define a row-level security policy on the table
- D. Apply column-level security so the column is hidden from the group

### 14. A cost column must be hidden from brand managers while the rest of the row stays readable. What should be applied?

Domain: Implement and manage an analytics solution

- A. Apply object-level security in the semantic model
- B. Define a row-level security policy on the table
- C. Grant access at the folder that holds the restricted files
- D. Apply column-level security so the column is hidden from the group

### 15. A brand manager must see only their brand and not the cost column. Which two controls apply? Select two.

Domain: Implement and manage an analytics solution

- A. Apply column-level security so the column is hidden from the group
- B. Define a row-level security policy on the table
- C. Grant access at the folder that holds the restricted files
- D. Apply object-level security in the semantic model
- E. Grant access at the individual file

### 16. A supplier identifier must not appear in the extract at all. What should be done?

Domain: Implement and manage an analytics solution

- A. Expose a view with the column omitted instead of masking it
- B. Mask the column in the report layer only
- C. Apply dynamic data masking to the column
- D. Exempt the authorised group from the mask

### 17. A margin column must be masked for most readers and absent from one feed. Which two features apply? Select two.

Domain: Implement and manage an analytics solution

- A. Apply dynamic data masking to the column
- B. Apply column-level security so the column is hidden from the group
- C. Exempt the authorised group from the mask
- D. Mask the column in the report layer only
- E. Expose a view with the column omitted instead of masking it

### 18. Two gold tables claim to be the revenue source and nobody knows which to trust. What should be done?

Domain: Implement and manage an analytics solution

- A. Set the default sensitivity label for the workspace
- B. Certify the item as the approved source
- C. Promote the item as ready for reuse
- D. Apply the sensitivity label to the item

### 19. New gold items must be classified and copies must not lose the class. Which two practices apply? Select two.

Domain: Implement and manage an analytics solution

- A. Certify the item as the approved source
- B. Promote the item as ready for reuse
- C. Apply the sensitivity label to the item
- D. Set the default sensitivity label for the workspace
- E. Let the label inherit from the labelled source file

### 20. An auditor asks which engineer queried the revenue table last Tuesday. What should be done?

Domain: Implement and manage an analytics solution

- A. Export the audit events before the retention window closes
- B. Filter the audit log by activity and by item
- C. Read the item activity log
- D. Read the Fabric audit log in the Microsoft Purview portal

### 21. Access evidence must be found and kept beyond the retention window. Which two steps apply? Select two.

Domain: Implement and manage an analytics solution

- A. Export the audit events before the retention window closes
- B. Read the item activity log
- C. Read the Fabric audit log in the Microsoft Purview portal
- D. Filter the audit log by activity and by item
- E. Read the refresh history for the semantic model

### 22. Contributors on the shared workspace can read every brand folder. What should be configured?

Domain: Implement and manage an analytics solution

- A. Grant access at the folder that holds the restricted files
- B. Scope the OneLake role to the folder that holds the restricted table
- C. Configure OneLake security roles for the lakehouse
- D. Grant the user a workspace role

### 23. One brand folder must be restricted to a named group. Which two settings apply? Select two.

Domain: Implement and manage an analytics solution

- A. Grant access at the folder that holds the restricted files
- B. Grant the OneLake role to a security group rather than to individuals
- C. Configure OneLake security roles for the lakehouse
- D. Scope the OneLake role to the folder that holds the restricted table
- E. Grant Admin on the workspace to the platform team

### 24. The revenue reconciliation is a set-based join over tables already in the warehouse. What should be used?

Domain: Implement and manage an analytics solution

- A. Use a pipeline for the copy and the orchestration
- B. Use a T-SQL script against the warehouse
- C. Use a notebook for the transformation
- D. Use a Dataflow Gen2 for the transformation

### 25. The brand consolidation needs PySpark that no low-code transform can express. What should be used?

Domain: Implement and manage an analytics solution

- A. Use a pipeline for the copy and the orchestration
- B. Use a notebook for the transformation
- C. Use a Dataflow Gen2 for the transformation
- D. Use a T-SQL script against the warehouse

### 26. One run must copy files and then reconcile them relationally. Which two items apply? Select two.

Domain: Implement and manage an analytics solution

- A. Use a T-SQL script against the warehouse
- B. Use a pipeline for the copy and the orchestration
- C. Use a KQL query against the eventhouse
- D. Use a notebook for the transformation
- E. Use a Dataflow Gen2 for the transformation

### 27. The nightly path includes today's date and is currently edited by hand. What should be used?

Domain: Implement and manage an analytics solution

- A. Pass the folder path as a pipeline parameter
- B. Look up the stored watermark before the copy
- C. Set the value in a pipeline variable and reference the variable
- D. Build the path with a dynamic expression at run time

### 28. A partner delivers at an unpredictable hour and the run must start on arrival. What should be configured?

Domain: Implement and manage an analytics solution

- A. Trigger on the file-created event for the landing folder
- B. Add an event-based trigger so the run starts when the file arrives
- C. Add a schedule trigger with the cadence and time zone the business expects
- D. Use an Until loop with a timeout for the long-running check

### 29. Four brand workspaces must adopt one reviewed release process. Which sequence is correct?

Domain: Implement and manage an analytics solution

- A. Create the deployment pipeline → connect the workspace to Git → promote through the stages → add deployment rules → commit the definitions
- B. Connect the workspace to Git → commit the item definitions → create the deployment pipeline → add deployment rules → promote through the stages
- C. Promote through the stages → create the deployment pipeline → commit the definitions → connect Git → add deployment rules
- D. Commit the item definitions → connect the workspace to Git → add deployment rules → create the pipeline → promote the stages

### 30. A shared analytics workspace must be created with governance from day one. Which sequence is correct?

Domain: Implement and manage an analytics solution

- A. Grant the workspace roles → create the workspace → choose the capacity → assign the domain
- B. Assign the domain → grant the roles → create the workspace → choose the capacity
- C. Choose the capacity and region → create the workspace → assign the domain → grant the workspace roles
- D. Create the workspace → choose the region after the first item is built → assign the domain → grant the roles

### 31. The partner reference repeats across partners and the reconciliation needs one key. What should the warehouse use?

Domain: Ingest and transform data

- A. Merge the incoming rows into the target on the business key
- B. Deduplicate on the business key and keep the latest record
- C. Generate a surrogate key instead of reusing the source key
- D. Build a type 2 dimension with validity dates and a current flag

### 32. The booking archive holds three years and the hourly run only needs new rows. What should change?

Domain: Ingest and transform data

- A. Run a full load and overwrite the target
- B. Store the last successful load timestamp in a control table
- C. Load only the rows newer than the stored watermark
- D. Route the failed rows to a reject table and continue the load

### 33. Four brands want their own detail and the board wants one number. What should be built?

Domain: Ingest and transform data

- A. Union the sources after conforming the columns
- B. Pivot the rows into the reporting columns
- C. Model the data as a star schema with conformed dimensions
- D. Denormalize the model so the report needs no join

### 34. The product hierarchy changed in April and last quarter must keep the old grouping. What should be built?

Domain: Ingest and transform data

- A. Deduplicate on the business key and keep the latest record
- B. Build a type 2 dimension with validity dates and a current flag
- C. Generate a surrogate key instead of reusing the source key
- D. Merge the incoming rows into the target on the business key

### 35. An hourly streaming load restarts and repeats the bookings it already wrote. What is missing?

Domain: Ingest and transform data

- A. Set a checkpoint location for the streaming query
- B. Query the stream through a OneLake shortcut
- C. Set a watermark so late events are handled deterministically
- D. Store the stream in native tables in the eventhouse

### 36. Curated booking tables must be readable by T-SQL without a warehouse load. Where should they be written?

Domain: Ingest and transform data

- A. Write the curated table into the lakehouse Tables area
- B. Create a KQL database for the time-series queries
- C. Load the curated model into the warehouse
- D. Store the telemetry in an eventhouse KQL database

### 37. The nightly reconciliation needs multi-table transactions. What should hold the model?

Domain: Ingest and transform data

- A. Create a KQL database for the time-series queries
- B. Land the extract in the lakehouse Files area
- C. Query the lakehouse through its SQL analytics endpoint
- D. Load the curated model into the warehouse

### 38. Analysts need read-only T-SQL and finance needs transactions. Which two stores apply? Select two.

Domain: Ingest and transform data

- A. Store the telemetry in an eventhouse KQL database
- B. Land the extract in the lakehouse Files area
- C. Query the lakehouse through its SQL analytics endpoint
- D. Load the curated model into the warehouse
- E. Write the curated table into the lakehouse Tables area

### 39. The booking reconciliation is a set-based join in the warehouse. What should be used?

Domain: Ingest and transform data

- A. Transform with T-SQL against the warehouse
- B. Transform with PySpark in a notebook
- C. Transform with KQL in the eventhouse
- D. Transform with Dataflow Gen2 and Power Query

### 40. The consolidation ranks brands within each region over sixty million rows. What should be used?

Domain: Ingest and transform data

- A. Transform with T-SQL against the warehouse
- B. Transform with KQL in the eventhouse
- C. Transform with Dataflow Gen2 and Power Query
- D. Transform with PySpark in a notebook

### 41. One step reconciles relationally and another ranks within a partition. Which two engines apply? Select two.

Domain: Ingest and transform data

- A. Use a Dataflow Gen2 for the transformation
- B. Transform with Dataflow Gen2 and Power Query
- C. Transform with KQL in the eventhouse
- D. Transform with T-SQL against the warehouse
- E. Transform with PySpark in a notebook

### 42. A brand's data must stay authoritative in its own lakehouse and must not be copied. What should be created?

Domain: Ingest and transform data

- A. Create an ADLS Gen2 shortcut to the external container
- B. Copy the remote data into a local table instead of shortcutting it
- C. Create an internal OneLake shortcut to the other lakehouse table
- D. Create a shortcut rather than a copy when the source stays authoritative

### 43. Every report over a shortcut-backed table scans the remote store. What should be enabled?

Domain: Ingest and transform data

- A. Create an internal OneLake shortcut to the other lakehouse table
- B. Copy the remote data into a local table instead of shortcutting it
- C. Enable query acceleration on the shortcut
- D. Create an ADLS Gen2 shortcut to the external container

### 44. A booking system must appear in Fabric within seconds and no pipeline runs. What should be enabled?

Domain: Ingest and transform data

- A. Use a Copy activity in the pipeline
- B. Create an internal OneLake shortcut to the other lakehouse table
- C. Enable mirroring for the operational database
- D. Run a full load and overwrite the target

### 45. The partner file must be preserved exactly as sent for dispute handling. What should be done?

Domain: Ingest and transform data

- A. Copy the files as binary and parse them downstream
- B. Use Get Metadata to list the files to process
- C. Append the new files instead of overwriting the target
- D. Use a Copy activity in the pipeline

### 46. The partner sends a variable number of files each hour. What should be used?

Domain: Ingest and transform data

- A. Iterate a ForEach activity over the returned list
- B. Copy the files as binary and parse them downstream
- C. Delete the processed source file after the load succeeds
- D. Use Get Metadata to list the files to process

### 47. Files must be preserved as received and the count is unknown. Which two actions apply? Select two.

Domain: Ingest and transform data

- A. Copy the files as binary and parse them downstream
- B. Append the new files instead of overwriting the target
- C. Use a Copy activity in the pipeline
- D. Delete the processed source file after the load succeeds
- E. Use Get Metadata to list the files to process

### 48. Each booking must carry the customer's previous booking date on the same row. What should be used?

Domain: Ingest and transform data

- A. Union the sources after conforming the columns
- B. Pivot the rows into the reporting columns
- C. Group and aggregate to the grain the report needs
- D. Use a window function to rank within the partition

### 49. Large row-level cleansing and a per-customer ranking are needed. Which two features apply? Select two.

Domain: Ingest and transform data

- A. Pivot the rows into the reporting columns
- B. Use a window function to rank within the partition
- C. Transform with Dataflow Gen2 and Power Query
- D. Transform with T-SQL against the warehouse
- E. Transform with PySpark in a notebook

### 50. A brand's low-code team must fix a column mapping themselves. What should be used?

Domain: Ingest and transform data

- A. Transform with KQL in the eventhouse
- B. Transform with Dataflow Gen2 and Power Query
- C. Transform with T-SQL against the warehouse
- D. Transform with PySpark in a notebook

### 51. A dimension needs a merge and the clickstream needs a window filter. Which two engines apply? Select two.

Domain: Ingest and transform data

- A. Transform with T-SQL against the warehouse
- B. Transform with PySpark in a notebook
- C. Pivot the rows into the reporting columns
- D. Transform with Dataflow Gen2 and Power Query
- E. Transform with KQL in the eventhouse

### 52. The board needs one row per brand-day and the detail needs one row per booking. What should be produced for the board?

Domain: Ingest and transform data

- A. Pivot the rows into the reporting columns
- B. Union the sources after conforming the columns
- C. Group and aggregate to the grain the report needs
- D. Denormalize the model so the report needs no join

### 53. Four brands export the same columns in different orders. What must happen first?

Domain: Ingest and transform data

- A. Denormalize the model so the report needs no join
- B. Union the sources after conforming the columns
- C. Pivot the rows into the reporting columns
- D. Group and aggregate to the grain the report needs

### 54. A booking appears twice with different values and neither is marked current. What rule should be applied?

Domain: Ingest and transform data

- A. Deduplicate on the business key and keep the latest record
- B. Deduplicate on the business key and keep the latest version
- C. Route the failed rows to a reject table and continue the load
- D. Replace the missing value with a documented default

### 55. Clickstream events must reach a KQL table without code. What should be used?

Domain: Ingest and transform data

- A. Process the stream with a KQL update policy
- B. Process the stream with Spark structured streaming
- C. Run a batch job every few minutes over the landing folder
- D. Process the stream with an eventstream

### 56. The hourly booking load must become incremental and safe. Which sequence is correct?

Domain: Ingest and transform data

- A. Merge into the target → read the watermark → update the watermark → extract the rows
- B. Read the watermark → extract only the rows after it → merge into the target → update the watermark
- C. Update the watermark → extract the rows → read the watermark → merge into the target
- D. Extract the full table → merge into the target → read the watermark → update the watermark

### 57. Hourly booking counts must be produced for each fixed hour. Which window fits?

Domain: Ingest and transform data

- A. Use a hopping window when the intervals must overlap
- B. Create a materialized view for the repeated aggregation
- C. Use a tumbling window for the fixed five-minute aggregate
- D. Use a sliding window that emits when the condition is met

### 58. Five reports recompute the same hourly count. What should be created?

Domain: Ingest and transform data

- A. Create a materialized view for the repeated aggregation
- B. Query the stream through a OneLake shortcut
- C. Use a hopping window when the intervals must overlap
- D. Use a tumbling window for the fixed five-minute aggregate

### 59. A consolidated revenue model must be built across four brands. Which sequence is correct?

Domain: Ingest and transform data

- A. Profile the source keys → define the grain of the fact → build the conformed dimensions → add the surrogate keys → load the fact
- B. Load the fact → build the conformed dimensions → profile the source keys → define the grain → add the surrogate keys
- C. Define the grain → add the surrogate keys → load the fact → profile the keys → build the dimensions
- D. Add the surrogate keys → load the fact → define the grain → profile the keys → build the dimensions

### 60. A revenue figure is wrong because of duplicate bookings and a late file. Which sequence is correct?

Domain: Ingest and transform data

- A. Decide the surviving record → recompute the aggregate → detect the duplicates → correct the partition
- B. Correct the partition → recompute the aggregate → decide the surviving record → detect the duplicates
- C. Recompute the aggregate → detect the duplicates → correct the partition → decide the surviving record
- D. Detect the duplicates and the late rows → decide the surviving record → correct the affected partition → recompute the aggregate

### 61. The whole nightly estate must be reviewed after a slow load. Where are the runs listed together?

Domain: Monitor and optimize an analytics solution

- A. Read the item activity log
- B. Send the logs to a Log Analytics workspace
- C. Read the refresh history for the semantic model
- D. Use the Monitoring hub for the run history

### 62. One notebook's run must be reviewed over a month. What should be read?

Domain: Monitor and optimize an analytics solution

- A. Read the item activity log
- B. Read the Fabric audit log in the Microsoft Purview portal
- C. Read the refresh history for the semantic model
- D. Use the Monitoring hub for the run history

### 63. A brand dashboard refreshes later each week. Where is the duration recorded?

Domain: Monitor and optimize an analytics solution

- A. Send the logs to a Log Analytics workspace
- B. Use the Monitoring hub for the run history
- C. Read the item activity log
- D. Read the refresh history for the semantic model

### 64. Refresh behaviour must be triaged today and analysed after a quarter. Which two sources apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Send the logs to a Log Analytics workspace
- B. Read the item activity log
- C. Read the refresh history for the semantic model
- D. Read the Fabric audit log in the Microsoft Purview portal
- E. Use the Monitoring hub for the run history

### 65. A silent load failure was discovered three days later. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Send the alert to the team that owns the item
- B. Alert on every successful run as well as every failure
- C. Configure an alert on the failing condition
- D. Use a Data Activator rule that watches the streaming condition

### 66. A retrying job pages the team several times a night for failures that clear. What should be configured?

Domain: Monitor and optimize an analytics solution

- A. Alert on every successful run as well as every failure
- B. Send the alert to the team that owns the item
- C. Set the alert to fire only after the retry policy has been exhausted
- D. Configure an alert on the failing condition

### 67. A pipeline fails and the run summary names no activity. What shows the cause?

Domain: Monitor and optimize an analytics solution

- A. Inspect the Dataflow Gen2 refresh error for the failing query step
- B. Read the activity output of the failed step
- C. Read the T-SQL error message and then the query plan
- D. Check the failing cell and the Spark driver log

### 68. A bad file reaches the gold layer and the run still reports success. What should be added?

Domain: Monitor and optimize an analytics solution

- A. Add an error branch so the failure is handled rather than ignored
- B. Use an Until loop with a timeout for the long-running check
- C. Add a retry policy with a delay to the failing activity
- D. Set the failure dependency so the handler runs when the step fails

### 69. A consolidation notebook succeeds but the runtime doubles week over week. What should be opened?

Domain: Monitor and optimize an analytics solution

- A. Inspect the failing cell output and exit value
- B. Open the Spark UI for the application
- C. Send the logs to a Log Analytics workspace
- D. Check the failing cell and the Spark driver log

### 70. A notebook fails on one brand with a null reference. Where is the stack?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Check the failing cell and the Spark driver log
- C. Open the Spark UI for the application
- D. Inspect the failing cell output and exit value

### 71. A notebook is slower and also failed once. Which two views apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Inspect the failing cell output and exit value
- C. Check the failing cell and the Spark driver log
- D. Send the logs to a Log Analytics workspace
- E. Open the Spark UI for the application

### 72. An eventstream delivers less than the source produces during peak. What shows the limit?

Domain: Monitor and optimize an analytics solution

- A. Read the refresh history for the semantic model
- B. Use the Monitoring hub for the run history
- C. Query the ingestion failures table in the KQL database
- D. Inspect the eventstream runtime metrics

### 73. A stream drops events and some land malformed. Which two sources apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Read the refresh history for the semantic model
- B. Read the Fabric audit log in the Microsoft Purview portal
- C. Use the Monitoring hub for the run history
- D. Inspect the eventstream runtime metrics
- E. Query the ingestion failures table in the KQL database

### 74. The reconciliation procedure fails after a column rename. What identifies the object?

Domain: Monitor and optimize an analytics solution

- A. Read the T-SQL error message and then the query plan
- B. Check the failing cell and the Spark driver log
- C. Check the shortcut connection and the delegated permission
- D. Read the activity output of the failed step

### 75. A shortcut-backed table returns nothing after a change in the source workspace. What should be checked?

Domain: Monitor and optimize an analytics solution

- A. Read the T-SQL error message and then the query plan
- B. Read the activity output of the failed step
- C. Check the failing cell and the Spark driver log
- D. Check the shortcut connection and the delegated permission

### 76. A procedure fails and a shortcut returns no rows. Which two checks apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Check the failing cell and the Spark driver log
- B. Read the activity output of the failed step
- C. Query the ingestion failures table in the KQL database
- D. Check the shortcut connection and the delegated permission
- E. Read the T-SQL error message and then the query plan

### 77. A table written every fifteen minutes holds 240,000 small files. What should be run?

Domain: Monitor and optimize an analytics solution

- A. Partition the table on the date column
- B. Run OPTIMIZE to compact the small files
- C. Enable V-Order on the table
- D. Run VACUUM to remove the files the table no longer references

### 78. Every report filters on order date and still scans the whole table. What should be added?

Domain: Monitor and optimize an analytics solution

- A. Partition the table on the date column
- B. Apply Z-Order on the frequently filtered columns
- C. Run OPTIMIZE to compact the small files
- D. Run VACUUM to remove the files the table no longer references

### 79. A small consolidated result is written as four hundred files. What should be done?

Domain: Monitor and optimize an analytics solution

- A. Coalesce the partitions before writing the small result
- B. Set the shuffle partition count to match the data volume
- C. Repartition before the write to control the file count
- D. Cache the DataFrame that is used twice

### 80. A warehouse table is read slowly and consists of thousands of small files. What should change?

Domain: Monitor and optimize an analytics solution

- A. Write fewer, larger files into the warehouse table
- B. Join on the distribution column so the rows stay on their node
- C. Insert the warehouse rows in batches rather than one at a time
- D. Update statistics so the optimizer sees the current distribution

### 81. A warehouse query is slow because of a bad estimate and a reshuffle. Which two actions apply? Select two.

Domain: Monitor and optimize an analytics solution

- A. Update statistics so the optimizer sees the current distribution
- B. Insert the warehouse rows in batches rather than one at a time
- C. Write fewer, larger files into the warehouse table
- D. Join on the distribution column so the rows stay on their node
- E. Coalesce the partitions before writing the small result

### 82. One customer key holds a fifth of nine billion rows and one task runs for an hour. What should be applied?

Domain: Monitor and optimize an analytics solution

- A. Enable skew join handling for the hot key
- B. Keep adaptive query execution enabled so the shuffle is re-planned
- C. Broadcast the small dimension to avoid the shuffle
- D. Salt the skewed key so the partitions even out

### 83. A nine-billion-row fact joins a customer dimension of forty thousand rows. What should be done?

Domain: Monitor and optimize an analytics solution

- A. Cache the DataFrame that is used twice
- B. Set the shuffle partition count to match the data volume
- C. Salt the skewed key so the partitions even out
- D. Broadcast the small dimension to avoid the shuffle

### 84. Both the load and the reporting queries are throttled in the same window. What should be changed?

Domain: Monitor and optimize an analytics solution

- A. Scale the destination throughput for the event volume
- B. Move the workspace to a larger capacity
- C. Enable capacity smoothing so a burst can borrow from the burst allowance
- D. Set the retention policy to match the query window

### 85. Four jobs start together, burst for twenty minutes, then idle. What should be enabled?

Domain: Monitor and optimize an analytics solution

- A. Set the retention policy to match the query window
- B. Increase the eventhouse capacity so the queries keep up
- C. Enable capacity smoothing so a burst can borrow from the burst allowance
- D. Move the workspace to a larger capacity

### 86. An eleven-minute report must be made faster with evidence. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Optimize the table → re-measure the query → read the plan → reduce the file count
- B. Read the query plan → reduce the file count → optimize and Z-Order the table → re-measure the query
- C. Reduce the file count → read the plan → re-measure the query → optimize the table
- D. Re-measure the query → optimize the table → read the plan → reduce the file count

### 87. A Spark job has one task that never finishes. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Find the skewed stage → open the Spark UI → re-run the job → broadcast the join
- B. Open the Spark UI → find the stage with the skewed task → broadcast or salt the join → re-run and compare the stage time
- C. Re-run and compare the stage time → open the Spark UI → find the skewed stage → salt the join
- D. Salt the join → re-run the job → open the Spark UI → find the skewed stage

### 88. A load failure must be detected rather than discovered. Which sequence is correct?

Domain: Monitor and optimize an analytics solution

- A. Review the alert history → enable the monitoring output → set the threshold → build the dashboard
- B. Build the dashboard → set the threshold → enable the output → review the history
- C. Enable the monitoring output → build the dashboard over it → set the alert threshold → review the alert history each week
- D. Set the alert threshold → build the dashboard → review the history → enable the output

---

## Case study — Lakeshore Retail Group

Lakeshore Retail Group operates four brands, each with its own product hierarchy and its own definition of a sale. The board wants one consolidated revenue number, and each brand wants its own detail. The engineering team has built one lakehouse per brand plus a shared gold layer, and the shared layer is rebuilt in full every night. Query performance on the shared layer has degraded as the brands added columns, and a recent load failed silently for three days because nobody watched the pipeline. The company has a Fabric capacity, a deployment pipeline, and an audit requirement that every revenue figure be reproducible from the gold layer alone.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. Each brand must keep its own source after promotion. What should be configured?

Domain: Implement and manage an analytics solution

- A. Add deployment rules so the target stage keeps its own connection and parameters
- B. Create a deployment pipeline with development, test, and production stages
- C. Compare the stages before promoting
- D. Select only the items that belong in the target stage

### 90. One revenue figure must be provably the approved one. What should be applied?

Domain: Implement and manage an analytics solution

- A. Promote the item as ready for reuse
- B. Set the default sensitivity label for the workspace
- C. Apply the sensitivity label to the item
- D. Certify the item as the approved source

### 91. The audit requires evidence that every revenue figure was reviewed. Where is it recorded?

Domain: Implement and manage an analytics solution

- A. Filter the audit log by activity and by item
- B. Export the audit events before the retention window closes
- C. Read the item activity log
- D. Read the Fabric audit log in the Microsoft Purview portal

---

## Case study — Margie Travel

Margie Travel books 90,000 trips a day through a web front end and a partner API. Booking events land in OneLake as JSON, and a notebook builds a warehouse fact table every hour. The finance team reconciles the warehouse against the payment provider nightly, and a mismatch of even one booking is escalated. The current load sometimes inserts the same booking twice when a partner retries a request. The engineering team wants the hourly load to finish in under ten minutes, and the reconciliation report identifies bookings by a partner reference that is not unique across partners.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. A partner retries and the load inserts the booking twice. What should be applied?

Domain: Ingest and transform data

- A. Reprocess the affected partitions when the data arrives late
- B. Deduplicate on the business key and keep the latest record
- C. Route the failed rows to a reject table and continue the load
- D. Replace the missing value with a documented default

### 93. The partner reference is not unique across partners. What should the warehouse use?

Domain: Ingest and transform data

- A. Deduplicate on the business key and keep the latest record
- B. Generate a surrogate key instead of reusing the source key
- C. Merge the incoming rows into the target on the business key
- D. Build a type 2 dimension with validity dates and a current flag

### 94. A corrected booking must replace the earlier version. What rule should be applied?

Domain: Ingest and transform data

- A. Deduplicate on the business key and keep the latest version
- B. Replace the missing value with a documented default
- C. Deduplicate on the business key and keep the latest record
- D. Route the failed rows to a reject table and continue the load

---

## Case study — VanArsdel Manufacturing

VanArsdel Manufacturing collects 11,000 sensor readings per second across nine plants and writes them into an eventhouse. The reliability dashboards query the last 24 hours, and a compliance report queries the last two years once a month. The eventstream that feeds the eventhouse drops events during shift changes, when the volume spikes. Queries that aggregate the last 24 hours have become slower every month even though the daily volume is flat. The team has one capacity, and the manufacturing director has asked for a plan that keeps the dashboard responsive without deleting the two-year history.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. Events are dropped during shift changes. What shows the constrained side?

Domain: Monitor and optimize an analytics solution

- A. Use the Monitoring hub for the run history
- B. Query the ingestion failures table in the KQL database
- C. Inspect the eventstream runtime metrics
- D. Read the refresh history for the semantic model

### 96. Two years must be kept for compliance but only a day is queried. What should be set?

Domain: Monitor and optimize an analytics solution

- A. Set the retention policy to match the query window
- B. Move the workspace to a larger capacity
- C. Increase the eventhouse capacity so the queries keep up
- D. Set the caching policy on the KQL table

### 97. Day queries have slowed as the table grew. What should be set?

Domain: Monitor and optimize an analytics solution

- A. Move the workspace to a larger capacity
- B. Increase the eventhouse capacity so the queries keep up
- C. Set the retention policy to match the query window
- D. Set the caching policy on the KQL table

---

## Case study — Wide World Importers

Wide World Importers holds 9 billion order-line rows in a Fabric lakehouse and reports on them through the SQL analytics endpoint. The nightly load writes about 240,000 small files, and a report that filters on order date and customer takes eleven minutes. The team has already confirmed that the query is not limited by the capacity and that the join to the customer dimension is not the bottleneck. The load itself now takes longer than the reporting window, and the team suspects that one customer accounts for a fifth of all rows. The company has one capacity and cannot add another before the next quarter.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. The nightly load writes 240,000 small files. What should be run first?

Domain: Monitor and optimize an analytics solution

- A. Partition the table on the date column
- B. Enable V-Order on the table
- C. Run OPTIMIZE to compact the small files
- D. Run VACUUM to remove the files the table no longer references

### 99. One customer holds a fifth of the order lines. What should be applied?

Domain: Monitor and optimize an analytics solution

- A. Salt the skewed key so the partitions even out
- B. Keep adaptive query execution enabled so the shuffle is re-planned
- C. Enable skew join handling for the hot key
- D. Broadcast the small dimension to avoid the shuffle

### 100. The load now exceeds the reporting window and no capacity can be added. What should be reviewed first?

Domain: Monitor and optimize an analytics solution

- A. Scale the destination throughput for the event volume
- B. Set the retention policy to match the query window
- C. Move the workspace to a larger capacity
- D. Enable capacity smoothing so a burst can borrow from the burst allowance

---

## Answer key and explanations

### Question 1 — C

Answer: Enable dynamic allocation so idle executors are released during the run. Dynamic allocation releases the executors the stage does not need. Dynamic allocation shrinks the executor set between stages, which matters when the stages are uneven. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace default environment means a new notebook inherits the approved libraries without a decision. Why the correct answer wins: Dynamic allocation releases the executors the stage does not need.
- **B:** Incorrect for this question. Autoscale adds executors while the job runs and releases them afterwards, so idle capacity is not billed. Why the correct answer wins: Dynamic allocation releases the executors the stage does not need.
- **C:** Correct. Dynamic allocation shrinks the executor set between stages, which matters when the stages are uneven. In this case: Dynamic allocation releases the executors the stage does not need.
- **D:** Incorrect for this question. A workspace Spark pool applies one node size and autoscale bound to every notebook that does not override it. Why the correct answer wins: Dynamic allocation releases the executors the stage does not need.

### Question 2 — C

Answer: Attach a custom Spark environment to the notebook. A custom environment carries that library set and Spark properties. An environment carries the library set and Spark properties, so every run starts from the same definition. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. An inline install changes the dependency per notebook and makes a run impossible to reproduce. Why the correct answer wins: A custom environment carries that library set and Spark properties.
- **B:** Incorrect for this question. A workspace default environment means a new notebook inherits the approved libraries without a decision. Why the correct answer wins: A custom environment carries that library set and Spark properties.
- **C:** Correct. An environment carries the library set and Spark properties, so every run starts from the same definition. In this case: A custom environment carries that library set and Spark properties.
- **D:** Incorrect for this question. A workspace Spark pool applies one node size and autoscale bound to every notebook that does not override it. Why the correct answer wins: A custom environment carries that library set and Spark properties.

### Question 3 — B

Answer: Assign the workspace to a capacity that has headroom. Every item shares one capacity, so headroom decides whether it fits. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. Local study-map skill 1.2 (Domain and OneLake Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. Why the correct answer wins: Every item shares one capacity, so headroom decides whether it fits.
- **B:** Correct. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. In this case: Every item shares one capacity, so headroom decides whether it fits.
- **C:** Incorrect for this question. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. Why the correct answer wins: Every item shares one capacity, so headroom decides whether it fits.
- **D:** Incorrect for this question. A domain groups workspaces for governance and discovery without moving the data. Why the correct answer wins: Every item shares one capacity, so headroom decides whether it fits.

### Question 4 — C

Answer: Assign the workspace to the domain that owns the subject area. A domain groups workspaces for governance and discovery. Local study-map skill 1.2 (Domain and OneLake Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. OneLake availability is what lets the warehouse and other workspaces read the same Delta files. Why the correct answer wins: A domain groups workspaces for governance and discovery.
- **B:** Incorrect for this question. Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them. Why the correct answer wins: A domain groups workspaces for governance and discovery.
- **C:** Correct. In this case: A domain groups workspaces for governance and discovery.
- **D:** Incorrect for this question. The workspace region is fixed at creation, so the decision cannot be corrected by a later setting. Why the correct answer wins: A domain groups workspaces for governance and discovery.

### Question 5 — A

Answer: Sync the Airflow DAG from the connected Git repository. Syncing the DAG from Git makes every change reviewable. Source-controlled DAGs keep the orchestration reviewable like any other item definition. Local study-map skill 1.3 (Apache Airflow Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Source-controlled DAGs keep the orchestration reviewable like any other item definition. In this case: Syncing the DAG from Git makes every change reviewable.
- **B:** Incorrect for this question. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. Why the correct answer wins: Syncing the DAG from Git makes every change reviewable.
- **C:** Incorrect for this question. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. Why the correct answer wins: Syncing the DAG from Git makes every change reviewable.
- **D:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: Syncing the DAG from Git makes every change reviewable.

### Question 6 — D

Answer: Rewrite the existing orchestration as a Fabric pipeline instead. Rewriting as a pipeline is the fallback when the DAG cannot run in Fabric. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. Local study-map skill 1.3 (Apache Airflow Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Source-controlled DAGs keep the orchestration reviewable like any other item definition. Why the correct answer wins: Rewriting as a pipeline is the fallback when the DAG cannot run in Fabric.
- **B:** Incorrect for this question. The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG. Why the correct answer wins: Rewriting as a pipeline is the fallback when the DAG cannot run in Fabric.
- **C:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: Rewriting as a pipeline is the fallback when the DAG cannot run in Fabric.
- **D:** Correct. Rewriting discards working logic and is only justified when the DAG cannot run in Fabric. In this case: Rewriting as a pipeline is the fallback when the DAG cannot run in Fabric.

### Question 7 — B

Answer: Work in a feature branch and merge through a pull request. A feature branch keeps each change separate until review. Branching keeps unfinished work out of the shared workspace and makes the change reviewable. Local study-map skill 1.4 (Version Control and Database Projects), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. An unresolved conflict blocks the update and leaves the workspace and the branch out of step. Why the correct answer wins: A feature branch keeps each change separate until review.
- **B:** Correct. Branching keeps unfinished work out of the shared workspace and makes the change reviewable. In this case: A feature branch keeps each change separate until review.
- **C:** Incorrect for this question. Git keeps a reviewable history of every item definition instead of an untracked live workspace. Why the correct answer wins: A feature branch keeps each change separate until review.
- **D:** Incorrect for this question. Committing build output makes every run look like a change. Why the correct answer wins: A feature branch keeps each change separate until review.

### Question 8 — C

Answer: Build the project into a DACPAC and deploy that artefact. The DACPAC is the versioned schema artefact. Local study-map skill 1.4 (Version Control and Database Projects), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A database project keeps the warehouse schema in source control and deploys it repeatably. Why the correct answer wins: The DACPAC is the versioned schema artefact.
- **B:** Incorrect for this question. Git keeps a reviewable history of every item definition instead of an untracked live workspace. Why the correct answer wins: The DACPAC is the versioned schema artefact.
- **C:** Correct. In this case: The DACPAC is the versioned schema artefact.
- **D:** Incorrect for this question. SQLCMD variables keep one project artefact deployable to both test and production. Why the correct answer wins: The DACPAC is the versioned schema artefact.

### Question 9 — A

Answer: Deploy backwards to recover the last known-good definition. A backward deployment restores the previous stage state. A backward deployment is the supported way to restore a previous stage state. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A backward deployment is the supported way to restore a previous stage state. In this case: A backward deployment restores the previous stage state.
- **B:** Incorrect for this question. The comparison shows what the promotion will change in the target before it happens. Why the correct answer wins: A backward deployment restores the previous stage state.
- **C:** Incorrect for this question. The pipeline promotes the same item definitions through the stages instead of rebuilding them. Why the correct answer wins: A backward deployment restores the previous stage state.
- **D:** Incorrect for this question. A rule stops a promotion from overwriting the target stage environment-specific settings. Why the correct answer wins: A backward deployment restores the previous stage state.

### Question 10 — A

Answer: Select only the items that belong in the target stage. Selecting the items keeps unfinished work out of the release. Promoting every item drags unrelated work into the release. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Promoting every item drags unrelated work into the release. In this case: Selecting the items keeps unfinished work out of the release.
- **B:** Incorrect for this question. The comparison shows what the promotion will change in the target before it happens. Why the correct answer wins: Selecting the items keeps unfinished work out of the release.
- **C:** Incorrect for this question. A rule stops a promotion from overwriting the target stage environment-specific settings. Why the correct answer wins: Selecting the items keeps unfinished work out of the release.
- **D:** Incorrect for this question. The pipeline promotes the same item definitions through the stages instead of rebuilding them. Why the correct answer wins: Selecting the items keeps unfinished work out of the release.

### Question 11 — D

Answer: Grant Viewer on the workspace. Viewer allows reading every item in the workspace without editing any of them. Viewer allows reading the items without editing them. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Admin is needed to manage access and settings, not to read the data. Why the correct answer wins: Viewer allows reading every item in the workspace without editing any of them.
- **B:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: Viewer allows reading every item in the workspace without editing any of them.
- **C:** Incorrect for this question. Read is the narrowest grant that still lets the item be consumed. Why the correct answer wins: Viewer allows reading every item in the workspace without editing any of them.
- **D:** Correct. Viewer allows reading the items without editing them. In this case: Viewer allows reading every item in the workspace without editing any of them.

### Question 12 — C

Answer: Share the single item with the user who needs only that item. Item sharing gives exactly the item needed. Item-level sharing avoids granting a workspace role for one report. Local study-map skill 1.6 (Workspace and Item-Level Access), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: Item sharing gives exactly the item needed.
- **B:** Incorrect for this question. A link is a shortcut to the item, not a substitute for the permission behind it. Why the correct answer wins: Item sharing gives exactly the item needed.
- **C:** Correct. Item-level sharing avoids granting a workspace role for one report. In this case: Item sharing gives exactly the item needed.
- **D:** Incorrect for this question. Admin is needed to manage access and settings, not to read the data. Why the correct answer wins: Item sharing gives exactly the item needed.

### Question 13 — A

Answer: Filter the table through a predicate that resolves the user to a region. The predicate must resolve the user to a brand before it filters. The predicate must resolve the identity to the region, or every user sees the same rows. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The predicate must resolve the identity to the region, or every user sees the same rows. In this case: The predicate must resolve the user to a brand before it filters.
- **B:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: The predicate must resolve the user to a brand before it filters.
- **C:** Incorrect for this question. Row-level security filters rows per identity, so one table returns different rows to different users. Why the correct answer wins: The predicate must resolve the user to a brand before it filters.
- **D:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: The predicate must resolve the user to a brand before it filters.

### Question 14 — D

Answer: Apply column-level security so the column is hidden from the group. Column-level security hides that column and leaves the table readable. Column-level security hides the column while leaving the rest of the table readable. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: Column-level security hides that column and leaves the table readable.
- **B:** Incorrect for this question. Row-level security filters rows per identity, so one table returns different rows to different users. Why the correct answer wins: Column-level security hides that column and leaves the table readable.
- **C:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: Column-level security hides that column and leaves the table readable.
- **D:** Correct. Column-level security hides the column while leaving the rest of the table readable. In this case: Column-level security hides that column and leaves the table readable.

### Question 15 — A, B

Answers: Define a row-level security policy on the table; Apply column-level security so the column is hidden from the group. Row-level security filters the rows, and column-level security hides the column. Row-level security filters rows per identity, so one table returns different rows to different users. Column-level security hides the column while leaving the rest of the table readable. Local study-map skill 1.7 (Row, Column, Object, and File-Level Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Column-level security hides the column while leaving the rest of the table readable. In this case: Row-level security filters the rows, and column-level security hides the column.
- **B:** Correct. Row-level security filters rows per identity, so one table returns different rows to different users. In this case: Row-level security filters the rows, and column-level security hides the column.
- **C:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: Row-level security filters the rows, and column-level security hides the column.
- **D:** Incorrect for this question. Object-level security hides a table or column from a role in the semantic model. Why the correct answer wins: Row-level security filters the rows, and column-level security hides the column.
- **E:** Incorrect for this question. A file-level grant is the narrowest path restriction the platform offers. Why the correct answer wins: Row-level security filters the rows, and column-level security hides the column.

### Question 16 — A

Answer: Expose a view with the column omitted instead of masking it. A view removes the column rather than masking its value. A view removes the column entirely, which is not the same as masking the value. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A view removes the column entirely, which is not the same as masking the value. In this case: A view removes the column rather than masking its value.
- **B:** Incorrect for this question. A report-level mask protects one visual and leaves every other consumer unmasked. Why the correct answer wins: A view removes the column rather than masking its value.
- **C:** Incorrect for this question. Masking shows a masked value to unauthorised users while the stored data stays intact. Why the correct answer wins: A view removes the column rather than masking its value.
- **D:** Incorrect for this question. The masking rule needs the exemption, or the authorised group sees masked values too. Why the correct answer wins: A view removes the column rather than masking its value.

### Question 17 — A, E

Answers: Apply dynamic data masking to the column; Expose a view with the column omitted instead of masking it. The mask protects the value, and the view removes the column. Masking shows a masked value to unauthorised users while the stored data stays intact. A view removes the column entirely, which is not the same as masking the value. Local study-map skill 1.8 (Dynamic Data Masking), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Masking shows a masked value to unauthorised users while the stored data stays intact. In this case: The mask protects the value, and the view removes the column.
- **B:** Incorrect for this question. Column-level security hides the column while leaving the rest of the table readable. Why the correct answer wins: The mask protects the value, and the view removes the column.
- **C:** Incorrect for this question. The masking rule needs the exemption, or the authorised group sees masked values too. Why the correct answer wins: The mask protects the value, and the view removes the column.
- **D:** Incorrect for this question. A report-level mask protects one visual and leaves every other consumer unmasked. Why the correct answer wins: The mask protects the value, and the view removes the column.
- **E:** Correct. A view removes the column entirely, which is not the same as masking the value. In this case: The mask protects the value, and the view removes the column.

### Question 18 — B

Answer: Certify the item as the approved source. Certification marks the reviewed, authoritative one. Certification tells consumers the item has been reviewed as authoritative. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A default label classifies new items that nobody labels by hand. Why the correct answer wins: Certification marks the reviewed, authoritative one.
- **B:** Correct. Certification tells consumers the item has been reviewed as authoritative. In this case: Certification marks the reviewed, authoritative one.
- **C:** Incorrect for this question. Promotion signals readiness without the review that certification implies. Why the correct answer wins: Certification marks the reviewed, authoritative one.
- **D:** Incorrect for this question. The label travels with the item and drives the protection downstream consumers inherit. Why the correct answer wins: Certification marks the reviewed, authoritative one.

### Question 19 — D, E

Answers: Set the default sensitivity label for the workspace; Let the label inherit from the labelled source file. The default labels new items, and inheritance preserves the class. A default label classifies new items that nobody labels by hand. Inheritance keeps one classification instead of a second opinion on the same data. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Certification tells consumers the item has been reviewed as authoritative. Why the correct answer wins: The default labels new items, and inheritance preserves the class.
- **B:** Incorrect for this question. Promotion signals readiness without the review that certification implies. Why the correct answer wins: The default labels new items, and inheritance preserves the class.
- **C:** Incorrect for this question. The label travels with the item and drives the protection downstream consumers inherit. Why the correct answer wins: The default labels new items, and inheritance preserves the class.
- **D:** Correct. A default label classifies new items that nobody labels by hand. In this case: The default labels new items, and inheritance preserves the class.
- **E:** Correct. Inheritance keeps one classification instead of a second opinion on the same data. In this case: The default labels new items, and inheritance preserves the class.

### Question 20 — B

Answer: Filter the audit log by activity and by item. Filtering the audit log narrows it to the events that answer the question. Filtering turns a very large log into the events that answer the question. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The audit log has a retention window, so an investigation that starts late needs the export. Why the correct answer wins: Filtering the audit log narrows it to the events that answer the question.
- **B:** Correct. Filtering turns a very large log into the events that answer the question. In this case: Filtering the audit log narrows it to the events that answer the question.
- **C:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: Filtering the audit log narrows it to the events that answer the question.
- **D:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: Filtering the audit log narrows it to the events that answer the question.

### Question 21 — A, C

Answers: Read the Fabric audit log in the Microsoft Purview portal; Export the audit events before the retention window closes. The audit log holds the events, and the export preserves them. The audit log records who did what to which item and when. The audit log has a retention window, so an investigation that starts late needs the export. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. The audit log has a retention window, so an investigation that starts late needs the export. In this case: The audit log holds the events, and the export preserves them.
- **B:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The audit log holds the events, and the export preserves them.
- **C:** Correct. The audit log records who did what to which item and when. In this case: The audit log holds the events, and the export preserves them.
- **D:** Incorrect for this question. Filtering turns a very large log into the events that answer the question. Why the correct answer wins: The audit log holds the events, and the export preserves them.
- **E:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The audit log holds the events, and the export preserves them.

### Question 22 — C

Answer: Configure OneLake security roles for the lakehouse. OneLake security governs the data independently of the workspace role. OneLake security governs data access independently of the workspace role. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: OneLake security governs the data independently of the workspace role.
- **B:** Incorrect for this question. A folder-scoped role restricts exactly the data rather than the whole lakehouse. Why the correct answer wins: OneLake security governs the data independently of the workspace role.
- **C:** Correct. OneLake security governs data access independently of the workspace role. In this case: OneLake security governs the data independently of the workspace role.
- **D:** Incorrect for this question. A workspace role is the coarse grant that every item in the workspace inherits. Why the correct answer wins: OneLake security governs the data independently of the workspace role.

### Question 23 — B, D

Answers: Scope the OneLake role to the folder that holds the restricted table; Grant the OneLake role to a security group rather than to individuals. The OneLake role governs the data, and the folder scope limits it. A folder-scoped role restricts exactly the data rather than the whole lakehouse. A group grant is maintained once instead of once per person. Local study-map skill 1.11 (OneLake Security), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A folder grant restricts the path without hiding the whole lakehouse. Why the correct answer wins: The OneLake role governs the data, and the folder scope limits it.
- **B:** Correct. A group grant is maintained once instead of once per person. In this case: The OneLake role governs the data, and the folder scope limits it.
- **C:** Incorrect for this question. OneLake security governs data access independently of the workspace role. Why the correct answer wins: The OneLake role governs the data, and the folder scope limits it.
- **D:** Correct. A folder-scoped role restricts exactly the data rather than the whole lakehouse. In this case: The OneLake role governs the data, and the folder scope limits it.
- **E:** Incorrect for this question. Admin is needed to manage access and settings, not to read the data. Why the correct answer wins: The OneLake role governs the data, and the folder scope limits it.

### Question 24 — B

Answer: Use a T-SQL script against the warehouse. T-SQL is the natural engine for a set-based join there. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: T-SQL is the natural engine for a set-based join there.
- **B:** Correct. Set-based T-SQL is the natural choice when the data already sits in the warehouse. In this case: T-SQL is the natural engine for a set-based join there.
- **C:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: T-SQL is the natural engine for a set-based join there.
- **D:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: T-SQL is the natural engine for a set-based join there.

### Question 25 — B

Answer: Use a notebook for the transformation. A notebook is the place for PySpark the low-code engine cannot express. A notebook is the right place for PySpark that a low-code transform cannot express. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Why the correct answer wins: A notebook is the place for PySpark the low-code engine cannot express.
- **B:** Correct. A notebook is the right place for PySpark that a low-code transform cannot express. In this case: A notebook is the place for PySpark the low-code engine cannot express.
- **C:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: A notebook is the place for PySpark the low-code engine cannot express.
- **D:** Incorrect for this question. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Why the correct answer wins: A notebook is the place for PySpark the low-code engine cannot express.

### Question 26 — A, B

Answers: Use a pipeline for the copy and the orchestration; Use a T-SQL script against the warehouse. The pipeline copies and orders, and T-SQL reconciles. A pipeline owns the scheduling, the copy activity, and the dependency between steps. Set-based T-SQL is the natural choice when the data already sits in the warehouse. Local study-map skill 1.12 (Choosing Between Dataflow Gen2, Pipeline, and Notebook), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. Set-based T-SQL is the natural choice when the data already sits in the warehouse. In this case: The pipeline copies and orders, and T-SQL reconciles.
- **B:** Correct. A pipeline owns the scheduling, the copy activity, and the dependency between steps. In this case: The pipeline copies and orders, and T-SQL reconciles.
- **C:** Incorrect for this question. KQL is the native language of the eventhouse tables. Why the correct answer wins: The pipeline copies and orders, and T-SQL reconciles.
- **D:** Incorrect for this question. A notebook is the right place for PySpark that a low-code transform cannot express. Why the correct answer wins: The pipeline copies and orders, and T-SQL reconciles.
- **E:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: The pipeline copies and orders, and T-SQL reconciles.

### Question 27 — D

Answer: Build the path with a dynamic expression at run time. A dynamic expression computes the path at run time. A dynamic expression computes the path instead of hard-coding a date. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. A parameter makes one pipeline reusable across folders and environments. Why the correct answer wins: A dynamic expression computes the path at run time.
- **B:** Incorrect for this question. The lookup is what makes the load incremental rather than a full reload. Why the correct answer wins: A dynamic expression computes the path at run time.
- **C:** Incorrect for this question. A variable carries the computed value between the activities that need it. Why the correct answer wins: A dynamic expression computes the path at run time.
- **D:** Correct. A dynamic expression computes the path instead of hard-coding a date. In this case: A dynamic expression computes the path at run time.

### Question 28 — B

Answer: Add an event-based trigger so the run starts when the file arrives. An event trigger starts the run when the file arrives. An event trigger removes the gap between the file landing and the run starting. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. The file-created event is the signal that the extract has finished arriving. Why the correct answer wins: An event trigger starts the run when the file arrives.
- **B:** Correct. An event trigger removes the gap between the file landing and the run starting. In this case: An event trigger starts the run when the file arrives.
- **C:** Incorrect for this question. The schedule trigger is what makes the run recur without a person starting it. Why the correct answer wins: An event trigger starts the run when the file arrives.
- **D:** Incorrect for this question. Until repeats the check and stops when the condition is met or the timeout expires. Why the correct answer wins: An event trigger starts the run when the file arrives.

### Question 29 — B

Answer: Connect the workspace to Git → commit the item definitions → create the deployment pipeline → add deployment rules → promote through the stages. Definitions are committed before the pipeline promotes them. The definitions have to be in source control before the pipeline promotes them, and the rules are added before the first promotion. Local study-map skill 1.13 (Schedules, Event Triggers, and Dynamic Parameters), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Promoting before the definitions are committed and before the rules exist overwrites the target with the wrong settings. Why the correct answer wins: Definitions are committed before the pipeline promotes them.
- **B:** Correct. The definitions have to be in source control before the pipeline promotes them, and the rules are added before the first promotion. In this case: Definitions are committed before the pipeline promotes them.
- **C:** Incorrect for this question. Every step is in the wrong order: a promotion needs the pipeline, the pipeline needs the definitions in Git, and the rules come first. Why the correct answer wins: Definitions are committed before the pipeline promotes them.
- **D:** Incorrect for this question. There is nothing to commit before the repository is connected, and the rules belong to a pipeline that does not exist yet. Why the correct answer wins: Definitions are committed before the pipeline promotes them.

### Question 30 — C

Answer: Choose the capacity and region → create the workspace → assign the domain → grant the workspace roles. The region and capacity come before the workspace, and access after it. The region is fixed at creation, so it is decided before the workspace exists, and access is granted after it does. Local study-map skill 1.1 (Spark Workspace Settings), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Roles cannot be granted before the workspace exists, and the capacity is chosen before, not after. Why the correct answer wins: The region and capacity come before the workspace, and access after it.
- **B:** Incorrect for this question. A domain assignment and a role grant both need the workspace, and the capacity is not a last step. Why the correct answer wins: The region and capacity come before the workspace, and access after it.
- **C:** Correct. The region is fixed at creation, so it is decided before the workspace exists, and access is granted after it does. In this case: The region and capacity come before the workspace, and access after it.
- **D:** Incorrect for this question. The region cannot be changed after creation, so choosing it later is not possible. Why the correct answer wins: The region and capacity come before the workspace, and access after it.

### Question 31 — C

Answer: Generate a surrogate key instead of reusing the source key. A surrogate key distinguishes two bookings that share a partner reference. A surrogate key decouples the warehouse from the source system identifiers. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: A surrogate key distinguishes two bookings that share a partner reference.
- **B:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: A surrogate key distinguishes two bookings that share a partner reference.
- **C:** Correct. A surrogate key decouples the warehouse from the source system identifiers. In this case: A surrogate key distinguishes two bookings that share a partner reference.
- **D:** Incorrect for this question. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. Why the correct answer wins: A surrogate key distinguishes two bookings that share a partner reference.

### Question 32 — C

Answer: Load only the rows newer than the stored watermark. An incremental load moves the delta instead of the history. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: An incremental load moves the delta instead of the history.
- **B:** Incorrect for this question. The control table is what lets the next run know where this one stopped. Why the correct answer wins: An incremental load moves the delta instead of the history.
- **C:** Correct. In this case: An incremental load moves the delta instead of the history.
- **D:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: An incremental load moves the delta instead of the history.

### Question 33 — C

Answer: Model the data as a star schema with conformed dimensions. A star schema keeps the facts narrow and the dimensions conformed. A star schema keeps the fact table narrow and the dimensions reusable. Local study-map skill 2.2 (Dimensional Model Preparation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: A star schema keeps the facts narrow and the dimensions conformed.
- **B:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: A star schema keeps the facts narrow and the dimensions conformed.
- **C:** Correct. A star schema keeps the fact table narrow and the dimensions reusable. In this case: A star schema keeps the facts narrow and the dimensions conformed.
- **D:** Incorrect for this question. Denormalization trades storage for the query shape the report actually uses. Why the correct answer wins: A star schema keeps the facts narrow and the dimensions conformed.

### Question 34 — B

Answer: Build a type 2 dimension with validity dates and a current flag. A type 2 dimension preserves the grouping that applied then. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. Local study-map skill 2.2 (Dimensional Model Preparation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: A type 2 dimension preserves the grouping that applied then.
- **B:** Correct. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. In this case: A type 2 dimension preserves the grouping that applied then.
- **C:** Incorrect for this question. A surrogate key decouples the warehouse from the source system identifiers. Why the correct answer wins: A type 2 dimension preserves the grouping that applied then.
- **D:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: A type 2 dimension preserves the grouping that applied then.

### Question 35 — A

Answer: Set a checkpoint location for the streaming query. The checkpoint records where the stream resumes. The checkpoint is what makes the stream restart from where it stopped. Local study-map skill 2.3 (Streaming Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. The checkpoint is what makes the stream restart from where it stopped. In this case: The checkpoint records where the stream resumes.
- **B:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: The checkpoint records where the stream resumes.
- **C:** Incorrect for this question. A watermark sets how long the engine waits for late events before closing a window. Why the correct answer wins: The checkpoint records where the stream resumes.
- **D:** Incorrect for this question. Native tables give full KQL capability over the streaming data. Why the correct answer wins: The checkpoint records where the stream resumes.

### Question 36 — A

Answer: Write the curated table into the lakehouse Tables area. A Delta table in the Tables area is exposed by the endpoint. A Delta table in Tables is what the SQL analytics endpoint exposes. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. A Delta table in Tables is what the SQL analytics endpoint exposes. In this case: A Delta table in the Tables area is exposed by the endpoint.
- **B:** Incorrect for this question. A KQL database indexes the timestamp column for the range queries the dashboards run. Why the correct answer wins: A Delta table in the Tables area is exposed by the endpoint.
- **C:** Incorrect for this question. A warehouse gives multi-table T-SQL transactions and a governed relational model. Why the correct answer wins: A Delta table in the Tables area is exposed by the endpoint.
- **D:** Incorrect for this question. An eventhouse is optimized for high-volume time-series queries. Why the correct answer wins: A Delta table in the Tables area is exposed by the endpoint.

### Question 37 — D

Answer: Load the curated model into the warehouse. A warehouse supports the transactional T-SQL the reconciliation needs. A warehouse gives multi-table T-SQL transactions and a governed relational model. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A KQL database indexes the timestamp column for the range queries the dashboards run. Why the correct answer wins: A warehouse supports the transactional T-SQL the reconciliation needs.
- **B:** Incorrect for this question. The Files area keeps the raw extract in its original format. Why the correct answer wins: A warehouse supports the transactional T-SQL the reconciliation needs.
- **C:** Incorrect for this question. The endpoint gives read-only T-SQL over the Delta tables without a copy. Why the correct answer wins: A warehouse supports the transactional T-SQL the reconciliation needs.
- **D:** Correct. A warehouse gives multi-table T-SQL transactions and a governed relational model. In this case: A warehouse supports the transactional T-SQL the reconciliation needs.

### Question 38 — D, E

Answers: Write the curated table into the lakehouse Tables area; Load the curated model into the warehouse. The lakehouse table serves the endpoint, and the warehouse serves the transactions. A Delta table in Tables is what the SQL analytics endpoint exposes. A warehouse gives multi-table T-SQL transactions and a governed relational model. Local study-map skill 2.4 (Choosing a Data Store), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. An eventhouse is optimized for high-volume time-series queries. Why the correct answer wins: The lakehouse table serves the endpoint, and the warehouse serves the transactions.
- **B:** Incorrect for this question. The Files area keeps the raw extract in its original format. Why the correct answer wins: The lakehouse table serves the endpoint, and the warehouse serves the transactions.
- **C:** Incorrect for this question. The endpoint gives read-only T-SQL over the Delta tables without a copy. Why the correct answer wins: The lakehouse table serves the endpoint, and the warehouse serves the transactions.
- **D:** Correct. A warehouse gives multi-table T-SQL transactions and a governed relational model. In this case: The lakehouse table serves the endpoint, and the warehouse serves the transactions.
- **E:** Correct. A Delta table in Tables is what the SQL analytics endpoint exposes. In this case: The lakehouse table serves the endpoint, and the warehouse serves the transactions.

### Question 39 — A

Answer: Transform with T-SQL against the warehouse. T-SQL is the natural engine for a set-based join there. T-SQL is the right engine once the data is relational and already in the warehouse. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. T-SQL is the right engine once the data is relational and already in the warehouse. In this case: T-SQL is the natural engine for a set-based join there.
- **B:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: T-SQL is the natural engine for a set-based join there.
- **C:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: T-SQL is the natural engine for a set-based join there.
- **D:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: T-SQL is the natural engine for a set-based join there.

### Question 40 — D

Answer: Transform with PySpark in a notebook. PySpark handles the windowed transformation at that scale. PySpark handles the row-level and windowed transformations that Spark scales. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: PySpark handles the windowed transformation at that scale.
- **B:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: PySpark handles the windowed transformation at that scale.
- **C:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: PySpark handles the windowed transformation at that scale.
- **D:** Correct. PySpark handles the row-level and windowed transformations that Spark scales. In this case: PySpark handles the windowed transformation at that scale.

### Question 41 — D, E

Answers: Transform with T-SQL against the warehouse; Transform with PySpark in a notebook. T-SQL performs the relational reconciliation, and PySpark performs the ranking. T-SQL is the right engine once the data is relational and already in the warehouse. PySpark handles the row-level and windowed transformations that Spark scales. Local study-map skill 2.5 (Choosing a Transformation Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A Dataflow Gen2 suits a transformation that is expressible in Power Query. Why the correct answer wins: T-SQL performs the relational reconciliation, and PySpark performs the ranking.
- **B:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: T-SQL performs the relational reconciliation, and PySpark performs the ranking.
- **C:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: T-SQL performs the relational reconciliation, and PySpark performs the ranking.
- **D:** Correct. T-SQL is the right engine once the data is relational and already in the warehouse. In this case: T-SQL performs the relational reconciliation, and PySpark performs the ranking.
- **E:** Correct. PySpark handles the row-level and windowed transformations that Spark scales. In this case: T-SQL performs the relational reconciliation, and PySpark performs the ranking.

### Question 42 — D

Answer: Create a shortcut rather than a copy when the source stays authoritative. A shortcut has no second copy to keep in step. Local study-map skill 2.6 (OneLake Shortcuts), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The shortcut exposes the external container as if the files were in OneLake. Why the correct answer wins: A shortcut has no second copy to keep in step.
- **B:** Incorrect for this question. A copy duplicates the data, so the source of truth is no longer one place. Why the correct answer wins: A shortcut has no second copy to keep in step.
- **C:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: A shortcut has no second copy to keep in step.
- **D:** Correct. In this case: A shortcut has no second copy to keep in step.

### Question 43 — C

Answer: Enable query acceleration on the shortcut. Query acceleration caches the columns the reports read. Query acceleration caches the columns a report reads, so the remote source is not scanned per query. Local study-map skill 2.6 (OneLake Shortcuts), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: Query acceleration caches the columns the reports read.
- **B:** Incorrect for this question. A copy duplicates the data, so the source of truth is no longer one place. Why the correct answer wins: Query acceleration caches the columns the reports read.
- **C:** Correct. Query acceleration caches the columns a report reads, so the remote source is not scanned per query. In this case: Query acceleration caches the columns the reports read.
- **D:** Incorrect for this question. The shortcut exposes the external container as if the files were in OneLake. Why the correct answer wins: Query acceleration caches the columns the reports read.

### Question 44 — C

Answer: Enable mirroring for the operational database. Mirroring replicates the source tables continuously into OneLake without a schedule. Local study-map skill 2.7 (Mirroring), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: Mirroring replicates the source tables continuously into OneLake without a schedule.
- **B:** Incorrect for this question. An internal shortcut points at another Fabric item without copying the data. Why the correct answer wins: Mirroring replicates the source tables continuously into OneLake without a schedule.
- **C:** Correct. In this case: Mirroring replicates the source tables continuously into OneLake without a schedule.
- **D:** Incorrect for this question. A full load is simple, but it reloads the whole history every time it runs. Why the correct answer wins: Mirroring replicates the source tables continuously into OneLake without a schedule.

### Question 45 — A

Answer: Copy the files as binary and parse them downstream. A binary copy keeps the file exactly as delivered. A binary copy keeps the source exactly as delivered for later validation. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. A binary copy keeps the source exactly as delivered for later validation. In this case: A binary copy keeps the file exactly as delivered.
- **B:** Incorrect for this question. Get Metadata turns an unknown folder into a list the loop can iterate. Why the correct answer wins: A binary copy keeps the file exactly as delivered.
- **C:** Incorrect for this question. Appending preserves the earlier loads that the incremental pattern depends on. Why the correct answer wins: A binary copy keeps the file exactly as delivered.
- **D:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: A binary copy keeps the file exactly as delivered.

### Question 46 — D

Answer: Use Get Metadata to list the files to process. Get Metadata turns the folder into a list the loop can iterate. Get Metadata turns an unknown folder into a list the loop can iterate. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. ForEach applies the same pattern to every object the lookup returned. Why the correct answer wins: Get Metadata turns the folder into a list the loop can iterate.
- **B:** Incorrect for this question. A binary copy keeps the source exactly as delivered for later validation. Why the correct answer wins: Get Metadata turns the folder into a list the loop can iterate.
- **C:** Incorrect for this question. Deleting after success prevents the same file being loaded twice. Why the correct answer wins: Get Metadata turns the folder into a list the loop can iterate.
- **D:** Correct. Get Metadata turns an unknown folder into a list the loop can iterate. In this case: Get Metadata turns the folder into a list the loop can iterate.

### Question 47 — A, E

Answers: Copy the files as binary and parse them downstream; Use Get Metadata to list the files to process. The binary copy preserves them, and Get Metadata lists them. A binary copy keeps the source exactly as delivered for later validation. Get Metadata turns an unknown folder into a list the loop can iterate. Local study-map skill 2.8 (Pipeline Ingestion), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. A binary copy keeps the source exactly as delivered for later validation. In this case: The binary copy preserves them, and Get Metadata lists them.
- **B:** Incorrect for this question. Appending preserves the earlier loads that the incremental pattern depends on. Why the correct answer wins: The binary copy preserves them, and Get Metadata lists them.
- **C:** Incorrect for this question. The Copy activity moves the files or rows as one orchestrated step. Why the correct answer wins: The binary copy preserves them, and Get Metadata lists them.
- **D:** Incorrect for this question. Deleting after success prevents the same file being loaded twice. Why the correct answer wins: The binary copy preserves them, and Get Metadata lists them.
- **E:** Correct. Get Metadata turns an unknown folder into a list the loop can iterate. In this case: The binary copy preserves them, and Get Metadata lists them.

### Question 48 — D

Answer: Use a window function to rank within the partition. A window function reads the previous row without collapsing it. A window computes across related rows without collapsing them into one. Local study-map skill 2.9 (PySpark Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: A window function reads the previous row without collapsing it.
- **B:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: A window function reads the previous row without collapsing it.
- **C:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: A window function reads the previous row without collapsing it.
- **D:** Correct. A window computes across related rows without collapsing them into one. In this case: A window function reads the previous row without collapsing it.

### Question 49 — B, E

Answers: Transform with PySpark in a notebook; Use a window function to rank within the partition. PySpark scales the cleansing, and the window function ranks. PySpark handles the row-level and windowed transformations that Spark scales. A window computes across related rows without collapsing them into one. Local study-map skill 2.9 (PySpark Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: PySpark scales the cleansing, and the window function ranks.
- **B:** Correct. A window computes across related rows without collapsing them into one. In this case: PySpark scales the cleansing, and the window function ranks.
- **C:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: PySpark scales the cleansing, and the window function ranks.
- **D:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: PySpark scales the cleansing, and the window function ranks.
- **E:** Correct. PySpark handles the row-level and windowed transformations that Spark scales. In this case: PySpark scales the cleansing, and the window function ranks.

### Question 50 — B

Answer: Transform with Dataflow Gen2 and Power Query. A Dataflow Gen2 is the low-code engine for that team. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Local study-map skill 2.10 (T-SQL and KQL Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. KQL is the native language for the eventhouse tables. Why the correct answer wins: A Dataflow Gen2 is the low-code engine for that team.
- **B:** Correct. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. In this case: A Dataflow Gen2 is the low-code engine for that team.
- **C:** Incorrect for this question. T-SQL is the right engine once the data is relational and already in the warehouse. Why the correct answer wins: A Dataflow Gen2 is the low-code engine for that team.
- **D:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: A Dataflow Gen2 is the low-code engine for that team.

### Question 51 — A, E

Answers: Transform with T-SQL against the warehouse; Transform with KQL in the eventhouse. T-SQL performs the merge, and KQL filters the stream. T-SQL is the right engine once the data is relational and already in the warehouse. KQL is the native language for the eventhouse tables. Local study-map skill 2.10 (T-SQL and KQL Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. T-SQL is the right engine once the data is relational and already in the warehouse. In this case: T-SQL performs the merge, and KQL filters the stream.
- **B:** Incorrect for this question. PySpark handles the row-level and windowed transformations that Spark scales. Why the correct answer wins: T-SQL performs the merge, and KQL filters the stream.
- **C:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: T-SQL performs the merge, and KQL filters the stream.
- **D:** Incorrect for this question. Dataflow Gen2 is the low-code engine for a connector-heavy transformation. Why the correct answer wins: T-SQL performs the merge, and KQL filters the stream.
- **E:** Correct. KQL is the native language for the eventhouse tables. In this case: T-SQL performs the merge, and KQL filters the stream.

### Question 52 — C

Answer: Group and aggregate to the grain the report needs. Grouping to the report grain removes the rows the board discards. Aggregating to the report grain removes rows the report would otherwise discard. Local study-map skill 2.11 (Denormalization, Grouping, and Aggregation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: Grouping to the report grain removes the rows the board discards.
- **B:** Incorrect for this question. Conforming the columns first is what makes the union valid. Why the correct answer wins: Grouping to the report grain removes the rows the board discards.
- **C:** Correct. Aggregating to the report grain removes rows the report would otherwise discard. In this case: Grouping to the report grain removes the rows the board discards.
- **D:** Incorrect for this question. Denormalization trades storage for the query shape the report actually uses. Why the correct answer wins: Grouping to the report grain removes the rows the board discards.

### Question 53 — B

Answer: Union the sources after conforming the columns. The columns must be conformed before the union is valid. Conforming the columns first is what makes the union valid. Local study-map skill 2.11 (Denormalization, Grouping, and Aggregation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Denormalization trades storage for the query shape the report actually uses. Why the correct answer wins: The columns must be conformed before the union is valid.
- **B:** Correct. Conforming the columns first is what makes the union valid. In this case: The columns must be conformed before the union is valid.
- **C:** Incorrect for this question. The pivot is what produces one column per period the report expects. Why the correct answer wins: The columns must be conformed before the union is valid.
- **D:** Incorrect for this question. Aggregating to the report grain removes rows the report would otherwise discard. Why the correct answer wins: The columns must be conformed before the union is valid.

### Question 54 — B

Answer: Deduplicate on the business key and keep the latest version. Keeping the latest version means the surviving row is the one acted on. Keeping the latest version means the surviving row is the one the business already acted on. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: Keeping the latest version means the surviving row is the one acted on.
- **B:** Correct. Keeping the latest version means the surviving row is the one the business already acted on. In this case: Keeping the latest version means the surviving row is the one acted on.
- **C:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Keeping the latest version means the surviving row is the one acted on.
- **D:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Keeping the latest version means the surviving row is the one acted on.

### Question 55 — D

Answer: Process the stream with an eventstream. An eventstream is the no-code path between source and destination. An eventstream is the no-code path from a source to a destination. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. An update policy transforms the data as it lands in the KQL table. Why the correct answer wins: An eventstream is the no-code path between source and destination.
- **B:** Incorrect for this question. Structured streaming suits stateful processing and the same PySpark logic used in batch. Why the correct answer wins: An eventstream is the no-code path between source and destination.
- **C:** Incorrect for this question. A batch job over the landing folder adds latency the streaming requirement may not allow. Why the correct answer wins: An eventstream is the no-code path between source and destination.
- **D:** Correct. An eventstream is the no-code path from a source to a destination. In this case: An eventstream is the no-code path between source and destination.

### Question 56 — B

Answer: Read the watermark → extract only the rows after it → merge into the target → update the watermark. The watermark bounds the extract and moves after the merge. The watermark bounds the extract, the merge applies the delta, and the watermark advances only after the merge succeeds. Local study-map skill 2.13 (Choosing a Streaming Engine), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Nothing has been extracted, so there is nothing to merge, and the watermark moves before the data does. Why the correct answer wins: The watermark bounds the extract and moves after the merge.
- **B:** Correct. The watermark bounds the extract, the merge applies the delta, and the watermark advances only after the merge succeeds. In this case: The watermark bounds the extract and moves after the merge.
- **C:** Incorrect for this question. Advancing the watermark before the merge loses every row the failed merge did not write. Why the correct answer wins: The watermark bounds the extract and moves after the merge.
- **D:** Incorrect for this question. A full extract ignores the watermark, so reading it afterwards adds nothing and the target reloads the history. Why the correct answer wins: The watermark bounds the extract and moves after the merge.

### Question 57 — C

Answer: Use a tumbling window for the fixed five-minute aggregate. A tumbling window covers fixed, non-overlapping intervals. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A hopping window covers overlapping intervals so a trend can be smoothed. Why the correct answer wins: A tumbling window covers fixed, non-overlapping intervals.
- **B:** Incorrect for this question. A materialized view keeps the aggregate fresh instead of recomputing it per query. Why the correct answer wins: A tumbling window covers fixed, non-overlapping intervals.
- **C:** Correct. In this case: A tumbling window covers fixed, non-overlapping intervals.
- **D:** Incorrect for this question. A sliding window emits on the event that satisfies the condition rather than on a fixed boundary. Why the correct answer wins: A tumbling window covers fixed, non-overlapping intervals.

### Question 58 — A

Answer: Create a materialized view for the repeated aggregation. A materialized view keeps the aggregate fresh for every consumer. A materialized view keeps the aggregate fresh instead of recomputing it per query. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. A materialized view keeps the aggregate fresh instead of recomputing it per query. In this case: A materialized view keeps the aggregate fresh for every consumer.
- **B:** Incorrect for this question. The shortcut exposes the data to engines that do not query KQL directly. Why the correct answer wins: A materialized view keeps the aggregate fresh for every consumer.
- **C:** Incorrect for this question. A hopping window covers overlapping intervals so a trend can be smoothed. Why the correct answer wins: A materialized view keeps the aggregate fresh for every consumer.
- **D:** Incorrect for this question. A tumbling window covers fixed, non-overlapping intervals. Why the correct answer wins: A materialized view keeps the aggregate fresh for every consumer.

### Question 59 — A

Answer: Profile the source keys → define the grain of the fact → build the conformed dimensions → add the surrogate keys → load the fact. Keys and grain are settled before the dimensions and the fact. Profiling the keys settles the grain, the grain settles the dimensions, and the fact loads against the keys those dimensions own. Local study-map skill 2.15 (Windowing and Real-Time Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Profiling the keys settles the grain, the grain settles the dimensions, and the fact loads against the keys those dimensions own. In this case: Keys and grain are settled before the dimensions and the fact.
- **B:** Incorrect for this question. The fact is loaded before the keys it references exist. Why the correct answer wins: Keys and grain are settled before the dimensions and the fact.
- **C:** Incorrect for this question. The keys are profiled and the dimensions built before the fact can be loaded. Why the correct answer wins: Keys and grain are settled before the dimensions and the fact.
- **D:** Incorrect for this question. Surrogate keys are assigned by the dimensions, which do not exist yet. Why the correct answer wins: Keys and grain are settled before the dimensions and the fact.

### Question 60 — D

Answer: Detect the duplicates and the late rows → decide the surviving record → correct the affected partition → recompute the aggregate. Detection and the survivor rule precede correction and recompute. The detection comes first, the rule decides the survivor, the partition is corrected, and only then is the published total recomputed. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. A rule chosen before the duplicates are known is chosen blind. Why the correct answer wins: Detection and the survivor rule precede correction and recompute.
- **B:** Incorrect for this question. The partition cannot be corrected before the rule decides which record survives. Why the correct answer wins: Detection and the survivor rule precede correction and recompute.
- **C:** Incorrect for this question. Recomputing before the data is corrected republishes the same wrong total. Why the correct answer wins: Detection and the survivor rule precede correction and recompute.
- **D:** Correct. The detection comes first, the rule decides the survivor, the partition is corrected, and only then is the published total recomputed. In this case: Detection and the survivor rule precede correction and recompute.

### Question 61 — D

Answer: Use the Monitoring hub for the run history. The Monitoring hub lists every run with its status and duration. The hub lists every run with its status, duration, and owning item. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **B:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **C:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The Monitoring hub lists every run with its status and duration.
- **D:** Correct. The hub lists every run with its status, duration, and owning item. In this case: The Monitoring hub lists every run with its status and duration.

### Question 62 — A

Answer: Read the item activity log. The item activity log covers that item's runs. The activity log records the runs of one item with their outcomes. Local study-map skill 3.1 (Monitoring Ingestion and Transformation), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The activity log records the runs of one item with their outcomes. In this case: The item activity log covers that item's runs.
- **B:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The item activity log covers that item's runs.
- **C:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The item activity log covers that item's runs.
- **D:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The item activity log covers that item's runs.

### Question 63 — D

Answer: Read the refresh history for the semantic model. The refresh history records each attempt and its duration. The refresh history separates a failed refresh from a slow one. Local study-map skill 3.2 (Monitoring Semantic Model Refresh), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The refresh history records each attempt and its duration.
- **B:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The refresh history records each attempt and its duration.
- **C:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The refresh history records each attempt and its duration.
- **D:** Correct. The refresh history separates a failed refresh from a slow one. In this case: The refresh history records each attempt and its duration.

### Question 64 — A, C

Answers: Read the refresh history for the semantic model; Send the logs to a Log Analytics workspace. The refresh history triages, and Log Analytics keeps the longer record. The refresh history separates a failed refresh from a slow one. Log Analytics keeps the history that the in-product views expire. Local study-map skill 3.2 (Monitoring Semantic Model Refresh), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. Log Analytics keeps the history that the in-product views expire. In this case: The refresh history triages, and Log Analytics keeps the longer record.
- **B:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The refresh history triages, and Log Analytics keeps the longer record.
- **C:** Correct. The refresh history separates a failed refresh from a slow one. In this case: The refresh history triages, and Log Analytics keeps the longer record.
- **D:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The refresh history triages, and Log Analytics keeps the longer record.
- **E:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The refresh history triages, and Log Analytics keeps the longer record.

### Question 65 — C

Answer: Configure an alert on the failing condition. An alert turns the silent failure into a notification. An alert turns a silent failure into a notification. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The alert must reach the owner, or it becomes noise nobody acts on. Why the correct answer wins: An alert turns the silent failure into a notification.
- **B:** Incorrect for this question. Alerting on success as well as failure trains the team to ignore the alert. Why the correct answer wins: An alert turns the silent failure into a notification.
- **C:** Correct. An alert turns a silent failure into a notification. In this case: An alert turns the silent failure into a notification.
- **D:** Incorrect for this question. An activator rule evaluates the stream and fires when the condition holds. Why the correct answer wins: An alert turns the silent failure into a notification.

### Question 66 — C

Answer: Set the alert to fire only after the retry policy has been exhausted. The alert should wait for the retry policy to be exhausted. Waiting for the retries stops a transient failure being reported as an outage. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Alerting on success as well as failure trains the team to ignore the alert. Why the correct answer wins: The alert should wait for the retry policy to be exhausted.
- **B:** Incorrect for this question. The alert must reach the owner, or it becomes noise nobody acts on. Why the correct answer wins: The alert should wait for the retry policy to be exhausted.
- **C:** Correct. Waiting for the retries stops a transient failure being reported as an outage. In this case: The alert should wait for the retry policy to be exhausted.
- **D:** Incorrect for this question. An alert turns a silent failure into a notification. Why the correct answer wins: The alert should wait for the retry policy to be exhausted.

### Question 67 — B

Answer: Read the activity output of the failed step. The activity output carries the error and its input. The activity output carries the error and the input that produced it. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The refresh error names the step, which is where the transform diverged. Why the correct answer wins: The activity output carries the error and its input.
- **B:** Correct. The activity output carries the error and the input that produced it. In this case: The activity output carries the error and its input.
- **C:** Incorrect for this question. The message names the object or the conversion; the plan explains the cost. Why the correct answer wins: The activity output carries the error and its input.
- **D:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The activity output carries the error and its input.

### Question 68 — A

Answer: Add an error branch so the failure is handled rather than ignored. An error branch turns a silent failure into an explicit outcome. Local study-map skill 3.4 (Pipeline and Dataflow Gen2 Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. In this case: An error branch turns a silent failure into an explicit outcome.
- **B:** Incorrect for this question. Until repeats the check and stops when the condition is met or the timeout expires. Why the correct answer wins: An error branch turns a silent failure into an explicit outcome.
- **C:** Incorrect for this question. A retry absorbs a transient failure that the next attempt would not repeat. Why the correct answer wins: An error branch turns a silent failure into an explicit outcome.
- **D:** Incorrect for this question. The dependency is what makes the failure path execute at all. Why the correct answer wins: An error branch turns a silent failure into an explicit outcome.

### Question 69 — B

Answer: Open the Spark UI for the application. The Spark UI shows where the stages spend their time. The Spark UI shows the stages and tasks where the time went. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The cell output is where the exception is reported with its stack. Why the correct answer wins: The Spark UI shows where the stages spend their time.
- **B:** Correct. The Spark UI shows the stages and tasks where the time went. In this case: The Spark UI shows where the stages spend their time.
- **C:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The Spark UI shows where the stages spend their time.
- **D:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The Spark UI shows where the stages spend their time.

### Question 70 — D

Answer: Inspect the failing cell output and exit value. The failing cell's output reports the exception with its stack. The cell output is where the exception is reported with its stack. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The failing cell's output reports the exception with its stack.
- **B:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The failing cell's output reports the exception with its stack.
- **C:** Incorrect for this question. The Spark UI shows the stages and tasks where the time went. Why the correct answer wins: The failing cell's output reports the exception with its stack.
- **D:** Correct. The cell output is where the exception is reported with its stack. In this case: The failing cell's output reports the exception with its stack.

### Question 71 — B, E

Answers: Open the Spark UI for the application; Inspect the failing cell output and exit value. The UI explains the time, and the cell output explains the failure. The Spark UI shows the stages and tasks where the time went. The cell output is where the exception is reported with its stack. Local study-map skill 3.5 (Notebook Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The UI explains the time, and the cell output explains the failure.
- **B:** Correct. The cell output is where the exception is reported with its stack. In this case: The UI explains the time, and the cell output explains the failure.
- **C:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The UI explains the time, and the cell output explains the failure.
- **D:** Incorrect for this question. Log Analytics keeps the history that the in-product views expire. Why the correct answer wins: The UI explains the time, and the cell output explains the failure.
- **E:** Correct. The Spark UI shows the stages and tasks where the time went. In this case: The UI explains the time, and the cell output explains the failure.

### Question 72 — D

Answer: Inspect the eventstream runtime metrics. The runtime metrics show whether the destination is refusing. The runtime metrics show whether the source or the destination is blocking. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The runtime metrics show whether the destination is refusing.
- **B:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The runtime metrics show whether the destination is refusing.
- **C:** Incorrect for this question. The failures table records the rejected records and the reason for each. Why the correct answer wins: The runtime metrics show whether the destination is refusing.
- **D:** Correct. The runtime metrics show whether the source or the destination is blocking. In this case: The runtime metrics show whether the destination is refusing.

### Question 73 — D, E

Answers: Query the ingestion failures table in the KQL database; Inspect the eventstream runtime metrics. The metrics show the gap, and the failures table shows the records. The failures table records the rejected records and the reason for each. The runtime metrics show whether the source or the destination is blocking. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The metrics show the gap, and the failures table shows the records.
- **B:** Incorrect for this question. The audit log records who did what to which item and when. Why the correct answer wins: The metrics show the gap, and the failures table shows the records.
- **C:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The metrics show the gap, and the failures table shows the records.
- **D:** Correct. The runtime metrics show whether the source or the destination is blocking. In this case: The metrics show the gap, and the failures table shows the records.
- **E:** Correct. The failures table records the rejected records and the reason for each. In this case: The metrics show the gap, and the failures table shows the records.

### Question 74 — A

Answer: Read the T-SQL error message and then the query plan. The T-SQL message names the object or the conversion. The message names the object or the conversion; the plan explains the cost. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The message names the object or the conversion; the plan explains the cost. In this case: The T-SQL message names the object or the conversion.
- **B:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The T-SQL message names the object or the conversion.
- **C:** Incorrect for this question. A shortcut fails for a connection or permission reason more often than for a data reason. Why the correct answer wins: The T-SQL message names the object or the conversion.
- **D:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The T-SQL message names the object or the conversion.

### Question 75 — D

Answer: Check the shortcut connection and the delegated permission. The delegated permission behind the shortcut must be rechecked. A shortcut fails for a connection or permission reason more often than for a data reason. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The message names the object or the conversion; the plan explains the cost. Why the correct answer wins: The delegated permission behind the shortcut must be rechecked.
- **B:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The delegated permission behind the shortcut must be rechecked.
- **C:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The delegated permission behind the shortcut must be rechecked.
- **D:** Correct. A shortcut fails for a connection or permission reason more often than for a data reason. In this case: The delegated permission behind the shortcut must be rechecked.

### Question 76 — D, E

Answers: Read the T-SQL error message and then the query plan; Check the shortcut connection and the delegated permission. The message names the object, and the shortcut needs its permission checked. The message names the object or the conversion; the plan explains the cost. A shortcut fails for a connection or permission reason more often than for a data reason. Local study-map skill 3.7 (T-SQL and Shortcut Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The driver log carries the executor and serialization errors the cell output omits. Why the correct answer wins: The message names the object, and the shortcut needs its permission checked.
- **B:** Incorrect for this question. The activity output carries the error and the input that produced it. Why the correct answer wins: The message names the object, and the shortcut needs its permission checked.
- **C:** Incorrect for this question. The failures table records the rejected records and the reason for each. Why the correct answer wins: The message names the object, and the shortcut needs its permission checked.
- **D:** Correct. A shortcut fails for a connection or permission reason more often than for a data reason. In this case: The message names the object, and the shortcut needs its permission checked.
- **E:** Correct. The message names the object or the conversion; the plan explains the cost. In this case: The message names the object, and the shortcut needs its permission checked.

### Question 77 — B

Answer: Run OPTIMIZE to compact the small files. OPTIMIZE compacts the small files into fewer larger ones. OPTIMIZE rewrites many small files into fewer larger ones. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. A partition on the filter column lets the engine skip the rows it does not need. Why the correct answer wins: OPTIMIZE compacts the small files into fewer larger ones.
- **B:** Correct. OPTIMIZE rewrites many small files into fewer larger ones. In this case: OPTIMIZE compacts the small files into fewer larger ones.
- **C:** Incorrect for this question. V-Order writes the files in a layout the Fabric engines read faster. Why the correct answer wins: OPTIMIZE compacts the small files into fewer larger ones.
- **D:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: OPTIMIZE compacts the small files into fewer larger ones.

### Question 78 — A

Answer: Partition the table on the date column. Partitioning on the filtered column lets the engine skip files. A partition on the filter column lets the engine skip the rows it does not need. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. A partition on the filter column lets the engine skip the rows it does not need. In this case: Partitioning on the filtered column lets the engine skip files.
- **B:** Incorrect for this question. Z-Order clusters related values so a filtered read touches fewer files. Why the correct answer wins: Partitioning on the filtered column lets the engine skip files.
- **C:** Incorrect for this question. OPTIMIZE rewrites many small files into fewer larger ones. Why the correct answer wins: Partitioning on the filtered column lets the engine skip files.
- **D:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: Partitioning on the filtered column lets the engine skip files.

### Question 79 — A

Answer: Coalesce the partitions before writing the small result. Coalesce reduces the file count without a full shuffle. Local study-map skill 3.9 (Optimizing Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. In this case: Coalesce reduces the file count without a full shuffle.
- **B:** Incorrect for this question. Too few partitions leave large tasks; too many add scheduling overhead. Why the correct answer wins: Coalesce reduces the file count without a full shuffle.
- **C:** Incorrect for this question. Repartitioning decides how many files the write produces. Why the correct answer wins: Coalesce reduces the file count without a full shuffle.
- **D:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: Coalesce reduces the file count without a full shuffle.

### Question 80 — A

Answer: Write fewer, larger files into the warehouse table. Fewer, larger files cost less to scan. Many small files cost more to scan than the same rows in fewer files. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. Many small files cost more to scan than the same rows in fewer files. In this case: Fewer, larger files cost less to scan.
- **B:** Incorrect for this question. A join on a different column forces a shuffle of both sides. Why the correct answer wins: Fewer, larger files cost less to scan.
- **C:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Fewer, larger files cost less to scan.
- **D:** Incorrect for this question. The warehouse optimizer plans from statistics, not from the data itself. Why the correct answer wins: Fewer, larger files cost less to scan.

### Question 81 — A, D

Answers: Update statistics so the optimizer sees the current distribution; Join on the distribution column so the rows stay on their node. Statistics fix the estimate, and the distribution key removes the reshuffle. The warehouse optimizer plans from statistics, not from the data itself. A join on a different column forces a shuffle of both sides. Local study-map skill 3.10 (Optimizing the Data Warehouse), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. The warehouse optimizer plans from statistics, not from the data itself. In this case: Statistics fix the estimate, and the distribution key removes the reshuffle.
- **B:** Incorrect for this question. Row-by-row inserts pay the transaction overhead once per row. Why the correct answer wins: Statistics fix the estimate, and the distribution key removes the reshuffle.
- **C:** Incorrect for this question. Many small files cost more to scan than the same rows in fewer files. Why the correct answer wins: Statistics fix the estimate, and the distribution key removes the reshuffle.
- **D:** Correct. A join on a different column forces a shuffle of both sides. In this case: Statistics fix the estimate, and the distribution key removes the reshuffle.
- **E:** Incorrect for this question. Coalesce reduces the file count without a full shuffle. Why the correct answer wins: Statistics fix the estimate, and the distribution key removes the reshuffle.

### Question 82 — D

Answer: Salt the skewed key so the partitions even out. Salting spreads the hot key across partitions. Salting spreads one hot key across several partitions. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Skew handling splits the oversized partition instead of leaving one task to finish alone. Why the correct answer wins: Salting spreads the hot key across partitions.
- **B:** Incorrect for this question. Adaptive execution re-plans from the actual partition sizes at run time. Why the correct answer wins: Salting spreads the hot key across partitions.
- **C:** Incorrect for this question. Broadcasting removes the shuffle of the large side of the join. Why the correct answer wins: Salting spreads the hot key across partitions.
- **D:** Correct. Salting spreads one hot key across several partitions. In this case: Salting spreads the hot key across partitions.

### Question 83 — D

Answer: Broadcast the small dimension to avoid the shuffle. Broadcasting the small side removes the shuffle of the large side. Broadcasting removes the shuffle of the large side of the join. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Caching the reused DataFrame avoids recomputing it for the second action. Why the correct answer wins: Broadcasting the small side removes the shuffle of the large side.
- **B:** Incorrect for this question. Too few partitions leave large tasks; too many add scheduling overhead. Why the correct answer wins: Broadcasting the small side removes the shuffle of the large side.
- **C:** Incorrect for this question. Salting spreads one hot key across several partitions. Why the correct answer wins: Broadcasting the small side removes the shuffle of the large side.
- **D:** Correct. Broadcasting removes the shuffle of the large side of the join. In this case: Broadcasting the small side removes the shuffle of the large side.

### Question 84 — B

Answer: Move the workspace to a larger capacity. Capacity units are the ceiling on everything the workspace runs. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The destination throughput caps how much the eventstream can deliver. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.
- **B:** Correct. In this case: Capacity units are the ceiling on everything the workspace runs.
- **C:** Incorrect for this question. Smoothing lets a short burst use the capacity allowance instead of being throttled. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.
- **D:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.

### Question 85 — C

Answer: Enable capacity smoothing so a burst can borrow from the burst allowance. Smoothing lets the burst use the burst allowance. Smoothing lets a short burst use the capacity allowance instead of being throttled. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: Smoothing lets the burst use the burst allowance.
- **B:** Incorrect for this question. Query throughput is bounded by the eventhouse capacity. Why the correct answer wins: Smoothing lets the burst use the burst allowance.
- **C:** Correct. Smoothing lets a short burst use the capacity allowance instead of being throttled. In this case: Smoothing lets the burst use the burst allowance.
- **D:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: Smoothing lets the burst use the burst allowance.

### Question 86 — B

Answer: Read the query plan → reduce the file count → optimize and Z-Order the table → re-measure the query. The plan decides the action and the second measurement proves it. The plan identifies the cost, compaction and clustering address it, and the measurement proves the effect. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The plan is what should have decided whether compaction was the right fix at all. Why the correct answer wins: The plan decides the action and the second measurement proves it.
- **B:** Correct. The plan identifies the cost, compaction and clustering address it, and the measurement proves the effect. In this case: The plan decides the action and the second measurement proves it.
- **C:** Incorrect for this question. Measuring before the change and again after it is what makes the comparison possible. Why the correct answer wins: The plan decides the action and the second measurement proves it.
- **D:** Incorrect for this question. Optimizing before reading the plan optimizes whatever seemed slow rather than what was costly. Why the correct answer wins: The plan decides the action and the second measurement proves it.

### Question 87 — B

Answer: Open the Spark UI → find the stage with the skewed task → broadcast or salt the join → re-run and compare the stage time. The UI locates the skew before the join is changed. The UI locates the skew, the join strategy addresses it, and the second run is the evidence. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The UI is what does the finding, so it cannot come after it. Why the correct answer wins: The UI locates the skew before the join is changed.
- **B:** Correct. The UI locates the skew, the join strategy addresses it, and the second run is the evidence. In this case: The UI locates the skew before the join is changed.
- **C:** Incorrect for this question. A comparison before any change compares the job with itself. Why the correct answer wins: The UI locates the skew before the join is changed.
- **D:** Incorrect for this question. Salting before locating the skew fixes a guess. Why the correct answer wins: The UI locates the skew before the join is changed.

### Question 88 — C

Answer: Enable the monitoring output → build the dashboard over it → set the alert threshold → review the alert history each week. The output exists before the dashboard and the alert. There is nothing to chart or alert on until the output exists, and the review is what keeps the threshold honest. Local study-map skill 3.3 (Alerts and Data Activator), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. There is no alert history before the alert exists. Why the correct answer wins: The output exists before the dashboard and the alert.
- **B:** Incorrect for this question. The dashboard and the threshold both read an output that does not exist yet. Why the correct answer wins: The output exists before the dashboard and the alert.
- **C:** Correct. There is nothing to chart or alert on until the output exists, and the review is what keeps the threshold honest. In this case: The output exists before the dashboard and the alert.
- **D:** Incorrect for this question. A threshold with no output behind it cannot be evaluated. Why the correct answer wins: The output exists before the dashboard and the alert.

### Question 89 — A

Answer: Add deployment rules so the target stage keeps its own connection and parameters. A deployment rule preserves the target stage's connection. A rule stops a promotion from overwriting the target stage environment-specific settings. Local study-map skill 1.5 (Deployment Pipelines), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Correct. A rule stops a promotion from overwriting the target stage environment-specific settings. In this case: A deployment rule preserves the target stage's connection.
- **B:** Incorrect for this question. The pipeline promotes the same item definitions through the stages instead of rebuilding them. Why the correct answer wins: A deployment rule preserves the target stage's connection.
- **C:** Incorrect for this question. The comparison shows what the promotion will change in the target before it happens. Why the correct answer wins: A deployment rule preserves the target stage's connection.
- **D:** Incorrect for this question. Promoting every item drags unrelated work into the release. Why the correct answer wins: A deployment rule preserves the target stage's connection.

### Question 90 — D

Answer: Certify the item as the approved source. Certification marks the item the board should trust. Certification tells consumers the item has been reviewed as authoritative. Local study-map skill 1.9 (Sensitivity Labels and Endorsement), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Promotion signals readiness without the review that certification implies. Why the correct answer wins: Certification marks the item the board should trust.
- **B:** Incorrect for this question. A default label classifies new items that nobody labels by hand. Why the correct answer wins: Certification marks the item the board should trust.
- **C:** Incorrect for this question. The label travels with the item and drives the protection downstream consumers inherit. Why the correct answer wins: Certification marks the item the board should trust.
- **D:** Correct. Certification tells consumers the item has been reviewed as authoritative. In this case: Certification marks the item the board should trust.

### Question 91 — D

Answer: Read the Fabric audit log in the Microsoft Purview portal. The audit log records who changed and promoted which item. The audit log records who did what to which item and when. Local study-map skill 1.10 (Fabric Audit Logs), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric workspace, security, and lifecycle management: https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces

- **A:** Incorrect for this question. Filtering turns a very large log into the events that answer the question. Why the correct answer wins: The audit log records who changed and promoted which item.
- **B:** Incorrect for this question. The audit log has a retention window, so an investigation that starts late needs the export. Why the correct answer wins: The audit log records who changed and promoted which item.
- **C:** Incorrect for this question. The activity log records the runs of one item with their outcomes. Why the correct answer wins: The audit log records who changed and promoted which item.
- **D:** Correct. The audit log records who did what to which item and when. In this case: The audit log records who changed and promoted which item.

### Question 92 — B

Answer: Deduplicate on the business key and keep the latest record. Deduplication leaves one row per business key. Deduplication makes the target one row per business key. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Reprocessing the partition corrects the aggregate that was already published. Why the correct answer wins: Deduplication leaves one row per business key.
- **B:** Correct. Deduplication makes the target one row per business key. In this case: Deduplication leaves one row per business key.
- **C:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Deduplication leaves one row per business key.
- **D:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Deduplication leaves one row per business key.

### Question 93 — B

Answer: Generate a surrogate key instead of reusing the source key. A surrogate key distinguishes bookings that share a reference. A surrogate key decouples the warehouse from the source system identifiers. Local study-map skill 2.1 (Full and Incremental Load Patterns), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: A surrogate key distinguishes bookings that share a reference.
- **B:** Correct. A surrogate key decouples the warehouse from the source system identifiers. In this case: A surrogate key distinguishes bookings that share a reference.
- **C:** Incorrect for this question. A merge updates the existing row and inserts the new one in the same step. Why the correct answer wins: A surrogate key distinguishes bookings that share a reference.
- **D:** Incorrect for this question. Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite. Why the correct answer wins: A surrogate key distinguishes bookings that share a reference.

### Question 94 — A

Answer: Deduplicate on the business key and keep the latest version. Keeping the latest version leaves the row the business already used. Keeping the latest version means the surviving row is the one the business already acted on. Local study-map skill 2.12 (Duplicate, Missing, and Late-Arriving Data), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric ingestion and transformation, lakehouse, warehouse, and Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview

- **A:** Correct. Keeping the latest version means the surviving row is the one the business already acted on. In this case: Keeping the latest version leaves the row the business already used.
- **B:** Incorrect for this question. A documented default keeps the aggregate correct instead of dropping the row. Why the correct answer wins: Keeping the latest version leaves the row the business already used.
- **C:** Incorrect for this question. Deduplication makes the target one row per business key. Why the correct answer wins: Keeping the latest version leaves the row the business already used.
- **D:** Incorrect for this question. A reject table preserves the bad rows for correction without stopping the load. Why the correct answer wins: Keeping the latest version leaves the row the business already used.

### Question 95 — C

Answer: Inspect the eventstream runtime metrics. The runtime metrics show whether the source or the destination is limiting. The runtime metrics show whether the source or the destination is blocking. Local study-map skill 3.6 (Eventhouse and Eventstream Errors), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The hub lists every run with its status, duration, and owning item. Why the correct answer wins: The runtime metrics show whether the source or the destination is limiting.
- **B:** Incorrect for this question. The failures table records the rejected records and the reason for each. Why the correct answer wins: The runtime metrics show whether the source or the destination is limiting.
- **C:** Correct. The runtime metrics show whether the source or the destination is blocking. In this case: The runtime metrics show whether the source or the destination is limiting.
- **D:** Incorrect for this question. The refresh history separates a failed refresh from a slow one. Why the correct answer wins: The runtime metrics show whether the source or the destination is limiting.

### Question 96 — A

Answer: Set the retention policy to match the query window. Retention beyond the query window pays for data nobody reads. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. In this case: Retention beyond the query window pays for data nobody reads.
- **B:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: Retention beyond the query window pays for data nobody reads.
- **C:** Incorrect for this question. Query throughput is bounded by the eventhouse capacity. Why the correct answer wins: Retention beyond the query window pays for data nobody reads.
- **D:** Incorrect for this question. The caching policy keeps the hot window on fast storage. Why the correct answer wins: Retention beyond the query window pays for data nobody reads.

### Question 97 — D

Answer: Set the caching policy on the KQL table. The caching policy keeps the hot window on fast storage. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. Capacity units are the ceiling on everything the workspace runs. Why the correct answer wins: The caching policy keeps the hot window on fast storage.
- **B:** Incorrect for this question. Query throughput is bounded by the eventhouse capacity. Why the correct answer wins: The caching policy keeps the hot window on fast storage.
- **C:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: The caching policy keeps the hot window on fast storage.
- **D:** Correct. In this case: The caching policy keeps the hot window on fast storage.

### Question 98 — C

Answer: Run OPTIMIZE to compact the small files. OPTIMIZE compacts the small files into fewer larger ones. OPTIMIZE rewrites many small files into fewer larger ones. Local study-map skill 3.8 (Optimizing Lakehouse Tables), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. A partition on the filter column lets the engine skip the rows it does not need. Why the correct answer wins: OPTIMIZE compacts the small files into fewer larger ones.
- **B:** Incorrect for this question. V-Order writes the files in a layout the Fabric engines read faster. Why the correct answer wins: OPTIMIZE compacts the small files into fewer larger ones.
- **C:** Correct. OPTIMIZE rewrites many small files into fewer larger ones. In this case: OPTIMIZE compacts the small files into fewer larger ones.
- **D:** Incorrect for this question. VACUUM reclaims the storage that deleted versions still hold. Why the correct answer wins: OPTIMIZE compacts the small files into fewer larger ones.

### Question 99 — A

Answer: Salt the skewed key so the partitions even out. Salting spreads the hot key across partitions. Salting spreads one hot key across several partitions. Local study-map skill 3.11 (Optimizing Spark Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Correct. Salting spreads one hot key across several partitions. In this case: Salting spreads the hot key across partitions.
- **B:** Incorrect for this question. Adaptive execution re-plans from the actual partition sizes at run time. Why the correct answer wins: Salting spreads the hot key across partitions.
- **C:** Incorrect for this question. Skew handling splits the oversized partition instead of leaving one task to finish alone. Why the correct answer wins: Salting spreads the hot key across partitions.
- **D:** Incorrect for this question. Broadcasting removes the shuffle of the large side of the join. Why the correct answer wins: Salting spreads the hot key across partitions.

### Question 100 — C

Answer: Move the workspace to a larger capacity. Capacity units are the ceiling on everything the workspace runs. Local study-map skill 3.12 (Optimizing Query and Real-Time Performance), mapped to the official guide: Microsoft DP-700 study guide, skills measured as of October 19, 2026 Primary reference: Fabric monitoring and performance optimization: https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs

- **A:** Incorrect for this question. The destination throughput caps how much the eventstream can deliver. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.
- **B:** Incorrect for this question. Retention beyond the query window pays for data nobody reads. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.
- **C:** Correct. In this case: Capacity units are the ceiling on everything the workspace runs.
- **D:** Incorrect for this question. Smoothing lets a short burst use the capacity allowance instead of being throttled. Why the correct answer wins: Capacity units are the ceiling on everything the workspace runs.
