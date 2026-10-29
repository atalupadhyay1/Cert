"""Canonical option dictionary for Exam DP-600: Implementing Analytics Solutions Using Microsoft Fabric.

Aligned to the official Microsoft Learn Study Guide (Skills measured as of October 19, 2026).
Every key maps to `(option_label, detailed_option_explanation)` and is referenced across
the 600-question bank so every correct answer and distractor carries a concrete, exam-accurate
architectural explanation.
"""

TERMS = {}


def t(key: str, label: str, explanation: str) -> None:
    if key in TERMS:
        raise ValueError(f'Duplicate term key: {key}')
    TERMS[key] = (label, explanation)


# ============================================================================
# DOMAIN 1 — Maintain a data analytics solution (Skills 1.1 – 1.11)
# ============================================================================

# --- 1.1 Workspace-level access controls ---
t('ws_admin',
  'Assign the Workspace Admin role',
  'Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items.')
t('ws_member',
  'Assign the Workspace Member role',
  'Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins.')
t('ws_contributor',
  'Assign the Workspace Contributor role',
  'Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS.')
t('ws_viewer',
  'Assign the Workspace Viewer role',
  'Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules.')
t('entra_sec_group',
  'Assign permissions to Microsoft Entra security groups rather than individual users',
  'Granting workspace, item, deployment-pipeline, and RLS role memberships to Microsoft Entra security groups centralizes joiner/mover/leaver governance and scales across workspaces without per-user ACL drift.')

# --- 1.2 Item-level access controls ---
t('item_share_read',
  'Share the item with Read permission only (no ReadData or ReadAll)',
  'Item-level Read metadata permission lets a user connect to a Lakehouse or Warehouse item container without granting broad OneLake file access; combine with SELECT or OneLake security roles for granular least-privilege access.')
t('item_share_readall',
  'Share the Lakehouse with ReadAll (Read all Apache Spark data) permission',
  'ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled.')
t('item_share_readdata',
  'Share the item with ReadData (Read all SQL endpoint data) permission',
  'ReadData grants SELECT across all tables/views in the SQL analytics endpoint or Warehouse without granting direct Spark/ABFS access to underlying Lakehouse files.')
t('item_build_perm',
  'Grant Build permission on the shared semantic model',
  'Build permission on a semantic model allows analysts to create new Power BI reports, use Analyze in Excel, and issue XMLA/DAX queries against the model without granting workspace Contributor rights or underlying Lakehouse access.')
t('dl_fixed_identity',
  'Bind the Direct Lake semantic model to a cloud connection with a fixed identity and disable SSO',
  'Configuring a fixed-identity cloud connection (Service Principal or Workspace Identity) with SSO disabled lets report consumers query the Direct Lake model enforced by semantic-model RLS without granting them any direct Lakehouse or SQL endpoint permissions.')
t('dl_sso_identity',
  'Enable single sign-on (SSO) on the Direct Lake semantic model connection',
  'With SSO enabled on a Direct Lake model, Fabric evaluates data permissions at the underlying SQL analytics endpoint or OneLake security layer using each viewing report consumer\'s own Microsoft Entra identity.')

# --- 1.3 Row-level, column-level, object-level, and file-level access control ---
t('onelake_sec_single_role',
  'Define both the RLS filter and CLS column allow-list inside a single OneLake security Grant role with Read permission',
  'OneLake security supports Grant roles only (Read permission required for RLS/CLS) and requires combining RLS and CLS on the same table within a single role — separate RLS and CLS roles on the same table return query errors.')
t('onelake_sec_folder',
  'Create a OneLake security role scoped to the specific Files/<subfolder> path with Read permission',
  'OneLake folder-level security grants inherited Read (or ReadWrite) access to the selected subfolder and its descendants while allowing parent traversal without exposing sibling folders or Tables.')
t('onelake_sec_readwrite_trap',
  'Create a OneLake security role with ReadWrite permission and attach an RLS predicate',
  'OneLake security roles granting ReadWrite permission cannot contain RLS or CLS constraints; fine-grained row and column rules are supported only on Read roles.')
t('sql_endpoint_user_id_mode',
  'Switch the Lakehouse SQL analytics endpoint to User\'s identity mode',
  'Setting the SQL analytics endpoint to User\'s identity mode evaluates OneLake security roles per caller across T-SQL and downstream shortcuts instead of running under the Lakehouse owner\'s fixed identity.')
t('sql_rls_tvf_policy',
  'Create an inline table-valued predicate function with SCHEMABINDING and a CREATE SECURITY POLICY FILTER PREDICATE in the Warehouse',
  'Fabric Warehouse and SQL analytics endpoints enforce native SQL RLS via an inline TVF (for example checking USER_NAME() or SUSER_SNAME()) bound with CREATE SECURITY POLICY ... ADD FILTER PREDICATE ... WITH (STATE = ON).')
t('sql_cls_grant_cols',
  'Grant T-SQL column-level SELECT on only the non-sensitive columns (GRANT SELECT ON dbo.Customer(CustomerID, Region) TO ...)',
  'In Fabric Warehouse and SQL analytics endpoints, column-level security restricts users to explicitly permitted columns via column-scoped GRANT SELECT without creating duplicate views or physical tables.')
