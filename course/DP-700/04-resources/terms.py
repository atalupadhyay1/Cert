"""Option bank for DP-700: one label and one meaning per answer or distractor.

Keys are stable and referenced by questions/*.txt. Adding an option means
adding it here first; build.py rejects an unknown key.
"""
TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term: {key}')
    TERMS[key] = (label, meaning)


# ---------------------------------------------------------------- domain 1
# Spark workspace settings.
t('sparkpool', 'Set a workspace-level custom Spark pool for the notebooks',
  'A workspace Spark pool applies one node size and autoscale bound to every notebook that does not override it.')
t('sparknodes', 'Size the pool for the node family and node count the workload needs',
  'The node family sets the memory-to-core ratio, and the node count sets the parallelism ceiling.')
t('autoscale', 'Enable autoscale with a minimum and maximum node count',
  'Autoscale adds executors while the job runs and releases them afterwards, so idle capacity is not billed.')
t('dynalloc', 'Enable dynamic allocation so idle executors are released during the run',
  'Dynamic allocation shrinks the executor set between stages, which matters when the stages are uneven.')
t('highconc', 'Enable high concurrency mode for shared sessions',
  'High concurrency lets several notebooks share one Spark session instead of starting a session each.')
t('sparkenv', 'Attach a custom Spark environment to the notebook',
  'An environment carries the library set and Spark properties, so every run starts from the same definition.')
t('libpin', 'Pin the library version in the environment instead of installing it in the notebook',
  'An inline install changes the dependency per notebook and makes a run impossible to reproduce.')
t('sparkdefault', 'Set the default environment at the workspace level',
  'A workspace default environment means a new notebook inherits the approved libraries without a decision.')

# Domain and OneLake workspace settings.
t('domainassign', 'Assign the workspace to the domain that owns the subject area',
  'A domain groups workspaces for governance and discovery without moving the data.')
t('onelakeon', 'Keep OneLake availability enabled so other engines can read the same data',
  'OneLake availability is what lets the warehouse and other workspaces read the same Delta files.')
t('regionfixed', 'Create the workspace in the required region at creation time',
  'The workspace region is fixed at creation, so the decision cannot be corrected by a later setting.')
t('capacityhead', 'Assign the workspace to a capacity that has headroom',
  'Every item in the workspace draws on one capacity, so an undersized capacity throttles all of them.')

# Apache Airflow workspace settings.
t('airflowenable', 'Enable the Apache Airflow job in the workspace and author the DAG',
  'The Airflow job runs Python DAGs inside Fabric, which suits orchestration that already exists as a DAG.')
t('airflowgit', 'Sync the Airflow DAG from the connected Git repository',
  'Source-controlled DAGs keep the orchestration reviewable like any other item definition.')
t('airflowmigrate', 'Rewrite the existing orchestration as a Fabric pipeline instead',
  'Rewriting discards working logic and is only justified when the DAG cannot run in Fabric.')

# Version control and database projects.
t('gitconnect', 'Connect the workspace to a Git repository and commit the item definitions',
  'Git keeps a reviewable history of every item definition instead of an untracked live workspace.')
t('gitbranch', 'Work in a feature branch and merge through a pull request',
  'Branching keeps unfinished work out of the shared workspace and makes the change reviewable.')
t('gitconflict', 'Resolve the conflict by choosing the definition that must win, then commit',
  'An unresolved conflict blocks the update and leaves the workspace and the branch out of step.')
t('gitignorecache', 'Add the generated artefacts to the ignore file rather than committing them',
  'Committing build output makes every run look like a change.')
t('dbproj', 'Create a database project and deploy the schema from it',
  'A database project keeps the warehouse schema in source control and deploys it repeatably.')
t('dbprojdacpac', 'Build the project into a DACPAC and deploy that artefact',
  'The DACPAC is the versioned schema artefact that the deployment consumes.')
t('sqlcmdvar', 'Use SQLCMD variables for the environment-specific values',
  'SQLCMD variables keep one project artefact deployable to both test and production.')

# Deployment pipelines.
t('deploypipe', 'Create a deployment pipeline with development, test, and production stages',
  'The pipeline promotes the same item definitions through the stages instead of rebuilding them.')
t('deployrules', 'Add deployment rules so the target stage keeps its own connection and parameters',
  'A rule stops a promotion from overwriting the target stage environment-specific settings.')
