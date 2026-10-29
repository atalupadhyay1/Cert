# Microsoft Exam DP-600: Implementing Analytics Solutions Using Microsoft Fabric — Full-Length Mock Exam 5

Exam DP-600 (Subscription Media Streaming, Ad-Tech Attribution, and Multi-Source Direct Lake) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint & Credential Notice:** Aligned to the official **October 19, 2026** DP-600 study guide (`Microsoft Certified: Fabric Analytics Engineer Associate`). Associate-level certification with **no prerequisite exam required**, free online annual renewal on Microsoft Learn, split-screen `learn.microsoft.com` access during non-lab exam sections, and hands-on coverage across **SQL**, **KQL**, **DAX**, **PySpark**, **Power Query M**, **TMDL**, and **TMSL**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` SQL/KQL/DAX/PySpark/M/TMDL/TMSL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Microsoft Fabric case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area SQL/KQL/DAX/TMDL dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn Fabric and Power BI documentation — never recalled live items or copied Microsoft sample case studies.

## Questions

### 1. A streaming data engineer needs to author Eventstreams, KQL querysets, and Spark notebooks in `Audience-Dev` without sharing assets externally or adding workspace members. Which workspace role satisfies least privilege?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Admin role
- B. Assign the Workspace Member role
- C. Assign the Workspace Viewer role
- D. Assign the Workspace Contributor role

### 2. Proposed solution: Regional ad-sales account executives are granted `Workspace Contributor` in `AdSales-Prod` workspace so they can open reports restricted by Semantic Model dynamic RLS to their own territory. Why does RLS fail to restrict them, and which workspace role is the ONLY role subject to RLS?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Viewer role
- B. Assign the Workspace Member role
- C. Assign the Workspace Contributor role
- D. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows

### 3. Studio analytics leads need to publish the `ContentExecutive` Workspace App, configure OneLake security roles, and manage Contributor access via corporate Entra groups without workspace-delete privileges. Which two choices apply? Select two.

Domain: Maintain a data analytics solution

- A. Assign the Workspace Member role
- B. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows
- C. Assign permissions to Microsoft Entra security groups rather than individual users
- D. Assign the Workspace Admin role
- E. Assign the Workspace Viewer role

### 4. You configure granular OneLake security roles on `SubscriberLakehouse` for external studio analysts who are not members of the workspace. Which baseline item-level share permission (`____`) do you grant alongside adding them to the OneLake security role?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Contributor role
- B. Share the item with ReadData (Read all SQL endpoint data) permission
- C. Share the Lakehouse with ReadAll (Read all Apache Spark data) permission
- D. Share the item with Read permission only (no ReadData or ReadAll)

### 5. Podcast producers in `Creator-Analytics` workspace want to build live thin Power BI reports over the Certified `PodcastEngagement` semantic model without editing the model. Which permission on `PodcastEngagement` is needed?

Domain: Maintain a data analytics solution

- A. Grant Build permission on the shared semantic model
- B. Share the Lakehouse with ReadAll (Read all Apache Spark data) permission
- C. Assign the Workspace Admin role
- D. Share the item with Read permission only (no ReadData or ReadAll)

### 6. Complete the DAX RLS filter expression `____` on `'DimSalesRep'` so signed-in ad reps in the Fabric portal see only rows matching their Microsoft Entra email address?

Domain: Maintain a data analytics solution

- A. Filter the RLS table using USERNAME() = [DomainLogin] without testing in the Fabric portal
- B. [ManagerEmail] = USERPRINCIPALNAME()
- C. CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))
- D. NAMEOF('DimTrade'[CurrencyPair])

### 7. Customer-support SQL analysts run `SELECT * FROM dbo.Subscribers` on `BillingWarehouse`; they must see masked credit-card and email strings (`XXXX` / `aXXX@XXXX.com`) without `SELECT *` throwing column-denied errors. Which Warehouse feature fits?

Domain: Maintain a data analytics solution

- A. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- B. Grant T-SQL column-level SELECT on only the non-sensitive columns (GRANT SELECT ON dbo.Customer(CustomerID, Region) TO ...)
- C. Apply T-SQL Dynamic Data Masking (MASKED WITH (FUNCTION = 'partial(...)')) on sensitive columns
- D. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL

### 8. Which four-step sequence rolls out OneLake security across `RoyaltiesLakehouse` and downstream label-partner shortcut workspaces?

Domain: Maintain a data analytics solution

- A. Enable OneLake security and define Read Grant roles → Assign consumers Workspace Viewer and OneLake security roles → Set SQL analytics endpoint to User's identity mode → Expose downstream shortcuts in User's identity mode
- B. Assign consumers the Workspace Contributor role → Enable OneLake security with a Deny role → Keep SQL analytics endpoint in Owner fixed identity mode → Create downstream shortcuts
- C. Set SQL analytics endpoint to Delegated mode with SQL DENY rules → Remove Workspace Viewer assignments → Enable OneLake security afterward → Export binary .pbix copies
- D. Create downstream shortcuts first → Assign consumers Workspace Member rights → Attach RLS predicates to a ReadWrite OneLake role → Enable SSO on an On-premises gateway

### 9. To restrict partner managers on `StreamRoyalties` by both `StudioId` rows and allowed non-cost columns in OneLake AND verify semantic-model RLS for `partner1@cinewave.io` before launch, which two actions are required? Select two.

Domain: Maintain a data analytics solution

- A. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- B. Create two separate OneLake security roles on the same table — Role A containing the RLS filter and Role B containing the CLS column rule — and assign the user to both
- C. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- D. Define both the RLS filter and CLS column allow-list inside a single OneLake security Grant role with Read permission
- E. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows

### 10. Pre-release box-office forecast tables in `StudioWarehouse` carry a `Confidential — Embargoed` Purview label. How does Fabric ensure new semantic models and reports created from `StudioWarehouse` inherit that classification?

Domain: Maintain a data analytics solution

- A. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- B. Apply a Microsoft Purview sensitivity label with downstream inheritance on the source Lakehouse or Warehouse
- C. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- D. Mark the item as Promoted in item settings

### 11. Proposed solution: You apply a text-only sensitivity label without encryption to `SubscriberChurnReport`, assuming exported `.xlsx` files emailed externally will block unauthorized readers. Does an unencrypted label block external opens, and what is required?

Domain: Maintain a data analytics solution

- A. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal
- B. Share the item with Read permission only (no ReadData or ReadAll)
- C. Apply T-SQL Dynamic Data Masking (MASKED WITH (FUNCTION = 'partial(...)')) on sensitive columns
- D. Use a Purview sensitivity label configured with file encryption so exported .pbix, Excel, PDF, and PowerPoint files stay protected outside Fabric

### 12. Media buyers ask which badge in OneLake catalog proves an attribution semantic model passed formal audit by the Admin-authorized Analytics Governance Council. Which badge is it?

Domain: Maintain a data analytics solution

- A. Mark the item as Promoted in item settings
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal
- D. Assign the Workspace Contributor role

### 13. Six streaming product squads maintain divergent copies of `DimContentCatalog`. Which endorsement option marks the central `GoldContentLakehouse` as the authoritative master reference source?

Domain: Maintain a data analytics solution

- A. Configure Certified endorsement with the Master data label on authoritative core tables or semantic models
- B. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- C. Mark the item as Promoted in item settings
- D. Enable a mandatory label policy and default sensitivity label in Microsoft Purview compliance portal for Fabric users

### 14. Four ad-tech BI engineers want line-by-line GitHub pull-request reviews on DAX calculation groups and visual JSON definitions while testing in isolated Fabric workspaces. Which two practices enable this? Select two.

Domain: Maintain a data analytics solution

- A. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- E. Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch

### 15. Promoting `AdAttributionModel` (`Direct Lake on SQL`) from `AdTech-Test` to `AdTech-Prod` via Deployment Pipeline must automatically point the `Prod` model to `ProdAttributionWarehouse`. What should you configure on the `Prod` stage?

Domain: Maintain a data analytics solution

- A. Configure Deployment pipeline data source and parameter rules on the Test and Production stages
- B. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline

### 16. An acquired podcast studio runs all production assets in a single `Podcast-Prod` workspace and now wants `Dev -> Test -> Prod` Deployment Pipeline stages without breaking existing `Prod` report URLs. How do you bootstrap `Test` and `Dev`?

Domain: Maintain a data analytics solution

- A. Perform a selective deployment selecting the modified item together with Select related to include required upstream dependencies
- B. Configure Deployment pipeline data source and parameter rules on the Test and Production stages
- C. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition
- D. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline

### 17. Your media ingestion pipelines and `Direct Lake on OneLake` models promote across `Dev -> Test -> Prod` stages and need environment-specific CDN container URLs and workspace IDs. Which Fabric CI/CD item stores stage-specific values?

Domain: Maintain a data analytics solution

- A. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- B. Configure Deployment pipeline data source and parameter rules on the Test and Production stages
- C. Use a Fabric Variable library (or autobinding across paired workspace items) to parameterize stage-specific environment references
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 18. Before retiring `LegacyClickDataflow` in `AdTech-Shared`, how do you list every dependent semantic model, report, and dashboard across 9 regional workspaces and send an impact alert to their owners?

Domain: Maintain a data analytics solution

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- C. Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View
- D. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time

### 19. You notice a `Royalties` report shows yesterday's numbers; opening Workspace `Lineage` view reveals an upstream `SilverToGoldLakehouse` refresh failed at `03:15 UTC`. Why is `Lineage` view ideal for root-cause triage?

Domain: Maintain a data analytics solution

- A. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- B. Mark the item as Promoted in item settings
- C. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- D. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL

### 20. Live Super Bowl streaming dashboards run on a 45 GB partitioned `Playback-Prod` semantic model; you must deploy two hotfix DAX measures from `Playback-Dev` with zero partition reprocessing. Which four-step XMLA sequence works?

Domain: Maintain a data analytics solution

- A. Verify XMLA Endpoint = Read Write on target capacity → Connect ALM Toolkit to Dev source and Prod XMLA target → Compare schemas while hiding unchanged partitions and keeping Prod data sources → Validate and deploy metadata-only TMSL changes
- B. Open Production in DAX Studio → Edit measures manually in Production without committing to Git → Copy cache.abf into GitHub → Disable sensitivity labels
- C. Leave XMLA Endpoint = Read Only → Execute T-SQL DELETE across Warehouse schemas → Grant all report viewers Capacity Admin rights → Skip downstream impact analysis
- D. Set XMLA Endpoint = Off → Overwrite Production with an empty unpartitioned .pbix file → Purge all 5 years of historical incremental partitions → Re-import 3 billion rows during peak business hours

### 21. After hourly ad-server settlement finishes for partition `2026M10`, an orchestrator sends TMSL command `____` to `powerbi://api.powerbi.com/v1.0/myorg/AdTech-Prod`. Which two items are required? Select two.

Domain: Maintain a data analytics solution

- A. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- B. Assign the Workspace Viewer role
- C. {"refresh": {"type": "dataOnly", "objects": [{"database": "WealthModel", "table": "FactPositions", "partition": "2026M10"}]}}
- D. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- E. Enable XMLA Endpoint = Read Write in Fabric Capacity workload settings and connect to powerbi://api.powerbi.com/v1.0/myorg/<WorkspaceName>

### 22. To help 25 new content analysts connect Power BI Desktop to `SubscriberWarehouse` without mistyping the Fabric SQL endpoint URL, which small connection-only launcher file should you share?

Domain: Maintain a data analytics solution

- A. Publish a single certified core semantic model in a data workspace and build thin live-connected Power BI reports in departmental workspaces
- B. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches

### 23. Regional licensing partners need a pre-built Power BI report layout with 20 DAX royalty measures and a `@TerritoryISO` query parameter prompt, containing zero embedded data rows. Which export format fits?

Domain: Maintain a data analytics solution

- A. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode

### 24. Subscriber billing runs on Azure Database for PostgreSQL Flexible Server with private VNet integration only (`vnet-media-core`). Which managed Fabric gateway connects Dataflow Gen2 without deploying self-hosted gateway VMs?

Domain: Prepare data

- A. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- B. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- C. Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet
- D. Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication

### 25. Eight pipelines pull ad-impression logs from Google BigQuery using one organizational service account credential that individual pipeline authors must not view in plain text. What should an administrator configure?

Domain: Prepare data

- A. Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication
- B. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- C. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- D. Enable single sign-on (SSO) on the Direct Lake semantic model connection

### 26. Which unified Fabric portal experience replaces the legacy OneLake data hub and provides both `Explore` asset search and `Govern` data-stewardship health insights?

Domain: Prepare data

- A. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results
- B. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time

### 27. Live-sports engineers want to (1) browse all video-player QoE streams and `Fabric capacity overview events` in one hub with Activator throttling alerts, and (2) route player heartbeat events continuously into Eventhouse. Which two features pair together? Select two.

Domain: Prepare data

- A. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- E. Use the Real-Time hub to subscribe to Microsoft.Fabric.OneLake.FileCreated events (or Capacity/CDC streams) and trigger an Activator rule

### 28. Ad-exchange partners publish 180 TB of open-format Apache Iceberg / Delta bid logs in Amazon S3. How can `AdTechLakehouse` query those tables in place without copying data?

Domain: Prepare data

- A. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- B. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- C. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging

### 29. Which three zero-ETL / streaming Fabric features eliminate custom batch copy scripts for: (1) operational subscriber profiles in Azure Cosmos DB, (2) partner Parquet archives in Google Cloud Storage, and (3) live Kafka video-buffering events? Select three.

Domain: Prepare data

- A. Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog
- B. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching
- C. Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table
- D. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- E. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- F. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 30. Video-player SDKs emit 2 million JSON QoE events per second (`rebuffer_ms`, `bitrate_kbps`, `cdn_pop`) queried interactively over sliding 1-minute windows in KQL. Which Fabric store is optimal?

Domain: Prepare data

- A. Choose a Fabric Lakehouse
- B. Choose a Fabric Eventhouse (KQL database)
- C. Choose a Fabric Data Warehouse
- D. Choose a SQL database in Microsoft Fabric

### 31. Content-recommendation data scientists process raw video subtitle `.vtt` files, thumbnail `.jpg` assets in `Files/`, and PySpark feature-engineered Delta tables in `Tables/`. Which Fabric store fits?

Domain: Prepare data

- A. Choose a Fabric Data Warehouse
- B. Choose a Fabric Eventhouse (KQL database)
- C. Choose a SQL database in Microsoft Fabric
- D. Choose a Fabric Lakehouse

### 32. Media finance needs (1) a full transactional T-SQL analytical store supporting multi-table royalty `BEGIN TRAN ... COMMIT` stored procedures, and (2) an operational OLTP database inside Fabric for rights-management web transactions. Which two stores should you provision? Select two.

Domain: Prepare data

- A. Choose a Fabric Data Warehouse
- B. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Choose a SQL database in Microsoft Fabric
- E. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint

### 33. You want `Direct Lake on OneLake` and Lakehouse Spark notebooks to read the `PlayerQoE` KQL table from `StreamingEventhouse` without exporting CSVs. Which setting must be enabled on the KQL database or table?

Domain: Prepare data

- A. Enable OneLake availability on the Eventhouse KQL database (or specific KQL table) and create an internal OneLake shortcut in the Lakehouse
- B. Point Direct Lake on SQL directly at an Eventhouse KQL database without enabling OneLake availability
- C. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- D. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL

### 34. Which four-step workflow connects live CDN buffering telemetry in an Eventhouse to a Lakehouse shortcut and a `Direct Lake on OneLake` semantic model?

Domain: Prepare data

- A. Export KQL query results manually to CSV every hour → Email CSVs to analysts → Import into binary .pbix files → Publish to My Workspace
- B. Create a Direct Lake on SQL model directly over the KQL queryset → Disable OneLake availability → Configure an On-premises data gateway → Run T-SQL MERGE on the KQL database
- C. Ingest streaming telemetry into an Eventhouse KQL database → Enable OneLake availability on the KQL database or table → Create an internal OneLake shortcut in the Lakehouse → Add the table to a Direct Lake on OneLake semantic model
- D. Create an Amazon S3 external shortcut to the KQL URI before enabling OneLake availability → Set storage mode to Dual only → Enable Auto date/time → Run XMLA clearValues

### 35. In `RoyaltiesWarehouse`, nightly artist payouts execute via `EXEC dbo.usp_CalculateMonthlyRoyalties @MonthKey = 202610`. Which Fabric store supports T-SQL stored procedures performing multi-table `INSERT`, `UPDATE`, and `MERGE`?

Domain: Prepare data

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- C. Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 36. Proposed solution: You define a non-materialized SQL view `vw_ActiveSubscribers` on `PlaybackLakehouse`'s SQL analytics endpoint and try to include it in a `Direct Lake on OneLake` model. Why is it rejected, and what works?

Domain: Prepare data

- A. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- B. Use a Lakehouse Materialized Lake View (or persisted Gold Delta table) instead of a non-materialized SQL analytics endpoint view for Direct Lake on OneLake
- C. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- D. Configure DirectQuery storage mode

### 37. In `AdRevenueWarehouse`, you grant junior analysts `SELECT` on `reporting.vw_CampaignSummary` while blocking them from querying `raw.InsertionOrders` (`____ SELECT ON OBJECT::raw.InsertionOrders TO [JuniorAnalysts]`). Which SQL control is this?

Domain: Prepare data

- A. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- B. Use T-SQL GRANT/DENY SELECT on specific Warehouse schemas, tables, or views
- C. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- D. Mark the item as Promoted in item settings

### 38. Content titles arrive from four acquired streaming catalogs with alphanumeric IDs (`"NF-9921"`, `"HB-9921"`). How should `Gold.DimTitle` be keyed for `FactWatchSessions`?

Domain: Prepare data

- A. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- D. Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions

### 39. Broadcast ad sales operate on a standard Broadcast Calendar (weeks always starting Monday and months ending on the last Sunday) shared across `FactAdImpressions` and `FactLinearSpots`. How should you enrich the Gold schema?

Domain: Prepare data

- A. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- B. Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. Configure DirectQuery storage mode

### 40. A Silver PySpark job derives `DeviceCategory` from 2 billion User-Agent strings (`df.____("DeviceCategory", F.when(...))`) and maps `TitleKey` surrogates, replacing a slow Python `@udf`. Which two engineering practices apply? Select two.

Domain: Prepare data

- A. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- B. Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs
- E. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals

### 41. When a subscriber upgrades from `Ad-Supported Basic` to `Ad-Free Ultra` on October 12, watch hours logged October 1–11 must remain attributed to `Ad-Supported Basic` while October 12+ hours attribute to `Ad-Free Ultra`. Which SCD type on `DimSubscriber` is required?

Domain: Prepare data

- A. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns
- B. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- C. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)
- D. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place

### 42. An episode title `"Episode IV: A New Hope (Remasterd)"` has a typo corrected in the CMS; all historical and future dashboards should show `"Remastered"` without splitting watch counts across two rows. Which SCD type fits?

Domain: Prepare data

- A. Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table
- B. Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE
- C. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns
- D. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place

### 43. Which four-step ELT sequence maintains `DimAdAgency` as a Type 2 Slowly Changing Dimension when agency holding-company ownership changes?

Domain: Prepare data

- A. Truncate the Gold dimension table → Reassign fresh random surrogate keys to all historical rows → Join historical facts without updating foreign keys → Set IsCurrent = 1 on every version
- B. Stage and deduplicate incoming records by natural key → Compare tracked attributes against active (IsCurrent = 1) Gold rows → Expire changed active rows (EffectiveEndDate, IsCurrent = 0) → Insert new active versions with fresh surrogate keys
- C. Insert raw duplicate staging rows directly into FactSales → Delete unmatched dimension keys → Leave EffectiveStartDate NULL → Enable Assume referential integrity on broken keys
- D. Insert new versions with IsCurrent = 0 first → Overwrite old EffectiveStartDate values in place → Remove the natural business key column → Deduplicate after publishing reports

### 44. Which three dimensional rules ensure `Gold.FactAdImpressions` avoids double-counted campaign budgets and broken `1:*` Direct Lake joins? Select three.

Domain: Prepare data

- A. Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures
- B. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- C. Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE
- D. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- E. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- F. Organize OneLake into Bronze (raw immutable), Silver (validated, deduplicated, conformed), and Gold (star-schema dimensions and facts with V-Order)

### 45. In the CMS database, `Episode -> Season -> Series -> Franchise -> Genre` spans five normalized tables. How should you design `Gold.DimContent` for Direct Lake?

Domain: Prepare data

- A. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- B. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- C. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()
- D. Choose a Fabric Eventhouse (KQL database)

### 46. Why does flattening `Advertiser -> Brand -> ParentConglomerate` into one `DimAdvertiser` table simplify DAX authoring and improve Storage Engine scan speed?

Domain: Prepare data

- A. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- B. Configure DirectQuery storage mode
- C. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns
- D. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition

### 47. Heartbeat pings log 25 billion 10-second playback rows per month, whereas executive content scorecards show daily total hours streamed and unique viewers by `Title` and `Country`. How should you reduce Direct Lake memory?

Domain: Prepare data

- A. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- B. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- C. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- D. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)

### 48. Complete `SELECT Country, SubscriptionTier, SUM(StreamHours) AS Hours FROM gold.FactDailyStreams ____;` so one T-SQL scan outputs `(Country, SubscriptionTier)`, `(Country)`, and global `()` totals?

Domain: Prepare data

- A. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- B. TRY_CAST(RawReading AS DECIMAL(18, 4))
- C. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- D. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)

### 49. When aggregating 120 million ad-impression rows into campaign daily totals in Dataflow Gen2 over a Snowflake source, why should you verify the step folding indicator shows `Folded` on `Group by`?

Domain: Prepare data