t('sql_ddm_masked',
  'Apply T-SQL Dynamic Data Masking (MASKED WITH (FUNCTION = \'partial(...)\')) on sensitive columns',
  'Dynamic Data Masking obfuscates sensitive strings/emails/numbers in query results for users lacking UNMASK permission while keeping the column present so SELECT * queries do not fail.')
t('sql_ols_deny',
  'Use T-SQL GRANT/DENY SELECT on specific Warehouse schemas, tables, or views',
  'Object-level security in Fabric Warehouse or SQL analytics endpoints controls visibility and query access to entire tables, views, or stored procedures using standard T-SQL GRANT and DENY permissions.')
t('sm_dax_dynamic_rls',
  'Create a dynamic DAX RLS role filtering a security mapping table with [UserEmail] = USERPRINCIPALNAME()',
  'Dynamic DAX RLS filters rows at query time based on USERPRINCIPALNAME() (always returning the Entra UPN email, unlike USERNAME() which can return DOMAIN\\user locally) and only restricts Workspace Viewers or App/shared consumers.')
t('sm_ols_tabular_editor',
  'Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL',
  'Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility.')
t('sm_view_as_test',
  'Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user\'s UPN',
  'Testing RLS/OLS with Test as role combined with a specific Viewer user\'s Entra UPN verifies both the DAX role predicate and the user\'s actual workspace/item permission level (catching the Contributor RLS-bypass trap).')

# --- 1.4 Sensitivity labels ---
t('purview_label_inherit',
  'Apply a Microsoft Purview sensitivity label with downstream inheritance on the source Lakehouse or Warehouse',
  'Sensitivity labels applied to Fabric Lakehouses, Warehouses, and Semantic Models automatically propagate downstream to newly connected semantic models, reports, and exported Excel/PDF/PPTX files when inheritance is enabled.')
t('purview_mandatory_policy',
  'Enable a mandatory label policy and default sensitivity label in Microsoft Purview compliance portal for Fabric users',
  'Mandatory and default sensitivity label policies in Microsoft Purview require content creators to classify unlabeled semantic models and reports on save and apply baseline classification automatically.')
t('purview_file_encryption',
  'Use a Purview sensitivity label configured with file encryption so exported .pbix, Excel, PDF, and PowerPoint files stay protected outside Fabric',
  'While sensitivity labels in Fabric classify items in the workspace without encrypting OneLake Delta storage itself, encryption-enabled labels enforce rights management automatically when users export data to Excel, PDF, PowerPoint, or .pbix.')

# --- 1.5 Endorse items ---
t('endorse_promoted',
  'Mark the item as Promoted in item settings',
  'Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review.')
t('endorse_certified',
  'Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal',
  'Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards.')
t('endorse_master_data',
  'Configure Certified endorsement with the Master data label on authoritative core tables or semantic models',
  'Fabric admins can enable Master data endorsement for authoritative single-source-of-truth silver/gold data assets so analysts distinguish core reference items in the OneLake catalog.')

# --- 1.6 Workspace Git version control ---
t('git_ws_branch_out',
  'Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch',
  'In Fabric Git integration, workspaces map 1-to-1 to branches; branching out into a dedicated developer workspace isolates in-progress notebook, pipeline, and semantic model edits before merging via pull request.')
t('git_commit_vs_update',
  'Commit workspace changes to Git from the Source control pane, merge via pull request, then select Update all in the target workspace',
  'Fabric Git sync is explicit rather than automatic on remote push: developers Commit workspace edits to their branch, complete a PR in Azure DevOps or GitHub, and run Update from Git in the downstream workspace.')
t('git_undo_uncommitted',
  'Use Undo in the Fabric Workspace Source control pane to discard uncommitted workspace edits back to the last synced commit',
  'Undo reverts uncommitted workspace item modifications to match the connected Git branch HEAD without rewriting shared remote commit history.')

# --- 1.7 Power BI Desktop projects (.pbip) ---
t('pbip_tmdl_pbir',
  'Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions',
  'A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs.')
t('pbip_gitignore_cache',
  'Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository',
  'cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore.')

# --- 1.8 Deployment pipelines ---
t('dp_rules_rebind',
  'Configure Deployment pipeline data source and parameter rules on the Test and Production stages',
  'Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings.')
t('dp_var_library',
  'Use a Fabric Variable library (or autobinding across paired workspace items) to parameterize stage-specific environment references',
  'Fabric Variable libraries store stage-specific workspace/lakehouse IDs, URLs, and thresholds across Dev/Test/Prod — essential for items like Data Pipelines and Direct Lake on OneLake models that do not use legacy SQL deployment rules.')
t('dp_selective_deploy',
  'Perform a selective deployment selecting the modified item together with Select related to include required upstream dependencies',
  'Selective deployment in Fabric Deployment Pipelines promotes only chosen items between stages, and Select related ensures newly referenced lakehouses or semantic models deploy alongside dependent reports.')
t('dp_backward_deploy',
  'Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline',
  'When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage.')

# --- 1.9 Impact analysis of downstream dependencies ---
t('lineage_impact_view',
  'Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts',
  'Fabric\'s Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners.')

