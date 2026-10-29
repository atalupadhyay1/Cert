# Microsoft Exam DP-600: Implementing Analytics Solutions Using Microsoft Fabric — Full-Length Mock Exam 1

Exam DP-600 (Omnichannel Retail, Global Inventory Lakehouses, and Direct Lake Merchandising) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint & Credential Notice:** Aligned to the official **October 19, 2026** DP-600 study guide (`Microsoft Certified: Fabric Analytics Engineer Associate`). Associate-level certification with **no prerequisite exam required**, free online annual renewal on Microsoft Learn, split-screen `learn.microsoft.com` access during non-lab exam sections, and hands-on coverage across **SQL**, **KQL**, **DAX**, **PySpark**, **Power Query M**, **TMDL**, and **TMSL**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` SQL/KQL/DAX/PySpark/M/TMDL/TMSL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Microsoft Fabric case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area SQL/KQL/DAX/TMDL dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn Fabric and Power BI documentation — never recalled live items or copied Microsoft sample case studies.

## Questions

### 1. A retail data engineer needs to create and schedule Spark notebooks and Data Factory pipelines in the `Merchandising-Dev` workspace but must be prevented from sharing items externally, publishing workspace apps, or adding new workspace members. Which workspace role satisfies least privilege?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Member role
- B. Assign the Workspace Viewer role
- C. Assign the Workspace Admin role
- D. Assign the Workspace Contributor role

### 2. Proposed solution: You grant 85 seasonal buyers the Workspace Contributor role in `Apparel-Prod` and define a DAX RLS role on the semantic model so each buyer sees only their department. Does this enforce row restrictions, and what should you assign instead?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Viewer role
- B. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows
- C. Assign the Workspace Member role
- D. Assign the Workspace Contributor role

### 3. Two lead analytics leads must publish the organizational Power BI App, configure OneLake security roles on Lakehouses, and add new Contributors, without being allowed to delete the workspace or remove Workspace Admins. Which two practices should you implement? Select two.

Domain: Maintain a data analytics solution

- A. Assign the Workspace Viewer role
- B. Assign the Workspace Admin role
- C. Assign the Workspace Member role
- D. Assign permissions to Microsoft Entra security groups rather than individual users
- E. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows

### 4. Business analysts in a separate `Store-Analytics` workspace need to connect Power BI Desktop live to a certified `RetailCore` semantic model and use Analyze in Excel without editing the model or viewing underlying Lakehouse files. Which item permission is required?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Contributor role
- B. Share the Lakehouse with ReadAll (Read all Apache Spark data) permission
- C. Share the item with ReadData (Read all SQL endpoint data) permission
- D. Grant Build permission on the shared semantic model

### 5. External inventory auditors need `SELECT` access across all tables in a Lakehouse SQL analytics endpoint using SSMS, but security policy prohibits them from reading raw Parquet files via Spark or OneLake File Explorer. Which Lakehouse sharing option should you select?

Domain: Maintain a data analytics solution

- A. Share the Lakehouse with ReadAll (Read all Apache Spark data) permission
- B. Assign the Workspace Admin role
- C. Share the item with Read permission only (no ReadData or ReadAll)
- D. Share the item with ReadData (Read all SQL endpoint data) permission

### 6. You are rolling out centralized OneLake security on a primary `InventoryHub` Lakehouse accessed via shortcuts from three downstream domain workspaces. Which four-step sequence enforces per-user row and object policies end-to-end?

Domain: Maintain a data analytics solution

- A. Assign consumers the Workspace Contributor role → Enable OneLake security with a Deny role → Keep SQL analytics endpoint in Owner fixed identity mode → Create downstream shortcuts
- B. Create downstream shortcuts first → Assign consumers Workspace Member rights → Attach RLS predicates to a ReadWrite OneLake role → Enable SSO on an On-premises gateway
- C. Enable OneLake security and define Read Grant roles → Assign consumers Workspace Viewer and OneLake security roles → Set SQL analytics endpoint to User's identity mode → Expose downstream shortcuts in User's identity mode
- D. Set SQL analytics endpoint to Delegated mode with SQL DENY rules → Remove Workspace Viewer assignments → Enable OneLake security afterward → Export binary .pbix copies

### 7. A retail analytics team must (1) allow pricing data scientists to read only `Files/pricing_extracts/` in a Lakehouse without seeing sibling `Files/hr_payroll/` folders or `Tables`, and (2) completely hide the `SupplierRebate` column metadata from store analysts in the semantic model. Which two controls meet both requirements? Select two.

Domain: Maintain a data analytics solution

- A. Create a OneLake security role with ReadWrite permission and attach an RLS predicate
- B. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- C. Create a Deny role in OneLake security to revoke table access granted by another OneLake role or Workspace Member role
- D. Create a OneLake security role scoped to the specific Files/<subfolder> path with Read permission
- E. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL

### 8. After applying a `Confidential — Executive Merchandising` Microsoft Purview sensitivity label to `GoldRetailWarehouse`, new semantic models and reports created from that Warehouse must automatically carry the same classification. Which capability handles this?

Domain: Maintain a data analytics solution

- A. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- B. Apply a Microsoft Purview sensitivity label with downstream inheritance on the source Lakehouse or Warehouse
- C. Mark the item as Promoted in item settings
- D. Apply T-SQL Dynamic Data Masking (MASKED WITH (FUNCTION = 'partial(...)')) on sensitive columns

### 9. Store directors occasionally export matrix data from a labeled Power BI report to `.xlsx` spreadsheets on laptops. How do you ensure unauthorized external recipients cannot open those exported Excel files?

Domain: Maintain a data analytics solution

- A. Use a Purview sensitivity label configured with file encryption so exported .pbix, Excel, PDF, and PowerPoint files stay protected outside Fabric
- B. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- C. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal
- D. Share the item with Read permission only (no ReadData or ReadAll)

### 10. A retail enterprise governance board requires a badge on the official `EnterpriseSales` semantic model proving an admin-authorized data steward reviewed its DAX definitions and security rules. Which endorsement state applies?

Domain: Maintain a data analytics solution

- A. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal
- B. Enable a mandatory label policy and default sensitivity label in Microsoft Purview compliance portal for Fabric users
- C. Grant Build permission on the shared semantic model
- D. Mark the item as Promoted in item settings

### 11. A merchandising analyst finishes building a seasonal clearance report and wants to highlight it as ready for team discovery without waiting for central governance committee sign-off. Which action can the analyst take immediately?

Domain: Maintain a data analytics solution

- A. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- B. Assign the Workspace Admin role
- C. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal
- D. Mark the item as Promoted in item settings

### 12. Four analytics engineers share a `Retail-Dev` workspace connected to the `main` branch in Azure Repos. How should an engineer develop a new Spark notebook and semantic model measure without destabilizing teammates' ongoing Dev runs?

Domain: Maintain a data analytics solution

- A. Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch
- B. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline
- C. Use Undo in the Fabric Workspace Source control pane to discard uncommitted workspace edits back to the last synced commit
- D. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches

### 13. Which four-step workflow properly moves a `.pbip` measure change from an engineer's isolated feature branch through Git review into `Test` and `Production` workspaces?

Domain: Maintain a data analytics solution

- A. Connect shared Dev workspace to main → Branch out to an isolated developer workspace and commit .pbip/Notebook edits → Merge pull request into main in Git → Run Update all in Dev and promote via Deployment Pipeline
- B. Connect Production directly to a feature branch → Edit semantic models live in Prod → Force-push binary .pbix files including cache.abf to main → Deploy backward to Development
- C. Branch out to personal My Workspace → Run Undo to push changes to GitHub → Delete .platform metadata files → Copy visuals manually into Production
- D. Edit items directly on main without branching → Merge an empty PR → Promote Dev to Test before running Update from Git → Configure Git integration last

### 14. Your retail BI squad converts a 550 MB `.pbix` file into a Git-tracked Power BI Desktop project (`.pbip`) containing `.gitignore` entry `**/____` to block cached VertiPaq data. Which two repository artifacts and hygiene rules ensure clean pull-request diffs without leaking customer rows? Select two.

Domain: Maintain a data analytics solution

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- D. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- E. Filter the RLS table using USERNAME() = [DomainLogin] without testing in the Fabric portal

### 15. In a Fabric Deployment Pipeline (`Dev -> Test -> Prod`), an Import semantic model in `Dev` reads `dev-pos-sql.database.windows.net`. How do you ensure promoting the model to `Prod` automatically binds it to `prod-pos-sql.database.windows.net` on every future release?

Domain: Maintain a data analytics solution

- A. Use Undo in the Fabric Workspace Source control pane to discard uncommitted workspace edits back to the last synced commit
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Configure Deployment pipeline data source and parameter rules on the Test and Production stages
- D. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline

### 16. You promote a Data Factory pipeline and a Direct Lake on OneLake semantic model across `Dev`, `Test`, and `Prod` stages where legacy SQL deployment rules are unavailable for Pipeline activities. Which Fabric ALM feature centralizes stage-specific workspace and Lakehouse IDs?

Domain: Maintain a data analytics solution

- A. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- B. Configure Deployment pipeline data source and parameter rules on the Test and Production stages
- C. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- D. Use a Fabric Variable library (or autobinding across paired workspace items) to parameterize stage-specific environment references

### 17. Only one report and its newly added upstream Lakehouse changed in `Retail-Dev`, while five unfinished experimental notebooks must remain in `Dev`. Which Deployment Pipeline action promotes the report without breaking lineage or promoting unfinished notebooks?

Domain: Maintain a data analytics solution

- A. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline
- B. Perform a selective deployment selecting the modified item together with Select related to include required upstream dependencies
- C. Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch
- D. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition

### 18. Before deprecating the `GrossMargin_Legacy` column in `GoldMerchandisingLakehouse`, you must identify all 19 semantic models and reports across four regional workspaces that depend on that Lakehouse and message their owners. Which Fabric view accomplishes both tasks?

Domain: Maintain a data analytics solution

- A. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- B. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- C. Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View
- D. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture

### 19. Proposed solution: To check whether any downstream workspaces consume a Dataflow Gen2 output before changing its output schema, an engineer inspects only the local workspace list view. Does this reveal cross-workspace consumers, and what should be used instead?

Domain: Maintain a data analytics solution

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- C. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- D. Configure Certified endorsement with the Master data label on authoritative core tables or semantic models

### 20. You must deploy three urgent Black Friday DAX measures from `Retail-Dev` to a 40 GB partitioned `Retail-Prod` semantic model during business hours without reprocessing historical partitions. Which four-step XMLA workflow is correct?

Domain: Maintain a data analytics solution

- A. Leave XMLA Endpoint = Read Only → Execute T-SQL DELETE across Warehouse schemas → Grant all report viewers Capacity Admin rights → Skip downstream impact analysis
- B. Set XMLA Endpoint = Off → Overwrite Production with an empty unpartitioned .pbix file → Purge all 5 years of historical incremental partitions → Re-import 3 billion rows during peak business hours
- C. Verify XMLA Endpoint = Read Write on target capacity → Connect ALM Toolkit to Dev source and Prod XMLA target → Compare schemas while hiding unchanged partitions and keeping Prod data sources → Validate and deploy metadata-only TMSL changes
- D. Open Production in DAX Studio → Edit measures manually in Production without committing to Git → Copy cache.abf into GitHub → Disable sensitivity labels

### 21. Nightly retail ETL updates only the `2026Q4` partition of `FactStoreSales`, and an Azure Automation runbook runs `____` (`{"refresh": {"type": "dataOnly", ...}}`) against `powerbi://api.powerbi.com/v1.0/myorg/Apparel-Prod`. Which two prerequisites and capabilities apply? Select two.

Domain: Maintain a data analytics solution

- A. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- B. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition
- C. Enable XMLA Endpoint = Read Write in Fabric Capacity workload settings and connect to powerbi://api.powerbi.com/v1.0/myorg/<WorkspaceName>
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- E. Configure DirectQuery storage mode

### 22. You want 30 junior merchandising analysts opening Power BI Desktop for the first time to connect straight to the `GoldRetailWarehouse` SQL endpoint without typing server connection strings or selecting the wrong connector. Which lightweight file should you distribute?

Domain: Maintain a data analytics solution

- A. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- D. Publish a single certified core semantic model in a data workspace and build thin live-connected Power BI reports in departmental workspaces

### 23. Twelve regional merchandising squads have copied the same `.pbix` file, resulting in 12 conflicting definitions of `[Comp Store Sales %]` and 12 redundant daily refreshes on the F64 capacity. Which architecture eliminates both problems?

Domain: Maintain a data analytics solution

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Configure Import storage mode
- D. Publish a single certified core semantic model in a data workspace and build thin live-connected Power BI reports in departmental workspaces

### 24. An apparel ERP database runs on Azure SQL Database with public network access disabled behind an Azure Private Endpoint inside `vnet-retail-prod`. Which gateway or connection type lets Dataflow Gen2 ingest from it without managing self-hosted Windows VMs?

Domain: Prepare data

- A. Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication
- B. Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet
- C. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- D. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes

### 25. Three pipeline authors need to orchestrate Copy activities from the same public Snowflake account using an organizational Service Principal without seeing or re-entering the client secret. What should a gateway/connection admin configure?

Domain: Prepare data

- A. Enable single sign-on (SSO) on the Direct Lake semantic model connection
- B. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- C. Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode

### 26. The Chief Data Officer wants one Fabric portal surface where domain owners can both filter `Certified` retail data products by domain and audit missing sensitivity labels or unendorsed Lakehouses across their estate. Which interface provides both views?

Domain: Prepare data

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- C. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- D. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results

### 27. E-commerce operations wants to discover all existing Kafka clickstreams and `Microsoft.Fabric.OneLake.____` arrival events in one catalog, trigger an Activator alert when supplier manifests arrive, and route clickstreams continuously. Which two Fabric capabilities work together? Select two.

Domain: Prepare data

- A. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- B. Use the Real-Time hub to subscribe to Microsoft.Fabric.OneLake.FileCreated events (or Capacity/CDC streams) and trigger an Activator rule
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- E. Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table

### 28. A European subsidiary stores 90 TB of governed Delta Parquet return logs in Amazon S3. You must analyze those tables in your Fabric Lakehouse alongside US store data without duplicating storage or scheduling nightly copy jobs. What should you configure?

Domain: Prepare data

- A. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching
- B. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- C. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging

### 29. Proposed solution: To replicate 180 operational loyalty tables from Azure Cosmos DB into OneLake with sub-minute freshness, you build 180 hourly full-load Dataflow Gen2 queries. Is this optimal, and what zero-ETL Fabric feature replaces it?

Domain: Prepare data

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- C. Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging

### 30. Every night you must move 4 TB of uncompressed raw CSV point-of-sale extracts from an SFTP server into a Lakehouse `Files/bronze/` folder as fast and cheaply as possible with zero column transformations. Which Fabric ingestion tool fits best?

Domain: Prepare data

- A. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- B. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- C. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- D. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view

### 31. You are standardizing ingestion patterns for a global retail Fabric tenant: (1) zero-copy access to existing ADLS Gen2 Parquet lakes, (2) continuous zero-ETL replication from Snowflake operational tables, and (3) citizen-developer M transformations over 40 SaaS REST connectors with bulk staging. Which three Fabric capabilities match these three needs? Select three.

Domain: Prepare data

- A. Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog
- B. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- C. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- D. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching
- E. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- F. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations

### 32. Your merchandising finance team writes stored procedures requiring multi-table `BEGIN TRANSACTION ... COMMIT` blocks, `UPDATE`/`DELETE` T-SQL statements, and native T-SQL column-level security without writing PySpark. Which Fabric data store should you provision?

Domain: Prepare data

- A. Choose a Fabric Data Warehouse
- B. Choose a Fabric Lakehouse
- C. Choose a SQL database in Microsoft Fabric
- D. Choose a Fabric Eventhouse (KQL database)

### 33. Data engineers process raw JPEG product images alongside semi-structured JSON catalog feeds and curated Delta tables using PySpark notebooks and Spark SQL. Which Fabric item natively stores both unmanaged `Files/` and managed Delta `Tables/`?

Domain: Prepare data

- A. Choose a Fabric Lakehouse
- B. Choose a Fabric Data Warehouse
- C. Configure Import storage mode
- D. Choose a SQL database in Microsoft Fabric

### 34. A retail platform team needs (1) an analytical store for 500,000 RFID warehouse gate pings per second queried with time-series functions, and (2) an operational OLTP store inside Fabric for a store-associate shift-swapping web app that auto-replicates to OneLake. Which two Fabric stores should they choose? Select two.

Domain: Prepare data

- A. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- D. Choose a Fabric Eventhouse (KQL database)
- E. Choose a SQL database in Microsoft Fabric

### 35. A legacy retail forecasting team maintains complex Power Query M logic inside a large Import semantic model. Data scientists want to read those exact refreshed Import model tables from a Lakehouse Spark notebook via OneLake shortcuts without rebuilding the M scripts. Which setting enables this?

Domain: Prepare data

- A. Enable OneLake integration in the Import semantic model settings so imported model tables export as Delta tables to OneLake
- B. Point Direct Lake on SQL directly at an Eventhouse KQL database without enabling OneLake availability
- C. Use ALM Toolkit over the XMLA endpoint to compare Dev and Prod semantic models and deploy only new measures without reprocessing unchanged partitions
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode

### 36. You want a Data Factory pipeline to invoke `EXEC ____ @RunDate = '2026-10-30'` (`gold.usp_LoadDailyMarkdowns`) to validate staging counts and upsert a Gold fact table using T-SQL. Where must this T-SQL DML procedure be created?

Domain: Prepare data

- A. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic

### 37. Proposed solution: You create a standard non-materialized T-SQL view `vw_NetStoreSales` in a Lakehouse SQL analytics endpoint and attempt to add it as a Direct Lake on OneLake table. Will this keep queries in pure Direct Lake memory, and what should you build instead?

Domain: Prepare data

- A. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- B. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- C. Configure DirectQuery storage mode
- D. Use a Lakehouse Materialized Lake View (or persisted Gold Delta table) instead of a non-materialized SQL analytics endpoint view for Direct Lake on OneLake

### 38. In a Fabric Warehouse, you write `CREATE FUNCTION dbo.fn_CleanSKU(@Raw VARCHAR(50)) RETURNS TABLE AS ____ (SELECT UPPER(TRIM(@Raw)) AS CleanSKU);`. Why are inline `RETURN (...)` table-valued functions preferred over multi-statement scalar loops in Warehouse ELT?

Domain: Prepare data

- A. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- B. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- C. Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic
- D. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository

### 39. Proposed solution: Retail SKUs arrive from three acquired brands (`"US-104"`, `"EU-104"`, `"APAC-104"`) where raw integer product codes collide across systems, so a developer uses the raw integer `ProductCode` directly as the `DimProduct` primary key. Does this prevent collisions, and how should `DimProduct` be keyed instead?

Domain: Prepare data

- A. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions
- D. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension

### 40. Retail buyers compare NRF 4-5-4 fiscal weeks, holiday blackout flags, and comparable-store prior-year weeks across `FactSales`, `FactInventory`, and `FactReturns`. What table should you enrich the Gold layer with?

Domain: Prepare data

- A. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- B. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- C. Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes
- D. Configure DirectQuery storage mode

### 41. A Silver-to-Gold PySpark notebook enriches 300 million e-commerce clickstream rows (`df.____("Host", F.regexp_extract("Url", ...))`) and surrogate dimension keys, but currently takes 75 minutes because of a Python `@udf` calling `urllib.parse`. Which two changes follow Fabric engineering best practices? Select two.

Domain: Prepare data

- A. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- B. Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs
- C. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- D. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- E. Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions

### 42. A receipt header table (`OrderTotal`, `TaxTotal`, `ShippingFee`) is joined directly to receipt line items (`LineQty`, `ExtendedPrice`) without allocating header shipping fees, causing `SUM(ShippingFee)` to multiply by line count. Which star-schema principle was violated?

Domain: Prepare data

- A. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- B. Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures
- C. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place
- D. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals

### 43. You are implementing nightly SCD Type 2 processing for `DimStore` in a Fabric Warehouse when store district assignments change. Which four-step execution sequence preserves historical accuracy?

Domain: Prepare data

- A. Truncate the Gold dimension table → Reassign fresh random surrogate keys to all historical rows → Join historical facts without updating foreign keys → Set IsCurrent = 1 on every version
- B. Stage and deduplicate incoming records by natural key → Compare tracked attributes against active (IsCurrent = 1) Gold rows → Expire changed active rows (EffectiveEndDate, IsCurrent = 0) → Insert new active versions with fresh surrogate keys
- C. Insert new versions with IsCurrent = 0 first → Overwrite old EffectiveStartDate values in place → Remove the natural business key column → Deduplicate after publishing reports
- D. Insert raw duplicate staging rows directly into FactSales → Delete unmatched dimension keys → Leave EffectiveStartDate NULL → Enable Assume referential integrity on broken keys

### 44. You are designing a greenfield omnichannel retail Lakehouse backing Direct Lake semantic models. Which three architectural choices align with Microsoft's dimensional modeling guidance? Select three.

Domain: Prepare data

- A. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- B. Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures
- C. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- D. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns
- E. Organize OneLake into Bronze (raw immutable), Silver (validated, deduplicated, conformed), and Gold (star-schema dimensions and facts with V-Order)
- F. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension

### 45. In `SilverWarehouse`, `DimStore` links to `DimDistrict`, which links to `DimRegion`, which links to `DimCountry`. Before exposing `DimStore` to a Direct Lake model, what transformation should you perform for `GoldWarehouse`?

Domain: Prepare data

- A. Create a local composite model using DirectQuery for Power BI semantic models and Analysis Services to combine a certified core semantic model with a departmental Excel/SQL table
- B. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()
- C. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- D. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension

### 46. An executive mobile scorecard displays only daily total net sales by Region and Division across 8 billion historical POS scan rows, and never drills to individual receipts. How do you minimize Direct Lake memory and CU usage?

Domain: Prepare data

- A. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Configure DirectQuery storage mode
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging

### 47. You are writing a Gold Warehouse summary query `SELECT Channel, Region, SUM(NetSales) AS Revenue FROM gold.FactPOS ____;` that must output `(Channel, Region)` subtotals, `(Region)` subtotals, and a single grand-total row without `UNION ALL`. Which clause fills the blank?

Domain: Prepare data

- A. TRY_CAST(RawReading AS DECIMAL(18, 4))
- B. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- C. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- D. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)

### 48. In PySpark, you aggregate `df.groupBy("StoreId", "SaleDate").agg(F.sum("NetAmt").alias("DailySales"), F.approx_count_distinct("BasketId").alias("ApproxBaskets"))`. Why would an analytics engineer choose `approx_count_distinct` over exact `countDistinct` on a 5-billion-row Bronze-to-Gold dashboard tile?

Domain: Prepare data

- A. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- B. Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs
- C. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'
- D. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table

### 49. Complete this Spark SQL Gold upsert so unchanged rows do not rewrite Delta Parquet files unnecessarily: `MERGE INTO gold.dim_customer AS target USING silver.stg_customer AS source ON target.CustomerId = source.CustomerId ____ target.Email = source.Email, target.Tier = source.Tier WHEN NOT MATCHED THEN INSERT *;`?

Domain: Prepare data

- A. WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET
- B. RANK() OVER (ORDER BY SpecimenId DESC)
- C. CAST(RawReading AS FLOAT)
- D. ADD BLOCK PREDICATE dbo.sp_checkregion(RegionCode) AFTER INSERT

### 50. Before inserting daily `FactReturns` rows, a Dataflow Gen2 validation query must output only return transactions whose `OriginalReceiptId` does NOT exist in `FactSales`. Which Power Query Merge join kind isolates those orphan returns?

Domain: Prepare data

- A. Apply broadcast(dim_df) in PySpark when joining a multi-hundred-million-row fact DataFrame with a small dimension DataFrame
- B. Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement
- C. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- D. Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table

### 51. In a retail Silver-to-Gold PySpark notebook, you join a 600-million-row `fact_df` against a 4 MB `dim_store_df` (`fact_df.join(____)`) and then upsert the result into `gold.fact_sales`. Which two techniques optimize shuffle cost and ACID writes? Select two.

