# Microsoft Exam DP-600: Implementing Analytics Solutions Using Microsoft Fabric — Full-Length Mock Exam 3

Exam DP-600 (Global FinTech Ledger Mirroring, Fraud KQL Streams, and Enterprise XMLA ALM) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint & Credential Notice:** Aligned to the official **October 19, 2026** DP-600 study guide (`Microsoft Certified: Fabric Analytics Engineer Associate`). Associate-level certification with **no prerequisite exam required**, free online annual renewal on Microsoft Learn, split-screen `learn.microsoft.com` access during non-lab exam sections, and hands-on coverage across **SQL**, **KQL**, **DAX**, **PySpark**, **Power Query M**, **TMDL**, and **TMSL**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` SQL/KQL/DAX/PySpark/M/TMDL/TMSL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Microsoft Fabric case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area SQL/KQL/DAX/TMDL dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn Fabric and Power BI documentation — never recalled live items or copied Microsoft sample case studies.

## Questions

### 1. A quantitative risk engineer needs to author Spark notebooks, Lakehouses, and Data Factory pipelines inside `Treasury-Dev` but must not grant access to other users or publish organizational apps. Which workspace role enforces least privilege?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Admin role
- B. Assign the Workspace Contributor role
- C. Assign the Workspace Viewer role
- D. Assign the Workspace Member role

### 2. Proposed solution: Branch managers are placed in the `RetailBanking-Prod` workspace `Member` role so they can view regional branch scorecards restricted by DAX RLS. Does DAX RLS filter `Member` users, and what role should they hold instead?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Viewer role
- B. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows
- C. Assign the Workspace Member role
- D. Assign the Workspace Contributor role

### 3. Two release managers in `CapitalMarkets-Prod` must publish workspace Apps, share semantic models, and configure OneLake security roles, without having permission to delete the workspace, and memberships must sync from corporate IAM. Which two choices apply? Select two.

Domain: Maintain a data analytics solution

- A. Assign the Workspace Viewer role
- B. Assign the Workspace Member role
- C. Assign permissions to Microsoft Entra security groups rather than individual users
- D. Assign the Workspace Admin role
- E. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows

### 4. Credit-committee executives hold `Read` permission on a `CreditPortfolio` Direct Lake report, and audit rules forbid granting executives any direct `ReadData` or `ReadAll` permissions on the underlying `CreditLakehouse`. How must the Direct Lake semantic model authenticate to `CreditLakehouse`?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Contributor role
- B. Bind the Direct Lake semantic model to a cloud connection with a fixed identity and disable SSO
- C. Share the Lakehouse with ReadAll (Read all Apache Spark data) permission
- D. Enable single sign-on (SSO) on the Direct Lake semantic model connection

### 5. Fixed-income analysts want to connect Excel PivotTables (`Analyze in Excel`) and live thin Power BI Desktop reports to the Certified `BondBook` semantic model without editing the model. Which minimum item permission on `BondBook` is required?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Admin role
- B. Share the item with Read permission only (no ReadData or ReadAll)
- C. Share the Lakehouse with ReadAll (Read all Apache Spark data) permission
- D. Grant Build permission on the shared semantic model

### 6. Proposed solution: On `GoldLoanLedger`, a security admin creates OneLake security `Role_East` with an RLS filter (`BranchRegion = 'East'`) and `Role_NoSSN` with a CLS rule hiding `BorrowerSSN`, then assigns loan officers to both roles. What happens when loan officers query `GoldLoanLedger`, and how do you fix it?

Domain: Maintain a data analytics solution

- A. Create a OneLake security role with ReadWrite permission and attach an RLS predicate
- B. Define both the RLS filter and CLS column allow-list inside a single OneLake security Grant role with Read permission
- C. Create a Deny role in OneLake security to revoke table access granted by another OneLake role or Workspace Member role
- D. Create two separate OneLake security roles on the same table — Role A containing the RLS filter and Role B containing the CLS column rule — and assign the user to both

### 7. Regulatory analysts connect via SSMS to `ComplianceWarehouse` and must run `SELECT LoanId, OriginationDate, PrincipalAmt FROM dbo.Loans` (`GRANT SELECT ON dbo.Loans(____) TO [RegAuditors]`), while queries referencing `BorrowerTaxId` must be denied at the SQL engine layer. Which control enforces this?

Domain: Maintain a data analytics solution

- A. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- B. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- C. Grant T-SQL column-level SELECT on only the non-sensitive columns (GRANT SELECT ON dbo.Customer(CustomerID, Region) TO ...)
- D. Mark the item as Promoted in item settings

### 8. Which four-step architecture enforces OneLake security roles consistently across a central `CoreLedgerLakehouse` and downstream shortcut workspaces?

Domain: Maintain a data analytics solution

- A. Enable OneLake security and define Read Grant roles → Assign consumers Workspace Viewer and OneLake security roles → Set SQL analytics endpoint to User's identity mode → Expose downstream shortcuts in User's identity mode
- B. Set SQL analytics endpoint to Delegated mode with SQL DENY rules → Remove Workspace Viewer assignments → Enable OneLake security afterward → Export binary .pbix copies
- C. Assign consumers the Workspace Contributor role → Enable OneLake security with a Deny role → Keep SQL analytics endpoint in Owner fixed identity mode → Create downstream shortcuts
- D. Create downstream shortcuts first → Assign consumers Workspace Member rights → Attach RLS predicates to a ReadWrite OneLake role → Enable SSO on an On-premises gateway

### 9. Investment banking compliance requires that junior analysts with `Build` permission on `DealPipelineModel` cannot even discover that the `[AdvisoryFee_USD]` column or its dependent measures exist in metadata, and you must verify the restriction as `analyst1@clearledger.com`. Which two steps are required? Select two.

Domain: Maintain a data analytics solution

- A. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- B. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- C. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- D. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows
- E. Filter the RLS table using USERNAME() = [DomainLogin] without testing in the Fabric portal

### 10. When a financial controller applies a `Strictly Confidential — MNPI` Purview sensitivity label to `EquitiesWarehouse`, how does Fabric protect newly built downstream semantic models and reports?

Domain: Maintain a data analytics solution

- A. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal
- B. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages
- C. Apply a Microsoft Purview sensitivity label with downstream inheritance on the source Lakehouse or Warehouse
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 11. Board members export a labeled `QuarterlyCapitalRatio` report to PDF and `.xlsx` attachments. Which Purview label capability ensures unauthorized users outside the `Board-of-Directors` Entra group cannot open those exported files?

Domain: Maintain a data analytics solution

- A. Use a Purview sensitivity label configured with file encryption so exported .pbix, Excel, PDF, and PowerPoint files stay protected outside Fabric
- B. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- C. Mark the item as Promoted in item settings
- D. Apply T-SQL Dynamic Data Masking (MASKED WITH (FUNCTION = 'partial(...)')) on sensitive columns

### 12. Risk regulators require that all Basel III capital reports connect exclusively to semantic models formally signed off by the bank's Enterprise Data Governance Office. Which endorsement badge represents that sign-off?

Domain: Maintain a data analytics solution

- A. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- B. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal
- C. Assign the Workspace Member role
- D. Mark the item as Promoted in item settings

### 13. Dozens of trading desks maintain conflicting Legal Entity Identifier (`LEI`) lookup tables. Which endorsement setting highlights `GoldCounterpartyLakehouse` in the OneLake catalog as the bank's single authoritative reference repository?

Domain: Maintain a data analytics solution

- A. Configure Certified endorsement with the Master data label on authoritative core tables or semantic models
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- D. Mark the item as Promoted in item settings

### 14. In an isolated `Risk-Feature-VaR` developer workspace linked to Git, an experimental edit corrupts two Dataflow Gen2 definitions before committing. Which Source control pane action reverts those uncommitted workspace edits cleanly back to the last synced Git commit?

Domain: Maintain a data analytics solution

- A. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- B. Use Undo in the Fabric Workspace Source control pane to discard uncommitted workspace edits back to the last synced commit
- C. Commit workspace changes to Git from the Source control pane, merge via pull request, then select Update all in the target workspace
- D. Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch

### 15. Which four-step sequence moves a validated `.pbip` and Spark notebook update from an isolated developer workspace through GitHub pull-request review into `Test` and `Production`?

Domain: Maintain a data analytics solution

- A. Connect Production directly to a feature branch → Edit semantic models live in Prod → Force-push binary .pbix files including cache.abf to main → Deploy backward to Development
- B. Connect shared Dev workspace to main → Branch out to an isolated developer workspace and commit .pbip/Notebook edits → Merge pull request into main in Git → Run Update all in Dev and promote via Deployment Pipeline
- C. Branch out to personal My Workspace → Run Undo to push changes to GitHub → Delete .platform metadata files → Copy visuals manually into Production
- D. Edit items directly on main without branching → Merge an empty PR → Promote Dev to Test before running Update from Git → Configure Git integration last

### 16. In a `.pbip` repository, under `<ModelName>.SemanticModel/definition/tables/FactTrades.____`, each table's columns, measures, partitions, and M expressions are stored as clean indentation-based text rather than a giant monolithic `model.bim` JSON file. Which serialization format is this?

Domain: Maintain a data analytics solution

- A. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode

### 17. Before committing a new `.pbip` wealth-management project to Azure Repos, which two repository checks ensure pull requests show granular measure diffs without committing cached account balances or personal UI settings? Select two.

Domain: Maintain a data analytics solution

- A. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- D. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- E. Configure DirectQuery storage mode

### 18. In `Payments-Dev`, `SettlementReport` and its newly created `SettlementSemanticModel` are ready for UAT in `Payments-Test`, while three in-progress fraud notebooks must stay in `Payments-Dev`. How should you promote to `Payments-Test`?

Domain: Maintain a data analytics solution

- A. Configure Deployment pipeline data source and parameter rules on the Test and Production stages
- B. Perform a selective deployment selecting the modified item together with Select related to include required upstream dependencies
- C. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline
- D. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition

### 19. A Direct Lake on SQL semantic model in `Dev` points to `DevLedgerWarehouse`'s SQL endpoint. Which Deployment Pipeline configuration automatically rebinds the `Test` and `Production` copies to `TestLedgerWarehouse` and `ProdLedgerWarehouse` on deployment?

Domain: Maintain a data analytics solution

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- C. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline
- D. Configure Deployment pipeline data source and parameter rules on the Test and Production stages

### 20. Note that `Direct Lake on OneLake` models and Data Factory `Copy` pipelines do not use legacy SQL deployment rules. Which Fabric CI/CD artifact lets you define stage-specific `WorkspaceId`, `LakehouseId`, and key-vault URI variables across `Dev`, `Test`, and `Prod`?

Domain: Maintain a data analytics solution

- A. Configure Deployment pipeline data source and parameter rules on the Test and Production stages
- B. Use a Fabric Variable library (or autobinding across paired workspace items) to parameterize stage-specific environment references
- C. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode

### 21. Before retiring `LegacyFXDataflow` in `Markets-Shared`, you must verify whether any executive dashboards in `Wealth-Prod`, `Retail-Prod`, or `Risk-Prod` still depend on it and send deprecation notices to their owners. Which feature should you use?

Domain: Maintain a data analytics solution

- A. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- B. Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts

### 22. Proposed solution: An engineer checks `EVALUATE INFO.VIEW.TABLES()` inside `LegacyFXModel` to find out which external workspaces have thin reports connected to `LegacyFXModel`. Does `INFO.VIEW.TABLES()` list downstream reports, and what tool does?

Domain: Maintain a data analytics solution

- A. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- B. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- C. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- D. Mark the item as Promoted in item settings

### 23. Commercial lending regional offices need an offline-capable Power BI Desktop starter file preloaded with corporate visuals, DAX credit ratios, and a `BranchRegionCode` query parameter prompt, containing zero customer data rows. Which file should you export?

Domain: Maintain a data analytics solution

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- D. Publish a single certified core semantic model in a data workspace and build thin live-connected Power BI reports in departmental workspaces

### 24. You want Treasury analysts launching Power BI Desktop to connect immediately to `TreasuryWarehouse`'s SQL endpoint (`xyz.datawarehouse.fabric.microsoft.com`) without copying URLs from Confluence. Which JSON launcher file accomplishes this?

Domain: Maintain a data analytics solution

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- C. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- D. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)

### 25. Five Data Factory pipelines ingest market exchange rates from a public cloud REST API authenticated via OAuth2 / Service Principal. How do you avoid embedding credentials inside five separate pipeline definitions?

Domain: Prepare data

- A. Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication
- B. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- C. Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet
- D. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network

### 26. Where in Microsoft Fabric can a banking data steward simultaneously review the count of unendorsed semantic models, sensitivity-label coverage percentages, and recommended governance actions across all workspaces they own?

Domain: Prepare data

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- C. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- D. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results

### 27. Quantitative analysts want to (1) discover `Certified` fixed-income Lakehouses filtered by the `Markets` domain, and (2) subscribe to live `Fabric capacity overview events` and SWIFT payment streams to trigger overage alerts via Activator. Which two discovery hubs should they use? Select two.

Domain: Prepare data

- A. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- B. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- C. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- E. Use the Real-Time hub to subscribe to Microsoft.Fabric.OneLake.FileCreated events (or Capacity/CDC streams) and trigger an Activator rule

### 28. Market-data vendors deliver 250 TB of historical tick-level Delta Parquet tables into an external Azure Data Lake Storage Gen2 account. How should you expose those tables inside `QuantLakehouse` with zero storage duplication?

Domain: Prepare data

- A. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- B. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- C. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- D. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching

### 29. Regulatory archiving requires copying 1.8 TB of fixed-width mainframe settlement files from an on-premises file share (via On-premises gateway) into `BronzeLakehouse/Files/mainframe/` every night at minimal CU cost without row transformations. Which tool is optimal?

Domain: Prepare data

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- C. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- D. Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table

### 30. Proposed solution: Regulatory reconciliation flags duplicate `SettlementBatchId` rows in `silver.stg_ach_batches`, so an analyst runs `SELECT DISTINCT *` even though retry rows carry slightly different `IngestionEpochMs` values. Why does `SELECT DISTINCT *` fail to deduplicate them, and what works?

Domain: Prepare data

- A. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- B. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- C. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- D. Deduplicate using ROW_NUMBER() OVER (PARTITION BY BusinessKey ORDER BY ModifiedTimestamp DESC) = 1

### 31. Select the three Fabric ingestion/virtualization patterns that avoid custom scheduled batch ETL scripts when accessing: (1) existing Amazon S3 Parquet lakes, (2) live Kafka card-swipe streams, and (3) operational Azure Cosmos DB NoSQL containers. Select three.

Domain: Prepare data

- A. Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table
- B. Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog
- C. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- E. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- F. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 32. General-ledger controllers require multi-table ACID transactions (`BEGIN TRAN ... COMMIT`) rolling back both `FactJournalEntries` and `FactTrialBalance` if debits do not equal credits, written purely in T-SQL. Which Fabric store must you select?

Domain: Prepare data

- A. Choose a Fabric Eventhouse (KQL database)
- B. Choose a SQL database in Microsoft Fabric
- C. Choose a Fabric Lakehouse
- D. Choose a Fabric Data Warehouse

### 33. Algorithmic trading compliance ingests 1.2 million FIX protocol JSON order-book events per second and runs ad-hoc KQL time-window pattern matching over the trailing 90 days. Which Fabric store is designed for this?

Domain: Prepare data

- A. Configure Import storage mode
- B. Choose a Fabric Data Warehouse
- C. Choose a Fabric Lakehouse
- D. Choose a Fabric Eventhouse (KQL database)

### 34. A digital bank builds (1) an operational microservice backend storing customer dispute tickets with sub-10 ms row-level OLTP writes inside Fabric, and (2) a Spark ML workspace processing PDF check scans in `Files/` plus Silver Delta tables. Which two Fabric stores fit? Select two.

Domain: Prepare data

- A. Choose a Fabric Lakehouse
- B. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Choose a SQL database in Microsoft Fabric
- E. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)

### 35. Proposed solution: A fraud data scientist tries to read an Eventhouse KQL table `WireAlerts` from a PySpark notebook via an ABFSS OneLake URI, but no Delta Parquet folder exists in OneLake. Why, and which setting on the KQL database creates it?

Domain: Prepare data

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- C. Enable OneLake availability on the Eventhouse KQL database (or specific KQL table) and create an internal OneLake shortcut in the Lakehouse
- D. Point Direct Lake on SQL directly at an Eventhouse KQL database without enabling OneLake availability

### 36. In which four-step order do you integrate streaming ATM telemetry from an Eventhouse into a Lakehouse shortcut and a Direct Lake on OneLake semantic model?

Domain: Prepare data

- A. Export KQL query results manually to CSV every hour → Email CSVs to analysts → Import into binary .pbix files → Publish to My Workspace
- B. Create an Amazon S3 external shortcut to the KQL URI before enabling OneLake availability → Set storage mode to Dual only → Enable Auto date/time → Run XMLA clearValues
- C. Create a Direct Lake on SQL model directly over the KQL queryset → Disable OneLake availability → Configure an On-premises data gateway → Run T-SQL MERGE on the KQL database
- D. Ingest streaming telemetry into an Eventhouse KQL database → Enable OneLake availability on the KQL database or table → Create an internal OneLake shortcut in the Lakehouse → Add the table to a Direct Lake on OneLake semantic model

### 37. In `TreasuryWarehouse`, you author `CREATE PROCEDURE dbo.usp_PostDailyAccruals @AsOfDate DATE AS ...` to run staging validations, `MERGE` dimension updates, and `INSERT` accrual facts. Why can't this exact T-SQL procedure run inside a Lakehouse SQL analytics endpoint?

Domain: Prepare data

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- C. Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic
- D. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint

### 38. A capital-markets semantic model built with Direct Lake on OneLake needs a pre-joined Gold customer-account projection from `LedgerLakehouse`. Why should you persist a Gold Delta table or `Materialized Lake View` instead of a standard SQL analytics endpoint `CREATE VIEW`?

Domain: Prepare data

- A. Use a Lakehouse Materialized Lake View (or persisted Gold Delta table) instead of a non-materialized SQL analytics endpoint view for Direct Lake on OneLake
- B. Configure DirectQuery storage mode
- C. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- D. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes

### 39. Complete `CREATE VIEW reporting.vw_ActiveLoans AS ____ LoanKey, AccountNumber, PrincipalBalance FROM gold.FactLoans WHERE LoanStatus = 'Active';` — when report users query `vw_ActiveLoans` in `LoansWarehouse` without permissions on `gold.FactLoans`, how does SQL ownership chaining help?

Domain: Prepare data

- A. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- B. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- C. Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic
- D. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear

### 40. Commercial loan accounts use 24-character IBAN strings across European subsidiaries. Why should `Gold.DimAccount` assign a 4-byte `INT` `AccountKey` surrogate key referenced by `FactDailyBalances`?

Domain: Prepare data

- A. Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- D. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension

### 41. Bond settlement analytics must skip NYSE/TARGET2 bank holidays, track business-day counts per month, and align fiscal quarters starting April 1 across `FactTrades` and `FactCoupons`. How should you enrich the Gold schema?

Domain: Prepare data

- A. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- B. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- C. Configure DirectQuery storage mode
- D. Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes

### 42. A Silver PySpark notebook parses 500 million SWIFT message strings (`df.____("BIC8", F.substring("RawBIC", 1, 8))`) and assigns integer dimension keys, replacing a slow Python `for` loop over `.collect()`. Which two PySpark/dimensional practices make this scalable? Select two.

Domain: Prepare data

- A. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- B. Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions
- C. Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs
- D. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- E. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals

### 43. When a borrower's internal credit rating downgrades from `AA` to `BBB` on September 15, Q1 and Q2 risk exposure reports must still show `AA` while Q4 reports show `BBB`. Which dimension design on `DimBorrower` is required?

Domain: Prepare data

- A. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)
- B. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns
- C. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- D. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place

### 44. A junior developer joins `FactLoanHeaders` (`OriginationFee`) to `FactMonthlyPayments` (`PaymentAmount`) into one wide table, inflating `SUM(OriginationFee)` 36x on a 36-month loan. How do you fix the dimensional design?

Domain: Prepare data

- A. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- D. Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures

### 45. Which four-step ELT pipeline sequence maintains `DimRelationshipManager` as an accurate SCD Type 2 table when managers move between private-banking regions?

Domain: Prepare data

- A. Insert new versions with IsCurrent = 0 first → Overwrite old EffectiveStartDate values in place → Remove the natural business key column → Deduplicate after publishing reports
- B. Insert raw duplicate staging rows directly into FactSales → Delete unmatched dimension keys → Leave EffectiveStartDate NULL → Enable Assume referential integrity on broken keys
- C. Stage and deduplicate incoming records by natural key → Compare tracked attributes against active (IsCurrent = 1) Gold rows → Expire changed active rows (EffectiveEndDate, IsCurrent = 0) → Insert new active versions with fresh surrogate keys
- D. Truncate the Gold dimension table → Reassign fresh random surrogate keys to all historical rows → Join historical facts without updating foreign keys → Set IsCurrent = 1 on every version

### 46. Which three lakehouse/warehouse modeling standards protect a regulated banking Gold layer from lost late-arriving wire facts and historical restatement errors? Select three.

Domain: Prepare data

- A. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- B. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- C. Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE
- D. Organize OneLake into Bronze (raw immutable), Silver (validated, deduplicated, conformed), and Gold (star-schema dimensions and facts with V-Order)
- E. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns
- F. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension

### 47. In the core banking ERP, `CostCenter` joins to `Department`, which joins to `BusinessUnit`, which joins to `LegalEntity`. How should you transform this hierarchy for `Gold.DimCostCenter`?

Domain: Prepare data

- A. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()
- B. Configure DirectQuery storage mode
- C. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- D. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension

### 48. Why does flattening `Instrument -> AssetSubClass -> AssetClass` into one `DimInstrument` table improve Direct Lake transcoding efficiency compared to keeping three separate snowflaked dimension tables?

Domain: Prepare data

- A. Choose a Fabric Eventhouse (KQL database)
- B. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- C. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 49. High-frequency market-making desks record 15 billion quote updates daily in Bronze/Silver, while Risk Committee dashboards display only end-of-hour net delta and VWAP per ticker. What Gold table strategy minimizes Direct Lake memory?

Domain: Prepare data

- A. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Configure DirectQuery storage mode
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging

### 50. Complete `SELECT Desk, AssetClass, SUM(PnL) AS TotalPnL FROM gold.FactDailyPnL ____;` so one T-SQL query returns `(Desk, AssetClass)`, `(Desk)` only, and overall bank `()` totals without scanning `FactDailyPnL` three times via `UNION ALL`?

Domain: Prepare data

- A. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- B. | summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)
- C. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- D. TRY_CAST(RawReading AS DECIMAL(18, 4))

### 51. When summarizing ledger balances in SQL or Power Query before loading Gold summary tables, why must `EndOfDayBalance` (a semi-additive snapshot balance) NOT be aggregated with `SUM()` across `DateKey`?

Domain: Prepare data

- A. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- B. Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table
- C. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- D. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals

### 52. Complete `MERGE INTO gold.FactWireTransfers t USING silver.StgWires s ON t.WireId = s.WireId ____ t.SettlementStatus = s.SettlementStatus WHEN NOT MATCHED THEN INSERT ...;` to skip rewriting Parquet files when `RowHash` has not changed?

Domain: Prepare data

- A. CAST(RawReading AS FLOAT)
- B. RANK() OVER (ORDER BY SpecimenId DESC)
- C. WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET
- D. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'

### 53. An AML reconciliation step must output all rows from `ExternalSwiftConfirmations` that have zero matching `WireId` in `InternalLedgerWires`. Which join operation isolates those unrecorded wires?

Domain: Prepare data

- A. Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement
- B. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- C. Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table
- D. Apply broadcast(dim_df) in PySpark when joining a multi-hundred-million-row fact DataFrame with a small dimension DataFrame

### 54. A Spark job enriches 1.4 billion card transactions with a 3 MB `dim_mcc_codes` merchant-category table (`tx_df.join(____)`) and upserts settled statuses into `gold.fact_card_tx`. Which two patterns avoid cluster shuffles and maintain ACID consistency? Select two.

Domain: Prepare data

- A. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- B. Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement
- C. fact_df.join(F.broadcast(dim_store_df), on="StoreKey", how="left")
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- E. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint

### 55. Payment gateway webhooks deliver at-least-once events, creating duplicate `PaymentId` records in `silver.stg_payments`. Complete `SELECT *, ____ AS rn FROM silver.stg_payments` so filtering `WHERE rn = 1` keeps strictly one latest status per payment?

Domain: Prepare data

- A. TRY_CAST(RawReading AS DECIMAL(18, 4))
- B. RANK() OVER (ORDER BY SpecimenId DESC)
- C. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- D. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())

### 56. You onboard a legacy mortgage acquisition feed: Power Query's top-1,000-row bar shows `100% Valid`, yet row 480,000 has null `BranchCode` values that later vanish from `INNER JOIN` reports. Which two practices catch and handle this properly? Select two.

Domain: Prepare data

- A. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- B. Launch Data Wrangler from a Fabric Spark notebook (or enable Power Query Column profiling based on entire data set) to inspect nulls, duplicates, and distributions and export generated PySpark code
- C. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- D. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- E. Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE

### 57. Mainframe COBOL extracts occasionally place `"PENDING"` inside the `InterestRatePct` text column (`SELECT LoanId, ____ AS CleanRate FROM stage.CobolLoans;`). Which T-SQL expression converts valid rates to exact 4-decimal fixed point while turning `"PENDING"` into `NULL` without aborting the load?

Domain: Prepare data

- A. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- B. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- C. CAST(RawReading AS FLOAT)
- D. TRY_CAST(RawReading AS DECIMAL(18, 4))

### 58. Proposed solution: A Spark engineer writes a `Gold.FactSettlements` Delta table containing `PayloadHash` (`BINARY`) and `AuditTrail` (`ARRAY<STRUCT<step:string,ts:timestamp>>`) and expects Direct Lake to expose both columns in Power BI visuals. Why does this fail, and what is required?

Domain: Prepare data

- A. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- B. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- C. Configure shared dimension tables in Dual storage mode inside a composite model
- D. Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake

### 59. In Dataflow Gen2 reading 400 million Oracle ledger rows, an analyst applies `Text.Proper([AccountDescription])` on Step 2 and `PostingDate >= #date(2026, 1, 1)` on Step 3, noticing `View Native Query` is disabled on Step 3. How do you cut refresh time from 48 minutes to 3 minutes?

