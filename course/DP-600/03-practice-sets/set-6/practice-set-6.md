# Microsoft Exam DP-600: Implementing Analytics Solutions Using Microsoft Fabric — Full-Length Mock Exam 6

Exam DP-600 (Renewable Energy Grids, Telecom Network Analytics, and Public-Sector Open Data) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint & Credential Notice:** Aligned to the official **October 19, 2026** DP-600 study guide (`Microsoft Certified: Fabric Analytics Engineer Associate`). Associate-level certification with **no prerequisite exam required**, free online annual renewal on Microsoft Learn, split-screen `learn.microsoft.com` access during non-lab exam sections, and hands-on coverage across **SQL**, **KQL**, **DAX**, **PySpark**, **Power Query M**, **TMDL**, and **TMSL**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` SQL/KQL/DAX/PySpark/M/TMDL/TMSL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Microsoft Fabric case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area SQL/KQL/DAX/TMDL dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn Fabric and Power BI documentation — never recalled live items or copied Microsoft sample case studies.

## Questions

### 1. A wind-farm telemetry engineer needs to build Lakehouses, Spark jobs, and Eventhouses in `GridAnalytics-Dev` without sharing items externally or modifying workspace role memberships. Which workspace role enforces least privilege?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Admin role
- B. Assign the Workspace Contributor role
- C. Assign the Workspace Viewer role
- D. Assign the Workspace Member role

### 2. Municipal water-district superintendents access reports in `Utilities-Prod` workspace and must be restricted to their own district via OneLake security and DAX RLS. Which workspace role must they be assigned?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Member role
- B. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows
- C. Assign the Workspace Viewer role
- D. Assign the Workspace Contributor role

### 3. Telecom BI release leads must update the organizational Power BI App, configure OneLake security roles, and onboard Contributors via Entra groups without being able to delete `Telco-Prod`. Which two options apply? Select two.

Domain: Maintain a data analytics solution

- A. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows
- B. Assign the Workspace Member role
- C. Assign the Workspace Viewer role
- D. Assign the Workspace Admin role
- E. Assign permissions to Microsoft Entra security groups rather than individual users

### 4. Network capacity planners in `RAN-Planning` workspace want to build live thin Power BI reports and Excel PivotTables on top of the Certified `5GTowerTraffic` semantic model. Which item permission on `5GTowerTraffic` is required?

Domain: Maintain a data analytics solution

- A. Share the Lakehouse with ReadAll (Read all Apache Spark data) permission
- B. Share the item with Read permission only (no ReadData or ReadAll)
- C. Assign the Workspace Admin role
- D. Grant Build permission on the shared semantic model

### 5. Which four-step sequence enforces OneLake security roles across a central `SmartMeterLakehouse` and three regional utility workspaces consuming it via OneLake shortcuts?

Domain: Maintain a data analytics solution

- A. Enable OneLake security and define Read Grant roles → Assign consumers Workspace Viewer and OneLake security roles → Set SQL analytics endpoint to User's identity mode → Expose downstream shortcuts in User's identity mode
- B. Assign consumers the Workspace Contributor role → Enable OneLake security with a Deny role → Keep SQL analytics endpoint in Owner fixed identity mode → Create downstream shortcuts
- C. Create downstream shortcuts first → Assign consumers Workspace Member rights → Attach RLS predicates to a ReadWrite OneLake role → Enable SSO on an On-premises gateway
- D. Set SQL analytics endpoint to Delegated mode with SQL DENY rules → Remove Workspace Viewer assignments → Enable OneLake security afterward → Export binary .pbix copies

### 6. On `SubstationLakehouse`, field contractors need (1) `Read` access exclusively to `Files/drone_lidar/region4/` without seeing `Files/nerc_cip_audits/`, and (2) both row filtering (`Region = 4`) and column hiding (`CustomerAccountSSN`) on `Tables/Outages`. Which two OneLake security rules work? Select two.

Domain: Maintain a data analytics solution

- A. Define both the RLS filter and CLS column allow-list inside a single OneLake security Grant role with Read permission
- B. Create two separate OneLake security roles on the same table — Role A containing the RLS filter and Role B containing the CLS column rule — and assign the user to both
- C. Create a OneLake security role scoped to the specific Files/<subfolder> path with Read permission
- D. Create a Deny role in OneLake security to revoke table access granted by another OneLake role or Workspace Member role
- E. Create a OneLake security role with ReadWrite permission and attach an RLS predicate

### 7. Critical-infrastructure tables in `GridSecurityWarehouse` carry a `Confidential — NERC CIP` Microsoft Purview sensitivity label. Which Fabric capability ensures new downstream semantic models and reports inherit that label automatically?

Domain: Maintain a data analytics solution

- A. Mark the item as Promoted in item settings
- B. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- C. Apply a Microsoft Purview sensitivity label with downstream inheritance on the source Lakehouse or Warehouse
- D. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository

### 8. Telecom regulators export subscriber complaint summaries to `.xlsx` and `.pdf`. Which sensitivity-label capability enforces Microsoft Entra rights checks even after those files leave the Fabric workspace?

Domain: Maintain a data analytics solution

- A. Use a Purview sensitivity label configured with file encryption so exported .pbix, Excel, PDF, and PowerPoint files stay protected outside Fabric
- B. Apply T-SQL Dynamic Data Masking (MASKED WITH (FUNCTION = 'partial(...)')) on sensitive columns
- C. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal
- D. Share the item with Read permission only (no ReadData or ReadAll)

### 9. Public-sector open-data stewards must formally badge datasets that passed statutory accuracy and privacy reviews, restricting who can apply that badge via the Fabric Admin portal. Which endorsement state applies?

Domain: Maintain a data analytics solution

- A. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal
- B. Mark the item as Promoted in item settings
- C. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- D. Assign the Workspace Contributor role

### 10. An RF engineer builds a helpful `CellSiteInterference` dashboard and wants to mark it as ready for broader engineering use without waiting for central governance certification. Which endorsement state can the engineer set directly?

Domain: Maintain a data analytics solution

- A. Configure Certified endorsement with the Master data label on authoritative core tables or semantic models
- B. Mark the item as Promoted in item settings
- C. Enable a mandatory label policy and default sensitivity label in Microsoft Purview compliance portal for Fabric users
- D. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal

### 11. Six telecom analytics engineers collaborate on `NetworkBI-Dev` linked to `main` in GitHub. How should an engineer develop a complex new churn `.pbip` calculation group without disrupting colleagues' workspace items?

Domain: Maintain a data analytics solution

- A. Use Undo in the Fabric Workspace Source control pane to discard uncommitted workspace edits back to the last synced commit
- B. Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch
- C. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- D. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline

### 12. Which four-step Git and Deployment Pipeline sequence cleanly promotes a `.pbip` grid-reliability update from an isolated developer workspace to `Grid-Prod`?

Domain: Maintain a data analytics solution

- A. Connect Production directly to a feature branch → Edit semantic models live in Prod → Force-push binary .pbix files including cache.abf to main → Deploy backward to Development
- B. Edit items directly on main without branching → Merge an empty PR → Promote Dev to Test before running Update from Git → Configure Git integration last
- C. Connect shared Dev workspace to main → Branch out to an isolated developer workspace and commit .pbip/Notebook edits → Merge pull request into main in Git → Run Update all in Dev and promote via Deployment Pipeline
- D. Branch out to personal My Workspace → Run Undo to push changes to GitHub → Delete .platform metadata files → Copy visuals manually into Production

### 13. Proposed solution: A public-transit BI team checks monolithic `.pbix` binaries into Azure Repos and struggles with unreadable merge conflicts whenever two developers edit measures on the same day. Switching to which format resolves this?

Domain: Maintain a data analytics solution

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- C. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode

### 14. Which two repository conventions are mandatory when storing a `.pbip` telecom semantic model in GitHub so measure changes diff cleanly and cached subscriber data (`**/____`) never leaks? Select two.

Domain: Maintain a data analytics solution

- A. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- B. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- C. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- D. Configure DirectQuery storage mode
- E. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches

### 15. In a `Dev -> Test -> Prod` Deployment Pipeline, how do you ensure `OutageModel` (`Direct Lake on SQL`) automatically binds to `ProdOutageWarehouse` every time changes deploy from `Test` to `Production`?

Domain: Maintain a data analytics solution

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Configure Deployment pipeline data source and parameter rules on the Test and Production stages

### 16. Only `SolarForecastReport` and its upstream `SolarSemanticModel` are approved for release from `Energy-Dev` to `Energy-Test`, while four experimental notebooks must remain in `Energy-Dev`. Which action deploys both cleanly?

Domain: Maintain a data analytics solution

- A. Use Undo in the Fabric Workspace Source control pane to discard uncommitted workspace edits back to the last synced commit
- B. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline
- C. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition
- D. Perform a selective deployment selecting the modified item together with Select related to include required upstream dependencies

### 17. You deploy Data Factory pipelines and `Direct Lake on OneLake` artifacts across `Dev`, `Test`, and `Prod` workspaces requiring stage-specific Lakehouse IDs and ADLS URIs. Which Fabric CI/CD item centralizes those values?

Domain: Maintain a data analytics solution

- A. Configure Deployment pipeline data source and parameter rules on the Test and Production stages
- B. Use a Fabric Variable library (or autobinding across paired workspace items) to parameterize stage-specific environment references
- C. Mark the item as Promoted in item settings
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode

### 18. Before decommissioning `LegacyBillingWarehouse`, how do you discover all dependent semantic models and reports across 11 municipal workspaces and send an automated notification to their owners?

Domain: Maintain a data analytics solution

- A. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- B. Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View
- C. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- D. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view

### 19. Proposed solution: To find out which external workspaces rely on `GridWeatherDataflow`, an engineer inspects only the Dataflow's Power Query M script. Does the M script reveal downstream consumers, and what should they open instead?

Domain: Maintain a data analytics solution

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- C. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- D. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts

### 20. During a severe winter storm, you must deploy two outage-duration DAX measures from `Grid-Dev` to a 38 GB partitioned `Grid-Prod` model without reprocessing 8 years of smart-meter partitions. Which four-step XMLA workflow works?

Domain: Maintain a data analytics solution

- A. Set XMLA Endpoint = Off → Overwrite Production with an empty unpartitioned .pbix file → Purge all 5 years of historical incremental partitions → Re-import 3 billion rows during peak business hours
- B. Leave XMLA Endpoint = Read Only → Execute T-SQL DELETE across Warehouse schemas → Grant all report viewers Capacity Admin rights → Skip downstream impact analysis
- C. Verify XMLA Endpoint = Read Write on target capacity → Connect ALM Toolkit to Dev source and Prod XMLA target → Compare schemas while hiding unchanged partitions and keeping Prod data sources → Validate and deploy metadata-only TMSL changes
- D. Open Production in DAX Studio → Edit measures manually in Production without committing to Git → Copy cache.abf into GitHub → Disable sensitivity labels

### 21. Every hour, telecom mediation updates only partition `2026M10` of `FactPositions` / `FactCDR` and triggers TMSL payload `____` against `powerbi://api.powerbi.com/v1.0/myorg/Telco-Prod`. Which two items are required? Select two.

Domain: Maintain a data analytics solution

- A. Assign the Workspace Viewer role
- B. {"refresh": {"type": "dataOnly", "objects": [{"database": "WealthModel", "table": "FactPositions", "partition": "2026M10"}]}}
- C. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- E. Enable XMLA Endpoint = Read Write in Fabric Capacity workload settings and connect to powerbi://api.powerbi.com/v1.0/myorg/<WorkspaceName>

### 22. Eight municipal transit agencies want tailored report visuals over a single Certified `RegionalTransit` semantic model without duplicating 20 GB of VertiPaq RAM eight times. Which reporting pattern should they adopt?

Domain: Maintain a data analytics solution

- A. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- B. Configure Import storage mode
- C. Publish a single certified core semantic model in a data workspace and build thin live-connected Power BI reports in departmental workspaces
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 23. Rural electric cooperatives need a downloadable starter report containing standardized NERC reliability visuals, DAX measures, and a `@CoopUtilityId` parameter prompt with zero utility data embedded. Which file format should you export?

Domain: Maintain a data analytics solution

- A. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 24. Substation SCADA historians run on on-premises OSIsoft/SQL servers inside regional control centers without Azure VNet peering. Which gateway setup provides resilient scheduled ingestion into Fabric?

Domain: Prepare data

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet
- C. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- D. Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication

### 25. Telecom subscriber CRM runs on Azure SQL Managed Instance locked inside a private subnet (`vnet-telco-prod`) with no public endpoint. Which managed Fabric gateway connects pipelines and Dataflows without Windows gateway VMs?

Domain: Prepare data

- A. Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet
- B. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- C. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- D. Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication

### 26. A Chief Data Steward wants to audit endorsement coverage and missing sensitivity labels across all energy-domain workspaces from one Fabric portal screen. Where should they go?

Domain: Prepare data

- A. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- B. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results

### 27. Grid operations wants to (1) discover all substation IoT Hub streams and `Microsoft.Fabric.OneLake.FileCreated` weather-forecast arrival events in one hub with Activator alerts, and (2) route live SCADA telemetry into Eventhouse. Which two capabilities work together? Select two.

Domain: Prepare data

- A. Use the Real-Time hub to subscribe to Microsoft.Fabric.OneLake.FileCreated events (or Capacity/CDC streams) and trigger an Activator rule
- B. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- C. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- D. Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table
- E. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 28. National weather agencies publish 120 TB of radar NetCDF/Parquet forecasts in Amazon S3 and Google Cloud Storage. How can `GridForecastLakehouse` read those Parquet datasets virtually without copying storage?

Domain: Prepare data

- A. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- B. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- C. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging

### 29. Proposed solution: To sync 140 customer outage-ticket tables from Azure Cosmos DB into OneLake every minute, an engineer schedules 140 full-reload Copy pipelines. Which zero-ETL Fabric feature replaces those pipelines?

Domain: Prepare data

- A. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- B. Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog
- C. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 30. Every night, 5G core switches dump 6 TB of compressed binary/Parquet CDR archives onto an SFTP/ADLS landing zone that must land raw in `BronzeLakehouse/Files/cdr/` at minimum CU cost. Which tool fits best?

Domain: Prepare data

- A. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- B. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- C. Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table
- D. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations

### 31. Match the three public-utility data patterns: (1) visual Power Query M transformations merging 30 Dataverse/SharePoint permit lists with Fast Copy staging, (2) zero-ETL replication from Snowflake billing tables, and (3) zero-copy access to ADLS Gen2 GIS Parquet files. Select three.

Domain: Prepare data

- A. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- D. Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog
- E. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching
- F. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging

### 32. 5G base stations emit 3 million syslog and radio-signal JSON events per second queried over 30-second sliding windows and geospatial cells in KQL. Which Fabric store is built for this?

Domain: Prepare data

- A. Choose a Fabric Lakehouse
- B. Choose a Fabric Data Warehouse
- C. Choose a SQL database in Microsoft Fabric
- D. Choose a Fabric Eventhouse (KQL database)

### 33. Utility rate-case accountants require multi-table T-SQL ACID transactions (`BEGIN TRAN ... UPDATE ... INSERT ... COMMIT`), cross-database T-SQL queries, and native SQL Dynamic Data Masking. Which store should you choose?

Domain: Prepare data

- A. Configure Import storage mode
- B. Choose a Fabric Data Warehouse
- C. Choose a Fabric Lakehouse
- D. Choose a Fabric Eventhouse (KQL database)

### 34. A smart-city department needs (1) an operational OLTP database inside Fabric for citizen 311 service-request web submissions, and (2) a Spark data-science store holding street-camera `.mp4`/`.jpg` files in `Files/` plus Silver Delta tables. Which two stores fit? Select two.

Domain: Prepare data

- A. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- B. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Choose a Fabric Lakehouse
- E. Choose a SQL database in Microsoft Fabric

### 35. A legacy telecom regulatory team maintains curated rate tables inside an `Import` semantic model. How can data engineers expose those imported model tables as Delta Parquet folders in OneLake for Lakehouse shortcuts?

Domain: Prepare data

- A. Point Direct Lake on SQL directly at an Eventhouse KQL database without enabling OneLake availability
- B. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- C. Enable OneLake integration in the Import semantic model settings so imported model tables export as Delta tables to OneLake
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode

### 36. In which four-step order do you integrate wind-turbine Eventhouse KQL telemetry with Lakehouse maintenance tables inside a `Direct Lake on OneLake` semantic model?

Domain: Prepare data

- A. Export KQL query results manually to CSV every hour → Email CSVs to analysts → Import into binary .pbix files → Publish to My Workspace
- B. Create a Direct Lake on SQL model directly over the KQL queryset → Disable OneLake availability → Configure an On-premises data gateway → Run T-SQL MERGE on the KQL database
- C. Create an Amazon S3 external shortcut to the KQL URI before enabling OneLake availability → Set storage mode to Dual only → Enable Auto date/time → Run XMLA clearValues
- D. Ingest streaming telemetry into an Eventhouse KQL database → Enable OneLake availability on the KQL database or table → Create an internal OneLake shortcut in the Lakehouse → Add the table to a Direct Lake on OneLake semantic model

### 37. You want a pre-joined `Gold.TowerOutageSummary` asset in `NetworkLakehouse` to feed a `Direct Lake on OneLake` model without falling back or failing validation. Why should you create a Gold Delta table or `Materialized Lake View` rather than a plain SQL endpoint `VIEW`?

Domain: Prepare data

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- C. Use a Lakehouse Materialized Lake View (or persisted Gold Delta table) instead of a non-materialized SQL analytics endpoint view for Direct Lake on OneLake
- D. Configure DirectQuery storage mode

### 38. In `TransitWarehouse`, open-data analysts are granted `SELECT` on `public_views.vw_RidershipAnon` while explicitly blocked from `raw.FareCardTaps` (`____ SELECT ON OBJECT::raw.FareCardTaps`). Which SQL mechanism enforces this?

Domain: Prepare data

- A. Mark the item as Promoted in item settings
- B. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- C. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- D. Use T-SQL GRANT/DENY SELECT on specific Warehouse schemas, tables, or views

### 39. Regional telecom acquisitions use incompatible natural tower IDs (`"NE-BOS-019"`, `99019`, `"TX_019"`). Why should `Gold.DimCellTower` generate a 4-byte `INT` `TowerKey` surrogate key?

Domain: Prepare data

- A. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- B. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- C. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- D. Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions

### 40. Energy market settlement requires peak/off-peak tariff flags, NERC holiday indicators, and Daylight Saving Time transition markers across `FactGeneration` and `FactLoad`. How should you enrich the Gold schema?

Domain: Prepare data

- A. Configure DirectQuery storage mode
- B. Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'

### 41. A Silver PySpark job normalizes 1.5 billion telecom IMEI strings (`df.____("TAC8", F.substring("IMEI", 1, 8))`) and joins integer `DeviceModelKey` surrogates instead of running a Python `@udf`. Which two engineering best practices apply? Select two.

Domain: Prepare data

- A. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- B. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- C. Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions
- D. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- E. Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs

### 42. When a cell tower upgrades from `4G LTE` to `5G Standalone` on August 10, dropped-call rates in June must still roll up under `4G LTE` while September calls roll up under `5G Standalone`. Which SCD pattern on `DimCellTower` is required?

Domain: Prepare data

- A. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)
- B. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place
- C. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- D. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns

### 43. Joining `WorkOrderHeader` (`DispatchTruckCost`) directly onto `WorkOrderReplacedParts` (`PartCost`) repeats `DispatchTruckCost` across 7 replaced parts, inflating dispatch expenses 7x. Which star-schema rule fixes this?

Domain: Prepare data

- A. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- B. Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures
- C. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- D. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place

### 44. Which four-step ELT sequence maintains `DimRateTariff` as an SCD Type 2 dimension when public utility commissions approve seasonal rate-class revisions?

Domain: Prepare data

- A. Stage and deduplicate incoming records by natural key → Compare tracked attributes against active (IsCurrent = 1) Gold rows → Expire changed active rows (EffectiveEndDate, IsCurrent = 0) → Insert new active versions with fresh surrogate keys
- B. Truncate the Gold dimension table → Reassign fresh random surrogate keys to all historical rows → Join historical facts without updating foreign keys → Set IsCurrent = 1 on every version
- C. Insert new versions with IsCurrent = 0 first → Overwrite old EffectiveStartDate values in place → Remove the natural business key column → Deduplicate after publishing reports
- D. Insert raw duplicate staging rows directly into FactSales → Delete unmatched dimension keys → Leave EffectiveStartDate NULL → Enable Assume referential integrity on broken keys

### 45. Select the three dimensional patterns that match: (1) Bronze/Silver/Gold lakehouse layering, (2) correcting a misspelled `SubstationName` across all historical reports without splitting history, and (3) preserving CDR facts from newly activated towers not yet in `DimCellTower`. Select three.

Domain: Prepare data

- A. Organize OneLake into Bronze (raw immutable), Silver (validated, deduplicated, conformed), and Gold (star-schema dimensions and facts with V-Order)
- B. Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE
- C. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- E. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- F. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table

### 46. In the GIS asset system, `Transformer -> FeederCircuit -> Substation -> TransmissionZone` is normalized across four tables. How should you structure `Gold.DimTransformer` for Direct Lake?

Domain: Prepare data

- A. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- B. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- C. Choose a Fabric Eventhouse (KQL database)
- D. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()

### 47. Proposed solution: A telecom modeler imports `HandsetModel -> Manufacturer -> CountryHQ` as three separate snowflaked tables in Direct Lake and turns on bidirectional relationships so `CountryHQ` filters `FactCDR`. What cleaner Gold transformation avoids chained relationships?

Domain: Prepare data

- A. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition
- B. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns
- C. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- D. Configure DirectQuery storage mode

### 48. Smart meters emit 18 billion 15-minute kWh intervals per year, while municipal regulatory dashboards display monthly kWh and peak kW by `ZipCode` and `RateClass`. How do you cut Direct Lake memory usage dramatically?

Domain: Prepare data

- A. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- B. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- C. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- D. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)