# --- 1.10 XMLA endpoint ---
t('xmla_readwrite_cap',
  'Enable XMLA Endpoint = Read Write in Fabric Capacity workload settings and connect to powerbi://api.powerbi.com/v1.0/myorg/<WorkspaceName>',
  'External ALM tools (Tabular Editor, SSMS, ALM Toolkit, SqlPackage/PowerShell Invoke-ASCmd) require workspace Fabric/Premium capacity with XMLA Endpoint set to Read Write to deploy or modify semantic models.')
t('xmla_tmsl_refresh',
  'Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition',
  'Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads.')
t('xmla_alm_toolkit',
  'Use ALM Toolkit over the XMLA endpoint to compare Dev and Prod semantic models and deploy only new measures without reprocessing unchanged partitions',
  'ALM Toolkit performs metadata-only diffs and incremental TMSL deployments over XMLA, preserving existing processed historical partitions and incremental refresh windows in Production.')

# --- 1.11 Reusable assets (.pbit, .pbids, shared semantic models) ---
t('pbit_template',
  'Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows',
  'A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open.')
t('pbids_datasource',
  'Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode',
  'A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector.')
t('thin_live_report',
  'Publish a single certified core semantic model in a data workspace and build thin live-connected Power BI reports in departmental workspaces',
  'Decoupling a shared golden semantic model from thin live-connected reports prevents measure duplication, reduces capacity memory footprint, and enforces centralized RLS/endorsement across teams.')


# ============================================================================
# DOMAIN 2 — Prepare data (Skills 2.1 – 2.18)
# ============================================================================

# --- 2.1 Create a data connection ---
t('conn_shareable_cloud',
  'Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication',
  'Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets.')
t('conn_vnet_gateway',
  'Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet',
  'A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs.')
t('conn_onprem_gateway',
  'Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network',
  'An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports.')

# --- 2.2 Discover data with OneLake catalog & Real-Time hub ---
t('onelake_catalog_govern',
  'Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture',
  'OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations.')
t('realtime_hub_events',
  'Use the Real-Time hub to subscribe to Microsoft.Fabric.OneLake.FileCreated events (or Capacity/CDC streams) and trigger an Activator rule',
  'Real-Time hub unifies streaming sources, CDC feeds, Azure Blob events, and Fabric workspace/OneLake/Capacity events so analytics engineers can discover streams in one catalog and trigger event-driven pipelines or Notebooks via Activator.')

# --- 2.3 Ingest or access data as needed ---
t('onelake_shortcut_ext',
  'Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching',
  'OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs.')
t('fabric_mirroring_cdc',
  'Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog',
  'Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness.')
t('df_copy_activity',
  'Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake',
  'Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead.')
t('dataflow_gen2_fastcopy',
  'Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations',
  'Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations.')
t('eventstream_ingest',
  'Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table',
  'Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse.')

# --- 2.4 Choose between different data stores ---
t('store_lakehouse',
  'Choose a Fabric Lakehouse',
  'Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint.')
t('store_warehouse',
  'Choose a Fabric Data Warehouse',
  'Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake.')
t('store_eventhouse',
  'Choose a Fabric Eventhouse (KQL database)',
  'Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events.')
t('store_sqldb_fabric',
  'Choose a SQL database in Microsoft Fabric',
  'SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics.')

# --- 2.5 OneLake integration for Eventhouse and semantic models ---
t('eventhouse_onelake_avail',
  'Enable OneLake availability on the Eventhouse KQL database (or specific KQL table) and create an internal OneLake shortcut in the Lakehouse',
  'KQL databases do not write Delta Parquet to OneLake by default; turning on OneLake availability creates a synced Delta Parquet logical representation in OneLake that Spark, SQL analytics endpoints, and Direct Lake on OneLake models can read without data movement.')
t('sm_onelake_integration',
  'Enable OneLake integration in the Import semantic model settings so imported model tables export as Delta tables to OneLake',
  'OneLake integration for Import semantic models writes Delta Parquet artifacts of the model\'s imported tables into OneLake, allowing Lakehouse shortcuts and Spark/SQL users to reuse curated Power Query model outputs.')

# --- 2.6 Create views, functions, and stored procedures ---
t('wh_stored_proc_elt',
  'Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic',
  'Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines.')
t('lh_materialized_view',
  'Use a Lakehouse Materialized Lake View (or persisted Gold Delta table) instead of a non-materialized SQL analytics endpoint view for Direct Lake on OneLake',
  'Non-materialized SQL analytics endpoint views cannot back Direct Lake on OneLake tables and force Direct Lake on SQL into DirectQuery fallback; materializing the view as a Delta table preserves pure in-memory Direct Lake speed.')

# --- 2.7 Enrich data by adding new columns or tables ---
t('enrich_surrogate_key',
  'Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions',
  'Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq.')
t('enrich_date_dim',
  'Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes',
  'A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering.')
t('enrich_pyspark_withcol',
  'Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs',
  'Native Catalyst/Photon-optimized pyspark.sql.functions execute in vectorized JVM/native code across partitions, avoiding the severe Python serialization bottleneck of row-level UDFs.')