Domain: Prepare data

- A. Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled
- B. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- C. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 60. On `gold.fact_trades` partitioned by `TradeYear` and Z-Ordered/V-Ordered on `TradeDate`, which T-SQL `WHERE` predicate preserves Parquet rowgroup min/max pruning: `WHERE FORMAT(TradeDate, 'yyyy-MM') = '2026-10'` or `WHERE TradeDate >= '2026-10-01' AND TradeDate < '2026-11-01'`?

Domain: Prepare data

- A. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'
- B. CAST(RawReading AS FLOAT)
- C. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- D. Filter on physical Delta partition or liquid-clustered date columns using sargable range predicates (OrderDate >= '2026-01-01') without wrapping the column in functions

### 61. A treasury operations analyst without SQL fluency wants to visually join `FactCashPositions` and `DimBankAccount` inside `TreasuryWarehouse`, filter `Currency = 'EUR'`, group total cash by `Country`, and save the result as a SQL view for Excel users. Which browser feature should they launch?

Domain: Prepare data

- A. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- B. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results

### 62. Which two capabilities are directly available from the ribbon inside the Fabric `Visual query editor` once an analyst finishes filtering and grouping a Lakehouse SQL analytics endpoint query?

Domain: Prepare data

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- C. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition
- D. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint

### 63. Complete `SELECT PortfolioId, ValuationDate, NetAssetValue, NetAssetValue - ____ AS DailyChange FROM gold.FactNAV;` (conceptually partitioning by entity and ordering by timestamp/date) to compute day-over-day NAV change without self-joining `FactNAV`?

Domain: Prepare data

- A. TRY_CAST(RawReading AS DECIMAL(18, 4))
- B. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- C. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- D. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)

### 64. Regulatory auditors ask ClearLedger's Warehouse team to (1) query `dbo.FactCapitalAdequacy` exactly as it stood at `2026-10-28T06:00:00.000` (`____`), and (2) freeze a zero-copy table clone of `dbo.FactSales` / `dbo.FactPositions` for stress-test sandbox queries. Which two Warehouse T-SQL features apply? Select two.

Domain: Prepare data

- A. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- B. CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales
- C. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- D. OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')
- E. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging

### 65. A quantitative BI developer wants to write `DEFINE MEASURE 'FactTrades'[Test Sharpe] = ... EVALUATE SUMMARIZECOLUMNS('DimDesk'[DeskName], "Sharpe", [Test Sharpe])` against a published workspace semantic model in the browser before committing measure changes. Which feature supports this?

Domain: Prepare data

- A. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results
- B. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- C. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- D. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN

### 66. Complete the DAX Query View statement `____` used by internal model-risk auditors to extract every measure expression, description, and display folder from `WealthModel` for SOX documentation?

Domain: Prepare data

- A. CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))
- B. [ManagerEmail] = USERPRINCIPALNAME()
- C. CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))
- D. EVALUATE INFO.VIEW.MEASURES()

### 67. `LedgerLakehouse` holds 900 million V-Order Delta rows updated every 20 minutes in OneLake, and wealth advisors expect sub-second Power BI visuals without waiting for 45-minute Import refreshes. Which storage mode should you choose?

Domain: Implement and manage semantic models

- A. Configure Direct Lake storage mode
- B. Configure Import storage mode
- C. Configure DirectQuery storage mode
- D. Configure shared dimension tables in Dual storage mode inside a composite model

### 68. A risk composite model combines an `Import` daily VaR summary table with a `DirectQuery` intraday trade-tick Warehouse table, both sharing `DimDesk` and `DimCounterparty`. Which storage mode on `DimDesk` and `DimCounterparty` serves summary visuals from RAM and tick drills via pushed SQL joins?

Domain: Implement and manage semantic models

- A. Configure Import storage mode
- B. Configure DirectQuery storage mode
- C. Configure shared dimension tables in Dual storage mode inside a composite model
- D. Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop)

### 69. In `TreasuryModel`, `DimCalendar[DateKey]` (`INT` `YYYYMMDD`) joins to `FactLiquidity[DateKey]`. Why must you run `Mark as date table` selecting `DimCalendar[CalendarDate]` (`Date` type) for `SAMEPERIODLASTYEAR` and `DATESYTD` to return accurate numbers?

Domain: Implement and manage semantic models

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column
- C. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- D. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension

### 70. Which two model-hygiene steps prepare `BondPortfolioModel` for self-service `Analyze in Excel` users so PivotTables never offer `Sum of BondSurrogateKey`, fiscal months sort Apr -> Mar chronologically, and hidden `LocalDateTable_*` bloat is eliminated? Select two.

Domain: Implement and manage semantic models

- A. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- B. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- C. Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column
- D. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- E. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear

### 71. Syndicated commercial loans have multiple `CoLenderBanks`, and each `CoLenderBank` participates in hundreds of `Loans`. How should you model `DimLoan`, `BridgeLoanSyndicate`, and `DimBank` without introducing permanent model-wide bidirectional filter ambiguity?

Domain: Implement and manage semantic models

- A. Introduce a deduplicated Bridge table between the two dimensions and scope bidirectional propagation strictly inside specific measures using CROSSFILTER(..., BOTH)
- B. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- C. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- D. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()

### 72. On a `DirectQuery` intraday risk model where Warehouse foreign-key checks guarantee zero orphan `CounterpartyKey` values in `FactIntradayExposure`, which relationship property upgrades generated SQL from `LEFT OUTER JOIN` to `INNER JOIN`?

Domain: Implement and manage semantic models

- A. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- B. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other

### 73. Proposed solution: A risk analyst writes `Liquidity Tier = IF([LCR Ratio] < 1.0, "Breach", IF([LCR Ratio] < 1.15, "Watch", "Healthy"))`, causing `[LCR Ratio]` (a heavy multi-table measure) to execute twice on every healthy branch. How do you halve Storage Engine work in one line?

Domain: Implement and manage semantic models

- A. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- B. Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches
- C. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table
- D. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows

### 74. Complete `High Yield Exposure = CALCULATE([Total Exposure], ____('DimRating'[RatingBucket] = "High Yield"))` so a matrix sliced by `RatingBucket` shows values only on the `"High Yield"` row and `BLANK()` on `"Investment Grade"` instead of repeating `"High Yield"` everywhere?

Domain: Implement and manage semantic models

- A. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- B. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table
- C. Pass simple column predicates wrapped in KEEPFILTERS(DimProduct[Color] = "Red") to CALCULATE instead of FILTER(ALL(FactSales), ...)
- D. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically

### 75. In a capital-markets matrix (`Region -> Desk -> Trader`), you need (1) `[Prior Custom Settlement Cycle PnL]` stepping back 1 period along `'Calendar'[FiscalPeriodSort]` (`____`), and (2) `[Trader Bonus %]` suppressed to `BLANK()` on `Desk` and `Region` subtotal rows (`____`). Which two DAX expressions apply? Select two.

Domain: Implement and manage semantic models

- A. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- B. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC)))
- E. IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK())

### 76. You build a `Currency Basis` Calculation Group (`Local`, `USD Spot`, `USD Constant FX`) applied across 50 P&L measures. Which DAX function (`____`) inside each calculation item stands in for whichever base P&L measure is active in the visual?

Domain: Implement and manage semantic models

- A. [ManagerEmail] = USERPRINCIPALNAME()
- B. EVALUATE INFO.VIEW.MEASURES()
- C. NAMEOF('DimTrade'[CurrencyPair])
- D. CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))

### 77. Why does setting a measure's `Format String Expression` to `____` (`IF(..., "0.0%", SELECTEDMEASUREFORMATSTRING())`) beat returning `FORMAT([Value], "0.0%")` inside the measure's main DAX expression?

Domain: Implement and manage semantic models

- A. IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())
- B. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- C. CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))
- D. NAMEOF('DimTrade'[CurrencyPair])

### 78. You try to connect Tabular Editor and SSMS over the XMLA endpoint to a growing 9.5 GB wealth model and plan for it to reach 22 GB next quarter on an F64 capacity. Turning on which toggle in semantic model settings prepares the model for >10 GB growth and faster XMLA writes?

Domain: Implement and manage semantic models

- A. Mark the item as Promoted in item settings
- B. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- C. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode

### 79. Private-banking architects want one semantic model joining `FactPortfolios` from `WealthLakehouse` (Direct Lake), `DimClient` from `CRMWarehouse` (Direct Lake), and `Import` macroeconomic forecast curves from an external HTTPS API via regular `1:*` relationships. Which storage architecture supports all three?

Domain: Implement and manage semantic models

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- D. Build a Direct Lake on OneLake composite semantic model combining Direct Lake fact tables from OneLake with Import dimension/target tables using regular relationships

### 80. Which two composite patterns let (1) an intraday trade-surveillance model answer `Desk x Hour` totals from VertiPaq RAM while routing rare `OrderId` drills to a 10-billion-row `DirectQuery` Warehouse, and (2) an equity analyst append a local CSV watch-list onto the Certified corporate `EquitiesCore` semantic model? Select two.

Domain: Implement and manage semantic models

- A. Create a local composite model using DirectQuery for Power BI semantic models and Analysis Services to combine a certified core semantic model with a departmental Excel/SQL table
- B. Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table
- C. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- E. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches

### 81. A CFO dashboard page containing 42 single-value cards and 9 slicers takes 10.5 seconds to load, though DAX Studio shows every underlying measure executes in <30 ms. Which Power BI Desktop tool proves visual-container queuing (`Other`) is the culprit?

Domain: Implement and manage semantic models

- A. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- B. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- C. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- D. Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View

### 82. On a live `DirectQuery` fraud-investigation page, analysts select 6 merchant countries in a filter pane; each selection immediately fires expensive Warehouse queries before the 6th country is checked. Which report setting batches slicer selections?

Domain: Implement and manage semantic models

- A. Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails
- B. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- C. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- D. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages

### 83. Which four-step workflow systematically resolves a 16-second `[Risk-Weighted Assets]` DAX measure on a Direct Lake model?

Domain: Implement and manage semantic models

- A. Test queries only against warm VertiPaq cache without Clear Cache → Add high-cardinality GUID calculated columns to FactSales → Force DirectQueryOnly behavior → Add 45 single-value card visuals to one page
- B. Hide slow measures in Display Folders → Turn on Auto date/time → Split one Gold dimension into 6 normalized snowflake tables → Remove calendar surrogate keys
- C. Capture visual timings in Performance Analyzer → Profile captured DAX in DAX Studio with Server Timings and Query Plan → Refactor FILTER(Fact,...) into VAR-cached SE column predicates and run V-Order OPTIMIZE → Re-test with Clear Cache
- D. Immediately upgrade from F64 to F512 without profiling → Enable bidirectional cross-filtering on all relationships → Convert numeric measures to FORMAT() strings → Disable V-Order on Gold tables

### 84. Streaming Spark micro-batches wrote 62,000 tiny Parquet files into `gold.fact_orders`, pushing rowgroup counts above capacity guardrails. Complete the Spark SQL maintenance command `____;` that compacts small files and applies VertiPaq-aligned columnar sorting?

Domain: Implement and manage semantic models

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. CAST(RawReading AS FLOAT)
- C. OPTIMIZE gold.fact_orders VORDER
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging

### 85. Which three practices keep a Direct Lake on SQL financial semantic model deterministic after nightly batch completion, within rowgroup guardrails, and immune to silent slow DirectQuery fallbacks? Select three.

Domain: Implement and manage semantic models

- A. Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes
- B. Expect Direct Lake on OneLake to automatically fall back to DirectQuery against the SQL analytics endpoint when capacity memory guardrails are exceeded
- C. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- D. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- E. Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails
- F. Set DirectLakeBehavior = DirectLakeOnly on a Direct Lake on SQL semantic model so queries fail fast instead of silently falling back to slow DirectQuery

### 86. Proposed solution: You build a new Direct Lake semantic model from a Lakehouse SQL analytics endpoint (`Direct Lake on SQL`), and later try to add a second Delta table from `RiskWarehouse` plus an `Import` holiday table. Why is that blocked, and which Direct Lake mode supports it?

Domain: Implement and manage semantic models

- A. Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop)
- B. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- C. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- D. Configure DirectQuery storage mode

### 87. In which four-step order do you migrate `Direct Lake on SQL` model `FXAnalytics` (backed purely by Delta tables) to `Direct Lake on OneLake` using Power BI Desktop without breaking bound thin reports?

Domain: Implement and manage semantic models

- A. Delete the semantic model in Production breaking report GUID bindings → Recreate measures manually from screenshots → Share Lakehouse Admin rights with all report viewers → Disable V-Order
- B. Download the Direct Lake model as an offline Import .pbix → Convert all tables to Dual storage mode → Replace AzureStorage.DataLake with OleDb.DataSource → Re-upload to My Workspace
- C. Live edit the model in Power BI Desktop and save a Version history point → Script the semantic model in TMDL view → Replace Sql.Database(...) with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...") → Apply TMDL and run framing refresh
- D. Keep non-materialized SQL analytics endpoint views as the only sources → Switch TMDL expression to AzureStorage.DataLake without materializing Delta tables → Enable DirectQuery fallback on Direct Lake on OneLake → Bind an On-premises gateway

### 88. Compliance requires retaining 7 years of imported `FactWireAudit` history while refreshing only the last 7 days nightly. Which four-step Incremental Refresh workflow ensures foldable queries and zero boundary-date double-counting?

Domain: Implement and manage semantic models

- A. Filter OrderDate > RangeEnd → Configure Detect data changes on the exact same OrderDate partition column → Disable query folding → Run XMLA clearValues without processing
- B. Create case-sensitive DateTime parameters RangeStart and RangeEnd → Apply foldable half-open filter (>= RangeStart and < RangeEnd) → Configure table Incremental refresh policy → Publish to workspace and run initial refresh to generate partitions
- C. Publish an unfiltered 2-billion-row Import PBIX locally first → Define RangeStart in DAX calculated tables afterward → Set storage mode to Direct Lake on OneLake → Enable VNet gateway on Direct Lake
- D. Create Text parameters named StartDate and EndDate → Add a custom M step breaking query folding before filtering → Use >= and <= inclusive bounds on both sides → Refresh only in Power BI Desktop

---

## Case study — ClearLedger Bank

ClearLedger Bank consolidates operational accounts from Azure SQL Database inside a private Azure VNet and cloud risk scores from Snowflake into Microsoft Fabric with minimal ETL maintenance. Analysts need near-real-time OneLake Delta availability for operational accounts and zero-copy T-SQL queries joining the Warehouse risk mart with a sibling Lakehouse in the same workspace.

The next 3 questions refer to **ClearLedger Bank**. Read the scenario brief once, then answer each item independently.

### 89. Which Fabric capability continuously replicates operational account tables from Azure SQL Database and risk tables from Snowflake into OneLake Delta Parquet format with zero ETL code?

Domain: Prepare data

- A. Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog
- B. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- C. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 90. How should Fabric connect securely to the private-endpoint Azure SQL Database inside ClearLedger's Azure VNet without deploying or patching IaaS gateway VMs?

Domain: Prepare data

- A. Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet
- B. Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication
- C. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- D. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes

### 91. Complete `SELECT r.AccountId, l.KycTier FROM dbo.RiskScores r JOIN ____ l ON r.AccountId = l.AccountId;` inside `RiskWarehouse` to join `KycLakehouse` in the same workspace with zero data movement?

Domain: Prepare data

- A. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching
- B. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- C. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- D. Query across a Warehouse and a Lakehouse SQL analytics endpoint in the same workspace using three-part T-SQL naming (SalesLakehouse.dbo.RawOrders)

---

## Case study — FraudShield Pay

FraudShield Pay streams card authorization events into an Eventhouse and curates settled transactions into a 2-billion-row Gold Lakehouse table. Fraud analysts query p99 latency and gap-filled 1-minute time series in KQL, while the Direct Lake semantic model consumes 72% of capacity RAM due to an unused `TransactionGUID` column and a millisecond `EventTimestamp` column.

The next 3 questions refer to **FraudShield Pay**. Read the scenario brief once, then answer each item independently.

### 92. Complete `AuthEvents ____` in the Eventhouse KQL queryset to produce gap-filled 1-minute authorization count arrays (`0` when quiet) per merchant region over the last 6 hours?

Domain: Prepare data

- A. | make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion
- B. | summarize arg_max(IngestionTime, *) by SpecimenId
- C. | mv-expand PhaseReading = parse_json(Payload).PhaseReadings
- D. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)

### 93. Fraud SREs run `AuthEvents | where EventTime > ago(1h) ____` to monitor 99th-percentile authorization latency in 5-minute buckets. Which KQL clause fills the blank?

Domain: Prepare data

- A. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- B. | make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion
- C. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- D. | summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)

### 94. Which optimization slashes the 72% capacity RAM footprint caused by unused `TransactionGUID` and millisecond `EventTimestamp` columns on the 2-billion-row Direct Lake model?

Domain: Implement and manage semantic models

- A. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time
- D. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension

---

## Case study — Meridian Wealth

Meridian Wealth promotes analytics across Development, Test, and Production workspaces on an F128 capacity. A 28 GB Import/Direct Lake enterprise semantic model exceeds standard size limits, emergency DAX measure hotfixes must deploy from Dev to Prod without wiping 7 years of processed partitions, and nightly ETL only needs to reload a single modified monthly partition.

The next 3 questions refer to **Meridian Wealth**. Read the scenario brief once, then answer each item independently.

### 95. Which semantic model configuration is mandatory so the 28 GB enterprise wealth model can load and refresh on the F128 capacity above the standard compressed size cap?

Domain: Implement and manage semantic models

- A. Configure DirectQuery storage mode
- B. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- C. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 96. In which four-step order should engineers push emergency DAX measure fixes from `Wealth-Dev` to `Wealth-Prod` without wiping 7 years of processed historical partitions?

Domain: Maintain a data analytics solution

- A. Leave XMLA Endpoint = Read Only → Execute T-SQL DELETE across Warehouse schemas → Grant all report viewers Capacity Admin rights → Skip downstream impact analysis
- B. Verify XMLA Endpoint = Read Write on target capacity → Connect ALM Toolkit to Dev source and Prod XMLA target → Compare schemas while hiding unchanged partitions and keeping Prod data sources → Validate and deploy metadata-only TMSL changes
- C. Set XMLA Endpoint = Off → Overwrite Production with an empty unpartitioned .pbix file → Purge all 5 years of historical incremental partitions → Re-import 3 billion rows during peak business hours
- D. Open Production in DAX Studio → Edit measures manually in Production without committing to Git → Copy cache.abf into GitHub → Disable sensitivity labels

### 97. Nightly wealth ETL modifies only partition `2026M10` of `FactPositions` and sends TMSL payload `____` over `powerbi://api.powerbi.com/v1.0/myorg/Wealth-Prod`. Which two elements are required? Select two.

Domain: Maintain a data analytics solution

- A. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- B. Assign the Workspace Viewer role
- C. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- D. {"refresh": {"type": "dataOnly", "objects": [{"database": "WealthModel", "table": "FactPositions", "partition": "2026M10"}]}}
- E. Enable XMLA Endpoint = Read Write in Fabric Capacity workload settings and connect to powerbi://api.powerbi.com/v1.0/myorg/<WorkspaceName>

---

## Case study — SwiftSettle FX

SwiftSettle FX tracks foreign-exchange trades carrying TradeDate, ValueDate, and SettlementDate keys against one Calendar table. Multi-currency revenue must multiply each trade's notional amount by its daily spot rate row-by-row without adding calculated columns, and portfolio managers want one slicer to switch matrix rows dynamically between Desk, CurrencyPair, and Counterparty.

The next 3 questions refer to **SwiftSettle FX**. Read the scenario brief once, then answer each item independently.

### 98. With `Calendar[DateKey]` actively joined to `FactTrades[TradeDateKey]` and inactively joined to `SettlementDateKey`, complete `Settled FX Volume = ____` without duplicating `Calendar`?

Domain: Implement and manage semantic models

- A. Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column
- B. CALCULATE([Encounter Count], CROSSFILTER('FactEncounter'[EncounterKey], 'BridgeEncounterDiag'[EncounterKey], BOTH))
- C. CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other

### 99. How should you compute USD revenue (`____(FactFXTrades, FactFXTrades[LocalNotional] * FactFXTrades[DailySpotRate])`) accurately across currencies without adding calculated columns?

Domain: Implement and manage semantic models

- A. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- B. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table
- C. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)
- D. Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches

### 100. Which feature lets portfolio managers switch matrix rows dynamically between `Desk`, `CurrencyPair` (`NAMEOF('DimTrade'[CurrencyPair])`), and `Counterparty` from a single slicer?

Domain: Implement and manage semantic models

- A. Create a Calculation Group with Calculation Items referencing SELECTEDMEASURE() and explicit Precedence ordering (automatically setting DiscourageImplicitMeasures = true)
- B. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically

---

## Answer key and explanations