t('deployselect', 'Select only the items that belong in the target stage',
  'Promoting every item drags unrelated work into the release.')
t('deployback', 'Deploy backwards to recover the last known-good definition',
  'A backward deployment is the supported way to restore a previous stage state.')
t('deploycompare', 'Compare the stages before promoting',
  'The comparison shows what the promotion will change in the target before it happens.')

# Workspace and item access.
t('wsrole', 'Grant the user a workspace role',
  'A workspace role is the coarse grant that every item in the workspace inherits.')
t('wsadmin', 'Grant Admin on the workspace to the platform team',
  'Admin is needed to manage access and settings, not to read the data.')
t('wsviewer', 'Grant Viewer on the workspace',
  'Viewer allows reading the items without editing them.')
t('itemshare', 'Share the single item with the user who needs only that item',
  'Item-level sharing avoids granting a workspace role for one report.')
t('itemread', 'Grant Read on the item',
  'Read is the narrowest grant that still lets the item be consumed.')
t('sharelink', 'Share a link to the item with the required permission',
  'A link is a shortcut to the item, not a substitute for the permission behind it.')

# Row, column, object, and file-level security.
t('rls', 'Define a row-level security policy on the table',
  'Row-level security filters rows per identity, so one table returns different rows to different users.')
t('rlspredicate', 'Filter the table through a predicate that resolves the user to a region',
  'The predicate must resolve the identity to the region, or every user sees the same rows.')
t('cls', 'Apply column-level security so the column is hidden from the group',
  'Column-level security hides the column while leaving the rest of the table readable.')
t('ols', 'Apply object-level security in the semantic model',
  'Object-level security hides a table or column from a role in the semantic model.')
t('folderacl', 'Grant access at the folder that holds the restricted files',
  'A folder grant restricts the path without hiding the whole lakehouse.')
t('fileacl', 'Grant access at the individual file',
  'A file-level grant is the narrowest path restriction the platform offers.')

# Dynamic data masking.
t('ddm', 'Apply dynamic data masking to the column',
  'Masking shows a masked value to unauthorised users while the stored data stays intact.')
t('ddmexempt', 'Exempt the authorised group from the mask',
  'The masking rule needs the exemption, or the authorised group sees masked values too.')
t('ddmview', 'Expose a view with the column omitted instead of masking it',
  'A view removes the column entirely, which is not the same as masking the value.')
t('ddmnomask', 'Mask the column in the report layer only',
  'A report-level mask protects one visual and leaves every other consumer unmasked.')

# Sensitivity labels and endorsement.
t('sensitivity', 'Apply the sensitivity label to the item',
  'The label travels with the item and drives the protection downstream consumers inherit.')
t('labelinherit', 'Let the label inherit from the labelled source file',
  'Inheritance keeps one classification instead of a second opinion on the same data.')
t('labeldefault', 'Set the default sensitivity label for the workspace',
  'A default label classifies new items that nobody labels by hand.')
t('certify', 'Certify the item as the approved source',
  'Certification tells consumers the item has been reviewed as authoritative.')
t('promote', 'Promote the item as ready for reuse',
  'Promotion signals readiness without the review that certification implies.')

# Fabric audit logs.
t('auditlog', 'Read the Fabric audit log in the Microsoft Purview portal',
  'The audit log records who did what to which item and when.')
t('auditfilter', 'Filter the audit log by activity and by item',
  'Filtering turns a very large log into the events that answer the question.')
t('auditexport', 'Export the audit events before the retention window closes',
  'The audit log has a retention window, so an investigation that starts late needs the export.')

# OneLake security.
t('onelakesec', 'Configure OneLake security roles for the lakehouse',
  'OneLake security governs data access independently of the workspace role.')
t('onelakesecfolder', 'Scope the OneLake role to the folder that holds the restricted table',
  'A folder-scoped role restricts exactly the data rather than the whole lakehouse.')
t('onelakesecgroup', 'Grant the OneLake role to a security group rather than to individuals',
  'A group grant is maintained once instead of once per person.')

# Choosing between Dataflow Gen2, pipeline, and notebook.
t('pickdataflow', 'Use a Dataflow Gen2 for the transformation',
  'A Dataflow Gen2 suits a transformation that is expressible in Power Query.')
t('pickpipeline', 'Use a pipeline for the copy and the orchestration',
  'A pipeline owns the scheduling, the copy activity, and the dependency between steps.')