Domain: Prepare data

- A. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- B. fact_df.join(F.broadcast(dim_store_df), on="StoreKey", how="left")
- C. Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- E. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations

### 52. Order webhook retries produced duplicate `OrderId` rows in `silver.stg_orders`. Complete the CTE expression `SELECT *, ____ AS rn FROM silver.stg_orders` (replacing `SpecimenId` conceptually with the entity key) that deterministically keeps one newest row per key when filtered by `WHERE rn = 1`?

Domain: Prepare data

- A. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- B. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- C. RANK() OVER (ORDER BY SpecimenId DESC)
- D. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)

### 53. Proposed solution: An analyst opens a 25-million-row supplier feed in Dataflow Gen2, sees `0% Error / 0% Empty` in the default preview bar, and promotes it directly to Gold without changing profiling scope or deduplicating. Which two steps actually verify full-dataset quality and remove duplicate business keys? Select two.

Domain: Prepare data

- A. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- B. Launch Data Wrangler from a Fabric Spark notebook (or enable Power Query Column profiling based on entire data set) to inspect nulls, duplicates, and distributions and export generated PySpark code
- C. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- D. Deduplicate using ROW_NUMBER() OVER (PARTITION BY BusinessKey ORDER BY ModifiedTimestamp DESC) = 1
- E. Filter Incremental Refresh with OrderDate >= RangeStart AND OrderDate <= RangeEnd using inclusive operators on both boundaries

### 54. Legacy store scale CSV files occasionally contain `"CALIBRATING"` inside the `WeightKg` string column. Which T-SQL expression safely parses valid weights to exact four-decimal precision while turning `"CALIBRATING"` into `NULL` instead of failing the Warehouse load?

Domain: Prepare data

- A. RANK() OVER (ORDER BY SpecimenId DESC)
- B. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- C. CAST(RawReading AS FLOAT)
- D. TRY_CAST(RawReading AS DECIMAL(18, 4))

### 55. After adding a Spark Delta table containing a `ReceiptSignature` (`BINARY`) column and a `ShippingAddress` (`STRUCT<street:string,zip:string>`) column to a Direct Lake model, those columns fail to load. How should you prepare the Gold table?

Domain: Prepare data

- A. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- B. Configure shared dimension tables in Dual storage mode inside a composite model
- C. Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake
- D. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically

### 56. In Dataflow Gen2 reading from an Azure SQL source, `View Native Query` is active on Step 2 (`Filtered Rows`), disabled on Step 3 (`Split Column by Delimiter` using custom regex M logic), and Step 4 filters `FiscalYear = 2026`. How do you restore query folding for the `FiscalYear` filter?

Domain: Prepare data

- A. Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled
- B. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- C. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- D. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'

### 57. A 3-billion-row Lakehouse Delta table is partitioned by `SaleYearMonth` and sorted on `SaleDate`. Why does `WHERE SaleDate >= '2026-10-01' AND SaleDate < '2026-11-01'` scan 98% fewer Parquet bytes than `WHERE LEFT(CONVERT(VARCHAR, SaleDate, 120), 7) = '2026-10'`?

Domain: Prepare data

- A. Filter on physical Delta partition or liquid-clustered date columns using sargable range predicates (OrderDate >= '2026-01-01') without wrapping the column in functions
- B. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- C. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'
- D. CAST(RawReading AS FLOAT)

### 58. A merchandising planner with `ReadData` access on `GoldRetailWarehouse` does not know T-SQL syntax, wants to join `FactMarkdowns` with `DimDepartment` in the browser, filter `DiscountPct > 0.30`, and save the result as a reusable SQL view. Which Fabric tool should they use?

Domain: Prepare data

- A. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- B. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- C. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results
- D. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts

### 59. When an analyst builds a multi-step transformation in the Fabric Visual query editor over a Lakehouse SQL analytics endpoint and selects `Save as view`, where does the transformation compute execute at query time?

Domain: Prepare data

- A. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- B. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- C. Use ALM Toolkit over the XMLA endpoint to compare Dev and Prod semantic models and deploy only new measures without reprocessing unchanged partitions
- D. Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic

### 60. `ApparelWarehouse` and `ClickstreamLakehouse` reside in the same `Retail-Prod` Fabric workspace. What is the simplest zero-copy way to complete `SELECT c.CustomerKey, w.SessionId FROM dbo.DimCustomer c JOIN ____ w ON c.CustomerId = w.CustomerId` inside `ApparelWarehouse`?

Domain: Prepare data

- A. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- B. Query across a Warehouse and a Lakehouse SQL analytics endpoint in the same workspace using three-part T-SQL naming (SalesLakehouse.dbo.RawOrders)
- C. Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet
- D. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching

### 61. An erroneous price-update script ran at `07:15 UTC` in `GoldRetailWarehouse`. Complete `SELECT SKU, UnitPrice FROM dbo.DimSKU ____;` to inspect exact prices as of `2026-10-28T06:00:00.000` without restoring backups?

Domain: Prepare data

- A. CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales
- B. ADD BLOCK PREDICATE dbo.sp_checkregion(RegionCode) AFTER INSERT
- C. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- D. OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')

### 62. A retail SQL analyst working in `GoldRetailWarehouse` must (1) calculate each store's cumulative year-to-date sales alongside week-over-week delta on detail rows without self-joins, and (2) create a zero-copy point-in-time table clone prior to a risky pricing script. Which two T-SQL features should they use? Select two.

Domain: Prepare data

- A. Write T-SQL window functions using LAG(...) OVER (PARTITION BY ... ORDER BY ...) and SUM(...) OVER (... ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
- B. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- C. Query historical Warehouse state using SELECT ... FROM dbo.FactSales OPTION (FOR TIMESTAMP AS OF '2026-10-15T00:00:00') or CREATE TABLE ... AS CLONE OF
- D. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- E. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'

### 63. An e-commerce site reliability analyst queries `CheckoutEvents` in Eventhouse to feed `series_decompose_anomalies()`, which requires a continuous 1-minute array per region where minutes with zero checkouts explicitly populate `0`. Which KQL operator completes `CheckoutEvents ____`?

Domain: Prepare data

- A. | make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion
- B. | summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)
- C. | summarize arg_max(IngestionTime, *) by SpecimenId
- D. | mv-expand PhaseReading = parse_json(Payload).PhaseReadings

### 64. You want to prototype four variations of `[Comparable Store YoY %]` against `RetailCore` in Power BI Desktop, view all four outputs together by `Region` and `Quarter` in a tabular result grid, and apply only the winning DAX definition to the model. Which built-in view supports this workflow?

Domain: Prepare data

- A. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- B. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- C. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results
- D. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view

### 65. For a retail governance audit, you open DAX Query View on `RetailCore` and run `____` to return a table listing every measure's name, home table, DAX expression, format string, and hidden status. Which query completes the blank?

Domain: Prepare data

- A. NAMEOF('DimTrade'[CurrencyPair])
- B. CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))
- C. [ManagerEmail] = USERPRINCIPALNAME()
- D. EVALUATE INFO.VIEW.MEASURES()

### 66. A boutique footwear division refreshes a 150 MB dataset once nightly from a legacy on-premises Oracle database and requires full DAX calculated-column flexibility and sub-100 ms slicer speed. Which storage mode is best?

Domain: Implement and manage semantic models

- A. Configure shared dimension tables in Dual storage mode inside a composite model
- B. Configure Direct Lake storage mode
- C. Configure Import storage mode
- D. Configure DirectQuery storage mode

### 67. In a composite semantic model containing an `Import` daily sales summary table and a `DirectQuery` receipt-line detail table, both tables relate to `DimStore` and `DimDate`. Which storage mode on `DimStore` and `DimDate` lets summary queries run 100% in memory while detail queries push native SQL joins down?

Domain: Implement and manage semantic models

- A. Configure shared dimension tables in Dual storage mode inside a composite model
- B. Configure Import storage mode
- C. Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop)
- D. Configure DirectQuery storage mode

### 68. Your semantic model relates `DimCalendar[DateKey]` (`20261030` integer) to `FactSales[OrderDateKey]`, and `TOTALYTD([Net Sales], DimCalendar[CalendarDate])` returns blank unless `ALL(DimCalendar)` is added manually. What semantic-model configuration fixes time intelligence cleanly while keeping integer keys?

Domain: Implement and manage semantic models

- A. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- B. Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions

### 69. During a semantic-model readiness review for `ApparelSales`, analysts complain that `April`, `August`, `December` sort alphabetically on charts, users keep dragging raw `StoreKey` into visuals as `Sum of StoreKey`, and 14 hidden `LocalDateTable_*` tables consume 900 MB. Which two configurations resolve all three issues? Select two.

Domain: Implement and manage semantic models

- A. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- B. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- E. Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column

### 70. `FactOrders` links to `Calendar` via an active relationship on `OrderDateKey` and an inactive relationship on `SettlementDateKey` (or `ShipDateKey`). Complete `Settled Sales = ____` so the measure aggregates by the inactive date relationship without duplicating `Calendar`?

Domain: Implement and manage semantic models

- A. CALCULATE([Encounter Count], CROSSFILTER('FactEncounter'[EncounterKey], 'BridgeEncounterDiag'[EncounterKey], BOTH))
- B. IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK())
- C. CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))
- D. CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))

### 71. Proposed solution: In a loyalty promotions model where one `Order` can redeem multiple `PromoCodes`, an analyst enables permanent `Both` bidirectional cross-filtering on every relationship in the semantic model. Does this follow best practice, and how should `CALCULATE([Redemptions], ____)` over `BridgeOrderPromo` be modeled instead?

Domain: Implement and manage semantic models

- A. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()
- B. Introduce a deduplicated Bridge table between the two dimensions and scope bidirectional propagation strictly inside specific measures using CROSSFILTER(..., BOTH)
- C. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- D. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear

### 72. A DirectQuery semantic model over a curated Retail Warehouse guarantees through ETL constraints that every `FactSales[StoreKey]` matches a non-null `DimStore[StoreKey]`. Enabling which relationship setting switches generated SQL from `LEFT OUTER JOIN` to faster `____` (`INNER JOIN`)?

Domain: Implement and manage semantic models

- A. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- B. Set DirectLakeBehavior = DirectLakeOnly on a Direct Lake on SQL semantic model so queries fail fast instead of silently falling back to slow DirectQuery
- C. Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column
- D. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid

### 73. Complete `Net Line Revenue = ____(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct]))` so discounted line revenue multiplies row-by-row without materializing a new fact column?

Domain: Implement and manage semantic models

- A. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- B. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table
- C. Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches
- D. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)

### 74. A measure `Tier Bonus = ____ CurrentMargin = [Net Margin] RETURN IF(CurrentMargin > 100000, CurrentMargin * 0.08, ...)` previously evaluated `[Net Margin]` three separate times per matrix cell. Which DAX construct eliminates the redundant Storage Engine scans?

Domain: Implement and manage semantic models

- A. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- B. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table
- C. Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches
- D. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows

### 75. In a matrix hierarchy `Division -> Department -> SKU`, `[Unit Margin]` is meaningful only when drilled to individual `SKU` rows (`Unit Margin Display = ____`) and must display blank on `Department`, `Division`, and Grand Total rows even when a department contains only one SKU. Which DAX expression fills the blank?

Domain: Implement and manage semantic models

- A. IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK())
- B. EVALUATE INFO.VIEW.MEASURES()
- C. NAMEOF('DimTrade'[CurrencyPair])
- D. [ManagerEmail] = USERPRINCIPALNAME()

### 76. You are writing two retail DAX measures: (1) `[Red Apparel Sales]` that must return `BLANK()` when a report user slices exclusively on `"Blue"` instead of overwriting the `"Blue"` slicer, and (2) `[Prior Fiscal Period Sales]` on a custom 4-5-4 calendar where `DATEADD` cannot operate. Which two DAX patterns solve these requirements? Select two.

Domain: Implement and manage semantic models

- A. CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC)))
- B. Pass simple column predicates wrapped in KEEPFILTERS(DimProduct[Color] = "Red") to CALCULATE instead of FILTER(ALL(FactSales), ...)
- C. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- D. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- E. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows

### 77. On a Calculation Group item or KPI measure switching between currency totals and `"YoY Growth"` percentages (`Format String Expression = ____`), which dynamic format string expression displays `"0.0%"` for `"YoY Growth"` while preserving each base measure's native `$` or integer mask?

Domain: Implement and manage semantic models

- A. [ManagerEmail] = USERPRINCIPALNAME()
- B. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- C. IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())
- D. NAMEOF('DimTrade'[CurrencyPair])

### 78. Merchandising VPs want a single matrix visual (`SliceBy = { ("Brand", ____('DimItem'[Brand]), 0), ... }`) where a button slicer swaps the matrix rows between `Brand`, `StoreFormat`, `BuyerName`, and `PriceBand` without duplicate bookmarked visuals. Which Power BI modeling feature provides this natively?

Domain: Implement and manage semantic models

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Create a Calculation Group with Calculation Items referencing SELECTEDMEASURE() and explicit Precedence ordering (automatically setting DiscourageImplicitMeasures = true)
- C. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- D. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()

### 79. An enterprise Import semantic model on an F64 capacity grows past 11 GB compressed during holiday peak and refresh fails with memory/size limit errors despite ample capacity RAM. Which semantic-model setting lifts the default compressed model ceiling up to the capacity SKU limit?

Domain: Implement and manage semantic models

- A. Configure DirectQuery storage mode
- B. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- C. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- D. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages

### 80. Beyond supporting multi-gigabyte models, why do enterprise BI teams enable `Large semantic model storage format` immediately on new Fabric semantic models managed by Tabular Editor and ALM Toolkit?

Domain: Implement and manage semantic models

- A. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- B. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- C. Mark the item as Promoted in item settings
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 81. Which two composite-modeling patterns apply when (1) accelerating 95% of grouped queries over a 5-billion-row DirectQuery table without importing atomic lines, and (2) letting a regional analyst join a personal Excel store-remodel sheet onto a corporate Certified semantic model without duplicating it? Select two.

Domain: Implement and manage semantic models

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- C. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- D. Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table
- E. Create a local composite model using DirectQuery for Power BI semantic models and Analysis Services to combine a certified core semantic model with a departmental Excel/SQL table

### 82. Users interacting with a DirectQuery loss-prevention report select 8 store IDs one by one in a multi-select slicer, firing 8 slow SQL queries before they even inspect the table visual. Which report-level setting eliminates the 7 intermediate queries?

Domain: Implement and manage semantic models

- A. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- B. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- C. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- D. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages

### 83. VertiPaq Analyzer shows that two columns — `POSReceiptGUID` (420 million unique strings, never used in any relationship or visual) and `ScanTimestampMs` (390 million unique millisecond datetimes) — account for 78% of your model's RAM. What is the highest-impact optimization?

Domain: Implement and manage semantic models

- A. Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer

### 84. A Direct Lake merchandising report measure takes 14 seconds on cold cache. Which four-step diagnostic and tuning workflow follows Microsoft's optimization methodology?

Domain: Implement and manage semantic models

- A. Hide slow measures in Display Folders → Turn on Auto date/time → Split one Gold dimension into 6 normalized snowflake tables → Remove calendar surrogate keys
- B. Test queries only against warm VertiPaq cache without Clear Cache → Add high-cardinality GUID calculated columns to FactSales → Force DirectQueryOnly behavior → Add 45 single-value card visuals to one page
- C. Immediately upgrade from F64 to F512 without profiling → Enable bidirectional cross-filtering on all relationships → Convert numeric measures to FORMAT() strings → Disable V-Order on Gold tables
- D. Capture visual timings in Performance Analyzer → Profile captured DAX in DAX Studio with Server Timings and Query Plan → Refactor FILTER(Fact,...) into VAR-cached SE column predicates and run V-Order OPTIMIZE → Re-test with Clear Cache

### 85. A PySpark notebook finishes appending 4 million morning POS rows into `gold.fact_sales` at `06:10 UTC`, yet a Direct Lake semantic model with automatic updates turned off still displays yesterday's totals at `06:30 UTC`. Why, and what lightweight operation exposes the new Parquet files?

Domain: Implement and manage semantic models

- A. Configure Import storage mode
- B. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- C. Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes
- D. Expect Direct Lake on OneLake to automatically fall back to DirectQuery against the SQL analytics endpoint when capacity memory guardrails are exceeded

### 86. Your team operates a Direct Lake on SQL semantic model over a Gold Lakehouse fed by frequent micro-batches. Which three configurations prevent tiny-file guardrail degradation, control point-in-time visibility after ETL runs, and stop silent slow DirectQuery fallbacks? Select three.

Domain: Implement and manage semantic models

- A. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- B. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- C. Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes
- D. Set DirectLakeBehavior = DirectLakeOnly on a Direct Lake on SQL semantic model so queries fail fast instead of silently falling back to slow DirectQuery
- E. Expect Direct Lake on OneLake to automatically fall back to DirectQuery against the SQL analytics endpoint when capacity memory guardrails are exceeded
- F. Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails

### 87. You want to upgrade an existing Direct Lake on SQL semantic model (containing only Delta tables, no SQL views) to Direct Lake on OneLake without breaking bound downstream reports. Which four-step Power BI Desktop workflow performs the migration?

Domain: Implement and manage semantic models

- A. Keep non-materialized SQL analytics endpoint views as the only sources → Switch TMDL expression to AzureStorage.DataLake without materializing Delta tables → Enable DirectQuery fallback on Direct Lake on OneLake → Bind an On-premises gateway
- B. Live edit the model in Power BI Desktop and save a Version history point → Script the semantic model in TMDL view → Replace Sql.Database(...) with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...") → Apply TMDL and run framing refresh
- C. Download the Direct Lake model as an offline Import .pbix → Convert all tables to Dual storage mode → Replace AzureStorage.DataLake with OleDb.DataSource → Re-upload to My Workspace
- D. Delete the semantic model in Production breaking report GUID bindings → Recreate measures manually from screenshots → Share Lakehouse Admin rights with all report viewers → Disable V-Order

### 88. You must configure Incremental Refresh on a 700-million-row `FactCatalogOrders` Import table retaining 5 years of history and refreshing only the trailing 10 days. Which four-step workflow avoids duplicate midnight rows and broken query folding?

Domain: Implement and manage semantic models

- A. Filter OrderDate > RangeEnd → Configure Detect data changes on the exact same OrderDate partition column → Disable query folding → Run XMLA clearValues without processing
- B. Create Text parameters named StartDate and EndDate → Add a custom M step breaking query folding before filtering → Use >= and <= inclusive bounds on both sides → Refresh only in Power BI Desktop
- C. Publish an unfiltered 2-billion-row Import PBIX locally first → Define RangeStart in DAX calculated tables afterward → Set storage mode to Direct Lake on OneLake → Enable VNet gateway on Direct Lake
- D. Create case-sensitive DateTime parameters RangeStart and RangeEnd → Apply foldable half-open filter (>= RangeStart and < RangeEnd) → Configure table Incremental refresh policy → Publish to workspace and run initial refresh to generate partitions

---

## Case study — CartVerve Marketplace

CartVerve Marketplace builds a Medallion Lakehouse and Warehouse over 1.2 billion e-commerce order lines. Category reassignments on merchants must preserve historical order attribution prior to the change date, late-arriving orders occasionally arrive before new merchant IDs register, and multi-hop Category -> Subcategory -> Brand joins slow executive Direct Lake dashboards.

The next 3 questions refer to **CartVerve Marketplace**. Read the scenario brief once, then answer each item independently.

### 89. Which dimensional design on `DimMerchant` ensures orders placed before a merchant's category reassignment remain attributed to the historical category while new orders reflect the updated category?

Domain: Prepare data

- A. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)
- B. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- C. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns
- D. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place

### 90. Late-arriving marketplace orders occasionally land before a newly onboarded `MerchantNaturalId` exists in `DimMerchant`. How should the Gold fact load handle those rows?

Domain: Prepare data

- A. Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake
- B. Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE
- C. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- D. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table

### 91. How should you eliminate the slow `Category -> Subcategory -> Brand` multi-hop join chain affecting executive Direct Lake dashboards?

Domain: Prepare data

- A. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place
- B. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- C. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- D. Choose a Fabric Eventhouse (KQL database)

---

## Case study — LoomCraft Home

LoomCraft Home has six analytics engineers co-authoring a flagship semantic model and 14 report pages. Binary .pbix merges in GitHub constantly conflict, executives want one slicer switching YTD, QTD, PY, and YoY% across 35 base measures with proper $ vs % formatting on bar charts, and a landing page with 38 KPI cards takes 9 seconds to render despite 40 ms DAX queries.

The next 3 questions refer to **LoomCraft Home**. Read the scenario brief once, then answer each item independently.

### 92. Which file format eliminates binary GitHub merge conflicts across the six analytics engineers co-authoring the flagship model and 14 report pages?

Domain: Maintain a data analytics solution

- A. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode

### 93. You author a Calculation Item `YTD = CALCULATE(____, DATESYTD('Calendar'[Date]))` across all 35 base measures while keeping numeric bar-chart plotting for both `$` currency and `%` growth. Which modeling feature and DAX substitution mechanism satisfies this?

Domain: Implement and manage semantic models

- A. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- B. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table
- C. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- D. Create a Calculation Group with Calculation Items referencing SELECTEDMEASURE() and explicit Precedence ordering (automatically setting DiscourageImplicitMeasures = true)

### 94. Why does the landing page with 38 KPI cards take 9 seconds to render despite 40 ms DAX queries, and which tool confirms the bottleneck?

Domain: Implement and manage semantic models

- A. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- B. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- C. Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails
- D. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages

---

## Case study — ShelfPulse POS

ShelfPulse POS streams 90,000 checkout scanner JSON events per minute from 1,100 stores into a Fabric Eventhouse KQL database. Store operations needs 5-minute anomaly buckets in KQL, while merchandising data engineers want to join those same telemetry tables with Lakehouse inventory Delta tables and expose both inside a single Direct Lake semantic model without duplicating ingestion pipelines.

The next 3 questions refer to **ShelfPulse POS**. Read the scenario brief once, then answer each item independently.

### 95. In which order should you expose the checkout Eventhouse KQL telemetry to Lakehouse Spark joins and a unified Direct Lake semantic model without duplicating ingestion?

Domain: Prepare data

- A. Export KQL query results manually to CSV every hour → Email CSVs to analysts → Import into binary .pbix files → Publish to My Workspace
- B. Create an Amazon S3 external shortcut to the KQL URI before enabling OneLake availability → Set storage mode to Dual only → Enable Auto date/time → Run XMLA clearValues
- C. Ingest streaming telemetry into an Eventhouse KQL database → Enable OneLake availability on the KQL database or table → Create an internal OneLake shortcut in the Lakehouse → Add the table to a Direct Lake on OneLake semantic model
- D. Create a Direct Lake on SQL model directly over the KQL queryset → Disable OneLake availability → Configure an On-premises data gateway → Run T-SQL MERGE on the KQL database

### 96. Store operations runs `ScannerEvents | where EventTime > ago(2h) ____` in a KQL queryset to compute 99th-percentile scan latency across fixed 5-minute intervals. Which KQL clause completes the query?

Domain: Prepare data

- A. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- B. | mv-expand PhaseReading = parse_json(Payload).PhaseReadings
- C. | summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)
- D. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)

### 97. Merchandising wants one semantic model combining the OneLake-enabled Eventhouse table, the Inventory Lakehouse table, and an imported promotional calendar from SharePoint with regular relationships. Which design works?

Domain: Implement and manage semantic models

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- C. Point Direct Lake on SQL directly at an Eventhouse KQL database without enabling OneLake availability
- D. Build a Direct Lake on OneLake composite semantic model combining Direct Lake fact tables from OneLake with Import dimension/target tables using regular relationships

---

## Case study — Solstice Apparel

Solstice Apparel runs an F64 Fabric capacity serving 400 regional store managers. Store managers hold Workspace Viewer access and must see only their assigned region's rows AND never see wholesale supplier cost columns on the Gold Sales Delta table across Spark, SQL, and Direct Lake reports, without maintaining separate physical tables per region.

The next 3 questions refer to **Solstice Apparel**. Read the scenario brief once, then answer each item independently.