### Question 1 — B

Answer: Assign the Workspace Contributor role. `Workspace Contributor` allows creating, editing, and scheduling items while blocking permission changes, external sharing, and app publishing. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: `Workspace Contributor` allows creating, editing, and scheduling items while blocking permission changes, external sharing, and app publishing.
- **B:** Correct. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. In this scenario: `Workspace Contributor` allows creating, editing, and scheduling items while blocking permission changes, external sharing, and app publishing.
- **C:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: `Workspace Contributor` allows creating, editing, and scheduling items while blocking permission changes, external sharing, and app publishing.
- **D:** Incorrect for this requirement. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. Why the keyed choice wins: `Workspace Contributor` allows creating, editing, and scheduling items while blocking permission changes, external sharing, and app publishing.

### Question 2 — A

Answer: Assign the Workspace Viewer role. Workspace `Admin`, `Member`, and `Contributor` roles bypass DAX RLS and OneLake security; branch managers must hold `Workspace Viewer` (or consume via an App with Read access). Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Correct. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. In this scenario: Workspace `Admin`, `Member`, and `Contributor` roles bypass DAX RLS and OneLake security; branch managers must hold `Workspace Viewer` (or consume via an App with Read access).
- **B:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: Workspace `Admin`, `Member`, and `Contributor` roles bypass DAX RLS and OneLake security; branch managers must hold `Workspace Viewer` (or consume via an App with Read access).
- **C:** Incorrect for this requirement. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. Why the keyed choice wins: Workspace `Admin`, `Member`, and `Contributor` roles bypass DAX RLS and OneLake security; branch managers must hold `Workspace Viewer` (or consume via an App with Read access).
- **D:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: Workspace `Admin`, `Member`, and `Contributor` roles bypass DAX RLS and OneLake security; branch managers must hold `Workspace Viewer` (or consume via an App with Read access).

### Question 3 — B, C

Answers: Assign the Workspace Member role; Assign permissions to Microsoft Entra security groups rather than individual users. Granting `Workspace Member` to a Microsoft Entra security group provides sharing, App publishing, and OneLake-role management without workspace deletion privileges. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: Granting `Workspace Member` to a Microsoft Entra security group provides sharing, App publishing, and OneLake-role management without workspace deletion privileges.
- **B:** Correct. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. In this scenario: Granting `Workspace Member` to a Microsoft Entra security group provides sharing, App publishing, and OneLake-role management without workspace deletion privileges.
- **C:** Correct. Granting workspace, item, deployment-pipeline, and RLS role memberships to Microsoft Entra security groups centralizes joiner/mover/leaver governance and scales across workspaces without per-user ACL drift. In this scenario: Granting `Workspace Member` to a Microsoft Entra security group provides sharing, App publishing, and OneLake-role management without workspace deletion privileges.
- **D:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: Granting `Workspace Member` to a Microsoft Entra security group provides sharing, App publishing, and OneLake-role management without workspace deletion privileges.
- **E:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: Granting `Workspace Member` to a Microsoft Entra security group provides sharing, App publishing, and OneLake-role management without workspace deletion privileges.

### Question 4 — B

Answer: Bind the Direct Lake semantic model to a cloud connection with a fixed identity and disable SSO. Binding the Direct Lake model to a Shareable cloud connection using a fixed identity (Service Principal or Workspace Identity) with SSO disabled lets the model read OneLake while enforcing DAX RLS on report viewers. Configuring a fixed-identity cloud connection (Service Principal or Workspace Identity) with SSO disabled lets report consumers query the Direct Lake model enforced by semantic-model RLS without granting them any direct Lakehouse or SQL endpoint permissions. Local study-map skill 1.2 (Implement Item-Level Access Controls (Read, ReadData, ReadAll, Build, SSO vs Fixed Identity)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Share items in Microsoft Fabric & Semantic model Build permission (https://learn.microsoft.com/en-us/fabric/fundamentals/share-items).

- **A:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: Binding the Direct Lake model to a Shareable cloud connection using a fixed identity (Service Principal or Workspace Identity) with SSO disabled lets the model read OneLake while enforcing DAX RLS on report viewers.
- **B:** Correct. Configuring a fixed-identity cloud connection (Service Principal or Workspace Identity) with SSO disabled lets report consumers query the Direct Lake model enforced by semantic-model RLS without granting them any direct Lakehouse or SQL endpoint permissions. In this scenario: Binding the Direct Lake model to a Shareable cloud connection using a fixed identity (Service Principal or Workspace Identity) with SSO disabled lets the model read OneLake while enforcing DAX RLS on report viewers.
- **C:** Incorrect for this requirement. ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled. Why the keyed choice wins: Binding the Direct Lake model to a Shareable cloud connection using a fixed identity (Service Principal or Workspace Identity) with SSO disabled lets the model read OneLake while enforcing DAX RLS on report viewers.
- **D:** Incorrect for this requirement. With SSO enabled on a Direct Lake model, Fabric evaluates data permissions at the underlying SQL analytics endpoint or OneLake security layer using each viewing report consumer's own Microsoft Entra identity. Why the keyed choice wins: Binding the Direct Lake model to a Shareable cloud connection using a fixed identity (Service Principal or Workspace Identity) with SSO disabled lets the model read OneLake while enforcing DAX RLS on report viewers.

### Question 5 — D

Answer: Grant Build permission on the shared semantic model. `Build` permission on the semantic model enables `Analyze in Excel`, live report creation, and XMLA read queries without granting workspace edit access. Build permission on a semantic model allows analysts to create new Power BI reports, use Analyze in Excel, and issue XMLA/DAX queries against the model without granting workspace Contributor rights or underlying Lakehouse access. Local study-map skill 1.2 (Implement Item-Level Access Controls (Read, ReadData, ReadAll, Build, SSO vs Fixed Identity)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Share items in Microsoft Fabric & Semantic model Build permission (https://learn.microsoft.com/en-us/fabric/fundamentals/share-items).

- **A:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: `Build` permission on the semantic model enables `Analyze in Excel`, live report creation, and XMLA read queries without granting workspace edit access.
- **B:** Incorrect for this requirement. Item-level Read metadata permission lets a user connect to a Lakehouse or Warehouse item container without granting broad OneLake file access; combine with SELECT or OneLake security roles for granular least-privilege access. Why the keyed choice wins: `Build` permission on the semantic model enables `Analyze in Excel`, live report creation, and XMLA read queries without granting workspace edit access.
- **C:** Incorrect for this requirement. ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled. Why the keyed choice wins: `Build` permission on the semantic model enables `Analyze in Excel`, live report creation, and XMLA read queries without granting workspace edit access.
- **D:** Correct. Build permission on a semantic model allows analysts to create new Power BI reports, use Analyze in Excel, and issue XMLA/DAX queries against the model without granting workspace Contributor rights or underlying Lakehouse access. In this scenario: `Build` permission on the semantic model enables `Analyze in Excel`, live report creation, and XMLA read queries without granting workspace edit access.

### Question 6 — B

Answer: Define both the RLS filter and CLS column allow-list inside a single OneLake security Grant role with Read permission. Assigning separate RLS and CLS OneLake security roles on the same table causes query errors; consolidating both the RLS predicate and CLS column list into one `Read` Grant role resolves the conflict. OneLake security supports Grant roles only (Read permission required for RLS/CLS) and requires combining RLS and CLS on the same table within a single role — separate RLS and CLS roles on the same table return query errors. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. OneLake security roles granting ReadWrite permission cannot contain RLS or CLS constraints; fine-grained row and column rules are supported only on Read roles. Why the keyed choice wins: Assigning separate RLS and CLS OneLake security roles on the same table causes query errors; consolidating both the RLS predicate and CLS column list into one `Read` Grant role resolves the conflict.
- **B:** Correct. OneLake security supports Grant roles only (Read permission required for RLS/CLS) and requires combining RLS and CLS on the same table within a single role — separate RLS and CLS roles on the same table return query errors. In this scenario: Assigning separate RLS and CLS OneLake security roles on the same table causes query errors; consolidating both the RLS predicate and CLS column list into one `Read` Grant role resolves the conflict.
- **C:** Incorrect for this requirement. OneLake security supports Grant roles only — there is no Deny role type, and OneLake security never restricts Workspace Admins, Members, or Contributors. Why the keyed choice wins: Assigning separate RLS and CLS OneLake security roles on the same table causes query errors; consolidating both the RLS predicate and CLS column list into one `Read` Grant role resolves the conflict.
- **D:** Incorrect for this requirement. OneLake security does not support combining an RLS role and a CLS role across separate roles on the same table; members assigned to that combination receive query errors. Why the keyed choice wins: Assigning separate RLS and CLS OneLake security roles on the same table causes query errors; consolidating both the RLS predicate and CLS column list into one `Read` Grant role resolves the conflict.

### Question 7 — C

Answer: Grant T-SQL column-level SELECT on only the non-sensitive columns (GRANT SELECT ON dbo.Customer(CustomerID, Region) TO ...). T-SQL column-level security (`GRANT SELECT ON dbo.Loans(LoanId, OriginationDate, PrincipalAmt) TO ...`) restricts SQL callers strictly to permitted columns without creating duplicate tables. In Fabric Warehouse and SQL analytics endpoints, column-level security restricts users to explicitly permitted columns via column-scoped GRANT SELECT without creating duplicate views or physical tables. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: T-SQL column-level security (`GRANT SELECT ON dbo.Loans(LoanId, OriginationDate, PrincipalAmt) TO ...`) restricts SQL callers strictly to permitted columns without creating duplicate tables.
- **B:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: T-SQL column-level security (`GRANT SELECT ON dbo.Loans(LoanId, OriginationDate, PrincipalAmt) TO ...`) restricts SQL callers strictly to permitted columns without creating duplicate tables.
- **C:** Correct. In Fabric Warehouse and SQL analytics endpoints, column-level security restricts users to explicitly permitted columns via column-scoped GRANT SELECT without creating duplicate views or physical tables. In this scenario: T-SQL column-level security (`GRANT SELECT ON dbo.Loans(LoanId, OriginationDate, PrincipalAmt) TO ...`) restricts SQL callers strictly to permitted columns without creating duplicate tables.
- **D:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: T-SQL column-level security (`GRANT SELECT ON dbo.Loans(LoanId, OriginationDate, PrincipalAmt) TO ...`) restricts SQL callers strictly to permitted columns without creating duplicate tables.

### Question 8 — A

Answer: Enable OneLake security and define Read Grant roles → Assign consumers Workspace Viewer and OneLake security roles → Set SQL analytics endpoint to User's identity mode → Expose downstream shortcuts in User's identity mode. Defining Read Grant roles on the source Lakehouse, assigning consumers Viewer + security roles, setting SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access. Correct order: enable OneLake security with Grant roles first, assign consumers to Viewer + security roles (never Contributor), set SQL analytics endpoints to User's identity mode, and expose shortcuts downstream. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Correct. Correct order: enable OneLake security with Grant roles first, assign consumers to Viewer + security roles (never Contributor), set SQL analytics endpoints to User's identity mode, and expose shortcuts downstream. In this scenario: Defining Read Grant roles on the source Lakehouse, assigning consumers Viewer + security roles, setting SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access.
- **B:** Incorrect for this requirement. Incorrect: mixing pre-existing SQL granular access with Delegated mode forces 100% DirectQuery fallback instead of clean OneLake security evaluation. Why the keyed choice wins: Defining Read Grant roles on the source Lakehouse, assigning consumers Viewer + security roles, setting SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access.
- **C:** Incorrect for this requirement. Incorrect: Contributors bypass OneLake security completely, OneLake security has no Deny role type, and Owner fixed identity bypasses per-user role evaluation on SQL queries. Why the keyed choice wins: Defining Read Grant roles on the source Lakehouse, assigning consumers Viewer + security roles, setting SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access.
- **D:** Incorrect for this requirement. Incorrect: Members bypass OneLake security, ReadWrite roles cannot contain RLS/CLS rules, and OneLake shortcuts do not use On-premises gateways. Why the keyed choice wins: Defining Read Grant roles on the source Lakehouse, assigning consumers Viewer + security roles, setting SQL endpoints to User's identity mode, and keeping downstream shortcuts in User's identity mode enforces uniform access.

### Question 9 — A, B

Answers: Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL; Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN. Configuring Object-Level Security (`None`) via Tabular Editor/TMDL hides `[AdvisoryFee_USD]` metadata completely, and validating with `Test as role` + `analyst1@clearledger.com` confirms effective enforcement. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Correct. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. In this scenario: Configuring Object-Level Security (`None`) via Tabular Editor/TMDL hides `[AdvisoryFee_USD]` metadata completely, and validating with `Test as role` + `analyst1@clearledger.com` confirms effective enforcement.
- **B:** Correct. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). In this scenario: Configuring Object-Level Security (`None`) via Tabular Editor/TMDL hides `[AdvisoryFee_USD]` metadata completely, and validating with `Test as role` + `analyst1@clearledger.com` confirms effective enforcement.
- **C:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Configuring Object-Level Security (`None`) via Tabular Editor/TMDL hides `[AdvisoryFee_USD]` metadata completely, and validating with `Test as role` + `analyst1@clearledger.com` confirms effective enforcement.
- **D:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: Configuring Object-Level Security (`None`) via Tabular Editor/TMDL hides `[AdvisoryFee_USD]` metadata completely, and validating with `Test as role` + `analyst1@clearledger.com` confirms effective enforcement.
- **E:** Incorrect for this requirement. In Power BI Desktop USERNAME() returns DOMAIN\user whereas in the Fabric service it returns the UPN; USERPRINCIPALNAME() consistently returns user@domain.com across cloud evaluations. Why the keyed choice wins: Configuring Object-Level Security (`None`) via Tabular Editor/TMDL hides `[AdvisoryFee_USD]` metadata completely, and validating with `Test as role` + `analyst1@clearledger.com` confirms effective enforcement.

### Question 10 — C

Answer: Apply a Microsoft Purview sensitivity label with downstream inheritance on the source Lakehouse or Warehouse. Downstream sensitivity-label inheritance automatically applies the `Strictly Confidential — MNPI` label to new semantic models and reports built from `EquitiesWarehouse`. Sensitivity labels applied to Fabric Lakehouses, Warehouses, and Semantic Models automatically propagate downstream to newly connected semantic models, reports, and exported Excel/PDF/PPTX files when inheritance is enabled. Local study-map skill 1.4 (Apply Microsoft Purview Sensitivity Labels, Inheritance, Default/Mandatory Policies, and Export Encryption), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Information protection & sensitivity labels in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-overview).

- **A:** Incorrect for this requirement. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Why the keyed choice wins: Downstream sensitivity-label inheritance automatically applies the `Strictly Confidential — MNPI` label to new semantic models and reports built from `EquitiesWarehouse`.
- **B:** Incorrect for this requirement. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Why the keyed choice wins: Downstream sensitivity-label inheritance automatically applies the `Strictly Confidential — MNPI` label to new semantic models and reports built from `EquitiesWarehouse`.
- **C:** Correct. Sensitivity labels applied to Fabric Lakehouses, Warehouses, and Semantic Models automatically propagate downstream to newly connected semantic models, reports, and exported Excel/PDF/PPTX files when inheritance is enabled. In this scenario: Downstream sensitivity-label inheritance automatically applies the `Strictly Confidential — MNPI` label to new semantic models and reports built from `EquitiesWarehouse`.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Downstream sensitivity-label inheritance automatically applies the `Strictly Confidential — MNPI` label to new semantic models and reports built from `EquitiesWarehouse`.

### Question 11 — A

Answer: Use a Purview sensitivity label configured with file encryption so exported .pbix, Excel, PDF, and PowerPoint files stay protected outside Fabric. Enabling Purview Information Protection file encryption on the sensitivity label embeds RMS access controls directly into exported `.xlsx`, `.pdf`, `.pptx`, and `.pbix` files. While sensitivity labels in Fabric classify items in the workspace without encrypting OneLake Delta storage itself, encryption-enabled labels enforce rights management automatically when users export data to Excel, PDF, PowerPoint, or .pbix. Local study-map skill 1.4 (Apply Microsoft Purview Sensitivity Labels, Inheritance, Default/Mandatory Policies, and Export Encryption), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Information protection & sensitivity labels in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-overview).

- **A:** Correct. While sensitivity labels in Fabric classify items in the workspace without encrypting OneLake Delta storage itself, encryption-enabled labels enforce rights management automatically when users export data to Excel, PDF, PowerPoint, or .pbix. In this scenario: Enabling Purview Information Protection file encryption on the sensitivity label embeds RMS access controls directly into exported `.xlsx`, `.pdf`, `.pptx`, and `.pbix` files.
- **B:** Incorrect for this requirement. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Why the keyed choice wins: Enabling Purview Information Protection file encryption on the sensitivity label embeds RMS access controls directly into exported `.xlsx`, `.pdf`, `.pptx`, and `.pbix` files.
- **C:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Enabling Purview Information Protection file encryption on the sensitivity label embeds RMS access controls directly into exported `.xlsx`, `.pdf`, `.pptx`, and `.pbix` files.
- **D:** Incorrect for this requirement. Dynamic Data Masking obfuscates sensitive strings/emails/numbers in query results for users lacking UNMASK permission while keeping the column present so SELECT * queries do not fail. Why the keyed choice wins: Enabling Purview Information Protection file encryption on the sensitivity label embeds RMS access controls directly into exported `.xlsx`, `.pdf`, `.pptx`, and `.pbix` files.

### Question 12 — B

Answer: Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal. `Certified` endorsement can only be applied by admin-designated governance reviewers after quality and security validation. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Local study-map skill 1.5 (Endorse Items Using Promoted, Certified, and Master Data Governance Badges), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Endorsement (Promoted, Certified, Master data) in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview).

- **A:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: `Certified` endorsement can only be applied by admin-designated governance reviewers after quality and security validation.
- **B:** Correct. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. In this scenario: `Certified` endorsement can only be applied by admin-designated governance reviewers after quality and security validation.
- **C:** Incorrect for this requirement. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. Why the keyed choice wins: `Certified` endorsement can only be applied by admin-designated governance reviewers after quality and security validation.
- **D:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: `Certified` endorsement can only be applied by admin-designated governance reviewers after quality and security validation.

### Question 13 — A

Answer: Configure Certified endorsement with the Master data label on authoritative core tables or semantic models. Applying `Certified` endorsement with `Master data` enabled badges `GoldCounterpartyLakehouse` as the authoritative master reference source. Fabric admins can enable Master data endorsement for authoritative single-source-of-truth silver/gold data assets so analysts distinguish core reference items in the OneLake catalog. Local study-map skill 1.5 (Endorse Items Using Promoted, Certified, and Master Data Governance Badges), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Endorsement (Promoted, Certified, Master data) in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview).

- **A:** Correct. Fabric admins can enable Master data endorsement for authoritative single-source-of-truth silver/gold data assets so analysts distinguish core reference items in the OneLake catalog. In this scenario: Applying `Certified` endorsement with `Master data` enabled badges `GoldCounterpartyLakehouse` as the authoritative master reference source.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Applying `Certified` endorsement with `Master data` enabled badges `GoldCounterpartyLakehouse` as the authoritative master reference source.
- **C:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Applying `Certified` endorsement with `Master data` enabled badges `GoldCounterpartyLakehouse` as the authoritative master reference source.
- **D:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Applying `Certified` endorsement with `Master data` enabled badges `GoldCounterpartyLakehouse` as the authoritative master reference source.

### Question 14 — B

Answer: Use Undo in the Fabric Workspace Source control pane to discard uncommitted workspace edits back to the last synced commit. Selecting `Undo` on the uncommitted items in the Workspace Source control pane discards local workspace changes and restores the connected branch's last synced commit. Undo reverts uncommitted workspace item modifications to match the connected Git branch HEAD without rewriting shared remote commit history. Local study-map skill 1.6 (Configure Workspace Version Control with Azure DevOps or GitHub (Branch Out, Commit, Update, Undo)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to Git integration in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration).

- **A:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Selecting `Undo` on the uncommitted items in the Workspace Source control pane discards local workspace changes and restores the connected branch's last synced commit.
- **B:** Correct. Undo reverts uncommitted workspace item modifications to match the connected Git branch HEAD without rewriting shared remote commit history. In this scenario: Selecting `Undo` on the uncommitted items in the Workspace Source control pane discards local workspace changes and restores the connected branch's last synced commit.
- **C:** Incorrect for this requirement. Fabric Git sync is explicit rather than automatic on remote push: developers Commit workspace edits to their branch, complete a PR in Azure DevOps or GitHub, and run Update from Git in the downstream workspace. Why the keyed choice wins: Selecting `Undo` on the uncommitted items in the Workspace Source control pane discards local workspace changes and restores the connected branch's last synced commit.
- **D:** Incorrect for this requirement. In Fabric Git integration, workspaces map 1-to-1 to branches; branching out into a dedicated developer workspace isolates in-progress notebook, pipeline, and semantic model edits before merging via pull request. Why the keyed choice wins: Selecting `Undo` on the uncommitted items in the Workspace Source control pane discards local workspace changes and restores the connected branch's last synced commit.

### Question 15 — B

Answer: Connect shared Dev workspace to main → Branch out to an isolated developer workspace and commit .pbip/Notebook edits → Merge pull request into main in Git → Run Update all in Dev and promote via Deployment Pipeline. Connecting `Dev` to `main`, branching out to an isolated workspace, merging the PR into `main`, running `Update all` in `Dev`, and promoting through the Deployment Pipeline prevents unreviewed drift. Correct order: link Dev to main, branch out to an isolated workspace for feature work, validate and merge via Git PR into main, run Update all in Dev, and promote via Deployment Pipeline with stage rules. Local study-map skill 1.6 (Configure Workspace Version Control with Azure DevOps or GitHub (Branch Out, Commit, Update, Undo)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to Git integration in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration).

- **A:** Incorrect for this requirement. Incorrect: editing Production directly on feature branches and committing cache.abf violates ALM isolation, leaks cached data, and bypasses Test validation. Why the keyed choice wins: Connecting `Dev` to `main`, branching out to an isolated workspace, merging the PR into `main`, running `Update all` in `Dev`, and promoting through the Deployment Pipeline prevents unreviewed drift.
- **B:** Correct. Correct order: link Dev to main, branch out to an isolated workspace for feature work, validate and merge via Git PR into main, run Update all in Dev, and promote via Deployment Pipeline with stage rules. In this scenario: Connecting `Dev` to `main`, branching out to an isolated workspace, merging the PR into `main`, running `Update all` in `Dev`, and promoting through the Deployment Pipeline prevents unreviewed drift.
- **C:** Incorrect for this requirement. Incorrect: My Workspace does not support full team Git ALM, Undo discards local changes rather than committing, and deleting .platform breaks item lineage. Why the keyed choice wins: Connecting `Dev` to `main`, branching out to an isolated workspace, merging the PR into `main`, running `Update all` in `Dev`, and promoting through the Deployment Pipeline prevents unreviewed drift.
- **D:** Incorrect for this requirement. Incorrect: Fabric workspaces do not auto-pull remote PR merges — skipping Update from Git promotes stale pre-PR workspace state to Test. Why the keyed choice wins: Connecting `Dev` to `main`, branching out to an isolated workspace, merging the PR into `main`, running `Update all` in `Dev`, and promoting through the Deployment Pipeline prevents unreviewed drift.

### Question 16 — C

Answer: Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions. Tabular Model Definition Language (`TMDL`, `.tmdl` files) inside `.pbip` splits model metadata into modular, merge-friendly text files per table, role, and perspective. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. Local study-map skill 1.7 (Create and Manage Power BI Desktop Projects (.pbip) with TMDL, PBIR, and .gitignore Hygiene), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Power BI Desktop projects (.pbip), TMDL, and PBIR (https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview).