# --- 2.8 Implement a star schema for a lakehouse or warehouse ---
t('star_scd_type2',
  'Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns',
  'SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records.')
t('star_scd_type1',
  'Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place',
  'SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes.')
t('star_fact_grain',
  'Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures',
  'Keeping fact tables at a single, consistent atomic grain with integer foreign keys and additive measures eliminates double-counting and supports flexible rollups across every conformed dimension.')
t('star_medallion',
  'Organize OneLake into Bronze (raw immutable), Silver (validated, deduplicated, conformed), and Gold (star-schema dimensions and facts with V-Order)',
  'The Medallion architecture separates raw source fidelity (Bronze), enterprise data quality/conformance (Silver), and BI/Direct Lake star-schema consumption (Gold).')

# --- 2.9 Denormalize data ---
t('denorm_snowflake_dim',
  'Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension',
  'Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models.')

# --- 2.10 Aggregate data ---
t('agg_gold_summary',
  'Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)',
  'Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency.')

# --- 2.11 Merge or join data ---
t('merge_delta_upsert',
  'Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement',
  'Delta Lake MERGE INTO (in Spark SQL, PySpark DeltaTable.forPath().merge(), or Warehouse T-SQL) atomically applies incremental CDC inserts, updates, and soft-deletes in a single ACID transaction.')
t('join_left_anti',
  'Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table',
  'A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys.')
t('join_broadcast_spark',
  'Apply broadcast(dim_df) in PySpark when joining a multi-hundred-million-row fact DataFrame with a small dimension DataFrame',
  'Broadcasting a small dimension table (<10–100 MB) to every executor avoids an expensive cluster-wide shuffle sort-merge join of the massive fact DataFrame.')

# --- 2.12 Duplicate, missing, or null values ---
t('dedup_rownum_window',
  'Deduplicate using ROW_NUMBER() OVER (PARTITION BY BusinessKey ORDER BY ModifiedTimestamp DESC) = 1',
  'Windowing by BusinessKey ordered descending by ingestion or source-change timestamp deterministically retains only the latest version of duplicate CDC events while preserving all non-key columns.')
t('null_unknown_member',
  'Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE',
  'Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity.')
t('data_wrangler_profile',
  'Launch Data Wrangler from a Fabric Spark notebook (or enable Power Query Column profiling based on entire data set) to inspect nulls, duplicates, and distributions and export generated PySpark code',
  'Power Query profiles only the top 1,000 rows by default unless switched to entire dataset, whereas Data Wrangler interactively profiles Pandas/Spark DataFrames and emits reproducible Python/PySpark cleaning code.')

# --- 2.13 Convert column data types ---
t('type_try_cast',
  'Convert dirty string columns using TRY_CAST / TRY_CONVERT in T-SQL (or Spark try_cast) so malformed rows evaluate to NULL for quarantine instead of aborting the batch',
  'Standard CAST throws a fatal conversion error on the first malformed token; TRY_CAST safely yields NULL so pipelines can quarantine invalid records without failing the entire load.')
t('type_dl_compat',
  'Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake',
  'Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures.')

# --- 2.14 Filter data ---
t('filter_query_folding',
  'Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled',
  'Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container.')
t('filter_partition_prune',
  'Filter on physical Delta partition or liquid-clustered date columns using sargable range predicates (OrderDate >= \'2026-01-01\') without wrapping the column in functions',
  'Wrapping a column in YEAR(OrderDate) = 2026 blocks file-level min/max data skipping and partition pruning; sargable range predicates let Spark and SQL endpoints skip irrelevant Parquet files entirely.')

# --- 2.15 Visual query editor ---
t('visual_query_editor',
  'Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view',
  'The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data.')

# --- 2.16 Query and analyze with SQL ---
t('sql_window_lag_running',
  'Write T-SQL window functions using LAG(...) OVER (PARTITION BY ... ORDER BY ...) and SUM(...) OVER (... ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)',
  'T-SQL analytic window functions compute period-over-period deltas and running totals in a single pass without self-joins or collapsing detail rows.')
t('sql_wh_time_travel',
  'Query historical Warehouse state using SELECT ... FROM dbo.FactSales OPTION (FOR TIMESTAMP AS OF \'2026-10-15T00:00:00\') or CREATE TABLE ... AS CLONE OF',
  'Fabric Warehouse supports T-SQL Time Travel (up to the 30-day retention window) via OPTION (FOR TIMESTAMP AS OF ...) and zero-copy table clones via CREATE TABLE ... AS CLONE OF ... AT.')
t('sql_cross_db_three_part',
  'Query across a Warehouse and a Lakehouse SQL analytics endpoint in the same workspace using three-part T-SQL naming (SalesLakehouse.dbo.RawOrders)',
  'Fabric Warehouse and SQL analytics endpoints inside the same workspace share a unified SQL engine namespace, enabling zero-copy cross-database T-SQL joins via DatabaseName.SchemaName.ObjectName.')