t('picknotebook', 'Use a notebook for the transformation',
  'A notebook is the right place for PySpark that a low-code transform cannot express.')
t('picksql', 'Use a T-SQL script against the warehouse',
  'Set-based T-SQL is the natural choice when the data already sits in the warehouse.')
t('pickkql', 'Use a KQL query against the eventhouse',
  'KQL is the native language of the eventhouse tables.')

# Schedules, event triggers, and dynamic parameters.
t('schedule', 'Add a schedule trigger with the cadence and time zone the business expects',
  'The schedule trigger is what makes the run recur without a person starting it.')
t('eventtrig', 'Add an event-based trigger so the run starts when the file arrives',
  'An event trigger removes the gap between the file landing and the run starting.')
t('filearrival', 'Trigger on the file-created event for the landing folder',
  'The file-created event is the signal that the extract has finished arriving.')
t('pipelineparam', 'Pass the folder path as a pipeline parameter',
  'A parameter makes one pipeline reusable across folders and environments.')
t('dynamicexpr', 'Build the path with a dynamic expression at run time',
  'A dynamic expression computes the path instead of hard-coding a date.')
t('foreach', 'Iterate a ForEach activity over the returned list',
  'ForEach applies the same pattern to every object the lookup returned.')
t('invokepipeline', 'Call a child pipeline from the parent pipeline',
  'A child pipeline keeps one reusable pattern instead of copied activities.')
t('lookup', 'Look up the stored watermark before the copy',
  'The lookup is what makes the load incremental rather than a full reload.')
t('until', 'Use an Until loop with a timeout for the long-running check',
  'Until repeats the check and stops when the condition is met or the timeout expires.')
t('setvariable', 'Set the value in a pipeline variable and reference the variable',
  'A variable carries the computed value between the activities that need it.')

# ---------------------------------------------------------------- domain 2
# Full and incremental loads.
t('fullload', 'Run a full load and overwrite the target',
  'A full load is simple, but it reloads the whole history every time it runs.')
t('incremental', 'Load only the rows newer than the stored watermark',
  'An incremental load moves the delta instead of the history.')
t('watermark', 'Store the last successful load timestamp in a control table',
  'The control table is what lets the next run know where this one stopped.')
t('upsert', 'Merge the incoming rows into the target on the business key',
  'A merge updates the existing row and inserts the new one in the same step.')
t('scd2', 'Build a type 2 dimension with validity dates and a current flag',
  'Type 2 keeps the history, so an attribute change becomes a new row instead of an overwrite.')
t('surrogate', 'Generate a surrogate key instead of reusing the source key',
  'A surrogate key decouples the warehouse from the source system identifiers.')
t('latearrive', 'Reprocess the affected partitions when the data arrives late',
  'Reprocessing the partition corrects the aggregate that was already published.')
t('dedupe', 'Deduplicate on the business key and keep the latest record',
  'Deduplication makes the target one row per business key.')
t('nullfill', 'Replace the missing value with a documented default',
  'A documented default keeps the aggregate correct instead of dropping the row.')
t('reject', 'Route the failed rows to a reject table and continue the load',
  'A reject table preserves the bad rows for correction without stopping the load.')

# Choosing a data store.
t('lakehousefiles', 'Land the extract in the lakehouse Files area',
  'The Files area keeps the raw extract in its original format.')
t('lakehousetable', 'Write the curated table into the lakehouse Tables area',
  'A Delta table in Tables is what the SQL analytics endpoint exposes.')
t('warehouse', 'Load the curated model into the warehouse',
  'A warehouse gives multi-table T-SQL transactions and a governed relational model.')
t('eventhouse', 'Store the telemetry in an eventhouse KQL database',
  'An eventhouse is optimized for high-volume time-series queries.')
t('sqlendpoint', 'Query the lakehouse through its SQL analytics endpoint',
  'The endpoint gives read-only T-SQL over the Delta tables without a copy.')
t('kqldb', 'Create a KQL database for the time-series queries',
  'A KQL database indexes the timestamp column for the range queries the dashboards run.')

# Choosing a transformation engine.
t('pyspark', 'Transform with PySpark in a notebook',
  'PySpark handles the row-level and windowed transformations that Spark scales.')
t('tspark', 'Transform with T-SQL against the warehouse',
  'T-SQL is the right engine once the data is relational and already in the warehouse.')