- **A:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Tabular Model Definition Language (`TMDL`, `.tmdl` files) inside `.pbip` splits model metadata into modular, merge-friendly text files per table, role, and perspective.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Tabular Model Definition Language (`TMDL`, `.tmdl` files) inside `.pbip` splits model metadata into modular, merge-friendly text files per table, role, and perspective.
- **C:** Correct. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. In this scenario: Tabular Model Definition Language (`TMDL`, `.tmdl` files) inside `.pbip` splits model metadata into modular, merge-friendly text files per table, role, and perspective.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Tabular Model Definition Language (`TMDL`, `.tmdl` files) inside `.pbip` splits model metadata into modular, merge-friendly text files per table, role, and perspective.

### Question 17 — A, D

Answers: Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions; Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository. Storing semantic models/reports in `.pbip` (`TMDL` + `PBIR`) enables granular text diffs, while keeping `**/cache.abf` and `**/localSettings.json` in `.gitignore` blocks local data caches and UI state. Local study-map skill 1.7 (Create and Manage Power BI Desktop Projects (.pbip) with TMDL, PBIR, and .gitignore Hygiene), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Power BI Desktop projects (.pbip), TMDL, and PBIR (https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview).

- **A:** Correct. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. In this scenario: Storing semantic models/reports in `.pbip` (`TMDL` + `PBIR`) enables granular text diffs, while keeping `**/cache.abf` and `**/localSettings.json` in `.gitignore` blocks local data caches and UI state.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Storing semantic models/reports in `.pbip` (`TMDL` + `PBIR`) enables granular text diffs, while keeping `**/cache.abf` and `**/localSettings.json` in `.gitignore` blocks local data caches and UI state.
- **C:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Storing semantic models/reports in `.pbip` (`TMDL` + `PBIR`) enables granular text diffs, while keeping `**/cache.abf` and `**/localSettings.json` in `.gitignore` blocks local data caches and UI state.
- **D:** Correct. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. In this scenario: Storing semantic models/reports in `.pbip` (`TMDL` + `PBIR`) enables granular text diffs, while keeping `**/cache.abf` and `**/localSettings.json` in `.gitignore` blocks local data caches and UI state.
- **E:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Storing semantic models/reports in `.pbip` (`TMDL` + `PBIR`) enables granular text diffs, while keeping `**/cache.abf` and `**/localSettings.json` in `.gitignore` blocks local data caches and UI state.

### Question 18 — B

Answer: Perform a selective deployment selecting the modified item together with Select related to include required upstream dependencies. Selecting `SettlementReport` with `Select related` runs a selective deployment promoting only the report and its required `SettlementSemanticModel`. Selective deployment in Fabric Deployment Pipelines promotes only chosen items between stages, and Select related ensures newly referenced lakehouses or semantic models deploy alongside dependent reports. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Why the keyed choice wins: Selecting `SettlementReport` with `Select related` runs a selective deployment promoting only the report and its required `SettlementSemanticModel`.
- **B:** Correct. Selective deployment in Fabric Deployment Pipelines promotes only chosen items between stages, and Select related ensures newly referenced lakehouses or semantic models deploy alongside dependent reports. In this scenario: Selecting `SettlementReport` with `Select related` runs a selective deployment promoting only the report and its required `SettlementSemanticModel`.
- **C:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Selecting `SettlementReport` with `Select related` runs a selective deployment promoting only the report and its required `SettlementSemanticModel`.
- **D:** Incorrect for this requirement. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. Why the keyed choice wins: Selecting `SettlementReport` with `Select related` runs a selective deployment promoting only the report and its required `SettlementSemanticModel`.

### Question 19 — D

Answer: Configure Deployment pipeline data source and parameter rules on the Test and Production stages. Configuring Deployment Pipeline data source rules on the `Test` and `Production` stages rebinds Direct Lake on SQL (and Import/DirectQuery) models automatically. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Configuring Deployment Pipeline data source rules on the `Test` and `Production` stages rebinds Direct Lake on SQL (and Import/DirectQuery) models automatically.
- **B:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Configuring Deployment Pipeline data source rules on the `Test` and `Production` stages rebinds Direct Lake on SQL (and Import/DirectQuery) models automatically.
- **C:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Configuring Deployment Pipeline data source rules on the `Test` and `Production` stages rebinds Direct Lake on SQL (and Import/DirectQuery) models automatically.
- **D:** Correct. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. In this scenario: Configuring Deployment Pipeline data source rules on the `Test` and `Production` stages rebinds Direct Lake on SQL (and Import/DirectQuery) models automatically.

### Question 20 — B

Answer: Use a Fabric Variable library (or autobinding across paired workspace items) to parameterize stage-specific environment references. A Fabric `Variable library` stores stage-specific value sets across pipeline stages for modern Fabric pipelines and workspace items. Fabric Variable libraries store stage-specific workspace/lakehouse IDs, URLs, and thresholds across Dev/Test/Prod — essential for items like Data Pipelines and Direct Lake on OneLake models that do not use legacy SQL deployment rules. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Why the keyed choice wins: A Fabric `Variable library` stores stage-specific value sets across pipeline stages for modern Fabric pipelines and workspace items.
- **B:** Correct. Fabric Variable libraries store stage-specific workspace/lakehouse IDs, URLs, and thresholds across Dev/Test/Prod — essential for items like Data Pipelines and Direct Lake on OneLake models that do not use legacy SQL deployment rules. In this scenario: A Fabric `Variable library` stores stage-specific value sets across pipeline stages for modern Fabric pipelines and workspace items.
- **C:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: A Fabric `Variable library` stores stage-specific value sets across pipeline stages for modern Fabric pipelines and workspace items.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: A Fabric `Variable library` stores stage-specific value sets across pipeline stages for modern Fabric pipelines and workspace items.

### Question 21 — D

Answer: Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts. Opening Workspace `Lineage` view, inspecting the `Impact analysis` side panel on `LegacyFXDataflow`, and using `Notify contacts` identifies all cross-workspace downstream items and alerts owners. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Local study-map skill 1.9 (Perform Downstream Dependency Impact Analysis Across Lakehouses, Warehouses, Dataflows, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Lineage and impact analysis in Microsoft Fabric workspaces (https://learn.microsoft.com/en-us/fabric/governance/lineage).

- **A:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: Opening Workspace `Lineage` view, inspecting the `Impact analysis` side panel on `LegacyFXDataflow`, and using `Notify contacts` identifies all cross-workspace downstream items and alerts owners.
- **B:** Incorrect for this requirement. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. Why the keyed choice wins: Opening Workspace `Lineage` view, inspecting the `Impact analysis` side panel on `LegacyFXDataflow`, and using `Notify contacts` identifies all cross-workspace downstream items and alerts owners.
- **C:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Opening Workspace `Lineage` view, inspecting the `Impact analysis` side panel on `LegacyFXDataflow`, and using `Notify contacts` identifies all cross-workspace downstream items and alerts owners.
- **D:** Correct. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. In this scenario: Opening Workspace `Lineage` view, inspecting the `Impact analysis` side panel on `LegacyFXDataflow`, and using `Notify contacts` identifies all cross-workspace downstream items and alerts owners.

### Question 22 — A

Answer: Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts. `INFO.VIEW.TABLES()` inspects internal semantic-model tables only; Workspace `Lineage` view -> `Impact analysis` enumerates downstream reports and dashboards across workspaces. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Local study-map skill 1.9 (Perform Downstream Dependency Impact Analysis Across Lakehouses, Warehouses, Dataflows, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Lineage and impact analysis in Microsoft Fabric workspaces (https://learn.microsoft.com/en-us/fabric/governance/lineage).

- **A:** Correct. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. In this scenario: `INFO.VIEW.TABLES()` inspects internal semantic-model tables only; Workspace `Lineage` view -> `Impact analysis` enumerates downstream reports and dashboards across workspaces.
- **B:** Incorrect for this requirement. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Why the keyed choice wins: `INFO.VIEW.TABLES()` inspects internal semantic-model tables only; Workspace `Lineage` view -> `Impact analysis` enumerates downstream reports and dashboards across workspaces.
- **C:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: `INFO.VIEW.TABLES()` inspects internal semantic-model tables only; Workspace `Lineage` view -> `Impact analysis` enumerates downstream reports and dashboards across workspaces.
- **D:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: `INFO.VIEW.TABLES()` inspects internal semantic-model tables only; Workspace `Lineage` view -> `Impact analysis` enumerates downstream reports and dashboards across workspaces.

### Question 23 — A

Answer: Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows. A Power BI Template (`.pbit`) exports report pages, model schema, measures, and parameters with zero data rows, prompting for `BranchRegionCode` when opened. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Local study-map skill 1.11 (Create and Update Reusable Assets (.pbit Templates, .pbids Data Sources, and Shared Golden Semantic Models)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create and use report templates (.pbit), data sources (.pbids), and shared semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-templates).

- **A:** Correct. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. In this scenario: A Power BI Template (`.pbit`) exports report pages, model schema, measures, and parameters with zero data rows, prompting for `BranchRegionCode` when opened.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: A Power BI Template (`.pbit`) exports report pages, model schema, measures, and parameters with zero data rows, prompting for `BranchRegionCode` when opened.
- **C:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: A Power BI Template (`.pbit`) exports report pages, model schema, measures, and parameters with zero data rows, prompting for `BranchRegionCode` when opened.
- **D:** Incorrect for this requirement. Decoupling a shared golden semantic model from thin live-connected reports prevents measure duplication, reduces capacity memory footprint, and enforces centralized RLS/endorsement across teams. Why the keyed choice wins: A Power BI Template (`.pbit`) exports report pages, model schema, measures, and parameters with zero data rows, prompting for `BranchRegionCode` when opened.

### Question 24 — B

Answer: Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode. Distributing a Power BI Data Source (`.pbids`) file pre-populates the exact connector and Warehouse SQL endpoint URL in Power BI Desktop. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Local study-map skill 1.11 (Create and Update Reusable Assets (.pbit Templates, .pbids Data Sources, and Shared Golden Semantic Models)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create and use report templates (.pbit), data sources (.pbids), and shared semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-templates).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Distributing a Power BI Data Source (`.pbids`) file pre-populates the exact connector and Warehouse SQL endpoint URL in Power BI Desktop.
- **B:** Correct. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. In this scenario: Distributing a Power BI Data Source (`.pbids`) file pre-populates the exact connector and Warehouse SQL endpoint URL in Power BI Desktop.
- **C:** Incorrect for this requirement. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. Why the keyed choice wins: Distributing a Power BI Data Source (`.pbids`) file pre-populates the exact connector and Warehouse SQL endpoint URL in Power BI Desktop.
- **D:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Distributing a Power BI Data Source (`.pbids`) file pre-populates the exact connector and Warehouse SQL endpoint URL in Power BI Desktop.

### Question 25 — A

Answer: Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication. Creating a single `Shareable cloud connection` in `Manage connections and gateways` centralizes authentication and lets authorized pipeline authors reference it without viewing raw credentials. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. Local study-map skill 2.1 (Create Data Connections (Shareable Cloud Connections, On-Premises Gateways, and VNet Data Gateways)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data source management, cloud connections, and VNet/on-premises gateways in Fabric (https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management).

- **A:** Correct. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. In this scenario: Creating a single `Shareable cloud connection` in `Manage connections and gateways` centralizes authentication and lets authorized pipeline authors reference it without viewing raw credentials.
- **B:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Creating a single `Shareable cloud connection` in `Manage connections and gateways` centralizes authentication and lets authorized pipeline authors reference it without viewing raw credentials.
- **C:** Incorrect for this requirement. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. Why the keyed choice wins: Creating a single `Shareable cloud connection` in `Manage connections and gateways` centralizes authentication and lets authorized pipeline authors reference it without viewing raw credentials.
- **D:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Creating a single `Shareable cloud connection` in `Manage connections and gateways` centralizes authentication and lets authorized pipeline authors reference it without viewing raw credentials.

### Question 26 — C

Answer: Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture. The `Govern` tab inside `OneLake catalog` provides centralized data-stewardship health metrics, compliance posture, and guided governance actions. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Local study-map skill 2.2 (Discover Data and Streams Using OneLake Catalog (Explore/Govern) and Real-Time Hub + Activator), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake catalog overview & Real-Time hub in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview).

- **A:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: The `Govern` tab inside `OneLake catalog` provides centralized data-stewardship health metrics, compliance posture, and guided governance actions.
- **B:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: The `Govern` tab inside `OneLake catalog` provides centralized data-stewardship health metrics, compliance posture, and guided governance actions.
- **C:** Correct. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. In this scenario: The `Govern` tab inside `OneLake catalog` provides centralized data-stewardship health metrics, compliance posture, and guided governance actions.
- **D:** Incorrect for this requirement. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Why the keyed choice wins: The `Govern` tab inside `OneLake catalog` provides centralized data-stewardship health metrics, compliance posture, and guided governance actions.

### Question 27 — C, E

Answers: Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture; Use the Real-Time hub to subscribe to Microsoft.Fabric.OneLake.FileCreated events (or Capacity/CDC streams) and trigger an Activator rule. `OneLake catalog` discovers domain-filtered Lakehouses/Warehouses/models, while `Real-Time hub` surfaces streaming data, CDC feeds, and Fabric capacity/OneLake events for Activator. Local study-map skill 2.2 (Discover Data and Streams Using OneLake Catalog (Explore/Govern) and Real-Time Hub + Activator), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake catalog overview & Real-Time hub in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview).

- **A:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: `OneLake catalog` discovers domain-filtered Lakehouses/Warehouses/models, while `Real-Time hub` surfaces streaming data, CDC feeds, and Fabric capacity/OneLake events for Activator.
- **B:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `OneLake catalog` discovers domain-filtered Lakehouses/Warehouses/models, while `Real-Time hub` surfaces streaming data, CDC feeds, and Fabric capacity/OneLake events for Activator.
- **C:** Correct. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. In this scenario: `OneLake catalog` discovers domain-filtered Lakehouses/Warehouses/models, while `Real-Time hub` surfaces streaming data, CDC feeds, and Fabric capacity/OneLake events for Activator.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `OneLake catalog` discovers domain-filtered Lakehouses/Warehouses/models, while `Real-Time hub` surfaces streaming data, CDC feeds, and Fabric capacity/OneLake events for Activator.
- **E:** Correct. Real-Time hub unifies streaming sources, CDC feeds, Azure Blob events, and Fabric workspace/OneLake/Capacity events so analytics engineers can discover streams in one catalog and trigger event-driven pipelines or Notebooks via Activator. In this scenario: `OneLake catalog` discovers domain-filtered Lakehouses/Warehouses/models, while `Real-Time hub` surfaces streaming data, CDC feeds, and Fabric capacity/OneLake events for Activator.

### Question 28 — D

Answer: Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching. Creating an external `OneLake shortcut` pointing to the ADLS Gen2 Delta path mounts the tables virtually under `QuantLakehouse/Tables` without copying bytes. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Creating an external `OneLake shortcut` pointing to the ADLS Gen2 Delta path mounts the tables virtually under `QuantLakehouse/Tables` without copying bytes.
- **B:** Incorrect for this requirement. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. Why the keyed choice wins: Creating an external `OneLake shortcut` pointing to the ADLS Gen2 Delta path mounts the tables virtually under `QuantLakehouse/Tables` without copying bytes.
- **C:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: Creating an external `OneLake shortcut` pointing to the ADLS Gen2 Delta path mounts the tables virtually under `QuantLakehouse/Tables` without copying bytes.
- **D:** Correct. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. In this scenario: Creating an external `OneLake shortcut` pointing to the ADLS Gen2 Delta path mounts the tables virtually under `QuantLakehouse/Tables` without copying bytes.

### Question 29 — C

Answer: Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake. A Data Factory Pipeline `Copy activity` performs high-throughput binary/raw file ingestion at far lower CU cost than Dataflow Gen2 or Spark row-by-row parsing. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` performs high-throughput binary/raw file ingestion at far lower CU cost than Dataflow Gen2 or Spark row-by-row parsing.
- **B:** Incorrect for this requirement. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` performs high-throughput binary/raw file ingestion at far lower CU cost than Dataflow Gen2 or Spark row-by-row parsing.
- **C:** Correct. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. In this scenario: A Data Factory Pipeline `Copy activity` performs high-throughput binary/raw file ingestion at far lower CU cost than Dataflow Gen2 or Spark row-by-row parsing.
- **D:** Incorrect for this requirement. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. Why the keyed choice wins: A Data Factory Pipeline `Copy activity` performs high-throughput binary/raw file ingestion at far lower CU cost than Dataflow Gen2 or Spark row-by-row parsing.

### Question 30 — D

Answer: Deduplicate using ROW_NUMBER() OVER (PARTITION BY BusinessKey ORDER BY ModifiedTimestamp DESC) = 1. `SELECT DISTINCT *` retains every retry because `IngestionEpochMs` differs; windowing with `ROW_NUMBER() OVER (PARTITION BY SettlementBatchId ORDER BY IngestionEpochMs DESC) = 1` keeps strictly the latest row per batch. Windowing by BusinessKey ordered descending by ingestion or source-change timestamp deterministically retains only the latest version of duplicate CDC events while preserving all non-key columns. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `SELECT DISTINCT *` retains every retry because `IngestionEpochMs` differs; windowing with `ROW_NUMBER() OVER (PARTITION BY SettlementBatchId ORDER BY IngestionEpochMs DESC) = 1` keeps strictly the latest row per batch.
- **B:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: `SELECT DISTINCT *` retains every retry because `IngestionEpochMs` differs; windowing with `ROW_NUMBER() OVER (PARTITION BY SettlementBatchId ORDER BY IngestionEpochMs DESC) = 1` keeps strictly the latest row per batch.
- **C:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: `SELECT DISTINCT *` retains every retry because `IngestionEpochMs` differs; windowing with `ROW_NUMBER() OVER (PARTITION BY SettlementBatchId ORDER BY IngestionEpochMs DESC) = 1` keeps strictly the latest row per batch.
- **D:** Correct. Windowing by BusinessKey ordered descending by ingestion or source-change timestamp deterministically retains only the latest version of duplicate CDC events while preserving all non-key columns. In this scenario: `SELECT DISTINCT *` retains every retry because `IngestionEpochMs` differs; windowing with `ROW_NUMBER() OVER (PARTITION BY SettlementBatchId ORDER BY IngestionEpochMs DESC) = 1` keeps strictly the latest row per batch.

### Question 31 — A, B, C

Answers: Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching; Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table; Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog. `OneLake shortcuts` virtualize S3 Parquet, `Eventstream` ingests live Kafka topics, and `Database Mirroring` replicates Cosmos DB CDC into OneLake automatically. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Correct. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. In this scenario: `OneLake shortcuts` virtualize S3 Parquet, `Eventstream` ingests live Kafka topics, and `Database Mirroring` replicates Cosmos DB CDC into OneLake automatically.
- **B:** Correct. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. In this scenario: `OneLake shortcuts` virtualize S3 Parquet, `Eventstream` ingests live Kafka topics, and `Database Mirroring` replicates Cosmos DB CDC into OneLake automatically.
- **C:** Correct. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. In this scenario: `OneLake shortcuts` virtualize S3 Parquet, `Eventstream` ingests live Kafka topics, and `Database Mirroring` replicates Cosmos DB CDC into OneLake automatically.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `OneLake shortcuts` virtualize S3 Parquet, `Eventstream` ingests live Kafka topics, and `Database Mirroring` replicates Cosmos DB CDC into OneLake automatically.
- **E:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `OneLake shortcuts` virtualize S3 Parquet, `Eventstream` ingests live Kafka topics, and `Database Mirroring` replicates Cosmos DB CDC into OneLake automatically.
- **F:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `OneLake shortcuts` virtualize S3 Parquet, `Eventstream` ingests live Kafka topics, and `Database Mirroring` replicates Cosmos DB CDC into OneLake automatically.

### Question 32 — D

Answer: Choose a Fabric Data Warehouse. `Fabric Data Warehouse` supports full multi-table ACID T-SQL DML transactions across tables, whereas Lakehouse SQL analytics endpoints are read-only. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Incorrect for this requirement. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Why the keyed choice wins: `Fabric Data Warehouse` supports full multi-table ACID T-SQL DML transactions across tables, whereas Lakehouse SQL analytics endpoints are read-only.
- **B:** Incorrect for this requirement. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. Why the keyed choice wins: `Fabric Data Warehouse` supports full multi-table ACID T-SQL DML transactions across tables, whereas Lakehouse SQL analytics endpoints are read-only.
- **C:** Incorrect for this requirement. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. Why the keyed choice wins: `Fabric Data Warehouse` supports full multi-table ACID T-SQL DML transactions across tables, whereas Lakehouse SQL analytics endpoints are read-only.
- **D:** Correct. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. In this scenario: `Fabric Data Warehouse` supports full multi-table ACID T-SQL DML transactions across tables, whereas Lakehouse SQL analytics endpoints are read-only.

### Question 33 — D

Answer: Choose a Fabric Eventhouse (KQL database). `Fabric Eventhouse` (KQL database) is optimized for ultra-high-ingestion time-series and semi-structured JSON event analytics. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) is optimized for ultra-high-ingestion time-series and semi-structured JSON event analytics.
- **B:** Incorrect for this requirement. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) is optimized for ultra-high-ingestion time-series and semi-structured JSON event analytics.
- **C:** Incorrect for this requirement. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) is optimized for ultra-high-ingestion time-series and semi-structured JSON event analytics.
- **D:** Correct. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. In this scenario: `Fabric Eventhouse` (KQL database) is optimized for ultra-high-ingestion time-series and semi-structured JSON event analytics.

### Question 34 — A, D

Answers: Choose a Fabric Lakehouse; Choose a SQL database in Microsoft Fabric. `SQL database in Microsoft Fabric` serves transactional OLTP workloads (auto-mirrored to OneLake), and `Lakehouse` stores unstructured `Files/` alongside Spark-engineered Delta `Tables/`. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Correct. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. In this scenario: `SQL database in Microsoft Fabric` serves transactional OLTP workloads (auto-mirrored to OneLake), and `Lakehouse` stores unstructured `Files/` alongside Spark-engineered Delta `Tables/`.
- **B:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `SQL database in Microsoft Fabric` serves transactional OLTP workloads (auto-mirrored to OneLake), and `Lakehouse` stores unstructured `Files/` alongside Spark-engineered Delta `Tables/`.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `SQL database in Microsoft Fabric` serves transactional OLTP workloads (auto-mirrored to OneLake), and `Lakehouse` stores unstructured `Files/` alongside Spark-engineered Delta `Tables/`.
- **D:** Correct. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. In this scenario: `SQL database in Microsoft Fabric` serves transactional OLTP workloads (auto-mirrored to OneLake), and `Lakehouse` stores unstructured `Files/` alongside Spark-engineered Delta `Tables/`.
- **E:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: `SQL database in Microsoft Fabric` serves transactional OLTP workloads (auto-mirrored to OneLake), and `Lakehouse` stores unstructured `Files/` alongside Spark-engineered Delta `Tables/`.

### Question 35 — C