### 98. How should you configure OneLake security on the Gold Sales Delta table so regional store managers see only their assigned region's rows AND cannot read wholesale supplier cost columns?

Domain: Maintain a data analytics solution

- A. Define both the RLS filter and CLS column allow-list inside a single OneLake security Grant role with Read permission
- B. Create two separate OneLake security roles on the same table — Role A containing the RLS filter and Role B containing the CLS column rule — and assign the user to both
- C. Create a OneLake security role with ReadWrite permission and attach an RLS predicate
- D. Create a Deny role in OneLake security to revoke table access granted by another OneLake role or Workspace Member role

### 99. Store managers querying the Lakehouse SQL analytics endpoint currently see all regions because the endpoint runs under the Lakehouse owner's identity. Which configuration enforces their OneLake security roles on T-SQL queries?

Domain: Maintain a data analytics solution

- A. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows
- B. Bind the Direct Lake semantic model to a cloud connection with a fixed identity and disable SSO
- C. Assign the Workspace Contributor role
- D. Switch the Lakehouse SQL analytics endpoint to User's identity mode

### 100. Which semantic model storage architecture lets the merchandising dashboard read the OneLake-secured Gold Sales table with in-memory Direct Lake speed and zero DirectQuery fallback?

Domain: Implement and manage semantic models

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop)
- C. Configure DirectQuery storage mode
- D. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)

---

## Answer key and explanations

### Question 1 — D

Answer: Assign the Workspace Contributor role. Workspace Contributor grants item creation, editing, and job execution without permitting item sharing, app publishing, or role management. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Incorrect for this requirement. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. Why the keyed choice wins: Workspace Contributor grants item creation, editing, and job execution without permitting item sharing, app publishing, or role management.
- **B:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: Workspace Contributor grants item creation, editing, and job execution without permitting item sharing, app publishing, or role management.
- **C:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: Workspace Contributor grants item creation, editing, and job execution without permitting item sharing, app publishing, or role management.
- **D:** Correct. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. In this scenario: Workspace Contributor grants item creation, editing, and job execution without permitting item sharing, app publishing, or role management.

### Question 2 — A

Answer: Assign the Workspace Viewer role. Contributors bypass semantic-model RLS completely; assigning the Workspace Viewer role ensures DAX RLS filters every query from those buyers. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Correct. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. In this scenario: Contributors bypass semantic-model RLS completely; assigning the Workspace Viewer role ensures DAX RLS filters every query from those buyers.
- **B:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: Contributors bypass semantic-model RLS completely; assigning the Workspace Viewer role ensures DAX RLS filters every query from those buyers.
- **C:** Incorrect for this requirement. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. Why the keyed choice wins: Contributors bypass semantic-model RLS completely; assigning the Workspace Viewer role ensures DAX RLS filters every query from those buyers.
- **D:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: Contributors bypass semantic-model RLS completely; assigning the Workspace Viewer role ensures DAX RLS filters every query from those buyers.

### Question 3 — C, D

Answers: Assign permissions to Microsoft Entra security groups rather than individual users; Assign the Workspace Member role. Assigning the Workspace Member role via a Microsoft Entra security group grants app-publishing, sharing, and OneLake-role administration while blocking workspace deletion and avoiding per-user role drift. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: Assigning the Workspace Member role via a Microsoft Entra security group grants app-publishing, sharing, and OneLake-role administration while blocking workspace deletion and avoiding per-user role drift.
- **B:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: Assigning the Workspace Member role via a Microsoft Entra security group grants app-publishing, sharing, and OneLake-role administration while blocking workspace deletion and avoiding per-user role drift.
- **C:** Correct. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. In this scenario: Assigning the Workspace Member role via a Microsoft Entra security group grants app-publishing, sharing, and OneLake-role administration while blocking workspace deletion and avoiding per-user role drift.
- **D:** Correct. Granting workspace, item, deployment-pipeline, and RLS role memberships to Microsoft Entra security groups centralizes joiner/mover/leaver governance and scales across workspaces without per-user ACL drift. In this scenario: Assigning the Workspace Member role via a Microsoft Entra security group grants app-publishing, sharing, and OneLake-role administration while blocking workspace deletion and avoiding per-user role drift.
- **E:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: Assigning the Workspace Member role via a Microsoft Entra security group grants app-publishing, sharing, and OneLake-role administration while blocking workspace deletion and avoiding per-user role drift.

### Question 4 — D

Answer: Grant Build permission on the shared semantic model. Build permission on the shared semantic model enables live report authoring and Analyze in Excel without exposing workspace Contributor access or raw OneLake files. Build permission on a semantic model allows analysts to create new Power BI reports, use Analyze in Excel, and issue XMLA/DAX queries against the model without granting workspace Contributor rights or underlying Lakehouse access. Local study-map skill 1.2 (Implement Item-Level Access Controls (Read, ReadData, ReadAll, Build, SSO vs Fixed Identity)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Share items in Microsoft Fabric & Semantic model Build permission (https://learn.microsoft.com/en-us/fabric/fundamentals/share-items).

- **A:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: Build permission on the shared semantic model enables live report authoring and Analyze in Excel without exposing workspace Contributor access or raw OneLake files.
- **B:** Incorrect for this requirement. ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled. Why the keyed choice wins: Build permission on the shared semantic model enables live report authoring and Analyze in Excel without exposing workspace Contributor access or raw OneLake files.
- **C:** Incorrect for this requirement. ReadData grants SELECT across all tables/views in the SQL analytics endpoint or Warehouse without granting direct Spark/ABFS access to underlying Lakehouse files. Why the keyed choice wins: Build permission on the shared semantic model enables live report authoring and Analyze in Excel without exposing workspace Contributor access or raw OneLake files.
- **D:** Correct. Build permission on a semantic model allows analysts to create new Power BI reports, use Analyze in Excel, and issue XMLA/DAX queries against the model without granting workspace Contributor rights or underlying Lakehouse access. In this scenario: Build permission on the shared semantic model enables live report authoring and Analyze in Excel without exposing workspace Contributor access or raw OneLake files.

### Question 5 — D

Answer: Share the item with ReadData (Read all SQL endpoint data) permission. Sharing with `ReadData` (`Read all SQL endpoint data`) grants SQL analytics endpoint `SELECT` access without granting `ReadAll` Apache Spark/ABFS file permissions. ReadData grants SELECT across all tables/views in the SQL analytics endpoint or Warehouse without granting direct Spark/ABFS access to underlying Lakehouse files. Local study-map skill 1.2 (Implement Item-Level Access Controls (Read, ReadData, ReadAll, Build, SSO vs Fixed Identity)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Share items in Microsoft Fabric & Semantic model Build permission (https://learn.microsoft.com/en-us/fabric/fundamentals/share-items).

- **A:** Incorrect for this requirement. ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled. Why the keyed choice wins: Sharing with `ReadData` (`Read all SQL endpoint data`) grants SQL analytics endpoint `SELECT` access without granting `ReadAll` Apache Spark/ABFS file permissions.
- **B:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: Sharing with `ReadData` (`Read all SQL endpoint data`) grants SQL analytics endpoint `SELECT` access without granting `ReadAll` Apache Spark/ABFS file permissions.
- **C:** Incorrect for this requirement. Item-level Read metadata permission lets a user connect to a Lakehouse or Warehouse item container without granting broad OneLake file access; combine with SELECT or OneLake security roles for granular least-privilege access. Why the keyed choice wins: Sharing with `ReadData` (`Read all SQL endpoint data`) grants SQL analytics endpoint `SELECT` access without granting `ReadAll` Apache Spark/ABFS file permissions.
- **D:** Correct. ReadData grants SELECT across all tables/views in the SQL analytics endpoint or Warehouse without granting direct Spark/ABFS access to underlying Lakehouse files. In this scenario: Sharing with `ReadData` (`Read all SQL endpoint data`) grants SQL analytics endpoint `SELECT` access without granting `ReadAll` Apache Spark/ABFS file permissions.

### Question 6 — C

Answer: Enable OneLake security and define Read Grant roles → Assign consumers Workspace Viewer and OneLake security roles → Set SQL analytics endpoint to User's identity mode → Expose downstream shortcuts in User's identity mode. Enabling OneLake security Grant roles, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and exposing downstream shortcuts enforces policies across every engine. Correct order: enable OneLake security with Grant roles first, assign consumers to Viewer + security roles (never Contributor), set SQL analytics endpoints to User's identity mode, and expose shortcuts downstream. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. Incorrect: Contributors bypass OneLake security completely, OneLake security has no Deny role type, and Owner fixed identity bypasses per-user role evaluation on SQL queries. Why the keyed choice wins: Enabling OneLake security Grant roles, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and exposing downstream shortcuts enforces policies across every engine.
- **B:** Incorrect for this requirement. Incorrect: Members bypass OneLake security, ReadWrite roles cannot contain RLS/CLS rules, and OneLake shortcuts do not use On-premises gateways. Why the keyed choice wins: Enabling OneLake security Grant roles, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and exposing downstream shortcuts enforces policies across every engine.
- **C:** Correct. Correct order: enable OneLake security with Grant roles first, assign consumers to Viewer + security roles (never Contributor), set SQL analytics endpoints to User's identity mode, and expose shortcuts downstream. In this scenario: Enabling OneLake security Grant roles, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and exposing downstream shortcuts enforces policies across every engine.
- **D:** Incorrect for this requirement. Incorrect: mixing pre-existing SQL granular access with Delegated mode forces 100% DirectQuery fallback instead of clean OneLake security evaluation. Why the keyed choice wins: Enabling OneLake security Grant roles, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and exposing downstream shortcuts enforces policies across every engine.

### Question 7 — D, E

Answers: Create a OneLake security role scoped to the specific Files/<subfolder> path with Read permission; Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL. A folder-scoped Read OneLake security role restricts file access to `Files/pricing_extracts/`, and Tabular Editor Object-Level Security (`None`) removes `SupplierRebate` metadata completely from unauthorized semantic-model roles. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. OneLake security roles granting ReadWrite permission cannot contain RLS or CLS constraints; fine-grained row and column rules are supported only on Read roles. Why the keyed choice wins: A folder-scoped Read OneLake security role restricts file access to `Files/pricing_extracts/`, and Tabular Editor Object-Level Security (`None`) removes `SupplierRebate` metadata completely from unauthorized semantic-model roles.
- **B:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: A folder-scoped Read OneLake security role restricts file access to `Files/pricing_extracts/`, and Tabular Editor Object-Level Security (`None`) removes `SupplierRebate` metadata completely from unauthorized semantic-model roles.
- **C:** Incorrect for this requirement. OneLake security supports Grant roles only — there is no Deny role type, and OneLake security never restricts Workspace Admins, Members, or Contributors. Why the keyed choice wins: A folder-scoped Read OneLake security role restricts file access to `Files/pricing_extracts/`, and Tabular Editor Object-Level Security (`None`) removes `SupplierRebate` metadata completely from unauthorized semantic-model roles.
- **D:** Correct. OneLake folder-level security grants inherited Read (or ReadWrite) access to the selected subfolder and its descendants while allowing parent traversal without exposing sibling folders or Tables. In this scenario: A folder-scoped Read OneLake security role restricts file access to `Files/pricing_extracts/`, and Tabular Editor Object-Level Security (`None`) removes `SupplierRebate` metadata completely from unauthorized semantic-model roles.
- **E:** Correct. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. In this scenario: A folder-scoped Read OneLake security role restricts file access to `Files/pricing_extracts/`, and Tabular Editor Object-Level Security (`None`) removes `SupplierRebate` metadata completely from unauthorized semantic-model roles.

### Question 8 — B

Answer: Apply a Microsoft Purview sensitivity label with downstream inheritance on the source Lakehouse or Warehouse. Sensitivity label downstream inheritance in Microsoft Fabric automatically propagates Purview classifications from Warehouses and Lakehouses to newly created semantic models and reports. Sensitivity labels applied to Fabric Lakehouses, Warehouses, and Semantic Models automatically propagate downstream to newly connected semantic models, reports, and exported Excel/PDF/PPTX files when inheritance is enabled. Local study-map skill 1.4 (Apply Microsoft Purview Sensitivity Labels, Inheritance, Default/Mandatory Policies, and Export Encryption), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Information protection & sensitivity labels in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-overview).

- **A:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Sensitivity label downstream inheritance in Microsoft Fabric automatically propagates Purview classifications from Warehouses and Lakehouses to newly created semantic models and reports.
- **B:** Correct. Sensitivity labels applied to Fabric Lakehouses, Warehouses, and Semantic Models automatically propagate downstream to newly connected semantic models, reports, and exported Excel/PDF/PPTX files when inheritance is enabled. In this scenario: Sensitivity label downstream inheritance in Microsoft Fabric automatically propagates Purview classifications from Warehouses and Lakehouses to newly created semantic models and reports.
- **C:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Sensitivity label downstream inheritance in Microsoft Fabric automatically propagates Purview classifications from Warehouses and Lakehouses to newly created semantic models and reports.
- **D:** Incorrect for this requirement. Dynamic Data Masking obfuscates sensitive strings/emails/numbers in query results for users lacking UNMASK permission while keeping the column present so SELECT * queries do not fail. Why the keyed choice wins: Sensitivity label downstream inheritance in Microsoft Fabric automatically propagates Purview classifications from Warehouses and Lakehouses to newly created semantic models and reports.

### Question 9 — A

Answer: Use a Purview sensitivity label configured with file encryption so exported .pbix, Excel, PDF, and PowerPoint files stay protected outside Fabric. Configuring the applied Purview sensitivity label with file encryption protects exported Excel, PDF, PowerPoint, and `.pbix` files via Microsoft Purview Information Protection rights outside Fabric. While sensitivity labels in Fabric classify items in the workspace without encrypting OneLake Delta storage itself, encryption-enabled labels enforce rights management automatically when users export data to Excel, PDF, PowerPoint, or .pbix. Local study-map skill 1.4 (Apply Microsoft Purview Sensitivity Labels, Inheritance, Default/Mandatory Policies, and Export Encryption), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Information protection & sensitivity labels in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-overview).

- **A:** Correct. While sensitivity labels in Fabric classify items in the workspace without encrypting OneLake Delta storage itself, encryption-enabled labels enforce rights management automatically when users export data to Excel, PDF, PowerPoint, or .pbix. In this scenario: Configuring the applied Purview sensitivity label with file encryption protects exported Excel, PDF, PowerPoint, and `.pbix` files via Microsoft Purview Information Protection rights outside Fabric.
- **B:** Incorrect for this requirement. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Why the keyed choice wins: Configuring the applied Purview sensitivity label with file encryption protects exported Excel, PDF, PowerPoint, and `.pbix` files via Microsoft Purview Information Protection rights outside Fabric.
- **C:** Incorrect for this requirement. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Why the keyed choice wins: Configuring the applied Purview sensitivity label with file encryption protects exported Excel, PDF, PowerPoint, and `.pbix` files via Microsoft Purview Information Protection rights outside Fabric.
- **D:** Incorrect for this requirement. Item-level Read metadata permission lets a user connect to a Lakehouse or Warehouse item container without granting broad OneLake file access; combine with SELECT or OneLake security roles for granular least-privilege access. Why the keyed choice wins: Configuring the applied Purview sensitivity label with file encryption protects exported Excel, PDF, PowerPoint, and `.pbix` files via Microsoft Purview Information Protection rights outside Fabric.

### Question 10 — A

Answer: Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal. `Certified` endorsement can only be applied by reviewers explicitly authorized in the Fabric Admin portal, distinguishing vetted enterprise models from self-service `Promoted` items. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Local study-map skill 1.5 (Endorse Items Using Promoted, Certified, and Master Data Governance Badges), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Endorsement (Promoted, Certified, Master data) in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview).

- **A:** Correct. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. In this scenario: `Certified` endorsement can only be applied by reviewers explicitly authorized in the Fabric Admin portal, distinguishing vetted enterprise models from self-service `Promoted` items.
- **B:** Incorrect for this requirement. Mandatory and default sensitivity label policies in Microsoft Purview require content creators to classify unlabeled semantic models and reports on save and apply baseline classification automatically. Why the keyed choice wins: `Certified` endorsement can only be applied by reviewers explicitly authorized in the Fabric Admin portal, distinguishing vetted enterprise models from self-service `Promoted` items.
- **C:** Incorrect for this requirement. Build permission on a semantic model allows analysts to create new Power BI reports, use Analyze in Excel, and issue XMLA/DAX queries against the model without granting workspace Contributor rights or underlying Lakehouse access. Why the keyed choice wins: `Certified` endorsement can only be applied by reviewers explicitly authorized in the Fabric Admin portal, distinguishing vetted enterprise models from self-service `Promoted` items.
- **D:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: `Certified` endorsement can only be applied by reviewers explicitly authorized in the Fabric Admin portal, distinguishing vetted enterprise models from self-service `Promoted` items.

### Question 11 — D

Answer: Mark the item as Promoted in item settings. Any item owner or collaborator with write permissions can set `Promoted` endorsement in item settings without Fabric Admin reviewer delegation. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Local study-map skill 1.5 (Endorse Items Using Promoted, Certified, and Master Data Governance Badges), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Endorsement (Promoted, Certified, Master data) in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview).

- **A:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: Any item owner or collaborator with write permissions can set `Promoted` endorsement in item settings without Fabric Admin reviewer delegation.
- **B:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: Any item owner or collaborator with write permissions can set `Promoted` endorsement in item settings without Fabric Admin reviewer delegation.
- **C:** Incorrect for this requirement. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Why the keyed choice wins: Any item owner or collaborator with write permissions can set `Promoted` endorsement in item settings without Fabric Admin reviewer delegation.
- **D:** Correct. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. In this scenario: Any item owner or collaborator with write permissions can set `Promoted` endorsement in item settings without Fabric Admin reviewer delegation.

### Question 12 — A

Answer: Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch. Using `Branch out` in Source control provisions an isolated developer workspace bound to a dedicated feature branch until changes merge back to `main` via pull request. In Fabric Git integration, workspaces map 1-to-1 to branches; branching out into a dedicated developer workspace isolates in-progress notebook, pipeline, and semantic model edits before merging via pull request. Local study-map skill 1.6 (Configure Workspace Version Control with Azure DevOps or GitHub (Branch Out, Commit, Update, Undo)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to Git integration in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration).

- **A:** Correct. In Fabric Git integration, workspaces map 1-to-1 to branches; branching out into a dedicated developer workspace isolates in-progress notebook, pipeline, and semantic model edits before merging via pull request. In this scenario: Using `Branch out` in Source control provisions an isolated developer workspace bound to a dedicated feature branch until changes merge back to `main` via pull request.
- **B:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Using `Branch out` in Source control provisions an isolated developer workspace bound to a dedicated feature branch until changes merge back to `main` via pull request.
- **C:** Incorrect for this requirement. Undo reverts uncommitted workspace item modifications to match the connected Git branch HEAD without rewriting shared remote commit history. Why the keyed choice wins: Using `Branch out` in Source control provisions an isolated developer workspace bound to a dedicated feature branch until changes merge back to `main` via pull request.
- **D:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Using `Branch out` in Source control provisions an isolated developer workspace bound to a dedicated feature branch until changes merge back to `main` via pull request.

### Question 13 — A

Answer: Connect shared Dev workspace to main → Branch out to an isolated developer workspace and commit .pbip/Notebook edits → Merge pull request into main in Git → Run Update all in Dev and promote via Deployment Pipeline. Branching out from `main`, committing `.pbip` changes, merging via PR, running `Update all` in `Dev`, and promoting through the Deployment Pipeline keeps Git and workspace stages synchronized. Correct order: link Dev to main, branch out to an isolated workspace for feature work, validate and merge via Git PR into main, run Update all in Dev, and promote via Deployment Pipeline with stage rules. Local study-map skill 1.6 (Configure Workspace Version Control with Azure DevOps or GitHub (Branch Out, Commit, Update, Undo)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to Git integration in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration).

- **A:** Correct. Correct order: link Dev to main, branch out to an isolated workspace for feature work, validate and merge via Git PR into main, run Update all in Dev, and promote via Deployment Pipeline with stage rules. In this scenario: Branching out from `main`, committing `.pbip` changes, merging via PR, running `Update all` in `Dev`, and promoting through the Deployment Pipeline keeps Git and workspace stages synchronized.
- **B:** Incorrect for this requirement. Incorrect: editing Production directly on feature branches and committing cache.abf violates ALM isolation, leaks cached data, and bypasses Test validation. Why the keyed choice wins: Branching out from `main`, committing `.pbip` changes, merging via PR, running `Update all` in `Dev`, and promoting through the Deployment Pipeline keeps Git and workspace stages synchronized.
- **C:** Incorrect for this requirement. Incorrect: My Workspace does not support full team Git ALM, Undo discards local changes rather than committing, and deleting .platform breaks item lineage. Why the keyed choice wins: Branching out from `main`, committing `.pbip` changes, merging via PR, running `Update all` in `Dev`, and promoting through the Deployment Pipeline keeps Git and workspace stages synchronized.
- **D:** Incorrect for this requirement. Incorrect: Fabric workspaces do not auto-pull remote PR merges — skipping Update from Git promotes stale pre-PR workspace state to Test. Why the keyed choice wins: Branching out from `main`, committing `.pbip` changes, merging via PR, running `Update all` in `Dev`, and promoting through the Deployment Pipeline keeps Git and workspace stages synchronized.

### Question 14 — C, D