### 49. In Dataflow Gen2 summarizing 200 million transit tap rows by `StationId` and `ServiceDate` from an Azure SQL source, why is preserving query folding up through `Group by` critical?

Domain: Prepare data

- A. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- B. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled

### 50. Complete `MERGE INTO gold.FactOutages t USING silver.StgOutages s ON t.OutageId = s.OutageId ____ t.RestoredUTC = s.RestoredUTC WHEN NOT MATCHED THEN INSERT *;` so unchanged open outages do not rewrite Delta Parquet files?

Domain: Prepare data

- A. ADD BLOCK PREDICATE dbo.sp_checkregion(RegionCode) AFTER INSERT
- B. RANK() OVER (ORDER BY SpecimenId DESC)
- C. WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET
- D. CAST(RawReading AS FLOAT)

### 51. Field maintenance wants a daily report of registered `DimSmartMeter` devices that transmitted **zero** interval readings in `FactMeterReads` over the last 24 hours ("silent meters"). Which join kind isolates silent meters?

Domain: Prepare data

- A. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- B. Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement
- C. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- D. Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table

### 52. A Spark job joins 2.2 billion 5G call-detail records with a 6 MB `dim_cell_sector` lookup (`cdr_df.join(____)`) and upserts dropped-call KPIs into `gold.fact_sector_hourly`. Which two patterns avoid cluster shuffles and maintain ACID writes? Select two.

Domain: Prepare data

- A. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- B. fact_df.join(F.broadcast(dim_store_df), on="StoreKey", how="left")
- C. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- D. Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement
- E. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations

### 53. Cellular backhaul retries deliver duplicate `MeterIntervalId` packets into `silver.stg_reads`. Complete `SELECT *, ____ AS rn FROM silver.stg_reads` so `WHERE rn = 1` keeps strictly one latest packet per interval ID?

Domain: Prepare data

- A. RANK() OVER (ORDER BY SpecimenId DESC)
- B. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- C. TRY_CAST(RawReading AS DECIMAL(18, 4))
- D. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)

### 54. Roaming international SIM calls arrive in `FactCDR` with carrier codes not yet loaded into `DimPartnerCarrier`. How should Gold ETL handle those unmatched carrier keys?

Domain: Prepare data

- A. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- B. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- C. Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE
- D. Filter Incremental Refresh with OrderDate >= RangeStart AND OrderDate <= RangeEnd using inclusive operators on both boundaries

### 55. Which two data-quality steps ensure a 75-million-row smart-water-meter CSV is profiled across all 75M rows (not just top 1,000) and stripped of duplicate `(MeterId, ReadTimestamp)` keys? Select two.

Domain: Prepare data

- A. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- B. Launch Data Wrangler from a Fabric Spark notebook (or enable Power Query Column profiling based on entire data set) to inspect nulls, duplicates, and distributions and export generated PySpark code
- C. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- E. Deduplicate using ROW_NUMBER() OVER (PARTITION BY BusinessKey ORDER BY ModifiedTimestamp DESC) = 1

### 56. Legacy weather-station CSV feeds write `"OFFLINE"` into numeric `WindSpeedMps` columns (`SELECT StationId, ____ AS WindMps FROM stage.WeatherRaw;`). Which T-SQL expression converts numbers to exact 4-decimal fixed point while turning `"OFFLINE"` into `NULL`?

Domain: Prepare data

- A. CAST(RawReading AS FLOAT)
- B. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- C. TRY_CAST(RawReading AS DECIMAL(18, 4))
- D. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)

### 57. Proposed solution: In Power Query importing from an Oracle utility billing database, `View Native Query` is enabled on Step 1 (`Navigation`) but disabled after Step 2 (`Invoke Custom Function` running local M regex) ahead of Step 3 (`BillDate >= RangeStart`), so an engineer upgrades gateway VM RAM instead of reordering steps. What actually restores fast refresh speed?

Domain: Prepare data

- A. Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- D. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'

### 58. A municipal transit planner without SQL skills wants to visually join `FactBusDelays` and `DimRoute` inside `TransitWarehouse`, filter `DelayMinutes > 15`, group counts by `Borough`, and choose `Save as view`. Which browser tool provides this?

Domain: Prepare data

- A. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results
- B. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- C. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- D. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view

### 59. What happens to underlying OneLake Parquet files when an analyst creates a 4-step filtered aggregation in the `Visual query editor` and selects `Save as view`?

Domain: Prepare data

- A. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- B. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition
- C. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- D. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view

### 60. Inside `GridWarehouse`, engineers must (1) join `WeatherLakehouse.dbo.SolarIrradiance` in the same workspace with zero data copies, and (2) query `dbo.FactTariffRates` as of `2026-10-28T06:00:00.000` (`____`) for a regulatory dispute. Which two T-SQL features apply? Select two.

Domain: Prepare data

- A. OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')
- B. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- C. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- E. Query across a Warehouse and a Lakehouse SQL analytics endpoint in the same workspace using three-part T-SQL naming (SalesLakehouse.dbo.RawOrders)

### 61. Smart-grid PMU sensors report frequency every second into `GridEventhouse`. Complete `PMUTelemetry | where Timestamp > ago(1h) ____` to fetch the single latest full telemetry row per `SubstationId`?

Domain: Prepare data

- A. | summarize arg_max(IngestionTime, *) by SpecimenId
- B. | summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)
- C. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- D. | make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion

### 62. A telecom BI engineer wants to write `DEFINE MEASURE 'FactCDR'[TestDroppedCallPct] = DIVIDE([Dropped Calls], [Total Calls]) EVALUATE SUMMARIZECOLUMNS('DimRegion'[Region], "DroppedCallPct", [TestDroppedCallPct])` against a published model before saving. Which feature runs this?

Domain: Prepare data

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results
- C. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- D. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time

### 63. Complete `____` in DAX Query View to generate an audit table of every measure name, DAX expression, and display folder in `UtilityReliabilityModel`?

Domain: Prepare data

- A. CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))
- B. NAMEOF('DimTrade'[CurrencyPair])
- C. EVALUATE INFO.VIEW.MEASURES()
- D. [ManagerEmail] = USERPRINCIPALNAME()

### 64. `TelcoLakehouse` lands 1.6 billion V-Order Delta CDR rows in OneLake updated every 10 minutes, and NOC dashboards require sub-second interactive filtering without scheduled Import copies. Which storage mode fits best?

Domain: Implement and manage semantic models

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Configure Import storage mode
- C. Configure DirectQuery storage mode
- D. Configure Direct Lake storage mode

### 65. A grid composite model combines an `Import` hourly substation summary table with a `DirectQuery` 1-second SCADA detail table, both related to `DimSubstation` and `DimDate`. Which storage mode on `DimSubstation` and `DimDate` optimizes both?

Domain: Implement and manage semantic models

- A. Configure shared dimension tables in Dual storage mode inside a composite model
- B. Configure DirectQuery storage mode
- C. Configure Import storage mode
- D. Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop)

### 66. `FactOutages[OutageDateKey]` (`INT` `YYYYMMDD`) joins to `DimCalendar[DateKey]`. Why must you disable `Auto date/time` and run `Mark as date table` on `DimCalendar` (`CalendarDate`)?

Domain: Implement and manage semantic models

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- C. Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column
- D. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension

### 67. Which two star-schema steps prevent self-service utility analysts from summing `SubstationSurrogateKey`, sort `"Jan..Dec"` chronologically instead of alphabetically, and remove 16 hidden auto-date hierarchies? Select two.

Domain: Implement and manage semantic models

- A. Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column
- B. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- C. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- E. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension

### 68. `FactServiceOrders` links to `Calendar[DateKey]` via `CreatedDateKey` (active), `DispatchedDateKey` (inactive), and `CompletedDateKey` (inactive). Complete `Completed Orders = ____` (activating the inactive key) without duplicating `Calendar`?

Domain: Implement and manage semantic models

- A. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- B. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- C. CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))
- D. CALCULATE([Encounter Count], CROSSFILTER('FactEncounter'[EncounterKey], 'BridgeEncounterDiag'[EncounterKey], BOTH))

### 69. One `GridStormEvent` affects multiple `Counties`, and each `County` experiences multiple storms over the year via `BridgeStormCounty`. How should you propagate `County` filters to storm restoration costs without permanent global `Both` relationships?

Domain: Implement and manage semantic models

- A. Introduce a deduplicated Bridge table between the two dimensions and scope bidirectional propagation strictly inside specific measures using CROSSFILTER(..., BOTH)
- B. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- C. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other

### 70. Each row of `FactEnergyIntervals` stores `MWhGenerated` and `LocationalMarginalPrice`. Complete `Wholesale Revenue = ____(FactEnergyIntervals, FactEnergyIntervals[MWhGenerated] * FactEnergyIntervals[LocationalMarginalPrice])` without adding a calculated column?

Domain: Implement and manage semantic models

- A. Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches
- B. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table
- C. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- D. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)

### 71. A `[SAIDI Penalty Tier]` measure evaluates `[Rolling 12M Outage Minutes]` three times across `IF` branches. Caching `[Rolling 12M Outage Minutes]` in a `____` before `RETURN` eliminates two redundant Storage Engine scans?

Domain: Implement and manage semantic models

- A. Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches
- B. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- C. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table
- D. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows

### 72. Proposed solution: A telecom analyst writes `5G Dropped Calls = CALCULATE([Dropped Calls], FILTER(FactCDR, FactCDR[RadioTech] = "5G"))` over 1.6 billion rows, causing multi-second Formula Engine scans. What compact filter argument replaces `FILTER(FactCDR, ...)` while preserving user slicer intersections?

Domain: Implement and manage semantic models

- A. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- B. Pass simple column predicates wrapped in KEEPFILTERS(DimProduct[Color] = "Red") to CALCULATE instead of FILTER(ALL(FactSales), ...)
- C. [ManagerEmail] = USERPRINCIPALNAME()
- D. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically

### 73. On a `Region -> Substation -> Feeder` matrix using a custom regulatory tariff calendar, you need (1) `[Prior Tariff Cycle Peak MW]` (`____`), and (2) `[Feeder Voltage Unbalance %]` shown only on `Feeder` leaf rows and `BLANK()` on `Substation`/`Region` subtotals (`____`). Which two DAX patterns apply? Select two.

Domain: Implement and manage semantic models

- A. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC)))
- D. IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK())
- E. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension

### 74. Utility regulators require `Current Month`, `YTD`, `Rolling 12M`, and `YoY %` across 40 reliability and revenue measures (`SAIDI`, `SAIFI`, `CAIDI`, `MWh`, `ARPU`). Which feature avoids authoring 160 separate measures?

Domain: Implement and manage semantic models

- A. Create a Calculation Group with Calculation Items referencing SELECTEDMEASURE() and explicit Precedence ordering (automatically setting DiscourageImplicitMeasures = true)
- B. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- C. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 75. Why must you use a `Dynamic Format String` expression (`"$#,0"` vs `"0.00%"` vs `"#,0 \M\W\h"`) instead of `FORMAT()` when switching units in a telecom executive KPI chart?

Domain: Implement and manage semantic models

- A. Configure a Dynamic Format String expression on the measure or calculation item (for example returning "\$#,0.00" vs "0.0%" via SELECTEDMEASUREFORMATSTRING()) without wrapping values in FORMAT()
- B. Mark the item as Promoted in item settings
- C. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- D. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically

### 76. In a `NetworkBreakdown` Field Parameter (`{ ("Band", 'DimCell'[SpectrumBand], 0), ("Vendor", ____, 1) }`), which DAX function wraps column or measure references so object renames automatically update parameter metadata?

Domain: Implement and manage semantic models

- A. [ManagerEmail] = USERPRINCIPALNAME()
- B. CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))
- C. EVALUATE INFO.VIEW.MEASURES()
- D. NAMEOF('DimTrade'[CurrencyPair])

### 77. A statewide smart-meter Import semantic model reaches 21 GB compressed on an F128 capacity. Which semantic-model setting allows refreshes beyond 10 GB and enables fast XMLA partition updates?

Domain: Implement and manage semantic models

- A. Configure DirectQuery storage mode
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages
- D. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)

### 78. On a large 12-GB smart-meter Import semantic model configured with Incremental Refresh, meter firmware backfills occasionally update `LastValidatedUTC` on historical partitions, AND dispatchers also want today's unclosed hours queried live. Which two Incremental Refresh options handle both?

Domain: Implement and manage semantic models

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Enable Detect data changes on an immutable LastModifiedUTC audit column (different from the partitioned OrderDate column) and optionally enable Get the latest data in real time with DirectQuery
- C. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- D. Filter Incremental Refresh with OrderDate >= RangeStart AND OrderDate <= RangeEnd using inclusive operators on both boundaries

### 79. Telecom architects want one semantic model joining `FactCDR` from `NetworkLakehouse` (`Direct Lake`), `DimSubscriber` from `BillingWarehouse` (`Direct Lake`), and `Import` FCC spectrum-auction tables from a public web URL with regular relationships. Which architecture supports this?

Domain: Implement and manage semantic models

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Build a Direct Lake on OneLake composite semantic model combining Direct Lake fact tables from OneLake with Import dimension/target tables using regular relationships
- C. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 80. Which two composite-modeling features let (1) `Tower x Day` visuals hit VertiPaq RAM over an 8-billion-row `DirectQuery` packet table, and (2) a municipal analyst join a local CSV bus-reroute sheet onto the Certified `RegionalTransit` semantic model? Select two.

Domain: Implement and manage semantic models

- A. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table
- D. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- E. Create a local composite model using DirectQuery for Power BI semantic models and Analysis Services to combine a certified core semantic model with a departmental Excel/SQL table

### 81. A grid-control overview page with 44 individual KPI card visuals takes 9.8 seconds to render even though every DAX query completes in <25 ms. Which tool proves `Other` visual-queue contention is responsible?

Domain: Implement and manage semantic models

- A. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- B. Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View
- C. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- D. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts

### 82. On a `DirectQuery` cell-site troubleshooting page, engineers pick 10 cell-tower IDs in a slicer; how do you prevent 9 wasted intermediate SQL queries before the 10th tower is selected?

Domain: Implement and manage semantic models

- A. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- B. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- C. Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails
- D. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages

### 83. Profiling `[Peak Coincident Demand]` in DAX Studio `Server Timings` shows `Total: 11,200 ms`, `FE: 10,800 ms`, `SE: 400 ms`, and `CallbackDataID` on an iterator scanning `FactIntervals`. What is the root cause and fix?

Domain: Implement and manage semantic models

- A. Profile the slow measure in DAX Studio using Server Timings to inspect Formula Engine (FE) vs Storage Engine (SE) CPU, SE query count, and CallbackDataID warnings
- B. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- C. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- D. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts

### 84. Which four-step workflow systematically diagnoses, fixes, and cold-cache-verifies a slow Direct Lake `[ARPU Churn Impact]` measure?

Domain: Implement and manage semantic models

- A. Capture visual timings in Performance Analyzer → Profile captured DAX in DAX Studio with Server Timings and Query Plan → Refactor FILTER(Fact,...) into VAR-cached SE column predicates and run V-Order OPTIMIZE → Re-test with Clear Cache
- B. Hide slow measures in Display Folders → Turn on Auto date/time → Split one Gold dimension into 6 normalized snowflake tables → Remove calendar surrogate keys
- C. Immediately upgrade from F64 to F512 without profiling → Enable bidirectional cross-filtering on all relationships → Convert numeric measures to FORMAT() strings → Disable V-Order on Gold tables
- D. Test queries only against warm VertiPaq cache without Clear Cache → Add high-cardinality GUID calculated columns to FactSales → Force DirectQueryOnly behavior → Add 45 single-value card visuals to one page

### 85. On a `Direct Lake on SQL` utility model, operations wants queries to return an immediate error rather than hammering the Warehouse with fallback DirectQuery scans if a table exceeds rowgroup guardrails (`____` in TMDL). Which setting enforces this?

Domain: Implement and manage semantic models

- A. directLakeBehavior: directLakeOnly
- B. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- C. Expect Direct Lake on OneLake to automatically fall back to DirectQuery against the SQL analytics endpoint when capacity memory guardrails are exceeded
- D. CAST(RawReading AS FLOAT)

### 86. Which three practices keep a 1.9-billion-row `Direct Lake` telecom CDR model within F64 capacity guardrails and aligned to completed hourly ETL batches? Select three.

Domain: Implement and manage semantic models

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time
- C. Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes
- D. Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails
- E. Expect Direct Lake on OneLake to automatically fall back to DirectQuery against the SQL analytics endpoint when capacity memory guardrails are exceeded
- F. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension

### 87. Which four-step Power BI Desktop sequence upgrades a `Direct Lake on SQL` grid model (using only Delta tables) to `Direct Lake on OneLake` with a safe rollback checkpoint?

Domain: Implement and manage semantic models

- A. Delete the semantic model in Production breaking report GUID bindings → Recreate measures manually from screenshots → Share Lakehouse Admin rights with all report viewers → Disable V-Order
- B. Live edit the model in Power BI Desktop and save a Version history point → Script the semantic model in TMDL view → Replace Sql.Database(...) with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...") → Apply TMDL and run framing refresh
- C. Keep non-materialized SQL analytics endpoint views as the only sources → Switch TMDL expression to AzureStorage.DataLake without materializing Delta tables → Enable DirectQuery fallback on Direct Lake on OneLake → Bind an On-premises gateway
- D. Download the Direct Lake model as an offline Import .pbix → Convert all tables to Dual storage mode → Replace AzureStorage.DataLake with OleDb.DataSource → Re-upload to My Workspace

### 88. Which four-step workflow configures Incremental Refresh on an 850-million-row `FactUtilityBills` Import table retaining 10 years of archive partitions and refreshing the trailing 15 days?

Domain: Implement and manage semantic models

- A. Filter OrderDate > RangeEnd → Configure Detect data changes on the exact same OrderDate partition column → Disable query folding → Run XMLA clearValues without processing
- B. Publish an unfiltered 2-billion-row Import PBIX locally first → Define RangeStart in DAX calculated tables afterward → Set storage mode to Direct Lake on OneLake → Enable VNet gateway on Direct Lake
- C. Create case-sensitive DateTime parameters RangeStart and RangeEnd → Apply foldable half-open filter (>= RangeStart and < RangeEnd) → Configure table Incremental refresh policy → Publish to workspace and run initial refresh to generate partitions
- D. Create Text parameters named StartDate and EndDate → Add a custom M step breaking query folding before filtering → Use >= and <= inclusive bounds on both sides → Refresh only in Power BI Desktop

---

## Case study — AquaSpan Utilities

AquaSpan Utilities created an early Direct Lake semantic model from a Lakehouse SQL analytics endpoint that suffers unexpected DirectQuery fallbacks and cannot add tables from a second Warehouse. Engineers plan to convert the model to Direct Lake on OneLake via Power BI Desktop, convert legacy `MeterBinaryHash` columns to supported types, and optimize DirectQuery detail joins on validated non-null keys.

The next 3 questions refer to **AquaSpan Utilities**. Read the scenario brief once, then answer each item independently.

### 89. While migrating the semantic model from `Direct Lake on SQL` to `Direct Lake on OneLake` in Power BI Desktop TMDL view, which M expression (`____`) replaces `Sql.Database(...)`?

Domain: Implement and manage semantic models

- A. AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/" & WorkspaceId & "/" & LakehouseId)
- B. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- C. CAST(RawReading AS FLOAT)
- D. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes

### 90. Why did `MeterBinaryHash` (`BINARY`) fail to load into the Direct Lake semantic model, and how should Gold ETL prepare it?

Domain: Prepare data

- A. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- B. Configure shared dimension tables in Dual storage mode inside a composite model
- C. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- D. Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake

### 91. For a companion `DirectQuery` meter-outage detail table whose foreign keys to `DimTransformer` are validated non-null in ETL, which relationship property switches SQL joins from `LEFT OUTER JOIN` to `INNER JOIN`?

Domain: Implement and manage semantic models

- A. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- B. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- C. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- D. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()

---

## Case study — CivicWorks Transit

CivicWorks Transit operates a public-transit Fabric Warehouse refreshed every night by Data Factory pipelines. Before running complex stored-procedure fare recalculations, engineers need an instant zero-copy backup copy of `dbo.FactRidership` inside the Warehouse, plus a single SQL summary query producing route, borough, and grand-total ridership subtotals in one pass.

The next 3 questions refer to **CivicWorks Transit**. Read the scenario brief once, then answer each item independently.

### 92. Complete `____;` (conceptually cloning `dbo.FactRidership`) to create an instantaneous zero-copy Warehouse backup table before running nightly fare recalculations?

Domain: Prepare data

- A. CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales
- B. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- C. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging

### 93. How should Data Factory pipelines encapsulate and execute the multi-step fare recalculation `MERGE` and audit-logging T-SQL transaction inside `TransitWarehouse`?

Domain: Prepare data

- A. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- B. Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view

### 94. Complete `SELECT RouteId, Borough, SUM(Riders) AS TotalRiders FROM gold.FactRidership ____;` to compute `(RouteId, Borough)` subtotals, `(Borough)` subtotals, and the citywide grand total `()` in one scan?

Domain: Prepare data

- A. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- B. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- C. TRY_CAST(RawReading AS DECIMAL(18, 4))
- D. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)

---

## Case study — SunGrid Renewables

SunGrid Renewables streams inverter telemetry payloads containing nested JSON `PhaseReadings` arrays into an Eventhouse and archives hourly generation in a Warehouse. Grid engineers need KQL queries expanding each phase element into rows, T-SQL queries comparing each hour's megawatt output to the prior hour's output per substation, and sargable date predicates that preserve Parquet file skipping.

The next 3 questions refer to **SunGrid Renewables**. Read the scenario brief once, then answer each item independently.

### 95. Solar inverters stream JSON payloads containing nested `PhaseReadings` arrays into `GridEventhouse`. Complete `InverterEvents ____ | summarize avg(toreal(PhaseReading.voltage)) by InverterId` to expand each phase element into its own row?

Domain: Prepare data

- A. | summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)
- B. | mv-expand PhaseReading = parse_json(Payload).PhaseReadings
- C. | make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion
- D. | summarize arg_max(IngestionTime, *) by SpecimenId