Answer: Enable OneLake availability on the Eventhouse KQL database (or specific KQL table) and create an internal OneLake shortcut in the Lakehouse. Unlike Lakehouses and Warehouses, Eventhouse KQL databases expose Delta Parquet in OneLake as an opt-in feature; turning on `OneLake availability` publishes the synced OneLake Delta table. KQL databases do not write Delta Parquet to OneLake by default; turning on OneLake availability creates a synced Delta Parquet logical representation in OneLake that Spark, SQL analytics endpoints, and Direct Lake on OneLake models can read without data movement. Local study-map skill 2.5 (Implement OneLake Integration for Eventhouse (OneLake Availability) and Import Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Eventhouse OneLake availability & OneLake integration for semantic models (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/one-lake-availability).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Unlike Lakehouses and Warehouses, Eventhouse KQL databases expose Delta Parquet in OneLake as an opt-in feature; turning on `OneLake availability` publishes the synced OneLake Delta table.
- **B:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Unlike Lakehouses and Warehouses, Eventhouse KQL databases expose Delta Parquet in OneLake as an opt-in feature; turning on `OneLake availability` publishes the synced OneLake Delta table.
- **C:** Correct. KQL databases do not write Delta Parquet to OneLake by default; turning on OneLake availability creates a synced Delta Parquet logical representation in OneLake that Spark, SQL analytics endpoints, and Direct Lake on OneLake models can read without data movement. In this scenario: Unlike Lakehouses and Warehouses, Eventhouse KQL databases expose Delta Parquet in OneLake as an opt-in feature; turning on `OneLake availability` publishes the synced OneLake Delta table.
- **D:** Incorrect for this requirement. Eventhouse KQL databases do not write Delta Parquet to OneLake unless OneLake availability is enabled, and Direct Lake on SQL does not support KQL databases (only Direct Lake on OneLake does once OneLake availability is on). Why the keyed choice wins: Unlike Lakehouses and Warehouses, Eventhouse KQL databases expose Delta Parquet in OneLake as an opt-in feature; turning on `OneLake availability` publishes the synced OneLake Delta table.

### Question 36 — D

Answer: Ingest streaming telemetry into an Eventhouse KQL database → Enable OneLake availability on the KQL database or table → Create an internal OneLake shortcut in the Lakehouse → Add the table to a Direct Lake on OneLake semantic model. Streaming into Eventhouse, enabling `OneLake availability` on the KQL database/table, creating an internal OneLake shortcut in the Lakehouse, and modeling with Direct Lake on OneLake avoids manual exports. Correct order: land streaming events in Eventhouse, opt in to OneLake availability so Delta Parquet files sync to OneLake, surface via Lakehouse shortcut (or connect directly), and model with Direct Lake on OneLake. Local study-map skill 2.5 (Implement OneLake Integration for Eventhouse (OneLake Availability) and Import Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Eventhouse OneLake availability & OneLake integration for semantic models (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/one-lake-availability).

- **A:** Incorrect for this requirement. Incorrect: manual hourly CSV exports add latency, operational toil, and duplicate storage instead of native Eventhouse OneLake availability. Why the keyed choice wins: Streaming into Eventhouse, enabling `OneLake availability` on the KQL database/table, creating an internal OneLake shortcut in the Lakehouse, and modeling with Direct Lake on OneLake avoids manual exports.
- **B:** Incorrect for this requirement. Incorrect: KQL tables are internal OneLake sources that only expose Delta Parquet folders after OneLake availability is enabled. Why the keyed choice wins: Streaming into Eventhouse, enabling `OneLake availability` on the KQL database/table, creating an internal OneLake shortcut in the Lakehouse, and modeling with Direct Lake on OneLake avoids manual exports.
- **C:** Incorrect for this requirement. Incorrect: Direct Lake on SQL does not support KQL databases, disabling OneLake availability prevents Delta Parquet generation, and Direct Lake never uses gateways. Why the keyed choice wins: Streaming into Eventhouse, enabling `OneLake availability` on the KQL database/table, creating an internal OneLake shortcut in the Lakehouse, and modeling with Direct Lake on OneLake avoids manual exports.
- **D:** Correct. Correct order: land streaming events in Eventhouse, opt in to OneLake availability so Delta Parquet files sync to OneLake, surface via Lakehouse shortcut (or connect directly), and model with Direct Lake on OneLake. In this scenario: Streaming into Eventhouse, enabling `OneLake availability` on the KQL database/table, creating an internal OneLake shortcut in the Lakehouse, and modeling with Direct Lake on OneLake avoids manual exports.

### Question 37 — C

Answer: Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic. Lakehouse SQL analytics endpoints support read-only `SELECT` views and functions, whereas T-SQL `CREATE PROCEDURE` performing `INSERT`/`UPDATE`/`DELETE`/`MERGE` DML requires a Fabric Data Warehouse (or SQL database in Fabric). Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Lakehouse SQL analytics endpoints support read-only `SELECT` views and functions, whereas T-SQL `CREATE PROCEDURE` performing `INSERT`/`UPDATE`/`DELETE`/`MERGE` DML requires a Fabric Data Warehouse (or SQL database in Fabric).
- **B:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Lakehouse SQL analytics endpoints support read-only `SELECT` views and functions, whereas T-SQL `CREATE PROCEDURE` performing `INSERT`/`UPDATE`/`DELETE`/`MERGE` DML requires a Fabric Data Warehouse (or SQL database in Fabric).
- **C:** Correct. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. In this scenario: Lakehouse SQL analytics endpoints support read-only `SELECT` views and functions, whereas T-SQL `CREATE PROCEDURE` performing `INSERT`/`UPDATE`/`DELETE`/`MERGE` DML requires a Fabric Data Warehouse (or SQL database in Fabric).
- **D:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Lakehouse SQL analytics endpoints support read-only `SELECT` views and functions, whereas T-SQL `CREATE PROCEDURE` performing `INSERT`/`UPDATE`/`DELETE`/`MERGE` DML requires a Fabric Data Warehouse (or SQL database in Fabric).

### Question 38 — A

Answer: Use a Lakehouse Materialized Lake View (or persisted Gold Delta table) instead of a non-materialized SQL analytics endpoint view for Direct Lake on OneLake. Direct Lake on OneLake reads Delta Parquet tables directly from OneLake and cannot bind to non-materialized SQL analytics endpoint views. Non-materialized SQL analytics endpoint views cannot back Direct Lake on OneLake tables and force Direct Lake on SQL into DirectQuery fallback; materializing the view as a Delta table preserves pure in-memory Direct Lake speed. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Correct. Non-materialized SQL analytics endpoint views cannot back Direct Lake on OneLake tables and force Direct Lake on SQL into DirectQuery fallback; materializing the view as a Delta table preserves pure in-memory Direct Lake speed. In this scenario: Direct Lake on OneLake reads Delta Parquet tables directly from OneLake and cannot bind to non-materialized SQL analytics endpoint views.
- **B:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Direct Lake on OneLake reads Delta Parquet tables directly from OneLake and cannot bind to non-materialized SQL analytics endpoint views.
- **C:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: Direct Lake on OneLake reads Delta Parquet tables directly from OneLake and cannot bind to non-materialized SQL analytics endpoint views.
- **D:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Direct Lake on OneLake reads Delta Parquet tables directly from OneLake and cannot bind to non-materialized SQL analytics endpoint views.

### Question 39 — C

Answer: Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic. Standard T-SQL `SELECT` views in a Warehouse let administrators grant `SELECT` on curated projection/filtered views while keeping underlying `gold` or `silver` base tables locked down. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Standard T-SQL `SELECT` views in a Warehouse let administrators grant `SELECT` on curated projection/filtered views while keeping underlying `gold` or `silver` base tables locked down.
- **B:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Standard T-SQL `SELECT` views in a Warehouse let administrators grant `SELECT` on curated projection/filtered views while keeping underlying `gold` or `silver` base tables locked down.
- **C:** Correct. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. In this scenario: Standard T-SQL `SELECT` views in a Warehouse let administrators grant `SELECT` on curated projection/filtered views while keeping underlying `gold` or `silver` base tables locked down.
- **D:** Incorrect for this requirement. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Why the keyed choice wins: Standard T-SQL `SELECT` views in a Warehouse let administrators grant `SELECT` on curated projection/filtered views while keeping underlying `gold` or `silver` base tables locked down.

### Question 40 — A

Answer: Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions. Replacing a 24-byte string natural key across billions of daily balance rows with a 4-byte integer surrogate key cuts Delta Parquet and VertiPaq foreign-key storage and accelerates hash joins. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Correct. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. In this scenario: Replacing a 24-byte string natural key across billions of daily balance rows with a 4-byte integer surrogate key cuts Delta Parquet and VertiPaq foreign-key storage and accelerates hash joins.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Replacing a 24-byte string natural key across billions of daily balance rows with a 4-byte integer surrogate key cuts Delta Parquet and VertiPaq foreign-key storage and accelerates hash joins.
- **C:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: Replacing a 24-byte string natural key across billions of daily balance rows with a 4-byte integer surrogate key cuts Delta Parquet and VertiPaq foreign-key storage and accelerates hash joins.
- **D:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Replacing a 24-byte string natural key across billions of daily balance rows with a 4-byte integer surrogate key cuts Delta Parquet and VertiPaq foreign-key storage and accelerates hash joins.

### Question 41 — D

Answer: Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes. Building a shared Gold `DimCalendar` table with `IsTradingDay`, `TradingDayOfMonth`, and April-start fiscal columns standardizes business-day logic across every fact table. A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: Building a shared Gold `DimCalendar` table with `IsTradingDay`, `TradingDayOfMonth`, and April-start fiscal columns standardizes business-day logic across every fact table.
- **B:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Building a shared Gold `DimCalendar` table with `IsTradingDay`, `TradingDayOfMonth`, and April-start fiscal columns standardizes business-day logic across every fact table.
- **C:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Building a shared Gold `DimCalendar` table with `IsTradingDay`, `TradingDayOfMonth`, and April-start fiscal columns standardizes business-day logic across every fact table.
- **D:** Correct. A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering. In this scenario: Building a shared Gold `DimCalendar` table with `IsTradingDay`, `TradingDayOfMonth`, and April-start fiscal columns standardizes business-day logic across every fact table.

### Question 42 — B, C

Answers: Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs; Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions. Using vectorized `pyspark.sql.functions` inside `.withColumn()` keeps execution distributed across executors without driver OOMs, and surrogate integer keys optimize downstream Gold joins. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Using vectorized `pyspark.sql.functions` inside `.withColumn()` keeps execution distributed across executors without driver OOMs, and surrogate integer keys optimize downstream Gold joins.
- **B:** Correct. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. In this scenario: Using vectorized `pyspark.sql.functions` inside `.withColumn()` keeps execution distributed across executors without driver OOMs, and surrogate integer keys optimize downstream Gold joins.
- **C:** Correct. Native Catalyst/Photon-optimized pyspark.sql.functions execute in vectorized JVM/native code across partitions, avoiding the severe Python serialization bottleneck of row-level UDFs. In this scenario: Using vectorized `pyspark.sql.functions` inside `.withColumn()` keeps execution distributed across executors without driver OOMs, and surrogate integer keys optimize downstream Gold joins.
- **D:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Using vectorized `pyspark.sql.functions` inside `.withColumn()` keeps execution distributed across executors without driver OOMs, and surrogate integer keys optimize downstream Gold joins.
- **E:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Using vectorized `pyspark.sql.functions` inside `.withColumn()` keeps execution distributed across executors without driver OOMs, and surrogate integer keys optimize downstream Gold joins.

### Question 43 — B

Answer: Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns. `SCD Type 2` creates a new `DimBorrower` version row with a new surrogate `BorrowerKey`, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag so historical facts stay tied to `AA`. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Why the keyed choice wins: `SCD Type 2` creates a new `DimBorrower` version row with a new surrogate `BorrowerKey`, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag so historical facts stay tied to `AA`.
- **B:** Correct. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. In this scenario: `SCD Type 2` creates a new `DimBorrower` version row with a new surrogate `BorrowerKey`, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag so historical facts stay tied to `AA`.
- **C:** Incorrect for this requirement. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Why the keyed choice wins: `SCD Type 2` creates a new `DimBorrower` version row with a new surrogate `BorrowerKey`, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag so historical facts stay tied to `AA`.
- **D:** Incorrect for this requirement. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Why the keyed choice wins: `SCD Type 2` creates a new `DimBorrower` version row with a new surrogate `BorrowerKey`, `EffectiveStartDate`, `EffectiveEndDate`, and `IsCurrent` flag so historical facts stay tied to `AA`.

### Question 44 — D

Answer: Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures. Keep `FactLoanOriginations` and `FactMonthlyPayments` as separate fact tables at their true atomic grains (sharing conformed `DimBorrower`, `DimBranch`, and `DimDate` dimensions) or allocate fees explicitly. Keeping fact tables at a single, consistent atomic grain with integer foreign keys and additive measures eliminates double-counting and supports flexible rollups across every conformed dimension. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Why the keyed choice wins: Keep `FactLoanOriginations` and `FactMonthlyPayments` as separate fact tables at their true atomic grains (sharing conformed `DimBorrower`, `DimBranch`, and `DimDate` dimensions) or allocate fees explicitly.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Keep `FactLoanOriginations` and `FactMonthlyPayments` as separate fact tables at their true atomic grains (sharing conformed `DimBorrower`, `DimBranch`, and `DimDate` dimensions) or allocate fees explicitly.
- **C:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Keep `FactLoanOriginations` and `FactMonthlyPayments` as separate fact tables at their true atomic grains (sharing conformed `DimBorrower`, `DimBranch`, and `DimDate` dimensions) or allocate fees explicitly.
- **D:** Correct. Keeping fact tables at a single, consistent atomic grain with integer foreign keys and additive measures eliminates double-counting and supports flexible rollups across every conformed dimension. In this scenario: Keep `FactLoanOriginations` and `FactMonthlyPayments` as separate fact tables at their true atomic grains (sharing conformed `DimBorrower`, `DimBranch`, and `DimDate` dimensions) or allocate fees explicitly.

### Question 45 — C

Answer: Stage and deduplicate incoming records by natural key → Compare tracked attributes against active (IsCurrent = 1) Gold rows → Expire changed active rows (EffectiveEndDate, IsCurrent = 0) → Insert new active versions with fresh surrogate keys. Deduplicating staged HR records, comparing attributes against `IsCurrent = 1` rows, expiring changed rows (`EffectiveEndDate`, `IsCurrent = 0`), and inserting new active rows with fresh surrogate keys preserves historical attribution. Correct order: deduplicate staging first, detect attribute changes against current rows, close out prior active intervals without losing their surrogate keys, and insert new active versions. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. Incorrect: new versions must be active (IsCurrent = 1), EffectiveStartDate of historical intervals must remain immutable, and natural keys are required to match future CDC updates. Why the keyed choice wins: Deduplicating staged HR records, comparing attributes against `IsCurrent = 1` rows, expiring changed rows (`EffectiveEndDate`, `IsCurrent = 0`), and inserting new active rows with fresh surrogate keys preserves historical attribution.
- **B:** Incorrect for this requirement. Incorrect: deleting unmatched keys and enabling Assume referential integrity omits orphan rows silently in INNER JOINs. Why the keyed choice wins: Deduplicating staged HR records, comparing attributes against `IsCurrent = 1` rows, expiring changed rows (`EffectiveEndDate`, `IsCurrent = 0`), and inserting new active rows with fresh surrogate keys preserves historical attribution.
- **C:** Correct. Correct order: deduplicate staging first, detect attribute changes against current rows, close out prior active intervals without losing their surrogate keys, and insert new active versions. In this scenario: Deduplicating staged HR records, comparing attributes against `IsCurrent = 1` rows, expiring changed rows (`EffectiveEndDate`, `IsCurrent = 0`), and inserting new active rows with fresh surrogate keys preserves historical attribution.
- **D:** Incorrect for this requirement. Incorrect: regenerating surrogate keys on truncate breaks every existing historical fact foreign key, and marking multiple rows IsCurrent = 1 duplicates fact joins. Why the keyed choice wins: Deduplicating staged HR records, comparing attributes against `IsCurrent = 1` rows, expiring changed rows (`EffectiveEndDate`, `IsCurrent = 0`), and inserting new active rows with fresh surrogate keys preserves historical attribution.

### Question 46 — C, D, E

Answers: Organize OneLake into Bronze (raw immutable), Silver (validated, deduplicated, conformed), and Gold (star-schema dimensions and facts with V-Order); Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns; Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE. Enforcing Bronze/Silver/Gold Medallion separation, versioning tracked dimension attributes with SCD Type 2, and mapping unmatched/late foreign keys via `COALESCE` to `-1` Unknown rows prevent silent data loss and restatement bugs. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Enforcing Bronze/Silver/Gold Medallion separation, versioning tracked dimension attributes with SCD Type 2, and mapping unmatched/late foreign keys via `COALESCE` to `-1` Unknown rows prevent silent data loss and restatement bugs.
- **B:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Enforcing Bronze/Silver/Gold Medallion separation, versioning tracked dimension attributes with SCD Type 2, and mapping unmatched/late foreign keys via `COALESCE` to `-1` Unknown rows prevent silent data loss and restatement bugs.
- **C:** Correct. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. In this scenario: Enforcing Bronze/Silver/Gold Medallion separation, versioning tracked dimension attributes with SCD Type 2, and mapping unmatched/late foreign keys via `COALESCE` to `-1` Unknown rows prevent silent data loss and restatement bugs.
- **D:** Correct. The Medallion architecture separates raw source fidelity (Bronze), enterprise data quality/conformance (Silver), and BI/Direct Lake star-schema consumption (Gold). In this scenario: Enforcing Bronze/Silver/Gold Medallion separation, versioning tracked dimension attributes with SCD Type 2, and mapping unmatched/late foreign keys via `COALESCE` to `-1` Unknown rows prevent silent data loss and restatement bugs.
- **E:** Correct. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. In this scenario: Enforcing Bronze/Silver/Gold Medallion separation, versioning tracked dimension attributes with SCD Type 2, and mapping unmatched/late foreign keys via `COALESCE` to `-1` Unknown rows prevent silent data loss and restatement bugs.
- **F:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Enforcing Bronze/Silver/Gold Medallion separation, versioning tracked dimension attributes with SCD Type 2, and mapping unmatched/late foreign keys via `COALESCE` to `-1` Unknown rows prevent silent data loss and restatement bugs.

### Question 47 — D

Answer: Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension. Denormalizing `DepartmentName`, `BusinessUnitName`, and `LegalEntityName` onto a single flattened `Gold.DimCostCenter` dimension removes three snowflake joins. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Local study-map skill 2.9 (Denormalize Snowflake Hierarchies into Flattened Gold Dimension Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Dimensional modeling & denormalizing snowflake tables in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables).

- **A:** Incorrect for this requirement. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Why the keyed choice wins: Denormalizing `DepartmentName`, `BusinessUnitName`, and `LegalEntityName` onto a single flattened `Gold.DimCostCenter` dimension removes three snowflake joins.
- **B:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Denormalizing `DepartmentName`, `BusinessUnitName`, and `LegalEntityName` onto a single flattened `Gold.DimCostCenter` dimension removes three snowflake joins.
- **C:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Denormalizing `DepartmentName`, `BusinessUnitName`, and `LegalEntityName` onto a single flattened `Gold.DimCostCenter` dimension removes three snowflake joins.
- **D:** Correct. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. In this scenario: Denormalizing `DepartmentName`, `BusinessUnitName`, and `LegalEntityName` onto a single flattened `Gold.DimCostCenter` dimension removes three snowflake joins.

### Question 48 — B

Answer: Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension. A single star dimension requires relationships and column transcoding across only one `1:*` hop (`DimInstrument -> FactPositions`) rather than traversing chained intermediate foreign keys across three tables. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Local study-map skill 2.9 (Denormalize Snowflake Hierarchies into Flattened Gold Dimension Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Dimensional modeling & denormalizing snowflake tables in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables).

- **A:** Incorrect for this requirement. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Why the keyed choice wins: A single star dimension requires relationships and column transcoding across only one `1:*` hop (`DimInstrument -> FactPositions`) rather than traversing chained intermediate foreign keys across three tables.
- **B:** Correct. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. In this scenario: A single star dimension requires relationships and column transcoding across only one `1:*` hop (`DimInstrument -> FactPositions`) rather than traversing chained intermediate foreign keys across three tables.
- **C:** Incorrect for this requirement. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Why the keyed choice wins: A single star dimension requires relationships and column transcoding across only one `1:*` hop (`DimInstrument -> FactPositions`) rather than traversing chained intermediate foreign keys across three tables.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: A single star dimension requires relationships and column transcoding across only one `1:*` hop (`DimInstrument -> FactPositions`) rather than traversing chained intermediate foreign keys across three tables.

### Question 49 — A

Answer: Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP). Materializing a pre-aggregated hourly `FactHourlyTickerSummary` Gold Delta table reduces row volume by orders of magnitude while answering every Risk Committee visual directly. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Correct. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. In this scenario: Materializing a pre-aggregated hourly `FactHourlyTickerSummary` Gold Delta table reduces row volume by orders of magnitude while answering every Risk Committee visual directly.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Materializing a pre-aggregated hourly `FactHourlyTickerSummary` Gold Delta table reduces row volume by orders of magnitude while answering every Risk Committee visual directly.
- **C:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Materializing a pre-aggregated hourly `FactHourlyTickerSummary` Gold Delta table reduces row volume by orders of magnitude while answering every Risk Committee visual directly.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Materializing a pre-aggregated hourly `FactHourlyTickerSummary` Gold Delta table reduces row volume by orders of magnitude while answering every Risk Committee visual directly.

### Question 50 — C

Answer: GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ()). `GROUP BY GROUPING SETS ((Desk, AssetClass), (Desk), ())` (using `GROUPING SETS`) computes exact specified subtotals and grand total in a single pass. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Incorrect for this requirement. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Why the keyed choice wins: `GROUP BY GROUPING SETS ((Desk, AssetClass), (Desk), ())` (using `GROUPING SETS`) computes exact specified subtotals and grand total in a single pass.
- **B:** Incorrect for this requirement. percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse. Why the keyed choice wins: `GROUP BY GROUPING SETS ((Desk, AssetClass), (Desk), ())` (using `GROUPING SETS`) computes exact specified subtotals and grand total in a single pass.
- **C:** Correct. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. In this scenario: `GROUP BY GROUPING SETS ((Desk, AssetClass), (Desk), ())` (using `GROUPING SETS`) computes exact specified subtotals and grand total in a single pass.
- **D:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `GROUP BY GROUPING SETS ((Desk, AssetClass), (Desk), ())` (using `GROUPING SETS`) computes exact specified subtotals and grand total in a single pass.

### Question 51 — B

Answer: Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table. Account balances are semi-additive: summing Monday's `$100` balance plus Tuesday's `$100` balance falsely reports `$200`; balances sum across accounts (`SUM`) but take `LASTNONBLANK` / closing snapshot across time. User-defined Import aggregations satisfy high-level grouped queries purely from in-memory VertiPaq cache and automatically route only unaggregated detail drill-throughs to the underlying DirectQuery source. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Account balances are semi-additive: summing Monday's `$100` balance plus Tuesday's `$100` balance falsely reports `$200`; balances sum across accounts (`SUM`) but take `LASTNONBLANK` / closing snapshot across time.
- **B:** Correct. User-defined Import aggregations satisfy high-level grouped queries purely from in-memory VertiPaq cache and automatically route only unaggregated detail drill-throughs to the underlying DirectQuery source. In this scenario: Account balances are semi-additive: summing Monday's `$100` balance plus Tuesday's `$100` balance falsely reports `$200`; balances sum across accounts (`SUM`) but take `LASTNONBLANK` / closing snapshot across time.
- **C:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Account balances are semi-additive: summing Monday's `$100` balance plus Tuesday's `$100` balance falsely reports `$200`; balances sum across accounts (`SUM`) but take `LASTNONBLANK` / closing snapshot across time.
- **D:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Account balances are semi-additive: summing Monday's `$100` balance plus Tuesday's `$100` balance falsely reports `$200`; balances sum across accounts (`SUM`) but take `LASTNONBLANK` / closing snapshot across time.

### Question 52 — C