# --- 2.17 Query and analyze with KQL ---
t('kql_summarize_bin_argmax',
  'Write a KQL query using | where Timestamp > ago(24h) | summarize arg_max(IngestionTime, *) by DeviceId and | summarize AvgTemp = avg(Temp), P95 = percentile(Temp, 95) by bin(Timestamp, 5m)',
  'In Eventhouse KQL, arg_max() retrieves the full latest row per entity key efficiently, and summarize ... by bin(Timestamp, 5m) buckets irregular streaming timestamps into fixed time windows.')
t('kql_parse_json_mvexpand',
  'Use KQL parse_json() (or dynamic column indexing) followed by | mv-expand SensorReadings to flatten nested JSON arrays before aggregating',
  'Eventhouse stores semi-structured JSON natively in dynamic columns; mv-expand expands multi-element JSON arrays into individual rows for downstream filtering and summarization.')

# --- 2.18 Query and analyze with DAX ---
t('dax_query_view_eval',
  'Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results',
  'DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated.')
t('dax_info_view_funcs',
  'Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View',
  'DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections.')


# ============================================================================
# DOMAIN 3 — Implement and manage semantic models (Skills 3.1 – 3.12)
# ============================================================================

# --- 3.1 Choose a storage mode ---
t('mode_import',
  'Configure Import storage mode',
  'Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary.')
t('mode_directquery',
  'Configure DirectQuery storage mode',
  'DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake.')
t('mode_direct_lake',
  'Configure Direct Lake storage mode',
  'Direct Lake loads Delta Parquet columns directly from OneLake into VertiPaq memory on demand without scheduled Import data duplication or slow per-visual SQL translation.')
t('mode_dual_dim',
  'Configure shared dimension tables in Dual storage mode inside a composite model',
  'Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins.')

# --- 3.2 Implement a star schema for a semantic model ---
t('sm_mark_date_table',
  'Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column',
  'Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence.')
t('sm_hide_keys_sortby',
  'Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear',
  'Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering.')

# --- 3.3 Relationships, bridge tables, and many-to-many ---
t('rel_userelationship',
  'Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()',
  'Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times.')
t('rel_bridge_crossfilter',
  'Introduce a deduplicated Bridge table between the two dimensions and scope bidirectional propagation strictly inside specific measures using CROSSFILTER(..., BOTH)',
  'Scoping CROSSFILTER(..., BOTH) inside a DAX measure over a bridge table satisfies many-to-many attribution without turning on permanent model-wide bidirectional relationships that cause ambiguity and performance degradation.')
t('rel_assume_ref_integrity',
  'Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid',
  'Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table.')

# --- 3.4 DAX variables, iterators, table filtering, windowing, information functions ---
t('dax_var_single_eval',
  'Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches',
  'DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability.')
t('dax_sumx_iterator',
  'Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table',
  'Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns.')
t('dax_keepfilters_col',
  'Pass simple column predicates wrapped in KEEPFILTERS(DimProduct[Color] = "Red") to CALCULATE instead of FILTER(ALL(FactSales), ...)',
  'KEEPFILTERS intersects the predicate with existing report slicer selections rather than overwriting them, and filtering a dimension column avoids scanning the entire multi-million-row fact table in the Formula Engine.')
t('dax_window_offset',
  'Use DAX window functions OFFSET(-1, ALLSELECTED(DimDate[YearMonth]), ORDERBY(DimDate[YearMonthNum], ASC)) or WINDOW() with PARTITIONBY()',
  'DAX windowing functions (OFFSET, INDEX, WINDOW) navigate sorted/partitioned visual axes directly even for custom fiscal calendars where standard DATEADD/SAMEPERIODLASTYEAR functions fail.')
t('dax_isinscope',
  'Use ISINSCOPE(DimProduct[Subcategory]) (or SELECTEDVALUE with an alternate result) to branch measure behavior cleanly across matrix hierarchy levels',
  'ISINSCOPE returns TRUE only when the specified column is actively grouping the current visual row/column level, making it superior to HASONEVALUE for subtotal vs leaf detection in matrices.')

# --- 3.5 Calculation groups, dynamic format strings, and field parameters ---
t('sm_calc_group',
  'Create a Calculation Group with Calculation Items referencing SELECTEDMEASURE() and explicit Precedence ordering (automatically setting DiscourageImplicitMeasures = true)',
  'A single Calculation Group applies reusable logic (YTD, PY, YoY%, Moving Avg) across dozens of base measures via SELECTEDMEASURE(), eliminating measure explosion (`50 base * 6 time calcs = 300 measures`).')
t('sm_dyn_format_str',
  'Configure a Dynamic Format String expression on the measure or calculation item (for example returning "\\$#,0.00" vs "0.0%" via SELECTEDMEASUREFORMATSTRING()) without wrapping values in FORMAT()',
  'Unlike FORMAT() — which converts numbers into text strings and breaks chart axes/sorting/aggregations — Dynamic Format Strings preserve true numeric data types while rendering context-aware currency or percentage formatting.')
t('sm_field_parameter',
  'Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer',
  'Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals.')

# --- 3.6 Large semantic model storage format ---
t('sm_large_format',
  'Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)',
  'Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance.')