Answers: Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions; Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository. `.pbip` projects serialize model metadata as TMDL and report definitions as PBIR JSON, while `.gitignore` excludes `**/cache.abf` and `**/localSettings.json` so cached data never enters Git. Local study-map skill 1.7 (Create and Manage Power BI Desktop Projects (.pbip) with TMDL, PBIR, and .gitignore Hygiene), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Power BI Desktop projects (.pbip), TMDL, and PBIR (https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `.pbip` projects serialize model metadata as TMDL and report definitions as PBIR JSON, while `.gitignore` excludes `**/cache.abf` and `**/localSettings.json` so cached data never enters Git.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: `.pbip` projects serialize model metadata as TMDL and report definitions as PBIR JSON, while `.gitignore` excludes `**/cache.abf` and `**/localSettings.json` so cached data never enters Git.
- **C:** Correct. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. In this scenario: `.pbip` projects serialize model metadata as TMDL and report definitions as PBIR JSON, while `.gitignore` excludes `**/cache.abf` and `**/localSettings.json` so cached data never enters Git.
- **D:** Correct. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. In this scenario: `.pbip` projects serialize model metadata as TMDL and report definitions as PBIR JSON, while `.gitignore` excludes `**/cache.abf` and `**/localSettings.json` so cached data never enters Git.
- **E:** Incorrect for this requirement. In Power BI Desktop USERNAME() returns DOMAIN\user whereas in the Fabric service it returns the UPN; USERPRINCIPALNAME() consistently returns user@domain.com across cloud evaluations. Why the keyed choice wins: `.pbip` projects serialize model metadata as TMDL and report definitions as PBIR JSON, while `.gitignore` excludes `**/cache.abf` and `**/localSettings.json` so cached data never enters Git.

### Question 15 — C

Answer: Configure Deployment pipeline data source and parameter rules on the Test and Production stages. Configuring Deployment Pipeline data source rules (or parameter rules) on the `Prod` stage rebinds the deployed semantic model cleanly without editing Production manually. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. Undo reverts uncommitted workspace item modifications to match the connected Git branch HEAD without rewriting shared remote commit history. Why the keyed choice wins: Configuring Deployment Pipeline data source rules (or parameter rules) on the `Prod` stage rebinds the deployed semantic model cleanly without editing Production manually.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Configuring Deployment Pipeline data source rules (or parameter rules) on the `Prod` stage rebinds the deployed semantic model cleanly without editing Production manually.
- **C:** Correct. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. In this scenario: Configuring Deployment Pipeline data source rules (or parameter rules) on the `Prod` stage rebinds the deployed semantic model cleanly without editing Production manually.
- **D:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Configuring Deployment Pipeline data source rules (or parameter rules) on the `Prod` stage rebinds the deployed semantic model cleanly without editing Production manually.

### Question 16 — D

Answer: Use a Fabric Variable library (or autobinding across paired workspace items) to parameterize stage-specific environment references. A Fabric Variable library defines stage-scoped environment values across Dev, Test, and Prod workspaces consumed dynamically by pipelines and workspace items. Fabric Variable libraries store stage-specific workspace/lakehouse IDs, URLs, and thresholds across Dev/Test/Prod — essential for items like Data Pipelines and Direct Lake on OneLake models that do not use legacy SQL deployment rules. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: A Fabric Variable library defines stage-scoped environment values across Dev, Test, and Prod workspaces consumed dynamically by pipelines and workspace items.
- **B:** Incorrect for this requirement. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Why the keyed choice wins: A Fabric Variable library defines stage-scoped environment values across Dev, Test, and Prod workspaces consumed dynamically by pipelines and workspace items.
- **C:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: A Fabric Variable library defines stage-scoped environment values across Dev, Test, and Prod workspaces consumed dynamically by pipelines and workspace items.
- **D:** Correct. Fabric Variable libraries store stage-specific workspace/lakehouse IDs, URLs, and thresholds across Dev/Test/Prod — essential for items like Data Pipelines and Direct Lake on OneLake models that do not use legacy SQL deployment rules. In this scenario: A Fabric Variable library defines stage-scoped environment values across Dev, Test, and Prod workspaces consumed dynamically by pipelines and workspace items.

### Question 17 — B

Answer: Perform a selective deployment selecting the modified item together with Select related to include required upstream dependencies. Selecting the modified report and choosing `Select related` performs a selective deployment that includes only required upstream dependencies. Selective deployment in Fabric Deployment Pipelines promotes only chosen items between stages, and Select related ensures newly referenced lakehouses or semantic models deploy alongside dependent reports. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Selecting the modified report and choosing `Select related` performs a selective deployment that includes only required upstream dependencies.
- **B:** Correct. Selective deployment in Fabric Deployment Pipelines promotes only chosen items between stages, and Select related ensures newly referenced lakehouses or semantic models deploy alongside dependent reports. In this scenario: Selecting the modified report and choosing `Select related` performs a selective deployment that includes only required upstream dependencies.
- **C:** Incorrect for this requirement. In Fabric Git integration, workspaces map 1-to-1 to branches; branching out into a dedicated developer workspace isolates in-progress notebook, pipeline, and semantic model edits before merging via pull request. Why the keyed choice wins: Selecting the modified report and choosing `Select related` performs a selective deployment that includes only required upstream dependencies.
- **D:** Incorrect for this requirement. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. Why the keyed choice wins: Selecting the modified report and choosing `Select related` performs a selective deployment that includes only required upstream dependencies.

### Question 18 — B

Answer: Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts. Switching to Workspace `Lineage` view, opening the `Impact analysis` pane on the Lakehouse, and using `Notify contacts` identifies cross-workspace dependents and alerts their owners. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Local study-map skill 1.9 (Perform Downstream Dependency Impact Analysis Across Lakehouses, Warehouses, Dataflows, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Lineage and impact analysis in Microsoft Fabric workspaces (https://learn.microsoft.com/en-us/fabric/governance/lineage).

- **A:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: Switching to Workspace `Lineage` view, opening the `Impact analysis` pane on the Lakehouse, and using `Notify contacts` identifies cross-workspace dependents and alerts their owners.
- **B:** Correct. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. In this scenario: Switching to Workspace `Lineage` view, opening the `Impact analysis` pane on the Lakehouse, and using `Notify contacts` identifies cross-workspace dependents and alerts their owners.
- **C:** Incorrect for this requirement. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. Why the keyed choice wins: Switching to Workspace `Lineage` view, opening the `Impact analysis` pane on the Lakehouse, and using `Notify contacts` identifies cross-workspace dependents and alerts their owners.
- **D:** Incorrect for this requirement. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Why the keyed choice wins: Switching to Workspace `Lineage` view, opening the `Impact analysis` pane on the Lakehouse, and using `Notify contacts` identifies cross-workspace dependents and alerts their owners.

### Question 19 — B

Answer: Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts. Workspace list view shows only items inside the current workspace; opening Lineage view and Downstream Impact Analysis reveals dependent items across all tenant workspaces. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Local study-map skill 1.9 (Perform Downstream Dependency Impact Analysis Across Lakehouses, Warehouses, Dataflows, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Lineage and impact analysis in Microsoft Fabric workspaces (https://learn.microsoft.com/en-us/fabric/governance/lineage).

- **A:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Workspace list view shows only items inside the current workspace; opening Lineage view and Downstream Impact Analysis reveals dependent items across all tenant workspaces.
- **B:** Correct. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. In this scenario: Workspace list view shows only items inside the current workspace; opening Lineage view and Downstream Impact Analysis reveals dependent items across all tenant workspaces.
- **C:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: Workspace list view shows only items inside the current workspace; opening Lineage view and Downstream Impact Analysis reveals dependent items across all tenant workspaces.
- **D:** Incorrect for this requirement. Fabric admins can enable Master data endorsement for authoritative single-source-of-truth silver/gold data assets so analysts distinguish core reference items in the OneLake catalog. Why the keyed choice wins: Workspace list view shows only items inside the current workspace; opening Lineage view and Downstream Impact Analysis reveals dependent items across all tenant workspaces.

### Question 20 — C

Answer: Verify XMLA Endpoint = Read Write on target capacity → Connect ALM Toolkit to Dev source and Prod XMLA target → Compare schemas while hiding unchanged partitions and keeping Prod data sources → Validate and deploy metadata-only TMSL changes. Enabling `Read Write` XMLA on the capacity and deploying a metadata-only diff with ALM Toolkit while retaining Production partitions and data sources avoids reprocessing outages. Correct order: confirm Read Write XMLA capacity setting, compare Dev vs Prod models, preserve Prod partition state and data-source bindings, and push metadata-only measure/relationship diffs. Local study-map skill 1.10 (Deploy and Manage Semantic Models Using the XMLA Endpoint (Read-Write, TMSL, Tabular Editor, ALM Toolkit)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model connectivity and management with the XMLA endpoint (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools).

- **A:** Incorrect for this requirement. Incorrect: Read Only XMLA rejects TMSL model deployments, and Capacity Admin rights violate least privilege. Why the keyed choice wins: Enabling `Read Write` XMLA on the capacity and deploying a metadata-only diff with ALM Toolkit while retaining Production partitions and data sources avoids reprocessing outages.
- **B:** Incorrect for this requirement. Incorrect: XMLA Off blocks external deployment, and overwriting Production with an unpartitioned file destroys incremental partitions and causes prolonged outage. Why the keyed choice wins: Enabling `Read Write` XMLA on the capacity and deploying a metadata-only diff with ALM Toolkit while retaining Production partitions and data sources avoids reprocessing outages.
- **C:** Correct. Correct order: confirm Read Write XMLA capacity setting, compare Dev vs Prod models, preserve Prod partition state and data-source bindings, and push metadata-only measure/relationship diffs. In this scenario: Enabling `Read Write` XMLA on the capacity and deploying a metadata-only diff with ALM Toolkit while retaining Production partitions and data sources avoids reprocessing outages.
- **D:** Incorrect for this requirement. Incorrect: DAX Studio is a query/profiling tool (not a model-deployment tool), and unversioned Production hotfixes cause immediate drift on next deployment. Why the keyed choice wins: Enabling `Read Write` XMLA on the capacity and deploying a metadata-only diff with ALM Toolkit while retaining Production partitions and data sources avoids reprocessing outages.

### Question 21 — B, C

Answers: Enable XMLA Endpoint = Read Write in Fabric Capacity workload settings and connect to powerbi://api.powerbi.com/v1.0/myorg/<WorkspaceName>; Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition. The Fabric capacity must enable `XMLA Endpoint = Read Write`, and executing a granular TMSL / Enhanced Refresh `dataOnly` command refreshes only the targeted partition over XMLA. Local study-map skill 1.10 (Deploy and Manage Semantic Models Using the XMLA Endpoint (Read-Write, TMSL, Tabular Editor, ALM Toolkit)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model connectivity and management with the XMLA endpoint (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools).

- **A:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: The Fabric capacity must enable `XMLA Endpoint = Read Write`, and executing a granular TMSL / Enhanced Refresh `dataOnly` command refreshes only the targeted partition over XMLA.
- **B:** Correct. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. In this scenario: The Fabric capacity must enable `XMLA Endpoint = Read Write`, and executing a granular TMSL / Enhanced Refresh `dataOnly` command refreshes only the targeted partition over XMLA.
- **C:** Correct. External ALM tools (Tabular Editor, SSMS, ALM Toolkit, SqlPackage/PowerShell Invoke-ASCmd) require workspace Fabric/Premium capacity with XMLA Endpoint set to Read Write to deploy or modify semantic models. In this scenario: The Fabric capacity must enable `XMLA Endpoint = Read Write`, and executing a granular TMSL / Enhanced Refresh `dataOnly` command refreshes only the targeted partition over XMLA.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: The Fabric capacity must enable `XMLA Endpoint = Read Write`, and executing a granular TMSL / Enhanced Refresh `dataOnly` command refreshes only the targeted partition over XMLA.
- **E:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: The Fabric capacity must enable `XMLA Endpoint = Read Write`, and executing a granular TMSL / Enhanced Refresh `dataOnly` command refreshes only the targeted partition over XMLA.

### Question 22 — A

Answer: Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode. A Power BI Data Source (`.pbids`) file preconfigures the connector type, server address, and database target while containing neither visuals nor data rows. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Local study-map skill 1.11 (Create and Update Reusable Assets (.pbit Templates, .pbids Data Sources, and Shared Golden Semantic Models)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create and use report templates (.pbit), data sources (.pbids), and shared semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-templates).

- **A:** Correct. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. In this scenario: A Power BI Data Source (`.pbids`) file preconfigures the connector type, server address, and database target while containing neither visuals nor data rows.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: A Power BI Data Source (`.pbids`) file preconfigures the connector type, server address, and database target while containing neither visuals nor data rows.
- **C:** Incorrect for this requirement. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. Why the keyed choice wins: A Power BI Data Source (`.pbids`) file preconfigures the connector type, server address, and database target while containing neither visuals nor data rows.
- **D:** Incorrect for this requirement. Decoupling a shared golden semantic model from thin live-connected reports prevents measure duplication, reduces capacity memory footprint, and enforces centralized RLS/endorsement across teams. Why the keyed choice wins: A Power BI Data Source (`.pbids`) file preconfigures the connector type, server address, and database target while containing neither visuals nor data rows.

### Question 23 — D

Answer: Publish a single certified core semantic model in a data workspace and build thin live-connected Power BI reports in departmental workspaces. Publishing one certified shared semantic model in a core workspace and connecting thin live Power BI reports from regional workspaces centralizes DAX logic and refreshes once. Decoupling a shared golden semantic model from thin live-connected reports prevents measure duplication, reduces capacity memory footprint, and enforces centralized RLS/endorsement across teams. Local study-map skill 1.11 (Create and Update Reusable Assets (.pbit Templates, .pbids Data Sources, and Shared Golden Semantic Models)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create and use report templates (.pbit), data sources (.pbids), and shared semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-templates).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Publishing one certified shared semantic model in a core workspace and connecting thin live Power BI reports from regional workspaces centralizes DAX logic and refreshes once.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Publishing one certified shared semantic model in a core workspace and connecting thin live Power BI reports from regional workspaces centralizes DAX logic and refreshes once.
- **C:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: Publishing one certified shared semantic model in a core workspace and connecting thin live Power BI reports from regional workspaces centralizes DAX logic and refreshes once.
- **D:** Correct. Decoupling a shared golden semantic model from thin live-connected reports prevents measure duplication, reduces capacity memory footprint, and enforces centralized RLS/endorsement across teams. In this scenario: Publishing one certified shared semantic model in a core workspace and connecting thin live Power BI reports from regional workspaces centralizes DAX logic and refreshes once.

### Question 24 — B

Answer: Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet. A Microsoft Fabric Virtual Network (VNet) data gateway injects managed gateway containers into a delegated subnet of `vnet-retail-prod` to reach private-endpoint Azure data sources. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. Local study-map skill 2.1 (Create Data Connections (Shareable Cloud Connections, On-Premises Gateways, and VNet Data Gateways)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data source management, cloud connections, and VNet/on-premises gateways in Fabric (https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management).

- **A:** Incorrect for this requirement. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. Why the keyed choice wins: A Microsoft Fabric Virtual Network (VNet) data gateway injects managed gateway containers into a delegated subnet of `vnet-retail-prod` to reach private-endpoint Azure data sources.
- **B:** Correct. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. In this scenario: A Microsoft Fabric Virtual Network (VNet) data gateway injects managed gateway containers into a delegated subnet of `vnet-retail-prod` to reach private-endpoint Azure data sources.
- **C:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: A Microsoft Fabric Virtual Network (VNet) data gateway injects managed gateway containers into a delegated subnet of `vnet-retail-prod` to reach private-endpoint Azure data sources.
- **D:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: A Microsoft Fabric Virtual Network (VNet) data gateway injects managed gateway containers into a delegated subnet of `vnet-retail-prod` to reach private-endpoint Azure data sources.

### Question 25 — C

Answer: Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication. Creating a Shareable cloud connection in `Manage connections and gateways` authenticated via Service Principal and sharing `Use` access lets pipeline authors reuse credentials securely. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. Local study-map skill 2.1 (Create Data Connections (Shareable Cloud Connections, On-Premises Gateways, and VNet Data Gateways)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data source management, cloud connections, and VNet/on-premises gateways in Fabric (https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management).

- **A:** Incorrect for this requirement. With SSO enabled on a Direct Lake model, Fabric evaluates data permissions at the underlying SQL analytics endpoint or OneLake security layer using each viewing report consumer's own Microsoft Entra identity. Why the keyed choice wins: Creating a Shareable cloud connection in `Manage connections and gateways` authenticated via Service Principal and sharing `Use` access lets pipeline authors reuse credentials securely.
- **B:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Creating a Shareable cloud connection in `Manage connections and gateways` authenticated via Service Principal and sharing `Use` access lets pipeline authors reuse credentials securely.
- **C:** Correct. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. In this scenario: Creating a Shareable cloud connection in `Manage connections and gateways` authenticated via Service Principal and sharing `Use` access lets pipeline authors reuse credentials securely.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Creating a Shareable cloud connection in `Manage connections and gateways` authenticated via Service Principal and sharing `Use` access lets pipeline authors reuse credentials securely.

### Question 26 — B

Answer: Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture. OneLake catalog provides the `Explore` tab for cross-tenant asset discovery and the `Govern` tab for stewardship posture insights and governance actions. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Local study-map skill 2.2 (Discover Data and Streams Using OneLake Catalog (Explore/Govern) and Real-Time Hub + Activator), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake catalog overview & Real-Time hub in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview).

- **A:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: OneLake catalog provides the `Explore` tab for cross-tenant asset discovery and the `Govern` tab for stewardship posture insights and governance actions.
- **B:** Correct. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. In this scenario: OneLake catalog provides the `Explore` tab for cross-tenant asset discovery and the `Govern` tab for stewardship posture insights and governance actions.
- **C:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: OneLake catalog provides the `Explore` tab for cross-tenant asset discovery and the `Govern` tab for stewardship posture insights and governance actions.
- **D:** Incorrect for this requirement. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Why the keyed choice wins: OneLake catalog provides the `Explore` tab for cross-tenant asset discovery and the `Govern` tab for stewardship posture insights and governance actions.

### Question 27 — B, E

Answers: Use the Real-Time hub to subscribe to Microsoft.Fabric.OneLake.FileCreated events (or Capacity/CDC streams) and trigger an Activator rule; Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table. Real-Time hub centralizes stream and `OneLake.FileCreated` discovery with Activator alerting, while Eventstream ingests and routes live event streams without code. Local study-map skill 2.2 (Discover Data and Streams Using OneLake Catalog (Explore/Govern) and Real-Time Hub + Activator), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake catalog overview & Real-Time hub in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview).

- **A:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Real-Time hub centralizes stream and `OneLake.FileCreated` discovery with Activator alerting, while Eventstream ingests and routes live event streams without code.
- **B:** Correct. Real-Time hub unifies streaming sources, CDC feeds, Azure Blob events, and Fabric workspace/OneLake/Capacity events so analytics engineers can discover streams in one catalog and trigger event-driven pipelines or Notebooks via Activator. In this scenario: Real-Time hub centralizes stream and `OneLake.FileCreated` discovery with Activator alerting, while Eventstream ingests and routes live event streams without code.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Real-Time hub centralizes stream and `OneLake.FileCreated` discovery with Activator alerting, while Eventstream ingests and routes live event streams without code.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Real-Time hub centralizes stream and `OneLake.FileCreated` discovery with Activator alerting, while Eventstream ingests and routes live event streams without code.
- **E:** Correct. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. In this scenario: Real-Time hub centralizes stream and `OneLake.FileCreated` discovery with Activator alerting, while Eventstream ingests and routes live event streams without code.

### Question 28 — A

Answer: Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching. An external OneLake shortcut to Amazon S3 (with optional shortcut caching) virtualizes the remote Delta tables directly under the Lakehouse `Tables` namespace with zero file duplication. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Correct. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. In this scenario: An external OneLake shortcut to Amazon S3 (with optional shortcut caching) virtualizes the remote Delta tables directly under the Lakehouse `Tables` namespace with zero file duplication.
- **B:** Incorrect for this requirement. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. Why the keyed choice wins: An external OneLake shortcut to Amazon S3 (with optional shortcut caching) virtualizes the remote Delta tables directly under the Lakehouse `Tables` namespace with zero file duplication.
- **C:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: An external OneLake shortcut to Amazon S3 (with optional shortcut caching) virtualizes the remote Delta tables directly under the Lakehouse `Tables` namespace with zero file duplication.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: An external OneLake shortcut to Amazon S3 (with optional shortcut caching) virtualizes the remote Delta tables directly under the Lakehouse `Tables` namespace with zero file duplication.

### Question 29 — C

Answer: Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog. Hourly full reloads burn massive RUs and Fabric CUs; configuring Fabric Database Mirroring for Azure Cosmos DB continuously syncs CDC changes into OneLake Delta tables automatically. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Hourly full reloads burn massive RUs and Fabric CUs; configuring Fabric Database Mirroring for Azure Cosmos DB continuously syncs CDC changes into OneLake Delta tables automatically.
- **B:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: Hourly full reloads burn massive RUs and Fabric CUs; configuring Fabric Database Mirroring for Azure Cosmos DB continuously syncs CDC changes into OneLake Delta tables automatically.
- **C:** Correct. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. In this scenario: Hourly full reloads burn massive RUs and Fabric CUs; configuring Fabric Database Mirroring for Azure Cosmos DB continuously syncs CDC changes into OneLake Delta tables automatically.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Hourly full reloads burn massive RUs and Fabric CUs; configuring Fabric Database Mirroring for Azure Cosmos DB continuously syncs CDC changes into OneLake Delta tables automatically.

### Question 30 — B

Answer: Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake. A Data Factory Pipeline `Copy activity` moves bulk binary/tabular files at maximum throughput and lowest CU cost when row-level Power Query transformations are unnecessary. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` moves bulk binary/tabular files at maximum throughput and lowest CU cost when row-level Power Query transformations are unnecessary.
- **B:** Correct. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. In this scenario: A Data Factory Pipeline `Copy activity` moves bulk binary/tabular files at maximum throughput and lowest CU cost when row-level Power Query transformations are unnecessary.
- **C:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` moves bulk binary/tabular files at maximum throughput and lowest CU cost when row-level Power Query transformations are unnecessary.
- **D:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` moves bulk binary/tabular files at maximum throughput and lowest CU cost when row-level Power Query transformations are unnecessary.

### Question 31 — A, D, F

Answers: Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching; Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog; Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations. External OneLake shortcuts virtualize ADLS Gen2, Database Mirroring replicates Snowflake CDC into OneLake, and Dataflow Gen2 with Fast Copy handles low-code SaaS transformations. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Correct. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. In this scenario: External OneLake shortcuts virtualize ADLS Gen2, Database Mirroring replicates Snowflake CDC into OneLake, and Dataflow Gen2 with Fast Copy handles low-code SaaS transformations.
- **B:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: External OneLake shortcuts virtualize ADLS Gen2, Database Mirroring replicates Snowflake CDC into OneLake, and Dataflow Gen2 with Fast Copy handles low-code SaaS transformations.
- **C:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: External OneLake shortcuts virtualize ADLS Gen2, Database Mirroring replicates Snowflake CDC into OneLake, and Dataflow Gen2 with Fast Copy handles low-code SaaS transformations.
- **D:** Correct. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. In this scenario: External OneLake shortcuts virtualize ADLS Gen2, Database Mirroring replicates Snowflake CDC into OneLake, and Dataflow Gen2 with Fast Copy handles low-code SaaS transformations.
- **E:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: External OneLake shortcuts virtualize ADLS Gen2, Database Mirroring replicates Snowflake CDC into OneLake, and Dataflow Gen2 with Fast Copy handles low-code SaaS transformations.
- **F:** Correct. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. In this scenario: External OneLake shortcuts virtualize ADLS Gen2, Database Mirroring replicates Snowflake CDC into OneLake, and Dataflow Gen2 with Fast Copy handles low-code SaaS transformations.

### Question 32 — A

Answer: Choose a Fabric Data Warehouse. Fabric Data Warehouse delivers a full transactional T-SQL engine with multi-table ACID DDL/DML writes and native SQL security backed by OneLake Delta Parquet. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Correct. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. In this scenario: Fabric Data Warehouse delivers a full transactional T-SQL engine with multi-table ACID DDL/DML writes and native SQL security backed by OneLake Delta Parquet.
- **B:** Incorrect for this requirement. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. Why the keyed choice wins: Fabric Data Warehouse delivers a full transactional T-SQL engine with multi-table ACID DDL/DML writes and native SQL security backed by OneLake Delta Parquet.
- **C:** Incorrect for this requirement. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. Why the keyed choice wins: Fabric Data Warehouse delivers a full transactional T-SQL engine with multi-table ACID DDL/DML writes and native SQL security backed by OneLake Delta Parquet.
- **D:** Incorrect for this requirement. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Why the keyed choice wins: Fabric Data Warehouse delivers a full transactional T-SQL engine with multi-table ACID DDL/DML writes and native SQL security backed by OneLake Delta Parquet.

### Question 33 — A

Answer: Choose a Fabric Lakehouse. A Fabric Lakehouse provides unified OneLake `Files` folders for unstructured assets and managed Delta `Tables` engineered via Spark with an automatic SQL analytics endpoint. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Correct. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. In this scenario: A Fabric Lakehouse provides unified OneLake `Files` folders for unstructured assets and managed Delta `Tables` engineered via Spark with an automatic SQL analytics endpoint.
- **B:** Incorrect for this requirement. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. Why the keyed choice wins: A Fabric Lakehouse provides unified OneLake `Files` folders for unstructured assets and managed Delta `Tables` engineered via Spark with an automatic SQL analytics endpoint.
- **C:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: A Fabric Lakehouse provides unified OneLake `Files` folders for unstructured assets and managed Delta `Tables` engineered via Spark with an automatic SQL analytics endpoint.
- **D:** Incorrect for this requirement. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. Why the keyed choice wins: A Fabric Lakehouse provides unified OneLake `Files` folders for unstructured assets and managed Delta `Tables` engineered via Spark with an automatic SQL analytics endpoint.

### Question 34 — D, E

Answers: Choose a Fabric Eventhouse (KQL database); Choose a SQL database in Microsoft Fabric. Eventhouse (KQL database) handles high-granularity streaming RFID time-series telemetry, while SQL database in Fabric serves transactional OLTP workloads with automatic OneLake mirroring. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Eventhouse (KQL database) handles high-granularity streaming RFID time-series telemetry, while SQL database in Fabric serves transactional OLTP workloads with automatic OneLake mirroring.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Eventhouse (KQL database) handles high-granularity streaming RFID time-series telemetry, while SQL database in Fabric serves transactional OLTP workloads with automatic OneLake mirroring.
- **C:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Eventhouse (KQL database) handles high-granularity streaming RFID time-series telemetry, while SQL database in Fabric serves transactional OLTP workloads with automatic OneLake mirroring.
- **D:** Correct. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. In this scenario: Eventhouse (KQL database) handles high-granularity streaming RFID time-series telemetry, while SQL database in Fabric serves transactional OLTP workloads with automatic OneLake mirroring.
- **E:** Correct. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. In this scenario: Eventhouse (KQL database) handles high-granularity streaming RFID time-series telemetry, while SQL database in Fabric serves transactional OLTP workloads with automatic OneLake mirroring.

### Question 35 — A

Answer: Enable OneLake integration in the Import semantic model settings so imported model tables export as Delta tables to OneLake. Enabling `OneLake integration` in the Import semantic model settings exports Delta Parquet representations of the model's imported tables into OneLake. OneLake integration for Import semantic models writes Delta Parquet artifacts of the model's imported tables into OneLake, allowing Lakehouse shortcuts and Spark/SQL users to reuse curated Power Query model outputs. Local study-map skill 2.5 (Implement OneLake Integration for Eventhouse (OneLake Availability) and Import Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Eventhouse OneLake availability & OneLake integration for semantic models (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/one-lake-availability).

- **A:** Correct. OneLake integration for Import semantic models writes Delta Parquet artifacts of the model's imported tables into OneLake, allowing Lakehouse shortcuts and Spark/SQL users to reuse curated Power Query model outputs. In this scenario: Enabling `OneLake integration` in the Import semantic model settings exports Delta Parquet representations of the model's imported tables into OneLake.
- **B:** Incorrect for this requirement. Eventhouse KQL databases do not write Delta Parquet to OneLake unless OneLake availability is enabled, and Direct Lake on SQL does not support KQL databases (only Direct Lake on OneLake does once OneLake availability is on). Why the keyed choice wins: Enabling `OneLake integration` in the Import semantic model settings exports Delta Parquet representations of the model's imported tables into OneLake.
- **C:** Incorrect for this requirement. ALM Toolkit performs metadata-only diffs and incremental TMSL deployments over XMLA, preserving existing processed historical partitions and incremental refresh windows in Production. Why the keyed choice wins: Enabling `OneLake integration` in the Import semantic model settings exports Delta Parquet representations of the model's imported tables into OneLake.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Enabling `OneLake integration` in the Import semantic model settings exports Delta Parquet representations of the model's imported tables into OneLake.

### Question 36 — D

Answer: Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic. Parameterized T-SQL DML stored procedures (`CREATE PROCEDURE` executing `INSERT`/`UPDATE`/`MERGE`) are supported in a Fabric Data Warehouse, whereas Lakehouse SQL analytics endpoints are read-only for DML. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Parameterized T-SQL DML stored procedures (`CREATE PROCEDURE` executing `INSERT`/`UPDATE`/`MERGE`) are supported in a Fabric Data Warehouse, whereas Lakehouse SQL analytics endpoints are read-only for DML.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Parameterized T-SQL DML stored procedures (`CREATE PROCEDURE` executing `INSERT`/`UPDATE`/`MERGE`) are supported in a Fabric Data Warehouse, whereas Lakehouse SQL analytics endpoints are read-only for DML.
- **C:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Parameterized T-SQL DML stored procedures (`CREATE PROCEDURE` executing `INSERT`/`UPDATE`/`MERGE`) are supported in a Fabric Data Warehouse, whereas Lakehouse SQL analytics endpoints are read-only for DML.
- **D:** Correct. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. In this scenario: Parameterized T-SQL DML stored procedures (`CREATE PROCEDURE` executing `INSERT`/`UPDATE`/`MERGE`) are supported in a Fabric Data Warehouse, whereas Lakehouse SQL analytics endpoints are read-only for DML.

### Question 37 — D

Answer: Use a Lakehouse Materialized Lake View (or persisted Gold Delta table) instead of a non-materialized SQL analytics endpoint view for Direct Lake on OneLake. Non-materialized SQL views are unsupported in Direct Lake on OneLake and force DirectQuery fallback on Direct Lake on SQL; persisting a Materialized Lake View or Gold Delta table preserves pure Direct Lake performance. Non-materialized SQL analytics endpoint views cannot back Direct Lake on OneLake tables and force Direct Lake on SQL into DirectQuery fallback; materializing the view as a Delta table preserves pure in-memory Direct Lake speed. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: Non-materialized SQL views are unsupported in Direct Lake on OneLake and force DirectQuery fallback on Direct Lake on SQL; persisting a Materialized Lake View or Gold Delta table preserves pure Direct Lake performance.
- **B:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Non-materialized SQL views are unsupported in Direct Lake on OneLake and force DirectQuery fallback on Direct Lake on SQL; persisting a Materialized Lake View or Gold Delta table preserves pure Direct Lake performance.
- **C:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Non-materialized SQL views are unsupported in Direct Lake on OneLake and force DirectQuery fallback on Direct Lake on SQL; persisting a Materialized Lake View or Gold Delta table preserves pure Direct Lake performance.
- **D:** Correct. Non-materialized SQL analytics endpoint views cannot back Direct Lake on OneLake tables and force Direct Lake on SQL into DirectQuery fallback; materializing the view as a Delta table preserves pure in-memory Direct Lake speed. In this scenario: Non-materialized SQL views are unsupported in Direct Lake on OneLake and force DirectQuery fallback on Direct Lake on SQL; persisting a Materialized Lake View or Gold Delta table preserves pure Direct Lake performance.

### Question 38 — C

Answer: Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic. Inline TVFs inline directly into the distributed T-SQL query optimizer plan across Warehouse compute nodes without row-by-row procedural execution bottlenecks. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Inline TVFs inline directly into the distributed T-SQL query optimizer plan across Warehouse compute nodes without row-by-row procedural execution bottlenecks.
- **B:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Inline TVFs inline directly into the distributed T-SQL query optimizer plan across Warehouse compute nodes without row-by-row procedural execution bottlenecks.
- **C:** Correct. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. In this scenario: Inline TVFs inline directly into the distributed T-SQL query optimizer plan across Warehouse compute nodes without row-by-row procedural execution bottlenecks.
- **D:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Inline TVFs inline directly into the distributed T-SQL query optimizer plan across Warehouse compute nodes without row-by-row procedural execution bottlenecks.

### Question 39 — C

Answer: Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions. Raw source integers collide across systems; generating a single-column integer surrogate key (`ProductKey`) mapped to `(SourceSystem, NaturalSKU)` resolves cross-system collisions and enables SCD2 history. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: Raw source integers collide across systems; generating a single-column integer surrogate key (`ProductKey`) mapped to `(SourceSystem, NaturalSKU)` resolves cross-system collisions and enables SCD2 history.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Raw source integers collide across systems; generating a single-column integer surrogate key (`ProductKey`) mapped to `(SourceSystem, NaturalSKU)` resolves cross-system collisions and enables SCD2 history.
- **C:** Correct. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. In this scenario: Raw source integers collide across systems; generating a single-column integer surrogate key (`ProductKey`) mapped to `(SourceSystem, NaturalSKU)` resolves cross-system collisions and enables SCD2 history.
- **D:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Raw source integers collide across systems; generating a single-column integer surrogate key (`ProductKey`) mapped to `(SourceSystem, NaturalSKU)` resolves cross-system collisions and enables SCD2 history.

### Question 40 — C

Answer: Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes. A conformed Gold `DimDate` calendar table containing unbroken daily rows plus 4-5-4 fiscal week/period/year integers enables consistent time intelligence across all facts and Direct Lake models. A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: A conformed Gold `DimDate` calendar table containing unbroken daily rows plus 4-5-4 fiscal week/period/year integers enables consistent time intelligence across all facts and Direct Lake models.
- **B:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: A conformed Gold `DimDate` calendar table containing unbroken daily rows plus 4-5-4 fiscal week/period/year integers enables consistent time intelligence across all facts and Direct Lake models.
- **C:** Correct. A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering. In this scenario: A conformed Gold `DimDate` calendar table containing unbroken daily rows plus 4-5-4 fiscal week/period/year integers enables consistent time intelligence across all facts and Direct Lake models.
- **D:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: A conformed Gold `DimDate` calendar table containing unbroken daily rows plus 4-5-4 fiscal week/period/year integers enables consistent time intelligence across all facts and Direct Lake models.

### Question 41 — B, E

Answers: Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs; Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions. Replacing row-level Python `@udf` functions with vectorized `pyspark.sql.functions` inside `.withColumn()` and joining compact integer surrogate keys eliminates Python JVM serialization bottlenecks. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Replacing row-level Python `@udf` functions with vectorized `pyspark.sql.functions` inside `.withColumn()` and joining compact integer surrogate keys eliminates Python JVM serialization bottlenecks.
- **B:** Correct. Native Catalyst/Photon-optimized pyspark.sql.functions execute in vectorized JVM/native code across partitions, avoiding the severe Python serialization bottleneck of row-level UDFs. In this scenario: Replacing row-level Python `@udf` functions with vectorized `pyspark.sql.functions` inside `.withColumn()` and joining compact integer surrogate keys eliminates Python JVM serialization bottlenecks.
- **C:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Replacing row-level Python `@udf` functions with vectorized `pyspark.sql.functions` inside `.withColumn()` and joining compact integer surrogate keys eliminates Python JVM serialization bottlenecks.
- **D:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Replacing row-level Python `@udf` functions with vectorized `pyspark.sql.functions` inside `.withColumn()` and joining compact integer surrogate keys eliminates Python JVM serialization bottlenecks.
- **E:** Correct. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. In this scenario: Replacing row-level Python `@udf` functions with vectorized `pyspark.sql.functions` inside `.withColumn()` and joining compact integer surrogate keys eliminates Python JVM serialization bottlenecks.

### Question 42 — B

Answer: Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures. Mixing order-header grain and order-line grain in a single fact table double-counts header metrics; every fact table must enforce a single uniform atomic grain (or allocate header amounts proportionally to lines). Keeping fact tables at a single, consistent atomic grain with integer foreign keys and additive measures eliminates double-counting and supports flexible rollups across every conformed dimension. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Why the keyed choice wins: Mixing order-header grain and order-line grain in a single fact table double-counts header metrics; every fact table must enforce a single uniform atomic grain (or allocate header amounts proportionally to lines).
- **B:** Correct. Keeping fact tables at a single, consistent atomic grain with integer foreign keys and additive measures eliminates double-counting and supports flexible rollups across every conformed dimension. In this scenario: Mixing order-header grain and order-line grain in a single fact table double-counts header metrics; every fact table must enforce a single uniform atomic grain (or allocate header amounts proportionally to lines).
- **C:** Incorrect for this requirement. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Why the keyed choice wins: Mixing order-header grain and order-line grain in a single fact table double-counts header metrics; every fact table must enforce a single uniform atomic grain (or allocate header amounts proportionally to lines).
- **D:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Mixing order-header grain and order-line grain in a single fact table double-counts header metrics; every fact table must enforce a single uniform atomic grain (or allocate header amounts proportionally to lines).

### Question 43 — B

Answer: Stage and deduplicate incoming records by natural key → Compare tracked attributes against active (IsCurrent = 1) Gold rows → Expire changed active rows (EffectiveEndDate, IsCurrent = 0) → Insert new active versions with fresh surrogate keys. Deduplicating incoming store rows, comparing tracked attributes against `IsCurrent = 1` rows, expiring changed rows (`EffectiveEndDate`, `IsCurrent = 0`), and inserting new active rows with fresh surrogate keys preserves history. Correct order: deduplicate staging first, detect attribute changes against current rows, close out prior active intervals without losing their surrogate keys, and insert new active versions. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. Incorrect: regenerating surrogate keys on truncate breaks every existing historical fact foreign key, and marking multiple rows IsCurrent = 1 duplicates fact joins. Why the keyed choice wins: Deduplicating incoming store rows, comparing tracked attributes against `IsCurrent = 1` rows, expiring changed rows (`EffectiveEndDate`, `IsCurrent = 0`), and inserting new active rows with fresh surrogate keys preserves history.
- **B:** Correct. Correct order: deduplicate staging first, detect attribute changes against current rows, close out prior active intervals without losing their surrogate keys, and insert new active versions. In this scenario: Deduplicating incoming store rows, comparing tracked attributes against `IsCurrent = 1` rows, expiring changed rows (`EffectiveEndDate`, `IsCurrent = 0`), and inserting new active rows with fresh surrogate keys preserves history.
- **C:** Incorrect for this requirement. Incorrect: new versions must be active (IsCurrent = 1), EffectiveStartDate of historical intervals must remain immutable, and natural keys are required to match future CDC updates. Why the keyed choice wins: Deduplicating incoming store rows, comparing tracked attributes against `IsCurrent = 1` rows, expiring changed rows (`EffectiveEndDate`, `IsCurrent = 0`), and inserting new active rows with fresh surrogate keys preserves history.
- **D:** Incorrect for this requirement. Incorrect: deleting unmatched keys and enabling Assume referential integrity omits orphan rows silently in INNER JOINs. Why the keyed choice wins: Deduplicating incoming store rows, comparing tracked attributes against `IsCurrent = 1` rows, expiring changed rows (`EffectiveEndDate`, `IsCurrent = 0`), and inserting new active rows with fresh surrogate keys preserves history.

### Question 44 — B, D, E

Answers: Organize OneLake into Bronze (raw immutable), Silver (validated, deduplicated, conformed), and Gold (star-schema dimensions and facts with V-Order); Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns; Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures. Structuring Bronze/Silver/Gold Medallion layers, maintaining uniform atomic fact grain with integer foreign keys, and tracking historical dimension attribute changes via SCD Type 2 form the recommended Gold star schema. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Structuring Bronze/Silver/Gold Medallion layers, maintaining uniform atomic fact grain with integer foreign keys, and tracking historical dimension attribute changes via SCD Type 2 form the recommended Gold star schema.
- **B:** Correct. Keeping fact tables at a single, consistent atomic grain with integer foreign keys and additive measures eliminates double-counting and supports flexible rollups across every conformed dimension. In this scenario: Structuring Bronze/Silver/Gold Medallion layers, maintaining uniform atomic fact grain with integer foreign keys, and tracking historical dimension attribute changes via SCD Type 2 form the recommended Gold star schema.
- **C:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Structuring Bronze/Silver/Gold Medallion layers, maintaining uniform atomic fact grain with integer foreign keys, and tracking historical dimension attribute changes via SCD Type 2 form the recommended Gold star schema.
- **D:** Correct. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. In this scenario: Structuring Bronze/Silver/Gold Medallion layers, maintaining uniform atomic fact grain with integer foreign keys, and tracking historical dimension attribute changes via SCD Type 2 form the recommended Gold star schema.
- **E:** Correct. The Medallion architecture separates raw source fidelity (Bronze), enterprise data quality/conformance (Silver), and BI/Direct Lake star-schema consumption (Gold). In this scenario: Structuring Bronze/Silver/Gold Medallion layers, maintaining uniform atomic fact grain with integer foreign keys, and tracking historical dimension attribute changes via SCD Type 2 form the recommended Gold star schema.
- **F:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Structuring Bronze/Silver/Gold Medallion layers, maintaining uniform atomic fact grain with integer foreign keys, and tracking historical dimension attribute changes via SCD Type 2 form the recommended Gold star schema.

### Question 45 — D

Answer: Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension. Denormalizing `DistrictName`, `RegionName`, and `CountryName` directly into `Gold.DimStore` turns a 4-table snowflake chain into a single 1-hop star dimension. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Local study-map skill 2.9 (Denormalize Snowflake Hierarchies into Flattened Gold Dimension Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Dimensional modeling & denormalizing snowflake tables in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables).

- **A:** Incorrect for this requirement. Connecting to an existing shared semantic model in DirectQuery mode creates a local composite model (using remote model chains and limited cross-island relationships) so analysts can extend governed enterprise measures without copying the core model. Why the keyed choice wins: Denormalizing `DistrictName`, `RegionName`, and `CountryName` directly into `Gold.DimStore` turns a 4-table snowflake chain into a single 1-hop star dimension.
- **B:** Incorrect for this requirement. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Why the keyed choice wins: Denormalizing `DistrictName`, `RegionName`, and `CountryName` directly into `Gold.DimStore` turns a 4-table snowflake chain into a single 1-hop star dimension.
- **C:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Denormalizing `DistrictName`, `RegionName`, and `CountryName` directly into `Gold.DimStore` turns a 4-table snowflake chain into a single 1-hop star dimension.
- **D:** Correct. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. In this scenario: Denormalizing `DistrictName`, `RegionName`, and `CountryName` directly into `Gold.DimStore` turns a 4-table snowflake chain into a single 1-hop star dimension.

### Question 46 — A

Answer: Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP). Materializing a pre-aggregated Gold summary Delta table grouped by `DateKey`, `RegionKey`, and `DivisionKey` reduces 8 billion scan rows to a few hundred thousand summary rows. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Correct. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. In this scenario: Materializing a pre-aggregated Gold summary Delta table grouped by `DateKey`, `RegionKey`, and `DivisionKey` reduces 8 billion scan rows to a few hundred thousand summary rows.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Materializing a pre-aggregated Gold summary Delta table grouped by `DateKey`, `RegionKey`, and `DivisionKey` reduces 8 billion scan rows to a few hundred thousand summary rows.
- **C:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Materializing a pre-aggregated Gold summary Delta table grouped by `DateKey`, `RegionKey`, and `DivisionKey` reduces 8 billion scan rows to a few hundred thousand summary rows.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Materializing a pre-aggregated Gold summary Delta table grouped by `DateKey`, `RegionKey`, and `DivisionKey` reduces 8 billion scan rows to a few hundred thousand summary rows.

### Question 47 — C

Answer: GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ()). `GROUP BY GROUPING SETS ((RouteId, Borough), ...)` — specifically `GROUPING SETS` — computes explicit multi-level subtotals and the grand total `()` in one scan. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `GROUP BY GROUPING SETS ((RouteId, Borough), ...)` — specifically `GROUPING SETS` — computes explicit multi-level subtotals and the grand total `()` in one scan.
- **B:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `GROUP BY GROUPING SETS ((RouteId, Borough), ...)` — specifically `GROUPING SETS` — computes explicit multi-level subtotals and the grand total `()` in one scan.
- **C:** Correct. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. In this scenario: `GROUP BY GROUPING SETS ((RouteId, Borough), ...)` — specifically `GROUPING SETS` — computes explicit multi-level subtotals and the grand total `()` in one scan.
- **D:** Incorrect for this requirement. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Why the keyed choice wins: `GROUP BY GROUPING SETS ((RouteId, Borough), ...)` — specifically `GROUPING SETS` — computes explicit multi-level subtotals and the grand total `()` in one scan.

### Question 48 — B

Answer: Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs. HyperLogLog `approx_count_distinct` avoids massive distinct-value shuffle hash maps when ~1–2% statistical tolerance satisfies executive trend monitoring. Native Catalyst/Photon-optimized pyspark.sql.functions execute in vectorized JVM/native code across partitions, avoiding the severe Python serialization bottleneck of row-level UDFs. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: HyperLogLog `approx_count_distinct` avoids massive distinct-value shuffle hash maps when ~1–2% statistical tolerance satisfies executive trend monitoring.
- **B:** Correct. Native Catalyst/Photon-optimized pyspark.sql.functions execute in vectorized JVM/native code across partitions, avoiding the severe Python serialization bottleneck of row-level UDFs. In this scenario: HyperLogLog `approx_count_distinct` avoids massive distinct-value shuffle hash maps when ~1–2% statistical tolerance satisfies executive trend monitoring.
- **C:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: HyperLogLog `approx_count_distinct` avoids massive distinct-value shuffle hash maps when ~1–2% statistical tolerance satisfies executive trend monitoring.
- **D:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: HyperLogLog `approx_count_distinct` avoids massive distinct-value shuffle hash maps when ~1–2% statistical tolerance satisfies executive trend monitoring.

### Question 49 — A

Answer: WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET. Adding `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` skips rewriting Parquet files when matched records have identical attribute hashes. Guarding WHEN MATCHED with a hash/attribute inequality prevents rewriting unchanged Delta Parquet files on untouched rows during incremental upserts. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Correct. Guarding WHEN MATCHED with a hash/attribute inequality prevents rewriting unchanged Delta Parquet files on untouched rows during incremental upserts. In this scenario: Adding `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` skips rewriting Parquet files when matched records have identical attribute hashes.
- **B:** Incorrect for this requirement. Omitting PARTITION BY ranks across the entire table globally rather than per entity, and RANK() returns duplicate rank-1 rows on exact timestamp ties. Why the keyed choice wins: Adding `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` skips rewriting Parquet files when matched records have identical attribute hashes.
- **C:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: Adding `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` skips rewriting Parquet files when matched records have identical attribute hashes.
- **D:** Incorrect for this requirement. Fabric Data Warehouse supports FILTER PREDICATE with inline TVFs (not stored procedures or SQL Server DML BLOCK PREDICATE triggers). Why the keyed choice wins: Adding `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` skips rewriting Parquet files when matched records have identical attribute hashes.

### Question 50 — D

Answer: Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table. A `Left Anti` join returns exclusively rows from the left table (`FactReturns`) with zero matching keys in the right table (`FactSales`). A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. Broadcasting a small dimension table (<10–100 MB) to every executor avoids an expensive cluster-wide shuffle sort-merge join of the massive fact DataFrame. Why the keyed choice wins: A `Left Anti` join returns exclusively rows from the left table (`FactReturns`) with zero matching keys in the right table (`FactSales`).
- **B:** Incorrect for this requirement. Delta Lake MERGE INTO (in Spark SQL, PySpark DeltaTable.forPath().merge(), or Warehouse T-SQL) atomically applies incremental CDC inserts, updates, and soft-deletes in a single ACID transaction. Why the keyed choice wins: A `Left Anti` join returns exclusively rows from the left table (`FactReturns`) with zero matching keys in the right table (`FactSales`).
- **C:** Incorrect for this requirement. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Why the keyed choice wins: A `Left Anti` join returns exclusively rows from the left table (`FactReturns`) with zero matching keys in the right table (`FactSales`).
- **D:** Correct. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. In this scenario: A `Left Anti` join returns exclusively rows from the left table (`FactReturns`) with zero matching keys in the right table (`FactSales`).

### Question 51 — B, C

Answers: fact_df.join(F.broadcast(dim_store_df), on="StoreKey", how="left"); Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement. Using `F.broadcast(dim_store_df)` eliminates shuffling the 600M-row fact DataFrame, and `MERGE INTO` commits the incremental upsert atomically in Delta Lake. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Using `F.broadcast(dim_store_df)` eliminates shuffling the 600M-row fact DataFrame, and `MERGE INTO` commits the incremental upsert atomically in Delta Lake.
- **B:** Correct. Wrapping the small dimension DataFrame in pyspark.sql.functions.broadcast() avoids shuffling the multi-hundred-million-row fact DataFrame across Spark executors. In this scenario: Using `F.broadcast(dim_store_df)` eliminates shuffling the 600M-row fact DataFrame, and `MERGE INTO` commits the incremental upsert atomically in Delta Lake.
- **C:** Correct. Delta Lake MERGE INTO (in Spark SQL, PySpark DeltaTable.forPath().merge(), or Warehouse T-SQL) atomically applies incremental CDC inserts, updates, and soft-deletes in a single ACID transaction. In this scenario: Using `F.broadcast(dim_store_df)` eliminates shuffling the 600M-row fact DataFrame, and `MERGE INTO` commits the incremental upsert atomically in Delta Lake.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Using `F.broadcast(dim_store_df)` eliminates shuffling the 600M-row fact DataFrame, and `MERGE INTO` commits the incremental upsert atomically in Delta Lake.
- **E:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Using `F.broadcast(dim_store_df)` eliminates shuffling the 600M-row fact DataFrame, and `MERGE INTO` commits the incremental upsert atomically in Delta Lake.

### Question 52 — D

Answer: ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC). `ROW_NUMBER() OVER (PARTITION BY <EntityKey> ORDER BY EventTimestamp DESC)` guarantees exactly one row receives `rn = 1` per entity key even when timestamps tie, unlike `RANK()`. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <EntityKey> ORDER BY EventTimestamp DESC)` guarantees exactly one row receives `rn = 1` per entity key even when timestamps tie, unlike `RANK()`.
- **B:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <EntityKey> ORDER BY EventTimestamp DESC)` guarantees exactly one row receives `rn = 1` per entity key even when timestamps tie, unlike `RANK()`.
- **C:** Incorrect for this requirement. Omitting PARTITION BY ranks across the entire table globally rather than per entity, and RANK() returns duplicate rank-1 rows on exact timestamp ties. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <EntityKey> ORDER BY EventTimestamp DESC)` guarantees exactly one row receives `rn = 1` per entity key even when timestamps tie, unlike `RANK()`.
- **D:** Correct. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. In this scenario: `ROW_NUMBER() OVER (PARTITION BY <EntityKey> ORDER BY EventTimestamp DESC)` guarantees exactly one row receives `rn = 1` per entity key even when timestamps tie, unlike `RANK()`.

### Question 53 — B, D

Answers: Launch Data Wrangler from a Fabric Spark notebook (or enable Power Query Column profiling based on entire data set) to inspect nulls, duplicates, and distributions and export generated PySpark code; Deduplicate using ROW_NUMBER() OVER (PARTITION BY BusinessKey ORDER BY ModifiedTimestamp DESC) = 1. Switching Power Query profiling to the entire dataset (or profiling in Spark Data Wrangler to generate PySpark code) exposes post-row-1000 anomalies, and `ROW_NUMBER() OVER (PARTITION BY ...)` removes duplicate keys. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Switching Power Query profiling to the entire dataset (or profiling in Spark Data Wrangler to generate PySpark code) exposes post-row-1000 anomalies, and `ROW_NUMBER() OVER (PARTITION BY ...)` removes duplicate keys.
- **B:** Correct. Power Query profiles only the top 1,000 rows by default unless switched to entire dataset, whereas Data Wrangler interactively profiles Pandas/Spark DataFrames and emits reproducible Python/PySpark cleaning code. In this scenario: Switching Power Query profiling to the entire dataset (or profiling in Spark Data Wrangler to generate PySpark code) exposes post-row-1000 anomalies, and `ROW_NUMBER() OVER (PARTITION BY ...)` removes duplicate keys.
- **C:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Switching Power Query profiling to the entire dataset (or profiling in Spark Data Wrangler to generate PySpark code) exposes post-row-1000 anomalies, and `ROW_NUMBER() OVER (PARTITION BY ...)` removes duplicate keys.
- **D:** Correct. Windowing by BusinessKey ordered descending by ingestion or source-change timestamp deterministically retains only the latest version of duplicate CDC events while preserving all non-key columns. In this scenario: Switching Power Query profiling to the entire dataset (or profiling in Spark Data Wrangler to generate PySpark code) exposes post-row-1000 anomalies, and `ROW_NUMBER() OVER (PARTITION BY ...)` removes duplicate keys.
- **E:** Incorrect for this requirement. Using >= AND <= on both ends causes rows stamped exactly at midnight on partition boundaries to load into two adjacent partitions, silently double-counting sales totals. Why the keyed choice wins: Switching Power Query profiling to the entire dataset (or profiling in Spark Data Wrangler to generate PySpark code) exposes post-row-1000 anomalies, and `ROW_NUMBER() OVER (PARTITION BY ...)` removes duplicate keys.

### Question 54 — D

Answer: TRY_CAST(RawReading AS DECIMAL(18, 4)). `TRY_CAST(RawReading AS DECIMAL(18, 4))` avoids fatal batch-aborting conversion exceptions and uses exact fixed-point `DECIMAL` rather than imprecise binary `FLOAT`. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Local study-map skill 2.13 (Convert Column Data Types Safely (TRY_CAST, Fixed Decimal, and Direct Lake Supported Primitive Types)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data types in Fabric Data Warehouse and Direct Lake Delta tables (https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types).

- **A:** Incorrect for this requirement. Omitting PARTITION BY ranks across the entire table globally rather than per entity, and RANK() returns duplicate rank-1 rows on exact timestamp ties. Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` avoids fatal batch-aborting conversion exceptions and uses exact fixed-point `DECIMAL` rather than imprecise binary `FLOAT`.
- **B:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` avoids fatal batch-aborting conversion exceptions and uses exact fixed-point `DECIMAL` rather than imprecise binary `FLOAT`.
- **C:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` avoids fatal batch-aborting conversion exceptions and uses exact fixed-point `DECIMAL` rather than imprecise binary `FLOAT`.
- **D:** Correct. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. In this scenario: `TRY_CAST(RawReading AS DECIMAL(18, 4))` avoids fatal batch-aborting conversion exceptions and uses exact fixed-point `DECIMAL` rather than imprecise binary `FLOAT`.

### Question 55 — C

Answer: Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake. Direct Lake does not support `Binary`, `GUID`, or nested `Struct`/`Array`/`Map` Delta types; flattening struct fields and converting/omitting binary or GUID columns into `STRING`/primitive columns ensures full compatibility. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. Local study-map skill 2.13 (Convert Column Data Types Safely (TRY_CAST, Fixed Decimal, and Direct Lake Supported Primitive Types)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data types in Fabric Data Warehouse and Direct Lake Delta tables (https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types).

- **A:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Direct Lake does not support `Binary`, `GUID`, or nested `Struct`/`Array`/`Map` Delta types; flattening struct fields and converting/omitting binary or GUID columns into `STRING`/primitive columns ensures full compatibility.
- **B:** Incorrect for this requirement. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Why the keyed choice wins: Direct Lake does not support `Binary`, `GUID`, or nested `Struct`/`Array`/`Map` Delta types; flattening struct fields and converting/omitting binary or GUID columns into `STRING`/primitive columns ensures full compatibility.
- **C:** Correct. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. In this scenario: Direct Lake does not support `Binary`, `GUID`, or nested `Struct`/`Array`/`Map` Delta types; flattening struct fields and converting/omitting binary or GUID columns into `STRING`/primitive columns ensures full compatibility.
- **D:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Direct Lake does not support `Binary`, `GUID`, or nested `Struct`/`Array`/`Map` Delta types; flattening struct fields and converting/omitting binary or GUID columns into `STRING`/primitive columns ensures full compatibility.

### Question 56 — A

Answer: Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled. Reordering the native `FiscalYear = 2026` row filter ahead of the non-foldable custom M transformation pushes `WHERE FiscalYear = 2026` down to SQL Server before rows stream out. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. Local study-map skill 2.14 (Filter Data Early Preserving Power Query Folding (View Native Query) and Sargable Delta File Pruning), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query folding indicators & predicate pushdown in Power Query and Delta Lake (https://learn.microsoft.com/en-us/power-query/query-folding-basics).

- **A:** Correct. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. In this scenario: Reordering the native `FiscalYear = 2026` row filter ahead of the non-foldable custom M transformation pushes `WHERE FiscalYear = 2026` down to SQL Server before rows stream out.
- **B:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Reordering the native `FiscalYear = 2026` row filter ahead of the non-foldable custom M transformation pushes `WHERE FiscalYear = 2026` down to SQL Server before rows stream out.
- **C:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Reordering the native `FiscalYear = 2026` row filter ahead of the non-foldable custom M transformation pushes `WHERE FiscalYear = 2026` down to SQL Server before rows stream out.
- **D:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: Reordering the native `FiscalYear = 2026` row filter ahead of the non-foldable custom M transformation pushes `WHERE FiscalYear = 2026` down to SQL Server before rows stream out.

### Question 57 — A

Answer: Filter on physical Delta partition or liquid-clustered date columns using sargable range predicates (OrderDate >= '2026-01-01') without wrapping the column in functions. Sargable range predicates on the raw `SaleDate` column leverage Parquet min/max column statistics and Delta file skipping, whereas wrapping the column in `CONVERT`/`LEFT` forces a full scan. Wrapping a column in YEAR(OrderDate) = 2026 blocks file-level min/max data skipping and partition pruning; sargable range predicates let Spark and SQL endpoints skip irrelevant Parquet files entirely. Local study-map skill 2.14 (Filter Data Early Preserving Power Query Folding (View Native Query) and Sargable Delta File Pruning), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query folding indicators & predicate pushdown in Power Query and Delta Lake (https://learn.microsoft.com/en-us/power-query/query-folding-basics).

- **A:** Correct. Wrapping a column in YEAR(OrderDate) = 2026 blocks file-level min/max data skipping and partition pruning; sargable range predicates let Spark and SQL endpoints skip irrelevant Parquet files entirely. In this scenario: Sargable range predicates on the raw `SaleDate` column leverage Parquet min/max column statistics and Delta file skipping, whereas wrapping the column in `CONVERT`/`LEFT` forces a full scan.
- **B:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: Sargable range predicates on the raw `SaleDate` column leverage Parquet min/max column statistics and Delta file skipping, whereas wrapping the column in `CONVERT`/`LEFT` forces a full scan.
- **C:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: Sargable range predicates on the raw `SaleDate` column leverage Parquet min/max column statistics and Delta file skipping, whereas wrapping the column in `CONVERT`/`LEFT` forces a full scan.
- **D:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: Sargable range predicates on the raw `SaleDate` column leverage Parquet min/max column statistics and Delta file skipping, whereas wrapping the column in `CONVERT`/`LEFT` forces a full scan.

### Question 58 — B

Answer: Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view. `New visual query` in the Warehouse/SQL analytics endpoint offers a no-code visual diagram canvas (`Merge`, `Filter`, `Group by`) with `Save as view`. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Local study-map skill 2.15 (Select, Filter, and Aggregate Data Using the Visual Query Editor and Save as SQL Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query using the Visual query editor in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/visual-query-editor).

- **A:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: `New visual query` in the Warehouse/SQL analytics endpoint offers a no-code visual diagram canvas (`Merge`, `Filter`, `Group by`) with `Save as view`.
- **B:** Correct. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. In this scenario: `New visual query` in the Warehouse/SQL analytics endpoint offers a no-code visual diagram canvas (`Merge`, `Filter`, `Group by`) with `Save as view`.
- **C:** Incorrect for this requirement. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Why the keyed choice wins: `New visual query` in the Warehouse/SQL analytics endpoint offers a no-code visual diagram canvas (`Merge`, `Filter`, `Group by`) with `Save as view`.
- **D:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: `New visual query` in the Warehouse/SQL analytics endpoint offers a no-code visual diagram canvas (`Merge`, `Filter`, `Group by`) with `Save as view`.

### Question 59 — B

Answer: Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view. Saving as a view compiles the visual diagram steps into a native T-SQL `CREATE VIEW` executed by the distributed SQL analytics endpoint engine without duplicating data into Power Query staging. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Local study-map skill 2.15 (Select, Filter, and Aggregate Data Using the Visual Query Editor and Save as SQL Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query using the Visual query editor in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/visual-query-editor).

- **A:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Saving as a view compiles the visual diagram steps into a native T-SQL `CREATE VIEW` executed by the distributed SQL analytics endpoint engine without duplicating data into Power Query staging.
- **B:** Correct. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. In this scenario: Saving as a view compiles the visual diagram steps into a native T-SQL `CREATE VIEW` executed by the distributed SQL analytics endpoint engine without duplicating data into Power Query staging.
- **C:** Incorrect for this requirement. ALM Toolkit performs metadata-only diffs and incremental TMSL deployments over XMLA, preserving existing processed historical partitions and incremental refresh windows in Production. Why the keyed choice wins: Saving as a view compiles the visual diagram steps into a native T-SQL `CREATE VIEW` executed by the distributed SQL analytics endpoint engine without duplicating data into Power Query staging.
- **D:** Incorrect for this requirement. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. Why the keyed choice wins: Saving as a view compiles the visual diagram steps into a native T-SQL `CREATE VIEW` executed by the distributed SQL analytics endpoint engine without duplicating data into Power Query staging.

### Question 60 — B

Answer: Query across a Warehouse and a Lakehouse SQL analytics endpoint in the same workspace using three-part T-SQL naming (SalesLakehouse.dbo.RawOrders). Same-workspace Warehouses and Lakehouse SQL analytics endpoints support direct three-part T-SQL cross-database naming (`ClickstreamLakehouse.dbo.WebSessions`) with zero data movement or shortcuts required. Fabric Warehouse and SQL analytics endpoints inside the same workspace share a unified SQL engine namespace, enabling zero-copy cross-database T-SQL joins via DatabaseName.SchemaName.ObjectName. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: Same-workspace Warehouses and Lakehouse SQL analytics endpoints support direct three-part T-SQL cross-database naming (`ClickstreamLakehouse.dbo.WebSessions`) with zero data movement or shortcuts required.
- **B:** Correct. Fabric Warehouse and SQL analytics endpoints inside the same workspace share a unified SQL engine namespace, enabling zero-copy cross-database T-SQL joins via DatabaseName.SchemaName.ObjectName. In this scenario: Same-workspace Warehouses and Lakehouse SQL analytics endpoints support direct three-part T-SQL cross-database naming (`ClickstreamLakehouse.dbo.WebSessions`) with zero data movement or shortcuts required.
- **C:** Incorrect for this requirement. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. Why the keyed choice wins: Same-workspace Warehouses and Lakehouse SQL analytics endpoints support direct three-part T-SQL cross-database naming (`ClickstreamLakehouse.dbo.WebSessions`) with zero data movement or shortcuts required.
- **D:** Incorrect for this requirement. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. Why the keyed choice wins: Same-workspace Warehouses and Lakehouse SQL analytics endpoints support direct three-part T-SQL cross-database naming (`ClickstreamLakehouse.dbo.WebSessions`) with zero data movement or shortcuts required.

### Question 61 — D

Answer: OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000'). `OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')` invokes Fabric Data Warehouse Time Travel up to the 30-day retention horizon. Fabric Data Warehouse Time Travel uses the query hint OPTION (FOR TIMESTAMP AS OF 'YYYY-MM-DDTHH:MM:SS.fff') to read exact point-in-time historical snapshots within the retention window. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Incorrect for this requirement. CREATE TABLE ... AS CLONE OF creates a zero-copy metadata clone of a Fabric Warehouse table instantaneously (optionally AT a specific UTC timestamp) without duplicating Parquet files. Why the keyed choice wins: `OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')` invokes Fabric Data Warehouse Time Travel up to the 30-day retention horizon.
- **B:** Incorrect for this requirement. Fabric Data Warehouse supports FILTER PREDICATE with inline TVFs (not stored procedures or SQL Server DML BLOCK PREDICATE triggers). Why the keyed choice wins: `OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')` invokes Fabric Data Warehouse Time Travel up to the 30-day retention horizon.
- **C:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: `OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')` invokes Fabric Data Warehouse Time Travel up to the 30-day retention horizon.
- **D:** Correct. Fabric Data Warehouse Time Travel uses the query hint OPTION (FOR TIMESTAMP AS OF 'YYYY-MM-DDTHH:MM:SS.fff') to read exact point-in-time historical snapshots within the retention window. In this scenario: `OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')` invokes Fabric Data Warehouse Time Travel up to the 30-day retention horizon.

### Question 62 — A, C

Answers: Write T-SQL window functions using LAG(...) OVER (PARTITION BY ... ORDER BY ...) and SUM(...) OVER (... ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW); Query historical Warehouse state using SELECT ... FROM dbo.FactSales OPTION (FOR TIMESTAMP AS OF '2026-10-15T00:00:00') or CREATE TABLE ... AS CLONE OF. Window functions (`LAG(...) OVER` and `SUM(...) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`) compute deltas/running totals in one pass, and `CREATE TABLE ... AS CLONE OF` creates zero-copy snapshots. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Correct. T-SQL analytic window functions compute period-over-period deltas and running totals in a single pass without self-joins or collapsing detail rows. In this scenario: Window functions (`LAG(...) OVER` and `SUM(...) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`) compute deltas/running totals in one pass, and `CREATE TABLE ... AS CLONE OF` creates zero-copy snapshots.
- **B:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Window functions (`LAG(...) OVER` and `SUM(...) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`) compute deltas/running totals in one pass, and `CREATE TABLE ... AS CLONE OF` creates zero-copy snapshots.
- **C:** Correct. Fabric Warehouse supports T-SQL Time Travel (up to the 30-day retention window) via OPTION (FOR TIMESTAMP AS OF ...) and zero-copy table clones via CREATE TABLE ... AS CLONE OF ... AT. In this scenario: Window functions (`LAG(...) OVER` and `SUM(...) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`) compute deltas/running totals in one pass, and `CREATE TABLE ... AS CLONE OF` creates zero-copy snapshots.
- **D:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: Window functions (`LAG(...) OVER` and `SUM(...) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`) compute deltas/running totals in one pass, and `CREATE TABLE ... AS CLONE OF` creates zero-copy snapshots.
- **E:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: Window functions (`LAG(...) OVER` and `SUM(...) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`) compute deltas/running totals in one pass, and `CREATE TABLE ... AS CLONE OF` creates zero-copy snapshots.

### Question 63 — A

Answer: | make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion. `| make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion` fills empty time buckets with `0`, unlike `summarize by bin()` which omits empty intervals. make-series builds regular gap-filled time-series arrays (filling empty 1-minute buckets with default = 0) required for KQL anomaly detection and trend functions; summarize by bin() omits empty buckets. Local study-map skill 2.17 (Select, Filter, and Aggregate Data Using KQL (summarize, bin, arg_max, percentile, parse_json, mv-expand)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query data in a KQL queryset in Microsoft Fabric Real-Time Intelligence (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/kql-queryset).

- **A:** Correct. make-series builds regular gap-filled time-series arrays (filling empty 1-minute buckets with default = 0) required for KQL anomaly detection and trend functions; summarize by bin() omits empty buckets. In this scenario: `| make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion` fills empty time buckets with `0`, unlike `summarize by bin()` which omits empty intervals.
- **B:** Incorrect for this requirement. percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse. Why the keyed choice wins: `| make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion` fills empty time buckets with `0`, unlike `summarize by bin()` which omits empty intervals.
- **C:** Incorrect for this requirement. In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key. Why the keyed choice wins: `| make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion` fills empty time buckets with `0`, unlike `summarize by bin()` which omits empty intervals.
- **D:** Incorrect for this requirement. mv-expand unpacks a dynamic JSON array into one output row per array element while preserving parent event columns. Why the keyed choice wins: `| make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion` fills empty time buckets with `0`, unlike `summarize by bin()` which omits empty intervals.

### Question 64 — C

Answer: Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results. `DAX Query View` supports query-scoped `DEFINE MEASURE` blocks evaluated via `EVALUATE SUMMARIZECOLUMNS(...)` with one-step `Update model` promotion. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Local study-map skill 2.18 (Select, Filter, and Aggregate Data Using DAX Queries (DAX Query View, EVALUATE, SUMMARIZECOLUMNS, INFO.VIEW)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Work with DAX query view & INFO.VIEW functions in Power BI (https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view).

- **A:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: `DAX Query View` supports query-scoped `DEFINE MEASURE` blocks evaluated via `EVALUATE SUMMARIZECOLUMNS(...)` with one-step `Update model` promotion.
- **B:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: `DAX Query View` supports query-scoped `DEFINE MEASURE` blocks evaluated via `EVALUATE SUMMARIZECOLUMNS(...)` with one-step `Update model` promotion.
- **C:** Correct. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. In this scenario: `DAX Query View` supports query-scoped `DEFINE MEASURE` blocks evaluated via `EVALUATE SUMMARIZECOLUMNS(...)` with one-step `Update model` promotion.
- **D:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `DAX Query View` supports query-scoped `DEFINE MEASURE` blocks evaluated via `EVALUATE SUMMARIZECOLUMNS(...)` with one-step `Update model` promotion.

### Question 65 — D

Answer: EVALUATE INFO.VIEW.MEASURES(). `EVALUATE INFO.VIEW.MEASURES()` outputs comprehensive measure metadata directly inside DAX Query View without external XMLA DMV clients. INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags. Local study-map skill 2.18 (Select, Filter, and Aggregate Data Using DAX Queries (DAX Query View, EVALUATE, SUMMARIZECOLUMNS, INFO.VIEW)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Work with DAX query view & INFO.VIEW functions in Power BI (https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view).

- **A:** Incorrect for this requirement. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Why the keyed choice wins: `EVALUATE INFO.VIEW.MEASURES()` outputs comprehensive measure metadata directly inside DAX Query View without external XMLA DMV clients.
- **B:** Incorrect for this requirement. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. Why the keyed choice wins: `EVALUATE INFO.VIEW.MEASURES()` outputs comprehensive measure metadata directly inside DAX Query View without external XMLA DMV clients.
- **C:** Incorrect for this requirement. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Why the keyed choice wins: `EVALUATE INFO.VIEW.MEASURES()` outputs comprehensive measure metadata directly inside DAX Query View without external XMLA DMV clients.
- **D:** Correct. INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags. In this scenario: `EVALUATE INFO.VIEW.MEASURES()` outputs comprehensive measure metadata directly inside DAX Query View without external XMLA DMV clients.

### Question 66 — C

Answer: Configure Import storage mode. `Import` storage mode compresses the 150 MB dataset into VertiPaq memory once nightly via an On-premises gateway, providing maximum DAX capability and speed when source data is not in OneLake. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Local study-map skill 3.1 (Choose a Semantic Model Storage Mode (Import, DirectQuery, Direct Lake, and Dual)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model storage modes in the Power BI service & Microsoft Fabric (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode).

- **A:** Incorrect for this requirement. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Why the keyed choice wins: `Import` storage mode compresses the 150 MB dataset into VertiPaq memory once nightly via an On-premises gateway, providing maximum DAX capability and speed when source data is not in OneLake.
- **B:** Incorrect for this requirement. Direct Lake loads Delta Parquet columns directly from OneLake into VertiPaq memory on demand without scheduled Import data duplication or slow per-visual SQL translation. Why the keyed choice wins: `Import` storage mode compresses the 150 MB dataset into VertiPaq memory once nightly via an On-premises gateway, providing maximum DAX capability and speed when source data is not in OneLake.
- **C:** Correct. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. In this scenario: `Import` storage mode compresses the 150 MB dataset into VertiPaq memory once nightly via an On-premises gateway, providing maximum DAX capability and speed when source data is not in OneLake.
- **D:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Import` storage mode compresses the 150 MB dataset into VertiPaq memory once nightly via an On-premises gateway, providing maximum DAX capability and speed when source data is not in OneLake.

### Question 67 — A

Answer: Configure shared dimension tables in Dual storage mode inside a composite model. `Dual` storage mode allows shared dimensions to act as cached Import tables for summary hits and as DirectQuery tables for source-pushed detail joins. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Local study-map skill 3.1 (Choose a Semantic Model Storage Mode (Import, DirectQuery, Direct Lake, and Dual)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model storage modes in the Power BI service & Microsoft Fabric (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode).

- **A:** Correct. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. In this scenario: `Dual` storage mode allows shared dimensions to act as cached Import tables for summary hits and as DirectQuery tables for source-pushed detail joins.
- **B:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Dual` storage mode allows shared dimensions to act as cached Import tables for summary hits and as DirectQuery tables for source-pushed detail joins.
- **C:** Incorrect for this requirement. Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery. Why the keyed choice wins: `Dual` storage mode allows shared dimensions to act as cached Import tables for summary hits and as DirectQuery tables for source-pushed detail joins.
- **D:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Dual` storage mode allows shared dimensions to act as cached Import tables for summary hits and as DirectQuery tables for source-pushed detail joins.

### Question 68 — B

Answer: Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column. Disabling `Auto date/time` and running `Mark as date table` on `DimCalendar` pointing to its unique `Date`-typed `CalendarDate` column instructs DAX to clear integer-key filters automatically during time intelligence. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. Local study-map skill 3.2 (Implement a Star Schema for a Semantic Model (Mark as Date Table, Hide Keys, Sort by Column, Display Folders)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Set and use date tables & star-schema best practices in Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables).

- **A:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: Disabling `Auto date/time` and running `Mark as date table` on `DimCalendar` pointing to its unique `Date`-typed `CalendarDate` column instructs DAX to clear integer-key filters automatically during time intelligence.
- **B:** Correct. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. In this scenario: Disabling `Auto date/time` and running `Mark as date table` on `DimCalendar` pointing to its unique `Date`-typed `CalendarDate` column instructs DAX to clear integer-key filters automatically during time intelligence.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Disabling `Auto date/time` and running `Mark as date table` on `DimCalendar` pointing to its unique `Date`-typed `CalendarDate` column instructs DAX to clear integer-key filters automatically during time intelligence.
- **D:** Incorrect for this requirement. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. Why the keyed choice wins: Disabling `Auto date/time` and running `Mark as date table` on `DimCalendar` pointing to its unique `Date`-typed `CalendarDate` column instructs DAX to clear integer-key filters automatically during time intelligence.

### Question 69 — A, E

Answers: Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column; Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear. Disabling `Auto date/time` + marking `DimCalendar` removes `LocalDateTable_*` bloat, and hiding surrogate keys/raw columns while setting `MonthName` `Sort by Column` to `MonthNumberOfYear` fixes sorting and self-service UX. Local study-map skill 3.2 (Implement a Star Schema for a Semantic Model (Mark as Date Table, Hide Keys, Sort by Column, Display Folders)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Set and use date tables & star-schema best practices in Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables).

- **A:** Correct. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. In this scenario: Disabling `Auto date/time` + marking `DimCalendar` removes `LocalDateTable_*` bloat, and hiding surrogate keys/raw columns while setting `MonthName` `Sort by Column` to `MonthNumberOfYear` fixes sorting and self-service UX.
- **B:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Disabling `Auto date/time` + marking `DimCalendar` removes `LocalDateTable_*` bloat, and hiding surrogate keys/raw columns while setting `MonthName` `Sort by Column` to `MonthNumberOfYear` fixes sorting and self-service UX.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Disabling `Auto date/time` + marking `DimCalendar` removes `LocalDateTable_*` bloat, and hiding surrogate keys/raw columns while setting `MonthName` `Sort by Column` to `MonthNumberOfYear` fixes sorting and self-service UX.
- **D:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Disabling `Auto date/time` + marking `DimCalendar` removes `LocalDateTable_*` bloat, and hiding surrogate keys/raw columns while setting `MonthName` `Sort by Column` to `MonthNumberOfYear` fixes sorting and self-service UX.
- **E:** Correct. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. In this scenario: Disabling `Auto date/time` + marking `DimCalendar` removes `LocalDateTable_*` bloat, and hiding surrogate keys/raw columns while setting `MonthName` `Sort by Column` to `MonthNumberOfYear` fixes sorting and self-service UX.

### Question 70 — C

Answer: CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey])). `CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))` activates the specified inactive `1:*` relationship strictly within that measure's filter context. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. CROSSFILTER(..., BOTH) enables bidirectional filter propagation across a bridge table only inside the specific measure rather than globally across the model. Why the keyed choice wins: `CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))` activates the specified inactive `1:*` relationship strictly within that measure's filter context.
- **B:** Incorrect for this requirement. ISINSCOPE('DimProduct'[SKU]) evaluates TRUE only when SKU is actively grouping the visual hierarchy level, suppressing misleading margin figures at subtotal rows. Why the keyed choice wins: `CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))` activates the specified inactive `1:*` relationship strictly within that measure's filter context.
- **C:** Correct. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. In this scenario: `CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))` activates the specified inactive `1:*` relationship strictly within that measure's filter context.
- **D:** Incorrect for this requirement. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. Why the keyed choice wins: `CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))` activates the specified inactive `1:*` relationship strictly within that measure's filter context.

### Question 71 — B

Answer: Introduce a deduplicated Bridge table between the two dimensions and scope bidirectional propagation strictly inside specific measures using CROSSFILTER(..., BOTH). Scoping `CROSSFILTER(..., BOTH)` inside targeted measures avoids permanent bidirectional relationship ambiguity and protects unrelated core sales measures from bridge-table performance overhead. Scoping CROSSFILTER(..., BOTH) inside a DAX measure over a bridge table satisfies many-to-many attribution without turning on permanent model-wide bidirectional relationships that cause ambiguity and performance degradation. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Why the keyed choice wins: Scoping `CROSSFILTER(..., BOTH)` inside targeted measures avoids permanent bidirectional relationship ambiguity and protects unrelated core sales measures from bridge-table performance overhead.
- **B:** Correct. Scoping CROSSFILTER(..., BOTH) inside a DAX measure over a bridge table satisfies many-to-many attribution without turning on permanent model-wide bidirectional relationships that cause ambiguity and performance degradation. In this scenario: Scoping `CROSSFILTER(..., BOTH)` inside targeted measures avoids permanent bidirectional relationship ambiguity and protects unrelated core sales measures from bridge-table performance overhead.
- **C:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Scoping `CROSSFILTER(..., BOTH)` inside targeted measures avoids permanent bidirectional relationship ambiguity and protects unrelated core sales measures from bridge-table performance overhead.
- **D:** Incorrect for this requirement. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Why the keyed choice wins: Scoping `CROSSFILTER(..., BOTH)` inside targeted measures avoids permanent bidirectional relationship ambiguity and protects unrelated core sales measures from bridge-table performance overhead.

### Question 72 — D

Answer: Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid. `Assume referential integrity` instructs the DirectQuery SQL generator to emit `INNER JOIN` clauses when non-null foreign-key integrity is guaranteed. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: `Assume referential integrity` instructs the DirectQuery SQL generator to emit `INNER JOIN` clauses when non-null foreign-key integrity is guaranteed.
- **B:** Incorrect for this requirement. Setting DirectLakeBehavior to DirectLakeOnly (on Direct Lake on SQL models) prevents unexpected DirectQuery fallback spikes on the SQL endpoint when guardrails or SQL views/RLS are encountered. Why the keyed choice wins: `Assume referential integrity` instructs the DirectQuery SQL generator to emit `INNER JOIN` clauses when non-null foreign-key integrity is guaranteed.
- **C:** Incorrect for this requirement. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. Why the keyed choice wins: `Assume referential integrity` instructs the DirectQuery SQL generator to emit `INNER JOIN` clauses when non-null foreign-key integrity is guaranteed.
- **D:** Correct. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. In this scenario: `Assume referential integrity` instructs the DirectQuery SQL generator to emit `INNER JOIN` clauses when non-null foreign-key integrity is guaranteed.

### Question 73 — B

Answer: Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table. Aggregating before multiplying ignores volume weighting per SKU; `SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct]))` multiplies at line grain in flight. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Aggregating before multiplying ignores volume weighting per SKU; `SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct]))` multiplies at line grain in flight.
- **B:** Correct. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. In this scenario: Aggregating before multiplying ignores volume weighting per SKU; `SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct]))` multiplies at line grain in flight.
- **C:** Incorrect for this requirement. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. Why the keyed choice wins: Aggregating before multiplying ignores volume weighting per SKU; `SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct]))` multiplies at line grain in flight.
- **D:** Incorrect for this requirement. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Why the keyed choice wins: Aggregating before multiplying ignores volume weighting per SKU; `SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct]))` multiplies at line grain in flight.

### Question 74 — C

Answer: Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches. Assigning `VAR CurrentMargin = [Net Margin]` once before `RETURN` caches the scalar result in the current filter context and reuses it across every `IF` branch. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Assigning `VAR CurrentMargin = [Net Margin]` once before `RETURN` caches the scalar result in the current filter context and reuses it across every `IF` branch.
- **B:** Incorrect for this requirement. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Why the keyed choice wins: Assigning `VAR CurrentMargin = [Net Margin]` once before `RETURN` caches the scalar result in the current filter context and reuses it across every `IF` branch.
- **C:** Correct. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. In this scenario: Assigning `VAR CurrentMargin = [Net Margin]` once before `RETURN` caches the scalar result in the current filter context and reuses it across every `IF` branch.
- **D:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: Assigning `VAR CurrentMargin = [Net Margin]` once before `RETURN` caches the scalar result in the current filter context and reuses it across every `IF` branch.

### Question 75 — A

Answer: IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK()). `IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK())` checks whether `SKU` is actively grouping the current visual row, unlike `HASONEVALUE` which returns `TRUE` on single-SKU department subtotals. ISINSCOPE('DimProduct'[SKU]) evaluates TRUE only when SKU is actively grouping the visual hierarchy level, suppressing misleading margin figures at subtotal rows. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Correct. ISINSCOPE('DimProduct'[SKU]) evaluates TRUE only when SKU is actively grouping the visual hierarchy level, suppressing misleading margin figures at subtotal rows. In this scenario: `IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK())` checks whether `SKU` is actively grouping the current visual row, unlike `HASONEVALUE` which returns `TRUE` on single-SKU department subtotals.
- **B:** Incorrect for this requirement. INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags. Why the keyed choice wins: `IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK())` checks whether `SKU` is actively grouping the current visual row, unlike `HASONEVALUE` which returns `TRUE` on single-SKU department subtotals.
- **C:** Incorrect for this requirement. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Why the keyed choice wins: `IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK())` checks whether `SKU` is actively grouping the current visual row, unlike `HASONEVALUE` which returns `TRUE` on single-SKU department subtotals.
- **D:** Incorrect for this requirement. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Why the keyed choice wins: `IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK())` checks whether `SKU` is actively grouping the current visual row, unlike `HASONEVALUE` which returns `TRUE` on single-SKU department subtotals.

### Question 76 — A, B

Answers: Pass simple column predicates wrapped in KEEPFILTERS(DimProduct[Color] = "Red") to CALCULATE instead of FILTER(ALL(FactSales), ...); CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC))). `KEEPFILTERS(DimProduct[Color] = "Red")` intersects with existing slicer context without scanning the whole fact table, and `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` shifts one custom fiscal period cleanly. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Correct. OFFSET(-1, ..., ORDERBY(...)) shifts one period backward along a custom 4-4-5 fiscal sort column where standard Gregorian DATEADD fails. In this scenario: `KEEPFILTERS(DimProduct[Color] = "Red")` intersects with existing slicer context without scanning the whole fact table, and `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` shifts one custom fiscal period cleanly.
- **B:** Correct. KEEPFILTERS intersects the predicate with existing report slicer selections rather than overwriting them, and filtering a dimension column avoids scanning the entire multi-million-row fact table in the Formula Engine. In this scenario: `KEEPFILTERS(DimProduct[Color] = "Red")` intersects with existing slicer context without scanning the whole fact table, and `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` shifts one custom fiscal period cleanly.
- **C:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: `KEEPFILTERS(DimProduct[Color] = "Red")` intersects with existing slicer context without scanning the whole fact table, and `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` shifts one custom fiscal period cleanly.
- **D:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: `KEEPFILTERS(DimProduct[Color] = "Red")` intersects with existing slicer context without scanning the whole fact table, and `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` shifts one custom fiscal period cleanly.
- **E:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: `KEEPFILTERS(DimProduct[Color] = "Red")` intersects with existing slicer context without scanning the whole fact table, and `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` shifts one custom fiscal period cleanly.

### Question 77 — C

Answer: IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING()). `IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())` returns the dynamic format mask while preserving numeric values and base measure formatting. Dynamic format string expressions return a format mask string while preserving the measure's underlying numeric type; SELECTEDMEASUREFORMATSTRING() preserves the base measure's native currency/decimal mask. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Why the keyed choice wins: `IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())` returns the dynamic format mask while preserving numeric values and base measure formatting.
- **B:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: `IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())` returns the dynamic format mask while preserving numeric values and base measure formatting.
- **C:** Correct. Dynamic format string expressions return a format mask string while preserving the measure's underlying numeric type; SELECTEDMEASUREFORMATSTRING() preserves the base measure's native currency/decimal mask. In this scenario: `IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())` returns the dynamic format mask while preserving numeric values and base measure formatting.
- **D:** Incorrect for this requirement. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Why the keyed choice wins: `IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())` returns the dynamic format mask while preserving numeric values and base measure formatting.

### Question 78 — C

Answer: Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer. A Field Parameter table referencing the four columns via `NAMEOF()` and placed in the matrix Rows well dynamically swaps the grouping column based on slicer selection. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: A Field Parameter table referencing the four columns via `NAMEOF()` and placed in the matrix Rows well dynamically swaps the grouping column based on slicer selection.
- **B:** Incorrect for this requirement. A single Calculation Group applies reusable logic (YTD, PY, YoY%, Moving Avg) across dozens of base measures via SELECTEDMEASURE(), eliminating measure explosion (`50 base * 6 time calcs = 300 measures`). Why the keyed choice wins: A Field Parameter table referencing the four columns via `NAMEOF()` and placed in the matrix Rows well dynamically swaps the grouping column based on slicer selection.
- **C:** Correct. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. In this scenario: A Field Parameter table referencing the four columns via `NAMEOF()` and placed in the matrix Rows well dynamically swaps the grouping column based on slicer selection.
- **D:** Incorrect for this requirement. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Why the keyed choice wins: A Field Parameter table referencing the four columns via `NAMEOF()` and placed in the matrix Rows well dynamically swaps the grouping column based on slicer selection.

### Question 79 — B

Answer: Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat). Enabling `Large semantic model storage format` allows semantic models to exceed the default compressed size boundary up to the Fabric capacity's max memory per model and enables on-demand segment paging. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Local study-map skill 3.6 (Identify Use Cases for and Configure Large Semantic Model Storage Format), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Large semantic models in Microsoft Fabric & Power BI Premium (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-large-models).

- **A:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Enabling `Large semantic model storage format` allows semantic models to exceed the default compressed size boundary up to the Fabric capacity's max memory per model and enables on-demand segment paging.
- **B:** Correct. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. In this scenario: Enabling `Large semantic model storage format` allows semantic models to exceed the default compressed size boundary up to the Fabric capacity's max memory per model and enables on-demand segment paging.
- **C:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Enabling `Large semantic model storage format` allows semantic models to exceed the default compressed size boundary up to the Fabric capacity's max memory per model and enables on-demand segment paging.
- **D:** Incorrect for this requirement. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Why the keyed choice wins: Enabling `Large semantic model storage format` allows semantic models to exceed the default compressed size boundary up to the Fabric capacity's max memory per model and enables on-demand segment paging.

### Question 80 — A

Answer: Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat). Large semantic model storage format upgrades segment metadata handling and significantly accelerates XMLA write/deployment operations for external ALM tools. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Local study-map skill 3.6 (Identify Use Cases for and Configure Large Semantic Model Storage Format), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Large semantic models in Microsoft Fabric & Power BI Premium (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-large-models).

- **A:** Correct. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. In this scenario: Large semantic model storage format upgrades segment metadata handling and significantly accelerates XMLA write/deployment operations for external ALM tools.
- **B:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Large semantic model storage format upgrades segment metadata handling and significantly accelerates XMLA write/deployment operations for external ALM tools.
- **C:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Large semantic model storage format upgrades segment metadata handling and significantly accelerates XMLA write/deployment operations for external ALM tools.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Large semantic model storage format upgrades segment metadata handling and significantly accelerates XMLA write/deployment operations for external ALM tools.

### Question 81 — D, E

Answers: Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table; Create a local composite model using DirectQuery for Power BI semantic models and Analysis Services to combine a certified core semantic model with a departmental Excel/SQL table. User-defined `Import` aggregation tables satisfy high-level DirectQuery groupings in memory, and `DirectQuery for Power BI semantic models` extends a shared model locally via a composite chain. Local study-map skill 3.7 (Design and Build Composite Models (Direct Lake on OneLake + Import, Dual + Aggregations, DirectQuery over PBI)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use composite models in Power BI Desktop & Direct Lake on OneLake composite models (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-web-modeling).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: User-defined `Import` aggregation tables satisfy high-level DirectQuery groupings in memory, and `DirectQuery for Power BI semantic models` extends a shared model locally via a composite chain.
- **B:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: User-defined `Import` aggregation tables satisfy high-level DirectQuery groupings in memory, and `DirectQuery for Power BI semantic models` extends a shared model locally via a composite chain.
- **C:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: User-defined `Import` aggregation tables satisfy high-level DirectQuery groupings in memory, and `DirectQuery for Power BI semantic models` extends a shared model locally via a composite chain.
- **D:** Correct. User-defined Import aggregations satisfy high-level grouped queries purely from in-memory VertiPaq cache and automatically route only unaggregated detail drill-throughs to the underlying DirectQuery source. In this scenario: User-defined `Import` aggregation tables satisfy high-level DirectQuery groupings in memory, and `DirectQuery for Power BI semantic models` extends a shared model locally via a composite chain.
- **E:** Correct. Connecting to an existing shared semantic model in DirectQuery mode creates a local composite model (using remote model chains and limited cross-island relationships) so analysts can extend governed enterprise measures without copying the core model. In this scenario: User-defined `Import` aggregation tables satisfy high-level DirectQuery groupings in memory, and `DirectQuery for Power BI semantic models` extends a shared model locally via a composite chain.

### Question 82 — D

Answer: Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages. Enabling `Query reduction` -> `Add an Apply button to each single/multi-select slicer` batches all 8 checkbox selections into a single query fired on `Apply`. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Local study-map skill 3.8 (Implement Performance Improvements in Queries and Report Visuals (Performance Analyzer & Query Reduction)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use Performance Analyzer to examine report element performance in Power BI (https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer).

- **A:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Enabling `Query reduction` -> `Add an Apply button to each single/multi-select slicer` batches all 8 checkbox selections into a single query fired on `Apply`.
- **B:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Enabling `Query reduction` -> `Add an Apply button to each single/multi-select slicer` batches all 8 checkbox selections into a single query fired on `Apply`.
- **C:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: Enabling `Query reduction` -> `Add an Apply button to each single/multi-select slicer` batches all 8 checkbox selections into a single query fired on `Apply`.
- **D:** Correct. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. In this scenario: Enabling `Query reduction` -> `Add an Apply button to each single/multi-select slicer` batches all 8 checkbox selections into a single query fired on `Apply`.

### Question 83 — A

Answer: Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time. Dropping unused `POSReceiptGUID` and splitting `ScanTimestampMs` into separate `ScanDate` (`~1,500` unique values) and `ScanTimeSecond` (`86,400` unique values) columns slashes dictionary cardinality by orders of magnitude. Columnar memory in VertiPaq and Direct Lake transcoding scales primarily with column cardinality rather than row count; dropping unused GUIDs or splitting millisecond timestamps into separate Date and Time columns cuts memory dramatically. Local study-map skill 3.9 (Improve DAX and Model Performance Using DAX Studio Server Timings (FE vs SE) and VertiPaq Cardinality Reduction), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Optimization guide for Power BI — DAX Formula Engine vs Storage Engine & VertiPaq (https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization).

- **A:** Correct. Columnar memory in VertiPaq and Direct Lake transcoding scales primarily with column cardinality rather than row count; dropping unused GUIDs or splitting millisecond timestamps into separate Date and Time columns cuts memory dramatically. In this scenario: Dropping unused `POSReceiptGUID` and splitting `ScanTimestampMs` into separate `ScanDate` (`~1,500` unique values) and `ScanTimeSecond` (`86,400` unique values) columns slashes dictionary cardinality by orders of magnitude.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Dropping unused `POSReceiptGUID` and splitting `ScanTimestampMs` into separate `ScanDate` (`~1,500` unique values) and `ScanTimeSecond` (`86,400` unique values) columns slashes dictionary cardinality by orders of magnitude.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Dropping unused `POSReceiptGUID` and splitting `ScanTimestampMs` into separate `ScanDate` (`~1,500` unique values) and `ScanTimeSecond` (`86,400` unique values) columns slashes dictionary cardinality by orders of magnitude.
- **D:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: Dropping unused `POSReceiptGUID` and splitting `ScanTimestampMs` into separate `ScanDate` (`~1,500` unique values) and `ScanTimeSecond` (`86,400` unique values) columns slashes dictionary cardinality by orders of magnitude.

### Question 84 — D

Answer: Capture visual timings in Performance Analyzer → Profile captured DAX in DAX Studio with Server Timings and Query Plan → Refactor FILTER(Fact,...) into VAR-cached SE column predicates and run V-Order OPTIMIZE → Re-test with Clear Cache. Isolating the visual's DAX query in Performance Analyzer, profiling FE/SE and fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing with `Clear Cache` verifies true cold-cache gains. Correct order: isolate visual vs DAX queue time in Performance Analyzer, profile FE/SE and Direct Lake fallback in DAX Studio Server Timings, fix DAX anti-patterns + Delta Parquet layout, and benchmark cold-cache results. Local study-map skill 3.9 (Improve DAX and Model Performance Using DAX Studio Server Timings (FE vs SE) and VertiPaq Cardinality Reduction), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Optimization guide for Power BI — DAX Formula Engine vs Storage Engine & VertiPaq (https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization).

- **A:** Incorrect for this requirement. Incorrect: snowflaking and Auto date/time increase relationship hops and memory overhead rather than resolving FE/SE bottlenecks. Why the keyed choice wins: Isolating the visual's DAX query in Performance Analyzer, profiling FE/SE and fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing with `Clear Cache` verifies true cold-cache gains.
- **B:** Incorrect for this requirement. Incorrect: benchmarking warm cache hides real SE/transcoding cost, GUID columns bloat dictionaries, DirectQueryOnly slows visuals, and 45 cards create visual-queue contention. Why the keyed choice wins: Isolating the visual's DAX query in Performance Analyzer, profiling FE/SE and fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing with `Clear Cache` verifies true cold-cache gains.
- **C:** Incorrect for this requirement. Incorrect: scaling capacity blindly wastes budget while bidirectional joins, FORMAT() strings, and disabled V-Order make FE and transcoding slower. Why the keyed choice wins: Isolating the visual's DAX query in Performance Analyzer, profiling FE/SE and fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing with `Clear Cache` verifies true cold-cache gains.
- **D:** Correct. Correct order: isolate visual vs DAX queue time in Performance Analyzer, profile FE/SE and Direct Lake fallback in DAX Studio Server Timings, fix DAX anti-patterns + Delta Parquet layout, and benchmark cold-cache results. In this scenario: Isolating the visual's DAX query in Performance Analyzer, profiling FE/SE and fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing with `Clear Cache` verifies true cold-cache gains.

### Question 85 — C

Answer: Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes. Direct Lake queries read the Parquet file snapshot captured at the last framing baseline; triggering a Direct Lake framing refresh updates the Delta log pointer in seconds so new files transcode on demand. Framing is a fast metadata-only operation updating the Direct Lake model's pointer to the latest Delta transaction log Parquet files and evicting stale resident columns so new ETL rows become visible consistently. Local study-map skill 3.10 (Configure Direct Lake Framing, Transcoding, V-Order/OPTIMIZE Guardrails, and DirectLakeBehavior Fallback), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: How Direct Lake works (framing, transcoding, V-Order, fallback & DirectLakeBehavior) (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works).

- **A:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: Direct Lake queries read the Parquet file snapshot captured at the last framing baseline; triggering a Direct Lake framing refresh updates the Delta log pointer in seconds so new files transcode on demand.
- **B:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Direct Lake queries read the Parquet file snapshot captured at the last framing baseline; triggering a Direct Lake framing refresh updates the Delta log pointer in seconds so new files transcode on demand.
- **C:** Correct. Framing is a fast metadata-only operation updating the Direct Lake model's pointer to the latest Delta transaction log Parquet files and evicting stale resident columns so new ETL rows become visible consistently. In this scenario: Direct Lake queries read the Parquet file snapshot captured at the last framing baseline; triggering a Direct Lake framing refresh updates the Delta log pointer in seconds so new files transcode on demand.
- **D:** Incorrect for this requirement. Direct Lake on OneLake operates exclusively in DirectLakeOnly mode and never falls back to DirectQuery; exceeding capacity guardrails fails framing/queries until Delta tables or SKU sizing are optimized. Why the keyed choice wins: Direct Lake queries read the Parquet file snapshot captured at the last framing baseline; triggering a Direct Lake framing refresh updates the Delta log pointer in seconds so new files transcode on demand.

### Question 86 — C, D, F

Answers: Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails; Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes; Set DirectLakeBehavior = DirectLakeOnly on a Direct Lake on SQL semantic model so queries fail fast instead of silently falling back to slow DirectQuery. Applying V-Order + `OPTIMIZE` compacts Delta rowgroups within SKU guardrails, explicit framing refreshes control snapshot visibility after ETL, and `DirectLakeBehavior = DirectLakeOnly` blocks silent DirectQuery fallback. Local study-map skill 3.10 (Configure Direct Lake Framing, Transcoding, V-Order/OPTIMIZE Guardrails, and DirectLakeBehavior Fallback), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: How Direct Lake works (framing, transcoding, V-Order, fallback & DirectLakeBehavior) (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works).

- **A:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Applying V-Order + `OPTIMIZE` compacts Delta rowgroups within SKU guardrails, explicit framing refreshes control snapshot visibility after ETL, and `DirectLakeBehavior = DirectLakeOnly` blocks silent DirectQuery fallback.
- **B:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Applying V-Order + `OPTIMIZE` compacts Delta rowgroups within SKU guardrails, explicit framing refreshes control snapshot visibility after ETL, and `DirectLakeBehavior = DirectLakeOnly` blocks silent DirectQuery fallback.
- **C:** Correct. Framing is a fast metadata-only operation updating the Direct Lake model's pointer to the latest Delta transaction log Parquet files and evicting stale resident columns so new ETL rows become visible consistently. In this scenario: Applying V-Order + `OPTIMIZE` compacts Delta rowgroups within SKU guardrails, explicit framing refreshes control snapshot visibility after ETL, and `DirectLakeBehavior = DirectLakeOnly` blocks silent DirectQuery fallback.
- **D:** Correct. Setting DirectLakeBehavior to DirectLakeOnly (on Direct Lake on SQL models) prevents unexpected DirectQuery fallback spikes on the SQL endpoint when guardrails or SQL views/RLS are encountered. In this scenario: Applying V-Order + `OPTIMIZE` compacts Delta rowgroups within SKU guardrails, explicit framing refreshes control snapshot visibility after ETL, and `DirectLakeBehavior = DirectLakeOnly` blocks silent DirectQuery fallback.
- **E:** Incorrect for this requirement. Direct Lake on OneLake operates exclusively in DirectLakeOnly mode and never falls back to DirectQuery; exceeding capacity guardrails fails framing/queries until Delta tables or SKU sizing are optimized. Why the keyed choice wins: Applying V-Order + `OPTIMIZE` compacts Delta rowgroups within SKU guardrails, explicit framing refreshes control snapshot visibility after ETL, and `DirectLakeBehavior = DirectLakeOnly` blocks silent DirectQuery fallback.
- **F:** Correct. Hundreds of tiny streaming Parquet files inflate Delta rowgroup counts past Fabric SKU guardrails and degrade transcoding; OPTIMIZE compacts files into large V-Order-sorted rowgroups optimized for VertiPaq in-memory compression. In this scenario: Applying V-Order + `OPTIMIZE` compacts Delta rowgroups within SKU guardrails, explicit framing refreshes control snapshot visibility after ETL, and `DirectLakeBehavior = DirectLakeOnly` blocks silent DirectQuery fallback.

### Question 87 — B

Answer: Live edit the model in Power BI Desktop and save a Version history point → Script the semantic model in TMDL view → Replace Sql.Database(...) with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...") → Apply TMDL and run framing refresh. Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the upgrade in place. Correct order: take a version history checkpoint while live editing, script the model in TMDL view, swap the shared M expression from Sql.Database to AzureStorage.DataLake OneLake URL, apply changes, and frame. Local study-map skill 3.11 (Choose Between Direct Lake on OneLake and Direct Lake on SQL Analytics Endpoint (and Migrate via TMDL)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Direct Lake overview: Direct Lake on OneLake vs Direct Lake on SQL analytics endpoint (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview).

- **A:** Incorrect for this requirement. Incorrect: Direct Lake on OneLake does not support non-materialized SQL views, DirectQuery fallback, or gateways. Why the keyed choice wins: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the upgrade in place.
- **B:** Correct. Correct order: take a version history checkpoint while live editing, script the model in TMDL view, swap the shared M expression from Sql.Database to AzureStorage.DataLake OneLake URL, apply changes, and frame. In this scenario: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the upgrade in place.
- **C:** Incorrect for this requirement. Incorrect: Direct Lake models are live-edited in workspaces (not offline Personal Workspace Import files), and OleDb breaks OneLake Direct Lake connectivity. Why the keyed choice wins: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the upgrade in place.
- **D:** Incorrect for this requirement. Incorrect: deleting the semantic model breaks downstream thin reports and lineage, and granting Workspace Admin violates security. Why the keyed choice wins: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the upgrade in place.

### Question 88 — D

Answer: Create case-sensitive DateTime parameters RangeStart and RangeEnd → Apply foldable half-open filter (>= RangeStart and < RangeEnd) → Configure table Incremental refresh policy → Publish to workspace and run initial refresh to generate partitions. Defining exact `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart` and `< RangeEnd` filters, setting the table policy, and publishing for initial partition generation implements incremental refresh cleanly. Correct order: define DateTime RangeStart/RangeEnd parameters, apply >= RangeStart and < RangeEnd preserving query folding, configure table incremental policy, and publish so Fabric generates historical and incremental partitions. Local study-map skill 3.12 (Implement Incremental Refresh and Hybrid Real-Time Partitions (RangeStart/RangeEnd, Detect Data Changes)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Configure incremental refresh and real-time data for Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-overview).

- **A:** Incorrect for this requirement. Incorrect: Detect data changes requires an audit/update timestamp column distinct from the date column used to partition RangeStart/RangeEnd. Why the keyed choice wins: Defining exact `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart` and `< RangeEnd` filters, setting the table policy, and publishing for initial partition generation implements incremental refresh cleanly.
- **B:** Incorrect for this requirement. Incorrect: parameter names/types must be exact DateTime RangeStart and RangeEnd, breaking query folding pulls the entire table on every refresh, and <= on both bounds double-counts midnight rows. Why the keyed choice wins: Defining exact `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart` and `< RangeEnd` filters, setting the table policy, and publishing for initial partition generation implements incremental refresh cleanly.
- **C:** Incorrect for this requirement. Incorrect: importing 2 billion rows locally crashes Desktop before partitioning exists, RangeStart belongs in Power Query M, and Incremental Refresh partitions apply to Import/Hybrid tables rather than Direct Lake. Why the keyed choice wins: Defining exact `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart` and `< RangeEnd` filters, setting the table policy, and publishing for initial partition generation implements incremental refresh cleanly.
- **D:** Correct. Correct order: define DateTime RangeStart/RangeEnd parameters, apply >= RangeStart and < RangeEnd preserving query folding, configure table incremental policy, and publish so Fabric generates historical and incremental partitions. In this scenario: Defining exact `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart` and `< RangeEnd` filters, setting the table policy, and publishing for initial partition generation implements incremental refresh cleanly.

### Question 89 — C

Answer: Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns. SCD Type 2 versions each merchant category change with a new surrogate key and `EffectiveStartDate`/`EffectiveEndDate` window so historical fact rows retain exact point-in-time attribution. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Why the keyed choice wins: SCD Type 2 versions each merchant category change with a new surrogate key and `EffectiveStartDate`/`EffectiveEndDate` window so historical fact rows retain exact point-in-time attribution.
- **B:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: SCD Type 2 versions each merchant category change with a new surrogate key and `EffectiveStartDate`/`EffectiveEndDate` window so historical fact rows retain exact point-in-time attribution.
- **C:** Correct. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. In this scenario: SCD Type 2 versions each merchant category change with a new surrogate key and `EffectiveStartDate`/`EffectiveEndDate` window so historical fact rows retain exact point-in-time attribution.
- **D:** Incorrect for this requirement. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Why the keyed choice wins: SCD Type 2 versions each merchant category change with a new surrogate key and `EffectiveStartDate`/`EffectiveEndDate` window so historical fact rows retain exact point-in-time attribution.

### Question 90 — B

Answer: Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE. Mapping unmatched or NULL foreign keys via `COALESCE` to a dedicated `-1` Unknown surrogate row in `DimMerchant` preserves fact totals and maintains valid `1:*` Direct Lake relationships. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. Why the keyed choice wins: Mapping unmatched or NULL foreign keys via `COALESCE` to a dedicated `-1` Unknown surrogate row in `DimMerchant` preserves fact totals and maintains valid `1:*` Direct Lake relationships.
- **B:** Correct. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. In this scenario: Mapping unmatched or NULL foreign keys via `COALESCE` to a dedicated `-1` Unknown surrogate row in `DimMerchant` preserves fact totals and maintains valid `1:*` Direct Lake relationships.
- **C:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: Mapping unmatched or NULL foreign keys via `COALESCE` to a dedicated `-1` Unknown surrogate row in `DimMerchant` preserves fact totals and maintains valid `1:*` Direct Lake relationships.
- **D:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Mapping unmatched or NULL foreign keys via `COALESCE` to a dedicated `-1` Unknown surrogate row in `DimMerchant` preserves fact totals and maintains valid `1:*` Direct Lake relationships.

### Question 91 — C

Answer: Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension. Denormalizing Brand, Subcategory, and Category attributes onto a single flattened Gold `DimItem` table removes snowflaked relationship hops and accelerates Direct Lake filtering. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Local study-map skill 2.9 (Denormalize Snowflake Hierarchies into Flattened Gold Dimension Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Dimensional modeling & denormalizing snowflake tables in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables).

- **A:** Incorrect for this requirement. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Why the keyed choice wins: Denormalizing Brand, Subcategory, and Category attributes onto a single flattened Gold `DimItem` table removes snowflaked relationship hops and accelerates Direct Lake filtering.
- **B:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Denormalizing Brand, Subcategory, and Category attributes onto a single flattened Gold `DimItem` table removes snowflaked relationship hops and accelerates Direct Lake filtering.
- **C:** Correct. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. In this scenario: Denormalizing Brand, Subcategory, and Category attributes onto a single flattened Gold `DimItem` table removes snowflaked relationship hops and accelerates Direct Lake filtering.
- **D:** Incorrect for this requirement. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Why the keyed choice wins: Denormalizing Brand, Subcategory, and Category attributes onto a single flattened Gold `DimItem` table removes snowflaked relationship hops and accelerates Direct Lake filtering.

### Question 92 — A

Answer: Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions. Saving as a Power BI Project (`.pbip`) stores the semantic model as text-based TMDL files and report visuals as PBIR JSON files for clean Git pull-request diffs and merges. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. Local study-map skill 1.7 (Create and Manage Power BI Desktop Projects (.pbip) with TMDL, PBIR, and .gitignore Hygiene), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Power BI Desktop projects (.pbip), TMDL, and PBIR (https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview).

- **A:** Correct. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. In this scenario: Saving as a Power BI Project (`.pbip`) stores the semantic model as text-based TMDL files and report visuals as PBIR JSON files for clean Git pull-request diffs and merges.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Saving as a Power BI Project (`.pbip`) stores the semantic model as text-based TMDL files and report visuals as PBIR JSON files for clean Git pull-request diffs and merges.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Saving as a Power BI Project (`.pbip`) stores the semantic model as text-based TMDL files and report visuals as PBIR JSON files for clean Git pull-request diffs and merges.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Saving as a Power BI Project (`.pbip`) stores the semantic model as text-based TMDL files and report visuals as PBIR JSON files for clean Git pull-request diffs and merges.

### Question 93 — D

Answer: Create a Calculation Group with Calculation Items referencing SELECTEDMEASURE() and explicit Precedence ordering (automatically setting DiscourageImplicitMeasures = true). A Calculation Group using `SELECTEDMEASURE()` paired with Dynamic Format Strings (`SELECTEDMEASUREFORMATSTRING()` / `"0.0%"`) applies all four time calculations without converting numbers to text via `FORMAT()`. A single Calculation Group applies reusable logic (YTD, PY, YoY%, Moving Avg) across dozens of base measures via SELECTEDMEASURE(), eliminating measure explosion (`50 base * 6 time calcs = 300 measures`). Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: A Calculation Group using `SELECTEDMEASURE()` paired with Dynamic Format Strings (`SELECTEDMEASUREFORMATSTRING()` / `"0.0%"`) applies all four time calculations without converting numbers to text via `FORMAT()`.
- **B:** Incorrect for this requirement. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Why the keyed choice wins: A Calculation Group using `SELECTEDMEASURE()` paired with Dynamic Format Strings (`SELECTEDMEASUREFORMATSTRING()` / `"0.0%"`) applies all four time calculations without converting numbers to text via `FORMAT()`.
- **C:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: A Calculation Group using `SELECTEDMEASURE()` paired with Dynamic Format Strings (`SELECTEDMEASUREFORMATSTRING()` / `"0.0%"`) applies all four time calculations without converting numbers to text via `FORMAT()`.
- **D:** Correct. A single Calculation Group applies reusable logic (YTD, PY, YoY%, Moving Avg) across dozens of base measures via SELECTEDMEASURE(), eliminating measure explosion (`50 base * 6 time calcs = 300 measures`). In this scenario: A Calculation Group using `SELECTEDMEASURE()` paired with Dynamic Format Strings (`SELECTEDMEASUREFORMATSTRING()` / `"0.0%"`) applies all four time calculations without converting numbers to text via `FORMAT()`.

### Question 94 — B

Answer: Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time. Performance Analyzer separates `DAX query`, `Visual display`, and `Other` queue wait time, confirming that 38 separate card visuals bottleneck on single-threaded visual container queuing; consolidating into fewer multi-measure matrix/card visuals resolves it. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Local study-map skill 3.8 (Implement Performance Improvements in Queries and Report Visuals (Performance Analyzer & Query Reduction)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use Performance Analyzer to examine report element performance in Power BI (https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer).

- **A:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Performance Analyzer separates `DAX query`, `Visual display`, and `Other` queue wait time, confirming that 38 separate card visuals bottleneck on single-threaded visual container queuing; consolidating into fewer multi-measure matrix/card visuals resolves it.
- **B:** Correct. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. In this scenario: Performance Analyzer separates `DAX query`, `Visual display`, and `Other` queue wait time, confirming that 38 separate card visuals bottleneck on single-threaded visual container queuing; consolidating into fewer multi-measure matrix/card visuals resolves it.
- **C:** Incorrect for this requirement. Hundreds of tiny streaming Parquet files inflate Delta rowgroup counts past Fabric SKU guardrails and degrade transcoding; OPTIMIZE compacts files into large V-Order-sorted rowgroups optimized for VertiPaq in-memory compression. Why the keyed choice wins: Performance Analyzer separates `DAX query`, `Visual display`, and `Other` queue wait time, confirming that 38 separate card visuals bottleneck on single-threaded visual container queuing; consolidating into fewer multi-measure matrix/card visuals resolves it.
- **D:** Incorrect for this requirement. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Why the keyed choice wins: Performance Analyzer separates `DAX query`, `Visual display`, and `Other` queue wait time, confirming that 38 separate card visuals bottleneck on single-threaded visual container queuing; consolidating into fewer multi-measure matrix/card visuals resolves it.

### Question 95 — C

Answer: Ingest streaming telemetry into an Eventhouse KQL database → Enable OneLake availability on the KQL database or table → Create an internal OneLake shortcut in the Lakehouse → Add the table to a Direct Lake on OneLake semantic model. Enabling OneLake availability on the KQL database/table writes logical Delta Parquet files to OneLake that Lakehouse shortcuts and Direct Lake on OneLake models consume directly. Correct order: land streaming events in Eventhouse, opt in to OneLake availability so Delta Parquet files sync to OneLake, surface via Lakehouse shortcut (or connect directly), and model with Direct Lake on OneLake. Local study-map skill 2.5 (Implement OneLake Integration for Eventhouse (OneLake Availability) and Import Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Eventhouse OneLake availability & OneLake integration for semantic models (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/one-lake-availability).

- **A:** Incorrect for this requirement. Incorrect: manual hourly CSV exports add latency, operational toil, and duplicate storage instead of native Eventhouse OneLake availability. Why the keyed choice wins: Enabling OneLake availability on the KQL database/table writes logical Delta Parquet files to OneLake that Lakehouse shortcuts and Direct Lake on OneLake models consume directly.
- **B:** Incorrect for this requirement. Incorrect: KQL tables are internal OneLake sources that only expose Delta Parquet folders after OneLake availability is enabled. Why the keyed choice wins: Enabling OneLake availability on the KQL database/table writes logical Delta Parquet files to OneLake that Lakehouse shortcuts and Direct Lake on OneLake models consume directly.
- **C:** Correct. Correct order: land streaming events in Eventhouse, opt in to OneLake availability so Delta Parquet files sync to OneLake, surface via Lakehouse shortcut (or connect directly), and model with Direct Lake on OneLake. In this scenario: Enabling OneLake availability on the KQL database/table writes logical Delta Parquet files to OneLake that Lakehouse shortcuts and Direct Lake on OneLake models consume directly.
- **D:** Incorrect for this requirement. Incorrect: Direct Lake on SQL does not support KQL databases, disabling OneLake availability prevents Delta Parquet generation, and Direct Lake never uses gateways. Why the keyed choice wins: Enabling OneLake availability on the KQL database/table writes logical Delta Parquet files to OneLake that Lakehouse shortcuts and Direct Lake on OneLake models consume directly.

### Question 96 — C

Answer: | summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m). `| summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)` buckets streaming scanner timestamps into 5-minute windows and computes tail latency. percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse. Local study-map skill 2.17 (Select, Filter, and Aggregate Data Using KQL (summarize, bin, arg_max, percentile, parse_json, mv-expand)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query data in a KQL queryset in Microsoft Fabric Real-Time Intelligence (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/kql-queryset).

- **A:** Incorrect for this requirement. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Why the keyed choice wins: `| summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)` buckets streaming scanner timestamps into 5-minute windows and computes tail latency.
- **B:** Incorrect for this requirement. mv-expand unpacks a dynamic JSON array into one output row per array element while preserving parent event columns. Why the keyed choice wins: `| summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)` buckets streaming scanner timestamps into 5-minute windows and computes tail latency.
- **C:** Correct. percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse. In this scenario: `| summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)` buckets streaming scanner timestamps into 5-minute windows and computes tail latency.
- **D:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `| summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)` buckets streaming scanner timestamps into 5-minute windows and computes tail latency.

### Question 97 — D

Answer: Build a Direct Lake on OneLake composite semantic model combining Direct Lake fact tables from OneLake with Import dimension/target tables using regular relationships. A Direct Lake on OneLake composite model combines Delta tables across multiple Fabric items (including KQL databases with OneLake availability) alongside Import tables using regular relationships. Direct Lake on OneLake supports true composite models that mix Direct Lake tables from multiple Fabric items with Import tables from any Power Query connector while preserving fast regular (non-limited) relationships. Local study-map skill 3.7 (Design and Build Composite Models (Direct Lake on OneLake + Import, Dual + Aggregations, DirectQuery over PBI)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use composite models in Power BI Desktop & Direct Lake on OneLake composite models (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-web-modeling).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: A Direct Lake on OneLake composite model combines Delta tables across multiple Fabric items (including KQL databases with OneLake availability) alongside Import tables using regular relationships.
- **B:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: A Direct Lake on OneLake composite model combines Delta tables across multiple Fabric items (including KQL databases with OneLake availability) alongside Import tables using regular relationships.
- **C:** Incorrect for this requirement. Eventhouse KQL databases do not write Delta Parquet to OneLake unless OneLake availability is enabled, and Direct Lake on SQL does not support KQL databases (only Direct Lake on OneLake does once OneLake availability is on). Why the keyed choice wins: A Direct Lake on OneLake composite model combines Delta tables across multiple Fabric items (including KQL databases with OneLake availability) alongside Import tables using regular relationships.
- **D:** Correct. Direct Lake on OneLake supports true composite models that mix Direct Lake tables from multiple Fabric items with Import tables from any Power Query connector while preserving fast regular (non-limited) relationships. In this scenario: A Direct Lake on OneLake composite model combines Delta tables across multiple Fabric items (including KQL databases with OneLake availability) alongside Import tables using regular relationships.

### Question 98 — A

Answer: Define both the RLS filter and CLS column allow-list inside a single OneLake security Grant role with Read permission. Combining both the RLS row predicate and the CLS column allow-list inside a single Read Grant OneLake security role enforces their intersection cleanly across Spark, SQL, and Direct Lake without separate-role query errors. OneLake security supports Grant roles only (Read permission required for RLS/CLS) and requires combining RLS and CLS on the same table within a single role — separate RLS and CLS roles on the same table return query errors. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Correct. OneLake security supports Grant roles only (Read permission required for RLS/CLS) and requires combining RLS and CLS on the same table within a single role — separate RLS and CLS roles on the same table return query errors. In this scenario: Combining both the RLS row predicate and the CLS column allow-list inside a single Read Grant OneLake security role enforces their intersection cleanly across Spark, SQL, and Direct Lake without separate-role query errors.
- **B:** Incorrect for this requirement. OneLake security does not support combining an RLS role and a CLS role across separate roles on the same table; members assigned to that combination receive query errors. Why the keyed choice wins: Combining both the RLS row predicate and the CLS column allow-list inside a single Read Grant OneLake security role enforces their intersection cleanly across Spark, SQL, and Direct Lake without separate-role query errors.
- **C:** Incorrect for this requirement. OneLake security roles granting ReadWrite permission cannot contain RLS or CLS constraints; fine-grained row and column rules are supported only on Read roles. Why the keyed choice wins: Combining both the RLS row predicate and the CLS column allow-list inside a single Read Grant OneLake security role enforces their intersection cleanly across Spark, SQL, and Direct Lake without separate-role query errors.
- **D:** Incorrect for this requirement. OneLake security supports Grant roles only — there is no Deny role type, and OneLake security never restricts Workspace Admins, Members, or Contributors. Why the keyed choice wins: Combining both the RLS row predicate and the CLS column allow-list inside a single Read Grant OneLake security role enforces their intersection cleanly across Spark, SQL, and Direct Lake without separate-role query errors.

### Question 99 — D

Answer: Switch the Lakehouse SQL analytics endpoint to User's identity mode. Switching the Lakehouse SQL analytics endpoint to User's identity mode evaluates OneLake security roles per caller rather than executing under the owner's unrestricted identity. Setting the SQL analytics endpoint to User's identity mode evaluates OneLake security roles per caller across T-SQL and downstream shortcuts instead of running under the Lakehouse owner's fixed identity. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: Switching the Lakehouse SQL analytics endpoint to User's identity mode evaluates OneLake security roles per caller rather than executing under the owner's unrestricted identity.
- **B:** Incorrect for this requirement. Configuring a fixed-identity cloud connection (Service Principal or Workspace Identity) with SSO disabled lets report consumers query the Direct Lake model enforced by semantic-model RLS without granting them any direct Lakehouse or SQL endpoint permissions. Why the keyed choice wins: Switching the Lakehouse SQL analytics endpoint to User's identity mode evaluates OneLake security roles per caller rather than executing under the owner's unrestricted identity.
- **C:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: Switching the Lakehouse SQL analytics endpoint to User's identity mode evaluates OneLake security roles per caller rather than executing under the owner's unrestricted identity.
- **D:** Correct. Setting the SQL analytics endpoint to User's identity mode evaluates OneLake security roles per caller across T-SQL and downstream shortcuts instead of running under the Lakehouse owner's fixed identity. In this scenario: Switching the Lakehouse SQL analytics endpoint to User's identity mode evaluates OneLake security roles per caller rather than executing under the owner's unrestricted identity.

### Question 100 — B

Answer: Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop). Direct Lake on OneLake integrates natively with OneLake security OLS and RLS while serving queries directly from in-memory transcoded Delta columns without DirectQuery fallback. Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery. Local study-map skill 3.11 (Choose Between Direct Lake on OneLake and Direct Lake on SQL Analytics Endpoint (and Migrate via TMDL)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Direct Lake overview: Direct Lake on OneLake vs Direct Lake on SQL analytics endpoint (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Direct Lake on OneLake integrates natively with OneLake security OLS and RLS while serving queries directly from in-memory transcoded Delta columns without DirectQuery fallback.
- **B:** Correct. Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery. In this scenario: Direct Lake on OneLake integrates natively with OneLake security OLS and RLS while serving queries directly from in-memory transcoded Delta columns without DirectQuery fallback.
- **C:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Direct Lake on OneLake integrates natively with OneLake security OLS and RLS while serving queries directly from in-memory transcoded Delta columns without DirectQuery fallback.
- **D:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: Direct Lake on OneLake integrates natively with OneLake security OLS and RLS while serving queries directly from in-memory transcoded Delta columns without DirectQuery fallback.
