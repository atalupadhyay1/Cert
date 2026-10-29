# Microsoft Exam DP-600: Implementing Analytics Solutions Using Microsoft Fabric — Full-Length Mock Exam 2

Exam DP-600 (Healthcare Claims Warehousing, Clinical IoT Eventhouses, and HIPAA Governance) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint & Credential Notice:** Aligned to the official **October 19, 2026** DP-600 study guide (`Microsoft Certified: Fabric Analytics Engineer Associate`). Associate-level certification with **no prerequisite exam required**, free online annual renewal on Microsoft Learn, split-screen `learn.microsoft.com` access during non-lab exam sections, and hands-on coverage across **SQL**, **KQL**, **DAX**, **PySpark**, **Power Query M**, **TMDL**, and **TMSL**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` SQL/KQL/DAX/PySpark/M/TMDL/TMSL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Microsoft Fabric case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area SQL/KQL/DAX/TMDL dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn Fabric and Power BI documentation — never recalled live items or copied Microsoft sample case studies.

## Questions

### 1. Proposed solution: You add 60 hospital department heads directly to the `Clinical-BI-Prod` workspace as Contributors so they can view published clinical dashboards filtered by semantic-model RLS. Will RLS restrict them, and which role is required?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Viewer role
- B. Assign the Workspace Member role
- C. Assign the Workspace Contributor role
- D. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows

### 2. Which minimum Fabric workspace role is required to delete an obsolete `Sandbox-Trials-2025` workspace or link a workspace for the first time to an Azure DevOps Git repository?

Domain: Maintain a data analytics solution

- A. Assign the Workspace Viewer role
- B. Assign the Workspace Admin role
- C. Assign the Workspace Member role
- D. Assign the Workspace Contributor role

### 3. A contract biostatistics team needs to author Dataflows and Lakehouse notebooks in `Oncology-Dev` without sharing items externally or modifying workspace security, and access must revoke automatically when contractors leave their Entra group. Which two actions apply? Select two.

Domain: Maintain a data analytics solution

- A. Assign permissions to Microsoft Entra security groups rather than individual users
- B. Assign the Workspace Viewer role
- C. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows
- D. Assign the Workspace Contributor role
- E. Assign the Workspace Admin role

### 4. A Direct Lake on SQL semantic model serves clinical analysts who already have T-SQL `SELECT` permissions and per-hospital SQL RLS predicates configured on `HospitalWarehouse`. Which model connection setting evaluates each analyst's own Entra identity against those SQL rules?

Domain: Maintain a data analytics solution

- A. Bind the Direct Lake semantic model to a cloud connection with a fixed identity and disable SSO
- B. Enable single sign-on (SSO) on the Direct Lake semantic model connection
- C. Share the Lakehouse with ReadAll (Read all Apache Spark data) permission
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 5. A medical imaging ML engineer runs PySpark jobs in `RadiologyML` workspace reading raw DICOM files and Delta tables from `CoreImagingLakehouse` (where OneLake granular security is off). Which item-level permission on `CoreImagingLakehouse` enables Spark ABFS reads without workspace membership?

Domain: Maintain a data analytics solution

- A. Share the item with ReadData (Read all SQL endpoint data) permission
- B. Share the Lakehouse with ReadAll (Read all Apache Spark data) permission
- C. Grant Build permission on the shared semantic model
- D. Share the item with Read permission only (no ReadData or ReadAll)

### 6. Clinical data architects are securing `PatientRegistryLakehouse` using OneLake security roles consumed by downstream research workspaces via OneLake shortcuts. Which four-step sequence enforces least privilege?

Domain: Maintain a data analytics solution

- A. Set SQL analytics endpoint to Delegated mode with SQL DENY rules → Remove Workspace Viewer assignments → Enable OneLake security afterward → Export binary .pbix copies
- B. Assign consumers the Workspace Contributor role → Enable OneLake security with a Deny role → Keep SQL analytics endpoint in Owner fixed identity mode → Create downstream shortcuts
- C. Enable OneLake security and define Read Grant roles → Assign consumers Workspace Viewer and OneLake security roles → Set SQL analytics endpoint to User's identity mode → Expose downstream shortcuts in User's identity mode
- D. Create downstream shortcuts first → Assign consumers Workspace Member rights → Attach RLS predicates to a ReadWrite OneLake role → Enable SSO on an On-premises gateway

### 7. You implement dynamic clinic-level RLS on `OutpatientModel` (`[ClinicLeadUPN] = ____`) and must verify before go-live that `dr.patel@aethercare.org` sees only Clinic 14 rows and does not accidentally hold RLS-bypassing workspace permissions. Which two steps should you perform? Select two.

Domain: Maintain a data analytics solution

- A. Filter the RLS table using USERNAME() = [DomainLogin] without testing in the Fabric portal
- B. Assign report consumers to the Workspace Contributor role and rely on Semantic Model DAX RLS to filter their rows
- C. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- D. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- E. Create a dynamic DAX RLS role filtering a security mapping table with [UserEmail] = USERPRINCIPALNAME()

### 8. Compliance auditors find 40 newly published ad-hoc clinical semantic models in Fabric carrying no sensitivity classification at all. Which Microsoft Purview configuration prevents creators from saving unlabeled assets?

Domain: Maintain a data analytics solution

- A. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- B. Enable a mandatory label policy and default sensitivity label in Microsoft Purview compliance portal for Fabric users
- C. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- D. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal

### 9. Dozens of hospital workspaces build separate copies of ICD-10 and NPI provider reference tables. Which Fabric endorsement badge designates the single authoritative `GoldProviderLakehouse` as the organization's core reference source in OneLake catalog?

Domain: Maintain a data analytics solution

- A. Configure Certified endorsement with the Master data label on authoritative core tables or semantic models
- B. Mark the item as Promoted in item settings
- C. Use a Purview sensitivity label configured with file encryption so exported .pbix, Excel, PDF, and PowerPoint files stay protected outside Fabric
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 10. After a pull request adding two clinical notebooks merges into the `main` branch in GitHub, `Pharma-Dev` workspace still shows an incoming changes badge and runs yesterday's notebook version. Why, and what must you do?

Domain: Maintain a data analytics solution

- A. Commit workspace changes to Git from the Source control pane, merge via pull request, then select Update all in the target workspace
- B. Use Undo in the Fabric Workspace Source control pane to discard uncommitted workspace edits back to the last synced commit
- C. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- D. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline

### 11. Which four-step Git and Deployment Pipeline workflow safely delivers a `.pbip` clinical measure enhancement from a developer's feature branch to `Clinical-Prod`?

Domain: Maintain a data analytics solution

- A. Connect Production directly to a feature branch → Edit semantic models live in Prod → Force-push binary .pbix files including cache.abf to main → Deploy backward to Development
- B. Branch out to personal My Workspace → Run Undo to push changes to GitHub → Delete .platform metadata files → Copy visuals manually into Production
- C. Edit items directly on main without branching → Merge an empty PR → Promote Dev to Test before running Update from Git → Configure Git integration last
- D. Connect shared Dev workspace to main → Branch out to an isolated developer workspace and commit .pbip/Notebook edits → Merge pull request into main in Git → Run Update all in Dev and promote via Deployment Pipeline

### 12. When initializing a Git repository for a `.pbip` clinical model containing local PHI test rows, which file pattern (`**/____`) must remain in `.gitignore` so local VertiPaq caches are never pushed to GitHub?

Domain: Maintain a data analytics solution

- A. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- D. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition

### 13. Two clinical BI developers need to edit different DAX measures and report pages concurrently, review text diffs in Azure DevOps pull requests, and test changes in isolated Fabric workspaces before merging. Which two practices enable this? Select two.

Domain: Maintain a data analytics solution

- A. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- B. Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch
- C. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- D. Configure DirectQuery storage mode
- E. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches

### 14. A hospital already runs live reports in `Clinical-Prod` but has no `Dev` or `Test` workspaces yet. After creating a Deployment Pipeline and assigning `Clinical-Prod` to the `Production` stage, how should you initialize empty `Test` and `Dev` workspaces with matching lineage?

Domain: Maintain a data analytics solution

- A. Perform a selective deployment selecting the modified item together with Select related to include required upstream dependencies
- B. Configure Deployment pipeline data source and parameter rules on the Test and Production stages
- C. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline
- D. Use Undo in the Fabric Workspace Source control pane to discard uncommitted workspace edits back to the last synced commit

### 15. Proposed solution: Each time you deploy `ClaimsDataflow` and `ClaimsModel` from `Test` to `Production`, an engineer manually edits the Production semantic model connection string back to `prod-claims-wh`, causing a 10-minute broken window. What eliminates manual post-deploy rebinding?

Domain: Maintain a data analytics solution

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline
- C. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- D. Configure Deployment pipeline data source and parameter rules on the Test and Production stages

### 16. A clinical Data Factory pipeline uses dynamic Lakehouse IDs and FHIR storage URLs that differ across `Dev`, `Test`, and `Production` stages. Which workspace item stores stage-aware variables natively integrated with Deployment Pipelines?

Domain: Maintain a data analytics solution

- A. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN
- B. Mark the item as Promoted in item settings
- C. Use a Fabric Variable library (or autobinding across paired workspace items) to parameterize stage-specific environment references
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 17. You switch a healthcare workspace from `List` view to `Lineage` view. What visual diagnostic information does `Lineage` view immediately expose across Dataflows, Lakehouses, Semantic Models, and Reports?

Domain: Maintain a data analytics solution

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results
- C. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- D. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages

### 18. You need to deploy urgent DRG measure updates from `Clinical-Dev` to the 35 GB `Clinical-Prod` model during hospital daytime shifts without wiping 84 processed historical partitions. Which four-step XMLA workflow applies?

Domain: Maintain a data analytics solution

- A. Set XMLA Endpoint = Off → Overwrite Production with an empty unpartitioned .pbix file → Purge all 5 years of historical incremental partitions → Re-import 3 billion rows during peak business hours
- B. Open Production in DAX Studio → Edit measures manually in Production without committing to Git → Copy cache.abf into GitHub → Disable sensitivity labels
- C. Leave XMLA Endpoint = Read Only → Execute T-SQL DELETE across Warehouse schemas → Grant all report viewers Capacity Admin rights → Skip downstream impact analysis
- D. Verify XMLA Endpoint = Read Write on target capacity → Connect ALM Toolkit to Dev source and Prod XMLA target → Compare schemas while hiding unchanged partitions and keeping Prod data sources → Validate and deploy metadata-only TMSL changes

### 19. Your clinical BI team uses ALM Toolkit to push five validated ICD-10 DAX measures from `Dev` to `Prod` while keeping `Prod`'s 84 historical monthly partitions untouched. Which two requirements apply? Select two.

Domain: Maintain a data analytics solution

- A. Use ALM Toolkit over the XMLA endpoint to compare Dev and Prod semantic models and deploy only new measures without reprocessing unchanged partitions
- B. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- C. Enable XMLA Endpoint = Read Write in Fabric Capacity workload settings and connect to powerbi://api.powerbi.com/v1.0/myorg/<WorkspaceName>
- D. Assign the Workspace Viewer role
- E. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches

### 20. You build a standardized Hospital Quality Scorecard report with a `HospitalFacilityCode` Power Query parameter and need to distribute it to 45 independent affiliate clinics with zero PHI rows embedded inside the file. Which file format should you export?

Domain: Maintain a data analytics solution

- A. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- D. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows

### 21. Nursing, Pharmacy, and Emergency Operations teams all need custom report layouts built over the exact same Certified `ClinicalEncounters` semantic model without duplicating data in capacity RAM. How should they author reports?

Domain: Maintain a data analytics solution

- A. Configure Import storage mode
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Publish a single certified core semantic model in a data workspace and build thin live-connected Power BI reports in departmental workspaces

### 22. A hospital's legacy HL7 pathology database runs on physical SQL Server 2019 hosts inside an on-premises hospital data center with no ExpressRoute or Azure VNet peering. Which gateway architecture allows scheduled Fabric pipeline and Dataflow Gen2 refreshes with high availability?

Domain: Prepare data

- A. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- B. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- C. Create a Shareable cloud connection in Manage connections and gateways with Service Principal or Workspace Identity authentication
- D. Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet

### 23. Proposed solution: To read an Azure Storage account locked down to a private endpoint in `vnet-clinical-eastus`, you spin up two IaaS Windows Server VMs and manually patch an On-premises data gateway every month. Which managed Fabric feature eliminates VM maintenance?

Domain: Prepare data

- A. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- B. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- C. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- D. Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet

### 24. Clinical researchers want to search across 30 workspaces for trusted oncology datasets while the Chief Medical Information Officer audits sensitivity-label coverage across all owned items. Which two Fabric governance features address both personas? Select two.

Domain: Prepare data

- A. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal
- B. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- E. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table

### 25. A clinical scheduling platform runs on Azure SQL Database (`Hyperscale`). You need continuous, near-real-time Delta Parquet replicas of 95 scheduling tables in OneLake without authoring Spark CDC merge notebooks or watermark pipelines. What should you configure?

Domain: Prepare data

- A. Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging

### 26. Genomics partner labs publish de-identified Parquet cohorts in Google Cloud Storage (GCS). How can your Fabric Lakehouse query those cohorts in place and reduce repeated cross-cloud egress fees on hot reference files?

Domain: Prepare data

- A. Choose a SQL database in Microsoft Fabric
- B. Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching
- C. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- D. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake

### 27. Intensive-care bedside monitors publish 120,000 vital-sign JSON messages per minute to Azure IoT Hub. Which Fabric item provides no-code live tumbling-window filtering and simultaneous routing to both an Eventhouse and a Lakehouse?

Domain: Prepare data

- A. Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table
- B. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- C. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- D. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode

### 28. Match the three clinical ingestion workloads to the optimal Fabric capabilities: (1) nightly 2 TB raw DICOM metadata Parquet copy from ADLS, (2) visual M transformations merging 15 SharePoint clinical trial trackers into a Warehouse, and (3) continuous HL7 Kafka stream routing. Which three tools fit? Select three.

Domain: Prepare data

- A. Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table
- B. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- C. Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations
- D. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- E. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- F. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging

### 29. Telemetry engineers retain 18 billion high-frequency ECG waveform and infusion-pump JSON events requiring sub-second time-series anomaly detection and full-text log search via KQL. Which Fabric data store is purpose-built for this workload?

Domain: Prepare data

- A. Choose a Fabric Lakehouse
- B. Choose a Fabric Eventhouse (KQL database)
- C. Choose a SQL database in Microsoft Fabric
- D. Choose a Fabric Data Warehouse

### 30. Proposed solution: An actuarial team selects a Lakehouse and attempts to run multi-table `BEGIN TRAN; UPDATE dbo.Claims ...; DELETE FROM dbo.ClaimHolds ...; COMMIT;` scripts through the Lakehouse SQL analytics endpoint. Why does this fail, and which store should they choose?

Domain: Prepare data

- A. Configure Import storage mode
- B. Choose a Fabric Data Warehouse
- C. Choose a Fabric Eventhouse (KQL database)
- D. Choose a Fabric Lakehouse

### 31. A healthcare payer separates data engineering (PySpark processing of unstructured PDF prior-authorization attachments in `Files/` plus Silver Delta tables) from finance reporting (stored-procedure T-SQL star schemas with native SQL CLS). Which two Fabric stores complement each other across OneLake? Select two.

Domain: Prepare data

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Point Direct Lake on SQL directly at an Eventhouse KQL database without enabling OneLake availability
- C. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- D. Choose a Fabric Lakehouse
- E. Choose a Fabric Data Warehouse

### 32. You enable `____` (`OneLake availability`) on the `InfusionTelemetry` KQL database inside an Eventhouse. What immediate architectural capability does this unlock for Spark notebooks and Direct Lake on OneLake semantic models?

Domain: Prepare data

- A. Point Direct Lake on SQL directly at an Eventhouse KQL database without enabling OneLake availability
- B. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network
- C. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- D. Enable OneLake availability on the Eventhouse KQL database (or specific KQL table) and create an internal OneLake shortcut in the Lakehouse

### 33. Which four-step workflow integrates real-time emergency-room wait-time events from an Eventhouse into a Lakehouse-joined Direct Lake on OneLake semantic model?

Domain: Prepare data

- A. Export KQL query results manually to CSV every hour → Email CSVs to analysts → Import into binary .pbix files → Publish to My Workspace
- B. Ingest streaming telemetry into an Eventhouse KQL database → Enable OneLake availability on the KQL database or table → Create an internal OneLake shortcut in the Lakehouse → Add the table to a Direct Lake on OneLake semantic model
- C. Create an Amazon S3 external shortcut to the KQL URI before enabling OneLake availability → Set storage mode to Dual only → Enable Auto date/time → Run XMLA clearValues
- D. Create a Direct Lake on SQL model directly over the KQL queryset → Disable OneLake availability → Configure an On-premises data gateway → Run T-SQL MERGE on the KQL database

### 34. In `ClaimsWarehouse`, you encapsulate nightly DRG grouping rules inside `CREATE PROCEDURE elt.usp_RefreshFactAdmissions @BatchId INT AS BEGIN ... END;`. How should a Fabric Data Factory pipeline execute this logic after Copy activities finish?

Domain: Prepare data

- A. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- B. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- C. Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic
- D. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages

### 35. An analytics engineer creates a complex 5-table clinical join as a non-materialized SQL view in a Lakehouse SQL analytics endpoint and notices Direct Lake on SQL falls back to DirectQuery on every visual. How do you preserve Direct Lake in-memory performance?

Domain: Prepare data

- A. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- B. Use a Lakehouse Materialized Lake View (or persisted Gold Delta table) instead of a non-materialized SQL analytics endpoint view for Direct Lake on OneLake
- C. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- D. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes

### 36. You expose `vw_DeidentifiedEncounters` in `ClaimsWarehouse` (`GRANT SELECT ON reporting.vw_DeidentifiedEncounters TO [ResearchAnalysts]`) while ensuring `[ResearchAnalysts]` cannot query the underlying `raw.PatientEncounters` table (`____ SELECT ON OBJECT::raw.PatientEncounters`). Which SQL security pattern applies?

Domain: Prepare data

- A. Use T-SQL GRANT/DENY SELECT on specific Warehouse schemas, tables, or views
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Mark the item as Promoted in item settings
- D. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS

### 37. Electronic health record merges combine `Cerner` alphanumeric `PatientId` strings and `Epic` GUID `PatientId` strings into `Gold.DimPatient`. Why should you add a `BIGINT` / `INT` `PatientKey` surrogate column instead of joining `FactEncounters` on composite `(SourceEHR, PatientGUID)` strings?

Domain: Prepare data

- A. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- B. CAST(RawReading AS FLOAT)
- C. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- D. Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions

### 38. Hospital epidemiology dashboards filter `AdmissionDate`, `DischargeDate`, and `LabCollectionDate` by flu-season week numbers and federal holiday indicators. How should you enrich the Gold Warehouse?

Domain: Prepare data

- A. Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet
- B. Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL

### 39. You are preparing Silver clinical trial lab tables for a Direct Lake model: engineers need derived `BMICategory` buckets computed across 400 million rows in PySpark (`df.____("BMICategory", F.when(...))`) plus standardized clinical study-week attributes without `Auto date/time`. Which two enrichments should you implement? Select two.

Domain: Prepare data

- A. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- B. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- C. Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs
- D. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- E. Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes

### 40. When a physician transfers from `Cardiology` to `Internal Medicine` on July 1, historical surgeries performed in March must still roll up under `Cardiology`, while August surgeries roll up under `Internal Medicine`. Which `DimPhysician` pattern is required?

Domain: Prepare data

- A. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)
- B. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- C. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns
- D. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place

### 41. A source clinic feed misspelled `"Massachusetts General"` as `"Massachussetts Genral"` on `DimFacility`. All historical and future reports should display the corrected spelling with no split history. Which SCD pattern applies?

Domain: Prepare data

- A. Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE
- B. Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place
- C. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns
- D. Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table

### 42. In which four-step order should your nightly Warehouse stored procedure update `DimHealthPlan` as a Type 2 Slowly Changing Dimension?

Domain: Prepare data

- A. Insert raw duplicate staging rows directly into FactSales → Delete unmatched dimension keys → Leave EffectiveStartDate NULL → Enable Assume referential integrity on broken keys
- B. Stage and deduplicate incoming records by natural key → Compare tracked attributes against active (IsCurrent = 1) Gold rows → Expire changed active rows (EffectiveEndDate, IsCurrent = 0) → Insert new active versions with fresh surrogate keys
- C. Insert new versions with IsCurrent = 0 first → Overwrite old EffectiveStartDate values in place → Remove the natural business key column → Deduplicate after publishing reports
- D. Truncate the Gold dimension table → Reassign fresh random surrogate keys to all historical rows → Join historical facts without updating foreign keys → Set IsCurrent = 1 on every version

### 43. Which three practices prevent double-counted claim lines and broken `1:*` Direct Lake joins in a clinical Medallion Warehouse? Select three.

Domain: Prepare data

- A. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE
- D. Organize OneLake into Bronze (raw immutable), Silver (validated, deduplicated, conformed), and Gold (star-schema dimensions and facts with V-Order)
- E. Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures
- F. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table

### 44. In the source EHR database, `Medication` joins to `TherapeuticSubclass`, which joins to `TherapeuticClass`, which joins to `FormularyTier`. How should you model these four tables in `GoldWarehouse` for Power BI?

Domain: Prepare data

- A. Choose a Fabric Eventhouse (KQL database)
- B. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other
- C. Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns
- D. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension

### 45. Proposed solution: To expose `Hospital -> HealthSystem -> GeographicDivision` in a Direct Lake semantic model, an engineer imports all three normalized tables and chains `1:*` relationships across them. What Gold-layer transformation reduces relationship traversal and memory overhead?

Domain: Prepare data

- A. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()
- B. Configure DirectQuery storage mode
- C. Execute an Enhanced Refresh API or XMLA TMSL refresh command specifying type = "dataOnly" or targeting only the modified partition
- D. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension

### 46. Continuous oximetry sensors generate 12 billion 1-second readings per month, but clinical quality dashboards only visualize hourly min/max/average `SpO2` per patient bed. What Gold-layer design cuts Direct Lake RAM consumption by >99%?

Domain: Prepare data

- A. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- B. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- C. Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP)
- D. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging

### 47. Complete `SELECT Facility, ServiceLine, COUNT(*) AS Admissions FROM gold.FactAdmissions ____;` to produce `(Facility, ServiceLine)` subtotals, `(Facility)` subtotals, and the overall hospital-system grand total in one T-SQL pass?

Domain: Prepare data

- A. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- B. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- C. | summarize arg_max(IngestionTime, *) by SpecimenId
- D. TRY_CAST(RawReading AS DECIMAL(18, 4))

### 48. In Dataflow Gen2, you apply a `Group by` step aggregating 90 million pharmacy dispense rows down to 40,000 daily drug totals against a Fabric Warehouse source. Why is keeping query folding intact before `Group by` critical?

Domain: Prepare data

- A. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- B. Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations

### 49. Complete `MERGE INTO gold.FactClaims AS target USING silver.StgClaims AS source ON target.ClaimLineId = source.ClaimLineId ____ target.PaidAmt = source.PaidAmt, target.Status = source.Status WHEN NOT MATCHED THEN INSERT ...;` so unchanged claim lines do not trigger unnecessary Delta file rewrites?

Domain: Prepare data

- A. ADD BLOCK PREDICATE dbo.sp_checkregion(RegionCode) AFTER INSERT
- B. CAST(RawReading AS FLOAT)
- C. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- D. WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET

### 50. A clinical data quality pipeline must find all `FactLabResults` records whose `OrderingNPI` code is missing from `DimProvider`. Which join pattern returns exclusively those unmatched lab rows?

Domain: Prepare data

- A. Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension
- B. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- C. Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table
- D. Execute a Delta Lake MERGE INTO target USING source ON ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT statement

### 51. In a Silver genomics PySpark notebook, you must (1) join a 900-million-row variant table with a 2 MB `dim_chromosome` lookup without shuffling the 900M rows (`variant_df.join(____)`), and (2) quarantine rows referencing retired reference-genome IDs missing from `dim_genome`. Which two join techniques apply? Select two.

Domain: Prepare data

- A. fact_df.join(F.broadcast(dim_store_df), on="StoreKey", how="left")
- B. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- C. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- D. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- E. Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table

### 52. HL7 interface engines occasionally emit duplicate admission messages for the same `SpecimenId` / `EncounterId`. Complete `WITH Dedup AS (SELECT *, ____ AS rn FROM bronze.hl7_events) SELECT * FROM Dedup WHERE rn = 1;` to retain strictly one newest event per key?

Domain: Prepare data

- A. GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ())
- B. RANK() OVER (ORDER BY SpecimenId DESC)
- C. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- D. TRY_CAST(RawReading AS DECIMAL(18, 4))

### 53. Emergency-room admissions arrive in real time before patient insurance plans are verified (`PlanNaturalId IS NULL`), and HL7 retries create duplicate `EncounterId` rows. Which two Silver-to-Gold rules protect `FactAdmissions`? Select two.

Domain: Prepare data

- A. Filter Incremental Refresh with OrderDate >= RangeStart AND OrderDate <= RangeEnd using inclusive operators on both boundaries
- B. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- C. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- D. Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE
- E. Deduplicate using ROW_NUMBER() OVER (PARTITION BY BusinessKey ORDER BY ModifiedTimestamp DESC) = 1

### 54. Point-of-care glucometer CSV files export `"LO"` or `"HI"` strings inside the numeric `GlucoseMgDl` column (`SELECT SpecimenId, ____ AS GlucoseNumeric FROM stage.GlucometerRaw;`). Which T-SQL expression prevents batch failure while preserving exact decimal precision?

Domain: Prepare data

- A. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- B. CAST(RawReading AS FLOAT)
- C. ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)
- D. TRY_CAST(RawReading AS DECIMAL(18, 4))

### 55. A Lakehouse Delta table synced from FHIR bundles includes `ObservationPayload` (`MAP<STRING,STRING>`) and `EncounterUUID` (`BINARY(16)`), which disappear or block selection when creating a Direct Lake semantic model. What transformation fixes this?

Domain: Prepare data

- A. Configure shared dimension tables in Dual storage mode inside a composite model
- B. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- C. Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake
- D. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)

### 56. In Power Query pulling from an on-premises clinical SQL Server, adding `Table.Buffer()` on Step 2 causes `View Native Query` to grey out on Step 3 (`Date >= #datetime(2025,1,1,0,0,0)`). What is the operational impact, and how do you fix it?

Domain: Prepare data

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled
- C. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- D. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'

### 57. Proposed solution: A clinical analyst filters a 4-billion-row Lakehouse Delta table with `WHERE YEAR(ServiceDate) = 2026 AND MONTH(ServiceDate) = 10` instead of `WHERE ServiceDate >= '2026-10-01' AND ServiceDate < '2026-11-01'`. Which predicate is superior for Delta Parquet file skipping, and why?

Domain: Prepare data

- A. Filter on physical Delta partition or liquid-clustered date columns using sargable range predicates (OrderDate >= '2026-01-01') without wrapping the column in functions
- B. CAST(RawReading AS FLOAT)
- C. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- D. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'

### 58. A clinical quality nurse with `ReadData` permission on `QualityWarehouse` wants to merge `FactReadmissions` with `DimDRG`, filter `DaysToReadmit <= 30`, aggregate counts by hospital unit visually in the browser, and save the query as `vw_30DayReadmissions`. Which Fabric tool fits?

Domain: Prepare data

- A. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results
- B. Use ALM Toolkit over the XMLA endpoint to compare Dev and Prod semantic models and deploy only new measures without reprocessing unchanged partitions
- C. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- D. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view

### 59. In the Fabric Visual query editor, an analyst inspects intermediate step previews while joining three Lakehouse SQL analytics endpoint tables and selects `Download Excel file` vs `Save as view`. Which option creates a live reusable virtual object in the SQL endpoint?