# --- 3.7 Design and build composite models ---
t('sm_composite_dl_import',
  'Build a Direct Lake on OneLake composite semantic model combining Direct Lake fact tables from OneLake with Import dimension/target tables using regular relationships',
  'Direct Lake on OneLake supports true composite models that mix Direct Lake tables from multiple Fabric items with Import tables from any Power Query connector while preserving fast regular (non-limited) relationships.')
t('sm_composite_agg_table',
  'Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table',
  'User-defined Import aggregations satisfy high-level grouped queries purely from in-memory VertiPaq cache and automatically route only unaggregated detail drill-throughs to the underlying DirectQuery source.')
t('sm_dq_over_pbi_local',
  'Create a local composite model using DirectQuery for Power BI semantic models and Analysis Services to combine a certified core semantic model with a departmental Excel/SQL table',
  'Connecting to an existing shared semantic model in DirectQuery mode creates a local composite model (using remote model chains and limited cross-island relationships) so analysts can extend governed enterprise measures without copying the core model.')

# --- 3.8 Performance improvements in queries and report visuals ---
t('opt_perf_analyzer',
  'Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time',
  'When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters.')
t('opt_query_reduction',
  'Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages',
  'Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering.')

# --- 3.9 Improve DAX performance ---
t('opt_dax_studio_fese',
  'Profile the slow measure in DAX Studio using Server Timings to inspect Formula Engine (FE) vs Storage Engine (SE) CPU, SE query count, and CallbackDataID warnings',
  'DAX Studio Server Timings reveals whether slow execution comes from hundreds of chatty SE scans, CallbackDataID forcing row-by-row FE callbacks inside SE scans, or unpushed complex predicates.')
t('opt_vertipaq_cardinality',
  'Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time',
  'Columnar memory in VertiPaq and Direct Lake transcoding scales primarily with column cardinality rather than row count; dropping unused GUIDs or splitting millisecond timestamps into separate Date and Time columns cuts memory dramatically.')

# --- 3.10 Configure Direct Lake (fallback & refresh / framing) ---
t('dl_framing_refresh',
  'Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes',
  'Framing is a fast metadata-only operation updating the Direct Lake model\'s pointer to the latest Delta transaction log Parquet files and evicting stale resident columns so new ETL rows become visible consistently.')
t('dl_vorder_optimize',
  'Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails',
  'Hundreds of tiny streaming Parquet files inflate Delta rowgroup counts past Fabric SKU guardrails and degrade transcoding; OPTIMIZE compacts files into large V-Order-sorted rowgroups optimized for VertiPaq in-memory compression.')
t('dl_behavior_only',
  'Set DirectLakeBehavior = DirectLakeOnly on a Direct Lake on SQL semantic model so queries fail fast instead of silently falling back to slow DirectQuery',
  'Setting DirectLakeBehavior to DirectLakeOnly (on Direct Lake on SQL models) prevents unexpected DirectQuery fallback spikes on the SQL endpoint when guardrails or SQL views/RLS are encountered.')

# --- 3.11 Choose between Direct Lake on OneLake vs Direct Lake on SQL ---
t('dl_choose_onelake',
  'Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop)',
  'Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery.')
t('dl_choose_sql_endpoint',
  'Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)',
  'Direct Lake on SQL binds to a single Fabric item\'s SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules.')
t('dl_migrate_tmdl_onelake',
  'Migrate the model in Power BI Desktop TMDL view by replacing Sql.Database(...) in the shared Expression with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<itemId>")',
  'Replacing the shared M expression from Sql.Database to the OneLake ABFS/HTTPS AzureStorage.DataLake URL in TMDL view upgrades an existing Direct Lake on SQL model to Direct Lake on OneLake.')

# --- 3.12 Implement incremental refresh for semantic models ---
t('inc_refresh_params',
  'Create exact case-sensitive DateTime parameters RangeStart and RangeEnd, filter Date >= RangeStart and Date < RangeEnd (half-open interval) with query folding intact, and enable Incremental refresh',
  'Incremental refresh requires exact DateTime-typed RangeStart and RangeEnd parameters and a half-open filter (>= RangeStart and < RangeEnd, never <= on both ends which duplicates boundary midnight rows) on a foldable query.')
t('inc_refresh_detect_rt',
  'Enable Detect data changes on an immutable LastModifiedUTC audit column (different from the partitioned OrderDate column) and optionally enable Get the latest data in real time with DirectQuery',
  'Detect data changes refreshes only historical archive partitions whose MAX(LastModifiedUTC) changed, while the hybrid real-time option adds a trailing DirectQuery partition for today\'s intra-day rows.')


# ============================================================================
# SHARED HIGH-DISCRIMINATION DISTRACTORS (Incorrect / Anti-Pattern Choices)
# ============================================================================
t('anti_ws_contributor_rls',
  'Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows',
  'Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows.')
t('anti_username_dax',
  'Filter the RLS table using USERNAME() = [DomainLogin] without testing in the Fabric portal',
  'In Power BI Desktop USERNAME() returns DOMAIN\\user whereas in the Fabric service it returns the UPN; USERPRINCIPALNAME() consistently returns user@domain.com across cloud evaluations.')
t('anti_display_hidden_sec',
  'Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS',
  'Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns.')
