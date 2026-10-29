# Microsoft Exam DP-600: Implementing Analytics Solutions Using Microsoft Fabric — Full-Length Mock Exam 4

Exam DP-600 (Smart Manufacturing, Connected Fleet Telemetry, and Supply-Chain Composite Models) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint & Credential Notice:** Aligned to the official **October 19, 2026** DP-600 study guide (`Microsoft Certified: Fabric Analytics Engineer Associate`). Associate-level certification with **no prerequisite exam required**, free online annual renewal on Microsoft Learn, split-screen `learn.microsoft.com` access during non-lab exam sections, and hands-on coverage across **SQL**, **KQL**, **DAX**, **PySpark**, **Power Query M**, **TMDL**, and **TMSL**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` SQL/KQL/DAX/PySpark/M/TMDL/TMSL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Microsoft Fabric case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area SQL/KQL/DAX/TMDL dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn Fabric and Power BI documentation — never recalled live items or copied Microsoft sample case studies.

## Questions

### 1. An industrial IoT engineer must build and schedule Spark notebooks and Eventstreams in `FactoryOps-Dev` without sharing items externally or modifying workspace access lists. Which workspace role fits least privilege?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Member role
- B. Assign the Workspace Admin role
- C. Assign the Workspace Contributor role
- D. Assign the Workspace Viewer role

### 2. Proposed solution: Plant supervisors are granted `Workspace Contributor` in `Manufacturing-Prod` so they can view shift scrap reports filtered by OneLake security RLS. Why do supervisors see all plants, and what role fixes it?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Viewer role
- B. Assign the Workspace Contributor role
- C. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows
- D. Assign the Workspace Member role

### 3. Platform leads must initialize Azure DevOps Git integration on `SupplyChain-Dev`, manage workspace capacity assignments, and govern role membership via corporate identity groups. Which two choices apply? Select two.

Domain: Maintain a data analytics solution

- A. Assign permissions to Microsoft Entra security groups rather than individual users
- B. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows
- C. Assign the Workspace Viewer role
- D. Assign the Workspace Contributor role
- E. Assign the Workspace Admin role

### 4. Procurement analysts need to create ad-hoc PivotTables in Excel (`Analyze in Excel`) against the shared `SupplierSpend` semantic model without editing the model or seeing raw Lakehouse files. Which item permission is required?

Domain: Maintain a data analytics solution

- A. Share the item with ReadData (Read all SQL endpoint data) permission
- B. Share the Lakehouse with ReadAll (Read all Apache Spark data) permission
- C. Assign the Workspace Admin role
- D. Grant Build permission on the shared semantic model

### 5. Quality engineers view a Direct Lake warranty report via a Power BI App, and compliance forbids granting them any `Read` or `ReadAll` permissions on `WarrantyLakehouse`. How should the Direct Lake model connect to `WarrantyLakehouse`?

Domain: Maintain a data analytics solution

- A. Share the Lakehouse with ReadAll (Read all Apache Spark data) permission
- B. Assign the Workspace Contributor role
- C. Enable single sign-on (SSO) on the Direct Lake semantic model connection
- D. Bind the Direct Lake semantic model to a cloud connection with a fixed identity and disable SSO

### 6. Warehouse plant analysts connect directly via T-SQL clients to `PlantWarehouse` and must see only rows where `PlantManagerUPN = USER_NAME()` (`CREATE SECURITY POLICY ... ADD ____ ... WITH (STATE = ON)`). Which native T-SQL security mechanism enforces this inside the Warehouse?

Domain: Maintain a data analytics solution

- A. Create a OneLake security role with ReadWrite permission and attach an RLS predicate
- B. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- C. Mark the item as Promoted in item settings
- D. Create an inline table-valued predicate function with SCHEMABINDING and a CREATE SECURITY POLICY FILTER PREDICATE in the Warehouse

### 7. You secure `GlobalPartsLakehouse` with OneLake security roles consumed by four assembly-plant workspaces via internal OneLake shortcuts. Which four-step sequence enforces per-caller policies?

Domain: Maintain a data analytics solution

- A. Create downstream shortcuts first → Assign consumers Workspace Member rights → Attach RLS predicates to a ReadWrite OneLake role → Enable SSO on an On-premises gateway
- B. Enable OneLake security and define Read Grant roles → Assign consumers Workspace Viewer and OneLake security roles → Set SQL analytics endpoint to User's identity mode → Expose downstream shortcuts in User's identity mode
- C. Assign consumers the Workspace Contributor role → Enable OneLake security with a Deny role → Keep SQL analytics endpoint in Owner fixed identity mode → Create downstream shortcuts
- D. Set SQL analytics endpoint to Delegated mode with SQL DENY rules → Remove Workspace Viewer assignments → Enable OneLake security afterward → Export binary .pbix copies

### 8. On `RoboticsLakehouse`, supplier engineers need (1) `Read` access only to `Files/cad_specs/v2/` without seeing `Files/payroll/`, and (2) both row filtering (`VendorId = 44`) and column hiding (`InternalCost`) on `Tables/PartQuotes`. Which two OneLake security configurations work? Select two.

Domain: Maintain a data analytics solution

- A. Create a OneLake security role scoped to the specific Files/<subfolder> path with Read permission
- B. Create two separate OneLake security roles on the same table — Role A containing the RLS filter and Role B containing the CLS column rule — and assign the user to both
- C. Define both the RLS filter and CLS column allow-list inside a single OneLake security Grant role with Read permission
- D. Create a Deny role in OneLake security to revoke table access granted by another OneLake role or Workspace Member role
- E. Create a OneLake security role with ReadWrite permission and attach an RLS predicate

### 9. Defense-aerospace export rules require `ITAR Restricted` sensitivity labels applied on `AvionicsWarehouse` to propagate automatically to downstream semantic models and reports. Which Fabric governance feature handles this?

Domain: Maintain a data analytics solution

- A. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- B. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- C. Apply a Microsoft Purview sensitivity label with downstream inheritance on the source Lakehouse or Warehouse
- D. Mark the item as Promoted in item settings

### 10. How do you force every analytics engineer saving a new semantic model or report in Fabric to select an approved sensitivity classification before publishing?

Domain: Maintain a data analytics solution

- A. Apply T-SQL Dynamic Data Masking (MASKED WITH (FUNCTION = 'partial(...)')) on sensitive columns
- B. Enable a mandatory label policy and default sensitivity label in Microsoft Purview compliance portal for Fabric users
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Share the item with Read permission only (no ReadData or ReadAll)

### 11. Supply-chain executives ask how to distinguish datasets audited by the central Data Quality Board from informal team experiments in OneLake catalog. Which endorsement tier represents formal steward approval?

Domain: Maintain a data analytics solution

- A. Mark the item as Promoted in item settings
- B. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- C. Assign the Workspace Contributor role
- D. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal

### 12. A logistics analyst wants to spotlight a useful `PortCongestionTracker` report for peers in the same division without submitting a formal central certification ticket. Which endorsement option can the analyst apply directly?

Domain: Maintain a data analytics solution

- A. Use a Purview sensitivity label configured with file encryption so exported .pbix, Excel, PDF, and PowerPoint files stay protected outside Fabric
- B. Configure Certified endorsement with the Master data label on authoritative core tables or semantic models
- C. Mark the item as Promoted in item settings
- D. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal

### 13. Five manufacturing BI developers collaborate on `MES-Analytics-Dev` connected to `main`. How should each developer build new Spark transformations and `.pbip` measures without interfering with teammates' uncommitted workspace state?

Domain: Maintain a data analytics solution

- A. Use Undo in the Fabric Workspace Source control pane to discard uncommitted workspace edits back to the last synced commit
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch
- D. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline

### 14. Which four-step workflow delivers a `.pbip` OEE measure change from a developer's feature branch through Git pull-request review into `Test` and `Production` workspaces?

Domain: Maintain a data analytics solution

- A. Edit items directly on main without branching → Merge an empty PR → Promote Dev to Test before running Update from Git → Configure Git integration last
- B. Connect shared Dev workspace to main → Branch out to an isolated developer workspace and commit .pbip/Notebook edits → Merge pull request into main in Git → Run Update all in Dev and promote via Deployment Pipeline
- C. Connect Production directly to a feature branch → Edit semantic models live in Prod → Force-push binary .pbix files including cache.abf to main → Deploy backward to Development
- D. Branch out to personal My Workspace → Run Undo to push changes to GitHub → Delete .platform metadata files → Copy visuals manually into Production

### 15. Proposed solution: Your team stores 1.1 GB `.pbix` manufacturing files in Git LFS, making pull-request code reviews of DAX formula changes impossible in browser diffs. Switching to which format exposes human-readable `.tmdl` and PBIR JSON files?

Domain: Maintain a data analytics solution

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode

### 16. Which two elements belong in a well-governed `.pbip` Git repository for a plant telemetry semantic model? Select two.

Domain: Maintain a data analytics solution

- A. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- B. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- C. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- D. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- E. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)

### 17. When deploying `InventoryModel` (`Import` mode) from `Supply-Test` to `Supply-Prod` in a Fabric Deployment Pipeline, how do you ensure `Supply-Prod` always queries `prod-erp-sql.database.windows.net` instead of `test-erp-sql`?

Domain: Maintain a data analytics solution

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Configure Deployment pipeline data source and parameter rules on the Test and Production stages

### 18. You updated `CarrierScorecardReport` and its upstream `CarrierSemanticModel` in `Dev`, while eight unfinished IoT notebooks in `Dev` are broken. How do you deploy only the scorecard and its model to `Test`?

Domain: Maintain a data analytics solution

- A. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline
- B. Perform a selective deployment selecting the modified item together with Select related to include required upstream dependencies
- C. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition
- D. Use Undo in the Fabric Workspace Source control pane to discard uncommitted workspace edits back to the last synced commit

### 19. You promote Data Factory pipelines orchestrating Lakehouse notebooks across `Dev`, `Test`, and `Prod` workspaces where SQL deployment rules do not apply to pipeline parameters. Which Fabric item provides stage-aware variables?

Domain: Maintain a data analytics solution

- A. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- B. Configure Deployment pipeline data source and parameter rules on the Test and Production stages
- C. Use a Fabric Variable library (or autobinding across paired workspace items) to parameterize stage-specific environment references
- D. Mark the item as Promoted in item settings

### 20. Before dropping legacy column `PalletWeightLbs` from `WarehouseLakehouse`, how do you enumerate every dependent Dataflow, Semantic Model, and Report across all tenant workspaces and alert their owners?

Domain: Maintain a data analytics solution

- A. Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View
- B. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- C. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- D. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view

### 21. In Workspace `Lineage` view, you trace a stale executive KPI back through a Semantic Model and a Lakehouse to a failed upstream Dataflow Gen2 refresh. Which capability makes `Lineage` view faster than checking items one by one in `List` view?

Domain: Maintain a data analytics solution

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- C. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- D. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture

### 22. Which four-step XMLA procedure deploys four new `[On-Time In-Full %]` DAX measures from `Logistics-Dev` to a 32 GB partitioned `Logistics-Prod` model without reprocessing 6 years of partitions?

Domain: Maintain a data analytics solution

- A. Leave XMLA Endpoint = Read Only → Execute T-SQL DELETE across Warehouse schemas → Grant all report viewers Capacity Admin rights → Skip downstream impact analysis
- B. Set XMLA Endpoint = Off → Overwrite Production with an empty unpartitioned .pbix file → Purge all 5 years of historical incremental partitions → Re-import 3 billion rows during peak business hours
- C. Verify XMLA Endpoint = Read Write on target capacity → Connect ALM Toolkit to Dev source and Prod XMLA target → Compare schemas while hiding unchanged partitions and keeping Prod data sources → Validate and deploy metadata-only TMSL changes
- D. Open Production in DAX Studio → Edit measures manually in Production without committing to Git → Copy cache.abf into GitHub → Disable sensitivity labels

### 23. An automated Airflow DAG triggers `{"refresh": {"type": "____", ...}}` (`dataOnly`) on partition `2026W44` via `powerbi://api.powerbi.com/v1.0/myorg/Logistics-Prod`. Which two requirements apply? Select two.

Domain: Maintain a data analytics solution

- A. Assign the Workspace Viewer role
- B. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition
- C. Enable XMLA Endpoint = Read Write in Fabric Capacity workload settings and connect to powerbi://api.powerbi.com/v1.0/myorg/<WorkspaceName>
- D. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- E. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches

### 24. Eight factories run legacy Siemens MES databases on air-gapped on-premises SQL Server hosts with no Azure VNet peering. Which gateway setup connects Fabric pipelines to those hosts without single-host SPOFs?

Domain: Prepare data

- A. Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet
- B. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- C. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- D. Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication

### 25. Data engineers share one Snowflake cloud source across 14 Fabric Copy pipelines authenticated via Workspace Identity / Service Principal without distributing credentials to individual authors. What should an admin create?

Domain: Prepare data

- A. Enable single sign-on (SSO) on the Direct Lake semantic model connection
- B. Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication
- C. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode

### 26. Supply-chain architects want analysts to locate the single authoritative `GlobalPartMaster` Lakehouse in seconds while stewards monitor governance gaps across 20 plant workspaces. Which two Fabric capabilities work together? Select two.

Domain: Prepare data

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- D. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- E. Configure Certified endorsement with the Master data label on authoritative core tables or semantic models

### 27. Your ERP order-management microservice runs on Azure SQL Database and updates inventory reservations every second. How do you replicate those tables continuously into OneLake Delta Parquet with zero pipeline code?

Domain: Prepare data

- A. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- B. Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog
- C. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- D. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view

### 28. Every shift, automated optical-inspection cameras write 3.5 TB of compressed Parquet defect logs to Azure Blob Storage that must copy raw into `BronzeLakehouse/Files/aoi/` at minimal CU cost. Which tool should you use?

Domain: Prepare data

- A. Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table
- B. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- C. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- D. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations

### 29. Which three Fabric ingestion tools match: (1) visual Power Query M lookups across 20 Smartsheet/SharePoint supplier trackers with bulk staging, (2) live MQTT/Event Hubs conveyor-belt telemetry routing, and (3) zero-ETL CDC replication from Snowflake? Select three.

Domain: Prepare data

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table
- C. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- D. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- E. Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog
- F. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint

### 30. CNC spindle vibration sensors emit 800,000 JSON telemetry events per second queried with time-series FFT/anomaly functions and 5-second KQL aggregations. Which Fabric data store fits best?

Domain: Prepare data

- A. Choose a Fabric Eventhouse (KQL database)
- B. Choose a Fabric Data Warehouse
- C. Choose a SQL database in Microsoft Fabric
- D. Choose a Fabric Lakehouse

### 31. Cost-accounting controllers require T-SQL stored procedures executing multi-table `BEGIN TRANSACTION ... UPDATE ... INSERT ... COMMIT` standard-cost rollups and T-SQL Dynamic Data Masking. Which Fabric data store is required?

Domain: Prepare data

- A. Choose a Fabric Eventhouse (KQL database)
- B. Configure Import storage mode
- C. Choose a Fabric Lakehouse
- D. Choose a Fabric Data Warehouse

### 32. A manufacturing app team needs (1) an operational OLTP database inside Fabric backing a dock-scheduling web app with sub-10 ms row inserts, and (2) a Spark data-engineering store holding raw acoustic WAV files in `Files/` plus Silver Delta tables. Which two stores apply? Select two.

Domain: Prepare data

- A. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- B. Choose a Fabric Lakehouse
- C. Choose a SQL database in Microsoft Fabric
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- E. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint

### 33. A legacy supply-chain planning model imports cleaned vendor lead-time tables via Power Query M. How can Lakehouse Spark notebooks read those imported semantic-model tables directly in OneLake without duplicating M logic?

Domain: Prepare data

- A. Point Direct Lake on SQL directly at an Eventhouse KQL database without enabling OneLake availability
- B. Enable OneLake integration in the Import semantic model settings so imported model tables export as Delta tables to OneLake
- C. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- D. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network

### 34. In which four-step order do you surface robotic-arm Eventhouse KQL telemetry inside a Lakehouse shortcut and a Direct Lake on OneLake semantic model?

Domain: Prepare data

- A. Create a Direct Lake on SQL model directly over the KQL queryset → Disable OneLake availability → Configure an On-premises data gateway → Run T-SQL MERGE on the KQL database
- B. Create an Amazon S3 external shortcut to the KQL URI before enabling OneLake availability → Set storage mode to Dual only → Enable Auto date/time → Run XMLA clearValues
- C. Ingest streaming telemetry into an Eventhouse KQL database → Enable OneLake availability on the KQL database or table → Create an internal OneLake shortcut in the Lakehouse → Add the table to a Direct Lake on OneLake semantic model
- D. Export KQL query results manually to CSV every hour → Email CSVs to analysts → Import into binary .pbix files → Publish to My Workspace

### 35. Proposed solution: An engineer connects a Data Factory `Stored procedure` activity to a **Lakehouse SQL analytics endpoint** hoping to run `CREATE PROCEDURE dbo.usp_UpsertBOM` containing `MERGE` and `DELETE` statements. Why does this fail, and what works?

Domain: Prepare data

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- D. Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic

### 36. You want a pre-joined `Gold.PartSupplierLeadTime` asset in a Lakehouse to feed a `Direct Lake on OneLake` semantic model with zero fallback. Why must you create a persisted Delta table or `Materialized Lake View` rather than a plain SQL endpoint `VIEW`?

Domain: Prepare data

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- C. Configure DirectQuery storage mode
- D. Use a Lakehouse Materialized Lake View (or persisted Gold Delta table) instead of a non-materialized SQL analytics endpoint view for Direct Lake on OneLake

### 37. Complete `CREATE ____ dbo.vw_OpenPurchaseOrders AS SELECT POId, VendorKey, OpenQty FROM gold.FactPO WHERE OpenQty > 0;` in `ProcurementWarehouse` to expose a reusable virtual projection without duplicating Parquet storage?

Domain: Prepare data

- A. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- B. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- C. Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic
- D. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations

### 38. Three ERP instances (`SAP-DE`, `Oracle-MX`, `NetSuite-US`) reuse overlapping numeric `VendorCode` integers (`10001`). How should `Gold.DimVendor` be keyed?

Domain: Prepare data

- A. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- B. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- C. Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions
- D. CAST(RawReading AS FLOAT)

### 39. Before building Direct Lake models over `FactProductionRuns`, which two Gold-layer enrichments ensure unbroken shift/ISO-week time intelligence (without `Auto date/time`) and compact integer fact joins? Select two.

Domain: Prepare data

- A. Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions
- B. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- C. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- D. Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes
- E. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals

### 40. When a supplier's ISO quality tier changes from `Tier-2` to `Tier-1` on May 1, defect rates in Q1 must remain attributed to `Tier-2` while May defects attribute to `Tier-1`. Which SCD design on `DimSupplier` is required?

Domain: Prepare data

- A. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns
- B. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)
- C. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place
- D. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension

### 41. Combining `ShipmentHeader` (`TotalFreightCost`) and `ShipmentContainerLines` (`ContainerWeightKg`) into one unallocated table causes `SUM(TotalFreightCost)` to multiply by the number of containers per shipment. What fixes this?

Domain: Prepare data

- A. Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other

### 42. Which four-step ELT sequence updates `DimWorkCenter` as an SCD Type 2 dimension when plant lines retool across cost centers?

Domain: Prepare data

- A. Stage and deduplicate incoming records by natural key → Compare tracked attributes against active (IsCurrent = 1) Gold rows → Expire changed active rows (EffectiveEndDate, IsCurrent = 0) → Insert new active versions with fresh surrogate keys
- B. Insert new versions with IsCurrent = 0 first → Overwrite old EffectiveStartDate values in place → Remove the natural business key column → Deduplicate after publishing reports
- C. Insert raw duplicate staging rows directly into FactSales → Delete unmatched dimension keys → Leave EffectiveStartDate NULL → Enable Assume referential integrity on broken keys
- D. Truncate the Gold dimension table → Reassign fresh random surrogate keys to all historical rows → Join historical facts without updating foreign keys → Set IsCurrent = 1 on every version

### 43. Select the three correct dimensional practices when (1) structuring raw/cleaned/curated OneLake zones, (2) fixing a typographical error in `PlantCityName` across all history, and (3) handling telemetry facts arriving before a new `MachineId` registers in `DimMachine`. Select three.

Domain: Prepare data

- A. Organize OneLake into Bronze (raw immutable), Silver (validated, deduplicated, conformed), and Gold (star-schema dimensions and facts with V-Order)
- B. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- C. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- D. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- E. Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE
- F. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place

### 44. Why should `WarehouseZone -> Aisle -> RackType` be flattened onto `Gold.DimStorageBin` rather than exposed as four chained tables in a semantic model?

Domain: Prepare data

- A. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- B. Configure DirectQuery storage mode
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other

### 45. Assembly-line torque wrenches log 9 billion millisecond bolt-tension rows per quarter, whereas VP Operations dashboards display daily defect counts and mean torque by `Plant` and `Shift`. How do you cut Direct Lake memory usage by 99%?

Domain: Prepare data

- A. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- B. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- C. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- D. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)

### 46. Complete `SELECT PlantCode, LineId, SUM(ScrapUnits) AS Scrap FROM gold.FactScrap ____;` so a single Warehouse scan outputs `(PlantCode, LineId)`, `(PlantCode)`, and overall company `()` scrap totals?

Domain: Prepare data

- A. | summarize arg_max(IngestionTime, *) by SpecimenId
- B. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- C. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- D. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())

### 47. In Dataflow Gen2, grouping 150 million warehouse scan rows down to 12,000 daily SKU totals finishes in 18 seconds when `View Native Query` stays enabled, versus 29 minutes when broken. Why?

Domain: Prepare data

- A. Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled
- B. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- C. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 48. Complete `MERGE INTO gold.FactInventorySnapshots t USING silver.StgSnapshots s ON t.SnapshotKey = s.SnapshotKey ____ t.OnHandQty = s.OnHandQty WHEN NOT MATCHED THEN INSERT *;` to avoid rewriting Delta Parquet files when quantities did not change?

Domain: Prepare data

- A. CAST(RawReading AS FLOAT)
- B. RANK() OVER (ORDER BY SpecimenId DESC)
- C. ADD BLOCK PREDICATE dbo.sp_checkregion(RegionCode) AFTER INSERT
- D. WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET

### 49. Before closing monthly inventory books, you need a query returning all `DimSKU` items that had **zero** movement rows in `FactInventoryMovements` during October. Which join kind produces that list?

Domain: Prepare data

- A. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- B. Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table
- C. Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement
- D. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid

### 50. In a fleet Silver-to-Gold PySpark job joining 800 million GPS pings with a 5 MB `dim_depot` table (`gps_df.join(____)`) and upserting into `gold.fact_trips`, which two patterns maximize throughput? Select two.

Domain: Prepare data

- A. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- B. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- C. fact_df.join(F.broadcast(dim_store_df), on="StoreKey", how="left")
- D. Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement
- E. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint

### 51. IoT edge gateways retry unacknowledged MQTT packets, creating duplicate `PacketId` rows in `bronze.iot_packets`. Complete `SELECT *, ____ AS rn FROM bronze.iot_packets` so `WHERE rn = 1` retains strictly one latest packet per key?

Domain: Prepare data

- A. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- B. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- C. RANK() OVER (ORDER BY SpecimenId DESC)
- D. TRY_CAST(RawReading AS DECIMAL(18, 4))

### 52. Automated guided vehicles (AGVs) transmit pallet moves before newly commissioned `DockDoorId` codes sync from SAP, producing `NULL` foreign keys during lookup. How should the Gold fact pipeline preserve those moves cleanly?

Domain: Prepare data

- A. Filter Incremental Refresh with OrderDate >= RangeStart AND OrderDate <= RangeEnd using inclusive operators on both boundaries
- B. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- C. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- D. Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE

### 53. Which two actions ensure a 60-million-row supplier ASN feed is profiled beyond Power Query's 1,000-row preview limit and purged of duplicate `ASNNumber` records before Gold load? Select two.

Domain: Prepare data

- A. Deduplicate using ROW_NUMBER() OVER (PARTITION BY BusinessKey ORDER BY ModifiedTimestamp DESC) = 1
- B. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- C. Launch Data Wrangler from a Fabric Spark notebook (or enable Power Query Column profiling based on entire data set) to inspect nulls, duplicates, and distributions and export generated PySpark code
- D. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- E. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table

### 54. A Spark Delta table `gold.fact_plc_events` contains `RawRegisterBytes` (`BINARY`) and `SensorArray` (`ARRAY<DOUBLE>`). Why do those columns fail to appear in Direct Lake modeling, and how do you fix them?

Domain: Prepare data

- A. Configure shared dimension tables in Dual storage mode inside a composite model
- B. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- C. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- D. Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake

### 55. Complete the foldable Power Query M filter expression `____` used on `OrderDate` with `RangeStart` and `RangeEnd` parameters so partition boundaries never duplicate midnight rows while keeping `View Native Query` active?

Domain: Prepare data

- A. Table.SelectRows(Source, each [OrderDate] >= RangeStart and [OrderDate] < RangeEnd)
- B. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'
- C. Filter Incremental Refresh with OrderDate >= RangeStart AND OrderDate <= RangeEnd using inclusive operators on both boundaries
- D. CAST(RawReading AS FLOAT)

### 56. Proposed solution: A manufacturing analyst filters `gold.fact_sensor_hourly` with `WHERE CAST(ReadingDate AS VARCHAR(10)) = '2026-10-30'` and wonders why Spark reads all 14 TB of historical Parquet files. What fixes file pruning?

Domain: Prepare data

- A. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'
- B. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- C. CAST(RawReading AS FLOAT)
- D. Filter on physical Delta partition or liquid-clustered date columns using sargable range predicates (OrderDate >= '2026-01-01') without wrapping the column in functions

### 57. When a supply-chain analyst uses `Merge queries` and `Group by` inside the Warehouse `Visual query editor`, how does Fabric execute those steps?

Domain: Prepare data

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- C. Use ALM Toolkit over the XMLA endpoint to compare Dev and Prod semantic models and deploy only new measures without reprocessing unchanged partitions
- D. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint

### 58. Complete `SELECT MachineId, ReadingHour, CumulativeCycles, CumulativeCycles - ____ AS HourlyCycles FROM gold.FactMeterCounters;` to compute hourly output from a monotonically increasing counter per machine?

Domain: Prepare data

- A. TRY_CAST(RawReading AS DECIMAL(18, 4))
- B. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- C. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- D. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())

### 59. `LogisticsWarehouse` and `TelematicsLakehouse` sit in the same `Fleet-Prod` workspace. Complete `SELECT w.RouteId, t.AlertCode FROM dbo.DimRoute w JOIN ____ t ON w.VehicleId = t.VehicleId;` to join without copying data or creating shortcuts?

Domain: Prepare data

- A. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching
- B. Query across a Warehouse and a Lakehouse SQL analytics endpoint in the same workspace using three-part T-SQL naming (SalesLakehouse.dbo.RawOrders)
- C. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- D. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network

### 60. Before deploying a major BOM costing update in `PlantWarehouse`, engineers want to (1) create a zero-copy table backup (`____`), and (2) query yesterday's pre-batch inventory valuation as of `2026-10-28T06:00:00.000` (`____`). Which two T-SQL features apply? Select two.

Domain: Prepare data

- A. OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')
- B. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- C. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- D. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- E. CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales

### 61. In `FleetEventhouse`, reefer trucks emit irregular GPS/temperature pings every 3–40 seconds with occasional duplicate retries (`ReeferPings | summarize ____ by DeviceId`). Which KQL pattern deduplicates latest status per truck and aggregates 5-minute p95 temperature buckets?

Domain: Prepare data

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Write a KQL query using | where Timestamp > ago(24h) | summarize arg_max(IngestionTime, *) by DeviceId and | summarize AvgTemp = avg(Temp), P95 = percentile(Temp, 95) by bin(Timestamp, 5m)
- C. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- D. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view

### 62. PLC controllers stream JSON payloads into Eventhouse where each message holds an array `MotorAxes` of 6 torque objects (`PlcEvents | ____ MotorAxis = parse_json(Payload).MotorAxes`). Which KQL operators unpack those 6 objects into individual rows before filtering stalled axes?

Domain: Prepare data

- A. | summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)
- B. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- C. Use KQL parse_json() (or dynamic column indexing) followed by | mv-expand SensorReadings to flatten nested JSON arrays before aggregating
- D. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)

### 63. You want to validate a new `[OTIF %]` DAX measure across 12 plant regions in a tabular grid using `DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...)` before committing changes to the semantic model. Which tool should you use?

Domain: Prepare data

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- C. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- D. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results

### 64. Which built-in DAX function (`EVALUATE ____`) executed in DAX Query View profiles every table column's cardinality, min/max values, and max string length without launching external tools?

Domain: Prepare data

- A. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages
- B. Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View
- C. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 65. `SupplyChainLakehouse` stores 800 million V-Order Delta rows refreshed every 15 minutes in OneLake, and logistics planners need sub-second interactive slicing without copying 800M rows into Import partitions. Which storage mode fits?

Domain: Implement and manage semantic models

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Configure Direct Lake storage mode
- C. Configure Import storage mode
- D. Configure DirectQuery storage mode

### 66. `FactShipments[ShipDateKey]` (`INT` `20261030`) joins to `DimDate[DateKey]`. What must you configure on `DimDate` so `DATESYTD('DimDate'[CalendarDate])` clears `DateKey` filters automatically?

Domain: Implement and manage semantic models

- A. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- B. Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid

### 67. Which two semantic-model star-schema practices prevent self-service report authors from accidentally averaging `PlantSurrogateKey`, fix alphabetical sorting of `"Q1, Q2, Q3, Q4"` / `"Jan..Dec"`, and remove hidden auto-date tables? Select two.

Domain: Implement and manage semantic models

- A. Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column
- B. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- E. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other

### 68. `FactPurchaseOrders` has `OrderDateKey` (active), `PromisedDateKey` (inactive), and `ReceivedDateKey` (inactive) linked to `Calendar[DateKey]`. Complete `Receipts by Received Date = ____` (conceptually activating the inactive key)?

Domain: Implement and manage semantic models

- A. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- B. CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))
- C. CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))
- D. CALCULATE([Encounter Count], CROSSFILTER('FactEncounter'[EncounterKey], 'BridgeEncounterDiag'[EncounterKey], BOTH))

### 69. A single `DefectIncident` can involve multiple `RootCauseCodes`, and each `RootCauseCode` appears across thousands of incidents. How should you connect `DimIncident`, `BridgeIncidentCause`, and `DimRootCause`?

Domain: Implement and manage semantic models

- A. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()
- B. Introduce a deduplicated Bridge table between the two dimensions and scope bidirectional propagation strictly inside specific measures using CROSSFILTER(..., BOTH)
- C. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other

### 70. On a `DirectQuery` Warehouse semantic model where non-null foreign-key constraints are enforced during Gold ELT, enabling `Assume referential integrity` changes generated SQL in what way?

Domain: Implement and manage semantic models

- A. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- B. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- C. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- D. Configure Import storage mode

### 71. Plant finance tracks 13 four-week manufacturing periods per year (`P01`–`P13`) where Gregorian `DATEADD(..., -1, MONTH)` fails. Which family of DAX functions compares `P08` directly against `P07` along `FiscalPeriodSort`?

Domain: Implement and manage semantic models

- A. Use DAX window functions OFFSET(-1, ALLSELECTED(DimDate[YearMonth]), ORDERBY(DimDate[YearMonthNum], ASC)) or WINDOW() with PARTITIONBY()
- B. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- C. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- D. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table

### 72. Complete `Total Scrap Cost = ____(FactScrapRuns, FactScrapRuns[ScrapUnits] * RELATED(DimPart[StandardUnitCost]))` to multiply units by part cost per row without adding a calculated column on `FactScrapRuns`?

Domain: Implement and manage semantic models

- A. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table
- B. Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches
- C. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- D. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)

### 73. Proposed solution: A measure `[Capacity Utilization Band]` calls `[Net Machine Hours]` five separate times inside nested `SWITCH(TRUE(), ...)` branches, causing five Storage Engine scan bursts. What single DAX change fixes this?

Domain: Implement and manage semantic models

- A. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- B. [ManagerEmail] = USERPRINCIPALNAME()
- C. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- D. Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches

### 74. You author two manufacturing DAX measures: (1) `[Hazmat Shipments]` that must intersect cleanly with user `MaterialClass` slicers rather than overwriting them, and (2) `[Line Cycle Time Sec]` that must display values on `WorkCenter` leaf rows and `BLANK()` on `Plant` subtotals. Which two DAX functions should you use? Select two.

Domain: Implement and manage semantic models

- A. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Use ISINSCOPE(DimProduct[Subcategory]) (or SELECTEDVALUE with an alternate result) to branch measure behavior cleanly across matrix hierarchy levels
- D. Pass simple column predicates wrapped in KEEPFILTERS(DimProduct[Color] = "Red") to CALCULATE instead of FILTER(ALL(FactSales), ...)
- E. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows

### 75. Instead of creating 180 separate measures (`30 KPIs x 6 horizons: WTD, MTD, YTD, PY, YoY, YoY%`), which semantic-model feature reduces maintenance to 30 base measures plus 6 reusable calculation items?

Domain: Implement and manage semantic models

- A. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Create a Calculation Group with Calculation Items referencing SELECTEDMEASURE() and explicit Precedence ordering (automatically setting DiscourageImplicitMeasures = true)
- D. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically

### 76. Proposed solution: Plant directors switch a single chart's measure between `$ Cost` (`$#,0`), `Defect PPM` (`#,0`), and `OEE %` (`0.0%`), so a developer wraps the measure in `FORMAT(..., "$#,0")` and notices line-chart continuous axes stop rendering. What fixes this while keeping values numeric?

Domain: Implement and manage semantic models

- A. Mark the item as Promoted in item settings
- B. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- C. Configure a Dynamic Format String expression on the measure or calculation item (for example returning "\$#,0.00" vs "0.0%" via SELECTEDMEASUREFORMATSTRING()) without wrapping values in FORMAT()
- D. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear

### 77. Supply-chain planners want one slicer (`Analyze By: Supplier, Carrier, OriginPort, or TransportMode`) that dynamically changes the column grouping a bar chart's Y-axis (`{ ("Supplier", ____('DimSupplier'[SupplierName]), 0), ... }`). Which feature implements this?

Domain: Implement and manage semantic models

- A. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()
- B. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- C. Create a Calculation Group with Calculation Items referencing SELECTEDMEASURE() and explicit Precedence ordering (automatically setting DiscourageImplicitMeasures = true)
- D. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer

### 78. A global bill-of-materials semantic model grows to 16 GB compressed on an F64 capacity. Enabling which setting prevents scheduled refresh failures at the legacy 10 GB cap and speeds up Tabular Editor saves?

Domain: Implement and manage semantic models

- A. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Configure DirectQuery storage mode
- D. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages

### 79. Before enabling `Large semantic model storage format` + Incremental Refresh on a 1.8-billion-row historical Oracle ERP Import table so Power BI Desktop never downloads 1.8B rows locally, what must you configure in Power Query?

Domain: Implement and manage semantic models

- A. Create exact case-sensitive DateTime parameters RangeStart and RangeEnd, filter Date >= RangeStart and Date < RangeEnd (half-open interval) with query folding intact, and enable Incremental refresh
- B. Filter Incremental Refresh with OrderDate >= RangeStart AND OrderDate <= RangeEnd using inclusive operators on both boundaries
- C. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- D. Configure Direct Lake storage mode

### 80. Which two scenarios use composite semantic models appropriately: (1) combining `Direct Lake on OneLake` plant tables with an `Import` SharePoint safety-target sheet using regular relationships, and (2) letting an analyst extend a Certified corporate model with a local SQL sandbox table via `DirectQuery for Power BI semantic models`? Select two.

Domain: Implement and manage semantic models

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Create a local composite model using DirectQuery for Power BI semantic models and Analysis Services to combine a certified core semantic model with a departmental Excel/SQL table
- C. Build a Direct Lake on OneLake composite semantic model combining Direct Lake fact tables from OneLake with Import dimension/target tables using regular relationships
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- E. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches

### 81. A shop-floor wallboard page with 48 gauge visuals refreshes sluggishly every minute; DAX queries take 15 ms each, yet total page render takes 12 seconds. Which tool isolates `Other` visual-queue contention?

Domain: Implement and manage semantic models

- A. Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View
- B. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts

### 82. Which report-level `Query reduction` setting stops multi-select part-number slicers on a `DirectQuery` report from firing premature Warehouse queries until the engineer finishes picking part numbers?

Domain: Implement and manage semantic models

- A. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- B. Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails
- C. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages
- D. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)

### 83. You profile `[Weighted Supplier Lead Time]` in DAX Studio `Server Timings` and see 140 separate `xmSQL` Storage Engine queries and 82% Formula Engine time caused by `FILTER(FactReceipts, ...)`. How should you refactor the DAX?

Domain: Implement and manage semantic models

- A. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- B. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- C. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- D. Profile the slow measure in DAX Studio using Server Timings to inspect Formula Engine (FE) vs Storage Engine (SE) CPU, SE query count, and CallbackDataID warnings

### 84. Which four-step workflow diagnoses and verifies fixes for a slow Direct Lake `[Scrap Cost Variance]` visual without warm-cache distortion?

Domain: Implement and manage semantic models

- A. Capture visual timings in Performance Analyzer → Profile captured DAX in DAX Studio with Server Timings and Query Plan → Refactor FILTER(Fact,...) into VAR-cached SE column predicates and run V-Order OPTIMIZE → Re-test with Clear Cache
- B. Immediately upgrade from F64 to F512 without profiling → Enable bidirectional cross-filtering on all relationships → Convert numeric measures to FORMAT() strings → Disable V-Order on Gold tables
- C. Test queries only against warm VertiPaq cache without Clear Cache → Add high-cardinality GUID calculated columns to FactSales → Force DirectQueryOnly behavior → Add 45 single-value card visuals to one page
- D. Hide slow measures in Display Folders → Turn on Auto date/time → Split one Gold dimension into 6 normalized snowflake tables → Remove calendar surrogate keys

### 85. Which three engineering practices maximize Direct Lake in-memory stability and transcoding speed on `Gold.FactProduction`? Select three.

Domain: Implement and manage semantic models

- A. Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails
- B. Expect Direct Lake on OneLake to automatically fall back to DirectQuery against the SQL analytics endpoint when capacity memory guardrails are exceeded
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes
- E. Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time
- F. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes

### 86. Proposed solution: You inspect an existing Direct Lake model in Power BI Desktop TMDL view and see `Sql.Database(...)` in its shared `Expression`, preventing you from adding tables from a second Warehouse, so a teammate suggests switching the entire model to `DirectQuery`. What TMDL edit (`____`) upgrades it cleanly to `Direct Lake on OneLake` instead?

Domain: Implement and manage semantic models

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Migrate the model in Power BI Desktop TMDL view by replacing Sql.Database(...) in the shared Expression with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<itemId>")
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)

### 87. In which four-step order should you perform an in-place Power BI Desktop migration from `Direct Lake on SQL` to `Direct Lake on OneLake` while preserving a rollback checkpoint?

Domain: Implement and manage semantic models

- A. Keep non-materialized SQL analytics endpoint views as the only sources → Switch TMDL expression to AzureStorage.DataLake without materializing Delta tables → Enable DirectQuery fallback on Direct Lake on OneLake → Bind an On-premises gateway
- B. Download the Direct Lake model as an offline Import .pbix → Convert all tables to Dual storage mode → Replace AzureStorage.DataLake with OleDb.DataSource → Re-upload to My Workspace
- C. Live edit the model in Power BI Desktop and save a Version history point → Script the semantic model in TMDL view → Replace Sql.Database(...) with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...") → Apply TMDL and run framing refresh
- D. Delete the semantic model in Production breaking report GUID bindings → Recreate measures manually from screenshots → Share Lakehouse Admin rights with all report viewers → Disable V-Order

### 88. Which four-step workflow configures Incremental Refresh on a 650-million-row `FactSupplierShipments` Import table over an On-premises gateway without breaking query folding?

Domain: Implement and manage semantic models

- A. Create case-sensitive DateTime parameters RangeStart and RangeEnd → Apply foldable half-open filter (>= RangeStart and < RangeEnd) → Configure table Incremental refresh policy → Publish to workspace and run initial refresh to generate partitions
- B. Publish an unfiltered 2-billion-row Import PBIX locally first → Define RangeStart in DAX calculated tables afterward → Set storage mode to Direct Lake on OneLake → Enable VNet gateway on Direct Lake
- C. Filter OrderDate > RangeEnd → Configure Detect data changes on the exact same OrderDate partition column → Disable query folding → Run XMLA clearValues without processing
- D. Create Text parameters named StartDate and EndDate → Add a custom M step breaking query folding before filtering → Use >= and <= inclusive bounds on both sides → Refresh only in Power BI Desktop

---

## Case study — ColdHaul Logistics

ColdHaul Logistics discovers live Azure IoT Hub reefer-truck temperature streams through the Fabric Real-Time hub. Supply-chain business analysts who do not write T-SQL want a browser diagram interface on the Warehouse to join shipments with carrier dimensions and save reusable SQL views, while raw CSV feeds occasionally contain `"N/A"` strings in numeric sensor columns.

The next 3 questions refer to **ColdHaul Logistics**. Read the scenario brief once, then answer each item independently.

### 89. Where in Microsoft Fabric do reefer-fleet engineers discover live Azure IoT Hub temperature streams alongside workspace events and attach Activator temperature-breach alerts?

Domain: Prepare data

- A. Use the Real-Time hub to subscribe to Microsoft.Fabric.OneLake.FileCreated events (or Capacity/CDC streams) and trigger an Activator rule
- B. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- C. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 90. Which browser experience lets non-SQL supply-chain analysts visually join `FactShipments` with `DimCarrier` on the Warehouse, filter late loads, and persist reusable SQL views?

Domain: Prepare data

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- C. Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic
- D. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results

### 91. Reefer CSV feeds occasionally emit `"N/A"` inside numeric `ReeferTempC` columns (`____(ReeferTempC AS DECIMAL(6,2))`). Which conversion approach quarantines `"N/A"` as `NULL` instead of aborting nightly loads?

Domain: Prepare data

- A. Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake
- B. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- C. Convert dirty string columns using TRY_CAST / TRY_CONVERT in T-SQL (or Spark try_cast) so malformed rows evaluate to NULL for quarantine instead of aborting the batch
- D. CAST(RawReading AS FLOAT)

---

## Case study — GridWorks Components

GridWorks Components serves plant operations from a 6-billion-row real-time DirectQuery Warehouse fact table alongside conformed Product, Plant, and Date dimensions. Ninety-five percent of executive visuals group by Date, Plant, and ProductCategory, while plant engineers occasionally drill down to individual serial-number events.

The next 3 questions refer to **GridWorks Components**. Read the scenario brief once, then answer each item independently.

### 92. How should you serve 95% of executive visuals grouped by `Date`, `Plant`, and `ProductCategory` in sub-second memory while routing serial-number drills to the 6-billion-row `DirectQuery` Warehouse table?

Domain: Implement and manage semantic models

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Configure Import storage mode
- C. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- D. Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table

### 93. Which storage mode must be set on `DimProduct`, `DimPlant`, and `DimDate` so both the in-memory aggregation table and the 6-billion-row `DirectQuery` detail table join cleanly without cross-source penalties?

Domain: Implement and manage semantic models

- A. Configure DirectQuery storage mode
- B. Configure shared dimension tables in Dual storage mode inside a composite model
- C. Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop)
- D. Configure Import storage mode

### 94. Plant ERP stores `Part -> SubAssembly -> AssemblyFamily -> ProductLine` in four normalized tables. How should you structure `Gold.DimProduct`?

Domain: Prepare data

- A. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()
- B. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- C. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns
- D. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension

---

## Case study — HarborPort Freight

HarborPort Freight maintains one Certified golden Supply Chain semantic model in a locked data workspace while 12 regional teams build thin reports in their own workspaces. External partner analysts must never discover that `ContractMargin` or `CarrierRebate` columns/measures even exist in metadata, and field offices receive a zero-data parameterized Power BI file to connect to local ports.

The next 3 questions refer to **HarborPort Freight**. Read the scenario brief once, then answer each item independently.

### 95. How should the 12 regional teams build customized logistics reports in their own workspaces while reusing the single Certified golden `SupplyChain` semantic model?

Domain: Maintain a data analytics solution

- A. Publish a single certified core semantic model in a data workspace and build thin live-connected Power BI reports in departmental workspaces
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- D. Configure Import storage mode

### 96. Which security control guarantees external partner analysts cannot even discover that `ContractMargin` or `CarrierRebate` columns and referencing measures exist in model metadata?

Domain: Maintain a data analytics solution

- A. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- B. Apply T-SQL Dynamic Data Masking (MASKED WITH (FUNCTION = 'partial(...)')) on sensitive columns
- C. Mark the item as Promoted in item settings
- D. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS

### 97. Which zero-data file format should you ship to field port offices so opening it prompts for their `PortTerminalCode` parameter and populates visuals against local data?

Domain: Maintain a data analytics solution

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- D. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)

---

## Case study — TorqueLine Motors

TorqueLine Motors mounts existing plant Parquet lakes from ADLS Gen2 and supplier quality logs from Amazon S3 into a Fabric Lakehouse without copying files. Micro-batch Spark writes generate 45,000 tiny Parquet files per Gold table, causing Direct Lake queries to degrade and fall back, while row-by-row Python `@udf` string cleanups bottleneck Silver notebooks.

The next 3 questions refer to **TorqueLine Motors**. Read the scenario brief once, then answer each item independently.