Domain: Prepare data

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint
- D. Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network

### 60. Before running an experimental ICD-10 remapping script in `ClaimsWarehouse`, you want an instantaneous zero-copy Warehouse backup table (`____;`) that consumes zero extra OneLake storage for unchanged Parquet files. Which T-SQL statement should you run?

Domain: Prepare data

- A. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- B. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- C. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- D. CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales

### 61. Inside `ClinicalWarehouse`, you write a query joining `ImagingLakehouse.dbo.ScanMetadata` in the same workspace and computing each patient's change in tumor size since their immediately preceding scan (`CurrentSize - ____`). Which two T-SQL capabilities apply? Select two.

Domain: Prepare data

- A. Query across a Warehouse and a Lakehouse SQL analytics endpoint in the same workspace using three-part T-SQL naming (SalesLakehouse.dbo.RawOrders)
- B. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- C. Filter historical queries with WHERE CONVERT(VARCHAR(10), OrderDate, 120) LIKE '2026-%'
- D. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- E. Run INSERT, UPDATE, and MERGE T-SQL statements directly against the Lakehouse SQL analytics endpoint

### 62. HL7 FHIR observations arrive in Eventhouse with a nested JSON array `Components` inside column `Payload`. Complete `FhirEvents ____ | summarize avg(toreal(Component.value)) by tostring(Component.code)` so each array element becomes a separate row?

Domain: Prepare data

- A. | make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion
- B. | summarize arg_max(IngestionTime, *) by SpecimenId
- C. | summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)
- D. | mv-expand PhaseReading = parse_json(Payload).PhaseReadings

### 63. A biostatistician live-editing a Direct Lake clinical semantic model in the browser wants to run `DEFINE VAR TargetDRG = "470" EVALUATE SUMMARIZECOLUMNS('DimHospital'[Region], "Cases", CALCULATE([Admissions], 'DimDRG'[Code] = TargetDRG))` without creating a report visual. Which Fabric / Power BI tool runs this natively?

Domain: Prepare data

- A. Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results
- B. Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts

### 64. Which family of built-in DAX functions (`EVALUATE ____`) lets an analytics engineer audit all relationships, cardinality settings, cross-filter directions, and active flags inside a semantic model directly from DAX Query View?

Domain: Prepare data

- A. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- B. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- C. Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View
- D. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN

### 65. An inpatient bed-capacity board connects to an external vendor's Snowflake transactional database (not mirrored to OneLake) and regulatory rules forbid caching or importing patient location data outside Snowflake while requiring <5-second live updates. Which storage mode is required?

Domain: Implement and manage semantic models

- A. Configure DirectQuery storage mode
- B. Configure Direct Lake storage mode
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Configure Import storage mode

### 66. Your hospital already curates a 1.5-billion-row V-Order optimized Gold Delta star schema in OneLake and needs sub-second interactive Power BI slicing without 2-hour scheduled Import data copies. Which storage mode fits best?

Domain: Implement and manage semantic models

- A. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- B. Configure Direct Lake storage mode
- C. Configure DirectQuery storage mode
- D. Configure Import storage mode

### 67. In `ClinicalQualityModel`, physicians using Personalize Visuals see `HospitalSurrogateKey`, `PatientSurrogateKey`, and raw `LengthOfStayDays` columns, and severity tiers sort `"Critical", "High", "Low", "Moderate"` alphabetically. How should you refine the star-schema model?

Domain: Implement and manage semantic models

- A. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS
- B. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other

### 68. You open a slow `.pbip` clinical model and find `Auto date/time` enabled across 22 date columns on a 180-million-row admission table. Which two actions reduce model memory and standardize time intelligence? Select two.

Domain: Implement and manage semantic models

- A. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- B. Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column
- E. Configure DirectQuery storage mode

### 69. `FactSurgeries` contains `ScheduledDateKey`, `AdmissionDateKey`, and `DischargeDateKey` all referencing `DimCalendar[DateKey]`. How do you calculate `[Admissions by Scheduled Date]` and `[Discharges by Discharge Date]` on the same visual date axis without creating three separate Calendar tables?

Domain: Implement and manage semantic models

- A. Introduce a deduplicated Bridge table between the two dimensions and scope bidirectional propagation strictly inside specific measures using CROSSFILTER(..., BOTH)
- B. Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP()
- C. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other

### 70. Proposed solution: On a DirectQuery model where `FactLabOrders[ReferringClinicKey]` contains `NULL` for walk-in patients, an engineer checks `Assume referential integrity` to speed up SQL joins. What unintended defect occurs on report totals?

Domain: Implement and manage semantic models

- A. Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop)
- B. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- C. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other

### 71. Complete `ICU Admissions = CALCULATE([Total Admissions], ____('DimUnit'[UnitType] = "ICU"))` so that when a report user filters a page slicer to `"Outpatient"`, `[ICU Admissions]` respects the intersection and returns `BLANK()` instead of repeating ICU totals on Outpatient rows?

Domain: Implement and manage semantic models

- A. Pass simple column predicates wrapped in KEEPFILTERS(DimProduct[Color] = "Red") to CALCULATE instead of FILTER(ALL(FactSales), ...)
- B. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table
- C. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows
- D. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically

### 72. Each row of `FactInfusions` has `DoseMgPerKg` and `PatientWeightKg`. Why should `Total Drug Mg = SUMX(FactInfusions, FactInfusions[DoseMgPerKg] * FactInfusions[PatientWeightKg])` be used instead of adding a persisted calculated column on a 600-million-row Import/Direct Lake table?

Domain: Implement and manage semantic models

- A. [ManagerEmail] = USERPRINCIPALNAME()
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table
- D. Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches

### 73. You are optimizing a complex `[Readmission Penalty %]` measure displayed in a `HealthSystem -> Hospital -> Ward` matrix: it repeats `[30-Day Readmissions]` four times in conditional logic and must return `BLANK()` at the `Ward` leaf level while showing values on `Hospital` and `HealthSystem` rows. Which two DAX techniques apply? Select two.

Domain: Implement and manage semantic models

- A. Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches
- B. Create a physical calculated column MarginPct = [Profit] / [Revenue] on the fact table and aggregate it with SUM or AVERAGE in visuals
- C. Use ISINSCOPE(DimProduct[Subcategory]) (or SELECTEDVALUE with an alternate result) to branch measure behavior cleanly across matrix hierarchy levels
- D. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically
- E. Write CALCULATE([Sales], FILTER(FactSales, FactSales[NetAmount] > 0 && RELATED(DimCustomer[Segment]) = "Enterprise")) over 500M rows

### 74. In Tabular Editor / Model view, you create a `Time Horizon` Calculation Group so clinical leaders can toggle `Rolling 30D`, `YTD`, and `Prior Year` across 40 quality measures. Complete the YTD calculation item expression `____`?

Domain: Implement and manage semantic models

- A. EVALUATE INFO.VIEW.MEASURES()
- B. CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))
- C. CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))
- D. NAMEOF('DimTrade'[CurrencyPair])

### 75. Proposed solution: A clinical analyst writes `Display Metric = SWITCH([SelectedKPI], 1, FORMAT([Avg LOS], "0.0 days"), 2, FORMAT([Mortality Rate], "0.00%"))` and tries to plot `[Display Metric]` on a clustered column chart. Why does the visual fail to plot bars, and what fixes it?

Domain: Implement and manage semantic models

- A. Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear
- B. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- C. Configure a Dynamic Format String expression on the measure or calculation item (for example returning "\$#,0.00" vs "0.0%" via SELECTEDMEASUREFORMATSTRING()) without wrapping values in FORMAT()
- D. Wrap numeric measures in FORMAT([Revenue], "$#,0.00") so currency symbols change dynamically

### 76. A Field Parameter table `ClinicalSlicer` lets users switch chart breakdowns dynamically: `ClinicalSlicer = { ("Payer Type", ____, 0), ("Age Cohort", 'DimPatient'[AgeCohort], 1) }`. Which DAX function wraps `'DimTrade'` / dimension column references inside Field Parameter definitions so column renames do not break the table?

Domain: Implement and manage semantic models

- A. IF(SELECTEDMEASURENAME() = "YoY Growth", "0.0%", SELECTEDMEASUREFORMATSTRING())
- B. CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))
- C. [ManagerEmail] = USERPRINCIPALNAME()
- D. NAMEOF('DimTrade'[CurrencyPair])

### 77. A national claims semantic model reaches 19 GB in compressed VertiPaq memory on an F128 capacity. Which setting must be enabled on the semantic model so scheduled refreshes and XMLA partition operations succeed past the standard size cap?

Domain: Implement and manage semantic models

- A. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- B. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages
- C. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)
- D. Configure DirectQuery storage mode

### 78. Even with `Large semantic model storage format` enabled on an F64 capacity (25 GB max model RAM), an unoptimized 29 GB model pages segments out of memory during peak morning usage. Which structural change shrinks compressed memory footprint below 25 GB without dropping historical years?

Domain: Implement and manage semantic models

- A. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal
- B. Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time
- C. Create a Field Parameter table using NAMEOF() on dimensions or measures and bind it to a visual axis/values well and slicer
- D. Configure Deployment pipeline data source and parameter rules on the Test and Production stages

### 79. A healthcare analytics team wants one semantic model combining a 500-million-row `FactClaims` table from `ClaimsLakehouse` in Direct Lake mode with a small `Import` table of state Medicaid fee schedules fetched from a public REST API, joined via regular `1:*` relationships. Which model architecture supports this?

Domain: Implement and manage semantic models

- A. Build a Direct Lake on OneLake composite semantic model combining Direct Lake fact tables from OneLake with Import dimension/target tables using regular relationships
- B. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- C. Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows
- D. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes

### 80. Over a 3-billion-row `DirectQuery` lab-results Warehouse table, you add an in-memory `FactLabDailyAgg` table grouped by `DateKey`, `TestTypeKey`, and `FacilityKey`. Which two configurations ensure high-level visuals hit RAM while specimen-level drillthrough queries push clean SQL joins to the Warehouse? Select two.

Domain: Implement and manage semantic models

- A. Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table
- B. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- C. Commit monolithic binary .pbix files containing 800 MB of imported data directly into Git feature branches
- D. Configure shared dimension tables in Dual storage mode inside a composite model
- E. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other

### 81. An inpatient executive report page takes 11 seconds to open. In Power BI Desktop Performance Analyzer, every visual shows `DAX query: 25 ms`, `Visual display: 45 ms`, and `Other: 6,800 ms`. What causes high `Other` duration, and what should you change?

Domain: Implement and manage semantic models

- A. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts
- B. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- C. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- D. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN

### 82. On a DirectQuery surgical-schedule report, clicking one bar in a chart triggers six cross-highlight SQL queries across complex scatter and matrix visuals on the same page. Which Power BI Desktop `Query reduction` option prevents automatic cross-highlight queries until requested?

Domain: Implement and manage semantic models

- A. Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails
- B. Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions
- C. Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages
- D. Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat)

### 83. A clinical DAX measure `[Complex Sepsis Cohort]` runs for 9.4 seconds; DAX Studio `Server Timings` reports `FE: 8,950 ms (95.2%)`, `SE: 450 ms (4.8%)`, and bold `CallbackDataID` markers in the `xmSQL` log. What does `CallbackDataID` indicate?

Domain: Implement and manage semantic models

- A. Profile the slow measure in DAX Studio using Server Timings to inspect Formula Engine (FE) vs Storage Engine (SE) CPU, SE query count, and CallbackDataID warnings
- B. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts

### 84. Which four-step workflow diagnoses and resolves a slow Direct Lake clinical mortality measure accurately without warm-cache bias?

Domain: Implement and manage semantic models

- A. Capture visual timings in Performance Analyzer → Profile captured DAX in DAX Studio with Server Timings and Query Plan → Refactor FILTER(Fact,...) into VAR-cached SE column predicates and run V-Order OPTIMIZE → Re-test with Clear Cache
- B. Test queries only against warm VertiPaq cache without Clear Cache → Add high-cardinality GUID calculated columns to FactSales → Force DirectQueryOnly behavior → Add 45 single-value card visuals to one page
- C. Hide slow measures in Display Folders → Turn on Auto date/time → Split one Gold dimension into 6 normalized snowflake tables → Remove calendar surrogate keys
- D. Immediately upgrade from F64 to F512 without profiling → Enable bidirectional cross-filtering on all relationships → Convert numeric measures to FORMAT() strings → Disable V-Order on Gold tables

### 85. On a Direct Lake on SQL semantic model, compliance policy forbids unexpected DirectQuery fallback queries from hitting the Warehouse compute pool if someone adds a table exceeding SKU rowguardrails (`____` in TMDL). Which TMDL property setting enforces fail-fast behavior?

Domain: Implement and manage semantic models

- A. directLakeBehavior: directLakeOnly
- B. CAST(RawReading AS FLOAT)
- C. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- D. Expect Direct Lake on OneLake to automatically fall back to DirectQuery against the SQL analytics endpoint when capacity memory guardrails are exceeded

### 86. A 1.1-billion-row clinical Direct Lake semantic model intermittently hits memory/rowgroup guardrails after streaming micro-batches write thousands of 2 MB Parquet files. Which three engineering actions keep the model comfortably inside Direct Lake guardrails? Select three.

Domain: Implement and manage semantic models

- A. Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time
- B. Expect Direct Lake on OneLake to automatically fall back to DirectQuery against the SQL analytics endpoint when capacity memory guardrails are exceeded
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes
- E. Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails
- F. Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes

### 87. A hospital data team has already built complex T-SQL `CREATE SECURITY POLICY` RLS predicates and T-SQL views inside `HospitalWarehouse` and accepts automatic DirectQuery fallback so report consumers reuse those exact SQL security rules and Deployment Pipeline data-source rules. Which Direct Lake mode must they choose?

Domain: Implement and manage semantic models

- A. Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression)
- B. Choose Direct Lake on OneLake (using the AzureStorage.DataLake M expression via OneLake catalog or Power BI Desktop)
- C. Configure Import storage mode
- D. Bind a Direct Lake semantic model to an On-premises or VNet data gateway for framing refreshes

### 88. After migrating SQL RLS policies into OneLake security, you want to convert a Direct Lake on SQL clinical semantic model to Direct Lake on OneLake in Power BI Desktop so you can add tables from a second Lakehouse. Which four-step sequence performs the conversion?

Domain: Implement and manage semantic models

- A. Download the Direct Lake model as an offline Import .pbix → Convert all tables to Dual storage mode → Replace AzureStorage.DataLake with OleDb.DataSource → Re-upload to My Workspace
- B. Keep non-materialized SQL analytics endpoint views as the only sources → Switch TMDL expression to AzureStorage.DataLake without materializing Delta tables → Enable DirectQuery fallback on Direct Lake on OneLake → Bind an On-premises gateway
- C. Delete the semantic model in Production breaking report GUID bindings → Recreate measures manually from screenshots → Share Lakehouse Admin rights with all report viewers → Disable V-Order
- D. Live edit the model in Power BI Desktop and save a Version history point → Script the semantic model in TMDL view → Replace Sql.Database(...) with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...") → Apply TMDL and run framing refresh

---

## Case study — AetherCare Health

AetherCare Health governs PHI clinical datasets in Microsoft Fabric. Highly Confidential Purview labels applied to Gold Warehouses must flow automatically to downstream semantic models and exported Excel files, only central HIPAA stewards may badge datasets as Certified, and engineers must notify owners across six departmental workspaces before renaming any clinical column.

The next 3 questions refer to **AetherCare Health**. Read the scenario brief once, then answer each item independently.

### 89. How do you ensure `Highly Confidential — PHI` classifications applied on Gold Warehouses propagate automatically to newly created semantic models and exported Excel workbooks?

Domain: Maintain a data analytics solution

- A. Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository
- B. Apply T-SQL Dynamic Data Masking (MASKED WITH (FUNCTION = 'partial(...)')) on sensitive columns
- C. Apply a Microsoft Purview sensitivity label with downstream inheritance on the source Lakehouse or Warehouse
- D. Mark the item as Promoted in item settings

### 90. Which endorsement configuration guarantees that only central HIPAA data stewards — and not arbitrary workspace Contributors — can badge clinical semantic models as officially vetted?

Domain: Maintain a data analytics solution

- A. Mark the item as Promoted in item settings
- B. Distribute a Power BI Data Source (.pbids) JSON file preconfigured with the server endpoint, database name, and connection mode
- C. Assign the Workspace Contributor role
- D. Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal

### 91. Before renaming `PatientMRN_Code` in the core clinical Warehouse, how should engineers identify every affected model across all six departmental workspaces and alert their owners?

Domain: Maintain a data analytics solution

- A. Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time
- B. Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View
- C. Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture
- D. Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts

---

## Case study — BioTrace Diagnostics

BioTrace Diagnostics ingests lab analyzer telemetry into an Eventhouse where retry bursts emit duplicate readings per SpecimenId, while reference Parquet extracts land unpredictably in a Lakehouse Files/inbound folder. Pipelines must trigger the instant new files arrive rather than polling hourly, and notebooks need full-dataset null/outlier profiling before Silver promotion.

The next 3 questions refer to **BioTrace Diagnostics**. Read the scenario brief once, then answer each item independently.

### 92. Retry bursts from lab analyzers write duplicate rows per `SpecimenId` into `AnalyzerTelemetry`. Complete `AnalyzerTelemetry | where IngestionTime > ago(12h) ____` to return the single latest full reading per specimen?

Domain: Prepare data

- A. | summarize arg_max(IngestionTime, *) by SpecimenId
- B. | summarize P99LatencyMs = percentile(DurationMs, 99) by bin(EventTime, 5m)
- C. | mv-expand PhaseReading = parse_json(Payload).PhaseReadings
- D. | make-series TxCount = count() default = 0 on EventTime from ago(6h) to now() step 1m by MerchantRegion

### 93. How should you trigger the Silver ingestion pipeline the instant new reference Parquet extracts arrive in `Files/inbound` rather than running wasteful hourly polling schedules?

Domain: Prepare data

- A. Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake
- B. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- C. Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view
- D. Use the Real-Time hub to subscribe to Microsoft.Fabric.OneLake.FileCreated events (or Capacity/CDC streams) and trigger an Activator rule

### 94. Which interactive notebook tool lets clinical data engineers inspect null percentages, quantiles, and outlier histograms across a Spark DataFrame and export clean PySpark code into Silver notebooks?

Domain: Prepare data

- A. Rely on Power Query's default Column quality bar (top 1,000 rows only) to certify zero duplicate keys across a 40-million-row staging table
- B. Iterate over Spark DataFrame rows in Python using df.collect() or a standard Python @udf loop for string/date transformations
- C. Launch Data Wrangler from a Fabric Spark notebook (or enable Power Query Column profiling based on entire data set) to inspect nulls, duplicates, and distributions and export generated PySpark code
- D. Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN

---

## Case study — MedBridge Claims

MedBridge Claims processes multi-table ACID adjudication batches in a Fabric Data Warehouse. Claims auditors querying via T-SQL must see only rows for their assigned payer network, see only the last four digits of patient tax IDs without breaking SELECT * queries, and compare current claim reserves against exact table state from 48 hours ago before an erroneous batch ran.

The next 3 questions refer to **MedBridge Claims**. Read the scenario brief once, then answer each item independently.

### 95. Complete `CREATE SECURITY POLICY ClaimsPayerPolicy ____;` in the Fabric Warehouse so T-SQL claims auditors see only rows belonging to their assigned payer network?

Domain: Maintain a data analytics solution

- A. ADD FILTER PREDICATE Security.fn_regionpredicate(RegionCode) ON dbo.FactSales WITH (STATE = ON)
- B. Create a dynamic DAX RLS role filtering a security mapping table with [UserEmail] = USERPRINCIPALNAME()
- C. Create a OneLake security role with ReadWrite permission and attach an RLS predicate
- D. ADD BLOCK PREDICATE dbo.sp_checkregion(RegionCode) AFTER INSERT

### 96. Which column definition on `PatientTaxId` (`ALTER TABLE dbo.Claims ALTER COLUMN PatientTaxId ADD ____;`) reveals only the trailing four digits to auditors while allowing `SELECT *` queries to execute without errors?

Domain: Maintain a data analytics solution

- A. Grant T-SQL column-level SELECT on only the non-sensitive columns (GRANT SELECT ON dbo.Customer(CustomerID, Region) TO ...)
- B. MASKED WITH (FUNCTION = 'partial(0,"XXX-XX-",4)')
- C. Configure Object-Level Security (OLS) set to None on the restricted table or column using Tabular Editor over XMLA or TMDL
- D. Mark sensitive salary or margin columns as Hidden in Model view instead of configuring OLS or CLS

### 97. Actuaries run `SELECT PayerId, SUM(ReserveAmt) FROM dbo.FactClaims ____ GROUP BY PayerId;` to compare current reserves against exact Warehouse state from 48 hours ago (`2026-10-28T06:00:00.000`). Which clause fills the blank?

Domain: Prepare data

- A. Truncate and reload all 10 years of a 6-billion-row historical table every 15 minutes using Dataflow Gen2 without staging
- B. LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC)
- C. FOR SYSTEM_TIME AS OF '2026-10-28T06:00:00.000'
- D. OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')

---

## Case study — VitalsCore Analytics

VitalsCore Analytics models hospital admissions where a single encounter maps to multiple ICD-10 diagnosis groups via a many-to-many relationship, fiscal quarters follow a 4-4-5 retail-health calendar requiring prior-period comparisons in DAX, and a 900-million-row Import claims archive refreshes over a VNet gateway with late adjustments updating `LastUpdatedUTC` on historical claims.

The next 3 questions refer to **VitalsCore Analytics**. Read the scenario brief once, then answer each item independently.

### 98. `FactEncounter` links `*:1` to `DimEncounter`, which links `1:*` to `BridgeEncounterDiag`, which links `*:1` to `DimDiagnosisGroup`. Complete `Diagnosed Encounters = ____` so diagnosis slicers filter encounter counts without global bidirectional joins?

Domain: Implement and manage semantic models

- A. CALCULATE([Total Notional], USERELATIONSHIP('Calendar'[DateKey], 'FactTrades'[SettlementDateKey]))
- B. CALCULATE([Encounter Count], CROSSFILTER('FactEncounter'[EncounterKey], 'BridgeEncounterDiag'[EncounterKey], BOTH))
- C. Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid
- D. Set Cross-filter direction to Both on every relationship in the semantic model to make all slicers filter each other

### 99. Because hospital finance uses a non-standard 4-4-5 fiscal calendar, `DATEADD` fails on period comparisons. Complete `Prior Period Revenue = ____` to fetch the preceding visible fiscal period?

Domain: Implement and manage semantic models

- A. CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC)))
- B. IF(ISINSCOPE('DimProduct'[SKU]), [Unit Margin], BLANK())
- C. Enable Auto date/time across a 200-million-row enterprise model with 18 date columns instead of a shared Calendar dimension
- D. CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))

### 100. On the 900-million-row Import claims archive where late claim adjustments update `LastUpdatedUTC`, in which four-step order should you configure Incremental Refresh with `Detect data changes`?

Domain: Implement and manage semantic models

- A. Create Text parameters named StartDate and EndDate → Add a custom M step breaking query folding before filtering → Use >= and <= inclusive bounds on both sides → Refresh only in Power BI Desktop
- B. Publish an unfiltered 2-billion-row Import PBIX locally first → Define RangeStart in DAX calculated tables afterward → Set storage mode to Direct Lake on OneLake → Enable VNet gateway on Direct Lake
- C. Create case-sensitive DateTime parameters RangeStart and RangeEnd → Apply foldable half-open filter (>= RangeStart and < RangeEnd) → Configure table Incremental refresh policy → Publish to workspace and run initial refresh to generate partitions
- D. Filter OrderDate > RangeEnd → Configure Detect data changes on the exact same OrderDate partition column → Disable query folding → Run XMLA clearValues without processing

---

## Answer key and explanations

### Question 1 — A

Answer: Assign the Workspace Viewer role. Workspace Contributors hold edit rights and bypass RLS completely; assigning the `Workspace Viewer` role (or distributing via an App with Read access) is mandatory for RLS enforcement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Correct. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. In this scenario: Workspace Contributors hold edit rights and bypass RLS completely; assigning the `Workspace Viewer` role (or distributing via an App with Read access) is mandatory for RLS enforcement.
- **B:** Incorrect for this requirement. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. Why the keyed choice wins: Workspace Contributors hold edit rights and bypass RLS completely; assigning the `Workspace Viewer` role (or distributing via an App with Read access) is mandatory for RLS enforcement.
- **C:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: Workspace Contributors hold edit rights and bypass RLS completely; assigning the `Workspace Viewer` role (or distributing via an App with Read access) is mandatory for RLS enforcement.
- **D:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: Workspace Contributors hold edit rights and bypass RLS completely; assigning the `Workspace Viewer` role (or distributing via an App with Read access) is mandatory for RLS enforcement.

### Question 2 — B

Answer: Assign the Workspace Admin role. Only `Workspace Admin` can delete a workspace, manage other Admins, or initialize workspace-level Git integration settings. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: Only `Workspace Admin` can delete a workspace, manage other Admins, or initialize workspace-level Git integration settings.
- **B:** Correct. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. In this scenario: Only `Workspace Admin` can delete a workspace, manage other Admins, or initialize workspace-level Git integration settings.
- **C:** Incorrect for this requirement. Workspace Members can create/edit items, share items, configure OneLake security roles, publish apps, and add Contributors or Viewers, without being able to delete the workspace or modify Workspace Admins. Why the keyed choice wins: Only `Workspace Admin` can delete a workspace, manage other Admins, or initialize workspace-level Git integration settings.
- **D:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: Only `Workspace Admin` can delete a workspace, manage other Admins, or initialize workspace-level Git integration settings.

### Question 3 — A, D

Answers: Assign the Workspace Contributor role; Assign permissions to Microsoft Entra security groups rather than individual users. Granting `Workspace Contributor` scoped to a Microsoft Entra security group provides least-privilege build rights with automated group lifecycle revocation. Local study-map skill 1.1 (Implement Workspace-Level Access Controls (Admin, Member, Contributor, Viewer & Entra Groups)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Roles in workspaces in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces).

- **A:** Correct. Granting workspace, item, deployment-pipeline, and RLS role memberships to Microsoft Entra security groups centralizes joiner/mover/leaver governance and scales across workspaces without per-user ACL drift. In this scenario: Granting `Workspace Contributor` scoped to a Microsoft Entra security group provides least-privilege build rights with automated group lifecycle revocation.
- **B:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: Granting `Workspace Contributor` scoped to a Microsoft Entra security group provides least-privilege build rights with automated group lifecycle revocation.
- **C:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: Granting `Workspace Contributor` scoped to a Microsoft Entra security group provides least-privilege build rights with automated group lifecycle revocation.
- **D:** Correct. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. In this scenario: Granting `Workspace Contributor` scoped to a Microsoft Entra security group provides least-privilege build rights with automated group lifecycle revocation.
- **E:** Incorrect for this requirement. Workspace Admins have full control over workspace settings, Git connection setup, adding/removing Admins and other role members, and deleting the workspace itself — exceeding least privilege when a user only builds or views items. Why the keyed choice wins: Granting `Workspace Contributor` scoped to a Microsoft Entra security group provides least-privilege build rights with automated group lifecycle revocation.

### Question 4 — B