t('kqlx', 'Transform with KQL in the eventhouse',
  'KQL is the native language for the eventhouse tables.')
t('dfg2', 'Transform with Dataflow Gen2 and Power Query',
  'Dataflow Gen2 is the low-code engine for a connector-heavy transformation.')

# OneLake shortcuts.
t('shortcutint', 'Create an internal OneLake shortcut to the other lakehouse table',
  'An internal shortcut points at another Fabric item without copying the data.')
t('shortcutadls', 'Create an ADLS Gen2 shortcut to the external container',
  'The shortcut exposes the external container as if the files were in OneLake.')
t('shortcutnocopy', 'Create a shortcut rather than a copy when the source stays authoritative',
  'A shortcut has no second copy to keep in step with the source.')
t('shortcutqa', 'Enable query acceleration on the shortcut',
  'Query acceleration caches the columns a report reads, so the remote source is not scanned per query.')
t('shortcutcache', 'Copy the remote data into a local table instead of shortcutting it',
  'A copy duplicates the data, so the source of truth is no longer one place.')

# Mirroring.
t('mirroring', 'Enable mirroring for the operational database',
  'Mirroring replicates the source tables continuously into OneLake.')
t('mirrorcdc', 'Rely on change data capture so the mirror needs no pipeline schedule',
  'Change data capture streams the changes instead of a periodic full compare.')
t('mirrorreplica', 'Mirror from a read replica so the source database keeps its capacity',
  'The replica absorbs the read load the mirror creates.')

# Pipeline ingestion.
t('copyact', 'Use a Copy activity in the pipeline',
  'The Copy activity moves the files or rows as one orchestrated step.')
t('copyappend', 'Append the new files instead of overwriting the target',
  'Appending preserves the earlier loads that the incremental pattern depends on.')
t('copybinary', 'Copy the files as binary and parse them downstream',
  'A binary copy keeps the source exactly as delivered for later validation.')
t('getmeta', 'Use Get Metadata to list the files to process',
  'Get Metadata turns an unknown folder into a list the loop can iterate.')
t('deletesrc', 'Delete the processed source file after the load succeeds',
  'Deleting after success prevents the same file being loaded twice.')

# Transformation shapes.
t('denormalize', 'Denormalize the model so the report needs no join',
  'Denormalization trades storage for the query shape the report actually uses.')
t('starschema', 'Model the data as a star schema with conformed dimensions',
  'A star schema keeps the fact table narrow and the dimensions reusable.')
t('groupagg', 'Group and aggregate to the grain the report needs',
  'Aggregating to the report grain removes rows the report would otherwise discard.')
t('windowfn', 'Use a window function to rank within the partition',
  'A window computes across related rows without collapsing them into one.')
t('pivotx', 'Pivot the rows into the reporting columns',
  'The pivot is what produces one column per period the report expects.')
t('unionconf', 'Union the sources after conforming the columns',
  'Conforming the columns first is what makes the union valid.')

# Duplicate, missing, and late-arriving data.
t('dedupekeep', 'Deduplicate on the business key and keep the latest version',
  'Keeping the latest version means the surviving row is the one the business already acted on.')
t('dedupeall', 'Keep every version and let the report choose',
  'Keeping every version pushes the decision to every consumer and every report.')
t('latereprocess', 'Reprocess the closed window when a late event arrives',
  'Reprocessing the window is what corrects a total that was already reported.')
t('latedrop', 'Drop the late event because its window has closed',
  'Dropping the event silently understates the total it belonged to.')
t('nullzero', 'Replace the null with zero before the aggregate',
  'Zero is a value, so it changes an average even when the measure is a sum.')

# Choosing a streaming engine.
t('eventstream', 'Process the stream with an eventstream',
  'An eventstream is the no-code path from a source to a destination.')
t('sparkss', 'Process the stream with Spark structured streaming',
  'Structured streaming suits stateful processing and the same PySpark logic used in batch.')
t('kqlstream', 'Process the stream with a KQL update policy',
  'An update policy transforms the data as it lands in the KQL table.')
t('batchstream', 'Run a batch job every few minutes over the landing folder',
  'A batch job over the landing folder adds latency the streaming requirement may not allow.')

# Eventstream, structured streaming, windowing, real-time tables.
t('materialized', 'Create a materialized view for the repeated aggregation',
  'A materialized view keeps the aggregate fresh instead of recomputing it per query.')