### 96. Complete `SELECT SubstationId, ReadingHour, MegawattOutput, MegawattOutput - ____ AS HourlyRampMW FROM gold.FactGeneration;` in the Warehouse to compare each hour's output against the immediately preceding hour per substation?

Domain: Prepare data

- A. TRY_CAST(RawReading AS DECIMAL(18, 4))
- B. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- C. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- D. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())

### 97. Why should grid engineers write `WHERE ReadingDate >= '2026-10-01' AND ReadingDate < '2026-11-01'` rather than `WHERE CONVERT(VARCHAR(7), ReadingDate, 120) = '2026-10'` on `gold.FactGeneration`?

Domain: Prepare data

- A. CAST(RawReading AS FLOAT)
- B. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- C. Filter on physical Delta partition or liquid-clustered date columns using sargable range predicates (OrderDate >= '2026-01-01') without wrapping the column in functions
- D. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'

---

## Case study — TelcoBeam Networks

TelcoBeam Networks publishes a Direct Lake subscriber-churn report to 1,500 retail store leads who hold Read + Build on the semantic model via an App, but security policy forbids granting store leads any direct access to the underlying Lakehouse or SQL analytics endpoint. Each store lead must see only rows matching their Microsoft Entra email address.

The next 3 questions refer to **TelcoBeam Networks**. Read the scenario brief once, then answer each item independently.

### 98. How must the `SubscriberChurn` Direct Lake semantic model connect to `ChurnLakehouse` so the 1,500 store leads can query reports and build thin visuals without holding any permissions on `ChurnLakehouse` or its SQL endpoint?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Contributor role
- B. Bind the Direct Lake semantic model to a cloud connection with a fixed identity and disable SSO
- C. Share the Lakehouse with ReadAll (Read all Apache Spark data) permission
- D. Enable single sign-on (SSO) on the Direct Lake semantic model connection

### 99. Complete the dynamic DAX RLS predicate `____` on `'DimStoreLead'` so each store lead sees only rows matching their signed-in Microsoft Entra email?

Domain: Maintain a data analytics solution

- A. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows
- B. [ManagerEmail] = USERPRINCIPALNAME()
- C. Filter the RLS table using USERNAME() = [DomainLogin] without testing in the Fabric portal
- D. NAMEOF('DimTrade'[CurrencyPair])

### 100. Before publishing the App to all 1,500 store leads, how do you verify both the DAX RLS predicate and effective workspace/item permissions for `lead42@telcobeam.com`?

Domain: Maintain a data analytics solution

- A. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- B. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- C. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- D. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts

---

## Answer key and explanations

### Question 1 — B

Answer: Assign the Workspace Contributor role. `Workspace Contributor` allows authoring and running workspace items without sharing, App-publishing, or role-management privileges. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: `Workspace Contributor` allows authoring and running workspace items without sharing, App-publishing, or role-management privileges.
- **B:** Correct. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. In this scenario: `Workspace Contributor` allows authoring and running workspace items without sharing, App-publishing, or role-management privileges.
- **C:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: `Workspace Contributor` allows authoring and running workspace items without sharing, App-publishing, or role-management privileges.
- **D:** Incorrect for this requirement. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. Why the keyed choice wins: `Workspace Contributor` allows authoring and running workspace items without sharing, App-publishing, or role-management privileges.

### Question 2 — C

Answer: Assign the Workspace Viewer role. `Workspace Viewer` is the only workspace role subject to OneLake security and semantic-model RLS; `Contributor`, `Member`, and `Admin` bypass RLS. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Incorrect for this requirement. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. Why the keyed choice wins: `Workspace Viewer` is the only workspace role subject to OneLake security and semantic-model RLS; `Contributor`, `Member`, and `Admin` bypass RLS.
- **B:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: `Workspace Viewer` is the only workspace role subject to OneLake security and semantic-model RLS; `Contributor`, `Member`, and `Admin` bypass RLS.
- **C:** Correct. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. In this scenario: `Workspace Viewer` is the only workspace role subject to OneLake security and semantic-model RLS; `Contributor`, `Member`, and `Admin` bypass RLS.
- **D:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: `Workspace Viewer` is the only workspace role subject to OneLake security and semantic-model RLS; `Contributor`, `Member`, and `Admin` bypass RLS.

### Question 3 — B, E

Answers: Assign the Workspace Member role; Assign permissions to Microsoft Entra security groups rather than individual users. Assigning `Workspace Member` to a Microsoft Entra security group grants App-update, sharing, and OneLake-role management without `Workspace Admin` workspace-deletion rights. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: Assigning `Workspace Member` to a Microsoft Entra security group grants App-update, sharing, and OneLake-role management without `Workspace Admin` workspace-deletion rights.
- **B:** Correct. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. In this scenario: Assigning `Workspace Member` to a Microsoft Entra security group grants App-update, sharing, and OneLake-role management without `Workspace Admin` workspace-deletion rights.
- **C:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: Assigning `Workspace Member` to a Microsoft Entra security group grants App-update, sharing, and OneLake-role management without `Workspace Admin` workspace-deletion rights.
- **D:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: Assigning `Workspace Member` to a Microsoft Entra security group grants App-update, sharing, and OneLake-role management without `Workspace Admin` workspace-deletion rights.
- **E:** Correct. Granting workspace, item, deployment-pipeline, and RLS role memberships to Microsoft Entra security groups centralizes joiner/mover/leaver governance and scales across workspaces without per-user ACL drift. In this scenario: Assigning `Workspace Member` to a Microsoft Entra security group grants App-update, sharing, and OneLake-role management without `Workspace Admin` workspace-deletion rights.

### Question 4 — D