Answer: Enable single sign-on (SSO) on the Direct Lake semantic model connection. Enabling single sign-on (`SSO`) on the Direct Lake model passes the viewing user's Entra identity to the SQL analytics endpoint / Warehouse permission check. With SSO enabled on a Direct Lake model, Fabric evaluates data permissions at the underlying SQL analytics endpoint or OneLake security layer using each viewing report consumer's own Microsoft Entra identity. Local study-map skill 1.2 (Implement Item-Level Access Controls (Read, ReadData, ReadAll, Build, SSO vs Fixed Identity)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Share items in Microsoft Fabric & Semantic model Build permission (https://learn.microsoft.com/en-us/fabric/fundamentals/share-items).

- **A:** Incorrect for this requirement. Configuring a fixed-identity cloud connection (Service Principal or Workspace Identity) with SSO disabled lets report consumers query the Direct Lake model enforced by semantic-model RLS without granting them any direct Lakehouse or SQL endpoint permissions. Why the keyed choice wins: Enabling single sign-on (`SSO`) on the Direct Lake model passes the viewing user's Entra identity to the SQL analytics endpoint / Warehouse permission check.
- **B:** Correct. With SSO enabled on a Direct Lake model, Fabric evaluates data permissions at the underlying SQL analytics endpoint or OneLake security layer using each viewing report consumer's own Microsoft Entra identity. In this scenario: Enabling single sign-on (`SSO`) on the Direct Lake model passes the viewing user's Entra identity to the SQL analytics endpoint / Warehouse permission check.
- **C:** Incorrect for this requirement. ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled. Why the keyed choice wins: Enabling single sign-on (`SSO`) on the Direct Lake model passes the viewing user's Entra identity to the SQL analytics endpoint / Warehouse permission check.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Enabling single sign-on (`SSO`) on the Direct Lake model passes the viewing user's Entra identity to the SQL analytics endpoint / Warehouse permission check.

### Question 5 — B

Answer: Share the Lakehouse with ReadAll (Read all Apache Spark data) permission. Sharing `CoreImagingLakehouse` with `ReadAll` (`Read all Apache Spark data`) grants OneLake ABFS read access to `Files/` and `Tables/` for Spark workloads. ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled. Local study-map skill 1.2 (Implement Item-Level Access Controls (Read, ReadData, ReadAll, Build, SSO vs Fixed Identity)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Share items in Microsoft Fabric & Semantic model Build permission (https://learn.microsoft.com/en-us/fabric/fundamentals/share-items).

- **A:** Incorrect for this requirement. ReadData grants SELECT across all tables/views in the SQL analytics endpoint or Warehouse without granting direct Spark/ABFS access to underlying Lakehouse files. Why the keyed choice wins: Sharing `CoreImagingLakehouse` with `ReadAll` (`Read all Apache Spark data`) grants OneLake ABFS read access to `Files/` and `Tables/` for Spark workloads.
- **B:** Correct. ReadAll grants direct ABFS/OneLake read access to all Lakehouse Delta tables and Files folders for Spark or Direct Lake on OneLake SSO when OneLake granular security is not enabled. In this scenario: Sharing `CoreImagingLakehouse` with `ReadAll` (`Read all Apache Spark data`) grants OneLake ABFS read access to `Files/` and `Tables/` for Spark workloads.
- **C:** Incorrect for this requirement. Build permission on a semantic model allows analysts to create new Power BI reports, use Analyze in Excel, and issue XMLA/DAX queries against the model without granting workspace Contributor rights or underlying Lakehouse access. Why the keyed choice wins: Sharing `CoreImagingLakehouse` with `ReadAll` (`Read all Apache Spark data`) grants OneLake ABFS read access to `Files/` and `Tables/` for Spark workloads.
- **D:** Incorrect for this requirement. Item-level Read metadata permission lets a user connect to a Lakehouse or Warehouse item container without granting broad OneLake file access; combine with SELECT or OneLake security roles for granular least-privilege access. Why the keyed choice wins: Sharing `CoreImagingLakehouse` with `ReadAll` (`Read all Apache Spark data`) grants OneLake ABFS read access to `Files/` and `Tables/` for Spark workloads.

### Question 6 — C

Answer: Enable OneLake security and define Read Grant roles → Assign consumers Workspace Viewer and OneLake security roles → Set SQL analytics endpoint to User's identity mode → Expose downstream shortcuts in User's identity mode. Enabling OneLake security Grant roles, assigning researchers Viewer + security roles, switching SQL endpoints to User's identity mode, and exposing shortcuts in User's identity mode enforces end-to-end policies. Correct order: enable OneLake security with Grant roles first, assign consumers to Viewer + security roles (never Contributor), set SQL analytics endpoints to User's identity mode, and expose shortcuts downstream. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. Incorrect: mixing pre-existing SQL granular access with Delegated mode forces 100% DirectQuery fallback instead of clean OneLake security evaluation. Why the keyed choice wins: Enabling OneLake security Grant roles, assigning researchers Viewer + security roles, switching SQL endpoints to User's identity mode, and exposing shortcuts in User's identity mode enforces end-to-end policies.
- **B:** Incorrect for this requirement. Incorrect: Contributors bypass OneLake security completely, OneLake security has no Deny role type, and Owner fixed identity bypasses per-user role evaluation on SQL queries. Why the keyed choice wins: Enabling OneLake security Grant roles, assigning researchers Viewer + security roles, switching SQL endpoints to User's identity mode, and exposing shortcuts in User's identity mode enforces end-to-end policies.
- **C:** Correct. Correct order: enable OneLake security with Grant roles first, assign consumers to Viewer + security roles (never Contributor), set SQL analytics endpoints to User's identity mode, and expose shortcuts downstream. In this scenario: Enabling OneLake security Grant roles, assigning researchers Viewer + security roles, switching SQL endpoints to User's identity mode, and exposing shortcuts in User's identity mode enforces end-to-end policies.
- **D:** Incorrect for this requirement. Incorrect: Members bypass OneLake security, ReadWrite roles cannot contain RLS/CLS rules, and OneLake shortcuts do not use On-premises gateways. Why the keyed choice wins: Enabling OneLake security Grant roles, assigning researchers Viewer + security roles, switching SQL endpoints to User's identity mode, and exposing shortcuts in User's identity mode enforces end-to-end policies.

### Question 7 — C, E

Answers: Create a dynamic DAX RLS role filtering a security mapping table with [UserEmail] = USERPRINCIPALNAME(); Validate the security role in the Fabric service or Power BI Desktop using Test as role / View as with a target user's UPN. Filtering with `[UserEmail] = USERPRINCIPALNAME()` ensures consistent cloud UPN matching, and validating via `Test as role` combined with `dr.patel@aethercare.org` verifies both the DAX predicate and effective permissions. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. In Power BI Desktop USERNAME() returns DOMAIN\user whereas in the Fabric service it returns the UPN; USERPRINCIPALNAME() consistently returns user@domain.com across cloud evaluations. Why the keyed choice wins: Filtering with `[UserEmail] = USERPRINCIPALNAME()` ensures consistent cloud UPN matching, and validating via `Test as role` combined with `dr.patel@aethercare.org` verifies both the DAX predicate and effective permissions.
- **B:** Incorrect for this requirement. Workspace Admins, Members, and Contributors hold edit rights on workspace items and completely bypass both Semantic Model RLS and OneLake security roles — leaking all rows. Why the keyed choice wins: Filtering with `[UserEmail] = USERPRINCIPALNAME()` ensures consistent cloud UPN matching, and validating via `Test as role` combined with `dr.patel@aethercare.org` verifies both the DAX predicate and effective permissions.
- **C:** Correct. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). In this scenario: Filtering with `[UserEmail] = USERPRINCIPALNAME()` ensures consistent cloud UPN matching, and validating via `Test as role` combined with `dr.patel@aethercare.org` verifies both the DAX predicate and effective permissions.
- **D:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Filtering with `[UserEmail] = USERPRINCIPALNAME()` ensures consistent cloud UPN matching, and validating via `Test as role` combined with `dr.patel@aethercare.org` verifies both the DAX predicate and effective permissions.
- **E:** Correct. Dynamic DAX RLS filters rows at query time based on USERPRINCIPALNAME() (always returning the Entra UPN email, unlike USERNAME() which can return DOMAIN\user locally) and only restricts Workspace Viewers or App/shared consumers. In this scenario: Filtering with `[UserEmail] = USERPRINCIPALNAME()` ensures consistent cloud UPN matching, and validating via `Test as role` combined with `dr.patel@aethercare.org` verifies both the DAX predicate and effective permissions.

### Question 8 — B

Answer: Enable a mandatory label policy and default sensitivity label in Microsoft Purview compliance portal for Fabric users. Enabling a mandatory labeling policy and a default sensitivity label for Power BI / Fabric in the Microsoft Purview compliance portal enforces classification on creation and save. Mandatory and default sensitivity label policies in Microsoft Purview require content creators to classify unlabeled semantic models and reports on save and apply baseline classification automatically. Local study-map skill 1.4 (Apply Microsoft Purview Sensitivity Labels, Inheritance, Default/Mandatory Policies, and Export Encryption), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Information protection & sensitivity labels in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-overview).

- **A:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Enabling a mandatory labeling policy and a default sensitivity label for Power BI / Fabric in the Microsoft Purview compliance portal enforces classification on creation and save.
- **B:** Correct. Mandatory and default sensitivity label policies in Microsoft Purview require content creators to classify unlabeled semantic models and reports on save and apply baseline classification automatically. In this scenario: Enabling a mandatory labeling policy and a default sensitivity label for Power BI / Fabric in the Microsoft Purview compliance portal enforces classification on creation and save.
- **C:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Enabling a mandatory labeling policy and a default sensitivity label for Power BI / Fabric in the Microsoft Purview compliance portal enforces classification on creation and save.
- **D:** Incorrect for this requirement. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Why the keyed choice wins: Enabling a mandatory labeling policy and a default sensitivity label for Power BI / Fabric in the Microsoft Purview compliance portal enforces classification on creation and save.

### Question 9 — A

Answer: Configure Certified endorsement with the Master data label on authoritative core tables or semantic models. Enabling `Certified` endorsement with the `Master data` designation marks authoritative core data repositories clearly in OneLake catalog search results. Fabric admins can enable Master data endorsement for authoritative single-source-of-truth silver/gold data assets so analysts distinguish core reference items in the OneLake catalog. Local study-map skill 1.5 (Endorse Items Using Promoted, Certified, and Master Data Governance Badges), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Endorsement (Promoted, Certified, Master data) in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview).

- **A:** Correct. Fabric admins can enable Master data endorsement for authoritative single-source-of-truth silver/gold data assets so analysts distinguish core reference items in the OneLake catalog. In this scenario: Enabling `Certified` endorsement with the `Master data` designation marks authoritative core data repositories clearly in OneLake catalog search results.
- **B:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Enabling `Certified` endorsement with the `Master data` designation marks authoritative core data repositories clearly in OneLake catalog search results.
- **C:** Incorrect for this requirement. While sensitivity labels in Fabric classify items in the workspace without encrypting OneLake Delta storage itself, encryption-enabled labels enforce rights management automatically when users export data to Excel, PDF, PowerPoint, or .pbix. Why the keyed choice wins: Enabling `Certified` endorsement with the `Master data` designation marks authoritative core data repositories clearly in OneLake catalog search results.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Enabling `Certified` endorsement with the `Master data` designation marks authoritative core data repositories clearly in OneLake catalog search results.

### Question 10 — A

Answer: Commit workspace changes to Git from the Source control pane, merge via pull request, then select Update all in the target workspace. Fabric workspaces do not auto-apply remote Git commits on merge; opening the Source control pane and selecting `Update all` syncs the merged `main` commit into the workspace. Fabric Git sync is explicit rather than automatic on remote push: developers Commit workspace edits to their branch, complete a PR in Azure DevOps or GitHub, and run Update from Git in the downstream workspace. Local study-map skill 1.6 (Configure Workspace Version Control with Azure DevOps or GitHub (Branch Out, Commit, Update, Undo)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to Git integration in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration).

- **A:** Correct. Fabric Git sync is explicit rather than automatic on remote push: developers Commit workspace edits to their branch, complete a PR in Azure DevOps or GitHub, and run Update from Git in the downstream workspace. In this scenario: Fabric workspaces do not auto-apply remote Git commits on merge; opening the Source control pane and selecting `Update all` syncs the merged `main` commit into the workspace.
- **B:** Incorrect for this requirement. Undo reverts uncommitted workspace item modifications to match the connected Git branch HEAD without rewriting shared remote commit history. Why the keyed choice wins: Fabric workspaces do not auto-apply remote Git commits on merge; opening the Source control pane and selecting `Update all` syncs the merged `main` commit into the workspace.
- **C:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Fabric workspaces do not auto-apply remote Git commits on merge; opening the Source control pane and selecting `Update all` syncs the merged `main` commit into the workspace.
- **D:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Fabric workspaces do not auto-apply remote Git commits on merge; opening the Source control pane and selecting `Update all` syncs the merged `main` commit into the workspace.

### Question 11 — D

Answer: Connect shared Dev workspace to main → Branch out to an isolated developer workspace and commit .pbip/Notebook edits → Merge pull request into main in Git → Run Update all in Dev and promote via Deployment Pipeline. Connecting `Dev` to `main`, branching out to an isolated workspace, merging via pull request, running `Update all` in `Dev`, and promoting through the Deployment Pipeline maintains clean governance. Correct order: link Dev to main, branch out to an isolated workspace for feature work, validate and merge via Git PR into main, run Update all in Dev, and promote via Deployment Pipeline with stage rules. Local study-map skill 1.6 (Configure Workspace Version Control with Azure DevOps or GitHub (Branch Out, Commit, Update, Undo)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to Git integration in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration).

- **A:** Incorrect for this requirement. Incorrect: editing Production directly on feature branches and committing cache.abf violates ALM isolation, leaks cached data, and bypasses Test validation. Why the keyed choice wins: Connecting `Dev` to `main`, branching out to an isolated workspace, merging via pull request, running `Update all` in `Dev`, and promoting through the Deployment Pipeline maintains clean governance.
- **B:** Incorrect for this requirement. Incorrect: My Workspace does not support full team Git ALM, Undo discards local changes rather than committing, and deleting .platform breaks item lineage. Why the keyed choice wins: Connecting `Dev` to `main`, branching out to an isolated workspace, merging via pull request, running `Update all` in `Dev`, and promoting through the Deployment Pipeline maintains clean governance.
- **C:** Incorrect for this requirement. Incorrect: Fabric workspaces do not auto-pull remote PR merges — skipping Update from Git promotes stale pre-PR workspace state to Test. Why the keyed choice wins: Connecting `Dev` to `main`, branching out to an isolated workspace, merging via pull request, running `Update all` in `Dev`, and promoting through the Deployment Pipeline maintains clean governance.
- **D:** Correct. Correct order: link Dev to main, branch out to an isolated workspace for feature work, validate and merge via Git PR into main, run Update all in Dev, and promote via Deployment Pipeline with stage rules. In this scenario: Connecting `Dev` to `main`, branching out to an isolated workspace, merging via pull request, running `Update all` in `Dev`, and promoting through the Deployment Pipeline maintains clean governance.

### Question 12 — C

Answer: Commit .gitignore automatically excluding **/cache.abf and **/localSettings.json from the .pbip repository. Excluding `**/cache.abf` (alongside `**/localSettings.json`) prevents local compressed VertiPaq data caches from leaking PHI or bloating Git history. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Local study-map skill 1.7 (Create and Manage Power BI Desktop Projects (.pbip) with TMDL, PBIR, and .gitignore Hygiene), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Power BI Desktop projects (.pbip), TMDL, and PBIR (https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview).

- **A:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Excluding `**/cache.abf` (alongside `**/localSettings.json`) prevents local compressed VertiPaq data caches from leaking PHI or bloating Git history.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Excluding `**/cache.abf` (alongside `**/localSettings.json`) prevents local compressed VertiPaq data caches from leaking PHI or bloating Git history.
- **C:** Correct. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. In this scenario: Excluding `**/cache.abf` (alongside `**/localSettings.json`) prevents local compressed VertiPaq data caches from leaking PHI or bloating Git history.
- **D:** Incorrect for this requirement. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. Why the keyed choice wins: Excluding `**/cache.abf` (alongside `**/localSettings.json`) prevents local compressed VertiPaq data caches from leaking PHI or bloating Git history.

### Question 13 — A, B

Answers: Save the solution as a Power BI Project (.pbip) using TMDL for the semantic model and PBIR for report definitions; Connect the shared workspace to main and use Branch out to a separate isolated developer workspace per feature branch. Authoring in `.pbip` format (`TMDL` + `PBIR`) produces human-readable text diffs, and `Branch out` creates isolated per-branch Fabric developer workspaces. Local study-map skill 1.7 (Create and Manage Power BI Desktop Projects (.pbip) with TMDL, PBIR, and .gitignore Hygiene), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Power BI Desktop projects (.pbip), TMDL, and PBIR (https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview).

- **A:** Correct. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. In this scenario: Authoring in `.pbip` format (`TMDL` + `PBIR`) produces human-readable text diffs, and `Branch out` creates isolated per-branch Fabric developer workspaces.
- **B:** Correct. In Fabric Git integration, workspaces map 1-to-1 to branches; branching out into a dedicated developer workspace isolates in-progress notebook, pipeline, and semantic model edits before merging via pull request. In this scenario: Authoring in `.pbip` format (`TMDL` + `PBIR`) produces human-readable text diffs, and `Branch out` creates isolated per-branch Fabric developer workspaces.
- **C:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Authoring in `.pbip` format (`TMDL` + `PBIR`) produces human-readable text diffs, and `Branch out` creates isolated per-branch Fabric developer workspaces.
- **D:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Authoring in `.pbip` format (`TMDL` + `PBIR`) produces human-readable text diffs, and `Branch out` creates isolated per-branch Fabric developer workspaces.
- **E:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Authoring in `.pbip` format (`TMDL` + `PBIR`) produces human-readable text diffs, and `Branch out` creates isolated per-branch Fabric developer workspaces.

### Question 14 — C

Answer: Deploy backward from Production (or Test) into an empty Development workspace to initialize the pipeline. Assigning empty workspaces to `Test` and `Development` and performing backward deployment (`Production -> Test -> Development`) clones supported items with intact pipeline pairing. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. Selective deployment in Fabric Deployment Pipelines promotes only chosen items between stages, and Select related ensures newly referenced lakehouses or semantic models deploy alongside dependent reports. Why the keyed choice wins: Assigning empty workspaces to `Test` and `Development` and performing backward deployment (`Production -> Test -> Development`) clones supported items with intact pipeline pairing.
- **B:** Incorrect for this requirement. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Why the keyed choice wins: Assigning empty workspaces to `Test` and `Development` and performing backward deployment (`Production -> Test -> Development`) clones supported items with intact pipeline pairing.
- **C:** Correct. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. In this scenario: Assigning empty workspaces to `Test` and `Development` and performing backward deployment (`Production -> Test -> Development`) clones supported items with intact pipeline pairing.
- **D:** Incorrect for this requirement. Undo reverts uncommitted workspace item modifications to match the connected Git branch HEAD without rewriting shared remote commit history. Why the keyed choice wins: Assigning empty workspaces to `Test` and `Development` and performing backward deployment (`Production -> Test -> Development`) clones supported items with intact pipeline pairing.

### Question 15 — D

Answer: Configure Deployment pipeline data source and parameter rules on the Test and Production stages. Configuring Deployment Pipeline data source and parameter rules on the `Production` stage automatically maps deployed items to `prod-claims-wh` on every promotion. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Configuring Deployment Pipeline data source and parameter rules on the `Production` stage automatically maps deployed items to `prod-claims-wh` on every promotion.
- **B:** Incorrect for this requirement. When an existing Production workspace precedes Dev/Test, assigning Production first and deploying backward populates an empty Test/Dev workspace with matching item lineage. Why the keyed choice wins: Configuring Deployment Pipeline data source and parameter rules on the `Production` stage automatically maps deployed items to `prod-claims-wh` on every promotion.
- **C:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Configuring Deployment Pipeline data source and parameter rules on the `Production` stage automatically maps deployed items to `prod-claims-wh` on every promotion.
- **D:** Correct. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. In this scenario: Configuring Deployment Pipeline data source and parameter rules on the `Production` stage automatically maps deployed items to `prod-claims-wh` on every promotion.

### Question 16 — C

Answer: Use a Fabric Variable library (or autobinding across paired workspace items) to parameterize stage-specific environment references. A Fabric `Variable library` maintains stage-specific values across `Dev`, `Test`, and `Prod` stages that pipelines reference dynamically without hardcoding GUIDs. Fabric Variable libraries store stage-specific workspace/lakehouse IDs, URLs, and thresholds across Dev/Test/Prod — essential for items like Data Pipelines and Direct Lake on OneLake models that do not use legacy SQL deployment rules. Local study-map skill 1.8 (Create and Configure Deployment Pipelines, Deployment Rules, Variable Libraries, and Selective/Backward Deploys), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Introduction to deployment pipelines & Variable libraries in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines).

- **A:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: A Fabric `Variable library` maintains stage-specific values across `Dev`, `Test`, and `Prod` stages that pipelines reference dynamically without hardcoding GUIDs.
- **B:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: A Fabric `Variable library` maintains stage-specific values across `Dev`, `Test`, and `Prod` stages that pipelines reference dynamically without hardcoding GUIDs.
- **C:** Correct. Fabric Variable libraries store stage-specific workspace/lakehouse IDs, URLs, and thresholds across Dev/Test/Prod — essential for items like Data Pipelines and Direct Lake on OneLake models that do not use legacy SQL deployment rules. In this scenario: A Fabric `Variable library` maintains stage-specific values across `Dev`, `Test`, and `Prod` stages that pipelines reference dynamically without hardcoding GUIDs.
- **D:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: A Fabric `Variable library` maintains stage-specific values across `Dev`, `Test`, and `Prod` stages that pipelines reference dynamically without hardcoding GUIDs.

### Question 17 — C