t('tumbling', 'Use a tumbling window for the fixed five-minute aggregate',
  'A tumbling window covers fixed, non-overlapping intervals.')
t('hopping', 'Use a hopping window when the intervals must overlap',
  'A hopping window covers overlapping intervals so a trend can be smoothed.')
t('sliding', 'Use a sliding window that emits when the condition is met',
  'A sliding window emits on the event that satisfies the condition rather than on a fixed boundary.')
t('native', 'Store the stream in native tables in the eventhouse',
  'Native tables give full KQL capability over the streaming data.')
t('shortcutrt', 'Query the stream through a OneLake shortcut',
  'The shortcut exposes the data to engines that do not query KQL directly.')
t('checkpoint', 'Set a checkpoint location for the streaming query',
  'The checkpoint is what makes the stream restart from where it stopped.')
t('watermarking', 'Set a watermark so late events are handled deterministically',
  'A watermark sets how long the engine waits for late events before closing a window.')

# ---------------------------------------------------------------- domain 3
# Monitoring.
t('monitorhub', 'Use the Monitoring hub for the run history',
  'The hub lists every run with its status, duration, and owning item.')
t('refreshhist', 'Read the refresh history for the semantic model',
  'The refresh history separates a failed refresh from a slow one.')
t('activitylog', 'Read the item activity log',
  'The activity log records the runs of one item with their outcomes.')
t('loganalytics', 'Send the logs to a Log Analytics workspace',
  'Log Analytics keeps the history that the in-product views expire.')
t('sparkui', 'Open the Spark UI for the application',
  'The Spark UI shows the stages and tasks where the time went.')
t('notebookcell', 'Inspect the failing cell output and exit value',
  'The cell output is where the exception is reported with its stack.')
t('kqlingestfail', 'Query the ingestion failures table in the KQL database',
  'The failures table records the rejected records and the reason for each.')
t('eventstreammetric', 'Inspect the eventstream runtime metrics',
  'The runtime metrics show whether the source or the destination is blocking.')
t('queryplan', 'Read the query plan for the expensive operator',
  'The plan shows which operator consumed the time.')
t('stats', 'Check the statistics the optimizer used',
  'Stale statistics make the optimizer choose the wrong join.')
t('dashboard', 'Build a real-time dashboard over the monitoring table',
  'A dashboard over the monitoring table makes the trend visible between runs.')

# Alerts and Data Activator.
t('alert', 'Configure an alert on the failing condition',
  'An alert turns a silent failure into a notification.')
t('activator', 'Use a Data Activator rule that watches the streaming condition',
  'An activator rule evaluates the stream and fires when the condition holds.')
t('alertowner', 'Send the alert to the team that owns the item',
  'The alert must reach the owner, or it becomes noise nobody acts on.')
t('alertnoise', 'Alert on every successful run as well as every failure',
  'Alerting on success as well as failure trains the team to ignore the alert.')
t('alertdelay', 'Set the alert to fire only after the retry policy has been exhausted',
  'Waiting for the retries stops a transient failure being reported as an outage.')

# Errors.
t('pipelineerr', 'Read the activity output of the failed step',
  'The activity output carries the error and the input that produced it.')
t('dataflowerr', 'Inspect the Dataflow Gen2 refresh error for the failing query step',
  'The refresh error names the step, which is where the transform diverged.')
t('notebookerr', 'Check the failing cell and the Spark driver log',
  'The driver log carries the executor and serialization errors the cell output omits.')
t('eventhouseerr', 'Check the ingestion failures for the KQL table',
  'The failures table names the record and the schema mismatch that rejected it.')
t('eventstreamerr', 'Inspect the eventstream runtime metrics for the blocked destination',
  'The metrics show whether the source is starving or the destination is refusing.')
t('tsqlerr', 'Read the T-SQL error message and then the query plan',
  'The message names the object or the conversion; the plan explains the cost.')
t('shortcuterr', 'Check the shortcut connection and the delegated permission',
  'A shortcut fails for a connection or permission reason more often than for a data reason.')
t('retry', 'Add a retry policy with a delay to the failing activity',
  'A retry absorbs a transient failure that the next attempt would not repeat.')
t('errbranch', 'Add an error branch so the failure is handled rather than ignored',
  'An error branch turns a silent failure into an explicit outcome.')