- A. Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled
- B. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- C. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 50. Complete `MERGE INTO gold.DimSubscriber t USING silver.StgSubscriber s ON t.SubscriberId = s.SubscriberId ____ t.Country = s.Country WHEN NOT MATCHED THEN INSERT *;` so untouched subscriber rows do not rewrite Parquet files?

Domain: Prepare data

- A. WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET
- B. ADD BLOCK PREDICATE dbo.sp_checkregion(RegionCode) AFTER INSERT
- C. CAST(RawReading AS FLOAT)
- D. RANK() OVER (ORDER BY SpecimenId DESC)

### 51. Content operations needs a list of licensed `DimTitle` movies that recorded **zero** `FactWatchSessions` in the past 90 days to evaluate non-renewal. Which join kind returns only unwatched titles?

Domain: Prepare data

- A. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- B. Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table
- C. Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement
- D. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid

### 52. A Spark job joins 1.8 billion ad-impression events with an 8 MB `dim_dma_region` table (`impr_df.join(____)`) and upserts reconciled billing totals into `gold.fact_ad_billing`. Which two techniques avoid shuffles and preserve ACID state? Select two.

Domain: Prepare data

- A. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- B. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- C. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- D. fact_df.join(F.broadcast(dim_store_df), on="StoreKey", how="left")
- E. Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement

### 53. Mobile player offline-sync queues upload duplicate `SessionEventId` records when Wi-Fi reconnects. Complete `SELECT *, ____ AS rn FROM silver.playback_events` so `WHERE rn = 1` keeps strictly one newest record per event ID?

Domain: Prepare data

- A. TRY_CAST(RawReading AS DECIMAL(18, 4))
- B. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- C. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- D. RANK() OVER (ORDER BY SpecimenId DESC)

### 54. Live premiere streams begin generating `FactWatchSessions` 10 minutes before the CMS metadata job inserts the new `LiveEventTitleId` into `DimTitle`. How do you prevent losing or blank-slicing those early watch rows?

Domain: Prepare data

- A. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- B. Filter Incremental Refresh with OrderDate >= RangeStart AND OrderDate <= RangeEnd using inclusive operators on both boundaries
- C. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- D. Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE

### 55. Proposed solution: A junior engineer trusts Power Query's default 1,000-row column profile on a 50-million-row partner royalty CSV and loads duplicate `RoyaltyLineId` rows into Gold. Which two steps fix profiling scope and deduplication? Select two.

Domain: Prepare data

- A. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- B. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- C. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- D. Deduplicate using ROW_NUMBER() OVER (PARTITION BY BusinessKey ORDER BY ModifiedTimestamp DESC) = 1
- E. Launch Data Wrangler from a Fabric Spark notebook (or enable Power Query Column profiling based on entire data set) to inspect nulls, duplicates, and distributions and export generated PySpark code

### 56. Third-party podcast download CSVs occasionally contain `"REDACTED"` in the `RevenueCPM` column (`SELECT EpisodeId, ____ AS CleanCPM FROM stage.PodcastAds;`). Which T-SQL expression converts valid numbers to exact fixed decimal and maps `"REDACTED"` to `NULL`?

Domain: Prepare data

- A. TRY_CAST(RawReading AS DECIMAL(18, 4))
- B. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- C. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- D. CAST(RawReading AS FLOAT)

### 57. `Gold.FactStreamEvents` contains `SessionUUID` (`GUID` / `BINARY`) and `DrmLicenseBlob` (`BINARY`), causing Direct Lake table validation warnings. What schema adjustment ensures clean Direct Lake compatibility?

Domain: Prepare data

- A. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- B. Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake
- C. Configure shared dimension tables in Dual storage mode inside a composite model
- D. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically

### 58. On a 6-billion-row `gold.fact_impressions` Delta table partitioned by `ImpressionDate`, why does `WHERE ImpressionDate >= '2026-10-01' AND ImpressionDate < '2026-10-08'` outperform `WHERE DATEPART(week, ImpressionDate) = 41`?

Domain: Prepare data

- A. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- B. CAST(RawReading AS FLOAT)
- C. Filter on physical Delta partition or liquid-clustered date columns using sargable range predicates (OrderDate >= '2026-01-01') without wrapping the column in functions
- D. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'

### 59. An ad-ops manager without T-SQL experience wants to join `FactCampaignSpend` and `DimAgency` visually in the browser inside `AdTechWarehouse`, filter `Spend > 50000`, and save `vw_TopAgencySpend`. Which tool fits?

Domain: Prepare data

- A. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- B. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results

### 60. Can an analyst use the `Visual query editor` against a read-only **Lakehouse SQL analytics endpoint** as well as a **Fabric Data Warehouse** to explore tables visually and save SQL views?

Domain: Prepare data

- A. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- B. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition

### 61. `BillingWarehouse` and `PlaybackLakehouse` live inside `Media-Prod` workspace. Complete `SELECT b.PlanId, COUNT(p.SessionId) FROM dbo.DimPlan b JOIN ____ p ON b.PlanId = p.PlanId GROUP BY b.PlanId;` for a zero-copy T-SQL join?

Domain: Prepare data

- A. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- B. Query across a Warehouse and a Lakehouse SQL analytics endpoint in the same workspace using three-part T-SQL naming (SalesLakehouse.dbo.RawOrders)
- C. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching
- D. Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet

### 62. Complete `SELECT SeriesId, ReleaseWeek, WeeklyViews, WeeklyViews - ____ AS WeekOverWeekDelta FROM gold.FactSeriesViews;` to calculate week-over-week audience drop-off per series?

Domain: Prepare data

- A. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- B. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- C. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- D. TRY_CAST(RawReading AS DECIMAL(18, 4))

### 63. Media royalties auditors need to (1) inspect `dbo.FactRoyaltyPayouts` exactly as it stood prior to an adjustment run at `2026-10-28T06:00:00.000` (`____`), and (2) create an instant zero-copy sandbox clone of the table in `RoyaltiesWarehouse`. Which two T-SQL features apply? Select two.

Domain: Prepare data

- A. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- B. CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales
- C. OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')
- D. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- E. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'

### 64. Smart-TV apps send periodic playback state heartbeats into `PlaybackEventhouse`. Complete `PlayerStateEvents | where IngestionTime > ago(4h) ____` to retrieve the single latest heartbeat state row per `DeviceSessionId`?

Domain: Prepare data

- A. | summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)
- B. | summarize arg_max(IngestionTime, *) by SpecimenId
- C. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- D. | make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion

### 65. Ad-pod beacon JSON payloads in `AdBeaconEventhouse` contain a nested array `QuartilesWatched` inside `Payload`. Complete `AdBeacons ____ | summarize count() by tostring(Quartile.event)` to count quartile completions?

Domain: Prepare data

- A. | summarize arg_max(IngestionTime, *) by SpecimenId
- B. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- C. | mv-expand PhaseReading = parse_json(Payload).PhaseReadings
- D. | summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)

### 66. A talent-contracts team refreshes a 90 MB semantic model once daily from Workday REST APIs and requires complex calculated columns and ultra-fast offline/online slicing. Which storage mode fits best?

Domain: Implement and manage semantic models

- A. Configure Direct Lake storage mode
- B. Configure Import storage mode
- C. Configure DirectQuery storage mode
- D. Configure shared dimension tables in Dual storage mode inside a composite model

### 67. In an ad-tech composite model with an `Import` daily campaign summary table and a `DirectQuery` impression-log Warehouse table, setting `DimCampaign` and `DimDate` to which storage mode serves both paths optimally?

Domain: Implement and manage semantic models

- A. Configure shared dimension tables in Dual storage mode inside a composite model
- B. Configure DirectQuery storage mode
- C. Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop)
- D. Configure Import storage mode

### 68. `FactSubscriptions[StartDateKey]` (`INT`) joins to `DimBroadcastDate[DateKey]`. What semantic-model setting on `DimBroadcastDate` ensures DAX time-intelligence functions clear `DateKey` filters properly and avoids hidden auto-date tables?

Domain: Implement and manage semantic models

- A. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- B. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column

### 69. Which two model-design steps ensure self-service media analysts see measures grouped into clean `Engagement` and `Monetization` folders, cannot accidentally sum `TitleSurrogateKey`, and see broadcast months sorted in broadcast order? Select two.

Domain: Implement and manage semantic models

- A. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- B. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- C. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- D. Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column
- E. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension

### 70. `FactSubscriptions` carries `SignupDateKey`, `TrialEndDateKey`, and `CancelDateKey` all referencing `DimCalendar[DateKey]`. How do you plot `[New Signups]` and `[Cancellations]` by calendar month on one chart without three Calendar tables?

Domain: Implement and manage semantic models

- A. Introduce a deduplicated Bridge table between the two dimensions and scope bidirectional propagation strictly inside specific measures using CROSSFILTER(..., BOTH)
- B. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- C. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- D. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()

### 71. Movies belong to multiple `Genres` (`Action`, `Sci-Fi`, `Thriller`) via `BridgeTitleGenre`. Complete `Genre Watch Hours = ____` (conceptually scoping bidirectional bridge filtering) so genre slicers filter watch hours without enabling permanent model-wide bidirectional relationships?

Domain: Implement and manage semantic models

- A. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- B. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- C. CALCULATE([Encounter Count], CROSSFILTER('FactEncounter'[EncounterKey], 'BridgeEncounterDiag'[EncounterKey], BOTH))
- D. CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))

### 72. On a `DirectQuery` live-event concurrency model backed by a curated Warehouse with validated non-null `EventKey` foreign keys, enabling which relationship property switches SQL joins from `OUTER JOIN` to `INNER JOIN`?

Domain: Implement and manage semantic models

- A. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- B. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- C. Configure Import storage mode
- D. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL

### 73. Each row of `FactAdPlacements` stores `Impressions` and `ContractCPM`. Complete `Gross Ad Spend = ____(FactAdPlacements, DIVIDE(FactAdPlacements[Impressions], 1000) * FactAdPlacements[ContractCPM])` to compute exact revenue without adding calculated columns?

Domain: Implement and manage semantic models

- A. Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches
- B. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)
- C. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- D. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table

### 74. A `[Churn Risk Tier]` measure calls `[Trailing 14D Watch Mins]` four times across nested `IF` checks. Refactoring `[Trailing 14D Watch Mins]` into a single `____` before `RETURN` reduces Storage Engine scans by 75%?

Domain: Implement and manage semantic models

- A. Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches
- B. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- C. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- D. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table

### 75. On a `Franchise -> Series -> Episode` matrix using CineWave's non-Gregorian Broadcast Calendar, you need (1) `[Prior Broadcast Period Hours]` (`____`), and (2) `[Episode Completion %]` suppressed to `BLANK()` on `Series` and `Franchise` subtotals (`____`). Which two DAX constructs apply? Select two.

Domain: Implement and manage semantic models

- A. CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC)))
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- D. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- E. IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK())

### 76. In a `Metric Comparison` Calculation Group (`Actual`, `Budget`, `Variance`, `Variance %`) applied across 45 subscriber and ad KPIs, which function (`____`) inside each calculation item dynamically evaluates the active measure?

Domain: Implement and manage semantic models

- A. [ManagerEmail] = USERPRINCIPALNAME()
- B. EVALUATE INFO.VIEW.MEASURES()
- C. NAMEOF('DimTrade'[CurrencyPair])
- D. CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))

### 77. Proposed solution: To format `"YoY Growth"` as `"0.0%"` and base revenue as `"$#,0"`, an analyst wraps the Calculation Item in `FORMAT(SELECTEDMEASURE(), ...)`, breaking all bar charts on the page. Which Dynamic Format String expression (`____`) fixes the charts?

Domain: Implement and manage semantic models

- A. IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())
- B. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- C. NAMEOF('DimTrade'[CurrencyPair])
- D. CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))

### 78. Content executives want one toggle slicer (`View By: Genre, Country, DevicePlatform, or SubscriptionTier`) that swaps a line chart's Legend dynamically without duplicate bookmarked visuals. Which modeling feature should you create?

Domain: Implement and manage semantic models

- A. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Create a Calculation Group with Calculation Items referencing SELECTEDMEASURE() and explicit Precedence ordering (automatically setting DiscourageImplicitMeasures = true)
- D. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer

### 79. An audience-panel Import semantic model reaches 14 GB compressed on an F64 capacity. Turning on which semantic-model setting enables refreshes past 10 GB and faster XMLA metadata updates?

Domain: Implement and manage semantic models

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Configure DirectQuery storage mode
- C. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages
- D. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)

### 80. How does on-demand segment paging behave on Fabric semantic models once `Large semantic model storage format` is enabled?

Domain: Implement and manage semantic models

- A. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- B. Mark the item as Promoted in item settings
- C. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- D. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view

### 81. Over a 7-billion-row `DirectQuery` ad-beacon Warehouse table, which two configurations let high-level `Date x Campaign` visuals run in sub-second memory while allowing rare creative-level drilldowns via native SQL `INNER`/`LEFT` joins? Select two.

Domain: Implement and manage semantic models

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table
- C. Configure shared dimension tables in Dual storage mode inside a composite model
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- E. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches

### 82. A live-launch war-room report page has 36 separate KPI cards and takes 8.5 seconds to refresh despite <35 ms DAX queries. Which tool proves `Other` visual-container queuing is the bottleneck?

Domain: Implement and manage semantic models

- A. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- B. Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View
- C. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- D. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time

### 83. On a `DirectQuery` ad-log explorer report, checking five advertisers in a multi-select slicer triggers five sequential Warehouse queries. Which `Query reduction` setting sends one combined query instead?

Domain: Implement and manage semantic models

- A. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- B. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- C. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages
- D. Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails

### 84. Proposed solution: VertiPaq Analyzer reveals `PlaybackSessionGUID` (950 million unique values, unused by any visual or relationship) consumes 11 GB of dictionary memory, so an engineer hides `PlaybackSessionGUID` in Model view assuming hidden columns take zero RAM. Does hiding free RAM, and what should you do?

Domain: Implement and manage semantic models

- A. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- B. Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time
- C. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- D. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer

### 85. Which four-step diagnostic sequence resolves a 12-second `[Attributed ROAS]` measure on a Direct Lake semantic model and verifies true cold-cache improvement?

Domain: Implement and manage semantic models

- A. Immediately upgrade from F64 to F512 without profiling → Enable bidirectional cross-filtering on all relationships → Convert numeric measures to FORMAT() strings → Disable V-Order on Gold tables
- B. Capture visual timings in Performance Analyzer → Profile captured DAX in DAX Studio with Server Timings and Query Plan → Refactor FILTER(Fact,...) into VAR-cached SE column predicates and run V-Order OPTIMIZE → Re-test with Clear Cache
- C. Hide slow measures in Display Folders → Turn on Auto date/time → Split one Gold dimension into 6 normalized snowflake tables → Remove calendar surrogate keys
- D. Test queries only against warm VertiPaq cache without Clear Cache → Add high-cardinality GUID calculated columns to FactSales → Force DirectQueryOnly behavior → Add 45 single-value card visuals to one page

### 86. Which three practices prevent a `Direct Lake on SQL` audience semantic model from hitting capacity rowgroup/memory guardrails or silently falling back to slow SQL queries? Select three.

Domain: Implement and manage semantic models

- A. Expect Direct Lake on OneLake to automatically fall back to DirectQuery against the SQL analytics endpoint when capacity memory guardrails are exceeded
- B. Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time
- C. Set DirectLakeBehavior = DirectLakeOnly on a Direct Lake on SQL semantic model so queries fail fast instead of silently falling back to slow DirectQuery
- D. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- E. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- F. Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails

### 87. You want to migrate `AdSalesModel` from `Direct Lake on SQL` to `Direct Lake on OneLake` in Power BI Desktop TMDL view (`____` -> `AzureStorage.DataLake(...)`) without breaking bound reports. Which four-step sequence applies?

Domain: Implement and manage semantic models

- A. Live edit the model in Power BI Desktop and save a Version history point → Script the semantic model in TMDL view → Replace Sql.Database(...) with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...") → Apply TMDL and run framing refresh
- B. Download the Direct Lake model as an offline Import .pbix → Convert all tables to Dual storage mode → Replace AzureStorage.DataLake with OleDb.DataSource → Re-upload to My Workspace
- C. Delete the semantic model in Production breaking report GUID bindings → Recreate measures manually from screenshots → Share Lakehouse Admin rights with all report viewers → Disable V-Order
- D. Keep non-materialized SQL analytics endpoint views as the only sources → Switch TMDL expression to AzureStorage.DataLake without materializing Delta tables → Enable DirectQuery fallback on Direct Lake on OneLake → Bind an On-premises gateway

### 88. Which four-step workflow configures Incremental Refresh on a 500-million-row `FactRoyaltyLedger` Import table retaining 5 years of history and refreshing the last 14 days?

Domain: Implement and manage semantic models

- A. Publish an unfiltered 2-billion-row Import PBIX locally first → Define RangeStart in DAX calculated tables afterward → Set storage mode to Direct Lake on OneLake → Enable VNet gateway on Direct Lake
- B. Create Text parameters named StartDate and EndDate → Add a custom M step breaking query folding before filtering → Use >= and <= inclusive bounds on both sides → Refresh only in Power BI Desktop
- C. Filter OrderDate > RangeEnd → Configure Detect data changes on the exact same OrderDate partition column → Disable query folding → Run XMLA clearValues without processing
- D. Create case-sensitive DateTime parameters RangeStart and RangeEnd → Apply foldable half-open filter (>= RangeStart and < RangeEnd) → Configure table Incremental refresh policy → Publish to workspace and run initial refresh to generate partitions

---

## Case study — AdPulse Attribution

AdPulse Attribution manages 180 DAX measures across campaign semantic models. Analytics engineers want to author and validate three candidate attribution measures side-by-side in a grid without committing broken DAX to the model, export a live inventory of all model measures and expressions via DAX, and fix a measure that accidentally overrides report `Channel` slicer selections.

The next 3 questions refer to **AdPulse Attribution**. Read the scenario brief once, then answer each item independently.

### 89. Which Power BI authoring surface lets engineers write and compare three candidate attribution measures side-by-side in a grid (`DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...)`) before saving to the model?

Domain: Prepare data

- A. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- B. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results

### 90. Complete the DAX Query View command `____` to export a live catalog of all 180 model measures, formulas, display folders, and format strings?

Domain: Prepare data

- A. NAMEOF('DimTrade'[CurrencyPair])
- B. [ManagerEmail] = USERPRINCIPALNAME()
- C. CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))
- D. EVALUATE INFO.VIEW.MEASURES()

### 91. `Paid Social Conversions = CALCULATE([Conversions], 'DimChannel'[Channel] = "Paid Social")` overwrites the user's report slicer when `"Search"` is selected. Wrapping the predicate in `____` fixes this?

Domain: Implement and manage semantic models

- A. Pass simple column predicates wrapped in KEEPFILTERS(DimProduct[Color] = "Red") to CALCULATE instead of FILTER(ALL(FactSales), ...)
- B. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- C. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- D. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table

---

## Case study — CineWave Stream

CineWave Stream stores 4 billion playback events in a Gold Lakehouse, subscription invoices in a separate Fabric Warehouse, and quarterly ad-sales targets in SharePoint Online Excel sheets. Architects want one semantic model reading both Fabric Delta sources via Direct Lake plus imported Excel targets with regular relationships and strict zero-fallback guarantees.

The next 3 questions refer to **CineWave Stream**. Read the scenario brief once, then answer each item independently.

### 92. Which Direct Lake mode lets one semantic model read both the 4-billion-row `PlaybackLakehouse` and the separate `BillingWarehouse` while guaranteeing zero DirectQuery fallback?

Domain: Implement and manage semantic models

- A. Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop)
- B. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- C. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- D. Configure DirectQuery storage mode

### 93. How can engineers add the SharePoint Online Excel ad-sales target sheets into that same `Direct Lake on OneLake` semantic model with fast regular `1:*` relationships?

Domain: Implement and manage semantic models

- A. Build a Direct Lake on OneLake composite semantic model combining Direct Lake fact tables from OneLake with Import dimension/target tables using regular relationships
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- D. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes

### 94. Hourly Spark jobs finish compacting playback Delta tables at `:05` past the hour, and CineWave disables automatic updates so partial mid-job writes never appear. What operation at `:06` exposes the completed batch?

Domain: Implement and manage semantic models

- A. Expect Direct Lake on OneLake to automatically fall back to DirectQuery against the SQL analytics endpoint when capacity memory guardrails are exceeded
- B. Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes
- C. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- D. Configure Import storage mode

---

## Case study — PressLine Digital

PressLine Digital ingests 600 GB of raw nightly CDN Parquet logs from Blob Storage and 35 tables from PostgreSQL requiring low-code M lookups and column splits. A junior analyst added an `Index Column` step before date filtering in Dataflow Gen2, causing refreshes to jump from 4 minutes to 52 minutes.

The next 3 questions refer to **PressLine Digital**. Read the scenario brief once, then answer each item independently.

### 95. Which Fabric tool should ingest the 600 GB of nightly raw CDN Parquet logs from Blob Storage into `BronzeLakehouse` at lowest CU consumption when no M transformations are needed?

Domain: Prepare data

- A. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- B. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table

### 96. Which configuration optimizes ingesting and splitting the 35 PostgreSQL tables requiring visual Power Query M lookups into `EditorialWarehouse`?

Domain: Prepare data

- A. Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table
- B. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- C. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- D. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations

### 97. Why did adding `Index Column` before the date filter jump Dataflow Gen2 duration from 4 minutes to 52 minutes, and how do you restore speed?

Domain: Prepare data

- A. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'
- B. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- C. Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled
- D. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table

---

## Case study — SoundStage Live

SoundStage Live links its Fabric workspaces to Azure DevOps Git using `.pbip` projects. One developer accidentally staged a 650 MB `cache.abf` file in a PR, another developer wants to discard broken uncommitted notebook edits in their feature workspace, and the team lead notices merged PR commits on `main` have not appeared in the shared Dev workspace yet.

