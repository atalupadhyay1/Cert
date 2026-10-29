"""Ordered 4-step (`→`) action sequence options for Exam DP-600 ordering items.

Every key in `SEQUENCES` has exactly three `→` separators (four ordered steps, <= 270 chars)
and is automatically registered in `TERMS` so ordering items (`kind == 'O'`) carry full
per-option explanations just like standard single-choice items.
"""
from terms import t

SEQUENCES = {}


def s(key: str, label: str, explanation: str) -> None:
    if label.count('→') != 3:
        raise ValueError(f'{key}: expected 3 arrows (4 steps), got {label.count("→")}')
    if len(label) > 275:
        raise ValueError(f'{key}: sequence label length {len(label)} > 275')
    SEQUENCES[key] = (label, explanation)
    t(key, label, explanation)


# 1. OneLake security architecture across workspaces
s('seq_onelake_sec_ok',
  'Enable OneLake security and define Read Grant roles → Assign consumers Workspace Viewer and OneLake security roles → Set SQL analytics endpoint to User\'s identity mode → Expose downstream shortcuts in User\'s identity mode',
  'Correct order: enable OneLake security with Grant roles first, assign consumers to Viewer + security roles (never Contributor), set SQL analytics endpoints to User\'s identity mode, and expose shortcuts downstream.')
s('seq_onelake_sec_bad_contrib',
  'Assign consumers the Workspace Contributor role → Enable OneLake security with a Deny role → Keep SQL analytics endpoint in Owner fixed identity mode → Create downstream shortcuts',
  'Incorrect: Contributors bypass OneLake security completely, OneLake security has no Deny role type, and Owner fixed identity bypasses per-user role evaluation on SQL queries.')
s('seq_onelake_sec_bad_rw',
  'Create downstream shortcuts first → Assign consumers Workspace Member rights → Attach RLS predicates to a ReadWrite OneLake role → Enable SSO on an On-premises gateway',
  'Incorrect: Members bypass OneLake security, ReadWrite roles cannot contain RLS/CLS rules, and OneLake shortcuts do not use On-premises gateways.')
s('seq_onelake_sec_bad_order',
  'Set SQL analytics endpoint to Delegated mode with SQL DENY rules → Remove Workspace Viewer assignments → Enable OneLake security afterward → Export binary .pbix copies',
  'Incorrect: mixing pre-existing SQL granular access with Delegated mode forces 100% DirectQuery fallback instead of clean OneLake security evaluation.')

# 2. Workspace Git feature-branch lifecycle (.pbip + PR + Deployment Pipeline)
s('seq_git_alm_ok',
  'Connect shared Dev workspace to main → Branch out to an isolated developer workspace and commit .pbip/Notebook edits → Merge pull request into main in Git → Run Update all in Dev and promote via Deployment Pipeline',
  'Correct order: link Dev to main, branch out to an isolated workspace for feature work, validate and merge via Git PR into main, run Update all in Dev, and promote via Deployment Pipeline with stage rules.')
s('seq_git_alm_bad_direct_prod',
  'Connect Production directly to a feature branch → Edit semantic models live in Prod → Force-push binary .pbix files including cache.abf to main → Deploy backward to Development',
  'Incorrect: editing Production directly on feature branches and committing cache.abf violates ALM isolation, leaks cached data, and bypasses Test validation.')
s('seq_git_alm_bad_skip_update',
  'Edit items directly on main without branching → Merge an empty PR → Promote Dev to Test before running Update from Git → Configure Git integration last',
  'Incorrect: Fabric workspaces do not auto-pull remote PR merges — skipping Update from Git promotes stale pre-PR workspace state to Test.')
s('seq_git_alm_bad_undo',
  'Branch out to personal My Workspace → Run Undo to push changes to GitHub → Delete .platform metadata files → Copy visuals manually into Production',
  'Incorrect: My Workspace does not support full team Git ALM, Undo discards local changes rather than committing, and deleting .platform breaks item lineage.')

# 3. Eventhouse OneLake integration -> Lakehouse -> Direct Lake on OneLake
s('seq_eventhouse_dl_ok',
  'Ingest streaming telemetry into an Eventhouse KQL database → Enable OneLake availability on the KQL database or table → Create an internal OneLake shortcut in the Lakehouse → Add the table to a Direct Lake on OneLake semantic model',
  'Correct order: land streaming events in Eventhouse, opt in to OneLake availability so Delta Parquet files sync to OneLake, surface via Lakehouse shortcut (or connect directly), and model with Direct Lake on OneLake.')
s('seq_eventhouse_dl_bad_sql_dl',
  'Create a Direct Lake on SQL model directly over the KQL queryset → Disable OneLake availability → Configure an On-premises data gateway → Run T-SQL MERGE on the KQL database',
  'Incorrect: Direct Lake on SQL does not support KQL databases, disabling OneLake availability prevents Delta Parquet generation, and Direct Lake never uses gateways.')