Answer: Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts. Workspace `Lineage` view renders the upstream-to-downstream directed dependency graph, refresh statuses, endorsement badges, and cross-workspace impact counts for each item. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Local study-map skill 1.9 (Perform Downstream Dependency Impact Analysis Across Lakehouses, Warehouses, Dataflows, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Lineage and impact analysis in Microsoft Fabric workspaces (https://learn.microsoft.com/en-us/fabric/governance/lineage).

- **A:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Workspace `Lineage` view renders the upstream-to-downstream directed dependency graph, refresh statuses, endorsement badges, and cross-workspace impact counts for each item.
- **B:** Incorrect for this requirement. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Why the keyed choice wins: Workspace `Lineage` view renders the upstream-to-downstream directed dependency graph, refresh statuses, endorsement badges, and cross-workspace impact counts for each item.
- **C:** Correct. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. In this scenario: Workspace `Lineage` view renders the upstream-to-downstream directed dependency graph, refresh statuses, endorsement badges, and cross-workspace impact counts for each item.
- **D:** Incorrect for this requirement. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Why the keyed choice wins: Workspace `Lineage` view renders the upstream-to-downstream directed dependency graph, refresh statuses, endorsement badges, and cross-workspace impact counts for each item.

### Question 18 — D

Answer: Verify XMLA Endpoint = Read Write on target capacity → Connect ALM Toolkit to Dev source and Prod XMLA target → Compare schemas while hiding unchanged partitions and keeping Prod data sources → Validate and deploy metadata-only TMSL changes. Confirming `XMLA Endpoint = Read Write`, comparing Dev and Prod in ALM Toolkit while hiding unchanged partitions and preserving Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing downtime. Correct order: confirm Read Write XMLA capacity setting, compare Dev vs Prod models, preserve Prod partition state and data-source bindings, and push metadata-only measure/relationship diffs. Local study-map skill 1.10 (Deploy and Manage Semantic Models Using the XMLA Endpoint (Read-Write, TMSL, Tabular Editor, ALM Toolkit)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model connectivity and management with the XMLA endpoint (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools).

- **A:** Incorrect for this requirement. Incorrect: XMLA Off blocks external deployment, and overwriting Production with an unpartitioned file destroys incremental partitions and causes prolonged outage. Why the keyed choice wins: Confirming `XMLA Endpoint = Read Write`, comparing Dev and Prod in ALM Toolkit while hiding unchanged partitions and preserving Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing downtime.
- **B:** Incorrect for this requirement. Incorrect: DAX Studio is a query/profiling tool (not a model-deployment tool), and unversioned Production hotfixes cause immediate drift on next deployment. Why the keyed choice wins: Confirming `XMLA Endpoint = Read Write`, comparing Dev and Prod in ALM Toolkit while hiding unchanged partitions and preserving Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing downtime.
- **C:** Incorrect for this requirement. Incorrect: Read Only XMLA rejects TMSL model deployments, and Capacity Admin rights violate least privilege. Why the keyed choice wins: Confirming `XMLA Endpoint = Read Write`, comparing Dev and Prod in ALM Toolkit while hiding unchanged partitions and preserving Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing downtime.
- **D:** Correct. Correct order: confirm Read Write XMLA capacity setting, compare Dev vs Prod models, preserve Prod partition state and data-source bindings, and push metadata-only measure/relationship diffs. In this scenario: Confirming `XMLA Endpoint = Read Write`, comparing Dev and Prod in ALM Toolkit while hiding unchanged partitions and preserving Prod data sources, and deploying metadata-only TMSL changes avoids reprocessing downtime.

### Question 19 — A, C

Answers: Enable XMLA Endpoint = Read Write in Fabric Capacity workload settings and connect to powerbi://api.powerbi.com/v1.0/myorg/<WorkspaceName>; Use ALM Toolkit over the XMLA endpoint to compare Dev and Prod semantic models and deploy only new measures without reprocessing unchanged partitions. The target capacity must set `XMLA Endpoint = Read Write`, and ALM Toolkit compares schemas over `powerbi://api.powerbi.com/v1.0/myorg/<Workspace>` to emit metadata-only TMSL scripts. Local study-map skill 1.10 (Deploy and Manage Semantic Models Using the XMLA Endpoint (Read-Write, TMSL, Tabular Editor, ALM Toolkit)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model connectivity and management with the XMLA endpoint (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools).

- **A:** Correct. ALM Toolkit performs metadata-only diffs and incremental TMSL deployments over XMLA, preserving existing processed historical partitions and incremental refresh windows in Production. In this scenario: The target capacity must set `XMLA Endpoint = Read Write`, and ALM Toolkit compares schemas over `powerbi://api.powerbi.com/v1.0/myorg/<Workspace>` to emit metadata-only TMSL scripts.
- **B:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: The target capacity must set `XMLA Endpoint = Read Write`, and ALM Toolkit compares schemas over `powerbi://api.powerbi.com/v1.0/myorg/<Workspace>` to emit metadata-only TMSL scripts.
- **C:** Correct. External ALM tools (Tabular Editor, SSMS, ALM Toolkit, SqlPackage/PowerShell Invoke-ASCmd) require workspace Fabric/Premium capacity with XMLA Endpoint set to Read Write to deploy or modify semantic models. In this scenario: The target capacity must set `XMLA Endpoint = Read Write`, and ALM Toolkit compares schemas over `powerbi://api.powerbi.com/v1.0/myorg/<Workspace>` to emit metadata-only TMSL scripts.
- **D:** Incorrect for this requirement. Workspace Viewers have read-only access to workspace items and SQL analytics endpoints, cannot edit items or run notebooks, and are the only workspace role enforced by Semantic Model RLS and OneLake security rules. Why the keyed choice wins: The target capacity must set `XMLA Endpoint = Read Write`, and ALM Toolkit compares schemas over `powerbi://api.powerbi.com/v1.0/myorg/<Workspace>` to emit metadata-only TMSL scripts.
- **E:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: The target capacity must set `XMLA Endpoint = Read Write`, and ALM Toolkit compares schemas over `powerbi://api.powerbi.com/v1.0/myorg/<Workspace>` to emit metadata-only TMSL scripts.

### Question 20 — D

Answer: Export a Power BI Template (.pbit) containing report layout, model schema, DAX measures, and query parameters with zero imported data rows. Exporting a Power BI Template (`.pbit`) packages report visuals, DAX measures, and schema with zero imported data rows and prompts each clinic for its `HospitalFacilityCode` on open. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Local study-map skill 1.11 (Create and Update Reusable Assets (.pbit Templates, .pbids Data Sources, and Shared Golden Semantic Models)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create and use report templates (.pbit), data sources (.pbids), and shared semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-templates).

- **A:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Exporting a Power BI Template (`.pbit`) packages report visuals, DAX measures, and schema with zero imported data rows and prompts each clinic for its `HospitalFacilityCode` on open.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Exporting a Power BI Template (`.pbit`) packages report visuals, DAX measures, and schema with zero imported data rows and prompts each clinic for its `HospitalFacilityCode` on open.
- **C:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Exporting a Power BI Template (`.pbit`) packages report visuals, DAX measures, and schema with zero imported data rows and prompts each clinic for its `HospitalFacilityCode` on open.
- **D:** Correct. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. In this scenario: Exporting a Power BI Template (`.pbit`) packages report visuals, DAX measures, and schema with zero imported data rows and prompts each clinic for its `HospitalFacilityCode` on open.

### Question 21 — D

Answer: Publish a single certified core semantic model in a data workspace and build thin live-connected Power BI reports in departmental workspaces. Connecting Power BI Desktop live to the shared `ClinicalEncounters` semantic model (`Build` permission) and publishing thin reports into departmental workspaces reuses one in-memory model. Decoupling a shared golden semantic model from thin live-connected reports prevents measure duplication, reduces capacity memory footprint, and enforces centralized RLS/endorsement across teams. Local study-map skill 1.11 (Create and Update Reusable Assets (.pbit Templates, .pbids Data Sources, and Shared Golden Semantic Models)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create and use report templates (.pbit), data sources (.pbids), and shared semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-templates).

- **A:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: Connecting Power BI Desktop live to the shared `ClinicalEncounters` semantic model (`Build` permission) and publishing thin reports into departmental workspaces reuses one in-memory model.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Connecting Power BI Desktop live to the shared `ClinicalEncounters` semantic model (`Build` permission) and publishing thin reports into departmental workspaces reuses one in-memory model.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Connecting Power BI Desktop live to the shared `ClinicalEncounters` semantic model (`Build` permission) and publishing thin reports into departmental workspaces reuses one in-memory model.
- **D:** Correct. Decoupling a shared golden semantic model from thin live-connected reports prevents measure duplication, reduces capacity memory footprint, and enforces centralized RLS/endorsement across teams. In this scenario: Connecting Power BI Desktop live to the shared `ClinicalEncounters` semantic model (`Build` permission) and publishing thin reports into departmental workspaces reuses one in-memory model.

### Question 22 — A

Answer: Install an On-premises data gateway in High-Availability cluster mode on domain-joined servers inside the corporate network. Installing an `On-premises data gateway` in High-Availability cluster mode across two or more domain-joined servers provides resilient outbound-only connectivity without inbound firewall holes. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Local study-map skill 2.1 (Create Data Connections (Shareable Cloud Connections, On-Premises Gateways, and VNet Data Gateways)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data source management, cloud connections, and VNet/on-premises gateways in Fabric (https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management).

- **A:** Correct. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. In this scenario: Installing an `On-premises data gateway` in High-Availability cluster mode across two or more domain-joined servers provides resilient outbound-only connectivity without inbound firewall holes.
- **B:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Installing an `On-premises data gateway` in High-Availability cluster mode across two or more domain-joined servers provides resilient outbound-only connectivity without inbound firewall holes.
- **C:** Incorrect for this requirement. Shareable cloud connections centralize credentials/OAuth/Service Principal/Workspace Identity settings for public cloud sources and can be shared with specific users without exposing raw secrets. Why the keyed choice wins: Installing an `On-premises data gateway` in High-Availability cluster mode across two or more domain-joined servers provides resilient outbound-only connectivity without inbound firewall holes.
- **D:** Incorrect for this requirement. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. Why the keyed choice wins: Installing an `On-premises data gateway` in High-Availability cluster mode across two or more domain-joined servers provides resilient outbound-only connectivity without inbound firewall holes.

### Question 23 — D

Answer: Deploy a Virtual Network (VNet) data gateway injected into a delegated Azure VNet subnet. Deploying a managed `Virtual Network (VNet) data gateway` into a delegated subnet of `vnet-clinical-eastus` connects Fabric workloads to Azure private endpoints without IaaS VMs. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. Local study-map skill 2.1 (Create Data Connections (Shareable Cloud Connections, On-Premises Gateways, and VNet Data Gateways)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data source management, cloud connections, and VNet/on-premises gateways in Fabric (https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management).

- **A:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Deploying a managed `Virtual Network (VNet) data gateway` into a delegated subnet of `vnet-clinical-eastus` connects Fabric workloads to Azure private endpoints without IaaS VMs.
- **B:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Deploying a managed `Virtual Network (VNet) data gateway` into a delegated subnet of `vnet-clinical-eastus` connects Fabric workloads to Azure private endpoints without IaaS VMs.
- **C:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Deploying a managed `Virtual Network (VNet) data gateway` into a delegated subnet of `vnet-clinical-eastus` connects Fabric workloads to Azure private endpoints without IaaS VMs.
- **D:** Correct. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. In this scenario: Deploying a managed `Virtual Network (VNet) data gateway` into a delegated subnet of `vnet-clinical-eastus` connects Fabric workloads to Azure private endpoints without IaaS VMs.

### Question 24 — A, D

Answers: Use the OneLake catalog Explore tab to filter certified domain assets and the Govern tab to review endorsement, sensitivity, and stewardship posture; Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal. `OneLake catalog` (`Explore` and `Govern` tabs) paired with `Certified` endorsement filtering lets researchers locate vetted assets and stewards monitor label compliance centrally. Local study-map skill 2.2 (Discover Data and Streams Using OneLake Catalog (Explore/Govern) and Real-Time Hub + Activator), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake catalog overview & Real-Time hub in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview).

- **A:** Correct. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. In this scenario: `OneLake catalog` (`Explore` and `Govern` tabs) paired with `Certified` endorsement filtering lets researchers locate vetted assets and stewards monitor label compliance centrally.
- **B:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: `OneLake catalog` (`Explore` and `Govern` tabs) paired with `Certified` endorsement filtering lets researchers locate vetted assets and stewards monitor label compliance centrally.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `OneLake catalog` (`Explore` and `Govern` tabs) paired with `Certified` endorsement filtering lets researchers locate vetted assets and stewards monitor label compliance centrally.
- **D:** Correct. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. In this scenario: `OneLake catalog` (`Explore` and `Govern` tabs) paired with `Certified` endorsement filtering lets researchers locate vetted assets and stewards monitor label compliance centrally.
- **E:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: `OneLake catalog` (`Explore` and `Govern` tabs) paired with `Certified` endorsement filtering lets researchers locate vetted assets and stewards monitor label compliance centrally.

### Question 25 — A

Answer: Configure Fabric Database Mirroring from Azure SQL Database, Cosmos DB, Snowflake, or Azure Databricks Unity Catalog. `Fabric Database Mirroring` for Azure SQL Database replicates initial snapshots and ongoing transaction-log CDC changes into OneLake Delta tables automatically. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Correct. Database Mirroring continuously replicates source tables and CDC changes in near-real-time into OneLake Delta Parquet format with zero ETL code and automatic SQL analytics endpoint + Direct Lake readiness. In this scenario: `Fabric Database Mirroring` for Azure SQL Database replicates initial snapshots and ongoing transaction-log CDC changes into OneLake Delta tables automatically.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Fabric Database Mirroring` for Azure SQL Database replicates initial snapshots and ongoing transaction-log CDC changes into OneLake Delta tables automatically.
- **C:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `Fabric Database Mirroring` for Azure SQL Database replicates initial snapshots and ongoing transaction-log CDC changes into OneLake Delta tables automatically.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `Fabric Database Mirroring` for Azure SQL Database replicates initial snapshots and ongoing transaction-log CDC changes into OneLake Delta tables automatically.

### Question 26 — B

Answer: Create an external OneLake shortcut to ADLS Gen2, Amazon S3, Google Cloud Storage, or Dataverse with optional shortcut caching. Creating an external `OneLake shortcut` to Google Cloud Storage with **shortcut caching** enabled reads files virtually and caches frequently accessed files in OneLake. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Incorrect for this requirement. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. Why the keyed choice wins: Creating an external `OneLake shortcut` to Google Cloud Storage with **shortcut caching** enabled reads files virtually and caches frequently accessed files in OneLake.
- **B:** Correct. OneLake shortcuts virtualize external Delta/Parquet/Iceberg or file folders directly into a Lakehouse without copying pipelines, avoiding duplicate storage and scheduled batch sync jobs. In this scenario: Creating an external `OneLake shortcut` to Google Cloud Storage with **shortcut caching** enabled reads files virtually and caches frequently accessed files in OneLake.
- **C:** Incorrect for this requirement. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. Why the keyed choice wins: Creating an external `OneLake shortcut` to Google Cloud Storage with **shortcut caching** enabled reads files virtually and caches frequently accessed files in OneLake.
- **D:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: Creating an external `OneLake shortcut` to Google Cloud Storage with **shortcut caching** enabled reads files virtually and caches frequently accessed files in OneLake.

### Question 27 — A

Answer: Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table. A Fabric `Eventstream` connects natively to Azure IoT Hub, applies live stream operators, and routes output to Eventhouse and Lakehouse destinations concurrently. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Correct. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. In this scenario: A Fabric `Eventstream` connects natively to Azure IoT Hub, applies live stream operators, and routes output to Eventhouse and Lakehouse destinations concurrently.
- **B:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: A Fabric `Eventstream` connects natively to Azure IoT Hub, applies live stream operators, and routes output to Eventhouse and Lakehouse destinations concurrently.
- **C:** Incorrect for this requirement. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. Why the keyed choice wins: A Fabric `Eventstream` connects natively to Azure IoT Hub, applies live stream operators, and routes output to Eventhouse and Lakehouse destinations concurrently.
- **D:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: A Fabric `Eventstream` connects natively to Azure IoT Hub, applies live stream operators, and routes output to Eventhouse and Lakehouse destinations concurrently.

### Question 28 — A, B, C

Answers: Use a Data Factory Pipeline Copy activity (or Copy job) for high-throughput bulk movement of raw Parquet/CSV/SQL tables into OneLake; Use Dataflow Gen2 (CI/CD) with Fast Copy enabled and a Lakehouse/Warehouse destination for low-code Power Query M transformations; Create a Fabric Eventstream with no-code stream processing operators routing live events to an Eventhouse or Lakehouse Delta table. Pipeline `Copy activity` handles bulk raw transfers, `Dataflow Gen2` with Fast Copy handles low-code M merges, and `Eventstream` handles continuous Kafka routing. Local study-map skill 2.3 (Ingest or Access Data via OneLake Shortcuts, Database Mirroring, Copy Pipelines, Dataflow Gen2, Spark, and Eventstreams), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data ingestion options, OneLake shortcuts, and Database Mirroring in Fabric (https://learn.microsoft.com/en-us/fabric/data-engineering/load-data-lakehouse).

- **A:** Correct. Eventstream ingests high-velocity Kafka, Azure Event Hubs, IoT Hub, or CDC streams, applies live windowing/filtering/routing, and lands events continuously in Eventhouse or Lakehouse. In this scenario: Pipeline `Copy activity` handles bulk raw transfers, `Dataflow Gen2` with Fast Copy handles low-code M merges, and `Eventstream` handles continuous Kafka routing.
- **B:** Correct. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. In this scenario: Pipeline `Copy activity` handles bulk raw transfers, `Dataflow Gen2` with Fast Copy handles low-code M merges, and `Eventstream` handles continuous Kafka routing.
- **C:** Correct. Dataflow Gen2 provides 300+ connectors and visual Power Query M transformations, while Fast Copy delegates bulk ingestion to the Copy backend before staging transformations. In this scenario: Pipeline `Copy activity` handles bulk raw transfers, `Dataflow Gen2` with Fast Copy handles low-code M merges, and `Eventstream` handles continuous Kafka routing.
- **D:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Pipeline `Copy activity` handles bulk raw transfers, `Dataflow Gen2` with Fast Copy handles low-code M merges, and `Eventstream` handles continuous Kafka routing.
- **E:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Pipeline `Copy activity` handles bulk raw transfers, `Dataflow Gen2` with Fast Copy handles low-code M merges, and `Eventstream` handles continuous Kafka routing.
- **F:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Pipeline `Copy activity` handles bulk raw transfers, `Dataflow Gen2` with Fast Copy handles low-code M merges, and `Eventstream` handles continuous Kafka routing.

### Question 29 — B

Answer: Choose a Fabric Eventhouse (KQL database). `Fabric Eventhouse` (KQL database) automatically indexes time-series, semi-structured JSON, and free-text telemetry for ultra-fast KQL analytics. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Incorrect for this requirement. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) automatically indexes time-series, semi-structured JSON, and free-text telemetry for ultra-fast KQL analytics.
- **B:** Correct. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. In this scenario: `Fabric Eventhouse` (KQL database) automatically indexes time-series, semi-structured JSON, and free-text telemetry for ultra-fast KQL analytics.
- **C:** Incorrect for this requirement. SQL database in Fabric hosts operational/transactional OLTP workloads (powered by Azure SQL DB engine) and automatically mirrors operational tables into OneLake for near-real-time analytics. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) automatically indexes time-series, semi-structured JSON, and free-text telemetry for ultra-fast KQL analytics.
- **D:** Incorrect for this requirement. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. Why the keyed choice wins: `Fabric Eventhouse` (KQL database) automatically indexes time-series, semi-structured JSON, and free-text telemetry for ultra-fast KQL analytics.

### Question 30 — B

Answer: Choose a Fabric Data Warehouse. The Lakehouse SQL analytics endpoint is read-only for T-SQL DML; choosing a `Fabric Data Warehouse` provides full multi-table transactional T-SQL `INSERT`/`UPDATE`/`DELETE`/`MERGE`. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: The Lakehouse SQL analytics endpoint is read-only for T-SQL DML; choosing a `Fabric Data Warehouse` provides full multi-table transactional T-SQL `INSERT`/`UPDATE`/`DELETE`/`MERGE`.
- **B:** Correct. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. In this scenario: The Lakehouse SQL analytics endpoint is read-only for T-SQL DML; choosing a `Fabric Data Warehouse` provides full multi-table transactional T-SQL `INSERT`/`UPDATE`/`DELETE`/`MERGE`.
- **C:** Incorrect for this requirement. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Why the keyed choice wins: The Lakehouse SQL analytics endpoint is read-only for T-SQL DML; choosing a `Fabric Data Warehouse` provides full multi-table transactional T-SQL `INSERT`/`UPDATE`/`DELETE`/`MERGE`.
- **D:** Incorrect for this requirement. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. Why the keyed choice wins: The Lakehouse SQL analytics endpoint is read-only for T-SQL DML; choosing a `Fabric Data Warehouse` provides full multi-table transactional T-SQL `INSERT`/`UPDATE`/`DELETE`/`MERGE`.

### Question 31 — D, E

Answers: Choose a Fabric Lakehouse; Choose a Fabric Data Warehouse. `Lakehouse` handles unstructured `Files/` + PySpark Silver engineering, while `Warehouse` serves transactional T-SQL Gold star schemas — sharing data zero-copy across OneLake. Local study-map skill 2.4 (Choose Between Fabric Data Stores (Lakehouse, Warehouse, Eventhouse/KQL DB, and SQL Database in Fabric)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Microsoft Fabric decision guide: choose a data store (Lakehouse, Warehouse, Eventhouse, SQL DB) (https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-data-store).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Lakehouse` handles unstructured `Files/` + PySpark Silver engineering, while `Warehouse` serves transactional T-SQL Gold star schemas — sharing data zero-copy across OneLake.
- **B:** Incorrect for this requirement. Eventhouse KQL databases do not write Delta Parquet to OneLake unless OneLake availability is enabled, and Direct Lake on SQL does not support KQL databases (only Direct Lake on OneLake does once OneLake availability is on). Why the keyed choice wins: `Lakehouse` handles unstructured `Files/` + PySpark Silver engineering, while `Warehouse` serves transactional T-SQL Gold star schemas — sharing data zero-copy across OneLake.
- **C:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `Lakehouse` handles unstructured `Files/` + PySpark Silver engineering, while `Warehouse` serves transactional T-SQL Gold star schemas — sharing data zero-copy across OneLake.
- **D:** Correct. Lakehouse combines unstructured/semi-structured Files folders and managed Delta Parquet Tables engineered via Spark/Python/Scala/Spark SQL/Dataflows, paired with an automatic read-only T-SQL analytics endpoint. In this scenario: `Lakehouse` handles unstructured `Files/` + PySpark Silver engineering, while `Warehouse` serves transactional T-SQL Gold star schemas — sharing data zero-copy across OneLake.
- **E:** Correct. Fabric Data Warehouse provides a full transactional T-SQL engine supporting multi-table ACID transactions (BEGIN TRAN/COMMIT), DDL/DML writes, cross-database SQL queries, and native SQL RLS/CLS/DDM stored as Delta Parquet in OneLake. In this scenario: `Lakehouse` handles unstructured `Files/` + PySpark Silver engineering, while `Warehouse` serves transactional T-SQL Gold star schemas — sharing data zero-copy across OneLake.

### Question 32 — D

Answer: Enable OneLake availability on the Eventhouse KQL database (or specific KQL table) and create an internal OneLake shortcut in the Lakehouse. Turning on `OneLake availability` syncs KQL table data into OneLake Delta Parquet format so Lakehouse shortcuts, Spark, SQL endpoints, and Direct Lake on OneLake models read it directly. KQL databases do not write Delta Parquet to OneLake by default; turning on OneLake availability creates a synced Delta Parquet logical representation in OneLake that Spark, SQL analytics endpoints, and Direct Lake on OneLake models can read without data movement. Local study-map skill 2.5 (Implement OneLake Integration for Eventhouse (OneLake Availability) and Import Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Eventhouse OneLake availability & OneLake integration for semantic models (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/one-lake-availability).

- **A:** Incorrect for this requirement. Eventhouse KQL databases do not write Delta Parquet to OneLake unless OneLake availability is enabled, and Direct Lake on SQL does not support KQL databases (only Direct Lake on OneLake does once OneLake availability is on). Why the keyed choice wins: Turning on `OneLake availability` syncs KQL table data into OneLake Delta Parquet format so Lakehouse shortcuts, Spark, SQL endpoints, and Direct Lake on OneLake models read it directly.
- **B:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: Turning on `OneLake availability` syncs KQL table data into OneLake Delta Parquet format so Lakehouse shortcuts, Spark, SQL endpoints, and Direct Lake on OneLake models read it directly.
- **C:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Turning on `OneLake availability` syncs KQL table data into OneLake Delta Parquet format so Lakehouse shortcuts, Spark, SQL endpoints, and Direct Lake on OneLake models read it directly.
- **D:** Correct. KQL databases do not write Delta Parquet to OneLake by default; turning on OneLake availability creates a synced Delta Parquet logical representation in OneLake that Spark, SQL analytics endpoints, and Direct Lake on OneLake models can read without data movement. In this scenario: Turning on `OneLake availability` syncs KQL table data into OneLake Delta Parquet format so Lakehouse shortcuts, Spark, SQL endpoints, and Direct Lake on OneLake models read it directly.

### Question 33 — B

Answer: Ingest streaming telemetry into an Eventhouse KQL database → Enable OneLake availability on the KQL database or table → Create an internal OneLake shortcut in the Lakehouse → Add the table to a Direct Lake on OneLake semantic model. Landing events in Eventhouse, enabling `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and adding the table to Direct Lake on OneLake avoids manual exports and unsupported SQL-endpoint Direct Lake paths. Correct order: land streaming events in Eventhouse, opt in to OneLake availability so Delta Parquet files sync to OneLake, surface via Lakehouse shortcut (or connect directly), and model with Direct Lake on OneLake. Local study-map skill 2.5 (Implement OneLake Integration for Eventhouse (OneLake Availability) and Import Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Eventhouse OneLake availability & OneLake integration for semantic models (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/one-lake-availability).

- **A:** Incorrect for this requirement. Incorrect: manual hourly CSV exports add latency, operational toil, and duplicate storage instead of native Eventhouse OneLake availability. Why the keyed choice wins: Landing events in Eventhouse, enabling `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and adding the table to Direct Lake on OneLake avoids manual exports and unsupported SQL-endpoint Direct Lake paths.
- **B:** Correct. Correct order: land streaming events in Eventhouse, opt in to OneLake availability so Delta Parquet files sync to OneLake, surface via Lakehouse shortcut (or connect directly), and model with Direct Lake on OneLake. In this scenario: Landing events in Eventhouse, enabling `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and adding the table to Direct Lake on OneLake avoids manual exports and unsupported SQL-endpoint Direct Lake paths.
- **C:** Incorrect for this requirement. Incorrect: KQL tables are internal OneLake sources that only expose Delta Parquet folders after OneLake availability is enabled. Why the keyed choice wins: Landing events in Eventhouse, enabling `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and adding the table to Direct Lake on OneLake avoids manual exports and unsupported SQL-endpoint Direct Lake paths.
- **D:** Incorrect for this requirement. Incorrect: Direct Lake on SQL does not support KQL databases, disabling OneLake availability prevents Delta Parquet generation, and Direct Lake never uses gateways. Why the keyed choice wins: Landing events in Eventhouse, enabling `OneLake availability`, creating an internal OneLake shortcut in the Lakehouse, and adding the table to Direct Lake on OneLake avoids manual exports and unsupported SQL-endpoint Direct Lake paths.

### Question 34 — C

Answer: Create parameterized T-SQL stored procedures and views in the Fabric Warehouse to encapsulate repeatable Gold-layer ELT logic. Adding a `Stored procedure` activity in the Data Factory pipeline connected to `ClaimsWarehouse` passes `@BatchId` dynamically and executes the T-SQL ELT transaction natively. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Adding a `Stored procedure` activity in the Data Factory pipeline connected to `ClaimsWarehouse` passes `@BatchId` dynamically and executes the T-SQL ELT transaction natively.
- **B:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: Adding a `Stored procedure` activity in the Data Factory pipeline connected to `ClaimsWarehouse` passes `@BatchId` dynamically and executes the T-SQL ELT transaction natively.
- **C:** Correct. Fabric Warehouse supports full T-SQL CREATE PROCEDURE, CREATE VIEW, and inline table-valued functions to modularize staging, validation, and dimension/fact loads orchestrated from Data Factory pipelines. In this scenario: Adding a `Stored procedure` activity in the Data Factory pipeline connected to `ClaimsWarehouse` passes `@BatchId` dynamically and executes the T-SQL ELT transaction natively.
- **D:** Incorrect for this requirement. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Why the keyed choice wins: Adding a `Stored procedure` activity in the Data Factory pipeline connected to `ClaimsWarehouse` passes `@BatchId` dynamically and executes the T-SQL ELT transaction natively.

### Question 35 — B

Answer: Use a Lakehouse Materialized Lake View (or persisted Gold Delta table) instead of a non-materialized SQL analytics endpoint view for Direct Lake on OneLake. Replacing the non-materialized SQL view with a persisted Gold Delta table or Lakehouse `Materialized Lake View` allows Direct Lake to load physical Delta Parquet columns directly into memory. Non-materialized SQL analytics endpoint views cannot back Direct Lake on OneLake tables and force Direct Lake on SQL into DirectQuery fallback; materializing the view as a Delta table preserves pure in-memory Direct Lake speed. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Replacing the non-materialized SQL view with a persisted Gold Delta table or Lakehouse `Materialized Lake View` allows Direct Lake to load physical Delta Parquet columns directly into memory.
- **B:** Correct. Non-materialized SQL analytics endpoint views cannot back Direct Lake on OneLake tables and force Direct Lake on SQL into DirectQuery fallback; materializing the view as a Delta table preserves pure in-memory Direct Lake speed. In this scenario: Replacing the non-materialized SQL view with a persisted Gold Delta table or Lakehouse `Materialized Lake View` allows Direct Lake to load physical Delta Parquet columns directly into memory.
- **C:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: Replacing the non-materialized SQL view with a persisted Gold Delta table or Lakehouse `Materialized Lake View` allows Direct Lake to load physical Delta Parquet columns directly into memory.
- **D:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Replacing the non-materialized SQL view with a persisted Gold Delta table or Lakehouse `Materialized Lake View` allows Direct Lake to load physical Delta Parquet columns directly into memory.

### Question 36 — A

Answer: Use T-SQL GRANT/DENY SELECT on specific Warehouse schemas, tables, or views. Using T-SQL `GRANT` on the curated view paired with `DENY` (or withholding permissions) on the raw base schema/table enforces object-level security cleanly in the Warehouse. Object-level security in Fabric Warehouse or SQL analytics endpoints controls visibility and query access to entire tables, views, or stored procedures using standard T-SQL GRANT and DENY permissions. Local study-map skill 2.6 (Create T-SQL Views, Inline Table-Valued Functions, Stored Procedures, and Materialized Lake Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Create tables, views, functions, and stored procedures in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/t-sql-surface-area).

- **A:** Correct. Object-level security in Fabric Warehouse or SQL analytics endpoints controls visibility and query access to entire tables, views, or stored procedures using standard T-SQL GRANT and DENY permissions. In this scenario: Using T-SQL `GRANT` on the curated view paired with `DENY` (or withholding permissions) on the raw base schema/table enforces object-level security cleanly in the Warehouse.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Using T-SQL `GRANT` on the curated view paired with `DENY` (or withholding permissions) on the raw base schema/table enforces object-level security cleanly in the Warehouse.
- **C:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Using T-SQL `GRANT` on the curated view paired with `DENY` (or withholding permissions) on the raw base schema/table enforces object-level security cleanly in the Warehouse.
- **D:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Using T-SQL `GRANT` on the curated view paired with `DENY` (or withholding permissions) on the raw base schema/table enforces object-level security cleanly in the Warehouse.

### Question 37 — D

Answer: Generate deterministic or sequential integer surrogate keys (for example ROW_NUMBER() + MAX(Key) in T-SQL or monotonically_increasing_id / hash in Spark) on Gold dimensions. Single-column integer surrogate keys dramatically shrink fact foreign-key dictionary size in Delta Parquet and VertiPaq while supporting SCD Type 2 patient demographic history. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Single-column integer surrogate keys dramatically shrink fact foreign-key dictionary size in Delta Parquet and VertiPaq while supporting SCD Type 2 patient demographic history.
- **B:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: Single-column integer surrogate keys dramatically shrink fact foreign-key dictionary size in Delta Parquet and VertiPaq while supporting SCD Type 2 patient demographic history.
- **C:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Single-column integer surrogate keys dramatically shrink fact foreign-key dictionary size in Delta Parquet and VertiPaq while supporting SCD Type 2 patient demographic history.
- **D:** Correct. Integer surrogate keys decouple analytical dimensions from mutable or composite operational natural keys, support SCD Type 2 versioning, and compress efficiently in Delta Parquet and VertiPaq. In this scenario: Single-column integer surrogate keys dramatically shrink fact foreign-key dictionary size in Delta Parquet and VertiPaq while supporting SCD Type 2 patient demographic history.

### Question 38 — B

Answer: Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes. Creating a conformed `DimCalendar` table with daily grain, flu-season week attributes, and holiday flags provides a single date dimension shared across all clinical dates. A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. Why the keyed choice wins: Creating a conformed `DimCalendar` table with daily grain, flu-season week attributes, and holiday flags provides a single date dimension shared across all clinical dates.
- **B:** Correct. A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering. In this scenario: Creating a conformed `DimCalendar` table with daily grain, flu-season week attributes, and holiday flags provides a single date dimension shared across all clinical dates.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Creating a conformed `DimCalendar` table with daily grain, flu-season week attributes, and holiday flags provides a single date dimension shared across all clinical dates.
- **D:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Creating a conformed `DimCalendar` table with daily grain, flu-season week attributes, and holiday flags provides a single date dimension shared across all clinical dates.

### Question 39 — C, E

Answers: Use PySpark DataFrame .withColumn() with built-in pyspark.sql.functions instead of row-by-row Python UDFs; Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes. Vectorized `.withColumn()` expressions using `pyspark.sql.functions.when` compute `BMICategory` at native Catalyst speed, and a dedicated Gold Calendar dimension provides study-week attributes. Local study-map skill 2.7 (Enrich Data by Adding Surrogate Keys, Conformed Calendar Tables, and Vectorized PySpark/SQL/M Columns), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Tutorial: Transform and enrich data in Lakehouse / Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-transform-data).

- **A:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Vectorized `.withColumn()` expressions using `pyspark.sql.functions.when` compute `BMICategory` at native Catalyst speed, and a dedicated Gold Calendar dimension provides study-week attributes.
- **B:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Vectorized `.withColumn()` expressions using `pyspark.sql.functions.when` compute `BMICategory` at native Catalyst speed, and a dedicated Gold Calendar dimension provides study-week attributes.
- **C:** Correct. Native Catalyst/Photon-optimized pyspark.sql.functions execute in vectorized JVM/native code across partitions, avoiding the severe Python serialization bottleneck of row-level UDFs. In this scenario: Vectorized `.withColumn()` expressions using `pyspark.sql.functions.when` compute `BMICategory` at native Catalyst speed, and a dedicated Gold Calendar dimension provides study-week attributes.
- **D:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Vectorized `.withColumn()` expressions using `pyspark.sql.functions.when` compute `BMICategory` at native Catalyst speed, and a dedicated Gold Calendar dimension provides study-week attributes.
- **E:** Correct. A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering. In this scenario: Vectorized `.withColumn()` expressions using `pyspark.sql.functions.when` compute `BMICategory` at native Catalyst speed, and a dedicated Gold Calendar dimension provides study-week attributes.

### Question 40 — C

Answer: Implement a Slowly Changing Dimension Type 2 (SCD Type 2) with SurrogateKey, NaturalKey, EffectiveStartDate, EffectiveEndDate, and IsCurrent columns. `SCD Type 2` inserts a new `DimPhysician` row with a new `PhysicianKey` and `EffectiveStartDate = '2026-07-01'` while closing out the prior `Cardiology` row. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Why the keyed choice wins: `SCD Type 2` inserts a new `DimPhysician` row with a new `PhysicianKey` and `EffectiveStartDate = '2026-07-01'` while closing out the prior `Cardiology` row.
- **B:** Incorrect for this requirement. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Why the keyed choice wins: `SCD Type 2` inserts a new `DimPhysician` row with a new `PhysicianKey` and `EffectiveStartDate = '2026-07-01'` while closing out the prior `Cardiology` row.
- **C:** Correct. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. In this scenario: `SCD Type 2` inserts a new `DimPhysician` row with a new `PhysicianKey` and `EffectiveStartDate = '2026-07-01'` while closing out the prior `Cardiology` row.
- **D:** Incorrect for this requirement. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Why the keyed choice wins: `SCD Type 2` inserts a new `DimPhysician` row with a new `PhysicianKey` and `EffectiveStartDate = '2026-07-01'` while closing out the prior `Cardiology` row.

### Question 41 — B

Answer: Implement a Slowly Changing Dimension Type 1 (SCD Type 1) overwriting changed dimension attributes in place. `SCD Type 1` overwrites the misspelled `FacilityName` attribute in place on the existing surrogate key so historical and current facts reflect the corrected label. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. Why the keyed choice wins: `SCD Type 1` overwrites the misspelled `FacilityName` attribute in place on the existing surrogate key so historical and current facts reflect the corrected label.
- **B:** Correct. SCD Type 1 updates attribute values directly without creating new surrogate keys — appropriate for correcting typos or when business rules intentionally restate history under current attributes. In this scenario: `SCD Type 1` overwrites the misspelled `FacilityName` attribute in place on the existing surrogate key so historical and current facts reflect the corrected label.
- **C:** Incorrect for this requirement. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. Why the keyed choice wins: `SCD Type 1` overwrites the misspelled `FacilityName` attribute in place on the existing surrogate key so historical and current facts reflect the corrected label.
- **D:** Incorrect for this requirement. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. Why the keyed choice wins: `SCD Type 1` overwrites the misspelled `FacilityName` attribute in place on the existing surrogate key so historical and current facts reflect the corrected label.

### Question 42 — B

Answer: Stage and deduplicate incoming records by natural key → Compare tracked attributes against active (IsCurrent = 1) Gold rows → Expire changed active rows (EffectiveEndDate, IsCurrent = 0) → Insert new active versions with fresh surrogate keys. Deduplicating staged plans, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active versions with fresh surrogate keys maintains point-in-time integrity. Correct order: deduplicate staging first, detect attribute changes against current rows, close out prior active intervals without losing their surrogate keys, and insert new active versions. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. Incorrect: deleting unmatched keys and enabling Assume referential integrity omits orphan rows silently in INNER JOINs. Why the keyed choice wins: Deduplicating staged plans, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active versions with fresh surrogate keys maintains point-in-time integrity.
- **B:** Correct. Correct order: deduplicate staging first, detect attribute changes against current rows, close out prior active intervals without losing their surrogate keys, and insert new active versions. In this scenario: Deduplicating staged plans, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active versions with fresh surrogate keys maintains point-in-time integrity.
- **C:** Incorrect for this requirement. Incorrect: new versions must be active (IsCurrent = 1), EffectiveStartDate of historical intervals must remain immutable, and natural keys are required to match future CDC updates. Why the keyed choice wins: Deduplicating staged plans, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active versions with fresh surrogate keys maintains point-in-time integrity.
- **D:** Incorrect for this requirement. Incorrect: regenerating surrogate keys on truncate breaks every existing historical fact foreign key, and marking multiple rows IsCurrent = 1 duplicates fact joins. Why the keyed choice wins: Deduplicating staged plans, comparing tracked attributes against active `IsCurrent = 1` rows, expiring changed rows, and inserting new active versions with fresh surrogate keys maintains point-in-time integrity.

### Question 43 — C, D, E

Answers: Organize OneLake into Bronze (raw immutable), Silver (validated, deduplicated, conformed), and Gold (star-schema dimensions and facts with V-Order); Define an explicit atomic transaction grain on the fact table storing only foreign surrogate keys, degenerate identifiers, and additive numeric measures; Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE. Separating Bronze/Silver/Gold layers, keeping `FactClaimLines` at strict single-line atomic grain, and mapping unmatched foreign keys to `-1` Unknown dimension members guarantee clean `1:*` star joins. Local study-map skill 2.8 (Implement a Star Schema for a Lakehouse or Warehouse (Medallion Layers, Fact Grain, SCD Type 1 & Type 2)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Understand star schema and the importance for Power BI & Fabric (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).

- **A:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Separating Bronze/Silver/Gold layers, keeping `FactClaimLines` at strict single-line atomic grain, and mapping unmatched foreign keys to `-1` Unknown dimension members guarantee clean `1:*` star joins.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Separating Bronze/Silver/Gold layers, keeping `FactClaimLines` at strict single-line atomic grain, and mapping unmatched foreign keys to `-1` Unknown dimension members guarantee clean `1:*` star joins.
- **C:** Correct. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. In this scenario: Separating Bronze/Silver/Gold layers, keeping `FactClaimLines` at strict single-line atomic grain, and mapping unmatched foreign keys to `-1` Unknown dimension members guarantee clean `1:*` star joins.
- **D:** Correct. The Medallion architecture separates raw source fidelity (Bronze), enterprise data quality/conformance (Silver), and BI/Direct Lake star-schema consumption (Gold). In this scenario: Separating Bronze/Silver/Gold layers, keeping `FactClaimLines` at strict single-line atomic grain, and mapping unmatched foreign keys to `-1` Unknown dimension members guarantee clean `1:*` star joins.
- **E:** Correct. Keeping fact tables at a single, consistent atomic grain with integer foreign keys and additive measures eliminates double-counting and supports flexible rollups across every conformed dimension. In this scenario: Separating Bronze/Silver/Gold layers, keeping `FactClaimLines` at strict single-line atomic grain, and mapping unmatched foreign keys to `-1` Unknown dimension members guarantee clean `1:*` star joins.
- **F:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Separating Bronze/Silver/Gold layers, keeping `FactClaimLines` at strict single-line atomic grain, and mapping unmatched foreign keys to `-1` Unknown dimension members guarantee clean `1:*` star joins.

### Question 44 — D

Answer: Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension. Denormalizing `TherapeuticSubclass`, `TherapeuticClass`, and `FormularyTier` columns directly onto a flat `DimMedication` table eliminates three snowflake join hops. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Local study-map skill 2.9 (Denormalize Snowflake Hierarchies into Flattened Gold Dimension Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Dimensional modeling & denormalizing snowflake tables in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables).

- **A:** Incorrect for this requirement. Eventhouse is optimized for high-velocity, append-heavy time-series telemetry, semi-structured JSON logs, geospatial functions, and sub-second KQL analytics over billions of streaming events. Why the keyed choice wins: Denormalizing `TherapeuticSubclass`, `TherapeuticClass`, and `FormularyTier` columns directly onto a flat `DimMedication` table eliminates three snowflake join hops.
- **B:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Denormalizing `TherapeuticSubclass`, `TherapeuticClass`, and `FormularyTier` columns directly onto a flat `DimMedication` table eliminates three snowflake join hops.
- **C:** Incorrect for this requirement. SCD Type 2 inserts a new dimension row with a fresh surrogate key whenever tracked attributes change and expires the prior row, preserving historically accurate point-in-time attribution for old fact records. Why the keyed choice wins: Denormalizing `TherapeuticSubclass`, `TherapeuticClass`, and `FormularyTier` columns directly onto a flat `DimMedication` table eliminates three snowflake join hops.
- **D:** Correct. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. In this scenario: Denormalizing `TherapeuticSubclass`, `TherapeuticClass`, and `FormularyTier` columns directly onto a flat `DimMedication` table eliminates three snowflake join hops.

### Question 45 — D

Answer: Denormalize ProductSubcategory and ProductCategory attributes directly onto DimProduct so the fact table joins to a single flat dimension. Flattening `HealthSystem` and `GeographicDivision` into `DimHospital` removes chained dimension-to-dimension relationship hops in VertiPaq/Direct Lake. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Local study-map skill 2.9 (Denormalize Snowflake Hierarchies into Flattened Gold Dimension Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Dimensional modeling & denormalizing snowflake tables in Fabric Data Warehouse (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables).

- **A:** Incorrect for this requirement. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Why the keyed choice wins: Flattening `HealthSystem` and `GeographicDivision` into `DimHospital` removes chained dimension-to-dimension relationship hops in VertiPaq/Direct Lake.
- **B:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Flattening `HealthSystem` and `GeographicDivision` into `DimHospital` removes chained dimension-to-dimension relationship hops in VertiPaq/Direct Lake.
- **C:** Incorrect for this requirement. Granular TMSL / Enhanced Refresh commands over XMLA allow refreshing a single partition, running dataOnly without recalculating hierarchies, or running calculate/clearValues independently of full model reloads. Why the keyed choice wins: Flattening `HealthSystem` and `GeographicDivision` into `DimHospital` removes chained dimension-to-dimension relationship hops in VertiPaq/Direct Lake.
- **D:** Correct. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. In this scenario: Flattening `HealthSystem` and `GeographicDivision` into `DimHospital` removes chained dimension-to-dimension relationship hops in VertiPaq/Direct Lake.

### Question 46 — C

Answer: Create pre-aggregated Gold summary Delta tables at the daily/store/category grain using GROUP BY (or GROUPING SETS / ROLLUP). Pre-aggregating 1-second sensor rows into an hourly `FactBedVitalsHourly` Gold Delta table (`GROUP BY PatientKey, BedKey, ReadingHour`) shrinks 3,600 rows per hour to 1 row. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Pre-aggregating 1-second sensor rows into an hourly `FactBedVitalsHourly` Gold Delta table (`GROUP BY PatientKey, BedKey, ReadingHour`) shrinks 3,600 rows per hour to 1 row.
- **B:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: Pre-aggregating 1-second sensor rows into an hourly `FactBedVitalsHourly` Gold Delta table (`GROUP BY PatientKey, BedKey, ReadingHour`) shrinks 3,600 rows per hour to 1 row.
- **C:** Correct. Pre-aggregating multi-billion-row telemetry or clickstream facts into compact Gold summary tables slashes Direct Lake memory footprint, CU consumption, and high-level executive dashboard latency. In this scenario: Pre-aggregating 1-second sensor rows into an hourly `FactBedVitalsHourly` Gold Delta table (`GROUP BY PatientKey, BedKey, ReadingHour`) shrinks 3,600 rows per hour to 1 row.
- **D:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Pre-aggregating 1-second sensor rows into an hourly `FactBedVitalsHourly` Gold Delta table (`GROUP BY PatientKey, BedKey, ReadingHour`) shrinks 3,600 rows per hour to 1 row.

### Question 47 — A

Answer: GROUP BY GROUPING SETS ((RouteId, Borough), (Borough), ()). `GROUP BY GROUPING SETS ((Facility, ServiceLine), (Facility), ())` — using the `GROUPING SETS` operator — computes exact multi-grain subtotals in a single scan. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Correct. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. In this scenario: `GROUP BY GROUPING SETS ((Facility, ServiceLine), (Facility), ())` — using the `GROUPING SETS` operator — computes exact multi-grain subtotals in a single scan.
- **B:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `GROUP BY GROUPING SETS ((Facility, ServiceLine), (Facility), ())` — using the `GROUPING SETS` operator — computes exact multi-grain subtotals in a single scan.
- **C:** Incorrect for this requirement. In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key. Why the keyed choice wins: `GROUP BY GROUPING SETS ((Facility, ServiceLine), (Facility), ())` — using the `GROUPING SETS` operator — computes exact multi-grain subtotals in a single scan.
- **D:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `GROUP BY GROUPING SETS ((Facility, ServiceLine), (Facility), ())` — using the `GROUPING SETS` operator — computes exact multi-grain subtotals in a single scan.

### Question 48 — B

Answer: Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled. When query folding stays intact, the Warehouse SQL engine executes `GROUP BY` natively and transfers only 40,000 aggregated rows instead of streaming 90 million raw rows into the Dataflow mashup engine. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. Local study-map skill 2.10 (Aggregate Data Using SQL GROUP BY/ROLLUP/GROUPING SETS, Spark Aggregations, and Gold Summary Tables), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Aggregate data in Spark, T-SQL, and Dataflow Gen2 in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables).

- **A:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: When query folding stays intact, the Warehouse SQL engine executes `GROUP BY` natively and transfers only 40,000 aggregated rows instead of streaming 90 million raw rows into the Dataflow mashup engine.
- **B:** Correct. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. In this scenario: When query folding stays intact, the Warehouse SQL engine executes `GROUP BY` natively and transfers only 40,000 aggregated rows instead of streaming 90 million raw rows into the Dataflow mashup engine.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: When query folding stays intact, the Warehouse SQL engine executes `GROUP BY` natively and transfers only 40,000 aggregated rows instead of streaming 90 million raw rows into the Dataflow mashup engine.
- **D:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: When query folding stays intact, the Warehouse SQL engine executes `GROUP BY` natively and transfers only 40,000 aggregated rows instead of streaming 90 million raw rows into the Dataflow mashup engine.

### Question 49 — D

Answer: WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET. `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only rows whose payload actually changed, minimizing write amplification in OneLake. Guarding WHEN MATCHED with a hash/attribute inequality prevents rewriting unchanged Delta Parquet files on untouched rows during incremental upserts. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. Fabric Data Warehouse supports FILTER PREDICATE with inline TVFs (not stored procedures or SQL Server DML BLOCK PREDICATE triggers). Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only rows whose payload actually changed, minimizing write amplification in OneLake.
- **B:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only rows whose payload actually changed, minimizing write amplification in OneLake.
- **C:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only rows whose payload actually changed, minimizing write amplification in OneLake.
- **D:** Correct. Guarding WHEN MATCHED with a hash/attribute inequality prevents rewriting unchanged Delta Parquet files on untouched rows during incremental upserts. In this scenario: `WHEN MATCHED AND target.RowHash <> source.RowHash THEN UPDATE SET` updates only rows whose payload actually changed, minimizing write amplification in OneLake.

### Question 50 — C

Answer: Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table. A `Left Anti Join` (or T-SQL `NOT EXISTS`) between `FactLabResults` and `DimProvider` isolates orphan records with no matching provider key. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Incorrect for this requirement. Flattening multi-hop snowflake dimension chains into one denormalized Gold dimension eliminates chained joins in SQL/Spark and removes multi-hop relationship overhead in Direct Lake and Import semantic models. Why the keyed choice wins: A `Left Anti Join` (or T-SQL `NOT EXISTS`) between `FactLabResults` and `DimProvider` isolates orphan records with no matching provider key.
- **B:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: A `Left Anti Join` (or T-SQL `NOT EXISTS`) between `FactLabResults` and `DimProvider` isolates orphan records with no matching provider key.
- **C:** Correct. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. In this scenario: A `Left Anti Join` (or T-SQL `NOT EXISTS`) between `FactLabResults` and `DimProvider` isolates orphan records with no matching provider key.
- **D:** Incorrect for this requirement. Delta Lake MERGE INTO (in Spark SQL, PySpark DeltaTable.forPath().merge(), or Warehouse T-SQL) atomically applies incremental CDC inserts, updates, and soft-deletes in a single ACID transaction. Why the keyed choice wins: A `Left Anti Join` (or T-SQL `NOT EXISTS`) between `FactLabResults` and `DimProvider` isolates orphan records with no matching provider key.

### Question 51 — A, E

Answers: fact_df.join(F.broadcast(dim_store_df), on="StoreKey", how="left"); Use a Left Anti Join (or T-SQL NOT EXISTS) between staging records and the target dimension/fact table. `F.broadcast(dim_chromosome)` avoids shuffling the large DataFrame, and a `left_anti` join isolates rows missing from `dim_genome` for quarantine. Local study-map skill 2.11 (Merge or Join Data Using Delta MERGE INTO Upserts, Anti-Joins, Power Query Merge, and Spark Broadcast Joins), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Merge and join data with Delta Lake MERGE INTO, T-SQL, and Power Query (https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-table-maintenance).

- **A:** Correct. Wrapping the small dimension DataFrame in pyspark.sql.functions.broadcast() avoids shuffling the multi-hundred-million-row fact DataFrame across Spark executors. In this scenario: `F.broadcast(dim_chromosome)` avoids shuffling the large DataFrame, and a `left_anti` join isolates rows missing from `dim_genome` for quarantine.
- **B:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `F.broadcast(dim_chromosome)` avoids shuffling the large DataFrame, and a `left_anti` join isolates rows missing from `dim_genome` for quarantine.
- **C:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `F.broadcast(dim_chromosome)` avoids shuffling the large DataFrame, and a `left_anti` join isolates rows missing from `dim_genome` for quarantine.
- **D:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: `F.broadcast(dim_chromosome)` avoids shuffling the large DataFrame, and a `left_anti` join isolates rows missing from `dim_genome` for quarantine.
- **E:** Correct. A Left Anti Join returns only rows from the left dataset that have zero matches on the right — ideal for isolating brand-new dimension members or orphan fact foreign keys. In this scenario: `F.broadcast(dim_chromosome)` avoids shuffling the large DataFrame, and a `left_anti` join isolates rows missing from `dim_genome` for quarantine.

### Question 52 — C

Answer: ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC). `ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)` assigns a unique sequential integer `1` to the latest record per entity even on timestamp ties. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. GROUPING SETS computes exact specified subtotal combinations and the grand total () in a single table scan without UNION ALL passes. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)` assigns a unique sequential integer `1` to the latest record per entity even on timestamp ties.
- **B:** Incorrect for this requirement. Omitting PARTITION BY ranks across the entire table globally rather than per entity, and RANK() returns duplicate rank-1 rows on exact timestamp ties. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)` assigns a unique sequential integer `1` to the latest record per entity even on timestamp ties.
- **C:** Correct. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. In this scenario: `ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)` assigns a unique sequential integer `1` to the latest record per entity even on timestamp ties.
- **D:** Incorrect for this requirement. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Why the keyed choice wins: `ROW_NUMBER() OVER (PARTITION BY SpecimenId ORDER BY EventTimestamp DESC)` assigns a unique sequential integer `1` to the latest record per entity even on timestamp ties.

### Question 53 — D, E

Answers: Insert a dedicated Unknown (-1) surrogate row in each Gold dimension and map NULL or late-arriving fact foreign keys to -1 via COALESCE; Deduplicate using ROW_NUMBER() OVER (PARTITION BY BusinessKey ORDER BY ModifiedTimestamp DESC) = 1. Deduplicating `EncounterId` with `ROW_NUMBER() OVER (PARTITION BY ...)` removes HL7 duplicates, and mapping `NULL` plan keys via `COALESCE` to `-1` (`Unknown Plan`) preserves every ER admission in inner/1:* joins. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. Using >= AND <= on both ends causes rows stamped exactly at midnight on partition boundaries to load into two adjacent partitions, silently double-counting sales totals. Why the keyed choice wins: Deduplicating `EncounterId` with `ROW_NUMBER() OVER (PARTITION BY ...)` removes HL7 duplicates, and mapping `NULL` plan keys via `COALESCE` to `-1` (`Unknown Plan`) preserves every ER admission in inner/1:* joins.
- **B:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: Deduplicating `EncounterId` with `ROW_NUMBER() OVER (PARTITION BY ...)` removes HL7 duplicates, and mapping `NULL` plan keys via `COALESCE` to `-1` (`Unknown Plan`) preserves every ER admission in inner/1:* joins.
- **C:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Deduplicating `EncounterId` with `ROW_NUMBER() OVER (PARTITION BY ...)` removes HL7 duplicates, and mapping `NULL` plan keys via `COALESCE` to `-1` (`Unknown Plan`) preserves every ER admission in inner/1:* joins.
- **D:** Correct. Replacing NULL/unmatched fact foreign keys with a -1 Unknown dimension member preserves inner-join completeness, prevents blank `(Blank)` slicer rows in Power BI, and enforces Direct Lake 1:* integrity. In this scenario: Deduplicating `EncounterId` with `ROW_NUMBER() OVER (PARTITION BY ...)` removes HL7 duplicates, and mapping `NULL` plan keys via `COALESCE` to `-1` (`Unknown Plan`) preserves every ER admission in inner/1:* joins.
- **E:** Correct. Windowing by BusinessKey ordered descending by ingestion or source-change timestamp deterministically retains only the latest version of duplicate CDC events while preserving all non-key columns. In this scenario: Deduplicating `EncounterId` with `ROW_NUMBER() OVER (PARTITION BY ...)` removes HL7 duplicates, and mapping `NULL` plan keys via `COALESCE` to `-1` (`Unknown Plan`) preserves every ER admission in inner/1:* joins.

### Question 54 — D

Answer: TRY_CAST(RawReading AS DECIMAL(18, 4)). `TRY_CAST(RawReading AS DECIMAL(18, 4))` converts `"LO"`/`"HI"` cleanly to `NULL` without throwing conversion exceptions. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. Local study-map skill 2.13 (Convert Column Data Types Safely (TRY_CAST, Fixed Decimal, and Direct Lake Supported Primitive Types)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data types in Fabric Data Warehouse and Direct Lake Delta tables (https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types).

- **A:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` converts `"LO"`/`"HI"` cleanly to `NULL` without throwing conversion exceptions.
- **B:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` converts `"LO"`/`"HI"` cleanly to `NULL` without throwing conversion exceptions.
- **C:** Incorrect for this requirement. ROW_NUMBER() partitioned by the natural entity key and ordered descending by event timestamp assigns rank 1 to the single newest record per key. Why the keyed choice wins: `TRY_CAST(RawReading AS DECIMAL(18, 4))` converts `"LO"`/`"HI"` cleanly to `NULL` without throwing conversion exceptions.
- **D:** Correct. TRY_CAST safely returns NULL when encountering non-numeric strings such as "N/A" while using exact fixed-precision DECIMAL instead of imprecise binary FLOAT. In this scenario: `TRY_CAST(RawReading AS DECIMAL(18, 4))` converts `"LO"`/`"HI"` cleanly to `NULL` without throwing conversion exceptions.

### Question 55 — C

Answer: Convert unsupported Binary, GUID (uniqueidentifier), or nested Struct/Array Delta columns into VARCHAR/STRING or flat primitive types before adding the table to Direct Lake. Extracting required map keys into flat primitive `STRING`/`DECIMAL`/`DATE` columns and converting or omitting `BINARY`/`GUID` columns satisfies Direct Lake column-type constraints. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. Local study-map skill 2.13 (Convert Column Data Types Safely (TRY_CAST, Fixed Decimal, and Direct Lake Supported Primitive Types)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Data types in Fabric Data Warehouse and Direct Lake Delta tables (https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types).

- **A:** Incorrect for this requirement. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. Why the keyed choice wins: Extracting required map keys into flat primitive `STRING`/`DECIMAL`/`DATE` columns and converting or omitting `BINARY`/`GUID` columns satisfies Direct Lake column-type constraints.
- **B:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Extracting required map keys into flat primitive `STRING`/`DECIMAL`/`DATE` columns and converting or omitting `BINARY`/`GUID` columns satisfies Direct Lake column-type constraints.
- **C:** Correct. Direct Lake semantic models do not support complex Delta types (struct/array/map), Binary, or GUID semantic columns; converting or projecting them to supported primitive types prevents table exclusion or framing failures. In this scenario: Extracting required map keys into flat primitive `STRING`/`DECIMAL`/`DATE` columns and converting or omitting `BINARY`/`GUID` columns satisfies Direct Lake column-type constraints.
- **D:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Extracting required map keys into flat primitive `STRING`/`DECIMAL`/`DATE` columns and converting or omitting `BINARY`/`GUID` columns satisfies Direct Lake column-type constraints.

### Question 56 — B

Answer: Place row filters and column removals as the earliest Power Query steps on native columns and verify View Native Query remains enabled. `Table.Buffer()` breaks query folding and pulls the entire historical SQL table across the On-premises gateway into RAM; removing `Table.Buffer()` (or placing native filters first) pushes `WHERE` execution back to SQL Server. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. Local study-map skill 2.14 (Filter Data Early Preserving Power Query Folding (View Native Query) and Sargable Delta File Pruning), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query folding indicators & predicate pushdown in Power Query and Delta Lake (https://learn.microsoft.com/en-us/power-query/query-folding-basics).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Table.Buffer()` breaks query folding and pulls the entire historical SQL table across the On-premises gateway into RAM; removing `Table.Buffer()` (or placing native filters first) pushes `WHERE` execution back to SQL Server.
- **B:** Correct. Early filtering and projection in Power Query M preserves query folding, pushing WHERE and SELECT clauses to the source database engine instead of pulling unfiltered tables into the Mashup container. In this scenario: `Table.Buffer()` breaks query folding and pulls the entire historical SQL table across the On-premises gateway into RAM; removing `Table.Buffer()` (or placing native filters first) pushes `WHERE` execution back to SQL Server.
- **C:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: `Table.Buffer()` breaks query folding and pulls the entire historical SQL table across the On-premises gateway into RAM; removing `Table.Buffer()` (or placing native filters first) pushes `WHERE` execution back to SQL Server.
- **D:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: `Table.Buffer()` breaks query folding and pulls the entire historical SQL table across the On-premises gateway into RAM; removing `Table.Buffer()` (or placing native filters first) pushes `WHERE` execution back to SQL Server.

### Question 57 — A

Answer: Filter on physical Delta partition or liquid-clustered date columns using sargable range predicates (OrderDate >= '2026-01-01') without wrapping the column in functions. Direct sargable range predicates (`ServiceDate >= '2026-10-01' AND ServiceDate < '2026-11-01'`) allow Spark and SQL endpoints to prune Parquet rowgroups using min/max statistics without evaluating functions per row. Wrapping a column in YEAR(OrderDate) = 2026 blocks file-level min/max data skipping and partition pruning; sargable range predicates let Spark and SQL endpoints skip irrelevant Parquet files entirely. Local study-map skill 2.14 (Filter Data Early Preserving Power Query Folding (View Native Query) and Sargable Delta File Pruning), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query folding indicators & predicate pushdown in Power Query and Delta Lake (https://learn.microsoft.com/en-us/power-query/query-folding-basics).

- **A:** Correct. Wrapping a column in YEAR(OrderDate) = 2026 blocks file-level min/max data skipping and partition pruning; sargable range predicates let Spark and SQL endpoints skip irrelevant Parquet files entirely. In this scenario: Direct sargable range predicates (`ServiceDate >= '2026-10-01' AND ServiceDate < '2026-11-01'`) allow Spark and SQL endpoints to prune Parquet rowgroups using min/max statistics without evaluating functions per row.
- **B:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: Direct sargable range predicates (`ServiceDate >= '2026-10-01' AND ServiceDate < '2026-11-01'`) allow Spark and SQL endpoints to prune Parquet rowgroups using min/max statistics without evaluating functions per row.
- **C:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: Direct sargable range predicates (`ServiceDate >= '2026-10-01' AND ServiceDate < '2026-11-01'`) allow Spark and SQL endpoints to prune Parquet rowgroups using min/max statistics without evaluating functions per row.
- **D:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: Direct sargable range predicates (`ServiceDate >= '2026-10-01' AND ServiceDate < '2026-11-01'`) allow Spark and SQL endpoints to prune Parquet rowgroups using min/max statistics without evaluating functions per row.

### Question 58 — D

Answer: Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view. The `Visual query editor` (`New visual query`) in the Warehouse/SQL analytics endpoint builds visual diagram steps and saves them directly as a T-SQL view. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Local study-map skill 2.15 (Select, Filter, and Aggregate Data Using the Visual Query Editor and Save as SQL Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query using the Visual query editor in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/visual-query-editor).

- **A:** Incorrect for this requirement. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Why the keyed choice wins: The `Visual query editor` (`New visual query`) in the Warehouse/SQL analytics endpoint builds visual diagram steps and saves them directly as a T-SQL view.
- **B:** Incorrect for this requirement. ALM Toolkit performs metadata-only diffs and incremental TMSL deployments over XMLA, preserving existing processed historical partitions and incremental refresh windows in Production. Why the keyed choice wins: The `Visual query editor` (`New visual query`) in the Warehouse/SQL analytics endpoint builds visual diagram steps and saves them directly as a T-SQL view.
- **C:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: The `Visual query editor` (`New visual query`) in the Warehouse/SQL analytics endpoint builds visual diagram steps and saves them directly as a T-SQL view.
- **D:** Correct. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. In this scenario: The `Visual query editor` (`New visual query`) in the Warehouse/SQL analytics endpoint builds visual diagram steps and saves them directly as a T-SQL view.

### Question 59 — A

Answer: Use New visual query in the Warehouse or Lakehouse SQL analytics endpoint to add tables to the canvas, Merge/Filter/Group by, and select Save as view. `Save as view` persists a virtual T-SQL `VIEW` definition inside the SQL analytics endpoint schema that always queries current underlying Delta data. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Local study-map skill 2.15 (Select, Filter, and Aggregate Data Using the Visual Query Editor and Save as SQL Views), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query using the Visual query editor in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/data-warehouse/visual-query-editor).

- **A:** Correct. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. In this scenario: `Save as view` persists a virtual T-SQL `VIEW` definition inside the SQL analytics endpoint schema that always queries current underlying Delta data.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `Save as view` persists a virtual T-SQL `VIEW` definition inside the SQL analytics endpoint schema that always queries current underlying Delta data.
- **C:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: `Save as view` persists a virtual T-SQL `VIEW` definition inside the SQL analytics endpoint schema that always queries current underlying Delta data.
- **D:** Incorrect for this requirement. An On-premises data gateway bridges Fabric pipelines, Dataflow Gen2, and Import/DirectQuery models to on-premises SQL Server, Oracle, or file shares without opening inbound firewall ports. Why the keyed choice wins: `Save as view` persists a virtual T-SQL `VIEW` definition inside the SQL analytics endpoint schema that always queries current underlying Delta data.

### Question 60 — D

Answer: CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales. `CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales` (using `AS CLONE OF`) creates a metadata-only table clone instantaneously in Fabric Data Warehouse. CREATE TABLE ... AS CLONE OF creates a zero-copy metadata clone of a Fabric Warehouse table instantaneously (optionally AT a specific UTC timestamp) without duplicating Parquet files. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: `CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales` (using `AS CLONE OF`) creates a metadata-only table clone instantaneously in Fabric Data Warehouse.
- **B:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: `CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales` (using `AS CLONE OF`) creates a metadata-only table clone instantaneously in Fabric Data Warehouse.
- **C:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales` (using `AS CLONE OF`) creates a metadata-only table clone instantaneously in Fabric Data Warehouse.
- **D:** Correct. CREATE TABLE ... AS CLONE OF creates a zero-copy metadata clone of a Fabric Warehouse table instantaneously (optionally AT a specific UTC timestamp) without duplicating Parquet files. In this scenario: `CREATE TABLE dbo.FactSales_Backup AS CLONE OF dbo.FactSales` (using `AS CLONE OF`) creates a metadata-only table clone instantaneously in Fabric Data Warehouse.

### Question 61 — A, D

Answers: Query across a Warehouse and a Lakehouse SQL analytics endpoint in the same workspace using three-part T-SQL naming (SalesLakehouse.dbo.RawOrders); LAG(MegawattOutput, 1, 0) OVER (PARTITION BY SubstationId ORDER BY ReadingHour ASC). Three-part naming (`ImagingLakehouse.dbo.ScanMetadata`) executes zero-copy cross-database joins, and `LAG(Size, 1) OVER (PARTITION BY PatientId ORDER BY ScanDate ASC)` fetches the prior scan value. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Correct. Fabric Warehouse and SQL analytics endpoints inside the same workspace share a unified SQL engine namespace, enabling zero-copy cross-database T-SQL joins via DatabaseName.SchemaName.ObjectName. In this scenario: Three-part naming (`ImagingLakehouse.dbo.ScanMetadata`) executes zero-copy cross-database joins, and `LAG(Size, 1) OVER (PARTITION BY PatientId ORDER BY ScanDate ASC)` fetches the prior scan value.
- **B:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: Three-part naming (`ImagingLakehouse.dbo.ScanMetadata`) executes zero-copy cross-database joins, and `LAG(Size, 1) OVER (PARTITION BY PatientId ORDER BY ScanDate ASC)` fetches the prior scan value.
- **C:** Incorrect for this requirement. Applying string conversion functions to the filtered column is non-sargable, forcing full Parquet/column scans and defeating Delta file skipping and Power Query folding. Why the keyed choice wins: Three-part naming (`ImagingLakehouse.dbo.ScanMetadata`) executes zero-copy cross-database joins, and `LAG(Size, 1) OVER (PARTITION BY PatientId ORDER BY ScanDate ASC)` fetches the prior scan value.
- **D:** Correct. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. In this scenario: Three-part naming (`ImagingLakehouse.dbo.ScanMetadata`) executes zero-copy cross-database joins, and `LAG(Size, 1) OVER (PARTITION BY PatientId ORDER BY ScanDate ASC)` fetches the prior scan value.
- **E:** Incorrect for this requirement. A Lakehouse SQL analytics endpoint is strictly read-only for data manipulation (supporting SELECT and CREATE VIEW/FUNCTION/SECURITY POLICY, but not T-SQL INSERT/UPDATE/DELETE/MERGE on Delta tables). Why the keyed choice wins: Three-part naming (`ImagingLakehouse.dbo.ScanMetadata`) executes zero-copy cross-database joins, and `LAG(Size, 1) OVER (PARTITION BY PatientId ORDER BY ScanDate ASC)` fetches the prior scan value.

### Question 62 — D

Answer: | mv-expand PhaseReading = parse_json(Payload).PhaseReadings. `| mv-expand ... = parse_json(Payload)...` flattens dynamic JSON arrays into individual KQL rows prior to `summarize`. mv-expand unpacks a dynamic JSON array into one output row per array element while preserving parent event columns. Local study-map skill 2.17 (Select, Filter, and Aggregate Data Using KQL (summarize, bin, arg_max, percentile, parse_json, mv-expand)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query data in a KQL queryset in Microsoft Fabric Real-Time Intelligence (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/kql-queryset).

- **A:** Incorrect for this requirement. make-series builds regular gap-filled time-series arrays (filling empty 1-minute buckets with default = 0) required for KQL anomaly detection and trend functions; summarize by bin() omits empty buckets. Why the keyed choice wins: `| mv-expand ... = parse_json(Payload)...` flattens dynamic JSON arrays into individual KQL rows prior to `summarize`.
- **B:** Incorrect for this requirement. In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key. Why the keyed choice wins: `| mv-expand ... = parse_json(Payload)...` flattens dynamic JSON arrays into individual KQL rows prior to `summarize`.
- **C:** Incorrect for this requirement. percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse. Why the keyed choice wins: `| mv-expand ... = parse_json(Payload)...` flattens dynamic JSON arrays into individual KQL rows prior to `summarize`.
- **D:** Correct. mv-expand unpacks a dynamic JSON array into one output row per array element while preserving parent event columns. In this scenario: `| mv-expand ... = parse_json(Payload)...` flattens dynamic JSON arrays into individual KQL rows prior to `summarize`.

### Question 63 — A

Answer: Use DAX Query View with DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...) to test uncommitted model measures and inspect multi-grain results. `DAX Query View` executes `DEFINE` + `EVALUATE SUMMARIZECOLUMNS(...)` queries directly against live-edited Direct Lake and Import semantic models. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. Local study-map skill 2.18 (Select, Filter, and Aggregate Data Using DAX Queries (DAX Query View, EVALUATE, SUMMARIZECOLUMNS, INFO.VIEW)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Work with DAX query view & INFO.VIEW functions in Power BI (https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view).

- **A:** Correct. DAX Query View (in Power BI Desktop and web modeling) lets analytics engineers author query-scoped DEFINE MEASURE blocks, test them with EVALUATE SUMMARIZECOLUMNS, and choose Update model when validated. In this scenario: `DAX Query View` executes `DEFINE` + `EVALUATE SUMMARIZECOLUMNS(...)` queries directly against live-edited Direct Lake and Import semantic models.
- **B:** Incorrect for this requirement. A Fabric VNet data gateway enables Dataflows, Pipelines, and Import semantic models to connect securely to private-endpoint Azure SQL, ADLS Gen2, or Snowflake sources inside an Azure VNet without managing Windows gateway VMs. Why the keyed choice wins: `DAX Query View` executes `DEFINE` + `EVALUATE SUMMARIZECOLUMNS(...)` queries directly against live-edited Direct Lake and Import semantic models.
- **C:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `DAX Query View` executes `DEFINE` + `EVALUATE SUMMARIZECOLUMNS(...)` queries directly against live-edited Direct Lake and Import semantic models.
- **D:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: `DAX Query View` executes `DEFINE` + `EVALUATE SUMMARIZECOLUMNS(...)` queries directly against live-edited Direct Lake and Import semantic models.

### Question 64 — C

Answer: Run EVALUATE INFO.VIEW.MEASURES(), INFO.VIEW.TABLES(), INFO.VIEW.RELATIONSHIPS(), or COLUMNSTATISTICS() in DAX Query View. `INFO.VIEW.RELATIONSHIPS()` (alongside `INFO.VIEW.TABLES()`, `INFO.VIEW.COLUMNS()`, and `INFO.VIEW.MEASURES()`) exposes semantic-model metadata directly as queryable DAX tables. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. Local study-map skill 2.18 (Select, Filter, and Aggregate Data Using DAX Queries (DAX Query View, EVALUATE, SUMMARIZECOLUMNS, INFO.VIEW)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Work with DAX query view & INFO.VIEW functions in Power BI (https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view).

- **A:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `INFO.VIEW.RELATIONSHIPS()` (alongside `INFO.VIEW.TABLES()`, `INFO.VIEW.COLUMNS()`, and `INFO.VIEW.MEASURES()`) exposes semantic-model metadata directly as queryable DAX tables.
- **B:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: `INFO.VIEW.RELATIONSHIPS()` (alongside `INFO.VIEW.TABLES()`, `INFO.VIEW.COLUMNS()`, and `INFO.VIEW.MEASURES()`) exposes semantic-model metadata directly as queryable DAX tables.
- **C:** Correct. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. In this scenario: `INFO.VIEW.RELATIONSHIPS()` (alongside `INFO.VIEW.TABLES()`, `INFO.VIEW.COLUMNS()`, and `INFO.VIEW.MEASURES()`) exposes semantic-model metadata directly as queryable DAX tables.
- **D:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: `INFO.VIEW.RELATIONSHIPS()` (alongside `INFO.VIEW.TABLES()`, `INFO.VIEW.COLUMNS()`, and `INFO.VIEW.MEASURES()`) exposes semantic-model metadata directly as queryable DAX tables.

### Question 65 — A

Answer: Configure DirectQuery storage mode. `DirectQuery` leaves all data inside Snowflake and queries live per visual interaction when OneLake storage and Import caching are prohibited. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Local study-map skill 3.1 (Choose a Semantic Model Storage Mode (Import, DirectQuery, Direct Lake, and Dual)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model storage modes in the Power BI service & Microsoft Fabric (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode).

- **A:** Correct. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. In this scenario: `DirectQuery` leaves all data inside Snowflake and queries live per visual interaction when OneLake storage and Import caching are prohibited.
- **B:** Incorrect for this requirement. Direct Lake loads Delta Parquet columns directly from OneLake into VertiPaq memory on demand without scheduled Import data duplication or slow per-visual SQL translation. Why the keyed choice wins: `DirectQuery` leaves all data inside Snowflake and queries live per visual interaction when OneLake storage and Import caching are prohibited.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `DirectQuery` leaves all data inside Snowflake and queries live per visual interaction when OneLake storage and Import caching are prohibited.
- **D:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `DirectQuery` leaves all data inside Snowflake and queries live per visual interaction when OneLake storage and Import caching are prohibited.

### Question 66 — B

Answer: Configure Direct Lake storage mode. `Direct Lake` loads Delta Parquet columns directly from OneLake into memory on demand without duplicating data via Import refreshes. Local study-map skill 3.1 (Choose a Semantic Model Storage Mode (Import, DirectQuery, Direct Lake, and Dual)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Semantic model storage modes in the Power BI service & Microsoft Fabric (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode).

- **A:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: `Direct Lake` loads Delta Parquet columns directly from OneLake into memory on demand without duplicating data via Import refreshes.
- **B:** Correct. In this scenario: `Direct Lake` loads Delta Parquet columns directly from OneLake into memory on demand without duplicating data via Import refreshes.
- **C:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: `Direct Lake` loads Delta Parquet columns directly from OneLake into memory on demand without duplicating data via Import refreshes.
- **D:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Direct Lake` loads Delta Parquet columns directly from OneLake into memory on demand without duplicating data via Import refreshes.

### Question 67 — B

Answer: Hide all surrogate/foreign key columns and raw numeric measure source columns, expose explicit DAX measures in Display Folders, and set MonthName Sort by Column to MonthNumberOfYear. Hiding surrogate keys and raw fact measure columns (exposing explicit DAX measures in Display Folders) and configuring `SeverityName` `Sort by Column = SeverityRank` enforces clean star-schema consumption. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Local study-map skill 3.2 (Implement a Star Schema for a Semantic Model (Mark as Date Table, Hide Keys, Sort by Column, Display Folders)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Set and use date tables & star-schema best practices in Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables).

- **A:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: Hiding surrogate keys and raw fact measure columns (exposing explicit DAX measures in Display Folders) and configuring `SeverityName` `Sort by Column = SeverityRank` enforces clean star-schema consumption.
- **B:** Correct. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. In this scenario: Hiding surrogate keys and raw fact measure columns (exposing explicit DAX measures in Display Folders) and configuring `SeverityName` `Sort by Column = SeverityRank` enforces clean star-schema consumption.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Hiding surrogate keys and raw fact measure columns (exposing explicit DAX measures in Display Folders) and configuring `SeverityName` `Sort by Column = SeverityRank` enforces clean star-schema consumption.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Hiding surrogate keys and raw fact measure columns (exposing explicit DAX measures in Display Folders) and configuring `SeverityName` `Sort by Column = SeverityRank` enforces clean star-schema consumption.

### Question 68 — B, D

Answers: Disable global/current-file Auto date/time and run Mark as date table on the dedicated Calendar dimension selecting its unique Date-typed column; Build a dedicated contiguous Gold Calendar/Date dimension table covering every day from the earliest to latest fact year with fiscal and holiday attributes. Building one conformed Calendar dimension covering the full date span and disabling `Auto date/time` while running `Mark as date table` eliminates all 22 hidden `LocalDateTable_*` hierarchies. Local study-map skill 3.2 (Implement a Star Schema for a Semantic Model (Mark as Date Table, Hide Keys, Sort by Column, Display Folders)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Set and use date tables & star-schema best practices in Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables).

- **A:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Building one conformed Calendar dimension covering the full date span and disabling `Auto date/time` while running `Mark as date table` eliminates all 22 hidden `LocalDateTable_*` hierarchies.
- **B:** Correct. A dedicated Calendar table with unbroken daily grain is mandatory for DAX time intelligence, Direct Lake date relationships (where Auto date/time is unsupported on Direct Lake on SQL), and cross-fact filtering. In this scenario: Building one conformed Calendar dimension covering the full date span and disabling `Auto date/time` while running `Mark as date table` eliminates all 22 hidden `LocalDateTable_*` hierarchies.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Building one conformed Calendar dimension covering the full date span and disabling `Auto date/time` while running `Mark as date table` eliminates all 22 hidden `LocalDateTable_*` hierarchies.
- **D:** Correct. Auto date/time bloats model size with hidden LocalDateTable_* tables on every date column; marking a dedicated Calendar table preserves existing integer YYYYMMDD surrogate relationships while enabling native DAX time intelligence. In this scenario: Building one conformed Calendar dimension covering the full date span and disabling `Auto date/time` while running `Mark as date table` eliminates all 22 hidden `LocalDateTable_*` hierarchies.
- **E:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Building one conformed Calendar dimension covering the full date span and disabling `Auto date/time` while running `Mark as date table` eliminates all 22 hidden `LocalDateTable_*` hierarchies.

### Question 69 — B

Answer: Create one active 1:* relationship on OrderDate and inactive 1:* relationships on ShipDate and DueDate activated inside measures via USERELATIONSHIP(). Keep one active `1:*` relationship (for example `AdmissionDateKey`) and two inactive `1:*` relationships activated inside measures via `CALCULATE(..., USERELATIONSHIP(...))`. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. Scoping CROSSFILTER(..., BOTH) inside a DAX measure over a bridge table satisfies many-to-many attribution without turning on permanent model-wide bidirectional relationships that cause ambiguity and performance degradation. Why the keyed choice wins: Keep one active `1:*` relationship (for example `AdmissionDateKey`) and two inactive `1:*` relationships activated inside measures via `CALCULATE(..., USERELATIONSHIP(...))`.
- **B:** Correct. Only one relationship path between two tables can be active simultaneously; inactive relationships combined with CALCULATE([Sales], USERELATIONSHIP(DimDate[DateKey], FactSales[ShipDateKey])) enable role-playing dimensions cleanly without duplicating DimDate three times. In this scenario: Keep one active `1:*` relationship (for example `AdmissionDateKey`) and two inactive `1:*` relationships activated inside measures via `CALCULATE(..., USERELATIONSHIP(...))`.
- **C:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: Keep one active `1:*` relationship (for example `AdmissionDateKey`) and two inactive `1:*` relationships activated inside measures via `CALCULATE(..., USERELATIONSHIP(...))`.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Keep one active `1:*` relationship (for example `AdmissionDateKey`) and two inactive `1:*` relationships activated inside measures via `CALCULATE(..., USERELATIONSHIP(...))`.

### Question 70 — C

Answer: Enable Assume referential integrity on DirectQuery 1:* relationships where foreign keys are guaranteed non-null and valid. `Assume referential integrity` emits `INNER JOIN` instead of `LEFT OUTER JOIN`, silently omitting every walk-in row with a `NULL` `ReferringClinicKey`; enable it only on validated non-null foreign keys. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery. Why the keyed choice wins: `Assume referential integrity` emits `INNER JOIN` instead of `LEFT OUTER JOIN`, silently omitting every walk-in row with a `NULL` `ReferringClinicKey`; enable it only on validated non-null foreign keys.
- **B:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: `Assume referential integrity` emits `INNER JOIN` instead of `LEFT OUTER JOIN`, silently omitting every walk-in row with a `NULL` `ReferringClinicKey`; enable it only on validated non-null foreign keys.
- **C:** Correct. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. In this scenario: `Assume referential integrity` emits `INNER JOIN` instead of `LEFT OUTER JOIN`, silently omitting every walk-in row with a `NULL` `ReferringClinicKey`; enable it only on validated non-null foreign keys.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: `Assume referential integrity` emits `INNER JOIN` instead of `LEFT OUTER JOIN`, silently omitting every walk-in row with a `NULL` `ReferringClinicKey`; enable it only on validated non-null foreign keys.

### Question 71 — A

Answer: Pass simple column predicates wrapped in KEEPFILTERS(DimProduct[Color] = "Red") to CALCULATE instead of FILTER(ALL(FactSales), ...). Wrapping the column predicate in `KEEPFILTERS(...)` intersects with outer filter context instead of overwriting existing `UnitType` filters. KEEPFILTERS intersects the predicate with existing report slicer selections rather than overwriting them, and filtering a dimension column avoids scanning the entire multi-million-row fact table in the Formula Engine. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Correct. KEEPFILTERS intersects the predicate with existing report slicer selections rather than overwriting them, and filtering a dimension column avoids scanning the entire multi-million-row fact table in the Formula Engine. In this scenario: Wrapping the column predicate in `KEEPFILTERS(...)` intersects with outer filter context instead of overwriting existing `UnitType` filters.
- **B:** Incorrect for this requirement. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Why the keyed choice wins: Wrapping the column predicate in `KEEPFILTERS(...)` intersects with outer filter context instead of overwriting existing `UnitType` filters.
- **C:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: Wrapping the column predicate in `KEEPFILTERS(...)` intersects with outer filter context instead of overwriting existing `UnitType` filters.
- **D:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Wrapping the column predicate in `KEEPFILTERS(...)` intersects with outer filter context instead of overwriting existing `UnitType` filters.

### Question 72 — C

Answer: Use SUMX(FactOrderLines, FactOrderLines[Quantity] * FactOrderLines[UnitPrice] * (1 - FactOrderLines[DiscountPct])) over the fact table. `SUMX` computes row-by-row multiplication in memory during Storage Engine scans without storing a high-cardinality physical calculated column (and Direct Lake on SQL does not even allow calculated columns referencing Direct Lake tables). Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Incorrect for this requirement. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Why the keyed choice wins: `SUMX` computes row-by-row multiplication in memory during Storage Engine scans without storing a high-cardinality physical calculated column (and Direct Lake on SQL does not even allow calculated columns referencing Direct Lake tables).
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: `SUMX` computes row-by-row multiplication in memory during Storage Engine scans without storing a high-cardinality physical calculated column (and Direct Lake on SQL does not even allow calculated columns referencing Direct Lake tables).
- **C:** Correct. Row-level multiplication must happen row by row via an iterator like SUMX before summing; multiplying SUM(Quantity) * SUM(UnitPrice) produces mathematically wrong totals while avoiding materialized calculated columns. In this scenario: `SUMX` computes row-by-row multiplication in memory during Storage Engine scans without storing a high-cardinality physical calculated column (and Direct Lake on SQL does not even allow calculated columns referencing Direct Lake tables).
- **D:** Incorrect for this requirement. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. Why the keyed choice wins: `SUMX` computes row-by-row multiplication in memory during Storage Engine scans without storing a high-cardinality physical calculated column (and Direct Lake on SQL does not even allow calculated columns referencing Direct Lake tables).

### Question 73 — A, C

Answers: Store repeated measure references in a DAX VAR before RETURN so each sub-expression evaluates once instead of multiple times across IF/DIVIDE branches; Use ISINSCOPE(DimProduct[Subcategory]) (or SELECTEDVALUE with an alternate result) to branch measure behavior cleanly across matrix hierarchy levels. Caching `[30-Day Readmissions]` in a `VAR` avoids four redundant SE scans, and checking `NOT ISINSCOPE('DimLocation'[Ward])` controls hierarchy-level visibility cleanly. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Correct. DAX variables evaluate eagerly at their definition filter context and cache the scalar or table result, cutting redundant Storage Engine scans and improving readability. In this scenario: Caching `[30-Day Readmissions]` in a `VAR` avoids four redundant SE scans, and checking `NOT ISINSCOPE('DimLocation'[Ward])` controls hierarchy-level visibility cleanly.
- **B:** Incorrect for this requirement. Ratios are non-additive: summing or unweighted-averaging row-level percentages across categories yields mathematically wrong portfolio margins and wastes columnar RAM compared to DIVIDE([Total Profit], [Total Revenue]). Why the keyed choice wins: Caching `[30-Day Readmissions]` in a `VAR` avoids four redundant SE scans, and checking `NOT ISINSCOPE('DimLocation'[Ward])` controls hierarchy-level visibility cleanly.
- **C:** Correct. ISINSCOPE returns TRUE only when the specified column is actively grouping the current visual row/column level, making it superior to HASONEVALUE for subtotal vs leaf detection in matrices. In this scenario: Caching `[30-Day Readmissions]` in a `VAR` avoids four redundant SE scans, and checking `NOT ISINSCOPE('DimLocation'[Ward])` controls hierarchy-level visibility cleanly.
- **D:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: Caching `[30-Day Readmissions]` in a `VAR` avoids four redundant SE scans, and checking `NOT ISINSCOPE('DimLocation'[Ward])` controls hierarchy-level visibility cleanly.
- **E:** Incorrect for this requirement. Passing an unfiltered fact table into FILTER() forces materialization and row-by-row iteration of the entire fact table instead of pushing compact column filter predicates to the Storage Engine. Why the keyed choice wins: Caching `[30-Day Readmissions]` in a `VAR` avoids four redundant SE scans, and checking `NOT ISINSCOPE('DimLocation'[Ward])` controls hierarchy-level visibility cleanly.

### Question 74 — C

Answer: CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date])). `CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))` applies the `DATESYTD` filter modifier dynamically to whichever measure occupies the visual. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. INFO.VIEW.MEASURES() can be run directly in DAX Query View to output a table of all model measures, DAX expressions, format strings, display folders, and hidden flags. Why the keyed choice wins: `CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))` applies the `DATESYTD` filter modifier dynamically to whichever measure occupies the visual.
- **B:** Incorrect for this requirement. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. Why the keyed choice wins: `CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))` applies the `DATESYTD` filter modifier dynamically to whichever measure occupies the visual.
- **C:** Correct. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. In this scenario: `CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))` applies the `DATESYTD` filter modifier dynamically to whichever measure occupies the visual.
- **D:** Incorrect for this requirement. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Why the keyed choice wins: `CALCULATE(SELECTEDMEASURE(), DATESYTD('Calendar'[Date]))` applies the `DATESYTD` filter modifier dynamically to whichever measure occupies the visual.