The next 3 questions refer to **SoundStage Live**. Read the scenario brief once, then answer each item independently.

### 98. How do you prevent developers from staging 650 MB `cache.abf` VertiPaq data files and personal `localSettings.json` files in `.pbip` pull requests?

Domain: Maintain a data analytics solution

- A. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- D. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository

### 99. Which Source control pane action lets the developer cleanly discard broken uncommitted notebook edits in their isolated feature workspace back to the last synced commit?

Domain: Maintain a data analytics solution

- A. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline
- B. Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch
- C. Use Undo in the Fabric Workspace Source control pane to discard uncommitted workspace edits back to the last synced commit
- D. Commit workspace changes to Git from the Source control pane, merge via pull request, then select Update all in the target workspace

### 100. Why haven't merged PR commits on `main` appeared in `SoundStage-Dev` yet, and which four-step end-to-end Git + Deployment Pipeline sequence completes promotion?

Domain: Maintain a data analytics solution

- A. Connect Production directly to a feature branch → Edit semantic models live in Prod → Force-push binary .pbix files including cache.abf to main → Deploy backward to Development
- B. Connect shared Dev workspace to main → Branch out to an isolated developer workspace and commit .pbip/Notebook edits → Merge pull request into main in Git → Run Update all in Dev and promote via Deployment Pipeline
- C. Edit items directly on main without branching → Merge an empty PR → Promote Dev to Test before running Update from Git → Configure Git integration last
- D. Branch out to personal My Workspace → Run Undo to push changes to GitHub → Delete .platform metadata files → Copy visuals manually into Production

---

## Answer key and explanations

### Question 1 — D

Answer: Assign the Workspace Contributor role. `Workspace Contributor` grants build and run permissions inside the workspace without external sharing, App publishing, or role administration rights. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: `Workspace Contributor` grants build and run permissions inside the workspace without external sharing, App publishing, or role administration rights.
- **B:** Incorrect for this requirement. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. Why the keyed choice wins: `Workspace Contributor` grants build and run permissions inside the workspace without external sharing, App publishing, or role administration rights.
- **C:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: `Workspace Contributor` grants build and run permissions inside the workspace without external sharing, App publishing, or role administration rights.
- **D:** Correct. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. In this scenario: `Workspace Contributor` grants build and run permissions inside the workspace without external sharing, App publishing, or role administration rights.

### Question 2 — A

Answer: Assign the Workspace Viewer role. `Workspace Viewer` is enforced by Semantic Model RLS and OneLake security, whereas `Admin`, `Member`, and `Contributor` bypass row restrictions. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Correct. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. In this scenario: `Workspace Viewer` is enforced by Semantic Model RLS and OneLake security, whereas `Admin`, `Member`, and `Contributor` bypass row restrictions.
- **B:** Incorrect for this requirement. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. Why the keyed choice wins: `Workspace Viewer` is enforced by Semantic Model RLS and OneLake security, whereas `Admin`, `Member`, and `Contributor` bypass row restrictions.
- **C:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: `Workspace Viewer` is enforced by Semantic Model RLS and OneLake security, whereas `Admin`, `Member`, and `Contributor` bypass row restrictions.
- **D:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: `Workspace Viewer` is enforced by Semantic Model RLS and OneLake security, whereas `Admin`, `Member`, and `Contributor` bypass row restrictions.

### Question 3 — A, C

Answers: Assign the Workspace Member role; Assign permissions to Microsoft Entra security groups rather than individual users. Granting `Workspace Member` to a Microsoft Entra security group enables App publishing, sharing, and OneLake-role management without `Workspace Admin` deletion risk. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Correct. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. In this scenario: Granting `Workspace Member` to a Microsoft Entra security group enables App publishing, sharing, and OneLake-role management without `Workspace Admin` deletion risk.
- **B:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: Granting `Workspace Member` to a Microsoft Entra security group enables App publishing, sharing, and OneLake-role management without `Workspace Admin` deletion risk.
- **C:** Correct. Granting workspace, item, deployment-pipeline, and RLS role memberships to Microsoft Entra security groups centralizes joiner/mover/leaver governance and scales across workspaces without per-user ACL drift. In this scenario: Granting `Workspace Member` to a Microsoft Entra security group enables App publishing, sharing, and OneLake-role management without `Workspace Admin` deletion risk.
- **D:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: Granting `Workspace Member` to a Microsoft Entra security group enables App publishing, sharing, and OneLake-role management without `Workspace Admin` deletion risk.
- **E:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: Granting `Workspace Member` to a Microsoft Entra security group enables App publishing, sharing, and OneLake-role management without `Workspace Admin` deletion risk.

### Question 4 — D