Answer: Grant Build permission on the shared semantic model. `Build` permission on the shared semantic model enables live thin reports and `Analyze in Excel` without workspace Contributor access. Build permission on a semantic model allows analysts to create new Power BI reports, use Analyze in Excel, and issue XMLA/DAX queries against the model without granting workspace Contributor rights or underlying Lakehouse access. Local study-map skill 1.2 (Implement Item-Level Access Controls (Read, ReadData, ReadAll, Build, SSO vs Fixed Identity)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Share items in Microsoft Fabric & Semantic model Build permission (https://learn.microsoft.com/en-us/fabric/fundamentals/share-items).

- **A:** Incorrect for this requirement. ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled. Why the keyed choice wins: `Build` permission on the shared semantic model enables live thin reports and `Analyze in Excel` without workspace Contributor access.
- **B:** Incorrect for this requirement. Item-level Read metadata permission lets a user connect to a Lakehouse or Warehouse item container without granting broad OneLake file access; combine with SELECT or OneLake security roles for granular least-privilege access. Why the keyed choice wins: `Build` permission on the shared semantic model enables live thin reports and `Analyze in Excel` without workspace Contributor access.
- **C:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: `Build` permission on the shared semantic model enables live thin reports and `Analyze in Excel` without workspace Contributor access.
- **D:** Correct. Build permission on a semantic model allows analysts to create new Power BI reports, use Analyze in Excel, and issue XMLA/DAX queries against the model without granting workspace Contributor rights or underlying Lakehouse access. In this scenario: `Build` permission on the shared semantic model enables live thin reports and `Analyze in Excel` without workspace Contributor access.

### Question 5 — A

Answer: Enable OneLake security and define Read Grant roles → Assign consumers Workspace Viewer and OneLake security roles → Set SQL analytics endpoint to User's identity mode → Expose downstream shortcuts in User's identity mode. Defining Read Grant roles on `SmartMeterLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access. Correct order: enable OneLake security with Grant roles first, assign consumers to Viewer + security roles (never Contributor), set SQL analytics endpoints to User's identity mode, and expose shortcuts downstream. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Correct. Correct order: enable OneLake security with Grant roles first, assign consumers to Viewer + security roles (never Contributor), set SQL analytics endpoints to User's identity mode, and expose shortcuts downstream. In this scenario: Defining Read Grant roles on `SmartMeterLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access.
- **B:** Incorrect for this requirement. Incorrect: Contributors bypass OneLake security completely, OneLake security has no Deny role type, and Owner fixed identity bypasses per-user role evaluation on SQL queries. Why the keyed choice wins: Defining Read Grant roles on `SmartMeterLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access.
- **C:** Incorrect for this requirement. Incorrect: Members bypass OneLake security, ReadWrite roles cannot contain RLS/CLS rules, and OneLake shortcuts do not use On-premises gateways. Why the keyed choice wins: Defining Read Grant roles on `SmartMeterLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access.
- **D:** Incorrect for this requirement. Incorrect: mixing pre-existing SQL granular access with Delegated mode forces 100% DirectQuery fallback instead of clean OneLake security evaluation. Why the keyed choice wins: Defining Read Grant roles on `SmartMeterLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access.

### Question 6 — A, C

Answers: Define both the RLS filter and CLS column allow-list inside a single OneLake security Grant role with Read permission; Create a OneLake security role scoped to the specific Files/<subfolder> path with Read permission. A folder-scoped `Read` Grant role isolates `Files/drone_lidar/region4/`, and a single `Read` Grant role combining both RLS and CLS secures `Tables/Outages`. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Correct. OneLake security supports Grant roles only (Read permission required for RLS/CLS) and requires combining RLS and CLS on the same table within a single role — separate RLS and CLS roles on the same table return query errors. In this scenario: A folder-scoped `Read` Grant role isolates `Files/drone_lidar/region4/`, and a single `Read` Grant role combining both RLS and CLS secures `Tables/Outages`.
- **B:** Incorrect for this requirement. OneLake security does not support combining an RLS role and a CLS role across separate roles on the same table; members assigned to that combination receive query errors. Why the keyed choice wins: A folder-scoped `Read` Grant role isolates `Files/drone_lidar/region4/`, and a single `Read` Grant role combining both RLS and CLS secures `Tables/Outages`.
- **C:** Correct. OneLake folder-level security grants inherited Read (or ReadWrite) access to the selected subfolder and its descendants while allowing parent traversal without exposing sibling folders or Tables. In this scenario: A folder-scoped `Read` Grant role isolates `Files/drone_lidar/region4/`, and a single `Read` Grant role combining both RLS and CLS secures `Tables/Outages`.
- **D:** Incorrect for this requirement. OneLake security supports Grant roles only — there is no Deny role type, and OneLake security never restricts Workspace Admins, Members, or Contributors. Why the keyed choice wins: A folder-scoped `Read` Grant role isolates `Files/drone_lidar/region4/`, and a single `Read` Grant role combining both RLS and CLS secures `Tables/Outages`.
- **E:** Incorrect for this requirement. OneLake security roles granting ReadWrite permission cannot contain RLS or CLS constraints; fine-grained row and column rules are supported only on Read roles. Why the keyed choice wins: A folder-scoped `Read` Grant role isolates `Files/drone_lidar/region4/`, and a single `Read` Grant role combining both RLS and CLS secures `Tables/Outages`.

### Question 7 — C

Answer: Apply a Microsoft Purview sensitivity label with downstream inheritance on the source Lakehouse or Warehouse. Sensitivity-label downstream inheritance automatically propagates Purview classifications from Warehouses and Lakehouses to dependent semantic models and reports. Sensitivity labels applied to Fabric Lakehouses, Warehouses, and Semantic Models automatically propagate downstream to newly connected semantic models, reports, and exported Excel/PDF/PPTX files when inheritance is enabled. Local study-map skill 1.4 (Apply Microsoft Purview Sensitivity Labels, Inheritance, Default/Mandatory Policies, and Export Encryption), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Information protection & sensitivity labels in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-overview).

- **A:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Sensitivity-label downstream inheritance automatically propagates Purview classifications from Warehouses and Lakehouses to dependent semantic models and reports.
- **B:** Incorrect for this requirement. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Why the keyed choice wins: Sensitivity-label downstream inheritance automatically propagates Purview classifications from Warehouses and Lakehouses to dependent semantic models and reports.
- **C:** Correct. Sensitivity labels applied to Fabric Lakehouses, Warehouses, and Semantic Models automatically propagate downstream to newly connected semantic models, reports, and exported Excel/PDF/PPTX files when inheritance is enabled. In this scenario: Sensitivity-label downstream inheritance automatically propagates Purview classifications from Warehouses and Lakehouses to dependent semantic models and reports.
- **D:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Sensitivity-label downstream inheritance automatically propagates Purview classifications from Warehouses and Lakehouses to dependent semantic models and reports.

### Question 8 — A

Answer: Use a Purview sensitivity label configured with file encryption so exported .pbix, Excel, PDF, and PowerPoint files stay protected outside Fabric. Purview Information Protection file encryption configured on the sensitivity label encrypts exported `.xlsx`, `.pdf`, `.pptx`, and `.pbix` files automatically. While sensitivity labels in Fabric classify items in the workspace without encrypting OneLake Delta storage itself, encryption-enabled labels enforce rights management automatically when users export data to Excel, PDF, PowerPoint, or .pbix. Local study-map skill 1.4 (Apply Microsoft Purview Sensitivity Labels, Inheritance, Default/Mandatory Policies, and Export Encryption), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Information protection & sensitivity labels in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-overview).

- **A:** Correct. While sensitivity labels in Fabric classify items in the workspace without encrypting OneLake Delta storage itself, encryption-enabled labels enforce rights management automatically when users export data to Excel, PDF, PowerPoint, or .pbix. In this scenario: Purview Information Protection file encryption configured on the sensitivity label encrypts exported `.xlsx`, `.pdf`, `.pptx`, and `.pbix` files automatically.
- **B:** Incorrect for this requirement. Dynamic Data Masking obfuscates sensitive strings/emails/numbers in query results for users lacking UNMASK permission while keeping the column present so SELECT * queries do not fail. Why the keyed choice wins: Purview Information Protection file encryption configured on the sensitivity label encrypts exported `.xlsx`, `.pdf`, `.pptx`, and `.pbix` files automatically.
- **C:** Incorrect for this requirement. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Why the keyed choice wins: Purview Information Protection file encryption configured on the sensitivity label encrypts exported `.xlsx`, `.pdf`, `.pptx`, and `.pbix` files automatically.
- **D:** Incorrect for this requirement. Item-level Read metadata permission lets a user connect to a Lakehouse or Warehouse item container without granting broad OneLake file access; combine with SELECT or OneLake security roles for granular least-privilege access. Why the keyed choice wins: Purview Information Protection file encryption configured on the sensitivity label encrypts exported `.xlsx`, `.pdf`, `.pptx`, and `.pbix` files automatically.

### Question 9 — A

Answer: Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal. `Certified` endorsement restricts badge assignment exclusively to admin-authorized governance reviewers. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Local study-map skill 1.5 (Endorse Items Using Promoted, Certified, and Master Data Governance Badges), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Endorsement (Promoted, Certified, Master data) in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview).

- **A:** Correct. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. In this scenario: `Certified` endorsement restricts badge assignment exclusively to admin-authorized governance reviewers.
- **B:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: `Certified` endorsement restricts badge assignment exclusively to admin-authorized governance reviewers.
- **C:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: `Certified` endorsement restricts badge assignment exclusively to admin-authorized governance reviewers.
- **D:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: `Certified` endorsement restricts badge assignment exclusively to admin-authorized governance reviewers.

### Question 10 — B

Answer: Mark the item as Promoted in item settings. `Promoted` endorsement can be applied by any item owner or editor with write access. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Local study-map skill 1.5 (Endorse Items Using Promoted, Certified, and Master Data Governance Badges), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Endorsement (Promoted, Certified, Master data) in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview).

- **A:** Incorrect for this requirement. Fabric admins can enable Master data endorsement for authoritative single-source-of-truth silver/gold data assets so analysts distinguish core reference items in the OneLake catalog. Why the keyed choice wins: `Promoted` endorsement can be applied by any item owner or editor with write access.
- **B:** Correct. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. In this scenario: `Promoted` endorsement can be applied by any item owner or editor with write access.
- **C:** Incorrect for this requirement. Mandatory and default sensitivity label policies in Microsoft Purview require content creators to classify unlabeled semantic models and reports on save and apply baseline classification automatically. Why the keyed choice wins: `Promoted` endorsement can be applied by any item owner or editor with write access.
- **D:** Incorrect for this requirement. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Why the keyed choice wins: `Promoted` endorsement can be applied by any item owner or editor with write access.

### Question 11 — B

Answer: Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch. Using `Branch out` in Source control provisions an isolated developer workspace tied to a dedicated feature branch until PR merge. In Fabric Git integration, workspaces map 1-to-1 to branches; branching out into a dedicated developer workspace isolates in-progress notebook, pipeline, and semantic model edits before merging via pull request. Local study-map skill 1.6 (Configure Workspace Version Control with Azure DevOps or GitHub (Branch Out, Commit, Update, Undo)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to Git integration in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration).

- **A:** Incorrect for this requirement. Undo reverts uncommitted workspace item modifications to match the connected Git branch HEAD without rewriting shared remote commit history. Why the keyed choice wins: Using `Branch out` in Source control provisions an isolated developer workspace tied to a dedicated feature branch until PR merge.
- **B:** Correct. In Fabric Git integration, workspaces map 1-to-1 to branches; branching out into a dedicated developer workspace isolates in-progress notebook, pipeline, and semantic model edits before merging via pull request. In this scenario: Using `Branch out` in Source control provisions an isolated developer workspace tied to a dedicated feature branch until PR merge.
- **C:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Using `Branch out` in Source control provisions an isolated developer workspace tied to a dedicated feature branch until PR merge.
- **D:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Using `Branch out` in Source control provisions an isolated developer workspace tied to a dedicated feature branch until PR merge.

### Question 12 — C

Answer: Connect shared Dev workspace to main → Branch out to an isolated developer workspace and commit .pbip/Notebook edits → Merge pull request into main in Git → Run Update all in Dev and promote via Deployment Pipeline. Connecting `Dev` to `main`, branching out to an isolated workspace, merging via pull request, running `Update all` in `Dev`, and promoting via Deployment Pipeline keeps Git and stages synchronized. Correct order: link Dev to main, branch out to an isolated workspace for feature work, validate and merge via Git PR into main, run Update all in Dev, and promote via Deployment Pipeline with stage rules. Local study-map skill 1.6 (Configure Workspace Version Control with Azure DevOps or GitHub (Branch Out, Commit, Update, Undo)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to Git integration in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration).

- **A:** Incorrect for this requirement. Incorrect: editing Production directly on feature branches and committing cache.abf violates ALM isolation, leaks cached data, and bypasses Test validation. Why the keyed choice wins: Connecting `Dev` to `main`, branching out to an isolated workspace, merging via pull request, running `Update all` in `Dev`, and promoting via Deployment Pipeline keeps Git and stages synchronized.
- **B:** Incorrect for this requirement. Incorrect: Fabric workspaces do not auto-pull remote PR merges — skipping Update from Git promotes stale pre-PR workspace state to Test. Why the keyed choice wins: Connecting `Dev` to `main`, branching out to an isolated workspace, merging via pull request, running `Update all` in `Dev`, and promoting via Deployment Pipeline keeps Git and stages synchronized.
- **C:** Correct. Correct order: link Dev to main, branch out to an isolated workspace for feature work, validate and merge via Git PR into main, run Update all in Dev, and promote via Deployment Pipeline with stage rules. In this scenario: Connecting `Dev` to `main`, branching out to an isolated workspace, merging via pull request, running `Update all` in `Dev`, and promoting via Deployment Pipeline keeps Git and stages synchronized.
- **D:** Incorrect for this requirement. Incorrect: My Workspace does not support full team Git ALM, Undo discards local changes rather than committing, and deleting .platform breaks item lineage. Why the keyed choice wins: Connecting `Dev` to `main`, branching out to an isolated workspace, merging via pull request, running `Update all` in `Dev`, and promoting via Deployment Pipeline keeps Git and stages synchronized.

### Question 13 — B

Answer: Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions. Saving as a Power BI Desktop project (`.pbip`) stores semantic models as modular TMDL text files and reports as PBIR JSON files for line-by-line Git merges. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. Local study-map skill 1.7 (Create and Manage Power BI Desktop Projects (.pbip) with TMDL, PBIR, and .gitignore Hygiene), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Power BI Desktop projects (.pbip), TMDL, and PBIR (https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Saving as a Power BI Desktop project (`.pbip`) stores semantic models as modular TMDL text files and reports as PBIR JSON files for line-by-line Git merges.
- **B:** Correct. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. In this scenario: Saving as a Power BI Desktop project (`.pbip`) stores semantic models as modular TMDL text files and reports as PBIR JSON files for line-by-line Git merges.
- **C:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Saving as a Power BI Desktop project (`.pbip`) stores semantic models as modular TMDL text files and reports as PBIR JSON files for line-by-line Git merges.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Saving as a Power BI Desktop project (`.pbip`) stores semantic models as modular TMDL text files and reports as PBIR JSON files for line-by-line Git merges.

### Question 14 — A, B

Answers: Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions; Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository. Committing `.pbip` (`TMDL` + `PBIR`) text metadata while excluding `**/cache.abf` and `**/localSettings.json` in `.gitignore` ensures clean diffs and zero data leakage. Local study-map skill 1.7 (Create and Manage Power BI Desktop Projects (.pbip) with TMDL, PBIR, and .gitignore Hygiene), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Power BI Desktop projects (.pbip), TMDL, and PBIR (https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview).

- **A:** Correct. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. In this scenario: Committing `.pbip` (`TMDL` + `PBIR`) text metadata while excluding `**/cache.abf` and `**/localSettings.json` in `.gitignore` ensures clean diffs and zero data leakage.
- **B:** Correct. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. In this scenario: Committing `.pbip` (`TMDL` + `PBIR`) text metadata while excluding `**/cache.abf` and `**/localSettings.json` in `.gitignore` ensures clean diffs and zero data leakage.
- **C:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Committing `.pbip` (`TMDL` + `PBIR`) text metadata while excluding `**/cache.abf` and `**/localSettings.json` in `.gitignore` ensures clean diffs and zero data leakage.
- **D:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Committing `.pbip` (`TMDL` + `PBIR`) text metadata while excluding `**/cache.abf` and `**/localSettings.json` in `.gitignore` ensures clean diffs and zero data leakage.
- **E:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Committing `.pbip` (`TMDL` + `PBIR`) text metadata while excluding `**/cache.abf` and `**/localSettings.json` in `.gitignore` ensures clean diffs and zero data leakage.

### Question 15 — D

Answer: Configure Deployment pipeline data source and parameter rules on the Test and Production stages. Configuring Deployment Pipeline data source rules on the `Production` stage rebinds supported semantic models to Production endpoints automatically. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Configuring Deployment Pipeline data source rules on the `Production` stage rebinds supported semantic models to Production endpoints automatically.
- **B:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Configuring Deployment Pipeline data source rules on the `Production` stage rebinds supported semantic models to Production endpoints automatically.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Configuring Deployment Pipeline data source rules on the `Production` stage rebinds supported semantic models to Production endpoints automatically.
- **D:** Correct. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. In this scenario: Configuring Deployment Pipeline data source rules on the `Production` stage rebinds supported semantic models to Production endpoints automatically.

### Question 16 — D

Answer: Perform a selective deployment selecting the modified item together with Select related to include required upstream dependencies. Selecting `SolarForecastReport` plus `Select related` runs a selective deployment promoting only the report and its required upstream dependency. Selective deployment in Fabric Deployment Pipelines promotes only chosen items between stages, and Select related ensures newly referenced lakehouses or semantic models deploy alongside dependent reports. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. Undo reverts uncommitted workspace item modifications to match the connected Git branch HEAD without rewriting shared remote commit history. Why the keyed choice wins: Selecting `SolarForecastReport` plus `Select related` runs a selective deployment promoting only the report and its required upstream dependency.
- **B:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Selecting `SolarForecastReport` plus `Select related` runs a selective deployment promoting only the report and its required upstream dependency.
- **C:** Incorrect for this requirement. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. Why the keyed choice wins: Selecting `SolarForecastReport` plus `Select related` runs a selective deployment promoting only the report and its required upstream dependency.
- **D:** Correct. Selective deployment in Fabric Deployment Pipelines promotes only chosen items between stages, and Select related ensures newly referenced lakehouses or semantic models deploy alongside dependent reports. In this scenario: Selecting `SolarForecastReport` plus `Select related` runs a selective deployment promoting only the report and its required upstream dependency.

### Question 17 — B

Answer: Use a Fabric Variable library (or autobinding across paired workspace items) to parameterize stage-specific environment references. A Fabric `Variable library` stores stage-aware environment values across Deployment Pipeline stages. Fabric Variable libraries store stage-specific workspace/lakehouse IDs, URLs, and thresholds across Dev/Test/Prod — essential for items like Data Pipelines and Direct Lake on OneLake models that do not use legacy SQL deployment rules. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Why the keyed choice wins: A Fabric `Variable library` stores stage-aware environment values across Deployment Pipeline stages.
- **B:** Correct. Fabric Variable libraries store stage-specific workspace/lakehouse IDs, URLs, and thresholds across Dev/Test/Prod — essential for items like Data Pipelines and Direct Lake on OneLake models that do not use legacy SQL deployment rules. In this scenario: A Fabric `Variable library` stores stage-aware environment values across Deployment Pipeline stages.
- **C:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: A Fabric `Variable library` stores stage-aware environment values across Deployment Pipeline stages.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: A Fabric `Variable library` stores stage-aware environment values across Deployment Pipeline stages.

### Question 18 — C

Answer: Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts. Switching to Workspace `Lineage` view, opening `Impact analysis` on `LegacyBillingWarehouse`, and selecting `Notify contacts` identifies cross-workspace dependents and alerts owners. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Local study-map skill 1.9 (Perform Downstream Dependency Impact Analysis Across Lakehouses, Warehouses, Dataflows, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Lineage and impact analysis in Microsoft Fabric workspaces (https://learn.microsoft.com/en-us/fabric/governance/lineage).

- **A:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: Switching to Workspace `Lineage` view, opening `Impact analysis` on `LegacyBillingWarehouse`, and selecting `Notify contacts` identifies cross-workspace dependents and alerts owners.
- **B:** Incorrect for this requirement. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. Why the keyed choice wins: Switching to Workspace `Lineage` view, opening `Impact analysis` on `LegacyBillingWarehouse`, and selecting `Notify contacts` identifies cross-workspace dependents and alerts owners.
- **C:** Correct. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. In this scenario: Switching to Workspace `Lineage` view, opening `Impact analysis` on `LegacyBillingWarehouse`, and selecting `Notify contacts` identifies cross-workspace dependents and alerts owners.
- **D:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Switching to Workspace `Lineage` view, opening `Impact analysis` on `LegacyBillingWarehouse`, and selecting `Notify contacts` identifies cross-workspace dependents and alerts owners.

### Question 19 — D

Answer: Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts. Power Query M shows only upstream sources; Workspace `Lineage` view -> `Impact analysis` enumerates all downstream semantic models, reports, and workspaces. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Local study-map skill 1.9 (Perform Downstream Dependency Impact Analysis Across Lakehouses, Warehouses, Dataflows, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Lineage and impact analysis in Microsoft Fabric workspaces (https://learn.microsoft.com/en-us/fabric/governance/lineage).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Power Query M shows only upstream sources; Workspace `Lineage` view -> `Impact analysis` enumerates all downstream semantic models, reports, and workspaces.
- **B:** Incorrect for this requirement. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Why the keyed choice wins: Power Query M shows only upstream sources; Workspace `Lineage` view -> `Impact analysis` enumerates all downstream semantic models, reports, and workspaces.
- **C:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: Power Query M shows only upstream sources; Workspace `Lineage` view -> `Impact analysis` enumerates all downstream semantic models, reports, and workspaces.
- **D:** Correct. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. In this scenario: Power Query M shows only upstream sources; Workspace `Lineage` view -> `Impact analysis` enumerates all downstream semantic models, reports, and workspaces.

### Question 20 — C

Answer: Verify XMLA Endpoint = Read Write on target capacity → Connect ALM Toolkit to Dev source and Prod XMLA target → Compare schemas while hiding unchanged partitions and keeping Prod data sources → Validate and deploy metadata-only TMSL changes. Verifying `XMLA Endpoint = Read Write`, comparing Dev and Prod in ALM Toolkit while hiding unchanged partitions and keeping Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing. Correct order: confirm Read Write XMLA capacity setting, compare Dev vs Prod models, preserve Prod partition state and data-source bindings, and push metadata-only measure/relationship diffs. Local study-map skill 1.10 (Deploy and Manage Semantic Models Using the XMLA Endpoint (Read-Write, TMSL, Tabular Editor, ALM Toolkit)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model connectivity and management with the XMLA endpoint (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools).

- **A:** Incorrect for this requirement. Incorrect: XMLA Off blocks external deployment, and overwriting Production with an unpartitioned file destroys incremental partitions and causes prolonged outage. Why the keyed choice wins: Verifying `XMLA Endpoint = Read Write`, comparing Dev and Prod in ALM Toolkit while hiding unchanged partitions and keeping Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing.
- **B:** Incorrect for this requirement. Incorrect: Read Only XMLA rejects TMSL model deployments, and Capacity Admin rights violate least privilege. Why the keyed choice wins: Verifying `XMLA Endpoint = Read Write`, comparing Dev and Prod in ALM Toolkit while hiding unchanged partitions and keeping Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing.
- **C:** Correct. Correct order: confirm Read Write XMLA capacity setting, compare Dev vs Prod models, preserve Prod partition state and data-source bindings, and push metadata-only measure/relationship diffs. In this scenario: Verifying `XMLA Endpoint = Read Write`, comparing Dev and Prod in ALM Toolkit while hiding unchanged partitions and keeping Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing.
- **D:** Incorrect for this requirement. Incorrect: DAX Studio is a query/profiling tool (not a model-deployment tool), and unversioned Production hotfixes cause immediate drift on next deployment. Why the keyed choice wins: Verifying `XMLA Endpoint = Read Write`, comparing Dev and Prod in ALM Toolkit while hiding unchanged partitions and keeping Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing.

### Question 21 — B, E

Answers: Enable XMLA Endpoint = Read Write in Fabric Capacity workload settings and connect to powerbi://api.powerbi.com/v1.0/myorg/<WorkspaceName>; {"refresh": {"type": "dataOnly", "objects": [{"database": "WealthModel", "table": "FactPositions", "partition": "2026M10"}]}}. Enabling `XMLA Endpoint = Read Write` on the Fabric capacity and sending a partition-scoped TMSL `dataOnly` refresh reloads only the active partition. Local study-map skill 1.10 (Deploy and Manage Semantic Models Using the XMLA Endpoint (Read-Write, TMSL, Tabular Editor, ALM Toolkit)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model connectivity and management with the XMLA endpoint (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools).

- **A:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: Enabling `XMLA Endpoint = Read Write` on the Fabric capacity and sending a partition-scoped TMSL `dataOnly` refresh reloads only the active partition.
- **B:** Correct. A TMSL refresh command with type = "dataOnly" scoped to a single partition reloads raw partition data over XMLA without rebuilding global relationships or calculated tables. In this scenario: Enabling `XMLA Endpoint = Read Write` on the Fabric capacity and sending a partition-scoped TMSL `dataOnly` refresh reloads only the active partition.
- **C:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Enabling `XMLA Endpoint = Read Write` on the Fabric capacity and sending a partition-scoped TMSL `dataOnly` refresh reloads only the active partition.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Enabling `XMLA Endpoint = Read Write` on the Fabric capacity and sending a partition-scoped TMSL `dataOnly` refresh reloads only the active partition.
- **E:** Correct. External ALM tools (Tabular Editor, SSMS, ALM Toolkit, SqlPackage/PowerShell Invoke-ASCmd) require workspace Fabric/Premium capacity with XMLA Endpoint set to Read Write to deploy or modify semantic models. In this scenario: Enabling `XMLA Endpoint = Read Write` on the Fabric capacity and sending a partition-scoped TMSL `dataOnly` refresh reloads only the active partition.

### Question 22 — C

Answer: Publish a single certified core semantic model in a data workspace and build thin live-connected Power BI reports in departmental workspaces. Authoring thin Power BI Desktop reports live-connected to the shared `RegionalTransit` semantic model (`Build` permission) reuses one centralized model. Decoupling a shared golden semantic model from thin live-connected reports prevents measure duplication, reduces capacity memory footprint, and enforces centralized RLS/endorsement across teams. Local study-map skill 1.11 (Create and Update Reusable Assets (.pbit Templates, .pbids Data Sources, and Shared Golden Semantic Models)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create and use report templates (.pbit), data sources (.pbids), and shared semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-templates).

- **A:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Authoring thin Power BI Desktop reports live-connected to the shared `RegionalTransit` semantic model (`Build` permission) reuses one centralized model.
- **B:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: Authoring thin Power BI Desktop reports live-connected to the shared `RegionalTransit` semantic model (`Build` permission) reuses one centralized model.
- **C:** Correct. Decoupling a shared golden semantic model from thin live-connected reports prevents measure duplication, reduces capacity memory footprint, and enforces centralized RLS/endorsement across teams. In this scenario: Authoring thin Power BI Desktop reports live-connected to the shared `RegionalTransit` semantic model (`Build` permission) reuses one centralized model.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Authoring thin Power BI Desktop reports live-connected to the shared `RegionalTransit` semantic model (`Build` permission) reuses one centralized model.

### Question 23 — D

Answer: Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows. Exporting a Power BI Template (`.pbit`) packages visuals, measures, schema, and parameter prompts with zero data rows. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Local study-map skill 1.11 (Create and Update Reusable Assets (.pbit Templates, .pbids Data Sources, and Shared Golden Semantic Models)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create and use report templates (.pbit), data sources (.pbids), and shared semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-templates).

- **A:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Exporting a Power BI Template (`.pbit`) packages visuals, measures, schema, and parameter prompts with zero data rows.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Exporting a Power BI Template (`.pbit`) packages visuals, measures, schema, and parameter prompts with zero data rows.
- **C:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Exporting a Power BI Template (`.pbit`) packages visuals, measures, schema, and parameter prompts with zero data rows.
- **D:** Correct. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. In this scenario: Exporting a Power BI Template (`.pbit`) packages visuals, measures, schema, and parameter prompts with zero data rows.

### Question 24 — C

Answer: Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network. Deploying an `On-premises data gateway` in High-Availability cluster mode across local servers provides redundant outbound connectivity. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Local study-map skill 2.1 (Create Data Connections (Shareable Cloud Connections, On-Premises Gateways, and VNet Data Gateways)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data source management, cloud connections, and VNet/on-premises gateways in Fabric (https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Deploying an `On-premises data gateway` in High-Availability cluster mode across local servers provides redundant outbound connectivity.
- **B:** Incorrect for this requirement. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. Why the keyed choice wins: Deploying an `On-premises data gateway` in High-Availability cluster mode across local servers provides redundant outbound connectivity.
- **C:** Correct. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. In this scenario: Deploying an `On-premises data gateway` in High-Availability cluster mode across local servers provides redundant outbound connectivity.
- **D:** Incorrect for this requirement. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. Why the keyed choice wins: Deploying an `On-premises data gateway` in High-Availability cluster mode across local servers provides redundant outbound connectivity.

### Question 25 — A

Answer: Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet. A Fabric `Virtual Network (VNet) data gateway` injected into a delegated subnet of `vnet-telco-prod` connects securely to private Azure data sources. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. Local study-map skill 2.1 (Create Data Connections (Shareable Cloud Connections, On-Premises Gateways, and VNet Data Gateways)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data source management, cloud connections, and VNet/on-premises gateways in Fabric (https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management).

- **A:** Correct. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. In this scenario: A Fabric `Virtual Network (VNet) data gateway` injected into a delegated subnet of `vnet-telco-prod` connects securely to private Azure data sources.
- **B:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: A Fabric `Virtual Network (VNet) data gateway` injected into a delegated subnet of `vnet-telco-prod` connects securely to private Azure data sources.
- **C:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: A Fabric `Virtual Network (VNet) data gateway` injected into a delegated subnet of `vnet-telco-prod` connects securely to private Azure data sources.
- **D:** Incorrect for this requirement. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. Why the keyed choice wins: A Fabric `Virtual Network (VNet) data gateway` injected into a delegated subnet of `vnet-telco-prod` connects securely to private Azure data sources.

### Question 26 — A

Answer: Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture. `OneLake catalog` -> `Govern` tab surfaces tenant/steward governance posture metrics and guided remediation actions alongside `Explore` discovery. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Local study-map skill 2.2 (Discover Data and Streams Using OneLake Catalog (Explore/Govern) and Real-Time Hub + Activator), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake catalog overview & Real-Time hub in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview).

- **A:** Correct. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. In this scenario: `OneLake catalog` -> `Govern` tab surfaces tenant/steward governance posture metrics and guided remediation actions alongside `Explore` discovery.
- **B:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: `OneLake catalog` -> `Govern` tab surfaces tenant/steward governance posture metrics and guided remediation actions alongside `Explore` discovery.
- **C:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `OneLake catalog` -> `Govern` tab surfaces tenant/steward governance posture metrics and guided remediation actions alongside `Explore` discovery.
- **D:** Incorrect for this requirement. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Why the keyed choice wins: `OneLake catalog` -> `Govern` tab surfaces tenant/steward governance posture metrics and guided remediation actions alongside `Explore` discovery.

### Question 27 — A, D

Answers: Use the Real-Time hub to subscribe to Microsoft.Fabric.OneLake.FileCreated events (or Capacity/CDC streams) and trigger an Activator rule; Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table. `Real-Time hub` centralizes stream/event discovery and Activator alerting, while `Eventstream` ingests and routes live SCADA telemetry. Local study-map skill 2.2 (Discover Data and Streams Using OneLake Catalog (Explore/Govern) and Real-Time Hub + Activator), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake catalog overview & Real-Time hub in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview).

- **A:** Correct. Real-Time hub unifies streaming sources, CDC feeds, Azure Blob events, and Fabric workspace/OneLake/Capacity events so analytics engineers can discover streams in one catalog and trigger event-driven pipelines or Notebooks via Activator. In this scenario: `Real-Time hub` centralizes stream/event discovery and Activator alerting, while `Eventstream` ingests and routes live SCADA telemetry.
- **B:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `Real-Time hub` centralizes stream/event discovery and Activator alerting, while `Eventstream` ingests and routes live SCADA telemetry.
- **C:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: `Real-Time hub` centralizes stream/event discovery and Activator alerting, while `Eventstream` ingests and routes live SCADA telemetry.
- **D:** Correct. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. In this scenario: `Real-Time hub` centralizes stream/event discovery and Activator alerting, while `Eventstream` ingests and routes live SCADA telemetry.
- **E:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Real-Time hub` centralizes stream/event discovery and Activator alerting, while `Eventstream` ingests and routes live SCADA telemetry.

### Question 28 — C

Answer: Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching. Creating external `OneLake shortcuts` to Amazon S3 and GCS mounts the remote Parquet paths directly in OneLake with optional shortcut caching. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: Creating external `OneLake shortcuts` to Amazon S3 and GCS mounts the remote Parquet paths directly in OneLake with optional shortcut caching.
- **B:** Incorrect for this requirement. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. Why the keyed choice wins: Creating external `OneLake shortcuts` to Amazon S3 and GCS mounts the remote Parquet paths directly in OneLake with optional shortcut caching.
- **C:** Correct. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. In this scenario: Creating external `OneLake shortcuts` to Amazon S3 and GCS mounts the remote Parquet paths directly in OneLake with optional shortcut caching.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Creating external `OneLake shortcuts` to Amazon S3 and GCS mounts the remote Parquet paths directly in OneLake with optional shortcut caching.

### Question 29 — B

Answer: Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog. `Fabric Database Mirroring` for Azure Cosmos DB continuously replicates source containers and CDC changes into OneLake Delta Parquet automatically. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `Fabric Database Mirroring` for Azure Cosmos DB continuously replicates source containers and CDC changes into OneLake Delta Parquet automatically.
- **B:** Correct. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. In this scenario: `Fabric Database Mirroring` for Azure Cosmos DB continuously replicates source containers and CDC changes into OneLake Delta Parquet automatically.
- **C:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: `Fabric Database Mirroring` for Azure Cosmos DB continuously replicates source containers and CDC changes into OneLake Delta Parquet automatically.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Fabric Database Mirroring` for Azure Cosmos DB continuously replicates source containers and CDC changes into OneLake Delta Parquet automatically.

### Question 30 — A

Answer: Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake. A Data Factory Pipeline `Copy activity` moves multi-terabyte raw files at maximum throughput and lowest CU overhead. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Correct. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. In this scenario: A Data Factory Pipeline `Copy activity` moves multi-terabyte raw files at maximum throughput and lowest CU overhead.
- **B:** Incorrect for this requirement. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` moves multi-terabyte raw files at maximum throughput and lowest CU overhead.
- **C:** Incorrect for this requirement. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` moves multi-terabyte raw files at maximum throughput and lowest CU overhead.
- **D:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` moves multi-terabyte raw files at maximum throughput and lowest CU overhead.

### Question 31 — C, D, E

Answers: Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations; Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog; Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching. `Dataflow Gen2` with Fast Copy handles low-code M merges, `Database Mirroring` replicates Snowflake CDC, and `OneLake shortcuts` virtualize ADLS Gen2 Parquet. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `Dataflow Gen2` with Fast Copy handles low-code M merges, `Database Mirroring` replicates Snowflake CDC, and `OneLake shortcuts` virtualize ADLS Gen2 Parquet.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Dataflow Gen2` with Fast Copy handles low-code M merges, `Database Mirroring` replicates Snowflake CDC, and `OneLake shortcuts` virtualize ADLS Gen2 Parquet.
- **C:** Correct. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. In this scenario: `Dataflow Gen2` with Fast Copy handles low-code M merges, `Database Mirroring` replicates Snowflake CDC, and `OneLake shortcuts` virtualize ADLS Gen2 Parquet.
- **D:** Correct. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. In this scenario: `Dataflow Gen2` with Fast Copy handles low-code M merges, `Database Mirroring` replicates Snowflake CDC, and `OneLake shortcuts` virtualize ADLS Gen2 Parquet.
- **E:** Correct. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. In this scenario: `Dataflow Gen2` with Fast Copy handles low-code M merges, `Database Mirroring` replicates Snowflake CDC, and `OneLake shortcuts` virtualize ADLS Gen2 Parquet.
- **F:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `Dataflow Gen2` with Fast Copy handles low-code M merges, `Database Mirroring` replicates Snowflake CDC, and `OneLake shortcuts` virtualize ADLS Gen2 Parquet.

### Question 32 — D

Answer: Choose a Fabric Eventhouse (KQL database). `Fabric Eventhouse` (KQL database) handles ultra-high-throughput time-series, log, JSON, and geospatial analytics via KQL. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Incorrect for this requirement. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) handles ultra-high-throughput time-series, log, JSON, and geospatial analytics via KQL.
- **B:** Incorrect for this requirement. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) handles ultra-high-throughput time-series, log, JSON, and geospatial analytics via KQL.
- **C:** Incorrect for this requirement. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) handles ultra-high-throughput time-series, log, JSON, and geospatial analytics via KQL.
- **D:** Correct. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. In this scenario: `Fabric Eventhouse` (KQL database) handles ultra-high-throughput time-series, log, JSON, and geospatial analytics via KQL.

### Question 33 — B

Answer: Choose a Fabric Data Warehouse. `Fabric Data Warehouse` provides a full transactional T-SQL engine with multi-table ACID writes and native SQL security over OneLake. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Fabric Data Warehouse` provides a full transactional T-SQL engine with multi-table ACID writes and native SQL security over OneLake.
- **B:** Correct. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. In this scenario: `Fabric Data Warehouse` provides a full transactional T-SQL engine with multi-table ACID writes and native SQL security over OneLake.
- **C:** Incorrect for this requirement. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. Why the keyed choice wins: `Fabric Data Warehouse` provides a full transactional T-SQL engine with multi-table ACID writes and native SQL security over OneLake.
- **D:** Incorrect for this requirement. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Why the keyed choice wins: `Fabric Data Warehouse` provides a full transactional T-SQL engine with multi-table ACID writes and native SQL security over OneLake.

### Question 34 — D, E

Answers: Choose a Fabric Lakehouse; Choose a SQL database in Microsoft Fabric. `SQL database in Microsoft Fabric` backs transactional OLTP apps (with auto-mirroring to OneLake), and `Lakehouse` stores unstructured `Files/` plus Spark Delta `Tables/`. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: `SQL database in Microsoft Fabric` backs transactional OLTP apps (with auto-mirroring to OneLake), and `Lakehouse` stores unstructured `Files/` plus Spark Delta `Tables/`.
- **B:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `SQL database in Microsoft Fabric` backs transactional OLTP apps (with auto-mirroring to OneLake), and `Lakehouse` stores unstructured `Files/` plus Spark Delta `Tables/`.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `SQL database in Microsoft Fabric` backs transactional OLTP apps (with auto-mirroring to OneLake), and `Lakehouse` stores unstructured `Files/` plus Spark Delta `Tables/`.
- **D:** Correct. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. In this scenario: `SQL database in Microsoft Fabric` backs transactional OLTP apps (with auto-mirroring to OneLake), and `Lakehouse` stores unstructured `Files/` plus Spark Delta `Tables/`.
- **E:** Correct. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. In this scenario: `SQL database in Microsoft Fabric` backs transactional OLTP apps (with auto-mirroring to OneLake), and `Lakehouse` stores unstructured `Files/` plus Spark Delta `Tables/`.

### Question 35 — C

Answer: Enable OneLake integration in the Import semantic model settings so imported model tables export as Delta tables to OneLake. Enabling `OneLake integration` in the Import semantic model settings exports Delta Parquet artifacts of imported tables to OneLake. OneLake integration for Import semantic models writes Delta Parquet artifacts of the model's imported tables into OneLake, allowing Lakehouse shortcuts and Spark/SQL users to reuse curated Power Query model outputs. Local study-map skill 2.5 (Implement OneLake Integration for Eventhouse (OneLake Availability) and Import Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Eventhouse OneLake availability & OneLake integration for semantic models (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/one-lake-availability).

- **A:** Incorrect for this requirement. Eventhouse KQL databases do not write Delta Parquet to OneLake unless OneLake availability is enabled, and Direct Lake on SQL does not support KQL databases (only Direct Lake on OneLake does once OneLake availability is on). Why the keyed choice wins: Enabling `OneLake integration` in the Import semantic model settings exports Delta Parquet artifacts of imported tables to OneLake.
- **B:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Enabling `OneLake integration` in the Import semantic model settings exports Delta Parquet artifacts of imported tables to OneLake.
- **C:** Correct. OneLake integration for Import semantic models writes Delta Parquet artifacts of the model's imported tables into OneLake, allowing Lakehouse shortcuts and Spark/SQL users to reuse curated Power Query model outputs. In this scenario: Enabling `OneLake integration` in the Import semantic model settings exports Delta Parquet artifacts of imported tables to OneLake.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Enabling `OneLake integration` in the Import semantic model settings exports Delta Parquet artifacts of imported tables to OneLake.

### Question 36 — D

Answer: Ingest streaming telemetry into an Eventhouse KQL database → Enable OneLake availability on the KQL database or table → Create an internal OneLake shortcut in the Lakehouse → Add the table to a Direct Lake on OneLake semantic model. Streaming into Eventhouse, enabling `OneLake availability` on the KQL database/table, creating an internal OneLake shortcut in the Lakehouse, and modeling with `Direct Lake on OneLake` unifies both datasets zero-copy. Correct order: land streaming events in Eventhouse, opt in to OneLake availability so Delta Parquet files sync to OneLake, surface via Lakehouse shortcut (or connect directly), and model with Direct Lake on OneLake. Local study-map skill 2.5 (Implement OneLake Integration for Eventhouse (OneLake Availability) and Import Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Eventhouse OneLake availability & OneLake integration for semantic models (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/one-lake-availability).

- **A:** Incorrect for this requirement. Incorrect: manual hourly CSV exports add latency, operational toil, and duplicate storage instead of native Eventhouse OneLake availability. Why the keyed choice wins: Streaming into Eventhouse, enabling `OneLake availability` on the KQL database/table, creating an internal OneLake shortcut in the Lakehouse, and modeling with `Direct Lake on OneLake` unifies both datasets zero-copy.
- **B:** Incorrect for this requirement. Incorrect: Direct Lake on SQL does not support KQL databases, disabling OneLake availability prevents Delta Parquet generation, and Direct Lake never uses gateways. Why the keyed choice wins: Streaming into Eventhouse, enabling `OneLake availability` on the KQL database/table, creating an internal OneLake shortcut in the Lakehouse, and modeling with `Direct Lake on OneLake` unifies both datasets zero-copy.
- **C:** Incorrect for this requirement. Incorrect: KQL tables are internal OneLake sources that only expose Delta Parquet folders after OneLake availability is enabled. Why the keyed choice wins: Streaming into Eventhouse, enabling `OneLake availability` on the KQL database/table, creating an internal OneLake shortcut in the Lakehouse, and modeling with `Direct Lake on OneLake` unifies both datasets zero-copy.
- **D:** Correct. Correct order: land streaming events in Eventhouse, opt in to OneLake availability so Delta Parquet files sync to OneLake, surface via Lakehouse shortcut (or connect directly), and model with Direct Lake on OneLake. In this scenario: Streaming into Eventhouse, enabling `OneLake availability` on the KQL database/table, creating an internal OneLake shortcut in the Lakehouse, and modeling with `Direct Lake on OneLake` unifies both datasets zero-copy.

### Question 37 — C

Answer: Use a Lakehouse Materialized Lake View (or persisted Gold Delta table) instead of a non-materialized SQL analytics endpoint view for Direct Lake on OneLake. `Direct Lake on OneLake` binds directly to Delta Parquet tables in OneLake and does not support non-materialized SQL analytics endpoint views. Non-materialized SQL analytics endpoint views cannot back Direct Lake on OneLake tables and force Direct Lake on SQL into DirectQuery fallback; materializing the view as a Delta table preserves pure in-memory Direct Lake speed. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: `Direct Lake on OneLake` binds directly to Delta Parquet tables in OneLake and does not support non-materialized SQL analytics endpoint views.
- **B:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: `Direct Lake on OneLake` binds directly to Delta Parquet tables in OneLake and does not support non-materialized SQL analytics endpoint views.
- **C:** Correct. Non-materialized SQL analytics endpoint views cannot back Direct Lake on OneLake tables and force Direct Lake on SQL into DirectQuery fallback; materializing the view as a Delta table preserves pure in-memory Direct Lake speed. In this scenario: `Direct Lake on OneLake` binds directly to Delta Parquet tables in OneLake and does not support non-materialized SQL analytics endpoint views.
- **D:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Direct Lake on OneLake` binds directly to Delta Parquet tables in OneLake and does not support non-materialized SQL analytics endpoint views.

### Question 38 — D

Answer: Use T-SQL GRANT/DENY SELECT on specific Warehouse schemas, tables, or views. T-SQL object-level security (`GRANT` on views paired with `DENY` or ungranted base schemas/tables) isolates raw PII tables from view consumers. Object-level security in Fabric Warehouse or SQL analytics endpoints controls visibility and query access to entire tables, views, or stored procedures using standard T-SQL GRANT and DENY permissions. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: T-SQL object-level security (`GRANT` on views paired with `DENY` or ungranted base schemas/tables) isolates raw PII tables from view consumers.
- **B:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: T-SQL object-level security (`GRANT` on views paired with `DENY` or ungranted base schemas/tables) isolates raw PII tables from view consumers.
- **C:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: T-SQL object-level security (`GRANT` on views paired with `DENY` or ungranted base schemas/tables) isolates raw PII tables from view consumers.
- **D:** Correct. Object-level security in Fabric Warehouse or SQL analytics endpoints controls visibility and query access to entire tables, views, or stored procedures using standard T-SQL GRANT and DENY permissions. In this scenario: T-SQL object-level security (`GRANT` on views paired with `DENY` or ungranted base schemas/tables) isolates raw PII tables from view consumers.

### Question 39 — D

Answer: Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions. Surrogate integer keys unify heterogeneous source natural keys, enable SCD Type 2 hardware-upgrade tracking, and compress foreign keys in `FactCDR`. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: Surrogate integer keys unify heterogeneous source natural keys, enable SCD Type 2 hardware-upgrade tracking, and compress foreign keys in `FactCDR`.
- **B:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Surrogate integer keys unify heterogeneous source natural keys, enable SCD Type 2 hardware-upgrade tracking, and compress foreign keys in `FactCDR`.
- **C:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Surrogate integer keys unify heterogeneous source natural keys, enable SCD Type 2 hardware-upgrade tracking, and compress foreign keys in `FactCDR`.
- **D:** Correct. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. In this scenario: Surrogate integer keys unify heterogeneous source natural keys, enable SCD Type 2 hardware-upgrade tracking, and compress foreign keys in `FactCDR`.

### Question 40 — B

Answer: Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes. Creating a conformed Gold `DimDate` / `DimInterval` dimension with tariff/holiday attributes provides consistent time attributes across all energy fact tables. A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Creating a conformed Gold `DimDate` / `DimInterval` dimension with tariff/holiday attributes provides consistent time attributes across all energy fact tables.
- **B:** Correct. A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering. In this scenario: Creating a conformed Gold `DimDate` / `DimInterval` dimension with tariff/holiday attributes provides consistent time attributes across all energy fact tables.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Creating a conformed Gold `DimDate` / `DimInterval` dimension with tariff/holiday attributes provides consistent time attributes across all energy fact tables.
- **D:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: Creating a conformed Gold `DimDate` / `DimInterval` dimension with tariff/holiday attributes provides consistent time attributes across all energy fact tables.

### Question 41 — C, E

Answers: Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs; Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions. Native Catalyst `pyspark.sql.functions` inside `.withColumn()` run vectorized across executors without Python UDF bottlenecks, and integer surrogate keys shrink Gold fact storage. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Native Catalyst `pyspark.sql.functions` inside `.withColumn()` run vectorized across executors without Python UDF bottlenecks, and integer surrogate keys shrink Gold fact storage.
- **B:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Native Catalyst `pyspark.sql.functions` inside `.withColumn()` run vectorized across executors without Python UDF bottlenecks, and integer surrogate keys shrink Gold fact storage.
- **C:** Correct. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. In this scenario: Native Catalyst `pyspark.sql.functions` inside `.withColumn()` run vectorized across executors without Python UDF bottlenecks, and integer surrogate keys shrink Gold fact storage.
- **D:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Native Catalyst `pyspark.sql.functions` inside `.withColumn()` run vectorized across executors without Python UDF bottlenecks, and integer surrogate keys shrink Gold fact storage.
- **E:** Correct. Native Catalyst/Photon-optimized pyspark.sql.functions execute in vectorized JVM/native code across partitions, avoiding the severe Python serialization bottleneck of row-level UDFs. In this scenario: Native Catalyst `pyspark.sql.functions` inside `.withColumn()` run vectorized across executors without Python UDF bottlenecks, and integer surrogate keys shrink Gold fact storage.

### Question 42 — D

Answer: Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns. `SCD Type 2` versions the tower upgrade with a new surrogate `TowerKey`, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Why the keyed choice wins: `SCD Type 2` versions the tower upgrade with a new surrogate `TowerKey`, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag.
- **B:** Incorrect for this requirement. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Why the keyed choice wins: `SCD Type 2` versions the tower upgrade with a new surrogate `TowerKey`, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag.
- **C:** Incorrect for this requirement. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Why the keyed choice wins: `SCD Type 2` versions the tower upgrade with a new surrogate `TowerKey`, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag.
- **D:** Correct. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. In this scenario: `SCD Type 2` versions the tower upgrade with a new surrogate `TowerKey`, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag.

### Question 43 — B

Answer: Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures. Enforcing a single uniform atomic grain per fact table (keeping separate `FactWorkOrders` and `FactWorkOrderParts` tables or allocating header truck cost across lines) eliminates fan-out inflation. Keeping fact tables at a single, consistent atomic grain with integer foreign keys and additive measures eliminates double-counting and supports flexible rollups across every conformed dimension. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Enforcing a single uniform atomic grain per fact table (keeping separate `FactWorkOrders` and `FactWorkOrderParts` tables or allocating header truck cost across lines) eliminates fan-out inflation.
- **B:** Correct. Keeping fact tables at a single, consistent atomic grain with integer foreign keys and additive measures eliminates double-counting and supports flexible rollups across every conformed dimension. In this scenario: Enforcing a single uniform atomic grain per fact table (keeping separate `FactWorkOrders` and `FactWorkOrderParts` tables or allocating header truck cost across lines) eliminates fan-out inflation.
- **C:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Enforcing a single uniform atomic grain per fact table (keeping separate `FactWorkOrders` and `FactWorkOrderParts` tables or allocating header truck cost across lines) eliminates fan-out inflation.
- **D:** Incorrect for this requirement. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Why the keyed choice wins: Enforcing a single uniform atomic grain per fact table (keeping separate `FactWorkOrders` and `FactWorkOrderParts` tables or allocating header truck cost across lines) eliminates fan-out inflation.

### Question 44 — A

Answer: Stage and deduplicate incoming records by natural key → Compare tracked attributes against active (IsCurrent = 1) Gold rows → Expire changed active rows (EffectiveEndDate, IsCurrent = 0) → Insert new active versions with fresh surrogate keys. Deduplicating staged tariffs, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves historical billing attribution. Correct order: deduplicate staging first, detect attribute changes against current rows, close out prior active intervals without losing their surrogate keys, and insert new active versions. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Correct. Correct order: deduplicate staging first, detect attribute changes against current rows, close out prior active intervals without losing their surrogate keys, and insert new active versions. In this scenario: Deduplicating staged tariffs, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves historical billing attribution.
- **B:** Incorrect for this requirement. Incorrect: regenerating surrogate keys on truncate breaks every existing historical fact foreign key, and marking multiple rows IsCurrent = 1 duplicates fact joins. Why the keyed choice wins: Deduplicating staged tariffs, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves historical billing attribution.
- **C:** Incorrect for this requirement. Incorrect: new versions must be active (IsCurrent = 1), EffectiveStartDate of historical intervals must remain immutable, and natural keys are required to match future CDC updates. Why the keyed choice wins: Deduplicating staged tariffs, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves historical billing attribution.
- **D:** Incorrect for this requirement. Incorrect: deleting unmatched keys and enabling Assume referential integrity omits orphan rows silently in INNER JOINs. Why the keyed choice wins: Deduplicating staged tariffs, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves historical billing attribution.

### Question 45 — A, B, C

Answers: Organize OneLake into Bronze (raw immutable), Silver (validated, deduplicated, conformed), and Gold (star-schema dimensions and facts with V-Order); Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place; Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE. Medallion zones separate data maturity layers, `SCD Type 1` overwrites typos in place, and `-1` Unknown surrogate members prevent dropped late-arriving facts. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Correct. The Medallion architecture separates raw source fidelity (Bronze), enterprise data quality/conformance (Silver), and BI/Direct Lake star-schema consumption (Gold). In this scenario: Medallion zones separate data maturity layers, `SCD Type 1` overwrites typos in place, and `-1` Unknown surrogate members prevent dropped late-arriving facts.
- **B:** Correct. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. In this scenario: Medallion zones separate data maturity layers, `SCD Type 1` overwrites typos in place, and `-1` Unknown surrogate members prevent dropped late-arriving facts.
- **C:** Correct. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. In this scenario: Medallion zones separate data maturity layers, `SCD Type 1` overwrites typos in place, and `-1` Unknown surrogate members prevent dropped late-arriving facts.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Medallion zones separate data maturity layers, `SCD Type 1` overwrites typos in place, and `-1` Unknown surrogate members prevent dropped late-arriving facts.
- **E:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Medallion zones separate data maturity layers, `SCD Type 1` overwrites typos in place, and `-1` Unknown surrogate members prevent dropped late-arriving facts.
- **F:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Medallion zones separate data maturity layers, `SCD Type 1` overwrites typos in place, and `-1` Unknown surrogate members prevent dropped late-arriving facts.

### Question 46 — A

Answer: Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension. Denormalizing `FeederCircuit`, `SubstationName`, and `TransmissionZone` directly onto `Gold.DimTransformer` flattens the 4-table snowflake into a 1-hop star dimension. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Local study-map skill 2.9 (Denormalize Snowflake Hierarchies into Flattened Gold Dimension Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Dimensional modeling & denormalizing snowflake tables in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables).

- **A:** Correct. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. In this scenario: Denormalizing `FeederCircuit`, `SubstationName`, and `TransmissionZone` directly onto `Gold.DimTransformer` flattens the 4-table snowflake into a 1-hop star dimension.
- **B:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Denormalizing `FeederCircuit`, `SubstationName`, and `TransmissionZone` directly onto `Gold.DimTransformer` flattens the 4-table snowflake into a 1-hop star dimension.
- **C:** Incorrect for this requirement. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Why the keyed choice wins: Denormalizing `FeederCircuit`, `SubstationName`, and `TransmissionZone` directly onto `Gold.DimTransformer` flattens the 4-table snowflake into a 1-hop star dimension.
- **D:** Incorrect for this requirement. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Why the keyed choice wins: Denormalizing `FeederCircuit`, `SubstationName`, and `TransmissionZone` directly onto `Gold.DimTransformer` flattens the 4-table snowflake into a 1-hop star dimension.

### Question 47 — C

Answer: Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension. Denormalizing `Manufacturer` and `CountryHQ` directly onto `Gold.DimHandset` enables a single `1:*` single-direction relationship to `FactCDR`. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Local study-map skill 2.9 (Denormalize Snowflake Hierarchies into Flattened Gold Dimension Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Dimensional modeling & denormalizing snowflake tables in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables).

- **A:** Incorrect for this requirement. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. Why the keyed choice wins: Denormalizing `Manufacturer` and `CountryHQ` directly onto `Gold.DimHandset` enables a single `1:*` single-direction relationship to `FactCDR`.
- **B:** Incorrect for this requirement. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. Why the keyed choice wins: Denormalizing `Manufacturer` and `CountryHQ` directly onto `Gold.DimHandset` enables a single `1:*` single-direction relationship to `FactCDR`.
- **C:** Correct. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. In this scenario: Denormalizing `Manufacturer` and `CountryHQ` directly onto `Gold.DimHandset` enables a single `1:*` single-direction relationship to `FactCDR`.
- **D:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Denormalizing `Manufacturer` and `CountryHQ` directly onto `Gold.DimHandset` enables a single `1:*` single-direction relationship to `FactCDR`.

### Question 48 — D

Answer: Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP). Materializing a pre-aggregated `FactMonthlyZipUsage` Gold Delta table (`GROUP BY MonthKey, ZipKey, RateClassKey`) serves regulatory visuals from tiny summary tables. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Materializing a pre-aggregated `FactMonthlyZipUsage` Gold Delta table (`GROUP BY MonthKey, ZipKey, RateClassKey`) serves regulatory visuals from tiny summary tables.
- **B:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Materializing a pre-aggregated `FactMonthlyZipUsage` Gold Delta table (`GROUP BY MonthKey, ZipKey, RateClassKey`) serves regulatory visuals from tiny summary tables.
- **C:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Materializing a pre-aggregated `FactMonthlyZipUsage` Gold Delta table (`GROUP BY MonthKey, ZipKey, RateClassKey`) serves regulatory visuals from tiny summary tables.
- **D:** Correct. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. In this scenario: Materializing a pre-aggregated `FactMonthlyZipUsage` Gold Delta table (`GROUP BY MonthKey, ZipKey, RateClassKey`) serves regulatory visuals from tiny summary tables.

### Question 49 — D

Answer: Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled. Folded `Group by` executes inside Azure SQL so only compact station-day summary rows stream over the network into Dataflow Gen2. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Folded `Group by` executes inside Azure SQL so only compact station-day summary rows stream over the network into Dataflow Gen2.
- **B:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Folded `Group by` executes inside Azure SQL so only compact station-day summary rows stream over the network into Dataflow Gen2.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Folded `Group by` executes inside Azure SQL so only compact station-day summary rows stream over the network into Dataflow Gen2.
- **D:** Correct. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. In this scenario: Folded `Group by` executes inside Azure SQL so only compact station-day summary rows stream over the network into Dataflow Gen2.

### Question 50 — C

Answer: WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET. `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only changed outage rows and avoids unnecessary Parquet rewrites. Guarding WHEN MATCHED with a hash/attribute inequality prevents rewriting unchanged Delta Parquet files on untouched rows during incremental upserts. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. Fabric Data Warehouse supports FILTER PREDICATE with inline TVFs (not stored procedures or SQL Server DML BLOCK PREDICATE triggers). Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only changed outage rows and avoids unnecessary Parquet rewrites.
- **B:** Incorrect for this requirement. Omitting PARTITION BY ranks across the entire table globally rather than per entity, and RANK() returns duplicate rank-1 rows on exact timestamp ties. Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only changed outage rows and avoids unnecessary Parquet rewrites.
- **C:** Correct. Guarding WHEN MATCHED with a hash/attribute inequality prevents rewriting unchanged Delta Parquet files on untouched rows during incremental upserts. In this scenario: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only changed outage rows and avoids unnecessary Parquet rewrites.
- **D:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only changed outage rows and avoids unnecessary Parquet rewrites.

### Question 51 — D

Answer: Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table. A `Left Anti Join` from `DimSmartMeter` to trailing-24h `FactMeterReads` returns exclusively meters with zero matching readings. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Why the keyed choice wins: A `Left Anti Join` from `DimSmartMeter` to trailing-24h `FactMeterReads` returns exclusively meters with zero matching readings.
- **B:** Incorrect for this requirement. Delta Lake MERGE INTO (in Spark SQL, PySpark DeltaTable.forPath().merge(), or Warehouse T-SQL) atomically applies incremental CDC inserts, updates, and soft-deletes in a single ACID transaction. Why the keyed choice wins: A `Left Anti Join` from `DimSmartMeter` to trailing-24h `FactMeterReads` returns exclusively meters with zero matching readings.
- **C:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: A `Left Anti Join` from `DimSmartMeter` to trailing-24h `FactMeterReads` returns exclusively meters with zero matching readings.
- **D:** Correct. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. In this scenario: A `Left Anti Join` from `DimSmartMeter` to trailing-24h `FactMeterReads` returns exclusively meters with zero matching readings.

### Question 52 — B, D

Answers: fact_df.join(F.broadcast(dim_store_df), on="StoreKey", how="left"); Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement. `F.broadcast(dim_cell_sector)` broadcasts the 6 MB table to executors without shuffling 2.2B CDRs, and Delta `MERGE INTO` performs atomic upserts. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `F.broadcast(dim_cell_sector)` broadcasts the 6 MB table to executors without shuffling 2.2B CDRs, and Delta `MERGE INTO` performs atomic upserts.
- **B:** Correct. Wrapping the small dimension DataFrame in pyspark.sql.functions.broadcast() avoids shuffling the multi-hundred-million-row fact DataFrame across Spark executors. In this scenario: `F.broadcast(dim_cell_sector)` broadcasts the 6 MB table to executors without shuffling 2.2B CDRs, and Delta `MERGE INTO` performs atomic upserts.
- **C:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `F.broadcast(dim_cell_sector)` broadcasts the 6 MB table to executors without shuffling 2.2B CDRs, and Delta `MERGE INTO` performs atomic upserts.
- **D:** Correct. Delta Lake MERGE INTO (in Spark SQL, PySpark DeltaTable.forPath().merge(), or Warehouse T-SQL) atomically applies incremental CDC inserts, updates, and soft-deletes in a single ACID transaction. In this scenario: `F.broadcast(dim_cell_sector)` broadcasts the 6 MB table to executors without shuffling 2.2B CDRs, and Delta `MERGE INTO` performs atomic upserts.
- **E:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: `F.broadcast(dim_cell_sector)` broadcasts the 6 MB table to executors without shuffling 2.2B CDRs, and Delta `MERGE INTO` performs atomic upserts.

### Question 53 — D

Answer: ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC). `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` assigns `rn = 1` to exactly one newest packet per key even on timestamp ties. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. Omitting PARTITION BY ranks across the entire table globally rather than per entity, and RANK() returns duplicate rank-1 rows on exact timestamp ties. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` assigns `rn = 1` to exactly one newest packet per key even on timestamp ties.
- **B:** Incorrect for this requirement. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` assigns `rn = 1` to exactly one newest packet per key even on timestamp ties.
- **C:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` assigns `rn = 1` to exactly one newest packet per key even on timestamp ties.
- **D:** Correct. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. In this scenario: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` assigns `rn = 1` to exactly one newest packet per key even on timestamp ties.

### Question 54 — C

Answer: Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE. Mapping unmatched keys via `COALESCE` to `-1` (`Unknown Partner Carrier`) in `DimPartnerCarrier` preserves roaming call totals and `1:*` Direct Lake integrity. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: Mapping unmatched keys via `COALESCE` to `-1` (`Unknown Partner Carrier`) in `DimPartnerCarrier` preserves roaming call totals and `1:*` Direct Lake integrity.
- **B:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Mapping unmatched keys via `COALESCE` to `-1` (`Unknown Partner Carrier`) in `DimPartnerCarrier` preserves roaming call totals and `1:*` Direct Lake integrity.
- **C:** Correct. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. In this scenario: Mapping unmatched keys via `COALESCE` to `-1` (`Unknown Partner Carrier`) in `DimPartnerCarrier` preserves roaming call totals and `1:*` Direct Lake integrity.
- **D:** Incorrect for this requirement. Using >= AND <= on both ends causes rows stamped exactly at midnight on partition boundaries to load into two adjacent partitions, silently double-counting sales totals. Why the keyed choice wins: Mapping unmatched keys via `COALESCE` to `-1` (`Unknown Partner Carrier`) in `DimPartnerCarrier` preserves roaming call totals and `1:*` Direct Lake integrity.

### Question 55 — B, E

Answers: Launch Data Wrangler from a Fabric Spark notebook (or enable Power Query Column profiling based on entire data set) to inspect nulls, duplicates, and distributions and export generated PySpark code; Deduplicate using ROW_NUMBER() OVER (PARTITION BY BusinessKey ORDER BY ModifiedTimestamp DESC) = 1. Full-dataset profiling in Spark Data Wrangler (or entire-dataset Power Query profiling) surfaces tail nulls/outliers, and `ROW_NUMBER() OVER (PARTITION BY ...)` deduplicates keys. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Full-dataset profiling in Spark Data Wrangler (or entire-dataset Power Query profiling) surfaces tail nulls/outliers, and `ROW_NUMBER() OVER (PARTITION BY ...)` deduplicates keys.
- **B:** Correct. Power Query profiles only the top 1,000 rows by default unless switched to entire dataset, whereas Data Wrangler interactively profiles Pandas/Spark DataFrames and emits reproducible Python/PySpark cleaning code. In this scenario: Full-dataset profiling in Spark Data Wrangler (or entire-dataset Power Query profiling) surfaces tail nulls/outliers, and `ROW_NUMBER() OVER (PARTITION BY ...)` deduplicates keys.
- **C:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Full-dataset profiling in Spark Data Wrangler (or entire-dataset Power Query profiling) surfaces tail nulls/outliers, and `ROW_NUMBER() OVER (PARTITION BY ...)` deduplicates keys.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Full-dataset profiling in Spark Data Wrangler (or entire-dataset Power Query profiling) surfaces tail nulls/outliers, and `ROW_NUMBER() OVER (PARTITION BY ...)` deduplicates keys.
- **E:** Correct. Windowing by BusinessKey ordered descending by ingestion or source-change timestamp deterministically retains only the latest version of duplicate CDC events while preserving all non-key columns. In this scenario: Full-dataset profiling in Spark Data Wrangler (or entire-dataset Power Query profiling) surfaces tail nulls/outliers, and `ROW_NUMBER() OVER (PARTITION BY ...)` deduplicates keys.

### Question 56 — C

Answer: TRY_CAST(RawReading AS DECIMAL(18, 4)). `TRY_CAST(RawReading AS DECIMAL(18, 4))` safely yields `NULL` on `"OFFLINE"` without failing the Warehouse batch load. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Local study-map skill 2.13 (Convert Column Data Types Safely (TRY_CAST, Fixed Decimal, and Direct Lake Supported Primitive Types)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data types in Fabric Data Warehouse and Direct Lake Delta tables (https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types).

- **A:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` safely yields `NULL` on `"OFFLINE"` without failing the Warehouse batch load.
- **B:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` safely yields `NULL` on `"OFFLINE"` without failing the Warehouse batch load.
- **C:** Correct. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. In this scenario: `TRY_CAST(RawReading AS DECIMAL(18, 4))` safely yields `NULL` on `"OFFLINE"` without failing the Warehouse batch load.
- **D:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` safely yields `NULL` on `"OFFLINE"` without failing the Warehouse batch load.

### Question 57 — A

Answer: Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled. Moving the foldable `BillDate >= RangeStart and BillDate < RangeEnd` filter ahead of the custom M function pushes the date predicate to Oracle's SQL engine. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. Local study-map skill 2.14 (Filter Data Early Preserving Power Query Folding (View Native Query) and Sargable Delta File Pruning), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query folding indicators & predicate pushdown in Power Query and Delta Lake (https://learn.microsoft.com/en-us/power-query/query-folding-basics).

- **A:** Correct. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. In this scenario: Moving the foldable `BillDate >= RangeStart and BillDate < RangeEnd` filter ahead of the custom M function pushes the date predicate to Oracle's SQL engine.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Moving the foldable `BillDate >= RangeStart and BillDate < RangeEnd` filter ahead of the custom M function pushes the date predicate to Oracle's SQL engine.
- **C:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Moving the foldable `BillDate >= RangeStart and BillDate < RangeEnd` filter ahead of the custom M function pushes the date predicate to Oracle's SQL engine.
- **D:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: Moving the foldable `BillDate >= RangeStart and BillDate < RangeEnd` filter ahead of the custom M function pushes the date predicate to Oracle's SQL engine.

### Question 58 — D

Answer: Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view. `New visual query` (Visual query editor) in the Warehouse builds diagram steps visually and saves them as a T-SQL view. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Local study-map skill 2.15 (Select, Filter, and Aggregate Data Using the Visual Query Editor and Save as SQL Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query using the Visual query editor in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/visual-query-editor).

- **A:** Incorrect for this requirement. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Why the keyed choice wins: `New visual query` (Visual query editor) in the Warehouse builds diagram steps visually and saves them as a T-SQL view.
- **B:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: `New visual query` (Visual query editor) in the Warehouse builds diagram steps visually and saves them as a T-SQL view.
- **C:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: `New visual query` (Visual query editor) in the Warehouse builds diagram steps visually and saves them as a T-SQL view.
- **D:** Correct. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. In this scenario: `New visual query` (Visual query editor) in the Warehouse builds diagram steps visually and saves them as a T-SQL view.

### Question 59 — D

Answer: Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view. Zero data is duplicated; `Save as view` stores only a virtual T-SQL `VIEW` metadata definition that queries live Delta Parquet tables on demand. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Local study-map skill 2.15 (Select, Filter, and Aggregate Data Using the Visual Query Editor and Save as SQL Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query using the Visual query editor in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/visual-query-editor).

- **A:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Zero data is duplicated; `Save as view` stores only a virtual T-SQL `VIEW` metadata definition that queries live Delta Parquet tables on demand.
- **B:** Incorrect for this requirement. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. Why the keyed choice wins: Zero data is duplicated; `Save as view` stores only a virtual T-SQL `VIEW` metadata definition that queries live Delta Parquet tables on demand.
- **C:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Zero data is duplicated; `Save as view` stores only a virtual T-SQL `VIEW` metadata definition that queries live Delta Parquet tables on demand.
- **D:** Correct. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. In this scenario: Zero data is duplicated; `Save as view` stores only a virtual T-SQL `VIEW` metadata definition that queries live Delta Parquet tables on demand.

### Question 60 — A, E

Answers: Query across a Warehouse and a Lakehouse SQL analytics endpoint in the same workspace using three-part T-SQL naming (SalesLakehouse.dbo.RawOrders); OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000'). Three-part T-SQL naming queries sibling Lakehouse SQL endpoints zero-copy, and `OPTION (FOR TIMESTAMP AS OF ...)` executes Warehouse Time Travel. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Correct. Fabric Data Warehouse Time Travel uses the query hint OPTION (FOR TIMESTAMP AS OF 'YYYY-MM-DDTHH:MM:SS.fff') to read exact point-in-time historical snapshots within the retention window. In this scenario: Three-part T-SQL naming queries sibling Lakehouse SQL endpoints zero-copy, and `OPTION (FOR TIMESTAMP AS OF ...)` executes Warehouse Time Travel.
- **B:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Three-part T-SQL naming queries sibling Lakehouse SQL endpoints zero-copy, and `OPTION (FOR TIMESTAMP AS OF ...)` executes Warehouse Time Travel.
- **C:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: Three-part T-SQL naming queries sibling Lakehouse SQL endpoints zero-copy, and `OPTION (FOR TIMESTAMP AS OF ...)` executes Warehouse Time Travel.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Three-part T-SQL naming queries sibling Lakehouse SQL endpoints zero-copy, and `OPTION (FOR TIMESTAMP AS OF ...)` executes Warehouse Time Travel.
- **E:** Correct. Fabric Warehouse and SQL analytics endpoints inside the same workspace share a unified SQL engine namespace, enabling zero-copy cross-database T-SQL joins via DatabaseName.SchemaName.ObjectName. In this scenario: Three-part T-SQL naming queries sibling Lakehouse SQL endpoints zero-copy, and `OPTION (FOR TIMESTAMP AS OF ...)` executes Warehouse Time Travel.

### Question 61 — A

Answer: | summarize arg_max(IngestionTime, *) by SpecimenId. `| summarize arg_max(IngestionTime, *) by <EntityKey>` retrieves the complete newest row per substation in KQL. In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key. Local study-map skill 2.17 (Select, Filter, and Aggregate Data Using KQL (summarize, bin, arg_max, percentile, parse_json, mv-expand)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query data in a KQL queryset in Microsoft Fabric Real-Time Intelligence (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/kql-queryset).

- **A:** Correct. In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key. In this scenario: `| summarize arg_max(IngestionTime, *) by <EntityKey>` retrieves the complete newest row per substation in KQL.
- **B:** Incorrect for this requirement. percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse. Why the keyed choice wins: `| summarize arg_max(IngestionTime, *) by <EntityKey>` retrieves the complete newest row per substation in KQL.
- **C:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `| summarize arg_max(IngestionTime, *) by <EntityKey>` retrieves the complete newest row per substation in KQL.
- **D:** Incorrect for this requirement. make-series builds regular gap-filled time-series arrays (filling empty 1-minute buckets with default = 0) required for KQL anomaly detection and trend functions; summarize by bin() omits empty buckets. Why the keyed choice wins: `| summarize arg_max(IngestionTime, *) by <EntityKey>` retrieves the complete newest row per substation in KQL.

### Question 62 — B

Answer: Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results. `DAX Query View` evaluates `DEFINE MEASURE` + `EVALUATE SUMMARIZECOLUMNS` queries against desktop or web semantic models before updating the model. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Local study-map skill 2.18 (Select, Filter, and Aggregate Data Using DAX Queries (DAX Query View, EVALUATE, SUMMARIZECOLUMNS, INFO.VIEW)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Work with DAX query view & INFO.VIEW functions in Power BI (https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view).

- **A:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `DAX Query View` evaluates `DEFINE MEASURE` + `EVALUATE SUMMARIZECOLUMNS` queries against desktop or web semantic models before updating the model.
- **B:** Correct. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. In this scenario: `DAX Query View` evaluates `DEFINE MEASURE` + `EVALUATE SUMMARIZECOLUMNS` queries against desktop or web semantic models before updating the model.
- **C:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: `DAX Query View` evaluates `DEFINE MEASURE` + `EVALUATE SUMMARIZECOLUMNS` queries against desktop or web semantic models before updating the model.
- **D:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: `DAX Query View` evaluates `DEFINE MEASURE` + `EVALUATE SUMMARIZECOLUMNS` queries against desktop or web semantic models before updating the model.

### Question 63 — C

Answer: EVALUATE INFO.VIEW.MEASURES(). `EVALUATE INFO.VIEW.MEASURES()` outputs full measure metadata directly as a DAX query result. INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags. Local study-map skill 2.18 (Select, Filter, and Aggregate Data Using DAX Queries (DAX Query View, EVALUATE, SUMMARIZECOLUMNS, INFO.VIEW)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Work with DAX query view & INFO.VIEW functions in Power BI (https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view).

- **A:** Incorrect for this requirement. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. Why the keyed choice wins: `EVALUATE INFO.VIEW.MEASURES()` outputs full measure metadata directly as a DAX query result.
- **B:** Incorrect for this requirement. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Why the keyed choice wins: `EVALUATE INFO.VIEW.MEASURES()` outputs full measure metadata directly as a DAX query result.
- **C:** Correct. INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags. In this scenario: `EVALUATE INFO.VIEW.MEASURES()` outputs full measure metadata directly as a DAX query result.
- **D:** Incorrect for this requirement. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Why the keyed choice wins: `EVALUATE INFO.VIEW.MEASURES()` outputs full measure metadata directly as a DAX query result.

### Question 64 — D

Answer: Configure Direct Lake storage mode. `Direct Lake` loads OneLake Delta Parquet columns directly into memory on demand without duplicating 1.6B rows via Import refreshes. Direct Lake loads Delta Parquet columns directly from OneLake into VertiPaq memory on demand without scheduled Import data duplication or slow per-visual SQL translation. Local study-map skill 3.1 (Choose a Semantic Model Storage Mode (Import, DirectQuery, Direct Lake, and Dual)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model storage modes in the Power BI service & Microsoft Fabric (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Direct Lake` loads OneLake Delta Parquet columns directly into memory on demand without duplicating 1.6B rows via Import refreshes.
- **B:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Direct Lake` loads OneLake Delta Parquet columns directly into memory on demand without duplicating 1.6B rows via Import refreshes.
- **C:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Direct Lake` loads OneLake Delta Parquet columns directly into memory on demand without duplicating 1.6B rows via Import refreshes.
- **D:** Correct. Direct Lake loads Delta Parquet columns directly from OneLake into VertiPaq memory on demand without scheduled Import data duplication or slow per-visual SQL translation. In this scenario: `Direct Lake` loads OneLake Delta Parquet columns directly into memory on demand without duplicating 1.6B rows via Import refreshes.

### Question 65 — A

Answer: Configure shared dimension tables in Dual storage mode inside a composite model. `Dual` storage mode serves `Import` summary visuals from memory while pushing native SQL joins down for `DirectQuery` detail queries. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Local study-map skill 3.1 (Choose a Semantic Model Storage Mode (Import, DirectQuery, Direct Lake, and Dual)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model storage modes in the Power BI service & Microsoft Fabric (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode).

- **A:** Correct. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. In this scenario: `Dual` storage mode serves `Import` summary visuals from memory while pushing native SQL joins down for `DirectQuery` detail queries.
- **B:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Dual` storage mode serves `Import` summary visuals from memory while pushing native SQL joins down for `DirectQuery` detail queries.
- **C:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Dual` storage mode serves `Import` summary visuals from memory while pushing native SQL joins down for `DirectQuery` detail queries.
- **D:** Incorrect for this requirement. Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery. Why the keyed choice wins: `Dual` storage mode serves `Import` summary visuals from memory while pushing native SQL joins down for `DirectQuery` detail queries.

### Question 66 — C

Answer: Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column. Marking `DimCalendar` removes hidden `LocalDateTable_*` bloat and ensures DAX time-intelligence functions clear surrogate `DateKey` filters automatically. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. Local study-map skill 3.2 (Implement a Star Schema for a Semantic Model (Mark as Date Table, Hide Keys, Sort by Column, Display Folders)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Set and use date tables & star-schema best practices in Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Marking `DimCalendar` removes hidden `LocalDateTable_*` bloat and ensures DAX time-intelligence functions clear surrogate `DateKey` filters automatically.
- **B:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: Marking `DimCalendar` removes hidden `LocalDateTable_*` bloat and ensures DAX time-intelligence functions clear surrogate `DateKey` filters automatically.
- **C:** Correct. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. In this scenario: Marking `DimCalendar` removes hidden `LocalDateTable_*` bloat and ensures DAX time-intelligence functions clear surrogate `DateKey` filters automatically.
- **D:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Marking `DimCalendar` removes hidden `LocalDateTable_*` bloat and ensures DAX time-intelligence functions clear surrogate `DateKey` filters automatically.

### Question 67 — A, C

Answers: Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear; Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column. Hiding surrogate/raw columns with `Sort by Column` + Display Folders, combined with disabling `Auto date/time` + `Mark as date table`, enforces semantic star-schema hygiene. Local study-map skill 3.2 (Implement a Star Schema for a Semantic Model (Mark as Date Table, Hide Keys, Sort by Column, Display Folders)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Set and use date tables & star-schema best practices in Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables).

- **A:** Correct. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. In this scenario: Hiding surrogate/raw columns with `Sort by Column` + Display Folders, combined with disabling `Auto date/time` + `Mark as date table`, enforces semantic star-schema hygiene.
- **B:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Hiding surrogate/raw columns with `Sort by Column` + Display Folders, combined with disabling `Auto date/time` + `Mark as date table`, enforces semantic star-schema hygiene.
- **C:** Correct. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. In this scenario: Hiding surrogate/raw columns with `Sort by Column` + Display Folders, combined with disabling `Auto date/time` + `Mark as date table`, enforces semantic star-schema hygiene.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Hiding surrogate/raw columns with `Sort by Column` + Display Folders, combined with disabling `Auto date/time` + `Mark as date table`, enforces semantic star-schema hygiene.
- **E:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Hiding surrogate/raw columns with `Sort by Column` + Display Folders, combined with disabling `Auto date/time` + `Mark as date table`, enforces semantic star-schema hygiene.

### Question 68 — C

Answer: CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey])). `CALCULATE([Order Count], USERELATIONSHIP('Calendar'[DateKey], 'Fact...'[CompletedDateKey]))` activates the inactive relationship exclusively inside that measure. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: `CALCULATE([Order Count], USERELATIONSHIP('Calendar'[DateKey], 'Fact...'[CompletedDateKey]))` activates the inactive relationship exclusively inside that measure.
- **B:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: `CALCULATE([Order Count], USERELATIONSHIP('Calendar'[DateKey], 'Fact...'[CompletedDateKey]))` activates the inactive relationship exclusively inside that measure.
- **C:** Correct. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. In this scenario: `CALCULATE([Order Count], USERELATIONSHIP('Calendar'[DateKey], 'Fact...'[CompletedDateKey]))` activates the inactive relationship exclusively inside that measure.
- **D:** Incorrect for this requirement. CROSSFILTER(..., BOTH) enables bidirectional filter propagation across a bridge table only inside the specific measure rather than globally across the model. Why the keyed choice wins: `CALCULATE([Order Count], USERELATIONSHIP('Calendar'[DateKey], 'Fact...'[CompletedDateKey]))` activates the inactive relationship exclusively inside that measure.

### Question 69 — A

Answer: Introduce a deduplicated Bridge table between the two dimensions and scope bidirectional propagation strictly inside specific measures using CROSSFILTER(..., BOTH). Keep relationships single-directional by default and enable `CROSSFILTER(..., BOTH)` strictly inside targeted storm-attribution DAX measures. Scoping CROSSFILTER(..., BOTH) inside a DAX measure over a bridge table satisfies many-to-many attribution without turning on permanent model-wide bidirectional relationships that cause ambiguity and performance degradation. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Correct. Scoping CROSSFILTER(..., BOTH) inside a DAX measure over a bridge table satisfies many-to-many attribution without turning on permanent model-wide bidirectional relationships that cause ambiguity and performance degradation. In this scenario: Keep relationships single-directional by default and enable `CROSSFILTER(..., BOTH)` strictly inside targeted storm-attribution DAX measures.
- **B:** Incorrect for this requirement. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Why the keyed choice wins: Keep relationships single-directional by default and enable `CROSSFILTER(..., BOTH)` strictly inside targeted storm-attribution DAX measures.
- **C:** Incorrect for this requirement. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Why the keyed choice wins: Keep relationships single-directional by default and enable `CROSSFILTER(..., BOTH)` strictly inside targeted storm-attribution DAX measures.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Keep relationships single-directional by default and enable `CROSSFILTER(..., BOTH)` strictly inside targeted storm-attribution DAX measures.

### Question 70 — B

Answer: Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table. `SUMX` multiplies `MWhGenerated * LocationalMarginalPrice` at interval grain in memory before summing, capturing true price-weighted generation revenue. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Incorrect for this requirement. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. Why the keyed choice wins: `SUMX` multiplies `MWhGenerated * LocationalMarginalPrice` at interval grain in memory before summing, capturing true price-weighted generation revenue.
- **B:** Correct. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. In this scenario: `SUMX` multiplies `MWhGenerated * LocationalMarginalPrice` at interval grain in memory before summing, capturing true price-weighted generation revenue.
- **C:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: `SUMX` multiplies `MWhGenerated * LocationalMarginalPrice` at interval grain in memory before summing, capturing true price-weighted generation revenue.
- **D:** Incorrect for this requirement. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Why the keyed choice wins: `SUMX` multiplies `MWhGenerated * LocationalMarginalPrice` at interval grain in memory before summing, capturing true price-weighted generation revenue.

### Question 71 — A

Answer: Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches. Defining a DAX `VAR` evaluates the measure once in the current filter context and reuses the scalar result. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Correct. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. In this scenario: Defining a DAX `VAR` evaluates the measure once in the current filter context and reuses the scalar result.
- **B:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Defining a DAX `VAR` evaluates the measure once in the current filter context and reuses the scalar result.
- **C:** Incorrect for this requirement. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Why the keyed choice wins: Defining a DAX `VAR` evaluates the measure once in the current filter context and reuses the scalar result.
- **D:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: Defining a DAX `VAR` evaluates the measure once in the current filter context and reuses the scalar result.

### Question 72 — B

Answer: Pass simple column predicates wrapped in KEEPFILTERS(DimProduct[Color] = "Red") to CALCULATE instead of FILTER(ALL(FactSales), ...). Passing `KEEPFILTERS('FactCDR'[RadioTech] = "5G")` (or filtering a `DimRadioTech` column with `KEEPFILTERS`) pushes a compact column predicate to the Storage Engine without materializing `FactCDR`. KEEPFILTERS intersects the predicate with existing report slicer selections rather than overwriting them, and filtering a dimension column avoids scanning the entire multi-million-row fact table in the Formula Engine. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: Passing `KEEPFILTERS('FactCDR'[RadioTech] = "5G")` (or filtering a `DimRadioTech` column with `KEEPFILTERS`) pushes a compact column predicate to the Storage Engine without materializing `FactCDR`.
- **B:** Correct. KEEPFILTERS intersects the predicate with existing report slicer selections rather than overwriting them, and filtering a dimension column avoids scanning the entire multi-million-row fact table in the Formula Engine. In this scenario: Passing `KEEPFILTERS('FactCDR'[RadioTech] = "5G")` (or filtering a `DimRadioTech` column with `KEEPFILTERS`) pushes a compact column predicate to the Storage Engine without materializing `FactCDR`.
- **C:** Incorrect for this requirement. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Why the keyed choice wins: Passing `KEEPFILTERS('FactCDR'[RadioTech] = "5G")` (or filtering a `DimRadioTech` column with `KEEPFILTERS`) pushes a compact column predicate to the Storage Engine without materializing `FactCDR`.
- **D:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Passing `KEEPFILTERS('FactCDR'[RadioTech] = "5G")` (or filtering a `DimRadioTech` column with `KEEPFILTERS`) pushes a compact column predicate to the Storage Engine without materializing `FactCDR`.

### Question 73 — C, D

Answers: CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC))); IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK()). `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` steps back one custom tariff period, and `ISINSCOPE('DimGrid'[Feeder])` restricts evaluation to leaf feeder rows. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` steps back one custom tariff period, and `ISINSCOPE('DimGrid'[Feeder])` restricts evaluation to leaf feeder rows.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` steps back one custom tariff period, and `ISINSCOPE('DimGrid'[Feeder])` restricts evaluation to leaf feeder rows.
- **C:** Correct. OFFSET(-1, ..., ORDERBY(...)) shifts one period backward along a custom 4-4-5 fiscal sort column where standard Gregorian DATEADD fails. In this scenario: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` steps back one custom tariff period, and `ISINSCOPE('DimGrid'[Feeder])` restricts evaluation to leaf feeder rows.
- **D:** Correct. ISINSCOPE('DimProduct'[SKU]) evaluates TRUE only when SKU is actively grouping the visual hierarchy level, suppressing misleading margin figures at subtotal rows. In this scenario: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` steps back one custom tariff period, and `ISINSCOPE('DimGrid'[Feeder])` restricts evaluation to leaf feeder rows.
- **E:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` steps back one custom tariff period, and `ISINSCOPE('DimGrid'[Feeder])` restricts evaluation to leaf feeder rows.

### Question 74 — A

Answer: Create a Calculation Group with Calculation Items referencing SELECTEDMEASURE() and explicit Precedence ordering (automatically setting DiscourageImplicitMeasures = true). A `Calculation Group` with 4 calculation items calling `SELECTEDMEASURE()` applies all four time horizons dynamically across the 40 base measures. A single Calculation Group applies reusable logic (YTD, PY, YoY%, Moving Avg) across dozens of base measures via SELECTEDMEASURE(), eliminating measure explosion (`50 base * 6 time calcs = 300 measures`). Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Correct. A single Calculation Group applies reusable logic (YTD, PY, YoY%, Moving Avg) across dozens of base measures via SELECTEDMEASURE(), eliminating measure explosion (`50 base * 6 time calcs = 300 measures`). In this scenario: A `Calculation Group` with 4 calculation items calling `SELECTEDMEASURE()` applies all four time horizons dynamically across the 40 base measures.
- **B:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: A `Calculation Group` with 4 calculation items calling `SELECTEDMEASURE()` applies all four time horizons dynamically across the 40 base measures.
- **C:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: A `Calculation Group` with 4 calculation items calling `SELECTEDMEASURE()` applies all four time horizons dynamically across the 40 base measures.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: A `Calculation Group` with 4 calculation items calling `SELECTEDMEASURE()` applies all four time horizons dynamically across the 40 base measures.

### Question 75 — A

Answer: Configure a Dynamic Format String expression on the measure or calculation item (for example returning "\$#,0.00" vs "0.0%" via SELECTEDMEASUREFORMATSTRING()) without wrapping values in FORMAT(). `FORMAT()` converts numbers into text strings that cannot plot on continuous chart axes, whereas Dynamic Format Strings preserve underlying numeric types. Unlike FORMAT() — which converts numbers into text strings and breaks chart axes/sorting/aggregations — Dynamic Format Strings preserve true numeric data types while rendering context-aware currency or percentage formatting. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Correct. Unlike FORMAT() — which converts numbers into text strings and breaks chart axes/sorting/aggregations — Dynamic Format Strings preserve true numeric data types while rendering context-aware currency or percentage formatting. In this scenario: `FORMAT()` converts numbers into text strings that cannot plot on continuous chart axes, whereas Dynamic Format Strings preserve underlying numeric types.
- **B:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: `FORMAT()` converts numbers into text strings that cannot plot on continuous chart axes, whereas Dynamic Format Strings preserve underlying numeric types.
- **C:** Incorrect for this requirement. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Why the keyed choice wins: `FORMAT()` converts numbers into text strings that cannot plot on continuous chart axes, whereas Dynamic Format Strings preserve underlying numeric types.
- **D:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: `FORMAT()` converts numbers into text strings that cannot plot on continuous chart axes, whereas Dynamic Format Strings preserve underlying numeric types.

### Question 76 — D

Answer: NAMEOF('DimTrade'[CurrencyPair]). `NAMEOF('Table'[Column])` binds the Field Parameter entry to the semantic-model object reference safely. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Why the keyed choice wins: `NAMEOF('Table'[Column])` binds the Field Parameter entry to the semantic-model object reference safely.
- **B:** Incorrect for this requirement. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. Why the keyed choice wins: `NAMEOF('Table'[Column])` binds the Field Parameter entry to the semantic-model object reference safely.
- **C:** Incorrect for this requirement. INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags. Why the keyed choice wins: `NAMEOF('Table'[Column])` binds the Field Parameter entry to the semantic-model object reference safely.
- **D:** Correct. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. In this scenario: `NAMEOF('Table'[Column])` binds the Field Parameter entry to the semantic-model object reference safely.

### Question 77 — D

Answer: Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat). Enabling `Large semantic model storage format` expands max model size up to the capacity SKU limit and optimizes XMLA segment writes. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Local study-map skill 3.6 (Identify Use Cases for and Configure Large Semantic Model Storage Format), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Large semantic models in Microsoft Fabric & Power BI Premium (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-large-models).

- **A:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Enabling `Large semantic model storage format` expands max model size up to the capacity SKU limit and optimizes XMLA segment writes.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Enabling `Large semantic model storage format` expands max model size up to the capacity SKU limit and optimizes XMLA segment writes.
- **C:** Incorrect for this requirement. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Why the keyed choice wins: Enabling `Large semantic model storage format` expands max model size up to the capacity SKU limit and optimizes XMLA segment writes.
- **D:** Correct. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. In this scenario: Enabling `Large semantic model storage format` expands max model size up to the capacity SKU limit and optimizes XMLA segment writes.

### Question 78 — B

Answer: Enable Detect data changes on an immutable LastModifiedUTC audit column (different from the partitioned OrderDate column) and optionally enable Get the latest data in real time with DirectQuery. Enabling `Detect data changes` on `LastValidatedUTC` (distinct from `ReadDate`) refreshes only modified historical partitions, and `Get the latest data in real time with DirectQuery` adds a hybrid real-time trailing partition. Detect data changes refreshes only historical archive partitions whose MAX(LastModifiedUTC) changed, while the hybrid real-time option adds a trailing DirectQuery partition for today's intra-day rows. Local study-map skill 3.6 (Identify Use Cases for and Configure Large Semantic Model Storage Format), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Large semantic models in Microsoft Fabric & Power BI Premium (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-large-models).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Enabling `Detect data changes` on `LastValidatedUTC` (distinct from `ReadDate`) refreshes only modified historical partitions, and `Get the latest data in real time with DirectQuery` adds a hybrid real-time trailing partition.
- **B:** Correct. Detect data changes refreshes only historical archive partitions whose MAX(LastModifiedUTC) changed, while the hybrid real-time option adds a trailing DirectQuery partition for today's intra-day rows. In this scenario: Enabling `Detect data changes` on `LastValidatedUTC` (distinct from `ReadDate`) refreshes only modified historical partitions, and `Get the latest data in real time with DirectQuery` adds a hybrid real-time trailing partition.
- **C:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Enabling `Detect data changes` on `LastValidatedUTC` (distinct from `ReadDate`) refreshes only modified historical partitions, and `Get the latest data in real time with DirectQuery` adds a hybrid real-time trailing partition.
- **D:** Incorrect for this requirement. Using >= AND <= on both ends causes rows stamped exactly at midnight on partition boundaries to load into two adjacent partitions, silently double-counting sales totals. Why the keyed choice wins: Enabling `Detect data changes` on `LastValidatedUTC` (distinct from `ReadDate`) refreshes only modified historical partitions, and `Get the latest data in real time with DirectQuery` adds a hybrid real-time trailing partition.

### Question 79 — B

Answer: Build a Direct Lake on OneLake composite semantic model combining Direct Lake fact tables from OneLake with Import dimension/target tables using regular relationships. A `Direct Lake on OneLake` composite semantic model mixes Direct Lake tables across multiple Fabric items with `Import` tables using regular `1:*` relationships. Direct Lake on OneLake supports true composite models that mix Direct Lake tables from multiple Fabric items with Import tables from any Power Query connector while preserving fast regular (non-limited) relationships. Local study-map skill 3.7 (Design and Build Composite Models (Direct Lake on OneLake + Import, Dual + Aggregations, DirectQuery over PBI)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use composite models in Power BI Desktop & Direct Lake on OneLake composite models (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-web-modeling).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: A `Direct Lake on OneLake` composite semantic model mixes Direct Lake tables across multiple Fabric items with `Import` tables using regular `1:*` relationships.
- **B:** Correct. Direct Lake on OneLake supports true composite models that mix Direct Lake tables from multiple Fabric items with Import tables from any Power Query connector while preserving fast regular (non-limited) relationships. In this scenario: A `Direct Lake on OneLake` composite semantic model mixes Direct Lake tables across multiple Fabric items with `Import` tables using regular `1:*` relationships.
- **C:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: A `Direct Lake on OneLake` composite semantic model mixes Direct Lake tables across multiple Fabric items with `Import` tables using regular `1:*` relationships.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: A `Direct Lake on OneLake` composite semantic model mixes Direct Lake tables across multiple Fabric items with `Import` tables using regular `1:*` relationships.

### Question 80 — C, E

Answers: Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table; Create a local composite model using DirectQuery for Power BI semantic models and Analysis Services to combine a certified core semantic model with a departmental Excel/SQL table. User-defined `Import` aggregations (`Manage aggregations`) serve grouped queries from RAM, and `DirectQuery for Power BI semantic models` builds a local composite extension over `RegionalTransit`. Local study-map skill 3.7 (Design and Build Composite Models (Direct Lake on OneLake + Import, Dual + Aggregations, DirectQuery over PBI)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use composite models in Power BI Desktop & Direct Lake on OneLake composite models (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-web-modeling).

- **A:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: User-defined `Import` aggregations (`Manage aggregations`) serve grouped queries from RAM, and `DirectQuery for Power BI semantic models` builds a local composite extension over `RegionalTransit`.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: User-defined `Import` aggregations (`Manage aggregations`) serve grouped queries from RAM, and `DirectQuery for Power BI semantic models` builds a local composite extension over `RegionalTransit`.
- **C:** Correct. User-defined Import aggregations satisfy high-level grouped queries purely from in-memory VertiPaq cache and automatically route only unaggregated detail drill-throughs to the underlying DirectQuery source. In this scenario: User-defined `Import` aggregations (`Manage aggregations`) serve grouped queries from RAM, and `DirectQuery for Power BI semantic models` builds a local composite extension over `RegionalTransit`.
- **D:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: User-defined `Import` aggregations (`Manage aggregations`) serve grouped queries from RAM, and `DirectQuery for Power BI semantic models` builds a local composite extension over `RegionalTransit`.
- **E:** Correct. Connecting to an existing shared semantic model in DirectQuery mode creates a local composite model (using remote model chains and limited cross-island relationships) so analysts can extend governed enterprise measures without copying the core model. In this scenario: User-defined `Import` aggregations (`Manage aggregations`) serve grouped queries from RAM, and `DirectQuery for Power BI semantic models` builds a local composite extension over `RegionalTransit`.

### Question 81 — C

Answer: Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time. `Performance Analyzer` isolates `DAX query`, `Visual display`, and `Other` queue durations, confirming 44 separate visuals bottleneck single-threaded container queuing. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Local study-map skill 3.8 (Implement Performance Improvements in Queries and Report Visuals (Performance Analyzer & Query Reduction)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use Performance Analyzer to examine report element performance in Power BI (https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer).

- **A:** Incorrect for this requirement. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Why the keyed choice wins: `Performance Analyzer` isolates `DAX query`, `Visual display`, and `Other` queue durations, confirming 44 separate visuals bottleneck single-threaded container queuing.
- **B:** Incorrect for this requirement. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. Why the keyed choice wins: `Performance Analyzer` isolates `DAX query`, `Visual display`, and `Other` queue durations, confirming 44 separate visuals bottleneck single-threaded container queuing.
- **C:** Correct. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. In this scenario: `Performance Analyzer` isolates `DAX query`, `Visual display`, and `Other` queue durations, confirming 44 separate visuals bottleneck single-threaded container queuing.
- **D:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: `Performance Analyzer` isolates `DAX query`, `Visual display`, and `Other` queue durations, confirming 44 separate visuals bottleneck single-threaded container queuing.

### Question 82 — D

Answer: Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages. Enabling `Add an Apply button to each single/multi-select slicer` under `Query reduction` sends one batched query when `Apply` is pressed. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Local study-map skill 3.8 (Implement Performance Improvements in Queries and Report Visuals (Performance Analyzer & Query Reduction)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use Performance Analyzer to examine report element performance in Power BI (https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer).

- **A:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Enabling `Add an Apply button to each single/multi-select slicer` under `Query reduction` sends one batched query when `Apply` is pressed.
- **B:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Enabling `Add an Apply button to each single/multi-select slicer` under `Query reduction` sends one batched query when `Apply` is pressed.
- **C:** Incorrect for this requirement. Hundreds of tiny streaming Parquet files inflate Delta rowgroup counts past Fabric SKU guardrails and degrade transcoding; OPTIMIZE compacts files into large V-Order-sorted rowgroups optimized for VertiPaq in-memory compression. Why the keyed choice wins: Enabling `Add an Apply button to each single/multi-select slicer` under `Query reduction` sends one batched query when `Apply` is pressed.
- **D:** Correct. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. In this scenario: Enabling `Add an Apply button to each single/multi-select slicer` under `Query reduction` sends one batched query when `Apply` is pressed.

### Question 83 — A

Answer: Profile the slow measure in DAX Studio using Server Timings to inspect Formula Engine (FE) vs Storage Engine (SE) CPU, SE query count, and CallbackDataID warnings. `CallbackDataID` indicates unpushed complex logic inside the iterator forcing row-by-row Formula Engine callbacks; pushing simple column filters to the Storage Engine and pre-computing/caching scalars in `VAR` eliminates it. DAX Studio Server Timings reveals whether slow execution comes from hundreds of chatty SE scans, CallbackDataID forcing row-by-row FE callbacks inside SE scans, or unpushed complex predicates. Local study-map skill 3.9 (Improve DAX and Model Performance Using DAX Studio Server Timings (FE vs SE) and VertiPaq Cardinality Reduction), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Optimization guide for Power BI — DAX Formula Engine vs Storage Engine & VertiPaq (https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization).

- **A:** Correct. DAX Studio Server Timings reveals whether slow execution comes from hundreds of chatty SE scans, CallbackDataID forcing row-by-row FE callbacks inside SE scans, or unpushed complex predicates. In this scenario: `CallbackDataID` indicates unpushed complex logic inside the iterator forcing row-by-row Formula Engine callbacks; pushing simple column filters to the Storage Engine and pre-computing/caching scalars in `VAR` eliminates it.
- **B:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `CallbackDataID` indicates unpushed complex logic inside the iterator forcing row-by-row Formula Engine callbacks; pushing simple column filters to the Storage Engine and pre-computing/caching scalars in `VAR` eliminates it.
- **C:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: `CallbackDataID` indicates unpushed complex logic inside the iterator forcing row-by-row Formula Engine callbacks; pushing simple column filters to the Storage Engine and pre-computing/caching scalars in `VAR` eliminates it.
- **D:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: `CallbackDataID` indicates unpushed complex logic inside the iterator forcing row-by-row Formula Engine callbacks; pushing simple column filters to the Storage Engine and pre-computing/caching scalars in `VAR` eliminates it.

### Question 84 — A

Answer: Capture visual timings in Performance Analyzer → Profile captured DAX in DAX Studio with Server Timings and Query Plan → Refactor FILTER(Fact,...) into VAR-cached SE column predicates and run V-Order OPTIMIZE → Re-test with Clear Cache. Capturing visual DAX in Performance Analyzer, profiling FE/SE + fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing with `Clear Cache` confirms cold-cache gains. Correct order: isolate visual vs DAX queue time in Performance Analyzer, profile FE/SE and Direct Lake fallback in DAX Studio Server Timings, fix DAX anti-patterns + Delta Parquet layout, and benchmark cold-cache results. Local study-map skill 3.9 (Improve DAX and Model Performance Using DAX Studio Server Timings (FE vs SE) and VertiPaq Cardinality Reduction), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Optimization guide for Power BI — DAX Formula Engine vs Storage Engine & VertiPaq (https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization).

- **A:** Correct. Correct order: isolate visual vs DAX queue time in Performance Analyzer, profile FE/SE and Direct Lake fallback in DAX Studio Server Timings, fix DAX anti-patterns + Delta Parquet layout, and benchmark cold-cache results. In this scenario: Capturing visual DAX in Performance Analyzer, profiling FE/SE + fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing with `Clear Cache` confirms cold-cache gains.
- **B:** Incorrect for this requirement. Incorrect: snowflaking and Auto date/time increase relationship hops and memory overhead rather than resolving FE/SE bottlenecks. Why the keyed choice wins: Capturing visual DAX in Performance Analyzer, profiling FE/SE + fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing with `Clear Cache` confirms cold-cache gains.
- **C:** Incorrect for this requirement. Incorrect: scaling capacity blindly wastes budget while bidirectional joins, FORMAT() strings, and disabled V-Order make FE and transcoding slower. Why the keyed choice wins: Capturing visual DAX in Performance Analyzer, profiling FE/SE + fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing with `Clear Cache` confirms cold-cache gains.
- **D:** Incorrect for this requirement. Incorrect: benchmarking warm cache hides real SE/transcoding cost, GUID columns bloat dictionaries, DirectQueryOnly slows visuals, and 45 cards create visual-queue contention. Why the keyed choice wins: Capturing visual DAX in Performance Analyzer, profiling FE/SE + fallback in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing with `Clear Cache` confirms cold-cache gains.

### Question 85 — A

Answer: directLakeBehavior: directLakeOnly. `directLakeBehavior: directLakeOnly` disables DirectQuery fallback on Direct Lake on SQL models. Setting directLakeBehavior: directLakeOnly in TMDL prevents a Direct Lake on SQL model from silently falling back to DirectQuery. Local study-map skill 3.10 (Configure Direct Lake Framing, Transcoding, V-Order/OPTIMIZE Guardrails, and DirectLakeBehavior Fallback), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: How Direct Lake works (framing, transcoding, V-Order, fallback & DirectLakeBehavior) (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works).

- **A:** Correct. Setting directLakeBehavior: directLakeOnly in TMDL prevents a Direct Lake on SQL model from silently falling back to DirectQuery. In this scenario: `directLakeBehavior: directLakeOnly` disables DirectQuery fallback on Direct Lake on SQL models.
- **B:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: `directLakeBehavior: directLakeOnly` disables DirectQuery fallback on Direct Lake on SQL models.
- **C:** Incorrect for this requirement. Direct Lake on OneLake operates exclusively in DirectLakeOnly mode and never falls back to DirectQuery; exceeding capacity guardrails fails framing/queries until Delta tables or SKU sizing are optimized. Why the keyed choice wins: `directLakeBehavior: directLakeOnly` disables DirectQuery fallback on Direct Lake on SQL models.
- **D:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `directLakeBehavior: directLakeOnly` disables DirectQuery fallback on Direct Lake on SQL models.

### Question 86 — B, C, D

Answers: Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails; Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes; Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time. Running `OPTIMIZE` with `V-Order` to bin-pack small Parquet files, dropping unused high-cardinality GUID/hex columns, and triggering explicit post-ETL `framing` refreshes maintain peak Direct Lake health. Local study-map skill 3.10 (Configure Direct Lake Framing, Transcoding, V-Order/OPTIMIZE Guardrails, and DirectLakeBehavior Fallback), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: How Direct Lake works (framing, transcoding, V-Order, fallback & DirectLakeBehavior) (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Running `OPTIMIZE` with `V-Order` to bin-pack small Parquet files, dropping unused high-cardinality GUID/hex columns, and triggering explicit post-ETL `framing` refreshes maintain peak Direct Lake health.
- **B:** Correct. Columnar memory in VertiPaq and Direct Lake transcoding scales primarily with column cardinality rather than row count; dropping unused GUIDs or splitting millisecond timestamps into separate Date and Time columns cuts memory dramatically. In this scenario: Running `OPTIMIZE` with `V-Order` to bin-pack small Parquet files, dropping unused high-cardinality GUID/hex columns, and triggering explicit post-ETL `framing` refreshes maintain peak Direct Lake health.
- **C:** Correct. Framing is a fast metadata-only operation updating the Direct Lake model's pointer to the latest Delta transaction log Parquet files and evicting stale resident columns so new ETL rows become visible consistently. In this scenario: Running `OPTIMIZE` with `V-Order` to bin-pack small Parquet files, dropping unused high-cardinality GUID/hex columns, and triggering explicit post-ETL `framing` refreshes maintain peak Direct Lake health.
- **D:** Correct. Hundreds of tiny streaming Parquet files inflate Delta rowgroup counts past Fabric SKU guardrails and degrade transcoding; OPTIMIZE compacts files into large V-Order-sorted rowgroups optimized for VertiPaq in-memory compression. In this scenario: Running `OPTIMIZE` with `V-Order` to bin-pack small Parquet files, dropping unused high-cardinality GUID/hex columns, and triggering explicit post-ETL `framing` refreshes maintain peak Direct Lake health.
- **E:** Incorrect for this requirement. Direct Lake on OneLake operates exclusively in DirectLakeOnly mode and never falls back to DirectQuery; exceeding capacity guardrails fails framing/queries until Delta tables or SKU sizing are optimized. Why the keyed choice wins: Running `OPTIMIZE` with `V-Order` to bin-pack small Parquet files, dropping unused high-cardinality GUID/hex columns, and triggering explicit post-ETL `framing` refreshes maintain peak Direct Lake health.
- **F:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Running `OPTIMIZE` with `V-Order` to bin-pack small Parquet files, dropping unused high-cardinality GUID/hex columns, and triggering explicit post-ETL `framing` refreshes maintain peak Direct Lake health.

### Question 87 — B

Answer: Live edit the model in Power BI Desktop and save a Version history point → Script the semantic model in TMDL view → Replace Sql.Database(...) with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...") → Apply TMDL and run framing refresh. Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the migration. Correct order: take a version history checkpoint while live editing, script the model in TMDL view, swap the shared M expression from Sql.Database to AzureStorage.DataLake OneLake URL, apply changes, and frame. Local study-map skill 3.11 (Choose Between Direct Lake on OneLake and Direct Lake on SQL Analytics Endpoint (and Migrate via TMDL)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Direct Lake overview: Direct Lake on OneLake vs Direct Lake on SQL analytics endpoint (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview).

- **A:** Incorrect for this requirement. Incorrect: deleting the semantic model breaks downstream thin reports and lineage, and granting Workspace Admin violates security. Why the keyed choice wins: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the migration.
- **B:** Correct. Correct order: take a version history checkpoint while live editing, script the model in TMDL view, swap the shared M expression from Sql.Database to AzureStorage.DataLake OneLake URL, apply changes, and frame. In this scenario: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the migration.
- **C:** Incorrect for this requirement. Incorrect: Direct Lake on OneLake does not support non-materialized SQL views, DirectQuery fallback, or gateways. Why the keyed choice wins: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the migration.
- **D:** Incorrect for this requirement. Incorrect: Direct Lake models are live-edited in workspaces (not offline Personal Workspace Import files), and OleDb breaks OneLake Direct Lake connectivity. Why the keyed choice wins: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the migration.

### Question 88 — C

Answer: Create case-sensitive DateTime parameters RangeStart and RangeEnd → Apply foldable half-open filter (>= RangeStart and < RangeEnd) → Configure table Incremental refresh policy → Publish to workspace and run initial refresh to generate partitions. Defining case-sensitive `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the table's incremental policy, and publishing for initial partition creation implements it cleanly. Correct order: define DateTime RangeStart/RangeEnd parameters, apply >= RangeStart and < RangeEnd preserving query folding, configure table incremental policy, and publish so Fabric generates historical and incremental partitions. Local study-map skill 3.12 (Implement Incremental Refresh and Hybrid Real-Time Partitions (RangeStart/RangeEnd, Detect Data Changes)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Configure incremental refresh and real-time data for Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-overview).