s('seq_eventhouse_dl_bad_export',
  'Export KQL query results manually to CSV every hour → Email CSVs to analysts → Import into binary .pbix files → Publish to My Workspace',
  'Incorrect: manual hourly CSV exports add latency, operational toil, and duplicate storage instead of native Eventhouse OneLake availability.')
s('seq_eventhouse_dl_bad_shortcut_first',
  'Create an Amazon S3 external shortcut to the KQL URI before enabling OneLake availability → Set storage mode to Dual only → Enable Auto date/time → Run XMLA clearValues',
  'Incorrect: KQL tables are internal OneLake sources that only expose Delta Parquet folders after OneLake availability is enabled.')

# 4. SCD Type 2 Dimension load in Warehouse / Lakehouse Gold layer
s('seq_scd2_load_ok',
  'Stage and deduplicate incoming records by natural key → Compare tracked attributes against active (IsCurrent = 1) Gold rows → Expire changed active rows (EffectiveEndDate, IsCurrent = 0) → Insert new active versions with fresh surrogate keys',
  'Correct order: deduplicate staging first, detect attribute changes against current rows, close out prior active intervals without losing their surrogate keys, and insert new active versions.')
s('seq_scd2_load_bad_overwrite',
  'Truncate the Gold dimension table → Reassign fresh random surrogate keys to all historical rows → Join historical facts without updating foreign keys → Set IsCurrent = 1 on every version',
  'Incorrect: regenerating surrogate keys on truncate breaks every existing historical fact foreign key, and marking multiple rows IsCurrent = 1 duplicates fact joins.')
s('seq_scd2_load_bad_null_fk',
  'Insert raw duplicate staging rows directly into FactSales → Delete unmatched dimension keys → Leave EffectiveStartDate NULL → Enable Assume referential integrity on broken keys',
  'Incorrect: deleting unmatched keys and enabling Assume referential integrity omits orphan rows silently in INNER JOINs.')
s('seq_scd2_load_bad_reverse',
  'Insert new versions with IsCurrent = 0 first → Overwrite old EffectiveStartDate values in place → Remove the natural business key column → Deduplicate after publishing reports',
  'Incorrect: new versions must be active (IsCurrent = 1), EffectiveStartDate of historical intervals must remain immutable, and natural keys are required to match future CDC updates.')

# 5. Semantic Model Incremental Refresh setup & initial partition generation
s('seq_inc_refresh_ok',
  'Create case-sensitive DateTime parameters RangeStart and RangeEnd → Apply foldable half-open filter (>= RangeStart and < RangeEnd) → Configure table Incremental refresh policy → Publish to workspace and run initial refresh to generate partitions',
  'Correct order: define DateTime RangeStart/RangeEnd parameters, apply >= RangeStart and < RangeEnd preserving query folding, configure table incremental policy, and publish so Fabric generates historical and incremental partitions.')
s('seq_inc_refresh_bad_text_param',
  'Create Text parameters named StartDate and EndDate → Add a custom M step breaking query folding before filtering → Use >= and <= inclusive bounds on both sides → Refresh only in Power BI Desktop',
  'Incorrect: parameter names/types must be exact DateTime RangeStart and RangeEnd, breaking query folding pulls the entire table on every refresh, and <= on both bounds double-counts midnight rows.')
s('seq_inc_refresh_bad_publish_first',
  'Publish an unfiltered 2-billion-row Import PBIX locally first → Define RangeStart in DAX calculated tables afterward → Set storage mode to Direct Lake on OneLake → Enable VNet gateway on Direct Lake',
  'Incorrect: importing 2 billion rows locally crashes Desktop before partitioning exists, RangeStart belongs in Power Query M, and Incremental Refresh partitions apply to Import/Hybrid tables rather than Direct Lake.')
s('seq_inc_refresh_bad_same_col',
  'Filter OrderDate > RangeEnd → Configure Detect data changes on the exact same OrderDate partition column → Disable query folding → Run XMLA clearValues without processing',
  'Incorrect: Detect data changes requires an audit/update timestamp column distinct from the date column used to partition RangeStart/RangeEnd.')

# 6. Direct Lake on SQL -> Direct Lake on OneLake migration in Power BI Desktop TMDL view
s('seq_tmdl_migrate_dl_ok',
  'Live edit the model in Power BI Desktop and save a Version history point → Script the semantic model in TMDL view → Replace Sql.Database(...) with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...") → Apply TMDL and run framing refresh',
  'Correct order: take a version history checkpoint while live editing, script the model in TMDL view, swap the shared M expression from Sql.Database to AzureStorage.DataLake OneLake URL, apply changes, and frame.')