Answer: Share the item with Read permission only (no ReadData or ReadAll). Sharing the Lakehouse with baseline `Read` metadata permission (without `ReadAll` or `ReadData`) allows callers to reach the item while their OneLake security role governs exact table/row/column access. Item-level Read metadata permission lets a user connect to a Lakehouse or Warehouse item container without granting broad OneLake file access; combine with SELECT or OneLake security roles for granular least-privilege access. Local study-map skill 1.2 (Implement Item-Level Access Controls (Read, ReadData, ReadAll, Build, SSO vs Fixed Identity)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Share items in Microsoft Fabric & Semantic model Build permission (https://learn.microsoft.com/en-us/fabric/fundamentals/share-items).

- **A:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: Sharing the Lakehouse with baseline `Read` metadata permission (without `ReadAll` or `ReadData`) allows callers to reach the item while their OneLake security role governs exact table/row/column access.
- **B:** Incorrect for this requirement. ReadData grants SELECT across all tables/views in the SQL analytics endpoint or Warehouse without granting direct Spark/ABFS access to underlying Lakehouse files. Why the keyed choice wins: Sharing the Lakehouse with baseline `Read` metadata permission (without `ReadAll` or `ReadData`) allows callers to reach the item while their OneLake security role governs exact table/row/column access.
- **C:** Incorrect for this requirement. ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled. Why the keyed choice wins: Sharing the Lakehouse with baseline `Read` metadata permission (without `ReadAll` or `ReadData`) allows callers to reach the item while their OneLake security role governs exact table/row/column access.
- **D:** Correct. Item-level Read metadata permission lets a user connect to a Lakehouse or Warehouse item container without granting broad OneLake file access; combine with SELECT or OneLake security roles for granular least-privilege access. In this scenario: Sharing the Lakehouse with baseline `Read` metadata permission (without `ReadAll` or `ReadData`) allows callers to reach the item while their OneLake security role governs exact table/row/column access.

### Question 5 — A

Answer: Grant Build permission on the shared semantic model. `Build` permission on the shared semantic model enables thin report creation, `Analyze in Excel`, and DAX queries without workspace edit access. Build permission on a semantic model allows analysts to create new Power BI reports, use Analyze in Excel, and issue XMLA/DAX queries against the model without granting workspace Contributor rights or underlying Lakehouse access. Local study-map skill 1.2 (Implement Item-Level Access Controls (Read, ReadData, ReadAll, Build, SSO vs Fixed Identity)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Share items in Microsoft Fabric & Semantic model Build permission (https://learn.microsoft.com/en-us/fabric/fundamentals/share-items).

- **A:** Correct. Build permission on a semantic model allows analysts to create new Power BI reports, use Analyze in Excel, and issue XMLA/DAX queries against the model without granting workspace Contributor rights or underlying Lakehouse access. In this scenario: `Build` permission on the shared semantic model enables thin report creation, `Analyze in Excel`, and DAX queries without workspace edit access.
- **B:** Incorrect for this requirement. ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled. Why the keyed choice wins: `Build` permission on the shared semantic model enables thin report creation, `Analyze in Excel`, and DAX queries without workspace edit access.
- **C:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: `Build` permission on the shared semantic model enables thin report creation, `Analyze in Excel`, and DAX queries without workspace edit access.
- **D:** Incorrect for this requirement. Item-level Read metadata permission lets a user connect to a Lakehouse or Warehouse item container without granting broad OneLake file access; combine with SELECT or OneLake security roles for granular least-privilege access. Why the keyed choice wins: `Build` permission on the shared semantic model enables thin report creation, `Analyze in Excel`, and DAX queries without workspace edit access.

### Question 6 — B

Answer: [ManagerEmail] = USERPRINCIPALNAME(). `[ManagerEmail] = USERPRINCIPALNAME()` reliably returns the signed-in user's Entra UPN (`user@domain.com`) in the Fabric service. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. In Power BI Desktop USERNAME() returns DOMAIN\user whereas in the Fabric service it returns the UPN; USERPRINCIPALNAME() consistently returns user@domain.com across cloud evaluations. Why the keyed choice wins: `[ManagerEmail] = USERPRINCIPALNAME()` reliably returns the signed-in user's Entra UPN (`user@domain.com`) in the Fabric service.
- **B:** Correct. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. In this scenario: `[ManagerEmail] = USERPRINCIPALNAME()` reliably returns the signed-in user's Entra UPN (`user@domain.com`) in the Fabric service.
- **C:** Incorrect for this requirement. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. Why the keyed choice wins: `[ManagerEmail] = USERPRINCIPALNAME()` reliably returns the signed-in user's Entra UPN (`user@domain.com`) in the Fabric service.
- **D:** Incorrect for this requirement. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Why the keyed choice wins: `[ManagerEmail] = USERPRINCIPALNAME()` reliably returns the signed-in user's Entra UPN (`user@domain.com`) in the Fabric service.

### Question 7 — C

Answer: Apply T-SQL Dynamic Data Masking (MASKED WITH (FUNCTION = 'partial(...)')) on sensitive columns. T-SQL `Dynamic Data Masking` (`MASKED WITH (FUNCTION = ...)`) masks sensitive values in query output for non-`UNMASK` users while allowing `SELECT *` queries to succeed. Dynamic Data Masking obfuscates sensitive strings/emails/numbers in query results for users lacking UNMASK permission while keeping the column present so SELECT * queries do not fail. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: T-SQL `Dynamic Data Masking` (`MASKED WITH (FUNCTION = ...)`) masks sensitive values in query output for non-`UNMASK` users while allowing `SELECT *` queries to succeed.
- **B:** Incorrect for this requirement. In Fabric Warehouse and SQL analytics endpoints, column-level security restricts users to explicitly permitted columns via column-scoped GRANT SELECT without creating duplicate views or physical tables. Why the keyed choice wins: T-SQL `Dynamic Data Masking` (`MASKED WITH (FUNCTION = ...)`) masks sensitive values in query output for non-`UNMASK` users while allowing `SELECT *` queries to succeed.
- **C:** Correct. Dynamic Data Masking obfuscates sensitive strings/emails/numbers in query results for users lacking UNMASK permission while keeping the column present so SELECT * queries do not fail. In this scenario: T-SQL `Dynamic Data Masking` (`MASKED WITH (FUNCTION = ...)`) masks sensitive values in query output for non-`UNMASK` users while allowing `SELECT *` queries to succeed.
- **D:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: T-SQL `Dynamic Data Masking` (`MASKED WITH (FUNCTION = ...)`) masks sensitive values in query output for non-`UNMASK` users while allowing `SELECT *` queries to succeed.

### Question 8 — A

Answer: Enable OneLake security and define Read Grant roles → Assign consumers Workspace Viewer and OneLake security roles → Set SQL analytics endpoint to User's identity mode → Expose downstream shortcuts in User's identity mode. Defining Read Grant roles on `RoyaltiesLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access. Correct order: enable OneLake security with Grant roles first, assign consumers to Viewer + security roles (never Contributor), set SQL analytics endpoints to User's identity mode, and expose shortcuts downstream. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Correct. Correct order: enable OneLake security with Grant roles first, assign consumers to Viewer + security roles (never Contributor), set SQL analytics endpoints to User's identity mode, and expose shortcuts downstream. In this scenario: Defining Read Grant roles on `RoyaltiesLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access.
- **B:** Incorrect for this requirement. Incorrect: Contributors bypass OneLake security completely, OneLake security has no Deny role type, and Owner fixed identity bypasses per-user role evaluation on SQL queries. Why the keyed choice wins: Defining Read Grant roles on `RoyaltiesLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access.
- **C:** Incorrect for this requirement. Incorrect: mixing pre-existing SQL granular access with Delegated mode forces 100% DirectQuery fallback instead of clean OneLake security evaluation. Why the keyed choice wins: Defining Read Grant roles on `RoyaltiesLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access.
- **D:** Incorrect for this requirement. Incorrect: Members bypass OneLake security, ReadWrite roles cannot contain RLS/CLS rules, and OneLake shortcuts do not use On-premises gateways. Why the keyed choice wins: Defining Read Grant roles on `RoyaltiesLakehouse`, assigning consumers Viewer + security roles, switching SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access.

### Question 9 — A, D

Answers: Define both the RLS filter and CLS column allow-list inside a single OneLake security Grant role with Read permission; Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN. Combining RLS and CLS inside one `Read` Grant OneLake security role avoids separate-role errors, and testing with `Test as role` + `partner1@cinewave.io` validates effective permissions. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Correct. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). In this scenario: Combining RLS and CLS inside one `Read` Grant OneLake security role avoids separate-role errors, and testing with `Test as role` + `partner1@cinewave.io` validates effective permissions.
- **B:** Incorrect for this requirement. OneLake security does not support combining an RLS role and a CLS role across separate roles on the same table; members assigned to that combination receive query errors. Why the keyed choice wins: Combining RLS and CLS inside one `Read` Grant OneLake security role avoids separate-role errors, and testing with `Test as role` + `partner1@cinewave.io` validates effective permissions.
- **C:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Combining RLS and CLS inside one `Read` Grant OneLake security role avoids separate-role errors, and testing with `Test as role` + `partner1@cinewave.io` validates effective permissions.
- **D:** Correct. OneLake security supports Grant roles only (Read permission required for RLS/CLS) and requires combining RLS and CLS on the same table within a single role — separate RLS and CLS roles on the same table return query errors. In this scenario: Combining RLS and CLS inside one `Read` Grant OneLake security role avoids separate-role errors, and testing with `Test as role` + `partner1@cinewave.io` validates effective permissions.
- **E:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: Combining RLS and CLS inside one `Read` Grant OneLake security role avoids separate-role errors, and testing with `Test as role` + `partner1@cinewave.io` validates effective permissions.

### Question 10 — B

Answer: Apply a Microsoft Purview sensitivity label with downstream inheritance on the source Lakehouse or Warehouse. Purview sensitivity-label downstream inheritance automatically propagates the Warehouse's label onto newly created semantic models and reports. Sensitivity labels applied to Fabric Lakehouses, Warehouses, and Semantic Models automatically propagate downstream to newly connected semantic models, reports, and exported Excel/PDF/PPTX files when inheritance is enabled. Local study-map skill 1.4 (Apply Microsoft Purview Sensitivity Labels, Inheritance, Default/Mandatory Policies, and Export Encryption), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Information protection & sensitivity labels in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-overview).

- **A:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Purview sensitivity-label downstream inheritance automatically propagates the Warehouse's label onto newly created semantic models and reports.
- **B:** Correct. Sensitivity labels applied to Fabric Lakehouses, Warehouses, and Semantic Models automatically propagate downstream to newly connected semantic models, reports, and exported Excel/PDF/PPTX files when inheritance is enabled. In this scenario: Purview sensitivity-label downstream inheritance automatically propagates the Warehouse's label onto newly created semantic models and reports.
- **C:** Incorrect for this requirement. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Why the keyed choice wins: Purview sensitivity-label downstream inheritance automatically propagates the Warehouse's label onto newly created semantic models and reports.
- **D:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Purview sensitivity-label downstream inheritance automatically propagates the Warehouse's label onto newly created semantic models and reports.

### Question 11 — D

Answer: Use a Purview sensitivity label configured with file encryption so exported .pbix, Excel, PDF, and PowerPoint files stay protected outside Fabric. Unencrypted labels only add visual metadata tags; configuring the Purview sensitivity label with file encryption enforces RMS access checks when `.xlsx`, `.pdf`, `.pptx`, or `.pbix` exports are opened externally. While sensitivity labels in Fabric classify items in the workspace without encrypting OneLake Delta storage itself, encryption-enabled labels enforce rights management automatically when users export data to Excel, PDF, PowerPoint, or .pbix. Local study-map skill 1.4 (Apply Microsoft Purview Sensitivity Labels, Inheritance, Default/Mandatory Policies, and Export Encryption), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Information protection & sensitivity labels in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-overview).

- **A:** Incorrect for this requirement. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Why the keyed choice wins: Unencrypted labels only add visual metadata tags; configuring the Purview sensitivity label with file encryption enforces RMS access checks when `.xlsx`, `.pdf`, `.pptx`, or `.pbix` exports are opened externally.
- **B:** Incorrect for this requirement. Item-level Read metadata permission lets a user connect to a Lakehouse or Warehouse item container without granting broad OneLake file access; combine with SELECT or OneLake security roles for granular least-privilege access. Why the keyed choice wins: Unencrypted labels only add visual metadata tags; configuring the Purview sensitivity label with file encryption enforces RMS access checks when `.xlsx`, `.pdf`, `.pptx`, or `.pbix` exports are opened externally.
- **C:** Incorrect for this requirement. Dynamic Data Masking obfuscates sensitive strings/emails/numbers in query results for users lacking UNMASK permission while keeping the column present so SELECT * queries do not fail. Why the keyed choice wins: Unencrypted labels only add visual metadata tags; configuring the Purview sensitivity label with file encryption enforces RMS access checks when `.xlsx`, `.pdf`, `.pptx`, or `.pbix` exports are opened externally.
- **D:** Correct. While sensitivity labels in Fabric classify items in the workspace without encrypting OneLake Delta storage itself, encryption-enabled labels enforce rights management automatically when users export data to Excel, PDF, PowerPoint, or .pbix. In this scenario: Unencrypted labels only add visual metadata tags; configuring the Purview sensitivity label with file encryption enforces RMS access checks when `.xlsx`, `.pdf`, `.pptx`, or `.pbix` exports are opened externally.

### Question 12 — C

Answer: Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal. `Certified` endorsement can only be granted by reviewers explicitly authorized in the Fabric Admin portal. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Local study-map skill 1.5 (Endorse Items Using Promoted, Certified, and Master Data Governance Badges), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Endorsement (Promoted, Certified, Master data) in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview).

- **A:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: `Certified` endorsement can only be granted by reviewers explicitly authorized in the Fabric Admin portal.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Certified` endorsement can only be granted by reviewers explicitly authorized in the Fabric Admin portal.
- **C:** Correct. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. In this scenario: `Certified` endorsement can only be granted by reviewers explicitly authorized in the Fabric Admin portal.
- **D:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: `Certified` endorsement can only be granted by reviewers explicitly authorized in the Fabric Admin portal.

### Question 13 — A

Answer: Configure Certified endorsement with the Master data label on authoritative core tables or semantic models. Applying `Certified` endorsement with `Master data` enabled designates authoritative core reference data assets in OneLake catalog. Fabric admins can enable Master data endorsement for authoritative single-source-of-truth silver/gold data assets so analysts distinguish core reference items in the OneLake catalog. Local study-map skill 1.5 (Endorse Items Using Promoted, Certified, and Master Data Governance Badges), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Endorsement (Promoted, Certified, Master data) in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview).

- **A:** Correct. Fabric admins can enable Master data endorsement for authoritative single-source-of-truth silver/gold data assets so analysts distinguish core reference items in the OneLake catalog. In this scenario: Applying `Certified` endorsement with `Master data` enabled designates authoritative core reference data assets in OneLake catalog.
- **B:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Applying `Certified` endorsement with `Master data` enabled designates authoritative core reference data assets in OneLake catalog.
- **C:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Applying `Certified` endorsement with `Master data` enabled designates authoritative core reference data assets in OneLake catalog.
- **D:** Incorrect for this requirement. Mandatory and default sensitivity label policies in Microsoft Purview require content creators to classify unlabeled semantic models and reports on save and apply baseline classification automatically. Why the keyed choice wins: Applying `Certified` endorsement with `Master data` enabled designates authoritative core reference data assets in OneLake catalog.

### Question 14 — C, E

Answers: Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions; Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch. Saving projects in `.pbip` (`TMDL` + `PBIR`) format exposes clean text diffs, and `Branch out` provisions isolated per-feature workspaces. Local study-map skill 1.7 (Create and Manage Power BI Desktop Projects (.pbip) with TMDL, PBIR, and .gitignore Hygiene), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Power BI Desktop projects (.pbip), TMDL, and PBIR (https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview).

- **A:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Saving projects in `.pbip` (`TMDL` + `PBIR`) format exposes clean text diffs, and `Branch out` provisions isolated per-feature workspaces.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Saving projects in `.pbip` (`TMDL` + `PBIR`) format exposes clean text diffs, and `Branch out` provisions isolated per-feature workspaces.
- **C:** Correct. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. In this scenario: Saving projects in `.pbip` (`TMDL` + `PBIR`) format exposes clean text diffs, and `Branch out` provisions isolated per-feature workspaces.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Saving projects in `.pbip` (`TMDL` + `PBIR`) format exposes clean text diffs, and `Branch out` provisions isolated per-feature workspaces.
- **E:** Correct. In Fabric Git integration, workspaces map 1-to-1 to branches; branching out into a dedicated developer workspace isolates in-progress notebook, pipeline, and semantic model edits before merging via pull request. In this scenario: Saving projects in `.pbip` (`TMDL` + `PBIR`) format exposes clean text diffs, and `Branch out` provisions isolated per-feature workspaces.

### Question 15 — A

Answer: Configure Deployment pipeline data source and parameter rules on the Test and Production stages. Configuring Deployment Pipeline data source rules on `AdTech-Prod` rebinds the `Direct Lake on SQL` semantic model to `ProdAttributionWarehouse` on every deployment. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Correct. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. In this scenario: Configuring Deployment Pipeline data source rules on `AdTech-Prod` rebinds the `Direct Lake on SQL` semantic model to `ProdAttributionWarehouse` on every deployment.
- **B:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Configuring Deployment Pipeline data source rules on `AdTech-Prod` rebinds the `Direct Lake on SQL` semantic model to `ProdAttributionWarehouse` on every deployment.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Configuring Deployment Pipeline data source rules on `AdTech-Prod` rebinds the `Direct Lake on SQL` semantic model to `ProdAttributionWarehouse` on every deployment.
- **D:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Configuring Deployment Pipeline data source rules on `AdTech-Prod` rebinds the `Direct Lake on SQL` semantic model to `ProdAttributionWarehouse` on every deployment.

### Question 16 — D

Answer: Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline. Assign `Podcast-Prod` to the `Production` pipeline stage and deploy backward into empty `Test` and `Development` workspaces. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. Selective deployment in Fabric Deployment Pipelines promotes only chosen items between stages, and Select related ensures newly referenced lakehouses or semantic models deploy alongside dependent reports. Why the keyed choice wins: Assign `Podcast-Prod` to the `Production` pipeline stage and deploy backward into empty `Test` and `Development` workspaces.
- **B:** Incorrect for this requirement. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Why the keyed choice wins: Assign `Podcast-Prod` to the `Production` pipeline stage and deploy backward into empty `Test` and `Development` workspaces.
- **C:** Incorrect for this requirement. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. Why the keyed choice wins: Assign `Podcast-Prod` to the `Production` pipeline stage and deploy backward into empty `Test` and `Development` workspaces.
- **D:** Correct. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. In this scenario: Assign `Podcast-Prod` to the `Production` pipeline stage and deploy backward into empty `Test` and `Development` workspaces.

### Question 17 — C

Answer: Use a Fabric Variable library (or autobinding across paired workspace items) to parameterize stage-specific environment references. A Fabric `Variable library` defines per-stage variable sets consumed across Deployment Pipeline environments. Fabric Variable libraries store stage-specific workspace/lakehouse IDs, URLs, and thresholds across Dev/Test/Prod — essential for items like Data Pipelines and Direct Lake on OneLake models that do not use legacy SQL deployment rules. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: A Fabric `Variable library` defines per-stage variable sets consumed across Deployment Pipeline environments.
- **B:** Incorrect for this requirement. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Why the keyed choice wins: A Fabric `Variable library` defines per-stage variable sets consumed across Deployment Pipeline environments.
- **C:** Correct. Fabric Variable libraries store stage-specific workspace/lakehouse IDs, URLs, and thresholds across Dev/Test/Prod — essential for items like Data Pipelines and Direct Lake on OneLake models that do not use legacy SQL deployment rules. In this scenario: A Fabric `Variable library` defines per-stage variable sets consumed across Deployment Pipeline environments.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: A Fabric `Variable library` defines per-stage variable sets consumed across Deployment Pipeline environments.

### Question 18 — B

Answer: Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts. Opening Workspace `Lineage` view, launching `Impact analysis` on `LegacyClickDataflow`, and selecting `Notify contacts` identifies cross-workspace dependents and messages owners. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Local study-map skill 1.9 (Perform Downstream Dependency Impact Analysis Across Lakehouses, Warehouses, Dataflows, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Lineage and impact analysis in Microsoft Fabric workspaces (https://learn.microsoft.com/en-us/fabric/governance/lineage).

- **A:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Opening Workspace `Lineage` view, launching `Impact analysis` on `LegacyClickDataflow`, and selecting `Notify contacts` identifies cross-workspace dependents and messages owners.
- **B:** Correct. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. In this scenario: Opening Workspace `Lineage` view, launching `Impact analysis` on `LegacyClickDataflow`, and selecting `Notify contacts` identifies cross-workspace dependents and messages owners.
- **C:** Incorrect for this requirement. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. Why the keyed choice wins: Opening Workspace `Lineage` view, launching `Impact analysis` on `LegacyClickDataflow`, and selecting `Notify contacts` identifies cross-workspace dependents and messages owners.
- **D:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: Opening Workspace `Lineage` view, launching `Impact analysis` on `LegacyClickDataflow`, and selecting `Notify contacts` identifies cross-workspace dependents and messages owners.

### Question 19 — C

Answer: Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts. `Lineage` view maps upstream-to-downstream item dependencies alongside refresh statuses so engineers spot the exact broken upstream link immediately. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Local study-map skill 1.9 (Perform Downstream Dependency Impact Analysis Across Lakehouses, Warehouses, Dataflows, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Lineage and impact analysis in Microsoft Fabric workspaces (https://learn.microsoft.com/en-us/fabric/governance/lineage).

- **A:** Incorrect for this requirement. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Why the keyed choice wins: `Lineage` view maps upstream-to-downstream item dependencies alongside refresh statuses so engineers spot the exact broken upstream link immediately.
- **B:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: `Lineage` view maps upstream-to-downstream item dependencies alongside refresh statuses so engineers spot the exact broken upstream link immediately.
- **C:** Correct. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. In this scenario: `Lineage` view maps upstream-to-downstream item dependencies alongside refresh statuses so engineers spot the exact broken upstream link immediately.
- **D:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: `Lineage` view maps upstream-to-downstream item dependencies alongside refresh statuses so engineers spot the exact broken upstream link immediately.

### Question 20 — A

Answer: Verify XMLA Endpoint = Read Write on target capacity → Connect ALM Toolkit to Dev source and Prod XMLA target → Compare schemas while hiding unchanged partitions and keeping Prod data sources → Validate and deploy metadata-only TMSL changes. Ensuring `XMLA Endpoint = Read Write`, comparing Dev vs Prod in ALM Toolkit while hiding unchanged partitions and preserving Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing. Correct order: confirm Read Write XMLA capacity setting, compare Dev vs Prod models, preserve Prod partition state and data-source bindings, and push metadata-only measure/relationship diffs. Local study-map skill 1.10 (Deploy and Manage Semantic Models Using the XMLA Endpoint (Read-Write, TMSL, Tabular Editor, ALM Toolkit)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model connectivity and management with the XMLA endpoint (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools).

- **A:** Correct. Correct order: confirm Read Write XMLA capacity setting, compare Dev vs Prod models, preserve Prod partition state and data-source bindings, and push metadata-only measure/relationship diffs. In this scenario: Ensuring `XMLA Endpoint = Read Write`, comparing Dev vs Prod in ALM Toolkit while hiding unchanged partitions and preserving Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing.
- **B:** Incorrect for this requirement. Incorrect: DAX Studio is a query/profiling tool (not a model-deployment tool), and unversioned Production hotfixes cause immediate drift on next deployment. Why the keyed choice wins: Ensuring `XMLA Endpoint = Read Write`, comparing Dev vs Prod in ALM Toolkit while hiding unchanged partitions and preserving Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing.
- **C:** Incorrect for this requirement. Incorrect: Read Only XMLA rejects TMSL model deployments, and Capacity Admin rights violate least privilege. Why the keyed choice wins: Ensuring `XMLA Endpoint = Read Write`, comparing Dev vs Prod in ALM Toolkit while hiding unchanged partitions and preserving Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing.
- **D:** Incorrect for this requirement. Incorrect: XMLA Off blocks external deployment, and overwriting Production with an unpartitioned file destroys incremental partitions and causes prolonged outage. Why the keyed choice wins: Ensuring `XMLA Endpoint = Read Write`, comparing Dev vs Prod in ALM Toolkit while hiding unchanged partitions and preserving Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing.

### Question 21 — C, E

Answers: Enable XMLA Endpoint = Read Write in Fabric Capacity workload settings and connect to powerbi://api.powerbi.com/v1.0/myorg/<WorkspaceName>; {"refresh": {"type": "dataOnly", "objects": [{"database": "WealthModel", "table": "FactPositions", "partition": "2026M10"}]}}. Enabling `XMLA Endpoint = Read Write` on the capacity and issuing a partition-scoped TMSL `dataOnly` refresh reloads only partition `2026M10`. Local study-map skill 1.10 (Deploy and Manage Semantic Models Using the XMLA Endpoint (Read-Write, TMSL, Tabular Editor, ALM Toolkit)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model connectivity and management with the XMLA endpoint (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools).

- **A:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Enabling `XMLA Endpoint = Read Write` on the capacity and issuing a partition-scoped TMSL `dataOnly` refresh reloads only partition `2026M10`.
- **B:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: Enabling `XMLA Endpoint = Read Write` on the capacity and issuing a partition-scoped TMSL `dataOnly` refresh reloads only partition `2026M10`.
- **C:** Correct. A TMSL refresh command with type = "dataOnly" scoped to a single partition reloads raw partition data over XMLA without rebuilding global relationships or calculated tables. In this scenario: Enabling `XMLA Endpoint = Read Write` on the capacity and issuing a partition-scoped TMSL `dataOnly` refresh reloads only partition `2026M10`.
- **D:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Enabling `XMLA Endpoint = Read Write` on the capacity and issuing a partition-scoped TMSL `dataOnly` refresh reloads only partition `2026M10`.
- **E:** Correct. External ALM tools (Tabular Editor, SSMS, ALM Toolkit, SqlPackage/PowerShell Invoke-ASCmd) require workspace Fabric/Premium capacity with XMLA Endpoint set to Read Write to deploy or modify semantic models. In this scenario: Enabling `XMLA Endpoint = Read Write` on the capacity and issuing a partition-scoped TMSL `dataOnly` refresh reloads only partition `2026M10`.

### Question 22 — B

Answer: Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode. A Power BI Data Source (`.pbids`) file preconfigures the connector and endpoint URL cleanly with zero report visuals or data. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Local study-map skill 1.11 (Create and Update Reusable Assets (.pbit Templates, .pbids Data Sources, and Shared Golden Semantic Models)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create and use report templates (.pbit), data sources (.pbids), and shared semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-templates).

- **A:** Incorrect for this requirement. Decoupling a shared golden semantic model from thin live-connected reports prevents measure duplication, reduces capacity memory footprint, and enforces centralized RLS/endorsement across teams. Why the keyed choice wins: A Power BI Data Source (`.pbids`) file preconfigures the connector and endpoint URL cleanly with zero report visuals or data.
- **B:** Correct. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. In this scenario: A Power BI Data Source (`.pbids`) file preconfigures the connector and endpoint URL cleanly with zero report visuals or data.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: A Power BI Data Source (`.pbids`) file preconfigures the connector and endpoint URL cleanly with zero report visuals or data.
- **D:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: A Power BI Data Source (`.pbids`) file preconfigures the connector and endpoint URL cleanly with zero report visuals or data.

### Question 23 — C

Answer: Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows. Exporting a Power BI Template (`.pbit`) strips all data rows while preserving report pages, DAX measures, schema, and parameter prompts. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Local study-map skill 1.11 (Create and Update Reusable Assets (.pbit Templates, .pbids Data Sources, and Shared Golden Semantic Models)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create and use report templates (.pbit), data sources (.pbids), and shared semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-templates).

- **A:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Exporting a Power BI Template (`.pbit`) strips all data rows while preserving report pages, DAX measures, schema, and parameter prompts.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Exporting a Power BI Template (`.pbit`) strips all data rows while preserving report pages, DAX measures, schema, and parameter prompts.
- **C:** Correct. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. In this scenario: Exporting a Power BI Template (`.pbit`) strips all data rows while preserving report pages, DAX measures, schema, and parameter prompts.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Exporting a Power BI Template (`.pbit`) strips all data rows while preserving report pages, DAX measures, schema, and parameter prompts.

### Question 24 — C

Answer: Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet. A Fabric `Virtual Network (VNet) data gateway` injected into a delegated subnet of `vnet-media-core` provides serverless private connectivity. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. Local study-map skill 2.1 (Create Data Connections (Shareable Cloud Connections, On-Premises Gateways, and VNet Data Gateways)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data source management, cloud connections, and VNet/on-premises gateways in Fabric (https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management).

- **A:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: A Fabric `Virtual Network (VNet) data gateway` injected into a delegated subnet of `vnet-media-core` provides serverless private connectivity.
- **B:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: A Fabric `Virtual Network (VNet) data gateway` injected into a delegated subnet of `vnet-media-core` provides serverless private connectivity.
- **C:** Correct. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. In this scenario: A Fabric `Virtual Network (VNet) data gateway` injected into a delegated subnet of `vnet-media-core` provides serverless private connectivity.
- **D:** Incorrect for this requirement. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. Why the keyed choice wins: A Fabric `Virtual Network (VNet) data gateway` injected into a delegated subnet of `vnet-media-core` provides serverless private connectivity.

### Question 25 — A

Answer: Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication. Creating a `Shareable cloud connection` in `Manage connections and gateways` stores credentials centrally and shares scoped `Use` access with pipeline authors. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. Local study-map skill 2.1 (Create Data Connections (Shareable Cloud Connections, On-Premises Gateways, and VNet Data Gateways)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data source management, cloud connections, and VNet/on-premises gateways in Fabric (https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management).

- **A:** Correct. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. In this scenario: Creating a `Shareable cloud connection` in `Manage connections and gateways` stores credentials centrally and shares scoped `Use` access with pipeline authors.
- **B:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Creating a `Shareable cloud connection` in `Manage connections and gateways` stores credentials centrally and shares scoped `Use` access with pipeline authors.
- **C:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Creating a `Shareable cloud connection` in `Manage connections and gateways` stores credentials centrally and shares scoped `Use` access with pipeline authors.
- **D:** Incorrect for this requirement. With SSO enabled on a Direct Lake model, Fabric evaluates data permissions at the underlying SQL analytics endpoint or OneLake security layer using each viewing report consumer's own Microsoft Entra identity. Why the keyed choice wins: Creating a `Shareable cloud connection` in `Manage connections and gateways` stores credentials centrally and shares scoped `Use` access with pipeline authors.

### Question 26 — B

Answer: Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture. `OneLake catalog` unifies tenant-wide item discovery (`Explore`) and stewardship posture management (`Govern`). OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Local study-map skill 2.2 (Discover Data and Streams Using OneLake Catalog (Explore/Govern) and Real-Time Hub + Activator), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake catalog overview & Real-Time hub in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview).

- **A:** Incorrect for this requirement. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Why the keyed choice wins: `OneLake catalog` unifies tenant-wide item discovery (`Explore`) and stewardship posture management (`Govern`).
- **B:** Correct. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. In this scenario: `OneLake catalog` unifies tenant-wide item discovery (`Explore`) and stewardship posture management (`Govern`).
- **C:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `OneLake catalog` unifies tenant-wide item discovery (`Explore`) and stewardship posture management (`Govern`).
- **D:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: `OneLake catalog` unifies tenant-wide item discovery (`Explore`) and stewardship posture management (`Govern`).

### Question 27 — C, E

Answers: Use the Real-Time hub to subscribe to Microsoft.Fabric.OneLake.FileCreated events (or Capacity/CDC streams) and trigger an Activator rule; Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table. `Real-Time hub` discovers streams and capacity events for Activator alerts, while `Eventstream` ingests and routes live player telemetry. Local study-map skill 2.2 (Discover Data and Streams Using OneLake Catalog (Explore/Govern) and Real-Time Hub + Activator), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake catalog overview & Real-Time hub in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview).

- **A:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: `Real-Time hub` discovers streams and capacity events for Activator alerts, while `Eventstream` ingests and routes live player telemetry.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Real-Time hub` discovers streams and capacity events for Activator alerts, while `Eventstream` ingests and routes live player telemetry.
- **C:** Correct. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. In this scenario: `Real-Time hub` discovers streams and capacity events for Activator alerts, while `Eventstream` ingests and routes live player telemetry.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `Real-Time hub` discovers streams and capacity events for Activator alerts, while `Eventstream` ingests and routes live player telemetry.
- **E:** Correct. Real-Time hub unifies streaming sources, CDC feeds, Azure Blob events, and Fabric workspace/OneLake/Capacity events so analytics engineers can discover streams in one catalog and trigger event-driven pipelines or Notebooks via Activator. In this scenario: `Real-Time hub` discovers streams and capacity events for Activator alerts, while `Eventstream` ingests and routes live player telemetry.

### Question 28 — C

Answer: Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching. Creating an external `OneLake shortcut` to the Amazon S3 bucket virtualizes those tables directly into OneLake without batch copy pipelines. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: Creating an external `OneLake shortcut` to the Amazon S3 bucket virtualizes those tables directly into OneLake without batch copy pipelines.
- **B:** Incorrect for this requirement. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. Why the keyed choice wins: Creating an external `OneLake shortcut` to the Amazon S3 bucket virtualizes those tables directly into OneLake without batch copy pipelines.
- **C:** Correct. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. In this scenario: Creating an external `OneLake shortcut` to the Amazon S3 bucket virtualizes those tables directly into OneLake without batch copy pipelines.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Creating an external `OneLake shortcut` to the Amazon S3 bucket virtualizes those tables directly into OneLake without batch copy pipelines.

### Question 29 — A, B, C

Answers: Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog; Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching; Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table. `Database Mirroring` replicates Cosmos DB CDC, external `OneLake shortcuts` virtualize GCS Parquet, and `Eventstream` ingests live Kafka events. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Correct. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. In this scenario: `Database Mirroring` replicates Cosmos DB CDC, external `OneLake shortcuts` virtualize GCS Parquet, and `Eventstream` ingests live Kafka events.
- **B:** Correct. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. In this scenario: `Database Mirroring` replicates Cosmos DB CDC, external `OneLake shortcuts` virtualize GCS Parquet, and `Eventstream` ingests live Kafka events.
- **C:** Correct. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. In this scenario: `Database Mirroring` replicates Cosmos DB CDC, external `OneLake shortcuts` virtualize GCS Parquet, and `Eventstream` ingests live Kafka events.
- **D:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `Database Mirroring` replicates Cosmos DB CDC, external `OneLake shortcuts` virtualize GCS Parquet, and `Eventstream` ingests live Kafka events.
- **E:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `Database Mirroring` replicates Cosmos DB CDC, external `OneLake shortcuts` virtualize GCS Parquet, and `Eventstream` ingests live Kafka events.
- **F:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Database Mirroring` replicates Cosmos DB CDC, external `OneLake shortcuts` virtualize GCS Parquet, and `Eventstream` ingests live Kafka events.

### Question 30 — B

Answer: Choose a Fabric Eventhouse (KQL database). `Fabric Eventhouse` (KQL database) is engineered for multi-million-event-per-second streaming time-series and JSON log analytics. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Incorrect for this requirement. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) is engineered for multi-million-event-per-second streaming time-series and JSON log analytics.
- **B:** Correct. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. In this scenario: `Fabric Eventhouse` (KQL database) is engineered for multi-million-event-per-second streaming time-series and JSON log analytics.
- **C:** Incorrect for this requirement. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) is engineered for multi-million-event-per-second streaming time-series and JSON log analytics.
- **D:** Incorrect for this requirement. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) is engineered for multi-million-event-per-second streaming time-series and JSON log analytics.

### Question 31 — D

Answer: Choose a Fabric Lakehouse. `Fabric Lakehouse` natively combines unstructured `Files/` storage and Spark-managed Delta `Tables/` with a read-only SQL analytics endpoint. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Incorrect for this requirement. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. Why the keyed choice wins: `Fabric Lakehouse` natively combines unstructured `Files/` storage and Spark-managed Delta `Tables/` with a read-only SQL analytics endpoint.
- **B:** Incorrect for this requirement. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Why the keyed choice wins: `Fabric Lakehouse` natively combines unstructured `Files/` storage and Spark-managed Delta `Tables/` with a read-only SQL analytics endpoint.
- **C:** Incorrect for this requirement. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. Why the keyed choice wins: `Fabric Lakehouse` natively combines unstructured `Files/` storage and Spark-managed Delta `Tables/` with a read-only SQL analytics endpoint.
- **D:** Correct. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. In this scenario: `Fabric Lakehouse` natively combines unstructured `Files/` storage and Spark-managed Delta `Tables/` with a read-only SQL analytics endpoint.

### Question 32 — A, D

Answers: Choose a Fabric Data Warehouse; Choose a SQL database in Microsoft Fabric. `Fabric Data Warehouse` serves transactional T-SQL analytical star schemas, while `SQL database in Microsoft Fabric` hosts operational OLTP workloads auto-mirrored to OneLake. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Correct. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. In this scenario: `Fabric Data Warehouse` serves transactional T-SQL analytical star schemas, while `SQL database in Microsoft Fabric` hosts operational OLTP workloads auto-mirrored to OneLake.
- **B:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: `Fabric Data Warehouse` serves transactional T-SQL analytical star schemas, while `SQL database in Microsoft Fabric` hosts operational OLTP workloads auto-mirrored to OneLake.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Fabric Data Warehouse` serves transactional T-SQL analytical star schemas, while `SQL database in Microsoft Fabric` hosts operational OLTP workloads auto-mirrored to OneLake.
- **D:** Correct. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. In this scenario: `Fabric Data Warehouse` serves transactional T-SQL analytical star schemas, while `SQL database in Microsoft Fabric` hosts operational OLTP workloads auto-mirrored to OneLake.
- **E:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `Fabric Data Warehouse` serves transactional T-SQL analytical star schemas, while `SQL database in Microsoft Fabric` hosts operational OLTP workloads auto-mirrored to OneLake.

### Question 33 — A

Answer: Enable OneLake availability on the Eventhouse KQL database (or specific KQL table) and create an internal OneLake shortcut in the Lakehouse. Enabling `OneLake availability` on the Eventhouse KQL database/table writes synced Delta Parquet files into OneLake. KQL databases do not write Delta Parquet to OneLake by default; turning on OneLake availability creates a synced Delta Parquet logical representation in OneLake that Spark, SQL analytics endpoints, and Direct Lake on OneLake models can read without data movement. Local study-map skill 2.5 (Implement OneLake Integration for Eventhouse (OneLake Availability) and Import Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Eventhouse OneLake availability & OneLake integration for semantic models (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/one-lake-availability).

- **A:** Correct. KQL databases do not write Delta Parquet to OneLake by default; turning on OneLake availability creates a synced Delta Parquet logical representation in OneLake that Spark, SQL analytics endpoints, and Direct Lake on OneLake models can read without data movement. In this scenario: Enabling `OneLake availability` on the Eventhouse KQL database/table writes synced Delta Parquet files into OneLake.
- **B:** Incorrect for this requirement. Eventhouse KQL databases do not write Delta Parquet to OneLake unless OneLake availability is enabled, and Direct Lake on SQL does not support KQL databases (only Direct Lake on OneLake does once OneLake availability is on). Why the keyed choice wins: Enabling `OneLake availability` on the Eventhouse KQL database/table writes synced Delta Parquet files into OneLake.
- **C:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Enabling `OneLake availability` on the Eventhouse KQL database/table writes synced Delta Parquet files into OneLake.
- **D:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Enabling `OneLake availability` on the Eventhouse KQL database/table writes synced Delta Parquet files into OneLake.

### Question 34 — C

Answer: Ingest streaming telemetry into an Eventhouse KQL database → Enable OneLake availability on the KQL database or table → Create an internal OneLake shortcut in the Lakehouse → Add the table to a Direct Lake on OneLake semantic model. Streaming into Eventhouse, enabling `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and modeling with `Direct Lake on OneLake` integrates real-time telemetry cleanly. Correct order: land streaming events in Eventhouse, opt in to OneLake availability so Delta Parquet files sync to OneLake, surface via Lakehouse shortcut (or connect directly), and model with Direct Lake on OneLake. Local study-map skill 2.5 (Implement OneLake Integration for Eventhouse (OneLake Availability) and Import Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Eventhouse OneLake availability & OneLake integration for semantic models (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/one-lake-availability).

- **A:** Incorrect for this requirement. Incorrect: manual hourly CSV exports add latency, operational toil, and duplicate storage instead of native Eventhouse OneLake availability. Why the keyed choice wins: Streaming into Eventhouse, enabling `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and modeling with `Direct Lake on OneLake` integrates real-time telemetry cleanly.
- **B:** Incorrect for this requirement. Incorrect: Direct Lake on SQL does not support KQL databases, disabling OneLake availability prevents Delta Parquet generation, and Direct Lake never uses gateways. Why the keyed choice wins: Streaming into Eventhouse, enabling `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and modeling with `Direct Lake on OneLake` integrates real-time telemetry cleanly.
- **C:** Correct. Correct order: land streaming events in Eventhouse, opt in to OneLake availability so Delta Parquet files sync to OneLake, surface via Lakehouse shortcut (or connect directly), and model with Direct Lake on OneLake. In this scenario: Streaming into Eventhouse, enabling `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and modeling with `Direct Lake on OneLake` integrates real-time telemetry cleanly.
- **D:** Incorrect for this requirement. Incorrect: KQL tables are internal OneLake sources that only expose Delta Parquet folders after OneLake availability is enabled. Why the keyed choice wins: Streaming into Eventhouse, enabling `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and modeling with `Direct Lake on OneLake` integrates real-time telemetry cleanly.

### Question 35 — C

Answer: Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic. `Fabric Data Warehouse` supports full T-SQL procedural ELT with `CREATE PROCEDURE` and multi-table DML writes. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `Fabric Data Warehouse` supports full T-SQL procedural ELT with `CREATE PROCEDURE` and multi-table DML writes.
- **B:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `Fabric Data Warehouse` supports full T-SQL procedural ELT with `CREATE PROCEDURE` and multi-table DML writes.
- **C:** Correct. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. In this scenario: `Fabric Data Warehouse` supports full T-SQL procedural ELT with `CREATE PROCEDURE` and multi-table DML writes.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Fabric Data Warehouse` supports full T-SQL procedural ELT with `CREATE PROCEDURE` and multi-table DML writes.

### Question 36 — B

Answer: Use a Lakehouse Materialized Lake View (or persisted Gold Delta table) instead of a non-materialized SQL analytics endpoint view for Direct Lake on OneLake. `Direct Lake on OneLake` requires Delta Parquet tables in OneLake rather than non-materialized SQL views; materializing the logic as a Lakehouse `Materialized Lake View` or Gold Delta table enables pure Direct Lake loading. Non-materialized SQL analytics endpoint views cannot back Direct Lake on OneLake tables and force Direct Lake on SQL into DirectQuery fallback; materializing the view as a Delta table preserves pure in-memory Direct Lake speed. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: `Direct Lake on OneLake` requires Delta Parquet tables in OneLake rather than non-materialized SQL views; materializing the logic as a Lakehouse `Materialized Lake View` or Gold Delta table enables pure Direct Lake loading.
- **B:** Correct. Non-materialized SQL analytics endpoint views cannot back Direct Lake on OneLake tables and force Direct Lake on SQL into DirectQuery fallback; materializing the view as a Delta table preserves pure in-memory Direct Lake speed. In this scenario: `Direct Lake on OneLake` requires Delta Parquet tables in OneLake rather than non-materialized SQL views; materializing the logic as a Lakehouse `Materialized Lake View` or Gold Delta table enables pure Direct Lake loading.
- **C:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: `Direct Lake on OneLake` requires Delta Parquet tables in OneLake rather than non-materialized SQL views; materializing the logic as a Lakehouse `Materialized Lake View` or Gold Delta table enables pure Direct Lake loading.
- **D:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Direct Lake on OneLake` requires Delta Parquet tables in OneLake rather than non-materialized SQL views; materializing the logic as a Lakehouse `Materialized Lake View` or Gold Delta table enables pure Direct Lake loading.

### Question 37 — B

Answer: Use T-SQL GRANT/DENY SELECT on specific Warehouse schemas, tables, or views. Object-level security via T-SQL `GRANT` on curated views and `DENY` (or withholding grants) on raw base tables governs object access inside the Warehouse. Object-level security in Fabric Warehouse or SQL analytics endpoints controls visibility and query access to entire tables, views, or stored procedures using standard T-SQL GRANT and DENY permissions. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Object-level security via T-SQL `GRANT` on curated views and `DENY` (or withholding grants) on raw base tables governs object access inside the Warehouse.
- **B:** Correct. Object-level security in Fabric Warehouse or SQL analytics endpoints controls visibility and query access to entire tables, views, or stored procedures using standard T-SQL GRANT and DENY permissions. In this scenario: Object-level security via T-SQL `GRANT` on curated views and `DENY` (or withholding grants) on raw base tables governs object access inside the Warehouse.
- **C:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Object-level security via T-SQL `GRANT` on curated views and `DENY` (or withholding grants) on raw base tables governs object access inside the Warehouse.
- **D:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Object-level security via T-SQL `GRANT` on curated views and `DENY` (or withholding grants) on raw base tables governs object access inside the Warehouse.

### Question 38 — D

Answer: Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions. Generating an integer surrogate key (`TitleKey`) mapped to `(CatalogSource, NaturalTitleId)` prevents cross-catalog collisions and compresses optimal integer foreign keys. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Generating an integer surrogate key (`TitleKey`) mapped to `(CatalogSource, NaturalTitleId)` prevents cross-catalog collisions and compresses optimal integer foreign keys.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Generating an integer surrogate key (`TitleKey`) mapped to `(CatalogSource, NaturalTitleId)` prevents cross-catalog collisions and compresses optimal integer foreign keys.
- **C:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: Generating an integer surrogate key (`TitleKey`) mapped to `(CatalogSource, NaturalTitleId)` prevents cross-catalog collisions and compresses optimal integer foreign keys.
- **D:** Correct. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. In this scenario: Generating an integer surrogate key (`TitleKey`) mapped to `(CatalogSource, NaturalTitleId)` prevents cross-catalog collisions and compresses optimal integer foreign keys.

### Question 39 — B

Answer: Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes. Building a conformed Gold `DimBroadcastCalendar` table with contiguous daily grain and broadcast week/month/quarter columns standardizes time intelligence across facts. A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: Building a conformed Gold `DimBroadcastCalendar` table with contiguous daily grain and broadcast week/month/quarter columns standardizes time intelligence across facts.
- **B:** Correct. A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering. In this scenario: Building a conformed Gold `DimBroadcastCalendar` table with contiguous daily grain and broadcast week/month/quarter columns standardizes time intelligence across facts.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Building a conformed Gold `DimBroadcastCalendar` table with contiguous daily grain and broadcast week/month/quarter columns standardizes time intelligence across facts.
- **D:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Building a conformed Gold `DimBroadcastCalendar` table with contiguous daily grain and broadcast week/month/quarter columns standardizes time intelligence across facts.

### Question 40 — B, D

Answers: Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs; Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions. Native Catalyst `pyspark.sql.functions` inside `.withColumn()` avoid Python UDF serialization bottlenecks, and integer surrogate keys shrink downstream Gold fact joins. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Native Catalyst `pyspark.sql.functions` inside `.withColumn()` avoid Python UDF serialization bottlenecks, and integer surrogate keys shrink downstream Gold fact joins.
- **B:** Correct. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. In this scenario: Native Catalyst `pyspark.sql.functions` inside `.withColumn()` avoid Python UDF serialization bottlenecks, and integer surrogate keys shrink downstream Gold fact joins.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Native Catalyst `pyspark.sql.functions` inside `.withColumn()` avoid Python UDF serialization bottlenecks, and integer surrogate keys shrink downstream Gold fact joins.
- **D:** Correct. Native Catalyst/Photon-optimized pyspark.sql.functions execute in vectorized JVM/native code across partitions, avoiding the severe Python serialization bottleneck of row-level UDFs. In this scenario: Native Catalyst `pyspark.sql.functions` inside `.withColumn()` avoid Python UDF serialization bottlenecks, and integer surrogate keys shrink downstream Gold fact joins.
- **E:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Native Catalyst `pyspark.sql.functions` inside `.withColumn()` avoid Python UDF serialization bottlenecks, and integer surrogate keys shrink downstream Gold fact joins.

### Question 41 — A

Answer: Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns. `SCD Type 2` versions subscriber tier transitions with new surrogate keys and effective date intervals so historical watch facts retain point-in-time plan attribution. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Correct. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. In this scenario: `SCD Type 2` versions subscriber tier transitions with new surrogate keys and effective date intervals so historical watch facts retain point-in-time plan attribution.
- **B:** Incorrect for this requirement. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Why the keyed choice wins: `SCD Type 2` versions subscriber tier transitions with new surrogate keys and effective date intervals so historical watch facts retain point-in-time plan attribution.
- **C:** Incorrect for this requirement. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Why the keyed choice wins: `SCD Type 2` versions subscriber tier transitions with new surrogate keys and effective date intervals so historical watch facts retain point-in-time plan attribution.
- **D:** Incorrect for this requirement. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Why the keyed choice wins: `SCD Type 2` versions subscriber tier transitions with new surrogate keys and effective date intervals so historical watch facts retain point-in-time plan attribution.

### Question 42 — D

Answer: Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place. `SCD Type 1` updates `TitleName` in place on the existing surrogate key so all historical and future sessions display the corrected title. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. Why the keyed choice wins: `SCD Type 1` updates `TitleName` in place on the existing surrogate key so all historical and future sessions display the corrected title.
- **B:** Incorrect for this requirement. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. Why the keyed choice wins: `SCD Type 1` updates `TitleName` in place on the existing surrogate key so all historical and future sessions display the corrected title.
- **C:** Incorrect for this requirement. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. Why the keyed choice wins: `SCD Type 1` updates `TitleName` in place on the existing surrogate key so all historical and future sessions display the corrected title.
- **D:** Correct. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. In this scenario: `SCD Type 1` updates `TitleName` in place on the existing surrogate key so all historical and future sessions display the corrected title.

### Question 43 — B

Answer: Stage and deduplicate incoming records by natural key → Compare tracked attributes against active (IsCurrent = 1) Gold rows → Expire changed active rows (EffectiveEndDate, IsCurrent = 0) → Insert new active versions with fresh surrogate keys. Deduplicating staged agencies, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves historical accuracy. Correct order: deduplicate staging first, detect attribute changes against current rows, close out prior active intervals without losing their surrogate keys, and insert new active versions. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. Incorrect: regenerating surrogate keys on truncate breaks every existing historical fact foreign key, and marking multiple rows IsCurrent = 1 duplicates fact joins. Why the keyed choice wins: Deduplicating staged agencies, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves historical accuracy.
- **B:** Correct. Correct order: deduplicate staging first, detect attribute changes against current rows, close out prior active intervals without losing their surrogate keys, and insert new active versions. In this scenario: Deduplicating staged agencies, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves historical accuracy.
- **C:** Incorrect for this requirement. Incorrect: deleting unmatched keys and enabling Assume referential integrity omits orphan rows silently in INNER JOINs. Why the keyed choice wins: Deduplicating staged agencies, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves historical accuracy.
- **D:** Incorrect for this requirement. Incorrect: new versions must be active (IsCurrent = 1), EffectiveStartDate of historical intervals must remain immutable, and natural keys are required to match future CDC updates. Why the keyed choice wins: Deduplicating staged agencies, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active rows with fresh surrogate keys preserves historical accuracy.

### Question 44 — A, C, F

Answers: Organize OneLake into Bronze (raw immutable), Silver (validated, deduplicated, conformed), and Gold (star-schema dimensions and facts with V-Order); Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures; Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE. Organizing Bronze/Silver/Gold Medallion zones, enforcing uniform single-impression (or daily-campaign) atomic grain, and mapping unmatched foreign keys to `-1` Unknown rows keep star joins clean. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Correct. Keeping fact tables at a single, consistent atomic grain with integer foreign keys and additive measures eliminates double-counting and supports flexible rollups across every conformed dimension. In this scenario: Organizing Bronze/Silver/Gold Medallion zones, enforcing uniform single-impression (or daily-campaign) atomic grain, and mapping unmatched foreign keys to `-1` Unknown rows keep star joins clean.
- **B:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Organizing Bronze/Silver/Gold Medallion zones, enforcing uniform single-impression (or daily-campaign) atomic grain, and mapping unmatched foreign keys to `-1` Unknown rows keep star joins clean.
- **C:** Correct. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. In this scenario: Organizing Bronze/Silver/Gold Medallion zones, enforcing uniform single-impression (or daily-campaign) atomic grain, and mapping unmatched foreign keys to `-1` Unknown rows keep star joins clean.
- **D:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Organizing Bronze/Silver/Gold Medallion zones, enforcing uniform single-impression (or daily-campaign) atomic grain, and mapping unmatched foreign keys to `-1` Unknown rows keep star joins clean.
- **E:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Organizing Bronze/Silver/Gold Medallion zones, enforcing uniform single-impression (or daily-campaign) atomic grain, and mapping unmatched foreign keys to `-1` Unknown rows keep star joins clean.
- **F:** Correct. The Medallion architecture separates raw source fidelity (Bronze), enterprise data quality/conformance (Silver), and BI/Direct Lake star-schema consumption (Gold). In this scenario: Organizing Bronze/Silver/Gold Medallion zones, enforcing uniform single-impression (or daily-campaign) atomic grain, and mapping unmatched foreign keys to `-1` Unknown rows keep star joins clean.

### Question 45 — B

Answer: Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension. Denormalizing `SeasonNumber`, `SeriesTitle`, `FranchiseName`, and `GenreName` directly onto a single flattened `Gold.DimContent` table eliminates four snowflake hops. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Local study-map skill 2.9 (Denormalize Snowflake Hierarchies into Flattened Gold Dimension Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Dimensional modeling & denormalizing snowflake tables in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables).

- **A:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Denormalizing `SeasonNumber`, `SeriesTitle`, `FranchiseName`, and `GenreName` directly onto a single flattened `Gold.DimContent` table eliminates four snowflake hops.
- **B:** Correct. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. In this scenario: Denormalizing `SeasonNumber`, `SeriesTitle`, `FranchiseName`, and `GenreName` directly onto a single flattened `Gold.DimContent` table eliminates four snowflake hops.
- **C:** Incorrect for this requirement. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Why the keyed choice wins: Denormalizing `SeasonNumber`, `SeriesTitle`, `FranchiseName`, and `GenreName` directly onto a single flattened `Gold.DimContent` table eliminates four snowflake hops.
- **D:** Incorrect for this requirement. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Why the keyed choice wins: Denormalizing `SeasonNumber`, `SeriesTitle`, `FranchiseName`, and `GenreName` directly onto a single flattened `Gold.DimContent` table eliminates four snowflake hops.

### Question 46 — A

Answer: Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension. Eliminating snowflaked dimension chains removes chained relationship joins during `xmSQL` / Direct Lake queries and keeps all advertiser hierarchy levels in one table for drill-down visuals. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Local study-map skill 2.9 (Denormalize Snowflake Hierarchies into Flattened Gold Dimension Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Dimensional modeling & denormalizing snowflake tables in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables).

- **A:** Correct. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. In this scenario: Eliminating snowflaked dimension chains removes chained relationship joins during `xmSQL` / Direct Lake queries and keeps all advertiser hierarchy levels in one table for drill-down visuals.
- **B:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Eliminating snowflaked dimension chains removes chained relationship joins during `xmSQL` / Direct Lake queries and keeps all advertiser hierarchy levels in one table for drill-down visuals.
- **C:** Incorrect for this requirement. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. Why the keyed choice wins: Eliminating snowflaked dimension chains removes chained relationship joins during `xmSQL` / Direct Lake queries and keeps all advertiser hierarchy levels in one table for drill-down visuals.
- **D:** Incorrect for this requirement. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. Why the keyed choice wins: Eliminating snowflaked dimension chains removes chained relationship joins during `xmSQL` / Direct Lake queries and keeps all advertiser hierarchy levels in one table for drill-down visuals.

### Question 47 — D

Answer: Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP). Materializing a pre-aggregated `FactDailyTitleStreamSummary` Gold Delta table reduces 25 billion pings to compact daily rows tailored to executive scorecards. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Materializing a pre-aggregated `FactDailyTitleStreamSummary` Gold Delta table reduces 25 billion pings to compact daily rows tailored to executive scorecards.
- **B:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Materializing a pre-aggregated `FactDailyTitleStreamSummary` Gold Delta table reduces 25 billion pings to compact daily rows tailored to executive scorecards.
- **C:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Materializing a pre-aggregated `FactDailyTitleStreamSummary` Gold Delta table reduces 25 billion pings to compact daily rows tailored to executive scorecards.
- **D:** Correct. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. In this scenario: Materializing a pre-aggregated `FactDailyTitleStreamSummary` Gold Delta table reduces 25 billion pings to compact daily rows tailored to executive scorecards.

### Question 48 — C

Answer: GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ()). `GROUP BY GROUPING SETS ((Country, SubscriptionTier), (Country), ())` computes all specified subtotal levels and grand total in a single table scan. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `GROUP BY GROUPING SETS ((Country, SubscriptionTier), (Country), ())` computes all specified subtotal levels and grand total in a single table scan.
- **B:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `GROUP BY GROUPING SETS ((Country, SubscriptionTier), (Country), ())` computes all specified subtotal levels and grand total in a single table scan.
- **C:** Correct. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. In this scenario: `GROUP BY GROUPING SETS ((Country, SubscriptionTier), (Country), ())` computes all specified subtotal levels and grand total in a single table scan.
- **D:** Incorrect for this requirement. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Why the keyed choice wins: `GROUP BY GROUPING SETS ((Country, SubscriptionTier), (Country), ())` computes all specified subtotal levels and grand total in a single table scan.

### Question 49 — A

Answer: Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled. When `Group by` folds, Snowflake's MPP warehouse computes the aggregation and sends only compact campaign totals rather than 120 million raw clickstream rows. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Correct. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. In this scenario: When `Group by` folds, Snowflake's MPP warehouse computes the aggregation and sends only compact campaign totals rather than 120 million raw clickstream rows.
- **B:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: When `Group by` folds, Snowflake's MPP warehouse computes the aggregation and sends only compact campaign totals rather than 120 million raw clickstream rows.
- **C:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: When `Group by` folds, Snowflake's MPP warehouse computes the aggregation and sends only compact campaign totals rather than 120 million raw clickstream rows.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: When `Group by` folds, Snowflake's MPP warehouse computes the aggregation and sends only compact campaign totals rather than 120 million raw clickstream rows.

### Question 50 — A

Answer: WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET. `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only changed rows and prevents unnecessary Delta file churn. Guarding WHEN MATCHED with a hash/attribute inequality prevents rewriting unchanged Delta Parquet files on untouched rows during incremental upserts. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Correct. Guarding WHEN MATCHED with a hash/attribute inequality prevents rewriting unchanged Delta Parquet files on untouched rows during incremental upserts. In this scenario: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only changed rows and prevents unnecessary Delta file churn.
- **B:** Incorrect for this requirement. Fabric Data Warehouse supports FILTER PREDICATE with inline TVFs (not stored procedures or SQL Server DML BLOCK PREDICATE triggers). Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only changed rows and prevents unnecessary Delta file churn.
- **C:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only changed rows and prevents unnecessary Delta file churn.
- **D:** Incorrect for this requirement. Omitting PARTITION BY ranks across the entire table globally rather than per entity, and RANK() returns duplicate rank-1 rows on exact timestamp ties. Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only changed rows and prevents unnecessary Delta file churn.

### Question 51 — B

Answer: Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table. A `Left Anti Join` from `DimTitle` to trailing-90-day `FactWatchSessions` isolates titles with zero matching watch sessions. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Why the keyed choice wins: A `Left Anti Join` from `DimTitle` to trailing-90-day `FactWatchSessions` isolates titles with zero matching watch sessions.
- **B:** Correct. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. In this scenario: A `Left Anti Join` from `DimTitle` to trailing-90-day `FactWatchSessions` isolates titles with zero matching watch sessions.
- **C:** Incorrect for this requirement. Delta Lake MERGE INTO (in Spark SQL, PySpark DeltaTable.forPath().merge(), or Warehouse T-SQL) atomically applies incremental CDC inserts, updates, and soft-deletes in a single ACID transaction. Why the keyed choice wins: A `Left Anti Join` from `DimTitle` to trailing-90-day `FactWatchSessions` isolates titles with zero matching watch sessions.
- **D:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: A `Left Anti Join` from `DimTitle` to trailing-90-day `FactWatchSessions` isolates titles with zero matching watch sessions.

### Question 52 — D, E

Answers: fact_df.join(F.broadcast(dim_store_df), on="StoreKey", how="left"); Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement. `F.broadcast(dim_dma_region)` broadcasts the small lookup to executors without shuffling 1.8B events, and Delta `MERGE INTO` commits atomic upserts. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `F.broadcast(dim_dma_region)` broadcasts the small lookup to executors without shuffling 1.8B events, and Delta `MERGE INTO` commits atomic upserts.
- **B:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: `F.broadcast(dim_dma_region)` broadcasts the small lookup to executors without shuffling 1.8B events, and Delta `MERGE INTO` commits atomic upserts.
- **C:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `F.broadcast(dim_dma_region)` broadcasts the small lookup to executors without shuffling 1.8B events, and Delta `MERGE INTO` commits atomic upserts.
- **D:** Correct. Wrapping the small dimension DataFrame in pyspark.sql.functions.broadcast() avoids shuffling the multi-hundred-million-row fact DataFrame across Spark executors. In this scenario: `F.broadcast(dim_dma_region)` broadcasts the small lookup to executors without shuffling 1.8B events, and Delta `MERGE INTO` commits atomic upserts.
- **E:** Correct. Delta Lake MERGE INTO (in Spark SQL, PySpark DeltaTable.forPath().merge(), or Warehouse T-SQL) atomically applies incremental CDC inserts, updates, and soft-deletes in a single ACID transaction. In this scenario: `F.broadcast(dim_dma_region)` broadcasts the small lookup to executors without shuffling 1.8B events, and Delta `MERGE INTO` commits atomic upserts.

### Question 53 — C

Answer: ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC). `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` guarantees a single unique `rn = 1` row per event ID even if retry timestamps tie. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` guarantees a single unique `rn = 1` row per event ID even if retry timestamps tie.
- **B:** Incorrect for this requirement. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` guarantees a single unique `rn = 1` row per event ID even if retry timestamps tie.
- **C:** Correct. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. In this scenario: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` guarantees a single unique `rn = 1` row per event ID even if retry timestamps tie.
- **D:** Incorrect for this requirement. Omitting PARTITION BY ranks across the entire table globally rather than per entity, and RANK() returns duplicate rank-1 rows on exact timestamp ties. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` guarantees a single unique `rn = 1` row per event ID even if retry timestamps tie.

### Question 54 — D

Answer: Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE. Mapping unmatched foreign keys via `COALESCE` to `-1` (`Unknown / Unassigned Title`) in `DimTitle` retains every watch session cleanly until late dimension resolution. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: Mapping unmatched foreign keys via `COALESCE` to `-1` (`Unknown / Unassigned Title`) in `DimTitle` retains every watch session cleanly until late dimension resolution.
- **B:** Incorrect for this requirement. Using >= AND <= on both ends causes rows stamped exactly at midnight on partition boundaries to load into two adjacent partitions, silently double-counting sales totals. Why the keyed choice wins: Mapping unmatched foreign keys via `COALESCE` to `-1` (`Unknown / Unassigned Title`) in `DimTitle` retains every watch session cleanly until late dimension resolution.
- **C:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Mapping unmatched foreign keys via `COALESCE` to `-1` (`Unknown / Unassigned Title`) in `DimTitle` retains every watch session cleanly until late dimension resolution.
- **D:** Correct. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. In this scenario: Mapping unmatched foreign keys via `COALESCE` to `-1` (`Unknown / Unassigned Title`) in `DimTitle` retains every watch session cleanly until late dimension resolution.

### Question 55 — D, E

Answers: Launch Data Wrangler from a Fabric Spark notebook (or enable Power Query Column profiling based on entire data set) to inspect nulls, duplicates, and distributions and export generated PySpark code; Deduplicate using ROW_NUMBER() OVER (PARTITION BY BusinessKey ORDER BY ModifiedTimestamp DESC) = 1. Profiling across the entire dataset (via Data Wrangler in Spark or Power Query entire-dataset profiling) exposes deep anomalies, and `ROW_NUMBER() OVER (PARTITION BY ...)` removes duplicate keys. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Profiling across the entire dataset (via Data Wrangler in Spark or Power Query entire-dataset profiling) exposes deep anomalies, and `ROW_NUMBER() OVER (PARTITION BY ...)` removes duplicate keys.
- **B:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Profiling across the entire dataset (via Data Wrangler in Spark or Power Query entire-dataset profiling) exposes deep anomalies, and `ROW_NUMBER() OVER (PARTITION BY ...)` removes duplicate keys.
- **C:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Profiling across the entire dataset (via Data Wrangler in Spark or Power Query entire-dataset profiling) exposes deep anomalies, and `ROW_NUMBER() OVER (PARTITION BY ...)` removes duplicate keys.
- **D:** Correct. Windowing by BusinessKey ordered descending by ingestion or source-change timestamp deterministically retains only the latest version of duplicate CDC events while preserving all non-key columns. In this scenario: Profiling across the entire dataset (via Data Wrangler in Spark or Power Query entire-dataset profiling) exposes deep anomalies, and `ROW_NUMBER() OVER (PARTITION BY ...)` removes duplicate keys.
- **E:** Correct. Power Query profiles only the top 1,000 rows by default unless switched to entire dataset, whereas Data Wrangler interactively profiles Pandas/Spark DataFrames and emits reproducible Python/PySpark cleaning code. In this scenario: Profiling across the entire dataset (via Data Wrangler in Spark or Power Query entire-dataset profiling) exposes deep anomalies, and `ROW_NUMBER() OVER (PARTITION BY ...)` removes duplicate keys.

### Question 56 — A

Answer: TRY_CAST(RawReading AS DECIMAL(18, 4)). `TRY_CAST(RawReading AS DECIMAL(18, 4))` prevents batch-failing conversion errors while preserving exact currency precision. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Local study-map skill 2.13 (Convert Column Data Types Safely (TRY_CAST, Fixed Decimal, and Direct Lake Supported Primitive Types)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data types in Fabric Data Warehouse and Direct Lake Delta tables (https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types).

- **A:** Correct. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. In this scenario: `TRY_CAST(RawReading AS DECIMAL(18, 4))` prevents batch-failing conversion errors while preserving exact currency precision.
- **B:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` prevents batch-failing conversion errors while preserving exact currency precision.
- **C:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` prevents batch-failing conversion errors while preserving exact currency precision.
- **D:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` prevents batch-failing conversion errors while preserving exact currency precision.

### Question 57 — B

Answer: Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake. Removing unreferenced `BINARY`/`GUID` columns (or projecting required identifiers as `STRING`/`VARCHAR`) aligns the Gold Delta table with Direct Lake's supported primitive types. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. Local study-map skill 2.13 (Convert Column Data Types Safely (TRY_CAST, Fixed Decimal, and Direct Lake Supported Primitive Types)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data types in Fabric Data Warehouse and Direct Lake Delta tables (https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types).

- **A:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Removing unreferenced `BINARY`/`GUID` columns (or projecting required identifiers as `STRING`/`VARCHAR`) aligns the Gold Delta table with Direct Lake's supported primitive types.
- **B:** Correct. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. In this scenario: Removing unreferenced `BINARY`/`GUID` columns (or projecting required identifiers as `STRING`/`VARCHAR`) aligns the Gold Delta table with Direct Lake's supported primitive types.
- **C:** Incorrect for this requirement. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Why the keyed choice wins: Removing unreferenced `BINARY`/`GUID` columns (or projecting required identifiers as `STRING`/`VARCHAR`) aligns the Gold Delta table with Direct Lake's supported primitive types.
- **D:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Removing unreferenced `BINARY`/`GUID` columns (or projecting required identifiers as `STRING`/`VARCHAR`) aligns the Gold Delta table with Direct Lake's supported primitive types.

### Question 58 — C

Answer: Filter on physical Delta partition or liquid-clustered date columns using sargable range predicates (OrderDate >= '2026-01-01') without wrapping the column in functions. Sargable range comparisons on `ImpressionDate` enable Delta partition pruning and Parquet min/max file skipping, whereas `DATEPART(...)` evaluates every row across all partitions. Wrapping a column in YEAR(OrderDate) = 2026 blocks file-level min/max data skipping and partition pruning; sargable range predicates let Spark and SQL endpoints skip irrelevant Parquet files entirely. Local study-map skill 2.14 (Filter Data Early Preserving Power Query Folding (View Native Query) and Sargable Delta File Pruning), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query folding indicators & predicate pushdown in Power Query and Delta Lake (https://learn.microsoft.com/en-us/power-query/query-folding-basics).

- **A:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: Sargable range comparisons on `ImpressionDate` enable Delta partition pruning and Parquet min/max file skipping, whereas `DATEPART(...)` evaluates every row across all partitions.
- **B:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: Sargable range comparisons on `ImpressionDate` enable Delta partition pruning and Parquet min/max file skipping, whereas `DATEPART(...)` evaluates every row across all partitions.
- **C:** Correct. Wrapping a column in YEAR(OrderDate) = 2026 blocks file-level min/max data skipping and partition pruning; sargable range predicates let Spark and SQL endpoints skip irrelevant Parquet files entirely. In this scenario: Sargable range comparisons on `ImpressionDate` enable Delta partition pruning and Parquet min/max file skipping, whereas `DATEPART(...)` evaluates every row across all partitions.
- **D:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: Sargable range comparisons on `ImpressionDate` enable Delta partition pruning and Parquet min/max file skipping, whereas `DATEPART(...)` evaluates every row across all partitions.

### Question 59 — C

Answer: Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view. The `Visual query editor` (`New visual query`) builds diagram-based joins and filters and persists them via `Save as view`. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Local study-map skill 2.15 (Select, Filter, and Aggregate Data Using the Visual Query Editor and Save as SQL Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query using the Visual query editor in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/visual-query-editor).

- **A:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: The `Visual query editor` (`New visual query`) builds diagram-based joins and filters and persists them via `Save as view`.
- **B:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: The `Visual query editor` (`New visual query`) builds diagram-based joins and filters and persists them via `Save as view`.
- **C:** Correct. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. In this scenario: The `Visual query editor` (`New visual query`) builds diagram-based joins and filters and persists them via `Save as view`.
- **D:** Incorrect for this requirement. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Why the keyed choice wins: The `Visual query editor` (`New visual query`) builds diagram-based joins and filters and persists them via `Save as view`.

### Question 60 — C

Answer: Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view. Yes — both Fabric Data Warehouses and Lakehouse SQL analytics endpoints expose `New visual query` with `Merge`, `Filter`, `Group by`, and `Save as view`. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Local study-map skill 2.15 (Select, Filter, and Aggregate Data Using the Visual Query Editor and Save as SQL Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query using the Visual query editor in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/visual-query-editor).

- **A:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Yes — both Fabric Data Warehouses and Lakehouse SQL analytics endpoints expose `New visual query` with `Merge`, `Filter`, `Group by`, and `Save as view`.
- **B:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Yes — both Fabric Data Warehouses and Lakehouse SQL analytics endpoints expose `New visual query` with `Merge`, `Filter`, `Group by`, and `Save as view`.
- **C:** Correct. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. In this scenario: Yes — both Fabric Data Warehouses and Lakehouse SQL analytics endpoints expose `New visual query` with `Merge`, `Filter`, `Group by`, and `Save as view`.
- **D:** Incorrect for this requirement. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. Why the keyed choice wins: Yes — both Fabric Data Warehouses and Lakehouse SQL analytics endpoints expose `New visual query` with `Merge`, `Filter`, `Group by`, and `Save as view`.

### Question 61 — B

Answer: Query across a Warehouse and a Lakehouse SQL analytics endpoint in the same workspace using three-part T-SQL naming (SalesLakehouse.dbo.RawOrders). Three-part T-SQL naming (`PlaybackLakehouse.dbo.FactSessions`) joins tables across sibling Lakehouse SQL endpoints and Warehouses in the same workspace zero-copy. Fabric Warehouse and SQL analytics endpoints inside the same workspace share a unified SQL engine namespace, enabling zero-copy cross-database T-SQL joins via DatabaseName.SchemaName.ObjectName. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: Three-part T-SQL naming (`PlaybackLakehouse.dbo.FactSessions`) joins tables across sibling Lakehouse SQL endpoints and Warehouses in the same workspace zero-copy.
- **B:** Correct. Fabric Warehouse and SQL analytics endpoints inside the same workspace share a unified SQL engine namespace, enabling zero-copy cross-database T-SQL joins via DatabaseName.SchemaName.ObjectName. In this scenario: Three-part T-SQL naming (`PlaybackLakehouse.dbo.FactSessions`) joins tables across sibling Lakehouse SQL endpoints and Warehouses in the same workspace zero-copy.
- **C:** Incorrect for this requirement. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. Why the keyed choice wins: Three-part T-SQL naming (`PlaybackLakehouse.dbo.FactSessions`) joins tables across sibling Lakehouse SQL endpoints and Warehouses in the same workspace zero-copy.
- **D:** Incorrect for this requirement. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. Why the keyed choice wins: Three-part T-SQL naming (`PlaybackLakehouse.dbo.FactSessions`) joins tables across sibling Lakehouse SQL endpoints and Warehouses in the same workspace zero-copy.

### Question 62 — C

Answer: LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC). `LAG(WeeklyViews, 1, 0) OVER (PARTITION BY SeriesId ORDER BY ReleaseWeek ASC)` retrieves the prior week's views within each series partition. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Incorrect for this requirement. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Why the keyed choice wins: `LAG(WeeklyViews, 1, 0) OVER (PARTITION BY SeriesId ORDER BY ReleaseWeek ASC)` retrieves the prior week's views within each series partition.
- **B:** Incorrect for this requirement. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Why the keyed choice wins: `LAG(WeeklyViews, 1, 0) OVER (PARTITION BY SeriesId ORDER BY ReleaseWeek ASC)` retrieves the prior week's views within each series partition.
- **C:** Correct. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. In this scenario: `LAG(WeeklyViews, 1, 0) OVER (PARTITION BY SeriesId ORDER BY ReleaseWeek ASC)` retrieves the prior week's views within each series partition.
- **D:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `LAG(WeeklyViews, 1, 0) OVER (PARTITION BY SeriesId ORDER BY ReleaseWeek ASC)` retrieves the prior week's views within each series partition.

### Question 63 — B, C

Answers: OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000'); CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales. `OPTION (FOR TIMESTAMP AS OF ...)` queries historical state via Warehouse Time Travel, and `CREATE TABLE ... AS CLONE OF` creates an instantaneous zero-copy clone. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `OPTION (FOR TIMESTAMP AS OF ...)` queries historical state via Warehouse Time Travel, and `CREATE TABLE ... AS CLONE OF` creates an instantaneous zero-copy clone.
- **B:** Correct. CREATE TABLE ... AS CLONE OF creates a zero-copy metadata clone of a Fabric Warehouse table instantaneously (optionally AT a specific UTC timestamp) without duplicating Parquet files. In this scenario: `OPTION (FOR TIMESTAMP AS OF ...)` queries historical state via Warehouse Time Travel, and `CREATE TABLE ... AS CLONE OF` creates an instantaneous zero-copy clone.
- **C:** Correct. Fabric Data Warehouse Time Travel uses the query hint OPTION (FOR TIMESTAMP AS OF 'YYYY-MM-DDTHH:MM:SS.fff') to read exact point-in-time historical snapshots within the retention window. In this scenario: `OPTION (FOR TIMESTAMP AS OF ...)` queries historical state via Warehouse Time Travel, and `CREATE TABLE ... AS CLONE OF` creates an instantaneous zero-copy clone.
- **D:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `OPTION (FOR TIMESTAMP AS OF ...)` queries historical state via Warehouse Time Travel, and `CREATE TABLE ... AS CLONE OF` creates an instantaneous zero-copy clone.
- **E:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: `OPTION (FOR TIMESTAMP AS OF ...)` queries historical state via Warehouse Time Travel, and `CREATE TABLE ... AS CLONE OF` creates an instantaneous zero-copy clone.

### Question 64 — B

Answer: | summarize arg_max(IngestionTime, *) by SpecimenId. `| summarize arg_max(IngestionTime, *) by <EntityKey>` returns the full latest row per session key in Eventhouse KQL. In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key. Local study-map skill 2.17 (Select, Filter, and Aggregate Data Using KQL (summarize, bin, arg_max, percentile, parse_json, mv-expand)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query data in a KQL queryset in Microsoft Fabric Real-Time Intelligence (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/kql-queryset).

- **A:** Incorrect for this requirement. percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse. Why the keyed choice wins: `| summarize arg_max(IngestionTime, *) by <EntityKey>` returns the full latest row per session key in Eventhouse KQL.
- **B:** Correct. In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key. In this scenario: `| summarize arg_max(IngestionTime, *) by <EntityKey>` returns the full latest row per session key in Eventhouse KQL.
- **C:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `| summarize arg_max(IngestionTime, *) by <EntityKey>` returns the full latest row per session key in Eventhouse KQL.
- **D:** Incorrect for this requirement. make-series builds regular gap-filled time-series arrays (filling empty 1-minute buckets with default = 0) required for KQL anomaly detection and trend functions; summarize by bin() omits empty buckets. Why the keyed choice wins: `| summarize arg_max(IngestionTime, *) by <EntityKey>` returns the full latest row per session key in Eventhouse KQL.

### Question 65 — C

Answer: | mv-expand PhaseReading = parse_json(Payload).PhaseReadings. `| mv-expand ... = parse_json(Payload)...` expands each element of the JSON array into its own KQL row before aggregation. mv-expand unpacks a dynamic JSON array into one output row per array element while preserving parent event columns. Local study-map skill 2.17 (Select, Filter, and Aggregate Data Using KQL (summarize, bin, arg_max, percentile, parse_json, mv-expand)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query data in a KQL queryset in Microsoft Fabric Real-Time Intelligence (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/kql-queryset).

- **A:** Incorrect for this requirement. In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key. Why the keyed choice wins: `| mv-expand ... = parse_json(Payload)...` expands each element of the JSON array into its own KQL row before aggregation.
- **B:** Incorrect for this requirement. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Why the keyed choice wins: `| mv-expand ... = parse_json(Payload)...` expands each element of the JSON array into its own KQL row before aggregation.
- **C:** Correct. mv-expand unpacks a dynamic JSON array into one output row per array element while preserving parent event columns. In this scenario: `| mv-expand ... = parse_json(Payload)...` expands each element of the JSON array into its own KQL row before aggregation.
- **D:** Incorrect for this requirement. percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse. Why the keyed choice wins: `| mv-expand ... = parse_json(Payload)...` expands each element of the JSON array into its own KQL row before aggregation.

### Question 66 — B

Answer: Configure Import storage mode. `Import` storage mode loads the 90 MB dataset into compressed VertiPaq RAM once daily for maximum DAX feature support and speed. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Local study-map skill 3.1 (Choose a Semantic Model Storage Mode (Import, DirectQuery, Direct Lake, and Dual)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model storage modes in the Power BI service & Microsoft Fabric (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode).

- **A:** Incorrect for this requirement. Direct Lake loads Delta Parquet columns directly from OneLake into VertiPaq memory on demand without scheduled Import data duplication or slow per-visual SQL translation. Why the keyed choice wins: `Import` storage mode loads the 90 MB dataset into compressed VertiPaq RAM once daily for maximum DAX feature support and speed.
- **B:** Correct. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. In this scenario: `Import` storage mode loads the 90 MB dataset into compressed VertiPaq RAM once daily for maximum DAX feature support and speed.
- **C:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Import` storage mode loads the 90 MB dataset into compressed VertiPaq RAM once daily for maximum DAX feature support and speed.
- **D:** Incorrect for this requirement. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Why the keyed choice wins: `Import` storage mode loads the 90 MB dataset into compressed VertiPaq RAM once daily for maximum DAX feature support and speed.

### Question 67 — A

Answer: Configure shared dimension tables in Dual storage mode inside a composite model. `Dual` storage mode lets `DimCampaign` and `DimDate` filter `Import` aggregations purely in RAM while pushing native SQL joins down for `DirectQuery` impression drills. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Local study-map skill 3.1 (Choose a Semantic Model Storage Mode (Import, DirectQuery, Direct Lake, and Dual)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model storage modes in the Power BI service & Microsoft Fabric (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode).

- **A:** Correct. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. In this scenario: `Dual` storage mode lets `DimCampaign` and `DimDate` filter `Import` aggregations purely in RAM while pushing native SQL joins down for `DirectQuery` impression drills.
- **B:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Dual` storage mode lets `DimCampaign` and `DimDate` filter `Import` aggregations purely in RAM while pushing native SQL joins down for `DirectQuery` impression drills.
- **C:** Incorrect for this requirement. Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery. Why the keyed choice wins: `Dual` storage mode lets `DimCampaign` and `DimDate` filter `Import` aggregations purely in RAM while pushing native SQL joins down for `DirectQuery` impression drills.
- **D:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Dual` storage mode lets `DimCampaign` and `DimDate` filter `Import` aggregations purely in RAM while pushing native SQL joins down for `DirectQuery` impression drills.

### Question 68 — D

Answer: Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column. Disabling `Auto date/time` and configuring `Mark as date table` on `DimBroadcastDate` using its unique `Date` column enables clean time intelligence over integer keys. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. Local study-map skill 3.2 (Implement a Star Schema for a Semantic Model (Mark as Date Table, Hide Keys, Sort by Column, Display Folders)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Set and use date tables & star-schema best practices in Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables).

- **A:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Disabling `Auto date/time` and configuring `Mark as date table` on `DimBroadcastDate` using its unique `Date` column enables clean time intelligence over integer keys.
- **B:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: Disabling `Auto date/time` and configuring `Mark as date table` on `DimBroadcastDate` using its unique `Date` column enables clean time intelligence over integer keys.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Disabling `Auto date/time` and configuring `Mark as date table` on `DimBroadcastDate` using its unique `Date` column enables clean time intelligence over integer keys.
- **D:** Correct. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. In this scenario: Disabling `Auto date/time` and configuring `Mark as date table` on `DimBroadcastDate` using its unique `Date` column enables clean time intelligence over integer keys.

### Question 69 — C, D

Answers: Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear; Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column. Hiding technical keys/raw fact columns with explicit measures in Display Folders + `Sort by Column`, paired with disabling `Auto date/time` + `Mark as date table`, delivers star-schema best practices. Local study-map skill 3.2 (Implement a Star Schema for a Semantic Model (Mark as Date Table, Hide Keys, Sort by Column, Display Folders)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Set and use date tables & star-schema best practices in Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables).

- **A:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Hiding technical keys/raw fact columns with explicit measures in Display Folders + `Sort by Column`, paired with disabling `Auto date/time` + `Mark as date table`, delivers star-schema best practices.
- **B:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Hiding technical keys/raw fact columns with explicit measures in Display Folders + `Sort by Column`, paired with disabling `Auto date/time` + `Mark as date table`, delivers star-schema best practices.
- **C:** Correct. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. In this scenario: Hiding technical keys/raw fact columns with explicit measures in Display Folders + `Sort by Column`, paired with disabling `Auto date/time` + `Mark as date table`, delivers star-schema best practices.
- **D:** Correct. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. In this scenario: Hiding technical keys/raw fact columns with explicit measures in Display Folders + `Sort by Column`, paired with disabling `Auto date/time` + `Mark as date table`, delivers star-schema best practices.
- **E:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Hiding technical keys/raw fact columns with explicit measures in Display Folders + `Sort by Column`, paired with disabling `Auto date/time` + `Mark as date table`, delivers star-schema best practices.

### Question 70 — D

Answer: Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP(). Keep `SignupDateKey` as the active `1:*` relationship and activate `CancelDateKey` inside `[Cancellations]` via `CALCULATE([Base Count], USERELATIONSHIP(DimCalendar[DateKey], FactSubscriptions[CancelDateKey]))`. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. Scoping CROSSFILTER(..., BOTH) inside a DAX measure over a bridge table satisfies many-to-many attribution without turning on permanent model-wide bidirectional relationships that cause ambiguity and performance degradation. Why the keyed choice wins: Keep `SignupDateKey` as the active `1:*` relationship and activate `CancelDateKey` inside `[Cancellations]` via `CALCULATE([Base Count], USERELATIONSHIP(DimCalendar[DateKey], FactSubscriptions[CancelDateKey]))`.
- **B:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: Keep `SignupDateKey` as the active `1:*` relationship and activate `CancelDateKey` inside `[Cancellations]` via `CALCULATE([Base Count], USERELATIONSHIP(DimCalendar[DateKey], FactSubscriptions[CancelDateKey]))`.
- **C:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Keep `SignupDateKey` as the active `1:*` relationship and activate `CancelDateKey` inside `[Cancellations]` via `CALCULATE([Base Count], USERELATIONSHIP(DimCalendar[DateKey], FactSubscriptions[CancelDateKey]))`.
- **D:** Correct. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. In this scenario: Keep `SignupDateKey` as the active `1:*` relationship and activate `CancelDateKey` inside `[Cancellations]` via `CALCULATE([Base Count], USERELATIONSHIP(DimCalendar[DateKey], FactSubscriptions[CancelDateKey]))`.

### Question 71 — C

Answer: CALCULATE([Encounter Count], CROSSFILTER('FactEncounter'[EncounterKey], 'BridgeEncounterDiag'[EncounterKey], BOTH)). Scoping `CROSSFILTER(..., BOTH)` inside the measure propagates genre filters across the bridge table only during that calculation. CROSSFILTER(..., BOTH) enables bidirectional filter propagation across a bridge table only inside the specific measure rather than globally across the model. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Scoping `CROSSFILTER(..., BOTH)` inside the measure propagates genre filters across the bridge table only during that calculation.
- **B:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: Scoping `CROSSFILTER(..., BOTH)` inside the measure propagates genre filters across the bridge table only during that calculation.
- **C:** Correct. CROSSFILTER(..., BOTH) enables bidirectional filter propagation across a bridge table only inside the specific measure rather than globally across the model. In this scenario: Scoping `CROSSFILTER(..., BOTH)` inside the measure propagates genre filters across the bridge table only during that calculation.
- **D:** Incorrect for this requirement. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. Why the keyed choice wins: Scoping `CROSSFILTER(..., BOTH)` inside the measure propagates genre filters across the bridge table only during that calculation.

### Question 72 — B

Answer: Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid. `Assume referential integrity` instructs Power BI's DirectQuery SQL generator to emit `INNER JOIN` statements. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: `Assume referential integrity` instructs Power BI's DirectQuery SQL generator to emit `INNER JOIN` statements.
- **B:** Correct. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. In this scenario: `Assume referential integrity` instructs Power BI's DirectQuery SQL generator to emit `INNER JOIN` statements.
- **C:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Assume referential integrity` instructs Power BI's DirectQuery SQL generator to emit `INNER JOIN` statements.
- **D:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: `Assume referential integrity` instructs Power BI's DirectQuery SQL generator to emit `INNER JOIN` statements.

### Question 73 — D

Answer: Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table. `SUMX` evaluates `(Impressions / 1000) * ContractCPM` row-by-row in memory before summing. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Incorrect for this requirement. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. Why the keyed choice wins: `SUMX` evaluates `(Impressions / 1000) * ContractCPM` row-by-row in memory before summing.
- **B:** Incorrect for this requirement. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Why the keyed choice wins: `SUMX` evaluates `(Impressions / 1000) * ContractCPM` row-by-row in memory before summing.
- **C:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: `SUMX` evaluates `(Impressions / 1000) * ContractCPM` row-by-row in memory before summing.
- **D:** Correct. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. In this scenario: `SUMX` evaluates `(Impressions / 1000) * ContractCPM` row-by-row in memory before summing.

### Question 74 — A

Answer: Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches. Caching `[Trailing 14D Watch Mins]` in a `VAR` evaluates it once in the current filter context and reuses the scalar result. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Correct. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. In this scenario: Caching `[Trailing 14D Watch Mins]` in a `VAR` evaluates it once in the current filter context and reuses the scalar result.
- **B:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: Caching `[Trailing 14D Watch Mins]` in a `VAR` evaluates it once in the current filter context and reuses the scalar result.
- **C:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Caching `[Trailing 14D Watch Mins]` in a `VAR` evaluates it once in the current filter context and reuses the scalar result.
- **D:** Incorrect for this requirement. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Why the keyed choice wins: Caching `[Trailing 14D Watch Mins]` in a `VAR` evaluates it once in the current filter context and reuses the scalar result.

### Question 75 — A, E

Answers: CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC))); IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK()). `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` steps back one custom broadcast period, and `ISINSCOPE('DimContent'[Episode])` restricts evaluation to episode rows. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Correct. OFFSET(-1, ..., ORDERBY(...)) shifts one period backward along a custom 4-4-5 fiscal sort column where standard Gregorian DATEADD fails. In this scenario: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` steps back one custom broadcast period, and `ISINSCOPE('DimContent'[Episode])` restricts evaluation to episode rows.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` steps back one custom broadcast period, and `ISINSCOPE('DimContent'[Episode])` restricts evaluation to episode rows.
- **C:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` steps back one custom broadcast period, and `ISINSCOPE('DimContent'[Episode])` restricts evaluation to episode rows.
- **D:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` steps back one custom broadcast period, and `ISINSCOPE('DimContent'[Episode])` restricts evaluation to episode rows.
- **E:** Correct. ISINSCOPE('DimProduct'[SKU]) evaluates TRUE only when SKU is actively grouping the visual hierarchy level, suppressing misleading margin figures at subtotal rows. In this scenario: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` steps back one custom broadcast period, and `ISINSCOPE('DimContent'[Episode])` restricts evaluation to episode rows.

### Question 76 — D

Answer: CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date])). `SELECTEDMEASURE()` substitutes whichever base KPI measure is currently evaluated in the visual cell. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Why the keyed choice wins: `SELECTEDMEASURE()` substitutes whichever base KPI measure is currently evaluated in the visual cell.
- **B:** Incorrect for this requirement. INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags. Why the keyed choice wins: `SELECTEDMEASURE()` substitutes whichever base KPI measure is currently evaluated in the visual cell.
- **C:** Incorrect for this requirement. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Why the keyed choice wins: `SELECTEDMEASURE()` substitutes whichever base KPI measure is currently evaluated in the visual cell.
- **D:** Correct. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. In this scenario: `SELECTEDMEASURE()` substitutes whichever base KPI measure is currently evaluated in the visual cell.