- **A:** Incorrect for this requirement. Incorrect: Detect data changes requires an audit/update timestamp column distinct from the date column used to partition RangeStart/RangeEnd. Why the keyed choice wins: Defining case-sensitive `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the table's incremental policy, and publishing for initial partition creation implements it cleanly.
- **B:** Incorrect for this requirement. Incorrect: importing 2 billion rows locally crashes Desktop before partitioning exists, RangeStart belongs in Power Query M, and Incremental Refresh partitions apply to Import/Hybrid tables rather than Direct Lake. Why the keyed choice wins: Defining case-sensitive `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the table's incremental policy, and publishing for initial partition creation implements it cleanly.
- **C:** Correct. Correct order: define DateTime RangeStart/RangeEnd parameters, apply >= RangeStart and < RangeEnd preserving query folding, configure table incremental policy, and publish so Fabric generates historical and incremental partitions. In this scenario: Defining case-sensitive `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the table's incremental policy, and publishing for initial partition creation implements it cleanly.
- **D:** Incorrect for this requirement. Incorrect: parameter names/types must be exact DateTime RangeStart and RangeEnd, breaking query folding pulls the entire table on every refresh, and <= on both bounds double-counts midnight rows. Why the keyed choice wins: Defining case-sensitive `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the table's incremental policy, and publishing for initial partition creation implements it cleanly.