Answer: WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET. `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` avoids unnecessary Delta file rewrites on unchanged matched records. Guarding WHEN MATCHED with a hash/attribute inequality prevents rewriting unchanged Delta Parquet files on untouched rows during incremental upserts. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` avoids unnecessary Delta file rewrites on unchanged matched records.
- **B:** Incorrect for this requirement. Omitting PARTITION BY ranks across the entire table globally rather than per entity, and RANK() returns duplicate rank-1 rows on exact timestamp ties. Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` avoids unnecessary Delta file rewrites on unchanged matched records.
- **C:** Correct. Guarding WHEN MATCHED with a hash/attribute inequality prevents rewriting unchanged Delta Parquet files on untouched rows during incremental upserts. In this scenario: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` avoids unnecessary Delta file rewrites on unchanged matched records.
- **D:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` avoids unnecessary Delta file rewrites on unchanged matched records.

### Question 53 — C

Answer: Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table. A `Left Anti Join` (`NOT EXISTS`) returns exclusively rows from `ExternalSwiftConfirmations` absent from `InternalLedgerWires`. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. Delta Lake MERGE INTO (in Spark SQL, PySpark DeltaTable.forPath().merge(), or Warehouse T-SQL) atomically applies incremental CDC inserts, updates, and soft-deletes in a single ACID transaction. Why the keyed choice wins: A `Left Anti Join` (`NOT EXISTS`) returns exclusively rows from `ExternalSwiftConfirmations` absent from `InternalLedgerWires`.
- **B:** Incorrect for this requirement. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Why the keyed choice wins: A `Left Anti Join` (`NOT EXISTS`) returns exclusively rows from `ExternalSwiftConfirmations` absent from `InternalLedgerWires`.
- **C:** Correct. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. In this scenario: A `Left Anti Join` (`NOT EXISTS`) returns exclusively rows from `ExternalSwiftConfirmations` absent from `InternalLedgerWires`.
- **D:** Incorrect for this requirement. Broadcasting a small dimension table (<10–100 MB) to every executor avoids an expensive cluster-wide shuffle sort-merge join of the massive fact DataFrame. Why the keyed choice wins: A `Left Anti Join` (`NOT EXISTS`) returns exclusively rows from `ExternalSwiftConfirmations` absent from `InternalLedgerWires`.

### Question 54 — B, C

Answers: fact_df.join(F.broadcast(dim_store_df), on="StoreKey", how="left"); Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement. `F.broadcast(dim_mcc_codes)` broadcasts the 3 MB lookup to every executor without shuffling 1.4B rows, and Delta `MERGE INTO` applies ACID upserts cleanly. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: `F.broadcast(dim_mcc_codes)` broadcasts the 3 MB lookup to every executor without shuffling 1.4B rows, and Delta `MERGE INTO` applies ACID upserts cleanly.
- **B:** Correct. Delta Lake MERGE INTO (in Spark SQL, PySpark DeltaTable.forPath().merge(), or Warehouse T-SQL) atomically applies incremental CDC inserts, updates, and soft-deletes in a single ACID transaction. In this scenario: `F.broadcast(dim_mcc_codes)` broadcasts the 3 MB lookup to every executor without shuffling 1.4B rows, and Delta `MERGE INTO` applies ACID upserts cleanly.
- **C:** Correct. Wrapping the small dimension DataFrame in pyspark.sql.functions.broadcast() avoids shuffling the multi-hundred-million-row fact DataFrame across Spark executors. In this scenario: `F.broadcast(dim_mcc_codes)` broadcasts the 3 MB lookup to every executor without shuffling 1.4B rows, and Delta `MERGE INTO` applies ACID upserts cleanly.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `F.broadcast(dim_mcc_codes)` broadcasts the 3 MB lookup to every executor without shuffling 1.4B rows, and Delta `MERGE INTO` applies ACID upserts cleanly.
- **E:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `F.broadcast(dim_mcc_codes)` broadcasts the 3 MB lookup to every executor without shuffling 1.4B rows, and Delta `MERGE INTO` applies ACID upserts cleanly.

### Question 55 — C

Answer: ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC). `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` deterministically assigns `1` to a single latest row per payment key. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` deterministically assigns `1` to a single latest row per payment key.
- **B:** Incorrect for this requirement. Omitting PARTITION BY ranks across the entire table globally rather than per entity, and RANK() returns duplicate rank-1 rows on exact timestamp ties. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` deterministically assigns `1` to a single latest row per payment key.
- **C:** Correct. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. In this scenario: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` deterministically assigns `1` to a single latest row per payment key.
- **D:** Incorrect for this requirement. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY <Key> ORDER BY EventTimestamp DESC)` deterministically assigns `1` to a single latest row per payment key.

### Question 56 — B, E

Answers: Launch Data Wrangler from a Fabric Spark notebook (or enable Power Query Column profiling based on entire data set) to inspect nulls, duplicates, and distributions and export generated PySpark code; Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE. Profiling the full dataset (in Power Query entire-dataset mode or Spark Data Wrangler) surfaces post-1,000-row nulls, and mapping `NULL` foreign keys to a `-1` Unknown `DimBranch` row prevents dropped mortgage rows. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: Profiling the full dataset (in Power Query entire-dataset mode or Spark Data Wrangler) surfaces post-1,000-row nulls, and mapping `NULL` foreign keys to a `-1` Unknown `DimBranch` row prevents dropped mortgage rows.
- **B:** Correct. Power Query profiles only the top 1,000 rows by default unless switched to entire dataset, whereas Data Wrangler interactively profiles Pandas/Spark DataFrames and emits reproducible Python/PySpark cleaning code. In this scenario: Profiling the full dataset (in Power Query entire-dataset mode or Spark Data Wrangler) surfaces post-1,000-row nulls, and mapping `NULL` foreign keys to a `-1` Unknown `DimBranch` row prevents dropped mortgage rows.
- **C:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Profiling the full dataset (in Power Query entire-dataset mode or Spark Data Wrangler) surfaces post-1,000-row nulls, and mapping `NULL` foreign keys to a `-1` Unknown `DimBranch` row prevents dropped mortgage rows.
- **D:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Profiling the full dataset (in Power Query entire-dataset mode or Spark Data Wrangler) surfaces post-1,000-row nulls, and mapping `NULL` foreign keys to a `-1` Unknown `DimBranch` row prevents dropped mortgage rows.
- **E:** Correct. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. In this scenario: Profiling the full dataset (in Power Query entire-dataset mode or Spark Data Wrangler) surfaces post-1,000-row nulls, and mapping `NULL` foreign keys to a `-1` Unknown `DimBranch` row prevents dropped mortgage rows.

### Question 57 — D

Answer: TRY_CAST(RawReading AS DECIMAL(18, 4)). `TRY_CAST(RawReading AS DECIMAL(18, 4))` safely yields `NULL` on `"PENDING"` and avoids binary floating-point rounding errors on financial rates. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Local study-map skill 2.13 (Convert Column Data Types Safely (TRY_CAST, Fixed Decimal, and Direct Lake Supported Primitive Types)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data types in Fabric Data Warehouse and Direct Lake Delta tables (https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types).

- **A:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` safely yields `NULL` on `"PENDING"` and avoids binary floating-point rounding errors on financial rates.
- **B:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` safely yields `NULL` on `"PENDING"` and avoids binary floating-point rounding errors on financial rates.
- **C:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` safely yields `NULL` on `"PENDING"` and avoids binary floating-point rounding errors on financial rates.
- **D:** Correct. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. In this scenario: `TRY_CAST(RawReading AS DECIMAL(18, 4))` safely yields `NULL` on `"PENDING"` and avoids binary floating-point rounding errors on financial rates.

### Question 58 — D

Answer: Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake. Direct Lake does not support `Binary`, `GUID`, or complex `Struct`/`Array`/`Map` columns; converting hashes to `STRING` (or omitting unused hashes) and flattening/separating array attributes into primitive columns makes them Direct Lake-compatible. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. Local study-map skill 2.13 (Convert Column Data Types Safely (TRY_CAST, Fixed Decimal, and Direct Lake Supported Primitive Types)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data types in Fabric Data Warehouse and Direct Lake Delta tables (https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types).

- **A:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Direct Lake does not support `Binary`, `GUID`, or complex `Struct`/`Array`/`Map` columns; converting hashes to `STRING` (or omitting unused hashes) and flattening/separating array attributes into primitive columns makes them Direct Lake-compatible.
- **B:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Direct Lake does not support `Binary`, `GUID`, or complex `Struct`/`Array`/`Map` columns; converting hashes to `STRING` (or omitting unused hashes) and flattening/separating array attributes into primitive columns makes them Direct Lake-compatible.
- **C:** Incorrect for this requirement. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Why the keyed choice wins: Direct Lake does not support `Binary`, `GUID`, or complex `Struct`/`Array`/`Map` columns; converting hashes to `STRING` (or omitting unused hashes) and flattening/separating array attributes into primitive columns makes them Direct Lake-compatible.
- **D:** Correct. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. In this scenario: Direct Lake does not support `Binary`, `GUID`, or complex `Struct`/`Array`/`Map` columns; converting hashes to `STRING` (or omitting unused hashes) and flattening/separating array attributes into primitive columns makes them Direct Lake-compatible.

### Question 59 — A

Answer: Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled. Moving the foldable `PostingDate >= #date(2026, 1, 1)` filter and column selection BEFORE `Text.Proper` pushes the date filter into Oracle's SQL `WHERE` clause. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. Local study-map skill 2.14 (Filter Data Early Preserving Power Query Folding (View Native Query) and Sargable Delta File Pruning), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query folding indicators & predicate pushdown in Power Query and Delta Lake (https://learn.microsoft.com/en-us/power-query/query-folding-basics).

- **A:** Correct. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. In this scenario: Moving the foldable `PostingDate >= #date(2026, 1, 1)` filter and column selection BEFORE `Text.Proper` pushes the date filter into Oracle's SQL `WHERE` clause.
- **B:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Moving the foldable `PostingDate >= #date(2026, 1, 1)` filter and column selection BEFORE `Text.Proper` pushes the date filter into Oracle's SQL `WHERE` clause.
- **C:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: Moving the foldable `PostingDate >= #date(2026, 1, 1)` filter and column selection BEFORE `Text.Proper` pushes the date filter into Oracle's SQL `WHERE` clause.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Moving the foldable `PostingDate >= #date(2026, 1, 1)` filter and column selection BEFORE `Text.Proper` pushes the date filter into Oracle's SQL `WHERE` clause.

### Question 60 — D

Answer: Filter on physical Delta partition or liquid-clustered date columns using sargable range predicates (OrderDate >= '2026-01-01') without wrapping the column in functions. `WHERE TradeDate >= '2026-10-01' AND TradeDate < '2026-11-01'` is sargable and prunes irrelevant partitions and Parquet files directly via column statistics, whereas `FORMAT(TradeDate, ...)` scans every row. Wrapping a column in YEAR(OrderDate) = 2026 blocks file-level min/max data skipping and partition pruning; sargable range predicates let Spark and SQL endpoints skip irrelevant Parquet files entirely. Local study-map skill 2.14 (Filter Data Early Preserving Power Query Folding (View Native Query) and Sargable Delta File Pruning), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query folding indicators & predicate pushdown in Power Query and Delta Lake (https://learn.microsoft.com/en-us/power-query/query-folding-basics).

- **A:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: `WHERE TradeDate >= '2026-10-01' AND TradeDate < '2026-11-01'` is sargable and prunes irrelevant partitions and Parquet files directly via column statistics, whereas `FORMAT(TradeDate, ...)` scans every row.
- **B:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `WHERE TradeDate >= '2026-10-01' AND TradeDate < '2026-11-01'` is sargable and prunes irrelevant partitions and Parquet files directly via column statistics, whereas `FORMAT(TradeDate, ...)` scans every row.
- **C:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: `WHERE TradeDate >= '2026-10-01' AND TradeDate < '2026-11-01'` is sargable and prunes irrelevant partitions and Parquet files directly via column statistics, whereas `FORMAT(TradeDate, ...)` scans every row.
- **D:** Correct. Wrapping a column in YEAR(OrderDate) = 2026 blocks file-level min/max data skipping and partition pruning; sargable range predicates let Spark and SQL endpoints skip irrelevant Parquet files entirely. In this scenario: `WHERE TradeDate >= '2026-10-01' AND TradeDate < '2026-11-01'` is sargable and prunes irrelevant partitions and Parquet files directly via column statistics, whereas `FORMAT(TradeDate, ...)` scans every row.

### Question 61 — C

Answer: Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view. `New visual query` (Visual query editor) in the Warehouse builds diagram-based joins/filters/aggregations and persists them via `Save as view`. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Local study-map skill 2.15 (Select, Filter, and Aggregate Data Using the Visual Query Editor and Save as SQL Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query using the Visual query editor in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/visual-query-editor).

- **A:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: `New visual query` (Visual query editor) in the Warehouse builds diagram-based joins/filters/aggregations and persists them via `Save as view`.
- **B:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: `New visual query` (Visual query editor) in the Warehouse builds diagram-based joins/filters/aggregations and persists them via `Save as view`.
- **C:** Correct. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. In this scenario: `New visual query` (Visual query editor) in the Warehouse builds diagram-based joins/filters/aggregations and persists them via `Save as view`.
- **D:** Incorrect for this requirement. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Why the keyed choice wins: `New visual query` (Visual query editor) in the Warehouse builds diagram-based joins/filters/aggregations and persists them via `Save as view`.

### Question 62 — A

Answer: Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view. The Visual query editor lets the analyst `Save as view` in the SQL endpoint, `Create a report`, or `Download Excel file` directly from the visual query result without writing T-SQL. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Local study-map skill 2.15 (Select, Filter, and Aggregate Data Using the Visual Query Editor and Save as SQL Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query using the Visual query editor in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/visual-query-editor).

- **A:** Correct. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. In this scenario: The Visual query editor lets the analyst `Save as view` in the SQL endpoint, `Create a report`, or `Download Excel file` directly from the visual query result without writing T-SQL.
- **B:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: The Visual query editor lets the analyst `Save as view` in the SQL endpoint, `Create a report`, or `Download Excel file` directly from the visual query result without writing T-SQL.
- **C:** Incorrect for this requirement. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. Why the keyed choice wins: The Visual query editor lets the analyst `Save as view` in the SQL endpoint, `Create a report`, or `Download Excel file` directly from the visual query result without writing T-SQL.
- **D:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: The Visual query editor lets the analyst `Save as view` in the SQL endpoint, `Create a report`, or `Download Excel file` directly from the visual query result without writing T-SQL.

### Question 63 — D

Answer: LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC). `LAG(<MeasureCol>, 1, 0) OVER (PARTITION BY <EntityId> ORDER BY <TimeCol> ASC)` reads the immediately prior row's value within each partition in a single scan. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `LAG(<MeasureCol>, 1, 0) OVER (PARTITION BY <EntityId> ORDER BY <TimeCol> ASC)` reads the immediately prior row's value within each partition in a single scan.
- **B:** Incorrect for this requirement. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Why the keyed choice wins: `LAG(<MeasureCol>, 1, 0) OVER (PARTITION BY <EntityId> ORDER BY <TimeCol> ASC)` reads the immediately prior row's value within each partition in a single scan.
- **C:** Incorrect for this requirement. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Why the keyed choice wins: `LAG(<MeasureCol>, 1, 0) OVER (PARTITION BY <EntityId> ORDER BY <TimeCol> ASC)` reads the immediately prior row's value within each partition in a single scan.
- **D:** Correct. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. In this scenario: `LAG(<MeasureCol>, 1, 0) OVER (PARTITION BY <EntityId> ORDER BY <TimeCol> ASC)` reads the immediately prior row's value within each partition in a single scan.

### Question 64 — B, D

Answers: OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000'); CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales. `OPTION (FOR TIMESTAMP AS OF ...)` queries point-in-time historical state via Time Travel, and `CREATE TABLE ... AS CLONE OF` creates an instant zero-copy metadata clone. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: `OPTION (FOR TIMESTAMP AS OF ...)` queries point-in-time historical state via Time Travel, and `CREATE TABLE ... AS CLONE OF` creates an instant zero-copy metadata clone.
- **B:** Correct. CREATE TABLE ... AS CLONE OF creates a zero-copy metadata clone of a Fabric Warehouse table instantaneously (optionally AT a specific UTC timestamp) without duplicating Parquet files. In this scenario: `OPTION (FOR TIMESTAMP AS OF ...)` queries point-in-time historical state via Time Travel, and `CREATE TABLE ... AS CLONE OF` creates an instant zero-copy metadata clone.
- **C:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `OPTION (FOR TIMESTAMP AS OF ...)` queries point-in-time historical state via Time Travel, and `CREATE TABLE ... AS CLONE OF` creates an instant zero-copy metadata clone.
- **D:** Correct. Fabric Data Warehouse Time Travel uses the query hint OPTION (FOR TIMESTAMP AS OF 'YYYY-MM-DDTHH:MM:SS.fff') to read exact point-in-time historical snapshots within the retention window. In this scenario: `OPTION (FOR TIMESTAMP AS OF ...)` queries point-in-time historical state via Time Travel, and `CREATE TABLE ... AS CLONE OF` creates an instant zero-copy metadata clone.
- **E:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `OPTION (FOR TIMESTAMP AS OF ...)` queries point-in-time historical state via Time Travel, and `CREATE TABLE ... AS CLONE OF` creates an instant zero-copy metadata clone.

### Question 65 — A

Answer: Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results. Web modeling / Desktop `DAX Query View` evaluates `DEFINE MEASURE` + `EVALUATE SUMMARIZECOLUMNS` queries against live semantic models. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Local study-map skill 2.18 (Select, Filter, and Aggregate Data Using DAX Queries (DAX Query View, EVALUATE, SUMMARIZECOLUMNS, INFO.VIEW)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Work with DAX query view & INFO.VIEW functions in Power BI (https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view).

- **A:** Correct. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. In this scenario: Web modeling / Desktop `DAX Query View` evaluates `DEFINE MEASURE` + `EVALUATE SUMMARIZECOLUMNS` queries against live semantic models.
- **B:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Web modeling / Desktop `DAX Query View` evaluates `DEFINE MEASURE` + `EVALUATE SUMMARIZECOLUMNS` queries against live semantic models.
- **C:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: Web modeling / Desktop `DAX Query View` evaluates `DEFINE MEASURE` + `EVALUATE SUMMARIZECOLUMNS` queries against live semantic models.
- **D:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: Web modeling / Desktop `DAX Query View` evaluates `DEFINE MEASURE` + `EVALUATE SUMMARIZECOLUMNS` queries against live semantic models.

### Question 66 — D

Answer: EVALUATE INFO.VIEW.MEASURES(). `EVALUATE INFO.VIEW.MEASURES()` outputs the model's complete measure catalog directly as a DAX result table. INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags. Local study-map skill 2.18 (Select, Filter, and Aggregate Data Using DAX Queries (DAX Query View, EVALUATE, SUMMARIZECOLUMNS, INFO.VIEW)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Work with DAX query view & INFO.VIEW functions in Power BI (https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view).

- **A:** Incorrect for this requirement. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. Why the keyed choice wins: `EVALUATE INFO.VIEW.MEASURES()` outputs the model's complete measure catalog directly as a DAX result table.
- **B:** Incorrect for this requirement. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Why the keyed choice wins: `EVALUATE INFO.VIEW.MEASURES()` outputs the model's complete measure catalog directly as a DAX result table.
- **C:** Incorrect for this requirement. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. Why the keyed choice wins: `EVALUATE INFO.VIEW.MEASURES()` outputs the model's complete measure catalog directly as a DAX result table.
- **D:** Correct. INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags. In this scenario: `EVALUATE INFO.VIEW.MEASURES()` outputs the model's complete measure catalog directly as a DAX result table.

### Question 67 — A

Answer: Configure Direct Lake storage mode. `Direct Lake` loads OneLake Delta Parquet columns directly into VertiPaq RAM upon framing without scheduled Import copy latency or DirectQuery SQL overhead. Direct Lake loads Delta Parquet columns directly from OneLake into VertiPaq memory on demand without scheduled Import data duplication or slow per-visual SQL translation. Local study-map skill 3.1 (Choose a Semantic Model Storage Mode (Import, DirectQuery, Direct Lake, and Dual)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model storage modes in the Power BI service & Microsoft Fabric (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode).

- **A:** Correct. Direct Lake loads Delta Parquet columns directly from OneLake into VertiPaq memory on demand without scheduled Import data duplication or slow per-visual SQL translation. In this scenario: `Direct Lake` loads OneLake Delta Parquet columns directly into VertiPaq RAM upon framing without scheduled Import copy latency or DirectQuery SQL overhead.
- **B:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Direct Lake` loads OneLake Delta Parquet columns directly into VertiPaq RAM upon framing without scheduled Import copy latency or DirectQuery SQL overhead.
- **C:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Direct Lake` loads OneLake Delta Parquet columns directly into VertiPaq RAM upon framing without scheduled Import copy latency or DirectQuery SQL overhead.
- **D:** Incorrect for this requirement. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Why the keyed choice wins: `Direct Lake` loads OneLake Delta Parquet columns directly into VertiPaq RAM upon framing without scheduled Import copy latency or DirectQuery SQL overhead.

### Question 68 — C

Answer: Configure shared dimension tables in Dual storage mode inside a composite model. `Dual` storage mode caches dimensions in memory for `Import` summary hits while simultaneously allowing native SQL pushdown joins against `DirectQuery` fact tables. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Local study-map skill 3.1 (Choose a Semantic Model Storage Mode (Import, DirectQuery, Direct Lake, and Dual)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model storage modes in the Power BI service & Microsoft Fabric (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode).

- **A:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Dual` storage mode caches dimensions in memory for `Import` summary hits while simultaneously allowing native SQL pushdown joins against `DirectQuery` fact tables.
- **B:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Dual` storage mode caches dimensions in memory for `Import` summary hits while simultaneously allowing native SQL pushdown joins against `DirectQuery` fact tables.
- **C:** Correct. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. In this scenario: `Dual` storage mode caches dimensions in memory for `Import` summary hits while simultaneously allowing native SQL pushdown joins against `DirectQuery` fact tables.
- **D:** Incorrect for this requirement. Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery. Why the keyed choice wins: `Dual` storage mode caches dimensions in memory for `Import` summary hits while simultaneously allowing native SQL pushdown joins against `DirectQuery` fact tables.

### Question 69 — B

Answer: Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column. When relationships use an integer surrogate key rather than the `Date` column itself, `Mark as date table` registers `CalendarDate` as the primary date key so DAX time intelligence automatically applies `REMOVEFILTERS(DimCalendar)`. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. Local study-map skill 3.2 (Implement a Star Schema for a Semantic Model (Mark as Date Table, Hide Keys, Sort by Column, Display Folders)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Set and use date tables & star-schema best practices in Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: When relationships use an integer surrogate key rather than the `Date` column itself, `Mark as date table` registers `CalendarDate` as the primary date key so DAX time intelligence automatically applies `REMOVEFILTERS(DimCalendar)`.
- **B:** Correct. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. In this scenario: When relationships use an integer surrogate key rather than the `Date` column itself, `Mark as date table` registers `CalendarDate` as the primary date key so DAX time intelligence automatically applies `REMOVEFILTERS(DimCalendar)`.
- **C:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: When relationships use an integer surrogate key rather than the `Date` column itself, `Mark as date table` registers `CalendarDate` as the primary date key so DAX time intelligence automatically applies `REMOVEFILTERS(DimCalendar)`.
- **D:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: When relationships use an integer surrogate key rather than the `Date` column itself, `Mark as date table` registers `CalendarDate` as the primary date key so DAX time intelligence automatically applies `REMOVEFILTERS(DimCalendar)`.

### Question 70 — C, E

Answers: Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column; Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear. Disabling `Auto date/time` + marking `DimCalendar` removes hidden date bloat, and hiding surrogate keys/raw columns while setting `FiscalMonthName` `Sort by Column = FiscalMonthOrder` cleans up Excel PivotTables. Local study-map skill 3.2 (Implement a Star Schema for a Semantic Model (Mark as Date Table, Hide Keys, Sort by Column, Display Folders)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Set and use date tables & star-schema best practices in Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables).

- **A:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Disabling `Auto date/time` + marking `DimCalendar` removes hidden date bloat, and hiding surrogate keys/raw columns while setting `FiscalMonthName` `Sort by Column = FiscalMonthOrder` cleans up Excel PivotTables.
- **B:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Disabling `Auto date/time` + marking `DimCalendar` removes hidden date bloat, and hiding surrogate keys/raw columns while setting `FiscalMonthName` `Sort by Column = FiscalMonthOrder` cleans up Excel PivotTables.
- **C:** Correct. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. In this scenario: Disabling `Auto date/time` + marking `DimCalendar` removes hidden date bloat, and hiding surrogate keys/raw columns while setting `FiscalMonthName` `Sort by Column = FiscalMonthOrder` cleans up Excel PivotTables.
- **D:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Disabling `Auto date/time` + marking `DimCalendar` removes hidden date bloat, and hiding surrogate keys/raw columns while setting `FiscalMonthName` `Sort by Column = FiscalMonthOrder` cleans up Excel PivotTables.
- **E:** Correct. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. In this scenario: Disabling `Auto date/time` + marking `DimCalendar` removes hidden date bloat, and hiding surrogate keys/raw columns while setting `FiscalMonthName` `Sort by Column = FiscalMonthOrder` cleans up Excel PivotTables.

### Question 71 — A

Answer: Introduce a deduplicated Bridge table between the two dimensions and scope bidirectional propagation strictly inside specific measures using CROSSFILTER(..., BOTH). Connect `DimLoan (1:* ) BridgeLoanSyndicate (*:1) DimBank` with single-direction relationships by default, and activate `CROSSFILTER(..., BOTH)` only inside specific syndicate attribution measures. Scoping CROSSFILTER(..., BOTH) inside a DAX measure over a bridge table satisfies many-to-many attribution without turning on permanent model-wide bidirectional relationships that cause ambiguity and performance degradation. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Correct. Scoping CROSSFILTER(..., BOTH) inside a DAX measure over a bridge table satisfies many-to-many attribution without turning on permanent model-wide bidirectional relationships that cause ambiguity and performance degradation. In this scenario: Connect `DimLoan (1:* ) BridgeLoanSyndicate (*:1) DimBank` with single-direction relationships by default, and activate `CROSSFILTER(..., BOTH)` only inside specific syndicate attribution measures.
- **B:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Connect `DimLoan (1:* ) BridgeLoanSyndicate (*:1) DimBank` with single-direction relationships by default, and activate `CROSSFILTER(..., BOTH)` only inside specific syndicate attribution measures.
- **C:** Incorrect for this requirement. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Why the keyed choice wins: Connect `DimLoan (1:* ) BridgeLoanSyndicate (*:1) DimBank` with single-direction relationships by default, and activate `CROSSFILTER(..., BOTH)` only inside specific syndicate attribution measures.
- **D:** Incorrect for this requirement. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Why the keyed choice wins: Connect `DimLoan (1:* ) BridgeLoanSyndicate (*:1) DimBank` with single-direction relationships by default, and activate `CROSSFILTER(..., BOTH)` only inside specific syndicate attribution measures.

### Question 72 — A

Answer: Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid. Enabling `Assume referential integrity` on the `1:*` DirectQuery relationship emits `INNER JOIN` queries for faster SQL execution plans. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Correct. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. In this scenario: Enabling `Assume referential integrity` on the `1:*` DirectQuery relationship emits `INNER JOIN` queries for faster SQL execution plans.
- **B:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Enabling `Assume referential integrity` on the `1:*` DirectQuery relationship emits `INNER JOIN` queries for faster SQL execution plans.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Enabling `Assume referential integrity` on the `1:*` DirectQuery relationship emits `INNER JOIN` queries for faster SQL execution plans.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Enabling `Assume referential integrity` on the `1:*` DirectQuery relationship emits `INNER JOIN` queries for faster SQL execution plans.

### Question 73 — B

Answer: Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches. Storing `VAR CurrentLCR = [LCR Ratio]` before `RETURN` evaluates `[LCR Ratio]` once per cell and reuses the cached scalar across both `IF` conditions. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Storing `VAR CurrentLCR = [LCR Ratio]` before `RETURN` evaluates `[LCR Ratio]` once per cell and reuses the cached scalar across both `IF` conditions.
- **B:** Correct. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. In this scenario: Storing `VAR CurrentLCR = [LCR Ratio]` before `RETURN` evaluates `[LCR Ratio]` once per cell and reuses the cached scalar across both `IF` conditions.
- **C:** Incorrect for this requirement. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Why the keyed choice wins: Storing `VAR CurrentLCR = [LCR Ratio]` before `RETURN` evaluates `[LCR Ratio]` once per cell and reuses the cached scalar across both `IF` conditions.
- **D:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: Storing `VAR CurrentLCR = [LCR Ratio]` before `RETURN` evaluates `[LCR Ratio]` once per cell and reuses the cached scalar across both `IF` conditions.

### Question 74 — C

Answer: Pass simple column predicates wrapped in KEEPFILTERS(DimProduct[Color] = "Red") to CALCULATE instead of FILTER(ALL(FactSales), ...). `KEEPFILTERS('DimRating'[RatingBucket] = "High Yield")` preserves and intersects with outer `RatingBucket` filter context rather than overwriting it. KEEPFILTERS intersects the predicate with existing report slicer selections rather than overwriting them, and filtering a dimension column avoids scanning the entire multi-million-row fact table in the Formula Engine. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: `KEEPFILTERS('DimRating'[RatingBucket] = "High Yield")` preserves and intersects with outer `RatingBucket` filter context rather than overwriting it.
- **B:** Incorrect for this requirement. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Why the keyed choice wins: `KEEPFILTERS('DimRating'[RatingBucket] = "High Yield")` preserves and intersects with outer `RatingBucket` filter context rather than overwriting it.
- **C:** Correct. KEEPFILTERS intersects the predicate with existing report slicer selections rather than overwriting them, and filtering a dimension column avoids scanning the entire multi-million-row fact table in the Formula Engine. In this scenario: `KEEPFILTERS('DimRating'[RatingBucket] = "High Yield")` preserves and intersects with outer `RatingBucket` filter context rather than overwriting it.
- **D:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: `KEEPFILTERS('DimRating'[RatingBucket] = "High Yield")` preserves and intersects with outer `RatingBucket` filter context rather than overwriting it.

### Question 75 — D, E

Answers: CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC))); IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK()). `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` navigates custom non-Gregorian periods, and `IF(ISINSCOPE('DimProduct'[SKU]) / 'DimOrg'[Trader], ...)` restricts evaluation strictly to leaf hierarchy rows. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` navigates custom non-Gregorian periods, and `IF(ISINSCOPE('DimProduct'[SKU]) / 'DimOrg'[Trader], ...)` restricts evaluation strictly to leaf hierarchy rows.
- **B:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` navigates custom non-Gregorian periods, and `IF(ISINSCOPE('DimProduct'[SKU]) / 'DimOrg'[Trader], ...)` restricts evaluation strictly to leaf hierarchy rows.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` navigates custom non-Gregorian periods, and `IF(ISINSCOPE('DimProduct'[SKU]) / 'DimOrg'[Trader], ...)` restricts evaluation strictly to leaf hierarchy rows.
- **D:** Correct. OFFSET(-1, ..., ORDERBY(...)) shifts one period backward along a custom 4-4-5 fiscal sort column where standard Gregorian DATEADD fails. In this scenario: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` navigates custom non-Gregorian periods, and `IF(ISINSCOPE('DimProduct'[SKU]) / 'DimOrg'[Trader], ...)` restricts evaluation strictly to leaf hierarchy rows.
- **E:** Correct. ISINSCOPE('DimProduct'[SKU]) evaluates TRUE only when SKU is actively grouping the visual hierarchy level, suppressing misleading margin figures at subtotal rows. In this scenario: `OFFSET(-1, ALLSELECTED(...), ORDERBY(...))` navigates custom non-Gregorian periods, and `IF(ISINSCOPE('DimProduct'[SKU]) / 'DimOrg'[Trader], ...)` restricts evaluation strictly to leaf hierarchy rows.

### Question 76 — D

Answer: CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date])). `SELECTEDMEASURE()` (as in `CALCULATE(SELECTEDMEASURE(), ...)`) dynamically references the measure currently in scope. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Why the keyed choice wins: `SELECTEDMEASURE()` (as in `CALCULATE(SELECTEDMEASURE(), ...)`) dynamically references the measure currently in scope.
- **B:** Incorrect for this requirement. INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags. Why the keyed choice wins: `SELECTEDMEASURE()` (as in `CALCULATE(SELECTEDMEASURE(), ...)`) dynamically references the measure currently in scope.
- **C:** Incorrect for this requirement. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Why the keyed choice wins: `SELECTEDMEASURE()` (as in `CALCULATE(SELECTEDMEASURE(), ...)`) dynamically references the measure currently in scope.
- **D:** Correct. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. In this scenario: `SELECTEDMEASURE()` (as in `CALCULATE(SELECTEDMEASURE(), ...)`) dynamically references the measure currently in scope.