### Question 75 — C

Answer: Configure a Dynamic Format String expression on the measure or calculation item (for example returning "\$#,0.00" vs "0.0%" via SELECTEDMEASUREFORMATSTRING()) without wrapping values in FORMAT(). `FORMAT()` converts numeric results into text strings that cannot plot on value axes; returning numeric values in the measure and moving `"0.0 \d\a\y\s"` / `"0.00%"` into a Dynamic Format String expression preserves numeric plotting. Unlike FORMAT() — which converts numbers into text strings and breaks chart axes/sorting/aggregations — Dynamic Format Strings preserve true numeric data types while rendering context-aware currency or percentage formatting. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. Hiding technical keys and raw fact columns prevents accidental SUM of IDs or implicit measures, while Sort by Column ensures chronological rather than alphabetical month ordering. Why the keyed choice wins: `FORMAT()` converts numeric results into text strings that cannot plot on value axes; returning numeric values in the measure and moving `"0.0 \d\a\y\s"` / `"0.00%"` into a Dynamic Format String expression preserves numeric plotting.
- **B:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: `FORMAT()` converts numeric results into text strings that cannot plot on value axes; returning numeric values in the measure and moving `"0.0 \d\a\y\s"` / `"0.00%"` into a Dynamic Format String expression preserves numeric plotting.
- **C:** Correct. Unlike FORMAT() — which converts numbers into text strings and breaks chart axes/sorting/aggregations — Dynamic Format Strings preserve true numeric data types while rendering context-aware currency or percentage formatting. In this scenario: `FORMAT()` converts numeric results into text strings that cannot plot on value axes; returning numeric values in the measure and moving `"0.0 \d\a\y\s"` / `"0.00%"` into a Dynamic Format String expression preserves numeric plotting.
- **D:** Incorrect for this requirement. FORMAT() returns a Text string rather than a numeric data type, preventing the measure from plotting on continuous line/bar chart axes, sorting numerically, or aggregating in downstream visuals. Why the keyed choice wins: `FORMAT()` converts numeric results into text strings that cannot plot on value axes; returning numeric values in the measure and moving `"0.0 \d\a\y\s"` / `"0.00%"` into a Dynamic Format String expression preserves numeric plotting.