t('anti_onelake_two_roles',
  'Create two separate OneLake security roles on the same table — Role A containing the RLS filter and Role B containing the CLS column rule — and assign the user to both',
  'OneLake security does not support combining an RLS role and a CLS role across separate roles on the same table; members assigned to that combination receive query errors.')
t('anti_onelake_deny_role',
  'Create a Deny role in OneLake security to revoke table access granted by another OneLake role or Workspace Member role',
  'OneLake security supports Grant roles only — there is no Deny role type, and OneLake security never restricts Workspace Admins, Members, or Contributors.')
t('anti_pbix_binary_git',
  'Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches',
  'Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs.')
t('anti_dl_gateway',
  'Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes',
  'Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway.')
t('anti_lh_sql_dml_write',
  'Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint',
  'A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables).')
t('anti_eventhouse_default_dl',
  'Point Direct Lake on SQL directly at an Eventhouse KQL database without enabling OneLake availability',
  'Eventhouse KQL databases do not write Delta Parquet to OneLake unless OneLake availability is enabled, and Direct Lake on SQL does not support KQL databases (only Direct Lake on OneLake does once OneLake availability is on).')
t('anti_auto_datetime_on',
  'Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension',
  'Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently.')
t('anti_bidir_all_rels',
  'Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other',
  'Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns.')
t('anti_format_func_measure',
  'Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically',
  'FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals.')
t('anti_filter_all_fact',
  'Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows',
  'Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine.')
t('anti_calc_col_fact_ratio',
  'Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals',
  'Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]).')
t('anti_inc_both_inclusive',
  'Filter Incremental Refresh with OrderDate >= RangeStart AND OrderDate <= RangeEnd using inclusive operators on both boundaries',
  'Using >= AND <= on both ends causes rows stamped exactly at midnight on partition boundaries to load into two adjacent partitions, silently double-counting sales totals.')
t('anti_dl_onelake_dq_fallback',
  'Expect Direct Lake on OneLake to automatically fall back to DirectQuery against the SQL analytics endpoint when capacity memory guardrails are exceeded',
  'Direct Lake on OneLake operates exclusively in DirectLakeOnly mode and never falls back to DirectQuery; exceeding capacity guardrails fails framing/queries until Delta tables or SKU sizing are optimized.')
t('anti_pq_1000_row_profile',
  'Rely on Power Query\'s default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table',
  'By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions.')
t('anti_python_udf_loop',
  'Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations',
  'df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions.')
t('anti_non_sargable_where',
  'Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE \'2026-%\'',
  'Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding.')
t('anti_copy_full_reload',
  'Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging',
  'Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring.')


# ============================================================================
# DEDICATED SYNTAX TOKENS FOR ____ CODE / QUERY / TMDL / TMSL COMPLETIONS
# ============================================================================

# --- SQL / Warehouse / Delta Lake tokens ---
t('tok_filter_predicate',
  'ADD FILTER PREDICATE Security.fn_regionpredicate(RegionCode) ON dbo.FactSales WITH (STATE = ON)',
  'CREATE SECURITY POLICY ... ADD FILTER PREDICATE binds an inline table-valued security predicate function to a Warehouse or SQL analytics endpoint table to filter SELECT rows transparently.')
t('tok_block_predicate_bad',
  'ADD BLOCK PREDICATE dbo.sp_checkregion(RegionCode) AFTER INSERT',
  'Fabric Data Warehouse supports FILTER PREDICATE with inline TVFs (not stored procedures or SQL Server DML BLOCK PREDICATE triggers).')
t('tok_masked_partial',
  'MASKED WITH (FUNCTION = \'partial(0,"XXX-XX-",4)\')',
  'The T-SQL Dynamic Data Masking partial(prefix, padding, suffix) function exposes only the last four characters while masking leading digits for callers without UNMASK permission.')
t('tok_for_timestamp_as_of',
  'OPTION (FOR TIMESTAMP AS OF \'2026-10-28T06:00:00.000\')',
  'Fabric Data Warehouse Time Travel uses the query hint OPTION (FOR TIMESTAMP AS OF \'YYYY-MM-DDTHH:MM:SS.fff\') to read exact point-in-time historical snapshots within the retention window.')
t('tok_system_time_bad',
  'FOR SYSTEM_TIME AS OF \'2026-10-28T06:00:00.000\'',
  'FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...).')
t('tok_clone_table_at',
  'CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales',
  'CREATE TABLE ... AS CLONE OF creates a zero-copy metadata clone of a Fabric Warehouse table instantaneously (optionally AT a specific UTC timestamp) without duplicating Parquet files.')
t('tok_grouping_sets',
  'GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())',
  'GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes.')
t('tok_try_cast_dec',
  'TRY_CAST(RawReading AS DECIMAL(18, 4))',
  'TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT.')
t('tok_cast_float_bad',
  'CAST(RawReading AS FLOAT)',
  'Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement.')
t('tok_rownum_dedup',
  'ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)',
  'ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key.')
t('tok_rank_ties_bad',
  'RANK() OVER (ORDER BY SpecimenId DESC)',
  'Omitting PARTITION BY ranks across the entire table globally rather than per entity, and RANK() returns duplicate rank-1 rows on exact timestamp ties.')