### Question 89 — A

Answer: AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/" & WorkspaceId & "/" & LakehouseId). `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/" & WorkspaceId & "/" & LakehouseId)` binds Direct Lake partitions directly to OneLake APIs, enabling multi-item sources and zero DirectQuery fallback. Direct Lake on OneLake partitions bind to a shared M expression calling AzureStorage.DataLake against the https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<itemId> endpoint. Local study-map skill 3.11 (Choose Between Direct Lake on OneLake and Direct Lake on SQL Analytics Endpoint (and Migrate via TMDL)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Direct Lake overview: Direct Lake on OneLake vs Direct Lake on SQL analytics endpoint (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview).

- **A:** Correct. Direct Lake on OneLake partitions bind to a shared M expression calling AzureStorage.DataLake against the https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<itemId> endpoint. In this scenario: `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/" & WorkspaceId & "/" & LakehouseId)` binds Direct Lake partitions directly to OneLake APIs, enabling multi-item sources and zero DirectQuery fallback.
- **B:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/" & WorkspaceId & "/" & LakehouseId)` binds Direct Lake partitions directly to OneLake APIs, enabling multi-item sources and zero DirectQuery fallback.
- **C:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/" & WorkspaceId & "/" & LakehouseId)` binds Direct Lake partitions directly to OneLake APIs, enabling multi-item sources and zero DirectQuery fallback.
- **D:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/" & WorkspaceId & "/" & LakehouseId)` binds Direct Lake partitions directly to OneLake APIs, enabling multi-item sources and zero DirectQuery fallback.