### Question 76 — D

Answer: NAMEOF('DimTrade'[CurrencyPair]). `NAMEOF('Table'[Column])` binds the parameter row to the underlying model object metadata rather than a fragile hardcoded string. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. Local study-map skill 3.5 (Implement Calculation Groups, Dynamic Format Strings, and Field Parameters (NAMEOF)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Calculation groups, dynamic format strings for measures, and field parameters (https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups).

- **A:** Incorrect for this requirement. Dynamic format string expressions return a format mask string while preserving the measure's underlying numeric type; SELECTEDMEASUREFORMATSTRING() preserves the base measure's native currency/decimal mask. Why the keyed choice wins: `NAMEOF('Table'[Column])` binds the parameter row to the underlying model object metadata rather than a fragile hardcoded string.
- **B:** Incorrect for this requirement. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. Why the keyed choice wins: `NAMEOF('Table'[Column])` binds the parameter row to the underlying model object metadata rather than a fragile hardcoded string.
- **C:** Incorrect for this requirement. USERPRINCIPALNAME() returns the signed-in consumer's Microsoft Entra UPN (user@domain.com) consistently in the Fabric service for dynamic RLS. Why the keyed choice wins: `NAMEOF('Table'[Column])` binds the parameter row to the underlying model object metadata rather than a fragile hardcoded string.
- **D:** Correct. Field Parameter tables use NAMEOF() so column or measure renames automatically propagate into the parameter metadata without breaking report slicers. In this scenario: `NAMEOF('Table'[Column])` binds the parameter row to the underlying model object metadata rather than a fragile hardcoded string.

### Question 77 — C

Answer: Enable Large semantic model storage format in semantic model settings (or set defaultPowerBIDataSourceVersion = powerBI_V3 with LargeDatasetStorageFormat). Enabling `Large semantic model storage format` unlocks capacity-tier memory limits above 10 GB and optimizes segment paging and XMLA write throughput. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Local study-map skill 3.6 (Identify Use Cases for and Configure Large Semantic Model Storage Format), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Large semantic models in Microsoft Fabric & Power BI Premium (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-large-models).

- **A:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: Enabling `Large semantic model storage format` unlocks capacity-tier memory limits above 10 GB and optimizes segment paging and XMLA write throughput.
- **B:** Incorrect for this requirement. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Why the keyed choice wins: Enabling `Large semantic model storage format` unlocks capacity-tier memory limits above 10 GB and optimizes segment paging and XMLA write throughput.
- **C:** Correct. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. In this scenario: Enabling `Large semantic model storage format` unlocks capacity-tier memory limits above 10 GB and optimizes segment paging and XMLA write throughput.
- **D:** Incorrect for this requirement. DirectQuery leaves rows in the external source system and translates every visual interaction into live native source queries — suitable when data cannot leave the source or requires real-time transactional visibility outside OneLake. Why the keyed choice wins: Enabling `Large semantic model storage format` unlocks capacity-tier memory limits above 10 GB and optimizes segment paging and XMLA write throughput.

### Question 78 — B

Answer: Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time. Auditing column sizes in VertiPaq Analyzer and removing unused high-cardinality `ClaimAuditNoteText` / `GUID` columns (plus splitting millisecond timestamps) reduces dictionary RAM dramatically. Columnar memory in VertiPaq and Direct Lake transcoding scales primarily with column cardinality rather than row count; dropping unused GUIDs or splitting millisecond timestamps into separate Date and Time columns cuts memory dramatically. Local study-map skill 3.6 (Identify Use Cases for and Configure Large Semantic Model Storage Format), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Large semantic models in Microsoft Fabric & Power BI Premium (https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-large-models).

- **A:** Incorrect for this requirement. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Why the keyed choice wins: Auditing column sizes in VertiPaq Analyzer and removing unused high-cardinality `ClaimAuditNoteText` / `GUID` columns (plus splitting millisecond timestamps) reduces dictionary RAM dramatically.
- **B:** Correct. Columnar memory in VertiPaq and Direct Lake transcoding scales primarily with column cardinality rather than row count; dropping unused GUIDs or splitting millisecond timestamps into separate Date and Time columns cuts memory dramatically. In this scenario: Auditing column sizes in VertiPaq Analyzer and removing unused high-cardinality `ClaimAuditNoteText` / `GUID` columns (plus splitting millisecond timestamps) reduces dictionary RAM dramatically.
- **C:** Incorrect for this requirement. Field Parameters let report consumers dynamically switch which columns or measures populate a visual axis, legend, or values well from a single slicer without maintaining bookmark-swapped duplicate visuals. Why the keyed choice wins: Auditing column sizes in VertiPaq Analyzer and removing unused high-cardinality `ClaimAuditNoteText` / `GUID` columns (plus splitting millisecond timestamps) reduces dictionary RAM dramatically.
- **D:** Incorrect for this requirement. Deployment rules in Test and Production automatically rebind supported semantic models, dataflows, notebooks, and paginated reports to stage-specific SQL endpoints or connection parameters on every deployment without overwriting Prod bindings. Why the keyed choice wins: Auditing column sizes in VertiPaq Analyzer and removing unused high-cardinality `ClaimAuditNoteText` / `GUID` columns (plus splitting millisecond timestamps) reduces dictionary RAM dramatically.

### Question 79 — A

Answer: Build a Direct Lake on OneLake composite semantic model combining Direct Lake fact tables from OneLake with Import dimension/target tables using regular relationships. A `Direct Lake on OneLake` composite semantic model supports mixing Direct Lake tables with `Import` tables from any Power Query connector using regular relationships. Direct Lake on OneLake supports true composite models that mix Direct Lake tables from multiple Fabric items with Import tables from any Power Query connector while preserving fast regular (non-limited) relationships. Local study-map skill 3.7 (Design and Build Composite Models (Direct Lake on OneLake + Import, Dual + Aggregations, DirectQuery over PBI)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use composite models in Power BI Desktop & Direct Lake on OneLake composite models (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-web-modeling).

- **A:** Correct. Direct Lake on OneLake supports true composite models that mix Direct Lake tables from multiple Fabric items with Import tables from any Power Query connector while preserving fast regular (non-limited) relationships. In this scenario: A `Direct Lake on OneLake` composite semantic model supports mixing Direct Lake tables with `Import` tables from any Power Query connector using regular relationships.
- **B:** Incorrect for this requirement. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Why the keyed choice wins: A `Direct Lake on OneLake` composite semantic model supports mixing Direct Lake tables with `Import` tables from any Power Query connector using regular relationships.
- **C:** Incorrect for this requirement. A .pbit file distributes reusable schema, visuals, and parameter prompts cleanly without bundling cached customer data, prompting each recipient for parameter values on first open. Why the keyed choice wins: A `Direct Lake on OneLake` composite semantic model supports mixing Direct Lake tables with `Import` tables from any Power Query connector using regular relationships.
- **D:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: A `Direct Lake on OneLake` composite semantic model supports mixing Direct Lake tables with `Import` tables from any Power Query connector using regular relationships.

### Question 80 — A, D

Answers: Configure shared dimension tables in Dual storage mode inside a composite model; Configure a user-defined Import aggregation table with Manage aggregations mappings (Sum, Count table rows, GroupBy) over a DirectQuery detail fact table. Configuring `Manage aggregations` (`Sum`/`Count`) on `FactLabDailyAgg` routes summary visuals to memory, and setting `DimDate`, `DimTestType`, and `DimFacility` to `Dual` storage mode avoids cross-source join penalties. Local study-map skill 3.7 (Design and Build Composite Models (Direct Lake on OneLake + Import, Dual + Aggregations, DirectQuery over PBI)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use composite models in Power BI Desktop & Direct Lake on OneLake composite models (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-web-modeling).

- **A:** Correct. User-defined Import aggregations satisfy high-level grouped queries purely from in-memory VertiPaq cache and automatically route only unaggregated detail drill-throughs to the underlying DirectQuery source. In this scenario: Configuring `Manage aggregations` (`Sum`/`Count`) on `FactLabDailyAgg` routes summary visuals to memory, and setting `DimDate`, `DimTestType`, and `DimFacility` to `Dual` storage mode avoids cross-source join penalties.
- **B:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Configuring `Manage aggregations` (`Sum`/`Count`) on `FactLabDailyAgg` routes summary visuals to memory, and setting `DimDate`, `DimTestType`, and `DimFacility` to `Dual` storage mode avoids cross-source join penalties.
- **C:** Incorrect for this requirement. Binary .pbix files bloat Git repositories, expose cached data in commit history, and produce unreadable binary merge conflicts instead of line-by-line TMDL/PBIR diffs. Why the keyed choice wins: Configuring `Manage aggregations` (`Sum`/`Count`) on `FactLabDailyAgg` routes summary visuals to memory, and setting `DimDate`, `DimTestType`, and `DimFacility` to `Dual` storage mode avoids cross-source join penalties.
- **D:** Correct. Dual storage mode stores a dimension both in VertiPaq memory and as a DirectQuery source so queries hitting Import/aggregation tables run purely in memory while queries hitting DirectQuery fact tables push joins down natively without limited cross-source joins. In this scenario: Configuring `Manage aggregations` (`Sum`/`Count`) on `FactLabDailyAgg` routes summary visuals to memory, and setting `DimDate`, `DimTestType`, and `DimFacility` to `Dual` storage mode avoids cross-source join penalties.
- **E:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: Configuring `Manage aggregations` (`Sum`/`Count`) on `FactLabDailyAgg` routes summary visuals to memory, and setting `DimDate`, `DimTestType`, and `DimFacility` to `Dual` storage mode avoids cross-source join penalties.

### Question 81 — B

Answer: Run Performance Analyzer in Power BI Desktop to separate DAX query duration, Visual display rendering time, and Other (single-threaded visual queue waiting) time. High `Other` duration reflects single-threaded visual initialization and query-queue wait across too many visuals/slicers on one page; reducing visual count by combining KPIs into matrix/multi-row visuals eliminates the queue bottleneck. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Local study-map skill 3.8 (Implement Performance Improvements in Queries and Report Visuals (Performance Analyzer & Query Reduction)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use Performance Analyzer to examine report element performance in Power BI (https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer).

- **A:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: High `Other` duration reflects single-threaded visual initialization and query-queue wait across too many visuals/slicers on one page; reducing visual count by combining KPIs into matrix/multi-row visuals eliminates the queue bottleneck.
- **B:** Correct. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. In this scenario: High `Other` duration reflects single-threaded visual initialization and query-queue wait across too many visuals/slicers on one page; reducing visual count by combining KPIs into matrix/multi-row visuals eliminates the queue bottleneck.
- **C:** Incorrect for this requirement. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Why the keyed choice wins: High `Other` duration reflects single-threaded visual initialization and query-queue wait across too many visuals/slicers on one page; reducing visual count by combining KPIs into matrix/multi-row visuals eliminates the queue bottleneck.
- **D:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: High `Other` duration reflects single-threaded visual initialization and query-queue wait across too many visuals/slicers on one page; reducing visual count by combining KPIs into matrix/multi-row visuals eliminates the queue bottleneck.

### Question 82 — C

Answer: Enable Query reduction options (Add an Apply button to slicers and disable cross-highlighting by default) on high-latency DirectQuery report pages. Enabling `Disabling cross highlighting/filtering by default` (alongside slicer `Apply` buttons) under `Options -> Query reduction` stops unwanted cascade queries on DirectQuery pages. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. Local study-map skill 3.8 (Implement Performance Improvements in Queries and Report Visuals (Performance Analyzer & Query Reduction)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Use Performance Analyzer to examine report element performance in Power BI (https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer).

- **A:** Incorrect for this requirement. Hundreds of tiny streaming Parquet files inflate Delta rowgroup counts past Fabric SKU guardrails and degrade transcoding; OPTIMIZE compacts files into large V-Order-sorted rowgroups optimized for VertiPaq in-memory compression. Why the keyed choice wins: Enabling `Disabling cross highlighting/filtering by default` (alongside slicer `Apply` buttons) under `Options -> Query reduction` stops unwanted cascade queries on DirectQuery pages.
- **B:** Incorrect for this requirement. A .pbip project replaces the opaque binary .pbix archive with human-readable TMDL (.tmdl) semantic-model files and PBIR JSON report files so Git pull requests show line-by-line measure, relationship, and visual diffs. Why the keyed choice wins: Enabling `Disabling cross highlighting/filtering by default` (alongside slicer `Apply` buttons) under `Options -> Query reduction` stops unwanted cascade queries on DirectQuery pages.
- **C:** Correct. Adding Apply buttons to multi-select slicers prevents firing intermediate SQL/DAX queries on every individual slicer selection before the user finishes filtering. In this scenario: Enabling `Disabling cross highlighting/filtering by default` (alongside slicer `Apply` buttons) under `Options -> Query reduction` stops unwanted cascade queries on DirectQuery pages.
- **D:** Incorrect for this requirement. Large semantic model storage format removes the legacy 1 GB / 10 GB compressed size cap (allowing models to scale up to the Fabric capacity SKU memory ceiling), enables on-demand segment paging, and improves XMLA write performance. Why the keyed choice wins: Enabling `Disabling cross highlighting/filtering by default` (alongside slicer `Apply` buttons) under `Options -> Query reduction` stops unwanted cascade queries on DirectQuery pages.

### Question 83 — A

Answer: Profile the slow measure in DAX Studio using Server Timings to inspect Formula Engine (FE) vs Storage Engine (SE) CPU, SE query count, and CallbackDataID warnings. `CallbackDataID` shows the Storage Engine could not evaluate a complex DAX expression (`IF`/`DIVIDE`/unpushed logic inside an iterator) natively and had to call back row-by-row to the single-threaded Formula Engine. DAX Studio Server Timings reveals whether slow execution comes from hundreds of chatty SE scans, CallbackDataID forcing row-by-row FE callbacks inside SE scans, or unpushed complex predicates. Local study-map skill 3.9 (Improve DAX and Model Performance Using DAX Studio Server Timings (FE vs SE) and VertiPaq Cardinality Reduction), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Optimization guide for Power BI — DAX Formula Engine vs Storage Engine & VertiPaq (https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization).

- **A:** Correct. DAX Studio Server Timings reveals whether slow execution comes from hundreds of chatty SE scans, CallbackDataID forcing row-by-row FE callbacks inside SE scans, or unpushed complex predicates. In this scenario: `CallbackDataID` shows the Storage Engine could not evaluate a complex DAX expression (`IF`/`DIVIDE`/unpushed logic inside an iterator) natively and had to call back row-by-row to the single-threaded Formula Engine.
- **B:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: `CallbackDataID` shows the Storage Engine could not evaluate a complex DAX expression (`IF`/`DIVIDE`/unpushed logic inside an iterator) natively and had to call back row-by-row to the single-threaded Formula Engine.
- **C:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: `CallbackDataID` shows the Storage Engine could not evaluate a complex DAX expression (`IF`/`DIVIDE`/unpushed logic inside an iterator) natively and had to call back row-by-row to the single-threaded Formula Engine.
- **D:** Incorrect for this requirement. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Why the keyed choice wins: `CallbackDataID` shows the Storage Engine could not evaluate a complex DAX expression (`IF`/`DIVIDE`/unpushed logic inside an iterator) natively and had to call back row-by-row to the single-threaded Formula Engine.

### Question 84 — A

Answer: Capture visual timings in Performance Analyzer → Profile captured DAX in DAX Studio with Server Timings and Query Plan → Refactor FILTER(Fact,...) into VAR-cached SE column predicates and run V-Order OPTIMIZE → Re-test with Clear Cache. Capturing the visual's query in Performance Analyzer, inspecting FE/SE and Direct Lake events in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + compacting Delta files with V-Order `OPTIMIZE`, and re-running after `Clear Cache` validates real gains. Correct order: isolate visual vs DAX queue time in Performance Analyzer, profile FE/SE and Direct Lake fallback in DAX Studio Server Timings, fix DAX anti-patterns + Delta Parquet layout, and benchmark cold-cache results. Local study-map skill 3.9 (Improve DAX and Model Performance Using DAX Studio Server Timings (FE vs SE) and VertiPaq Cardinality Reduction), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Optimization guide for Power BI — DAX Formula Engine vs Storage Engine & VertiPaq (https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization).

- **A:** Correct. Correct order: isolate visual vs DAX queue time in Performance Analyzer, profile FE/SE and Direct Lake fallback in DAX Studio Server Timings, fix DAX anti-patterns + Delta Parquet layout, and benchmark cold-cache results. In this scenario: Capturing the visual's query in Performance Analyzer, inspecting FE/SE and Direct Lake events in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + compacting Delta files with V-Order `OPTIMIZE`, and re-running after `Clear Cache` validates real gains.
- **B:** Incorrect for this requirement. Incorrect: benchmarking warm cache hides real SE/transcoding cost, GUID columns bloat dictionaries, DirectQueryOnly slows visuals, and 45 cards create visual-queue contention. Why the keyed choice wins: Capturing the visual's query in Performance Analyzer, inspecting FE/SE and Direct Lake events in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + compacting Delta files with V-Order `OPTIMIZE`, and re-running after `Clear Cache` validates real gains.
- **C:** Incorrect for this requirement. Incorrect: snowflaking and Auto date/time increase relationship hops and memory overhead rather than resolving FE/SE bottlenecks. Why the keyed choice wins: Capturing the visual's query in Performance Analyzer, inspecting FE/SE and Direct Lake events in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + compacting Delta files with V-Order `OPTIMIZE`, and re-running after `Clear Cache` validates real gains.
- **D:** Incorrect for this requirement. Incorrect: scaling capacity blindly wastes budget while bidirectional joins, FORMAT() strings, and disabled V-Order make FE and transcoding slower. Why the keyed choice wins: Capturing the visual's query in Performance Analyzer, inspecting FE/SE and Direct Lake events in DAX Studio Server Timings, refactoring `FILTER(Fact,...)` + compacting Delta files with V-Order `OPTIMIZE`, and re-running after `Clear Cache` validates real gains.

### Question 85 — A

Answer: directLakeBehavior: directLakeOnly. Setting `directLakeBehavior: directLakeOnly` disables DirectQuery fallback on Direct Lake on SQL models so guardrail violations surface immediately instead of silently degrading into SQL queries. Setting directLakeBehavior: directLakeOnly in TMDL prevents a Direct Lake on SQL model from silently falling back to DirectQuery. Local study-map skill 3.10 (Configure Direct Lake Framing, Transcoding, V-Order/OPTIMIZE Guardrails, and DirectLakeBehavior Fallback), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: How Direct Lake works (framing, transcoding, V-Order, fallback & DirectLakeBehavior) (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works).

- **A:** Correct. Setting directLakeBehavior: directLakeOnly in TMDL prevents a Direct Lake on SQL model from silently falling back to DirectQuery. In this scenario: Setting `directLakeBehavior: directLakeOnly` disables DirectQuery fallback on Direct Lake on SQL models so guardrail violations surface immediately instead of silently degrading into SQL queries.
- **B:** Incorrect for this requirement. Standard CAST throws a runtime conversion error on strings like "N/A" and aborts the entire SQL statement. Why the keyed choice wins: Setting `directLakeBehavior: directLakeOnly` disables DirectQuery fallback on Direct Lake on SQL models so guardrail violations surface immediately instead of silently degrading into SQL queries.
- **C:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Setting `directLakeBehavior: directLakeOnly` disables DirectQuery fallback on Direct Lake on SQL models so guardrail violations surface immediately instead of silently degrading into SQL queries.
- **D:** Incorrect for this requirement. Direct Lake on OneLake operates exclusively in DirectLakeOnly mode and never falls back to DirectQuery; exceeding capacity guardrails fails framing/queries until Delta tables or SKU sizing are optimized. Why the keyed choice wins: Setting `directLakeBehavior: directLakeOnly` disables DirectQuery fallback on Direct Lake on SQL models so guardrail violations surface immediately instead of silently degrading into SQL queries.

### Question 86 — A, E, F

Answers: Enable V-Order Parquet writes and schedule Delta Lake OPTIMIZE (bin-packing small files) and VACUUM on Gold tables to stay under capacity rowgroup/file guardrails; Trigger a Direct Lake framing refresh (via Pipeline Semantic model refresh activity, Enhanced Refresh API, or Keep your Direct Lake data up to date) after ETL completes; Inspect column dictionary and hierarchy sizes with VertiPaq Analyzer (or INFO.VIEW / DMV) and remove unused high-cardinality GUID/timestamp/free-text columns or split datetime into Date + Time. Running Delta `OPTIMIZE` with `V-Order`, dropping unused high-cardinality GUID/note columns, and orchestrating controlled post-ETL framing refreshes keep rowgroups and resident memory within SKU limits. Local study-map skill 3.10 (Configure Direct Lake Framing, Transcoding, V-Order/OPTIMIZE Guardrails, and DirectLakeBehavior Fallback), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: How Direct Lake works (framing, transcoding, V-Order, fallback & DirectLakeBehavior) (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works).

- **A:** Correct. Columnar memory in VertiPaq and Direct Lake transcoding scales primarily with column cardinality rather than row count; dropping unused GUIDs or splitting millisecond timestamps into separate Date and Time columns cuts memory dramatically. In this scenario: Running Delta `OPTIMIZE` with `V-Order`, dropping unused high-cardinality GUID/note columns, and orchestrating controlled post-ETL framing refreshes keep rowgroups and resident memory within SKU limits.
- **B:** Incorrect for this requirement. Direct Lake on OneLake operates exclusively in DirectLakeOnly mode and never falls back to DirectQuery; exceeding capacity guardrails fails framing/queries until Delta tables or SKU sizing are optimized. Why the keyed choice wins: Running Delta `OPTIMIZE` with `V-Order`, dropping unused high-cardinality GUID/note columns, and orchestrating controlled post-ETL framing refreshes keep rowgroups and resident memory within SKU limits.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: Running Delta `OPTIMIZE` with `V-Order`, dropping unused high-cardinality GUID/note columns, and orchestrating controlled post-ETL framing refreshes keep rowgroups and resident memory within SKU limits.
- **D:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: Running Delta `OPTIMIZE` with `V-Order`, dropping unused high-cardinality GUID/note columns, and orchestrating controlled post-ETL framing refreshes keep rowgroups and resident memory within SKU limits.
- **E:** Correct. Hundreds of tiny streaming Parquet files inflate Delta rowgroup counts past Fabric SKU guardrails and degrade transcoding; OPTIMIZE compacts files into large V-Order-sorted rowgroups optimized for VertiPaq in-memory compression. In this scenario: Running Delta `OPTIMIZE` with `V-Order`, dropping unused high-cardinality GUID/note columns, and orchestrating controlled post-ETL framing refreshes keep rowgroups and resident memory within SKU limits.
- **F:** Correct. Framing is a fast metadata-only operation updating the Direct Lake model's pointer to the latest Delta transaction log Parquet files and evicting stale resident columns so new ETL rows become visible consistently. In this scenario: Running Delta `OPTIMIZE` with `V-Order`, dropping unused high-cardinality GUID/note columns, and orchestrating controlled post-ETL framing refreshes keep rowgroups and resident memory within SKU limits.

### Question 87 — A

Answer: Choose Direct Lake on SQL analytics endpoint (created from the SQL analytics endpoint using the Sql.Database M expression). `Direct Lake on SQL analytics endpoint` discovers tables/views via the SQL endpoint, supports Deployment Pipeline data-source rules, and honors SQL-based RLS/views via DirectQuery fallback (unlike Direct Lake on OneLake). Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. Local study-map skill 3.11 (Choose Between Direct Lake on OneLake and Direct Lake on SQL Analytics Endpoint (and Migrate via TMDL)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Direct Lake overview: Direct Lake on OneLake vs Direct Lake on SQL analytics endpoint (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview).

- **A:** Correct. Direct Lake on SQL binds to a single Fabric item's SQL analytics endpoint: choose it when the model must expose SQL views, honor SQL-based RLS/CLS via DirectQuery fallback, or rebind sources via Deployment Pipeline data source rules. In this scenario: `Direct Lake on SQL analytics endpoint` discovers tables/views via the SQL endpoint, supports Deployment Pipeline data-source rules, and honors SQL-based RLS/views via DirectQuery fallback (unlike Direct Lake on OneLake).
- **B:** Incorrect for this requirement. Direct Lake on OneLake connects directly to OneLake APIs without SQL analytics endpoint coupling: it supports combining tables across multiple Lakehouses/Warehouses/Eventhouses/Cosmos DB, enforces OneLake security OLS+RLS, supports composite Import tables, and never falls back to DirectQuery. Why the keyed choice wins: `Direct Lake on SQL analytics endpoint` discovers tables/views via the SQL endpoint, supports Deployment Pipeline data-source rules, and honors SQL-based RLS/views via DirectQuery fallback (unlike Direct Lake on OneLake).
- **C:** Incorrect for this requirement. Import mode loads compressed columnar data into VertiPaq RAM during scheduled refresh, delivering the fastest sub-second DAX engine capabilities across arbitrary non-OneLake connectors when sub-minute real-time latency is unnecessary. Why the keyed choice wins: `Direct Lake on SQL analytics endpoint` discovers tables/views via the SQL endpoint, supports Deployment Pipeline data-source rules, and honors SQL-based RLS/views via DirectQuery fallback (unlike Direct Lake on OneLake).
- **D:** Incorrect for this requirement. Direct Lake (both on OneLake and on SQL analytics endpoints) reads OneLake cloud storage directly and does not support operating through any On-premises or VNet data gateway. Why the keyed choice wins: `Direct Lake on SQL analytics endpoint` discovers tables/views via the SQL endpoint, supports Deployment Pipeline data-source rules, and honors SQL-based RLS/views via DirectQuery fallback (unlike Direct Lake on OneLake).

### Question 88 — D

Answer: Live edit the model in Power BI Desktop and save a Version history point → Script the semantic model in TMDL view → Replace Sql.Database(...) with AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...") → Apply TMDL and run framing refresh. Saving a Version history restore point while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and triggering a framing refresh upgrades the model cleanly. Correct order: take a version history checkpoint while live editing, script the model in TMDL view, swap the shared M expression from Sql.Database to AzureStorage.DataLake OneLake URL, apply changes, and frame. Local study-map skill 3.11 (Choose Between Direct Lake on OneLake and Direct Lake on SQL Analytics Endpoint (and Migrate via TMDL)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Direct Lake overview: Direct Lake on OneLake vs Direct Lake on SQL analytics endpoint (https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview).

- **A:** Incorrect for this requirement. Incorrect: Direct Lake models are live-edited in workspaces (not offline Personal Workspace Import files), and OleDb breaks OneLake Direct Lake connectivity. Why the keyed choice wins: Saving a Version history restore point while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and triggering a framing refresh upgrades the model cleanly.
- **B:** Incorrect for this requirement. Incorrect: Direct Lake on OneLake does not support non-materialized SQL views, DirectQuery fallback, or gateways. Why the keyed choice wins: Saving a Version history restore point while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and triggering a framing refresh upgrades the model cleanly.
- **C:** Incorrect for this requirement. Incorrect: deleting the semantic model breaks downstream thin reports and lineage, and granting Workspace Admin violates security. Why the keyed choice wins: Saving a Version history restore point while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and triggering a framing refresh upgrades the model cleanly.
- **D:** Correct. Correct order: take a version history checkpoint while live editing, script the model in TMDL view, swap the shared M expression from Sql.Database to AzureStorage.DataLake OneLake URL, apply changes, and frame. In this scenario: Saving a Version history restore point while live editing, scripting the model in TMDL view, replacing `Sql.Database(...)` with `AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/...")`, and triggering a framing refresh upgrades the model cleanly.

### Question 89 — C

Answer: Apply a Microsoft Purview sensitivity label with downstream inheritance on the source Lakehouse or Warehouse. Applying a Microsoft Purview sensitivity label with downstream inheritance (and file encryption) on the Gold Warehouse propagates classification automatically to dependent semantic models, reports, and Office exports. Sensitivity labels applied to Fabric Lakehouses, Warehouses, and Semantic Models automatically propagate downstream to newly connected semantic models, reports, and exported Excel/PDF/PPTX files when inheritance is enabled. Local study-map skill 1.4 (Apply Microsoft Purview Sensitivity Labels, Inheritance, Default/Mandatory Policies, and Export Encryption), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Information protection & sensitivity labels in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/service-security-sensitivity-label-overview).

- **A:** Incorrect for this requirement. cache.abf stores local cached VertiPaq data (often hundreds of MBs and potentially sensitive rows) and localSettings.json holds per-developer UI state; both must remain untracked in .gitignore. Why the keyed choice wins: Applying a Microsoft Purview sensitivity label with downstream inheritance (and file encryption) on the Gold Warehouse propagates classification automatically to dependent semantic models, reports, and Office exports.
- **B:** Incorrect for this requirement. Dynamic Data Masking obfuscates sensitive strings/emails/numbers in query results for users lacking UNMASK permission while keeping the column present so SELECT * queries do not fail. Why the keyed choice wins: Applying a Microsoft Purview sensitivity label with downstream inheritance (and file encryption) on the Gold Warehouse propagates classification automatically to dependent semantic models, reports, and Office exports.
- **C:** Correct. Sensitivity labels applied to Fabric Lakehouses, Warehouses, and Semantic Models automatically propagate downstream to newly connected semantic models, reports, and exported Excel/PDF/PPTX files when inheritance is enabled. In this scenario: Applying a Microsoft Purview sensitivity label with downstream inheritance (and file encryption) on the Gold Warehouse propagates classification automatically to dependent semantic models, reports, and Office exports.
- **D:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: Applying a Microsoft Purview sensitivity label with downstream inheritance (and file encryption) on the Gold Warehouse propagates classification automatically to dependent semantic models, reports, and Office exports.

### Question 90 — D

Answer: Request and apply Certified endorsement through a reviewer authorized in the Fabric Admin portal. `Certified` endorsement restricts badge assignment exclusively to security groups or reviewers explicitly authorized by a Fabric Administrator in tenant settings. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. Local study-map skill 1.5 (Endorse Items Using Promoted, Certified, and Master Data Governance Badges), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Endorsement (Promoted, Certified, Master data) in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview).

- **A:** Incorrect for this requirement. Any item owner or user with write permissions can Promote a semantic model, lakehouse, warehouse, or report to highlight it as ready for broader sharing without waiting for central governance review. Why the keyed choice wins: `Certified` endorsement restricts badge assignment exclusively to security groups or reviewers explicitly authorized by a Fabric Administrator in tenant settings.
- **B:** Incorrect for this requirement. A .pbids file standardizes how report authors connect Power BI Desktop to an approved Warehouse, SQL analytics endpoint, or semantic model without typing server URLs or choosing the wrong connector. Why the keyed choice wins: `Certified` endorsement restricts badge assignment exclusively to security groups or reviewers explicitly authorized by a Fabric Administrator in tenant settings.
- **C:** Incorrect for this requirement. Workspace Contributors can create, edit, and run notebooks, pipelines, lakehouses, warehouses, and semantic models inside the workspace, but cannot share items, update apps, or manage workspace/OneLake security role assignments — and they bypass RLS. Why the keyed choice wins: `Certified` endorsement restricts badge assignment exclusively to security groups or reviewers explicitly authorized by a Fabric Administrator in tenant settings.
- **D:** Correct. Certified endorsement requires explicit authorization granted by a Fabric Administrator to designated governance reviewers and signals that the asset meets strict organizational quality and security standards. In this scenario: `Certified` endorsement restricts badge assignment exclusively to security groups or reviewers explicitly authorized by a Fabric Administrator in tenant settings.

### Question 91 — D

Answer: Switch the workspace to Lineage view, open the Impact analysis side pane on the semantic model or Lakehouse, and select Notify contacts. Opening Workspace `Lineage` view, launching the `Impact analysis` side pane on the Warehouse, and using `Notify contacts` surfaces cross-workspace dependencies and messages every downstream owner. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. Local study-map skill 1.9 (Perform Downstream Dependency Impact Analysis Across Lakehouses, Warehouses, Dataflows, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Lineage and impact analysis in Microsoft Fabric workspaces (https://learn.microsoft.com/en-us/fabric/governance/lineage).

- **A:** Incorrect for this requirement. When Performance Analyzer shows tiny DAX query ms but multi-second Other times, the bottleneck is excessive visual/card count queuing on the page — solved by consolidating multi-measure matrices/KPI visuals and adding default slicer filters. Why the keyed choice wins: Opening Workspace `Lineage` view, launching the `Impact analysis` side pane on the Warehouse, and using `Notify contacts` surfaces cross-workspace dependencies and messages every downstream owner.
- **B:** Incorrect for this requirement. DAX INFO.VIEW.* functions and COLUMNSTATISTICS() self-document measures, storage modes, relationships, cardinality, and max string lengths directly via DAX without external DMV connections. Why the keyed choice wins: Opening Workspace `Lineage` view, launching the `Impact analysis` side pane on the Warehouse, and using `Notify contacts` surfaces cross-workspace dependencies and messages every downstream owner.
- **C:** Incorrect for this requirement. OneLake catalog replaces the legacy OneLake data hub with centralized Explore discovery (filtered by Domain, Endorsement, Item type, Tag) and a Govern view surfacing actionable data-stewardship recommendations. Why the keyed choice wins: Opening Workspace `Lineage` view, launching the `Impact analysis` side pane on the Warehouse, and using `Notify contacts` surfaces cross-workspace dependencies and messages every downstream owner.
- **D:** Correct. Fabric's Impact analysis panel enumerates all downstream workspaces, semantic models, dataflows, reports, and dashboards across the tenant that depend on the asset and sends targeted change alerts to item owners. In this scenario: Opening Workspace `Lineage` view, launching the `Impact analysis` side pane on the Warehouse, and using `Notify contacts` surfaces cross-workspace dependencies and messages every downstream owner.

### Question 92 — A

Answer: | summarize arg_max(IngestionTime, *) by SpecimenId. `| summarize arg_max(IngestionTime, *) by SpecimenId` selects the entire row carrying the newest `IngestionTime` for each `SpecimenId` in Eventhouse KQL. In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key. Local study-map skill 2.17 (Select, Filter, and Aggregate Data Using KQL (summarize, bin, arg_max, percentile, parse_json, mv-expand)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query data in a KQL queryset in Microsoft Fabric Real-Time Intelligence (https://learn.microsoft.com/en-us/fabric/real-time-intelligence/kql-queryset).

- **A:** Correct. In KQL, summarize arg_max(TimestampColumn, *) by KeyColumn returns the complete row corresponding to the maximum timestamp per key. In this scenario: `| summarize arg_max(IngestionTime, *) by SpecimenId` selects the entire row carrying the newest `IngestionTime` for each `SpecimenId` in Eventhouse KQL.
- **B:** Incorrect for this requirement. percentile(col, 99) paired with bin(EventTime, 5m) calculates streaming tail latency over fixed 5-minute windows in Eventhouse. Why the keyed choice wins: `| summarize arg_max(IngestionTime, *) by SpecimenId` selects the entire row carrying the newest `IngestionTime` for each `SpecimenId` in Eventhouse KQL.
- **C:** Incorrect for this requirement. mv-expand unpacks a dynamic JSON array into one output row per array element while preserving parent event columns. Why the keyed choice wins: `| summarize arg_max(IngestionTime, *) by SpecimenId` selects the entire row carrying the newest `IngestionTime` for each `SpecimenId` in Eventhouse KQL.
- **D:** Incorrect for this requirement. make-series builds regular gap-filled time-series arrays (filling empty 1-minute buckets with default = 0) required for KQL anomaly detection and trend functions; summarize by bin() omits empty buckets. Why the keyed choice wins: `| summarize arg_max(IngestionTime, *) by SpecimenId` selects the entire row carrying the newest `IngestionTime` for each `SpecimenId` in Eventhouse KQL.

### Question 93 — D

Answer: Use the Real-Time hub to subscribe to Microsoft.Fabric.OneLake.FileCreated events (or Capacity/CDC streams) and trigger an Activator rule. Subscribing in the Fabric Real-Time hub to `Microsoft.Fabric.OneLake.FileCreated` events on the `Files/inbound` folder and routing them via Activator triggers the pipeline immediately on file arrival. Real-Time hub unifies streaming sources, CDC feeds, Azure Blob events, and Fabric workspace/OneLake/Capacity events so analytics engineers can discover streams in one catalog and trigger event-driven pipelines or Notebooks via Activator. Local study-map skill 2.2 (Discover Data and Streams Using OneLake Catalog (Explore/Govern) and Real-Time Hub + Activator), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake catalog overview & Real-Time hub in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview).

- **A:** Incorrect for this requirement. Pipeline Copy activity is purpose-built for petabyte-scale, low-CU binary/tabular data movement without row-by-row transformation overhead. Why the keyed choice wins: Subscribing in the Fabric Real-Time hub to `Microsoft.Fabric.OneLake.FileCreated` events on the `Files/inbound` folder and routing them via Activator triggers the pipeline immediately on file arrival.
- **B:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: Subscribing in the Fabric Real-Time hub to `Microsoft.Fabric.OneLake.FileCreated` events on the `Files/inbound` folder and routing them via Activator triggers the pipeline immediately on file arrival.
- **C:** Incorrect for this requirement. The Visual query editor provides a low-code Power Query-like diagram canvas directly inside Warehouse and SQL analytics endpoints that compiles diagram steps to native T-SQL and can persist results as a SQL View without copying data. Why the keyed choice wins: Subscribing in the Fabric Real-Time hub to `Microsoft.Fabric.OneLake.FileCreated` events on the `Files/inbound` folder and routing them via Activator triggers the pipeline immediately on file arrival.
- **D:** Correct. Real-Time hub unifies streaming sources, CDC feeds, Azure Blob events, and Fabric workspace/OneLake/Capacity events so analytics engineers can discover streams in one catalog and trigger event-driven pipelines or Notebooks via Activator. In this scenario: Subscribing in the Fabric Real-Time hub to `Microsoft.Fabric.OneLake.FileCreated` events on the `Files/inbound` folder and routing them via Activator triggers the pipeline immediately on file arrival.

### Question 94 — C

Answer: Launch Data Wrangler from a Fabric Spark notebook (or enable Power Query Column profiling based on entire data set) to inspect nulls, duplicates, and distributions and export generated PySpark code. Launching Data Wrangler from a Fabric Spark notebook profiles distributions/missing values interactively and generates deterministic Python/PySpark transformation code. Power Query profiles only the top 1,000 rows by default unless switched to entire dataset, whereas Data Wrangler interactively profiles Pandas/Spark DataFrames and emits reproducible Python/PySpark cleaning code. Local study-map skill 2.12 (Identify and Resolve Duplicate Data, Missing Data, and Null Foreign Keys (ROW_NUMBER, -1 Unknown, Data Wrangler)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Clean, deduplicate, and profile data with Data Wrangler and Power Query (https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler).

- **A:** Incorrect for this requirement. By default Power Query profiles only the first 1,000 preview rows, completely missing duplicates, nulls, and data-type anomalies appearing later in multi-million-row partitions. Why the keyed choice wins: Launching Data Wrangler from a Fabric Spark notebook profiles distributions/missing values interactively and generates deterministic Python/PySpark transformation code.
- **B:** Incorrect for this requirement. df.collect() pulls distributed executor partitions onto the single driver node risking OutOfMemory crashes, while standard Python UDFs serialize rows across JVM-Python boundaries far slower than native Spark SQL functions. Why the keyed choice wins: Launching Data Wrangler from a Fabric Spark notebook profiles distributions/missing values interactively and generates deterministic Python/PySpark transformation code.
- **C:** Correct. Power Query profiles only the top 1,000 rows by default unless switched to entire dataset, whereas Data Wrangler interactively profiles Pandas/Spark DataFrames and emits reproducible Python/PySpark cleaning code. In this scenario: Launching Data Wrangler from a Fabric Spark notebook profiles distributions/missing values interactively and generates deterministic Python/PySpark transformation code.
- **D:** Incorrect for this requirement. Testing RLS/OLS with Test as role combined with a specific Viewer user's Entra UPN verifies both the DAX role predicate and the user's actual workspace/item permission level (catching the Contributor RLS-bypass trap). Why the keyed choice wins: Launching Data Wrangler from a Fabric Spark notebook profiles distributions/missing values interactively and generates deterministic Python/PySpark transformation code.

### Question 95 — A

Answer: ADD FILTER PREDICATE Security.fn_regionpredicate(RegionCode) ON dbo.FactSales WITH (STATE = ON). `ADD FILTER PREDICATE Security.fn_regionpredicate(...) ON ... WITH (STATE = ON)` binds an inline `SCHEMABINDING` predicate function directly to the Warehouse table. CREATE SECURITY POLICY ... ADD FILTER PREDICATE binds an inline table-valued security predicate function to a Warehouse or SQL analytics endpoint table to filter SELECT rows transparently. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Correct. CREATE SECURITY POLICY ... ADD FILTER PREDICATE binds an inline table-valued security predicate function to a Warehouse or SQL analytics endpoint table to filter SELECT rows transparently. In this scenario: `ADD FILTER PREDICATE Security.fn_regionpredicate(...) ON ... WITH (STATE = ON)` binds an inline `SCHEMABINDING` predicate function directly to the Warehouse table.
- **B:** Incorrect for this requirement. Dynamic DAX RLS filters rows at query time based on USERPRINCIPALNAME() (always returning the Entra UPN email, unlike USERNAME() which can return DOMAIN\user locally) and only restricts Workspace Viewers or App/shared consumers. Why the keyed choice wins: `ADD FILTER PREDICATE Security.fn_regionpredicate(...) ON ... WITH (STATE = ON)` binds an inline `SCHEMABINDING` predicate function directly to the Warehouse table.
- **C:** Incorrect for this requirement. OneLake security roles granting ReadWrite permission cannot contain RLS or CLS constraints; fine-grained row and column rules are supported only on Read roles. Why the keyed choice wins: `ADD FILTER PREDICATE Security.fn_regionpredicate(...) ON ... WITH (STATE = ON)` binds an inline `SCHEMABINDING` predicate function directly to the Warehouse table.
- **D:** Incorrect for this requirement. Fabric Data Warehouse supports FILTER PREDICATE with inline TVFs (not stored procedures or SQL Server DML BLOCK PREDICATE triggers). Why the keyed choice wins: `ADD FILTER PREDICATE Security.fn_regionpredicate(...) ON ... WITH (STATE = ON)` binds an inline `SCHEMABINDING` predicate function directly to the Warehouse table.

### Question 96 — B

Answer: MASKED WITH (FUNCTION = 'partial(0,"XXX-XX-",4)'). `MASKED WITH (FUNCTION = 'partial(0,"XXX-XX-",4)')` applies T-SQL Dynamic Data Masking so `SELECT *` succeeds while masking leading characters for callers without `UNMASK`. The T-SQL Dynamic Data Masking partial(prefix, padding, suffix) function exposes only the last four characters while masking leading digits for callers without UNMASK permission. Local study-map skill 1.3 (Implement Row-Level, Column-Level, Object-Level, and File-Level Access Control Across OneLake, SQL, and Semantic Models), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: OneLake security roles (RLS, CLS, OLS, folders) & SQL granular permissions (https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

- **A:** Incorrect for this requirement. In Fabric Warehouse and SQL analytics endpoints, column-level security restricts users to explicitly permitted columns via column-scoped GRANT SELECT without creating duplicate views or physical tables. Why the keyed choice wins: `MASKED WITH (FUNCTION = 'partial(0,"XXX-XX-",4)')` applies T-SQL Dynamic Data Masking so `SELECT *` succeeds while masking leading characters for callers without `UNMASK`.
- **B:** Correct. The T-SQL Dynamic Data Masking partial(prefix, padding, suffix) function exposes only the last four characters while masking leading digits for callers without UNMASK permission. In this scenario: `MASKED WITH (FUNCTION = 'partial(0,"XXX-XX-",4)')` applies T-SQL Dynamic Data Masking so `SELECT *` succeeds while masking leading characters for callers without `UNMASK`.
- **C:** Incorrect for this requirement. Semantic model OLS completely hides restricted tables or columns (including metadata and referencing measures, making them behave as if they do not exist) from unauthorized roles, whereas Display Hidden merely hides UI visibility. Why the keyed choice wins: `MASKED WITH (FUNCTION = 'partial(0,"XXX-XX-",4)')` applies T-SQL Dynamic Data Masking so `SELECT *` succeeds while masking leading characters for callers without `UNMASK`.
- **D:** Incorrect for this requirement. Hiding a column in Model view is purely a report-authoring UX convenience — users with Build permission, Analyze in Excel, DAX Query View, or Personalize visuals can still query hidden columns. Why the keyed choice wins: `MASKED WITH (FUNCTION = 'partial(0,"XXX-XX-",4)')` applies T-SQL Dynamic Data Masking so `SELECT *` succeeds while masking leading characters for callers without `UNMASK`.

### Question 97 — D

Answer: OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000'). `OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')` queries historical Fabric Warehouse snapshots in place via T-SQL Time Travel. Fabric Data Warehouse Time Travel uses the query hint OPTION (FOR TIMESTAMP AS OF 'YYYY-MM-DDTHH:MM:SS.fff') to read exact point-in-time historical snapshots within the retention window. Local study-map skill 2.16 (Select, Filter, and Aggregate Data Using SQL (Window Functions, 3-Part Cross-DB Queries, Time Travel & Clone)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Query the SQL analytics endpoint or Warehouse (T-SQL windowing, cross-DB, Time Travel & Clone) (https://learn.microsoft.com/en-us/fabric/data-warehouse/query-warehouse).

- **A:** Incorrect for this requirement. Full-table 15-minute reloads waste massive Fabric Capacity Units (CUs) and cause throttling compared to watermark/CDC incremental pipelines or Database Mirroring. Why the keyed choice wins: `OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')` queries historical Fabric Warehouse snapshots in place via T-SQL Time Travel.
- **B:** Incorrect for this requirement. LAG(col, 1, 0) retrieves the immediately preceding hour's value within each SubstationId partition, defaulting the first row to 0. Why the keyed choice wins: `OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')` queries historical Fabric Warehouse snapshots in place via T-SQL Time Travel.
- **C:** Incorrect for this requirement. FOR SYSTEM_TIME AS OF is SQL Server temporal-table syntax requiring explicit PERIOD FOR SYSTEM_TIME history tables; Fabric Warehouse Time Travel uses OPTION (FOR TIMESTAMP AS OF ...). Why the keyed choice wins: `OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')` queries historical Fabric Warehouse snapshots in place via T-SQL Time Travel.
- **D:** Correct. Fabric Data Warehouse Time Travel uses the query hint OPTION (FOR TIMESTAMP AS OF 'YYYY-MM-DDTHH:MM:SS.fff') to read exact point-in-time historical snapshots within the retention window. In this scenario: `OPTION (FOR TIMESTAMP AS OF '2026-10-28T06:00:00.000')` queries historical Fabric Warehouse snapshots in place via T-SQL Time Travel.

### Question 98 — B

Answer: CALCULATE([Encounter Count], CROSSFILTER('FactEncounter'[EncounterKey], 'BridgeEncounterDiag'[EncounterKey], BOTH)). `CALCULATE([Encounter Count], CROSSFILTER('FactEncounter'[EncounterKey], 'BridgeEncounterDiag'[EncounterKey], BOTH))` scopes bidirectional bridge propagation strictly to that measure. CROSSFILTER(..., BOTH) enables bidirectional filter propagation across a bridge table only inside the specific measure rather than globally across the model. Local study-map skill 3.3 (Implement Relationships Including Role-Playing USERELATIONSHIP, Bridge Tables, Many-to-Many, and Referential Integrity), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Model relationships, USERELATIONSHIP, bridge tables, and many-to-many guidance (https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many).

- **A:** Incorrect for this requirement. USERELATIONSHIP activates an inactive 1:* relationship strictly for the duration of the CALCULATE evaluation. Why the keyed choice wins: `CALCULATE([Encounter Count], CROSSFILTER('FactEncounter'[EncounterKey], 'BridgeEncounterDiag'[EncounterKey], BOTH))` scopes bidirectional bridge propagation strictly to that measure.
- **B:** Correct. CROSSFILTER(..., BOTH) enables bidirectional filter propagation across a bridge table only inside the specific measure rather than globally across the model. In this scenario: `CALCULATE([Encounter Count], CROSSFILTER('FactEncounter'[EncounterKey], 'BridgeEncounterDiag'[EncounterKey], BOTH))` scopes bidirectional bridge propagation strictly to that measure.
- **C:** Incorrect for this requirement. Assume referential integrity causes DirectQuery to emit faster SQL INNER JOIN statements instead of OUTER JOIN statements, which requires validated non-null foreign keys in the fact table. Why the keyed choice wins: `CALCULATE([Encounter Count], CROSSFILTER('FactEncounter'[EncounterKey], 'BridgeEncounterDiag'[EncounterKey], BOTH))` scopes bidirectional bridge propagation strictly to that measure.
- **D:** Incorrect for this requirement. Enabling permanent bidirectional cross-filtering across multiple fact/dimension paths creates ambiguous relationship loops, unpredictable DAX filter propagation, and severe Formula Engine slowdowns. Why the keyed choice wins: `CALCULATE([Encounter Count], CROSSFILTER('FactEncounter'[EncounterKey], 'BridgeEncounterDiag'[EncounterKey], BOTH))` scopes bidirectional bridge propagation strictly to that measure.

### Question 99 — A

Answer: CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC))). `CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC)))` steps backward one custom sorted period using DAX windowing. OFFSET(-1, ..., ORDERBY(...)) shifts one period backward along a custom 4-4-5 fiscal sort column where standard Gregorian DATEADD fails. Local study-map skill 3.4 (Write DAX Calculations Using Variables (VAR), Iterators (SUMX), Filter Modifiers (KEEPFILTERS), Windowing (OFFSET/WINDOW), and ISINSCOPE), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: DAX variables, iterators, filter modifiers, and window functions (OFFSET, INDEX, WINDOW) (https://learn.microsoft.com/en-us/dax/dax-overview).

- **A:** Correct. OFFSET(-1, ..., ORDERBY(...)) shifts one period backward along a custom 4-4-5 fiscal sort column where standard Gregorian DATEADD fails. In this scenario: `CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC)))` steps backward one custom sorted period using DAX windowing.
- **B:** Incorrect for this requirement. ISINSCOPE('DimProduct'[SKU]) evaluates TRUE only when SKU is actively grouping the visual hierarchy level, suppressing misleading margin figures at subtotal rows. Why the keyed choice wins: `CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC)))` steps backward one custom sorted period using DAX windowing.
- **C:** Incorrect for this requirement. Auto date/time generates 18 separate hidden calculated date hierarchies, inflating memory footprint and preventing a single slicer from filtering OrderDate, ShipDate, and InvoiceDate consistently. Why the keyed choice wins: `CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC)))` steps backward one custom sorted period using DAX windowing.
- **D:** Incorrect for this requirement. Inside a Calculation Group item, SELECTEDMEASURE() dynamically substitutes whichever base measure is currently evaluated in the visual. Why the keyed choice wins: `CALCULATE([Net Revenue], OFFSET(-1, ALLSELECTED('Calendar'[FiscalPeriod], 'Calendar'[FiscalPeriodSort]), ORDERBY('Calendar'[FiscalPeriodSort], ASC)))` steps backward one custom sorted period using DAX windowing.

### Question 100 — C

Answer: Create case-sensitive DateTime parameters RangeStart and RangeEnd → Apply foldable half-open filter (>= RangeStart and < RangeEnd) → Configure table Incremental refresh policy → Publish to workspace and run initial refresh to generate partitions. Defining `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the incremental policy (`Detect data changes` on `LastUpdatedUTC`), and publishing for initial partition creation implements it cleanly. Correct order: define DateTime RangeStart/RangeEnd parameters, apply >= RangeStart and < RangeEnd preserving query folding, configure table incremental policy, and publish so Fabric generates historical and incremental partitions. Local study-map skill 3.12 (Implement Incremental Refresh and Hybrid Real-Time Partitions (RangeStart/RangeEnd, Detect Data Changes)), aligned to the official DP-600 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600). Primary reference: Configure incremental refresh and real-time data for Power BI semantic models (https://learn.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-overview).

- **A:** Incorrect for this requirement. Incorrect: parameter names/types must be exact DateTime RangeStart and RangeEnd, breaking query folding pulls the entire table on every refresh, and <= on both bounds double-counts midnight rows. Why the keyed choice wins: Defining `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the incremental policy (`Detect data changes` on `LastUpdatedUTC`), and publishing for initial partition creation implements it cleanly.
- **B:** Incorrect for this requirement. Incorrect: importing 2 billion rows locally crashes Desktop before partitioning exists, RangeStart belongs in Power Query M, and Incremental Refresh partitions apply to Import/Hybrid tables rather than Direct Lake. Why the keyed choice wins: Defining `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the incremental policy (`Detect data changes` on `LastUpdatedUTC`), and publishing for initial partition creation implements it cleanly.
- **C:** Correct. Correct order: define DateTime RangeStart/RangeEnd parameters, apply >= RangeStart and < RangeEnd preserving query folding, configure table incremental policy, and publish so Fabric generates historical and incremental partitions. In this scenario: Defining `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the incremental policy (`Detect data changes` on `LastUpdatedUTC`), and publishing for initial partition creation implements it cleanly.
- **D:** Incorrect for this requirement. Incorrect: Detect data changes requires an audit/update timestamp column distinct from the date column used to partition RangeStart/RangeEnd. Why the keyed choice wins: Defining `DateTime` `RangeStart`/`RangeEnd` parameters, applying foldable `>= RangeStart and < RangeEnd` filters, configuring the incremental policy (`Detect data changes` on `LastUpdatedUTC`), and publishing for initial partition creation implements it cleanly.