t('tok_lag_window',
  'LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)',
  'LAG(col, 1, 0) retrieves the immediately preceding hour\'s value within each SubstationId partition, defaulting the first row to 0.')
t('tok_merge_when_matched',
  'WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET',
  'Guarding WHEN MATCHED with a hash/attribute inequality prevents rewriting unchanged Delta Parquet files on untouched rows during incremental upserts.')
t('tok_delta_optimize_vorder',
  'OPTIMIZE gold.fact_orders VORDER',
  'Running OPTIMIZE ... VORDER bin-packs small Delta Parquet files into large rowgroups and applies V-Order columnar sorting for peak Direct Lake compression and transcoding.')

# --- KQL (Eventhouse) tokens ---
t('tok_kql_arg_max',
  '| summarize arg_max(IngestionTime, *) by SpecimenId',
  'In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key.')
t('tok_kql_mv_expand',
  '| mv-expand PhaseReading = parse_json(Payload).PhaseReadings',
  'mv-expand unpacks a dynamic JSON array into one output row per array element while preserving parent event columns.')
t('tok_kql_make_series',
  '| make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion',
  'make-series builds regular gap-filled time-series arrays (filling empty 1-minute buckets with default = 0) required for KQL anomaly detection and trend functions; summarize by bin() omits empty buckets.')
t('tok_kql_bin_p99',
  '| summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)',
  'percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse.')

# --- DAX / Semantic Model / TMDL / TMSL tokens ---
t('tok_dax_upn',
  '[ManagerEmail] = USERPRINCIPALNAME()',
  'USERPRINCIPALNAME() returns the signed-in consumer\'s Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS.')
t('tok_dax_selectedmeasure',
  'CALCULATE(SELECTEDMEASURE(), DATESYTD(\'Calendar\'[Date]))',
  'Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual.')
t('tok_dax_dyn_fmt_token',
  'IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())',
  'Dynamic format string expressions return a format mask string while preserving the measure\'s underlying numeric type; SELECTEDMEASUREFORMATSTRING() preserves the base measure\'s native currency/decimal mask.')
t('tok_dax_nameof',
  'NAMEOF(\'DimTrade\'[CurrencyPair])',
  'Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers.')
t('tok_dax_userelationship',
  'CALCULATE([Total Notional], USERELATIONSHIP(\'Calendar\'[DateKey], \'FactTrades\'[SettlementDateKey]))',
  'USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation.')
t('tok_dax_crossfilter_both',
  'CALCULATE([Encounter Count], CROSSFILTER(\'FactEncounter\'[EncounterKey], \'BridgeEncounterDiag\'[EncounterKey], BOTH))',
  'CROSSFILTER(..., BOTH) enables bidirectional filter propagation across a bridge table only inside the specific measure rather than globally across the model.')
t('tok_dax_offset_window',
  'CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED(\'Calendar\'[FiscalPeriod], \'Calendar\'[FiscalPeriodSort]), ORDERBY(\'Calendar\'[FiscalPeriodSort], ASC)))',
  'OFFSET(-1, ..., ORDERBY(...)) shifts one period backward along a custom 4-4-5 fiscal sort column where standard Gregorian DATEADD fails.')
t('tok_dax_isinscope_token',
  'IF(ISINSCOPE(\'DimProduct\'[SKU]), [Unit Margin], BLANK())',
  'ISINSCOPE(\'DimProduct\'[SKU]) evaluates TRUE only when SKU is actively grouping the visual hierarchy level, suppressing misleading margin figures at subtotal rows.')
t('tok_dax_info_measures',
  'EVALUATE INFO.VIEW.MEASURES()',
  'INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags.')
t('tok_tmdl_onelake_expr',
  'AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/" & WorkspaceId & "/" & LakehouseId)',
  'Direct Lake on OneLake partitions bind to a shared M expression calling AzureStorage.DataLake against the https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<itemId> endpoint.')
t('tok_tmdl_directlake_only',
  'directLakeBehavior: directLakeOnly',
  'Setting directLakeBehavior: directLakeOnly in TMDL prevents a Direct Lake on SQL model from silently falling back to DirectQuery.')
t('tok_tmsl_refresh_dataonly',
  '{"refresh": {"type": "dataOnly", "objects": [{"database": "WealthModel", "table": "FactPositions", "partition": "2026M10"}]}}',
  'A TMSL refresh command with type = "dataOnly" scoped to a single partition reloads raw partition data over XMLA without rebuilding global relationships or calculated tables.')
t('tok_pq_half_open_m',
  'Table.SelectRows(Source, each [OrderDate] >= RangeStart and [OrderDate] < RangeEnd)',
  'Power Query M incremental refresh requires exact case-sensitive RangeStart and RangeEnd parameters using >= RangeStart and < RangeEnd so boundary timestamps are never loaded twice.')
t('tok_pyspark_broadcast',
  'fact_df.join(F.broadcast(dim_store_df), on="StoreKey", how="left")',
  'Wrapping the small dimension DataFrame in pyspark.sql.functions.broadcast() avoids shuffling the multi-hundred-million-row fact DataFrame across Spark executors.')