s('seq_tmdl_migrate_dl_bad_pbix',
  'Download the Direct Lake model as an offline Import .pbix → Convert all tables to Dual storage mode → Replace AzureStorage.DataLake with OleDb.DataSource → Re-upload to My Workspace',
  'Incorrect: Direct Lake models are live-edited in workspaces (not offline Personal Workspace Import files), and OleDb breaks OneLake Direct Lake connectivity.')
s('seq_tmdl_migrate_dl_bad_views',
  'Keep non-materialized SQL analytics endpoint views as the only sources → Switch TMDL expression to AzureStorage.DataLake without materializing Delta tables → Enable DirectQuery fallback on Direct Lake on OneLake → Bind an On-premises gateway',
  'Incorrect: Direct Lake on OneLake does not support non-materialized SQL views, DirectQuery fallback, or gateways.')
s('seq_tmdl_migrate_dl_bad_drop',
  'Delete the semantic model in Production breaking report GUID bindings → Recreate measures manually from screenshots → Share Lakehouse Admin rights with all report viewers → Disable V-Order',
  'Incorrect: deleting the semantic model breaks downstream thin reports and lineage, and granting Workspace Admin violates security.')

# 7. Diagnosing & fixing DAX + Direct Lake performance bottlenecks
s('seq_perf_diag_ok',
  'Capture visual timings in Performance Analyzer → Profile captured DAX in DAX Studio with Server Timings and Query Plan → Refactor FILTER(Fact,...) into VAR-cached SE column predicates and run V-Order OPTIMIZE → Re-test with Clear Cache',
  'Correct order: isolate visual vs DAX queue time in Performance Analyzer, profile FE/SE and Direct Lake fallback in DAX Studio Server Timings, fix DAX anti-patterns + Delta Parquet layout, and benchmark cold-cache results.')
s('seq_perf_diag_bad_sku_blind',
  'Immediately upgrade from F64 to F512 without profiling → Enable bidirectional cross-filtering on all relationships → Convert numeric measures to FORMAT() strings → Disable V-Order on Gold tables',
  'Incorrect: scaling capacity blindly wastes budget while bidirectional joins, FORMAT() strings, and disabled V-Order make FE and transcoding slower.')
s('seq_perf_diag_bad_warm_cache',
  'Test queries only against warm VertiPaq cache without Clear Cache → Add high-cardinality GUID calculated columns to FactSales → Force DirectQueryOnly behavior → Add 45 single-value card visuals to one page',
  'Incorrect: benchmarking warm cache hides real SE/transcoding cost, GUID columns bloat dictionaries, DirectQueryOnly slows visuals, and 45 cards create visual-queue contention.')
s('seq_perf_diag_bad_ols',
  'Hide slow measures in Display Folders → Turn on Auto date/time → Split one Gold dimension into 6 normalized snowflake tables → Remove calendar surrogate keys',
  'Incorrect: snowflaking and Auto date/time increase relationship hops and memory overhead rather than resolving FE/SE bottlenecks.')

# 8. XMLA Zero-Downtime Metadata Deployment with ALM Toolkit / Tabular Editor
s('seq_xmla_deploy_ok',
  'Verify XMLA Endpoint = Read Write on target capacity → Connect ALM Toolkit to Dev source and Prod XMLA target → Compare schemas while hiding unchanged partitions and keeping Prod data sources → Validate and deploy metadata-only TMSL changes',
  'Correct order: confirm Read Write XMLA capacity setting, compare Dev vs Prod models, preserve Prod partition state and data-source bindings, and push metadata-only measure/relationship diffs.')
s('seq_xmla_deploy_bad_overwrite',
  'Set XMLA Endpoint = Off → Overwrite Production with an empty unpartitioned .pbix file → Purge all 5 years of historical incremental partitions → Re-import 3 billion rows during peak business hours',
  'Incorrect: XMLA Off blocks external deployment, and overwriting Production with an unpartitioned file destroys incremental partitions and causes prolonged outage.')
s('seq_xmla_deploy_bad_readonly',
  'Leave XMLA Endpoint = Read Only → Execute T-SQL DELETE across Warehouse schemas → Grant all report viewers Capacity Admin rights → Skip downstream impact analysis',
  'Incorrect: Read Only XMLA rejects TMSL model deployments, and Capacity Admin rights violate least privilege.')
s('seq_xmla_deploy_bad_manual',
  'Open Production in DAX Studio → Edit measures manually in Production without committing to Git → Copy cache.abf into GitHub → Disable sensitivity labels',
  'Incorrect: DAX Studio is a query/profiling tool (not a model-deployment tool), and unversioned Production hotfixes cause immediate drift on next deployment.')