### Question 77 — A

Answer: IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING()). Dynamic Format Strings format display masks dynamically (`$`, `€`, `¥`, `%`, `bps`) while keeping the measure's underlying data type numeric so visuals can chart, sort, and total it. Dynamic format string expressions return a format mask string while preserving the measure's underlying numeric type; SELECTEDMEASUREFORMATSTRING() preserves the base measure's native currency/decimal mask. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Correct. Dynamic format string expressions return a format mask string while preserving the measure's underlying numeric type; SELECTEDMEASUREFORMATSTRING() preserves the base measure's native currency/decimal mask. In this scenario: Dynamic Format Strings format display masks dynamically (`$`, `€`, `¥`, `%`, `bps`) while keeping the measure's underlying data type numeric so visuals can chart, sort, and total it.
- **B:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Dynamic Format Strings format display masks dynamically (`$`, `€`, `¥`, `%`, `bps`) while keeping the measure's underlying data type numeric so visuals can chart, sort, and total it.
- **C:** Incorrect for this requirement. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. Why the keyed choice wins: Dynamic Format Strings format display masks dynamically (`$`, `€`, `¥`, `%`, `bps`) while keeping the measure's underlying data type numeric so visuals can chart, sort, and total it.
- **D:** Incorrect for this requirement. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Why the keyed choice wins: Dynamic Format Strings format display masks dynamically (`$`, `€`, `¥`, `%`, `bps`) while keeping the measure's underlying data type numeric so visuals can chart, sort, and total it.

### Question 78 — B

Answer: Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat). Enabling `Large semantic model storage format` upgrades storage metadata to `LargeDatasetStorageFormat` supporting capacity-limit model sizes. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Local study-map skill 3.6 (Identify Use Cases for and Configure Large Semantic Model Storage Format), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Large semantic models in Microsoft Fabric & Power BI Premium (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-large-models).

- **A:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Enabling `Large semantic model storage format` upgrades storage metadata to `LargeDatasetStorageFormat` supporting capacity-limit model sizes.
- **B:** Correct. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. In this scenario: Enabling `Large semantic model storage format` upgrades storage metadata to `LargeDatasetStorageFormat` supporting capacity-limit model sizes.
- **C:** Incorrect for this requirement. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Why the keyed choice wins: Enabling `Large semantic model storage format` upgrades storage metadata to `LargeDatasetStorageFormat` supporting capacity-limit model sizes.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Enabling `Large semantic model storage format` upgrades storage metadata to `LargeDatasetStorageFormat` supporting capacity-limit model sizes.

### Question 79 — D