### Question 90 — D

Answer: Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake. Direct Lake does not support `Binary`, `GUID`, or complex nested columns; converting needed hashes to `VARCHAR`/`STRING` (or omitting unreferenced binary hashes) resolves table compatibility. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. Local study-map skill 2.13 (Convert Column Data Types Safely (TRY_CAST, Fixed Decimal, and Direct Lake Supported Primitive Types)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data types in Fabric Data Warehouse and Direct Lake Delta tables (https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types).

- **A:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Direct Lake does not support `Binary`, `GUID`, or complex nested columns; converting needed hashes to `VARCHAR`/`STRING` (or omitting unreferenced binary hashes) resolves table compatibility.
- **B:** Incorrect for this requirement. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Why the keyed choice wins: Direct Lake does not support `Binary`, `GUID`, or complex nested columns; converting needed hashes to `VARCHAR`/`STRING` (or omitting unreferenced binary hashes) resolves table compatibility.
- **C:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Direct Lake does not support `Binary`, `GUID`, or complex nested columns; converting needed hashes to `VARCHAR`/`STRING` (or omitting unreferenced binary hashes) resolves table compatibility.
- **D:** Correct. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. In this scenario: Direct Lake does not support `Binary`, `GUID`, or complex nested columns; converting needed hashes to `VARCHAR`/`STRING` (or omitting unreferenced binary hashes) resolves table compatibility.

### Question 91 — C

Answer: Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid. Checking `Assume referential integrity` instructs Power BI to emit faster `INNER JOIN` queries against the Warehouse. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Checking `Assume referential integrity` instructs Power BI to emit faster `INNER JOIN` queries against the Warehouse.
- **B:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Checking `Assume referential integrity` instructs Power BI to emit faster `INNER JOIN` queries against the Warehouse.
- **C:** Correct. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. In this scenario: Checking `Assume referential integrity` instructs Power BI to emit faster `INNER JOIN` queries against the Warehouse.
- **D:** Incorrect for this requirement. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Why the keyed choice wins: Checking `Assume referential integrity` instructs Power BI to emit faster `INNER JOIN` queries against the Warehouse.

### Question 92 — A

Answer: CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales. `CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales` (`CREATE TABLE ... AS CLONE OF`) creates a zero-copy metadata clone instantaneously in Fabric Data Warehouse. CREATE TABLE ... AS CLONE OF creates a zero-copy metadata clone of a Fabric Warehouse table instantaneously (optionally AT a specific UTC timestamp) without duplicating Parquet files. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Correct. CREATE TABLE ... AS CLONE OF creates a zero-copy metadata clone of a Fabric Warehouse table instantaneously (optionally AT a specific UTC timestamp) without duplicating Parquet files. In this scenario: `CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales` (`CREATE TABLE ... AS CLONE OF`) creates a zero-copy metadata clone instantaneously in Fabric Data Warehouse.
- **B:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: `CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales` (`CREATE TABLE ... AS CLONE OF`) creates a zero-copy metadata clone instantaneously in Fabric Data Warehouse.
- **C:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: `CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales` (`CREATE TABLE ... AS CLONE OF`) creates a zero-copy metadata clone instantaneously in Fabric Data Warehouse.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales` (`CREATE TABLE ... AS CLONE OF`) creates a zero-copy metadata clone instantaneously in Fabric Data Warehouse.

### Question 93 — B

Answer: Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic. Creating a parameterized T-SQL stored procedure (`CREATE PROCEDURE`) in `TransitWarehouse` invoked by a pipeline `Stored procedure` activity runs multi-table ACID ELT cleanly. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Creating a parameterized T-SQL stored procedure (`CREATE PROCEDURE`) in `TransitWarehouse` invoked by a pipeline `Stored procedure` activity runs multi-table ACID ELT cleanly.
- **B:** Correct. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. In this scenario: Creating a parameterized T-SQL stored procedure (`CREATE PROCEDURE`) in `TransitWarehouse` invoked by a pipeline `Stored procedure` activity runs multi-table ACID ELT cleanly.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Creating a parameterized T-SQL stored procedure (`CREATE PROCEDURE`) in `TransitWarehouse` invoked by a pipeline `Stored procedure` activity runs multi-table ACID ELT cleanly.
- **D:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Creating a parameterized T-SQL stored procedure (`CREATE PROCEDURE`) in `TransitWarehouse` invoked by a pipeline `Stored procedure` activity runs multi-table ACID ELT cleanly.

### Question 94 — A

Answer: GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ()). `GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())` computes exact multi-level subtotals and grand total in a single table scan without `UNION ALL`. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Correct. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. In this scenario: `GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())` computes exact multi-level subtotals and grand total in a single table scan without `UNION ALL`.
- **B:** Incorrect for this requirement. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Why the keyed choice wins: `GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())` computes exact multi-level subtotals and grand total in a single table scan without `UNION ALL`.
- **C:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())` computes exact multi-level subtotals and grand total in a single table scan without `UNION ALL`.
- **D:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())` computes exact multi-level subtotals and grand total in a single table scan without `UNION ALL`.

### Question 95 — B

Answer: | mv-expand PhaseReading = parse_json(Payload).PhaseReadings. `| mv-expand PhaseReading = parse_json(Payload).PhaseReadings` unpacks the nested JSON array into individual rows before KQL aggregation. mv-expand unpacks a dynamic JSON array into one output row per array element while preserving parent event columns. Local study-map skill 2.17 (Select, Filter, and Aggregate Data Using KQL (summarize, bin, arg_max, percentile, parse_json, mv-expand)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query data in a KQL queryset in Microsoft Fabric Real-Time Intelligence (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/kql-queryset).

- **A:** Incorrect for this requirement. percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse. Why the keyed choice wins: `| mv-expand PhaseReading = parse_json(Payload).PhaseReadings` unpacks the nested JSON array into individual rows before KQL aggregation.
- **B:** Correct. mv-expand unpacks a dynamic JSON array into one output row per array element while preserving parent event columns. In this scenario: `| mv-expand PhaseReading = parse_json(Payload).PhaseReadings` unpacks the nested JSON array into individual rows before KQL aggregation.
- **C:** Incorrect for this requirement. make-series builds regular gap-filled time-series arrays (filling empty 1-minute buckets with default = 0) required for KQL anomaly detection and trend functions; summarize by bin() omits empty buckets. Why the keyed choice wins: `| mv-expand PhaseReading = parse_json(Payload).PhaseReadings` unpacks the nested JSON array into individual rows before KQL aggregation.
- **D:** Incorrect for this requirement. In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key. Why the keyed choice wins: `| mv-expand PhaseReading = parse_json(Payload).PhaseReadings` unpacks the nested JSON array into individual rows before KQL aggregation.

### Question 96 — B

Answer: LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC). `LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)` fetches the prior hour's output per substation in one window scan. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)` fetches the prior hour's output per substation in one window scan.
- **B:** Correct. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. In this scenario: `LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)` fetches the prior hour's output per substation in one window scan.
- **C:** Incorrect for this requirement. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Why the keyed choice wins: `LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)` fetches the prior hour's output per substation in one window scan.
- **D:** Incorrect for this requirement. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Why the keyed choice wins: `LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)` fetches the prior hour's output per substation in one window scan.