### Question 77 — A

Answer: IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING()). `IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())` applies dynamic text formatting masks while keeping measure outputs numeric. Dynamic format string expressions return a format mask string while preserving the measure's underlying numeric type; SELECTEDMEASUREFORMATSTRING() preserves the base measure's native currency/decimal mask. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Correct. Dynamic format string expressions return a format mask string while preserving the measure's underlying numeric type; SELECTEDMEASUREFORMATSTRING() preserves the base measure's native currency/decimal mask. In this scenario: `IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())` applies dynamic text formatting masks while keeping measure outputs numeric.
- **B:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: `IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())` applies dynamic text formatting masks while keeping measure outputs numeric.
- **C:** Incorrect for this requirement. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Why the keyed choice wins: `IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())` applies dynamic text formatting masks while keeping measure outputs numeric.
- **D:** Incorrect for this requirement. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. Why the keyed choice wins: `IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())` applies dynamic text formatting masks while keeping measure outputs numeric.

### Question 78 — D

Answer: Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer. A `Field Parameter` (`NAMEOF(...)`) placed in the chart's Legend well swaps grouping columns dynamically from one slicer. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: A `Field Parameter` (`NAMEOF(...)`) placed in the chart's Legend well swaps grouping columns dynamically from one slicer.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: A `Field Parameter` (`NAMEOF(...)`) placed in the chart's Legend well swaps grouping columns dynamically from one slicer.
- **C:** Incorrect for this requirement. A single Calculation Group applies reusable logic (YTD, PY, YoY%, Moving Avg) across dozens of base measures via SELECTEDMEASURE(), eliminating measure explosion (`50 base * 6 time calcs = 300 measures`). Why the keyed choice wins: A `Field Parameter` (`NAMEOF(...)`) placed in the chart's Legend well swaps grouping columns dynamically from one slicer.
- **D:** Correct. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. In this scenario: A `Field Parameter` (`NAMEOF(...)`) placed in the chart's Legend well swaps grouping columns dynamically from one slicer.