Answer: Build a Direct Lake on OneLake composite semantic model combining Direct Lake fact tables from OneLake with Import dimension/target tables using regular relationships. `Direct Lake on OneLake` composite modeling natively combines Direct Lake tables from multiple Fabric sources with `Import` tables from Power Query connectors using regular relationships. Direct Lake on OneLake supports true composite models that mix Direct Lake tables from multiple Fabric items with Import tables from any Power Query connector while preserving fast regular (non-limited) relationships. Local study-map skill 3.7 (Design and Build Composite Models (Direct Lake on OneLake + Import, Dual + Aggregations, DirectQuery over PBI)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use composite models in Power BI Desktop & Direct Lake on OneLake composite models (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-web-modeling).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: `Direct Lake on OneLake` composite modeling natively combines Direct Lake tables from multiple Fabric sources with `Import` tables from Power Query connectors using regular relationships.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Direct Lake on OneLake` composite modeling natively combines Direct Lake tables from multiple Fabric sources with `Import` tables from Power Query connectors using regular relationships.
- **C:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: `Direct Lake on OneLake` composite modeling natively combines Direct Lake tables from multiple Fabric sources with `Import` tables from Power Query connectors using regular relationships.
- **D:** Correct. Direct Lake on OneLake supports true composite models that mix Direct Lake tables from multiple Fabric items with Import tables from any Power Query connector while preserving fast regular (non-limited) relationships. In this scenario: `Direct Lake on OneLake` composite modeling natively combines Direct Lake tables from multiple Fabric sources with `Import` tables from Power Query connectors using regular relationships.

### Question 80 — A, B

Answers: Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table; Create a local composite model using DirectQuery for Power BI semantic models and Analysis Services to combine a certified core semantic model with a departmental Excel/SQL table. User-defined `Import` aggregation tables accelerate grouped DirectQuery visuals in memory, and `DirectQuery for Power BI semantic models` builds a local composite extension over `EquitiesCore`. Local study-map skill 3.7 (Design and Build Composite Models (Direct Lake on OneLake + Import, Dual + Aggregations, DirectQuery over PBI)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use composite models in Power BI Desktop & Direct Lake on OneLake composite models (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-web-modeling).

- **A:** Correct. Connecting to an existing shared semantic model in DirectQuery mode creates a local composite model (using remote model chains and limited cross-island relationships) so analysts can extend governed enterprise measures without copying the core model. In this scenario: User-defined `Import` aggregation tables accelerate grouped DirectQuery visuals in memory, and `DirectQuery for Power BI semantic models` builds a local composite extension over `EquitiesCore`.
- **B:** Correct. User-defined Import aggregations satisfy high-level grouped queries purely from in-memory VertiPaq cache and automatically route only unaggregated detail drill-throughs to the underlying DirectQuery source. In this scenario: User-defined `Import` aggregation tables accelerate grouped DirectQuery visuals in memory, and `DirectQuery for Power BI semantic models` builds a local composite extension over `EquitiesCore`.
- **C:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: User-defined `Import` aggregation tables accelerate grouped DirectQuery visuals in memory, and `DirectQuery for Power BI semantic models` builds a local composite extension over `EquitiesCore`.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: User-defined `Import` aggregation tables accelerate grouped DirectQuery visuals in memory, and `DirectQuery for Power BI semantic models` builds a local composite extension over `EquitiesCore`.
- **E:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: User-defined `Import` aggregation tables accelerate grouped DirectQuery visuals in memory, and `DirectQuery for Power BI semantic models` builds a local composite extension over `EquitiesCore`.

### Question 81 — B

Answer: Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time. `Performance Analyzer` breaks down each visual into `DAX query`, `Visual display`, and `Other` duration, pinpointing visual-count queue contention solved by consolidating cards into fewer matrix/new-card visuals. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Local study-map skill 3.8 (Implement Performance Improvements in Queries and Report Visuals (Performance Analyzer & Query Reduction)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use Performance Analyzer to examine report element performance in Power BI (https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer).

- **A:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: `Performance Analyzer` breaks down each visual into `DAX query`, `Visual display`, and `Other` duration, pinpointing visual-count queue contention solved by consolidating cards into fewer matrix/new-card visuals.
- **B:** Correct. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. In this scenario: `Performance Analyzer` breaks down each visual into `DAX query`, `Visual display`, and `Other` duration, pinpointing visual-count queue contention solved by consolidating cards into fewer matrix/new-card visuals.
- **C:** Incorrect for this requirement. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Why the keyed choice wins: `Performance Analyzer` breaks down each visual into `DAX query`, `Visual display`, and `Other` duration, pinpointing visual-count queue contention solved by consolidating cards into fewer matrix/new-card visuals.
- **D:** Incorrect for this requirement. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. Why the keyed choice wins: `Performance Analyzer` breaks down each visual into `DAX query`, `Visual display`, and `Other` duration, pinpointing visual-count queue contention solved by consolidating cards into fewer matrix/new-card visuals.

### Question 82 — D

Answer: Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages. Enabling `Add an Apply button to each single/multi-select slicer` under `Query reduction` holds query execution until the analyst submits all 6 selections together. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Local study-map skill 3.8 (Implement Performance Improvements in Queries and Report Visuals (Performance Analyzer & Query Reduction)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use Performance Analyzer to examine report element performance in Power BI (https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer).

- **A:** Incorrect for this requirement. Hundreds of tiny streaming Parquet files inflate Delta rowgroup counts past Fabric SKU guardrails and degrade transcoding; OPTIMIZE compacts files into large V-Order-sorted rowgroups optimized for VertiPaq in-memory compression. Why the keyed choice wins: Enabling `Add an Apply button to each single/multi-select slicer` under `Query reduction` holds query execution until the analyst submits all 6 selections together.
- **B:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Enabling `Add an Apply button to each single/multi-select slicer` under `Query reduction` holds query execution until the analyst submits all 6 selections together.
- **C:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Enabling `Add an Apply button to each single/multi-select slicer` under `Query reduction` holds query execution until the analyst submits all 6 selections together.
- **D:** Correct. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. In this scenario: Enabling `Add an Apply button to each single/multi-select slicer` under `Query reduction` holds query execution until the analyst submits all 6 selections together.

### Question 83 — C

Answer: Capture visual timings in Performance Analyzer → Profile captured DAX in DAX Studio with Server Timings and Query Plan → Refactor FILTER(Fact,...) into VAR-cached SE column predicates and run V-Order OPTIMIZE → Re-test with Clear Cache. Capturing the query in Performance Analyzer, profiling FE/SE + CallbackDataID + fallback in DAX Studio Server Timings, rewriting row-level table filters + running `OPTIMIZE VORDER`, and re-benchmarking with `Clear Cache` validates cold-cache speedups. Correct order: isolate visual vs DAX queue time in Performance Analyzer, profile FE/SE and Direct Lake fallback in DAX Studio Server Timings, fix DAX anti-patterns + Delta Parquet layout, and benchmark cold-cache results. Local study-map skill 3.9 (Improve DAX and Model Performance Using DAX Studio Server Timings (FE vs SE) and VertiPaq Cardinality Reduction), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Optimization guide for Power BI — DAX Formula Engine vs Storage Engine & VertiPaq (https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization).

- **A:** Incorrect for this requirement. Incorrect: benchmarking warm cache hides real SE/transcoding cost, GUID columns bloat dictionaries, DirectQueryOnly slows visuals, and 45 cards create visual-queue contention. Why the keyed choice wins: Capturing the query in Performance Analyzer, profiling FE/SE + CallbackDataID + fallback in DAX Studio Server Timings, rewriting row-level table filters + running `OPTIMIZE VORDER`, and re-benchmarking with `Clear Cache` validates cold-cache speedups.
- **B:** Incorrect for this requirement. Incorrect: snowflaking and Auto date/time increase relationship hops and memory overhead rather than resolving FE/SE bottlenecks. Why the keyed choice wins: Capturing the query in Performance Analyzer, profiling FE/SE + CallbackDataID + fallback in DAX Studio Server Timings, rewriting row-level table filters + running `OPTIMIZE VORDER`, and re-benchmarking with `Clear Cache` validates cold-cache speedups.
- **C:** Correct. Correct order: isolate visual vs DAX queue time in Performance Analyzer, profile FE/SE and Direct Lake fallback in DAX Studio Server Timings, fix DAX anti-patterns + Delta Parquet layout, and benchmark cold-cache results. In this scenario: Capturing the query in Performance Analyzer, profiling FE/SE + CallbackDataID + fallback in DAX Studio Server Timings, rewriting row-level table filters + running `OPTIMIZE VORDER`, and re-benchmarking with `Clear Cache` validates cold-cache speedups.
- **D:** Incorrect for this requirement. Incorrect: scaling capacity blindly wastes budget while bidirectional joins, FORMAT() strings, and disabled V-Order make FE and transcoding slower. Why the keyed choice wins: Capturing the query in Performance Analyzer, profiling FE/SE + CallbackDataID + fallback in DAX Studio Server Timings, rewriting row-level table filters + running `OPTIMIZE VORDER`, and re-benchmarking with `Clear Cache` validates cold-cache speedups.

### Question 84 — C

Answer: OPTIMIZE gold.fact_orders VORDER. `OPTIMIZE gold.fact_orders VORDER` bin-packs tiny Parquet files into large optimal rowgroups with V-Order encoding for fast Direct Lake transcoding. Running OPTIMIZE ... VORDER bin-packs small Delta Parquet files into large rowgroups and applies V-Order columnar sorting for peak Direct Lake compression and transcoding. Local study-map skill 3.10 (Configure Direct Lake Framing, Transcoding, V-Order/OPTIMIZE Guardrails, and DirectLakeBehavior Fallback), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: How Direct Lake works (framing, transcoding, V-Order, fallback & DirectLakeBehavior) (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: `OPTIMIZE gold.fact_orders VORDER` bin-packs tiny Parquet files into large optimal rowgroups with V-Order encoding for fast Direct Lake transcoding.
- **B:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `OPTIMIZE gold.fact_orders VORDER` bin-packs tiny Parquet files into large optimal rowgroups with V-Order encoding for fast Direct Lake transcoding.
- **C:** Correct. Running OPTIMIZE ... VORDER bin-packs small Delta Parquet files into large rowgroups and applies V-Order columnar sorting for peak Direct Lake compression and transcoding. In this scenario: `OPTIMIZE gold.fact_orders VORDER` bin-packs tiny Parquet files into large optimal rowgroups with V-Order encoding for fast Direct Lake transcoding.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `OPTIMIZE gold.fact_orders VORDER` bin-packs tiny Parquet files into large optimal rowgroups with V-Order encoding for fast Direct Lake transcoding.

### Question 85 — A, E, F

Answers: Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes; Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails; Set DirectLakeBehavior = DirectLakeOnly on a Direct Lake on SQL semantic model so queries fail fast instead of silently falling back to slow DirectQuery. Disabling automatic updates in favor of post-ETL explicit `framing` refreshes, running `OPTIMIZE` with `V-Order`, and setting `DirectLakeBehavior = DirectLakeOnly` guarantee predictable in-memory performance. Local study-map skill 3.10 (Configure Direct Lake Framing, Transcoding, V-Order/OPTIMIZE Guardrails, and DirectLakeBehavior Fallback), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: How Direct Lake works (framing, transcoding, V-Order, fallback & DirectLakeBehavior) (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works).

- **A:** Correct. Framing is a fast metadata-only operation updating the Direct Lake model's pointer to the latest Delta transaction log Parquet files and evicting stale resident columns so new ETL rows become visible consistently. In this scenario: Disabling automatic updates in favor of post-ETL explicit `framing` refreshes, running `OPTIMIZE` with `V-Order`, and setting `DirectLakeBehavior = DirectLakeOnly` guarantee predictable in-memory performance.
- **B:** Incorrect for this requirement. Direct Lake on OneLake operates exclusively in DirectLakeOnly mode and never falls back to DirectQuery; exceeding capacity guardrails fails framing/queries until Delta tables or SKU sizing are optimized. Why the keyed choice wins: Disabling automatic updates in favor of post-ETL explicit `framing` refreshes, running `OPTIMIZE` with `V-Order`, and setting `DirectLakeBehavior = DirectLakeOnly` guarantee predictable in-memory performance.
- **C:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Disabling automatic updates in favor of post-ETL explicit `framing` refreshes, running `OPTIMIZE` with `V-Order`, and setting `DirectLakeBehavior = DirectLakeOnly` guarantee predictable in-memory performance.
- **D:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Disabling automatic updates in favor of post-ETL explicit `framing` refreshes, running `OPTIMIZE` with `V-Order`, and setting `DirectLakeBehavior = DirectLakeOnly` guarantee predictable in-memory performance.
- **E:** Correct. Hundreds of tiny streaming Parquet files inflate Delta rowgroup counts past Fabric SKU guardrails and degrade transcoding; OPTIMIZE compacts files into large V-Order-sorted rowgroups optimized for VertiPaq in-memory compression. In this scenario: Disabling automatic updates in favor of post-ETL explicit `framing` refreshes, running `OPTIMIZE` with `V-Order`, and setting `DirectLakeBehavior = DirectLakeOnly` guarantee predictable in-memory performance.
- **F:** Correct. Setting DirectLakeBehavior to DirectLakeOnly (on Direct Lake on SQL models) prevents unexpected DirectQuery fallback spikes on the SQL endpoint when guardrails or SQL views/RLS are encountered. In this scenario: Disabling automatic updates in favor of post-ETL explicit `framing` refreshes, running `OPTIMIZE` with `V-Order`, and setting `DirectLakeBehavior = DirectLakeOnly` guarantee predictable in-memory performance.

### Question 86 — A

Answer: Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop). `Direct Lake on SQL` is restricted to a single Fabric source item and does not support composite models; `Direct Lake on OneLake` supports multi-item Delta tables plus `Import` composite tables. Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery. Local study-map skill 3.11 (Choose Between Direct Lake on OneLake and Direct Lake on SQL Analytics Endpoint (and Migrate via TMDL)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Direct Lake overview: Direct Lake on OneLake vs Direct Lake on SQL analytics endpoint (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview).

- **A:** Correct. Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery. In this scenario: `Direct Lake on SQL` is restricted to a single Fabric source item and does not support composite models; `Direct Lake on OneLake` supports multi-item Delta tables plus `Import` composite tables.
- **B:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: `Direct Lake on SQL` is restricted to a single Fabric source item and does not support composite models; `Direct Lake on OneLake` supports multi-item Delta tables plus `Import` composite tables.
- **C:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: `Direct Lake on SQL` is restricted to a single Fabric source item and does not support composite models; `Direct Lake on OneLake` supports multi-item Delta tables plus `Import` composite tables.
- **D:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Direct Lake on SQL` is restricted to a single Fabric source item and does not support composite models; `Direct Lake on OneLake` supports multi-item Delta tables plus `Import` composite tables.

### Question 87 — C

Answer: Live edit the model in Power BI Desktop and save a Version history point → Script the semantic model in TMDL view → Replace Sql.Database(...) with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...") → Apply TMDL and run framing refresh. Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and running a framing refresh upgrades the model seamlessly. Correct order: take a version history checkpoint while live editing, script the model in TMDL view, swap the shared M expression from Sql.Database to AzureStorage.DataLake OneLake URL, apply changes, and frame. Local study-map skill 3.11 (Choose Between Direct Lake on OneLake and Direct Lake on SQL Analytics Endpoint (and Migrate via TMDL)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Direct Lake overview: Direct Lake on OneLake vs Direct Lake on SQL analytics endpoint (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview).

- **A:** Incorrect for this requirement. Incorrect: deleting the semantic model breaks downstream thin reports and lineage, and granting Workspace Admin violates security. Why the keyed choice wins: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and running a framing refresh upgrades the model seamlessly.
- **B:** Incorrect for this requirement. Incorrect: Direct Lake models are live-edited in workspaces (not offline Personal Workspace Import files), and OleDb breaks OneLake Direct Lake connectivity. Why the keyed choice wins: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and running a framing refresh upgrades the model seamlessly.
- **C:** Correct. Correct order: take a version history checkpoint while live editing, script the model in TMDL view, swap the shared M expression from Sql.Database to AzureStorage.DataLake OneLake URL, apply changes, and frame. In this scenario: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and running a framing refresh upgrades the model seamlessly.
- **D:** Incorrect for this requirement. Incorrect: Direct Lake on OneLake does not support non-materialized SQL views, DirectQuery fallback, or gateways. Why the keyed choice wins: Saving a Version history checkpoint while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and running a framing refresh upgrades the model seamlessly.

### Question 88 — B

Answer: Create case-sensitive DateTime parameters RangeStart and RangeEnd → Apply foldable half-open filter (>= RangeStart and < RangeEnd) → Configure table Incremental refresh policy → Publish to workspace and run initial refresh to generate partitions. Creating exact `DateTime` `RangeStart`/`RangeEnd` parameters, filtering `>= RangeStart and < RangeEnd` with query folding intact, configuring the table's incremental policy, and publishing for initial partition creation implements it cleanly. Correct order: define DateTime RangeStart/RangeEnd parameters, apply >= RangeStart and < RangeEnd preserving query folding, configure table incremental policy, and publish so Fabric generates historical and incremental partitions. Local study-map skill 3.12 (Implement Incremental Refresh and Hybrid Real-Time Partitions (RangeStart/RangeEnd, Detect Data Changes)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Configure incremental refresh and real-time data for Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-overview).

- **A:** Incorrect for this requirement. Incorrect: Detect data changes requires an audit/update timestamp column distinct from the date column used to partition RangeStart/RangeEnd. Why the keyed choice wins: Creating exact `DateTime` `RangeStart`/`RangeEnd` parameters, filtering `>= RangeStart and < RangeEnd` with query folding intact, configuring the table's incremental policy, and publishing for initial partition creation implements it cleanly.
- **B:** Correct. Correct order: define DateTime RangeStart/RangeEnd parameters, apply >= RangeStart and < RangeEnd preserving query folding, configure table incremental policy, and publish so Fabric generates historical and incremental partitions. In this scenario: Creating exact `DateTime` `RangeStart`/`RangeEnd` parameters, filtering `>= RangeStart and < RangeEnd` with query folding intact, configuring the table's incremental policy, and publishing for initial partition creation implements it cleanly.
- **C:** Incorrect for this requirement. Incorrect: importing 2 billion rows locally crashes Desktop before partitioning exists, RangeStart belongs in Power Query M, and Incremental Refresh partitions apply to Import/Hybrid tables rather than Direct Lake. Why the keyed choice wins: Creating exact `DateTime` `RangeStart`/`RangeEnd` parameters, filtering `>= RangeStart and < RangeEnd` with query folding intact, configuring the table's incremental policy, and publishing for initial partition creation implements it cleanly.
- **D:** Incorrect for this requirement. Incorrect: parameter names/types must be exact DateTime RangeStart and RangeEnd, breaking query folding pulls the entire table on every refresh, and <= on both bounds double-counts midnight rows. Why the keyed choice wins: Creating exact `DateTime` `RangeStart`/`RangeEnd` parameters, filtering `>= RangeStart and < RangeEnd` with query folding intact, configuring the table's incremental policy, and publishing for initial partition creation implements it cleanly.

### Question 89 — A

Answer: Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog. Fabric Database Mirroring continuously syncs initial snapshots and ongoing CDC changes from Azure SQL Database and Snowflake directly into OneLake Delta tables. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Correct. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. In this scenario: Fabric Database Mirroring continuously syncs initial snapshots and ongoing CDC changes from Azure SQL Database and Snowflake directly into OneLake Delta tables.
- **B:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Fabric Database Mirroring continuously syncs initial snapshots and ongoing CDC changes from Azure SQL Database and Snowflake directly into OneLake Delta tables.
- **C:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: Fabric Database Mirroring continuously syncs initial snapshots and ongoing CDC changes from Azure SQL Database and Snowflake directly into OneLake Delta tables.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Fabric Database Mirroring continuously syncs initial snapshots and ongoing CDC changes from Azure SQL Database and Snowflake directly into OneLake Delta tables.

### Question 90 — A

Answer: Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet. Deploying a Fabric Virtual Network (VNet) data gateway into a delegated subnet of the bank's Azure VNet provides managed private connectivity. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. Local study-map skill 2.1 (Create Data Connections (Shareable Cloud Connections, On-Premises Gateways, and VNet Data Gateways)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data source management, cloud connections, and VNet/on-premises gateways in Fabric (https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management).

- **A:** Correct. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. In this scenario: Deploying a Fabric Virtual Network (VNet) data gateway into a delegated subnet of the bank's Azure VNet provides managed private connectivity.
- **B:** Incorrect for this requirement. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. Why the keyed choice wins: Deploying a Fabric Virtual Network (VNet) data gateway into a delegated subnet of the bank's Azure VNet provides managed private connectivity.
- **C:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Deploying a Fabric Virtual Network (VNet) data gateway into a delegated subnet of the bank's Azure VNet provides managed private connectivity.
- **D:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Deploying a Fabric Virtual Network (VNet) data gateway into a delegated subnet of the bank's Azure VNet provides managed private connectivity.

### Question 91 — D

Answer: Query across a Warehouse and a Lakehouse SQL analytics endpoint in the same workspace using three-part T-SQL naming (SalesLakehouse.dbo.RawOrders). Three-part T-SQL naming (`KycLakehouse.dbo.CustomerKYC`) executes zero-copy cross-database joins across Warehouses and Lakehouse SQL analytics endpoints within the same workspace. Fabric Warehouse and SQL analytics endpoints inside the same workspace share a unified SQL engine namespace, enabling zero-copy cross-database T-SQL joins via DatabaseName.SchemaName.ObjectName. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Incorrect for this requirement. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. Why the keyed choice wins: Three-part T-SQL naming (`KycLakehouse.dbo.CustomerKYC`) executes zero-copy cross-database joins across Warehouses and Lakehouse SQL analytics endpoints within the same workspace.
- **B:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: Three-part T-SQL naming (`KycLakehouse.dbo.CustomerKYC`) executes zero-copy cross-database joins across Warehouses and Lakehouse SQL analytics endpoints within the same workspace.
- **C:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Three-part T-SQL naming (`KycLakehouse.dbo.CustomerKYC`) executes zero-copy cross-database joins across Warehouses and Lakehouse SQL analytics endpoints within the same workspace.
- **D:** Correct. Fabric Warehouse and SQL analytics endpoints inside the same workspace share a unified SQL engine namespace, enabling zero-copy cross-database T-SQL joins via DatabaseName.SchemaName.ObjectName. In this scenario: Three-part T-SQL naming (`KycLakehouse.dbo.CustomerKYC`) executes zero-copy cross-database joins across Warehouses and Lakehouse SQL analytics endpoints within the same workspace.

### Question 92 — A

Answer: | make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion. `| make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion` generates regular zero-filled time-series arrays for anomaly scoring. make-series builds regular gap-filled time-series arrays (filling empty 1-minute buckets with default = 0) required for KQL anomaly detection and trend functions; summarize by bin() omits empty buckets. Local study-map skill 2.17 (Select, Filter, and Aggregate Data Using KQL (summarize, bin, arg_max, percentile, parse_json, mv-expand)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query data in a KQL queryset in Microsoft Fabric Real-Time Intelligence (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/kql-queryset).

- **A:** Correct. make-series builds regular gap-filled time-series arrays (filling empty 1-minute buckets with default = 0) required for KQL anomaly detection and trend functions; summarize by bin() omits empty buckets. In this scenario: `| make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion` generates regular zero-filled time-series arrays for anomaly scoring.
- **B:** Incorrect for this requirement. In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key. Why the keyed choice wins: `| make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion` generates regular zero-filled time-series arrays for anomaly scoring.
- **C:** Incorrect for this requirement. mv-expand unpacks a dynamic JSON array into one output row per array element while preserving parent event columns. Why the keyed choice wins: `| make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion` generates regular zero-filled time-series arrays for anomaly scoring.
- **D:** Incorrect for this requirement. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Why the keyed choice wins: `| make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion` generates regular zero-filled time-series arrays for anomaly scoring.

### Question 93 — D

Answer: | summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m). `| summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)` computes streaming p99 latency across fixed 5-minute windows. percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse. Local study-map skill 2.17 (Select, Filter, and Aggregate Data Using KQL (summarize, bin, arg_max, percentile, parse_json, mv-expand)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query data in a KQL queryset in Microsoft Fabric Real-Time Intelligence (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/kql-queryset).

- **A:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `| summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)` computes streaming p99 latency across fixed 5-minute windows.
- **B:** Incorrect for this requirement. make-series builds regular gap-filled time-series arrays (filling empty 1-minute buckets with default = 0) required for KQL anomaly detection and trend functions; summarize by bin() omits empty buckets. Why the keyed choice wins: `| summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)` computes streaming p99 latency across fixed 5-minute windows.
- **C:** Incorrect for this requirement. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Why the keyed choice wins: `| summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)` computes streaming p99 latency across fixed 5-minute windows.
- **D:** Correct. percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse. In this scenario: `| summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)` computes streaming p99 latency across fixed 5-minute windows.

### Question 94 — C

Answer: Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time. Removing the unreferenced `TransactionGUID` column and splitting `EventTimestamp` into separate low-cardinality `EventDate` and `EventTime` columns drastically shrinks column dictionaries. Columnar memory in VertiPaq and Direct Lake transcoding scales primarily with column cardinality rather than row count; dropping unused GUIDs or splitting millisecond timestamps into separate Date and Time columns cuts memory dramatically. Local study-map skill 3.9 (Improve DAX and Model Performance Using DAX Studio Server Timings (FE vs SE) and VertiPaq Cardinality Reduction), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Optimization guide for Power BI — DAX Formula Engine vs Storage Engine & VertiPaq (https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization).

- **A:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Removing the unreferenced `TransactionGUID` column and splitting `EventTimestamp` into separate low-cardinality `EventDate` and `EventTime` columns drastically shrinks column dictionaries.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Removing the unreferenced `TransactionGUID` column and splitting `EventTimestamp` into separate low-cardinality `EventDate` and `EventTime` columns drastically shrinks column dictionaries.
- **C:** Correct. Columnar memory in VertiPaq and Direct Lake transcoding scales primarily with column cardinality rather than row count; dropping unused GUIDs or splitting millisecond timestamps into separate Date and Time columns cuts memory dramatically. In this scenario: Removing the unreferenced `TransactionGUID` column and splitting `EventTimestamp` into separate low-cardinality `EventDate` and `EventTime` columns drastically shrinks column dictionaries.
- **D:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Removing the unreferenced `TransactionGUID` column and splitting `EventTimestamp` into separate low-cardinality `EventDate` and `EventTime` columns drastically shrinks column dictionaries.

### Question 95 — B

Answer: Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat). Enabling `Large semantic model storage format` lifts the default size ceiling up to the capacity SKU's max memory per model and accelerates XMLA metadata writes. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Local study-map skill 3.6 (Identify Use Cases for and Configure Large Semantic Model Storage Format), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Large semantic models in Microsoft Fabric & Power BI Premium (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-large-models).

- **A:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Enabling `Large semantic model storage format` lifts the default size ceiling up to the capacity SKU's max memory per model and accelerates XMLA metadata writes.
- **B:** Correct. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. In this scenario: Enabling `Large semantic model storage format` lifts the default size ceiling up to the capacity SKU's max memory per model and accelerates XMLA metadata writes.
- **C:** Incorrect for this requirement. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Why the keyed choice wins: Enabling `Large semantic model storage format` lifts the default size ceiling up to the capacity SKU's max memory per model and accelerates XMLA metadata writes.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Enabling `Large semantic model storage format` lifts the default size ceiling up to the capacity SKU's max memory per model and accelerates XMLA metadata writes.

### Question 96 — B

Answer: Verify XMLA Endpoint = Read Write on target capacity → Connect ALM Toolkit to Dev source and Prod XMLA target → Compare schemas while hiding unchanged partitions and keeping Prod data sources → Validate and deploy metadata-only TMSL changes. Verifying `XMLA Endpoint = Read Write`, connecting ALM Toolkit to Dev and Prod, hiding unchanged partitions while retaining Prod data sources, and deploying metadata-only TMSL changes avoids full reprocessing. Correct order: confirm Read Write XMLA capacity setting, compare Dev vs Prod models, preserve Prod partition state and data-source bindings, and push metadata-only measure/relationship diffs. Local study-map skill 1.10 (Deploy and Manage Semantic Models Using the XMLA Endpoint (Read-Write, TMSL, Tabular Editor, ALM Toolkit)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model connectivity and management with the XMLA endpoint (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools).

- **A:** Incorrect for this requirement. Incorrect: Read Only XMLA rejects TMSL model deployments, and Capacity Admin rights violate least privilege. Why the keyed choice wins: Verifying `XMLA Endpoint = Read Write`, connecting ALM Toolkit to Dev and Prod, hiding unchanged partitions while retaining Prod data sources, and deploying metadata-only TMSL changes avoids full reprocessing.
- **B:** Correct. Correct order: confirm Read Write XMLA capacity setting, compare Dev vs Prod models, preserve Prod partition state and data-source bindings, and push metadata-only measure/relationship diffs. In this scenario: Verifying `XMLA Endpoint = Read Write`, connecting ALM Toolkit to Dev and Prod, hiding unchanged partitions while retaining Prod data sources, and deploying metadata-only TMSL changes avoids full reprocessing.
- **C:** Incorrect for this requirement. Incorrect: XMLA Off blocks external deployment, and overwriting Production with an unpartitioned file destroys incremental partitions and causes prolonged outage. Why the keyed choice wins: Verifying `XMLA Endpoint = Read Write`, connecting ALM Toolkit to Dev and Prod, hiding unchanged partitions while retaining Prod data sources, and deploying metadata-only TMSL changes avoids full reprocessing.
- **D:** Incorrect for this requirement. Incorrect: DAX Studio is a query/profiling tool (not a model-deployment tool), and unversioned Production hotfixes cause immediate drift on next deployment. Why the keyed choice wins: Verifying `XMLA Endpoint = Read Write`, connecting ALM Toolkit to Dev and Prod, hiding unchanged partitions while retaining Prod data sources, and deploying metadata-only TMSL changes avoids full reprocessing.

### Question 97 — D, E

Answers: Enable XMLA Endpoint = Read Write in Fabric Capacity workload settings and connect to powerbi://api.powerbi.com/v1.0/myorg/<WorkspaceName>; {"refresh": {"type": "dataOnly", "objects": [{"database": "WealthModel", "table": "FactPositions", "partition": "2026M10"}]}}. Setting `XMLA Endpoint = Read Write` on the F128 capacity and sending `{"refresh": {"type": "dataOnly", "objects": [{"database": "WealthModel", "table": "FactPositions", "partition": "2026M10"}]}}` refreshes only that partition. Local study-map skill 1.10 (Deploy and Manage Semantic Models Using the XMLA Endpoint (Read-Write, TMSL, Tabular Editor, ALM Toolkit)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model connectivity and management with the XMLA endpoint (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools).

- **A:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Setting `XMLA Endpoint = Read Write` on the F128 capacity and sending `{"refresh": {"type": "dataOnly", "objects": [{"database": "WealthModel", "table": "FactPositions", "partition": "2026M10"}]}}` refreshes only that partition.
- **B:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: Setting `XMLA Endpoint = Read Write` on the F128 capacity and sending `{"refresh": {"type": "dataOnly", "objects": [{"database": "WealthModel", "table": "FactPositions", "partition": "2026M10"}]}}` refreshes only that partition.
- **C:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Setting `XMLA Endpoint = Read Write` on the F128 capacity and sending `{"refresh": {"type": "dataOnly", "objects": [{"database": "WealthModel", "table": "FactPositions", "partition": "2026M10"}]}}` refreshes only that partition.
- **D:** Correct. A TMSL refresh command with type = "dataOnly" scoped to a single partition reloads raw partition data over XMLA without rebuilding global relationships or calculated tables. In this scenario: Setting `XMLA Endpoint = Read Write` on the F128 capacity and sending `{"refresh": {"type": "dataOnly", "objects": [{"database": "WealthModel", "table": "FactPositions", "partition": "2026M10"}]}}` refreshes only that partition.
- **E:** Correct. External ALM tools (Tabular Editor, SSMS, ALM Toolkit, SqlPackage/PowerShell Invoke-ASCmd) require workspace Fabric/Premium capacity with XMLA Endpoint set to Read Write to deploy or modify semantic models. In this scenario: Setting `XMLA Endpoint = Read Write` on the F128 capacity and sending `{"refresh": {"type": "dataOnly", "objects": [{"database": "WealthModel", "table": "FactPositions", "partition": "2026M10"}]}}` refreshes only that partition.

### Question 98 — C

Answer: CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey])). `CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))` activates the inactive settlement-date relationship strictly within the measure. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. Why the keyed choice wins: `CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))` activates the inactive settlement-date relationship strictly within the measure.
- **B:** Incorrect for this requirement. CROSSFILTER(..., BOTH) enables bidirectional filter propagation across a bridge table only inside the specific measure rather than globally across the model. Why the keyed choice wins: `CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))` activates the inactive settlement-date relationship strictly within the measure.
- **C:** Correct. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. In this scenario: `CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))` activates the inactive settlement-date relationship strictly within the measure.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: `CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))` activates the inactive settlement-date relationship strictly within the measure.

### Question 99 — B

Answer: Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table. Using the `SUMX` iterator multiplies each trade's `LocalNotional * DailySpotRate` row-by-row in memory before summing, avoiding non-additive `SUM * AVERAGE` errors and physical column bloat. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Using the `SUMX` iterator multiplies each trade's `LocalNotional * DailySpotRate` row-by-row in memory before summing, avoiding non-additive `SUM * AVERAGE` errors and physical column bloat.
- **B:** Correct. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. In this scenario: Using the `SUMX` iterator multiplies each trade's `LocalNotional * DailySpotRate` row-by-row in memory before summing, avoiding non-additive `SUM * AVERAGE` errors and physical column bloat.
- **C:** Incorrect for this requirement. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Why the keyed choice wins: Using the `SUMX` iterator multiplies each trade's `LocalNotional * DailySpotRate` row-by-row in memory before summing, avoiding non-additive `SUM * AVERAGE` errors and physical column bloat.
- **D:** Incorrect for this requirement. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. Why the keyed choice wins: Using the `SUMX` iterator multiplies each trade's `LocalNotional * DailySpotRate` row-by-row in memory before summing, avoiding non-additive `SUM * AVERAGE` errors and physical column bloat.

### Question 100 — B

Answer: Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer. Creating a `Field Parameter` bound to the matrix Rows well and a report slicer switches grouping dimensions dynamically without maintaining duplicate visuals. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. A single Calculation Group applies reusable logic (YTD, PY, YoY%, Moving Avg) across dozens of base measures via SELECTEDMEASURE(), eliminating measure explosion (`50 base * 6 time calcs = 300 measures`). Why the keyed choice wins: Creating a `Field Parameter` bound to the matrix Rows well and a report slicer switches grouping dimensions dynamically without maintaining duplicate visuals.
- **B:** Correct. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. In this scenario: Creating a `Field Parameter` bound to the matrix Rows well and a report slicer switches grouping dimensions dynamically without maintaining duplicate visuals.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Creating a `Field Parameter` bound to the matrix Rows well and a report slicer switches grouping dimensions dynamically without maintaining duplicate visuals.
- **D:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Creating a `Field Parameter` bound to the matrix Rows well and a report slicer switches grouping dimensions dynamically without maintaining duplicate visuals.