### Question 97 — C

Answer: Filter on physical Delta partition or liquid-clustered date columns using sargable range predicates (OrderDate >= '2026-01-01') without wrapping the column in functions. Sargable range predicates on the raw `ReadingDate` column preserve Delta partition pruning and Parquet rowgroup min/max file skipping. Wrapping a column in YEAR(OrderDate) = 2026 blocks file-level min/max data skipping and partition pruning; sargable range predicates let Spark and SQL endpoints skip irrelevant Parquet files entirely. Local study-map skill 2.14 (Filter Data Early Preserving Power Query Folding (View Native Query) and Sargable Delta File Pruning), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query folding indicators & predicate pushdown in Power Query and Delta Lake (https://learn.microsoft.com/en-us/power-query/query-folding-basics).

- **A:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: Sargable range predicates on the raw `ReadingDate` column preserve Delta partition pruning and Parquet rowgroup min/max file skipping.
- **B:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: Sargable range predicates on the raw `ReadingDate` column preserve Delta partition pruning and Parquet rowgroup min/max file skipping.
- **C:** Correct. Wrapping a column in YEAR(OrderDate) = 2026 blocks file-level min/max data skipping and partition pruning; sargable range predicates let Spark and SQL endpoints skip irrelevant Parquet files entirely. In this scenario: Sargable range predicates on the raw `ReadingDate` column preserve Delta partition pruning and Parquet rowgroup min/max file skipping.
- **D:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: Sargable range predicates on the raw `ReadingDate` column preserve Delta partition pruning and Parquet rowgroup min/max file skipping.

### Question 98 — B

Answer: Bind the Direct Lake semantic model to a cloud connection with a fixed identity and disable SSO. Binding the Direct Lake model to a Shareable cloud connection with a fixed identity (Service Principal or Workspace Identity) and SSO disabled lets the model read OneLake while isolating store leads from the Lakehouse. Configuring a fixed-identity cloud connection (Service Principal or Workspace Identity) with SSO disabled lets report consumers query the Direct Lake model enforced by semantic-model RLS without granting them any direct Lakehouse or SQL endpoint permissions. Local study-map skill 1.2 (Implement Item-Level Access Controls (Read, ReadData, ReadAll, Build, SSO vs Fixed Identity)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Share items in Microsoft Fabric & Semantic model Build permission (https://learn.microsoft.com/en-us/fabric/fundamentals/share-items).

- **A:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: Binding the Direct Lake model to a Shareable cloud connection with a fixed identity (Service Principal or Workspace Identity) and SSO disabled lets the model read OneLake while isolating store leads from the Lakehouse.
- **B:** Correct. Configuring a fixed-identity cloud connection (Service Principal or Workspace Identity) with SSO disabled lets report consumers query the Direct Lake model enforced by semantic-model RLS without granting them any direct Lakehouse or SQL endpoint permissions. In this scenario: Binding the Direct Lake model to a Shareable cloud connection with a fixed identity (Service Principal or Workspace Identity) and SSO disabled lets the model read OneLake while isolating store leads from the Lakehouse.
- **C:** Incorrect for this requirement. ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled. Why the keyed choice wins: Binding the Direct Lake model to a Shareable cloud connection with a fixed identity (Service Principal or Workspace Identity) and SSO disabled lets the model read OneLake while isolating store leads from the Lakehouse.
- **D:** Incorrect for this requirement. With SSO enabled on a Direct Lake model, Fabric evaluates data permissions at the underlying SQL analytics endpoint or OneLake security layer using each viewing report consumer's own Microsoft Entra identity. Why the keyed choice wins: Binding the Direct Lake model to a Shareable cloud connection with a fixed identity (Service Principal or Workspace Identity) and SSO disabled lets the model read OneLake while isolating store leads from the Lakehouse.

### Question 99 — B

Answer: [ManagerEmail] = USERPRINCIPALNAME(). `[ManagerEmail] = USERPRINCIPALNAME()` returns the viewing store lead's Entra UPN (`lead@telcobeam.com`) consistently in the Fabric portal. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: `[ManagerEmail] = USERPRINCIPALNAME()` returns the viewing store lead's Entra UPN (`lead@telcobeam.com`) consistently in the Fabric portal.
- **B:** Correct. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. In this scenario: `[ManagerEmail] = USERPRINCIPALNAME()` returns the viewing store lead's Entra UPN (`lead@telcobeam.com`) consistently in the Fabric portal.
- **C:** Incorrect for this requirement. In Power BI Desktop USERNAME() returns DOMAIN\user whereas in the Fabric service it returns the UPN; USERPRINCIPALNAME() consistently returns user@domain.com across cloud evaluations. Why the keyed choice wins: `[ManagerEmail] = USERPRINCIPALNAME()` returns the viewing store lead's Entra UPN (`lead@telcobeam.com`) consistently in the Fabric portal.
- **D:** Incorrect for this requirement. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Why the keyed choice wins: `[ManagerEmail] = USERPRINCIPALNAME()` returns the viewing store lead's Entra UPN (`lead@telcobeam.com`) consistently in the Fabric portal.

### Question 100 — B

Answer: Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN. Using `Test as role` (`View as`) in the Fabric service while entering `lead42@telcobeam.com` tests both the RLS filter and whether `lead42` accidentally holds RLS-bypassing workspace permissions. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: Using `Test as role` (`View as`) in the Fabric service while entering `lead42@telcobeam.com` tests both the RLS filter and whether `lead42` accidentally holds RLS-bypassing workspace permissions.
- **B:** Correct. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). In this scenario: Using `Test as role` (`View as`) in the Fabric service while entering `lead42@telcobeam.com` tests both the RLS filter and whether `lead42` accidentally holds RLS-bypassing workspace permissions.
- **C:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Using `Test as role` (`View as`) in the Fabric service while entering `lead42@telcobeam.com` tests both the RLS filter and whether `lead42` accidentally holds RLS-bypassing workspace permissions.
- **D:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: Using `Test as role` (`View as`) in the Fabric service while entering `lead42@telcobeam.com` tests both the RLS filter and whether `lead42` accidentally holds RLS-bypassing workspace permissions.