### Question 79 — D

Answer: Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat). `Large semantic model storage format` unlocks full capacity SKU memory ceilings and improves XMLA write performance. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Local study-map skill 3.6 (Identify Use Cases for and Configure Large Semantic Model Storage Format), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Large semantic models in Microsoft Fabric & Power BI Premium (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-large-models).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Large semantic model storage format` unlocks full capacity SKU memory ceilings and improves XMLA write performance.
- **B:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Large semantic model storage format` unlocks full capacity SKU memory ceilings and improves XMLA write performance.
- **C:** Incorrect for this requirement. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Why the keyed choice wins: `Large semantic model storage format` unlocks full capacity SKU memory ceilings and improves XMLA write performance.
- **D:** Correct. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. In this scenario: `Large semantic model storage format` unlocks full capacity SKU memory ceilings and improves XMLA write performance.

### Question 80 — C

Answer: Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat). Similar to Direct Lake column loading, large Import models page needed column/dictionary segments into memory on demand during queries rather than loading the entire model upfront. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Local study-map skill 3.6 (Identify Use Cases for and Configure Large Semantic Model Storage Format), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Large semantic models in Microsoft Fabric & Power BI Premium (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-large-models).

- **A:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Similar to Direct Lake column loading, large Import models page needed column/dictionary segments into memory on demand during queries rather than loading the entire model upfront.
- **B:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Similar to Direct Lake column loading, large Import models page needed column/dictionary segments into memory on demand during queries rather than loading the entire model upfront.
- **C:** Correct. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. In this scenario: Similar to Direct Lake column loading, large Import models page needed column/dictionary segments into memory on demand during queries rather than loading the entire model upfront.
- **D:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Similar to Direct Lake column loading, large Import models page needed column/dictionary segments into memory on demand during queries rather than loading the entire model upfront.