### 98. How should you expose existing plant Parquet lakes in ADLS Gen2 and supplier quality logs in Amazon S3 inside your Fabric Lakehouse without duplicating files or scheduling copy pipelines?

Domain: Prepare data

- A. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- B. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- C. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- D. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching

### 99. Micro-batch Spark writes produced 45,000 tiny Parquet files on `gold.fact_orders` / `gold.fact_assembly`, triggering Direct Lake guardrail degradation. Complete the maintenance command `____;` to compact rowgroups and optimize columnar compression?

Domain: Implement and manage semantic models

- A. Configure DirectQuery storage mode
- B. OPTIMIZE gold.fact_orders VORDER
- C. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- D. CAST(RawReading AS FLOAT)

### 100. How should Silver notebooks replace the slow row-by-row Python `@udf` string cleanups (`df.____("CleanVIN", F.upper(F.trim("RawVIN")))`) across hundreds of millions of assembly records?

Domain: Prepare data

- A. Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs
- B. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- C. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- D. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals

---

## Answer key and explanations

### Question 1 — C

Answer: Assign the Workspace Contributor role. `Workspace Contributor` permits authoring and scheduling Fabric items while preventing external sharing, App updates, and role changes. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Incorrect for this requirement. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. Why the keyed choice wins: `Workspace Contributor` permits authoring and scheduling Fabric items while preventing external sharing, App updates, and role changes.
- **B:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: `Workspace Contributor` permits authoring and scheduling Fabric items while preventing external sharing, App updates, and role changes.
- **C:** Correct. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. In this scenario: `Workspace Contributor` permits authoring and scheduling Fabric items while preventing external sharing, App updates, and role changes.
- **D:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: `Workspace Contributor` permits authoring and scheduling Fabric items while preventing external sharing, App updates, and role changes.

### Question 2 — A

Answer: Assign the Workspace Viewer role. Workspace `Admin`, `Member`, and `Contributor` roles bypass OneLake security and semantic-model RLS; assigning `Workspace Viewer` enforces row restrictions. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Correct. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. In this scenario: Workspace `Admin`, `Member`, and `Contributor` roles bypass OneLake security and semantic-model RLS; assigning `Workspace Viewer` enforces row restrictions.
- **B:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: Workspace `Admin`, `Member`, and `Contributor` roles bypass OneLake security and semantic-model RLS; assigning `Workspace Viewer` enforces row restrictions.
- **C:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: Workspace `Admin`, `Member`, and `Contributor` roles bypass OneLake security and semantic-model RLS; assigning `Workspace Viewer` enforces row restrictions.
- **D:** Incorrect for this requirement. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. Why the keyed choice wins: Workspace `Admin`, `Member`, and `Contributor` roles bypass OneLake security and semantic-model RLS; assigning `Workspace Viewer` enforces row restrictions.

### Question 3 — A, E

Answers: Assign the Workspace Admin role; Assign permissions to Microsoft Entra security groups rather than individual users. `Workspace Admin` is required to link workspace Git integration and manage workspace settings, assigned cleanly through Microsoft Entra security groups. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Correct. Granting workspace, item, deployment-pipeline, and RLS role memberships to Microsoft Entra security groups centralizes joiner/mover/leaver governance and scales across workspaces without per-user ACL drift. In this scenario: `Workspace Admin` is required to link workspace Git integration and manage workspace settings, assigned cleanly through Microsoft Entra security groups.
- **B:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: `Workspace Admin` is required to link workspace Git integration and manage workspace settings, assigned cleanly through Microsoft Entra security groups.
- **C:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: `Workspace Admin` is required to link workspace Git integration and manage workspace settings, assigned cleanly through Microsoft Entra security groups.
- **D:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: `Workspace Admin` is required to link workspace Git integration and manage workspace settings, assigned cleanly through Microsoft Entra security groups.
- **E:** Correct. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. In this scenario: `Workspace Admin` is required to link workspace Git integration and manage workspace settings, assigned cleanly through Microsoft Entra security groups.

### Question 4 — D

Answer: Grant Build permission on the shared semantic model. `Build` permission on `SupplierSpend` grants XMLA/Excel query and thin-report creation access without workspace edit or Lakehouse file rights. Build permission on a semantic model allows analysts to create new Power BI reports, use Analyze in Excel, and issue XMLA/DAX queries against the model without granting workspace Contributor rights or underlying Lakehouse access. Local study-map skill 1.2 (Implement Item-Level Access Controls (Read, ReadData, ReadAll, Build, SSO vs Fixed Identity)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Share items in Microsoft Fabric & Semantic model Build permission (https://learn.microsoft.com/en-us/fabric/fundamentals/share-items).

- **A:** Incorrect for this requirement. ReadData grants SELECT across all tables/views in the SQL analytics endpoint or Warehouse without granting direct Spark/ABFS access to underlying Lakehouse files. Why the keyed choice wins: `Build` permission on `SupplierSpend` grants XMLA/Excel query and thin-report creation access without workspace edit or Lakehouse file rights.
- **B:** Incorrect for this requirement. ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled. Why the keyed choice wins: `Build` permission on `SupplierSpend` grants XMLA/Excel query and thin-report creation access without workspace edit or Lakehouse file rights.
- **C:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: `Build` permission on `SupplierSpend` grants XMLA/Excel query and thin-report creation access without workspace edit or Lakehouse file rights.
- **D:** Correct. Build permission on a semantic model allows analysts to create new Power BI reports, use Analyze in Excel, and issue XMLA/DAX queries against the model without granting workspace Contributor rights or underlying Lakehouse access. In this scenario: `Build` permission on `SupplierSpend` grants XMLA/Excel query and thin-report creation access without workspace edit or Lakehouse file rights.

### Question 5 — D

Answer: Bind the Direct Lake semantic model to a cloud connection with a fixed identity and disable SSO. Binding the Direct Lake model to a cloud connection configured with a fixed identity (Workspace Identity or Service Principal) and SSO disabled decouples report viewer access from Lakehouse ACLs. Configuring a fixed-identity cloud connection (Service Principal or Workspace Identity) with SSO disabled lets report consumers query the Direct Lake model enforced by semantic-model RLS without granting them any direct Lakehouse or SQL endpoint permissions. Local study-map skill 1.2 (Implement Item-Level Access Controls (Read, ReadData, ReadAll, Build, SSO vs Fixed Identity)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Share items in Microsoft Fabric & Semantic model Build permission (https://learn.microsoft.com/en-us/fabric/fundamentals/share-items).

- **A:** Incorrect for this requirement. ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled. Why the keyed choice wins: Binding the Direct Lake model to a cloud connection configured with a fixed identity (Workspace Identity or Service Principal) and SSO disabled decouples report viewer access from Lakehouse ACLs.
- **B:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: Binding the Direct Lake model to a cloud connection configured with a fixed identity (Workspace Identity or Service Principal) and SSO disabled decouples report viewer access from Lakehouse ACLs.
- **C:** Incorrect for this requirement. With SSO enabled on a Direct Lake model, Fabric evaluates data permissions at the underlying SQL analytics endpoint or OneLake security layer using each viewing report consumer's own Microsoft Entra identity. Why the keyed choice wins: Binding the Direct Lake model to a cloud connection configured with a fixed identity (Workspace Identity or Service Principal) and SSO disabled decouples report viewer access from Lakehouse ACLs.
- **D:** Correct. Configuring a fixed-identity cloud connection (Service Principal or Workspace Identity) with SSO disabled lets report consumers query the Direct Lake model enforced by semantic-model RLS without granting them any direct Lakehouse or SQL endpoint permissions. In this scenario: Binding the Direct Lake model to a cloud connection configured with a fixed identity (Workspace Identity or Service Principal) and SSO disabled decouples report viewer access from Lakehouse ACLs.

### Question 6 — D

Answer: Create an inline table-valued predicate function with SCHEMABINDING and a CREATE SECURITY POLICY FILTER PREDICATE in the Warehouse. Creating a `SCHEMABINDING` inline table-valued predicate function bound via `CREATE SECURITY POLICY ... ADD FILTER PREDICATE ... WITH (STATE = ON)` enforces T-SQL RLS natively. Fabric Warehouse and SQL analytics endpoints enforce native SQL RLS via an inline TVF (for example checking USER_NAME() or SUSER_SNAME()) bound with CREATE SECURITY POLICY ... ADD FILTER PREDICATE ... WITH (STATE = ON). Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. OneLake security roles granting ReadWrite permission cannot contain RLS or CLS constraints; fine-grained row and column rules are supported only on Read roles. Why the keyed choice wins: Creating a `SCHEMABINDING` inline table-valued predicate function bound via `CREATE SECURITY POLICY ... ADD FILTER PREDICATE ... WITH (STATE = ON)` enforces T-SQL RLS natively.
- **B:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Creating a `SCHEMABINDING` inline table-valued predicate function bound via `CREATE SECURITY POLICY ... ADD FILTER PREDICATE ... WITH (STATE = ON)` enforces T-SQL RLS natively.
- **C:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Creating a `SCHEMABINDING` inline table-valued predicate function bound via `CREATE SECURITY POLICY ... ADD FILTER PREDICATE ... WITH (STATE = ON)` enforces T-SQL RLS natively.
- **D:** Correct. Fabric Warehouse and SQL analytics endpoints enforce native SQL RLS via an inline TVF (for example checking USER_NAME() or SUSER_SNAME()) bound with CREATE SECURITY POLICY ... ADD FILTER PREDICATE ... WITH (STATE = ON). In this scenario: Creating a `SCHEMABINDING` inline table-valued predicate function bound via `CREATE SECURITY POLICY ... ADD FILTER PREDICATE ... WITH (STATE = ON)` enforces T-SQL RLS natively.

### Question 7 — B

Answer: Enable OneLake security and define Read Grant roles → Assign consumers Workspace Viewer and OneLake security roles → Set SQL analytics endpoint to User's identity mode → Expose downstream shortcuts in User's identity mode. Defining Read Grant roles on `GlobalPartsLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces rules uniformly. Correct order: enable OneLake security with Grant roles first, assign consumers to Viewer + security roles (never Contributor), set SQL analytics endpoints to User's identity mode, and expose shortcuts downstream. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. Incorrect: Members bypass OneLake security, ReadWrite roles cannot contain RLS/CLS rules, and OneLake shortcuts do not use On-premises gateways. Why the keyed choice wins: Defining Read Grant roles on `GlobalPartsLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces rules uniformly.
- **B:** Correct. Correct order: enable OneLake security with Grant roles first, assign consumers to Viewer + security roles (never Contributor), set SQL analytics endpoints to User's identity mode, and expose shortcuts downstream. In this scenario: Defining Read Grant roles on `GlobalPartsLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces rules uniformly.
- **C:** Incorrect for this requirement. Incorrect: Contributors bypass OneLake security completely, OneLake security has no Deny role type, and Owner fixed identity bypasses per-user role evaluation on SQL queries. Why the keyed choice wins: Defining Read Grant roles on `GlobalPartsLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces rules uniformly.
- **D:** Incorrect for this requirement. Incorrect: mixing pre-existing SQL granular access with Delegated mode forces 100% DirectQuery fallback instead of clean OneLake security evaluation. Why the keyed choice wins: Defining Read Grant roles on `GlobalPartsLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces rules uniformly.

### Question 8 — A, C

Answers: Define both the RLS filter and CLS column allow-list inside a single OneLake security Grant role with Read permission; Create a OneLake security role scoped to the specific Files/<subfolder> path with Read permission. A folder-scoped `Read` Grant role isolates `Files/cad_specs/v2/`, and a single `Read` Grant role combining both RLS and CLS secures `Tables/PartQuotes` without multi-role conflicts. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Correct. OneLake folder-level security grants inherited Read (or ReadWrite) access to the selected subfolder and its descendants while allowing parent traversal without exposing sibling folders or Tables. In this scenario: A folder-scoped `Read` Grant role isolates `Files/cad_specs/v2/`, and a single `Read` Grant role combining both RLS and CLS secures `Tables/PartQuotes` without multi-role conflicts.
- **B:** Incorrect for this requirement. OneLake security does not support combining an RLS role and a CLS role across separate roles on the same table; members assigned to that combination receive query errors. Why the keyed choice wins: A folder-scoped `Read` Grant role isolates `Files/cad_specs/v2/`, and a single `Read` Grant role combining both RLS and CLS secures `Tables/PartQuotes` without multi-role conflicts.
- **C:** Correct. OneLake security supports Grant roles only (Read permission required for RLS/CLS) and requires combining RLS and CLS on the same table within a single role — separate RLS and CLS roles on the same table return query errors. In this scenario: A folder-scoped `Read` Grant role isolates `Files/cad_specs/v2/`, and a single `Read` Grant role combining both RLS and CLS secures `Tables/PartQuotes` without multi-role conflicts.
- **D:** Incorrect for this requirement. OneLake security supports Grant roles only — there is no Deny role type, and OneLake security never restricts Workspace Admins, Members, or Contributors. Why the keyed choice wins: A folder-scoped `Read` Grant role isolates `Files/cad_specs/v2/`, and a single `Read` Grant role combining both RLS and CLS secures `Tables/PartQuotes` without multi-role conflicts.
- **E:** Incorrect for this requirement. OneLake security roles granting ReadWrite permission cannot contain RLS or CLS constraints; fine-grained row and column rules are supported only on Read roles. Why the keyed choice wins: A folder-scoped `Read` Grant role isolates `Files/cad_specs/v2/`, and a single `Read` Grant role combining both RLS and CLS secures `Tables/PartQuotes` without multi-role conflicts.

### Question 9 — C

Answer: Apply a Microsoft Purview sensitivity label with downstream inheritance on the source Lakehouse or Warehouse. Microsoft Purview sensitivity-label downstream inheritance automatically carries classifications from Warehouses/Lakehouses to newly connected semantic models and reports. Sensitivity labels applied to Fabric Lakehouses, Warehouses, and Semantic Models automatically propagate downstream to newly connected semantic models, reports, and exported Excel/PDF/PPTX files when inheritance is enabled. Local study-map skill 1.4 (Apply Microsoft Purview Sensitivity Labels, Inheritance, Default/Mandatory Policies, and Export Encryption), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Information protection & sensitivity labels in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-overview).

- **A:** Incorrect for this requirement. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Why the keyed choice wins: Microsoft Purview sensitivity-label downstream inheritance automatically carries classifications from Warehouses/Lakehouses to newly connected semantic models and reports.
- **B:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Microsoft Purview sensitivity-label downstream inheritance automatically carries classifications from Warehouses/Lakehouses to newly connected semantic models and reports.
- **C:** Correct. Sensitivity labels applied to Fabric Lakehouses, Warehouses, and Semantic Models automatically propagate downstream to newly connected semantic models, reports, and exported Excel/PDF/PPTX files when inheritance is enabled. In this scenario: Microsoft Purview sensitivity-label downstream inheritance automatically carries classifications from Warehouses/Lakehouses to newly connected semantic models and reports.
- **D:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Microsoft Purview sensitivity-label downstream inheritance automatically carries classifications from Warehouses/Lakehouses to newly connected semantic models and reports.

### Question 10 — B

Answer: Enable a mandatory label policy and default sensitivity label in Microsoft Purview compliance portal for Fabric users. Configuring a mandatory sensitivity label policy in the Microsoft Purview compliance portal requires users to apply a label on save/publish. Mandatory and default sensitivity label policies in Microsoft Purview require content creators to classify unlabeled semantic models and reports on save and apply baseline classification automatically. Local study-map skill 1.4 (Apply Microsoft Purview Sensitivity Labels, Inheritance, Default/Mandatory Policies, and Export Encryption), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Information protection & sensitivity labels in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-overview).

- **A:** Incorrect for this requirement. Dynamic Data Masking obfuscates sensitive strings/emails/numbers in query results for users lacking UNMASK permission while keeping the column present so SELECT * queries do not fail. Why the keyed choice wins: Configuring a mandatory sensitivity label policy in the Microsoft Purview compliance portal requires users to apply a label on save/publish.
- **B:** Correct. Mandatory and default sensitivity label policies in Microsoft Purview require content creators to classify unlabeled semantic models and reports on save and apply baseline classification automatically. In this scenario: Configuring a mandatory sensitivity label policy in the Microsoft Purview compliance portal requires users to apply a label on save/publish.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Configuring a mandatory sensitivity label policy in the Microsoft Purview compliance portal requires users to apply a label on save/publish.
- **D:** Incorrect for this requirement. Item-level Read metadata permission lets a user connect to a Lakehouse or Warehouse item container without granting broad OneLake file access; combine with SELECT or OneLake security roles for granular least-privilege access. Why the keyed choice wins: Configuring a mandatory sensitivity label policy in the Microsoft Purview compliance portal requires users to apply a label on save/publish.

### Question 11 — D

Answer: Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal. `Certified` endorsement requires explicit authorization from a Fabric Administrator and designates formally vetted datasets. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Local study-map skill 1.5 (Endorse Items Using Promoted, Certified, and Master Data Governance Badges), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Endorsement (Promoted, Certified, Master data) in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview).

- **A:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: `Certified` endorsement requires explicit authorization from a Fabric Administrator and designates formally vetted datasets.
- **B:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: `Certified` endorsement requires explicit authorization from a Fabric Administrator and designates formally vetted datasets.
- **C:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: `Certified` endorsement requires explicit authorization from a Fabric Administrator and designates formally vetted datasets.
- **D:** Correct. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. In this scenario: `Certified` endorsement requires explicit authorization from a Fabric Administrator and designates formally vetted datasets.

### Question 12 — C

Answer: Mark the item as Promoted in item settings. `Promoted` endorsement is available to any item owner or collaborator with write access to highlight ready-to-share content. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Local study-map skill 1.5 (Endorse Items Using Promoted, Certified, and Master Data Governance Badges), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Endorsement (Promoted, Certified, Master data) in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview).

- **A:** Incorrect for this requirement. While sensitivity labels in Fabric classify items in the workspace without encrypting OneLake Delta storage itself, encryption-enabled labels enforce rights management automatically when users export data to Excel, PDF, PowerPoint, or .pbix. Why the keyed choice wins: `Promoted` endorsement is available to any item owner or collaborator with write access to highlight ready-to-share content.
- **B:** Incorrect for this requirement. Fabric admins can enable Master data endorsement for authoritative single-source-of-truth silver/gold data assets so analysts distinguish core reference items in the OneLake catalog. Why the keyed choice wins: `Promoted` endorsement is available to any item owner or collaborator with write access to highlight ready-to-share content.
- **C:** Correct. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. In this scenario: `Promoted` endorsement is available to any item owner or collaborator with write access to highlight ready-to-share content.
- **D:** Incorrect for this requirement. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Why the keyed choice wins: `Promoted` endorsement is available to any item owner or collaborator with write access to highlight ready-to-share content.

### Question 13 — C

Answer: Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch. Selecting `Branch out` creates a dedicated isolated workspace linked to a new feature branch until changes pass pull-request review. In Fabric Git integration, workspaces map 1-to-1 to branches; branching out into a dedicated developer workspace isolates in-progress notebook, pipeline, and semantic model edits before merging via pull request. Local study-map skill 1.6 (Configure Workspace Version Control with Azure DevOps or GitHub (Branch Out, Commit, Update, Undo)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to Git integration in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration).

- **A:** Incorrect for this requirement. Undo reverts uncommitted workspace item modifications to match the connected Git branch HEAD without rewriting shared remote commit history. Why the keyed choice wins: Selecting `Branch out` creates a dedicated isolated workspace linked to a new feature branch until changes pass pull-request review.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Selecting `Branch out` creates a dedicated isolated workspace linked to a new feature branch until changes pass pull-request review.
- **C:** Correct. In Fabric Git integration, workspaces map 1-to-1 to branches; branching out into a dedicated developer workspace isolates in-progress notebook, pipeline, and semantic model edits before merging via pull request. In this scenario: Selecting `Branch out` creates a dedicated isolated workspace linked to a new feature branch until changes pass pull-request review.
- **D:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Selecting `Branch out` creates a dedicated isolated workspace linked to a new feature branch until changes pass pull-request review.

### Question 14 — B

Answer: Connect shared Dev workspace to main → Branch out to an isolated developer workspace and commit .pbip/Notebook edits → Merge pull request into main in Git → Run Update all in Dev and promote via Deployment Pipeline. Connecting `Dev` to `main`, branching out to an isolated workspace, merging the PR into `main`, running `Update all` in `Dev`, and promoting via Deployment Pipeline keeps stages aligned. Correct order: link Dev to main, branch out to an isolated workspace for feature work, validate and merge via Git PR into main, run Update all in Dev, and promote via Deployment Pipeline with stage rules. Local study-map skill 1.6 (Configure Workspace Version Control with Azure DevOps or GitHub (Branch Out, Commit, Update, Undo)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to Git integration in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration).

- **A:** Incorrect for this requirement. Incorrect: Fabric workspaces do not auto-pull remote PR merges — skipping Update from Git promotes stale pre-PR workspace state to Test. Why the keyed choice wins: Connecting `Dev` to `main`, branching out to an isolated workspace, merging the PR into `main`, running `Update all` in `Dev`, and promoting via Deployment Pipeline keeps stages aligned.
- **B:** Correct. Correct order: link Dev to main, branch out to an isolated workspace for feature work, validate and merge via Git PR into main, run Update all in Dev, and promote via Deployment Pipeline with stage rules. In this scenario: Connecting `Dev` to `main`, branching out to an isolated workspace, merging the PR into `main`, running `Update all` in `Dev`, and promoting via Deployment Pipeline keeps stages aligned.
- **C:** Incorrect for this requirement. Incorrect: editing Production directly on feature branches and committing cache.abf violates ALM isolation, leaks cached data, and bypasses Test validation. Why the keyed choice wins: Connecting `Dev` to `main`, branching out to an isolated workspace, merging the PR into `main`, running `Update all` in `Dev`, and promoting via Deployment Pipeline keeps stages aligned.
- **D:** Incorrect for this requirement. Incorrect: My Workspace does not support full team Git ALM, Undo discards local changes rather than committing, and deleting .platform breaks item lineage. Why the keyed choice wins: Connecting `Dev` to `main`, branching out to an isolated workspace, merging the PR into `main`, running `Update all` in `Dev`, and promoting via Deployment Pipeline keeps stages aligned.

### Question 15 — C