t('dependency', 'Set the failure dependency so the handler runs when the step fails',
  'The dependency is what makes the failure path execute at all.')

# Optimizing lakehouse tables.
t('vorder', 'Enable V-Order on the table',
  'V-Order writes the files in a layout the Fabric engines read faster.')
t('optimize', 'Run OPTIMIZE to compact the small files',
  'OPTIMIZE rewrites many small files into fewer larger ones.')
t('vacuum', 'Run VACUUM to remove the files the table no longer references',
  'VACUUM reclaims the storage that deleted versions still hold.')
t('partition', 'Partition the table on the date column',
  'A partition on the filter column lets the engine skip the rows it does not need.')
t('zorder', 'Apply Z-Order on the frequently filtered columns',
  'Z-Order clusters related values so a filtered read touches fewer files.')
t('liquidclustering', 'Use liquid clustering instead of a fixed partition column',
  'Liquid clustering adapts to the query pattern instead of freezing one partition key.')

# Optimizing pipelines.
t('parallelcopy', 'Raise the parallelism of the copy so independent slices move together',
  'Independent slices that run one after another waste the capacity the run already has.')
t('broadcastjoin', 'Broadcast the small dimension to avoid the shuffle',
  'Broadcasting removes the shuffle of the large side of the join.')
t('shuffleparts', 'Set the shuffle partition count to match the data volume',
  'Too few partitions leave large tasks; too many add scheduling overhead.')
t('cache', 'Cache the DataFrame that is used twice',
  'Caching the reused DataFrame avoids recomputing it for the second action.')
t('salt', 'Salt the skewed key so the partitions even out',
  'Salting spreads one hot key across several partitions.')
t('repartition', 'Repartition before the write to control the file count',
  'Repartitioning decides how many files the write produces.')
t('coalesce', 'Coalesce the partitions before writing the small result',
  'Coalesce reduces the file count without a full shuffle.')

# Optimizing the warehouse.
t('batchinsert', 'Insert the warehouse rows in batches rather than one at a time',
  'Row-by-row inserts pay the transaction overhead once per row.')
t('dwstats', 'Update statistics so the optimizer sees the current distribution',
  'The warehouse optimizer plans from statistics, not from the data itself.')
t('dwjoin', 'Join on the distribution column so the rows stay on their node',
  'A join on a different column forces a shuffle of both sides.')
t('dwfilecount', 'Write fewer, larger files into the warehouse table',
  'Many small files cost more to scan than the same rows in fewer files.')

# Optimizing Spark.
t('broadcastthr', 'Raise the broadcast threshold for the small table',
  'A threshold below the table size silently disables the broadcast plan.')
t('aqe', 'Keep adaptive query execution enabled so the shuffle is re-planned',
  'Adaptive execution re-plans from the actual partition sizes at run time.')
t('skewjoin', 'Enable skew join handling for the hot key',
  'Skew handling splits the oversized partition instead of leaving one task to finish alone.')
t('writepart', 'Partition by the column the readers filter on',
  'The write layout decides whether a reader can prune at all.')

# Optimizing query and real-time performance.
t('capacityscale', 'Move the workspace to a larger capacity',
  'Capacity units are the ceiling on everything the workspace runs.')
t('smoothing', 'Enable capacity smoothing so a burst can borrow from the burst allowance',
  'Smoothing lets a short burst use the capacity allowance instead of being throttled.')
t('retention', 'Set the retention policy to match the query window',
  'Retention beyond the query window pays for data nobody reads.')
t('cachingpolicy', 'Set the caching policy on the KQL table',
  'The caching policy keeps the hot window on fast storage.')
t('eventhousescale', 'Increase the eventhouse capacity so the queries keep up',
  'Query throughput is bounded by the eventhouse capacity.')
t('streamthroughput', 'Scale the destination throughput for the event volume',
  'The destination throughput caps how much the eventstream can deliver.')
t('kqlmaterialize', 'Materialize the repeated aggregation in the KQL database',
  'Materializing the aggregate stops every dashboard tile recomputing it.')

# The sequencing bank is merged last so a sequencing item can be authored as
# an ordinary single-answer item whose four options are four candidate orders.
from sequences import SEQUENCES  # noqa: E402

for _key, _value in SEQUENCES.items():
    if _key in TERMS:
        raise ValueError(f'Duplicate term: {_key}')
    TERMS[_key] = _value