### Question 81 — B, C

Answers: Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table; Configure shared dimension tables in Dual storage mode inside a composite model. Configuring `Manage aggregations` on an `Import` daily campaign table and setting shared `DimDate` / `DimCampaign` tables to `Dual` storage mode accelerates summary queries without cross-source join limits. Local study-map skill 3.7 (Design and Build Composite Models (Direct Lake on OneLake + Import, Dual + Aggregations, DirectQuery over PBI)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use composite models in Power BI Desktop & Direct Lake on OneLake composite models (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-web-modeling).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Configuring `Manage aggregations` on an `Import` daily campaign table and setting shared `DimDate` / `DimCampaign` tables to `Dual` storage mode accelerates summary queries without cross-source join limits.
- **B:** Correct. User-defined Import aggregations satisfy high-level grouped queries purely from in-memory VertiPaq cache and automatically route only unaggregated detail drill-throughs to the underlying DirectQuery source. In this scenario: Configuring `Manage aggregations` on an `Import` daily campaign table and setting shared `DimDate` / `DimCampaign` tables to `Dual` storage mode accelerates summary queries without cross-source join limits.
- **C:** Correct. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. In this scenario: Configuring `Manage aggregations` on an `Import` daily campaign table and setting shared `DimDate` / `DimCampaign` tables to `Dual` storage mode accelerates summary queries without cross-source join limits.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Configuring `Manage aggregations` on an `Import` daily campaign table and setting shared `DimDate` / `DimCampaign` tables to `Dual` storage mode accelerates summary queries without cross-source join limits.
- **E:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Configuring `Manage aggregations` on an `Import` daily campaign table and setting shared `DimDate` / `DimCampaign` tables to `Dual` storage mode accelerates summary queries without cross-source join limits.

### Question 82 — D

Answer: Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time. Power BI Desktop `Performance Analyzer` surfaces high `Other` wait times across the 36 visuals, guiding consolidation into fewer multi-metric visuals. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Local study-map skill 3.8 (Implement Performance Improvements in Queries and Report Visuals (Performance Analyzer & Query Reduction)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use Performance Analyzer to examine report element performance in Power BI (https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer).

- **A:** Incorrect for this requirement. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Why the keyed choice wins: Power BI Desktop `Performance Analyzer` surfaces high `Other` wait times across the 36 visuals, guiding consolidation into fewer multi-metric visuals.
- **B:** Incorrect for this requirement. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. Why the keyed choice wins: Power BI Desktop `Performance Analyzer` surfaces high `Other` wait times across the 36 visuals, guiding consolidation into fewer multi-metric visuals.
- **C:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: Power BI Desktop `Performance Analyzer` surfaces high `Other` wait times across the 36 visuals, guiding consolidation into fewer multi-metric visuals.
- **D:** Correct. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. In this scenario: Power BI Desktop `Performance Analyzer` surfaces high `Other` wait times across the 36 visuals, guiding consolidation into fewer multi-metric visuals.

### Question 83 — C

Answer: Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages. Enabling `Add an Apply button to each single/multi-select slicer` batches multi-select filter changes into a single query on `Apply`. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Local study-map skill 3.8 (Implement Performance Improvements in Queries and Report Visuals (Performance Analyzer & Query Reduction)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use Performance Analyzer to examine report element performance in Power BI (https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer).

- **A:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Enabling `Add an Apply button to each single/multi-select slicer` batches multi-select filter changes into a single query on `Apply`.
- **B:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Enabling `Add an Apply button to each single/multi-select slicer` batches multi-select filter changes into a single query on `Apply`.
- **C:** Correct. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. In this scenario: Enabling `Add an Apply button to each single/multi-select slicer` batches multi-select filter changes into a single query on `Apply`.
- **D:** Incorrect for this requirement. Hundreds of tiny streaming Parquet files inflate Delta rowgroup counts past Fabric SKU guardrails and degrade transcoding; OPTIMIZE compacts files into large V-Order-sorted rowgroups optimized for VertiPaq in-memory compression. Why the keyed choice wins: Enabling `Add an Apply button to each single/multi-select slicer` batches multi-select filter changes into a single query on `Apply`.

### Question 84 — B

Answer: Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time. Hiding a column only removes UI visibility while keeping its full dictionary in VertiPaq RAM; excluding `PlaybackSessionGUID` from the semantic model removes the 11 GB dictionary. Columnar memory in VertiPaq and Direct Lake transcoding scales primarily with column cardinality rather than row count; dropping unused GUIDs or splitting millisecond timestamps into separate Date and Time columns cuts memory dramatically. Local study-map skill 3.9 (Improve DAX and Model Performance Using DAX Studio Server Timings (FE vs SE) and VertiPaq Cardinality Reduction), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Optimization guide for Power BI — DAX Formula Engine vs Storage Engine & VertiPaq (https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization).

- **A:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Hiding a column only removes UI visibility while keeping its full dictionary in VertiPaq RAM; excluding `PlaybackSessionGUID` from the semantic model removes the 11 GB dictionary.
- **B:** Correct. Columnar memory in VertiPaq and Direct Lake transcoding scales primarily with column cardinality rather than row count; dropping unused GUIDs or splitting millisecond timestamps into separate Date and Time columns cuts memory dramatically. In this scenario: Hiding a column only removes UI visibility while keeping its full dictionary in VertiPaq RAM; excluding `PlaybackSessionGUID` from the semantic model removes the 11 GB dictionary.
- **C:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Hiding a column only removes UI visibility while keeping its full dictionary in VertiPaq RAM; excluding `PlaybackSessionGUID` from the semantic model removes the 11 GB dictionary.
- **D:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: Hiding a column only removes UI visibility while keeping its full dictionary in VertiPaq RAM; excluding `PlaybackSessionGUID` from the semantic model removes the 11 GB dictionary.

### Question 85 — B

Answer: Capture visual timings in Performance Analyzer → Profile captured DAX in DAX Studio with Server Timings and Query Plan → Refactor FILTER(Fact,...) into VAR-cached SE column predicates and run V-Order OPTIMIZE → Re-test with Clear Cache. Isolating the visual query in Performance Analyzer, profiling FE/SE + CallbackDataID in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing after `Clear Cache` validates the fix. Correct order: isolate visual vs DAX queue time in Performance Analyzer, profile FE/SE and Direct Lake fallback in DAX Studio Server Timings, fix DAX anti-patterns + Delta Parquet layout, and benchmark cold-cache results. Local study-map skill 3.9 (Improve DAX and Model Performance Using DAX Studio Server Timings (FE vs SE) and VertiPaq Cardinality Reduction), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Optimization guide for Power BI — DAX Formula Engine vs Storage Engine & VertiPaq (https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization).

- **A:** Incorrect for this requirement. Incorrect: scaling capacity blindly wastes budget while bidirectional joins, FORMAT() strings, and disabled V-Order make FE and transcoding slower. Why the keyed choice wins: Isolating the visual query in Performance Analyzer, profiling FE/SE + CallbackDataID in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing after `Clear Cache` validates the fix.
- **B:** Correct. Correct order: isolate visual vs DAX queue time in Performance Analyzer, profile FE/SE and Direct Lake fallback in DAX Studio Server Timings, fix DAX anti-patterns + Delta Parquet layout, and benchmark cold-cache results. In this scenario: Isolating the visual query in Performance Analyzer, profiling FE/SE + CallbackDataID in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing after `Clear Cache` validates the fix.
- **C:** Incorrect for this requirement. Incorrect: snowflaking and Auto date/time increase relationship hops and memory overhead rather than resolving FE/SE bottlenecks. Why the keyed choice wins: Isolating the visual query in Performance Analyzer, profiling FE/SE + CallbackDataID in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing after `Clear Cache` validates the fix.
- **D:** Incorrect for this requirement. Incorrect: benchmarking warm cache hides real SE/transcoding cost, GUID columns bloat dictionaries, DirectQueryOnly slows visuals, and 45 cards create visual-queue contention. Why the keyed choice wins: Isolating the visual query in Performance Analyzer, profiling FE/SE + CallbackDataID in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + running V-Order `OPTIMIZE`, and re-testing after `Clear Cache` validates the fix.

### Question 86 — B, C, F

Answers: Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails; Set DirectLakeBehavior = DirectLakeOnly on a Direct Lake on SQL semantic model so queries fail fast instead of silently falling back to slow DirectQuery; Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time. Compacting Delta tables with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID columns, and setting `DirectLakeBehavior = DirectLakeOnly` prevent guardrail breaches and silent fallback. Local study-map skill 3.10 (Configure Direct Lake Framing, Transcoding, V-Order/OPTIMIZE Guardrails, and DirectLakeBehavior Fallback), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: How Direct Lake works (framing, transcoding, V-Order, fallback & DirectLakeBehavior) (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works).

- **A:** Incorrect for this requirement. Direct Lake on OneLake operates exclusively in DirectLakeOnly mode and never falls back to DirectQuery; exceeding capacity guardrails fails framing/queries until Delta tables or SKU sizing are optimized. Why the keyed choice wins: Compacting Delta tables with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID columns, and setting `DirectLakeBehavior = DirectLakeOnly` prevent guardrail breaches and silent fallback.
- **B:** Correct. Columnar memory in VertiPaq and Direct Lake transcoding scales primarily with column cardinality rather than row count; dropping unused GUIDs or splitting millisecond timestamps into separate Date and Time columns cuts memory dramatically. In this scenario: Compacting Delta tables with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID columns, and setting `DirectLakeBehavior = DirectLakeOnly` prevent guardrail breaches and silent fallback.
- **C:** Correct. Setting DirectLakeBehavior to DirectLakeOnly (on Direct Lake on SQL models) prevents unexpected DirectQuery fallback spikes on the SQL endpoint when guardrails or SQL views/RLS are encountered. In this scenario: Compacting Delta tables with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID columns, and setting `DirectLakeBehavior = DirectLakeOnly` prevent guardrail breaches and silent fallback.
- **D:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Compacting Delta tables with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID columns, and setting `DirectLakeBehavior = DirectLakeOnly` prevent guardrail breaches and silent fallback.
- **E:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Compacting Delta tables with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID columns, and setting `DirectLakeBehavior = DirectLakeOnly` prevent guardrail breaches and silent fallback.
- **F:** Correct. Hundreds of tiny streaming Parquet files inflate Delta rowgroup counts past Fabric SKU guardrails and degrade transcoding; OPTIMIZE compacts files into large V-Order-sorted rowgroups optimized for VertiPaq in-memory compression. In this scenario: Compacting Delta tables with `OPTIMIZE` + `V-Order`, removing unused high-cardinality GUID columns, and setting `DirectLakeBehavior = DirectLakeOnly` prevent guardrail breaches and silent fallback.

### Question 87 — A

Answer: Live edit the model in Power BI Desktop and save a Version history point → Script the semantic model in TMDL view → Replace Sql.Database(...) with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...") → Apply TMDL and run framing refresh. Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the upgrade cleanly. Correct order: take a version history checkpoint while live editing, script the model in TMDL view, swap the shared M expression from Sql.Database to AzureStorage.DataLake OneLake URL, apply changes, and frame. Local study-map skill 3.11 (Choose Between Direct Lake on OneLake and Direct Lake on SQL Analytics Endpoint (and Migrate via TMDL)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Direct Lake overview: Direct Lake on OneLake vs Direct Lake on SQL analytics endpoint (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview).

- **A:** Correct. Correct order: take a version history checkpoint while live editing, script the model in TMDL view, swap the shared M expression from Sql.Database to AzureStorage.DataLake OneLake URL, apply changes, and frame. In this scenario: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the upgrade cleanly.
- **B:** Incorrect for this requirement. Incorrect: Direct Lake models are live-edited in workspaces (not offline Personal Workspace Import files), and OleDb breaks OneLake Direct Lake connectivity. Why the keyed choice wins: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the upgrade cleanly.
- **C:** Incorrect for this requirement. Incorrect: deleting the semantic model breaks downstream thin reports and lineage, and granting Workspace Admin violates security. Why the keyed choice wins: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the upgrade cleanly.
- **D:** Incorrect for this requirement. Incorrect: Direct Lake on OneLake does not support non-materialized SQL views, DirectQuery fallback, or gateways. Why the keyed choice wins: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and framing completes the upgrade cleanly.

### Question 88 — D

Answer: Create case-sensitive DateTime parameters RangeStart and RangeEnd → Apply foldable half-open filter (>= RangeStart and < RangeEnd) → Configure table Incremental refresh policy → Publish to workspace and run initial refresh to generate partitions. Creating case-sensitive `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, setting the incremental refresh policy, and publishing for initial partition generation implements it properly. Correct order: define DateTime RangeStart/RangeEnd parameters, apply >= RangeStart and < RangeEnd preserving query folding, configure table incremental policy, and publish so Fabric generates historical and incremental partitions. Local study-map skill 3.12 (Implement Incremental Refresh and Hybrid Real-Time Partitions (RangeStart/RangeEnd, Detect Data Changes)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Configure incremental refresh and real-time data for Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-overview).

- **A:** Incorrect for this requirement. Incorrect: importing 2 billion rows locally crashes Desktop before partitioning exists, RangeStart belongs in Power Query M, and Incremental Refresh partitions apply to Import/Hybrid tables rather than Direct Lake. Why the keyed choice wins: Creating case-sensitive `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, setting the incremental refresh policy, and publishing for initial partition generation implements it properly.
- **B:** Incorrect for this requirement. Incorrect: parameter names/types must be exact DateTime RangeStart and RangeEnd, breaking query folding pulls the entire table on every refresh, and <= on both bounds double-counts midnight rows. Why the keyed choice wins: Creating case-sensitive `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, setting the incremental refresh policy, and publishing for initial partition generation implements it properly.
- **C:** Incorrect for this requirement. Incorrect: Detect data changes requires an audit/update timestamp column distinct from the date column used to partition RangeStart/RangeEnd. Why the keyed choice wins: Creating case-sensitive `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, setting the incremental refresh policy, and publishing for initial partition generation implements it properly.
- **D:** Correct. Correct order: define DateTime RangeStart/RangeEnd parameters, apply >= RangeStart and < RangeEnd preserving query folding, configure table incremental policy, and publish so Fabric generates historical and incremental partitions. In this scenario: Creating case-sensitive `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, setting the incremental refresh policy, and publishing for initial partition generation implements it properly.

### Question 89 — D

Answer: Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results. `DAX Query View` evaluates multiple query-scoped `DEFINE MEASURE` definitions side-by-side and writes them to the semantic model only when `Update model` is selected. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Local study-map skill 2.18 (Select, Filter, and Aggregate Data Using DAX Queries (DAX Query View, EVALUATE, SUMMARIZECOLUMNS, INFO.VIEW)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Work with DAX query view & INFO.VIEW functions in Power BI (https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view).

- **A:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: `DAX Query View` evaluates multiple query-scoped `DEFINE MEASURE` definitions side-by-side and writes them to the semantic model only when `Update model` is selected.
- **B:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: `DAX Query View` evaluates multiple query-scoped `DEFINE MEASURE` definitions side-by-side and writes them to the semantic model only when `Update model` is selected.
- **C:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `DAX Query View` evaluates multiple query-scoped `DEFINE MEASURE` definitions side-by-side and writes them to the semantic model only when `Update model` is selected.
- **D:** Correct. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. In this scenario: `DAX Query View` evaluates multiple query-scoped `DEFINE MEASURE` definitions side-by-side and writes them to the semantic model only when `Update model` is selected.

### Question 90 — D

Answer: EVALUATE INFO.VIEW.MEASURES(). `EVALUATE INFO.VIEW.MEASURES()` queries the model's measure metadata directly inside DAX Query View. INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags. Local study-map skill 2.18 (Select, Filter, and Aggregate Data Using DAX Queries (DAX Query View, EVALUATE, SUMMARIZECOLUMNS, INFO.VIEW)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Work with DAX query view & INFO.VIEW functions in Power BI (https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view).

- **A:** Incorrect for this requirement. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Why the keyed choice wins: `EVALUATE INFO.VIEW.MEASURES()` queries the model's measure metadata directly inside DAX Query View.
- **B:** Incorrect for this requirement. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Why the keyed choice wins: `EVALUATE INFO.VIEW.MEASURES()` queries the model's measure metadata directly inside DAX Query View.
- **C:** Incorrect for this requirement. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. Why the keyed choice wins: `EVALUATE INFO.VIEW.MEASURES()` queries the model's measure metadata directly inside DAX Query View.
- **D:** Correct. INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags. In this scenario: `EVALUATE INFO.VIEW.MEASURES()` queries the model's measure metadata directly inside DAX Query View.

### Question 91 — A

Answer: Pass simple column predicates wrapped in KEEPFILTERS(DimProduct[Color] = "Red") to CALCULATE instead of FILTER(ALL(FactSales), ...). `KEEPFILTERS('DimChannel'[Channel] = "Paid Social")` intersects with active report slicer selections so `"Search"` rows evaluate cleanly to `BLANK()`. KEEPFILTERS intersects the predicate with existing report slicer selections rather than overwriting them, and filtering a dimension column avoids scanning the entire multi-million-row fact table in the Formula Engine. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Correct. KEEPFILTERS intersects the predicate with existing report slicer selections rather than overwriting them, and filtering a dimension column avoids scanning the entire multi-million-row fact table in the Formula Engine. In this scenario: `KEEPFILTERS('DimChannel'[Channel] = "Paid Social")` intersects with active report slicer selections so `"Search"` rows evaluate cleanly to `BLANK()`.
- **B:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: `KEEPFILTERS('DimChannel'[Channel] = "Paid Social")` intersects with active report slicer selections so `"Search"` rows evaluate cleanly to `BLANK()`.
- **C:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: `KEEPFILTERS('DimChannel'[Channel] = "Paid Social")` intersects with active report slicer selections so `"Search"` rows evaluate cleanly to `BLANK()`.
- **D:** Incorrect for this requirement. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Why the keyed choice wins: `KEEPFILTERS('DimChannel'[Channel] = "Paid Social")` intersects with active report slicer selections so `"Search"` rows evaluate cleanly to `BLANK()`.

### Question 92 — A

Answer: Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop). `Direct Lake on OneLake` connects directly to OneLake across multiple Fabric items (`Lakehouse` + `Warehouse`) and runs strictly in `DirectLakeOnly` mode without DirectQuery fallback. Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery. Local study-map skill 3.11 (Choose Between Direct Lake on OneLake and Direct Lake on SQL Analytics Endpoint (and Migrate via TMDL)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Direct Lake overview: Direct Lake on OneLake vs Direct Lake on SQL analytics endpoint (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview).

- **A:** Correct. Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery. In this scenario: `Direct Lake on OneLake` connects directly to OneLake across multiple Fabric items (`Lakehouse` + `Warehouse`) and runs strictly in `DirectLakeOnly` mode without DirectQuery fallback.
- **B:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: `Direct Lake on OneLake` connects directly to OneLake across multiple Fabric items (`Lakehouse` + `Warehouse`) and runs strictly in `DirectLakeOnly` mode without DirectQuery fallback.
- **C:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: `Direct Lake on OneLake` connects directly to OneLake across multiple Fabric items (`Lakehouse` + `Warehouse`) and runs strictly in `DirectLakeOnly` mode without DirectQuery fallback.
- **D:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Direct Lake on OneLake` connects directly to OneLake across multiple Fabric items (`Lakehouse` + `Warehouse`) and runs strictly in `DirectLakeOnly` mode without DirectQuery fallback.

### Question 93 — A

Answer: Build a Direct Lake on OneLake composite semantic model combining Direct Lake fact tables from OneLake with Import dimension/target tables using regular relationships. Editing the `Direct Lake on OneLake` semantic model in Power BI web modeling (`Get data` / `Transform data`) adds `Import` tables from SharePoint Excel alongside Direct Lake tables with regular relationships. Direct Lake on OneLake supports true composite models that mix Direct Lake tables from multiple Fabric items with Import tables from any Power Query connector while preserving fast regular (non-limited) relationships. Local study-map skill 3.7 (Design and Build Composite Models (Direct Lake on OneLake + Import, Dual + Aggregations, DirectQuery over PBI)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use composite models in Power BI Desktop & Direct Lake on OneLake composite models (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-web-modeling).

- **A:** Correct. Direct Lake on OneLake supports true composite models that mix Direct Lake tables from multiple Fabric items with Import tables from any Power Query connector while preserving fast regular (non-limited) relationships. In this scenario: Editing the `Direct Lake on OneLake` semantic model in Power BI web modeling (`Get data` / `Transform data`) adds `Import` tables from SharePoint Excel alongside Direct Lake tables with regular relationships.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Editing the `Direct Lake on OneLake` semantic model in Power BI web modeling (`Get data` / `Transform data`) adds `Import` tables from SharePoint Excel alongside Direct Lake tables with regular relationships.
- **C:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: Editing the `Direct Lake on OneLake` semantic model in Power BI web modeling (`Get data` / `Transform data`) adds `Import` tables from SharePoint Excel alongside Direct Lake tables with regular relationships.
- **D:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Editing the `Direct Lake on OneLake` semantic model in Power BI web modeling (`Get data` / `Transform data`) adds `Import` tables from SharePoint Excel alongside Direct Lake tables with regular relationships.

### Question 94 — B

Answer: Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes. Triggering a semantic-model `framing` refresh (via Data Factory `Semantic model refresh` activity or Enhanced Refresh API) repoints the model to the latest committed Delta log Parquet files in seconds. Framing is a fast metadata-only operation updating the Direct Lake model's pointer to the latest Delta transaction log Parquet files and evicting stale resident columns so new ETL rows become visible consistently. Local study-map skill 3.10 (Configure Direct Lake Framing, Transcoding, V-Order/OPTIMIZE Guardrails, and DirectLakeBehavior Fallback), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: How Direct Lake works (framing, transcoding, V-Order, fallback & DirectLakeBehavior) (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works).

- **A:** Incorrect for this requirement. Direct Lake on OneLake operates exclusively in DirectLakeOnly mode and never falls back to DirectQuery; exceeding capacity guardrails fails framing/queries until Delta tables or SKU sizing are optimized. Why the keyed choice wins: Triggering a semantic-model `framing` refresh (via Data Factory `Semantic model refresh` activity or Enhanced Refresh API) repoints the model to the latest committed Delta log Parquet files in seconds.
- **B:** Correct. Framing is a fast metadata-only operation updating the Direct Lake model's pointer to the latest Delta transaction log Parquet files and evicting stale resident columns so new ETL rows become visible consistently. In this scenario: Triggering a semantic-model `framing` refresh (via Data Factory `Semantic model refresh` activity or Enhanced Refresh API) repoints the model to the latest committed Delta log Parquet files in seconds.
- **C:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Triggering a semantic-model `framing` refresh (via Data Factory `Semantic model refresh` activity or Enhanced Refresh API) repoints the model to the latest committed Delta log Parquet files in seconds.
- **D:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: Triggering a semantic-model `framing` refresh (via Data Factory `Semantic model refresh` activity or Enhanced Refresh API) repoints the model to the latest committed Delta log Parquet files in seconds.

### Question 95 — A

Answer: Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake. A Data Factory Pipeline `Copy activity` (or Copy job) moves bulk binary/Parquet logs at high throughput and minimal CU cost. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Correct. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. In this scenario: A Data Factory Pipeline `Copy activity` (or Copy job) moves bulk binary/Parquet logs at high throughput and minimal CU cost.
- **B:** Incorrect for this requirement. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` (or Copy job) moves bulk binary/Parquet logs at high throughput and minimal CU cost.
- **C:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` (or Copy job) moves bulk binary/Parquet logs at high throughput and minimal CU cost.
- **D:** Incorrect for this requirement. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` (or Copy job) moves bulk binary/Parquet logs at high throughput and minimal CU cost.

### Question 96 — D

Answer: Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations. `Dataflow Gen2` with `Fast Copy` and staging enabled combines visual M transformations with high-speed Copy backend ingestion. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. Why the keyed choice wins: `Dataflow Gen2` with `Fast Copy` and staging enabled combines visual M transformations with high-speed Copy backend ingestion.
- **B:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: `Dataflow Gen2` with `Fast Copy` and staging enabled combines visual M transformations with high-speed Copy backend ingestion.
- **C:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: `Dataflow Gen2` with `Fast Copy` and staging enabled combines visual M transformations with high-speed Copy backend ingestion.
- **D:** Correct. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. In this scenario: `Dataflow Gen2` with `Fast Copy` and staging enabled combines visual M transformations with high-speed Copy backend ingestion.

### Question 97 — C

Answer: Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled. `Table.AddIndexColumn` does not fold to PostgreSQL, pulling the entire unfiltered historical table before filtering; moving native date filtering and column selection BEFORE `Index Column` restores `View Native Query` folding. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. Local study-map skill 2.14 (Filter Data Early Preserving Power Query Folding (View Native Query) and Sargable Delta File Pruning), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query folding indicators & predicate pushdown in Power Query and Delta Lake (https://learn.microsoft.com/en-us/power-query/query-folding-basics).

- **A:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: `Table.AddIndexColumn` does not fold to PostgreSQL, pulling the entire unfiltered historical table before filtering; moving native date filtering and column selection BEFORE `Index Column` restores `View Native Query` folding.
- **B:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `Table.AddIndexColumn` does not fold to PostgreSQL, pulling the entire unfiltered historical table before filtering; moving native date filtering and column selection BEFORE `Index Column` restores `View Native Query` folding.
- **C:** Correct. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. In this scenario: `Table.AddIndexColumn` does not fold to PostgreSQL, pulling the entire unfiltered historical table before filtering; moving native date filtering and column selection BEFORE `Index Column` restores `View Native Query` folding.
- **D:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: `Table.AddIndexColumn` does not fold to PostgreSQL, pulling the entire unfiltered historical table before filtering; moving native date filtering and column selection BEFORE `Index Column` restores `View Native Query` folding.

### Question 98 — D

Answer: Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository. Ensuring `.gitignore` contains `**/cache.abf` and `**/localSettings.json` keeps local cached model data and personal settings untracked by Git. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Local study-map skill 1.7 (Create and Manage Power BI Desktop Projects (.pbip) with TMDL, PBIR, and .gitignore Hygiene), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Power BI Desktop projects (.pbip), TMDL, and PBIR (https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview).

- **A:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Ensuring `.gitignore` contains `**/cache.abf` and `**/localSettings.json` keeps local cached model data and personal settings untracked by Git.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Ensuring `.gitignore` contains `**/cache.abf` and `**/localSettings.json` keeps local cached model data and personal settings untracked by Git.
- **C:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Ensuring `.gitignore` contains `**/cache.abf` and `**/localSettings.json` keeps local cached model data and personal settings untracked by Git.
- **D:** Correct. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. In this scenario: Ensuring `.gitignore` contains `**/cache.abf` and `**/localSettings.json` keeps local cached model data and personal settings untracked by Git.

### Question 99 — C

Answer: Use Undo in the Fabric Workspace Source control pane to discard uncommitted workspace edits back to the last synced commit. Selecting `Undo` in the Workspace Source control pane reverts uncommitted workspace item changes back to the connected branch HEAD. Undo reverts uncommitted workspace item modifications to match the connected Git branch HEAD without rewriting shared remote commit history. Local study-map skill 1.6 (Configure Workspace Version Control with Azure DevOps or GitHub (Branch Out, Commit, Update, Undo)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to Git integration in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration).

- **A:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Selecting `Undo` in the Workspace Source control pane reverts uncommitted workspace item changes back to the connected branch HEAD.
- **B:** Incorrect for this requirement. In Fabric Git integration, workspaces map 1-to-1 to branches; branching out into a dedicated developer workspace isolates in-progress notebook, pipeline, and semantic model edits before merging via pull request. Why the keyed choice wins: Selecting `Undo` in the Workspace Source control pane reverts uncommitted workspace item changes back to the connected branch HEAD.
- **C:** Correct. Undo reverts uncommitted workspace item modifications to match the connected Git branch HEAD without rewriting shared remote commit history. In this scenario: Selecting `Undo` in the Workspace Source control pane reverts uncommitted workspace item changes back to the connected branch HEAD.
- **D:** Incorrect for this requirement. Fabric Git sync is explicit rather than automatic on remote push: developers Commit workspace edits to their branch, complete a PR in Azure DevOps or GitHub, and run Update from Git in the downstream workspace. Why the keyed choice wins: Selecting `Undo` in the Workspace Source control pane reverts uncommitted workspace item changes back to the connected branch HEAD.

### Question 100 — B

Answer: Connect shared Dev workspace to main → Branch out to an isolated developer workspace and commit .pbip/Notebook edits → Merge pull request into main in Git → Run Update all in Dev and promote via Deployment Pipeline. Fabric Git sync requires explicitly selecting `Update all` in the `Dev` workspace after a PR merges into `main` before promoting items through the Deployment Pipeline. Correct order: link Dev to main, branch out to an isolated workspace for feature work, validate and merge via Git PR into main, run Update all in Dev, and promote via Deployment Pipeline with stage rules. Local study-map skill 1.6 (Configure Workspace Version Control with Azure DevOps or GitHub (Branch Out, Commit, Update, Undo)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to Git integration in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration).

- **A:** Incorrect for this requirement. Incorrect: editing Production directly on feature branches and committing cache.abf violates ALM isolation, leaks cached data, and bypasses Test validation. Why the keyed choice wins: Fabric Git sync requires explicitly selecting `Update all` in the `Dev` workspace after a PR merges into `main` before promoting items through the Deployment Pipeline.
- **B:** Correct. Correct order: link Dev to main, branch out to an isolated workspace for feature work, validate and merge via Git PR into main, run Update all in Dev, and promote via Deployment Pipeline with stage rules. In this scenario: Fabric Git sync requires explicitly selecting `Update all` in the `Dev` workspace after a PR merges into `main` before promoting items through the Deployment Pipeline.
- **C:** Incorrect for this requirement. Incorrect: Fabric workspaces do not auto-pull remote PR merges — skipping Update from Git promotes stale pre-PR workspace state to Test. Why the keyed choice wins: Fabric Git sync requires explicitly selecting `Update all` in the `Dev` workspace after a PR merges into `main` before promoting items through the Deployment Pipeline.
- **D:** Incorrect for this requirement. Incorrect: My Workspace does not support full team Git ALM, Undo discards local changes rather than committing, and deleting .platform breaks item lineage. Why the keyed choice wins: Fabric Git sync requires explicitly selecting `Update all` in the `Dev` workspace after a PR merges into `main` before promoting items through the Deployment Pipeline.