Answer: Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions. Saving as a Power BI Desktop project (`.pbip`) stores semantic-model definitions in TMDL text files and report layouts in PBIR JSON files for line-by-line Git diffs. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. Local study-map skill 1.7 (Create and Manage Power BI Desktop Projects (.pbip) with TMDL, PBIR, and .gitignore Hygiene), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Power BI Desktop projects (.pbip), TMDL, and PBIR (https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Saving as a Power BI Desktop project (`.pbip`) stores semantic-model definitions in TMDL text files and report layouts in PBIR JSON files for line-by-line Git diffs.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Saving as a Power BI Desktop project (`.pbip`) stores semantic-model definitions in TMDL text files and report layouts in PBIR JSON files for line-by-line Git diffs.
- **C:** Correct. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. In this scenario: Saving as a Power BI Desktop project (`.pbip`) stores semantic-model definitions in TMDL text files and report layouts in PBIR JSON files for line-by-line Git diffs.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Saving as a Power BI Desktop project (`.pbip`) stores semantic-model definitions in TMDL text files and report layouts in PBIR JSON files for line-by-line Git diffs.

### Question 16 — B, C

Answers: Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions; Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository. Human-readable `.tmdl` + PBIR definition folders should be tracked in Git, while `**/cache.abf` and `**/localSettings.json` must be excluded via `.gitignore`. Local study-map skill 1.7 (Create and Manage Power BI Desktop Projects (.pbip) with TMDL, PBIR, and .gitignore Hygiene), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Power BI Desktop projects (.pbip), TMDL, and PBIR (https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview).

- **A:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Human-readable `.tmdl` + PBIR definition folders should be tracked in Git, while `**/cache.abf` and `**/localSettings.json` must be excluded via `.gitignore`.
- **B:** Correct. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. In this scenario: Human-readable `.tmdl` + PBIR definition folders should be tracked in Git, while `**/cache.abf` and `**/localSettings.json` must be excluded via `.gitignore`.
- **C:** Correct. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. In this scenario: Human-readable `.tmdl` + PBIR definition folders should be tracked in Git, while `**/cache.abf` and `**/localSettings.json` must be excluded via `.gitignore`.
- **D:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Human-readable `.tmdl` + PBIR definition folders should be tracked in Git, while `**/cache.abf` and `**/localSettings.json` must be excluded via `.gitignore`.
- **E:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Human-readable `.tmdl` + PBIR definition folders should be tracked in Git, while `**/cache.abf` and `**/localSettings.json` must be excluded via `.gitignore`.

### Question 17 — D

Answer: Configure Deployment pipeline data source and parameter rules on the Test and Production stages. Defining a Deployment Pipeline data source rule (or parameter rule) on the `Production` stage automatically rebinds the model to `prod-erp-sql.database.windows.net`. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Defining a Deployment Pipeline data source rule (or parameter rule) on the `Production` stage automatically rebinds the model to `prod-erp-sql.database.windows.net`.
- **B:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Defining a Deployment Pipeline data source rule (or parameter rule) on the `Production` stage automatically rebinds the model to `prod-erp-sql.database.windows.net`.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Defining a Deployment Pipeline data source rule (or parameter rule) on the `Production` stage automatically rebinds the model to `prod-erp-sql.database.windows.net`.
- **D:** Correct. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. In this scenario: Defining a Deployment Pipeline data source rule (or parameter rule) on the `Production` stage automatically rebinds the model to `prod-erp-sql.database.windows.net`.

### Question 18 — B

Answer: Perform a selective deployment selecting the modified item together with Select related to include required upstream dependencies. Selecting `CarrierScorecardReport` and choosing `Select related` executes a selective deployment including only required upstream dependencies. Selective deployment in Fabric Deployment Pipelines promotes only chosen items between stages, and Select related ensures newly referenced lakehouses or semantic models deploy alongside dependent reports. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Selecting `CarrierScorecardReport` and choosing `Select related` executes a selective deployment including only required upstream dependencies.
- **B:** Correct. Selective deployment in Fabric Deployment Pipelines promotes only chosen items between stages, and Select related ensures newly referenced lakehouses or semantic models deploy alongside dependent reports. In this scenario: Selecting `CarrierScorecardReport` and choosing `Select related` executes a selective deployment including only required upstream dependencies.
- **C:** Incorrect for this requirement. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. Why the keyed choice wins: Selecting `CarrierScorecardReport` and choosing `Select related` executes a selective deployment including only required upstream dependencies.
- **D:** Incorrect for this requirement. Undo reverts uncommitted workspace item modifications to match the connected Git branch HEAD without rewriting shared remote commit history. Why the keyed choice wins: Selecting `CarrierScorecardReport` and choosing `Select related` executes a selective deployment including only required upstream dependencies.

### Question 19 — C

Answer: Use a Fabric Variable library (or autobinding across paired workspace items) to parameterize stage-specific environment references. A Fabric `Variable library` manages stage-specific workspace/lakehouse GUIDs and endpoints across Deployment Pipeline stages. Fabric Variable libraries store stage-specific workspace/lakehouse IDs, URLs, and thresholds across Dev/Test/Prod — essential for items like Data Pipelines and Direct Lake on OneLake models that do not use legacy SQL deployment rules. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: A Fabric `Variable library` manages stage-specific workspace/lakehouse GUIDs and endpoints across Deployment Pipeline stages.
- **B:** Incorrect for this requirement. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Why the keyed choice wins: A Fabric `Variable library` manages stage-specific workspace/lakehouse GUIDs and endpoints across Deployment Pipeline stages.
- **C:** Correct. Fabric Variable libraries store stage-specific workspace/lakehouse IDs, URLs, and thresholds across Dev/Test/Prod — essential for items like Data Pipelines and Direct Lake on OneLake models that do not use legacy SQL deployment rules. In this scenario: A Fabric `Variable library` manages stage-specific workspace/lakehouse GUIDs and endpoints across Deployment Pipeline stages.
- **D:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: A Fabric `Variable library` manages stage-specific workspace/lakehouse GUIDs and endpoints across Deployment Pipeline stages.

### Question 20 — C

Answer: Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts. Switching to `Lineage` view, opening the `Impact analysis` side pane on `WarehouseLakehouse`, and selecting `Notify contacts` identifies and notifies all downstream owners. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Local study-map skill 1.9 (Perform Downstream Dependency Impact Analysis Across Lakehouses, Warehouses, Dataflows, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Lineage and impact analysis in Microsoft Fabric workspaces (https://learn.microsoft.com/en-us/fabric/governance/lineage).

- **A:** Incorrect for this requirement. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. Why the keyed choice wins: Switching to `Lineage` view, opening the `Impact analysis` side pane on `WarehouseLakehouse`, and selecting `Notify contacts` identifies and notifies all downstream owners.
- **B:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: Switching to `Lineage` view, opening the `Impact analysis` side pane on `WarehouseLakehouse`, and selecting `Notify contacts` identifies and notifies all downstream owners.
- **C:** Correct. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. In this scenario: Switching to `Lineage` view, opening the `Impact analysis` side pane on `WarehouseLakehouse`, and selecting `Notify contacts` identifies and notifies all downstream owners.
- **D:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Switching to `Lineage` view, opening the `Impact analysis` side pane on `WarehouseLakehouse`, and selecting `Notify contacts` identifies and notifies all downstream owners.

### Question 21 — C

Answer: Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts. `Lineage` view visualizes end-to-end upstream-to-downstream dataflow chains alongside live refresh timestamps and failure indicators on one canvas. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Local study-map skill 1.9 (Perform Downstream Dependency Impact Analysis Across Lakehouses, Warehouses, Dataflows, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Lineage and impact analysis in Microsoft Fabric workspaces (https://learn.microsoft.com/en-us/fabric/governance/lineage).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Lineage` view visualizes end-to-end upstream-to-downstream dataflow chains alongside live refresh timestamps and failure indicators on one canvas.
- **B:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: `Lineage` view visualizes end-to-end upstream-to-downstream dataflow chains alongside live refresh timestamps and failure indicators on one canvas.
- **C:** Correct. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. In this scenario: `Lineage` view visualizes end-to-end upstream-to-downstream dataflow chains alongside live refresh timestamps and failure indicators on one canvas.
- **D:** Incorrect for this requirement. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Why the keyed choice wins: `Lineage` view visualizes end-to-end upstream-to-downstream dataflow chains alongside live refresh timestamps and failure indicators on one canvas.

### Question 22 — C

Answer: Verify XMLA Endpoint = Read Write on target capacity → Connect ALM Toolkit to Dev source and Prod XMLA target → Compare schemas while hiding unchanged partitions and keeping Prod data sources → Validate and deploy metadata-only TMSL changes. Verifying `XMLA Endpoint = Read Write`, connecting ALM Toolkit to Dev and Prod, hiding unchanged partitions while retaining Prod data sources, and deploying metadata-only TMSL diffs avoids reprocessing. Correct order: confirm Read Write XMLA capacity setting, compare Dev vs Prod models, preserve Prod partition state and data-source bindings, and push metadata-only measure/relationship diffs. Local study-map skill 1.10 (Deploy and Manage Semantic Models Using the XMLA Endpoint (Read-Write, TMSL, Tabular Editor, ALM Toolkit)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model connectivity and management with the XMLA endpoint (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools).

- **A:** Incorrect for this requirement. Incorrect: Read Only XMLA rejects TMSL model deployments, and Capacity Admin rights violate least privilege. Why the keyed choice wins: Verifying `XMLA Endpoint = Read Write`, connecting ALM Toolkit to Dev and Prod, hiding unchanged partitions while retaining Prod data sources, and deploying metadata-only TMSL diffs avoids reprocessing.
- **B:** Incorrect for this requirement. Incorrect: XMLA Off blocks external deployment, and overwriting Production with an unpartitioned file destroys incremental partitions and causes prolonged outage. Why the keyed choice wins: Verifying `XMLA Endpoint = Read Write`, connecting ALM Toolkit to Dev and Prod, hiding unchanged partitions while retaining Prod data sources, and deploying metadata-only TMSL diffs avoids reprocessing.
- **C:** Correct. Correct order: confirm Read Write XMLA capacity setting, compare Dev vs Prod models, preserve Prod partition state and data-source bindings, and push metadata-only measure/relationship diffs. In this scenario: Verifying `XMLA Endpoint = Read Write`, connecting ALM Toolkit to Dev and Prod, hiding unchanged partitions while retaining Prod data sources, and deploying metadata-only TMSL diffs avoids reprocessing.
- **D:** Incorrect for this requirement. Incorrect: DAX Studio is a query/profiling tool (not a model-deployment tool), and unversioned Production hotfixes cause immediate drift on next deployment. Why the keyed choice wins: Verifying `XMLA Endpoint = Read Write`, connecting ALM Toolkit to Dev and Prod, hiding unchanged partitions while retaining Prod data sources, and deploying metadata-only TMSL diffs avoids reprocessing.

### Question 23 — B, C

Answers: Enable XMLA Endpoint = Read Write in Fabric Capacity workload settings and connect to powerbi://api.powerbi.com/v1.0/myorg/<WorkspaceName>; Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition. The Fabric capacity must set `XMLA Endpoint = Read Write`, and executing a granular TMSL / Enhanced Refresh `dataOnly` command reloads only the targeted weekly partition. Local study-map skill 1.10 (Deploy and Manage Semantic Models Using the XMLA Endpoint (Read-Write, TMSL, Tabular Editor, ALM Toolkit)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model connectivity and management with the XMLA endpoint (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools).

- **A:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: The Fabric capacity must set `XMLA Endpoint = Read Write`, and executing a granular TMSL / Enhanced Refresh `dataOnly` command reloads only the targeted weekly partition.
- **B:** Correct. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. In this scenario: The Fabric capacity must set `XMLA Endpoint = Read Write`, and executing a granular TMSL / Enhanced Refresh `dataOnly` command reloads only the targeted weekly partition.
- **C:** Correct. External ALM tools (Tabular Editor, SSMS, ALM Toolkit, SqlPackage/PowerShell Invoke-ASCmd) require workspace Fabric/Premium capacity with XMLA Endpoint set to Read Write to deploy or modify semantic models. In this scenario: The Fabric capacity must set `XMLA Endpoint = Read Write`, and executing a granular TMSL / Enhanced Refresh `dataOnly` command reloads only the targeted weekly partition.
- **D:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: The Fabric capacity must set `XMLA Endpoint = Read Write`, and executing a granular TMSL / Enhanced Refresh `dataOnly` command reloads only the targeted weekly partition.
- **E:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: The Fabric capacity must set `XMLA Endpoint = Read Write`, and executing a granular TMSL / Enhanced Refresh `dataOnly` command reloads only the targeted weekly partition.

### Question 24 — C

Answer: Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network. Installing an `On-premises data gateway` in High-Availability cluster mode across multiple local servers provides redundant outbound connectivity. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Local study-map skill 2.1 (Create Data Connections (Shareable Cloud Connections, On-Premises Gateways, and VNet Data Gateways)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data source management, cloud connections, and VNet/on-premises gateways in Fabric (https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management).

- **A:** Incorrect for this requirement. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. Why the keyed choice wins: Installing an `On-premises data gateway` in High-Availability cluster mode across multiple local servers provides redundant outbound connectivity.
- **B:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Installing an `On-premises data gateway` in High-Availability cluster mode across multiple local servers provides redundant outbound connectivity.
- **C:** Correct. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. In this scenario: Installing an `On-premises data gateway` in High-Availability cluster mode across multiple local servers provides redundant outbound connectivity.
- **D:** Incorrect for this requirement. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. Why the keyed choice wins: Installing an `On-premises data gateway` in High-Availability cluster mode across multiple local servers provides redundant outbound connectivity.

### Question 25 — B

Answer: Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication. A `Shareable cloud connection` in `Manage connections and gateways` centralizes authentication and grants scoped `Use` permissions to pipeline authors. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. Local study-map skill 2.1 (Create Data Connections (Shareable Cloud Connections, On-Premises Gateways, and VNet Data Gateways)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data source management, cloud connections, and VNet/on-premises gateways in Fabric (https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management).

- **A:** Incorrect for this requirement. With SSO enabled on a Direct Lake model, Fabric evaluates data permissions at the underlying SQL analytics endpoint or OneLake security layer using each viewing report consumer's own Microsoft Entra identity. Why the keyed choice wins: A `Shareable cloud connection` in `Manage connections and gateways` centralizes authentication and grants scoped `Use` permissions to pipeline authors.
- **B:** Correct. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. In this scenario: A `Shareable cloud connection` in `Manage connections and gateways` centralizes authentication and grants scoped `Use` permissions to pipeline authors.
- **C:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: A `Shareable cloud connection` in `Manage connections and gateways` centralizes authentication and grants scoped `Use` permissions to pipeline authors.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: A `Shareable cloud connection` in `Manage connections and gateways` centralizes authentication and grants scoped `Use` permissions to pipeline authors.

### Question 26 — C, E

Answers: Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture; Configure Certified endorsement with the Master data label on authoritative core tables or semantic models. Badging `GlobalPartMaster` with `Certified` + `Master data` endorsement and browsing/auditing via `OneLake catalog` (`Explore` and `Govern` tabs) satisfies both discovery and stewardship. Local study-map skill 2.2 (Discover Data and Streams Using OneLake Catalog (Explore/Govern) and Real-Time Hub + Activator), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake catalog overview & Real-Time hub in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Badging `GlobalPartMaster` with `Certified` + `Master data` endorsement and browsing/auditing via `OneLake catalog` (`Explore` and `Govern` tabs) satisfies both discovery and stewardship.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Badging `GlobalPartMaster` with `Certified` + `Master data` endorsement and browsing/auditing via `OneLake catalog` (`Explore` and `Govern` tabs) satisfies both discovery and stewardship.
- **C:** Correct. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. In this scenario: Badging `GlobalPartMaster` with `Certified` + `Master data` endorsement and browsing/auditing via `OneLake catalog` (`Explore` and `Govern` tabs) satisfies both discovery and stewardship.
- **D:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Badging `GlobalPartMaster` with `Certified` + `Master data` endorsement and browsing/auditing via `OneLake catalog` (`Explore` and `Govern` tabs) satisfies both discovery and stewardship.
- **E:** Correct. Fabric admins can enable Master data endorsement for authoritative single-source-of-truth silver/gold data assets so analysts distinguish core reference items in the OneLake catalog. In this scenario: Badging `GlobalPartMaster` with `Certified` + `Master data` endorsement and browsing/auditing via `OneLake catalog` (`Explore` and `Govern` tabs) satisfies both discovery and stewardship.

### Question 27 — B

Answer: Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog. `Fabric Database Mirroring` for Azure SQL Database streams initial snapshots and ongoing CDC changes automatically into OneLake Delta tables. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `Fabric Database Mirroring` for Azure SQL Database streams initial snapshots and ongoing CDC changes automatically into OneLake Delta tables.
- **B:** Correct. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. In this scenario: `Fabric Database Mirroring` for Azure SQL Database streams initial snapshots and ongoing CDC changes automatically into OneLake Delta tables.
- **C:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: `Fabric Database Mirroring` for Azure SQL Database streams initial snapshots and ongoing CDC changes automatically into OneLake Delta tables.
- **D:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `Fabric Database Mirroring` for Azure SQL Database streams initial snapshots and ongoing CDC changes automatically into OneLake Delta tables.

### Question 28 — B

Answer: Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake. A Data Factory Pipeline `Copy activity` moves multi-terabyte raw Parquet files at peak throughput and minimal CU cost without M or Spark overhead. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` moves multi-terabyte raw Parquet files at peak throughput and minimal CU cost without M or Spark overhead.
- **B:** Correct. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. In this scenario: A Data Factory Pipeline `Copy activity` moves multi-terabyte raw Parquet files at peak throughput and minimal CU cost without M or Spark overhead.
- **C:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` moves multi-terabyte raw Parquet files at peak throughput and minimal CU cost without M or Spark overhead.
- **D:** Incorrect for this requirement. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` moves multi-terabyte raw Parquet files at peak throughput and minimal CU cost without M or Spark overhead.

### Question 29 — B, D, E

Answers: Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations; Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table; Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog. `Dataflow Gen2` with Fast Copy handles visual M transformations, `Eventstream` routes live telemetry, and `Database Mirroring` replicates Snowflake into OneLake. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Dataflow Gen2` with Fast Copy handles visual M transformations, `Eventstream` routes live telemetry, and `Database Mirroring` replicates Snowflake into OneLake.
- **B:** Correct. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. In this scenario: `Dataflow Gen2` with Fast Copy handles visual M transformations, `Eventstream` routes live telemetry, and `Database Mirroring` replicates Snowflake into OneLake.
- **C:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `Dataflow Gen2` with Fast Copy handles visual M transformations, `Eventstream` routes live telemetry, and `Database Mirroring` replicates Snowflake into OneLake.
- **D:** Correct. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. In this scenario: `Dataflow Gen2` with Fast Copy handles visual M transformations, `Eventstream` routes live telemetry, and `Database Mirroring` replicates Snowflake into OneLake.
- **E:** Correct. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. In this scenario: `Dataflow Gen2` with Fast Copy handles visual M transformations, `Eventstream` routes live telemetry, and `Database Mirroring` replicates Snowflake into OneLake.
- **F:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `Dataflow Gen2` with Fast Copy handles visual M transformations, `Eventstream` routes live telemetry, and `Database Mirroring` replicates Snowflake into OneLake.

### Question 30 — A

Answer: Choose a Fabric Eventhouse (KQL database). `Fabric Eventhouse` (KQL database) is purpose-built for high-ingestion streaming time-series and semi-structured JSON telemetry. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Correct. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. In this scenario: `Fabric Eventhouse` (KQL database) is purpose-built for high-ingestion streaming time-series and semi-structured JSON telemetry.
- **B:** Incorrect for this requirement. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) is purpose-built for high-ingestion streaming time-series and semi-structured JSON telemetry.
- **C:** Incorrect for this requirement. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) is purpose-built for high-ingestion streaming time-series and semi-structured JSON telemetry.
- **D:** Incorrect for this requirement. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) is purpose-built for high-ingestion streaming time-series and semi-structured JSON telemetry.

### Question 31 — D

Answer: Choose a Fabric Data Warehouse. `Fabric Data Warehouse` provides full multi-table transactional T-SQL DML and native SQL security over OneLake Delta Parquet. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Incorrect for this requirement. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Why the keyed choice wins: `Fabric Data Warehouse` provides full multi-table transactional T-SQL DML and native SQL security over OneLake Delta Parquet.
- **B:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Fabric Data Warehouse` provides full multi-table transactional T-SQL DML and native SQL security over OneLake Delta Parquet.
- **C:** Incorrect for this requirement. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. Why the keyed choice wins: `Fabric Data Warehouse` provides full multi-table transactional T-SQL DML and native SQL security over OneLake Delta Parquet.
- **D:** Correct. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. In this scenario: `Fabric Data Warehouse` provides full multi-table transactional T-SQL DML and native SQL security over OneLake Delta Parquet.

### Question 32 — B, C

Answers: Choose a Fabric Lakehouse; Choose a SQL database in Microsoft Fabric. `SQL database in Microsoft Fabric` handles operational OLTP transactions (auto-mirrored to OneLake), and `Lakehouse` combines unstructured `Files/` with Spark-managed Delta `Tables/`. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: `SQL database in Microsoft Fabric` handles operational OLTP transactions (auto-mirrored to OneLake), and `Lakehouse` combines unstructured `Files/` with Spark-managed Delta `Tables/`.
- **B:** Correct. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. In this scenario: `SQL database in Microsoft Fabric` handles operational OLTP transactions (auto-mirrored to OneLake), and `Lakehouse` combines unstructured `Files/` with Spark-managed Delta `Tables/`.
- **C:** Correct. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. In this scenario: `SQL database in Microsoft Fabric` handles operational OLTP transactions (auto-mirrored to OneLake), and `Lakehouse` combines unstructured `Files/` with Spark-managed Delta `Tables/`.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `SQL database in Microsoft Fabric` handles operational OLTP transactions (auto-mirrored to OneLake), and `Lakehouse` combines unstructured `Files/` with Spark-managed Delta `Tables/`.
- **E:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `SQL database in Microsoft Fabric` handles operational OLTP transactions (auto-mirrored to OneLake), and `Lakehouse` combines unstructured `Files/` with Spark-managed Delta `Tables/`.

### Question 33 — B

Answer: Enable OneLake integration in the Import semantic model settings so imported model tables export as Delta tables to OneLake. Enabling `OneLake integration` on the Import semantic model exports Delta Parquet folders for its imported tables into OneLake. OneLake integration for Import semantic models writes Delta Parquet artifacts of the model's imported tables into OneLake, allowing Lakehouse shortcuts and Spark/SQL users to reuse curated Power Query model outputs. Local study-map skill 2.5 (Implement OneLake Integration for Eventhouse (OneLake Availability) and Import Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Eventhouse OneLake availability & OneLake integration for semantic models (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/one-lake-availability).

- **A:** Incorrect for this requirement. Eventhouse KQL databases do not write Delta Parquet to OneLake unless OneLake availability is enabled, and Direct Lake on SQL does not support KQL databases (only Direct Lake on OneLake does once OneLake availability is on). Why the keyed choice wins: Enabling `OneLake integration` on the Import semantic model exports Delta Parquet folders for its imported tables into OneLake.
- **B:** Correct. OneLake integration for Import semantic models writes Delta Parquet artifacts of the model's imported tables into OneLake, allowing Lakehouse shortcuts and Spark/SQL users to reuse curated Power Query model outputs. In this scenario: Enabling `OneLake integration` on the Import semantic model exports Delta Parquet folders for its imported tables into OneLake.
- **C:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Enabling `OneLake integration` on the Import semantic model exports Delta Parquet folders for its imported tables into OneLake.
- **D:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Enabling `OneLake integration` on the Import semantic model exports Delta Parquet folders for its imported tables into OneLake.

### Question 34 — C

Answer: Ingest streaming telemetry into an Eventhouse KQL database → Enable OneLake availability on the KQL database or table → Create an internal OneLake shortcut in the Lakehouse → Add the table to a Direct Lake on OneLake semantic model. Landing telemetry in Eventhouse, turning on `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and modeling with Direct Lake on OneLake integrates streams zero-copy. Correct order: land streaming events in Eventhouse, opt in to OneLake availability so Delta Parquet files sync to OneLake, surface via Lakehouse shortcut (or connect directly), and model with Direct Lake on OneLake. Local study-map skill 2.5 (Implement OneLake Integration for Eventhouse (OneLake Availability) and Import Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Eventhouse OneLake availability & OneLake integration for semantic models (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/one-lake-availability).

- **A:** Incorrect for this requirement. Incorrect: Direct Lake on SQL does not support KQL databases, disabling OneLake availability prevents Delta Parquet generation, and Direct Lake never uses gateways. Why the keyed choice wins: Landing telemetry in Eventhouse, turning on `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and modeling with Direct Lake on OneLake integrates streams zero-copy.
- **B:** Incorrect for this requirement. Incorrect: KQL tables are internal OneLake sources that only expose Delta Parquet folders after OneLake availability is enabled. Why the keyed choice wins: Landing telemetry in Eventhouse, turning on `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and modeling with Direct Lake on OneLake integrates streams zero-copy.
- **C:** Correct. Correct order: land streaming events in Eventhouse, opt in to OneLake availability so Delta Parquet files sync to OneLake, surface via Lakehouse shortcut (or connect directly), and model with Direct Lake on OneLake. In this scenario: Landing telemetry in Eventhouse, turning on `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and modeling with Direct Lake on OneLake integrates streams zero-copy.
- **D:** Incorrect for this requirement. Incorrect: manual hourly CSV exports add latency, operational toil, and duplicate storage instead of native Eventhouse OneLake availability. Why the keyed choice wins: Landing telemetry in Eventhouse, turning on `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and modeling with Direct Lake on OneLake integrates streams zero-copy.

### Question 35 — D

Answer: Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic. Lakehouse SQL analytics endpoints are read-only for data manipulation (`INSERT`/`UPDATE`/`DELETE`/`MERGE`); DML stored procedures must target a `Fabric Data Warehouse` (or SQL DB in Fabric). Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Lakehouse SQL analytics endpoints are read-only for data manipulation (`INSERT`/`UPDATE`/`DELETE`/`MERGE`); DML stored procedures must target a `Fabric Data Warehouse` (or SQL DB in Fabric).
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Lakehouse SQL analytics endpoints are read-only for data manipulation (`INSERT`/`UPDATE`/`DELETE`/`MERGE`); DML stored procedures must target a `Fabric Data Warehouse` (or SQL DB in Fabric).
- **C:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Lakehouse SQL analytics endpoints are read-only for data manipulation (`INSERT`/`UPDATE`/`DELETE`/`MERGE`); DML stored procedures must target a `Fabric Data Warehouse` (or SQL DB in Fabric).
- **D:** Correct. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. In this scenario: Lakehouse SQL analytics endpoints are read-only for data manipulation (`INSERT`/`UPDATE`/`DELETE`/`MERGE`); DML stored procedures must target a `Fabric Data Warehouse` (or SQL DB in Fabric).

### Question 36 — D

Answer: Use a Lakehouse Materialized Lake View (or persisted Gold Delta table) instead of a non-materialized SQL analytics endpoint view for Direct Lake on OneLake. `Direct Lake on OneLake` reads physical Delta Parquet files directly from OneLake and does not support non-materialized SQL analytics endpoint views. Non-materialized SQL analytics endpoint views cannot back Direct Lake on OneLake tables and force Direct Lake on SQL into DirectQuery fallback; materializing the view as a Delta table preserves pure in-memory Direct Lake speed. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: `Direct Lake on OneLake` reads physical Delta Parquet files directly from OneLake and does not support non-materialized SQL analytics endpoint views.
- **B:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: `Direct Lake on OneLake` reads physical Delta Parquet files directly from OneLake and does not support non-materialized SQL analytics endpoint views.
- **C:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Direct Lake on OneLake` reads physical Delta Parquet files directly from OneLake and does not support non-materialized SQL analytics endpoint views.
- **D:** Correct. Non-materialized SQL analytics endpoint views cannot back Direct Lake on OneLake tables and force Direct Lake on SQL into DirectQuery fallback; materializing the view as a Delta table preserves pure in-memory Direct Lake speed. In this scenario: `Direct Lake on OneLake` reads physical Delta Parquet files directly from OneLake and does not support non-materialized SQL analytics endpoint views.

### Question 37 — C

Answer: Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic. Creating a T-SQL `VIEW` (`CREATE VIEW`) alongside modular stored procedures encapsulates repeatable filter/projection logic virtually in the Warehouse. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Creating a T-SQL `VIEW` (`CREATE VIEW`) alongside modular stored procedures encapsulates repeatable filter/projection logic virtually in the Warehouse.
- **B:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Creating a T-SQL `VIEW` (`CREATE VIEW`) alongside modular stored procedures encapsulates repeatable filter/projection logic virtually in the Warehouse.
- **C:** Correct. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. In this scenario: Creating a T-SQL `VIEW` (`CREATE VIEW`) alongside modular stored procedures encapsulates repeatable filter/projection logic virtually in the Warehouse.
- **D:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Creating a T-SQL `VIEW` (`CREATE VIEW`) alongside modular stored procedures encapsulates repeatable filter/projection logic virtually in the Warehouse.

### Question 38 — C

Answer: Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions. Assigning an integer surrogate key (`VendorKey`) mapped to `(ERPInstance, NaturalVendorCode)` prevents cross-ERP collisions and supports SCD Type 2 vendor changes. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Assigning an integer surrogate key (`VendorKey`) mapped to `(ERPInstance, NaturalVendorCode)` prevents cross-ERP collisions and supports SCD Type 2 vendor changes.
- **B:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Assigning an integer surrogate key (`VendorKey`) mapped to `(ERPInstance, NaturalVendorCode)` prevents cross-ERP collisions and supports SCD Type 2 vendor changes.
- **C:** Correct. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. In this scenario: Assigning an integer surrogate key (`VendorKey`) mapped to `(ERPInstance, NaturalVendorCode)` prevents cross-ERP collisions and supports SCD Type 2 vendor changes.
- **D:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: Assigning an integer surrogate key (`VendorKey`) mapped to `(ERPInstance, NaturalVendorCode)` prevents cross-ERP collisions and supports SCD Type 2 vendor changes.

### Question 39 — A, D

Answers: Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes; Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions. Adding a contiguous daily Gold `DimCalendar` dimension with ISO-week/shift attributes and replacing composite string natural keys with integer surrogate keys optimizes Direct Lake models. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Correct. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. In this scenario: Adding a contiguous daily Gold `DimCalendar` dimension with ISO-week/shift attributes and replacing composite string natural keys with integer surrogate keys optimizes Direct Lake models.
- **B:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Adding a contiguous daily Gold `DimCalendar` dimension with ISO-week/shift attributes and replacing composite string natural keys with integer surrogate keys optimizes Direct Lake models.
- **C:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Adding a contiguous daily Gold `DimCalendar` dimension with ISO-week/shift attributes and replacing composite string natural keys with integer surrogate keys optimizes Direct Lake models.
- **D:** Correct. A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering. In this scenario: Adding a contiguous daily Gold `DimCalendar` dimension with ISO-week/shift attributes and replacing composite string natural keys with integer surrogate keys optimizes Direct Lake models.
- **E:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Adding a contiguous daily Gold `DimCalendar` dimension with ISO-week/shift attributes and replacing composite string natural keys with integer surrogate keys optimizes Direct Lake models.

### Question 40 — A

Answer: Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns. `SCD Type 2` versions the supplier row with a new surrogate key, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag to preserve historical attribution. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Correct. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. In this scenario: `SCD Type 2` versions the supplier row with a new surrogate key, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag to preserve historical attribution.
- **B:** Incorrect for this requirement. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Why the keyed choice wins: `SCD Type 2` versions the supplier row with a new surrogate key, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag to preserve historical attribution.
- **C:** Incorrect for this requirement. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Why the keyed choice wins: `SCD Type 2` versions the supplier row with a new surrogate key, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag to preserve historical attribution.
- **D:** Incorrect for this requirement. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Why the keyed choice wins: `SCD Type 2` versions the supplier row with a new surrogate key, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag to preserve historical attribution.

### Question 41 — A

Answer: Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures. Enforcing strict uniform atomic grain (either keeping separate Header and Line fact tables or allocating `TotalFreightCost` proportionally by weight/volume across lines) prevents double-counting. Keeping fact tables at a single, consistent atomic grain with integer foreign keys and additive measures eliminates double-counting and supports flexible rollups across every conformed dimension. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Correct. Keeping fact tables at a single, consistent atomic grain with integer foreign keys and additive measures eliminates double-counting and supports flexible rollups across every conformed dimension. In this scenario: Enforcing strict uniform atomic grain (either keeping separate Header and Line fact tables or allocating `TotalFreightCost` proportionally by weight/volume across lines) prevents double-counting.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Enforcing strict uniform atomic grain (either keeping separate Header and Line fact tables or allocating `TotalFreightCost` proportionally by weight/volume across lines) prevents double-counting.
- **C:** Incorrect for this requirement. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Why the keyed choice wins: Enforcing strict uniform atomic grain (either keeping separate Header and Line fact tables or allocating `TotalFreightCost` proportionally by weight/volume across lines) prevents double-counting.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Enforcing strict uniform atomic grain (either keeping separate Header and Line fact tables or allocating `TotalFreightCost` proportionally by weight/volume across lines) prevents double-counting.

### Question 42 — A

Answer: Stage and deduplicate incoming records by natural key → Compare tracked attributes against active (IsCurrent = 1) Gold rows → Expire changed active rows (EffectiveEndDate, IsCurrent = 0) → Insert new active versions with fresh surrogate keys. Deduplicating staged work centers, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves history. Correct order: deduplicate staging first, detect attribute changes against current rows, close out prior active intervals without losing their surrogate keys, and insert new active versions. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Correct. Correct order: deduplicate staging first, detect attribute changes against current rows, close out prior active intervals without losing their surrogate keys, and insert new active versions. In this scenario: Deduplicating staged work centers, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves history.
- **B:** Incorrect for this requirement. Incorrect: new versions must be active (IsCurrent = 1), EffectiveStartDate of historical intervals must remain immutable, and natural keys are required to match future CDC updates. Why the keyed choice wins: Deduplicating staged work centers, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves history.
- **C:** Incorrect for this requirement. Incorrect: deleting unmatched keys and enabling Assume referential integrity omits orphan rows silently in INNER JOINs. Why the keyed choice wins: Deduplicating staged work centers, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves history.
- **D:** Incorrect for this requirement. Incorrect: regenerating surrogate keys on truncate breaks every existing historical fact foreign key, and marking multiple rows IsCurrent = 1 duplicates fact joins. Why the keyed choice wins: Deduplicating staged work centers, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves history.

### Question 43 — A, E, F

Answers: Organize OneLake into Bronze (raw immutable), Silver (validated, deduplicated, conformed), and Gold (star-schema dimensions and facts with V-Order); Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place; Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE. Medallion Bronze/Silver/Gold zones structure the lakehouse, `SCD Type 1` overwrites typos in place without splitting history, and `-1` Unknown surrogate members capture late-arriving foreign keys. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Correct. The Medallion architecture separates raw source fidelity (Bronze), enterprise data quality/conformance (Silver), and BI/Direct Lake star-schema consumption (Gold). In this scenario: Medallion Bronze/Silver/Gold zones structure the lakehouse, `SCD Type 1` overwrites typos in place without splitting history, and `-1` Unknown surrogate members capture late-arriving foreign keys.
- **B:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Medallion Bronze/Silver/Gold zones structure the lakehouse, `SCD Type 1` overwrites typos in place without splitting history, and `-1` Unknown surrogate members capture late-arriving foreign keys.
- **C:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Medallion Bronze/Silver/Gold zones structure the lakehouse, `SCD Type 1` overwrites typos in place without splitting history, and `-1` Unknown surrogate members capture late-arriving foreign keys.
- **D:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Medallion Bronze/Silver/Gold zones structure the lakehouse, `SCD Type 1` overwrites typos in place without splitting history, and `-1` Unknown surrogate members capture late-arriving foreign keys.
- **E:** Correct. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. In this scenario: Medallion Bronze/Silver/Gold zones structure the lakehouse, `SCD Type 1` overwrites typos in place without splitting history, and `-1` Unknown surrogate members capture late-arriving foreign keys.
- **F:** Correct. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. In this scenario: Medallion Bronze/Silver/Gold zones structure the lakehouse, `SCD Type 1` overwrites typos in place without splitting history, and `-1` Unknown surrogate members capture late-arriving foreign keys.

### Question 44 — A

Answer: Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension. Denormalizing snowflake attributes onto `Gold.DimStorageBin` eliminates intermediate relationship hops and reduces query-plan complexity in SQL and DAX. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Local study-map skill 2.9 (Denormalize Snowflake Hierarchies into Flattened Gold Dimension Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Dimensional modeling & denormalizing snowflake tables in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables).

- **A:** Correct. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. In this scenario: Denormalizing snowflake attributes onto `Gold.DimStorageBin` eliminates intermediate relationship hops and reduces query-plan complexity in SQL and DAX.
- **B:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Denormalizing snowflake attributes onto `Gold.DimStorageBin` eliminates intermediate relationship hops and reduces query-plan complexity in SQL and DAX.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Denormalizing snowflake attributes onto `Gold.DimStorageBin` eliminates intermediate relationship hops and reduces query-plan complexity in SQL and DAX.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Denormalizing snowflake attributes onto `Gold.DimStorageBin` eliminates intermediate relationship hops and reduces query-plan complexity in SQL and DAX.

### Question 45 — D

Answer: Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP). Materializing a pre-aggregated `FactDailyShiftQuality` Gold Delta table (`GROUP BY DateKey, PlantKey, ShiftKey`) serves executive dashboards from compact summary rows. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Materializing a pre-aggregated `FactDailyShiftQuality` Gold Delta table (`GROUP BY DateKey, PlantKey, ShiftKey`) serves executive dashboards from compact summary rows.
- **B:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Materializing a pre-aggregated `FactDailyShiftQuality` Gold Delta table (`GROUP BY DateKey, PlantKey, ShiftKey`) serves executive dashboards from compact summary rows.
- **C:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Materializing a pre-aggregated `FactDailyShiftQuality` Gold Delta table (`GROUP BY DateKey, PlantKey, ShiftKey`) serves executive dashboards from compact summary rows.
- **D:** Correct. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. In this scenario: Materializing a pre-aggregated `FactDailyShiftQuality` Gold Delta table (`GROUP BY DateKey, PlantKey, ShiftKey`) serves executive dashboards from compact summary rows.

### Question 46 — D

Answer: GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ()). `GROUP BY GROUPING SETS ((PlantCode, LineId), (PlantCode), ())` — using `GROUPING SETS` — computes multi-grain subtotals and grand total in one pass. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Incorrect for this requirement. In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key. Why the keyed choice wins: `GROUP BY GROUPING SETS ((PlantCode, LineId), (PlantCode), ())` — using `GROUPING SETS` — computes multi-grain subtotals and grand total in one pass.
- **B:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `GROUP BY GROUPING SETS ((PlantCode, LineId), (PlantCode), ())` — using `GROUPING SETS` — computes multi-grain subtotals and grand total in one pass.
- **C:** Incorrect for this requirement. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Why the keyed choice wins: `GROUP BY GROUPING SETS ((PlantCode, LineId), (PlantCode), ())` — using `GROUPING SETS` — computes multi-grain subtotals and grand total in one pass.
- **D:** Correct. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. In this scenario: `GROUP BY GROUPING SETS ((PlantCode, LineId), (PlantCode), ())` — using `GROUPING SETS` — computes multi-grain subtotals and grand total in one pass.

### Question 47 — A

Answer: Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled. Intact query folding pushes `GROUP BY` execution to the remote database engine so only 12,000 summary rows cross the network into the Dataflow mashup container. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Correct. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. In this scenario: Intact query folding pushes `GROUP BY` execution to the remote database engine so only 12,000 summary rows cross the network into the Dataflow mashup container.
- **B:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Intact query folding pushes `GROUP BY` execution to the remote database engine so only 12,000 summary rows cross the network into the Dataflow mashup container.
- **C:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Intact query folding pushes `GROUP BY` execution to the remote database engine so only 12,000 summary rows cross the network into the Dataflow mashup container.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Intact query folding pushes `GROUP BY` execution to the remote database engine so only 12,000 summary rows cross the network into the Dataflow mashup container.

### Question 48 — D

Answer: WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET. `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` skips untouched rows and minimizes Parquet write amplification. Guarding WHEN MATCHED with a hash/attribute inequality prevents rewriting unchanged Delta Parquet files on untouched rows during incremental upserts. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` skips untouched rows and minimizes Parquet write amplification.
- **B:** Incorrect for this requirement. Omitting PARTITION BY ranks across the entire table globally rather than per entity, and RANK() returns duplicate rank-1 rows on exact timestamp ties. Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` skips untouched rows and minimizes Parquet write amplification.
- **C:** Incorrect for this requirement. Fabric Data Warehouse supports FILTER PREDICATE with inline TVFs (not stored procedures or SQL Server DML BLOCK PREDICATE triggers). Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` skips untouched rows and minimizes Parquet write amplification.
- **D:** Correct. Guarding WHEN MATCHED with a hash/attribute inequality prevents rewriting unchanged Delta Parquet files on untouched rows during incremental upserts. In this scenario: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` skips untouched rows and minimizes Parquet write amplification.

### Question 49 — B

Answer: Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table. A `Left Anti Join` from `DimSKU` to October `FactInventoryMovements` returns only SKUs with no matching movement rows. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Why the keyed choice wins: A `Left Anti Join` from `DimSKU` to October `FactInventoryMovements` returns only SKUs with no matching movement rows.
- **B:** Correct. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. In this scenario: A `Left Anti Join` from `DimSKU` to October `FactInventoryMovements` returns only SKUs with no matching movement rows.
- **C:** Incorrect for this requirement. Delta Lake MERGE INTO (in Spark SQL, PySpark DeltaTable.forPath().merge(), or Warehouse T-SQL) atomically applies incremental CDC inserts, updates, and soft-deletes in a single ACID transaction. Why the keyed choice wins: A `Left Anti Join` from `DimSKU` to October `FactInventoryMovements` returns only SKUs with no matching movement rows.
- **D:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: A `Left Anti Join` from `DimSKU` to October `FactInventoryMovements` returns only SKUs with no matching movement rows.

### Question 50 — C, D

Answers: fact_df.join(F.broadcast(dim_store_df), on="StoreKey", how="left"); Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement. `F.broadcast(dim_depot)` prevents shuffling 800M GPS rows across executors, and Delta `MERGE INTO` performs atomic upserts. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: `F.broadcast(dim_depot)` prevents shuffling 800M GPS rows across executors, and Delta `MERGE INTO` performs atomic upserts.
- **B:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `F.broadcast(dim_depot)` prevents shuffling 800M GPS rows across executors, and Delta `MERGE INTO` performs atomic upserts.
- **C:** Correct. Wrapping the small dimension DataFrame in pyspark.sql.functions.broadcast() avoids shuffling the multi-hundred-million-row fact DataFrame across Spark executors. In this scenario: `F.broadcast(dim_depot)` prevents shuffling 800M GPS rows across executors, and Delta `MERGE INTO` performs atomic upserts.
- **D:** Correct. Delta Lake MERGE INTO (in Spark SQL, PySpark DeltaTable.forPath().merge(), or Warehouse T-SQL) atomically applies incremental CDC inserts, updates, and soft-deletes in a single ACID transaction. In this scenario: `F.broadcast(dim_depot)` prevents shuffling 800M GPS rows across executors, and Delta `MERGE INTO` performs atomic upserts.
- **E:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `F.broadcast(dim_depot)` prevents shuffling 800M GPS rows across executors, and Delta `MERGE INTO` performs atomic upserts.

### Question 51 — B

Answer: ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC). `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` deterministically assigns `1` to a single latest record per packet key. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` deterministically assigns `1` to a single latest record per packet key.
- **B:** Correct. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. In this scenario: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` deterministically assigns `1` to a single latest record per packet key.
- **C:** Incorrect for this requirement. Omitting PARTITION BY ranks across the entire table globally rather than per entity, and RANK() returns duplicate rank-1 rows on exact timestamp ties. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` deterministically assigns `1` to a single latest record per packet key.
- **D:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` deterministically assigns `1` to a single latest record per packet key.

### Question 52 — D

Answer: Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE. Mapping `NULL`/unmatched lookups via `COALESCE` to `-1` (`Unknown Dock Door`) in `DimDockDoor` preserves total move counts and keeps `1:*` relationships valid. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. Using >= AND <= on both ends causes rows stamped exactly at midnight on partition boundaries to load into two adjacent partitions, silently double-counting sales totals. Why the keyed choice wins: Mapping `NULL`/unmatched lookups via `COALESCE` to `-1` (`Unknown Dock Door`) in `DimDockDoor` preserves total move counts and keeps `1:*` relationships valid.
- **B:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: Mapping `NULL`/unmatched lookups via `COALESCE` to `-1` (`Unknown Dock Door`) in `DimDockDoor` preserves total move counts and keeps `1:*` relationships valid.
- **C:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Mapping `NULL`/unmatched lookups via `COALESCE` to `-1` (`Unknown Dock Door`) in `DimDockDoor` preserves total move counts and keeps `1:*` relationships valid.
- **D:** Correct. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. In this scenario: Mapping `NULL`/unmatched lookups via `COALESCE` to `-1` (`Unknown Dock Door`) in `DimDockDoor` preserves total move counts and keeps `1:*` relationships valid.

### Question 53 — A, C

Answers: Launch Data Wrangler from a Fabric Spark notebook (or enable Power Query Column profiling based on entire data set) to inspect nulls, duplicates, and distributions and export generated PySpark code; Deduplicate using ROW_NUMBER() OVER (PARTITION BY BusinessKey ORDER BY ModifiedTimestamp DESC) = 1. Profiling across the full dataset in Spark Data Wrangler (or full-dataset Power Query profiling) uncovers tail anomalies, and `ROW_NUMBER() OVER (PARTITION BY ASNNumber ...)` removes duplicates. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Correct. Windowing by BusinessKey ordered descending by ingestion or source-change timestamp deterministically retains only the latest version of duplicate CDC events while preserving all non-key columns. In this scenario: Profiling across the full dataset in Spark Data Wrangler (or full-dataset Power Query profiling) uncovers tail anomalies, and `ROW_NUMBER() OVER (PARTITION BY ASNNumber ...)` removes duplicates.
- **B:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Profiling across the full dataset in Spark Data Wrangler (or full-dataset Power Query profiling) uncovers tail anomalies, and `ROW_NUMBER() OVER (PARTITION BY ASNNumber ...)` removes duplicates.
- **C:** Correct. Power Query profiles only the top 1,000 rows by default unless switched to entire dataset, whereas Data Wrangler interactively profiles Pandas/Spark DataFrames and emits reproducible Python/PySpark cleaning code. In this scenario: Profiling across the full dataset in Spark Data Wrangler (or full-dataset Power Query profiling) uncovers tail anomalies, and `ROW_NUMBER() OVER (PARTITION BY ASNNumber ...)` removes duplicates.
- **D:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Profiling across the full dataset in Spark Data Wrangler (or full-dataset Power Query profiling) uncovers tail anomalies, and `ROW_NUMBER() OVER (PARTITION BY ASNNumber ...)` removes duplicates.
- **E:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Profiling across the full dataset in Spark Data Wrangler (or full-dataset Power Query profiling) uncovers tail anomalies, and `ROW_NUMBER() OVER (PARTITION BY ASNNumber ...)` removes duplicates.

### Question 54 — D

Answer: Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake. Direct Lake excludes `Binary`, `GUID`, and nested `Array`/`Struct`/`Map` Delta types; projecting required array statistics or flattened primitive `DOUBLE`/`STRING` columns resolves compatibility. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. Local study-map skill 2.13 (Convert Column Data Types Safely (TRY_CAST, Fixed Decimal, and Direct Lake Supported Primitive Types)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data types in Fabric Data Warehouse and Direct Lake Delta tables (https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types).

- **A:** Incorrect for this requirement. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Why the keyed choice wins: Direct Lake excludes `Binary`, `GUID`, and nested `Array`/`Struct`/`Map` Delta types; projecting required array statistics or flattened primitive `DOUBLE`/`STRING` columns resolves compatibility.
- **B:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Direct Lake excludes `Binary`, `GUID`, and nested `Array`/`Struct`/`Map` Delta types; projecting required array statistics or flattened primitive `DOUBLE`/`STRING` columns resolves compatibility.
- **C:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Direct Lake excludes `Binary`, `GUID`, and nested `Array`/`Struct`/`Map` Delta types; projecting required array statistics or flattened primitive `DOUBLE`/`STRING` columns resolves compatibility.
- **D:** Correct. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. In this scenario: Direct Lake excludes `Binary`, `GUID`, and nested `Array`/`Struct`/`Map` Delta types; projecting required array statistics or flattened primitive `DOUBLE`/`STRING` columns resolves compatibility.

### Question 55 — A

Answer: Table.SelectRows(Source, each [OrderDate] >= RangeStart and [OrderDate] < RangeEnd). `Table.SelectRows(Source, each [OrderDate] >= RangeStart and [OrderDate] < RangeEnd)` applies the half-open `>=` and `<` interval that folds cleanly into SQL `WHERE`. Power Query M incremental refresh requires exact case-sensitive RangeStart and RangeEnd parameters using >= RangeStart and < RangeEnd so boundary timestamps are never loaded twice. Local study-map skill 2.14 (Filter Data Early Preserving Power Query Folding (View Native Query) and Sargable Delta File Pruning), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query folding indicators & predicate pushdown in Power Query and Delta Lake (https://learn.microsoft.com/en-us/power-query/query-folding-basics).

- **A:** Correct. Power Query M incremental refresh requires exact case-sensitive RangeStart and RangeEnd parameters using >= RangeStart and < RangeEnd so boundary timestamps are never loaded twice. In this scenario: `Table.SelectRows(Source, each [OrderDate] >= RangeStart and [OrderDate] < RangeEnd)` applies the half-open `>=` and `<` interval that folds cleanly into SQL `WHERE`.
- **B:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: `Table.SelectRows(Source, each [OrderDate] >= RangeStart and [OrderDate] < RangeEnd)` applies the half-open `>=` and `<` interval that folds cleanly into SQL `WHERE`.
- **C:** Incorrect for this requirement. Using >= AND <= on both ends causes rows stamped exactly at midnight on partition boundaries to load into two adjacent partitions, silently double-counting sales totals. Why the keyed choice wins: `Table.SelectRows(Source, each [OrderDate] >= RangeStart and [OrderDate] < RangeEnd)` applies the half-open `>=` and `<` interval that folds cleanly into SQL `WHERE`.
- **D:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `Table.SelectRows(Source, each [OrderDate] >= RangeStart and [OrderDate] < RangeEnd)` applies the half-open `>=` and `<` interval that folds cleanly into SQL `WHERE`.

### Question 56 — D

Answer: Filter on physical Delta partition or liquid-clustered date columns using sargable range predicates (OrderDate >= '2026-01-01') without wrapping the column in functions. Replacing `CAST(ReadingDate AS VARCHAR(10))` with sargable `WHERE ReadingDate = '2026-10-30'` lets Delta Lake prune non-matching partitions and Parquet rowgroups via min/max stats. Wrapping a column in YEAR(OrderDate) = 2026 blocks file-level min/max data skipping and partition pruning; sargable range predicates let Spark and SQL endpoints skip irrelevant Parquet files entirely. Local study-map skill 2.14 (Filter Data Early Preserving Power Query Folding (View Native Query) and Sargable Delta File Pruning), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query folding indicators & predicate pushdown in Power Query and Delta Lake (https://learn.microsoft.com/en-us/power-query/query-folding-basics).

- **A:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: Replacing `CAST(ReadingDate AS VARCHAR(10))` with sargable `WHERE ReadingDate = '2026-10-30'` lets Delta Lake prune non-matching partitions and Parquet rowgroups via min/max stats.
- **B:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: Replacing `CAST(ReadingDate AS VARCHAR(10))` with sargable `WHERE ReadingDate = '2026-10-30'` lets Delta Lake prune non-matching partitions and Parquet rowgroups via min/max stats.
- **C:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: Replacing `CAST(ReadingDate AS VARCHAR(10))` with sargable `WHERE ReadingDate = '2026-10-30'` lets Delta Lake prune non-matching partitions and Parquet rowgroups via min/max stats.
- **D:** Correct. Wrapping a column in YEAR(OrderDate) = 2026 blocks file-level min/max data skipping and partition pruning; sargable range predicates let Spark and SQL endpoints skip irrelevant Parquet files entirely. In this scenario: Replacing `CAST(ReadingDate AS VARCHAR(10))` with sargable `WHERE ReadingDate = '2026-10-30'` lets Delta Lake prune non-matching partitions and Parquet rowgroups via min/max stats.

### Question 57 — A

Answer: Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view. The Visual query editor translates the diagram steps into native distributed T-SQL executed directly inside the Warehouse engine. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Local study-map skill 2.15 (Select, Filter, and Aggregate Data Using the Visual Query Editor and Save as SQL Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query using the Visual query editor in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/visual-query-editor).

- **A:** Correct. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. In this scenario: The Visual query editor translates the diagram steps into native distributed T-SQL executed directly inside the Warehouse engine.
- **B:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: The Visual query editor translates the diagram steps into native distributed T-SQL executed directly inside the Warehouse engine.
- **C:** Incorrect for this requirement. ALM Toolkit performs metadata-only diffs and incremental TMSL deployments over XMLA, preserving existing processed historical partitions and incremental refresh windows in Production. Why the keyed choice wins: The Visual query editor translates the diagram steps into native distributed T-SQL executed directly inside the Warehouse engine.
- **D:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: The Visual query editor translates the diagram steps into native distributed T-SQL executed directly inside the Warehouse engine.

### Question 58 — C

Answer: LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC). `LAG(CumulativeCycles, 1, 0) OVER (PARTITION BY MachineId ORDER BY ReadingHour ASC)` subtracts the prior hour's counter value in a single window scan. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `LAG(CumulativeCycles, 1, 0) OVER (PARTITION BY MachineId ORDER BY ReadingHour ASC)` subtracts the prior hour's counter value in a single window scan.
- **B:** Incorrect for this requirement. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Why the keyed choice wins: `LAG(CumulativeCycles, 1, 0) OVER (PARTITION BY MachineId ORDER BY ReadingHour ASC)` subtracts the prior hour's counter value in a single window scan.
- **C:** Correct. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. In this scenario: `LAG(CumulativeCycles, 1, 0) OVER (PARTITION BY MachineId ORDER BY ReadingHour ASC)` subtracts the prior hour's counter value in a single window scan.
- **D:** Incorrect for this requirement. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Why the keyed choice wins: `LAG(CumulativeCycles, 1, 0) OVER (PARTITION BY MachineId ORDER BY ReadingHour ASC)` subtracts the prior hour's counter value in a single window scan.

### Question 59 — B

Answer: Query across a Warehouse and a Lakehouse SQL analytics endpoint in the same workspace using three-part T-SQL naming (SalesLakehouse.dbo.RawOrders). Same-workspace Warehouses and Lakehouse SQL analytics endpoints support direct three-part T-SQL queries (`TelematicsLakehouse.dbo.DriverEvents`). Fabric Warehouse and SQL analytics endpoints inside the same workspace share a unified SQL engine namespace, enabling zero-copy cross-database T-SQL joins via DatabaseName.SchemaName.ObjectName. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Incorrect for this requirement. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. Why the keyed choice wins: Same-workspace Warehouses and Lakehouse SQL analytics endpoints support direct three-part T-SQL queries (`TelematicsLakehouse.dbo.DriverEvents`).
- **B:** Correct. Fabric Warehouse and SQL analytics endpoints inside the same workspace share a unified SQL engine namespace, enabling zero-copy cross-database T-SQL joins via DatabaseName.SchemaName.ObjectName. In this scenario: Same-workspace Warehouses and Lakehouse SQL analytics endpoints support direct three-part T-SQL queries (`TelematicsLakehouse.dbo.DriverEvents`).
- **C:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: Same-workspace Warehouses and Lakehouse SQL analytics endpoints support direct three-part T-SQL queries (`TelematicsLakehouse.dbo.DriverEvents`).
- **D:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Same-workspace Warehouses and Lakehouse SQL analytics endpoints support direct three-part T-SQL queries (`TelematicsLakehouse.dbo.DriverEvents`).

### Question 60 — A, E

Answers: OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000'); CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales. `CREATE TABLE ... AS CLONE OF` creates a zero-copy metadata clone, and `OPTION (FOR TIMESTAMP AS OF ...)` executes Warehouse Time Travel queries. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Correct. Fabric Data Warehouse Time Travel uses the query hint OPTION (FOR TIMESTAMP AS OF 'YYYY-MM-DDTHH:MM:SS.fff') to read exact point-in-time historical snapshots within the retention window. In this scenario: `CREATE TABLE ... AS CLONE OF` creates a zero-copy metadata clone, and `OPTION (FOR TIMESTAMP AS OF ...)` executes Warehouse Time Travel queries.
- **B:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `CREATE TABLE ... AS CLONE OF` creates a zero-copy metadata clone, and `OPTION (FOR TIMESTAMP AS OF ...)` executes Warehouse Time Travel queries.
- **C:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `CREATE TABLE ... AS CLONE OF` creates a zero-copy metadata clone, and `OPTION (FOR TIMESTAMP AS OF ...)` executes Warehouse Time Travel queries.
- **D:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: `CREATE TABLE ... AS CLONE OF` creates a zero-copy metadata clone, and `OPTION (FOR TIMESTAMP AS OF ...)` executes Warehouse Time Travel queries.
- **E:** Correct. CREATE TABLE ... AS CLONE OF creates a zero-copy metadata clone of a Fabric Warehouse table instantaneously (optionally AT a specific UTC timestamp) without duplicating Parquet files. In this scenario: `CREATE TABLE ... AS CLONE OF` creates a zero-copy metadata clone, and `OPTION (FOR TIMESTAMP AS OF ...)` executes Warehouse Time Travel queries.

### Question 61 — B

Answer: Write a KQL query using | where Timestamp > ago(24h) | summarize arg_max(IngestionTime, *) by DeviceId and | summarize AvgTemp = avg(Temp), P95 = percentile(Temp, 95) by bin(Timestamp, 5m). Combining `| summarize arg_max(IngestionTime, *) by DeviceId` for latest entity state and `| summarize ..., percentile(Temp, 95) by bin(Timestamp, 5m)` handles both patterns natively in KQL. In Eventhouse KQL, arg_max() retrieves the full latest row per entity key efficiently, and summarize ... by bin(Timestamp, 5m) buckets irregular streaming timestamps into fixed time windows. Local study-map skill 2.17 (Select, Filter, and Aggregate Data Using KQL (summarize, bin, arg_max, percentile, parse_json, mv-expand)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query data in a KQL queryset in Microsoft Fabric Real-Time Intelligence (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/kql-queryset).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Combining `| summarize arg_max(IngestionTime, *) by DeviceId` for latest entity state and `| summarize ..., percentile(Temp, 95) by bin(Timestamp, 5m)` handles both patterns natively in KQL.
- **B:** Correct. In Eventhouse KQL, arg_max() retrieves the full latest row per entity key efficiently, and summarize ... by bin(Timestamp, 5m) buckets irregular streaming timestamps into fixed time windows. In this scenario: Combining `| summarize arg_max(IngestionTime, *) by DeviceId` for latest entity state and `| summarize ..., percentile(Temp, 95) by bin(Timestamp, 5m)` handles both patterns natively in KQL.
- **C:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Combining `| summarize arg_max(IngestionTime, *) by DeviceId` for latest entity state and `| summarize ..., percentile(Temp, 95) by bin(Timestamp, 5m)` handles both patterns natively in KQL.
- **D:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Combining `| summarize arg_max(IngestionTime, *) by DeviceId` for latest entity state and `| summarize ..., percentile(Temp, 95) by bin(Timestamp, 5m)` handles both patterns natively in KQL.

### Question 62 — C

Answer: Use KQL parse_json() (or dynamic column indexing) followed by | mv-expand SensorReadings to flatten nested JSON arrays before aggregating. `parse_json()` (or dynamic column access) followed by `| mv-expand` flattens nested JSON arrays into one KQL row per axis element. Eventhouse stores semi-structured JSON natively in dynamic columns; mv-expand expands multi-element JSON arrays into individual rows for downstream filtering and summarization. Local study-map skill 2.17 (Select, Filter, and Aggregate Data Using KQL (summarize, bin, arg_max, percentile, parse_json, mv-expand)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query data in a KQL queryset in Microsoft Fabric Real-Time Intelligence (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/kql-queryset).

- **A:** Incorrect for this requirement. percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse. Why the keyed choice wins: `parse_json()` (or dynamic column access) followed by `| mv-expand` flattens nested JSON arrays into one KQL row per axis element.
- **B:** Incorrect for this requirement. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Why the keyed choice wins: `parse_json()` (or dynamic column access) followed by `| mv-expand` flattens nested JSON arrays into one KQL row per axis element.
- **C:** Correct. Eventhouse stores semi-structured JSON natively in dynamic columns; mv-expand expands multi-element JSON arrays into individual rows for downstream filtering and summarization. In this scenario: `parse_json()` (or dynamic column access) followed by `| mv-expand` flattens nested JSON arrays into one KQL row per axis element.
- **D:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `parse_json()` (or dynamic column access) followed by `| mv-expand` flattens nested JSON arrays into one KQL row per axis element.

### Question 63 — D

Answer: Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results. `DAX Query View` runs ad-hoc `DEFINE MEASURE` + `EVALUATE` queries and updates model metadata only when confirmed. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Local study-map skill 2.18 (Select, Filter, and Aggregate Data Using DAX Queries (DAX Query View, EVALUATE, SUMMARIZECOLUMNS, INFO.VIEW)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Work with DAX query view & INFO.VIEW functions in Power BI (https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view).

- **A:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `DAX Query View` runs ad-hoc `DEFINE MEASURE` + `EVALUATE` queries and updates model metadata only when confirmed.
- **B:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: `DAX Query View` runs ad-hoc `DEFINE MEASURE` + `EVALUATE` queries and updates model metadata only when confirmed.
- **C:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: `DAX Query View` runs ad-hoc `DEFINE MEASURE` + `EVALUATE` queries and updates model metadata only when confirmed.
- **D:** Correct. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. In this scenario: `DAX Query View` runs ad-hoc `DEFINE MEASURE` + `EVALUATE` queries and updates model metadata only when confirmed.

### Question 64 — B

Answer: Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View. `COLUMNSTATISTICS()` and the `INFO.VIEW.*` functions (`INFO.VIEW.COLUMNS()`, `INFO.VIEW.MEASURES()`) return model metadata and cardinality profiles directly via DAX. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. Local study-map skill 2.18 (Select, Filter, and Aggregate Data Using DAX Queries (DAX Query View, EVALUATE, SUMMARIZECOLUMNS, INFO.VIEW)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Work with DAX query view & INFO.VIEW functions in Power BI (https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view).

- **A:** Incorrect for this requirement. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Why the keyed choice wins: `COLUMNSTATISTICS()` and the `INFO.VIEW.*` functions (`INFO.VIEW.COLUMNS()`, `INFO.VIEW.MEASURES()`) return model metadata and cardinality profiles directly via DAX.
- **B:** Correct. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. In this scenario: `COLUMNSTATISTICS()` and the `INFO.VIEW.*` functions (`INFO.VIEW.COLUMNS()`, `INFO.VIEW.MEASURES()`) return model metadata and cardinality profiles directly via DAX.
- **C:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: `COLUMNSTATISTICS()` and the `INFO.VIEW.*` functions (`INFO.VIEW.COLUMNS()`, `INFO.VIEW.MEASURES()`) return model metadata and cardinality profiles directly via DAX.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `COLUMNSTATISTICS()` and the `INFO.VIEW.*` functions (`INFO.VIEW.COLUMNS()`, `INFO.VIEW.MEASURES()`) return model metadata and cardinality profiles directly via DAX.

### Question 65 — B

Answer: Configure Direct Lake storage mode. `Direct Lake` loads OneLake Delta Parquet columns directly into VertiPaq memory on demand without scheduled Import duplication. Local study-map skill 3.1 (Choose a Semantic Model Storage Mode (Import, DirectQuery, Direct Lake, and Dual)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model storage modes in the Power BI service & Microsoft Fabric (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Direct Lake` loads OneLake Delta Parquet columns directly into VertiPaq memory on demand without scheduled Import duplication.
- **B:** Correct. In this scenario: `Direct Lake` loads OneLake Delta Parquet columns directly into VertiPaq memory on demand without scheduled Import duplication.
- **C:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Direct Lake` loads OneLake Delta Parquet columns directly into VertiPaq memory on demand without scheduled Import duplication.
- **D:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Direct Lake` loads OneLake Delta Parquet columns directly into VertiPaq memory on demand without scheduled Import duplication.

### Question 66 — B

Answer: Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column. Disabling `Auto date/time` and running `Mark as date table` on `DimDate` designating `CalendarDate` (`Date` data type) enables native DAX time intelligence over integer keys. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. Local study-map skill 3.2 (Implement a Star Schema for a Semantic Model (Mark as Date Table, Hide Keys, Sort by Column, Display Folders)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Set and use date tables & star-schema best practices in Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables).

- **A:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Disabling `Auto date/time` and running `Mark as date table` on `DimDate` designating `CalendarDate` (`Date` data type) enables native DAX time intelligence over integer keys.
- **B:** Correct. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. In this scenario: Disabling `Auto date/time` and running `Mark as date table` on `DimDate` designating `CalendarDate` (`Date` data type) enables native DAX time intelligence over integer keys.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Disabling `Auto date/time` and running `Mark as date table` on `DimDate` designating `CalendarDate` (`Date` data type) enables native DAX time intelligence over integer keys.
- **D:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: Disabling `Auto date/time` and running `Mark as date table` on `DimDate` designating `CalendarDate` (`Date` data type) enables native DAX time intelligence over integer keys.

### Question 67 — A, B

Answers: Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column; Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear. Disabling `Auto date/time` + marking `DimDate` removes hidden tables, and hiding technical keys/raw fact columns while setting `Sort by Column` enforces clean self-service modeling. Local study-map skill 3.2 (Implement a Star Schema for a Semantic Model (Mark as Date Table, Hide Keys, Sort by Column, Display Folders)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Set and use date tables & star-schema best practices in Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables).

- **A:** Correct. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. In this scenario: Disabling `Auto date/time` + marking `DimDate` removes hidden tables, and hiding technical keys/raw fact columns while setting `Sort by Column` enforces clean self-service modeling.
- **B:** Correct. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. In this scenario: Disabling `Auto date/time` + marking `DimDate` removes hidden tables, and hiding technical keys/raw fact columns while setting `Sort by Column` enforces clean self-service modeling.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Disabling `Auto date/time` + marking `DimDate` removes hidden tables, and hiding technical keys/raw fact columns while setting `Sort by Column` enforces clean self-service modeling.
- **D:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Disabling `Auto date/time` + marking `DimDate` removes hidden tables, and hiding technical keys/raw fact columns while setting `Sort by Column` enforces clean self-service modeling.
- **E:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Disabling `Auto date/time` + marking `DimDate` removes hidden tables, and hiding technical keys/raw fact columns while setting `Sort by Column` enforces clean self-service modeling.

### Question 68 — C

Answer: CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey])). `CALCULATE([Base Measure], USERELATIONSHIP('Calendar'[DateKey], 'Fact...'[InactiveDateKey]))` activates the chosen role-playing date relationship dynamically. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: `CALCULATE([Base Measure], USERELATIONSHIP('Calendar'[DateKey], 'Fact...'[InactiveDateKey]))` activates the chosen role-playing date relationship dynamically.
- **B:** Incorrect for this requirement. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. Why the keyed choice wins: `CALCULATE([Base Measure], USERELATIONSHIP('Calendar'[DateKey], 'Fact...'[InactiveDateKey]))` activates the chosen role-playing date relationship dynamically.
- **C:** Correct. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. In this scenario: `CALCULATE([Base Measure], USERELATIONSHIP('Calendar'[DateKey], 'Fact...'[InactiveDateKey]))` activates the chosen role-playing date relationship dynamically.
- **D:** Incorrect for this requirement. CROSSFILTER(..., BOTH) enables bidirectional filter propagation across a bridge table only inside the specific measure rather than globally across the model. Why the keyed choice wins: `CALCULATE([Base Measure], USERELATIONSHIP('Calendar'[DateKey], 'Fact...'[InactiveDateKey]))` activates the chosen role-playing date relationship dynamically.

### Question 69 — B

Answer: Introduce a deduplicated Bridge table between the two dimensions and scope bidirectional propagation strictly inside specific measures using CROSSFILTER(..., BOTH). Use `1:*` single-direction relationships into `BridgeIncidentCause` by default and invoke `CROSSFILTER(..., BOTH)` strictly inside specific root-cause measures. Scoping CROSSFILTER(..., BOTH) inside a DAX measure over a bridge table satisfies many-to-many attribution without turning on permanent model-wide bidirectional relationships that cause ambiguity and performance degradation. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Why the keyed choice wins: Use `1:*` single-direction relationships into `BridgeIncidentCause` by default and invoke `CROSSFILTER(..., BOTH)` strictly inside specific root-cause measures.
- **B:** Correct. Scoping CROSSFILTER(..., BOTH) inside a DAX measure over a bridge table satisfies many-to-many attribution without turning on permanent model-wide bidirectional relationships that cause ambiguity and performance degradation. In this scenario: Use `1:*` single-direction relationships into `BridgeIncidentCause` by default and invoke `CROSSFILTER(..., BOTH)` strictly inside specific root-cause measures.
- **C:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: Use `1:*` single-direction relationships into `BridgeIncidentCause` by default and invoke `CROSSFILTER(..., BOTH)` strictly inside specific root-cause measures.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Use `1:*` single-direction relationships into `BridgeIncidentCause` by default and invoke `CROSSFILTER(..., BOTH)` strictly inside specific root-cause measures.

### Question 70 — B

Answer: Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid. Power BI emits faster `INNER JOIN` clauses instead of `LEFT OUTER JOIN` clauses when pushing queries to the Warehouse SQL engine. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Why the keyed choice wins: Power BI emits faster `INNER JOIN` clauses instead of `LEFT OUTER JOIN` clauses when pushing queries to the Warehouse SQL engine.
- **B:** Correct. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. In this scenario: Power BI emits faster `INNER JOIN` clauses instead of `LEFT OUTER JOIN` clauses when pushing queries to the Warehouse SQL engine.
- **C:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Power BI emits faster `INNER JOIN` clauses instead of `LEFT OUTER JOIN` clauses when pushing queries to the Warehouse SQL engine.
- **D:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: Power BI emits faster `INNER JOIN` clauses instead of `LEFT OUTER JOIN` clauses when pushing queries to the Warehouse SQL engine.

### Question 71 — A

Answer: Use DAX window functions OFFSET(-1, ALLSELECTED(DimDate[YearMonth]), ORDERBY(DimDate[YearMonthNum], ASC)) or WINDOW() with PARTITIONBY(). DAX windowing functions (`OFFSET(-1, ALLSELECTED(...), ORDERBY(...))`, `INDEX`, `WINDOW`) step across custom sorted partitions cleanly without Gregorian date requirements. DAX windowing functions (OFFSET, INDEX, WINDOW) navigate sorted/partitioned visual axes directly even for custom fiscal calendars where standard DATEADD/SAMEPERIODLASTYEAR functions fail. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Correct. DAX windowing functions (OFFSET, INDEX, WINDOW) navigate sorted/partitioned visual axes directly even for custom fiscal calendars where standard DATEADD/SAMEPERIODLASTYEAR functions fail. In this scenario: DAX windowing functions (`OFFSET(-1, ALLSELECTED(...), ORDERBY(...))`, `INDEX`, `WINDOW`) step across custom sorted partitions cleanly without Gregorian date requirements.
- **B:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: DAX windowing functions (`OFFSET(-1, ALLSELECTED(...), ORDERBY(...))`, `INDEX`, `WINDOW`) step across custom sorted partitions cleanly without Gregorian date requirements.
- **C:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: DAX windowing functions (`OFFSET(-1, ALLSELECTED(...), ORDERBY(...))`, `INDEX`, `WINDOW`) step across custom sorted partitions cleanly without Gregorian date requirements.
- **D:** Incorrect for this requirement. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Why the keyed choice wins: DAX windowing functions (`OFFSET(-1, ALLSELECTED(...), ORDERBY(...))`, `INDEX`, `WINDOW`) step across custom sorted partitions cleanly without Gregorian date requirements.

### Question 72 — A

Answer: Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table. `SUMX` iterates `FactScrapRuns` and multiplies `ScrapUnits * RELATED(DimPart[StandardUnitCost])` in memory before summing. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Correct. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. In this scenario: `SUMX` iterates `FactScrapRuns` and multiplies `ScrapUnits * RELATED(DimPart[StandardUnitCost])` in memory before summing.
- **B:** Incorrect for this requirement. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. Why the keyed choice wins: `SUMX` iterates `FactScrapRuns` and multiplies `ScrapUnits * RELATED(DimPart[StandardUnitCost])` in memory before summing.
- **C:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: `SUMX` iterates `FactScrapRuns` and multiplies `ScrapUnits * RELATED(DimPart[StandardUnitCost])` in memory before summing.
- **D:** Incorrect for this requirement. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Why the keyed choice wins: `SUMX` iterates `FactScrapRuns` and multiplies `ScrapUnits * RELATED(DimPart[StandardUnitCost])` in memory before summing.

### Question 73 — D

Answer: Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches. Defining `VAR MachineHrs = [Net Machine Hours]` once above `RETURN` caches the measure value and eliminates four redundant evaluations. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Defining `VAR MachineHrs = [Net Machine Hours]` once above `RETURN` caches the measure value and eliminates four redundant evaluations.
- **B:** Incorrect for this requirement. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Why the keyed choice wins: Defining `VAR MachineHrs = [Net Machine Hours]` once above `RETURN` caches the measure value and eliminates four redundant evaluations.
- **C:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: Defining `VAR MachineHrs = [Net Machine Hours]` once above `RETURN` caches the measure value and eliminates four redundant evaluations.
- **D:** Correct. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. In this scenario: Defining `VAR MachineHrs = [Net Machine Hours]` once above `RETURN` caches the measure value and eliminates four redundant evaluations.

### Question 74 — C, D

Answers: Pass simple column predicates wrapped in KEEPFILTERS(DimProduct[Color] = "Red") to CALCULATE instead of FILTER(ALL(FactSales), ...); Use ISINSCOPE(DimProduct[Subcategory]) (or SELECTEDVALUE with an alternate result) to branch measure behavior cleanly across matrix hierarchy levels. `KEEPFILTERS` preserves outer slicer intersections without table-scan `FILTER(Fact, ...)`, and `ISINSCOPE('DimLine'[WorkCenter])` detects active hierarchy levels accurately. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: `KEEPFILTERS` preserves outer slicer intersections without table-scan `FILTER(Fact, ...)`, and `ISINSCOPE('DimLine'[WorkCenter])` detects active hierarchy levels accurately.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: `KEEPFILTERS` preserves outer slicer intersections without table-scan `FILTER(Fact, ...)`, and `ISINSCOPE('DimLine'[WorkCenter])` detects active hierarchy levels accurately.
- **C:** Correct. ISINSCOPE returns TRUE only when the specified column is actively grouping the current visual row/column level, making it superior to HASONEVALUE for subtotal vs leaf detection in matrices. In this scenario: `KEEPFILTERS` preserves outer slicer intersections without table-scan `FILTER(Fact, ...)`, and `ISINSCOPE('DimLine'[WorkCenter])` detects active hierarchy levels accurately.
- **D:** Correct. KEEPFILTERS intersects the predicate with existing report slicer selections rather than overwriting them, and filtering a dimension column avoids scanning the entire multi-million-row fact table in the Formula Engine. In this scenario: `KEEPFILTERS` preserves outer slicer intersections without table-scan `FILTER(Fact, ...)`, and `ISINSCOPE('DimLine'[WorkCenter])` detects active hierarchy levels accurately.
- **E:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: `KEEPFILTERS` preserves outer slicer intersections without table-scan `FILTER(Fact, ...)`, and `ISINSCOPE('DimLine'[WorkCenter])` detects active hierarchy levels accurately.

### Question 75 — C

Answer: Create a Calculation Group with Calculation Items referencing SELECTEDMEASURE() and explicit Precedence ordering (automatically setting DiscourageImplicitMeasures = true). A `Calculation Group` with 6 calculation items invoking `SELECTEDMEASURE()` applies horizon logic orthogonal to all 30 base measures. A single Calculation Group applies reusable logic (YTD, PY, YoY%, Moving Avg) across dozens of base measures via SELECTEDMEASURE(), eliminating measure explosion (`50 base * 6 time calcs = 300 measures`). Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: A `Calculation Group` with 6 calculation items invoking `SELECTEDMEASURE()` applies horizon logic orthogonal to all 30 base measures.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: A `Calculation Group` with 6 calculation items invoking `SELECTEDMEASURE()` applies horizon logic orthogonal to all 30 base measures.
- **C:** Correct. A single Calculation Group applies reusable logic (YTD, PY, YoY%, Moving Avg) across dozens of base measures via SELECTEDMEASURE(), eliminating measure explosion (`50 base * 6 time calcs = 300 measures`). In this scenario: A `Calculation Group` with 6 calculation items invoking `SELECTEDMEASURE()` applies horizon logic orthogonal to all 30 base measures.
- **D:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: A `Calculation Group` with 6 calculation items invoking `SELECTEDMEASURE()` applies horizon logic orthogonal to all 30 base measures.

### Question 76 — C

Answer: Configure a Dynamic Format String expression on the measure or calculation item (for example returning "\$#,0.00" vs "0.0%" via SELECTEDMEASUREFORMATSTRING()) without wrapping values in FORMAT(). Configuring a `Dynamic Format String` expression returns `"$#,0"`, `"#,0"`, or `"0.0%"` dynamically without converting numbers to strings via `FORMAT()`. Unlike FORMAT() — which converts numbers into text strings and breaks chart axes/sorting/aggregations — Dynamic Format Strings preserve true numeric data types while rendering context-aware currency or percentage formatting. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Configuring a `Dynamic Format String` expression returns `"$#,0"`, `"#,0"`, or `"0.0%"` dynamically without converting numbers to strings via `FORMAT()`.
- **B:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Configuring a `Dynamic Format String` expression returns `"$#,0"`, `"#,0"`, or `"0.0%"` dynamically without converting numbers to strings via `FORMAT()`.
- **C:** Correct. Unlike FORMAT() — which converts numbers into text strings and breaks chart axes/sorting/aggregations — Dynamic Format Strings preserve true numeric data types while rendering context-aware currency or percentage formatting. In this scenario: Configuring a `Dynamic Format String` expression returns `"$#,0"`, `"#,0"`, or `"0.0%"` dynamically without converting numbers to strings via `FORMAT()`.
- **D:** Incorrect for this requirement. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Why the keyed choice wins: Configuring a `Dynamic Format String` expression returns `"$#,0"`, `"#,0"`, or `"0.0%"` dynamically without converting numbers to strings via `FORMAT()`.

### Question 77 — D

Answer: Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer. A `Field Parameter` (`NAMEOF(...)`) bound to the bar chart Y-axis and a slicer swaps dimensions dynamically. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Why the keyed choice wins: A `Field Parameter` (`NAMEOF(...)`) bound to the bar chart Y-axis and a slicer swaps dimensions dynamically.
- **B:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: A `Field Parameter` (`NAMEOF(...)`) bound to the bar chart Y-axis and a slicer swaps dimensions dynamically.
- **C:** Incorrect for this requirement. A single Calculation Group applies reusable logic (YTD, PY, YoY%, Moving Avg) across dozens of base measures via SELECTEDMEASURE(), eliminating measure explosion (`50 base * 6 time calcs = 300 measures`). Why the keyed choice wins: A `Field Parameter` (`NAMEOF(...)`) bound to the bar chart Y-axis and a slicer swaps dimensions dynamically.
- **D:** Correct. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. In this scenario: A `Field Parameter` (`NAMEOF(...)`) bound to the bar chart Y-axis and a slicer swaps dimensions dynamically.

### Question 78 — A

Answer: Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat). `Large semantic model storage format` allows models to utilize full capacity SKU memory limits and optimizes XMLA write operations. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Local study-map skill 3.6 (Identify Use Cases for and Configure Large Semantic Model Storage Format), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Large semantic models in Microsoft Fabric & Power BI Premium (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-large-models).

- **A:** Correct. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. In this scenario: `Large semantic model storage format` allows models to utilize full capacity SKU memory limits and optimizes XMLA write operations.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Large semantic model storage format` allows models to utilize full capacity SKU memory limits and optimizes XMLA write operations.
- **C:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Large semantic model storage format` allows models to utilize full capacity SKU memory limits and optimizes XMLA write operations.
- **D:** Incorrect for this requirement. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Why the keyed choice wins: `Large semantic model storage format` allows models to utilize full capacity SKU memory limits and optimizes XMLA write operations.

### Question 79 — A

Answer: Create exact case-sensitive DateTime parameters RangeStart and RangeEnd, filter Date >= RangeStart and Date < RangeEnd (half-open interval) with query folding intact, and enable Incremental refresh. Creating exact case-sensitive `DateTime` `RangeStart` and `RangeEnd` parameters with a foldable `>= RangeStart and < RangeEnd` filter bounds Desktop preview downloads to a small date window. Incremental refresh requires exact DateTime-typed RangeStart and RangeEnd parameters and a half-open filter (>= RangeStart and < RangeEnd, never <= on both ends which duplicates boundary midnight rows) on a foldable query. Local study-map skill 3.6 (Identify Use Cases for and Configure Large Semantic Model Storage Format), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Large semantic models in Microsoft Fabric & Power BI Premium (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-large-models).

- **A:** Correct. Incremental refresh requires exact DateTime-typed RangeStart and RangeEnd parameters and a half-open filter (>= RangeStart and < RangeEnd, never <= on both ends which duplicates boundary midnight rows) on a foldable query. In this scenario: Creating exact case-sensitive `DateTime` `RangeStart` and `RangeEnd` parameters with a foldable `>= RangeStart and < RangeEnd` filter bounds Desktop preview downloads to a small date window.
- **B:** Incorrect for this requirement. Using >= AND <= on both ends causes rows stamped exactly at midnight on partition boundaries to load into two adjacent partitions, silently double-counting sales totals. Why the keyed choice wins: Creating exact case-sensitive `DateTime` `RangeStart` and `RangeEnd` parameters with a foldable `>= RangeStart and < RangeEnd` filter bounds Desktop preview downloads to a small date window.
- **C:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Creating exact case-sensitive `DateTime` `RangeStart` and `RangeEnd` parameters with a foldable `>= RangeStart and < RangeEnd` filter bounds Desktop preview downloads to a small date window.
- **D:** Incorrect for this requirement. Direct Lake loads Delta Parquet columns directly from OneLake into VertiPaq memory on demand without scheduled Import data duplication or slow per-visual SQL translation. Why the keyed choice wins: Creating exact case-sensitive `DateTime` `RangeStart` and `RangeEnd` parameters with a foldable `>= RangeStart and < RangeEnd` filter bounds Desktop preview downloads to a small date window.

### Question 80 — B, C

Answers: Build a Direct Lake on OneLake composite semantic model combining Direct Lake fact tables from OneLake with Import dimension/target tables using regular relationships; Create a local composite model using DirectQuery for Power BI semantic models and Analysis Services to combine a certified core semantic model with a departmental Excel/SQL table. Both `Direct Lake on OneLake + Import` (regular relationships) and `DirectQuery over Power BI semantic models + local table` (remote/local composite chain) are first-class composite architectures. Local study-map skill 3.7 (Design and Build Composite Models (Direct Lake on OneLake + Import, Dual + Aggregations, DirectQuery over PBI)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use composite models in Power BI Desktop & Direct Lake on OneLake composite models (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-web-modeling).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Both `Direct Lake on OneLake + Import` (regular relationships) and `DirectQuery over Power BI semantic models + local table` (remote/local composite chain) are first-class composite architectures.
- **B:** Correct. Connecting to an existing shared semantic model in DirectQuery mode creates a local composite model (using remote model chains and limited cross-island relationships) so analysts can extend governed enterprise measures without copying the core model. In this scenario: Both `Direct Lake on OneLake + Import` (regular relationships) and `DirectQuery over Power BI semantic models + local table` (remote/local composite chain) are first-class composite architectures.
- **C:** Correct. Direct Lake on OneLake supports true composite models that mix Direct Lake tables from multiple Fabric items with Import tables from any Power Query connector while preserving fast regular (non-limited) relationships. In this scenario: Both `Direct Lake on OneLake + Import` (regular relationships) and `DirectQuery over Power BI semantic models + local table` (remote/local composite chain) are first-class composite architectures.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Both `Direct Lake on OneLake + Import` (regular relationships) and `DirectQuery over Power BI semantic models + local table` (remote/local composite chain) are first-class composite architectures.
- **E:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Both `Direct Lake on OneLake + Import` (regular relationships) and `DirectQuery over Power BI semantic models + local table` (remote/local composite chain) are first-class composite architectures.

### Question 81 — B

Answer: Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time. Power BI Desktop `Performance Analyzer` logs `DAX query`, `Visual display`, and `Other` wait times per visual, proving excessive gauge count is queuing rendering. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Local study-map skill 3.8 (Implement Performance Improvements in Queries and Report Visuals (Performance Analyzer & Query Reduction)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use Performance Analyzer to examine report element performance in Power BI (https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer).

- **A:** Incorrect for this requirement. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. Why the keyed choice wins: Power BI Desktop `Performance Analyzer` logs `DAX query`, `Visual display`, and `Other` wait times per visual, proving excessive gauge count is queuing rendering.
- **B:** Correct. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. In this scenario: Power BI Desktop `Performance Analyzer` logs `DAX query`, `Visual display`, and `Other` wait times per visual, proving excessive gauge count is queuing rendering.
- **C:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Power BI Desktop `Performance Analyzer` logs `DAX query`, `Visual display`, and `Other` wait times per visual, proving excessive gauge count is queuing rendering.
- **D:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: Power BI Desktop `Performance Analyzer` logs `DAX query`, `Visual display`, and `Other` wait times per visual, proving excessive gauge count is queuing rendering.

### Question 82 — C

Answer: Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages. Adding an `Apply` button to slicers under `Options -> Query reduction` defers query execution until the user confirms selections. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Local study-map skill 3.8 (Implement Performance Improvements in Queries and Report Visuals (Performance Analyzer & Query Reduction)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use Performance Analyzer to examine report element performance in Power BI (https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer).

- **A:** Incorrect for this requirement. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. Why the keyed choice wins: Adding an `Apply` button to slicers under `Options -> Query reduction` defers query execution until the user confirms selections.
- **B:** Incorrect for this requirement. Hundreds of tiny streaming Parquet files inflate Delta rowgroup counts past Fabric SKU guardrails and degrade transcoding; OPTIMIZE compacts files into large V-Order-sorted rowgroups optimized for VertiPaq in-memory compression. Why the keyed choice wins: Adding an `Apply` button to slicers under `Options -> Query reduction` defers query execution until the user confirms selections.
- **C:** Correct. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. In this scenario: Adding an `Apply` button to slicers under `Options -> Query reduction` defers query execution until the user confirms selections.
- **D:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Adding an `Apply` button to slicers under `Options -> Query reduction` defers query execution until the user confirms selections.

### Question 83 — D

Answer: Profile the slow measure in DAX Studio using Server Timings to inspect Formula Engine (FE) vs Storage Engine (SE) CPU, SE query count, and CallbackDataID warnings. Replace whole-table `FILTER(FactReceipts, ...)` predicates with compact dimension/fact column predicates pushed to the Storage Engine and cache repeated sub-expressions in `VAR`. DAX Studio Server Timings reveals whether slow execution comes from hundreds of chatty SE scans, CallbackDataID forcing row-by-row FE callbacks inside SE scans, or unpushed complex predicates. Local study-map skill 3.9 (Improve DAX and Model Performance Using DAX Studio Server Timings (FE vs SE) and VertiPaq Cardinality Reduction), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Optimization guide for Power BI — DAX Formula Engine vs Storage Engine & VertiPaq (https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization).

- **A:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: Replace whole-table `FILTER(FactReceipts, ...)` predicates with compact dimension/fact column predicates pushed to the Storage Engine and cache repeated sub-expressions in `VAR`.
- **B:** Incorrect for this requirement. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Why the keyed choice wins: Replace whole-table `FILTER(FactReceipts, ...)` predicates with compact dimension/fact column predicates pushed to the Storage Engine and cache repeated sub-expressions in `VAR`.
- **C:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: Replace whole-table `FILTER(FactReceipts, ...)` predicates with compact dimension/fact column predicates pushed to the Storage Engine and cache repeated sub-expressions in `VAR`.
- **D:** Correct. DAX Studio Server Timings reveals whether slow execution comes from hundreds of chatty SE scans, CallbackDataID forcing row-by-row FE callbacks inside SE scans, or unpushed complex predicates. In this scenario: Replace whole-table `FILTER(FactReceipts, ...)` predicates with compact dimension/fact column predicates pushed to the Storage Engine and cache repeated sub-expressions in `VAR`.

### Question 84 — A

Answer: Capture visual timings in Performance Analyzer → Profile captured DAX in DAX Studio with Server Timings and Query Plan → Refactor FILTER(Fact,...) into VAR-cached SE column predicates and run V-Order OPTIMIZE → Re-test with Clear Cache. Capturing visual DAX in Performance Analyzer, profiling FE/SE + fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing after `Clear Cache` confirms cold-cache gains. Correct order: isolate visual vs DAX queue time in Performance Analyzer, profile FE/SE and Direct Lake fallback in DAX Studio Server Timings, fix DAX anti-patterns + Delta Parquet layout, and benchmark cold-cache results. Local study-map skill 3.9 (Improve DAX and Model Performance Using DAX Studio Server Timings (FE vs SE) and VertiPaq Cardinality Reduction), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Optimization guide for Power BI — DAX Formula Engine vs Storage Engine & VertiPaq (https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization).

- **A:** Correct. Correct order: isolate visual vs DAX queue time in Performance Analyzer, profile FE/SE and Direct Lake fallback in DAX Studio Server Timings, fix DAX anti-patterns + Delta Parquet layout, and benchmark cold-cache results. In this scenario: Capturing visual DAX in Performance Analyzer, profiling FE/SE + fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing after `Clear Cache` confirms cold-cache gains.
- **B:** Incorrect for this requirement. Incorrect: scaling capacity blindly wastes budget while bidirectional joins, FORMAT() strings, and disabled V-Order make FE and transcoding slower. Why the keyed choice wins: Capturing visual DAX in Performance Analyzer, profiling FE/SE + fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing after `Clear Cache` confirms cold-cache gains.
- **C:** Incorrect for this requirement. Incorrect: benchmarking warm cache hides real SE/transcoding cost, GUID columns bloat dictionaries, DirectQueryOnly slows visuals, and 45 cards create visual-queue contention. Why the keyed choice wins: Capturing visual DAX in Performance Analyzer, profiling FE/SE + fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing after `Clear Cache` confirms cold-cache gains.
- **D:** Incorrect for this requirement. Incorrect: snowflaking and Auto date/time increase relationship hops and memory overhead rather than resolving FE/SE bottlenecks. Why the keyed choice wins: Capturing visual DAX in Performance Analyzer, profiling FE/SE + fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing after `Clear Cache` confirms cold-cache gains.

### Question 85 — A, D, E

Answers: Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes; Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails; Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time. Compacting Delta files with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID/string columns, and running coordinated post-ETL `framing` refreshes keep Direct Lake fast and within guardrails. Local study-map skill 3.10 (Configure Direct Lake Framing, Transcoding, V-Order/OPTIMIZE Guardrails, and DirectLakeBehavior Fallback), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: How Direct Lake works (framing, transcoding, V-Order, fallback & DirectLakeBehavior) (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works).

- **A:** Correct. Hundreds of tiny streaming Parquet files inflate Delta rowgroup counts past Fabric SKU guardrails and degrade transcoding; OPTIMIZE compacts files into large V-Order-sorted rowgroups optimized for VertiPaq in-memory compression. In this scenario: Compacting Delta files with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID/string columns, and running coordinated post-ETL `framing` refreshes keep Direct Lake fast and within guardrails.
- **B:** Incorrect for this requirement. Direct Lake on OneLake operates exclusively in DirectLakeOnly mode and never falls back to DirectQuery; exceeding capacity guardrails fails framing/queries until Delta tables or SKU sizing are optimized. Why the keyed choice wins: Compacting Delta files with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID/string columns, and running coordinated post-ETL `framing` refreshes keep Direct Lake fast and within guardrails.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Compacting Delta files with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID/string columns, and running coordinated post-ETL `framing` refreshes keep Direct Lake fast and within guardrails.
- **D:** Correct. Framing is a fast metadata-only operation updating the Direct Lake model's pointer to the latest Delta transaction log Parquet files and evicting stale resident columns so new ETL rows become visible consistently. In this scenario: Compacting Delta files with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID/string columns, and running coordinated post-ETL `framing` refreshes keep Direct Lake fast and within guardrails.
- **E:** Correct. Columnar memory in VertiPaq and Direct Lake transcoding scales primarily with column cardinality rather than row count; dropping unused GUIDs or splitting millisecond timestamps into separate Date and Time columns cuts memory dramatically. In this scenario: Compacting Delta files with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID/string columns, and running coordinated post-ETL `framing` refreshes keep Direct Lake fast and within guardrails.
- **F:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Compacting Delta files with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID/string columns, and running coordinated post-ETL `framing` refreshes keep Direct Lake fast and within guardrails.

### Question 86 — B

Answer: Migrate the model in Power BI Desktop TMDL view by replacing Sql.Database(...) in the shared Expression with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<itemId>"). Replacing `Sql.Database(...)` in the shared Expression with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<itemId>")` converts the model to Direct Lake on OneLake. Replacing the shared M expression from Sql.Database to the OneLake ABFS/HTTPS AzureStorage.DataLake URL in TMDL view upgrades an existing Direct Lake on SQL model to Direct Lake on OneLake. Local study-map skill 3.11 (Choose Between Direct Lake on OneLake and Direct Lake on SQL Analytics Endpoint (and Migrate via TMDL)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Direct Lake overview: Direct Lake on OneLake vs Direct Lake on SQL analytics endpoint (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Replacing `Sql.Database(...)` in the shared Expression with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<itemId>")` converts the model to Direct Lake on OneLake.
- **B:** Correct. Replacing the shared M expression from Sql.Database to the OneLake ABFS/HTTPS AzureStorage.DataLake URL in TMDL view upgrades an existing Direct Lake on SQL model to Direct Lake on OneLake. In this scenario: Replacing `Sql.Database(...)` in the shared Expression with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<itemId>")` converts the model to Direct Lake on OneLake.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Replacing `Sql.Database(...)` in the shared Expression with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<itemId>")` converts the model to Direct Lake on OneLake.
- **D:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: Replacing `Sql.Database(...)` in the shared Expression with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<itemId>")` converts the model to Direct Lake on OneLake.

### Question 87 — C

Answer: Live edit the model in Power BI Desktop and save a Version history point → Script the semantic model in TMDL view → Replace Sql.Database(...) with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...") → Apply TMDL and run framing refresh. Saving a Version history restore point while live editing, scripting the model in TMDL view, swapping `Sql.Database` to `AzureStorage.DataLake` OneLake URI, and running a framing refresh completes the upgrade safely. Correct order: take a version history checkpoint while live editing, script the model in TMDL view, swap the shared M expression from Sql.Database to AzureStorage.DataLake OneLake URL, apply changes, and frame. Local study-map skill 3.11 (Choose Between Direct Lake on OneLake and Direct Lake on SQL Analytics Endpoint (and Migrate via TMDL)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Direct Lake overview: Direct Lake on OneLake vs Direct Lake on SQL analytics endpoint (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview).

- **A:** Incorrect for this requirement. Incorrect: Direct Lake on OneLake does not support non-materialized SQL views, DirectQuery fallback, or gateways. Why the keyed choice wins: Saving a Version history restore point while live editing, scripting the model in TMDL view, swapping `Sql.Database` to `AzureStorage.DataLake` OneLake URI, and running a framing refresh completes the upgrade safely.
- **B:** Incorrect for this requirement. Incorrect: Direct Lake models are live-edited in workspaces (not offline Personal Workspace Import files), and OleDb breaks OneLake Direct Lake connectivity. Why the keyed choice wins: Saving a Version history restore point while live editing, scripting the model in TMDL view, swapping `Sql.Database` to `AzureStorage.DataLake` OneLake URI, and running a framing refresh completes the upgrade safely.
- **C:** Correct. Correct order: take a version history checkpoint while live editing, script the model in TMDL view, swap the shared M expression from Sql.Database to AzureStorage.DataLake OneLake URL, apply changes, and frame. In this scenario: Saving a Version history restore point while live editing, scripting the model in TMDL view, swapping `Sql.Database` to `AzureStorage.DataLake` OneLake URI, and running a framing refresh completes the upgrade safely.
- **D:** Incorrect for this requirement. Incorrect: deleting the semantic model breaks downstream thin reports and lineage, and granting Workspace Admin violates security. Why the keyed choice wins: Saving a Version history restore point while live editing, scripting the model in TMDL view, swapping `Sql.Database` to `AzureStorage.DataLake` OneLake URI, and running a framing refresh completes the upgrade safely.

### Question 88 — A

Answer: Create case-sensitive DateTime parameters RangeStart and RangeEnd → Apply foldable half-open filter (>= RangeStart and < RangeEnd) → Configure table Incremental refresh policy → Publish to workspace and run initial refresh to generate partitions. Defining exact `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the incremental policy, and publishing for initial partition creation implements it cleanly. Correct order: define DateTime RangeStart/RangeEnd parameters, apply >= RangeStart and < RangeEnd preserving query folding, configure table incremental policy, and publish so Fabric generates historical and incremental partitions. Local study-map skill 3.12 (Implement Incremental Refresh and Hybrid Real-Time Partitions (RangeStart/RangeEnd, Detect Data Changes)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Configure incremental refresh and real-time data for Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-overview).

- **A:** Correct. Correct order: define DateTime RangeStart/RangeEnd parameters, apply >= RangeStart and < RangeEnd preserving query folding, configure table incremental policy, and publish so Fabric generates historical and incremental partitions. In this scenario: Defining exact `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the incremental policy, and publishing for initial partition creation implements it cleanly.
- **B:** Incorrect for this requirement. Incorrect: importing 2 billion rows locally crashes Desktop before partitioning exists, RangeStart belongs in Power Query M, and Incremental Refresh partitions apply to Import/Hybrid tables rather than Direct Lake. Why the keyed choice wins: Defining exact `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the incremental policy, and publishing for initial partition creation implements it cleanly.
- **C:** Incorrect for this requirement. Incorrect: Detect data changes requires an audit/update timestamp column distinct from the date column used to partition RangeStart/RangeEnd. Why the keyed choice wins: Defining exact `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the incremental policy, and publishing for initial partition creation implements it cleanly.
- **D:** Incorrect for this requirement. Incorrect: parameter names/types must be exact DateTime RangeStart and RangeEnd, breaking query folding pulls the entire table on every refresh, and <= on both bounds double-counts midnight rows. Why the keyed choice wins: Defining exact `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the incremental policy, and publishing for initial partition creation implements it cleanly.

### Question 89 — A

Answer: Use the Real-Time hub to subscribe to Microsoft.Fabric.OneLake.FileCreated events (or Capacity/CDC streams) and trigger an Activator rule. `Real-Time hub` centralizes discovery of Microsoft streaming sources (including Azure IoT Hub and Event Hubs), Fabric events, and Activator alert rules. Real-Time hub unifies streaming sources, CDC feeds, Azure Blob events, and Fabric workspace/OneLake/Capacity events so analytics engineers can discover streams in one catalog and trigger event-driven pipelines or Notebooks via Activator. Local study-map skill 2.2 (Discover Data and Streams Using OneLake Catalog (Explore/Govern) and Real-Time Hub + Activator), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake catalog overview & Real-Time hub in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview).

- **A:** Correct. Real-Time hub unifies streaming sources, CDC feeds, Azure Blob events, and Fabric workspace/OneLake/Capacity events so analytics engineers can discover streams in one catalog and trigger event-driven pipelines or Notebooks via Activator. In this scenario: `Real-Time hub` centralizes discovery of Microsoft streaming sources (including Azure IoT Hub and Event Hubs), Fabric events, and Activator alert rules.
- **B:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `Real-Time hub` centralizes discovery of Microsoft streaming sources (including Azure IoT Hub and Event Hubs), Fabric events, and Activator alert rules.
- **C:** Incorrect for this requirement. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Why the keyed choice wins: `Real-Time hub` centralizes discovery of Microsoft streaming sources (including Azure IoT Hub and Event Hubs), Fabric events, and Activator alert rules.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Real-Time hub` centralizes discovery of Microsoft streaming sources (including Azure IoT Hub and Event Hubs), Fabric events, and Activator alert rules.

### Question 90 — A

Answer: Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view. `New visual query` (Visual query editor) in the Warehouse builds diagram-based joins and filters and saves them directly via `Save as view`. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Local study-map skill 2.15 (Select, Filter, and Aggregate Data Using the Visual Query Editor and Save as SQL Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query using the Visual query editor in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/visual-query-editor).

- **A:** Correct. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. In this scenario: `New visual query` (Visual query editor) in the Warehouse builds diagram-based joins and filters and saves them directly via `Save as view`.
- **B:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: `New visual query` (Visual query editor) in the Warehouse builds diagram-based joins and filters and saves them directly via `Save as view`.
- **C:** Incorrect for this requirement. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. Why the keyed choice wins: `New visual query` (Visual query editor) in the Warehouse builds diagram-based joins and filters and saves them directly via `Save as view`.
- **D:** Incorrect for this requirement. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Why the keyed choice wins: `New visual query` (Visual query editor) in the Warehouse builds diagram-based joins and filters and saves them directly via `Save as view`.

### Question 91 — C

Answer: Convert dirty string columns using TRY_CAST / TRY_CONVERT in T-SQL (or Spark try_cast) so malformed rows evaluate to NULL for quarantine instead of aborting the batch. `TRY_CAST` / `TRY_CONVERT` (or Spark `try_cast`) evaluates malformed tokens to `NULL` rather than throwing a fatal batch conversion error. Standard CAST throws a fatal conversion error on the first malformed token; TRY_CAST safely yields NULL so pipelines can quarantine invalid records without failing the entire load. Local study-map skill 2.13 (Convert Column Data Types Safely (TRY_CAST, Fixed Decimal, and Direct Lake Supported Primitive Types)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data types in Fabric Data Warehouse and Direct Lake Delta tables (https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types).

- **A:** Incorrect for this requirement. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. Why the keyed choice wins: `TRY_CAST` / `TRY_CONVERT` (or Spark `try_cast`) evaluates malformed tokens to `NULL` rather than throwing a fatal batch conversion error.
- **B:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: `TRY_CAST` / `TRY_CONVERT` (or Spark `try_cast`) evaluates malformed tokens to `NULL` rather than throwing a fatal batch conversion error.
- **C:** Correct. Standard CAST throws a fatal conversion error on the first malformed token; TRY_CAST safely yields NULL so pipelines can quarantine invalid records without failing the entire load. In this scenario: `TRY_CAST` / `TRY_CONVERT` (or Spark `try_cast`) evaluates malformed tokens to `NULL` rather than throwing a fatal batch conversion error.
- **D:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `TRY_CAST` / `TRY_CONVERT` (or Spark `try_cast`) evaluates malformed tokens to `NULL` rather than throwing a fatal batch conversion error.

### Question 92 — D

Answer: Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table. Configuring a user-defined `Import` aggregation table (`Manage aggregations`) satisfies grouped queries from VertiPaq RAM and sends only atomic serial-number drills to DirectQuery. User-defined Import aggregations satisfy high-level grouped queries purely from in-memory VertiPaq cache and automatically route only unaggregated detail drill-throughs to the underlying DirectQuery source. Local study-map skill 3.7 (Design and Build Composite Models (Direct Lake on OneLake + Import, Dual + Aggregations, DirectQuery over PBI)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use composite models in Power BI Desktop & Direct Lake on OneLake composite models (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-web-modeling).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Configuring a user-defined `Import` aggregation table (`Manage aggregations`) satisfies grouped queries from VertiPaq RAM and sends only atomic serial-number drills to DirectQuery.
- **B:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: Configuring a user-defined `Import` aggregation table (`Manage aggregations`) satisfies grouped queries from VertiPaq RAM and sends only atomic serial-number drills to DirectQuery.
- **C:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Configuring a user-defined `Import` aggregation table (`Manage aggregations`) satisfies grouped queries from VertiPaq RAM and sends only atomic serial-number drills to DirectQuery.
- **D:** Correct. User-defined Import aggregations satisfy high-level grouped queries purely from in-memory VertiPaq cache and automatically route only unaggregated detail drill-throughs to the underlying DirectQuery source. In this scenario: Configuring a user-defined `Import` aggregation table (`Manage aggregations`) satisfies grouped queries from VertiPaq RAM and sends only atomic serial-number drills to DirectQuery.

### Question 93 — B

Answer: Configure shared dimension tables in Dual storage mode inside a composite model. `Dual` storage mode allows shared dimensions to operate in memory for aggregation hits and push native SQL joins down for DirectQuery detail hits. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Local study-map skill 3.1 (Choose a Semantic Model Storage Mode (Import, DirectQuery, Direct Lake, and Dual)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model storage modes in the Power BI service & Microsoft Fabric (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode).

- **A:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Dual` storage mode allows shared dimensions to operate in memory for aggregation hits and push native SQL joins down for DirectQuery detail hits.
- **B:** Correct. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. In this scenario: `Dual` storage mode allows shared dimensions to operate in memory for aggregation hits and push native SQL joins down for DirectQuery detail hits.
- **C:** Incorrect for this requirement. Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery. Why the keyed choice wins: `Dual` storage mode allows shared dimensions to operate in memory for aggregation hits and push native SQL joins down for DirectQuery detail hits.
- **D:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Dual` storage mode allows shared dimensions to operate in memory for aggregation hits and push native SQL joins down for DirectQuery detail hits.

### Question 94 — D

Answer: Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension. Denormalizing `SubAssembly`, `AssemblyFamily`, and `ProductLine` columns directly onto `Gold.DimProduct` flattens the 4-level snowflake into a single star dimension. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Local study-map skill 2.9 (Denormalize Snowflake Hierarchies into Flattened Gold Dimension Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Dimensional modeling & denormalizing snowflake tables in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables).

- **A:** Incorrect for this requirement. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Why the keyed choice wins: Denormalizing `SubAssembly`, `AssemblyFamily`, and `ProductLine` columns directly onto `Gold.DimProduct` flattens the 4-level snowflake into a single star dimension.
- **B:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Denormalizing `SubAssembly`, `AssemblyFamily`, and `ProductLine` columns directly onto `Gold.DimProduct` flattens the 4-level snowflake into a single star dimension.
- **C:** Incorrect for this requirement. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. Why the keyed choice wins: Denormalizing `SubAssembly`, `AssemblyFamily`, and `ProductLine` columns directly onto `Gold.DimProduct` flattens the 4-level snowflake into a single star dimension.
- **D:** Correct. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. In this scenario: Denormalizing `SubAssembly`, `AssemblyFamily`, and `ProductLine` columns directly onto `Gold.DimProduct` flattens the 4-level snowflake into a single star dimension.

### Question 95 — A

Answer: Publish a single certified core semantic model in a data workspace and build thin live-connected Power BI reports in departmental workspaces. Granting `Build` permission on the Certified semantic model lets regional teams publish thin live-connected reports in their own workspaces backed by one shared model. Decoupling a shared golden semantic model from thin live-connected reports prevents measure duplication, reduces capacity memory footprint, and enforces centralized RLS/endorsement across teams. Local study-map skill 1.11 (Create and Update Reusable Assets (.pbit Templates, .pbids Data Sources, and Shared Golden Semantic Models)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create and use report templates (.pbit), data sources (.pbids), and shared semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-templates).

- **A:** Correct. Decoupling a shared golden semantic model from thin live-connected reports prevents measure duplication, reduces capacity memory footprint, and enforces centralized RLS/endorsement across teams. In this scenario: Granting `Build` permission on the Certified semantic model lets regional teams publish thin live-connected reports in their own workspaces backed by one shared model.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Granting `Build` permission on the Certified semantic model lets regional teams publish thin live-connected reports in their own workspaces backed by one shared model.
- **C:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Granting `Build` permission on the Certified semantic model lets regional teams publish thin live-connected reports in their own workspaces backed by one shared model.
- **D:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: Granting `Build` permission on the Certified semantic model lets regional teams publish thin live-connected reports in their own workspaces backed by one shared model.

### Question 96 — A

Answer: Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL. Configuring Object-Level Security (`OLS = None`) via Tabular Editor or TMDL hides restricted columns and dependent measures completely from metadata discovery. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Correct. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. In this scenario: Configuring Object-Level Security (`OLS = None`) via Tabular Editor or TMDL hides restricted columns and dependent measures completely from metadata discovery.
- **B:** Incorrect for this requirement. Dynamic Data Masking obfuscates sensitive strings/emails/numbers in query results for users lacking UNMASK permission while keeping the column present so SELECT * queries do not fail. Why the keyed choice wins: Configuring Object-Level Security (`OLS = None`) via Tabular Editor or TMDL hides restricted columns and dependent measures completely from metadata discovery.
- **C:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Configuring Object-Level Security (`OLS = None`) via Tabular Editor or TMDL hides restricted columns and dependent measures completely from metadata discovery.
- **D:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Configuring Object-Level Security (`OLS = None`) via Tabular Editor or TMDL hides restricted columns and dependent measures completely from metadata discovery.

### Question 97 — A

Answer: Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows. A Power BI Template (`.pbit`) packages report pages, DAX measures, schema, and parameter prompts without embedding any imported rows. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Local study-map skill 1.11 (Create and Update Reusable Assets (.pbit Templates, .pbids Data Sources, and Shared Golden Semantic Models)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create and use report templates (.pbit), data sources (.pbids), and shared semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-templates).

- **A:** Correct. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. In this scenario: A Power BI Template (`.pbit`) packages report pages, DAX measures, schema, and parameter prompts without embedding any imported rows.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: A Power BI Template (`.pbit`) packages report pages, DAX measures, schema, and parameter prompts without embedding any imported rows.
- **C:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: A Power BI Template (`.pbit`) packages report pages, DAX measures, schema, and parameter prompts without embedding any imported rows.
- **D:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: A Power BI Template (`.pbit`) packages report pages, DAX measures, schema, and parameter prompts without embedding any imported rows.

### Question 98 — D

Answer: Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching. External OneLake shortcuts mount ADLS Gen2 and Amazon S3 folders/Delta tables virtually inside the Lakehouse namespace with optional shortcut caching. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. Why the keyed choice wins: External OneLake shortcuts mount ADLS Gen2 and Amazon S3 folders/Delta tables virtually inside the Lakehouse namespace with optional shortcut caching.
- **B:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: External OneLake shortcuts mount ADLS Gen2 and Amazon S3 folders/Delta tables virtually inside the Lakehouse namespace with optional shortcut caching.
- **C:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: External OneLake shortcuts mount ADLS Gen2 and Amazon S3 folders/Delta tables virtually inside the Lakehouse namespace with optional shortcut caching.
- **D:** Correct. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. In this scenario: External OneLake shortcuts mount ADLS Gen2 and Amazon S3 folders/Delta tables virtually inside the Lakehouse namespace with optional shortcut caching.

### Question 99 — B

Answer: OPTIMIZE gold.fact_orders VORDER. `OPTIMIZE gold.fact_orders VORDER` compacts thousands of tiny files into large rowgroups sorted with V-Order for fast Direct Lake transcoding. Running OPTIMIZE ... VORDER bin-packs small Delta Parquet files into large rowgroups and applies V-Order columnar sorting for peak Direct Lake compression and transcoding. Local study-map skill 3.10 (Configure Direct Lake Framing, Transcoding, V-Order/OPTIMIZE Guardrails, and DirectLakeBehavior Fallback), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: How Direct Lake works (framing, transcoding, V-Order, fallback & DirectLakeBehavior) (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works).

- **A:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `OPTIMIZE gold.fact_orders VORDER` compacts thousands of tiny files into large rowgroups sorted with V-Order for fast Direct Lake transcoding.
- **B:** Correct. Running OPTIMIZE ... VORDER bin-packs small Delta Parquet files into large rowgroups and applies V-Order columnar sorting for peak Direct Lake compression and transcoding. In this scenario: `OPTIMIZE gold.fact_orders VORDER` compacts thousands of tiny files into large rowgroups sorted with V-Order for fast Direct Lake transcoding.
- **C:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: `OPTIMIZE gold.fact_orders VORDER` compacts thousands of tiny files into large rowgroups sorted with V-Order for fast Direct Lake transcoding.
- **D:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `OPTIMIZE gold.fact_orders VORDER` compacts thousands of tiny files into large rowgroups sorted with V-Order for fast Direct Lake transcoding.

### Question 100 — A

Answer: Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs. Vectorized `pyspark.sql.functions` inside `.withColumn()` execute natively in Spark's Catalyst/Photon engine without JVM-to-Python row serialization overhead. Native Catalyst/Photon-optimized pyspark.sql.functions execute in vectorized JVM/native code across partitions, avoiding the severe Python serialization bottleneck of row-level UDFs. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Correct. Native Catalyst/Photon-optimized pyspark.sql.functions execute in vectorized JVM/native code across partitions, avoiding the severe Python serialization bottleneck of row-level UDFs. In this scenario: Vectorized `pyspark.sql.functions` inside `.withColumn()` execute natively in Spark's Catalyst/Photon engine without JVM-to-Python row serialization overhead.
- **B:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Vectorized `pyspark.sql.functions` inside `.withColumn()` execute natively in Spark's Catalyst/Photon engine without JVM-to-Python row serialization overhead.
- **C:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Vectorized `pyspark.sql.functions` inside `.withColumn()` execute natively in Spark's Catalyst/Photon engine without JVM-to-Python row serialization overhead.
- **D:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Vectorized `pyspark.sql.functions` inside `.withColumn()` execute natively in Spark's Catalyst/Photon engine without JVM-to-Python row serialization overhead.
